# 페이지 600

Chapter 18
Crossbar Integrity Checker (XBIC)
18.1 Chip-specific XBIC information
18.1.1 XBIC instances and configuration
This chip has up to seven instances of XBIC. The following tables describes the instances and their configuration.
Table 67. XBIC instances
Instance
S32K388/S32K389
S32K358/S32K348/
S32K338/S32K328
S32K344/S32K324/S32K314/S32K342/
S32K322/S32K341
S32K310/
S32K311/
S32K312
XBIC_0
Yes
Yes
Yes
Yes
XBIC_1
Yes
Yes
Yes
No
XBIC_2
Yes
Yes
Yes
No
XBIC_3
Yes
No
Yes
No
XBIC_4
Yes
Yes
No
No
XBIC_5
Yes
No
No
No
XBIC_6
Yes
No
No
No
Table 68. XBIC configuration for S32K388/S32K389
Instance
Available on crossbar
Initiator and target assignments
XBIC_0
AXBS_0 (main)
Initiator 
port
Initiator module
Target 
port
Target module
M0
Cortex-M7_0 AHBM
S0
S32K388: Flash memory 
port 0
S32K389: Flash memory 0 
port 0
M1
DMA
S1
S32K388: Flash memory 
port 1
S32K389: Flash memory 1 
port 0
M2
HSE_B/AES_ACCEL
S2
PRAM_0
M3
GMAC_0
S3
S32K388: Cortex-M7 
TCM/ PRAM_2
S32K389: Cortex-M7 TCM/ 
PRAM_2 / PRAM_3
M4
Cortex-M7_1 AHBM
S4
S32K388: Flash memory 
Port 2
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
651 / 5251


---
# 페이지 601

Instance
Available on crossbar
Initiator and target assignments
S32K389: Flash memory 0 
Port 1
M5
Cortex-M7_2 AHBM
S5
QuadSPI
M6
GMAC_1
S6
PRAM_1
M7
Cortex-M7_3 AHBM
S7
S32K388: Flash memory 
port 3
S32K389: Flash memory 1 
port 1
XBIC_1
AXBS_1 (peripheral)
Initiator 
port
Initiator module
Target 
port
Target module
M0
Cortex-M7_0 AHBP
S0
AIPS_0
M1
DMA
S1
AIPS_1
M2
HSE_B/ ACE
S2
AIPS_2
M3
Cortex-M7_1 AHBP
S3
ACE target
M4
Cortex-M7_2 AHBP
M5
Cortex-M7_3 AHBP
XBIC_2
AXBS_2 (eDMA)
Initiator 
port
Initiator module
Target 
port
Target module
M0
eDMA
S0
System AXBS
S1
Peripheral AXBS
XBIC_3
AXBS_3 (Cortex-
M7 TCM)
Initiator 
port
Initiator module
Target 
port
Target module
M0
TCM PRAM AXBS
S0
Cortex-M7_0 TCM
S1
Cortex-M7_1 TCM
S2
Cortex-M7_2 TCM
S3
Cortex-M7_3 TCM
XBIC_4
AXBS_4 (TCM PRAM)
Initiator 
port
Initiator module
Target 
port
Target module
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
652 / 5251


---
# 페이지 602

Table 68. XBIC configuration for S32K388/S32K389 (continued)
Instance
Available on crossbar
Initiator and target assignments
M0
System AXBS
S0
PRAM_2
S1
TCM AXBS
S2
PRAM3 (Applicable for 
S32K389 only)
XBIC_5
AXBS_5 (ACE 
HSE_B AXBS)
Initiator 
port
Initiator module
Target 
port
Target module
M0
HSE_B
S0
Main AXBS
M1
ACE
S1
Peripheral AXBS
XBIC_6
AXBS_6 (ACE AXBS)
Initiator 
port
Initiator module
Target 
port
Target module
M0
ACE M0
S0
ACE HSE AXBS
M1
ACE M1
 
For AES_ACCEL initiator, only SRAM slave is applicable. Accessing other slaves from AES_ACCEL can result in 
unpredictable system behavior.
  NOTE  
Table 69. XBIC configuration for S32K358/S32K348/S32K338/S32K328
Instance
Available on crossbar
Initiator and target assignments
XBIC_0
AXBS_0 (main)
Initiator 
port
Initiator module
Target 
port
Target module
M0
Cortex-M7_0 AHBM
S0
Flash memory port 0
M1
DMA
S1
Flash memory port 1
M2
HSE_B
S2
PRAM_0
M3
GMAC
S3
Cortex-M7 TCM/ PRAM_2
M4
Cortex-M7_1 AHBM
S4
Flash memory Port 2
M5
Cortex-M7_2 AHBM
S5
QuadSPI
M6
uSDHC
S6
PRAM_1
S7
Flash memory port 3
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
653 / 5251


---
# 페이지 603

Table 69. XBIC configuration for S32K358/S32K348/S32K338/S32K328 (continued)
Instance
Available on crossbar
Initiator and target assignments
XBIC_1
AXBS_1 (peripheral)
Initiator 
port
Initiator module
Target 
port
Target module
M0
Cortex-M7_0 AHBP
S0
AIPS_0
M1
DMA
S1
AIPS_1
M2
HSE_B
S2
AIPS_2
M3
Cortex-M7_1 AHBP
M4
Cortex-M7_2 AHBP
XBIC_2
AXBS_2 (eDMA)
Initiator 
port
Initiator module
Target 
port
Target module
M0
eDMA
S0
System AXBS
S1
Peripheral AXBS
XBIC_3
AXBS_3 (Cortex-
M7 TCM)
Not applicable
XBIC_4
AXBS_4 (Cortex-M7 
TCM PRAM)
Initiator 
port
Initiator module
Target 
port
Target module
M0
System AXBS
S0
PRAM_2
S1
Cortex-M7_0 TCM
S2
Cortex-M7_1 TCM
S3
Cortex-M7_2 TCM
Table 70. XBIC configuration for S32K344/S32K324/S32K314/S32K342/S32K322/S32K341
Instance
Available on crossbar
Initiator and target assignments
XBIC_0
AXBS_0 (main)
Initiator 
port
Initiator module
Target 
port
Target module
M0
Cortex-M7_0 AHBM
S0
Flash memory port 0
M1
AXBS_2 S0
S1
Flash memory port 1
M2
HSE_B
S2
PRAM_0
M3
EMAC
S3
Cortex-M7 TCM
M41
Cortex-M7_1 AHBM
S4
Flash memory Port 2
S5
QuadSPI
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
654 / 5251


---
# 페이지 604

Instance
Available on crossbar
Initiator and target assignments
S6
PRAM_1
XBIC_1
AXBS_1 (peripheral)
Initiator 
port
Initiator module
Target 
port
Target module
M0
Cortex-M7_0 AHBP
S0
AIPS_0
M1
AXBS_2 S1
S1
AIPS_1
M2
HSE_B
S2
AIPS_2
M31
Cortex-M7_1 AHBP
1. These ports are reserved for S32K314.
XBIC_2
AXBS_2 (eDMA)
Initiator 
port
Initiator module
Target 
port
Target module
M0
eDMA
S0
AXBS_0 M1
S1
AXBS_1 M1
XBIC_3
AXBS_3 (Cortex-M7 
TCM) 2
Initiator 
port
Initiator module
Target 
port
Target module
M0
AXBS_0 S3
S0
Cortex-M7_0 TCM
S11
Cortex-M7_1 TCM
1. Base address: 4040_0000h. This instance follows the memory map given in section 'XBIC memory map'.
Table 71. XBIC configuration for S32K312 and S32K311
Instance
Available on crossbar
Initiator and target assignments
XBIC_0
AXBS_0 (main)
Initiator 
port
Initiator module
Target 
port
Target module
M0
Cortex-M7_0 AHBM
S0
Flash memory port 0
M1
eDMA
S1
Flash memory port 1
M2
HSE_B
S2
PRAM_0
M3
Cortex-M7_0 AHBP
S3
Cortex-M7 TCM
M4
Reserved
S4
AIPS_0
S5
AIPS_1
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
655 / 5251


---
# 페이지 605

The errors detected are connected to FCCU. See the memory map file attached to this document for details.
 
• Reset value of MCR register for S32K311, S32K342/S32K322/S32K341 and S32K344/S32K324/S32K314 
is "FFFF_0000h".
• For S32K388/S32K389/S32K358/S32K348/S32K338/S32K328 specific reset value, see MCR 
register description.
  NOTE  
18.1.2 Target master IDs
See "Chip-specific XRDC information" for master IDs.
18.1.3 XBIC_ESR[VLD] behavior across S32K3xx chips
In S32K388, S32K389, S32K358, S32K348, S32K338 and S32K328, the XBIC_ESR[VLD] bit is W1C and writing 1'b1 clears this 
bit as mentioned in the XBIC_ESR[VLD] description. In rest of the chips, this bit field is reserved and accessing this bit results in 
transfer error.
18.2 Overview
XBIC is a safety module that verifies the integrity of crossbar transfers.
18.2.1 Block diagram
The chip routes crossbar transfer attribute information for all mapped initiator and target ports to XBIC, which calculates and 
checks the EDC value of the attribute information, as shown in the following diagram.
m1
XBIC
...
m7
m0
s1
...
s7
s0
m1
Crossbar
...
m7
m0
Initiator 0
Initiator 1
Initiator 7
Target 0
Error out
to FCCU
Target 1
Target 7
s1
...
s7
s0
Initiator data phase output
Target data phase output
Initiator attribute input
Target attribute input
Attribute EDC output
Attribute EDC input
Figure 45. XBIC system block diagram
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
656 / 5251


---
# 페이지 606

The above figure illustrates one of many possible XBIC and crossbar configurations. See the Chip-specific XBIC information 
section for actual port mappings.
18.2.2 Features
XBIC includes the following features:
• Verification of attribute information for crossbar transfers [1],[2]
— EDC detects single-bit and double-bit errors
• Verification of feedback information for each data phase during crossbar transfers
• Error injection for testing
— Programmable initiator and target port specifiers
— Programmable 8-bit toggle vector to insert error in initiator EDC value
— Address, EDC syndrome, initiator, and target port information are captured when error is detected
• Crossbar transfer attribute integrity check programmable on a per-target-port basis
• Feedback integrity check programmable on a per-initiator-port basis
18.3 Functional description
XBIC verifies the integrity of the crossbar interface on an individual port basis according to the configuration specified via the MCR 
register. When XBIC detects an error, it reports relevant information and sends an error signal to the FCCU module, but does 
not generate a bus error. XBIC integrity checking is independent of end-to-end ECC, which monitors the integrity of the transfer 
address and data.
During the address phase of a transfer, XBIC verifies the crossbar attribute information using an 8-bit EDC, which detects any 
single-bit or double-bit errors. When XBIC detects an error (an attribute integrity error), due to either hardware fault or error 
injection, it reports information related to the error in ESR and EAR.
During the data phase of a data transfer, XBIC verifies the integrity of response signals from target to intiator as they pass through 
the crossbar. When XBIC detects an error in the response signals (a feedback integrity error), it reports the XBIC target and intiator 
ports in ESR[DPSE0] - ESR[DPSE7] and ESR[DPME0] - ESR[DPME7], respectively.
During the data phase, XBIC sends an alarm to the FCCU module if a intiator port attempts back-to-back accesses in which:
1. The first access terminates normally.
2. The second attempts access to an address space not mapped to any target on the crossbar.
The resultant 'absent target error' causes the crossbar to generate a bus error response to the requesting intiator. XBIC detects 
the bus error response as a difference because the bus error did not originate from the target port.
You can program XBIC to inject EDC errors for testing purposes. Error injection targets a single target port and a single intiator 
port, as specified by the configuration settings in the EIR register. When XBIC inserts an error, it changes the EDC syndrome, 
causing the XBIC to assert an error indication to the FCCU module. Otherwise, transfers are unaffected by error injection. This 
enables verification of the check logic without compromising the integrity of the data transfer. After you enable error injection 
function by writing 1 to EIR[EIE], XBIC induces errors on all subsequent targeted transactions until you write a 0 to the field. After 
the FCCU error indication asserts, it remains asserted even after you write 0 to EIR[EIE]. The error indication deasserts after 
FCCU specifically clears the existing error. After FCCU clears the XBIC error, additional error injection testing can continue.
To trace a fault reported by the XBIC to the FCCU:
1. Note the error reported by the FCCU. For example, "NCF[46]".
2. Locate the source module and error description in the attached fault mapping spreadsheet. For example:
[1] See Table 72 for a list of crossbar attribute signals verified.
[2] The chip verifies read and write data separately, via the end-to-end ECC architecture.
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
657 / 5251


---
# 페이지 607

• Channel number: NCF[46]
• Source module: AXBS_1 integrity checker
• Description: Instruction crossbar error indication to FCCU if syndrome calculated using EDC on the data is not zero
3. Refer to the Chip-specific XBIC information section for the source XBIC module to determine the specific XBIC module 
instanceâ€”"XBIC_1", for example.
4. Determine the type of error (attribute integrity error or feedback integrity error) and the XBIC port(s) involved by reading the 
information reported in the ESR register of the reported XBIC instance.
5. For attribute integrity check errors, read the XBIC EAR register for the target address of the requested transfer.
6. Refer to the Chip-specific XBIC information section and possibly the Chip-specific AXBS information section for port 
mapping of XBIC ports to AXBS ports.
Decode a single-bit error syndrome value reported in ESR[SYN] by finding the value in the following table. Any syndrome value 
not included in the table indicates a multi-bit error.
Table 72. Hexadecimal attribute single-bit error syndromes
Signal
SYN
Signal
SYN
Signal
SYN
Signal
SYN
hwrite
07
hbstrb[7]
70
hdecor[31]
25
hdecor[15]
23
htrans[0]
0b
hbstrb[6]
32
hdecor[30]
68
hdecor[14]
51
hsize[2]
0d
hbstrb[5]
52
hdecor[29]
c7
hdecor[13]
54
hsize[1]
0e
hbstrb[4]
a8
hdecor[28]
83
hdecor[12]
61
hsize[0]
13
hbstrb[3]
43
hdecor[27]
85
hdecor[11]
e3
hprot[5]
15
hbstrb[2]
45
hdecor[26]
86
hdecor[10]
e6
hprot[4]
16
hbstrb[1]
4c
hdecor[25]
89
hdecor[9]
f8
hprot[3]
19
hbstrb[0]
a4
hdecor[24]
8a
hdecor[8]
38
hprot[2]
1a
hmaster[3]
a2
hdecor[23]
8c
hdecor[7]
58
hprot[1]
1c
hmaster[2]
b0
hdecor[22]
49
hdecor[6]
37
hprot[0]
91
hmaster[1]
c1
hdecor[21]
92
hdecor[5]
f1
hburst[2]
a1
hmaster[0]
c2
hdecor[20]
94
hdecor[4]
3b
hburst[1]
64
hslave[2]
c4
hdecor[19]
98
hdecor[3]
3d
hburst[0]
29
hslave[1]
c8
hdecor[18]
46
hdecor[2]
3e
hmastlock
2a
hslave[0]
d0
hdecor[17]
34
hdecor[1]
4f
hunalign
2c
hdecorated
e0
hdecor[16]
4a
hdecor[0]
6e
edc[7]
80
edc[6]
40
edc[5]
20
edc[4]
10
edc[3]
08
edc[2]
04
edc[1]
02
edc[0]
01
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
658 / 5251


---
# 페이지 608

18.3.1 Interrupts
This module has no interrupts.
18.4 External signals
XBIC has no external interface signals.
18.5 Initialization
This module does not require initialization.
18.6 XBIC register descriptions
The XBIC programming model consists of four 32-bit registers. Software can access this model only in supervisor mode using 
32-bit (word) accesses. Each of the following generates a transfer error back to the requesting intiator. Such errors could cause 
core exceptions apart from other problems.
• Access size other than 32-bit
• Access to an undefined (reserved) address
• Access in user mode
18.6.1 XBIC memory map
XBIC_AXBS base address: 4020_4000h
XBIC_AXBS_ACE base address: 4040_C000h
XBIC_AXBS_ACE_HSE base address: 4000_8000h
XBIC_AXBS_PERI base address: 4020_8000h
XBIC_AXBS_PRAM_TCM base address: 4040_8000h
XBIC_AXBS_TCM base address: 4040_0000h
XBIC_AXBS_eDMA base address: 4040_4000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
XBIC Module Control (MCR)
32
RW
See section
4h
XBIC Error Injection Attributes (EIR)
32
RW
0000_0000h
8h
XBIC Error Status Attributes (ESR)
32
RW
0000_0000h
Ch
XBIC Error Address (EAR)
32
R
0000_0000h
18.6.2 XBIC Module Control (MCR)
Offset
Register
Offset
MCR
0h
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
659 / 5251


---
# 페이지 609

Function
Use this register to turn attribute integrity checking and feedback integrity checking on or off on a per-port basis.
• Turn on attribute integrity checking on one or more XBIC target ports by ensuring that the associated SEn field(s) have 
a value of 1. For example, setting field SE0 enables attribute integrity checking for target port 0. The default (reset) 
behavior is for attribute integrity checking to be performed for all target ports. XBIC performs EDC-based checks on all 
transfer requests targeting the selected target port(s). The signals verified are transfer attribute signals going from initiator 
to target. When XBIC detects an attribute integrity error, it reports relevant information in the ESR and EAR registers.
• Turn on feedback integrity checking on one or more XBIC initiator ports by ensuring that the associated MEn field(s) have 
a value of 1. For example, setting field ME0 to 1 enables feedback integrity checking for initiator port 0. The default (reset) 
behavior is for feedback integrity checking to be performed for all initiator ports. XBIC checks target-to-initiator feedback 
signals for transfer requests originating from the selected XBIC initiator port(s). If any feedback signal value is different at 
the initiator and target ports during the data phase, XBIC reports the relevant initiator and target ports in the ESR register.
Each field in this register references a specific initiator or target port using XBIC port numbering. Referring to Figure 45, "target 
port 0" refers to XBIC port "s0" in the figure, "target port 1" refers to port "s1", and so on. Similarly, "initiator port 0" refers to XBIC 
port "m0", "initiator port 1" refers to port "m1", and so on. See the "Chip-specific XBIC information" section in this document for the 
mapping of XBIC instances to AXBS instances and XBIC ports to AXBS ports. See the "Chip-specific AXBS information" section 
in this document for the device component(s) mapped to each port of an AXBS instance.
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
SE0 
SE1 
SE2 
SE3 
SE4 
SE5 
SE6 
SE7 
ME0 
ME1 
ME2 
ME3 
ME4 
ME5 
ME6 
ME7 
W
Reset
See Register reset values.
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
See Register reset values.
Register reset values
Register
Reset value
MCR
XBIC_AXBS: FFFF_0000h
XBIC_AXBS_ACE: 80C0_0000h
XBIC_AXBS_ACE_HSE: C0C0_0000h
XBIC_AXBS_PERI: F0FC_0000h
XBIC_AXBS_PRAM_TCM: E080_0000h
XBIC_AXBS_TCM: F080_0000h
XBIC_AXBS_eDMA: C0C0_0000h
Fields
Field
Function
31
target port EDC Error Detection Enable
Table continues on the next page...
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
660 / 5251


---
# 페이지 610

Table continued from the previous page...
Field
Function
SE0
0b - Attribute integrity checking disabled for target port 0
1b - Attribute integrity checking enabled for target port 0
30
SE1
target port EDC Error Detection Enable
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
XBIC_AXBS
MCR
—
XBIC_AXBS_ACE
—
MCR
XBIC_AXBS_ACE_HSE
MCR
—
XBIC_AXBS_PERI
MCR
—
XBIC_AXBS_PRAM_TCM
MCR
—
XBIC_AXBS_TCM
MCR
—
XBIC_AXBS_eDMA
MCR
—
0b - Attribute integrity checking disabled for target port 1
1b - Attribute integrity checking enabled for target port 1
29
SE2
target port EDC Error Detection Enable
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
XBIC_AXBS
MCR
—
XBIC_AXBS_ACE
—
MCR
XBIC_AXBS_ACE_HSE
—
MCR
XBIC_AXBS_PERI
MCR
—
XBIC_AXBS_PRAM_TCM
MCR
—
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
661 / 5251


---
# 페이지 611

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
XBIC_AXBS_TCM
MCR
—
XBIC_AXBS_eDMA
—
MCR
0b - Attribute integrity checking disabled for target port 2
1b - Attribute integrity checking enabled for target port 2
28
SE3
target port EDC Error Detection Enable
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
XBIC_AXBS
MCR
—
XBIC_AXBS_ACE
—
MCR
XBIC_AXBS_ACE_HSE
—
MCR
XBIC_AXBS_PERI
MCR
—
XBIC_AXBS_PRAM_TCM
—
MCR
XBIC_AXBS_TCM
MCR
—
XBIC_AXBS_eDMA
—
MCR
0b - Attribute integrity checking disabled for target port 3
1b - Attribute integrity checking enabled for target port 3
27
SE4
target port EDC Error Detection Enable
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
XBIC_AXBS
MCR
—
Table continues on the next page...
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
662 / 5251


---
# 페이지 612

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
XBIC_AXBS_ACE
—
MCR
XBIC_AXBS_ACE_HSE
—
MCR
XBIC_AXBS_PERI
—
MCR
XBIC_AXBS_PRAM_TCM
—
MCR
XBIC_AXBS_TCM
—
MCR
XBIC_AXBS_eDMA
—
MCR
0b - Attribute integrity checking disabled for target port 4
1b - Attribute integrity checking enabled for target port 4
26
SE5
target port EDC Error Detection Enable
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
XBIC_AXBS
MCR
—
XBIC_AXBS_ACE
—
MCR
XBIC_AXBS_ACE_HSE
—
MCR
XBIC_AXBS_PERI
—
MCR
XBIC_AXBS_PRAM_TCM
—
MCR
XBIC_AXBS_TCM
—
MCR
XBIC_AXBS_eDMA
—
MCR
0b - Attribute integrity checking disabled for target port 5
1b - Attribute integrity checking enabled for target port 5
25
SE6
target port EDC Error Detection Enable
Table continues on the next page...
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
663 / 5251


---
# 페이지 613

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
XBIC_AXBS
MCR
—
XBIC_AXBS_ACE
—
MCR
XBIC_AXBS_ACE_HSE
—
MCR
XBIC_AXBS_PERI
—
MCR
XBIC_AXBS_PRAM_TCM
—
MCR
XBIC_AXBS_TCM
—
MCR
XBIC_AXBS_eDMA
—
MCR
0b - Attribute integrity checking disabled for target port 6
1b - Attribute integrity checking enabled for target port 6
24
SE7
target Port EDC Error Detection Enable
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
XBIC_AXBS
MCR
—
XBIC_AXBS_ACE
—
MCR
XBIC_AXBS_ACE_HSE
—
MCR
XBIC_AXBS_PERI
—
MCR
XBIC_AXBS_PRAM_TCM
—
MCR
XBIC_AXBS_TCM
—
MCR
XBIC_AXBS_eDMA
—
MCR
Table continues on the next page...
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
664 / 5251


---
# 페이지 614

Table continued from the previous page...
Field
Function
0b - Attribute integrity checking disabled for target port 7
1b - Attribute integrity checking enabled for target port 7
23
ME0
initiator Port Enable For Feedback Integrity Check
0b - Feedback integrity checking disabled for initiator port 0
1b - Feedback integrity checking enabled for initiator port 0
22
ME1
initiator Port Enable For Feedback Integrity Check
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
XBIC_AXBS
MCR
—
XBIC_AXBS_ACE
MCR
—
XBIC_AXBS_ACE_HSE
MCR
—
XBIC_AXBS_PERI
MCR
—
XBIC_AXBS_PRAM_TCM
—
MCR
XBIC_AXBS_TCM
—
MCR
XBIC_AXBS_eDMA
MCR
—
0b - Feedback integrity checking disabled for initiator port 1
1b - Feedback integrity checking enabled for initiator port 1
21
ME2
initiator Port Enable For Feedback Integrity Check
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
XBIC_AXBS
MCR
—
XBIC_AXBS_ACE
—
MCR
XBIC_AXBS_ACE_HSE
—
MCR
Table continues on the next page...
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
665 / 5251


---
# 페이지 615

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
XBIC_AXBS_PERI
MCR
—
XBIC_AXBS_PRAM_TCM
—
MCR
XBIC_AXBS_TCM
—
MCR
XBIC_AXBS_eDMA
—
MCR
0b - Feedback integrity checking disabled for initiator port 2
1b - Feedback integrity checking enabled for initiator port 2
20
ME3
initiator Port Enable For Feedback Integrity Check
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
XBIC_AXBS
MCR
—
XBIC_AXBS_ACE
—
MCR
XBIC_AXBS_ACE_HSE
—
MCR
XBIC_AXBS_PERI
MCR
—
XBIC_AXBS_PRAM_TCM
—
MCR
XBIC_AXBS_TCM
—
MCR
XBIC_AXBS_eDMA
—
MCR
0b - Feedback integrity checking disabled for initiator port 3
1b - Feedback integrity checking enabled for initiator port 3
19
ME4
initiator Port Enable For Feedback Integrity Check
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
666 / 5251


---
# 페이지 616

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
XBIC_AXBS
MCR
—
XBIC_AXBS_ACE
—
MCR
XBIC_AXBS_ACE_HSE
—
MCR
XBIC_AXBS_PERI
MCR
—
XBIC_AXBS_PRAM_TCM
—
MCR
XBIC_AXBS_TCM
—
MCR
XBIC_AXBS_eDMA
—
MCR
0b - Feedback integrity checking disabled for initiator port 4
1b - Feedback integrity checking enabled for initiator port 4
18
ME5
initiator Port Enable For Feedback Integrity Check
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
XBIC_AXBS
MCR
—
XBIC_AXBS_ACE
—
MCR
XBIC_AXBS_ACE_HSE
—
MCR
XBIC_AXBS_PERI
MCR
—
XBIC_AXBS_PRAM_TCM
—
MCR
XBIC_AXBS_TCM
—
MCR
XBIC_AXBS_eDMA
—
MCR
0b - Feedback integrity checking disabled for initiator port 5
1b - Feedback integrity checking enabled for initiator port 5
17
initiator Port Enable For Feedback Integrity Check
Table continues on the next page...
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
667 / 5251


---
# 페이지 617

Table continued from the previous page...
Field
Function
ME6
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
XBIC_AXBS
MCR
—
XBIC_AXBS_ACE
—
MCR
XBIC_AXBS_ACE_HSE
—
MCR
XBIC_AXBS_PERI
—
MCR
XBIC_AXBS_PRAM_TCM
—
MCR
XBIC_AXBS_TCM
—
MCR
XBIC_AXBS_eDMA
—
MCR
0b - Feedback integrity checking disabled for initiator port 6
1b - Feedback integrity checking enabled for initiator port 6
16
ME7
initiator Port Enable For Feedback Integrity Check
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
XBIC_AXBS
MCR
—
XBIC_AXBS_ACE
—
MCR
XBIC_AXBS_ACE_HSE
—
MCR
XBIC_AXBS_PERI
—
MCR
XBIC_AXBS_PRAM_TCM
—
MCR
XBIC_AXBS_TCM
—
MCR
XBIC_AXBS_eDMA
—
MCR
Table continues on the next page...
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
668 / 5251


---
# 페이지 618

Table continued from the previous page...
Field
Function
0b - Feedback integrity checking disabled for initiator port 7
1b - Feedback integrity checking enabled for initiator port 7
15-0
—
Reserved
18.6.3 XBIC Error Injection Attributes (EIR)
Offset
Register
Offset
EIR
4h
Function
Use this register to configure the XBIC error injection function and turn it on or off. When enabled, the XBIC error injection 
function inserts an attribute integrity error when the targeted initiator requests a transaction of the targeted target port. The 
inserted error changes the calculated EDC syndrome value, causing XBIC to:
• Capture transfer information in the ESR and EAR registers
• Assert an error signal to the FCCU module
Otherwise, XBIC error injection does not affect transfers.
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
EIE 
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
SLV 
MST 
SYN 
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
EIE
Error Injection Enable
0b - Error injection disabled
Table continues on the next page...
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
669 / 5251


---
# 페이지 619

Table continued from the previous page...
Field
Function
1b - Error injection enabled
30-15
—
Reserved
14-12
SLV
Target Port
Specifies the target port for error injection—other target ports are unaffected.
Specify the target port by its XBIC target port number (0–7). See the "Chip-specific XBIC information" 
section in this document for the mapping of XBIC instances to AXBS instances and XBIC ports to AXBS 
ports. See the "Chip-specific AXBS information" section in this document for the device component(s) 
mapped to each port of an AXBS instance.
11-8
MST
Target initiator ID
Specifies the target initiator port for error injection—transfers with other intiators are unaffected.
Specify the target initiator port using the logical initiator ID number of the target bus initiator. See the "Chip-
specific XBIC information" section in this document for the initiator IDs and their corresponding components.
7-0
SYN
Syndrome
XBIC performs an exclusive OR operation on the value in this field and the calculated syndrome, to generate 
an error with the specified syndrome. A value of zero does not generate an error. See Table 72 for a list of 
transfer attribute single-bit error syndromes, noting that the values given in the table are hexadecimal.
18.6.4 XBIC Error Status Attributes (ESR)
Offset
Register
Offset
ESR
8h
Function
In this register, XBIC reports information about the most recent transfer with an error detected. If XBIC detects an attribute integrity 
check error, it reports:
• The target port identifier (SLV)
• The initiator port identifier (MST) and the error syndrome (SYN)
If XBIC detects a mismatch among feedback signals during the data phase:
• The DPSE0 - DPSE7 field with a value of 1 indicates the XBIC target port. In the DPSE0-DPSE7 field descriptions, the target 
port number refers to the XBIC target port number. Referring to Figure 45, "target port 0" refers to XBIC port "s0" in the figure, 
"target port 1" refers to port "s1", and so on. See the "Chip-specific XBIC information" section in this document for the mapping 
of XBIC instances to AXBS instances and XBIC ports to AXBS ports. See the "Chip-specific AXBS information" section in this 
document for the device component(s) mapped to each port of an AXBS instance.
• The DPME0 - DPME7 field with a value of 1 indicates the XBIC initiator port. In the DPME0-DPME7 field descriptions, the 
initiator port number refers to the XBIC initiator port number. Referring to Figure 45, "initiator port 0" refers to XBIC port "m0" in 
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
670 / 5251


---
# 페이지 620

the figure, "initiator port 1" refers to port "m1", and so on. See the "Chip-specific XBIC information" section in this document for 
the mapping of XBIC instances to AXBS instances and XBIC ports to AXBS ports. See the "Chip-specific AXBS information" 
section in this document for the device component(s) mapped to each port of an AXBS instance.
XBIC sets this register to all 0s only on reset.
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
VLD 
DPSE
0 
DPSE
1 
DPSE
2 
DPSE
3 
DPSE
4 
DPSE
5 
DPSE
6 
DPSE
7 
DPME
0 
DPME
1 
DPME
2 
DPME
3 
DPME
4 
DPME
5 
DPME
6 
W
W1C
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
DPME
7 
SLV 
MST 
SYN 
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
VLD
Error Status Valid
0b - No error detected—other fields of the ESR and EAR registers are invalid
1b - Error detected—all fields of the ESR and EAR registers are valid
30
DPSE0
Data Phase target Port Error
0b - No feedback integrity error detected on target port 0
1b - Feedback integrity error detected on target port 0
29
DPSE1
Data Phase target Port Error
0b - No feedback integrity error detected on target port 1
1b - Feedback integrity error detected on target port 1
28
DPSE2
Data Phase target Port Error
0b - No feedback integrity error detected on target port 2
1b - Feedback integrity error detected on target port 2
27
DPSE3
Data Phase target Port Error
0b - No feedback integrity error detected on target port 3
1b - Feedback integrity error detected on target port 3
26
DPSE4
Data Phase target Port Error
0b - No feedback integrity error detected on target port 4
Table continues on the next page...
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
671 / 5251


---
# 페이지 621

Table continued from the previous page...
Field
Function
1b - Feedback integrity error detected on target port 4
25
DPSE5
Data Phase target Port Error
0b - No feedback integrity error detected on target port 5
1b - Feedback integrity error detected on target port 5
24
DPSE6
Data Phase target Port Error
0b - No feedback integrity error detected on target port 6
1b - Feedback integrity error detected on target port 6
23
DPSE7
Data Phase target Port Error
0b - No feedback integrity error detected on target port 7
1b - Feedback integrity error detected on target port 7
22
DPME0
Data Phase initiator Port Error
0b - No feedback integrity error detected on initiator port 0
1b - Feedback integrity error detected on initiator port 0
21
DPME1
Data Phase initiator Port Error
0b - No feedback integrity error detected on initiator port 1
1b - Feedback integrity error detected on initiator port 1
20
DPME2
Data Phase initiator Port Error
0b - No feedback integrity error detected on initiator port 2
1b - Feedback integrity error detected on initiator port 2
19
DPME3
Data Phase initiator Port Error
0b - No feedback integrity error detected on initiator port 3
1b - Feedback integrity error detected on initiator port 3
18
DPME4
Data Phase initiator Port Error
0b - No feedback integrity error detected on initiator port 4
1b - Feedback integrity error detected on initiator port 4
17
DPME5
Data Phase initiator Port Error
0b - No feedback integrity error detected on initiator port 5
1b - Feedback integrity error detected on initiator port 5
16
DPME6
Data Phase initiator Port Error
0b - No feedback integrity error detected on initiator port 6
1b - Feedback integrity error detected on initiator port 6
Table continues on the next page...
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
672 / 5251


---
# 페이지 622

Table continued from the previous page...
Field
Function
15
DPME7
Data Phase initiator Port Error
0b - No feedback integrity error detected on initiator port 7
1b - Feedback integrity error detected on initiator port 7
14-12
SLV
target Port
target port targeted by the most recent transfer with an attribute integrity check error detected.
The value in this field is the XBIC target port number (0–7). See the "Chip-specific XBIC information" section 
in this document for the mapping of XBIC instances to AXBS instances and XBIC ports to AXBS ports. See 
the "Chip-specific AXBS information" section in this document for the device component(s) mapped to each 
port of an AXBS instance.
11-8
MST
initiator ID
initiator port that requested the most recent transfer with an attribute integrity check error detected.
The value in this field is the logical initiator ID number of the bus initiator. See the "Chip-specific XBIC 
information" section in this document for the initiator IDs and their corresponding components.
7-0
SYN
Syndrome
Syndrome calculated for the most recent transfer with an attribute integrity check error detected.
For single-bit errors, identify the signal in error by matching the SYN value in Table 72, noting that the 
syndrome (SYN) values in the table are hexadecimal.
18.6.5 XBIC Error Address (EAR)
Offset
Register
Offset
EAR
Ch
Function
In this register, XBIC reports the address of the most recent transfer with an attribute integrity check error detected—either 
because of a hardware fault or error injection. XBIC sets this register to all 0s only on reset.
 
An attempted write to this read-only register results in a transfer error.
  NOTE  
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
673 / 5251


---
# 페이지 623

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
ADDR 
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
ADDR 
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
31-0
ADDR
Error Address
Address of the most recent transfer with an attribute integrity check error detected.
18.7 Glossary
EDC
Error Detection Code
hdecor[31:0]
Non-standard AHB address phase signal for transporting optional decorated storage instruction information
hdecorated
Non-standard AHB address phase signal for transporting optional decorated storage instruction information
NXP Semiconductors
Crossbar Integrity Checker (XBIC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
674 / 5251


---