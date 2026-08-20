# 페이지 1

Chapter 31
Reset Overview
31.1 Introduction
This chip's reset logic consists of a reset sequence that leads the chip to a fixed deterministic state after predefined reset events 
occur. These events can pertain to chip failure events, the chip's special operating conditions, or certain software-governed events 
to initiate a chip reset sequence. This chapter discusses the chip reset scheme and related topics such as:
• Types of reset reactions
• Reset event sources
• Chip reset sequences
— POR
— Destructive reset
— Functional reset
• RAM retention across functional reset
• Reset pin (RESET_b) behavior
• Debug system reset
• Signal-level reset flow
31.2 Chip reset types and reactions
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1176 / 5251


---
# 페이지 2

31.2.1 Chip reset blocks
PMC
MDM_AP
SWT_0
SWT_2
FOSU
MC_PCU
RESET_b
MC_CGM
MC_ME
JTAGC
STCU2
FCCU
HSE_B
FIRC
MC_RGM
Present in S32K358 , 
S32K388, and S32K389
SWT_1
Not present in S32K312
and S32K311.
CMU_FC_[3:5]
CMU_FC_0
PLL
PLL_AUX
Present in S32K358,  
S32K388, and S32K389
SWT_3
Present in S32K388 
and S32K389
CMU_FC_6
Present in S32K388
and S32K389
Figure 137. Chip reset blocks
31.2.2 Chip reset types
Table 185. Chip reset types
Reset event type
Functional description
POR
Leads to a complete chip reset.
Destructive
Leads most parts of the chip, except a few modules, to reset. SRAM content is lost after this 
reset event.
Table continues on the next page...
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1177 / 5251


---
# 페이지 3

Table 185. Chip reset types (continued)
Reset event type
Functional description
Functional
Leads all the communication peripherals and cores to reset. The communication protocols' sanity 
is not guaranteed and they are assumed to be reinitialized after reset. The SRAM content, and 
the functionality of certain modules, is preserved across functional reset.
31.2.3 High-level reset sequence overview
Functional reset
entry sequence
Functional reset event
Chip out of reset
in Normal Run mode
Destructive reset
sequence
Destructive reset event
Power-on reset
sequence
In case of Standby mode, only the Run domain resets
and the exit from POR happens on Standby mode exit.
Power-on reset event
Standby entry sequence
Functional reset
asserts
Functional reset
exit sequence
Figure 138. High-level reset sequence overview
31.2.3.1
Reset event reactions
Table 186. Reset event reactions
Reset event type
Triggered from
Reaction
POR
Anywhere
Moves to the beginning of the power-on sequence
Destructive reset
Power-on sequence
No reset sequence change
Anywhere in the chip operation except in 
the power-on-sequence
Moves to the beginning of the destructive reset sequence
Functional reset
Out-of-reset
Moves to the beginning of the functional reset entry 
sequence
Anywhere within the functional reset 
sequence
No reset sequence change
31.2.3.2
Chip action after reset event
For each reset event, immediately after MC_RGM captures it, the chip performs these actions:
1. Writes 1 to the corresponding reset event status fields in MC_RGM.DES and MC_RGM.FES (see the MC_RGM chapter 
for more information).
2. Places its pins in their default states (see the IOMUX file attached to this document for more information).
3. Asserts the RESET_b pin.
 
After self-test completes, you can configure RESET_b assertion using MC_RGM.FES[ST_DONE].
  NOTE  
4. Enters the reset sequence as described in Reset event reactions, depending on the current state and reset event type.
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1178 / 5251


---
# 페이지 4

31.3 Reset sources—POR, destructive, and functional
MC_RGM records reset events in MC_RGM.FES and MC_RGM.DES, indicating the source of functional reset events and 
destructive reset events, respectively. You must read these fields to identify the reset source on reset recovery.
31.3.1 POR sources
Table 187. POR sources
Source module
Field in MC_RGM.DES
RESET_b assertion
Description
PMC
F_POR
Always
VDD_LV POR
LVR on 1.1 V supply in Standby mode
LVR on 1.1 V supply in Run mode
LVR on 2.5 V supply in Standby mode
LVR on 2.5 V supply in Run mode
LVR on VDD_HV_A supply in Standby mode
LVR on VDD_HV_A supply in Run mode
LVR on VDD_HV_B supply in Standby mode 1
LVR on VDD_HV_B supply in Run mode 1
POR_WDG
POR_WDG timeout (see the POR_WDG chapter 
for more information)
1. LVR on VDD_HV_B run mode and LVR on VDD_HV_B standby mode are not present in S32K312 and S32K311.
 
You cannot escalate or demote POR to an interrupt.
  NOTE  
31.3.2 Stages of the POR sequence
Table 188. Stages of the POR sequence
Stage
Process
PWRUP
1. Starts after a POR event (for example, a POR source assert).
2. Waits for the power-up sequence to complete.
3. Exits when all the POR sources clear.
4. Transitions to the FIRC_STRT stage after the procedure completes.
FIRC_STRT
1. Enters this stage after exiting the PWRUP stage.
 
FIRC_CLK, if enabled, becomes available after it is stable. The duration 
depends on the clock startup time (see the chip datasheet for more 
information). The MC_RGM state machine proceeds further after 
FIRC_CLK is available.
  NOTE  
2. Transitions to the destructive reset sequence after the procedure completes.
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1179 / 5251


---
# 페이지 5

31.3.3 Destructive reset sources
Table 189. Destructive reset sources
Source module1
Field in MC_RGM.DES
Description
FOSU
FCCU_FTR
FCCU failure to react
STCU2
STCU_URF
STCU2 unrecoverable fault
MC_RGM
MC_RGM_FRE
Functional reset escalation
CMU_FC_0
FXOSC_FAIL
FXOSC failure
PLL
PLL_LOL
PLL loss of lock
CMU_FC_3
CORE_CLK_FAIL
Core clock failure
CMU_FC_4
AIPS_PLAT_CLK_FAIL
AIPS_PLAT_CLK failure
CMU_FC_5
HSE_CLK_FAIL
HSE_CLK failure
CMU_FC_6
CM7_CORE CLK FAIL
CM7_CORE_CLK Failure
MC_CGM
SYS_DIV_FAIL
System clock dividers alignment failure
HSE_B
HSE_TMPR_R ST
HSE_B tamper detect reset
HSE_B
HSE_SNVS_RST
HSE_B SNVS tamper detection
MC_ME
SW_DEST
Software destructive reset
MDM_AP
DEBUG_DEST
Debug destructive reset
RESET_b pin
EXT_RST
RESET_b pin assertion
1. All destructive resets can be escalated, but only the PLL LOL destructive reset can be demoted to an interrupt (see 
Destructive reset event bypass for PLL LOL destructive reset bypass details).
 
All reset sources in the table above assert the RESET_b pin.
  NOTE  
31.3.4 Destructive sequence stage description
Table 190. DEST0 description
Stage
Process
DEST0
1. Asserts reset to the entire chip, except logic running on POR.
2. Waits for all the destructive reset events to clear.
3. Waits for the minimum destructive reset assertion duration of eight FIRC_CLK cycles.
4. Deasserts after stage completion.
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1180 / 5251


---
# 페이지 6

31.3.5 Functional reset sources
Table 191. Functional reset sources
Source module
Field in 
MC_RGM.FES
RESET_b assertion
Demotable to IRQ1
Escalation2
Description
FCCU soft 
reaction3
FCCU_RST
Always
Yes4
Yes
FCCU reset 
reaction
STCU2
ST_DONE
Configurable
No
No
Self-test done
SWT_0
SWT0_RST
Always
Yes5
Yes
SWT reset request
SWT_16
SWT1_RST
Always
Yes7
Yes
SWT reset request
SWT_28
SWT2_RST
Always
Yes9
Yes
SWT reset request
SWT_310
SWT3_RST
Always
Yes11
Yes
SWT reset request
PLL_AUX12
PLL_AUX_RST13
Always
Yes14
Yes
PLL reset request
JTAGC
JTAG_RST
Always
Yes 15
No
JTAG reset
HSE_B
HSE_SWT_RST
Always
No
Yes
HSE_B SWT 
timeout
HSE_B
HSE_BOOT_RST
Always
No
Yes
HSE_B boot reset
MC_ME
SW_FUNC
Always
No
Yes
Software 
functional reset
MDM_AP
DEBUG_FUNC
Always
Yes 16
Yes
Debug functional 
reset
1. See Functional reset demotion to an interrupt for more information.
2. See Reset escalation for more information.
3. An FCCU soft functional reset is a chip functional reset (see the FCCU chapter for more information).
4. Controlled by MC_RGM.FERD[D_FCCU_RST].
5. Controlled by MC_RGM.FERD[D_SWT0_RST].
6. SWT_1 is not present in S32K312, S32K311, S32K310, S32K348, S32K314, S32K341, S32K342, S32K344.
7. Controlled by MC_RGM.FERD[D_SWT1_RST].
8. SWT_2 is only present in S32K338/S32K388/S32K389.
9. Controlled by MC_RGM.FERD[D_SWT2_RST]
10. SWT_3 is only present in S32K388/S32K389.
11. Controlled by MC_RGM.FERD[D_SWT3_RST]
12. PLL_AUX is only present in S32K358, S32K388, and S32K389.
13. In order to use PLL_Aux as functional reset /interrupt source, the 24th bit of Functional Reset Register (DCMRWF2) should 
be configured.
14. Controlled by MC_RGM.FERD[D_PLL_AUX_RST]
15. Controlled by MC_RGM.FERD[D_JTAG_RST].
16. Controlled by MC_RGM.FERD[D_DEBUG_FUNC].
31.3.6 Functional reset sequence descriptions
Table 192. Functional reset sequence descriptions
Stage
Series of events
Functional reset entry sequences
FUNC0
This stage starts after any functional reset event.
Table continues on the next page...
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1181 / 5251


---
# 페이지 7

Table 192. Functional reset sequence descriptions (continued)
Stage
Series of events
The FCCU fault monitoring and CMU_Fx_n monitoring for FLL events is masked in this step to avoid any 
false fault or reset.
FUNC1
In this stage, a halt sequence that includes daisy chaining of all the gaskets halts, disabling the crossbar.
The stage completes after the halt-handshake sequence completes.
FUNC2
In this stage, MC_RGM triggers the MC_CGM hardware clock multiplexers to switch to FIRC_CLK.
• Software-based clock multiplexers do not support switching to FIRC_CLK on functional reset.
• If PCFS is enabled, the system clock switching can be done via PCFS.
This stage completes after MC_CGM switches the system clock to FIRC.
FUNC3
In this stage, MC_RGM triggers all the MC_CGM hardware-based clock multiplexers with PCFS enabled 
or disabled to move their dividers to default values.
• Software-based clock multiplexers do not support this feature.
This stage completes after all the clock multiplexer dividers initialize to their corresponding default values.
FUNC4
In this stage, PLLDIG turns off synchronously.
The stage completes after PLLDIG turns off.
FUNC5
FXOSC_CLK switches off synchronously.
The FUNC4 and FUNC5 stages ensure that PLLDIG disables cleanly to ensure there are no glitches on 
the PLLDIG clock because of reset.
The stage completes after FXOSC switches off.
FUNC6
In this stage, clocks of modules that are a part of LBIST and working on the destructive reset are enabled to 
meet their synchronous reset requirements, if any. For the self-test logic, in self-test, the destructive reset 
deasserts after this stage completes and after safe stating is removed.
 
In the self-test sequence, the logic, which is a part of self-test (LBIST logic) resets when 
self-test completes. All the parts of logic in self-test (POR, destructive, and functional 
reset) reset after self-test completes whereas the rest of the chip undergoes a functional 
reset sequence because of self-test completion (MC_RGM.FES[ST_DONE] = 1). See the 
"Safety Overview" and STCU2 chapters for more information on the self-test operation.
  NOTE  
FUNC7
MC_RGM asserts the functional reset and triggers a counter running on FIRC_CLK (for up to 64 cycles) 
to enable clocks for the modules having synchronous reset requirements.
Flash memory comes out of reset after this stage completes.
 
The flash memory resets after a functional reset event but comes out of reset, before the 
rest of the modules do, at the start of the functional reset exit sequence. The rest of the 
modules reset when the functional reset comes out of reset at the end of the functional 
reset exit sequence. Therefore, the reset to flash memory is an early functional reset that 
deasserts earlier than the functional reset, even if asserted at the same time.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1182 / 5251


---
# 페이지 8

Table 192. Functional reset sequence descriptions (continued)
Stage
Series of events
Functional reset exit sequences
FUNC8
This stage consists of flash memory and MC_RGM handshaking.
Flash memory indicates the completion of its initialization to MC_RGM.
FUNC9
DCM initiates the scanning of flash memory DCF records.
This state completes after the flash memory scanning completes. See the DCF clients file attached to this 
document for more information.
FUNC10
After DCM scans the DCF records from the flash memory, DCM initiates the trim loading sequence for 
analog blocks.
The analog blocks are loaded with the configured trimmed values in this stage, which completes after a 
trim-loading sequence completes.
FUNC11
In this stage, MG_RGM stops driving RESET_b and checks that the signal does not assert externally.
If you enable low-power debug, MC_RGM waits for a debug acknowledge.
The completion of this stage indicates that MC_RGM completed the reset sequence, deasserting the 
functional reset to the system.
31.4 Reset and boot sequence
The chip reset sequence consists of several reset stages based on the occurrence of a particular reset event. All reset events 
follow the same chip reset sequence; only the entry points vary depending on the type of reset event. MC_RGM triggers each stage 
after the previous stage completes. These stages execute in a specific order, which ensures a deterministic state of the chip when 
a reset event completes.
Figure 139 shows a high-level representation of the chip startup sequence.
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1183 / 5251


---
# 페이지 9

Chip power up
No
Keep chip in POR
Yes
FIRC powers on
Wait for FIRC stabilization
sBAF initialization code
sBAF enabling application core
Standby recovery initialization
HSE_FW enabling application core
Destructive reset
sequence proceeds
Functional reset
sequence proceeds
Move to application
V>VtPOR
HSE_FW verification
HSE_FW boot
Yes
Yes
Security functions disabled
Chip out of reset in normal Run mode
Security functions enabled
App core VTOR change
Flash memory initialization
Flash memory scanning
Trim loading
Change FIRC_DIV to DIV1
Enable FXOSC, PLLDIG (configurable)
Boot header parsing
XRDC configurations
CAAM_RNG initialization
Debug authorization
CAAM_RNG initialization
OS initialization
HSE_FW initialization code
Application boot
Legend:
Note: HSE_FW and application sizes are considered as 128 KB each
No
Standby
exit
No
RUN
Functional reset
Destructive reset
Power-on reset
Secure
boot?
Execute self-test
Application core
software
HSE_B sBAF
HSE_B firmware 
Hardware
Yes
No
Trigger
self-test?
Change MC_RGM.DRET to 0xF if it's '0'
Fast 
Stadby 
exit
Yes
Figure 139. Chip reset and boot overview
31.4.1 POR
This stage starts when the POR event occurs, that is, when a POR source asserts. The logic within the Run power domain running 
on POR also resets in the chip Standby entry sequence.
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1184 / 5251


---
# 페이지 10

 
The logic in the Standby power domain does not reset in the chip Standby mode entry sequence.
  NOTE  
The POR sequence consist of two stages:
1. Power-up (PWRUP)
2. FIRC oscillator start (FIRC_STRT)
See POR sequence for more information and Stages of the POR sequence for POR stages and their descriptions.
31.4.1.1
POR sequence
Power-on reset event
PWRUP
Assert reset to all domains.
Wait for complete power-up.
FIRC_STRT
Deassert POR and enable FIRC.
All POR
events
clear?
No
Yes
Destructive reset
sequence
FIRC_CLK
stable?
No
Yes
Figure 140. POR flow
31.4.2 Destructive reset
The chip enters a destructive reset sequence after the POR sequence or any destructive reset event completes. Destructive 
reset sequence illustrates the destructive reset sequence and Destructive sequence stage description discusses the stages of 
destructive sequence.
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1185 / 5251


---
# 페이지 11

31.4.2.1
Destructive reset sequence
POR sequence
Destructive reset event
Standby reset
sequence
Functional reset
sequence
All destructive reset events clear.
Minimum destructive reset assertion duration expires.
Destructive reset escalation threshold not exceeded.
DEST0
Assert reset all domains except POR and debug.
Wait for all destructive events to clear.
Wait for minimum destructive reset assertion duration.
In case of Standby mode, only the Run
domain resets and the exit from POR 
happens on Standby mode exit. 
Figure 141. Destructive reset sequence
31.4.2.1.1
Destructive sequence stage description
Table 193. DEST0 description
Stage
Process
DEST0
1. Asserts reset to the entire chip, except logic running on POR.
2. Waits for all the destructive reset events to clear.
3. Waits for the minimum destructive reset assertion duration of eight FIRC_CLK cycles.
4. Deasserts after stage completion.
31.4.2.2
Destructive reset event bypass
This chip supports a destructive reset event demotion mechanism that the application software configures. The destructive reset 
bypasses and an interrupt event occurs (demotion). Table 194 discusses details related to GPR configuration and corresponding 
interrupt identification.
A successful chip operation is not guaranteed if a destructive reset event is bypassed.
Table 194. Destructive reset event bypass
Destructive reset event
Destructive reset event 
description
DCM field to bypass reset event
NVIC interrupt 
ID
MC_RGM.DES[PLL_LOL]
PLL loss of lock
DCM.DCMRWP3[9]
212
31.4.3 Functional reset
The chip enters the functional reset sequence when any of the following events occur:
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1186 / 5251


---
# 페이지 12

• Functional reset
• POR or destructive reset (after the DEST0 stage completion)
On any functional reset event, the chip starts a functional reset entry sequence before the functional reset asserts and ensures 
the stability of logic running on a destructive reset and POR. On a destructive reset event or POR events the functional reset entry 
sequence does not execute.
The functional reset exit sequence consists of steps that ensure proper initialization of the chip after functional reset recovery.
31.4.3.1
Functional reset sequence
Functional reset flow illustrates the functional reset flow and Functional reset sequence descriptions discusses the functional reset 
stages and their descriptions.
Stages FUNC0 to FUNC6 present the functional reset entry sequence. It occurs on any functional reset event before the functional 
reset. In other words, when a functional reset event occurs, MC_RGM holds the asserted reset and executes the functional reset 
entry sequence. After the sequence completes, MC_RGM resets the chip, which remains in Run mode during the functional reset 
entry sequence.
Stages FUNC7 to FUNC11 present the functional reset exit sequence, which occurs after a functional reset event before 
deasserting the chip reset. This includes handshaking with the flash memory and analog blocks, ensuring correct operation after 
reset exit.
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1187 / 5251


---
# 페이지 13

31.4.3.1.1
Functional reset flow
FUNC0
Disable safety features
FUNC7
Assert functional reset
Revive system clock
Wait for 64 FIRC cycles
FUNC11
Stop driving RESET_b and
wait for debug acknowledge if
LP_DEBUG is enabled
Crossbar disable process completed
Clock switching to FIRC completed
Default clock configurations completed
PLL disabled
FXOSC disabled
Functional reset
event
FUNC1
Initiate crossbar disable
Minimum functional reset duration completed
FUNC2
Initiate PCFS
Switch clock to FIRC
Flash memory reset recovery process completed
FUNC8
Initiate flash memory reset
recovery handshake
Flash memory scanning completed
FUNC9
Initiate flash memory
scanning by DCM
Trim loading of analog modules completed
RESET_b pin deasserted
Debug acknowledge done for LP_DEBUG if enabled
FUNC10
Initiate trim loading
of analog modules
FUNC3
Initiate default clock configuration
FUNC4
Disable PLL
FUNC5
Disable FXOSC
FUNC6
Initiate sync reset clocks
Destructive
reset event
or sequence
Out
of
reset
Figure 142. Functional reset flow
31.4.3.2
FUNC9 and FUNC10 stage bypass for faster Standby mode exit
The chip supports optional bypassing of the FUNC9 and FUNC10 (only FIRC and PMC phases) stages on Standby mode exit 
to considerably reduce the Standby mode exit duration. This feature is recommended only for Standby mode exit and must be 
configured on:
• Standby mode entry sequence
• SW3
• Disabled on Standby mode exit
See the "Faster Standby recovery" section in the "Power Management" chapter for more information.
31.4.3.3
Standby reset sequence
The logic within Run domain is reset additionally apart from the reset sequence in the chip standby entry sequence, wherein all 
the resets assert (POR, destructive, and functional) to the Run domain logic. The chip standby entry sequence does not have any 
impact on the logic in Standby power domain.
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1188 / 5251


---
# 페이지 14

Wake-up from Standby mode removes the resets to the Run domain in the standby entry sequence.
See the "Peripheral reset status" section in the "Reset Overview" chapter for the logic present in Run domain.
31.4.3.4
Reset function redirection
Resets may escalate or demote to an IRQ, depending on the chip configuration.
31.4.3.4.1
Functional reset demotion to an interrupt
This chip supports the reset sequence demotion feature for functional resets. You can configure a functional reset to create an 
interrupt instead of a reset (see the MC_RGM chapter for details).
31.4.3.4.2
Reset escalation
The chip supports the reset escalation feature. If multiple functional or destructive resets occur, the related reset can escalate 
to a higher priority reset sequence (see the "Functional reset escalation" and "Destructive reset escalation" sections in the 
MC_RGM chapter).
31.4.3.4.2.1
Destructive reset escalation
You can enable destructive reset escalation by configuring a DCF client. You must also configure the destructive count threshold 
in MC_RGM.DRET (see "Destructive Reset Escalation Enable Register (DEST_RST_ESC):dcf_client_dest_rst_esc" in the DCF 
file attached to this document). The escalation event can individually be enabled or disabled for each reset source, and the fields 
in the dcf_client_dest_rst_esc register correspond with the fields in MC_RGM.DES register.
After being configured, MC_RGM immediately asserts a destructive reset escalation when the destructive event count reaches 
the threshold count in MC_RGM.DRET[DRET]. When the destructive and escalation reset assert, the reset sequence immediately 
enters the DEST0 state. The reset sequencing remains in DEST0 until a POR event occurs. If enabled, the destructive reset 
escalation counter increments with each destructive reset event. The application software clears the destructive reset escalation 
counter by writing any value to MC_RGM.DRET[DRET].
 
You can configure GPR settings to allow demotion of destructive resets to interrupts instead of escalation 
(DCMRWP3[DEST_RST9_AS_IPI]). See Destructive reset event bypass for more information.
  NOTE  
31.5 Reset timing diagram
b
c
FIRC trimming
i
b
j
FIRC startup and setting time
Power-on reset (active-low)
FIRC_CLK
Destructive reset (active low)
Flash memory reset (active-low)
Flash memory reset recovery done
Flash memory scanning start
Flash memory scanning complete
FIRC, PMC, ADC, TempSense, and so on
Start trim loading
Trim loading done
RESET_b
Functional reset (active-low)
≈ 20 FIRC cycles
e
f
Flash memory reset recovery time < 15 µs
g
h
k
l
m
Flash memory scanning time ≈ 10 µs
Analog modules (for example, FIRC) trimming
Trimming done
d
≈ 64 FIRC cycles
Reset pin goes high
Chip out of reset in Run mode
Figure 143. Reset timing diagram
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1189 / 5251


---
# 페이지 15

31.6 Chip status after reset deassertion
Table 195. Chip status after reset deassertion
Function or feature
After POR deassertion
After destructive 
reset deassertion
After functional reset deassertion
Clock sources
• FIRC_CLK and 
SIRC_CLK on
• Others off
• FIRC_CLK and 
SIRC_CLK on
• Others off
• FIRC_CLK and 
SIRC_CLK on
• SXOSC_CLK same as 
before functional reset
• FXOSC_CLK and 
PLL_PHIn_CLK off
Clock selection
FIRC_CLK
FIRC_CLK
FIRC_CLK
Clock dividers
Default configuration
Default configuration
Default configuration
Reset status flags
MC_RGM.DES[F_POR] equals 
1, others equal 0
MC_RGM.DES[F_DR_n] equals 
1, others equal 0
MC_RGM.FES[F_FR_n] equals 
1, others equal 0
MC_ME 
previous mode
Reset
Reset
Reset
FCCU 
fault information
Cleared
Cleared
Retained
SRAM content
Invalid
Invalid
Retained
DCF configurations 
in DCM
Reset value
Existing loaded value (reset 
value after POR)
Reloaded from flash memory
Cores
All off
All off
Cores initialized as per 
application configuration
Logic on POR1
Out of reset with 
default configuration
Out of reset with 
default configuration
Out of reset with 
default configuration
Logic on destructive 
reset 1
Under reset with 
default configuration
Out of reset with 
default configuration
Out of reset with 
default configuration
Logic on functional 
reset 1
Under reset with 
default configuration
Under reset with 
default configuration
Out of reset with 
default configuration
1. For the list of peripherals affected by POR, destructive reset, and functional reset events, see Module reset status.
31.7 Module reset status
Table 196. Module reset status
Module instances1
Destructive
Functional
Power domain2
Part of LBIST3
MC_RGM
Y
Y
Standby
No
PRAMC
Y
Y
Run
Yes
PFC
Y
Y
Run
Yes
SIUL_VIRTWRAPPER_PDAC0
Y
Y
Run
No
Table continues on the next page...
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1190 / 5251


---
# 페이지 16

Table 196. Module reset status (continued)
Module instances1
Destructive
Functional
Power domain2
Part of LBIST3
SIUL_VIRTWRAPPER_PDAC1
Y
Y
Run
No
SIUL_VIRTWRAPPER_PDAC2
Y
Y
Run
No
SIUL_VIRTWRAPPER_PDAC3
Y
Y
Run
No
SIUL_VIRTWRAPPER_PDAC44
Y
Y
Run
No
SIUL_VIRTWRAPPER_PDAC55
Y
Y
Run
No
DCM
Y
Y
Run and Standby6
No
TRGMUX
Y
Y
Run
No
WKPU
Y
Y
Standby
No
CMU_Fx_[0:5]
Y
Y
Run
CMU 0-3: No
CMU 1-2: Yes
CMU 4-5: Yes
FIRC
Y7
Y7
Standby
No
FXOSC
Y
Y
Standby
No
MC_CGM 8
Y
N
Run
No
MC_ME
Y
Y
Run
No
PLL
Y
Y
Run
No
PLL_AUX4
Y
Y
Run
No
Configuration GPR
Y
Y
Run
No
eMIOS 0-2
Y
Y
Run
No
PIT_0
Y
Y
Standby9
No
PIT_[1:2]
Y
Y
Run
No
PIT_[3]11
Y
Y
Run
No
FlexCAN_[0:5]
Y
Y
Run
No
FlexCAN_[6:7]4
Y
Y
Run
No
FlexCAN_[8:11]10
Y
Y
Run
No
FlexIO
Y
Y
Run
No
LPUART_[0:15]
Y
Y
Run
No
LPI2C_[0:1]
Y
Y
Run
No
LPSPI_[0:5]
Y
Y
Run
No
QuadSPI
Y
Y
Run
No
SAI_[0:1]
Y
Y
Run
No
uSDHC4
Y
Y
Run
No
ADC_[0:2]
Y
Y14
Run
No
Table continues on the next page...
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1191 / 5251


---
# 페이지 17

Table 196. Module reset status (continued)
Module instances1
Destructive
Functional
Power domain2
Part of LBIST3
LPCMP_[0:2]
Y
Y
Standby
No
TempSense
Y
Y14
Run
No
CRC
Y
Y
Run
Yes
FCCU (+FOSU)
Y
N
Run
Yes
STCU2
Y
N
Run
No
HSE_B MUA-MUB
Y
Y
Run
No
MU_2 MUA-MUB4
Y
Y
Run
No
MU_3 MUA-MUB11
Y
Y
Run
No
MU_4 MUA-MUB11
Y
Y
Run
No
JDC
Y12
Y12
Run
No
DMAMUX_[0:1]
Y
Y
Run
No
PMC
Y13
N
Standby
No
Flash memory
Y
Y14
Run
No
SIRC
Y7
Y7
Standby
No
SXOSC
Y15
N
Standby
No
BCTU
Y
Y
Run
No
LCU[0:1]
Y
Y
Run
No
RTC
Y
N16
Standby
No
EMAC
Y
Y
Run
No
GMAC4/GMAC_0
Y
Y
Run
No
GMAC_111
Y
Y
Run
No
HSE_B
Y
Y
Run
No
SWT_0
Y
Y
Standby
No
SWT_1
Y
Y
Run
Yes
SWT_24
Y
Y
Run
Yes
SWT_311
Y
Y
Run
Yes
STM_0
Y
Y
Run
No
STM_1
Y
Y
Run
No
STM_24
Y
Y
Run
No
STM_311
Y
Y
Run
No
MSCM
Y
Y
Run
No
ERM_0
Y
Y
Run
Yes
Table continues on the next page...
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1192 / 5251


---
# 페이지 18

Table 196. Module reset status (continued)
Module instances1
Destructive
Functional
Power domain2
Part of LBIST3
ERM_14
Y
Y
Run
Yes
EIM_0
Y
Y
Run
Yes
EIM_14
Y
Y
Run
Yes
EIM_24
Y
Y
Run
Yes
EIM_311
Y
Y
Run
Yes
eDMA
Y
Y
Run
Yes
JTAGC
N
N
Run
No
MDM_AP
Y
N
Run
No
APB_AP
Y
N
Run
No
Cortex-M7_0
Y
Y17
Run
No
Cortex-M7_1
Y
Y17
Run
No
Cortex-M7_24
Y
Y
Run
No
Cortex-M7_0 AHB-AP
Y
N
Run
No
Cortex-M7_0 AHB-AP
Y
N
Run
No
Cortex-M7_311
Y
Y
Run
No
MC_PCU
Y
N
Standby
No
Legends:
Y
The entire module resets on this particular reset.
Y
Only a portion of the module resets on this particular reset.
N
No portion of the module resets on this particular reset
1. All the modules listed in this table are reset on a POR event. See the memory map file attached to this document for the 
availability of modules across various parts in the S32K3xx family.
2. The modules in the RUN domain get reset on standby exit. The modules in STANDBY domain are not impacted by 
standby exit and retain their contents. However in case of standby exit via functional reset or destructive reset event, the 
corresponding flops within the STANDBY domain modules will also get reset.
3. The modules in the LBIST logic get reset on selftest completion.
4. Applicable for S32K358, S32K388, and S32K389 only.
5. Applicable for S32K388 and S32K389 only.
6. Flash memory scanning logic is available in the Run domain. GPRs and LC decode logic are available in Standby domain.
7. All memory-mapped registers are on functional reset. The trimming logic is on destructive reset. Rest of counter and other 
stuff is on POR.
8. During functional reset stages FUNC2 and FUNC3 (see the Functional reset sequence descriptions for functional reset 
stage descriptions), MC_CGM.MUX_n_CSC and MC_CGM.MUX_n_DIV_m are automatically set to their default values. 
The default value of the MC_CGM.MUX_n_CSC[SELCTL] selects FIRC_CLK as the source clock for all multiplexers. The 
default value of the MC_CGM.MUX_n_DIV_m is register instance specific (see the "MC_CGM register descriptions" section 
in the "Clock Generation Module (MC_CGM)" chapter).
9. Only PIT_0 supports the RTI feature, and exists in the Standby domain.
10. Applicable for S32K389 only.
11. Applicable for S32K388 and S32K389 only
12. The system domain is reset on functional reset. A POR will reset it completely.
13. PMC registers are reset on a destructive reset except PMC.LVSC, which is reset only by own PMC.LVSC[PORF] flag. The 
LVR and POR logic is reset on an LVR or own PORF (see PMC.CONFIG and PMC.LVSC descriptions for details).
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1193 / 5251


---
# 페이지 19

14. Reset on a functional reset; however, reset recovery occurs before the chip functional reset recovery, at the functional 
reset exit sequence start, for proper trim scanning and loading.
15. SXOSC is reset on a destructive reset so that the RTC operates properly across a functional reset.
16. RTC operates during a functional reset.
17. The functional reset maps to nSYSRESET to Arm Cortex-M7 and the destructive reset maps to nPORESET to Arm 
Cortex-M7. See the Cortex-M7 TRM for further description on part of logic on different domains within Cortex-M7.
31.8 System RAM retention across functional reset
System RAM retains content during functional reset through the crossbar halt handshake. The system crossbar halts during the 
functional reset entry sequence. Therefore, the accesses do not cause any content corruption (see Functional reset sequence for 
more information).
Follow this sequence for the crossbar halt handshake (see Halt handshake using the daisy-chaining method for gasket locations):
1. Send a halt request to the HSE_B AXBS, DMA AXBS, and EMAC IAHB bridges in parallel.
2. Wait for a halt acknowledgement from HSE_AXBS and DMA AXBS.
3. Send a halt request to the DMA IAHB and HSE_B IAHB gaskets.
4. Wait for a halt acknowledgement from all the gaskets listed in the aforementioned steps.
5. Send a halt request to the system AXBS.
6. Wait for a halt acknowledgement from the system AXBS.
7. Send a halt request to a peripheral AXBS.
8. Wait for a halt acknowledgement from a peripheral AXBS.
9. Send a halt request to the TCM IAHB and QSPI IAHB gaskets.
10. Wait for a halt acknowledgement from all the gaskets listed in the aforementioned steps.
11. Send a halt request to the AIPS0 IAHB and AIPS1 IAHB gaskets.
12. Wait for a acknowledgement from all of the gaskets listed in the aforementioned steps.
13. Send a halt request to TCM AXBS.
14. Wait for a halt acknowledgement from TCM AXBS.
 
AXBS halt handshake sequence is automatically performed by the hardware.
  NOTE  
After this halt sequence completes, the crossbar halt acknowledgement sequence also completes and the chip proceeds to the 
FUNC1 stage in the functional reset entry sequence.
 
RAM retention is supported across the functional reset event for system RAMs only and not for HSE_B or 
peripheral memories.
  NOTE  
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1194 / 5251


---
# 페이지 20

31.8.1 Halt handshake using the daisy-chaining method
PLL=240/160 MHz
8-40 MHz FXOSC
DIV
DIV
DIV
160 MHz 120 MHz 80 MHz
Cortex-M7_0
Primary core
Optional lockstep
XHB400
MPU
NVIC
FPU
DSP
64-bit
32-bit
32-bit
Decoupled = 0
Lockstep = 1
AHBS
32-bit
AXI
64-bit
AHBP
32-bit
M0
AXBS_Lite
S0
S1
0
1
ADDR
GEN
RDATA
CHK
wDATA
GEN
M0
M4
M3
M2
M1
M0
M3
M1
S0
S1
S2
M2
S2
S6
S3
System AXBS
64-bit @ 160 MHz
Peripheral AXBS
64-bit @ 160 MHz
S5
S0
Decoupled = 0
Lockstep = 1
64-bit
32-bit
32-bit
0
1
0
1
AHB
32-bit
0
1
0
1
0
1
MDAC0
S4
MRC0
P0
P2
P1
64-bit + ECC
PFLASH
x256
32 MHz
S1
ADDR
GEN
RDATA
CHK
wDATA
GEN
ADDR
GEN
RDATA
CHK
wDATA
GEN
ADDR
GEN
RDATA
CHK
wDATA
GEN
ADDR
CHK
RDATA
GEN
wDATA
CHK
* ECC data and address encode
ADDR
CHK
RDATA
GEN
wDATA
CHK
Cortex-M7_1
Secondary
(checker’s) core
XHB400
MPU
NVIC
FPU
DSP
AHBS
32-bit
AXI
64-bit
AHBP
32-bit
ADDR
GEN
RDATA
CHK
wDATA
GEN
MDAC4
1:2 32:64
MDAC5
EMAC
PLAT_AIPS_CLK
CORE_CLK
ADDR
GEN
RDATA
CHK
wDATA
GEN
MDAC1
eDMA3
32ch
HSE_CLK
AHB
64-bit
1:1
bypass
PRAM0
64-bit + ECC*
64-bit + ECC*
160 KB
160 KB
SRAM0
SRAM1
ADDR
CHK
RDATA
GEN
ADDR
CHK
LEGEND 
INTERNAL USE ONLY
IPBUS
Fixed gaskets
ECC gaskets
Configurable
gaskets
AHB32
AHB64
AXI64
APB v3
RDATA
GEN
ADDR
CHK
RDATA
GEN
MRC1
1:1 64:32
AHB
splitter
QSPI AHB
DATA
& CODE
x72
x72
XBIC
XBIC
AXBS (64-bit)
AXBS_Lite (64-bit)
120 MHz
XBIC
MRC2
2:1
XBIC
On platform
Peripherals
MU HSE_0
Off platform
Peripherals
On platform
Peripherals
MU HSE_1
MU_A
MU_B
Off platform
Peripherals
PDAC1
PDAC2
2:1
2:1
ADDR
CHK
RDATA
GEN
wDATA
CHK
ADDR
CHK
RDATA
GEN
wDATA
CHK
ADDR
CHK
RDATA
GEN
wDATA
CHK
AIPS1
AIPS2
D-FLASH
128 KB
ADDR
CHK
RDATA
GEN
wDATA
CHK
ADDR
CHK
RDATA
GEN
wDATA
CHK
ADDR
CHK
RDATA
GEN
wDATA
CHK
ADDR
GEN
RDATA
CHK
wDATA
GEN
ADDR
CHK
RDATA
GEN
wDATA
CHK
C-FLASH
C-FLASH
1 MB
1 MB
MDAC3
HSE
CM0+
AHB
64-bit
ADDR
GEN
RDATA
CHK
wDATA
GEN
1:2
AHB
splitter
AHB_32_64
AHB_32_64
I-CACHE
D-CACHE
8 KB
8 KB
I-CACHE
D-CACHE
8 KB
8 KB
I-TCM
32 KB
D-TCM
32 KB
D-TCM
32 KB
I-TCM
32 KB
D-TCM
32 KB
D-TCM
32 KB
PDAC0
Fast off platf.
Peripherals
AIPS0
P0
PRAM1
P0
Figure 144. Halt handshake using the daisy-chaining method
31.9 Pad state during reset and after reset
SIUL2 controls the GPIO functionality. It sets to its default state on a functional reset, and ensures that every pad initializes to its 
default state (see the default configurations and reset states of the chip's GPIO in the IOMUX file attached to this document).
31.10 Reset pin
This chip contains a bidirectional reset pin (RESET_b) indicating the reset state. RESET_b multiplexes with the other functions 
on port PTA5 (see the IOMUX file attached to this document).
The DCF configuration controls the multiplexing capabilities of RESET_b. The default configuration of the RESET_b port is that of 
a dedicated reset signal (for example, not multiplexed. See the DCF clients file attached to this document for more information).
The RESET_b pin offers the following uses if you configure it for the reset functionality:
• Acts as an external destructive reset source
• Acts as an indicator for the chip reset sequence for both functional and destructive reset sequences
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1195 / 5251


---
# 페이지 21

 
MC_RGM.FES[F_EXR] captures an externally sourced RESET_b assertion for a destructive reset.
  NOTE  
The RESET_b pin also indicates an internally asserted reset to external modules. It has a weak internal pullup. In normal Run 
mode, it keeps the chip out of reset.
31.10.1 Reset pin control during self-test
You can write 1 to MC_RGM.ERCTRL[ERASSERT] to assert RESET_b (writes only in Supervisor mode), before LBIST or MBIST 
executes. MC_RGM then asserts RESET_b and tristates the GPIO pins placing them in a safe state. Tristating GPIO ensures 
a safe state for the chip pins when LBIST or MBIST executes. Following BIST, the chip executes a reset sequence. The chip 
configures again for the application software, before executing the safety function. MC_RGM.ERCTRL[ERASSERT] clears on a 
functional reset. See Figure 8 for an illustration.
 
Writing 1 to SIUL2.MSCRn[SMC] enables the GPIO pins and the chip continues its normal I/O functionality.
  NOTE  
Initiate self-test
Configure self-test
Write
MC_RGM.ERCTRL[ERASSERT]
Figure 145. Reset pin control before self-test
Multiple chip configuration scenarios cause RESET_b to react differently after self-test completion:
• You can write 1 to MC_RGM.ERCTRL[ERASSERT] causing RESET_b to assert. This assertion does not impact the reset 
sequence, and the reset indicates that the chip is not available in Functional mode (although the chip is not in reset sequence).
Reset
Run
Chip operation mode
MC_RGM.ERCTRL[ERASSERT]
RESET_b
Run
Reset
Reset
Self-test configuration
Normal application run
Reset after self-test
Self-test
Figure 146. Reaction when MC_RGM.ERCTRL[ERASSERT] = 1
• If MC_RGM.ERCTRL[ERASSERT] = 0 (the default value), the RESET_b pin goes low after self-test completes. After self-test, 
the chip undergoes a functional reset in which the chip hardware writes 0 to MC_RGM.ERCTRL[ERASSERT]. The RESET_b 
pin goes high after the reset deasserts.
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1196 / 5251


---
# 페이지 22

Reset
Run
Chip operation mode
MC_RGM.ERCTRL[ERASSERT]
RESET_b
Run
Reset
Reset
Self-test configuration
Normal application run
Reset after self-test
Self-test
Figure 147. Reaction when MC_RGM.ERCTRL[ERASSERT] = 0
• If MC_RGM.ERCTRL[ERASSERT] = 0 (the default value), but you write 1 to MC_RGM.FBRE[ST_DONE], the RESET_b pin 
does not assert after self-test completes.
Reset
Run
Chip operation mode
MC_RGM.ERCTRL[ERASSERT]
RESET_b
Run
Reset
Reset
Self-test configuration
Normal application run
Reset after self-test
Self-test
Figure 148. Reaction when MC_RGM.ERCTRL[ERASSERT] = 0 and MC_RGM.FBRE[ST_DONE] = 1
31.11 Reset control in Lockstep mode
In Lockstep mode, a two-cycle delayed lockstep implementation controls the reset to both the application cores, Cortex-M7_0 and 
Cortex-M7_1. This lockstep implementation means Cortex-M7_0 starts two clock cycles before Cortex-M7_1. You can configure 
the dcf_client_utest_misc[LOCSTEP_EN] field to control the lockstep (see the DCF clients file attached to this document for 
more information).
The Cortex-M7 cores consist of two reset domains:
• PORESETn (see PORESETn control in Lockstep mode)
• SYSRESETn (see SYSRESETn control in lockstep)
.
 
Lockstep feature is available in S32K341, S32K342, S32K344, S32K348, S32K358, S32K388, and S32K389. For 
all these variants, Cortex-M7_0 and Cortex-M7_1 are split lock capable. For S32K388 and S32K389, Cortex-M7_2, 
Cortex-M7_2 checker are in permanent lockstep.
  NOTE  
31.11.1 PORESETn control in Lockstep mode
PORESETn includes debug modules that work across chip warm resets. The PORESETn domain resets on any destructive 
reset event. PORESETn deasserts after two cycles of reset deassertion synchronization delay, as soon as destructive reset 
sequence exits. In Lockstep mode, the reset deassertion to Cortex-M7_1 is further delayed by two CORE_CLK cycles as shown 
in PORESETn control in Lockstep mode.
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1197 / 5251


---
# 페이지 23

31.11.1.1
PORESETn control in Lockstep mode
RSL
Cortex-M7_1 PORESETn
Lockstep enable
(from UTEST_DCF_MISC_CLIENT)
clk
D
Q
RSL
Destructive reset
CORE_CLK
Two-cycle lockstep
Cortex-M7_0 PORESETn
clk
D
Q
clk
D
Q
Figure 149. PORESETn control in Lockstep mode
31.11.2 SYSRESETn control in lockstep
Most of the components within the Cortex-M7 cores reside in the SYSRESETn domain, except the debug modules. These 
components reset on any functional reset event. The SYSRESETn reset remains gated even if it exits the functional reset until 
MC_ME.PRTN0_COREn_PCONF[CCE] enables the core clocks. The debugger can hold the core's SYSRESETn domain in 
reset, as described in section "Application core debug from first instruction" in the "Debug Subsystem" chapter.
After a chip's functional reset deasserts, the core clocks are functional, and there is no gating from the debugger, the application 
core's SYSRESETn is released after a two-cycle reset deassertion synchronizer delay. In Lockstep mode, the reset deassertion 
to Cortex-M7_1 is delayed by two CORE_CLK cycles, as shown in SYSRESETn control in Lockstep mode.
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1198 / 5251


---
# 페이지 24

31.11.2.1
SYSRESETn control in Lockstep mode
RSL
Cortex-M7_1 SYSRSTn
Lockstep enable
(from UTEST_DCF_MISC_CLIENT)
clk
D
Q
RSL
Two-cycle lockstep
8 cycle delay*
8 cycle delay*
dbg_pwrup_req
dbg_pwrup_req
Functional reset
CORE_CLK
SDA_AP[RST_RELEASE_CM7_0]
(Reset value=1)
CCTL_CM7_0
PRTN0_CORE0_PCONF[CCE] in MC_ME
(Reset value=0)
SDA_AP[RST_RELEASE_CM7_1]
(Reset value=1)
CCTL_CM7_1
PRTN0_CORE1_PCONF[CCE] in MC_ME
(Reset value=0)
CORE_CLK
Functional reset
Cortex-M7_0 SYSRSTn
clk
D
Q
clk
D
Q
clk
D
Q
clk
D
Q
clk
D
Q
clk
D
Q
Figure 150. SYSRESETn control in Lockstep mode
31.12 Glossary
DCF
Device configuration format
POR
Power-on reset
NXP Semiconductors
Reset Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1199 / 5251


---