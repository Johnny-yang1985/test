# 페이지 106

Chapter 25
Clock Generation Module (MC_CGM)
25.1 Chip-specific MC_CGM information
25.1.1 Associated content references
See the Clocking chapter for details pertaining to these:
• Chip clocking
• MC_CGM clock source mapping (see the "MC_CGM clock sources mapping" section for this)
• MC_CGM clock multiplexers (see the "MC_CGM clock multiplexers" section for this)
 
Clock sources listed in the MUX_n_CSC[SELCTL] bit field are defined based on S32K388 and S32K389. For other 
variants, see the clock system diagrams in section “Clocking overview” in the “Clocking ” chapter.
  NOTE  
 
MC_CGM clock multiplexer configurations to non-supported and reserved clock sources are prohibited and can 
result in chip malfunctioning.
  CAUTION  
25.1.2 Clock Mux 7 select control register MUX_7_CSC[SELCTL] description (S32K328, S32K338, 
S32K348, and S32K358)
Table 173. MUX_7_CSC[SELCTL] description
Bit field
Description
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 7. The reserved values are not displayed.
0_0000b - FIRC_CLK
0_1000b - PLL_PHI0_CLK
0_1100b - PLL_AUX_PHI0_CLK
1_1000b - GMAC_MII_RMII_RGMII_TX_CLK
1_1001b - GMAC_MII_RGMII_RX_CLK
25.1.3 Clock Mux 7 select control register MUX_7_CSC[SELCTL] description (S32K344, S32K324, 
S32K314, S32K322, S32K341 and S32K342)
Table 174. MUX_7_CSC[SELCTL] description
Bit field
Description
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 7. The reserved values are not displayed.
0_0000b - FIRC_CLK
1_1000b - EMAC_MII_RMII_TX_CLK
1_1001b - EMAC_MII_RX_CLK
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1008 / 5251


---
# 페이지 107

25.2 Introduction
The clock generation module (MC_CGM) is used to set up the configurable clock domains used by various chip blocks as per the 
application needs. It includes the clock multiplexers that allow software to select the desired clock sources for these domains. This 
is managed by the MC_CGM to ensure that the changing of the clock selection from one source to another occurs in a glitch-less 
fashion. In addition, the MC_CGM includes the clock dividers that can be configured by software.
See following figure for the MC_CGM block diagram:
MC_CGM
PCFS configuration registers
DIV
DIV
DIV
DIV
DIV
DIV
%
%
%
Clock Mux 0
Clock Mux 1
Clock Mux 20
Clock sources
(input)
Generated Clocks
(output)
Configuration
bus
PCFS
PCFS
PCFS
Figure 124. MC_CGM block diagram
 
The block diagram is generic and does not necessarily reflect any specific MC_CGM implementation.
  NOTE  
25.3 Features
MC_CGM includes the following features:
• Implements software configurable clock multiplexers for selecting from various clock sources
• Provides hardware-controlled multiplexers that guarantee glitchless transition, while the software-controlled multiplexers 
need a software sequence to ensure such a transition
• Provides software configurable automatic PCFS on certain clocks to minimize the impact of a sudden power consumption 
change through a gentle ramp-down and -up of the clock frequency when switching clock sources
• Implements software configurable clock dividers
25.4 Functional description
25.4.1 Clock selection multiplexer
Each of the clock multiplexers inside the MC_CGM either implements a fully hardware-controlled clock multiplexer or a 
software-controlled clock multiplexer. The following sections describe the two variants of the clock multiplexer.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1009 / 5251


---
# 페이지 108

25.4.1.1
Hardware-controlled clock multiplexer
In hardware-based clock multiplexing, the underlying assumption is that under some conditions, error or reset states, software 
may not be active. Therefore, the clock switching is fully hardware based and is glitchless. To facilitate clock switching requests 
with software, the MUX_n_CSC and MUX_n_CSS registers implement request and status for the clock multiplexer, the rest 
is managed in hardware. Using these registers, the software can monitor the state of the hardware-based clock multiplexer 
and also make clock switching requests. It is recommended that a new clock switch request is given only when there are 
no pending/ongoing clock switching requests. However, a switch to the safe clock, that is, FIRC, can be performed at any 
instance of time. A switch to the safe clock is always completed. Software should ensure that while making a software-based 
switch to safe clock, the register configuration clock should be available, at least for completing the write to the MUX_n_CSC 
register. This means that the clock should be running for the register write to complete. Hardware clock multiplexer also 
supports hardware-based switch to safe clock, which is requested externally to MC_CGM (for example, by MC_RGM). For a 
hardware-based switch to safe clock, it is not required to have a register configuration clock for MC_CGM.
 
• "Switch to safe clock" from software is requested by programming the MUX_n_CSC[SAFE_SW] bit field only 
and not by combining the MUX_n_CSC[CLK_SW] and MUX_n_CSC[SELCTL] bit fields of the MUX_n_CSC 
register. Writes to other fields are ignored when requesting switch for safe clock.
• After the switch to the safe clock requested by the MC_RGM has completed, the MC_RGM also requests the 
clock dividers to switch to their default values. This hardware-triggered divider update can be monitored in the 
same manner as for software-configured updates, and software should use it to ensure that the configuration 
update has completed before reconfiguring the clocks.
• Write accesses to the MUX_n_CSC register with clock select pointing to the "reserved" input clock source are 
aborted with bus transfer errors.
  NOTE  
See Figure 125 that shows the flowchart representation for the sequence of steps to be followed when making a clock switch 
request to hardware-controlled clock multiplexer. Switch to safe clock can be requested at any instance of time, and for clarity 
reasons, it is not shown in Figure 125.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1010 / 5251


---
# 페이지 109

Y
N
Read
MUX_n_CSS
MUX_n_CSS
[SWIP] completed?
Start
Read
MUX_n_CSS
Configure
MUX_n_CSC
for clock switch
Wait for CLK_SW or
SAFE_SW or
RAMPDOWN or 
RAMPUP fields to auto-clear
N
Y
End
Check the
MUX_n_CSS[SWTRG]
field status
MUX_n_CSS
[SWIP] in progress?
Figure 125. Flow for clock switch request on hardware-controlled clock multiplexer
 
• A switch to the safe clock command always leads to a ramp-down from the currently selected clock and then 
a switch to "safe clock", except when there is an ongoing clock switch requested by the software without 
ramp-up and ramp-down. A safe clock switch request when there is an ongoing clock switch without ramp-up 
or ramp-down results in a switch to the safe clock without performing a ramp-down (either by MC_RGM or 
provided using the MUX_n_CSC register) does not perform a ramp-down before switching to "safe clock".
• The above flowchart steps can be preceded by points 1 and 3 below:
1. Disable the divider.
2. Switch clocks through hardware multiplexer.
3. Enable and configure the dividers (atomic write instruction).
  NOTE  
25.4.1.2
Software-controlled clock multiplexer
In software-based clock multiplexing, the underlying assumption is that the software is always available and there are no error or 
reset conditions in the chip. This implies that a glitchless switch between input clock sources of MC_CGM MUX can be achieved 
by following a sequence of steps in software. The software-based clock multiplexer implements a clock gate at the output of 
the clock mux. The software can gate the selected clock of MC_CGM MUX using a synchronous/graceful clock gate bit (that is, 
MUX_n_CSC[CG]) or a forced clock gate bit (that is, MUX_n_CSC[FCG]). The hardware does not guarantee that any glitches will 
escape when using forced clock gating. When a forced clock gate bit is written to 1, the internal clock gate forcefully gates the 
selected clock to logic-0, therefore, to avoid clock glitches, it should be ensured that the selected clock source is not running. See 
Figure 126 that shows the flowchart representation for the sequence of steps to be followed when making a clock switch request 
to software-controlled clock multiplexer. No switch to safe clock is supported in software-controlled clock multiplexer.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1011 / 5251


---
# 페이지 110

Start
Is current clock
source active?
N
Y
Read 
MUX_n_CSS
Y
N
Select the desired 
clock source
Read 
MUX_n_CSS
Y
N
End
Is current clock
source active? 
Y
N
Write logic-1 to
MUX_n_CSC[FCG] 
Write logic-0 to
MUX_n_CSC[FCG],
if it is logic-1 
Write logic-1 to
MUX_n_CSC[CG] 
Write logic-0 to
MUX_n_CSC[CG] 
Write logic-1 to
MUX_n_CSC[CG] 
Is
MUX_n_CSS[CS]
logic-0?
Is
MUX_n_CSS[CS]
logic-1?
Figure 126. Flow for clock switch request on software controlled clock multiplexer
 
• Ensure that before using the force gate bit, any IP or other logic using the clock of MC_CGM MUX is in the 
inactive state or a clock glitch resulting from usage of forced gating does not effect the IP (that is, it is clock 
gated after the MC_CGM).
• In Figure 126, the clock source to be selected should be active at the time of clock switch, else the 
MUX_n_CSS[CS] field will remain set to logic-0. In case the clock source to be selected becomes inactive (that 
is, loss of clock, and so on) during the switching operation, the switch to another clock source can be initiated 
by writing both the MUX_n_CSC[CG] and MUX_n_CSC[FCG] fields to logic-1.
• Writing a 'reserved' value for the MUX_n_CSC[SELCTL] field may result in an unpredictable clock at the output 
of the clock multiplexer.
  NOTE  
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1012 / 5251


---
# 페이지 111

 
The above flowchart steps can be preceded by points 1 and 3 below:
1. Disable the divider.
2. Switch clocks through software multiplexer.
3. Enable and configure the dividers (atomic write instruction).
  NOTE  
25.4.2 PCFS
MC_CGM implements PCFS when changing clock source at an MC_CGM clock mux. The PCFS is only implemented in a 
hardware-controlled clock multiplexer and not in a software-controlled clock multiplexer. It allows a gradual load change for a 
power/voltage supply unit by employing a gradual frequency changeover from one to another. The frequency changeover is 
achieved by clock division of input clock source with a sequence of division values, where frequency ramp down and ramp up 
is achieved when the sequence of division values are ascending and descending in nature, respectively. As the clock division 
(fractional) is implemented in digital logic, therefore, it is a coarse-level clock division rather than being an accurate-level division, 
implying that the duty cycle of the progressively divided clock can vary with time.
The PCFS feature is utilized when a drain current to frequency relationship is known, that is, for a given drain current what is the 
maximum allowed change in frequency (fchg). The fchg is the first input parameter for PCFS and other parameters for PCFS are 
specified or calculated in relation to FIRC.
The PCFS hardware generates the clock division factors based on certain values that are programmed into the PCFS 
configuration register. The following pseudo codes represent the generation of clock division value sequence (di).
/* ramp down division values (dn) with k steps*/
      delta1 = RATE/1000;
      delta2 = RATE/1000;
      d0       = 1.0;
      for i=1 to k-1 do
        di = di-1 + delta1;
        delta1 = delta1 + delta2;
      endfor
/* ramp up division values (dn) with k steps*/
      delta1 = RATE*k/1000;
      delta2 = RATE/1000;
      d0       = 1.0 + RATE*k*(k+1)/2;
      for i=1 to k-1 do
        di = di-1 - delta1;
        delta1 = delta1 - delta2;
    endfor
As the generation of clock division values is not a closed-bounded function, calculating RATE for a given fchg is an iterative 
process. Find a value of RATE that produces a clock division sequence, which when used does not lead to a frequency change 
greater than fchg. See Table 175 that tabulates some of the RATE values against amax, where
amax=fchg/Fi
where, Fi is the frequency of ith input clock source of the clock mux.
Table 175. PCFS RATE values
amax
PCFS rate
0.005
12
0.01
48
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1013 / 5251


---
# 페이지 112

Table 175. PCFS RATE values (continued)
amax
PCFS rate
0.15
112
0.20
184
The last clock division factor in case of ramp-down or the first clock in case of ramp-up (following a ramp-down procedure), should 
be such that clock switch from any input clock source to another should be termed as safe, indicating that load changes have 
sustainable power effects. This frequency level is referred to as "safe frequency", equivalent to frequency of FIRC referred to as 
"safe clock" with frequency "safe clock frequency" (fsafe). The last clock division factor in the sequence of clock division factors 
happens after "k" steps. The factor k (=steps) is calculated by using the following formula:
 k = ceil(0.5 + sqrt(0.25 - (2000 * (1 -(Fi/fsafe)) / RATE)))
Using the above formula, all the PCFS register configuration values can be calculated for a given frequency of a clock source:
PCFS_DIVEi.DIV = (Fi/fsafe)*1000-1;
        PCFS_DIVCi.INIT = RATE * k;
        PCFS_DIVCi.RATE = RATE;
        PCFS_DIVSi.DIV  = 999 + (RATE * k * (k+1)/2);
See Figure 127 that shows a graphical representation of the change in frequency, which happens during PCFS ramp-down 
and ramp-up.
N
Max
Frequency change rate for ramp-down and ramp-up
Frequency change -->
Figure 127. PCFS steps vs frequency changes
For any given clock source, if its frequency is less than that of FIRC, then its corresponding registers should be programmed to 
default values, where the default values are such that PCFS divider start and PCFS divider end values are same and equal to 
divide-by-1. The default values ensure that no progressive clock division is done when a clock switch request is given to switch 
from or to that source.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1014 / 5251


---
# 페이지 113

 
Calculate the minimum frequency during the PCFS RAMPDOWN and RAMPUP operations by using the formula:
(FIRC/((PCFS_DIVE+1)/1000)) MHz
  NOTE  
25.4.2.1
PCFS control
The PCFS operation is configured by a set of configuration registers. One set pertains to the calculation of the clock division 
factors, which are PCFS_DIVC, PCFS_DIVE, PCFS_DIVS, and PCFS_SDUR, while the registers MUX_n_CSC and MUX_n_CSS 
implement trigger and status of the PCFS operation. The clock division factors are expected to be programmed before any other 
MC_CGM operation is initiated and remain unchanged. All the registers corresponding to the clock division factors should be 
programmed with FIRC as the configuration clock and before doing any clock switch or PCFS operation on any of the MC_CGM 
mux. It should be noted that the default values of the register corresponding to clock division factors are such that only the clock 
division factor is calculated by hardware that is divide-by-1. The PCFS operation is always triggered when the safe clock request is 
generated except when there is an on-going clock switch without ramp-up or ramp-down. Therefore, the software needs to ensure 
that the PCFS configuration is complete and correct.
While configuring MUX_n_CSC, only valid PCFS and clock switch requests should be provided. PCFS or clock switch requests 
should only be provided if the PCFS operation is in the idle state. If there is an ongoing PCFS operation, it is recommended not 
to provide any new PCFS triggers (except switch to safe clock) until the ongoing operation is completed. Switch to safe clock via 
hardware or by register configuration can be provided at any instance of time and is always completed. Valid combinations of 
PCFS and clock switches triggers are listed in Table 176. All the PCFS commands should be atomic in nature, which means a 
single register write should provide complete PCFS sequence to be executed that is ramp-down, clock switch, and ramp-up.
Table 176. Valid PCFS and clock switch requests
PCFS operation state
Command
Idle
Ramp-down, clock switch, and ramp-up
Idle
Clock switch only (without ramp-up or ramp-down)
When a switch to safe clock is provided by writing to MUX_n_CSC, then writes to other register fields are ignored.
25.4.2.2
Clock source power-up and selection
This section provides guidelines for powering up a given clock source and selecting it at the MC_CGM clock multiplexer.
Following is the power-up procedure for a clock source:
1. Configure the parameter, if any.
2. Configure the power-up (or power-down) control field.
3. Wait for the power-up status indication.
After a power-up indication, the clock source can be selected to provide output clock at an MC_CGM clock multiplexer. A 
clock-monitoring setup can also be activated on the powered-up clock source.
See Figure 128 that shows a flow chart representation of this sequence.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1015 / 5251


---
# 페이지 114

Start
Program clock source 
configuration register(s)
Power-up the clock 
source
Is clock 
source 
stable?
No
Program clock mux 
control for corresponding 
clock selection inside 
MC_CGM with PCFS
Yes
PCFS to 
destination clock 
is triggered
Setup clock
monitor for power-up
clock source
Read the PCFS 
completion status
Is PCFS 
complete? 
No
Yes
End
Program the corresponding
PCFS configuration
register inside MC_CGM
Read the clock source
stabilization status (for
example, PLL LOCK
Figure 128. Clock source power-up and selection procedure
25.4.2.3
Clock source power-down and deselection
This section provides guidelines for powering down a given clock source and deselecting it at MC_CGM clock multiplexer.
Following is the power-down procedure for a clock source:
1. Deselect the clock source at all MC_CGM clock multiplexers.
2. Configure the power-up (or power-down) control field.
3. Wait for the power-down status indication.
See Figure 129 that shows a flow chart representation of this sequence.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1016 / 5251


---
# 페이지 115

Read the PCFS 
completion status
Start
Deselect clock source at
all clock muxs of
MC_CGM with PCFS
PCFS to
destination clock
is triggered
Program the clock
source to power down
Read the clock source
power status
Is PCFS
complete?
Yes
No
Yes
No
Is clock source
powered down?
End
Figure 129. Clock source power-down and clock source deselection procedure
25.4.2.4
Clock switch with load change
This section provides guidelines to switch between two high-frequency clock sources along with load changes in the system. 
Load change is referred to switching ON or OFF of logic/peripherals in the system, which has an effect of significant capacitance 
changes on the chip. This triggers the voltage regulation for the chip.
When a large number of peripherals or digital logic is enabled or disabled, it is recommended that this step should be performed at 
a low frequency. Independent of whether a clock switch is required, this criteria needs to be met. When a clock switch is required 
at two high frequencies, the recommended sequence is as follows:
1. Intermediately switch to FIRC.
2. Change load (that is, enable/disable peripherals).
3. Switch to the target clock.
See the following figure that shows a flow chart representation of this sequence.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1017 / 5251


---
# 페이지 116

Start
Select FIRC at clock 
muxs of MC_CGM where load 
change is required with PCFS
PCFS to 
destination clock 
is triggered
Read the PCFS 
completion status
Is PCFS 
complete? 
No
Yes
Program clock mux 
control inside MC_CGM 
to select target clock with 
PCFS
PCFS to 
destination clock 
is triggered
Read the PCFS 
completion status
Is PCFS 
complete? 
No
Yes
End
Perform load 
change
Figure 130. Clock switch with load change procedure
25.4.3 Clock dividers
Clock dividers are used for the generation of a divided clock that is used for running IPs or peripherals. The MC_CGM provides 
the following built-in dividers at each clock mux:
• 50% clock dividers
Each divider can be controlled by the Divider Enable (DE) bit and the Division Value (DIV) field. If a divider has its DE bit set to 
logic-0 in the respective configuration register, then that divider is disabled and the output divided clock is held to logic-0. If the 
DE bit is logic-1, the divider is enabled and provides a divided clock according to the value set in the DIV field.
25.4.3.1
50% clock divider
50% duty cycle dividers generate a real divided clock. The division factor is always an integer but is not restricted to even numbers. 
The rising edge of the divided clock is always synchronous to the rising edge of the divider source clock, but the falling edge is 
synchronous to the rising edge or the falling edge depending on whether the division factor is even or odd, respectively. If the input 
clock has a duty cycle of 50%, the divided output clock maintains the same 50% duty cycle. See Figure 131 that shows the 50% 
clock divider operation and its associated signals.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1018 / 5251


---
# 페이지 117

Clock input
Divider counter
3
2
1
0
3
2
1
0
3
2
1
0
3
2
1
0
Divided clock output (%4)
Figure 131. 50% clock divider programmed for divide by 4 (DIV=3)
A 50% divided clock can be considered asynchronous (not edge aligned) to other divided clocks from dividers at the same clock 
mux. 50% clock dividers are implemented without an active closed loop, and are expected not to get stuck if the input clock glitches 
for a single cycle.
25.4.3.2
Clock dividers update
To update the division value or the divider enable, the software should follow the procedure as shown in Figure 132. These updates 
happen only after the current division cycle has elapsed. However, if the phase of the clock divider is updated, the update happens 
independently from the state of the division cycle. Any update to the clock divider fields does not result in clock glitch either at the 
divided clock output or the phase-divided clock output.
Start
Configure the 
MUX_n_DIV_x register
Read the
MUX_n_DIV_UPD_STAT
register
Is divider
update complete?
Y
N
End
Figure 132. Flow for clock divider programming update
Following is the procedure for updating the dividers using the common trigger update:
1. Configure the MUX_n_DIV_TRIG_CTRL register.
2. Wait for the update to finish (until MUX_n_DIV_UPD_STAT is 0).
3. Update the clock dividers (only 50%) per the divider update procedure.
4. After the divider update is finished, perform a write operation on the MUX_n_DIV_TRIG register.
5. Wait for the update to finish, that is, until MUX_n_DIV_UPD_STAT is 0. During this period, the following process takes place:
• Halt handshake is initiated if configured in step 1.
• Clock dividers is updated only when AXBS is halted (that is, halt acknowledgment is received by MC_CGM). It is 
initiated, else the dividers are updated at alignment.
• After the clock dividers are updated, MUX_n_DIV_UPD_STAT is asserted to 0.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1019 / 5251


---
# 페이지 118

• When the bit fields MUX_x_DIV_TRIG_CTRL[TCTL] and MUX_x_DIV_TRIG_CTRL[HHEN] are set to 1, then any 
write operation on trigger register will assert (MUX_n_DIV_UPD_STAT). Once the dividers are updated and aligned 
(MUX_n_DIV_UPD_STAT) will be deasserted.
 
• The MUX_x_DIV_TRIG_CTRL[HHEN] bit should only be set when MUX_x_DIV_TRIG_CTRL[TCTL] is set, 
otherwise it may lead to misalignment of the dividers.
• In case of divider initialization by MC_RGM, a halt handshake protocol is initiated if the corresponding register 
bit is set and the clock dividers are initialized after the halt handshake protocol completion.
  NOTE  
6. This completes the divider update.
7. When multiple writes to the dividers of same clock MUX is made without waiting for the previous update status signal to 
finish may lead to misalignment of the dividers.
For aligned dividers, the LCM of the division values programmed in the dividers of respective clock mux should be less than 100.
 
Performing multiple writes to the divider without waiting for the earlier update to complete can lead to misalignment 
of the dividers.
  NOTE  
Recommended software sequence for ensuring no undivided output at MC_CGM:
1. Reset is de-asserted
2. MC_RGM goes to IDLE
3. Enable the clock dividers of MC_CGM to provide FIRC clock so that reset of fixed dividers can be lifted.
4. Program the MC_CGM as per use case division values.
5. Switch the clock of MC_CGM Mux to desired one, and run the system.
25.5 MC_CGM register descriptions
MC_CGM implements a set of clock multiplexers that share PCFS configuration registers. MC_CGM registers have the 
following properties:
• All registers are 32-bit wide.
• Only 32-bit read and write accesses are supported.
• Read/write accesses of less than 32 bits terminate with an error.
• Writes to read-only register fields in writable registers are ignored and do not provide an error response.
• Writes to read-only registers are aborted with an error response.
25.5.1 MC_CGM memory map
MC_CGM base address: 402D_8000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
PCFS Step Duration (PCFS_SDUR)
32
RW
0000_0000h
58h
PCFS Divider Change 8 Register (PCFS_DIVC8)
32
RW
0000_0000h
5Ch
PCFS Divider End 8 Register (PCFS_DIVE8)
32
RW
0000_03E7h
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1020 / 5251


---
# 페이지 119

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
60h
PCFS Divider Start 8 Register (PCFS_DIVS8)
32
RW
0000_03E7h
300h
Clock Mux 0 Select Control Register (MUX_0_CSC)
32
RW
0000_0000h
304h
Clock Mux 0 Select Status Register (MUX_0_CSS)
32
R
0008_0000h
308h
Clock Mux 0 Divider 0 Control Register (MUX_0_DC_0)
32
RW
8000_0000h
30Ch
Clock Mux 0 Divider 1 Control Register (MUX_0_DC_1)
32
RW
8000_0000h
310h
Clock Mux 0 Divider 2 Control Register (MUX_0_DC_2)
32
RW
8001_0000h
314h
Clock Mux 0 Divider 3 Control Register (MUX_0_DC_3)
32
RW
8000_0000h
318h
Clock Mux 0 Divider 4 Control Register (MUX_0_DC_4)
32
RW
8000_0000h
31Ch
Clock Mux 0 Divider 5 Control Register (MUX_0_DC_5)
32
RW
8007_0000h
320h
Clock Mux 0 Divider 6 Control Register (MUX_0_DC_6)
32
RW
8000_0000h
324h
Clock Mux 0 Divider 7 Control Register (MUX_0_DC_7)
32
RW
8000_0000h
334h
Clock Mux 0 Divider Trigger Control Register 
(MUX_0_DIV_TRIG_CTRL)
32
RW
0000_0000h
338h
Clock Mux 0 Divider Trigger Register (MUX_0_DIV_TRIG)
32
W
0000_0000h
33Ch
Clock Mux 0 Divider Update Status Register 
(MUX_0_DIV_UPD_STAT)
32
R
0000_0000h
340h
Clock Mux 1 Select Control Register (MUX_1_CSC)
32
RW
0000_0000h
344h
Clock Mux 1 Select Status Register (MUX_1_CSS)
32
R
0008_0000h
348h
Clock Mux 1 Divider 0 Control Register (MUX_1_DC_0)
32
RW
0000_0000h
37Ch
Clock Mux 1 Divider Update Status Register 
(MUX_1_DIV_UPD_STAT)
32
R
0000_0000h
380h
Clock Mux 2 Select Control Register (MUX_2_CSC)
32
RW
0000_0000h
384h
Clock Mux 2 Select Status Register (MUX_2_CSS)
32
R
0008_0000h
388h
Clock Mux 2 Divider 0 Control Register (MUX_2_DC_0)
32
RW
0000_0000h
3BCh
Clock Mux 2 Divider Update Status Register 
(MUX_2_DIV_UPD_STAT)
32
R
0000_0000h
3C0h
Clock Mux 3 Select Control Register (MUX_3_CSC)
32
RW
0000_0000h
3C4h
Clock Mux 3 Select Status Register (MUX_3_CSS)
32
R
0008_0000h
3C8h
Clock Mux 3 Divider 0 Control Register (MUX_3_DC_0)
32
RW
0000_0000h
3FCh
Clock Mux 3 Divider Update Status Register 
(MUX_3_DIV_UPD_STAT)
32
R
0000_0000h
400h
Clock Mux 4 Select Control Register (MUX_4_CSC)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1021 / 5251


---
# 페이지 120

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
404h
Clock Mux 4 Select Status Register (MUX_4_CSS)
32
R
0008_0000h
408h
Clock Mux 4 Divider 0 Control Register (MUX_4_DC_0)
32
RW
0000_0000h
43Ch
Clock Mux 4 Divider Update Status Register 
(MUX_4_DIV_UPD_STAT)
32
R
0000_0000h
440h
Clock Mux 5 Select Control Register (MUX_5_CSC)
32
RW
0000_0000h
444h
Clock Mux 5 Select Status Register (MUX_5_CSS)
32
R
0002_0000h
448h
Clock Mux 5 Divider 0 Control Register (MUX_5_DC_0)
32
RW
8001_0000h
47Ch
Clock Mux 5 Divider Update Status Register 
(MUX_5_DIV_UPD_STAT)
32
R
0000_0000h
480h
Clock Mux 6 Select Control Register (MUX_6_CSC)
32
RW
0000_0000h
484h
Clock Mux 6 Select Status Register (MUX_6_CSS)
32
R
0002_0000h
488h
Clock Mux 6 Divider 0 Control Register (MUX_6_DC_0)
32
RW
8001_0000h
4BCh
Clock Mux 6 Divider Update Status Register 
(MUX_6_DIV_UPD_STAT)
32
R
0000_0000h
4C0h
Clock Mux 7 Select Control Register (MUX_7_CSC)
32
RW
0000_0000h
4C4h
Clock Mux 7 Select Status Register (MUX_7_CSS)
32
R
0008_0000h
4C8h
Clock Mux 7 Divider 0 Control Register (MUX_7_DC_0)
32
RW
0000_0000h
4FCh
Clock Mux 7 Divider Update Status Register 
(MUX_7_DIV_UPD_STAT)
32
R
0000_0000h
500h
Clock Mux 8 Select Control Register (MUX_8_CSC)
32
RW
0000_0000h
504h
Clock Mux 8 Select Status Register (MUX_8_CSS)
32
R
0008_0000h
508h
Clock Mux 8 Divider 0 Control Register (MUX_8_DC_0)
32
RW
0000_0000h
53Ch
Clock Mux 8 Divider Update Status Register 
(MUX_8_DIV_UPD_STAT)
32
R
0000_0000h
540h
Clock Mux 9 Select Control Register (MUX_9_CSC)
32
RW
0000_0000h
544h
Clock Mux 9 Select Status Register (MUX_9_CSS)
32
R
0008_0000h
548h
Clock Mux 9 Divider 0 Control Register (MUX_9_DC_0)
32
RW
0000_0000h
57Ch
Clock Mux 9 Divider Update Status Register 
(MUX_9_DIV_UPD_STAT)
32
R
0000_0000h
580h
Clock Mux 10 Select Control Register (MUX_10_CSC)
32
RW
0000_0000h
584h
Clock Mux 10 Select Status Register (MUX_10_CSS)
32
R
0008_0000h
588h
Clock Mux 10 Divider 0 Control Register (MUX_10_DC_0)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1022 / 5251


---
# 페이지 121

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
5BCh
Clock Mux 10 Divider Update Status Register 
(MUX_10_DIV_UPD_STAT)
32
R
0000_0000h
5C0h
Clock Mux 11 Select Control Register (MUX_11_CSC)
32
RW
0000_0000h
5C4h
Clock Mux 11 Select Status Register (MUX_11_CSS)
32
R
0002_0000h
5C8h
Clock Mux 11 Divider 0 Control Register (MUX_11_DC_0)
32
RW
8000_0000h
5FCh
Clock Mux 11 Divider Update Status Register 
(MUX_11_DIV_UPD_STAT)
32
R
0000_0000h
640h
Clock Mux 13 Select Control Register (MUX_13_CSC)
32
RW
0000_0000h
644h
Clock Mux 13 Select Status Register (MUX_13_CSS)
32
R
0008_0000h
648h
Clock Mux 13 Divider 0 Control Register (MUX_13_DC_0)
32
RW
0000_0000h
67Ch
Clock Mux 13 Divider Update Status Register 
(MUX_13_DIV_UPD_STAT)
32
R
0000_0000h
6C0h
Clock Mux 15 Select Control Register (MUX_15_CSC)
32
RW
0000_0000h
6C4h
Clock Mux 15 Select Status Register (MUX_15_CSS)
32
R
0008_0000h
6C8h
Clock Mux 15 Divider 0 Control Register (MUX_15_DC_0)
32
RW
0000_0000h
6FCh
Clock Mux 15 Divider Update Status Register 
(MUX_15_DIV_UPD_STAT)
32
R
0000_0000h
700h
Clock Mux 16 Select Control Register (MUX_16_CSC)
32
RW
0000_0000h
704h
Clock Mux 16 Select Status Register (MUX_16_CSS)
32
R
0008_0000h
708h
Clock Mux 16 Divider 0 Control Register (MUX_16_DC_0)
32
RW
0000_0000h
73Ch
Clock Mux 16 Divider Update Status Register 
(MUX_16_DIV_UPD_STAT)
32
R
0000_0000h
780h
Clock Mux 18 Select Control Register (MUX_18_CSC)
32
RW
0000_0000h
784h
Clock Mux 18 Select Status Register (MUX_18_CSS)
32
R
0008_0000h
788h
Clock Mux 18 Divider 0 Control Register (MUX_18_DC_0)
32
RW
0001_0000h
7BCh
Clock Mux 18 Divider Update Status Register 
(MUX_18_DIV_UPD_STAT)
32
R
0000_0000h
7C0h
Clock Mux 19 Select Control Register (MUX_19_CSC)
32
RW
0000_0000h
7C4h
Clock Mux 19 Select Status Register (MUX_19_CSS)
32
R
0008_0000h
7C8h
Clock Mux 19 Divider 0 Control Register (MUX_19_DC_0)
32
RW
0000_0000h
7FCh
Clock Mux 19 Divider Update Status Register 
(MUX_19_DIV_UPD_STAT)
32
R
0000_0000h
800h
Clock Mux 20 Select Control Register (MUX_20_CSC)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1023 / 5251


---
# 페이지 122

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
804h
Clock Mux 20 Select Status Register (MUX_20_CSS)
32
R
0008_0000h
808h
Clock Mux 20 Divider 0 Control Register (MUX_20_DC_0)
32
RW
0000_0000h
83Ch
Clock Mux 20 Divider Update Status Register 
(MUX_20_DIV_UPD_STAT)
32
R
0000_0000h
25.5.2 PCFS Step Duration (PCFS_SDUR)
Offset
Register
Offset
PCFS_SDUR
0h
Function
This register specifies the step duration of each PCFS step. The value provided in this register specifies the PCFS step duration 
in terms of the number of cycles of FIRC.
This register is reset only by a destructive reset. For details, see PCFS.
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
SDUR 
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
This field is reserved and reads return zeros.
15-0
SDUR
Step duration
Count value of the step duration
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1024 / 5251


---
# 페이지 123

25.5.3 PCFS Divider Change 8 Register (PCFS_DIVC8)
Offset
Register
Offset
PCFS_DIVC8
58h
Function
This register defines the rate of frequency change and initial change value on frequency ramp-up for the Progressive Clock 
Frequency switching of PLL_PHI0_CLK.
This register is reset only on destructive reset.
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
INIT 
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
RATE 
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
INIT
Divider change initial value
This field provides the initial change value of the clock divider for the clock ramp-up phase 
of PLL_PHI0_CLK.
15-8
—
This field is reserved and reads return zeros.
7-0
RATE
Divider change rate
This value controls the change value of the clock divider for the clock ramp-up and ramp-down phase of 
PLL_PHI0_CLK.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1025 / 5251


---
# 페이지 124

25.5.4 PCFS Divider End 8 Register (PCFS_DIVE8)
Offset
Register
Offset
PCFS_DIVE8
5Ch
Function
This register defines the final division value on frequency ramp-down for the progressive system clock switching 
of PLL_PHI0_CLK.
This registers is reset only on destructive reset.
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
DIVE 
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
DIVE 
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
1
1
1
0
0
1
1
1
Fields
Field
Function
31-20
—
This field is reserved and reads return zeros.
19-0
DIVE
Divider end value
This field provides the end value of the clock divider for the PLL_PHI0_CLK ramp-down phase.
25.5.5 PCFS Divider Start 8 Register (PCFS_DIVS8)
Offset
Register
Offset
PCFS_DIVS8
60h
Function
This register defines the initial division value on frequency ramp-up for the progressive system clock switching of PLL_PHI0_CLK.
This register is reset only on destructive reset.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1026 / 5251


---
# 페이지 125

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
DIVS 
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
DIVS 
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
1
1
1
0
0
1
1
1
Fields
Field
Function
31-20
—
This field is reserved and reads return zeros.
19-0
DIVS
Divider start value
This field provides the start value of the clock divider for the PLL_PHI0_CLK ramp-up phase
25.5.6 Clock Mux 0 Select Control Register (MUX_0_CSC)
Offset
Register
Offset
MUX_0_CSC
300h
Function
This register provides the clock source selection control for clock mux 0. Clock mux 0 implements hardware control clock switching 
ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" 
section for details.
This register is reset on destructive reset only.
An update to all the PCFS-related fields of this register must be an atomic write, which means a single write must update the 
CLK_SW, RAMPDOWN, and RAMPUP fields. It is necessary to set both RAMPUP and RAMPDOWN bits together even if you 
want to trigger either RAMPUP or RAMPDOWN process otherwise the desired PCFS sequence will not be executed.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1027 / 5251


---
# 페이지 126

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
SELCTL 
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
SAFE_
SW 
CLK_
SW 
RAMP
DOWN 
RAMP
UP 
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
This field is reserved and reads return zeros.
27-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 0. The reserved values are not displayed.
0000b - FIRC
1000b - PLL_PHI0_CLK
23-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
2
CLK_SW
Clock switch
Writing 1 to this bit makes a clock switch request to clock mux 0. After a clock switch operation is requested, 
this bit is auto cleared and a corresponding bit in the status register is set.
1
RAMPDOWN
PCFS ramp-down
Writing 1 to this bit makes a PCFS ramp-down request to clock mux 0. After a PCFS ramp-down operation 
is requested, this bit is auto cleared and a corresponding bit in the status register is set.
0
RAMPUP
PCFS ramp-up
Writing 1 to this bit makes a PCFS ramp-up request to clock mux 0. After a PCFS ramp-up operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1028 / 5251


---
# 페이지 127

25.5.7 Clock Mux 0 Select Status Register (MUX_0_CSS)
Offset
Register
Offset
MUX_0_CSS
304h
Function
This register provides the current clock source selection status for clock mux 0.
This register is reset on destructive reset only.
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
SELSTAT 
0
SWTRG 
SWIP 
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
SAFE_
SW 
CLK_
SW 
RAMP
DOWN 
RAMP
UP 
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
This field is reserved and reads return zeros.
27-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 0. The reserved values are not displayed.
0000b - FIRC
1000b - PLL_PHI0_CLK
23-20
—
This field is reserved and reads return zeros.
19-17
SWTRG
Switch trigger cause
This value indicates the cause for the latest clock source switch.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1029 / 5251


---
# 페이지 128

Table continued from the previous page...
Field
Function
 
If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware 
clock mux, the value of the SWTRG field can be either 4 or 5.
  NOTE  
000b - Reserved
001b - Switch after request succeeded.
010b - Switch after the request failed because of an inactive target clock and the current clock is 
FIRC.
011b - Switch after the request failed because of an inactive current clock and the current clock is 
FIRC.
100b - Switch to FIRC because of a safe clock request or reset succeeded.
101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous 
current clock source was inactive.
110b - Reserved
111b - Reserved
16
SWIP
Switch in progress
 
New clock switch request can only be given three clock cycles after the completion of the 
previous request.
  NOTE  
0b - Clock source switching is complete.
1b - Clock source switching is in progress.
15-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
This field provides an indication of whether a switch to safe clock operation was requested during the 
previous/ongoing request on clock mux 0.
0b - No safe clock switch operation was requested.
1b - Safe clock switch operation was requested.
2
CLK_SW
Clock switch
This field provides an indication of whether a clock switch operation was requested during the previous/
ongoing request on clock mux 0.
0b - No clock switch operation was requested.
1b - Clock switch operation was requested.
1
RAMPDOWN
PCFS ramp-down
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1030 / 5251


---
# 페이지 129

Table continued from the previous page...
Field
Function
This field provides an indication of whether a PCFS ramp-down operation was requested during the 
previous/ongoing request on clock mux 0.
 
In case of safe clock switching, the ramp-down operation runs internally, but the value of the 
corresponding status field is not set to 1.
  NOTE  
0b - No ramp-down operation was requested.
1b - Ramp-down operation was requested.
0
RAMPUP
PCFS ramp-up
This field provides an indication of whether a PCFS ramp-up operation was requested during the previous/
ongoing request on clock mux 0.
0b - No ramp-up operation was requested.
1b - Ramp-up operation was requested.
25.5.8 Clock Mux 0 Divider 0 Control Register (MUX_0_DC_0)
Offset
Register
Offset
MUX_0_DC_0
308h
Function
This register controls the clock divider 0 for clock mux 0. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1031 / 5251


---
# 페이지 130

Fields
Field
Function
31
DE
Divider enable
0b - Unused
1b - Divider is enabled.
30-19
—
This field is reserved and reads return zeros.
18-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.9 Clock Mux 0 Divider 1 Control Register (MUX_0_DC_1)
Offset
Register
Offset
MUX_0_DC_1
30Ch
Function
This register controls the clock divider 1 for clock mux 0. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1032 / 5251


---
# 페이지 131

Fields
Field
Function
31
DE
Divider enable
0b - Unused
1b - Divider is enabled.
30-19
—
This field is reserved and reads return zeros.
18-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.10 Clock Mux 0 Divider 2 Control Register (MUX_0_DC_2)
Offset
Register
Offset
MUX_0_DC_2
310h
Function
This register controls the clock divider 2 for clock mux 0. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1033 / 5251


---
# 페이지 132

Fields
Field
Function
31
DE
Divider enable
0b - Unused
1b - Divider is enabled.
30-20
—
This field is reserved and reads return zeros.
19-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.11 Clock Mux 0 Divider 3 Control Register (MUX_0_DC_3)
Offset
Register
Offset
MUX_0_DC_3
314h
Function
This register controls the clock divider 3 for clock mux 0. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1034 / 5251


---
# 페이지 133

Fields
Field
Function
31
DE
Divider enable
0b - Unused
1b - Divider is enabled.
30-19
—
This field is reserved and reads return zeros.
18-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.12 Clock Mux 0 Divider 4 Control Register (MUX_0_DC_4)
Offset
Register
Offset
MUX_0_DC_4
318h
Function
This register controls the clock divider 4 for clock mux 0. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1035 / 5251


---
# 페이지 134

Fields
Field
Function
31
DE
Divider enable
0b - Unused
1b - Divider is enabled.
30-19
—
This field is reserved and reads return zeros.
18-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.13 Clock Mux 0 Divider 5 Control Register (MUX_0_DC_5)
Offset
Register
Offset
MUX_0_DC_5
31Ch
Function
This register controls the clock divider 5 for clock mux 0. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1036 / 5251


---
# 페이지 135

Fields
Field
Function
31
DE
Divider enable
0b - Unused
1b - Divider is enabled.
30-19
—
This field is reserved and reads return zeros.
18-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-3
—
Reserved
2-0
—
Reserved
25.5.14 Clock Mux 0 Divider 6 Control Register (MUX_0_DC_6)
Offset
Register
Offset
MUX_0_DC_6
320h
Function
This register controls the clock divider 6 for clock mux 0. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
  NOTE  
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1037 / 5251


---
# 페이지 136

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
DE 
0
DIV 
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
DE
Divider enable
0b - Unused
1b - Divider is enabled.
30-19
—
This field is reserved and reads return zeros.
18-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.15 Clock Mux 0 Divider 7 Control Register (MUX_0_DC_7)
Offset
Register
Offset
MUX_0_DC_7
324h
Function
This register controls the clock divider 7 for clock mux 0. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
  NOTE  
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1038 / 5251


---
# 페이지 137

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
DE 
0
DIV 
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
DE
Divider enable
0b - Unused
1b - Divider is enabled.
30-18
—
This field is reserved and reads return zeros.
17-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.16 Clock Mux 0 Divider Trigger Control Register (MUX_0_DIV_TRIG_CTRL)
Offset
Register
Offset
MUX_0_DIV_TRIG_CTR
L
334h
Function
This register selects whether the dividers associated with clock mux 0 are updated immediately on writing to the corresponding 
divider configuration register (referred to as immediate divider update) or only on writing to the MC_CGM_MUX_0_DIV_TRIG 
register (referred to as common trigger update). When common trigger update is configured, this register also controls initiation 
of the halt handshake protocol with the on-chip AXBS. Software is required to configure HHEN field for handshaking with on-chip 
AXBS when the ratio of division value among the clock dividers need to be changed.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1039 / 5251


---
# 페이지 138

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
HHEN 
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
TCTL 
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
HHEN
Halt handshake enable
This field controls the initiation of the halt handshake protocol with AXBS when a common trigger divider 
update is initiated.
0b - No halt handshake protocol is initiated.
1b - Halt handshake protocol is initiated.
30-1
—
This field is reserved and reads return zeros.
0
TCTL
Trigger control
This field controls the divider update configuration between immediate and common update.
0b - Immediate divider update
1b - Common trigger divider update
25.5.17 Clock Mux 0 Divider Trigger Register (MUX_0_DIV_TRIG)
Offset
Register
Offset
MUX_0_DIV_TRIG
338h
Function
This register provides a common trigger for the clock dividers (only 50% duty cycle dividers) of clock mux 0. Writing any 
value to this register provides a trigger to the dividers. This register should only be written after appropriately configuring the 
MC_CGM_MUX_0_DIV_TRIG_CTRL register.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1040 / 5251


---
# 페이지 139

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
TRIGGER 
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
TRIGGER 
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
TRIGGER
Trigger for divider update
25.5.18 Clock Mux 0 Divider Update Status Register (MUX_0_DIV_UPD_STAT)
Offset
Register
Offset
MUX_0_DIV_UPD_STAT
33Ch
Function
This register provides the update status of the clock dividers corresponding to clock mux 0. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
  NOTE  
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1041 / 5251


---
# 페이지 140

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
DIV_
STAT 
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
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 0
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
25.5.19 Clock Mux 1 Select Control Register (MUX_1_CSC)
Offset
Register
Offset
MUX_1_CSC
340h
Function
This register provides the clock source selection control for clock mux 1. Clock mux 1 implements hardware control clock switching 
ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" 
section for details.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1042 / 5251


---
# 페이지 141

This register is reset on destructive reset only.
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
SELCTL 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 1. The reserved values are not displayed.
0_0000b - FIRC
0_0010b - FXOSC
1_0110b - AIPS_PLAT_CLK
23-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
2
CLK_SW
Clock switch
Writing 1 to this bit makes a clock switch request to clock mux 1. After a clock switch operation is requested, 
this bit is auto cleared and a corresponding bit in the status register is set.
1-0
—
This field is reserved and reads return zeros.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1043 / 5251


---
# 페이지 142

25.5.20 Clock Mux 1 Select Status Register (MUX_1_CSS)
Offset
Register
Offset
MUX_1_CSS
344h
Function
This register provides the current clock source selection status for clock mux 1.
This register is reset on destructive reset only.
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
SELSTAT 
0
SWTRG 
SWIP 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 1. The reserved values are not displayed.
0_0000b - FIRC
0_0010b - FXOSC
1_0110b - AIPS_PLAT_CLK
23-20
—
This field is reserved and reads return zeros.
19-17
SWTRG
Switch trigger cause
This value indicates the cause for the latest clock source switch.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1044 / 5251


---
# 페이지 143

Table continued from the previous page...
Field
Function
 
If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware 
clock mux, the value of the SWTRG field can be either 4 or 5.
  NOTE  
000b - Reserved
001b - Switch after request succeeded.
010b - Switch after the request failed because of an inactive target clock and the current clock is 
FIRC.
011b - Switch after the request failed because of an inactive current clock and the current clock is 
FIRC.
100b - Switch to FIRC because of a safe clock request or reset succeeded.
101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous 
current clock source was inactive.
110b - Reserved
111b - Reserved
16
SWIP
Switch in progress
 
New clock switch request can only be given three clock cycles after the completion of the 
previous request.
  NOTE  
0b - Clock source switching is complete.
1b - Clock source switching is in progress.
15-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
This field provides an indication of whether a switch to safe clock operation was requested during the 
previous/ongoing request on clock mux 1.
0b - No safe clock switch operation was requested.
1b - Safe clock switch operation was requested.
2
CLK_SW
Clock switch
This field provides an indication of whether a clock switch operation was requested during the previous/
ongoing request on clock mux 1.
0b - No clock switch operation was requested.
1b - Clock switch operation was requested.
1-0
—
This field is reserved and reads return zeros.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1045 / 5251


---
# 페이지 144

25.5.21 Clock Mux 1 Divider 0 Control Register (MUX_1_DC_0)
Offset
Register
Offset
MUX_1_DC_0
348h
Function
This register controls the clock divider 0 for clock mux 1. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
DE
Divider enable
0b - Divider is disabled.
1b - Divider is enabled.
30-17
—
This field is reserved and reads return zeros.
16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1046 / 5251


---
# 페이지 145

25.5.22 Clock Mux 1 Divider Update Status Register (MUX_1_DIV_UPD_STAT)
Offset
Register
Offset
MUX_1_DIV_UPD_STAT
37Ch
Function
This register provides the update status of the clock dividers corresponding to clock mux 1. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
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
DIV_
STAT 
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
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 1
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1047 / 5251


---
# 페이지 146

Table continued from the previous page...
Field
Function
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
25.5.23 Clock Mux 2 Select Control Register (MUX_2_CSC)
Offset
Register
Offset
MUX_2_CSC
380h
Function
This register provides the clock source selection control for clock mux 2. Clock mux 2 implements hardware control clock switching 
ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" 
section for details.
This register is reset on destructive reset only.
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
SELCTL 
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
SAFE_
SW 
CLK_
SW 
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
31-29
This field is reserved and reads return zeros.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1048 / 5251


---
# 페이지 147

Table continued from the previous page...
Field
Function
—
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 2. The reserved values are not displayed.
0_0000b - FIRC
0_0010b - FXOSC
1_0110b - AIPS_PLAT_CLK
23-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
2
CLK_SW
Clock switch
Writing 1 to this bit makes a clock switch request to clock mux 2. After a clock switch operation is requested, 
this bit is auto cleared and a corresponding bit in the status register is set.
1-0
—
This field is reserved and reads return zeros.
25.5.24 Clock Mux 2 Select Status Register (MUX_2_CSS)
Offset
Register
Offset
MUX_2_CSS
384h
Function
This register provides the current clock source selection status for clock mux 2.
This register is reset on destructive reset only.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1049 / 5251


---
# 페이지 148

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
SELSTAT 
0
SWTRG 
SWIP 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 2. The reserved values are not displayed.
0_0000b - FIRC
0_0010b - FXOSC
1_0110b - AIPS_PLAT_CLK
23-20
—
This field is reserved and reads return zeros.
19-17
SWTRG
Switch trigger cause
This value indicates the cause for the latest clock source switch.
 
If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware 
clock mux, the value of the SWTRG field can be either 4 or 5.
  NOTE  
000b - Reserved
001b - Switch after request succeeded.
010b - Switch after the request failed because of an inactive target clock and the current clock is 
FIRC.
011b - Switch after the request failed because of an inactive current clock and the current clock is 
FIRC.
100b - Switch to FIRC because of a safe clock request or reset succeeded.
101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous 
current clock source was inactive.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1050 / 5251


---
# 페이지 149

Table continued from the previous page...
Field
Function
110b - Reserved
111b - Reserved
16
SWIP
Switch in progress
 
New clock switch request can only be given three clock cycles after the completion of the 
previous request.
  NOTE  
0b - Clock source switching is complete.
1b - Clock source switching is in progress.
15-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
This field provides an indication of whether a switch to safe clock operation was requested during the 
previous/ongoing request on clock mux 2.
0b - No safe clock switch operation was requested.
1b - Safe clock switch operation was requested.
2
CLK_SW
Clock switch
This field provides an indication of whether a clock switch operation was requested during the previous/
ongoing request on clock mux 2.
0b - No clock switch operation was requested.
1b - Clock switch operation was requested.
1-0
—
This field is reserved and reads return zeros.
25.5.25 Clock Mux 2 Divider 0 Control Register (MUX_2_DC_0)
Offset
Register
Offset
MUX_2_DC_0
388h
Function
This register controls the clock divider 0 for clock mux 2. 
This divider is a 50% duty cycle divider.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1051 / 5251


---
# 페이지 150

 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
DE
Divider enable
0b - Divider is disabled.
1b - Divider is enabled.
30-17
—
This field is reserved and reads return zeros.
16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.26 Clock Mux 2 Divider Update Status Register (MUX_2_DIV_UPD_STAT)
Offset
Register
Offset
MUX_2_DIV_UPD_STAT
3BCh
Function
This register provides the update status of the clock dividers corresponding to clock mux 2. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1052 / 5251


---
# 페이지 151

clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
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
DIV_
STAT 
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
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 2
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1053 / 5251


---
# 페이지 152

25.5.27 Clock Mux 3 Select Control Register (MUX_3_CSC)
Offset
Register
Offset
MUX_3_CSC
3C0h
Function
This register provides the clock source selection control for clock mux 3. Clock mux 3 implements hardware control clock switching 
ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" 
section for details.
This register is reset on destructive reset only.
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
SELCTL 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 3. The reserved values are not displayed.
0_0000b - FIRC
0_0010b - FXOSC
1_0110b - AIPS_PLAT_CLK
23-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1054 / 5251


---
# 페이지 153

Table continued from the previous page...
Field
Function
Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
2
CLK_SW
Clock switch
Writing 1 to this bit makes a clock switch request to clock mux 3. After a clock switch operation is requested, 
this bit is auto cleared and a corresponding bit in the status register is set.
1-0
—
This field is reserved and reads return zeros.
25.5.28 Clock Mux 3 Select Status Register (MUX_3_CSS)
Offset
Register
Offset
MUX_3_CSS
3C4h
Function
This register provides the current clock source selection status for clock mux 3.
This register is reset on destructive reset only.
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
SELSTAT 
0
SWTRG 
SWIP 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1055 / 5251


---
# 페이지 154

Table continued from the previous page...
Field
Function
28-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 3. The reserved values are not displayed.
0_0000b - FIRC
0_0010b - FXOSC
1_0110b - AIPS_PLAT_CLK
23-20
—
This field is reserved and reads return zeros.
19-17
SWTRG
Switch trigger cause
This value indicates the cause for the latest clock source switch.
 
If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware 
clock mux, the value of the SWTRG field can be either 4 or 5.
  NOTE  
000b - Reserved
001b - Switch after request succeeded.
010b - Switch after the request failed because of an inactive target clock and the current clock is 
FIRC.
011b - Switch after the request failed because of an inactive current clock and the current clock is 
FIRC.
100b - Switch to FIRC because of a safe clock request or reset succeeded.
101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous 
current clock source was inactive.
110b - Reserved
111b - Reserved
16
SWIP
Switch in progress
 
New clock switch request can only be given three clock cycles after the completion of the 
previous request.
  NOTE  
0b - Clock source switching is complete.
1b - Clock source switching is in progress.
15-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1056 / 5251


---
# 페이지 155

Table continued from the previous page...
Field
Function
This field provides an indication of whether a switch to safe clock operation was requested during the 
previous/ongoing request on clock mux 3.
0b - No safe clock switch operation was requested.
1b - Safe clock switch operation was requested.
2
CLK_SW
Clock switch
This field provides an indication of whether a clock switch operation was requested during the previous/
ongoing request on clock mux 3.
0b - No clock switch operation was requested.
1b - Clock switch operation was requested.
1-0
—
This field is reserved and reads return zeros.
25.5.29 Clock Mux 3 Divider 0 Control Register (MUX_3_DC_0)
Offset
Register
Offset
MUX_3_DC_0
3C8h
Function
This register controls the clock divider 0 for clock mux 3. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1057 / 5251


---
# 페이지 156

Fields
Field
Function
31
DE
Divider enable
0b - Divider is disabled.
1b - Divider is enabled.
30-18
—
This field is reserved and reads return zeros.
17-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.30 Clock Mux 3 Divider Update Status Register (MUX_3_DIV_UPD_STAT)
Offset
Register
Offset
MUX_3_DIV_UPD_STAT
3FCh
Function
This register provides the update status of the clock dividers corresponding to clock mux 3. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
  NOTE  
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1058 / 5251


---
# 페이지 157

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
DIV_
STAT 
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
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 3
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
25.5.31 Clock Mux 4 Select Control Register (MUX_4_CSC)
Offset
Register
Offset
MUX_4_CSC
400h
Function
This register provides the clock source selection control for clock mux 4. Clock mux 4 implements hardware control clock switching 
ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" 
section for details.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1059 / 5251


---
# 페이지 158

This register is reset on destructive reset only.
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
SELCTL 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 4. The reserved values are not displayed.
0_0000b - FIRC
0_0010b - FXOSC
1_0110b - AIPS_PLAT_CLK
23-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
2
CLK_SW
Clock switch
Writing 1 to this bit makes a clock switch request to clock mux 4. After a clock switch operation is requested, 
this bit is auto cleared and a corresponding bit in the status register is set.
1-0
—
This field is reserved and reads return zeros.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1060 / 5251


---
# 페이지 159

25.5.32 Clock Mux 4 Select Status Register (MUX_4_CSS)
Offset
Register
Offset
MUX_4_CSS
404h
Function
This register provides the current clock source selection status for clock mux 4.
This register is reset on destructive reset only.
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
SELSTAT 
0
SWTRG 
SWIP 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 4. The reserved values are not displayed.
0_0000b - FIRC
0_0010b - FXOSC
1_0110b - AIPS_PLAT_CLK
23-20
—
This field is reserved and reads return zeros.
19-17
SWTRG
Switch trigger cause
This value indicates the cause for the latest clock source switch.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1061 / 5251


---
# 페이지 160

Table continued from the previous page...
Field
Function
 
If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware 
clock mux, the value of the SWTRG field can be either 4 or 5.
  NOTE  
000b - Reserved
001b - Switch after request succeeded.
010b - Switch after the request failed because of an inactive target clock and the current clock is 
FIRC.
011b - Switch after the request failed because of an inactive current clock and the current clock is 
FIRC.
100b - Switch to FIRC because of a safe clock request or reset succeeded.
101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous 
current clock source was inactive.
110b - Reserved
111b - Reserved
16
SWIP
Switch in progress
 
New clock switch request can only be given three clock cycles after the completion of the 
previous request.
  NOTE  
0b - Clock source switching is complete.
1b - Clock source switching is in progress.
15-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
This field provides an indication of whether a switch to safe clock operation was requested during the 
previous/ongoing request on clock mux 4.
0b - No safe clock switch operation was requested.
1b - Safe clock switch operation was requested.
2
CLK_SW
Clock switch
This field provides an indication of whether a clock switch operation was requested during the previous/
ongoing request on clock mux 4.
0b - No clock switch operation was requested.
1b - Clock switch operation was requested.
1-0
—
This field is reserved and reads return zeros.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1062 / 5251


---
# 페이지 161

25.5.33 Clock Mux 4 Divider 0 Control Register (MUX_4_DC_0)
Offset
Register
Offset
MUX_4_DC_0
408h
Function
This register controls the clock divider 0 for clock mux 4. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
DE
Divider enable
0b - Divider is disabled.
1b - Divider is enabled.
30-18
—
This field is reserved and reads return zeros.
17-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1063 / 5251


---
# 페이지 162

25.5.34 Clock Mux 4 Divider Update Status Register (MUX_4_DIV_UPD_STAT)
Offset
Register
Offset
MUX_4_DIV_UPD_STAT
43Ch
Function
This register provides the update status of the clock dividers corresponding to clock mux 4. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
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
DIV_
STAT 
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
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 4
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1064 / 5251


---
# 페이지 163

Table continued from the previous page...
Field
Function
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
25.5.35 Clock Mux 5 Select Control Register (MUX_5_CSC)
Offset
Register
Offset
MUX_5_CSC
440h
Function
This register provides the clock source selection control of clock mux 5. Clock mux 5 implements software control clock switching, 
and a graceful clock switch can be performed by executing a sequence of steps in software. See "Software-controlled clock 
multiplexer" section for details.
This register is reset on destructive reset only.
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
SELCTL 
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
FCG 
CG 
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
31-29
This field is reserved and reads return zeros.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1065 / 5251


---
# 페이지 164

Table continued from the previous page...
Field
Function
—
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 5. The reserved values are not displayed.
0_0000b - FIRC
0_0001b - SIRC
0_0010b - FXOSC
0_0100b - SXOSC
1_0111b - AIPS_SLOW_CLK
23-4
—
This field is reserved and reads return zeros.
3
FCG
Force clock gate
Writing 1 to this bit gates the clock at the output of clock mux 5 to logic-0 irrespective of the logic level of the 
currently selected clock. Clock gating using this bit should only be performed when it is insured that current 
clock source is inactive.
2
CG
Clock gate
Writing 1 to this bit gates the clock at the output of clock mux 5 to logic-0. Using this bit it is insured that no 
glitches are resulted when gating the clock.
1-0
—
This field is reserved and reads return zeros.
25.5.36 Clock Mux 5 Select Status Register (MUX_5_CSS)
Offset
Register
Offset
MUX_5_CSS
444h
Function
This register provides the current clock source selection status for clock mux 5.
This register is reset on destructive reset only.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1066 / 5251


---
# 페이지 165

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
SELSTAT 
0
0
CS 
GRIP 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 5. The reserved values are not displayed.
0_0000b - FIRC
0_0001b - SIRC
0_0010b - FXOSC
0_0100b - SXOSC
1_0111b - AIPS_SLOW_CLK
23-20
—
This field is reserved and reads return zeros.
19-18
—
This field is reserved and reads return zeros.
17
CS
Clock status
This field indicates state of the clock at the output of the clock mux.
0b - Clock is gated to logic-0 at output of clock mux
1b - Clock mux is transparent. Active clock pulses at input of clock mux results in same number of 
pulses at its output
16
GRIP
Gating request is in progress.
When a clock gate request is given this bit indicates if the clock gating at the output of mux has completed 
or not.
0b - Clock source gating or ungating has completed.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1067 / 5251


---
# 페이지 166

Table continued from the previous page...
Field
Function
1b - Clock source gating or ungating is in progress.
15-0
—
This field is reserved and reads return zeros.
25.5.37 Clock Mux 5 Divider 0 Control Register (MUX_5_DC_0)
Offset
Register
Offset
MUX_5_DC_0
448h
Function
This register controls the clock divider 0 for clock mux 5. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
  NOTE  
 
Software-controlled clock multiplexer dividers are not expected to return to the default state on the hardware 
transitions and handshakes occurring as part of the functional reset entry sequence (only hardware-controlled 
clock multiplexer dividers return to the default state).
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
DE 
0
DIV 
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
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1068 / 5251


---
# 페이지 167

Fields
Field
Function
31
DE
Divider enable
0b - Divider is disabled.
1b - Divider is enabled.
30-19
—
This field is reserved and reads return zeros.
18-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.38 Clock Mux 5 Divider Update Status Register (MUX_5_DIV_UPD_STAT)
Offset
Register
Offset
MUX_5_DIV_UPD_STAT
47Ch
Function
This register provides the update status of the clock dividers corresponding to clock mux 5. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
  NOTE  
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1069 / 5251


---
# 페이지 168

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
DIV_
STAT 
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
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 5
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
25.5.39 Clock Mux 6 Select Control Register (MUX_6_CSC)
Offset
Register
Offset
MUX_6_CSC
480h
Function
This register provides the clock source selection control of clock mux 6. Clock mux 6 implements software control clock switching, 
and a graceful clock switch can be performed by executing a sequence of steps in software. See "Software-controlled clock 
multiplexer" section for details.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1070 / 5251


---
# 페이지 169

This register is reset on destructive reset only.
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
SELCTL 
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
FCG 
CG 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 6. The reserved values are not displayed.
0_0000b - FIRC
0_0001b - SIRC
0_0010b - FXOSC
0_0100b - SXOSC
0_1000b - PLL_PHI0_CLK
0_1001b - PLL_PHI1_CLK
0_1100b - PLL_AUX_PHI0_CLK
0_1101b - PLL_AUX_PHI1_CLK
1_0000b - CORE_CLK
1_0011b - HSE_CLK
1_0110b - AIPS_PLAT_CLK
1_0111b - AIPS_SLOW_CLK
1_1000b - GMAC0_MII_RMII_RGMII_TX_CLK
1_1001b - GMAC0_MII_RGMII_RX_CLK
23-4
—
This field is reserved and reads return zeros.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1071 / 5251


---
# 페이지 170

Table continued from the previous page...
Field
Function
3
FCG
Force clock gate
Writing 1 to this bit gates the clock at the output of clock mux 6 to logic-0 irrespective of the logic level of the 
currently selected clock. Clock gating using this bit should only be performed when it is insured that current 
clock source is inactive.
2
CG
Clock gate
Writing 1 to this bit gates the clock at the output of clock mux 6 to logic-0. Using this bit it is insured that no 
glitches are resulted when gating the clock.
1-0
—
This field is reserved and reads return zeros.
25.5.40 Clock Mux 6 Select Status Register (MUX_6_CSS)
Offset
Register
Offset
MUX_6_CSS
484h
Function
This register provides the current clock source selection status for clock mux 6.
This register is reset on destructive reset only.
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
SELSTAT 
0
0
CS 
GRIP 
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
31-29
This field is reserved and reads return zeros.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1072 / 5251


---
# 페이지 171

Table continued from the previous page...
Field
Function
—
28-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 6. The reserved values are not displayed.
0_0000b - FIRC
0_0001b - SIRC
0_0010b - FXOSC
0_0100b - SXOSC
0_1000b - PLL_PHI0_CLK
0_1001b - PLL_PHI1_CLK
0_1100b - PLL_AUX_PHI0_CLK
0_1101b - PLL_AUX_PHI1_CLK
1_0000b - CORE_CLK
1_0011b - HSE_CLK
1_0110b - AIPS_PLAT_CLK
1_0111b - AIPS_SLOW_CLK
1_1000b - GMAC0_MII_RMII_RGMII_TX_CLK
1_1001b - GMAC0_MII_RGMII_RX_CLK
23-20
—
This field is reserved and reads return zeros.
19-18
—
This field is reserved and reads return zeros.
17
CS
Clock status
This field indicates state of the clock at the output of the clock mux.
0b - Clock is gated to logic-0 at output of clock mux
1b - Clock mux is transparent. Active clock pulses at input of clock mux results in same number of 
pulses at its output
16
GRIP
Gating request is in progress.
When a clock gate request is given this bit indicates if the clock gating at the output of mux has completed 
or not.
0b - Clock source gating or ungating has completed.
1b - Clock source gating or ungating is in progress.
15-0
This field is reserved and reads return zeros.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1073 / 5251


---
# 페이지 172

Table continued from the previous page...
Field
Function
—
25.5.41 Clock Mux 6 Divider 0 Control Register (MUX_6_DC_0)
Offset
Register
Offset
MUX_6_DC_0
488h
Function
This register controls the clock divider 0 for clock mux 6. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
  NOTE  
 
Software-controlled clock multiplexer dividers are not expected to return to the default state on the hardware 
transitions and handshakes occurring as part of the functional reset entry sequence (only hardware-controlled 
clock multiplexer dividers return to the default state).
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
DE 
0
DIV 
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
DE
Divider enable
0b - Divider is disabled.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1074 / 5251


---
# 페이지 173

Table continued from the previous page...
Field
Function
1b - Divider is enabled.
30-22
—
This field is reserved and reads return zeros.
21-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.42 Clock Mux 6 Divider Update Status Register (MUX_6_DIV_UPD_STAT)
Offset
Register
Offset
MUX_6_DIV_UPD_STAT
4BCh
Function
This register provides the update status of the clock dividers corresponding to clock mux 6. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
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
DIV_
STAT 
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
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1075 / 5251


---
# 페이지 174

Fields
Field
Function
31-1
—
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 6
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
25.5.43 Clock Mux 7 Select Control Register (MUX_7_CSC)
Offset
Register
Offset
MUX_7_CSC
4C0h
Function
This register provides the clock source selection control for clock mux 7. Clock mux 7 implements hardware control clock switching 
ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" 
section for details.
This register is reset on destructive reset only.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1076 / 5251


---
# 페이지 175

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
SELCTL 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 7. The reserved values are not displayed.
0_0000b - FIRC
1_1000b - GMAC0_MII_RMII_RGMII_TX_CLK
23-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
2
CLK_SW
Clock switch
Writing 1 to this bit makes a clock switch request to clock mux 7. After a clock switch operation is requested, 
this bit is auto cleared and a corresponding bit in the status register is set.
1-0
—
This field is reserved and reads return zeros.
25.5.44 Clock Mux 7 Select Status Register (MUX_7_CSS)
Offset
Register
Offset
MUX_7_CSS
4C4h
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1077 / 5251


---
# 페이지 176

Function
This register provides the current clock source selection status for clock mux 7.
This register is reset on destructive reset only.
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
SELSTAT 
0
SWTRG 
SWIP 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 7. The reserved values are not displayed.
0_0000b - FIRC
1_1000b - GMAC0_MII_RMII_RGMII_TX_CLK
23-20
—
This field is reserved and reads return zeros.
19-17
SWTRG
Switch trigger cause
This value indicates the cause for the latest clock source switch.
 
If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware 
clock mux, the value of the SWTRG field can be either 4 or 5.
  NOTE  
000b - Reserved
001b - Switch after request succeeded.
010b - Switch after the request failed because of an inactive target clock and the current clock is 
FIRC.
011b - Switch after the request failed because of an inactive current clock and the current clock is 
FIRC.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1078 / 5251


---
# 페이지 177

Table continued from the previous page...
Field
Function
100b - Switch to FIRC because of a safe clock request or reset succeeded.
101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous 
current clock source was inactive.
110b - Reserved
111b - Reserved
16
SWIP
Switch in progress
 
New clock switch request can only be given three clock cycles after the completion of the 
previous request.
  NOTE  
0b - Clock source switching is complete.
1b - Clock source switching is in progress.
15-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
This field provides an indication of whether a switch to safe clock operation was requested during the 
previous/ongoing request on clock mux 7.
0b - No safe clock switch operation was requested.
1b - Safe clock switch operation was requested.
2
CLK_SW
Clock switch
This field provides an indication of whether a clock switch operation was requested during the previous/
ongoing request on clock mux 7.
0b - No clock switch operation was requested.
1b - Clock switch operation was requested.
1-0
—
This field is reserved and reads return zeros.
25.5.45 Clock Mux 7 Divider 0 Control Register (MUX_7_DC_0)
Offset
Register
Offset
MUX_7_DC_0
4C8h
Function
This register controls the clock divider 0 for clock mux 7. 
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1079 / 5251


---
# 페이지 178

This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
DE
Divider enable
0b - Divider is disabled.
1b - Divider is enabled.
30-22
—
This field is reserved and reads return zeros.
21-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.46 Clock Mux 7 Divider Update Status Register (MUX_7_DIV_UPD_STAT)
Offset
Register
Offset
MUX_7_DIV_UPD_STAT
4FCh
Function
This register provides the update status of the clock dividers corresponding to clock mux 7. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1080 / 5251


---
# 페이지 179

divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
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
DIV_
STAT 
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
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 7
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1081 / 5251


---
# 페이지 180

25.5.47 Clock Mux 8 Select Control Register (MUX_8_CSC)
Offset
Register
Offset
MUX_8_CSC
500h
Function
This register provides the clock source selection control for clock mux 8. Clock mux 8 implements hardware control clock switching 
ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" 
section for details.
This register is reset on destructive reset only.
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
SELCTL 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 8. The reserved values are not displayed.
0_0000b - FIRC
0_1100b - PLL_AUX_PHI0_CLK
1_1000b - GMAC0_MII_RMII_RGMII_TX_CLK
23-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1082 / 5251


---
# 페이지 181

Table continued from the previous page...
Field
Function
Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
2
CLK_SW
Clock switch
Writing 1 to this bit makes a clock switch request to clock mux 8. After a clock switch operation is requested, 
this bit is auto cleared and a corresponding bit in the status register is set.
1-0
—
This field is reserved and reads return zeros.
25.5.48 Clock Mux 8 Select Status Register (MUX_8_CSS)
Offset
Register
Offset
MUX_8_CSS
504h
Function
This register provides the current clock source selection status for clock mux 8.
This register is reset on destructive reset only.
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
SELSTAT 
0
SWTRG 
SWIP 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1083 / 5251


---
# 페이지 182

Table continued from the previous page...
Field
Function
28-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 8. The reserved values are not displayed.
0_0000b - FIRC
0_1100b - PLL_AUX_PHI0_CLK
1_1000b - GMAC0_MII_RMII_RGMII_TX_CLK
23-20
—
This field is reserved and reads return zeros.
19-17
SWTRG
Switch trigger cause
This value indicates the cause for the latest clock source switch.
 
If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware 
clock mux, the value of the SWTRG field can be either 4 or 5.
  NOTE  
000b - Reserved
001b - Switch after request succeeded.
010b - Switch after the request failed because of an inactive target clock and the current clock is 
FIRC.
011b - Switch after the request failed because of an inactive current clock and the current clock is 
FIRC.
100b - Switch to FIRC because of a safe clock request or reset succeeded.
101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous 
current clock source was inactive.
110b - Reserved
111b - Reserved
16
SWIP
Switch in progress
 
New clock switch request can only be given three clock cycles after the completion of the 
previous request.
  NOTE  
0b - Clock source switching is complete.
1b - Clock source switching is in progress.
15-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1084 / 5251


---
# 페이지 183

Table continued from the previous page...
Field
Function
This field provides an indication of whether a switch to safe clock operation was requested during the 
previous/ongoing request on clock mux 8.
0b - No safe clock switch operation was requested.
1b - Safe clock switch operation was requested.
2
CLK_SW
Clock switch
This field provides an indication of whether a clock switch operation was requested during the previous/
ongoing request on clock mux 8.
0b - No clock switch operation was requested.
1b - Clock switch operation was requested.
1-0
—
This field is reserved and reads return zeros.
25.5.49 Clock Mux 8 Divider 0 Control Register (MUX_8_DC_0)
Offset
Register
Offset
MUX_8_DC_0
508h
Function
This register controls the clock divider 0 for clock mux 8. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1085 / 5251


---
# 페이지 184

Fields
Field
Function
31
DE
Divider enable
0b - Divider is disabled.
1b - Divider is enabled.
30-22
—
This field is reserved and reads return zeros.
21-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.50 Clock Mux 8 Divider Update Status Register (MUX_8_DIV_UPD_STAT)
Offset
Register
Offset
MUX_8_DIV_UPD_STAT
53Ch
Function
This register provides the update status of the clock dividers corresponding to clock mux 8. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
  NOTE  
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1086 / 5251


---
# 페이지 185

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
DIV_
STAT 
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
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 8
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
25.5.51 Clock Mux 9 Select Control Register (MUX_9_CSC)
Offset
Register
Offset
MUX_9_CSC
540h
Function
This register provides the clock source selection control for clock mux 9. Clock mux 9 implements hardware control clock switching 
ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock multiplexer" 
section for details.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1087 / 5251


---
# 페이지 186

This register is reset on destructive reset only.
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
SELCTL 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 9. The reserved values are not displayed.
0_0000b - FIRC
0_0010b - FXOSC
0_1100b - PLL_AUX_PHI0_CLK
1_1000b - GMAC0_MII_RMII_RGMII_TX_CLK
1_1001b - GMAC0_MII_RGMII_RX_CLK
1_1101b - GMAC1_MII_RGMII_RX_CLK
1_1110b - GMAC1_MII_RMII_RGMII_TX_CLK
23-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
2
CLK_SW
Clock switch
Writing 1 to this bit makes a clock switch request to clock mux 9. After a clock switch operation is requested, 
this bit is auto cleared and a corresponding bit in the status register is set.
1-0
—
This field is reserved and reads return zeros.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1088 / 5251


---
# 페이지 187

25.5.52 Clock Mux 9 Select Status Register (MUX_9_CSS)
Offset
Register
Offset
MUX_9_CSS
544h
Function
This register provides the current clock source selection status for clock mux 9.
This register is reset on destructive reset only.
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
SELSTAT 
0
SWTRG 
SWIP 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 9. The reserved values are not displayed.
0_0000b - FIRC
0_0010b - FXOSC
0_1100b - PLL_AUX_PHI0_CLK
1_1000b - GMAC0_MII_RMII_RGMII_TX_CLK
1_1001b - GMAC0_MII_RGMII_RX_CLK
1_1101b - GMAC1_MII_RGMII_RX_CLK
1_1110b - GMAC1_MII_RMII_RGMII_TX_CLK
23-20
This field is reserved and reads return zeros.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1089 / 5251


---
# 페이지 188

Table continued from the previous page...
Field
Function
—
19-17
SWTRG
Switch trigger cause
This value indicates the cause for the latest clock source switch.
 
If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware 
clock mux, the value of the SWTRG field can be either 4 or 5.
  NOTE  
000b - Reserved
001b - Switch after request succeeded.
010b - Switch after the request failed because of an inactive target clock and the current clock is 
FIRC.
011b - Switch after the request failed because of an inactive current clock and the current clock is 
FIRC.
100b - Switch to FIRC because of a safe clock request or reset succeeded.
101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous 
current clock source was inactive.
110b - Reserved
111b - Reserved
16
SWIP
Switch in progress
 
New clock switch request can only be given three clock cycles after the completion of the 
previous request.
  NOTE  
0b - Clock source switching is complete.
1b - Clock source switching is in progress.
15-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
This field provides an indication of whether a switch to safe clock operation was requested during the 
previous/ongoing request on clock mux 9.
0b - No safe clock switch operation was requested.
1b - Safe clock switch operation was requested.
2
CLK_SW
Clock switch
This field provides an indication of whether a clock switch operation was requested during the previous/
ongoing request on clock mux 9.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1090 / 5251


---
# 페이지 189

Table continued from the previous page...
Field
Function
0b - No clock switch operation was requested.
1b - Clock switch operation was requested.
1-0
—
This field is reserved and reads return zeros.
25.5.53 Clock Mux 9 Divider 0 Control Register (MUX_9_DC_0)
Offset
Register
Offset
MUX_9_DC_0
548h
Function
This register controls the clock divider 0 for clock mux 9. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
DE
Divider enable
0b - Divider is disabled.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1091 / 5251


---
# 페이지 190

Table continued from the previous page...
Field
Function
1b - Divider is enabled.
30-22
—
This field is reserved and reads return zeros.
21-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.54 Clock Mux 9 Divider Update Status Register (MUX_9_DIV_UPD_STAT)
Offset
Register
Offset
MUX_9_DIV_UPD_STAT
57Ch
Function
This register provides the update status of the clock dividers corresponding to clock mux 9. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
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
DIV_
STAT 
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
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1092 / 5251


---
# 페이지 191

Fields
Field
Function
31-1
—
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 9
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
25.5.55 Clock Mux 10 Select Control Register (MUX_10_CSC)
Offset
Register
Offset
MUX_10_CSC
580h
Function
This register provides the clock source selection control for clock mux 10. Clock mux 10 implements hardware control clock 
switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock 
multiplexer" section for details.
This register is reset on destructive reset only.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1093 / 5251


---
# 페이지 192

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
SELCTL 
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
SAFE_
SW 
CLK_
SW 
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
This field is reserved and reads return zeros.
27-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 10. The reserved values are not displayed.
0000b - FIRC
0010b - FXOSC
1001b - PLL_PHI1_CLK
1100b - PLL_AUX_PHI0_CLK
23-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
2
CLK_SW
Clock switch
Writing 1 to this bit makes a clock switch request to clock mux 10. After a clock switch operation is requested, 
this bit is auto cleared and a corresponding bit in the status register is set.
1-0
—
This field is reserved and reads return zeros.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1094 / 5251


---
# 페이지 193

25.5.56 Clock Mux 10 Select Status Register (MUX_10_CSS)
Offset
Register
Offset
MUX_10_CSS
584h
Function
This register provides the current clock source selection status for clock mux 10.
This register is reset on destructive reset only.
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
SELSTAT 
0
SWTRG 
SWIP 
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
SAFE_
SW 
CLK_
SW 
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
This field is reserved and reads return zeros.
27-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 10. The reserved values are not 
displayed.
0000b - FIRC
0010b - FXOSC
1001b - PLL_PHI1_CLK
1100b - PLL_AUX_PHI0_CLK
23-20
—
This field is reserved and reads return zeros.
19-17
Switch trigger cause
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1095 / 5251


---
# 페이지 194

Table continued from the previous page...
Field
Function
SWTRG
This value indicates the cause for the latest clock source switch.
 
If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware 
clock mux, the value of the SWTRG field can be either 4 or 5.
  NOTE  
000b - Reserved
001b - Switch after request succeeded.
010b - Switch after the request failed because of an inactive target clock and the current clock is 
FIRC.
011b - Switch after the request failed because of an inactive current clock and the current clock is 
FIRC.
100b - Switch to FIRC because of a safe clock request or reset succeeded.
101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous 
current clock source was inactive.
110b - Reserved
111b - Reserved
16
SWIP
Switch in progress
 
New clock switch request can only be given three clock cycles after the completion of the 
previous request.
  NOTE  
0b - Clock source switching is complete.
1b - Clock source switching is in progress.
15-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
This field provides an indication of whether a switch to safe clock operation was requested during the 
previous/ongoing request on clock mux 10.
0b - No safe clock switch operation was requested.
1b - Safe clock switch operation was requested.
2
CLK_SW
Clock switch
This field provides an indication of whether a clock switch operation was requested during the previous/
ongoing request on clock mux 10.
0b - No clock switch operation was requested.
1b - Clock switch operation was requested.
1-0
This field is reserved and reads return zeros.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1096 / 5251


---
# 페이지 195

Table continued from the previous page...
Field
Function
—
25.5.57 Clock Mux 10 Divider 0 Control Register (MUX_10_DC_0)
Offset
Register
Offset
MUX_10_DC_0
588h
Function
This register controls the clock divider 0 for clock mux 10. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
DE
Divider enable
0b - Divider is disabled.
1b - Divider is enabled.
30-19
—
This field is reserved and reads return zeros.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1097 / 5251


---
# 페이지 196

Table continued from the previous page...
Field
Function
18-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.58 Clock Mux 10 Divider Update Status Register (MUX_10_DIV_UPD_STAT)
Offset
Register
Offset
MUX_10_DIV_UPD_STA
T
5BCh
Function
This register provides the update status of the clock dividers corresponding to clock mux 10. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
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
DIV_
STAT 
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
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1098 / 5251


---
# 페이지 197

Fields
Field
Function
31-1
—
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 10
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
25.5.59 Clock Mux 11 Select Control Register (MUX_11_CSC)
Offset
Register
Offset
MUX_11_CSC
5C0h
Function
This register provides the clock source selection control of clock mux 11. Clock mux 11 implements software control clock 
switching, and a graceful clock switch can be performed by executing a sequence of steps in software. See "Software-controlled 
clock multiplexer" section for details.
This register is reset on destructive reset only.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1099 / 5251


---
# 페이지 198

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
SELCTL 
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
FCG 
CG 
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
This field is reserved and reads return zeros.
27-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 11. The reserved values are not displayed.
0000b - FIRC
0010b - FXOSC
1001b - PLL_PHI1_CLK
1100b - PLL_AUX_PHI0_CLK
23-4
—
This field is reserved and reads return zeros.
3
FCG
Force clock gate
Writing 1 to this bit gates the clock at the output of clock mux 11 to logic-0 irrespective of the logic level of the 
currently selected clock. Clock gating using this bit should only be performed when it is insured that current 
clock source is inactive.
2
CG
Clock gate
Writing 1 to this bit gates the clock at the output of clock mux 11 to logic-0. Using this bit it is insured that no 
glitches are resulted when gating the clock.
1-0
—
This field is reserved and reads return zeros.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1100 / 5251


---
# 페이지 199

25.5.60 Clock Mux 11 Select Status Register (MUX_11_CSS)
Offset
Register
Offset
MUX_11_CSS
5C4h
Function
This register provides the current clock source selection status for clock mux 11.
This register is reset on destructive reset only.
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
SELSTAT 
0
0
CS 
GRIP 
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
31-28
—
This field is reserved and reads return zeros.
27-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 11. The reserved values are not 
displayed.
0000b - FIRC
0010b - FXOSC
1001b - PLL_PHI1_CLK
1100b - PLL_AUX_PHI0_CLK
23-20
—
This field is reserved and reads return zeros.
19-18
—
This field is reserved and reads return zeros.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1101 / 5251


---
# 페이지 200

Table continued from the previous page...
Field
Function
17
CS
Clock status
This field indicates state of the clock at the output of the clock mux.
0b - Clock is gated to logic-0 at output of clock mux
1b - Clock mux is transparent. Active clock pulses at input of clock mux results in same number of 
pulses at its output
16
GRIP
Gating request is in progress.
When a clock gate request is given this bit indicates if the clock gating at the output of mux has completed 
or not.
0b - Clock source gating or ungating has completed.
1b - Clock source gating or ungating is in progress.
15-0
—
This field is reserved and reads return zeros.
25.5.61 Clock Mux 11 Divider 0 Control Register (MUX_11_DC_0)
Offset
Register
Offset
MUX_11_DC_0
5C8h
Function
This register controls the clock divider 0 for clock mux 11. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
  NOTE  
 
Software-controlled clock multiplexer dividers are not expected to return to the default state on the hardware 
transitions and handshakes occurring as part of the functional reset entry sequence (only hardware-controlled 
clock multiplexer dividers return to the default state).
  NOTE  
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1102 / 5251


---
# 페이지 201

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
DE 
0
DIV 
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
DE
Divider enable
0b - Divider is disabled.
1b - Divider is enabled.
30-20
—
This field is reserved and reads return zeros.
19-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.62 Clock Mux 11 Divider Update Status Register (MUX_11_DIV_UPD_STAT)
Offset
Register
Offset
MUX_11_DIV_UPD_STA
T
5FCh
Function
This register provides the update status of the clock dividers corresponding to clock mux 11. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1103 / 5251


---
# 페이지 202

 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
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
DIV_
STAT 
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
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 11
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
25.5.63 Clock Mux 13 Select Control Register (MUX_13_CSC)
Offset
Register
Offset
MUX_13_CSC
640h
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1104 / 5251


---
# 페이지 203

Function
This register provides the clock source selection control for clock mux 13. Clock mux 13 implements hardware control clock 
switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock 
multiplexer" section for details.
This register is reset on destructive reset only.
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
SELCTL 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 13. The reserved values are not displayed.
0_0000b - FIRC
0_0010b - FXOSC
1_0110b - AIPS_PLAT_CLK
23-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
2
CLK_SW
Clock switch
Writing 1 to this bit makes a clock switch request to clock mux 13. After a clock switch operation is requested, 
this bit is auto cleared and a corresponding bit in the status register is set.
1-0
—
This field is reserved and reads return zeros.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1105 / 5251


---
# 페이지 204

25.5.64 Clock Mux 13 Select Status Register (MUX_13_CSS)
Offset
Register
Offset
MUX_13_CSS
644h
Function
This register provides the current clock source selection status for clock mux 13.
This register is reset on destructive reset only.
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
SELSTAT 
0
SWTRG 
SWIP 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 13. The reserved values are not 
displayed.
0_0000b - FIRC
0_0010b - FXOSC
1_0110b - AIPS_PLAT_CLK
23-20
—
This field is reserved and reads return zeros.
19-17
SWTRG
Switch trigger cause
This value indicates the cause for the latest clock source switch.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1106 / 5251


---
# 페이지 205

Table continued from the previous page...
Field
Function
 
If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware 
clock mux, the value of the SWTRG field can be either 4 or 5.
  NOTE  
000b - Reserved
001b - Switch after request succeeded.
010b - Switch after the request failed because of an inactive target clock and the current clock is 
FIRC.
011b - Switch after the request failed because of an inactive current clock and the current clock is 
FIRC.
100b - Switch to FIRC because of a safe clock request or reset succeeded.
101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous 
current clock source was inactive.
110b - Reserved
111b - Reserved
16
SWIP
Switch in progress
 
New clock switch request can only be given three clock cycles after the completion of the 
previous request.
  NOTE  
0b - Clock source switching is complete.
1b - Clock source switching is in progress.
15-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
This field provides an indication of whether a switch to safe clock operation was requested during the 
previous/ongoing request on clock mux 13.
0b - No safe clock switch operation was requested.
1b - Safe clock switch operation was requested.
2
CLK_SW
Clock switch
This field provides an indication of whether a clock switch operation was requested during the previous/
ongoing request on clock mux 13.
0b - No clock switch operation was requested.
1b - Clock switch operation was requested.
1-0
—
This field is reserved and reads return zeros.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1107 / 5251


---
# 페이지 206

25.5.65 Clock Mux 13 Divider 0 Control Register (MUX_13_DC_0)
Offset
Register
Offset
MUX_13_DC_0
648h
Function
This register controls the clock divider 0 for clock mux 13. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
DE
Divider enable
0b - Divider is disabled.
1b - Divider is enabled.
30-17
—
This field is reserved and reads return zeros.
16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1108 / 5251


---
# 페이지 207

25.5.66 Clock Mux 13 Divider Update Status Register (MUX_13_DIV_UPD_STAT)
Offset
Register
Offset
MUX_13_DIV_UPD_STA
T
67Ch
Function
This register provides the update status of the clock dividers corresponding to clock mux 13. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
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
DIV_
STAT 
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
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 13
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1109 / 5251


---
# 페이지 208

Table continued from the previous page...
Field
Function
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
25.5.67 Clock Mux 15 Select Control Register (MUX_15_CSC)
Offset
Register
Offset
MUX_15_CSC
6C0h
Function
This register provides the clock source selection control for clock mux 15. Clock mux 15 implements hardware control clock 
switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock 
multiplexer" section for details.
This register is reset on destructive reset only.
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
SELCTL 
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
SAFE_
SW 
CLK_
SW 
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
31-29
This field is reserved and reads return zeros.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1110 / 5251


---
# 페이지 209

Table continued from the previous page...
Field
Function
—
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 15. The reserved values are not displayed.
0_0000b - FIRC
1_1110b - GMAC1_MII_RMII_RGMII_TX_CLK
23-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
2
CLK_SW
Clock switch
Writing 1 to this bit makes a clock switch request to clock mux 15. After a clock switch operation is requested, 
this bit is auto cleared and a corresponding bit in the status register is set.
1-0
—
This field is reserved and reads return zeros.
25.5.68 Clock Mux 15 Select Status Register (MUX_15_CSS)
Offset
Register
Offset
MUX_15_CSS
6C4h
Function
This register provides the current clock source selection status for clock mux 15.
This register is reset on destructive reset only.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1111 / 5251


---
# 페이지 210

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
SELSTAT 
0
SWTRG 
SWIP 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 15. The reserved values are not 
displayed.
0_0000b - FIRC
1_1110b - GMAC1_MII_RMII_RGMII_TX_CLK
23-20
—
This field is reserved and reads return zeros.
19-17
SWTRG
Switch trigger cause
This value indicates the cause for the latest clock source switch.
 
If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware 
clock mux, the value of the SWTRG field can be either 4 or 5.
  NOTE  
000b - Reserved
001b - Switch after request succeeded.
010b - Switch after the request failed because of an inactive target clock and the current clock is 
FIRC.
011b - Switch after the request failed because of an inactive current clock and the current clock is 
FIRC.
100b - Switch to FIRC because of a safe clock request or reset succeeded.
101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous 
current clock source was inactive.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1112 / 5251


---
# 페이지 211

Table continued from the previous page...
Field
Function
110b - Reserved
111b - Reserved
16
SWIP
Switch in progress
 
New clock switch request can only be given three clock cycles after the completion of the 
previous request.
  NOTE  
0b - Clock source switching is complete.
1b - Clock source switching is in progress.
15-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
This field provides an indication of whether a switch to safe clock operation was requested during the 
previous/ongoing request on clock mux 15.
0b - No safe clock switch operation was requested.
1b - Safe clock switch operation was requested.
2
CLK_SW
Clock switch
This field provides an indication of whether a clock switch operation was requested during the previous/
ongoing request on clock mux 15.
0b - No clock switch operation was requested.
1b - Clock switch operation was requested.
1-0
—
This field is reserved and reads return zeros.
25.5.69 Clock Mux 15 Divider 0 Control Register (MUX_15_DC_0)
Offset
Register
Offset
MUX_15_DC_0
6C8h
Function
This register controls the clock divider 0 for clock mux 15. 
This divider is a 50% duty cycle divider.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1113 / 5251


---
# 페이지 212

 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
DE
Divider enable
0b - Divider is disabled.
1b - Divider is enabled.
30-22
—
This field is reserved and reads return zeros.
21-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.70 Clock Mux 15 Divider Update Status Register (MUX_15_DIV_UPD_STAT)
Offset
Register
Offset
MUX_15_DIV_UPD_STA
T
6FCh
Function
This register provides the update status of the clock dividers corresponding to clock mux 15. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1114 / 5251


---
# 페이지 213

clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
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
DIV_
STAT 
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
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 15
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1115 / 5251


---
# 페이지 214

25.5.71 Clock Mux 16 Select Control Register (MUX_16_CSC)
Offset
Register
Offset
MUX_16_CSC
700h
Function
This register provides the clock source selection control for clock mux 16. Clock mux 16 implements hardware control clock 
switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock 
multiplexer" section for details.
This register is reset on destructive reset only.
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
SELCTL 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 16. The reserved values are not displayed.
0_0000b - FIRC
0_1100b - PLL_AUX_PHI0_CLK
1_1110b - GMAC1_MII_RMII_RGMII_TX_CLK
23-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1116 / 5251


---
# 페이지 215

Table continued from the previous page...
Field
Function
Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
2
CLK_SW
Clock switch
Writing 1 to this bit makes a clock switch request to clock mux 16. After a clock switch operation is requested, 
this bit is auto cleared and a corresponding bit in the status register is set.
1-0
—
This field is reserved and reads return zeros.
25.5.72 Clock Mux 16 Select Status Register (MUX_16_CSS)
Offset
Register
Offset
MUX_16_CSS
704h
Function
This register provides the current clock source selection status for clock mux 16.
This register is reset on destructive reset only.
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
SELSTAT 
0
SWTRG 
SWIP 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1117 / 5251


---
# 페이지 216

Table continued from the previous page...
Field
Function
28-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 16. The reserved values are not 
displayed.
0_0000b - FIRC
0_1100b - PLL_AUX_PHI0_CLK
1_1110b - GMAC1_MII_RMII_RGMII_TX_CLK
23-20
—
This field is reserved and reads return zeros.
19-17
SWTRG
Switch trigger cause
This value indicates the cause for the latest clock source switch.
 
If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware 
clock mux, the value of the SWTRG field can be either 4 or 5.
  NOTE  
000b - Reserved
001b - Switch after request succeeded.
010b - Switch after the request failed because of an inactive target clock and the current clock is 
FIRC.
011b - Switch after the request failed because of an inactive current clock and the current clock is 
FIRC.
100b - Switch to FIRC because of a safe clock request or reset succeeded.
101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous 
current clock source was inactive.
110b - Reserved
111b - Reserved
16
SWIP
Switch in progress
 
New clock switch request can only be given three clock cycles after the completion of the 
previous request.
  NOTE  
0b - Clock source switching is complete.
1b - Clock source switching is in progress.
15-4
—
This field is reserved and reads return zeros.
3
Safe clock request
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1118 / 5251


---
# 페이지 217

Table continued from the previous page...
Field
Function
SAFE_SW
This field provides an indication of whether a switch to safe clock operation was requested during the 
previous/ongoing request on clock mux 16.
0b - No safe clock switch operation was requested.
1b - Safe clock switch operation was requested.
2
CLK_SW
Clock switch
This field provides an indication of whether a clock switch operation was requested during the previous/
ongoing request on clock mux 16.
0b - No clock switch operation was requested.
1b - Clock switch operation was requested.
1-0
—
This field is reserved and reads return zeros.
25.5.73 Clock Mux 16 Divider 0 Control Register (MUX_16_DC_0)
Offset
Register
Offset
MUX_16_DC_0
708h
Function
This register controls the clock divider 0 for clock mux 16. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1119 / 5251


---
# 페이지 218

Fields
Field
Function
31
DE
Divider enable
0b - Divider is disabled.
1b - Divider is enabled.
30-22
—
This field is reserved and reads return zeros.
21-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.74 Clock Mux 16 Divider Update Status Register (MUX_16_DIV_UPD_STAT)
Offset
Register
Offset
MUX_16_DIV_UPD_STA
T
73Ch
Function
This register provides the update status of the clock dividers corresponding to clock mux 16. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
  NOTE  
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1120 / 5251


---
# 페이지 219

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
DIV_
STAT 
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
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 16
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
25.5.75 Clock Mux 18 Select Control Register (MUX_18_CSC)
Offset
Register
Offset
MUX_18_CSC
780h
Function
This register provides the clock source selection control for clock mux 18. Clock mux 18 implements hardware control clock 
switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock 
multiplexer" section for details.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1121 / 5251


---
# 페이지 220

This register is reset on destructive reset only.
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
SELCTL 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 18. The reserved values are not displayed.
0_0000b - FIRC
0_0010b - FXOSC
1_0110b - AIPS_PLAT_CLK
23-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
2
CLK_SW
Clock switch
Writing 1 to this bit makes a clock switch request to clock mux 18. After a clock switch operation is requested, 
this bit is auto cleared and a corresponding bit in the status register is set.
1-0
—
This field is reserved and reads return zeros.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1122 / 5251


---
# 페이지 221

25.5.76 Clock Mux 18 Select Status Register (MUX_18_CSS)
Offset
Register
Offset
MUX_18_CSS
784h
Function
This register provides the current clock source selection status for clock mux 18.
This register is reset on destructive reset only.
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
SELSTAT 
0
SWTRG 
SWIP 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 18. The reserved values are not 
displayed.
0_0000b - FIRC
0_0010b - FXOSC
1_0110b - AIPS_PLAT_CLK
23-20
—
This field is reserved and reads return zeros.
19-17
SWTRG
Switch trigger cause
This value indicates the cause for the latest clock source switch.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1123 / 5251


---
# 페이지 222

Table continued from the previous page...
Field
Function
 
If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware 
clock mux, the value of the SWTRG field can be either 4 or 5.
  NOTE  
000b - Reserved
001b - Switch after request succeeded.
010b - Switch after the request failed because of an inactive target clock and the current clock is 
FIRC.
011b - Switch after the request failed because of an inactive current clock and the current clock is 
FIRC.
100b - Switch to FIRC because of a safe clock request or reset succeeded.
101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous 
current clock source was inactive.
110b - Reserved
111b - Reserved
16
SWIP
Switch in progress
 
New clock switch request can only be given three clock cycles after the completion of the 
previous request.
  NOTE  
0b - Clock source switching is complete.
1b - Clock source switching is in progress.
15-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
This field provides an indication of whether a switch to safe clock operation was requested during the 
previous/ongoing request on clock mux 18.
0b - No safe clock switch operation was requested.
1b - Safe clock switch operation was requested.
2
CLK_SW
Clock switch
This field provides an indication of whether a clock switch operation was requested during the previous/
ongoing request on clock mux 18.
0b - No clock switch operation was requested.
1b - Clock switch operation was requested.
1-0
—
This field is reserved and reads return zeros.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1124 / 5251


---
# 페이지 223

25.5.77 Clock Mux 18 Divider 0 Control Register (MUX_18_DC_0)
Offset
Register
Offset
MUX_18_DC_0
788h
Function
This register controls the clock divider 0 for clock mux 18. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
DE
Divider enable
0b - Divider is disabled.
1b - Divider is enabled.
30-17
—
This field is reserved and reads return zeros.
16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1125 / 5251


---
# 페이지 224

25.5.78 Clock Mux 18 Divider Update Status Register (MUX_18_DIV_UPD_STAT)
Offset
Register
Offset
MUX_18_DIV_UPD_STA
T
7BCh
Function
This register provides the update status of the clock dividers corresponding to clock mux 18. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
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
DIV_
STAT 
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
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 18
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1126 / 5251


---
# 페이지 225

Table continued from the previous page...
Field
Function
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
25.5.79 Clock Mux 19 Select Control Register (MUX_19_CSC)
Offset
Register
Offset
MUX_19_CSC
7C0h
Function
This register provides the clock source selection control for clock mux 19. Clock mux 19 implements hardware control clock 
switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock 
multiplexer" section for details.
This register is reset on destructive reset only.
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
SELCTL 
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
SAFE_
SW 
CLK_
SW 
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
This field is reserved and reads return zeros.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1127 / 5251


---
# 페이지 226

Table continued from the previous page...
Field
Function
—
27-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 19. The reserved values are not displayed.
0000b - FIRC
1101b - PLL_AUX_PHI1_CLK
23-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
2
CLK_SW
Clock switch
Writing 1 to this bit makes a clock switch request to clock mux 19. After a clock switch operation is requested, 
this bit is auto cleared and a corresponding bit in the status register is set.
1-0
—
This field is reserved and reads return zeros.
25.5.80 Clock Mux 19 Select Status Register (MUX_19_CSS)
Offset
Register
Offset
MUX_19_CSS
7C4h
Function
This register provides the current clock source selection status for clock mux 19.
This register is reset on destructive reset only.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1128 / 5251


---
# 페이지 227

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
SELSTAT 
0
SWTRG 
SWIP 
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
SAFE_
SW 
CLK_
SW 
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
This field is reserved and reads return zeros.
27-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 19. The reserved values are not 
displayed.
0000b - FIRC
1101b - PLL_AUX_PHI1_CLK
23-20
—
This field is reserved and reads return zeros.
19-17
SWTRG
Switch trigger cause
This value indicates the cause for the latest clock source switch.
 
If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware 
clock mux, the value of the SWTRG field can be either 4 or 5.
  NOTE  
000b - Reserved
001b - Switch after request succeeded.
010b - Switch after the request failed because of an inactive target clock and the current clock is 
FIRC.
011b - Switch after the request failed because of an inactive current clock and the current clock is 
FIRC.
100b - Switch to FIRC because of a safe clock request or reset succeeded.
101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous 
current clock source was inactive.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1129 / 5251


---
# 페이지 228

Table continued from the previous page...
Field
Function
110b - Reserved
111b - Reserved
16
SWIP
Switch in progress
 
New clock switch request can only be given three clock cycles after the completion of the 
previous request.
  NOTE  
0b - Clock source switching is complete.
1b - Clock source switching is in progress.
15-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
This field provides an indication of whether a switch to safe clock operation was requested during the 
previous/ongoing request on clock mux 19.
0b - No safe clock switch operation was requested.
1b - Safe clock switch operation was requested.
2
CLK_SW
Clock switch
This field provides an indication of whether a clock switch operation was requested during the previous/
ongoing request on clock mux 19.
0b - No clock switch operation was requested.
1b - Clock switch operation was requested.
1-0
—
This field is reserved and reads return zeros.
25.5.81 Clock Mux 19 Divider 0 Control Register (MUX_19_DC_0)
Offset
Register
Offset
MUX_19_DC_0
7C8h
Function
This register controls the clock divider 0 for clock mux 19. 
This divider is a 50% duty cycle divider.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1130 / 5251


---
# 페이지 229

 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
DE
Divider enable
0b - Divider is disabled.
1b - Divider is enabled.
30-22
—
This field is reserved and reads return zeros.
21-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.82 Clock Mux 19 Divider Update Status Register (MUX_19_DIV_UPD_STAT)
Offset
Register
Offset
MUX_19_DIV_UPD_STA
T
7FCh
Function
This register provides the update status of the clock dividers corresponding to clock mux 19. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1131 / 5251


---
# 페이지 230

clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
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
DIV_
STAT 
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
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 19
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1132 / 5251


---
# 페이지 231

25.5.83 Clock Mux 20 Select Control Register (MUX_20_CSC)
Offset
Register
Offset
MUX_20_CSC
800h
Function
This register provides the clock source selection control for clock mux 20. Clock mux 20 implements hardware control clock 
switching ensuring that the clock switch happens in a graceful manner (without glitches). See the "Hardware-controlled clock 
multiplexer" section for details.
This register is reset on destructive reset only.
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
SELCTL 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
28-24
SELCTL
Clock source selection control
Selects the source clock for clock mux 20. The reserved values are not displayed.
0_0000b - FIRC
0_0010b - FXOSC
1_0110b - AIPS_PLAT_CLK
23-4
—
This field is reserved and reads return zeros.
3
SAFE_SW
Safe clock request
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1133 / 5251


---
# 페이지 232

Table continued from the previous page...
Field
Function
Writing 1 to this bit makes a safe clock switch request to FIRC. After a safe clock switch operation is 
requested, this bit is auto cleared and a corresponding bit in the status register is set.
2
CLK_SW
Clock switch
Writing 1 to this bit makes a clock switch request to clock mux 20. After a clock switch operation is requested, 
this bit is auto cleared and a corresponding bit in the status register is set.
1-0
—
This field is reserved and reads return zeros.
25.5.84 Clock Mux 20 Select Status Register (MUX_20_CSS)
Offset
Register
Offset
MUX_20_CSS
804h
Function
This register provides the current clock source selection status for clock mux 20.
This register is reset on destructive reset only.
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
SELSTAT 
0
SWTRG 
SWIP 
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
SAFE_
SW 
CLK_
SW 
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
31-29
—
This field is reserved and reads return zeros.
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1134 / 5251


---
# 페이지 233

Table continued from the previous page...
Field
Function
28-24
SELSTAT
Clock source selection status
This value indicates the current source selected for clock mux 20. The reserved values are not 
displayed.
0_0000b - FIRC
0_0010b - FXOSC
1_0110b - AIPS_PLAT_CLK
23-20
—
This field is reserved and reads return zeros.
19-17
SWTRG
Switch trigger cause
This value indicates the cause for the latest clock source switch.
 
If the clock fails, followed by multiple safe clock switch requests for MC_CGM hardware 
clock mux, the value of the SWTRG field can be either 4 or 5.
  NOTE  
000b - Reserved
001b - Switch after request succeeded.
010b - Switch after the request failed because of an inactive target clock and the current clock is 
FIRC.
011b - Switch after the request failed because of an inactive current clock and the current clock is 
FIRC.
100b - Switch to FIRC because of a safe clock request or reset succeeded.
101b - Switch to FIRC because of a safe clock request or reset succeeded, but the previous 
current clock source was inactive.
110b - Reserved
111b - Reserved
16
SWIP
Switch in progress
 
New clock switch request can only be given three clock cycles after the completion of the 
previous request.
  NOTE  
0b - Clock source switching is complete.
1b - Clock source switching is in progress.
15-4
—
This field is reserved and reads return zeros.
3
Safe clock request
Table continues on the next page...
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1135 / 5251


---
# 페이지 234

Table continued from the previous page...
Field
Function
SAFE_SW
This field provides an indication of whether a switch to safe clock operation was requested during the 
previous/ongoing request on clock mux 20.
0b - No safe clock switch operation was requested.
1b - Safe clock switch operation was requested.
2
CLK_SW
Clock switch
This field provides an indication of whether a clock switch operation was requested during the previous/
ongoing request on clock mux 20.
0b - No clock switch operation was requested.
1b - Clock switch operation was requested.
1-0
—
This field is reserved and reads return zeros.
25.5.85 Clock Mux 20 Divider 0 Control Register (MUX_20_DC_0)
Offset
Register
Offset
MUX_20_DC_0
808h
Function
This register controls the clock divider 0 for clock mux 20. 
This divider is a 50% duty cycle divider.
 
The update to the fields of this register should be an atomic write, that is, one single write should update the 
complete register.
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
DE 
0
DIV 
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
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1136 / 5251


---
# 페이지 235

Fields
Field
Function
31
DE
Divider enable
0b - Divider is disabled.
1b - Divider is enabled.
30-18
—
This field is reserved and reads return zeros.
17-16
DIV
Division value
This field provides the division value for the clock divider. The clock period of the clock after division is 
'DIV+1' times the time period of the current input clock to the divider.
15-0
—
This field is reserved and reads return zeros.
25.5.86 Clock Mux 20 Divider Update Status Register (MUX_20_DIV_UPD_STAT)
Offset
Register
Offset
MUX_20_DIV_UPD_STA
T
83Ch
Function
This register provides the update status of the clock dividers corresponding to clock mux 20. When a write operation on any 
divider control register is performed, the divider status bit in this register is set to logic-1. The bit is set to logic-0 when the 
divider has sampled the new divider configuration. Performing multiple writes without tracking the status bit on same or other 
clock dividers inside the same clock mux leads to inconsistent reporting, that is, the divider status maybe be set to logic-0 
when the corresponding divider update is pending.
 
Read accesses to MUX_n_DIV_UPD_STAT always complete without returning bus transfer error independent of 
whether any divider(s) are implemented inside MC_CGM clock mux.
  NOTE  
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1137 / 5251


---
# 페이지 236

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
DIV_
STAT 
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
This field is reserved and reads return zeros.
0
DIV_STAT
Divider status for clock mux 20
On reading MUX_n_DIV_UPD_STAT after updating a divider control register, if the value of this field is 
fixed to 1 because of an error in the selected clock source, perform the following steps to switch the mux 
to a new clock source:
1. Switch the mux to a working clock source without polling this field.
2. Update MUX_n_DC_m and poll this field.
 
This field clears once divider configuration is updated or on destructive reset. If functional 
reset comes when this field is 1 then it can remain fixed to 1 until divider input clock 
is restored.
  NOTE  
0b - No divider configuration update is pending.
1b - Divider configuration update on at least one divider associated with this multiplexer is 
pending.
25.6 Glossary
PCFS
Progressive clock frequency switching
LCM
Least common multiple
NXP Semiconductors
Clock Generation Module (MC_CGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1138 / 5251


---