# 페이지 237

Chapter 26
Fast Internal RC Oscillator (FIRC)
26.1 Overview
The FIRC digital interface controls the internal 48 MHz RC oscillator system.
26.1.1 Features
FIRC can be disabled in Standby mode via software.
• Status register provides the current operating state:
— On and stable
— Off or on but not stable
26.2 External signals
This module has no external signals.
26.3 Initialization
This module does not require initialization.
26.4 FIRC register descriptions
26.4.1 FIRC memory map
FIRC base address: 402D_0000h
Offset
Register
Width
(In bits)
Access
Reset value
4h
Status Register (Status_Register)
32
R
0000_0001h
8h
Standby Enable Register (STDBY_ENABLE)
32
RW
0000_0000h
26.4.2 Status Register (Status_Register)
Offset
Register
Offset
Status_Register
4h
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1139 / 5251


---
# 페이지 238

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
Reserved 
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
Reserved 
STATU
S 
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
1
Fields
Field
Function
31-1
—
Reserved
0
STATUS
Status bit for FIRC
0b - FIRC is off or unstable.
1b - FIRC is on and stable.
26.4.3 Standby Enable Register (STDBY_ENABLE)
Offset
Register
Offset
STDBY_ENABLE
8h
Function
This register enables or disables FIRC in chip’s Standby mode.
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
Reserved 
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
Reserved 
STDB
Y_EN 
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
NXP Semiconductors
Fast Internal RC Oscillator (FIRC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1140 / 5251


---
# 페이지 239

Fields
Field
Function
31-1
—
RESERVED
0
STDBY_EN
Enables or disables FIRC in chip’s Standby mode.
0b - Disabled
1b - Enabled
26.5 Glossary
Standby mode
Power saving mode of the chip
NXP Semiconductors
Fast Internal RC Oscillator (FIRC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1141 / 5251


---