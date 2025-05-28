import ctypes
from enum import IntEnum

############Metadata registers#############
NUM_REGISTERS = 64


class TEMP_SENSOR_0x00(ctypes.LittleEndianStructure):
    """
    Temperature of CMOS Image Sensor (CIS) dynamically updated every frame.

    The temperature is an <8,8> fixed point number.
    """

    _fields_ = [
        ("temperature_sensor_0", ctypes.c_int16),
        ("_unimplemented", ctypes.c_int16),
    ]
    _pack_ = 1


assert ctypes.sizeof(TEMP_SENSOR_0x00) == ctypes.sizeof(ctypes.c_uint32)


class LED_LIFETIME_0x01(ctypes.LittleEndianStructure):
    """
    Accumulated service time of the CTS since initial configuration, in minutes.
    """

    _fields_ = [("minutes", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(LED_LIFETIME_0x01) == ctypes.sizeof(ctypes.c_uint32)


class GLOBAL_FRM_CNT_0x02(ctypes.LittleEndianStructure):
    """
    Number of thermal frames captured since reset.
    """

    _fields_ = [("frame_count", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(GLOBAL_FRM_CNT_0x02) == ctypes.sizeof(ctypes.c_uint32)


class RESERVED_0x03_0x04(ctypes.LittleEndianStructure):
    """
    Reserved.
    """

    _fields_ = [("_reserved0", ctypes.c_uint32), ("_reserved1", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(RESERVED_0x03_0x04) == 2 * ctypes.sizeof(ctypes.c_uint32)


class EXPOSURE_0x05(ctypes.LittleEndianStructure):
    """
    CIS exposure.
    """

    _fields_ = [("exposure", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(EXPOSURE_0x05) == ctypes.sizeof(ctypes.c_uint32)


class LUMINOSITY_0x06(ctypes.LittleEndianStructure):
    """
    Accumulated luminosity dynamically updated every frame.
    """

    _fields_ = [("luminosity", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(LUMINOSITY_0x06) == ctypes.sizeof(ctypes.c_uint32)


class IS_TEMP_0x07(ctypes.LittleEndianStructure):
    """
    Averaged CIS measured temperature. !!! we doing this?
    """

    _fields_ = [("image_sensor_temp", ctypes.c_int32)]
    _pack_ = 1


assert ctypes.sizeof(IS_TEMP_0x07) == ctypes.sizeof(ctypes.c_uint32)


class LINEAR_COMP_INST_0x08(ctypes.LittleEndianStructure):
    """
    Linear compensation for current frame.
    """

    _fields_ = [("linear_comp_inst", ctypes.c_int32)]
    _pack_ = 1


assert ctypes.sizeof(LINEAR_COMP_INST_0x08) == ctypes.sizeof(ctypes.c_uint32)


class LINEAR_COMP_AVG_0x09(ctypes.LittleEndianStructure):
    """
    Moving average for linear compensation (16 frames).
    """

    _fields_ = [("linear_comp_avg", ctypes.c_int32)]
    _pack_ = 1


assert ctypes.sizeof(LINEAR_COMP_AVG_0x09) == ctypes.sizeof(ctypes.c_uint32)


class SHIELDED_COMP_INST_0x0A(ctypes.LittleEndianStructure):
    """
    Shielded compensation for current frame.
    """

    _fields_ = [("shielded_comp_inst", ctypes.c_int32)]
    _pack_ = 1


assert ctypes.sizeof(SHIELDED_COMP_INST_0x0A) == ctypes.sizeof(ctypes.c_uint32)


class SHIELDED_COMP_AVG_0x0B(ctypes.LittleEndianStructure):
    """
    Moving average for shielded pixel compensation (16 frames).
    """

    _fields_ = [("shielded_comp_avg", ctypes.c_int32)]
    _pack_ = 1


assert ctypes.sizeof(SHIELDED_COMP_AVG_0x0B) == ctypes.sizeof(ctypes.c_uint32)


class MAGNIFICATION_COMP_INST_0x0C(ctypes.LittleEndianStructure):
    """
    Unimplemented.
    """

    _fields_ = [("_unimplemented", ctypes.c_int32)]
    _pack_ = 1


assert ctypes.sizeof(MAGNIFICATION_COMP_INST_0x0C) == ctypes.sizeof(ctypes.c_uint32)


class MAGNIFICATION_COMP_AVG_0x0D(ctypes.LittleEndianStructure):
    """
    Unimplemented.
    """

    _fields_ = [("_unimplemented", ctypes.c_int32)]
    _pack_ = 1


assert ctypes.sizeof(MAGNIFICATION_COMP_AVG_0x0D) == ctypes.sizeof(ctypes.c_uint32)


class GRAV_COMP_0x0E(ctypes.LittleEndianStructure):
    """
    Unimplemented.
    """

    _fields_ = [("_unimplemented", ctypes.c_int32)]
    _pack_ = 1


assert ctypes.sizeof(GRAV_COMP_0x0E) == ctypes.sizeof(ctypes.c_uint32)


class WARMUP_COMP_0x0F(ctypes.LittleEndianStructure):
    """
    Unimplemented.
    """

    _fields_ = [("_unimplemented", ctypes.c_int32)]
    _pack_ = 1


assert ctypes.sizeof(WARMUP_COMP_0x0F) == ctypes.sizeof(ctypes.c_uint32)


class LONG_TERM_COMP_0x10(ctypes.LittleEndianStructure):
    """
    Unimplemented.
    """

    _fields_ = [("_unimplemented", ctypes.c_int32)]
    _pack_ = 1


assert ctypes.sizeof(LONG_TERM_COMP_0x10) == ctypes.sizeof(ctypes.c_uint32)


class STRAY_LIGHT_COMP_0x11(ctypes.LittleEndianStructure):
    """
    Unimplemented.
    """

    _fields_ = [("_unimplemented", ctypes.c_int32)]
    _pack_ = 1


assert ctypes.sizeof(STRAY_LIGHT_COMP_0x11) == ctypes.sizeof(ctypes.c_uint32)


class RESERVED_0x12_0x13(ctypes.LittleEndianStructure):  # 0x12 - 0x13
    """
    Unimplemented.
    """

    _fields_ = [("_reserved0", ctypes.c_uint32), ("_reserved1", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(RESERVED_0x12_0x13) == (0x13 - 0x12 + 1) * ctypes.sizeof(ctypes.c_uint32)


class SERIAL_NUMBER_LO_0x14(ctypes.LittleEndianStructure):
    """
    Lower word of device serial number.
    """

    _fields_ = [("serial_lo", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(SERIAL_NUMBER_LO_0x14) == ctypes.sizeof(ctypes.c_uint32)


class SERIAL_NUMBER_HI_0x15(ctypes.LittleEndianStructure):
    """
    Upper word of device serial number.
    """

    _fields_ = [("serial_hi", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(SERIAL_NUMBER_HI_0x15) == ctypes.sizeof(ctypes.c_uint32)


class FW_VERSION_0x16(ctypes.LittleEndianStructure):
    """
    Firmware semantic version.
    """

    _fields_ = [
        ("ver_patch", ctypes.c_uint8),
        ("ver_minor", ctypes.c_uint8),
        ("ver_major", ctypes.c_uint8),
        ("_reserved", ctypes.c_uint8),
    ]
    _pack_ = 1


assert ctypes.sizeof(FW_VERSION_0x16) == ctypes.sizeof(ctypes.c_uint32)


class FOV_LENS_0x17(ctypes.LittleEndianStructure):
    """
    FOV lens identifier.
    """

    _fields_ = [
        ("lens_index", ctypes.c_uint32, 6),  # bit   0 -  5
        ("assembly_type_generation_index", ctypes.c_uint32, 6),  # bit   6 - 11
        ("lens_material_index", ctypes.c_uint32, 4),  # bit  12 - 15
        ("config_type_index", ctypes.c_uint32, 6),  # bit  16 - 21
        ("metadata_version", ctypes.c_uint32, 5),  # bit  22 - 26
        ("die_type_index", ctypes.c_uint32, 5),
    ]  # bit  27 - 31
    _pack_ = 1


assert ctypes.sizeof(FOV_LENS_0x17) == ctypes.sizeof(ctypes.c_uint32)


class DECENTRATION_0x18(ctypes.LittleEndianStructure):
    """
    Lens centration point as <10,3> fixed point numbers, and the row and column start indices for cropping.
    """

    _fields_ = [
        ("centre_x", ctypes.c_uint32, 10),  # bit   0 -  9
        ("centre_y", ctypes.c_uint32, 10),  # bit  10 - 19
        ("column_start", ctypes.c_uint32, 6),  # bit  20 - 25
        ("row_start", ctypes.c_uint32, 6),  # bit  26 - 31
    ]
    _pack_ = 1


assert ctypes.sizeof(DECENTRATION_0x18) == ctypes.sizeof(ctypes.c_uint32)


class CALIB_PARAMS_0x19(ctypes.LittleEndianStructure):
    """
    !!! Matt can you provide a description?
    """

    _fields_ = [("calib_params", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(CALIB_PARAMS_0x19) == ctypes.sizeof(ctypes.c_uint32)


class RESERVED_0x1A_0x1E(ctypes.LittleEndianStructure):  # 0x1A - 0x1E
    """
    Unimplemented.
    """

    _fields_ = [
        ("_reserved0", ctypes.c_uint32),
        ("_reserved1", ctypes.c_uint32),
        ("_reserved0", ctypes.c_uint32),
        ("_reserved0", ctypes.c_uint32),
        ("_reserved0", ctypes.c_uint32),
    ]
    _pack_ = 1


assert ctypes.sizeof(RESERVED_0x1A_0x1E) == (0x1E - 0x1A + 1) * ctypes.sizeof(ctypes.c_uint32)


class CIS_frame_rate_enum(IntEnum):
    """
    CIS FPS settings which populate `FRAME_RATE_MODE` in [CTS_CTRL_0x1F][ctsgen3.registers.registers.CTS_CTRL_0x1F]
    """

    FPS_60 = 0  #: 60 FPS (default)
    FPS_32 = 1  #: 32 FPS
    FPS_8 = 2  #: 8 FPS
    FPS_1 = 3  #: 1 FPS


class CTS_CTRL_0x1F(ctypes.LittleEndianStructure):
    """
    Flags enabling image processing techniques, # frames used to average (2^NUM_FRAMES_TO_AVG), frame rate (FRAME_RATE_MODE as CIS_frame_rate)
    """

    _fields_ = [
        # !!! Matt can you review?
        # remove/rethink disable_img_proc, disable i2c_poll? put as unimplemented?
        # make frames to avg and frame rate read only
        # test patterns enabled? put as unimplemented?
        ("EXPOSURE_CTRL_ENABLE_BIT", ctypes.c_uint32, 1),  # bit   0
        ("BAD_PIXEL_ENABLE_BIT", ctypes.c_uint32, 1),  # bit   1
        ("_reserved2", ctypes.c_uint32, 1),  # bit   2
        ("_reserved3", ctypes.c_uint32, 1),  # bit   3
        ("LINEAR_COMP_ENABLE_BIT", ctypes.c_uint32, 1),  # bit   4
        ("DX_CENTROID_ENABLE_BIT", ctypes.c_uint32, 1),  # bit   5
        ("_reserved6", ctypes.c_uint32, 1),  # bit   6
        ("SHIELDED_COMP_ENABLE_BIT", ctypes.c_uint32, 1),  # bit   7
        ("NUM_FRAMES_TO_AVG", ctypes.c_uint32, 3),  # bits  8 - 10
        ("_reserved11", ctypes.c_uint32, 1),  # bit  11
        ("FRAME_RATE_MODE", ctypes.c_uint32, 4),  # bits 12 - 15
        ("_reserved16_23", ctypes.c_uint32, 8),  # bits 16 - 23
        ("ENABLE_CMOS_TEST_PATTERN", ctypes.c_uint32, 1),  # bit  24
        ("ENABLE_CENTROID_TEST_PATTERN", ctypes.c_uint32, 1),  # bit  25
        ("_reserved26_28", ctypes.c_uint32, 3),  # bits 26 - 28
        ("DISABLE_I2C_POLL", ctypes.c_uint32, 1),  # bit  29
        ("_reserved30", ctypes.c_uint32, 1),  # bit  30
        ("DISABLE_IMG_PROC", ctypes.c_uint32, 1),  # bit  31
    ]
    _pack_ = 1


assert ctypes.sizeof(CTS_CTRL_0x1F) == ctypes.sizeof(ctypes.c_uint32)


class BB_WIDTH_0x20(ctypes.LittleEndianStructure):
    """
    Default bounding box width values, 6bit unsigned.
    """

    _fields_ = [
        ("width0", ctypes.c_uint32, 6),  # bit   0 -  5
        ("reserved6_7", ctypes.c_uint32, 2),  # bit   6 -  7
        ("width1", ctypes.c_uint32, 6),  # bit   8 - 13
        ("reserved14_15", ctypes.c_uint32, 2),  # bit  14 - 15
        ("width2", ctypes.c_uint32, 6),  # bit  16 - 21
        ("reserved", ctypes.c_uint32, 2),  # bit  22 - 23
        ("width3", ctypes.c_uint32, 6),  # bit  24 - 29
        ("reserved22_23", ctypes.c_uint32, 2),  # bit  29 - 31
    ]
    _pack_ = 1


assert ctypes.sizeof(BB_WIDTH_0x20) == ctypes.sizeof(ctypes.c_uint32)


class BB_HEIGHT_0x21(ctypes.LittleEndianStructure):
    """
    Default bounding box height values, 6bit unsigned.
    """

    _fields_ = [
        ("height0", ctypes.c_uint32, 6),  # bit   0 -  5
        ("reserved6_7", ctypes.c_uint32, 2),  # bit   6 -  7
        ("height1", ctypes.c_uint32, 6),  # bit   8 - 13
        ("reserved14_15", ctypes.c_uint32, 2),  # bit  14 - 15
        ("height2", ctypes.c_uint32, 6),  # bit  16 - 21
        ("reserved", ctypes.c_uint32, 2),  # bit  22 - 23
        ("height3", ctypes.c_uint32, 6),  # bit  24 - 29
        ("reserved22_23", ctypes.c_uint32, 2),  # bit  29 - 31
    ]
    _pack_ = 1


assert ctypes.sizeof(BB_HEIGHT_0x21) == ctypes.sizeof(ctypes.c_uint32)


class THRES_0x22(ctypes.LittleEndianStructure):
    """
    Default bounding box threshold values, 6bit unsigned.
    """

    _fields_ = [
        ("thres0", ctypes.c_uint8),
        ("thres1", ctypes.c_uint8),
        ("thres2", ctypes.c_uint8),
        ("thres3", ctypes.c_uint8),
    ]
    _pack_ = 1


assert ctypes.sizeof(THRES_0x22) == ctypes.sizeof(ctypes.c_uint32)


class TEMP_OFFSET_0x23(ctypes.LittleEndianStructure):
    """
    Per pixel constant temperature offset `C` for image processing and CIS constant temperature offset `E` as <8,8> fixed point numbers.
    """

    _fields_ = [
        ("conv_temp_offset", ctypes.c_int16),
        ("is_temp_offset", ctypes.c_int16),
    ]
    _pack_ = 1


assert ctypes.sizeof(TEMP_OFFSET_0x23) == ctypes.sizeof(ctypes.c_uint32)


class EXPCTRL_LUMITGT_0x24(ctypes.LittleEndianStructure):
    """
    Target accumulated luminosity.
    """

    _fields_ = [("luminosity_target", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(EXPCTRL_LUMITGT_0x24) == ctypes.sizeof(ctypes.c_uint32)


class EXPCTRL_LUMITHS_0x25(ctypes.LittleEndianStructure):
    """
    Accumulated luminosity threshold
    """

    _fields_ = [("luminosity_thresh", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(EXPCTRL_LUMITHS_0x25) == ctypes.sizeof(ctypes.c_uint32)


class EXPCTRL_EXPMAX_0x26(ctypes.LittleEndianStructure):
    """
    Maximum corrected exposure value.
    """

    _fields_ = [("exposure_max", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(EXPCTRL_EXPMAX_0x26) == ctypes.sizeof(ctypes.c_uint32)


class EXPCTRL_EXPMIN_0x27(ctypes.LittleEndianStructure):
    """
    Minimum corrected exposure value.
    """

    _fields_ = [("exposure_min", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(EXPCTRL_EXPMIN_0x27) == ctypes.sizeof(ctypes.c_uint32)


class EXPCTRL_CONFIG_0x28(ctypes.LittleEndianStructure):
    """
    Exposure correction step value.
    """

    _fields_ = [
        ("exposure_correction", ctypes.c_uint32, 10),
        ("_reserved10_31", ctypes.c_uint32, 22),
    ]
    _pack_ = 1


assert ctypes.sizeof(EXPCTRL_CONFIG_0x28) == ctypes.sizeof(ctypes.c_uint32)


class SHIELDED_COMP_CONFIG_0x29(ctypes.LittleEndianStructure):
    """
    Constant multiplier for shielded compensation value as a <8,8> signed integer.
    """

    _fields_ = [
        ("shielded_multiplier", ctypes.c_int16),
        ("_reserved16_31", ctypes.c_uint16),
    ]
    _pack_ = 1


assert ctypes.sizeof(SHIELDED_COMP_CONFIG_0x29) == ctypes.sizeof(ctypes.c_uint32)


class EXPCTRL_LUMIBBTGT_0x2A(ctypes.LittleEndianStructure):
    """
    Target accumulated luminosity of bounding boxes only.
    """

    _fields_ = [("bb_luminosity_target", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(EXPCTRL_LUMIBBTGT_0x2A) == ctypes.sizeof(ctypes.c_uint32)


class EXPCTRL_LUMIBBTHS_0x2B(ctypes.LittleEndianStructure):
    """
    Accumulated luminosity threshold of bounding boxes only.
    """

    _fields_ = [("bb_luminosity_thresh", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(EXPCTRL_LUMIBBTHS_0x2B) == ctypes.sizeof(ctypes.c_uint32)


class RESERVED_0x2C_0x3B(ctypes.LittleEndianStructure):  # 0x2C - 0x3B
    """
    Unimplemented.
    """

    _fields_ = [
        ("_reserved0", ctypes.c_uint32),
        ("_reserved1", ctypes.c_uint32),
        ("_reserved2", ctypes.c_uint32),
        ("_reserved3", ctypes.c_uint32),
        ("_reserved4", ctypes.c_uint32),
        ("_reserved5", ctypes.c_uint32),
        ("_reserved6", ctypes.c_uint32),
        ("_reserved7", ctypes.c_uint32),
        ("_reserved8", ctypes.c_uint32),
        ("_reserved9", ctypes.c_uint32),
        ("_reserved10", ctypes.c_uint32),
        ("_reserved11", ctypes.c_uint32),
        ("_reserved12", ctypes.c_uint32),
        ("_reserved13", ctypes.c_uint32),
        ("_reserved14", ctypes.c_uint32),
        ("_reserved15", ctypes.c_uint32),
    ]
    _pack_ = 1


assert ctypes.sizeof(RESERVED_0x2C_0x3B) == (0x3B - 0x2C + 1) * ctypes.sizeof(ctypes.c_uint32)


class IR_RESOLUTION_0x3C(ctypes.LittleEndianStructure):
    """
    Thermal image pixel dimensions.
    """

    _fields_ = [
        ("ir_rows", ctypes.c_uint8),
        ("ir_cols", ctypes.c_uint8),
        ("_reserved16_31", ctypes.c_uint16),
    ]
    _pack_ = 1


assert ctypes.sizeof(IR_RESOLUTION_0x3C) == ctypes.sizeof(ctypes.c_uint32)


class CMOS_RESOLUTION_0x3D(ctypes.LittleEndianStructure):
    """
    CIS pixel dimensions.
    """

    _fields_ = [
        ("cmos_rows", ctypes.c_uint16),
        ("cmos_cols", ctypes.c_uint16),
    ]
    _pack_ = 1


assert ctypes.sizeof(CMOS_RESOLUTION_0x3D) == ctypes.sizeof(ctypes.c_uint32)


class CMOS_FRAME_CRC_0x3E(ctypes.LittleEndianStructure):
    """
    !!! Matt we aren't doing this right?
    """

    _fields_ = [
        ("checksum", ctypes.c_uint16),
        ("error_count", ctypes.c_uint16),
    ]
    _pack_ = 1


assert ctypes.sizeof(CMOS_FRAME_CRC_0x3E) == ctypes.sizeof(ctypes.c_uint32)


class CMOS_FRAME_CNT_ADDR_0x3F(ctypes.LittleEndianStructure):
    """
    !!! Matt are we doing this?
    """

    _fields_ = [("cmos_frame_count", ctypes.c_uint32)]
    _pack_ = 1


assert ctypes.sizeof(CMOS_FRAME_CNT_ADDR_0x3F) == ctypes.sizeof(ctypes.c_uint32)


class RegisterMap(ctypes.LittleEndianStructure):
    """

    This struct is laid out exactly as it appears in memory, and maps each register address
    to its corresponding ctypes structure.

    Each field corresponds to one or more 32-bit metadata registers.
    """

    _fields_ = [
        ("TEMP_SENSOR_0x00", TEMP_SENSOR_0x00),
        ("LED_LIFETIME_0x01", LED_LIFETIME_0x01),
        ("GLOBAL_FRM_CNT_0x02", GLOBAL_FRM_CNT_0x02),
        ("RESERVED_0x03_0x04", RESERVED_0x03_0x04),
        ("EXPOSURE_0x05", EXPOSURE_0x05),
        ("LUMINOSITY_0x06", LUMINOSITY_0x06),
        ("IS_TEMP_0x07", IS_TEMP_0x07),
        ("LINEAR_COMP_INST_0x08", LINEAR_COMP_INST_0x08),
        ("LINEAR_COMP_AVG_0x09", LINEAR_COMP_AVG_0x09),
        ("SHIELDED_COMP_INST_0x0A", SHIELDED_COMP_INST_0x0A),
        ("SHIELDED_COMP_AVG_0x0B", SHIELDED_COMP_AVG_0x0B),
        ("MAGNIFICATION_COMP_INST_0x0C", MAGNIFICATION_COMP_INST_0x0C),
        ("MAGNIFICATION_COMP_AVG_0x0D", MAGNIFICATION_COMP_AVG_0x0D),
        ("GRAV_COMP_0x0E", GRAV_COMP_0x0E),
        ("WARMUP_COMP_0x0F", WARMUP_COMP_0x0F),
        ("LONG_TERM_COMP_0x10", LONG_TERM_COMP_0x10),
        ("STRAY_LIGHT_COMP_0x11", STRAY_LIGHT_COMP_0x11),
        ("RESERVED_0x12_0x13", RESERVED_0x12_0x13),
        ("SERIAL_NUMBER_LO_0x14", SERIAL_NUMBER_LO_0x14),
        ("SERIAL_NUMBER_HI_0x15", SERIAL_NUMBER_HI_0x15),
        ("FW_VERSION_0x16", FW_VERSION_0x16),
        ("FOV_LENS_0x17", FOV_LENS_0x17),
        ("DECENTRATION_0x18", DECENTRATION_0x18),
        ("CALIB_PARAMS_0x19", CALIB_PARAMS_0x19),
        ("RESERVED_0x1A_0x1E", RESERVED_0x1A_0x1E),
        ("CTS_CTRL_0x1F", CTS_CTRL_0x1F),
        ("BB_WIDTH_0x20", BB_WIDTH_0x20),
        ("BB_HEIGHT_0x21", BB_HEIGHT_0x21),
        ("THRES_0x22", THRES_0x22),
        ("TEMP_OFFSET_0x23", TEMP_OFFSET_0x23),
        ("EXPCTRL_LUMITGT_0x24", EXPCTRL_LUMITGT_0x24),
        ("EXPCTRL_LUMITHS_0x25", EXPCTRL_LUMITHS_0x25),
        ("EXPCTRL_EXPMAX_0x26", EXPCTRL_EXPMAX_0x26),
        ("EXPCTRL_EXPMIN_0x27", EXPCTRL_EXPMIN_0x27),
        ("EXPCTRL_CONFIG_0x28", EXPCTRL_CONFIG_0x28),
        ("SHIELDED_COMP_CONFIG_0x29", SHIELDED_COMP_CONFIG_0x29),
        ("EXPCTRL_LUMIBBTGT_0x2A", EXPCTRL_LUMIBBTGT_0x2A),
        ("EXPCTRL_LUMIBBTHS_0x2B", EXPCTRL_LUMIBBTHS_0x2B),
        ("RESERVED_0x2C_0x3B", RESERVED_0x2C_0x3B),
        ("IR_RESOLUTION_0x3C", IR_RESOLUTION_0x3C),
        ("CMOS_RESOLUTION_0x3D", CMOS_RESOLUTION_0x3D),
        ("CMOS_FRAME_CRC_0x3E", CMOS_FRAME_CRC_0x3E),
        ("CMOS_FRAME_CNT_ADDR_0x3F", CMOS_FRAME_CNT_ADDR_0x3F),
    ]
    _pack_ = 1
