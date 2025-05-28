import ft4222
from crc import Calculator, Configuration
from ctsgen3.registers.registers import RegisterMap
import ctypes

#################SPI output################
# these should go somewhere else later...
PIXEL_HEIGHT = 15
"""
Thermal image pixel height.
"""
PIXEL_WIDTH = 20
"""
Thermal image pixel width.
"""
MAX_NUM_DETECTIONS = 21
"""
Maximum number of detections
"""
CRC_POLYNOMIAL = 0x1021
CRC_INITIAL_VALUE = 0xFFFF


class CvDetection(ctypes.LittleEndianStructure):
    """
    CV algorithm outputs for each detected heat blob.
    """

    _fields_ = [
        ("id", ctypes.c_uint8),
        ("label", ctypes.c_uint8),
        ("temperature_centre_location_x", ctypes.c_uint8),
        ("temperature_centre_location_y", ctypes.c_uint8),
        ("frames_since_motion", ctypes.c_uint32),
        ("peak_temperature", ctypes.c_float),
        ("foot_position_estimate_x", ctypes.c_float),
        ("foot_position_estimate_y", ctypes.c_float),
    ]
    _pack_ = 1

    def __repr__(self) -> str:
        fields = [f"{name}={getattr(self, name)!r}" for field in self._fields_ for name in [field[0]]]
        return f"{self.__class__.__name__}({', '.join(fields)})"


class SpiThermalPacket(ctypes.LittleEndianStructure):
    """
    SPI bulk data thermal frame packet.
    """

    _fields_ = [
        ("thermal_frame", ctypes.c_int16 * (PIXEL_HEIGHT * PIXEL_WIDTH)),
        ("crc", ctypes.c_uint16),
    ]
    _pack_ = 1


class SpiMetadataPacket(ctypes.LittleEndianStructure):
    """
    SPI bulk data metadata packet.
    """

    _fields_ = [
        ("metadata", RegisterMap),
        ("crc", ctypes.c_uint16),
    ]
    _pack_ = 1


class SpiCvForegroundPacket(ctypes.LittleEndianStructure):
    """
    SPI bulk data CV foreground packet.
    """

    _fields_ = [
        ("cv_foreground", ctypes.c_int16 * (PIXEL_HEIGHT * PIXEL_WIDTH)),
        ("crc", ctypes.c_uint16),
    ]
    _pack_ = 1


class SpiCvDetectionsPacket(ctypes.LittleEndianStructure):
    """
    SPI bulk data CV detections packet.
    """

    _fields_ = [
        ("cv_detections", CvDetection * MAX_NUM_DETECTIONS),
        ("crc", ctypes.c_uint16),
    ]
    _pack_ = 1


class SpiPacket(ctypes.LittleEndianStructure):
    """
    Full SpiPacket when all sections are configured via command and control I2C interface.
    """

    _fields_ = [
        ("thermal_frame", SpiThermalPacket),
        ("metadata", SpiMetadataPacket),
        ("cv_foreground", SpiCvForegroundPacket),
        ("cv_detections", SpiCvDetectionsPacket),
    ]
    _pack_ = 1


if __name__ == "__main__":
    devA = ft4222.openByDescription("FT4222 A")
    devA.setClock(ft4222.SysClock.CLK_60)
    devA.spiMaster_Init(
        ft4222.SPIMaster.Mode.SINGLE,
        ft4222.SPIMaster.Clock.DIV_16,
        ft4222.SPI.Cpol.IDLE_HIGH,
        ft4222.SPI.Cpha.CLK_LEADING,
        ft4222.SPIMaster.SlaveSelect.SS0,
    )  # initialisation asserts CS briefly, triggering an internal buffer reset
    config = Configuration(
        width=16,
        polynomial=CRC_POLYNOMIAL,
        init_value=CRC_INITIAL_VALUE,
        final_xor_value=0x00,
        reverse_input=False,
        reverse_output=False,
    )
    crc_calculator = Calculator(config)
    for i in range(0, 100000):
        rx = devA.spiMaster_SingleReadWrite(bytes(2500 * [0]), True)
        spi_packet = SpiPacket.from_buffer_copy(rx)
        crc_data = ctypes.string_at(
            ctypes.addressof(spi_packet.thermal_frame),
            ctypes.sizeof(spi_packet.thermal_frame) - ctypes.sizeof(ctypes.c_uint16),
        )
        crc_computed = crc_calculator.checksum(crc_data)
        if crc_computed != spi_packet.thermal_frame.crc:
            print("⚠️ Thermal CRC fail.\n" f"Got: {spi_packet.thermal_frame.crc}\n" f"Expected: {crc_computed}")
        crc_data = ctypes.string_at(
            ctypes.addressof(spi_packet.cv_foreground),
            ctypes.sizeof(spi_packet.cv_foreground) - ctypes.sizeof(ctypes.c_uint16),
        )
        crc_computed = crc_calculator.checksum(crc_data)
        if crc_computed != spi_packet.cv_foreground.crc:
            print("⚠️ Foreground CRC fail.\n" f"Got: {spi_packet.cv_foreground.crc}\n" f"Expected: {crc_computed}")
        crc_data = ctypes.string_at(
            ctypes.addressof(spi_packet.cv_detections),
            ctypes.sizeof(spi_packet.cv_detections) - ctypes.sizeof(ctypes.c_uint16),
        )
        crc_computed = crc_calculator.checksum(crc_data)
        if crc_computed != spi_packet.cv_detections.crc:
            print("⚠️ Detections CRC fail.\n" f"Got: {spi_packet.cv_detections.crc}\n" f"Expected: {crc_computed}")
        crc_data = ctypes.string_at(
            ctypes.addressof(spi_packet.metadata),
            ctypes.sizeof(spi_packet.metadata) - ctypes.sizeof(ctypes.c_uint16),
        )
        crc_computed = crc_calculator.checksum(crc_data)
        if crc_computed != spi_packet.metadata.crc:
            print("⚠️ Metadata CRC fail.\n" f"Got: {spi_packet.metadata.crc}\n" f"Expected: {crc_computed}")
