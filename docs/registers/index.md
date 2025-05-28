# Metadata registers

The API reference defines each CTS Gen3 metadata register (e.g. [Temperature sensor register at address 0x00][ctsgen3.registers.registers.TEMP_SENSOR_0x00]) and the entire register bank ([RegisterMap][ctsgen3.registers.registers.RegisterMap]) as a `ctypes` struct.

Given the raw `bytes` of the entire register bank (or a subset of registers) you can populate the struct like

```
register_instance = RegisterMap.from_buffer_copy(raw_register_bytes)
```

See source code snippets for fields within each register.

The registers are accessible from the processing modules bulk data SPI and command and control I2C interfaces.

There are 64 registers x 32 bit per register = 256B of data.
