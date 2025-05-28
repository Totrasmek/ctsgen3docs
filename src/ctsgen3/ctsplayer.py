from crc import Calculator, Configuration
import numpy as np
import matplotlib.pyplot
import matplotlib.animation
import ctypes  # Data format
from typing import List
from ctsgen3.spi.spi import (
    PIXEL_HEIGHT,
    PIXEL_WIDTH,
    CRC_POLYNOMIAL,
    CRC_INITIAL_VALUE,
    SpiPacket,
)

import ft4222


if __name__ == "__main__":
    ################Serial Config################
    devA = ft4222.openByDescription("FT4222 A")
    devA.setClock(ft4222.SysClock.CLK_60)
    devA.spiMaster_Init(
        ft4222.SPIMaster.Mode.SINGLE,
        ft4222.SPIMaster.Clock.DIV_32,
        ft4222.SPI.Cpol.IDLE_HIGH,
        ft4222.SPI.Cpha.CLK_LEADING,
        ft4222.SPIMaster.SlaveSelect.SS0,
    )
    #################Plot Config#################
    fig, (ax1, ax2) = matplotlib.pyplot.subplots(1, 2, figsize=(15, 10))
    heatmap = ax1.imshow(np.zeros((PIXEL_HEIGHT, PIXEL_WIDTH)), cmap="jet", interpolation="nearest")
    colorbar = matplotlib.pyplot.colorbar(heatmap, ax=ax1, label="Temperature")
    ax1.set_title("Thermal Heatmap")
    ax1.set_xlabel("Columns")
    ax1.set_ylabel("Rows")
    cv_foreground_heatmap = ax2.imshow(np.zeros((PIXEL_HEIGHT, PIXEL_WIDTH)), cmap="jet", interpolation="nearest")
    colorbar2 = matplotlib.pyplot.colorbar(cv_foreground_heatmap, ax=ax2, label="CV foreground")
    ax2.set_title("CV Foreground")
    ax2.set_xlabel("Columns")
    ax2.set_ylabel("Rows")
    #################CRC Config##################
    config = Configuration(
        width=16,
        polynomial=CRC_POLYNOMIAL,
        init_value=CRC_INITIAL_VALUE,
        final_xor_value=0x00,
        reverse_input=False,
        reverse_output=False,
    )
    crc_calculator = Calculator(config)

    def update(
        frame: int,
    ) -> List[matplotlib.artist.Artist]:  # function for matplotlib animation updates
        spi_packet = SpiPacket.from_buffer_copy(
            devA.spiMaster_SingleReadWrite(bytes([0] * ctypes.sizeof(SpiPacket)), True)
        )
        crc_data = ctypes.string_at(
            ctypes.addressof(spi_packet.thermal_frame),
            ctypes.sizeof(spi_packet.thermal_frame) - ctypes.sizeof(ctypes.c_uint16),
        )
        crc_computed = crc_calculator.checksum(crc_data)
        if crc_computed != spi_packet.thermal_frame.crc:
            print("⚠️ Thermal CRC fail.\n" f"Got: {spi_packet.thermal_frame.crc}\n" f"Expected: {crc_computed}")
            return [heatmap, cv_foreground_heatmap]
        crc_data = ctypes.string_at(
            ctypes.addressof(spi_packet.cv_foreground),
            ctypes.sizeof(spi_packet.cv_foreground) - ctypes.sizeof(ctypes.c_uint16),
        )
        crc_computed = crc_calculator.checksum(crc_data)
        if crc_computed != spi_packet.cv_foreground.crc:
            print("⚠️ Foreground CRC fail.\n" f"Got: {spi_packet.cv_foreground.crc}\n" f"Expected: {crc_computed}")
            return [heatmap, cv_foreground_heatmap]
        crc_data = ctypes.string_at(
            ctypes.addressof(spi_packet.cv_detections),
            ctypes.sizeof(spi_packet.cv_detections) - ctypes.sizeof(ctypes.c_uint16),
        )
        crc_computed = crc_calculator.checksum(crc_data)
        if crc_computed != spi_packet.cv_detections.crc:
            print("⚠️ Detections CRC fail.\n" f"Got: {spi_packet.cv_detections.crc}\n" f"Expected: {crc_computed}")
            return [heatmap, cv_foreground_heatmap]
        crc_data = ctypes.string_at(
            ctypes.addressof(spi_packet.metadata),
            ctypes.sizeof(spi_packet.metadata) - ctypes.sizeof(ctypes.c_uint16),
        )
        crc_computed = crc_calculator.checksum(crc_data)
        if crc_computed != spi_packet.metadata.crc:
            print("⚠️ Metadata CRC fail.\n" f"Got: {spi_packet.metadata.crc}\n" f"Expected: {crc_computed}")
            return [heatmap, cv_foreground_heatmap]
        ###############Print CV detections################
        print()
        print("detections:")
        for detection in spi_packet.cv_detections.cv_detections:
            print(detection)
        ###############Update heatmap################
        ir_frame_np = (
            np.ctypeslib.as_array(spi_packet.thermal_frame.thermal_frame).astype(np.float32) / 256.0
        ).reshape((PIXEL_HEIGHT, PIXEL_WIDTH))
        heatmap.set_data(ir_frame_np)
        heatmap.set_clim(vmin=ir_frame_np.min(), vmax=ir_frame_np.max())  # Normalize color scale
        cv_foreground_np = (
            np.ctypeslib.as_array(spi_packet.cv_foreground.cv_foreground).astype(np.float32) / 256.0
        ).reshape((PIXEL_HEIGHT, PIXEL_WIDTH))
        cv_foreground_heatmap.set_data(cv_foreground_np)
        cv_foreground_heatmap.set_clim(vmin=-7, vmax=7)
        fig.canvas.draw_idle()
        return [heatmap, cv_foreground_heatmap]

    ani = matplotlib.animation.FuncAnimation(fig, update, interval=250, cache_frame_data=False)
    matplotlib.pyplot.show()
    devA.close()
