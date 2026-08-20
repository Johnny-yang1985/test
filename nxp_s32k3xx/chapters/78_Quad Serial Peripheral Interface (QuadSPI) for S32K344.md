# 페이지 1812

Chapter 78
Quad Serial Peripheral Interface (QuadSPI) for 
S32K322, S32K342, S32K341, S32K314, S32K324, and 
S32K344
78.1 Chip-specific QuadSPI information
78.1.1 QuadSPI configuration
Table 694. QuadSPI instances
Instance
S32K322/S32K342/S32K341/S32K314/S32K324/S32K344
S32K310/S32K311/S32K312
QuadSPI
Yes
No
Table 695. QuadSPI configuration details
Configuration
S32K312/S32K322/S32K342/S32K344/
S32K324/S32K314
QuadSPI Tx FIFO size
32 words
QuadSPI Rx FIFO size
32 words
Look Up Table Size
4 words
Rx Buffer
256 Bytes
For supported data rates, see device Datasheet.
 
• Boot from QuadSPI is not supported but execution from external memory is supported.
• SFP is not supported in S32K344, S32K324, S32K314, S32K342, and S32K341.
• SoC generate secure access from all CM7 core to QuadSPI.
  NOTE  
Table 696. Features supported
Feature
S32K322/S32K342/S32K341/S32K344/S32K324/S32K314
AHB Write
No
Data learning feature
No
DLL
No
OTFAD (On-the-fly-AES-decryption engine)
No
DDR mode
No
HyperRAM
No
HyperFlash
No
External DQS (Data Strobe)
No
Boot from QuadSPI interface
No
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4672 / 5251


---
# 페이지 1813

The following block diagram depicts the QuadSPI Flash A Interface.
LUT
Command Arbitor
Programmable sequence engine
Clock Domain Crosser
Flexible l/O controller
QuadSPI Flash A Interface
IP Control
Flash Interface
AHB Control
AHB slave
AHB Bus
(64 bit)
Peripheral Bus
(32 bit)
Registers
RX
Buffer
TX
Buffer
transmit
(Data to flash)
received
(Data from flash)
received
(Data from flash)
+
Control Information
AHB
Buffer
IP
command build
& control
DMA and Interrupt Control
Figure 498. Block diagram
78.1.2 Supported read modes
The table below provides an overview of the QuadSPI read modes.
Table 697. QuadSPI read modes
Read modes
SDR support 
(QuadSPI_MCR 
[DDR_EN]=0)
QuadSPI_MCR 
[DQS_EN]
QuadSPI_MCR 
[DQS_FA_SEL]
Data learning 
support
DLL
DQS 
sampling 
method
Pad loopback
Yes
1
01
No
No
78.1.3 QuadSPI initialization sequence
Following initialization sequence should be followed for proper QuadSPI operation:
• Enable QuadSPI module by MC_ME peripheral clock enable (register PRTNx_COFBy_CLKEN present within MC_ME). 
Refer MC_ME chapter for peripheral mapping.
• Configure the SIUL2 registers MSCR[OBE] as 1 and MSCR[SSS] as 0 for QuadSPI_SCKFA pin.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4673 / 5251


---
# 페이지 1814

• Initialize QuadSPI SCKFA by writing a sequence of 1010 to the SIUL2 register GPDO[PDO_a] for QuadSPI_SCKFA pin.
• Configure the SIUL2 register MSCR[OBE] back as 0 for the pins.
• Initiate a dummy flash read to reset all DQS flops by itself and any crossing from DQS domain to IPS/AHB is taken care 
by CDC logic.
• Initiate a peripheral software reset to QuadSPI controller by writing to QuadSPI controller’s MCR.
• Post this initialization sequence, the QuadSPI will work in intended deterministic manner.
 
QuadSPI initialization is to be done before using QuadSPI after each functional reset.
  NOTE  
78.1.4 Pad clock loopback
This chip supports pad clock loopback. The QuadSPI can be configured to use clock loopback to sample input data. SCK is 
delayed by the SCK pin output delay, plus the SCK pin input delay using pad loopback, and is configured by setting QuadSPI 
config registers SOCCR[SOCCFG] and MCR[DQS_FA_SEL]. Enabling the loopback version of SCK can improve the setup time 
of the input data from the Flash.
For details of these register, see QuadSPI register descriptions.
78.1.5 QuadSPI SOC Configuration register SOCCR[SOCCFG] implementation
The QuadSPI SOC Configuration register QuadSPI_SOCCR[SOCCFG] register is used to control dummy loopback pads and 
obe_pull_timing_relax_b. Below is the description of it's bits:
Table 698. SOCCR[SOCCFG] implementation
Bit
Description
Bit[0]
obe_pull_timing_relax_b : enables the timing relaxation by pulling obe for pad 1 for half cycle, if 
0 then enabled else disabled.
Bit[1]
ibe of QSPIA_SCK_DUMMY pad. 0: Disable input receiver 1: Enable input receiver.
Bit[2]
obe of QSPIA_SCK_DUMMY pad. 0: Disable output driver 1: Enable output driver.
Bit[3]
dse of QSPIA_SCK_DUMMY pad. 0: Disable drive strength 1: Enable drive strength.
Bit[4]
pue of QSPIA_SCK_DUMMY pad. 0: Disable internal pullup or pulldown resistor 1: Enable 
internal pullup or pulldown resistor.
Bit[5]
pus of QSPIA_SCK_DUMMYpad. 0: Enable internal pulldown resistor if pue is set 1: Enable 
internal pullup resistor if pue is set.
Bit[6]
sre of QSPIA_SCK_DUMMY pad. 0: Disable slew rate control 1: Enable slew rate control.
Bit[31:7]
Reserved
To Enable the Quadspi dummy PAD loopback use following settings
For Flash-A: MCR[DQS_FB_SEL] = 0x2
SOCCR[SOCCFG] = 0x0000000E (ibe=1, obe=1, dse=1 and sre=0)
 
S32K3xx SoCs does not support dual die flashes. Hence, the signal PCSFA2 from QuadSPI is not used.
  NOTE  
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4674 / 5251


---
# 페이지 1815

78.1.6 QuadSPI AHB Buffer write access control
In S32K344/S32K324/S32K314 the QuadSPI AHB buffer does not support writes. A write to QuadSPI AHB buffer results in error 
response from QuadSPI.
QuadSPI might behave unexpectedly in case if its AHB buffer is written with QuadSPI MCR[MDIS] =1. In cases wherein QuadSPI 
is disabled with above MDIS control bit, XRDC must also be appropriately configured to block the accesses to QSPI AHB buffer 
and indicate an error response.
78.2 Introduction
The QuadSPI module acts as an interface to a single serial flash memory device, with up to four bidirectional data lines.
78.2.1 Features
QuadSPI supports the following features:
• Flexible sequence engine to support various flash memory vendor devices. As there is no specific standard, the module 
supports various kinds of flash memories from different vendors. See Serial flash memory devices for example sequences.
• Single, dual, and quad modes of operation supported for Quad flash memories
• Support for HyperFlash memory
• AHB master to read RX buffer data through AMBA AHB (64-bit width interface) or IPS registers space (32-bit access) and fill 
TX buffer via IPS registers space (32-bit access)
— AHB master can be a DMA with a configurable inner loop size
• Multi-master accesses are allowed
— Flexible and configurable buffer for each master—total available buffer size is 256 bytes.
• All AHB accesses to flash/RAM memory devices are directly memory mapped to the chip system memory
• Programmable sequence engine to cater to future command/protocol changes and ability to support all existing vendor 
commands and operations. The software needs to select the corresponding sequence according to the connected flash 
memory device.
— Support for 3-byte and 4-byte addressing
78.2.2 RX buffer push event
To add the valid entries into the RX buffer
By default, each buffer push event adds two entries to the RX buffer because the interface to the serial clock domain is 64 bits 
in width. Depending on the number of bytes read from the serial flash memory device, it is possible for the very last buffer push 
event that only one entry is added.
RBSR[RDBFL] is incremented by the number of entries added to the RX buffer.
78.2.3 RX buffer POP event
To remove valid entries from the RX buffer
Each buffer POP event removes (RBCT[WMRK] + 1) valid entries from the buffer. BSR[RDBFL] is decremented by the same 
number and RBSR[RDCTR] is incremented accordingly.
78.2.4 Block diagram
The following figure shows a block diagram of the QuadSPI module.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4675 / 5251


---
# 페이지 1816

IP_Ctrl 
com m and_build 
& buffer control 
TX 
Buffer
RX 
Buffer
LUT
DM A and Interrupt Control
AHB_Serve 
fetch 
(addr, size, type)
AHB 
Buffer
received 
(Data) 
AHB_Control 
IP_Control
QSPI_IC_SFM
Clock Dom ain Crosser
QSPI_IF
Program m able sequence engine 
SCLK clock dom ain
Flexible I/O controller 
SCLK clock dom ain
define
Peripheral Bus
AHB Bus
(Addr, Cm d)
wr_data
(Data)
rd_data
(Data)
Registers
read
(Addr, Size)
read_done
(Data)
IOFA[3:0]
SCKFA
PCSFA2
PCSFA1
QuadSPI Bus Flash A
Figure 499. QuadSPI Block Diagram
78.2.5 QuadSPI modes of operation
QuadSPI supports the following modes of operation:
• Normal mode: You can use this mode for write or read accesses to an external serial flash memory device. See Normal mode 
for details.
— Serial flash memory write: You can program data into the flash memory through the IP interface only. See Flash memory 
programming for details.
— Serial flash memory read: Read the contents of the serial flash memory device. Two separate read channels are 
available through the RX buffer and AHB buffer. See Flash memory read for details.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4676 / 5251


---
# 페이지 1817

• Module Disable mode: You can use this mode for disabling serial flash memory clock and AHB command. The clock to 
the non-memory mapped logic in QuadSPI can be stopped in the Module Disable mode. The module enters the mode by 
setting MCR[MDIS].
78.3 External signal description
This section provides the external signal information for the QuadSPI module.
The following table lists the external signals belonging to the module in conjunction with the different modes of operation.
Table 699. Signal properties
Signal 
name
Function
Direction
Description
PCSFA1
Peripheral Chip Select 
Flash Memory A1
O
This signal is the chip select for the serial flash memory device A1 that 
represents the first of the two flash memory devices that share IOFA.
PCSFA2
Peripheral Chip Select 
Flash Memory A2
O
This signal is the chip select for the serial flash memory device A2 that 
represents the the second of the two flash memory devices that share IOFA.
SCKFA
Serial Clock Flash 
Memory A
O
This signal is the serial clock output to the serial flash memory device A.
IOFA[3:0]
Serial I/O Flash 
memory A
I/O
These signals are the data I/O lines to/from the serial flash memory device 
A. See Driving external signals for details about the signal drive and timing 
behavior. Note that the signal pins of the serial flash memory device may 
change their function according to the SFM Command executed, leaving 
them as control inputs when single and dual instructions are executed. 
The module supports driving these inputs to dedicated values. In single I/O 
mode, QuadSPI drives data on IOFA[0] and expects data on IOFA[1].
 
Please refer to chip specific information to check the configuration of QuadSPI block.
  NOTE  
78.3.1 Driving external signals
Single/dual/quad instructions
Depending on the serial flash memory device connected to the QuadSPI module, there are instructions using a different number 
of data lines:
• Single pad: Single line I/O with one data out and one data in line to/from the serial flash memory device
• Dual pad: Dual line I/O with two bidirectional I/O lines, driven alternatively by the serial flash memory device or the 
QuadSPI module
• Quad pad: Quad line I/O with four bidirectional I/O lines, driven alternatively by the serial flash memory device or the 
QuadSPImodule
The different phases of the serial flash memory access scheme are shown in the following figure.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4677 / 5251


---
# 페이지 1818

PCSFx
Single Pad (I/O) Instructions
Not Driven
SCKFx
IOFx[0]
IOFx[1]
IOFx[3:2]
IOFx[3:2]
IOFx[1:0]
(pad
Driven all the time, values taken according to phase
Not Driven
IOFx[3:0]
Not Driven
Driven for 
Tx Instr. only
Driven for 
Tx Instr. only
Dual Pad (I/O) Instructions
Quad Pad (I/O) Instructions
(pad
IDLE
INSTRUCTION
ADDRESS
IDLE
DATA
MODE
DUMMY
=
=
2'b0)
2'b01)
(pad = 2'b10)
Driven as given in the Note1
Driven all the time, values taken from QSPI_MCR[ISDnFx]
Driven all the time, values taken from QSPI_MCR[ISDnFx]
Driven as given in the Note1
Figure 500. Serial flash memory access scheme
Note1:The IOs are driven from QuadSPI as per the number of pads configured for ongoing phase.
Note:The lines status will change based on command mode in case of instruction, address and mode phases. It can be either 1,2 
or 4 lines
Following are the different phases and the I/O driving characteristics of the QuadSPI module:
• Idle: Serial flash memory device not selected – no interaction with the serial flash memory device and the IOFx signals 
are driven.
• Instruction: Serial flash memory device selected – the instruction is sent to the serial device and all the IOFx signals are driven.
• Address: Serial flash memory address is sent to the device – all the IOFx signals are driven and this phase is not applicable 
for all SFM commands.
• Mode: Mode bytes are sent to the serial flash memory device – all the IOFx signals are driven and this phase is not applicable 
for all SFM commands.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4678 / 5251


---
# 페이지 1819

• Dummy: Dummy clocks are provided to the serial flash memory device. See Figure 500 for the IOFx signals driven. The actual 
data lines required for the SFM command executed are not driven for data read commands.
 
— This phase is not applicable for all the SFM commands.
— All read commands in Dual pad, Quad pad modes must use dummy phase before read phase. Note that this 
restriction is not applicable to Single-pad mode.
  NOTE  
• Data: Serial flash memory data are sent to or received from the serial flash memory device. See the preceding figure for the 
IOFx signals driven. The actual data lines required for the SFM command executed are not driven for data read commands.
 
This phase is not applicable for all the SFM commands.
  NOTE  
The PCSFx and SCKFx signals are driven permanently throughout all the phases. In the individual flash memory mode, this 
applies to the selected flash memory device.
Access to a single, individual serial flash memory device
See Serial flash memory access schemes for details.
Read access to two serial flash memory devices attached to the QuadSPI module in parallel. See Serial flash memory access 
schemes for details.
78.4 Functional description
This section provides a functional description of the QuadSPI module.
78.4.1 Serial flash memory access schemes
In the individual flash memory mode, all supported commands are available.
78.4.2 Normal mode
This mode allows communication with an external serial flash memory device. Compared to the standard SPI protocol, this 
communication method uses up to four bidirectional data lines operating at high-data rates. The communication to the external 
serial flash memory device consists of an instruction code and optional address, mode, dummy, and data transfers. The flexible 
programmable core engine described below is immune to a wide variety of command or protocol differences in the serial flash 
memory devices provided by various flash memory vendors.
78.4.2.1
Programmable sequence engine
The core of the QuadSPI module is a programmable sequence engine that works on "instruction-operand" pairs. The core 
controller executes each programmed instruction sequentially. The complete list of instructions and the corresponding operands 
are provided in the following table.
Table 700. Instruction set
Instruction
Instruction 
encoding
Pins
Operand
Action on serial flash memories
CMD
1d
N={0,1,2}d
0d - One pad
1d - Two pads
2d - Four pads
8-bit 
command 
value
Provides the serial flash memory with the SFM command 
operand (Encoded) on the number of pads specified in 
STR mode.
ADDR
2d
Number of 
address bits 
Provide the serial flash memory with address cycles according 
to the operand on the number of pads specified
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4679 / 5251


---
# 페이지 1820

Table 700. Instruction set (continued)
Instruction
Instruction 
encoding
Pins
Operand
Action on serial flash memories
to be sent (for 
example, 24d 
=> 24 address 
bits required)
The actual address to be provided is derived from the incoming 
address in case of AHB-initiated transactions and the value of 
SFAR in case of IPS-initiated transactions.
DUMMY
3d
Number of 
dummy clock 
cycles (should 
be <= 64 and 
> 2 cycles)
Provide the serial flash memory with dummy cycles according 
the operand
The PAD information defines the number of pads in input mode. 
For example, one pad implies that pad 1 is not driven, rest all 
are driven.
MODE
4d
8-bit mode 
value
Provide the serial flash memory with 8-bit operand on the 
number of pads specified
MODE2
5d
N={0,1}d
2-bit mode 
value
Provide the serial flash memory with 2-bit operand on the 
number of pads1 specified
MODE4
6d
N={0,1,2}d
4-bit mode 
value
Provide the serial flash memory with 4-bit operand on the 
number of pads2 specified
READ
7d
N={0,1,2}d
0d - One pad
1d - Two pads
2d - Four pads
Read data 
size in bytes 
(for AHB 
transactions, 
your 
application 
should ensure 
that data size 
is a multiple of 
8 bytes)
Read data from flash memory on the number of pads specified
The data size can be overwritten by writing to the ADATSZ field 
of the BUFxCR registers for AHB-initiated transactions and to 
the IDATSZ field of the IP Configuration Register (IPCR) for 
IPS-initiated transactions.
WRITE
8
Write data 
size in bytes
Write data on the number of pads specified
The data size can be overwritten by writing to the IDATSZ field 
of IP Configuration Register (IPCR).
JMP_ON_CS
3
9d
NA
Instruction 
number
Every time the CS is deasserted, jump to the instruction pointed 
to by the operand. This instruction allows the programmer 
to specify the behavior of the controller when a new read 
transaction is initiated following a CS deassertion.
STOP3
0d
NA
NA
Stop execution; deassert CS
1. For a one-pad instruction, MODE2 takes two serial flash memory clock cycles on the flash memory interface.
2. For a one-pad instruction, MODE4 takes four serial flash memory clock cycles on the flash memory interface. For a 
four-pad instruction, MODE4 takes one serial flash memory clock cycle on the flash memory interface.
3. Sequence ending with this instruction must have all remaining bits as 0s after it.
The programmable sequence engine allows you to configure the QuadSPI module according to the serial flash memory connected 
on board. This flexible structure is compatible with new command or protocol changes from different vendors.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4680 / 5251


---
# 페이지 1821

78.4.2.2
Flexible read xAHB buffers
To reduce the latency of the reads for AHB masters, the data read from serial flash memory is buffered in flexible AHB buffers. 
There are four such flexible buffers. The size of each of these buffers is configurable with the minimum size being 0 bytes and 
maximum size being the size of the complete buffer instantiated (256 bytes). The size of buffer 0 ranges from 0 to BUF0IND. The 
size of buffer 1 ranges from BUF0IND to BUF1IND, buffer2 from BUF1IND to BUF2IND and, buffer 3 ranges from BUF2IND to 
the size of the complete buffer (256 bytes).
Each flexible AHB buffer is associated with the following:
• An AHB master: Optionally, buffer3 may be configured as an "all master" buffer by writing 1 to BUF3CR[ALLMST]. When 
buffer3 is configured in such a way, any access from a master not associated with any other buffer is routed to buffer3.
• A datasize field representing the amount of data to be fetched from the flash memory on every missed access.
The master ID of every incoming request is checked and the data is returned or fetched into the corresponding associated buffer. 
See the chip-specific QuadSPI information for details about master IDs and their corresponding components. Every missed 
access to the buffer causes the controller to clear the buffer and fetch the BUFxCR[ADATSZ] amount of data from the serial 
flash memory. As such, you need not configure the buffer size to be greater than ADATSZ because the locations greater than 
ADATSZ are never used. For any AHB access, the sequence pointed to by BFGENCR[SEQID] is used for the initiated flash 
memory transaction. The data is returned to the master as soon as the requested amount is read from the serial flash memory. 
The controller; however, continues to prefetch the rest of the data in anticipation of a next consecutive request. See Figure 501 
that shows flexible AHB buffers.
BFGENCR[SEQID] points to an index of the LUT. See LUT for details.
Parametrizable max 
size
BUF2IND
BUF1IND
BUF0IND
buffer3
buffer2
buffer1
buffer0
BFGENCR[SEQID]
LUT
Figure 501. Flexible read AHB buffers
78.4.2.3
Abort mechanism during AHB read
Any ongoing read transaction is aborted if a request from the same master arrives for a location other than the location at which 
the transaction is going on. The abort can happen at any point of time.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4681 / 5251


---
# 페이지 1822

78.4.2.4
HBURST support with AHB read
QuadSPI controller supports HBURST and HSIZE on the AHB read interface. HBURST indicates if the transfer forms part of 
a burst. Four, eight, and sixteen beat bursts are supported and the bursts might either be incrementing or wrapping. HSIZE 
indicates the size of the transfer, and supports 8-, 16-, 32-, and 64-bit data sizes. In case of WRAP accesses, QuadSPI generates 
aligned accesses to serial flash memory if there is no buffer hit for any incoming, non-sequential AHB read access. In case there 
is a buffer hit, the incoming address in the haddr line is latched as it is. If the total burst size is more than the data prefetch 
size, an error response is generated and the value of FR[AIBSEF] is configured as 1. The data prefetch size can be defined by 
BUFxCR[ADATSZ] or data size mentioned in the sequence pointed to by the SEQID field when ADATSZ is programmed as 0. In 
case of wrap burst, data prefetch size must be greater than or equal to the wrap burst size + 32 bytes. A few examples are shown 
in the figure below:
       
HADDR = 0x38       
HBUST = WRAP4       
HSIZE = 64 bits       
Flash xsaction start = 0x20       
HADDR = 0x50       
HBUST = WRAP8       
HSIZE = 64 bits       
Flash xsaction start = 0x40       
       
HADDR = 0x38       
HBUST = INCR4       
HSIZE = 64 bits       
Flash xsaction start = 0x38       
HADDR = 0xD0       
HBUST = WRAP16       
HSIZE = 64 bits       
Flash xsaction start = 0x80       
       
HADDR = 0xD4       
HBUST = WRAP8       
HSIZE = 32bits       
Flash xsaction start = 0xC0       
HADDR = 0x54       
HBUST = INCR8       
HSIZE = 32bits       
Flash xsaction start = 0x54       
Incoming AHB access= 0x50, 0x58, 0x60, 0x68, 0x70, 0x78, 0x40, 0x48
Incoming AHB access= 0x38, 0x20, 0x28, 0x30
Incoming AHB access= 0x38, 0x40, 0x48, 0x50
Incoming AHB access= 0xD0, 0xD8, 0xE0, ...0xF8, 0x80, 0x88, ... 0xC8
Incoming AHB access= 0xD4, 0xD8, 0xDC, 0xC0, 0xC4, 0xC8,0xCC, 0xD0
Incoming AHB access= 0x54, 0x58, 0x5C, 0x60, 0x64, 0x68,0x6C, 0x70
Figure 502. QuadSPI HBURST support
 
The software must take care that the prefetch size should never be set less than the minimum data needed by any 
external interface to start processing.
  NOTE  
 
Whenever a core accesses QuadSPI memory with cache enabled, the prefetch size must be configured as equal 
or more than the cache line size; otherwise, FR[AIBSEF] error appears.
  NOTE  
78.4.2.5
LUT
The LUT consists of a number of pre-programmed sequences. Each sequence is basically a sequence of instruction-operand 
pairs, which when executed sequentially, generate a valid serial flash memory transaction. Each sequence can have a maximum 
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4682 / 5251


---
# 페이지 1823

of 10 instruction-operand pairs. The LUT can hold a maximum of sequences. The figure below shows the basic structure of the 
sequence in the LUT.
At reset, the index 0 of the LUT[0..4] is programmed with a basic read sequence as described in Reset sequence. After reset, the 
complete LUT may be reprogrammed according to the chip connected on board. To protect its contents, during a code runover, 
the LUT might be locked, after which a write to the LUT will not be successful until it has been unlocked again. The key for locking 
or unlocking the LUT is 5AF05AF0h, and the associated processes are as follows:
Locking the LUT
1. Write the key 5AF05AF0h into the LUT Key Register (LUTKEY).
2. Write 0b01 to the LUT Lock Configuration Register (LCKCR). Note that this IPS transaction should immediately follow the 
above IPS transaction (no other IPS transaction can be issued). A successful write to this register locks the LUT.
Unlocking the LUT
1. Write the key 5AF05AF0h into the LUT Key Register (LUTKEY).
2. Write 0b10 to the LUT Lock Configuration Register (LCKCR). Note that this IPS transaction should immediately follow the 
above IPS transaction (no other IPS transaction can be issued in between). A successful write to this register unlocks 
the LUT.
The lock status of the LUT can be read from the LCKCR[UNLOCK] and LCKCR[LOCK] fields.
Some example sequences are defined in Example sequences. After reset the instruction sequence 0 is populated with the default 
read sequence shown in the table below.
Table 701. Read sequence
Instruction
Pad
Operand
Comment
CMD
0h
3h
Read data byte command on one pad
ADDR
0h
18h
24 address bits to be sent on one pad
READ
0h
8h
Read 64 bits
JMP_ON_CS
0h
0h
Jump to instruction 0 (CMD)
 
If DLL is disabled then JMP_ON_CS or STOP instruction can be used else only STOP instruction can be used.
  NOTE  
78.4.2.6
Issuing SFM commands
Each access to the external device follows this sequence:
1. You must pre-populate the LUT with the serial flash memory command sequences that are required for the flash memory 
device being used.
2. The module executes the instructions in this sequence one by one. The transaction starts and the module configures the 
value of SR[BUSY].
3. Communication with the external serial flash memory device starts and the transaction executes.
4. After the transaction is complete (all transmit and receive operations with the external serial flash memory device are 
complete), the module resets SR[BUSY]. In case of an IP command, FR[TFF] is asserted.
For details, see Flash memory programming and Flash memory read.
You can trigger the processing of SFM commands in the QuadSPI module in one of the following ways:
Using IP commands
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4683 / 5251


---
# 페이지 1824

For IP commands, the required components need to be written into the following registers and in this sequence:
1. Write the serial flash memory address to be used as provided in the Serial Flash Address Register (SFAR). For IP 
commands not related to specific addresses, the base address of the related flash memory needs to be programmed. 
For example, for an instruction which does not require an address (that is, write enable instruction), the SFAR should be 
programmed with the base address of the memory the command is to be sent to.
2. Write the sequence ID and data size details in the IP Configuration Register (IPCR).
3. Note that writing a value to IPCR[SEQID] must be the last step of the sequence. It is possible to combine all the fields of 
the IPCR into one single write. See IP Configuration Register (IPCR) for details.
Using AHB commands
Any AHB memory-mapped access is routed to one of the buffers depending on the master ID of the request. If the access 
is a "miss," a new serial flash memory transaction is initiated. The transaction is based on the sequence pointed to by 
BFGENCR[SEQID] as described in Flexible read xAHB buffers.
An AHB access is considered memory mapped when the access is to the memory-mapped serial flash memories, as described 
in Memory Mapped Serial Flash Data - Individual Flash mode on Flash memory A.
78.4.2.7
Flash memory programming
In all NOR Flash devices memory sector to be written needs to be erased first. The programming sequence is then initiated in the 
following way:
1. Check that SR[BUSY] is de-asserted or the value of the BUSY field is 0, also, check that the TX buffer is empty. If you need 
to discard the data present in the TX buffer (SR[TXNE]) then the TX buffer must be cleared by writing 1 to MCR[CLR_TXF].
2. Program the address related to the command in SFAR.
3. Provide initial data for the program command into the circular buffer through the TBDR. At least one words of data must be 
written into the TX buffer up to a maximum of 32 entries.
4. Program the IPCR to trigger the command. IPCR[SEQID] should point to an index of the LUT that has the flash memory 
program sequence pre-programmed. Write an appropriate value to IPCR[IDATSZ] to denote the size of the write in bytes.
5. Repeat step 3, depending on the amount of data required, until all of the required data is written to the TBDR. SR[TXFULL] 
can be used to check if the buffer is ready to receive more data. At any time, TBSR[TRCTR] can be read to check how many 
words have been written into the TX buffer.
After writing to IPCR[SEQID] (see step 4), the module starts executing the programmed sequence. The software ensures that 
the correct sequence is programmed into the LUT in accordance with the flash memory connected to the module. The data is 
fetched from the TX buffer. It consists of 32 entries of 32-bit sizes and is organized as a circular FIFO, the read pointer for which is 
incremented after each fetch. When all the data is transmitted, the QuadSPI module returns from the busy state to the idle state. 
However, this is not true for the external device because the internal programming is still ongoing. You may monitor the relevant 
status information available from the serial flash memory device and ensure that the programming is done appropriately.
78.4.2.8
Flash memory read
Host access to the data stored in the external serial flash memory device is performed in two steps. First, the data must be read 
into the internal buffers and in the second step, these internal buffers can be read by the host.
Reading serial flash memory data into the QuadSPImodule internal buffers
A read access to the external serial flash memory device can be triggered in two different ways:
• IP command read: For reading flash memory data into the RX buffer, you must provide the correct sequence ID in 
IPCR[SEQID]. The sequence ID points to a sequence in the LUT. The software needs to ensure that a correct read sequence 
is programmed in the LUT in accordance with the serial flash memory device connected on board. You must program the 
SFAR , and IPCRs. All available read commands supported by the external serial flash memory are possible.
Optionally, it is possible to clear the RX buffer pointer prior to triggering the IP command by writing a 1 to MCR[CLR_RXF]. 
This will invalidate the data currently present in the RX buffer and any new read data will overwrite the old one.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4684 / 5251


---
# 페이지 1825

Using these inputs, the complete transaction is built when IPCR[SEQID] is written to. The transaction related to the read 
access starts and the requested number of bytes is fetched from the external serial flash memory device into the RX buffer. 
As the read access is triggered by an IP command, the value of both SR[IP_ACC] and SR[BUSY] is set to 1.. A count of the 
number of entries currently in the Rx buffer can be obtained from RBSR[RDBFL].
Communication with the external serial flash memory stops if the specified number of bytes are read (on successful 
completion of the transaction).
• AHB command read: For reading flash memory data into the AHB buffer, you must:
— Set up a read access by a master to the address range in the system memory map, which the external serial flash 
memory devices are mapped to.
—
— Program the buffer registers corresponding to the AHB master initiating the request.
— Provide the correct sequence ID in the BFGENCR. The software ensures that a correct read sequence is programmed 
in the LUT in accordance with the serial flash memory device connected on board. Flash memory device selection and 
access mode are determined by the address accessed in the AHB address space associated with the QuadSPI module 
(see Memory-mapped serial flash memory data—individual flash memory mode on flash memory A
On each AHB read access to the memory mapped area, the valid data in the AHB buffer is checked against the address 
requested in the actual read. When the AHB read request cannot be served from the content of the AHB buffer, the buffer 
is flushed and the controller executes the sequence pointed to by the sequence ID. The requested number of buffer entries 
defined in BUFxCR[ADATSZ] is then fetched from the external serial flash memory device into the internal AHB buffer. As 
the read access is triggered through the AHB bus, the value of SR[AHB_ACC] is set, driving SR[BUSY] in turn, until the 
transaction is complete. Communication with the external serial flash memory stops when the specified number of entries 
is filled.
Data transfer from the QuadSPI module internal buffers
The data read out from the external serial flash memory device by the QuadSPI module is stored in the internal buffers. The means 
of accessing the data from the buffer differs depending on which buffer the data is loaded to. See Block diagram for details on the 
two available buffers, the RX buffer and the AHB buffer, in this module. The buffer appears transparent to you and is non-memory 
mapped. See the "Flexible AHB Buffer" section for details.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4685 / 5251


---
# 페이지 1826

         
Memory mapped access       
         
Register access (RBDR)       
         
Memory mapped access       
         
ARDB access       
         This buffer appears transparent to you and is non-memory mapped. See the "Flexible AHB Buffer" section for details.       
         AHB buffer
    
         
Byte swapper for endianness       
         
Note:       
         Read access       
         Read access       
         Write access       
         
System AHB/IPS       
         External flash memory     
         
QuadSPI       
         RX buffer
    
         TX buffer
    
Figure 503. QuadSPI memory map
The RX buffer is implemented as FIFO of depth entries of 4 bytes. Its content is accessible in two different address areas, both 
referring to identical data and the same physical memory:
• In the IPS address space in the area associated with RX Buffer Data Register (RBDR0 - RBDR63).
• In the AHB address space in the area associated with AHB RX Data Buffer Register (ARDB0 - ARDB127).Two successive 
entries are accessed with one single 64-bit AHB read operation.
The RX buffer operation can be summarized as follows:
• RBCT[WMRK] determines at which fill level SR[RXWE] is asserted and how many entries are removed from the RX buffer 
on each buffer POP operation.
• SR[RXWE] indicates that the configured number of data entries is available in the RX buffer and RBSR[RDBFL] indicates 
how many valid entries are available in total.
• The first entry (RBDR0 or ARDB0) always corresponds to the first valid entry in the RX buffer.
For details, see RX Buffer Data Register (RBDR0 - RBDR63) and AHB RX Data Buffer Register (ARDB0 - ARDB127).
• Flag-based data read of the RX buffer is performed by polling SR[RXWE]. When it is asserted, the valid entries can be 
read either via the IPS address space (RBDRn) or the AHB address space (ARDBn). A buffer POP operation must be 
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4686 / 5251


---
# 페이지 1827

triggered by the application by writing a 1 to FR[RBDF]. This automatically updates the FIFO to point to the next entry as 
defined by RBCT[WMRK]. For example, if WMRK is set to 3, then the buffer discards 16 bytes of data.
• DMA-controlled data read of the RX buffer is performed by using the DMA module. The application must ensure that the 
DMA controller of the related chip is programmed appropriately, as described in DMA usage.
• DMA-controlled read out is triggered fully automatically by the assertion of SR[RXWE]. The related buffer POP operation 
is also handled completely inside the QuadSPI module. As in the case explained here, accessing the RX buffer content 
either on RBDRn or ARDBn related addresses is equivalent.
• AHB buffer data read via memory-mapped access: This kind of access is performed by reading one of the addresses 
assigned to the external serial flash memory device(s) within the range specified in Table 723. If this is not the case, a 
memory-mapped AHB command read is triggered as described above. If the requested data is already available in the 
AHB buffer, it is provided directly to the host.
When an AHB access is made to the flash memory mapped address, the data is fetched and returned to the AHB interface. The 
AHB interface is stalled until the data is fetched. As soon as the data from the requested address is read by the QuadSPI module, 
the AHB read access is served. Therefore, it is possible to run sequential reads from the AHB buffer at arbitrary speed without 
the need to monitor any information about the availability of the data. Nevertheless, this access scheme stalls the AHB bus for 
the time required to read the data from the serial flash memory device. If you know that the access is sequential, a better way is 
to have a prefetch enabled by programming the value of BUFxCR[ADATSZ] so that the data is fetched into the buffer before the 
next sequential AHB access.
As long as the host restricts its accesses to the data present in the buffer and to the data currently fetched from the serial 
flash memory, it is possible to run the host read from the AHB buffer simultaneously with the serial flash memory read into the 
AHB buffer.
78.4.2.9
Byte ordering of serial flash memory read data
The basic scheme is that the first byte read out of the serial flash memory device, which is addressed by SFAR[SFADR], 
corresponds to RBDR0[31:24] for IP command read. Similarly, to send a single byte it should be positioned in TBDR[0:7]. In 
contrast to that for AHB command read, the bytes are always positioned according to the byte ordering of the AHB bus.
• Byte ordering in individual flash memory mode
The following table provides the byte ordering scheme of how the byte oriented data space of the serial flash memory device 
is mapped into one single 32-bit entry of the RX buffer or the AHB buffer. The table is valid within the following context:
— Flash memory A in individual flash memory mode
— All AHB data read commands with 32-bit access size
Table 702. Byte ordering in individual flash memory mode
Serial flash memory byte numbering
3
2
1
0
Buffer entry bit position [31:0]
(32-bit data width)
[31:24]
[23:16]
[15:8]
[7:0]
 
For IP commands, the read size can be specified as number of bytes. If this number is not a multiple of four, then 
the last buffer entry is not completely filled with the missing higher numbered bytes at undefined values.
  NOTE  
For AHB commands and reads, starting from an address not aligned to 32-bit boundaries, the requested bytes are given at 
the appropriate positions according to the AMBA AHB specification.
• Buffer entry ordering for 64-bit read access
For read access via the AHB interface, a 64-bit access is possible. Each 64-bit access reads two 32-bit entries, 
simultaneously. The ordering of these 32-bit entries within the 64-bit word is provided in the following table.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4687 / 5251


---
# 페이지 1828

Table 703. 64-bit read access buffer entry ordering
AHB read data bit position [63:0]
[63:32]
[31:0]
Buffer entry #
Odd (1, 3, 5, ...)
Even (0, 2, 4, ...)
78.4.2.10
Normal mode interrupt and DMA requests
The QuadSPI module has different flags that can only generate interrupt requests and one flag that can generate an interrupt as 
well as DMA requests. The following table lists the eight conditions. Note that the flags mentioned in the table are associated with 
the Flag Register (FR).
Table 704. Interrupt and DMA request conditions
Condition
Flag (FR)
DMA
TX buffer fill
TBFF
-
TX buffer underrun
TBUF
-
Illegal instruction error
ILLINE
-
RX buffer drain
RBDF
X
RX buffer overflow
RBOF
-
AHB buffer overflow
ABOF
-
AHB sequence error
ABSEF
-
AHB illegal transaction error
AITEF
-
AHB illegal burst size error
AIBSEF
-
IP command trigger during AHB 
access error
IPAEF
-
IP command trigger could not be 
executed error
IPIEF
-
IP command related transaction finished
TFF
-
Each condition has a corresponding field in Flag Register (FR) and a request enable field in DMA Request Select and Enable 
Register (RSER). FR[RBDF] has separate enable fields for generating IRQ and DMA requests. Note that not all the fields have 
an individual IRQ line. See the chip's Interrupt Vector table for details.
• Transmit buffer fill interrupt request
This indicates that the TX buffer can accept new data. The buffer is asserted if FR[TBFF] is asserted and if the value of the 
corresponding enable field, RSER[TBFIE], is 1. See TX buffer Operation for details on the assertion of FR[TBFF].
Apart from IRQ, it is possible to handle the TX buffer fill by using the DMA. If the value of RSER[TBFDE] is 1, a DMA request 
is triggered when the number of available space in the TX buffer is more than the TBCT[WMRK] valid entries and value of 
SR[TXWA] is set. The application must configure the environment appropriately (for example, the DMA controller) for the 
DMA transfer.
• Receive buffer drain interrupt or DMA request
This is derived from FR[RBDF], indicating that the RX buffer of the QuadSPI module has data available from the serial flash 
memory device to be read by the host. It remains set as long as RBSR[RXWE] is configured. Also, RSER[RBDIE] enables 
the related IRQ.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4688 / 5251


---
# 페이지 1829

Apart from the IRQ, it is possible to handle the RX buffer drain by using the DMA. If the value of RSER[RBDDE] is 1, a 
DMA request is triggered when the RX buffer contains more than RBCT[WMRK] valid entries. The application must set the 
environment appropriately (for example, the DMA controller) for the DMA transfers.
• Buffer overflow/underrun interrupt request
This is a combination of the following fields (all located in the Flag Register (FR) with the related enable bits in the DMA 
Request Select and Enable Register (RSER)):
— TBUF - TX buffer underrun, enabled by TBUIE
— RBOF - RX buffer overflow, enabled by RBOIE
— ABOF - AHB buffer overflow, enabled by ABOIE
— The transmit buffer underrun indicates that an underrun condition in the TX buffer has occurred. It is generated when 
a write instruction is triggered whilst the TX buffer is empty and the the value of RSER[TBUIE] is 1.
— The receive buffer overflow indicates that an overflow condition in the RX buffer has occurred. It is generated when the 
RX buffer is full, an additional read transfer attempts to write into the RX buffer, and the value of RSER[RBOIE] is 1.
— The AHB buffer overflow indicates that an overflow condition in the AHB buffer has occurred. It is generated when the 
AHB buffer is full, an additional read transfer attempts to write into the AHB buffer and the value of RSER[ABOIE] is 1.
— The data from the transfers that generated the individual overflow conditions is ignored.
• Serial flash memory command error interrupt request
If the IPAEF, IPIEF fields in the FR are set, and the related interrupt enable bits in the RSER are also set, then an interrupt 
is requested.
• Transaction finished interrupt request
The IP command transaction finished IRQ indicates the completion of the current IP command. It is triggered by FR[TFF] and 
is masked by RSER[TFIE].
78.4.2.11
TX buffer operation
The TX buffer provides the data used for page programming. For proper operation, it is required to provide at least one entry in the 
TX buffer prior to starting the execution of the page programming command. The application must ensure that the required number 
of data bytes is written into the TX buffer fast enough as long as the command is executed without a TX buffer overflow or underrun.
The QuadSPI module sets the FR[TBFF] field as long as the TX buffer is not full and can accept more data. At the end of write 
through TX buffer, you must clear FR[TBFF] to avoid unnecessary last TX buffer fill interrupt. However, there would always be a 
pending request asserted from QuadSPI controller at the end of any DMA transfer. When external DMA finishes transfer iteration, 
this request from QuadSPI is kept asserted for the next iteration loop.
 
Even if the generation of DMA requests for filling the TX buffer is disabled by using RSER[TBFDE], the TX buffer 
still accepts a DMA transfer because of the last asserted pending request.
Disabling of DMA transfer should be controlled by an external DMA master.
  NOTE  
When the QuadSPI module tries to pull data out of an empty TX buffer, FR[TBUB] signals the TX buffer underrun. The TX buffer 
underrun flag is also asserted when the TX buffer contains less than 32-bits of data and the QuadSPI module tries to pull out data 
from it. The current IP command leading to the underrun condition is continued until the specified number of bytes is sent to the 
serial flash memory device. Also, the data that is transferred is in the Fs format. This means, after the underrun flag is set under 
this condition, it returns Fs until the required number of bytes are not sent. This has been done to ensure that the software does 
not erase the whole sector after underrun and just reprogramming from failure point serves the purpose. When this sequence 
command is complete, FR[TBFF] is asserted, indicating that the TX buffer is ready to be written again.
The TX buffer overflow is not signaled explicitly, but TBSR[TRBFL] can monitor the TX buffer fill level.
For more information, see TX Buffer Status Register (TBSR) and Flag Register (FR).
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4689 / 5251


---
# 페이지 1830

78.4.2.12
Address scheme
Earlier, serial flash memories supported only a 24-bit address space, restricting the maximum memory size of the serial flash 
memory to 16 MB. The new memory specification supports two types of 32-bit addressing mode in addition to the legacy 24-bit 
address mode.
Extended address mode
In this mode, the legacy 24-bit commands are converted to accept 32-bit address commands. The flash memory needs to be 
configured for the 32-bit address mode. Also, while programming the LUT sequence in QuadSPI for 32-bit mode, the ADDR 
commands should be programmed with 32d as the operand value . By default, QuadSPI is in 24-bit legacy address mode. Each 
of the memory vendors have a different way of enabling this mode (see the memory specification from memory vendors). For 
example, the command B7h sent to the Macronix flash memory enables it for the 32-bit address mode.
Extended address register
In this mode, the upper 8 bits of the 32-bit register are provided by the Extended address register in the memory, which provides 
a specific register that is updated according to the address to be accessed. This effectively converts the legacy 24-bit address 
command into 32-bit address commands. The memories greater in size than 16 MB consist of banks of 16 MB each. The 8 bits 
occupied in the extended address register effectively enable a bank. For example, in Spansion memory, when the extended 
address register is updated with a value of 1h, with the help of the 17h command, it opens Bank1 of the memory. The consequent 
24-bit address commands lead to Bank1. The extended address register needs to be updated with the respective value for access 
to other banks. This effectively converts the legacy 24-bit address command into 32-bit address commands.
78.4.3 Module Disable mode
Module Disable mode is a block-specific mode that the QuadSPI can enter to disable serial flash memory clock and AHB 
command. This mode can be entered by:
• The host software: by writing a '1' to MCR[MDIS]
Below are the condition that must be fulfilled to enter the Module Disable mode:
• SR[BUSY] = 0
• SR[AHBTRN] = 0
• RBSR[RDBFL] = 0
• SR[RXDMA] = 0
• SR[TXDMA] = 0
• None of the flags in FR are enabled as interrupts is set
The conditions mentioned above ensures the following:
• There is no SFM command currently being executed.
• All the data read into the RX buffer from the serial flash memory have been fetched by the application.
• There is no current AHB access.
• There is no active DMA request.
• There is no enabled interrupt that is pending.
Certain read or write operations have a different effect when the QuadSPI is in the Module Disable mode. In the Module Disable 
mode, not all of the status and flag bits of the QuadSPI module are updated, and writing to them has no effect. Interrupt and DMA 
request signals cannot be cleared while in the Module Disable mode.
 
It is illegal to issue a new SFM command starting two clock cycles prior to raising the request of entering the Module 
Disable mode until the QuadSPI stays in this mode.
  NOTE  
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4690 / 5251


---
# 페이지 1831

78.4.4 Leaving Module Disable mode
In the Module Disable mode, the serial flash memory clock and AHB command to the QuadSPI module are switched off.
After the QuadSPI has left this mode and has returned to Normal mode, the execution of the first SFM command is deferred until 
the clock to drive that part of the module related to the serial flash memory device is available. Depending upon the point in time 
when the first SFM command is triggered, the actual execution of the command starts with a delay, respective with the re-enabling 
of the flash memory clock signal.
78.5 Initialization/application information
This section provides the initialization and application information of the QuadSPI module.
78.5.1 Power up and reset
The serial flash memory devices connected to the QuadSPI module might require special voltage characteristics of their inputs 
during power up or reset. The application must ensure this.
 
Erase or program commands should be completed before issuing a reset or power cycle to avoid corrupted flash 
pages. The application shall ensure there is a backup of critical data stored at a different location to enable recovery 
from corrupted flash pages.
  CAUTION  
Example: Flash reset sequence
Use the following sequence to reset flash A:
1. Make sure that the flash supports a reset for the condition CS#=high and IOF[3]=low.
2. Set MCR[SWRSTSD] and MCR[SWRSTHD] fields and then clear them.
3. Set MCR[MDIS] field.
4. Reset MCR[ISD3FA] field for flash A.
5. Clear MCR[MDIS] field.
6. Set MCR[MDIS] field.
7. Set MCR[ISD3FA] field for flash A.
8. Clear MCR[MDIS] field.
78.5.2 Available status/flag information
This section provides an overview of the different flags and statuses available, and their interdependencies for different use cases. 
The SR and FR are the related registers.
78.5.2.1
IP commands
See IP Configuration Register (IPCR) for additional details not explicitly covered in this paragraph.
• IP commands—normal operation
Writing to IPCR[SEQID] triggers the execution of a new IP command. Given that this is a legal command, SR[IPACC] and 
SR[BUSY] are asserted simultaneously, immediately after the execution starts.
After the instruction on the serial flash memory device is complete, these field deassert and FR[TFF] is configured.
• IP commands—error situations
See Overview_of_Error_Flags for details.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4691 / 5251


---
# 페이지 1832

78.5.2.2
AHB commands
See the "Reading serial flash memory data into the QuadSPI module internal buffers" topic in theFlash Memory Read section 
for details.
• AHB commands—normal operation
Memory-mapped read access to a serial flash memory address not contained in the AHB buffer triggers the execution of an 
AHB command. Given that this is a legal command, SR[AHB_ACC] and SR[BUSY] are asserted simultaneously, immediately 
after the execution starts. After the instruction on the serial flash memory device is complete, these fields are deasserted.
• IP commands—error situations
See Overview of FR error flags for details.
78.5.2.3
SFM commands
An SFM command consists of an instruction code and all other parameters (for example, size or mode bytes) needed for that 
specific instruction code. Triggering a command either initiates a transaction on the external serial flash memory or results in an 
error. See Table 705 for details on errors.
78.5.2.4
Overview of error flags
The following table provides an overview of the different error flags in the FR and additional error-related details.
Table 705. Overview of FR error flags
Error category
Error flag in FR
Command execution on serial flash 
memory device
TFF behavior (in case of IP 
commands only)
Description
AHB error flag
ABOF
Flash memory transaction continues until 
it finishes
Set when the module tries to 
push data into the AHB buffer that 
exceeds the size of the AHB buffer. 
Occurs only because of the wrong 
programming of BUFxCR[ADATSZ].
AHB error flag
AIBSEF
Flash memory transaction is aborted
Total burst size of the AHB 
transaction is greater than prefetch 
data size.
AHB error flag
AITEF
Flash memory transaction is aborted
No response is generated from 
QuadSPI to AHB bus in case 
of illegal transaction. Also, the 
watchdog timer expires.
Miscellaneous error 
flag
ILLINE
Flash memory transaction aborted
Illegal instruction error flag - set 
when an illegal instruction is 
encountered by the controller in any 
of the sequences.
Command 
arbitration error
IPIEF
TFF not asserted in conjunction with that 
command
IP command error - caused when 
IP access is currently in progress 
(IP_ACC is set) and during:
• Write attempt to IPCR register
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4692 / 5251


---
# 페이지 1833

Table 705. Overview of FR error flags (continued)
Error category
Error flag in FR
Command execution on serial flash 
memory device
TFF behavior (in case of IP 
commands only)
Description
• Write attempt to SFAR register
• Write attempt to RBCT register
Command arbitration 
error
IPAEF
TFF not asserted in conjunction with that 
command
• AHB command already running, 
another IP command could not 
be executed
• AHB command already running, 
write attempt to IPCR[SEQID]
Buffer-related error
RBOF
TFF is asserted on completion
• RX buffer overrun
Buffer-related error
TBUF
TFF is asserted on completion
• TX buffer underrun
Note that only the buffer-related errors are associated with a transaction on the external serial flash memory. All the other errors 
do not trigger an actual transaction.
78.5.2.5
IP bus and AHB access command collisions
There are following flags related to this topic: FR[IPAEF] and FR[IPIEF]. See the "Reading serial flash memory data into the 
QuadSPI module internal buffers" topic of the Flash Memory read section for a description of the flags.
78.5.3 Flash memory device selection
Regardless of the SFM command (IP or AHB), the access mode is selected by specifying the 32-bit address value for the following 
SFM command.
For IP commands, the access mode is selected with the address programmed into the SFAR register. See Serial Flash Address 
Register (SFAR) for details.
For AHB commands, the access mode is determined by the memory-mapped address. See AMBA Bus Register Memory Map 
for details.
78.5.4 DMA usage
For a complete description of the DMA module, see the related DMA Controller chapter. This section only provides QuadSPI-
specific DMA usage details.
78.5.4.1
DMA usage in normal mode
78.5.4.1.1
Bandwidth considerations
Careful consideration of the throughput rate of the entire chain (serial flash memory -> AHB bus / IP bus -> DMA controller) 
involved in the read/write data process is essential for a proper operation. Such analysis must take into account not only the data 
rate provided by the serial flash memory but also the data rate of the AHB bus and the performance of the DMA controller in 
reading/writing data from/to the RX/TX buffer.
Two figures must match for a proper operation, which means that the data rate provided by the serial flash memory device must 
not exceed the average RX buffer readout data rate. Otherwise, the longer this state persists, it results into an RX buffer overflow. 
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4693 / 5251


---
# 페이지 1834

Similarly, the data consumed by the serial flash memory device must not exceed the average TX buffer fill rate. If this persists, it 
leads to an underrun.
AHB bus side (data read)
The total number of bus cycles for each DMA minor loop completion is added from the following components:
The following table provides certain examples for typical use cases:
Case 1: DMA needs to read 4 bytes from SRAM and provide to QuadSPI. It costs total four bus clock cycles. Then, DMA 
handshake adds additional six bus clock cycles, resulting in a total of [6 + 4 * (32/4) = 38] bus clock cycles. 
Table 706. Access duration examples for bus clock side
TBCT[WMRK]
Number of bytes per DMA 
loop
Number of bus clock cycles 
for DMA minor loop
Time duration of DMA minor 
loop for 60 MHz bus clock 
frequency
3
16
6+(16/4)*4 = 22
~366ns
7
32
6+(32/4)*4 = 38
~633ns
11
48
6+(48/4)*4 = 54
~900ns
15
64
6+(64/4)*4 = 70
~1166ns
Case 2: DMA needs to read 32 bytes from SRAM and provide to QuadSPI. DMA handshake takes an additional six bus cycles, 
with 32 bytes DMA read from SRAM costs (8 + 3) core clock cycles. DMA writes 32 bytes to QuadSPI, takes 2 * (32/4) = 16 bus 
cycles with one additional CPU access to QuadSPI, costing two bus clock cycles. This results in a total 6 + (8+3)/2 + 2 * (32/4) 
+2 = 30 bus clock cycles. 
Table 707. Access duration examples for bus clock side
TBCT[WMRK]
Number of bytes per DMA 
loop >
Number of bus clock cycles 
for DMA minor loop
Time duration of DMA minor 
loop for 80 MHz bus clock 
frequency
3
16
6 + (4+3) /2 + (16/4)*2 + 2 = 
20
~333ns
7
32
6 + (8+3) /2 + (32/4)*2 + 2 = 
30
~500ns
11
48
6 + (4+3)/2*3 + (48/4)*2 + 2 = 
44
~733ns
15
64
6 + (8+3) + (64/4)*2 + 2 = 51
~810ns
 
This table figure represents an ideal scenario; actual performance depends on how the chip integrates DMA and 
QuadSPI modules.
  NOTE  
Serial flash memory device side (data read)
The number of serial flash memory cycles can be determined in the following way:
• Number of serial flash memory clock cycles is required to read 4 bytes, corresponding to one RX buffer entry (setup of 
command and address not considered): , eight cycles for quad mode (SDR) instructions in individual flash memory mode, 
and so on.
• Overhead because of clock domain crossing: one cycle
The following table lists the number of clock cycles required to read the data from the serial flash memory corresponding to the 
different settings of RBCT[WMRK]:
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4694 / 5251


---
# 페이지 1835

Table 708. Access duration examples for serial flash memory side
RBCT[WMRK] 
setting
Num bytes per 
DMA loop 1
Num SCKFx for 80 MHz SCKFx
Time duration of flash memory 
data readout for 80 MHz SCKFx 
(~12.5ns period)
IFM 2 quad
IFM quad DDR
IFM quad
IFM quad DDR
0
4
8
4
~100ns
~50ns
1
8
16
8
~200ns
~100ns
3
16
32
16
~400ns
~200ns
7
32
64
32
~800ns
~400ns
1. DMA loop refers to one minor loop completion that is equivalent to one major loop iteration.
2. Individual flash memory mode
 
The table figure represents an ideal scenario; actual performance depends on how the chip integrates with DMA 
and QuadSPI modules.
  NOTE  
A complementary example is when the watermark is set to be too high. In such a case, the time taken by the DMA to read out the 
RX buffer entries should be lesser than the time taken by the controller to push in the remaining entries in the buffer.
IPS bus side (data write)
The total number of bus cycles for each DMA minor loop completion are added from the following components:
• Overhead for each minor loop, given by DMA controller: assume 10 cycles
• Overhead because to clock domain crossing: assume two cycles
• Number of bus clock cycles required for 16 bytes (128-bit write size): assume four cycles (read/write sequence of DMA 
controller)
Note that the size of the minor loop is determined by the size of TBCT[WMRK]; therefore, the overhead specified above distributes 
among (TBCT[WMRK]+1) write accesses of 32-bit each.
The following table provides some examples for typical use cases:
Table 709. Access duration examples for bus clock side
TBCT[WMRK]
Number of bytes per DMA 
loop 1
Number of bus clock cycles for 
DMA minor loop
Time duration of DMA minor 
loop for 80 MHz bus 
clock frequency
3
16
12+4 = 16
~200ns
7
32
12+8 = 20
~250ns
11
48
12+12 = 24
~300ns
15
64
12+16 = 28
~350ns
19
80
12+20 = 32
~400ns
1. DMA loop refers to one minor loop completion that is equivalent to one.
 
The table figure represents an ideal scenario; actual performance depends on how the chip integrates with DMA 
and QuadSPI modules.
  NOTE  
Serial flash memory device side (data write) 
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4695 / 5251


---
# 페이지 1836

The number of serial flash memory cycles can be determined in the following way:
• Number of serial flash memory clock cycles required to write 16 bytes, corresponding to four TX buffer entry (setup of 
command and address not considered): 32 cycles for quad SDR writes in individual flash memory mode.
• Overhead due to clock domain crossing: one cycle
The following table lists the number of clock cycles required to read the data from the serial flash memory corresponding to the 
different settings of TBCT[WMRK]:
Table 710. Access duration examples for serial flash memory side
TBCT[WMRK
] setting
Num bytes 
per DMA 
loop 1
Num SCKFx
Time duration for consuming 
data at flash memory 
interface 100 MHz SCKFx (10 
ns period)2
Time for FIFO to get empty3
IFM 4 quad
5 single IO 
SDR mode
IFM quad
PFM single 
IO SDR
IFM quad
PFM single 
IO SDR
3
16
32
64
320ns
640ns
2240ns
4480ns
7
32
64
128
640ns
1280ns
1920ns
3840ns
15
64
128
256
1280ns
2560ns
1280ns
2560ns
23
96
192
384
1920ns
3840ns
640ns
1280ns
1. DMA loop refers to one minor loop completion that is equivalent to one major loop iteration.
2. Not all flash memory devices support writes at 100 MHz. See the flash memory data sheet for the actual page program 
frequency supported.
3. The assumption for these timings is that the TX Fifo is full when the transaction is initiated
4. Individual flash memory mode
5. Parallel flash memory mode
 
The tables mentioned above are only examples which must be correlated with the DMA in the system.
  NOTE  
Considering the examples provided in the two tables above for TX FIFO, it is evident that depending on the relationship between 
the bus clock and serial flash memory clock frequencies, there are settings possible where the serial flash memory consumes 
data faster than the IPS bus can write data in TX buffer. In these cases, a TX buffer underrun situation occurs. To avoid TX buffer 
underrun, the data transaction size should be large enough.
78.5.5 Flash memory devices address mapping
QuadSPI is configured in Single mode for the supported flash memory port A
The sizes of the flash memory devices are mapped with the system memory space based on the configurations of the 
following registers:
• SFA1AD
• SFA2AD
• SFB1AD
• SFB2AD
The total memory region for the flash memory devices is mapped between QuadSPI_AMBA_BASE and TOP_ADDR_MEMB2 
such that the corresponding CS is asserted based on SFA1AD, SFA2AD and SFB1AD register configurations.
78.5.5.1
Single mode
For single mode configuration, you must write the same value to SFB1AD and SFB2AD registers that you write to the 
SFA2AD register.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4696 / 5251


---
# 페이지 1837

For dual-die flash memories, the values you write to SFB1AD and SFB2AD registers corresponds to the mapped top addresses 
of each die.
For single-die flash memories, you must write the same value to SFA2AD register that you write to the SFA1AD register.
Following is a programming example for single mode single-die flash memory:
• QuadSPI_AMBA_BASE - 1000_0000h
• SFA1AD[TPADA1] - 2000_0000h
• SFA2AD[TPADA2] - 2000_0000h
• SFB1AD[TPADB1] - 2000_0000h
• SFB2AD[TPADB2] - 2000_0000h
The following figure illustrates the memory mapping for single mode QuadSPI configuration.
A1
AMBA_BASE
SFA1AD
SFA2AD
SFB1AD
SFB2AD
Dual-die
Single-die
A1
AMBA_BASE
SFA1AD
SFA2AD
SFB1AD
SFB2AD
A2
Figure 504. Memory map for Single mode
78.6 Byte ordering – endianness
The following topics show the byte ordering in 64-bit LE configuration for AHB buffer and 32-bit LE for TX/RX buffer.
78.6.1 Programming flash memory data
CPU writes instructions to the TBDR register, such as:
• Write TBDR: 4_03_02_01h
• Write TBDR: 8_07_06_05h
The following table shows the content against each TX buffer entry.
Table 711. Example of QuadSPI TX buffer
TX buffer entry
Content
0
4_03_02_01h
1
8_07_06_05h
Programming the TX buffer into the external serial flash memory device results in the following byte order to be sent to the serial 
flash memory:
• 01...02...03...04...05...06...07...08
78.6.2 Reading flash memory data into the RX buffer
Reading the content from the same address provides the following sequence of bytes, identical to the write case:
• 01...02...03...04...05...06...07...08
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4697 / 5251


---
# 페이지 1838

The following table shows the content against each TX buffer entry.
Table 712. Resulting RX buffer content
RX buffer entry
Content
0
4_03_02_01h
1
8_07_06_05h
78.6.2.1
Readout of the RX buffer through RBDRn
The RX buffer content appears at CPU read access through the peripheral bus interface in the following order:
• Read RBDR0: 4_03_02_01h
• Read RBDR1: 8_07_06_05h
78.6.2.2
Readout of the RX buffer through ARDBn
The RX buffer content appears at read access on the AMBA AHB interface at the QuadSPI module boundary:
• 32-bit access: Read ARDB0: 4_03_02_01h
• 32-bit access: Read ARDB1: 8_07_06_05h
• 64-bit access: Read ARDB0: 8_07_06_05_04_03_02_01h
78.6.3 Reading flash memory data into the AHB buffer
Reading the content from the same address as it was written to provides the following sequence of bytes, identical to the 
write case:
• 01...02...03...04...05...06...07...08
The following table shows the content against each TX buffer entry.
Table 713. Resulting AHB buffer content
AHB buffer entry
Content
0
8_07_06_05_04_03_02_01h
78.6.3.1
Readout of the AHB buffer through memory-mapped read
The AHB buffer content appears at read access on the AMBA AHB interface at the QuadSPI module boundary:
• 32-bit read access: 4_03_02_01h
• 32-bit read access: 8_07_06_05h
• 64-bit read access: 8_07_06_05_04_03_02_01h
78.7 Driving flash memory control signals in single and dual modes
In single and dual modes, the serial flash memory devices that can connect to the QuadSPI module expect additional control 
signals on the inputs, which are connected to IOFA[3], IOFA[2] in the quad mode. For easy interfacing, the outputs IOFA[3:2] for 
flash memory A are driven to the logic state given by the configuration fields MCR[ISD3FA], MCR[ISD2FA].
These outputs are driven all the time to the logic level programmed in the MCR except the time when quad commands of the serial 
flash memory are executed. See the specifications of the related serial flash memory device for details about the inactive level.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4698 / 5251


---
# 페이지 1839

78.8 Serial flash memory devices
Several different vendors make flash memory devices with a QuadSPI interface. At present, there is no set standard for the 
QuadSPI instruction set. The most common commands currently have the same instruction code for all vendors; however, some 
commands are unique to specific vendors. Some of the example sequences are provided in the following sections.
78.8.1 Example sequences
This section provides the example sequences of the QuadSPI module.
Table 714. Exit 4 x I/O read enhance performance mode (XIP) (Macronix) and read status
Instruction
Pad
Operand
Description
CMD
0h
EBh
4xIO read command
ADDR
2h
18h
24-bit address to be sent on 
four pads
MODE
2h
0h
2 mode cycles (exit XIP)
DUMMY
0h
4h
4 dummy cycles
READ
2h
8h
Read 64 bits
CMD
0h
5h
Read Status register
READ
0h
1h
Status register data
STOP
0h
0h
Stop, instruction over
78.8.1.1
Fast read sequence (Macronix/Numonyx/Spansion/Winbond)
The following table shows the fast read sequence for Macronix/Numonyx/Spansion/Winbond flash memories.
Table 715. Fast read sequence
Instruction
Pad
Operand
Description
CMD
0h
Bh
Fast read command = 0Bh
ADDR
0h
18h
24 address bits to be sent on one pad
DUMMY
0h
8h
Eight dummy cycles
READ
0h
4h
Read 32 bits on one pad
JMP_ON_CS
0h
0h
Jump to instruction 0 (CMD)
 
If DLL is disabled then JMP_ON_CS or STOP instruction can be used else only STOP instruction can be used.
  NOTE  
78.8.1.2
Fast read quad output (Winbond)
The following table shows the fast read quad output sequence for Winbond memories
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4699 / 5251


---
# 페이지 1840

Table 716. Fast read quad output sequence
Instruction
Pad
Operand
Description
CMD
0h
6Bh
Fast read quad output command = 6Bh
ADDR
0h
18h
24 address bits to be sent on one pad
DUMMY
0h
8h
Eight dummy cycles
READ
2h
4h
Read 32 bits on four pads
JMP_ON_CS
0h
0h
Jump to instruction 0 (CMD)
 
If DLL is disabled then JMP_ON_CS or STOP instruction can be used else only STOP instruction can be used.
  NOTE  
78.8.1.3
4 x I/O read enhance performance mode (XIP) (Macronix)
The following table shows the 4 x I/O read enhance performance mode for Macronix flash memories. The enhanced performance 
mode is also known as XIP mode.
Table 717. Fast read quad output sequence
Instruction
Pad
Operand
Description
CMD
0h
EBh
4xI/O read command = EBh
ADDR
2h
18h
24 address bits to be sent on four pads
MODE
2h
A5h
Two mode cycles
DUMMY
0h
4h
Four dummy cycles
READ
2h
4h
Read 32 bits on four pads
JMP_ON_CS
0h
1h
Jump to instruction 1 (ADDR)
When in XIP mode, the software must ensure that all the flash memories connected to the controller are in this mode. As a part 
of initializing the controller, all the flash memories might be enabled with XIP by carrying out dummy reads.
78.8.1.4
Dual command page program (Numonyx)
The following table shows the dual command page program sequence for Numonyx flash memories.
Table 718. Dual command page program sequence
Instruction
Pad
Operand
Description
CMD
1h
2h
Dual command page program = 02h on 2 pads
ADDR
1h
18h
24 address bits to be sent on two pads
WRITE
1h
20h
Write 32 bytes on two pads
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4700 / 5251


---
# 페이지 1841

Table 718. Dual command page program sequence (continued)
Instruction
Pad
Operand
Description
STOP
0h
0h
Stop, instruction over
78.8.1.5
Sector erase (Macronix/Numonyx/Spansion)
The following table shows the Sector erase sequence for the Macronix/Numonyx/Spansion flash memories.
Table 719. Sector erase sequence
Instruction
Pad
Operand
Description
CMD
0h
20h
Sector erase command = 20h
ADDR
0h
18h
24 address bits to be sent on one pad
STOP
0h
0h
Stop, instruction over
78.8.1.6
Read status register (Macronix/Numonyx/Spansion/Winbond)
The following table shows the read status register sequence for Macronix/Numonyx/Spansion/Winbond flash memories.
Table 720. Read status register sequence
Instruction
Pad
Operand
Description
CMD
0h
0h5
Read status register command = 05h
READ
0h
0h1
Read status register data
STOP
0h
0h
Stop, instruction over
78.9 Sampling of serial flash memory input data
78.9.1 Basic description
QuadSPI is used to read data from the serial flash memory device. Depending on the actual implementation, there is a delay 
between the internal clocking in the QuadSPI module and the external serial flash memory device. See the following figure for an 
overview of this scheme.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4701 / 5251


---
# 페이지 1842

QUADSPI
Clock Gen
Sampling
Serial flash memory
Clock
Data 
Out
SCK - Serial Flash Memory Clock
SI_IO[0:3] - Serial Flash Memory Data
1
5
2
4
3
Figure 505. Serial flash memory sampling clock overview
The rising edge of the internal reference clock is taken as timing reference for the data output of the serial flash memory. After a 
time of ttotal_delay the data arrives at the internal sampling stage of the QuadSPI module. Considering the figure provided here, the 
following parts of the delay chain contribute to ttotal_delay:
• Output delay of the serial flash memory clock output of the device containing the QuadSPI module
• Wire delay of application/PCB from the device containing the QuadSPI module to the external serial flash memory device
• Clock to data out delay of the external serial flash memory device, including input and output delays
• Wire delay of application/PCB from the external serial flash memory device to the device containing the QuadSPI module
• Device delay corresponding to the input data
 
The ttotal_delay is specific to the characteristics of the actual implementation. Also, the serial flash memory device 
clock (SCK) is inverted with respect to the QuadSPI internal reference clock.
  NOTE  
78.9.2 DQS sampling method
78.9.2.1
Basic description
In the DQS mode, the data strobe signal (DQS/RWDS) is used to sample the read data. Here, both DQS and the data sent by the 
flash memory move in the same direction; therefore, it is relatively easier to achieve at higher frequencies.
When using DQS for SDR reads, QuadSPI internally samples the incoming data on the rising edge of the strobe signal.
The next figure shows the sampling read data in the SDR mode using the DQS.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4702 / 5251


---
# 페이지 1843

Internal Ref 
clock
SCK
Data Strobe Signal
  
Data
internal reference for serial flash memory data sampling
Data sampled on only rising edge of Data Strobe Signal
Figure 506. Data strobe functionality in SDR mode for read operation.
 
Consider "Data Strobe Signal" as "Data Strobe Signal driven by memory" and "Data" as "Data from memory".
  NOTE  
 
Refer to the Datasheet for specific timing waveforms of QuadSPI
  NOTE  
 
For Specific details - Refer to the Data Sheet specification of QuadSPI module.
  NOTE  
78.9.2.2
Dummy Pad loopback
The internal clock is loop-backed from the dummy internal pad to compensate data pad delays. This can be enabled by configuring 
the value of MCR[DQS_FA_SEL] as "01" for flash memory A. This mode can be used with the following configuration:
• High/low frequency delay chain manual programming in bypass mode using DLLCRA[SLV_DLY_COARSE] 
and DLLCR[FREQEN].
 
Refer to Auto-DataLearning (4x Sampling method) section with DLL for further details
  NOTE  
 
This mode may not be available on the chip. See the "Supported read modes" section in the chip-specific QuadSPI 
information for the read modes that this chip supports.
  NOTE  
78.10 Delay chain usage
Slave delay chain programming sequence—
Following is the programming sequence for DLL bypass mode.
1. Program DLLCRA[SLV_EN]=1, DLLCRA[SLV_DLL_BYPASS]=1, and DLLCRA[SLAVE_AUTO_UPDT]=0.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4703 / 5251


---
# 페이지 1844

2. Program the following fields to provide the desired DQS delay for sampling: DLLCRA[SLV_FINE_OFFSET], 
DLLCRA[SLV_DLY_COARSE], and DLLCR[FREQEN]. See the chip-specific QuadSPI information for the supported 
programming settings.
3. Program DLLCRA[SLV_UPD]=1 to load these values in the slave delay chain.
4. Check the slave delay chain update status by polling DLLSR[SLVA_LOCK]=1 and clear DLLCRA[SLV_UPD] after 
confirming the update state.
78.11 Memory map and register definition
This section provides the memory map and register definitions for the QuadSPI module.
78.11.1 Register write access
Following are the write access restriction terms that apply to all the registers:
• Register write access restriction
For each register field, the write access conditions are specified in the detailed register description.
The following table provides a description of the write access conditions. If, for a specific register bit or field, none of the given 
write access conditions is fulfilled, any write attempt to this register bit or field is ignored without any notification. The values 
of the bits or fields are not changed.
The condition term [A or B] indicates that the register or field can be written to if at least one of the conditions is fulfilled.
Table 721. Register write access restrictions
Condition
Description
Anytime
No write access restriction
Disabled mode
Write access only if MCR[MDIS] = 1
Normal mode
Write access only if the module is in the normal mode
• Register write access requirements
You can access all registers using 8-bit, 16-bit, and 32-bit wide operations. For some of the registers, at least a 16-bit or 
32-bit wide write access is required to ensure correct operation. This write access requirement is stated in the detailed register 
description for each affected register.
78.11.2 QuadSPI register descriptions
This section provides the memory map and register definitions for the QuadSPI module.
Access to the following addresses does not result in a transfer error:
• 4h
• 50h
• 64h
• 104h
• 120h
• 138h
• 168h
• 188h
• 18Ch
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4704 / 5251


---
# 페이지 1845

78.11.2.1
QuadSPI memory map
QuadSPI_34x base address: 404C_C000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Module Configuration Register (MCR)
32
RW
000F_404Ch
8h
IP Configuration Register (IPCR)
32
RW
0000_0000h
Ch
Flash Memory Configuration Register (FLSHCR)
32
RW
0000_0303h
10h
Buffer 0 Configuration Register (BUF0CR)
32
RW
0000_0003h
14h
Buffer 1 Configuration Register (BUF1CR)
32
RW
0000_0002h
18h
Buffer 2 Configuration Register (BUF2CR)
32
RW
0000_0001h
1Ch
Buffer 3 Configuration Register (BUF3CR)
32
RW
8000_0000h
20h
Buffer Generic Configuration Register (BFGENCR)
32
RW
0000_0000h
24h
SOC Configuration Register (SOCCR)
32
RW
0000_0000h
30h
Buffer 0 Top Index Register (BUF0IND)
32
RW
0000_0000h
34h
Buffer 1 Top Index Register (BUF1IND)
32
RW
0000_0000h
38h
Buffer 2 Top Index Register (BUF2IND)
32
RW
0000_0000h
60h
DLL Flash Memory A Configuration Register (DLLCRA)
32
RW
0120_0000h
100h
Serial Flash Memory Address Register (SFAR)
32
RW
0000_0000h
108h
Sampling Register (SMPR)
32
RW
FF00_0000h
10Ch
RX Buffer Status Register (RBSR)
32
R
0000_0000h
110h
RX Buffer Control Register (RBCT)
32
RW
0000_0000h
134h
Data Learning Status Flash Memory A Register (DLSR_FA)
32
R
0000_0000h
150h
TX Buffer Status Register (TBSR)
32
R
0000_0000h
154h
TX Buffer Data Register (TBDR)
32
RW
0000_0000h
158h
TX Buffer Control Register (TBCT)
32
RW
0000_0000h
15Ch
Status Register (SR)
32
R
0200_3800h
160h
Flag Register (FR)
32
RW
0800_0000h
164h
Interrupt and DMA Request Select and Enable Register (RSER)
32
RW
0000_0000h
16Ch
Sequence Pointer Clear Register (SPTRCLR)
32
RW
0000_0000h
180h
Serial Flash Memory A1 Top Address Register (SFA1AD)
32
RW
7000_0000h
184h
Serial Flash Memory A2 Top Address Register (SFA2AD)
32
RW
7000_0000h
188h
Serial Flash Memory B1 Top Address Register (SFB1AD)
32
RW
7000_0000h
18Ch
Serial Flash Memory B2 Top Address Register (SFB2AD)
32
RW
7000_0000h
200h - 2FCh
RX Buffer Data Register (RBDR0 - RBDR63)
32
R
0000_0000h
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4705 / 5251


---
# 페이지 1846

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
300h
LUT Key Register (LUTKEY)
32
RW
5AF0_5AF0h
304h
LUT Lock Configuration Register (LCKCR)
32
RW
0000_0002h
310h
LUT Register (LUT0)
32
RW
0818_0403h
314h
LUT Register (LUT1)
32
RW
2400_1C08h
318h - 35Ch
LUT Register (LUT2 - LUT19)
32
RW
0000_0000h
78.11.2.2
Module Configuration Register (MCR)
Offset
Register
Offset
MCR
0h
Function
This register holds configuration data associated with the QuadSPI operation.
Special write-access is permitted in different modes:
• DQS_FA_SEL: Disabled mode
• ISD3FA, ISD2FA: Disabled mode
• All other fields: Anytime
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
Reserv
ed 
Reserv
ed 
Reserved 
Reserv
ed 
Reserv
ed 
DQS_FA_SEL 
Reserv
ed 
Reserv
ed 
0
Reserv
ed 
Reserv
ed 
ISD3F
A 
ISD2F
A 
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
Reserv
ed 
MDIS 
Reserv
ed 
Reserv
ed 
0
0
0
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserved 
SWRS
THD 
SWRS
TSD 
W
CLR_
TXF 
CLR_
RXF 
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
1
0
0
1
1
0
0
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4706 / 5251


---
# 페이지 1847

Fields
Field
Function
31
—
Reserved
30
—
Reserved
29-28
—
Reserved
27
—
Reserved
26
—
Reserved
25-24
DQS_FA_SEL
DQS clock for sampling read data at flash memory A
Selects DQS clock for sampling read data at flash memory A QuadSPI port
00b - Reserved
01b - Pad loopback
10b - Reserved
11b - Reserved
23
—
Reserved
22
—
Reserved
21-20
—
Reserved
19
—
Reserved
18
—
Reserved
17
ISD3FA
Idle signal drive IOFA[3] flash memory A
Determines the logic level that the IOFA[3] output of the QuadSPI module is driven to in the inactive state. 
See Driving flash memory control signals in single and dual modes for details.
0b - IOFA[3] is driven to logic L
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4707 / 5251


---
# 페이지 1848

Table continued from the previous page...
Field
Function
1b - IOFA[3] is driven to logic H
16
ISD2FA
Idle signal drive IOFA[2] flash memory A
Determines the logic level that the IOFA[2] output of the QuadSPI module is driven to in the inactive state. 
See Driving flash memory control signals in single and dual modes for details.
0b - IOFA[2] is driven to logic L.
1b - IOFA[2] is driven to logic H.
15
—
Reserved
14
MDIS
Module disable
Allows the clock to the non-memory mapped logic in the QuadSPI to be stopped.
0b - Enable QuadSPI clocks
1b - Allow external logic to disable QuadSPI clocks
13
—
Reserved
12
—
Reserved
11
CLR_TXF
Clear TX FIFO/buffer
This is a self-clearing field that invalidates the TX buffer content.
 
Software must wait for at least five system cycles and three flash cycles after writing '1' to 
this field.
  NOTE  
0b - No action
1b - Read and write pointers of the TX buffer are reset to 0 and TBSR[TRCTR] is reset to 0.
10
CLR_RXF
Clear RX FIFO
This is a self-clearing field that invalidates the RX buffer content.
0b - No action
1b - Read and write pointers of the RX buffer are reset to 0 and RBSR[RDBFL] is reset to 0.
9
—
Reserved
8
—
Reserved
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4708 / 5251


---
# 페이지 1849

Table continued from the previous page...
Field
Function
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
3-2
—
Reserved
1
SWRSTHD
Software reset for AHB domain
0b - De-assert Software reset
1b - AHB domain flops are reset. This field does not reset configuration registers. It is advisable to reset both 
the serial flash memory domain and AHB domain at the same time. Resetting only one domain might lead 
to side effects.
 
The software resets need the clock to be running to propagate to the design. The value of 
MCR[MDIS] should be 0 when the software reset bits are asserted. Also, before they can 
be deasserted again (by setting MCR[SWRSTHD] to 0), it is recommended to set the value 
of MCR[MDIS] to 1. After the software resets have been deasserted, the normal operation 
can be started by setting MCR[MDIS] to 0.
  NOTE  
 
Software must wait for at least three system cycles and three flash cycles after changing the 
value of this field.
  NOTE  
0
SWRSTSD
Software reset for serial flash memory domain
0b - De-assert Software reset
1b - Serial flash memory domain flops are reset. This field does not reset configuration registers. It is 
advisable to reset both the serial flash memory domain and AHB domain at the same time. Resetting only 
one domain might lead to side effects.
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4709 / 5251


---
# 페이지 1850

Table continued from the previous page...
Field
Function
 
The software resets need the clock to be running to propagate to the design. The value 
of MCR[MDIS] should therefore be 0 when the software reset bits are asserted. Also, 
before they can be deasserted again (by specifying 0 as the value for MCR[SWRSTSD]), 
it is recommended to specify 1 as the value for MCR[MDIS]. After the software resets 
are deasserted, the normal operation can be started by specifying 0 as the value 
for MCR[MDIS].
  NOTE  
 
Software must wait for at least three system cycles and three flash cycles after changing the 
value of this field.
  NOTE  
78.11.2.3
IP Configuration Register (IPCR)
Offset
Register
Offset
IPCR
8h
Function
This register provides all the configuration required for an IP-initiated command, which can be triggered by writing in the SEQID 
field of this register. If the SEQID field is written successfully, a new command to the external serial flash memory is initiated per 
the sequence pointed to by this field. See Normal mode for details on command triggering and command execution.
Special write-access is permitted if:
• SR[IP_ACC]=0
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
SEQID 
0
0
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
IDATSZ 
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
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4710 / 5251


---
# 페이지 1851

Fields
Field
Function
31-28
—
Reserved
27-24
SEQID
Points to a sequence in the LUT
This field contains the sequence index of the LUT. See LUT for details.
Each sequence index can accommodate up to 10 instructions (2 instructions per register).
A write to this field triggers a transaction on the serial flash memory interface.
23
—
Reserved
22
—
Reserved
21-17
—
Reserved
16
—
Reserved
15-0
IDATSZ
IP data transfer size
This field defines the data transfer size, in bytes, of the IP command.
78.11.2.4
Flash Memory Configuration Register (FLSHCR)
Offset
Register
Offset
FLSHCR
Ch
Function
This register contains the timings that are specific to the flash memory device. The QuadSPI controller must meet these timings 
for the device to function correctly.
Special write-access is permitted if:
• SR[AHB_ACC] = 0
• SR[IP_ACC] = 0
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4711 / 5251


---
# 페이지 1852

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
TCSH 
0
TCSS 
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
1
1
Fields
Field
Function
31-18
—
Reserved
17-16
—
Reserved
15-12
—
Reserved
11-8
TCSH
Serial flash memory CS hold time
This hold time is in terms of serial flash memory clock cycles, and it must be greater than or equal to five 
flash memory clock cycles. Refer the chip datasheet for the exact value.
7-4
—
Reserved
3-0
TCSS
Serial flash memory CS setup time
This setup time is in terms of serial flash memory clock cycles, and it must be greater than or equal to two 
flash memory clock cycles. Refer the chip Datasheet for the exact value.
78.11.2.5
Buffer 0 Configuration Register (BUF0CR)
Offset
Register
Offset
BUF0CR
10h
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4712 / 5251


---
# 페이지 1853

Function
This register provides the configuration for any read access routed to buffer0, which happens when the master ID of the incoming 
AHB request matches BUF0CR[MSTRID]. Any buffer "miss" leads to a serial flash memory transaction being triggered per the 
sequence pointed to by BFGENCR[SEQID].
Special write-access is permitted if:
• SR[AHB_ACC] = 0
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
Reserv
ed 
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
ADATSZ 
0
MSTRID 
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
31
—
Reserved
30-14
—
Reserved
13-8
ADATSZ
AHB data transfer size
Defines the read data transfer size in 8 bytes of an AHB triggered read access to serial flash memory. For 
example, a value of 0x2 sets transfer size to 16 bytes. When ADATSZ = 0, the data size mentioned in the 
sequence pointed to by the SEQID field overrides this value. The software should ensure that this transfer 
size is not greater than the size of the buffer.
7-4
—
Reserved
3-0
MSTRID
Master ID
ID of the AHB master associated with BUFFER 0
Any AHB read access with this master ID is routed to this buffer. You must ensure that the master IDs 
associated with all buffers are different.
 
See the chip-specific QuadSPI information for details about master IDs and their 
corresponding components.
  NOTE  
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4713 / 5251


---
# 페이지 1854

78.11.2.6
Buffer 1 Configuration Register (BUF1CR)
Offset
Register
Offset
BUF1CR
14h
Function
This register provides the configuration for any access routed to buffer 1, which happens when the master ID of the incoming AHB 
request matches the MSTRID field of this register. Any buffer "miss" leads to the buffer being flushed and a serial flash memory 
transaction being triggered per the sequence pointed to by BFGENCR[SEQID].
Special write-access is permitted if:
• SR[AHB_ACC] = 0
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
ADATSZ 
0
MSTRID 
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
31-14
—
Reserved
13-8
ADATSZ
AHB data transfer size
This field defines the read data transfer size in 8 bytes of an AHB triggered read access to serial flash 
memory. For example, a value of 0x2 sets the transfer size to 16 bytes. When ADATSZ = 0, the data size 
mentioned in the sequence pointed to by the SEQID field overrides this value. Software should ensure that 
this transfer size is not greater than the size of this buffer.
7-4
—
Reserved
3-0
MSTRID
Master ID
ID of the AHB master associated with BUFFER 1
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4714 / 5251


---
# 페이지 1855

Table continued from the previous page...
Field
Function
Any AHB read access with this master ID is routed to this buffer. You must ensure that the master IDs 
associated with all buffers are different.
 
See the chip-specific QuadSPI information for details about master IDs and their 
corresponding components.
  NOTE  
78.11.2.7
Buffer 2 Configuration Register (BUF2CR)
Offset
Register
Offset
BUF2CR
18h
Function
This register provides the configuration for any access routed to buffer 2, which happens when the master ID of the incoming AHB 
request matches the MSTRID field of this register. Any buffer "miss" leads to the buffer being flushed and a serial flash memory 
transaction being triggered per the sequence pointed to by BFGENCR[SEQID].
Special write-access is permitted if:
• SR[AHB_ACC] = 0
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
ADATSZ 
0
MSTRID 
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
31-14
—
Reserved
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4715 / 5251


---
# 페이지 1856

Table continued from the previous page...
Field
Function
13-8
ADATSZ
AHB data transfer size
This field defines the read data transfer size in 8 bytes of an AHB triggered read access to the serial flash 
memory. For example, a value of 0x2 sets transfer size to 16 bytes. When ADATSZ = 0, the data size 
mentioned in the sequence pointed to by the SEQID field overrides this value. The software should ensure 
that this transfer size is not greater than the size of this buffer.
7-4
—
Reserved
3-0
MSTRID
Master ID
The ID of the AHB master associated with BUFFER2. Any AHB read access with this master ID is routed 
to this buffer.
It must be ensured that the master IDs associated with all buffers are different.
 
See the chip-specific QuadSPI information for details about master IDs and their 
corresponding components.
  NOTE  
78.11.2.8
Buffer 3 Configuration Register (BUF3CR)
Offset
Register
Offset
BUF3CR
1Ch
Function
This register provides the configuration for any access to buffer 3.
An access is routed to buffer 3 when the master ID of the incoming AHB request matches the MSTRID field of BUF3CR. Any 
buffer "miss" leads to the buffer being flushed and a serial flash memory transaction being triggered per the sequence pointed to 
by BFGENCR[SEQID].
In case the value of the ALLMST field is not 1, any such transaction (where master ID does not match any of the MSTRID fields) 
is returned with an ERROR response.
Special write-access is permitted if:
• SR[AHB_ACC] = 0
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4716 / 5251


---
# 페이지 1857

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
ALLMS
T 
0
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
ADATSZ 
0
MSTRID 
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
ALLMST
All master enable
When set, buffer3 acts as an all-master buffer. Any AHB access with a master ID not matching with the 
master ID of buffer0, buffer1, or buffer2 is routed to buffer3. When set, the MSTRID field of this register 
is ignored.
30-18
—
Reserved
17-14
—
Reserved
13-8
ADATSZ
AHB data transfer size
Defines the read data transfer size in 8 bytes of an AHB triggered read access to serial flash memory. When 
ADATSZ = 0, the data size mentioned in the sequence pointed to by the SEQID field overrides this value.
7-4
—
Reserved
3-0
MSTRID
Master ID
ID of the AHB master associated with BUFFER 3. Any AHB read access with this master ID is routed to this 
buffer. You must ensure that the master IDs associated with all buffers are different.
 
See the chip-specific QuadSPI information for details about master IDs and their 
corresponding components.
  NOTE  
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4717 / 5251


---
# 페이지 1858

78.11.2.9
Buffer Generic Configuration Register (BFGENCR)
Offset
Register
Offset
BFGENCR
20h
Function
This register provides generic configuration to any of the buffer accesses. Any buffer "miss" leads to the buffer being flushed and 
a serial flash memory transaction being triggered per the sequence pointed to by the SEQID field.
Special write-access is permitted if:
• SR[AHB_ACC] = 0
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
SEQID 
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
31-28
—
Reserved
27-18
—
Reserved
17
—
Reserved
16
—
Reserved
15-12
SEQID
Points to a sequence in the LUT.
This field contains the sequence index of the LUT... See LUT.
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4718 / 5251


---
# 페이지 1859

Table continued from the previous page...
Field
Function
 
If the sequence pointer differs in the new and the previous sequences, you should reset it. 
See sequence pointer clear register for more information.
  NOTE  
11-0
—
Reserved
78.11.2.10
SOC Configuration Register (SOCCR)
Offset
Register
Offset
SOCCR
24h
Function
This register is programmed at the chip level for QuadSPI configuration. For details, see chip-specific QuadSPI information.
Special write-access is permitted if:
• SR[AHB_ACC] = 0
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
SOCCFG 
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
SOCCFG 
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
SOCCFG
SOC configuration
This field configuration is specific to chip. For details, see chip-specific QuadSPI information.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4719 / 5251


---
# 페이지 1860

78.11.2.11
Buffer 0 Top Index Register (BUF0IND)
Offset
Register
Offset
BUF0IND
30h
Function
This register specifies the top index for buffer 0, which defines its size. Note that the three LSBs of this register are set to 0. This 
ensures that the buffer is 64-bit aligned because each buffer entry is 64-bits long.
The register value should be set to the desired number of bytes. For example, setting BUF0IND[31:3] to 0 gives 0 bytes, setting 
the value to 1 gives 8 bytes, and so on.
The size of buffer 0 is the difference between BUF0IND and 0.
The software must ensure that the value of TPINDX0 is not greater than the size of buffer 0.
Special write-access is permitted if:
• SR[AHB_ACC] = 0
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
TPINDX0 
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
31-9
—
Reserved
8-3
TPINDX0
Top index of buffer 0
2-0
—
Reserved
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4720 / 5251


---
# 페이지 1861

78.11.2.12
Buffer 1 Top Index Register (BUF1IND)
Offset
Register
Offset
BUF1IND
34h
Function
This register specifies the top index of buffer 1, which defines its size. Note that the three LSBs of this register are set to 0. This 
ensures that the buffer is 64-bit aligned because each buffer entry is 64-bits long.
The size of buffer 1 is the difference between BUF1IND and BUF0IND. The register value should be entered in bytes. For example, 
if BUF0IND = 0x100, then setting BUF1IND = 0x130 sets the size of buffer 1 to 0x30 bytes.
The software must ensure that the value of TPINDX1 is not greater than the size of buffer 1.
Special write-access is permitted if:
• SR[AHB_ACC] = 0
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
TPINDX1 
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
31-9
—
Reserved
8-3
TPINDX1
Top index of buffer 1
2-0
—
Reserved
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4721 / 5251


---
# 페이지 1862

78.11.2.13
Buffer 2 Top Index Register (BUF2IND)
Offset
Register
Offset
BUF2IND
38h
Function
This register specifies the top index of buffer 2, which defines its size. Note that the three LSBs of this register are set to 0. This 
ensures that the buffer is 64-bit aligned because each buffer entry is 64-bits long.
The size of buffer 2 is the difference between BUF2IND and BUF1IND. The register value should be entered in bytes. For example, 
if BUF1IND = 0x130 then setting BUF2IND = 0x180 sets the size of buffer 2 to 0x50 bytes.
The software must ensure that the value of TPINDX2 is not greater than the size of buffer 2.
Special write-access is permitted if:
• SR[AHB_ACC] = 0
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
TPINDX2 
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
31-9
—
Reserved
8-3
TPINDX2
Top index of buffer 2
2-0
—
Reserved
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4722 / 5251


---
# 페이지 1863

78.11.2.14
DLL Flash Memory A Configuration Register (DLLCRA)
Offset
Register
Offset
DLLCRA
60h
Function
This register configures slave delay chain for flash memory A.
See Delay chain usage for the programming sequence.
 
See the chip data sheet for information on programming register fields.
  NOTE  
 
Please see the chip specific section of QuadSPI DLLCRA register for delay elements data
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
Reserv
ed 
FREQ
EN 
0
Reserved 
Reserved 
SLV_FINE_OFFSET 
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
1
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
Reserv
ed 
SLV_DLY_OFFSET 
SLV_DLY_COARSE 
Reserved 
0
Reserv
ed 
SLV_
EN 
SLV_D
LL...
SLV_
UPD 
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
FREQEN
Frequency enable
0b - Selects delay chain for low frequency of operation
1b - Selects delay chain for high frequency of operation
29-28
—
Reserved
27-24
Reserved
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4723 / 5251


---
# 페이지 1864

Table continued from the previous page...
Field
Function
—
23-20
—
Reserved
19-16
SLV_FINE_OFF
SET
Fine offset delay elements in incoming DQS
This field sets the number of fine offset delay elements up to 16 in incoming DQS, and the default must 
be 1 element.
15
—
Reserved
14-12
SLV_DLY_OFF
SET
T/16 offset delay elements in incoming DQS
This field sets the number of T/16 offset delay elements in incoming DQS; default is 0.
11-8
SLV_DLY_COA
RSE
Delay elements in each delay tap
This field sets the number of delay elements in each delay tap. The field is used to overwrite DLL-
generated delay values and works when the value of SLV_DLL_BYPASS is 1. Note : Please refer to the 
QuadSPI datasheet for more details.
7-5
—
Reserved
4
—
Reserved
3
—
Reserved
2
SLV_EN
Slave enable
0b - DLL slave logic remains in reset, and its value should be 0 for at least three flash memory 
clock cycles for reset.
1b - Enables DQS slave delay chain, and should be 1 before any slave configuration settings take 
place.
1
SLV_DLL_BYP
ASS
Slave DLL bypass
This field enables selection of the number of delays in each slave delay tap.
0b - Disables manual selection of coarse delays in the slave delay chain.
1b - Enables selection of number of delays in each slave delay tap, based on 
DLLCRA[SLV_DLY_COARSE].
0
Slave update
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4724 / 5251


---
# 페이지 1865

Table continued from the previous page...
Field
Function
SLV_UPD
You must program this field only after slave delay chain configuration takes place.
0b - Disables any further update on DQS slave delay chain.
1b - Updates the DQS slave delay chain with either ref-delay or bypass slave delay value, and 
should be set in the absence of the DQS clock.
78.11.2.15
Serial Flash Memory Address Register (SFAR)
Offset
Register
Offset
SFAR
100h
Function
The module automatically translates this address on the memory map to the address on the flash memory. When operating in a 
24-bit mode, only bits 23-0 are sent to the flash memory. In the 32-bit mode, bits 27-0 are used with bits 31-28 driven to 0 . See 
Table 722 for the mapping between the access mode and the SFAR content and Normal mode for details on command triggering 
and command execution. The software must ensure that the serial flash memory address provided in the SFAR register lies in the 
valid flash memory address range, as defined in Table 722.
Special write-access is permitted if:
• SR[IP_ACC] = 0
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
SFADR 
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
SFADR 
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
SFADR
Serial flash memory address
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4725 / 5251


---
# 페이지 1866

78.11.2.16
Sampling Register (SMPR)
Offset
Register
Offset
SMPR
108h
Function
This register allows configuration of how the incoming data from the external serial flash memory devices is sampled in the 
QuadSPI module.
 
See the chip data sheet for programming the register fields.
  NOTE  
Special write-access is permitted in the disabled mode.
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
Reserv
ed 
Reserved 
Reserv
ed 
DLLFSMPFA 
0
Reserved 
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
FSDLY 
FSPH
S 
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
Fields
Field
Function
31
—
Reserved
30-28
—
Reserved
27
—
Reserved
26-24
DLLFSMPFA
Selects the nth tap provided by slave delay chain for flash memory A
The value of n can vary from 0 to 7, with each tap delay based on the DLLCRA register.
23-19
Reserved
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4726 / 5251


---
# 페이지 1867

Table continued from the previous page...
Field
Function
—
18-16
—
Reserved
15-7
—
Reserved
6
FSDLY
Full speed delay selection for SDR instructions
Select the delay with respect to the reference edge for the sample point valid for full speed commands.
0b - One clock cycle delay
1b - Two clock cycles delay
5
FSPHS
Full-speed phase selection for SDR instructions
This field selects the edge of the sampling clock valid for full-speed commands.
0b - Select sampling at non-inverted clock
1b - Select sampling at inverted clock
4-3
—
Reserved
2-0
—
Reserved
78.11.2.17
RX Buffer Status Register (RBSR)
Offset
Register
Offset
RBSR
10Ch
Function
This register contains information related to the receive data buffer.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4727 / 5251


---
# 페이지 1868

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
RDCTR 
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
RDBFL 
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
31-16
RDCTR
Read counter
Indicates the number of 4-byte entries removed from the RX buffer. For example, a value of 0x2 indicates 
that 8 bytes have been removed.
It is incremented by the number (RBCT[WMRK] + 1) on RX buffer POP event. The RX buffer can be popped 
using DMA or FR[RBDF]. The RSER[RBDDE] defines which pop should be pursued. For details, see AHB 
RX Data Buffer Register (ARDB0 - ARDB127) and Data Transfer from the QuadSPI Module Internal Buffers.
15-8
—
Reserved
7-0
RDBFL
RX buffer fill level
Indicates the number of 4-byte entries available in the RX buffer. For example, a value of 0x2 indicates 8 
bytes are available.
78.11.2.18
RX Buffer Control Register (RBCT)
Offset
Register
Offset
RBCT
110h
Function
This register contains control data related to the receive data buffer.
Special write-access is permitted if:
• SR[IP_ACC] = 0
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4728 / 5251


---
# 페이지 1869

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
Reserv
ed 
0
WMRK 
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
31-9
—
Reserved
8
—
Reserved
7-5
—
Reserved
4-0
WMRK
RX buffer watermark
This field determines when the readout action of the RX buffer is triggered. When the number of valid entries 
in the RX buffer is equal to or greater than the number provided by (WMRK+1), the SR[RXWE] flag is 
asserted. The value should be entered as the number of 4-byte entries minus 1. For example, a value of 0x0 
sets the watermark to 4 bytes, 1 to 8bytes, 2 to 12 bytes, and so on.
For details, see DMA usage.
 
This field should never be programmed above 63 because there are only 64 memory 
mapped RBDR registers. If watermark is programmed above 63, data above 64 words will 
be lost.
  NOTE  
78.11.2.19
Data Learning Status Flash Memory A Register (DLSR_FA)
Offset
Register
Offset
DLSR_FA
134h
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4729 / 5251


---
# 페이지 1870

Function
This register shows sampling point selected by data learning algorithm when the value of DLSR_FA[DLPFFA] is 0. Otherwise, 
it shows the pattern matching outline.
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
DLPFF
A 
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
POS_EDGE 
NEG_EDGE 
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
DLPFFA
Data learning pattern fail
This field asserts when data learning fails at flash memory A.
30-16
—
Reserved
15-8
POS_EDGE
DLP positive edge match signature for flash memory A
7-0
NEG_EDGE
DLP negative edge match signature for flash memory A
78.11.2.20
TX Buffer Status Register (TBSR)
Offset
Register
Offset
TBSR
150h
Function
This register contains information related to the transmit data buffer.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4730 / 5251


---
# 페이지 1871

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
TRCTR 
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
TRBFL 
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
31-16
TRCTR
Transmit counter
This field indicates how many entries of 4 bytes have been written into the TX buffer by host accesses. It 
is reset to 0 when a 1 is written to MCR[CLR_TXF]. It is incremented on each write access to the TBDR 
register when another word has been pushed onto the TX buffer. When it is not cleared, the TRCTR field 
wraps around to 0. See TX Buffer Data Register (TBDR) for details.
15-9
—
Reserved
8-6
—
Reserved
5-0
TRBFL
TX buffer fill level
This field contains the number of entries of 4 bytes each available in the TX buffer for the QuadSPI module 
to transmit to the serial flash memory device. The value of this field can reach maximum up to the total TX 
buffer size.
78.11.2.21
TX Buffer Data Register (TBDR)
Offset
Register
Offset
TBDR
154h
Function
This register provides access to the circular TX buffer of depth 32 , so the total size is 32 * 4 bytes. This buffer provides the data 
written into it as write data for the page programming commands to the serial flash memory device. See Table 702 for the byte 
ordering scheme. A write transaction on the flash memory with data size of less than 32 bits leads to the removal of one data entry 
from the TX buffer. The valid bits are used and the rest of the bits are discarded.
Special write-access is permitted if:
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4731 / 5251


---
# 페이지 1872

• SR[TXFULL] = 0
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
TXDATA 
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
TXDATA 
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
TXDATA
TX data
On write access, the data is written to the next available entry of the TX buffer and TBSR[TRBFL] is 
updated accordingly.
On a read access, the last data written to the register is returned.
78.11.2.22
TX Buffer Control Register (TBCT)
Offset
Register
Offset
TBCT
158h
Function
This register contains control information for transmit data buffer.
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
WMRK 
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
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4732 / 5251


---
# 페이지 1873

Fields
Field
Function
31-8
—
Reserved
7-5
—
Reserved
4-0
WMRK
Watermark for TX buffer
Determines the watermark for the TX buffer
When the number of available space in the TX buffer is greater than or equal to the number provided by 
WMRK (number of 4-byte entries), SR[TXWA] is asserted. For example, a value of 0x1 sets the watermark 
to 4 bytes, 0x2 sets it to 8 bytes, 0x3 sets it to 12 bytes, and so on. For details, see DMA usage.
WMRK = 0 is invalid.
78.11.2.23
Status Register (SR)
Offset
Register
Offset
SR
15Ch
Function
This register provides all the available status information about SFM command execution and arbitration, the RX buffer, TX buffer, 
and the AHB buffer.
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
TXFUL
L 
TXDM
A 
TXWA 
TXNE 
RXDM
A 
0
RXFU
LL 
0
RXWE 
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
AHB3
FUL 
AHB2
FUL 
AHB1
FUL 
AHB0
FUL 
AHB3
NE 
AHB2
NE 
AHB1
NE 
AHB0
NE 
AHBT
RN 
Reserv
ed 
0
Reserv
ed 
AHB_
ACC 
IP_
ACC 
BUSY 
W
Reset
0
0
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
0
0
0
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4733 / 5251


---
# 페이지 1874

Fields
Field
Function
31-29
—
Reserved
28
—
Reserved
27
TXFULL
TX buffer full
Asserted when the FIFO level reaches 39 (that is, TX buffer size of 32 + async FIFO size of 7)
26
TXDMA
TX DMA
Asserted when the TXFIFO fill via DMA is active and DMA is requested or running
25
TXWA
TX buffer watermark available
Asserted when the number of available spaces in the TX buffer is greater than or equal to the value provided 
by TBCT[WMRK]
Example: When TBCT[WMRK]=1, SR[TXWA] is de-asserted when TX FIFO has 32+7(size of async 
FIFO) entries
24
TXNE
TX buffer not empty
Asserted when TX buffer contains data
23
RXDMA
RX buffer DMA
Asserted when RX buffer read out via DMA is active; that is, when DMA is requested or running
22-20
—
Reserved
19
RXFULL
RX buffer full
Asserted when the RX buffer is full; that is, when RBSR[RDBFL] is equal to 128
18-17
—
Reserved
16
RXWE
RX buffer watermark exceeded
Asserted when the number of valid entries in the RX buffer exceeds the number provided in RBCT[WMRK]
15
—
Reserved
14
AHB3FUL
AHB 3 buffer full
Asserted when AHB 3 buffer is full
13
AHB 2 buffer full
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4734 / 5251


---
# 페이지 1875

Table continued from the previous page...
Field
Function
AHB2FUL
Asserted when AHB 2 buffer is full
12
AHB1FUL
AHB 1 buffer full
Asserted when the AHB 1 buffer is full
11
AHB0FUL
AHB 0 buffer full
Asserted when the AHB 0 buffer is full
10
AHB3NE
AHB 3 buffer not empty
Asserted when the AHB 3 buffer contains data
9
AHB2NE
AHB 2 buffer not empty
Asserted when the AHB 2 buffer contains data
8
AHB1NE
AHB 1 buffer not empty
Asserted when the AHB 1 buffer contains data
7
AHB0NE
AHB 0 buffer not empty
Asserted when the AHB 0 buffer contains data
6
AHBTRN
AHB access transaction pending
Asserted when there is a pending request on the AHB interface. See Flash memory mapped AMBA bus.
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
AHB_ACC
AHB read access
Asserted when the currently executed transaction is initiated by the AHB bus
1
IP_ACC
IP access
Asserted when transaction currently executed is initiated by the IP bus
0
BUSY
Module busy
Asserted when module is currently busy handling a transaction to an external flash memory device
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4735 / 5251


---
# 페이지 1876

78.11.2.24
Flag Register (FR)
Offset
Register
Offset
FR
160h
Function
This register provides all available flags about SFM command execution and arbitration, which may serve as the source for the 
generation of interrupt service requests. Note that the error flags in this register do not relate directly to the execution of the 
transaction in the serial flash memory device itself but only to the behavior and conditions visible in the QuadSPI module.
Special write-access is permitted in the enabled mode.
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
Reserv
ed 
0
Reserv
ed 
0
TBFF 
TBUF 
0
0
ILLINE 
0
0
0
RBOF 
RBDF 
W
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
AITEF 
AIBSE
F 
ABOF 
Reserv
ed 
0
0
0
IPAEF 
IPIEF 
0
0
0
TFF 
W
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
—
Reserved
30
—
Reserved
29
—
Reserved
28
—
Reserved
27
TBFF
TX buffer fill flag
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4736 / 5251


---
# 페이지 1877

Table continued from the previous page...
Field
Function
Before writing to the TX buffer, this field should be cleared. Then, it should be read back. If it is set, the TX 
buffer can include more data. If the field remains cleared, the TX buffer can be considered as full. See TX 
buffer operation for details.
26
TBUF
TX buffer underrun flag
This field is set if the module tries to pull data when the TX buffer is empty. The IP command leading to 
the TX buffer underrun is continued (data sent to the serial flash memory device is undefined ). Here, a 
valid underrun means that it should have occurred during the transaction so that few bytes (that is, less 
than 4 bytes) are left in FIFO and the remaining are filled with "FFFFh". The software should initiate a TX 
transaction only when 128 bits are written in the TX buffer. This field does not set if transfer is less than 128 
bits. The application must clear the TX buffer in response to this event by writing a 1 to MCR[CLR_TXF]. The 
application must clear the TX buffer in response to this event by writing a 1 to MCR[CLR_TXF].
25
—
Reserved
24
—
Reserved
23
ILLINE
Illegal instruction error flag
This field is set when an illegal instruction is encountered by the controller in any of the sequences. As 
soon as the field is set, you must assert MCR[SWRSTSD] and MCR[SWRSTHD]. That is, reset the flash 
memory and AHB domain after reconfiguring the correct sequence instruction. See Table 700 for a list of 
legal instructions.
22-21
—
Reserved
20
—
Reserved
19-18
—
Reserved
17
RBOF
RX buffer overflow flag
This field is set when no more data can be pushed into the RX buffer from the serial flash memory device.
The IP command leading to this condition is continued until the number of bytes in IPCR[IDATSZ] are read 
from the serial flash memory device.
The content of the RX buffer remains unchanged.
16
RBDF
RX buffer drain flag
This field is set if SR[RXWE] is asserted.
Writing 1 to this field triggers one of the following actions:
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4737 / 5251


---
# 페이지 1878

Table continued from the previous page...
Field
Function
• If the RX buffer has up to RBCT[WMRK] valid entries, then the flag is cleared.
• If the RX buffer has more than RBCT[WMRK] valid entries and the RSER[RBDDE] field is not set 
(flag driven mode), an RX buffer POP event is triggered.
The flag remains set if the RX buffer contains more than RBCT[WMRK] valid entries after the RX buffer POP 
event is complete.
The flag is cleared if the RX buffer contains less than or equal to RBCT[WMRK] valid entries after the RX 
buffer POP event is complete.
See the "Receive Buffer Drain Interrupt or DMA Request" section in Normal mode interrupt and DMA 
requests for details.
15
—
Reserved
14
AITEF
AHB illegal transaction error flag
This is set whenever there is no response generated from QuadSPI to AHB bus in case of an illegal 
transaction and the watchdog timer expires. The timer value is considered as a parameter.
13
AIBSEF
AHB illegal burst size error flag
This is set whenever the total burst size (size x beat) of an AHB transaction is greater than the prefetch 
data size, which is defined by BUFxCR[ADATSZ] or data size mentioned in the sequence pointed to by 
the SEQID field in case ADATSZ = 0. See HBURST support with AHB read details on HBURST feature.
12
ABOF
AHB buffer overflow flag
This is set when the size of the AHB access exceeds the size of the AHB buffer. This condition can occur 
only if BUFxCR[ADATSZ] is programmed incorrectly.
The AHB command leading to this condition is continued until the number of entries according to 
BUFxCR[ADATSZ] have been read from the serial flash memory device.
The content of the AHB buffer is not changed.
11
—
Reserved
10
—
Reserved
9
—
Reserved
8
—
Reserved
7
IPAEF
IP command trigger during AHB access error flag
This is set when the following condition occurs:
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4738 / 5251


---
# 페이지 1879

Table continued from the previous page...
Field
Function
• A write access occurs to IPCR[SEQID] and the SR[AHB_ACC] field is set. Any command leading to 
the assertion of the IPAEF field is ignored.
6
IPIEF
IP command trigger could not be executed error flag
This is set when the SR[IP_ACC] and SR[AWRACC] fields are set (that is, an IP triggered command is 
currently executing) and any of the following conditions occurs:
• Write access to the IPCR. Any command leading to the assertion of the IPIEF flag is ignored.
• Write access to the SFAR
• Write access to the RBCT
5
—
Reserved
4
—
Reserved
3-1
—
Reserved
0
TFF
IP command transaction finished flag
This field is set after the QuadSPI module completes a running IP command. If an error occurs, and the 
related error flags are valid in the same clock cycle, the TFF flag is asserted.
78.11.2.25
Interrupt and DMA Request Select and Enable Register (RSER)
Offset
Register
Offset
RSER
164h
Function
This register provides enables and selectors for the interrupts in the QuadSPI module.
 
Each field of the FR enabled as source for an interrupt prevents the QuadSPI module from entering the Stop mode 
or Module Disable mode when this flag is set.
  NOTE  
Special write-access is permitted in the "Anytime" mode.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4739 / 5251


---
# 페이지 1880

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
Reserv
ed 
Reserved 
0
TBFIE 
TBUIE 
TBFD
E 
Reserv
ed 
ILLINI
E 
Reserv
ed 
RBDD
E 
Reserv
ed 
0
RBOIE RBDIE 
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
Reserv
ed 
AITIE 
AIBSI
E 
ABOIE 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
IPAEI
E 
IPIEIE 
0
Reserv
ed 
0
TFIE 
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
30-29
—
Reserved
28
—
Reserved
27
TBFIE
TX buffer fill interrupt enable flag
This field indicates the TX buffer fill interrupt enable flag.
0b - No TBFF interrupt is generated.
1b - TBFF interrupt is generated.
26
TBUIE
TX buffer underrun interrupt enable flag
This field indicates the TX buffer underrun interrupt enable flag.
0b - No TBUF interrupt is generated
1b - TBUF interrupt is generated
25
TBFDE
TX buffer fill DMA enable
Enables generation of DMA requests for TX buffer fill. When the value of this field is 1, DMA requests are 
generated as long as number of available spaces in the TX buffer is greater than or equal to the value 
provided by TBCT[WMRK].
 
After you write 1 to this field (to enable DMA transfers), writing 0 does not disable 
DMA transfers. You must perform a software reset for the AHB domain by using 
MCR[SWRSTHD] to disable DMA transfers.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4740 / 5251


---
# 페이지 1881

Table continued from the previous page...
Field
Function
0b - No DMA request is generated
1b - DMA request is generated
24
—
Reserved
23
ILLINIE
Illegal instruction error interrupt enable
Triggered by the ILLINE flag in FR
0b - No ILLINE interrupt is generated.
1b - ILLINE interrupt is generated.
22
—
Reserved
21
RBDDE
RX buffer drain DMA enable
This field enables generation of DMA requests for RX buffer drain. When the value of this field is 1, the DMA 
requests are generated as long as SR[RXWE] is set.
 
After you write 1 to this field (to enable DMA transfers), writing 0 does not disable 
DMA transfers. You must perform a software reset for the AHB domain by using 
MCR[SWRSTHD] to disable DMA transfers.
  NOTE  
0b - No DMA request is generated.
1b - DMA request is generated.
20
—
Reserved
19-18
—
Reserved
17
RBOIE
RX buffer overflow interrupt enable
This field indicates the RX buffer overflow interrupt enable flag.
0b - No RBOF interrupt is generated.
1b - RBOF interrupt is generated.
16
RBDIE
RX buffer drain interrupt enable
This field enables generation of IRQ requests for RX buffer drain. When the value of this field is 1, the 
interrupt is asserted as long as SR[RBDF] is set.
0b - No RBDF interrupt is generated.
1b - RBDF Interrupt is generated.
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4741 / 5251


---
# 페이지 1882

Table continued from the previous page...
Field
Function
15
—
Reserved
14
AITIE
AHB illegal transaction interrupt enable flag
This field indicates the AHB illegal transaction interrupt enable flag.
0b - No AITEF interrupt is generated.
1b - AITEF interrupt is generated.
13
AIBSIE
AHB illegal burst size interrupt enable flag
This field indicates the AHB illegal burst size interrupt enable flag.
0b - No AIBSEF interrupt is generated.
1b - AIBSEF interrupt is generated.
12
ABOIE
AHB buffer overflow interrupt enable flag
This field indicates the AHB buffer overflow interrupt enable flag.
0b - No ABOF interrupt is generated.
1b - ABOF interrupt is generated.
11
—
Reserved
10
—
Reserved
9
—
Reserved
8
—
Reserved
7
IPAEIE
IP command trigger during AHB read access error interrupt enable flag
This field indicates IP command trigger during AHB read access error interrupt enable flag.
0b - No IPAEF interrupt is generated
1b - IPAEF interrupt is generated
6
IPIEIE
IP command trigger during IP access error interrupt enable flag
This field indicates IP command trigger during IP access error interrupt enable flag.
0b - No IPIEF interrupt is generated
1b - IPIEF interrupt is generated
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4742 / 5251


---
# 페이지 1883

Table continued from the previous page...
Field
Function
5
—
Reserved
4
—
Reserved
3-1
—
Reserved
0
TFIE
Transaction finished interrupt enable flag
This field indicates the transaction finished interrupt enable flag.
0b - No TFF interrupt is generated.
1b - TFF interrupt is generated.
78.11.2.26
Sequence Pointer Clear Register (SPTRCLR)
Offset
Register
Offset
SPTRCLR
16Ch
Function
This register provides fields to reset the IP and buffer sequence pointers. The sequence pointer contains the index of instructions 
within the LUT entry that is to be executed next. For example, if the LUT entry ends on a JMP_ON_CS value of 2, the index is 
stored as 2.
The software should reset the sequence pointers defined by JMP_ON_CS operand whenever the sequence ID is required to be 
changed by updating the SEQID field in the IPCR or BFGENCR.
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
0
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
W
IPPTR
C 
BFPTR
C 
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
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4743 / 5251


---
# 페이지 1884

Fields
Field
Function
31-26
—
Reserved
25-24
—
Reserved
23-20
—
Reserved
19-18
—
Reserved
17-16
—
Reserved
15-9
—
Reserved
8
IPPTRC
IP pointer clear
This is a self-clearing field.
1b - Clears the sequence pointer for IP accesses as defined in IPCR.
7-1
—
Reserved
0
BFPTRC
Buffer pointer clear
This is a self-clearing field.
1b - Clears the sequence pointer for AHB read accesses as defined in BFGENCR.
78.11.2.27
Serial Flash Memory A1 Top Address Register (SFA1AD)
Offset
Register
Offset
SFA1AD
180h
Function
This register provides the address mapping for serial flash memory A1. The difference between SFA1AD[TPADA1] and 
AMBA_BASE defines the size of the memory map for serial flash memory A1.
Special write-access is permitted if:
• SR[IP_ACC] = 0
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4744 / 5251


---
# 페이지 1885

• SR[AHB_ACC] = 0
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
TPADA1 
W
Reset
0
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
TPADA1 
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
31-10
TPADA1
Top address for serial flash memory A1
In effect, TPADxx is the first location of the next memory.
9-0
—
Reserved
78.11.2.28
Serial Flash Memory A2 Top Address Register (SFA2AD)
Offset
Register
Offset
SFA2AD
184h
Function
This register provides the address mapping for serial flash memory A2. The difference between SFA2AD[TPADA2] and 
SFA1AD[TPADA1] defines the size of the memory map for serial flash memory A2.
Special write-access is permitted if:
• SR[IP_ACC] = 0
• SR[AHB_ACC] = 0
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4745 / 5251


---
# 페이지 1886

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
TPADA2 
W
Reset
0
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
TPADA2 
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
31-10
TPADA2
Top address for serial flash memory A2
In effect, TPxxAD is the first location of the next memory.
9-0
—
Reserved
78.11.2.29
Serial Flash Memory B1 Top Address Register (SFB1AD)
Offset
Register
Offset
SFB1AD
188h
Function
This register provides the address mapping for serial flash memory B1. The difference between SFB1AD[TPADB1] and 
SFA2AD[TPADA2] defines the size of the memory map for serial flash memory B1.
Special write-access is permitted if:
• SR[IP_ACC] = 0
• SR[AHB_ACC] = 0
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4746 / 5251


---
# 페이지 1887

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
TPADB1 
W
Reset
0
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
TPADB1 
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
31-10
TPADB1
Top address for serial flash memory B1.
In effect, TPxxAD is the first location of the next memory.
9-0
—
Reserved
78.11.2.30
Serial Flash Memory B2 Top Address Register (SFB2AD)
Offset
Register
Offset
SFB2AD
18Ch
Function
This register provides the address mapping for serial flash memory B2. The difference between SFB2AD[TPADB2] and 
SFB1AD[TPADB1] defines the size of the memory map for serial flash memory B2.
Special write-access is permitted if:
• SR[IP_ACC] = 0
• SR[AHB_ACC] = 0
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4747 / 5251


---
# 페이지 1888

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
TPADB2 
W
Reset
0
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
TPADB2 
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
31-10
TPADB2
Top address for serial flash memory B2.
In effect, TPxxAD is the first location of the next memory.
9-0
—
Reserved
78.11.2.31
RX Buffer Data Register (RBDR0 - RBDR63)
Offset
For a = 0 to 63:
Register
Offset
RBDRa
200h + (a × 4h)
Function
These registers provide access to individual entries in the RX buffer. See Table 702 for the byte ordering scheme.
RBDR0 corresponds to the actual position of the read pointer within the RX buffer. The number of valid entries available depends 
on the number of RX buffer entries implemented and on the number of valid buffer entries available in the RX buffer.
Example 1 - RX buffer filled completely with 128 words: In this case, the address range for valid read access extends from RBDR0 
to RBDR63.
Example 2 - RX buffer filled with five valid words: RX buffer fill level of RBSR[RDBFL] is 5. In this case, access to RBDR4 provides 
the last valid entry.
Any access beyond the range of valid RX buffer entries provides undefined results.
 
To access data beyond RBDR[63], you must pop the data by using FR[RBDF]. See here for details.
  NOTE  
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4748 / 5251


---
# 페이지 1889

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
RXDATA 
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
RXDATA 
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
RXDATA
RX data
This field contains the data associated with the related RX buffer entry. For data format and byte ordering, 
see Byte ordering of serial flash memory read data.
78.11.2.32
LUT Key Register (LUTKEY)
Offset
Register
Offset
LUTKEY
300h
Function
This register contains the key to lock and unlock the LUT. See LUT for details.
Special write-access is permitted in the "Anytime" mode.
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
KEY 
W
Reset
0
1
0
1
1
0
1
0
1
1
1
1
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
KEY 
W
Reset
0
1
0
1
1
0
1
0
1
1
1
1
0
0
0
0
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4749 / 5251


---
# 페이지 1890

Fields
Field
Function
31-0
KEY
Key to lock or unlock the LUT
The key is 0x5AF05AF0 and the read value is always 0x5AF05AF0.
78.11.2.33
LUT Lock Configuration Register (LCKCR)
Offset
Register
Offset
LCKCR
304h
Function
This register is used along with the LUTKEY register to lock or unlock the LUT. This register should be written immediately after 
the LUTKEY register for the lock or unlock operation to be successful. See LUT for details. Setting both the LOCK and UNLOCK 
bits as "00" or "11" is not allowed.
Special write access is permitted after writing the LUT key register.
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
UNLO
CK 
LOCK 
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
1
UNLOCK
Unlock LUT
Unlocks the LUT when the following two conditions are met:
• This register is written just after the LUT Key Register (LUTKEY).
• The LUT key register was written with the 0x5AF05AF0 key.
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4750 / 5251


---
# 페이지 1891

Table continued from the previous page...
Field
Function
0
LOCK
Lock LUT
Locks the LUT when the following conditions are met:
• This register is written just after the LUT Key Register (LUTKEY).
• The LUT key register is written with the 0x5AF05AF0 key.
78.11.2.34
LUT Register (LUT0)
Offset
Register
Offset
LUT0
310h
Function
A sequence of instruction-operand pairs may be pre-populated in the LUT according to the device connected on board. Each 
instruction-operand pair is of 16 bits (2 bytes) each. Every sequence preprogrammed by Program Sequence Engine in the LUT 
is referred to by its index. The LUT registers act as lookup tables for sequences of instructions. The programmable sequence 
engine executes the instructions in these sequences to generate a valid serial flash memory transaction. There are a total of 20 
LUT registers. These 20 registers are divided into groups of 5 registers that make a valid sequence. Therefore, LUT[0], LUT[5], 
LUT[10] ..... LUT[15] are the starting registers of a valid sequence. Each of these sets of 5 registers can have a maximum of 10 
instructions. Reset value of the register shown below is only applicable to LUT2 to LUT19. A maximum of 4 sequences can be 
defined at one time. See LUT that describes the LUT registers in detail.
Special write-access is permitted if the LUT is unlocked.
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
INSTR1 
PAD1 
OPRND1 
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
0
0
0
1
1
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
INSTR0 
PAD0 
OPRND0 
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
1
1
Fields
Field
Function
31-26
Instruction 1
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4751 / 5251


---
# 페이지 1892

Table continued from the previous page...
Field
Function
INSTR1
25-24
PAD1
Pad information for INSTR1
00b - 1 Pad
01b - 2 Pads
10b - 4 Pads
11b - NA
23-16
OPRND1
Operand for INSTR1
15-10
INSTR0
Instruction 0
9-8
PAD0
Pad information for INSTR0
00b - 1 Pad
01b - 2 Pads
10b - 4 Pads
11b - NA
7-0
OPRND0
Operand for INSTR0
78.11.2.35
LUT Register (LUT1)
Offset
Register
Offset
LUT1
314h
Function
A sequence of instruction-operand pairs may be pre-populated in the LUT according to the device connected on board. Each 
instruction-operand pair is of 16 bits (2 bytes) each. Every sequence preprogrammed by Program Sequence Engine in the LUT 
is referred to by its index. The LUT registers act as lookup tables for sequences of instructions. The programmable sequence 
engine executes the instructions in these sequences to generate a valid serial flash memory transaction. There are a total of 20 
LUT registers. These 20 registers are divided into groups of 5 registers that make a valid sequence. Therefore, LUT[0], LUT[5], 
LUT[10] ..... LUT[15] are the starting registers of a valid sequence. Each of these sets of 5 registers can have a maximum of 10 
instructions. Reset value of the register shown below is only applicable to LUT2 to LUT19. A maximum of 4 sequences can be 
defined at one time. See LUT that describes the LUT registers in detail.
Special write-access is permitted if the LUT is unlocked.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4752 / 5251


---
# 페이지 1893

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
INSTR1 
PAD1 
OPRND1 
W
Reset
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
INSTR0 
PAD0 
OPRND0 
W
Reset
0
0
0
1
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
0
Fields
Field
Function
31-26
INSTR1
Instruction 1
25-24
PAD1
Pad information for INSTR1
00b - 1 Pad
01b - 2 Pads
10b - 4 Pads
11b - NA
23-16
OPRND1
Operand for INSTR1
15-10
INSTR0
Instruction 0
9-8
PAD0
Pad information for INSTR0
00b - 1 Pad
01b - 2 Pads
10b - 4 Pads
11b - NA
7-0
OPRND0
Operand for INSTR0
78.11.2.36
LUT Register (LUT2 - LUT19)
Offset
For a = 2 to 19:
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4753 / 5251


---
# 페이지 1894

Register
Offset
LUTa
310h + (a × 4h)
Function
A sequence of instruction-operand pairs may be pre-populated in the LUT according to the device connected on board. Each 
instruction-operand pair is of 16 bits (2 bytes) each. Every sequence preprogrammed by Program Sequence Engine in the LUT 
is referred to by its index. The LUT registers act as lookup tables for sequences of instructions. The programmable sequence 
engine executes the instructions in these sequences to generate a valid serial flash memory transaction. There are a total of 20 
LUT registers. These 20 registers are divided into groups of 5 registers that make a valid sequence. Therefore, LUT[0], LUT[5], 
LUT[10] ..... LUT[15] are the starting registers of a valid sequence. Each of these sets of 5 registers can have a maximum of 10 
instructions. Reset value of the register shown below is only applicable to LUT2 to LUT19. A maximum of 4 sequences can be 
defined at one time. See LUT that describes the LUT registers in detail.
Special write-access is permitted if the LUT is unlocked.
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
INSTR1 
PAD1 
OPRND1 
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
INSTR0 
PAD0 
OPRND0 
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
31-26
INSTR1
Instruction 1
25-24
PAD1
Pad information for INSTR1
00b - 1 Pad
01b - 2 Pads
10b - 4 Pads
11b - NA
23-16
OPRND1
Operand for INSTR1
15-10
Instruction 0
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4754 / 5251


---
# 페이지 1895

Table continued from the previous page...
Field
Function
INSTR0
9-8
PAD0
Pad information for INSTR0
00b - 1 Pad
01b - 2 Pads
10b - 4 Pads
11b - NA
7-0
OPRND0
Operand for INSTR0
78.11.3 Serial flash memory address assignment
The serial flash memory address assignment can be modified by writing into Serial Flash Memory A1 Top Address Register 
(SFA1AD) and Serial Flash Memory A2 Top Address Register (SFA2AD) for device A
Table 722. Serial flash memory address assignment
Parameter
Function
Access mode
QuadSPI_AMBA_BAS
E ((31:10) - 22 bits)
QuadSPI AHB base address
First address of the serial flash 
memory device as presented to the 
QuadSPI controller. This might be 
the base of the serial flash memory 
in the system address map or it may 
be a remapping, for instance to 0h, 
performed by the system. (See the 
system address map file attached to 
this document)
QuadSPI_ARDB_BAS
E
First address of the QuadSPI Rx 
buffer on system memory map
TOP_ADDR_MEMA1(T
PADA1)
Top address for the external flash 
memory A1 (the first of the two 
independent flash memories sharing 
the IOFA)
Any access to the address space between 
TOP_ADDR_MEMA1 and QuadSPI_AMBA_BASE is routed 
to serial flash memory A1.
TOP_ADDR_MEMA2(T
PADA2)
Top address for the external flash 
memory A2 (the second of the two 
independent flash memories sharing 
the IOFA)
Any access to the address space between 
TOP_ADDR_MEMA2 and TOP_ADDR_MEMA1 is routed to 
serial flash memory A2.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4755 / 5251


---
# 페이지 1896

78.12 Flash memory mapped AMBA bus
QuadSPI_AMBA_BASE defines the address to be used as the start address of the serial flash memory device, as defined by the 
system memory map. Note that this may be a remapping of the physical address of the serial flash memory in the system. See 
the system address map for details.
Table 723. QuadSPI AMBA bus memory map
Address
Register name
QuadSPI_AMBA_BASE to (TOP_ADDR_MEMA2 
- 1h)
• See Memory-mapped serial flash memory data—individual flash 
memory mode on flash memory A.
• For information about byte ordering, see Table 702 and Table 703.
QuadSPI_ARDB_BASE to... (32 * 4 Byte) 
QuadSPI_ARDB_BASE + 1FFh
• See AHB RX Data Buffer Register (ARDB0 - ARDB127).
• For information about the byte ordering, see Table 702.
 
Any read access to non-implemented addresses provides undefined results.
In individual flash memory modes, the 3/4 address bytes (as programmed in the instruction/operand in the 
sequence) available for the flash memory address are determined by SFADR[23:0] or SFADR[31:0] as provided 
in the table shown above.
  NOTE  
78.12.1 AHB bus access read considerations
Note that all logic in the QuadSPI module implementing the AHB bus access is designed to read the content of an external serial 
flash memory device. Therefore, the following restrictions apply to the QuadSPI module with respect to accesses to the AHB bus:
• Any AHB command resulting in the assertion of the FR[ABSEF] flag is answered with the ERROR condition according to 
the AMBA_AHB specification. The resulting AHB command is ignored.
• AHB bus read access types—NONSEQ and BUSY—are fully supported.
• AHB read access type—SEQ—is treated in the same way as NONSEQ. See Flash memory mapped AMBA bus for 
details.
• Early burst termination is not supported for AHB transactions.
78.12.2 Memory-mapped serial flash memory data—individual flash memory mode on flash memory A
Starting with address QuadSPI_AMBA_BASE, the content of the first external serial flash memory device is mapped into the 
address space of the device containing the QuadSPI module. Serial flash memory byte address 0h corresponds to bus address, 
QuadSPI_AMBA_BASE, in an increasing order. . See the following table for the address mapping. The byte ordering for 32-bit 
access is provided in Table 702 and for 64-bit read access, the byte ordering is provided in Table 703.
Table 724. Memory-mapped individual flash memory mode—flash memory A address scheme
Memory-mapped address 32-
bit access
Memory-mapped address 64-
bit access
Serial flash memory byte address
Flash 
memory 
device
QuadSPI_AMBA_BASE + 0h
QuadSPI_AMBA_BASE + 0h
0h to 3h
A1
QuadSPI_AMBA_BASE + 4h
4h to 7h
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4756 / 5251


---
# 페이지 1897

Table 724. Memory-mapped individual flash memory mode—flash memory A address scheme (continued)
Memory-mapped address 32-
bit access
Memory-mapped address 64-
bit access
Serial flash memory byte address
Flash 
memory 
device
...
...
...
TOP_ADDR_MEMA1 - 8h
TOP_ADDR_MEMA1 - 8h
(TOP_ADDR_MEMA1- 8h) to 
(TOP_ADDR_MEMA1 - 0h4 -0h1)
TOP_ADDR_MEMA1 - 4h
(TOP_ADDR_MEMA1 - 4h) to 
(TOP_ADDR_MEMA1 - 0h1)
TOP_ADDR_MEMA1 + 4h
TOP_ADDR_MEMA1 + 0h
0h to 3h
A2
TOP_ADDR_MEMA1 + 0h4
4h to 7h
...
...
...
TOP_ADDR_MEMA2 - 8h
TOP_ADDR_MEMA2 - 8h
(TOP_ADDR_MEMA2 - 8h) to 
(TOP_ADDR_MEMA2 - 4h - 1h)
TOP_ADDR_MEMA2 - 4h
(TOP_ADDR_MEMA2 - 4h) to 
(TOP_ADDR_MEMA2 - 1h)
The available address range depends on the size of the external serial flash memory device. Any access beyond the size of the 
external serial flash memory provides undefined results.
For details concerning the read process, see Flash memory read.
78.12.3 ARDB register descriptions
 
See the system memory map in this document for the base address of the QuadSPI AHB RX data buffer.
  NOTE  
78.12.3.1
ARDB memory map
QuadSPI_34x_ARDB base address: 6800_0000h
Offset
Register
Width
(In bits)
Access
Reset value
0h - 1FCh
AHB RX Data Buffer Register (ARDB0 - ARDB127)
32
R
0000_0000h
78.12.3.2
AHB RX Data Buffer Register (ARDB0 - ARDB127)
Offset
For a = 0 to 127:
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4757 / 5251


---
# 페이지 1898

Register
Offset
ARDBa
0h + (a × 4h)
Function
This register is used to read the buffer content of the RX buffer from successive addresses. ARDB0 corresponds to the RX buffer 
register entry corresponding to the current value of the read pointer in an increasing order.
The increment of the read pointer depends on the access scheme (DMA or flag-driven). See Flash memory read, RX buffer, 
data read through register interface, and AHB read for the description of successive accesses to the RX buffer content. See Byte 
Ordering of Serial Flash Memory Read Data for the byte ordering scheme.
Valid address range accessible in the ARDBn range depends on the number of RX buffer entries implemented and on the number 
of valid buffer entries available in the RX buffer.
• Example 1 - RX buffer filled completely with 128 words: In this case, the address range for valid read access extends from 
ARDB0 to ARDB127.
• Example 2 - RX buffer filled with five valid words; RX buffer fill level RBSR[RDBFL] is 5. In this case, an access to ARDB4 
provides the last valid entry.
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
ARXD 
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
ARXD 
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
ARXD
ARDB provided RX buffer data
Byte order (endianness) is identical to the RX buffer data registers.
78.13 Glossary
AHB
Advanced high-performance bus, a version of AMBA
AMBA
Advanced microcontroller bus architecture
APB
Advanced peripheral bus
BE
Big endian byte ordering
CRS
Center aligned read strobe
CS
Chip select
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4758 / 5251


---
# 페이지 1899

FRAD
Flash region access descriptor
I/O
Input output, I/O lines are also referred to as pads in this chapter
IFM
Individual flash memory mode
LE
Little endian
MDAD
Master domain access descriptors
MGID
Master-Group identifier
PCS
Peripheral chip select
SCK
Serial communications clock
SFM
Serial flash memory
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K322, S32K342, S32K341, S32K314, S32K324, and S32K344
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4759 / 5251


---