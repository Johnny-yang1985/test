# 페이지 222

Chapter 62
Logic Control Unit (LCU)
62.1 Chip-specific LCU information
62.1.1 LCU instances
This chip has two identical LCU instances, LCU_0 and LCU_1.
62.2 Overview
LCU selects multiple inputs from timers, Pulse Width Modulation (PWM) signals, and Input/Output (I/O) pads, and combines them 
using a programmable logic function to create output waveforms.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2531 / 5251


---
# 페이지 223

62.2.1 Block diagram
LU_IN0
LU_IN1
l0_DFF[0]
O0_DFF[0]
To MUX....
-
-
O3_DFF[0]
O0[0]
-
-
O3[0]
int_req[0]
dma_req[0]
-
-
l3_DFF[0]
1
0
0
2
LU_IN2
3
LU_IN3
4
sync[0]
sync[n]
force[0]
-
-
force[n]
LU_IN4*n-1
4*n
int_req[2]
dma_req[2]
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
O0_DFF[0]
-
4*n + 1
M 
U 
X 
S 
E 
L 
0 
- 
11
-
-
-
O3_DFF[0]
4*n + 4
O0_DFF[1]
4*n + 5
-
-
-
-
-
-
-
-
-
-
-
-
O3_DFF[n]
8n
l0_DFF[n]
-
-
l3_DFF[n]
sync[0]
-
-
sync[n]
force[0]
-
-
force[n]
sync[0]
-
-
-
-
-
-
-
-
-
-
-
-
sync[n]
force[0]
-
-
force[n]
To I/O pads
To I/O pads
O0[n]
-
-
O3[n]
O0_DFF[n]
To MUX....
-
-
O3_DFF[n]
LC0
LCn
Figure 281. Block diagram
62.2.2 Features
• 3 LCs with programmable logic function for generating output results
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2532 / 5251


---
# 페이지 224

• 12 inputs to and 12 outputs from LCs
• Muxing to map any input to any LC
• Independent filters for the rising and falling output states of each LC
• Software override logic for inputs using multiple modes
• 3 force inputs with programmable edge filtering to force output states using multiple modes
• 2 sync inputs to control transition timing
• Lock bit to block writes to CFG[WP]
• Interrupt request generation based on output change or force event
• DMA transfer request generation based on output change or force event
62.3 Functional description
62.3.1 LC operation
62.3.1.1
Overview
An LC performs logic operations based on the LUT principle, as described in Logic operations.
Each LC supports the following features:
• Independent filter thresholds for the rising and falling output states support different transition delays.
• Bypass of the output state filter by setting the filter threshold to zero. Bypassing the filter causes the asynchronous signal 
to propagate to the output of the LC.
• Force logic that instantly switches an LC output to the inactive state upon external fault signal assertion. The return from 
the inactive state to the output state is either:
— Instantaneous: when LCU deasserts the force signal.
— Instantaneous synchronized: when LCU deasserts the force signal and then the sync input asserts.
— Manual: when you write 1 to the force status bit and then the LCU deasserts the force input.
— Manual synchronized: when you write 1 to the force status bit and LCU deasserts the force input, and then the sync 
input asserts.
• Input software override logic to override external inputs by writing to the following registers:
— LCn Sync Control (LCn_SCTRL[SW_MODE])
— Software Override Value (SWVALUE[SWVALUE])
— Software Override Enable (SWEN[SWEN])
• Generation of interrupt requests or DMA transfer requests.
62.3.1.2
LC diagram
This figure illustrates an example LC implementation with:
• One LC
• Four force inputs
• Two sync inputs
For the number of each resource in this chip, see Features.
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2533 / 5251


---
# 페이지 225

Lcu_clock
Q
Q
Q
0
0
M
U
X
S
E
L
0
1
I0_DFF[0]
I3_DFF[0]
O0_DFF[0]
2
3
4
5
6
7
8
MUXSEL0[MUXSEL]
Q
Lcu_clock
Q
Q
Q
0
1
0
1
Q
Q
Q
Q
Q
Q
Q
SWVALUE[0]
LC0_SCTRL[SW_SYNC_SEL]
To other LCs
sync[0]
sync[n]
l0
l1
l2
l3
force[0]
-
-
force[n]
0
1
0
1
0
1
2
3
LC0_LUTCTRL0[LUTCTRL]
LC0_SCTRL[SW_MODE]
Software override
LC0
LCU
SWEN[0]
SWOUT[0]
LC_INPUTS[0]
0
1
1
LC0_FILT0[LUT_RISE_FILT]
LC0_FILT0[LUT_FALL_FILT]
LC0_FCTRL[FORCE_MODE0]
0
0
1
1
2
1
3
LC0_FCTRL[SYNC_SEL0]
LC0STS[FORCESTS[0]]
Force deassertion
DMA and interrupt control
Force assertion
0
1
2
3
0
1
LCO_OUTPOL[0]
O0_DFF[0]
O0[0]
O3[0]
O3_DFF[0]
LCOUT[0]
LUT
block
Rise and fall
edge delay
OUTEN[0]
FORCEOUT[0]
To other LCs
Lcu_clock
To other LCs
int_req[0]
Q
Q
LC0_FFILT[FORCE_POL[0]]
Rise and fall
edge delay
Lcu_clock
0
1
LC0_FFILT[COMB_EN[0]]
0
1
LC0_FFILT[FORCE_FILT]
LC0_FCTRL[FORCE_SENSE0[0]]
0
0
1
LC0_INTDMAEN[FORCE_INT_EN[0]]
FORCEOUT[0]
0
0
1
LC0_INTDMAEN[LUT_INT_EN[0]]
LCOUT[0]
0
0
1
dma_req[0]
LC0_INTDMAEN[FORCE_DMA_EN[0]]
FORCEOUT[0]
0
0
1
LC0_INTDMAEN[LUT_DMA_EN[0]]
LCOUT[0]
0
0
1
-
-
-
-
-
-
-
-
Figure 282. LC diagram
62.3.1.3
Logic operations
An LC reads its set of inputs (inputs 3, 2, 1, and 0) as a four-bit binary value, with Input 3 as the most-significant bit and Input 0 
as the least-significant bit. For example, if:
Input 0 = 0
Input 1 = 1
Input 2 = 0
Input 3 = 1
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2534 / 5251


---
# 페이지 226

then the combined input value is 1010b (10 decimal).
Each possible four-bit input value corresponds to a bit position in the LUT Control (LCn_LUTCTRLm[LUTCTRL]), as illustrated in 
LC LUT. For a given LC output, if the combined LC input value corresponds to a bit position in that output's LUTCTRL value that 
equals 1, then the LC asserts that output.
For example, if you write 35h to LUTCTRL (shown in the Example column of the LC LUT), then the combined input values 0 
(0000b), 2 (0010b), 4 (0100b), and 5 (0101b) cause assertion of the output. All other input values cause deassertion of the output.
LCU processes each look-up table asynchronously.
62.3.1.4
LC LUT
The LUT maps the combined LC input value to a bit position in LCn_LUTCTRLm.
Table 358. LC LUT
Input 3
Input 2
Input 1
Input 0
LUTCTRL bit position
Example LUTCTRL value: 
35h
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
1
0
0
0
1
0
2
1
0
0
1
1
3
0
0
1
0
0
4
1
0
1
0
1
5
1
0
1
1
0
6
0
0
1
1
1
7
0
1
0
0
0
8
0
1
0
0
1
9
0
1
0
1
0
10
0
1
0
1
1
11
0
1
1
0
0
12
0
1
1
0
1
13
0
1
1
1
0
14
0
1
1
1
1
15
0
62.3.1.5
LC output filters
Each LC supports two optional digital filters, a Rise Filter (LCn_FLITm[LUT_RISE_FILT]) and a Fall Filter 
(LCn_FLITm[LUT_FALL_FILT]), to post-process the LUT output and delay the output signal change.
Each filter starts accumulating clock cycles on the occurrence of the associated LUT event. The Rise Filter counts from an output 
assertion, and the Fall Filter counts from an output deassertion. When the number of clock cycles reaches the filter threshold 
(matches the specified filter value), the output flips to the new state. For example, if you specify a Rise Filter value of 100h, and 
the LUT event triggers an output assertion, the output signal does not assert until the 256th clock cycle after the event.
A filter value of 0 bypasses the filter.
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2535 / 5251


---
# 페이지 227

 
LCU usecase (intercell/feedback loop path along with TRGMUX Path) does not work with default RISE/FALL filter 
time. You must configure RISE/FALL Filter delay at least for 1 cycle to avoid such glitches/failures.
  NOTE  
62.3.2 Behavior in different chip modes of operation
Table 359. Modes of operation
Operation mode
Status of outputs
Normal
• Controlled by LCn_LUTCTRLm and MUXSELn
• Toggled based on the states of the selected inputs
Debug
Inactive or normal operation controlled by Debug Mode 
Enable (DBGEN)
62.3.3 Clocking
This module has no clocking considerations.
62.3.4 Interrupts
Each LC has a single interrupt request output int_req[n]. Interrupt request enables bits for all the 4 outputs in each LC defined 
in LCn_INTDMAEN with LCn_INTDMAEN[FORCE_INT_EN] for interrupt request generation when a force event occurs and 
LCn_INTDMAEN[LUT_INT_EN] for interrupt request generation when a LUT event occurs.
When user enables interrupt for a force event on an output and the force event occurs on that output, LCU generates an 
interrupt request if LCn_STS[FORCESTS] and LCn_INTDMAEN[FORCE_INT_EN] for that output is 1. Similarly when user 
enables interrupt for a LUT event on an output and a LUT event occurs on that output, LCU generates an interrupt request if 
LCn_STS[LUT_STS] and LCn_INTDMAEN[LUT_INT_EN] for that output is 1.
62.3.5 DMA
Each LC has a single DMA request output dma_req[n]. DMA request enables bits for all the 4 outputs in each LC defined 
in LCn_INTDMAEN with LCn_INTDMAEN[FORCE_DMA_EN] for DMA request generation when a force event occurs and 
LCn_INTDMAEN[LUT_DMA_EN] for DMA request generation when a LUT event occurs.
When user enables DMA for a force event on an output and the force event occurs on that output, LCU generates a DMA request 
if LCn_STS[FORCESTS] and LCn_INTDMAEN[FORCE_DMA_EN] for that output is 1. Similarly when user enables DMA for 
a LUT event on an output and a LUT event occurs on that output, LCU generates a DMA request if LCn_STS[LUT_STS] and 
LCn_INTDMAEN[LUT_DMA_EN] for that output is 1.
62.4 External signals
This module has no external signals.
62.5 Initialization
This module does not require initialization.
62.6 Application information
62.6.1 Use-case examples
62.6.1.1
Two-channel multiplexer
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2536 / 5251


---
# 페이지 228

62.6.1.1.1
Overview
A multiplexer (or mux) takes multiple inputs and, based on some control mechanism, passes only one of those inputs to the output. 
You can implement a two-channel multiplexer controlled by an external signal or a software override using three inputs and one 
output of a single LC, as illustrated in Logic diagram and Implementation.
This example implementation controls the multiplexer with the SEL input signal and a software override. The software override 
controls the multiplexer output regardless of the SEL signal state. To use software override, you must enable it for the 
corresponding output (SWEN[SWEN]). You assert software override by writing 1 to the corresponding bit of the Software Override 
Value (SWVALUE[SWVALUE]).
62.6.1.1.2
Logic diagram
A
SEL
B
Y
SEL
Figure 283. Logic diagram
62.6.1.1.3
Implementation
I0
I1
O0
LC0
Path delays:
2 clocks
I2
OUTEN
SWEN
SWVALUE
SEL
A
B
Y
FILTx clocks
Figure 284. Implementation
62.6.1.1.4
Connections and controls
Table 360. Connections and controls
Name
Description
SEL
Input signal
A
B
OUTEN
Output enable
SWEN
Software override enable
SWVALUE
Software override
Y
Output signal
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2537 / 5251


---
# 페이지 229

62.6.1.1.5
Truth table
Table 361. Truth table
Inputs
Output
A
B
SEL
Y
0
0
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
1
0
1
0
0
1
0
0
0
1
1
1
1
1
0
1
1
1
1
1
62.6.1.1.6
Register configuration
Table 362. Register configuration
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL0
—
—
—
—
E4E4h
—
—
—
LUTCTRL1
—
—
—
—
—
0h
—
—
LUTCTRL2
—
—
—
—
—
—
0h
—
LUTCTRL3
—
—
—
—
—
—
—
0h
FILT0
—
—
—
—
0h
—
—
—
FILT1
—
—
—
—
—
0h
—
—
FILT2
—
—
—
—
—
—
0h
—
FILT3
—
—
—
—
—
—
—
0h
INTDMAEN
—
—
—
—
0h
OUTPOL
—
—
—
—
0h
FFILT
—
—
—
—
0h
FCTRL
—
—
—
—
0h
SCTRL
—
—
—
—
0h
MUXSEL0
—
—
—
1h
—
—
—
—
MUXSEL1
—
—
2h
—
—
—
—
—
MUXSEL2
—
3h
—
—
—
—
—
—
MUXSEL3
0h
—
—
—
—
—
—
—
SWEN
—
—
—
—
Disable software override for LC0 input 0: 0h
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2538 / 5251


---
# 페이지 230

Table 362. Register configuration (continued)
Register
I3
I2
I1
I0
O0
O1
O2
O3
Enable software override for LC0 input 0: 1h
SWVALUE
—
—
—
—
Deassert software override for LC0 input 0: 0h
Assert software override for LC0 input 0: 1h
OUTEN
—
—
—
—
1h
62.6.1.1.7
Waveforms
In this figure, the SWEN and SWVALUE signals represent the states of the software override control registers. Writes to SWEN 
and SWVALUE have immediate impact on LC outputs, whereas LC inputs require input synchronization to prevent metastability.
0
System clock
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
A
Y
B
Sel
OUTEN
SWEN
SWVALUE
Figure 285. Waveforms
62.6.1.2
Binary to Gray code converter
62.6.1.2.1
Overview
Gray code, also known as reflected binary code (RBC), is a non-weighted, minimum change code. In this code, any two adjacent 
code numbers differ by only one bit. This code solves the problem of physical switch transitions by changing only one switch at 
a time, so there is never any ambiguity of position.
You can implement binary to Gray code conversion using a single LC, as illustrated in Logic diagram and Implementation.
In this example, the LC also generates a DMA request on each rising edge of output 3, which is bit 0 of the Gray code (G0).
62.6.1.2.2
Conversion table
Table 363. Conversion table
Decimal
Binary
Gray
0
0000
0000
1
0001
0001
2
0010
0011
3
0011
0010
4
0100
0110
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2539 / 5251


---
# 페이지 231

Table 363. Conversion table (continued)
Decimal
Binary
Gray
5
0101
0111
6
0110
0101
7
0111
0100
8
1000
1100
9
1001
1101
10
1010
1111
11
1011
1110
12
1100
1010
13
1101
1011
14
1110
1001
15
1111
1000
62.6.1.2.3
Logic diagram
B0
B1
G0
B1
B2
G1
B2
B3
B3
G2
G3
Figure 286. Logic diagram
62.6.1.2.4
Implementation
B3
G0
B2
G1
B1
G2
B0
G3
I0
I1
I2
I3
O0
O1
O2
O3
LC0
Path delays:
2 clocks
Clock
FILTx clocks
Figure 287. Implementation
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2540 / 5251


---
# 페이지 232

62.6.1.2.5
Connections and controls
Table 364. Connections and controls
Name
Description
B0
Bit 0 of the input binary code
B1
Bit 1 of the input binary code
B2
Bit 2 of the input binary code
B3
Bit 3 of the input binary code
G0
Bit 0 of the output Gray code
G1
Bit 1 of the output Gray code
G2
Bit 2 of the output Gray code
G3
Bit 3 of the output Gray code
Clock
System clock input
62.6.1.2.6
Truth table
Table 365. Truth table
Inputs
Outputs
B3
B2
B1
B0
G3
G2
G1 
G0
0
0
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
1
0
0
1
0
0
0
1
1
0
0
1
1
0
0
1
0
0
1
0
0
0
1
1
0
0
1
0
1
0
1
1
1
0
1
1
0
0
1
0
1
0
1
1
1
0
1
0
0
1
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
1
1
1
0
1
1
0
1
0
1
1
1
1
1
0
1
1
1
1
1
0
1
1
0
0
1
0
1
0
1
1
0
1
1
0
1
1
1
1
1
0
1
0
0
1
1
1
1
1
1
0
0
0
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2541 / 5251


---
# 페이지 233

62.6.1.2.7
Register configuration
Table 366. Register configuration
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL0
—
—
—
—
FF00h
—
—
—
LUTCTRL1
—
—
—
—
—
FF0h
—
—
LUTCTRL2
—
—
—
—
—
—
3C3Ch
—
LUTCTRL3
—
—
—
—
—
—
—
6666h
FILT0
—
—
—
—
0h
—
—
—
FILT1
—
—
—
—
—
0h
—
—
FILT2
—
—
—
—
—
—
0h
—
FILT3
—
—
—
—
—
—
—
0h
INTDMAEN
—
—
—
—
800h
OUTPOL
—
—
—
—
0h
FFILT
—
—
—
—
0h
FCTRL
—
—
—
—
0h
SCTRL
—
—
—
—
0h
MUXSEL0h
—
—
—
01h
—
—
—
—
MUXSEL1
—
—
2h
—
—
—
—
—
MUXSEL2
—
3h
—
—
—
—
—
—
MUXSEL3
4h
—
—
—
—
—
—
—
SWEN
—
—
—
—
0h
SWVALUE
—
—
—
—
0h
OUTEN
—
—
—
—
Fh
62.6.1.2.8
Waveforms
The LC outputs are delayed by two clock cycles because of the two-stage input synchronizers.
0
System clock
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
B3
B0
Binary code
B1
G2
37 38 39 40 41 42 43 44 45 46 47 48 49
B2
G1
G3
G0
DMA request
OUTEN 0h
Fh
Gray code
Figure 288. Waveforms
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2542 / 5251


---
# 페이지 234

62.6.1.3
Manchester encoder and decoder
62.6.1.3.1
Overview
Manchester encoding (also known as phase encoding) is a data-modulation technique for binary data transfer based one of 
these signals:
• Analog
• RF
• Optical
• High-speed-digital
• Long-distance-digital
The fundamental idea behind Manchester encoding is to use voltage transitions, instead of voltage levels, to represent 1s and 0s. 
It performs an exclusive OR of data and clock signals to encode and decode data. A high-to-low transition on the falling clock edge 
indicates 0. A low-to-high transition on the rising clock edge indicates 1.
62.6.1.3.2
Logic diagram
Clock
Data
PE
Clock
PE
Data
Figure 289. Logic diagram
62.6.1.3.3
Implementation
Clock out
Data out
Decoder
PE
Clock
Clock in
Data in
I2
I3
O2
O3
LC0
Path delays:
2 clocks
System clock
FILTx+1 clock
FILTx clocks
I1
O1
I0
O0
Encoder
Figure 290. Implementation
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2543 / 5251


---
# 페이지 235

62.6.1.3.4
Connections and controls
Table 367. Connections and controls
Name
Description
Data in
Input signal
Clock in
PE
Manchester-encoded signal from LC
Clock
Auxiliary signal fed to the decoder to allow Manchester decoding
Data out
Output signal after Manchester decoding
System clock
Clock frequency supplied to LC
Clock out
Output signal
62.6.1.3.5
Truth table for encoder
Table 368. Truth table for encoder
Inputs
Output
Data in
Clock in
PE
0
0
0
0
1
1
1
0
1
1
1
0
62.6.1.3.6
Truth table for decoder
Table 369. Truth table for decoder
Inputs
Output
Clock
PE
Data out
0
0
0
0
1
1
1
0
1
1
1
0
62.6.1.3.7
Register configuration
Table 370. Register configuration
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL0
—
—
—
—
6666h
—
—
—
LUTCTRL1
—
—
—
—
—
AAAAh
—
—
LUTCTRL2
—
—
—
—
—
—
FF0h
—
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2544 / 5251


---
# 페이지 236

Table 370. Register configuration (continued)
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL3
—
—
—
—
—
—
—
FF00h
FILT0
—
—
—
—
0h
—
—
—
FILT1
—
—
—
—
—
0h
—
—
FILT2
—
—
—
—
—
—
0h
—
FILT3
—
—
—
—
—
—
—
0h
INTDMAEN
—
—
—
—
0h
OUTPOL
—
—
—
—
0h
FFILT
—
—
—
—
0h
FCTRL
—
—
—
—
0h
SCTRL
—
—
—
—
0h
MUXSEL0
—
—
—
1h
—
—
—
—
MUXSEL1
—
—
2h
—
—
—
—
—
MUXSEL2
—
5h
—
—
—
—
—
—
MUXSEL3
6h
—
—
—
—
—
—
—
SWEN
—
—
—
—
0h
SWVALUE
—
—
—
—
0h
OUTEN
—
—
—
—
Fh
62.6.1.3.8
Waveforms for encoder
This figure includes the Manchester-encoded waveform (labeled PE) of the input waveform (labeled "Data in"). The PE waveform 
is delayed by two clock cycles because of two-stage input synchronization.
0
System clock
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
Clock in
Clock
PE
Data in
OUTEN
0h
Fh
Figure 291. Waveforms for encoder
62.6.1.3.9
Waveforms for decoder
The output waveform (labeled "Data out") is delayed by four clock cycles from the input waveform (labeled "Data in") because of 
two-stage input synchronization. In this example, the Manchester encoder also propagates the Clock waveform that the decoder 
uses to reconstruct the "Data in" waveform from the Manchester-decoded waveform (labeled PE).
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2545 / 5251


---
# 페이지 237

0
System clock
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
PE
Clock out
Data out
Clock
OUTEN
0h
Fh
Figure 292. Waveforms for decoder
62.6.1.4
Adjustable PWM/FM generator
62.6.1.4.1
Overview
In many cases, it is useful to route an LC output back to one of its inputs, as illustrated in Implementation. In addition, you can 
delay outputs with a digital filter with different time constants for delaying rising and falling edges. Combining these capabilities, 
you can use an LC to generate output waveforms with adjustable pulse width and frequency.
In addition to waveform generation, the software-override feature forces the generator output low or high by software. You control 
the override via Software Override Enable (SWEN) and Software Override Value (SWVALUE).
62.6.1.4.2
Implementation
Path delays:
System clock
SYNC
OUT
FILTx+1 clock
FILTx clocks
I0
O0
LC0
Figure 293. Implementation
62.6.1.4.3
Connections and controls
Table 371. Connections and controls
Name
Description
I0
Delayed output routed back to LC input
O0 and OUT
Delayed output
System clock
Clock frequency supplied to LC
SYNC
Software override synchronization signal
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2546 / 5251


---
# 페이지 238

62.6.1.4.4
Truth table
This example generates an adjustable PWM/FM waveform according to the following table. In the table:
• OUT is the LC output signal that is also routed to the LC input using an internal multiplexer.
• TdH is the digital filter value to delay the rising edge of the output signal.
• TdL is the digital filter value to delay the falling edge of the output signal.
Table 372. Truth table
I0
OUT
0
1 delayed by TdH (see Output edge delays)
1
0 delayed by TdL (see Output edge delays)
62.6.1.4.5
Output edge delays
I0
OUT
TdH
TdL
Figure 294. Output edge delays
62.6.1.4.6
Register configuration
Table 373. Register configuration
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL0
—
—
—
—
1h
—
—
—
LUTCTRL1
—
—
—
—
—
0h
—
—
LUTCTRL2
—
—
—
—
—
—
0h
—
LUTCTRL3
—
—
—
—
—
—
—
0h
FILT0
—
—
—
—
1_0001h
—
—
—
FILT1
—
—
—
—
—
0h
—
—
FILT2
—
—
—
—
—
—
0h
—
FILT3
—
—
—
—
—
—
—
0h
INTDMAEN
—
—
—
—
0h
OUTPOL
—
—
—
—
0h
FFILT
—
—
—
—
0h
FCTRL
—
—
—
—
0h
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2547 / 5251


---
# 페이지 239

Table 373. Register configuration (continued)
Register
I3
I2
I1
I0
O0
O1
O2
O3
SCTRL
—
—
—
—
SWVALUE for input 0 changes immediately: 0h
SWVALUE for input 0 changes on rising edge of 
sync: 1h
MUXSEL0
—
—
—
5h
—
—
—
—
MUXSEL1
—
—
0h
—
—
—
—
—
MUXSEL2
—
0h
—
—
—
—
—
—
MUXSEL3
0h
—
—
—
—
—
—
—
SWEN
—
—
—
—
Disable software override: 0h
Enable software override: 1h
SWVALUE
—
—
—
—
Deassert software override: 0h
Assert software override: 1h
OUTEN
—
—
—
—
1h
62.6.1.4.7
Waveforms for immediate software override
In this figure, the SWEN and SWVALUE signals represent the states of the software override control registers. Writes to Software 
Override Enable (SWEN) and Software Override Value (SWVALUE) have immediate impact on LC outputs, whereas LC inputs 
require input synchronization to prevent metastability.
0
System clock
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
LUT_RISE_FILT
SWVALUE
SWEN
SYNC
37 38 39 40 41 42 43 44 45 46 47 48 49 50 51
OUT
OUTEN
LUT_FALL_FILT
1h
1h
3h
Figure 295. Waveforms for immediate software override
62.6.1.4.8
Waveforms for synced software override
In this example, software override control is synced with the rising edges of the SYNC waveform.
0
System clock
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
LUT_RISE_FILT
SWVALUE
SWEN
SYNC
37 38 39 40 41 42 43 44 45 46 47 48 49 50 51
OUT
OUTEN
LUT_FALL_FILT
1h
1h
3h
Figure 296. Waveforms for synced software override
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2548 / 5251


---
# 페이지 240

62.6.1.5
SR latch
62.6.1.5.1
Overview
An SR latch is the simplest bistable device and a fundamental component of data storage.
This example implementation uses one LC that includes an internal feedback path configured by the internal multiplexer, as 
illustrated in Implementation. Output Q responds to inputs S (set) and R (reset). It changes with a delay of two clock cycles—the 
time required for the S and R signal inputs to pass through the internal two-stage synchronizers. This example implementation 
bypasses the Q digital filter; therefore, the loop of Q back to the input experiences a delay of one clock cycle." See Waveforms.
62.6.1.5.2
Implementation
Path delays:
2 clocks
System clock
Q
FILTx+1 clock
FILTx clocks
I0
O0
LC0
I1
I2
S
R
Figure 297. Implementation
62.6.1.5.3
Connections and controls
Table 374. Connections and controls
Name
Description
S
Set input
R
Reset input
Q
Both an output signal and an input that feeds back to LC0
System clock
Clock frequency supplied to LC
62.6.1.5.4
Truth table
Table 375. Truth table
Inputs
Output
State
R
S
Q
Q
0
0
0
0
Latch
0
0
1
1
Latch
0
1
0
1
Set
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2549 / 5251


---
# 페이지 241

Table 375. Truth table (continued)
Inputs
Output
State
R
S
Q
Q
0
1
1
1
Set
1
0
0
0
Reset
1
0
1
0
Reset
1
1
0
0
Not allowed
1
1
1
0
62.6.1.5.5
Register configuration
Table 376. Register configuration
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL0
—
—
—
—
Eh
—
—
—
LUTCTRL1
—
—
—
—
—
0h
—
—
LUTCTRL2
—
—
—
—
—
—
0h
—
LUTCTRL3
—
—
—
—
—
—
—
0h
FILT0
—
—
—
—
0h
—
—
—
FILT1
—
—
—
—
—
0h
—
—
FILT2
—
—
—
—
—
—
0h
—
FILT3
—
—
—
—
—
—
—
0h
INTDMAEN
—
—
—
—
0h
OUTPOL
—
—
—
—
0h
FFILT
—
—
—
—
0h
FCTRL
—
—
—
—
0h
SCTRL
—
—
—
—
0h
MUXSEL0
—
—
—
5h
—
—
—
—
MUXSEL1
—
—
2h
—
—
—
—
—
MUXSEL2
—
3h
—
—
—
—
—
—
MUXSEL3
0h
—
—
—
—
—
—
—
SWEN
—
—
—
—
0h
SWVALUE
—
—
—
—
0h
OUTEN
—
—
—
—
1h
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2550 / 5251


---
# 페이지 242

62.6.1.5.6
Waveforms
0
System clock
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
S
Q
29
R
OUTEN
1h
Figure 298. Waveforms
62.6.1.6
D flip-flop
62.6.1.6.1
Overview
A D flip-flop stores and outputs whatever logic level is applied to its data terminal at the time its clock input goes high.
You can implement a D flip-flop element using an LC as illustrated in Implementation. On a clock rising edge, the LC either asserts 
or deasserts the Q output based on the D input.
The Q output and CLKO digital filters are bypassed. Therefore, the states of these variables are fed to inputs with a delay of one 
clock cycle. See Waveforms.
62.6.1.6.2
Implementation
CLK
CLKO
D
Q
I0
I1
I2
I3
O0
O1
O2
O3
LC0
Path delays:
2 clocks
FILTx+1 clock
FILTx clocks
System clock
Figure 299. Implementation
62.6.1.6.3
Connections and controls
Table 377. Connections and controls
Name
Description
D
Input signal
CLK
Input clock
Q
Output signal; holds the logic state of the last Q output
CLKO
Holds the logic state of the last CLK input
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2551 / 5251


---
# 페이지 243

62.6.1.6.4
Truth table
Table 378. Truth table
Inputs
Outputs
State
CLKO
Q
CLK
D
Q
CLKO
0
0
0
0
0
0
Hold
0
0
0
1
0
0
Hold
0
0
1
0
0
1
Reset
0
0
1
1
1
1
Set
0
1
0
0
1
0
Hold
0
1
0
1
1
0
Hold
0
1
1
0
0
1
Reset
0
1
1
1
1
1
Set
1
0
0
0
0
0
Hold
1
0
0
1
0
0
Hold
1
0
1
0
0
1
Hold
1
0
1
1
0
1
Hold
1
1
0
0
1
0
Hold
1
1
0
1
1
0
Hold
1
1
1
0
1
1
Hold
1
1
1
1
1
1
Hold
62.6.1.6.5
Register configuration
Table 379. Register configuration
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL0
—
—
—
—
F0B8h
—
—
—
LUTCTRL1
—
—
—
—
—
CCCCh
—
—
LUTCTRL2
—
—
—
—
—
—
0h
—
LUTCTRL3
—
—
—
—
—
—
—
0h
FILT0
—
—
—
—
0h
—
—
—
FILT1
—
—
—
—
—
0h
—
—
FILT2
—
—
—
—
—
—
0h
—
FILT3
—
—
—
—
—
—
—
0h
INTDMAEN
—
—
—
—
0h
OUTPOL
—
—
—
—
0h
FFILT
—
—
—
—
0h
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2552 / 5251


---
# 페이지 244

Table 379. Register configuration (continued)
Register
I3
I2
I1
I0
O0
O1
O2
O3
FCTRL
—
—
—
—
0h
SCTRL
—
—
—
—
0h
MUXSEL0
—
—
—
1h
—
—
—
—
MUXSEL1
—
—
2h
—
—
—
—
—
MUXSEL2
—
5h
—
—
—
—
—
—
MUXSEL3
6h
—
—
—
—
—
—
—
SWEN
—
—
—
—
0h
SWVALUE
—
—
—
—
0h
OUTEN
—
—
—
—
3h
62.6.1.6.6
Waveforms
0
System clock
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
D
Q
29
30
31
32
33
34
35
CLK
OUTEN
3h
Figure 300. Waveforms
62.6.1.7
JK flip-flop
62.6.1.7.1
Overview
A JK flip-flop is a gated SR latch (see SR latch) with an added clock input circuit that prevents the illegal or invalid output condition 
that can occur when both SR-latch inputs (S and R) are asserted.
Truth table for JK flip-flop presents the four possible input combinations for a JK flip-flop. All output changes occur at the clock 
rising edge.
You can create a JK flip-flop using two LCs, as illustrated in Implementation. The first LC detects rising edges of the CLK clock 
input (see Truth table for LC0). The second LC processes J and K inputs at every rising clock edge (see Truth table for LC1).
Output Q and CLKO digital filters are bypassed. Therefore, the states of these variables are fed to inputs with a delay of one clock 
cycle (see Waveforms).
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2553 / 5251


---
# 페이지 245

62.6.1.7.2
Implementation
Path delays:
2 clocks
System clock
FILTx+1 clock
FILTx clocks
K
J
Q
I0
I1
I2
I3
O0
O1
O2
O3
LC1
CLK
CLK0
EDGE
I0
I1
I2
I3
O0
O1
O2
O3
LC0
Figure 301. Implementation
62.6.1.7.3
Truth table for JK flip-flop
Table 380. Truth table for JK flip-flop
J
K
State
0
0
Hold
1
0
Set
0
1
Clear
1
1
Toggle
62.6.1.7.4
Truth table for LC0
Table 381. Truth table for LC0
Inputs
Outputs
State
CLKO
CLK
CLKO
EDGE
0
0
0
0
No edge
0
1
1
1
Edge detected
1
0
0
0
No edge
1
1
1
0
No edge
62.6.1.7.5
Truth table for LC1
Table 382. Truth table for LC1
Inputs
Output
State
EDGE
Q
J
K
Q
0
0
X
X
0
Hold
0
1
X
X
1
Hold
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2554 / 5251


---
# 페이지 246

Table 382. Truth table for LC1 (continued)
Inputs
Output
State
EDGE
Q
J
K
Q
1
0
0
0
0
Hold
1
1
0
0
1
Hold
1
X
1
0
1
Set
1
X
0
1
0
Clear
1
0
1
1
1
Toggle
1
1
1
1
0
Toggle
62.6.1.7.6
Register configuration for LC0
Table 383. Register configuration for LC0
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL0
—
—
—
—
Ah
—
—
—
LUTCTRL1
—
—
—
—
—
2h
—
—
LUTCTRL2
—
—
—
—
—
—
0h
—
LUTCTRL3
—
—
—
—
—
—
—
0h
FILT0
—
—
—
—
0h
—
—
—
FILT1
—
—
—
—
—
0h
—
—
FILT2
—
—
—
—
—
—
0h
—
FILT3
—
—
—
—
—
—
—
0h
INTDMAEN
—
—
—
—
0h
OUTPOL
—
—
—
—
0h
FFILT
—
—
—
—
0h
FCTRL
—
—
—
—
0h
SCTRL
—
—
—
—
0h
MUXSEL0
—
—
—
1h
—
—
—
—
MUXSEL1
—
—
9h
—
—
—
—
—
MUXSEL2
—
0h
—
—
—
—
—
—
MUXSEL3
0h
—
—
—
—
—
—
—
SWEN
—
—
—
—
0h
SWVALUE
—
—
—
—
0h
OUTEN
—
—
—
—
3h
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2555 / 5251


---
# 페이지 247

62.6.1.7.7
Register configuration for LC1
Table 384. Register configuration for LC1
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL0
—
—
—
—
3AF0h
—
—
—
LUTCTRL1
—
—
—
—
—
0h
—
—
LUTCTRL2
—
—
—
—
—
—
0h
—
LUTCTRL3
—
—
—
—
—
—
—
0h
FILT0
—
—
—
—
0h
—
—
—
FILT1
—
—
—
—
—
0h
—
—
FILT2
—
—
—
—
—
—
0h
—
FILT3
—
—
—
—
—
—
—
0h
INTDMAEN
—
—
—
—
0h
OUTPOL
—
—
—
—
0h
FFILT
—
—
—
—
0h
FCTRL
—
—
—
—
0h
SCTRL
—
—
—
—
0h
MUXSEL4
—
—
—
5h
—
—
—
—
MUXSEL5
—
—
6h
—
—
—
—
—
MUXSEL6
—
Dh
—
—
—
—
—
—
MUXSEL7
Ah
—
—
—
—
—
—
—
SWEN
—
—
—
—
0h
SWVALUE
—
—
—
—
0h
OUTEN
—
—
—
—
10h
62.6.1.7.8
Waveforms
0
System clock
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
CLK
K
LC0
LC1
J
Q
EDGE
OUTEN
EDGE
13h
Figure 302. Waveforms
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2556 / 5251


---
# 페이지 248

62.6.1.8
Incremental encoder
62.6.1.8.1
Overview
An incremental encoder provides A and B pulse outputs in the form of 90-degree shifted waveforms (see Outputs). The decoding 
circuit processes these waveforms to detect the rotor position and the direction of rotation.
This example implementation requires two LCs (see Implementation):
• LC0 provides pulse streams on CW or CCW output at every A and B signal edge. If the encoder rotation is CW (A signal 
leading), then pulses appear at the CW output. If the encoder rotation is CCW (B signal leading), then pulses appear at 
the CCW output. Two pulse counters accumulate these pulse streams to provide the actual absolute encoder position in 
the respective direction of rotation.
• LC1 then uses the LC0 outputs to detect the direction of the rotation.
62.6.1.8.2
Outputs
0
A
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
B
DIR
CW
CCW
Figure 303. Outputs
62.6.1.8.3
Implementation
Path delays:
2 clocks
System clock
FILTx+1 clock
FILTx clocks
CCW
DIR
CW
B 
A
DIR
PULSE
I0
I1
I2
I3
O0
O1
O2
O3
LC1
AO
BO
I0
I1
I2
I3
O0
O1
O2
O3
LC0
Figure 304. Implementation
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2557 / 5251


---
# 페이지 249

62.6.1.8.4
Truth table for pulse generation
Table 385. Truth table for pulse generation
Inputs
Outputs
BO
AO
B
A
AO
BO
CW
CCW
0
0
0
0
0
0
—
—
0
0
0
1
1
0
1
—
0
0
1
0
0
1
—
1
0
0
1
1
1
1
0
1
0
0
0
0
—
1
0
1
0
1
1
0
0
1
1
0
0
1
—
—
0
1
1
1
1
1
1
—
1
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
1
0
—
—
1
0
1
0
0
1
—
—
1
0
1
1
1
1
—
1
1
1
0
0
0
0
1
1
0
1
1
0
—
1
1
1
1
0
0
1
1
—
1
1
1
1
1
1
—
—
62.6.1.8.5
Truth table for decoding direction of rotation
In this table:
• DIR = 0 represents a CCW direction.
• DIR = 1 represents a CW direction.
Table 386. Truth table for decoding direction of rotation
Inputs
Output
DIR
CCW
CW
DIR
0
0
0
0
0
0
1
1
0
1
0
0
0
1
1
1
1
0
0
1
1
0
1
1
1
1
0
0
1
1
1
1
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2558 / 5251


---
# 페이지 250

62.6.1.8.6
Register configuration for LC0
Table 387. Register configuration for LC0
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL0
—
—
—
—
AAAAh
—
—
—
LUTCTRL1
—
—
—
—
—
CCCCh
—
—
LUTCTRL2
—
—
—
—
—
—
4182h
—
LUTCTRL3
—
—
—
—
—
—
—
2814h
FILT0
—
—
—
—
1_0001h
—
—
—
FILT1
—
—
—
—
—
1_0001h
—
—
FILT2
—
—
—
—
—
—
0h
—
FILT3
—
—
—
—
—
—
—
0h
INTDMAEN
—
—
—
—
0h
OUTPOL
—
—
—
—
0h
FFILT
—
—
—
—
0h
FCTRL
—
—
—
—
0h
SCTRL
—
—
—
—
0h
MUXSEL0
—
—
—
1h
—
—
—
—
MUXSEL1
—
—
2h
—
—
—
—
—
MUXSEL2
—
9h
—
—
—
—
—
—
MUXSEL3
Ah
—
—
—
—
—
—
—
SWEN
—
—
—
—
0h
SWVALUE
—
—
—
—
0h
OUTEN
—
—
—
—
Fh
62.6.1.8.7
Register configuration for LC1
Table 388. Register configuration for LC1
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL0
—
—
—
—
BAh
—
—
—
LUTCTRL1
—
—
—
—
—
0h
—
—
LUTCTRL2
—
—
—
—
—
—
0h
—
LUTCTRL3
—
—
—
—
—
—
—
0h
FILT0
—
—
—
—
0h
—
—
—
FILT1
—
—
—
—
—
0h
—
—
FILT2
—
—
—
—
—
—
0h
—
FILT3
—
—
—
—
—
—
—
0h
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2559 / 5251


---
# 페이지 251

Table 388. Register configuration for LC1 (continued)
Register
I3
I2
I1
I0
O0
O1
O2
O3
INTDMAEN
—
—
—
—
0h
OUTPOL
—
—
—
—
0h
FFILT
—
—
—
—
0h
FCTRL
—
—
—
—
0h
SCTRL
—
—
—
—
0h
MUXSEL4
—
—
—
Bh
—
—
—
—
MUXSEL5
—
—
Ch
—
—
—
—
—
MUXSEL6
—
Dh
—
—
—
—
—
—
MUXSEL7
0h
—
—
—
—
—
—
—
SWEN
—
—
—
—
0h
SWVALUE
—
—
—
—
0h
OUTEN
—
—
—
—
10h
62.6.1.8.8
Waveforms
0
System clock
1
2
3
4
5
6
7
8
9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36
B
A
CCW
PULSE
37 38 39 40 41 42 43 44 45 46 47 48 49 50 51
DIR
CW
OUTEN
1Fh
52 53 54 55 56 57
CW
CCW
Figure 305. Waveforms
62.6.1.9
AC motor PWM controller
62.6.1.9.1
Overview
Driving a three-phase AC motor requires dedicated PWMs to perform:
• Complementary signal generation
• Dead time insertion
• Fault-state assertion
• Manual or automatic fault recovery
LCU enhances basic timer functionality with the necessary complementary features available only on dedicated motor 
control PWMs.
Implementation for AC motor controller shows all input and output signals of LCU in a typical three-phase motor control application.
TdH is the time delay preceding each rising edge of the complementary PWM output signals. See Truth table for details.
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2560 / 5251


---
# 페이지 252

Fault signals are routed from analog comparators or external protection circuits to protect power switches against damage caused 
by overcurrent. Any active fault must immediately change all PWM outputs to the inactive state. Force logic causes PWM outputs 
to transition to the inactive state upon an external fault event. See Truth table for details.
The dead time is one clock cycle. On a fault event, both PWM outputs transition to the inactive state (logic 0). When the fault event 
deasserts, both PWM signals start operating according to FORCE_MODE = 00 (cleared on force deassertion). See Waveforms 
for force cleared on force deassertion for details.
62.6.1.9.2
Implementation for AC motor controller
TMR2
TMR1
TMR0
PWMA_T
PWMA_B
PWMB_T
PWMB_B
PWMC_T
PWMC_B
LCU
LC0
LC1
Path delays:
2 clocks
FILTx clocks
System clock
FAULT0
SYNC
FAULT1
FAULT2
Figure 306. Implementation for AC motor controller
62.6.1.9.3
Implementation for controlling one phase of AC motor controller
I0
O0
LC0
Path delays:
2 clocks
System clock
FAULT
SYNC
TMR0
PWMA_T
O1
PWMA_B
FILTx clocks
Figure 307. Implementation for controlling one phase of AC motor controller
62.6.1.9.4
Connections and controls
Table 389. Connections and controls
Name
Description
TMRn
Synchronized timer input signals
System clock
Clock supplied to the LC
FAULTn
Fault signal (see Overview)
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2561 / 5251


---
# 페이지 253

Table 389. Connections and controls (continued)
Name
Description
SYNC
Sync signal for optional automatic fault recovery
PWMx_T
PWM output signal for controlling top power switch
PWMx_B
PWM output signal for controlling bottom power switch
62.6.1.9.5
Truth table
Table 390. Truth table
Input
Outputs
TMR0
PWMA_T
PWMB_B
0
0
1 delayed by TdH (see Output edge delays)
1
1 delayed by TdH (see Output edge delays)
0
62.6.1.9.6
Register configuration
Table 391. Register configuration
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL0
—
—
—
—
2h
—
—
—
LUTCTRL1
—
—
—
—
—
1h
—
—
LUTCTRL2
—
—
—
—
—
—
0h
—
LUTCTRL3
—
—
—
—
—
—
—
0h
FILT0
—
—
—
—
1_0000h
—
—
—
FILT1
—
—
—
—
—
1_0000h
—
—
FILT2
—
—
—
—
—
—
0h
—
FILT3
—
—
—
—
—
—
—
0h
INTDMAEN
—
—
—
—
0h
OUTPOL
—
—
—
—
0h
FFILT
—
—
—
—
100_0000h
FCTRL
—
—
—
—
0h
SCTRL
—
—
—
—
Software sync on rising edge for inputs 2 and 0, 
immediate for 3 and 1: 101h
Software sync on rising edge for all four inputs: 1111h
MUXSEL0
—
—
—
01h
—
—
—
—
MUXSEL1
—
—
0h
—
—
—
—
—
MUXSEL2
—
0h
—
—
—
—
—
—
MUXSEL3
0h
—
—
—
—
—
—
—
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2562 / 5251


---
# 페이지 254

Table 391. Register configuration (continued)
Register
I3
I2
I1
I0
O0
O1
O2
O3
SWEN
—
—
—
—
0h
SWVALUE
—
—
—
—
0h
OUTEN
—
—
—
—
3h
62.6.1.9.7
Waveforms for force cleared on force deassertion
This example shows two behaviors, depending on the Force Clearing mode (LC0_FCTRL[FORCE_MODE0]).
00b - Both PWM signals start normal operation when the fault event deasserts. See Waveforms for force cleared on 
force deassertion for details.
01b - Both PWM signals start normal operation on rising sync after the fault event deasserts. See Waveforms for force 
cleared on rising sync after force deassertion for details.
0
System clock
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
TMR
PWM_B
FAULT
SYNC
OUTEN
PWM_T
38
Figure 308. Waveforms for force cleared on force deassertion
62.6.1.9.8
Waveforms for force cleared on rising sync after force deassertion
0
System clock
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
TMR
PWM_B
FAULT
SYNC
OUTEN
PWM_T
38
Figure 309. Waveforms for force cleared on rising sync after force deassertion
62.6.1.10
AC motor double-switching controller
62.6.1.10.1
Overview
The simplest method of obtaining motor winding currents is to measure the current in each phase by placing a shunt resistor in 
two or three inverter legs (phases).
This example implementation of an AC motor drive for low-cost and high-volume applications uses a single shunt on the DC 
bus return path, as illustrated in AC motor power stage schematic. LCU supports double-switching by XORing two timer channel 
outputs. The implementation uses two LCs arranged to perform double switching, dead time generation, and the processing of 
three external fault signals.
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2563 / 5251


---
# 페이지 255

62.6.1.10.2
Double-switching
The double-switching technique requires:
• Six synchronized timer pulses
• Three fault signals
• Six PWM outputs for controlling top and bottom power switches
• A sync signal for automatic fault recovery
Waveforms for double-switching technique example applies the PWM switching cycle to an AC motor to reconstruct currents 
in three phases using a single DC bus shunt resistor (RSH). It applies the non-zero switching vectors 100, 110, and 101 to the 
power switches, which sample currents IA[0], -IC[0], -IC[1], and IA[1]. Because the durations (T1) of active vectors 110 and 101 
are the same, it also applies the zero switching vector (000) with durations T2 and T3 in the middle of the switching cycle to 
allow phase current reconstruction. This technique can only be used by PWM modules targeted at motor control and power 
conversion applications.
62.6.1.10.3
Fault inputs and deadtime insertion
Fault signals are routed from analog comparators or external protection circuits to protect power switches against damage caused 
by overcurrent. You must program the Combinational Force Path (LCn_FFILT[COMB_EN]) to enable an active fault input to 
immediately force all PWM outputs to the inactive state.
62.6.1.10.4
Deadtime insertion
In Waveforms for generation of PWM complementary signals using an LC, the PWMA_T output is generated by XORing timer 
outputs TMR0 and TMR1. The PWMA_B output is complementary to PWMA_T. Digital filters insert a dead time of one system 
clock cycle to delay the rising edges of both PWM signals.
62.6.1.10.5
Fault events
Waveforms for force cleared on force deassertion shows the reaction to the fault event. On a fault event, both the PWM 
outputs transition to the inactive state (logic 0). When fault event deasserts, both the PWM signals start operating according to 
FORCE_MODE = 00 (cleared on force deassertion).
Alternatively, after the fault event deasserts, fault clearing can be performed according to FORCE_MODE = 01 (cleared on rising 
sync force deassertion). See Waveforms for force cleared on rising sync after force deassertion for details.
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2564 / 5251


---
# 페이지 256

62.6.1.10.6
AC motor power stage schematic
PWMA_B
PWMA_T
RSH
CDC
IA
PWMB_B
PWMB_T
IB
IDC
PWMC_T
PWMC_B
AC motor
Phase B
Phase A
Phase C
IC
Figure 310. AC motor power stage schematic
62.6.1.10.7
Waveforms for double-switching technique example
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
Lcu_clk
UA
UB
UC
PWMA_T
PWMA_B
PWMB_T
PWMB_B
PWMC_T
PWMC_B
IA
IA[0]
IA[1]
IB
IC
-IC[0]
-IC[1]
IA
(IA[0]+IA[1])/2
IA=
IB
IB=-IA-IC
IC
(IC[0]+IC[1])/2
IC=
T1
T2
T1
T3
T3
Sample IA[0]
Sample IA[0]
Sample -IC[0]
Sample -IC[1]
i
j
k
l
g
h
a
b
c
d
e
f
m
n
o
p
Phase voltages
Power switches
ADC sampling
Computing
Figure 311. Waveforms for double-switching technique example
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2565 / 5251


---
# 페이지 257

62.6.1.10.8
Implementation for AC motor double-switching controller
TMR2
TMR1
TMR0
TMR5
TMR4
TMR3
PWMA_T
PWMA_B
PWMB_T
PWMB_B
PWMC_T
PWMC_B
LCU
LC0
LC1
Path delays:
2 clocks
FILTx clocks
System clock
FAULT0
SYNC
FAULT1
FAULT2
Figure 312. Implementation for AC motor double-switching controller
62.6.1.10.9
Implementation for controlling one phase
O0
LC0
Path delays:
2 clocks
System clock
FAULT
SYNC
TMR0
TMR1
PWMA_T
O1
I0
I1
PWMA_B
FILTx clocks
Figure 313. Implementation for controlling one phase
62.6.1.10.10
Connections and controls
Table 392. Connections and controls
Name
Description
TMRn
Synchronized timer input signals
System clock
Clock supplied to the LC
FAULTn
Fault signal (see Implementation for AC motor double-
switching controller for more details)
SYNC
Sync signal for optional automatic fault recovery
PWMx_T
PWM output signal for controlling top power switch
PWMx_B
PWM output signal for controlling bottom power switch
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2566 / 5251


---
# 페이지 258

62.6.1.10.11
Truth table
Table 393. Truth table
Inputs
Outputs
TMR1
TMR0
PWMA_T
PWMB_B
0
0
0
1 delayed by TdH (see Output edge delays)
0
1
1 delayed by TdH (see Output edge delays)
0
1
0
1 delayed by TdH (see Output edge delays)
0
1
1
0
1 delayed by TdH (see Output edge delays)
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
1
1
0
0
62.6.1.10.12
Register configuration
Table 394. Register configuration
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL0
—
—
—
—
6h
—
—
—
LUTCTRL1
—
—
—
—
—
9h
—
—
LUTCTRL2
—
—
—
—
—
—
0h
—
LUTCTRL3
—
—
—
—
—
—
—
0h
FILT0
—
—
—
—
1_0000h
—
—
—
FILT1
—
—
—
—
—
1_0000h
—
—
FILT2
—
—
—
—
—
—
0h
—
FILT3
—
—
—
—
—
—
—
0h
INTDMAEN
—
—
—
—
0h
OUTPOL
—
—
—
—
0h
FFILT
—
—
—
—
100_0000h
FCTRL
—
—
—
—
Force inputs 2 and 0 affect output 0, but force inputs 3 
and 1 do not affect output 0: 101h
All four inputs affect output 0: 1111h
SCTRL
—
—
—
—
0h
MUXSEL0
—
—
—
1h
—
—
—
—
MUXSEL1
—
—
2h
—
—
—
—
—
MUXSEL2
—
0h
—
—
—
—
—
—
MUXSEL3
0h
—
—
—
—
—
—
—
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2567 / 5251


---
# 페이지 259

Table 394. Register configuration (continued)
Register
I3
I2
I1
I0
O0
O1
O2
O3
SWEN
—
—
—
—
0h
SWVALUE
—
—
—
—
0h
OUTEN
—
—
—
—
3h
62.6.1.10.13
Waveforms for generation of PWM complementary signals using an LC
0
System clock
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
SYNC
PWMA_B
TMR0
TMR1
FAULT
OUTEN
PWMA_T
38
39
Figure 314. Waveforms for generation of PWM complementary signals using an LC
62.6.1.10.14
Waveforms for force cleared on force deassertion
0
System clock
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
SYNC
PWMA_B
TMR0
TMR1
FAULT
OUTEN
PWMA_T
38
39
Figure 315. Waveforms for force cleared on force deassertion
62.6.1.10.15
Waveforms for force cleared on rising sync after force deassertion
0
System clock
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
SYNC
PWMA_B
TMR0
TMR1
FAULT
OUTEN
PWMA_T
38
39
Figure 316. Waveforms for force cleared on rising sync after force deassertion
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2568 / 5251


---
# 페이지 260

62.6.1.11
Brushless DC (BLDC) motor PWM controller
62.6.1.11.1
Overview
You can use LCU to replace the mechanical commutator in the BLDC motor control application with Hall-sensor 
position measurement.
In this example implementation, LC0 receives the direction (DIR) and Hall A, Hall B, and Hall C sensor output states, and from 
those inputs generates the switching states S1, S2, and S3. LC1 and LC2 convert the switching states to PWM or on-off signals 
for controlling power switches, as illustrated in Waveforms for BLDC motor control technique.
BLDC motor power stage schematic and BLDC motor electrical arrangement illustrate a three-phase BLDC motor power stage 
with switching pulses and phase currents controlling motor rotation in the CCW direction. The state of the Hall sensors is 010. As 
the rotor shaft rotates, Hall sensors track the motor position. You accelerate or decelerate the motor by controlling the width of the 
PWM signal. You can include one or more faults (force inputs) to force power switches instantaneously into the inactive state if 
there is an overcurrent.
62.6.1.11.2
Implementation
Path delays:
2 clocks
System clock
FILTx+1 clock
FILTx clocks
Fault
S2
S3
S1
S1
S2
S3
Q3H
Q1H
Q1L
Q3L
Q2H
Q2L
HALL A
PWM
HALL B
HALL C
DIR
I0
I1
I2
I3
O0
O1
O2
O3
LC2
I0
I1
I2
I3
O0
O1
O2
O3
LC0
I0
I1
I2
I3
O0
O1
O2
O3
LC1
Figure 317. Implementation
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2569 / 5251


---
# 페이지 261

62.6.1.11.3
BLDC motor power stage schematic
A
B
Hall A
C
Hall B
Hall C
Q1L
Q1H
CDC
Q2L
IDC
Q3H
Q2H
Q3L
BLDC motor
IA
IC
Figure 318. BLDC motor power stage schematic
62.6.1.11.4
BLDC motor electrical arrangement
180°
0° = 360°
120°
60°
A
B
100
101
110
010
010
240°
300°
Hall A
C
001
Hall B
Hall C
Figure 319. BLDC motor electrical arrangement
62.6.1.11.5
Waveforms for BLDC motor control technique
This figure illustrates the basic waveforms for controlling a BLDC motor with stator windings and Hall sensors arranged according 
to BLDC motor electrical arrangement. Configure the external hardware (motor or sensor) so that it can produce these waveforms; 
then you can configure LCU.
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2570 / 5251


---
# 페이지 262

Hall A
Hall B
Hall C
Hall states
Direction [DIR]
Phases [ABC]
Q1H
Q1L
Q2H
Q2L
Q3H
Q3L
Direction [DIR]
Phases [ABC]
Q1H
Q1L
Q2H
Q2L
Q3H
Q3L
0
30
60
90
120
150
180
210
240
270
300
330
110
100
101
001
011
010
360
−+NC
NC+−
+NC−
+−NC
NC−+
−NC+
+−NC
NC−+
−NC+
−+NC
NC+−
+NC−
ON
OFF
OFF
OFF
OFF
ON
OFF
OFF
OFF
OFF
OFF
OFF
OFF
ON
ON
OFF
OFF
OFF
OFF
OFF
OFF
ON
ON
OFF
OFF
OFF
OFF
OFF
OFF
OFF
OFF
OFF
ON
ON
OFF
OFF
OFF
OFF
OFF
OFF
OFF
OFF
OFF
OFF
ON
ON
OFF
OFF
OFF
OFF
ON
ON
OFF
OFF
OFF
OFF
OFF
OFF
OFF
OFF
Hall sensors
CW direction [360→0]
CCW direction [0→360]
Figure 320. Waveforms for BLDC motor control technique
62.6.1.11.6
Connections and controls
Table 395. Connections and controls
Input-output group
Name
Description
LC0 inputs
HALL A
Hall sensor A output state
HALL B
Hall sensor B output state
HALL C
Hall sensor C output state
DIR
Direction of shaft rotation, as illustrated in Waveforms for reversing BLDC 
motor.
LC1 and LC2 inputs
S1
Switching state 1 (output 0 from LC0)
S2
Switching state 2 (output 1 from LC0)
S2
Switching state 3 (output 2 from LC0)
PWM
Output from PWM
LC0, LC1, and LC2 inputs
Clock
LCU clock input
Fault
Optional fault input
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2571 / 5251


---
# 페이지 263

Table 395. Connections and controls (continued)
Input-output group
Name
Description
LC1 outputs
Q1H
Motor control switch outputs, as illustrated in BLDC motor electrical 
arrangement
Q1L
Q2H
Q2L
LC2 outputs
Q3H
Q3L
62.6.1.11.7
Truth table for generating switching states
This table includes all Hall sensor states, even those that never occur because of sensor displacement by 120°.
Table 396. Truth table for generating switching states
Inputs
Outputs
Comments
DIR
Hall C
Hall B
Hall A
S1
S2
S3
0
0
0
0
0
0
0
Not used
0
0
0
1
1
0
0
Hall states
0
0
1
0
0
1
0
Hall states
0
0
1
1
1
1
0
Hall states
0
1
0
0
0
0
1
Hall states
0
1
0
1
1
0
1
Hall states
0
1
1
0
0
1
1
Hall states
0
1
1
1
0
0
0
Not used
1
0
0
0
0
0
0
Not used
1
0
0
1
0
1
1
Complement of Hall states
1
0
1
0
1
0
1
Complement of Hall states
1
0
1
1
0
0
1
Complement of Hall states
1
1
0
0
1
1
0
Complement of Hall states
1
1
0
1
0
1
0
Complement of Hall states
1
1
1
0
1
0
0
Complement of Hall states
1
1
1
1
0
0
0
Not used
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2572 / 5251


---
# 페이지 264

62.6.1.11.8
Truth table for generating switching pulses for phases A and B
Table 397. Truth table for generating switching pulses for phases A and B
Inputs
Outputs
Comments
PWM
S3
S2
S1
Q1H
Q1L
Q2H
Q2L
0
0
0
0
0
0
0
0
Not used
0
0
0
1
0
0
0
0
—
0
0
1
0
0
1
0
0
—
0
0
1
1
0
1
0
0
—
0
1
0
0
0
0
0
1
—
0
1
0
1
0
0
0
0
—
0
1
1
0
0
0
0
1
—
0
1
1
1
0
0
0
0
Not used
1
0
0
0
0
0
0
0
Not used
1
0
0
1
0
0
1
0
—
1
0
1
0
0
1
0
0
—
1
0
1
1
0
1
1
0
—
1
1
0
0
1
0
0
1
—
1
1
0
1
1
0
0
0
—
1
1
1
0
0
0
0
1
—
1
1
1
1
0
0
0
0
Not used
62.6.1.11.9
Truth table for generating switching pulses for phase C
Table 398. Truth table for generating switching pulses for phase C
Inputs
Outputs
Comments
PWM
S3
S2
S1
Q3H
Q3L
0
0
0
0
0
0
Not used
0
0
0
1
0
1
—
0
0
1
0
0
0
—
0
0
1
1
0
0
—
0
1
0
0
0
0
—
0
1
0
1
0
1
—
0
1
1
0
0
0
—
0
1
1
1
0
0
Not used
1
0
0
0
0
0
Not used
1
0
0
1
0
1
—
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2573 / 5251


---
# 페이지 265

Table 398. Truth table for generating switching pulses for phase C (continued)
Inputs
Outputs
Comments
PWM
S3
S2
S1
Q3H
Q3L
1
0
1
0
1
0
—
1
0
1
1
0
0
—
1
1
0
0
0
0
—
1
1
0
1
0
1
—
1
1
1
0
1
0
—
1
1
1
1
0
0
Not used
62.6.1.11.10
Configuration for generating switching states
Table 399. Configuration for generating switching states
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL0
—
—
—
—
542Ah
—
—
—
LUTCTRL1
—
—
—
—
—
324Ch
—
—
LUTCTRL2
—
—
—
—
—
—
E70h
—
LUTCTRL3
—
—
—
—
—
—
—
0h
FILT0
—
—
—
—
0h
—
—
—
FILT1
—
—
—
—
—
0h
—
—
FILT2
—
—
—
—
—
—
0h
—
FILT3
—
—
—
—
—
—
—
0h
INTDMAEN
—
—
—
—
0h
OUTPOL
—
—
—
—
0h
FFILT
—
—
—
—
0h
FCTRL
—
—
—
—
0h
SCTRL
—
—
—
—
0h
MUXSEL0
—
—
—
1h
—
—
—
—
MUXSEL1
—
—
2h
—
—
—
—
—
MUXSEL2
—
3h
—
—
—
—
—
—
MUXSEL3
4h
—
—
—
—
—
—
—
SWEN
—
—
—
—
0h
SWVALUE
—
—
—
—
0h
OUTEN
—
—
—
—
7h
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2574 / 5251


---
# 페이지 266

62.6.1.11.11
Configuration for switching pulses for phases A and B
Table 400. Configuration for switching pulses for phases A and B
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL0
—
—
—
—
3000h
—
—
—
LUTCTRL1
—
—
—
—
—
C0Ch
—
—
LUTCTRL2
—
—
—
—
—
—
A00h
—
LUTCTRL3
—
—
—
—
—
—
—
5050h
FILT0
—
—
—
—
0h
—
—
—
FILT1
—
—
—
—
—
0h
—
—
FILT2
—
—
—
—
—
—
0h
—
FILT3
—
—
—
—
—
—
—
0h
INTDMAEN
—
—
—
—
0h
OUTPOL
—
—
—
—
0h
FFILT
—
—
—
—
F00_0000h
FCTRL
—
—
—
—
101_0101h
SCTRL
—
—
—
—
0h
MUXSEL4
—
—
—
Dh
—
—
—
—
MUXSEL5
—
—
Eh
—
—
—
—
—
MUXSEL6
—
Fh
—
—
—
—
—
—
MUXSEL7
8h
—
—
—
—
—
—
—
SWEN
—
—
—
—
0h
SWVALUE
—
—
—
—
0h
OUTEN
—
—
—
—
F0h
62.6.1.11.12
Configuration for switching pulses for phase C
Table 401. Configuration for switching pulses for phase C
Register
I3
I2
I1
I0
O0
O1
O2
O3
LUTCTRL0
—
—
—
—
4400h
—
—
—
LUTCTRL1
—
—
—
—
—
2222h
—
—
LUTCTRL2
—
—
—
—
—
—
0h
—
LUTCTRL3
—
—
—
—
—
—
—
0h
FILT0
—
—
—
—
0h
—
—
—
FILT1
—
—
—
—
—
0h
—
—
FILT2
—
—
—
—
—
—
0h
—
FILT3
—
—
—
—
—
—
—
0h
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2575 / 5251


---
# 페이지 267

Table 401. Configuration for switching pulses for phase C (continued)
Register
I3
I2
I1
I0
O0
O1
O2
O3
INTDMAEN
—
—
—
—
0h
OUTPOL
—
—
—
—
0h
FFILT
—
—
—
—
0300_0000h
FCTRL
—
—
—
—
101h
SCTRL
—
—
—
—
0h
MUXSEL8
—
—
—
Dh
—
—
—
—
MUXSEL9
—
—
Eh
—
—
—
—
—
MUXSEL10
—
Fh
—
—
—
—
—
—
MUXSEL11
8h
—
—
—
—
—
—
—
SWEN
—
—
—
—
0h
SWVALUE
—
—
—
—
0h
OUTEN
—
—
—
—
300h
62.6.1.11.13
Waveforms for reversing BLDC motor
This figure illustrates the waveforms for controlling a reversing BLDC motor. The DIR input indicates the direction of rotation:
• Logic 0 for CW rotation
• Logic 1 for CCW rotation
System clock
PWM
FAULT
Hall A
Hall B
Hall C
DIR
Hall States
Inputs
3F7h
00h
Q1H
Q1L
Q2H
S
Q2L
Q3H
Q3L
OUTEN
010b
100b
110b
010b
011b
001b
110b
100b
101b
001b
011b
010b
011b
101b
001b
100b
110b
100b
101b
001b
011b
010b
Outputs
Figure 321. Waveforms for reversing BLDC motor
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2576 / 5251


---
# 페이지 268

62.6.1.11.14
Waveforms for reversing BLDC motor with fault assertion
This figure illustrates the waveforms for the reaction to an external fault in addition to reversing the BLDC motor. On the occurrence 
of an external fault event, the power switches transition to the inactive state (logic 0). Two clock cycles after external fault 
deassertion, the power switches start operating normally.
Switching state outputs S1, S2, and S3, generated by LC0, receive an additional delay of one clock cycle on their way to the inputs 
of other LCs (digital filters bypassed).
System clock
PWM
FAULT
Hall A
Hall B
Hall C
DIR
Hall States
Inputs
3F7h
00h
Q1H
Q1L
Q2H
S
Q2L
Q3H
Q3L
OUTEN
010b
100b
110b
010b
011b
001b
110b
100b
101b
001b
011b
010b
011b
101b
001b
100b
110b
100b
101b
001b
011b
010b
Outputs
Figure 322. Waveforms for reversing BLDC motor with fault assertion
62.7 Mapping of 12-bit input, output, and state fields
This table maps inputs, outputs, or states to the bit positions in the following 12-bit fields:
• SWEN[SWEN]
• SWVALUE[SWVALUE]
• OUTEN[OUTEN]
• LCIN[LC_INPUTS]
• SWOUT[SWOUT]
• LCOUT[LCOUT]
• FORCEOUT[FORCEOUT]
• FORCESTS[FORCESTS]
• DBGEN[DBGEN]
LC
Input, output, or state
Bit
0
0
0
1
1
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2577 / 5251


---
# 페이지 269

Table continued from the previous page...
LC
Input, output, or state
Bit
2
2
3
3
1
0
4
1
5
2
6
3
7
2
0
8
1
9
2
10
3
11
62.8 LCU register descriptions
 
Access to address offset 2A4h does not generate a transfer error.
  NOTE  
62.8.1 LCU memory map
LCU_0 base address: 4009_8000h
LCU_1 base address: 4009_C000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
LC 0 Output 0 LUT Control (LC0_LUTCTRL0)
32
RW
0000_0000h
4h
LC 0 Output 1 LUT Control (LC0_LUTCTRL1)
32
RW
0000_0000h
8h
LC 0 Output 2 LUT Control (LC0_LUTCTRL2)
32
RW
0000_0000h
Ch
LC 0 Output 3 LUT Control (LC0_LUTCTRL3)
32
RW
0000_0000h
10h
LC 0 Output 0 Filter (LC0_FILT0)
32
RW
0000_0000h
14h
LC 0 Output 1 Filter (LC0_FILT1)
32
RW
0000_0000h
18h
LC 0 Output 2 Filter (LC0_FILT2)
32
RW
0000_0000h
1Ch
LC 0 Output 3 Filter (LC0_FILT3)
32
RW
0000_0000h
20h
LC 0 Interrupt and DMA Enable (LC0_INTDMAEN)
32
RW
0000_0000h
24h
LC 0 Status (LC0_STS)
32
RW
0000_0000h
28h
LC 0 Output Polarity Control (LC0_OUTPOL)
32
RW
0000_0000h
2Ch
LC 0 Force Filter (LC0_FFILT)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2578 / 5251


---
# 페이지 270

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
30h
LC 0 Force Control (LC0_FCTRL)
32
RW
0000_0000h
34h
LC 0 Sync Control (LC0_SCTRL)
32
RW
0000_0000h
40h
LC 1 Output 0 LUT Control (LC1_LUTCTRL0)
32
RW
0000_0000h
44h
LC 1 Output 1 LUT Control (LC1_LUTCTRL1)
32
RW
0000_0000h
48h
LC 1 Output 2 LUT Control (LC1_LUTCTRL2)
32
RW
0000_0000h
4Ch
LC 1 Output 3 LUT Control (LC1_LUTCTRL3)
32
RW
0000_0000h
50h
LC 1 Output 0 Filter (LC1_FILT0)
32
RW
0000_0000h
54h
LC 1 Output 1 Filter (LC1_FILT1)
32
RW
0000_0000h
58h
LC 1 Output 2 Filter (LC1_FILT2)
32
RW
0000_0000h
5Ch
LC 1 Output 3 Filter (LC1_FILT3)
32
RW
0000_0000h
60h
LC 1 Interrupt and DMA Enable (LC1_INTDMAEN)
32
RW
0000_0000h
64h
LC 1 Status (LC1_STS)
32
RW
0000_0000h
68h
LC 1 Output Polarity Control (LC1_OUTPOL)
32
RW
0000_0000h
6Ch
LC 1 Force Filter (LC1_FFILT)
32
RW
0000_0000h
70h
LC 1 Force Control (LC1_FCTRL)
32
RW
0000_0000h
74h
LC 1 Sync Control (LC1_SCTRL)
32
RW
0000_0000h
80h
LC 2 Output 0 LUT Control (LC2_LUTCTRL0)
32
RW
0000_0000h
84h
LC 2 Output 1 LUT Control (LC2_LUTCTRL1)
32
RW
0000_0000h
88h
LC 2 Output 2 LUT Control (LC2_LUTCTRL2)
32
RW
0000_0000h
8Ch
LC 2 Output 3 LUT Control (LC2_LUTCTRL3)
32
RW
0000_0000h
90h
LC 2 Output 0 Filter (LC2_FILT0)
32
RW
0000_0000h
94h
LC 2 Output 1 Filter (LC2_FILT1)
32
RW
0000_0000h
98h
LC 2 Output 2 Filter (LC2_FILT2)
32
RW
0000_0000h
9Ch
LC 2 Output 3 Filter (LC2_FILT3)
32
RW
0000_0000h
A0h
LC 2 Interrupt and DMA Enable (LC2_INTDMAEN)
32
RW
0000_0000h
A4h
LC 2 Status (LC2_STS)
32
RW
0000_0000h
A8h
LC 2 Output Polarity Control (LC2_OUTPOL)
32
RW
0000_0000h
ACh
LC 2 Force Filter (LC2_FFILT)
32
RW
0000_0000h
B0h
LC 2 Force Control (LC2_FCTRL)
32
RW
0000_0000h
B4h
LC 2 Sync Control (LC2_SCTRL)
32
RW
0000_0000h
200h - 22Ch
Mux Select (MUXSEL0 - MUXSEL11)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2579 / 5251


---
# 페이지 271

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
280h
Configuration (CFG)
32
RW
0303_0280h
284h
Software Override Enable (SWEN)
32
RW
0000_0000h
288h
Software Override Value (SWVALUE)
32
RW
0000_0000h
28Ch
Output Enable (OUTEN)
32
RW
0000_0000h
290h
Logic Inputs (LCIN)
32
R
0000_0000h
294h
Overridden Inputs (SWOUT)
32
R
0000_0000h
298h
Logic Outputs (LCOUT)
32
R
0000_0000h
29Ch
Forced Outputs (FORCEOUT)
32
R
0000_0000h
2A0h
Force Status (FORCESTS)
32
RW
0000_0000h
2A8h
Debug Mode Enable (DBGEN)
32
RW
0000_0000h
62.8.2 LC n Output m LUT Control (LC0_LUTCTRL0 - LC2_LUTCTRL3)
Offset
For n = 0 to 2; m = 0 to 3:
Register
Offset
LCn_LUTCTRLm
0h + (n × 40h) + (m × 4h)
Function
See LUTCTRL.
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
LUTCTRL 
W
Reset
0
0
0
0
0
0
0
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
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2580 / 5251


---
# 페이지 272

Fields
Field
Function
31-16
—
Reserved
15-0
LUTCTRL
LUT Control
Specifies the LUT positions, based on the combined LC input value, that result in assertion of this output. 
For more information, see Logic operations.
62.8.3 LC n Output m Filter (LC0_FILT0 - LC2_FILT3)
Offset
For n = 0 to 2; m = 0 to 3:
Register
Offset
LCn_FILTm
10h + (n × 40h) + (m × 4h)
Function
Specifies the rising- and falling-edge thresholds for the LC output filters.
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
LUT_RISE_FILT 
W
Reset
0
0
0
0
0
0
0
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
LUT_FALL_FILT 
W
Reset
0
0
0
0
0
0
0
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
LUT_RISE_FIL
T
Rise Filter
Specifies the number of consecutive clock cycles the filter output must be logic 1 before the output signal 
goes high.
0000_0000_0000_0000b - Bypass filter
All other values - Filter threshold
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2581 / 5251


---
# 페이지 273

Table continued from the previous page...
Field
Function
15-0
LUT_FALL_FIL
T
Fall Filter
Specifies the number of consecutive clock cycles the filter output must be logic 0 before the output signal 
goes low.
0000_0000_0000_0000b - Bypass filter
All other values - Filter threshold
62.8.4 LC n Interrupt and DMA Enable (LC0_INTDMAEN - LC2_INTDMAEN)
Offset
Register
Offset
LC0_INTDMAEN
20h
LC1_INTDMAEN
60h
LC2_INTDMAEN
A0h
Function
Enables interrupt and DMA requests for LUT and force events.
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
FORCE_DMA_EN 
0
FORCE_INT_EN 
W
Reset
0
0
0
0
0
0
0
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
LUT_DMA_EN 
0
LUT_INT_EN 
W
Reset
0
0
0
0
0
0
0
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
Reserved
27-24
Force DMA Enable
Enables the generation of a DMA request when a force event occurs (LCn_STS[FORCESTS]).
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2582 / 5251


---
# 페이지 274

Table continued from the previous page...
Field
Function
FORCE_DMA_
EN
For each bit:
0b - Disable
1b - Enable
Mapping of bits:
Output
Register bit
0
24
1
25
2
26
3
27
23-20
—
Reserved
19-16
FORCE_INT_E
N
Force Interrupt Enable
Enables the generation of an interrupt request when a force event occurs (LCn_STS[FORCESTS]).
For each bit:
0b - Disable
1b - Enable
Mapping of bits:
Output
Register bit
0
16
1
17
2
18
3
19
15-12
—
Reserved
11-8
LUT_DMA_EN
LUT DMA Enable
Enables the generation of a DMA request when an LUT event occurs (LCn_STS[LUT_STS]).
For each bit:
0b - Disable
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2583 / 5251


---
# 페이지 275

Table continued from the previous page...
Field
Function
1b - Enable
Mapping of bits:
Output
Register bit
0
8
1
9
2
10
3
11
7-4
—
Reserved
3-0
LUT_INT_EN
LUT Interrupt Enable
Enables the generation of an interrupt request when an LUT event occurs (LCn_STS[LUT_STS]).
For each bit:
0b - Disable
1b - Enable
Mapping of bits:
Output
Register bit
0
0
1
1
2
2
3
3
62.8.5 LC n Status (LC0_STS - LC2_STS)
Offset
Register
Offset
LC0_STS
24h
LC1_STS
64h
LC2_STS
A4h
Function
Indicates the occurrence of LUT and force events.
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2584 / 5251


---
# 페이지 276

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
FORCESTS 
0
LUT_STS 
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
31-12
—
Reserved
11-8
FORCESTS
Force Event
Indicates that a force event has occurred on the associated output.
For each bit:
0b - No event
1b - Event occurred
Mapping of bits:
Output
Register bit
0
8
1
9
2
10
3
11
When you enable DMA for a force output (LCn_INTDMAEN[FORCE_DMA_EN]) and a force event occurs 
on that output, LCU generates a DMA request. The resulting DMA done signal causes LCU to change the 
bit to 0, or you can write 1 to the bit.
You can also change these bits to 0 by writing to the corresponding Force Status 
bits (FORCESTS[FORCESTS]).
The timing of status clearing depends on the selected Force Mode (LCn_FCTRL[FORCE_MODEm]).
7-4
—
Reserved
3-0
LUT Event
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2585 / 5251


---
# 페이지 277

Table continued from the previous page...
Field
Function
LUT_STS
Indicates that an LUT event has occurred for the associated LC output.
For each bit:
0b - No event
1b - Event occurred
Mapping of bits:
Output
Register bit
0
0
1
1
2
2
3
3
When you enable DMA for an LUT event on an output (LCn_INTDMAEN[LUT_DMA_EN]) and an LUT 
event occurs on that output, LCU generates a DMA request. The resulting DMA done signal causes LCU 
to change the bit to 0.
When you enable interrupt request for an output (LCn_INTDMAEN[LUT_INT_EN]) and an LUT event occurs 
on that output, LCU generates an interrupt request. Write 1 to the bit to change it to 0.
62.8.6 LC n Output Polarity Control (LC0_OUTPOL - LC2_OUTPOL)
Offset
Register
Offset
LC0_OUTPOL
28h
LC1_OUTPOL
68h
LC2_OUTPOL
A8h
Function
Specifies the polarity of the LC outputs.
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2586 / 5251


---
# 페이지 278

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
OUTPOL 
W
Reset
0
0
0
0
0
0
0
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
OUTPOL
Output Polarity
Specifies the polarity of the outputs.
For each bit:
0b - Not inverted
1b - Inverted
Mapping of bits:
Output
Bit
0
0
1
1
2
2
3
3
62.8.7 LC n Force Filter (LC0_FFILT - LC2_FFILT)
Offset
Register
Offset
LC0_FFILT
2Ch
LC1_FFILT
6Ch
LC2_FFILT
ACh
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2587 / 5251


---
# 페이지 279

Function
Controls the force filter for this LC.
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
COMB_FORCE 
0
COMB_EN 
0
FORCE_POL 
W
Reset
0
0
0
0
0
0
0
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
FORCE_FILT 
W
Reset
0
0
0
0
0
0
0
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
COMB_FORCE
Combined Sensed Force Input
Indicates the combined value of force inputs to each output.
For each bit:
0b - Logic low
1b - Logic high
Mapping of bits:
Output
Bit
0
28
1
29
2
30
3
31
27
—
Reserved
26-24
COMB_EN
Combinational Force Path (CFP) Enable
Enables an active force input to combinationally affect the LC outputs. When CFP is not enabled, force 
inputs must be synchronized and then optionally filtered. When you enable CFP (write 1 to one of these bits), 
the corresponding force input bypasses synchronization and filtering and immediately affects the LC output.
The Force Filter (FORCE_FILT) is still in effect. Force inputs that do not meet the pulse width requirements 
for synchronization and filtering are not registered in Force Status (FORCESTS) and you do not need to 
write 1 to change the bit to 0.
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2588 / 5251


---
# 페이지 280

Table continued from the previous page...
Field
Function
CFP provides a safety factor when the LC outputs drive a motor and immediate response is required. In 
some topologies, an oscillation can result if the assertion of the force input causes the LC output to turn off. 
This situation in turn leads to deassertion of the force input and the output turning back on. In general, you 
must disable CFP unless the LCU outputs drive a motor or similar safety-critical application, which requires 
an immediate response without synchronization delays.
23-19
—
Reserved
18-16
FORCE_POL
Force Input Polarity
Specifies the polarity of the force inputs to this LC.
For each bit:
0b - Not inverted
1b - Inverted
Mapping of bits:
Input
Bit
0
16
1
17
2
18
15-8
—
Reserved
7-0
FORCE_FILT
Force Filter
Specifies the count, in clock cycles, that a force input must remain at a given logic state before the filtered 
force input switches state.
0000_0000b - Bypass filter
All other values - Filter threshold
62.8.8 LC n Force Control (LC0_FCTRL - LC2_FCTRL)
Offset
Register
Offset
LC0_FCTRL
30h
LC1_FCTRL
70h
LC2_FCTRL
B0h
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2589 / 5251


---
# 페이지 281

Function
Provides control of the force inputs.
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
SYNC_SEL3 
FORCE_MODE
3 
FORCE_SENSE3 
SYNC_SEL2 
FORCE_MODE
2 
FORCE_SENSE2 
W
Reset
0
0
0
0
0
0
0
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
SYNC_SEL1 
FORCE_MODE
1 
FORCE_SENSE1 
SYNC_SEL0 
FORCE_MODE
0 
FORCE_SENSE0 
W
Reset
0
0
0
0
0
0
0
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
SYNC_SEL3
Sync Select
Selects which sync input to use for output 3 of this LC.
00b - Sync input 0
01b - Sync input 1
10b - Reserved
11b - Reserved
29-28
FORCE_MODE
3
Force Clearing Mode
Specifies the timing for clearing force events for output 3 in this LC.
00b - Deassertion. Cleared on deassertion of force inputs
01b - Rising sync after deassertion. Cleared on rising sync after deassertion of force inputs
10b - Writing 1 after deassertion. Cleared by writing 1 to the correct LCn_STS[FORCESTS] or 
FORCESTS[FORCESTS] bits after deassertion of force inputs
11b - Rising sync after writing 1 and deassertion. Cleared on rising sync after writing 1 to the 
correct LCn_STS[FORCESTS] or FORCESTS[FORCESTS] bits and deassertion of force inputs
27-24
FORCE_SENS
E3
Force Input Sensitivity
Selects which force inputs affect output 3 of this LC.
For each bit:
0b - Does not affect
1b - Affects
Mapping of bits:
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2590 / 5251


---
# 페이지 282

Table continued from the previous page...
Field
Function
Input
Bit
0
24
1
25
2
26
Reserved
27
Example: 011b selects force inputs 0 and 1, but not 2.
23-22
SYNC_SEL2
Sync Select
Selects which sync input to use for output 2 of this LC.
00b - Sync input 0
01b - Sync input 1
10b - Reserved
11b - Reserved
21-20
FORCE_MODE
2
Force Clearing Mode
Specifies the timing for clearing force events for output 2 in this LC.
00b - Deassertion. Cleared on deassertion of force inputs
01b - Rising sync after deassertion. Cleared on rising sync after deassertion of force inputs
10b - Writing 1 after deassertion. Cleared by writing 1 to the correct LCn_STS[FORCESTS] or 
FORCESTS[FORCESTS] bits after deassertion of force inputs
11b - Rising sync after writing 1 and deassertion. Cleared on rising sync after writing 1 to the 
correct LCn_STS[FORCESTS] or FORCESTS[FORCESTS] bits and deassertion of force inputs
19-16
FORCE_SENS
E2
Force Input Sensitivity
Selects which force inputs affect output 2 of this LC.
For each bit:
0b - Does not affect
1b - Affects
Mapping of bits:
Input
Bit
0
16
1
17
2
18
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2591 / 5251


---
# 페이지 283

Table continued from the previous page...
Field
Function
Input
Bit
Reserved
19
Example: 011b selects force inputs 0 and 1, but not 2.
15-14
SYNC_SEL1
Sync Select
Selects which sync input to use for output 1 of this LC.
00b - Sync input 0
01b - Sync input 1
10b - Reserved
11b - Reserved
13-12
FORCE_MODE
1
Force Clearing Mode
Specifies the timing for clearing force events for output 1 in this LC.
00b - Deassertion. Cleared on deassertion of force inputs
01b - Rising sync after deassertion. Cleared on rising sync after deassertion of force inputs
10b - Writing 1 after deassertion. Cleared by writing 1 to the correct LCn_STS[FORCESTS] or 
FORCESTS[FORCESTS] bits after deassertion of force inputs
11b - Rising sync after writing 1 and deassertion. Cleared on rising sync after writing 1 to the 
correct LCn_STS[FORCESTS] or FORCESTS[FORCESTS] bits and deassertion of force inputs
11-8
FORCE_SENS
E1
Force Input Sensitivity
Selects which force inputs affect output 1 of this LC.
For each bit:
0b - Does not affect
1b - Affects
Mapping of bits:
Input
Bit
0
8
1
9
2
10
Reserved
11
Example: 011b selects force inputs 0 and 1, but not 2.
7-6
Sync Select
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2592 / 5251


---
# 페이지 284

Table continued from the previous page...
Field
Function
SYNC_SEL0
Selects which sync input to use for output 0 of this LC.
00b - Sync input 0
01b - Sync input 1
10b - Reserved
11b - Reserved
5-4
FORCE_MODE
0
Force Clearing Mode
Specifies the timing for clearing force events for output 0 in this LC.
00b - Deassertion. Cleared on deassertion of force inputs
01b - Rising sync after deassertion. Cleared on rising sync after deassertion of force inputs
10b - Writing 1 after deassertion. Cleared by writing 1 to the correct LCn_STS[FORCESTS] or 
FORCESTS[FORCESTS] bits after deassertion of force inputs
11b - Rising sync after writing 1 and deassertion. Cleared on rising sync after writing 1 to the 
correct LCn_STS[FORCESTS] or FORCESTS[FORCESTS] bits and deassertion of force inputs
3-0
FORCE_SENS
E0
Force Input Sensitivity
Selects which force inputs affect output 0 of this LC.
For each bit:
0b - Does not affect
1b - Affects
Mapping of bits:
Input
Bit
0
0
1
1
2
2
Reserved
3
Example: 011b selects force inputs 0 and 1, but not 2.
62.8.9 LC n Sync Control (LC0_SCTRL - LC2_SCTRL)
Offset
Register
Offset
LC0_SCTRL
34h
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2593 / 5251


---
# 페이지 285

Table continued from the previous page...
Register
Offset
LC1_SCTRL
74h
LC2_SCTRL
B4h
Function
Controls the software sync behavior.
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
SW_S
YNC...
0
SW_MODE 
W
Reset
0
0
0
0
0
0
0
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
SW_SYNC_SE
L
Software Sync Select
Selects which sync input to use for software synced mode.
0b - Sync input 0
1b - Sync input 1
7-4
—
Reserved
3-0
SW_MODE
Software Sync Mode
Specifies the software sync mode for the inputs to this LC. When Software Override is enabled (SWEN), 
these bits control whether Software Override Value (SWVALUE) changes occur immediately or on the rising 
edge of the selected sync pulse.
For each bit:
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2594 / 5251


---
# 페이지 286

Table continued from the previous page...
Field
Function
0b - Immediate
1b - On rising edge of sync
Mapping of bits:
Input
Bit
0
0
1
1
2
2
3
3
62.8.10 Mux Select (MUXSEL0 - MUXSEL11)
Offset
For a = 0 to 11:
Register
Offset
MUXSELa
200h + (a × 4h)
Function
Selects the sources for inputs to the LCs.
 
Access to Address space 200h + (48 to (124)) does not generate a transfer error.
  NOTE  
Register
LC
Input
MUXSEL0
0
0
MUXSEL1
1
MUXSEL2
2
MUXSEL3
3
MUXSEL4
1
0
MUXSEL5
1
MUXSEL6
2
MUXSEL7
3
MUXSEL8
2
0
Table continues on the next page...
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2595 / 5251


---
# 페이지 287

Table continued from the previous page...
Register
LC
Input
MUXSEL9
1
MUXSEL10
2
MUXSEL11
3
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
MUXSEL 
W
Reset
0
0
0
0
0
0
0
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
MUXSEL
Mux Select
Selects the source of the LC input.
All LU_IN inputs go through a two-stage synchronizer, but the LU_OUT signals fed back to this mux do not 
have this two-stage delay because they are already synchronous to LCU clock.
0000_0000b - Logic 0
0000_0001b-0000_1100b - LU_IN0 to LU_IN11
0000_1101b-0001_1000b - LU_OUT0 to LU_OUT11
All other values are reserved.
62.8.11 Configuration (CFG)
Offset
Register
Offset
CFG
280h
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2596 / 5251


---
# 페이지 288

Function
Indicates the LCU configuration, and provides write protection.
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
NUM_LOGIC_CELLS 
NUM_FORCES 
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
NUM_SYNCS 
INCL_
MU...
0
WP 
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
31-24
NUM_LOGIC_C
ELLS
LCs
Indicates the number of LCs.
23-16
NUM_FORCES
Force Inputs
Indicates the number of force inputs for each LC.
15-8
NUM_SYNCS
Sync Inputs
Indicates the number of sync inputs for each LC.
7
INCL_MUXES
Input Muxing
Indicates whether LCU supports input muxing.
0b - Not supported
1b - Supported
6-1
—
Reserved
0
WP
Write Protect
Turns on write protection for all LCU registers except SWVALUE, LCn_STS, and FORCESTS.
0b - No effect
1b - Turn on write protection
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2597 / 5251


---
# 페이지 289

62.8.12 Software Override Enable (SWEN)
Offset
Register
Offset
SWEN
284h
Function
Enables overrides for LC inputs.
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
SWEN 
W
Reset
0
0
0
0
0
0
0
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
31-12
—
Reserved
11-0
SWEN
Software Override Enable
Enables software override of LC inputs.
For each bit:
0b - Disable
1b - Enable
Mapping of bits: See Mapping of 12-bit input, output, and state fields.
62.8.13 Software Override Value (SWVALUE)
Offset
Register
Offset
SWVALUE
288h
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2598 / 5251


---
# 페이지 290

Function
Specifies the software override value for each LC input.
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
SWVALUE 
W
Reset
0
0
0
0
0
0
0
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
31-12
—
Reserved
11-0
SWVALUE
Software Override Value
Specifies the software override value for each LC input.
For each bit:
0b - 0
1b - 1
Mapping of bits: See Mapping of 12-bit input, output, and state fields.
62.8.14 Output Enable (OUTEN)
Offset
Register
Offset
OUTEN
28Ch
Function
Enables LC outputs.
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2599 / 5251


---
# 페이지 291

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
OUTEN 
W
Reset
0
0
0
0
0
0
0
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
31-12
—
Reserved
11-0
OUTEN
Output Enables
Enables LC outputs.
For each bit:
0b - Disable
1b - Enable
Mapping of bits: See Mapping of 12-bit input, output, and state fields.
62.8.15 Logic Inputs (LCIN)
Offset
Register
Offset
LCIN
290h
Function
Indicates states of LC inputs.
If you write to this register, LCU generates a bus transfer error.
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2600 / 5251


---
# 페이지 292

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
LC_INPUTS 
W
Reset
0
0
0
0
0
0
0
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
31-12
—
Reserved
11-0
LC_INPUTS
Logic Inputs
Indicates states of LC inputs.
For each bit:
0b - 0
1b - 1
Mapping of bits: See Mapping of 12-bit input, output, and state fields.
62.8.16 Overridden Inputs (SWOUT)
Offset
Register
Offset
SWOUT
294h
Function
Indicates states of LC inputs or states of software-overridden inputs, depending upon the state of the corresponding SWEN bit.
If you write to this register, LCU generates a bus transfer error.
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2601 / 5251


---
# 페이지 293

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
SWOUT 
W
Reset
0
0
0
0
0
0
0
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
31-12
—
Reserved
11-0
SWOUT
Overridden Inputs
Indicates states of LC inputs or software-overridden inputs.
For each bit, when the corresponding SWEN bit is 0:
0b - LC input is 0
1b - LC input is 1
For each bit, when the corresponding SWEN bit is 1:
0b - Software-overridden input is 0
1b - Software-overridden input is 1
Mapping of bits: See Mapping of 12-bit input, output, and state fields.
62.8.17 Logic Outputs (LCOUT)
Offset
Register
Offset
LCOUT
298h
Function
Indicates states of LC outputs.
If you write to this register, LCU generates a bus transfer error.
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2602 / 5251


---
# 페이지 294

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
LCOUT 
W
Reset
0
0
0
0
0
0
0
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
31-12
—
Reserved
11-0
LCOUT
Logic Outputs
Indicates states of LC outputs.
For each bit:
0b - 0
1b - 1
Mapping of bits: See Mapping of 12-bit input, output, and state fields.
62.8.18 Forced Outputs (FORCEOUT)
Offset
Register
Offset
FORCEOUT
29Ch
Function
Indicates the current state of the force outputs for all LCU logic outputs. Writing to this register generates a bus transfer error.
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2603 / 5251


---
# 페이지 295

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
FORCEOUT 
W
Reset
0
0
0
0
0
0
0
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
31-12
—
Reserved
11-0
FORCEOUT
Forced Outputs
Indicates the current state of force outputs for the logic outputs.
For each bit:
0b - Not asserted
1b - Asserted
Mapping of bits: See Mapping of 12-bit input, output, and state fields.
62.8.19 Force Status (FORCESTS)
Offset
Register
Offset
FORCESTS
2A0h
Function
See FORCESTS.
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2604 / 5251


---
# 페이지 296

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
FORCESTS 
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
31-12
—
Reserved
11-0
FORCESTS
Force Status
Indicates the current force states of all LCs, mirrored from LCn_STS[FORCESTS]. Change these bits to 0 
by writing 1 to them or to the corresponding bit in the specific LCn_STS register. This field allows you to 
simultaneously change FORCESTS bits to 0 across multiple LCs.
For each bit:
0b - Not in force state
1b - Read: In force state — Write: Clear force state bit
Mapping of bits: See Mapping of 12-bit input, output, and state fields.
62.8.20 Debug Mode Enable (DBGEN)
Offset
Register
Offset
DBGEN
2A8h
Function
Enables outputs to continue operation when the chip is in Debug mode.
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2605 / 5251


---
# 페이지 297

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
DBGEN 
W
Reset
0
0
0
0
0
0
0
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
31-12
—
Reserved
11-0
DBGEN
Debug Mode Enable
Enables outputs to continue operation in Debug mode.
For each bit:
0b - Debug mode inactive
1b - Debug mode active
Mapping of bits: See Mapping of 12-bit input, output, and state fields.
62.9 Glossary
CCW
Counterclockwise
CW
Clockwise
LC
Logic cell
LUT
Lookup table
NXP Semiconductors
Logic Control Unit (LCU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2606 / 5251


---