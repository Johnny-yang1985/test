# 페이지 505

Chapter 67
System Timer Module (STM)
67.1 Chip-specific STM information
67.1.1 STM instances and configuration
This chip has up to four instances of STM, one for each Cortex-M7 core. The STM counter increments at the STM module clock 
frequency divided by a pre-scaled value.
Table 434. STM instances
Instance
S32K388/
S32K389
S32K358/
S32K348/
S32K338/
S32K328
S32K322/S32K342/S32K341/S32K314/
S32K324/S32K344
S32K310/S32K311/S32K312
STM_0
Yes
Yes
Yes
Yes
STM_1
Yes
Yes
Yes
No
STM_2
Yes
Yes
No
No
STM_3
Yes
No
No
No
Table 435. STM configuration
Instance
Description
Number of 
Channels
Number of 
Registers (32-bit)
STM_0
Intended for Cortex-M7_0 core
4
14
STM_1
Intended for Cortex-M7_1 core
4
14
STM_2
Intended for Cortex-M7_2 core
4
14
STM_3
Intended for Cortex-M7_3 core
4
14
67.2 Overview
STM supports commonly required system and application software timing functions. STM includes a 32-bit count-up timer and four 
32-bit compare channels with a separate interrupt source for each channel. The timer is driven by the STM module clock divided 
by an 8-bit prescale value (1 to 256).
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2814 / 5251


---
# 페이지 506

67.2.1 Block diagram
Clock
CNT[CNT]
CIR0[CIF]
CMP0[CMP]
32-bit counter
=
CR[TEN]
CCR0[CEN]
CIR1[CIF]
CMP1[CMP]1
=
CCR1[CEN]
CIR2[CIF]
CMP2[CMP]
=
CCR2[CEN]
CIR3[CIF]
CMP3[CMP]
=
CCR3[CEN]
Figure 383. Block diagram
67.2.2 Features
STM has the following features:
• One 32-bit count-up timer with an 8-bit prescaler
• Four 32-bit compare channels
• An independent interrupt source for each channel
• Ability to stop the timer in Debug mode
67.3 Functional description
67.3.1 Count-up timer
STM has one 32-bit count-up timer that serves as the time base for four compare channels. When enabled, the counter increments 
at the module clock frequency divided by a prescaler value in the range from 1 to 256. When enabled in Normal mode, the timer 
increments continuously. The counter rolls over at FFFF_FFFFh to 0000_0000h with no restrictions at this boundary.
67.3.2 Compare channels
STM has four identical compare channels. Each channel includes a channel control register (CCRn), a channel interrupt register 
(CCRn), and a channel compare register (CMPn). When the channel is enabled and its channel compare value matches the timer 
count, STM sets the channel interrupt flag and generates an IRQ on that channel.
NXP Semiconductors
System Timer Module (STM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2815 / 5251


---
# 페이지 507

67.3.3 Behavior in different chip modes
STM supports the chip modes of operation as follows:
Chip mode
STM behavior
Normal
When the timer is enabled (CR[TEN] = 1), the timer counts up continuously.
Debug
If CR[FRZ] = 1, STM stops the timer. Otherwise, when the timer is enabled (CR[TEN] = 1), the timer 
counts up continuously.
67.3.4 Clocking
This module has no clocking considerations.
67.3.5 Interrupts
STM can generate a channel interrupt. For information, see:
• Compare channels
• Respond to compare channel events
• Channel Interrupt (CIR0 - CIR3)
67.4 External signals
This module has no external signals.
67.5 Initialization
This module does not require initialization.
67.6 Application information
67.6.1 Configure the timer
1. Set the initial timer count (CNT[CNT]).
2. Specify STM behavior in chip Debug mode (CNT[FRZ]).
3. Set the counter prescaler (CR[CPS]).
4. Start the timer (CR[TEN]).
67.6.2 Configure the compare channels
For each compare channel:
1. Set the channel compare value (CMPn[CMP]).
2. Enable the compare channel (CCRn[CEN]).
67.6.3 Respond to compare channel events
For each compare channel:
1. Check the channel interrupt flag (CIRn[CIF]).
2. If the channel interrupt flag is set, respond to the interrupt request.
3. When the channel interrupt has been handled, clear the channel interrupt flag (CIRn[CIF]).
NXP Semiconductors
System Timer Module (STM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2816 / 5251


---
# 페이지 508

67.7 STM register descriptions
The STM programming model allows only 32-bit (word) accesses. An attempted reference using a different size or to a reserved 
address generates a bus error termination.
67.7.1 STM memory map
STM_0 base address: 4027_4000h
STM_1 base address: 4047_4000h
STM_2 base address: 4047_8000h
STM_3 base address: 4047_C000h
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
0000_0000h
4h
Count (CNT)
32
RW
0000_0000h
10h
Channel Control (CCR0)
32
RW
0000_0000h
14h
Channel Interrupt (CIR0)
32
RW
0000_0000h
18h
Channel Compare (CMP0)
32
RW
0000_0000h
20h
Channel Control (CCR1)
32
RW
0000_0000h
24h
Channel Interrupt (CIR1)
32
RW
0000_0000h
28h
Channel Compare (CMP1)
32
RW
0000_0000h
30h
Channel Control (CCR2)
32
RW
0000_0000h
34h
Channel Interrupt (CIR2)
32
RW
0000_0000h
38h
Channel Compare (CMP2)
32
RW
0000_0000h
40h
Channel Control (CCR3)
32
RW
0000_0000h
44h
Channel Interrupt (CIR3)
32
RW
0000_0000h
48h
Channel Compare (CMP3)
32
RW
0000_0000h
67.7.2 Control (CR)
Offset
Register
Offset
CR
0h
Function
Contains fields for the prescale value, freeze control, and timer enable.
NXP Semiconductors
System Timer Module (STM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2817 / 5251


---
# 페이지 509

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
CPS 
0
FRZ 
TEN 
W
Reset
0
0
0
0
0
0
0
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
15-8
CPS
Counter Prescaler
Selects the module clock divide value for the prescaler (1–256).
• 00h - Divide module clock by 1
• 01h - Divide module clock by 2
• ...
• FFh - Divide module clock by 256
7-2
—
Reserved
1
FRZ
Freeze
Stops the timer when the chip enters Debug mode.
 
When the chip enters Debug mode, it notifies STM, which in turn uses this field to determine 
timer operation.
  NOTE  
0b - Timer runs in Debug mode
1b - Timer stops in Debug mode
0
TEN
Timer Enable
Enables the module timer.
0b - Disabled
1b - Enabled
NXP Semiconductors
System Timer Module (STM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2818 / 5251


---
# 페이지 510

67.7.3 Count (CNT)
Offset
Register
Offset
CNT
4h
Function
Holds the timer count value.
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
CNT 
W
Reset
0
0
0
0
0
0
0
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
CNT 
W
Reset
0
0
0
0
0
0
0
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
CNT
Timer Count
The time base for all compare channels. When enabled, the timer count increments at the rate of the 
module clock divided by the prescale value.
67.7.4 Channel Control (CCR0 - CCR3)
Offset
Register
Offset
CCR0
10h
CCR1
20h
CCR2
30h
CCR3
40h
Function
Enables channel n of the timer.
NXP Semiconductors
System Timer Module (STM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2819 / 5251


---
# 페이지 511

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
CEN 
W
Reset
0
0
0
0
0
0
0
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
0
CEN
Channel Enable
0b - Disabled
1b - Enabled
67.7.5 Channel Interrupt (CIR0 - CIR3)
Offset
Register
Offset
CIR0
14h
CIR1
24h
CIR2
34h
CIR3
44h
Function
Indicates and clears the interrupt flag for channel n of the timer.
NXP Semiconductors
System Timer Module (STM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2820 / 5251


---
# 페이지 512

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
CIF 
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
0
CIF
Channel Interrupt Flag
Indicates the channel IRQ is asserted due to a match on the channel.
0b - Read: IRQ is not asserted. Write: No effect.
1b - Read: IRQ is asserted. Write: Clear the flag.
67.7.6 Channel Compare (CMP0 - CMP3)
Offset
Register
Offset
CMP0
18h
CMP1
28h
CMP2
38h
CMP3
48h
Function
The compare value for channel n.
NXP Semiconductors
System Timer Module (STM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2821 / 5251


---
# 페이지 513

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
CMP 
W
Reset
0
0
0
0
0
0
0
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
CMP 
W
Reset
0
0
0
0
0
0
0
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
CMP
Channel Compare
If the channel is enabled (CCRn[CEN]), when the timer count (CNT) matches this value, STM asserts the 
channel IRQ and sets the channel interrupt flag (CIRn[CIF]).
67.8 Glossary
IRQ
Interrupt request
NXP Semiconductors
System Timer Module (STM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2822 / 5251


---