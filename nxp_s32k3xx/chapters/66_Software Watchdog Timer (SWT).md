# 페이지 487

Chapter 66
Software Watchdog Timer (SWT)
66.1 Chip-specific SWT information
66.1.1 SWT instances and configuration
This chip supports up to four instances of SWT, one for each Cortex-M7 core.
Table 430. SWT instances
Instance
S32K388/
S32K389
S32K358
S32K348
S32K338
S32K328
S32K322/
S32K324
S32K310/S32K311/
S32K312/S32K314/
S32K342/
S32K341/S32K344
SWT_0
Yes
Yes
Yes
Yes
Yes
Yes
Yes
SWT_1
Yes
Yes
No
Yes
Yes
Yes
No
SWT_2
Yes
No
No
Yes
No
No
No
SWT_3
Yes
No
No
No
No
No
No
Table 431. SWT configuration
Instance
Core
Reset type
Clock Source
SWT_MIN_TO 
(100μs)
SWT_TO_RST (25ms)
SWT_01
Cortex-M7_0
Functional Reset - 
RAM retention
SIRC (32K)
3
320h
SWT_1
Cortex-M7_1
Functional Reset - 
RAM retention
SIRC (32K)
3
320h
SWT_2
Cortex-M7_2
Functional Reset - 
RAM retention
SIRC (32K)
3
320h
SWT_3
Cortex-M7_3
Functional Reset - 
RAM retention
SIRC (32K)
3
320h
1. SWT_0 supports operation in STANDBY mode.
 
When using SWT as a wakeup source from standby, software should ensure proper value of timeout such that SWT 
timeout doesn't get expired again (after wakeup till standby exit is completed). The timeout should be programmed 
to a value greater than the time till standby exit is complete (sum of standby exit time and the time till software 
disables padkeeping).
  NOTE  
 
The "Reset only the SWT" feature using SWT_RRR[RRF] is supported only when SWT reset reaction is demoted 
to interrupt within MC_RGM.
  NOTE  
Protect SWT from service by non-core initiators
You must program protection for the SWT registers so that only core initiators can service SWT.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2796 / 5251


---
# 페이지 488

When an SWT timeout takes place, the logic generating a reset to the system runs off the slow internal RC oscillator (32KHz). It 
could therefore take the SWT almost 31.25μs to reset the system, after timeout, leaving more time for runaway code to execute. 
The register interface clock of SWT is running from AIPS_SLOW_CLK, see Clocking chapter for more details. The register 
interface clock is responsible for generating the abort for invalid access while the counter clock is responsible for generating the 
SWT reset request. Since there is a synchronization happening between the register interface clock and counter clock domains 
before generating the SWT reset request, thus the generation of the reset request can take a number of register interface clock 
cycles after an invalid access is done.
66.2 Overview
The Software Watchdog Timer (SWT) is a 32-bit window watchdog timer that enables the system to recover from situations 
such as:
• Software trapped in a loop
• A bus transaction failing to terminate
In regular operation, SWT requires periodic execution of a watchdog servicing operation. The servicing operation resets the timer 
to a specified timeout period. If this servicing action does not occur before the timer expires, SWT generates an interrupt or a 
hardware reset request.
You can configure SWT to generate a reset request or an interrupt on the initial timeout. SWT always generates a reset request 
on a second consecutive timeout.
 
Terminology in this chapter has been updated as follows:
Table 432. Updated terms
Updated terms
Deprecated term
Initiator
Master
  NOTE  
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2797 / 5251


---
# 페이지 489

66.2.1 Block diagram
PROGRAMMING
MODEL
REGISTERS
Peripheral bus
Stop
Debug
SWT Clock
Clock
RESET_B
RESET_SWT_B
SWT
COUNTER
Counter
evaluation
logic
CO
Figure 381. SWT block diagram
66.2.2 Features
SWT has the following features:
• 32-bit countdown timer
• Selection of regular or window servicing
• Selection of reset request or interrupt on an initial timeout
• Selection of fixed or keyed service sequence
• Initiator access protection
• Hard and soft configuration lock bits
66.3 Functional description
66.3.1 Behavior in different chip and core modes
SWT supports the core modes of operation as follows:
Core mode
SWT behavior
Normal
When SWT is enabled (CR[WEN] = 1), the SWT timer counts down continuously.
Debug
If CR[FRZ] = 1, SWT stops the timer; otherwise, the timer continues to run.
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2798 / 5251


---
# 페이지 490

66.3.2 Register access latency
Accesses to SWT registers occur with no peripheral bus wait states. The peripheral bus bridge may add 1 or more system wait 
states. However, due to synchronization logic in the SWT design, recognition of the service sequence or configuration changes 
may require up to three system clock cycles plus seven counter clock cycles.
66.3.3 Service key generation
SWT generates service keys with the pseudorandom key generator defined by the following equation.
Figure 382. Pseudorandom key generator
This algorithm generates a sequence of 216 different key values before repeating. In keyed service sequence mode, each time 
you write a valid key to SR[WSC], SWT updates SK[SK] with the next key.
For example, if the previous service key (SK[SK]) is 100h, then the next service sequence keys are 1103h followed by 2136h.
66.3.4 Clocking
The SWT has two clock domains, one for the IPS interface and the other for the counter and reset request logic. The two clocks 
can be asynchronous to each other and have independent resets.
See the chip-specific SWT information for the clock source of the counter and reset logic.
See the chip-specific SWT information to find the clock source that drives the countdown timer.
66.3.5 Reset
The following table describes the SWT resets:
Table 433. SWT resets
Reset
Description
RESET_B
It is used to reset the programming model registers.
RESET_SWT_B
It is used to reset the functional domain of the SWT.
66.3.6 Interrupts
The SWT generates one interrupt:
• Timeout interrupt: it is asserted when the watchdog timer count exceeds the timeout period in the TO register.
66.3.7 Reset only the SWT
When a timeout triggers a reset request and the application does not require a system reset, you can make the SWT instance reset 
itself rather than the whole system.
To make a timeout reset request trigger only an SWT reset (rather than the whole system), write 1 to the Reset Request 
Flag (RRR[RRF]).
This action causes SWT to:
• Clear the reset request.
• If an interrupt request also occurred, clear the interrupt request (IR[TIF]).
• Reset and restart the SWT.
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2799 / 5251


---
# 페이지 491

For systems with multiple SWT instances, this feature allows you to reset an individual SWT instance, avoiding the widespread 
impact of a system reset.
66.3.8 Test SWT operation
When you disable SWT, it loads the current countdown timer into CO[CNT]. When you enable SWT, it clears this register. You 
can use CO[CNT] to perform a software self-test of SWT.
To test SWT operation:
1. Enable the SWT (CR[WEN] = 1).
2. Do not service SWT for a fixed period of time that is less than the timeout value.
3. Disable the SWT (CR[WEN] = 0).
4. Read the value in CO[CNT] to determine whether the internal countdown timer is working properly.
 
The value shown in CO[CNT] can lag behind the actual internal timer up to six system clock cycles plus eight 
counter clock cycles.
  NOTE  
66.4 External signals
This module has no external signals.
66.5 Initialization
66.5.1 Initialize the SWT
To initialize the SWT, you must do the following:
• Set the timeout period.
• Control timeout behavior. There are two options:
— Select reset request on timeout, or
— Select interrupt on initial timeout.
You must initialize all registers before enabling SWT (CR[WEN]). You can initialize the registers in any sequence.
66.5.1.1
Set the timeout period
When you enable SWT, it loads the greater of the specified watchdog timeout period or the minimum timeout period into an internal 
32-bit countdown timer every time you perform a valid service operation.
To set the watchdog timeout period:
• Write the desired timeout period to TO[WTO].
The minimum timeout period is 3 clock cycles.
66.5.1.2
Control timeout behavior
SWT can respond to a timeout in one of two ways:
• Generate an immediate reset request on any timeout.
• Generate an interrupt and load the countdown timer on an initial timeout, then generate a reset request on a subsequent 
timeout.
66.5.1.2.1
Select reset request on timeout
To configure SWT to generate an immediate reset request on any timeout:
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2800 / 5251


---
# 페이지 492

• Write 0 to CR[ITR].
66.5.1.2.2
Select interrupt on initial timeout
To configure SWT to generate an interrupt on an initial timeout:
• Write 1 to CR[ITR].
In this configuration, on the initial timeout:
• SWT loads the countdown timer with the timeout period (TO[WTO]).
• SWT indicates the interrupt with the timeout interrupt flag (IR[TIF]).
• If a second consecutive timeout occurs before writing the service sequence for the first timeout, SWT generates a reset 
request.
You clear the interrupt flag by writing 1 to IR[TIF].
66.5.1.3
Configure locking and unlocking
You can lock the SWT configuration with either a hard lock or a soft lock. When either lock is in effect, CR, TO, WN, and SK 
are read-only.
66.5.1.3.1
Enable the hard lock
To enable the hard lock:
• Write 1 to CR[HLK].
Hard lock is disabled only by a reset.
66.5.1.3.2
Enable the soft lock
To enable the soft lock:
• Write 1 to CR[SLK].
66.5.1.3.3
Unlock the soft lock
To unlock the soft lock:
1. Write C520h to SR[WSC].
2. Write D928h to SR[WSC].
This unlock sequence:
• Ignores service sequence writes.
• Recognizes the unlock sequence regardless of previous writes.
• Recognizes the unlock sequence regardless of the time between writes.
• Does not require CR[WEN] to be 1.
You can write this unlock sequence at any time.
 
It is possible for a keyed service sequence to unlock soft lock. See Avoid soft unlock for the procedure to handle 
this situation.
  NOTE  
66.5.1.3.4
Avoid soft unlock
When SWT operates in keyed sequence service, the sequence of service keys generated by the pseudorandom generator 
includes the unlock keys for soft lock. If one or more service routines use both unlock keys in the proper order, 0xC520 followed 
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2801 / 5251


---
# 페이지 493

at any future time by 0xD928, SWT unlocks soft lock (CR[SLK] = 0). The unlock sequence logic ignores any service keys other 
than the unlock keys, so the unlock keys don’t have to be inserted consecutively. If the second unlock key is also the second key 
of a service operation, unlock occurs before the service operation completes.
To avoid unlock:
If the service routine writes a key value of C520h to SR[WSC] as a key of the service operation, then do the following:
1. Complete the service operation.
2. Complete the unlock sequence by writing the second unlock key, D928h, to SR[WSC].
3. Reinitiate the soft lock (CR[SLK] = 1).
66.5.1.4
Select behavior on an invalid access
SWT can respond to an invalid access one of two ways:
• Generate a bus error.
• Generate a bus error and, if SWT is enabled, a reset request.
To select how SWT responds to an invalid access:
• Write the appropriate value to CR[RIA].
66.5.2 Initiate service operations
When enabled, SWT requires periodic execution of a servicing operation.
SWT can operate in one of the following service sequence modes:
• Fixed service sequence
• Keyed service sequence
66.5.2.1
Initiate a fixed service sequence
To initiate the fixed service sequence:
1. Select the fixed servicing mode (write 00b to CR[SMD]).
2. Write A602h to SR[WSC].
3. Write B480h to SR[WSC].
There is no timing requirement between the two writes. The service sequence logic ignores unlock-sequence writes.
66.5.2.2
Initiate a keyed service sequence
To initiate the keyed service sequence:
1. Select the keyed servicing mode (write 01b to CR[SMD]).
2. Read the initial service key from SK[SK].
3. Calculate the next service key using the provided equation.
4. Write that service key to SR[WSC].
5. Repeat steps 2 through 4 one time.
See Service key generation for information about service keys.
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2802 / 5251


---
# 페이지 494

66.5.2.3
Select window service mode
In window service mode, you must write the service sequence only when the watchdog timer is less than the window start value 
(WN[WST]). If you write the service sequence outside of this window, the access is invalid and generates a bus error or reset 
request depending on the Reset on Invalid Access setting (CR[RIA]).
For example, if the timeout period is 5000 and the window start value is 1000, you must write the service sequence during the last 
20% of the timeout period.
Synchronization logic in SWT causes a slight delay in the opening of the window. This delay can be up to three system clock cycles 
plus four counter clock cycles.
To select window service mode:
• Write 1 to (CR[WND]).
66.6 SWT register descriptions
The SWT programming model allows only 32-bit (word) accesses.
Any of the following attempted accesses are invalid:
• Non-32-bit accesses
• Writes to read-only registers
• Writes of incorrect values to SR when SWT is enabled
• Accesses to reserved addresses
• Accesses by initiators without permission
You control how SWT responds to an invalid access with CR[RIA].
66.6.1 SWT memory map
SWT_0 base address: 4027_0000h
SWT_1 base address: 4046_C000h
SWT_2 base address: 4047_0000h
SWT_3 base address: 4007_0000h
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
FF00_010Ah
4h
Interrupt (IR)
32
RW
0000_0000h
8h
Timeout (TO)
32
RW
0000_0320h
Ch
Window (WN)
32
RW
0000_0000h
10h
Service (SR)
32
RW
0000_0000h
14h
Counter Output (CO)
32
R
0000_0000h
18h
Service Key (SK)
32
RW
0000_0000h
1Ch
Event Request (RRR)
32
RW
0000_0000h
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2803 / 5251


---
# 페이지 495

66.6.2 Control (CR)
Offset
Register
Offset
CR
0h
Function
Contains fields for configuring and controlling SWT. The register is read-only if either hard lock or soft lock is enabled (either HLK 
or SLK is 1).
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
MAP0 
MAP1 
MAP2 
MAP3 
MAP4 
MAP5 
MAP6 
MAP7 
0
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
SMD 
RIA 
WND 
ITR 
HLK 
SLK 
Reserv
ed 
STP 
FRZ 
WEN 
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
1
0
1
0
Fields
Field
Function
31
MAP0
Initiator Access Protection 0
The platform bus initiator assignments are chip-specific.
The number of this field corresponds to the XRDC DIDs of the bus initiator. MAP0 corresponds to XRDC 
DIDs 0 and 8.
0b - Access disabled
1b - Access enabled
30
MAP1
Initiator Access Protection 1
See the description for MAP0. MAP1 corresponds to XRDC DIDs 1 and 9.
0b - Access disabled
1b - Access enabled
29
MAP2
Initiator Access Protection 2
See the description for MAP0. MAP2 corresponds to XRDC DIDs 2 and 10.
0b - Access disabled
Table continues on the next page...
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2804 / 5251


---
# 페이지 496

Table continued from the previous page...
Field
Function
1b - Access enabled
28
MAP3
Initiator Access Protection 3
See the description for MAP0. MAP3 corresponds to XRDC DIDs 3 and 11.
0b - Access disabled
1b - Access enabled
27
MAP4
Initiator Access Protection 4
See the description for MAP0. MAP4 corresponds to XRDC DIDs 4 and 12.
0b - Access disabled
1b - Access enabled
26
MAP5
Initiator Access Protection 5
See the description for MAP0. MAP5 corresponds to XRDC DIDs 5 and 13.
0b - Access disabled
1b - Access enabled
25
MAP6
Initiator Access Protection 6
See the description for MAP0. MAP6 corresponds to XRDC DIDs 6 and 14.
0b - Access disabled
1b - Access enabled
24
MAP7
Initiator Access Protection 7
See the description for MAP0. MAP7 corresponds to XRDC DIDs 7 and 15.
0b - Access disabled
1b - Access enabled
23-11
—
Reserved
10-9
SMD
Service Mode
00b - Fixed Service Sequence. To service the watchdog, write the fixed sequence 0xA602, 
0xB480 to SR.
01b - Keyed Service Sequence. To service the watchdog, write two pseudorandom key values to 
SR.
10b - Reserved. Do not use this value. Writing this value can cause the watchdog to not be 
serviced.
11b - Reserved. Do not use this value. Writing this value can cause the watchdog not to be 
serviced.
Table continues on the next page...
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2805 / 5251


---
# 페이지 497

Table continued from the previous page...
Field
Function
8
RIA
Reset on Invalid Access
Controls how SWT responds to an invalid access.
 
For a description of how this chip implements SWT reset requests resulting from SWT 
invalid accesses, see the chip-specific SWT information.
  NOTE  
0b - Generate a bus error
1b - Generate a bus error and reset request. If SWT is enabled (WEN = 1), generate a bus error 
and a reset request; otherwise, generate a bus error.
7
WND
Window Mode
Specify regular or window mode operation.
0b - Regular mode. Can execute service sequence at any time
1b - Window mode. Can execute service sequence only when the timeout counter is less than the 
value in WN
6
ITR
Interrupt Then Reset Request
 
For a description of how this chip implements SWT reset requests and interrupt requests 
resulting from SWT timeouts, see the chip-specific SWT information.
  NOTE  
0b - Generate a reset request on a timeout
1b - Generate an interrupt on an initial timeout; generate a reset request on a second consecutive 
timeout
5
HLK
Hard Lock
Indicates that the hard lock is enabled. You cannot directly write 0 to this field. This field becomes 0 only after 
a reset.
0b - CR, TO, WN, and SK are read/write registers if SLK is also 0
1b - CR, TO, WN, and SK are read-only registers
4
SLK
Soft Lock
Indicates that the soft lock is enabled. You cannot directly write 0 to this field. Clear this field by writing the 
unlock sequence to the service register.
0b - CR, TO, WN, and SK are read/write registers if HLK is also 0
1b - CR, TO, WN, and SK are read-only registers
3
—
Reserved
2
Stop Mode Control
Table continues on the next page...
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2806 / 5251


---
# 페이지 498

Table continued from the previous page...
Field
Function
STP
Controls the watchdog timer when the chip enters Stop or Standby mode.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
SWT_0
CR
—
SWT_1
—
CR
SWT_2
—
CR
SWT_3
—
CR
0b - Timer continues
1b - Timer stops
1
FRZ
Debug Mode Control
Controls the watchdog timer when the core enters Debug mode.
0b - Timer continues
1b - Timer stops
0
WEN
Watchdog Enable
Enables or disables SWT.
The reset value is 0. Therefore, after reset, you must enable SWT to start the countdown timer.
0b - Disabled
1b - Enabled
66.6.3 Interrupt (IR)
Offset
Register
Offset
IR
4h
Function
The timeout interrupt flag.
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2807 / 5251


---
# 페이지 499

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
TIF 
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
TIF
Timeout Interrupt Flag
Write 1 to this field to clear the flag and interrupt. Writing a 0 has no effect.
0b - No interrupt request
1b - Interrupt request due to an initial timeout
66.6.4 Timeout (TO)
Offset
Register
Offset
TO
8h
Function
Contains the 32-bit timeout period. The register is read-only if either hard lock or soft lock is enabled (CR[HLK] or CR[SLK] is 1).
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2808 / 5251


---
# 페이지 500

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
WTO 
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
WTO 
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
1
0
0
0
0
0
Fields
Field
Function
31-0
WTO
Watchdog Timeout
Watchdog timeout period in clock cycles. When software writes a service sequence or enables SWT, SWT 
loads the internal 32-bit countdown timer with this value or 3h, whichever is greater.
66.6.5 Window (WN)
Offset
Register
Offset
WN
Ch
Function
Contains the 32-bit window start value. SWT clears this register on reset. The register is read-only if either hard lock or soft lock 
is enabled (CR[HLK] or CR[SLK] is 1).
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
WST 
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
WST 
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
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2809 / 5251


---
# 페이지 501

Fields
Field
Function
31-0
WST
Window Start Value
When you enable window mode (CR[WND]), you can write the service sequence only when the internal 
timer is less than this value.
66.6.6 Service (SR)
Offset
Register
Offset
SR
10h
Function
Initiates the service operation and resets the watchdog timer.
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
W
WSC 
Reset
0
0
0
0
0
0
0
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
15-0
WSC
Watchdog Service Code
Use this field to service the watchdog and to unlock the Soft Lock (CR[SLK]).
To service the watchdog: If SWT is in keyed service mode (CR[SMD]), write two pseudorandom key values 
to WSC (see Service key generation for details). Otherwise, write the following values to WSC, in the 
order shown:
Table continues on the next page...
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2810 / 5251


---
# 페이지 502

Table continued from the previous page...
Field
Function
1. A602h
2. B480h
To unlock the Soft Lock (CR[SLK]), write the following values to WSC, in the order shown:
1. C520h
2. D928h
When read, WSC always returns zero.
66.6.7 Counter Output (CO)
Offset
Register
Offset
CO
14h
Function
Shows the value of the internal timer when SWT is disabled.
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
Watchdog Count
When SWT is disabled (CR[WEN] is 0), CNT shows the value of the internal timer. When SWT is enabled 
(CR[WEN] is 1), it writes 0 to CNT. Values in this field can lag behind the internal timer value up to six 
system clock cycles plus eight counter clock cycles. Therefore, the CNT value that is read immediately after 
disabling SWT may be higher than the actual value of the internal timer.
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2811 / 5251


---
# 페이지 503

66.6.8 Service Key (SK)
Offset
Register
Offset
SK
18h
Function
Holds the previous (or initial) service key value. This register is read-only if either hard lock or soft lock is enabled (CR[HLK] or 
CR[SLK] is 1).
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
SK 
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
15-0
SK
Service Key
Holds the previous (or initial) service key value used in Initiate a keyed service sequence. If CR[SMD] is 01b, 
the next key value to write to SR is (17 * SK + 3) mod 216.
66.6.9 Event Request (RRR)
Offset
Register
Offset
RRR
1Ch
Function
Contains the timeout reset request flag. See the chip-specific information for the specific event associated with this flag.
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2812 / 5251


---
# 페이지 504

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
RRF 
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
RRF
Reset Request Flag
Write 1 to clear the flag and request. Writing 0 has no effect.
0b - No reset request
1b - Any reset request initiated
NXP Semiconductors
Software Watchdog Timer (SWT)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2813 / 5251


---