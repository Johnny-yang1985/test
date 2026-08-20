# 페이지 30

Chapter 3
Memory Map
3.1 Introduction
This chip contains various memories and memory-mapped peripherals that are placed in a 32-bit contiguous memory space, and 
this chapter describes the memory and peripheral locations within that memory space.
For high-level chip memory map details, see the memory map file attached to this document.
3.2 SRAM memory map
The memory map file attached to this document provides a complete architectural address space definition for various sections 
that the RAM is partitioned into and across the S32K3xx product series. Based on the physical sizes of the memories and 
peripherals, the actual address regions used may be smaller. For details see chapter 'Memory and Memory Interfaces'.
3.3 Access-related details of the memory types used in this chip
The Cortex-M7 core can access these memories sequentially:
• ITCM
• DTCM
• I-cache
• D-cache
ITCM and DTCM can be accessed via 32-bit AHBS interface by any master, e.g., different Cortex-M7 cores, eDMA, etc to bootload 
instructions in ITCM. EMAC is another master that can access DTCM. See 'Block diagram' in the 'Introduction' chapter for details 
on the transaction path.
Access to SRAM beyond the RAM available on the chip terminates the bus cycle with an error followed by an appropriate response 
in the requesting bus master.
3.4 TCM as system memory
On multi–core device, all enabled core and non–core masters can use TCMs of the disabled core. In order to allow use of ITCM 
and DTCM of the disabled core as system memories the following steps must be executed by enabled core:
1. Write 1 to MC_ME's PRTN2_COFB1_CLKEN[REQ62] field for Cortex-M7_0, PRTN2_COFB1_CLKEN[REQ63] field for 
Cortex-M7_1, PRTN2_COFB2_CLKEN[REQ64] field for Cortex-M7_2, and PRTN2_COFB2_CLKEN[REQ65] field for 
Cortex-M7_3. This enables the Cortex-M7 core's TCM controller clock.
2. . Write 1 to DCM_GPR's DCMRWF4[CM7_0_CPUWAIT] field for Cortex-M7_0, DCMRWF4[CM7_1_CPUWAIT] field 
for Cortex-M7_1, DCMRWF4[CM7_2_CPUWAIT] field for Cortex-M7_2, and DCMRWF4[CM7_3_CPUWAIT] field for 
Cortex-M7_3. This configures the core operation in Wait mode.
3. Write 1 to MC_ME's PRTN0_CORE0_PCONF[CCE] field for Cortex-M7_0, PRTN0_CORE1_PCONF[CCE] field for 
Cortex-M7 _1, PRTN0_CORE4_PCONF[CCE] field for Cortex-M7_2, and PRTN0_CORE3_PCONF[CCE] field for 
Cortex-M7_3. This enables the Cortex-M7 core's clock.
Table 6. TCM modes of operation
Description
Control bit (Internal signal)
Cortex-M7 and 
TCM mode
Table continues on the next page...
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
36 / 5251


---
# 페이지 31

Table 6. TCM modes of operation (continued)
PRTN2_COFBi_CLKEN[RE
Q62+n] 1
DCMRWF4[CM7_n_CP
UWAIT]
PRTN0_COREn_PCON
F[CCE]
CM7_n 
mode
CM7_n_T
CM 
backdoor 
enabled
Application 
configurations
—
0
1
RUN
Yes
0
1
1
WAIT
Yes
1
1
1
WAIT
Yes
—
—
0
Disabled
No
1. where i represent 1 for Cortex-M7_0/1 and 2 for Cortex-M7_2/3
3.5 Considerations related to TCM's implementation
You must first initialize TCM (ITCM and DTCM) and system RAMs by 64-bit writes before performing read accesses. The system 
RAM can be initialized using eDMA and core. The ITCM initialization can be performed only by core using either direct or back-door 
accesses. ITCM initialization via back-door can be done by using STM (Store Multiple) with even number of registers. STRD (Store 
Dual) instruction would not work.
The DTCM can be initialized also by 32-bit writes performed either using core's direct and back-door accesses using eDMA. These 
writes are required to set up the initial ECC code words after chip power-on reset.
Each Cortex-M7 core is equipped with a 32 KB ITCM and 64 KB DTCM with a zero wait-state access. In the lockstep operation, 
the checker core's TCM is added to the primary core.
See table 'Memory ECC initialization summary' in chapter 'Memory and Memory Interfaces' for details on memory 
ECC initialization.
3.6 Flash memory map
For details, see the memory map file attached to this document.
3.7 AIPS-Lite memory map
You can access the peripheral memory map via a crossbar slave port. The next table shows the three regions associated with 
peripheral space.
Table 7. Regions associated with peripheral space
Address of region
Region description
4000_0000h–401F_FFFFh
This 2048 KB region (AIPS_Lite_0) is partitioned into 128 spaces, each 16 KB 
in size, having 32 on-platform and 96 off-platform spaces. AIPS_Lite generates 
unique module enables for all the 32 on-platform spaces.
4020_0000h–403F_FFFFh
This 2048 KB region (AIPS_Lite_1) is partitioned into 128 spaces, each 16 KB 
in size, having 32 on-platform and 96 off-platform spaces. AIPS_Lite generates 
unique module enables for all the 32 on-platform spaces.
4040_0000h–405F_FFFFh
This 2048 KB region (AIPS_Lite_2) is partitioned into 128 spaces, each 16 KB 
in size, having 32 on-platform and 96 off-platform spaces. AIPS_Lite generates 
unique module enables for all the 32 on-platform spaces.
Modules that are disabled via their clock gate control fields in the MC_CGM registers disable the associated AIPS_Lite slots. 
Access to any address within an unimplemented or disabled peripheral bridge slot results in a transfer error termination.
NXP Semiconductors
Memory Map
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
37 / 5251


---
# 페이지 32

Multiple instances of same peripherals are connected to different bridges on the interconnect. For details, see the memory map 
file attached to this document.
3.8 Serialization of memory operations
In particular cases, you must complete the process of writing to a peripheral before the subsequent action occurs. Examples of 
such situations include:
• Exiting an interrupt service routine
• Changing a mode
• Configuring a function
In these situations, you must perform a read-after-write sequence to achieve the required serialization of memory operations. The 
following table provides this sequence.
Table 8. Read-after-write sequence for serialization of memory operations
Step
Action
1
Write to the associated peripheral register.
2
Read the register to verify the write process.
3
Continue with the subsequent operations.
3.9 PPB memory map
PPB is a part of the defined Arm bus architecture and provides access to specific processor-local modules. You can access these 
modules only through the core, and not through other system masters.
Table 9. PPB memory map
Starting hex address
Ending hex address
Size (KB)
Module
E000_0000
E000_0FFF
4
ITM
E000_1000
E000_1FFF
DWT
E000_2000
E000_2FFF
FPB
E000_3000
E000_DFFF
44
—
E000_E000
E000_EFFF
4
SCS
E000_F000
E003_FFFF
196
Reserved
E004_0000
E004_0FFF
4
TPIU
E004_1000
E004_1FFF
ETM
E004_2000
E004_2FFF
CTI
E004_3000
E004_3FFF
—
E004_4000
E004_4FFF
E004_5000
E004_5FFF
E004_6000
E007_FFFF
232
E008_0000
E008_0FFF
4
MCM
E008_1000
E008_1FFF
—
Table continues on the next page...
NXP Semiconductors
Memory Map
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
38 / 5251


---
# 페이지 33

Table 9. PPB memory map (continued)
Starting hex address
Ending hex address
Size (KB)
Module
E008_2000
E008_2FFF
E008_3000
E00F_EFFF
496
E00F_F000
E00F_FFFF
4
Cortex-M7 PPB ROM table
3.10 Glossary
CTI
Cross trigger interface
DTCM
Data tightly coupled memory
D-cache
Data cache
DWT
Debug watchpoint and trace
ETM
Embedded trace macrocell
FPB
Flash patch and breakpoints
ITCM
Instruction tightly coupled memory
I-cache
Instruction cache
ITM
Instrumentation trace macrocells
PPB
Private peripheral bus
SCS
System control space
SRAM
Static random access memory
TPIU
Trace port interface unit
NXP Semiconductors
Memory Map
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
39 / 5251


---