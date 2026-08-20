# 페이지 243

Chapter 28
Fast Crystal Oscillator Digital Controller (FXOSC)
28.1 Chip-specific FXOSC information
28.1.1 Chip-specific FXOSC information
For bypass mode applications, the EXTAL pin should be driven low when FXOSC is in off/disabled state.
• While initializing FXOSC: When the FXOSC is used in Bypass mode, the external clock source can only be enabled after the 
FXOSC is enabled.
• While disabling FXOSC: When the FXOSC is used in Bypass mode, the external clock source must already be inactive before 
disabling the FXOSC.
28.2 Overview
The Fast Crystal Oscillator (FXOSC) generates a clock which can be used at the SoC level. The FXOSC has a digital interface 
to control and configure the oscillator. When FXOSC is powered down at any time, it is designed not to generate any glitch at 
the output clock. A counter inside FXOSC handles different stabilization times. CG cell is clock gating cell, it gates the clock till 
stabilization time.
28.2.1 Block diagram
Counter logic
CG cell
clk div
FXOSC (Digital logic)
FXOSC (Analog logic)
Power ports
Mode selection
Power down
Other controls
extal
xtal
CTRL[EOCV]
OSC_STAT
IPS
Reg
IPS
CLK
Synchronous 
power-down logic
OSC_STAT
Figure 133. FXOSC block diagram
28.2.2 Features
FXOSC features are as follows:
• Status register shows current module state.
• Control register can:
— Select a mode of operation:
◦Crystal mode
◦Single-Input Bypass mode using EXTAL clock input
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1145 / 5251


---
# 페이지 244

— Disable the module (Power-Down mode)
28.3 Functional description
The table below shows configuration settings for the different FXOSC modes set by the CTRL register:
Table 177. FXOSC operation mode settings
Mode
CTRL[OSCON]
CTRL[OSC_BYP]
CTRL[COMP_EN]
FXOSC_CLK
Power-Down mode
0
X
X
0
Crystal mode
1
0
1
Crystal clock
Single-Input Bypass 
mode
1
1
0
EXTAL
Power-Down mode is the FXOSC default condition after any reset: POR, Destructive, or Functional.
28.3.1 Clock generation in Crystal mode
FXOSC_CLK start when counter value reaches FXOSC_CTRL[EOCV] × 128.
28.3.2 Clock generation in Single-Input Bypass mode
This mode bypasses the oscillator and uses a single-input external clock (EXTAL input) for FXOSC_CLK. When FXOSC enters 
Bypass mode:
• Enable the external clock after enabling FXOSC during FXOSC initialization.
• Disable the external clock beforehand when disabling FXOSC.
28.3.3 Clocking
This module has no clocking considerations.
28.3.4 Interrupts
This module has no interrupts.
28.4 External signals
This module has no external signals.
28.5 Initialization
Initializing FXOSC
Initialize FXOSC as follows:
1. Write the desired value to CTRL[OSC_BYP] and CTRL[COMP_EN] to select an operation mode as shown in Table 177.
 
FXOSC must be disabled when the operation mode is modified.
  NOTE  
2. Configure CTRL[GM_SEL].
• In Crystal mode configure the transconductance based on the module specification in the chip data sheet.
• In Single-Input Bypass mode write 0000b to this field.
NXP Semiconductors
Fast Crystal Oscillator Digital Controller (FXOSC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1146 / 5251


---
# 페이지 245

 
In Crystal mode FXOSC will not function with zero transconductance (GM_SEL = 0000b).
  NOTE  
3. Set CTRL[EOCV] calculating the value as follows:
• EOCV (in decimal) = (stabilization time in ns) ÷ (4×128×(period of clock in ns))
4. Write 1 to CRTL[OSCON] to enable FXOSC.
 
When the FXOSC is used in Bypass mode, the clock from the external source can only be used after the FXOSC 
is enabled
  NOTE  
5. Confirm the clock is stable (STAT[OSC_STAT] = 1) before using it.
 
See Hardware design guide for further details and the recommended circuit for each mode.
  NOTE  
Disabling FXOSC
Write 0 to CRTL[OSCON] to disable FXOSC when FXOSC_CLK is running and stable.
FXOSC enters Power-down mode after at least four crystal clocks. No glitches occur during the transition to Power-Down mode 
because synchronizers are used.
 
After disabling FXOSC:
• Wait for at least 2μs before enabling FXOSC again.
• You must not change other values in FXOSC registers for at least 16 FXOSC_CLK cycles.
  NOTE  
28.6 FXOSC register descriptions
This section provides the descriptions of all registers used for configuring the FXOSC.
28.6.1 FXOSC memory map
Use 8-bit, 16-bit, or 32-bit addressing to access registers.
FXOSC base address: 402D_4000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
FXOSC Control Register (CTRL)
32
RW
019D_00C0h
4h
Oscillator Status Register (STAT)
32
R
0000_0000h
28.6.2 FXOSC Control Register (CTRL)
Offset
Register
Offset
CTRL
0h
NXP Semiconductors
Fast Crystal Oscillator Digital Controller (FXOSC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1147 / 5251


---
# 페이지 246

Function
Configures FXOSC operation.
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
BYP 
0
Reserved 
Reserv
ed 
COMP
_EN 
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
1
1
0
0
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
Reserv
ed 
ALC_D 
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
1
1
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
OSC_BYP
Oscillator bypass
Bypasses the internal oscillator.
0b - Internal oscillator not bypassed
1b - Internal oscillator bypassed
30
—
Reserved
29-26
—
Reserved
25
—
Reserved
24
COMP_EN
Comparator enable
Enables or disables the comparator.
• For Crystal mode set this field to 1.
• For Single-Input Bypass mode set this field to 0.
0b - Comparator disabled
1b - Comparator enabled
23-16
EOCV
End of count value
Specifies the end-of-count.
Table continues on the next page...
NXP Semiconductors
Fast Crystal Oscillator Digital Controller (FXOSC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1148 / 5251


---
# 페이지 247

Table continued from the previous page...
Field
Function
The oscillator counter runs on the crystal clock divided by 4 and counts up to EOCV ✕ 128. This counting 
period ensures that the external oscillator clock signal is stable before the system selects FXOSC as 
a source.
 
• You must set EOCV to the appropriate value to allow clock and duty cycle to stabilize 
and guarantee that OSC_STAT becomes set within the crystal startup time.
— In Crystal mode, EOCV value must to be calculated to appropriate value based 
on the crystal specification using the equation in Initializing FXOSC.
— In Single-Input Bypass mode, EOCV value is irrelevant. FXOSC holds the 
counter in reset.
• Before modifying EOCV, FXOSC must be disabled.
  NOTE  
15-8
—
Reserved
7-4
GM_SEL
Crystal overdrive protection
Selects the transconductance applied by the FXOSC amplifier. This setting depends on 
crystal specification.
 
• In Crystal mode FXOSC will not function with zero transconductance 
(GM_SEL = 0000b).
• For details on how to set this field, see Initializing FXOSC.
  NOTE  
0000b - 0x
0001b - 0.1004x
0010b - 0.2009x
0011b - 0.3013x
0100b - 0.2343x
0101b - 0.3348x
0110b - 0.4345x
0111b - 0.5349x
1000b - 0.4679x
1001b - 0.5684x
1010b - 0.6681x
1011b - 0.7678x
1100b - 0.7016x
1101b - 0.8013x
Table continues on the next page...
NXP Semiconductors
Fast Crystal Oscillator Digital Controller (FXOSC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1149 / 5251


---
# 페이지 248

Table continued from the previous page...
Field
Function
1110b - 0.9003x
1111b - 1x
3
—
Reserved
2
ALC_D
Automatic level controller enable
The ALC feature of the FXOSC internal circuit automatically adjusts the bias current of the crystal 
oscillator’s amplifier. It must be used in crystal oscillator mode. During startup the EXTAL/XTAL 
amplitude would be lower, so the ALC circuit dynamically increases the bias current of the internal 
amplifier to provide higher current and make crystal oscillator startup faster in normal oscillator mode. 
After EXTAL/XTAL amplitude has increased to a steady state, the ALC circuit automatically reduces the 
amplifier’s bias current to save power.
0b - Enables automatic level controller
1b - Disables automatic level controller
1
—
Reserved
0
OSCON
Crystal oscillator power-down control
Enables or disables FXOSC
0b - Disables FXOSC
1b - Enables FXOSC
28.6.3 Oscillator Status Register (STAT)
Offset
Register
Offset
STAT
4h
Function
Shows current state of FXOSC.
NXP Semiconductors
Fast Crystal Oscillator Digital Controller (FXOSC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1150 / 5251


---
# 페이지 249

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
Indicates the crystal oscillator status.
 
OSC_STAT value is not valid if transconductance is set to 0.
  NOTE  
0b - Crystal oscillator is off or on but not stable.
1b - Crystal oscillator is on and providing a stable clock.
30-0
—
Reserved
NXP Semiconductors
Fast Crystal Oscillator Digital Controller (FXOSC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1151 / 5251


---