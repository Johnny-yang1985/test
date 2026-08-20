# 페이지 256

Chapter 30
PLL Digital Interface (PLLDIG)
30.1 Chip-specific PLLDIG information
30.1.1 PLLDIG instances
This chip supports up to two instances of PLLDIG.
Table 179. PLLDIG instances
Instance
S32K388/S32K389/S32K358/S32K348/
S32K338/S32K328
S32K310/S32K311/S32K312/
S32K314/S32K322/S32K324/S32K342/
S32K341/S32K344
PLL
Yes
Yes
PLL_AUX
Yes
No
Table 180. PLLDIG configuration
Instance
Frequency 
modulation supported
Number of reference 
clocks supported
Number of clock 
outputs supported
PLL
Yes
11
2
PLL_AUX
No
1
22
1. For S32K310 and S32K311: 2
2. For S32K328, S32K338, S32K348, and S32K358: 3
30.1.2 PLL-supported accesses and frequencies
The PLLODIV_0 and PLLODIV_1 registers support only word accesses. When you write to these registers, you must retain the 
default values of the reserved fields.
PLLDIG supports a down-spread modulation of up to 500 MHz PLL PHI clock output only.
30.1.3 Register implementation
In S32K358, S32K311 and S32K310 there are additional registers as compared to what is mentioned in section 'PLLDIG memory 
map'. See following table for details.
Table 181. Register details
Register/Bitfield
Offset
Availability
PLLCLKMUX[REFCLKSEL]1
20h
Only available in S32K311 and S32K310
PLLODIV_22
88h
Only available in S32K358, S32K348, S32K338, and S32K328
1. See section 'PLLCLKMUX definition' for register definition
2. Implementation of this register is same as PLLODIV_0/1. See PLLODIV_0/1 in section 'PLLDIG memory map' for 
register definition
30.1.3.1
PLLCLKMUX definition
Register PLLCLKMUX (PLL Clock Multiplexer) is available at offset 20h. This register selects the PLL clock source. Bitfield 
definition of this register is as shown below:
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1158 / 5251


---
# 페이지 257

Table 182. PLLCLKMUX Definition
Bitfield offset
Bitfield name
Bitfield description
0
REFCLKSEL
Reference Clock Select: Selects the PLL clock source.
• 0b-FXOSC_CLK
• 1b-FIRC_DIV2_CLK
1-31
Reserved
30.1.4 Initialization information for S32K311 and S32K310
Perform the following steps to initialize PLL:
1. Confirm that PLLODIV_n[DE] is 0 for all dividers.
2. Confirm that PLLCR[PLLPD] is 1.
3. Program PLLCLKMUX to select the appropriate reference clock.
4. Program the following as needed:
• PLLDV
• PLLFD
• PLLFM to the desired value
5. Program PLLDV[ODIV2] and PLLODIV_n[DIV] to the desired values.
6. Wait for the PLL reference clock to be stable.
7. Write 0 to PLLCR[PLLPD].
8. Wait for PLLSR[LOCK] to be 1.
9. Write 1 to PLLODIV_n[DE].
Perform the following steps to shut down PLL:
1. Write 0 to PLLODIV_n[DE] for all dividers.
2. Write 1 to PLLCR[PLLPD].
30.2 Overview
PLL can multiply or divide the frequency of a given clock input.
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1159 / 5251


---
# 페이지 258

30.2.1 Block diagram
Reference
divider
Reference clock
Register interface
PLLDV[RDIV]
PLLDV[ODIV2]
VCO
divider
vcoclkout
PFD+CPUMP
+FILTER
Feedback Divider
+ Sigma Delta
Modulator
PLLDV[MF]
PLLFD[MFN]
PLLFM[STEPNO]
PLLFM[STEPSIZE]
Lock
Detector
Loss of lock
Detector
lol
lock
0
divider
PLLODIV_0[DIV]
PLL_PHI0
PLL_PHI1
PLL_PHIn
divider
PLLODIV_1[DIV]
divider
PLLODIV_n[DIV]
Figure 135. Block diagram
The number of output dividers can vary with the module instance. See the Clocking chapter to confirm the number of PLL 
output dividers.
30.2.2 Features
PLL includes the following features:
• Programmable frequency modulation
• Multiple integer dividers on PLL outputs
• Lock detection circuitry reports when PLL achieves frequency lock
• Continuous monitoring of lock status to report Loss of Lock (LOL) condition
• Powering down the module for low-power operation (Power-Down mode)
30.3 Functional description
This section explains PLL operation and configuration.
30.3.1 Modes of operation
Table 183. Modes of operation
PLLCR[PLLPD]
PLLFD[SDMEN]
PLLFM[SSCGBYP]
Description
1
x
x
PLL is disabled.
Table continues on the next page...
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1160 / 5251


---
# 페이지 259

Table 183. Modes of operation (continued)
PLLCR[PLLPD]
PLLFD[SDMEN]
PLLFM[SSCGBYP]
Description
0
0
1
Functional mode – PLL operates in integer-only mode. 
See Clock configuration.
0
1
1
Functional mode – PLL operates in Fractional mode 
(non-Frequency modulation). See Clock configuration.
0
1
0
Functional mode – PLL operates in Frequency 
Modulation mode. See Frequency modulation.
30.3.2 Input clock frequency
PLL is designed to operate over a specified input clock frequency range. PLL source frequency limits are discussed in this chip's 
data sheet.
30.3.3 Clock configuration
See the equations below and the corresponding register configuration that determine the relationship between VCO frequency 
(fVCO) and PLL reference frequency.
• Integer-only mode:
— When PLLDV[RDIV] is 0:
Equation 1. PLL VCO frequency in integer-only mode when PLLDV[RDIV] is 0
— When PLLDV[RDIV] is not 0:
Equation 2. PLL VCO frequency in integer-only mode when PLLDV[RDIV] is not 0
• Fractional mode:
— When PLLDV[RDIV] is 0:
Equation 3. PLL VCO frequency in Fractional mode when PLLDV[RDIV] is 0
— When PLLDV[RDIV] is not 0:
Equation 4. PLL VCO frequency in Fractional mode when PLLDV[RDIV] is not 0
See the equation below and the corresponding register configuration that determine the relationship between reference and 
PLL_PHIn output frequencies.
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1161 / 5251


---
# 페이지 260

Equation 5. PLL PHI output frequency
When configuring PLL, you must not violate the maximum system clock frequency or maximum and minimum VCO frequency 
specification of PLL (see this chip's data sheet for frequency limits).
You must disable PLL by writing 1 to PLLCR[PLLPD] before any PLL configuration or input clock are modified.
You must disable PLL by writing 1 to PLLCR[PLLPD] for at least 5 μs before writing 0 to PLLCR[PLLPD] to enable PLL.
The recommended procedure to program PLL and enter Normal mode is shown in Initialization information.
30.3.4 Loss of lock (LOL)
PLL provides LOL indication. The LOL indication can only be generated when PLL is in Functional mode (see Modes of operation). 
When PLL detects a LOL, it asserts its LOL event output.
PLL does not detect loss of reference clock. If the reference clock stops after PLL achieves lock, PLL continues to indicate lock. 
It is assumed that monitoring of PLL's reference clock that is done outside PLL is enabled while PLL is in operation.
PLL LOL is intended for detection of gross failures. Use CMUs for accurate frequency monitoring.
30.3.5 Frequency modulation
In Frequency Modulation mode, PLL generates a frequency-modulated clock. The modulation depth and modulation frequency 
are calculated using the equations shown in Frequency modulation programming.
Write 1 to PLLFM[SPREADCTL] to select down-spread modulation. See Figure 136 that shows an example of down-
spread modulation.
Down spread
Modulation frequency (fMOD)
Modulation Depth (MD)
nominal VCO frequency (fpll_VCO)
Figure 136. Frequency modulation
30.3.5.1
Frequency modulation programming
Modulation depth and modulation frequency programming uses step number (PLLFM[STEPNO]) and step size 
(PLLFM[STEPSIZE]). The table below shows variables used during calculations when programming PLL for 
frequency modulation.
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1162 / 5251


---
# 페이지 261

Table 184. Variables for configuring modulation depth and frequency
Variable
Description
fREF
Input clock frequency
fMOD
Expected modulation frequency
MD
Expected modulation depth in percentage
LDF
Loop division factor
fpll_VCO
Nominal VCO frequency
Use the following equations to configure PLL for frequency modulation.
Equation 6. LDF
Equation 7. Step number
Equation 8. Step size
Frequency modulation is only possible if the condition shown in Equation 9 is met.
Equation 9. Requirement to achieve FM
You must write 0 to PLLFM[SSCGBYP] and write 1 to PLLFD[SDMEN] to enable frequency modulation.
Equation 10. Maximum possible modulation depth when PLL[RDIV] is 0
Equation 11. Maximum possible modulation depth when PLL[RDIV] is not 0
 
The effective modulation depth may differ from the intended modulation depth because of rounding operations 
applied to PLLFM[STEPSIZE] and PLLFM[STEPNO].
  CAUTION  
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1163 / 5251


---
# 페이지 262

30.3.6 Interrupt signals
This module has no interrupt signals.
30.4 External signals
This module has no external signals.
30.5 Initialization information
Perform the following steps to initialize PLL:
1. Confirm that PLLODIV_n[DE] is 0 for all dividers.
2. Confirm that PLLCR[PLLPD] is 1.
3. Program the following as needed:
• PLLDV
• PLLFD
• PLLFM to the desired value
4. Program PLLDV[ODIV2] and PLLODIV_n[DIV] to the desired values.
5. Wait for the PLL reference clock to be stable.
6. Write 0 to PLLCR[PLLPD].
7. Wait for PLLSR[LOCK] to be 1.
8. Write 1 to PLLODIV_n[DE].
Perform the following steps to shut down PLL:
1. Write 0 to PLLODIV_n[DE] for all dividers.
2. Write 1 to PLLCR[PLLPD].
30.6 PLLDIG register descriptions
This section provides the memory map and detailed descriptions of registers used for configuring PLL. The table below shows 
the memory map. Addresses are given as offsets from the module base address. All registers are accessed using 8-bit, 16-bit, or 
32-bit addressing.
30.6.1 PLLDIG memory map
PLL base address: 402E_0000h
PLL_AUX base address: 402E_4000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
PLL Control (PLLCR)
32
RW
8000_0000h
4h
PLL Status (PLLSR)
32
RW
0000_0300h
8h
PLL Divider (PLLDV)
32
RW
0C3F_1032h
Ch
PLL Frequency Modulation (PLLFM)
32
RW
4000_0000h
Table continues on the next page...
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1164 / 5251


---
# 페이지 263

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
10h
PLL Fractional Divider (PLLFD)
32
RW
0000_0000h
18h
PLL Calibration Register 2 (PLLCAL2)
32
RW
0006_0000h
80h - 84h
PLL Output Divider (PLLODIV_0 - PLLODIV_1)
32
RW
0000_0000h
30.6.2 PLL Control (PLLCR)
Offset
Register
Offset
PLLCR
0h
Function
Configures PLL functionality.
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
PLLPD 
0
W
Reset
1
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
PLLPD
PLL Power Down
Powers down or powers up PLL.
0b - Powered up
1b - Powered down
30-0
—
Reserved
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1165 / 5251


---
# 페이지 264

30.6.3 PLL Status (PLLSR)
Offset
Register
Offset
PLLSR
4h
Function
Shows the PLL status.
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
Reserved 
0
LOL 
LOCK 
0
W
W1C
Reset
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
0
0
Fields
Field
Function
31-11
—
Reserved
10-8
—
Reserved
7-4
—
Reserved
3
LOL
Loss-Of-Lock Flag
Indicates the current PLL lock status.
0b - No loss of lock detected
1b - Loss of lock detected
2
LOCK
Lock Status
Indicates that PLL has acquired lock.
0b - Unlocked
Table continues on the next page...
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1166 / 5251


---
# 페이지 265

Table continued from the previous page...
Field
Function
1b - Locked
1-0
—
Reserved
30.6.4 PLL Divider (PLLDV)
Offset
Register
Offset
PLLDV
8h
Function
Divides input clocks for PLL output generation.
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
ODIV2 
0
Reserved 
W
Reset
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
0
RDIV 
0
MFI 
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
1
0
0
1
0
Fields
Field
Function
31
—
Reserved
30-25
ODIV2
Output frequency divider for raw PLL clock.
6-bit field determining the VCO clock post divider for driving the PHI output clock.
000000 – Divide by 1
000001 – Divide by 1
000010 – Divide by 2
Table continues on the next page...
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1167 / 5251


---
# 페이지 266

Table continued from the previous page...
Field
Function
000011 – Divide by 3
000100 – Divide by 4
.......
111111 – Divide by 63
24-22
—
Reserved
21-16
—
Reserved
15
—
Reserved
14-12
RDIV
Input Clock Predivider
Sets the input clock divider.
The output of the predivider circuit generates the PLL loop reference clock.
000b - Divide by 1
001b - Divide by 1
010b - Divide by 2
011b - Divide by 3
100b - Divide by 4
101b - Divide by 5
110b - Divide by 6
111b - Divide by 7
11-8
—
Reserved
7-0
MFI
Integer Portion Of Loop Divider
Sets the value of the divider in the PLL feedback loop.
The value specified establishes the multiplication factor applied to the reference frequency. Write the divider 
value to this field, where the chosen value does not violate VCO frequency specifications.
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1168 / 5251


---
# 페이지 267

30.6.5 PLL Frequency Modulation (PLLFM)
Offset
Register
Offset
PLLFM
Ch
Function
Configures PLL frequency modulation parameters.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
PLL
PLLFM
—
PLL_AUX
—
PLLFM
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
SSCG
BYP 
SPRE
ADC...
0
STEPSIZE 
W
Reset
0
1
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
STEPNO 
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
—
Reserved
30
SSCGBYP
Frequency Modulation (Spread Spectrum Clock Generation) Bypass
Bypasses frequency modulation.
0b - Not bypassed
1b - Bypassed
29
Modulation Type Selection
Table continues on the next page...
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1169 / 5251


---
# 페이지 268

Table continued from the previous page...
Field
Function
SPREADCTL
Indicates that the modulation is spread below the nominal frequency. You must write 1 to this field.
0b - Reserved
1b - Spread below nominal frequency
28-26
—
Reserved
25-16
STEPSIZE
Frequency Modulation Step Size
Provides the step size for modulation depth and frequency in Frequency Modulation mode (see 
Frequency modulation).
15-11
—
Reserved
10-0
STEPNO
Number Of Steps Of Modulation Period Or Frequency Modulation
Provides the number of steps to achieve modulation depth in Frequency Modulation mode (see 
Frequency modulation).
30.6.6 PLL Fractional Divider (PLLFD)
Offset
Register
Offset
PLLFD
10h
Function
Enables and configures frequency modulation.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
PLL
PLLFD
—
PLL_AUX
—
PLLFD
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1170 / 5251


---
# 페이지 269

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
SDME
N 
SDM2 
SDM3 
0
Reserved 
0
Reserv
ed 
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
MFN 
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
—
Reserved
30
SDMEN
Fractional Mode Enable
Enables Fractional mode.
0b - Disabled
1b - Enabled
29
SDM2
Fractional Mode Configuration
When you are in the fractional mode (SDMEN = 1), write 1 to this field.
 
If SDMEN = 1, this field must be written 1.
  NOTE  
28
SDM3
Fractional Mode Configuration
When you are in the fractional mode (SDMEN = 1), write 1 to this field.
 
If SDMEN = 1, this field must be written 1.
  NOTE  
27-22
—
Reserved
21-18
—
Reserved
17
—
Reserved
16
Reserved
Table continues on the next page...
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1171 / 5251


---
# 페이지 270

Table continued from the previous page...
Field
Function
—
15
—
Reserved
14-0
MFN
Numerator Of Fractional Loop Division Factor
Sets the numerator of the fractional loop division factor.
You must write a value of less than 18432 to this field. When Fractional mode is disabled, you must write 
000_0000_0000_0000b to this field.
30.6.7 PLL Calibration Register 2 (PLLCAL2)
Offset
Register
Offset
PLLCAL2
18h
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
PLL
PLLCAL2
—
PLL_AUX
—
PLLCAL2
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
0
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
1
1
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
ULKCTL 
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
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1172 / 5251


---
# 페이지 271

Fields
Field
Function
31-22
—
Reserved
21-19
—
Reserved
18-16
—
Reserved
15-9
—
Reserved
8-7
ULKCTL
Unlock Control Accuracy
Defines the accuracy necessary to achieve unlock.
The lock counter determines unlock if the number of VCO clock cycles in the window of reference cycles is 
outside the number of cycles defined by this field.
00b - Unlock range = Expected value ± 9 (recommended when PLLFM[SSCGBYP] = 1). Unlock 
range = Expected value ± 9 (recommended when PLLFM[SSCGBYP] = 1)
01b - Unlock range = Expected value ± 17 (recommended when PLLFM[SSCGBYP] = 0). Unlock 
range = Expected value ± 17 (recommended when PLLFM[SSCGBYP] = 0)
10b - Unlock range = Expected value ± 33
11b - Unlock range = Expected value ± 5
6-0
—
Reserved
30.6.8 PLL Output Divider (PLLODIV_0 - PLLODIV_1)
Offset
Register
Offset
PLLODIV_0
80h
PLLODIV_1
84h
Function
Controls the PLL output clock divider settings.
This divider has a 50% duty cycle.
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1173 / 5251


---
# 페이지 272

 
These registers support only word accesses. Other write accesses lead to the following:
• Unpredictable behavior
• No transfer error generated
  NOTE  
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
DE 
0
DIV 
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
31
DE
Divider Enable
Enables PLL output divider. Divider must be disabled before disabling PLL.
0b - Disabled
1b - Enabled
30-24
—
Reserved
23-16
DIV
Division Value
Provides the division value for the output clock divider. The clock period of the clock after division is 
DIV + 1 times the time period of the divider input clock.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
PLL
PLLODIV_0–PLLODIV_1
—
PLL_AUX
PLLODIV_0–PLLODIV_1[20–16]
PLLODIV_0–PLLODIV_1[23–21]
15-2
Reserved
Table continues on the next page...
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1174 / 5251


---
# 페이지 273

Table continued from the previous page...
Field
Function
—
1-0
—
Reserved
Do not write any value other than the reset value.
NXP Semiconductors
PLL Digital Interface (PLLDIG)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1175 / 5251


---
