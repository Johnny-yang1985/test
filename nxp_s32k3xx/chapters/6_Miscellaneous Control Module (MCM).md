# 페이지 6

Chapter 6
Miscellaneous Control Module (MCM)
6.1 Chip-specific MCM information
6.1.1 MCM instances and configuration
This chip supports up to four instances of MCM:
• MCM_0
• MCM_1
• MCM_2
• MCM_3
 
For S32K358 and S32K338, the reset value for CM7_2 is:
• LMEM_DESC_0: 8706_0000h
• LMEM_DESC_1-2 : 8704_2000h
  NOTE  
Table 29. MCM instances
Instances
S32K388/
S32K389
S32K358/
S32K348/
S32K338/
S32K328
S32K322/S32K324/S32K344/S32K342
S32K312/S32K311/
S32K310/S32K314
MCM_0
Yes
Yes
Yes
Yes
MCM_1
Yes
Yes
Yes
No
MCM_2
Yes
Yes
No
No
MCM_3
Yes
No
No
No
Table 30. Memories for all chips except S32K358/S32K348/S32K338/S32K328/S32K388/S32K389
Memory
S32K311/S32K310/S32K312/S32K314 
(Single core)
S32K322/S32K324 (Dual 
core)
S32K342/S32K344 
(Lockstep mode)
Icache
8 KB
8 KB (per core)
8 KB
Dcache
8 KB
8 KB (per core)
8 KB
ITCM
32 KB
32 KB (per core)
64 KB
DTCM
64 KB
64 KB (per core)
128 KB
Table 31. Memories for S32K358/S32K348/S32K338/S32K328/S32K388/S32K389
Memory
Dual core CM7_0 
and CM7_1
Single core 
CM7_2 1
CM7_0 and CM7_1 
(Lockstep mode
CM7_2 (Lockstep 
mode) 2
CM7_32
Icache
16 KB (per core)
16 KB
16 KB
16 KB
16 KB
Dcache
16 KB (per core)
16 KB
16 KB
16 KB
16 KB
Table continues on the next page...
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
57 / 5251


---
# 페이지 7

Table 31. Memories for S32K358/S32K348/S32K338/S32K328/S32K388/S32K389 (continued)
Memory
Dual core CM7_0 
and CM7_1
Single core 
CM7_2 1
CM7_0 and CM7_1 
(Lockstep mode
CM7_2 (Lockstep 
mode) 2
CM7_32
ITCM
32 KB (per core)
64 KB
64 KB
32 KB
32 KB
DTCM
64 KB (per core)
128 KB
128 KB
64 KB
64 KB
1. Available only in S32K358
2. Available only in S32K388/S32K389
6.2 Overview
MCM provides miscellaneous control functions and contains local memory descriptors for the Cortex-M7 core. For more 
information about core-related registers, see the Cortex-M7 core overview chapter.
 
The terminology in this chapter has been updated to align with Arm's AMBA AHB Protocol Specification, as shown 
in the table below.
Table 32. Updated terms
Updated term
Deprecated term
Manager
Master
Subordinate
Slave
  NOTE  
6.2.1 Features
The MCM includes the following features:
• Program-visible information on the platform configuration and revision
• Floating Point Exception monitor and interrupt control
• Local memory descriptors:
— ITCM
— D0TCM
— D1TCM
— I-cache
— D-cache
6.3 Functional description
6.3.1 Interrupts
MCM generates an interrupt if any of the following are true:
• FPU input denormal interrupt is enabled (FIDCE) and an input is denormalized (FIDC).
• FPU inexact interrupt is enabled (FIXCE) and a number is inexact (FIXC).
• FPU underflow interrupt is enabled (FUFCE) and an underflow occurs (FUFC).
• FPU overflow interrupt is enabled (FOFCE) and an overflow occurs (FOFC).
• FPU divide-by-zero interrupt is enabled (FDZCE) and a divide-by-zero occurs (FDZC).
• FPU invalid operation interrupt is enabled (FIOCE) and an invalid operation occurs (FIOC).
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
58 / 5251


---
# 페이지 8

• Write abort interrupt is enabled (WABE) and a write abort occurs (CORTEX-M7 WABORTS INDICATOR).
Determining interrupt source
To determine the exact source of the interrupt for Cortex-M7 core, qualify the interrupt status flags with the corresponding interrupt 
enable fields.
• MCM_ISCR[31:16] && MCM_ISCR[15:0]
• Search the result for asserted flags, which indicate the exact interrupt sources.
6.4 Memory map and register descriptions
The memory map and register descriptions below describe the registers using byte addresses.
 
The following actions result in bus errors:
• Writing to read-only registers at 0x0.
• Reading from or writing to an address from offset 480h and above.
• Accessing any MCM register while in User mode. These registers are only accessible while in 
Supervisor mode.
  NOTE  
6.4.1 MCM register descriptions
6.4.1.1
MCM memory map
MCM_0_CM7 base address: E008_0000h
MCM_1_CM7 base address: E008_0000h
MCM_2_CM7 base address: E008_0000h
MCM_3_CM7 base address: E008_0000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
SoC-defined Platform Revision (PLREV)
16
R
0000h
2h
Processor Core Type (PCT)
16
R
AC70h
Ch
Core Platform Control (CPCR)
32
RW
0000_0200h
10h
Interrupt Status and Control (ISCR)
32
RW
0000_0000h
30h
Process Identifier (PID)
8
RW
00h
400h
Local Memory Descriptor 0 (LMEM_DESC_0)
32
RW
8606_0000h
404h - 408h
Local Memory Descriptor a (LMEM_DESC_1 - LMEM_DESC_2)
32
RW
8604_2000h
40Ch
Local Memory Descriptor 3 (LMEM_DESC_3)
32
RW
8526_4000h
410h
Local Memory Descriptor 4 (LMEM_DESC_4)
32
RW
8544_6000h
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
59 / 5251


---
# 페이지 9

6.4.1.2
SoC-defined Platform Revision (PLREV)
Offset
Register
Offset
PLREV
0h
Function
Specifies a chip-defined platform revision number. A platform input signal defines the state of this register; it can only be read from 
the IPS programming model. Any attempted write is ignored.
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
PLREV 
W
Reset
0
0
0
0
0
0
0
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
15-0
PLREV
Defines the software-visible revision number, specified by a platform input signal.
6.4.1.3
Processor Core Type (PCT)
Offset
Register
Offset
PCT
2h
Function
Specifies the architecture of the processor core within the platform on the chip. A module input signal defines the state of this 
register, which can only be read from the IPS programming model. Any attempted write is ignored.
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
60 / 5251


---
# 페이지 10

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
PCT 
W
Reset
1
0
1
0
1
1
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
Fields
Field
Function
15-0
PCT
Core Complex Identifier
Identifies the core complex. This MCM design supports the Arm Cortex M7 core.
1010_1100_0111_0000b - Arm Cortex-M7
6.4.1.4
Core Platform Control (CPCR)
Offset
Register
Offset
CPCR
Ch
Function
Defines the arbitration and protection schemes for the two system RAM arrays.
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
CM7_A
HB...
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
Reserved 
Reserv
ed 
Reserv
ed 
Reserved 
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
Fields
Field
Function
31-28
Reserved
Table continues on the next page...
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
61 / 5251


---
# 페이지 11

Table continued from the previous page...
Field
Function
—
27
CM7_AHBSPRI
AHB Subordinate Priority
Indicates the access priority on the AHBS port of the Cortex-M7.
 
This setting has no effect unless enabled by AHBSCR[CTL]1 of the Cortex-M7 core.
  NOTE  
0b - Uses a round-robin arbitration scheme
1b - AHB-subordinate access has priority over a core access
26-11
—
Reserved
10
—
Reserved
9
—
Reserved
8-0
—
Reserved
1. For more information see Cortex-M7 documentation: Arm Cortex-M7 Processor Technical Reference Manual at 
www.arm.com.
6.4.1.5
Interrupt Status and Control (ISCR)
Offset
Register
Offset
ISCR
10h
Function
Defines the configuration and reports the status for a number of core-related interrupt exception conditions. It includes:
• Enable and status fields associated with the core's floating-point exceptions
• Bus errors associated with the core's cache write buffer
The individual event indicators are first qualified with their exception enables, and then logically summed to form an interrupt 
request sent to the core's NVIC.
Bits 15-8 are read-only indicator flags based on the processor's FPSCR register. Attempted writes to these fields are ignored. 
When these flags are 1, they retain this value until software clears the corresponding FPSCR field. For more information see 
Cortex-M7 documentation: Arm Cortex-M7 Processor Technical Reference Manual at www.arm.com.
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
62 / 5251


---
# 페이지 12

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
FIDCE 
0
FIXCE 
FUFC
E 
FOFC
E 
FDZC
E 
FIOCE 
0
WABE 
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
FIDC 
0
FIXC 
FUFC 
FOFC 
FDZC 
FIOC 
0
WABS
O 
WABS 
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
Fields
Field
Function
31
FIDCE
FPU Input Denormal Interrupt Enable
0b - Disable
1b - Enable
30-29
—
Reserved
28
FIXCE
FPU Inexact Interrupt Enable
0b - Disable
1b - Enable
27
FUFCE
FPU Underflow Interrupt Enable
0b - Disable
1b - Enable
26
FOFCE
FPU Overflow Interrupt Enable
0b - Disable
1b - Enable
25
FDZCE
FPU Divide-by-Zero Interrupt Enable
0b - Disable
1b - Enable
24
FIOCE
FPU Invalid Operation Interrupt Enable
0b - Disable
1b - Enable
23-22
Reserved
Table continues on the next page...
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
63 / 5251


---
# 페이지 13

Table continued from the previous page...
Field
Function
—
21
WABE
TCM Write Abort Interrupt Enable
0b - Disable
1b - Enable
20-16
—
Reserved
15
FIDC
FPU Input Denormal Interrupt Status
Indicates that an input denormalized number has been detected in the processor's FPU. This field is a 
copy of the core's FPSCR[IDC] field. When this field is 1, it retains this value until software clears the 
FPSCR[IDC] field.
0b - No interrupt
1b - Interrupt occurred
14-13
—
Reserved
12
FIXC
FPU Inexact Interrupt Status
Indicates that an inexact number has been detected in the processor's FPU. This field is a copy of the 
core's FPSCR[IXC] field. When this field is 1, it retains this value until software clears the FPSCR[IXC] 
field.
0b - No interrupt
1b - Interrupt occurred
11
FUFC
FPU Underflow Interrupt Status
Indicates that an underflow has been detected in the processor's FPU. This field is a copy of the core's 
FPSCR[UFC] field. When this field is 1, it retains this value until software clears the FPSCR[UFC] field.
0b - No interrupt
1b - Interrupt occurred
10
FOFC
FPU Overflow Interrupt Status
Indicates that an overflow has been detected in the processor's FPU. This field is a copy of the core's 
FPSCR[OFC] field. When this field is 1, it retains this value until software clears the FPSCR[OFC] field.
0b - No interrupt
1b - Interrupt occurred
9
FDZC
FPU Divide-by-Zero Interrupt Status
Indicates that a divide-by-zero operation has been detected in the processor's FPU. This field is a 
copy of the core's FPSCR[DZC] field. When this field is 1, it retains this value until software clears the 
FPSCR[DZC] field.
Table continues on the next page...
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
64 / 5251


---
# 페이지 14

Table continued from the previous page...
Field
Function
0b - No interrupt
1b - Interrupt occurred
8
FIOC
FPU Invalid Operation Interrupt Status
Indicates that an illegal operation has been detected in the processor's FPU. This field is a copy of the 
core's FPSCR[IOC] field. When this field is 1, it retains this value until software clears the FPSCR[IOC] 
field.
0b - No interrupt
1b - Interrupt occurred
7
—
Reserved
6
WABSO
Write Abort on Subordinate Overrun
The overrun conditions are reported only if WABE=1.
0b - No write abort overrun
1b - Write abort overrun occurred
5
WABS
Write Abort on Subordinate
Indicates when a write abort has occurred on the AHBS interface.
0b - No write abort occurred on AHBS interface
1b - Write abort occurred on AHBS interface
4-0
—
Reserved
6.4.1.6
Process Identifier (PID)
Offset
Register
Offset
PID
30h
Function
Contains the CPU process ID.
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
65 / 5251


---
# 페이지 15

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
Fields
Field
Function
7-0
PID
Process Identifier
Identifies the CPU process.
6.4.1.7
Local Memory Descriptor 0 (LMEM_DESC_0)
Offset
Register
Offset
LMEM_DESC_0
400h
Function
 
The DESC_a registers map to the LMEMs in this way:
• DESC_0: ITCM
• DESC_1: D0TCM
• DESC_2: D1TCM
• DESC_3: I-cache
• DESC_4: D-cache
  NOTE  
 
You can read and write to the reserved fields (instead of read as zero and write ignored). Writing to any of these 
fields has no functional impact.
  NOTE  
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
66 / 5251


---
# 페이지 16

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
LMV 
Reserved 
LMSZ
H 
LMSZ 
WY 
DPW 
Reserv
ed 
W
Reset
1
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
MT 
Reserved 
Reserved 
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
Fields
Field
Function
31
LMV
Local Memory Valid
This read-only field defines the validity (presence) of the local memory.
0b - LMEMn not present
1b - LMEMn present
30-29
—
Reserved
28
LMSZH
LMEM Size Hole
Used for local memories that are not fully populated (that is, local memories that include a memory "hole" 
in the upper 25 % of the address range).
0b - LMEMn is a power-of-2 capacity
1b - LMEMn is not a power-of-2, with capacity of 0.75 × LMSZ
27-24
LMSZ
Local Memory Size
0000b - 0 KB
0001b - 1 KB
0010b - 2 KB
0011b - 4 KB
0100b - 8 KB
0101b - 16 KB
0110b - 32 KB
0111b - 64 KB
1000b - 128 KB
1001b - 256 KB
Table continues on the next page...
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
67 / 5251


---
# 페이지 17

Table continued from the previous page...
Field
Function
1010b - 512 KB
1011b - 1024 KB
1100b - 2048 KB
1101b - 4096 KB
1110b - 8192 KB
1111b - 16384 KB
23-20
WY
Level 1 Cache Ways
0000b - No cache
0010b - 2-way set associative
0100b - 4-way set associative
19-17
DPW
Data Path Width
Defines the LMEMn data path width, which is the width of the local memory.
000b-001b - Reserved
010b - 32 bits
011b - 64 bits
100b-111b - Reserved
16
—
Reserved
15-13
MT
Memory Type
000b - ITCM
001b - DTCM
010b - I-cache
011b - D-cache
12-4
—
Reserved
3-2
—
Reserved
1-0
—
Reserved
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
68 / 5251


---
# 페이지 18

6.4.1.8
Local Memory Descriptor a (LMEM_DESC_1 - LMEM_DESC_2)
Offset
Register
Offset
LMEM_DESC_1
404h
LMEM_DESC_2
408h
Function
 
The DESC_a registers map to the LMEMs in this way:
• DESC_0: ITCM
• DESC_1: D0TCM
• DESC_2: D1TCM
• DESC_3: I-cache
• DESC_4: D-cache
  NOTE  
 
You can read and write to the reserved fields (instead of read as zero and write ignored). Writing to any of these 
fields has no functional impact.
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
LMV 
Reserved 
LMSZ
H 
LMSZ 
WY 
DPW 
Reserv
ed 
W
Reset
1
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
MT 
Reserved 
Reserved 
Reserved 
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
Fields
Field
Function
31
LMV
Local Memory Valid
This read-only field defines the validity (presence) of the local memory.
0b - LMEMn not present
1b - LMEMn present
Table continues on the next page...
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
69 / 5251


---
# 페이지 19

Table continued from the previous page...
Field
Function
30-29
—
Reserved
28
LMSZH
LMEM Size Hole
Used for local memories that are not fully populated (that is, local memories that include a memory "hole" 
in the upper 25 % of the address range).
0b - LMEMn is a power-of-2 capacity
1b - LMEMn is not a power-of-2, with capacity of 0.75 × LMSZ
27-24
LMSZ
Local Memory Size
0000b - 0 KB
0001b - 1 KB
0010b - 2 KB
0011b - 4 KB
0100b - 8 KB
0101b - 16 KB
0110b - 32 KB
0111b - 64 KB
1000b - 128 KB
1001b - 256 KB
1010b - 512 KB
1011b - 1024 KB
1100b - 2048 KB
1101b - 4096 KB
1110b - 8192 KB
1111b - 16384 KB
23-20
WY
Level 1 Cache Ways
0000b - No cache
0010b - 2-way set associative
0100b - 4-way set associative
19-17
DPW
Data Path Width
Defines the LMEMn data path width, which is the width of the local memory.
000b-001b - Reserved
010b - 32 bits
Table continues on the next page...
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
70 / 5251


---
# 페이지 20

Table continued from the previous page...
Field
Function
011b - 64 bits
100b-111b - Reserved
16
—
Reserved
15-13
MT
Memory Type
000b - ITCM
001b - DTCM
010b - I-cache
011b - D-cache
12-4
—
Reserved
3-2
—
Reserved
1-0
—
Reserved
6.4.1.9
Local Memory Descriptor 3 (LMEM_DESC_3)
Offset
Register
Offset
LMEM_DESC_3
40Ch
Function
 
The DESC_a registers map to the LMEMs in this way:
• DESC_0: ITCM
• DESC_1: D0TCM
• DESC_2: D1TCM
• DESC_3: I-cache
• DESC_4: D-cache
  NOTE  
 
You can read and write to the reserved fields (instead of read as zero and write ignored). Writing to any of these 
fields has no functional impact.
  NOTE  
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
71 / 5251


---
# 페이지 21

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
LMV 
Reserved 
LMSZ
H 
LMSZ 
WY 
DPW 
Reserv
ed 
W
Reset
1
0
0
0
0
1
0
1
0
0
1
0
0
1
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
MT 
Reserved 
Reserved 
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
LMV
Local Memory Valid
This read-only field defines the validity (presence) of the local memory.
0b - LMEMn not present
1b - LMEMn present
30-29
—
Reserved
28
LMSZH
LMEM Size Hole
Used for local memories that are not fully populated (that is, local memories that include a memory "hole" 
in the upper 25 % of the address range).
0b - LMEMn is a power-of-2 capacity
1b - LMEMn is not a power-of-2, with capacity of 0.75 × LMSZ
27-24
LMSZ
Local Memory Size
0000b - 0 KB
0001b - 1 KB
0010b - 2 KB
0011b - 4 KB
0100b - 8 KB
0101b - 16 KB
0110b - 32 KB
0111b - 64 KB
1000b - 128 KB
1001b - 256 KB
Table continues on the next page...
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
72 / 5251


---
# 페이지 22

Table continued from the previous page...
Field
Function
1010b - 512 KB
1011b - 1024 KB
1100b - 2048 KB
1101b - 4096 KB
1110b - 8192 KB
1111b - 16384 KB
23-20
WY
Level 1 Cache Ways
0000b - No cache
0010b - 2-way set associative
0100b - 4-way set associative
19-17
DPW
Data Path Width
Defines the LMEMn data path width, which is the width of the local memory.
000b-001b - Reserved
010b - 32 bits
011b - 64 bits
100b-111b - Reserved
16
—
Reserved
15-13
MT
Memory Type
000b - ITCM
001b - DTCM
010b - I-cache
011b - D-cache
12-4
—
Reserved
3-2
—
Reserved
1-0
—
Reserved
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
73 / 5251


---
# 페이지 23

6.4.1.10
Local Memory Descriptor 4 (LMEM_DESC_4)
Offset
Register
Offset
LMEM_DESC_4
410h
Function
 
The DESC_a registers map to the LMEMs in this way:
• DESC_0: ITCM
• DESC_1: D0TCM
• DESC_2: D1TCM
• DESC_3: I-cache
• DESC_4: D-cache
  NOTE  
 
You can read and write to the reserved fields (instead of read as zero and write ignored). Writing to any of these 
fields has no functional impact.
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
LMV 
Reserved 
LMSZ
H 
LMSZ 
WY 
DPW 
Reserv
ed 
W
Reset
1
0
0
0
0
1
0
1
0
1
0
0
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
MT 
Reserved 
Reserved 
Reserved 
W
Reset
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
LMV
Local Memory Valid
This read-only field defines the validity (presence) of the local memory.
0b - LMEMn not present
1b - LMEMn present
30-29
Reserved
Table continues on the next page...
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
74 / 5251


---
# 페이지 24

Table continued from the previous page...
Field
Function
—
28
LMSZH
LMEM Size Hole
Used for local memories that are not fully populated (that is, local memories that include a memory "hole" 
in the upper 25 % of the address range).
0b - LMEMn is a power-of-2 capacity
1b - LMEMn is not a power-of-2, with capacity of 0.75 × LMSZ
27-24
LMSZ
Local Memory Size
0000b - 0 KB
0001b - 1 KB
0010b - 2 KB
0011b - 4 KB
0100b - 8 KB
0101b - 16 KB
0110b - 32 KB
0111b - 64 KB
1000b - 128 KB
1001b - 256 KB
1010b - 512 KB
1011b - 1024 KB
1100b - 2048 KB
1101b - 4096 KB
1110b - 8192 KB
1111b - 16384 KB
23-20
WY
Level 1 Cache Ways
0000b - No cache
0010b - 2-way set associative
0100b - 4-way set associative
19-17
DPW
Data Path Width
Defines the LMEMn data path width, which is the width of the local memory.
000b-001b - Reserved
010b - 32 bits
011b - 64 bits
100b-111b - Reserved
Table continues on the next page...
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
75 / 5251


---
# 페이지 25

Table continued from the previous page...
Field
Function
16
—
Reserved
15-13
MT
Memory Type
000b - ITCM
001b - DTCM
010b - I-cache
011b - D-cache
12-4
—
Reserved
3-2
—
Reserved
1-0
—
Reserved
6.5 Glossary
ITCM
Instruction Tightly-Coupled Memory
DTCM
Data Tightly Coupled Memory
I-cache
Instruction Cache Memory
D-cache
Data Cache Memory
NXP Semiconductors
Miscellaneous Control Module (MCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
76 / 5251


---