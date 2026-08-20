# 페이지 181

Chapter 61
Low Power Comparator (LPCMP)
61.1 Chip-specific LPCMP information
61.1.1 Instantiation information
Table 352. LPCMP instances
Chip
Instance
No. of external inputs
S32K388/S32K389/S32K358/S32K348/
S32K338/S32K328/S32K344/S32K324/
S32K314
LPCMP_0
8
LPCMP_1
4
LPCMP_2
4
S32K312/S32K342/S32K322/S32K341
LPCMP_0
8
LPCMP_1
4
S32K311/S32K310
LPCMP_0
8
61.1.2 LPCMP input output connections
See the IOMUX file attached to this document for pin/pad assignments corresponding to CMP pins.
The LPCMP channels can be used as a wakeup source in trigger mode to wakeup the device from standby mode.
61.1.3 LPCMP-DAC "vrefh0" and "vrefh1" references
The 8-bit DAC sub-block supports selection of "vrefh0" and "vrefh1" by CMPx_DCR[VRSEL]. For this device, the references are 
connected as follows:
• vrefh0 (External Reference): VDD_HV_A
• vrefh1 (Internal Reference): 1.2 V PMC bandgap reference
 
1.2 V internal reference voltage is not available in Standby mode.
  NOTE  
61.1.4 LPCMP window control
The window mode operation of all the comparator instances in the chip can be enabled/disabled by the TRGMUX. See the 
TRGMUX connectivity file attached to this document for details.
 
Window signal must be of minimum 4 cycle pulse for window mode to function.
  NOTE  
61.1.5 Comparator Trigger Mode
The comparator modules in the device support trigger mode operation as described in 'Trigger Mode' section. Device can operate 
in trigger mode in both standby and run mode to continuously scan the input channels. The main features of the device trigger 
mode operation are:
• Round robin clock: RTC_CLK
• Round robin trigger source: RTC_API
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2490 / 5251


---
# 페이지 182

 
• It must be ensured that the RTC_CLK period is greater than the comparison time corresponding to the value 
of C0[PMODE]. It is also required to not select the internal reserved channels, if available on the package, for 
trigger mode operation by INPSEL and INNSEL. See the IOMUX file attached to this document for the pins 
available in various packages supported for the device.
• Only SIRC and SXOSC are supported as RTC_CLK for trigger mode operation. The LPCMP initialization 
delay is not supported by RRCR0[RR_INITMOD] with FXOSC or FIRC as RTC_CLK.
• In run mode, the generated trigger is delayed by 3 RTC_CLK cycles before being given to comparator 
trigger input.
• When used in Round Robin mode, the LPCMP outputs the enable signal of the comparator on CMPx_RRT 
pin, on each cycle of comparator circuit. See the IOMUX file attached to this document for the pins on which 
CMPx_RRT functions are available.
  NOTE  
61.1.6 Interaction with RTC API to cause wakeup
LPCMP can be used for waking up the chip from standby. For this, RTC-API and LPCMP must be configured before entering into 
standby mode as per below shown figure.
 
Enter into STANDBY mode
 
Configure CMPx for round robin operation
Configure CMP_x.RRCR0[RR_EN] to put CMP_x 
in trigger mode/round robin mode and configure 
RTC.APIVAL  for trigger mode/round robin period
No
Compares
INP > INM
Device stays in STANDBY mode
and CMP_x waits for next trigger.
Sample the configured inputs 
and stores the results
Yes
 
Software
 
CMP
 
RTC-API
Wakeup from STANDBY mode
On time-out, RTC-API sends a 
trigger to CMP_x to start round
robin operation periodically
Figure 262. LPCMP-RTC interaction
In the trigger mode operation, only the continuous mode is supported. None of the window/filter/sample functions should be used. 
Refer to the "Functional Modes" section for details on comparator modes of operation.
Register configurations before entering Standby mode for LPCMP trigger mode operation: 
1. Configure RTC.APIVAL to set the period of the round robin operation.
2. Execute standby mode entry.
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2491 / 5251


---
# 페이지 183

61.2 Overview
The LPCMP module provides a circuit to compare two analog input voltages. It includes the following:
• A low power comparator (CMP)
• A DAC
• An analog mux (ANMUX)
See Block diagram for more information.
LPCMP can operate across the full range of the supply voltage, known as rail-to-rail operation.
DAC is a 256-tap resistor ladder network that provides a selectable voltage reference for applications requiring a voltage 
reference. DAC divides the supply reference Vin into 256 voltage levels. An 8-bit digital signal input selects the output voltage level, 
which varies from Vin to Vin/256.
You can select Vin from the following voltage sources:
• VREFH0
• VREFH1
See the Chip-specific LPCMP information for more information on source of VREFH0 and VREFH1.
 
The LPCMP's internal DAC output is available as an on-chip internal signal only and is not available for an external 
chip pin.
  NOTE  
ANMUX allows you to select an analog input signal from among eight channel options. One channel option is the DAC output. 
Other chip resources are connected to the other channels. See the Chip-specific LPCMP information section for more information. 
ANMUX can operate across the full range of the supply voltage.
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2492 / 5251


---
# 페이지 184

61.2.1 Block diagram
0
1
MUX
MUX
Vin
Resistor
ladder
VRSEL
vrefh1
vrefh0
DCR[DAC_DATA]
DCR[DAC_EN]
DAC output
RR_ACTIVE
DAC
Input channel 0
Input channel 1
Input channel 2
Input channel 3
Input channel 4
Input channel 5
ANMUX
INP
INM
CMP
CMP
DMA_REQ
IRQ
CMPO
Input channel 6
Input channel 7
PMUX
INPMUX
INMMUX
RRCR0
[RR_EN]
RRCR1
[RR_CHxN]
RRCR1
[FIXCH]
CCR2[PSEL]
Round-
robin
switch
1
0
CCR2[INPSEL]
000
MMUX
001
010
011
100
101
110
111
CCR2[MSEL]
RRCR0
[RR_EN]
From
round-robin
switch
Window
and
filter control
SAMPLE/WINDOW input
000
001
010
011
100
01
00
0
1
01
00
101
110
111
CCR2[INMSEL]
Round-
roubin
FSM
Figure 263. Block diagram
61.2.2 Features
The features of the LPCMP module include：
• Includes two 8-to-1 channel MUXes to select input signal from eight channels
• Supports multiple operation modes to produce a wide range of outputs such as:
— Sampled
— Windowed, which is ideal for certain PWM zero-crossing-detection applications
— Digitally filtered
• Provides the following advance features for window and sample:
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2493 / 5251


---
# 페이지 185

— Window and sample signals can be inverted.
— CMPO rising, falling or both edges closes the window.
— CMPO level can be defined when window is closed.
• Provides selectable performance levels:
— Low-Power (speed) mode
— High-Power (speed) mode
• Supports programmable hysteresis control
• Provides a selectable inversion on comparator output
• Uses an external hysteresis at the same time the output filter is used for internal functions
• Provides interrupt and DMA support
• Supports Round Robin Trigger mode
• Includes an 8-bit resolution DAC
• Provides a selectable supply reference source for DAC
61.3 Functional description
61.3.1 Functional block diagram
 
COUT_INV
COUT
WINDOW_EN
CCR1[COUT_SEL]
+
-
HYSTCTR
FILT_CNT
CFR/F_IE
CCR1[SAMPLE_EN]
DMA_REQ
IRQ
Interrupt
/DMA 
Control
DMA_EN
Divided Bus Clock
CMPO to PAD
CFR/F
COUT
To other SOC functions
COUT_PEN
To open PAD for CMPO
Sampling Clock
Window
Control
Polarity
Select
Filter
Block
Clock
Prescaler
Bus Clock
CCR1[FILT_PER]
COUT_RAW
 
 
Internal Bus
INP
INM
WINDOW/SAMPLE
COUTA
1
0
1
0
CMP_EN
CMP_HPMD
CMP_NPMD
Figure 264. Functional block diagram
As shown in the block diagram, the functions are:
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2494 / 5251


---
# 페이지 186

• Compared two analog input voltages applied to INP and INM, COUT_RAW is high when the INP input voltage is greater 
than the INM input voltage, and COUT_RAW is low when the INP input voltage is less than the INM input voltage.
• The COUT_RAW signal can be inverted by enabling CCR1[COUT_INV].
• The optionally inverted comparator output COUT_RAW is sampled on every bus clock when you enable the 
CCR1[WINDOW_EN] to generate COUTA. In this case, the comparator output is ignored during time periods when the input 
voltages are not valid. This is useful when you implement zero-crossing-detection for certain PWM applications.
• The window control block is bypassed when CCR1[WINDOW_EN] is disabled.
• The filter block acts as a simple sampler when CCR1[FILT_CNT] is set to 01h.
• The filter block acts as a filter based on multiple samples when CCR1[FILT_CNT] is set to be greater than 01h.
— If CCR1[SAMPLE_EN] is set to 1, use the external SAMPLE input as the sampling clock.
— If CCR1[SAMPLE_EN] is set to 0, use the divided bus clock as the sampling clock.
• Bypasses the filter block when it is not in use.
Bypass_Filter_Block = (FILT_CNT == 0x00) |  (~SAMPLE_EN & (FILT_PER == 0x00))
• Both COUTA and COUT can be configured as module output CMPO by configuring CCR1[COUT_SEL], and are used for 
different purposes within the system.
• The optionally filtered COUT can be read directly in CSR[COUT].
• The SAMPLE/WINDOW signal can be inverted by setting CCR1[WINDOW_INV].
• The SAMPLE/WINDOW signal can be closed by CMPO's falling edge and/or rising edge by setting CCR1[WINDOW_CLS] 
in Window mode.
• In Window mode, when window is closed, define the COUTA value as CCR1[COUTA_OW] by setting 
CCR1[COUTA_OWEN]. If CCR1[COUTA_OWEN] is not set, COUTA holds the last sampled value.
 
See the chip configuration section for the source of SAMPLE/WINDOW input.
  NOTE  
61.3.2 Round-robin trigger mode
You can enable Round-Robin Trigger mode by setting RRCR0[RR_EN] and CCR0[CMP_EN] to 1. A trigger event initiates a 
comparison sequence. The next trigger event should not occur before the current sequence completes.
RRCR1[FIXP] and RRCR1[FIXCH] select the reference channel for the plus side mux or the minus side mux. 
RRCR1[RR_CHnEN] selects active channels.
When a trigger comes, the analog comparator enables. After the comparison sequence completes, the analog comparator 
disables again. RRCR0[RR_INITMOD] controls the analog stabilization time.
 
RR_INITMOD*round robin clock period must be longer than the initialization delay specified in the Comparator and 
8-bit DAC electrical specifications section of LPCMP datasheet.
  NOTE  
After the stabilization process completes, the round robin manner comparison sequence begins. Sample the comparison result 
for the selected active channel after RRCR0[RR_NSAM] defines the configurable number of operation clocks.
After all the active channels are sampled/compared, if the comparison result changes from its pre-programmed state, the 
corresponding flag in RRSR[RR_CHnF] is set. Write to RRCSR[RR_CHnOUT] to configure the pre-programmed state for each 
channel. Update RRCSR[RR_CHnOUT] to store the last comparison result for each channel. If any flag in RRSR[RR_CHnF] sets, 
CSR[RRF] also sets. If IER[RRF_IE] sets, an asynchronous interrupt asserts. Note that these flags do not support generating a 
DMA transfer event.
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2495 / 5251


---
# 페이지 187

The following diagram shows the basic flow of this mode. In the diagram, RRCR1[RR_CH1EN], RRCR1[RR_CH3EN], and 
RRCR1[RR_CH4EN] are 1, so channels #1, #3, and #4 are selected for round-robin depending on their priority setting. 
RRCR0[RR_NSAM] sets to 2'b01, so you can sample one clock later the comparison result of the selected channel. After you 
compare the channel #4, the result is sampled, and round-robin ends. If any of the comparison results from channel #1, #3, or #4 
changed from their programmed value (written to RRCSR[RR_CH1OUT], RRCSR[RR_CH3OUT], and RRCSR[RR_CH4OUT]), 
generates an interrupt. Software can then poll RRSR[RR_CHnF] to see which channel input(s) changed value.
IDLE
CH1
CH3
CH4
Round Robin Clock
Round Robin Trigger
Round Robin Start
CMP (and possible DAC) Enable
RR_ACTIVE
Active Channel Select State 
Sample Channel
Comparision Result 
RR_CH1OUT
RR_CH1/3OUT
RR_CH1/3/4OUT
Channel Results 
Possible Interrupt 
RR_INITMOD
NSAM
NSAM
NSAM
Figure 265. Trigger mode
The table below shows the channel decode in both Functional mode and Trigger mode. Other cases not in the table are illegal.
Table 353. CMP channel decode in functional mode and round-robin trigger mode
Mode
RR_E
N
PSEL[2:
0]
MSEL[2:
0]
INPSEL[1:
0]
INMSEL[1
:0]
FIX
P
FIXCH[2
:0]
RR_CH
xN
INP
INM
CMP 
Behavior
Function
al mode
0
x1
0 to 7
0
1
x
x
x
DAC
Channel 
decoded 
from 
MSEL[2:
0]
Channel 0 
to 7 can be 
compared 
with DAC
Table continues on the next page...
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2496 / 5251


---
# 페이지 188

Table 353. CMP channel decode in functional mode and round-robin trigger mode (continued)
Mode
RR_E
N
PSEL[2:
0]
MSEL[2:
0]
INPSEL[1:
0]
INMSEL[1
:0]
FIX
P
FIXCH[2
:0]
RR_CH
xN
INP
INM
CMP 
Behavior
0 to 7
x
1
0
x
x
x
Channel 
decoded 
from 
PSEL[2:0
]
DAC
Channel 0 
to 7 can be 
compared 
with DAC
0 to 7
0 to 7
1
1
x
x
x
Channel 
decoded 
from 
PSEL[2:0
]
Channel 
decoded 
from 
MSEL[2:
0]
Channel 0 
to 7 can be 
compared 
with 
channel 0 
to 72
Trigger 
mode
1
x
x
0
1
0
x
0 to 7
DAC
Channel 
sweep 
(RR_CHx
N)
Channel 0 
to 7 can be 
swept with 
DAC
x
x
1
0
1
x
0 to 7
Channel 
sweep 
(RR_CHx
N)
DAC
Channel 0 
to 7 can be 
swept with 
DAC
x
x
1
1
0
0 to 7
0 to 7
Channel 
fixed by 
FIXCH[2:
0]
Channel 
sweep 
(RR_CHx
N)
Channel 0 
to 7 can be 
swept with 
a fixed 
channel(0 
to 7)3
x
x
1
1
1
0 to 7
0 to 7
Channel 
sweep 
(RR_CHx
N)
Channel 
fixed by 
FIXCH[2:
0]
Channel 0 
to 7 can be 
swept with 
a fixed 
channel(0 
to 7)3
1. "x" means "don't care"
2. PSEL should not be same as MSEL.
3. Channel in the sweep side should not be same as the fixed side.
61.3.3 Low-pass filter mode
The low-pass filter mode operates on an unfiltered, optionally inverted comparator output COUTA, and generates the filtered and 
synchronized output COUT. You can configure both COUTA and COUT as module outputs and use for different purposes within 
the system.
Synchronization and edge detection determine the bit values of status register. They also apply to COUT for all sampling and 
windowed modes. You can perform filtering using an internal timebase defined by CCR1[FILT_PER], or use an external sample 
input to determine sample time.
The need for digital filtering and the amount of filtering depends on your requirements. Filtering can become more useful in the 
absence of an external hysteresis circuit. Without external hysteresis, generate a high-frequency oscillations at COUTA when the 
selected INM and INP input voltages differ by less than the offset voltage of the differential comparator.
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2497 / 5251


---
# 페이지 189

61.3.3.1
Enabling low-pass filter mode
You can enable low-pass filter mode by setting the following:
• CCR1[FILT_CNT] > 01h
• CCR1[FILT_PER] to a nonzero value or writing 1 to CCR1[SAMPLE_EN].
If you use the divided bus clock to drive the low-pass filter, it samples COUTA every CCR1[FILT_PER] bus clock cycle.
If CCR1[SAMPLE_EN] is set to 1, the low-pass filter samples COUTA on each positive transition of the sample input. The output 
state of the filter changes when all the consecutive CCR1[FILT_CNT] samples agree that the output value has changed.
61.3.3.2
Latency issues
Program the value of CCR1[FILT_PER] or sample period such that the sampling period is longer than the period of the expected 
noise, ensuring that a given noise spike corrupts only one sample. You must choose the value of CCR1[FILT_CNT] to reduce the 
probability of noisy samples causing an incorrect transition to recognize. The probability of an incorrect transition is defined as the 
probability of an incorrect sample raised to the power of CCR1[FILT_CNT].
You must trade off the values of CCR1[FILT_PER] or sample period and CCR1[FILT_CNT] against the need for minimal latency in 
recognizing actual comparator output transitions. The probability of detecting an actual output change within the nominal latency 
is the probability of a correct sample raised to the power of CCR1[FILT_CNT].
Table 355 summarizes maximum latency values for the various modes of operation in the absence of noise. Filtering latency 
restarts each time the noise masks an actual output transition.
61.3.4 Low power mode operation
Below table introduces the mode of operation of lower power.
Table 354. Low power mode operation
Mode of operation
Description
STOP
LPCMP can operate only in Continuous mode or Round-robin 
trigger mode.
61.3.5 Functional modes
You can combine the comparator window and filter features as shown in the following table.
Table 355. Functional modes
Mode 
#
CMP_EN
WINDOW_
EN
SAMPLE_
EN
FILT_CNT
FILT_PER
Operation
Maximum latency1
1
0
X
X
X
X
See the Disabled 
mode (#1).
N/A
2A
1
0
X
0x00
X
See the Continuous 
mode (#2A and #2B).
TPD
2B
1
0
0
X
0x00
3A
1
0
1
0x01
X
See the Sampled, non-
filtered mode (#3A 
and #3B).
TPD + TSAMPLE + 3Tper
3B
1
0
0
0x01
> 0x00
TPD + (FILT_PER * Tper) 
+ 3Tper
Table continues on the next page...
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2498 / 5251


---
# 페이지 190

Table 355. Functional modes (continued)
Mode 
#
CMP_EN
WINDOW_
EN
SAMPLE_
EN
FILT_CNT
FILT_PER
Operation
Maximum latency1
4A
1
0
1
> 0x01
X
See the Sampled, 
filtered mode (#4A 
and #4B).
TPD + (FILT_CNT * 
TSAMPLE) + 3Tper
4B
1
0
0
> 0x01
> 0x00
TPD + (FILT_CNT * 
FILT_PER x Tper) + 3Tper
5A
1
1
0
0x00
X
See the Windowed 
mode (#5A and #5B).
TPD + 2Tper
5B
1
1
0
X
0x00
6
1
1
0
0x01
> 0x00
See the Windowed/
Resampled mode (#6).
TPD + (FILT_PER * Tper) 
+ 3Tper
7
1
1
0
> 0x01
> 0x00
See the Windowed/
Filtered mode (#7).
TPD + (FILT_CNT * 
FILT_PER x Tper) + 3Tper
All other combinations of CMP_EN, WINDOW_EN, SAMPLE_EN, FILT_CNT, and FILT_PER are illegal.
1. TPD represents the intrinsic delay of the analog component plus the polarity select logic. TSAMPLE is the clock period of the 
external sample clock. Tper is the period of the bus clock.
61.3.5.1
Disabled mode (#1)
In this mode:
• The analog comparator is non-functional and consumes no power.
• CSR[COUT] and CMPO are the same as CCR1[COUT_INV].
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2499 / 5251


---
# 페이지 191

61.3.5.2
Continuous mode (#2A and #2B)
 
COUT_INV
COUT
 
WINDOW_EN
COUT_SEL
+
-
HYSTCTR
FILT_CNT
CFR/F_IE
SAMPLE_EN
DMA_REQ
IRQ
Interrupt
/DMA 
Control
DMA_EN
Divided Bus Clock
CMPO to PAD
CFR/F
COUT
To other SOC functions
COUT_PEN
To open PAD for CMPO
Window
Control
Polarity
Select
Filter
Block
Clock
Prescaler
Bus Clock
FILT_PER
COUT_RAW
 
 
Internal Bus
INP
INM
WINDOW/SAMPLE
COUTA
1
0
1
0
CMP_EN
CMP_HPMD
CMP_NPMD
0
0
0x00 (#2A)
0x00 (#2B)
Sampling Clock
Figure 266. Comparator operation in continuous mode
COUT_RAW is optionally inverted in this mode but is not subject to external sampling or filtering. Both window control and filter 
blocks bypass completely, and CSR[COUT] updates continuously. The path from comparator input pins to output pins operates 
in a combinational (unclocked) mode. COUT and COUTA are identical in this mode.
For cases where a comparator drives a fault input, you must configure it to operate in Continuous mode so that an external fault 
can immediately pass to the target fault circuitry through the comparator.
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2500 / 5251


---
# 페이지 192

61.3.5.3
Sampled, non-filtered mode (#3A and #3B)
 
COUT_INV
COUT
WINDOW_EN
COUT_SEL
+
-
HYSTCTR
FILT_CNT
CFR/F_IE
SAMPLE_EN
DMA_REQ
IRQ
Interrupt
/DMA 
Control
DMA_EN
Divided Bus Clock
CMPO to PAD
CFR/F
COUT
To other SOC functions
COUT_PEN
To open PAD for CMPO
Window
Control
Polarity
Select
Filter
Block
Clock
Prescaler
Bus Clock
FILT_PER
COUT_RAW
 
 
Internal Bus
INP
INM
WINDOW/SAMPLE
COUTA
1
0
1
0
CMP_EN
CMP_HPMD
CMP_NPMD
1
0
0x01
Sampling Clock
Figure 267. Sampled, non-filtered (#3A): sampling point externally driven
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2501 / 5251


---
# 페이지 193

 
COUT_INV
COUT
WINDOW_EN
COUT_SEL
+
-
HYSTCTR
FILT_CNT
CFR/F_IE
SAMPLE_EN
DMA_REQ
IRQ
Interrupt
/DMA 
Control
DMA_EN
Divided Bus Clock
CMPO to PAD
CFR/F
COUT
To other SOC functions
COUT_PEN
To open PAD for CMPO
Window
Control
Polarity
Select
Filter
Block
Clock
Prescaler
Bus Clock
FILT_PER
COUT_RAW
 
 
Internal Bus
INP
INM
WINDOW/SAMPLE
COUTA
1
0
1
0
CMP_EN
CMP_HPMD
CMP_NPMD
0
0x01
0
>0x00
Sampling Clock
Figure 268. Sampled, Non-Filtered (#3B): sampling interval internally derived
In this mode, the path from analog inputs to COUTA is combinational (unclocked). Windowing control bypasses completely. You 
can sample COUTA whenever you detect a rising edge on the sampling clock.
The difference in two operation modes (#3A and #3B) of sampled, non-filtered mode is that how you drive the clock to the filter 
block. In #3A, the clock to filter block drives externally, and in #3B, the clock to filter block drives internally.
The filter block has no other function than sample or hold of the comparator output in this mode.
The following figure shows the comparator operation in this mode, assuming that the polarity select sets to a non-inverting state.
COUT_RAW
COUT
Sample point
Figure 269. Sampled, Non-Filtered mode timing diagram
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2502 / 5251


---
# 페이지 194

61.3.5.4
Sampled, filtered mode (#4A and #4B)
 
COUT_INV
COUT
WINDOW_EN
COUT_SEL
+
-
HYSTCTR
FILT_CNT
CFR/F_IE
SAMPLE_EN
DMA_REQ
IRQ
Interrupt
/DMA 
Control
DMA_EN
Divided Bus Clock
CMPO to PAD
CFR/F
COUT
To other SOC functions
COUT_PEN
To open PAD for CMPO
Window
Control
Polarity
Select
Filter
Block
Clock
Prescaler
Bus Clock
FILT_PER
COUT_RAW
 
 
Internal Bus
INP
INM
WINDOW/SAMPLE
COUTA
1
0
1
0
CMP_EN
CMP_HPMD
CMP_NPMD
0
>0x01
1
Sampling Clock
Figure 270. Sampled, filtered (#4A): sampling point externally driven
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2503 / 5251


---
# 페이지 195

 
COUT_INV
COUT
WINDOW_EN
COUT_SEL
+
-
HYSTCTR
FILT_CNT
CFR/F_IE
SAMPLE_EN
DMA_REQ
IRQ
Interrupt
/DMA 
Control
DMA_EN
Divided Bus Clock
CMPO to PAD
CFR/F
COUT
To other SOC functions
COUT_PEN
To open PAD for CMPO
Window
Control
Polarity
Select
Filter
Block
Clock
Prescaler
Bus Clock
FILT_PER
COUT_RAW
 
 
Internal Bus
INP
INM
WINDOW/SAMPLE
COUTA
1
0
1
0
CMP_EN
CMP_HPMD
CMP_NPMD
0
>0x01
0
Sampling Clock
>0x00
Figure 271. Sampled, filtered (#4B): sampling point internally derived
In this mode, the path from the analog inputs to COUTA is combinational(unclocked). Windowing control bypasses completely. 
You can sample COUTA whenever you detect a rising edge on the sampling clock.
The only difference in operation between sampled, non-filtered (#3A) mode and sampled, filtered (#4A) mode is that 
CCR1[FILT_CNT] is larger than 1, which activates filter operation.
The only difference in operation between sampled, non-filtered (#3B) mode and sampled, filtered (#4B) mode is that 
CCR1[FILT_CNT] is larger than 1, which activates filter operation.
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2504 / 5251


---
# 페이지 196

61.3.5.5
Windowed mode (#5A and #5B)
 
COUT_INV
COUT
WINDOW_EN
COUT_SEL
+
-
HYSTCTR
FILT_CNT
CFR/F_IE
SAMPLE_EN
DMA_REQ
IRQ
Interrupt
/DMA 
Control
DMA_EN
Divided Bus Clock
CMPO to PAD
CFR/F
COUT
To other SOC functions
COUT_PEN
To open PAD for CMPO
Window
Control
Polarity
Select
Filter
Block
Clock
Prescaler
Bus Clock
FILT_PER
COUT_RAW
 
 
Internal Bus
INP
INM
WINDOW/SAMPLE
COUTA
1
0
1
0
CMP_EN
CMP_HPMD
CMP_NPMD
1
0
0x00 (#5A)
0x00 (#5B)
Sampling Clock
Figure 272. Windowed mode
The bus clock clocks COUTA whenever you enable the window in this mode. The last latched value holds after you disable the 
window and the filter block is bypassed.
The following figure shows the comparator operation in this mode, ignoring the latency of the analog comparator, polarity select, 
and window control block. The polarity select sets to a non-inverting state.
COUTA may lag the analog inputs by up to two functional clock cycles plus the combinational path delay through the comparator 
and polarity select logic in the actual operation.
Window
COUT_RAW
COUTA
Figure 273. Windowed mode timing diagram
The following figure shows that if CCR1[COUTA_OWEN] becomes 1, you can define COUTA level as CCR1[COUTA_OW], after 
you closes the window.
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2505 / 5251


---
# 페이지 197

Window
User-defined level (COUTA_OW = 0)
COUT_RAW
COUTA
Figure 274. Windowed mode timing diagram with user defined value 0 outside window
Window
User-defined level (COUTA_OW = 1)
COUT_RAW
COUTA
Figure 275. Windowed mode timing diagram with user defined value 1 outside window
 
When the window is open, COUT_A will switch from COUTA_OW to COUT_RAW. When the window is closed, 
COUT_A will switch from COUT_RAW to COUTA_OW. This may generate unnecessary transition flags, for 
instance, CFR or CFF. User needs to choose COUTA_OW carefully according to the actual application, and select 
the appropriate flag CFR or CFF to generate interrupt.
  NOTE  
If CCR1[WINDOW_CLS] becomes 1, you can define the CMPO event (rising edge, falling edge or both edges that 
CCR1[EVT_SEL] selects) to close the window. The external window signal has to go to zero and back to one to enable 
the internal window again. The following figure shows an example that CMPO rising edge closes the internal window.
WINDOW
COUT_RAW
CMPO
WINDOW_INTERNAL
CMPO rising edge causes internal window close
Figure 276. Windowed mode timing diagram with CMPO rising edge close window
The following figure shows that if CCR1[WINDOW_INV] becomes 1, you can invert the window signal before you use it.
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2506 / 5251


---
# 페이지 198

WINDOW
COUT_RAW
CCR1[WINDOW_INV]
COUTA
WINDOW_INTERNAL
Figure 277. Windowed mode timing diagram with window signal inverted
61.3.5.6
Windowed/Resampled mode (#6)
 
COUT_INV
COUT
WINDOW_EN
COUT_SEL
+
-
HYSTCTR
FILT_CNT
CFR/F_IE
SAMPLE_EN
DMA_REQ
IRQ
Interrupt
/DMA 
Control
DMA_EN
Divided Bus Clock
CMPO to PAD
CFR/F
COUT
To other SOC functions
COUT_PEN
To open PAD for CMPO
Window
Control
Polarity
Select
Filter
Block
Clock
Prescaler
Bus Clock
FILT_PER
COUT_RAW
 
 
Internal Bus
INP
INM
WINDOW/SAMPLE
COUTA
1
0
1
0
CMP_EN
CMP_HPMD
CMP_NPMD
1
0x01
0
>0x00
Sampling Clock
Figure 278. Windowed/Resampled mode
This mode of operation results in an unfiltered string of comparator samples where CCR1[FILT_PER] and the bus clock rate 
determines the interval between the samples. The following section shows that the configuration for this mode is virtually identical 
to that for the Windowed/Filtered mode. The only difference is that the value of CCR1[FILT_CNT] must be 1 in this mode.
The following figure uses the same input stimulus shown in Figure 273, and adds resampling of COUTA to generate COUT. The 
arrows in the figure indicate the time points at which the samples are taken. You can ignore prop delays and latency for clarity.
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2507 / 5251


---
# 페이지 199

COUT_RAW
Sample point
Window
COUT
COUTA
Figure 279. Windowed/Resampled mode operation
This example demonstrates the operation of the comparator in Windowed/Resampled mode, and does not reflect any specific 
application. Based on the sampling rate and window placement, COUT may not see zero-crossing events that the analog 
comparator detects. You must carefully consider the sampling period and/or window placement for a given application.
61.3.5.7
Windowed/Filtered mode (#7)
 
COUT_INV
COUT
WINDOW_EN
COUT_SEL
+
-
HYSTCTR
FILT_CNT
CFR/F_IE
SAMPLE_EN
DMA_REQ
IRQ
Interrupt
/DMA 
Control
DMA_EN
Divided Bus Clock
CMPO to PAD
CFR/F
COUT
To other SOC functions
COUT_PEN
To open PAD for CMPO
Window
Control
Polarity
Select
Filter
Block
Clock
Prescaler
Bus Clock
FILT_PER
COUT_RAW
 
 
Internal Bus
INP
INM
WINDOW/SAMPLE
COUTA
1
0
1
0
CMP_EN
CMP_HPMD
CMP_NPMD
1
>0x01
0
>0x00
Sampling Clock
Figure 280. Windowed/Filtered mode
The only difference in operation between Windowed/Resampled mode (#6) and Windowed/Filtered mode (#7) is that 
CCR1[FILT_CNT] is >1, which activates filter operation.
This mode is the most complex mode of operation for the comparator block, as it utilizes both windowing and filtering features. It 
also has the highest latency of any of the modes. This is approximately: up to 2 peripheral clock synchronization in the window 
function + ((CCR1[FILT_CNT] x CCR1[FILT_PER]) + 1) x peripheral clock for the filter function.
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2508 / 5251


---
# 페이지 200

61.3.6 DMA
After DMA is enabled by writing 1 to CCR1[DMA_EN] and interrupt is enabled by writing 1 to IER[CFR_IE], IER[CFF_IE], or 
both, the corresponding change on COUT forces a DMA transfer request rather than a CPU interrupt. After the DMA completes 
the transfer, it sends a transfer completing indicator signal that deasserts the DMA transfer request and clears the flags (both 
CSR[CFR] and CSR[CFF]) to allow a subsequent change on comparator output to occur and forces another DMA request.
61.3.7 Clocking
LPCMP requires the following clocks to operate:
Table 356. LPCMP clocks
Type of clock
Description
Bus
Controls the access to LPCMP registers and window/
filter function.
Round-robin clock (RCLK)
Controls Round-robin trigger mode.
61.3.8 Resets
The global chip reset signal resets LPCMP.
61.3.9 Interrupts
After the corresponding IER becomes 1, CSR[CFR], CSR[CFF], and CSR[RRF] can generate an interrupt, assuming that 
CCR1[DMA_EN] is not 1. You can clear either the flag or IER to deassert the interrupt.
61.4 External signal descriptions
Below table introduces external signals.
Table 357. External signal descriptions
Signal
Description
I/O
CMPO
Filtered or unfiltered comparator output
O
Input_Analog_Channels
Analog input channels (see the chip-specific information for more 
on the connections).
I
VREFH_EXT
External reference voltage for the CMP-DAC (see the chip-specific 
information for more on the connections).
I
RR_ACTIVE
Round-robin trigger mode enabled.
O
61.5 Initialization
You can enable LPCMP by writing 1 to CCR0[CMP_EN], and then configuring the control registers (CCR1, CCR2, DCR, and 
so on).
To disable LPCMP, write 0 to CCR0[CMP_EN]. Switching operation modes or changing control register fields on-the-fly (when 
CCR0[CMP_EN] is set to 1) may cause noise on the COUT or COUTA signals. To avoid unwanted signal noise, you must ensure 
to disable the module before switching modes or changing control fields.
The time required to stabilize COUT is the power-on delay of the comparators plus the largest propagation delay from a selected 
analog source through the analog comparator, windowing function, and filter (see the Comparator and 8-bit DAC electrical 
specifications section of LPCMP datasheet for more information on propagation delay and power-up delay). Table 355 specifies 
the delay that the windowing and filter function causes.
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2509 / 5251


---
# 페이지 201

During operation, you must always consider the propagation delay of the selected data paths. It can take many bus clock cycles 
for COUT and CSR[CFR]/CSR[CFF] to reflect an input change or a configuration change to one of the components involved in 
the data path.
61.6 Application information
61.6.1 Round-robin trigger mode programing recommendation
Configure the Round-robin trigger mode as follows:
1. Configure the comparison cycles by RRCR0[RR_NSAM]. Note: It is a mandatory request that the round robin cycling 
period must set longer than the time that all the active channels complete the specified comparison cycles set by 
RRCR0[RR_NSAM].
2. Configure CMP initialization delay by RRCR0[RR_INITMOD]. Note: In programming RRCR0[RR_INITMOD], the 
RR_INITMOD x round robin clock period must be longer than the initialization delay, see the LPCMP datasheet for 
more information.
3. Configure RRCR1[FIXP] to select the fixed port of CMP and
a. If you use one input channel to compare with other channels, configure RRCR1[FIXCH] to select the fixed 
channel.
b. If you use DAC output to compare with input channels, configure CCR2[INPSEL] or CCR2[INMSEL] (according to 
RRCR1[FIXP] ) to select the DAC output.
4. Configure channels for comparison by RRCR1[RR_CHnEN].
5. Write RRCSR[RR_CHnOUT] to define the pre-set state of channel n.
6. Clear channel flags RRSR[RR_CHnF].
7. Enable round robin interrupt by IER[RRF_IE] (disable IER[CFR_IE] and IER[CFF_IE]).
8. Enable round-robin trigger mode by setting RRCR0[RR_EN] to 1.
9. Enable comparator by setting CCR0[CMP_EN] to 1.
61.6.2 Round-robin clock (RCLK) frequency requirement
(1) RCLK high frequency limit
RCLK high frequency limit depends on two facts:
1. The analog CMP and DAC initialization time (see the chip data sheet for more information on the initialization time.)
• RRCR0[RR_INITMOD] provides a maximum 63 RCLK cycles for the analog CMP and DAC initialization.
• RCLK must be slow to assure: 63 * (1/fRCLK) > Tinitialization, where fRCLK is in MHz, and Tinitialization is in microsecond.
• so fRCLK < 63 / Tinitialization
• Example: Tinitialization = 40 μs, then fRCLK should be smaller than 1.575 MHz.
2. The analog CMP propagation delay (see the Comparator and 8-bit DAC electrical specifications section of LPCMP 
datasheet for more information on the CMP propagation delay.)
• RRCR0[RR_NSAM] provides a maximum 4 RCLK cycles for the analog CMP propagation delay.
• RCLK must be slow to assure: 4 * (1/fRCLK) > Tpropagation, where fRCLK is in MHz, and Tpropagation is in microsecond.
• fRCLK < 4 / Tpropagation
• Example: Tpropagation = 0.1 μs, then fRCLK must be smaller than 40 MHz.
(2) RCLK low frequency limit
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2510 / 5251


---
# 페이지 202

In theory, RCLK frequency has no low limit. But the lower the RCLK frequency, the longer the scan time. Therefore, the lower limit 
of the RCLK frequency depends on the system application.
61.7 LPCMP register descriptions
The memory map comprises of 32-bit aligned registers, which you can access via 8-, 16- or 32-bit reads and 32-bit write. 
Attempted accesses using unsupported write data sizes, writes to read-only resources, or to reserved spaces terminate with an 
error. Read access to reserved address generates a transfer error and the read data bus shows all 0s.
61.7.1 LPCMP memory map
LPCMP_0 base address: 4037_0000h
LPCMP_1 base address: 4037_4000h
LPCMP_2 base address: 404E_8000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Version ID (VERID)
32
R
0100_0001h
4h
Parameter (PARAM)
32
R
0000_0002h
8h
Comparator Control Register 0 (CCR0)
32
RW
0000_0002h
Ch
Comparator Control Register 1 (CCR1)
32
RW
0000_0000h
10h
Comparator Control Register 2 (CCR2)
32
RW
0000_0000h
18h
DAC Control (DCR)
32
RW
0000_0000h
1Ch
Interrupt Enable (IER)
32
RW
0000_0000h
20h
Comparator Status (CSR)
32
RW
0000_0000h
24h
Round Robin Control Register 0 (RRCR0)
32
RW
0000_0000h
28h
Round Robin Control Register 1 (RRCR1)
32
RW
0000_0000h
2Ch
Round Robin Control and Status (RRCSR)
32
RW
0000_0000h
30h
Round Robin Status (RRSR)
32
RW
0000_0000h
61.7.2 Version ID (VERID)
Offset
Register
Offset
VERID
0h
Function
Contains version numbers for the module design and feature set.
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2511 / 5251


---
# 페이지 203

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
MAJOR 
MINOR 
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
FEATURE 
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
Fields
Field
Function
31-24
MAJOR
Major Version Number
Returns the major version number for the module design.
23-16
MINOR
Minor Version Number
Returns the minor version number for the module design.
15-0
FEATURE
Feature Specification Number
Returns the feature set number.
0000_0000_0000_0001b - Round robin feature
61.7.3 Parameter (PARAM)
Offset
Register
Offset
PARAM
4h
Function
Contains parameter values that are implemented in the module.
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2512 / 5251


---
# 페이지 204

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
0
0
0
0
0
0
0
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
DAC_RES 
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
Fields
Field
Function
31-4
—
Reserved
3-0
DAC_RES
DAC Resolution
Indicates supported DAC resolutions.
 
All other bit field values are reserved.
  NOTE  
0000b - 4-bit DAC
0001b - 6-bit DAC
0010b - 8-bit DAC
0011b - 10-bit DAC
0100b - 12-bit DAC
0101b - 14-bit DAC
0110b - 16-bit DAC
61.7.4 Comparator Control Register 0 (CCR0)
Offset
Register
Offset
CCR0
8h
Function
Contains configuration options for enabling the analog comparator and the DAC.
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2513 / 5251


---
# 페이지 205

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
LINKE
N 
CMP_
STO...
CMP_
EN 
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
Fields
Field
Function
31-3
—
Reserved
2
LINKEN
CMP-to-DAC Link Enable
Enables the CMP-to-DAC link.
0b - Disable: enabling or disabling the DAC is independent from enabling or disabling the CMP.
1b - Enable: enabling/disabling DAC is controlled by the CMP_EN bit instead of DCR[DAC_EN]. 
Also, when the CMP is auto-disabled because software selects the same signal for both the plus 
and minus comparator inputs, the DAC is disabled too.
1
CMP_STOP_E
N
Comparator STOP Mode Enable
Enables the analog comparator or the DAC when the module is in STOP mode.
 
This field has no effect in Round-robin Trigger mode.
  NOTE  
0b - Disables the analog comparator regardless of CMP_EN.
1b - Allows CMP_EN to enable the analog comparator.
0
CMP_EN
Comparator Enable
Enables the analog comparator.
 
When CCR0[LINKEN]=1, CMP_EN also controls the enabling/disabling of the DAC instead 
of DCR[DAC_EN].
  NOTE  
0b - Disable (The analog logic remains off and consumes no power.)
1b - Enable
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2514 / 5251


---
# 페이지 206

61.7.5 Comparator Control Register 1 (CCR1)
Offset
Register
Offset
CCR1
Ch
Function
Contains configuration options for the comparator operation, such as enabling Sampling or Windowing mode.
 
You cannot enable Sampling and Windowing modes both at the same time. Sampling mode takes precedence over 
Windowing mode. If you write 1 to both SAMPLE_EN and WINDOW_EN, only SAMPLE_EN becomes 1.
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
FILT_PER 
0
FILT_CNT 
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
EVT_SEL 
WIND
OW_...
WIND
OW_...
COUT
A_OW 
COUT
A_O...
COUT
_PEN 
COUT
_SEL 
COUT
_INV 
DMA_
EN 
SAMP
LE_...
WIND
OW_...
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
31-24
FILT_PER
Filter Sample Period
Specifies the sampling period (in bus clock cycles) of the comparator output filter. Programming this field to 
00h bypasses the filter. See Functional description for more information on filter programming and latency.
 
FILT_PER has no effect in Sampling mode (CCR1[SAMPLE_EN] = 1).
  NOTE  
23-19
—
Reserved
18-16
FILT_CNT
Filter Sample Count
Specifies the number of consecutive samples that must agree before the comparator output filter 
accepts the sample as a new valid output state. See Functional description for more information on 
filter programming and latency.
Table continues on the next page...
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2515 / 5251


---
# 페이지 207

Table continued from the previous page...
Field
Function
000b - Filter is bypassed: COUT = COUTA
001b - 1 consecutive sample (Comparator output is simply sampled.)
010b - 2 consecutive samples
011b - 3 consecutive samples
100b - 4 consecutive samples
101b - 5 consecutive samples
110b - 6 consecutive samples
111b - 7 consecutive samples
15-14
—
Reserved
13-12
—
Reserved
11-10
EVT_SEL
CMPO Event Select
Selects which CMPO signal edge (rising, falling, or both) defines a CMPO event.
 
Valid only in Windowing mode.
  NOTE  
00b - Rising edge
01b - Falling edge
1xb - Both edges
9
WINDOW_CLS
CMPO Event Window Close
Enables a CMPO event (defined as a CMPO rising edge, falling edge, or both) to close an active window. 
See EVT_SEL to configure the CMPO event.
 
The WINDOW signal has to go to zero and back to one again to re-activate the window. 
Valid only in Windowing mode.
  NOTE  
0b - CMPO event cannot close the window
1b - CMPO event can close the window
8
WINDOW_INV
WINDOW/SAMPLE Signal Invert
Inverts the window/sample signal.
0b - Do not invert
1b - Invert
7
COUTA Output Level for Closed Window
Table continues on the next page...
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2516 / 5251


---
# 페이지 208

Table continued from the previous page...
Field
Function
COUTA_OW
Defines the COUTA signal value when the window is closed.
 
Valid only in Windowing mode and when COUTA_OWEN=1.
  NOTE  
0b - COUTA is 0
1b - COUTA is 1
6
COUTA_OWEN
COUTA_OW Enable
Enables the COUTA signal value to be defined by COUTA_OW when the window is closed.
 
Valid only in Windowing mode.
  NOTE  
0b - COUTA holds the last sampled value.
1b - Enables the COUTA signal value to be defined by COUTA_OW.
5
COUT_PEN
Comparator Output Pin Enable
Enables the comparator output to become an available signal option for a selected package pin.
0b - Not available
1b - Available
4
COUT_SEL
Comparator Output Select
Selects which comparator output option, COUT or COUTA, to use for CMPO.
0b - Use COUT (filtered)
1b - Use COUTA (unfiltered)
3
COUT_INV
Comparator Invert
Selects the polarity of the analog comparator function, affecting the value driven to the COUT output (on 
both the chip pin and as CSR[COUT]) when CCR0[CMP_EN] is 0.
 
COUT_INV has no effect in Trigger mode.
  NOTE  
0b - Do not invert
1b - Invert
2
DMA_EN
DMA Enable
Enables DMA transfers triggered from the LPCMP module. After this field and the corresponding 
interrupt enable field becomes 1, a DMA request is asserted when CFR or CFF becomes 1.
0b - Disable
1b - Enable
1
Sampling Enable
Table continues on the next page...
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2517 / 5251


---
# 페이지 209

Table continued from the previous page...
Field
Function
SAMPLE_EN
Enables Sampling mode.
0b - Disable
1b - Enable
0
WINDOW_EN
Windowing Enable
Enables Windowing mode.
 
Valid only when SAMPLE_EN = 0.
  NOTE  
0b - Disable
1b - Enable
61.7.6 Comparator Control Register 2 (CCR2)
Offset
Register
Offset
CCR2
10h
Function
Contains the configuration options for the comparator operation, such as selecting the plus and minus comparator inputs and the 
hysteresis levels.
 
When an inappropriate operation selects the same signal for both the plus and minus comparator inputs, the analog 
comparator automatically shuts down (regardless of CMP_EN) to prevent itself from becoming a noise generator.
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
INMSEL 
0
INPSEL 
0
MSEL 
0
PSEL 
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
HYSTCTR 
0
OFFS
ET 
0
CMP_
HPMD 
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
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2518 / 5251


---
# 페이지 210

Fields
Field
Function
31-30
—
Reserved
29-28
INMSEL
Input Minus Select
Selects the minus input of the comparator.
 
These selections connect directly to the minus input of the comparator.
  NOTE  
00b - IN0: from the 8-bit DAC output
01b - IN1: from the analog 8-1 mux
10b - Reserved
11b - Reserved
27-26
—
Reserved
25-24
INPSEL
Input Plus Select
Selects the plus input of the comparator.
 
These selections connect directly to the plus input of the comparator.
  NOTE  
00b - IN0: from the 8-bit DAC output
01b - IN1: from the analog 8-1 mux
10b - Reserved
11b - Reserved
23
—
Reserved
22-20
MSEL
Minus Input MUX Select
Selects the input used for the negative mux. See the chip-specific LPCMP information for more 
on connections.
 
MSEL has no effect in Trigger mode.
  NOTE  
000b - Input channel 0
001b - Input channel 1
010b - Input channel 2
011b - Input channel 3
Table continues on the next page...
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2519 / 5251


---
# 페이지 211

Table continued from the previous page...
Field
Function
100b - Input channel 4
101b - Input channel 5
110b - Input channel 6
111b - Input channel 7
19
—
Reserved
18-16
PSEL
Plus Input MUX Select
Selects the input used for the positive mux. See the chip-specific LPCMP information for more 
on connections.
 
PSEL has no effect in Trigger mode.
  NOTE  
000b - Input channel 0
001b - Input channel 1
010b - Input channel 2
011b - Input channel 3
100b - Input channel 4
101b - Input channel 5
110b - Input channel 6
111b - Input channel 7
15-6
—
Reserved
5-4
HYSTCTR
Comparator Hysteresis Control
Selects the level of internally generated hysteresis for the comparator output.
 
This applies to the comparator hard block.
  NOTE  
00b - Level 0: Analog comparator hysteresis 0 mV.
01b - Level 1: Analog comparator hysteresis 10 mV.
10b - Level 2: Analog comparator hysteresis 20 mV.
11b - Level 3: Analog comparator hysteresis 30 mV.
3
—
Reserved
2
Comparator Offset Control
Table continues on the next page...
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2520 / 5251


---
# 페이지 212

Table continued from the previous page...
Field
Function
OFFSET
Selects the level of internally generated voltage offset for the comparator output. See the chip data sheet 
to get the specific values for each offset level.
0b - Level 0: The hysteresis selected by HYSTCTR is valid for both directions (rising and falling).
1b - Level 1: Hysteresis does not apply when INP (input-plus) crosses INM (input-minus) in the 
rising direction or when INM crosses INP in the falling direction. Hysteresis still applies for INP 
crossing INM in the falling direction.
1
—
Reserved
0
CMP_HPMD
CMP High Power Mode Select
Selects Low or High Power(Speed) mode for the comparator.
0b - Low power (speed) comparison mode
1b - High power (speed) comparison mode
61.7.7 DAC Control (DCR)
Offset
Register
Offset
DCR
18h
Function
Contains the configuration options to enable the DAC.
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
DAC_DATA 
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
VRSE
L 
0
0
DAC_
EN 
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
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2521 / 5251


---
# 페이지 213

Fields
Field
Function
31-24
—
Reserved
23-16
DAC_DATA
DAC Output Voltage Select
Selects the DAC output (DACO) voltage from one of 256 distinct levels by configuring the value of 
DAC_DATA. The DACO ranges from Vin/256 to Vin.
 
DACO = (Vin/256) * (DAC_DATA + 1)
  NOTE  
15-9
—
Reserved
8
VRSEL
DAC Reference High Voltage Source Select
Selects the high voltage reference source for the Vin supply of the DAC's resistor ladder network. See 
the chip-specific LPCMP information for the source of vrefh0 and vrefh1.
0b - VREFH0
1b - VREFH1
7-2
—
Reserved
1
—
Reserved
0
DAC_EN
DAC Enable
Enables the DAC. When disabled, power-down the DAC to conserve power.
 
You can control the link from the CMP enable to the DAC enable by setting 
up CCR0[LINKEN].
  NOTE  
0b - Disable
1b - Enable
61.7.8 Interrupt Enable (IER)
Offset
Register
Offset
IER
1Ch
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2522 / 5251


---
# 페이지 214

Function
Provides enable fields for the comparator and round-robin flag interrupts.
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
RRF_
IE 
CFF_
IE 
CFR_
IE 
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
31-3
—
Reserved
2
RRF_IE
Round-Robin Flag Interrupt Enable
Enables or disables the round-robin flag interrupt.
0b - Disables the round-robin flag interrupt.
1b - Enables the round-robin flag interrupt when the comparison result changes for a given 
channel.
1
CFF_IE
Comparator Flag Falling Interrupt Enable
Enables or disables the comparator flag falling interrupt.
0b - Disables the comparator flag falling interrupt.
1b - Enables the comparator flag falling interrupt when CFF is set.
0
CFR_IE
Comparator Flag Rising Interrupt Enable
Enables or disables the comparator flag rising interrupt.
0b - Disables the comparator flag rising interrupt.
1b - Enables the comparator flag rising interrupt when CFR is set.
61.7.9 Comparator Status (CSR)
Offset
Register
Offset
CSR
20h
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2523 / 5251


---
# 페이지 215

Function
Indicates comparator status, including COUT, CFF, CFR, and RRF.
 
LPCMP may output a glitch and affect the value of CSR[CFF] and CSR[CFR] at the moment of enabling CMP. 
In order to ensure correctness, it is recommended to write one to clear (W1C) CSR[CFF] and CSR[CFR] before 
further configuring CMP.
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
COUT 
0
RRF 
CFF 
CFR 
W
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
31-9
—
Reserved
8
COUT
Analog Comparator Output
Returns the current value of the analog comparator output when read. This field resets to 0 and reads 
as CCR1[COUT_INV] after the analog comparator module disables when CCR0[CMP_EN] = 0. Writing 
to this field is ignored.
7-3
—
Reserved
2
RRF
Round-Robin Flag
Detects when any channel's last comparison result is different from the pre-set value in Trigger mode. 
Write 1 to clear this field. This field clears when CCR0[CMP_EN] or RRCR0[RR_EN] is not 1.
0b - Not detected
1b - Detected
1
CFF
Analog Comparator Flag Falling
Detects when a falling edge on COUT occurs. Write 1 to clear this field when CCR1[DMA_EN] is 
disabled. If CCR1[DMA_EN] is enabled, the flag automatically clears after DMA is done. This field clears 
when CCR0[CMP_EN] is not 1.
Table continues on the next page...
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2524 / 5251


---
# 페이지 216

Table continued from the previous page...
Field
Function
0b - Not detected
1b - Detected
0
CFR
Analog Comparator Flag Rising
Detects when a rising edge on COUT occurs. Write 1 to clear this field when CCR1[DMA_EN] is 
disabled. If CCR1[DMA_EN] is enabled, the flag automatically clears after DMA is done. This field clears 
when CCR0[CMP_EN] is not 1.
0b - Not detected
1b - Detected
61.7.10 Round Robin Control Register 0 (RRCR0)
Offset
Register
Offset
RRCR0
24h
Function
Contains configuration options for the round-robin operation, such as enabling it and specifying the initialization delay.
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
RR_INITMOD 
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
RR_NSAM 
0
0
RR_
EN 
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
31-22
—
Reserved
Table continues on the next page...
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2525 / 5251


---
# 페이지 217

Table continued from the previous page...
Field
Function
21-16
RR_INITMOD
Initialization Delay Modulus
Specifies the number of round-robin clock cycles that determines the comparator and DAC initialization 
delay specified in the chip datasheet. Calculate the initialization delay as RR_INITMOD * (round-robin 
clock period).
For example, if the initialization delay is 80us and the round-robin clock is 100kHz, program RR_INITMOD 
to be 80us/10us = 8.
00_0000b - 63 cycles (same as 111111b)
00_0001b-11_1111b - 1 to 63 cycles
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
RR_NSAM
Number of Sample Clocks
Specifies the number of the round-robin clock cycles to wait after scanning the active channel before 
sampling the channel's comparison result. After the next cycle of the round-robin clock, the sampling 
takes place RR_NSAM clocks later.
00b - 0 clock
01b - 1 clock
10b - 2 clocks
11b - 3 clocks
7-2
—
Reserved
1
—
Reserved
0
RR_EN
Round-Robin Enable
Enables the round-robin operation.
0b - Disable
1b - Enable
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2526 / 5251


---
# 페이지 218

61.7.11 Round Robin Control Register 1 (RRCR1)
Offset
Register
Offset
RRCR1
28h
Function
Contains configuration options for the round-robin operation, such as enabling individual channels to participate.
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
FIXCH 
0
FIXP 
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
RR_C
H7EN 
RR_C
H6EN 
RR_C
H5EN 
RR_C
H4EN 
RR_C
H3EN 
RR_C
H2EN 
RR_C
H1EN 
RR_C
H0EN 
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
31-23
—
Reserved
22-20
FIXCH
Fixed Channel Select
Selects which channel in the mux port to fix for a given round-robin trigger mode application.
000b - Channel 0
001b - Channel 1
010b - Channel 2
011b - Channel 3
100b - Channel 4
101b - Channel 5
110b - Channel 6
111b - Channel 7
19-17
—
Reserved
Table continues on the next page...
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2527 / 5251


---
# 페이지 219

Table continued from the previous page...
Field
Function
16
FIXP
Fixed Port
Fixes an analog mux port (plus or minus) for round-robin trigger mode. The inputs to the non-fixed port 
sweep during each round.
0b - Fix the plus port. Sweep only the inputs to the minus port.
1b - Fix the minus port. Sweep only the inputs to the plus port.
15-8
—
Reserved
7-0
RR_CHnEN
Channel n Input Enable in Trigger Mode
Enables channel n of the non-fixed mux port to check its voltage value when in Trigger mode.
 
RR_CHnEN has no effect when the same channel is selected as the reference voltage.
  NOTE  
0b - Disable
1b - Enable
61.7.12 Round Robin Control and Status (RRCSR)
Offset
Register
Offset
RRCSR
2Ch
Function
Contains the latest comparison results of the individual channels with the fixed mux port. It also allows you to define the 
pre-set state for each channel.
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
RR_C
H7O...
RR_C
H6O...
RR_C
H5O...
RR_C
H4O...
RR_C
H3O...
RR_C
H2O...
RR_C
H1O...
RR_C
H0O...
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
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2528 / 5251


---
# 페이지 220

Fields
Field
Function
31-8
—
Reserved
7-0
RR_CHnOUT
Comparison Result for Channel n
Returns the latest comparison result for channel n when read and defines the pre-set state for channel n 
when written to.
61.7.13 Round Robin Status (RRSR)
Offset
Register
Offset
RRSR
30h
Function
Contains individual channel flags that indicates when a channel's last comparison result is different from its pre-set value.
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
RR_
CH7F 
RR_
CH6F 
RR_
CH5F 
RR_
CH4F 
RR_
CH3F 
RR_
CH2F 
RR_
CH1F 
RR_
CH0F 
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
RR_CHnF
Channel n Input Changed Flag
Indicates when the corresponding channel's last comparison result is different from its pre-set value.
Table continues on the next page...
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2529 / 5251


---
# 페이지 221

Table continued from the previous page...
Field
Function
 
To clear a flag, write a 1 to it.
  NOTE  
0b - No different
1b - Different
61.8 Glossary
CMP
Comparator
DAC
Digital-to-analog convertor
ANMUX
Analog multiplexer
NXP Semiconductors
Low Power Comparator (LPCMP)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2530 / 5251


---