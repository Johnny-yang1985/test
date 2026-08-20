# 페이지 450

Chapter 12
Crossbar Switch (AXBS)
12.1 Chip-specific AXBS information
12.1.1 AXBS instances and connectivity matrix
This chip has up to seven instances of AXBS.
 
AXBS support concurrent transaction requests from initiator to same target and do time multiplex internally. Also, 
it supports concurrent transactions between mutually exclusive initiator-target pairs.
  NOTE  
Table 45. AXBS instances
Instance
S32K388/
S32K389
S32K358/
S32K348/
S32K338/
S32K328
S32K344/
S32K324/
S32K314
S32K342/
S32K322/
S32K341/
S32K322
S32K310/
S32K311/
S32K312
AXBS_0
Yes
Yes
Yes
Yes
Yes1
AXBS_1
Yes
Yes
Yes
Yes
No
AXBS_2
Yes
Yes
Yes
Yes
No
AXBS_3
Yes
Yes
Yes
Yes
No
AXBS_4
Yes
Yes
Yes
Yes
No
AXBS_5
Yes
No
No
No
No
AXBS_6
Yes
No
No
No
No
1. AXBS for S32K311 does not have programming model.
Table 46. AXBS connectivity matrix for S32K388/S32K389
Instance
Initiator and target assignments
AXBS_0 (main)
Initiator 
port
Initiator module
Target port Target module
M0
Cortex-M7_0 AHBM
S0
S32K388: Flash memory port 0
S32K389: Flash memory 0 port 0
M1
DMA
S1
S32K388: Flash memory port 1
S32K389: Flash memory 1 port 0
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
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
501 / 5251


---
# 페이지 451

Instance
Initiator and target assignments
M4
Cortex-M7_1 AHBM
S4
S32K388: Flash memory Port 2
S32K389: Flash memory 0 port 1
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
S32K388: Flash memory port 3
S32K389: Flash memory 1 port 1
AXBS_1 (peripheral)
Initiator 
port
Initiator module
Target port Target module
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
AXBS_2 (eDMA)
Initiator 
port
Initiator module
Target port Target module
M0
eDMA
S0
System AXBS
S1
Peripheral AXBS
AXBS_3 (Cortex-M7 TCM)
Initiator 
port
Initiator module
Target port Target module
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
AXBS_4 (TCM PRAM)
Initiator 
port
Initiator module
Target port Target module
M0
System AXBS
S0
PRAM_2
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
502 / 5251


---
# 페이지 452

Table 46. AXBS connectivity matrix for S32K388/S32K389 (continued)
Instance
Initiator and target assignments
S1
TCM AXBS
S2
PRAM_3
AXBS_5 (ACE 
HSE_B AXBS)
Initiator 
port
Initiator module
Target port Target module
M0
HSE_B
S0
Main AXBS
M1
ACE
S1
Peripheral AXBS
AXBS_6 (ACE AXBS)
Initiator 
port
Initiator module
Target port Target module
M0
ACE M0
S0
ACE HSE AXBS
M1
ACE M1
Table 47. AXBS connectivity matrix for S32K358/S32K348/S32K338/S32K328
Instance
Initiator and target assignments
AXBS_0 (main)
Initiator 
port
Initiator module
Target port Target module
M0
Cortex-M7_0 AHBM
S0
Flash memory port 0
M1
AXBS_2 S0
S1
Flash memory port 1
M2
AXBS_4 S0
S2
PRAM_0
M3
GMAC
S3
PRAM2_TCM splitter
M4
Cortex-M7_1 AHBM
S4
Flash memory port 2
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
AXBS_1 (peripheral)
Initiator 
port
Initiator module
Target port Target module
M0
Cortex-M7_0 AHBP
S0
AIPS_0
M1
AXBS_2 S1
S1
AIPS_1
M2
AXBS_4 S1
S2
AIPS_2
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
503 / 5251


---
# 페이지 453

Instance
Initiator and target assignments
M3
Cortex-M7_1 AHBP
M4
Cortex-M7_2 AHBP
AXBS_2 (eDMA)
Initiator 
port
Initiator module
Target port Target module
M0
eDMA
S0
AXBS_0 M1
M1
Reserved
S1
AXBS_1 M1
AXBS_3 (Cortex-M7 TCM)
Not applicable
AXBS_4 (HSE)
Initiator 
port
Initiator module
Target port Target module
M0
HSE_B
S0
AXBS_0 M2
S1
AXBS_1 M2
AXBS_5 (TCM_PRAM)
Initiator 
port
Initiator module
Target port Target module
M0
AXBS_0 S3
S0
PRAM_2
S1
Cortex-M7_0 TCM
S2
Cortex-M7_1 TCM
S3
Cortex-M7_2 TCM
Table 48. AXBS connectivity matrix for S32K344, S32K324, S32K314, S32K342, S32K322, S32K341, and S32K322
Instance
Initiator and target assignments
AXBS_0 (main)
Initiator 
port
Initiator module
Target port Target module
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
Flash memory port 2
S5
QuadSPI
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
504 / 5251


---
# 페이지 454

Instance
Initiator and target assignments
S6
PRAM_12
1. These ports are reserved for S32K314.
2. These ports are reserved for S32K342/S32K322/S32K341.
AXBS_1 (peripheral)
Initiator 
port
Initiator module
Target port Target module
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
AXBS_2 (eDMA)
Initiator 
port
Initiator module
Target port Target module
M0
eDMA
S0
AXBS_0 M1
S1
AXBS_1 M1
AXBS_3 (Cortex-M7 TCM)
Initiator 
port
Initiator module
Target port Target module
M0
AXBS_0 S3
S0
Cortex-M7_0 TCM
S11
Cortex-M7_1 TCM
AXBS_4 (HSE)
Initiator 
port
Initiator module
Target port Target module
M0
HSE_B
S0
AXBS_0 M2
S11
AXBS_1 M2
Table 49. AXBS connectivity matrix for S32K311 and S32K312
Instance
Initiator and target assignments
AXBS_0 (main)
Initiator 
port
Initiator module
Target port Target module
M0
Cortex-M7 AHBM
S0
Flash memory port 0
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
505 / 5251


---
# 페이지 455

Instance
Initiator and target assignments
M1
eDMA
S1
Flash memory port 1
M2
HSE_B
S2
PRAM_0
M3
Cortex-M7 AHBP
S3
Cortex-M7 TCM
M4
Reserved
S4
AIPS_0
S5
AIPS_1
12.2 Overview
This section provides information on the layout, configuration, and programming of the crossbar switch.
The crossbar switch connects bus initiators and bus targets using a crossbar switch structure. This structure allows all bus 
initiators to access different bus targets simultaneously, while providing arbitration among the bus initiators when they access the 
same target. A variety of bus arbitration methods and attributes may be programmed on a target-by-target basis.
12.2.1 Features
• Symmetric crossbar bus switch implementation
— Allows concurrent access from different Initiators to different Targets
— Target arbitration attributes configured on a Target-by-Target basis
• Single-clock 64-bit transfer
• Support for burst transfers of 64 bits of data
• Support for low-power park mode
• Initiator high-priority elevation
• 64-bit AHB crossbar bus switch compatible with ARM's AMBA Specification v2.0
12.3 Functional description
Information about general operation and arbitration are provided in this section.
12.3.1 General operation
When a Initiator accesses the crossbar switch, the access is immediately taken. If the targeted target port of the access is 
available, then the access is immediately presented on the target port. Single-clock or zero-wait-state accesses are possible 
through the crossbar. If the targeted target port of the access is busy or parked on a different Initiator port, the requesting Initiator 
sees wait states inserted until the targeted target port can service the Initiator's request. The latency in servicing the request 
depends on each Initiator's priority level and the responding target's access time.
Because the crossbar switch appears to be just another target to the Initiator device, the Initiator device does not know whether 
it owns the target port it is targeting. The Initiator waits while it does not have control of the target port it is targeting.
After the Initiator acquires control of the target port, it controls the port until it relinquishes the port by running an IDLE cycle or by 
targeting a different target port for its next access.
The Initiator can also lose control of the target port if another higher-priority Initiator makes a request to the target port. However, 
if the Initiator is running a fixed-length burst transfer, it retains control of the target port until that transfer completes.
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
506 / 5251


---
# 페이지 456

The crossbar terminates all Initiator IDLE transfers, as opposed to allowing the termination to come from one of the target buses. 
Additionally, when no Initiator is requesting access to a target port, the crossbar drives IDLE transfers onto the target bus, even 
though a default Initiator may be granted access to the target port.
When a target bus is being idled by the crossbar, it can park the target port on the Initiator port indicated by CRSn[PARK]. This is 
done to save the initial clock of arbitration delay that otherwise would be seen if the same Initiator had to arbitrate to gain control 
of the target port. The target port can also be put into low-power park mode to save power, by using CRSn[PCTL].
12.3.2 Register coherency
The operation of the crossbar is affected as soon as a register is written. The values of the registers do not track with 
target-port-related Initiator accesses, but instead track only with target accesses.
12.3.3 Arbitration
The crossbar switch supports the following arbitration algorithms:
• Fixed priority
• Round-robin
The arbitration scheme is independently programmable for each target port.
12.3.3.1
Fixed-priority operation
When operating in fixed-priority mode, each initiator is assigned a unique priority level in the priority registers (PRSn). If two 
initiators request access to the same target port, the initiator with the highest priority in the selected priority register gains control 
over the target port.
 
In this arbitration mode, a higher-priority initiator can monopolize a target port, preventing access from any 
lower-priority initiator to the port.
  NOTE  
When a initiator makes a request to a target port, the target port checks whether the new requesting initiator's priority level is higher 
than that of the initiator that currently has control over the target port, unless the target port is in a parked state. The target port 
performs an arbitration check at every clock edge to ensure that the initiator, if any, has control of the target port.
The following table describes possible scenarios based on the requesting initiator port.
Table 50. Methods of how the crossbar switch grants control of a target port to a initiator
When
Then the crossbar switch grants control to the requesting 
initiator
Both of the following are true:
• The current initiator is not running a transfer.
• The new requesting initiator's priority level is higher than 
that of the current initiator.
At the next clock edge
Both of the following are true:
• The current initiator is running a fixed-length burst 
transfer or a locked transfer.
• The requesting initiator's priority level is higher than that 
of the current initiator.
At the end of the burst transfer or locked transfer
The requesting initiator's priority level is lower than the 
current initiator.
At the conclusion of one of the following cycles:
Table continues on the next page...
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
507 / 5251


---
# 페이지 457

Table 50. Methods of how the crossbar switch grants control of a target port to a initiator (continued)
When
Then the crossbar switch grants control to the requesting 
initiator
• An IDLE cycle
• A non-IDLE cycle to a location other than the current 
target port
12.3.3.2
Round-robin priority operation
When operating in round-robin mode, each initiator is assigned a relative priority based on the initiator port number. This relative 
priority is compared to the initiator port number (ID) of the last initiator to perform a transfer on the target bus. The highest priority 
requests the initiator owns the target bus at the next transfer boundary, accounting for locked and fixed-length burst transfers. 
Priority is based on how far ahead the ID of the requesting initiator is of the ID of the last initiator.
After a initiator is granted access to a target port, a initiator may perform as many transfers as desired to that port until another 
initiator requests the same target port. The next initiator in line is granted access to the target port at the next transfer boundary, 
or possibly on the next clock cycle, if the current initiator has no pending access request.
As an example of arbitration in round-robin mode, assume that the crossbar is implemented with initiator ports 0, 1, 4, and 5. If 
the last initiator of the target port was initiator 1, and initiators 0, 4, and 5 make simultaneous requests, they are serviced in this 
order: 4,5, and then 0.
Parking may continue to be used in a round-robin mode, but does not affect the round-robin pointer unless the parked initiator 
performs a transfer. Handoff occurs to the next initiator in line after one cycle of arbitration. If the target port is put into low-power 
park mode, the round-robin pointer is reset to point at initiator port 0, giving it the highest priority.
12.3.3.3
Clocking
This module has no clocking considerations.
12.3.3.4
Interrupts
This module has no interrupts.
12.3.3.5
Priority assignment
Each initiator port must be assigned a unique 3-bit priority level. If an attempt is made to program multiple initiator ports with 
the same priority level within the priority registers (PRSn), the crossbar switch responds with a bus error and the registers are 
not updated.
12.4 External signals
This module has no external signals.
12.5 Initialization/application information
No initialization is required for the crossbar switch.
Hardware reset ensures that all the register bits used by the crossbar switch are properly initialized to a valid state. However, the 
following settings and priorities may be programmed to achieve the maximum system performance:
• During the configuration of the crossbar switch, all other initiators must be IDLE.
• To prevent reconfiguration of the crossbar switch, write 1 to CRSn[RO].
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
508 / 5251


---
# 페이지 458

12.6 Memory map and register definition
Each target port of the crossbar switch contains configuration registers. Read- and write transfers require two bus clock cycles. 
The registers can be read from and written to only in supervisor mode. Additionally, these registers can be read from or written 
to only by 32-bit accesses.
A bus error response is returned if an unimplemented location is accessed within the crossbar switch.
The CRSn and PRSn registers can be programmed as read-only to prevent changes to their configuration. After being read-only 
protected, future writes to them terminate with a data storage error.
 
This section shows the registers for all eight initiator and target ports. If a initiator or target is not used on this 
particular chip, then unexpected results occur when writing to its registers. See the chip configuration details for 
the exact initiator and target assignments for your chip.
All references to the crossbar switch registers are based on the physical port connections.
  NOTE  
12.6.1 AXBS register descriptions
12.6.1.1
AXBS memory map
AXBS_LITE base address: 4020_0000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Priority Target Registers (PRS0)
32
RW
7654_3210h
10h
Control Register (CRS0)
32
RW
0002_0110h
100h
Priority Target Registers (PRS1)
32
RW
7654_3210h
110h
Control Register (CRS1)
32
RW
0002_0110h
200h
Priority Target Registers (PRS2)
32
RW
7654_3210h
210h
Control Register (CRS2)
32
RW
0002_0110h
300h
Priority Target Registers (PRS3)
32
RW
7654_3210h
310h
Control Register (CRS3)
32
RW
0002_0110h
400h
Priority Target Registers (PRS4)
32
RW
7654_3210h
410h
Control Register (CRS4)
32
RW
0002_0110h
500h
Priority Target Registers (PRS5)
32
RW
7654_3210h
510h
Control Register (CRS5)
32
RW
0002_0110h
600h
Priority Target Registers (PRS6)
32
RW
7654_3210h
610h
Control Register (CRS6)
32
RW
0002_0110h
700h
Priority Target Registers (PRS7)
32
RW
7654_3210h
710h
Control Register (CRS7)
32
RW
0002_0110h
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
509 / 5251


---
# 페이지 459

12.6.1.2
Priority Target Registers (PRS0 - PRS7)
Offset
Register
Offset
PRS0
0h
PRS1
100h
PRS2
200h
PRS3
300h
PRS4
400h
PRS5
500h
PRS6
600h
PRS7
700h
Function
The priority target registers(PRSn) set the priority of each initiator port on a per target port basis and reside in each target port. 
The priority register can be accessed only with 32-bit access. After the CRSn[RO] bit is set, the PRSn register can only be read; 
attempts to write to it have no effect on PRSn and result in a bus-error response to the initiator initiating the write.
Two available initiators must not be programmed with the same priority level. Attempts to program two or more initiators with the 
same priority level result in a bus-error response and the PRSn is not updated.
 
Valid values for the Mn priority fields depend on which initiators are available on the chip. This information can be 
found in the chip-specific information for the crossbar.
• If the chip contains fewer than three initiators, only one bit is valid.
• If the chip contains fewer than five initiators, only two bits are valid.
• If five or more initiators are present, all three bits of the priority field are used.
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
0
M7 
0
M6 
0
M5 
0
M4 
W
Reset
0
1
1
1
0
1
1
0
0
1
0
1
0
1
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
M3 
0
M2 
0
M1 
0
M0 
W
Reset
0
0
1
1
0
0
1
0
0
0
0
1
0
0
0
0
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
510 / 5251


---
# 페이지 460

Fields
Field
Function
31
—
Reserved
30-28
M7
Initiator 7 Priority
This field sets the arbitration priority for this port on the associated target port.
000b - This initiator has level 1 or highest priority when accessing the target port.
001b - This initiator has level 2 priority when accessing the target port.
010b - This initiator has level 3 priority when accessing the target port.
011b - This initiator has level 4 priority when accessing the target port.
100b - This initiator has level 5 priority when accessing the target port.
101b - This initiator has level 6 priority when accessing the target port.
110b - This initiator has level 7 priority when accessing the target port.
111b - This initiator has level 8 or lowest priority when accessing the target port.
27
—
Reserved
26-24
M6
Initiator 6 Priority
This field sets the arbitration priority for this port on the associated target port.
000b - This initiator has level 1 or highest priority when accessing the target port.
001b - This initiator has level 2 priority when accessing the target port.
010b - This initiator has level 3 priority when accessing the target port.
011b - This initiator has level 4 priority when accessing the target port.
100b - This initiator has level 5 priority when accessing the target port.
101b - This initiator has level 6 priority when accessing the target port.
110b - This initiator has level 7 priority when accessing the target port.
111b - This initiator has level 8the or lowest priority when accessing the target port.
23
—
Reserved
22-20
M5
Initiator 5 Priority
This field sets the arbitration priority for this port on the associated target port.
000b - This initiator has level 1 or highest priority when accessing the target port.
001b - This initiator has level 2 priority when accessing the target port.
010b - This initiator has level 3 priority when accessing the target port.
Table continues on the next page...
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
511 / 5251


---
# 페이지 461

Table continued from the previous page...
Field
Function
011b - This initiator has level 4 priority when accessing the target port.
100b - This initiator has level 5 priority when accessing the target port.
101b - This initiator has level 6 priority when accessing the target port.
110b - This initiator has level 7 priority when accessing the target port.
111b - This initiator has level 8 or lowest priority when accessing the target port.
19
—
Reserved
18-16
M4
Initiator 4 Priority
This field sets the arbitration priority for this port on the associated target port.
000b - This initiator has level 1 or highest priority when accessing the target port.
001b - This initiator has level 2 priority when accessing the target port.
010b - This initiator has level 3 priority when accessing the target port.
011b - This initiator has level 4 priority when accessing the target port.
100b - This initiator has level 5 priority when accessing the target port.
101b - This initiator has level 6 priority when accessing the target port.
110b - This initiator has level 7 priority when accessing the target port.
111b - This initiator has level 8 or lowest priority when accessing the target port.
15
—
Reserved
14-12
M3
Initiator 3 Priority
This field sets the arbitration priority for this port on the associated target port.
000b - This initiator has level 1 or highest priority when accessing the target port.
001b - This initiator has level 2 priority when accessing the target port.
010b - This initiator has level 3 priority when accessing the target port.
011b - This initiator has level 4 priority when accessing the target port.
100b - This initiator has level 5 priority when accessing the target port.
101b - This initiator has level 6 priority when accessing the target port.
110b - This initiator has level 7 priority when accessing the target port.
111b - This initiator has level 8the or lowest priority when accessing the target port.
11
—
Reserved
10-8
Initiator 2 Priority
Table continues on the next page...
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
512 / 5251


---
# 페이지 462

Table continued from the previous page...
Field
Function
M2
This field sets the arbitration priority for this port on the associated target port.
000b - This initiator has level 1 or highest priority when accessing the target port.
001b - This initiator has level 2 priority when accessing the target port.
010b - This initiator has level 3 priority when accessing the target port.
011b - This initiator has level 4 priority when accessing the target port.
100b - This initiator has level 5 priority when accessing the target port.
101b - This initiator has level 6 priority when accessing the target port.
110b - This initiator has level 7 priority when accessing the target port.
111b - This initiator has level 8the or lowest priority when accessing the target port.
7
—
Reserved
6-4
M1
Initiator 1 Priority
This field sets the arbitration priority for this port on the associated target port.
000b - This initiator has level 1 or highest priority when accessing the target port.
001b - This initiator has level 2 priority when accessing the target port.
010b - This initiator has level 3 priority when accessing the target port.
011b - This initiator has level 4 priority when accessing the target port.
100b - This initiator has level 5 priority when accessing the target port.
101b - This initiator has level 6 priority when accessing the target port.
110b - This initiator has level 7 priority when accessing the target port.
111b - This initiator has level 8 or lowest priority when accessing the target port.
3
—
Reserved
2-0
M0
Initiator 0 Priority
This field sets the arbitration priority for this port on the associated target port.
000b - This initiator has level 1 or highest priority when accessing the target port.
001b - This initiator has level 2 priority when accessing the target port.
010b - This initiator has level 3 priority when accessing the target port.
011b - This initiator has level 4 priority when accessing the target port.
100b - This initiator has level 5 priority when accessing the target port.
101b - This initiator has level 6 priority when accessing the target port.
110b - This initiator has level 7 priority when accessing the target port.
Table continues on the next page...
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
513 / 5251


---
# 페이지 463

Table continued from the previous page...
Field
Function
111b - This initiator has level 8 or the lowest priority when accessing the target port.
12.6.1.3
Control Register (CRS0 - CRS7)
Offset
Register
Offset
CRS0
10h
CRS1
110h
CRS2
210h
CRS3
310h
CRS4
410h
CRS5
510h
CRS6
610h
CRS7
710h
Function
These registers control several features of each target port and must be accessed using 32-bit accesses. After CRSn[RO] is set, 
the PRSn can only be read; attempts to write to it have no effect and results in an error response.
 
See the chip-specific crossbar information for the reset value of this register.
Not all HPE n fields may be active. See the chip-specific crossbar information for which initiators support initiator 
high-priority elevation. Setting a field corresponding to a initiator that does not support initiator, high-priority 
elevation has no effect.
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
RO 
HLP 
0
HPE7 
HPE6 
HPE5 
HPE4 
HPE3 
HPE2 
HPE1 
HPE0 
W
1
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
ARB 
0
PCTL 
0
PARK 
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
0
0
0
1
0
0
0
0
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
514 / 5251


---
# 페이지 464

Fields
Field
Function
31
RO
Read Only
Forces the PRSn and CRSn registers to be read-only. After being set, only a hardware reset clears this field.
0b - The CRSn and PRSn registers are writeable
1b - The CRSn and PRSn registers are read-only and cannot be written (attempted writes have 
no effect on the registers and result in a bus error response).
30
HLP
Halt Low Priority
This field sets the initial arbitration priority for low power-mode requests . Setting this bit will not affect 
the ,request for low power-mode from attaining the highest priority after it has control of the target ports.
0b - The low-power mode request has the highest priority for arbitration on this target port.
1b - The low-power mode request has the lowest initial priority for arbitration on this target port.
29-24
—
Reserved
23
HPE7
High Priority Elevation 7
This field enables initiator high-priority elevation for initiator 7 on this target port. If enabled, the initiator is 
able to elevate its priority to the highest.
0b - Initiator high-priority elevation for initiator 7 is disabled on this target port.
1b - Initiator high-priority elevation for initiator 7 is enabled on this target port.
22
HPE6
High Priority Elevation 6
This field enables initiator high-priority elevation for initiator 6 on this target port. If enabled, the initiator is 
able to elevate its priority to the highest.
0b - Initiator high-priority elevation for initiator 6 is disabled on this target port.
1b - Initiator high-priority elevation for initiator 6 is enabled on this target port.
21
HPE5
High Priority Elevation 5
This field enables initiator high-priority elevation for initiator 5 on this target port. If enabled, the initiator is 
able to elevate its priority to the highest.
0b - Initiator high-priority elevation for initiator 5 is disabled on this target port.
1b - Initiator high-priority elevation for initiator 5 is enabled on this target port.
20
HPE4
High Priority Elevation 4
This field enables initiator high-priority elevation for initiator 4 on this target port. If enabled, the initiator 
can elevate its priority to the highest.
0b - Initiator high-priority elevation for initiator 4 is disabled on this target port.
1b - Initiator high-priority elevation for initiator 4 is enabled on this target port.
19
High Priority Elevation 3
Table continues on the next page...
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
515 / 5251


---
# 페이지 465

Table continued from the previous page...
Field
Function
HPE3
This field enables initiator high-priority elevation for initiator 3 on this target port. If enabled, the initiator 
can elevate its priority to the highest.
0b - Initiator high-priority elevation for initiator 3 is disabled on this target port.
1b - Initiator high-priority elevation for initiator 3 is enabled on this target port.
18
HPE2
High Priority Elevation 2
This field enables initiator high-priority elevation for initiator 2 on this target port. If enabled, the initiator 
can elevate its priority to the highest.
0b - Initiator high-priority elevation for initiator 2 is disabled on this target port.
1b - Initiator high-priority elevation for initiator 2 is enabled on this target port.
17
HPE1
High Priority Elevation 1
This field enables initiator high-priority elevation for initiator 1 on this target port. If enabled, the initiator 
can elevate its priority to the highest.
0b - Initiator high-priority elevation for initiator 1 is disabled on this target port.
1b - Initiator high-priority elevation for initiator 1 is enabled on this target port.
16
HPE0
High Priority Elevation 0
This field enables initiator high-priority elevation for initiator 0 on this target port. If enabled, the initiator 
can elevate its priority to the highest.
0b - Initiator high-priority elevation for initiator 0 is disabled on this target port.
1b - Initiator high-priority elevation for initiator 0 is enabled on this target port.
15-10
—
Reserved
9-8
ARB
Arbitration Mode
This field selects the arbitration policy for the target port.
00b - Fixed priority
01b - Round-robin (rotating) priority
10b - Reserved
11b - Reserved
7-6
—
Reserved
5-4
PCTL
Parking Control
This field determines the target port's parking control. The low-power park feature results in an overall 
power savings if the target port is not saturated; however, this forces an extra latency clock when any 
initiator tries to access the target port when not in use because it is not parked on any initiator.
Table continues on the next page...
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
516 / 5251


---
# 페이지 466

Table continued from the previous page...
Field
Function
00b - When no initiator makes a request, the arbiter parks the target port on the initiator port 
defined by the PARK bit field.
01b - When no initiator makes a request, the arbiter parks the target port on the last initiator to be 
in control of the target port.
10b - Low-power park. When no initiator makes a request, the target port is not parked on a 
initiator and the arbiter drives all outputs to a constant safe state.
11b - Reserved
3
—
Reserved
2-0
PARK
Park
This field determines which initiator port the current target port parks on when no initiators are actively 
making requests and the PCTL bits are cleared.
 
Select only initiator ports that are present on the chip. Otherwise, undefined behavior 
might occur.
  NOTE  
000b - Park on initiator port M0
001b - Park on initiator port M1
010b - Park on initiator port M2
011b - Park on initiator port M3
100b - Park on initiator port M4
101b - Park on initiator port M5
110b - Park on initiator port M6
111b - Park on initiator port M7
12.7 Glossary
AMBA
Advanced Microcontroller Bus Architecture
IDLE
A type of transfer that a initiator uses when it does not want to perform a data transfer
ID
Initiator port number
NXP Semiconductors
Crossbar Switch (AXBS)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
517 / 5251


---