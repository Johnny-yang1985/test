# 페이지 1900

Chapter 79
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
79.1 Chip-specific QuadSPI information
79.1.1 QuadSPI configuration
Table 725. QuadSPI instances
Instance
S32K358/S32K348/S32K338/S32K328
QuadSPI
Yes
Table 726. QuadSPI configuration details
Configuration
S32K358/S32K348/S32K338/S32K328
QuadSPI Tx FIFO size
256 words
QuadSPI Rx FIFO size
32 words
Look Up Table Size
16 words
Rx Buffer
1024 Bytes
For supported data rates, see device Datasheet.
 
Boot from QuadSPI is not supported but execution from external memory is supported.
  NOTE  
Table 727. Features supported
Feature
S32K358/S32K348/S32K338/S32K328
AHB Write
Yes
Data learning feature
Yes
DLL
Yes
OTFAD (On-the-fly-AES-decryption engine)
No
DDR mode
Yes
HyperRAM
Yes
HyperFlash
Yes
External DQS (Data Strobe)
Yes
Boot from QuadSPI interface
No
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4760 / 5251


---
# 페이지 1901

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
Figure 507. Block diagram
79.1.2 Supported read modes
The table below provides an overview of the QuadSPI read modes.
Table 728. QuadSPI read modes
Read modes
SDR support 
(QuadSPI_MCR 
[DDR_EN]=0)
QuadSPI_MCR 
[DQS_EN]
QuadSPI_MCR 
[DQS_FA_SEL]
DLL/Data 
learning 
support
DQS sampling 
method
Pad loopback
Yes
1
01
Yes
79.1.3 QuadSPI initialization sequence
Following initialization sequence should be followed for proper QuadSPI operation:
• Enable QuadSPI module by MC_ME peripheral clock enable (register PRTNx_COFBy_CLKEN present within MC_ME). 
Refer MC_ME chapter for peripheral mapping.
• Configure the SIUL2 registers MSCR[OBE] as 1 and MSCR[SSS] as 0 for QuadSPI_SCKFA pin.
• Initialize QuadSPI SCKFA by writing a sequence of 1010 to the SIUL2 register GPDO[PDO_a] for QuadSPI_SCKFA pin.
• Configure the SIUL2 register MSCR[OBE] back as 0 for the pins.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4761 / 5251


---
# 페이지 1902

• Initiate a dummy flash read to reset all DQS flops by itself and any crossing from DQS domain to IPS/AHB is taken care 
by CDC logic.
• Initiate a peripheral software reset to QuadSPI controller by writing to QuadSPI controller’s MCR.
• Post this initialization sequence, the QuadSPI will work in intended deterministic manner.
 
QuadSPI initialization is to be done before using QuadSPI after each functional reset.
  NOTE  
79.1.4 Pad clock loopback
This chip supports pad clock loopback. The QuadSPI can be configured to use clock loopback to sample input data. SCK is 
delayed by the SCK pin output delay, plus the SCK pin input delay using pad loopback, and is configured by setting QuadSPI 
config registers SOCCR[SOCCFG] and MCR[DQS_FA_SEL]. Enabling the loopback version of SCK can improve the setup time 
of the input data from the Flash.
For details of these register, see QuadSPI register descriptions.
79.1.5 QuadSPI SOC Configuration register SOCCR[SOCCFG] implementation
The QuadSPI SOC Configuration register QuadSPI_SOCCR[SOCCFG] register is used to control dummy loopback pads and 
obe_pull_timing_relax_b. Below is the description of it's bits:
Table 729. SOCCR[SOCCFG] implementation
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
 
This SoC does not support dual die flashes. Hence, the signal PCSFA2 from QuadSPI is not used.
  NOTE  
79.2 Introduction
The QuadSPI module acts as an interface to a single serial flash memory device, with up to eight bidirectional data lines.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4762 / 5251


---
# 페이지 1903

79.2.1 Features
QuadSPI supports the following features:
• Flexible sequence engine to support various flash memory vendor devices. As there is no specific standard, the module 
supports various kinds of flash memories from different vendors. See Serial flash memory devices for example sequences.
• Single, dual, and quad modes of operation supported for Quad flash memories
• Octal and single IO modes of operation supported for Octal flash memories
• Double Data Rate (DDR)/Double Transfer Rate (DTR) mode in which the data is generated on every edge of the serial flash 
memory clock
• Flash memory data strobe signal to support data sampling in DDR and Single Data Rate (SDR) mode
• Support for HyperFlash memory
• Support for HyperRAM
• Support for Macronix Octal Data integrity features such as ECC and R/W parity (CRC1)
• AHB master to read RX buffer data through AMBA AHB (64-bit width interface) or IPS registers space (32-bit access) and fill 
TX buffer via IPS registers space (32-bit access) or using AHB (64-bit width interface)
— AHB master can be a DMA with a configurable inner loop size
• Multi-master accesses are allowed
— Flexible and configurable buffer for each master—total available buffer size is 1024 bytes.
• All AHB accesses to flash/RAM memory devices are directly memory mapped to the chip system memory
• Programmable sequence engine to cater to future command/protocol changes and ability to support all existing vendor 
commands and operations. The software needs to select the corresponding sequence according to the connected flash 
memory device.
— Support for all types of addressing
79.2.2 RX buffer push event
To add the valid entries into the RX buffer
By default, each buffer push event adds two entries to the RX buffer because the interface to the serial clock domain is 64 bits 
in width. Depending on the number of bytes read from the serial flash memory device, it is possible for the very last buffer push 
event that only one entry is added.
RBSR[RDBFL] is incremented by the number of entries added to the RX buffer.
79.2.3 RX buffer POP event
To remove valid entries from the RX buffer
Each buffer POP event removes (RBCT[WMRK] + 1) valid entries from the buffer. BSR[RDBFL] is decremented by the same 
number and RBSR[RDCTR] is incremented accordingly.
79.2.4 Block diagram
The following figure shows a block diagram of the QuadSPI module.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4763 / 5251


---
# 페이지 1904

QSPI_IC_SFM
Clock Domain Crosser
QSPI_IF
Programmable sequence engine
SCLK clock domain
Flexible I/O controller
SCLK clock domain
IOFA[7:0]
SCKFA
PCSFA2
PCSFA1
QuadSPI Bus Flash Memory A
DQSFA
RX 
Buffer
LUT
DMA and interrupt control
Registers
IP command 
build and control
AHB control
IP control
  TX 
buffer
AHB
buffer
AHB slave and 
buffer management
      received
(data from flash)
             +
Control information
ARDB
Read
AHB read
    data
      IPS write
(Data + Control)
      IPS read
(Data + Control)
     transmit
(data to flash)
      received
(data from flash)
Peripheral Bus
AHB Bus
read/write
(Addr, Size)
read_done
(Data)
AHB write
    data
wr_data
(Data)
define
(Addr, Cmd)
wr_data
(Data)
rd_data
(Data)
SFP
Figure 508. QuadSPI block diagram
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4764 / 5251


---
# 페이지 1905

79.2.5 QuadSPI modes of operation
QuadSPI supports the following modes of operation:
• Normal mode: You can use this mode for write or read accesses to an external serial flash memory device. See Normal mode 
for details.
— Serial flash memory write: You can program data into the flash memory through the IP interface only. See Flash memory 
programming for details.
— Serial flash memory read: Read the contents of the serial flash memory device. Two separate read channels are 
available through the RX buffer and AHB buffer. See Flash memory read for details.
• Module Disable mode: You can use this mode for disabling serial flash memory clock and AHB command. The clock to 
the non-memory mapped logic in QuadSPI can be stopped in the Module Disable mode. The module enters the mode by 
setting MCR[MDIS].
79.3 External signal description
This section provides the external signal information for the QuadSPI module.
The following table lists the external signals belonging to the module in conjunction with the different modes of operation.
Table 730. Signal properties
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
represents the second of the two flash memory devices that share IOFA.
SCKFA
Serial Clock Flash 
Memory A
O
This signal is the serial clock output to the serial flash memory device A.
IOFA[7:0]
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
DQSFA
Data Strobe signal 
Flash Memory A
I/O
This is the data strobe signal for port A. Some flash memory vendors provide 
the Data Read Strobe (DQS) signal to which the read data is aligned in DDR 
mode. It is also provided as an output signal during write data phase.
INTA
ECC error signal for 
Flash Memory A
I
Flash Memory A drives this signal to active low value in case of an ECC 
error.
 
Please refer to chip specific information to check the configuration of QuadSPI block.
  NOTE  
79.3.1 Driving external signals
Single/dual/quad/octal instructions
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4765 / 5251


---
# 페이지 1906

Depending on the serial flash memory device connected to the QuadSPI module, there are instructions using a different number 
of data lines:
• Single pad: Single line I/O with one data out and one data in line to/from the serial flash memory device
• Dual pad: Dual line I/O with two bidirectional I/O lines, driven alternatively by the serial flash memory device or the 
QuadSPI module
• Quad pad: Quad line I/O with four bidirectional I/O lines, driven alternatively by the serial flash memory device or the 
QuadSPImodule
• Octal pad: Octal line I/O with eight bidirectional I/O lines, driven alternatively by the serial flash memory device or the 
QuadSPI module
The different phases of the serial flash memory access scheme are shown in the following figure.
PCSFx
Single pad(I/O) instructions
Not driven
SCKFx
IOFx[0]
IOFx[1]
IOFx[3:2]
IOFx[3:2]
IOFx[1:0]
(pad
Driven all the time, values taken according to phase
Not driven
IOFx[3:0]
Not driven
Driven for 
Tx Instr. only
Driven for 
Tx Instr. only
Dual pad (I/O) instructions
Quad pad (I/O) instructions
(pad
Idle
Instruction
Address
Idle
Data
Mode
Dummy
=
=
2'b0)
2'b01)
(pad = 2'b10)
Octal pad (I/O) instructions (pad = 2'b11)
IOFx[7:0]
Not driven
Driven for 
Tx Instr. only
Driven all the time, values taken from QSPI_MCR[ISDnFx]
Driven all the time, values taken from QSPI_MCR[ISDnFx]
Driven as given in the Note1
Driven as given in the Note1
Driven as given in the Note1
Figure 509. Serial flash memory access scheme
Note1:The IOs are driven from QuadSPI as per the number of pads configured for ongoing phase.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4766 / 5251


---
# 페이지 1907

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
• Dummy: Dummy clocks are provided to the serial flash memory device. See Figure 509 for the IOFx signals driven. The actual 
data lines required for the SFM command executed are not driven for data read commands.
 
— This phase is not applicable for all the SFM commands.
— All read commands in Dual pad, Quad pad /or Octal pad modes must use a Dummy phase immediately 
before the Data phase. The Dummy phase pad configuration in the LUT must use the same number of pads 
as the subsequent Data phase. Note that this restriction is not applicable to Single-pad mode.
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
79.4 Functional description
This section provides a functional description of the QuadSPI module.
79.4.1 Serial flash memory access schemes
In the individual flash memory mode, all supported commands are available.
79.4.2 Normal mode
This mode allows communication with an external serial flash memory device. Compared to the standard SPI protocol, this 
communication method uses up to eight bidirectional data lines operating at high-data rates. The communication to the external 
serial flash memory device consists of an instruction code and optional address, mode, dummy, and data transfers. The flexible 
programmable core engine described below is immune to a wide variety of command or protocol differences in the serial flash 
memory devices provided by various flash memory vendors.
79.4.2.1
Programmable sequence engine
The core of the QuadSPI module is a programmable sequence engine that works on "instruction-operand" pairs. The core 
controller executes each programmed instruction sequentially. The complete list of instructions and the corresponding operands 
are provided in the following table.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4767 / 5251


---
# 페이지 1908

Table 731. Instruction set
Instruction
Instruction 
encoding
Pins
Operand
Action on serial flash memories
CMD
1d
N={0,1,2,3}d
0d - One pad
1d - Two pads
2d - Four pads
3d- Eight pads
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
to be sent (for 
example, 24d 
=> 24 address 
bits required)
Provide the serial flash memory with address cycles according 
to the operand on the number of pads specified
The actual address to be provided is derived from the incoming 
address in case of AHB-initiated transactions and the value 
of SFAR in case of IPS-initiated transactions, if the value of 
SFACR[CAS] is set to 0. Otherwise, the actual address takes 
CAS into consideration.
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
 
If DLL is enabled and N dummy cycles 
are needed, you must program two back-
to-back DUMMY instructions: DUMMY: 
N-2 followed by DUMMY:2.
  NOTE  
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
N={0,1,2,3}d
0d - One pad
1d - Two pads
2d - Four pads
3d- Eight pads
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
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4768 / 5251


---
# 페이지 1909

Table 731. Instruction set (continued)
Instruction
Instruction 
encoding
Pins
Operand
Action on serial flash memories
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
 
This instruction is not supported if DLL 
is enabled.
  NOTE  
ADDR_DDR
10d
N={0,1,2,3}d
0d - One pad
1d - Two pads
2d - Four pads
3d- Eight pads
Number of 
address bits 
to be sent (for 
example, 24d 
=> 24 address 
bits required)
Provide the serial flash memory with address cycles according 
to the operand on the number of pads specified at each clock 
edge of serial flash memory clock. The actual address to be 
provided is derived from the incoming address in case of 
AHB-initiated transactions and the value of SFAR in case of 
IPS-initiated transactions if SFACR[CAS] is set to 0. Otherwise, 
the actual address takes CAS into consideration.
MODE_DDR
11d
8-bit mode 
value
Provide the serial flash memory with 8-bit operand on the 
number of pads specified at each clock edge of serial 
flash memory
MODE2_DDR 12d
N={0}d
2-bit mode 
value
Provide the serial flash memory with 2-bit operand on the 
number of pads specified at each clock edge of serial flash 
memory 4
MODE4_DDR 13d
N={0,1}d
4-bit mode 
value
Provide the serial flash memory with 4-bit operand on the 
number of pads specified at each clock edge of serial flash 
memory 5.
READ_DDR
14d
N={0,1,2,3}d
0d - One pad
1d - Two pads
2d - Four pads
3d - Eight 
pads
Read data 
size in bytes 
(for AHB 
transactions, 
the 
application 
should ensure 
that data size 
is in multiple 
of 8 bytes)
Read data from flash memory on the number of pads specified 
at each clock edge of serial flash memory. The data size might 
be overwritten by writing to the ADATSZ field of the BUFxCR 
registers for AHB-initiated transactions and IDATSZ field of IP 
Configuration Register (IPCR) for IP initiated transactions.
WRITE_DDR
15d
Write data 
size in bytes
Write data on the number of pads specified at each clock edge 
of serial flash memory
The data size can be overwritten by writing to the IDATSZ field 
of IP Configuration Register (IPCR).
DATA_LEAR
N
16d
N={0,1,2,3}d
0d - One pad
Operand[7]-
Find the correct sampling point with the data learning pattern.
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4769 / 5251


---
# 페이지 1910

Table 731. Instruction set (continued)
Instruction
Instruction 
encoding
Pins
Operand
Action on serial flash memories
1d - Two pads
2d - Four pads
3d- Eight pads
• 1 - DDR 
mode
• 0 - SDR 
mode
Operand[6:0]-
• Number 
of bits to 
be used 
for data 
learning. 
For 
example, 
if operand 
is 16 then 
a 16-bit 
data 
learning 
pattern is 
read and 
compare
d.
When this instruction is encountered, the value of Sampling 
Register (SMPR) is ignored and the controller finds the 
correct sampling point on its own by sampling the data 
learning pattern.6
CMD_DDR
17d
N={0,1,2,3}d
0d - One pad
1d - Two pads
2d - Four pads
3d- Eight pads
8-bit 
command 
value
Provides the serial flash memory with the SFM command 
operand (Encoded) on the number of pads specified in 
DTR mode.
CADDR
18d
Number of 
column 
address bits 
to be sent (8d 
means 8 bits 
of column 
address is to 
be sent)
Provide the serial flash memory with column address cycles 
according to the operand on the number of pads specified. 
The actual address to be provided to flash memory depends 
on the value of SFACR[CAS]. For example, if the value of 
SFACR[CAS] is 3, then the address to flash memory will be 
[2:0] of incoming address in case of AHB and the value of SFAR 
in case of IP. This is appended with 0 if SFACR[CAS] is less 
than number of pads for a flash memory.
CADDR_DDR 19d
Number of 
column 
address bits 
to be sent(8d 
means 8 bits 
of column 
address is to 
be sent)
Provide the serial flash memory with column address cycles 
according to the operand on the number of pads specified 
at each clock edge of the serial flash memory. The actual 
address to be provided to flash memory depends on the value 
of SFACR[CAS]. For example, if CAS is 3, then the address to 
flash memory will be [2:0] of incoming address in case of AHB 
and the value of SFAR in case of IP. This is appended with 0 if 
CAS is less than the number of pads for a flash memory.
JMP_TO_SE
Q3
20d
NA
Sequence 
number
Every time CS is deasserted, jump to the LUT sequence 
is pointed to by the operand. This instruction allows the 
programmer to join two sequences and initiates the second 
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4770 / 5251


---
# 페이지 1911

Table 731. Instruction set (continued)
Instruction
Instruction 
encoding
Pins
Operand
Action on serial flash memories
flash memory transaction automatically. It can be used to join 
write-enables with flash memory write or data learn with read.
 
This instruction is not supported if DLL 
is enabled.
  NOTE  
STOP3
0d
NA
NA
Stop execution; deassert CS
1. For a one-pad instruction, MODE2 takes two serial flash memory clock cycles on the flash memory interface.
2. For a one-pad instruction, MODE4 takes four serial flash memory clock cycles on the flash memory interface. For a 
four-pad instruction, MODE4 takes one serial flash memory clock cycle on the flash memory interface.
3. Sequence ending with this instruction must have all remaining bits as 0s after it.
4. For a one-pad instruction, MODE2_DDR takes one serial flash memory clock cycle on the flash memory interface.
5. For a one-pad instruction, MODE4_DDR takes two serial flash memory clock cycles on the flash memory interface. For a 
four-pad instruction MODE4_DDR takes half a cycle on the serial flash memory interface.
6. It is not recommended to have 0h or FFh as the data learning pattern.
The programmable sequence engine allows you to configure the QuadSPI module according to the serial flash memory connected 
on board. This flexible structure is compatible with new command or protocol changes from different vendors.
79.4.2.2
Flexible read xAHB buffers
To reduce the latency of the reads for AHB masters, the data read from serial flash memory is buffered in flexible AHB buffers. 
There are four such flexible buffers. The size of each of these buffers is configurable with the minimum size being 0 bytes and 
maximum size being the size of the complete buffer instantiated (1024 bytes). The size of buffer 0 ranges from 0 to BUF0IND. The 
size of buffer 1 ranges from BUF0IND to BUF1IND, buffer2 from BUF1IND to BUF2IND and, buffer 3 ranges from BUF2IND to 
the size of the complete buffer (1024 bytes).
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
The controller; however, continues to prefetch the rest of the data in anticipation of a next consecutive request. See Figure 510 
that shows flexible AHB buffers.
BFGENCR[SEQID] points to an index of the LUT. See LUT for details.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4771 / 5251


---
# 페이지 1912

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
Figure 510. Flexible read AHB buffers
79.4.2.3
Abort mechanism during AHB read
Any ongoing read transaction is aborted if a request from the same master arrives for a location other than the location at which 
the transaction is going on. The abort can happen at any point of time.
79.4.2.4
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
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4772 / 5251


---
# 페이지 1913

       
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
Figure 511. QuadSPI HBURST support
 
The software must take care that the prefetch size should never be set less than the minimum data needed by any 
external interface to start processing.
  NOTE  
 
Whenever a core accesses QuadSPI memory with cache enabled, the prefetch size must be configured as equal 
or more than the cache line size; otherwise, FR[AIBSEF] error appears.
  NOTE  
79.4.2.5
LUT
The LUT consists of a number of pre-programmed sequences. Each sequence is basically a sequence of instruction-operand 
pairs, which when executed sequentially, generate a valid serial flash memory transaction. Each sequence can have a maximum 
of 10 instruction-operand pairs. The LUT can hold a maximum of 16 sequences. The figure below shows the basic structure of 
the sequence in the LUT.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4773 / 5251


---
# 페이지 1914

instr(6 bits)
LUT[5..9]
operand (8 bits)
pads (2 bits)
10 instruction-operand pairs 
in one sequence(LUT[0..4])
LUT[10..14]
LUT[75..79]
16 possible 
sequences 
can be 
programmed 
in the 
LUT
LUT
The instructions are executed sequentially until the last instruction or the 
STOP instruction is encountered.
Figure 512. LUT and sequence structure
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
Table 732. Read sequence
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
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4774 / 5251


---
# 페이지 1915

Table 732. Read sequence (continued)
Instruction
Pad
Operand
Comment
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
79.4.2.6
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
79.4.2.7
Flash memory programming
In all NOR Flash devices memory sector to be written needs to be erased first. The programming sequence is then initiated in the 
following way:
1. Program the FRAD and MDAD registers.
2. Program the address related to the command in SFAR (with access attributes programmed in MDAD). If required, write 
the desired value to SFACR[CAS], otherwise write 0 to it. Also, write 1 to SFACR[WA] if the serial flash memory is a 
word addressable flash memory, or write 0 in case serial flash memory is byte addressable
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4775 / 5251


---
# 페이지 1916

3. Program the IPCR register (with access attributes programmed in MDAD). IPCR[SEQID] should point to an index of the 
LUT that has the flash memory program sequence pre-programmed. Write an appropriate value to IPCR[IDATSZ] to 
denote the size of the write in bytes.
4. Check FSM Status (FSMSTAT) register to know status of current transaction. Valid[31] bit should be ‘1’ and domain ID 
[11:8] should match the ID with which SFAR and IPCR were written. Program the TX watermark in TBCT[WMRK] field 
and wait for STAT[1:0] bits to turn ‘01’.
5. Check that the TX buffer is empty. If you need to discard the data present in the TX buffer (SR[TXEDA]) field is set, then 
the TX buffer must be cleared by writing 1 to MCR[CLR_TXF].
6. Provide data for the program command into the circular buffer through the TBDR. Once the TX buffer is written till 
watermark level and SR[TXWA] flag is de-asserted this IP command will be triggered. FSMSTAT[STAT] will get set to 
10.
7. Repeat step 3, depending on the amount of data required, until all of the required data is written to the TBDR. 
SR[TXFULL] can be used to check if the buffer is ready to receive more data. At any time, TBSR[TRCTR] can be read 
to check how many words have been written into the TX buffer.
8. Once the transaction completes FSMSTAT[VLD] bit will set to 0, SR[BUSY] is reset and FR[TFF] is asserted. Please 
refer to section Secure flash programming for more details.
After writing to IPCR[SEQID] , the module starts executing the programmed sequence when QuadSPI SFM is IDLE. The software 
ensures that the correct sequence is programmed into the LUT in accordance with the flash memory connected to the module. 
The data is fetched from the TX buffer. It consists of 256 entries of 32-bit sizes and is organized as a circular FIFO, the read pointer 
for which is incremented after each fetch. When all the data is transmitted, the QuadSPI module returns from the busy state to the 
idle state. However, this is not true for the external device because the internal programming is still ongoing. You may monitor the 
relevant status information available from the serial flash memory device and ensure that the programming is done appropriately.
79.4.2.8
Flash memory read
Host access to the data stored in the external serial flash memory device is performed in two steps. First, the data must be read 
into the internal buffers and in the second step, these internal buffers can be read by the host.
Reading serial flash memory data into the QuadSPImodule internal buffers
A read access to the external serial flash memory device can be triggered in two different ways:
• IP command read: For reading flash memory data into the RX buffer, you must provide the correct sequence ID in 
IPCR[SEQID]. The sequence ID points to a sequence in the LUT. The software needs to ensure that a correct read sequence 
is programmed in the LUT in accordance with the serial flash memory device connected on board. You must program the 
SFAR , SFACR[CAS], and IPCRs. All available read commands supported by the external serial flash memory are possible.
Optionally, it is possible to clear the RX buffer pointer prior to triggering the IP command by writing a 1 to MCR[CLR_RXF]. 
This will invalidate the data currently present in the RX buffer and any new read data will overwrite the old one.
Using these inputs, the complete transaction is built when IPCR[SEQID] is written to and if MDAD checks are passing (based 
on the access attributes while writing SFAR and IPCR). The transaction related to the read access starts when QuadSPI 
is IDLE and FSMSTAT[VLD] bit is 1. The data is fetched for the domain ID that is shown in FSMSTAT[11:8] bits when 
FSMSTAT[STAT] is set to 11 and the requested number of bytes is fetched from the external serial flash memory device into 
the RX buffer. As the read access is triggered by an IP command, the value of both SR[IP_ACC] and SR[BUSY] is set to 1.. 
A count of the number of entries currently in the Rx buffer can be obtained from RBSR[RDBFL].
Communication with the external serial flash memory stops if the specified number of bytes are read (on successful 
completion of the transaction).
 
In case of external DQS strobe based sampling, read data size (IDATSZ or LUT size) must be in multiples of 
8 bytes.
  NOTE  
• AHB command read: For reading flash memory data into the AHB buffer, you must:
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4776 / 5251


---
# 페이지 1917

— Set up a read access by a master to the address range in the system memory map, which the external serial flash 
memory devices are mapped to.
— Write a desired value to SFACR[CAS], if required, or write 0 to the field. 
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
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4777 / 5251


---
# 페이지 1918

         
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
    
Figure 513. QuadSPI memory map
The RX buffer is implemented as FIFO of depth 32 entries of 4 bytes. Its content is accessible in two different address areas, both 
referring to identical data and the same physical memory:
• In the IPS address space in the area associated with RX Buffer Data Register (RBDR0 - RBDR31).
• In the AHB address space in the area associated with AHB RX Data Buffer Register (ARDB0 - ARDB31).Two successive 
entries are accessed with one single 64-bit AHB read operation.
The RX buffer operation can be summarized as follows:
• RBCT[WMRK] determines at which fill level SR[RXWE] is asserted and how many entries are removed from the RX buffer 
on each buffer POP operation.
• SR[RXWE] indicates that the configured number of data entries is available in the RX buffer and RBSR[RDBFL] indicates 
how many valid entries are available in total.
• The first entry (RBDR0 or ARDB0) always corresponds to the first valid entry in the RX buffer.
For details, see RX Buffer Data Register (RBDR0 - RBDR31) and AHB RX Data Buffer Register (ARDB0 - ARDB31).
• Flag-based data read of the RX buffer is performed by polling SR[RXWE]. When it is asserted, the valid entries can be 
read either via the IPS address space (RBDRn) or the AHB address space (ARDBn). A buffer POP operation must be 
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4778 / 5251


---
# 페이지 1919

triggered by the application by writing a 1 to FR[RBDF]. This automatically updates the FIFO to point to the next entry as 
defined by RBCT[WMRK]. For example, if WMRK is set to 3, then the buffer discards 16 bytes of data.
• DMA-controlled data read of the RX buffer is performed by using the DMA module. The application must ensure that the 
DMA controller of the related chip is programmed appropriately, as described in DMA usage.
• DMA-controlled read out is triggered fully automatically by the assertion of SR[RXWE]. The related buffer POP operation 
is also handled completely inside the QuadSPI module. As in the case explained here, accessing the RX buffer content 
either on RBDRn or ARDBn related addresses is equivalent.
• AHB buffer data read via memory-mapped access: This kind of access is performed by reading one of the addresses 
assigned to the external serial flash memory device(s) within the range specified in Table 770. If this is not the case, a 
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
79.4.2.9
AHB write
This module supports a single master AHB write with these burst types — INCR4, INCR8, INCR16, and INCR unspecified 4n bytes 
and single 4n bytes — and these burst types are supported with all Hsizes. An AHB write transaction size can be expressed in 
multiples of 4 bytes, and a single transaction must have a minimum of 4 bytes. In case of HyperRAM ,this limitation of minimum 
4 bytes is not present. Also unspecified INCR and single transactions are supported without the limitation of 4n bytes in case 
of HyperRAM.
The following restrictions apply to the QuadSPI module with respect to AHB write transactions:
• AHB transactions of WRAP* types are not supported. For these unsupported access types, the controller returns an error 
response and does not initiate any flash memory transaction.
• Back to back, fixed address AHB write is not supported.
• Early burst termination is not supported for AHB transactions.
The QuadSPI controller queues back-to-back AHB writes with continuous address and sends them in a single flash memory 
transaction. However, in case the AHB address of a burst is not in continuous addressing sequence to previous write burst, a new 
flash memory transaction is initiated.
Following is the programming sequence for an AHB write:
1. Check that SR[BUSY] is deasserted or is 0 and check that the TX buffer is empty. If there is any residue data present in 
the TX buffer(SR[TXNE]), the buffer must be cleared by writing '1'1 to MCR[CLR_TXF].
2. Based on the type of flash memory device that is used for page programming, AWRCR[PPW_WR_DIS] and 
AWRCR[PPW_RD_DIS] need to be programmed.
The default reset value for both the fields is 0 and allows writing to flash memory device assuming a very low Tpp (page 
program wait time) period. This period is very high for most of the flash memory devices. After any write to a flash memory 
device, the module waits for the write to finish before proceeding further.
This is controlled by the AWRCR[PPW_WR_DIS] and AWRCR[PPW_RD_DIS] field configurations.
3. Program the BFGENCR[SEQID] to point to the LUT where flash memory write sequence is stored.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4779 / 5251


---
# 페이지 1920

4. AHB write master can now enable the transactions to be written to the flash memory. The AHB master must ensure data 
throughout to avoid underflow.
5. When a flash memory write completes and flash memory CS is deasserted, the software must poll SR[BUSY] for the 
deasserted value, which is 0. This indicates that the AHB write is complete. In case an underflow has occurred, flash 
memory CS is deasserted with (SR[TXNE])to know that an AHB write is pending with some residue data in the TX buffer.
6. Whenever flash memory CS is deasserted after an AHB write sequence, FR[PPWF] is set if any of AWRCR[PPW_RD/
WR_DIS] is enabled. FR[PPWF] disables any further flash memory read/write based on AWRCR[PPW_RD]/
AWRCR[WR_DIS]. After FR[PPWF] is set, it returns every incoming AHB transaction with an error response.
7. The software must clear FR[PPWF] to resume AHB transactions after the expiry of Tpp period of flash memory. It can also 
send IPS read command to the flash memory for checking if Tpp is over.
8. The software must ensure that the correct read and write LUT sequences are selected corresponding to the AHB read and 
write transactions. QuadSPI would malfunction if flash memory read sequence is selected during AHB write or vice versa.
 
An AHB error response occurs in case of AHB write if flash is not able to consume data at the rate master is writing 
in TX FIFO and TX FIFO eventually becomes full
  NOTE  
79.4.2.10
Byte ordering of serial flash memory read data
The basic scheme is that the first byte read out of the serial flash memory device, which is addressed by SFAR[SFADR], 
corresponds to RBDR0[31:24] for IP command read. Similarly, to send a single byte it should be positioned in TBDR[0:7]. In 
contrast to that for AHB command read, the bytes are always positioned according to the byte ordering of the AHB bus.
• Byte ordering in individual flash memory mode
The following table provides the byte ordering scheme of how the byte oriented data space of the serial flash memory device 
is mapped into one single 32-bit entry of the RX buffer or the AHB buffer. The table is valid within the following context:
— Flash memory A in individual flash memory mode
— All AHB data read commands with 32-bit access size
Table 733. Byte ordering in individual flash memory mode
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
Table 734. 64-bit read access buffer entry ordering
AHB read data bit position [63:0]
[63:32]
[31:0]
Buffer entry #
Odd (1, 3, 5, ...)
Even (0, 2, 4, ...)
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4780 / 5251


---
# 페이지 1921

79.4.2.11
Normal mode interrupt and DMA requests
The QuadSPI module has different flags that can only generate interrupt requests and one flag that can generate an interrupt as 
well as DMA requests. The following table lists the eight conditions. Note that the flags mentioned in the table are associated with 
the Flag Register (FR).
Table 735. Interrupt and DMA request conditions
Condition
Flag (FR)
DMA
Data learn pattern failure
DLPFF
-
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
In SFP Enabled configurations, program RSER[TBFDE] bit to 1 only when arbitration is won and TBDR access is unlocked 
after checking STATE field of FSMSTAT register. After TBDR programming is completed by DMA, reset this bit otherwise, 
QuadSPI SFM state will remain busy and no further IPS accesses can be served by that Target queue.
• Receive buffer drain interrupt or DMA request
This is derived from FR[RBDF], indicating that the RX buffer of the QuadSPI module has data available from the serial flash 
memory device to be read by the host. It remains set as long as RBSR[RXWE] is configured. Also, RSER[RBDIE] enables 
the related IRQ.
Apart from the IRQ, it is possible to handle the RX buffer drain by using the DMA. If the value of RSER[RBDDE] is 1, a 
DMA request is triggered when the RX buffer contains more than RBCT[WMRK] valid entries. The application must set the 
environment appropriately (for example, the DMA controller) for the DMA transfers.
• Buffer overflow/underrun interrupt request
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4781 / 5251


---
# 페이지 1922

This is a combination of the following fields (all located in the Flag Register (FR) with the related enable bits in the DMA 
Request Select and Enable Register (RSER)):
— TBUF - TX buffer underrun, enabled by TBUIE
— RBOF - RX buffer overflow, enabled by RBOIE
— ABOF - AHB buffer overflow, enabled by ABOIE
— The transmit buffer underrun indicates that an underrun condition in the TX buffer has occurred. It is generated when 
a write instruction is triggered whilst the TX buffer is empty and the value of RSER[TBUIE] is 1.
— The receive buffer overflow indicates that an overflow condition in the RX buffer has occurred. It is generated when the 
RX buffer is full, an additional read transfer attempts to write into the RX buffer, and the value of RSER[RBOIE] is 1.
— The AHB buffer overflow indicates that an overflow condition in the AHB buffer has occurred. It is generated when the 
AHB buffer is full, an additional read transfer attempts to write into the AHB buffer and the value of RSER[ABOIE] is 1.
— The data from the transfers that generated the individual overflow conditions is ignored.
• Serial flash memory command error interrupt request
• Transaction finished interrupt request
The IP command transaction finished IRQ indicates the completion of the current IP command. It is triggered by FR[TFF] and 
is masked by RSER[TFIE].
79.4.2.12
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
79.4.2.13
Address scheme
Earlier, serial flash memories supported only a 24-bit address space, restricting the maximum memory size of the serial flash 
memory to 16 MB. The new memory specification supports two types of 32-bit addressing mode in addition to the legacy 24-bit 
address mode. It also supports segregation of address programmed into Row address and Column address of the flash memory, 
as per the requirement.
Extended address mode
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4782 / 5251


---
# 페이지 1923

In this mode, the legacy 24-bit commands are converted to accept 32-bit address commands. The flash memory needs to be 
configured for the 32-bit address mode. Also, while programming the LUT sequence in QuadSPI for 32-bit mode, the ADDR and 
ADDR_DDR commands should be programmed with 32d as the operand value with SFACR[CAS] programmed to 0. If a flash 
memory needs some bits of the address as its column address, then it must be considered that a total of 12 bits are required by 
the flash memory; however, the number of bits should not exceed 32 because the maximum address supported by QuadSPI is 
32 bits.. Each of the memory vendors have a different way of enabling this mode (see the memory specification from memory 
vendors). For example, the command B7h sent to the Macronix flash memory enables it for the 32-bit address mode.
Extended address register
In this mode, the upper 8 bits of the 32-bit register are provided by the Extended address register in the memory, which provides 
a specific register that is updated according to the address to be accessed. This effectively converts the legacy 24-bit address 
command into 32-bit address commands. The memories greater in size than 16 MB consist of banks of 16 MB each. The 8 bits 
occupied in the extended address register effectively enable a bank. For example, in Spansion memory, when the extended 
address register is updated with a value of 1h, with the help of the 17h command, it opens Bank1 of the memory. The consequent 
24-bit address commands lead to Bank1. The extended address register needs to be updated with the respective value for access 
to other banks. This effectively converts the legacy 24-bit address command into 32-bit address commands.
Separation of address into rows and columns
This mode has been introduced for flash memories that need addresses segregated into rows and columns. The value in 
SFACR[CAS] defines the width of the column address required by a flash memory. The actual address to be provided is derived 
from the incoming address in case of AHB-initiated transactions and the value of SFAR in case of IPS-initiated transactions, if the 
value of SFACR[CAS] is 0. Otherwise, the actual address takes CAS into consideration. If the value of SFACR[CAS] is 3, then bits 
26-3 of the programmed address are sent to the flash memory as its page address. This is in case the flash memory is operating 
in a 24-bit mode and bits 2-0 are sent as its column address. If a flash memory requirement for column address is less than the 
number of pads in which address has to be sent, then QuadSPI appends the remaining bits by 0. You must program the operand 
value in CADDR and CADDR_DDR command accordingly. It must be ensured that the total number of address bits requested by 
flash memory as its page and column address must not be more than 32 bits.
Word addressable mode for flash memory
This mode has been introduced for flash memories, which have a word-addressable memory. This means, each address of the 
flash memory contains one word (two bytes) of data. The value of SFACR [WA] is configured to 1 to enter this mode. QuadSPI 
internally divides the incoming address in the AHB bus or the address in the SFAR to map it to a valid flash memory location. For 
example, if the incoming address is 2004h, the controller re-maps this address to access the flash memory location 1002h. If not 
in this mode, the incoming address 2004h is mapped to flash memory location 2004h.
79.4.3 Module Disable mode
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
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4783 / 5251


---
# 페이지 1924

• There is no current AHB access.
• There is no active DMA request.
• There is no enabled interrupt that is pending.
Certain read or write operations have a different effect when the QuadSPI is in the Module Disable mode. In the Module Disable 
mode, not all of the status and flag bits of the QuadSPI module are updated, and writing to them has no effect. Interrupt and DMA 
request signals cannot be cleared while in the Module Disable mode.
 
It is illegal to issue a new SFM command starting two clock cycles prior to raising the request of entering the Module 
Disable mode until the QuadSPI stays in this mode.
  NOTE  
79.4.4 Leaving Module Disable mode
In the Module Disable mode, the serial flash memory clock and AHB command to the QuadSPI module are switched off.
After the QuadSPI has left this mode and has returned to Normal mode, the execution of the first SFM command is deferred until 
the clock to drive that part of the module related to the serial flash memory device is available. Depending upon the point in time 
when the first SFM command is triggered, the actual execution of the command starts with a delay, respective with the re-enabling 
of the flash memory clock signal.
79.4.5 HyperRAM support
QuadSPI supports HyperRAM memories, and by virtue of this protocol, QuadSPI supports the following functionalities.
• Bidirectional data strobe/read write data strobe (RWDS)
— If QuadSPI is configured to use the HyperRAM mode, the RWDS pad should be pulled down.
• Variable refresh latency
— If the value of MCR[VAR_LAT_EN] is 1, based on the status of RWDS from HyperRAM during the command/address 
phase, QuadSPI includes an additional initial access latency. If RWDS is high, QuadSPI includes twice + 1 the latency 
mentioned in the dummy phase. If RWDS is low, latency mentioned in the dummy phase is not included.
— If the value of MCR[VAR_LAT_EN] is not set, fixed latency mentioned in the dummy phase is included.
• Read data strobe to latch data from HyperRAM
• Programming considerations for HyperRAM support:
— Data masking during the AHB write is enabled when MCR[DQS_OUT_EN] bit is programmed as ’1’.
— It is suggested that while using Hyper RAM program the SPTRCLR[PREFETCH_DIS] bit as ‘1’ so that every time a new 
AHB read transaction starts it reads new data from external memory instead of reading the data already stored in AHB 
buffers. This will ensure that the data read back after an AHB write is not a stale data.
— AHB write doesn’t supports wrap transactions (WRAP4, WRAP8, WRAP16) even with HyperRAM.
— If there is multiple switching between AHB read and write transactions then software should program 
AWRCR[AWTRGLVL] cautiously. It should ensure that during AHB write the data written to memory is more than the 
AWRCR[AWTRGLVL] programmed before switching over to AHB read transactions. This will ensure that IP is not left 
waiting for sufficient write data to be collected.
79.5 Initialization/application information
This section provides the initialization and application information of the QuadSPI module.
79.5.1 Power up and reset
The serial flash memory devices connected to the QuadSPI module might require special voltage characteristics of their inputs 
during power up or reset. The application must ensure this.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4784 / 5251


---
# 페이지 1925

 
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
79.5.2 Available status/flag information
This section provides an overview of the different flags and statuses available, and their interdependencies for different use cases. 
The SR and FR are the related registers.
79.5.2.1
IP commands
See IP Configuration Register (IPCR) for additional details not explicitly covered in this paragraph.
• IP commands—normal operation
Writing to IPCR[SEQID] triggers the execution of a new IP command. Given that this is a legal command, SR[IPACC] and 
SR[BUSY] are asserted simultaneously, immediately after the execution starts.
After the instruction on the serial flash memory device is complete, these field deassert and FR[TFF] is configured.
• IP commands—error situations
See Overview_of_Error_Flags for details.
79.5.2.2
AHB commands
See the "Reading serial flash memory data into the QuadSPI module internal buffers" topic in theFlash Memory Read section 
for details.
• AHB commands—normal operation
Memory-mapped read access to a serial flash memory address not contained in the AHB buffer triggers the execution of an 
AHB command. Given that this is a legal command, SR[AHB_ACC] and SR[BUSY] are asserted simultaneously, immediately 
after the execution starts. After the instruction on the serial flash memory device is complete, these fields are deasserted.
• IP commands—error situations
See Overview of FR error flags for details.
79.5.2.3
SFM commands
An SFM command consists of an instruction code and all other parameters (for example, size or mode bytes) needed for that 
specific instruction code. Triggering a command either initiates a transaction on the external serial flash memory or results in an 
error. See Table 736 for details on errors.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4785 / 5251


---
# 페이지 1926

79.5.2.4
Overview of error flags
The following table provides an overview of the different error flags in the FR and additional error-related details.
Table 736. Overview of FR error flags
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
Miscellaneous error flag
DLPFF
Flash memory transaction continues until 
it finishes
Set when the DATA_LEARN 
instruction is encountered in a 
sequence but no sampling point is 
found for the data learning pattern.
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
• Write attempt to RBCT register
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
79.5.2.5
IP bus and AHB access command collisions
There are following flags related to this topic: FR[IPIEF]. See the "Reading serial flash memory data into the QuadSPI module 
internal buffers" topic of the Flash Memory read section for a description of the flags.
79.5.3 Flash memory device selection
Regardless of the SFM command (IP or AHB), the access mode is selected by specifying the 32-bit address value for the following 
SFM command.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4786 / 5251


---
# 페이지 1927

For IP commands, the access mode is selected with the address programmed into the SFAR register. See Serial Flash Address 
Register (SFAR) for details.
For AHB commands, the access mode is determined by the memory-mapped address. See AMBA Bus Register Memory Map 
for details.
79.5.4 DMA usage
For a complete description of the DMA module, see the related DMA Controller chapter. This section only provides QuadSPI-
specific DMA usage details.
79.5.4.1
DMA usage in normal mode
79.5.4.1.1
Bandwidth considerations
Careful consideration of the throughput rate of the entire chain (serial flash memory -> AHB bus / IP bus -> DMA controller) 
involved in the read/write data process is essential for a proper operation. Such analysis must take into account not only the data 
rate provided by the serial flash memory but also the data rate of the AHB bus and the performance of the DMA controller in 
reading/writing data from/to the RX/TX buffer.
Two figures must match for a proper operation, which means that the data rate provided by the serial flash memory device must 
not exceed the average RX buffer readout data rate. Otherwise, the longer this state persists, it results into an RX buffer overflow. 
Similarly, the data consumed by the serial flash memory device must not exceed the average TX buffer fill rate. If this persists, it 
leads to an underrun.
AHB bus side (data read)
The total number of bus cycles for each DMA minor loop completion is added from the following components:
The following table provides certain examples for typical use cases:
Case 1: DMA needs to read 4 bytes from SRAM and provide to QuadSPI. It costs total four bus clock cycles. Then, DMA 
handshake adds additional six bus clock cycles, resulting in a total of [6 + 4 * (32/4) = 38] bus clock cycles. 
Table 737. Access duration examples for bus clock side
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
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4787 / 5251


---
# 페이지 1928

Table 738. Access duration examples for bus clock side
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
command and address not considered): , two cycles for the Octal DDR mode in the individual flash memory mode, eight 
cycles for quad mode (SDR) instructions in individual flash memory mode, and so on.
• Overhead because of clock domain crossing: one cycle
The following table lists the number of clock cycles required to read the data from the serial flash memory corresponding to the 
different settings of RBCT[WMRK]:
Table 739. Access duration examples for serial flash memory side
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
11
48
96
48
~1200ns
~600ns
1. DMA loop refers to one minor loop completion that is equivalent to one major loop iteration.
2. Individual flash memory mode
 
The table figure represents an ideal scenario; actual performance depends on how the chip integrates with DMA 
and QuadSPI modules.
  NOTE  
A complementary example is when the watermark is set to be too high. In such a case, the time taken by the DMA to read out the 
RX buffer entries should be lesser than the time taken by the controller to push in the remaining entries in the buffer.
IPS bus side (data write)
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4788 / 5251


---
# 페이지 1929

The total number of bus cycles for each DMA minor loop completion are added from the following components:
• Overhead for each minor loop, given by DMA controller: assume 10 cycles
• Overhead because to clock domain crossing: assume two cycles
• Number of bus clock cycles required for 16 bytes (128-bit write size): assume four cycles (read/write sequence of DMA 
controller)
Note that the size of the minor loop is determined by the size of TBCT[WMRK]; therefore, the overhead specified above distributes 
among (TBCT[WMRK]+1) write accesses of 32-bit each.
The following table provides some examples for typical use cases:
Table 740. Access duration examples for bus clock side
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
1. DMA loop refers to one minor loop completion that is equivalent to one.
 
The table figure represents an ideal scenario; actual performance depends on how the chip integrates with DMA 
and QuadSPI modules.
  NOTE  
Serial flash memory device side (data write) 
The number of serial flash memory cycles can be determined in the following way:
• Number of serial flash memory clock cycles required to write 16 bytes, corresponding to four TX buffer entry (setup of 
command and address not considered): Eight cycles for Octal DDR mode instructions in individual flash memory mode, 32 
cycles for quad SDR writes in individual flash memory mode.
• Overhead due to clock domain crossing: one cycle
The following table lists the number of clock cycles required to read the data from the serial flash memory corresponding to the 
different settings of TBCT[WMRK]:
Table 741. Access duration examples for serial flash memory side
TBCT[WMRK] 
setting
Num bytes 
per DMA 
loop 1
Num SCKFx
Time duration for consuming 
data at flash memory 
interface 100 MHz SCKFx 
(10 ns period)2
Time for FIFO to get empty3
IFM 4 quad
IFM octal 
DDR
IFM quad
IFM octal 
DDR
IFM quad
IFM octal 
DDR
3
16
32
8
320ns
80ns
2240ns
560ns
7
32
64
16
640ns
160ns
1920ns
480ns
1. DMA loop refers to one minor loop completion that is equivalent to one major loop iteration.
2. Not all flash memory devices support writes at 100 MH. See the flash memory data sheet for the actual page program 
frequency supported.
3. The assumption for these timings is that the TX Fifo is full when the transaction is initiated
4. Individual flash memory mode
 
The tables mentioned above are only examples which must be correlated with the DMA in the system.
  NOTE  
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4789 / 5251


---
# 페이지 1930

Considering the examples provided in the two tables above for TX FIFO, it is evident that depending on the relationship between 
the bus clock and serial flash memory clock frequencies, there are settings possible where the serial flash memory consumes 
data faster than the IPS bus can write data in TX buffer. In these cases, a TX buffer underrun situation occurs. To avoid TX buffer 
underrun, the data transaction size should be large enough.
79.5.5 Flash memory devices address mapping
QuadSPI is configured in Single mode for the supported flash memory port A
The sizes of the flash memory devices are mapped with the system memory space based on the configurations of the 
following registers:
• SFA1AD
• SFA2AD
The total memory region for the flash memory devices is mapped between QuadSPI_AMBA_BASE and TOP_ADDR_MEMA2 
such that the corresponding CS is asserted based on SFA1AD and SFA2AD register configurations.
79.5.5.1
Single mode
For single-die flash memories, you must write the same value to SFA2AD register that you write to the SFA1AD register.
Following is a programming example for single mode single-die flash memory:
• QuadSPI_AMBA_BASE - 1000_0000h
• SFA1AD[TPADA1] - 2000_0000h
• SFA2AD[TPADA2] - 2000_0000h
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
Figure 514. Memory map for Single mode
79.6 Byte ordering – endianness
The following topics show the byte ordering in 64-bit LE configuration for AHB buffer and 32-bit LE for TX/RX buffer.
79.6.1 Programming flash memory data
CPU writes instructions to the TBDR register, such as:
• Write TBDR: 4_03_02_01h
• Write TBDR: 8_07_06_05h
The following table shows the content against each TX buffer entry.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4790 / 5251


---
# 페이지 1931

Table 742. Example of QuadSPI TX buffer
TX buffer entry
Content
0
4_03_02_01h
1
8_07_06_05h
Programming the TX buffer into the external serial flash memory device results in the following byte order to be sent to the serial 
flash memory:
• 01...02...03...04...05...06...07...08
79.6.2 Reading flash memory data into the RX buffer
Reading the content from the same address provides the following sequence of bytes, identical to the write case:
• 01...02...03...04...05...06...07...08
The following table shows the content against each TX buffer entry.
Table 743. Resulting RX buffer content
RX buffer entry
Content
0
4_03_02_01h
1
8_07_06_05h
79.6.2.1
Readout of the RX buffer through RBDRn
The RX buffer content appears at CPU read access through the peripheral bus interface in the following order:
• Read RBDR0: 4_03_02_01h
• Read RBDR1: 8_07_06_05h
79.6.2.2
Readout of the RX buffer through ARDBn
The RX buffer content appears at read access on the AMBA AHB interface at the QuadSPI module boundary:
• 32-bit access: Read ARDB0: 4_03_02_01h
• 32-bit access: Read ARDB1: 8_07_06_05h
• 64-bit access: Read ARDB0: 8_07_06_05_04_03_02_01h
79.6.3 Reading flash memory data into the AHB buffer
Reading the content from the same address as it was written to provides the following sequence of bytes, identical to the 
write case:
• 01...02...03...04...05...06...07...08
The following table shows the content against each TX buffer entry.
Table 744. Resulting AHB buffer content
AHB buffer entry
Content
0
8_07_06_05_04_03_02_01h
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4791 / 5251


---
# 페이지 1932

79.6.3.1
Readout of the AHB buffer through memory-mapped read
The AHB buffer content appears at read access on the AMBA AHB interface at the QuadSPI module boundary:
• 32-bit read access: 4_03_02_01h
• 32-bit read access: 8_07_06_05h
• 64-bit read access: 8_07_06_05_04_03_02_01h
79.7 Driving flash memory control signals in single and dual modes
In single and dual modes, the serial flash memory devices that can connect to the QuadSPI module expect additional control 
signals on the inputs, which are connected to IOFA[3], IOFA[2] in the quad mode. For easy interfacing, the outputs IOFA[3:2] for 
flash memory A are driven to the logic state given by the configuration fields MCR[ISD3FA], MCR[ISD2FA].
These outputs are driven all the time to the logic level programmed in the MCR except the time when quad commands of the serial 
flash memory are executed. See the specifications of the related serial flash memory device for details about the inactive level.
79.8 Serial flash memory devices
Several different vendors make flash memory devices with a QuadSPI interface. At present, there is no set standard for the 
QuadSPI instruction set. The most common commands currently have the same instruction code for all vendors; however, some 
commands are unique to specific vendors. Some of the example sequences are provided in the following sections.
79.8.1 Example sequences
This section provides the example sequences of the QuadSPI module.
Table 745. Exit 4 x I/O read enhance performance mode (XIP) (Macronix) and read status
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
2h
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
79.8.1.1
Read command (hyperflash memory/HyperRAM)
This section provides the read command sequences (hyperflash memory/HyperRAM) of the QuadSPI module.
Table 746. Read command (hyperflash memory/HyperRAM)
Instruction
Pad
Operand
Comment
CMD_DDR
3h
A0h
Read command with 
continuous burst type
ADDR_DDR
3h
18h
24-bit row address
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4792 / 5251


---
# 페이지 1933

Table 746. Read command (hyperflash memory/HyperRAM) (continued)
CADDR_DDR
3h
10h
16-bit column address with 
lower 3 bits valid and rest 0
Dummy
3h
0hF
15 dummy cycles
READ_DDR
3h
4h
32-bit data read on 8 pads
STOP
3h
0h
Stop, instruction over
Hyperflash memory/HyperRAM is a word addressable flash memory. This means that each address accesses a word-wide 
(two-byte) data value. The software should ensure that when Hyperflash memory/HyperRAM is connected to the controller, the 
value of SFACR[WA] must be 1. With this value, the controller remaps a byte addressable access to a word addressable access.
79.8.1.2
Read status register (hyperflash memory/HyperRAM)
This section provides details related to the read status register of the QuadSPI module.
Table 747. Read status register (hyperflash memory/HyperRAM)
Instruction
Instruction sequence
Pad
Operand
Description
CMD_DDR
Read Pre Command
3h
0h
Write command with 
wrapped burst type
ADDR_DDR
3h
18h
24-bit row 
address (0000AAh)
CADDR_DDR
3h
10h
16-bit column address 
with lower 3 bits 
valid and rest 0(0005h) 
treated as command
CMD_DDR
3h
0h
Write command with 
wrapped burst type
CMD_DDR
3h
70h
Write data to be sent 
to flash memory as pre-
command
CMD_DDR
Command phase 
(fourth/final chip 
select phase)
3h
A0h
Read command with 
continuous burst type
ADDR_DDR
3h
18h
24-bit row address
CADDR_DDR
3h
10h
16-bit column address 
with lower 3 bits as valid 
and rest 0
DUMMY
3h
0hF
15 dummy cycles
READ_DDR
3h
4h
32-bit data read on 
8 pads
STOP
3h
0h
Stop, instruction over
79.8.1.3
Word program (hyperflash memory/HyperRAM)
This section provides the word program (hyperflash memory/HyperRAM) of the QuadSPI module.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4793 / 5251


---
# 페이지 1934

Table 748. Word program (hyperflash memory/HyperRAM)
Instruction
Instruction sequence
Pad
Operand
Description
CMD_DDR
Unlock sequence 1 (first 
chip select phase)
3h
0h
Write command with 
wrapped burst type
CMD_DDR
3h
0h
8-bit address 00h 
treated as command
CMD_DDR
3h
0h
8-bit address 00h 
treated as command
CMD_DDR
3h
AAh
8-bit address AAh 
treated as command
CADDR_DDR
3h
10h
16-bit column address 
with lower 3 bits 
valid and rest 0(0005h) 
treated as command
CMD_DDR
3h
0h
Write command with 
wrapped burst type
CMD_DDR
3h
AAh
Write data to be sent 
to flash memory as pre-
command
CMD_DDR
Unlock sequence 
2 (second chip 
select phase)
3h
0h
Write command with 
wrapped burst type
CMD_DDR
3h
0h
8-bit address 00h 
treated as command
CMD_DDR
3h
0h
8-bit address 00h 
treated as command
CMD_DDR
3h
55h
8-bit address 55h 
treated as command
CADDR_DDR
3h
10h
16-bit column address 
with lower 3-bits valid 
and rest 0(0002h) 
treated as command
CMD_DDR
3h
0h
Write command with 
wrapped burst type
CMD_DDR
3h
55h
Write data to be sent 
to flash memory as pre-
command
CMD_DDR
Program setup phase 
(third chip select phase)
3h
0h
Write command with 
wrapped burst type
CMD_DDR
3h
0h
8-bit address 00h 
treated as command
CMD_DDR
3h
0h
8-bit address 00h 
treated as command
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4794 / 5251


---
# 페이지 1935

Table 748. Word program (hyperflash memory/HyperRAM) (continued)
CMD_DDR
3h
AAh
8-bit address AAh 
treated as command
CADDR_DDR
3h
10h
16-bit column address 
with lower 3 bits 
valid and rest 0(0005h) 
treated as command
CMD_DDR
3h
0h
Write command with 
wrapped burst type
CMD_DDR
3h
A0h
Write data to be sent 
to flash memory as pre-
command
CMD_DDR
Command phase 
(fourth/final chip 
select phase)
3h
0h
Write command with 
wrapped burst type
ADDR_DDR
3h
18h
24-bit row address
CADDR_DDR
3h
10h
16-bit column address 
with lower 3 bits as valid 
and rest as 0
WRITE_DDR
3h
2h
2-byte data written on 8 
pads (D1D2)
STOP
3h
0h
Stop, instruction over
79.8.1.4
Fast read sequence (Macronix/Numonyx/Spansion/Winbond)
The following table shows the fast read sequence for Macronix/Numonyx/Spansion/Winbond flash memories.
Table 749. Fast read sequence
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
79.8.1.5
Fast dual I/O DT read sequence (Macronix)
The following table shows the fast dual I/O DT read sequence for Macronix flash memories.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4795 / 5251


---
# 페이지 1936

Table 750. Fast dual I/O DT read sequence
Instruction
Pad
Operand
Description
CMD
0h
BDh
Fast dual I/O DT read command = BDh
ADDR_DDR
1h
18h
24 address bits to be sent on two pads in the 
DDR mode
MODE4_DDR
1h
0h
P2=P0 or P3=P1 is necessary. See the Macronix 
data sheet for details. One clock cycle for mode.
DUMMY
1h
6h
Six dummy cycles
READ_DDR
1h
4h
Read 32 bits on two pads in the DDR mode
JMP_ON_CS
0h
0h
Jump to instruction 0 (CMD)
 
If DLL is disabled then JMP_ON_CS or STOP instruction can be used else only STOP instruction can be used.
  NOTE  
79.8.1.6
Fast read quad output (Winbond)
The following table shows the fast read quad output sequence for Winbond memories
Table 751. Fast read quad output sequence
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
2h
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
79.8.1.7
4 x I/O read enhance performance mode (XIP) (Macronix)
The following table shows the 4 x I/O read enhance performance mode for Macronix flash memories. The enhanced performance 
mode is also known as XIP mode.
Table 752. Fast read quad output sequence
Instruction
Pad
Operand
Description
CMD
0h
EBh
4xI/O read command = EBh
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4796 / 5251


---
# 페이지 1937

Table 752. Fast read quad output sequence (continued)
Instruction
Pad
Operand
Description
ADDR
2h
18h
24 address bits to be sent on four pads
MODE
2h
A5h
Two mode cycles
DUMMY
2h
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
79.8.1.8
Dual command page program (Numonyx)
The following table shows the dual command page program sequence for Numonyx flash memories.
Table 753. Dual command page program sequence
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
STOP
0h
0h
Stop, instruction over
79.8.1.9
Sector erase (Macronix/Numonyx/Spansion)
The following table shows the Sector erase sequence for the Macronix/Numonyx/Spansion flash memories.
Table 754. Sector erase sequence
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
79.8.1.10
Read status register (Macronix/Numonyx/Spansion/Winbond)
The following table shows the read status register sequence for Macronix/Numonyx/Spansion/Winbond flash memories.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4797 / 5251


---
# 페이지 1938

Table 755. Read status register sequence
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
79.8.1.11
Data learn instruction sequence
The following table shows the data learn sequence for 4 I/O flash memory.
Table 756. Data learn instruction sequence (4 I/O)
Instruction
Pad
Operand
Description
CMD
0h
6Bh
Fast read quad command = 
6Bh
ADDR_DDR
2h
18h
24 address bits in the DDR 
mode to be sent on four pads
DUMMY
2h
8h
8-cycle dummy
DATA_LEARN
2h
1h
1-byte data learn
READ_DDR
2h
6h
Read 6 bytes in 4 pads1
JMP_ON_CS
0h
0h
Jump to Inst 0 (CMD)
1. Data learn instruction needs to be followed by a read DDR instruction of minimum 6 bytes in case of 4 I/O mode.
 
If DLL is disabled then JMP_ON_CS or STOP instruction can be used else only STOP instruction can be used.
  NOTE  
The following table shows the data learn sequence for 8 I/O (hyperflash memory) flash memory.
Table 757. Data learn instruction sequence (8 I/O)
Instruction
Pad
Operand
Description
CMD_DDR
3h
AOh
Read command for 
hyperflash memory
ADDR_DDR
3h
18h
24-bit row address1
CADDR_DDR
3h
10h
16-bit column address
DUMMY
3h
Fh
15-cycle dummy
DATA_LEARN
3h
1h
1-byte data learn
READ_DDR
3h
Ch
Read 12 bytes in 8 pads2
STOP
3h
0h
Stop, instruction over
1. The address needs to be aligned, which means, no latency should be there between the RWDS edges.
2. The data learn instruction needs to be followed by a read DDR instruction of minimum 12 bytes in case of 8 I/O mode.
The following table shows the data learn sequence for 4 I/O flash memory.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4798 / 5251


---
# 페이지 1939

Table 758. Data learn instruction sequence (4 I/O)
Instruction
Pad
Operand
Description
CMD
0h
6Bh
Fast read quad command = 
6Bh
ADDR_DDR
2h
18h
24 address bits in DDR mode 
to be sent on four pads
DUMMY
2h
8h
8 dummy cycles
DATA_LEARN
2h
1h
1-byte data learn
READ_DDR
2h
6h
Read 6 bytes in 4 pads
JMP_ON_CS
0h
0h
Jump to Inst 0 (CMD)
 
If DLL is disabled then JMP_ON_CS or STOP instruction can be used else only STOP instruction can be used.
  NOTE  
The following table shows the data learn sequence for 8 I/O (Hyperflash) flash memory.
Table 759. Data learn instruction sequence (8 I/O)
Instruction
Pad
Operand
Description
CMD_DDR
3h
AOh
Read command for 
hyperflash memory
ADDR_DDR
3h
18h
24-bit row address1
CADDR_DDR
3h
10h
16-bit column address
DUMMY
3h
Fh
15-cycle dummy
DATA_LEARN
3h
1h
1-byte data learn
READ_DDR
3h
8h
Read 8 bytes in 8 pads
STOP
3h
0h
Stop, instruction over
1. The address needs to be aligned, which means, no latency should be there between the RWDS edges.
 
If DLL is disabled then JMP_ON_CS or STOP instruction can be used else only STOP instruction can be used.
  NOTE  
79.9 Sampling of serial flash memory input data
79.9.1 Basic description
QuadSPI is used to read data from the serial flash memory device. Depending on the actual implementation, there is a delay 
between the internal clocking in the QuadSPI module and the external serial flash memory device. See the following figure for an 
overview of this scheme.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4799 / 5251


---
# 페이지 1940

QUADSPI
Clock Gen
Sampling
Serial flash memory
Clock
Data 
Out
SCK - Serial Flash Memory Clock
SI_IO[0:7] - Serial Flash Memory Data
1
5
2
4
3
Figure 515. Serial flash memory sampling clock overview
The rising edge of the internal reference clock is taken as timing reference for the data output of the serial flash memory. After a 
time of ttotal_delay the data arrives at the internal sampling stage of the QuadSPI module. Considering the figure provided here, the 
following parts of the delay chain contribute to ttotal_delay:
• Output delay of the serial flash memory clock output of the device containing the QuadSPI module
• Wire delay of application/PCB from the device containing the QuadSPI module to the external serial flash memory device
• Clock to data out delay of the external serial flash memory device, including input and output delays
• Wire delay of application/PCB from the external serial flash memory device to the device containing the QuadSPI module
• Device delay corresponding to the input data
 
The ttotal_delay is specific to the characteristics of the actual implementation.
  NOTE  
79.9.2 DQS sampling method
79.9.2.1
Basic description
In the DQS mode, the data strobe signal (DQS/RWDS) is used to sample the read data. Here, both DQS and the data sent by the 
flash memory move in the same direction; therefore, it is relatively easier to achieve at higher frequencies.
When using DQS for SDR reads, QuadSPI internally samples the incoming data on the rising edge of the strobe signal.
The next figure shows the sampling read data in the SDR mode using the DQS.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4800 / 5251


---
# 페이지 1941

Internal Ref 
clock
SCK
Data Strobe Signal
  
Data
internal reference for serial flash memory data sampling
Data sampled on only rising edge of Data Strobe Signal
Figure 516. Data strobe functionality in SDR mode for read operation.
 
Consider "Data Strobe Signal" as "Data Strobe Signal driven by memory" and "Data" as "Data from memory".
  NOTE  
 
Refer to the Datasheet for specific timing waveforms of QuadSPI
  NOTE  
When using the DQS for DDR reads, QuadSPI internally samples the incoming data on both the edges of the strobe signal. See 
the next figure for details.
Internal Ref 
clock
SCK
       
Data Strobe Signal     
       
            
     
       
Data     
       
internal reference for serial flash memory data sampling     
       
Data sampled on both the edges of Data Strobe Signal     
Figure 517. Data strobe functionality in DDR mode for read operation.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4801 / 5251


---
# 페이지 1942

 
Consider "Data Strobe Signal" as "Data Strobe Signal driven by memory" and "Data" as "Data from memory".
  NOTE  
 
For Specific details - Refer to the Data Sheet specification of QuadSPI module.
  NOTE  
79.9.2.2
External DQS
In serial flash memories supporting DQS, the data strobe signal is an output from the flash memory device that indicates when 
data is being transferred from the flash memory to the host controller. The data is then captured by the controller on:
• Only one edge (either rising or falling edge) of DQS signal in the SDR mode
• Both rising/falling edges of the DQS signal in the DDR mode
This can be enabled by programming MCR[DQS_FA_SEL] = "11" for flash memory A. This mode supports the 
following configuration:
• Both high/low frequency delay chain manual programming using DLLCRA[SLV_DLY_COARSE] 
and DLLCRA[SLV_FLINE_OFFSET]
• DLL-assisted sampling only using and DLLCRB[DLLEN]
• DLL-assisted auto data learning using and DLLCRB[DLLEN] along with MCR{DLPEN]
• should be disabled as DLL is used
 
This mode may not be available on the chip. See the "Supported read modes" section in the chip-specific QuadSPI 
information for the read modes that this chip supports.
  NOTE  
79.9.2.3
Dummy Pad loopback
The internal clock is loop-backed from the dummy internal pad to compensate data pad delays. This can be enabled by configuring 
the value of MCR[DQS_FA_SEL] as "01" for flash memory A. This mode can be used with the following configuration:
• High/low frequency delay chain manual programming in bypass mode using DLLCRA[SLV_DLY_COARSE] 
and DLLCR[FREQEN].
• DLL-assisted sampling only using DLLCRA[DLLEN]
 
Refer to DS or "Chip-specific section" of QSPI for Fixed sampling Tap specific settings/details with out without DLL 
(in bypass mode)
  NOTE  
• DLL-assisted auto data learning using DLLCRA[DLLEN] and along with MCR[DLPEN]
 
Refer to Auto-DataLearning (4x Sampling method) section with DLL for further details
  NOTE  
 
This mode may not be available on the chip. See the "Supported read modes" section in the chip-specific QuadSPI 
information for the read modes that this chip supports.
  NOTE  
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4802 / 5251


---
# 페이지 1943

79.10 Data learning
79.10.1 Basic description
Data learning is used to manage varying data valid windows from the flash memory as well as any variations in the chip based 
on PVT conditions in the DDR mode. QuadSPI provides this feature via the DATA_LEARN instruction for all flash memories, 
irrespective of whether the flash memory supports it. The DATA_LEARN instruction accepts an operand that defines the number 
of bits of the known pattern for which the data learning has to be done. The known pattern is provided in the DLPR register.
QuadSPI supports the following data learning:
• QuadSPI supports data learning with DLL enabled only
The following sections explain data learning in detail.
79.10.2 DQS sampling method
The semi-automatic data learning is supported in the DQS sampling method. To start data learning:
1. Configure a known pattern in the Data Learn register inside flash memories that support data learning. The pattern 
should be selected to have multiple low and high transitions in the data bus.
 
Certain flash memories provide data learning as a feature for DDR data reads.
  NOTE  
2. Set up a QuadSPI DDR data read sequence, inserting a DATA_LEARN instruction before the READ_DDR instruction. 
The flash memory returns the data learning pattern in between dummy cycles in every read command. Each I/O gives 
the same DLP value for every clock edge.
 
For flash memories that do not support data learning, configure a known location in flash memory with a known 
pattern. The pattern should not have 0h or FFh included. The pattern should be selected to have multiple low and 
high transitions in the data bus. Set up a QuadSPI DDR data read sequence, inserting a DATA_LEARN instruction. 
The address in the SFAR register should point to the known location within the pattern. Configure the known pattern 
in DLPR[DLPV]. See Programming the data learning pattern in flash memory for details on how the data has to be 
ordered in memory for correct operation.
  NOTE  
3. Select a sampling point. See chip-specific QuadSPI information for selection of the sampling point.
4. Initiate the read via a peripheral transaction.
5. QuadSPI reads the data from the flash memory. It then encounters the DATA_LEARN instruction and samples the 
incoming data on both edges (rising and falling) of the DQS.
 
If the data from the flash memory does not match the data learning pattern, the FR[DLPFF] flag is set. The QuadSPI 
module reports no sampling point automatically.
  NOTE  
6. Repeat steps 2-7 with varying VT conditions for a particular process until FR[DLPFF] is set. The sampling points where 
no FR[DLPFF] is set signify a valid setting.
In the case of multiple valid settings, the software should select the middle point. The sampling point should be fixed within the 
above selected point for the next READ transactions.
 
Ensure that QuadSPI is not accessed during calibration.
  NOTE  
This feature might be used to auto-calibrate the sampling point for DDR reads, and auto-calibration might be triggered at fixed 
intervals, or depending on a change in PVT conditions.In case the sampling point needs to be changed based on initiating options 
(such as, DLL lock status, time period, or software forced interrupt), data learn instruction has to be re-initiated.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4803 / 5251


---
# 페이지 1944

The following figure shows data learning in DQS mode.
Pre-programmed
location read
‘DATA LEARN’ pattern
read
Flash memory
Flexible instruction set sequence given to flash memory
internal reference for serial flash memory data sampling
lnternal Ref clock
SCK
Data Strobe Signal*
Data sampled on both the
edges of Data Strobe Signal
Sampling circuit for DQS mode
Data
@DQS clock
@DQS inverted clock
QSPI_FR[DLPFF] is set
Known pattern
comparator
Sampled pattern
No Match
INSTR
ADDR
MODE
DATA_LEARN
Figure 518. Data learning with DQS sampling method
 
This mode might not be available on the chip. See the chip-specific QuadSPI information for the read modes that 
this chip supports.
  NOTE  
79.10.3 Programming the data learning pattern in flash memory
Example scenario: If the value of DLPR[DLPV] is 43h, QuadSPI controller tries to match the sequence of bits sent on selected data 
lines with the pattern in DLPR[DLPV]. The following table shows the data programmed in flash memory with endianness taken 
into consideration.
Table 760. Programming the data learning pattern in flash memory
Single Pad
Double Pad
Quad Pad
Octal Pad
DLPR IO1 pattern
0x349A
0x349A
0x3514
0x349A
DLPR IO3 pattern
NA
NA
0x349A
0x3514
Flash Pattern
0x2C59
0xF04CC226
0x0DF02D0D
0x00FFF020
0xF708f700
0xF70000FF
0x00FF0008
0x0000FFFF
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4804 / 5251


---
# 페이지 1945

79.11 DLL and delay chain usage
The DLL is a general-purpose, dynamically adaptive clock delay module. It provides the ability to select a quantized delay (in 
fractions of the clock period) regardless of on-chip variations such as process, voltage, and temperature (PVT). The DLL is suitable 
for applications where accurate delay adjustment is required, such as in case of DDR interfaces.
DLL working concept 
The DLL control loop consists of a counter, reference delay line, and phase detector which operate on the ref_clock reference 
clock input. The reference clock (clk_ref) is fed into the reference delay line. After reset, a single delay tap is selected. A phase 
detector is used to detect the condition where a half shift has occurred. In addition to this, signals are generated to either increment 
or decrement the counter, which controls the delay line (if the half-phase detect condition is not met). Any changes in the delay of 
the individual elements of the delay chain (because of PVT) automatically cause the phase detector logic to determine if a change 
in the counter value is required. After the half-phase shift is detected, an internal lock signal is generated, and after a lock event 
occurs, the slave delay chain is ready to be updated based on a triggering event.
Slave delay chain programming sequence—
Following is the programming sequence for DLL bypass mode.
1. Program DLLCRA[SLV_EN]=1, DLLCRA[SLV_DLL_BYPASS]=1, and DLLCRA[SLAVE_AUTO_UPDT]=0.
2. Program the following fields to provide the desired DQS delay for sampling: DLLCRA[SLV_FINE_OFFSET], 
DLLCRA[SLV_DLY_COARSE], and DLLCR[FREQEN]. See the chip-specific QuadSPI information for the supported 
programming settings.
3. Program DLLCRA[SLV_UPD]=1 to load these values in the slave delay chain.
4. Check the slave delay chain update status by polling DLLSR[SLVA_LOCK]=1 and clear DLLCRA[SLV_UPD] after 
confirming the update state.
Following is the programming sequence for DLL auto update mode.
1. Program DLLCRA[SLV_EN]=1, DLLCRA[SLV_DLL_BYPASS]=0, and DLLCRA[SLAVE_AUTO_UPDT]=1.
2. Program the DLL configuration by using DLLCRA[DLL_REFCNTR] and DLLCRA[DLLRES]. See the chip-specific QuadSPI 
information for the supported DLL configuration settings.
3. Program the slave settings to delay DQS by using these fields: DLLCRA[SLV_FINE_OFFSET], 
DLLCRA[SLV_DLY_OFFSET], and DLLCR[FREQEN]. See the chip-specific QuadSPI information for the 
supported settings.
4. If offset delay needs to be updated on the slave chain, program DLLCRA[SLV_UPD]=1.
5. Enable DLL by programming DLLCRA[DLLEN]=1 and reset DLLCRA[SLV_UPD]=0. Slave delay chain is updated 
automatically and can be checked by polling DLLSR[SLVA_LOCK]==1
79.12 Secure flash protection
This secure flash module enforces access control policies based on the MGID, privilege and secure attributes of the IPS 
transactions. All accesses throughout the flash device need to be monitored to determine the validity of all accesses. If transaction 
from a given master has appropriate access rights, it is forwarded to flash, else the access is denied, and an error is generated.
There are two level of checks present in this module, based on MDAD and FRAD descriptors programmed. First level checks the 
input transactions based on secure attribute and MGID associated with that transaction which are checked according to MDAD. 
Second level check selects the appropriate FRAD based on address range of transaction. And each FRAD allows the transaction 
to pass through only when secure, privilege and other MGID related attributes are matching. Else the transaction is not forwarded 
and IPS bus error/interrupt is generated. Flash regions can be programmed to cover the entire address space to provide a default 
set of access permissions. For flash read transactions only first level of check is enabled.
Software can bypass both or anyone of these checks by writing to MGC[GVLDFRAD], MGC[GVLDMDAD] and MGC[GVLD] fields.
The IPS masters should write on QuadSPI register (SFAR, IPCR and TBDR) addresses for generating transfers to flash. SFP 
block monitors these IPS transfers and checks if the write is being done on SFAR or IPCR registers and forwards them for MDAD 
and FRAD checks. If the transaction passes both checks then it is passed through to QuadSPI register else bus error or interrupt is 
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4805 / 5251


---
# 페이지 1946

generated. FRAD check is only done for flash write transactions not for read. Actual write on QuadSPI SFAR and IPCR register is 
done by SFP module only after the transaction passes MDAD and FRAD checks. There is only a single IPS slave interface which 
can be used for QuadSPI IPS register access and SFP IPS register access.
An IPS master transaction is secure if IPS_NONSECURE_ACCESS attribute is set to 0 for that transaction. An IPS master 
transaction is privileged if IPS_SUPERVISOR_ACCESS attribute is set to 1 for that transaction.
QuadSPI SFP related register sets are present here.
79.12.1 MDAD
These descriptors form the first level of checks on the input IPS transaction. There are two target group queues (TG0 and TG1) 
present in SFP block and each of these queues can be programmed with different set of MGAD descriptors checks in TGnMDAD 
registers. These registers are under access control and can only be programmed by privilege masters. These descriptors (one 
or both) should be programmed before start of any flash transaction else any IPS write on SFAR, IPCR or TBDR registers will 
generate an IPS bus error. After programming the target group descriptor the TGnMDAD[VLD] should be set to 1 for that register.
There are two target group queues (TG0 and TG1) so two transactions by different master ID can be stored inside SFP block while 
one of them is being processed by QuadSPI.
79.12.1.1
MDAD checks
• Secure check – This is decided by the TGnMDAD[SA] field of the MDAD descriptor. If the fields are set to 01 then queue is 
reserved for only non-secure transactions. If set to 10 then queue is reserved for only secure transactions. If the bits are set 
to 11 then this check is bypassed.
• MasterID check – This check compares themasterID of the input transaction with the MID match value set 
inTGnTGnMDAD[MIDMATCH]fields and allows only matching transactions inside the queue. There are 6 mask fields 
(TGnTGnMDAD[MASK]) inside the descriptor. If the mask type (TGnTGnMDAD[MASKTYPE]) is set to 0 then the input 
transactions master ID is ANDed with the mask bits before comparing with the MID match value. If the mask type is set to 1 
then the input master ID is ORed with the masks bits and then compared with the MID match bits. Multiple master IDs can 
be allowed inside the queue using this mask.
When an IPS write is done to SFAR or IPCR registers then SFP block checks the attributes with MDAD descriptors of both the 
queues. If the attributes match with descriptor of any queue, then the value is written inside that queue and master ID is assigned 
to that queue. The queue is considered locked once the SEQID bits of IPCR register are written. So software should ensure that 
IPCR SEQID bits are written only after SFAR and other IPCR bits like DATSZ are written in that queue. The queue will be unlocked 
when flash transfer is completed for that transaction.
Once a master ID is assigned to a queue then transactions with only that master ID are allowed inside the queue. Any write of 
SFAR/IPCR is mapped to this queue even if other queue is free. So same master ID cannot have transaction on both queues at 
a time. The data in the queue is cleared once the flash transaction is finally completed by the QuadSPI.
The data path for input IPS writes to SFAR or IPCR registers are shown in the following figure.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4806 / 5251


---
# 페이지 1947

Store in TG0/TG1 
Status registers
Descriptor checks
TG0 and TG1
Queue busy 
Assign Master ID
Queue locked 
Data write to
Check Pass
SEQID written
Check pass
Check Fail
Generate bus 
Clear queue
Flash transaction
complete
Write to
 SFAR/ICPR 
 registers
error
FRAD check started
QuadSPI registers
Check Fail
Figure 519. Data path for input IPS write to QuadSPI SFAR or IPCR registers
If the SFAR write passes first level of MDAD checks then the value is written in SFP register TGnSFAR and valid bit is set 
in TGnSFARS register and queue is considered as busy. Similarly when ICPR write passes the checks, its value is written 
into TGnIPRCS register and TGnIPRCS[VLD] field is set to 1 and queue is considered as locked. It is mandatory that IPCR is 
written only after SFAR has been written for a queue and queue is busy. If IPCR is written before SFAR then it will result in 
IPS transfer error. Master should ensure that it completes the programming sequence for flash access request (write SFAR and 
IPCR with SEQID) so that target queue is not left after writing SFAR or IPCR without the SEQID. Both queues TG0 and TG1 are 
processed in round robin arbitration. The queue receiving the data first is processed first and next queue is processed after the 
first transfer completes.
 
TBDR register write is not allowed until the SFAR and IPCR entries of that master has passed MDAD and FRAD 
checks and the transaction is queued for writing to QuadSPI. If TBDR registers are written before arbitration win, 
transfer error will be generated. IPS master can read FSMSTAT register to check the status of their transaction. 
TBDR access is allowed when FSMSTAT[VLD] field is set and for the master whose master ID matches with fields 
[11:8] of this register, and field [1:0] are set to 01 or 10. IPCR and SFAR registers are forwarded to QuadSPI only 
after the TX buffer is filled till watermark level in case of write transactions. IPCR should be written only after SFAR 
has been written successfully to a queue.
  NOTE  
79.12.1.2
Error conditions
The error conditions for first level of MDAD checks and the response is given in table below. These error conditions can occur 
when SFAR, IPCR or TBDR registers are being written.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4807 / 5251


---
# 페이지 1948

 
Queue is considered busy if it has been written successfully once with any of the values SFAR, IDATSZ or PAR. 
Queue is considered locked when SEQID has been written successfully by passing MDAD checks.
  NOTE  
Table 761. MDAD check error conditions
Error condition
Response
Common/Queue error
None of the queue descriptors 
are programmed
IPS transfer error is generated
Common error
Both queues are locked
IPS transfer error is generated
Common error
Both queues are busy and another 
master writes whose master ID is not 
matching with either queue.
IPS transfer error is generated.
Common error
Queue busy and same master writes 
SFAR or IPCR registers with wrong 
security attribute
IPS transfer error is generated and queue 
is cleared (SFAR and IPCR needs to be 
written again for transfer to start).
Queue error
Queue is locked and same master writes IPS transfer error is generated
Common error
If master ID of transaction doesn’t qualify 
MID check of any of the queues
IPS transfer error is generated
Common error
If both the queues are empty and security 
attribute of transaction doesn’t match 
with any of the queues
IPS transfer error is generated
Common error
TBDR register is written before SFAR 
and IPCR SEQID qualifies MDAD checks
IPS transfer error is generated
-
If none of FRAD descriptors 
are programmed
IPS transfer error is generated
Common error
IPCR is written before SFAR
IPS transfer error is generated
Common Error - If the transaction doesn't 
matches the security attribute check or 
MID check of any MDAD.
No common or queue error - If it matches 
security and MID attribute of any queue.
When a common error is generated its details are latched in IPSERROR register and corresponding error field is set to 1. This 
register will tell if the transaction failed because of queue locked, MID mismatch or security failure along with the master ID of that 
transaction. This register will keep the last error transaction latched unless cleared by writing 1 to CLR bit of this register. Then from 
next cycle onwards this register can latch new errors. Common error will also be generated if none of the FRAD descriptors are 
programmed. In case a queue is busy and same master writes IPCR or SFAR with wrong security attributes the queue is cleared, 
the Target Group n SFAR Status (TG0SFARS - TG1SFARS) valid bit goes low. In this case the master should write the SFAR an 
IPCR again for proper transaction to start.
In case of queue error the details are latched in Target Group n IPCR Status (TG0IPCRS - TG1IPCRS) or Target Group n SFAR 
Status (TG0SFARS - TG1SFARS) registers. These registers will also keep the error status latched until cleared by writing 1 to 
CLR bit of respective registers.
79.12.2 FRAD
These descriptors form the second level check for IPS flash write and flash erase transactions. IPS read transaction are not 
processed by this level of check and are passed through after MDAD checks. There are 8 FRADs which can be programmed 
by privilege masters. So the access checks can be programmed for up to 8 unique address ranges. Each of the address range 
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4808 / 5251


---
# 페이지 1949

is equipped with different access attribute checks and based on this write access can be controlled for the flash region. These 
descriptors must be programmed before starting transactions on flash.
After programming the FRADn_WORD0, FRADn_WORD1, FRADn_WORD2 and FRADn_WORD3 registers, 
FRADn_WORD3[VLD] field should be written 1. SFP block doesn’t consider the FRAD descriptors which are not valid. If 
none of the FRAD are programmed, then error interrupt will be generated if enabled, and transaction is not forwarded to QuadSPI.
There is a descriptor lock feature to prevent spurious changes to the FRAD. FRADn_WORD3[LOCK] can be programmed to make 
all FRAD registers as read only or to allow write access to all or some masters with specific master ID.
79.12.2.1
FRAD checks
• Address range checks – Start and end address for FRAD region are programmed in FRADn_WORD0 and FRADn_WORD1 
registers. Start address of IPS flash transaction written in SFAR register and data size programmed in IPCR register, is used 
to check if the transaction lies within any of the FRAD address ranges. This address range match will be used to select the 
corresponding FRAD from which other access checks will be done. The start and end address are programmed around 64 
KB boundary so 16 MSB are only used for range check..
The data size should not be programmed as 0 in IPCR register for normal data transfers to flash and actual size should be 
programmed. In the cases where only flash instruction has to be send and no data has to be written in TBDR register, this 
DATSZ can be programmed as 0. In case the DATSZ is programmed as 0 in IPCR, SFP module blocks the write access to 
TBDR register and if any write is done then that generates IPS transfer error.
• Exclusive access lock – Exclusive master access lock can be enabled over any flash address defined under a FRAD. 
The master ID of the master which enables/owns the exclusive access is captured in FRADn_WORD2[EALO] fields. 
Once enabled, the exclusive lock can be released only by the same master which enabled the lock by writing on 
FRADn_WORD3[EAL] fields. The exclusive write access permissions of a flash region are decided as given in table below:
Table 762. Exclusive access lock
FRADn_WORD3[EAL]
Write permissions
00
No lock. The write permissions are decided as set in FRADn_WORD2[MDnACP] 
fields for respective master domain.
10
Write permissions are revoked for all masters. Any write transaction coming to this 
flash address region will not be forwarded through and will result in an error.
11
Write permissions are revoked for all masters except the master ID matching the ID 
specified by FRADn_WORD2[EALO] fields.
• Flash region privilege checks – If the FRADn_WORD3[EAL] fields are set to 00 then flash write access permissions for any 
IPS master is decided based on the settings done in FRADn_WORD2[MDnACP] fields as given in table below. MD0ACP 
permission checks are done for transaction coming through target group 0 queue (TG0) and MD1ACP permission checks are 
for transactions coming through target group 1 queue (TG1).
Table 763. Flash region privilege checks
MDxACP value
Privilege access
Secure access
Write access
111
No
No
Not allowed
No
Yes
Not allowed
Yes
No
Allowed
Yes
Yes
Allowed
110
No
No
Allowed
No
Yes
Allowed
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4809 / 5251


---
# 페이지 1950

Table 763. Flash region privilege checks (continued)
MDxACP value
Privilege access
Secure access
Write access
Yes
No
Allowed
Yes
Yes
Allowed
101
No
No
Not allowed
No
Yes
Not allowed
Yes
No
Not allowed
Yes
Yes
Allowed
100
No
No
Not allowed
No
Yes
Allowed
Yes
No
Not allowed
Yes
Yes
Allowed
0xx
-
-
Not allowed
If any transaction fails FRAD check then error interrupt is generated if enabled.
FRAD status registers keep the details of last transaction which lie within the address range of that respective FRAD and will be 
updated only when a new transaction comes which falls within the same address range.
Flash Region Compare Address Status (FRAD0_WORD4 - FRAD7_WORD4) register stores the flash start address that was 
compared and Flash Region Compare Status Data (FRAD0_WORD5 - FRAD7_WORD5) contains the master ID, privilege and 
secure attributes of the transaction. The transaction details are stored in FRAD register for which the address compare check 
passed. These status registers are not updated in case of read transfers or when FRAD check is disabled. For example, if the 
transaction address lies in the range set in FRAD2_WORD0 and FRAD2_WORD1 then the transaction details will be stored in 
FRAD2_WORD4 and FRAD2_WORD5 registers and valid field [30] will be set. If transaction fails, the security or privilege attribute 
check for the corresponding FRAD then error field [29] is set in FRADx_WORD5 status register. This bit and other transaction 
details will remain latched unless cleared by writing '1' to W1C bit of corresponding FRAD in ERRSTAT register.
If transaction address doesn’t match any of the FRAD address range or if matches with multiple FRAD address ranges, then also 
error interrupt is generated. But for no FRAD match, the details will not be stored in any of the FRAD status registers.
FRAD checks are done only for flash write transactions, flash read transactions are passed through to QuadSPI if MDAD checks 
are passed. At least one FRAD region should be made valid (if the FRAD check is enabled from MGC register) for flash read 
instructions to go through even when FRAD check is not done for read instructions. SFP module checks if a transaction is read or 
write from the SEQID written in IPCR register and LUT table programmed inside QuadSPI. Master Read Command (MRC) register 
shows the read command code which SFP block identifies. There are two command codes which are predefined READ_DDR and 
READ commands. Software can program two other command code as per its convenience by writing into fields [21:16] or [29:24] 
and then writing respective valid bit as 1.
79.12.2.2
Error conditions
Any transaction passing the MDAD checks will be checked for FRAD checks and can lead to following error scenarios.
Table 764. Error conditions
Error condition
Response
None of the FRAD are programmed
IPS transfer error will be generated and status will be latched in 
IPS_ERROR register
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4810 / 5251


---
# 페이지 1951

Table 764. Error conditions (continued)
Error condition
Response
Transaction address doesn’t fall within any of the FRAD 
address range
Error interrupt will be generated if enabled
Transaction match with multiple FRAD address range
Error interrupt will be generated if enabled. Error bit will be set, and 
status will be stored in FRADx_WORD5 status registers for whom the 
address check passed
Transaction passes FRAD address check but fails 
privilege or security checks
Error interrupt will be generated if enabled. Error bit will be set, and 
status will be stored in FRADx_WORD5 status registers for whom the 
address check passed
Transaction passes FRAD address check but range was 
locked by EAL bits
Error interrupt will be generated if enabled. Error bit will be set, and 
status will be stored in FRADx_WORD5 status registers for whom the 
address check passed
Read transaction
No FRAD check will be done and no error will be generated for FRAD 
failure. But if FRAD check is enabled in MGC then at least one FRAD 
should be valid else it will give error during SFAR/IPCR write
79.12.2.3
Atomic commands considerations
For security reasons, the atomic commands (where flash's internal configuration region is accessed) like flash erase etc. should 
always be programmed in last 6 SEQID locations of LUT. FRAD0 has access to all the LUT locations including these last 6 SEQID. 
Remaining FRAD regions will not allow write access if the IPCR SEQID is set for any of the last 6 locations of LUT. It will result 
in FRAD access error and it will set in FRAD status registers. Also the software must set the FRAD0 MDACP to 101 so that write 
access is allowed only for secure privilege masters. This is done to ensure that no other master can use the atomic commands 
like flash erase to change the contents of flash. So when any master wants to use these atomic command programmed in last 6 
locations of LUT it will have to write FRAD0 start address in SFAR and keep IPCR DATSZ such that it falls under FRAD0 address 
region and MDACP programmed in FRAD0 are checked.
For flash configuration in case of dual-die the software needs to change the address range of FRAD0 accordingly so that address 
goes to second die. Similar consideration to be taken in case of dual flash where Port A and B are being used.
79.12.3 TBDR register write lock
SFP module keeps the TBDR write locked for IPS transactions by default. When a IPS master writes SFAR and IPCR transactions 
and this transaction passes MDAD and FRAD checks then the accesses are unlocked for that master ID. Lock and unlock 
procedure is shown with an example in figure below:
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4811 / 5251


---
# 페이지 1952

 
Input transaction 
 
MID = M1
MDAD 
 
checks
 passed
TG0/TG1 queue 
FRAD 
checks passed
 
Queued for  
QuadSPI Idle
 
Write QuadSPI IPCR, 
 
SFAR registers
Flash 
 
TG0/TG1 
 
TBDR write locked
 
Unlocked 
queue clear
transaction 
finished
QuadSPI
for master M1
TBDR write
locked
Figure 520. TBDR lock and unlock procedure
If any master writes on TBDR register when it is not unlocked for that master ID it will result in IPS transfer error. IPS master should 
ensure that it writes the TBDR register once QuadSPI registers have been written by the SFP module. This can be checked by 
reading FSM Status (FSMSTAT). Bits [11:8] of this register tells which master ID is currently active, and if the value of bits [1:0] is 
01 or 10 and bit 31 is set as 1, then the TBDR lock is open for write transactions. It is advisable that for write transactions where 
IDATSZ is non zero, master clears the TBDR buffer from any residue data and program the TBCT[WMRK] watermark once its 
request is granted in arbitration (FSMSTAT bit [1:0] are 01). In case of transfers having IDATSZ programmed as 0 the TBDR 
register remains locked and data can't be written to this register. In case DMA is being used to fill the TBDR buffer, program 
RSER[TBFDE] field to 1 only when write access is granted and TBDR access is unlocked after checking FSMSTAT[STATE] 
field. Once DMA completes the TBDR write reset, this field is set back to 0. After this, the SFP will write SFAR and IPCR to 
QuadSPI triggering the flash transfer. It should be made sure that the DMA should have same master ID as the master which won 
the arbitration.
79.12.4 Transaction status registers
SFP module has two registers (FSM Status (FSMSTAT) and FlashSeq Request (FLSEQREQ)) which shows the current and last 
transaction status. These registers are updated only after MDAD and FRAD check are passed.
• FSM Status (FSMSTAT) register shows the current transaction which is queued for QuadSPI when valid field [31] is set. Field 
[16] of this register if set to 1 then it is a non-read instruction sequence and it is set to 0 then it means that this is a read 
sequence. Fields [11:8] show the master ID from which this transaction is generated. Fields [1:0] show the current state of 
active transaction when valid field [31] is set.
The figure below shows the IPS transaction flow inside SFP block along with various values of bits [1:0]:
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4812 / 5251


---
# 페이지 1953

Insert in queue if 
MDADn check is 
passing
IPS IN
QuadSPI
status check
Idle
TBDR lock open
Clear queue
and TBDR locked 
Transfer complete
Busy
Yes
If second 
queue has an 
active transfer
Check FRADn for 
write transfers
(No check for read transfer)
Timeout
error?
Write transfer
Read transfer
Write SFAR and SEQID
 to QuadSPI
Timeout
Timeout
QuadSPI
status check
Idle
Busy
Txbuffer filled above 
watermark threshold
Figure 521. Transaction status
 
If the DATSZ programmed in TG0/TG1 IPCR register is more than the TX buffer watermark threshold value (256- 
Watermark programmed in TBCT) then it waits for threshold to cross before writing the SFAR and IPCR registers 
to QuadSPI. Else SFP block waits for one entry to be written to TBDR register and after that it writes the SFAR and 
IPCR to QuadSPI thus triggering the transfer. In case of read transfers, SFAR and IPCR are written as soon as 
QSPI is IDLE.
  NOTE  
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4813 / 5251


---
# 페이지 1954

 
QuadSPI is considered IDLE if transaction is finished at flash, No DMA and interrupt pending and RX data is 
completely read. In case RX data is pending it can be cleared by writing to MCR[CLR_RXF]. Refer to section 
Timeout error for more details.
  NOTE  
FSM state values in FSM Status (FSMSTAT) for different states are in the following table:
Table 765. FSMSTAT register field details
FSMSTAT 
register fields
VLD
0 - No IPS transfer is queued for launch to QuadSPI
1 - IPS transfer is queued or running in QuadSPI
STAT
00 - QuadSPI is busy with AHB transfer, any DMA transfer is pending, RDBFL has residue data or any 
interrupt is pending.
01 - TBDR lock is open. QuadSPI considers IPS transfer. AHB transfer should not start.
10 - TX buffer filled above threshold. Write transfer is triggered. SEQID is written.
11 - Read transfer is triggered. SEQID is written.
For flash write transfers which passes MDAD and FRAD checks and QuadSPI is not busy with any previous transfer, TBDR 
lock is opened and bits [1:0] shows value of 01. Once the IPS master fills the TX buffer till the level where free entries in TX 
buffer are less than the watermark threshold set in TX Buffer Control Register (TBCT) and SR[TXWA] flag is de-asserted, SFP 
block writes the SFAR and IPCR entries to QuadSPI registers and transaction is triggered. To avoid underrun, program the 
watermark accordingly for size of the data to be transferred. This programming can be done when TBDR access is allowed 
after arbitration is granted. TBCT Watermark can be programmed as 256-(IDATSZ/4-1) in most of the scenarios. If the DATSZ 
entry written in IPCR is less such that TX buffer can never be filled till watermark threshold, in such cases SFP block does not 
wait for the TBCT[WMRK] to trigger and writes the SFAR and ICPR registers as soon as one data entry is written to TBDR 
register. When the SFAR and IPCR register are written, bits [1:0] are set to 10. In case of flash memory read transfers SFAR 
and IPCR entries are written to QuadSPI as soon as QuadSPI is IDLE and bits [1:0] are set to 11. QuadSPI is considered IDLE 
only if no AHB/IPS transfer is ongoing, any DMA transfer is not pending, RDBFL doesn't have residue data and any interrupt 
is not pending (FR[TFF], FR[TBFF], FR[TBUF], FR[RBDF], FR[RBOF], FR[ABOF], FR[AIBSEF], FR[AITEF], , , FR[IPIEF], , 
FR[ILLINE], , ). Valid bit [31] goes to 0 once the IPS transfer is completed. IPS master should clear the TX buffer before writing 
to TBDR register to ensure that no data from previous transaction is left in TX buffer.
If the IPS transaction has passed the MDAD and FRAD checks but QuadSPI is busy with some AHB transfer, then the bits 
[1:0] are set to 00. Other than ongoing AHB transfer QuadSPI can be busy because of other reasons also like if any TXDMA 
or RXDMA pending, if read buffer has data pending or if any QuadSPI interrupt is enabled and pending for servicing. So IPS 
master should ensure that no interrupt is pending or previous read transfer is completed. If the QuadSPI remains busy for a 
longer time it may result in timeout error.
Software must take care that no AHB transaction is launched when any IPS transaction is ongoing, TBDR lock is open or IPS 
transaction is getting executed on QuadSPI. It can be checked by reading this FSM status register. if the valid bit is 1 and bits 
[1:0] are set to 01, 10 or 11 then no AHB transfer should be generated towards QuadSPI.
For any IPS initiated RW transaction which needs two separate transactions at flash interface, like Write-Enable transaction 
followed by Write-data transaction (Data-Learn flash transaction followed by Read-data transaction) at flash interface must 
be joined together with JMP_2_SEQ instruction.
• FlashSeq Request (FLSEQREQ) register holds the details of transaction which was last send to QuadSPI. After a flash 
transaction is completed this register is updated and its valid field [31] is set to 1. This register holds the command type (read 
or write), transaction master ID (fields [3:0]), target group queue (TG0 or TG1) from which this transaction passed in field [4], 
privilege and secure attributes for the transaction, SEQID (fields [19:16]) and number of flash descriptor FRAD within whose 
address range the transaction lies (fields [14:12]).
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4814 / 5251


---
# 페이지 1955

This register also contains a timeout error field [27] which is set when a timeout error occurs, and transaction is aborted. When 
the error occurs this register keeps the status latched unless it is cleared by writing 1 to clear field [29].
79.12.5 Timeout error
MTO register can be programmed with a timeout value above which the transaction should be aborted. When the transaction 
passes MDAD and FRAD level checks and QuadSPI is idle (no AHB transaction is ongoing, no DMA transfer is pending, 
RDBFL doesn't have any residue data from last transfer and (FR[TFF], FR[TBFF], FR[TBUF], FR[RBDF], FR[RBOF], FR[ABOF], 
FR[AIBSEF], FR[AITEF], , , FR[IPIEF], , FR[ILLINE], , ) interrupt is not pending) this counter is started. If the transaction is not 
completed before this timeout counter reaches the value programmed in MTO register the transaction is considered aborted by 
SFP and an error interrupt is generated if enabled. The error bit is also set in FLSEQREQ register along with the transaction details. 
After the timeout error, next transaction is written to QuadSPI register which was queued in another target group queue once 
SR[BUSY] flag goes low.
79.12.6 Arbitration lock
The arbitration lock feature is used to lock the arbitration for a particular queue. This lock can be requested by a master by writing 
'1' into IPCR[ARB_LOCK] field. Once the transaction passes both the checks (MDAD & FRAD) and wins the arbitration, this lock 
will be granted. After this, the transaction from the other queue will not be granted unless the arbitration is unlocked by previous 
queue. The master which locked the arbitration can unlock it by writing '1' to IPCR[ARB_UNLOCK] field. Once the transaction with 
unlock bit 1 passes the MDAD and FRAD checks, it will unlock the arbitration. After this transaction is finished, the other queue 
will be granted the arbitration which was waiting.
This arbitration lock feature can be used by software while doing any transaction to flash which may result in a waiting period. For 
example, in case of NOR flash, after a write is issued to flash there is a waiting period (TPP) for which the flash is inaccessible. In 
this case, the software should ensure that while writing this SEQID to IPCR register it should lock the arbitration so that transaction 
coming to other queue is not passed to flash controller which may result in failure. Once the software ensures that waiting period at 
flash is over, it can read the flash configuration/status registers to confirm. And after getting confirmation, it can send another read 
command to same configuration register with IPCR[ARB_UNLOCK] field set to '1'. This will ensure that the transaction waiting in 
another queue are granted. If the flash being used does not have a waiting period attached with transactions, then this ARB_LOCK 
field can be always kept to 0.
In case software uses this LOCK functionality RWW support will not be available. Because in this case, all the transaction from 
other queue which was blocked from arbitration will be blocked irrespective of read or write access. So, RWW support (read can 
go through even when flash is in waiting state) will not be available. The master which has arbitration lock granted can still send 
read accesses to flash during the waiting period in case the flash supports it.
79.12.7 Soft reset consideration with SFP
If there is any pending transaction in MDAD queue, do not assert QuadSPI reset bits unless you observe unexpected behavior 
like no response from the module. In that case, assert QSPI reset twice.
In case the soft reset is being used for QSPI, software should take some considerations so that correct functionality is maintained. 
if the soft reset is asserted when a transaction is being executed by SFP (FSM_STATE [1:0] bits are 01, 10 or 11) then this 
transaction will be aborted. Different conditions that can occur in case of soft reset are listed in table below:
Table 766. Soft reset conditions
Condition at time of soft reset
FSM state register 
at time of soft reset
Result
Timeout scenario
Some AHB transaction was 
ongoing and SFP/IPS is in 
waiting state.
FSM_STATE[1:0] = 
00
After the soft reset if de-asserted the SFP 
will schedule its transaction over QSPI. 
FSM_STATE[1:0] will change to other values 
than 00. Software can fill TBDR in case it is 
a write transfer or start reading from RBDR.
In this case software 
doesn’t writes to TBDR 
or read from RBDR it 
will result in timeout 
error.
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4815 / 5251


---
# 페이지 1956

Table 766. Soft reset conditions (continued)
Condition at time of soft reset
FSM state register 
at time of soft reset
Result
Timeout scenario
QSPI was IDLE and 
SFP transaction has been 
arbitrated. TBDR is being 
filled and SFAR, IPCR are 
not currently written to QSPI.
FSM_STATE[1:0] = 
01
Currently TBDR was being filled after soft 
reset all the entries in TBDR are flushed. So 
it is expected from software that it will start 
filling TBDR from start after the reset has 
de-asserted. SFP will write SFAR and IPCR 
to QSPI once its normal conditions are met 
(when number of available spaces in the TX 
buffer is greater than or equal to the value 
provided by TBCT[WMRK] or single TBDR 
write in case watermark check is disabled)
Timeout will occur if 
TBDR is not filled again 
after the soft reset is 
lifted.
SFP has written just SFAR to 
QSPI IPCR is not written yet.
(For a read transfer or write 
transfer with data size 0)
FSM_STATE[1:0] = 
01
After the soft reset is lifted the SFP will write 
ICPR to QSPI module and FSM_STATE will 
change to 11 (read) or 10(write). Transaction 
will finish normally.
Timeout conditions will 
be same as that for 
normal transfer.
SFP has written just SFAR to 
QSPI IPCR is not written yet.
(Write data size is non 0)
FSM_STATE[1:0] = 
01
After soft reset is lifted the SFP will write 
IPCR to QSPI module once software fill 
TBDR (from start) and FSM_STATE will 
change to 10.
Timeout conditions will 
be same as that for 
normal transfer.
SFP has written SFAR and 
IPCR to QSPI.
FSM_STATE[1:0] = 
10 or 11
After the soft reset is de-asserted the 
current transaction will be deemed aborted. 
FSM_STATE valid will go low as transfer has 
finished.
No timeout.
So to conclude in case the soft reset is asserted when FSM_STATE[31] bit is 1 and state bits are 10 or 11 current transaction will 
be aborted & the next transaction will proceed as normal. In case the state bits are 00 or 11 then it is advisable that software doesn't 
writes into TBDR after the reset is de-asserted and waits for timeout error to be generated to know when current ongoing SFP 
transaction is aborted. After clearing the timeout error a new transaction can be launched to SFP or if already a new transaction 
is present in another queue it will be arbitrated.
79.12.8 Error Interrupt Enable
INT_EN register allow software to disable or enable the interrupt signal generation in case of any of the listed error conditions. This 
interrupt is generated on 'ipi_int_ored' interface signal of QuadSPI.
• Time out error (INT_EN[TO_ERR])
• IPCR register write error (INT_EN[TGnIPCR])
• SFAR register write error (INT_EN[TGnSFAR])
• IPS common error (INT_EN[IPS_ERR])
• FRAD access error (INT_EN[FRADnACC])
• No FRAD address range match error (INT_EN[FRADMTCH])
If the respective field is set to 1 for any of the error conditions, then the interrupt signal is set to 1 when that error occurs and it 
remains set until the error is cleared by writing 1 to error clear bit as listed in register descriptions.
79.13 Memory map and register definition
This section provides the memory map and register definitions for the QuadSPI module.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4816 / 5251


---
# 페이지 1957

79.13.1 Register write access
Following are the write access restriction terms that apply to all the registers:
• Register write access restriction
For each register field, the write access conditions are specified in the detailed register description.
The following table provides a description of the write access conditions. If, for a specific register bit or field, none of the given 
write access conditions is fulfilled, any write attempt to this register bit or field is ignored without any notification. The values 
of the bits or fields are not changed.
The condition term [A or B] indicates that the register or field can be written to if at least one of the conditions is fulfilled.
Table 767. Register write access restrictions
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
79.13.2 QuadSPI register descriptions
This section provides the memory map and register definitions for the QuadSPI module.
Access to the following addresses does not result in a transfer error:
• 64h
• 138h
• 168h
• 188h
• 18Ch
• 198h
79.13.2.1
QuadSPI memory map
QuadSPI_S32K358 base address: 404C_C000h
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
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4817 / 5251


---
# 페이지 1958

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
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
50h
AHB Write Configuration Register (AWRCR)
32
RW
0000_0000h
60h
DLL Flash Memory A Configuration Register (DLLCRA)
32
RW
0120_0000h
6Ch
Parity Configuration Register (PARITYCR)
32
RW
0000_0000h
100h
Serial Flash Memory Address Register (SFAR)
32
RW
0000_0000h
104h
Serial Flash Memory Address Configuration Register (SFACR)
32
RW
0000_0800h
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
120h
AHB Write Status Register (AWRSR)
32
R
0000_0000h
12Ch
DLL Status Register (DLLSR)
32
R
8000_8000h
130h
Data Learning Configuration Register (DLCR)
32
RW
40FF_40FFh
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
0100_0000h
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
190h
Data Learn Pattern Register (DLPR)
32
RW
AA55_3443h
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4818 / 5251


---
# 페이지 1959

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
194h
Flash Memory A Failing Address Status Register (FAILA_ADDR)
32
R
FFFF_FFFFh
200h - 27Ch
RX Buffer Data Register (RBDR0 - RBDR31)
32
R
0000_0000h
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
318h - 44Ch
LUT Register (LUT2 - LUT79)
32
RW
0000_0000h
800h
Flash Region Start Address (FRAD0_WORD0)
32
RW
0000_0000h
804h
Flash Region End Address (FRAD0_WORD1)
32
RW
0000_FFFFh
808h
Flash Region Privileges (FRAD0_WORD2)
32
RW
0000_0000h
80Ch
Flash Region Lock Control (FRAD0_WORD3)
32
RW
0000_0000h
810h
Flash Region Compare Address Status (FRAD0_WORD4)
32
R
0000_0000h
814h
Flash Region Compare Status Data (FRAD0_WORD5)
32
R
0000_0000h
820h
Flash Region Start Address (FRAD1_WORD0)
32
RW
0000_0000h
824h
Flash Region End Address (FRAD1_WORD1)
32
RW
0000_FFFFh
828h
Flash Region Privileges (FRAD1_WORD2)
32
RW
0000_0000h
82Ch
Flash Region Lock Control (FRAD1_WORD3)
32
RW
0000_0000h
830h
Flash Region Compare Address Status (FRAD1_WORD4)
32
R
0000_0000h
834h
Flash Region Compare Status Data (FRAD1_WORD5)
32
R
0000_0000h
840h
Flash Region Start Address (FRAD2_WORD0)
32
RW
0000_0000h
844h
Flash Region End Address (FRAD2_WORD1)
32
RW
0000_FFFFh
848h
Flash Region Privileges (FRAD2_WORD2)
32
RW
0000_0000h
84Ch
Flash Region Lock Control (FRAD2_WORD3)
32
RW
0000_0000h
850h
Flash Region Compare Address Status (FRAD2_WORD4)
32
R
0000_0000h
854h
Flash Region Compare Status Data (FRAD2_WORD5)
32
R
0000_0000h
860h
Flash Region Start Address (FRAD3_WORD0)
32
RW
0000_0000h
864h
Flash Region End Address (FRAD3_WORD1)
32
RW
0000_FFFFh
868h
Flash Region Privileges (FRAD3_WORD2)
32
RW
0000_0000h
86Ch
Flash Region Lock Control (FRAD3_WORD3)
32
RW
0000_0000h
870h
Flash Region Compare Address Status (FRAD3_WORD4)
32
R
0000_0000h
874h
Flash Region Compare Status Data (FRAD3_WORD5)
32
R
0000_0000h
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4819 / 5251


---
# 페이지 1960

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
880h
Flash Region Start Address (FRAD4_WORD0)
32
RW
0000_0000h
884h
Flash Region End Address (FRAD4_WORD1)
32
RW
0000_FFFFh
888h
Flash Region Privileges (FRAD4_WORD2)
32
RW
0000_0000h
88Ch
Flash Region Lock Control (FRAD4_WORD3)
32
RW
0000_0000h
890h
Flash Region Compare Address Status (FRAD4_WORD4)
32
R
0000_0000h
894h
Flash Region Compare Status Data (FRAD4_WORD5)
32
R
0000_0000h
8A0h
Flash Region Start Address (FRAD5_WORD0)
32
RW
0000_0000h
8A4h
Flash Region End Address (FRAD5_WORD1)
32
RW
0000_FFFFh
8A8h
Flash Region Privileges (FRAD5_WORD2)
32
RW
0000_0000h
8ACh
Flash Region Lock Control (FRAD5_WORD3)
32
RW
0000_0000h
8B0h
Flash Region Compare Address Status (FRAD5_WORD4)
32
R
0000_0000h
8B4h
Flash Region Compare Status Data (FRAD5_WORD5)
32
R
0000_0000h
8C0h
Flash Region Start Address (FRAD6_WORD0)
32
RW
0000_0000h
8C4h
Flash Region End Address (FRAD6_WORD1)
32
RW
0000_FFFFh
8C8h
Flash Region Privileges (FRAD6_WORD2)
32
RW
0000_0000h
8CCh
Flash Region Lock Control (FRAD6_WORD3)
32
RW
0000_0000h
8D0h
Flash Region Compare Address Status (FRAD6_WORD4)
32
R
0000_0000h
8D4h
Flash Region Compare Status Data (FRAD6_WORD5)
32
R
0000_0000h
8E0h
Flash Region Start Address (FRAD7_WORD0)
32
RW
0000_0000h
8E4h
Flash Region End Address (FRAD7_WORD1)
32
RW
0000_FFFFh
8E8h
Flash Region Privileges (FRAD7_WORD2)
32
RW
0000_0000h
8ECh
Flash Region Lock Control (FRAD7_WORD3)
32
RW
0000_0000h
8F0h
Flash Region Compare Address Status (FRAD7_WORD4)
32
R
0000_0000h
8F4h
Flash Region Compare Status Data (FRAD7_WORD5)
32
R
0000_0000h
900h
Target Group n Master Domain Access Descriptor (TG0MDAD)
32
RW
0000_0000h
904h
Target Group n SFAR Address (TG0SFAR)
32
R
0000_0000h
908h
Target Group n SFAR Status (TG0SFARS)
32
RW
0000_0000h
90Ch
Target Group n IPCR Status (TG0IPCRS)
32
RW
0000_0000h
910h
Target Group n Master Domain Access Descriptor (TG1MDAD)
32
RW
0000_0000h
914h
Target Group n SFAR Address (TG1SFAR)
32
R
0000_0000h
918h
Target Group n SFAR Status (TG1SFARS)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4820 / 5251


---
# 페이지 1961

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
91Ch
Target Group n IPCR Status (TG1IPCRS)
32
RW
0000_0000h
920h
Master Global Configuration (MGC)
32
RW
A800_0000h
924h
Master Read Command (MRC)
32
RW
0050_0E07h
928h
Master Timeout (MTO)
32
RW
FFFF_FFFFh
92Ch
FlashSeq Request (FLSEQREQ)
32
RW
0000_0000h
930h
FSM Status (FSMSTAT)
32
R
0000_0000h
934h
IPS Error (IPSERROR)
32
RW
0000_0000h
938h
Error Status (ERRSTAT)
32
RW
0000_0000h
93Ch
Interrupt Enable (INT_EN)
32
RW
0000_0000h
79.13.2.2
Module Configuration Register (MCR)
Offset
Register
Offset
MCR
0h
Function
This register holds configuration data associated with the QuadSPI operation.
 
When out of reset, after first initial MCR programming and exiting module disable mode (that is, when the value 
of MCR[MDIS] is 0), you must write 1 to MCR[SWRSTSD] and release it after six (three system and three flash 
memory) clock cycles.
  NOTE  
Special write-access is permitted in different modes:
• DQS_FA_SEL: Disabled mode
• ISD3FA, ISD2FA: Disabled mode
• All other fields: Anytime
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4821 / 5251


---
# 페이지 1962

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
DLPE
N 
0
0
0
VAR_L
AT...
DDR_
EN 
DQS_
EN 
Reserv
ed 
DQS_
OUT...
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
11b - External DQS
 
In case of an padloopback selection to access port A, port B cannot be programmed for 
external DQS and vice-versa.
  NOTE  
23
—
Reserved
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4822 / 5251


---
# 페이지 1963

Table continued from the previous page...
Field
Function
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
DLPEN
Data learning pattern enable
Write 1 to this field to enable data learning mechanism.
11
CLR_TXF
Clear TX FIFO/buffer
This is a self-clearing field that invalidates the TX buffer content.
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4823 / 5251


---
# 페이지 1964

Table continued from the previous page...
Field
Function
 
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
VAR_LAT_EN
Variable latency
Is used to enable the variable latency feature in the controller. This field is valid for HyperRAM where data 
strobe acts as an output from the memory during the command and address (CA) cycles of a read or write 
transaction. This is to indicate whether additional initial access latency is needed to perform a dynamic 
memory refresh operation. For details, see HyperRAM support.
0b - Fixed latency: Twice + 1 latency enable
1b - Variable latency: "Once" or "twice + 1" the initial latency based on data strobe during the CA 
phase. If enabled, you need to ensure that the value of FLSHCR[TCSS] is >= 2.
7
DDR_EN
DDR mode enable
Enables the DDR mode
0b - 2x clock disabled for SDR instructions only
1b - 2x clock enabled for DDR instructions. Note: 2x clock - This is twice the SCKF clock used to 
shift the TX data by 90 degree.
6
DQS_EN
DQS enable
Is valid for both the SDR and DDR modes. For details, see DQS sampling method.
0b - Reserved. Do not program 0 to this field.
1b - DQS enabled. The incoming data is sampled on both the edges of the DQS input when the 
value of MCR[DDR_EN] is 1; else, on only one edge when MCR[DDR_EN] is 0.
5
—
Reserved
4
DQS_OUT_EN
DQS as an output
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4824 / 5251


---
# 페이지 1965

Table continued from the previous page...
Field
Function
Is valid when data strobe is also used as an output from controller during the write data phase. This is 
valid for HyperRAM where the data strobe acts as a Read Write Data Strobe (RWDS). For details, see 
HyperRAM support.
0b - DQS as an output from controller is disabled.
1b - DQS as an output from controller is enabled.
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
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4825 / 5251


---
# 페이지 1966

79.13.2.3
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
 
Only one of the fields should be written '1' at a time out of ARB_LOCK and ARB_UNLOCK. If both the fields 
are written '1' at same time then it will invert the lock status. If the arbitration was already locked, it will unlock it 
and vice-versa.
  NOTE  
 
If MDAD and FRAD checks are enabled in MGC register but none of the MDAD and FRAD descriptors are valid, 
then any write on this register will generate a bus transfer error
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
SEQID 
0
0
0
Reserv
ed 
W
ARB_
UNL...
ARB_
LOCK 
Reset
0
0
0
0
0
0
0
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
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4826 / 5251


---
# 페이지 1967

Table continued from the previous page...
Field
Function
Each sequence index can accommodate up to 10 instructions (2 instructions per register).
In case of read command, a write to this field triggers a transaction on the serial flash memory interface if 
QSPI SFM is IDLE.
In case of write command, a write to this fields unlocks the TBDR access if QSPI SFM is not busy. Refer to 
section Secure flash protection for more details
23
ARB_UNLOCK
Arbitration Unlock
Writing 1 to this bit unlocks the arbitration. Writing 0 will have no effect. The arbitration unlock will be 
done only if the transaction passes both MDAD and FRAD checks. To lock the arbitration write 1 to 
ARB_LOCK bit. This bit is always read as 0.
22
ARB_LOCK
Arbitration Lock
Writing 1 to this bit locks the arbitration for that specific target queue. Writing 0 will have no effect. The 
arbitration lock will be granted only if the transaction passes both MDAD and FRAD checks. To unlock 
the arbitration write 1 to ARB_UNLOCK bit. This bit is always read as 0.
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
79.13.2.4
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
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4827 / 5251


---
# 페이지 1968

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
This hold time is in terms of serial flash memory clock cycles, and it must be greater than or equal to two 
flash memory clock cycles . Refer the chip datasheet for the exact value.
7-4
—
Reserved
3-0
TCSS
Serial flash memory CS setup time
This setup time is in terms of serial flash memory clock cycles, and it must be greater than or equal to two 
flash memory clock cycles. Refer the chip Datasheet for the exact value.
79.13.2.5
Buffer 0 Configuration Register (BUF0CR)
Offset
Register
Offset
BUF0CR
10h
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4828 / 5251


---
# 페이지 1969

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
30-16
—
Reserved
15-8
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
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4829 / 5251


---
# 페이지 1970

79.13.2.6
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
31-16
—
Reserved
15-8
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
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4830 / 5251


---
# 페이지 1971

Table continued from the previous page...
Field
Function
Any AHB read access with this master ID is routed to this buffer. You must ensure that the master IDs 
associated with all buffers are different.
 
See the chip-specific QuadSPI information for details about master IDs and their 
corresponding components.
  NOTE  
79.13.2.7
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
31-16
—
Reserved
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4831 / 5251


---
# 페이지 1972

Table continued from the previous page...
Field
Function
15-8
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
79.13.2.8
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
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4832 / 5251


---
# 페이지 1973

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
Reserved 
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
17-16
—
Reserved
15-8
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
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4833 / 5251


---
# 페이지 1974

79.13.2.9
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
This register is access controlled and can only be programmed by privilege masters.
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
SEQID_WR 
0
SEQID
_W...
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
SEQID_WR
Write Sequence ID
This field points to write seq-id of LUT and would be selected in case of AHB write transaction, if 
SEQID_WR_EN==1.
27-18
—
Reserved
17
SEQID_WR_EN
Enable Write Sequence ID
16
—
Reserved
15-12
Points to a sequence in the LUT.
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4834 / 5251


---
# 페이지 1975

Table continued from the previous page...
Field
Function
SEQID
This field contains the sequence index of the LUT. and would be selected in case of AHB read transaction 
(and AHB write transactions if SEQID_WR_EN==0).. See LUT.
 
If the sequence pointer differs in the new and the previous sequences, you should reset it. 
See sequence pointer clear register for more information.
  NOTE  
11-0
—
Reserved
79.13.2.10
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
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4835 / 5251


---
# 페이지 1976

79.13.2.11
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
31-11
—
Reserved
10-3
TPINDX0
Top index of buffer 0
2-0
—
Reserved
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4836 / 5251


---
# 페이지 1977

79.13.2.12
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
31-11
—
Reserved
10-3
TPINDX1
Top index of buffer 1
2-0
—
Reserved
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4837 / 5251


---
# 페이지 1978

79.13.2.13
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
31-11
—
Reserved
10-3
TPINDX2
Top index of buffer 2
2-0
—
Reserved
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4838 / 5251


---
# 페이지 1979

79.13.2.14
AHB Write Configuration Register (AWRCR)
Offset
Register
Offset
AWRCR
50h
Function
Special write-access is permitted if:
• SR[AWRACC] = 0
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
PPW_
WR_...
PPW_
RD_...
0
AWTRGLVL 
W
Reset
0
0
0
0
0
0
0
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
—
Reserved
15
PPW_WR_DIS
Page program wait write disabled
0b - Enables subsequent writes
1b - Disables subsequent writes to the flash memory. After the first write transaction, AHB write is 
returned with an error response.
14
PPW_RD_DIS
Page program wait read disabled
0b - Enables subsequent reads
1b - Disables subsequent reads to the flash memory. After the first write transaction, AHB read is 
returned with an error response.
13-8
—
Reserved
7-0
AHB write trigger level
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4839 / 5251


---
# 페이지 1980

Table continued from the previous page...
Field
Function
AWTRGLVL
Defines a trigger level of TX FIFO in terms of a 4-byte entry. AHB write to the flash memory is triggered when 
either of the following happens:
• TX FIFO crosses the level defined by this field
• AHB transaction completes
This is done to prevent an under run in the flash memory.
For HyperRAM, this field must be set to 0. For details, see HyperRAM support
79.13.2.15
DLL Flash Memory A Configuration Register (DLLCRA)
Offset
Register
Offset
DLLCRA
60h
Function
This register configures DLL and slave delay chain for flash memory A.
The value of the DLLEN field must be 1 after all reference (FREQEN, DLL_REFCNTR, DLLRES, SLAVE_AUTO_UPDT) delay 
chain configurations are programmed.
See DLL and delay chain usage for the programming sequence.
 
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
DLLEN 
FREQ
EN 
0
DLL_REFCNTR 
DLLRES 
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
DLL_
CDL8 
SLAVE
_A...
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
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4840 / 5251


---
# 페이지 1981

Fields
Field
Function
31
DLLEN
DLL enable
0b - DLL reference logic remains in reset and should be 0 for at least three flash memory clock 
cycles for reset.
1b - Enables DLL logic. Set it to 1 after all the configuration for DLLCR reference settings is 
complete.
30
FREQEN
Frequency enable
0b - Selects delay chain for low frequency of operation
1b - Selects delay chain for high frequency of operation
29-28
—
Reserved
27-24
DLL_REFCNTR
DLL reference counter
Select the "n+1" interval of DLL phase detection and reference delay updating interval (minimum 
recommended value = 1).
23-20
DLLRES
DLL resolution
Minimum resolution for DLL phase detector to remain locked/unlocked based on flash memory clock jitter. 
The minimum value is 2, and should be programmed to a more suitable value, such as 6.
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
DLL_CDL8
DLL CDL8 Enable
0b - DLL is implemented to support within 2x variation
1b - DLL is implemented to support within 3x variation (BCS -> WCS)
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4841 / 5251


---
# 페이지 1982

Table continued from the previous page...
Field
Function
3
SLAVE_AUTO_
UPDT
Slave chain update
This field automatically updates the slave chain as soon as DLL is locked.
0b - Auto-update feature is disabled.
1b - Auto-update feature is enabled.
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
SLV_UPD
Slave update
You must program this field only after slave delay chain configuration takes place.
0b - Disables any further update on DQS slave delay chain.
1b - Updates the DQS slave delay chain with either ref-delay or bypass slave delay value, and 
should be set in the absence of the DQS clock.
79.13.2.16
Parity Configuration Register (PARITYCR)
Offset
Register
Offset
PARITYCR
6Ch
Function
This register replicates the parity related configuration programming performed on the flash memory configuration registers.
You must write 1 to PARITYCR[CRCEN_FA] and PARITYCR[CRCEN_FB] after all parity configuration bits are programmed. 
However, you can program PARITYCR[BYTE_SIZE_FA] and PARITYCR[BYTE_SIZE_FB] at any time.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4842 / 5251


---
# 페이지 1983

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
W
Reset
0
0
0
0
0
0
0
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
CRC_
WND...
CHUNKSIZE_FA 
BYTE_
SI...
CRCE
N_FA 
CRCB
EN_...
CRCBI
N_...
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
31-21
—
Reserved
20-16
—
Reserved
15
CRC_WNDW_F
A
CRC address window configuration
0b - Calculates parity (CRC) over fixed address window within the denoted flash memory A chunk 
size boundary.
1b - Calculates parity (CRC) over incremental window of flash memory A chunk size, irrespective 
of address.
14-9
CHUNKSIZE_F
A
Chunk size for flash memory A
Defines the chunk size (in terms of 4 bytes) after parity is inserted and compared by the QuadSPI 
controller for flash memory A. Values 0x1, 0x2, and so on indicate 4 bytes, 8 bytes, and so on.
8
BYTE_SIZE_FA
Byte size for flash memory A
This field can be programmed any time. It enables single-byte, read/write parity with flash memory A 
configuration register. The field overrides the chunk size used for flash memory data array.
You must write 1 to this field before any read/write operation on the flash memory internal registers. And you 
must write 0 to this field before reading flash memory data array.
7
CRCEN_FA
CRC parity checker logic
0b - Disables parity mechanism. In case of parity error, set it to 0 to clear parity error. Only 
supported for DDR Octal commands.
1b - CRC parity checker logic for flash memory A read paths. Configure this field after 
programming CHUNK_SIZEA, CRCBEN_FA and CRCBIN_FA.
6
CRCBEN_FA
Adds CRC bar parity from flash memory A output to QuadSPI controller
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4843 / 5251


---
# 페이지 1984

Table continued from the previous page...
Field
Function
5
CRCBIN_FA
Adds CRC bar parity to flash memory A input from QuadSPI controller
4-0
—
Reserved
79.13.2.17
Serial Flash Memory Address Register (SFAR)
Offset
Register
Offset
SFAR
100h
Function
The module automatically translates this address on the memory map to the address on the flash memory. When operating in a 
24-bit mode, only bits 23-0 are sent to the flash memory. In the 32-bit mode, bits 27-0 are used with bits 31-28 driven to 0 when the 
value of SFACR[CAS] is 0. For example, if the value of SFACR[CAS] is 3, then bits 26-3 are sent to the flash memory as its page 
address in case flash memory is operating in a 24-bit mode. The total number of address bits requested by the flash memory, as 
its page and column address, must not be more than 32 bits. See Table 769 for the mapping between the access mode and the 
SFAR content and Normal mode for details on command triggering and command execution. The software must ensure that the 
serial flash memory address provided in the SFAR register lies in the valid flash memory address range, as defined in Table 769.
Special write-access is permitted if:
• SR[IP_ACC] = 0
 
If MDAD and FRAD checks are enabled in MGC register but none of the MDAD and FRAD descriptors are valid, 
then any write on this register will generate a bus transfer error
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
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4844 / 5251


---
# 페이지 1985

Fields
Field
Function
31-0
SFADR
Serial flash memory address
79.13.2.18
Serial Flash Memory Address Configuration Register (SFACR)
Offset
Register
Offset
SFACR
104h
Function
This register contains the address requirements that are specific to serial flash memory. These requirements must be configured 
according to the connected flash memory, for the controller to function properly. The module automatically translates the address 
of SFAR on the memory map or the incoming address on the AHB bus to the column address on the flash memory. For example, 
if a flash memory needs 3 bits as its column address, then only the lower three bits of the SFAR/AHB address are sent to the 
flash memory as its column address. The software should ensure that the serial flash memory address provided in SFAR or the 
incoming AHB address lies in the valid flash memory address range.
Special write-access is permitted if:
• SR[IP_ACC] = 0
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
CAS_I
NT...
0
Reserv
ed 
WA 
W
Reset
0
0
0
0
0
0
0
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
PPWB 
0
CAS 
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
0
0
0
0
0
Fields
Field
Function
31-21
—
Reserved
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4845 / 5251


---
# 페이지 1986

Table continued from the previous page...
Field
Function
20
CAS_INTRLVD
CAS Interleaving
0b - CAS interleaving is disabled
1b - CAS interleaving is enabled
19-18
—
Reserved
17
—
Reserved
16
WA
Word addressable
Defines whether the serial flash memory is a byte addressable flash memory or a word addressable flash 
memory. According to the configuration of this field, the address is remapped to the flash memory interface. 
See Address scheme for details.
0b - Byte addressable serial flash memory mode
1b - Word (2-byte) addressable serial flash memory mode
15-14
—
Reserved
13
—
Reserved
12-8
PPWB
Page program boundary
Flash memory-specific page program boundary size should be programmed in Log2 (size in bytes) 
format. The default is 8 = log2(256) for a 256-byte page program size.
7-4
—
Reserved
3-0
CAS
Column address space
Defines the width of the column address. If the column address is, for example, [2:0] of SFAR/AHB address, 
then CAS must be 3. If there is no column address separation in any serial flash memory, the value of this 
field must be specified as 0.
79.13.2.19
Sampling Register (SMPR)
Offset
Register
Offset
SMPR
108h
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4846 / 5251


---
# 페이지 1987

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
—
Reserved
18-16
—
Reserved
15-7
—
Reserved
6
Full-speed delay selection for internal/pad loop back DQS sampling
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4847 / 5251


---
# 페이지 1988

Table continued from the previous page...
Field
Function
FSDLY
This field selects the delay in accordance with the reference edge for the valid sample point.
0b - Same DQS
1b - Half-cycle early DQS
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
79.13.2.20
RX Buffer Status Register (RBSR)
Offset
Register
Offset
RBSR
10Ch
Function
This register contains information related to the receive data buffer.
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
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4848 / 5251


---
# 페이지 1989

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
RX Data Buffer Register (ARDB0 - ARDB31) and Data Transfer from the QuadSPI Module Internal Buffers.
15-6
—
Reserved
5-0
RDBFL
RX buffer fill level
Indicates the number of 4-byte entries available in the RX buffer. For example, a value of 0x2 indicates 8 
bytes are available.
79.13.2.21
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
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4849 / 5251


---
# 페이지 1990

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
 
This field should never be programmed above 31 because there are only 32 memory 
mapped RBDR registers. If watermark is programmed above 31, data above 32 words will 
be lost.
  NOTE  
79.13.2.22
AHB Write Status Register (AWRSR)
Offset
Register
Offset
AWRSR
120h
Function
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
SEQA
UJO...
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
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4850 / 5251


---
# 페이지 1991

Fields
Field
Function
31-3
—
Reserved
2
SEQAUJOIN
Sequence auto join
Asserted when the LUT sequences are automatically joined using the JMP_TO_SEQ command. This 
remains asserted as long as you do not encounter the STOP/JMP_ON_CS command.
1
—
Reserved
0
—
Reserved
79.13.2.23
DLL Status Register (DLLSR)
Offset
Register
Offset
DLLSR
12Ch
Function
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
DLLA_
LO...
SLVA_
LO...
DLLA_
RA...
DLLA_
FI...
0
DLLA_SLV_FINE_VAL 
DLLA_SLV_COARSE_VAL 
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
Fields
Field
Function
31-28
Reserved
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4851 / 5251


---
# 페이지 1992

Table continued from the previous page...
Field
Function
—
27-24
—
Reserved
23-16
—
Reserved
15
DLLA_LOCK
DLL A lock status
14
SLVA_LOCK
Slave high lock status
High-frequency slave delay chain locked. The field is configured when the slave decoder is updated with 
DLLCRA[SLV_UPD] and is reset after you configure SLV_UPD to 0.
13
DLLA_RANGE_
ERR
DLL master delay chain
The value 1 indicates that DLL master delay chain is working out of delay range because of incorrect 
DLL configuration.
12
DLLA_FINE_UN
DERFLOW
Fine delay chain underflow
The value 1 indicates that fine delay chain underflow has occurred.
11-8
—
Reserved
7-4
DLLA_SLV_FIN
E_VAL
Fine delay cells in slave delay chain
This value indicates the total number of fine delay cells (1 delay unit) selected in the slave delay chain.
3-0
DLLA_SLV_CO
ARSE_VAL
Coarse delay cells in slave delay chain
This value indicates the total number of coarse delay cells (16 delay units) selected in the slave delay 
chain.
79.13.2.24
Data Learning Configuration Register (DLCR)
Offset
Register
Offset
DLCR
130h
Function
This register is used for programming the data learning settings.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4852 / 5251


---
# 페이지 1993

• A flash memory device that supports data learning but cannot provide more than 10 bits of data learn pattern must be 
considered as non-DLP Flash. For Non-DLP flash devices, you must read at least 16 bits data learn pattern from a 
known location.
• You must program different learning pattern on the two data pins–IO1 and IO3. This is required to accommodate pessimistic 
data skew between the different IO lines.
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
Reserv
ed 
DL_NO
ND...
Reserved 
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
DLP_SEL_FA 
0
Reserved 
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
31-30
—
Reserved
29-26
—
Reserved
25
—
Reserved
24
DL_NONDLP_F
LSH
Data learning enabled for non-DLP flash memory
Configure the value of this field as 1 to enable data learning for flash memories that do not provide a data 
learning pattern.
For a non-DLP flash memory, execute a one-time data learning through the IPS to select a tap before an 
AHB read operation.
23-16
—
Reserved
15-14
DLP_SEL_FA
Selects pattern matching IO pads
00b - Pattern matching is ignored. This is only for debugging purpose and should not be 
programmed.
01b - IO1 is used for matching
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4853 / 5251


---
# 페이지 1994

Table continued from the previous page...
Field
Function
10b - IO3 is used for matching. This is only for debugging purpose and should not be 
programmed.
11b - Both IO1 and IO3 are used for pattern matching
13-8
—
Reserved
7-0
—
Reserved
79.13.2.25
Data Learning Status Flash Memory A Register (DLSR_FA)
Offset
Register
Offset
DLSR_FA
134h
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
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4854 / 5251


---
# 페이지 1995

Table continued from the previous page...
Field
Function
30-16
—
Reserved
15-8
POS_EDGE
DLP positive edge match signature for flash memory A
7-0
NEG_EDGE
DLP negative edge match signature for flash memory A
79.13.2.26
TX Buffer Status Register (TBSR)
Offset
Register
Offset
TBSR
150h
Function
This register contains information related to the transmit data buffer.
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
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4855 / 5251


---
# 페이지 1996

Table continued from the previous page...
Field
Function
15-9
—
Reserved
8-0
TRBFL
TX buffer fill level
This field contains the number of entries of 4 bytes each available in the TX buffer for the QuadSPI module 
to transmit to the serial flash memory device. The value of this field can reach maximum up to the total TX 
buffer size.
79.13.2.27
TX Buffer Data Register (TBDR)
Offset
Register
Offset
TBDR
154h
Function
This register provides access to the circular TX buffer of depth 256, so the total size is 256 * 4 bytes. This buffer provides the data 
written into it as write data for the page programming commands to the serial flash memory device. See Table 733 for the byte 
ordering scheme. A write transaction on the flash memory with data size of less than 32 bits leads to the removal of one data entry 
from the TX buffer. The valid bits are used and the rest of the bits are discarded.
Special write-access is permitted if:
• SR[TXFULL] = 0
 
This register can only be written when write access is granted by SFP block else bus transfer error is generated 
on write. Please refer to section TBDR register write lock
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
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4856 / 5251


---
# 페이지 1997

Fields
Field
Function
31-0
TXDATA
TX data
On write access, the data is written to the next available entry of the TX buffer and TBSR[TRBFL] is 
updated accordingly.
On a read access, the last data written to the register is returned.
79.13.2.28
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
31-8
—
Reserved
7-0
WMRK
Watermark for TX buffer
Determines the watermark for the TX buffer
When the number of available space in the TX buffer is greater than or equal to the number provided by 
WMRK (number of 4-byte entries), SR[TXWA] is asserted. For example, a value of 0x1 sets the watermark 
to 4 bytes, 0x2 sets it to 8 bytes, 0x3 sets it to 12 bytes, and so on. For details, see DMA usage.
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4857 / 5251


---
# 페이지 1998

Table continued from the previous page...
Field
Function
WMRK = 0 is invalid.
 
For IPS write with SFP enabled, this field must be programmed as per formula to prevent TX 
underflow: If data size in words >1, watermark=(TX FIFO size in words - data size in words) 
+1, If data size in words =1, watermark=(TX FIFO size in words - data size in words) 
  NOTE  
79.13.2.29
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
AWRA
CC 
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
Fields
Field
Function
31-29
—
Reserved
28
—
Reserved
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4858 / 5251


---
# 페이지 1999

Table continued from the previous page...
Field
Function
27
TXFULL
TX buffer full
Asserted when the FIFO level reaches TX buffer size
26
TXDMA
TX DMA
Asserted when the TXFIFO fill via DMA is active and DMA is requested or running
25
TXWA
TX buffer watermark available
Asserted when the number of available spaces in the TX buffer is greater than or equal to the value provided 
by TBCT[WMRK]
Example: When TBCT[WMRK]=1, SR[TXWA] is de-asserted when TX FIFO has 256+7(size of async 
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
Asserted when the RX buffer is full; that is, when RBSR[RDBFL] is equal to 32
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
AHB2FUL
AHB 2 buffer full
Asserted when AHB 2 buffer is full
12
AHB1FUL
AHB 1 buffer full
Asserted when the AHB 1 buffer is full
11
AHB 0 buffer full
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4859 / 5251


---
# 페이지 2000

Table continued from the previous page...
Field
Function
AHB0FUL
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
AWRACC
AHB write access
Asserted when AHB write access is enabled
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
79.13.2.30
Flag Register (FR)
Offset
Register
Offset
FR
160h
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4860 / 5251


---
# 페이지 2001

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
DLPFF 
0
Reserv
ed 
DLLAB
RT 
TBFF 
TBUF 
0
DLLU
NLCK 
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
AAEF 
AITEF 
AIBSE
F 
ABOF 
Reserv
ed 
CRCA
EF 
Reserv
ed 
PPWF 
0
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
DLPFF
Data learning pattern failure flag
This field is set when the DATA_LEARN instruction is encountered in a sequence, but no sampling point is 
found for the data learning pattern.
30
—
Reserved
29
—
Reserved
28
DLLABRT
DLL abort
1b - This field is set whenever DLL is unlocked while reading data from the flash memory.
27
TBFF
TX buffer fill flag
Before writing to the TX buffer, this field should be cleared. Then, it should be read back. If it is set, the TX 
buffer can include more data. If the field remains cleared, the TX buffer can be considered as full. See TX 
buffer operation for details.
26
TBUF
TX buffer underrun flag
This field is set if the module tries to pull data when the TX buffer is empty.. The IP command leading to the 
TX buffer underrun is continued (data sent to the serial flash memory device is undefined ). Here, a valid 
underrun means that it should have occurred during the transaction so that few bytes (that is, less than 4 
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4861 / 5251


---
# 페이지 2002

Table continued from the previous page...
Field
Function
bytes) are left in FIFO and the remaining are filled with "FFFFh". This field does not set if transfer is less than 
128 bits. The application must clear the TX buffer in response to this event by writing a 1 to MCR[CLR_TXF]. 
The application must clear the TX buffer in response to this event by writing a 1 to MCR[CLR_TXF].
25
—
Reserved
24
DLLUNLCK
DLL unlock
1b - This field is set whenever DLL unlock event occurs, irrespective of flash memory access.
23
ILLINE
Illegal instruction error flag
This field is set when an illegal instruction is encountered by the controller in any of the sequences. As 
soon as the field is set, you must assert MCR[SWRSTSD] and MCR[SWRSTHD]. That is, reset the flash 
memory and AHB domain after reconfiguring the correct sequence instruction. See Table 731 for a list of 
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
• If the RX buffer has up to RBCT[WMRK] valid entries, then the flag is cleared.
• If the RX buffer has more than RBCT[WMRK] valid entries and the RSER[RBDDE] field is not set 
(flag driven mode), an RX buffer POP event is triggered.
The flag remains set if the RX buffer contains more than RBCT[WMRK] valid entries after the RX buffer POP 
event is complete.
The flag is cleared if the RX buffer contains less than or equal to RBCT[WMRK] valid entries after the RX 
buffer POP event is complete.
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4862 / 5251


---
# 페이지 2003

Table continued from the previous page...
Field
Function
See the "Receive Buffer Drain Interrupt or DMA Request" section in Normal mode interrupt and DMA 
requests for details.
15
AAEF
AHB abort error flag
This flag can be set when AHB transaction in ongoing and any of the below conditions occur which may 
result in AHB error response (HRESP) generation:
• When Software abort is asserted from SPTRCLT[ABRT_CLR] during AHB read.
• During data learning pattern failure if any AHB transaction is ongoing. (FR[DLPFF])
• CRC or ECC error from flash memory during AHB transaction. (FR[CRCAEF])
• If AIBSEF flag is set during the AHB transfer. (FR[AIBSEF])
Software should clear this flag and other related flags in FR register (mentioned in points above) before 
initiating any new AHB transfer.
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
This is set when the size of the AHB access exceeds the size of the AHB buffer. This condition can occur only 
if BUFxCR[ADATSZ] is programmed incorrectly. The AHB command leading to this condition is continued 
until the number of entries according to BUFxCR[ADATSZ] have been read from the serial flash memory 
device. The content of the AHB buffer is not changed.
11
—
Reserved
10
CRCAEF
Sets when there is CRC or ECC error for flash memory A
0b - CRCEF interrupt is not generated.
1b - CRCEF interrupt is generated.
9
—
Reserved
8
PPWF
Page-program wait flag after flash memory write flag
This field indicates page-program wait flag after flash memory write.
7
—
Reserved
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4863 / 5251


---
# 페이지 2004

Table continued from the previous page...
Field
Function
6
IPIEF
IP command trigger could not be executed error flag
This is set when the SR[IP_ACC] and SR[AWRACC] fields are set (that is, an IP triggered command is 
currently executing) and any of the following conditions occurs:
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
79.13.2.31
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
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4864 / 5251


---
# 페이지 2005

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
DLPFI
E 
Reserved 
0
TBFIE 
TBUIE 
TBFD
E 
DLLUL
IE 
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
AAIE 
AITIE 
AIBSI
E 
ABOIE 
Reserv
ed 
CRCAI
E 
Reserv
ed 
PPWI
E 
Reserv
ed 
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
DLPFIE
Data learning pattern failure interrupt enable
Triggered by DLPFF flag in FR.
0b - No DLPFF interrupt is generated.
1b - DLPFF interrupt is generated.
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
This interrupt should not be enabled when using SFP functionality because it causes QSPI BUSY SFM to 
go high and keeps SFP to generate any transaction over to QSPI.
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
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4865 / 5251


---
# 페이지 2006

Table continued from the previous page...
Field
Function
0b - No DMA request is generated
1b - DMA request is generated
24
DLLULIE
DLL unlock interrupt enable
1b - Write 1 to this to enable generation of interrupt on DLL unlock event.
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
15
AAIE
AHB abort error interrupt enable
Triggered by AAEF flags in FR.
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4866 / 5251


---
# 페이지 2007

Table continued from the previous page...
Field
Function
0b - No AAEF interrupt is generated
1b - AAEF interrupt is generated
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
CRCAIE
CRC and ECC interrupt enable for flash memory A
0b - CRCAEF interrupt is not generated.
1b - CRCAEF interrupt is generated.
9
—
Reserved
8
PPWIE
Page-program wait interrupt flag
This field indicates page-program wait interrupt.
0b - No PPWIE interrupt is generated
1b - PPWIE interrupt is generated
7
—
Reserved
6
IPIEIE
IP command trigger during IP access error interrupt enable flag
This field indicates IP command trigger during IP access error interrupt enable flag.
0b - No IPIEF interrupt is generated
1b - IPIEF interrupt is generated
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4867 / 5251


---
# 페이지 2008

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
79.13.2.32
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
Reserved 
0
Reserv
ed 
Reserv
ed 
PREF
ETC...
ABRT_
CLR 
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
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4868 / 5251


---
# 페이지 2009

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
19
—
Reserved
18
—
Reserved
17
PREFETCH_DI
S
Prefetch disable
This field should be configured to disable the prefetch mechanism of receiver. It is not based on dynamic 
programming. Therefore, it should be programmed initially at once. When this field is set, then during an 
ongoing flash memory read, any subsequent AHB read is checked for buffer hit. However, after the end of 
flash memory read, as soon as chip select is deasserted, any subsequent AHB read results in flushing of 
the current AHB buffer data and issues fresh flash memory transaction if the AHB buffer data is not updated 
with the flash memory.
16
ABRT_CLR
Flash memory Abort/AHB buffer clear
This is a dynamic field. Writing a 1 to it, irrespective of the prefetch disable, clears the AHB buffer pointers 
and also aborts any ongoing flash memory transaction (if any) and rejects any ongoing AHB read with an 
error response (if any).
QuadSPI sets this field to 0 after clearing the AHB buffer pointers.
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
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4869 / 5251


---
# 페이지 2010

79.13.2.33
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
79.13.2.34
Serial Flash Memory A2 Top Address Register (SFA2AD)
Offset
Register
Offset
SFA2AD
184h
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4870 / 5251


---
# 페이지 2011

Function
This register provides the address mapping for serial flash memory A2. The difference between SFA2AD[TPADA2] and 
SFA1AD[TPADA1] defines the size of the memory map for serial flash memory A2.
Special write-access is permitted if:
• SR[IP_ACC] = 0
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
79.13.2.35
Data Learn Pattern Register (DLPR)
Offset
Register
Offset
DLPR
190h
Function
This register contains the information of the data to be used for data learning.
Special write-access is permitted if:
• SR[IP_ACC] = 0
• SR[AHB_ACC] = 0
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4871 / 5251


---
# 페이지 2012

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
DLPV 
W
Reset
1
0
1
0
1
0
1
0
0
1
0
1
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
DLPV 
W
Reset
0
0
1
1
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
1
1
Fields
Field
Function
31-0
DLPV
Data learning pattern value
This value is used for data learning in the DDR and DQS modes. For example, if you request for more than 
32 bits of data learning, the value is repeated in the register. For example, if 64-bit data learning is requested 
by any flash memory and the value of DLPR is aa55_3443, then the 64-bit value is aa55_3443_aa55_3443.
This value is used for data learning in SDR/DDR modes along with DATA_LEARN instruction. Different 
patterns can be matched at selected IOs. That is, IO1 and IO3 using DLCR[DLP_SEL_FA], DLPR[31:16] 
for IO3, and DLPR[15:0] for IO1. DLP pattern for IO1 and IO3 should be stored, bit-wise, in the little 
endian format.
For details, see Data learning.
79.13.2.36
Flash Memory A Failing Address Status Register (FAILA_ADDR)
Offset
Register
Offset
FAILA_ADDR
194h
Function
This register provides the flash memory address where data learning or parity error has occurred.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4872 / 5251


---
# 페이지 2013

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
ADDR 
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
ADDR
Failing address for flash memory A
79.13.2.37
RX Buffer Data Register (RBDR0 - RBDR31)
Offset
For a = 0 to 31:
Register
Offset
RBDRa
200h + (a × 4h)
Function
These registers provide access to individual entries in the RX buffer. See Table 733 for the byte ordering scheme.
RBDR0 corresponds to the actual position of the read pointer within the RX buffer. The number of valid entries available depends 
on the number of RX buffer entries implemented and on the number of valid buffer entries available in the RX buffer.
Example 1 - RX buffer filled completely with 32 words: In this case, the address range for valid read access extends from RBDR0 
to RBDR31 RBDR63.
Example 2 - RX buffer filled with five valid words: RX buffer fill level of RBSR[RDBFL] is 5. In this case, access to RBDR4 provides 
the last valid entry.
Any access beyond the range of valid RX buffer entries provides undefined results.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4873 / 5251


---
# 페이지 2014

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
79.13.2.38
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
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4874 / 5251


---
# 페이지 2015

Fields
Field
Function
31-0
KEY
Key to lock or unlock the LUT
The key is 0x5AF05AF0 and the read value is always 0x5AF05AF0.
79.13.2.39
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
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4875 / 5251


---
# 페이지 2016

Table continued from the previous page...
Field
Function
0
LOCK
Lock LUT
Locks the LUT when the following conditions are met:
• This register is written just after the LUT Key Register (LUTKEY).
• The LUT key register is written with the 0x5AF05AF0 key.
79.13.2.40
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
engine executes the instructions in these sequences to generate a valid serial flash memory transaction. There are a total of 80 
LUT registers. These 80 registers are divided into groups of 5 registers that make a valid sequence. Therefore, LUT[0], LUT[5], 
LUT[10] ..... LUT[75] are the starting registers of a valid sequence. Each of these sets of 5 registers can have a maximum of 10 
instructions. Reset value of the register shown below is only applicable to LUT2 to LUT79. A maximum of 16 sequences can be 
defined at one time. See LUT that describes the LUT registers in detail.
Special write-access is permitted if the LUT is unlocked.
This register is access controlled and can only be programmed by privilege masters. Last six LUT SEQID locations should be used 
for programming SEQID for atomic commands (where flash's internal config region is accessed) like flash erase etc. where data 
transfer is not required. These 6 SEQID can be send to QSPI using only FRAD0 and can't be qualified using any other FRAD. For 
details, see Atomic commands considerations.
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
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4876 / 5251


---
# 페이지 2017

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
11b - 8 Pads
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
11b - 8 Pads
7-0
OPRND0
Operand for INSTR0
79.13.2.41
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
engine executes the instructions in these sequences to generate a valid serial flash memory transaction. There are a total of 80 
LUT registers. These 80 registers are divided into groups of 5 registers that make a valid sequence. Therefore, LUT[0], LUT[5], 
LUT[10] ..... LUT[75] are the starting registers of a valid sequence. Each of these sets of 5 registers can have a maximum of 10 
instructions. Reset value of the register shown below is only applicable to LUT2 to LUT79. A maximum of 16 sequences can be 
defined at one time. See LUT that describes the LUT registers in detail.
Special write-access is permitted if the LUT is unlocked.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4877 / 5251


---
# 페이지 2018

This register is access controlled and can only be programmed by privilege masters. Last six LUT SEQID locations should be used 
for programming SEQID for atomic commands (where flash's internal config region is accessed) like flash erase etc. where data 
transfer is not required. These 6 SEQID can be send to QSPI using only FRAD0 and can't be qualified using any other FRAD. For 
details, see Atomic commands considerations.
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
11b - 8 Pads
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
11b - 8 Pads
7-0
OPRND0
Operand for INSTR0
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4878 / 5251


---
# 페이지 2019

79.13.2.42
LUT Register (LUT2 - LUT79)
Offset
For a = 2 to 79:
Register
Offset
LUTa
310h + (a × 4h)
Function
A sequence of instruction-operand pairs may be pre-populated in the LUT according to the device connected on board. Each 
instruction-operand pair is of 16 bits (2 bytes) each. Every sequence preprogrammed by Program Sequence Engine in the LUT 
is referred to by its index. The LUT registers act as lookup tables for sequences of instructions. The programmable sequence 
engine executes the instructions in these sequences to generate a valid serial flash memory transaction. There are a total of 80 
LUT registers. These 80 registers are divided into groups of 5 registers that make a valid sequence. Therefore, LUT[0], LUT[5], 
LUT[10] ..... LUT[75] are the starting registers of a valid sequence. Each of these sets of 5 registers can have a maximum of 10 
instructions. Reset value of the register shown below is only applicable to LUT2 to LUT79. A maximum of 16 sequences can be 
defined at one time. See LUT that describes the LUT registers in detail.
Special write-access is permitted if the LUT is unlocked.
This register is access controlled and can only be programmed by privilege masters. Last six LUT SEQID locations should be used 
for programming SEQID for atomic commands (where flash's internal config region is accessed) like flash erase etc. where data 
transfer is not required. These 6 SEQID can be send to QSPI using only FRAD0 and can't be qualified using any other FRAD. For 
details, see Atomic commands considerations.
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
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4879 / 5251


---
# 페이지 2020

Table continued from the previous page...
Field
Function
01b - 2 Pads
10b - 4 Pads
11b - 8 Pads
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
11b - 8 Pads
7-0
OPRND0
Operand for INSTR0
79.13.2.43
Flash Region Start Address (FRAD0_WORD0 - FRAD7_WORD0)
Offset
For n = 0 to 7:
Register
Offset
FRADn_WORD0
800h + (n × 20h)
Function
This register is access controlled and can only be programmed by privilege masters.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4880 / 5251


---
# 페이지 2021

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
STARTADR 
W
Reset
0
0
0
0
0
0
0
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
31-16
STARTADR
Start Address
Specifies the specific flash memory region starting address (around 64 KB boundary)
15-0
—
Reserved
79.13.2.44
Flash Region End Address (FRAD0_WORD1 - FRAD7_WORD1)
Offset
For n = 0 to 7:
Register
Offset
FRADn_WORD1
804h + (n × 20h)
Function
This register is access controlled and can only be programmed by privilege masters.
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
ENDADR 
W
Reset
0
0
0
0
0
0
0
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
1
1
1
1
1
1
1
1
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4881 / 5251


---
# 페이지 2022

Fields
Field
Function
31-16
ENDADR
End Address
Specifies the specific flash memory region end address (around 64 KB boundary)
15-0
—
Reserved
79.13.2.45
Flash Region Privileges (FRAD0_WORD2 - FRAD7_WORD2)
Offset
For n = 0 to 7:
Register
Offset
FRADn_WORD2
808h + (n × 20h)
Function
This register is access controlled and can only be programmed by privilege masters.
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
EALO 
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
MD1ACP 
MD0ACP 
W
Reset
0
0
0
0
0
0
0
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
—
Reserved
29-24
EALO
Exclusive Access Lock Owner
When FRADn_WORD3[EAL] = 11, this field indicates the domain/master ID that owns the exclusive 
access lock.
23-6
Reserved
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4882 / 5251


---
# 페이지 2023

Field
Function
—
5-3: MD1ACP
2-0: MD0ACP
Master Domain Access Control Policy
This field define the access restrictions for respective Master Domain 0 and 1 corresponding to this FRAD 
region. Write permissions are decided based on secure and privilege attributes of current transaction. Read 
access is not restricted. This field can not be programmed if MDAD registers are not valid. If EAL is being 
written in same cycle (10 or 11), or if FRAD_WORD3 [LOCK] bits are written as 11. If LOCK bits are written 
as 10 then this field can be programmed only if Master ID matches the ID check of respective MDAD queue. 
If MDAD descriptor is not valid then respective MDxACP also becomes read-only.
Table 768. Field value mapping
Policy
Secure privilege
Secure user
Non 
secure privilege
Non secure user
111
Read/Write
Read
Read/Write
Read
110
Read/Write
Read/Write
Read/Write
Read/Write
101
Read/Write
Read
Read
Read
100
Read/Write
Read/Write
Read
Read
0xx
Read
Read
Read
Read
 
The software must program the value 101 for MDACP fields for FRAD0 as this FRAD has 
access to all the atomic instructions. For details, see Atomic commands considerations.
  NOTE  
79.13.2.46
Flash Region Lock Control (FRAD0_WORD3 - FRAD7_WORD3)
Offset
For n = 0 to 7:
Register
Offset
FRADn_WORD3
80Ch + (n × 20h)
Function
This register is access controlled and can only be programmed by privilege masters.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4883 / 5251


---
# 페이지 2024

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
LOCK 
0
EAL 
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
This field indicates whether the FRAD Descriptor for a specific flash region is valid. This field can not be 
written in same cycle if EAL field is being written as 10 or 11.
 
You must enable this field after programming FRAD0_WORD0, FRAD0_WORD1, 
FRAD0_WORD2 and FRAD0_WORD3 registers.
  NOTE  
0b - FRAD-Assignment is invalid
1b - FRAD-Assignment is valid
30-29
LOCK
Descriptor Lock
This field enables masking of accidental write on FRAD registers. Lock is enabled/disabled by Secure/
Privileged master. Lock functionality does not affects the EAL bits of FRAD. They can still be written 
even if FRAD descriptors are locked.
00b-01b - Lock disabled. Descriptor registers can be written by any master
10b - Lock enabled. Descriptors are read-only. MDnACP fields can be programmed only by the 
master with ID matching the MID check of their respective Target group MDAD. If the Target 
group MDAD is not valid then MDnACP fields also become read-only.
11b - Lock enabled. Descriptor registers are read-only.
28-26
—
Reserved
25-24
EAL
Exclusive Access Lock
This field provides exclusive write lock over a FRAD region based on MDnACP.
00b - No lock. Write permissions available for all masters based on their MDxACP evaluation.
01b - NA
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4884 / 5251


---
# 페이지 2025

Table continued from the previous page...
Field
Function
10b - Lock enabled. Write permissions revoked for all domains. It can only be changed to 11b and 
can't directly be changed to 00b.
11b - Lock enabled. Exclusive write permission for master with master ID given in 
FRADn_WORD3[EALO] fields based on its MDxACP evaluation. Write disabled for other masters. 
Exclusive lock can be taken by a master only if it its ID matches the master ID check of any of 
the MDAD target queue, which is valid. MDxACP field corresponding to that target queue is not 
programmed as 0b. when a master writes 11b on this field it will be written only if above condition 
is met and then the master ID will be stored in FRADn_WORD3[EALO]. No transfer error will be 
generated in case the master does not satisfies the check.
23-0
—
Reserved
79.13.2.47
Flash Region Compare Address Status (FRAD0_WORD4 - FRAD7_WORD4)
Offset
For n = 0 to 7:
Register
Offset
FRADn_WORD4
810h + (n × 20h)
Function
This register is access controlled and can only be programmed by privilege masters.
 
Any write access to these registers will result in bus transfer error
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
CMP_ADDR 
W
Reset
0
0
0
0
0
0
0
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
CMP_ADDR 
W
Reset
0
0
0
0
0
0
0
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
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4885 / 5251


---
# 페이지 2026

Fields
Field
Function
31-0
CMP_ADDR
Capture Address
This field indicates the 32-bit start address of the last transaction which lies inside the address range of 
this FRAD descriptor.
79.13.2.48
Flash Region Compare Status Data (FRAD0_WORD5 - FRAD7_WORD5)
Offset
For n = 0 to 7:
Register
Offset
FRADn_WORD5
814h + (n × 20h)
Function
This register is access controlled and can only be programmed by privilege masters.
 
Any write access to these registers will result in bus transfer error
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
CMPV
ALID 
CMP_
ERR 
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
CMP_
PA 
CMP_
SA 
CMP_MDID 
W
Reset
0
0
0
0
0
0
0
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
CMPVALID
Comparison Valid
This field indicates the validity of flash region specific comparison check.
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4886 / 5251


---
# 페이지 2027

Table continued from the previous page...
Field
Function
0b - Access result/status not available
1b - Access result/status is available
29
CMP_ERR
Comparison Error
This field indicates the error status (based on secure/privilege attributes checked with MDxACP permissions 
or exclusive access lock as programmed in FRAD) for flash region specific comparison check for 
last transaction.
When this field is set, it can be cleared by writing '1' to W1C field of ERRSTAT register. It will update new 
value only after the error field has been cleared.
0b - No error
1b - Access error
28-8
—
Reserved
7
CMP_PA
Capture Privilege Attribute
Capture Privilege attribute of last transaction which passed the address check for this FRAD.
0b - Non-privilege transaction
1b - Privilege transaction
6
CMP_SA
Capture Secure Attribute
Capture Secure attribute of last transaction which passed the address check for this FRAD.
0b - Non-secure transaction
1b - Secure transaction
5-0
CMP_MDID
Capture MDID Value
Capture master ID (MDID) value of the last transaction which passed the address check for this FRAD.
79.13.2.49
Target Group n Master Domain Access Descriptor (TG0MDAD - TG1MDAD)
Offset
Register
Offset
TG0MDAD
900h
TG1MDAD
910h
Function
This register is access controlled and can only be programmed by privilege masters.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4887 / 5251


---
# 페이지 2028

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
0
LCK 
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
SA 
0
MASK
TYPE 
MASK 
MIDMATCH 
W
Reset
0
0
0
0
0
0
0
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
Indicates whether MDAD Descriptor for the target group n is valid.
0b - MDAD-Assignment is invalid
1b - MDAD-Assignment is valid
30
—
Reserved
29
LCK
Descriptor Lock
This field provides a means to make the MDAD descriptor read-only.
0b - Lock disabled. Registers can be written.
1b - Lock enabled. Registers are read-only.
28-16
—
Reserved
15-14
SA
Secure Attribute
Defines the secure attribute selection criteria for entry into descriptor queue..
00b - NA. This option should not be used. Allows the bus attribute for this master to non-secure 
only
01b - Allow the bus attribute for this master to non-secure only
10b - Allow the bus attribute for this master to secure only
11b - Allow the bus master's attribute: Both secure and non-secure
13
—
Reserved
12
Mask Type
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4888 / 5251


---
# 페이지 2029

Table continued from the previous page...
Field
Function
MASKTYPE
0b - ANDed mask
1b - ORed mask
11-6
MASK
Mask
Defines the 6-bit mask value for the ID-Match comparison
5-0
MIDMATCH
Master ID Reference
Specifies the reference value of the Master-ID (MID) for MID-comparison
79.13.2.50
Target Group n SFAR Address (TG0SFAR - TG1SFAR)
Offset
Register
Offset
TG0SFAR
904h
TG1SFAR
914h
Function
Flash memory start address of the transaction in this target group queue.
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
SFARADDR 
W
Reset
0
0
0
0
0
0
0
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
SFARADDR 
W
Reset
0
0
0
0
0
0
0
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
SFARADDR
SFAR Address
Flash memory start address of the transaction which qualified into this target group queue.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4889 / 5251


---
# 페이지 2030

79.13.2.51
Target Group n SFAR Status (TG0SFARS - TG1SFARS)
Offset
Register
Offset
TG0SFARS
908h
TG1SFARS
918h
Function
Target group n SFAR status.
 
This register can only be read if the master reading the register passes the security checks set in TGnMDAD[SA] 
fields or if MDAD descriptor is not valid. Else this register will be read as 0. It will also read as 0 if TGnMDAD[SA] 
bits in descriptor are set as 00.
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
VLD 
ERR 
CLR 
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
0
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
PA 
0
SA 
0
TG_MID 
W
Reset
0
0
0
0
0
0
0
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
Indicates whether the SFAR Address for the target group n is valid and queue is busy. This bit will not be 
set when ERR bit is set.
0b - SFAR-Assignment is invalid
1b - SFAR-Assignment is valid
30
ERR
Error
Indicates whether the SFAR address stored by a Master is with required access attributes for this target 
group descriptor.
0b - SFAR with required attributes
1b - SFAR without required attributes
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4890 / 5251


---
# 페이지 2031

Table continued from the previous page...
Field
Function
29
CLR
Clear
Clears the SFAR Status register. This register can only be cleared by the master having security attribute 
defined by TGnMDAD[SA].
After clearing if there is any valid transaction present in MDAD queue, it will again get updated in this register 
else it will be cleared. It will not be cleared if TGxMDAD[SA] bits are set to 00.
28-13
—
Reserved
12
PA
Privileged Attribute
Privilege attribute of the master which wrote the SFAR register.
0b - Non-privileged
1b - Privileged
11
—
Reserved
10
SA
Secure Attribute
Secure attribute of the master which wrote the SFAR register.
0b - Non-secure
1b - Secure
9-6
—
Reserved
5-0
TG_MID
Transaction Master ID
Indicates the Master-ID of a transaction which programmed the SFAR registers with required attributes.
79.13.2.52
Target Group n IPCR Status (TG0IPCRS - TG1IPCRS)
Offset
Register
Offset
TG0IPCRS
90Ch
TG1IPCRS
91Ch
Function
Target group n IPCR status.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4891 / 5251


---
# 페이지 2032

 
This register can only be read if the master reading the register passes the security checks set in TGnMDAD[SA] 
fields or if MDAD descriptor is not valid. Else this register will be read as 0. It will also read as 0 if TGnMDAD[SA] 
bits in descriptor are set as 00.
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
VLD 
ERR 
CLR 
0
ARB_
UNL...
ARB_
LOCK 
PAR 
SEQID 
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
Fields
Field
Function
31
VLD
Valid
Indicates whether the IPCR-IDATZ, IPCR-SEQID and PAR stored in this target group queue is valid and 
queue is locked. This bit will not be set in case ERR is set.
0b - IPCR-assignment is invalid
1b - IPCR-assignment is valid and queue is locked.
30-29
ERR
Error
Indicates whether the IPCR stored by a Master with required access attributes wrt target group MDAD
00b - IPCR programming with required attributes
01b - IPCR-DATZ programming without required attributes
10b - IPCR-SEQID programming without required attributes
11b - IPCR-DATZ and SEQID both programming without required attributes
28
CLR
Clear
Clears the status in IPCR Status register.
This register can only be cleared by the master having security attribute defined by TGnMDAD[SA]. After 
clearing if there is any valid transaction present in MDAD queue it will again get updated in this register else 
it will be cleared. It will not be cleared if TGxMDAD[SA] bits are set to 00.
27-23
—
Reserved
22
Arbitration Unlock
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4892 / 5251


---
# 페이지 2033

Table continued from the previous page...
Field
Function
ARB_UNLOCK
Specifies if the arbitration unlock is requested for TGn.
0b - No effect
1b - Arbitration unlock is requested
21
ARB_LOCK
Arbitration Lock
Specifies if the arbitration lock is requested for TGn.
0b - No effect
1b - Arbitration lock is requested
20
PAR
Parallel Mode Enable Value
Indicates the parallel mode enable value programmed in the target group queue.
19-16
SEQID
SEQID Value
Indicates the SEQID value programmed in target group queue.
15-0
IDATSZ
IDATSZ Value
Indicates the IDATSZ value programmed in target group queue.
79.13.2.53
Master Global Configuration (MGC)
Offset
Register
Offset
MGC
920h
Function
This register is access controlled. It can only be programmed by master with master ID equal to 000011b. For MGC, MRC and 
MTO registers access checks master ID is being used. For transaction level checks inside MDAD and FRAD domain IDs are 
being used.
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
GVLD 
0
GVLD
MDAD 
0
GVLD
FRAD 
0
W
Reset
1
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
GCLCK 
0
GCLCKMID 
W
Reset
0
0
0
0
0
0
0
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
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4893 / 5251


---
# 페이지 2034

Fields
Field
Function
31
GVLD
Global Valid access control
0b - Access controls are disabled. No descriptor comparison check. All transactions are allowed.
1b - Access controls are enabled.
30
—
Reserved
29
GVLDMDAD
Global Valid MDAD
0b - MDADs are disabled
1b - MDADs are enabled
28
—
Reserved
27
GVLDFRAD
Global Valid FRAD
0b - FRADs are disabled
1b - FRADs are enabled
26-12
—
Reserved
11-10
GCLCK
Global Configuration Lock
This field provides a mechanism to limit write access to descriptors specific registers (MGC, MRC and 
MTO registers).
00b - Global Lock disabled. Registers can be written based on individual register access attribute.
01b - NA
10b - Lock enabled. Only the global configuration lock owner can write to the registers.
11b - Lock enabled. All registers are read only until unlocked
9-6
—
Reserved
5-0
GCLCKMID
Global configuration Lock Owner Status
This fields specifies the 6-bit Master-ID of Global configuration Lock owner (which set 
MGC[GCLCK]=10). Input value of Global Master-ID is provided by sideband signals.
79.13.2.54
Master Read Command (MRC)
Offset
Register
Offset
MRC
924h
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4894 / 5251


---
# 페이지 2035

Function
This register is access controlled. It can only be programmed by master with master ID equal to 000011b.
 
In case of Sequence Auto Join instruction in LUT, SFP will parse only first sequence. Second sequence will not be 
parsed for checking Read commands.
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
VLDC
MD03 
READ_CMD3 
0
VLDC
MD02 
READ_CMD2 
W
Reset
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
READ_CMD1 
0
READ_CMD0 
W
Reset
0
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
1
1
Fields
Field
Function
31
—
Reserved
30
VLDCMD03
Valid command
0b - READ_CMD3 value invalid
1b - READ_CMD3 value valid
29-24
READ_CMD3
Read Command 3
Programmes the additional READ Instruction/Command encoding information, if applicable
23
—
Reserved
22
VLDCMD02
Valid command
0b - READ_CMD2 value invalid
1b - READ_CMD2 value valid
21-16
READ_CMD2
Read Command 2
Stores the existing instruction—DATA_LEARN command encoding information. Can be overwritten with 
additional read command, if required.
15-14
—
Reserved
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4895 / 5251


---
# 페이지 2036

Table continued from the previous page...
Field
Function
13-8
READ_CMD1
Read Command 1
Stores the existing instruction—READ_DDR command encoding information.
7-6
—
Reserved
5-0
READ_CMD0
Read Command 0
Stores the existing instruction—READ command encoding information.
79.13.2.55
Master Timeout (MTO)
Offset
Register
Offset
MTO
928h
Function
This register is access controlled. It can only be programmed by master with master ID equal to 000011b.
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
WRITE_TO 
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
WRITE_TO 
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
WRITE_TO
Write Timeout
Maximum timeout value to abort the ongoing write or read command. The timeout counter starts after 
the access from any target queue has won the arbitration and QSPI is IDLE (FSM_STAT state field is 
not 00). SFP queue is cleared once this timeout value has been reached and interrupt is generated if 
enabled.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4896 / 5251


---
# 페이지 2037

79.13.2.56
FlashSeq Request (FLSEQREQ)
Offset
Register
Offset
FLSEQREQ
92Ch
Function
This register is access controlled and can only be programmed by privilege masters.
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
0
CLR 
0
TIMEO
UT 
0
0
CMD 
0
SEQID 
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
0
FRAD 
0
ARB_
LOCK 
PA 
SA 
0
REQ_
TG 
REQ_MID 
W
Reset
0
0
0
0
0
0
0
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
Indicates whether the FlashSeq request status is valid
0b - Status is invalid
1b - Status is valid
30
—
Reserved
29
CLR
Clear
Clears the status
28
—
Reserved
27
TIMEOUT
Timeout Error Status
Timeout error status of last executed FlashSeq request.
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4897 / 5251


---
# 페이지 2038

Table continued from the previous page...
Field
Function
0b - Instruction completed without timeout error
1b - Instruction aborted after timeout error
26-25
—
Reserved
24-23
—
Reserved
22
CMD
Instruction Type
Instruction type of last executed FlashSeq request.
0b - Read Instruction Sequence
1b - Non-Read Instruction Sequence
21-20
—
Reserved
19-16
SEQID
Sequence ID
Sequence ID of last executed FlashSeq request.
15
—
Reserved
14-12
FRAD
Flash Region Descriptor Number
Flash Region specific number (FRAD) of last executed FlashSeq request.
This will remain 0 in case of read transfers.
11
—
Reserved
10
ARB_LOCK
Arbitration Lock
Arbitration lock status for last completed request.
0b - Arbitration was not locked
1b - Arbitration was locked
9
PA
Privilege Attribute
Privilege attribute of last executed FlashSeq request.
0b - Non-privilege Transaction
1b - Privilege Transaction
8
Secure Attribute
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4898 / 5251


---
# 페이지 2039

Table continued from the previous page...
Field
Function
SA
Secure attribute of last executed FlashSeq request.
0b - Non-secure Transaction
1b - Secure Transaction
7
—
Reserved
6
REQ_TG
FlashSeq Request Target Group
Target group queue from which last executed transaction passed.
0b - TG0
1b - TG1
5-0
REQ_MID
FlashSeq Request Master ID
Indicates the master-ID of last executed FlashSeq request.
79.13.2.57
FSM Status (FSMSTAT)
Offset
Register
Offset
FSMSTAT
930h
Function
This register is access controlled and can only be programmed by privilege masters.
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
0
ARB_
LOCK 
CMD 
W
Reset
0
0
0
0
0
0
0
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
MID 
0
STATE 
W
Reset
0
0
0
0
0
0
0
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
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4899 / 5251


---
# 페이지 2040

Fields
Field
Function
31
VLD
Valid
Indicates whether the FSM Status is valid.
0b - Status is invalid. No IPS transfer is queued.
1b - Status is valid. IPS transfer is queued or execution on QuadSPI.
30-18
—
Reserved
17
ARB_LOCK
Arbitration Lock
Arbitration lock status for present request.
0b - Arbitration not locked
1b - Arbitration locked
16
CMD
Command
Instruction type of currently initiated Flash transaction on QuadSPI.
0b - Read instruction sequence
1b - Non-read instruction sequence
15-14
—
Reserved
13-8
MID
Master ID
Indicates the Master-ID of the currently initiated FlashSeq transaction on QuadSPI.
7-2
—
Reserved
1-0
STATE
FSM State Status
00b - Transaction is Queued, but QuadSPI is busy with AHB transfer, any previous DMA 
transaction is ongoing, any residue data left in RDBFL or if any interrupt is pending..
01b - TBDR lock is open. IPS master can write in TBDR.
10b - Write transfer is triggered. SEQID is written to QuadSPI.
11b - Read transfer is triggered. SEQID is written to QuadSPI.
79.13.2.58
IPS Error (IPSERROR)
Offset
Register
Offset
IPSERROR
934h
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4900 / 5251


---
# 페이지 2041

Function
This register contains the error status of IPS write on SFAR or IPCR registers if they are not qualified for any of the target 
group queues.
This register is access controlled and can only be programmed by privilege masters.
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
CLR 
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
0
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
FRAD
PROG 
MDAD
PROG 
TG1MI
D 
TG0MI
D 
TG1S
EC 
TG0S
EC 
TG1LC
K 
TG0LC
K 
0
MID 
W
Reset
0
0
0
0
0
0
0
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
—
Reserved
29
CLR
Clear
Clear the status of IPS Error register.
28-16
—
Reserved
15
FRADPROG
FRAD Descriptor Program Status
0b - Some or all of the FRAD descriptors are programmed
1b - None of the FRAD descriptors are programmed
14
MDADPROG
TG/MDAD Descriptor Program Status
0b - One or both of target group descriptors programmed
1b - None of the target group descriptors are programmed and valid
13-12
TGnMID
TGn Master-ID Status
0b - TGn master-ID check passed
1b - TGn master-ID check failed
11-10
TGnSEC
TGn Security Status
0b - Security attribute check passed for TGn
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4901 / 5251


---
# 페이지 2042

Table continued from the previous page...
Field
Function
1b - Security attribute check failed for TGn
9-8
TGnLCK
TGn Lock
0b - TGn queue SEQID is not written yet.
1b - TGn queue SEQID is written and queue is locked
7-6
—
Reserved
5-0
MID
IPS DID Master ID
IPS Master ID for the transaction which generated this IPS transfer error.
79.13.2.59
Error Status (ERRSTAT)
Offset
Register
Offset
ERRSTAT
938h
Function
This register is access controlled and can only be programmed by privilege masters.
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
TO_
ERR 
TG1IP
CR 
TG0IP
CR 
TG1S
FAR 
TG0S
FAR 
IPS_
ERR 
FRAD
7ACC 
FRAD
6ACC 
FRAD
5ACC 
FRAD
4ACC 
FRAD
3ACC 
FRAD
2ACC 
FRAD
1ACC 
FRAD
0ACC 
FRAD
MTCH 
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
Reset
0
0
0
0
0
0
0
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
31-15
Reserved
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4902 / 5251


---
# 페이지 2043

Table continued from the previous page...
Field
Function
—
14
TO_ERR
Timeout Error
This field is set if any flash transaction generated on QuadSPI results in timeout error and is aborted by 
SFP module.
This field can be cleared by writing 1 to FLSEQREQ[CLR].
0b - No timeout Error generated
1b - Timeout error is generated
13-12
TGnIPCR
TGn IPCR Error
This field is set if any IPCR write generates error while being written to Target group queue.
This field can be cleared by writing 1 to TGnIPCRS[CLR].
0b - No Error generated
1b - Error is generated
11-10
TGnSFAR
TGn SFAR Error
This field is set if any SFAR write generates error while being written to Target group queue.
This field can be cleared by writing 1 to TGnSFARS[CLR].
0b - No Error generated
1b - Error is generated
9
IPS_ERR
IPS Error
Some common error occurred and IPS bus transfer error is also generated.
The details of the IPS error can be found in IPSERROR register. This field can be cleared by writing 1 
to IPSERROR[CLR].
0b - No Error generated
1b - Error is generated
8-1
FRADnACC
FRADn Access Error
This bit is set when the transaction address lies within the address range of this FRAD but it does not qualify 
the access permission checks for this FRAD or this FRAD was under exclusive lock (FRADn_WORD3[EAL] 
= 10 or 11) by another master. It may also be set if the transaction address qualifies for multiple 
FRAD regions.
0b - No valid Error transaction
1b - Transaction is with error and target queue is cleared
0
FRADMTCH
No FRAD Match Error
Transaction address does not lie within address range of any FRAD descriptor.
0b - No Error generated
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4903 / 5251


---
# 페이지 2044

Table continued from the previous page...
Field
Function
1b - Transaction does not lie within any FRAD address range and error is generated
79.13.2.60
Interrupt Enable (INT_EN)
Offset
Register
Offset
INT_EN
93Ch
Function
This register is access controlled and can only be programmed by privilege masters.
 
In case Queue Specific Error Interrupt bits (TG0SFAR,TG1SFAR,TG0IPCR,TG1IPCR) are enabled, ensure that 
the core executing interrupt handler can clear the Queue specific TGxSFARS and TGxIPCRS registers only when 
core's security attribute matches the queue. In case there is a mismatch in security attribute, you must change the 
TGMDADx.SA attribute of that queue to match the core SA attribute. After that, core can clear the error and then 
revert the changes in TGMDADx.SA field.
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
W
Reset
0
0
0
0
0
0
0
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
TO_
ERR 
TG1IP
CR 
TG0IP
CR 
TG1S
FAR 
TG0S
FAR 
IPS_
ERR 
FRAD
7ACC 
FRAD
6ACC 
FRAD
5ACC 
FRAD
4ACC 
FRAD
3ACC 
FRAD
2ACC 
FRAD
1ACC 
FRAD
0ACC 
FRAD
MTCH 
W
Reset
0
0
0
0
0
0
0
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
31-15
—
Reserved
14
TO_ERR
Timeout Error Interrupt Enable
0b - Interrupt disabled
1b - Interrupt enabled
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4904 / 5251


---
# 페이지 2045

Table continued from the previous page...
Field
Function
13-12
TGnIPCR
TGn IPCR Error Interrupt Enable
0b - Interrupt disabled
1b - Interrupt enabled
11-10
TGnSFAR
TGn SFAR Error Interrupt Enable
0b - Interrupt disabled
1b - Interrupt enabled
9
IPS_ERR
IPS Error Interrupt Enable
0b - Interrupt disabled
1b - Interrupt enabled
8-1
FRADnACC
FRADn Access Error Interrupt Enable
0b - Interrupt disabled
1b - Interrupt enabled
0
FRADMTCH
No FRAD Match Error Interrupt Enable
0b - Interrupt disabled
1b - Interrupt enabled
79.13.3 Serial flash memory address assignment
The serial flash memory address assignment can be modified by writing into Serial Flash Memory A1 Top Address Register 
(SFA1AD) and Serial Flash Memory A2 Top Address Register (SFA2AD) for device A
Table 769. Serial flash memory address assignment
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
Table continues on the next page...
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4905 / 5251


---
# 페이지 2046

Table 769. Serial flash memory address assignment (continued)
Parameter
Function
Access mode
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
79.14 Flash memory mapped AMBA bus
QuadSPI_AMBA_BASE defines the address to be used as the start address of the serial flash memory device, as defined by the 
system memory map. Note that this may be a remapping of the physical address of the serial flash memory in the system. See 
the system address map for details.
Table 770. QuadSPI AMBA bus memory map
Address
Register name
QuadSPI_AMBA_BASE to (TOP_ADDR_MEMA2 
- 1h)
• See Memory-mapped serial flash memory data—individual flash 
memory mode on flash memory A.
• For information about byte ordering, see Table 733 and Table 734.
QuadSPI_ARDB_BASE to... (32 * 4 Byte) 
QuadSPI_ARDB_BASE + 1FFh
• See AHB RX Data Buffer Register (ARDB0 - ARDB31).
• For information about the byte ordering, see Table 733.
 
Any read access to non-implemented addresses provides undefined results.
In individual flash memory modes, the 3/4 address bytes (as programmed in the instruction/operand in the 
sequence) available for the flash memory address are determined by SFADR[23:0] or SFADR[31:0] as provided 
in the table shown above.
  NOTE  
79.14.1 AHB bus access read considerations
Note that all logic in the QuadSPI module implementing the AHB bus access is designed to read the content of an external serial 
flash memory device. Therefore, the following restrictions apply to the QuadSPI module with respect to accesses to the AHB bus:
• AHB bus read access types—NONSEQ and BUSY—are fully supported.
• AHB read access type—SEQ—is treated in the same way as NONSEQ. See Flash memory mapped AMBA bus for 
details.
• Early burst termination is not supported for AHB transactions.
• An AHB error response is provided on occurrence of:
— Parity error
— ECC error from flash memory
— Data learning failure
Also, interrupts (if enabled) are provided along with the AHB error response.
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4906 / 5251


---
# 페이지 2047

• An AHB error response occurs when FR[AITEF] bit is set
• An AHB bus stall along with error response occurs when FR[AAEF] bit is set
79.14.2 Memory-mapped serial flash memory data—individual flash memory mode on flash memory A
Starting with address QuadSPI_AMBA_BASE, the content of the first external serial flash memory device is mapped into the 
address space of the device containing the QuadSPI module. Serial flash memory byte address 0h corresponds to bus address, 
QuadSPI_AMBA_BASE, in an increasing order. . See the following table for the address mapping. The byte ordering for 32-bit 
access is provided in Table 733 and for 64-bit read access, the byte ordering is provided in Table 734.
Table 771. Memory-mapped individual flash memory mode—flash memory A address scheme
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
79.14.3 ARDB register descriptions
 
See the system memory map in this document for the base address of the QuadSPI AHB RX data buffer.
  NOTE  
79.14.3.1
ARDB memory map
QuadSPI_S32K358_ARDB base address: 6800_0000h
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4907 / 5251


---
# 페이지 2048

Offset
Register
Width
(In bits)
Access
Reset value
0h - 7Ch
AHB RX Data Buffer Register (ARDB0 - ARDB31)
32
R
0000_0000h
79.14.3.2
AHB RX Data Buffer Register (ARDB0 - ARDB31)
Offset
For a = 0 to 31:
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
• Example 1 - RX buffer filled completely with 32 words: In this case, the address range for valid read access extends from 
ARDB0 to ARDB31 .
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
NXP Semiconductors
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4908 / 5251


---
# 페이지 2049

Fields
Field
Function
31-0
ARXD
ARDB provided RX buffer data
Byte order (endianness) is identical to the RX buffer data registers.
79.15 Glossary
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
Quad Serial Peripheral Interface (QuadSPI) for S32K358, S32K348, S32K338, and S32K328
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4909 / 5251


---