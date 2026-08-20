# 페이지 46

Chapter 33
Reset Generation Module (MC_RGM)
33.1 Chip-specific MC_RGM information
33.1.1 MC_RGM configuration
The "Reset sources—POR, Destructive, and Functional" section of the "Reset Overview" chapter provides information about 
MC_RGM's reset sources. The chapter also provides details about the chip's reset architecture.
 
The ERCTRL register configuration takes several cycles to be effective. Any further access to MC_RGM must 
happen after at least nine AIPS_SLOW_CLK cycles of writing to ERCTRL.
  NOTE  
Table 219. Register fields and applicability
Register
Bit field
Chips where applicable
Functional /External Reset Status 
Register (FES)
SWT1_RST
S32K324, S32K322, S32K328, 
S32K338, S32K358, S32K388, S32K389
SWT2_RST
S32K338, S32K388, S32K389
SWT3_RST
S32K388, S32K389
Functional Event Reset Disable 
Register (FERD)
D_SWT1_RST
S32K324, S32K322, S32K328, 
S32K338, S32K358, S32K388, S32K389
D_SWT2_RST
S32K338, S32K388, S32K389
D_SWT3_RST
S32K388, S32K389
33.1.2 Functional reset entry timer implementation
The default timeout value of the functional reset entry timer is 2048 clocks of MC_RGM clock (FIRC). If the RGM entry sequence 
hangs, then POR_WDG would trigger and the status of this functional reset entry sequence timeout is indicated at chip-level status 
register. The status of timeout in such case, is indicated at DCM.DCMROPP1[28]. There is no impact to the device behavior if the 
functional reset entry sequence gets completed within the POR_WDG timeout window.
33.1.3 S32K3xx reset state machine
The reset sequence of the S32K3xx products is depicted in the figure below:
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1221 / 5251


---
# 페이지 47

Power-on 
sequence
Power-on 
reset event
Destructive 
reset event
Functional 
reset event
Functional reset 
sequence
Functional reset 
entry sequence
Out of reset
Destructive reset 
sequence
Exit from 
Standby mode
Enter
Standby mode
Standby mode
Destructive 
reset event
Destructive 
reset event
In case of Standby mode, only the Run
domain resets and the exit from POR 
happens on Standby mode exit. 
Figure 156. S32K3xx reset state machine
33.2 Introduction
The Reset Generation Module (MC_RGM) centralizes the different reset sources and manages the reset sequence of the chip. It 
provides a register interface and the reset sequencer. There are various registers available in this module to monitor and control 
the chip reset sequence.
The following figure shows the block diagram of MC_RGM.
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1222 / 5251


---
# 페이지 48

Registers
Platform interface
Destructive reset
 filter
Functional reset 
filter
MC_RGM
Reset state
 machine
Power-on
External reset
Software resettable
 domains
Destructive reset n
Functional reset n
Chip resets
Standard IPS interface
MC_CGM
MC_ME
Figure 157. MC_RGM block diagram
33.3 Features
Here are the key features of MC_RGM:
• Destructive and functional reset management
• Capturing the reset sources for each reset sequence (reset status flags)
• Assertion the RESET_B pin to propagate the reset sequence out of chip
• Configurable escalation of recurring 'functional' resets to 'destructive' reset
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1223 / 5251


---
# 페이지 49

• Configurable escalation of recurring 'destructive' resets to keep the chip in the reset state until the next power-on reset
• Software controllable reset assertion
• Pad safe state control generation
33.4 Reset sources
The reset sources are organized in three categories: power-on, destructive, and functional.
A power-on reset source is associated with an event typically related to power-up or low-voltage scenarios. When a power-on reset 
occurs, the full reset sequence is applied to the chip. This resets the full chip, including the MC_RGM, and the memory content 
must be considered to be invalid.
A destructive reset source is associated with an event related to a critical, usually hardware, error or dysfunction. When a 
destructive reset event occurs, the full reset sequence is applied to the chip. This resets the full chip ensuring a safe start-up state 
for both digital and analog modules, and the memory content must be considered to be invalid.
A functional reset source is associated with an event related to a less-critical, usually non-hardware, error or dysfunction. When a 
functional reset event occurs, a partial reset sequence is applied to the chip. In this case, most digital modules are reset normally, 
while the state of analog modules or specific digital modules as well as the system memory content is preserved.
33.5 External signal description
The MC_RGM interfaces with the RESET_B pin.
The following table describes the signals that are connected to the I/O pad ring.
Table 220. MC_RGM external signals
Signal name
Reset value
Description
RESET_B
0
Active low external reset.
A bidirectional reset pin indicating the reset state.
33.6 RESET_B pin assertion and pin safe state control
The MC_RGM asserts the RESET_B pin when the device is in a reset sequence, and it remains asserted until the end of the reset 
sequence. During this reset sequence, most of the chip's pins are safe/pad stated according to the values shown in the IOMUX 
table/spreadsheet. Note that the safe state values may vary according to the reset sequence type.
In addition, the MC_RGM has a feature to assert the RESET_B pin through software, without initiating a reset sequence. This is 
achieved by writing 1b to the ERCTRL[ERASSERT]. When this occurs, most of the chip's pins are safe-stated according to the 
values shown in the IOMUX table/spread sheet. The RESET_B assertion and pin safe-stating remain active until the end of the 
next reset sequence.
This features has to be used only with selftest of the main reset domain.
33.7 Functional description
33.7.1 Reset state machine
The main role of MC_RGM is the generation of the reset sequence that ensures that the correct parts of the chip are reset based 
on the reset source event.
For each reset event, immediately after it is captured by the MC_RGM, the following takes place:
1. The corresponding reset event status bit is set in the MC_RGM_DES and MC_RGM_FES registers.
2. The pins are put into their default states
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1224 / 5251


---
# 페이지 50

3. The RESET_B pin is asserted.
Power-on 
sequence
Power-on 
reset event
Destructive 
reset event
Functional 
reset event
Functional reset 
sequence
Functional reset 
entry sequence
Out of reset
Destructive reset 
sequence
Destructive 
reset event
Destructive 
reset event
Destructive 
reset event
Exit from 
Standby mode
Enter
Standby mode
Standby mode
Figure 158. Reset sequence
 
See chip-specific MC_RGM information for chip-specific reset sequence details.
  NOTE  
33.7.1.1
Power-on reset sequence
A reset is always generated when the power-on reset source is asserted, and it has priority over all other reset sources. Such a 
power-on reset forces the reset state machine to enter the power-on sequence resulting in the assertion of all reset signals. The 
reset state machine starts progressing when the following two conditions are verified:
1. All the power-on reset events are cleared
2. The MC_RGM's clock source (the FIRC) has started up and stabilized
If a power-on reset event has occurred, the DES[F_POR] bit is set.
The power-on reset cannot be demoted by the software.
33.7.1.2
Destructive reset sequence
The 'Destructive reset sequence' is comprised of a number of phases, where DEST0 is the first phase and is followed by DEST1 
and so forth.
This phase is entered immediately from any phase on a power-on, standby reset sequence, or enabled destructive reset event . 
A destructive reset counter starts immediately on entry in the DEST0 phase. The DEST0 state is exited to the DEST1 state on the 
rising edge of FIRC_CLK immediately after all of the following conditions have been established:
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1225 / 5251


---
# 페이지 51

• The DEST0 duration time has expired
• All destructive reset inputs are cleared
The DEST0 state is immediately exited to the power-on state if a power-on reset event occurs.
The reset state machine exits the destructive reset sequence and enters the functional reset sequence when:
• All the destructive reset events are cleared.
• All the processes that take place during the destructive reset sequence have completed. For details, see Reset chapter.
• The 'destructive' reset escalator counter has not reached the value in DRET[DRET].
33.7.1.3
Functional reset sequence
There are two functional reset sequence, the functional reset entry sequence and the functional reset exit sequence.
33.7.1.3.1
Functional reset entry sequence
The functional reset entry sequence is only entered when a functional reset event occurs during the idle phase.
If a functional reset event occurs during an ongoing reset sequence, the corresponding event status flag is set, and the RESET_B 
pin is asserted per the reset event's configuration. However, the reset sequence is not influenced, and it continues to progress 
without interruption.
Functional reset is not asserted during functional reset entry sequence.
The functional reset entry sequence is exited to the DEST0 on the next rising edge of FIRC if a destructive reset event has 
occurred. The sequence immediately enters the power up sequence if a POR event occurs
In all other cases, the sequence exits to the first stage of functional reset exit sequence.
33.7.1.3.2
Functional reset exit sequence
The functional reset exit sequence is entered either on exit from the destructive reset sequence or on completion of the functional 
reset entry sequence. The reset state machine exits this sequence and enters the idle phase on verification of the following:
• All the functional reset events are cleared.
• All the processes that take place during the functional reset sequence have completed. For details, see Reset chapter.
If a functional reset event occurs during an ongoing reset sequence, the corresponding event status flag is set, and the RESET_B 
pin is asserted per the reset event's configuration. However, the reset sequence is not influenced, and it continues to progress 
without interruption.
33.7.1.4
Idle phase
This is the final phase and is entered on exit from the functional reset exit sequence . When this phase is reached, MC_RGM 
releases control of the system to the platform and waits for the new reset events that can trigger a reset sequence.
33.7.2 Destructive resets
A destructive reset indicates that an event has occurred after which critical register or memory content can no longer 
be guaranteed.
The status flag associated with a given destructive reset event (Destructive Event Status Register (DES)) is set when the 
destructive reset is asserted and the power-on reset is not asserted. It is possible for multiple status bits to be set simultaneously 
and the software determines which reset source is the most critical for the application.
The low-voltage detector threshold ensures that when the reset corresponding to the core supply low-voltage detect is enabled, 
the supply is sufficient to have the destructive event correctly propagated through the digital logic. Therefore, if a given destructive 
reset is enabled, MC_RGM ensures that the associated reset event is correctly triggered to the full system.
An enabled destructive reset triggers a reset sequence starting from the beginning of DEST0.
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1226 / 5251


---
# 페이지 52

33.7.3 External reset
MC_RGM manages the external reset coming from RESET_B. The detection of a falling edge on RESET_B starts the reset 
sequence from the beginning of the destructive reset entry sequence.
The status flag associated with the external reset falling edge event (the FES[F_EXR]) is set when the external reset is asserted 
and the power-on reset is not asserted.
33.7.4 Functional resets
A functional reset indicates that an event has occurred after which it can be guaranteed that critical register and memory content 
is still intact.
The status flag associated with a given functional reset event (Functional /External Reset Status Register (FES)) is set when the 
functional reset is asserted and the power-on reset is not asserted. It is possible for multiple status bits to be set simultaneously 
and the software determines which reset source is the most critical for the application.
An enabled functional reset triggers a reset sequence starting from the beginning of the functional reset entry sequence.
33.7.5 Alternate event generation
MC_RGM provides alternative events to be generated on reset source assertion. When a reset source is asserted, MC_RGM 
normally enters the reset sequence. Alternatively, it is possible for some reset source events to be converted from a reset to an 
interrupt request issued to the core. Alternate event selection for a given reset source is made through the RGM_FERD register 
as shown in the following table.
Table 221. Functional Reset Disable Register (RGM_FERD) field descriptions
RGM bit FERD value
Generated event
0
Reset
1
Interrupt request
The alternate event is cleared by deasserting the source of the request (that is, at the reset source that caused the alternate 
request) and also clearing the appropriate RGM_FES status bit.
33.7.6 RESET_B assertion control
The software indicates to the MC_RGM that the RESET_B is to be asserted by writing to the ERASSERT bit in the RGM_ERCTRL 
register. When this bit is set by the software, RESET_B gets asserted. Setting of this field does not impact the reset sequence in 
any way.
An example where the ERCTRL[ERASSERT] field could be set by the software is when entering the self test sequence, during 
which RESET_B is to be asserted. This indicates the chip is not available in the functional mode although a reset sequence is not 
in progress. The deassertion of RESET_B is not controlled by the software. Instead, the RESET_B pin remains asserted until the 
next time the chip exits a reset sequence.
ERASSERT bit is also cleared during the reset sequence.
MC_RGM asserts the external reset if the reset sequence is triggered by one of the following:
• A power-on reset
• A destructive reset event
• A functional reset event
In this case, external reset is asserted until all conditions for the exiting reset sequence have been met, with the exception of the 
RESET_B assertion check
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1227 / 5251


---
# 페이지 53

33.7.7 Functional reset escalation
Functional reset escalation can be used to generate a destructive reset if a number of functional resets is occurred between 
software writes to the RGM_FRET register. This function is enabled by writing a non-zero value to the FRET field of this register.
After the functional reset escalation is enabled, MC_RGM increases a counter on each functional reset that causes a reset 
sequence to be initiated (which means, entrance into FUNC0 from the IDLE phase). This counter is cleared on a write of any value 
to the RGM_FRET register and on any power-on or destructive reset. If the counter reaches the value in the FRET field of the 
RGM_FRET register, MC_RGM asserts a destructive reset.
The following figure shows the functional reset escalation counter.
RGM_FRET
register
functional reset               
count
functional reset event
destructive reset
write to RGM_FRET
1
0
1
0
=
destructive 
reset event
RGM_FRET
register
functional reset               
count
functional reset event
destructive reset
write to RGM_FRET
1
0
1
0
=
destructive 
reset event
Figure 159. Functional reset escalation counter
 
Functional counter increments for each reset source for which escalation is enabled. For details, see "Reset 
sources" table in the Reset chapter.
  NOTE  
33.7.8 Destructive reset escalation
Destructive reset escalation can be used to keep the chip in the reset state until the power-on triggers a reset sequence if a 
number of destructive resets are occurred between software writes to the RGM_DRET register. This function is enabled by writing 
a non-zero value to the DRET field of this register.
After destructive reset escalation is enabled, MC_RGM increases a counter on each destructive reset that is enabled. . This 
causes a reset sequence to be initiated (that is, entrance into DEST0 from the idle phase or any other reset phase) or an ongoing 
reset sequence to restart (that is, entrance into DEST0 from any other reset phase). This counter is cleared on a write of any value 
to the RGM_DRET register and on any power-on reset. If the counter reaches the value in the DRET field of the RGM_DRET 
register, MC_RGM enters reset DEST0 and stays there until the next power-on reset occurs .
The following figure shows the destructive reset escalation counter.
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1228 / 5251


---
# 페이지 54

RGM_DRET
register
destructive reset               
count
destructive reset event
power-on reset
write to RGM_DRET
1
0
1
0
=
stay in reset phase DEST0
Figure 160. Destructive reset escalation counter
 
Destructive counter increments for each reset source for which escalation is enabled. For details, see "Reset 
sources" table in the Reset chapter.
  NOTE  
33.8 MC_RGM register descriptions
Access to the following locations do not generate transfer error:
• 2Ch
All registers can be accessed as read/write in supervisor mode.
33.8.1 MC RGM Register Map memory map
MC_RGM base address: 4028_C000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Destructive Event Status Register (DES)
32
RW
0000_0001h
8h
Functional /External Reset Status Register (FES)
32
RW
0000_0000h
Ch
Functional Event Reset Disable Register (FERD)
32
RW
0000_0000h
10h
Functional Bidirectional Reset Enable Register (FBRE)
32
RW
0000_0000h
14h
Functional Reset Escalation Counter Register (FREC)
32
RW
0000_0000h
18h
Functional Reset Escalation Threshold Register (FRET)
32
RW
0000_000Fh
1Ch
Destructive Reset Escalation Threshold Register (DRET)
32
RW
0000_0000h
20h
External Reset Control Register (ERCTRL)
32
RW
0000_0000h
24h
Reset During Standby Status Register (RDSS)
32
RW
0000_0000h
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1229 / 5251


---
# 페이지 55

33.8.2 Destructive Event Status Register (DES)
Offset
Register
Offset
DES
0h
Function
This register contains the status of the 'destructive' reset sources. This register can be accessed as read/write in supervisor mode 
and read-only in user mode. Register bits are cleared on write '1'. This register is reset only on power-on reset.
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
DEBU
G_D...
SW_
DEST 
0
0
0
0
0
0
0
0
0
0
HSE_
SNV...
HSE_T
MP...
CM7_
COR...
W
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
SYS_
DIV...
HSE_
CLK...
0
AIPS_
PL...
0
CORE
_CL...
PLL_
LOL 
FXOS
C_F...
0
MC_R
GM_...
0
STCU
_URF 
FCCU
_FTR 
0
0
F_
POR 
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
1
Fields
Field
Function
31
—
Reserved
30
DEBUG_DEST
Flag for 'Destructive' Reset DEBUG_DEST
0b - 'Destructive' reset event DEBUG_DEST has not occurred since either the last clear or the 
last power-on reset assertion.
1b - 'Destructive' reset event DEBUG_DEST has occurred.
29
SW_DEST
Flag for 'Destructive' Reset SW_DEST
0b - 'Destructive' reset event SW_DEST has not occurred since either the last clear or the last 
power-on reset assertion.
1b - 'Destructive' reset event SW_DEST has occurred.
28
—
Reserved
27
Reserved
Table continues on the next page...
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1230 / 5251


---
# 페이지 56

Table continued from the previous page...
Field
Function
—
26
—
Reserved
25
—
Reserved
24
—
Reserved
23
—
Reserved
22
—
Reserved
21
—
Reserved
20
—
Reserved
19
—
Reserved
18
HSE_SNVS_RS
T
Flag for 'Destructive' Reset HSE_SNVS_RST
0b - 'Destructive' reset event HSE_SNVS_RST has not occurred since either the last clear or the 
last power-on reset assertion.
1b - 'Destructive' reset event HSE_SNVS_RST has occurred.
17
HSE_TMPR_R
ST
Flag for 'Destructive' Reset HSE_TMPR_RST
0b - 'Destructive' reset event HSE_TMPR_RST has not occurred since either the last clear or the 
last power-on reset assertion.
1b - 'Destructive' reset event HSE_TMPR_RST has occurred.
16
CM7_CORE_C
LK_FAIL
Flag for 'Destructive' Reset CM7_CORE_CLK_FAIL
0b - 'Destructive' reset event CM7_CORE_CLK_FAIL has not occurred since either the last clear 
or the last power-on reset assertion.
1b - 'Destructive' reset event CM7_CORE_CLK_FAIL has occurred.
15
SYS_DIV_FAIL
Flag for 'Destructive' Reset SYS_DIV_FAIL
Table continues on the next page...
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1231 / 5251


---
# 페이지 57

Table continued from the previous page...
Field
Function
0b - 'Destructive' reset event SYS_DIV_FAIL has not occurred since either the last clear or the 
last power-on reset assertion.
1b - 'Destructive' reset event SYS_DIV_FAIL has occurred.
14
HSE_CLK_FAIL
Flag for 'Destructive' Reset HSE_CLK_FAIL
0b - 'Destructive' reset event HSE_CLK_FAIL has not occurred since either the last clear or the 
last power-on reset assertion.
1b - 'Destructive' reset event HSE_CLK_FAIL has occurred.
13
—
Reserved
12
AIPS_PLAT_CL
K_FAIL
Flag for 'Destructive' Reset AIPS_PLAT_CLK_FAIL
0b - 'Destructive' reset event AIPS_PLAT_CLK_FAIL has not occurred since either the last clear 
or the last power-on reset assertion.
1b - 'Destructive' reset event AIPS_PLAT_CLK_FAIL has occurred.
11
—
Reserved
10
CORE_CLK_FA
IL
Flag for 'Destructive' Reset CORE_CLK_FAIL
0b - 'Destructive' reset event CORE_CLK_FAIL has not occurred since either the last clear or the 
last power-on reset assertion.
1b - 'Destructive' reset event CORE_CLK_FAIL has occurred.
9
PLL_LOL
Flag for 'Destructive' Reset PLL_LOL
0b - 'Destructive' reset event PLL_LOL has not occurred since either the last clear or the last 
power-on reset assertion.
1b - 'Destructive' reset event PLL_LOL has occurred.
8
FXOSC_FAIL
Flag for 'Destructive' Reset FXOSC_FAIL
0b - 'Destructive' reset event FXOSC_FAIL has not occurred since either the last clear or the last 
power-on reset assertion.
1b - 'Destructive' reset event FXOSC_FAIL has occurred.
7
—
Reserved
6
MC_RGM_FRE
Flag for 'Destructive' Reset MC_RGM_FRE
0b - 'Destructive' reset event MC_RGM_FRE has not occurred since either the last clear or the 
last power-on reset assertion.
1b - 'Destructive' reset event MC_RGM_FRE has occurred.
Table continues on the next page...
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1232 / 5251


---
# 페이지 58

Table continued from the previous page...
Field
Function
5
—
Reserved
4
STCU_URF
Flag for 'Destructive' Reset STCU_URF
0b - 'Destructive' reset event STCU_URF has not occurred since either the last clear or the last 
power-on reset assertion.
1b - 'Destructive' reset event STCU_URF has occurred.
3
FCCU_FTR
Flag for 'Destructive' Reset FCCU_FTR
0b - 'Destructive' reset event FCCU_FTR has not occurred since either the last clear or the last 
power-on reset assertion.
1b - 'Destructive' reset event FCCU_FTR has occurred.
2
—
Reserved
1
—
Reserved
0
F_POR
Flag for power-on reset
 
If this field is set, ignore all the fields of Destructive Event Status Register (DES) and 
Functional /External Reset Status Register (FES) registers at power up.
  NOTE  
0b - No power-on event has occurred since the last clear.
1b - A power-on event has occurred.
33.8.3 Functional /External Reset Status Register (FES)
Offset
Register
Offset
FES
8h
Function
This register contains the status of the 'functional' and external reset sources. This register can be accessed as read/write in 
supervisor mode and read-only in user mode. Register fields are cleared on write '1' if the triggering event has already been 
cleared at the source. This register is reset only on power-on reset.
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1233 / 5251


---
# 페이지 59

 
• The startup self-test functional reset event to MC_RGM initiates a functional reset sequence after which the 
FES[ST_DONE] is set. This field is sticky in nature and gets cleared if software clears this field.
• If functional reset escalation to destructive reset is disabled, then the status of this register must be ignored 
if the fields of Destructive Event Status Register (DES) other than DES[F_POR] are set.
• If functional reset escalation to destructive reset is enabled and if the fields of Destructive Event Status 
Register (DES), other than DES[F_POR], are set, then based on these fields user should check if the cause of 
the destructive reset was due to functional reset escalation or if it was triggered directly by a destructive reset 
source, in which case FES needs to be ignored.
• See chip-specific MC_RGM information for applicability of the FES[ST_DONE] field.
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
DEBU
G_F...
SW_
FUNC 
0
0
0
0
0
0
0
0
HSE_
BOO...
0
0
0
HSE_
SWT...
W
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
PLL_
AUX 
0
SWT3
_RST 
JTAG_
RST 
SWT2
_RST 
SWT1
_RST 
SWT0
_RST 
0
ST_
DONE 
FCCU
_RST 
0
0
F_EXR 
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
—
Reserved
30
DEBUG_FUNC
Flag for 'Functional' Reset DEBUG_FUNC
0b - 'Functional' reset event DEBUG_FUNC has not occurred since either the last clear or the last 
power-on reset assertion.
1b - 'Functional' reset event DEBUG_FUNC has occurred.
29
SW_FUNC
Flag for 'Functional' Reset SW_FUNC
0b - 'Functional' reset event SW_FUNC has not occurred since either the last clear or the last 
power-on reset assertion.
1b - 'Functional' reset event SW_FUNC has occurred.
28
—
Reserved
27
Reserved
Table continues on the next page...
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1234 / 5251


---
# 페이지 60

Table continued from the previous page...
Field
Function
—
26
—
Reserved
25
—
Reserved
24
—
Reserved
23
—
Reserved
22
—
Reserved
21
—
Reserved
20
HSE_BOOT_R
ST
Flag for 'Functional' Reset HSE_BOOT_RST
0b - 'Functional' reset event HSE_BOOT_RST has not occurred since either the last clear or the 
last power-on reset assertion.
1b - 'Functional' reset event HSE_BOOT_RST has occurred.
19
—
Reserved
18
—
Reserved
17
—
Reserved
16
HSE_SWT_RS
T
Flag for 'Functional' Reset HSE_SWT_RST
0b - 'Functional' reset event HSE_SWT_RST has not occurred since either the last clear or the 
last power-on reset assertion.
1b - 'Functional' reset event HSE_SWT_RST has occurred.
15
—
Reserved
14
Reserved
Table continues on the next page...
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1235 / 5251


---
# 페이지 61

Table continued from the previous page...
Field
Function
—
13
—
Reserved
12
PLL_AUX
Flag for 'Functional' Reset PLL_AUX
0b - 'Functional' reset event PLL_AUX has not occurred since either the last clear or the last 
power-on reset assertion.
1b - 'Functional' reset event PLL_AUX has occurred.
11
—
Reserved
10
SWT3_RST
Flag for 'Functional' Reset SWT3_RST
0b - 'Functional' reset event SWT3_RST has not occurred since either the last clear or the last 
power-on reset assertion.
1b - 'Functional' reset event SWT3_RST has occurred.
9
JTAG_RST
Flag for 'Functional' Reset JTAG_RST
0b - 'Functional' reset event JTAG_RST has not occurred since either the last clear or the last 
power-on reset assertion.
1b - 'Functional' reset event JTAG_RST has occurred.
8
SWT2_RST
Flag for 'Functional' Reset SWT2_RST
0b - 'Functional' reset event SWT2_RST has not occurred since either the last clear or the last 
power-on reset assertion.
1b - 'Functional' reset event SWT2_RST has occurred.
7
SWT1_RST
Flag for 'Functional' Reset SWT1_RST
0b - 'Functional' reset event SWT1_RST has not occurred since either the last clear or the last 
power-on reset assertion.
1b - 'Functional' reset event SWT1_RST has occurred.
6
SWT0_RST
Flag for 'Functional' Reset SWT0_RST
0b - 'Functional' reset event SWT0_RST has not occurred since either the last clear or the last 
power-on reset assertion.
1b - 'Functional' reset event SWT0_RST has occurred.
5
—
Reserved
4
ST_DONE
Flag for 'Functional' Reset ST_DONE
Table continues on the next page...
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1236 / 5251


---
# 페이지 62

Table continued from the previous page...
Field
Function
0b - 'Functional' reset event ST_DONE has not occurred since either the last clear or the last 
power-on reset assertion.
1b - 'Functional' reset event ST_DONE has occurred.
3
FCCU_RST
Flag for 'Functional' Reset FCCU_RST
0b - 'Functional' reset event FCCU_RST has not occurred since either the last clear or the last 
power-on reset assertion.
1b - 'Functional' reset event FCCU_RST has occurred.
2
—
Reserved
1
—
Reserved
0
F_EXR
Flag for External Reset
External reset is a source of destructive reset. 
0b - No external reset event has occurred since either the last clear or the last power-on reset 
assertion.
1b - An external reset event has occurred.
33.8.4 Functional Event Reset Disable Register (FERD)
Offset
Register
Offset
FERD
Ch
Function
This register provides dedicated fields to disable functional reset sources. When any of these reset sources are disabled, the 
associated functional event is demoted to trigger an interrupt request. This register can be accessed as read/write in supervisor 
mode and read-only in user mode. Each byte can be written to only once after a destructive or power-on reset and this register 
is reset only on power-on and any destructive reset.
 
It is important to clear the Functional /External Reset Status Register (FES) before writing 1 to any of the fields in 
this register. Otherwise a interrupt request may occur.
  NOTE  
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1237 / 5251


---
# 페이지 63

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
D_DE
BUG...
0
0
0
0
0
0
0
0
0
0
0
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
0
0
0
0
D_SW
T3_...
D_JTA
G_...
D_SW
T2_...
D_SW
T1_...
D_SW
T0_...
0
0
D_FC
CU_...
0
0
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
Fields
Field
Function
31
—
Reserved
30
D_DEBUG_FU
NC
DEBUG_FUNC Disable Control
0b - Functional reset event DEBUG_FUNC triggers a reset sequence.
1b - Functional reset event DEBUG_FUNC generates an interrupt request.
29
—
Reserved
28
—
Reserved
27
—
Reserved
26
—
Reserved
25
—
Reserved
24
—
Reserved
23
—
Reserved
22
Reserved
Table continues on the next page...
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1238 / 5251


---
# 페이지 64

Table continued from the previous page...
Field
Function
—
21
—
Reserved
20
—
Reserved
19
—
Reserved
18
—
Reserved
17
—
Reserved
16
—
Reserved
15
—
Reserved
14
—
Reserved
13
—
Reserved
12
—
Reserved
11
—
Reserved
10
D_SWT3_RST
SWT3_RST Disable Control
0b - Functional reset event SWT3_RST triggers a reset sequence.
1b - Functional reset event SWT3_RST generates an interrupt request.
9
D_JTAG_RST
JTAG_RST Disable Control
0b - Functional reset event JTAG_RST triggers a reset sequence.
1b - Functional reset event JTAG_RST generates an interrupt request.
Table continues on the next page...
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1239 / 5251


---
# 페이지 65

Table continued from the previous page...
Field
Function
8
D_SWT2_RST
SWT2_RST Disable Control
0b - Functional reset event SWT2_RST triggers a reset sequence.
1b - Functional reset event SWT2_RST generates an interrupt request.
7
D_SWT1_RST
SWT1_RST Disable Control
0b - Functional reset event SWT1_RST triggers a reset sequence.
1b - Functional reset event SWT1_RST generates an interrupt request.
6
D_SWT0_RST
SWT0_RST Disable Control
0b - Functional reset event SWT0_RST triggers a reset sequence.
1b - Functional reset event SWT0_RST generates an interrupt request.
5
—
Reserved
4
—
Reserved
3
D_FCCU_RST
FCCU_RST Disable Control
0b - Functional reset event FCCU_RST triggers a reset sequence.
1b - Functional reset event FCCU_RST generates an interrupt request.
2
—
Reserved
1
—
Reserved
0
—
Reserved
33.8.5 Functional Bidirectional Reset Enable Register (FBRE)
Offset
Register
Offset
FBRE
10h
Function
This register enables the generation of an external reset on 'functional' reset.This register can be accessed as read/write in 
supervisor mode and read-only in user mode. This register is reset on power-on and any 'destructive' reset.
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1240 / 5251


---
# 페이지 66

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
BE_D
EBU...
BE_S
W_F...
0
0
0
0
0
0
0
0
BE_H
SE_...
0
0
0
BE_H
SE_...
W
Reset
0
0
0
0
0
0
0
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
BE_PL
L_...
0
BE_S
WT3...
BE_JT
AG...
BE_S
WT2...
BE_S
WT1...
BE_S
WT0...
0
BE_ST
_D...
BE_FC
CU...
0
0
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
Fields
Field
Function
31
—
Reserved
30
BE_DEBUG_FU
NC
Bidirectional Reset Enables for 'Functional' Reset DEBUG_FUNC
0b - External reset pin is asserted on a 'Functional' reset DEBUG_FUNC event if the reset is 
enabled.
1b - External reset pin is not asserted on a 'functional' reset DEBUG_FUNC event.
29
BE_SW_FUNC
Bidirectional Reset Enables for 'Functional' Reset SW_FUNC
0b - External reset pin is asserted on a 'Functional' reset SW_FUNC event if the reset is enabled.
1b - External reset pin is not asserted on a 'functional' reset SW_FUNC event.
28
—
Reserved
27
—
Reserved
26
—
Reserved
25
—
Reserved
24
—
Reserved
23
Reserved
Table continues on the next page...
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1241 / 5251


---
# 페이지 67

Table continued from the previous page...
Field
Function
—
22
—
Reserved
21
—
Reserved
20
BE_HSE_BOOT
_RST
Bidirectional Reset Enables for 'Functional' Reset HSE_BOOT_RST
0b - External reset pin is asserted on a 'Functional' reset HSE_BOOT_RST event if the reset is 
enabled.
1b - External reset pin is not asserted on a 'functional' reset HSE_BOOT_RST event.
19
—
Reserved
18
—
Reserved
17
—
Reserved
16
BE_HSE_SWT_
RST
Bidirectional Reset Enables for 'Functional' Reset HSE_SWT_RST
0b - External reset pin is asserted on a 'Functional' reset HSE_SWT_RST event if the reset is 
enabled.
1b - External reset pin is not asserted on a 'functional' reset HSE_SWT_RST event.
15
—
Reserved
14
—
Reserved
13
—
Reserved
12
BE_PLL_AUX
Bidirectional Reset Enables for 'Functional' Reset PLL_AUX
0b - External reset pin is asserted on a 'Functional' reset PLL_AUX event if the reset is enabled.
1b - External reset pin is not asserted on a 'functional' reset PLL_AUX event.
11
—
Reserved
Table continues on the next page...
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1242 / 5251


---
# 페이지 68

Table continued from the previous page...
Field
Function
10
BE_SWT3_RST
Bidirectional Reset Enables for 'Functional' Reset SWT3_RST
0b - External reset pin is asserted on a 'Functional' reset SWT3_RST event if the reset is enabled.
1b - External reset pin is not asserted on a 'functional' reset SWT3_RST event.
9
BE_JTAG_RST
Bidirectional Reset Enables for 'Functional' Reset JTAG_RST
0b - External reset pin is asserted on a 'Functional' reset JTAG_RST event if the reset is enabled.
1b - External reset pin is not asserted on a 'functional' reset JTAG_RST event.
8
BE_SWT2_RST
Bidirectional Reset Enables for 'Functional' Reset SWT2_RST
0b - External reset pin is asserted on a 'Functional' reset SWT2_RST event if the reset is enabled.
1b - External reset pin is not asserted on a 'functional' reset SWT2_RST event.
7
BE_SWT1_RST
Bidirectional Reset Enables for 'Functional' Reset SWT1_RST
0b - External reset pin is asserted on a 'Functional' reset SWT1_RST event if the reset is enabled.
1b - External reset pin is not asserted on a 'functional' reset SWT1_RST event.
6
BE_SWT0_RST
Bidirectional Reset Enables for 'Functional' Reset SWT0_RST
0b - External reset pin is asserted on a 'Functional' reset SWT0_RST event if the reset is enabled.
1b - External reset pin is not asserted on a 'functional' reset SWT0_RST event.
5
—
Reserved
4
BE_ST_DONE
Bidirectional Reset Enables for 'Functional' Reset ST_DONE
0b - External reset pin is asserted on a 'Functional' reset ST_DONE event if the reset is enabled.
1b - External reset pin is not asserted on a 'functional' reset ST_DONE event.
3
BE_FCCU_RST
Bidirectional Reset Enables for 'Functional' Reset FCCU_RST
0b - External reset pin is asserted on a 'Functional' reset FCCU_RST event if the reset is enabled.
1b - External reset pin is not asserted on a 'functional' reset FCCU_RST event.
2
—
Reserved
1
—
Reserved
0
—
Reserved
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1243 / 5251


---
# 페이지 69

33.8.6 Functional Reset Escalation Counter Register (FREC)
Offset
Register
Offset
FREC
14h
Function
This register provides the current value of functional reset escalation counter. It can be accessed in read/write, in supervisor mode. 
It can be accessed in read in the user mode. This register is reset by power-on reset, destructive reset, when you reconfigure the 
FREC field to Fh and when you write any value to the Functional Reset Escalation Threshold Register (FRET) register.
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
FREC 
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
31-4
—
Reserved
3-0
FREC
Functional' Reset Escalation Counter
This field provides the value of functional reset escalation counter.
33.8.7 Functional Reset Escalation Threshold Register (FRET)
Offset
Register
Offset
FRET
18h
Function
This register sets the threshold for 'functional' reset escalation to a 'destructive' reset. It can be accessed in read/write, either 
in supervisor mode. It can be accessed in read-only in the user mode. Writing a non-zero value to the FRET field enables 
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1244 / 5251


---
# 페이지 70

the 'functional' reset escalation function. Writing any value to this register resets the 'functional' reset escalation counter. See 
Functional reset escalation for details on the 'functional' reset escalation function. This register is reset on power-on and any 
'destructive' reset.
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
FRET 
W
Reset
0
0
0
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
Fields
Field
Function
31-4
—
Reserved
3-0
FRET
'Functional' Reset Escalation Threshold
If the value of this field is 0, the 'functional' reset escalation function is disabled. Any other value is the 
number of 'functional' resets that causes a 'destructive' reset.
33.8.8 Destructive Reset Escalation Threshold Register (DRET)
Offset
Register
Offset
DRET
1Ch
Function
This register sets the threshold for 'destructive' reset escalation to keeping the chip in the reset state until the next power-on reset 
triggers a new reset sequence. It can be accessed in read/write, either in supervisor mode. It can be accessed in read-only in the 
user mode. Writing a non-zero value to the DRET field enables the 'destructive' reset escalation function. Writing any value to 
this register resets the 'destructive' reset counter. See Destructive reset escalation for details on the 'destructive' reset escalation 
function. This register is reset only on power-on reset.
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1245 / 5251


---
# 페이지 71

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
DRET 
W
Reset
0
0
0
0
0
0
0
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
3-0
DRET
'Destructive' Reset Escalation Threshold
If the value of this field is 0, the 'destructive' reset escalation function is disabled. Any other value is 
the number of 'destructive' resets which keeps the chip in the reset state until the next power-on reset 
triggers a new reset sequence.
33.8.9 External Reset Control Register (ERCTRL)
Offset
Register
Offset
ERCTRL
20h
Function
This register allows software to control the assertion of External reset pin. It can be accessed in read/write, in supervisor mode. 
It can be accessed in read-only in the user mode. This register is reset on all resets.
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1246 / 5251


---
# 페이지 72

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
ERAS
SERT 
W
Reset
0
0
0
0
0
0
0
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
ERASSERT
ERASSERT
 
Setting ERASSERT to 1b also safe/pad states most of the chip's pins. See the IOMUX 
table/spreadsheet for each pin's safe/pad state value. Software must use the ERASSERT 
field for this purpose only as part of the main reset domain self-test entry procedure. Using 
it at any other time may result in unpredictable system behavior.
  NOTE  
0b - No change
1b - External reset is asserted
33.8.10 Reset During Standby Status Register (RDSS)
Offset
Register
Offset
RDSS
24h
Function
This register provides status of whether a reset event occurred during standby mode. Register bits are cleared on write '1'. This 
register is reset only on power-on reset.
 
On exiting a reset sequence after standby exit, the software must perform a read operation on 
MC_ME[PREV_MODE] and RDSS register. If any field of the RDSS register is set, the software must ignore the 
status reported by MC_ME[PREV_MODE] register otherwise the status of MC_ME[PREV_MODE] register reports 
the device status.
If MC_ME indicates last mode as RESET, then perform a reset exit in software else a standby exit.
  NOTE  
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1247 / 5251


---
# 페이지 73

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
FES_
RES 
DES_
RES 
W
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
31-2
—
Reserved
1
FES_RES
FES_RES
0b - No functional reset event occurred during standby mode.
1b - Functional reset event occurred during standby mode.
0
DES_RES
DES_RES
0b - No destructive reset event occurred during standby mode.
1b - Destructive reset event occurred during standby mode.
NXP Semiconductors
Reset Generation Module (MC_RGM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1248 / 5251


---