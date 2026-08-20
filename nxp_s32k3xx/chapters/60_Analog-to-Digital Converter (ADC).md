# 페이지 18

Chapter 60
Analog-to-Digital Converter (ADC)
60.1 Chip-specific ADC information
60.1.1 ADC Configuration
This chip has up to 3 instances of ADC. ADC channels are divided into 3 groups - Precision, Standard and External (each with 
independent configuration settings and different accuracy/performance level). The following table shows the ADC configuration:
Table 340. ADC instances
Instance
S32K388/S32K389/S32K358/
S32K348/S32K338/S32K328/S32K344/
S32K324/S32K314
S32K342/S32K322/S32K341/S32K312/
S32K311/S32K310
ADC_0
Yes
Yes
ADC_1
Yes
Yes
ADC_2
Yes
No
Table 341. ADC configuration
Feature
ADC_0
ADC_1
ADC_2
No. of precision channels
8
8
8
No. of standard channels
16
16
16
No. of special internal channels
11
0
0
No. of external channels
32
32
0
BCTU trigger support
Yes
Yes
Yes
DMA support
Yes
Yes
Yes
Hardware interleaving
Yes
Yes
Yes
No. of watchdogs
4
4
4
No. of Hardware trigger
3
3
3
1. CHAN_INT0 - channel 50(S)
 
See the device IOMUX file attached to this document for the availability of ADC channels for different devices 
and packages.
  NOTE  
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2327 / 5251


---
# 페이지 19

Table 342. ADC maximum clock frequency
Feature
S32K389/S32K388
S32K358/
S32K348/
S32K338/
S32K328
S32K344/
S32K324/
S32K314/
S32K342/
S32K322/
S32K341
S32K312
S32K311/
S32K310
ADC module clock 
frequency (f_mc)
160 MHz
240 MHz
160/120 MHz
120 MHz
120 MHz
 
For register configurations need for different frequencies, see 'Functional description' section in this chapter.
  NOTE  
ADC Channel mapping Table 
Table 343. ADC channel mapping
Channel Number
ADC_0
ADC_1
ADC_2
0
ADC0_P0
ADC1_P0
ADC2_P0
1
ADC0_P1
ADC1_P1
ADC2_P1
2
ADC0_P2
ADC1_P2
ADC2_P2
3
ADC0_P3
ADC1_P3
ADC2_P3
4
ADC0_P4
ADC1_P4
ADC2_P4
5
ADC0_P5
ADC1_P5
ADC2_P5
6
ADC0_P6
ADC1_P6
ADC2_P6
7
ADC0_P7
ADC1_P7
ADC2_P7
8
—1
—
—
9
—
—
—
10
—
—
—
11
—
—
—
12
—
—
—
13
—
—
—
14
—
—
—
15
—
—
—
16
—
—
—
17
—
—
—
18
—
—
—
19
—
—
—
20
—
—
—
21
—
—
—
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2328 / 5251


---
# 페이지 20

Table 343. ADC channel mapping (continued)
Channel Number
ADC_0
ADC_1
ADC_2
22
—
—
—
23
—
—
—
24
—
—
—
25
—
—
—
26
—
—
—
27
—
—
—
28
—
—
—
29
—
—
—
30
—
—
—
31
—
—
—
32
ADC0_S[8]
ADC1_S[8]
ADC2_S[8]
33
ADC0_S[9]
ADC1_S[9]
ADC2_S[9]
34
ADC0_S[10]
ADC1_S[10]
ADC2_S[10]
35
ADC0_S[11]
ADC1_S[11]
ADC2_S[11]
36
ADC0_S[12]
ADC1_S[12]
ADC2_S[12]
37
ADC0_S[13]
ADC1_S[13]
ADC2_S[13]
38
ADC0_S[14]
ADC1_S[14]
ADC2_S[14]
39
ADC0_S[15]
ADC1_S[15]
ADC2_S[15]
40
ADC0_S[16]
ADC1_S[16]
ADC2_S[16]
41
ADC0_S[17]
ADC1_S[17]
ADC2_S[17]
42
ADC0_S[18]
ADC1_S[18]
ADC2_S[18]
43
ADC0_S[19]
ADC1_S[19]
ADC2_S[19]
44
ADC0_S[20]
ADC1_S[20]
ADC2_S[20]
45
ADC0_S[21]
ADC1_S[21]
ADC2_S[21]
46
ADC0_S[22]
ADC1_S[22]
ADC2_S[22]
47
ADC0_S[23]
ADC1_S[23]
ADC2_S[23]
48
Bandgap
Bandgap
Bandgap
49
Tempsensor output
Tempsensor output
Tempsensor output
50
ANAMUX_OUT
—
—
51
—
—
—
52
—
—
—
53
—
—
—
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2329 / 5251


---
# 페이지 21

Table 343. ADC channel mapping (continued)
Channel Number
ADC_0
ADC_1
ADC_2
54
VREFL
VREFL
VREFL
55
VREFH
VREFH
VREFH
56
—
—
—
57
—
—
—
58
—
—
—
59
—
—
—
60
—
—
—
61
—
—
—
62
—
—
—
63
—
—
—
64
ADC0_X[0]
ADC0_MA[2:0]=3'h0
ADC1_X[0]
ADC1_MA[2:0]=3'h0
—
65
ADC0_X[0]
ADC0_MA[2:0]=3'h1
ADC1_X[0]
ADC1_MA[2:0]=3'h1
—
66
ADC0_X[0]
ADC0_MA[2:0]=3'h3
ADC1_X[0]
ADC1_MA[2:0]=3'h3
—
67
ADC0_X[0]
ADC0_MA[2:0]=3'h2
ADC1_X[0]
ADC1_MA[2:0]=3'h2
—
68
ADC0_X[0]
ADC0_MA[2:0]=3'h6
ADC1_X[0]
ADC1_MA[2:0]=3'h6
—
69
ADC0_X[0]
ADC0_MA[2:0]=3'h7
ADC1_X[0]
ADC1_MA[2:0]=3'h7
—
70
ADC0_X[0]
ADC0_MA[2:0]=3'h5
ADC1_X[0]
ADC1_MA[2:0]=3'h5
—
71
ADC0_X[0]
ADC0_MA[2:0]=3'h4
ADC1_X[0]
ADC1_MA[2:0]=3'h4
—
72
ADC0_X[1]
ADC0_MA[2:0]=3'h0
ADC1_X[1]
ADC1_MA[2:0]=3'h0
—
73
ADC0_X[1]
ADC0_MA[2:0]=3'h1
ADC1_X[1]
ADC1_MA[2:0]=3'h1
—
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2330 / 5251


---
# 페이지 22

Table 343. ADC channel mapping (continued)
Channel Number
ADC_0
ADC_1
ADC_2
74
ADC0_X[1]
ADC0_MA[2:0]=3'h3
ADC1_X[1]
ADC1_MA[2:0]=3'h3
—
75
ADC0_X[1]
ADC0_MA[2:0]=3'h2
ADC1_X[1]
ADC1_MA[2:0]=3'h2
—
76
ADC0_X[1]
ADC0_MA[2:0]=3'h6
ADC1_X[1]
ADC1_MA[2:0]=3'h6
—
77
ADC0_X[1]
ADC0_MA[2:0]=3'h7
ADC1_X[1]
ADC1_MA[2:0]=3'h7
—
78
ADC0_X[1]
ADC0_MA[2:0]=3'h5
ADC1_X[1]
—
79
ADC0_X[1]
ADC0_MA[2:0]=3'h4
ADC1_X[1]
ADC1_MA[2:0]=3'h4
—
80
ADC0_X[2]
ADC0_MA[2:0]=3'h0
ADC1_X[2]
ADC1_MA[2:0]=3'h0
—
81
ADC0_X[2]
ADC0_MA[2:0]=3'h1
ADC1_X[2]
ADC1_MA[2:0]=3'h1
—
82
ADC0_X[2]
ADC0_MA[2:0]=3'h3
ADC1_X[2]
ADC1_MA[2:0]=3'h3
—
83
ADC0_X[2]
ADC0_MA[2:0]=3'h2
ADC1_X[2]
ADC1_MA[2:0]=3'h2
—
84
ADC0_X[2]
ADC0_MA[2:0]=3'h6
ADC1_X[2]
ADC1_MA[2:0]=3'h6
—
85
ADC0_X[2]
ADC0_MA[2:0]=3'h7
ADC1_X[2]
ADC1_MA[2:0]=3'h7
—
86
ADC0_X[2]
ADC0_MA[2:0]=3'h5
ADC1_X[2]
ADC1_MA[2:0]=3'h5
—
87
ADC0_X[2]
ADC0_MA[2:0]=3'h4
ADC1_X[2]
ADC1_MA[2:0]=3'h4
—
88
ADC0_X[3]
ADC1_X[3]
—
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2331 / 5251


---
# 페이지 23

Table 343. ADC channel mapping (continued)
Channel Number
ADC_0
ADC_1
ADC_2
ADC0_MA[2:0]=3'h0
ADC1_MA[2:0]=3'h0
89
ADC0_X[3]
ADC0_MA[2:0]=3'h1
ADC1_X[3]
ADC1_MA[2:0]=3'h1
—
90
ADC0_X[3]
ADC0_MA[2:0]=3'h3
ADC1_X[3]
ADC1_MA[2:0]=3'h3
—
91
ADC0_X[3]
ADC0_MA[2:0]=3'h2
ADC1_X[3]
ADC1_MA[2:0]=3'h2
—
92
ADC0_X[3]
ADC0_MA[2:0]=3'h6
ADC1_X[3]
ADC1_MA[2:0]=3'h6
—
93
ADC0_X[3]
ADC0_MA[2:0]=3'h7
ADC1_X[3]
ADC1_MA[2:0]=3'h7
—
94
ADC0_X[3]
ADC0_MA[2:0]=3'h5
ADC1_X[3]
ADC1_MA[2:0]=3'h5
—
95
ADC0_X[3]
ADC0_MA[2:0]=3'h4
ADC1_X[3]
ADC1_MA[2:0]=3'h4
—
1. Channels marked with “-“ means they are reserved and access to any reserved channel may result in inappropriate data.
 
The decoding signals for the selection of external ADC channels (ADC_X) are gray-encoded.
  NOTE  
 
Value of ANAMUX_OUT is selected by DCMRWF1[SUPPLY_MON_SEL] field.
  NOTE  
 
The module clock mentioned in this chapter is CORE_CLK for this chip.
  NOTE  
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2332 / 5251


---
# 페이지 24

60.1.2 ANAMUX for internal supply monitoring
000
001
001
011
100
101
110
111
VDD_HV_A_DIV
VDD_HV_B_DIV
VDD_1.5_DIV
VDD_2.5_OSC
VDD1.1_PD1_HOT_POINT
VDD1.1_PLL
VDD1.1_PD0
SUPPLY_MON_SEL
VDD1.1_PD1_COLD_POINT
SUPPLY_MON_SEL
CHAN_INT0
ADC_0
VSS_LV
VSS_LV_ANMUX_EN
A
N
A
M
U
X
Figure 247.
 
VDD_HV_B_DIV, VDD_1.5_DIV are not available in S32K312 and S32K311.
  NOTE  
60.1.3 BCTU Interface
All 3 instances of ADC are triggered from the BCTU. The BCTU provides channel conversion commands to the ADC (includes 
channel number information). In addition, the ADC provides the conversion result back to the BCTU.
 
Self-test conversion in BCTU mode is not supported in S32K3xx devices.
  NOTE  
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2333 / 5251


---
# 페이지 25

BCTU
ADC_0
bct u_t r g_0
bct u_channel _0
adc_dat a_0
adc_end_of _conv_0
adc_nxt _cmd_0
bct u_channel _1
adc_dat a_1
adc_end_of _conv_1
adc_nxt _cmd_1
ADC_1
bct u_channel _2
adc_dat a_2
adc_end_of _conv_2
adc_nxt _cmd_2
ADC_2
bct u_t r g_1
bct u_t r g_2
Figure 248. ADC Cross-triggering Unit
BCTU gives trigger pulse to all the 72 channels of ADC to initiate a conversion based on BCTU channel number.
BCTU-ADC result register
ADC result registers (ADCx_PCDRn[CDATA], ADCx_ICDRn[CDATA] and ADCx_ECDRn[CDATA]) store 15 bit conversion 
data. The BCTU ADC registers store 15-bit conversion data (BCTU_ADC0DR[ADC0_DATA], BCTU_ADC1DR[ADC1_DATA] 
and BCTU_ADC2DR[ADC2_DATA]).
60.1.4 DMA interface
Each ADC supports a single DMA request that can be requested after the conversion of every channel. The conversion result is 
stored into a register DMAR and is transferred via DMA or host access.
 
The last ongoing conversion will be aborted as soon as ADC gets STOP request from the software and it will move 
to STOP mode.
  NOTE  
60.1.5 Hardware triggers
In this chip, hardware trigger signals can be provided from TRGMUX outputs. This feature enables synchronous conversion of 
two independent ADC instances in parallel. If ADC is in Idle state (that is, no conversion phase ongoing and the MCR[PWDN] 
and MCR[ACKO] fields are 0) and the MCR[XSTRTEN] is set, an event on the external start signal causes ADC to start either 
normal or injected conversion operation. The MCR[NSTART]/MCR[JSTART] field is automatically set respectively. The normal 
conversion sync pulse is used with normal conversion trigger to synchronize the start timing of normal conversion between 
multiple ADC instances.
Table 344. Hardware triggers
TRGMUX output number
Hardware trigger functions
0
ADC_0 Normal Conversion
1
ADC_0 Injected Conversion
2
ADC_0 Normal Conversion Sync Pulse
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2334 / 5251


---
# 페이지 26

Table 344. Hardware triggers (continued)
TRGMUX output number
Hardware trigger functions
4
ADC_1 Normal Conversion
5
ADC_1 Injected Conversion
6
ADC_1 Normal Conversion Sync Pulse
8
ADC_2 Normal Conversion
9
ADC_2 Injected Conversion
10
ADC_2 Normal Conversion Sync Pulse
60.1.6 ADC Self-Test
It is important to check at regular intervals if the ADC is operating correctly. For this purpose a self test feature is provided. When 
self-test is enabled, the ADC automatically checks its components and flags errors.
60.1.7 ADC mux-mode channels
There are some channels in ADC which are driven by multiple pads. For this, GPR bits from DCM are used to define which pad 
is connected to a particular ADC channel.
For example as below, where ADC0 S8 is driven by GPIO_PAD0 (default) and GPIO_PAD45 (mux_mode). ADC2 S8 is driven 
by GPIO_PAD133 (default) and GPIO_PAD45 (mux_mode). ADC1 S8 has a dedicated pad GPIO45, so its TGATE doesn't need 
GPR bit gating. Similar implementation is for ADC0_S9 and ADC2_S9. Following DCM GPR bits have been used:
Table 345. ADC mux_mode GPR
ADC channel
GPR_bit
Connected pad
ADC0 Standard channel 8 (ADC0 S8)
DCM.DCMRWF4[1]
0: GPIO PAD0 (default)
1: GPIO PAD45
ADC0 Standard channel 9 (ADC0 S9)
DCM.DCMRWF4[2]
0: GPIO PAD1 (default)
1: GPIO PAD46
ADC 1 standard channel 14 (ADC1 S14)
DCM.DCMRWF4[3]
0: GPIO PAD69 (default)
1: GPIO PAD32
ADC 1 standard channel 15 (ADC1 S15)
DCM.DCMRWF4[4]
0: GPIO PAD4 (default)
1: GPIO PAD33
ADC1 Standard channel 22 (ADC1 S22)
DCM.DCMRWF4[5]
0: GPIO PAD124 (default)
1: GPIO PAD145
ADC1 Standard channel 23 (ADC1 S23)
DCM.DCMRWF4[6]
0: GPIO PAD125 (default)
1: GPIO PAD146
ADC2 Standard channel 8 (ADC2 S8)
DCM.DCMRWF4[9]
0: GPIO PAD133 (default)
1: GPIO PAD45
ADC2 Standard channel 9 (ADC2 S9)
DCM.DCMRWF4[10]
0: GPIO PAD132 (default)
1: GPIO PAD46
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2335 / 5251


---
# 페이지 27

IO Tgate Cell
GPIO
PAD 0
default_path
gated by (~GPR_bit & sample_enable_ADC0_S8)
in
out
ADC0_S8
ADC1_S8
ADC2_S8
IO Tgate Cell
gated by (GPR_bit & sample_enable_ADC0_S8)
gated by (GPR_bit & sample_enable_ADC2_S8)
gated by (~GPR_bit & sample_enable_ADC2_S8)
GPIO
PAD 45
max_mode_path
default_path
mux_mode_path
PAD shared
across 3 ADCs
in
out
IO Tgate Cell
in
out
IO Tgate Cell
in
out
IO Tgate Cell
in
out
IO Tgate Cell
GPIO
PAD 32
 only gated by sample_enable_ADC0_S14)
in
out
ADC0_S14
ADC1_S14
IO Tgate Cell
gated by (GPR_bit & sample_enable_ADC1_S14)
gated by (~GPR_bit & sample_enable_ADC1_S14)
max_mode_path
default path
in
out
IO Tgate Cell
in
out
PAD 133
GPIO 
PAD 69
GPIO 
Figure 249. ADC channel interleaving
60.2 Overview
ADC produces a digital value from an input analog voltage using the SAR algorithm. It features various methods to trigger a 
conversion and offers flexibility in the selection of input channels. ADC is useful for a wide range of applications.
A configurable self-test capability supports use cases with increased requirements for functional safety.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2336 / 5251


---
# 페이지 28

60.2.1 Block diagram
&
BCTU
trigger
BCTU
trigger
MCR[BCTUEN]
&
1
2 ^ MCR[ADCLKSEL]
Precision
Do conversion#(n+1)
Data capture
MCR[OWREN]
#ch
chsel
st_en
st_step
**DRk[VALID]
1
1
≥1
Input channel
MCR[AVGEN]&
2^(2+MCR[AVGS]) ≠ n
result[14:0]
= raw_result[14:0]
+ error_correction[14:0]
conversion_data[14:0]
= sum_n(result[14:0])/n
Start
Conversion done
conversion_data[14:0]
st_control
inpsamp
Conversion control
SAMPLE
CTU data out
Write outputs
Data read
Data read
MCR[WLSIDE]
PCDRk[CDATA]
ICDRk[CDATA]
ECDRk[CDATA]
STDR1[TCDATA]
DMAE[DCLR]
DMA req
EOC interrupt
Critical flag
Noncritical flag
Self-test interrupt
DMA ack
TIMER WD
reset
end
en
limit
Threshold WD
STCR2[MSK*]
Data read
DMAE[DMAEN]
STAWsR[WDTE]
Ananlog watchdog
Self test Watchdog
STBRR[WDT]
conversion data[14:0]
STAWsR[THR*]
STCR2[FMA_*]
DMAR[DMAk]
&
CIMRi[]
IMR[]
STCR2[MSKWDG_EOA_C]
STCR2[MSKWDG_EOA_S]
*[15:1]
*[14:0]
Standard
External
Internal
FSM
Power down
All inputs converted
IDLE
# ch ≠ m
WAIT
DSDR[]
m++
CONVERT
DONE
PDEDR[]
MCR[PWDN]
MCR[ABORT] ││
MCR[ABORTCHAIN]
Convert
&
Conversion clock
MODULE_CLK
MCR[ACKO]
FSM IDLE
S
R
lnjected
trigger
Priority
Multiplexer
run
Injection
trigger
MCR[JEDGE]
MCR[JTRGEN]
MCR[JSTART]
S
R
Standard
trigger
Self-test
control
trigger
External
start
MCR[XSTRTEN]
MCR[MODE]
MCR[EDGE]
MCR[TRGEN]
STCR2[EN]
STCR3[ALG]
STBRR[BR]
STCR3[MSTEP]
MCR[NSTART]
S
R
1
STCR1[INPSAMP_*]
Channel select
CTRi[INPSAMP]
CTU channel select
MCR[ABORTCHAIN]
NCMRi[CHk]
JCMRi[CHk]
0
1
2
3
type
1
1
1
1
CALBISTREG[RESN]
COMPARE
AVERAGING
1
1
1
S
R
1
1
&
&
1
WTIMR[MSKWDGx*]
*CDRk[CDATA]
THRHLR[THR*]
*CDRk[VALID]
CWENRi[CWENk]
CWSELRx[WSEL_CHy]
&
1
STAWsR[AWDE]
Analog watchdog
interrupt
&
Normal
Figure 250. ADC block diagram
Guide to the diagram:
• The signal flow through the diagram is from left to right: inputs to blocks are on the left side, outputs are on the right.
• Block names have the first letters in uppercase and the other letters in lowercase—"Conversion Control," for example).
• Register names are in uppercase followed by a field name in brackets ("MCR[NSTART]," for example). Letters in lowercase 
are indexes. Asterisks are placeholders for letters (wildcards). Register names in the block diagram map to the names in ADC 
register descriptions.
• Signal names are in lowercase ("conversion done," for example).
• All digital signals shown are synchronous signals. Asynchronous inputs to the ADC are internally synchronized (synchronizers 
not shown).
The block diagram shows the signal flow through ADC from the left to the right and from the top to the bottom:
1. When ADC receives one of the three different types of triggers (BCTU, injected, or normal), the priority multiplexer initiates 
the conversion.
2. The input to be converted is selected in the Channel Select subblock, based on the type of trigger and on the 
self-test configuration.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2337 / 5251


---
# 페이지 29

3. The state machine (FSM) transitions from Idle state to Convert state. In case the channel to convert changed since the last 
conversion and this new channel is an external channel, the conversion starts after a delay configured by DSDR[DSD].
4. After a conversion begins, the Conversion Control block holds the internal capacitance network CDAC in the sample phase 
for a time defined by CTRi[INPSAMP].
5. During the compare phase, CALBISTREG[RESN] defines the number of steps used to execute the successive 
approximation algorithm. The error_correction values, determined during calibration, are added to the raw result. If 
averaging is enabled (MCR[AVGEN] = 1), up to 32 (specified via MCR[AVGS]) conversion results are averaged to obtain 
the result.
6. When the conversion completes and all averaging steps have completed:
a. The conversion done signal indicates completion.
b. Conversion_data[14:0] is written to the result registers in the Data Capture subblock.
c. The FSM transitions into Done state.
7. The next input in the Channel Select block is selected and the next conversion is started by the transition of the FSM to 
Convert state. This continues until all selected inputs have been converted.
8. If an analog watchdog is enabled, the conversion result is compared to the configured threshold. If the limits are exceeded, 
an interrupt can be triggered.
9. Self-test can check the integrity of ADC, either interleaved with normal conversions or as a standalone check.
10. If an ongoing conversion is aborted (by writing 1 to MCR[ABORT]) or an ongoing conversion of a set of input channels 
is aborted (by writing 1 to MCR[ABORTCHAIN]), the FSM transitions into Idle state. The Conversion Control block stops 
the current conversion if MCR[ABORT] was written with 1, or finishes the current conversion if MCR[ABORTCHAIN] was 
written with 1. In both cases, the conversion done output signal of the Conversion Control block is set to 1.
Some details are not shown in the block diagram:
• Calibration must be performed to determine the error_correction values (see Calibration) before ADC can do 
meaningful conversions.
• An input can presample the internal low or high reference voltages to avoid a memory effect that may be present in the 
comparison due to a previous conversion (see Presampling).
• Monitor ADC status via status flags.
— See Main Status (MSR) for the FSM state.
— See Interrupt Status (ISR) to monitor interrupts.
— See Channel End Of Conversion Flag For Precision Inputs (CEOCFR0) for conversion phase per input.
— See the following registers to monitor analog watchdogs:
◦Analog Watchdog Out Of Range For Precision Inputs (AWORR0)
◦Analog Watchdog Out Of Range For Standard Inputs (AWORR1)
◦Analog Watchdog Out Of Range For External Inputs (AWORR2)
See Analog Watchdog Threshold Interrupt Status (WTISR) to monitor analog watchdog interrupts.
— See Self-Test Status 1 (STSR1) – Self-Test Status 4 (STSR4) to monitor self-test.
60.2.2 Features
• Selectable resolution (8-, 10-, 12-, 14-bit). Note that the conversion result is always 15 bits wide, even though the selected 
resolution is smaller (see CALBISTREG[RESN])
• Conversion data captured in a separate register for each input channel.
• Option to improve accuracy via averaging, which calculates conversion data by averaging the data of up to 32 
conversions.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2338 / 5251


---
# 페이지 30

• Conversion triggers:
— Normal conversion trigger converts a number of input channels, either once per trigger or continuously.
— Injected conversion trigger interrupts an ongoing normal conversion and converts another set of input channels.
— BCTU conversion trigger interrupts an ongoing conversion and converts an input channel, in which the input is 
selected and the conversion is started via the BCTU.
• An analog watchdog optionally monitors conversion data for each input channel and issues an interrupt if the converted 
data is below or above configurable limits.
• DMA functionality transfers conversion data to other modules.
• Programmable interrupts optionally issue an interrupt when conversion of one or of a set of input channels is finished.
• Self-test functions validate ADC structural integrity during functional operation and generate events with different 
severities on any finding.
• Conversion clock (AD_clk) control enables the use of ADC in systems with a higher clock frequency by using internal clock 
dividers.
• Auto turn-off of the conversion clock when ADC is idle.
60.3 Functional description
60.3.1 Clock
ADC is controlled by one clock signal, the module clock. Internally, the conversion circuit is controlled by the conversion clock, 
which is derived from the module clock.
The frequency of the conversion clock has to be within the limits defined in the data sheet. If the module clock frequency is higher 
than the maximum frequency of the conversion clock allowed during the functional conversion or during the calibration (see the 
chip data sheet), then you must configure the ADC conversion clock divider (MCR[ADCLKSEL]) so that the frequency of the 
conversion clock is within allowed limits. See Table 346.
Table 346. Clock configuration for highest conversion speeds
Module Clock Frequency f_mc1
Configuration during calibration
Configuration during 
functional conversion
40 MHz < f_mc ≤ 80 MHz
MCR[ADCLKSEL] = 1h
AMSIO[HSEN] = 0h
AMSIO[CMPCTRL0] = 0b
MCR[ADCLKSEL] = 0h
AMSIO[HSEN] = 0h
AMSIO[CMPCTRL0] = 0b
80 MHz < f_mc ≤ 120 MHz
MCR[ADCLKSEL] = 1h
AMSIO[HSEN] = 1h
AMSIO[CMPCTRL0] = 1b
MCR[ADCLKSEL] = 0h
AMSIO[HSEN] = 1h
AMSIO[CMPCTRL0] = 1b
120 MHz < f_mc ≤ 160 MHz
MCR[ADCLKSEL] = 2h
AMSIO[HSEN] = 0h
AMSIO[CMPCTRL0] = 0b
MCR[ADCLKSEL] = 1h
AMSIO[HSEN] = 0h
AMSIO[CMPCTRL0] = 0b
160 MHz < f_mc ≤ 240 MHz
MCR[ADCLKSEL] = 2h
AMSIO[HSEN] = 1h
AMSIO[CMPCTRL0] = 1b
MCR[ADCLKSEL] = 1h
AMSIO[HSEN] = 1h
AMSIO[CMPCTRL0] = 1b
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2339 / 5251


---
# 페이지 31

Table 346. Clock configuration for highest conversion speeds (continued)
Module Clock Frequency f_mc1
Configuration during calibration
Configuration during 
functional conversion
240 MHz < f_mc ≤ 320 MHz
MCR[ADCLKSEL] = 3h
AMSIO[HSEN] = 0h
AMSIO[CMPCTRL0] = 0b
MCR[ADCLKSEL] = 2h
AMSIO[HSEN] = 0h
AMSIO[CMPCTRL0] = 0b
320 MHz < f_mc ≤ 480 MHz
MCR[ADCLKSEL] = 3h
AMSIO[HSEN] = 1h
AMSIO[CMPCTRL0] = 1b
MCR[ADCLKSEL] = 2h
AMSIO[HSEN] = 1h
AMSIO[CMPCTRL0] = 1b
1. Lower resulting frequencies are allowed—see the chip data sheet.
When ADC is not converting (state machine is in Idle state), the conversion clock can be turned off (MCR[ACKO]).
60.3.2 Modes of operation
ADC is always in Functional mode. No other mode selection exists.
• Put ADC into Power Down state by writing 1 to MCR[PWDN] to reduce power consumption.
• Gate the clock signal by writing 1 to MCR[ACKO] when ADC is in Idle state.
60.3.3 Conversion
ADC measures the voltage of a signal—it converts an analog input value into a digital representation. When you read the 
conversion result, you must divide this conversion result by the number of codes (defined by selected conversion resolution 
in CALBISTREG[RESN]), and multiply it with the reference voltage value. This calculation provides the voltage value of the 
converted signal.
To convert an analog input voltage into its digital representation, ADC:
1. Receives a signal, referred to as a trigger, indicating it is to perform a conversion.
2. Captures the voltage of a signal via internal capacitances in a process referred to as sampling.
3. Compares the voltage to the reference voltage, using the SAR algorithm.
Before a conversion can be performed, you must select:
• The trigger source(s) to use (on the chip level)
• The input channel(s) to convert (NCMR0–2, JCMR0–2)
Additionally, you can tailor the conversion to meet your needs by changing the default configuration. For example, you can:
• Configure ADC to convert the selected input channel(s) only once or continuously in a loop (MCR[MODE]).
• Specify the duration that ADC samples the input signal (CTR0/1/2).
• Specify the resolution of the conversion result by selecting the number of bits (CALBISTREG[RESN]).
• Enable an analog watchdog to generate an interrupt when a conversion result falls outside a specified range (see Analog 
watchdog functions).
• Enable the DMA interface to send requests and receive acknowledgments (see DMA functionality).
• Check the operational integrity of ADC by running a self-test (see Self-test).
After power-up or a functional reset, ADC remains in Power Down state until enabled by writing 0 to MCR[PWDN]. After the system 
is powered on, you must run the calibration (see Calibration), before you can do a meaningful conversion with ADC.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2340 / 5251


---
# 페이지 32

Some configuration fields (listed below) are writeable only in Power Down state. If you intend to write to them, you must do so 
before exiting Power Down state.
• Select the conversion clock frequency to be within the allowed limits for a conversion.
60.3.4 Normal trigger
Select the input channels to convert by configuring the fields in NCMR0, NCMR1, and NCMR2.
These registers must be programmed before the start of conversion. You cannot reconfigure them until the conversion of all 
selected channels is complete. The sequence is always to convert the selected input channels in this order:
1. Start from the lowest input channel of the precision input channels.
2. Proceed through the standard input channels in ascending order.
3. End with the highest input channel of the external input channels.
60.3.4.1
Starting conversions in normal conversion mode
After programming the required fields of the following registers, you can start a conversion by writing 1 to MCR[NSTART]:
• Normal Conversion Enable For Precision Inputs (NCMR0)
• Normal Conversion Enable For Standard Inputs (NCMR1)
• Normal Conversion Enable For External Inputs (NCMR2)
• Main Configuration (MCR)
A hardware trigger can also start a normal conversion.
• If the external trigger is enabled (MCR[TRGEN] = 1), an external trigger enable is detected to start the conversion. The enable 
is checked only during start of conversion.
• Detection of an active edge defined by MCR[EDGE] (rising = 1, falling = 0) on an external trigger transitions MCR[NSTART] 
to 1 and starts the normal conversion.
• When MCR[TRGEN] = 1 (for example, when external trigger is enabled), conversion can be started by software.
• Any external trigger or software initiated conversion in normal conversion mode is ignored during any ongoing 
conversion chain.
 
To have reliable operation there must be a gap of 3 clock cycles between configuration of NCMRx and the start 
of a conversion (by writing 1 to MCR[NSTART], or arrival of an external or internal hardware start trigger). ADC 
calculates the number of channels to be converted during this period.
  NOTE  
60.3.4.2
Operation modes in normal conversions
Two operational modes are available during normal conversion:
• One-Shot mode
• Scan mode
For normal conversion, select the mode via MCR[MODE]. The first phase of the conversion process involves sampling the analog 
channel. The next phase is the conversion phase, curing which the sampled analog value is converted to digital as shown in the 
following figure.
Sample E
Convert E
Convert D
Convert C
Sample D
Sample C
Sample B
Convert B
Figure 251. Normal conversion flow
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2341 / 5251


---
# 페이지 33

In One-Shot mode (MCR[MODE] = 0), a sequential conversion specified in the NCMRn mask registers is performed only once. 
At the end of each conversion, the digital result of the conversion is stored in the corresponding data register (CDRn).
For example: Channels A→B→C→D→E→F→G→H are present in a device where channels B→D→E are to be converted in One-Shot 
mode. Conversion begins with channel B, followed by conversion of channels D and E. At the end of conversion of channel E, the 
scanning of channels stops.
MSR[NSTART] automatically transitions to 1 when a normal conversion starts. At the same time, MCR[NSTART] is reset to zero 
by hardware, enabling software to program a new start of conversion in advance. In this case, the new requested conversion 
starts after completion of the running/current conversion. However, for correct functioning of the device, you should program 
MCR[NSTART] for the new conversion only after completion of the current conversion. The application can wait for an ECH 
interrupt prior to writing 1 to MCR[NSTART] again.
If an external trigger starts the conversion chain, ADC does not observe the trigger input until the conversion chain is finished. After 
the chain is finished, the next chain can be triggered by another hardware trigger edge.
In Scan mode operation (MCR[MODE]=1), a sequential conversion of N channels specified in the NCMRn registers is 
continuously performed. At the end of each conversion, the result is stored in the corresponding data register, as in One-
Shot mode.
MSR[NSTART] automatically transitions to 1 when a normal conversion starts. Unlike One-Shot mode, MCR[NSTART] is not reset 
to 0 in Scan mode. It can be reset by software when you must exit Scan mode. In that case, ADC completes the current chain and 
after the last conversion, it resets MCR[NSTART] to 0.
For example: Channels A→B→C→D→E→F→G→H are present in the device where channels B→D→E are to be converted in Scan 
mode. MCR[MODE] = 1 selects Scan mode operation. Conversion starts from channel B followed by conversion of channels 
D→E. After conversion of channel E, the scanning of channel B starts followed by conversion of the channels D→E. This sequence 
repeats itself until MCR[NSTART] is reset to 0 by software.
If an external trigger starts a conversion, then MCR[NSTART] does not transition to 1. This scan chain can be stopped by writing 
0 to MCR[NSTART]. The conversion stops when the ongoing chain is finished. Consequently, after it starts, the only way to stop 
Scan mode conversion is to write 0 to MCR[MODE].
End of conversion
In both modes, at the end of each conversion, an End of Conversion (EOC) interrupt is issued if enabled by the corresponding 
mask fields in CIMRn and IMR).
After conversion of all selected channels in NCMRn is complete, the conversion operation is considered finished. Then ISR[ECH] 
transitions to 1 and the End of Chain (ECH) interrupt is issued (if enabled in IMR[MSKECH]).
The corresponding channel field in the CEOCFRn register(s) is updated to indicate that data is available on data register CDRn 
of the respective channel.
If there is no channel selected in NCMRn and there is a start-of-conversion trigger, then ISR[ECH] is set to 1 and the End of Chain 
(ECH) interrupt is immediately issued (if enabled).
60.3.5 Injected trigger
An injected trigger enables you to convert a set of input channels although the standard trigger has already started conversion of 
another set of input channels. Each channel can be individually enabled by writing 1 to the corresponding field in JCMR0, JCMR1, 
or JCMR2.
The set of input channels of the injected trigger is converted only once. A continuous conversion of a set of input channels in 
a loop is only possible when started by a standard trigger. When an injected trigger is received, an ongoing conversion started 
by a standard trigger is interrupted. After the set of input channels of the injected trigger is converted once, the interrupted 
conversion of the set of input channels of the standard trigger resumes from the input channel that was interrupted, as shown in 
the following figure.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2342 / 5251


---
# 페이지 34

Sample B
Sample C
Convert C
Sample D
Convert D
Sample E
Convert E
Convert B
Sample C
Sample I
Convert I
Conversion resumes from the last aborted
channel of the chain executed in Normal
Conversion mode.
Injected conversion of channels l and J
When an injected conversion is triggered, the ongoing conversion 
chain is suspended (current channel conversion aborted) and the 
injected conversion chain is processed. After the injected chain is 
complete, the suspended conversion chain resumes from the 
channel at which conversion was aborted in Normal Conversion 
mode.
Sample J
Convert J
Sample C
Convert C
Abort C
Figure 252. Injected trigger conversion sequence
60.3.5.1
Starting conversions in injected conversion mode
An injected conversion chain can be started:
• By software: When external triggering is disabled (MCR[JTRGEN] = 0), you can write 1 to MCR[JSTART], which causes the 
current conversion chain processed in Normal Conversion mode to be suspended and the injected chain to be processed.
• By external trigger: When external triggering is enabled (MCR[JTRGEN] = 1), a programmed event (rising/falling edge 
depending on the value of MCR[JEDGE]) on the injection external input starts the injected conversion.
MCR[JSTART] automatically transitions to 1 when the injected conversion chain starts. At the same time MCR[JSTART] is reset 
to 0, enabling software to program a new start of conversion in advance. In that case the new requested conversion starts after 
the running conversion completes.
At the end of each conversion, an End Of Injected Conversion (JEOC) interrupt is issued, if enabled by the corresponding mask 
field in Interrupt Mask (IMR). At the end of a chain, an End Of Injected Chain (JECH) interrupt is issued, if enabled by the 
corresponding mask field. Additionally, ADC writes 1 to ISR[JECH].
 
If the content of all the Injected Conversion mask registers (JCMRn) is zero, that is, no channel is selected, the 
JECH interrupt is immediately issued after the start of conversion.
To have reliable ADC operation, there must be a gap of 3 cycles between configuration of JCMRx and starting 
of conversion (writing 1 to MCR[JSTART] or arrival of either an external or internal hardware start trigger). ADC 
calculates the total channel numbers to be converted during this period.
  NOTE  
The corresponding channel bit in the CEOCFRn register is updated to indicate data is available in the channel's conversion data 
register, CDRn.
After starting, an injected chain conversion cannot be interrupted.
60.3.6 BCTU interface
The BCTU interface enhances ADC's injected conversion capability. It contains control inputs to select the channels to be 
converted from the appropriate event configuration register. Figure 253 shows the interface.
The BCTU generates a trigger (bctu_trigger) and a channel number (bctu_numchannel) to be converted. A single channel is 
converted for each request. After performing the conversion, ADC returns the result on the bctu_dataout bus together with two 
output signals named bctu_nextcmd and bctu_push. The assertion of signal bctu_nextcmd means ADC is ready to accept the 
next trigger from BCTU. The bctu_push signal is asserted at the end of conversion, meaning that conversion is finished and the 
conversion result available at output bctu_dataout is valid.
The conversion result is also saved in the corresponding channel's data register and is compared with analog watchdog thresholds 
if requested.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2343 / 5251


---
# 페이지 35

The signals bctu_trigger, bctu_nextcmd and bctu_push are all of type single-cycle active-high-pulse in the ADC clock domain. 
The channel number provided from BCTU must be valid when bctu trigger is active-high. The result data from ADC is valid with 
bctu_push high.
BCTU
Trigger
Channel
Next command
End of conversion
Data [11:0]
ADC
Figure 253. BCTU interface
The BCTU interface has two modes of operation:
• Trigger
• Control
To enable the BCTU interface, write 1 to MCR[BCTUEN]. The operating mode (Trigger or Control) can be fixed or programmable.
60.3.6.1
BCTU Trigger mode
In Trigger mode, normal and injected conversions can also be performed. All types of conversions can be initiated in this mode. 
The priorities among the three types of conversions are discussed below.
When a trigger is received, the channel number is taken as an injected channel value and the triggered injected conversion starts. 
MSR[BCTUSTART] transitions to 1 automatically at this point and it is also automatically reset to 0 when the triggered injected 
conversion is completed.
BCTU conversions must be requested only after successful ADC calibration. The application must prevent any BCTU trigger 
during calibration.
If a BCTU trigger is received during an ongoing injected conversion, the injected chain is aborted immediately and only the 
BCTU-triggered injected conversion proceeds. Additionally, MSR[JSTART] is reset to zero. The abort of an injected conversion 
is indicated by MSR[JABORT].
If a BCTU trigger is received during an ongoing normal conversion, the ongoing normal channel conversion is suspended and the 
BCTU-triggered injected conversion is processed. Normal conversion resumes from the suspended channel after completion of 
the BCTU-triggered conversion.
If a normal conversion is requested during BCTU conversion (MSR[BCTUSTART] = 1), the normal conversion starts after the 
BCTU conversion completes (MSR[BCTUSTART] is reset to zero).
Any injected conversion is discarded if requested during BCTU conversion and MCR[JSTART] is immediately reset to zero.
60.3.6.2
BCTU Control mode
In BCTU control mode (MCR[BCTU_MODE] = 0), only the BCTU can start a conversion. All other trigger sources are ignored.
Along with BCTU trigger, the information provided with signal bctu_numchannel is taken as the channel number for injected 
channel and BCTU triggered conversion starts. MSR[BCTUSTART] transitions to 1 automatically at the start of the conversion 
and it remains 1 unless BCTU is disabled by writing 0 to MCR[BCTUEN].
The conversion must be requested (generating bctu_trigger) when calibration has finished successfully. If a BCTU trigger is 
received during calibration execution, calibration is stopped immediately in order to satisfy the BCTU request. Calibration fails in 
this case.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2344 / 5251


---
# 페이지 36

60.3.7 Aborting a conversion
Two abort functions are provided:
• Abort of a single channel
• Abort of a chain
To abort an ongoing conversion, write 1 to MCR[ABORT]. The current conversion aborts and conversion of the next channel of 
the chain begins immediately.
Depending on the current state of a conversion, an Abort action may take 1 to 4 cycles of the bus clock. At the start of any 
conversion, and at the end of a particular conversion when internal state counters are changing, an abort action is delayed by a 
maximum of 3 cycles to put all states in a stable condition.
To ensure that the abort action completes, do not change MCR[ABORT] for the next 3 cycles.
Avoid writing 1 to MCR[ABORT] along with, and within 3 cycles of, writing 1 to MCR[NSTART] or MCR[JSTART].
During an abort:
• MCR[NSTART] and MCR[JSTART] remain 1, if not in the last channel of the chain.
• MCR[ABORT] is reset to 0 when the channel is aborted.
• The EOC interrupt corresponding to the aborted channel is not generated. This behavior applies to normal and injected 
conversions. If the last channel of a chain is aborted, the end of chain is reported by generating an ECH interrupt.
It is possible to abort the current chain of conversions by writing 1 to MCR[ABORTCHAIN]. In this case, the behavior of ADC 
depends on the value of MCR[MODE] (One-Shot/Scan operation modes). If Scan operation mode is disabled, MCR[NSTART] is 
automatically reset to 0 along with MCR[ABORTCHAIN]. Otherwise, in Scan Operation mode, a new chain is started. The EOC 
interrupt of the current aborted conversion is not generated but an ECH interrupt is generated to signal the end of the chain.
 
For a single channel chain, an ECH interrupt is not generated for an abort or abort chain.
  NOTE  
When an abort chain is requested while an injected chain is running over a suspended normal chain, both the injected and normal 
chains are aborted, and both MCR[NSTART] and MCR[JSTART] are reset to 0.
60.3.8 Configuring ADC clock divider and sample time settings
You can scale the AD_clk frequency via MCR[ADCLKSEL]. ADCLKSEL can only be written in Power Down state 
(MCR[PWDN] = 1). Depending on the frequency of the module clock, there might be different settings necessary for functional 
conversion and for calibration. See the chip data sheet for ADC electrical characteristics.
Three conversion timing registers are used (CTRn) to support different sampling times for the different types of channels. An 
exception exists for the temperature sensor channel, which always uses the Conversion Timing For Standard Inputs (CTR1) value. 
See the register description for details.
60.3.9 Presampling
The presampling feature enables pre-charge or discharge of the ADC internal sample capacitor node to a defined level before 
sampling of the selected analog input channel starts. This is useful for resetting information (history effect/offset) from the most 
recent conversion. During presampling, ADC samples the internally generated voltage. During the sampling phase, ADC samples 
analog input coming from pads.
Enable presampling on a per-channel basis by setting the corresponding fields in the PSRn registers to one.
After enabling presampling for a channel, the normal sequence of operation for the channel is:
1. Presampling
2. Sampling
3. Evaluation
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2345 / 5251


---
# 페이지 37

You can bypass sampling of all channels by writing 1 to PSCR[PRECONV]. When sampling of a channel is bypassed, the sampled 
and stored internal voltage applied during the presampling phase is converted (Figure 254). See Conversion time for the timing 
equation for conversion.
Presampling does not apply for self-test channels.
Sample B
Presample C
Convert C
Sample D
Convert B
Presampling is enabled in channels C and D
Total conversion clock cycles for channel B = S + C
Total conversion clock cycles for channel C and D = (P) + (S) + (C)
Sample C
Presample D
Convert D
Sample E
Figure 254. Presampling sequence
Sample B
Presample C
Presample D
Sample E
Convert E
Convert B
Presampling is enabled in channels C and D  but sampling is bypassed in these channels by writing 1
to PSCR[PRECONV]
Total conversion clock cycles for channel C and D = (P) + (C)
Convert C
Convert D
Figure 255. Presampling sequence with PRECONV=1
60.3.9.1
Enabling presampling per channel
Enable presampling for specific channels by programming Presampling Control (PSCR). You can select between two internally 
generated voltages by configuring the PREVALn fields in Presampling Control (PSCR) to the appropriate values, as given in the 
following table.
Table 347. Presampling voltage selection via PREVALn
PREVALn
Presampling voltage
0
Presample voltage – 0: VREFL
1
Presample voltage – 1: VREFH
The presampling configuration field(s) (PSCR[PREVAL0], PSCR[PREVAL1], PSCR[PREVAL2]) are located in Presampling 
Control (PSCR). These fields enable selection of the presampling channel.
The temperature sensor channel has an exception. This channel is mapped with a fixed channel depending on device 
configuration, but it uses the presampling configuration defined for channel group 2. So, when the temperature sensor channel is 
selected, the presampling voltage defined by PSCR[PREVAL1] is selected. This voltage might be different from the one selected 
for channel group 1 via PSCR[PREVAL0].
60.3.10 Analog watchdog functions
When enabled, an analog watchdog monitors conversion results for an associated channel and reports an issue if it determines 
a result is outside customer-defined limits (as shown in Analog watchdog configuration (up to 16 watchdogs) ). These limits are 
specified by an upper and a lower threshold value named THRH and THRL respectively.
After the conversion of the selected channel a comparison is performed between the converted value and the threshold values. 
If the converted value is outside that threshold value, then ADC generates a corresponding threshold violation interrupt.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2346 / 5251


---
# 페이지 38

The comparison result is stored as HAWIFx and LAWIFx fields in Analog Watchdog Threshold Interrupt Status (WTISR), as 
explained in the following table. Depending on the values of WTIMR[LAWIFENx] and WTIMR[HDWIFENx] mask fields, an 
interrupt is generated on a threshold violation.
Table 348. Values of HAWIFx and LAWIFx
HAWIFx
LAWIFx
Conversion result
1
0
Conversion result > THRH
0
1
Conversion result < THRL
0
0
THRH ≥ conversion result ≥ THRL
Depending on the chip's factory settings, up to 16 analog watchdogs are available. See the chip-specific configuration information 
for availability.
There are two types of mutually exclusive settings for analog watchdogs. Both types are described in the following sections. The 
availability depends on device configuration. See the chip-specific configuration information for availability.
Different capabilities are available with the two settings, as described below.
60.3.10.1
Channel analog watchdog select registers
ADC configuration includes selecting the analog watchdog threshold register (THRHLRn) that provides limits to monitor inputs of 
a given type. You select the THRHLRn using CWSELRaIn registers.
Table 349. CWSELRaIn register naming
Index
Description
a
ADC input type associated with a CWSELRaIn register.
• P = Precision inputs
• S = Standard inputs
• E = External inputs
n
0-indexed register number.
60.3.10.2
Analog watchdog configuration (up to 16 watchdogs)
ADC can have up to 16 watchdogs in the factory configuration. (See the chip-specific configuration information for availability.) 
For each watchdog there is one threshold value register, THRHLRn, that contains the high and low thresholds.
You can independently enable the analog watchdog for each channel by programming the appropriate CWENRn register.
The threshold values for each channel can be selected independently from a maximum of 16 threshold registers (THRHLRn) using 
the corresponding WSEL_CHn field in the appropriate CWSELRaIn, where a indicates the input type:
• P = precision
• S = standard
• E = external
Each CWSELRaIn register is associated with 8 consecutive channels. CWSELRaI0 holds 8 WSEL_CH fields for channels 0 to 7. 
CWSELRaI1 is for channels 8 to 15 and so on. The availability of fields and registers depends on device configuration. See the 
chip-specific configuration information for availability.
If the conversion result of a selected channel is outside the range specified by threshold values, then the corresponding field in the 
Analog Watchdog Out of Range register (AWORRn) transitions to 1. For example, if channel 7 is to be monitored with the threshold 
values in THRHLR3, then CWSELRaI0[WSEL_CH7] must be programmed with 3. Enabling the watchdog is done by writing 1 to 
the corresponding field for channel 7 in CWENR0.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2347 / 5251


---
# 페이지 39

In this configuration, a set of threshold values (THRHLRn) can be linked to several ADC channels.
THRH
THRL
Analog voltage
Upper threshold
Lower threshold
Guarded area
Figure 256. Guarded area
 
If the higher threshold of the analog watchdog is programmed below the lower threshold and the conversion 
result is below the lower threshold, then the WDGnL interrupt for the low threshold violation transitions to 1. If the 
conversion result is greater than the lower threshold (and therefore also greater than the higher threshold), then 
the interrupt WDGnH for high threshold violation is generated. Thus you should take care to avoid that situation, 
as it could lead to misinterpretation of the watchdog interrupts.
  NOTE  
60.3.11 DMA functionality
Conversion result data from any channel can be transferred from a register to system memory via Direct Memory Access (DMA). 
DMA transfers are enabled by writing 1 to DMAE[DMAEN]. After being enabled, the on-chip DMA controller can receive a DMA 
request after the conversion of each channel by writing 1 to the respective masking field in:
• DMA Request Enable For Precision Inputs (DMAR0)
• DMA Request Enable For Standard Inputs (DMAR1)
• DMA Request Enable For External Inputs (DMAR2)
DMA masking registers must be programmed before starting any conversion.
A DMA request to the DMA controller can be cleared at different times in two modes:
• Mode-1: Clearing of DMA request on acknowledgment from DMA controller (DMAE[DCLR] = 0)
• Mode-2: Clearing of DMA request on read to data registers (DMAE[DCLR] = 1)
The figures below show the operation of DMA in two modes (cycle counts are typical values).
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2348 / 5251


---
# 페이지 40

Clock
Clearing of DMA
request on ACK
12 cycles
6 cycles
DMA request
DMA acknowledge
DMA data read
Figure 257. DMA operation Mode-1 (DMAE[DCLR] = 0)
Clock
Clearing of DMA request
on read to data register
One cycle fixed delay
DMA request
DMA acknowledge
DMA data read
Figure 258. DMA operation Mode-2 (DMAE[DCLR] = 1)
60.3.12 Interrupts
ADC generates the following maskable interrupts:
• EOC (End of Conversion)
• ECH (End of Chain)
• JEOC (End of Injected Conversion)
• JECH (End of Injected Chain)
• EOBCTU (End of BCTU-triggered Conversion)
• LAWIFx and HDWIFx (Watchdog threshold)
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2349 / 5251


---
# 페이지 41

• Self-testing interrupts
Interrupts are generated during the conversion process to signal events such as End Of Conversion (EOC), and so on, as 
described in Interrupt Status (ISR). ISR and another register, Interrupt Mask (IMR), are provided to check and enable the interrupt 
request to an external interrupt controller.
Interrupts can be individually enabled on a per-channel basis by programming EOC Interrupt Enable For Precision 
Inputs (CIMR0).
CEOCFRn are used for pending End of Conversion interrupts, with one field per channel to indicate completed conversions on a 
per-channel basis.
Interrupts generated due to the analog watchdogs are managed by two 32-bit registers, Analog Watchdog Threshold Interrupt 
Status (WTISR) and Analog Watchdog Threshold Interrupt Enable (WTIMR), to check and enable the interrupt request. A 
watchdog interrupt causes two corresponding fields to transition to 1 for each channel monitored. One field is in WTISR[WDGnH] 
and another in WTISR[WDGnL].
Generated events are logged into status registers and used to generate interrupts if enabled in corresponding Mask registers.
There are three different interrupt outputs. The interrupt structure is shown in Figure 259.
Each interrupt is generated by combining a group of events.
The following interrupts are combined (logic OR) into one interrupt output.
• EOC
• ECH
• EOBCTU
• JEOC
• JECH
• End of self-test algorithm (WDG_EOA_S and WDG_EOA_C)
Interrupts of all HDWIFx and LAWIFx are combined on the second interrupt output.
Interrupts of all self-test errors (watchdog threshold, sequence, and timer violations) in Self-Test Status 1 (STSR1) are combined 
on the third interrupt output. The errors are:
• WDSERR
• WDTERR
• ERR_S0
• ERR_S1
• ERR_S2
• ERR_C
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2350 / 5251


---
# 페이지 42

AND
AND
AND
AND
OR
AND
AND
AND
CIMRx[CIMn]
CEOCFRx[EOCCHn]
AND
OR
STCR2[MSKWDG_EOA_C]
STSR1[WDG_EOA_C]
AND
WTIMR[HDWIFENx]
WTISR[HAWIFx]
AND
AND
WTIMR[LAWIFENx]
WTISR[LAWIFx]
AND
STCR2[MSKERR_S0]
STSR1[ERR_S0]
AND
STCR2[MSKERR_S1]
STSR1[ERR_S1]
AND
STCR2[MSKERR_S2]
STSR1[ERR_S2]
AND
STCR2[MSKERR_C]
STSR1[ERR_C]
AND
STCR2[MSKWDTERR]
STSR1[WDTERR]
AND
STCR2[MSKWDSERR]
STSR1[WDSERR]
OR
STCR2[MSKWDG_EOA_S]
STSR1[WDG_EOA_S]
IMR[MSKJEOC]
ISR[JEOC]
STCR2[MSKST_EOC]
STSR1[ST_EOC]
IMR[MSKEOC]
ISR[EOC]
IMR[MSKJECH]
ISR[JECH]
IMR[MSKECH]
ISR[ECH]
IMR[MSKEOBCTU]
ISR[EOBCTU]
EOC [Injected]
(jeoc_irq)
ECH [Injected]
(jeoh_irq)
EOC [Normal]
(eoc_irq)
EOC [BCTU]
(eobctu_irq)
Self-test completion
(st_eoc_int)
ECH [Normal]
(ech_irq)
OR
OR
Combined interrupt 2
Analog watchdog
errors
(ipi_int_wd)
Combined interrupt 1
EOC
ECH
Self-test algorithm
(ipi_int_eoc)
Combined interrupt 3
Self test
errors
(ipi_int_er)
Figure 259. Interrupt structure of ADC
Interrupt Status (ISR) Indicates the interrupt pending request status. Write 1 to the corresponding status field to clear the pending 
interrupt flag (at this write operation all the other fields in Interrupt Status (ISR) must be maintained at 0).
ISR checks for three types of interrupts.
The first type, Interrupt 1, relates to the following:
• End of normal or injected conversion (EOC or JEOC)
• End of normal or injected conversion chain (ECH or JECH)
• End of algorithm C or algorithm S self-test (WD_EOA_C or WD_EOA_S)
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2351 / 5251


---
# 페이지 43

Perform the following actions for this type of interrupt:
1. Read Interrupt Status (ISR) to determine whether the event is an EOC, JEOC, ECH, JECH, or EOBCTU event.
2. Read Self-Test Status 1 (STSR1) to identify the end of self-test algorithm events (WDG_EOA_S or WDG_EOA_C), 
if present.
3. If the interrupt is an EOC or JEOC event:
• Clear the respective channel pending field in the appropriate CEOCFRn register for an EOC by writing a 1 to it.
• Clear ISR[EOC] or ISRJEOC] by writing a 1 to it.
4. If the interrupt is an ECH or JECH, clear ISR[ECH] or ISR[JECH] by writing 1 to it.
5. If the interrupt is EOBCTU, clear ISR[EOBCTU] by writing 1 to it.
6. If the interrupt is for self-test end of algorithm, clear STSR1[WDG_EOA_S] or STSR1[WDG_EOA_C] by writing 1 to it.
The second type, Interrupt 2, relates to analog watchdog errors. Perform the following actions for this type of interrupt:
1. Read Analog Watchdog Threshold Interrupt Status (WTISR) to determine which watchdog triggered the interrupt.
2. Read the AWORRx register(s) to determine which channel's data caused the interrupt (if present).
3. Clear the respective field of the WTISR[WDGnH/WDGnL] register, where n = watchdog number, by writing 1 to it.
4. Clear the respective field of the AWORRn[AWOR_CHn] register, where x = register, n = channel, by writing 1 to it.
The third type, Interrupt 3, relates to self-test errors. Perform the following actions for this type of interrupt:
1. Read Self-Test Status 1 (STSR1) to determine the type of error encountered in self-test (WDSERR, WDTERR, ERR_S0, 
ERR_S1, ERR_S2, ERR_C, and so on) if present.
2. Clear the respective field in Self-Test Status 1 (STSR1) by writing 1 to it.
The connectivity of interrupt lines at the chip level (external to ADC) determines whether software must read all the registers for 
all three interrupts or any one or combination of any two.
60.3.13 External decode signals delay
The ADC provides three external decode signals which it uses to select one channel out of eight in the external analog 
multiplexers. There can be a maximum of four such multiplexers used to connect the 32 external channels. The ADC automatically 
sets the decode signals to control these external analog multiplexers, based on the current channel selected for conversion. Delay 
Start Of Data Conversion (DSDR) is provided to take the switching time of the external analog multiplexer into account. It enables 
you to program the delay between the decoding signal selection and the actual start of conversion.
If presampling is enabled, the DSD delay starts after the presample phase (presampling time is the same duration as sample time).
60.3.14 Power Down state
The analog part, along with the ADC controller, can be put in Power Down state by writing 1 to MCR[PWDN]. This shuts down ADC 
and stops the clock to the ADC controller. After release of reset, MCR[PWDN] remains 1, so the ADC analog module is kept in 
Power Down state by default. You must exit this state before starting any operation, by writing 0 to MCR[PWDN]. In Power Down 
state, no conversion can be started. If a BCTU trigger pulse is received during this state, it is discarded. You must ensure that a 
BCTU trigger is not initiated to ADC before writing 0 to MCR[PWDN], as it may cause the BCTU module to be stuck in a wait state.
You can set MCR[PWDN] by writing 1 to it at any time. If a conversion is ongoing, ADC does not move into Power Down state 
immediately. ADC enters Power Down state only after completion of the ongoing conversion. During scan operation, the ongoing 
operation should be aborted manually by writing 0 to MCR[NSTART] before or after writing 1 to MCR[PWDN].
ADC Power Down state status is indicated by MSR[ADCSTATUS] when ADC enters into Power Down state.
If the BCTU is enabled and MSR[BCTUSTART] = 1, then you cannot write 1 to PWDN. When BCTU Trigger mode is enabled, 
the application must wait for the end of conversion (MSR[BCTUSTART] is automatically reset to 0). When BCTU Control mode 
is enabled, before entering Power Down state the application must write 0 to BCTUEN also.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2352 / 5251


---
# 페이지 44

If Power Down state is entered by writing 1 to MCR[PWDN], the process running before entry into Power Down state must be 
restarted manually (by writing 1 to the appropriate START field in Main Configuration (MCR)) after exiting Power Down state.
 
Writing 0 to MCR[PWDN] and writing 1 to MCR[NSTART] or MCR[JSTART] during the same cycle is not supported.
  NOTE  
60.3.15 Low Power mode support
For low-power operation, ADC must be in Idle state and then put into Power Down state to ensure proper signal condition at the 
analog boundary.
From any of the states listed below, follow the sequence of steps shown to put ADC into Power Down state.
1. Idle condition
a. Verify that ADC is in Idle state (MSR[ADCSTATUS] = 000b).
b. Write 1 to MCR[PWDN], to shut off the clock to the hard macro with the proper state of signals required for Low 
Power mode.
c. Verify that ADC is in Power Down state (MSR[ADCSTATUS] = 001b).
2. During calibration
 
Writing 1 to MCR[PWDN] during calibration is prohibited. After calibration is started it should be allowed to finish 
normally. Alternatively, it can be terminated by starting a normal conversion before writing 1 to MCR[PWDN].
  NOTE  
a. Check the current ADC state either via MSR[ADCSTATUS] (000b = Idle, 011b = Calibration), or via 
CALBISTREG[C_T_BUSY] (1 = calibration is in progress).
b. When ADC is in Idle state, write 1 to MCR[PWDN] to shut off the clock to the hard macro with the proper state of 
signals required for Low Power mode.
c. Verify that ADC is in Power Down state (MSR[ADCSTATUS] = 001b).
3. During conversion (normal [one-shot]/Injected/BCTU):
a. Write 1 to MCR[PWDN].
b. ADC enters Power Down mode after completing the current conversion chain (for normal and injected conversions) 
or the conversion for conversion triggered by BCTU.
c. Check the ADC state via MSR[ADCSTATUS] (000b = Idle state, 001b = Power Down state).
4. During Scan mode operation of normal conversion
 
Writing 1 to MCR[PWDN] during scan mode operation has no effect other than to prevent software from starting 
a new normal or injected conversion. It does not stop a conversion in progress and cannot put ADC into Power 
Down state.
  NOTE  
a. Software must write 0 to MCR[NSTART] to stop the ongoing scan conversion before (or after) writing 1 to 
MCR[PWDN]. This stops conversion at the current chain boundary.
b. ADC enters Power Down mode after coming to an Idle state after MCR[PWDN] is written with 1. This shuts the clock 
off to the hard macro and puts analog inputs in the proper state required for Low Power mode.
c. Verify that ADC is in Power Down state (MSR[ADCSTATUS] = 001b).
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2353 / 5251


---
# 페이지 45

60.3.16 Auto Clock Off mode
To reduce power consumption during Idle state (without going into Power Down state), an auto-clock-off feature can be enabled 
by writing 1 to MCR[ACKO]. When enabled, the internal ADC operating clock (AD_Clk) is automatically switched off during an idle 
period (for example, no conversion is programmed).
60.3.17 Calibration and self-test
60.3.17.1
Calibration
ADC must be calibrated before it can do meaningful conversions. The application must prevent any start of conversion before the 
ongoing calibration has finished successfully. No conversion trigger may be received during calibration.
During calibration, a known reference voltage is sampled and converted under controlled conditions to determine the correction 
values (calibration values) for offset, gain, and capacitor mismatch.
These calibration values (except gain calibration) are used in a post-processing step after conversion, reducing or eliminating the 
various error contribution effects. The gain calibration is used during sample phase to define the additional charge to be loaded 
to compensate for gain failure.
You must run calibration after every power-up reset (check device-specific reset connectivity for appropriate reset applied). You 
must also run calibration if it is indicated by the self-test (see Self-test).
Configuration and start of calibration is done by programming the Control And Calibration Status (CALBISTREG). During 
calibration, internal hardware averaging function should be enabled. Maximum averaging is recommended, and 16 should be 
the minimum.
Calibration status is captured by a status flag (CALBISTREG[TEST_FAIL]) to indicate any fault detected during calibration 
execution or if calibration was prematurely aborted. Calibration is aborted if any normal conversion is initiated during the calibration 
execution, which is called premature termination. (Flag TEST_FAIL = 1 indicates a calibration fail, for example when a calibration 
value is out of internally defined limits.)
To execute the calibration algorithm, perform the following steps:
1. Select the conversion clock frequency to be within the allowed limits for the calibration.
2. Bring ADC from Power Down state to active conversion (program MCR[PWDN] = 0b).
3. Configure the Control And Calibration Status (CALBISTREG). The default values are set for maximum accuracy 
(recommended).
4. Disable the error correction for the smaller capacitances in the CDAC of the ADC (write 0h to CAL2[ENX]).
5. Start calibration (program CALBISTREG[TEST_EN] = 1b), and calibration starts immediately.
6. Poll the status of CALBISTREG[C_T_BUSY] for 0 (wait until it transitions to 0).
7. Check CALBISTREG[TEST_FAIL] to determine the final status. If 1, then calibration failed.
8. Check the status of MSR[CALIBRTD]. If calibration was successful this field is 1.
60.3.17.2
Self-test
For safety applications, it is important to verify correct operation at regular intervals. ADC has a self-test feature for this purpose. 
When self-test is enabled, ADC automatically checks its components and flags errors, if any are found.
Tests can be enabled to check the reference (VrefH) and calibrated values.
The following test algorithms have been implemented:
• Supply self-test (algorithm S): It includes the conversion of the band gap and VREF voltages. It includes a sequence of 
num_supply_steps test conversions (steps). The supply test conversions must be an atomic operation (that is, all supply 
algorithm conversions must be performed one after another with no functional conversions in between).
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2354 / 5251


---
# 페이지 46

• Capacitive self-test (algorithm C): It includes a sequence of test steps per definition of algorithm C (see Table 350) which 
executes the capacitive matrix of the CDAC used for sampling and conversion.
Individual steps can take up to 1 µs at 80 MHz ADC clock frequency.
Table 350. Self-test steps
STCR3[ALG]
STCR3 
[step](per 
algorithm 
definition)
Description
Outcome
Comment
00 (algorithm S)
0
Supply self-test (band 
gap voltage)
Measures the internal band gap 
voltage
1
Supply self-test 
(reference voltage 
high)
Measures ADC high reference 
voltage
2
Supply self-test 
(reference voltage 
high)
Measures ADC high reference 
voltage
01 (Reserved)
Reserved
10 (algorithm C)
0 – 11
Capacitive self-test. 
One of the calibration 
steps is being run.
The difference/error of the 
individual offset value from the 
previously calibrated value is 
being returned as an ADC 
result that is compared with the 
programmed value in the self-
test analog watchdog register(s) 
to detect any fault.
The ideal result value is 
expected to be 0. If the returned 
value is higher, it indicates a 
runtime fault or accuracy shift. 
The error is indicated in the 
status register and can be used 
to generate an interrupt also. It 
that indicates ADC should be 
recalibrated to check whether 
the reported error can be 
managed by calibration or that 
permanent damage occurred to 
ADC.
11 (algorithm 
S + C)
0 – 2 (S), 0 –
 11 (C)
Supply for One-
Shot mode and 
(supply + capacitive) 
for Scan mode only.
Same as above.
ADC:
• Schedules self-testing algorithms using configuration registers.
• Monitors the converted data using analog watchdog registers.
• Flags any errors to a fault control unit (FCCU), if one exists.
Self-test steps can be activated from software (CPU) or BCTU.
ADC mode
TEST algorithm (CPU)
TEST algorithm/step (BCTU)
CPU mode (MCR[BCTUEN] = 0)
Yes
No
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2355 / 5251


---
# 페이지 47

Table continued from the previous page...
ADC mode
TEST algorithm (CPU)
TEST algorithm/step (BCTU)
• One-Shot operation mode
• Scan operation mode
BCTU mode
No
Yes
60.3.17.2.1
CPU mode
In this mode, self-test conversion is similar to normal conversion. You enable self-test by writing 1 to STCR2[EN].
Self-test conversions execute along with the functional conversions. The sequencing of steps of the selected algorithm depends 
on the operating mode of normal conversions (selected by MCR[MODE]).
In One-Shot operation mode, if self-test is enabled, only one step of the selected self-testing algorithm is executed at the end of 
the chain. The step number and algorithm to be executed are programmed in Self-Test Status 3 (STSR3). In One-Shot operation 
mode the sequence is:
1. Program NCMRn to select channels to be converted for normal conversion.
2. Write 0 to MCR[MODE] to select one-shot operation.
3. Configure the self-test algorithm threshold values (see Table 351).
4. Program sampling duration values in STCR1[INPSAMPm] (m = S, C).
5. Select the self-testing algorithm (in STCR3[ALG]), and step (in STCR3[MSTEP]). The default is algorithm S, step 0.
6. Enable self-testing by writing 1 to STCR2[EN].
7. Start the normal conversion by writing 1 to MCR[NSTART].
8. All normal conversions are executed as usual.
9. At the end of all normal conversions in the chain, the step number (programmed in STCR3[MSTEP]) of the self-testing 
algorithm (selected by STCR3[ALG]), is executed similar to a normal functional channel.
10. At the end of the conversion for the self-test channel:
• The result is written to STDR1[TCDATA].
• STDR1[VALID] transitions to 1.
• ISR[EOC], ISR[ECH], and STSR1[ST_EOC] transition to 1.
11. ADC returns to Idle state.
For example: Channels A→B→C→D→E→F→G→H are present in the device where channels B→D→E are to be converted in 
One-Shot operation mode. At the end of conversion for channels B→D→E, self-test conversion is performed and ISR[ECH] and 
ISR[EOC] transition to 1. The sequence is B→D→E→self-test step.
MSR[NSTART] transitions to 1 when the normal conversion starts and transitions to 0 at the end of conversion for the test channel.
In Scan operation mode, consecutive steps of the selected self-test algorithm are converted continuously at the end of each chain 
of normal conversions. The number of channels converted at the end of each chain is 1 (except for algorithm S, in which all the 
steps are performed sequentially without any functional conversion interleaved). So, in Scan operation mode the sequence is:
1. Program NCMRn to select the channels to be converted for normal conversion.
2. Write 1 to MCR[MODE] to select Scan operation mode.
3. Configure the self-test algorithm threshold values (see Table 351).
4. Program sampling duration values in STCR1[INPSAMPm] field (m = S, C).
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2356 / 5251


---
# 페이지 48

5. Select the self-testing algorithm in STCR3[ALG]. By default, all algorithms (supply and capacitive) are selected, that is, 
all algorithms are executed step-by-step, one after the other.
6. Enable self-testing by writing 1 to STCR2[EN].
7. Start the normal conversion by writing 1 to MCR[NSTART].
8. All normal conversions are executed as usual.
9. At the end of the chain of normal conversions (assuming the default value of STCR3[ALG]), all steps of algorithm S are 
performed (as algorithm S is always atomic). MSR[SELF_TEST_S] transitions to 1.
10. At the end of the conversion of the self-test channel for the last step of algorithm S, the result is written to 
STDR1[TCDATA] and STDR1[VALID] transitions to 1. At the same time, MSR[SELF_TEST_S] transitions to 0. The 
following registers also transition to 1:
• ISR[EOC]
• ISR[ECH]
• STSR1[ST_EOC]
11. The next chain of normal conversions then starts.
12. At end of the chain of normal conversions, ADC executes step 0 of algorithm C.
13. At the end of the conversion of the test channel for step 0 of algorithm C, the result is stored in STDR1[TCDATA] 
and STDR1[VALID] transitions to 1 (if STSR1[OVERWR] is 1). Also, ISR[EOC] and ISR[ECH] transition to 1. 
STSR1[ST_EOC] also transitions to 1.
14. The next chain of normal conversion then starts.
15. At the end of the normal conversion chain, ADC executes step1 of algorithm C.
This process continues for all steps of all three algorithms. The state machine returns to Idle state when MCR[NSTART] transitions 
to 0.
For example: channels A→B→C→D→E→F→G→H are present in the device where channels B→D→E are to be converted in Scan 
operation mode. At the end of every conversion chain for channels B→D→E, one step of the self-test conversion is performed and 
ISR[ECH] and ISR[EOC] transition to 1.
The sequence is:
B→D→E→ST-S0→ST-S1→ST-S2→B→D→E→ST-C0→B→D→E→ST-C1→B→D→E→ST-C2→ . . . B→D→E→ST-C11→B→D→E→ST-
S0 . . .
ST-Sx - Self-test supply step x (x = 0, 1, 2)
ST-Cx - Self-test capacitive step x (x = 0 to 11)
MSR[NSTART] transitions to 1 when normal conversion starts.
 
• If instead of starting normal conversion by software (by writing 1 to MCR[NSTART]), it is started by an external 
trigger, the self-test behavior remains the same.
• Self-test channel conversion is not performed for injected conversions. It is performed only during 
normal conversions.
• If, during a test channel conversion, an injected conversion arrives, the test conversion is aborted 
(just as a normal functional channel) and the injected conversion is performed. After the injected 
conversion is complete, the test conversion resumes from the step at which it was aborted. In this case, 
MSR[SELF_TEST_S] remains 1 during the injected conversion.
• For self-test, MCR[MODE] should be programmed (at least one cycle) before writing 1 MCR[NSTART] and 
should not be changed until the conversion is finished or terminated.
  NOTE  
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2357 / 5251


---
# 페이지 49

Table 351. Recommended self-test threshold values
Register field
Hex value
Decimal value
Comment
STAW0R[THRH]
3669h
13929
The threshold values depend 
on the stability of the supply 
and the reference voltage. 
When you see voltage 
variations, widen the limits.
STAW0R[THRL]
5 V reference: 1A7Fh
3 V reference: 2B27h
5 V reference: 6784
3 V reference: 11047
STAW1R[THRL]
3FF9h
16377
STAW2R[THRL]
3FF9h
16377
STAW4R[THRH]
20h
32
STAW4R[THRL]
7FE0h
–32
STAW5R[THRH]
20h
32
STAW5R[THRL]
7FE0h
–32
60.3.17.2.2
BCTU mode
BCTU mode is enabled by writing 1 to MCR[BCTUEN].
Self-test conversion behaves in the same way for all BCTU operating modes (Trigger mode and Control mode). In both cases, if 
MCR[BCTUEN] = 1, the self-test conversion can be started only by BCTU—software cannot start it. MCR[BCTUEN] must not be 
changed during normal conversion. The interface between BCTU and ADC (for self-test) is shown in the following figure.
BCTU
Algorithm
Self-test enable
Step number
Trigger
End of conversion
Conversion data out
ADC
Figure 260. Self-test interface between ADC and BCTU
For self-test conversions in BCTU mode, BCTU asserts self-test enable along with the Trigger command. The algorithm and the 
step number to be executed is put on algorithm and step number, respectively. The other commands (Trigger, End Of Conversion, 
and Conversion Data Out) have the same meaning, like normal BCTU functional conversion.
As already mentioned for algorithm S, the three steps must be atomic. In BCTU mode, this is managed by BCTU, that is, BCTU 
sends three triggers (one for each step) asserting self-test enable and updating test_step for each step.
60.3.17.2.3
Abort and abort chain for self-testing channel
Writing 1 to MCR[ABORT] during self-test channel conversion has no effect.
In One-Shot operation mode, if you write 1 to MCR[ABORTCHAIN] during the self-test channel conversion, the self-test channel 
is aborted and ISR[ECH] transitions to 1. In this case, ISR[EOC] for the self-test channel is not generated.
In Scan operation mode, if MCR[ABORTCHAIN] = 1 when self-test channel step n is ongoing, self-test channel step n is aborted 
and the next chain conversion begins. At the end of the chain, the step n conversion is performed again. (For algorithm S, the full 
algorithm is executed again).
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2358 / 5251


---
# 페이지 50

60.3.17.2.4
Self-test analog watchdog
ADC provides monitoring options for conversion data generated by self-test algorithms. Analog watchdogs determine whether 
the conversion results for self-test algorithms are in the range of a particular guard area. ADC provides separate self-test analog 
watchdog registers for each algorithm.
After the conversion of each step of a self-test algorithm, ADC compares the converted value and the threshold values if the 
analog watchdog feature has been enabled by writing 1 to STAWnR[AWDE] (for example, STAW0R[AWDE]). If the converted 
value is not between the upper and lower threshold values specified by the Self-Test Analog Watchdog Register for the particular 
algorithm, the corresponding error flag, STSR1[ERR_x], transitions to 1 and the step number in which error occurred is captured in 
STSR1[STEP_x] (for algorithm C). Erroneous data is written to STSR4[DATAn]. The STSR1[ERR_x] flags generate an interrupt 
if enabled by the corresponding mask bit in Self-Test Configuration 2 (STCR2). The fault indication is also forwarded to the fault 
control unit, if present, so that necessary action can be taken at the chip level. The fault type (critical or noncritical) is specified by 
the configuration in Self-Test Configuration 2 (STCR2).
The analog watchdog feature works differently for algorithm S. Algorithm S is always an atomic operation. Self-Test Status 1 
(STSR1) has a separate error field for each step of algorithm S to avoid overwrite in case an error occurs in more than one step. 
Therefore, there are separate mask bits for each step in STCR1. For the same reason, the status registers (Self-Test Status 2 
(STSR2) and Self-Test Status 3 (STSR3)) have separate fields for each step to store erroneous data.
In step 0 of the supply algorithm, ADC measures the band gap voltage (1.2 V), which is assumed to be stable. The conversion 
result of step 0 is compared against high (THRH) and low (THRL) thresholds as defined in Self-Test Analog Watchdog S0 
(STAW0R), if enabled (STAW0R[AWDE] = 1). The STSR1[ERR_S0] flag transitions to 1 if any of the thresholds are violated. 
STSR1[ERR_S0] is cleared by writing 1 to it. The conversion result of ADC can be calculated with the following formula:
• ADC data (decimal) = ( Vin × 215 ÷ (Vrh - Vrl))
Where:
• Vin: input voltage (band gap voltage in this case)
• Vrh: ADC reference high voltage
• Vrl: ADC reference low voltage
The upper and lower threshold value can be calculated with the above formula using maximum and minimum values of Vin, Vrh, 
Vrl (Vin is the band gap supply voltage in this case):
• Upper threshold (THRH, decimal) = (Vin[max] × 215) ÷ (Vrh[min] - Vrl[max])
• Lower threshold (THRL, decimal) = (Vin[min] × 215) ÷ (Vrh[max] - Vrl[min])
The minimum and maximum voltages can be obtained from the chip data sheet. The band gap voltage tolerance, as well as the 
actual reference voltage used and its tolerances, must be considered when calculating high and low thresholds.
For algorithm S steps 1 and 2, (VREF/VREF) is measured in order to check the integrity of the sampling signal. For these particular 
conversions, no higher threshold value is required as the ideal value is FFFh. Only the lower threshold value is programmed in 
Self-Test Analog Watchdog S1 (STAW1R) and Self-Test Analog Watchdog S2 (STAW2R).
For algorithm C, a separate register is provided for step 0. In step 0 an offset for other steps is measured. The converted data 
is compared with the threshold values in Self-Test Analog Watchdog C (STAW5R) if STAW4R[AWDE] = 1. For other steps, this 
offset is subtracted from converted data before performing watchdog checks.
60.3.17.2.5
Watchdog timer
The watchdog timer is an additional check that monitors the sequence of the self-testing algorithm that has been implemented, 
and also checks whether the algorithm is completed within a safe time period. The watchdog timers are enabled for CPU as well as 
BCTU conversions. Each algorithm has an independent watchdog timer. The watchdog timer for a particular algorithm is enabled 
by writing 1 to STAWxR[WDTE]. The safe time value is programmed in STBRR[WDT] (the default value is 10 ms, assuming an 
80 MHz clock).
The safe time is measured starting from step 0 of the algorithm (including all normal chain conversions in between) to the point 
where step 0 of the same algorithm starts again.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2359 / 5251


---
# 페이지 51

The programming sequence is:
1. Program NCMRn to select the channels for normal conversion in Scan operation mode (MCR[MODE] = 1).
2. Select the self-test algorithm in STCR3[ALG]. By default, all algorithms (supply and capacitive) are selected (all 
algorithms are executed step-by-step, one after the other).
3. Enable the self-test channel by writing 1 to STCR2[EN].
4. Program the safe period value in STBRR[WDT].
5. Enable the watchdog timer by writing 1 to STAWxR[WDTE]. Assume writing 1 to STAWxR[WDTE] occurs at time t0. It is 
important to do all configuration programming before writing 1 to STAWxR[WDTE], because the safe time check is also 
performed between writing 1 to STAWxR[WDTE] and the start of step 0. This is to verify that the algorithm has started 
within the safe time.
6. Start the normal conversion by writing 1 to MCR[NSTART].
7. At the end of the first conversion chain, three steps (steps 0, 1, and 2) of algorithm S are executed in sequence. 
Assume the start of Step 0 occurs at time t1.
8. After completion of algorithm S, ADC performs conversion of the next chain.
9. At the end of the conversion chain, the first step (step 0) of algorithm C is performed.
10. In this way, one step of algorithm C is performed after completion of one conversion chain until all steps are finished. 
Steps are executed in sequence (steps 0–11)
11. After the last step of algorithm C, another chain conversion is executed. At the end of this chain conversion, step 
0 of algorithm S is started again, repeating the whole sequence. Assume this time (starting of step 0 of the supply 
algorithm) to be at time t2.
12. For algorithm S, if (t1 - t0) > safe period or (t2 - t1) > safe period, the watchdog timer flags an error and 
STSR1[WDTERR] transitions to 1. ADC asserts a fault signal per the criticality configuration (critical or noncritical) 
and an interrupt is generated, if enabled (STCR2[MSKWDTERR] = 1). Otherwise, the watchdog timer counter is reset 
and starts again to monitor the next sequence.
13. A similar sequence is followed for watchdog timers for algorithm C.
Normal
conversion
Alg-S step 0
Alg-S step 1
Alg-S step 2
Alg-S step 0
t2
Normal
conversion
t1
Writing 1
to WDTE
(t0)
Figure 261. Watchdog timer monitor for algorithm S
 
1. Because BCTU may not incorporate any safe period checking mechanism, the watchdog timers can also 
be enabled for BCTU conversions.
2. You must disable watchdog timers for self-test algorithms that are not executed.
  NOTE  
60.3.17.2.5.1
Watchdog sequence checking
The self-test watchdog timer incorporates sequence checking features to verify that the steps of each algorithm are executed in 
the correct order. If the steps are not in the correct order, STSR1[WDSERR] transitions to 1 to indicate the error. A fault is indicated 
by an interrupt flag if STCR2[MSKWDSERR] = 1. A fault is also asserted as per criticality configuration (critical or noncritical) and 
an interrupt generated if STCR2[MSKWDSERR] = 1.
A watchdog sequence error is flagged in the following cases:
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2360 / 5251


---
# 페이지 52

• The steps of any algorithm are not executed in proper order.
• The step numbers provided by BCTU for a BCTU conversion are not in order. Watchdog sequence checking is significant 
only for BCTU burst mode.
• When an abort chain occurs during a self-test channel conversion, that step must be repeated at the end of the next chain. 
This generates a sequence error as soon as the self-test channel conversion resumes. There is an exception, however. If 
an abort chain occurs during the last step of algorithm S, the sequence error is not flagged because the whole algorithm 
must be repeated.
If an injected conversion occurs during self-test channel conversion, a watchdog sequence error is not flagged, although the 
ongoing step number is aborted and is repeated.
 
The watchdog timer feature is applicable for Scan operation mode but not for One-Shot operation mode.
  NOTE  
60.3.17.2.6
Baud rate control for test channel
The baud rate control feature controls the scheduling of self-test channel conversions between normal conversion chains. The 
scheduling rate is specified by STBRR[BR].
By default, if the self-test channel is enabled, one step of the selected algorithm is executed after each normal conversion chain. 
The bandwidth consumed by the self-test channel depends on the number of channels in the normal chain. For example, if you 
have 50 normal conversions in a chain, then the self-test channel consumes only 2% of the total bandwidth, which is very small. If 
the number decreases to just 3 channels, the bandwidth consumed by the self-test channel is 25%, which is significant (and may 
not be desirable because it slows down the normal conversion rate).
STBRR[BR] provides flexibility by scheduling the self-test channel conversion to be performed not at the end of every chain, 
but at the end of BR + 1 chains. For example, if STBRR[BR]  = 5, a single step of the selected algorithm for the test channel is 
performed after 6 chain conversions. The next step is performed at the end of the next six chain conversions, and so on. By default, 
STBRR[BR] = 0.
 
This feature is applicable only for Scan operation mode and not for One-Shot operation mode. STBRR[BR] should 
be written with 0 for One-Shot operation mode.
To use the baud rate control feature in Scan operation mode, NCMRn should have a nonzero value.
  NOTE  
60.3.17.2.6.1
Abort chain when baud rate is nonzero
As already described, for a nonzero value of STBRR[BR], the self-test channel conversion is performed at the end of BR + 1 
chains. If an abort chain occurs during the chain in which a self-test channel conversion is scheduled to be performed, the self-test 
channel conversion is performed after the next BR + 1 chains.
For example, if STBRR[BR] = 2, the sequence is two normal chains (without any self-test channel conversion), followed by a chain 
with the self-test channel converted at the end. If an abort chain occurs during the first two chains, it is treated as a normal chain 
abort and the self-test channel is converted at the end of the third chain only (as in the case without any abort chain). However, 
if an abort chain occurs during the third chain in which the self-test channel is scheduled to be converted, the self-test channel is 
converted after the next three chains (for example, at the end of the sixth chain, counting from the beginning).
60.3.18 Conversion time
Total conversion time depends on the conversion clock frequency, which is configured by programming MCR[ADCLKSEL].
The components of conversion time and affecting configurations are:
• PST
• ST
• CT
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2361 / 5251


---
# 페이지 53

• DP
• TPT
Presample phase time is equal to the sample time with a one AD_clk cycle delay for phase transition from presample phase to 
sample phase. CTRn[INPSAMP] controls sample time for different types of channels and is specified in terms of AD_clk cycles, 
so the presampling time is sample time plus one cycle of AD_clk. The minimum value of sample time is 8. If the value programmed 
is less than 8, it has no effect on sample time and the sample time is 8 AD_clk cycles.
Compare phase time is controlled by:
• The evaluation time of a single bit
• The number of bits converted
For n-bit conversions, the value of CT is n multiplied by the evaluation time of a single bit in terms of AD_clk cycles.
The evaluation time of a single bit is 4 AD_clk cycles if AMSIO[HSEN] = 0h and AMSIO[CMPCTRL0] = 0b. The evaluation time 
of a single bit is 6 AD_clk cycles if AMSIO[HSEN] = 1h and AMSIO[CMPCTRL0] = 1b.
The data processing time is 2 cycles of AD_clk. During these cycles raw converted data is corrected for offset, gain, capacitor 
mismatch, and so on.
Trigger processing time consists of:
• One module_clock cycle, which is required to prepare the channel and calculate the initial gain value used by ADC for the 
first conversion.
• BCTU triggering time:
— Triggers from the synchronous BCTU interface require 1 cycle of the module clock for processing. One more cycle is 
required to register the BCTU trigger in synchronous mode.
The total conversion time, in terms of the module clock cycles, is calculated using the following equation for normal and 
injected conversions:
Total_conversion_time = ( [(PST + ST + CT + DP) × chain_length] + TPT) × TAD_clk
Example:
The ADC controller clock is equal to the module clock (80 MHz, clock cycle = 12.5 ns)
• ADC resolution 12 bit + 1 bit for a special capacitor (CS)
• Three channels are programmed in NCMRn, so a chain of three is to be converted
• Default sample time (22 cycles) is specified
• No presampling
• Conversion time (4 cycles per bit)
The total time for the three conversions = [(0 + 22 + (4×13) + 2) × 3] + 1 = 229 cycles ~= 2.862 µs
Conversion timing in Calibration for full test:
• Single conversion time = [sample time (CALBISTREG[TSAMP]) + compare time (11 × 4) + data proc(2)]
• Inter-conversion gap = 1 cycle
• Total number of tests = 12
• Averaging = 32
One test duration = (single conversion time + inter-conversion gap) × averaging samples
Total test duration = ( ( one test duration ) × total number of tests).
Example: sample time = 22
Total test time = ( ( ( (22 + (11×4) +2)+1) × 32) × 12) = 26496 cycles × 12.5 ns (80 MHz) = 331200 ns
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2362 / 5251


---
# 페이지 54

Conversion time in self-test:
Self-test conversion time equals one test period multiplied by the number of consecutive (atomic) steps. For supply self-test, the 
atomic step is 3 and for other tests it is 1.
One test period for self-test is as below.
• For supply tests: ( [ sample_time + (13 × 4) + 2] )
• For other algorithms: ( [ sample_time + (11 × 4) + 2] )
 
Algorithm S steps (conversions) always run in atomic operation, required for an algorithmic procedure. In Scan 
operation mode, when all algorithms are selected, three steps of algorithm S run together after the end of the 
conversion chain. algorithm C steps are not required to be run together, so after each conversion chain one step 
is executed serially. Conversion time with self-test must also be calculated accordingly.
  NOTE  
Example.
• Channels in chain A→B→C.
• Scan operation mode.
• All self-test algorithms are selected.
So, the resulting conversion order is:
[A→B→C→AS_step0→AS_step1→AS_step2→A→B→C→AC_step0→A→B→C→AC_step1→A→B→C→AC_step2→.....→A→B→C→AC_s
tep11]→[same sequence repeats]
 
• AS = Algorithm S (supply self-test)
• AC = Algorithm C (capacitive self-test)
  NOTE  
60.3.19 Conversion data processing
Raw converted data contains many types of errors, such as offset, gain, and so on. ADC processes raw conversion data before 
writing the result to a data register, to reduce or eliminate error contributions. The process of error correction happens in parallel 
with bit-by-bit evaluation, using the correction values generated during the offset determination and calibration process.
The error correction value is subtracted from the raw conversion result whenever the comparator output for one of the calibrated 
capacitors evaluates high during the conversion period.
To reduce data processing time, error correction is done in parallel during each bit evaluation of a conversion. Lower-weighted 
capacitors (smaller than C9) are not calibrated, so no error correction is performed for these capacitors. However, they are 
self-tested to guarantee that the error contribution is below specified accuracy limits.
The final result is checked for any overflow or underflow. When the processed data is above the maximum value that can be 
represented by ADC resolution, the output data is forced to all 1s (FFFh for 12-bit resolution). Similarly, if the processed data is 
negative then output data is forced to all 0s (000h for 12-bit resolution).
60.3.20 User-defined offset and gain values
In addition to the ADC-calculated offset value and gain value, ADC enables you to specify another set of offset and gain values in 
Offset And Gain User (OFSGNUSR). These values must be stored in two's complement format, where the leftmost bit (the most 
significant bit) is the sign bit.
ADC subtracts these values from the final processed conversion result. The values are used to removed fixed DC bias or any other 
known errors—for instance those caused by board design, sensors, and so on.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2363 / 5251


---
# 페이지 55

60.4 External signals
This module has no external signals.
60.5 Clock frequency
ADC's internal blocks are designed for an input clock frequency up to the Fin (Input Signal Bandwidth) maximum (see the ADC 
electrical specification section in the chip data sheet). The specified speed can be achieved with this clock frequency. If the 
input clock frequency exceeds the specified maximum frequency, ADC accuracy degrades and, in the worst case scenario, ADC 
malfunctions. ADC accuracy also degrades if the input clock frequency is below the specified minimum frequency. Sampling time 
has an absolute maximum value to guarantee the specified parameters and accuracy. For slower clocks, the sampling clock count 
must be programmed accordingly.
60.6 Memory map and register definition
ADC has a wide range of configurations to tailor its operation to application requirements. This comes with the drawback of 
possible corner cases. To avoid unintended behavior, configure ADC before starting a conversion and change any configuration 
only when ADC is idle, in other words when MSR[ADCSTATUS] = 0.
60.6.1 Transfer error description
The following register accesses cause a transfer error and do not change register content:
• Any access to an unused address.
• Any write access to a read-only register.
60.6.2 ADC register descriptions
60.6.2.1
ADC memory map
ADC_0 base address: 400A_0000h
ADC_1 base address: 400A_4000h
ADC_2 base address: 400A_8000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Main Configuration (MCR)
32
RW
0000_0001h
4h
Main Status (MSR)
32
R
0000_0001h
10h
Interrupt Status (ISR)
32
RW
0000_0000h
14h
Channel End Of Conversion Flag For Precision Inputs (CEOCFR0)
32
RW
0000_0000h
18h
Channel End Of Conversion Flag For Standard Inputs (CEOCFR1)
32
RW
0000_0000h
1Ch
Channel End Of Conversion Flag For External Inputs (CEOCFR2)
32
RW
0000_0000h
20h
Interrupt Mask (IMR)
32
RW
0000_0000h
24h
EOC Interrupt Enable For Precision Inputs (CIMR0)
32
RW
0000_0000h
28h
EOC Interrupt Enable For Standard Inputs (CIMR1)
32
RW
0000_0000h
2Ch
EOC Interrupt Enable For External Inputs (CIMR2)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2364 / 5251


---
# 페이지 56

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
30h
Analog Watchdog Threshold Interrupt Status (WTISR)
32
RW
0000_0000h
34h
Analog Watchdog Threshold Interrupt Enable (WTIMR)
32
RW
0000_0000h
40h
Direct Memory Access Configuration (DMAE)
32
RW
0000_0000h
44h
DMA Request Enable For Precision Inputs (DMAR0)
32
RW
0000_0000h
48h
DMA Request Enable For Standard Inputs (DMAR1)
32
RW
0000_0000h
4Ch
DMA Request Enable For External Inputs (DMAR2)
32
RW
0000_0000h
60h - 6Ch
Analog Watchdog Threshold Values (THRHLR0 - THRHLR3)
32
RW
7FFF_0000h
80h
Presampling Control (PSCR)
32
RW
0000_0000h
84h
Presampling Enable For Precision Inputs (PSR0)
32
RW
0000_0000h
88h
Presampling Enable For Standard Inputs (PSR1)
32
RW
0000_0000h
8Ch
Presampling Enable For External Inputs (PSR2)
32
RW
0000_0000h
94h
Conversion Timing For Precision Inputs (CTR0)
32
RW
0000_0016h
98h
Conversion Timing For Standard Inputs (CTR1)
32
RW
0000_0016h
9Ch
Conversion Timing For External Inputs (CTR2)
32
RW
0000_0016h
A4h
Normal Conversion Enable For Precision Inputs (NCMR0)
32
RW
0000_0000h
A8h
Normal Conversion Enable For Standard Inputs (NCMR1)
32
RW
0000_0000h
ACh
Normal Conversion Enable For External Inputs (NCMR2)
32
RW
0000_0000h
B4h
Injected Conversion Enable For Precision Inputs (JCMR0)
32
RW
0000_0000h
B8h
Injected Conversion Enable For Standard Inputs (JCMR1)
32
RW
0000_0000h
BCh
Injected Conversion Enable For External Inputs (JCMR2)
32
RW
0000_0000h
C4h
Delay Start Of Data Conversion (DSDR)
32
RW
0000_0000h
C8h
Power Down Exit Delay (PDEDR)
32
RW
0000_0000h
100h - 11Ch
Precision Input n Conversion Data (PCDR0 - PCDR7)
32
R
0000_0000h
180h - 1DCh
Standard Input n Conversion Data (ICDR0 - ICDR23)
32
R
0000_0000h
200h - 27Ch
External Input n Conversion Data (ECDR0 - ECDR31)
32
R
0000_0000h
2B0h
Channel Analog Watchdog Select For Precision Inputs 
(CWSELRPI0)
32
RW
0000_0000h
2B4h
Channel Analog Watchdog Select For Precision Inputs 
(CWSELRPI1)
32
R
0000_0000h
2C0h
Channel Analog Watchdog Select For Standard Inputs 
(CWSELRSI0)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2365 / 5251


---
# 페이지 57

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
2C4h
Channel Analog Watchdog Select For Standard Inputs 
(CWSELRSI1)
32
RW
0000_0000h
2C8h
Channel Analog Watchdog Select For Standard Inputs 
(CWSELRSI2)
32
RW
0000_0000h
2D0h
Channel Analog Watchdog Select For External inputs (CWSELREI0)
32
RW
0000_0000h
2D4h
Channel Analog Watchdog Select For External inputs (CWSELREI1)
32
RW
0000_0000h
2D8h
Channel Analog Watchdog Select For External inputs (CWSELREI2)
32
RW
0000_0000h
2DCh
Channel Analog Watchdog Select For External inputs (CWSELREI3)
32
RW
0000_0000h
2E0h
Channel Watchdog Enable For Precision Inputs (CWENR0)
32
RW
0000_0000h
2E4h
Channel Watchdog Enable For Standard Inputs (CWENR1)
32
RW
0000_0000h
2E8h
Channel Watchdog Enable For External Inputs (CWENR2)
32
RW
0000_0000h
2F0h
Analog Watchdog Out Of Range For Precision Inputs (AWORR0)
32
RW
0000_0000h
2F4h
Analog Watchdog Out Of Range For Standard Inputs (AWORR1)
32
RW
0000_0000h
2F8h
Analog Watchdog Out Of Range For External Inputs (AWORR2)
32
RW
0000_0000h
340h
Self-Test Configuration 1 (STCR1)
32
RW
1818_2507h
344h
Self-Test Configuration 2 (STCR2)
32
RW
0000_0005h
348h
Self-Test Configuration 3 (STCR3)
32
RW
0000_0300h
34Ch
Self-Test Baud Rate (STBRR)
32
RW
0005_0000h
350h
Self-Test Status 1 (STSR1)
32
RW
0000_0000h
354h
Self-Test Status 2 (STSR2)
32
R
0000_0000h
358h
Self-Test Status 3 (STSR3)
32
R
0000_0000h
35Ch
Self-Test Status 4 (STSR4)
32
R
0000_0000h
370h
Self-Test Conversion Data 1 (STDR1)
32
R
0000_0000h
380h
Self-Test Analog Watchdog S0 (STAW0R)
32
RW
0727_04C5h
388h
Self-Test Analog Watchdog S1 (STAW1R)
32
RW
0000_3FF9h
38Ch
Self-Test Analog Watchdog S2 (STAW2R)
32
RW
0000_3FF9h
394h
Self-Test Analog Watchdog C0 (STAW4R)
32
RW
0010_3FF0h
398h
Self-Test Analog Watchdog C (STAW5R)
32
RW
0010_3FF0h
39Ch
Analog Miscellaneous In/Out register (AMSIO)
32
RW
0000_0811h
3A0h
Control And Calibration Status (CALBISTREG)
32
RW
See section
3A8h
Offset And Gain User (OFSGNUSR)
32
RW
0004_0000h
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2366 / 5251


---
# 페이지 58

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
3B4h
Calibration Value 2 (CAL2)
32
RW
4300_8243h
60.6.2.2
Main Configuration (MCR)
Offset
Register
Offset
MCR
0h
Function
Configures most ADC features. You must change field values only when ADC is in Idle state, except for the ABORTCHAIN 
and ABORT fields.
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
OWRE
N 
WLSID
E 
MODE 
0
TRGE
N 
EDGE 
XSTR
TEN 
NSTA
RT 
0
JTRG
EN 
JEDG
E 
JSTAR
T 
0
BCTU
EN 
BCTU
_MO...
W
Reset
0
0
0
0
0
0
0
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
AVGE
N 
AVGS 
Reserv
ed 
ABOR
TCH...
ABOR
T 
ACKO 
0
ADCLKSEL 
PWDN 
W
STCL 
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
OWREN
Overwrite Enable
Specifies whether a conversion data register accepts new data before the current conversion data has 
been read. When enabled, the new conversion result overwrites the older data, regardless of the validity 
of the older conversion data. When PCDRn[VALID] = 1, the conversion data has not been read.
0b - Disable
1b - Enable
30
WLSIDE
Write Left-Aligned
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2367 / 5251


---
# 페이지 59

Table continued from the previous page...
Field
Function
Specifies whether conversion data is right-aligned or left-aligned when written to one of the conversion 
data registers:
• PCDRn
• ICDR0n
• ECDRn
Right-aligned data occupies *CDR[14:0]. Left-aligned data occupies *CDR[15:1],
0b - Right aligned
1b - Left-aligned
29
MODE
Normal Conversion Mode
Specifies whether the set of input channels selected for a normal conversion are converted only once per 
start event or continuously after a start event.
If a conversion is done only once, ADC enters an idle state after conversion is complete.
For continuous conversion, all input channels selected for the normal conversion are converted 
continuously in a loop. Stop the loop by writing 0 to NSTART.
0b - Single conversion
1b - Continuous conversion
28
—
Reserved
27
TRGEN
External Trigger Enable
Specifies whether the normal trigger input starts a conversion.
0b - Normal trigger input does not start a conversion
1b - Normal trigger input starts a conversion
26
EDGE
External Trigger Edge Selection
Selects which edge of the normal trigger input starts a conversion.
0b - Falling edge
1b - Rising edge
25
XSTRTEN
Auxiliary External Start Enable
Enables the auxiliary normal trigger source to start a conversion. You can use this field to synchronize 
the start of a conversion of two ADC instances.
0b - Disable
1b - Enable
24
NSTART
Start Normal Conversion
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2368 / 5251


---
# 페이지 60

Table continued from the previous page...
Field
Function
Starts a normal conversion. If the continuous mode is selected (MODE = 1), the value of this field 
remains 1. Write 0 to this field to stop the in-progress conversion loop after conversion of the last input 
channel of the selected set of input channels is complete.
If continuous mode is not selected (MODE = 0), this field automatically resets to 0 after writing 1.
0b - No effect
1b - Starts conversion
23
—
Reserved
22
JTRGEN
Injection Trigger Enable
Enables the injected trigger input as a source to start a conversion.
0b - Disable
1b - Enable
21
JEDGE
Injected Trigger Edge Selection
Selects which edge of the injected trigger input starts an injected conversion.
0b - Falling edge
1b - Rising edge
20
JSTART
Injected Start
Interrupts any ongoing normal conversion and starts an injected conversion. This field automatically 
resets to 0. If an injected conversion is already ongoing, the field value remains 1 until the next injected 
conversion starts. This field can only be written with 1.
0b - Injected conversion can be started
1b - Starts an injected conversion
19-18
—
Reserved
17
BCTUEN
Body Cross Trigger Unit Enable
Enables BCTU as a trigger source.
0b - Disable
1b - Enable
16
BCTU_MODE
Body Cross Trigger Unit Mode Select
Specifies whether sources other than BCTU can start a conversion when the BCTU is enabled as a 
trigger source (BCTUEN = 1). This field is writeable only when ADC is in Power Down state (PWDN = 1).
0b - Only BCTU can trigger conversion
1b - All trigger sources can trigger conversion
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2369 / 5251


---
# 페이지 61

Table continued from the previous page...
Field
Function
15
STCL
Self-Test Configuration Lock
Protects the following registers from writing:
• STCR1
• STCR2
• STCR3
• STBRR
• STAW0R
• STAW1R
• STAW2R
• STAW4R
• STAW5R
0b - Registers are writeable
1b - Registers are read-only
14-12
—
Reserved
11
AVGEN
Averaging Enable
Enables conversion averaging.
0b - Disable
1b - Enable
10-9
AVGS
Averaging Select
Specifies the number of conversions ADC uses to calculate the conversion result.
00b - 4 conversions
01b - 8 conversions
10b - 16 conversions
11b - 32 conversions
8
—
Reserved
7
ABORTCHAIN
Abort Chain
Aborts the conversion of the selected set of input channels (chain of input channels). The currently 
ongoing conversion completes.
This field always reads 0.
This field cannot be programmed during BCTU conversion.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2370 / 5251


---
# 페이지 62

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Undefined
When writing
0b - Conversion continues
1b - Conversion aborted
6
ABORT
Abort Conversion
Aborts an ongoing conversion. This field always reads 0 and cannot be written during BCTU conversion.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Undefined
When writing
0b - Conversion continues
1b - Conversion aborted
5
ACKO
Auto Clock Off
Reduces power consumption by turning off the clock of the analog part of ADC when it is in Idle state.
0b - Clock always active
1b - Clock gated
4-3
—
Reserved
2-1
ADCLKSEL
Conversion Clock (AD_clk) Frequency Selection
Selects the frequency for the clock signal of the conversion circuit (AD_clk = module 
clock ÷ (2ADCLKSEL)). This field can be written only when ADC is in Power Down state (PWDN = 1).
00b - Module clock frequency
01b - Module clock frequency ÷ 2
10b - Module clock frequency ÷ 4
11b - Module clock frequency ÷ 8
0
PWDN
Power Down
Reduces power consumption by turning off power to the analog portion of ADC.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2371 / 5251


---
# 페이지 63

Table continued from the previous page...
Field
Function
0b - ADC enters a functional state
1b - ADC enters Power Down state
60.6.2.3
Main Status (MSR)
Offset
Register
Offset
MSR
4h
Function
Contains flags that indicate the current ADC state.
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
CALIB
RTD 
0
NSTA
RT 
JABO
RT 
0
JSTAR
T 
0
SELF_
TE...
Reserv
ed 
BCTU
STA...
W
Reset
0
0
0
0
0
0
0
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
CHADDR 
0
ACKO 
0
ADCSTATUS 
W
Reset
0
0
0
0
0
0
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
CALIBRTD
Calibration Status
Indicates ADC calibration status.
0b - Uncalibrated or calibration unsuccessful
1b - Calibrated
30-25
—
Reserved
24
NSTART
Normal Conversion Started
Shows whether a normal conversion is in progress.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2372 / 5251


---
# 페이지 64

Table continued from the previous page...
Field
Function
0b - Not in progress
1b - In progress
23
JABORT
Injected Conversion Aborted
Indicates whether the conversion of a set of inputs selected for injected conversion has been aborted. 
This field resets to 0 when a new injected conversion is started.
0b - Not aborted
1b - Aborted
22-21
—
Reserved
20
JSTART
Injected Conversion Started
Indicates whether an ongoing conversion was started by the injection trigger.
0b - Not an injected conversion
1b - Injected conversion
19
—
Reserved
18
SELF_TEST_S
Indicates whether an ongoing conversion is for self-test.
0b - Not self-test
1b - Self-test
17
—
Reserved
16
BCTUSTART
BCTU Conversion Started
Indicates whether a BCTU conversion is ongoing. This field is 1 when a BCTU trigger event is received 
and the BCTU conversion starts. When the BCTU trigger mode is selected, this field is automatically 
reset to 0 when conversion is completed. Otherwise, if BCTU control mode is selected, this field resets to 
0 when the BCTU is disabled (BCTUEN = 0).
0b - Conversion was not triggered by BCTU
1b - Ongoing conversion was triggered by BCTU
15-9
CHADDR
Input Under Measure
Contains the number of the input that is currently converted.
000_0000b-011_1111b - Input number
8-6
—
Reserved
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2373 / 5251


---
# 페이지 65

Table continued from the previous page...
Field
Function
5
ACKO
Auto Clock-Off On
Indicates whether the auto clock-off feature is active, and the conversion circuit is not receiving a clock 
signal.
When auto clock-off is inactive, the conversion circuit is clocked.
0b - Inactive
1b - Active
4-3
—
Reserved
2-0
ADCSTATUS
ADC State
Indicates the current state of the ADC Finite State Machine (FSM).
000b - Idle
001b - Power Down
010b - Wait
011b - Calibrate
100b - Convert
110b - Done
60.6.2.4
Interrupt Status (ISR)
Offset
Register
Offset
ISR
10h
Function
Contains flags that indicate whether an interrupt has been generated.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2374 / 5251


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
W
Reset
0
0
0
0
0
0
0
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
EOBC
TU 
JEOC 
JECH 
EOC 
ECH 
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
Fields
Field
Function
31-5
—
Reserved
4
EOBCTU
End Of BCTU Conversion
Indicates the status of the End of BCTU Conversion (EOBCTU) interrupt, which is generated after a 
BCTU conversion completes.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No EOBCTU interrupt generated
1b - EOBCTU interrupt generated
When writing
0b - No effect
1b - Clears flag
3
JEOC
End Of Injected Conversion
Indicates the status of the End of Injected Conversion (JEOC) interrupt, which is generated after an 
injected conversion completes.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No JEOC interrupt generated
1b - JEOC interrupt generated
When writing
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2375 / 5251


---
# 페이지 67

Table continued from the previous page...
Field
Function
0b - No effect
1b - Clears flag
2
JECH
End Of Injected Chain Conversion
Indicates the status of the End of Injected Chain (JECH) interrupt, which is generated after injected 
conversion of a set of inputs completes.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No JECH interrupt generated
1b - JECH interrupt generated
When writing
0b - No effect
1b - Clears flag
1
EOC
End Of Conversion
Indicates the status of the End of Conversion (EOC) interrupt, which is generated after a normal 
conversion completes.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No EOC interrupt generated
1b - Interrupt generated
When writing
0b - No effect
1b - Clears flag
0
ECH
End Of Chain Conversion
Indicates the status of the End of Chain (ECH) conversion interrupt, which is generated after a set of 
inputs has been converted normally.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Indicates no ECH interrupt generated
1b - Indicates an ECH interrupt has been generated
When writing
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2376 / 5251


---
# 페이지 68

Table continued from the previous page...
Field
Function
0b - No effect
1b - Clears flag
60.6.2.5
Channel End Of Conversion Flag For Precision Inputs (CEOCFR0)
Offset
Register
Offset
CEOCFR0
14h
Function
Contains flags that indicate whether conversion is complete for a precision input.
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
Reserv
ed 
Reserv
ed 
PIEOC
F7 
PIEOC
F6 
PIEOC
F5 
PIEOC
F4 
PIEOC
F3 
PIEOC
F2 
PIEOC
F1 
PIEOC
F0 
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
31-10
—
Reserved
9
—
Reserved
8
—
Reserved
7
Precision Input End Of Conversion Flag 7
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2377 / 5251


---
# 페이지 69

Table continued from the previous page...
Field
Function
PIEOCF7
Indicates whether conversion of a precision input 7 has completed.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion not complete
1b - Conversion complete
When writing
0b - No effect
1b - Clears flag
6
PIEOCF6
Precision Input End Of Conversion Flag 6
Indicates whether conversion of a precision input 6 has completed.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion not complete
1b - Conversion complete
When writing
0b - No effect
1b - Clears flag
5
PIEOCF5
Precision Input End Of Conversion Flag 5
Indicates whether conversion of a precision input 5 has completed.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion not complete
1b - Conversion complete
When writing
0b - No effect
1b - Clears flag
4
PIEOCF4
Precision Input End Of Conversion Flag 4
Indicates whether conversion of a precision input 4 has completed.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2378 / 5251


---
# 페이지 70

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion not complete
1b - Conversion complete
When writing
0b - No effect
1b - Clears flag
3
PIEOCF3
Precision Input End Of Conversion Flag 3
Indicates whether conversion of a precision input 3 has completed.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion not complete
1b - Conversion complete
When writing
0b - No effect
1b - Clears flag
2
PIEOCF2
Precision Input End Of Conversion Flag 2
Indicates whether conversion of a precision input 2 has completed.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion not complete
1b - Conversion complete
When writing
0b - No effect
1b - Clears flag
1
PIEOCF1
Precision Input End Of Conversion Flag 1
Indicates whether conversion of a precision input 1 has completed.
 
This field behaves differently for register reads and writes.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2379 / 5251


---
# 페이지 71

Table continued from the previous page...
Field
Function
When reading
0b - Conversion not complete
1b - Conversion complete
When writing
0b - No effect
1b - Clears flag
0
PIEOCF0
Precision Input End Of Conversion Flag 0
Indicates whether conversion of a precision input 0 has completed.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion not complete
1b - Conversion complete
When writing
0b - No effect
1b - Clears flag
60.6.2.6
Channel End Of Conversion Flag For Standard Inputs (CEOCFR1)
Offset
Register
Offset
CEOCFR1
18h
Function
Contains flags that indicate whether conversion is complete for a standard input.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2380 / 5251


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
Reserved 
SIEOC
F23 
SIEOC
F22 
SIEOC
F21 
SIEOC
F20 
SIEOC
F19 
SIEOC
F18 
SIEOC
F17 
SIEOC
F16 
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
SIEOC
F15 
SIEOC
F14 
SIEOC
F13 
SIEOC
F12 
SIEOC
F11 
SIEOC
F10 
SIEOC
F9 
SIEOC
F8 
SIEOC
F7 
SIEOC
F6 
SIEOC
F5 
SIEOC
F4 
SIEOC
F3 
SIEOC
F2 
SIEOC
F1 
SIEOC
F0 
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
31-24
—
Reserved
23-0
SIEOCFn
Standard Input End Of Conversion Flag
Indicates whether conversion on standard input n is complete.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion not complete
1b - Conversion complete
When writing
0b - No effect
1b - Clears flag
60.6.2.7
Channel End Of Conversion Flag For External Inputs (CEOCFR2)
Offset
Register
Offset
CEOCFR2
1Ch
Function
Contains flags that indicate whether conversion is complete for an external input.
 
Each module instance supports a different number of registers.
  NOTE  
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2381 / 5251


---
# 페이지 73

Instance
Register supported
Register not supported
ADC_0
CEOCFR2
—
ADC_1
CEOCFR2
—
ADC_2
—
CEOCFR2
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
EIEOC
F31 
EIEOC
F30 
EIEOC
F29 
EIEOC
F28 
EIEOC
F27 
EIEOC
F26 
EIEOC
F25 
EIEOC
F24 
EIEOC
F23 
EIEOC
F22 
EIEOC
F21 
EIEOC
F20 
EIEOC
F19 
EIEOC
F18 
EIEOC
F17 
EIEOC
F16 
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
EIEOC
F15 
EIEOC
F14 
EIEOC
F13 
EIEOC
F12 
EIEOC
F11 
EIEOC
F10 
EIEOC
F9 
EIEOC
F8 
EIEOC
F7 
EIEOC
F6 
EIEOC
F5 
EIEOC
F4 
EIEOC
F3 
EIEOC
F2 
EIEOC
F1 
EIEOC
F0 
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
31-0
EIEOCFn
External Input End Of Conversion Flag
Indicates whether conversion on external input n is complete.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion not complete
1b - Conversion complete
When writing
0b - No effect
1b - Clears flag
60.6.2.8
Interrupt Mask (IMR)
Offset
Register
Offset
IMR
20h
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2382 / 5251


---
# 페이지 74

Function
Enables flagging of interrupts.
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
MSKE
OBC...
MSKJ
EOC 
MSKJ
ECH 
MSKE
OC 
MSKE
CH 
W
Reset
0
0
0
0
0
0
0
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
MSKEOBCTU
EOBCTU Interrupt Flag Enable
Specifies whether a completed BCTU conversion flags the EOBCTU interrupt.
0b - Interrupt is not flagged
1b - Interrupt is flagged
3
MSKJEOC
JEOC Interrupt Flag Enable
Specifies whether completion of an injected conversion flags the JEOC interrupt.
0b - Interrupt is not flagged
1b - Interrupt is flagged
2
MSKJECH
JECH Interrupt Flag Enable
Specifies whether completion of an injected conversion of a set of inputs flags the JECH interrupt.
0b - Interrupt is not flagged
1b - Interrupt is flagged
1
MSKEOC
EOC Interrupt Flag Enable
Specifies whether completion of a normal conversion flags the EOC interrupt.
0b - Interrupt is not flagged
1b - Interrupt is flagged
0
ECH Interrupt Flag Enable
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2383 / 5251


---
# 페이지 75

Table continued from the previous page...
Field
Function
MSKECH
Specifies whether completion of a normal conversion of a set of inputs flags the ECH interrupt.
0b - Interrupt is not flagged
1b - Interrupt is flagged
60.6.2.9
EOC Interrupt Enable For Precision Inputs (CIMR0)
Offset
Register
Offset
CIMR0
24h
Function
Specifies whether a completed conversion of a precision input flags an EOC interrupt.
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
Reserv
ed 
Reserv
ed 
PIEOC
IE...
PIEOC
IE...
PIEOC
IE...
PIEOC
IE...
PIEOC
IE...
PIEOC
IE...
PIEOC
IE...
PIEOC
IE...
W
Reset
0
0
0
0
0
0
0
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
9
—
Reserved
8
—
Reserved
7
Precision Input EOC Interrupt Enable
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2384 / 5251


---
# 페이지 76

Table continued from the previous page...
Field
Function
PIEOCIEN7
Specifies whether a completed conversion of precision input n flags an EOC interrupt.
0b - Interrupt is not flagged
1b - Interrupt is flagged
6
PIEOCIEN6
Precision Input EOC Interrupt Enable
Specifies whether a completed conversion of precision input n flags an EOC interrupt.
0b - Interrupt is not flagged
1b - Interrupt is flagged
5
PIEOCIEN5
Precision Input EOC Interrupt Enable
Specifies whether a completed conversion of precision input n flags an EOC interrupt.
0b - Interrupt is not flagged
1b - Interrupt is flagged
4
PIEOCIEN4
Precision Input EOC Interrupt Enable
Specifies whether a completed conversion of precision input n flags an EOC interrupt.
0b - Interrupt is not flagged
1b - Interrupt is flagged
3
PIEOCIEN3
Precision Input EOC Interrupt Enable
Specifies whether a completed conversion of precision input n flags an EOC interrupt.
0b - Interrupt is not flagged
1b - Interrupt is flagged
2
PIEOCIEN2
Precision Input EOC Interrupt Enable
Specifies whether a completed conversion of precision input n flags an EOC interrupt.
0b - Interrupt is not flagged
1b - Interrupt is flagged
1
PIEOCIEN1
Precision Input EOC Interrupt Enable
Specifies whether a completed conversion of precision input n flags an EOC interrupt.
0b - Interrupt is not flagged
1b - Interrupt is flagged
0
PIEOCIEN0
Precision Input EOC Interrupt Enable
Specifies whether a completed conversion of precision input n flags an EOC interrupt.
0b - Interrupt is not flagged
1b - Interrupt is flagged
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2385 / 5251


---
# 페이지 77

60.6.2.10
EOC Interrupt Enable For Standard Inputs (CIMR1)
Offset
Register
Offset
CIMR1
28h
Function
Specifies whether a completed conversion of a standard input flags an EOC interrupt.
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
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
W
Reset
0
0
0
0
0
0
0
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
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
SIEOC
IE...
W
Reset
0
0
0
0
0
0
0
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
—
Reserved
23-0
SIEOCIENn
Standard Input EOC Interrupt Enable
Specifies whether a completed conversion of standard input n flags an EOC interrupt.
0b - Interrupt is not flagged
1b - Interrupt is flagged
60.6.2.11
EOC Interrupt Enable For External Inputs (CIMR2)
Offset
Register
Offset
CIMR2
2Ch
Function
Specifies whether a completed conversion of an external input flags an EOC interrupt.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2386 / 5251


---
# 페이지 78

 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
ADC_0
CIMR2
—
ADC_1
CIMR2
—
ADC_2
—
CIMR2
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
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
W
Reset
0
0
0
0
0
0
0
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
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
EIEOC
IE...
W
Reset
0
0
0
0
0
0
0
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
EIEOCIENn
External Input EOC Interrupt Enable
Specifies whether a completed conversion of external input n flags an EOC interrupt.
0b - Interrupt is not flagged
1b - Interrupt is flagged
60.6.2.12
Analog Watchdog Threshold Interrupt Status (WTISR)
Offset
Register
Offset
WTISR
30h
Function
Contains flags that indicate the result of a comparison between the conversion result and the threshold value defined in the 
analog watchdog.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2387 / 5251


---
# 페이지 79

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
HAWI
F16 
LAWIF
16 
HAWI
F15 
LAWIF
15 
HAWI
F14 
LAWIF
14 
HAWI
F13 
LAWIF
13 
HAWI
F12 
LAWIF
12 
HAWI
F11 
LAWIF
11 
HAWI
F10 
LAWIF
10 
HAWI
F9 
LAWIF
9 
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
HAWI
F8 
LAWIF
8 
HAWI
F7 
LAWIF
7 
HAWI
F6 
LAWIF
6 
HAWI
F5 
LAWIF
5 
HAWI
F4 
LAWIF
4 
HAWI
F3 
LAWIF
3 
HAWI
F2 
LAWIF
2 
HAWI
F1 
LAWIF
1 
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
HAWIF16
High Analog Watchdog Interrupt Flag 16
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 
16.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
0b - No effect
1b - Clears flag
30
LAWIF16
Low Analog Watchdog Interrupt Flag 16
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 16.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is greater than the specified low threshold
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
29
High Analog Watchdog Interrupt Flag 15
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2388 / 5251


---
# 페이지 80

Table continued from the previous page...
Field
Function
HAWIF15
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 
15.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
0b - No effect
1b - Clears flag
28
LAWIF15
Low Analog Watchdog Interrupt Flag 15
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 15.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is greater than the specified low threshold
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
27
HAWIF14
High Analog Watchdog Interrupt Flag 14
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 
14.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
0b - No effect
1b - Clears flag
26
LAWIF14
Low Analog Watchdog Interrupt Flag 14
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 14.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2389 / 5251


---
# 페이지 81

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is greater than the specified low threshold
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
25
HAWIF13
High Analog Watchdog Interrupt Flag 13
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 
13.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
0b - No effect
1b - Clears flag
24
LAWIF13
Low Analog Watchdog Interrupt Flag 13
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 13.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is greater than the specified low threshold
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
23
HAWIF12
High Analog Watchdog Interrupt Flag 12
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 
12.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2390 / 5251


---
# 페이지 82

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
0b - No effect
1b - Clears flag
22
LAWIF12
Low Analog Watchdog Interrupt Flag 12
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 12.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is greater than the specified low threshold
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
21
HAWIF11
High Analog Watchdog Interrupt Flag 11
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 
11.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
0b - No effect
1b - Clears flag
20
LAWIF11
Low Analog Watchdog Interrupt Flag 11
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 11.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2391 / 5251


---
# 페이지 83

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is greater than the specified low threshold
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
19
HAWIF10
High Analog Watchdog Interrupt Flag 10
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 
10.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
0b - No effect
1b - Clears flag
18
LAWIF10
Low Analog Watchdog Interrupt Flag 10
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 10.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is greater than the specified low threshold
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
17
HAWIF9
High Analog Watchdog Interrupt Flag 9
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 9.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2392 / 5251


---
# 페이지 84

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
0b - No effect
1b - Clears flag
16
LAWIF9
Low Analog Watchdog Interrupt Flag 9
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 9.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is greater than the specified low threshold
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
15
HAWIF8
High Analog Watchdog Interrupt Flag 8
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 8.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
0b - No effect
1b - Clears flag
14
LAWIF8
Low Analog Watchdog Interrupt Flag 8
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 8.
 
This field behaves differently for register reads and writes.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2393 / 5251


---
# 페이지 85

Table continued from the previous page...
Field
Function
When reading
0b - Conversion result is greater than the specified low threshold
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
13
HAWIF7
High Analog Watchdog Interrupt Flag 7
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 7.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
0b - No effect
1b - Clears flag
12
LAWIF7
Low Analog Watchdog Interrupt Flag 7
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 7.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is greater than the specified low threshold
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
11
HAWIF6
High Analog Watchdog Interrupt Flag 6
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 6.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2394 / 5251


---
# 페이지 86

Table continued from the previous page...
Field
Function
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
0b - No effect
1b - Clears flag
10
LAWIF6
Low Analog Watchdog Interrupt Flag 6
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 6.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is greater than the specified low threshold
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
9
HAWIF5
High Analog Watchdog Interrupt Flag 5
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 5.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
0b - No effect
1b - Clears flag
8
LAWIF5
Low Analog Watchdog Interrupt Flag 5
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 5.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is greater than the specified low threshold
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2395 / 5251


---
# 페이지 87

Table continued from the previous page...
Field
Function
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
7
HAWIF4
High Analog Watchdog Interrupt Flag 4
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 4.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
0b - No effect
1b - Clears flag
6
LAWIF4
Low Analog Watchdog Interrupt Flag 4
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 4.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is greater than the specified low threshold
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
5
HAWIF3
High Analog Watchdog Interrupt Flag 3
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 3.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2396 / 5251


---
# 페이지 88

Table continued from the previous page...
Field
Function
0b - No effect
1b - Clears flag
4
LAWIF3
Low Analog Watchdog Interrupt Flag 3
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 3.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is greater than the specified low threshold
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
3
HAWIF2
High Analog Watchdog Interrupt Flag 2
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 2.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
0b - No effect
1b - Clears flag
2
LAWIF2
Low Analog Watchdog Interrupt Flag 2
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 2.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is greater than the specified low threshold
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2397 / 5251


---
# 페이지 89

Table continued from the previous page...
Field
Function
1
HAWIF1
High Analog Watchdog Interrupt Flag 1
Indicates whether the conversion result is higher than the high threshold value of the analog watchdog 1.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is lower than the specified high threshold
1b - Conversion result is higher than the specified high threshold
When writing
0b - No effect
1b - Clears flag
0
LAWIF1
Low Analog Watchdog Interrupt Flag 1
Indicates whether the conversion result is lower than the low threshold value of the analog watchdog 1.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion result is greater than the specified low threshold
1b - Conversion result is lower than the specified low threshold
When writing
0b - No effect
1b - Clears flag
60.6.2.13
Analog Watchdog Threshold Interrupt Enable (WTIMR)
Offset
Register
Offset
WTIMR
34h
Function
Enables the interrupt for each analog watchdog threshold value.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2398 / 5251


---
# 페이지 90

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
HDWI
FEN4 
LAWIF
EN4 
HDWI
FEN3 
LAWIF
EN3 
HDWI
FEN2 
LAWIF
EN2 
HDWI
FEN1 
LAWIF
EN1 
W
Reset
0
0
0
0
0
0
0
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
7
HDWIFEN4
High Data Watchdog Interrupt Flag Enable n
Enables flagging of an interrupt when a conversion result is higher than the high threshold value of the 
analog watchdog n.
0b - Interrupt is not flagged
1b - Interrupt is flagged
6
LAWIFEN4
Low Analog Watchdog Interrupt Flag Enable n
Enables flagging of an interrupt when a conversion result is lower than the low threshold value of analog 
watchdog n.
0b - Interrupt is not flagged
1b - Interrupt is flagged
5
HDWIFEN3
High Data Watchdog Interrupt Flag Enable n
Enables flagging of an interrupt when a conversion result is higher than the high threshold value of the 
analog watchdog n.
0b - Interrupt is not flagged
1b - Interrupt is flagged
4
LAWIFEN3
Low Analog Watchdog Interrupt Flag Enable n
Enables flagging of an interrupt when a conversion result is lower than the low threshold value of analog 
watchdog n.
0b - Interrupt is not flagged
1b - Interrupt is flagged
3
High Data Watchdog Interrupt Flag Enable n
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2399 / 5251


---
# 페이지 91

Table continued from the previous page...
Field
Function
HDWIFEN2
Enables flagging of an interrupt when a conversion result is higher than the high threshold value of the 
analog watchdog n.
0b - Interrupt is not flagged
1b - Interrupt is flagged
2
LAWIFEN2
Low Analog Watchdog Interrupt Flag Enable n
Enables flagging of an interrupt when a conversion result is lower than the low threshold value of analog 
watchdog n.
0b - Interrupt is not flagged
1b - Interrupt is flagged
1
HDWIFEN1
High Data Watchdog Interrupt Flag Enable n
Enables flagging of an interrupt when a conversion result is higher than the high threshold value of the 
analog watchdog n.
0b - Interrupt is not flagged
1b - Interrupt is flagged
0
LAWIFEN1
Low Analog Watchdog Interrupt Flag Enable n
Enables flagging of an interrupt when a conversion result is lower than the low threshold value of analog 
watchdog n.
0b - Interrupt is not flagged
1b - Interrupt is flagged
60.6.2.14
Direct Memory Access Configuration (DMAE)
Offset
Register
Offset
DMAE
40h
Function
Configures the DMA feature.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2400 / 5251


---
# 페이지 92

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
DCLR 
DMAE
N 
W
Reset
0
0
0
0
0
0
0
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
DCLR
DMA Clear Request
Selects one of the following events to clear a DMA request:
• DMA controller acknowledges the request.
• Application reads the conversion data register.
0b - DMA controller acknowledges the request
1b - Conversion data register is read
0
DMAEN
DMA Enable
Enables DMA.
0b - Disable
1b - Enable
60.6.2.15
DMA Request Enable For Precision Inputs (DMAR0)
Offset
Register
Offset
DMAR0
44h
Function
Selects the precision inputs that trigger a DMA request after conversion is complete.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2401 / 5251


---
# 페이지 93

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
Reserv
ed 
Reserv
ed 
PIDMA
RE...
PIDMA
RE...
PIDMA
RE...
PIDMA
RE...
PIDMA
RE...
PIDMA
RE...
PIDMA
RE...
PIDMA
RE...
W
Reset
0
0
0
0
0
0
0
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
9
—
Reserved
8
—
Reserved
7
PIDMAREN7
Precision Input DMA Request Enable 7
Specifies whether a DMA request is triggered after conversion is complete for precision input 7.
0b - Not triggered
1b - Triggered
6
PIDMAREN6
Precision Input DMA Request Enable 6
Specifies whether a DMA request is triggered after conversion is complete for precision input 6.
0b - Not triggered
1b - Triggered
5
PIDMAREN5
Precision Input DMA Request Enable 5
Specifies whether a DMA request is triggered after conversion is complete for precision input 5.
0b - Not triggered
1b - Triggered
4
PIDMAREN4
Precision Input DMA Request Enable 4
Specifies whether a DMA request is triggered after conversion is complete for precision input 4.
0b - Not triggered
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2402 / 5251


---
# 페이지 94

Table continued from the previous page...
Field
Function
1b - Triggered
3
PIDMAREN3
Precision Input DMA Request Enable 3
Specifies whether a DMA request is triggered after conversion is complete for precision input 3.
0b - Not triggered
1b - Triggered
2
PIDMAREN2
Precision Input DMA Request Enable 2
Specifies whether a DMA request is triggered after conversion is complete for precision input 2.
0b - Not triggered
1b - Triggered
1
PIDMAREN1
Precision Input DMA Request Enable 1
Specifies whether a DMA request is triggered after conversion is complete for precision input 1.
0b - Not triggered
1b - Triggered
0
PIDMAREN0
Precision Input DMA Request Enable 0
Specifies whether a DMA request is triggered after conversion is complete for precision input 0.
0b - Not triggered
1b - Triggered
60.6.2.16
DMA Request Enable For Standard Inputs (DMAR1)
Offset
Register
Offset
DMAR1
48h
Function
Selects the standard inputs that trigger a DMA request after conversion is complete.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2403 / 5251


---
# 페이지 95

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
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
W
Reset
0
0
0
0
0
0
0
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
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
SIDMA
RE...
W
Reset
0
0
0
0
0
0
0
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
—
Reserved
23-0
SIDMARENn
Standard Input DMA Request Enable n
Specifies whether a DMA request is triggered after conversion is complete for standard input n.
0b - DMA request is not triggered
1b - DMA is request triggered
60.6.2.17
DMA Request Enable For External Inputs (DMAR2)
Offset
Register
Offset
DMAR2
4Ch
Function
Selects the external inputs that trigger a DMA request after conversion is complete.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
ADC_0
DMAR2
—
ADC_1
DMAR2
—
ADC_2
—
DMAR2
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2404 / 5251


---
# 페이지 96

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
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
W
Reset
0
0
0
0
0
0
0
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
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
EIDMA
RE...
W
Reset
0
0
0
0
0
0
0
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
EIDMARENn
External Input DMA Request Enable n
Specifies whether a DMA request is triggered after external input n is converted.
0b - DMA request is not triggered
1b - DMA request is triggered
60.6.2.18
Analog Watchdog Threshold Values (THRHLR0 - THRHLR3)
Offset
Register
Offset
THRHLR0
60h
THRHLR1
64h
THRHLR2
68h
THRHLR3
6Ch
Function
Specifies limits for the valid operating range of a monitored input.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2405 / 5251


---
# 페이지 97

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
THRH 
W
Reset
0
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
THRL 
W
Reset
0
0
0
0
0
0
0
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
30-16
THRH
High Threshold Value
If enabled, flags an interrupt when the converted data of the input is higher than this value.
15
—
Reserved
14-0
THRL
Low Threshold Value
If enabled, flags an interrupt when the converted data of the input is lower than this value.
60.6.2.19
Presampling Control (PSCR)
Offset
Register
Offset
PSCR
80h
Function
Configures ADC to presample an internal voltage before the actual input is converted.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2406 / 5251


---
# 페이지 98

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
PREV
AL2 
0
PREV
AL1 
0
PREV
AL0 
PREC
ONV 
W
Reset
0
0
0
0
0
0
0
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
31-6
—
Reserved
5
PREVAL2
Presampling Voltage Select For External Inputs
Selects the internal voltage that is presampled for external inputs.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
ADC_0
PSCR
—
ADC_1
PSCR
—
ADC_2
—
PSCR
0b - VREFL
1b - VREFH
4
—
Reserved
3
PREVAL1
Presampling Voltage Select For Standard Inputs
Selects the internal voltage that is presampled for standard inputs and for the temperature sensor.
0b - VREFL
1b - VREFH
2
Reserved
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2407 / 5251


---
# 페이지 99

Table continued from the previous page...
Field
Function
—
1
PREVAL0
Presampling Voltage Select For Precision Inputs
Selects the internal voltage that is presampled for precision inputs.
0b - VREFL
1b - VREFH
0
PRECONV
Convert Presampled Value
Specifies whether presampling is followed by the comparison. If enabled, presampling is followed by 
conversion and the result is written to the conversion data register of the selected input.
0b - No conversion after presampling
1b - Presampling is followed by conversion
60.6.2.20
Presampling Enable For Precision Inputs (PSR0)
Offset
Register
Offset
PSR0
84h
Function
Enables presampling for each precision input.
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
Reserv
ed 
Reserv
ed 
PRES
7 
PRES
6 
PRES
5 
PRES
4 
PRES
3 
PRES
2 
PRES
1 
PRES
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
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2408 / 5251


---
# 페이지 100

Fields
Field
Function
31-10
—
Reserved
9
—
Reserved
8
—
Reserved
7
PRES7
Presampling Enable n
Enables presampling for precision input n.
0b - Disable
1b - Enable
6
PRES6
Presampling Enable n
Enables presampling for precision input n.
0b - Disable
1b - Enable
5
PRES5
Presampling Enable n
Enables presampling for precision input n.
0b - Disable
1b - Enable
4
PRES4
Presampling Enable n
Enables presampling for precision input n.
0b - Disable
1b - Enable
3
PRES3
Presampling Enable n
Enables presampling for precision input n.
0b - Disable
1b - Enable
2
PRES2
Presampling Enable n
Enables presampling for precision input n.
0b - Disable
1b - Enable
1
Presampling Enable n
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2409 / 5251


---
# 페이지 101

Table continued from the previous page...
Field
Function
PRES1
Enables presampling for precision input n.
0b - Disable
1b - Enable
0
PRES0
Presampling Enable n
Enables presampling for precision input n.
0b - Disable
1b - Enable
60.6.2.21
Presampling Enable For Standard Inputs (PSR1)
Offset
Register
Offset
PSR1
88h
Function
Enables presampling for each standard input.
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
PRES
23 
PRES
22 
PRES
21 
PRES
20 
PRES
19 
PRES
18 
PRES
17 
PRES
16 
W
Reset
0
0
0
0
0
0
0
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
PRES
15 
PRES
14 
PRES
13 
PRES
12 
PRES
11 
PRES
10 
PRES
9 
PRES
8 
PRES
7 
PRES
6 
PRES
5 
PRES
4 
PRES
3 
PRES
2 
PRES
1 
PRES
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
31-24
—
Reserved
23-0
Presampling Enable n
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2410 / 5251


---
# 페이지 102

Table continued from the previous page...
Field
Function
PRESn
Enables presampling for standard input n.
0b - Disable
1b - Enable
60.6.2.22
Presampling Enable For External Inputs (PSR2)
Offset
Register
Offset
PSR2
8Ch
Function
Enables presampling for each external input.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
ADC_0
PSR2
—
ADC_1
PSR2
—
ADC_2
—
PSR2
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
PRES
31 
PRES
30 
PRES
29 
PRES
28 
PRES
27 
PRES
26 
PRES
25 
PRES
24 
PRES
23 
PRES
22 
PRES
21 
PRES
20 
PRES
19 
PRES
18 
PRES
17 
PRES
16 
W
Reset
0
0
0
0
0
0
0
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
PRES
15 
PRES
14 
PRES
13 
PRES
12 
PRES
11 
PRES
10 
PRES
9 
PRES
8 
PRES
7 
PRES
6 
PRES
5 
PRES
4 
PRES
3 
PRES
2 
PRES
1 
PRES
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
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2411 / 5251


---
# 페이지 103

Fields
Field
Function
31-0
PRESn
Presampling Enable n
Enables presampling for external input n.
0b - Disable
1b - Enable
60.6.2.23
Conversion Timing For Precision Inputs (CTR0)
Offset
Register
Offset
CTR0
94h
Function
Specifies duration, in terms of the number of conversion clock cycles, of the sampling of precision inputs.
The conversion clock frequency depends on the configuration of MCR[ADCLKSEL].
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
INPSAMP 
W
Reset
0
0
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
1
0
Fields
Field
Function
31-8
—
Reserved
7-0
INPSAMP
Input Sample Cycles
Specifies the sample duration in terms of conversion clock cycles. The minimum value is 8. Specifying a 
lower value automatically forces a value of 8.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2412 / 5251


---
# 페이지 104

60.6.2.24
Conversion Timing For Standard Inputs (CTR1)
Offset
Register
Offset
CTR1
98h
Function
Specifies the duration, in terms of the number of conversion clock cycles, of the sampling of standard inputs or the 
temperature sensor.
The conversion clock frequency depends on the configuration of MCR[ADCLKSEL].
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
INPSAMP 
TSEN
SOR...
W
Reset
0
0
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
1
0
Fields
Field
Function
31-8
—
Reserved
7-1
INPSAMP
Specifies the sample duration in terms of conversion clock cycles. The minimum value is 8. Specifying a 
lower value automatically forces a value of 8.
This field uses the TSENSOR_SEL bit as its low-order bit. In other words, INPSAMP is effectively an 8-bit 
field, but the low-order bit has a dual function.
0
TSENSOR_SEL
Temperature Sensor Voltage Select
Selects the voltage for external temperature sensors (if available).
If a temperature sensor is available, this field may be used as the selector for the mux between two 
temperature sensors.
 
This field is applicable only when there is more than one temperature sensor.
  NOTE  
0b - Selects temperature sensor source 0
1b - Selects temperature sensor source 1
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2413 / 5251


---
# 페이지 105

60.6.2.25
Conversion Timing For External Inputs (CTR2)
Offset
Register
Offset
CTR2
9Ch
Function
Specifies the number of conversion clock cycles when the external inputs are sampled.
The conversion clock frequency depends on the configuration of MCR[ADCLKSEL].
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
ADC_0
CTR2
—
ADC_1
CTR2
—
ADC_2
—
CTR2
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
INPSAMP 
W
Reset
0
0
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
1
0
Fields
Field
Function
31-8
—
Reserved
7-0
INPSAMP
Input Sample Cycles
Specifies the sample duration in terms of conversion clock cycles. The minimum acceptable value is 8. 
Specifying a lower value automatically forces a value of 8.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2414 / 5251


---
# 페이지 106

60.6.2.26
Normal Conversion Enable For Precision Inputs (NCMR0)
Offset
Register
Offset
NCMR0
A4h
Function
Selects the precision inputs to be converted during a normal conversion.
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
Reserv
ed 
Reserv
ed 
CH7 
CH6 
CH5 
CH4 
CH3 
CH2 
CH1 
CH0 
W
Reset
0
0
0
0
0
0
0
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
9
—
Reserved
8
—
Reserved
7
CH7
Precision Input To Be Converted
Selects precision input n for conversion.
0b - Input is not selected
1b - Input is selected
6
CH6
Precision Input To Be Converted
Selects precision input n for conversion.
0b - Input is not selected
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2415 / 5251


---
# 페이지 107

Table continued from the previous page...
Field
Function
1b - Input is selected
5
CH5
Precision Input To Be Converted
Selects precision input n for conversion.
0b - Input is not selected
1b - Input is selected
4
CH4
Precision Input To Be Converted
Selects precision input n for conversion.
0b - Input is not selected
1b - Input is selected
3
CH3
Precision Input To Be Converted
Selects precision input n for conversion.
0b - Input is not selected
1b - Input is selected
2
CH2
Precision Input To Be Converted
Selects precision input n for conversion.
0b - Input is not selected
1b - Input is selected
1
CH1
Precision Input To Be Converted
Selects precision input n for conversion.
0b - Input is not selected
1b - Input is selected
0
CH0
Precision Input To Be Converted
Selects precision input n for conversion.
0b - Input is not selected
1b - Input is selected
60.6.2.27
Normal Conversion Enable For Standard Inputs (NCMR1)
Offset
Register
Offset
NCMR1
A8h
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2416 / 5251


---
# 페이지 108

Function
Selects the standard inputs to be converted during a normal conversion.
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
CH55 
CH54 
CH53 
CH52 
CH51 
CH50 
CH49 
CH48 
W
Reset
0
0
0
0
0
0
0
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
CH47 
CH46 
CH45 
CH44 
CH43 
CH42 
CH41 
CH40 
CH39 
CH38 
CH37 
CH36 
CH35 
CH34 
CH33 
CH32 
W
Reset
0
0
0
0
0
0
0
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
—
Reserved
23-0
CHn
Standard Input To Be Converted
Selects standard input n for conversion.
0b - Input n is not selected
1b - Input n is selected
60.6.2.28
Normal Conversion Enable For External Inputs (NCMR2)
Offset
Register
Offset
NCMR2
ACh
Function
Selects the external inputs to be converted during a normal conversion.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
ADC_0
NCMR2
—
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2417 / 5251


---
# 페이지 109

Table continued from the previous page...
Instance
Register supported
Register not supported
ADC_1
NCMR2
—
ADC_2
—
NCMR2
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
CH95 
CH94 
CH93 
CH92 
CH91 
CH90 
CH89 
CH88 
CH87 
CH86 
CH85 
CH84 
CH83 
CH82 
CH81 
CH80 
W
Reset
0
0
0
0
0
0
0
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
CH79 
CH78 
CH77 
CH76 
CH75 
CH74 
CH73 
CH72 
CH71 
CH70 
CH69 
CH68 
CH67 
CH66 
CH65 
CH64 
W
Reset
0
0
0
0
0
0
0
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
CHn
External Input To Be Converted
Selects external input n for conversion.
0b - Input n is not selected
1b - Input n is selected
60.6.2.29
Injected Conversion Enable For Precision Inputs (JCMR0)
Offset
Register
Offset
JCMR0
B4h
Function
Selects the precision inputs to be converted during an injected conversion.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2418 / 5251


---
# 페이지 110

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
Reserv
ed 
Reserv
ed 
CH7 
CH6 
CH5 
CH4 
CH3 
CH2 
CH1 
CH0 
W
Reset
0
0
0
0
0
0
0
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
9
—
Reserved
8
—
Reserved
7
CH7
Precision Input To Be Converted
Selects precision input 7 for conversion.
0b - Input 7 is not selected
1b - Input 7 is selected
6
CH6
Precision Input To Be Converted
Selects precision input 6 for conversion.
0b - Input 6 is not selected
1b - Input 6 is selected
5
CH5
Precision Input To Be Converted
Selects precision input 5 for conversion.
0b - Input 5 is not selected
1b - Input 5 is selected
4
CH4
Precision Input To Be Converted
Selects precision input 4 for conversion.
0b - Input 4 is not selected
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2419 / 5251


---
# 페이지 111

Table continued from the previous page...
Field
Function
1b - Input 4 is selected
3
CH3
Precision Input To Be Converted
Selects precision input 3 for conversion.
0b - Input 3 is not selected
1b - Input 3 is selected
2
CH2
Precision Input To Be Converted
Selects precision input 2 for conversion.
0b - Input 2 is not selected
1b - Input 2 is selected
1
CH1
Precision Input To Be Converted
Selects precision input 1 for conversion.
0b - Input 1 is not selected
1b - Input 1 is selected
0
CH0
Precision Input To Be Converted
Selects precision input 0 for conversion.
0b - Input 0 is not selected
1b - Input 0 is selected
60.6.2.30
Injected Conversion Enable For Standard Inputs (JCMR1)
Offset
Register
Offset
JCMR1
B8h
Function
Selects the standard inputs to be converted during an injected conversion.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2420 / 5251


---
# 페이지 112

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
CH55 
CH54 
CH53 
CH52 
CH51 
CH50 
CH49 
CH48 
W
Reset
0
0
0
0
0
0
0
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
CH47 
CH46 
CH45 
CH44 
CH43 
CH42 
CH41 
CH40 
CH39 
CH38 
CH37 
CH36 
CH35 
CH34 
CH33 
CH32 
W
Reset
0
0
0
0
0
0
0
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
—
Reserved
23-0
CHn
Standard Input To Be Converted
Selects standard input n for conversion.
0b - Input n is not selected
1b - Input n is selected
60.6.2.31
Injected Conversion Enable For External Inputs (JCMR2)
Offset
Register
Offset
JCMR2
BCh
Function
Selects the external inputs to be converted during an injected conversion.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
ADC_0
JCMR2
—
ADC_1
JCMR2
—
ADC_2
—
JCMR2
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2421 / 5251


---
# 페이지 113

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
CH95 
CH94 
CH93 
CH92 
CH91 
CH90 
CH89 
CH88 
CH87 
CH86 
CH85 
CH84 
CH83 
CH82 
CH81 
CH80 
W
Reset
0
0
0
0
0
0
0
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
CH79 
CH78 
CH77 
CH76 
CH75 
CH74 
CH73 
CH72 
CH71 
CH70 
CH69 
CH68 
CH67 
CH66 
CH65 
CH64 
W
Reset
0
0
0
0
0
0
0
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
CHn
External Input To Be Converted
Selects external input n for conversion.
0b - Input n is not selected
1b - Input n is selected
60.6.2.32
Delay Start Of Data Conversion (DSDR)
Offset
Register
Offset
DSDR
C4h
Function
Delays the start of the conversion when another input channel is selected. The necessary delay depends on the device 
characteristics of, for example, the input channel multiplexer.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
ADC_0
DSDR
—
ADC_1
DSDR
—
ADC_2
—
DSDR
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2422 / 5251


---
# 페이지 114

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
DSD 
W
Reset
0
0
0
0
0
0
0
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
DSD
Delay
Specifies the delay in terms of the number of module clock cycles.
60.6.2.33
Power Down Exit Delay (PDEDR)
Offset
Register
Offset
PDEDR
C8h
Function
Delays the transition out of Power Down into Idle state to wait for necessary settling times. See the device data sheet for the 
minimal time between the power-down exit request and when ADC can start a conversion.
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
PDED 
W
Reset
0
0
0
0
0
0
0
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
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2423 / 5251


---
# 페이지 115

Fields
Field
Function
31-8
—
Reserved
7-0
PDED
Delay
Specifies a delay in terms of the number of conversion clock cycles.
60.6.2.34
Precision Input n Conversion Data (PCDR0 - PCDR7)
Offset
For n = 0 to 7:
Register
Offset
PCDRn
100h + (n × 4h)
Function
Contains conversion data from precision input n.
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
VALID 
OVER
W 
RESULT 
W
Reset
0
0
0
0
0
0
0
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
CDATA 
W
Reset
0
0
0
0
0
0
0
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
31-20
—
Reserved
19
VALID
Conversion Data Available
Indicates whether new conversion data is available. This field is automatically reset to 0 when the data is 
read.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2424 / 5251


---
# 페이지 116

Table continued from the previous page...
Field
Function
0b - No unread conversion data
1b - Unread conversion data is available
18
OVERW
Overwrite Status Flag
Indicates whether the previous conversion data was overwritten without having been read, in which case 
the overwritten data is lost.
The ability to overwrite conversion data is controlled by MCR[OWREN].
0b - No unread data is overwritten
1b - Unread data is overwritten
17-16
RESULT
Conversion Data Type
Indicates the type of trigger that started the conversion for this conversion data.
00b - Normal trigger
01b - Injected trigger
10b - BCTU trigger
15-0
CDATA
Conversion Data
Contains conversion data from precision input n, determined by the successive approximation algorithm. 
The conversion data is always 15 bits wide, regardless of the conversion resolution selected 
(CALBISTREG[RESN]).
Depending on the value of MCR[WLSIDE], the conversion data can be in bits [14:0] (MCR[WLSIDE] = 0), 
or in bits [15:1] (MCR[WLSIDE] = 1).
60.6.2.35
Standard Input n Conversion Data (ICDR0 - ICDR23)
Offset
For a = 0 to 23:
Register
Offset
ICDRa
180h + (a × 4h)
Function
Contains conversion data from standard input n.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2425 / 5251


---
# 페이지 117

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
VALID 
OVER
W 
RESULT 
W
Reset
0
0
0
0
0
0
0
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
CDATA 
W
Reset
0
0
0
0
0
0
0
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
31-20
—
Reserved
19
VALID
Conversion Data Available
Indicates whether new conversion data is available. This field is automatically reset to 0 when the data is 
read.
0b - No unread conversion data
1b - Unread conversion data is available
18
OVERW
Overwrite Status Flag
Indicates whether the previous conversion data was overwritten without having been read, in which case 
the overwritten data is lost.
The ability to overwrite conversion data is controlled by MCR[OWREN].
0b - No unread data is overwritten
1b - Unread data is overwritten
17-16
RESULT
Conversion Data Type
Indicates the type of trigger that started the conversion for this conversion data.
00b - Normal trigger
01b - Injected trigger
10b - BCTU trigger
15-0
CDATA
Conversion Data
Contains conversion data from standard input n, determined by the SAR algorithm. The conversion data 
bit count is dependent on the conversion resolution selected (CALBISTREG[RESN]).
Depending on the value of MCR[WLSIDE], the conversion data MSB bits start from 14 (MCR[WLSIDE] = 0), 
or 15 (MCR[WLSIDE] = 1).
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2426 / 5251


---
# 페이지 118

60.6.2.36
External Input n Conversion Data (ECDR0 - ECDR31)
Offset
For a = 0 to 31:
Register
Offset
ECDRa
200h + (a × 4h)
Function
Contains conversion data from external input n.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
ADC_0
ECDR0–ECDR31
—
ADC_1
ECDR0–ECDR31
—
ADC_2
—
ECDR0–ECDR31
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
VALID 
OVER
W 
RESULT 
W
Reset
0
0
0
0
0
0
0
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
CDATA 
W
Reset
0
0
0
0
0
0
0
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
31-20
—
Reserved
19
VALID
Conversion Data Available
Indicates whether new conversion data is available. This field is automatically reset to 0 when the data is 
read.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2427 / 5251


---
# 페이지 119

Table continued from the previous page...
Field
Function
0b - No unread conversion data
1b - Unread conversion data is available
18
OVERW
Overwrite Status Flag
Indicates whether the previous conversion data was overwritten without having been read, in which case 
the overwritten data is lost.
The ability to overwrite conversion data is controlled by MCR[OWREN].
0b - No unread data is overwritten
1b - Unread data is overwritten
17-16
RESULT
Conversion Data Type
Indicates the type of trigger that started the conversion for this conversion data.
00b - Normal trigger
01b - Injected trigger
10b - BCTU trigger
15-0
CDATA
Conversion Data
Contains conversion data from external input n, determined by the SAR algorithm. The conversion data 
is always 15 bits wide, regardless of the conversion resolution selected (CALBISTREG[RESN]).
Depending on the value of MCR[WLSIDE], the conversion data can be in bits [14:0] (MCR[WLSIDE] = 0), 
or in bits [15:1] (MCR[WLSIDE] = MCR[WLSIDE]).
60.6.2.37
Channel Analog Watchdog Select For Precision Inputs (CWSELRPI0)
Offset
Register
Offset
CWSELRPI0
2B0h
Function
Selects the analog watchdog threshold register (THRHLR) that provides limits to monitor precision inputs.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2428 / 5251


---
# 페이지 120

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
WSEL_SI0_7 
0
WSEL_SI0_6 
0
WSEL_SI0_5 
0
WSEL_SI0_4 
W
Reset
0
0
0
0
0
0
0
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
WSEL_SI0_3 
0
WSEL_SI0_2 
0
WSEL_SI0_1 
0
WSEL_SI0_0 
W
Reset
0
0
0
0
0
0
0
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
29-28
WSEL_SI0_7
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
27-26
—
Reserved
25-24
WSEL_SI0_6
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
23-22
—
Reserved
21-20
WSEL_SI0_5
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2429 / 5251


---
# 페이지 121

Table continued from the previous page...
Field
Function
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
19-18
—
Reserved
17-16
WSEL_SI0_4
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
15-14
—
Reserved
13-12
WSEL_SI0_3
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
11-10
—
Reserved
9-8
WSEL_SI0_2
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
7-6
—
Reserved
5-4
WSEL_SI0_1
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2430 / 5251


---
# 페이지 122

Table continued from the previous page...
Field
Function
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
3-2
—
Reserved
1-0
WSEL_SI0_0
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
60.6.2.38
Channel Analog Watchdog Select For Precision Inputs (CWSELRPI1)
Offset
Register
Offset
CWSELRPI1
2B4h
Function
Selects the analog watchdog threshold register (THRHLR) that provides limits to monitor precision inputs.
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
W
Reset
0
0
0
0
0
0
0
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
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2431 / 5251


---
# 페이지 123

Fields
Field
Function
31-8
—
Reserved
7-4
—
Reserved
3-0
—
Reserved
60.6.2.39
Channel Analog Watchdog Select For Standard Inputs (CWSELRSI0)
Offset
Register
Offset
CWSELRSI0
2C0h
Function
Selects the analog watchdog threshold register (THRHLR) that provides limits to monitor the standard inputs.
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
WSEL_SI7_0 
0
WSEL_SI6_0 
0
WSEL_SI5_0 
0
WSEL_SI4_0 
W
Reset
0
0
0
0
0
0
0
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
WSEL_SI3_0 
0
WSEL_SI2_0 
0
WSEL_SI1_0 
0
WSEL_SI0_0 
W
Reset
0
0
0
0
0
0
0
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
29-28
WSEL_SI7_0
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2432 / 5251


---
# 페이지 124

Table continued from the previous page...
Field
Function
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
27-26
—
Reserved
25-24
WSEL_SI6_0
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
23-22
—
Reserved
21-20
WSEL_SI5_0
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
19-18
—
Reserved
17-16
WSEL_SI4_0
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
15-14
—
Reserved
13-12
Analog Watchdog Selection
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2433 / 5251


---
# 페이지 125

Table continued from the previous page...
Field
Function
WSEL_SI3_0
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
11-10
—
Reserved
9-8
WSEL_SI2_0
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
7-6
—
Reserved
5-4
WSEL_SI1_0
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
3-2
—
Reserved
1-0
WSEL_SI0_0
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2434 / 5251


---
# 페이지 126

60.6.2.40
Channel Analog Watchdog Select For Standard Inputs (CWSELRSI1)
Offset
Register
Offset
CWSELRSI1
2C4h
Function
Selects the analog watchdog threshold register (THRHLR) that provides limits to monitor the standard inputs.
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
WSEL_SI7_1 
0
WSEL_SI6_1 
0
WSEL_SI5_1 
0
WSEL_SI4_1 
W
Reset
0
0
0
0
0
0
0
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
WSEL_SI3_1 
0
WSEL_SI2_1 
0
WSEL_SI1_1 
0
WSEL_SI0_1 
W
Reset
0
0
0
0
0
0
0
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
29-28
WSEL_SI7_1
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
27-26
—
Reserved
25-24
WSEL_SI6_1
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2435 / 5251


---
# 페이지 127

Table continued from the previous page...
Field
Function
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
23-22
—
Reserved
21-20
WSEL_SI5_1
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
19-18
—
Reserved
17-16
WSEL_SI4_1
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
15-14
—
Reserved
13-12
WSEL_SI3_1
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
11-10
—
Reserved
9-8
WSEL_SI2_1
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2436 / 5251


---
# 페이지 128

Table continued from the previous page...
Field
Function
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
7-6
—
Reserved
5-4
WSEL_SI1_1
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
3-2
—
Reserved
1-0
WSEL_SI0_1
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
60.6.2.41
Channel Analog Watchdog Select For Standard Inputs (CWSELRSI2)
Offset
Register
Offset
CWSELRSI2
2C8h
Function
Selects the analog watchdog threshold register (THRHLR) that provides limits to monitor the standard inputs.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2437 / 5251


---
# 페이지 129

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
WSEL_SI7_2 
0
WSEL_SI6_2 
0
WSEL_SI5_2 
0
WSEL_SI4_2 
W
Reset
0
0
0
0
0
0
0
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
WSEL_SI3_2 
0
WSEL_SI2_2 
0
WSEL_SI1_2 
0
WSEL_SI0_2 
W
Reset
0
0
0
0
0
0
0
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
29-28
WSEL_SI7_2
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
27-26
—
Reserved
25-24
WSEL_SI6_2
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
23-22
—
Reserved
21-20
WSEL_SI5_2
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2438 / 5251


---
# 페이지 130

Table continued from the previous page...
Field
Function
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
19-18
—
Reserved
17-16
WSEL_SI4_2
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
15-14
—
Reserved
13-12
WSEL_SI3_2
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
11-10
—
Reserved
9-8
WSEL_SI2_2
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
7-6
—
Reserved
5-4
WSEL_SI1_2
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2439 / 5251


---
# 페이지 131

Table continued from the previous page...
Field
Function
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
3-2
—
Reserved
1-0
WSEL_SI0_2
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
60.6.2.42
Channel Analog Watchdog Select For External inputs (CWSELREI0)
Offset
Register
Offset
CWSELREI0
2D0h
Function
Selects the analog watchdog threshold register (THRHLR) that provides limits to monitor external inputs.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
ADC_0
CWSELREI0
—
ADC_1
CWSELREI0
—
ADC_2
—
CWSELREI0
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2440 / 5251


---
# 페이지 132

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
WSEL_SI0_7 
0
WSEL_SI0_6 
0
WSEL_SI0_5 
0
WSEL_SI0_4 
W
Reset
0
0
0
0
0
0
0
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
WSEL_SI0_3 
0
WSEL_SI0_2 
0
WSEL_SI0_1 
0
WSEL_SI0_0 
W
Reset
0
0
0
0
0
0
0
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
29-28
WSEL_SI0_7
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
27-26
—
Reserved
25-24
WSEL_SI0_6
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
23-22
—
Reserved
21-20
WSEL_SI0_5
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2441 / 5251


---
# 페이지 133

Table continued from the previous page...
Field
Function
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
19-18
—
Reserved
17-16
WSEL_SI0_4
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
15-14
—
Reserved
13-12
WSEL_SI0_3
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
11-10
—
Reserved
9-8
WSEL_SI0_2
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
7-6
—
Reserved
5-4
WSEL_SI0_1
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2442 / 5251


---
# 페이지 134

Table continued from the previous page...
Field
Function
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
3-2
—
Reserved
1-0
WSEL_SI0_0
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
60.6.2.43
Channel Analog Watchdog Select For External inputs (CWSELREI1)
Offset
Register
Offset
CWSELREI1
2D4h
Function
Selects the analog watchdog threshold register (THRHLR) that provides limits to monitor external inputs.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
ADC_0
CWSELREI1
—
ADC_1
CWSELREI1
—
ADC_2
—
CWSELREI1
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2443 / 5251


---
# 페이지 135

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
WSEL_SI1_15 
0
WSEL_SI1_14 
0
WSEL_SI1_13 
0
WSEL_SI1_12 
W
Reset
0
0
0
0
0
0
0
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
WSEL_SI1_11 
0
WSEL_SI1_10 
0
WSEL_SI1_9 
0
WSEL_SI1_8 
W
Reset
0
0
0
0
0
0
0
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
29-28
WSEL_SI1_15
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
27-26
—
Reserved
25-24
WSEL_SI1_14
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
23-22
—
Reserved
21-20
WSEL_SI1_13
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2444 / 5251


---
# 페이지 136

Table continued from the previous page...
Field
Function
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
19-18
—
Reserved
17-16
WSEL_SI1_12
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
15-14
—
Reserved
13-12
WSEL_SI1_11
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
11-10
—
Reserved
9-8
WSEL_SI1_10
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
7-6
—
Reserved
5-4
WSEL_SI1_9
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2445 / 5251


---
# 페이지 137

Table continued from the previous page...
Field
Function
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
3-2
—
Reserved
1-0
WSEL_SI1_8
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
60.6.2.44
Channel Analog Watchdog Select For External inputs (CWSELREI2)
Offset
Register
Offset
CWSELREI2
2D8h
Function
Selects the analog watchdog threshold register (THRHLR) that provides limits to monitor external inputs.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
ADC_0
CWSELREI2
—
ADC_1
CWSELREI2
—
ADC_2
—
CWSELREI2
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2446 / 5251


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
0
WSEL_SI2_23 
0
WSEL_SI2_22 
0
WSEL_SI2_21 
0
WSEL_SI2_20 
W
Reset
0
0
0
0
0
0
0
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
WSEL_SI2_19 
0
WSEL_SI2_18 
0
WSEL_SI2_17 
0
WSEL_SI2_16 
W
Reset
0
0
0
0
0
0
0
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
29-28
WSEL_SI2_23
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
27-26
—
Reserved
25-24
WSEL_SI2_22
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
23-22
—
Reserved
21-20
WSEL_SI2_21
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2447 / 5251


---
# 페이지 139

Table continued from the previous page...
Field
Function
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
19-18
—
Reserved
17-16
WSEL_SI2_20
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
15-14
—
Reserved
13-12
WSEL_SI2_19
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
11-10
—
Reserved
9-8
WSEL_SI2_18
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
7-6
—
Reserved
5-4
WSEL_SI2_17
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2448 / 5251


---
# 페이지 140

Table continued from the previous page...
Field
Function
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
3-2
—
Reserved
1-0
WSEL_SI2_16
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
60.6.2.45
Channel Analog Watchdog Select For External inputs (CWSELREI3)
Offset
Register
Offset
CWSELREI3
2DCh
Function
Selects the analog watchdog threshold register (THRHLR) that provides limits to monitor external inputs.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
ADC_0
CWSELREI3
—
ADC_1
CWSELREI3
—
ADC_2
—
CWSELREI3
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2449 / 5251


---
# 페이지 141

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
WSEL_SI3_31 
0
WSEL_SI3_30 
0
WSEL_SI3_29 
0
WSEL_SI3_28 
W
Reset
0
0
0
0
0
0
0
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
WSEL_SI3_27 
0
WSEL_SI3_26 
0
WSEL_SI3_25 
0
WSEL_SI3_24 
W
Reset
0
0
0
0
0
0
0
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
29-28
WSEL_SI3_31
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
27-26
—
Reserved
25-24
WSEL_SI3_30
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
23-22
—
Reserved
21-20
WSEL_SI3_29
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2450 / 5251


---
# 페이지 142

Table continued from the previous page...
Field
Function
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
19-18
—
Reserved
17-16
WSEL_SI3_28
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
15-14
—
Reserved
13-12
WSEL_SI3_27
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
11-10
—
Reserved
9-8
WSEL_SI3_26
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
7-6
—
Reserved
5-4
WSEL_SI3_25
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2451 / 5251


---
# 페이지 143

Table continued from the previous page...
Field
Function
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
3-2
—
Reserved
1-0
WSEL_SI3_24
Analog Watchdog Selection
Selects the analog watchdog thresholds that the input is to be compared to.
00b - Analog watchdog THRHLR0
01b - Analog watchdog THRHLR1
10b - Analog watchdog THRHLR2
11b - Analog watchdog THRHLR3
60.6.2.46
Channel Watchdog Enable For Precision Inputs (CWENR0)
Offset
Register
Offset
CWENR0
2E0h
Function
Enables the analog watchdog per precision input.
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
Reserv
ed 
Reserv
ed 
CWEN
7 
CWEN
6 
CWEN
5 
CWEN
4 
CWEN
3 
CWEN
2 
CWEN
1 
CWEN
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
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2452 / 5251


---
# 페이지 144

Fields
Field
Function
31-10
—
Reserved
9
—
Reserved
8
—
Reserved
7
CWEN7
Channel Analog Watchdog Enable 7
Enables the analog watchdog for precision input 7.
When enabled, conversion data on the input is compared to the selected data watchdog threshold value.
0b - Disable
1b - Enable
6
CWEN6
Channel Analog Watchdog Enable 6
Enables the analog watchdog for precision input 6.
When enabled, conversion data on the input is compared to the selected data watchdog threshold value.
0b - Disable
1b - Enable
5
CWEN5
Channel Analog Watchdog Enable 5
Enables the analog watchdog for precision input 5.
When enabled, conversion data on the input is compared to the selected data watchdog threshold value.
0b - Disable
1b - Enable
4
CWEN4
Channel Analog Watchdog Enable 4
Enables the analog watchdog for precision input 4.
When enabled, conversion data on the input is compared to the selected data watchdog threshold value.
0b - Disable
1b - Enable
3
CWEN3
Channel Analog Watchdog Enable 3
Enables the analog watchdog for precision input 3.
When enabled, conversion data on the input is compared to the selected data watchdog threshold value.
0b - Disable
1b - Enable
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2453 / 5251


---
# 페이지 145

Table continued from the previous page...
Field
Function
2
CWEN2
Channel Analog Watchdog Enable 2
Enables the analog watchdog for precision input 2.
When enabled, conversion data on the input is compared to the selected data watchdog threshold value.
0b - Disable
1b - Enable
1
CWEN1
Channel Analog Watchdog Enable 1
Enables the analog watchdog for precision input 1.
When enabled, conversion data on the input is compared to the selected data watchdog threshold value.
0b - Disable
1b - Enable
0
CWEN0
Channel Analog Watchdog Enable 0
Enables the analog watchdog for precision input 0.
When enabled, conversion data on the input is compared to the selected data watchdog threshold value.
0b - Disable
1b - Enable
60.6.2.47
Channel Watchdog Enable For Standard Inputs (CWENR1)
Offset
Register
Offset
CWENR1
2E4h
Function
Enables the analog watchdog for standard input n.
When enabled, conversion data on the input is compared to the selected data watchdog threshold value.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2454 / 5251


---
# 페이지 146

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
CWEN
55 
CWEN
54 
CWEN
53 
CWEN
52 
CWEN
51 
CWEN
50 
CWEN
49 
CWEN
48 
W
Reset
0
0
0
0
0
0
0
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
CWEN
47 
CWEN
46 
CWEN
45 
CWEN
44 
CWEN
43 
CWEN
42 
CWEN
41 
CWEN
40 
CWEN
39 
CWEN
38 
CWEN
37 
CWEN
36 
CWEN
35 
CWEN
34 
CWEN
33 
CWEN
32 
W
Reset
0
0
0
0
0
0
0
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
—
Reserved
23-0
CWENn
Channel Analog Watchdog Enable For Standard Inputs
Enables the analog watchdog for standard input n.
0b - Disable
1b - Enable
60.6.2.48
Channel Watchdog Enable For External Inputs (CWENR2)
Offset
Register
Offset
CWENR2
2E8h
Function
Enables the analog watchdog per external input.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
ADC_0
CWENR2
—
ADC_1
CWENR2
—
ADC_2
—
CWENR2
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2455 / 5251


---
# 페이지 147

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
CWEN
95 
CWEN
94 
CWEN
93 
CWEN
92 
CWEN
91 
CWEN
90 
CWEN
89 
CWEN
88 
CWEN
87 
CWEN
86 
CWEN
85 
CWEN
84 
CWEN
83 
CWEN
82 
CWEN
81 
CWEN
80 
W
Reset
0
0
0
0
0
0
0
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
CWEN
79 
CWEN
78 
CWEN
77 
CWEN
76 
CWEN
75 
CWEN
74 
CWEN
73 
CWEN
72 
CWEN
71 
CWEN
70 
CWEN
69 
CWEN
68 
CWEN
67 
CWEN
66 
CWEN
65 
CWEN
64 
W
Reset
0
0
0
0
0
0
0
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
CWENn
Channel Analog Watchdog Enable For External Inputs
Enables the analog watchdog for external input n.
0b - Disable
1b - Enable
60.6.2.49
Analog Watchdog Out Of Range For Precision Inputs (AWORR0)
Offset
Register
Offset
AWORR0
2F0h
Function
Indicates the status of analog watchdog comparisons on precision inputs.
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
AWOR
_CH7 
AWOR
_CH6 
AWOR
_CH5 
AWOR
_CH4 
AWOR
_CH3 
AWOR
_CH2 
AWOR
_CH1 
AWOR
_CH0 
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
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2456 / 5251


---
# 페이지 148

Fields
Field
Function
31-10
—
Reserved
9
—
Reserved
8
—
Reserved
7
AWOR_CH7
Analog Watchdog Out Of Range For Precision Inputs
Indicates whether a data conversion on precision input 7 is out of the limits defined by the selected 
analog watchdog threshold value.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion is within limits
1b - Conversion is not within limits
When writing
0b - No effect
1b - Clears flag
6
AWOR_CH6
Analog Watchdog Out Of Range For Precision Inputs
Indicates whether a data conversion on precision input 6 is out of the limits defined by the selected 
analog watchdog threshold value.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion is within limits
1b - Conversion is not within limits
When writing
0b - No effect
1b - Clears flag
5
AWOR_CH5
Analog Watchdog Out Of Range For Precision Inputs
Indicates whether a data conversion on precision input 5 is out of the limits defined by the selected 
analog watchdog threshold value.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2457 / 5251


---
# 페이지 149

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion is within limits
1b - Conversion is not within limits
When writing
0b - No effect
1b - Clears flag
4
AWOR_CH4
Analog Watchdog Out Of Range For Precision Inputs
Indicates whether a data conversion on precision input 4 is out of the limits defined by the selected 
analog watchdog threshold value.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion is within limits
1b - Conversion is not within limits
When writing
0b - No effect
1b - Clears flag
3
AWOR_CH3
Analog Watchdog Out Of Range For Precision Inputs
Indicates whether a data conversion on precision input 3 is out of the limits defined by the selected 
analog watchdog threshold value.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion is within limits
1b - Conversion is not within limits
When writing
0b - No effect
1b - Clears flag
2
AWOR_CH2
Analog Watchdog Out Of Range For Precision Inputs
Indicates whether a data conversion on precision input 2 is out of the limits defined by the selected 
analog watchdog threshold value.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2458 / 5251


---
# 페이지 150

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion is within limits
1b - Conversion is not within limits
When writing
0b - No effect
1b - Clears flag
1
AWOR_CH1
Analog Watchdog Out Of Range For Precision Inputs
Indicates whether a data conversion on precision input 1 is out of the limits defined by the selected 
analog watchdog threshold value.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion is within limits
1b - Conversion is not within limits
When writing
0b - No effect
1b - Clears flag
0
AWOR_CH0
Analog Watchdog Out Of Range For Precision Inputs
Indicates whether a data conversion on precision input 0 is out of the limits defined by the selected 
analog watchdog threshold value.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion is within limits
1b - Conversion is not within limits
When writing
0b - No effect
1b - Clears flag
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2459 / 5251


---
# 페이지 151

60.6.2.50
Analog Watchdog Out Of Range For Standard Inputs (AWORR1)
Offset
Register
Offset
AWORR1
2F4h
Function
Indicates the status of analog watchdog comparisons on standard inputs.
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
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
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
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH9 
AWOR
_CH8 
AWOR
_CH7 
AWOR
_CH6 
AWOR
_CH5 
AWOR
_CH4 
AWOR
_CH3 
AWOR
_CH2 
AWOR
_CH1 
AWOR
_CH0 
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
31-24
—
Reserved
23-0
AWOR_CHn
Analog Watchdog Out Of Range For Standard Inputs
Indicates whether a data conversion on a standard input n is out of the limits defined by the selected 
analog watchdog threshold value.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Conversion is within limits
1b - Conversion is not within limits
When writing
0b - No effect
1b - Clears flag
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2460 / 5251


---
# 페이지 152

60.6.2.51
Analog Watchdog Out Of Range For External Inputs (AWORR2)
Offset
Register
Offset
AWORR2
2F8h
Function
Indicates the status of analog watchdog comparisons on external inputs.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
ADC_0
AWORR2
—
ADC_1
AWORR2
—
ADC_2
—
AWORR2
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
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
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
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH...
AWOR
_CH9 
AWOR
_CH8 
AWOR
_CH7 
AWOR
_CH6 
AWOR
_CH5 
AWOR
_CH4 
AWOR
_CH3 
AWOR
_CH2 
AWOR
_CH1 
AWOR
_CH0 
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
31-0
AWOR_CHn
Analog Watchdog Out Of Range For External Inputs
Indicates whether a data conversion on external input n is out of the limits defined by the selected analog 
watchdog threshold value.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2461 / 5251


---
# 페이지 153

Field
Function
0b - Conversion is within limits
1b - Conversion is not within limits
When writing
0b - No effect
1b - Clears flag
60.6.2.52
Self-Test Configuration 1 (STCR1)
Offset
Register
Offset
STCR1
340h
Function
Specifies the input sampling duration in terms of conversion clock cycles.
Conversion clock frequency depends on the configuration of MCR[ADCLKSEL].
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
INPSAMP_C 
0
W
Reset
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
INPSAMP_S 
0
W
Reset
0
0
1
0
0
1
0
1
0
0
0
0
0
1
1
1
Fields
Field
Function
31-24
INPSAMP_C
Input Sampling Time Algorithm C
Specifies the sample duration for test conversions related to algorithm C. The minimum acceptable value 
is 8. Specifying a lower value automatically forces a value of 8.
23-16
—
Reserved
15-8
Input Sampling Time Algorithm S
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2462 / 5251


---
# 페이지 154

Table continued from the previous page...
Field
Function
INPSAMP_S
Specifies sample duration for test conversions related to algorithm S. The minimum value is 8. 
Specifying a lower value automatically forces a value of 8.
7-0
—
Reserved
60.6.2.53
Self-Test Configuration 2 (STCR2)
Offset
Register
Offset
STCR2
344h
Function
Configures ADC self-test functions.
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
MSKW
DSE...
SERR 
MSKW
DTE...
0
MSKS
T_E...
0
MSKW
DG_...
0
MSKW
DG_...
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
MSKE
RR_C 
0
MSKE
RR_...
MSKE
RR_...
MSKE
RR_...
0
EN 
0
FMA_
WDS...
FMA_
WDT...
FMA_
C 
0
FMA_
S 
W
Reset
0
0
0
0
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
31-28
—
Reserved
27
MSKWDSERR
Mask Interrupt Self-Test Watchdog Sequence Error
Generates an interrupt when the WDSERR flag transitions to 1.
0b - No interrupt is generated
1b - Interrupt is generated
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2463 / 5251


---
# 페이지 155

Table continued from the previous page...
Field
Function
26
SERR
Self-Test Error Injection
Writes 1 to the STSR1[ERR_C], STSR1[ERR_S0], STSR1[ERR_S1], and STSR1[ERR_S2] status fields, 
causing an error. This field is reset to 0 immediately after writing.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Error can be injected
1b - Error is being injected
When writing
0b - No effect
1b - Injects a self-test error
25
MSKWDTERR
Mask Interrupt Self-Test Watchdog Timer Error
Generates an interrupt when the WDTERR flag is set.
0b - No interrupt is generated
1b - Interrupt is generated
24
—
Reserved
23
MSKST_EOC
Mask Interrupt Self-Test End Of Conversion
Generates an interrupt when the ST_EOC flag is set.
0b - No interrupt is generated
1b - Interrupt is generated
22-19
—
Reserved
18
MSKWDG_EOA
_C
Mask Error Interrupt End Of Algorithm C
Generates an interrupt when the WDG_EOA_C flag is set.
0b - No interrupt is generated
1b - Interrupt is generated
17
—
Reserved
16
MSKWDG_EOA
_S
Mask Error Interrupt End Of Algorithm S
Generates an interrupt when the WDG_EOA_S flag is set.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2464 / 5251


---
# 페이지 156

Table continued from the previous page...
Field
Function
0b - No interrupt is generated
1b - Interrupt is generated
15
MSKERR_C
Mask Error Interrupt Algorithm C
Generates an interrupt when the ERR_C flag is set.
0b - No interrupt is generated
1b - Interrupt is generated
14
—
Reserved
13
MSKERR_S2
Mask Error Interrupt Algorithm S2
Generates an interrupt when the ERR_S2 flag is set.
0b - No interrupt is generated
1b - Interrupt is generated
12
MSKERR_S1
Mask Error Interrupt Algorithm S1
Generates an interrupt when the ERR_S1 flag is set.
0b - No interrupt is generated
1b - Interrupt is generated
11
MSKERR_S0
Mask Error Interrupt Algorithm S0
Generates an interrupt when the ERR_S0 flag is set.
0b - No interrupt is generated
1b - Interrupt is generated
10-8
—
Reserved
7
EN
Self-Test Enable
Enables ADC structural self-test. When BCTU is enabled, this field has no effect. This field must be 1 
before starting normal conversion and must not be changed during conversion. This field must be reset 
to 0 only after end of conversion for the last self-test channel has been received.
0b - Disable
1b - Enable
6-5
—
Reserved
4
Fault Mapping Self-Test Watchdog Sequence Error
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2465 / 5251


---
# 페이지 157

Table continued from the previous page...
Field
Function
FMA_WDSERR
Specifies whether a self-test watchdog sequence error sets the flag on the critical or noncritical fault line.
0b - Noncritical fault line
1b - Critical fault line
3
FMA_WDTERR
Fault Mapping Self-Test Watchdog Timer Error
Specifies whether a self-test watchdog timer error sets the flag on the critical or noncritical fault line.
0b - Noncritical fault line
1b - Critical fault line
2
FMA_C
Fault Mapping Algorithm C
Specifies whether a fault in algorithm C sets the flag on the critical or noncritical fault line.
0b - Noncritical fault line
1b - Critical fault line
1
—
Reserved
0
FMA_S
Fault Mapping Algorithm S
Specifies whether a fault in algorithm S sets the flag on the critical or noncritical fault line.
0b - Noncritical fault line
1b - Critical fault line
60.6.2.54
Self-Test Configuration 3 (STCR3)
Offset
Register
Offset
STCR3
348h
Function
Configures ADC self-test functions. When BCTU is enabled, writes to the fields registers have no effect. This register must be 
programmed before starting a conversion and must not be changed when conversion is ongoing.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2466 / 5251


---
# 페이지 158

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
ALG 
0
MSTEP 
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
ALG
Algorithm Selection
One-Shot operation mode:
• 00 Algorithm S (single step = MSTEP)
• 01 Reserved
• 10 Algorithm C (single step = MSTEP)
• 11 Algorithm S (default)
(use for test/debug purposes)
Continuous conversion mode:
• 00 Algorithm S
• 01 Reserved
• 10 Algorithm C
• 11 Algorithm S + algorithm C (default)
7-5
—
Reserved
4-0
MSTEP
Algorithm Step
For One-Shot operation mode:
• MSTEP = 0 to 2 for algorithm S
• MSTEP = 0 to 11 for algorithm C
Unused codes are reserved and must not be used.
For Scan operation mode:
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2467 / 5251


---
# 페이지 159

Table continued from the previous page...
Field
Function
This field is not used in Scan operation mode because single-step execution (interleaved mode) is 
always performed.
This field must be programmed to zero in Scan operation mode.
60.6.2.55
Self-Test Baud Rate (STBRR)
Offset
Register
Offset
STBRR
34Ch
Function
Specifies when the self-test algorithm steps are executed and the maximum time allowed for self-test to finish.
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
WDT 
W
Reset
0
0
0
0
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
BR 
W
Reset
0
0
0
0
0
0
0
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
31-19
—
Reserved
18-16
WDT
Self-Test Watchdog Timer
Specifies the safe time period in terms of conversion clock cycles. The safe time period is the maximum 
duration until the running self-test is expected to finish.
000b - 8192 conversion clock cycles (~0.1 ms at 80 MHz)
001b - 39,936 conversion clock cycles (~0.5 ms at 80 MHz)
010b - 79,872 conversion clock cycles (~1 ms at 80 MHz)
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2468 / 5251


---
# 페이지 160

Table continued from the previous page...
Field
Function
011b - 159,744 conversion clock cycles (~2 ms at 80 MHz)
100b - 400,384 conversion clock cycles (~5 ms at 80 MHz)
101b - 799,744 conversion clock cycles (~10 ms at 80 MHz)
110b - 1,599,488 conversion clock cycles (~20 ms at 80 MHz)
111b - 3,999,744 conversion clock cycles (~50 ms at 80 MHz)
15-8
—
Reserved
7-0
BR
Baud Rate
Selects the number of conversions of the selected inputs, after which the next self-test algorithm step 
executes. This field must be programmed when STCR2[EN] is zero, that is, before enabling self-test.
0000_0000b - A step of the selected self-test algorithm is executed every time after the set of 
selected inputs has been converted.
1111_1111b - A step of the selected self-test algorithm is executed after the set of selected inputs 
has been converted 256 times.
60.6.2.56
Self-Test Status 1 (STSR1)
Offset
Register
Offset
STSR1
350h
Function
Indicates self-test status.
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
WDSE
RR 
0
WDTE
RR 
OVER
WR 
ST_
EOC 
0
WDG_
EOA...
0
WDG_
EOA...
W
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
ERR_
C 
0
ERR_
S2 
ERR_
S1 
ERR_
S0 
0
STEP_C 
0
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
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2469 / 5251


---
# 페이지 161

Fields
Field
Function
31-28
—
Reserved
27
WDSERR
Self-Test Watchdog Sequence Error
Indicates whether the selected self-test algorithm has executed in the correct sequence.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Algorithm executed in correct sequence
1b - Algorithm did not execute in correct sequence
When writing
0b - No effect
1b - Clears flag
26
—
Reserved
25
WDTERR
Self-Test Watchdog Timer Error
Indicates whether the self-test algorithm has finished within the defined safe time period.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Algorithm finished within the safe time period (or safe time period not yet elapsed).
1b - Algorithm did not finish within safe time period.
When writing
0b - No effect
1b - Clears flag
24
OVERWR
Self-Test Error Status Overwrite
Indicates whether an error occurred when the respective error status flag (ERR_S0, ERR_S1, ERR_S2, 
or ERR_C) was set.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No self-test error status flag overwritten
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2470 / 5251


---
# 페이지 162

Table continued from the previous page...
Field
Function
1b - Self-test error status flag overwritten
When writing
0b - No effect
1b - Clears flag
23
ST_EOC
Self-Test End Of Conversion
Indicates whether a self-test conversion has completed.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not complete
1b - Complete
When writing
0b - No effect
1b - Clears flag
22-19
—
Reserved
18
WDG_EOA_C
Self-Test Watchdog End Of Algorithm C
Indicates whether self-test algorithm C has completed.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not complete
1b - Complete
When writing
0b - No effect
1b - Clears flag
17
—
Reserved
16
WDG_EOA_S
Self-Test Watchdog End Of Algorithm S
Indicates whether self-test algorithm S has completed.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2471 / 5251


---
# 페이지 163

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not complete
1b - Complete
When writing
0b - No effect
1b - Clears flag
15
ERR_C
Error Algorithm C
Indicates whether an error occurred during execution of algorithm C.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No error
1b - Error
When writing
0b - No effect
1b - Clears flag
14
—
Reserved
13
ERR_S2
Error Algorithm S Step 2
Indicates whether an error occurred during execution of step 2 of algorithm S.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No error
1b - Error
When writing
0b - No effect
1b - Clears flag
12
ERR_S1
Error Algorithm S Step 1
Indicates whether an error occurred during execution of step 1 of algorithm S.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2472 / 5251


---
# 페이지 164

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No error
1b - Error
When writing
0b - No effect
1b - Clears flag
11
ERR_S0
Error Algorithm S Step 0
Indicates whether an error occurred during execution of step 0 of algorithm S.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No error
1b - Error
When writing
0b - No effect
1b - Clears flag
10
—
Reserved
9-5
STEP_C
Step Of Algorithm C
Indicates the step of self-test algorithm C in which an error occurred. Although this register field is 
read-only, no transfer error is generated when writing to it.
4-0
—
Reserved
60.6.2.57
Self-Test Status 2 (STSR2)
Offset
Register
Offset
STSR2
354h
Function
Contains the conversion result when an error in step 1 of algorithm S has occurred.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2473 / 5251


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
W
Reset
0
0
0
0
0
0
0
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
DATA0 
W
Reset
0
0
0
0
0
0
0
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
15
—
Reserved
14-0
DATA0
Conversion Data ERR_S1
Contains conversion data from the moment when the error in step 1 of algorithm S has occurred.
60.6.2.58
Self-Test Status 3 (STSR3)
Offset
Register
Offset
STSR3
358h
Function
Contains the conversion result when an error has occurred in step 2 or step 0 of algorithm S.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2474 / 5251


---
# 페이지 166

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
DATA1 
W
Reset
0
0
0
0
0
0
0
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
DATA0 
W
Reset
0
0
0
0
0
0
0
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
30-16
DATA1
Conversion Data ERR_S2
Contains conversion data from the moment when the error in step 2 of algorithm S has occurred.
15
—
Reserved
14-0
DATA0
Conversion Data ERR_S0
Contains the conversion data from the moment when the error in step 0 of algorithm S has occurred.
60.6.2.59
Self-Test Status 4 (STSR4)
Offset
Register
Offset
STSR4
35Ch
Function
Contains the conversion result when an error has occurred in algorithm C.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2475 / 5251


---
# 페이지 167

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
DATA1 
W
Reset
0
0
0
0
0
0
0
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
W
Reset
0
0
0
0
0
0
0
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
30-16
DATA1
Conversion Data ERR_C
Conversion data from the moment when the error in algorithm C has occurred.
15-0
—
Reserved
60.6.2.60
Self-Test Conversion Data 1 (STDR1)
Offset
Register
Offset
STDR1
370h
Function
Contains the result of the self-test conversion.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2476 / 5251


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
VALID 
OWER
WR 
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
TCDATA 
W
Reset
0
0
0
0
0
0
0
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
31-20
—
Reserved
19
VALID
Valid Conversion Data
Indicates that conversion data is available in TCDATA. This field is automatically reset to 0 when the 
conversion data is read.
0b - No unread conversion data
1b - Unread conversion data is available
18
OWERWR
Conversion Data Overwrite Status
Indicates whether the conversion data in TCDATA has been overwritten over previous data that had not 
been read.
0b - Current conversion data not overwritten
1b - Current conversion data was overwritten
17-16
—
Reserved
15
—
Reserved
14-0
TCDATA
Test Channel Conversion Data
Contains the conversion data from self-test. If overwrite is enabled (MCR[OWREN]=1), the conversion 
data is from the last-executed self-test conversion. When overwrite is not enabled, conversion data is 
available (not overwritten) until it is read by software. The conversion data in this register is in two's 
complement format.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2477 / 5251


---
# 페이지 169

60.6.2.61
Self-Test Analog Watchdog S0 (STAW0R)
Offset
Register
Offset
STAW0R
380h
Function
Configures self-test for step 0 of algorithm S.
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
AWDE 
WDTE 
THRH 
W
Reset
0
0
0
0
0
1
1
1
0
0
1
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
THRL 
W
Reset
0
0
0
0
0
1
0
0
1
1
0
0
0
1
0
1
Fields
Field
Function
31
AWDE
Self-Test Watchdog Enable
Enables the self-test watchdog for step 0 of algorithm S.
0b - Disable
1b - Enable
30
WDTE
Self-Test Watchdog Timer Enable
Enables the self-test watchdog timer for algorithm S.
The self-test watchdog timer verifies:
• Correct sequence of execution of the steps of the algorithm
• Execution of the algorithm within the safe time period as defined by STBRR[WDT]
This field must be 1 only in continuous conversion mode (MCR[MODE]=1).
The safe time period starts when this field is written with 1. If the safe time period has elapsed before 
algorithm S starts, the WDTERR flag is set. The safe time period is restarted each time algorithm S starts.
0b - Disable
1b - Enable
29-16
Higher Threshold Value
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2478 / 5251


---
# 페이지 170

Table continued from the previous page...
Field
Function
THRH
Sets the ERR_S0 flag when a self-test conversion value is greater than this value.
15
—
Reserved
14-0
THRL
Lower Threshold Value
Sets the ERR_S0 flag when a self-test conversion value is less than this value.
60.6.2.62
Self-Test Analog Watchdog S1 (STAW1R)
Offset
Register
Offset
STAW1R
388h
Function
Configures self-test for step 1 of algorithm S.
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
AWDE 
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
THRL 
W
Reset
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
1
1
1
0
0
1
Fields
Field
Function
31
AWDE
Self-Test Watchdog Enable
Enables the self-test watchdog for step 1 of algorithm S.
0b - Disable
1b - Enable
30-16
Reserved
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2479 / 5251


---
# 페이지 171

Table continued from the previous page...
Field
Function
—
15
—
Reserved
14-0
THRL
Lower Threshold Value
Sets the ERR_S1 flag when a self-test conversion value is less than this value.
60.6.2.63
Self-Test Analog Watchdog S2 (STAW2R)
Offset
Register
Offset
STAW2R
38Ch
Function
Configures self-test for step 2 of algorithm S.
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
AWDE 
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
THRL 
W
Reset
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
1
1
1
0
0
1
Fields
Field
Function
31
AWDE
Self-Test Watchdog Enable
Enables the self-test watchdog for step 2 of algorithm S.
0b - Disable
1b - Enable
30-16
Reserved
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2480 / 5251


---
# 페이지 172

Table continued from the previous page...
Field
Function
—
15
—
Reserved
14-0
THRL
Lower Threshold Value
Sets the ERR_S2 flag when a self-test conversion value is less than this value.
60.6.2.64
Self-Test Analog Watchdog C0 (STAW4R)
Offset
Register
Offset
STAW4R
394h
Function
Configures self-test for step 0 of algorithm C.
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
AWDE 
WDTE 
THRH 
W
Reset
0
0
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
THRL 
W
Reset
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
1
1
0
0
0
0
Fields
Field
Function
31
AWDE
Self-Test Watchdog Enable
Enables the self-test watchdog for algorithm C.
0b - Disable
1b - Enable
30
Self-Test Watchdog Timer Enable
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2481 / 5251


---
# 페이지 173

Table continued from the previous page...
Field
Function
WDTE
Enables the self-test watchdog timer for algorithm C.
The self-test watchdog timer verifies:
• Correct sequence of execution of algorithm steps
• Execution of the algorithm within the safe time period as defined by STBRR[WDT]
This field must be 1 only in continuous conversion mode (MODE 1).
The safe time period starts when this field is written with 1. If the safe time period elapses before algorithm 
C starts, the WDTERR flag is set. The safe time period is restarted each time algorithm C starts.
0b - Disable
1b - Enable
29-16
THRH
Higher Threshold Value
Sets the ERR_C flag when a self-test conversion value is greater than this value. This value must be in 
two's complement format and must be positive.
This value is valid only for step 0 of algorithm C (see STAW5R for the values used for the other steps of 
algorithm C).
15
—
Reserved
14-0
THRL
Lower Threshold Value
Sets the ERR_C flag when a self-test conversion value is less than this value. This value must be in 
two's complement format and must be negative. (With the reset value of this bit field, the test always 
fails. You must set at least STAW4R[14]=1, in order to have a negative value in this bit field.)
This value is used only for step 0 of algorithm C (see STAW5R for the values used for the other steps of 
algorithm C).
60.6.2.65
Self-Test Analog Watchdog C (STAW5R)
Offset
Register
Offset
STAW5R
398h
Function
Configures self-test for steps 1–11 of algorithm C.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2482 / 5251


---
# 페이지 174

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
THRH 
W
Reset
0
0
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
THRL 
W
Reset
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
1
1
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
30-16
THRH
Higher Threshold Value
Sets the ERR_C flag when a self-test conversion value is greater than this value. This value must be 
entered in two's complement format and must be positive.
This value is valid only for steps 1–11 of algorithm C (see STAW4R for the value used for step 0 of 
algorithm C).
15
—
Reserved
14-0
THRL
Lower Threshold Value
Sets the ERR_C flag when a self-test conversion value is less than this value. This value must be in 
two's complement format and must be negative.
This value is used only for steps 1–11 of algorithm C (see STAW4R for the value used for step 0 of 
algorithm C).
60.6.2.66
Analog Miscellaneous In/Out register (AMSIO)
Offset
Register
Offset
AMSIO
39Ch
Function
Configures the SAR algorithm compare step. In case you want to do a high-speed calibration or a high-speed conversion see 
Table 346. All other values in this register must stay at their reset value and may not be written.
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2483 / 5251


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
Reserved 
0
Reserv
ed 
HSEN 
CMPC
TRL0 
W
Reset
0
0
0
0
0
0
0
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
Reserved 
W
Reset
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
1
0
0
0
1
Fields
Field
Function
31-23
—
Reserved
22-21
—
Reserved
20
—
Reserved
19
—
Reserved
18-17
HSEN
High-Speed Enable
This setting must be adapted to the ADC clock frequency. See Table 346.
16
CMPCTRL0
Compare Control 0
This setting must be adapted to the ADC clock frequency. See Table 346.
15-12
—
Reserved
11-0
—
Reserved
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2484 / 5251


---
# 페이지 176

60.6.2.67
Control And Calibration Status (CALBISTREG)
Offset
Register
Offset
CALBISTREG
3A0h
Function
Controls several ADC functions for data conversion, calibration, and calibration status.
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
RESN 
TSAMP 
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
C_T_B
USY 
CALST
FUL 
Reserved 
Reserv
ed 
NR_SMPL 
AVG_
EN 
TEST_
FA...
0
TEST_
EN 
W
W1C
Reset
0
0
u
u
u
u
u
u
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
31-29
RESN
Conversion Resolution
Specifies the number of significant bits per conversion data (functional conversion only, not for 
calibration or self-test). Reducing this number speeds up the conversion because the SAR algorithm 
executes fewer steps. This field must be modified only when ADC is idle.
000b - 14-bit resolution
001b - 12-bit resolution
010b - 10-bit resolution
011b - 8-bit resolution
28-27
TSAMP
Sample Period In Calibration
Specifies the number of conversion clock cycles during which the reference voltage is sampled.
00b - 22 conversion clock cycles
01b - 8 conversion clock cycles
10b - 16 conversion clock cycles
11b - 32 conversion clock cycles
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2485 / 5251


---
# 페이지 177

Table continued from the previous page...
Field
Function
26-16
—
Reserved
The value of this field must not be modified.
15
C_T_BUSY
Calibration Busy
Indicates whether calibration is running.
0b - Calibration can be started
1b - Calibration is in progress
14
CALSTFUL
Calibration And Self-Test Full Range Comparison
Specifies the range of conversion data bits compared when ADC is calibrated or running self-test. 
Because the results from calibration and self-test are so low that the significant bits are in the lower 11 
bits only, the comparison cycles for the upper 4 bits can be skipped to reduce the execution duration of 
the calibration and of the self-test.
0b - Lowest 11 bits are compared.
1b - All 15 bits are compared.
13-8
—
Reserved
 
This field contains a value that ADC uses internally. Writing to this field can cause ADC to 
operate unreliably.
  CAUTION  
7
—
Reserved
This field is reserved and always has the value 0. Only the reset value can be written to this field.
6-5
NR_SMPL
Calibration Averaging Number
Specifies the number of data conversions per result (averaging) during calibration.
00b - 4 samples
01b - 8 samples
10b - 16 samples
11b - 32 samples
4
AVG_EN
Calibration Averaging Enable
Enables averaging of the calibration results over several conversion iterations to improve accuracy. This 
field only affects the calibration process.
0b - Disable
1b - Enable
3
TEST_FAIL
Calibration Status
Indicates calibration status. This field reads 0 when calibration is in progress. This field is reset to 0 when 
calibration starts.
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2486 / 5251


---
# 페이지 178

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Calibration finished successfully or has not been run since the last reset
1b - Calibration did not finish successfully
When writing
0b - No effect
1b - Clears flag
2-1
—
Reserved
0
TEST_EN
Calibration Enable
Calibrates ADC. This field automatically resets to 0 after the calibration is complete or is interrupted.
0b - Wait to start a calibration
1b - Start calibration
60.6.2.68
Offset And Gain User (OFSGNUSR)
Offset
Register
Offset
OFSGNUSR
3A8h
Function
Specifies the user-configured offset and gain values used by the SAR algorithm. The values must be written in two's 
complement format and can be either positive or negative.
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
GAIN_USER 
W
Reset
0
0
0
0
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
OFFSET_USER 
W
Reset
0
0
0
0
0
0
0
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
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2487 / 5251


---
# 페이지 179

Fields
Field
Function
31-26
—
Reserved
25-16
GAIN_USER
Gain User
Adds extra gain to the gain calculated during calibration. The value must be in two's complement format.
15-8
—
Reserved
7-0
OFFSET_USER
Offset User
Adds extra offset to the offset calculated by calibration. The value is must be in two's complement format.
60.6.2.69
Calibration Value 2 (CAL2)
Offset
Register
Offset
CAL2
3B4h
Function
Contains fields used during calibration.
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
Reserv
ed 
Reserved 
W
Reset
0
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
ENX 
0
Reserved 
W
Reset
1
0
0
0
0
0
1
0
0
1
0
0
0
0
1
1
Fields
Field
Function
31-24
—
Reserved
Table continues on the next page...
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2488 / 5251


---
# 페이지 180

Table continued from the previous page...
Field
Function
23
—
Reserved
22-16
—
Reserved
15
ENX
Enable X
Enables the inclusion of CLPX in error processing.
0b - Disable
1b - Enable
14-12
—
Reserved
11-0
—
Reserved
60.7 Glossary
CDAC
Capacitive digital to analog converter
CT
Compare phase time
DMA
Direct memory access
DP
Data processing time
PST
Presample phase time
ST
Sample phase time
SAR
Successive approximation
TPT
Trigger processing time
VrefH
Reference voltage high
VrefL
Reference voltage low
NXP Semiconductors
Analog-to-Digital Converter (ADC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2489 / 5251


---