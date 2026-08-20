# 페이지 240

Chapter 27
Slow Internal RC Oscillator (SIRC)
27.1 Overview
The SIRC digital interface controls the slow internal on-chip 32 KHz RC oscillator system.
27.1.1 Features
The SIRC module:
• Status register provides the current operating state:
— On and stable
— Off or on but not stable
• Operates at a frequency of 32 kHz in Functional mode
27.2 Operating mode
Only a POR reset will initialize the SIRC. Destructive or Functional resets do not impact the SIRC functionality.
SIRC stabilization occurs after 96 SIRC_CLK cycles.
The SIRC output clock remains invalid until the analog SIRC stabilizes. The output clock does not glitch or overshoot its frequency 
during enabling or disabling. Also, the clock does not get stuck or produce glitches on a very short hardware disable pulse.
27.3 External signals
This module has no external signals.
27.4 Initialization
This module does not require initialization.
27.5 SIRC register descriptions
27.5.1 SIRC memory map
Access to registers use 8-bit, 16-bit, or 32-bit addressing.
SIRC base address: 402C_8000h
Offset
Register
Width
(In bits)
Access
Reset value
4h
Status Register (SR)
32
R
0000_0001h
Ch
Miscellaneous input (MISCELLANEOUS_IN)
32
RW
0000_0000h
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1142 / 5251


---
# 페이지 241

27.5.2 Status Register (SR)
Offset
Register
Offset
SR
4h
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
Status bit for SIRC
0b - SIRC is off or unstable
1b - SIRC is on and stable
27.5.3 Miscellaneous input (MISCELLANEOUS_IN)
Offset
Register
Offset
MISCELLANEOUS_IN
Ch
NXP Semiconductors
Slow Internal RC Oscillator (SIRC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1143 / 5251


---
# 페이지 242

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
STAN
DBY...
Reserved 
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
Fields
Field
Function
31-9
—
Reserved
8
STANDBY_EN
ABLE
Standby Enable for SIRC
0b - SIRC disables in Standby mode
1b - SIRC enables in Standby mode
7-4
—
Reserved
3-0
—
Reserved
NXP Semiconductors
Slow Internal RC Oscillator (SIRC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1144 / 5251


---