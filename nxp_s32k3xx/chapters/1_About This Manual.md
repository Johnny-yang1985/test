# 페이지 1

Chapter 1
About This Manual
1.1 Audience
This reference manual (RM) is intended for system software, hardware developers, and applications programmers who need to 
develop products using this chip. It assumes that its users understand operating systems, microprocessor system design, and 
basic principles of software and hardware.
1.2 Organization
This manual has two main sets of chapters.
• Chapters in the first set contain information that applies to all components on the chip.
• Chapters in the second set are organized into functional groupings that detail particular areas of functionality.
— Examples of these groupings are clocking, timers, and communication interfaces.
— Each grouping includes chapters that provide a technical description of individual modules.
1.2.1 Attachments
This manual includes key information in the files attached to it. For example, memory map and I/O details. Use the content in these 
attachments in conjunction with this manual's content.
 
Select the paperclip icon on the left side of the PDF window to see the list of attachments.
  NOTE  
1.3 Module descriptions
Each module chapter has two main parts:
• The first section, chip-specific [module name] information, provides details such as the number of module instances on the 
chip and connections between that module and the other ones. Read this section first because its content is crucial for 
understanding the information in the other sections of the chapter.
• The subsequent sections provide general information about the module, including its signals, registers, and functional 
description.
The following figure shows you an example of this demarcation.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
7 / 5251


---
# 페이지 2

Chapter 49
Enhanced Serial Communication Interface (eSCI)
49.1
Chip-specific eSCI information
This chip has six instances of the eSCI module. Some feature details vary between the
instances.
The following table summarizes the feature differences. The table does not list feature
details that the instances share.
Table 49-1. eSCI instance feature differences
Instance
DMA support
eSCI_A and eSCI_B
Yes
eSCI_C, eSCI_D, eSCI_E, and eSCI_F
No: descriptions of eSCI DMA functionality do not apply to
these instances
NOTE
For eSCI_D, the single wire feature does not apply for TX/RX
via PCSA3 because this pad works only as an output.
49.2
Introduction
The eSCI block is an enhanced SCI block with a LIN controller interface layer and DMA
support. The LIN controller layer complies with the specifications LIN 1.3, LIN 2.0, LIN
2.1, and SAE J2602/1.
49.2.1
Bibliography
• LIN Specification Package Revision 1.3; December 12, 2002
• LIN Specification Package Revision 2.0; September 23, 2003
Sample Reference Manual
EXAMPLE
Chip-specific information 
that should be read first
Beginning of general 
module information
Figure 1. Example of chapter chip-specific information and general module information
1.3.1 Chip-specific information that clarifies content in the same chapter
The following figure shows an example of chip-specific information that clarifies general module information presented later in the 
chapter. In this case, the chip-specific register reset values supersede the reset values that appear in the register diagram.
NXP Semiconductors
About This Manual
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
8 / 5251


---
# 페이지 3

Chapter 9
System Integration Unit Lite2 (SIUL2)
9.1 Chip-specific SIUL2 information
9.1.1 Feature configurations
In this device, the SIUL2_0 module instance does not support the following features described in the generic description:
• Interrupts
• DMA channels
9.1.2 Notes for IMCR
Out of reset, PA_00, PA_04, and PA_05 pads have JTAG input functionality selected by default. It should be disabled in the
corresponding IMCR registers (IMCR61, IMCR60, and IMCR50 respectively) in order to use other functionality such as GPIO.
9.2 Introduction
9.2.1 Overview
The System Integration Unit Lite2 provides control over all the electrical pin controls and ports with 16 bits of bidirectional, general-
purpose input and output signals. One of the most important functions of the SIUL2 is to enable the user to select the functions
and electrical characteristics that appear on external device pins. It also controls the multiplexing of internal signals from one
module to another and controls chip I/O. It supports as many as 32 external interrupts with trigger event configuration. The following
figure is the block diagram of SIUL2 and its interfaces to other system components.
System Integration Unit Lite2 (SIUL2)
Sample Reference Manual
NXP Semiconductors
IPS
controller
IPS BUS
DMA
Interrupt
Controller
Interrupt
- Configuration
- Glitch Filter
Interrupt/DMA Request
GPIO
MSCRs/
IMCRs
Pad Control and Pin Muxing
IP Modules
IO
MUX
PADS
SIUL2 Module
Data Registers
Figure 23. System Integration Unit Lite2 block diagram
This module provides dedicated pad control to general-purpose pads that can be configured as either inputs or outputs. The
SIUL2 module provides registers that enable user software to read values from GPIO pads configured as inputs, and write values
to GPIO pads configured as outputs:
• When configured as output, you can write to an internal register to control the state driven on the associated output pad.
• When configured as input, you can detect the state of the associated pad by reading the value from an internal register.
• When configured as input and output, the pad value can be read back, which can be used as a method of checking if the
written value appeared on the pad.
To assist software development, GPIO data registers can be accessed using various mechanisms. These differing mechanisms
allow support for port access or for bit manipulation without the need to use read-modify-write operations:
• Access to two 16-bit ports in one access
• Read/write access to a single bit
• A 16-bit port write with a bit mask, using single 32-bit access.
Introduction
Sample Reference Manual
NXP Semiconductors
Chapter 9
System Integration Unit Lite2 (SIUL2)
9.1 Chip-specific SIUL2 information
9.1.1 Feature configurations
In this device, the SIUL2_0 module instance does not support the following features described in the generic description:
• Interrupts
• DMA channels
9.1.2 Notes for IMCR
Out of reset, PA_00, PA_04, and PA_05 pads have JTAG input functionality selected by default. It should be disabled in the
corresponding IMCR registers (IMCR61, IMCR60, and IMCR50 respectively) in order to use other functionality such as GPIO.
9.2 Introduction
9.2.1 Overview
The System Integration Unit Lite2 provides control over all the electrical pin controls and ports with 16 bits of bidirectional, general-
purpose input and output signals. One of the most important functions of the SIUL2 is to enable the user to select the functions
and electrical characteristics that appear on external device pins. It also controls the multiplexing of internal signals from one
module to another and controls chip I/O. It supports as many as 32 external interrupts with trigger event configuration. The following
figure is the block diagram of SIUL2 and its interfaces to other system components.
System Integration Unit Lite2 (SIUL2)
Sample Reference Manual
NXP Semiconductors
IPS
IPS BUS
DMA
Interrupt
Controller
Interrupt
- Configuration
- Glitch Filter
Interrupt/DMA Request
GPIO
MSCRs/
IMCRs
Pad Control and Pin Muxing
IP Modules
IO
MUX
PADS
SIUL2 Module
Data Registers
Figure 23. System Integration Unit Lite2 block diagram
This module provides dedicated pad control to general-purpose pads that can be configured as either inputs or outputs. The
SIUL2 module provides registers that enable user software to read values from GPIO pads configured as inputs, and write values
to GPIO pads configured as outputs:
• When configured as output, you can write to an internal register to control the state driven on the associated output pad.
• When configured as input, you can detect the state of the associated pad by reading the value from an internal register.
• When configured as input and output, the pad value can be read back, which can be used as a method of checking if the
written value appeared on the pad.
To assist software development, GPIO data registers can be accessed using various mechanisms. These differing mechanisms
allow support for port access or for bit manipulation without the need to use read-modify-write operations:
• Access to two 16-bit ports in one access
• Read/write access to a single bit
• A 16-bit port write with a bit mask, using single 32-bit access.
Introduction
Sample Reference Manual
NXP Semiconductors
EXAMPLE
Figure 2. Example of chip-specific information that clarifies content in the same chapter
1.3.2 Chip-specific information that refers to a different chapter
Related chip-specific information may be provided in different chapters of the manual. The following figure shows an example of 
two such connected pieces of information. In this case, read both before you proceed.
NXP Semiconductors
About This Manual
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
9 / 5251


---
# 페이지 4

Chapter 10
Crossbar Integrity Checker (XBIC)
10.1 Chip-specific XBIC information
This chip has one instance of the XBIC module.
10.1.1 XBIC controller and target assignments
The XBIC identifies each XBAR controller and target in terms of the controller or target's
physical port number. See the "Physical controller port" assignments in Table 9-1 and the
"target port" assignments in Table 9-2.
10.1.2
Unimplemented MCR and ESR fields
10.2 Overview
Sample Reference Manual
Chapter 9
Crossbar Switch (XBAR)
9.1 Chip-specific XBAR information
This chip has one instance of the XBAR module.
9.1.1
XBAR controller and target assignments
The following table lists the XBAR physical port numbers and logical IDs for all controller
ports on this SoC.
•Each port number matches the default priority assigned to the corresponding physical
controller port. This default priority equals the reset value of the priority field for each
controller port in the PRS   registers.
n
•A priority value of 0 is the highest priority. There is no "disabled" value for the
priority.
•A Nexus_3 module and core data bus share the same physical controller port for each
core.
The logical controller ID corresponds to the logical address provided by the controller module
and is unique for each module. The logical controller IDs are used by the bus controllers
connected to the XBAR. The Nexus controller is identified by setting the MSB in the 4-bit
field that supplies the controller ID number.
Table 9-1.XBAR controller ports and logical controller IDs
Module
Physical controller port
Logical controller ID
Comment
Core0 instruction
0
0
Core0 data
1
0
Nexus_3_0
8
Nexus_3_0 arbitrates with Core0 data for XBAR port 1
Core1 instruction
2
1
Core1 data
3
1
Nexus_3_1
9
Nexus_3_1 arbitrates with Core1 data for XBAR port 3
Table continues on the next page...
Sample Reference Manual
The Crossbar Integrity Checker (XBIC) verifies the integrity of the crossbar transfers.
For forward signals (controller to target), it is done by verifying the integrity of the attribute
information using an 8-bit Error Detection Code (EDC). The EDC detects any single- or
double-bit errors in the attribute information and signals the Fault Collection and Control
Unit (FCCU) when an error is detected. For feedback signals (target to controller), it is done
by comparing the consistency of the signals during the AHB dataphase.There are three
signals from target to controller, hready, hresp0, and hresp2. If any of the controller signals is
different from the target signals during dataphase, the error will be reported in the Error
Status Register.
On this chip, the MCR[SE5] and ESR[DPSE5] fields are not implemented. In XBIC
Module Control Register (XBIC_MCR) and XBIC Error Status Register (XBIC_ESR),
these fields are reserved.
EXAMPLE
Figure 3. Example of chip-specific information that refers to a different chapter
1.4 Register descriptions
Module chapters present register information in the following:
• Memory maps, which contain:
— An offset from the module's base address
— The mnemonic and name of each register
— The width of each register (in bits)
— The reset value of each register
• Register figures
• Field-description tables
• Associated text
The following figure shows register figure conventions used throughout the manual.
NXP Semiconductors
About This Manual
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
10 / 5251


---
# 페이지 5

Figure 4. Register figure conventions
 
Reset values of reserved locations documented in this manual are subject to change and must not be used for 
diagnostic purposes.
  NOTE  
NXP Semiconductors
About This Manual
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
11 / 5251


---
# 페이지 6

1.5 Conventions
1.5.1 Notes and cautions
Specific information is provided as part of notes and cautions throughout this manual.
 
Emphasizes information that deserves extra attention.
  NOTE  
 
Informs you of situations that could lead to highly undesirable outcomes—such as damage to the chip or 
irreversible malfunction.
  CAUTION  
1.5.2 Numbering systems
The following suffixes identify different numbering systems:
Table 1. Numbering systems
This suffix
Identifies a
b
Binary number. For example, the binary equivalent of the number 5 is mentioned as 101b. In some 
cases, 0b is prefixed to binary numbers.
d
Decimal number. Decimal numbers are followed by this suffix only when there is a possibility of 
confusion. In general, decimal numbers are used without a suffix.
h
Hexadecimal number. For example, the hexadecimal equivalent of the number 60 is mentioned as 
3Ch. In some cases, 0x is prefixed to hexadecimal numbers.
1.5.3 Typographic notation
The following typographic notations are used throughout this document:
Table 2. Typographic notation
Example
Description
x and other italicized text
The italicized, lowercase x is used as a placeholder for replaceable numbers. In general, 
italicized text is used for titles of publications and for emphasis. Additionally, italics could 
be used for metasymbols in syntax descriptions. Plain lowercase letters are used as 
placeholders for single letters and numbers.
code font
Fixed-width font (such as Courier) used for code. It is used for a letter, word, or phrase that you 
want the user to type. For example, "Type Read and press Enter."
This type of font is also used for instruction mnemonics, directives, symbols, subcommands, 
parameters, operators, computer-language elements, code listings, commands that appear in 
running text, and for sample code. Instruction mnemonics and directives in text and tables are 
mentioned in all caps; for example, BSR.
SR[SCM]
A mnemonic in square brackets represents the name of a register field. This example refers 
to the Scaling Mode (SCM) field in the Status Register (SR).
REVNO[6:4], XAD[7:0]
Numbers in brackets that are separated by a colon represent either:
• A subset of a register's named field
Table continues on the next page...
NXP Semiconductors
About This Manual
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
12 / 5251


---
# 페이지 7

Table 2. Typographic notation (continued)
Example
Description
For example, REVNO[6:4] refers to bits 6-4 that are part of the COREREV field occupying 
bits 6-0 of the REVNO register.
• A continuous range of individual signals of a bus
For example, XAD[7:0] refers to signals 7-0 of the XAD bus.
MOD.REG
A period separates the elements of a hierarchy: subsystem.module.register. For example:
• SWT.TO means that the TO register is located in the SWT module.
• SMU.XRDC.CR means that the CR register is located in the XRDC module within the 
SMU subsystem.
1.5.4 Special terms
The following terms have special meanings.
Table 3. Special terms
Term
Meaning
Asserted
Refers to the state of a signal as follows:
• An active-high signal is asserted when high (1).
• An active-low signal is asserted when low (0).
Deasserted
Refers to the state of a signal as follows:
• An active-high signal is deasserted when low (0).
• An active-low signal is deasserted when high (1).
In some cases, deasserted signals are described as negated.
Reserved
Refers to memory space, register, field, or programming setting. Writes to a reserved location can 
result in unpredictable functionality or behavior. You must:
• Before writing to a location which contain reserved bits user must make sure the write 
operation will write the reserved bit with value specified as the reset value in NXP reference 
manual.
• Consider undefined locations in memory to be reserved as reset value 0 shall be assumed. 
You might get a BERR(transfer error) response on access to undefined locations in memory.
• If user reads data from memory area containing reserved bit, the value of reserved bits should 
be ignored and not used for any functional purposes.
 
BootROM could modify the reserved bit values after reset. Please refer to the 
BootROM settings attachment.
  NOTE  
Write 1 to clear (w1c)
Refers to the access type of a register field that is used to clear the field by writing the value 1 to it.
Undefined (u)
Refers to undefined reset values
1.6 Editorial changes
Each new release of this document includes editorial improvements such as:
NXP Semiconductors
About This Manual
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
13 / 5251


---
# 페이지 8

• Spelling
• Grammar
• Punctuation
• Voice
• Tense
• Capitalization
• Formatting
• Presentation
• Navigation
NXP Semiconductors
About This Manual
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
14 / 5251

