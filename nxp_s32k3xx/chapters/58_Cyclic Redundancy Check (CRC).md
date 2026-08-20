# 페이지 382

Chapter 58
Cyclic Redundancy Check (CRC)
58.1 Chip-specific CRC information
This chip supports one instance of CRC module.
58.2 Overview
CRC generates 16-bit or 32-bit CRC codes output for error detection. You can calculate these codes for up to 32 bits input data 
at a time.
CRC provides a programmable polynomial and other parameters to meet 16-bit or 32-bit CRC standards.
58.2.1 Block diagram
Combine
logic
[31:24]
[23:16]
[15:8]
[7:0]
Reverse
logic
TOT
Data register
Data register
16- and 32-bit select
Polynomial register
NOT
logic
Reverse
logic
CRC engine
CRC data
Polynomial
TCRC
Checksum
Data
Seed
MUX
[31:24]
[23:16]
[15:8]
[7:0]
[31:24]
[23:16]
[15:8]
[7:0]
WAS
FXOR
TOTR
Figure 231. Block diagram
58.2.2 Features
CRC has the following features:
• Hardware CRC generator circuit using 16-bit or 32-bit programmable shift registers
• Programmable initial seed value and polynomial
• Transpose of input or output data (CRC result) in bitwise or bytewise (this option is required for certain CRC standards. 
You cannot perform a bytewise transpose operation when accessing DATA via 8-bit access.)
• Invert final CRC result
• 32-bit CPU register programming interface
58.3 Functional description
58.3.1 Modes of operation
The following sections describe various modes of operation that affect the functionality of CRC: Run mode and Low power mode.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2299 / 5251


---
# 페이지 383

58.3.1.1
Run mode
Run mode is the basic mode of operation.
58.3.1.2
Low-power modes
When the chip enters the low-power mode, the CRC module clock (ipg_clk and ipg_clk_s) is disabled and the in-progress 
CRC calculation stops. The calculation resumes after the CRC module clock is enabled or the chip exits low power mode via 
system reset.
 
See the chip-specific power management chapter to know the specific low-power modes supported on your device.
  NOTE  
58.3.2 CRC calculations
In 16-bit and 32-bit CRC modes, you can program data values as 8 bits, 16 bits, or 32 bits at a time, provided all bytes are 
contiguous. Noncontiguous bytes lead to an incorrect CRC calculation.
58.3.2.1
Calculating a 16-bit CRC
Perform these steps to calculate a 16-bit CRC:
1. Write 0 to CTRL[TCRC] to enable 16-bit CRC mode.
2. Program the transpose and complement options in Control (CTRL) as required for the CRC calculation.
3. Write a 16-bit polynomial to GPOLY[LOW].
GPOLY[HIGH] is not usable in 16-bit CRC mode.
4. Write 1 to CTRL[WAS] to program the seed value.
5. Write a 16-bit seed to DATA[LU] and DATA[LL].
DATA[HU] and DATA[HL] are not used.
6. Write 0 to CTRL[WAS] to start writing data values.
7. Write data values into DATA[LU], and DATA[LL]
CRC is calculated on every data value write and the intermediate CRC result is stored back into DATA[LU] and DATA[LL] 
8. After writing all the data values, read the final CRC result from DATA[LU] and DATA[LL].
CRC is calculated bytewise and two clocks are required to complete one CRC calculation.
The transpose and complement operations are performed on-the-fly when reading or writing values. See Transpose feature and 
Result complement for details.
58.3.2.2
Calculating a 32-bit CRC
Perform these steps to calculate a 32-bit CRC:
1. Write 1 to CTRL[TCRC] to enable 32-bit CRC mode.
2. Program the transpose and complement options in Control (CTRL) as required for CRC calculation. See Transpose 
feature and Result complement for details.
3. Write a 32-bit polynomial to GPOLY[HIGH] and GPOLY[LOW] .
4. Write 1 to CTRL[WAS] to program the seed value.
5. Write a 32-bit seed to DATA[HU], DATA[HL], DATA[LU], and DATA[LL].
6. Write 0 to CTRL[WAS] to start writing data values.
7. Write data values into DATA[HU], DATA[HL], DATA[LU], and DATA[LL] 
NXP Semiconductors
Cyclic Redundancy Check (CRC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2300 / 5251


---
# 페이지 384

CRC is computed on every data value write and the intermediate CRC result is stored back into DATA . 
8. After writing all the values, read the final CRC result from DATA[HU], DATA[HL], DATA[LU], and DATA[LL].
CRC is calculated bytewise and two clocks are required to complete one CRC calculation.
The transpose and complement operations are performed on-the-fly when reading or writing values. See Transpose feature and 
Result complement for details.
58.3.3 Transpose feature
Transpose is not enabled by default. However, CRC requires input data and/or final checksum to be transposed. You have an 
option to configure each transpose operation separately to meet CRC standards. The data is transposed on-the-fly while being 
read or written.
Some protocols use the little-endian format for data stream to calculateCRC. In this case, transpose flips bits.
58.3.3.1
Types of transpose
CRC provides several types of transpose to flip bits and/or bytes for both writing input data and reading result separately using 
the CTRL[TOT] and CTRL[TOTR] according to the CRC calculation being used.
The following types of transpose are available for writing to and reading from DATA.
1. CTRL[TOT] or CTRL[TOTR] is 0.
No transposition occurs.
2. CTRL[TOT] or CTRL[TOTR] is 1.
Bits in a byte are transposed when bytes are not transposed.
reg[31:0] becomes {reg[24:31], reg[16:23], reg[8:15], reg[0:7]}.
31
24
24
31
23
16
16
23
15
8
8
15
7
0
0
7
Figure 232. Transpose type 1b
3. CTRL[TOT] or CTRL[TOTR] is 10b.
Both bits in bytes and bytes are transposed.
reg[31:0] becomes {reg[0:7], reg[8:15], reg[16:23], reg[24:31]}.
31
0
0
31
Figure 233. Transpose type 10b
4. CTRL[TOT] or CTRL[TOTR] is 11b.
Bytes are transposed but bits are not transposed.
reg[31:0] becomes {reg[7:0], reg[15:8], reg[23:16], reg[31:24]}.
NXP Semiconductors
Cyclic Redundancy Check (CRC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2301 / 5251


---
# 페이지 385

31
24
7
0
23
16
15
8
15
8
23
16
7
0
31
24
Figure 234. Transpose type 11b
 
For 8-bit and 16-bit write accesses to Data (DATA), the data is transposed with 0s on the unused byte or bytes 
(taking 32 bits as a whole), but CRC is calculated on the valid byte(s) only. When reading the Data (DATA) for 
a 16-bit CRC result and using transpose options 10 and 11, the resulting value after transposition resides in 
DATA[HU] and DATA[HL]. You must account for this situation when reading the 16-bit CRC result, so reading 32 
bits is preferred.
  NOTE  
58.3.4 Result complement
When CTRL[FXOR] = 1, the checksum is complemented. The CRC result complement function outputs the complement of the 
checksum value stored in Data (DATA) every time Data (DATA) is read. When CTRL[FXOR] = 0,, reading Data (DATA) accesses 
the raw checksum value.
58.3.5 Clocking
Table 328. CRC clocks
Type of clock
Description
Bus clock 
(ipg_clk/ipg_clk_s)
ipg_clk_s controls the access to the CRC registers. ipg_clk and ipg_clk_s function the CRC module.
 
See the chip-specific clocking chapter, to know the specific CRC clocks supported on your device.
  NOTE  
58.3.6 Interrupts
This module has no interrupts.
58.4 External signals
There is no CRC signal that connects off chip.
58.5 Initialization
To enable CRC calculation, you must program:
• CTRL[WAS] .
• Polynomial (GPOLY).
• Parameters for transposition and CRC result inversion in the applicable registers.
Writing 1 to CTRL[WAS] enables you to program the seed value into CRC Data registers.
After writing all the data, you must wait for at least two clock cycles to read the data from CRC Data (DATA) register.
After a CRC calculation completes, you can reinitialize the module for a new CRC computation by again writing 1 to CTRL[WAS] 
and programming a new, or previously used, seed value. You must set all other parameters before programming the seed value 
and subsequent data values.
NXP Semiconductors
Cyclic Redundancy Check (CRC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2302 / 5251


---
# 페이지 386

58.6 Use cases
The following tables use the little-endian format.
58.6.1 CTRL programming
The following table shows Control (CTRL) programming for 16-bit CRC.
Table 329. CTRL programming for 16-bit CRC
Algorithm
Polynomial
Seed
Ref in
Ref out
XOR out
CTRL[TO
T]
CTRL[TO
TR]
CTRL[FX
OR]
CRC-16_CCITT_FALSE
1021h
FFFFh
0
0
0000h
0h
0h
0h
CRC-16_ARC
8005h
0000h
1
1
0000h
1h
2h
0h
CRC-16_AUG_CCITT
1021h
1D0Fh
0
0
0000h
0h
0h
0h
CRC-16_BUYPASS
8005h
0000h
0
0
0000h
0h
0h
0h
CRC-16_CCITT_ZERO
1021h
0000h
0
0
0000h
0h
0h
0h
CRC-16_CDMA2000
C867h
FFFFh
0
0
0000h
0h
0h
0h
CRC-16_DDS_110
8005h
800Dh
0
0
0000h
0h
0h
0h
CRC-16_DECT_X
589h
0000h
0
0
0000h
0h
0h
0h
CRC-16_DNP
3D65h
0000h
1
1
FFFFh
1h
2h
1h
CRC-16_EN_13757
3D65h
0000h
0
0
FFFFh
0h
0h
1h
CRC-16_GENIBUS
1021h
FFFFh
0
0
FFFFh
0h
0h
1h
CRC-16_MAXIM
8005h
0000h
1
1
FFFFh
1h
2h
1h
CRC-16_MCRF4XX
1021h
FFFFh
1
1
0000h
1h
2h
0h
CRC-16_RIELLO
1021h
B2AAh
1
1
0000h
1h
2h
0h
CRC-16_T10_DIF
8BB7h
0000h
0
0
0000h
0h
0h
0h
CRC-16_TELEDISK
A097h
0000h
0
0
0000h
0h
0h
0h
CRC-16_TMS37157
1021h
89ECh
1
1
0000h
1h
2h
0h
CRC-16_USB
8005h
FFFFh
1
1
FFFFh
1h
2h
1h
CRC-16_A
1021h
C6C6h
1
1
0000h
1h
2h
0h
CRC-16_KERMIT
1021h
0000h
1
1
0000h
1h
2h
0h
CRC-16_MODBUS
8005h
FFFFh
1
1
0000h
1h
2h
0h
CRC-16_X_25
1021h
FFFFh
1
1
FFFFh
1h
2h
1h
CRC-16_XMODEM
1021h
0000h
0
0
0000h
0h
0h
0h
The following table shows Control (CTRL) programming for 32-bit CRC.
NXP Semiconductors
Cyclic Redundancy Check (CRC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2303 / 5251


---
# 페이지 387

Table 330. CTRL programming for 32-bit CRC
Algorithm
Polynomial
Seed
Ref in
Ref out
XOR out
CTRL[TOT]
CTRL[TO
TR]
CTRL[FX
OR]
CRC-32
04C11DB7h
FFFFFFFFh 1
1
FFFF_FFFFh 1h
2h
1h
CRC-32_BZIP2
04C11DB7h
FFFFFFFFh 0
0
FFFF_FFFFh 0h
0h
1h
CRC-32C
1EDC6F41h
FFFFFFFFh 1
1
FFFF_FFFFh 1h
2h
1h
CRC-32D
A833982Bh
FFFFFFFFh 1
1
FFFF_FFFFh 1h
2h
1h
CRC-32_MPEG-2
04C11DB7h
FFFFFFFFh 0
0
0000_0000h
0h
0h
0h
CRC-32_POSIX
04C11DB7h
00000000h
0
0
FFFF_FFFFh 0h
0h
1h
CRC-32Q
814141ABh
00000000h
0
0
0000_0000h
0h
0h
0h
CRC-32_JAMCRC
04C11DB7h
FFFFFFFFh 1
1
0000_0000h
1h
2h
0h
CRC-32_XFER
000000AFh
00000000h
0
0
0000_0000h
0h
0h
0h
58.6.2 Expected read data fields
The following table shows the expected read data fields for 16-bit CRC.
Table 331. Expected read data fields for 16-bit CRC
Algorithm
Data (DATA)
CRC16_CCITT_FALSE
[31:16] = Unknown[15:0] = Valid data
CRC16_ARC
[31:16] = Valid data [15:0] = Unknown
CRC16_AUG_CCITT
[31:16] = Unknown [15:0] = Valid data
CRC16_BUYPASS
[31:16] = Unknown [15:0] = Valid data
CRC16_CCITT_ZERO
[31:16] = Unknown [15:0] = Valid data
CRC16_CDMA2000
[31:16] = Unknown [15:0] = Valid data
CRC16_DDS_110
[31:16] = Unknown [15:0] = Valid data
CRC16_DECT_X
[31:16] = Unknown [15:0] = Valid data
CRC16_DNP
[31:16] = Valid data [15:0] = Unknown
CRC-16_EN_13757
[31:16] = Unknown [15:0] = Valid data
CRC-16_GENIBUS
[31:16] = Unknown [15:0] = Valid data
CRC-16_MAXIM
[31:16] = Valid data [15:0] = Unknown
CRC-16_MCRF4XX
[31:16] = Valid data [15:0] = Unknown
CRC-16_RIELLO
[31:16] = Valid data [15:0] = Unknown
CRC-16_T10_DIF
[31:16] = Unknown [15:0] = Valid data
CRC-16_TELEDISK
[31:16] = Unknown [15:0] = Valid data
CRC-16_TMS37157
[31:16] = Valid data [15:0] = Unknown
CRC-16_USB
[31:16] = Valid data [15:0] = Unknown
Table continues on the next page...
NXP Semiconductors
Cyclic Redundancy Check (CRC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2304 / 5251


---
# 페이지 388

Table 331. Expected read data fields for 16-bit CRC (continued)
Algorithm
Data (DATA)
CRC-16_A
[31:16] = Valid data [15:0] = Unknown
CRC-16_KERMIT
[31:16] = Valid data [15:0] = Unknown
CRC-16_MODBUS
[31:16] = Valid data [15:0] = Unknown
CRC-16_X_25
[31:16] = Valid data [15:0] = Unknown
CRC-16_XMODEM
[31:16] = Unknown [15:0] = Valid data
The following table shows the expected read data fields for 32-bit CRC.
Table 332. Expected read data fields for 32-bit CRC
Algorithm
Data (DATA)
CRC-32
[31:0] = Valid data
CRC-32_BZIP2
[31:0] = Valid data
CRC-32C
[31:0] = Valid data
CRC-32D
[31:0] = Valid data
CRC-32_MPEG-2
[31:0] = Valid data
CRC-32_POSIX
[31:0] = Valid data
CRC-32Q
[31:0] = Valid data
CRC-32_JAMCRC
[31:0] = Valid data
CRC-32_XFER
[31:0] = Valid data
58.7 Memory map and register descriptions
 
You must reconfigure CRC engine in case an IPS transfer error occurs (ips_xfr_err).
  NOTE  
The CRC module generates a transfer error in the following cases:
• Write accesses to the register addresses that are not mapped to the peripherals but included in the address spaces of 
the peripherals.
58.7.1 CRC register descriptions
58.7.1.1
CRC memory map
CRC base address: 4038_0000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Data (DATA)
32
RW
FFFF_FFFFh
4h
Polynomial (GPOLY)
32
RW
0000_1021h
8h
Control (CTRL)
32
RW
0000_0000h
NXP Semiconductors
Cyclic Redundancy Check (CRC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2305 / 5251


---
# 페이지 389

58.7.1.2
Data (DATA)
Offset
Register
Offset
DATA
0h
Function
Configures the value of seed, data, and checksum. When CTRL[WAS] = 1, any write to this register is regarded as the seed value. 
When CTRL[WAS] becomes 0, any write to this register is regarded as data for general CRC calculation.
In 16-bit CRC mode, DATA[HU] and DATA[HL] are not used for programming the seed value, and reads of these fields return an 
indeterminate value. In 32-bit CRC mode, all fields are used for programming the seed value.
When programming data values, you can program to write 8 bits, 16 bits, or 32 bits in big endian order, provided all bytes are 
contiguous, with the MSB of data value written first.
After writing all data values, you can read the CRC result from DATA register. In 16-bit CRC mode, the CRC result is available 
in DATA[LU] and DATA[LL]. In 32-bit CRC mode, all fields contain the result. After writing all data, you must wait for at least two 
clock cycles to read the data from CRC data (DATA) register.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
HU 
HL 
W
Reset
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
LU 
LL 
W
Reset
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
Fields
Field
Function
31-24
HU
Upper Part of High Byte
Generates CRC checksum in both 16-bit and 32-bit CRC modes if CTRL[WAS] = 0.
• In 16-bit CRC mode (CTRL[TCRC] = 0), this field is not used for programming a seed value.
• In 32-bit CRC mode (CTRL[TCRC] = 1), the values written to this field are part of the seed value 
when CTRL[WAS] = 1.
23-16
HL
Lower Part of High Byte
Generates CRC checksum in both 16-bit and 32-bit CRC modes if CTRL[WAS] = 0.
• In 16-bit CRC mode (CTRL[TCRC] = 0), this field is not used for programming a seed value.
Table continues on the next page...
NXP Semiconductors
Cyclic Redundancy Check (CRC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2306 / 5251


---
# 페이지 390

Table continued from the previous page...
Field
Function
• In 32-bit CRC mode (CTRL[TCRC] = 1), the values written to this field are part of the seed value 
when CTRL[WAS] = 1.
15-8
LU
Upper Part of Low Byte
Generates CRC checksum when CTRL[WAS] = 0.
When CTRL[WAS] = 1,the values written to this field are part of the seed value.
7-0
LL
Lower Part of Low Byte
Generates CRC checksum when CTRL[WAS] = 0.
When CTRL[WAS] = 1, the values written to this field are part of the seed value.
58.7.1.3
Polynomial (GPOLY)
Offset
Register
Offset
GPOLY
4h
Function
Configures polynomial value for CRC calculation.
• Sets the upper 16 bits of polynomial that are used only in 32-bit CRC mode. Writes to this field are ignored in 16-bit CRC 
mode.
• Sets the lower 16 bits of polynomial that are used in both 16-bit and 32-bit CRC modes.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
HIGH 
W
Reset
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
LOW 
W
Reset
0
0
0
1
0
0
0
0
0
0
1
0
0
0
0
1
NXP Semiconductors
Cyclic Redundancy Check (CRC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2307 / 5251


---
# 페이지 391

Fields
Field
Function
31-16
HIGH
High Half-Word
Writable and readable in 32-bit CRC mode (CTRL[TCRC] = 1). You cannot write to this field in 16-bit 
CRC mode (CTRL[TCRC] = 0).
15-0
LOW
Low Half-Word
Writable and readable in both 16-bit and 32-bit CRC modes.
58.7.1.4
Control (CTRL)
Offset
Register
Offset
CTRL
8h
Function
Sets control for CRC. You must write 1 to the appropriate fields of this register before starting a new CRC calculation, which 
you can initialize by writing 1 to CTRL[WAS] and then writing the seed into DATA.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
TOT 
TOTR 
0
FXOR 
WAS 
TCRC 
0
W
Reset
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
0
W
Reset
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
Fields
Field
Function
31-30
TOT
Transpose Type for Write
Sets transpose type for the values written to DATA. See Transpose feature for the available transpose 
options.
00b - No transposition
01b - Bits in bytes are transposed, but bytes are not transposed.
Table continues on the next page...
NXP Semiconductors
Cyclic Redundancy Check (CRC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2308 / 5251


---
# 페이지 392

Table continued from the previous page...
Field
Function
10b - Both bits in bytes and bytes are transposed.
11b - Only bytes are transposed, no bits in a byte are transposed.
29-28
TOTR
Transpose Type for Read
Sets transpose type for the values read from DATA . See Transpose feature for the available transpose 
options.
00b - No transposition
01b - Bits in bytes are transposed, but bytes are not transposed.
10b - Both bits in bytes and bytes are transposed.
11b - Only bytes are transposed, no bits in a byte are transposed.
27
—
Reserved
26
FXOR
Complement Read of CRC Data Register
Enables on-the-fly complementing of read data.
Some CRC protocols require the final checksum to be XORed with FFFFFFFFh or FFFFh.
0b - Disables XOR on reading data.
1b - Inverts or complements the read value of the CRC Data.
25
WAS
Write as Seed
Specifies whether writes to DATA are data values or seed values.
When this field = 1, the value that you write to is considered as seed value. When this field = 0, the value 
that you write to is considered as data for CRC calculation.
0b - Data values
1b - Seed values
24
TCRC
TCRC
Defines the width of CRC.
0b - 16 bits
1b - 32 bits
23-0
—
Reserved
58.8 Glossary
Transpose
Flipping input or output data bits (or bytes)
Seed value
Initial value of CRC calculation
NXP Semiconductors
Cyclic Redundancy Check (CRC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2309 / 5251


---
