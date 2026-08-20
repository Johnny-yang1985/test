# 페이지 52

Chapter 44
Power Management Controller (PMC for S32K358, 
S32K328, S32K338, and S32K348)
44.1 Overview
PMC is the power management controller for the S32K3 family of microcontrollers. It provides multiple power options to allow you 
to optimize power consumption for the level of functionality needed. It includes internal voltage regulators, POR, and the integrated 
low/high voltage detect system with reset (brown-out) capability. The voltage regulator requires a 3.3 V or 5 V input to generate 
all the required secondary supplies.
44.1.1 Block diagram
The following figure shows the block diagram for this module.
SMPS (DCDC)
Flash
memory
LPCMP_n
FXOSC
SIRC
FIRC
SXOSC
Registers
- Standby domain
- Standby domain (optional)
- On during FPM (Run mode) only
PLLDIG0
MC_RGM
WKPU
MC_PCU
PIT_0
(RTI)
SOG
(Run)
SRAM
64 kB
RTC
DCM
PLLDIG1
TempSense
SOG
(Standby)
ADC_n
LPM
PMC
LPM (V15)
V11_STANDBY
V25
V11_RUN
V11_STANDBY
V11_STANDBY
(Triple bond)
Last Mile
distributed
regulator
FPM
SW*
SW*
optional
optional
VIN
VC_BJT
VDD_HV_A
VREFH
VREFL
V11
V25
VSS
VSS_DCDC
PMOS_CTRL
VDD_DCDC
VDD_HV_B
VRC_CTRL
Pads
GPIO
VDD_HV_A
VSS
Pads
GPIO
VDD_HV_B
VSS
(Triple bond)
V15
Figure 188. PMC block diagram
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1710 / 5251


---
# 페이지 53

44.1.2 Features
PMC includes the following features:
• Combination of internal and external voltage regulator options, offering RUN and Standby modes
• Active POR providing brown-out detect
• LVR for all system-relevant power domains
• LVD and HVD as indication for software
44.2 Functional description
The following sections describe functional details of the PMC.
44.2.1 Modes of operation
PMC provides two basic modes of operation for the voltage regulators and monitors:
• FPM, which is used on chip-level in RUN modes: For high-current consumption
• LPM, which is used on chip-level for Standby modes: For low-current consumption
44.2.2 Reset
The POR and all LVRs are combined into one single MCU POR.
After an MCU POR event, it can be determined which power domain caused it, by reading in the PMC_LVSC register, the POR 
flag, and LVR flags.
After an initial power ramp up of the MCU in the PMC_LVSC register, the POR flag and the LVR flags are all set to 1. The Go/Nogo 
flags have an arbitrary value.
 
After an initial power ramp up, all flags in the LVSC register must be cleared (by writing 0xFFFFFFFF to the 
LVSC register).
  NOTE  
Because the flags are sticky bits, it is required to clear them before usage. So, in case of an unexpected MCU POR, the source 
of the problem can be tracked and debugged by reading the flags in the LVSC register.
44.2.3 Interrupts
PMC includes two interrupt sources:
• HVD interrupt: It combines all HVD monitors into one interrupt source. Interrupt enable is the HVDIE field in the 
CONFIG register.
• LVD interrupt: This is the interrupt for the LVD5A monitor. Interrupt enable is the LVDIE field in the CONFIG register.
See the PMC Configuration Register (CONFIG) and Low Voltage Status and Control Register (LVSC) registers for details.
44.3 Signals
This table describes the PMC module signals.
Table 256. Signal Description
Signal
I/O
Description
VDD_HV_A
Supply input
This is the primary high-voltage supply input to PMC. VDD_HV_A is 
used for the PMC internal precision references. After the VDD_HV_A 
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K358, S32K328, S32K338, and S32K348)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1711 / 5251


---
# 페이지 54

Table 256. Signal Description (continued)
Signal
I/O
Description
domain is powered up, it must be kept powered at all times of 
operation (FPM and LPM).
VDD_HV_B
Supply input
This is the secondary high-voltage supply input supervised by the 
PMC. After the VDD_HV_B domain is powered up, it must be kept 
powered at all times of operation (FPM and LPM).
V25
Supply output
V25 power supply domain is driven by a fully integrated low-dropout 
linear voltage regulator. It supplies the Flash memory and (via a 
double bond) the clock modules.
V15
Supply input
This is the high-current input for core/logic supply that can be fed by 
an external BJT or the SMPS or an external source.
VRC_CTRL
Output
VRC_CTRL connects to the base of external BJT, if this option is used 
to generate V15.
V11
Supply output
V11 is the core/logic supply. It is driven by a fully integrated low-
dropout linear voltage regulator.
VSS
Ground
VSS must be grounded. All VSS Pins need to be externally connected 
to the same ground node.
VDD_DCDC
Supply input
This is the power supply domain for the SMPS gate driver and must 
be shorted with the source voltage of the external power FET. An 
off-chip decoupling capacitor between VDD_DCDC and ground is 
required. See Datasheet for the recommended value.
 
If SMPS (DCDC) mode is used and the PMC is in 
low power mode, it must be ensured that SMPS 
supply input VDD_DCDC is fully operational and 
loadable before wake-up from low power mode. 
Otherwise a low voltage reset might occur on wake-
up.
  NOTE  
VSS_DCDC
Ground
This is the power ground for the SMPS gate driver and must be 
shorted with the main ground node and the ground node of the 
external Schottky diode.
PMOS_CTRL
Output
This is the gate driver output for the external power FET for the SMPS 
regulator.
44.4 PMC register descriptions
44.4.1 PMC memory map
This section includes the PMC module memory map and detailed descriptions for all the registers.
PMC_S32K358 base address: 402E_8000h
NXP Semiconductors
Power Management Controller (PMC for S32K358, S32K328, S32K338, and S32K348)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1712 / 5251


---
# 페이지 55

Offset
Register
Width
(In bits)
Access
Reset value
0h
Low Voltage Status and Control Register (LVSC)
32
RW
See section
4h
PMC Configuration Register (CONFIG)
32
RW
0000_0083h
8h
SMPS Configuration Register (SMPSCONFIG)
32
RW
See section
Ch
Version ID register (VERID)
32
R
0400_0001h
44.4.2 Low Voltage Status and Control Register (LVSC)
Offset
Register
Offset
LVSC
0h
Function
This register contains status and control bits to support the low-voltage reset and low- or high-voltage detect function. When 
the PMC is in LPM, the low- or high-voltage detect systems are disabled.
 
For all flags that are not affected by reset (POR flag, all LVR flags, all GNG flags), in case a reset occurs at the same 
time while trying to clear the flags (by writing 1), the flag value is not defined appropriately. In this case, you need 
to clear the flag again after exit from reset.
  NOTE  
 
For the GNG flags, in case a GNG event occurs at the same time as the GNG flag is read, the flag value might not 
be defined appropriately. In such case, you need to read the flag twice and consider the value only if it both read 
values match.
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
PORF 
0
GNG1
1OS...
GNG2
5OS...
GNG1
1OS...
GNG2
5OS...
LVR11
LPF 
LVR11
F 
LVR25
LPF 
LVR25
F 
LVRBL
PF 
LVRB
F 
LVRAL
PF 
LVRA
F 
W
W1C
W1C
W1C
W1C
W1C
W1C
W1C
W1C
W1C
W1C
W1C
W1C
W1C
Reset
u
0
0
0
u
u
u
u
u
u
u
u
u
u
u
u
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
HVD1
5S 
Reserv
ed 
LVD5A
S 
HVD1
1S 
HVD2
5S 
HVDB
S 
HVDA
S 
0
HVD1
5F 
0
LVD5A
F 
HVD1
1F 
HVD2
5F 
HVDB
F 
HVDA
F 
W
W1C
W1C
W1C
W1C
W1C
W1C
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
0
0
0
0
0
0
NXP Semiconductors
Power Management Controller (PMC for S32K358, S32K328, S32K338, and S32K348)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1713 / 5251


---
# 페이지 56

Fields
Field
Function
31
PORF
POR flag
Indicates that a power-on reset event has occurred. Writing 1 to this field clears it, and other reset 
sources have no effect.
0b - No power-on reset event has occurred
1b - Power-on reset event has occurred
30-28
—
Reserved
27
GNG11OSC2F
Go/NoGo detect flag on 2nd PLL part of V11 domain
Indicates that the Go/NoGo sensor has detected a low voltage on the V11 domain in FPM. This applies 
to only that part of the domain which supplies the 2nd PLL. Writing 1 to the field clears it, and other reset 
sources have no effect.
0b - No event has occurred
1b - NoGo event has occurred
26
GNG25OSC2F
GO/NoGo detect flag on 2nd PLL part of V25 domain
Indicates that the Go/NoGo sensor has detected a low voltage on the V25 domain in FPM. This applies 
to only that part of the domain which supplies the 2nd PLL. Writing 1 to the field clears it, and other reset 
sources have no effect.
0b - No event has occurred
1b - NoGo event has occurred
25
GNG11OSCF
Go/NoGo detect flag on Osc part of V11 domain
Indicates that the Go/NoGo sensor has detected a low voltage on the V11 domain in FPM. This applies 
to only that part of the domain which supplies the 1.1V clocking modules (e.g. PLL, IRC). Writing 1 to the 
field clears it, and other reset sources have no effect.
0b - No event has occurred
1b - NoGo event has occurred
24
GNG25OSCF
GO/NoGo detect flag on Osc part of V25 domain
Indicates that the Go/NoGo sensor has detected a low voltage on the V25 domain in FPM. This applies 
to only that part of the domain which supplies the 2.5V clocking modules (e.g. PLL, XOSC and IRC ). 
Writing 1 to the field clears it, and other reset sources have no effect.
0b - No event has occurred
1b - NoGo event has occurred
23
LVR11LPF
LVR11LP flag on V11 domain
Indicates that a low-voltage reset event has occurred on the 1.1V V11 power domain (FPM or LPM). 
Writing 1 to the field clears it, and other reset sources have no effect.
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K358, S32K328, S32K338, and S32K348)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1714 / 5251


---
# 페이지 57

Table continued from the previous page...
Field
Function
0b - No low-voltage reset event has occurred
1b - Low-voltage reset event has occurred
22
LVR11F
LVR11 flag on V11 domain in FPM
Indicates that a low-voltage reset event has occurred on the 1.1V V11 power domain in the FPM. Writing 
1 to this field clears it, and other reset sources have no effect.
0b - No low-voltage reset event has occurred
1b - Low-voltage reset event has occurred
21
LVR25LPF
LVR25LP flag on V25 domain
Indicates that a low-voltage reset event has occurred on the V25 power domain (FPM or LPM). Writing 1 
to this field clears it, and other reset sources have no effect.
0b - No low-voltage reset event has occurred
1b - Low-voltage reset event has occurred
20
LVR25F
LVR25 flag on V25 domain in FPM
Indicates that a low-voltage reset event has occurred on the V25 power domain in FPM. Writing 1 to this 
field clears it, and other reset sources have no effect.
0b - No low-voltage reset event has occurred
1b - Low-voltage reset event has occurred
19
LVRBLPF
LVRBLP flag on VDD_HV_B domain
Indicates that a low-voltage reset event has occurred on the VDD_HV_B power domain (FPM or LPM). 
Writing 1 to this field clears it, and other reset sources have no effect.
0b - No low-voltage reset event has occurred
1b - Low-voltage reset event has occurred
18
LVRBF
LVRB flag on VDD_HV_B domain in FPM
Indicates that a low-voltage reset event has occurred on the VDD_HV_B power domain in FPM. Writing 1 
to this field clears it, and other reset sources have no effect.
0b - No low-voltage reset event has occurred
1b - Low-voltage reset event has occurred
17
LVRALPF
LVRALP flag on VDD_HV_A domain
Indicates that a low-voltage reset event has occurred on the VDD_HV_A power domain (FPM or LPM). 
Writing 1 to this field clears it, and other reset sources have no effect.
0b - No low-voltage reset event has occurred
1b - Low-voltage reset event has occurred
16
LVRA flag on VDD_HV_A domain in FPM
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K358, S32K328, S32K338, and S32K348)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1715 / 5251


---
# 페이지 58

Table continued from the previous page...
Field
Function
LVRAF
Indicates that a low-voltage reset event has occurred on the VDD_HV_A power domain in FPM. Writing 1 
to this field clears it, and other reset sources have no effect.
0b - No low-voltage reset event has occurred
1b - Low-voltage reset event has occurred
15
—
Reserved
14
HVD15S
HVD15 status on V15 domain in FPM
Shows the status of the high-voltage detect, HVD15, on the V15 power domain. This feature is only 
available in FPM and disabled in LPM.
0b - Voltage on V15 is below high-voltage detect threshold or LPM.
1b - Voltage on V15 is above high-voltage detect threshold and FPM.
13
—
Reserved, ignore value
Reserved, ignore value
12
LVD5AS
LVD5A status on VDD_HV_A domain in FPM
Shows the status of the 5V low-voltage detect, LVD5A, on the VDD_HV_A power domain. This monitor 
indicates if the voltage is below a certain threshold, which is set slightly below 4.5V (see Datasheet for 
exact value). The feature is only available in FPM and disabled in LPM. After a reset or wakeup from 
LPM, the software should clear the LVD5AF flag and check the status bit LVD5AS to determine voltage 
level on VDD_HV_A supply.
0b - Voltage on VDD_HV_A is above low-voltage detect threshold
1b - Voltage on VDD_HV_A is below low-voltage detect threshold
11
HVD11S
HVD11 status on V11 domain in FPM
Shows the status of the high-voltage detect, HVD11, on the V11 power domain. This feature is only 
available in FPM and disabled in LPM.
0b - Voltage on V11 is below high-voltage detect threshold or LPM.
1b - Voltage on V11 is above high-voltage detect threshold and FPM.
10
HVD25S
HVD25 status on V25 domain in FPM
Shows the status of the high-voltage detect, HVD25, on the V25 power domain. The feature is only 
available in FPM and disabled in LPM.
0b - Voltage on V25 is below high-voltage detect threshold or LPM.
1b - Voltage on V25 is above high-voltage detect threshold and FPM.
9
HVDBS
HVDB status on VDD_HV_B domain in FPM
Shows the status of the high-voltage detect, HVDB, on the VDD_HV_B power domain. The feature is 
only available in FPM and disabled in LPM.
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K358, S32K328, S32K338, and S32K348)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1716 / 5251


---
# 페이지 59

Table continued from the previous page...
Field
Function
0b - Voltage on VDD_HV_B is below high-voltage detect threshold or LPM.
1b - Voltage on VDD_HV_B is above high-voltage detect threshold and FPM.
8
HVDAS
HVDA status on VDD_HV_A domain in FPM
Shows the status of the high-voltage detect HVDA on the VDD_HV_A power domain. The feature is only 
available in FPM and disabled in LPM.
0b - Voltage on VDD_HV_A is below high-voltage detect threshold or LPM.
1b - Voltage on VDD_HV_A is above high-voltage detect threshold and FPM.
7
—
Reserved
6
HVD15F
HVD15 flag on V15 domain in FPM
PMC writes 1 to this field when the HVD15S status field changes. To clear HVD15F, write 1 to it. If 
enabled, HVD15F causes an interrupt request.
0b - HVD15S has not changed.
1b - HVD15S has changed.
5
—
Reserved
4
LVD5AF
LVD5A flag on VDD_HV_A domain in FPM
PMC writes 1 to this field when LVD5AS status field changes. To clear LVD5AF, write 1 to it. If enabled, 
LVD5AF causes an interrupt request.
0b - LVD5AS has not changed.
1b - LVD5AS has changed.
3
HVD11F
HVD11 flag on V11 domain in FPM
PMC writes 1 to this field when the HVD11S status field changes. To clear HVD11F, write 1 to it. If 
enabled, HVD11F causes an interrupt request.
0b - HVD11S has not changed.
1b - HVD11S has changed.
2
HVD25F
HVD25 flag on V25 domain in FPM
PMC writes 1 to the HVD25F field when HVD25S status field changes. To clear HVD25F, write 1 to it. If 
enabled, HVD25F causes an interrupt request.
0b - HVD25S has not changed.
1b - HVD25S has changed.
1
HVDB flag on VDD_HV_B domain in FPM
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K358, S32K328, S32K338, and S32K348)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1717 / 5251


---
# 페이지 60

Table continued from the previous page...
Field
Function
HVDBF
PMC writes 1 to the HVDBF field when HVDBS status field changes. To clear HVDBF, write 1 to it. If 
enabled, HVDBF causes an interrupt request.
0b - HVDBS has not changed.
1b - HVDBS has changed.
0
HVDAF
HVDA flag on VDD_HV_A domain in FPM
PMC writes 1 to the HVDAF field when HVDAS status field changes. To clear HVDAF, write 1 to it. If 
enabled, HVDAF causes an interrupt request.
0b - HVDAS has not changed.
1b - HVDAS has changed.
44.4.3 PMC Configuration Register (CONFIG)
Offset
Register
Offset
CONFIG
4h
Function
This register configures the various PMC options.
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
LVDIE 
HVDIE 
LMSM
PSEN 
0
LVRBL
PEN 
LPM25
EN 
FAST
REC 
LMBC
TLEN 
LMEN 
W
0
0
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
0
0
0
0
0
1
1
Fields
Field
Function
31-10
—
Reserved
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K358, S32K328, S32K338, and S32K348)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1718 / 5251


---
# 페이지 61

Table continued from the previous page...
Field
Function
9
LVDIE
Low voltage detect interrupt enable
Enables hardware interrupt requests if LVD5AF is set. LVD interrupt must be disabled before going into 
LPM.
0b - LVD hardware interrupt is disabled (use polling).
1b - Request an LVD hardware interrupt when LVD5AF=1.
8
HVDIE
High voltage detect interrupt enable
Enables hardware interrupt requests if any of the following flags is set: HVDAF, HVDBF, HVD25F, 
HVD11F.
0b - HVD hardware interrupt is disabled (use polling).
1b - Request an HVD hardware interrupt when HVDAF=1, HVDBF=1, HVD25F=1, or HVD11F=1.
7
LMSMPSEN
V15 Switched-mode power supply enable bit
Enables the SMPS regulator (Switched-mode power supply), which regulates from VDD_DCDC down 
to 1.5V on V15 pin to supply the Last Mile regulator. As LMSMPSEN=1 after startup or reset, in case 
SMPS is not used, software must write LMBSMPSEN=0 after each reset to turn the feature off. Once 
LMSMPSEN=0 it can no longer be written 1 until next reset.
0b - Switched-mode power supply (SMPS) for V15 disabled
1b - Switched-mode power supply (SMPS) for V15 enabled
6-5
—
Reserved
4
LVRBLPEN
LVRBLP enable bit during LPM
Controls whether the low-voltage reset detection (LVRBLP) on the VDD_HV_B power domain is active or 
inactive in LPM
0b - Low-voltage reset detection is disabled in LPM.
1b - Low-voltage reset detection is enabled in LPM.
3
LPM25EN
V25 domain enable bit during LPM
Enables a low power V25 regulator and the low-voltage reset detection (LVR25LP) in LPM. In FPM this 
low power regulator is always off.
0b - V25 regulator and LVR25LP are disabled in LPM.
1b - V25 regulator and LVR25LP are enabled in LPM.
2
FASTREC
Fast recovery from LPM enable bit
Controls the recovery time from LPM to FPM. This causes a higher current demand on V15, and this 
translates to a higher current demand on the primary side of the V15 supply.
0b - Normal recovery time from LPM
1b - Fast recovery time from LPM
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K358, S32K328, S32K338, and S32K348)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1719 / 5251


---
# 페이지 62

Table continued from the previous page...
Field
Function
1
LMBCTLEN
V15 external BJT enable bit
This field must be set to 1 if external BJT between VDD_HV_A and V15 is used on the PCB. The 
base of this BJT must be connected to the VRC_CTRL pin and is controlled by the PMC to regulate a 
voltage of 1.5V on V15 pin to supply the Last Mile Regulator. As LMBCTLEN=1 after startup or reset, in 
case BJT is not used, software must write LMBCTLEN=0 after each reset to turn the feature off. Once 
LMBCTLEN=0 it can no longer be written 1 until next reset.
0b - External BCTL regulator for V15 disabled
1b - External BCTL regulator for V15 enabled
0
LMEN
Last Mile regulator enable bit
Enables the Last Mile regulator, which regulates an external 1.5V voltage on V15 down to the core and 
logic supply (V11 power domain), which is typically 1.1V. As the Last Mile regulator is always enabled on 
this device, LMEN bit is read-only and always reads 1.
44.4.4 SMPS Configuration Register (SMPSCONFIG)
Offset
Register
Offset
SMPSCONFIG
8h
Function
This register configures the various options of the Switched-mode power supply (SMPS) generating the V15 (1.5V input supply 
to the last mile regulator).
Table 257. SMPS configurations for driving PMOS_CTRL pin
CFG[3:0] bits
PMOS_CTRL Frequency
PMOS_CTRL Duty cycle 3V
PMOS_CTRL Duty cycle 5V
0000
470 kHz
58.8%
47.1%
0001
470 kHz
64.7%
52.9%
0010
470 kHz
52.9%
41.2%
0011
533 kHz
60%
46.7%
0100
533 kHz
66.7%
53.3%
0101
533 kHz
53.3%
40%
0110
421 kHz
57.9%
47.4%
0111
421 kHz
63.2%
52.6%
1000
421 kHz
52.6%
42.1%
1001 to 1110
Reserved
Reserved
Reserved
1111
8 MHz / (PERIOD[4:0]+1)
ONTIME3V[4:0] / 
(PERIOD[4:0]+1)
ONTIME5V[4:0] / 
(PERIOD[4:0]+1)
NXP Semiconductors
Power Management Controller (PMC for S32K358, S32K328, S32K338, and S32K348)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1720 / 5251


---
# 페이지 63

Table 258. 8 MHz IRC Dither configurations
DITHERCFG[1:0] bits
Dither Amplitude
Dither Frequency
00
+/- 0.4 MHz
400 kHz
01
+/- 0.6 MHz
286 kHz
10
+/- 0.8 MHz
222 kHz
11
+/- 1 MHz
182 kHz
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
ONTIME5V 
PGAT
ES 
0
ONTIME3V 
W
Reset
0
0
0
0
1
0
0
0
u
0
0
0
1
0
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
0
PERIOD 
DITHE
REN 
DITHERCFG 
LPM15
EN 
CFG 
W
Reset
0
0
0
0
1
1
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
31-29
—
Reserved
28-24
ONTIME5V
SMPS Duty cycle for 5V range
These bits determine the duty cycle of the output signal at PMOS_CTRL pin. This duty cycle is applied 
while VDD_DCDC is greater or equal than 4V.
It calculates as follows: Duty_pmos_ctrl = ONTIME3V[4:0] / (PERIOD[4:0] + 1)
23
PGATES
PMOS_CTRL Status Bit
This read-only bit reflects the status of the PMOS_CTRL pin.
0b - PMOS_CTRL pin driven to VSS_DCDC (which is connect to GND)
1b - PMOS_CTRL pin driven to VDD_DCDC voltage
22-21
—
Reserved
20-16
ONTIME3V
SMPS Duty cycle for 3V range
These bits determine the duty cycle of the output signal at PMOS_CTRL pin. This duty cycle is applied 
while VDD_DCDC is smaller than 4V.
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K358, S32K328, S32K338, and S32K348)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1721 / 5251


---
# 페이지 64

Table continued from the previous page...
Field
Function
It calculates as follows: Duty_pmos_ctrl = ONTIME3V[4:0] / (PERIOD[4:0] + 1)
15-13
—
Reserved
12-8
PERIOD
SMPS Period
These bits determine the frequency of the output signal at PMOS_CTRL pin.
The frequency calculates as follows: Freq_pmos_ctrl = 8 MHz / (PERIOD[4:0] + 1)
7
DITHEREN
IRC Dither Enable
This bit enables dithering of the 8MHz IRC. The amplitude and frequency of the dithering is determined 
by the DITHERCFG[1:0] bits.
0b - 8MHz IRC dithering disabled
1b - 8MHz IRC dithering enabled
6-5
DITHERCFG
IRC Dither Configuration
Selects the IRC dithering amplitude and frequency.
This feature spreads the frequency spectrum of driving the PMOS_CTRL pin to reduce radiated emission. 
To change the value:
1. Write 0 to DITHEREN.
2. Write the dither configuration (DITHERCFG[1:0]).
3. Write 1 to DITHEREN.
See Table 258 for configuration options.
4
LPM15EN
V15 domain enable bit during LPM
Enables the V15 in LPM. This is useful for fast recovery to FPM when using the SMPS mode to generate 
the V15. This feature is only active in LPM, in FPM it is turned off. For this purpose there is a small LDO 
inside the PMC that regulates the V15 to target value during LPM.
 
LPM15EN bit is only allowed to use, when using the SMPS to generate the V15. For other 
options to generate the V15 it is forbidden and software should always write 0 to LPM15EN.
  NOTE  
0b - V15 not kept on target in LPM
1b - V15 kept on target in LPM
3-0
CFG
SMPS configuration select
These bits select a configuration for frequency and duty cycle (ontime) of the Switched-mode power 
supply driving via PMOS_CTRL the external power FET according to Table 257.
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K358, S32K328, S32K338, and S32K348)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1722 / 5251


---
# 페이지 65

Table continued from the previous page...
Field
Function
 
As seen in the table CFG[3:0] = 1111 allows for free customization of the PERIOD[4:0], 
ONTIME5V[4:0] and ONTIME3V[3:0] bits. If choosing this option consider carefully the 
value of these bits. To ensure the proper function of the SMPS, and to keep the 
EMI in check, the switching frequency and duty cycle must be programmed within a 
reasonable range.
  NOTE  
44.4.5 Version ID register (VERID)
Offset
Register
Offset
VERID
Ch
Function
This register returns the major and minor version numbers of hardware implementation.
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
MAJOR 
MINOR 
W
Reset
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
LMFE
AT 
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
31-24
MAJOR
Major version number
Returns the version number for the specification
23-16
MINOR
Minor version number
Returns the version number for the hardware implementation
15-1
Reserved
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K358, S32K328, S32K338, and S32K348)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1723 / 5251


---
# 페이지 66

Table continued from the previous page...
Field
Function
—
0
LMFEAT
Last Mile Regulator Feature
This read-only field shows if the Last Mile regulator feature is available.
0b - No Last Mile regulator
1b - Last Mile regulator (1.5V to 1.1V) is available
44.5 Glossary
FPM
Full Performance mode
HVD
High voltage detect
IRC
Internal RC oscillator
LM
Last mile regulator
LPM
Low Performance mode
LVD
Low voltage detect
LVR
Low voltage reset
NVM
Nonvolatile memory
POR
Power on reset
XOSC
External crystal oscillator
SMPS
Switched-mode power supply
NXP Semiconductors
Power Management Controller (PMC for S32K358, S32K328, S32K338, and S32K348)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1724 / 5251


---