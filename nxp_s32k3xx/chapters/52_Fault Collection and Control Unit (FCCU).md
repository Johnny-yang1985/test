# 페이지 221

Chapter 52
Fault Collection and Control Unit (FCCU)
52.1 Chip-specific FCCU information
52.1.1 FCCU NCF slots
Table 296. FCCU NCF slots
Slot number
Source module (error type)
NCF[0]
• Cortex-M7 LS and core lockup
NCF[1]
Interconnect:
• All EDC bus gaskets
• XBIC monitors and platform gaskets
NCF[2]
ECC errors:
• PRAMC
• TCMs
• Caches
• eDMA
• EDC after ECC
• QuadSPI1
• AES_ACCEL (include DMA TCD) errors 2
NCF[3]
All flash memory errors:
• FMU
• PFLASH
• DCM flash memory
• Flash Address Remapping3
NCF[4]
Voltage-related errors:
• PMC 1.1 V and 2.5 V GNG
• PMC 1.1 V and 2.5 V GNG21
• Pad overvoltage
NCF[5]
Debug and test monitoring, STCU faults 4
NCF[6]
INTM
NCF[7]
Software notification
1. For S32K358/S32K348/S32K338/S32K328 only.
2. For S32K388/S32K389 only.
3. For S32K389 only.
4. The fault would be raised if DBGPWRUPREQ toggles while any core is in halted state. If this operation is expected, the 
application can ignore/disable such an NCF event.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2138 / 5251


---
# 페이지 222

52.1.2 Chip-boundary FCCU signals
Table 297. Chip-boundary FCCU signals
FCCU signal
Chip signal
EOUT0
FCCU_ERR0
EOUT1
FCCU_ERR1
52.1.3 FCCU clocking
Table 298. FCCU clocking
FCCU clock signal
Chip clock signal
CLKSAFE
FIRC_CLK
CLKPRIM
AIPS_PLAT_CLK
52.1.4 FOSU timer interval
The FOSU_COUNT value determines the FOSU timer interval. On this chip, FOSU_COUNT is 69780h.
52.1.5 Supported internal chip reactions
The short functional reset discussed in this chapter is equivalent to the chip functional reset. See the interrupt map file attached 
to this document for interrupts from FCCU to NVIC.
 
After STCU2 completes the self-testing procedure, the chip reboots and FCCU resets.
  NOTE  
52.1.6 Recommended reaction programming for faults
You can upgrade or downgrade the reaction of the faults according to the recommended reaction discussed in the fault map file 
attached to this document.
In case you upgrade a reaction, no issues are expected in the behavior. If you downgrade the reaction, the functionality is 
not guaranteed.
This is the recommendation for faults caused by lockstep errors:
1. The recommended reaction for the lockstep error fault is a functional reset.
2. Program the core to perform the following steps after rebooting:
a. Initialize TCM (because TCMs can become corrupted)
b. Invalidate the cache (because caches can become corrupted)
3. Write 1 to the corresponding bit in FCCU.NCF_S0 register to clear the non-critical fault status.
4. If the FCCU fault gets cleared, you have nothing else to do for fault handling (this means, the FCCU lockstep error 
is recovered).
5. If the error persists, it indicates that the internal registers of the two cores have different values. To bring them to the same 
value, you could perform any of these steps:
a. Initialize destructive reset through software by using MC_ME.MODE_CONF[DEST_RST] to recover from lockstep. 
This initializes the FCCU with no pending faults.
b. Reconfigure the Cortex-M7 debug configurations (which would have been lost in previous step due to destructive 
reset in the system).
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2139 / 5251


---
# 페이지 223

52.1.7 FCCU NCF handling architecture
This chip supports eight NCFs. Therefore, multiple faults of similar nature are ORed together and then connected as a single NCF 
to FCCU. To control individual fault, there are enable/disable controls provided within DCM in registers DCMRWDn.
Similarly, the FCCU.NCF_S0 captures the status of fault within FCCU. This fault might have resulted due to any fault mapped 
on the corresponding FCCU NCF channel. The DCM status registers DCMRODn capture the status of individual faults which are 
mapped onto FCCU NCFs. Figure 209 shows this arrangement.
Peripheral 1
Fault
reaction
Reset=0
FCCU
Fault
enable [i]
Reset=0
DCM
Fault status [i]
(within DCMRODn)
Fault status [i]
(within DCMRODn)
Fault status [i]
(within DCMRODn)
Fault enable [i]
(within DCMRODn)
Reset=1
Peripheral 2
Peripheral n
Fault enable [i]
(within DCMRODn)
Reset=1
Fault enable [i]
(within DCMRODn)
Reset=1
Figure 209. FCCU NCF handling architecture
52.2 Overview
The FCCU provides a hardware interface to collect faults and to place the device into a safe state when a failure is detected in 
the device. No CPU intervention is requested for collection and control operations. FCCU offers a systematic approach to fault 
collection and control.
52.2.1 Block diagram
The following figure represents a top-level diagram of the FCCU module.
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2140 / 5251


---
# 페이지 224

IPS
MC_RGM,
NMI,IRQ
FAULT intf
FAULT
CLKPRIM
HNSHK 
WDOG
ALRT
FSM
EOUT1 intf
EOUT0 intf
HNSHK 
(Slave)
 
REG intf
PB
EOUT[1]
EOUT[0] EIN[0]
EIN[1]
Figure 210. FCCU block diagram
This table describes the FCCU submodules.
Table 299. FCCU submodules
Submodule
Description
REG intf
Includes the register file, the IPS bus interface, the IRQ interface and the 
parity block (PB) for the configuration registers
HNSHK blocks (master and slave blocks)
Includes the FSM ability to support the handshake between the REG 
interface and the FSM unit because of the usage of two asynchronous 
clocks [CLKPRIM(module clock) and CLKSAFE(RC oscillator clock)]
FSM unit
Implements the main functions of FCCU. The FSM also includes the:
• Watchdog timer (WDG)
• Alarm timer (ALRT)
FAULT intf
Implements the interface for fault conditioning and management
EOUTx units
Implement the output stage to manage the EOUT interfaces
52.2.2 Features
The key features of the FCCU module are these:
• Management of non-critical faults
• HW or SW fault recovery management
• Fault collection from safety relevant modules on the device
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2141 / 5251


---
# 페이지 225

• Fault injection (fake faults)
• Collection of test results
• Lockable configuration
— Changes are only possible after entering the CONFIG state
— Supports a transient and a permanent lock
— Configuration changes observed by a watchdog timer
• Configurable fault control
• External reaction (FAULT state): EOUT signaling. Error indication via the pin(s) is controlled by FCCU.
• Internal chip reactions (ALARM state): interrupt request
• Configurable internal chip reactions for each NCF (FAULT state):
— Short functional reset request pulse
— NMI
— No reaction
— IRQ
• In Bi-Stable operational mode, one of the EOUT signals is high to indicate an OK operational state of FCCU. 
• After power on, the EOUT signals have high impedance.[11] They indicate an operational state only after the software 
configures them. 
• In case of a failure event or on software request for error pin indication, the pin(s) are set to faulty state for a minimum time 
Tmin (see DELTA_T[DELTA_T]), even if the software tries to release it before (for the case of error pin configured in Bi-Stable 
mode only).
The self-checking procedure checks the FCCU circuitry at the start up. The FCCU is operational with the default configuration 
immediately after the completion of the self-checking procedure. Internal (short functional reset request pulse, interrupt request) 
and external (EOUT signaling) reactions are statically defined or programmable. The default configuration can be modified only 
in the Configuration (CONFIG) state. FCCU is designed to function when CLKPRIM is faster than the CLKSAFE clocks.
52.3 Functional description
52.3.1 Definitions
In general, the following definitions are applicable for fault management:
• HW recoverable fault: The fault indication is a level-sensitive signal that remains asserted until the fault cause is deasserted. 
That is, if logical 0 on the fault signal indicates fault, then the status flags are valid as long as the fault line stays at 0. The 
status is automatically cleared when the fault signal goes to 1. Typically the fault signal is latched external to the FCCU in the 
module where the fault occurred. The FCCU state transitions are consequently executed on the state changes of the input 
fault signal. No SW intervention in the FCCU is required to recover the fault condition.
• SW recoverable fault: The fault indication is a signal asserted without a defined time duration. The fault signal is latched in 
the FCCU. The fault recovery is executed following a SW recovery procedure (status/flag register clearing).
HW recoverable is an option to exclude the handling of error sources by FCCU management SW, in case it is known that the fault 
is recoverable by itself when the fault condition is corrected.
For details related to reset interface, see the reset interface section in the chip reference manual.
52.3.2 FSM description
The functionality of FCCU is depicted by the FSM state diagram (see Figure 211).
[11] Actual value depends on device-specific setting at pad level.
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2142 / 5251


---
# 페이지 226

FCCU has four states that are identified with the following meaning:
• CONFIG: Used only to modify the configuration of FCCU from its default. A subset of the FCCU registers, dedicated to define 
the FCCU configuration (global configuration, reactions to fault, timeout, non-critical fault masking) can be accessed in write 
mode only in the CONFIG state.
The CONFIG state is accessible only in the NORMAL state and if the configuration is not locked. A permanent configuration 
lock can be disabled by a reset that also resets the FCCU. The transient lock register is unlocked by writing BCh into it. FCCU 
gets transiently locked again if an invalid key is written into TRANS_LOCK[TRANSKEY] (that is, other than BCh). To lock 
FCCU for configuration, write FFh to PERMNT_LOCK[PERMNTKEY].
After the release of reset, the state of the transient lock is locked, and the state of the permanent lock is unlocked.
The locking feature only restricts the FSM movement into CONFIG state. After the user enters the CONFIG state and then 
tries to lock the configuration, the locking of configuration is effective only after FCCU moves to the NORMAL state; it will not 
be effective in the current CONFIG state.
The CONFIG to NORMAL state transition can be executed by SW or automatically following a timeout condition of the 
watchdog. In case the timeout information and the SW request for state change to NORMAL appears at the same time, 
watchdog timeout has the priority and hence the configuration registers (those that are writable only in the CONFIG state) are 
reset to their default values. The movement to the NORMAL state is made.
The incoming faults, occurring during the configuration phase (CONFIG state) are latched in order to process them when 
FCCU is moved to the NORMAL state, according to the new configuration.
All pending faults that occur during the CONFIG state result in both of the following:
— Highest-priority state transition
— Interrupt generation (NMI or alarm IRQ)
If the state transition occurs, it gives the reset reaction corresponding to the worst case based on all the faults (pending or 
non-pending faults) that occurred during the CONFIG state.
• NORMAL: This is FCCU's operating state when no faults are occurring. It is also the default state on the reset exit. Following 
state transitions occur on one of the following events:
— Unmasked non-critical faults with the timeout disabled: FCCU moves to the FAULT state.
— Unmasked non-critical faults with the timeout enabled: FCCU moves to the ALARM state.
— Masked non-critical faults: FCCU stays in the NORMAL state.
• ALARM: FCCU moves into the ALARM state when an unmasked non-critical fault occurs and the timeout is enabled.
Transition to the ALARM state goes along with an interrupt alarm, if enabled. By definition, this fault may be recovered within a 
programmable timeout period, before it generates a transition to the FAULT state. The timeout is reinitialized if FCCU enters 
the NORMAL state. The timeout restarts following the recovery from the FAULT state.
• FAULT: FCCU moves into the FAULT state when one of the following condition occurs:
— Timeout related to a non-critical fault when FCCU is in the ALARM state
— Unmasked non-critical faults with the timeout disabled
The transition from the NORMAL or ALARM to the FAULT state goes along with the generation of:
• Internal chip reaction—NMI interrupt (optional)
• External reaction—EOUT signaling (optional) 
• Internal chip reaction—SW option: Soft reaction (Short functional reset request pulse if configured) 
• Non Maskable Interrupt (NMI) is routed to all cores.
After moving to the FAULT state, if there is either a previous pending fault or a new fault for which NMI is enabled, NMI generation 
takes place.
Multiple faults can occur at the same time.
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2143 / 5251


---
# 페이지 227

FAULT
Configuration exit OR 
timeout
CONFIG
fault (masked)
NORMAL
All faults recovered
Reset
Fault 
(unmasked AND timeout enabled)
ALARM
Fault not recovered on time 
OR 
Fault 
(unmasked AND timeout disabled)
Fault 
(unmasked AND timeout disabled)
Configuration entry 
AND (configuration unlocked)
recovered
All faults
pending fault (unmasked AND timeout enabled)
  
Any Fault Pending 
AND FCCU_IRQ_ALARM_ENn
Figure 211. FCCU state diagram
52.3.3 Fault priority scheme and nesting
The FAULT state has a higher priority than the ALARM state in case of concurrent fault events (non-critical) that occur in the 
NORMAL state.
The ALARM to FAULT state transition occurs if a non-critical fault (unmasked and with timeout disabled) is asserted in the 
ALARM state.
The ALARM to NORMAL state transition occurs only if all the non-critical faults (including the faults that have been collected after 
the entry in the ALARM state) have been cleared (SW or HW recovery); otherwise the FCCU remains in the ALARM state.
The FAULT to NORMAL state transition occurs only if all the non-critical faults (including the faults that have been collected after 
the entry in the FAULT/ALARM state) have been cleared (SW or HW recovery); otherwise the FCCU moves to the ALARM state 
(if any non-critical fault is still pending and the timeout is not elapsed).
In general, no fault nesting is supported except for the non-critical faults that cause an ALARM to FAULT state transition. In this 
case, the NCF timer is stopped until the FAULT state is recovered. If FCCU is in the ALARM state and another fault occurs, which 
has its alarm timeout enabled, then the alarm timer shall not reload and shall not start again.
52.3.4 Fault recovery
The following timing diagrams describe the main use cases of FCCU in terms of fault events and related recovery.
A typical sequence related to non-critical fault management (ALARM state), see Figure 212 and Figure 213, is as follows:
1. Non-critical fault assertion
2. FCCU state transition (automatic): NORMAL to ALARM
• Alarm interrupt request (if enabled)
• Timeout running
3. System state: RUN
4. Alarm interrupt management: fault recovery
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2144 / 5251


---
# 페이지 228

• FCCU state transition: ALARM to NORMAL
RUN
SW ALARM recovery
Alarm interrupt 
request
Fault event
FCCU reset
System state
FCCU state
NCF timer
NORMAL
NORMAL
IDLE
ALARM
TIMER ON
IDLE
Figure 212. Non-critical fault (ALARM state) SW recovery
RUN
Alarm interrupt 
request
FCCU reset
System state
FCCU state
NCF timer
NORMAL
NORMAL
IDLE
ALARM
TIMER ON
IDLE
Fault event
Figure 213. Non-critical fault (ALARM state) HW recovery
A typical sequence related to non-critical fault management (ALARM to FAULT state), see Figure 214, is as follows:
1. Non-critical fault assertion
2. FCCU state transition (automatic): NORMAL to ALARM
• Alarm interrupt request (if enabled)
• Timeout running
3. FCCU state transition (following the timeout trigger): ALARM to FAULT
• NMI assertion (if enabled)
4. NMI interrupt management (if enabled)
• Fault recovery (by software): FCCU state transition: FAULT to NORMAL
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2145 / 5251


---
# 페이지 229

RUN
SW FAULT recovery
Alarm interrupt 
request
Functional reset request 
(short)
System state
FCCU state
NCF timer
NORMAL
NORMAL
IDLE
ALARM
TIMEOUT
IDLE
NMI
EOUT
FCCU reset
FAULT
SAFE
RUN
TIMER ON
IDLE
IDLE
ERROR ON
Fault event
Figure 214. Non-critical fault (ALARM to FAULT state) recovery
52.3.5 EOUT interface
Introduction
You use the EOUT[1:0] signals to indicate FCCU's condition (or, for Fault-Toggle fault-output mode, faults only) to off-chip logic. 
 
For information on the availability and names of these FCCU signals on the boundary of this chip, see the 
chip-specific FCCU information.
  NOTE  
The FCCU conditions
There are three FCCU conditions:
Condition
Description
Faulty
All of the following are true:
• The fault-output (EOUT) timer is running (see How 
the fault-output (EOUT) timer works in Bi-Stable fault-
output mode).
• FCCU is in FAULT state.
Non-faulty
All of the following are true:
• The fault-output (EOUT) timer is not running.
• FCCU is in ALARM or NORMAL state.
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2146 / 5251


---
# 페이지 230

Table continued from the previous page...
Condition
Description
Configuration
All of the following are true:
• The fault-output (EOUT) timer is not running.
• FCCU is in CONFIG state.
How the fault-output (EOUT) timer works in Bi-Stable fault-output mode
In Bi-Stable fault-output mode (FOM), FCCU starts the fault-output (EOUT) timer when all of the following are true:
• If the EOUT signals are in Bi-Stable FOM, and the EOUT signals are not programmed to be always 
low (CFG[FCCU_SET_CLEAR]).
• The EOUT timer is not already running.
• FCCU enters the FAULT state as the result of a fault.
When the fault-output (EOUT) timer is already running and a new fault occurs:
• If FCCU is in the CONFIG state: FCCU does not restart the EOUT timer.
• If FCCU is in the NORMAL or ALARM state:
— And ALARM state is enabled for the fault (non-critical): FCCU enters (or remains in) the ALARM state but does not 
restart the EOUT timer.
— And ALARM state is disabled for the fault (non-critical): FCCU enters the FAULT state and restarts the EOUT timer.
• If FCCU is in the FAULT state: FCCU restarts the fault-output (EOUT) timer.
FCCU stops and reinitializes the fault-output (EOUT) timer when all of the following are true:
• If the EOUT signals are in Bi-Stable fault-output mode (CFG[FOM]), and Tmin (see DELTA_T[DELTA_T]) has expired.
• All faults that caused FCCU to enter or remain in the FAULT state since FCCU started the fault-output (EOUT) timer have 
been cleared, causing FCCU to return to the NORMAL state.
How the fault-output (EOUT) timer works in Fault-Toggle fault-output mode
In Fault-Toggle fault-output mode, FCCU initializes the fault-output (EOUT) timer with the value of Tmin (see DELTA_T[DELTA_T]) 
and begins decrementing the timer when any of the following are true:
• FCCU enters the FAULT state as the result of a fault.
• In FAULT state, a fault occurs while the EOUT timer is 0 (idle).
• In FAULT state, a fault occurs while the EOUT timer is running because of a previous fault (also called a pending fault), and 
then in any state the EOUT timer reaches 0 (idle).
FCCU stops the EOUT timer when it reaches 0 (idle).
Prepare the EOUT signals to indicate FCCU's condition
• If the EOUT signals are in Bi-Stable or Fault-Toggle fault-output mode (CFG[FOM]), ensure that the EOUT signals are 
controlled by FCCU's FSM (CFG[FCCU_SET_CLEAR]).
• Ensure that the EOUT signals are active (CFG[FCCU_SET_AFTER_RESET]).
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2147 / 5251


---
# 페이지 231

 
If the EOUT signals are in Bi-Stable or Fault-Toggle fault-output mode, you must deactivate and then reactivate the 
EOUT signals (CFG[FCCU_SET_AFTER_RESET]) to correctly initialize them so they have opposite states.
  NOTE  
More about the EOUT interface
Different fault-output modes (protocols) for the fault-output (EOUT) interface are supported (CFG[FOM]):
• Bi-Stable
• Fault-Toggle
 
See the chip-specific FCCU information for the fault-output modes supported by this chip.
  NOTE  
You can further configure the fault-output modes using the following attributes:
Attribute
Field
Setting used in the example diagrams 
and tables that follow
Configuration mode
CFG[CM]
Different
Polarity selection
CFG[PS]
For the faulty indication, EOUT1 is high, 
and EOUT0 is low.
EOUT frequency: This frequency is generated by dividing the CLKSAFE frequency by a fixed factor of 218.
EOUTfreq = 
218
CLKSAFEfreq
For example, with a CLKSAFE frequency of 16 MHz, this drives a signal of 61 Hz on EOUT.
In case of a failure event or on software request for EOUT indication, the signal(s) are set to the faulty state for a minimum time 
(Tmin), even if software tries to release it before. If software configures the error pins to OK(1), and if a fault comes trying to 
drive the pin to NOK(0), then priority is given to the fault indication and the error signals indicate NOK, such as an incoming fault 
is not masked even when software has set the error signal to high. Also, if the error signals are forced to low by software by 
writing to CFG[FCCU_SET_CLEAR], then the signals shall remain low (or high) for the entire duration of Tmin. During the Tmin 
by a non-software fault, the FCCU FSM moves independently of this signal state (low), and as soon as the timer expires, the 
pin behavior is dictated by the state in which the FSM finds itself in, and it is not possible to set the signals to OK by software 
moving FCCU to the CONFIG state, as long as this timer is running. No software intervention is needed to bring the signal from 
the low state.
Software can bring the pin back to OK state by clearing the faults and waiting for the Tmin interval to expire, after which the FCCU 
automatically enters the NORMAL state and the error signal indicates OK.
In case another failure event happens within Tmin after a first one, the Tmin counter is restarted.
52.3.5.1
Bi-Stable protocol
The encoding scheme is provided in Table 300 and the related timing diagram is shown in Figure 215.
Table 300. Bi-Stable encoding
Condition
EOUT[1:0] (CFG[PS] is 0)
EOUT[1:0] (CFG[PS] is 1)
Non-faulty
Static 01
Static 10
Faulty
Static 10
Static 01
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2148 / 5251


---
# 페이지 232

Table 300. Bi-Stable encoding (continued)
Condition
EOUT[1:0] (CFG[PS] is 0)
EOUT[1:0] (CFG[PS] is 1)
Reset
High-impedance (no toggling)1
High-impedance (no toggling)
Configuration 
(CFG[CM] is 1 and 
CFG[FCCU_SET_AFT
ER_RESET] is 0)
High-impedance (no toggling)2
High-impedance (no toggling)
Configuration (When 
CFG[CM] is 1 and 
CFG[FCCU_SET_AFT
ER_RESET] is 1)
Static 01
Static 10
1. Final value depends on device specific settings at pad level.
2. Ensure that the EOUT signals are active (CFG[FCCU_SET_AFTER_RESET]); otherwise, the EOUT signals stay in a 
high-impedance state after reset lifts.
 
Figure 215 is formatted to display the behavior in all four conditions (reset, non-faulty, faulty, and configuration), 
not to imply transitions between one condition and another. In particular, a transition from the faulty condition to the 
configuration condition is not possible.
  NOTE  
Configuration phase
Faulty phase
Non-faulty phase
Reset phase 
or self-test
Input
or high-Z
Output
EOUT[0]
EOUT[1]
Figure 215. Bi-Stable protocol
52.3.5.2
Fault-Toggle protocol
The Fault-Toggle protocol uses the EOUT signals to indicate only the occurrences of faults, not FCCU's condition like the other 
protocols. In Fault-Toggle fault-output mode, when controlled by the FSM (CFG[FCCU_SET_CLEAR]), the EOUT signals:
• Have opposite states
• Toggle their states to indicate a fault and then maintain those new states for at least Tmin (see DELTA_T[DELTA_T]), after 
which they are free to toggle to indicate another fault
FCCU uses the fault-output (EOUT) timer to measure Tmin. For more information, see How the fault-output (EOUT) timer works 
in Fault-Toggle fault-output mode.
The EOUT polarity selection (CFG[PS]) determines the initial states of the EOUT signals, which FCCU applies after you deactivate 
and then reactivate the EOUT signals (CFG[FCCU_SET_AFTER_RESET]).
If two or more faults occur while the EOUT timer is running, then the EOUT signals toggle only once after the EOUT timer reaches 
zero (idle). In other words, FCCU can pipeline only one fault.
Note that FCCU does not toggle the EOUT signals in CONFIG state. FCCU toggles the EOUT signals only when FCCU enters 
the FAULT state or when a fault occurs in the FAULT state.
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2149 / 5251


---
# 페이지 233

Example 1
NORMAL
FAULT
NORMAL
Tmin
Tmin
Faults recovered
A
B
FCCU state
Fault
EOUT0
Tmin
C
EOUT1
FAULT
Stage
Description
1
A fault source indicates fault A to FCCU.
2
FCCU enters the FAULT state.
3
FCCU toggles the EOUT signals in response to fault A, 
initializes the fault-output (EOUT) timer with the value of 
Tmin (see DELTA_T[DELTA_T]), and begins decrementing 
the timer.
4
A fault source indicates fault B to FCCU while FCCU is still in 
the FAULT state.
5
The EOUT timer has already reached 0 (idle), so FCCU toggles 
the EOUT signals in response to fault B, initializes the EOUT 
timer with the value of Tmin, and begins decrementing the timer.
6
The source (for hardware-recoverable faults) and software (for 
software-recoverable faults) recovers the faults.
7
FCCU enters the NORMAL state.
8
A fault source indicates fault C to FCCU.
9
The EOUT timer has not yet reached 0 (idle), so FCCU leaves 
the EOUT signals as they are.
10
When the EOUT timer reaches 0 (idle), FCCU toggles the 
EOUT signals in response to fault C, initializes the EOUT timer 
with the value of Tmin, and begins decrementing the timer.
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2150 / 5251


---
# 페이지 234

Example 2
NORMAL
FAULT
Tmin
Tmin
Faults recovered
A
B
C
D
No toggling for this fault
NORMAL
Tmin
FCCU state
Fault
EOUT0
EOUT1
Stage
Description
1
A fault source indicates fault A to FCCU.
2
FCCU enters the FAULT state.
3
FCCU toggles the EOUT signals in response to fault A, 
initializes the fault-output (EOUT) timer with the value of 
Tmin (see DELTA_T[DELTA_T]), and begins decrementing 
the timer.
4
A fault source indicates fault B to FCCU while FCCU is still in 
the FAULT state.
5
The EOUT timer has already reached 0 (idle), so FCCU toggles 
the EOUT signals in response to fault B, initializes the EOUT 
timer with the value of Tmin, and begins decrementing the timer.
6
A fault source indicates fault C to FCCU while FCCU is still in 
the FAULT state.
7
The EOUT timer has not yet reached 0 (idle), so FCCU leaves 
the EOUT signals as they are. Fault C is now pending.
8
A fault source indicates fault D to FCCU while FCCU is still in 
the FAULT state. (FCCU can pipeline only one fault, so FCCU 
ignores fault D.)
9
The EOUT timer has not yet reached 0 (idle), so FCCU leaves 
the EOUT signals as they are.
10
When the EOUT timer reaches 0 (idle), FCCU toggles the 
EOUT signals in response to fault C, initializes the EOUT 
timer with the value of Tmin, and begins decrementing the 
timer. FCCU never toggles the EOUT signals in response to 
fault D because FCCU can pipeline only one fault.
52.3.6 Modes of operation
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2151 / 5251


---
# 페이지 235

52.3.6.1
Put FCCU in the NORMAL state
52.3.6.1.1
Introduction
You put FCCU in the NORMAL state to save changes to the configuration, and to allow FCCU to enter the ALARM or FAULT state 
when a fault occurs on an enabled fault channel.
52.3.6.1.2
About putting FCCU in NORMAL state
When putting FCCU in the NORMAL state:
• If you attempt to lock the configuration while FCCU is in CONFIG state, FCCU does not actually lock the configuration until 
FCCU leaves CONFIG state—that is, either you put FCCU in the NORMAL state, or FCCU puts itself in the NORMAL state 
because the Configuration-state timeout interval (CFG_TO[TO]) expires.
• After you permanently lock the configuration, you must reset FCCU before you can put FCCU in the CONFIG state.
52.3.6.1.3
Put FCCU in the NORMAL state
1. Check the FCCU status (STAT[STATUS]).
• If the FCCU status is NORMAL, go to step 6.
• If the FCCU status is CONFIG, go to step 2.
• If the FCCU status is ALARM or FAULT, go to step 4.
2. Run the OP2 operation (see Run an operation).
3. Check the operation status (CTRL[OPS]).
• If the operation status is Successful, FCCU is in the NORMAL state. Go to step 6.
• If the operation status is Aborted, go to step 2.
4. Recover all faults (see Fault recovery).
5. Go to step 1.
6. Lock the configuration if you want to prevent any changes to it:
• To require a key to unlock the configuration, from Supervisor mode, temporarily lock the 
configuration (TRANS_LOCK[TRANSKEY]).
• To require a reset of FCCU to unlock the configuration, from Supervisor mode, permanently lock the 
configuration (PERMNT_LOCK[PERMNTKEY]).
The configuration is permanently locked until FCCU is reset.
52.3.6.2
Manage faults
52.3.6.2.1
Introduction
After saving changes to the configuration, you are ready to use FCCU to manage faults.
52.3.6.2.2
Determine if there are any unrecovered non-critical faults
Check the unrecovered-fault indicators for the non-critical faults (NCF_Sa[NCFSn]).
52.3.6.2.3
Recover a software-recoverable non-critical fault
1. Resolve the source of the software-recoverable non-critical fault.
2. Unlock the NCF_Sa registers (NCFK[NCFK]) using a 32-bit write.
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2152 / 5251


---
# 페이지 236

3. Initiate clearing of the unrecovered-fault indicator for the software-recoverable non-critical fault (NCF_Sa[NCFSn]) using 
a 32-bit write.
FCCU initiates the OP12 operation.
 
If you want to clear multiple unrecovered-fault indicators and those indicators reside in different NCF_Sa registers, 
you must perform steps 2 and 3 for each individual register.
  NOTE  
4. Check the operation status (CTRL[OPS]).
• If the operation status is In Progress, go to step 4.
• If the operation status is Successful, go to step 5.
• If the operation status is Aborted, go to step 2.
5. Check the unrecovered-fault indicator for the software-recoverable non-critical fault (NCF_Sa[NCFSn]).
• If the indicator indicates no unrecovered fault, the fault has been recovered. Stop.
• If the indicator still indicates an unrecovered fault, go to step 2.
52.3.6.2.4
Clear the freeze-status indicators
1. Run the OP13 operation (see Run an operation).
2. Check the operation status (CTRL[OPS]).
• If the operation status is Successful, stop .
• If the operation status is Aborted, go to step 1.
52.3.6.3
Run operations
52.3.6.3.1
Introduction
You run operations to perform actions such as putting FCCU in the CONFIG state or setting the operation status to Idle. For a 
complete list of operations you can run, see CTRL[OPR].
52.3.6.3.2
About running operations
When running operations:
• FCCU ignores any operations initiated while the operation status is In Progress.
• Certain operations must be unlocked before you can initiate them. After you initiate them, they are locked again.
52.3.6.3.3
Run an operation
1. Check the operation status (CTRL[OPS]).
2. Go to step 1 if the operation status is In Progress.
3. Unlock the operation (CTRLK[CTRLK]) using a 32-bit write, if the operation must be unlocked before you can initiate it.
 
The Control Key (CTRLK) register used in this step and the Control (CTRL) register used in the next step must 
be written with consecutive instructions. Do not use read-modify-write instructions, such as bit-field instructions, to 
modify these registers.
  NOTE  
4. Initiate the operation (CTRL[OPR]) using a 32-bit write.
5. Check the operation status (CTRL[OPS]).
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2153 / 5251


---
# 페이지 237

6. Go to step 5 if the operation status is In Progress.
The operation status is now Idle (OP15 only), Aborted, or Successful.
52.3.7 FOSU
The FOSU provides a supervision of the primary fault notification path by analyzing FCCU's behavior for correctness. It waits for 
any reaction of the FCCU in a fixed time window after a fault is signaled.
The intention of the FOSU is to provide a secondary fault reaction path in most cases when the FCCU fails but not to needlessly 
propagate a fault which is already handled by the FCCU in a full chip reset. Only a failed primary fault reaction (that is, FCCU's 
failure) is a reason for the secondary reaction to take over (and generate a destructive reset request).
There is a 'do nothing' input coming from FCCU which indicates that the FCCU is programmed for no reaction for ALL FAULTS. It 
is a "static" input in the sense that it does not change after FCCU configuration. The FOSU masks the incoming faults with the 'do 
nothing' control from the FCCU, meaning that a fault is not captured by the FOSU if the 'do nothing' signal is asserted (that is, a 
disabled fault). There is no minimum pulse width requirement on the fault indication other than what is required by the technology, 
which is the same as that of the FCCU. FOSU does not monitor FCCU for the case of faults occurring during the CONFIG state.
The FOSU contains a timer with a duration of FOSU_COUNT, driven by CLKSAFE. The timer is initialized and started on any 
captured, enabled fault. While the timer is running, any subsequent captured fault will neither restart nor reinitialize the timer. 
The timer is stopped when the FCCU shows any of the following reactions (the FOSU does not check whether the reaction is the 
configured one for the faults which occurred):
• Reset: short functional reset
• IRQ (triggered by ALARM state)
• NMI 
• Error out triggered (by FCCU or by SW)
When the timer is stopped, the fault capture logic is cleared to ensure that the timer is not restarted because of faults still 'stuck' in 
the capture logic. The timer is then restarted by the next new failure indication. When the timer expires, the FOSU's failure indicator 
output is asserted after it ensures that the fault is enabled and the static "fccu program to do nothing" signal is deasserted. This 
is because FCCU uses settings after it exits CONFIG state, even if fault captured before the exit.
The FOSU's failure indicator output is connected to one of the MC_RGM's 'destructive' reset inputs, so its assertion will cause a 
reset sequence to be initiated starting at DEST0. The FOSU module is reset with the same reset as is used by the FCCU. When 
this reset is asserted, the FOSU's capture logic is cleared, its timer is kept stopped and in a non-expired state, and its failure 
indicator output is deasserted.
 
FOSU is triggered on assertion of enabled fault. In case the triggering fault is disabled, FOSU times out 
without reaction.
  NOTE  
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2154 / 5251


---
# 페이지 238

CPU 0
Out of
Time
Out of
Time
CPU 1
FCCU
FOSU
External
Device
EOUT[0]
EOUT[1]
Reset
MC_RGM
IRQ
Note: The fault sources shown are examples only.
FIF
SW
Watchdog
SW
Watchdog
Figure 216. FOSU connections to the FCCU and MC_RGM
52.3.8 Clocking
This module has no clocking considerations.
52.3.9 Interrupts
This module has no interrupts.
52.4 External signals
FCCU interfaces with the EOUT pin. Signaling on the EOUT pin depends on whether the module is processing an error or is idle.
52.5 Initialization
52.5.1 Prepare FCCU for configuration
52.5.1.1
Introduction
You prepare FCCU for configuration by first configuring the CONFIG state and then putting FCCU in that state.
52.5.1.2
About preparing FCCU for configuration
When preparing FCCU for configuration, keep the following in mind:
• To put FCCU in CONFIG state, FCCU must be in NORMAL state.
• After FCCU is reset, the configuration is temporarily locked. You must temporarily unlock the configuration before you can put 
FCCU in the CONFIG state.
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2155 / 5251


---
# 페이지 239

• When FCCU is in the CONFIG state, FCCU does not actually save the changes you make to the configuration. To save 
changes to the configuration, you must manually put FCCU in the NORMAL state. If FCCU automatically leaves the CONFIG 
state and enters the NORMAL state because the Configuration-state timeout interval (CFG_TO[TO]) expires (called a 
Configuration-state timeout), FCCU changes the value of the Configuration (CFG) register to its Configuration-state-timeout 
value and the value of each of the other configuration registers to its reset value. FCCU also changes the value of the 
Configuration-State Timeout Interval (CFG_TO) register to its reset value. For information on the Configuration-state timeout 
value, see CFG register bit value at different events. For a list of configuration registers, see Configuration registers.
52.5.1.3
Configure the CONFIG state
1. Set the Configuration-state timeout interval (CFG_TO[TO]).
2. Enable the Configuration-state-timeout interrupt signal (IRQ_EN[CFG_TO_IEN]), if you want FCCU to request an 
interrupt when a Configuration-state timeout occurs.
52.5.1.4
Put FCCU in the CONFIG state
1. Unlock the configuration temporarily (TRANS_LOCK[TRANSKEY]) in Supervisor mode.
2. Check the FCCU status (STAT[STATUS]).
• If the FCCU status is CONFIG, FCCU is in the CONFIG state. Stop.
• If the FCCU status is NORMAL, go to step 3.
• If the FCCU status is ALARM or FAULT, go to step 5.
3. Run the OP1 operation (see Run an operation).
4. Check the operation status (CTRL[OPS]).
• If the operation status is Successful, FCCU is in the CONFIG state. Stop.
• If the operation status is Aborted, the configuration is probably permanently locked. Go to step 7.
5. Recover all faults (see Fault recovery).
6. Go to step 2.
7. Reset FCCU.
52.5.2 Configure FCCU
52.5.2.1
Introduction
You configure FCCU so it functions according to the needs of your particular application.
52.5.2.2
About configuring FCCU
When configuring FCCU:
• If you enable a non-critical fault channel but disable all reactions for that channel, FCCU changes state when necessary but 
does not perform any reaction because reactions are disabled. If you enable reactions for a non-critical fault channel but 
disable that channel, and FCCU is in the NORMAL state when a fault occurs on the channel, FCCU does not enter the ALARM 
or FAULT state and therefore does not perform any reaction.
52.5.2.3
Configure the non-critical fault channels
For each non-critical fault channel that you want FCCU to monitor:
1. Set the recovery type (NCF_CFGa[NCFCn]).
2. Enable at least one type of Fault-state reaction:
• Chip functional reset (NCFS_CFGa[NCFSCn])
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2156 / 5251


---
# 페이지 240

• Non-maskable interrupt (NMI_ENa[NMIENn])
• EOUT signaling (EOUT_SIG_ENa[EOUTENn])
 
If you enable the chip functional reset as the type of Fault-state reaction for a channel, enable at least one other 
type of Fault-state reaction for the channel or enable the ALARM state (step 4) for the channel.
  NOTE  
3. Set the Alarm-state timeout interval (NCF_TO[TO]), if you plan to enable the ALARM state for any non-critical fault channel.
 
Ensure that the Alarm-state timeout interval is less than the FOSU module's timeout interval; otherwise, FOSU 
generates a chip reset every time a fault occurs on the channel. The FOSU timeout interval (FOSU_COUNT) is a 
chip-specific value. See the chip-specific FCCU information.
  NOTE  
4. Enable the ALARM state (NCF_TOEa[NCFTOEn]) for any non-critical fault channel for which you want FCCU to enter the 
ALARM state before entering the FAULT state.
5. Enable the Alarm-state reaction (IRQ_ALARM_ENa[IRQENn]) for each non-critical fault channel for which you enabled the 
ALARM state.
6. Enable the corresponding NCF_Ea[NCFEn] field for each non-critical fault channel that you want FCCU to monitor.
52.6 Application information
52.6.1 Use cases and limitations
Configuration guidelines
Follow these guidelines to configure FCCU:
• If you want FCCU to react to a fault on a non-critical fault channel:
— Enable the channel (Non-critical Fault Enable (NCF_E0)).
— Enable at least one type of Fault-state reaction for the channel: chip reset (Non-critical Fault-State Configuration 
(NCFS_CFG0)), fault-output (EOUT) signaling (Non-critical Fault-State EOUT Signaling Enable (EOUT_SIG_EN0)), 
or non-maskable interrupt (Non-critical Fault-State Non-maskable-Interrupt-Request Enable (NMI_EN0)).
— If you enable chip reset as the type of Fault-state reaction for the channel (Non-critical Fault-State Configuration 
(NCFS_CFG0)), enable either ALARM state (Non-critical-Fault Alarm-State Timeout Enable (NCF_TOE0)) or at least 
one other type of Fault-state reaction for the channel: fault-output (EOUT) signaling (Non-critical Fault-State EOUT 
Signaling Enable (EOUT_SIG_EN0)) or non-maskable interrupt (Non-critical Fault-State Non-maskable-Interrupt-
Request Enable (NMI_EN0)).
— If you enable ALARM state for the channel (Non-critical-Fault Alarm-State Timeout Enable (NCF_TOE0)), enable the 
Alarm-state reaction (Non-critical Alarm-State Interrupt-Request Enable (IRQ_ALARM_EN0)).
— If you enable ALARM state for the channel (Non-critical-Fault Alarm-State Timeout Enable (NCF_TOE0)), make 
sure the Alarm-state timer interval (Non-critical-Fault Alarm-State Timeout Interval (NCF_TO)) is less than the FOSU 
module's timer interval; otherwise, FOSU generates a chip reset every time a fault occurs on the channel. The FOSU 
timer interval (FOSU_COUNT) is chip-specific. See the chip-specific FCCU information.
Recommendations to configure FCCU
1. After a power on, or 'destructive' reset (when initiated by the assertion of the chip reset pin, RESET_B), where both 
system and FCCU are reset, the following steps could be followed to configure FCCU:
a. Check and clear any pending fault status
b. Verify FCCU is in NORMAL state, else repeat step(a) above
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2157 / 5251


---
# 페이지 241

c. Configure FCCU
2. After any 'functional' reset of the system, arising out of a reset request from FCCU or other sources, the following steps 
could be followed to reconfigure FCCU:
a. If active, wait for the Error out Tmin to expire
b. Check and clear fault status
c. Error pin moves to "non faulty" state, once fault status is cleared and Tmin expires
d. Verify FCCU is in NORMAL state, else repeat step(a) above
e. Read and verify value in NCF_En
f.
Reconfigure FCCU, if necessary
52.7 Register descriptions
52.7.1 FCCU register descriptions
The FCCU registers are listed in the table below. Any address offset not explicitly mentioned in this table is reserved.
The FCCU supports word (32-bit), half-word (16-bit), and byte (8-bit) read and write accesses.
Follow these register-access guidelines:
• Do not read from or write to any addresses that are not shown in the following table. Doing so may or may not result in a 
transfer error.
• Do not write to any of the configuration registers unless FCCU is in the CONFIG state. Doing so results in a transfer error.
• Do not write to the Transient Configuration Lock (TRANS_LOCK) or Permanent Configuration Lock (PERMNT_LOCK) 
registers unless your code runs in the Supervisor mode. Doing so results in a transfer error.
For each possible NCF failure source, a different reaction—including no reaction—is configurable through the use of NMI, IRQ, 
and short reset selection registers. It is not possible for a single event upset to switch off all reactions on failures as implementation 
is per fault source (but it will be possible to switch them all off by SW if intended). Failures themselves are not able to disable all 
reactions and indications. 
52.7.1.1
FCCU memory map
FCCU base address: 4038_4000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Control (CTRL)
32
RW
0000_00C0h
4h
Control Key (CTRLK)
32
W
0000_0000h
8h
Configuration (CFG)
32
RW
0000_0000h
1Ch
Non-critical Fault Configuration (NCF_CFG0)
32
RW
0000_00FFh
4Ch
Non-critical Fault-State Configuration (NCFS_CFG0)
32
RW
0000_0000h
80h
Non-critical Fault Status (NCF_S0)
32
RW
0000_0000h
90h
Non-critical Fault Key (NCFK)
32
W
0000_0000h
94h
Non-critical Fault Enable (NCF_E0)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2158 / 5251


---
# 페이지 242

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
A4h
Non-critical-Fault Alarm-State Timeout Enable (NCF_TOE0)
32
RW
0000_00FFh
B4h
Non-critical-Fault Alarm-State Timeout Interval (NCF_TO)
32
RW
0003_A980h
B8h
Configuration-State Timeout Interval (CFG_TO)
32
RW
0000_0005h
BCh
IO Control (EINOUT)
32
RW
See section
C0h
Status (STAT)
32
R
0000_0010h
C4h
Normal-to-Alarm Freeze Status (N2AF_STATUS)
32
R
0000_0000h
C8h
Alarm-to-Fault Freeze Status (A2FF_STATUS)
32
R
0000_0000h
CCh
Normal-to-Fault Freeze Status (N2FF_STATUS)
32
R
0000_0000h
D0h
Fault-to-Alarm Freeze Status (F2AF_STATUS)
32
R
0000_0000h
DCh
Non-critical Fault Fake (NCFF)
32
RW
0000_0000h
E0h
IRQ Status (IRQ_STAT)
32
RW
0000_0000h
E4h
IRQ Enable (IRQ_EN)
32
RW
0000_0000h
F0h
Transient Configuration Lock (TRANS_LOCK)
32
RW
0000_0000h
F4h
Permanent Configuration Lock (PERMNT_LOCK)
32
RW
0000_0000h
F8h
Delta T (DELTA_T)
32
RW
0000_0000h
FCh
Non-critical Alarm-State Interrupt-Request Enable 
(IRQ_ALARM_EN0)
32
RW
0000_0000h
10Ch
Non-critical Fault-State Non-maskable-Interrupt-Request Enable 
(NMI_EN0)
32
RW
0000_0000h
11Ch
Non-critical Fault-State EOUT Signaling Enable (EOUT_SIG_EN0)
32
RW
0000_0000h
12Ch
Alarm-State Timer (TMR_ALARM)
32
R
0003_A980h
134h
Configuration-State Timer (TMR_CFG)
32
R
000F_FFFFh
138h
Fault-Output Timer (TMR_ETMR)
32
R
0000_0000h
52.7.1.2
Control (CTRL)
Offset
Register
Offset
CTRL
0h
Function
Initiates and indicates the status of operations—and enables the Debug mode.
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2159 / 5251


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
0
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
DEBU
G 
0
OPS 
0
OPR 
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
1
1
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
28-10
—
Reserved
9
DEBUG
Debug Mode Enable
Specifies whether the Debug mode is enabled. If so, FCCU enters the Debug mode when the Debug signal 
is asserted. When FCCU enters the Debug mode, it halts operation and remains in the state it was in before 
it entered this mode.
 
FOSU does not halt when FCCU enters the Debug mode. Therefore, FOSU can still cause 
a reset if a fault occurs while FCCU is in the Debug mode.
  NOTE  
0b - Disabled
1b - Enabled
8
—
Reserved
7-6
OPS
Operation Status
This field can be read and cleared (via OP15 operation) by the software.
00b - Idle
01b - In progress
10b - Aborted
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2160 / 5251


---
# 페이지 244

Table continued from the previous page...
Field
Function
11b - Successful
5
—
Reserved
4-0
OPR
Operation Run
Initiates operations that perform actions such as putting FCCU in the CONFIG state or setting the operation 
status to Idle. For information on how to run operations, see Run operations.
FCCU ignores any write to this field while the operation status (CTRL[OPS]) is "In progress". After 
completion of an operation, FCCU sets this field to OP0.
The following events result in an operation status (CTRL[OPS]) of "Aborted":
• Writing to a NCF_Sa register (which automatically initiates the OP12 operation) without first 
successfully unlocking the register (NCFK[NCFK])
• Initiating an OP1 operation when FCCU is not in the NORMAL state or the configuration is locked
• Initiating an OP1, or OP2, operation without first unlocking the operation (CTRLK[CTRLK])
00000 OP0—No operation
00001 OP1—Applies only when the configuration is unlocked, when FCCU is in the NORMAL state, and 
immediately after you unlock the operation (CTRLK[CTRLK]). Put FCCU in the CONFIG state.
00010 OP2—Applies only immediately after you unlock the operation (CTRLK[CTRLK]). Put FCCU in the 
NORMAL state.
00011 Reserved
00100 Reserved
00101 Reserved
00110 Reserved
00111 Reserved
01000 Reserved
01001 Reserved
01010 Reserved
01011 Reserved
01100 OP12—Do not initiate this operation; it is automatically initiated by the FCCU. A NCF_Sa register 
status clear operation is in progress.
01101 OP13—Clear the freeze status registers.
01110 OP14—Do not initiate this operation; it is automatically initiated by the FCCU. A Configuration-state 
timeout is in progress. For more information, see Configuration registers.
01111 OP15—Set the operation status (CTRL[OPS]) to Idle.
10000 Reserved
10001 Reserved
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2161 / 5251


---
# 페이지 245

Table continued from the previous page...
Field
Function
10010 Reserved
10011 Reserved
10100 Reserved
10101—11110 Forbidden. Writing any of these values returns an operation status (CTRL[OPS]) of 
"Aborted" with no side effect.
11111 Reserved
52.7.1.3
Control Key (CTRLK)
Offset
Register
Offset
CTRLK
4h
Function
See CTRLK[CTRLK].
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
W
CTRLK 
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
W
CTRLK 
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
CTRLK
Locked-Operation Control Key
Writable only with a 32‑bit write. Unlocks locked operations (CTRL[OPR]) so you can initiate them. For 
information on how to unlock locked operations before you initiate them, see Run an operation.
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2162 / 5251


---
# 페이지 246

Field
Function
 
• You must initiate an operation in the FCCU register access that immediately follows the 
one that unlocks it; otherwise, the operation is again locked.
• Reading from this register always returns the value 0000_0000h.
  NOTE  
Operations not listed here are not locked and do not need to be unlocked.
9137_56AFh: Unlock OP1.
825A_132Bh: Unlock OP2.
Any other value: Do nothing.
52.7.1.4
Configuration (CFG)
Offset
Register
Offset
CFG
8h
Function
Writable only when FCCU is in the CONFIG state. Changed by FCCU to another value when the chip resets FCCU, a 
Configuration-state timeout occurs, or you run an OP31 operation. See CFG register bit value at different events for more 
information. Specifies the global configuration for FCCU.
 
If you specify a new value for any of the fields in this register that affect the EOUT signals while the fault-output 
(EOUT) timer is running (FCCU is indicating a fault on the EOUT signals), FCCU does not use the new settings you 
specified until after the fault-output (EOUT) timer expires (FCCU stops indicating a fault on the EOUT signals).
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
FCCU_
SE...
FCCU_SET_CL
EAR 
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
Reserved 
Reserv
ed 
CM 
Reserv
ed 
PS 
FOM 
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
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2163 / 5251


---
# 페이지 247

Fields
Field
Function
31-25
—
Reserved
24
FCCU_SET_AF
TER_RESET
Fault-Output (EOUT) Activate
For fault-output (EOUT) signaling, controls whether the EOUT signals are active. 
0b - Inactive (the EOUT signals are in a high-impedance state)
1b - Active (the EOUT signals indicate FCCU's condition)
23-22
FCCU_SET_CL
EAR
Fault-Output (EOUT) Control
Applies only to Bi-Stable and Fault-Toggle fault-output modes (CFG[FOM]) and when the EOUT signals 
are active (CFG[FCCU_SET_AFTER_RESET]). Controls whether the fault-output (EOUT) signals are 
managed by FCCU's FSM.
 
When the EOUT signals are in the Fault-Toggle fault-output mode, if you change 
the value of this field, you must also deactivate and then reactivate the EOUT 
signals (CFG[FCCU_SET_AFTER_RESET]) to correctly initialize them so they have 
opposite states.
  NOTE  
00b - Controlled by the FSM
01b - Always low
10b - Controlled by the FSM
11b - High until a fault occurs on a channel, regardless of whether that fault is disabled; 
thereafter, controlled by the FSM. Note: FCCU ignores an attempt to write this value if the 
fault-output (EOUT) timer is already running.
21-20
—
Reserved
19-16
—
Reserved
15
—
Reserved
14-13
—
Reserved
12
—
Reserved
Always write the reset value to this field.
11
CM
Fault-Output (EOUT) Configuration-Indication Mode
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2164 / 5251


---
# 페이지 248

Table continued from the previous page...
Field
Function
For fault-output (EOUT) signaling, this field controls whether the configuration indication is the same as the 
non-faulty indication.
0b - Different
1b - Same
10
—
Reserved
9
PS
Fault-Output (EOUT) Polarity Selection
Applies to fault-output (EOUT) signaling and controls the polarity of the signals for fault-output mode 
indications that hold the signals low or high (versus toggling them or placing them in a high-impedance 
state). Applies only to Bi-Stable fault-output mode (for all indications).
0b - For the faulty indication, EOUT1 is high, and EOUT0 is low.
1b - For the faulty indication, EOUT1 is low, and EOUT0 is high.
8-6
FOM
Fault-Output (EOUT) Mode
For fault-output (EOUT) signaling, controls the protocol of the signaling.
 
See the chip-specific FCCU information for the fault-output modes supported by this chip.
  NOTE  
000b - Reserved
001b - Reserved
010b - Bi-Stable
011b - Fault-Toggle
100b - Reserved
101b - Test 0 (controlled by the EINOUT register; EOUT1 is an output; EOUT0 is an input)
110b - Test 1 (controlled by the EINOUT register; EOUT1 and EOUT0 are both outputs)
111b - Test 2 (controlled by the EINOUT register; EOUT1 is an input; EOUT0 is an output)
5-0
—
Reserved
52.7.1.5
Non-critical Fault Configuration (NCF_CFG0)
Offset
Register
Offset
NCF_CFG0
1Ch
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2165 / 5251


---
# 페이지 249

Function
See NCF_CFGa[NCFCn].
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
NCFC
7 
NCFC
6 
NCFC
5 
NCFC
4 
NCFC
3 
NCFC
2 
NCFC
1 
NCFC
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
31-8
—
Reserved
7-0
NCFCn
Non-critical Fault Configuration n
Writable only when FCCU is in the CONFIG state. Changed by FCCU to its reset value when a 
Configuration-state timeout occurs. Controls the recovery type (HW or SW) of the associated non-critical 
fault channel (n). For information on how to configure the non-critical fault channels, see Configure the 
non-critical fault channels.
 
Configure a non-critical fault channel as hardware-recoverable only if the source continues 
to indicate a fault on the fault channel's input (NCFn) until the condition that caused 
the fault is no longer true; otherwise, configure the non-critical fault channel as software-
recoverable.
  NOTE  
0b - Hardware-recoverable
1b - Software-recoverable
52.7.1.6
Non-critical Fault-State Configuration (NCFS_CFG0)
Offset
Register
Offset
NCFS_CFG0
4Ch
Function
See NCFS_CFGa[NCFSCn].
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2166 / 5251


---
# 페이지 250

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
NCFSC7 
NCFSC6 
NCFSC5 
NCFSC4 
NCFSC3 
NCFSC2 
NCFSC1 
NCFSC0 
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
15-14: NCFSC7
13-12: NCFSC6
11-10: NCFSC5
9-8: NCFSC4
7-6: NCFSC3
5-4: NCFSC2
3-2: NCFSC1
1-0: NCFSC0
Non-critical Fault-State Configuration n
Writable only when FCCU is in the CONFIG state. Changed by FCCU to its reset value when a 
Configuration-state timeout occurs. Controls whether the chip functional reset is enabled as a Fault-state 
reaction for the associated non-critical fault channel (n). When the chip functional reset is enabled for an 
enabled non-critical fault channel, a fault on that channel causes FCCU to assert the rst_sfunc_b signal 
when FCCU enters the FAULT state. For information on how to configure the non-critical fault channels, see 
Configure the non-critical fault channels.
00b - Disabled
01b - Enabled (rst_sfunc_b) (short)
10b - Reserved
11b - Disabled
52.7.1.7
Non-critical Fault Status (NCF_S0)
Offset
Register
Offset
NCF_S0
80h
Function
See NCF_Sa[NCFSn].
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2167 / 5251


---
# 페이지 251

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
NCFS
7 
NCFS
6 
NCFS
5 
NCFS
4 
NCFS
3 
NCFS
2 
NCFS
1 
NCFS
0 
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
0
0
0
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
NCFSn
Non-critical Fault Status n
Indicates whether there is an unrecovered fault on the associated non-critical fault channel (n).
 
To recover a software-recoverable non-critical fault, which includes clearing its 
unrecovered-fault indicator, see Recover a software-recoverable non-critical fault. FCCU 
clears the unrecovered-fault indicator for a hardware-recoverable non-critical fault 
automatically when the source no longer indicates a fault on the fault channel's input 
signal; if you attempt to clear the unrecovered-fault indicator for a hardware-recoverable 
non-critical fault, FCCU does not clear the indicator and does not indicate an error.
  NOTE  
0b - No unrecovered fault
1b - Unrecovered fault
52.7.1.8
Non-critical Fault Key (NCFK)
Offset
Register
Offset
NCFK
90h
Function
See NCFK[NCFK].
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2168 / 5251


---
# 페이지 252

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
NCFK 
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
NCFK 
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
NCFK
Non-critical Fault Key
Writable only with a 32‑bit write. Unlocks the NCF_Sa registers so you can write to them while recovering 
a software-recoverable non-critical fault. For information on how to unlock the NCF_Sa registers before 
writing to them, see Recover a software-recoverable non-critical fault.
 
• You must write to one of the NCF_Sa registers immediately after unlocking it (that 
is, in the FCCU register access that immediately follows the one that unlocks them); 
otherwise the registers are again locked. If you want to write to multiple NCF_Sa 
registers, you must unlock each register immediately before you write to it.
• Reading from this register always returns the value 0000_0000h.
  NOTE  
AB34_98FEh: Unlock.
Any other value: Do nothing.
52.7.1.9
Non-critical Fault Enable (NCF_E0)
Offset
Register
Offset
NCF_E0
94h
Function
See NCF_Ea[NCFEn].
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2169 / 5251


---
# 페이지 253

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
NCFE
7 
NCFE
6 
NCFE
5 
NCFE
4 
NCFE
3 
NCFE
2 
NCFE
1 
NCFE
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
31-8
—
Reserved
7-0
NCFEn
Non-critical Fault Enable n
Writable only when FCCU is in the CONFIG state. Changed by FCCU to its reset value when a 
Configuration-state timeout occurs. Controls whether the associated non-critical fault channel (n) is 
enabled. When a non-critical fault channel is enabled, a fault on that channel causes FCCU to leave the 
NORMAL state and enter the FAULT state (or ALARM state if enabled for the channel). For information on 
how to configure the non-critical fault channels, see Configure the non-critical fault channels.
0b - Disabled
1b - Enabled
52.7.1.10
Non-critical-Fault Alarm-State Timeout Enable (NCF_TOE0)
Offset
Register
Offset
NCF_TOE0
A4h
Function
See NCF_TOEa[NCFTOEn].
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2170 / 5251


---
# 페이지 254

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
NCFT
OE7 
NCFT
OE6 
NCFT
OE5 
NCFT
OE4 
NCFT
OE3 
NCFT
OE2 
NCFT
OE1 
NCFT
OE0 
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
31-8
—
Reserved
7-0
NCFTOEn
Non-critical-Fault Alarm-State Timeout Enable n
Writable only when FCCU is in the CONFIG state. Changed by FCCU to its reset value when a 
Configuration-state timeout occurs. Controls whether the ALARM state is enabled for the associated 
non-critical fault channel (n). When the ALARM state is enabled for an enabled non-critical fault channel, 
a fault on that channel causes FCCU to leave the NORMAL state and enter the ALARM state instead 
of FAULT state. If the fault is not recovered within the Alarm-state timeout interval, then FCCU leaves 
the ALARM state and enters the FAULT state. For information on how to configure the non-critical fault 
channels, see Configure the non-critical fault channels.
0b - Disabled
1b - Enabled
52.7.1.11
Non-critical-Fault Alarm-State Timeout Interval (NCF_TO)
Offset
Register
Offset
NCF_TO
B4h
Function
See NCF_TO[TO]
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2171 / 5251


---
# 페이지 255

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
TO 
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
TO 
W
Reset
1
0
1
0
1
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
Fields
Field
Function
31-0
TO
Non-critical-Fault Alarm-State Timeout Interval
Writable only when FCCU is in the CONFIG state. Changed by FCCU to its reset value when a 
Configuration-state timeout occurs. Controls the maximum amount of time that FCCU can be in the 
ALARM state (TMax Alarm) according to this equation:
TMax Alarm = TO × TCLKSAFE
where TCLKSAFE is the safe-clock period.
If FCCU enters the ALARM state (because a fault occurs on an enabled non-critical fault channel for which 
the ALARM state is enabled) and this timeout interval expires (called an Alarm-state timeout), then FCCU 
leaves the ALARM state and enters the FAULT state.
 
Make sure the Alarm-state timeout interval is less than the FOSU module's timeout interval; 
otherwise, a fault that occurs while FCCU is in the ALARM state can cause FOSU to 
generate a chip reset. The FOSU timeout interval (FOSU_COUNT) is chip-specific. See the 
chip-specific FCCU information.
  NOTE  
52.7.1.12
Configuration-State Timeout Interval (CFG_TO)
Offset
Register
Offset
CFG_TO
B8h
Function
See CFG_TO[TO]
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2172 / 5251


---
# 페이지 256

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
TO 
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
1
0
1
Fields
Field
Function
31-3
—
Reserved
2-0
TO
Configuration-State Timeout Interval
Writable only when FCCU is in the NORMAL, ALARM, or FAULT state (not in the CONFIG state). 
Changed by FCCU to its reset value when a Configuration-state timeout occurs. Not accessible while a 
Configuration-state timeout (OP14 operation) is in progress. Controls the maximum amount of time that 
FCCU can be in the CONFIG state (TMax configuration) according to this equation:
TMax configuration = TCLKSAFE × 2(TO + 13)
where TCLKSAFE is the safe-clock period.
If you put FCCU in the CONFIG state and this timeout interval expires (called a Configuration-state timeout), 
then FCCU:
• Automatically leaves the CONFIG state and enters the NORMAL state
• Changes the value of the Configuration (CFG) register to its Configuration-state-timeout value and the 
value of each of the other configuration registers to its reset value. For information on the Configuration 
(CFG) register's Configuration-state-timeout value, see CFG register bit value at different events. For 
a list of configuration registers, see Configuration registers.
52.7.1.13
IO Control (EINOUT)
Offset
Register
Offset
EINOUT
BCh
Function
The EINOUT register allows the following operations typically in the NORMAL state:
• To control the EOUT[1] output level when the FCCU is configured in "Test1" or "Test0" fault output mode (CFG[FOM])
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2173 / 5251


---
# 페이지 257

• To control the EOUT[0] output level when the FCCU is configured in "Test1" or "Test2" fault output mode (CFG[FOM])
• to observe the state of signals at EIN[1:0] pins
The following table shows Bi-Stable encoding.
Table 301. Bi-Stable encoding
Mode = CFG[FOM]
EOUT[0]
EOUT[1]
Test1
output
output
Test2
output
input
Test0
input
output
 
Because of the resynchronization stage of the EOUT interface, there is a latency of a few CLKSAFE cycles 
following a write/read operation of the EINOUT register.
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
EIN1 
EIN0 
0
EOUT
1 
EOUT
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
u1
u
0
0
0
0
1. Reset value varies as per the corresponding EIN signal.
Fields
Field
Function
31-6
—
Reserved
5
EIN1
Error Input 1
Indicates the state of the EIN1 signal.
 
When IP’s SET_AFTER_RESET bit is 0, then corresponding pad is in High-Z state, in this 
case values sampled on EIN1 will depend on board/pad pull up/down values.
  NOTE  
0b - Low
1b - High
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2174 / 5251


---
# 페이지 258

Table continued from the previous page...
Field
Function
4
EIN0
Error Input 0
Indicates the state of the EIN0 signal.
 
When IP’s SET_AFTER_RESET bit is 0, then corresponding pad is in High-Z state, in this 
case values sampled on EIN0 will depend on board/pad pull up/down values.
  NOTE  
0b - Low
1b - High
3-2
—
Reserved
1
EOUT1
EOUT1
Error out 1 (significant only if the CFG.FOM = Test1 or Test0 => EOUT[1] configured in output mode). 
The EOUT1 set/clear the respective EOUT[1] output signal if CFG.FOM = 110 or 101, otherwise it is a 
"don't-care" value.
 
When the configuration watchdog timer expires, FCCU changes the value of this field to its 
reset value.
  NOTE  
0b - force EOUT[1] = 0
1b - force EOUT[1] = 1
0
EOUT0
EOUT0
Error out 0 (significant only if the CFG.FOM = Test1 or Test2 => EOUT[0] configured in output mode). The 
EOUT0 set/clear the respective EOUT[0] output signal if CFG.FOM = 110 or 111, otherwise it is a "don't 
care" value.
 
When the configuration watchdog timer expires, FCCU changes the value of this field to its 
reset value.
  NOTE  
0b - force EOUT[0] = 0
1b - force EOUT[0] = 1
52.7.1.14
Status (STAT)
Offset
Register
Offset
STAT
C0h
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2175 / 5251


---
# 페이지 259

Function
This register indicates the following:
• States that FCCU is driving on the EOUT signals
• Whether FCCU is in a faulty condition
• Current state of FCCU
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
PhysicErrorPin 
ESTAT 
STATUS 
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
1
0
0
0
0
Fields
Field
Function
31-6
—
Reserved
5-4
PhysicErrorPin
EOUT Signal States
Applies only when the EOUT signals are active (CFG[FCCU_SET_AFTER_RESET]). Indicates the states 
that FCCU is driving on the EOUT signals. 
00b - EOUT1 is low; EOUT0 is low.
01b - EOUT1 is low; EOUT0 is high.
10b - EOUT1 is high; EOUT0 is low.
11b - EOUT1 is high; EOUT0 is high.
3
ESTAT
FCCU Faulty Condition
Indicates whether FCCU is in faulty condition (as indicated by the EOUT signals). For more information, see 
The FCCU conditions. 
0b - Not in faulty condition (in non-faulty or configuration condition)
1b - In faulty condition
2-0
STATUS
FCCU State
Indicates the current state of FCCU
000b - NORMAL
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2176 / 5251


---
# 페이지 260

Table continued from the previous page...
Field
Function
001b - CONFIG
010b - ALARM
011b - FAULT
100b - Reserved
101b - Reserved
110b - Reserved
111b - Reserved
52.7.1.15
Normal-to-Alarm Freeze Status (N2AF_STATUS)
Offset
Register
Offset
N2AF_STATUS
C4h
Function
See N2AF_STATUS[NAFS].
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
NAFS 
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
Normal-to-Alarm Freeze Status
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2177 / 5251


---
# 페이지 261

Table continued from the previous page...
Field
Function
NAFS
Used only for testing and debugging. Indicates whether FCCU left the NORMAL state and entered the 
ALARM state since the last time this register was cleared and, if so, which non-critical fault caused FCCU 
to do so.
 
To clear this register and the other freeze status registers, see Clear the freeze-
status indicators.
  NOTE  
00h: No Normal-to-Alarm-state transition (cleared)
01h: NCF0
10h: NCF1
...
7Fh: NCF126
80h: NCF127
...
FFh: Multiple Normal-to-Alarm-state transitions
52.7.1.16
Alarm-to-Fault Freeze Status (A2FF_STATUS)
Offset
Register
Offset
A2FF_STATUS
C8h
Function
Used only for testing and debugging. Indicates whether FCCU left the ALARM state and entered the FAULT state since the last 
time this register was cleared and, if so, which type of fault caused FCCU to do so.
 
To clear this register and the other freeze status registers, see Clear the freeze-status indicators.
  NOTE  
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2178 / 5251


---
# 페이지 262

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
AF_SRC 
AFFS 
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
—
Reserved
9-8
AF_SRC
Alarm-to-Fault Source
Used only for testing and debugging. Indicates the type of fault that caused FCCU to leave the ALARM state 
and enter the FAULT state since the last time this register was cleared.
 
To clear this register and the other freeze status registers, see Clear the freeze-
status indicators.
  NOTE  
00b - No Alarm-to-Fault-state fault
01b - Reserved
10b - Non-critical fault
11b - Multiple Alarm-to-Fault-state faults
7-0
AFFS
Alarm-to-Fault Freeze Status
Used only for testing and debugging. Indicates whether FCCU left the ALARM state and entered the FAULT 
state since the last time this register was cleared and, if so, which fault caused FCCU to do so.
 
To clear this register and the other freeze status registers, see Clear the freeze-
status indicators.
  NOTE  
00h: No Alarm-to-Fault-state transition (cleared)
01h: NCF0 (due to an Alarm-state timeout)
10h: NCF1 (due to an Alarm-state timeout)
...
7Fh: NCF126 (due to an Alarm-state timeout)
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2179 / 5251


---
# 페이지 263

Table continued from the previous page...
Field
Function
80h: NCF127 (due to an Alarm-state timeout)
...
FFh: Multiple Alarm-to-Fault-state transitions
52.7.1.17
Normal-to-Fault Freeze Status (N2FF_STATUS)
Offset
Register
Offset
N2FF_STATUS
CCh
Function
Used only for testing and debugging. Indicates whether FCCU left the NORMAL state and entered the FAULT state since the last 
time this register was cleared and, if so, which type of fault caused FCCU to do so.
 
To clear this register and the other freeze status registers, see Clear the freeze-status indicators.
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
NF_SRC 
NFFS 
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
—
Reserved
9-8
NF_SRC
Normal-to-Fault Source
Used only for testing and debugging. Indicates the type of fault that caused FCCU to leave the NORMAL 
state and enter the FAULT state since the last time this register was cleared.
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2180 / 5251


---
# 페이지 264

Table continued from the previous page...
Field
Function
 
To clear this register and the other freeze status registers, see Clear the freeze-
status indicators.
  NOTE  
00b - No Normal-to-Fault-state fault
01b - Reserved
10b - Non-critical fault
11b - Multiple Normal-to-Fault-state faults
7-0
NFFS
Normal-to-Fault Freeze Status
Used only for testing and debugging. Indicates whether FCCU left the NORMAL state and entered the 
FAULT state since the last time this register was cleared and, if so, which fault caused FCCU to do so.
 
To clear this register and the other freeze status registers, see Clear the freeze-
status indicators.
  NOTE  
00h: No Normal-to-Fault-state transition (cleared)
01h: NCF0
10h: NCF1
...
7Fh: NCF126
80h: NCF127
...
FFh: Multiple Normal-to-Fault-state transitions
52.7.1.18
Fault-to-Alarm Freeze Status (F2AF_STATUS)
Offset
Register
Offset
F2AF_STATUS
D0h
Function
See F2AF_STATUS[FAFS].
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2181 / 5251


---
# 페이지 265

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
FAFS 
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
8-0
FAFS
Fault-to-Alarm Freeze Status
Used only for testing and debugging. Indicates whether FCCU left the FAULT state and entered the ALARM 
state since the last time this register was cleared and, if so, which non-critical fault caused FCCU to do so.
 
To clear this register and the other freeze status registers, see Clear the freeze-
status indicators.
  NOTE  
00h: No Fault-to-Alarm-state transition (cleared)
01h: NCF0
10h: NCF1
...
7Fh: NCF126
80h: NCF127
...
FFh: Multiple Fault-to-Alarm-state transitions
52.7.1.19
Non-critical Fault Fake (NCFF)
Offset
Register
Offset
NCFF
DCh
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2182 / 5251


---
# 페이지 266

Function
This register contains a unique code to set a non-critical fault in mutually exclusive mode by the external FAULT interface (signal 
setting). It allows the SW emulation of the non-critical faults, by injecting the fault directly in the FAULT root, to verify the entire 
path and reaction. The reaction following a fake non-critical fault cannot be masked.
This is a write-only register with a set of codes corresponding to each non-critical fault injection.
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
FNCFC 
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
6-0
FNCFC
FNCFC
Fake non-critical fault code
 
Writing to this field injects fake faults; writing 00 and the default value being 0 renders 
different results.
  NOTE  
00h: Fake non-critical fault injection at non-critical fault source 0
01h: Fake non-critical fault injection at non-critical fault source 1
02h: Fake non-critical fault injection at non-critical fault source 2
...
7Fh: Fake non-critical fault injection at non-critical fault source 127
52.7.1.20
IRQ Status (IRQ_STAT)
Offset
Register
Offset
IRQ_STAT
E0h
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2183 / 5251


---
# 페이지 267

Function
This register provides the FCCU interrupt status related to the following events:
• Configuration-state timeout error
• Alarm interrupt
• NMI interrupt
The configuration-state timeout interrupt is asserted if both IRQ_STAT[CFG_TO_STAT] and IRQ_EN[CFG_TO_IEN] bits are 
asserted. It is cleared when a 1 is written to the IRQ_STAT[CFG_TO_STAT] bit.
The NMI and ALARM interrupts are asserted and cleared according to the FCCU state. The status bits of the IRQ_STAT trace the 
status of the related interrupt lines.
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
Reserv
ed 
NMI_
STAT 
ALRM
_ST...
CFG_T
O_...
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
31-5
—
Reserved
4
—
Reserved
3
—
Reserved
2
NMI_STAT
NMI Interrupt Status
0b - NMI interrupt is OFF
1b - NMI interrupt is ON
1
ALRM_STAT
Alarm Interrupt Status
0b - Alarm interrupt is OFF
1b - Alarm interrupt is ON
0
Configuration-State Timeout Status
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2184 / 5251


---
# 페이지 268

Table continued from the previous page...
Field
Function
CFG_TO_STAT
0b - No configuration-stat timeout error
1b - Configuration-state timeout error
52.7.1.21
IRQ Enable (IRQ_EN)
Offset
Register
Offset
IRQ_EN
E4h
Function
This register is used to configure enabling of interrupt related to the "Configuration-state timeout error".
The configuration-state timeout interrupt is asserted if both the IRQ_STAT[CFG_TO_STAT] and IRQ_EN[CFG_TO_IEN] fields are 
set to 1.
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
CFG_T
O_...
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
3
—
Reserved
2-1
—
Reserved
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2185 / 5251


---
# 페이지 269

Table continued from the previous page...
Field
Function
0
CFG_TO_IEN
Configuration-State Timeout Interrupt Enable
0b - Configuration-state timeout interrupt disabled
1b - Configuration-state timeout interrupt enabled
52.7.1.22
Transient Configuration Lock (TRANS_LOCK)
Offset
Register
Offset
TRANS_LOCK
F0h
Function
See TRANS_LOCK[TRANSKEY]
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
TRANSKEY 
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
8-0
TRANSKEY
Transient Configuration Lock
Writable only by code running in Supervisor mode. Temporarily locks and unlocks the configuration. Locking 
the configuration prevents FCCU from entering the CONFIG state. For information about putting FCCU in 
configuration, see Prepare FCCU for configuration and Configure FCCU.
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2186 / 5251


---
# 페이지 270

Table continued from the previous page...
Field
Function
 
You can write to this field when FCCU is in any state, but the lock will not get into effect until 
FCCU is in the NORMAL state.
  NOTE  
BCh: Unlock.
Any other value: Lock.
52.7.1.23
Permanent Configuration Lock (PERMNT_LOCK)
Offset
Register
Offset
PERMNT_LOCK
F4h
Function
See PERMNT_LOCK[PERMNTKEY]
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
PERMNTKEY 
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
8-0
PERMNTKEY
Permanent Configuration Lock
Writable only by code running in the Supervisor mode. Permanently locks the configuration, which prevents 
FCCU from entering the CONFIG state until FCCU is reset. For information about putting FCCU in 
configuration, see Prepare FCCU for configuration and Configure FCCU.
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2187 / 5251


---
# 페이지 271

Table continued from the previous page...
Field
Function
 
You can write to this field when FCCU is in any state, but the lock will not get into effect until 
FCCU is in NORMAL state.
  NOTE  
FFh: Lock.
Any other value: Do nothing.
52.7.1.24
Delta T (DELTA_T)
Offset
Register
Offset
DELTA_T
F8h
Function
The DELTA_T register is used for programming the value of delta_T constant (see DELTA_T), in microseconds.
 
This register can be written only when the FCCU is in the CONFIG state.
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
DELTA_T 
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
29-16
Reserved
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2188 / 5251


---
# 페이지 272

Table continued from the previous page...
Field
Function
—
15-14
—
Reserved
13-0
DELTA_T
Minimum Fault-Output (EOUT) Timer Interval
Applies only to Bi-Stable and Fault-Toggle fault-output modes (CFG[FOM]). Controls the minimum amount 
of time (Tmin) that the fault-output (EOUT) timer runs according to this equation:
Tmin = (250+ DELTA_T) µs * (48000/CLKSAFE freq KHz )
 
The durations shown for the DELTA_T values depend on CLKSAFE signals. For frequency 
of CLKSAFE signals see the chip-specific FCCU information). Also see chip's data sheet for 
the trimmed frequency variation (for example, δFvar).
  NOTE  
52.7.1.25
Non-critical Alarm-State Interrupt-Request Enable (IRQ_ALARM_EN0)
Offset
Register
Offset
IRQ_ALARM_EN0
FCh
Function
See IRQ_ALARM_ENa[IRQENn].
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
IRQEN
7 
IRQEN
6 
IRQEN
5 
IRQEN
4 
IRQEN
3 
IRQEN
2 
IRQEN
1 
IRQEN
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
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2189 / 5251


---
# 페이지 273

Fields
Field
Function
31-8
—
Reserved
7-0
IRQENn
Non-critical Alarm-State Interrupt-Request Enable n
Writable only when FCCU is in the CONFIG state. Changed by FCCU to its reset value when a 
Configuration-state timeout occurs. Controls whether the interrupt request is enabled as the Alarm-state 
reaction for the associated non-critical fault channel (n). When the ALARM state and the Alarm-state 
interrupt request are enabled for an enabled non-critical fault channel, a fault on that channel causes FCCU 
to assert the irq_alarm signal when FCCU enters the ALARM state; irq_alarm remains asserted until FCCU 
is in the NORMAL state. For information on how to configure the non-critical fault channels, see Configure 
the non-critical fault channels.
0b - Disabled 
1b - Enabled
52.7.1.26
Non-critical Fault-State Non-maskable-Interrupt-Request Enable (NMI_EN0)
Offset
Register
Offset
NMI_EN0
10Ch
Function
See NMI_ENa[NMIENn].
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
NMIEN
7 
NMIEN
6 
NMIEN
5 
NMIEN
4 
NMIEN
3 
NMIEN
2 
NMIEN
1 
NMIEN
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
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2190 / 5251


---
# 페이지 274

Fields
Field
Function
31-8
—
Reserved
7-0
NMIENn
Non-critical Fault-State Non-maskable-Interrupt-Request Enable n
Writable only when FCCU is in the CONFIG state. Changed by FCCU to its reset value when a 
Configuration-state timeout occurs. Controls whether the non-maskable interrupt request is enabled as 
a Fault-state reaction for the associated non-critical fault channel (n). When the non-maskable interrupt 
request is enabled for an enabled non-critical fault channel, a fault on that channel causes FCCU to 
assert the NMIOUT signal when FCCU enters the FAULT state; NMIOUT remains asserted until FCCU 
exits FAULT state. For information on how to configure the non-critical fault channels, see Configure the 
non-critical fault channels.
0b - Disabled
1b - Enabled
52.7.1.27
Non-critical Fault-State EOUT Signaling Enable (EOUT_SIG_EN0)
Offset
Register
Offset
EOUT_SIG_EN0
11Ch
Function
See EOUT_SIG_ENa[EOUTENn].
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
EOUT
EN7 
EOUT
EN6 
EOUT
EN5 
EOUT
EN4 
EOUT
EN3 
EOUT
EN2 
EOUT
EN1 
EOUT
EN0 
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
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2191 / 5251


---
# 페이지 275

Fields
Field
Function
31-8
—
Reserved
7-0
EOUTENn
Non-critical Fault-State EOUT Signaling Enable n
Writable only when FCCU is in the CONFIG state. Changed by FCCU to its reset value 
when a Configuration-state timeout occurs. Applies only when the EOUT signals are active 
(CFG[FCCU_SET_AFTER_RESET]). When FCCU is configured for Bi-Stable fault-output mode 
(CFG[FOM]), controls whether EOUT signaling is enabled as a Fault-state reaction for the associated 
non-critical fault channel (n). (For other fault-output modes, EOUT signaling is always enabled, regardless 
of the value of this field.) When EOUT signaling is enabled for an enabled non-critical fault channel, a fault 
on that channel causes FCCU to indicate the faulty condition on the EOUT[1:0] signals when FCCU enters 
the FAULT state. For information on how to configure the non-critical fault channels, see Configure the 
non-critical fault channels.
For all fault-output modes, also controls whether FCCU asserts the FIF signal when a fault on the associated 
non-critical fault channel (n) causes FCCU to enter the FAULT state.
 
For all fault-output modes, you must set this field to enabled to ensure that FCCU 
asserts the FIF signal when FCCU enters FAULT state as the result of a fault on the 
associated non-critical fault channel (n) so the FOSU module does not mistakenly generate 
a destructive chip reset.
  NOTE  
0b - In Bi-Stable fault-output mode, both EOUT signaling and FIF assertion are disabled; in other 
fault-output modes, EOUT signaling is enabled and FIF assertion is disabled.
1b - Both EOUT signaling and FIF assertion are enabled in all fault-output modes.
52.7.1.28
Alarm-State Timer (TMR_ALARM)
Offset
Register
Offset
TMR_ALARM
12Ch
Function
See TMR_ALARM[COUNT].
This table shows how the Alarm-state timer's state and value vary by FCCU state:
Table 302. TMR_ALARM reset value
FCCU state
Timer state
Timer value
CONFIG
Idle
0000_0000h
NORMAL
Idle
Initial value: NCF_TO[TO]
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2192 / 5251


---
# 페이지 276

Table 302. TMR_ALARM reset value (continued)
FCCU state
Timer state
Timer value
ALARM
Running
Value when read
FAULT
Idle
End of count
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
COUNT 
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
COUNT 
W
Reset
1
0
1
0
1
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
1. The default reset value is provided by NCF_TO[TO]. See Table 302 for the reset value at different FCCU states.
Fields
Field
Function
31-0
COUNT
Alarm-State Timer Count
Specifies the value of the Alarm-state timer in CLKSAFE periods.
52.7.1.29
Configuration-State Timer (TMR_CFG)
Offset
Register
Offset
TMR_CFG
134h
Function
See TMR_CFG[COUNT].
This table shows how the Configuration-state timer's state and value vary by FCCU state:
FCCU state
Timer state
Timer value
CONFIG
Running
Value when read
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2193 / 5251


---
# 페이지 277

Table continued from the previous page...
FCCU state
Timer state
Timer value
NORMAL
Idle
000F_FFFFh
ALARM
Idle
000F_FFFFh
FAULT
Idle
000F_FFFFh
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
COUNT 
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
COUNT 
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
COUNT
Configuration-State Timer Count
Specifies the value of the Configuration-state timer in CLKSAFE periods.
52.7.1.30
Fault-Output Timer (TMR_ETMR)
Offset
Register
Offset
TMR_ETMR
138h
Function
See TMR_ETMR[COUNT].
This table shows how the fault-output timer's state and value vary by FCCU state and fault-output mode:
FCCU state
Timer state (value)
CONFIG
Not Fault-Toggle: Idle (0000_0000h)
Table continues on the next page...
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2194 / 5251


---
# 페이지 278

Table continued from the previous page...
FCCU state
Timer state (value)
Fault-Toggle: Running (value when read) or idle (0000_0000h)
NORMAL
Not Fault-Toggle: Idle (0000_0000h)
Fault-Toggle: Running (value when read) or idle (0000_0000h)
ALARM
Not Fault-Toggle: Idle (0000_0000h)
Fault-Toggle: Running (value when read) or idle (0000_0000h)
FAULT
Not Fault-Toggle: Running (value when read. It is an up-
counter which rollbacks to zero after reaching maximum value 
and then it begins counting again.)
Fault-Toggle: Running (value when read) or idle (0000_0000h)
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
COUNT 
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
COUNT 
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
COUNT
Fault-Output Timer Count
Specifies the value of the fault-output timer in CLKSAFE periods.
52.7.2 Configuration registers
52.7.2.1
Definition
Configuration registers are registers that:
• Let you configure FCCU's Alarm-state timer interval, fault channels, and fault-output (EOUT) signals.
• You can write to only when the configuration is not locked and FCCU is in CONFIG state (see Put FCCU in the CONFIG state).
• Save the values you write to them while FCCU is in CONFIG state only after you manually put FCCU in NORMAL 
state. If FCCU automatically leaves CONFIG state and enters NORMAL state because the configuration-timer interval 
(CFG_TO[TO]) expires (called a Configuration-state timeout), FCCU changes the value of the Configuration (CFG) register 
to its Configuration-state-timeout value and the value of each of the other configuration registers to its reset value; FCCU also 
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2195 / 5251


---
# 페이지 279

changes the value of the Configuration-State Timeout Interval (CFG_TO) register to its reset value. For information on the 
Configuration-state timeout value, see CFG register bit value at different events.
52.7.2.2
Configuration registers
Following is the list of configuration registers in this module. They are listed in an offset order from lowest to highest.
• Configuration (CFG)
• Non-critical Fault Configuration (NCF_CFGa)
• Non-critical Fault-State Configuration (NCFS_CFG0)
• Non-critical Fault Enable (NCF_E0)
• Non-critical-Fault Alarm-State Timeout Enable (NCF_TOE0)
• Non-critical-Fault Alarm-State Timeout Interval (NCF_TO)
• Delta T (DELTA_T)
• Non-critical Alarm-State Interrupt-Request Enable (IRQ_ALARM_EN0)
• Non-critical Fault-State Non-maskable-Interrupt-Request Enable (NMI_EN0)
• Non-critical Fault-State EOUT Signaling Enable (EOUT_SIG_EN0)
52.7.3 CFG register bit value at different events
In this chip, there are no events that affect the bits in the configuration register.
52.8 Glossary
CF
Critical fault
EOUT
Error out
FOSU
FCCU output supervision unit
FSM
Finite state machine
intf
Interface
IRQ
Interrupt request
NCF
Non-critical fault
NMI
Non-maskable interrupt
NXP Semiconductors
Fault Collection and Control Unit (FCCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2196 / 5251


---