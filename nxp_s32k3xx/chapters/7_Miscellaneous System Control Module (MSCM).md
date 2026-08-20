# 페이지 26

Chapter 7
Miscellaneous System Control Module (MSCM)
7.1 Chip-specific MSCM information
7.1.1 MSCM instance
This chip has one instance of MSCM.
 
The XN_CTRL register is used to restrict execution from SRAM, including TCMs and their backdoors, 
which will be permanent until next device reset, while still allowing data R/W.
XN_CTRL register is reserved for S32K344/S32K324/S32K314.
  NOTE  
7.1.2 Reporting of core-to-core interrupts
For all the variants the core-to-core interrupts are reported to both INTM and MSCM for CM7_0 and CM7_1. But, for CM7_2 the 
core-to-core interrupts are reported to MSCM, instead of INTM. See the interrupt map file attached to this document for details.
7.1.3 ENEDC register implementation
In S32K310, S32K311, S32K312, S32K314, S32K322, S32K324, S32K341, S32K342, and S32K344 there are additional bit field 
as compared to what is mentioned in section 'MSCM memory map'. See following table for details.
Table 33. Bitfield details
Bitfield name
Bitfield position
ENEDC[EN_WR_TCM]1
16
ENEDC[EN_ADD_TCM] 1
17
1. See section EN_WR_TCM and EN_ADD_TCM definition for details
7.1.3.1
EN_WR_TCM and EN_ADD_TCM definition
Register ENEDC has the following additional bitfields:
Table 34. Bitfield definition
Bitfield position
Bitfield name
Bitfield description
16
EN_WR_TCM (Enable 
Write Data Check TCM)
Enables or disables the write data check for TCM 64-bit path.
• 0b-Disabled
• 1b-Enabled
17
EN_ADD_TCM (Enable 
Address Check TCM)
Enables or disables the address check for TCM 64-bit path.
• 0b-Disabled
• 1b-Enabled
7.1.4 ENEDC and ENEDC1 register implementation for S32K358, S32K348, S32K338, and S32K328
In S32K358, S32K348, S32K338, and S32K328 there are some differences in register[bit field] as compared to what is mentioned 
in section 'MSCM memory map'. See following table for details.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
77 / 5251


---
# 페이지 27

Table 35. Bitfield details
Register[Bitfield name]
Bitfield position
ENEDC[ADD_TCM_BACKDOOR]
17
ENEDC1[CM7_3_WDATA_CHK]1
12
ENEDC1[CM7_3_ADDR_CHK]1
13
ENEDC1[USDHC]
16
ENEDC1[CM7_3_AHBM]1
17
ENEDC1[CM7_3_AHBP]1
18
ENEDC1[MSTR_CHK_ACE_RESULT_CHK]1
19
ENEDC1[MSTR_CHK_ACE_FEED_CHK]1
20
ENEDC1[SLV_CHK_ACE_ADDR_CHK]1
21
ENEDC1[SLV_CHK_ACE_ACCEL_RESULT_M1_GSKT_WDATA_CHK]1
22
ENEDC1[SLV_CHK_ACE_ACCEL_RESULT_M1_GSKT_ADDR_CHK]1
23
ENEDC1[TCM_GSKT_ADDR_CHK]1
24
1. This field is Reserved for S32K358, S32K348, S32K338, and S32K328.
7.1.4.1
ENEDC[ADD_TCM_BACKDOOR] and ENEDC1 [USDHC] definition
In S32K358, S32K348, S32K338, and S32K328 ENEDC register has the following additional bitfields:
Table 36. Bitfield definition
Bitfield position
Bitfield name
Bitfield description
17
ADD_TCM_BACKDOOR (Write Data 
Check For TCM Backdoor)
Enables or disables the address check 
for the TCM backdoor path.
• 0b-Disabled
• 1b-Enabled
In S32K358, S32K348, S32K338, and S32K328 ENEDC1 register has the following additional bitfields:
Table 37. Bitfield definition
Bitfield position
Bitfield name
Bitfield description
16
USDHC (Enable Read Data 
Check uSDHC)
Enables or disables the read data check 
for the uSDHC path.
• 0b-Disabled
• 1b-Enabled
7.2 Overview
MSCM contains registers for:
• CPU configuration
• On-chip memory control
• Interrupt router control
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
78 / 5251


---
# 페이지 28

• Message-based interrupt configuration
• Virtual management
7.2.1 Features
• Software-accessible processor core configuration information
• Support for interrupt router control
• Support for message-based interrupt configuration
7.3 Functional description
MSCM provides information of the system cores and can identify the core that is running currently.
7.3.1 MSI routing
MSIs are interrupts that are indirectly broadcast to a target core by writing configuration bits in MSCM. These MSIs can be 
initiated by one core targeting another core in the system (known as core-to-core interrupts). These MSIs are initiated via writes 
to Interrupt Router CPn Interrupt Generation (IRCP0IGR0 - IRCP3IGR3) and managed through Interrupt Router CPn Interrupt 
Status (IRCP0ISR0 - IRCP3ISR3). The Cortex-M7 cores can support up to four outstanding core-to-core interrupts.
int_en
CPn Core-to-Core Int0
cp0_int
cp1_int
IRCP nlGR0
IRCP nlSR0
int_en
CPn Core-to-Core Int1
cp0_int
cp1_int
IRCP nlGR1
IRCP nlSR1
int_en
CPn Core-to-Core Int2
cp0_int
cp1_int
IRCP nlGR2
IRCP nlSR2
CPn Core-to-Core Int3  
 
 
cp0_int
cp1_int
IRCP nlGR3
IRCP nlSR3
int0_en
Figure 16. IRCPnIGRm/IRCPnISRm pairs for one core
int_en
CPn Core-to-Core Int0
cp0_int
cp1_int
IRCP nlGR0
IRCP nlSR0
int_en
CPn Core-to-Core Int1
cp0_int
cp1_int
IRCP nlGR1
IRCP nlSR1
int_en
CPn Core-to-Core Int2
cp0_int
cp1_int
IRCP nlGR2
IRCP nlSR2
CP0
CP1
CPn Core-to-Core Int3
 
 
cp0_int
cp1_int
IRCP nlGR3
IRCP nlSR3
int0_en
Figure 17. IRCPnIGRm/IRCPnISRm pairs per core
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
79 / 5251


---
# 페이지 29

7.3.1.1
Core-to-core MSIs
The next figure depicts the sequence for initiating a core-to-core MSI, in which m represents the initiating core, n represents the 
target core, and x indicates the MSI number. CPm writes to IRCPnIGRx to initiate an MSI. The outstanding MSI that CPm initiates, 
targeting CPn, is reflected in the corresponding bit-mapped field in IRCPnISRx.
IRCPnIGRx
IRCPnISRx
CPm masterID
CPm writes to
IRCPnlGRx to generate
core-to-core
interrupt to CPn
1
int_en
cp0_int
cp1_int
wr
Figure 18. Initiating a core-to-core MSI via IRCPnIGRx/IRCPnISRx
7.3.2 Interrupt steering and semaphores
7.3.2.1
Interrupt handling overview
The interrupt handling mechanisms of the Cortex-M7 cores are very similar. These cores have an NVIC tightly coupled to the 
processor core. The real-time performance of the cores means the NVIC directly provides an appropriate interrupt vector, in the 
form of the starting instruction address for the interrupt service routine, to the core. These core architectural features directly 
translate into a faster ISR entry and exit capabilities, coupled with an improved runtime performance. See the Arm modules and 
Arm core technical reference manuals for details.
In this architecture, a total of 240 IRQs are supported, where this parameter is defined by the realistic limits of the NVIC 
implementation, both in terms of silicon size and supported frequency of operation. These 240 IRQs are split into a total of four 
directed requests and 236 shared peripheral requests. Unless noted otherwise, let the directed requests be defined as IRQ[3:0] 
and the shared peripheral requests as IRQ[239:4]. See the interrupt map file attached to this document for details.
7.3.2.2
MSCM interrupt router functional description
As described in MSCM register descriptions, the interrupt routing registers enable the steering of requests to the processor cores.
7.3.3 Clocking
This module has no clocking considerations.
7.4 External signals
This module has no external signals.
7.5 Initialization
This module does not require initialization.
7.6 Memory map and register definition
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
80 / 5251


---
# 페이지 30

7.6.1 Core configuration registers
These read-only registers contain data that defines the core setup for this chip. You can access the registers using 32-bit read 
references; other access sizes terminate with an error. Attempted write accesses to the read-only core configuration registers also 
terminate with an error.
The core configuration portion of the MSCM programming model map is organized based on the logical core number, and not on 
any type of physical port number. The following table shows how the configuration is partitioned.
Table 38. MSCM core configuration partitioning
Offset address 
range
Purpose
0h–018h
Defines the generic core x configuration information. Only the MSCM associated controllers can access 
this region in either User or Privileged mode; reads by noncore bus controllers (including the debugger) 
are treated as read as zero (RAZ) accesses. Write attempts are not permitted and terminate with a system 
bus error.
020h–038h
Defines the configuration information for core 0 (CP0). Any bus controller can access this region in either User 
or Privileged mode. Write attempts are not permitted and terminate with a system bus error.
 
Attempted accesses to reserved locations are not permitted and terminate with a system bus error.
  NOTE  
7.6.2 Shared peripheral interrupt (SPI) routing
The SPI router portion of MSCM provides a set of memory-mapped registers defining the interrupt routing for all the SPIs on 
this chip.
7.6.3 MSCM register descriptions
7.6.3.1
MSCM memory map
MSCM base address: 4026_0000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Processor X Type (CPXTYPE)
32
R
See section
4h
Processor X Number (CPXNUM)
32
R
See section
8h
Processor X Revision (CPXREV)
32
R
See section
Ch
Processor X Configuration 0 (CPXCFG0)
32
R
0602_0604h
10h
Processor X Configuration 1 (CPXCFG1)
32
R
See section
14h
Processor X Configuration 2 (CPXCFG2)
32
R
See section
18h
Processor X Configuration 3 (CPXCFG3)
32
R
0000_000Bh
20h
Processor 0 Type (CP0TYPE)
32
R
434D_3730h
24h
Processor 0 Number (CP0NUM)
32
R
See section
28h
Processor 0 Count (CP0REV)
32
R
See section
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
81 / 5251


---
# 페이지 31

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
2Ch
Processor 0 Configuration 0 (CP0CFG0)
32
R
0502_0504h
30h
Processor 0 Configuration 1 (CP0CFG1)
32
R
0000_0000h
34h
Processor 0 Configuration 2 (CP0CFG2)
32
R
See section
38h
Processor 0 Configuration 3 (CP0CFG3)
32
R
0000_000Bh
40h
Processor 1 Type (CP1TYPE)
32
R
434D_3731h
44h
Processor 1 Number (CP1NUM)
32
R
0000_0001h
48h
Processor 1 Count (CP1REV)
32
R
See section
4Ch
Processor 1 Configuration 0 (CP1CFG0)
32
R
0502_0504h
50h
Processor 1 Configuration 1 (CP1CFG1)
32
R
See section
54h
Processor 1 Configuration 2 (CP1CFG2)
32
R
See section
58h
Processor 1 Configuration 3 (CP1CFG3)
32
R
0000_000Bh
60h
Processor 2 Type (CP2TYPE)
32
R
434D_3732h
64h
Processor 2 Number (CP2NUM)
32
R
0000_0002h
68h
Processor 2 Count (CP2REV)
32
R
See section
6Ch
Processor 2 Configuration 0 (CP2CFG0)
32
R
0602_0604h
70h
Processor 2 Configuration 1 (CP2CFG1)
32
R
See section
74h
Processor 2 Configuration 2 (CP2CFG2)
32
R
See section
78h
Processor 2 Configuration 3 (CP2CFG3)
32
R
0000_000Bh
80h
Processor 3 Type (CP3TYPE)
32
R
434D_3733h
84h
Processor 3 Number (CP3NUM)
32
R
0000_0003h
88h
Processor 3 Count (CP3REV)
32
R
See section
8Ch
Processor 3 Configuration 0 (CP3CFG0)
32
R
0602_0604h
90h
Processor 3 Configuration 1 (CP3CFG1)
32
R
See section
94h
Processor 3 Configuration 2 (CP3CFG2)
32
R
See section
98h
Processor 3 Configuration 3 (CP3CFG3)
32
R
0000_000Bh
200h
Interrupt Router CP0 Interrupt Status (IRCP0ISR0)
32
RW
0000_0000h
204h
Interrupt Router CP0 Interrupt Generation (IRCP0IGR0)
32
RW
0000_0000h
208h
Interrupt Router CP0 Interrupt Status (IRCP0ISR1)
32
RW
0000_0000h
20Ch
Interrupt Router CP0 Interrupt Generation (IRCP0IGR1)
32
RW
0000_0000h
210h
Interrupt Router CP0 Interrupt Status (IRCP0ISR2)
32
RW
0000_0000h
214h
Interrupt Router CP0 Interrupt Generation (IRCP0IGR2)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
82 / 5251


---
# 페이지 32

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
218h
Interrupt Router CP0 Interrupt Status (IRCP0ISR3)
32
RW
0000_0000h
21Ch
Interrupt Router CP0 Interrupt Generation (IRCP0IGR3)
32
RW
0000_0000h
220h
Interrupt Router CP1 Interrupt Status (IRCP1ISR0)
32
RW
0000_0000h
224h
Interrupt Router CP1 Interrupt Generation (IRCP1IGR0)
32
RW
0000_0000h
228h
Interrupt Router CP1 Interrupt Status (IRCP1ISR1)
32
RW
0000_0000h
22Ch
Interrupt Router CP1 Interrupt Generation (IRCP1IGR1)
32
RW
0000_0000h
230h
Interrupt Router CP1 Interrupt Status (IRCP1ISR2)
32
RW
0000_0000h
234h
Interrupt Router CP1 Interrupt Generation (IRCP1IGR2)
32
RW
0000_0000h
238h
Interrupt Router CP1 Interrupt Status (IRCP1ISR3)
32
RW
0000_0000h
23Ch
Interrupt Router CP1 Interrupt Generation (IRCP1IGR3)
32
RW
0000_0000h
240h
Interrupt Router CP2 Interrupt Status (IRCP2ISR0)
32
RW
0000_0000h
244h
Interrupt Router CP2 Interrupt Generation (IRCP2IGR0)
32
RW
0000_0000h
248h
Interrupt Router CP2 Interrupt Status (IRCP2ISR1)
32
RW
0000_0000h
24Ch
Interrupt Router CP2 Interrupt Generation (IRCP2IGR1)
32
RW
0000_0000h
250h
Interrupt Router CP2 Interrupt Status (IRCP2ISR2)
32
RW
0000_0000h
254h
Interrupt Router CP2 Interrupt Generation (IRCP2IGR2)
32
RW
0000_0000h
258h
Interrupt Router CP2 Interrupt Status (IRCP2ISR3)
32
RW
0000_0000h
25Ch
Interrupt Router CP2 Interrupt Generation (IRCP2IGR3)
32
RW
0000_0000h
260h
Interrupt Router CP3 Interrupt Status (IRCP3ISR0)
32
RW
0000_0000h
264h
Interrupt Router CP3 Interrupt Generation (IRCP3IGR0)
32
RW
0000_0000h
268h
Interrupt Router CP3 Interrupt Status (IRCP3ISR1)
32
RW
0000_0000h
26Ch
Interrupt Router CP3 Interrupt Generation (IRCP3IGR1)
32
RW
0000_0000h
270h
Interrupt Router CP3 Interrupt Status (IRCP3ISR2)
32
RW
0000_0000h
274h
Interrupt Router CP3 Interrupt Generation (IRCP3IGR2)
32
RW
0000_0000h
278h
Interrupt Router CP3 Interrupt Status (IRCP3ISR3)
32
RW
0000_0000h
27Ch
Interrupt Router CP3 Interrupt Generation (IRCP3IGR3)
32
RW
0000_0000h
400h
Interrupt Router Configuration (IRCPCFG)
32
RW
0000_0000h
500h
Memory Execution Controls (XN_CTRL)
32
RW
4000_0000h
600h
Enable Interconnect Error Detection (ENEDC)
32
RW
0000_0000h
604h
Enable Interconnect Error Detection (ENEDC1)
32
RW
0000_0000h
700h
AHB Gasket Configuration (IAHBCFGREG)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
83 / 5251


---
# 페이지 33

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
880h - A5Eh
Interrupt Router Shared Peripheral Routing Control (IRSPRC0 - 
IRSPRC239)
16
RW
000Fh
7.6.3.2
Processor X Type (CPXTYPE)
Offset
Register
Offset
CPXTYPE
0h
Function
Provides a CPU-specific response indicating the personality of the core making the access. The 32-bit response includes four 
ASCII characters defining the CPU type (Cortex-M7 cores) along with a byte defining the logical revision number and a byte 
defining the instance number of the core.
A read from Cortex-M7 returns the appropriate processor information. Reads from any other bus controller return all 0s and 
attempted write accesses terminate with an error.
Access: User or privileged read-only
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
PERSONALITY 
W
Reset
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
PERSONALITY 
W
Reset
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
u
u
u
u
Fields
Field
Function
31-0
PERSONALITY
Personality of CPx
Defines the processor personality for CPx.
Processor
Personality
CPx = Cortex-M7_0
43_4D_37_30h
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
84 / 5251


---
# 페이지 34

Field
Function
Processor
Personality
CPx = Cortex-M7_1
43_4D_37_31h
CPx = Cortex-M7_2
43_4D_37_32h
CPx = Cortex-M7_3
43_4D_37_33h
7.6.3.3
Processor X Number (CPXNUM)
Offset
Register
Offset
CPXNUM
4h
Function
Provides a CPU-specific response indicating the logical processor number of the core making the access.
A read from the Cortex-M7 cores returns the appropriate processor information. Reads from any other bus controller return all 0s 
and attempted write accesses terminate with an error.
Access: User or privileged read-only
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
CPN 
W
Reset
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
u
u
u
u
Fields
Field
Function
31-3
—
Reserved
2-0
Processor Number
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
85 / 5251


---
# 페이지 35

Table continued from the previous page...
Field
Function
CPN
Defines the logical processor number for CPx.
 
CPN in MSCM indicates only the on-platform cores and not the HSE_B core. CPN = 0 
represents Cortex-M7_0 if it is a lockstep or dual core. In Lockstep mode, CPN = 1 does not 
read from Processor X Number (CPXNUM).
  NOTE  
000b - Cortex-M7 core 0
001b - Cortex-M7 core 1
010b - Cortex-M7 core 2
011b - Cortex-M7 core 3
7.6.3.4
Processor X Revision (CPXREV)
Offset
Register
Offset
CPXREV
8h
Function
Provides a CPU-specific response indicating the logical revision number of the core.
A read from the Cortex-M7 cores returns the appropriate processor information. Reads from any other bus controller return all 0s 
and attempted write accesses terminate with an error.
Access: User or privileged read-only
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
RYPZ 
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
u
u
u
u
u
u
u
u
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
86 / 5251


---
# 페이지 36

Fields
Field
Function
31-8
—
Reserved
7-0
RYPZ
Processor Revision
Defines the processor revision for CPx.
For the Cortex-M7 cores in this chip, RYPZ = 12h corresponding to the r1p2 core release.
7.6.3.5
Processor X Configuration 0 (CPXCFG0)
Offset
Register
Offset
CPXCFG0
Ch
Function
Provides a CPU-specific response detailing configuration information. In this case, it is information on Level 1 (L1) cache, 
if present.
A read from Cortex-M7 returns the appropriate processor information. Reads from any other bus controller return all 0s and 
attempted write accesses terminate with an error.
Access: User or privileged read-only
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
ICSZ 
ICWY 
W
Reset
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
DCSZ 
DCWY 
W
Reset
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
1
0
0
Fields
Field
Function
31-24
ICSZ
Level 1 Instruction Cache Size
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
87 / 5251


---
# 페이지 37

Table continued from the previous page...
Field
Function
Provides an encoded value of the instruction cache size. The capacity of the memory is derived using the 
formula 2(8+SZ) and expressed as bytes. Here, ICSZ is a nonzero value and ICSZ = 0 indicates that the 
memory is not present.
For information about cache sizes, see the "Miscellaneous Control Module (MCM)" chapter.
23-16
ICWY
L1 Instruction Cache Ways
Provides the number of cache ways for the instruction cache.
For the Cortex-M7 cores in this chip, ICWY = 2h (2-way set-associative).
15-8
DCSZ
L1 Data Cache Size
Provides an encoded value of the data cache size.
The capacity of the memory is derived using the formula 2(8+SZ) and expressed as bytes. Here, DCSZ is a 
nonzero value and DCSZ = 0 indicates that the memory is not present.
For information about cache sizes, see the "Miscellaneous Control Module (MCM)" chapter.
7-0
DCWY
L1 Data Cache Ways
Provides the number of cache ways for the data cache.
For the Cortex-M7 cores in this chip, DCWY = 4h (4-way set-associative).
7.6.3.6
Processor X Configuration 1 (CPXCFG1)
Offset
Register
Offset
CPXCFG1
10h
Function
Provides a CPU-specific response detailing configuration information. In this case, it is information on Level 2 (L2) cache, 
if present.
A read from the Cortex-M7 cores returns the appropriate processor information. Reads from any other bus controller return all 0s 
and attempted write accesses terminate with an error.
Access: User or privileged read-only
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
88 / 5251


---
# 페이지 38

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
L2SZ 
L2WY 
W
Reset
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
31-24
L2SZ
L2 Cache Size
Provides an encoded value of the L2 cache size. The capacity of the memory is derived using the formula 
2(8+SZ) and expressed as bytes. Here, L2SZ is a nonzero value, and L2SZ = 0 indicates that the memory is 
not present.
For the Cortex-M7 cores in this chip, L2SZ = 0h (not present).
23-16
L2WY
L2 Cache Ways
Provides the number of cache ways for the L2 cache.
For the Cortex-M7 cores in this chip, L2WY = 0h (not present).
15-0
—
Reserved
7.6.3.7
Processor X Configuration 2 (CPXCFG2)
Offset
Register
Offset
CPXCFG2
14h
Function
Provides a CPU-specific response detailing configuration information. In this case, it is information on tightly coupled local 
memories, if present.
A read from the Cortex-M7 cores returns the appropriate processor information. Reads from any other bus controller return all 0s 
and attempted write accesses terminate with an error.
Access: User or privileged read-only
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
89 / 5251


---
# 페이지 39

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
DTCMSZ 
ITCMSZ 
W
Reset
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
31-24
DTCMSZ
Tightly Coupled Data Memory Size
Provides an encoded value of the tightly coupled local data memory size. The capacity of the memory is 
derived using the formula 2(8+SZ) and expressed as bytes. Here, DTCMSZ is a nonzero value and DTCMSZ 
= 0 indicates that the memory is not present.
For the Cortex-M7 cores in this chip:
• DTCMSZ = 08 in Decoupled mode (64 KB)
• DTCMSZ = 09 for Cortex-M7_0 in Lockstep mode (128 KB)
23-16
ITCMSZ
Instruction Tightly Coupled Memory Size
Provides an encoded value of the tightly coupled local instruction memory size. The capacity of the memory 
is derived using the formula 2(8+SZ) and expressed as bytes. Here, ITCMSZ is a nonzero value, and ITCMSZ 
= 0 indicates that the memory is not present.
For the Cortex-M7 cores in this chip:
• ITCMSZ = 07 in Decoupled mode (32 KB)
• ITCMSZ = 08 for Cortex-M7_0 in Lockstep mode (64 KB)
15-0
—
Reserved
7.6.3.8
Processor X Configuration 3 (CPXCFG3)
Offset
Register
Offset
CPXCFG3
18h
Function
Provides a CPU-specific response detailing configuration information. In this case, it is information on processor options.
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
90 / 5251


---
# 페이지 40

A privileged read from Cortex-M7 returns the appropriate processor information. Reads from any other bus controller return all 0s 
and attempted write accesses terminate with an error.
Access: User or privileged read-only
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
CPY 
CMP 
MMU 
SIMD 
FPU 
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
1
0
1
1
Fields
Field
Function
31-5
—
Reserved
4
CPY
Cryptography
Indicates whether the cryptography extensions are supported in the core.
For the Cortex-M7 cores in this chip, CPY = 0h.
0b - Not supported
1b - Supported
3
CMP
Core Memory Protection Unit
Indicates whether the core memory protection hardware is included in this core.
For the Cortex-M7 cores in this chip, CMP = 1h.
0b - Not included
1b - Included
2
MMU
Memory Management Unit
Indicates whether virtual management capabilities are supported in this core.
For the Cortex-M7 cores in this chip, MMU = 0h.
0b - Not supported
1b - Supported
1
SIMD
SIMD/NEON Instruction Support
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
91 / 5251


---
# 페이지 41

Table continued from the previous page...
Field
Function
Indicates whether the instruction set extensions supporting SIMD and/or NEON capabilities are included in 
the processor.
For the Cortex-M7 cores in this chip, SIMD = 1h.
0b - Not included
1b - Included
0
FPU
Floating Point Unit
Indicates whether hardware support for floating point capabilities is provided in the processor.
For the Cortex-M7 cores in this chip, FPU = 1h.
0b - Not provided
1b - Provided
7.6.3.9
Processor 0 Type (CP0TYPE)
Offset
Register
Offset
CP0TYPE
20h
Function
Defines the configuration information for processor 0 (CP0). It has the same field definitions and functionality as provided in 
Processor X Type (CPXTYPE).
A read from any bus controller returns the appropriate processor information and attempted write accesses terminate with an error.
Access: User or privileged read-only
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
PERSONALITY 
W
Reset
0
1
0
0
0
0
1
1
0
1
0
0
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
PERSONALITY 
W
Reset
0
0
1
1
0
1
1
1
0
0
1
1
0
0
0
0
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
92 / 5251


---
# 페이지 42

Fields
Field
Function
31-0
PERSONALITY
Processor Personality
Defines the processor personality for CP0.
For Cortex-M7 core 0, personality = 43_4D_37_30h.
7.6.3.10
Processor 0 Number (CP0NUM)
Offset
Register
Offset
CP0NUM
24h
Function
Defines the configuration information for processor 0 (CP0). It has the same field definitions and functionality as provided in 
Processor X Number (CPXNUM).
A privileged read from any bus controllers returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
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
CPN 
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
u
Fields
Field
Function
31-2
—
Reserved
1-0
CPN
Processor Number
Defines the logical processor number for CP0.
For processor Cortex-M7 core 0, processor number = 0.
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
93 / 5251


---
# 페이지 43

7.6.3.11
Processor 0 Count (CP0REV)
Offset
Register
Offset
CP0REV
28h
Function
Defines the configuration information for processor 0 (CP0). It has the same field definitions and functionality as provided in 
Processor X Revision (CPXREV).
A read from any bus controller returns the appropriate processor information and attempted write accesses terminate with an error.
Access: User or privileged read-only
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
RYPZ 
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
u
u
u
u
u
u
u
u
Fields
Field
Function
31-8
—
Reserved
7-0
RYPZ
Processor Revision
Defines the processor revision for CP0.
For the Cortex-M7 processor, RYPZ = 12h corresponding to the r1p2 core release.
7.6.3.12
Processor 0 Configuration 0 (CP0CFG0)
Offset
Register
Offset
CP0CFG0
2Ch
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
94 / 5251


---
# 페이지 44

Function
Defines the configuration information for processor 0 (CP0). It has the same field definitions and functionality as provided in 
Processor X Configuration 0 (CPXCFG0).
A read from any bus controller returns the appropriate processor information and attempted write accesses terminate with an error.
Access: User or privileged read-only
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
ICSZ 
ICWY 
W
Reset
0
0
0
0
0
1
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
DCSZ 
DCWY 
W
Reset
0
0
0
0
0
1
0
1
0
0
0
0
0
1
0
0
Fields
Field
Function
31-24
ICSZ
Level 1 Instruction Cache Size
Provides an encoded value of the instruction cache size. The capacity of the memory is derived using the 
formula 2(8+SZ) and expressed as bytes. Here, ICSZ is a nonzero value, and ICSZ = 0 indicates that the 
memory is not present.
For information about cache sizes, see the "Miscellaneous Control Module (MCM)" chapter.
23-16
ICWY
L1 Instruction Cache Ways
Provides the number of cache ways for the instruction cache.
For the Cortex-M7 cores in this chip, ICWY = 2h (2-way set-associative).
15-8
DCSZ
L1 Data Cache Size
Provides an encoded value of the data cache size.
The capacity of the memory is derived using the formula 2(8+SZ) and expressed as bytes. Here, DCSZ is a 
nonzero value, and DCSZ = 0 indicates that the memory is not present.
For information about cache sizes, see the "Miscellaneous Control Module (MCM)" chapter.
7-0
DCWY
L1 Data Cache Ways
Provides the number of cache ways for the data cache.
For the Cortex-M7 cores in this chip, DCWY = 4h (4-way set-associative).
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
95 / 5251


---
# 페이지 45

7.6.3.13
Processor 0 Configuration 1 (CP0CFG1)
Offset
Register
Offset
CP0CFG1
30h
Function
Defines the configuration information for processor 0 (CP0). It has the same field definitions and functionality as provided in 
Processor X Configuration 1 (CPXCFG1).
A privileged read from any bus controller returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
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
L2SZ 
L2WY 
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
31-24
L2SZ
L2 Cache Size
Provides an encoded value of the L2 cache size.
The capacity of the memory is derived using the formula 2(8+SZ) and expressed as bytes. Here, L2SZ is a 
nonzero value, and L2SZ = 0 indicates that the memory is not present.
For the Cortex-M7 cores in this chip, L2SZ = 0h (not present).
23-16
L2WY
L2 Cache Ways
Provides the number of cache ways for the L2 cache.
For the Cortex-M7 cores in this chip, L2WY = 0h (not present).
15-0
—
Reserved
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
96 / 5251


---
# 페이지 46

7.6.3.14
Processor 0 Configuration 2 (CP0CFG2)
Offset
Register
Offset
CP0CFG2
34h
Function
Defines the configuration information for processor 0 (CP0). It has the same field definitions and functionality as provided in 
Processor X Configuration 2 (CPXCFG2).
A privileged read from any bus controller returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
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
DTCMSZ 
ITCMSZ 
W
Reset
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
31-24
DTCMSZ
Tightly Coupled Data Memory Size
Provides an encoded value of the tightly coupled local data memory size.
The capacity of the memory is derived using the formula 2(8+SZ) and expressed as bytes. Here, TMLSZ is 
a nonzero value, and TMLSZ = 0 indicates that the memory is not present.
For the Cortex-M7 cores in this chip:
• DTCMSZ = 8h in Decoupled mode (64 KB)
• DTCMSZ = 9h in Lockstep mode (128 KB)
23-16
ITCMSZ
Instruction Tightly Coupled Memory Size
Provides an encoded value of the tightly coupled local instruction memory size.
The capacity of the memory is derived using the formula 2(8+SZ) and expressed as bytes. Here, TMUSZ is 
a nonzero value, and TMUSZ = 0 indicates that the memory is not present.
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
97 / 5251


---
# 페이지 47

Table continued from the previous page...
Field
Function
For the Cortex-M7 cores in this chip:
• ITCMSZ = 7h in Decoupled mode (32 KB)
• ITCMSZ = 8h in Lockstep mode (64 KB)
15-0
—
Reserved
7.6.3.15
Processor 0 Configuration 3 (CP0CFG3)
Offset
Register
Offset
CP0CFG3
38h
Function
Defines the configuration information for processor 0 (CP0). It has the same field definitions and functionality as provided in the 
CPXCFG3 register.
A privileged read from any bus controller returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
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
CPY 
CMP 
MMU 
SIMD 
FPU 
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
1
0
1
1
Fields
Field
Function
31-5
—
Reserved
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
98 / 5251


---
# 페이지 48

Table continued from the previous page...
Field
Function
4
CPY
Cryptography
Indicates whether the cryptography extensions are supported in the core.
For the Cortex-M7 cores in this chip, CPY = 0h.
0b - Not supported
1b - Supported
3
CMP
Core Memory Protection Unit
Indicates whether the core memory protection hardware is included in this core.
For the Cortex-M7 cores in this chip, CMP = 1h.
0b - Not included
1b - Included
2
MMU
Memory Management Unit
Indicates whether virtual management capabilities are supported in this core.
For the Cortex-M7 cores in this chip, MMU = 0h.
0b - Not supported
1b - Supported
1
SIMD
SIMD/NEON Instruction Support
Indicates whether the instruction set extensions supporting SIMD and/or NEON capabilities are included in 
the processor.
For the Cortex-M7 cores in this chip, SIMD = 1h.
0b - Not included
1b - Included
0
FPU
Floating Point Unit
Indicates whether hardware support for floating point capabilities is provided in the processor.
For the Cortex-M7 cores in this chip, FPU = 1h.
0b - Not provided
1b - Provided
7.6.3.16
Processor 1 Type (CP1TYPE)
Offset
Register
Offset
CP1TYPE
40h
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
99 / 5251


---
# 페이지 49

Function
Defines the configuration information for processor 1 (CP1). It has the same field definitions and functionality as provided in 
Processor X Type (CPXTYPE).
A read from any bus controller returns the appropriate processor information and attempted write accesses terminate with an error.
Access: User or privileged read-only
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
PERSONALITY 
W
Reset
0
1
0
0
0
0
1
1
0
1
0
0
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
PERSONALITY 
W
Reset
0
0
1
1
0
1
1
1
0
0
1
1
0
0
0
1
Fields
Field
Function
31-0
PERSONALITY
Personality Processor
Defines the processor personality for CP1.
CP1 = Cortex-M7 core 1 and processor personality = 43_4D_37_31h.
7.6.3.17
Processor 1 Number (CP1NUM)
Offset
Register
Offset
CP1NUM
44h
Function
Defines the configuration information for processor 1 (CP1). It has the same field definitions and functionality as provided in 
Processor X Number (CPXNUM).
A read from any bus controller returns the appropriate processor information and attempted write accesses terminate with an error.
Access: User or privileged read-only
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
100 / 5251


---
# 페이지 50

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
CPN 
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
31-2
—
Reserved
1-0
CPN
Processor Number
Defines the logical processor number for CP1.
For the Cortex-M7 core 1 processor, the processor number = 1.
7.6.3.18
Processor 1 Count (CP1REV)
Offset
Register
Offset
CP1REV
48h
Function
Defines the configuration information for processor 1 (CP1). It has the same field definitions and functionality as provided in 
Processor X Revision (CPXREV).
A read from any bus controller returns the appropriate processor information and attempted write accesses terminate with an error.
Access: User or privileged read-only
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
101 / 5251


---
# 페이지 51

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
RYPZ 
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
u
u
u
u
u
u
u
u
Fields
Field
Function
31-8
—
Reserved
7-0
RYPZ
Processor Revision
Defines the processor revision for CP1.
For the Cortex-M7 processor, RYPZ = 12h corresponding to the r1p2 core release.
7.6.3.19
Processor 1 Configuration 0 (CP1CFG0)
Offset
Register
Offset
CP1CFG0
4Ch
Function
Defines the configuration information for processor 1 (CP1). It has the same field definitions and functionality as provided in 
Processor X Configuration 0 (CPXCFG0).
A privileged read from any bus controller returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
102 / 5251


---
# 페이지 52

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
ICSZ 
ICWY 
W
Reset
0
0
0
0
0
1
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
DCSZ 
DCWY 
W
Reset
0
0
0
0
0
1
0
1
0
0
0
0
0
1
0
0
Fields
Field
Function
31-24
ICSZ
Level 1 Instruction Cache Size
Provides an encoded value of the instruction cache size.
The capacity of the memory is derived using the formula 2(8+SZ) and expressed as bytes. Here, ICSZ is a 
nonzero value, and ICSZ = 0 indicates that the memory is not present.
For information about cache sizes, see the "Miscellaneous Control Module (MCM)" chapter.
23-16
ICWY
Level 1 Instruction Cache Ways
Provides the number of cache ways for the instruction cache.
For the Cortex-M7 cores in this chip, ICWY = 2h (2-way set-associative).
15-8
DCSZ
L1 Data Cache Size
Provides an encoded value of the data cache size.
The capacity of the memory is derived using the formula 2(8+SZ) and expressed as bytes. Here, DCSZ is a 
nonzero value, and DCSZ = 0 indicates that the memory is not present.
For information about cache sizes, see the "Miscellaneous Control Module (MCM)" chapter.
7-0
DCWY
L1 Data Cache Ways
Provides the number of cache ways for the data cache.
For the Cortex-M7 cores in this chip, DCWY = 4h (4-way set-associative).
7.6.3.20
Processor 1 Configuration 1 (CP1CFG1)
Offset
Register
Offset
CP1CFG1
50h
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
103 / 5251


---
# 페이지 53

Function
Defines the configuration information for processor 1 (CP1). It has the same field definitions and functionality as provided in 
Processor X Configuration 1 (CPXCFG1).
A privileged read from any bus controller returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
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
L2SZ 
L2WY 
W
Reset
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
31-24
L2SZ
L2 Cache Size
Provides an encoded value of the L2 cache size.
The capacity of the memory is derived using the formula 2(8+SZ) and expressed as bytes. Here, L2SZ is a 
nonzero value, and L2SZ = 0 indicates that the memory is not present.
For the Cortex-M7 cores in this chip, L2SZ = 0h (not present).
23-16
L2WY
L2 Cache Ways
Provides the number of cache ways for the L2 cache.
For the Cortex-M7 cores in this chip, L2WY = 0h (not present).
15-0
—
Reserved
7.6.3.21
Processor 1 Configuration 2 (CP1CFG2)
Offset
Register
Offset
CP1CFG2
54h
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
104 / 5251


---
# 페이지 54

Function
Defines the configuration information for processor 1 (CP1). It has the same field definitions and functionality as provided in 
Processor X Configuration 2 (CPXCFG2).
A privileged read from any bus controller returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
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
DTCMSZ 
ITCMSZ 
W
Reset
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
31-24
DTCMSZ
Tightly Coupled Data Memory Size
Provides an encoded value of the tightly coupled local data memory size.
The capacity of the memory is derived using the formula 2(8+SZ) and expressed as bytes. Here, TMLSZ is 
a nonzero value, and TMLSZ = 0 indicates that the memory is not present.
For the Cortex-M7 cores in this chip, DTCMSZ = 8h in Decoupled mode (64 KB), and this value is not 
applicable in Lockstep mode.
23-16
ITCMSZ
Instruction Tightly Coupled Memory Size
Provides an encoded value of the tightly coupled local instruction memory size. The capacity of the memory 
is derived using the formula 2(8+SZ) and expressed as bytes. Here, TMUSZ is a nonzero value, and TMUSZ 
= 0 indicates that the memory is not present.
For the Cortex-M7 cores in this chip, ITCMSZ = 7h in Decoupled mode (32 KB); this value is not applicable 
in Lockstep mode.
15-0
—
Reserved
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
105 / 5251


---
# 페이지 55

7.6.3.22
Processor 1 Configuration 3 (CP1CFG3)
Offset
Register
Offset
CP1CFG3
58h
Function
Defines the configuration information for processor 1 (CP1). It has the same field definitions and functionality as provided in the 
CPXCFG3 register.
A privileged read from any bus controller returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
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
CPY 
CMP 
MMU 
SIMD 
FPU 
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
1
0
1
1
Fields
Field
Function
31-5
—
Reserved
4
CPY
Cryptography
Indicates whether cryptography extensions are supported in the core.
For the Cortex-M7 cores in this chip, CPY = 0h.
0b - Not supported
1b - Supported
3
CMP
Core Memory Protection Unit
Indicates whether the core memory protection hardware is included in this core.
For the Cortex-M7 cores in this chip, CMP = 1h.
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
106 / 5251


---
# 페이지 56

Table continued from the previous page...
Field
Function
0b - Not included
1b - Included
2
MMU
Memory Management Unit
Indicates whether virtual management capabilities are supported in this core.
For the Cortex-M7 cores in this chip, MMU = 0h.
0b - Not supported
1b - Supported
1
SIMD
SIMD/NEON Instruction Support
Indicates whether the instruction set extensions supporting SIMD and/or NEON capabilities are included in 
the processor.
For the Cortex-M7 cores in this chip, SIMD = 1h.
0b - Not included
1b - Included
0
FPU
Floating Point Unit
Indicates whether the processor includes hardware support for floating point capabilities.
For the Cortex-M7 cores in this chip, FPU = 1h.
0b - Not included
1b - Included
7.6.3.23
Processor 2 Type (CP2TYPE)
Offset
Register
Offset
CP2TYPE
60h
Function
Defines the configuration information for processor 2 (CP2). It has the same field definitions and functionality as provided in 
Processor X Type (CPXTYPE).
A read from any bus controller returns the appropriate processor information and attempted write accesses terminate with an error.
Access: User or privileged read-only
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
107 / 5251


---
# 페이지 57

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
PERSONALITY 
W
Reset
0
1
0
0
0
0
1
1
0
1
0
0
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
PERSONALITY 
W
Reset
0
0
1
1
0
1
1
1
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
31-0
PERSONALITY
Processor Personality
Defines the processor personality for CP2.
CP2 = Cortex-M7 core 2 and processor personality = 43_4D_37_32h.
7.6.3.24
Processor 2 Number (CP2NUM)
Offset
Register
Offset
CP2NUM
64h
Function
Defines the configuration information for processor 2 (CP2). It has the same field definitions and functionality as provided in 
Processor X Number (CPXNUM).
A read from any bus controller returns the appropriate processor information and attempted write accesses terminate with an error.
Access: User or privileged read-only
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
108 / 5251


---
# 페이지 58

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
CPN 
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
1
0
Fields
Field
Function
31-2
—
Reserved
1-0
CPN
Processor Number
Defines the logical processor number for CP2.
For Cortex-M7 core 2, processor number = 2.
7.6.3.25
Processor 2 Count (CP2REV)
Offset
Register
Offset
CP2REV
68h
Function
Defines the configuration information for processor 2 (CP2). It has the same field definitions and functionality as provided in 
Processor X Revision (CPXREV).
A read from any bus controller returns the appropriate processor information and attempted write accesses terminate with an error.
Access: User or privileged read-only
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
109 / 5251


---
# 페이지 59

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
RYPZ 
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
u
u
u
u
u
u
u
u
Fields
Field
Function
31-8
—
Reserved
7-0
RYPZ
Processor Revision
Defines the processor revision for CP2.
For the Cortex-M7 processor, RYPZ = 12h corresponding to the r1p2 core release.
7.6.3.26
Processor 2 Configuration 0 (CP2CFG0)
Offset
Register
Offset
CP2CFG0
6Ch
Function
Defines the configuration information for processor 2 (CP2). It has the same field definitions and functionality as provided in 
Processor X Configuration 0 (CPXCFG0).
A privileged read from any bus controller returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
110 / 5251


---
# 페이지 60

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
ICSZ 
ICWY 
W
Reset
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
DCSZ 
DCWY 
W
Reset
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
1
0
0
Fields
Field
Function
31-24
ICSZ
Level 1 Instruction Cache Size
Provides an encoded value of the instruction cache size.
The capacity of the memory is derived using the formula 2(8+SZ) and expressed as bytes. Here, ICSZ is a 
nonzero value, and ICSZ = 0 indicates that the memory is not present.
For information about cache sizes, see the "Miscellaneous Control Module (MCM)" chapter.
23-16
ICWY
Level 1 Instruction Cache Ways
Provides the number of cache ways for the instruction cache.
For the Cortex-M7 cores in this chip, ICWY = 2h (2-way set-associative).
15-8
DCSZ
L1 Data Cache Size
Provides an encoded value of the data cache size.
The capacity of the memory is derived using the formula 2(8+SZ) and expressed as bytes. Here, DCSZ is a 
nonzero value, and DCSZ = 0 indicates that the memory is not present.
For information about cache sizes, see the "Miscellaneous Control Module (MCM)" chapter.
7-0
DCWY
L1 Data Cache Ways
Provides the number of cache ways for the data cache.
For the Cortex-M7 cores in this chip, DCWY = 4h (4-way set-associative).
7.6.3.27
Processor 2 Configuration 1 (CP2CFG1)
Offset
Register
Offset
CP2CFG1
70h
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
111 / 5251


---
# 페이지 61

Function
Defines the configuration information for processor 2 (CP2). It has the same field definitions and functionality as provided in 
Processor X Configuration 1 (CPXCFG1).
A privileged read from any bus controller returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
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
L2SZ 
L2WY 
W
Reset
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
31-24
L2SZ
L2 Cache Size
Provides an encoded value of the L2 cache size. The capacity of the memory is derived using the formula 
2(8+SZ) and expressed as bytes. Here, L2SZ is a nonzero value, and L2SZ = 0 indicates that the memory is 
not present.
For the Cortex-M7 cores in this chip, L2SZ = 0h (not present).
23-16
L2WY
L2 Cache Ways
Provides the number of cache ways for the L2 cache.
For the Cortex-M7 cores in this chip, L2WY = 0h (not present).
15-0
—
Reserved
7.6.3.28
Processor 2 Configuration 2 (CP2CFG2)
Offset
Register
Offset
CP2CFG2
74h
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
112 / 5251


---
# 페이지 62

Function
Defines the configuration information for processor 2 (CP2). It has the same field definitions and functionality as provided in 
Processor X Configuration 2 (CPXCFG2).
A privileged read from any bus controller returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
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
DTCMSZ 
ITCMSZ 
W
Reset
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
31-24
DTCMSZ
Tightly Coupled Data Memory Size
Provides an encoded value of the tightly coupled local data memory size.
The capacity of the memory is derived using the formula 2(8+SZ) and expressed as bytes. Here, TMLSZ is 
a nonzero value, and TMLSZ = 0 indicates that the memory is not present.
For the Cortex-M7 cores in this chip, DTCMSZ = 8h in Decoupled mode (64 KB), and this value is not 
applicable in Lockstep mode.
23-16
ITCMSZ
Instruction Tightly Coupled Memory Size
Provides an encoded value of the tightly coupled local instruction memory size. The capacity of the memory 
is derived using the formula 2(8+SZ) and expressed as bytes. Here, TMUSZ is a nonzero value, and TMUSZ 
= 0 indicates that the memory is not present.
For the Cortex-M7 cores in this chip, ITCMSZ = 7h in Decoupled mode (32 KB); this value is not applicable 
in Lockstep mode.
15-0
—
Reserved
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
113 / 5251


---
# 페이지 63

7.6.3.29
Processor 2 Configuration 3 (CP2CFG3)
Offset
Register
Offset
CP2CFG3
78h
Function
Defines the configuration information for processor 2 (CP2). It has the same field definitions and functionality as provided in the 
CPXCFG3 register.
A privileged read from any bus controller returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
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
CPY 
CMP 
MMU 
SIMD 
FPU 
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
1
0
1
1
Fields
Field
Function
31-5
—
Reserved
4
CPY
Cryptography
Indicates whether cryptography extensions are supported in the core.
For the Cortex-M7 cores in this chip, CPY = 0h.
0b - Not supported
1b - Supported
3
CMP
Core Memory Protection Unit
Indicates whether the core memory protection hardware is included in this core.
For the Cortex-M7 cores in this chip, CMP = 1h.
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
114 / 5251


---
# 페이지 64

Table continued from the previous page...
Field
Function
0b - Not included
1b - Included
2
MMU
Memory Management Unit
Indicates whether virtual management capabilities are supported in this core.
For the Cortex-M7 cores in this chip, MMU = 0h.
0b - Not supported
1b - Supported
1
SIMD
SIMD/NEON Instruction Support
Indicates whether the instruction set extensions supporting SIMD and/or NEON capabilities are included in 
the processor.
For the Cortex-M7 cores in this chip, SIMD = 1h.
0b - Not included
1b - Included
0
FPU
Floating Point Unit
Indicates whether the processor includes hardware support for floating point capabilities.
For the Cortex-M7 cores in this chip, FPU = 1h.
0b - Not included
1b - Included
7.6.3.30
Processor 3 Type (CP3TYPE)
Offset
Register
Offset
CP3TYPE
80h
Function
Defines the configuration information for processor 3 (CP3). It has the same field definitions and functionality as provided in 
Processor X Type (CPXTYPE).
A read from any bus controller returns the appropriate processor information and attempted write accesses terminate with an error.
Access: User or privileged read-only
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
115 / 5251


---
# 페이지 65

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
PERSONALITY 
W
Reset
0
1
0
0
0
0
1
1
0
1
0
0
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
PERSONALITY 
W
Reset
0
0
1
1
0
1
1
1
0
0
1
1
0
0
1
1
Fields
Field
Function
31-0
PERSONALITY
Processor Personality
Defines the processor personality for CP3.
CP3 = Cortex-M7 core 3 and processor personality = 43_4D_37_33h.
7.6.3.31
Processor 3 Number (CP3NUM)
Offset
Register
Offset
CP3NUM
84h
Function
Defines the configuration information for processor 3 (CP3). It has the same field definitions and functionality as provided in 
Processor X Number (CPXNUM).
A read from any bus controller returns the appropriate processor information and attempted write accesses terminate with an error.
Access: User or privileged read-only
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
116 / 5251


---
# 페이지 66

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
CPN 
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
1
1
Fields
Field
Function
31-2
—
Reserved
1-0
CPN
Processor Number
Defines the logical processor number for CP3.
For Cortex-M7 core 3, processor number = 3.
7.6.3.32
Processor 3 Count (CP3REV)
Offset
Register
Offset
CP3REV
88h
Function
Defines the configuration information for processor 3 (CP3). It has the same field definitions and functionality as provided in 
Processor X Revision (CPXREV).
A read from any bus controller returns the appropriate processor information and attempted write accesses terminate with an error.
Access: User or privileged read-only
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
117 / 5251


---
# 페이지 67

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
RYPZ 
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
u
u
u
u
u
u
u
u
Fields
Field
Function
31-8
—
Reserved
7-0
RYPZ
Processor Revision
Defines the processor revision for CP3.
For the Cortex-M7 processor, RYPZ = 12h corresponding to the r1p2 core release.
7.6.3.33
Processor 3 Configuration 0 (CP3CFG0)
Offset
Register
Offset
CP3CFG0
8Ch
Function
Defines the configuration information for processor 3 (CP3). It has the same field definitions and functionality as provided in 
Processor X Configuration 0 (CPXCFG0).
A privileged read from any bus controller returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
118 / 5251


---
# 페이지 68

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
ICSZ 
ICWY 
W
Reset
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
DCSZ 
DCWY 
W
Reset
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
1
0
0
Fields
Field
Function
31-24
ICSZ
Level 1 Instruction Cache Size
Provides an encoded value of the instruction cache size.
The capacity of the memory is derived using the formula 2(8+SZ) and expressed as bytes. Here, ICSZ is a 
nonzero value, and ICSZ = 0 indicates that the memory is not present.
For information about cache sizes, see the "Miscellaneous Control Module (MCM)" chapter.
23-16
ICWY
Level 1 Instruction Cache Ways
Provides the number of cache ways for the instruction cache.
For the Cortex-M7 cores in this chip, ICWY = 2h (2-way set-associative).
15-8
DCSZ
L1 Data Cache Size
Provides an encoded value of the data cache size.
The capacity of the memory is derived using the formula 2(8+SZ) and expressed as bytes. Here, DCSZ is a 
nonzero value, and DCSZ = 0 indicates that the memory is not present.
For information about cache sizes, see the "Miscellaneous Control Module (MCM)" chapter.
7-0
DCWY
L1 Data Cache Ways
Provides the number of cache ways for the data cache.
For the Cortex-M7 cores in this chip, DCWY = 4h (4-way set-associative).
7.6.3.34
Processor 3 Configuration 1 (CP3CFG1)
Offset
Register
Offset
CP3CFG1
90h
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
119 / 5251


---
# 페이지 69

Function
Defines the configuration information for processor 3 (CP3). It has the same field definitions and functionality as provided in 
Processor X Configuration 1 (CPXCFG1).
A privileged read from any bus controller returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
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
L2SZ 
L2WY 
W
Reset
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
31-24
L2SZ
L2 Cache Size
Provides an encoded value of the L2 cache size. The capacity of the memory is derived using the formula 
2(8+SZ) and expressed as bytes. Here, L2SZ is a nonzero value, and L2SZ = 0 indicates that the memory is 
not present.
For the Cortex-M7 cores in this chip, L2SZ = 0h (not present).
23-16
L2WY
L2 Cache Ways
Provides the number of cache ways for the L2 cache.
For the Cortex-M7 cores in this chip, L2WY = 0h (not present).
15-0
—
Reserved
7.6.3.35
Processor 3 Configuration 2 (CP3CFG2)
Offset
Register
Offset
CP3CFG2
94h
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
120 / 5251


---
# 페이지 70

Function
Defines the configuration information for processor 3 (CP3). It has the same field definitions and functionality as provided in 
Processor X Configuration 2 (CPXCFG2).
A privileged read from any bus controller returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
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
DTCMSZ 
ITCMSZ 
W
Reset
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
31-24
DTCMSZ
Tightly Coupled Data Memory Size
Provides an encoded value of the tightly coupled local data memory size.
The capacity of the memory is derived using the formula 2(8+SZ) and expressed as bytes. Here, TMLSZ is 
a nonzero value, and TMLSZ = 0 indicates that the memory is not present.
For the Cortex-M7 cores in this chip, DTCMSZ = 8h in Decoupled mode (64 KB), and this value is not 
applicable in Lockstep mode.
23-16
ITCMSZ
Instruction Tightly Coupled Memory Size
Provides an encoded value of the tightly coupled local instruction memory size. The capacity of the memory 
is derived using the formula 2(8+SZ) and expressed as bytes. Here, TMUSZ is a nonzero value, and TMUSZ 
= 0 indicates that the memory is not present.
For the Cortex-M7 cores in this chip, ITCMSZ = 7h in Decoupled mode (32 KB); this value is not applicable 
in Lockstep mode.
15-0
—
Reserved
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
121 / 5251


---
# 페이지 71

7.6.3.36
Processor 3 Configuration 3 (CP3CFG3)
Offset
Register
Offset
CP3CFG3
98h
Function
Defines the configuration information for processor 3 (CP3). It has the same field definitions and functionality as provided in the 
CPXCFG3 register.
A privileged read from any bus controller returns the appropriate processor information and attempted write accesses terminate 
with an error.
Access: User or privileged read-only
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
CPY 
CMP 
MMU 
SIMD 
FPU 
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
1
0
1
1
Fields
Field
Function
31-5
—
Reserved
4
CPY
Cryptography
Indicates whether cryptography extensions are supported in the core.
For the Cortex-M7 cores in this chip, CPY = 0h.
0b - Not supported
1b - Supported
3
CMP
Core Memory Protection Unit
Indicates whether the core memory protection hardware is included in this core.
For the Cortex-M7 cores in this chip, CMP = 1h.
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
122 / 5251


---
# 페이지 72

Table continued from the previous page...
Field
Function
0b - Not included
1b - Included
2
MMU
Memory Management Unit
Indicates whether virtual management capabilities are supported in this core.
For the Cortex-M7 cores in this chip, MMU = 0h.
0b - Not supported
1b - Supported
1
SIMD
SIMD/NEON Instruction Support
Indicates whether the instruction set extensions supporting SIMD and/or NEON capabilities are included in 
the processor.
For the Cortex-M7 cores in this chip, SIMD = 1h.
0b - Not included
1b - Included
0
FPU
Floating Point Unit
Indicates whether the processor includes hardware support for floating point capabilities.
For the Cortex-M7 cores in this chip, FPU = 1h.
0b - Not included
1b - Included
7.6.3.37
Interrupt Router CPn Interrupt Status (IRCP0ISR0 - IRCP3ISR3)
Offset
For n = 0 to 3; m = 0 to 3:
Register
Offset
IRCPnISRm
200h + (n × 20h) + (m × 8h)
Function
Provides an interrupt bit map, where each bit defines the state of a unique MSI based on the initiating core. An MSI interrupt clears 
in an interrupt service routine by writing 1 to the appropriate field in IRCPnISRm.
In this discussion, CPm represents the initiating core and CPn represents the target core for a core-to-core interrupt. For more 
information on interrupt source mapping, see the interrupt map file attached to this document.
For read access:
• Reads to IRCPnISRm are only accessible in Privileged mode using 32-bit (word) accesses.
• Privileged 32-bit read accesses from noncore (and nondebugger) bus controllers are treated as RAZ.
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
123 / 5251


---
# 페이지 73

• Attempted accesses in User mode or the ones using a size other than 32 bits are not permitted. They terminate with an error.
• When CPn requests to read IRCPnISRm, MSCM returns the entire content of IRCPnISRm.
• When a trusted core, as the IRCPCFG register indicates, requests to read IRCPnISRm, MSCM returns the entire content 
of IRCPnISRm.
• When the debugger requests to read IRCPnISRm, MSCM returns the entire content of IRCPnISRm.
• When CPm requests to read IRCPnISRm, MSCM returns the value of the corresponding status, CPm_INT, while not exposing 
all the other pending interrupts that the cores initiated.
• When CPm requests to read IRCPnISRm, MSCM returns the value of the corresponding status, CPm_INT, in bit position 0, 
reflecting how CPm set the MSI when it wrote to IRCPnIGRm. All the other fields on the returned read value are zero-filled.
For write access:
• Writes to IRCPnISRm are only accessible in Privileged mode using 32-bit (word) accesses.
• Attempted accesses in User mode or the ones using a size other than 32 bits are not permitted. They terminate with an 
error.
• Writes to IRCPnISRm follow the Write 1 to Clear (W1C) protocol, whereby writing 1 causes the corresponding field to 
become 0, and writing 0 is ignored.
• The target core, CPn, has full access to write to all the fields of IRCPnISRm.
• A trusted core, as the IRCPCFG register indicates, has full access to write to all the fields of IRCPnISRm.
• When CPm is different from CPn, the W1C action by CPm only clears IRCPnISRm[CPm_INT].
• The CPm field must present W1C in bit position 0 to clear its corresponding interrupt. Write data bits 1-31 that CPm 
presents are ignored.
• Privileged write accesses from the noncore (and nondebugger) bus controllers are treated as Writes Ignored (WI).
• Privileged write accesses from the debugger are treated as WI.
Access: Privileged mode only
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
CP3_
INT 
CP2_
INT 
CP1_
INT 
CP0_
INT 
W
W1C
W1C
W1C
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
Fields
Field
Function
31-4
Reserved
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
124 / 5251


---
# 페이지 74

Table continued from the previous page...
Field
Function
—
3
CP3_INT
CP3-to-CPn Interrupt
Generates a directed interrupt initiated by core 3 targeting core n, if the appropriate interrupt routing bit 
is enabled. The interrupt is negated when the target core, a trusted core, or core 3 writes 1 to clear the 
field.
0b - No interrupt is asserted to CPn
1b - Interrupt to CPn is asserted
2
CP2_INT
CP2-to-CPn Interrupt
Generates a directed interrupt initiated by core 2 targeting core n, if the appropriate interrupt routing bit 
is enabled. The interrupt is negated when the target core, a trusted core, or core 2 writes 1 to clear the 
field.
0b - No interrupt is asserted to CPn
1b - Interrupt to CPn is asserted
1
CP1_INT
CP1-to-CPn Interrupt
Generates a directed interrupt initiated by core 1 targeting core n, if the appropriate interrupt routing bit 
is enabled. The interrupt is negated when the target core, a trusted core, or core 1 writes 1 to clear the 
field.
0b - No interrupt is asserted to CPn
1b - Interrupt to CPn is asserted
0
CP0_INT
CP0-to-CPn Interrupt
Generates a directed interrupt initiated by core 0 targeting core n, if the appropriate interrupt routing bit 
is enabled. The interrupt is negated when the target core, a trusted core, or core 0 writes 1 to clear the 
field.
0b - No interrupt asserted to CPn
1b - Interrupt to CPn asserted
7.6.3.38
Interrupt Router CPn Interrupt Generation (IRCP0IGR0 - IRCP3IGR3)
Offset
For n = 0 to 3; m = 0 to 3:
Register
Offset
IRCPnIGRm
204h + (n × 20h) + (m × 8h)
Function
Provides a mechanism for cores to initiate an MSI to another core in the system.
Privileged, 32-bit accesses from the:
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
125 / 5251


---
# 페이지 75

• Cortex-M7 cores are treated as RAZ/W.
• Debugger are treated as RAZ/WI.
• Noncore (and nondebugger) bus controllers are treated as RAZ/WI.
Access: Privileged mode only. Attempted accesses in User mode or the ones using a size other than 32 bits are not permitted and 
terminate with an error.
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
0
W
INT_
EN 
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
31-1
—
Reserved
0
INT_EN
Interrupt Enable
Initiates a core-to-core interrupt targeting CPn, if CPm writes to this field (where n indicates the logical 
core number (0-1) and m represents the interrupt number (0-3)).
7.6.3.39
Interrupt Router Configuration (IRCPCFG)
Offset
Register
Offset
IRCPCFG
400h
Function
Provides a mechanism to designate specific cores in the system as trusted. These trusted cores are allowed to access and 
manage outstanding MSIs.
Privileged, 32-bit accesses from the:
• Cortex-M7 cores are treated as R/W.
• Debugger are treated as R/WI.
• Noncore (and nondebugger) bus controllers are treated as RAZ/WI.
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
126 / 5251


---
# 페이지 76

Attempted accesses in User mode or the ones using a size other than 32 bits are not permitted. They terminate with an error.
Access: Privileged mode only
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
LOCK 
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
CP3_
TR 
CP2_
TR 
CP1_
TR 
CP0_
TR 
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
LOCK
Lock
Provides a locking mechanism that can be used to limit the ability to write to the register. After you write 
1 to this field, it remains 1 until the next reset.
0b - Register can be written by any privileged write
1b - Register is locked (read-only) until the next reset
30-4
—
Reserved
3
CP3_TR
CP3 as Trusted Core
Indicates whether CP3 is a trusted core with access to read the full contents of IRCPnISRm.
0b - Not trusted
1b - Trusted
2
CP2_TR
CP2 as Trusted Core
Indicates whether CP2 is a trusted core with access to read the full contents of IRCPnISRm.
0b - Not trusted
1b - Trusted
1
CP1_TR
CP1 as Trusted Core
Indicates whether CP1 is a trusted core with access to read the full contents of IRCPnISRm.
0b - Not trusted
1b - Trusted
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
127 / 5251


---
# 페이지 77

Table continued from the previous page...
Field
Function
0
CP0_TR
CP0 as Trusted Core
Indicates whether CP0 is a trusted core with access to read the full contents of IRCPnISRm.
0b - Not trusted
1b - Trusted
7.6.3.40
Memory Execution Controls (XN_CTRL)
Offset
Register
Offset
XN_CTRL
500h
Function
Controls whether an instruction fetch, also known as a code fetch or executable fetch, is allowed for SRAM and TCM.
 
• This register does not inhibit HSE_B instruction accesses.
• Only PRAM0, PRAM1, and PRAM2 support code execution control.
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
HLK 
SLK 
0
CM7_3
_D...
CM7_2
_D...
CM7_1
_D...
CM7_0
_D...
CM7_3
_D...
CM7_2
_D...
CM7_1
_D...
CM7_0
_D...
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
CM7_3
_I...
CM7_2
_I...
CM7_1
_I...
CM7_0
_I...
CM7_3
_D...
CM7_2
_D...
CM7_1
_D...
CM7_0
_D...
0
PRAM
_3 
PRAM
_2 
PRAM
_1 
PRAM
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
HLK
Hard Lock
Enables hard lock.
This field locks the register to disable writes until the next hardware reset.
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
128 / 5251


---
# 페이지 78

Table continued from the previous page...
Field
Function
0b - Disable
1b - Enable
30
SLK
Soft Lock
Enables soft lock.
This field locks the register to disable writes until this field becomes 0.
0b - Disable
1b - Enable
29-24
—
Reserved
23
CM7_3_DTCM
Transaction Control For Cortex-M7_3 DTCM
Does not select Cortex-M7_3 as target. All code fetch or executable fetch transactions to Cortex-M7_3 
DTCM are not generated because Cortex-M7_3 DTCM is not selected (backdoor access).
0b - Transaction enabled
1b - Transaction disabled
22
CM7_2_DTCM
Transaction Control For Cortex-M7_2 DTCM
Does not select Cortex-M7_2 as target. All code fetch or executable fetch transactions to Cortex-M7_2 
DTCM are not generated because Cortex-M7_2 DTCM is not selected (backdoor access).
0b - Transaction enabled
1b - Transaction disabled
21
CM7_1_DTCM
Transaction Control For Cortex-M7_1 DTCM
Does not select Cortex-M7_1 as target. All code fetch or executable fetch transactions to Cortex-M7_1 
DTCM are not generated because Cortex-M7_1 DTCM is not selected (backdoor access).
0b - Transaction enabled
1b - Transaction disabled
20
CM7_0_DTCM
Transaction Control For Cortex-M7_0 DTCM
Does not select Cortex-M7_0 as target. All code fetch or executable fetch transactions to Cortex-M7_0 
DTCM are not generated because Cortex-M7_0 DTCM is not selected (backdoor access).
0b - Transaction enabled
1b - Transaction disabled
19
CM7_3_DIS_D0
_D1TCM_EXEC
Disable D0 and D1 TCM Execution For Cortex-M7_3
Disables D0 and D1 TCM execution for Cortex-M7_3. It is provided to the core. If execution is disabled, it 
is taken as illegal access by the core.
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
129 / 5251


---
# 페이지 79

Table continued from the previous page...
Field
Function
0b - Enable
1b - Disable
18
CM7_2_DIS_D0
_D1TCM_EXEC
Disable D0 and D1 TCM Execution For Cortex-M7_2
Disables D0 and D1 TCM execution for Cortex-M7_2. It is provided to the core. If execution is disabled, it 
is taken as illegal access by the core.
0b - Enable
1b - Disable
17
CM7_1_DIS_D0
_D1TCM_EXEC
D0 and D1 TCM Execution For Cortex-M7_1
Disables D0 and D1 TCM execution for Cortex-M7_1. It is provided to the core. If execution is disabled, it 
is taken as illegal access by the core.
0b - Enable
1b - Disable
16
CM7_0_DIS_D0
_D1TCM_EXEC
D0 And D1 TCM Execution For Cortex-M7_0
Disables D0 and D1 TCM execution for Cortex-M7_0. It is provided to the core. If execution is disabled, it 
is taken as illegal access by the core.
0b - Enable
1b - Disable
15
CM7_3_ITCM
Transaction Control For Cortex-M7_3 ITCM
Does not select Cortex-M7_3 ITCM as target. All code fetch or executable fetch transactions to Cortex-
M7_3 ITCM are not generated because Cortex-M7_3 ITCM is not selected (backdoor access).
0b - Execution enabled
1b - Execution disabled
14
CM7_2_ITCM
Transaction Control For Cortex-M7_2 ITCM
Does not select Cortex-M7_2 ITCM as target. All code fetch or executable fetch transactions to Cortex-
M7_2 ITCM are not generated because Cortex-M7_2 ITCM is not selected (backdoor access).
0b - Execution enabled
1b - Execution disabled
13
CM7_1_ITCM
Transaction Control For Cortex-M7_1 ITCM
Does not select Cortex-M7_1 ITCM as target. All code fetch or executable fetch transactions to Cortex-
M7_1 ITCM are not generated because Cortex-M7_1 ITCM is not selected (backdoor access).
0b - Execution enabled
1b - Execution disabled
12
Transaction Control For Cortex-M7_0 ITCM
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
130 / 5251


---
# 페이지 80

Table continued from the previous page...
Field
Function
CM7_0_ITCM
Specifies the execution status.
This field does not select Cortex-M7_0 ITCM as target. All code fetch or executable fetch transactions to 
Cortex-M7_0 ITCM are not generated because Cortex-M7_0 ITCM is not selected (backdoor access).
0b - Execution enabled
1b - Execution disabled
11
CM7_3_DIS_IT
CM_EXEC
ITCM Execution for Cortex-M7_3
Disables ITCM execution for Cortex-M7_3. It is provided to the core. If execution is disabled, it is 
considered an illegal access by the core.
0b - Enable
1b - Disable
10
CM7_2_DIS_IT
CM_EXEC
ITCM Execution for Cortex-M7_2
Disables ITCM execution for Cortex-M7_2. It is provided to the core. If execution is disabled, it is 
considered an illegal access by the core.
0b - Enable
1b - Disable
9
CM7_1_DIS_IT
CM_EXEC
ITCM Execution For Cortex-M7_1
Disables ITCM execution for Cortex-M7_1. It is provided to the core. If execution is disabled, it is 
considered an illegal access by the core.
0b - Enable
1b - Disable
8
CM7_0_DIS_IT
CM_EXEC
ITCM Execution For Cortex-M7_0
Disables ITCM execution for Cortex-M7_0. It is provided to the core. If execution is disabled, it is 
considered an illegal access by the core.
0b - Enable
1b - Disable
7-4
—
Reserved
3
PRAM_3
Transaction Control For PRAM 3
Does not select PRAM3 as target. All code fetch or executable fetch transactions to PRAM3 are not 
generated because PRAM3 is not selected.
0b - Transaction enabled
1b - Transaction disabled
2
Transaction Control For PRAM 2
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
131 / 5251


---
# 페이지 81

Table continued from the previous page...
Field
Function
PRAM_2
Does not select PRAM2 as target. All code fetch or executable fetch transactions to PRAM2 are not 
generated because PRAM2 is not selected.
0b - Transaction enabled
1b - Transaction disabled
1
PRAM_1
Transaction Control For PRAM 1
Does not select PRAM1 as target. All code fetch or executable fetch transactions to PRAM1 are not 
generated because PRAM1 is not selected.
0b - Transaction enabled
1b - Transaction disabled
0
PRAM0
Transaction Control For PRAM 0
Does not select PRAM0 as target. All code fetch or executable fetch transactions to PRAM0 are not 
generated because PRAM0 is not selected.
0b - Transaction enabled
1b - Transaction disabled
7.6.3.41
Enable Interconnect Error Detection (ENEDC)
Offset
Register
Offset
ENEDC
600h
Function
Enables interconnect error detection.
For more information, see the FCCU file attached to this document.
Access: Privileged mode only
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
ADD_
CM7...
CM7_1
_T...
ADD_
CM7...
CM7_0
_T...
ADD_
AIP...
AIPS2 
ADD_
AIP...
AIPS1 
ADD_
AIP...
AIPS0 
ADD_
QSPI 
QSPI 
0
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
ADD_
PRA...
PRAM
1 
ADD_
PRA...
PRAM
0 
PF1_P
0_...
PF0_P
1_...
PF0_P
0_...
0
CM7_1
_A...
CM7_1
_A...
ENET 
HSE 
0
EDMA 
CM7_0
_A...
CM7_0
_A...
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
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
132 / 5251


---
# 페이지 82

Fields
Field
Function
31-30
—
Reserved
29
ADD_CM7_1_T
CM
Address Check For Cortex-M7_1_TCM
Enables address check for the Cortex-M7_1_TCM backdoor path.
0b - Disable
1b - Enable
28
CM7_1_TCM
Write Data Check For Cortex-M7_1_TCM
Enables write data check for the Cortex-M7_1_TCM backdoor path.
0b - Disable
1b - Enable
27
ADD_CM7_0_T
CM
Address Check For Cortex-M7_0_TCM
Enables address check for the Cortex-M7_0_TCM backdoor path.
0b - Disable
1b - Enable
26
CM7_0_TCM
Write Data Check For Cortex-M7_0_TCM
Enables write data check for the Cortex-M7_0_TCM backdoor path.
0b - Disable
1b - Enable
25
ADD_AIPS2
Address Check For AIPS2
Enables address check for the AIPS2 path.
0b - Disable
1b - Enable
24
AIPS2
Write Data Check For AIPS2
Enables write data check for the AIPS2 path.
0b - Disable
1b - Enable
23
ADD_AIPS1
Address Check For AIPS1
Enables address check for the AIPS1 path.
0b - Disable
1b - Enable
22
Write Data Check For AIPS1
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
133 / 5251


---
# 페이지 83

Table continued from the previous page...
Field
Function
AIPS1
Enables write data check for the AIPS1 path.
0b - Disable
1b - Enable
21
ADD_AIPS0
Address Check For AIPS0
Enables address check for the AIPS0 path.
0b - Disable
1b - Enable
20
AIPS0
Write Data Check For AIPS0
Enables write data check for the AIPS0 path.
0b - Disable
1b - Enable
19
ADD_QSPI
Address Check For QuadSPI
Enables address check for the QuadSPI path.
0b - Disable
1b - Enable
18
QSPI
Write Data Check For QuadSPI
Enables write data check for the QuadSPI path.
0b - Disable
1b - Enable
17
—
Reserved
16
—
Reserved
15
ADD_PRAM1
Address Check For PRAM1
Enables address check for the PRAM1 path.
0b - Disable
1b - Enable
14
PRAM1
Write Data Check For PRAM1
Enables write data check for the PRAM1 path.
0b - Disable
1b - Enable
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
134 / 5251


---
# 페이지 84

Table continued from the previous page...
Field
Function
13
ADD_PRAM0
Address Check For PRAM0
Enables address check for the PRAM0 path.
0b - Disable
1b - Enable
12
PRAM0
Write Data Check For PRAM0
Enables write data check for the PRAM0 path.
0b - Disable
1b - Enable
11
PF1_P0_ACHK
Address Check for PF1 P0
Enables address check for flash memory controller 1 P0.
0b - Disable
1b - Enable
10
PF0_P1_ACHK
Address Check for PF0 P1
Enables address check for flash memory controller 0 P1.
0b - Disable
1b - Enable
9
PF0_P0_ACHK
Address Check for PF0 P0
Enables address check for flash controller 0 P0.
0b - Disable
1b - Enable
8
—
Reserved
7
CM7_1_AHBP
Read Data Check For Cortex-M7_1_AHBP
Enables read data check for the Cortex-M7_1_AHBP path.
0b - Disable
1b - Enable
6
CM7_1_AHBM
Read Data Check For Cortex-M7_1_AHBM
Enables read data check for the Cortex-M7_1_AHBM path.
0b - Disable
1b - Enable
5
Read Data Check For ENET
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
135 / 5251


---
# 페이지 85

Table continued from the previous page...
Field
Function
ENET
Enables read data check for the ENET path.
0b - Disable
1b - Enable
4
HSE
Read Data Check For HSE_B
Enables read data check for the HSE_B path.
0b - Disable
1b - Enable
3
—
Reserved
2
EDMA
Read Data Check For eDMA
Enables read data check for the eDMA path.
0b - Disable
1b - Enable
1
CM7_0_AHBP
Read Data Check For Cortex-M7_0_AHBP
Enables read data check for the Cortex-M7_0_AHBP path.
0b - Disable
1b - Enable
0
CM7_0_AHBM
Read Data Check For Cortex-M7_0_AHBM
Enables read data check for the Cortex-M7_0_AHBM path.
0b - Disable
1b - Enable
7.6.3.42
Enable Interconnect Error Detection (ENEDC1)
Offset
Register
Offset
ENEDC1
604h
Function
Enables interconnect error detection.
For more information, see the FCCU file attached to this document.
Access: Privileged mode only
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
136 / 5251


---
# 페이지 86

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
PRAM
3_A...
PRAM
3_W...
0
TCM_
GSK...
SLV_C
HK...
SLV_C
HK...
SLV_C
HK...
MSTR
_CH...
MSTR
_CH...
CM7_3
_A...
CM7_3
_A...
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
ADD_
CM7...
CM7_2
_T...
CM7_3
_A...
CM7_3
_W...
ADD_
EN_...
EN_P
RAM2 
0
MSTR
_CH...
EDMA
_S1 
EDMA
_S0 
PF1_P
1_...
CM7_2
_A...
CM7_2
_A...
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
31-29
—
Reserved
28
PRAM3_ACHK
Address Check for PRAM3
Enables address check for PRAM3.
0b - Disable
1b - Enable
27
PRAM3_WCHK
Write Data Check for PRAM3
Enables write data check for PRAM3.
0b - Disable
1b - Enable
26-25
—
Reserved
24
TCM_GSKT_A
DDR_CHK
TCM Gasket Address Check
Enables address check for TCM gasket.
0b - Disable
1b - Enable
23
SLV_CHK_ACE
_ACCEL_RESU
LT_M1_GSKT_
ADDR_CHK
Target Check Accelerator Result M1 Gasket Address Check
Enables gasket address check for target accelerator result.
0b - Disable
1b - Enable
22
Target Check Accelerator Result M1 Gasket Write Data Check
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
137 / 5251


---
# 페이지 87

Table continued from the previous page...
Field
Function
SLV_CHK_ACE
_ACCEL_RESU
LT_M1_GSKT_
WDATA_CHK
Enables gasket write data check for target accelerator result.
0b - Disable
1b - Enable
21
SLV_CHK_ACE
_ADDR_CHK
Target Check Accelerator Address
Enables target check for accelerator address.
0b - Disable
1b - Enable
20
MSTR_CHK_A
CE_FEED_CHK
Controller Check Accelerator Feed
Enables controller check for accelerator feed.
0b - Disable
1b - Enable
19
MSTR_CHK_A
CE_RESULT_C
HK
Controller Check Accelerator Result
Enables controller check for accelerator result.
0b - Disable
1b - Enable
18
CM7_3_AHBP
Enable Read Data Check Cortex-M7_3_AHBP
Enables the read data check for the Cortex-M7_3_AHBP path.
0b - Disable
1b - Enable
17
CM7_3_AHBM
Enable Read Data Check Cortex-M7_3_AHBM
Enables the read data check for the Cortex-M7_3_AHBM path.
0b - Disable
1b - Enable
16
—
Reserved
15
ADD_CM7_2_T
CM
Enable Address Check Cortex-M7_2_TCM
Enables the address data check for the Cortex-M7_2_TCM backdoor path.
0b - Disable
1b - Enable
14
CM7_2_TCM
Enable Write Data Check Cortex-M7_2_TCM
Enables write data check for the Cortex-M7_2_TCM backdoor path.
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
138 / 5251


---
# 페이지 88

Table continued from the previous page...
Field
Function
0b - Disable
1b - Enable
13
CM7_3_ADDR_
CHK
Enable Address Check Cortex-M7_3_TCM
Enables the address check for the Cortex-M7_3_TCM backdoor path.
0b - Disable
1b - Enable
12
CM7_3_WDAT
A_CHK
Enable Write Data Check Cortex-M7_3_TCM
Enables write data check for the Cortex-M7_3_TCM backdoor path.
0b - Disable
1b - Enable
11
ADD_EN_PRA
M2
Enable Address Check PRAM 2
Enables the address check for the PRAM 2 path.
0b - Disable
1b - Enable
10
EN_PRAM2
Enable Write Data Check PRAM 2
Enables the write data check for PRAM2.
0b - Disable
1b - Enable
9-8
—
Reserved
7
MSTR_CHECK
_ENET1
Controller Check ENET1
Enables the controller check for ENET1.
0b - Disable
1b - Enable
6
EDMA_S1
Enable Address Check eDMA S1
Enables the address check for the eDMA S1 path.
0b - Disable
1b - Enable
5
EDMA_S0
Enable Address Check eDMA S0
Enables address check for the eDMA S0 path.
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
139 / 5251


---
# 페이지 89

Table continued from the previous page...
Field
Function
0b - Disable
1b - Enable
4
PF1_P1_ACHK
Enable Address Check PF1 P1
Enables address check for flash controller 1 P1.
0b - Disable
1b - Enable
3
CM7_2_AHBP
Enable Read Data Check Cortex-M7_2_AHBP
Enables read data check for the Cortex-M7_2_AHBP path.
0b - Disable
1b - Enable
2
CM7_2_AHBM
Enable Read Data Check Cortex-M7_2_AHBM
Enables read data check for the Cortex-M7_2_AHBM path.
0b - Disable
1b - Enable
1-0
—
Reserved
7.6.3.43
AHB Gasket Configuration (IAHBCFGREG)
Offset
Register
Offset
IAHBCFGREG
700h
Function
Controls the functional configuration of the AHB gaskets located on the platform.
Access: Privileged mode only
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
140 / 5251


---
# 페이지 90

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
HSE_
CMX...
ACE_
GSK...
ACE_
ACC...
CM7_3
_A...
CM7_3
_A...
CM7_2
_A...
CM7_1
_A...
CM7_0
_A...
CM7_3
_A...
CM7_2
_A...
CM7_1
_A...
CM7_0
_A...
PRAM
2_D...
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
TCM_
PRA...
PRAM
1_D...
GMAC
1_D...
USDH
C_D...
AIPS0
_D...
AIPS2
_D...
AIPS1
_D...
CM7_2
_A...
CM7_1
_A...
CM7_0
_A...
QSPI_
DI...
TCM_
DIS...
HSE_
DIS...
DMA_
AXB...
DMA_
AXB...
EMAC
_DI...
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
HSE_CMX_GS
KT_DAP_DISA
BLE_OPT_WR
HSE CMX Gasket Disable Write Optimization
Determines whether write burst optimizations in the HSE_B CMX gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
27
ACE_GSKT_DI
SABLE_OPT_W
R
ACE Gasket Disable Write Optimization
Determines whether write burst optimizations in the ACE gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
26
ACE_ACCEL_R
ESULT_M1_GS
KT_DISABLE_
OPT_WR
Ace Accelerator Disable Write Optimization
Determines whether write burst optimizations in the ace accelerator result M1 gasket are enabled 
or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
25
CM7_3_AHBS_
DIS_WR_OPT
Cortex-M7_3 AHBS Disable Write Optimization
Determines whether write burst optimizations in the Cortex-M7_3_AHBS gasket are enabled or disabled.
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
141 / 5251


---
# 페이지 91

Table continued from the previous page...
Field
Function
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
24
CM7_3_AHBP_
DIS_WR_OPT
Cortex-M7_3 AHBP Disable Write Optimization
Determines whether write burst optimizations in the Cortex-M7_3_AHBP gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
23
CM7_2_AHBP_
DIS_WR_OPT
Cortex-M7_2 AHBP Disable Write Optimization
Determines whether write burst optimizations in the Cortex-M7_2_AHBP gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
22
CM7_1_AHBP_
DIS_WR_OPT
Cortex-M7_1 AHBP Disable Write Optimization
Determines whether write burst optimizations in the Cortex-M7_1_AHBP gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
21
CM7_0_AHBP_
DIS_WR_OPT
Cortex-M7_0 AHBP Disable Write Optimization
Determines whether write burst optimizations in the Cortex-M7_0_AHBP gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
20
CM7_3_AHBM_
DIS_WR_OPT
Cortex-M7_3 AHBM Disable Write Optimization
Determines whether write burst optimizations in the Cortex-M7_3_AHBM gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
142 / 5251


---
# 페이지 92

Table continued from the previous page...
Field
Function
19
CM7_2_AHBM_
DIS_WR_OPT
Cortex-M7_2 AHBM Disable Write Optimization
Determines whether write burst optimizations in the Cortex-M7_2_AHBM gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
18
CM7_1_AHBM_
DIS_WR_OPT
Cortex-M7_1 AHBM Disable Write Optimization
Determines whether write burst optimizations in the Cortex-M7_1_AHBM gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
17
CM7_0_AHBM_
DIS_WR_OPT
Cortex-M7_0 AHBM Disable Write Optimization
Determines whether write burst optimizations in the Cortex-M7_0_AHBM gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
16
PRAM2_DIS_W
R_OPT
PRAM2 Disable Write Optimization
Determines whether write burst optimizations in the PRAM2 gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
15
TCM_PRAM_DI
S_WR_OPT
TCM PRAM Disable Write Optimization
Determines whether write burst optimizations in the TCM_PRAM gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
14
PRAM1_DIS_W
R_OPT
PRAM1 Disable Write Optimization
Determines whether write burst optimizations in the PRAM1 gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
143 / 5251


---
# 페이지 93

Table continued from the previous page...
Field
Function
0b - Enable
1b - Disable
13
GMAC1_DIS_W
R_OPT
GMAC1 Disable Write Optimization
Determines whether write burst optimizations in the GMAC1 gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
12
USDHC_DIS_W
R_OPT
uSDHC Disable Write Optimization
Determines whether write burst optimizations in the uSDHC gasket are enabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
11
AIPS0_DIS_WR
_OPT
AIPS0 Disable Write Optimization
Determines whether write burst optimizations in the AIPS2 AHB gasket are enabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
10
AIPS2_DIS_WR
_OPT
AIPS2 Disable Write Optimization
Determines whether write burst optimizations in the AIPS2 AHB gasket are enabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
9
AIPS1_DIS_WR
_OPT
AIPS1 Disable Write Optimization
Determines whether write burst optimizations in the AIPS1 AHB gasket are enabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
8
Cortex-M7_2 AHBS Disable Write Optimization
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
144 / 5251


---
# 페이지 94

Table continued from the previous page...
Field
Function
CM7_2_AHBS_
DIS_WR_OPT
Determines whether write burst optimizations in the Cortex-M7_2_AHBS gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
7
CM7_1_AHBS_
DIS_WR_OPT
Cortex-M7_1 AHBS Disable Write Optimization
Determines whether write burst optimizations in the Cortex-M7_1_AHBS gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
6
CM7_0_AHBS_
DIS_WR_OPT
Cortex-M7_0 AHBS Disable Write Optimization
Determines whether write burst optimizations in the Cortex-M7_0_AHBS gasket are enabled or disabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
5
QSPI_DIS_WR_
OPT
QSPI Disable Write Optimization
Determines whether write burst optimizations in the QuadSPI AHB gasket are enabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
4
TCM_DIS_WR_
OPT
TCM Disable Write Optimization
Determines whether write burst optimizations in the TCM AHB gasket are enabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
3
HSE_DIS_WR_
OPT
HSE Disable Write Optimization
Determines whether write burst optimizations in the HSE_B AHB gasket are enabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
Table continues on the next page...
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
145 / 5251


---
# 페이지 95

Table continued from the previous page...
Field
Function
0b - Enable
1b - Disable
2
DMA_AXBS_S1
_DIS_WR_OPT
DMA AXBS S1 Disable Write Optimization
Determines whether write burst optimizations in the DMA AXBS S1 AHB gasket are enabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
1
DMA_AXBS_S0
_DIS_WR_OPT
DMA AXBS S0 Disable Write Optimization
Determines whether write burst optimizations in the DMA AXBS S0 AHB gasket are enabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
0
EMAC_DIS_WR
_OPT
EMAC Disable Write Optimization
Determines whether write burst optimizations in the EMAC AHB gasket are enabled.
Enabling optimization allows performance improvements during burst writes. Disabling optimization is 
required only if you expect an early write burst termination from a controller.
0b - Enable
1b - Disable
7.6.3.44
Interrupt Router Shared Peripheral Routing Control (IRSPRC0 - IRSPRC239)
Offset
For n = 0 to 239:
Register
Offset
IRSPRCn
880h + (n × 2h)
Function
Provides an array of 16-bit registers, where each register defines the routing control for the corresponding interrupt request, 
starting from IRQ = 0 (first on-platform interrupt vector). See the interrupt map file attached to this document for details.
For this chip, each interrupt request can be either routed to a subset or to all the cores using the bit-mapped fields in IRSPRCn. If 
all the CPxEn fields are cleared, the interrupt request is disabled. Each routing control halfword can be locked by writing 1 to the 
LOCK field.
Privileged accesses from noncore (and nondebug) bus controllers are treated as RAZ/WI, and any attempted User mode 
reference terminates with an error. Attempted accesses using a size other than a 16-bit halfword also terminate with an error.
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
146 / 5251


---
# 페이지 96

If you write 1 to all the CPxEn bits, all the cores service the interrupt. You must ensure that no conflicts arise from this setup either 
via the interrupt handler or through programming core level interrupt routing (NVIC/GIC).
Reads and writes to this register beyond IRSPRC207 lead to unpredictable results.
Access: Privileged mode only
Diagram
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
LOCK 
0
M7_3 
M7_2 
M7_1 
M7_0 
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
1
1
1
1
Fields
Field
Function
15
LOCK
Lock
Provides a mechanism to lock the routing of the corresponding interrupt request. After you write 1 to this 
field, attempted writes to IRSPRCn are ignored until the next reset writes 0 to the field.
0b - Writes to IRSPRCn allowed
1b - Writes to IRSPRCn ignored
14-4
—
Reserved
3
M7_3
Enable Cortex-M7_3 Interrupt Steering
Enables the corresponding interrupt request to route to Cortex-M7_3.
0b - Routing disabled
1b - Routing enabled
2
M7_2
Enable Cortex-M7_2 Interrupt Steering
Enables the corresponding interrupt request to route to Cortex-M7_2.
0b - Routing disabled
1b - Routing enabled
1
M7_1
Enable Cortex-M7_1 Interrupt Steering
Enables the corresponding interrupt request to route to Cortex-M7_1.
0b - Routing disabled
1b - Routing enabled
0
M7_0
Enable Cortex-M7_0 Interrupt Steering
Enables the corresponding interrupt request to route to Cortex-M7_0.
0b - Routing disabled
1b - Routing enabled
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
147 / 5251


---
# 페이지 97

7.7 Glossary
GIC
Generic interrupt controller
IRQs
Interrupt requests
ISR
Interrupt service routine
MSI
Message signal interface
NVIC
Nested vector interrupt controller
NXP Semiconductors
Miscellaneous System Control Module (MSCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
148 / 5251


---