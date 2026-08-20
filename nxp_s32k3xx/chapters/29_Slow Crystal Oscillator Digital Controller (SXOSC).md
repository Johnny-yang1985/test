# 페이지 250

Chapter 29
Slow Crystal Oscillator Digital Controller (SXOSC)
29.1 Overview
The Slow crystal oscillator (SXOSC) generates a clock which can be used at the SoC level. The SXOSC has a digital interface 
to control and configure the oscillator. When SXOSC is powered down at any time, it is designed not to generate any glitch at 
the output clock. A counter inside SXOSC handles different stabilization times. CG cell is clock gating cell, it gates the clock till 
stabilization time.
29.1.1 Block diagram
Synchronous power
down logic
Counter logic
CG cell
IPS
reg
IPS
power ports
clk div
power down
other controls
STATUS
CLK
extal
xtal
ANALOG LOGIC
DIGITAL LOGIC
SXOSC
SXOSC
OSC_STAT
OSC_STAT
CTRL[EOCV]
Figure 134. Block diagram
29.2 Features
• SXOSC generates a 32 KHz clock output in crystal mode
• SXOSC contains a status register, the value of which becomes 1 when the crystal stabilization time is complete
• SXOSC can be powered down through software bit.
29.3 Functional description
SXOSC generates control signals to configure the analog module to operate in specific modes.
The following table shows the mode of operation available for selection and its settings.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1152 / 5251


---
# 페이지 251

Table 178. Operation mode settings
Mode
Value of SXOSC_CTRL[OSCON]
Output clock
Functional Oscillator
0 (oscillator switched off)
0 (indicates no output)
1 (oscillator switched on)
Crystal clock
29.3.1 Clock generation in crystal mode
After hard reset, the crystal oscillator is switched off by default. For clock generation in crystal mode, see Table 178. The counter 
logic starts counting and the stable clock starts running one clock cycle after reaching the value of SXOSC_CTRL[EOCV] x 128 
counter value. The module writes 1 to SXOSC_STAT[OSC_STAT] after two module clock cycles.
29.3.2 Clock stopping in crystal mode
To stop a stable, running clock, configure the power down mode as specified in Table 178. A glitch does not occur because 
synchronizers are used.
29.3.1 Modes of operation
The SXOSC has following modes of operation.
29.3.1.1
Crystal mode
In this mode crystal is connected between extal and xtal ports, to select crystal mode see Table 178
29.3.1.2
Bypass mode
The bypass mode is handled outside the DA Wrapper.
 
In this mode crystal is removed from extal and xtal ports and extal is driven by external clock and xtal 
is unconnected.
  NOTE  
29.3.2 Clocking
This module has no clocking considerations.
29.3.3 Interrupts
This module has no interrupts.
29.4 External signals
This module has no external signals.
29.5 Initialization information
To enter into any mode the following sequences must be followed. By default IP is disabled.
• Power-down Mode:
— When SXOSC is running in any mode, de-assert SXOSC_CTRL[OSCON]
• Crystal Mode:
1. Disable the IP by de-asserting SXOSC_CTRL[OSCON] bit
2. Connect the crystal between extal and xtal ports
NXP Semiconductors
Slow Crystal Oscillator Digital Controller (SXOSC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1153 / 5251


---
# 페이지 252

3. Write an appropriate value to SXOSC_CTRL[EOCV]
4. Program recommended value in SXOSC_CTRL[GM_SEL]
5. Enable the IP by asserting SXOSC_CTRL[OSCON] bit
6. SXOSC_STAT[OSC_STAT] bit will be set after counter runs as per programming of SXOSC_CTRL[EOCV] and 
clock will be released to SoC
29.6 SXOSC register descriptions
This section provides the description of all registers for configuring the SXOSC.
29.6.1 SXOSC memory map
Addresses are given as offsets from the module base address. All registers can be accessed using 8-bit, 16-bit or 32-
bit addressing.
 
Some of the register reset values are specifically configured for each unique device by external configuration 
signals or parameters.
  NOTE  
SXOSC base address: 402C_C000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Oscillator Control Register (SXOSC_CTRL)
32
RW
007D_0000h
4h
Oscillator Status Register (SXOSC_STAT)
32
R
0000_0000h
29.6.2 Oscillator Control Register (SXOSC_CTRL)
Offset
Register
Offset
SXOSC_CTRL
0h
Function
Oscillator Control Register
NXP Semiconductors
Slow Crystal Oscillator Digital Controller (SXOSC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1154 / 5251


---
# 페이지 253

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
0
0
CURR_PRG_S
F 
CURR_PRG_C
OMP 
EOCV 
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
1
1
1
1
1
0
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
0
GM_SEL 
0
0
OSCO
N 
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
31-29
—
Reserved
28
—
Reserved
27-26
CURR_PRG_S
F
These bits specify programmability of level shifter current.
00b - 3x
01b - 2x
10b - 3.5x
11b - 4x
25-24
CURR_PRG_C
OMP
These bits specify programmability of comparator current.
00b - 1x
01b - 2x
10b - 3x
11b - 4x
23-16
EOCV
End of count value
These bits specify the end of count value. This value is used by the oscillator Stabilization counter for 
comparison whenever it is switched On. This counting period ensures that the external oscillator clock signal 
is stable before it can be selected by the system. Oscillator counter runs on crystal clock divide by 4, and 
counts value upto EOCV * 128.
 
In order to find the appropriate EOCV value, ensure that the internal counter is running for 
at least the stabilization time of the crystal as given in the Data Sheet.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Slow Crystal Oscillator Digital Controller (SXOSC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1155 / 5251


---
# 페이지 254

Table continued from the previous page...
Field
Function
 
It is recommended to change the value of EOCV only when the IP is in disabled state.
  NOTE  
15-8
—
Reserved
7-6
GM_SEL
Crystal overdrive protection This field setting decides the trans-conductance applied by SXOSC 
amplifier, and it will depend on crystal specification.
00b - 1x
01b - 1.25x
10b - 1.3x
11b - 1.6x
5
—
Reserved
4-1
—
Reserved
0
OSCON
Crystal oscillator power-down control
 
When disabling the IP through software, program 0 to this bit-field, and ensure to not change 
any other values in the registers for at least 16 SXOSC clock cycles.
  NOTE  
0b - Crystal oscillator is switched OFF
1b - Crystal oscillator is switched ON
29.6.3 Oscillator Status Register (SXOSC_STAT)
Offset
Register
Offset
SXOSC_STAT
4h
Function
Oscillator Status Register
NXP Semiconductors
Slow Crystal Oscillator Digital Controller (SXOSC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1156 / 5251


---
# 페이지 255

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
OSC_
STAT 
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
31
OSC_STAT
Crystal oscillator status
0b - Crystal oscillator output clock is not stable.
1b - Crystal oscillator is providing a stable clock.
30-0
—
Reserved
NXP Semiconductors
Slow Crystal Oscillator Digital Controller (SXOSC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1157 / 5251


---