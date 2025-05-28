# SPI bulk data interface

Calumino's Gen3 processing module serves thermal frames, computer vision detections, computer vision foreground, and metadata over a bulk data Serial Peripheral Interface (SPI).

The processing module is a SPI slave that only transmits data, it does not receive data.

The bulk data can be configured by using the processing module's command and control Inter-Integrated Circuit (I2C) interface.

!!! warning
    v0.1.0 processing module firmware shipped with P3 units does not support an I2C interface for configuration of the SPI bulk data interface.

## Configuration

### Pins

| #   | Name      | Type            | Description                                   |
| --- | ----------| ----------------| --------------------------------------------- |
| PB2 | `MISO`    | Digital output  | Serial data output.                           |
| PB3 | `MOSI`    | Digital input   | Serial data input. Unused.                    |
| PB4 | `SCLK`    | Digital input   | Serial clock input.                           |
| PB5 | `CS`      | Digital input   | Chip select; active low.                      |
| PB6 | `DRDY`    | Digital output  | Data ready indicator; active low.             |
| PB7 | `RST`     | Digital input   | Transaction finished interrupt (route to CS)  |

### Mode and timing

!!! note
    Switching characteristics and timimg requirements are provided in Himax's WE2 datasheet.

| Mode | CPHA | CPOL |
| ---- | ---- | ---- |
|    0 |    0 |    0 | 

The minimum SCLK period is 533ns (max frequency 1.875MHz).

!!! note
    v0.1.0 processing module firmware ***can*** be operated with an SCLK period of 267ns (max frequency 3.75MHz) if the host uses SPI mode 1 or 2 (whilst the processing module uses mode 0), though the reasons for this are not clear and more testing is being performed.

## Data packet

The data provided in a transmission is a single contiguous packet of each section shown below.

wavedrom (
    { signal: [ { name: "MISO", wave: "0.3..24..25..26..20.", data: ["Thermal frame", "CRC", "Metadata","CRC","CV foreground","CRC","CV detections","CRC"] },] }
)

Each section a 2 byte CRC using the CRC-16-CCITT (XModem) algorithm. Each section can be selectively turned on and off by using the command and control I2C interface.

The API reference defines ctype structs for the SPI packet ([SpiPacket][ctsgen3.spi.spi.SpiPacket]) and its subsections (e.g. [SpiPacket][ctsgen3.spi.spi.SpiThermalPacket]).

## Data retrieval

!!! warning
    EVKs rev1 and below do not have FRDY routed to the FTDI I2C/SPI to USB chip - hosts should read at the native FPS of their firmware (4FPS for v0.1.0) 

The processing module prepares the data SPI TX FIFO with data as configured by the command and control I2C interface.

When this occurs, the DRDY pin will be asserted low to trigger data retrieval for at least 10us.

Retrieve data by asserting CS low and clocking out as many bytes as `ctypes.sizeof(SpiPacket)` or size of I2C configured data sections, then deasserting CS high.

!!! warning
    CS must be deasserted high at the end of a read in order for the processing module to safely reset the SPI TX FIFO. Do not keep CS asserted low.

DRDY then deasserts high.

wavedrom(
    {
        "signal" :
        [
            { "name": "CS",	"wave": "1.0..|....1." },
            { "name": "SCLK",		"wave": "1..N.|...h.." },
            { "name": "MISO", 		"wave": "0..2.....0..", "data": ["SpiPacket"] },
            { "name": "DRDY",  "wave": "10...|.....1" },
        ]
    }
)

The processing module will reset the SPI TX FIFO at the end of each transaction after CS is desasserted high.

Therefore, if a CRC error occurs, or if the read bytes != `ctypes.sizeof(SpiPacket)`, simply retrieve data again before FRDY next goes high (at which point the old data is lost).

!!! warning
    EVKs rev1 do not route the SPI RST pin to CS, so the SPI TX FIFO will not reset. Therefore, any CRC errors or over/under reads will cause lost data.

Imagine the contents of the SPI TX FIFO are `[0x00, 0x01, 0x02, ... 0xFE, 0xFF]`.

If the read bytes < `ctypes.sizeof(SpiPacket)`, then DRDY will stay asserted until a subsequent transaction ends that has read all >= `ctypes.sizeof(SpiPacket)`. The subsequent transaction will contain the same data repeated.

wavedrom(
    {
        "signal" :
        [
            { "name": "CS",	 "wave": "1.0.|..1.0..|...1." },
            { "name": "SCLK","wave": "1..N|.h...N.|..h.." },
            { "name": "MISO","wave": "0..2..0...2....0..", "data": ["0x00 0x01 0x02","0x00 0x01 0x02 ... 0xFF"] },
            { "name": "DRDY","wave": "10......|........1" },
        ]
    }
)

If the read bytes > `ctypes.sizeof(SpiPacket)`, then DRDY will deassert, and all bytes extra bytes read are copies of the last byte. The subsequent transaction will contain the same data repeated.

wavedrom(
    {
        "signal" :
        [
            { "name": "CS",  "wave": "1.0...|....1.0.|..1" },
            { "name": "SCLK","wave": "1..N..|...h...N|.h." },
            { "name": "MISO","wave": "0..2......0...2..0.", "data": ["0x00 0x01 0x02 ... 0xFF 0xFF 0xFF","0x00 0x01 0x02"] },
            { "name": "DRDY","wave": "10....|.....1......" },
        ]
    }
)