# 페이지 227

Chapter 47
Power Control Unit (MC_PCU)
47.1 Introduction
The power control unit (MC_PCU) is used for initiating a Standby mode entry that reduces the overall chip power consumption. 
Power can be saved by disconnecting parts of the chip from the power supply. The blocks inside the chip are grouped into multiple 
parts having this capability, which are called "power domains".
When a power domain is disconnected from the supply, the power consumption is reduced to zero and the configuration of the 
every core and module that belongs to such power domain is completely lost. When you reconnect a power domain to the supply 
voltage, the domain draws an increased current until the power domain reaches its operational voltage. Maximum power saving 
is achieved by entering the Standby mode.
After the MC_ME asserts a standby entry request, MC_PCU initiates the power sequence, which is non-retractable and includes 
the handshake with the chip power management controller. The power-up/down sequences are handled by FSMs to ensure a 
smooth and safe transition into and out of the Standby mode. Exiting the Standby mode can only be done through a system 
wakeup event, power-on reset, destructive reset, or a functional reset.
47.2 Power sequence FSM
MC_PCU implements an FSM to initiate the power sequencing of the Standby mode entry/exit sequence for the chip.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1885 / 5251


---
# 페이지 228

IDLE
Input ISO. active
INTF
LOCK
Output ISO. active
SW OPEN
PWR DOWN
INTF
UNLOCK
SW L
CLOSE
SW H
CLOSE
PWR UP
FIRC PowerDown
Input ISO inactive
Output ISO inactive
FIRC PowerUp
Reset event (Functional/destructive) activated
or
Wakeup source activated
standby entry request
PMC in low
power mode 
PMC in full
performance mode
Switchable domain supply ON 
Switchable domain supply OFF 
MC_ME
software low-power
entry process
Figure 198. MC_PCU FSM
 
When destructive reset is asserted from MC_RGM, MC_PCU FSM moves to the IDLE state immediately. Indication 
of this is not shown in the above figure.
  NOTE  
Table 267. MC_PCU FSM transition description
State
Name
Exit condition
Signal controlled
Signal monitored
IDLE
Idle state
Standby request 
received from MC_ME
-
-
MC_ME software low 
power entry process
MC_ME software low 
power entry process
Software entry 
sequence completed 
(SW4 process 
completed)
-
-
INTF LOCK
Interface lock state
Input isolation active
Input isolation 
activation
Input isolation active
Table continues on the next page...
NXP Semiconductors
Power Control Unit (MC_PCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1886 / 5251


---
# 페이지 229

Table 267. MC_PCU FSM transition description (continued)
State
Name
Exit condition
Signal controlled
Signal monitored
SW OPEN
Switch open state
Output isolation active, 
Switchable domain 
supply turned off
Output isolation 
activation, low power 
mode request to PMC
Output isolation active, 
Switchable domain 
supply
PWR DOWN
Power down state
Wakeup/functional 
reset occurrence
FIRC power down
Wakeup and functional 
reset
PWR UP
Power up state
PMC in full 
performance mode
-
-
SW H CLOSE
Switch H close state
Switchable domain 
supply turned on
-
Switchable domain 
supply
SW L CLOSE
Switch L close state
Input isolation inactive
Input isolation inactive
Input isolation active
INTF UNLOCK
Interface unlock
-
-
-
47.3 Glossary
FSM
Finite state machine
NXP Semiconductors
Power Control Unit (MC_PCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1887 / 5251


---