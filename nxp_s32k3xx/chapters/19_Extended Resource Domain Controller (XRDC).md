# 페이지 624

Chapter 19
Extended Resource Domain Controller (XRDC)
19.1 Chip-specific XRDC information
19.1.1 MDAC configuration
All MDACs with DID = 0 use the default DID parameter.
Table 73. MDAC configuration
Submodule 
instance
Configuration
XRDC 
MDACFG#
Bus initiator
Initiator 
ID value
Default 
DID
PID
Nonsecure 
input
Applicability
XRDC_MDAC0
Processor
1
Cortex-
M7_0, AXI, 
AHBP
0h
0h
PID0
0b
S32K310, 
S32K311, 
S32K312, 
S32K344, 
S32K324, 
S32K314, 
S32K342, 
S32K322, 
S32K341, 
S32K388, 
S32K389, 
S32K358, 
S32K348, 
S32K338, 
S32K328
Cortex-M7_0 
debug
8h
S32K388, 
S32K389, 
S32K358, 
S32K348, 
S32K338, 
S32K328
XRDC_MDAC1
Nonprocessor
1
eDMA AHB
2h
0h
—
1b
All
XRDC_MDAC4
Processor
1
Cortex-
M7_1, AXI, 
AHBP
1h
0h
PID4
0b
S32K322, 
S32K324, 
S32K388, 
S32K389, 
S32K358, 
S32K348, 
S32K338, 
S32K328
Cortex-M7_1 
debug
9h
S32K388, 
S32K389, 
S32K348,S32
K338, 
S32K328
Table continues on the next page...
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
675 / 5251


---
# 페이지 625

Table 73. MDAC configuration (continued)
Submodule 
instance
Configuration
XRDC 
MDACFG#
Bus initiator
Initiator 
ID value
Default 
DID
PID
Nonsecure 
input
Applicability
XRDC_MDAC5
Nonprocessor
1
EMAC AHB
4h
0h
—
1b
S32K342, 
S32K322, 
S32K314, 
S32K324, 
S32K344
GMAC_0 
AHB
S32K338, 
S32K348, 
S32K328, 
S32K358, 
S32K388, 
S32K389
XRDC_MDAC6
Processor
1
Cortex-
M7_2, AXI, 
AHBP
Cortex-M7_2 
debug
7h
Bh
0h
PID6
1b
S32K338, 
S32K358, 
S32K388, 
S32K389
XRDC_MDAC7
Nonprocessor
1
uSDHC AHB
6h
0h
—
1b
S32K338, 
S32K348, 
S32K328, 
S32K358
GMAC_1 
AHB
S32K388, 
S32K389
XRDC_MDAC8
Processor
1
Cortex-
M7_3, AXI, 
AHBP, 
debug
5h
0h
PID8
0b
S32K388, 
S32K389
XRDC_MDAC9
Nonprocessor
1
AES_ACCEL
8h, 9h
0h
—
1b
S32K388, 
S32K389
19.1.2 MRC configuration
Table 74. MRC configuration
Submodule instance
Region format
Number of 
region descriptors
Slaves protected (port number)
Applicability
XRDC_MRC0
Auto
161 or 8
PFLASH_0 (0)
PFLASH_1 (1)
PFLASH_2 (2)1
PFLASH_3 (3)
PFLASH_WR (3)
S32K310, S32K311, 
S32K312, S32K342, 
S32K322, S32K314, 
S32K324, S32K344, 
S32K358, S32K348, 
S32K338, 
S32K328, S32K388
XRDC_MRC0
Auto
16 or 8
PFLASH_0 (P0)
S32K389
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
676 / 5251


---
# 페이지 626

Table 74. MRC configuration (continued)
Submodule instance
Region format
Number of 
region descriptors
Slaves protected (port number)
Applicability
PFLASH_0 (P1)
PFLASH_0_WR
XRDC_MRC1
Auto
161 or 8
PRAM0_0 (0)
PRAM1_01 (1)
S32K310, S32K311, 
S32K312, S32K342, 
S32K322, S32K314, 
S32K324, S32K344, 
S32K358, S32K348, 
S32K338, S32K328, 
S32K388, S32K389
XRDC_MRC2
Auto
4
QuadSPI (0)
S32K342, 
S32K322, S32K314, 
S32K324, S32K344, 
S32K328, S32K338, 
S32K348, S32K358, 
S32K388, S32K389
XRDC_MRC3
Auto
16
TCM backdoor/ PRAM2(0)
TCM backdoor / PRAM2 (0) / 
PRAM3 (2)2
S32K358, S32K348, 
S32K338, S32K328, 
S32K388, S32K389
XRDC_MRC4
Auto
1
AES_ACCEL backdoor
S32K388, S32K389
XRDC_MRC5
Auto
1
PFLASH_1 (P0)
PFLASH_1 (P1)
PFLASH_1_WR
S32K389
1. Applicable to S32K342, S32K341, S32K322, S32K314, S32K324, S32K344, S32K328, S32K338, S32K348, 
S32K358, S32K388
2. Applicable to S32K389
19.1.3 PAC configuration
Table 75. PAC configuration
Module name
Slaves protected
Applicability
XRDC_PAC0
AIPS_0
S32K310, S32K311, S32K312, S32K342, S32K341, S32K322, 
S32K314, S32K324, S32K344, S32K358, S32K348, S32K338, S32K328, 
S32K388, S32K389
XRDC_PAC1
AIPS_1
S32K310, S32K311, S32K312, S32K342, S32K341, S32K322, 
S32K314, S32K324, S32K344, S32K358, S32K348, S32K338, S32K328, 
S32K388, S32K389
XRDC_PAC2
AIPS_2
S32K342, S32K341, S32K322, S32K314, S32K324, S32K344, S32K358, 
S32K348, S32K338, S32K328, S32K388, S32K389
 
For PDAC registers assignment to peripherals, see the memory map file attached to this document.
  NOTE  
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
677 / 5251


---
# 페이지 627

19.1.4 Number of Domain ID
Table 76. Number of Domain ID
Chip
Number of Domain 
ID supported
Supported values
S32K310, S32K311, S32K312
2
0, 1
S32K322, S32K342, S32K314, S32K324, S32K344
3
0, 1, 2
S32K358, S32K348, S32K338, S32K328
4
0, 1, 2, 3
S32K388, S32K389
5
0, 1, 2, 3, 4
19.1.5 Domain Error Word registers (DERR_Wx_0-18) mapping
The mapping of the domain error capture registers is as follows:
Table 77. Domain Error Word registers mapping
Register
Corresponding MRC/PAC
Available in chips
DERR_Wx_0
MRC0
S32K310, S32K311, S32K312, S32K342, S32K341, S32K322, 
S32K314, S32K324, S32K344, S32K358, S32K348, S32K338, S32K328, 
S32K388, S32K389
DERR_Wx_1
MRC1
S32K310, S32K311, S32K312, S32K342, S32K341, S32K322, 
S32K314, S32K324, S32K344, S32K358, S32K348, S32K338, S32K328, 
S32K388, S32K389
DERR_Wx_2
MRC2
S32K342, S32K341, S32K322, S32K314, S32K324, S32K344, S32K358, 
S32K348, S32K338, S32K328, S32K388, S32K389
DERR_Wx_3
MRC3
S32K358, S32K348, S32K338, S32K328, S32K388, S32K389
DERR_Wx_4
MRC4
S32K388, S32K389
DERR_Wx_16
PAC0
S32K310, S32K311, S32K312, S32K342, S32K341, S32K322, 
S32K314, S32K324, S32K344, S32K358, S32K348, S32K338, S32K328, 
S32K388, S32K389
DERR_Wx_17
PAC1
S32K310, S32K311, S32K312, S32K342, S32K341, S32K322, 
S32K314, S32K324, S32K344, S32K358, S32K348, S32K338, S32K328, 
S32K388, S32K389
DERR_Wx_18
PAC2
S32K342, S32K341, S32K322, S32K314, S32K324, S32K344, S32K358, 
S32K348, S32K338, S32K328, S32K388, S32K389
Where x: 0, 1, 2, 3.
If the above registers are accessed in chips wherein they are not present, a bus error gets reported.
19.1.6 Exceptions and violations
A write attempt by a noncore bus master outside the defined ranges leads to an exception in case the XRDC region is defined to 
prevent noncore master access. The chip generates a bus error if you violate XRDC policies.
19.1.7 Configuration using SBAF
SBAF must protect access to its own resources. Hence, XRDC is configured during initialization. SBAF provides the mechanism 
for you to configure XRDC during boot. You must program the configuration data in the application flash memory region.
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
678 / 5251


---
# 페이지 628

19.1.7.1
PDAC default configuration
SBAF configures and lock the following peripherals for its exclusive use. Read and write access to these peripheral are not 
provided to application domains.
Table 78. PDAC default configuration
Peripheral
Peripheral PDAC number
Remarks
Flash memory controller alternate
187
HSE_B uses the alternate interface exclusively.
Flash memory alternate
188
HSE_B uses the alternate interface exclusively.
Flash memory 1 controller alternate1
352
HSE_B uses the alternate interface exclusively.
Flash memory 1 alternate1
353
HSE_B uses the alternate interface exclusively.
1. Applicable to S32K389.
19.1.8 Configuration when HSE_B firmware-feature flag is cleared
When the HSE_B firmware-feature flag is cleared, SBAF:
• Does not permit XRDC configuration.
• Locks the aforementioned configurations.
19.1.9 HWCFG0 register reset value in different chips
Table 79. HWCFG0 reset value
Chip
Reset value
S32K310, S32K311, S32K312, S32K322
0x11010301
S32K341, S32K342, S32K314, S32K344, S32K324
0x12020502
S32K358, S32K348, S32K338, S32K328
0x12030703
S32K388
0x12040904
S32K389
0x12050904
19.2 Overview
XRDC manages access control between initiators (cores and noncore initiators) and targets (memories and peripherals) by 
placing them in virtual groups called domains.
Conceptually, a domain is one or more initiators and memories and peripherals, that are isolated from others. It may help to look 
at a domain as a permissions group within a computing environment. All initiators in a domain have the same access to chip 
resources such as memory and peripherals. See Introduction to domains for more information on domains.
The protection provided by XRDC access control is in addition to the local memory protection unit contained within each core.
 
Terminology in this chapter has been updated as follows:
Table 80. Updated terms
Updated term
Deprecated term
Initiator
Master
Target
Slave
  NOTE  
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
679 / 5251


---
# 페이지 629

19.2.1 Features
• Enables you to partition chip resources (initiator and target) into access-controlled domain.
— Each domain has a unique DID .
— The DID is an attribute of every system bus transaction.
• Provides a four-level hierarchical access control scheme for defining an ACP for each target in a domain. See Access control 
model for more information.
— Memory region descriptors define access policies for address ranges within memories.
— Peripheral access control registers define access policies for individual peripherals.
• Supports optional hardware semaphores to dynamically modify access rights for target resources.
19.2.2 Block diagram
Initiator m
XRDC
Domain
assignment
(MDAC)
Switch fabric or
crossbar
Memory module
Peripheral s
Peripheral access
contol policy
evaluation
(PAC)
Memory access
control policy
evaluation
(MRC)
Figure 46. Block diagram
19.2.3 Block descriptions
Block
Description
Domain assignment
A process that adds information to transactions, including:
• DID
• Privileged attribute
• Secure attribute
Domain assignment is performed by the MDAC submodule.
See:
• Domain assignment
• Master domain assignment controller (MDAC)
Initiator
A core or noncore (for example, DMA) module that can initiate transactions with memory or 
peripheral resources.
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
680 / 5251


---
# 페이지 630

Table continued from the previous page...
Block
Description
Memory
Non-volatile memory, RAM, or other memory.
Memory access control 
policy evaluation
A process that determines whether the domain associated with a transaction has access rights 
to a memory location. The process is performed by the MRC submodule.
See:
• Memory region ACP evaluation
• Memory region controller (MRC)
Peripheral
A nonmemory resource module within the chip—an ADC, timer module, or communications 
module, for example.
Peripheral access control 
policy evaluation
A process that determines whether the domain associated with a transaction has access rights 
to a peripheral. The process is performed by the PAC submodule.
See Peripheral access controller (PAC).
Crossbar
The chip's module and I/O interconnect infrastructure.
19.2.4 Indexes used in this chapter
Table 81. Indexes used in this chapter
Index
Description
c
Memory controller number. For example, MRCc.
d
Domain number. For example, PDAC_W0_6[DdACP].
m
Initiator number. For example, PIDm.
r
Memory region number. For example, RGD_W0_r.
s
PDAC slot number. For example, PDAC_W0_s[D0ACP].
w
Word number. In a group of registers consisting of consecutive 32-bit registers, w is the 0-indexed register 
number. For example, MRGD_Ww_0.
19.2.5 Exceptions and violations
A write attempt by a noncore bus initiator outside the defined ranges leads to an exception in case the XRDC region is defined to 
prevent noncore initiator access. The chip generates a bus error if you violate XRDC policies.
19.3 Modes of operation
XRDC does not support any special modes of operation.
19.4 External signal description
XRDC does not have any external signals.
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
681 / 5251


---
# 페이지 631

19.5 Functional description
19.5.1 Introduction to domains
A domain typically consists of one or more initiators, along with the memories and peripherals those initiators are allowed to 
access. Because it is access-controlled, a domain acts as an independent computing environment.
Domains enable applications to coexist on the same silicon with a firewall between them, enforcing absolute 
interference protection.
Generally, you create each domain to meet a specific need. Examples of XRDC domain usage include:
• Isolation of real-time from non-real-time applications to ensure resource availability
• Isolation of safety-critical code from non-safety-critical code
• Isolation of third-party untrusted applications from trusted software
• Isolation of memory regions to ensure data security or to prevent accidental overwrites
• Limiting write access for a specific area of system memory to a single DMA module instance
• Limiting read access for a specific area of system memory to a specific processor core
You can assign a core to multiple domains but only one of those domains can be active at a given time.
Within each XRDC instance, each domain has a unique identifier, known as its DID. If an XRDC instance has 16 DIDs, that means 
the instance has 16 available domains.
You control which initiators can access a peripheral by configuring the domain ACP for each peripheral. Similarly, you control 
which initiators can access a memory region by configuring the ACP for each memory region.
19.5.2 Submodules
XRDC implements its functionality through its hardware submodules:
• Master domain assignment controller (MDAC)
• Memory region controller (MRC)
• Peripheral access controller (PAC)
19.5.2.1
Master domain assignment controller (MDAC)
The MDAC submodule performs domain assignment logic. XRDC contains an MDAC submodule for each XRDC-protected 
initiator. Each MDAC assigns a DID to every transaction from its associated initiator. You configure the domain assignment activity 
for each MDAC through a set of registers, in one of two formats:
• DFMT0 core domain assignment registers
• DFMT1 noncore domain assignment registers
To understand the role of domains in XRDC protection, see Introduction to domains.
For a full explanation of the domain assignment process, see Domain assignment.
19.5.2.2
Memory region controller (MRC)
The MRC submodule performs memory region access control. Each XRDC instance contains the number of MRCs indicated in 
HWCFG0[NMRC]. Each MRC is associated with one or more memories (see the chip-specific XRDC information for details). The 
MRC controls memory access using memory region descriptors. MRCFGc[NMRGD] indicates the number of region descriptors 
available for MRC c.
Each memory region descriptor defines a memory address range and a configurable access control policy for each domain using 
a set of four or five 32-bit registers (see Memory ACP evaluation registers).
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
682 / 5251


---
# 페이지 632

Memory region descriptors also support including an optional hardware semaphore in the ACP evaluation for memory regions 
shared by multiple domains (see Hardware semaphores and dynamic access rights).
For a full explanation of the memory region ACP evaluation process, see Memory region ACP evaluation.
19.5.2.3
Peripheral access controller (PAC)
The PAC submodule provides domain access control for all peripherals connected to a single peripheral bus. Each XRDC contains 
the number of PACs indicated in HWCFG0[NPAC]. Each PAC supports up to 128 peripheral slots (see Finding the PDAC slot 
number for a peripheral). You configure the ACP for each peripheral using a set of PDAC_Ww_s registers (see Peripheral ACP 
evaluation registers).
Peripheral access control also enable a hardware semaphore to be included in the access control policy evaluation for peripherals 
shared by multiple domains. See Hardware semaphores and dynamic access rights for more details.
For a full explanation of the peripheral ACP evaluation process, see Peripheral ACP evaluation process.
19.5.3 Transaction protection
During application execution, high-level chip modules such as cores or DMA, Ethernet, known as initiators, initiate transaction 
requests to memory and peripheral resources. XRDC adds protection capabilities to ensure the requesting initiator accesses only 
the resources that it is authorized to access. These capabilities support security and safety requirements.
XRDC provides this protection by adding two steps to the unprotected transaction flow, as shown in XRDC transaction flow.
XRDC transaction processing differs depending on:
• The type of initiator making the request (see Transaction request sources).
• The type of target receiving the request (see Transaction targets).
 
See chip-specific XRDC information for the domain ID of each initiator on chip.
  NOTE  
19.5.4 XRDC transaction flow
Table 82. XRDC transaction flow
Step
Operation
Performed by
Description
1
Transaction 
request
Initiator
An initiator requests a read or write transaction targeting memory or a 
peripheral.
2
Domain 
assignment
XRDC
XRDC MDAC submodule intercepts the request and performs domain 
assignment, which adds this metadata to the transaction:
• DID
• Privileged attribute
• Secure attribute
3
Interconnect
Chip
The chip transmits the domain-assigned transaction request across the 
interconnect (crossbar).
4
ACP evaluation
XRDC
XRDC MRC or PAC submodule intercepts the transaction request and 
evaluates it against the target's ACP to determine whether the requesting 
initiator has sufficient access rights to the target. If it does, the transaction 
continues. Otherwise, XRDC generates an access violation error and the 
transaction terminates.
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
683 / 5251


---
# 페이지 633

Table 82. XRDC transaction flow (continued)
Step
Operation
Performed by
Description
5
Transaction 
response
Target resource
If the previous step does not generate an access violation error, the target 
resource processes the transaction request and transmits data (for read 
transactions) and transaction status information (for all transactions) back 
across the interconnect to the requesting initiator.
XRDC is not involved in the flow of information from the target resource back 
to the requesting initiator.
19.5.5 Domain assignment
19.5.5.1
Overview
Domain assignment associates a DID with each transaction request from an initiator. To determine the DID for a 
transaction, XRDC evaluates the domain-specific configuration data in the set of MDAC registers (MDA_Wn_m_DFMT0 or 
MDA_Wn_m_DFMT1) associated with the requesting initiator. The exact process depends on the source of the request (see 
Transaction request sources).
If the value of MDACFGm[NMDAR] is 1, which means a single Ww register for a given initiator, the specified domain identifier is 
used directly. In case this value is more than 1, which means there are multiple Ww registers for a given initiator, MDAC evaluates 
the conditional terms to determine a "hit". For all Ww hits, their corresponding domain identifiers are logically summed together 
(boolean OR). Use cases are typically expected to hit in a single Ww. Special care is needed if none of the conditional terms hit in 
any Wn evaluation; in this case, the generated DID = 0 and you must be aware of any potential access rights granted for this DID.
The number of MDAC registers can vary for each initiator. See the chip-specific information. MDACFGm[NMDAR] indicates the 
number of MDA registers, where m is the initiator number. You need m to locate the registers relevant for domain assignment. 
See the chip-specific XRDC information for more on initiator numbers. See:
• Register settings for DFMT0 direct domain assignment transactions
• Register settings for DFMT0 PID-based transactions
• Register settings for DFMT1 direct domain assignment transactions
Domain assignment also assigns the secure and privileged attributes to the transaction.
19.5.5.2
PID-based domain assignment
To provide more flexibility in routing core tasks to chip resources in different access-controlled domains, XRDC supports the use 
of a PID. If the core initiator contains a built-in PID register, indicated by HWCFG2[PIDPm] = 1 , XRDC reflects the core PID value 
in PIDm[PID], and bit 5 of that field indicates the secure attribute for the transaction request. Otherwise, an application can mimic 
PID-based domain assignment by writing a value to that field.
19.5.5.3
Transaction request sources
The domain assignment process for an XRDC-protected transaction request depends on the source of the request.
Table 83. Transaction request sources
Request source
Topic
Brief description
Core initiator
DFMT0 direct domain assignment 
example
Direct domain assignment using a DFMT0 master domain assignment 
register.
Core initiator
DFMT0 PID-based domain 
assignment example
PID-based domain assignment using a DFMT0 master domain 
assignment register.
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
684 / 5251


---
# 페이지 634

Table 83. Transaction request sources (continued)
Request source
Topic
Brief description
Core initiator
DFMT1 direct domain assignment 
example-single MDA
Direct domain assignment using a DFMT1 master domain assignment 
register with single MDA.
19.5.5.4
DFMT0 core domain assignment registers
Table 84. DFMT0 core domain assignment registers
Register
Index
MDACFGm
m = initiator number. See the chip-specific XRDC information for the available list of initiators with 
their IDs.
MDA_Ww_m_DFMT01
m = initiator number.
w = word (see MDA register structure). MDACFGm[NMDAR] indicates the number of MDA registers 
(words) per initiator.
PIDm
m = initiator number.
1. See MDA register structure.
19.5.5.5
DFMT1 noncore domain assignment registers
Table 85. DFMT1 noncore domain assignment registers
Register
Index
MDACFGm
m = initiator number. See the chip-specific XRDC information for the available list of initiators and 
their IDs.
MDA_Ww_m_DFMT11
m = initiator number.
w = word. MDACFGm[NMDAR] indicates the number of MDA registers (words) per initiator.
1. See MDA register structure.
19.5.5.6
MDA register structure
MDA_Wn_m_DFMT0
Core initiators
One set per domain
MDA_Wn_m_DFMT1
Noncore initiators
One set per master
MDA_Wn_m_DFMT1
Core initiators
One set per domain
VLD
LK1
PIDM
PID
LPID
LPE
PE
DIDS
DID
0
0
0
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
DFMT
VLD
LK1
SA
DIDB
PA
DID
0
0
0
0
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
DFMT
VLD
LK1
LPE
LPID
SA
DIDB
PA
DID
0
0
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
DFMT
Figure 47. MDA register structure
 
This XRDC configuration does not have LPE and LPID fields and should be considered as reserved fields.
  NOTE  
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
685 / 5251


---
# 페이지 635

19.5.6 ACP evaluation
19.5.6.1
Overview
When XRDC is not enabled, all peripherals and memories allow unrestricted access. XRDC allows you to limit that access to 
requests from a particular domain or domains with an application-specified ACP. XRDC intercepts the transaction request and 
evaluates it against the target's ACP to determine whether the requesting initiator has sufficient access rights to the target, based 
on the:
• Domain ID assignment (DID)
• Privileged attribute
• Secured attribute
XRDC obtains the target resource's domain ACP from the associated Domain Access Control Policy (DdACP) field (see Domain 
ACP specification) in the appropriate register set:
• Peripheral ACP evaluation registers
• Memory ACP evaluation registers
If ACP evaluation determines that the transaction request has sufficient access rights to the target resource, XRDC allows the 
transaction to continue. Otherwise, it terminates the request with an error and captures the address and attribute information in 
the appropriate error registers.
The exact process depends on the target of the request (see Transaction targets).
XRDC optionally supports the inclusion of a hardware semaphore to dynamically alter the ACP of a memory region or peripheral 
(see Hardware semaphores and dynamic access rights).
19.5.6.2
Transaction targets
The ACP evaluation for an XRDC-protected transaction request depends on the target of the request.
Table 86. Transaction targets
Request target
Topic
Brief description
Peripheral
Peripheral ACP evaluation example
Process for a transaction request to a target peripheral that is 
within a protected domain, with ACP evaluation configured by 
PDAC_Ww_s.
Memory
Memory ACP evaluation example
Process for a transaction request to a target memory region 
that is within a protected domain, with ACP evaluation 
configured by MRGD_Ww_r.
19.5.6.3
Peripheral ACP evaluation registers
Table 87. Peripheral ACP evaluation registers
Register
Index
Brief description
PDAC_W0_s1
s = peripheral slot
Specifies the ACP for an XRDC-protected peripheral, and an optional hardware 
semaphore.
PDAC_W1_s1
s = peripheral slot
Enables the set of PDAC registers for the associated peripheral and locks the set. 
Typically, you configure the peripheral by writing to the PDAC registers and then 
limiting their respective domains from making updates to the DdACP fields or by 
locking the set for all updates.
1. See PDAC register structure.
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
686 / 5251


---
# 페이지 636

19.5.6.4
PDAC register structure
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
0
0
LK2
SNUM
D7ACP
D6ACP
D5ACP
D4ACP
D3ACP
D2ACP
D1ACP
D0ACP
D15ACP
D14ACP
D13ACP
D12ACP
D11ACP
D10ACP
D9ACP
D8ACP
SE
VLD
0
PDAC_W0_r
PDAC_W1_r
Figure 48. PDAC register structure
19.5.6.5
Memory ACP evaluation registers
When XRDC is enabled (CR[GVLD] = 1), you cannot access any XRDC-protected memory unless you configure at least one set 
of memory region descriptors (see MRGD_Ww_r) that includes the targeted memory.
Table 88. Memory ACP evaluation registers
Register
Index
Brief description
MRCFGc
c = memory 
controller instance
Indicates the number of memory regions per memory controller (NMRGD). Each 
memory region is configured by a set of memory region descriptor registers 
(MRGD_Ww_r) described below.
MRGD_W0_r1
r = memory region
Specifies starting address for the memory region.
MRGD_W1_r1
r = memory region
Specifies ending address for the memory region.
MRGD_W2_r1
r = memory region
Specifies the ACP for each supported domain, and an optional hardware 
semaphore.
MRGD_W3_r1
r = memory region
Enables the set of MRGD registers for the associated region and locks the set. 
Typically, you define the memory region by writing to the MRGD registers and then 
limiting their respective domains from updating the DdACP fields or by locking the 
set for all updates.
1. See MRGD register structure.
19.5.6.6
MRGD register structure
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
SRTADDR
Reserved
ENDADDR
1
0
0
LK2
SNUM
D7ACP
D6ACP
D5ACP
D4ACP
D3ACP
D2ACP
D1ACP
D0ACP
D15ACP
D14ACP
D13ACP
D12ACP
D11ACP
D10ACP
D9ACP
D8ACP
SE
VLD
0
MRGD_W0_r
MRGD_W1_r
MRGD_W2_r
MRGD_W3_r
Figure 49. MRGD register structure
19.5.6.7
Access control model
XRDC supports a four-level hierarchical access control model. This model combines the traditional privileged (also known as 
supervisor) and user access levels with an additional signal for the secure attribute of each memory reference, as shown in Access 
control model levels.
Each level has different access control policies that specify the read and write accessibility for a target. XRDC combines the 
privileged and secure attributes with the DID assigned to each system bus transaction to form the hardware basis for the access 
control mechanism. You specify the ACP for target resources using the DdACP fields (see Domain ACP specification) found in 
the configuration registers shown in Peripheral ACP evaluation registers and Memory ACP evaluation registers.
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
687 / 5251


---
# 페이지 637

You can dynamically control access to shared memory regions and target peripherals with the optional inclusion of a hardware 
semaphore (see Hardware semaphores and dynamic access rights). If you enable this semaphore for a given address space or 
peripheral, XRDC allows writes to the target resource only if the requesting domain owns the semaphore.
For cores that support only the three-state access control model (Secure Privileged, Secure User, Nonsecure User), XRDC forces 
the nonsecure output signal from the MDAC submodule to 0 in privileged mode. This change enables precise state transitions 
between user and privileged modes. Specifically, the MDAC logic for initiator m generates the nonsecure attribute output signal 
as a function of the Three-State Model (PIDm[TSM]) and PID Present (HWCFG2[PIDPm]) fields, as shown in Generation of 
secure attribute).
19.5.6.7.1
Access control model levels
Table 89. Access control model levels
Secure
Nonsecure
Privileged 
(supervisor)
Not privileged 
(user)
Level
Yes
Not applicable
Yes
Not applicable
Most restricted
Yes
Not applicable
Not applicable
Yes
More restricted
Not applicable
Yes
Yes
Not applicable
Less restricted
Not applicable
Yes
Not applicable
Yes
Least restricted
19.5.6.7.2
Generation of secure attribute
This table shows how XRDC generates the secure attribute for a transaction.
Table 90. Generation of secure attribute
Access 
levels 1
PIDm[TSM] 
(b)
PID present 2
Secure attribute determined by
4
0
No
Initiator secure attribute
4
0
Yes
Initiator secure attribute && ~initiator privileged attribute
3
1
No
PIDm[5] && ~initiator privileged attribute
3
1
Yes
Local secure attribute && ~initiator privileged attribute
1. XRDC assumes a core initiator supports the four-level access model. If a core supports only the three-state access control 
model, you must write 1 to PIDm[TSM] before loading any nonsecure value into the PID.
2. Indicated in HWCFG2–3[PIDPm].
19.5.6.8
Domain ACP specification
Table 91. Domain ACP specification
DdACP
Allowable accesses
Secure
Privileged
Secure
User
Nonsecure
Privileged
Nonsecure
User
111b
R, W
R, W
R, W
R, W
110b
R, W
R, W
R, W
None
101b
R, W
R, W
R
R
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
688 / 5251


---
# 페이지 638

Table 91. Domain ACP specification (continued)
DdACP
Allowable accesses
Secure
Privileged
Secure
User
Nonsecure
Privileged
Nonsecure
User
100b
R, W
R, W
R
None
011b
R, W
R, W
None
None
010b
R, W
None
None
None
001b
R
R
None
None
000b
None
None
None
None
19.5.6.9
Memory region ACP evaluation
During ACP evaluation of a memory transaction request, if the target memory location falls within the address range specified 
by any XRDC memory region descriptor, then XRDC identifies the request as a memory region hit. For each memory region 
hit, XRDC compares the DID, privileged attribute, and secured attribute of the transaction to the associated domain ACP 
(MRGD_W{2,3}_r[DdACP]) in the memory region descriptor. See ACP evaluation for additional details on this function.
The following conditions cause XRDC to report an access error:
• The target memory location does not fall within any defined memory regions; in other words, the transaction request is not 
a hit.
• The transaction request does not have the appropriate access permissions for the region, which triggers a domain 
violation.
• The transaction request hits multiple (overlapping) regions, and all of those regions signal access violations.
Unimplemented domain identifiers default to no access privileges, and therefore the access type of a DdACP field for an 
unimplemented domain is read-as-zero/writes-ignored (RAZ/WI).
19.5.6.10
Hardware semaphores and dynamic access rights
XRDC memory region descriptors and peripheral access control support an optional hardware semaphore in their access 
evaluations. This hardware semaphore allows hardware enforcement of dynamic access rights, based on the state of the 
semaphore for shared memory regions or shared peripherals.
If enabled, the state of the semaphore dynamically modifies the access control policies so that only the domain owning it has write 
access to the resource. The write permissions for all other domains are revoked based on the semaphore state. If no domain owns 
the semaphore, the PAC and MRC submodules evaluate DdACP normally.
If you enable a hardware semaphore (by writing 1 to MRGD_W2_r[SE] or PDAC_W0_r[SE]) then, before the normal DdACP 
evaluation, XRDC checks the state of the hardware semaphore specified in MRGD_W2_r[SNUM] or PDAC_W0_r[SNUM].
On a write transaction, if the semaphore is not idle (the semaphore state is non-zero) and the requesting domain does not own the 
semaphore, the memory or peripheral access terminates with an error. In other words, writes into a semaphore-enabled address 
space or peripheral are allowed only if the semaphore is idle or the requesting domain owns the semaphore.
19.5.7 XRDC transaction examples
To see the complete transaction process for an XRDC-protected transaction request from an initiator to target:
1. Follow one of these examples of domain assignment:
• DFMT0 direct domain assignment example
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
689 / 5251


---
# 페이지 639

• DFMT0 PID-based domain assignment example
• DFMT1 direct domain assignment example-single MDA
2. Then follow one of these examples of ACP evaluation:
• Peripheral ACP evaluation example
• Memory ACP evaluation example
19.5.7.1
DFMT0 direct domain assignment example
This configuration assigns a specific domain to all incoming transactions.
• A core initiator has initiator number = 6.
• The core has one MDAC register (MDACFG6[NMDAR] = 1), configured as shown in Register settings for DFMT0 direct 
domain assignment transactions.
MDAC_Ww_m_DFMT0 registers do not include fields for secure and privileged attributes. Those attributes are part of the 
transaction data from core initiators and are forwarded with the transaction after domain assignment.
19.5.7.1.1
Register settings for DFMT0 direct domain assignment transactions
Table 92. Register settings for DFMT0 direct domain assignment transactions
Field
MDA_W0_6_DFMT0
Comments
VLD
1
Enables this register for use in domain assignment.
LK1
1
Locks the settings in this register until the next module reset.
DFMT
0
Indicates that this is a DFMT0 register.
PID
00_0000b
Not used because PE = 00b.
PIDM
00_0000b
Not used because PE = 00b.
PE
00b
Disables PID-based filtering.
DIDS
00b
All incoming transactions are to be assigned to the domain specified by the DID 
field.
DID
001b
Because PE = 00b and DIDS = 00b, all incoming transactions are to be assigned 
DID value 001b.
19.5.7.1.2
DFMT0 direct domain assignment process
The application configures XRDC as it boots. After application boot completes, a core issues a read request to a target peripheral.
1. XRDC intercepts the request and performs domain assignment using the configuration in MDA_W0_6_DFMT0. In this 
example, XRDC assigns DID = 001b to all incoming transactions.
2. The transaction proceeds with DID = 001b and the privileged and secure attributes provided by the core.
19.5.7.2
DFMT0 PID-based domain assignment example
This example configuration demonstrates PID-based domain assignment:
• A core initiator with initiator number = 4 processes both safety-critical tasks and routine tasks, using two domains:
— Domain 0 is reserved for safety-critical tasks (PID = 0–15).
— Domain 1 is reserved for routine tasks (PID > 15).
• The core has eight MDAC registers (MDACFG4[NMDAR] = 8), configured as follows (see Register settings for DFMT0 
PID-based transactions):
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
690 / 5251


---
# 페이지 640

— MDA_W0_4_DFMT0 assigns safety-critical tasks (PID = 0–15) to domain 0.
— MDA_W1_4_DFMT0 assigns routine tasks (PID = 16–31) to domain 1.
— MDA_W2_4_DFMT0 assigns routine tasks (PID = 32–63) to domain 1.
— MDA_W3_4_DFMT0 through MDA_W7_4_DFMT0 are not used.
MDAC_Ww_m_DFMT0 registers do not include fields for secure and privileged attributes. Those attributes are part of the 
transaction data from core initiators and are forwarded with the transaction after domain assignment.
19.5.7.2.1
Register settings for DFMT0 PID-based transactions
Table 93. Register settings for PID-based transactions
Field
Registers
MDA_W0_4_D
FMT0
MDA_W1_4_D
FMT0
MDA_W2_4_D
FMT0
MDA_W[3–
7]_4_DFMT0
Comments
VLD
1
1
1
0
Enables this register for use when assigning 
domains.
LK1
1
1
1
1
Locks the settings in each register until the next 
device reset.
DFMT
0
0
0
0
Indicates that these registers apply to domain 
assignment for core initiators.
PID
00_0000b
01_0000b
10_0000b
—
Constant match value to be used for PID-based 
filtering.
PIDM
00_1111b
10_1111b
01_1111b
—
Each 0 bit causes the corresponding PID bit to 
be considered in domain assignment.
PE
10b
10b
10b
—
Specifies the type of pattern matching used for 
PID evaluation.
DIDS
00b
00b
00b
—
Assign all incoming transactions with PIDs that 
pass the filtering criteria to the domain specified 
by the DID field.
DID
000b
001b
001b
—
This DID value is assigned to incoming 
transactions with PIDs that pass the filtering 
criteria.
19.5.7.2.2
DFMT0 PID-based domain assignment process
The application configures XRDC as it boots. After booting completes, a core issues a read request to a target peripheral. The 
task making the request has PID = 6, indicating that it is a safety-critical task.
1. XRDC intercepts the request and performs domain assignment using each enabled MDA_Wn_4_DFMT0 register, 
regardless of whether it has already found a match. In this example, XRDC performs the domain assignments as shown 
in DFMT0 PID-based domain assignment evaluation.
2. After XRDC completes all domain assignment evaluations, it logically ORs the assigned DIDs to determine the final DID 
assigned to the transaction. In this example, only one evaluation results in a DID assignment, so there is no OR operation.
3. The transaction proceeds with DID 000b and the privilege and secure attributes provided by the core.
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
691 / 5251


---
# 페이지 641

19.5.7.2.3
DFMT0 PID-based domain assignment evaluation
Table 94. DFMT0 PID-based domain assignment evaluation
Register
Evaluation steps
Boolean math
Result
MDA_W0_4_DFMT0
1. Bitwise AND of PID with inverted PIDM.
00_0000b & 11_0000b
00_0000b
2. Bitwise AND of transaction PID (PID4[PID]) 
with inverted PIDM.
000110b & 11_0000b
00_0000b
3. Compare the results of steps 1 and 2.
00_0000b == 000000b
True: Assign DID 0
MDA_W1_4_DFMT0
1. Bitwise AND of PID with inverted PIDM.
01_0000b & 01_0000b
01_0000b
2. Bitwise AND of transaction PID (PID4[PID]) 
with inverted PIDM.
00_0110b & 01_0000b
00_0000b
3. Compare the results of steps 1 and 2.
01_0000b == 00_0000
b
False: No DID 
assignment
MDA_W2_4_DFMT0
1. Bitwise AND of PID with inverted PIDM.
10_0000b & 10_0000b
10_0000b
2. Bitwise AND of transaction PID (PID4[PID]) 
with inverted PIDM.
00_0110b & 10_0000b
00_0000b
3. Compare the results of steps 1 and 2.
10_0000b == 00_0000
b
False: No DID 
assignment
19.5.7.3
DFMT1 direct domain assignment example-single MDA
This configuration assigns a specific domain to all incoming transactions.
• An initiator has initiator number = 6.
• The initiator has one MDAC register (MDACFG6[NMDAR] = 1) as shown in Register settings for DFMT1 direct domain 
assignment transactions.
19.5.7.3.1
Register settings for DFMT1 direct domain assignment transactions
Table 95. Register settings for DFMT1 direct domain assignment transactions
Field
MDA_W0_6_DFMT1
Comments
VLD
1
Enables this register for use in domain assignment.
LK1
1
Locks the settings in this register until the next chip reset.
DFMT
1
Indicates that this is a DFMT1 register.
DIDB
0b
All incoming transactions are to be assigned to the domain that the DID field 
specifies.
SA
10b
All incoming transactions retain their Secure attribute value.
PA
10b
All incoming transactions retain their Privileged attribute value.
DID
001b
Because DIDB = 0b, all incoming transactions are to be assigned DID value 001b.
19.5.7.3.2
DFMT1 direct domain assignment process
The application configures XRDC as it boots. After application boot completes, an initiator issues a read request to a 
target peripheral.
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
692 / 5251


---
# 페이지 642

1. XRDC intercepts the request and assigns a domain using the configuration in MDA_W0_6_DFMT1. In this example, XRDC 
assigns DID = 001b to all incoming transactions.
2. The transaction proceeds with DID = 001b and the privileged and secure attributes provided by the initiator.
19.5.7.4
Peripheral ACP evaluation example
This example configuration demonstrates ACP evaluation for a target peripheral.
• The core initiator must have exclusive access to the ADC0 peripheral for safety-critical tasks in domain 0.
• The core initiator supports 8 domains (HWCFG0[NDID] = 111b).
• ADC occupies PDAC slot 40 in the chip, as defined in an example memory map file (see Finding the PDAC slot number for 
a peripheral).
• Given 8 domains and PDAC slot 40, the PDAC registers associated with ADC0 are PDAC_W0_40 and PDAC_W1_40.
The following sections describe the register configurations for this example.
19.5.7.4.1
Finding the PDAC slot number for a peripheral
This topic shows how to find the PDAC slot number for a peripheral, but it is a generic example. Memory map file organization and 
appearance can vary.
To find the PDAC slot number for a peripheral:
1. Open the memory map file attached to this document and view the peripherals page.
2. Locate the peripheral in the "Instance" column.
3. The PDAC slot number for the peripheral is at the intersection of the "PDAC slot number" column and the peripheral 
row.
In this figure, for peripheral ADC_0, the PDAC slot number is 40. Therefore, the PDAC registers for ADC0 are PDAC_Ww_40.
Figure 50. Finding the PDAC slot number for a peripheral
19.5.7.4.2
Register settings for peripheral ACP evaluation
This table shows the PDAC_Ww_40 settings for a safety-critical task assigned to domain 0.
Table 96. Register settings for peripheral ACP evaluation
Register
Field
Value (b)
Comments
PDAC_W0_40
SE
0
The hardware semaphore (see the SEMA42 chapter) is disabled.
SNUM
(don't care)
The hardware semaphore is not used in this example.
D7ACP
000
Domain 7 has no access to the peripheral.
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
693 / 5251


---
# 페이지 643

Table 96. Register settings for peripheral ACP evaluation (continued)
Register
Field
Value (b)
Comments
D6ACP
000
Domain 6 has no access to the peripheral.
D5ACP
000
Domain 5 has no access to the peripheral.
D4ACP
000
Domain 4 has no access to the peripheral.
D3ACP
000
Domain 3 has no access to the peripheral.
D2ACP
000
Domain 2 has no access to the peripheral.
D1ACP
000
Domain 1 has no access to the peripheral.
D0ACP
010
Only privileged, secure transactions from domain 0 have access.
PDAC_W1_40
VLD
1
Use this register set in domain ACP evaluations.
LK2
11
Lock the settings in this register until the next device reset.
19.5.7.4.3
Peripheral ACP evaluation process
XRDC performs the following process for ACP evaluation:
1. When the application is running, the core issues a read request to a target peripheral. The task making the request has 
PID = 0, indicating that it is a safety-critical task. The transaction request is privileged and secured.
2. Between the chip interconnect and ADC0, XRDC intercepts the request and compares its DID, privileged attribute, and 
secured attribute to the configuration in PDAC_W0_40 and PDAC_W1_40.
3. Because the ADC0 D0ACP field is 010b for privileged, secured access, XRDC grants access to the transaction.
4. The transaction proceeds normally without any further intervention from XRDC.
19.5.7.5
Memory ACP evaluation example
This example configuration demonstrates ACP evaluation for a target memory. Following are the desired features:
• The core initiator must have exclusive access to the memory region for safety-critical tasks in domain 0.
• The target memory is the address range 1B00_0000h–1B00_1FFFh, protected by memory controller 0 (MRC0), for 
example.
• Access to the entire memory range will be controlled by the memory region descriptor defined by MRGD_Ww_0.
• The requested transaction is secure privileged.
With the configuration settings shown in Register settings for memory ACP evaluation, XRDC grants access and the transaction 
proceeds normally. There is no further XRDC intervention.
19.5.7.5.1
Register settings for memory ACP evaluation
Table 97. Register settings for memory ACP evaluation
Register
Field
Value
Comments
MRGD_W0_0
SRTADDR
1B00_0000h
Starting address of the memory region.
MRGD_W1_0
ENDADDR
1B00_1FFFh
Ending address of the memory region.
MRGD_W2_0
SE
0
The hardware semaphore (see the SEMA42 chapter) is disabled.
SNUM
(don't care)
The hardware semaphore is not used in this example.
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
694 / 5251


---
# 페이지 644

Table 97. Register settings for memory ACP evaluation (continued)
Register
Field
Value
Comments
D7ACP
000b
Domain 7 has no access to the peripheral.
D6ACP
000b
Domain 6 has no access to the peripheral.
D5ACP
000b
Domain 5 has no access to the peripheral.
D4ACP
000b
Domain 4 has no access to the peripheral.
D3ACP
000b
Domain 3 has no access to the peripheral.
D2ACP
000b
Domain 2 has no access to the peripheral.
D1ACP
000b
Domain 1 has no access to the peripheral.
D0ACP
010b
Only privileged, secure transactions from domain 0 have access.
MRGD_W3_0
VLD
1
Use this register set in domain ACP evaluations.
LK2
11b
Lock the settings in this register until the next device reset.
19.5.7.5.2
Memory ACP evaluation process
In this example, XRDC performs the following process for ACP evaluation:
1. When the application is running, the core issues a read request to address 1B00_0100h. The transaction request is 
secure privileged.
2. Between the chip interconnect and the memory, XRDC intercepts the request and compares its DID, memory location of 
the address, privileged attribute, and secured attribute to the configuration in MRGD_W0_0, MRGD_W1_0, MRGD_W2_0 
and MRGD_W3_0.
3. Because the address 1B00_0100h is in the memory range 1B00_0000h–1B00_1FFFh and its D0ACP field is 010b for 
privileged, secured access, XRDC grants access to the transaction.
4. The transaction proceeds normally without any no further intervention from XRDC.
19.5.8 Clocking
This module has no clocking considerations.
19.5.9 Interrupts
This module outputs an interrupt signal which can be connected to interrupt controller. Check chip-specific interrupt assignment 
for details. Interrupt is asserted on detection of access violation by any checker, and it remains asserted until DERRLOC registers 
are cleared.
19.6 Initialization information
Out of reset, XRDC is disabled (CR[GVLD] = 0), which allows secure privileged startup code to configure the entire 
programming model.
19.6.1 Initialization procedure
1. Read the hardware configuration registers to obtain the implemented XRDC hardware capabilities for the chip:
• HWCFG0
• HWCFG1
• HWCFG2
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
695 / 5251


---
# 페이지 645

• MDACFGm (one for each supported bus initiator—number indicated in HWCFG0[NMSTR])
• MRCFGc (one for each supported memory controller—number indicated in HWCFG0[NMRC])
2. Use the information retrieved in step 1 and the desired domain architecture to configure:
• Domain assignments (MDA_Ww_m_DFMT0 and MDA_Ww_m_DFMT1)
• Memory region descriptors (MRGD_Ww_n)
• Peripheral access control (PDAC_Ww_s)
Ensure that you enable the necessary registers and register sets using the appropriate VLD fields. Also, you can limit 
access to these registers or lock them after you configure them, by using the appropriate LK1 fields.
3. Enable XRDC (write 1 to CR[GVLD]).
XRDC is now fully operational.
19.6.2 Minimize access errors
When you configure and enable XRDC, it begins generating DIDs for transaction requests and evaluating access rights at the 
target memory and peripheral resources. Because of the distributed design hierarchy and the pipelined nature of the hardware 
system bus fabric, it can take multiple cycles for a generated DID to propagate. Until that happens, XRDC uses the initiator's 
default DID. Depending on the programmed ACPs, the default DID might generate an access error response.
If XRDC generates incorrect error responses, you can use the following approaches to minimize or eliminate these extraneous 
access errors:
• Minimize the amount of system bus traffic when XRDC is enabled (CR[GVLD] = 1).
• Ensure that all target memory addresses provide sufficient access rights for any default DIDs and for the newly programmed 
DIDs. After XRDC is fully operational, as confirmed by a read of HWCFG1, you can remove the permissions for the 
default DIDs.
• Try to have the bus initiator that programs and configures XRDC use the same DID, that is, its default DID, for both initialization 
and configuration, besides normal system operation. You do this when you define the DID assignments for the system.
19.7 Application information
19.7.1 Master domain assignments
The typical use case for master domain assignments is to include one or more core bus initiators in a single domain, possibly 
combined with other noncore bus initiator modules such as DMA. This configuration may be static or may be changed dynamically 
to select between a small number of domains. HWCFG0[NDID] indicates the maximum number of supported domains. XRDC also 
supports the optional use of PIDs to create multiple classes of cores, each in different domains.
For example, you can group critical tasks—safety-critical, performance-critical, and so on—into one domain and all other tasks 
into a second domain. Typically, you assign the DID at initialization, but you can also reconfigure domain assignment while the 
application is running.
A core bus initiator typically has multiple MDA_Ww_m_DFMT0 registers associated with it.
A noncore bus initiator typically has a single MDA_Ww_m_DFMT1 register associated with it.
The master domain assignment, memory region descriptor, and peripheral domain access control registers have lock fields that 
enable you to limit access to, or to lock, the registers. These actions protect the configuration.
19.7.2 Memory region descriptor management
There are two important concepts to consider for managing the memory region descriptors.
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
696 / 5251


---
# 페이지 646

Each MRCc configuration is chip-specific. See the chip-specific XRDC information for the number of implemented memory 
region descriptors (MRGD_Ww_n) in a given MRCc instance, and the specific port numbers associated with the target memories 
being monitored.
Second, as detailed in Memory region ACP evaluation, after you enable the XRDC, a memory reference must hit one or more of 
the configured regions. Otherwise, the transaction results in an access violation. Two other conditions also result in access errors:
• The access hits a single region descriptor and that region signals a domain violation.
• The access hits multiple (overlapping) regions and all regions signal violations.
The second condition reflects that XRDC gives priority to permission granting over access denying for overlapping regions. This 
approach provides more flexibility to system software in memory region descriptor assignments.
19.7.3 Domain error capture management
19.7.3.1
Domain error capture registers
When an MRC or PAC detects a domain access violation, XRDC captures information about the transaction in the 
following registers:
Table 98. Domain error capture registers
Register[field]
Index
Information
DERRLOCd[MRCINST]
d = DID
Domain error location for MRC instances, with asserted bits indicating 
which MRC instance numbers are reporting an error
DERRLOCd[PACINST]
d = DID
Domain error location for PAC instances, with asserted bits indicating 
which PAC instance numbers are reporting an error
DERR_W0_i
i = instance number
Transaction target address
DERR_W1_i
i = instance number
Additional information about the transaction
DERR_W3_i
i = instance number
Reset and rearm domain error capture for the instance
19.7.3.2
Handling domain access violation errors
When an MRC or PAC instance detects a domain access violation, it reports the error by asserting the associated bit in 
DERRLOCd[MRCINST] or [PACINST], and XRDC asserts the error interrupt output. To retrieve information about the error, the 
error handler must:
1. Read each DERRLOCd register until it finds a non-zero MRCINST or PACINST value.
The index of the DERRLOCd register is the DID for the domain in which the error occurred.
2. Configure the domain assignment for the master executing the exception handler (MDA_Ww_m_DFMTf[DID]) to assign 
the DID that corresponds to the DERRLOCd register index, such that the DERR_Ww_i registers show the error for that 
domain.
3. Read HWCFG1[DID] to be sure the error handler is now operating in the correct domain. In other words, make sure 
HWCFG1[DID] equals the value written to MDA_Ww_m_DFMTf[DID].
4. Find the number of an MRC or PAC instance reporting an error by parsing DERRLOCd[MRCINST] and 
DERRLOCd[PACINST] for an asserted bit.
There may be multiple access violations, across multiple MRC or PAC instances, pending for a given domain. To quickly 
find the lowest numbered instance reporting an access violation, execute a "find first one bit" instruction (alternatively known 
as "count leading zeroes") on the MRCINST and PACINST fields.
5. Retrieve the error address (DERR_W0_i[EADDR]).
6. Retrieve the error information (DERR_W1_i).
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
697 / 5251


---
# 페이지 647

More than one error may have occurred in the MRC or PAC instance, as indicated by the error status 
(DERR_W1_i[EST] = 11b). If more than one error has occurred in the instance, XRDC captures data only for the 
first error.
7. Use the error address and information to handle the error (whatever that may require).
8. Reset the DERR_Ww_i registers and rearm error capture (write 1b to DERR_W3_i[RECR]).
Rearming error capture deasserts the instance bit in DERRLOCd.
9. Repeat steps 1 and 8 for each asserted bit in PACINST and MRCINST until there are no more asserted bits.
Domain error retrieval illustrates an example error retrieval.
19.7.3.3
Domain error retrieval
DERRLOCd
0000
0000
0000
1000
0000
0000
0
1
2
3
...
14
15
0000 0000 0000 0000
EADDR
Register
MRC 0
EATR, EDID, EST = 10b, ...
RECR
DERR_W0_0
Instance
DERR_W1_0
DERR_W3_0
EADDR
MRC 1
EATR, EDID, EST = 11b, ...
RECR
DERR_W0_1
DERR_W1_1
DERR_W3_1
EADDR
MCR 2
EATR, EDID, EST = 11b, ...
RECR
DERR_W0_2
DERR_W1_2
DERR_W3_2
EADDR
MRC 3
EATR, EDID, ...
RECR
...
...
DERR_W0_3
DERR_W1_3
DERR_W3_3
EADDR
PAC 2
EATR, EDID, ...
RECR
DERR_W0_18
DERR_W1_18
DERR_W3_18
EADDR
PAC 3
EATR, EDID, EST = 11b, ...
RECR
DERR_W0_19
DERR_W1_19
DERR_W3_19
PACINST
MRCINST
. . .
. . .
0000 0000 0000 0000
0000 0000 0000 0000
0000 0000 0000 0110
0000 0000 0000 0001
0000 0000 0000 0000
Faulting DID
Faulting DID
Field
Figure 51. Domain error retrieval
19.8 Memory map and register definitions
19.8.1 Register organization
XRDC registers are partitioned into these groups:
• Basic hardware control and configuration
• Domain errors (including location and details)
• Master domain assignments
• Peripheral domain access controls
• Memory region descriptors
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
698 / 5251


---
# 페이지 648

19.8.2 Register access guidelines
The following guidelines apply to XRDC register access:
• You can access the XRDC registers only in secure, privileged access mode.
• Unless stated otherwise, the registers support 8-, 16-, and 32-bit reads, and 32-bit writes.
• Unless stated otherwise, XRDC terminates the following access attempts with an error:
— Accesses in a different access mode
— Unsupported write data size
— Writes to read-only resources
— Writes to reserved address spaces
• Accesses to these memory map holes return an error:
— Any access to a register that does not exist
— Holes in the 0–F0h and DERR to PID register space
— For MDAC, gaps in the master domain assignment (MDA_Ww_m_DFMTn) registers
— For MRCs, any gap in the MRGD_Ww_r registers (for example, if there are four memory region descriptors, 
attempted access to a fifth descriptor fails)
• Accesses to these memory map holes do not return a bus error:
— MRCs: Memory region descriptors occupy only four words but have an additional four words of address available: 
words 4–7
— PDAC: Registers associated with unimplemented PDAC slots
• Read accesses to these memory map holes do not return a bus error:
— Offset F8h and FCh
— Offset 100–13Fh
— Offset 140–14Fh
— Offset 200–23Ch
19.8.3 XRDC register descriptions
19.8.3.1
XRDC memory map
XRDC base address: 4027_8000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Control (CR)
32
RW
0000_008Ah
F0h
Hardware Configuration 0 (HWCFG0)
32
R
1205_0904h
F4h
Hardware Configuration 1 (HWCFG1)
32
R
See section
F8h
Hardware Configuration 2 (HWCFG2)
32
R
0000_0000h
100h
Master Domain Assignment Configuration (MDACFG0)
8
R
01h
101h
Master Domain Assignment Configuration (MDACFG1)
8
R
81h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
699 / 5251


---
# 페이지 649

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
102h
Master Domain Assignment Configuration (MDACFG2)
8
R
81h
103h
Master Domain Assignment Configuration (MDACFG3)
8
R
01h
104h
Master Domain Assignment Configuration (MDACFG4)
8
R
01h
105h
Master Domain Assignment Configuration (MDACFG5)
8
R
81h
106h
Master Domain Assignment Configuration (MDACFG6)
8
R
01h
107h
Master Domain Assignment Configuration (MDACFG7)
8
R
81h
108h
Master Domain Assignment Configuration (MDACFG8)
8
R
01h
109h
Master Domain Assignment Configuration (MDACFG9)
8
R
81h
140h
Memory Region Configuration (MRCFG0)
8
R
10h
141h
Memory Region Configuration (MRCFG1)
8
R
10h
142h
Memory Region Configuration (MRCFG2)
8
R
04h
143h
Memory Region Configuration (MRCFG3)
8
R
10h
144h
Memory Region Configuration (MRCFG4)
8
R
04h
145h
Memory Region Configuration (MRCFG5)
8
R
10h
200h - 210h
Domain Error Location (DERRLOC0 - DERRLOC4)
32
R
0000_0000h
400h
Domain Error Word 0 (DERR_W0_0)
32
R
0000_0000h
404h
Domain Error Word 1 (DERR_W1_0)
32
R
0000_0000h
40Ch
Domain Error Word 3 (DERR_W3_0)
32
RW
0000_0000h
410h
Domain Error Word 0 (DERR_W0_1)
32
R
0000_0000h
414h
Domain Error Word 1 (DERR_W1_1)
32
R
0000_0000h
41Ch
Domain Error Word 3 (DERR_W3_1)
32
RW
0000_0000h
420h
Domain Error Word 0 (DERR_W0_2)
32
R
0000_0000h
424h
Domain Error Word 1 (DERR_W1_2)
32
R
0000_0000h
42Ch
Domain Error Word 3 (DERR_W3_2)
32
RW
0000_0000h
430h
Domain Error Word 0 (DERR_W0_3)
32
R
0000_0000h
434h
Domain Error Word 1 (DERR_W1_3)
32
R
0000_0000h
43Ch
Domain Error Word 3 (DERR_W3_3)
32
RW
0000_0000h
440h
Domain Error Word 0 (DERR_W0_4)
32
R
0000_0000h
444h
Domain Error Word 1 (DERR_W1_4)
32
R
0000_0000h
44Ch
Domain Error Word 3 (DERR_W3_4)
32
RW
0000_0000h
450h
Domain Error Word 0 (DERR_W0_5)
32
R
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
700 / 5251


---
# 페이지 650

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
454h
Domain Error Word 1 (DERR_W1_5)
32
R
0000_0000h
45Ch
Domain Error Word 3 (DERR_W3_5)
32
RW
0000_0000h
500h
Domain Error Word 0 (DERR_W0_16)
32
R
0000_0000h
504h
Domain Error Word 1 (DERR_W1_16)
32
R
0000_0000h
50Ch
Domain Error Word 3 (DERR_W3_16)
32
RW
0000_0000h
510h
Domain Error Word 0 (DERR_W0_17)
32
R
0000_0000h
514h
Domain Error Word 1 (DERR_W1_17)
32
R
0000_0000h
51Ch
Domain Error Word 3 (DERR_W3_17)
32
RW
0000_0000h
520h
Domain Error Word 0 (DERR_W0_18)
32
R
0000_0000h
524h
Domain Error Word 1 (DERR_W1_18)
32
R
0000_0000h
52Ch
Domain Error Word 3 (DERR_W3_18)
32
RW
0000_0000h
700h
Process Identifier (PID0)
32
RW
0000_0000h
70Ch
Process Identifier (PID3)
32
RW
0000_0000h
710h
Process Identifier (PID4)
32
RW
0000_0000h
718h
Process Identifier (PID6)
32
RW
0000_0000h
720h
Process Identifier (PID8)
32
RW
0000_0000h
800h
Master Domain Assignment (MDA_W0_0_DFMT0)
32
RW
0000_0000h
820h
Master Domain Assignment (MDA_W0_1_DFMT1)
32
RW
2000_0000h
840h
Master Domain Assignment (MDA_W0_2_DFMT1)
32
RW
2000_0000h
860h
Master Domain Assignment (MDA_W0_3_DFMT0)
32
RW
0000_0000h
880h
Master Domain Assignment (MDA_W0_4_DFMT0)
32
RW
0000_0000h
8A0h
Master Domain Assignment (MDA_W0_5_DFMT1)
32
RW
2000_0000h
8C0h
Master Domain Assignment (MDA_W0_6_DFMT0)
32
RW
0000_0000h
8E0h
Master Domain Assignment (MDA_W0_7_DFMT1)
32
RW
2000_0000h
900h
Master Domain Assignment (MDA_W0_8_DFMT0)
32
RW
0000_0000h
920h
Master Domain Assignment (MDA_W0_9_DFMT1)
32
RW
2000_0000h
1010h
Peripheral Domain Access Control Word 0 (PDAC_W0_2)
32
RW
0000_0000h
1014h
Peripheral Domain Access Control Word 1 (PDAC_W1_2)
32
RW
0000_0000h
1018h
Peripheral Domain Access Control Word 0 (PDAC_W0_3)
32
RW
0000_0000h
101Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_3)
32
RW
0000_0000h
10E0h
Peripheral Domain Access Control Word 0 (PDAC_W0_28)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
701 / 5251


---
# 페이지 651

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
10E4h
Peripheral Domain Access Control Word 1 (PDAC_W1_28)
32
RW
0000_0000h
1100h
Peripheral Domain Access Control Word 0 (PDAC_W0_32)
32
RW
0000_0000h
1104h
Peripheral Domain Access Control Word 1 (PDAC_W1_32)
32
RW
0000_0000h
1108h
Peripheral Domain Access Control Word 0 (PDAC_W0_33)
32
RW
0000_0000h
110Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_33)
32
RW
0000_0000h
1110h
Peripheral Domain Access Control Word 0 (PDAC_W0_34)
32
RW
0000_0000h
1114h
Peripheral Domain Access Control Word 1 (PDAC_W1_34)
32
RW
0000_0000h
1118h
Peripheral Domain Access Control Word 0 (PDAC_W0_35)
32
RW
0000_0000h
111Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_35)
32
RW
0000_0000h
1120h
Peripheral Domain Access Control Word 0 (PDAC_W0_36)
32
RW
0000_0000h
1124h
Peripheral Domain Access Control Word 1 (PDAC_W1_36)
32
RW
0000_0000h
1130h
Peripheral Domain Access Control Word 0 (PDAC_W0_38)
32
RW
0000_0000h
1134h
Peripheral Domain Access Control Word 1 (PDAC_W1_38)
32
RW
0000_0000h
1138h
Peripheral Domain Access Control Word 0 (PDAC_W0_39)
32
RW
0000_0000h
113Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_39)
32
RW
0000_0000h
1140h
Peripheral Domain Access Control Word 0 (PDAC_W0_40)
32
RW
0000_0000h
1144h
Peripheral Domain Access Control Word 1 (PDAC_W1_40)
32
RW
0000_0000h
1148h
Peripheral Domain Access Control Word 0 (PDAC_W0_41)
32
RW
0000_0000h
114Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_41)
32
RW
0000_0000h
1150h
Peripheral Domain Access Control Word 0 (PDAC_W0_42)
32
RW
0000_0000h
1154h
Peripheral Domain Access Control Word 1 (PDAC_W1_42)
32
RW
0000_0000h
1160h
Peripheral Domain Access Control Word 0 (PDAC_W0_44)
32
RW
0000_0000h
1164h
Peripheral Domain Access Control Word 1 (PDAC_W1_44)
32
RW
0000_0000h
1168h
Peripheral Domain Access Control Word 0 (PDAC_W0_45)
32
RW
0000_0000h
116Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_45)
32
RW
0000_0000h
1170h
Peripheral Domain Access Control Word 0 (PDAC_W0_46)
32
RW
0000_0000h
1174h
Peripheral Domain Access Control Word 1 (PDAC_W1_46)
32
RW
0000_0000h
1178h
Peripheral Domain Access Control Word 0 (PDAC_W0_47)
32
RW
0000_0000h
117Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_47)
32
RW
0000_0000h
1188h
Peripheral Domain Access Control Word 0 (PDAC_W0_49)
32
RW
0000_0000h
118Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_49)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
702 / 5251


---
# 페이지 652

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1190h
Peripheral Domain Access Control Word 0 (PDAC_W0_50)
32
RW
0000_0000h
1194h
Peripheral Domain Access Control Word 1 (PDAC_W1_50)
32
RW
0000_0000h
1198h
Peripheral Domain Access Control Word 0 (PDAC_W0_51)
32
RW
0000_0000h
119Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_51)
32
RW
0000_0000h
11A0h
Peripheral Domain Access Control Word 0 (PDAC_W0_52)
32
RW
0000_0000h
11A4h
Peripheral Domain Access Control Word 1 (PDAC_W1_52)
32
RW
0000_0000h
1400h
Peripheral Domain Access Control Word 0 (PDAC_W0_128)
32
RW
0000_0000h
1404h
Peripheral Domain Access Control Word 1 (PDAC_W1_128)
32
RW
0000_0000h
1408h
Peripheral Domain Access Control Word 0 (PDAC_W0_129)
32
RW
0000_0000h
140Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_129)
32
RW
0000_0000h
1410h
Peripheral Domain Access Control Word 0 (PDAC_W0_130)
32
RW
0000_0000h
1414h
Peripheral Domain Access Control Word 1 (PDAC_W1_130)
32
RW
0000_0000h
1418h
Peripheral Domain Access Control Word 0 (PDAC_W0_131)
32
RW
0000_0000h
141Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_131)
32
RW
0000_0000h
1420h
Peripheral Domain Access Control Word 0 (PDAC_W0_132)
32
RW
0000_0000h
1424h
Peripheral Domain Access Control Word 1 (PDAC_W1_132)
32
RW
0000_0000h
1428h
Peripheral Domain Access Control Word 0 (PDAC_W0_133)
32
RW
0000_0000h
142Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_133)
32
RW
0000_0000h
1430h
Peripheral Domain Access Control Word 0 (PDAC_W0_134)
32
RW
0000_0000h
1434h
Peripheral Domain Access Control Word 1 (PDAC_W1_134)
32
RW
0000_0000h
1438h
Peripheral Domain Access Control Word 0 (PDAC_W0_135)
32
RW
0000_0000h
143Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_135)
32
RW
0000_0000h
1440h
Peripheral Domain Access Control Word 0 (PDAC_W0_136)
32
RW
0000_0000h
1444h
Peripheral Domain Access Control Word 1 (PDAC_W1_136)
32
RW
0000_0000h
1448h
Peripheral Domain Access Control Word 0 (PDAC_W0_137)
32
RW
0000_0000h
144Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_137)
32
RW
0000_0000h
1450h
Peripheral Domain Access Control Word 0 (PDAC_W0_138)
32
RW
0000_0000h
1454h
Peripheral Domain Access Control Word 1 (PDAC_W1_138)
32
RW
0000_0000h
1458h
Peripheral Domain Access Control Word 0 (PDAC_W0_139)
32
RW
0000_0000h
145Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_139)
32
RW
0000_0000h
1460h
Peripheral Domain Access Control Word 0 (PDAC_W0_140)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
703 / 5251


---
# 페이지 653

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1464h
Peripheral Domain Access Control Word 1 (PDAC_W1_140)
32
RW
0000_0000h
1468h
Peripheral Domain Access Control Word 0 (PDAC_W0_141)
32
RW
0000_0000h
146Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_141)
32
RW
0000_0000h
1470h
Peripheral Domain Access Control Word 0 (PDAC_W0_142)
32
RW
0000_0000h
1474h
Peripheral Domain Access Control Word 1 (PDAC_W1_142)
32
RW
0000_0000h
1478h
Peripheral Domain Access Control Word 0 (PDAC_W0_143)
32
RW
0000_0000h
147Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_143)
32
RW
0000_0000h
1480h
Peripheral Domain Access Control Word 0 (PDAC_W0_144)
32
RW
0000_0000h
1484h
Peripheral Domain Access Control Word 1 (PDAC_W1_144)
32
RW
0000_0000h
1488h
Peripheral Domain Access Control Word 0 (PDAC_W0_145)
32
RW
0000_0000h
148Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_145)
32
RW
0000_0000h
1490h
Peripheral Domain Access Control Word 0 (PDAC_W0_146)
32
RW
0000_0000h
1494h
Peripheral Domain Access Control Word 1 (PDAC_W1_146)
32
RW
0000_0000h
1498h
Peripheral Domain Access Control Word 0 (PDAC_W0_147)
32
RW
0000_0000h
149Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_147)
32
RW
0000_0000h
14A0h
Peripheral Domain Access Control Word 0 (PDAC_W0_148)
32
RW
0000_0000h
14A4h
Peripheral Domain Access Control Word 1 (PDAC_W1_148)
32
RW
0000_0000h
14A8h
Peripheral Domain Access Control Word 0 (PDAC_W0_149)
32
RW
0000_0000h
14ACh
Peripheral Domain Access Control Word 1 (PDAC_W1_149)
32
RW
0000_0000h
14B8h
Peripheral Domain Access Control Word 0 (PDAC_W0_151)
32
RW
0000_0000h
14BCh
Peripheral Domain Access Control Word 1 (PDAC_W1_151)
32
RW
0000_0000h
14C0h
Peripheral Domain Access Control Word 0 (PDAC_W0_152)
32
RW
0000_0000h
14C4h
Peripheral Domain Access Control Word 1 (PDAC_W1_152)
32
RW
0000_0000h
14C8h
Peripheral Domain Access Control Word 0 (PDAC_W0_153)
32
RW
0000_0000h
14CCh
Peripheral Domain Access Control Word 1 (PDAC_W1_153)
32
RW
0000_0000h
14D0h
Peripheral Domain Access Control Word 0 (PDAC_W0_154)
32
RW
0000_0000h
14D4h
Peripheral Domain Access Control Word 1 (PDAC_W1_154)
32
RW
0000_0000h
14D8h
Peripheral Domain Access Control Word 0 (PDAC_W0_155)
32
RW
0000_0000h
14DCh
Peripheral Domain Access Control Word 1 (PDAC_W1_155)
32
RW
0000_0000h
14E0h
Peripheral Domain Access Control Word 0 (PDAC_W0_156)
32
RW
0000_0000h
14E4h
Peripheral Domain Access Control Word 1 (PDAC_W1_156)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
704 / 5251


---
# 페이지 654

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
14E8h
Peripheral Domain Access Control Word 0 (PDAC_W0_157)
32
RW
0000_0000h
14ECh
Peripheral Domain Access Control Word 1 (PDAC_W1_157)
32
RW
0000_0000h
14F0h
Peripheral Domain Access Control Word 0 (PDAC_W0_158)
32
RW
0000_0000h
14F4h
Peripheral Domain Access Control Word 1 (PDAC_W1_158)
32
RW
0000_0000h
14F8h
Peripheral Domain Access Control Word 0 (PDAC_W0_159)
32
RW
0000_0000h
14FCh
Peripheral Domain Access Control Word 1 (PDAC_W1_159)
32
RW
0000_0000h
1500h
Peripheral Domain Access Control Word 0 (PDAC_W0_160)
32
RW
0000_0000h
1504h
Peripheral Domain Access Control Word 1 (PDAC_W1_160)
32
RW
0000_0000h
1508h
Peripheral Domain Access Control Word 0 (PDAC_W0_161)
32
RW
0000_0000h
150Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_161)
32
RW
0000_0000h
1510h
Peripheral Domain Access Control Word 0 (PDAC_W0_162)
32
RW
0000_0000h
1514h
Peripheral Domain Access Control Word 1 (PDAC_W1_162)
32
RW
0000_0000h
1518h
Peripheral Domain Access Control Word 0 (PDAC_W0_163)
32
RW
0000_0000h
151Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_163)
32
RW
0000_0000h
1520h
Peripheral Domain Access Control Word 0 (PDAC_W0_164)
32
RW
0000_0000h
1524h
Peripheral Domain Access Control Word 1 (PDAC_W1_164)
32
RW
0000_0000h
1528h
Peripheral Domain Access Control Word 0 (PDAC_W0_165)
32
RW
0000_0000h
152Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_165)
32
RW
0000_0000h
1530h
Peripheral Domain Access Control Word 0 (PDAC_W0_166)
32
RW
0000_0000h
1534h
Peripheral Domain Access Control Word 1 (PDAC_W1_166)
32
RW
0000_0000h
1538h
Peripheral Domain Access Control Word 0 (PDAC_W0_167)
32
RW
0000_0000h
153Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_167)
32
RW
0000_0000h
1540h
Peripheral Domain Access Control Word 0 (PDAC_W0_168)
32
RW
0000_0000h
1544h
Peripheral Domain Access Control Word 1 (PDAC_W1_168)
32
RW
0000_0000h
1548h
Peripheral Domain Access Control Word 0 (PDAC_W0_169)
32
RW
0000_0000h
154Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_169)
32
RW
0000_0000h
1550h
Peripheral Domain Access Control Word 0 (PDAC_W0_170)
32
RW
0000_0000h
1554h
Peripheral Domain Access Control Word 1 (PDAC_W1_170)
32
RW
0000_0000h
1558h
Peripheral Domain Access Control Word 0 (PDAC_W0_171)
32
RW
0000_0000h
155Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_171)
32
RW
0000_0000h
1568h
Peripheral Domain Access Control Word 0 (PDAC_W0_173)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
705 / 5251


---
# 페이지 655

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
156Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_173)
32
RW
0000_0000h
1578h
Peripheral Domain Access Control Word 0 (PDAC_W0_175)
32
RW
0000_0000h
157Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_175)
32
RW
0000_0000h
1588h
Peripheral Domain Access Control Word 0 (PDAC_W0_177)
32
RW
0000_0000h
158Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_177)
32
RW
0000_0000h
1590h
Peripheral Domain Access Control Word 0 (PDAC_W0_178)
32
RW
0000_0000h
1594h
Peripheral Domain Access Control Word 1 (PDAC_W1_178)
32
RW
0000_0000h
1598h
Peripheral Domain Access Control Word 0 (PDAC_W0_179)
32
RW
0000_0000h
159Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_179)
32
RW
0000_0000h
15A0h
Peripheral Domain Access Control Word 0 (PDAC_W0_180)
32
RW
0000_0000h
15A4h
Peripheral Domain Access Control Word 1 (PDAC_W1_180)
32
RW
0000_0000h
15A8h
Peripheral Domain Access Control Word 0 (PDAC_W0_181)
32
RW
0000_0000h
15ACh
Peripheral Domain Access Control Word 1 (PDAC_W1_181)
32
RW
0000_0000h
15B0h
Peripheral Domain Access Control Word 0 (PDAC_W0_182)
32
RW
0000_0000h
15B4h
Peripheral Domain Access Control Word 1 (PDAC_W1_182)
32
RW
0000_0000h
15B8h
Peripheral Domain Access Control Word 0 (PDAC_W0_183)
32
RW
0000_0000h
15BCh
Peripheral Domain Access Control Word 1 (PDAC_W1_183)
32
RW
0000_0000h
15C0h
Peripheral Domain Access Control Word 0 (PDAC_W0_184)
32
RW
0000_0000h
15C4h
Peripheral Domain Access Control Word 1 (PDAC_W1_184)
32
RW
0000_0000h
15C8h
Peripheral Domain Access Control Word 0 (PDAC_W0_185)
32
RW
0000_0000h
15CCh
Peripheral Domain Access Control Word 1 (PDAC_W1_185)
32
RW
0000_0000h
15D0h
Peripheral Domain Access Control Word 0 (PDAC_W0_186)
32
RW
0000_0000h
15D4h
Peripheral Domain Access Control Word 1 (PDAC_W1_186)
32
RW
0000_0000h
15D8h
Peripheral Domain Access Control Word 0 (PDAC_W0_187)
32
RW
0000_0000h
15DCh
Peripheral Domain Access Control Word 1 (PDAC_W1_187)
32
RW
0000_0000h
15E0h
Peripheral Domain Access Control Word 0 (PDAC_W0_188)
32
RW
0000_0000h
15E4h
Peripheral Domain Access Control Word 1 (PDAC_W1_188)
32
RW
0000_0000h
15E8h
Peripheral Domain Access Control Word 0 (PDAC_W0_189)
32
RW
0000_0000h
15ECh
Peripheral Domain Access Control Word 1 (PDAC_W1_189)
32
RW
0000_0000h
15F0h
Peripheral Domain Access Control Word 0 (PDAC_W0_190)
32
RW
0000_0000h
15F4h
Peripheral Domain Access Control Word 1 (PDAC_W1_190)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
706 / 5251


---
# 페이지 656

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
15F8h
Peripheral Domain Access Control Word 0 (PDAC_W0_191)
32
RW
0000_0000h
15FCh
Peripheral Domain Access Control Word 1 (PDAC_W1_191)
32
RW
0000_0000h
1600h
Peripheral Domain Access Control Word 0 (PDAC_W0_192)
32
RW
0000_0000h
1604h
Peripheral Domain Access Control Word 1 (PDAC_W1_192)
32
RW
0000_0000h
1608h
Peripheral Domain Access Control Word 0 (PDAC_W0_193)
32
RW
0000_0000h
160Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_193)
32
RW
0000_0000h
1610h
Peripheral Domain Access Control Word 0 (PDAC_W0_194)
32
RW
0000_0000h
1614h
Peripheral Domain Access Control Word 1 (PDAC_W1_194)
32
RW
0000_0000h
1618h
Peripheral Domain Access Control Word 0 (PDAC_W0_195)
32
RW
0000_0000h
161Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_195)
32
RW
0000_0000h
1620h
Peripheral Domain Access Control Word 0 (PDAC_W0_196)
32
RW
0000_0000h
1624h
Peripheral Domain Access Control Word 1 (PDAC_W1_196)
32
RW
0000_0000h
1628h
Peripheral Domain Access Control Word 0 (PDAC_W0_197)
32
RW
0000_0000h
162Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_197)
32
RW
0000_0000h
1630h
Peripheral Domain Access Control Word 0 (PDAC_W0_198)
32
RW
0000_0000h
1634h
Peripheral Domain Access Control Word 1 (PDAC_W1_198)
32
RW
0000_0000h
1638h
Peripheral Domain Access Control Word 0 (PDAC_W0_199)
32
RW
0000_0000h
163Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_199)
32
RW
0000_0000h
1640h
Peripheral Domain Access Control Word 0 (PDAC_W0_200)
32
RW
0000_0000h
1644h
Peripheral Domain Access Control Word 1 (PDAC_W1_200)
32
RW
0000_0000h
1648h
Peripheral Domain Access Control Word 0 (PDAC_W0_201)
32
RW
0000_0000h
164Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_201)
32
RW
0000_0000h
1650h
Peripheral Domain Access Control Word 0 (PDAC_W0_202)
32
RW
0000_0000h
1654h
Peripheral Domain Access Control Word 1 (PDAC_W1_202)
32
RW
0000_0000h
1658h
Peripheral Domain Access Control Word 0 (PDAC_W0_203)
32
RW
0000_0000h
165Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_203)
32
RW
0000_0000h
1660h
Peripheral Domain Access Control Word 0 (PDAC_W0_204)
32
RW
0000_0000h
1664h
Peripheral Domain Access Control Word 1 (PDAC_W1_204)
32
RW
0000_0000h
1668h
Peripheral Domain Access Control Word 0 (PDAC_W0_205)
32
RW
0000_0000h
166Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_205)
32
RW
0000_0000h
1670h
Peripheral Domain Access Control Word 0 (PDAC_W0_206)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
707 / 5251


---
# 페이지 657

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1674h
Peripheral Domain Access Control Word 1 (PDAC_W1_206)
32
RW
0000_0000h
1678h
Peripheral Domain Access Control Word 0 (PDAC_W0_207)
32
RW
0000_0000h
167Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_207)
32
RW
0000_0000h
1680h
Peripheral Domain Access Control Word 0 (PDAC_W0_208)
32
RW
0000_0000h
1684h
Peripheral Domain Access Control Word 1 (PDAC_W1_208)
32
RW
0000_0000h
1688h
Peripheral Domain Access Control Word 0 (PDAC_W0_209)
32
RW
0000_0000h
168Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_209)
32
RW
0000_0000h
1690h
Peripheral Domain Access Control Word 0 (PDAC_W0_210)
32
RW
0000_0000h
1694h
Peripheral Domain Access Control Word 1 (PDAC_W1_210)
32
RW
0000_0000h
1698h
Peripheral Domain Access Control Word 0 (PDAC_W0_211)
32
RW
0000_0000h
169Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_211)
32
RW
0000_0000h
16A0h
Peripheral Domain Access Control Word 0 (PDAC_W0_212)
32
RW
0000_0000h
16A4h
Peripheral Domain Access Control Word 1 (PDAC_W1_212)
32
RW
0000_0000h
16A8h
Peripheral Domain Access Control Word 0 (PDAC_W0_213)
32
RW
0000_0000h
16ACh
Peripheral Domain Access Control Word 1 (PDAC_W1_213)
32
RW
0000_0000h
16B0h
Peripheral Domain Access Control Word 0 (PDAC_W0_214)
32
RW
0000_0000h
16B4h
Peripheral Domain Access Control Word 1 (PDAC_W1_214)
32
RW
0000_0000h
16B8h
Peripheral Domain Access Control Word 0 (PDAC_W0_215)
32
RW
0000_0000h
16BCh
Peripheral Domain Access Control Word 1 (PDAC_W1_215)
32
RW
0000_0000h
16C0h
Peripheral Domain Access Control Word 0 (PDAC_W0_216)
32
RW
0000_0000h
16C4h
Peripheral Domain Access Control Word 1 (PDAC_W1_216)
32
RW
0000_0000h
16C8h
Peripheral Domain Access Control Word 0 (PDAC_W0_217)
32
RW
0000_0000h
16CCh
Peripheral Domain Access Control Word 1 (PDAC_W1_217)
32
RW
0000_0000h
16D8h
Peripheral Domain Access Control Word 0 (PDAC_W0_219)
32
RW
0000_0000h
16DCh
Peripheral Domain Access Control Word 1 (PDAC_W1_219)
32
RW
0000_0000h
16E0h
Peripheral Domain Access Control Word 0 (PDAC_W0_220)
32
RW
0000_0000h
16E4h
Peripheral Domain Access Control Word 1 (PDAC_W1_220)
32
RW
0000_0000h
16E8h
Peripheral Domain Access Control Word 0 (PDAC_W0_221)
32
RW
0000_0000h
16ECh
Peripheral Domain Access Control Word 1 (PDAC_W1_221)
32
RW
0000_0000h
16F8h
Peripheral Domain Access Control Word 0 (PDAC_W0_223)
32
RW
0000_0000h
16FCh
Peripheral Domain Access Control Word 1 (PDAC_W1_223)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
708 / 5251


---
# 페이지 658

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1700h
Peripheral Domain Access Control Word 0 (PDAC_W0_224)
32
RW
0000_0000h
1704h
Peripheral Domain Access Control Word 1 (PDAC_W1_224)
32
RW
0000_0000h
1708h
Peripheral Domain Access Control Word 0 (PDAC_W0_225)
32
RW
0000_0000h
170Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_225)
32
RW
0000_0000h
1710h
Peripheral Domain Access Control Word 0 (PDAC_W0_226)
32
RW
0000_0000h
1714h
Peripheral Domain Access Control Word 1 (PDAC_W1_226)
32
RW
0000_0000h
1718h
Peripheral Domain Access Control Word 0 (PDAC_W0_227)
32
RW
0000_0000h
171Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_227)
32
RW
0000_0000h
1728h
Peripheral Domain Access Control Word 0 (PDAC_W0_229)
32
RW
0000_0000h
172Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_229)
32
RW
0000_0000h
1730h
Peripheral Domain Access Control Word 0 (PDAC_W0_230)
32
RW
0000_0000h
1734h
Peripheral Domain Access Control Word 1 (PDAC_W1_230)
32
RW
0000_0000h
1738h
Peripheral Domain Access Control Word 0 (PDAC_W0_231)
32
RW
0000_0000h
173Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_231)
32
RW
0000_0000h
1740h
Peripheral Domain Access Control Word 0 (PDAC_W0_232)
32
RW
0000_0000h
1744h
Peripheral Domain Access Control Word 1 (PDAC_W1_232)
32
RW
0000_0000h
1748h
Peripheral Domain Access Control Word 0 (PDAC_W0_233)
32
RW
0000_0000h
174Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_233)
32
RW
0000_0000h
1750h
Peripheral Domain Access Control Word 0 (PDAC_W0_234)
32
RW
0000_0000h
1754h
Peripheral Domain Access Control Word 1 (PDAC_W1_234)
32
RW
0000_0000h
1758h
Peripheral Domain Access Control Word 0 (PDAC_W0_235)
32
RW
0000_0000h
175Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_235)
32
RW
0000_0000h
1760h
Peripheral Domain Access Control Word 0 (PDAC_W0_236)
32
RW
0000_0000h
1764h
Peripheral Domain Access Control Word 1 (PDAC_W1_236)
32
RW
0000_0000h
1770h
Peripheral Domain Access Control Word 0 (PDAC_W0_238)
32
RW
0000_0000h
1774h
Peripheral Domain Access Control Word 1 (PDAC_W1_238)
32
RW
0000_0000h
1780h
Peripheral Domain Access Control Word 0 (PDAC_W0_240)
32
RW
0000_0000h
1784h
Peripheral Domain Access Control Word 1 (PDAC_W1_240)
32
RW
0000_0000h
1788h
Peripheral Domain Access Control Word 0 (PDAC_W0_241)
32
RW
0000_0000h
178Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_241)
32
RW
0000_0000h
1790h
Peripheral Domain Access Control Word 0 (PDAC_W0_242)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
709 / 5251


---
# 페이지 659

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1794h
Peripheral Domain Access Control Word 1 (PDAC_W1_242)
32
RW
0000_0000h
1798h
Peripheral Domain Access Control Word 0 (PDAC_W0_243)
32
RW
0000_0000h
179Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_243)
32
RW
0000_0000h
17A0h
Peripheral Domain Access Control Word 0 (PDAC_W0_244)
32
RW
0000_0000h
17A4h
Peripheral Domain Access Control Word 1 (PDAC_W1_244)
32
RW
0000_0000h
17A8h
Peripheral Domain Access Control Word 0 (PDAC_W0_245)
32
RW
0000_0000h
17ACh
Peripheral Domain Access Control Word 1 (PDAC_W1_245)
32
RW
0000_0000h
17B0h
Peripheral Domain Access Control Word 0 (PDAC_W0_246)
32
RW
0000_0000h
17B4h
Peripheral Domain Access Control Word 1 (PDAC_W1_246)
32
RW
0000_0000h
17B8h
Peripheral Domain Access Control Word 0 (PDAC_W0_247)
32
RW
0000_0000h
17BCh
Peripheral Domain Access Control Word 1 (PDAC_W1_247)
32
RW
0000_0000h
17C0h
Peripheral Domain Access Control Word 0 (PDAC_W0_248)
32
RW
0000_0000h
17C4h
Peripheral Domain Access Control Word 1 (PDAC_W1_248)
32
RW
0000_0000h
17C8h
Peripheral Domain Access Control Word 0 (PDAC_W0_249)
32
RW
0000_0000h
17CCh
Peripheral Domain Access Control Word 1 (PDAC_W1_249)
32
RW
0000_0000h
17D0h
Peripheral Domain Access Control Word 0 (PDAC_W0_250)
32
RW
0000_0000h
17D4h
Peripheral Domain Access Control Word 1 (PDAC_W1_250)
32
RW
0000_0000h
17D8h
Peripheral Domain Access Control Word 0 (PDAC_W0_251)
32
RW
0000_0000h
17DCh
Peripheral Domain Access Control Word 1 (PDAC_W1_251)
32
RW
0000_0000h
17E0h
Peripheral Domain Access Control Word 0 (PDAC_W0_252)
32
RW
0000_0000h
17E4h
Peripheral Domain Access Control Word 1 (PDAC_W1_252)
32
RW
0000_0000h
17E8h
Peripheral Domain Access Control Word 0 (PDAC_W0_253)
32
RW
0000_0000h
17ECh
Peripheral Domain Access Control Word 1 (PDAC_W1_253)
32
RW
0000_0000h
17F0h
Peripheral Domain Access Control Word 0 (PDAC_W0_254)
32
RW
0000_0000h
17F4h
Peripheral Domain Access Control Word 1 (PDAC_W1_254)
32
RW
0000_0000h
17F8h
Peripheral Domain Access Control Word 0 (PDAC_W0_255)
32
RW
0000_0000h
17FCh
Peripheral Domain Access Control Word 1 (PDAC_W1_255)
32
RW
0000_0000h
1800h
Peripheral Domain Access Control Word 0 (PDAC_W0_256)
32
RW
0000_0000h
1804h
Peripheral Domain Access Control Word 1 (PDAC_W1_256)
32
RW
0000_0000h
1808h
Peripheral Domain Access Control Word 0 (PDAC_W0_257)
32
RW
0000_0000h
180Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_257)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
710 / 5251


---
# 페이지 660

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1810h
Peripheral Domain Access Control Word 0 (PDAC_W0_258)
32
RW
0000_0000h
1814h
Peripheral Domain Access Control Word 1 (PDAC_W1_258)
32
RW
0000_0000h
1818h
Peripheral Domain Access Control Word 0 (PDAC_W0_259)
32
RW
0000_0000h
181Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_259)
32
RW
0000_0000h
1820h
Peripheral Domain Access Control Word 0 (PDAC_W0_260)
32
RW
0000_0000h
1824h
Peripheral Domain Access Control Word 1 (PDAC_W1_260)
32
RW
0000_0000h
1828h
Peripheral Domain Access Control Word 0 (PDAC_W0_261)
32
RW
0000_0000h
182Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_261)
32
RW
0000_0000h
1830h
Peripheral Domain Access Control Word 0 (PDAC_W0_262)
32
RW
0000_0000h
1834h
Peripheral Domain Access Control Word 1 (PDAC_W1_262)
32
RW
0000_0000h
1838h
Peripheral Domain Access Control Word 0 (PDAC_W0_263)
32
RW
0000_0000h
183Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_263)
32
RW
0000_0000h
1840h
Peripheral Domain Access Control Word 0 (PDAC_W0_264)
32
RW
0000_0000h
1844h
Peripheral Domain Access Control Word 1 (PDAC_W1_264)
32
RW
0000_0000h
1848h
Peripheral Domain Access Control Word 0 (PDAC_W0_265)
32
RW
0000_0000h
184Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_265)
32
RW
0000_0000h
1850h
Peripheral Domain Access Control Word 0 (PDAC_W0_266)
32
RW
0000_0000h
1854h
Peripheral Domain Access Control Word 1 (PDAC_W1_266)
32
RW
0000_0000h
1858h
Peripheral Domain Access Control Word 0 (PDAC_W0_267)
32
RW
0000_0000h
185Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_267)
32
RW
0000_0000h
1860h
Peripheral Domain Access Control Word 0 (PDAC_W0_268)
32
RW
0000_0000h
1864h
Peripheral Domain Access Control Word 1 (PDAC_W1_268)
32
RW
0000_0000h
1868h
Peripheral Domain Access Control Word 0 (PDAC_W0_269)
32
RW
0000_0000h
186Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_269)
32
RW
0000_0000h
1870h
Peripheral Domain Access Control Word 0 (PDAC_W0_270)
32
RW
0000_0000h
1874h
Peripheral Domain Access Control Word 1 (PDAC_W1_270)
32
RW
0000_0000h
1878h
Peripheral Domain Access Control Word 0 (PDAC_W0_271)
32
RW
0000_0000h
187Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_271)
32
RW
0000_0000h
1880h
Peripheral Domain Access Control Word 0 (PDAC_W0_272)
32
RW
0000_0000h
1884h
Peripheral Domain Access Control Word 1 (PDAC_W1_272)
32
RW
0000_0000h
1888h
Peripheral Domain Access Control Word 0 (PDAC_W0_273)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
711 / 5251


---
# 페이지 661

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
188Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_273)
32
RW
0000_0000h
1890h
Peripheral Domain Access Control Word 0 (PDAC_W0_274)
32
RW
0000_0000h
1894h
Peripheral Domain Access Control Word 1 (PDAC_W1_274)
32
RW
0000_0000h
1898h
Peripheral Domain Access Control Word 0 (PDAC_W0_275)
32
RW
0000_0000h
189Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_275)
32
RW
0000_0000h
18A0h
Peripheral Domain Access Control Word 0 (PDAC_W0_276)
32
RW
0000_0000h
18A4h
Peripheral Domain Access Control Word 1 (PDAC_W1_276)
32
RW
0000_0000h
18A8h
Peripheral Domain Access Control Word 0 (PDAC_W0_277)
32
RW
0000_0000h
18ACh
Peripheral Domain Access Control Word 1 (PDAC_W1_277)
32
RW
0000_0000h
18B0h
Peripheral Domain Access Control Word 0 (PDAC_W0_278)
32
RW
0000_0000h
18B4h
Peripheral Domain Access Control Word 1 (PDAC_W1_278)
32
RW
0000_0000h
18B8h
Peripheral Domain Access Control Word 0 (PDAC_W0_279)
32
RW
0000_0000h
18BCh
Peripheral Domain Access Control Word 1 (PDAC_W1_279)
32
RW
0000_0000h
18C0h
Peripheral Domain Access Control Word 0 (PDAC_W0_280)
32
RW
0000_0000h
18C4h
Peripheral Domain Access Control Word 1 (PDAC_W1_280)
32
RW
0000_0000h
18C8h
Peripheral Domain Access Control Word 0 (PDAC_W0_281)
32
RW
0000_0000h
18CCh
Peripheral Domain Access Control Word 1 (PDAC_W1_281)
32
RW
0000_0000h
18D0h
Peripheral Domain Access Control Word 0 (PDAC_W0_282)
32
RW
0000_0000h
18D4h
Peripheral Domain Access Control Word 1 (PDAC_W1_282)
32
RW
0000_0000h
18D8h
Peripheral Domain Access Control Word 0 (PDAC_W0_283)
32
RW
0000_0000h
18DCh
Peripheral Domain Access Control Word 1 (PDAC_W1_283)
32
RW
0000_0000h
18E0h
Peripheral Domain Access Control Word 0 (PDAC_W0_284)
32
RW
0000_0000h
18E4h
Peripheral Domain Access Control Word 1 (PDAC_W1_284)
32
RW
0000_0000h
18E8h
Peripheral Domain Access Control Word 0 (PDAC_W0_285)
32
RW
0000_0000h
18ECh
Peripheral Domain Access Control Word 1 (PDAC_W1_285)
32
RW
0000_0000h
18F0h
Peripheral Domain Access Control Word 0 (PDAC_W0_286)
32
RW
0000_0000h
18F4h
Peripheral Domain Access Control Word 1 (PDAC_W1_286)
32
RW
0000_0000h
18F8h
Peripheral Domain Access Control Word 0 (PDAC_W0_287)
32
RW
0000_0000h
18FCh
Peripheral Domain Access Control Word 1 (PDAC_W1_287)
32
RW
0000_0000h
1908h
Peripheral Domain Access Control Word 0 (PDAC_W0_289)
32
RW
0000_0000h
190Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_289)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
712 / 5251


---
# 페이지 662

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1910h
Peripheral Domain Access Control Word 0 (PDAC_W0_290)
32
RW
0000_0000h
1914h
Peripheral Domain Access Control Word 1 (PDAC_W1_290)
32
RW
0000_0000h
1918h
Peripheral Domain Access Control Word 0 (PDAC_W0_291)
32
RW
0000_0000h
191Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_291)
32
RW
0000_0000h
1920h
Peripheral Domain Access Control Word 0 (PDAC_W0_292)
32
RW
0000_0000h
1924h
Peripheral Domain Access Control Word 1 (PDAC_W1_292)
32
RW
0000_0000h
1928h
Peripheral Domain Access Control Word 0 (PDAC_W0_293)
32
RW
0000_0000h
192Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_293)
32
RW
0000_0000h
1930h
Peripheral Domain Access Control Word 0 (PDAC_W0_294)
32
RW
0000_0000h
1934h
Peripheral Domain Access Control Word 1 (PDAC_W1_294)
32
RW
0000_0000h
1938h
Peripheral Domain Access Control Word 0 (PDAC_W0_295)
32
RW
0000_0000h
193Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_295)
32
RW
0000_0000h
1940h
Peripheral Domain Access Control Word 0 (PDAC_W0_296)
32
RW
0000_0000h
1944h
Peripheral Domain Access Control Word 1 (PDAC_W1_296)
32
RW
0000_0000h
1948h
Peripheral Domain Access Control Word 0 (PDAC_W0_297)
32
RW
0000_0000h
194Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_297)
32
RW
0000_0000h
1950h
Peripheral Domain Access Control Word 0 (PDAC_W0_298)
32
RW
0000_0000h
1954h
Peripheral Domain Access Control Word 1 (PDAC_W1_298)
32
RW
0000_0000h
1978h
Peripheral Domain Access Control Word 0 (PDAC_W0_303)
32
RW
0000_0000h
197Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_303)
32
RW
0000_0000h
1980h
Peripheral Domain Access Control Word 0 (PDAC_W0_304)
32
RW
0000_0000h
1984h
Peripheral Domain Access Control Word 1 (PDAC_W1_304)
32
RW
0000_0000h
1998h
Peripheral Domain Access Control Word 0 (PDAC_W0_307)
32
RW
0000_0000h
199Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_307)
32
RW
0000_0000h
19B8h
Peripheral Domain Access Control Word 0 (PDAC_W0_311)
32
RW
0000_0000h
19BCh
Peripheral Domain Access Control Word 1 (PDAC_W1_311)
32
RW
0000_0000h
19D0h
Peripheral Domain Access Control Word 0 (PDAC_W0_314)
32
RW
0000_0000h
19D4h
Peripheral Domain Access Control Word 1 (PDAC_W1_314)
32
RW
0000_0000h
19D8h
Peripheral Domain Access Control Word 0 (PDAC_W0_315)
32
RW
0000_0000h
19DCh
Peripheral Domain Access Control Word 1 (PDAC_W1_315)
32
RW
0000_0000h
19F0h
Peripheral Domain Access Control Word 0 (PDAC_W0_318)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
713 / 5251


---
# 페이지 663

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
19F4h
Peripheral Domain Access Control Word 1 (PDAC_W1_318)
32
RW
0000_0000h
19F8h
Peripheral Domain Access Control Word 0 (PDAC_W0_319)
32
RW
0000_0000h
19FCh
Peripheral Domain Access Control Word 1 (PDAC_W1_319)
32
RW
0000_0000h
1A00h
Peripheral Domain Access Control Word 0 (PDAC_W0_320)
32
RW
0000_0000h
1A04h
Peripheral Domain Access Control Word 1 (PDAC_W1_320)
32
RW
0000_0000h
1A08h
Peripheral Domain Access Control Word 0 (PDAC_W0_321)
32
RW
0000_0000h
1A0Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_321)
32
RW
0000_0000h
1A18h
Peripheral Domain Access Control Word 0 (PDAC_W0_323)
32
RW
0000_0000h
1A1Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_323)
32
RW
0000_0000h
1A20h
Peripheral Domain Access Control Word 0 (PDAC_W0_324)
32
RW
0000_0000h
1A24h
Peripheral Domain Access Control Word 1 (PDAC_W1_324)
32
RW
0000_0000h
1A28h
Peripheral Domain Access Control Word 0 (PDAC_W0_325)
32
RW
0000_0000h
1A2Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_325)
32
RW
0000_0000h
1A30h
Peripheral Domain Access Control Word 0 (PDAC_W0_326)
32
RW
0000_0000h
1A34h
Peripheral Domain Access Control Word 1 (PDAC_W1_326)
32
RW
0000_0000h
1A40h
Peripheral Domain Access Control Word 0 (PDAC_W0_328)
32
RW
0000_0000h
1A44h
Peripheral Domain Access Control Word 1 (PDAC_W1_328)
32
RW
0000_0000h
1A48h
Peripheral Domain Access Control Word 0 (PDAC_W0_329)
32
RW
0000_0000h
1A4Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_329)
32
RW
0000_0000h
1A50h
Peripheral Domain Access Control Word 0 (PDAC_W0_330)
32
RW
0000_0000h
1A54h
Peripheral Domain Access Control Word 1 (PDAC_W1_330)
32
RW
0000_0000h
1A58h
Peripheral Domain Access Control Word 0 (PDAC_W0_331)
32
RW
0000_0000h
1A5Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_331)
32
RW
0000_0000h
1A60h
Peripheral Domain Access Control Word 0 (PDAC_W0_332)
32
RW
0000_0000h
1A64h
Peripheral Domain Access Control Word 1 (PDAC_W1_332)
32
RW
0000_0000h
1A68h
Peripheral Domain Access Control Word 0 (PDAC_W0_333)
32
RW
0000_0000h
1A6Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_333)
32
RW
0000_0000h
1A70h
Peripheral Domain Access Control Word 0 (PDAC_W0_334)
32
RW
0000_0000h
1A74h
Peripheral Domain Access Control Word 1 (PDAC_W1_334)
32
RW
0000_0000h
1A78h
Peripheral Domain Access Control Word 0 (PDAC_W0_335)
32
RW
0000_0000h
1A7Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_335)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
714 / 5251


---
# 페이지 664

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1A88h
Peripheral Domain Access Control Word 0 (PDAC_W0_337)
32
RW
0000_0000h
1A8Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_337)
32
RW
0000_0000h
1A90h
Peripheral Domain Access Control Word 0 (PDAC_W0_338)
32
RW
0000_0000h
1A94h
Peripheral Domain Access Control Word 1 (PDAC_W1_338)
32
RW
0000_0000h
1A98h
Peripheral Domain Access Control Word 0 (PDAC_W0_339)
32
RW
0000_0000h
1A9Ch
Peripheral Domain Access Control Word 1 (PDAC_W1_339)
32
RW
0000_0000h
1AA0h
Peripheral Domain Access Control Word 0 (PDAC_W0_340)
32
RW
0000_0000h
1AA4h
Peripheral Domain Access Control Word 1 (PDAC_W1_340)
32
RW
0000_0000h
1AA8h
Peripheral Domain Access Control Word 0 (PDAC_W0_341)
32
RW
0000_0000h
1AACh
Peripheral Domain Access Control Word 1 (PDAC_W1_341)
32
RW
0000_0000h
1AB0h
Peripheral Domain Access Control Word 0 (PDAC_W0_342)
32
RW
0000_0000h
1AB4h
Peripheral Domain Access Control Word 1 (PDAC_W1_342)
32
RW
0000_0000h
1AB8h
Peripheral Domain Access Control Word 0 (PDAC_W0_343)
32
RW
0000_0000h
1ABCh
Peripheral Domain Access Control Word 1 (PDAC_W1_343)
32
RW
0000_0000h
1AC0h
Peripheral Domain Access Control Word 0 (PDAC_W0_344)
32
RW
0000_0000h
1AC4h
Peripheral Domain Access Control Word 1 (PDAC_W1_344)
32
RW
0000_0000h
1AC8h
Peripheral Domain Access Control Word 0 (PDAC_W0_345)
32
RW
0000_0000h
1ACCh
Peripheral Domain Access Control Word 1 (PDAC_W1_345)
32
RW
0000_0000h
1AD0h
Peripheral Domain Access Control Word 0 (PDAC_W0_346)
32
RW
0000_0000h
1AD4h
Peripheral Domain Access Control Word 1 (PDAC_W1_346)
32
RW
0000_0000h
1AD8h
Peripheral Domain Access Control Word 0 (PDAC_W0_347)
32
RW
0000_0000h
1ADCh
Peripheral Domain Access Control Word 1 (PDAC_W1_347)
32
RW
0000_0000h
2000h
Memory Region Descriptor Word 0 (MRGD_W0_0)
32
RW
0000_0001h
2004h
Memory Region Descriptor Word 1 (MRGD_W1_0)
32
RW
0000_001Fh
2008h
Memory Region Descriptor Word 2 (MRGD_W2_0)
32
RW
0000_0000h
200Ch
Memory Region Descriptor Word 3 (MRGD_W3_0)
32
RW
0000_0000h
2020h
Memory Region Descriptor Word 0 (MRGD_W0_1)
32
RW
0000_0001h
2024h
Memory Region Descriptor Word 1 (MRGD_W1_1)
32
RW
0000_001Fh
2028h
Memory Region Descriptor Word 2 (MRGD_W2_1)
32
RW
0000_0000h
202Ch
Memory Region Descriptor Word 3 (MRGD_W3_1)
32
RW
0000_0000h
2040h
Memory Region Descriptor Word 0 (MRGD_W0_2)
32
RW
0000_0001h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
715 / 5251


---
# 페이지 665

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
2044h
Memory Region Descriptor Word 1 (MRGD_W1_2)
32
RW
0000_001Fh
2048h
Memory Region Descriptor Word 2 (MRGD_W2_2)
32
RW
0000_0000h
204Ch
Memory Region Descriptor Word 3 (MRGD_W3_2)
32
RW
0000_0000h
2060h
Memory Region Descriptor Word 0 (MRGD_W0_3)
32
RW
0000_0001h
2064h
Memory Region Descriptor Word 1 (MRGD_W1_3)
32
RW
0000_001Fh
2068h
Memory Region Descriptor Word 2 (MRGD_W2_3)
32
RW
0000_0000h
206Ch
Memory Region Descriptor Word 3 (MRGD_W3_3)
32
RW
0000_0000h
2080h
Memory Region Descriptor Word 0 (MRGD_W0_4)
32
RW
0000_0001h
2084h
Memory Region Descriptor Word 1 (MRGD_W1_4)
32
RW
0000_001Fh
2088h
Memory Region Descriptor Word 2 (MRGD_W2_4)
32
RW
0000_0000h
208Ch
Memory Region Descriptor Word 3 (MRGD_W3_4)
32
RW
0000_0000h
20A0h
Memory Region Descriptor Word 0 (MRGD_W0_5)
32
RW
0000_0001h
20A4h
Memory Region Descriptor Word 1 (MRGD_W1_5)
32
RW
0000_001Fh
20A8h
Memory Region Descriptor Word 2 (MRGD_W2_5)
32
RW
0000_0000h
20ACh
Memory Region Descriptor Word 3 (MRGD_W3_5)
32
RW
0000_0000h
20C0h
Memory Region Descriptor Word 0 (MRGD_W0_6)
32
RW
0000_0001h
20C4h
Memory Region Descriptor Word 1 (MRGD_W1_6)
32
RW
0000_001Fh
20C8h
Memory Region Descriptor Word 2 (MRGD_W2_6)
32
RW
0000_0000h
20CCh
Memory Region Descriptor Word 3 (MRGD_W3_6)
32
RW
0000_0000h
20E0h
Memory Region Descriptor Word 0 (MRGD_W0_7)
32
RW
0000_0001h
20E4h
Memory Region Descriptor Word 1 (MRGD_W1_7)
32
RW
0000_001Fh
20E8h
Memory Region Descriptor Word 2 (MRGD_W2_7)
32
RW
0000_0000h
20ECh
Memory Region Descriptor Word 3 (MRGD_W3_7)
32
RW
0000_0000h
2100h
Memory Region Descriptor Word 0 (MRGD_W0_8)
32
RW
0000_0001h
2104h
Memory Region Descriptor Word 1 (MRGD_W1_8)
32
RW
0000_001Fh
2108h
Memory Region Descriptor Word 2 (MRGD_W2_8)
32
RW
0000_0000h
210Ch
Memory Region Descriptor Word 3 (MRGD_W3_8)
32
RW
0000_0000h
2120h
Memory Region Descriptor Word 0 (MRGD_W0_9)
32
RW
0000_0001h
2124h
Memory Region Descriptor Word 1 (MRGD_W1_9)
32
RW
0000_001Fh
2128h
Memory Region Descriptor Word 2 (MRGD_W2_9)
32
RW
0000_0000h
212Ch
Memory Region Descriptor Word 3 (MRGD_W3_9)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
716 / 5251


---
# 페이지 666

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
2140h
Memory Region Descriptor Word 0 (MRGD_W0_10)
32
RW
0000_0001h
2144h
Memory Region Descriptor Word 1 (MRGD_W1_10)
32
RW
0000_001Fh
2148h
Memory Region Descriptor Word 2 (MRGD_W2_10)
32
RW
0000_0000h
214Ch
Memory Region Descriptor Word 3 (MRGD_W3_10)
32
RW
0000_0000h
2160h
Memory Region Descriptor Word 0 (MRGD_W0_11)
32
RW
0000_0001h
2164h
Memory Region Descriptor Word 1 (MRGD_W1_11)
32
RW
0000_001Fh
2168h
Memory Region Descriptor Word 2 (MRGD_W2_11)
32
RW
0000_0000h
216Ch
Memory Region Descriptor Word 3 (MRGD_W3_11)
32
RW
0000_0000h
2180h
Memory Region Descriptor Word 0 (MRGD_W0_12)
32
RW
0000_0001h
2184h
Memory Region Descriptor Word 1 (MRGD_W1_12)
32
RW
0000_001Fh
2188h
Memory Region Descriptor Word 2 (MRGD_W2_12)
32
RW
0000_0000h
218Ch
Memory Region Descriptor Word 3 (MRGD_W3_12)
32
RW
0000_0000h
21A0h
Memory Region Descriptor Word 0 (MRGD_W0_13)
32
RW
0000_0001h
21A4h
Memory Region Descriptor Word 1 (MRGD_W1_13)
32
RW
0000_001Fh
21A8h
Memory Region Descriptor Word 2 (MRGD_W2_13)
32
RW
0000_0000h
21ACh
Memory Region Descriptor Word 3 (MRGD_W3_13)
32
RW
0000_0000h
21C0h
Memory Region Descriptor Word 0 (MRGD_W0_14)
32
RW
0000_0001h
21C4h
Memory Region Descriptor Word 1 (MRGD_W1_14)
32
RW
0000_001Fh
21C8h
Memory Region Descriptor Word 2 (MRGD_W2_14)
32
RW
0000_0000h
21CCh
Memory Region Descriptor Word 3 (MRGD_W3_14)
32
RW
0000_0000h
21E0h
Memory Region Descriptor Word 0 (MRGD_W0_15)
32
RW
0000_0001h
21E4h
Memory Region Descriptor Word 1 (MRGD_W1_15)
32
RW
0000_001Fh
21E8h
Memory Region Descriptor Word 2 (MRGD_W2_15)
32
RW
0000_0000h
21ECh
Memory Region Descriptor Word 3 (MRGD_W3_15)
32
RW
0000_0000h
2200h
Memory Region Descriptor Word 0 (MRGD_W0_16)
32
RW
0000_0001h
2204h
Memory Region Descriptor Word 1 (MRGD_W1_16)
32
RW
0000_001Fh
2208h
Memory Region Descriptor Word 2 (MRGD_W2_16)
32
RW
0000_0000h
220Ch
Memory Region Descriptor Word 3 (MRGD_W3_16)
32
RW
0000_0000h
2220h
Memory Region Descriptor Word 0 (MRGD_W0_17)
32
RW
0000_0001h
2224h
Memory Region Descriptor Word 1 (MRGD_W1_17)
32
RW
0000_001Fh
2228h
Memory Region Descriptor Word 2 (MRGD_W2_17)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
717 / 5251


---
# 페이지 667

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
222Ch
Memory Region Descriptor Word 3 (MRGD_W3_17)
32
RW
0000_0000h
2240h
Memory Region Descriptor Word 0 (MRGD_W0_18)
32
RW
0000_0001h
2244h
Memory Region Descriptor Word 1 (MRGD_W1_18)
32
RW
0000_001Fh
2248h
Memory Region Descriptor Word 2 (MRGD_W2_18)
32
RW
0000_0000h
224Ch
Memory Region Descriptor Word 3 (MRGD_W3_18)
32
RW
0000_0000h
2260h
Memory Region Descriptor Word 0 (MRGD_W0_19)
32
RW
0000_0001h
2264h
Memory Region Descriptor Word 1 (MRGD_W1_19)
32
RW
0000_001Fh
2268h
Memory Region Descriptor Word 2 (MRGD_W2_19)
32
RW
0000_0000h
226Ch
Memory Region Descriptor Word 3 (MRGD_W3_19)
32
RW
0000_0000h
2280h
Memory Region Descriptor Word 0 (MRGD_W0_20)
32
RW
0000_0001h
2284h
Memory Region Descriptor Word 1 (MRGD_W1_20)
32
RW
0000_001Fh
2288h
Memory Region Descriptor Word 2 (MRGD_W2_20)
32
RW
0000_0000h
228Ch
Memory Region Descriptor Word 3 (MRGD_W3_20)
32
RW
0000_0000h
22A0h
Memory Region Descriptor Word 0 (MRGD_W0_21)
32
RW
0000_0001h
22A4h
Memory Region Descriptor Word 1 (MRGD_W1_21)
32
RW
0000_001Fh
22A8h
Memory Region Descriptor Word 2 (MRGD_W2_21)
32
RW
0000_0000h
22ACh
Memory Region Descriptor Word 3 (MRGD_W3_21)
32
RW
0000_0000h
22C0h
Memory Region Descriptor Word 0 (MRGD_W0_22)
32
RW
0000_0001h
22C4h
Memory Region Descriptor Word 1 (MRGD_W1_22)
32
RW
0000_001Fh
22C8h
Memory Region Descriptor Word 2 (MRGD_W2_22)
32
RW
0000_0000h
22CCh
Memory Region Descriptor Word 3 (MRGD_W3_22)
32
RW
0000_0000h
22E0h
Memory Region Descriptor Word 0 (MRGD_W0_23)
32
RW
0000_0001h
22E4h
Memory Region Descriptor Word 1 (MRGD_W1_23)
32
RW
0000_001Fh
22E8h
Memory Region Descriptor Word 2 (MRGD_W2_23)
32
RW
0000_0000h
22ECh
Memory Region Descriptor Word 3 (MRGD_W3_23)
32
RW
0000_0000h
2300h
Memory Region Descriptor Word 0 (MRGD_W0_24)
32
RW
0000_0001h
2304h
Memory Region Descriptor Word 1 (MRGD_W1_24)
32
RW
0000_001Fh
2308h
Memory Region Descriptor Word 2 (MRGD_W2_24)
32
RW
0000_0000h
230Ch
Memory Region Descriptor Word 3 (MRGD_W3_24)
32
RW
0000_0000h
2320h
Memory Region Descriptor Word 0 (MRGD_W0_25)
32
RW
0000_0001h
2324h
Memory Region Descriptor Word 1 (MRGD_W1_25)
32
RW
0000_001Fh
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
718 / 5251


---
# 페이지 668

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
2328h
Memory Region Descriptor Word 2 (MRGD_W2_25)
32
RW
0000_0000h
232Ch
Memory Region Descriptor Word 3 (MRGD_W3_25)
32
RW
0000_0000h
2340h
Memory Region Descriptor Word 0 (MRGD_W0_26)
32
RW
0000_0001h
2344h
Memory Region Descriptor Word 1 (MRGD_W1_26)
32
RW
0000_001Fh
2348h
Memory Region Descriptor Word 2 (MRGD_W2_26)
32
RW
0000_0000h
234Ch
Memory Region Descriptor Word 3 (MRGD_W3_26)
32
RW
0000_0000h
2360h
Memory Region Descriptor Word 0 (MRGD_W0_27)
32
RW
0000_0001h
2364h
Memory Region Descriptor Word 1 (MRGD_W1_27)
32
RW
0000_001Fh
2368h
Memory Region Descriptor Word 2 (MRGD_W2_27)
32
RW
0000_0000h
236Ch
Memory Region Descriptor Word 3 (MRGD_W3_27)
32
RW
0000_0000h
2380h
Memory Region Descriptor Word 0 (MRGD_W0_28)
32
RW
0000_0001h
2384h
Memory Region Descriptor Word 1 (MRGD_W1_28)
32
RW
0000_001Fh
2388h
Memory Region Descriptor Word 2 (MRGD_W2_28)
32
RW
0000_0000h
238Ch
Memory Region Descriptor Word 3 (MRGD_W3_28)
32
RW
0000_0000h
23A0h
Memory Region Descriptor Word 0 (MRGD_W0_29)
32
RW
0000_0001h
23A4h
Memory Region Descriptor Word 1 (MRGD_W1_29)
32
RW
0000_001Fh
23A8h
Memory Region Descriptor Word 2 (MRGD_W2_29)
32
RW
0000_0000h
23ACh
Memory Region Descriptor Word 3 (MRGD_W3_29)
32
RW
0000_0000h
23C0h
Memory Region Descriptor Word 0 (MRGD_W0_30)
32
RW
0000_0001h
23C4h
Memory Region Descriptor Word 1 (MRGD_W1_30)
32
RW
0000_001Fh
23C8h
Memory Region Descriptor Word 2 (MRGD_W2_30)
32
RW
0000_0000h
23CCh
Memory Region Descriptor Word 3 (MRGD_W3_30)
32
RW
0000_0000h
23E0h
Memory Region Descriptor Word 0 (MRGD_W0_31)
32
RW
0000_0001h
23E4h
Memory Region Descriptor Word 1 (MRGD_W1_31)
32
RW
0000_001Fh
23E8h
Memory Region Descriptor Word 2 (MRGD_W2_31)
32
RW
0000_0000h
23ECh
Memory Region Descriptor Word 3 (MRGD_W3_31)
32
RW
0000_0000h
2400h
Memory Region Descriptor Word 0 (MRGD_W0_32)
32
RW
0000_0001h
2404h
Memory Region Descriptor Word 1 (MRGD_W1_32)
32
RW
0000_001Fh
2408h
Memory Region Descriptor Word 2 (MRGD_W2_32)
32
RW
0000_0000h
240Ch
Memory Region Descriptor Word 3 (MRGD_W3_32)
32
RW
0000_0000h
2420h
Memory Region Descriptor Word 0 (MRGD_W0_33)
32
RW
0000_0001h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
719 / 5251


---
# 페이지 669

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
2424h
Memory Region Descriptor Word 1 (MRGD_W1_33)
32
RW
0000_001Fh
2428h
Memory Region Descriptor Word 2 (MRGD_W2_33)
32
RW
0000_0000h
242Ch
Memory Region Descriptor Word 3 (MRGD_W3_33)
32
RW
0000_0000h
2440h
Memory Region Descriptor Word 0 (MRGD_W0_34)
32
RW
0000_0001h
2444h
Memory Region Descriptor Word 1 (MRGD_W1_34)
32
RW
0000_001Fh
2448h
Memory Region Descriptor Word 2 (MRGD_W2_34)
32
RW
0000_0000h
244Ch
Memory Region Descriptor Word 3 (MRGD_W3_34)
32
RW
0000_0000h
2460h
Memory Region Descriptor Word 0 (MRGD_W0_35)
32
RW
0000_0001h
2464h
Memory Region Descriptor Word 1 (MRGD_W1_35)
32
RW
0000_001Fh
2468h
Memory Region Descriptor Word 2 (MRGD_W2_35)
32
RW
0000_0000h
246Ch
Memory Region Descriptor Word 3 (MRGD_W3_35)
32
RW
0000_0000h
2600h
Memory Region Descriptor Word 0 (MRGD_W0_48)
32
RW
0000_0001h
2604h
Memory Region Descriptor Word 1 (MRGD_W1_48)
32
RW
0000_001Fh
2608h
Memory Region Descriptor Word 2 (MRGD_W2_48)
32
RW
0000_0000h
260Ch
Memory Region Descriptor Word 3 (MRGD_W3_48)
32
RW
0000_0000h
2620h
Memory Region Descriptor Word 0 (MRGD_W0_49)
32
RW
0000_0001h
2624h
Memory Region Descriptor Word 1 (MRGD_W1_49)
32
RW
0000_001Fh
2628h
Memory Region Descriptor Word 2 (MRGD_W2_49)
32
RW
0000_0000h
262Ch
Memory Region Descriptor Word 3 (MRGD_W3_49)
32
RW
0000_0000h
2640h
Memory Region Descriptor Word 0 (MRGD_W0_50)
32
RW
0000_0001h
2644h
Memory Region Descriptor Word 1 (MRGD_W1_50)
32
RW
0000_001Fh
2648h
Memory Region Descriptor Word 2 (MRGD_W2_50)
32
RW
0000_0000h
264Ch
Memory Region Descriptor Word 3 (MRGD_W3_50)
32
RW
0000_0000h
2660h
Memory Region Descriptor Word 0 (MRGD_W0_51)
32
RW
0000_0001h
2664h
Memory Region Descriptor Word 1 (MRGD_W1_51)
32
RW
0000_001Fh
2668h
Memory Region Descriptor Word 2 (MRGD_W2_51)
32
RW
0000_0000h
266Ch
Memory Region Descriptor Word 3 (MRGD_W3_51)
32
RW
0000_0000h
2680h
Memory Region Descriptor Word 0 (MRGD_W0_52)
32
RW
0000_0001h
2684h
Memory Region Descriptor Word 1 (MRGD_W1_52)
32
RW
0000_001Fh
2688h
Memory Region Descriptor Word 2 (MRGD_W2_52)
32
RW
0000_0000h
268Ch
Memory Region Descriptor Word 3 (MRGD_W3_52)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
720 / 5251


---
# 페이지 670

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
26A0h
Memory Region Descriptor Word 0 (MRGD_W0_53)
32
RW
0000_0001h
26A4h
Memory Region Descriptor Word 1 (MRGD_W1_53)
32
RW
0000_001Fh
26A8h
Memory Region Descriptor Word 2 (MRGD_W2_53)
32
RW
0000_0000h
26ACh
Memory Region Descriptor Word 3 (MRGD_W3_53)
32
RW
0000_0000h
26C0h
Memory Region Descriptor Word 0 (MRGD_W0_54)
32
RW
0000_0001h
26C4h
Memory Region Descriptor Word 1 (MRGD_W1_54)
32
RW
0000_001Fh
26C8h
Memory Region Descriptor Word 2 (MRGD_W2_54)
32
RW
0000_0000h
26CCh
Memory Region Descriptor Word 3 (MRGD_W3_54)
32
RW
0000_0000h
26E0h
Memory Region Descriptor Word 0 (MRGD_W0_55)
32
RW
0000_0001h
26E4h
Memory Region Descriptor Word 1 (MRGD_W1_55)
32
RW
0000_001Fh
26E8h
Memory Region Descriptor Word 2 (MRGD_W2_55)
32
RW
0000_0000h
26ECh
Memory Region Descriptor Word 3 (MRGD_W3_55)
32
RW
0000_0000h
2700h
Memory Region Descriptor Word 0 (MRGD_W0_56)
32
RW
0000_0001h
2704h
Memory Region Descriptor Word 1 (MRGD_W1_56)
32
RW
0000_001Fh
2708h
Memory Region Descriptor Word 2 (MRGD_W2_56)
32
RW
0000_0000h
270Ch
Memory Region Descriptor Word 3 (MRGD_W3_56)
32
RW
0000_0000h
2720h
Memory Region Descriptor Word 0 (MRGD_W0_57)
32
RW
0000_0001h
2724h
Memory Region Descriptor Word 1 (MRGD_W1_57)
32
RW
0000_001Fh
2728h
Memory Region Descriptor Word 2 (MRGD_W2_57)
32
RW
0000_0000h
272Ch
Memory Region Descriptor Word 3 (MRGD_W3_57)
32
RW
0000_0000h
2740h
Memory Region Descriptor Word 0 (MRGD_W0_58)
32
RW
0000_0001h
2744h
Memory Region Descriptor Word 1 (MRGD_W1_58)
32
RW
0000_001Fh
2748h
Memory Region Descriptor Word 2 (MRGD_W2_58)
32
RW
0000_0000h
274Ch
Memory Region Descriptor Word 3 (MRGD_W3_58)
32
RW
0000_0000h
2760h
Memory Region Descriptor Word 0 (MRGD_W0_59)
32
RW
0000_0001h
2764h
Memory Region Descriptor Word 1 (MRGD_W1_59)
32
RW
0000_001Fh
2768h
Memory Region Descriptor Word 2 (MRGD_W2_59)
32
RW
0000_0000h
276Ch
Memory Region Descriptor Word 3 (MRGD_W3_59)
32
RW
0000_0000h
2780h
Memory Region Descriptor Word 0 (MRGD_W0_60)
32
RW
0000_0001h
2784h
Memory Region Descriptor Word 1 (MRGD_W1_60)
32
RW
0000_001Fh
2788h
Memory Region Descriptor Word 2 (MRGD_W2_60)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
721 / 5251


---
# 페이지 671

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
278Ch
Memory Region Descriptor Word 3 (MRGD_W3_60)
32
RW
0000_0000h
27A0h
Memory Region Descriptor Word 0 (MRGD_W0_61)
32
RW
0000_0001h
27A4h
Memory Region Descriptor Word 1 (MRGD_W1_61)
32
RW
0000_001Fh
27A8h
Memory Region Descriptor Word 2 (MRGD_W2_61)
32
RW
0000_0000h
27ACh
Memory Region Descriptor Word 3 (MRGD_W3_61)
32
RW
0000_0000h
27C0h
Memory Region Descriptor Word 0 (MRGD_W0_62)
32
RW
0000_0001h
27C4h
Memory Region Descriptor Word 1 (MRGD_W1_62)
32
RW
0000_001Fh
27C8h
Memory Region Descriptor Word 2 (MRGD_W2_62)
32
RW
0000_0000h
27CCh
Memory Region Descriptor Word 3 (MRGD_W3_62)
32
RW
0000_0000h
27E0h
Memory Region Descriptor Word 0 (MRGD_W0_63)
32
RW
0000_0001h
27E4h
Memory Region Descriptor Word 1 (MRGD_W1_63)
32
RW
0000_001Fh
27E8h
Memory Region Descriptor Word 2 (MRGD_W2_63)
32
RW
0000_0000h
27ECh
Memory Region Descriptor Word 3 (MRGD_W3_63)
32
RW
0000_0000h
2800h
Memory Region Descriptor Word 0 (MRGD_W0_64)
32
RW
0000_0001h
2804h
Memory Region Descriptor Word 1 (MRGD_W1_64)
32
RW
0000_001Fh
2808h
Memory Region Descriptor Word 2 (MRGD_W2_64)
32
RW
0000_0000h
280Ch
Memory Region Descriptor Word 3 (MRGD_W3_64)
32
RW
0000_0000h
2820h
Memory Region Descriptor Word 0 (MRGD_W0_65)
32
RW
0000_0001h
2824h
Memory Region Descriptor Word 1 (MRGD_W1_65)
32
RW
0000_001Fh
2828h
Memory Region Descriptor Word 2 (MRGD_W2_65)
32
RW
0000_0000h
282Ch
Memory Region Descriptor Word 3 (MRGD_W3_65)
32
RW
0000_0000h
2840h
Memory Region Descriptor Word 0 (MRGD_W0_66)
32
RW
0000_0001h
2844h
Memory Region Descriptor Word 1 (MRGD_W1_66)
32
RW
0000_001Fh
2848h
Memory Region Descriptor Word 2 (MRGD_W2_66)
32
RW
0000_0000h
284Ch
Memory Region Descriptor Word 3 (MRGD_W3_66)
32
RW
0000_0000h
2860h
Memory Region Descriptor Word 0 (MRGD_W0_67)
32
RW
0000_0001h
2864h
Memory Region Descriptor Word 1 (MRGD_W1_67)
32
RW
0000_001Fh
2868h
Memory Region Descriptor Word 2 (MRGD_W2_67)
32
RW
0000_0000h
286Ch
Memory Region Descriptor Word 3 (MRGD_W3_67)
32
RW
0000_0000h
2A00h
Memory Region Descriptor Word 0 (MRGD_W0_80)
32
RW
0000_0001h
2A04h
Memory Region Descriptor Word 1 (MRGD_W1_80)
32
RW
0000_001Fh
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
722 / 5251


---
# 페이지 672

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
2A08h
Memory Region Descriptor Word 2 (MRGD_W2_80)
32
RW
0000_0000h
2A0Ch
Memory Region Descriptor Word 3 (MRGD_W3_80)
32
RW
0000_0000h
2A20h
Memory Region Descriptor Word 0 (MRGD_W0_81)
32
RW
0000_0001h
2A24h
Memory Region Descriptor Word 1 (MRGD_W1_81)
32
RW
0000_001Fh
2A28h
Memory Region Descriptor Word 2 (MRGD_W2_81)
32
RW
0000_0000h
2A2Ch
Memory Region Descriptor Word 3 (MRGD_W3_81)
32
RW
0000_0000h
2A40h
Memory Region Descriptor Word 0 (MRGD_W0_82)
32
RW
0000_0001h
2A44h
Memory Region Descriptor Word 1 (MRGD_W1_82)
32
RW
0000_001Fh
2A48h
Memory Region Descriptor Word 2 (MRGD_W2_82)
32
RW
0000_0000h
2A4Ch
Memory Region Descriptor Word 3 (MRGD_W3_82)
32
RW
0000_0000h
2A60h
Memory Region Descriptor Word 0 (MRGD_W0_83)
32
RW
0000_0001h
2A64h
Memory Region Descriptor Word 1 (MRGD_W1_83)
32
RW
0000_001Fh
2A68h
Memory Region Descriptor Word 2 (MRGD_W2_83)
32
RW
0000_0000h
2A6Ch
Memory Region Descriptor Word 3 (MRGD_W3_83)
32
RW
0000_0000h
2A80h
Memory Region Descriptor Word 0 (MRGD_W0_84)
32
RW
0000_0001h
2A84h
Memory Region Descriptor Word 1 (MRGD_W1_84)
32
RW
0000_001Fh
2A88h
Memory Region Descriptor Word 2 (MRGD_W2_84)
32
RW
0000_0000h
2A8Ch
Memory Region Descriptor Word 3 (MRGD_W3_84)
32
RW
0000_0000h
2AA0h
Memory Region Descriptor Word 0 (MRGD_W0_85)
32
RW
0000_0001h
2AA4h
Memory Region Descriptor Word 1 (MRGD_W1_85)
32
RW
0000_001Fh
2AA8h
Memory Region Descriptor Word 2 (MRGD_W2_85)
32
RW
0000_0000h
2AACh
Memory Region Descriptor Word 3 (MRGD_W3_85)
32
RW
0000_0000h
2AC0h
Memory Region Descriptor Word 0 (MRGD_W0_86)
32
RW
0000_0001h
2AC4h
Memory Region Descriptor Word 1 (MRGD_W1_86)
32
RW
0000_001Fh
2AC8h
Memory Region Descriptor Word 2 (MRGD_W2_86)
32
RW
0000_0000h
2ACCh
Memory Region Descriptor Word 3 (MRGD_W3_86)
32
RW
0000_0000h
2AE0h
Memory Region Descriptor Word 0 (MRGD_W0_87)
32
RW
0000_0001h
2AE4h
Memory Region Descriptor Word 1 (MRGD_W1_87)
32
RW
0000_001Fh
2AE8h
Memory Region Descriptor Word 2 (MRGD_W2_87)
32
RW
0000_0000h
2AECh
Memory Region Descriptor Word 3 (MRGD_W3_87)
32
RW
0000_0000h
2B00h
Memory Region Descriptor Word 0 (MRGD_W0_88)
32
RW
0000_0001h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
723 / 5251


---
# 페이지 673

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
2B04h
Memory Region Descriptor Word 1 (MRGD_W1_88)
32
RW
0000_001Fh
2B08h
Memory Region Descriptor Word 2 (MRGD_W2_88)
32
RW
0000_0000h
2B0Ch
Memory Region Descriptor Word 3 (MRGD_W3_88)
32
RW
0000_0000h
2B20h
Memory Region Descriptor Word 0 (MRGD_W0_89)
32
RW
0000_0001h
2B24h
Memory Region Descriptor Word 1 (MRGD_W1_89)
32
RW
0000_001Fh
2B28h
Memory Region Descriptor Word 2 (MRGD_W2_89)
32
RW
0000_0000h
2B2Ch
Memory Region Descriptor Word 3 (MRGD_W3_89)
32
RW
0000_0000h
2B40h
Memory Region Descriptor Word 0 (MRGD_W0_90)
32
RW
0000_0001h
2B44h
Memory Region Descriptor Word 1 (MRGD_W1_90)
32
RW
0000_001Fh
2B48h
Memory Region Descriptor Word 2 (MRGD_W2_90)
32
RW
0000_0000h
2B4Ch
Memory Region Descriptor Word 3 (MRGD_W3_90)
32
RW
0000_0000h
2B60h
Memory Region Descriptor Word 0 (MRGD_W0_91)
32
RW
0000_0001h
2B64h
Memory Region Descriptor Word 1 (MRGD_W1_91)
32
RW
0000_001Fh
2B68h
Memory Region Descriptor Word 2 (MRGD_W2_91)
32
RW
0000_0000h
2B6Ch
Memory Region Descriptor Word 3 (MRGD_W3_91)
32
RW
0000_0000h
2B80h
Memory Region Descriptor Word 0 (MRGD_W0_92)
32
RW
0000_0001h
2B84h
Memory Region Descriptor Word 1 (MRGD_W1_92)
32
RW
0000_001Fh
2B88h
Memory Region Descriptor Word 2 (MRGD_W2_92)
32
RW
0000_0000h
2B8Ch
Memory Region Descriptor Word 3 (MRGD_W3_92)
32
RW
0000_0000h
2BA0h
Memory Region Descriptor Word 0 (MRGD_W0_93)
32
RW
0000_0001h
2BA4h
Memory Region Descriptor Word 1 (MRGD_W1_93)
32
RW
0000_001Fh
2BA8h
Memory Region Descriptor Word 2 (MRGD_W2_93)
32
RW
0000_0000h
2BACh
Memory Region Descriptor Word 3 (MRGD_W3_93)
32
RW
0000_0000h
2BC0h
Memory Region Descriptor Word 0 (MRGD_W0_94)
32
RW
0000_0001h
2BC4h
Memory Region Descriptor Word 1 (MRGD_W1_94)
32
RW
0000_001Fh
2BC8h
Memory Region Descriptor Word 2 (MRGD_W2_94)
32
RW
0000_0000h
2BCCh
Memory Region Descriptor Word 3 (MRGD_W3_94)
32
RW
0000_0000h
2BE0h
Memory Region Descriptor Word 0 (MRGD_W0_95)
32
RW
0000_0001h
2BE4h
Memory Region Descriptor Word 1 (MRGD_W1_95)
32
RW
0000_001Fh
2BE8h
Memory Region Descriptor Word 2 (MRGD_W2_95)
32
RW
0000_0000h
2BECh
Memory Region Descriptor Word 3 (MRGD_W3_95)
32
RW
0000_0000h
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
724 / 5251


---
# 페이지 674

19.8.3.2
Control (CR)
Offset
Register
Offset
CR
0h
Function
Provides XRDC status and enables XRDC operation.
Access: Secure privileged read/write
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
LK1 
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
VAW 
MRF 
0
HRL 
GVLD 
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
0
0
0
1
0
1
0
Fields
Field
Function
31
—
Reserved
30
LK1
Lock
Prohibits writes to this register.
• If unlocked, this register accepts any secure privileged write.
• If locked, you cannot write to this register and it remains read-only until after the next reset.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Unlocked
1b - Locks
When writing
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
725 / 5251


---
# 페이지 675

Table continued from the previous page...
Field
Function
0b - No effect
1b - Locks
29-9
—
Reserved
8
VAW
Virtualization Aware
Indicates whether domain assignments support the optional inclusion of a logical partition identifier, 
which is also known as an operating system number or Arm virtual machine identifier (VMID).
0b - Not virtualization-aware
1b - Virtualization-aware
7
MRF
Memory Region Format
Indicates the format of memory region descriptors.
0b - Reserved
1b - SMPU family format
6-5
—
Reserved
4-1
HRL
Hardware Revision Level
Indicates the XRDC hardware revision level, which is associated with a set of functional characteristics of 
the module.
0
GVLD
Global Valid (XRDC Global Enable/Disable)
Enables XRDC. When XRDC is disabled, all bus initiators can access all targets.
0b - Disables
1b - Enables
19.8.3.3
Hardware Configuration 0 (HWCFG0)
Offset
Register
Offset
HWCFG0
F0h
Function
Indicates XRDC configuration details, including:
• XRDC module ID
• Number of implemented domains
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
726 / 5251


---
# 페이지 676

• Number of bus initiators
• Number of MRCs
• Number of PACs
Attempting to write to this register causes an error.
Access: Secure privileged read
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
MID 
NPAC 
NMRC 
W
Reset
0
0
0
1
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
NMSTR 
NDID 
W
Reset
0
0
0
0
1
0
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
31-28
MID
Module ID
27-24
NPAC
Number Of PACs
Indicates the number of PACs minus 1. In other words, the actual number of PACs is NPAC + 1.
23-16
NMRC
Number of MRCs
Indicates the number of MRCs minus 1. In other words, the actual number of MRCs is NMRC + 1.
15-8
NMSTR
Number Of Bus Initiators
Indicates the number of bus initiators minus 1. In other words, the actual number of bus initiators is 
NMSTR + 1.
7-0
NDID
Number Of DIDs
Indicates the number of domains (DIDs) minus 1. In other words, the actual number of DIDs is NDID + 1.
19.8.3.4
Hardware Configuration 1 (HWCFG1)
Offset
Register
Offset
HWCFG1
F4h
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
727 / 5251


---
# 페이지 677

Function
Indicates the DID of the bus initiator making the current transaction request. See Domain error capture management for 
information about typical usage.
Attempting to write to this register causes an error.
Access: Secure privileged read
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
DID 
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
u1
u
u
u
1. The reset value is determined by the current configuration of the accessing initiator.
Fields
Field
Function
31-4
—
Reserved
3-0
DID
Domain Identifier
Indicates the DID of the requesting bus initiator.
19.8.3.5
Hardware Configuration 2 (HWCFG2)
Offset
Register
Offset
HWCFG2
F8h
Function
For initiators 0–31, indicates whether a given initiator has a built-in PID register as part of its programming model. If not, you must 
use the corresponding PIDm register to mimic the functionality of a built-in PID register.
Each bit corresponds to the same numbered initiator. For example, if PIDP18 is 1, bus initiator 18 has its own PID register. If 
PIDP18 is 0, then initiator 18 does not have its own PID register and you must use PID18.
Attempting to write to this register causes an error.
Access: Secure privileged read
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
728 / 5251


---
# 페이지 678

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
PIDP3
1 
PIDP3
0 
PIDP2
9 
PIDP2
8 
PIDP2
7 
PIDP2
6 
PIDP2
5 
PIDP2
4 
PIDP2
3 
PIDP2
2 
PIDP2
1 
PIDP2
0 
PIDP1
9 
PIDP1
8 
PIDP1
7 
PIDP1
6 
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
PIDP1
5 
PIDP1
4 
PIDP1
3 
PIDP1
2 
PIDP1
1 
PIDP1
0 
PIDP9 
PIDP8 
PIDP7 
PIDP6 
PIDP5 
PIDP4 
PIDP3 
PIDP2 
PIDP1 
PIDP0 
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
PIDPn
Process Identifier Present
0b - Does not have PID register
1b - Has PID register
19.8.3.6
Master Domain Assignment Configuration (MDACFG0 - MDACFG9)
Offset
For m = 0 to 9:
Register
Offset
MDACFGm
100h + (m × 1h)
Function
Indicates the number of implemented master domain assignment registers (MDA_Ww_m_DFMT0 or MDA_Ww_m_DFMT1) for 
initiator m, where m ranges from 0 to 63. You can read these registers using 8-, 16-, or 32-bit accesses.
If NMDAR is 0, the associated initiator does not exist.
Attempting to write to this register causes an error.
Access: Secure privileged read
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
729 / 5251


---
# 페이지 679

Diagram
Bits
7
6
5
4
3
2
1
0
R
NCM 
0
NMDAR 
W
Reset
See Register reset values.
Register reset values
Register
Reset value
MDACFG0
01h
MDACFG1–MDACFG2
81h
MDACFG3–MDACFG4
01h
MDACFG5
81h
MDACFG6
01h
MDACFG7
81h
MDACFG8
01h
MDACFG9
81h
Fields
Field
Function
7
NCM
Noncore Master
If NMDAR is greater than zero, indicates whether initiator m uses MDA_Ww_m_DFMT0 or 
MDA_Ww_m_DFMT1 to configure domain assignment.
This field is 0 for a non-existent initiator.
0b - Core initiator or initiator does not exist
1b - Noncore initiator
6-4
—
Reserved
3-0
NMDAR
Number Of Master Domain Assignment Registers
Indicates the number of master domain assignment registers (MDA_Ww_m_DFMT0 or 
MDA_Ww_m_DFMT1) associated with initiator m.
0000b - Initiator does not exist
0001b-1000b - Number of registers
All other values are reserved.
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
730 / 5251


---
# 페이지 680

19.8.3.7
Memory Region Configuration (MRCFG0 - MRCFG5)
Offset
Register
Offset
MRCFG0
140h
MRCFG1
141h
MRCFG2
142h
MRCFG3
143h
MRCFG4
144h
MRCFG5
145h
Function
Indicates the number of memory region descriptors (r) for MRCc, from 4 to 16 in increments of four, with 0 indicating a non-existent 
MRC. These registers are organized as byte-sized data arrays and can be read using 8-, 16-, or 32-bit accesses.
Attempting to write to this register causes an error.
Access: Secure Privileged Read
Diagram
Bits
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
NMRGD 
W
Reset
See Register reset values.
Register reset values
Register
Reset value
MRCFG0–MRCFG1
10h
MRCFG2
04h
MRCFG3
10h
MRCFG4
04h
MRCFG5
10h
Fields
Field
Function
7-5
—
Reserved
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
731 / 5251


---
# 페이지 681

Table continued from the previous page...
Field
Function
4-0
NMRGD
Number Of Memory Region Descriptors
Indicates the number of memory region descriptors associated with the MRC.
0_0000b - MRC does not exist
0_0100b - 4
0_1000b - 8
0_1100b - 12
1_0000b - 16
All other values are reserved.
19.8.3.8
Domain Error Location (DERRLOC0 - DERRLOC4)
Offset
Register
Offset
DERRLOC0
200h
DERRLOC1
204h
DERRLOC2
208h
DERRLOC3
20Ch
DERRLOC4
210h
Function
Indicates the MRC or PAC instance in domain d where an access violation has occurred. Each bit corresponds to the 
like-numbered instance. For more information, see Domain error capture management.
Attempting to write to this register causes an error.
Access: Secure privileged read
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
PACINST 
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
MRCINST 
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
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
732 / 5251


---
# 페이지 682

Fields
Field
Function
31-20
—
Reserved
19-16
PACINST
PAC Instance
Indicates the presence of a detected access violation for domain d in a PAC instance. Each bit corresponds 
to the instance index for the DERR_Ww_i registers: bit 16 of the register corresponds to the DERR_Ww_16 
registers, which show error information for PAC 0, and so on. Multiple bits can be 1 at any time, indicating 
access violations have been detected across multiple PACs.
For each bit in this field:
0b - No access violation error or the PAC instance is not physically present
1b - Access violation detected
15-0
MRCINST
MRC Instance
Indicates the presence of a detected access violation for domain d in an MRC instance. Each bit 
corresponds to the like-numbered MRC instance: bit 0 (bit 0 of the register) corresponds to MRC instance 
0, and so on. Multiple bits can be 1 at any time, indicating access violations have been detected across 
multiple MRCs.
For each bit in this field:
0b - No access violation error or the MRC instance is not physically present
1b - Access violation detected
19.8.3.9
Domain Error Word 0 (DERR_W0_0 - DERR_W0_18)
Offset
Register
Offset
DERR_W0_0
400h
DERR_W0_1
410h
DERR_W0_2
420h
DERR_W0_3
430h
DERR_W0_4
440h
DERR_W0_5
450h
DERR_W0_16
500h
DERR_W0_17
510h
DERR_W0_18
520h
Function
Indicates the address of an access violation detected by an MRC or a PAC, indexed by the MRC or PAC instance (i) that detected 
the violation, as indicated in DERRLOCd. This register is part of a 16-byte set:
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
733 / 5251


---
# 페이지 683

• DERR_W0_i: Word 0, the first 4 bytes
• DERR_W1_i: Word 1, the second 4 bytes
• Word 2, 4 reserved bytes
• DERR_W3_i: Word 3, the fourth 4 bytes
The first 16 sets (i from 0 to 15) are associated with MRCs and the rest (starting with i = 16) are associated with PACs. For more 
information, see Domain error capture management.
The error capture registers in the memory region controller and peripheral access controller submodules contain physical registers 
for each domain, but are organized in the DERR_Wn registers to provide the information for the requesting domain only. The 
registers return the error information for the domain id that is used to read the registers. When no error occurred for this domain 
id, it returns 0 data.
When the error capture logic is rearmed by writing the required data pattern to DERR_W3_n, this register is cleared.
When XRDC detects an access violation, it captures the error information and disables subsequent updates to the error capture 
registers until you write to DERR_W3_i.
 
If initiators with the same DID cause simultaneous error accesses, the error capture registers record only the error 
of the lowest target index.
  NOTE  
Attempting to write to this register causes an error. Attempting to read the error registers for a non-existent MRC or PAC instance 
causes an error.
Access: Secure privileged read
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
EADDR 
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
EADDR 
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
EADDR
Error Address
Indicates the target address of the first transaction that causes an access violation after reset or after 
rearming error capture.
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
734 / 5251


---
# 페이지 684

19.8.3.10
Domain Error Word 1 (DERR_W1_0 - DERR_W1_18)
Offset
Register
Offset
DERR_W1_0
404h
DERR_W1_1
414h
DERR_W1_2
424h
DERR_W1_3
434h
DERR_W1_4
444h
DERR_W1_5
454h
DERR_W1_16
504h
DERR_W1_17
514h
DERR_W1_18
524h
Function
Indicates the attributes of an access violation detected by an MRC or a PAC, indexed by the MRC or PAC instance (i) that detected 
the access violation, as indicated in DERRLOCd. For more information, see DERR_W0_i and Domain error capture management.
The error capture registers in the memory region controller and peripheral access controller submodules contain physical registers 
for each domain, but are organized in the DERR_Wn registers to provide the information for the requesting domain only. The 
registers return the error information for the domain id that is used to read the registers. When no error occurred for this domain 
id, it returns 0 data.
When the error capture logic is rearmed by writing the required data pattern to DERR_W3_n, this register is cleared.
 
If initiators with the same DID cause simultaneous error accesses, the error capture registers record only the error 
of the lowest target index.
  NOTE  
Attempting to write to this register causes an error. Attempting to read the error registers for a non-existent MRC or PAC instance 
causes an error.
Access: Secure privileged read
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
EST 
0
EPORT 
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
ERW 
EATR 
0
EDID 
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
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
735 / 5251


---
# 페이지 685

Fields
Field
Function
31-30
EST
Error State
Indicates the state of access violations for this domain in this instance of the MRC or PAC. After the first 
access violation to occur after reset or rearming of error capture, XRDC records subsequent errors as an 
overrun condition without any data captured.
00b-01b - No access violations detected
10b - A single access violation has been detected
11b - Multiple access violations have been detected
29-27
—
Reserved
26-24
EPORT
Error Port
Identifies the encoded port number of the MRC that detected the access violation. See the chip-specific 
configuration details for the MRC port connections. For access violations detected by a PAC, this field is 
zero.
23-12
—
Reserved
11
ERW
Error Read Or Write
Indicates whether the captured access violation occurred on a read or write access.
0b - Read access
1b - Write access
10-8
EATR
Error Attributes
Indicates attributes of the access violation.
000b - Secure user mode, instruction fetch access
001b - Secure user mode, data access
010b - Secure privileged mode, instruction fetch access
011b - Secure privileged mode, data access
100b - Nonsecure user mode, instruction fetch access
101b - Nonsecure user mode, data access
110b - Nonsecure privileged mode, instruction fetch access
111b - Nonsecure privileged mode, data access
7-4
—
Reserved
3-0
EDID
Error Domain Identifier
Indicates the DID of the access violation.
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
736 / 5251


---
# 페이지 686

19.8.3.11
Domain Error Word 3 (DERR_W3_0 - DERR_W3_18)
Offset
Register
Offset
DERR_W3_0
40Ch
DERR_W3_1
41Ch
DERR_W3_2
42Ch
DERR_W3_3
43Ch
DERR_W3_4
44Ch
DERR_W3_5
45Ch
DERR_W3_16
50Ch
DERR_W3_17
51Ch
DERR_W3_18
52Ch
Function
Rearms instance error capture, resets the error capture registers (DERR_W0_d, DERR_W1_d ), and deasserts the instance bit 
in DERRLOCd. After reading the access violation error information, an error handler must write 1 to RECR.
Register write only rearms error capture registers for the domain id that is used to write this register.
This register returns 0000h when read. Attempted reads of an MRC or PAC instance that is not physically present cause an error.
For more information, see Domain error capture management.
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
W
RECR 
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
RECR
Rearm Error Capture Registers
Resets and rearms the domain error capture registers for this instance, including deasserting the 
instance bit in DERRLOCd.
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
737 / 5251


---
# 페이지 687

Table continued from the previous page...
Field
Function
00b,10b,11b - No effect
01b - Rearms error capture, resets error capture registers, and deasserts instance bit in 
DERRLOCd
29-0
—
Reserved
19.8.3.12
Process Identifier (PID0 - PID8)
Offset
Register
Offset
PID0
700h
PID3
70Ch
PID4
710h
PID6
718h
PID8
720h
Function
Specifies the PID for the associated core initiator m.
Some cores contain a built-in PID register. If the core has a built-in PID register, XRDC populates the PID field with the value 
from the core PID register. If the core does not have the built-in register, the XRDC PID register allows applications to mimic PID 
operation for that core by writing the desired PID to the associated register.
HWCFG2 provides a bitmap of the implemented PIDm registers. Noncore initiators do not have an associated PID register.
For information about PID-based operation, see PID-based domain assignment.
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
LK2 
TSM 
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
PID 
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
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
738 / 5251


---
# 페이지 688

Fields
Field
Function
31
—
Reserved
30-29
LK2
Lock
Limits or prohibits writes to this register.
When you assert a bit in this field, it remains asserted until the next module reset.
If the core initiator has a built-in PID register, as indicated in HWCFG2, then a secure privileged read returns 
0 for this field.
00b,01b - Any secure privileged write
10b - Secure privileged writes from initiator only
11b - Locks
28
TSM
Three-State Model
Specifies that the core initiator supports only the three-state access control model. If you write 1 to this field, 
it remains asserted until the next reset.
For cores that support only the three-state access control model, you must assert this field before loading 
any nonsecure value into the PID.
See Generation of secure attribute.
27-6
—
Reserved
5-0
PID
Process Identifier
Specifies the transaction PID for the corresponding core initiator.
If the core has a built-in PID register, then a secure privileged read returns the core's PID register value.
Bit 5 specifies the secure attribute (0 = secure, 1 = nonsecure) for the transaction.
19.8.3.13
Master Domain Assignment (MDA_W0_0_DFMT0 - MDA_W0_8_DFMT0)
Offset
Register
Offset
MDA_W0_0_DFMT0
800h
MDA_W0_3_DFMT0
860h
MDA_W0_4_DFMT0
880h
MDA_W0_6_DFMT0
8C0h
MDA_W0_8_DFMT0
900h
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
739 / 5251


---
# 페이지 689

Function
Specifies the information used by the MDAC to assign a core bus initiator to a specific domain (DID). For more information, see 
Master domain assignment controller (MDAC).
Access: Secure privileged read/write
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
LK1 
DFMT 
0
0
0
PID 
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
PIDM 
PE 
DIDS 
0
DID 
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
Valid
Specifies whether this domain assignment is valid. In other words, if VLD and CR[GVLD] are both asserted, 
XRDC uses the configuration in this register in the domain assignment process. If CR[GVLD] is set to 1 and 
VLD is set to 0 then every transaction from this initiator will be assigned a DID of 0.
This field has no effect unless XRDC is enabled (CR[GVLD] = 1).
0b - Invalid
1b - Valid
30
LK1
Lock
Prohibits writes to this register.
• If unlocked, this register accepts any secure privileged write.
• If locked, you cannot write to this register and it remains read-only until after the next reset.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Unlocked
1b - Locks
When writing
0b - No effect
1b - Locks
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
740 / 5251


---
# 페이지 690

Table continued from the previous page...
Field
Function
29
DFMT
Domain Format
Indicates the domain assignment format.
0b - Core bus initiator domain assignment (DFMT0)
28
—
Reserved
27-24
—
Reserved
23-22
—
Reserved
21-16
PID
Process Identifier
Specifies the PID to be combined with the PIDM field and included in the domain assignment process. 
This field applies only if PID is enabled (PE = 1).
15-14
—
Reserved
13-8
PIDM
Process Identifier Mask
Specifies a mask applied to the PID to support including multiple PIDs in the domain hit determination. 
For each bit asserted in PIDM, the corresponding bit of the PID is ignored in the comparison. This field 
applies only if PID is enabled (PE = 1).
7-6
PE
Process Identifier Enable
Enables the optional inclusion of PID, qualified by PIDM, in the domain hit evaluation. This inclusion 
supports the definition of inclusive or exclusive sets of masked PID values.
00b-01b - No PID is included
10b - Partial domain hit = (PID & ~PIDM) == (PIDm[PID] & ~PIDM)
11b - Partial domain hit = ~((PID & ~PIDM) == (PIDm[PID] & ~PIDM))
5-4
DIDS
DID Select
Selects the source of the DID.
00b - Use the DID field of this register
01b - Use the input DID
10b - Concatenate bits 3–2 of this register with the least significant 2 bits of the input DID 
(DID_in[1:0])
11b - Reserved
3
Reserved
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
741 / 5251


---
# 페이지 691

Table continued from the previous page...
Field
Function
—
2-0
DID
Domain Identifier
Specifies the DID. DIDS controls whether and how this value is used.
19.8.3.14
Master Domain Assignment (MDA_W0_1_DFMT1 - MDA_W0_9_DFMT1)
Offset
Register
Offset
MDA_W0_1_DFMT1
820h
MDA_W0_2_DFMT1
840h
MDA_W0_5_DFMT1
8A0h
MDA_W0_7_DFMT1
8E0h
MDA_W0_9_DFMT1
920h
Function
Specifies the information used by the MDAC to assign a bus initiator to a specific domain (DID). For more information, see Master 
domain assignment controller (MDAC).
Access: Secure privileged read/write
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
LK1 
DFMT 
0
0
0
W
Reset
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
DIDB 
SA 
PA 
0
DID 
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
Valid
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
742 / 5251


---
# 페이지 692

Table continued from the previous page...
Field
Function
VLD
Specifies whether this domain assignment is valid. In other words, if VLD and CR[GVLD] are both asserted, 
XRDC uses the configuration in this register in the domain assignment process. If CR[GVLD] is set to 1 and 
VLD is set to 0 then every transaction from this initiator will be assigned a DID of 0.
This field has no effect unless XRDC is enabled (CR[GVLD] = 1).
0b - Invalid
1b - Valid
30
LK1
Lock
Prohibits writes to this register.
• If unlocked, this register accepts any secure privileged write.
• If locked, you cannot write to this register and it remains read-only until after the next reset.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Unlocked
1b - Locks
When writing
0b - No effect
1b - Locks
29
DFMT
Domain Format
Indicates the domain assignment format.
1b - Bus initiator domain assignment (DFMT1)
28
—
Reserved
27-24
—
Reserved
23-9
—
Reserved
8
DIDB
DID Bypass
Enables bypassing of an input DID as the domain identifier for this initiator. This capability allows noncore 
initiators (for example, a DMA) to appear as a core.
After this field is set to 1, it remains at that value until the next reset.
0b - Bypass DID input. Use DID
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
743 / 5251


---
# 페이지 693

Table continued from the previous page...
Field
Function
1b - Use DID input
7-6
SA
Secure Attribute
Specifies the secure attribute.
 
If SA = 1X or VLD = 0, use the secure attribute input from the initiator.
  NOTE  
00b - Force to secure
01b - Force to nonsecure
1xb - Use secure attribute from the initiator
5-4
PA
Privileged Attribute
Specifies the privileged (supervisor/user) attribute.
 
If PA = 1X or VLD = 0, use the privileged attribute input from the initiator.
  NOTE  
00b - Force to user
01b - Force to privileged
1xb - Use privileged attribute from the initiator
3
—
Reserved
2-0
DID
Domain Identifier
Specifies the DID.
19.8.3.15
Peripheral Domain Access Control Word 0 (PDAC_W0_2 - PDAC_W0_347)
Offset
Register
Offset
PDAC_W0_2
1010h
PDAC_W0_3
1018h
PDAC_W0_28
10E0h
PDAC_W0_32
1100h
PDAC_W0_33
1108h
PDAC_W0_34
1110h
PDAC_W0_35
1118h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
744 / 5251


---
# 페이지 694

Table continued from the previous page...
Register
Offset
PDAC_W0_36
1120h
PDAC_W0_38
1130h
PDAC_W0_39
1138h
PDAC_W0_40
1140h
PDAC_W0_41
1148h
PDAC_W0_42
1150h
PDAC_W0_44
1160h
PDAC_W0_45
1168h
PDAC_W0_46
1170h
PDAC_W0_47
1178h
PDAC_W0_49
1188h
PDAC_W0_50
1190h
PDAC_W0_51
1198h
PDAC_W0_52
11A0h
PDAC_W0_128
1400h
PDAC_W0_129
1408h
PDAC_W0_130
1410h
PDAC_W0_131
1418h
PDAC_W0_132
1420h
PDAC_W0_133
1428h
PDAC_W0_134
1430h
PDAC_W0_135
1438h
PDAC_W0_136
1440h
PDAC_W0_137
1448h
PDAC_W0_138
1450h
PDAC_W0_139
1458h
PDAC_W0_140
1460h
PDAC_W0_141
1468h
PDAC_W0_142
1470h
PDAC_W0_143
1478h
PDAC_W0_144
1480h
PDAC_W0_145
1488h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
745 / 5251


---
# 페이지 695

Table continued from the previous page...
Register
Offset
PDAC_W0_146
1490h
PDAC_W0_147
1498h
PDAC_W0_148
14A0h
PDAC_W0_149
14A8h
PDAC_W0_151
14B8h
PDAC_W0_152
14C0h
PDAC_W0_153
14C8h
PDAC_W0_154
14D0h
PDAC_W0_155
14D8h
PDAC_W0_156
14E0h
PDAC_W0_157
14E8h
PDAC_W0_158
14F0h
PDAC_W0_159
14F8h
PDAC_W0_160
1500h
PDAC_W0_161
1508h
PDAC_W0_162
1510h
PDAC_W0_163
1518h
PDAC_W0_164
1520h
PDAC_W0_165
1528h
PDAC_W0_166
1530h
PDAC_W0_167
1538h
PDAC_W0_168
1540h
PDAC_W0_169
1548h
PDAC_W0_170
1550h
PDAC_W0_171
1558h
PDAC_W0_173
1568h
PDAC_W0_175
1578h
PDAC_W0_177
1588h
PDAC_W0_178
1590h
PDAC_W0_179
1598h
PDAC_W0_180
15A0h
PDAC_W0_181
15A8h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
746 / 5251


---
# 페이지 696

Table continued from the previous page...
Register
Offset
PDAC_W0_182
15B0h
PDAC_W0_183
15B8h
PDAC_W0_184
15C0h
PDAC_W0_185
15C8h
PDAC_W0_186
15D0h
PDAC_W0_187
15D8h
PDAC_W0_188
15E0h
PDAC_W0_189
15E8h
PDAC_W0_190
15F0h
PDAC_W0_191
15F8h
PDAC_W0_192
1600h
PDAC_W0_193
1608h
PDAC_W0_194
1610h
PDAC_W0_195
1618h
PDAC_W0_196
1620h
PDAC_W0_197
1628h
PDAC_W0_198
1630h
PDAC_W0_199
1638h
PDAC_W0_200
1640h
PDAC_W0_201
1648h
PDAC_W0_202
1650h
PDAC_W0_203
1658h
PDAC_W0_204
1660h
PDAC_W0_205
1668h
PDAC_W0_206
1670h
PDAC_W0_207
1678h
PDAC_W0_208
1680h
PDAC_W0_209
1688h
PDAC_W0_210
1690h
PDAC_W0_211
1698h
PDAC_W0_212
16A0h
PDAC_W0_213
16A8h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
747 / 5251


---
# 페이지 697

Table continued from the previous page...
Register
Offset
PDAC_W0_214
16B0h
PDAC_W0_215
16B8h
PDAC_W0_216
16C0h
PDAC_W0_217
16C8h
PDAC_W0_219
16D8h
PDAC_W0_220
16E0h
PDAC_W0_221
16E8h
PDAC_W0_223
16F8h
PDAC_W0_224
1700h
PDAC_W0_225
1708h
PDAC_W0_226
1710h
PDAC_W0_227
1718h
PDAC_W0_229
1728h
PDAC_W0_230
1730h
PDAC_W0_231
1738h
PDAC_W0_232
1740h
PDAC_W0_233
1748h
PDAC_W0_234
1750h
PDAC_W0_235
1758h
PDAC_W0_236
1760h
PDAC_W0_238
1770h
PDAC_W0_240
1780h
PDAC_W0_241
1788h
PDAC_W0_242
1790h
PDAC_W0_243
1798h
PDAC_W0_244
17A0h
PDAC_W0_245
17A8h
PDAC_W0_246
17B0h
PDAC_W0_247
17B8h
PDAC_W0_248
17C0h
PDAC_W0_249
17C8h
PDAC_W0_250
17D0h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
748 / 5251


---
# 페이지 698

Table continued from the previous page...
Register
Offset
PDAC_W0_251
17D8h
PDAC_W0_252
17E0h
PDAC_W0_253
17E8h
PDAC_W0_254
17F0h
PDAC_W0_255
17F8h
PDAC_W0_256
1800h
PDAC_W0_257
1808h
PDAC_W0_258
1810h
PDAC_W0_259
1818h
PDAC_W0_260
1820h
PDAC_W0_261
1828h
PDAC_W0_262
1830h
PDAC_W0_263
1838h
PDAC_W0_264
1840h
PDAC_W0_265
1848h
PDAC_W0_266
1850h
PDAC_W0_267
1858h
PDAC_W0_268
1860h
PDAC_W0_269
1868h
PDAC_W0_270
1870h
PDAC_W0_271
1878h
PDAC_W0_272
1880h
PDAC_W0_273
1888h
PDAC_W0_274
1890h
PDAC_W0_275
1898h
PDAC_W0_276
18A0h
PDAC_W0_277
18A8h
PDAC_W0_278
18B0h
PDAC_W0_279
18B8h
PDAC_W0_280
18C0h
PDAC_W0_281
18C8h
PDAC_W0_282
18D0h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
749 / 5251


---
# 페이지 699

Table continued from the previous page...
Register
Offset
PDAC_W0_283
18D8h
PDAC_W0_284
18E0h
PDAC_W0_285
18E8h
PDAC_W0_286
18F0h
PDAC_W0_287
18F8h
PDAC_W0_289
1908h
PDAC_W0_290
1910h
PDAC_W0_291
1918h
PDAC_W0_292
1920h
PDAC_W0_293
1928h
PDAC_W0_294
1930h
PDAC_W0_295
1938h
PDAC_W0_296
1940h
PDAC_W0_297
1948h
PDAC_W0_298
1950h
PDAC_W0_303
1978h
PDAC_W0_304
1980h
PDAC_W0_307
1998h
PDAC_W0_311
19B8h
PDAC_W0_314
19D0h
PDAC_W0_315
19D8h
PDAC_W0_318
19F0h
PDAC_W0_319
19F8h
PDAC_W0_320
1A00h
PDAC_W0_321
1A08h
PDAC_W0_323
1A18h
PDAC_W0_324
1A20h
PDAC_W0_325
1A28h
PDAC_W0_326
1A30h
PDAC_W0_328
1A40h
PDAC_W0_329
1A48h
PDAC_W0_330
1A50h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
750 / 5251


---
# 페이지 700

Table continued from the previous page...
Register
Offset
PDAC_W0_331
1A58h
PDAC_W0_332
1A60h
PDAC_W0_333
1A68h
PDAC_W0_334
1A70h
PDAC_W0_335
1A78h
PDAC_W0_337
1A88h
PDAC_W0_338
1A90h
PDAC_W0_339
1A98h
PDAC_W0_340
1AA0h
PDAC_W0_341
1AA8h
PDAC_W0_342
1AB0h
PDAC_W0_343
1AB8h
PDAC_W0_344
1AC0h
PDAC_W0_345
1AC8h
PDAC_W0_346
1AD0h
PDAC_W0_347
1AD8h
Function
In conjunction with PDAC_W1_s, specifies the ACP configuration for peripheral slot s. The ACP controls access to the 
peripheral by all initiators within the domain. For the available ACPs, see Domain ACP specification. For more information, see 
Peripheral access controller (PAC).
Access: Secure privileged read/write
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
SE 
0
SNUM 
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
D4ACP 
D3ACP 
D2ACP 
D1ACP 
D0ACP 
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
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
751 / 5251


---
# 페이지 701

Fields
Field
Function
31
—
Reserved
30
SE
Semaphore Enable
Enables the inclusion of the semaphore specified in SNUM in the DdACP evaluation.
0b - Disables
1b - Enables
29-28
—
Reserved
27-24
SNUM
Semaphore Number
Specifies the hardware semaphore to include in the DdACP access evaluation. This field applies only if 
you enable semaphore (write 1 to SE).
23-15
—
Reserved
14-12: D4ACP
11-9: D3ACP
8-6: D2ACP
5-3: D1ACP
2-0: D0ACP
Domain Access Control Policy
Specifies the ACP for the associated domain. This field applies only for a supported DID; if the DID 
is not implemented, the field is read-only zero (no access rights). For field values, see Domain ACP 
specification.
19.8.3.16
Peripheral Domain Access Control Word 1 (PDAC_W1_2 - PDAC_W1_347)
Offset
Register
Offset
PDAC_W1_2
1014h
PDAC_W1_3
101Ch
PDAC_W1_28
10E4h
PDAC_W1_32
1104h
PDAC_W1_33
110Ch
PDAC_W1_34
1114h
PDAC_W1_35
111Ch
PDAC_W1_36
1124h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
752 / 5251


---
# 페이지 702

Table continued from the previous page...
Register
Offset
PDAC_W1_38
1134h
PDAC_W1_39
113Ch
PDAC_W1_40
1144h
PDAC_W1_41
114Ch
PDAC_W1_42
1154h
PDAC_W1_44
1164h
PDAC_W1_45
116Ch
PDAC_W1_46
1174h
PDAC_W1_47
117Ch
PDAC_W1_49
118Ch
PDAC_W1_50
1194h
PDAC_W1_51
119Ch
PDAC_W1_52
11A4h
PDAC_W1_128
1404h
PDAC_W1_129
140Ch
PDAC_W1_130
1414h
PDAC_W1_131
141Ch
PDAC_W1_132
1424h
PDAC_W1_133
142Ch
PDAC_W1_134
1434h
PDAC_W1_135
143Ch
PDAC_W1_136
1444h
PDAC_W1_137
144Ch
PDAC_W1_138
1454h
PDAC_W1_139
145Ch
PDAC_W1_140
1464h
PDAC_W1_141
146Ch
PDAC_W1_142
1474h
PDAC_W1_143
147Ch
PDAC_W1_144
1484h
PDAC_W1_145
148Ch
PDAC_W1_146
1494h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
753 / 5251


---
# 페이지 703

Table continued from the previous page...
Register
Offset
PDAC_W1_147
149Ch
PDAC_W1_148
14A4h
PDAC_W1_149
14ACh
PDAC_W1_151
14BCh
PDAC_W1_152
14C4h
PDAC_W1_153
14CCh
PDAC_W1_154
14D4h
PDAC_W1_155
14DCh
PDAC_W1_156
14E4h
PDAC_W1_157
14ECh
PDAC_W1_158
14F4h
PDAC_W1_159
14FCh
PDAC_W1_160
1504h
PDAC_W1_161
150Ch
PDAC_W1_162
1514h
PDAC_W1_163
151Ch
PDAC_W1_164
1524h
PDAC_W1_165
152Ch
PDAC_W1_166
1534h
PDAC_W1_167
153Ch
PDAC_W1_168
1544h
PDAC_W1_169
154Ch
PDAC_W1_170
1554h
PDAC_W1_171
155Ch
PDAC_W1_173
156Ch
PDAC_W1_175
157Ch
PDAC_W1_177
158Ch
PDAC_W1_178
1594h
PDAC_W1_179
159Ch
PDAC_W1_180
15A4h
PDAC_W1_181
15ACh
PDAC_W1_182
15B4h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
754 / 5251


---
# 페이지 704

Table continued from the previous page...
Register
Offset
PDAC_W1_183
15BCh
PDAC_W1_184
15C4h
PDAC_W1_185
15CCh
PDAC_W1_186
15D4h
PDAC_W1_187
15DCh
PDAC_W1_188
15E4h
PDAC_W1_189
15ECh
PDAC_W1_190
15F4h
PDAC_W1_191
15FCh
PDAC_W1_192
1604h
PDAC_W1_193
160Ch
PDAC_W1_194
1614h
PDAC_W1_195
161Ch
PDAC_W1_196
1624h
PDAC_W1_197
162Ch
PDAC_W1_198
1634h
PDAC_W1_199
163Ch
PDAC_W1_200
1644h
PDAC_W1_201
164Ch
PDAC_W1_202
1654h
PDAC_W1_203
165Ch
PDAC_W1_204
1664h
PDAC_W1_205
166Ch
PDAC_W1_206
1674h
PDAC_W1_207
167Ch
PDAC_W1_208
1684h
PDAC_W1_209
168Ch
PDAC_W1_210
1694h
PDAC_W1_211
169Ch
PDAC_W1_212
16A4h
PDAC_W1_213
16ACh
PDAC_W1_214
16B4h
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
755 / 5251


---
# 페이지 705

Table continued from the previous page...
Register
Offset
PDAC_W1_215
16BCh
PDAC_W1_216
16C4h
PDAC_W1_217
16CCh
PDAC_W1_219
16DCh
PDAC_W1_220
16E4h
PDAC_W1_221
16ECh
PDAC_W1_223
16FCh
PDAC_W1_224
1704h
PDAC_W1_225
170Ch
PDAC_W1_226
1714h
PDAC_W1_227
171Ch
PDAC_W1_229
172Ch
PDAC_W1_230
1734h
PDAC_W1_231
173Ch
PDAC_W1_232
1744h
PDAC_W1_233
174Ch
PDAC_W1_234
1754h
PDAC_W1_235
175Ch
PDAC_W1_236
1764h
PDAC_W1_238
1774h
PDAC_W1_240
1784h
PDAC_W1_241
178Ch
PDAC_W1_242
1794h
PDAC_W1_243
179Ch
PDAC_W1_244
17A4h
PDAC_W1_245
17ACh
PDAC_W1_246
17B4h
PDAC_W1_247
17BCh
PDAC_W1_248
17C4h
PDAC_W1_249
17CCh
PDAC_W1_250
17D4h
PDAC_W1_251
17DCh
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
756 / 5251


---
# 페이지 706

Table continued from the previous page...
Register
Offset
PDAC_W1_252
17E4h
PDAC_W1_253
17ECh
PDAC_W1_254
17F4h
PDAC_W1_255
17FCh
PDAC_W1_256
1804h
PDAC_W1_257
180Ch
PDAC_W1_258
1814h
PDAC_W1_259
181Ch
PDAC_W1_260
1824h
PDAC_W1_261
182Ch
PDAC_W1_262
1834h
PDAC_W1_263
183Ch
PDAC_W1_264
1844h
PDAC_W1_265
184Ch
PDAC_W1_266
1854h
PDAC_W1_267
185Ch
PDAC_W1_268
1864h
PDAC_W1_269
186Ch
PDAC_W1_270
1874h
PDAC_W1_271
187Ch
PDAC_W1_272
1884h
PDAC_W1_273
188Ch
PDAC_W1_274
1894h
PDAC_W1_275
189Ch
PDAC_W1_276
18A4h
PDAC_W1_277
18ACh
PDAC_W1_278
18B4h
PDAC_W1_279
18BCh
PDAC_W1_280
18C4h
PDAC_W1_281
18CCh
PDAC_W1_282
18D4h
PDAC_W1_283
18DCh
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
757 / 5251


---
# 페이지 707

Table continued from the previous page...
Register
Offset
PDAC_W1_284
18E4h
PDAC_W1_285
18ECh
PDAC_W1_286
18F4h
PDAC_W1_287
18FCh
PDAC_W1_289
190Ch
PDAC_W1_290
1914h
PDAC_W1_291
191Ch
PDAC_W1_292
1924h
PDAC_W1_293
192Ch
PDAC_W1_294
1934h
PDAC_W1_295
193Ch
PDAC_W1_296
1944h
PDAC_W1_297
194Ch
PDAC_W1_298
1954h
PDAC_W1_303
197Ch
PDAC_W1_304
1984h
PDAC_W1_307
199Ch
PDAC_W1_311
19BCh
PDAC_W1_314
19D4h
PDAC_W1_315
19DCh
PDAC_W1_318
19F4h
PDAC_W1_319
19FCh
PDAC_W1_320
1A04h
PDAC_W1_321
1A0Ch
PDAC_W1_323
1A1Ch
PDAC_W1_324
1A24h
PDAC_W1_325
1A2Ch
PDAC_W1_326
1A34h
PDAC_W1_328
1A44h
PDAC_W1_329
1A4Ch
PDAC_W1_330
1A54h
PDAC_W1_331
1A5Ch
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
758 / 5251


---
# 페이지 708

Table continued from the previous page...
Register
Offset
PDAC_W1_332
1A64h
PDAC_W1_333
1A6Ch
PDAC_W1_334
1A74h
PDAC_W1_335
1A7Ch
PDAC_W1_337
1A8Ch
PDAC_W1_338
1A94h
PDAC_W1_339
1A9Ch
PDAC_W1_340
1AA4h
PDAC_W1_341
1AACh
PDAC_W1_342
1AB4h
PDAC_W1_343
1ABCh
PDAC_W1_344
1AC4h
PDAC_W1_345
1ACCh
PDAC_W1_346
1AD4h
PDAC_W1_347
1ADCh
Function
In conjunction with PDAC_W0_s, specifies the ACP configuration for peripheral slot s.
Access: Secure privileged read/write
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
LK2 
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
Valid
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
759 / 5251


---
# 페이지 709

Table continued from the previous page...
Field
Function
VLD
Specifies whether this domain assignment is valid. In other words, if VLD and CR[GVLD] are both asserted, 
XRDC uses the configuration in this pair of registers. If either CR[GVLD] or this field is 0, all accesses to 
the peripheral are allowed. To support a coherent register state, any write to PDAC_W0_s forces this field 
to zero.
This field has no effect unless XRDC is enabled (CR[GVLD] = 1).
0b - Invalid
1b - Valid
30-29
LK2
Lock
Limits or prohibits writes to the set of PDAC words (PDAC_W0_s and PDAC_W1_s) for this peripheral slot.
When you assert a bit in this field, it remains asserted until the next module reset.
00b-01b - Both words can be written to
10b - Domain d can update only its associated DdACP field—all other fields are read-only
11b - Locks (both words are read-only)
28-24
—
Reserved
23-0
—
Reserved
19.8.3.17
Memory Region Descriptor Word 0 (MRGD_W0_0 - MRGD_W0_95)
Offset
Registers in this array exist only for the following combinations of index values.
Index n
Index m
0–1, 3, 5
0–15
2, 4
0–3
Register
Offset
MRGD_W0_(n * 16 + m)
2000h + (n × 200h) + (m × 20h)
Function
Specifies the starting address of memory region r.
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
760 / 5251


---
# 페이지 710

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
SRTADDR 
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
SRTADDR 
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
1
Fields
Field
Function
31-5
SRTADDR
Start Address
Specifies the most significant bits of the 0-modulo 32-byte start address of the memory region. The minimum 
region size is 32 bytes.
4-0
—
Reserved
19.8.3.18
Memory Region Descriptor Word 1 (MRGD_W1_0 - MRGD_W1_95)
Offset
Registers in this array exist only for the following combinations of index values.
Index n
Index m
0–1, 3, 5
0–15
2, 4
0–3
Register
Offset
MRGD_W1_(n * 16 + m)
2004h + (n × 200h) + (m × 20h)
Function
Specifies the ending address of memory region r.
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
761 / 5251


---
# 페이지 711

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
ENDADDR 
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
ENDADDR 
1
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
1
1
1
1
1
Fields
Field
Function
31-5
ENDADDR
End Address
Specifies the most significant bits of the 31-modulo 32-byte end address of memory region r.
4-0
—
Reserved
19.8.3.19
Memory Region Descriptor Word 2 (MRGD_W2_0 - MRGD_W2_95)
Offset
Registers in this array exist only for the following combinations of index values.
Index n
Index m
0–1, 3, 5
0–15
2, 4
0–3
Register
Offset
MRGD_W2_(n * 16 + m)
2008h + (n × 200h) + (m × 20h)
Function
Specifies the ACP for the associated domain. The encodings specify read and write access capabilities based on the four 
operating states. This field applies only for a supported DID; if the DID is not implemented, the field is read-only zero (no 
access rights).
For field values, see Domain ACP specification.
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
762 / 5251


---
# 페이지 712

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
SE 
0
SNUM 
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
D4ACP 
D3ACP 
D2ACP 
D1ACP 
D0ACP 
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
SE
Semaphore Enable
Enables the inclusion of the semaphore specified in SNUM in the DdACP evaluation.
0b - Disables
1b - Enables
29-28
—
Reserved
27-24
SNUM
Semaphore Number
Specifies the hardware semaphore to include in the DdACP access evaluation. This field applies only if 
you enable semaphore (write 1 to SE).
23-15
—
Reserved
14-12: D4ACP
11-9: D3ACP
8-6: D2ACP
5-3: D1ACP
2-0: D0ACP
Domain Access Control Policy
Specifies the ACP for the associated domain. This field applies only for a supported DID; if the DID 
is not implemented, the field is read-only zero (no access rights). For field values, see Domain ACP 
specification.
19.8.3.20
Memory Region Descriptor Word 3 (MRGD_W3_0 - MRGD_W3_95)
Offset
Registers in this array exist only for the following combinations of index values.
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
763 / 5251


---
# 페이지 713

Index n
Index m
0–1, 3, 5
0–15
2, 4
0–3
Register
Offset
MRGD_W3_(n * 16 + m)
200Ch + (n × 200h) + (m × 20h)
Function
Specifies whether this memory region descriptor is enabled and limits or prohibits writes to it.
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
LK2 
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
VLD
Valid
Specifies whether this domain assignment is valid. In other words, if VLD and CR[GVLD] are both asserted, 
XRDC uses the configuration in this set of registers. If CR[GVLD] is 0, all accesses to the memory are 
allowed. If CR[GVLD] is 1 and VLD is 0, all accesses are blocked. To support a coherent register state, a 
write to any of the MRGD W0–W2 registers forces this field to zero.
This field has no effect unless XRDC is enabled (CR[GVLD] = 1).
0b - Invalid
1b - Valid
30-29
LK2
Lock
Limits or prohibits writes to the set of MRGD words (MRGD_Ww_r) for this memory region.
When you assert a bit in this field, it remains asserted until the next module reset.
00b - All words in the set can be written to
01b - Reserved
Table continues on the next page...
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
764 / 5251


---
# 페이지 714

Table continued from the previous page...
Field
Function
10b - Domain d can update only its associated DdACP field; all other fields are read-only
11b - Locks (all words are read-only)
28-24
—
Reserved
23-0
—
Reserved
19.9 Glossary
ACP
access control policy. The access limitations specified for memory and peripheral resources.
DID
domain identifier. A numeric value that identifies a specific domain.
domain
An access-controlled virtual group of on-chip initiators (cores and noncore initiators) and targets (memories and 
peripherals) that comprise an isolated computing environment. All initiators in a domain have the same access to 
chip resources within that domain.
See Introduction to domains for more information.
initiator
A processor core or non-processor module, such as DMA or a communications channel, that can initiate 
transactions with memory and peripheral resources. This term replaces "master".
LPID
logical partition identifier. Also called an operating system ID or VMID, the LPID identifies a virtual initiator (either 
core or noncore) that runs on a hypervisor.
MDAC
Master Domain Assignment Controller. Manages resource assignments and DIDs.
MGR
Manager. Manages accesses through the XRDC programming model.
MRC
Memory Region Controller. Controls access to memories based on memory region descriptors.
PAC
Peripheral Access Controller (also sometimes called PDAC). Controls access to peripherals.
PDAC
See PAC.
PID
process identifier. A numeric value provided by some core processors to identify the currently active process.
SDAC
Deprecated. See MRC.
target
A peripheral or memory resource that one or more initiators can access. This term replaces "slave".
transaction A read or write request made by an initiator to a target peripheral or memory.
VMID
virtual machine identifier. See LPID.
NXP Semiconductors
Extended Resource Domain Controller (XRDC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
765 / 5251


---
