# 페이지 257

Chapter 40
Messaging Unit (MU)
40.1 Chip-specific MU information
40.1.1 MU instances and configuration
This chip includes MUs for communication across the different cores. Each MU includes two interfaces, MUA and MUB. Two 
different processors control them for communication.
Table 235 indicates the MUs and their interfaces present in different parts of the S32K3 chip family. The table also summarizes 
the implementation of this module in each chip of the S32K3 product series.
 
The HSE_B core controls the MUA interface of MU_0 and MU_1. Therefore, the application core cannot control 
the interface.
  NOTE  
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1509 / 5251


---
# 페이지 258

Table 235. MU instances
Instance
S32K388, 
S32K389
S32K328, 
S32K338, 
S32K358
S32K348
S32K344
S32K324
S32K314
S32K342, 
S32K341
S32K322
S32K312
S32K311, 
S32K310
Use case
MU_0
Yes
Communication between HSE_B 
and application cores
MU_1
Yes
MU_2
Yes
No
Yes
No
Yes
No
Communication between 
application cores
MU_3
Yes
No
MU_4
Yes
No
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1510 / 5251


---
# 페이지 259

The base address of MU_1's MUB interface is different across the S32K3xx product series because AIPS_2 is unavailable in 
S32K312 and S32K311. Table 236 summarizes this difference.
Table 236. Base-address difference in MU_1's MUB interface across S32K3xx product series
S32K388, S32K389, S32K328, S32K338, S32K348, S32K358, 
S32K344, S32K324, S32K314, S32K342, S32K341, S32K322
S32K312, S32K311, S32K310
Base address
404E_C000h
4039_0000h
 
• For S32K344/S32K324/S32K314/S32K312/S32K311/S32K310 reset value of MUA_VER and MUB_VER 
register is 0300_000Fh.
• For others, reset value of MUA_VER and MUB_VER register is 0309_000Fh.
  NOTE  
40.2 Overview
MU enables two processors on a chip to communicate and coordinate by passing messages (for example, data, status, and 
control) through the MU interface. MU also allows one processor to signal the other processor using interrupts.
MU must synchronize the accesses from one side to the other because MU can manage messaging between processors using 
different clocks. MU accomplishes synchronization using two sets of matching registers: processor A-facing and processor B-
facing.
40.2.1 Block diagram
Processor A
MUA
MUB
Processor B
MU
Processor B
peripheral
bus
TX and RX
registers
Status and
control
registers
Status and
control
registers
Sync and
control
registers
Sync and
control
registers
Generate
interrupts
TX and RX
registers
Generate
interrupts
Interrupts to
processor B
interrupt
controller
Interrupts to
processor A
interrupt
controller
Processor A
peripheral
bus
Figure 167. Block diagram
40.2.2 Features
• Memory-mapped registers (MU is connected as a peripheral under the peripheral bus on the processor A-side and 
processor B-side)
• Synchronized message transfers between cores
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1511 / 5251


---
# 페이지 260

— To send data or messages from one side to the other, MUA provides 4 transmit registers and 4 receive registers. 
MUB provides 4 transmit registers and 4 receive registers.
— Transmit empty flags (TSR[TEn]) and receive full flags (RSR[RFn]) facilitate the transfer of data or messages 
between cores on both sides of MU.
— A synchronization mechanism updates the transmit and the receive flags. There is an inherent latency between 
updating the flag on one side and reflecting its status on the other side. See Event update timing.
— MU has a 3-bit flag data register, which you can use to send flag data between the two MU sides.
• Interprocessor interrupts
— MU has 9 interrupt sources on each side (processor A-side, processor B-side) for signaling the other processor. 
You can use the interrupts for notification of receive and transmit events and for general-purpose signaling between 
processors. There are 1 general-purpose interrupt requests available and 8 receive and transmit interrupt sources.
• Reset (Each processor can issue a reset to MU via CR[MUR], which is a self-clearing field).
40.3 Functional description
MU enables two cores (processor A and processor B) to communicate with each other:
• By sharing messages and data.
• By enabling one core to wake the other core by using interrupts.
The messaging, control, and status registers of the two cores are mapped to processor A memory and processor B memory as 
a regular peripheral. The peripheral data bus is 32 bits wide inside MU.
Messaging logic is used with shared memory. Various messaging methods can implement a messaging protocol. For example, 
a message could mean one of the following:
• A message of n words has been written starting at offset x in the memory.
• The previous data block that was sent has been read.
The ability to keep messaging logic independent of the shared memory is not restricted to a predefined hardware protocol. The 
software required to manage the messaging is short and straightforward.
Most of the messaging mechanisms are symmetric. They are duplicated and are available on both the processor A side and 
processor B side. The messaging mechanisms are:
• 4 32-bit transmit registers, which are each reflected in 4 read-only receive registers on the side of the other processor. 
These registers can transfer 32-bit word messages or the frame information of the messages written to the shared 
memory. For example, they can transfer the number of words, initial address, and message type code.
• Writing to a transmitter-side transmit register (TRn) clears the Transmitter Empty flag in the transmitter-side Status register 
(TSn[TEn]), and sets the Receiver Full flag in the receiver-side Status register (RSn[RFn]). Setting the flag on the receiver 
side can trigger an interrupt on the receiver side (a maskable receive interrupt).
• Reading a receiver-side receive register (RRn) clears the Receiver Full flag in the receiver-side Status register 
(RSn[RFn]), and sets the Transmitter Empty flag in the transmitter-side Status register (TSn[TEn]). Setting the Transmitter 
Empty flag can trigger an interrupt on the transmitter side (a maskable transmit interrupt).
• 1 general-purpose interrupt request flags are reflected in General-purpose Status (GSR) on the receiver side.
• 3-bit flag data is transmitted from Flag Control (FCR) to Flag Status (FSR) on the side receiving the flag data. SR[FUP] 
sets when the flag data is transmitted and clears when the receiving side acknowledges the flag data (the flag is updated).
Writing to a transmit register signals to the receiver side that data is ready for retrieval.
Do not write to the transmit register again without verifying that the data is retrieved. The transmitter side cannot determine the 
exact time that the receiver attempts to retrieve the data. Before attempting to write to the transmit register again, the transmitter 
side must wait for the Transmitter Empty interrupt or it must poll TSR[TEn].
Reading a receive register signals to the transmitter side that data can be written to that register.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1512 / 5251


---
# 페이지 261

Do not read the receive register again without verifying that the data is written. The receiver side cannot determine the exact time 
that the transmitter attempts to write the data. Before attempting to read the receive register again, the receiver side must wait for 
the Receiver Full interrupt or it must poll RSR[RFn].
40.3.1 Submodules
40.3.1.1
MUA side
MUA receives its register configuration via the processor A peripheral bus. It sends or receives messages to or from MUB. 
Processor A can receive messages by reading MUA registers, and MUA can send interrupts to processor A when interrupts 
are enabled.
 
Processor B should not access MUA registers. Processor C, if exist, should also not access MUA registers. TRDC 
might be needed to prevent such illegal access of Processor B or C to MUA registers.
  NOTE  
40.3.1.2
MUB side
MUB receives its register configuration via the processor B peripheral bus. It sends or receives messages to or from MUA. 
Processor B can receive messages by reading MUB registers, and MUB can send interrupts to processor B when interrupts 
are enabled.
 
Processor A should not access MUB registers. Processor C, if exist, should also not access MUB registers. TRDC 
might be needed to prevent such illegal access of Processor A or C to MUB registers.
  NOTE  
40.3.2 Event update timing
The messaging side of each processor has a hardware mechanism to send event update requests to the other processor. An event 
occurs when the status register of the receiving processor must reflect any information change. The event update latency is the 
delay between the event being ready at one processor and the resulting update at the status register of the other processor:
• The minimum event latency is (1 clock cycle of the sending side) + (2.5 clock cycles of the receiving side). This minimum 
case happens when no event is pending when the new event occurs.
• The maximum event latency is (6 clock cycles of the sending side) + (6.5 clock cycles of the receiving side). The 
maximum case happens when the event occurs just after a previous event is sent to the other side.
The event update latency varies depending on the time at which the subsequent event is triggered.
40.3.3 Clocking
Table 237. MU clocks
Clock name
Description
Bus clock MUA
Used only for bus accesses to MUA control and configuration registers
Bus clock MUB
Used only for bus accesses to MUB control and configuration registers
40.3.4 Resets
The following sections list the reset sources included in MU. Each reset performs a different function for the MU module compared 
to the function it performs for the system.
40.3.4.1
Asynchronous system reset
When the asynchronous system reset on either side of MU is asserted, SR[MURS] becomes 1 until the asynchronous system 
reset sequence on both the MUA and MUB sides ends. Verify that SR[MURS] becomes 0 before accessing MU.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1513 / 5251


---
# 페이지 262

The asynchronous system reset on one side of MU resets the other side of MU. The reset forces all control and status registers 
to return to their default values and clears all internal states. The following table shows the exceptions to this behavior.
Table 238. Exceptions to asynchronous system reset
MUA-side exceptions
MUB-side exceptions
MUB_CR[MURIE]
MUB_SR[MURIP]
MUB_SR[MURS]
MUA_CR[MURIE]
MUA_SR[MURIP]
MUA_SR[MURS]
40.3.4.2
MU software reset
Writing 1 to CR[MUR] causes most control and status registers to return to their default values and clears all internal states.
The instruction immediately following the assertion of CR[MUR] must not write to the MU registers. The reset sequence may 
overwrite such a write, with the register retaining the reset value. To know the end of the reset sequence for both processors, 
monitor the value of SR[MURS]. After the reset sequence on both processors has ended, a write to the MU registers can 
be attempted.
 
The process of CR[MUR] becoming 1 is delicate because it asynchronously affects the registers on the other side. 
CR[MUR] becoming 1 may cause unpredictable behavior if, for example, the other processor is concurrently testing 
an MU register field (TSR[TEn] in the other processor). Before writing 1 to CR[MUR], verify that the other processor 
is not engaged in an MU signaling activity.
  NOTE  
40.3.5 Interrupts
MU controls interrupt requests that one processor makes to the other processor. This section describes all the interrupts that the 
module generates.
MU can generate these interrupt sources individually to send to the processors:
• 4 receive interrupts (asserted when the Receive Full flags are set in Receive Status (RSR) and enabled in Receive 
Control (RCR)) for each receive register
• 4 transmit interrupts (asserted when the Transmit Empty flags are set in Transmit Status (TSR) and enabled in Transmit 
Control (TCR)) for each transmit register
• 1 general-purpose interrupt (asserted when the GIP flag is set in General-Purpose Interrupt Enable (GIER) and enabled in 
General-Purpose Interrupt Enable (GIER))
All interrupts are maskable in the processor control registers: TCR, RCR, GIER, and CR. MU does not assume any internal priority 
of these interrupts. Multiple interrupts (for example, receive 0 and receive 1, or any transmit or general-purpose interrupt) can be 
asserted simultaneously. The interrupt controller must resolve the priority of these interrupts at the chip level.
Triggering any enabled interrupt wakes the processor from below mode before servicing the interrupt
The software (as part of the interrupt handler) must clear the general-purpose interrupt pending flag (GSR[GIP0]) to deassert the 
request to the interrupt controller.
When a processor writes to the general-purpose interrupt flag (GCR[GIR0]), MU synchronizes the write event to the other 
processor to set the general-interrupt request pending flag (GSR[GIP0]). When GSR[GIP0] is set, if the general-purpose interrupt 
is enabled on the receiving processor side (GIER[GIE0] is 1), the transmitting-side general-purpose interrupt is issued to the 
receiving processor, which clears this interrupt by writing 1 to GSR[GIP0]. The interrupt is deasserted as soon as the write to 
GSR[GIP0] occurs. MU synchronizes the write event of GSR[GIP0] to the other processor. The synchronized signal clears the 
GIR0 flag.
Before writing 1 to GCR[GIR0], verify that this field is 0, which means that a general interrupt is not pending. Generally, MU ignores 
writing 1 to this field while the field is already 1, but in some cases it may issue a second interrupt.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1514 / 5251


---
# 페이지 263

40.4 External signals
This module has no external signals.
40.5 Initialization
MU does not require initialization.
40.6 Application information
MU facilitates messages between processors. For example, MU passes:
• Short messages. Transmit registers can pass short messages from 1 to 4 words in length for processor A and from 1 to 
4 words for processor B. For example, for a four-word message, only one register must have its corresponding interrupt 
enabled on the receiving side. The first three words of the message are written to the registers with masked interrupts. 
The fourth word is written to the last register, triggering an interrupt on the receiving side.
• Frame information. Transmit registers can pass frame information for long messages written to the shared system 
memory. Such frame information normally includes a start address and a number of words. It can include a message type 
code.
• Event notices and requests. MU can signal events and requests that do not include data words between processors using 
general-purpose interrupts. For example, one such event is acknowledging that a long message is read from the shared 
system memory.
• Fixed-length data. Formatted data with a fixed length can be written to predetermined locations in the shared memory. A 
processor can use general-purpose interrupts to signal to the other processor that the data is ready.
• Announcements. A processor can use the 3 flags to announce its current program state or other billboard messages to the 
other processor.
40.6.1 Messaging protocols using interrupts
The example below describes a four-word messaging sequence sent between the processor A and processor B.
The transmitting processor writes to the transmit registers sequentially. When n = 0, 1, and 2, the interrupts are disabled, so no 
interrupt goes to the processor (although interrupt conditions occur). For n = 3, the interrupt is enabled, and MU generates the last 
receive interrupt request.
1. Write sequence:
a. The transmitting processor writes the message information sequentially to its Transmit registers 0, 1, 2.
b. When the write to Transmit register 3 occurs, RSR[RF3] is set after synchronization. It immediately triggers the 
receive full 3 interrupt on the receiving processor.
2. Read sequence:
a. The receiving processor receives the receive full 3 interrupt and starts reading the message transferred from the 
receive registers.
b. After the receiving processor reads Receive register 3, MU clears RSR[RF3].
Table 239 and Figure 168 describe the messaging model, using transmit and receive registers and the interrupt 
messaging protocol.
Table 239. Interrupt messaging protocol (generalized)
Step
Action
Description
1
Processor A writes data.
RRn on processor B's side reflects a data write to TRn by 
processor A.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1515 / 5251


---
# 페이지 264

Table 239. Interrupt messaging protocol (generalized) (continued)
Step
Action
Description
2
Clear the transmitter empty flag and 
set the receiver full flag.
The data write to TRn:
• Clears TSR[TEn] on the processor A side.
• Sets RSR[RFn] on the processor B side.
3
Generate the receive interrupt 
request.
Setting RSR[RFn] generates a receive interrupt request to 
processor B.
4
Processor B reads the data.
After receiving the receive interrupt request, processor B 
performs a data read of RRn.
5
Clear the receiver full flag and set 
the transmitter empty flag.
Reading the data from the RRn register:
• Clears RSR[RFn] on the processor B side.
• Sets TSR[TEn] on the processor A side.
6
Generate the transmit interrupt 
request.
Setting TSR[TEn] generates a transmit interrupt request to 
processor A.
Processor A
Processor B
Tx status
Data write
Rx status
Tx control
Rx control
Data read
MU
Transmitter side
Receiver side
Tx empty
TEn
Rx full
RFn
A write from the
fourth transmit register
triggers an interrupt
A read from the
fourth receive register
triggers an interrupt
Transmit
interrupt
request
Set
Clear
Set
Clear
Interrupt
enable
Interrupt
enable
Receive
interrupt
request
RIEn
TIEn
3
1
6
Registers
Registers
2
5
4
Figure 168. Messaging model using transmit and receive registers
You can use the messaging hardware to implement messaging protocols for an array of message types. MU provides full support 
for interrupt and polling management schemes.
40.6.2 Messaging protocols using event interrupts
MU can signal events and requests that do not include data words between processors using general-purpose interrupts.
Formatted data with a fixed length can be written to predetermined locations in the shared memory. A processor can use a 
general-purpose interrupt to signal to the other processor that the data is ready.
A processor can use the 3 flags to announce its current program state (or similar messages) to the other processor.
Table 240 and Figure 169 describe the event steps when the processor triggers a general-purpose interrupt.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1516 / 5251


---
# 페이지 265

Table 240. General-purpose interrupt messaging protocol (generalized)
Step
Action
Description
1
Processor A sets its associated 
general-purpose interrupt request 
flag.
Processor A sets GCR[GIR0].
2
The general-purpose interrupt 
request pending status flag is set.
GSR[GIP0] is set.
3
MU generates the general-purpose 
interrupt request to processor B.
Setting GSR[GIP0] generates the general-purpose interrupt 
request to processor B. GIER[GIE0] must be set for 
processor B.
4
Processor B reads the status 
register.
Processor B reads GSR[GIP0].
5
Processor B services the interrupt.
—
6
Processor B sets GSR[GIP0] to clear 
the interrupt.
Processor B writes 1 to the corresponding GSR[GIP0] flag to 
clear the interrupt.
7
GCR[GIR0] is cleared.
Setting GSR[GIP0] clears GCR[GIR0] on the processor A 
side.
Processor A
Processor B
Messaging Unit (MU)
GIR0
int req
Control
Status
Control
GIP0
int pend
GIE0
Interrupt
Enable
set
clear
General Purpose
Interrupt Request
Read GIP0 bit
2
3
GCR
Register
GSR
Register
GIER
Register
7
1
set
6
Write "1" to clear
4
5
Services
Interrupt
Figure 169. Messaging model using a general-purpose interrupt
40.6.3 Exclusive access to shared memory
MU can signal one processor about its current access to shared memory. This signaling prevents the other processor from 
overwriting data during the exclusive memory access period.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1517 / 5251


---
# 페이지 266

The following tables describe the signaling protocol that processor A uses to inform processor B about its current access (write) 
to shared memory:
• Table 241 shows processor A performing an exclusive access to shared memory.
• Table 242 shows processor B scanning for transaction information.
• Table 243 shows processor B accepting exclusive access from processor A.
• Table 244 shows processor B rejecting exclusive access from processor A.
According to the examples shown in the following tables, GCR[GIR0], RRn, and TRn are reserved to support exclusive access 
to the shared memory protocol.
Table 241. Processor A performs an exclusive access to shared memory
Step
Action
Description
1
Processor A sends the GIR0 
request to processor B using the 
processor A control register.
Before processor A performs an exclusive access to the 
shared memory, it sends a GIR0 request to processor B.
2
Processor A sends an exclusive-
access request using a transmit 
data register (TRn).
Processor A sends an exclusive-access request (command, 
location, and length of target access) to processor B using a 
selected transmit data register (TR0).
3
Processor A waits for a dedicated 
interrupt from processor B.
Processor A waits for a dedicated interrupt (as 
an acknowledgment) triggered by processor B before 
proceeding.
4
Processor A accesses the shared 
memory.
After receiving a dedicated interrupt from processor B, 
processor A proceeds.
Table 242. Processor B scans for transaction information
Step
Action
Description
1
Processor B receives an interrupt 
from a receive data register (RRn).
—
2
Processor B reads the receive data 
register (RRn).
—
3
Processor B scans the receive data 
register contents.
Processor B scans for transaction information (whether 
processor A has requested exclusive access).
Table 243. Processor B accepts exclusive access from processor A
Step
Action
Description
1
Processor B triggers a dedicated 
interrupt.
Processor B acknowledges the request from processor A by 
triggering a dedicated interrupt (ack) to processor A.
2
Processor B sends a code message 
to processor A.
With the acknowledge interrupt, processor B sends a code 
message to processor A through the selected transmit 
register (TRn). The message informs processor A that it can 
exclusively access the shared memory.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1518 / 5251


---
# 페이지 267

Table 244. Processor B rejects exclusive access from processor A
Step
Action
Description
1
Processor B ignores the request 
from processor A for exclusive 
access.
If processor B does not provide permission to processor A, 
processor B ignores the exclusive-access request.
40.6.4 Packet data transfers
The following table describes an example packet transfer sequence between processor B and processor A subsystems.
Table 245. Packet data transfer sequence
Step
Action
Description
1
Processor B requests DMA.
Processor B sends a DMA request to initiate the packet data 
transfer.
2
DMA data transfer
DMA acknowledges.
3
DMA starts transferring data from the specified processor B 
memory location to the specified shared memory.
4
DMA interrupts processor B to signal that the packet transfer has 
finished.
5
Processor B informs processor A 
that data is in shared memory.
Using a B-side transmit register, processor B sends a packet 
information message to processor A about the arrival of new 
packet data stored in shared memory. The message contains the 
command, location, and length of packet data.
6
Processor A receives an interrupt.
Processor A receives an interrupt (assuming its corresponding 
processor A MU-side receive interrupt is enabled). The pending 
processing task becomes active and processes packet data from 
memory.
7
Processor A reads data, then 
writes data.
Processor A reads or processes packet data from shared memory.
8
Processor A writes the result from packet processing to a separate 
buffer.
9
Processor A informs processor B 
that the transfer is finished.
After the processing of the packet data finishes, processor A 
informs processor B (using MU processor A-side transmit register, 
MUA_TRn).
10
Processor A sends an interrupt to 
processor B (a request for more 
data).
Processor B receives the next interrupt from processor A, in which 
processor A requests more packet data.
40.6.5 Freeing a processor from deadlock
During normal operation, one processor may determine that the other processor is not working or is deadlocked. Using Status 
(SR), the processor can use the methods in the following table to identify and correct the problem.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1519 / 5251


---
# 페이지 268

Table 246. Freeing a processor from deadlock
Processor mode
Technique
Description
—
Processor issues an interrupt.
The other processor can interrupt the processor by 
issuing one of the 9 (general purpose, receive, or 
transmit) interrupts.
40.7 Register definition
MU provides transmit and receive data registers (xTR0–n, xRR0–n) for communication between processor A and processor B. 
It also provides control registers (xCR) for operations such as interrupts and resets, and status registers (xSR) for checking the 
status of the other MU-side. Figure 170 shows the schematic for MU registers.
xTR0-n
xRR0-n
xRR0-n
xTR0-n
xSR
xCR
xCR
xSR
MU
Processor
Other
processor
Figure 170. MU registers
40.7.1 MU register descriptions
This section contains the detailed register descriptions for MUA registers.
 
A module transfer error to processor A or processor B is generated when:
• A read or write access is made to an invalid location.
• A write operation is performed on a read-only register on the processor A side or processor B side of MU.
  NOTE  
40.7.1.1
MU memory map
MU_2.MUA base address: 400B_8000h
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1520 / 5251


---
# 페이지 269

MU_3.MUA base address: 400C_4000h
MU_4.MUA base address: 400C_C000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Version ID (VER)
32
R
0309_000Fh
4h
Parameter (PAR)
32
R
0301_0404h
8h
Control (CR)
32
RW
0000_0000h
Ch
Status (SR)
32
RW
See section
100h
Flag Control (FCR)
32
RW
0000_0000h
104h
Flag Status (FSR)
32
R
0000_0000h
110h
General-Purpose Interrupt Enable (GIER)
32
RW
0000_0000h
114h
General-Purpose Control (GCR)
32
RW
0000_0000h
118h
General-purpose Status (GSR)
32
RW
0000_0000h
120h
Transmit Control (TCR)
32
RW
0000_0000h
124h
Transmit Status (TSR)
32
R
0000_000Fh
128h
Receive Control (RCR)
32
RW
0000_0000h
12Ch
Receive Status (RSR)
32
R
0000_0000h
200h - 20Ch
Transmit (TR0 - TR3)
32
W
0000_0000h
280h - 28Ch
Receive (RR0 - RR3)
32
R
0000_0000h
40.7.1.2
Version ID (VER)
Offset
Register
Offset
VER
0h
Function
Determines the version ID and feature set number of MUA.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1521 / 5251


---
# 페이지 270

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
1
0
0
0
0
1
0
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
FEATURE 
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
31-24
MAJOR
Major Version Number
23-16
MINOR
Minor Version Number
15-0
FEATURE
Feature Set Number
Indicates the feature set number.
MU implements:
• Standard features
• Expanded number of TRn/RRn registers
40.7.1.3
Parameter (PAR)
Offset
Register
Offset
PAR
4h
Function
Defines the number of flags, transmit registers, receive registers, and general-purpose interrupt requests available for MU.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1522 / 5251


---
# 페이지 271

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
FLAG_WIDTH 
GIR_NUM 
W
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
RR_NUM 
TR_NUM 
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
1
0
0
Fields
Field
Function
31-24
FLAG_WIDTH
Flag Width
Specifies the number of flag bits (3) in the Flag Control (FCR) and Flag Status (FSR) registers.
23-16
GIR_NUM
General-Purpose Interrupt Request Number
Specifies the number of general-purpose interrupt requests available (1).
15-8
RR_NUM
Receive Register Number
Specifies the number of receive registers (4).
7-0
TR_NUM
Transmit Register Number
Specifies the number of transmit registers (4).
40.7.1.4
Control (CR)
Offset
Register
Offset
CR
8h
Function
Controls MU reset and reset interrupt enable.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1523 / 5251


---
# 페이지 272

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
MURIE 
MUR 
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
31-2
—
Reserved
1
MURIE
MUA Reset Interrupt Enable
Enables the processor A-side MU reset interrupt request due to MU reset issued by MUB.
If the value of this field is 1, an MU reset interrupt request is issued to processor A when 
MUA_SR[MURIP] = 1.
If the value of this field is 0, MU ignores the value of MURIP and issues no MU reset interrupt request.
Only a system reset can reset this field. CR[MUR] cannot reset this field.
0b - Disable
1b - Enable
0
MUR
MU Reset
Resets MU. Writing 1 to this field resets the MUA and MUB sides. All internal states are cleared. It forces all 
control and status registers to return to their default values (except MURIE in MUA/B_CR registers; MURIP 
and MURS in MUA/B_SR registers).
Before writing 1 to this field, interrupt processor B because writing 1 to this field may affect the ongoing 
processor B program.
After writing 1 to this field, monitor the value of MUA_SR[MURS] to know when the reset sequence on the 
processor B-side has ended.
This field always reads 0, and it becomes 0 during the MU reset sequence.
0b - Idle
1b - Reset
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1524 / 5251


---
# 페이지 273

40.7.1.5
Status (SR)
Offset
Register
Offset
SR
Ch
Function
Shows the status of MU resets and the status of pending events and requests.
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
RFP 
TEP 
GIRP 
FUP 
EP 
MURIP 
MURS 
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
u
Fields
Field
Function
31-8
—
Reserved
7
—
Reserved
6
RFP
MUA Receive Full Pending
Indicates whether a receive full message is pending.
This field becomes 1 when MUB writes to a TRn register to send data to MUA. After this field becomes 1, 
MU checks RSR[RFn] to determine whether the data in the Receive register is ready for MUA to read it.
This field becomes 0 when all MUA RRn registers are read, or when MU is reset.
0b - Not pending; MUB is not writing to a Transmit register
1b - Pending; MUB is writing to a Transmit register
5
TEP
MUA Transmit Empty Pending
Indicates whether a transmit empty message is pending.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1525 / 5251


---
# 페이지 274

Table continued from the previous page...
Field
Function
This field becomes 1 when any TCR[TIEn] field is 1 and TSR[TEn] flag is set. After this field becomes 1, MU 
checks TSR[TEn] to determine whether the data in the Transmit (TRn) register is ready for MUA to write to it.
This field becomes 0 when write operations to all MUA Transmit (TRn) registers where TCR[TIEn] = 1 
(transfer interrupt enabled) are completed, or when MU is reset.
0b - No MUA transmit empty event pending
1b - Pending; any TCR[TIEn] field is 1 and TSR[TEn] flag is set
4
GIRP
MUA General-Purpose Interrupt Pending
Indicates that MUB has sent a general-purpose interrupt request.
This field becomes 1 when the MUB side sends a general-purpose interrupt request to the MUA side. 
GSR[GIP0] identifies which general-purpose interrupt request is received.
This field becomes 0 when MUA_GSR[GIP0] is cleared, or when MU is reset.
0b - No request sent
1b - Request sent
3
FUP
MUA Flag Update Pending
Indicates whether a flag update request is pending. MU generates this request when there is a change to 
the Fn[2:0] bits of MUA_FCR.
This field becomes 1 when the MUA side sends a flag update request to the MUB side.
This field becomes 0 when MU acknowledges this flag update request internally (the flag is updated) from 
the MUB side, or during MU reset.
No flag update changes are allowed when this field is 1. When FUP = 1, a write to the Fn[2:0] bits of 
MUA_FCR does not generate a flag update event. The Fn[2:0] bits do not change.
If SR[EP] = 1 (event pending), writing to MUA_FCR does not immediately cause this field to become 1.
0b - No pending update flags (initiated by MUA)
1b - Pending update flags (initiated by MUA)
2
EP
MUA Side Event Pending
Indicates a pending side event when the MUA side sends an event update request to the MUB side. An 
event is any hardware message that the Status register on the MUB side reflects. For example, an event 
occurs when Transmit register 0 is the target of a write operation. During normal operations, the update 
mechanism for this field operates automatically.
MU clears this field automatically when the event update acknowledgment is received, or when MU resets.
To ensure that events are posted to MUB, verify that this field is 0. If it is 1, wait and continue to poll this field 
until it becomes 0.
0b - Not pending
1b - Pending
1
MU Reset Interrupt Pending Flag
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1526 / 5251


---
# 페이지 275

Table continued from the previous page...
Field
Function
MURIP
Indicates whether processor B has issued an MU reset.
This flag is set after processor B initiates an MU reset by setting MUB_CR[MUR]. If CR[MURIE] = 1, the 
processor A MU reset interrupt request is issued when processor B writes 1 to MUB_CR[MUR].
Clearing this flag also clears the MU reset interrupt request.
Only a system reset can reset this flag. MU reset cannot reset this flag.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Reset not issued
1b - Reset issued
When writing
0b - No effect
1b - Clear the flag
0
MURS
MUA and MUB Reset State
Indicates the reset state of MUA and MUB.
This field becomes 1 during any system reset or MU reset from the MUA or MUB side.
This field becomes 0 when the reset sequence on both MUA and MUB sides ends. After issuing any of the 
aforementioned reset events, verify that this field is 0 before starting any access.
0b - Out of reset
1b - In reset
40.7.1.6
Flag Control (FCR)
Offset
Register
Offset
FCR
100h
Function
Configures MUB_FSR[Fn] flags.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1527 / 5251


---
# 페이지 276

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
F2 
F1 
F0 
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
31-3
—
Reserved
2-0
Fn
MUA to MUB Flag
Configures MUB_FSR[Fn] flags, where n = 0 to 2.
Fn configures the corresponding MUB_FSR[Fn] flag.
Fn becomes 0 when MU resets.
0b - Clear MUB_FSR[Fn]
1b - Set MUB_FSR[Fn]
40.7.1.7
Flag Status (FSR)
Offset
Register
Offset
FSR
104h
Function
Contains flags configured by the values written to MUB_FCR[Fn].
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1528 / 5251


---
# 페이지 277

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
F2 
F1 
F0 
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
31-3
—
Reserved
2-0
Fn
MUB to MUA-Side Flag
Contains flags configured by the values written to MUB_FCR[Fn], where n = 0 to 2.
Fn is the MUA-side flag configured by the values written to MUB_FCR[Fn].
When MUB_FCR[Fn] is written to, the write event updates MUA_FSR[Fn], after the event update latency.
0b - MUB_FCR[Fn] = 0
1b - MUB_FCR[Fn] = 1
40.7.1.8
General-Purpose Interrupt Enable (GIER)
Offset
Register
Offset
GIER
110h
Function
Contains the MUA general-purpose interrupt enable fields.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1529 / 5251


---
# 페이지 278

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
GIE0 
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
31-1
—
Reserved
0-0
GIEn
MUA General-purpose Interrupt Enable
Enables general-purpose interrupt. There is one general-purpose interrupt (n = 0).
When GIE0 = 1, a general-purpose interrupt n request is issued to processor A when MUA GSR[GIP0] = 1.
If GIE0 = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIE0 becomes 0 when MU resets.
0b - Disable
1b - Enable
40.7.1.9
General-Purpose Control (GCR)
Offset
Register
Offset
GCR
114h
Function
Contains the MUA general-purpose interrupt request fields.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1530 / 5251


---
# 페이지 279

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
GIR0 
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
31-1
—
Reserved
0-0
GIRn
MUA General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUB. There is one general-purpose interrupt 
(n = 0).
Writing 1 to GIR0 sets MUB_GSR[GIP0]. If MUB_GIER[GIE0] = 1, a general-purpose interrupt request is 
triggered on processor B.
This field becomes 0 when MUB_GSR[GIP0] is cleared. This clearing informs MUA that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIR0 is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
0b - Not requested
1b - Requested
40.7.1.10
General-purpose Status (GSR)
Offset
Register
Offset
GSR
118h
Function
Contains the status of the MUA general-purpose interrupt pending requests.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1531 / 5251


---
# 페이지 280

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
GIP0 
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
Fields
Field
Function
31-1
—
Reserved
0-0
GIPn
MUA General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There is one general-purpose interrupt 
(n = 0).
GIP0 informs MUA that MUB_GCR[GIR0] changed from 0 to 1. If MUA_GIER[GIE0] = 1, a general-purpose 
interrupt request is issued to processor A.
GIP0 is cleared when MU resets.
After GIP0 is cleared, if MUA_GIER[GIE0] = 1, the general-purpose interrupt request is cleared on the 
MUA side.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
40.7.1.11
Transmit Control (TCR)
Offset
Register
Offset
TCR
120h
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1532 / 5251


---
# 페이지 281

Function
Contains the MUA transmit interrupt enable fields.
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
TIE3 
TIE2 
TIE1 
TIE0 
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
31-4
—
Reserved
3-0
TIEn
MUA Transmit Interrupt Enable
Enables MUA transmit interrupt n, where n = 0 to 3.
If this field is 1, an MUA transmit interrupt n request is issued when MUA_TSR[TEn] is set.
If this field is 0, MU ignores the value of MUA_TSR[TEn], and no MUA transmit interrupt n request is issued.
0b - Disable
1b - Enable
40.7.1.12
Transmit Status (TSR)
Offset
Register
Offset
TSR
124h
Function
Indicates whether the MUA transmit registers are empty.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1533 / 5251


---
# 페이지 282

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
TE3 
TE2 
TE1 
TE0 
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
31-4
—
Reserved
3-0
TEn
MUA Transmit Empty
Indicates whether MUA Transmit (TRn) register is empty, where n = 0 to 3.
This field becomes 1 after the MUB_RRn register is read on the MUB side. When TEn = 1, it indicates to 
the MUA side that the MUA_TRn register is ready to be written on the MUA side. If MUA_TCR[TIEn] = 1, a 
transmit n interrupt is issued on the MUA side.
This field becomes 0 after the MUA_TRn register is written to on the MUA side. After this field becomes 0, 
if MUA_TCR[TIEn] = 1, the transmit n interrupt request is cleared on the MUA side.
This field becomes 1 when MU resets.
0b - Not empty
1b - Empty
40.7.1.13
Receive Control (RCR)
Offset
Register
Offset
RCR
128h
Function
Contains the MUA receive interrupt enables.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1534 / 5251


---
# 페이지 283

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
RIE3 
RIE2 
RIE1 
RIE0 
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
31-4
—
Reserved
3-0
RIEn
MUA Receive Interrupt Enable
Enables MUA receive interrupt n, where n = 0 to 3.
If this field is 1, an MUA receive interrupt n request is issued when MUA_RSR[RFn] is set.
If this field is 0, MU ignores the value of MUA_RSR[RFn], and no MUA receive interrupt request is issued.
0b - Disable
1b - Enable
40.7.1.14
Receive Status (RSR)
Offset
Register
Offset
RSR
12Ch
Function
Indicates whether the MUA receive registers are full.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1535 / 5251


---
# 페이지 284

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
RF3 
RF2 
RF1 
RF0 
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
31-4
—
Reserved
3-0
RFn
MUA Receive Register Full
Indicates whether MUA Receive register (RRn) is full, where n = 0 to 3.
RFn becomes 1 when the MUB_TRn register is written to on the MUB side.
When RFn is 1, it indicates to the MUA side that new data in the MUA_RRn register is ready for MUA to read 
it. If MUA_RCR[RIEn] = 1, a receive n interrupt is issued on the MUA side.
RFn becomes 0 when the MUA_RRn register is read, or when MU is reset.
After RFn becomes 0, if MUA_RCR[RIEn] = 1, the receive n interrupt request is cleared on the MUA side.
0b - Not full
1b - Full
40.7.1.15
Transmit (TR0 - TR3)
Offset
Register
Offset
TR0
200h
TR1
204h
TR2
208h
TR3
20Ch
Function
Contains MUA transmit data.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1536 / 5251


---
# 페이지 285

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
TR_DATA 
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
TR_DATA 
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
TR_DATA
MUA Transmit Data
Contains MUA transmit data. MUB_RRn reflects the data written to this register.
The TRn and RRn registers are not double-buffered. Writing to MUA_TRn overrides the data readable in the 
MUA_RRn register.
A write to the Transmit register clears MUA_TSR[TEn] on the transmitter side, and sets MUB_RSR[RFn] on 
the receiver side.
You can write to this register only when MUA_TSR[TEn] = 1.
Reading this register returns all zeroes.
40.7.1.16
Receive (RR0 - RR3)
Offset
Register
Offset
RR0
280h
RR1
284h
RR2
288h
RR3
28Ch
Function
Contains MUA receive data.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1537 / 5251


---
# 페이지 286

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
RR_DATA 
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
RR_DATA 
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
RR_DATA
MUA Receive Data
Reflects the data written to MUB TRn.
Reading this register clears MUA_RSR[RFn] on the receiver side, and sets MUB_TSR[TEn] on the 
transmitter side.
You can read this register only when MUA_RSR[RFn] = 1. Reading it before MUA_RSR[RFn] becomes 1 
may result in reading incorrect data. Poll MUA_RSR[RFn] to confirm it is set before reading RRn.
Writing to this register generates an error response to MUA.
40.7.2 MU register descriptions
This section contains the detailed register descriptions for MUB registers.
 
A module transfer error to processor A or processor B is generated when:
• A read or write access is made to an invalid location.
• A write operation is performed on a read-only register on the processor A side or processor B side of MU.
  NOTE  
40.7.2.1
MU memory map
MU_0.MUB base address: 4038_C000h
MU_1.MUB base address: 404E_C000h
MU_2.MUB base address: 400B_C000h
MU_3.MUB base address: 400C_8000h
MU_4.MUB base address: 400D_0000h
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1538 / 5251


---
# 페이지 287

Offset
Register
Width
(In bits)
Access
Reset value
0h
Version ID (VER)
32
R
0309_000Fh
4h
Parameter (PAR)
32
R
See section
8h
Control (CR)
32
RW
0000_0000h
Ch
Status (SR)
32
RW
See section
10h
Core Control 0 (CCR0)
32
RW
0000_0000h
18h
Core Sticky Status 0 (CSSR0)
32
RW
See section
100h
Flag Control (FCR)
32
RW
0000_0000h
104h
Flag Status (FSR)
32
R
0000_0000h
110h
General-Purpose Interrupt Enable (GIER)
32
RW
0000_0000h
114h
General-Purpose Control (GCR)
32
RW
0000_0000h
118h
General-purpose Status (GSR)
32
RW
0000_0000h
120h
Transmit Control (TCR)
32
RW
0000_0000h
124h
Transmit Status (TSR)
32
R
0000_000Fh
128h
Receive Control (RCR)
32
RW
0000_0000h
12Ch
Receive Status (RSR)
32
R
0000_0000h
200h - 20Ch
Transmit (TR0 - TR3)
32
W
0000_0000h
280h - 28Ch
Receive (RR0 - RR3)
32
R
0000_0000h
40.7.2.2
Version ID (VER)
Offset
Register
Offset
VER
0h
Function
Determines the version ID and feature set number of MUB.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1539 / 5251


---
# 페이지 288

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
1
0
0
0
0
1
0
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
FEATURE 
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
31-24
MAJOR
Major Version Number
23-16
MINOR
Minor Version Number
15-0
FEATURE
Feature Set Number
Indicates the feature set number.
MU implements:
• Standard features
• Expanded number of TRn/RRn registers
40.7.2.3
Parameter (PAR)
Offset
Register
Offset
PAR
4h
Function
Defines the number of flags, transmit registers, receive registers, and general-purpose interrupt requests available for MU.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1540 / 5251


---
# 페이지 289

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
FLAG_WIDTH 
GIR_NUM 
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
RR_NUM 
TR_NUM 
W
Reset
See Register reset values.
Register reset values
Register
Reset value
PAR
MU_0.MUB,MU_1.MUB: 2020_0404h
MU_2.MUB–MU_4.MUB: 0301_0404h
Fields
Field
Function
31-24
FLAG_WIDTH
Flag Width
Specifies the number of flag bits (32) in the Flag Control (FCR) and Flag Status (FSR) registers.
23-16
GIR_NUM
General-Purpose Interrupt Request Number
Specifies the number of general-purpose interrupt requests available (32).
15-8
RR_NUM
Receive Register Number
Specifies the number of receive registers (4).
7-0
TR_NUM
Transmit Register Number
Specifies the number of transmit registers (4).
40.7.2.4
Control (CR)
Offset
Register
Offset
CR
8h
Function
Controls MU reset and reset interrupt enable.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1541 / 5251


---
# 페이지 290

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
MURIE 
MUR 
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
31-2
—
Reserved
1
MURIE
MUB Reset Interrupt Enable
Enables the processor B-side MU reset interrupt request due to MU reset issued by MUA.
If the value of this field is 1, an MU reset interrupt request is issued to processor B when 
MUB_SR[MURIP] = 1.
If the value of this field is 0, MU ignores the value of MURIP and issues no MU reset interrupt request.
Only a system reset can reset this field. CR[MUR] cannot reset this field.
0b - Disable
1b - Enable
0
MUR
MU Reset
Resets MU. Writing 1 to this field resets the MUB and MUA sides. All internal states are cleared. It forces 
all control and status registers to return to their default values (except in MUB/A_CCR0 registers; MURIE 
in MUB/A_CR registers; MURIP and MURS in MUB/A_SR registers).
Before writing 1 to this field, interrupt processor A because writing 1 to this field may affect the ongoing 
processor A program.
After writing 1 to this field, monitor the value of MUB_SR[MURS] to know when the reset sequence on the 
processor A-side has ended.
This field always reads 0, and it becomes 0 during the MU reset sequence.
0b - Idle
1b - Reset
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1542 / 5251


---
# 페이지 291

40.7.2.5
Status (SR)
Offset
Register
Offset
SR
Ch
Function
Shows the status of MU resets and the status of pending events and requests.
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
RFP 
TEP 
GIRP 
FUP 
EP 
MURIP 
MURS 
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
u
Fields
Field
Function
31-8
—
Reserved
7
—
Reserved
6
RFP
MUB Receive Full Pending
Indicates whether a receive full message is pending.
This field becomes 1 when MUA writes to a TRn register to send data to MUB. After this field becomes 1, 
MU checks RSR[RFn] to determine whether the data in the Receive register is ready for MUB to read it.
This field becomes 0 when all MUB RRn registers are read, or when MU is reset.
0b - Not pending; MUA is not writing to a Transmit register
1b - Pending; MUA is writing to a Transmit register
5
TEP
MUB Transmit Empty Pending
Indicates whether a transmit empty message is pending.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1543 / 5251


---
# 페이지 292

Table continued from the previous page...
Field
Function
This field becomes 1 when any TCR[TIEn] field is 1 and TSR[TEn] flag is set. After this field becomes 1, MU 
checks TSR[TEn] to determine whether the data in the Transmit (TRn) register is ready for MUB to write to it.
This field becomes 0 when write operations to all MUB Transmit (TRn) registers where TCR[TIEn] = 1 
(transfer interrupt enabled) are completed, or when MU is reset.
0b - No MUB transmit empty event pending
1b - Pending; any TCR[TIEn] field is 1 and TSR[TEn] flag is set
4
GIRP
MUB General-Purpose Interrupt Pending
Indicates that MUA has sent a general-purpose interrupt request.
This field becomes 1 when the MUA side sends a general-purpose interrupt request to the MUB side. 
GSR[GIPn] identifies which general-purpose interrupt request is received.
This field becomes 0 when all MUB_GSR[GIPn] fields are cleared, or when MU is reset.
0b - No request sent
1b - Request sent
3
FUP
MUB Flag Update Pending
Indicates whether a flag update request is pending. MU generates this request when there is a change to 
the Fn[31:0] bits of MUB_FCR.
This field becomes 1 when the MUB side sends a flag update request to the MUA side.
This field becomes 0 when MU acknowledges this flag update request internally (the flag is updated) from 
the MUA side, or during MU reset.
No flag update changes are allowed when this field is 1. When FUP = 1, a write to the Fn[31:0] bits of 
MUB_FCR does not generate a flag update event. The Fn[31:0] bits do not change.
If SR[EP] = 1 (event pending), writing to MUB_FCR does not immediately cause this field to become 1.
0b - No pending update flags (initiated by MUB)
1b - Pending update flags (initiated by MUB)
2
EP
MUB Side Event Pending
Indicates a pending side event when the MUB side sends an event update request to the MUA side. An 
event is any hardware message that the Status register on the MUA side reflects. For example, an event 
occurs when Transmit register 0 is the target of a write operation. During normal operations, the update 
mechanism for this field operates automatically.
MU clears this field automatically when the event update acknowledgment is received, or when MU resets.
To ensure that events are posted to MUA, verify that this field is 0. If it is 1, wait and continue to poll this field 
until it becomes 0.
0b - Not pending
1b - Pending
1
MU Reset Interrupt Pending Flag
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1544 / 5251


---
# 페이지 293

Table continued from the previous page...
Field
Function
MURIP
Indicates whether processor A has issued an MU reset.
This flag is set after processor A initiates an MU reset by setting MUB_CR[MUR]. If CR[MURIE] = 1, the 
processor B MU reset interrupt request is issued when processor A writes 1 to MUA_CR[MUR].
Clearing this flag also clears the MU reset interrupt request.
Only a system reset can reset this flag. MU reset cannot reset this flag.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Reset not issued
1b - Reset issued
When writing
0b - No effect
1b - Clear the flag
0
MURS
MUA and MUB Reset State
Indicates the reset state of MUA and MUB.
This field becomes 1 during any system reset or MU reset from the MUA or MUB side.
This field becomes 0 when the reset sequence on both MUA and MUB sides ends. After issuing any of the 
aforementioned reset events, verify that this field is 0 before starting any access.
0b - Out of reset
1b - In reset
40.7.2.6
Core Control 0 (CCR0)
Offset
Register
Offset
CCR0
10h
Function
Allows MUB to control the processor on the MUA side.
 
Each module instance supports a different number of registers.
  NOTE  
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1545 / 5251


---
# 페이지 294

Instance
Register supported
Register not supported
MU_0.MUB
CCR0
—
MU_1.MUB
CCR0
—
MU_2.MUB
—
CCR0
MU_3.MUB
—
CCR0
MU_4.MUB
—
CCR0
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
Reserv
ed 
0
Reserv
ed 
0
NMI 
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
31-7
—
Reserved
6-5
—
Reserved
4
—
Reserved
3
—
Reserved
2
—
Reserved
1
—
Reserved
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1546 / 5251


---
# 페이지 295

Table continued from the previous page...
Field
Function
0
NMI
MUA Nonmaskable Interrupt Request
Indicates whether Processor B has issued a nonmaskable interrupt to Processor A.
When this field becomes 1, it initiates a nonmaskable interrupt to processor A.
This field becomes 0 after 1 is written to MUA_CSSR0[NMIC] to clear that field. After this field becomes 0, 
MUB can initiate another nonmaskable interrupt to MUA.
This field is cleared when MU resets.
0b - Nonmaskable interrupt not issued
1b - Nonmaskable interrupt issued
40.7.2.7
Core Sticky Status 0 (CSSR0)
Offset
Register
Offset
CSSR0
18h
Function
Shows the status of interrupts pending (W1C).
The reset value is chip-specific.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
MU_0.MUB
CSSR0
—
MU_1.MUB
CSSR0
—
MU_2.MUB
—
CSSR0
MU_3.MUB
—
CSSR0
MU_4.MUB
—
CSSR0
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1547 / 5251


---
# 페이지 296

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
0
0
0
0
0
0
NMIC 
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
u
Fields
Field
Function
31-8
—
Reserved
7
—
Reserved
6
—
Reserved
5
—
Reserved
4
—
Reserved
3
—
Reserved
2
—
Reserved
1
—
Reserved
0
NMIC
Processor B Nonmaskable Interrupt Clear
Clears the nonmaskable interrupt (NMI) request from the MUA side. The MUB-side NMI service routine uses 
this field.
Writing 1 to this field clears MUA_CCR0[NMI], deasserting the NMI request and enabling MUA_CCR0[NMI] 
to trigger another NMI request.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1548 / 5251


---
# 페이지 297

Table continued from the previous page...
Field
Function
This field always reads as 0, so you cannot poll it. You can only use this field as part of the NMI service 
routine, in which you must write 1 to this field only once.
This field is cleared when MU resets.
0b - Default
1b - Clear MUA_CCR0[NMI]
40.7.2.8
Flag Control (FCR)
Offset
Register
Offset
FCR
100h
Function
Configures MUA_FSR[Fn] flags.
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
F31 
F30 
F29 
F28 
F27 
F26 
F25 
F24 
F23 
F22 
F21 
F20 
F19 
F18 
F17 
F16 
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
F15 
F14 
F13 
F12 
F11 
F10 
F9 
F8 
F7 
F6 
F5 
F4 
F3 
F2 
F1 
F0 
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
F31
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1549 / 5251


---
# 페이지 298

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
30
F30
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
29
MUB to MUA Flag
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1550 / 5251


---
# 페이지 299

Table continued from the previous page...
Field
Function
F29
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
28
F28
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1551 / 5251


---
# 페이지 300

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
27
F27
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
26
F26
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1552 / 5251


---
# 페이지 301

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
25
F25
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
24
F24
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1553 / 5251


---
# 페이지 302

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
23
F23
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
22
MUB to MUA Flag
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1554 / 5251


---
# 페이지 303

Table continued from the previous page...
Field
Function
F22
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
21
F21
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1555 / 5251


---
# 페이지 304

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
20
F20
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
19
F19
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1556 / 5251


---
# 페이지 305

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
18
F18
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
17
F17
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1557 / 5251


---
# 페이지 306

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
16
F16
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
15
MUB to MUA Flag
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1558 / 5251


---
# 페이지 307

Table continued from the previous page...
Field
Function
F15
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
14
F14
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1559 / 5251


---
# 페이지 308

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
13
F13
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
12
F12
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1560 / 5251


---
# 페이지 309

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
11
F11
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
10
F10
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1561 / 5251


---
# 페이지 310

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
9
F9
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
8
MUB to MUA Flag
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1562 / 5251


---
# 페이지 311

Table continued from the previous page...
Field
Function
F8
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
7
F7
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1563 / 5251


---
# 페이지 312

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
6
F6
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
5
F5
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1564 / 5251


---
# 페이지 313

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
4
F4
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
3
F3
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1565 / 5251


---
# 페이지 314

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FCR
—
MU_1.MUB
FCR
—
MU_2.MUB
—
FCR
MU_3.MUB
—
FCR
MU_4.MUB
—
FCR
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
2
F2
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
1
F1
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
0
F0
MUB to MUA Flag
Configures MUA_FSR[Fn] flags, where n = 0 to 31.
Fn configures the corresponding MUA_FSR[Fn] flag.
Fn becomes 0 when MU resets.
0b - Clear MUA_FSR[Fn]
1b - Set MUA_FSR[Fn]
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1566 / 5251


---
# 페이지 315

40.7.2.9
Flag Status (FSR)
Offset
Register
Offset
FSR
104h
Function
Contains flags configured by the values written to MUA_FCR[Fn].
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
F31 
F30 
F29 
F28 
F27 
F26 
F25 
F24 
F23 
F22 
F21 
F20 
F19 
F18 
F17 
F16 
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
F15 
F14 
F13 
F12 
F11 
F10 
F9 
F8 
F7 
F6 
F5 
F4 
F3 
F2 
F1 
F0 
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
F31
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1567 / 5251


---
# 페이지 316

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
30
F30
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
29
F29
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1568 / 5251


---
# 페이지 317

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
28
F28
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
27
F27
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1569 / 5251


---
# 페이지 318

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
26
F26
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
25
MUA to MUB-Side Flag
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1570 / 5251


---
# 페이지 319

Table continued from the previous page...
Field
Function
F25
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
24
F24
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1571 / 5251


---
# 페이지 320

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
23
F23
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
22
F22
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1572 / 5251


---
# 페이지 321

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
21
F21
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
20
F20
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1573 / 5251


---
# 페이지 322

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
19
F19
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
18
MUA to MUB-Side Flag
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1574 / 5251


---
# 페이지 323

Table continued from the previous page...
Field
Function
F18
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
17
F17
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1575 / 5251


---
# 페이지 324

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
16
F16
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
15
F15
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1576 / 5251


---
# 페이지 325

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
14
F14
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
13
F13
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1577 / 5251


---
# 페이지 326

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
12
F12
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
11
MUA to MUB-Side Flag
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1578 / 5251


---
# 페이지 327

Table continued from the previous page...
Field
Function
F11
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
10
F10
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1579 / 5251


---
# 페이지 328

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
9
F9
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
8
F8
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1580 / 5251


---
# 페이지 329

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
7
F7
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
6
F6
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1581 / 5251


---
# 페이지 330

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
5
F5
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
4
MUA to MUB-Side Flag
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1582 / 5251


---
# 페이지 331

Table continued from the previous page...
Field
Function
F4
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
3
F3
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
FSR
—
MU_1.MUB
FSR
—
MU_2.MUB
—
FSR
MU_3.MUB
—
FSR
MU_4.MUB
—
FSR
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1583 / 5251


---
# 페이지 332

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
2
F2
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
1
F1
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
0
F0
MUA to MUB-Side Flag
Contains flags configured by the values written to MUA_FCR[Fn], where n = 0 to 31.
Fn is the MUB-side flag configured by the values written to MUA_FCR[Fn].
When MUA_FCR[Fn] is written to, the write event updates MUB_FSR[Fn], after the event update latency.
0b - MUA_FCR[Fn] = 0
1b - MUA_FCR[Fn] = 1
40.7.2.10
General-Purpose Interrupt Enable (GIER)
Offset
Register
Offset
GIER
110h
Function
Contains the MUB general-purpose interrupt enable fields.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1584 / 5251


---
# 페이지 333

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
GIE31 
GIE30 
GIE29 
GIE28 
GIE27 
GIE26 
GIE25 
GIE24 
GIE23 
GIE22 
GIE21 
GIE20 
GIE19 
GIE18 
GIE17 
GIE16 
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
GIE15 
GIE14 
GIE13 
GIE12 
GIE11 
GIE10 
GIE9 
GIE8 
GIE7 
GIE6 
GIE5 
GIE4 
GIE3 
GIE2 
GIE1 
GIE0 
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
GIE31
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
30
GIE30
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1585 / 5251


---
# 페이지 334

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
29
GIE29
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1586 / 5251


---
# 페이지 335

Table continued from the previous page...
Field
Function
28
GIE28
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
27
GIE27
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1587 / 5251


---
# 페이지 336

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
26
GIE26
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
25
GIE25
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1588 / 5251


---
# 페이지 337

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
24
GIE24
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1589 / 5251


---
# 페이지 338

Table continued from the previous page...
Field
Function
23
GIE23
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
22
GIE22
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1590 / 5251


---
# 페이지 339

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
21
GIE21
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
20
GIE20
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1591 / 5251


---
# 페이지 340

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
19
GIE19
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1592 / 5251


---
# 페이지 341

Table continued from the previous page...
Field
Function
18
GIE18
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
17
GIE17
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1593 / 5251


---
# 페이지 342

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
16
GIE16
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
15
GIE15
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1594 / 5251


---
# 페이지 343

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
14
GIE14
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1595 / 5251


---
# 페이지 344

Table continued from the previous page...
Field
Function
13
GIE13
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
12
GIE12
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1596 / 5251


---
# 페이지 345

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
11
GIE11
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
10
GIE10
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1597 / 5251


---
# 페이지 346

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
9
GIE9
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1598 / 5251


---
# 페이지 347

Table continued from the previous page...
Field
Function
8
GIE8
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
7
GIE7
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1599 / 5251


---
# 페이지 348

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
6
GIE6
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
5
GIE5
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1600 / 5251


---
# 페이지 349

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
4
GIE4
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1601 / 5251


---
# 페이지 350

Table continued from the previous page...
Field
Function
3
GIE3
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
2
GIE2
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1602 / 5251


---
# 페이지 351

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
1
GIE1
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GIER
—
MU_1.MUB
GIER
—
MU_2.MUB
—
GIER
MU_3.MUB
—
GIER
MU_4.MUB
—
GIER
0b - Disable
1b - Enable
0
GIE0
MUB General-purpose Interrupt Enable
Enables general-purpose interrupt. There are 32 general-purpose interrupts (n = 0 to 31).
When GIEn = 1, a general-purpose interrupt n request is issued to processor B when MUB GSR[GIPn] = 1.
If GIEn = 0, the general-purpose interrupt request pending does not trigger the general-purpose interrupt.
GIEn becomes 0 when MU resets.
0b - Disable
1b - Enable
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1603 / 5251


---
# 페이지 352

40.7.2.11
General-Purpose Control (GCR)
Offset
Register
Offset
GCR
114h
Function
Contains the MUB general-purpose interrupt request fields.
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
GIR31 
GIR30 
GIR29 
GIR28 
GIR27 
GIR26 
GIR25 
GIR24 
GIR23 
GIR22 
GIR21 
GIR20 
GIR19 
GIR18 
GIR17 
GIR16 
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
GIR15 
GIR14 
GIR13 
GIR12 
GIR11 
GIR10 
GIR9 
GIR8 
GIR7 
GIR6 
GIR5 
GIR4 
GIR3 
GIR2 
GIR1 
GIR0 
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
GIR31
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1604 / 5251


---
# 페이지 353

Field
Function
Instance
Field supported in
Field not supported in
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
30
GIR30
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
29
GIR29
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1605 / 5251


---
# 페이지 354

Table continued from the previous page...
Field
Function
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
28
GIR28
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1606 / 5251


---
# 페이지 355

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
27
GIR27
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1607 / 5251


---
# 페이지 356

Table continued from the previous page...
Field
Function
26
GIR26
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
25
GIR25
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1608 / 5251


---
# 페이지 357

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
24
GIR24
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1609 / 5251


---
# 페이지 358

Table continued from the previous page...
Field
Function
23
GIR23
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
22
GIR22
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1610 / 5251


---
# 페이지 359

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
21
GIR21
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1611 / 5251


---
# 페이지 360

Table continued from the previous page...
Field
Function
20
GIR20
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
19
GIR19
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1612 / 5251


---
# 페이지 361

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
18
GIR18
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1613 / 5251


---
# 페이지 362

Table continued from the previous page...
Field
Function
17
GIR17
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
16
GIR16
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1614 / 5251


---
# 페이지 363

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
15
GIR15
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1615 / 5251


---
# 페이지 364

Table continued from the previous page...
Field
Function
14
GIR14
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
13
GIR13
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1616 / 5251


---
# 페이지 365

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
12
GIR12
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1617 / 5251


---
# 페이지 366

Table continued from the previous page...
Field
Function
11
GIR11
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
10
GIR10
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1618 / 5251


---
# 페이지 367

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
9
GIR9
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1619 / 5251


---
# 페이지 368

Table continued from the previous page...
Field
Function
8
GIR8
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
7
GIR7
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1620 / 5251


---
# 페이지 369

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
6
GIR6
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1621 / 5251


---
# 페이지 370

Table continued from the previous page...
Field
Function
5
GIR5
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
4
GIR4
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1622 / 5251


---
# 페이지 371

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
3
GIR3
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1623 / 5251


---
# 페이지 372

Table continued from the previous page...
Field
Function
2
GIR2
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
1
GIR1
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1624 / 5251


---
# 페이지 373

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_0.MUB
GCR
—
MU_1.MUB
GCR
—
MU_2.MUB
—
GCR
MU_3.MUB
—
GCR
MU_4.MUB
—
GCR
0b - Not requested
1b - Requested
0
GIR0
MUB General-Purpose Interrupt Request
Specifies whether general-purpose interrupts are requested to MUA. There are 32 general-purpose 
interrupts (n = 0 to 31).
Writing 1 to GIRn sets MUA_GSR[GIPn]. If MUA_GIER[GIEn] = 1, a general-purpose interrupt request is 
triggered on processor A.
This field becomes 0 when MUA_GSR[GIPn] is cleared. This clearing informs MUB that the interrupt is 
accepted (cleared by software).
To ensure proper operations, verify that GIRn is 0 (no pending interrupt) before writing 1 to it.
This field becomes 0 when MU resets.
0b - Not requested
1b - Requested
40.7.2.12
General-purpose Status (GSR)
Offset
Register
Offset
GSR
118h
Function
Contains the status of the MUB general-purpose interrupt pending requests.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1625 / 5251


---
# 페이지 374

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
GIP31 
GIP30 
GIP29 
GIP28 
GIP27 
GIP26 
GIP25 
GIP24 
GIP23 
GIP22 
GIP21 
GIP20 
GIP19 
GIP18 
GIP17 
GIP16 
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
GIP15 
GIP14 
GIP13 
GIP12 
GIP11 
GIP10 
GIP9 
GIP8 
GIP7 
GIP6 
GIP5 
GIP4 
GIP3 
GIP2 
GIP1 
GIP0 
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
31
GIP31
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1626 / 5251


---
# 페이지 375

Table continued from the previous page...
Field
Function
1b - Pending
When writing
0b - No effect
1b - Clear the flag
30
GIP30
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
29
GIP29
MUB General-Purpose Interrupt Request Pending
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1627 / 5251


---
# 페이지 376

Table continued from the previous page...
Field
Function
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
28
GIP28
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1628 / 5251


---
# 페이지 377

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
27
GIP27
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1629 / 5251


---
# 페이지 378

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
26
GIP26
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1630 / 5251


---
# 페이지 379

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
25
GIP25
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1631 / 5251


---
# 페이지 380

Table continued from the previous page...
Field
Function
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
24
GIP24
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1632 / 5251


---
# 페이지 381

Table continued from the previous page...
Field
Function
23
GIP23
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
22
GIP22
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1633 / 5251


---
# 페이지 382

Table continued from the previous page...
Field
Function
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
21
GIP21
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1634 / 5251


---
# 페이지 383

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
20
GIP20
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1635 / 5251


---
# 페이지 384

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
19
GIP19
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1636 / 5251


---
# 페이지 385

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
18
GIP18
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1637 / 5251


---
# 페이지 386

Table continued from the previous page...
Field
Function
0b - No effect
1b - Clear the flag
17
GIP17
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
16
GIP16
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1638 / 5251


---
# 페이지 387

Table continued from the previous page...
Field
Function
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
15
GIP15
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1639 / 5251


---
# 페이지 388

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
14
GIP14
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1640 / 5251


---
# 페이지 389

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
13
GIP13
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1641 / 5251


---
# 페이지 390

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
12
GIP12
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1642 / 5251


---
# 페이지 391

Table continued from the previous page...
Field
Function
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
11
GIP11
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1643 / 5251


---
# 페이지 392

Table continued from the previous page...
Field
Function
10
GIP10
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
9
GIP9
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1644 / 5251


---
# 페이지 393

Table continued from the previous page...
Field
Function
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
8
GIP8
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1645 / 5251


---
# 페이지 394

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
7
GIP7
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1646 / 5251


---
# 페이지 395

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
6
GIP6
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1647 / 5251


---
# 페이지 396

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
5
GIP5
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1648 / 5251


---
# 페이지 397

Table continued from the previous page...
Field
Function
0b - No effect
1b - Clear the flag
4
GIP4
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
3
GIP3
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1649 / 5251


---
# 페이지 398

Table continued from the previous page...
Field
Function
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
2
GIP2
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1650 / 5251


---
# 페이지 399

Table continued from the previous page...
Field
Function
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
1
GIP1
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
MU_0.MUB
GSR
—
Table continues on the next page...
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1651 / 5251


---
# 페이지 400

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
MU_1.MUB
GSR
—
MU_2.MUB
—
GSR
MU_3.MUB
—
GSR
MU_4.MUB
—
GSR
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
0
GIP0
MUB General-Purpose Interrupt Request Pending
Indicates whether a general-purpose interrupt request is pending. There are 32 general-purpose interrupts 
(n = 0 to 31).
GIPn informs MUB that MUA_GCR[GIRn] changed from 0 to 1. If MUB_GIER[GIEn] = 1, a general-purpose 
interrupt request is issued to processor B.
GIPn is cleared when MU resets.
After GIPn is cleared, if MUB_GIER[GIEn] = 1, the general-purpose interrupt request is cleared on the 
MUB side.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not pending
1b - Pending
When writing
0b - No effect
1b - Clear the flag
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1652 / 5251


---
# 페이지 401

40.7.2.13
Transmit Control (TCR)
Offset
Register
Offset
TCR
120h
Function
Contains the MUB transmit interrupt enable fields.
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
TIE3 
TIE2 
TIE1 
TIE0 
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
31-4
—
Reserved
3-0
TIEn
MUB Transmit Interrupt Enable
Enables MUB transmit interrupt n, where n = 0 to 3.
If this field is 1, an MUB transmit interrupt n request is issued when MUB_TSR[TEn] is set.
If this field is 0, MU ignores the value of MUB_TSR[TEn], and no MUB transmit interrupt n request is issued.
0b - Disable
1b - Enable
40.7.2.14
Transmit Status (TSR)
Offset
Register
Offset
TSR
124h
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1653 / 5251


---
# 페이지 402

Function
Indicates whether the MUB transmit registers are empty.
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
TE3 
TE2 
TE1 
TE0 
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
31-4
—
Reserved
3-0
TEn
MUB Transmit Empty
Indicates whether MUB Transmit (TRn) register is empty, where n = 0 to 3.
This field becomes 1 after the MUA_RRn register is read on the MUA side. When TEn = 1, it indicates to 
the MUB side that the MUB_TRn register is ready to be written on the MUB side. If MUB_TCR[TIEn] = 1, a 
transmit n interrupt is issued on the MUB side.
This field becomes 0 after the MUB_TRn register is written to on the MUB side. After this field becomes 0, 
if MUB_TCR[TIEn] = 1, the transmit n interrupt request is cleared on the MUB side.
This field becomes 1 when MU resets.
0b - Not empty
1b - Empty
40.7.2.15
Receive Control (RCR)
Offset
Register
Offset
RCR
128h
Function
Contains the MUB receive interrupt enables.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1654 / 5251


---
# 페이지 403

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
RIE3 
RIE2 
RIE1 
RIE0 
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
31-4
—
Reserved
3-0
RIEn
MUB Receive Interrupt Enable
Enables MUB receive interrupt n, where n = 0 to 3.
If this field is 1, an MUB receive interrupt n request is issued when MUB_RSR[RFn] is set.
If this field is 0, MU ignores the value of MUB_RSR[RFn], and no MUB receive interrupt request is issued.
0b - Disable
1b - Enable
40.7.2.16
Receive Status (RSR)
Offset
Register
Offset
RSR
12Ch
Function
Indicates whether the MUB receive registers are full.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1655 / 5251


---
# 페이지 404

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
RF3 
RF2 
RF1 
RF0 
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
31-4
—
Reserved
3-0
RFn
MUB Receive Register Full
Indicates whether MUB Receive register (RRn) is full, where n = 0 to 3.
RFn becomes 1 when the MUA_TRn register is written to on the MUA side.
When RFn is 1, it indicates to the MUB side that new data in the MUB_RRn register is ready for MUB to read 
it. If MUB_RCR[RIEn] = 1, a receive n interrupt is issued on the MUB side.
RFn becomes 0 when the MUB_RRn register is read, or when MU is reset.
After RFn becomes 0, if MUB_RCR[RIEn] = 1, the receive n interrupt request is cleared on the MUB side.
0b - Not full
1b - Full
40.7.2.17
Transmit (TR0 - TR3)
Offset
Register
Offset
TR0
200h
TR1
204h
TR2
208h
TR3
20Ch
Function
Contains MUB transmit data.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1656 / 5251


---
# 페이지 405

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
TR_DATA 
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
TR_DATA 
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
TR_DATA
MUB Transmit Data
Contains MUB transmit data. MUA_RRn reflects the data written to this register.
The TRn and RRn registers are not double-buffered. Writing to MUB_TRn overrides the data readable in the 
MUA_RRn register.
A write to the Transmit register clears MUB_TSR[TEn] on the transmitter side, and sets MUA_RSR[RFn] on 
the receiver side.
You can write to this register only when MUB_TSR[TEn] = 1.
Reading this register returns all zeroes.
40.7.2.18
Receive (RR0 - RR3)
Offset
Register
Offset
RR0
280h
RR1
284h
RR2
288h
RR3
28Ch
Function
Contains MUB receive data.
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1657 / 5251


---
# 페이지 406

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
RR_DATA 
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
RR_DATA 
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
RR_DATA
MUB Receive Data
Reflects the data written to MUA TRn.
Reading this register clears MUB_RSR[RFn] on the receiver side, and sets MUA_TSR[TEn] on the 
transmitter side.
You can read this register only when MUB_RSR[RFn] = 1. Reading it before MUB_RSR[RFn] becomes 1 
may result in reading incorrect data. Poll MUB_RSR[RFn] to confirm it is set before reading RRn.
Writing to this register generates an error response to MUB.
40.8 Glossary
EP
Event Pending
GIR
General-purpose Interrupt Request
GIP
General-purpose Interrupt Pending
MUR
Messaging Unit Reset
RF
Receiver Full
RFP
Receive Full Pending
TE
Transmitter Empty
TEP
Transmit Empty Pending
MUA
Messaging Unit A
MUB
Messaging Unit B
NXP Semiconductors
Messaging Unit (MU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1658 / 5251


---
