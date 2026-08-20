# 페이지 161

Chapter 9
Virtualization Wrapper (VIRT_WRAPPER) for all chips 
except S32K388 and S32K389
9.1 Chip-specific VIRT_WRAPPER information
9.1.1 Virtual Wrapper instances
This chip has one instance of Virtual Wrapper.
9.1.2 System overview of PDAC scheme
This figure shows the interaction of XRDC (containing PDACs), related to different cores (domain IDs), with VIRT_WRAPPER.
Cortex-M7_1
PDAC2
Cortex-M7_1 domain ID = IDC
ConfigC
Typical cores assignment
using XRDC in software
32 KB
Cortex-M7_0
PDAC1
SIUL2
Cortex-M7_0 domain ID = IDB
ConfigB
32 KB
HSE_B
PDAC0
HSE_B domain ID = IDA
ConfigA
32 KB
PDAC3
HSE_B and/or other domain ID
Write access to SIUL2 registers allowed through PDAC0-2,4 
 (ConfigA..C,D) after VIRT_WRAPPER is configured
Write access to all SIUL2 registers allowed prior
VIRT_WRAPPER is configured
Write access to VIRT_WRAPPER configuration registers only
XRDC
16 KB
VIRT_WRAPPER
REG_PROT
Cortex-M7_2
PDAC4
Cortex-M7_2 domain ID = IDD
32 KB
ConfigD
Config A, B, C, and D (write only)
S32K358
S32K342(4)
S32K311(2)
Figure 21. System overview of PDAC scheme
9.1.3 Initial VIRT_WRAPPER operation
Initially, VIRT_WRAPPER:
• Protects the "ConfigB-C" paths to SIUL2. You must configure VIRT_WRAPPER to define the SIUL2 R/W control registers that 
you can access through the "ConfigB-C" VIRT_WRAPPER access paths.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
212 / 5251


---
# 페이지 162

• Does not protect the direct path to SIUL2. It allows write accesses to all the SIUL2 R/W control registers. If PDAC0 is set to 
allow write access only to master core, for example HSE-B core (variant supported by the chip), then other masters cannot 
program the SIUL2 register. However, if these non-HSE_B masters program SIUL2 registers using other PDAC slots, a 
transfer error occurs. Any core can act as master core.
• Protects the "ConfigB-D" paths to SIUL2. You must configure VIRT_WRAPPER to define the SIUL2 R/W control registers that 
you can access through the "ConfigB-D" VIRT_WRAPPER access paths.
• The Virtualization Wrapper shall be configured using "IPS register interface". The Virtualization Wrapper access paths are 
accessible using IPS register interface.
9.1.4 Additional VIRT_WRAPPER details
See the "SIUL2 memory map overview and protection" table, later in this chapter, for an overview of the SIUL2 registers and their 
protection attributes.
By default, any core can access SIUL2 registers through PDAC0. This process is called ANY_MASTER. However, after XRDC 
configuration, HSE_B:
• Assigns PDACs to the respective cores or domain IDs
• Locks the XRDC configuration
• Programs VIRT_WRAPPER registers for pad assignments
HSE_B accesses PDAC0 solely for the pads having 11b as the value in their corresponding registers. Also, HSE_B retains the 
same value for the pads that it stores. In case HSE_B needs to take control of some pins, it can still configure PDACn to be 
accessible not only from a specific core master, but also from HSE_B, before it allows other cores to execute.
PDAC3 protects the IPS register portal of VIRT_WRAPPER configuration registers that any master can access but only via the 
memory slot assigned to PDAC3. The configuration via IPS register portal can be locked to prevent any further changes until the 
next functional reset. PDAC3 implements this locking.
The protection information of the parallel port output registers is inherited from the protection information of the included pads, 
according to these rules:
• When all the pads assigned to a GPIO port share the same protection information, the corresponding parallel port output 
register for this port inherits the same protection information.
• When at least one of the pads assigned to a GPIO port has different protection information than the other pads assigned 
to this GPIO port, access to the corresponding parallel port output register for this port is disabled for all the masters. 
Because of the aforementioned protection group mapping, the data bits of a register encode the protection control 
information related to one full GPIO port, or a chunk of 16 pads.
• You can assign the following SIUL2 registers to individual PDAC control:
— DISR0
— DIRER0
— DIRSR0
— IREER0
— IFEER0
— IFER0
— IFMCR0–31
— IFCPR
Then, you can access all these registers only through the assigned PDAC because the 
VIRT_WRAPPER_REG_C1039_1024 register controls the SIUL2 interrupt registers.
• You cannot access the SIUL2 R/W control registers configured through PDAC3 to be accessible through the ConfigA 
VIRT_WRAPPER access path, using the ConfigB VIRT_WRAPPER access path.
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
213 / 5251


---
# 페이지 163

• You cannot access any of the SIUL2 R/W control registers through ConfigB-C VIRT_WRAPPER access paths prior to 
VIRT_WRAPPER configuration. By default, any core can access SIUL2 registers through PDAC0 after reset.
• The same PDAC that accesses the main SIUL2 registers is used to access the SIUL2-mirrored registers and soft-lock-bit 
registers. This is because these registers are a part of the same 16 KB space.
• Access to mirrored SIUL2 registers sets the bit in Soft lock bit as an inherent property of register protection. See the 
"Register Protection" chapter for details on the soft lock bit behavior, when accessing the mirrored region.
• You cannot access any of the SIUL2 R/W control registers through ConfigB-D VIRT_WRAPPER access paths prior to 
VIRT_WRAPPER configuration. By default, any core can access SIUL2 registers through PDAC0 after reset. Once Virtual 
wrapper is configured, each attempt to write to SIUL R/W register through any of unassigned paths shall result in a 
transfer error.
9.2 Introduction
Virtualization refers to the various techniques, methods, or approaches of creating a virtual (rather than actual) version of 
something, such as a virtual hardware platform, operating system (OS), storage device, or network resources. The term "hardware 
virtualization" refers to the creation of a virtual machine that acts like a real computer with an operating system. The underlying 
hardware resources separate the software executed on these virtual machines (named "guest program"). In many cases, the 
specifically modified guest programs are required to run in such a virtual environment.
There are different types of hardware virtualization. One of them is para-virtualization. The para-virtualization is a non-simulated 
hardware environment. However, a guest program is executed in its own isolated domain, as if it is running on a separate 
system. Such a behavior is especially beneficial for the software targeted toward functional safety, because it allows freedom of 
interference for certain aspects of this software.
The hardware-assisted virtualization is a way of improving the efficiency of hardware virtualization. It involves employing specially 
designed CPUs and hardware components that help improve the performance of a guest environment. VIRT_WRAPPER, 
described in this chapter, is such a hardware component.
9.2.1 Overview
Virtualization is implemented by protecting (for example, granting or inhibiting) the access to a register within the virtualized 
module, dependent on the specific criteria. Virtualized module is the module instance associated with VIRT_WRAPPER. In this 
chip, SIUL2 is the virtualized module. Registers within virtualized module are virtualized by granting or inhibiting the access 
to different PDAC slots as encoded within virtualization pad assignments in VIRT_WRAPPER configuration registers. For this 
purpose, the virtualization information is programmed into VIRT_WRAPPER configuration registers that specify the grouping 
of registers within the virtualized module. Upon an access to virtualized module through the peripheral interface, the grouping 
information is exercised to identify whether the corresponding transaction should be granted or inhibited. The following figure 
depicts the usage of VIRT_WRAPPER in combination with the virtualized module.
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
214 / 5251


---
# 페이지 164

Register
grouping
Address
space
Access
allowed
?
Peripheral
enable
Peripheral
bus
Virtualized
module (VM)
Peripheral bus (for VIRT_WRAPPER)
Protection setup
information
Grant/inhibit
Figure 22. VIRT_WRAPPER block diagram
9.2.2 Features
VIRT_WRAPPER includes these features:
• A programmable chip-specific virtualization setup, capable to select a subset of the available masters in combination with up 
to four available address spaces
• Virtualizing accesses to the registers within a VM by inhibiting accesses to a subset of these registers under control of the 
specified virtualization information. Only write accesses can be inhibited for a specific master or set of masters.
9.2.3 Modes of operation
VIRT_WRAPPER is operable when the VM is operable. For details about the availability of the VM, see the chapter of the 
corresponding module. When there is no virtualization information specified for the VIRT_WRAPPER module, if XRDC is not 
configured, PDAC slot 0 is open as the default value of configuration register is 11b that is assigned with PDAC slot 0 and any 
master can access through it.
9.3 Functional description
This section describes the following topics:
• PDAC-based protection scheme
• Register group mapping considering SIUL2
• Access errors
9.3.1 PDAC-based protection scheme
VIRT_WRAPPER uses a protection scheme of the PDACs sub-blocks of XRDC. Each PDAC slot is assigned to one or more cores 
(by domain ID assignment in XRDC) as shown in Chip-specific VIRT_WRAPPER information section. Only the write accesses are 
protected by the virtualization feature. Read accesses are not impacted.
For any protection group defined within the register, two bits specify the protection control information according to the 
following table.
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
215 / 5251


---
# 페이지 165

Table 42. Protection control information for a single group
Value
Mnemonic
Protection
Description
00
PDAC1
Restricted access of registers, 
MSCR, IMCR, to PDAC slot 1
Protection setup information for PDAC slot 1 is used.
01
PDAC2
Restricted access of registers, 
MSCR, IMCR, to PDAC slot 2
Protection setup information for PDAC slot 2 is used.
10
PDAC3
Restricted access of registers, 
MSCR, IMCR, to PDAC slot 3
Protection setup information for PDAC slot 3 is used.
11
PDAC0
By default, any core can access 
SIUL2 registers through PDAC 
slot 0. This process is called 
ANY_MASTER.
Protection setup information for PDAC slot 0 is used.
9.3.2 Clocking
This module has no major clocking considerations.
9.3.3 Register group mapping for SIUL2
For the SIUL2 instance, the corresponding virtualization information within the VIRT_WRAPPER module is defined on a per-pad 
basis. Additionally, the virtualization information protects the control registers (controlling the input multiplexing scheme).
9.3.3.1
Virtualization of pad output registers
Any functional pad (controlled by the SIUL2 instance) is assigned to a separate protection group. This scheme excludes the pads 
that an MSCR register does not control within an SIUL2 instance (for example, power supply pads). As a result, the protection 
granularity defined by the virtualization information is a single pad. The control information associated with this protection group 
affects all the registers related to this pad.
The protection control information for pad i is specified within the protection group i; thus, it enables a very simple assignment 
scheme for the related protection control data that is hard-coded. The protection control information for pad i affects all the 
registers related to this pad, in the MSCRi and the GPDOi registers (in case such registers exist).
SIUL2 can control up to 512 pads that the MSCR, GPDO, and GPDI registers can access individually. The actual number of 
pads associated with a SIUL2 instance is specific to implementation. GPIO pads are also organized in GPIO ports consisting of 
a maximum of 16 pads that the parallel port registers (PGPDO, PGPDI, MPGPDO) can access.
Only the pad control and pad output registers are protected. Accesses to the read-only registers GPDI and PGPDI are not affected 
by virtualization.
As the protection granularity is a single pad, any virtualization information associated with this pad affects the corresponding 
MCSR and GPDO registers directly.
The parallel port output registers (PGPDO, MPGPDO) inherit the protection information from the protection information of the 
included pads according to the following rules:
• When all pads assigned to a GPIO port share the same protection information, the corresponding parallel port output register 
for this port inherits the same protection information.
• When at least one of the pads assigned to a GPIO port has a different protection information than the other pads assigned 
to this GPIO port, the write access to the corresponding parallel port output register (PGPDO and MPGPDO) for this port is 
disabled for all the masters through all the PDAC slots and a transfer error is generated.
Due to the aforementioned protection group mapping, the data bits of a register encode the protection control information related 
to one full GPIO port, or a chunk of 16 pads.
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
216 / 5251


---
# 페이지 166

9.3.3.2
Virtualization of input multiplexing control registers
Additionally, the SIUL2 instance supports the control of an input multiplexer (INMUX) scheme. This scheme provides the capability 
to select one of a set of the input pads to be the source of an input function for some of the peripheral modules. Any INMUX 
controlled by the SIUL2 instance is assigned to a separate protection group. It therefore provides an equivalent protection 
granularity within the virtualization information.
The protection group 512+i specifies the protection control information for the input multiplexer INMUX i. This enables a very 
simple assignment scheme for the related protection control data that is hard-coded. The protection control information for INMUX 
i affects the input multiplexing control register related to this input—namely, IMCRi.
SIUL2 can control up to 512 MSCRs and 512 IMCRs input multiplexers that the IMCRs can access individually. GPIO inputs 
are not affected by the input multiplexer scheme. Therefore, the associated virtualization information does not affect the 
corresponding pad input registers.
As the protection granularity is a single INMUX, any virtualization information associated with this INMUX affects the 
corresponding IMCR directly.
9.3.3.3
Virtualization of interrupt control registers
Additionally, the complete set of interrupt control registers within SIUL2 (address offset range 0010h–00C3h) can be protected as 
a separate group (protection group #1024).
The following table shows an overview of the SIUL2 registers and their protection attributes.
Table 43. SIUL2 memory map overview and protection
Offset range
Register
Size 
(bits)
Protected
Description
0000–000Fh
MIDR1, MIDR2
32
N
Read-only registers, not protected
0010–00C3h
Interrupt registers
32
Y
Protected as a single group—no individual protection 
of related registers
0240–A3Fh 1
MSCR
32
Y
Amount of registers defines maximum number of 
PADs to be controlled and protected
0A40–0123Fh
IMCR
32
Y
Amount of registers defines maximum number of 
INMUXes to be controlled and protected
1300–14FFh
GPDO GPDO[0] (8-
bit) register controls 
single PAD[0] pad 
means that if PAD[0] 
is assigned to PDAC 
slot 1 then PDAC 
slot 1 can write to 
GPDO[0] (8-bit).
8
Y
There are fewer GPDO registers than MSCR registers, 
as some PADs are not made available as GPIO 
PADs, but their electrical characteristics can still be 
programmed
1500–16FFh
GPDI
8
N
PAD input register, not protected
1700–173Fh
PGPDO PGPDO[0] 
(16-bit) register 
controls PAD[0-15] 
pads meaning if only 
all the PADs[0-15] 
are assigned to 
PDAC slot 1, then 
PDAC slot 1 can 
16
Y
Writable with 8-, 16-, and as a pair with 32-bit 
accesses
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
217 / 5251


---
# 페이지 167

Table 43. SIUL2 memory map overview and protection (continued)
Offset range
Register
Size 
(bits)
Protected
Description
write to PGPDO[0] 
(16-bit).
1740–177Fh
PGPDI
16
N
PAD input register, not protected
1780–17FFh
MPGPDO 
MPGPDO[0] (32-bit) 
register controls 
PAD[0-15] pads 
meaning if only all 
the PADs[0-15] are 
assigned to PDAC 
slot 1, then PDAC 
slot 1 can write 
to MPGPDO[0] (32-
bit).
32
Y
Only writable with 32-bit accesses
2010–20C3h
Reserved
—
—
—
2240–2A3Fh
Reserved
—
—
—
2A40–323Fh
Reserved
—
—
—
3300–34FFh
Reserved
—
—
—
4000–47FFh
Reserved
—
—
—
4800–48FFh
Reserved
—
—
—
1. The SIUL2 block guide specifies the support of a maximum of 512 MSCRs.
9.4 External signals
This module has no external signals.
9.5 Initialization
This module does not require initialization.
9.6 Application Information
This module supports virtualization of accesses to the registers within a SIUL2 by inhibiting or granting accesses to a subset of 
these registers under control of the specified master(core) information.
9.7 VIRT_WRAPPER memory map register descriptions
 
Access to reserved spaces outside the register bank and holes (unimplemented registers) within register bank 
generates the transfer error. Access to offset 104h does not generate any transfer error.
  NOTE  
9.7.1 VIRT_WRAPPER memory map
VIRTUAL_WRAPPER base address: 402A_8000h
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
218 / 5251


---
# 페이지 168

Offset
Register
Width
(In bits)
Access
Reset value
0h - 4h
Parameter_n Register (REG_A0 - REG_A1)
32
RW
FFFF_FFFFh
8h
Parameter_n Register (REG_A2)
32
RW
FFFF_FFFFh
Ch - 34h
Parameter_n Register (REG_A3 - REG_A13)
32
RW
FFFF_FFFFh
38h
Parameter_n Register (REG_A14)
32
RW
FFFF_FFFFh
80h
Parameter_n Register (REG_B0)
32
RW
FFFF_FFFFh
84h - 8Ch
Parameter_n Register (REG_B1 - REG_B3)
32
RW
FFFF_FFFFh
90h
Parameter_n Register (REG_B4)
32
RW
FFFF_FFFFh
94h
Parameter_n Register (REG_B5)
32
RW
FFFF_FFFFh
98h
Parameter_n Register (REG_B6)
32
RW
FFFF_FFFFh
9Ch
Parameter_n Register (REG_B7)
32
RW
FFFF_FFFFh
A0h
Parameter_n Register (REG_B8)
32
RW
FFFF_FFFFh
A4h
Parameter_n Register (REG_B9)
32
RW
FFFF_FFFFh
A8h - ACh
Parameter_n Register (REG_B10 - REG_B11)
32
RW
FFFF_FFFFh
B0h
Parameter_n Register (REG_B12)
32
RW
FFFF_FFFFh
B4h
Parameter_n Register (REG_B13)
32
RW
FFFF_FFFFh
B8h - BCh
Parameter_n Register (REG_B14 - REG_B15)
32
RW
FFFF_FFFFh
C0h
Parameter_n Register (REG_B16)
32
RW
FFFF_FFFFh
C8h
Parameter_n Register (REG_B18)
32
RW
FFFF_FFFFh
CCh
Parameter_n Register (REG_B19)
32
RW
FFFF_FFFFh
D0h
Parameter_n Register (REG_B20)
32
RW
FFFF_FFFFh
D4h
Parameter_n Register (REG_B21)
32
RW
FFFF_FFFFh
D8h
Parameter_n Register (REG_B22)
32
RW
FFFF_FFFFh
DCh
Parameter_n Register (REG_B23)
32
RW
FFFF_FFFFh
E0h
Parameter_n Register (REG_B24)
32
RW
FFFF_FFFFh
E4h
Parameter_n Register (REG_B25)
32
RW
FFFF_FFFFh
E8h
Parameter_n Register (REG_B26)
32
RW
FFFF_FFFFh
ECh
Parameter_n Register (REG_B27)
32
RW
FFFF_FFFFh
100h
Parameter_n Register (REG_C1039_1024)
32
RW
FFFF_FFFFh
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
219 / 5251


---
# 페이지 169

9.7.2 Parameter_n Register (REG_A0 - REG_A1)
Offset
Register
Offset
REG_A0
0h
REG_A1
4h
Function
This register set is for PAD0-511. They control MSCR, GPDO, PGPDO, and MPGPDO. Two bits assigned per PDAC slot have 
attributes of one of the implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
PAD_15 
PAD_14 
PAD_13 
PAD_12 
PAD_11 
PAD_10 
PAD_9 
PAD_8 
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
PAD_7 
PAD_6 
PAD_5 
PAD_4 
PAD_3 
PAD_2 
PAD_1 
PAD_0 
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
31-30
PAD_15
PAD_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
220 / 5251


---
# 페이지 170

Table continued from the previous page...
Field
Function
11b - SIUL2_VIRTWRAPPER_PDAC0
29-28
PAD_14
PAD_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
PAD_13
PAD_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
PAD_12
PAD_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
PAD_11
PAD_11
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
PAD_10
PAD_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
PAD_9
PAD_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
PAD_8
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
221 / 5251


---
# 페이지 171

Table continued from the previous page...
Field
Function
PAD_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
PAD_7
PAD_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
PAD_6
PAD_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
PAD_5
PAD_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
PAD_4
PAD_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
PAD_3
PAD_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
PAD_2
PAD_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
222 / 5251


---
# 페이지 172

Table continued from the previous page...
Field
Function
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
PAD_1
PAD_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
PAD_0
PAD_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.3 Parameter_n Register (REG_A2)
Offset
Register
Offset
REG_A2
8h
Function
This register set is for PAD0-511. They control MSCR, GPDO, PGPDO, and MPGPDO. Two bits assigned per PDAC slot have 
attributes of one of the implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
  NOTE  
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
223 / 5251


---
# 페이지 173

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
PAD_15 
PAD_14 
PAD_13 
PAD_12 
PAD_11 
PAD_10 
PAD_9 
PAD_8 
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
Reserved 
Reserved 
PAD_5 
PAD_4 
PAD_3 
PAD_2 
PAD_1 
PAD_0 
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
31-30
PAD_15
PAD_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
29-28
PAD_14
PAD_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
PAD_13
PAD_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
PAD_12
PAD_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
PAD_11
PAD_11
00b - SIUL2_VIRTWRAPPER_PDAC1
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
224 / 5251


---
# 페이지 174

Table continued from the previous page...
Field
Function
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
PAD_10
PAD_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
PAD_9
PAD_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
PAD_8
PAD_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
—
Reserved
13-12
—
Reserved
11-10
PAD_5
PAD_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
PAD_4
PAD_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
225 / 5251


---
# 페이지 175

Table continued from the previous page...
Field
Function
7-6
PAD_3
PAD_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
PAD_2
PAD_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
PAD_1
PAD_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
PAD_0
PAD_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.4 Parameter_n Register (REG_A3 - REG_A13)
Offset
For a = 3 to 13:
Register
Offset
REG_Aa
0h + (a × 4h)
Function
This register set is for PAD0-511. They control MSCR, GPDO, PGPDO, and MPGPDO. Two bits assigned per PDAC slot have 
attributes of one of the implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
226 / 5251


---
# 페이지 176

• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
PAD_15 
PAD_14 
PAD_13 
PAD_12 
PAD_11 
PAD_10 
PAD_9 
PAD_8 
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
PAD_7 
PAD_6 
PAD_5 
PAD_4 
PAD_3 
PAD_2 
PAD_1 
PAD_0 
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
31-30
PAD_15
PAD_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
29-28
PAD_14
PAD_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
PAD_13
PAD_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
PAD_12
PAD_12
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
227 / 5251


---
# 페이지 177

Table continued from the previous page...
Field
Function
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
PAD_11
PAD_11
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
PAD_10
PAD_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
PAD_9
PAD_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
PAD_8
PAD_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
PAD_7
PAD_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
PAD_6
PAD_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
228 / 5251


---
# 페이지 178

Table continued from the previous page...
Field
Function
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
PAD_5
PAD_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
PAD_4
PAD_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
PAD_3
PAD_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
PAD_2
PAD_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
PAD_1
PAD_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
PAD_0
PAD_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
229 / 5251


---
# 페이지 179

9.7.5 Parameter_n Register (REG_A14)
Offset
Register
Offset
REG_A14
38h
Function
This register set is for PAD0-511. They control MSCR, GPDO, PGPDO, and MPGPDO. Two bits assigned per PDAC slot have 
attributes of one of the implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
Reserved 
Reserved 
Reserved 
PAD_12 
PAD_11 
PAD_10 
PAD_9 
PAD_8 
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
PAD_7 
PAD_6 
PAD_5 
PAD_4 
PAD_3 
PAD_2 
PAD_1 
PAD_0 
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
31-30
—
Reserved
29-28
—
Reserved
27-26
Reserved
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
230 / 5251


---
# 페이지 180

Table continued from the previous page...
Field
Function
—
25-24
PAD_12
PAD_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
PAD_11
PAD_11
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
PAD_10
PAD_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
PAD_9
PAD_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
PAD_8
PAD_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
PAD_7
PAD_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
PAD_6
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
231 / 5251


---
# 페이지 181

Table continued from the previous page...
Field
Function
PAD_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
PAD_5
PAD_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
PAD_4
PAD_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
PAD_3
PAD_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
PAD_2
PAD_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
PAD_1
PAD_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
PAD_0
PAD_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
232 / 5251


---
# 페이지 182

Table continued from the previous page...
Field
Function
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.6 Parameter_n Register (REG_B0)
Offset
Register
Offset
REG_B0
80h
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
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
Reserved 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
233 / 5251


---
# 페이지 183

Fields
Field
Function
31-30
—
Reserved
29-28
—
Reserved
27-26
—
Reserved
25-24
—
Reserved
23-22
—
Reserved
21-20
—
Reserved
19-18
—
Reserved
17-16
—
Reserved
15-14
—
Reserved
13-12
—
Reserved
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
234 / 5251


---
# 페이지 184

Table continued from the previous page...
Field
Function
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.7 Parameter_n Register (REG_B1 - REG_B3)
Offset
Register
Offset
REG_B1
84h
REG_B2
88h
REG_B3
8Ch
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
235 / 5251


---
# 페이지 185

• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
INMUX_15 
INMUX_14 
INMUX_13 
INMUX_12 
INMUX_11 
INMUX_10 
INMUX_9 
INMUX_8 
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
INMUX_7 
INMUX_6 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
31-30
INMUX_15
INMUX_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
29-28
INMUX_14
INMUX_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
INMUX_13
INMUX_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
INMUX_12
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
236 / 5251


---
# 페이지 186

Table continued from the previous page...
Field
Function
INMUX_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
INMUX_11
INMUX_11
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
INMUX_10
INMUX_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
INMUX_9
INMUX_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
INMUX_8
INMUX_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
INMUX_6
INMUX_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
237 / 5251


---
# 페이지 187

Table continued from the previous page...
Field
Function
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
238 / 5251


---
# 페이지 188

9.7.8 Parameter_n Register (REG_B4)
Offset
Register
Offset
REG_B4
90h
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
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
INMUX_7 
INMUX_6 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
31-30
—
Reserved
29-28
—
Reserved
27-26
Reserved
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
239 / 5251


---
# 페이지 189

Table continued from the previous page...
Field
Function
—
25-24
—
Reserved
23-22
—
Reserved
21-20
—
Reserved
19-18
—
Reserved
17-16
—
Reserved
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
INMUX_6
INMUX_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
240 / 5251


---
# 페이지 190

Table continued from the previous page...
Field
Function
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.9 Parameter_n Register (REG_B5)
Offset
Register
Offset
REG_B5
94h
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
241 / 5251


---
# 페이지 191

 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
INMUX_15 
INMUX_14 
INMUX_13 
INMUX_12 
INMUX_11 
INMUX_10 
INMUX_9 
INMUX_8 
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
INMUX_7 
INMUX_6 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
31-30
INMUX_15
INMUX_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
29-28
INMUX_14
INMUX_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
INMUX_13
INMUX_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
INMUX_12
INMUX_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
242 / 5251


---
# 페이지 192

Table continued from the previous page...
Field
Function
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
INMUX_11
INMUX_11
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
INMUX_10
INMUX_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
INMUX_9
INMUX_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
INMUX_8
INMUX_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
INMUX_6
INMUX_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
243 / 5251


---
# 페이지 193

Table continued from the previous page...
Field
Function
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
244 / 5251


---
# 페이지 194

9.7.10 Parameter_n Register (REG_B6)
Offset
Register
Offset
REG_B6
98h
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
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
INMUX_7 
INMUX_6 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
31-30
—
Reserved
29-28
—
Reserved
27-26
Reserved
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
245 / 5251


---
# 페이지 195

Table continued from the previous page...
Field
Function
—
25-24
—
Reserved
23-22
—
Reserved
21-20
—
Reserved
19-18
—
Reserved
17-16
—
Reserved
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
INMUX_6
INMUX_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
246 / 5251


---
# 페이지 196

Table continued from the previous page...
Field
Function
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.11 Parameter_n Register (REG_B7)
Offset
Register
Offset
REG_B7
9Ch
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
247 / 5251


---
# 페이지 197

 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
INMUX_15 
INMUX_14 
INMUX_13 
INMUX_12 
INMUX_11 
INMUX_10 
INMUX_9 
INMUX_8 
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
INMUX_7 
INMUX_6 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
31-30
INMUX_15
INMUX_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
29-28
INMUX_14
INMUX_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
INMUX_13
INMUX_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
INMUX_12
INMUX_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
248 / 5251


---
# 페이지 198

Table continued from the previous page...
Field
Function
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
INMUX_11
INMUX_11
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
INMUX_10
INMUX_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
INMUX_9
INMUX_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
INMUX_8
INMUX_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
INMUX_6
INMUX_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
249 / 5251


---
# 페이지 199

Table continued from the previous page...
Field
Function
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
250 / 5251


---
# 페이지 200

9.7.12 Parameter_n Register (REG_B8)
Offset
Register
Offset
REG_B8
A0h
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
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
INMUX_7 
INMUX_6 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
31-30
—
Reserved
29-28
—
Reserved
27-26
Reserved
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
251 / 5251


---
# 페이지 201

Table continued from the previous page...
Field
Function
—
25-24
—
Reserved
23-22
—
Reserved
21-20
—
Reserved
19-18
—
Reserved
17-16
—
Reserved
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
INMUX_6
INMUX_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
252 / 5251


---
# 페이지 202

Table continued from the previous page...
Field
Function
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.13 Parameter_n Register (REG_B9)
Offset
Register
Offset
REG_B9
A4h
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
253 / 5251


---
# 페이지 203

 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
INMUX_15 
INMUX_14 
INMUX_13 
INMUX_12 
INMUX_11 
INMUX_10 
INMUX_9 
INMUX_8 
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
Reserved 
Reserved 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
31-30
INMUX_15
INMUX_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
29-28
INMUX_14
INMUX_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
INMUX_13
INMUX_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
INMUX_12
INMUX_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
254 / 5251


---
# 페이지 204

Table continued from the previous page...
Field
Function
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
INMUX_11
INMUX_11
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
INMUX_10
INMUX_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
INMUX_9
INMUX_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
INMUX_8
INMUX_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
—
Reserved
13-12
—
Reserved
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
255 / 5251


---
# 페이지 205

Table continued from the previous page...
Field
Function
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.14 Parameter_n Register (REG_B10 - REG_B11)
Offset
Register
Offset
REG_B10
A8h
REG_B11
ACh
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
256 / 5251


---
# 페이지 206

Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
INMUX_15 
INMUX_14 
INMUX_13 
INMUX_12 
INMUX_11 
INMUX_10 
INMUX_9 
INMUX_8 
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
INMUX_7 
INMUX_6 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
31-30
INMUX_15
INMUX_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
29-28
INMUX_14
INMUX_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
INMUX_13
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
257 / 5251


---
# 페이지 207

Table continued from the previous page...
Field
Function
INMUX_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
INMUX_12
INMUX_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
INMUX_11
INMUX_11
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
INMUX_10
INMUX_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
INMUX_9
INMUX_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
INMUX_8
INMUX_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
258 / 5251


---
# 페이지 208

Table continued from the previous page...
Field
Function
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
INMUX_6
INMUX_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
259 / 5251


---
# 페이지 209

Table continued from the previous page...
Field
Function
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.15 Parameter_n Register (REG_B12)
Offset
Register
Offset
REG_B12
B0h
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
INMUX_10 
INMUX_9 
INMUX_8 
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
INMUX_7 
INMUX_6 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
260 / 5251


---
# 페이지 210

Fields
Field
Function
31-30
—
Reserved
29-28
—
Reserved
27-26
—
Reserved
25-24
—
Reserved
23-22
—
Reserved
21-20
INMUX_10
INMUX_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
INMUX_9
INMUX_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
INMUX_8
INMUX_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
INMUX_6
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
261 / 5251


---
# 페이지 211

Table continued from the previous page...
Field
Function
INMUX_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
262 / 5251


---
# 페이지 212

Table continued from the previous page...
Field
Function
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.16 Parameter_n Register (REG_B13)
Offset
Register
Offset
REG_B13
B4h
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
INMUX_15 
INMUX_14 
INMUX_13 
INMUX_12 
INMUX_11 
INMUX_10 
INMUX_9 
INMUX_8 
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
INMUX_7 
INMUX_6 
INMUX_5 
INMUX_4 
INMUX_3 
Reserved 
Reserved 
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
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
263 / 5251


---
# 페이지 213

Fields
Field
Function
31-30
INMUX_15
INMUX_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
29-28
INMUX_14
INMUX_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
INMUX_13
INMUX_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
INMUX_12
INMUX_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
INMUX_11
INMUX_11
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
INMUX_10
INMUX_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
INMUX_9
INMUX_9
00b - SIUL2_VIRTWRAPPER_PDAC1
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
264 / 5251


---
# 페이지 214

Table continued from the previous page...
Field
Function
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
INMUX_8
INMUX_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
INMUX_6
INMUX_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
265 / 5251


---
# 페이지 215

Table continued from the previous page...
Field
Function
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
—
Reserved
3-2
—
Reserved
1-0
—
Reserved
9.7.17 Parameter_n Register (REG_B14 - REG_B15)
Offset
Register
Offset
REG_B14
B8h
REG_B15
BCh
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
  NOTE  
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
266 / 5251


---
# 페이지 216

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
INMUX_15 
INMUX_14 
INMUX_13 
INMUX_12 
INMUX_11 
INMUX_10 
INMUX_9 
INMUX_8 
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
INMUX_7 
INMUX_6 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
31-30
INMUX_15
INMUX_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
29-28
INMUX_14
INMUX_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
INMUX_13
INMUX_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
INMUX_12
INMUX_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
INMUX_11
INMUX_11
00b - SIUL2_VIRTWRAPPER_PDAC1
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
267 / 5251


---
# 페이지 217

Table continued from the previous page...
Field
Function
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
INMUX_10
INMUX_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
INMUX_9
INMUX_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
INMUX_8
INMUX_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
INMUX_6
INMUX_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
268 / 5251


---
# 페이지 218

Table continued from the previous page...
Field
Function
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.18 Parameter_n Register (REG_B16)
Offset
Register
Offset
REG_B16
C0h
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
269 / 5251


---
# 페이지 219

Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
Reserved 
Reserved 
Reserved 
INMUX_12 
INMUX_11 
INMUX_10 
INMUX_9 
INMUX_8 
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
INMUX_7 
INMUX_6 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
31-30
—
Reserved
29-28
—
Reserved
27-26
—
Reserved
25-24
INMUX_12
INMUX_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
270 / 5251


---
# 페이지 220

Table continued from the previous page...
Field
Function
23-22
INMUX_11
INMUX_11
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
INMUX_10
INMUX_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
INMUX_9
INMUX_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
INMUX_8
INMUX_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
INMUX_6
INMUX_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
271 / 5251


---
# 페이지 221

Table continued from the previous page...
Field
Function
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
272 / 5251


---
# 페이지 222

9.7.19 Parameter_n Register (REG_B18)
Offset
Register
Offset
REG_B18
C8h
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
INMUX_15 
INMUX_14 
INMUX_13 
INMUX_12 
INMUX_11 
INMUX_10 
INMUX_9 
INMUX_8 
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
INMUX_7 
INMUX_6 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
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
Fields
Field
Function
31-30
INMUX_15
INMUX_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
273 / 5251


---
# 페이지 223

Table continued from the previous page...
Field
Function
29-28
INMUX_14
INMUX_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
INMUX_13
INMUX_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
INMUX_12
INMUX_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
INMUX_11
INMUX_11
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
INMUX_10
INMUX_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
INMUX_9
INMUX_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
INMUX_8
INMUX_8
00b - SIUL2_VIRTWRAPPER_PDAC1
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
274 / 5251


---
# 페이지 224

Table continued from the previous page...
Field
Function
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
INMUX_6
INMUX_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
275 / 5251


---
# 페이지 225

Table continued from the previous page...
Field
Function
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
—
Reserved
9.7.20 Parameter_n Register (REG_B19)
Offset
Register
Offset
REG_B19
CCh
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
  NOTE  
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
276 / 5251


---
# 페이지 226

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
INMUX_15 
INMUX_14 
INMUX_13 
INMUX_12 
INMUX_11 
Reserved 
Reserved 
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
Reserved 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
31-30
INMUX_15
INMUX_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
29-28
INMUX_14
INMUX_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
INMUX_13
INMUX_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
INMUX_12
INMUX_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
INMUX_11
INMUX_11
00b - SIUL2_VIRTWRAPPER_PDAC1
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
277 / 5251


---
# 페이지 227

Table continued from the previous page...
Field
Function
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
—
Reserved
19-18
—
Reserved
17-16
—
Reserved
15-14
—
Reserved
13-12
—
Reserved
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
278 / 5251


---
# 페이지 228

Table continued from the previous page...
Field
Function
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.21 Parameter_n Register (REG_B20)
Offset
Register
Offset
REG_B20
D0h
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
  NOTE  
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
279 / 5251


---
# 페이지 229

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
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
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
Reserved 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
31-30
—
Reserved
29-28
—
Reserved
27-26
—
Reserved
25-24
—
Reserved
23-22
—
Reserved
21-20
—
Reserved
19-18
—
Reserved
17-16
—
Reserved
15-14
—
Reserved
13-12
—
Reserved
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
280 / 5251


---
# 페이지 230

Table continued from the previous page...
Field
Function
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
281 / 5251


---
# 페이지 231

9.7.22 Parameter_n Register (REG_B21)
Offset
Register
Offset
REG_B21
D4h
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
INMUX_15 
INMUX_14 
INMUX_13 
INMUX_12 
INMUX_11 
INMUX_10 
INMUX_9 
INMUX_8 
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
INMUX_7 
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
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
Fields
Field
Function
31-30
INMUX_15
INMUX_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
282 / 5251


---
# 페이지 232

Table continued from the previous page...
Field
Function
29-28
INMUX_14
INMUX_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
INMUX_13
INMUX_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
INMUX_12
INMUX_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
INMUX_11
INMUX_11
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
INMUX_10
INMUX_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
INMUX_9
INMUX_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
INMUX_8
INMUX_8
00b - SIUL2_VIRTWRAPPER_PDAC1
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
283 / 5251


---
# 페이지 233

Table continued from the previous page...
Field
Function
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
—
Reserved
11-10
—
Reserved
9-8
—
Reserved
7-6
—
Reserved
5-4
—
Reserved
3-2
—
Reserved
1-0
—
Reserved
9.7.23 Parameter_n Register (REG_B22)
Offset
Register
Offset
REG_B22
D8h
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
284 / 5251


---
# 페이지 234

• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
INMUX_15 
INMUX_14 
INMUX_13 
INMUX_12 
INMUX_11 
INMUX_10 
INMUX_9 
INMUX_8 
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
INMUX_7 
INMUX_6 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
31-30
INMUX_15
INMUX_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
29-28
INMUX_14
INMUX_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
INMUX_13
INMUX_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
285 / 5251


---
# 페이지 235

Table continued from the previous page...
Field
Function
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
INMUX_12
INMUX_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
INMUX_11
INMUX_11
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
INMUX_10
INMUX_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
INMUX_9
INMUX_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
INMUX_8
INMUX_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
INMUX_6
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
286 / 5251


---
# 페이지 236

Table continued from the previous page...
Field
Function
INMUX_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
287 / 5251


---
# 페이지 237

Table continued from the previous page...
Field
Function
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.24 Parameter_n Register (REG_B23)
Offset
Register
Offset
REG_B23
DCh
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
INMUX_10 
INMUX_9 
INMUX_8 
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
INMUX_7 
INMUX_6 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
288 / 5251


---
# 페이지 238

Fields
Field
Function
31-30
—
Reserved
29-28
—
Reserved
27-26
—
Reserved
25-24
—
Reserved
23-22
—
Reserved
21-20
INMUX_10
INMUX_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
INMUX_9
INMUX_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
INMUX_8
INMUX_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
INMUX_6
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
289 / 5251


---
# 페이지 239

Table continued from the previous page...
Field
Function
INMUX_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
290 / 5251


---
# 페이지 240

Table continued from the previous page...
Field
Function
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.25 Parameter_n Register (REG_B24)
Offset
Register
Offset
REG_B24
E0h
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
INMUX_15 
INMUX_14 
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
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
Reserved 
INMUX_5 
Reserved 
Reserved 
Reserved 
Reserved 
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
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
291 / 5251


---
# 페이지 241

Fields
Field
Function
31-30
INMUX_15
INMUX_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
29-28
INMUX_14
INMUX_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
—
Reserved
25-24
—
Reserved
23-22
—
Reserved
21-20
—
Reserved
19-18
—
Reserved
17-16
—
Reserved
15-14
—
Reserved
13-12
—
Reserved
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
292 / 5251


---
# 페이지 242

Table continued from the previous page...
Field
Function
9-8
—
Reserved
7-6
—
Reserved
5-4
—
Reserved
3-2
—
Reserved
1-0
—
Reserved
9.7.26 Parameter_n Register (REG_B25)
Offset
Register
Offset
REG_B25
E4h
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
  NOTE  
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
293 / 5251


---
# 페이지 243

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
INMUX_15 
INMUX_14 
INMUX_13 
INMUX_12 
INMUX_11 
INMUX_10 
INMUX_9 
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
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
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
Fields
Field
Function
31-30
INMUX_15
INMUX_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
29-28
INMUX_14
INMUX_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
INMUX_13
INMUX_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
INMUX_12
INMUX_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
INMUX_11
INMUX_11
00b - SIUL2_VIRTWRAPPER_PDAC1
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
294 / 5251


---
# 페이지 244

Table continued from the previous page...
Field
Function
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
INMUX_10
INMUX_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
INMUX_9
INMUX_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
—
Reserved
15-14
—
Reserved
13-12
—
Reserved
11-10
—
Reserved
9-8
—
Reserved
7-6
—
Reserved
5-4
—
Reserved
3-2
—
Reserved
1-0
Reserved
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
295 / 5251


---
# 페이지 245

Table continued from the previous page...
Field
Function
—
9.7.27 Parameter_n Register (REG_B26)
Offset
Register
Offset
REG_B26
E8h
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
INMUX_15 
INMUX_14 
INMUX_13 
INMUX_12 
INMUX_11 
INMUX_10 
INMUX_9 
INMUX_8 
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
INMUX_7 
INMUX_6 
INMUX_5 
INMUX_4 
INMUX_3 
INMUX_2 
INMUX_1 
INMUX_0 
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
31-30
INMUX_15
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
296 / 5251


---
# 페이지 246

Table continued from the previous page...
Field
Function
INMUX_15
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
29-28
INMUX_14
INMUX_14
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
27-26
INMUX_13
INMUX_13
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
25-24
INMUX_12
INMUX_12
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
23-22
INMUX_11
INMUX_11
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
21-20
INMUX_10
INMUX_10
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
19-18
INMUX_9
INMUX_9
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
297 / 5251


---
# 페이지 247

Table continued from the previous page...
Field
Function
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
17-16
INMUX_8
INMUX_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
INMUX_7
INMUX_7
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
13-12
INMUX_6
INMUX_6
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
INMUX_4
INMUX_4
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
7-6
INMUX_3
INMUX_3
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
298 / 5251


---
# 페이지 248

Table continued from the previous page...
Field
Function
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.28 Parameter_n Register (REG_B27)
Offset
Register
Offset
REG_B27
ECh
Function
Controls access to pads 0 to 255 specific for IMCR registers. Two bits assigned per IMCR register have attributes of one of the 
implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
• Any master can access holes (unimplemented registers) of SIUL2 through PDAC0.
• After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
  NOTE  
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
299 / 5251


---
# 페이지 249

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
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
Reserved 
INMUX_8 
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
Reserved 
Reserved 
INMUX_5 
Reserved 
Reserved 
INMUX_2 
INMUX_1 
INMUX_0 
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
31-30
—
Reserved
29-28
—
Reserved
27-26
—
Reserved
25-24
—
Reserved
23-22
—
Reserved
21-20
—
Reserved
19-18
—
Reserved
17-16
INMUX_8
INMUX_8
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
15-14
—
Reserved
Table continues on the next page...
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
300 / 5251


---
# 페이지 250

Table continued from the previous page...
Field
Function
13-12
—
Reserved
11-10
INMUX_5
INMUX_5
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9-8
—
Reserved
7-6
—
Reserved
5-4
INMUX_2
INMUX_2
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
3-2
INMUX_1
INMUX_1
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
1-0
INMUX_0
INMUX_0
00b - SIUL2_VIRTWRAPPER_PDAC1
01b - SIUL2_VIRTWRAPPER_PDAC2
10b - SIUL2_VIRTWRAPPER_PDAC4
11b - SIUL2_VIRTWRAPPER_PDAC0
9.7.29 Parameter_n Register (REG_C1039_1024)
Offset
Register
Offset
REG_C1039_1024
100h
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
301 / 5251


---
# 페이지 251

Function
Controls access to DISR0, DIRER0, DIRSR0, IREER0, IFEER0, IFER0, IFMCR, and IFCPR0 interrupt registers. Eight bits 
assigned per PDAC slot have attributes of one of the implemented PDAC slots:
• 00-SIUL2_VIRTWRAPPER_PDAC1
• 01-SIUL2_VIRTWRAPPER_PDAC2
• 10-SIUL2_VIRTWRAPPER_PDAC4
• 11-SIUL2_VIRTWRAPPER_PDAC0
 
After reset, when XRDC is not configured, any master can access SIUL2 registers through PDAC0 without 
getting transfer error. However, if SIUL2 registers are accessed through other PDAC slots, a transfer error will 
be generated.
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
INTC_CTRL 
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
31-2
—
Reserved
1-0
INTC_CTRL
Interrupt register control
This bit controls the interrupt register.
9.8 Glossary
VM
Virtualized module, such as SIUL2.
PDAC
Peripheral domain access control. PDAC and PDAC slot are interchangeable terms.
NXP Semiconductors
Virtualization Wrapper (VIRT_WRAPPER) for all chips except S32K388 and S32K389
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
302 / 5251


---