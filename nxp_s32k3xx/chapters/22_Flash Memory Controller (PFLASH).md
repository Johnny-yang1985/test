Chapter 22
Flash Memory Controller (PFLASH)
22.1 Chip-specific PFLASH information
22.1.1 Flash memory architecture
The flash memory on the chip consists of a flash memory controller and a flash memory array module. The flash memory controller 
provides flash–memory configuration and control functions and manages the interface between the flash memory array and the 
chip's crossbar switch.
This chip implements upto four 64-bit AHB buses.
Core 0
Port 0
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
Core 1/ Core 3**
Flash memory array
Port 1
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
All other masters
Port 2*
Core 2
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
Port 3*
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
* This port does not exist on S32K311 and S32K312
** This core is only available in S32K388
Figure 53. Flash memory architecture
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
845 / 5251


---
# 페이지 81

Core 0 / Core2
PFC0
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
Core 0 / Core 2
Flash_0 memory array
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
and all other masters
Core 1 / Core3
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
256 + 32 bit
buffer
(Port 0)
PFC0
(Port 1)
PFC1
(Port 0)
PFC1
(Port 1)
Core 1 / Core3
and all other masters
Flash_1 memory array
Figure 54. Flash memory architecture (S32K389)
22.1.2 Flash memory controller
The flash memory controller:
• Acts as an interface between the system bus and flash memory array.
• Is a triple-ported controller with a dedicated line buffering per port and per master ID. This enables you to use the line buffers 
more efficiently because various masters have dedicated buffers that are not compromised when other masters perform 
read operations.
Also, by having separate ports, you can have separate connections for each CPU instruction bus and a single port for all data 
accesses as shown in Figure 53.
In general, the flash memory controller registers affect the global flash memory behavior (for example, read buffering and 
access control).
 
In S32K311, S32K312, and S32K342:
• PFLASH block 3 and block 4 are not present, so both the sector and super sector registers are not available.
• For PFLASH block 2, the super sector registers are not available.
  NOTE  
S32K389 supports the following flash operations:
• Single read, per controller
• Dual read, per controller
• Parallel single read, two controllers
• Parallel dual read, two controllers
 
Only parallel dual-read is supported. Quad-read in a single controller, parallel quad-read is no supported.
  NOTE  
22.1.2.1
Dual Flash memory controller architecture (for S32K389)
As shown in Figure 55, the device implements two flash controllers with two separate ports.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
846 / 5251


---
# 페이지 82

• PFC0: 8MB C-Flash (4x blocks of 2MB) + 256KB D-Flash
• PFC1: 4MB C-Flash (4x blocks of 1MB)
 
See the “Flash memory read timing parameters” specification in the product data-sheet for the required RWSC 
(read wait-state control) settings according to the Flash frequency of operation (for each flash).
  NOTE  
Natively, both flash controllers map their access requests to addresses starting from “0x40_0000” (see “PHYSICAL” purple box 
in the left side of the Figure 55). However, the device implements a FAR “Flash Address Remapping” logic for translating the 
addresses from a continuous memory map (see “USER” green box in the right side of the Figure 55) to the corresponding 
physical ones.
In other words, the overall system memory map remains continuous, from the user perspective, and each time a system master 
requests certain address, it is internally remapped to the one that the controller can natively understand.
 
See, table “Flash block configuration (S32K389)” in "Embedded Flash Memory (c40asf)" chapter for more details 
about the physical address range of each flash.
  NOTE  
Figure 55. Flash Address Remapping (FAR) for S32K389
22.1.3 ECC error handling on data flash block (for S32K389)
As explained in Dual Flash memory controller architecture (for S32K389), each time a system master requests certain address, 
it is internally remapped to the one that the controller can natively understand.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
847 / 5251


---
# 페이지 83

In the scenario, where ECC error occurs, the flash controllers detect and send two parameters to the ERM to be latched.
1. Type: single-bit or multi-bit error
2. Error address (for both code and data blocks).
However, the reporting of the second one (error address) is based on the physical address (not the system logic address). Hence, 
in order to correctly interpret this information, the application software needs to perform this translation. See section "ECC error 
address remapping (S32K389)" in the "Error Reporting Module (ERM)" chapter.
22.1.4 Platform flash configuration registers (PFCRn)
The table below defines the PFCRn fields that the chip uses.
Table 110. Platform flash configuration registers (PFCRn)
Master
Buffer enable field
Prefetch enable field
Cortex–M7_0
P0_CBFEN, P0_DBFEN
P0_CPFEN, P0_DPFEN
eDMA + HSE_B + EMAC1 + GMAC_02 + GMAC_1
P1_CBFEN, P1_DBFEN
P1_CPFEN, P1_DPFEN
Cortex–M7_1 + Cortex-M7_33
P2_CBFEN, P2_DBFEN
P2_CPFEN, P2_DPFEN
Cortex–M7_2
P3_CBFEN, P3_DBFEN
P3_CPFEN, P3_DPFEN
S32K389:
Cortex-M7_0, Cortex-M7_2
PF0_P0_CBFEN, 
PF0_P0_DBFEN, 
PF1_P0_CBFEN, 
PF1_P0_DBFEN
PF0_P0_CPFEN, 
PF0_P0_DPFEN,PF1_P0_CP
FEN, PF1_P0_DPFEN
S32K389:
Cortex-M7_1, Cortex_M7_3, eDMA, HSE,GMAC_0, GMAC_1
PF0_P1_CBFEN, 
PF0_P1_DBFEN, 
PF1_P1_CBFEN, 
PF1_P1_DBFEN
PF0_P1_CPFEN, 
PF0_P1_DPFEN,PF1_P1_CP
FEN, PF1_P1_DPFEN
1. S32K358, S32K388, S32K389, S32K312, S32K311, and S32K310 do not support EMAC.
2. Only available in S32K358, and S32K388.
3. Only available in S32K388.
22.1.5 Platform flash access protection register (PFAPR)
This table defines the PFAPR[MnAP] fields that the chip uses. This chip does not use the other master access protection fields, 
but those fields are readable and writable.
Table 111. Platform flash access protection register (PFAPR)
Master number
Master name
Access protection field
0
Cortex–M7_0 AHBM
M0AP
1
Cortex–M7_1 AHBM
M1AP
2
eDMA
M2AP
3
HSE
M3AP
4
EMAC/GMAC_0
M4AP
5
Cortex–M7_3 AHBM
M5AP
6
uSDHC/ GMAC_1
M6AP
7
Cortex–M7_2 AHBM
M7AP
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
848 / 5251


---
# 페이지 84

Table 111. Platform flash access protection register (PFAPR) (continued)
Master number
Master name
Access protection field
8
ACE_ACCEL RESULT
M8AP
9
ACE_ACCEL FEED
M9AP
22.2 Overview
PFLASH acts as an interface between the system bus (AHB-Lite 2.v6) and flash memory array. 
PFLASH supports three 64-bit AHB buses and a 256-bit read data interface from each flash memory array. The slave port 
assignments and buffer organization are organized to offer maximum performance of code execution in a multicore architecture. 
The buffer mechanism serves to deliver flash memory read data with zero-wait state response on lines that reside in cache. 
AHB requests that miss the prefetch cache generate the needed flash memory array access and are forwarded to the AHB upon 
completion. Each cache entry is 256 bits, matching the flash memory array page size and providing 512 bytes of high-speed 
local storage.
22.2.1 Block diagrams
The following figure provides a block diagram showing PFLASH and the attached flash memory array.
Arm Cortex-M
processor
AMBA-AHB
AXBS
Flash
memory
Memory
PFLASH
System
RAM
Figure 56. Platform-centric simple block diagram with PFLASH
22.2.2 Features
• Four 64-bit AHB interface ports (p0, p1, p2, p3) allowing simultaneous access to dedicated prefetch mini-cache per slave 
port
• 256-bit read data bus and 64-bit write data bus
• Configurable read buffering and line prefetching support via a mini-cache, plus a prefetch controller for each AHB port to 
provide single-cycle buffer hit read response
• Configurable access control based on read/write and AHB master ID attributes
• Support for reporting single-bit and multi-bit flash memory ECC events on a 64-bit doubleword boundary
22.3 Functional description
As shown in Figure 56, PFLASH interfaces between:
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
849 / 5251


---
# 페이지 85

• The AHB system bus port
• The flash memory array
For accesses targeting flash memory, the PFLASH generates as inputs to the flash memory array:
• Read and write enables
• Block selects
• Array address
• Write size
• Write data
PFLASH captures read data from the flash memory array and drives it onto the AHB system bus. Up to four pages of data (256-bit 
page size) may be buffered in each prefetch buffer for AHB Port0, Port1, and Port2. and Port 3. Lines may be prefetched in 
advance of being requested, allowing single-cycle (zero AHB wait-states) read data responses on buffer hits.
Access protections may be applied on a per-master basis for both reads and writes to support security and privilege mechanisms.
22.3.1 Read transactions
On an incoming AHB read request, a mini-cache lookup and access privilege evaluation are performed during the AHB address 
phase. If a buffer hit occurs, the requested data is retrieved from the previously loaded prefetch buffer entry and returned on the 
system bus with a zero wait-state response. If a buffer miss occurs, a flash memory access is initiated.
Read accesses are terminated under control of the appropriate wait state settings. Access timing can be varied to account for the 
operating conditions of the chip (for example, frequency, voltage, temperature, and so on) by appropriately setting the read wait 
state field in flash memory.
22.3.2 Write transactions
An interlock write on a program or erase sequence is initiated by first writing to Platform Flash Memory Program Erase Address 
Logical (PFCPGM_PEADR_L), Platform Flash Memory Express Program Erase Address Logical (PFCPGM_XPEADR_L)(see the 
Flash Memory chapter for write sequence details).
22.3.3 Access protections
22.3.3.1
PFAPR
PFLASH provides programmable, configurable access protections for read cycles on a per-master basis in PFAPR[MnAP]. This 
field restricts read access on a per-master basis. This functionality is described in Platform Flash Memory Access Protection 
(PFAPR). Detection of a protection violation based on PFAPR settings results in an error response from PFLASH on the 
AHB transfer.
22.3.4 Error termination
PFLASH can invoke a system bus error termination in the following scenarios:
• Access privilege violation (see Access protections for details)
• Attempted access by an AHB master to a reserved region in the flash memory map
• Multi-bit ECC error detection on AHB read, and PFCR4[DMEEE] = 0 (for data flash memory, it is further qualified by 
PFCR4[DERR_SUP] = 0)
22.3.5 Line read buffers and prefetch operation
The PFLASH AHB ports of the a mini-cache. PFLASH uses the buffers for both prefetch and normal demand fetches. Also, the 
buffers are shared for code and data fetches, and can be controlled independently for code and data from control registers.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
850 / 5251


---
# 페이지 86

Prefetch triggering is controllable on a per-port basis. A PFLASH read access may trigger a prefetch to the next sequential line of 
array data on the cycle following the request. The access address is incremented by 32 bytes, and a subsequent flash memory 
access is initiated. A flash memory array prefetch is initiated if the data is not already resident in a line read buffer. Prefetched data 
is always loaded into the least-recently-used buffer.
For Port0, Port1, and Port2 there are four line buffer entries in their respective prefetch mini-caches that follow a fully associative, 
least-recently-used replacement policy. Port 3 configuration is the same as other ports. 
For prefetching to occur, you must set the following configuration fields, where n corresponds to the port number and m 
corresponds to C (code) or D (data):
PFCRn[Pn_mBFEN] = 1 and PFCRn[Pn_mPFEN] = 1
22.3.6 Array integrity considerations
During an array integrity sequence, the flash memory array ignores any incoming read requests. When a flash memory array 
integrity check is in progress, PFLASH terminates all flash memory access requests with an error. More specifically, it aborts the 
incoming flash memory access requests and terminates the system bus transfer with an error.
22.3.7 Safety considerations
22.3.7.1
Flash memory address generation check
Functional safety coverage of the address path and control within PFLASH rely on a feedback path between PFLASH and flash 
memory. Remember that on a requested access to flash memory, PFLASH must decode the system AHB bus signals to generate 
the corresponding flash memory interface signals to invoke a flash memory lookup. In addition to providing the requested read 
data, the flash memory also provides output sidebands reflecting the encoded address and block selects used to perform the 
actual row lookup.
PFLASH uses this sideband information to verify the expected transaction. If a mismatch is detected, indicating a failure in the 
address generation or control logic within PFLASH or the transmission path between PFLASH and the flash memory array, then 
the event is forwarded to the chip fault collection module and the corresponding buffer is invalidated.
22.3.8 ECC error handling on data flash block
When PFCR4[DERR_SUP] is enabled, ECC errors on data flash blocks are handled specially.
If there is a noncorrectable error detection, a fixed, illegal opcode value is returned to the requesting master along with the 
associated ECC checkbits as determined by the requesting address.
For noncorrectable error detection, PFLASH returns a value of 1555_1555h to the requesting master.
This is mainly used for EEPROM emulation applications.
22.3.9 Read cycles—buffer miss
On an incoming AHB read request, a mini-cache lookup and access privilege evaluation are performed during the AHB address 
phase. If a buffer miss occurs, a flash memory access is initiated.
If the flash memory access was the direct result of an AHB transaction, the corresponding page buffer is loaded and marked as the 
most-recently-used. If the flash memory access was the result of a speculative prefetch to the next sequential line, it is loaded into 
the least-recently-used buffer. The status of this buffer is not changed to most-recently-used until a subsequent buffer hit occurs 
as a result of an AHB read request.
22.3.10 Read cycles—buffer hit
PFLASH allows single-cycle read responses to the AHB when the requested read access was previously loaded into one of the 
page buffers. In these cases of a buffer hit, read data is returned on the system bus with a zero wait-state response.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
851 / 5251


---
# 페이지 87

22.3.11 Flash memory error response operation
The flash memory array may signal an error response to terminate a requested access because of improper sequencing during 
program/erase operations and improper sequencing during array integrity testing. When an error response is received, PFLASH 
does not update or validate a page read buffer. An error response may be signaled on a read or interlock write operation. For more 
information on the specifics related to signaling of flash memory errors, including flash memory ECC events, array integrity testing, 
and read-while-write events, see the flash memory chapter.
22.3.12 Clocking
This module has no clocking considerations.
22.3.13 Interrupts
This module has no interrupts.
22.4 External signals
This module has no external signals.
22.5 PFLASH0 register descriptions
PFLASH provides an IPS programming model mapped to a standard 16 KB on-platform peripheral slot. The programming model 
consists of flash memory access configuration.
You can reference the programming model only by using a 32-bit (word) access. References that are attempted using different 
access sizes, or to undefined (reserved) addresses, or in User mode generate an IPS error termination. PFLASH allows access 
to the programming model by all system bus masters.
Write to read only registers don't generate error termination.
You can only access the programming model in Supervisor mode, except *PEADR* registers which can be accessed in Supervisor 
or User mode.
Attempted updates to the programming model when PFLASH is in the middle of an operation results in non-deterministic behavior. 
You must architect software to avoid this scenario. The recommended flow for multicore devices is:
1. Start only one core.
2. Execute initialization code until it is complete.
3. Start the remaining cores.
If you need to reconfigure the flash memory, code execution must be temporarily moved to system RAM.
22.5.1 PFLASH0 memory map
PFLASH0 base address: 4026_8000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Platform Flash Memory Configuration 0 (PFCR0)
32
RW
0000_0003h
4h
Platform Flash Memory Configuration 1 (PFCR1)
32
RW
0000_0003h
8h
Platform Flash Memory Configuration 2 (PFCR2)
32
RW
0000_0003h
Ch
Platform Flash Memory Configuration 3 (PFCR3)
32
RW
0000_0003h
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
852 / 5251


---
# 페이지 88

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
10h
Platform Flash Memory Configuration 4 (PFCR4)
32
RW
0000_0000h
14h
Platform Flash Memory Access Protection (PFAPR)
32
RW
FFFF_FFFFh
300h
Platform Flash Memory Program Erase Address Logical 
(PFCPGM_PEADR_L)
32
RW
0000_0000h
304h
Platform Flash Memory Program Erase Address Physical 
(PFCPGM_PEADR_P)
32
R
0000_0000h
308h
Platform Flash Memory Express Program Erase Address Logical 
(PFCPGM_XPEADR_L)
32
RW
0000_0000h
30Ch
Platform Flash Memory Express Program Erase Address Physical 
(PFCPGM_XPEADR_P)
32
R
0000_0000h
340h - 350h
Block n Sector Program Erase Lock (PFCBLK0_SPELOCK - 
PFCBLK4_SPELOCK)
32
RW
FFFF_FFFFh
358h
Block UTEST Sector Program Erase Lock (PFCBLKU_SPELOCK)
32
RW
0000_0001h
35Ch - 368h
Block n Super Sector Program Erase Lock (PFCBLK0_SSPELOCK - 
PFCBLK3_SSPELOCK)
32
RW
0FFF_FFFFh
380h - 390h
Block n Set Sector Lock (PFCBLK0_SETSLOCK - 
PFCBLK4_SETSLOCK)
32
RW
0000_0000h
398h
Block UTEST Set Sector Lock (PFCBLKU_SETSLOCK)
32
RW
0000_0000h
39Ch - 3A8h
Block n Set Super Sector Lock (PFCBLK0_SSETSLOCK - 
PFCBLK3_SSETSLOCK)
32
RW
0000_0000h
3C0h - 45Ch
Block a Lock Master Sector b (PFCBLK0_LOCKMASTER_S0 - 
PFCBLK4_LOCKMASTER_S7)
32
R
FFFF_FFFFh
480h
Block UTEST Lock Master Sector (PFCBLKU_LOCKMASTER_S)
32
R
0000_00FFh
484h - 4F0h
Block m Lock Master Super Sector n 
(PFCBLK0_LOCKMASTER_SS0 - PFCBLK3_LOCKMASTER_SS6)
32
R
FFFF_FFFFh
22.5.2 Platform Flash Memory Configuration 0 (PFCR0)
Offset
Register
Offset
PFCR0
0h
Function
Specifies the operation of PFLASH Port0.
See the chip-specific PFLASH information for details about the actual masters available on the chip.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
853 / 5251


---
# 페이지 89

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
P0_DP
FEN 
P0_CP
FEN 
0
P0_DB
FEN 
P0_CB
FEN 
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
31-6
—
Reserved
5
P0_DPFEN
Port0 Data Prefetch Enable
Enables or disables data prefetching initiated by a read access on Port0. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to DBFEN. Hardware reset returns this field to 0.
0b - Disable
1b - Enable
4
P0_CPFEN
Port0 Code Prefetch Enable
Enables or disables code prefetching initiated by a read access on Port0. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to CBFEN. Hardware reset returns this field to 0.
0b - Disable
1b - Enable
3-2
—
Reserved
1
P0_DBFEN
Port0 PFLASH Line Read Data Buffers Enable
Enables or disables line read data buffer hits. It is also used to invalidate the buffers.
If this field is 0, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are 
set to 0. If this field is enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid 
bits may be set when the buffers are successfully filled.
0b - Disable
1b - Enable
0
P0_CBFEN
Port0 PFLASH Line Read Code Buffers Enable
Enables or disables line read code buffer hits. It is also used to invalidate the buffers.
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
854 / 5251


---
# 페이지 90

Table continued from the previous page...
Field
Function
If disabled, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are set 
to 0. If enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid bits may be 
set when the buffers are successfully filled.
0b - Disable
1b - Enable
22.5.3 Platform Flash Memory Configuration 1 (PFCR1)
Offset
Register
Offset
PFCR1
4h
Function
Specifies the operation of PFLASH Port1.
See the chip-specific PFLASH information for details about the actual masters available on the chip.
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
P1_DP
FEN 
P1_CP
FEN 
0
P1_DB
FEN 
P1_CB
FEN 
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
31-6
—
Reserved
5
P1_DPFEN
Port1 Data Prefetch Enable
Enables or disables data prefetching initiated by a read access on Port1. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to DBFEN. Hardware reset returns this field to 0.
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
855 / 5251


---
# 페이지 91

Table continued from the previous page...
Field
Function
0b - Disable
1b - Enable
4
P1_CPFEN
Port1 Code Prefetch Enable
Enables or disables code prefetching initiated by a read access on Port1. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to CBFEN. Hardware reset returns this field to 0.
0b - Disable
1b - Enable
3-2
—
Reserved
1
P1_DBFEN
Port1 PFLASH Line Read Data Buffers Enable
Enables or disables line read data buffer hits. It is also used to invalidate the buffers.
If this field is 0, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are 
set to 0. If this field is enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid 
bits may be set when the buffers are successfully filled.
0b - Disable
1b - Enable
0
P1_CBFEN
Port1 PFLASH Line Read Code Buffers Enable
Enables or disables line read code buffer hits. It is also used to invalidate the buffers.
If disabled, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are set 
to 0. If enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid bits may be 
set when the buffers are successfully filled.
0b - Disable
1b - Enable
22.5.4 Platform Flash Memory Configuration 2 (PFCR2)
Offset
Register
Offset
PFCR2
8h
Function
Specifies the operation of PFLASH Port2.
See the chip-specific PFLASH information for details about the actual masters available on the chip.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
856 / 5251


---
# 페이지 92

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
P2_DP
FEN 
P2_CP
FEN 
0
P2_DB
FEN 
P2_CB
FEN 
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
31-6
—
Reserved
5
P2_DPFEN
Port2 Data Prefetch Enable
Enables or disables data prefetching initiated by a read access on Port2. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to DBFEN. Hardware reset returns this field to 0.
0b - Disable
1b - Enable
4
P2_CPFEN
Port2 Code Prefetch Enable
Enables or disables code prefetching initiated by a read access on Port2. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to CBFEN. Hardware reset returns this field to 0.
0b - Disable
1b - Enable
3-2
—
Reserved
1
P2_DBFEN
Port2 PFLASH Line Read Data Buffers Enable
Enables or disables line read data buffer hits. It is also used to invalidate the buffers.
If this field is 0, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are 
set to 0. If this field is enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid 
bits may be set when the buffers are successfully filled.
0b - Disable
1b - Enable
0
P2_CBFEN
Port2 PFLASH Line Read Code Buffers Enable
Enables or disables line read code buffer hits. It is also used to invalidate the buffers.
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
857 / 5251


---
# 페이지 93

Table continued from the previous page...
Field
Function
If disabled, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are set 
to 0. If enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid bits may be 
set when the buffers are successfully filled.
0b - Disable
1b - Enable
22.5.5 Platform Flash Memory Configuration 3 (PFCR3)
Offset
Register
Offset
PFCR3
Ch
Function
Specifies the operation of PFLASH Port3.
See the chip-specific PFLASH information for details about the actual masters available on the chip.
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
P3_DP
FEN 
P3_CP
FEN 
0
P3_DB
FEN 
P3_CB
FEN 
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
31-6
—
Reserved
5
P3_DPFEN
Port3 Data Prefetch Enable
Enables or disables data prefetching initiated by a read access on Port3. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to DBFEN. Hardware reset returns this field to 0.
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
858 / 5251


---
# 페이지 94

Table continued from the previous page...
Field
Function
0b - Disable
1b - Enable
4
P3_CPFEN
Port3 Code Prefetch Enable
Enables or disables code prefetching initiated by a read access on Port3. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to CBFEN. Hardware reset returns this field to 0.
0b - Disable
1b - Enable
3-2
—
Reserved
1
P3_DBFEN
Port3 PFLASH Line Read Data Buffers Enable
Enables or disables line read data buffer hits. It is also used to invalidate the buffers.
If this field is 0, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are 
set to 0. If this field is enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid 
bits may be set when the buffers are successfully filled.
0b - Disable
1b - Enable
0
P3_CBFEN
Port3 PFLASH Line Read Code Buffers Enable
Enables or disables line read code buffer hits. It is also used to invalidate the buffers.
If disabled, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are set 
to 0. If enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid bits may be 
set when the buffers are successfully filled.
0b - Disable
1b - Enable
22.5.6 Platform Flash Memory Configuration 4 (PFCR4)
Offset
Register
Offset
PFCR4
10h
Function
Specifies operation of the flash memory controller buffer.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
859 / 5251


---
# 페이지 95

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
DMEE
E 
0
BLK4_PS 
DERR
_SUP 
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
31-8
—
Reserved
7
DMEEE
Disable Multi-Bit ECC Error Exception
Enables or disables system bus error response on multi-bit ECC error. Hardware reset returns this field to 0.
0b - Error response sent on system bus for multi-bit ECC error
1b - Error response not sent on system bus for multi-bit ECC error
6-4
—
Reserved
3-1
BLK4_PS
Block 4 Pipe Select
Selects the active pipe for flash memory block 4 access.
PFLASH has four independent command pipes to issue four parallel read commands to different flash 
memory blocks. Reads from flash memory block 0–3 are always done through command pipe 0–3, 
respectively. However, the access to block 4 is not fixed and can be through any of the command pipes. You 
must only change this field when there is no ongoing block 4 access.
A special round-robin arbitration scheme snoops the availability of a command pipe during block 4 access. 
If any of the command pipes are idle during the first read request to block 4, the ownership of that command 
pipe gets shared between block 4 and the respective block. If none of the command pipes are idle during a 
block 4 read request, block 4 gets associated with each of the command pipes in round-robin fashion. When 
a command pipe acquires ownership of block 4, it keeps that ownership until all the commands to block 4 
from all the masters are served.
000b - Block 4 access is always through pipe0
001b - Block 4 access is always through pipe1
010b - Block 4 access is always through pipe2
011b - Block 4 access is always through pipe3
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
860 / 5251


---
# 페이지 96

Table continued from the previous page...
Field
Function
1xxb - Block 4 access can be through any of the command pipes, based on which command pipe 
is available for block 4 access
0
DERR_SUP
Data Error Suppression
See the Embedded Flash Memory configuration information or system memory map for which flash 
memory blocks are affected by this field.
0b - Reports ECC events on data flash memory accesses
1b - Single-bit and multi-bit ECC events on data flash memory accesses are suppressed
22.5.7 Platform Flash Memory Access Protection (PFAPR)
Offset
Register
Offset
PFAPR
14h
Function
Controls read accesses to the flash memory array.
See the chip-specific PFLASH information for details about the actual masters available on the chip.
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
M0AP 
M1AP 
M2AP 
M3AP 
M4AP 
M5AP 
M6AP 
M7AP 
W
Reset
1
1
1
1
1
1
1
1
1
1
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
M8AP 
M9AP 
M10AP 
M11AP 
M12AP 
M13AP 
M14AP 
M15AP 
W
Reset
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
Fields
Field
Function
31-30: M0AP
29-28: M1AP
27-26: M2AP
Master n Access Protection
Controls whether read accesses to the flash memory are allowed based on the master ID of a requesting 
master. These fields are initialized by hardware reset. The field M4'd3AP is reserved.
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
861 / 5251


---
# 페이지 97

Field
Function
25-24: M3AP
23-22: M4AP
21-20: M5AP
19-18: M6AP
17-16: M7AP
15-14: M8AP
13-12: M9AP
11-10: M10AP
9-8: M11AP
7-6: M12AP
5-4: M13AP
3-2: M14AP
1-0: M15AP
x0b - This master cannot perform any read accesses
x1b - This master can perform read accesses
22.5.8 Platform Flash Memory Program Erase Address Logical (PFCPGM_PEADR_L)
Offset
Register
Offset
PFCPGM_PEADR_L
300h
Function
Provides the flash memory address to be programmed, or the location of the sector or block to be erased through main flash 
memory (pgm/erase) queue. Write access to this register is domain-ID aware.
The respective bus master must have program/erase permission to the flash memory address written to this register. Otherwise 
a transfer error results. For further information on flash memory address restrictions see the XRDC chapter.
A write to this register is managed via three-cycle access. Before updating the register, you must ensure that no ongoing 
high-voltage operation is executing through the flash memory main queue.
Unauthorized flash memory address writes result in a transfer error.
Writes to this register during an ongoing high-voltage operation (initiated through the flash memory main queue) or during express 
program operation are ignored.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
862 / 5251


---
# 페이지 98

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
PEADR_L 
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
PEADR_L 
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
PEADR_L
Program Erase Address Logical
Contains the system logical address for flash memory program/erase.
22.5.9 Platform Flash Memory Program Erase Address Physical (PFCPGM_PEADR_P)
Offset
Register
Offset
PFCPGM_PEADR_P
304h
Function
Reflects the flash memory block number and offset address corresponding to Platform Flash Memory Program Erase Address 
Logical (PFCPGM_PEADR_L). This register has the same format as the PEADR register in the Flash Memory chapter—see it 
for details.
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
PEADR_P 
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
PEADR_P 
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
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
863 / 5251


---
# 페이지 99

Fields
Field
Function
31-0
PEADR_P
Program Erase Address Physical
Contains the flash block select and offset address for flash memory program/erase.
22.5.10 Platform Flash Memory Express Program Erase Address Logical (PFCPGM_XPEADR_L)
Offset
Register
Offset
PFCPGM_XPEADR_L
308h
Function
Provides the flash memory address to be programmed using the flash memory express program feature. Write access to this 
register is domain-ID aware.
The respective bus master must have program/erase permission to the flash memory address written to this register. Otherwise 
a transfer error results. See the XRDC chapter for further information on flash memory address restrictions.
A write to this register is managed via three-cycle access. Before updating the register, you must ensure that no ongoing 
high-voltage operation is executing through the flash memory main queue.
Unauthorized flash memory address writes result in a transfer error.
Writes to this register during an ongoing express program operation are ignored.
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
XPEADR_L 
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
XPEADR_L 
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
XPEADR_L
Express Program Erase Address Logical
Contains the system logical address for express flash program/erase.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
864 / 5251


---
# 페이지 100

22.5.11 Platform Flash Memory Express Program Erase Address Physical (PFCPGM_XPEADR_P)
Offset
Register
Offset
PFCPGM_XPEADR_P
30Ch
Function
Reflects the flash memory block number and offset address corresponding to PFCPGM_XPEADR_L. This register has the same 
format as the XPEADR register in the Flash Memory chapter—see it for details.
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
XPEADR_P 
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
XPEADR_P 
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
XPEADR_P
Express Program Erase Address Physical
Contains the flash memory block select and offset address for flash memory express program/erase.
22.5.12 Block n Sector Program Erase Lock (PFCBLK0_SPELOCK - PFCBLK4_SPELOCK)
Offset
Register
Offset
PFCBLK0_SPELOCK
340h
PFCBLK1_SPELOCK
344h
PFCBLK2_SPELOCK
348h
PFCBLK3_SPELOCK
34Ch
PFCBLK4_SPELOCK
350h
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
865 / 5251


---
# 페이지 101

Function
Provides a way to protect sectors from being modified. Sector protection is available on the last 256 KB of every block (for 256 
KB blocks, all sectors are available for protection). Each lock bit can be associated with a particular domain ID by writing 1 to 
the appropriate bit in PFCBLKn_SETSLOCK[SETSLCK]. After the lock is acquired, only a master having the same domain ID 
can modify the corresponding lock bit. If the corresponding PFCBLKn_SETSLOCK[SETSLCK] bit is not equal to 1, any master 
can modify the appropriate SLCK bit. If a lock bit is already acquired by a particular domain ID, any effort to modify (1 to 0, or 0 
to 1) the lock bit by a master with a different domain ID results in a transfer error.
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
SLCK 
W
Reset
1
1
1
1
1
1
1
1
1
1
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
SLCK 
W
Reset
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
Fields
Field
Function
31-0
SLCK
Sector Lock
Locks selected sector. If vector bit value = 0, the sector is available for program and erase operations. If 
vector bit value = 1, the sector is locked and not available for program and erase operations.
22.5.13 Block UTEST Sector Program Erase Lock (PFCBLKU_SPELOCK)
Offset
Register
Offset
PFCBLKU_SPELOCK
358h
Function
Provides a way to protect sectors from being modified. Sector protection is available on the last 256 KB of every block (for 
256 KB blocks, all sectors are available for protection). Each lock bit can be associated with a particular domain ID by writing 
1 to PFCBLKU_SETSLOCK[SETSLCK]. After the lock is acquired, only a master having the same domain ID can modify the 
corresponding lock bit. If the corresponding PFCBLKU_SETSLOCK[SETSLCK] bit is not equal to 1, any master can modify the 
SLCK bit. If a lock bit is already acquired by a particular domain ID, any effort to modify (1 to 0, or 0 to 1) the lock bit by a 
master with a different domain ID results in a transfer error.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
866 / 5251


---
# 페이지 102

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
SLCK 
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
SLCK
Sector Lock
Locks selected sector. If vector bit value = 0, the sector is available for program and erase operations. If 
vector bit value = 1, the sector is locked and not available for program and erase operations.
22.5.14 Block n Super Sector Program Erase Lock (PFCBLK0_SSPELOCK - PFCBLK3_SSPELOCK)
Offset
Register
Offset
PFCBLK0_SSPELOCK
35Ch
PFCBLK1_SSPELOCK
360h
PFCBLK2_SSPELOCK
364h
PFCBLK3_SSPELOCK
368h
Function
Provides a way to protect super sectors from being modified. Super sector protection is available on block space larger 
than 256 KB. For 256 KB blocks, this register is not applicable. For 512 KB blocks, the first half of the block is protected 
with super sector granularity. For 1 MB blocks, the first 768 KB is protected with super sector granularity. Each lock bit can 
be associated with a particular domain ID by writing 1 to the appropriate bit in PFCBLKn_SSETSLOCK[SSETSLCK]. After 
the lock is acquired, only a master having the same domain ID can modify the corresponding lock bit. If the corresponding 
PFCBLKn_SSETSLOCK[SSETSLCK] bit is not equal to 1, any master can modify the SSLCK bit. If a lock bit is already 
acquired by a particular domain ID, any effort to modify (1 to 0, or 0 to 1) the lock bit by a master with a different domain ID 
results in a transfer error.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
867 / 5251


---
# 페이지 103

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
SSLCK 
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
1
1
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
SSLCK 
W
Reset
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
Fields
Field
Function
31-28
—
Reserved
27-0
SSLCK
Super Sector Lock
Locks selected super sector. If vector bit value = 0, the super sector is available for program and 
erase operations. If vector bit value = 1, the super sector is locked and not available for program and 
erase operations.
22.5.15 Block n Set Sector Lock (PFCBLK0_SETSLOCK - PFCBLK4_SETSLOCK)
Offset
Register
Offset
PFCBLK0_SETSLOCK
380h
PFCBLK1_SETSLOCK
384h
PFCBLK2_SETSLOCK
388h
PFCBLK3_SETSLOCK
38Ch
PFCBLK4_SETSLOCK
390h
Function
Provides a mechanism for the masters to gain the ownership of the corresponding PFCBLKn_SPELOCK lock bit based on 
domain id . After it is equal to 1, the bit is returned to 0 at next reset. If any SETSLOCK bit is not equal to 1, the corresponding 
LOCK bit can be modified by any master. If a bit is already acquired by a particular domain ID, any effort to modify the lock bit 
by a master with a different domain ID is ignored without transfer error.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
868 / 5251


---
# 페이지 104

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
SETSLCK 
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
SETSLCK 
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
SETSLCK
If the vector bit value = 0, the corresponding lock bit is not owned by any master. If the vector bit value = 1, 
the lock bit is owned by the masters having the domain ID stored in PFCBLKn_LOCKMASTER_Sm.
22.5.16 Block UTEST Set Sector Lock (PFCBLKU_SETSLOCK)
Offset
Register
Offset
PFCBLKU_SETSLOCK
398h
Function
Provides a mechanism for the masters to gain ownership of the corresponding PFCBLKU_SPELOCK lock bit based on 
domain id. After it is equal to 1, the bit is returned to 0 at next reset. If any SETSLOCK bit is not equal to 1, the corresponding 
LOCK bit can be modified by any master. If a bit is already acquired by a particular domain ID, any effort to modify the lock bit 
by a master with a different domain ID is ignored without transfer error.
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
SETSL
CK 
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
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
869 / 5251


---
# 페이지 105

Fields
Field
Function
31-1
—
Reserved
0
SETSLCK
Set Sector Lock
Locks selected sector. If vector bit value = 0, the corresponding lock bit is not owned by any 
master. If vector bit value = 1, the lock bit is owned by the masters having the domain ID stored 
in PFCBLKn_LOCKMASTER_SSm.
22.5.17 Block n Set Super Sector Lock (PFCBLK0_SSETSLOCK - PFCBLK3_SSETSLOCK)
Offset
Register
Offset
PFCBLK0_SSETSLOCK
39Ch
PFCBLK1_SSETSLOCK
3A0h
PFCBLK2_SSETSLOCK
3A4h
PFCBLK3_SSETSLOCK
3A8h
Function
Provides a mechanism for the masters to gain ownership of the corresponding PFCBLKn_SPELOCK lock bit based on domain 
id. After it is equal to 1, the bit is returned to 0 at next reset. If any SSETSLOCK bit is not equal to 1, the corresponding LOCK 
bit can be modified by any master. If a bit is already acquired by a particular domain ID, any effort to modify the lock bit by a 
master with a different domain ID is ignored without transfer error.
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
SSETSLCK 
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
SSETSLCK 
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
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
870 / 5251


---
# 페이지 106

Fields
Field
Function
31-28
—
Reserved
27-0
SSETSLCK
Set Super Sector Lock
Locks selected super sector. If vector bit value = 0, the corresponding lock bit is not owned by any master. If 
vector bit value = 1, the lock bit is owned by the masters having the domain ID stored in Block a Lock Master 
Sector b (PFCBLK0_LOCKMASTER_S0 - PFCBLK4_LOCKMASTER_S7).
22.5.18 Block a Lock Master Sector b (PFCBLK0_LOCKMASTER_S0 - 
PFCBLK4_LOCKMASTER_S7)
Offset
For a = 0 to 4; b = 0 to 7:
Register
Offset
PFCBLKa_LOCKMASTE
R_Sb
3C0h + (a × 20h) + (b × 4h)
Function
Provides the domain ID information of the master currently acquiring the lock bit. The domain ID is represented by an 8-bit 
field. This is a read-only register.
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
LOCKMASTER_S 
W
Reset
1
1
1
1
1
1
1
1
1
1
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
LOCKMASTER_S 
W
Reset
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
Fields
Field
Function
31-0
Block a Lock Master Sector b
Contains domain ID of the master currently acquiring the lock bit.
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
871 / 5251


---
# 페이지 107

Field
Function
LOCKMASTER
_S
PFCBLK0_LOCKMASTER_S0[LOCKMASTER_S[7:0]] holds the domain ID information 
of PFCBLK0_SPELOCK[0].
PFCBLK0_LOCKMASTER_S0[LOCKMASTER_S[15:8]] holds the domain ID information of 
PFCBLK0_SPELOCK[1], and so on in incremental order.
22.5.19 Block UTEST Lock Master Sector (PFCBLKU_LOCKMASTER_S)
Offset
Register
Offset
PFCBLKU_LOCKMAST
ER_S
480h
Function
Provides the domain ID information of the master currently acquiring the lock bit. The domain ID is represented by an 8-bit 
field. This is a read-only register.
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
LOCKMASTER_S 
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
1
1
1
1
1
1
Fields
Field
Function
31-8
—
Reserved
7-0
LOCKMASTER
_S
Lock Master Sector
Contains domain ID of the master currently acquiring the lock bit.
PFCBLKU_LOCKMASTER_S[LOCKMASTER_S[7:0]] holds the domain ID information 
of PFCBLKU_SPELOCK[0].
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
872 / 5251


---
# 페이지 108

22.5.20 Block m Lock Master Super Sector n (PFCBLK0_LOCKMASTER_SS0 - 
PFCBLK3_LOCKMASTER_SS6)
Offset
For a = 0 to 3; b = 0 to 6:
Register
Offset
PFCBLKa_LOCKMASTE
R_SSb
484h + (a × 1Ch) + (b × 4h)
Function
Provides the domain ID information of the master currently acquiring the lock bit. The domain ID is represented by an 8-bit 
field. This is a read-only register.
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
LOCKMASTER_SS 
W
Reset
1
1
1
1
1
1
1
1
1
1
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
LOCKMASTER_SS 
W
Reset
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
Fields
Field
Function
31-0
LOCKMASTER
_SS
Block a Lock Master Super Sector b
Contains domain ID of the master currently acquiring the lock bit.
PFCBLK0_LOCKMASTER_SS0[LOCKMASTER_SS[7:0]] holds the domain ID information 
of PFCBLK0_SSPELOCK[0].
PFCBLK0_LOCKMASTER_SS0[LOCKMASTER_SS[15:8]] holds the domain ID information of 
PFCBLK0_SSPELOCK[1], and so on in incremental order.
22.6 PFLASH1 register descriptions
PFLASH provides an IPS programming model mapped to a standard 16 KB on-platform peripheral slot. The programming model 
consists of flash memory access configuration.
You can reference the programming model only by using a 32-bit (word) access. References that are attempted using different 
access sizes, or to undefined (reserved) addresses, or in User mode generate an IPS error termination. PFLASH allows access 
to the programming model by all system bus masters.
Write to read only registers don't generate error termination.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
873 / 5251


---
# 페이지 109

You can only access the programming model in Supervisor mode, except *PEADR* registers which can be accessed in Supervisor 
or User mode.
Attempted updates to the programming model when PFLASH is in the middle of an operation results in non-deterministic behavior. 
You must architect software to avoid this scenario. The recommended flow for multicore devices is:
1. Start only one core.
2. Execute initialization code until it is complete.
3. Start the remaining cores.
If you need to reconfigure the flash memory, code execution must be temporarily moved to system RAM.
22.6.1 PFLASH1 memory map
PFLASH1 base address: 4006_8000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Platform Flash Memory Configuration 0 (PFCR0)
32
RW
0000_0003h
4h
Platform Flash Memory Configuration 1 (PFCR1)
32
RW
0000_0003h
8h
Platform Flash Memory Configuration 2 (PFCR2)
32
RW
0000_0003h
Ch
Platform Flash Memory Configuration 3 (PFCR3)
32
RW
0000_0003h
10h
Platform Flash Memory Configuration 4 (PFCR4)
32
RW
0000_0000h
14h
Platform Flash Memory Access Protection (PFAPR)
32
RW
FFFF_FFFFh
300h
Platform Flash Memory Program Erase Address Logical 
(PFCPGM_PEADR_L)
32
RW
0000_0000h
304h
Platform Flash Memory Program Erase Address Physical 
(PFCPGM_PEADR_P)
32
R
0000_0000h
308h
Platform Flash Memory Express Program Erase Address Logical 
(PFCPGM_XPEADR_L)
32
RW
0000_0000h
30Ch
Platform Flash Memory Express Program Erase Address Physical 
(PFCPGM_XPEADR_P)
32
R
0000_0000h
340h - 350h
Block n Sector Program Erase Lock (PFCBLK0_SPELOCK - 
PFCBLK4_SPELOCK)
32
RW
FFFF_FFFFh
358h
Block UTEST Sector Program Erase Lock (PFCBLKU_SPELOCK)
32
RW
0000_0001h
35Ch - 368h
Block n Super Sector Program Erase Lock (PFCBLK0_SSPELOCK - 
PFCBLK3_SSPELOCK)
32
RW
0000_0FFFh
380h - 390h
Block n Set Sector Lock (PFCBLK0_SETSLOCK - 
PFCBLK4_SETSLOCK)
32
RW
0000_0000h
398h
Block UTEST Set Sector Lock (PFCBLKU_SETSLOCK)
32
RW
0000_0000h
39Ch - 3A8h
Block n Set Super Sector Lock (PFCBLK0_SSETSLOCK - 
PFCBLK3_SSETSLOCK)
32
RW
0000_0000h
3C0h - 45Ch
Block a Lock Master Sector b (PFCBLK0_LOCKMASTER_S0 - 
PFCBLK4_LOCKMASTER_S7)
32
R
FFFF_FFFFh
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
874 / 5251


---
# 페이지 110

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
480h
Block UTEST Lock Master Sector (PFCBLKU_LOCKMASTER_S)
32
R
0000_00FFh
484h
Block m Lock Master Super Sector n 
(PFCBLK0_LOCKMASTER_SS0)
32
R
FFFF_FFFFh
488h
Block m Lock Master Super Sector n 
(PFCBLK0_LOCKMASTER_SS1)
32
R
FFFF_FFFFh
48Ch
Block m Lock Master Super Sector n 
(PFCBLK0_LOCKMASTER_SS2)
32
R
FFFF_FFFFh
494h
Block m Lock Master Super Sector n 
(PFCBLK1_LOCKMASTER_SS0)
32
R
FFFF_FFFFh
498h
Block m Lock Master Super Sector n 
(PFCBLK1_LOCKMASTER_SS1)
32
R
FFFF_FFFFh
49Ch
Block m Lock Master Super Sector n 
(PFCBLK1_LOCKMASTER_SS2)
32
R
FFFF_FFFFh
4A4h
Block m Lock Master Super Sector n 
(PFCBLK2_LOCKMASTER_SS0)
32
R
FFFF_FFFFh
4A8h
Block m Lock Master Super Sector n 
(PFCBLK2_LOCKMASTER_SS1)
32
R
FFFF_FFFFh
4ACh
Block m Lock Master Super Sector n 
(PFCBLK2_LOCKMASTER_SS2)
32
R
FFFF_FFFFh
4B4h
Block m Lock Master Super Sector n 
(PFCBLK3_LOCKMASTER_SS0)
32
R
FFFF_FFFFh
4B8h
Block m Lock Master Super Sector n 
(PFCBLK3_LOCKMASTER_SS1)
32
R
FFFF_FFFFh
4BCh
Block m Lock Master Super Sector n 
(PFCBLK3_LOCKMASTER_SS2)
32
R
FFFF_FFFFh
22.6.2 Platform Flash Memory Configuration 0 (PFCR0)
Offset
Register
Offset
PFCR0
0h
Function
Specifies the operation of PFLASH Port0.
See the chip-specific PFLASH information for details about the actual masters available on the chip.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
875 / 5251


---
# 페이지 111

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
P0_DP
FEN 
P0_CP
FEN 
0
P0_DB
FEN 
P0_CB
FEN 
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
31-6
—
Reserved
5
P0_DPFEN
Port0 Data Prefetch Enable
Enables or disables data prefetching initiated by a read access on Port0. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to DBFEN. Hardware reset returns this field to 0.
0b - Disable
1b - Enable
4
P0_CPFEN
Port0 Code Prefetch Enable
Enables or disables code prefetching initiated by a read access on Port0. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to CBFEN. Hardware reset returns this field to 0.
0b - Disable
1b - Enable
3-2
—
Reserved
1
P0_DBFEN
Port0 PFLASH Line Read Data Buffers Enable
Enables or disables line read data buffer hits. It is also used to invalidate the buffers.
If this field is 0, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are 
set to 0. If this field is enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid 
bits may be set when the buffers are successfully filled.
0b - Disable
1b - Enable
0
P0_CBFEN
Port0 PFLASH Line Read Code Buffers Enable
Enables or disables line read code buffer hits. It is also used to invalidate the buffers.
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
876 / 5251


---
# 페이지 112

Table continued from the previous page...
Field
Function
If disabled, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are set 
to 0. If enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid bits may be 
set when the buffers are successfully filled.
0b - Disable
1b - Enable
22.6.3 Platform Flash Memory Configuration 1 (PFCR1)
Offset
Register
Offset
PFCR1
4h
Function
Specifies the operation of PFLASH Port1.
See the chip-specific PFLASH information for details about the actual masters available on the chip.
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
P1_DP
FEN 
P1_CP
FEN 
0
P1_DB
FEN 
P1_CB
FEN 
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
31-6
—
Reserved
5
P1_DPFEN
Port1 Data Prefetch Enable
Enables or disables data prefetching initiated by a read access on Port1. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to DBFEN. Hardware reset returns this field to 0.
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
877 / 5251


---
# 페이지 113

Table continued from the previous page...
Field
Function
0b - Disable
1b - Enable
4
P1_CPFEN
Port1 Code Prefetch Enable
Enables or disables code prefetching initiated by a read access on Port1. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to CBFEN. Hardware reset returns this field to 0.
0b - Disable
1b - Enable
3-2
—
Reserved
1
P1_DBFEN
Port1 PFLASH Line Read Data Buffers Enable
Enables or disables line read data buffer hits. It is also used to invalidate the buffers.
If this field is 0, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are 
set to 0. If this field is enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid 
bits may be set when the buffers are successfully filled.
0b - Disable
1b - Enable
0
P1_CBFEN
Port1 PFLASH Line Read Code Buffers Enable
Enables or disables line read code buffer hits. It is also used to invalidate the buffers.
If disabled, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are set 
to 0. If enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid bits may be 
set when the buffers are successfully filled.
0b - Disable
1b - Enable
22.6.4 Platform Flash Memory Configuration 2 (PFCR2)
Offset
Register
Offset
PFCR2
8h
Function
Specifies the operation of PFLASH Port2.
See the chip-specific PFLASH information for details about the actual masters available on the chip.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
878 / 5251


---
# 페이지 114

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
P2_DP
FEN 
P2_CP
FEN 
0
P2_DB
FEN 
P2_CB
FEN 
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
31-6
—
Reserved
5
P2_DPFEN
Port2 Data Prefetch Enable
Enables or disables data prefetching initiated by a read access on Port2. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to DBFEN. Hardware reset returns this field to 0.
0b - Disable
1b - Enable
4
P2_CPFEN
Port2 Code Prefetch Enable
Enables or disables code prefetching initiated by a read access on Port2. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to CBFEN. Hardware reset returns this field to 0.
0b - Disable
1b - Enable
3-2
—
Reserved
1
P2_DBFEN
Port2 PFLASH Line Read Data Buffers Enable
Enables or disables line read data buffer hits. It is also used to invalidate the buffers.
If this field is 0, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are 
set to 0. If this field is enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid 
bits may be set when the buffers are successfully filled.
0b - Disable
1b - Enable
0
P2_CBFEN
Port2 PFLASH Line Read Code Buffers Enable
Enables or disables line read code buffer hits. It is also used to invalidate the buffers.
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
879 / 5251


---
# 페이지 115

Table continued from the previous page...
Field
Function
If disabled, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are set 
to 0. If enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid bits may be 
set when the buffers are successfully filled.
0b - Disable
1b - Enable
22.6.5 Platform Flash Memory Configuration 3 (PFCR3)
Offset
Register
Offset
PFCR3
Ch
Function
Specifies the operation of PFLASH Port3.
See the chip-specific PFLASH information for details about the actual masters available on the chip.
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
P3_DP
FEN 
P3_CP
FEN 
0
P3_DB
FEN 
P3_CB
FEN 
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
31-6
—
Reserved
5
P3_DPFEN
Port3 Data Prefetch Enable
Enables or disables data prefetching initiated by a read access on Port3. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to DBFEN. Hardware reset returns this field to 0.
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
880 / 5251


---
# 페이지 116

Table continued from the previous page...
Field
Function
0b - Disable
1b - Enable
4
P3_CPFEN
Port3 Code Prefetch Enable
Enables or disables code prefetching initiated by a read access on Port3. Prefetching can only be 
enabled if the buffers are enabled by writing 1 to CBFEN. Hardware reset returns this field to 0.
0b - Disable
1b - Enable
3-2
—
Reserved
1
P3_DBFEN
Port3 PFLASH Line Read Data Buffers Enable
Enables or disables line read data buffer hits. It is also used to invalidate the buffers.
If this field is 0, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are 
set to 0. If this field is enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid 
bits may be set when the buffers are successfully filled.
0b - Disable
1b - Enable
0
P3_CBFEN
Port3 PFLASH Line Read Code Buffers Enable
Enables or disables line read code buffer hits. It is also used to invalidate the buffers.
If disabled, the line read buffers are disabled from satisfying read requests, and all buffer valid bits are set 
to 0. If enabled, the line read buffers are enabled to satisfy read requests on hits. Buffer valid bits may be 
set when the buffers are successfully filled.
0b - Disable
1b - Enable
22.6.6 Platform Flash Memory Configuration 4 (PFCR4)
Offset
Register
Offset
PFCR4
10h
Function
Specifies operation of the flash memory controller buffer.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
881 / 5251


---
# 페이지 117

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
DMEE
E 
0
BLK4_PS 
DERR
_SUP 
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
31-8
—
Reserved
7
DMEEE
Disable Multi-Bit ECC Error Exception
Enables or disables system bus error response on multi-bit ECC error. Hardware reset returns this field to 0.
0b - Error response sent on system bus for multi-bit ECC error
1b - Error response not sent on system bus for multi-bit ECC error
6-4
—
Reserved
3-1
BLK4_PS
Block 4 Pipe Select
Selects the active pipe for flash memory block 4 access.
PFLASH has four independent command pipes to issue four parallel read commands to different flash 
memory blocks. Reads from flash memory block 0–3 are always done through command pipe 0–3, 
respectively. However, the access to block 4 is not fixed and can be through any of the command pipes. You 
must only change this field when there is no ongoing block 4 access.
A special round-robin arbitration scheme snoops the availability of a command pipe during block 4 access. 
If any of the command pipes are idle during the first read request to block 4, the ownership of that command 
pipe gets shared between block 4 and the respective block. If none of the command pipes are idle during a 
block 4 read request, block 4 gets associated with each of the command pipes in round-robin fashion. When 
a command pipe acquires ownership of block 4, it keeps that ownership until all the commands to block 4 
from all the masters are served.
000b - Block 4 access is always through pipe0
001b - Block 4 access is always through pipe1
010b - Block 4 access is always through pipe2
011b - Block 4 access is always through pipe3
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
882 / 5251


---
# 페이지 118

Table continued from the previous page...
Field
Function
1xxb - Block 4 access can be through any of the command pipes, based on which command pipe 
is available for block 4 access
0
DERR_SUP
Data Error Suppression
See the Embedded Flash Memory configuration information or system memory map for which flash 
memory blocks are affected by this field.
0b - Reports ECC events on data flash memory accesses
1b - Single-bit and multi-bit ECC events on data flash memory accesses are suppressed
22.6.7 Platform Flash Memory Access Protection (PFAPR)
Offset
Register
Offset
PFAPR
14h
Function
Controls read accesses to the flash memory array.
See the chip-specific PFLASH information for details about the actual masters available on the chip.
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
M0AP 
M1AP 
M2AP 
M3AP 
M4AP 
M5AP 
M6AP 
M7AP 
W
Reset
1
1
1
1
1
1
1
1
1
1
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
M8AP 
M9AP 
M10AP 
M11AP 
M12AP 
M13AP 
M14AP 
M15AP 
W
Reset
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
Fields
Field
Function
31-30: M0AP
29-28: M1AP
27-26: M2AP
Master n Access Protection
Controls whether read accesses to the flash memory are allowed based on the master ID of a requesting 
master. These fields are initialized by hardware reset. The field M4'd3AP is reserved.
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
883 / 5251


---
# 페이지 119

Field
Function
25-24: M3AP
23-22: M4AP
21-20: M5AP
19-18: M6AP
17-16: M7AP
15-14: M8AP
13-12: M9AP
11-10: M10AP
9-8: M11AP
7-6: M12AP
5-4: M13AP
3-2: M14AP
1-0: M15AP
x0b - This master cannot perform any read accesses
x1b - This master can perform read accesses
22.6.8 Platform Flash Memory Program Erase Address Logical (PFCPGM_PEADR_L)
Offset
Register
Offset
PFCPGM_PEADR_L
300h
Function
Provides the flash memory address to be programmed, or the location of the sector or block to be erased through main flash 
memory (pgm/erase) queue. Write access to this register is domain-ID aware.
The respective bus master must have program/erase permission to the flash memory address written to this register. Otherwise 
a transfer error results. For further information on flash memory address restrictions see the XRDC chapter.
A write to this register is managed via three-cycle access. Before updating the register, you must ensure that no ongoing 
high-voltage operation is executing through the flash memory main queue.
Unauthorized flash memory address writes result in a transfer error.
Writes to this register during an ongoing high-voltage operation (initiated through the flash memory main queue) or during express 
program operation are ignored.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
884 / 5251


---
# 페이지 120

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
PEADR_L 
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
PEADR_L 
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
PEADR_L
Program Erase Address Logical
Contains the system logical address for flash memory program/erase.
22.6.9 Platform Flash Memory Program Erase Address Physical (PFCPGM_PEADR_P)
Offset
Register
Offset
PFCPGM_PEADR_P
304h
Function
Reflects the flash memory block number and offset address corresponding to Platform Flash Memory Program Erase Address 
Logical (PFCPGM_PEADR_L). This register has the same format as the PEADR register in the Flash Memory chapter—see it 
for details.
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
PEADR_P 
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
PEADR_P 
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
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
885 / 5251


---
# 페이지 121

Fields
Field
Function
31-0
PEADR_P
Program Erase Address Physical
Contains the flash block select and offset address for flash memory program/erase.
22.6.10 Platform Flash Memory Express Program Erase Address Logical (PFCPGM_XPEADR_L)
Offset
Register
Offset
PFCPGM_XPEADR_L
308h
Function
Provides the flash memory address to be programmed using the flash memory express program feature. Write access to this 
register is domain-ID aware.
The respective bus master must have program/erase permission to the flash memory address written to this register. Otherwise 
a transfer error results. See the XRDC chapter for further information on flash memory address restrictions.
A write to this register is managed via three-cycle access. Before updating the register, you must ensure that no ongoing 
high-voltage operation is executing through the flash memory main queue.
Unauthorized flash memory address writes result in a transfer error.
Writes to this register during an ongoing express program operation are ignored.
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
XPEADR_L 
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
XPEADR_L 
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
XPEADR_L
Express Program Erase Address Logical
Contains the system logical address for express flash program/erase.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
886 / 5251


---
# 페이지 122

22.6.11 Platform Flash Memory Express Program Erase Address Physical (PFCPGM_XPEADR_P)
Offset
Register
Offset
PFCPGM_XPEADR_P
30Ch
Function
Reflects the flash memory block number and offset address corresponding to PFCPGM_XPEADR_L. This register has the same 
format as the XPEADR register in the Flash Memory chapter—see it for details.
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
XPEADR_P 
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
XPEADR_P 
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
XPEADR_P
Express Program Erase Address Physical
Contains the flash memory block select and offset address for flash memory express program/erase.
22.6.12 Block n Sector Program Erase Lock (PFCBLK0_SPELOCK - PFCBLK4_SPELOCK)
Offset
Register
Offset
PFCBLK0_SPELOCK
340h
PFCBLK1_SPELOCK
344h
PFCBLK2_SPELOCK
348h
PFCBLK3_SPELOCK
34Ch
PFCBLK4_SPELOCK
350h
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
887 / 5251


---
# 페이지 123

Function
Provides a way to protect sectors from being modified. Sector protection is available on the last 256 KB of every block (for 256 
KB blocks, all sectors are available for protection). Each lock bit can be associated with a particular domain ID by writing 1 to 
the appropriate bit in PFCBLKn_SETSLOCK[SETSLCK]. After the lock is acquired, only a master having the same domain ID 
can modify the corresponding lock bit. If the corresponding PFCBLKn_SETSLOCK[SETSLCK] bit is not equal to 1, any master 
can modify the appropriate SLCK bit. If a lock bit is already acquired by a particular domain ID, any effort to modify (1 to 0, or 0 
to 1) the lock bit by a master with a different domain ID results in a transfer error.
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
SLCK 
W
Reset
1
1
1
1
1
1
1
1
1
1
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
SLCK 
W
Reset
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
Fields
Field
Function
31-0
SLCK
Sector Lock
Locks selected sector. If vector bit value = 0, the sector is available for program and erase operations. If 
vector bit value = 1, the sector is locked and not available for program and erase operations.
22.6.13 Block UTEST Sector Program Erase Lock (PFCBLKU_SPELOCK)
Offset
Register
Offset
PFCBLKU_SPELOCK
358h
Function
Provides a way to protect sectors from being modified. Sector protection is available on the last 256 KB of every block (for 
256 KB blocks, all sectors are available for protection). Each lock bit can be associated with a particular domain ID by writing 
1 to PFCBLKU_SETSLOCK[SETSLCK]. After the lock is acquired, only a master having the same domain ID can modify the 
corresponding lock bit. If the corresponding PFCBLKU_SETSLOCK[SETSLCK] bit is not equal to 1, any master can modify the 
SLCK bit. If a lock bit is already acquired by a particular domain ID, any effort to modify (1 to 0, or 0 to 1) the lock bit by a 
master with a different domain ID results in a transfer error.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
888 / 5251


---
# 페이지 124

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
SLCK 
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
SLCK
Sector Lock
Locks selected sector. If vector bit value = 0, the sector is available for program and erase operations. If 
vector bit value = 1, the sector is locked and not available for program and erase operations.
22.6.14 Block n Super Sector Program Erase Lock (PFCBLK0_SSPELOCK - PFCBLK3_SSPELOCK)
Offset
Register
Offset
PFCBLK0_SSPELOCK
35Ch
PFCBLK1_SSPELOCK
360h
PFCBLK2_SSPELOCK
364h
PFCBLK3_SSPELOCK
368h
Function
Provides a way to protect super sectors from being modified. Super sector protection is available on block space larger 
than 256 KB. For 256 KB blocks, this register is not applicable. For 512 KB blocks, the first half of the block is protected 
with super sector granularity. For 1 MB blocks, the first 768 KB is protected with super sector granularity. Each lock bit can 
be associated with a particular domain ID by writing 1 to the appropriate bit in PFCBLKn_SSETSLOCK[SSETSLCK]. After 
the lock is acquired, only a master having the same domain ID can modify the corresponding lock bit. If the corresponding 
PFCBLKn_SSETSLOCK[SSETSLCK] bit is not equal to 1, any master can modify the SSLCK bit. If a lock bit is already 
acquired by a particular domain ID, any effort to modify (1 to 0, or 0 to 1) the lock bit by a master with a different domain ID 
results in a transfer error.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
889 / 5251


---
# 페이지 125

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
SSLCK 
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
1
1
1
1
1
1
1
1
Fields
Field
Function
31-12
—
Reserved
11-0
SSLCK
Super Sector Lock
Locks selected super sector. If vector bit value = 0, the super sector is available for program and 
erase operations. If vector bit value = 1, the super sector is locked and not available for program and 
erase operations.
22.6.15 Block n Set Sector Lock (PFCBLK0_SETSLOCK - PFCBLK4_SETSLOCK)
Offset
Register
Offset
PFCBLK0_SETSLOCK
380h
PFCBLK1_SETSLOCK
384h
PFCBLK2_SETSLOCK
388h
PFCBLK3_SETSLOCK
38Ch
PFCBLK4_SETSLOCK
390h
Function
Provides a mechanism for the masters to gain the ownership of the corresponding PFCBLKn_SPELOCK lock bit based on 
domain id . After it is equal to 1, the bit is returned to 0 at next reset. If any SETSLOCK bit is not equal to 1, the corresponding 
LOCK bit can be modified by any master. If a bit is already acquired by a particular domain ID, any effort to modify the lock bit 
by a master with a different domain ID is ignored without transfer error.
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
890 / 5251


---
# 페이지 126

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
SETSLCK 
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
SETSLCK 
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
SETSLCK
If the vector bit value = 0, the corresponding lock bit is not owned by any master. If the vector bit value = 1, 
the lock bit is owned by the masters having the domain ID stored in PFCBLKn_LOCKMASTER_Sm.
22.6.16 Block UTEST Set Sector Lock (PFCBLKU_SETSLOCK)
Offset
Register
Offset
PFCBLKU_SETSLOCK
398h
Function
Provides a mechanism for the masters to gain ownership of the corresponding PFCBLKU_SPELOCK lock bit based on 
domain id. After it is equal to 1, the bit is returned to 0 at next reset. If any SETSLOCK bit is not equal to 1, the corresponding 
LOCK bit can be modified by any master. If a bit is already acquired by a particular domain ID, any effort to modify the lock bit 
by a master with a different domain ID is ignored without transfer error.
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
SETSL
CK 
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
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
891 / 5251


---
# 페이지 127

Fields
Field
Function
31-1
—
Reserved
0
SETSLCK
Set Sector Lock
Locks selected sector. If vector bit value = 0, the corresponding lock bit is not owned by any 
master. If vector bit value = 1, the lock bit is owned by the masters having the domain ID stored 
in PFCBLKn_LOCKMASTER_SSm.
22.6.17 Block n Set Super Sector Lock (PFCBLK0_SSETSLOCK - PFCBLK3_SSETSLOCK)
Offset
Register
Offset
PFCBLK0_SSETSLOCK
39Ch
PFCBLK1_SSETSLOCK
3A0h
PFCBLK2_SSETSLOCK
3A4h
PFCBLK3_SSETSLOCK
3A8h
Function
Provides a mechanism for the masters to gain ownership of the corresponding PFCBLKn_SPELOCK lock bit based on domain 
id. After it is equal to 1, the bit is returned to 0 at next reset. If any SSETSLOCK bit is not equal to 1, the corresponding LOCK 
bit can be modified by any master. If a bit is already acquired by a particular domain ID, any effort to modify the lock bit by a 
master with a different domain ID is ignored without transfer error.
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
SSETSLCK 
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
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
892 / 5251


---
# 페이지 128

Fields
Field
Function
31-12
—
Reserved
11-0
SSETSLCK
Set Super Sector Lock
Locks selected super sector. If vector bit value = 0, the corresponding lock bit is not owned by any master. If 
vector bit value = 1, the lock bit is owned by the masters having the domain ID stored in Block a Lock Master 
Sector b (PFCBLK0_LOCKMASTER_S0 - PFCBLK4_LOCKMASTER_S7).
22.6.18 Block a Lock Master Sector b (PFCBLK0_LOCKMASTER_S0 - 
PFCBLK4_LOCKMASTER_S7)
Offset
For a = 0 to 4; b = 0 to 7:
Register
Offset
PFCBLKa_LOCKMASTE
R_Sb
3C0h + (a × 20h) + (b × 4h)
Function
Provides the domain ID information of the master currently acquiring the lock bit. The domain ID is represented by an 8-bit 
field. This is a read-only register.
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
LOCKMASTER_S 
W
Reset
1
1
1
1
1
1
1
1
1
1
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
LOCKMASTER_S 
W
Reset
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
Fields
Field
Function
31-0
Block a Lock Master Sector b
Contains domain ID of the master currently acquiring the lock bit.
Table continues on the next page...
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
893 / 5251


---
# 페이지 129

Field
Function
LOCKMASTER
_S
PFCBLK0_LOCKMASTER_S0[LOCKMASTER_S[7:0]] holds the domain ID information 
of PFCBLK0_SPELOCK[0].
PFCBLK0_LOCKMASTER_S0[LOCKMASTER_S[15:8]] holds the domain ID information of 
PFCBLK0_SPELOCK[1], and so on in incremental order.
22.6.19 Block UTEST Lock Master Sector (PFCBLKU_LOCKMASTER_S)
Offset
Register
Offset
PFCBLKU_LOCKMAST
ER_S
480h
Function
Provides the domain ID information of the master currently acquiring the lock bit. The domain ID is represented by an 8-bit 
field. This is a read-only register.
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
LOCKMASTER_S 
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
1
1
1
1
1
1
Fields
Field
Function
31-8
—
Reserved
7-0
LOCKMASTER
_S
Lock Master Sector
Contains domain ID of the master currently acquiring the lock bit.
PFCBLKU_LOCKMASTER_S[LOCKMASTER_S[7:0]] holds the domain ID information 
of PFCBLKU_SPELOCK[0].
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
894 / 5251


---
# 페이지 130

22.6.20 Block m Lock Master Super Sector n (PFCBLK0_LOCKMASTER_SS0 - 
PFCBLK3_LOCKMASTER_SS2)
Offset
For a = 0 to 3; b = 0 to 2:
Register
Offset
PFCBLKa_LOCKMASTE
R_SSb
484h + (a × 10h) + (b × 4h)
Function
Provides the domain ID information of the master currently acquiring the lock bit. The domain ID is represented by an 8-bit 
field. This is a read-only register.
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
LOCKMASTER_SS 
W
Reset
1
1
1
1
1
1
1
1
1
1
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
LOCKMASTER_SS 
W
Reset
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
1
Fields
Field
Function
31-0
LOCKMASTER
_SS
Block a Lock Master Super Sector b
Contains domain ID of the master currently acquiring the lock bit.
PFCBLK0_LOCKMASTER_SS0[LOCKMASTER_SS[7:0]] holds the domain ID information 
of PFCBLK0_SSPELOCK[0].
PFCBLK0_LOCKMASTER_SS0[LOCKMASTER_SS[15:8]] holds the domain ID information of 
PFCBLK0_SSPELOCK[1], and so on in incremental order.
22.7 Glossary
AHB
Advanced high-performance bus
ECC
Error correcting code
HSE
Hardware security engine
IPS
Internal peripheral system
ID
Identification
NXP Semiconductors
Flash Memory Controller (PFLASH)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
895 / 5251


---