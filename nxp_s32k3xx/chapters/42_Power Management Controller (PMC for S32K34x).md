# 페이지 27

Chapter 42
Power Management Controller (PMC for S32K34x, 
S32K322, S32K324, and S32K314)
42.1 Overview
PMC is the power management controller for the S32K3 family of microcontrollers. It provides multiple power options to allow you 
to optimize power consumption for the level of functionality needed. It includes internal voltage regulators, POR, and the integrated 
low/high voltage detect system with reset (brown-out) capability. The voltage regulator requires a 3.3 V or 5 V input to generate 
all the required secondary supplies.
42.1.1 Block diagram
The following figure shows the block diagram for this module.
optional
VDD_HV_A
V25
V11 (RUN)
PLL
& CTS
SOG (STANDBY)
SIRC, FIRC,
SXOSC
VSS
GPIO
Pads
ADC
CMP
VREFH
VREFL
Flash
VDD_HV_B
PMC
V15
VRC_CTRL
V25
(double bond)
VDD_HV_B
GPIO
Pads
VDD_HV_A
VSS
SOG (RUN)
sw
VSS
VSS
VSS
V11
(double bond)
V11 
(STANDBY)
Last Mile
distributed
regulator
VSS
VSS
VC_BJT
Boot
FPM
FXOSC
V11 
(STANDBY)
LPM
[V11 (STANDBY)]
Figure 186. PMC block diagram
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1685 / 5251


---
# 페이지 28

42.1.2 Features
PMC includes the following features:
• Combination of internal and external voltage regulator options, offering RUN and Standby modes
• Active POR providing brown-out detect
• LVR for all system-relevant power domains
• LVD and HVD as indication for software
42.2 Functional description
The following sections describe functional details of the PMC.
42.2.1 Modes of operation
PMC provides two basic modes of operation for the voltage regulators and monitors:
• FPM, which is used on chip-level in RUN modes: For high-current consumption
• LPM, which is used on chip-level for Standby modes: For low-current consumption
42.2.2 Reset
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
42.2.3 Interrupts
PMC includes two interrupt sources:
• HVD interrupt: It combines all HVD monitors into one interrupt source. Interrupt enable is the HVDIE field in the CONFIG 
register. See the PMC Configuration Register (CONFIG) and Low Voltage Status and Control Register (LVSC) registers 
for details.
• LVD interrupt: It combines the LVD15 and LVD5A monitors into one interrupt source. Interrupt enable is the LVDIE field in the 
CONFIG register. See the CONFIG and LVSC registers for details.
42.3 Signals
This table describes the PMC module signals.
Table 254. Signal Description
Signal
I/O
Description
VDD_HV_A
Supply input
This is the primary high-voltage supply input to PMC. VDD_HV_A is 
used for the PMC internal precision references. After the VDD_HV_A 
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K34x, S32K322, S32K324, and S32K314)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1686 / 5251


---
# 페이지 29

Table 254. Signal Description (continued)
Signal
I/O
Description
domain is powered up, it must be kept powered at all times of 
operation (FPM and LPM).
VDD_HV_B1
Supply input
This is the secondary high-voltage supply input supervised by the 
PMC. After the VDD_HV_B domain is powered up, it must be kept 
powered at all times of operation (FPM and LPM).
V25
Supply output
V25 power supply domain is driven by a fully integrated low-dropout 
linear voltage regulator. It supplies the Flash memory and (via a 
double bond) the clock modules.
V151
Supply input
This is the high-current input for core/logic supply that can be fed by 
an external BJT or another source.
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
1. VDD_HV_B and V15 not present in S32K312 and S32K311.
42.4 PMC register descriptions
42.4.1 PMC memory map
This section includes the PMC module memory map and detailed descriptions for all the registers.
PMC_S32K344 base address: 402E_8000h
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
See section
Ch
Version ID register (VERID)
32
R
0200_0001h
42.4.2 Low Voltage Status and Control Register (LVSC)
Offset
Register
Offset
LVSC
0h
Function
This register contains status and control bits to support the low-voltage reset and low- or high-voltage detect function. When 
the PMC is in LPM, the low- or high-voltage detect systems are disabled.
NXP Semiconductors
Power Management Controller (PMC for S32K34x, S32K322, S32K324, and S32K314)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1687 / 5251


---
# 페이지 30

 
For all flags that are not affected by reset (POR flag, all LVR flags, all GNG flags), in case a reset occurs at the same 
time while trying to clear the flags (by writing 1), the flag value is not defined appropriately. In this case, you need 
to clear the flag again after exit from reset.
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
LVRBF 
LVRAL
PF 
LVRAF 
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
Reset
u
0
0
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
LVD15
S 
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
LVD15
F 
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
0
0
0
0
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
30-26
—
Reserved
25
GNG11OSCF
Go/NoGo detect flag on Osc part of V11 domain
Indicates that the Go/NoGo sensor has detected a low voltage on the V11 domain in FPM. This applies 
to only that part of the domain which supplies the 1.1V clocking modules (for example, PLL). Writing 1 to 
the field clears it, and other reset sources have no effect.
0b - No event has occurred
1b - NoGo event has occurred
24
GNG25OSCF
GO/NoGo detect flag on Osc part of V25 domain
Indicates that the Go/NoGo sensor has detected a low voltage on the V25 domain in FPM. This applies 
to only that part of the domain which supplies the 2.5V clocking modules (for example, XOSC and IRC). 
Writing 1 to the field clears it, and other reset sources have no effect.
0b - No event has occurred
1b - NoGo event has occurred
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K34x, S32K322, S32K324, and S32K314)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1688 / 5251


---
# 페이지 31

Table continued from the previous page...
Field
Function
23
LVR11LPF
LVR11LP flag on V11 domain
Indicates that a low-voltage reset event has occurred on the 1.1V V11 power domain (FPM or LPM). 
Writing 1 to the field clears it, and other reset sources have no effect.
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
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K34x, S32K322, S32K324, and S32K314)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1689 / 5251


---
# 페이지 32

Table continued from the previous page...
Field
Function
0b - No low-voltage reset event has occurred
1b - Low-voltage reset event has occurred
16
LVRAF
LVRA flag on VDD_HV_A domain in FPM
Indicates that a low-voltage reset event has occurred on the VDD_HV_A power domain in FPM. Writing 1 
to this field clears it, and other reset sources have no effect.
0b - No low-voltage reset event has occurred
1b - Low-voltage reset event has occurred
15-14
—
Reserved
13
LVD15S
LVD15 status on V15 domain in FPM
Shows the status of the 1.5V low-voltage detect, LVD15, on the V15 power domain. This monitor 
indicates when the V15 voltage level generated from external is on target. This feature is available only 
in FPM and disabled in LPM. After a reset or wakeup from LPM, the software should clear the LVD15F 
flag and check the status bit LVD15S to determine voltage level on V15 supply.
0b - Voltage on V15 is above low-voltage detect threshold or LPM.
1b - Voltage on V15 is below low-voltage detect threshold and FPM.
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
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K34x, S32K322, S32K324, and S32K314)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1690 / 5251


---
# 페이지 33

Table continued from the previous page...
Field
Function
9
HVDBS
HVDB status on VDD_HV_B domain in FPM
Shows the status of the high-voltage detect, HVDB, on the VDD_HV_B power domain. The feature is 
only available in FPM and disabled in LPM.
0b - Voltage on VDD_HV_B is below high-voltage detect threshold or LPM.
1b - Voltage on VDD_HV_B is above high-voltage detect threshold and FPM.
8
HVDAS
HVDA status on VDD_HV_A domain in FPM
Shows the status of the high-voltage detect HVDA on the VDD_HV_A power domain. The feature is only 
available in FPM and disabled in LPM.
0b - Voltage on VDD_HV_A is below high-voltage detect threshold or LPM.
1b - Voltage on VDD_HV_A is above high-voltage detect threshold and FPM.
7-6
—
Reserved
5
LVD15F
LVD15 flag on V15 domain in FPM
PMC writes 1 to the LVD15F field when the LVD15S status field changes. To clear LVD15F, write 1 to it. 
If enabled, LVD15F causes an interrupt request.
0b - LVD15S has not changed.
1b - LVD15S has changed.
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
Power Management Controller (PMC for S32K34x, S32K322, S32K324, and S32K314)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1691 / 5251


---
# 페이지 34

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
42.4.3 PMC Configuration Register (CONFIG)
Offset
Register
Offset
CONFIG
4h
Function
If the Last Mile Regulator option is not available on your device ( Version ID register (VERID) register: LMFEAT=0), then the 
bits LMEN, LMBCTLEN, LMAUTOEN and LMSTAT fields can not be written and read always 0.
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
LMST
AT 
LMAU
TOEN 
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
u
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
LVDIE 
HVDIE 
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
31-18
Reserved
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K34x, S32K322, S32K324, and S32K314)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1692 / 5251


---
# 페이지 35

Table continued from the previous page...
Field
Function
—
17
LMSTAT
Last Mile regulator status bit
This bits reflects the current status of the Last Mile regulator. This information is required as when auto 
turn over feature is enabled (LMAUTOEN=1) the PMC will switch automatically between Boot regulator 
and Last Mile regulator depending on the V15 status (LVD15S).
0b - Last Mile Regulator is off
1b - Last Mile Regulator is on
16
LMAUTOEN
Last Mile regulator auto turn over bit
Enables to turn over automatically from Boot Regulator Mode to Last Mile regulator mode and vice versa 
depending on the V15 voltage status (LVD15S). As long as LMEN=0 software must make sure that the 
system clock is on FIRC clock or slower. To use higher clock speed software must set LMEN=1.
0b - Auto turnover disabled
1b - Auto turnover enabled
15-10
—
Reserved
9
LVDIE
Low voltage detect interrupt enable
Enables hardware interrupt requests if any of the following flags is set: LVD5AF, LVD15F. LVD interrupt 
must be disabled before going into LPM.
0b - LVD hardware interrupt is disabled (use polling).
1b - Request an LVD hardware interrupt when LVDA5F=1 or LVD15F=1.
8
HVDIE
High voltage detect interrupt enable
Enables hardware interrupt requests if any of the following flags is set: HVDAF, HVDBF, HVD25F, 
HVD11F.
0b - HVD hardware interrupt is disabled (use polling).
1b - Request an HVD hardware interrupt when HVDAF=1, HVDBF=1, HVD25F=1, or HVD11F=1.
7-5
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
V25 domain enable bit during LPM
Table continues on the next page...
NXP Semiconductors
Power Management Controller (PMC for S32K34x, S32K322, S32K324, and S32K314)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1693 / 5251


---
# 페이지 36

Table continued from the previous page...
Field
Function
LPM25EN
Controls whether the V25 regulator and low-voltage reset detection (LVR25LP) are active or inactive in 
LPM
0b - V25 regulator and LVR25LP are disabled in LPM.
1b - V25 regulator and LVR25LP are enabled in LPM.
2
FASTREC
Fast recovery from LPM enable bit
Controls the recovery time from LPM to FPM. At recovery from LPM, all the tank capacitors from the 
secondary supplies have to be recharged. This causes a high-current demand, which might not be 
met by the supply driving the VDD_HV_A primary domain. When selecting the fast recovery time, the 
current for recharging is approximately three times higher than that for FASTREC=0. The application 
must determine from the drive capability of the external VDD_HV_A regulator, the size of tank caps on 
the secondary supply pins and the selected recovery time if this is sufficient to start up from LPM in time.
0b - Normal recovery time from LPM
1b - Fast recovery time from LPM
1
LMBCTLEN
Last Mile regulator base control enable bit
This field must be set to 1 if external BJT between VDD_HV_A and V15 is used on the PCB. The 
base of this BJT must be connected to the VRC_CTRL pin and is controlled by the PMC to regulate a 
voltage of 1.5V on V15 pin. After setting LMBCTLEN=1 the software has to wait for 15us (FASTREC=1) 
respectively 50us (FASTREC=0) before polling LVD15S=0 and then setting LMEN=1. This respects the 
softstart time of the V15 regulator. If LMAUTOEN=1 then LMBCTLEN can be left enabled when going 
into LPM, the hardware will turn the regulator off and back on automatically after recovery from LPM.
0b - External BCTL regulator for V15 disabled
1b - External BCTL regulator for V15 enabled
0
LMEN
Last Mile regulator enable bit
Enables the Last Mile regulator, which regulates an external 1.5V voltage on V15 down to the core and 
logic supply (V11 power domain), which is typically 1.1V. Setting LMEN=1 hands over the V11 voltage 
generation from the Boot regulator to the Last Mile regulator. The software must ensure that before 
enabling the Last Mile regulator, the voltage on V15 is sufficiently high as indicated by the LVD15S 
status field (LVD15S=0). To use external BJT between VDD_HV_A and V15, the LMBCTLEN field must 
be set before the LMEN field, and the software must wait until 1.5V is up (LVD15S=0). If LMAUTOEN=0 
then to disable the Last Mile regulator, LMEN and LMBCTLEN must be cleared simultaneously (single 
register write). The software must disable (LMEN=0) the Last Mile regulator before going into LPM. After 
setting LMEN=1, software must wait a minimum time of 1.5us before changing clock rate.
0b - Last Mile regulator is disabled.
1b - Last Mile regulator is enabled.
NXP Semiconductors
Power Management Controller (PMC for S32K34x, S32K322, S32K324, and S32K314)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1694 / 5251


---
# 페이지 37

42.4.4 Version ID register (VERID)
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
—
Reserved
0
LMFEAT
Last Mile Regulator Feature
This read-only field shows if the Last Mile regulator feature is available.
0b - No Last Mile regulator
1b - Last Mile regulator (1.5V to 1.1V) is available
42.5 Glossary
FPM
Full Performance mode
HVD
High voltage detect
NXP Semiconductors
Power Management Controller (PMC for S32K34x, S32K322, S32K324, and S32K314)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1695 / 5251


---
# 페이지 38

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
NXP Semiconductors
Power Management Controller (PMC for S32K34x, S32K322, S32K324, and S32K314)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1696 / 5251


---