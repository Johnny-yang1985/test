# 페이지 82

Chapter 46
Mode Entry Module (MC_ME)
46.1 Chip-specific MC_ME information
46.1.1 MC_ME modes
This chip implements these modes:
• Reset
• Run
• Standby
The chip always enters Run mode after exiting Reset mode wherein you can configure the chip to perform its computational and 
communication functions. In Run mode:
• The chip remains fully powered. The boot core is the only core enabled on Run entry.
• You can enable and disable application cores and peripherals as needed, based on functional and power requirements.
• You can configure the pins and self-test as needed. See "Self-Test programming sequence" section in the STCU2 chapter 
for the self-test programming sequence to be followed before initiating self-test, in which:
— Pins are safe-stated.
— No computational or communication activities are possible.
• The chip automatically enters Reset mode after self-test (BIST) is complete.
46.1.2 Core operation modes
The Cortex-M7 cores in the chip support these two modes of operation:
• Decoupled/independent operation
• Coupled/lockstep operation
The device configuration clients (utest_misc DCF client) control these modes of operation. See the DCF clients file attached to 
this document for details.
46.1.3 MC_ME partition mapping of cores and peripherals
MC_ME provides registers and interface signals to support multiple partitions. These MC_ME partitions are different from the 
chip's LBIST partitions described in the "Safety Overview" chapter. This chip has three MC_ME partitions:
• Partition 0: Contains application cores and the on/off-platform slots on AIPS_0 bridge
• Partition 1: Contains the on/off-platform slots on AIPS_1 bridge
• Partition 2: Contains the on/off-platform slots on AIPS_2 bridge
Table 262 and Table 263 specify the core and peripheral mapping on MC_ME partitions and their associated clock 
gating possibilities.
MC_ME also provides provisions to control the booting address for application cores, which can be configured to start from a 
nondefault address location by appropriately configuring PRTNx_COREn_ADDR[ADDR].
46.1.4 Core clock gating
MC_ME has individual core-clock enable fields that gate the application core clocks, which can also be clock gated by executing 
Waiting for Interrupt (WFI).
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1740 / 5251


---
# 페이지 83

You can enable the application cores by configuring the respective CCE fields. See Application core initialization process and 
Application core shutdown process for proper initialization and shutdown of application cores. There is no clock control for the 
HSE_B core. It needs to be only put into WFI if required to be shutdown (for example, in Standby mode).
Table 262. MC_ME partition core mapping
Core
MC_ME partition
MC_ME clock enable register field
Cortex-M7_0
0
MC_ME.PRTN0_CORE0_PCONF[CCE]
Cortex-M7_1 1
0
MC_ME.PRTN0_CORE1_PCONF[CCE]
Cortex-M7_2 1, 2
0
MC_ME.PRTN0_CORE4_PCONF[CCE]
Cortex-M7_3 1, 3
0
MC_ME.PRTN0_CORE3_PCONF[CCE]
1. Not present on S32K312 and S32K311
2. Only present on S32K388, S32K389, S32K358, S32K348, S32K338, and S32K328
3. Only present on S32K388 and S32K389
46.1.5 Peripheral clock gating
See Peripheral initialization process and Peripheral shutdown process for proper initialization and shutdown of peripherals. 
See Table 263 for peripheral clock gating possibilities. This table details clock gating possibilities of all chips. For applicable 
modules/module instances see corresponding chip-specific section of the module. "MC_ME memory map" section the details 
clock gating possibilities of S32K388/S32K389 chip.
The application core can program the reserved configurations.
 
Before accessing the registers of a peripheral to start using it, its clock must be turned on, otherwise, a Hard-Fault 
event will occur.
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1741 / 5251


---
# 페이지 84

Table 263. MC_ME partition peripheral mapping and clock control
AIPS
Peripheral description
MC_ME COFB control register
MC_ME 
peripheral 
control 
register
MC_ME 
peripheral 
slot no. in 
partition
Clock gating 
control 
supported
Enabled on 
reset
On Platform
0
Crossbar Integrity Checker (HSE & 
AES_ACCEL AXBS_Lite)1
PRTN0_COFB0_CLKEN[REQ2]
2
2
No
Yes
Yes
0
ERM1
PRTN0_COFB0_CLKEN[REQ3]2
3
3
Yes
No
Yes
0
Flash controller 13
PRTN0_COFB0_CLKEN[REQ26]
26
26
No
Yes
Yes
0
Flash controller 1 alternate1
PRTN0_COFB0_CLKEN[REQ27]
27
27
No
Yes
Yes
0
Software Watchdog 3
PRTN0_COFB0_CLKEN[REQ28]1
28
28
Yes
No
Yes
0
Trigger Multiplexing Control
PRTN0_COFB1_CLKEN[REQ32]
32
32
Yes
No
No
0
Body Cross Triggering Unit
PRTN0_COFB1_CLKEN[REQ33]
33
33
Yes
No
No
0
eMIOS 0
PRTN0_COFB1_CLKEN[REQ34]
34
34
Yes
No
No
0
eMIOS 1
PRTN0_COFB1_CLKEN[REQ35]
35
35
Yes
No
No
0
eMIOS 24
PRTN0_COFB1_CLKEN[REQ36]
36
36
Yes
No
No
0
Logic Control Unit 0
PRTN0_COFB1_CLKEN[REQ38]
38
38
Yes
No
No
0
Logic Control Unit 1
PRTN0_COFB1_CLKEN[REQ39]
39
39
Yes
No
No
0
Analog-to-digital converter 0
PRTN0_COFB1_CLKEN[REQ40]
40
40
Yes
No
No
0
Analog-to-digital converter 1
PRTN0_COFB1_CLKEN[REQ41]
41
41
Yes
No
No
0
Analog-to-digital converter 24
PRTN0_COFB1_CLKEN[REQ42]
42
42
Yes
No
No
0
Programmable Interrupt Timer 0
PRTN0_COFB1_CLKEN[REQ44]
44
44
Yes
Yes
No
0
Programmable Interrupt Timer 1
PRTN0_COFB1_CLKEN[REQ45]
45
45
Yes
No
No
0
MU_2_MUA5
PRTN0_COFB1_CLKEN[REQ46]
46
46
Yes
No
No
0
MU_2_MUB5
PRTN0_COFB1_CLKEN[REQ47]
47
47
Yes
No
No
0
MU_3_MUA1
PRTN0_COFB1_CLKEN[REQ49]
49
49
Yes
No
No
0
MU_3_MUB1
PRTN0_COFB1_CLKEN[REQ50]
50
50
Yes
No
No
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1742 / 5251


---
# 페이지 85

Table 263. MC_ME partition peripheral mapping and clock control (continued)
AIPS
Peripheral description
MC_ME COFB control register
MC_ME 
peripheral 
control 
register
MC_ME 
peripheral 
slot no. in 
partition
Clock gating 
control 
supported
Enabled on 
reset
On Platform
0
MU_4_MUA1
PRTN0_COFB1_CLKEN[REQ51]
51
51
Yes
No
No
0
MU_4_MUB1
PRTN0_COFB1_CLKEN[REQ52]
52
52
Yes
No
No
1
System crossbar switch6
PRTN1_COFB0_CLKEN[REQ0]
128
0
No
Yes
Yes
1
Crossbar Integrity Checker 
(System AXBS / AXBS Lite)
PRTN1_COFB0_CLKEN[REQ1]
129
1
No
Yes
Yes
1
Crossbar Integrity Checker 
(Peripheral AXBS-Lite)6
PRTN1_COFB0_CLKEN[REQ2]
130
2
No
Yes
Yes
1
eDMA control & status (MP_CSR; 
MP_ES; MP_HRS)
PRTN1_COFB0_CLKEN[REQ3]
131
3
Yes
No
Yes
1
eDMA transfer control descriptor 0
PRTN1_COFB0_CLKEN[REQ4]
132
4
Yes
No
Yes
1
eDMA transfer control descriptor 1
PRTN1_COFB0_CLKEN[REQ5]
133
5
Yes
No
Yes
1
eDMA transfer control descriptor 2
PRTN1_COFB0_CLKEN[REQ6]
134
6
Yes
No
Yes
1
eDMA transfer control descriptor 3
PRTN1_COFB0_CLKEN[REQ7]
135
7
Yes
No
Yes
1
eDMA transfer control descriptor 4
PRTN1_COFB0_CLKEN[REQ8]
136
8
Yes
No
Yes
1
eDMA transfer control descriptor 5
PRTN1_COFB0_CLKEN[REQ9]
137
9
Yes
No
Yes
1
eDMA transfer control descriptor 6
PRTN1_COFB0_CLKEN[REQ10]
138
10
Yes
No
Yes
1
eDMA transfer control descriptor 7
PRTN1_COFB0_CLKEN[REQ11]
139
11
Yes
No
Yes
1
eDMA transfer control descriptor 8
PRTN1_COFB0_CLKEN[REQ12]
140
12
Yes
No
Yes
1
eDMA transfer control descriptor 9
PRTN1_COFB0_CLKEN[REQ13]
141
13
Yes
No
Yes
1
eDMA transfer control descriptor 
10
PRTN1_COFB0_CLKEN[REQ14]
142
14
Yes
No
Yes
1
eDMA transfer control descriptor 
11
PRTN1_COFB0_CLKEN[REQ15]
143
15
Yes
No
Yes
1
Debug APB Page0
PRTN1_COFB0_CLKEN[REQ21]
149
21
No
Yes
Yes
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1743 / 5251


---
# 페이지 86

Table 263. MC_ME partition peripheral mapping and clock control (continued)
AIPS
Peripheral description
MC_ME COFB control register
MC_ME 
peripheral 
control 
register
MC_ME 
peripheral 
slot no. in 
partition
Clock gating 
control 
supported
Enabled on 
reset
On Platform
1
Debug APB Page1
PRTN1_COFB0_CLKEN[REQ21]
149
21
No
Yes
Yes
1
Debug APB Page2
PRTN1_COFB0_CLKEN[REQ21]
149
21
No
Yes
Yes
1
Debug APB Page3
PRTN1_COFB0_CLKEN[REQ21]
149
21
No
Yes
Yes
1
Debug APB Paged Area
PRTN1_COFB0_CLKEN[REQ21]
149
21
No
Yes
Yes
1
SDA-AP
PRTN1_COFB0_CLKEN[REQ21]
149
21
Yes
Yes
Yes
1
EIM07
PRTN1_COFB0_CLKEN[REQ22]
150
22
Yes
No
Yes
1
ERM0
PRTN1_COFB0_CLKEN[REQ23]
151
23
Yes
No
Yes
1
MSCM
PRTN1_COFB0_CLKEN[REQ24]
152
24
Yes
No
Yes
1
RAM controller 0
PRTN1_COFB0_CLKEN[REQ25]
153
25
No
Yes
Yes
1
Flash controller
PRTN1_COFB0_CLKEN[REQ26]
154
26
No
Yes
Yes
1
Flash controller alternate
PRTN1_COFB0_CLKEN[REQ27]
155
27
No
Yes
Yes
1
Software Watchdog 0
PRTN1_COFB0_CLKEN[REQ28]
156
28
Yes
Yes
Yes
1
System Timer Module 0
PRTN1_COFB0_CLKEN[REQ29]
157
29
Yes
No
Yes
1
XRDC
PRTN1_COFB0_CLKEN[REQ30]
158
30
No
Yes
Yes
1
Interrupt Monitor
PRTN1_COFB0_CLKEN[REQ31]
159
31
Yes
No
Yes
1
DMA Channel Multiplexer 0
PRTN1_COFB1_CLKEN[REQ32]
160
32
Yes
No
No
1
DMA Channel Multiplexer 1
PRTN1_COFB1_CLKEN[REQ33]
161
33
Yes
No
No
1
Real-time clock
PRTN1_COFB1_CLKEN[REQ34]
162
34
Yes
Yes
No
1
Reset Generation Module
PRTN1_COFB1_CLKEN[REQ35]
163
35
No
Yes
No
1
SIUL_VIRTWRAPPER_PDAC0
PRTN1_COFB1_CLKEN[REQ36]
164
36
No
Yes
No
1
SIUL_VIRTWRAPPER_PDAC0
PRTN1_COFB1_CLKEN[REQ37]
165
37
No
Yes
No
1
SIUL_VIRTWRAPPER_PDAC1
PRTN1_COFB1_CLKEN[REQ38]
166
38
No
Yes
No
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1744 / 5251


---
# 페이지 87

Table 263. MC_ME partition peripheral mapping and clock control (continued)
AIPS
Peripheral description
MC_ME COFB control register
MC_ME 
peripheral 
control 
register
MC_ME 
peripheral 
slot no. in 
partition
Clock gating 
control 
supported
Enabled on 
reset
On Platform
1
SIUL_VIRTWRAPPER_PDAC1
PRTN1_COFB1_CLKEN[REQ39]
167
39
No
Yes
No
1
SIUL_VIRTWRAPPER_PDAC25
PRTN1_COFB1_CLKEN[REQ40]
168
40
No
Yes
No
1
SIUL_VIRTWRAPPER_PDAC25
PRTN1_COFB1_CLKEN[REQ41]
169
41
No
Yes
No
1
SIUL_VIRTWRAPPER_PDAC3
PRTN1_COFB1_CLKEN[REQ42]
170
42
Yes
Yes
No
1
System Status and Configuration 
Module
PRTN1_COFB1_CLKEN[REQ43]
171
43
No
Yes
No
1
Wakeup Unit
PRTN1_COFB1_CLKEN[REQ45]
173
45
Yes
Yes
No
1
CMU 0-6
PRTN1_COFB1_CLKEN[REQ47]
175
47
Yes
No
No
1
Touch Sensing Coupling Controller
PRTN1_COFB1_CLKEN[REQ49]
177
49
Yes
Yes
No
1
32 kHz Slow Internal RC Oscillator
PRTN1_COFB1_CLKEN[REQ50]
178
50
No
Yes
No
1
32 kHz Slow External Crystal 
Oscillator 8
PRTN1_COFB1_CLKEN[REQ51]
179
51
Yes
Yes
No
1
48 MHz Fast Internal RC Oscillator
PRTN1_COFB1_CLKEN[REQ52]
180
52
No
Yes
No
1
8-40 MHz Fast External Crystal 
Oscillator
PRTN1_COFB1_CLKEN[REQ53]
181
53
Yes
Yes
No
1
Clock Generation Module
PRTN1_COFB1_CLKEN[REQ54]
182
54
No
Yes
No
1
Mode Entry Module
PRTN1_COFB1_CLKEN[REQ55]
183
55
No
Yes
No
1
Frequency Modulated Phase-
Locked Loop
PRTN1_COFB1_CLKEN[REQ56]
184
56
Yes
No
No
1
Frequency Modulated Phase-
Locked Loop 29
PRTN1_COFB1_CLKEN[REQ57]
185
57
Yes
No
No
1
Power management controller
PRTN1_COFB1_CLKEN[REQ58]
186
58
No
Yes
No
1
Flash memory
PRTN1_COFB1_CLKEN[REQ59]
187
59
No
Yes
No
1
Flash memory alternate
PRTN1_COFB1_CLKEN[REQ60]
188
60
No
Yes
No
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1745 / 5251


---
# 페이지 88

Table 263. MC_ME partition peripheral mapping and clock control (continued)
AIPS
Peripheral description
MC_ME COFB control register
MC_ME 
peripheral 
control 
register
MC_ME 
peripheral 
slot no. in 
partition
Clock gating 
control 
supported
Enabled on 
reset
On Platform
1
SIUL_VIRTWRAPPER_PDAC410
PRTN1_COFB1_CLKEN[REQ61]
189
61
No
Yes
No
1
SIUL_VIRTWRAPPER_PDAC410
PRTN1_COFB1_CLKEN[REQ62]
190
62
No
Yes
No
1
Programmable Interrupt Timer 2
PRTN1_COFB1_CLKEN[REQ63]
191
63
Yes
No
No
1
Programmable Interrupt Timer 31
PRTN1_COFB2_CLKEN[REQ64]
192
64
Yes
No
No
1
FlexCAN 0
PRTN1_COFB2_CLKEN[REQ65]
193
65
Yes
No
No
1
FlexCAN 1
PRTN1_COFB2_CLKEN[REQ66]
194
66
Yes
No
No
1
FlexCAN 2
PRTN1_COFB2_CLKEN[REQ67]
195
67
Yes
No
No
1
FlexCAN 38
PRTN1_COFB2_CLKEN[REQ68]
196
68
Yes
No
No
1
FlexCAN 411
PRTN1_COFB2_CLKEN[REQ69]
197
69
Yes
No
No
1
FlexCAN 511
PRTN1_COFB2_CLKEN[REQ70]
198
70
Yes
No
No
1
FlexCAN 62
PRTN1_COFB2_CLKEN[REQ71]
199
71
Yes
No
No
1
FlexCAN 72
PRTN1_COFB2_CLKEN[REQ72]
200
72
Yes
No
No
1
Flexible IO
PRTN1_COFB2_CLKEN[REQ73]
201
73
Yes
No
No
1
Low Power UART 0
PRTN1_COFB2_CLKEN[REQ74]
202
74
Yes
No
No
1
Low Power UART 1
PRTN1_COFB2_CLKEN[REQ75]
203
75
Yes
No
No
1
Low Power UART 2
PRTN1_COFB2_CLKEN[REQ76]
204
76
Yes
No
No
1
Low Power UART 3
PRTN1_COFB2_CLKEN[REQ77]
205
77
Yes
No
No
1
Low Power UART 411
PRTN1_COFB2_CLKEN[REQ78]
206
78
Yes
No
No
1
Low Power UART 511
PRTN1_COFB2_CLKEN[REQ79]
207
79
Yes
No
No
1
Low Power UART 611
PRTN1_COFB2_CLKEN[REQ80]
208
80
Yes
No
No
1
Low Power UART 711
PRTN1_COFB2_CLKEN[REQ81]
209
81
Yes
No
No
1
SIUL_VIRTWRAPPER_PDAC51
PRTN1_COFB2_CLKEN[REQ82]
210
82
No
Yes
No
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1746 / 5251


---
# 페이지 89

Table 263. MC_ME partition peripheral mapping and clock control (continued)
AIPS
Peripheral description
MC_ME COFB control register
MC_ME 
peripheral 
control 
register
MC_ME 
peripheral 
slot no. in 
partition
Clock gating 
control 
supported
Enabled on 
reset
On Platform
1
SIUL_VIRTWRAPPER_PDAC51
PRTN1_COFB2_CLKEN[REQ83]
211
83
No
Yes
No
1
Low Power I2C 0
PRTN1_COFB2_CLKEN[REQ84]
212
84
Yes
No
No
1
Low Power I2C 1
PRTN1_COFB2_CLKEN[REQ85]
213
85
Yes
No
No
1
Low Power SPI 0
PRTN1_COFB2_CLKEN[REQ86]
214
86
Yes
No
No
1
Low Power SPI 1
PRTN1_COFB2_CLKEN[REQ87]
215
87
Yes
No
No
1
Low Power SPI 2
PRTN1_COFB2_CLKEN[REQ88]
216
88
Yes
No
No
1
Low Power SPI 3
PRTN1_COFB2_CLKEN[REQ89]
217
89
Yes
No
No
1
Synchronous Audio Interface 06
PRTN1_COFB2_CLKEN[REQ91]
219
91
Yes
No
No
1
Low Power Comparator 0
PRTN1_COFB2_CLKEN[REQ92]
220
92
Yes
Yes
No
1
Low Power Comparator 18
PRTN1_COFB2_CLKEN[REQ93]
221
93
Yes
Yes
No
1
TMU Temperature Sensor Unit
PRTN1_COFB2_CLKEN[REQ95]
223
95
Yes
No
No
1
CRC
PRTN1_COFB3_CLKEN[REQ96]
224
96
Yes
No
No
1
FCCU (+FOSU)
PRTN1_COFB3_CLKEN[REQ97]
225
97
No
Yes
No
1
MU_0_MUB
PRTN1_COFB3_CLKEN[REQ99]
227
99
No
Yes
No
1
MU_1_MUB12
PRTN1_COFB3_CLKEN[REQ100]
228
100
No
Yes
No
1
JDC (JTAG Data Communication)
PRTN1_COFB3_CLKEN[REQ101]
229
101
No
Yes
No
1
Configuration GPR
PRTN1_COFB3_CLKEN[REQ103]
231
103
No
Yes
No
1
Self-Test Control Unit
PRTN1_COFB3_CLKEN[REQ104]
232
104
Yes
Yes
No
1
Selftest GPR6
PRTN1_COFB3_CLKEN[REQ108]
236
108
No
Yes
No
1
AES Accelerator 1,13
PRTN1_COFB3_CLKEN[REQ112-REQ-115]
240
112
Yes
No
No
1
AES Application 01,13
PRTN1_COFB3_CLKEN[REQ116-REQ119]
244
116
Yes
No
No
1
AES Application 11,13
PRTN1_COFB3_CLKEN[REQ120-REQ123]
248
120
Yes
No
No
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1747 / 5251


---
# 페이지 90

Table 263. MC_ME partition peripheral mapping and clock control (continued)
AIPS
Peripheral description
MC_ME COFB control register
MC_ME 
peripheral 
control 
register
MC_ME 
peripheral 
slot no. in 
partition
Clock gating 
control 
supported
Enabled on 
reset
On Platform
1
AES Application 21,13
PRTN1_COFB3_CLKEN[REQ124-REQ127]
252
124
Yes
No
No
2
Crossbar Integrity Checker (TCM 
backdoor AHB Splitter)14
PRTN2_COFB0_CLKEN[REQ0]
256
0
No
Yes
Yes
2
Crossbar Integrity Checker (eDMA 
& STAM AXBS-Lite)14
PRTN2_COFB0_CLKEN[REQ1]
257
1
No
Yes
Yes
2
Crossbar Integrity Checker 
(PRAM2 & TCM backdoor AHB 
Splitter)2
PRTN2_COFB0_CLKEN[REQ2]
258
2
No
Yes
Yes
2
Crossbar Integrity Checker 
(AES_ACCEL AHB Multiplexer)1
PRTN2_COFB0_CLKEN[REQ3]
259
3
No
Yes
Yes
2
eDMA transfer control descriptor 
126
PRTN2_COFB0_CLKEN[REQ4]
260
4
Yes
No
Yes
2
eDMA transfer control descriptor 
136
PRTN2_COFB0_CLKEN[REQ5]
261
5
Yes
No
Yes
2
eDMA transfer control descriptor 
146
PRTN2_COFB0_CLKEN[REQ6]
262
6
Yes
No
Yes
2
eDMA transfer control descriptor 
156
PRTN2_COFB0_CLKEN[REQ7]
263
7
Yes
No
Yes
2
eDMA transfer control descriptor 
166
PRTN2_COFB0_CLKEN[REQ8]
264
8
Yes
No
Yes
2
eDMA transfer control descriptor 
176
PRTN2_COFB0_CLKEN[REQ9]
265
9
Yes
No
Yes
2
eDMA transfer control descriptor 
186
PRTN2_COFB0_CLKEN[REQ10]
266
10
Yes
No
Yes
2
eDMA transfer control descriptor 
196
PRTN2_COFB0_CLKEN[REQ11]
267
11
Yes
No
Yes
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1748 / 5251


---
# 페이지 91

Table 263. MC_ME partition peripheral mapping and clock control (continued)
AIPS
Peripheral description
MC_ME COFB control register
MC_ME 
peripheral 
control 
register
MC_ME 
peripheral 
slot no. in 
partition
Clock gating 
control 
supported
Enabled on 
reset
On Platform
2
eDMA transfer control descriptor 
206
PRTN2_COFB0_CLKEN[REQ12]
268
12
Yes
No
Yes
2
eDMA transfer control descriptor 
216
PRTN2_COFB0_CLKEN[REQ13]
269
13
Yes
No
Yes
2
eDMA transfer control descriptor 
226
PRTN2_COFB0_CLKEN[REQ14]
270
14
Yes
No
Yes
2
eDMA transfer control descriptor 
236
PRTN2_COFB0_CLKEN[REQ15]
271
15
Yes
No
Yes
2
eDMA transfer control descriptor 
246
PRTN2_COFB0_CLKEN[REQ16]
272
16
Yes
No
Yes
2
eDMA transfer control descriptor 
256
PRTN2_COFB0_CLKEN[REQ17]
273
17
Yes
No
Yes
2
eDMA transfer control descriptor 
266
PRTN2_COFB0_CLKEN[REQ18]
274
18
Yes
No
Yes
2
eDMA transfer control descriptor 
276
PRTN2_COFB0_CLKEN[REQ19]
275
19
Yes
No
Yes
2
eDMA transfer control descriptor 
286
PRTN2_COFB0_CLKEN[REQ20]
276
20
Yes
No
Yes
2
eDMA transfer control descriptor 
296
PRTN2_COFB0_CLKEN[REQ21]
277
21
Yes
No
Yes
2
eDMA transfer control descriptor 
306
PRTN2_COFB0_CLKEN[REQ22]
278
22
Yes
No
Yes
2
eDMA transfer control descriptor 
316
PRTN2_COFB0_CLKEN[REQ23]
279
23
Yes
No
Yes
2
Semaphores26
PRTN2_COFB0_CLKEN[REQ24]
280
24
Yes
No
Yes
2
RAM controller 14
PRTN2_COFB0_CLKEN[REQ25]
281
25
No
Yes
Yes
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1749 / 5251


---
# 페이지 92

Table 263. MC_ME partition peripheral mapping and clock control (continued)
AIPS
Peripheral description
MC_ME COFB control register
MC_ME 
peripheral 
control 
register
MC_ME 
peripheral 
slot no. in 
partition
Clock gating 
control 
supported
Enabled on 
reset
On Platform
2
RAM controller 22
PRTN2_COFB0_CLKEN[REQ26]
282
26
No
Yes
Yes
2
Software Watchdog 115
PRTN2_COFB0_CLKEN[REQ27]
283
27
Yes
No
Yes
2
Software Watchdog 216
PRTN2_COFB0_CLKEN[REQ28]
284
28
Yes
No
Yes
2
System Timer Module 16
PRTN2_COFB0_CLKEN[REQ29]
285
29
Yes
No
Yes
2
System Timer Module 22
PRTN2_COFB0_CLKEN[REQ30]
286
30
Yes
No
Yes
2
System Timer Module 31
PRTN2_COFB0_CLKEN[REQ31]
287
31
Yes
No
Yes
2
EMAC17
PRTN2_COFB1_CLKEN[REQ32]
288
32
Yes
No
No
2
GMAC02
PRTN2_COFB1_CLKEN[REQ33]
289
33
Yes
No
No
2
GMAC11
PRTN2_COFB1_CLKEN[REQ34]
290
34
Yes
No
No
2
Low Power UART 84
PRTN2_COFB1_CLKEN[REQ35]
291
35
Yes
No
No
2
Low Power UART 94
PRTN2_COFB1_CLKEN[REQ36]
292
36
Yes
No
No
2
Low Power UART 104
PRTN2_COFB1_CLKEN[REQ37]
293
37
Yes
No
No
2
Low Power UART 114
PRTN2_COFB1_CLKEN[REQ38]
294
38
Yes
No
No
2
Low Power UART 124
PRTN2_COFB1_CLKEN[REQ39]
295
39
Yes
No
No
2
Low Power UART 134
PRTN2_COFB1_CLKEN[REQ40]
296
40
Yes
No
No
2
Low Power UART 144
PRTN2_COFB1_CLKEN[REQ41]
297
41
Yes
No
No
2
Low Power UART 154
PRTN2_COFB1_CLKEN[REQ42]
298
42
Yes
No
No
2
Low Power SPI 44
PRTN2_COFB1_CLKEN[REQ47]
303
47
Yes
No
No
2
Low Power SPI 54
PRTN2_COFB1_CLKEN[REQ48]
304
48
Yes
No
No
2
QuadSPI4
PRTN2_COFB1_CLKEN[REQ51]
307
51
Yes
No
No
2
Synchronous Audio Interface 14
PRTN2_COFB1_CLKEN[REQ55]
311
55
Yes
No
No
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1750 / 5251


---
# 페이지 93

Table 263. MC_ME partition peripheral mapping and clock control (continued)
AIPS
Peripheral description
MC_ME COFB control register
MC_ME 
peripheral 
control 
register
MC_ME 
peripheral 
slot no. in 
partition
Clock gating 
control 
supported
Enabled on 
reset
On Platform
2
Ultra Secured Digital Host 
Controller18
PRTN2_COFB1_CLKEN[REQ57]
313
57
Yes
No
No
2
Low Power Comparator 24
PRTN2_COFB1_CLKEN[REQ58]
314
58
Yes
Yes
No
2
MU_1_MUB4
PRTN2_COFB1_CLKEN[REQ59]
315
59
No
Yes
No
2
EIM02
PRTN2_COFB2_CLKEN[REQ67]
323
67
Yes
No
No
2
EIM12
PRTN2_COFB2_CLKEN[REQ68]
324
68
Yes
No
No
2
EIM22
PRTN2_COFB2_CLKEN[REQ69]
325
69
Yes
No
No
2
EIM32
PRTN2_COFB2_CLKEN[REQ70]
326
70
Yes
No
No
2
AES Application 31,13
PRTN2_COFB2_CLKEN[REQ72-REQ75]
328
72
Yes
No
No
2
AES Application 41,13
PRTN2_COFB2_CLKEN[REQ76-REQ79]
332
76
Yes
No
No
2
AES Application 51,13
PRTN2_COFB2_CLKEN[REQ80-REQ83]
336
80
Yes
No
No
2
AES Application 61,13
PRTN2_COFB2_CLKEN[REQ84-REQ87]
340
84
Yes
No
No
2
AES Application 71,13
PRTN2_COFB2_CLKEN[REQ88-REQ91]
344
88
Yes
No
No
2
FlexCAN 83
PRTN2_COFB2_CLKEN[REQ92]
348
92
Yes
No
No
2
FlexCAN 93
PRTN2_COFB2_CLKEN[REQ93]
349
93
Yes
No
No
2
FlexCAN 103
PRTN2_COFB2_CLKEN[REQ94]
350
94
Yes
No
No
2
FlexCAN 113
PRTN2_COFB2_CLKEN[REQ95]
351
95
Yes
No
No
2
Flash memory 13
PRTN2_COFB3_CLKEN[REQ96]
352
96
No
Yes
No
2
Flash memory 1 alternate3
PRTN2_COFB3_CLKEN[REQ97]
353
97
No
Yes
No
2
RAM controller 33
PRTN2_COFB3_CLKEN[REQ98]
354
98
No
Yes
No
1. Applicable for S32K388 and S32K389 only.
2. Applicable for S32K328, S32K338, S32K348, S32K358, S32K388, and S43K389 only.
3. Applicable for S32K389 only.
4. Applicable for S32K314, S32K324, S32K344, S32K328,S32K338, S32K348, S32K358, S32K388, and S32K389 only.
5. Applicable for S32K322, S32K324, S32K328, S32K338, S32K358, S32K388, and S32K389 only.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1751 / 5251


---
# 페이지 94

6. Reserved for S32K310, S32K311, and S32K312.
7. Applicable for S32K310, S32K311, S32K312, S32K322, S32K341, S32K342, S32K314, S32K324, and S32K344
Table 264. PRTN1_COFB0_CLKEN[REQ22]
Bit filed
Description
REQ22
Clock enable
This bit provides the clock enable control for block 22 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
8. Reserved for S32K310 and S32K311.
9. Applicable for S32K328, S32K338, S32K348, S32K358, S32K388, and S32K389 only.
10. Applicable for S32K338, S32K388 and S32K389 only.
11. Reserved for S32K310, S32K311, S32K322, S32K341, and S32K342.
12. Applicable for S32K310, S32K311, and S32K312 only.
13. All the corresponding MC_ME slots must be configured to access the peripheral. For example, PRTN1_COFB3_CLKEN[REQ112], 
PRTN1_COFB3_CLKEN[REQ113], PRTN1_COFB3_CLKEN[REQ114], and PRTN1_COFB3_CLKEN[REQ115] must be configured to access AES Accelerator.
14. Applicable for S32K322, S32K341, S32K342, S32K314, S32K324, S32K344, S32K388, and S32K389
15. Applicable for S32K322, S32K324, S32K328, S32K338, S32K358, S32K388, and S32K389 only.
16. Applicable for S32K338, S32K388, and S32K389 only.
17. Applicable for S32K322, S32K341, S32K342, S32K314, S32K324, and S32K344 only.
Table 265. PRTN2_COFB1_CLKEN[REQ32]
Bit filed
Description
REQ32
Clock enable
This bit provides the clock enable control for block 32 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
18. Applicable for S32K328, S32K338, S32K348, and S32K358 only.
Table 266. PRTN2_COFB1_CLKEN[REQ57]
Bit filed
Description
REQ57
Clock enable
This bit provides the clock enable control for block 57 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1752 / 5251


---
# 페이지 95

46.1.6 Application core initialization process
Start
Core starts execution
from boot address
Write the application core boot address to
PRTN   _CORE  _ADDR
m
n
Write valid key sequence to
CTL_KEY
Enable the application core clock by using
PRTN   _CORE  _PCONF[CCE]
m
n
Write to
PRTN   _CORE  _PUPD
m
n
Read the process-update status from
PRTN   _CORE  _PUPD
m
n
Run software diagnostics
Process
completed
(PUPD=0)?
Read the application core clock status from
PRTN   _CORE  _STAT[CCS]
m
n
Core clock
enabled?
Yes
No
Figure 190. Application core initialization process
46.1.7 Application core shutdown process
If a debugger is attached to the chip and application debug is enabled, the application core continues running if you write 0 
to MDM_AP.MDMAPCT[CM7_n_CORE_ACCESS].
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1753 / 5251


---
# 페이지 96

Core is in Running
or Active state
Stop any ongoing core
communication
Request core to enter WFI by writing
to corresponding core registers
Core in Turn-Off
or Inactive state
Read the application core WFI status from
PRTN   _CORE  _STAT[WFI]
m
n
Write valid key sequence to
CTL_KEY
Disable the application core clock by using
PRTN   _CORE  _PCONF[CCE]
m
n
Write to
PRTN   _CORE  _PUPD
m
n
Read the process-update status from
PRTN   _CORE  _PUPD
m
n
Run software diagnostics
Process
completed
(PUPD=0)?
Read the application core clock status by using
PRTN   _CORE  _STAT[CCS]
m
n
Core clock
disabled?
Yes
No
Figure 191. Application core shutdown process
46.1.8 Peripheral initialization process
You cannot control all the peripherals. For example, you cannot turn on and turn off the peripherals required for chip functionality 
across reset or power-up. They always remain on.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1754 / 5251


---
# 페이지 97

Start
Start peripheral
operation
Write valid key sequence to
CTL_KEY
Enable the peripheral core clock by using
PRTN   _COFB  _CLKEN[REQ  ]
m
n
z
Write to
PRTN   _PUPD
m
Read the process-update status from
PRTN   _PUPD
m
Run software diagnostics
Process
completed
(PUPD=0)?
Read the application core clock status from
PRTN   _COFB  _STAT[BLOCK  ]
m
n
z
Peripheral
clock
enabled?
Yes
No
Consider the peripheral initialization
requirements or sequence in the
corresponding chapter
Figure 192. Peripheral initialization process
46.1.9 Peripheral shutdown process
You cannot control all the peripherals. For example, you cannot turn on and turn off the peripherals required for chip functionality 
across reset or power-up. They always remain on.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1755 / 5251


---
# 페이지 98

Peripheral in Running
or Active state
Stop any ongoing communication with
input, output, cores or peripherals
Disable peripheral by writing to
its module-disable field (MDIS, EN or similar)
Peripheral in Turn-Off
or Inactive state
Read the peripheral status by reading back
the module-disable field (MDIS, EN or similar)
Write valid key sequence to
CTL_KEY
Disable the peripheral by using
PRTN   _COFB  _CLKEN[REQ  ]
m
z
n
Write to
PRTN   _PUPD
m
Read the process-update status from
PRTN   _PUPD
m
Run software diagnostics
Process
completed
(PUPD=0)?
Read the application core clock status from
PRTN   _COFB  _STAT[BLOCK  ]
m
n
z
Peripheral
clock
disabled?
Yes
No
Figure 193. Peripheral shutdown process
46.2 Introduction
The MC_ME module generates control signals for a set of modules of the SoC. The set of signals are defined in corresponding 
'Partition Configuration Registers'. It also implements a software-based mechanism for initiating a functional and destructive reset 
sequence and standby entry handshake with power management of SoC. See Figure 194 for the MC_ME block diagram.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1756 / 5251


---
# 페이지 99

Configuration registers
Partition 0
P
P
P
Partition 2
P
P
P
Mode controller
Configuration bus
Partition controls
Partition controls
Figure 194. MC_ME block diagram
46.3 Features
MC_ME includes the following features:
• 3 logic partitions implementation and their controls
• Core clock controls
• Partition clock control
• Control mechanism for initiating a destructive or functional reset sequence to MC_RGM
• Control mechanism for initiating standby mode entry for SoC
The logic partition inside MC_ME refers to a certain group of on-chip resources (or IP blocks) that are clubbed together to represent 
a single 'Partition' inside MC_ME. The MC_ME partition can be the same or different than an LBIST partition. Each of the MC_ME 
partitions implements a certain number of hardware processes. These hardware processes provide a mechanism to regulate 
various control signals provided to or received from the IP blocks. The corresponding status signals can also be monitored from 
MC_ME register(s). Each of the hardware processes is bound to finish in 512 cycles of the MC_ME register configuration clocks. 
Therefore, the hardware processes are non blocking in nature. Mismatch in the expected versus actual status of any hardware 
process is controlled by a pre-defined software.
46.4 Partition processes
Each of the processes inside the partition controls register space and corresponds to a control signal provided to that partition. A 
partition can include a core, or COFBs, or both. The MC_ME hardware processes provide control and status via signals provided 
to partitions. Each partition can be assigned a signal for control and a signal for status. Each of the control signals implements 
functionality for the partition. For example, clock gating and peripheral control.
The hardware process can be triggered and monitored using a set of three registers:
• Configuration register; for example, Partition n Process Configuration register
• Update register; for example, Partition n Process Update register
• Status register; for example, Partition n Status register
Similar registers exist for cores inside the partition.
The process setup and triggering procedure is shown in Figure 195. Each of the processes is independent of others and can be 
triggered or re-triggered in parallel or sequential to other processes. The triggering or re-triggering mechanism remains the same.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1757 / 5251


---
# 페이지 100

Run software
diagnostics
N
Y
N
Y
Program
PRTNn_PCONF
register
Program
PRTNn_PUPD
register
Write valid key 
sequence in
CTL_KEY register
Read
PRTNn_PUPD
register
Is
hardware
update
process
finished?
Is status
expected?
Finish
Figure 195. Partition process setup procedure
All the hardware processes are bound to finish in 512 cycles of the MC_ME configuration clock. If the actual and the expected 
status for a process does not match, then the diagnostics is left as a software responsibility. The software diagnostic can include 
further wait cycles for the status to match.
46.5 Mode transition
MC_ME implements a mode transition mechanism, whereby the mode of operation for SoC can be changed. Then module 
implements a mechanism that can lead to:
• Destructive reset
• Functional reset
• Standby mode entry
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1758 / 5251


---
# 페이지 101

Destructive reset and functional reset requests from MC_ME are non-retractable transitions. After it is initiated, the other MC_ME 
functionality is rendered unusable and bus errors are provided for upcoming access to the MC_ME register until a reset sequence 
is executed by MC_RGM. Hence, it is vital that MC_RGM should never ignore or gate the reset requests from MC_ME.
For transition into the standby mode, the software should ensure that required IP blocks such as clock sources and I/O 
communication are in their respective inactive states before initiating a standby mode transition to MC_ME. After MC_ME 
initiates a power down sequence request, it cannot be retracted. The SoC enters a standby power down sequence and then 
reenter power-up sequence even for cases where the standby wakeup happens right at the time of initiating a power-down 
sequence request.
Steps for initiating the MC_ME mode transition:
1. Setup the MODE_CONF register with the corresponding target mode bit set to logic-1.
2. Perform the same update as done in the MODE_CONF register on the CONF_UPD register.
3. Write the valid control key (0x5AF0) on the CTL_KEY register.
4. Write the valid invert control key (0xA50F) on the CTL_KEY register.
Mode transition to MC_ME is initiated, after the sequence mentioned above is completed.
In step 1, if both FUNC_RST and DEST_RST in Mode Configuration Register (MODE_CONF) are 1:
• After step 4 is complete, MC_ME initiates a mode transition to a destructive (not functional) reset.
• After the chip exits reset, MC_RGM records that both MC_ME's destructive reset and MC_ME's functional reset were the 
reset source.
 
Any hardware partition processes setup, along with mode transition, is executed in parallel to the mode transition 
of MC_ME.
  NOTE  
46.6 Standby entry
MC_ME provides hardware processes that implement shutdown sequencing of on-chip resources, such as cores and COFBs. 
The standby entry sequencing can be achieved or implemented using these hardware processes. The order of the hardware 
process is determined by the software and MC_ME. It requires no restriction in sequencing of the operation. Following is an 
example sequence for initiating a power-down sequence for entering the standby mode for SoC. The standby entry sequence 
should include (but not limited to) the following steps:
1. Setting up wakeup lines
2. Shutting down cores and COFBs
3. Switching all MC_CGM muxes to FIRC with PCFS
4. Powering down all clock sources except FIRC
5. Setting up MC_ME using the main core and initiating a standby mode transition
6. Executing WFI instruction on the main core (per Arm specification)
46.6.1 Application core shutdown
This section describes a mechanism for shutting down an application core. The sequence proposed here is extendible with the 
housekeeping tasks required for other IPs. Each of the tasks mentioned in the following sequence, can be further integrated with 
an SoC-specific task.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1759 / 5251


---
# 페이지 102

Application cores 
begin shut down 
sequence
Disable all IRQs
Outstanding 
instructions 
finished/retired
WFI executed
MC_ME receives WFI 
status
MC_ME updates 
corresponding core 
status register
Application 
core 
shutdown
MC_ME
Application core
MAIN CORE
Check for application
core WFI status in
MC_ME
WFI
received?
N
Y
Request application
cores to stop
undefined
delay
Figure 196. Application core shutdown
After the application core is shutdown, the main core can optionally decide to gate the respective core clock using the 
corresponding core clock hardware process.
46.6.2 Main core shutdown and standby entry
This section describes standby entry sequence along with the main core shutdown. This sequence should only be initiated after 
SoC is ready for entering standby and has completed all the housekeeping activities. It is necessary that the main core has 
completed all the operations pertaining to other (application cores) and is the last active core before initiating the standby entry 
sequence. See Figure 197.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1760 / 5251


---
# 페이지 103

Program wakeup IP
MC_ME waits for WFI 
signaling from main 
core
MC_PCU
MC_ME
Main core
Disable IRQs
and NMI
Program MC_ME for 
valid main core ID
Finish outstanding 
instructions
Program MC_ME for 
standby mode 
transition
Finish outstanding 
instructions
WFI executed
Power down 
sequence 
initiated
Figure 197. Standby entry sequence along with main core shutdown
 
• MC_ME initiates the power sequence to MC_PCU. This enables the main core to remain inactive (WFI state) 
until it is reset and power-up again at standby exit.
  NOTE  
46.7 MC_ME register descriptions
MC_ME implements set hardware processes that can be used by the software for changing the mode of operation for a partition. 
Following are the features of MC_ME registers:
• All registers are 32-bit wide.
• Only 32-bit read and write accesses are supported.
• Read/write accesses of less than 32 bits terminate with an error.
• Writes to read-only register fields in writable registers are ignored and do not provide an error message.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1761 / 5251


---
# 페이지 104

• Writes to read-only registers are aborted with an error message.
46.7.1 MC_ME memory map
MC_ME base address: 402D_C000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Control Key Register (CTL_KEY)
32
RW
0000_5AF0h
4h
Mode Configuration Register (MODE_CONF)
32
RW
0000_0000h
8h
Mode Update Register (MODE_UPD)
32
RW
0000_0000h
Ch
Mode Status Register (MODE_STAT)
32
R
0000_0000h
10h
Main Core ID Register (MAIN_COREID)
32
RW
0000_0000h
100h
Partition 0 Process Configuration Register (PRTN0_PCONF)
32
RW
0000_0001h
104h
Partition 0 Process Update Register (PRTN0_PUPD)
32
RW
0000_0000h
108h
Partition 0 Status Register (PRTN0_STAT)
32
R
0000_0001h
10Ch
Partition 0 Core Lockstep Control Register 
(PRTN0_CORE_LOCKSTEP)
32
RW
0000_0000h
110h
Partition 0 COFB Set 0 Clock Status Register 
(PRTN0_COFB0_STAT)
32
R
0C00_0004h
114h
Partition 0 COFB Set 1 Clock Status Register 
(PRTN0_COFB1_STAT)
32
R
0000_1000h
130h
Partition 0 COFB Set 0 Clock Enable Register 
(PRTN0_COFB0_CLKEN)
32
RW
0C00_0004h
134h
Partition 0 COFB Set 1 Clock Enable Register 
(PRTN0_COFB1_CLKEN)
32
RW
0000_1000h
140h
Partition 0 Core 0 Process Configuration Register 
(PRTN0_CORE0_PCONF)
32
RW
0000_0000h
144h
Partition 0 Core 0 Process Update Register (PRTN0_CORE0_PUPD)
32
RW
0000_0000h
148h
Partition 0 Core 0 Status Register (PRTN0_CORE0_STAT)
32
R
0000_0000h
14Ch
Partition 0 Core 0 Address Register (PRTN0_CORE0_ADDR)
32
RW
0040_0000h
160h
Partition 0 Core 1 Process Configuration Register 
(PRTN0_CORE1_PCONF)
32
RW
0000_0000h
164h
Partition 0 Core 1 Process Update Register (PRTN0_CORE1_PUPD)
32
RW
0000_0000h
168h
Partition 0 Core 1 Status Register (PRTN0_CORE1_STAT)
32
R
0000_0000h
16Ch
Partition 0 Core 1 Address Register (PRTN0_CORE1_ADDR)
32
RW
0041_0000h
188h
Partition 0 Core 2 Status Register (PRTN0_CORE2_STAT)
32
R
0000_0001h
18Ch
Partition 0 Core 2 Address Register (PRTN0_CORE2_ADDR)
32
R
00FF_FC00h
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1762 / 5251


---
# 페이지 105

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1A0h
Partition 0 Core 3 Process Configuration Register 
(PRTN0_CORE3_PCONF)
32
RW
0000_0000h
1A4h
Partition 0 Core 3 Process Update Register (PRTN0_CORE3_PUPD)
32
RW
0000_0000h
1A8h
Partition 0 Core 3 Status Register (PRTN0_CORE3_STAT)
32
R
0000_0000h
1ACh
Partition 0 Core 3 Address Register (PRTN0_CORE3_ADDR)
32
RW
0043_0000h
1C0h
Partition 0 Core 4 Process Configuration Register 
(PRTN0_CORE4_PCONF)
32
RW
0000_0000h
1C4h
Partition 0 Core 4 Process Update Register (PRTN0_CORE4_PUPD)
32
RW
0000_0000h
1C8h
Partition 0 Core 4 Status Register (PRTN0_CORE4_STAT)
32
R
0000_0000h
1CCh
Partition 0 Core 4 Address Register (PRTN0_CORE4_ADDR)
32
RW
0042_0000h
1E0h
Partition 0 Core 5 Process Configuration Register 
(PRTN0_CORE5_PCONF)
32
RW
0000_0000h
1E4h
Partition 0 Core 5 Process Update Register (PRTN0_CORE5_PUPD)
32
RW
0000_0000h
1E8h
Partition 0 Core 5 Status Register (PRTN0_CORE5_STAT)
32
R
0000_0000h
1ECh
Partition 0 Core 5 Address Register (PRTN0_CORE5_ADDR)
32
RW
0042_0000h
300h
Partition 1 Process Configuration Register (PRTN1_PCONF)
32
RW
0000_0001h
304h
Partition 1 Process Update Register (PRTN1_PUPD)
32
RW
0000_0000h
308h
Partition 1 Status Register (PRTN1_STAT)
32
R
0000_0001h
310h
Partition 1 COFB Set 0 Clock Status Register 
(PRTN1_COFB0_STAT)
32
R
5E3F_0007h
314h
Partition 1 COFB Set 1 Clock Status Register 
(PRTN1_COFB1_STAT)
32
R
7CFE_2FFCh
318h
Partition 1 COFB Set 2 Clock Status Register 
(PRTN1_COFB2_STAT)
32
R
300C_0000h
31Ch
Partition 1 COFB Set 3 Clock Status Register 
(PRTN1_COFB3_STAT)
32
R
0000_5FEEh
330h
Partition 1 COFB Set 0 Clock Enable Register 
(PRTN1_COFB0_CLKEN)
32
RW
5E3F_0007h
334h
Partition 1 COFB Set 1 Clock Enable Register 
(PRTN1_COFB1_CLKEN)
32
RW
7CFE_2FFCh
338h
Partition 1 COFB Set 2 Clock Enable Register 
(PRTN1_COFB2_CLKEN)
32
RW
300C_0000h
33Ch
Partition 1 COFB Set 3 Clock Enable Register 
(PRTN1_COFB3_CLKEN)
32
RW
0000_5FEEh
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1763 / 5251


---
# 페이지 106

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
500h
Partition 2 Process Configuration Register (PRTN2_PCONF)
32
RW
0000_0001h
504h
Partition 2 Process Update Register (PRTN2_PUPD)
32
RW
0000_0000h
508h
Partition 2 Status Register (PRTN2_STAT)
32
R
0000_0001h
510h
Partition 2 COFB Set 0 Clock Status Register 
(PRTN2_COFB0_STAT)
32
R
0600_000Fh
514h
Partition 2 COFB Set 1 Clock Status Register 
(PRTN2_COFB1_STAT)
32
R
CC00_0000h
518h
Partition 2 COFB Set 2 Clock Status Register 
(PRTN2_COFB2_STAT)
32
R
0000_0003h
51Ch
Partition 2 COFB Set 3 Clock Status Register 
(PRTN2_COFB3_STAT)
32
R
0000_0007h
530h
Partition 2 COFB Set 0 Clock Enable Register 
(PRTN2_COFB0_CLKEN)
32
RW
0600_000Fh
534h
Partition 2 COFB Set 1 Clock Enable Register 
(PRTN2_COFB1_CLKEN)
32
RW
CC00_0000h
538h
Partition 2 COFB Set 2 Clock Enable Register 
(PRTN2_COFB2_CLKEN)
32
RW
0000_0003h
46.7.2 Control Key Register (CTL_KEY)
Offset
Register
Offset
CTL_KEY
0h
Function
This register provides the mechanism to MC_ME for starting the hardware processes for the partition(s) and standby entry 
sequence. The hardware processes for partitions are triggered through the corresponding PRTNn_PCONF register. The 
mechanism to trigger the hardware processes of the respective partitions require two write operations: first time with key and 
second time with inverted key. The hexadecimal value of key is 0x5AF0 whereas for inverted key is 0xA50F.
For initiating a standby entry sequence, the MODE_CONF register is used for providing a standby entry request along with a valid 
key combination.
 
Reads from this register return a valid key value to be written next.
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1764 / 5251


---
# 페이지 107

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
KEY 
W
Reset
0
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
This field is reserved and read returns zeros.
15-0
KEY
Control key
Key for starting the hardware processes. Writes with a value other than key or inverted key are ignored. 
Reads return bit inverted value corresponding to last write.
46.7.3 Mode Configuration Register (MODE_CONF)
Offset
Register
Offset
MODE_CONF
4h
Function
This register is used for initiating a standby request or a reset event (destructive or functional) for the chip. The functional or 
destructive events are signaled to MC_RGM for further handling.
 
Software must not enable mode entry if the value of multiple fields is 1 in the MODE_CONF register.
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1765 / 5251


---
# 페이지 108

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
STAN
DBY 
0
FUNC
_RST 
DEST_
RST 
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
15
STANDBY
Standby request
Writing a logic-1 to this bit along with the MODE_UPD register configuration and followed with a valid key 
combination makes a standby entry sequence request to MC_ME.
14-2
—
Reserved
This field is reserved and read returns zeros.
1
FUNC_RST
Functional reset request
Writing a logic-1 to this bit along with the MODE_UPD register configuration and followed with a valid key 
combination makes a functional reset event signaling to MC_RGM.
0
DEST_RST
Destructive reset request
Writing a logic-1 to this bit along with the MODE_UPD register configuration and followed with a valid key 
combination makes a destructive reset event signaling to MC_RGM.
46.7.4 Mode Update Register (MODE_UPD)
Offset
Register
Offset
MODE_UPD
8h
Function
This register is used for initiating a mode change. Mode change refers to initiating a standby request, or generating a destructive 
or functional reset event to MC_RGM. Setting mode update field to logic-1, along with programming MODE_CONF registers and 
then followed by a valid key combination will generate a mode transition request.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1766 / 5251


---
# 페이지 109

 
The MODE_UPD register is implemented to make mode transition programming model the same as partition 
programming model. This is for future expansion inside MC_ME.
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
MODE
_UPD 
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
0
MODE_UPD
Mode update
Writing a logic-1 to this bit, followed by a valid key combination initiates a mode change as per the 
MODE_CONF register.
46.7.5 Mode Status Register (MODE_STAT)
Offset
Register
Offset
MODE_STAT
Ch
Function
This register provides the status of the previous mode. In case of standby exit, if the reset event status register of MC_RGM are 
set, then contents of this register should be ignored.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1767 / 5251


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
PREV_
MO...
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
0
PREV_MODE
Previous mode
This bit shows the status of the previous mode.
0b - The previous mode was reset (any reset).
1b - The previous mode was standby.
46.7.6 Main Core ID Register (MAIN_COREID)
Offset
Register
Offset
MAIN_COREID
10h
Function
This register provides the ID of the main core sequencing the operation for the standby sequence. Core ID is required for entering 
in the standby mode, and using this MC_ME locates the WFI instruction execution of the main core. The core ID in this register 
is specified by the partition index along with the core index.
 
Before initiating a standby entry sequence, the contents of this register should point to the correct main core. 
Providing non-existing or incorrect core ID leads to unpredictable hardware behavior.
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1768 / 5251


---
# 페이지 111

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
PIDX 
0
CIDX 
W
Reset
0
0
0
0
0
0
0
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
31-13
—
Reserved
This field is reserved and read returns zeros.
12-8
PIDX
Partition index
Provides the partition index of the main core. Only values 0 - 2 can be written.
7-3
—
Reserved
This field is reserved and read returns zeros.
2-0
CIDX
Core index
Provides the core index of the main core inside the partition.
46.7.7 Partition 0 Process Configuration Register (PRTN0_PCONF)
Offset
Register
Offset
PRTN0_PCONF
100h
Function
This register provides a configuration for the hardware processes corresponding to partition 0. Each of the configuration bit 
corresponds to the 'nature' of the processes; for example, enabling/disabling and the trigger is controlled by the corresponding 
field in the PRTN0_PUPD register. When valid KEY combinations are written onto the CTL_KEY register, the PRTN0_PCONF 
and PRTN0_PUPD registers are used to determine the hardware processes to be executed. These are triggered in parallel and 
independent of each other. All dependent processes should be requested one after another from the software.
 
The partition clock enable/disable are not standalone and must be done coherently in a fixed sequence. For details, 
see Software Reset Partition Turn-On Flow Chart and Software reset partition turn-off flowchart in Reset chapter.
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1769 / 5251


---
# 페이지 112

 
See chip-specific MC_ME information to check if this register is implemented on chip.
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
0
0
0
0
0
0
PCE 
W
Reset
0
0
0
0
0
0
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
31-7
—
Reserved
This field is reserved and read returns zeros.
6
—
Reserved
This field is reserved and read returns zeros.
5
—
Reserved
This field is reserved and read returns zeros.
4
—
Reserved
This field is reserved and read returns zeros.
3
—
Reserved
This field is reserved and read returns zeros.
2
—
Reserved
This field is reserved and read returns zeros.
1
—
Reserved
This field is reserved and read returns zeros.
0
PCE
Partition clock enable
This bit controls whether the clock to IPs (other than core(s)) in the partition should be enabled or disabled.
0b - Disable the clock to IPs
1b - Enable the clock to IPs
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1770 / 5251


---
# 페이지 113

46.7.8 Partition 0 Process Update Register (PRTN0_PUPD)
Offset
Register
Offset
PRTN0_PUPD
104h
Function
This register provides trigger signaling for the hardware processes corresponding to partition 0. Each of the control bit acts as 
a trigger for the corresponding hardware processes. When valid KEY combinations are written onto the CTL_KEY register, the 
hardware checks the bit fields that are programmed as logic-1 in this register, and then triggers the hardware process per the value 
in the corresponding bit field in the PRTN0_PCONF register. When the hardware process is finished the corresponding bit in this 
register is auto-cleared to logic-0.
 
See chip-specific MC_ME information to check if this register is implemented on chip.
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
0
0
0
0
0
0
PCUD 
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
6
—
Reserved
This field is reserved and read returns zeros.
5
—
Reserved
This field is reserved and read returns zeros.
4
—
Reserved
This field is reserved and read returns zeros.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1771 / 5251


---
# 페이지 114

Table continued from the previous page...
Field
Function
3
—
Reserved
This field is reserved and read returns zeros.
2
—
Reserved
This field is reserved and read returns zeros.
1
—
Reserved
This field is reserved and read returns zeros.
0
PCUD
Partition clock update
This bit controls whether the hardware processes for enabling/disabling the clock to IPs (other than core(s)) 
in the partition should be triggered or not.
0b - Do not trigger the hardware process
1b - Trigger the hardware process
46.7.9 Partition 0 Status Register (PRTN0_STAT)
Offset
Register
Offset
PRTN0_STAT
108h
Function
This register provides the current status of the control signals from the partition 0.
 
See chip-specific MC_ME information to check if this register is implemented on chip.
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
0
0
0
0
0
0
PCS 
W
Reset
0
0
0
0
0
0
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
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1772 / 5251


---
# 페이지 115

Fields
Field
Function
31-7
—
Reserved
This field is reserved and read returns zeros.
6
—
Reserved
This field is reserved and read returns zeros.
5
—
Reserved
This field is reserved and read returns zeros.
4
—
Reserved
This field is reserved and read returns zeros.
3
—
Reserved
This field is reserved and read returns zeros.
2
—
Reserved
This field is reserved and read returns zeros.
1
—
Reserved
This field is reserved and read returns zeros.
0
PCS
Partition clock status
This bit provides the status of the clock to partition.
0b - Clock is inactive
1b - Clock is active
46.7.10 Partition 0 Core Lockstep Control Register (PRTN0_CORE_LOCKSTEP)
Offset
Register
Offset
PRTN0_CORE_LOCKST
EP
10Ch
Function
This register provides the control for indicating a set of cores for lockstep execution in partition 0. Writes to this register immediately 
provide the corresponding bit to the described cores. No hardware process updates are required.
 
See chip-specific MC_ME information to check if this register is implemented on chip.
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1773 / 5251


---
# 페이지 116

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
LS2 
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
Fields
Field
Function
31-4
—
Reserved
This field is reserved and read returns zeros.
3
—
Reserved
2
LS2
Lockstep 2
This bit provides the lockstep indication to Core 4 & Core 5 in partition 0.
0b - Lockstep disabled
1b - Lockstep enabled
1
—
Reserved
0
—
Reserved
46.7.11 Partition 0 COFB Set 0 Clock Status Register (PRTN0_COFB0_STAT)
Offset
Register
Offset
PRTN0_COFB0_STAT
110h
Function
This register provides the status of set 0 of COFBs inside partition 0.
 
The reset value of this register can vary depending on the availability of active clock pulses inside partition 0.
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1774 / 5251


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
0
0
BLOC
K28 
BLOC
K27 
BLOC
K26 
0
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
0
0
0
0
0
0
0
BLOC
K3 
BLOC
K2 
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
1
0
0
Fields
Field
Function
31
—
Reserved
This field is reserved and read returns zeros.
30
—
Reserved
This field is reserved and read returns zeros.
29
—
Reserved
This field is reserved and read returns zeros.
28
BLOCK28
IP block status
This bit provides the clock status of SWT 3 in partition 0.
0b - Clock is not running.
1b - Clock is running.
27
BLOCK27
IP block status
This bit provides the clock status of block 27 in partition 0.
0b - Clock is not running.
1b - Clock is running.
26
BLOCK26
IP block status
This bit provides the clock status of block 26 in partition 0.
0b - Clock is not running.
1b - Clock is running.
25
—
Reserved
This field is reserved and read returns zeros.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1775 / 5251


---
# 페이지 118

Table continued from the previous page...
Field
Function
24
—
Reserved
This field is reserved and read returns zeros.
23
—
Reserved
This field is reserved and read returns zeros.
22
—
Reserved
This field is reserved and read returns zeros.
21
—
Reserved
This field is reserved and read returns zeros.
20
—
Reserved
This field is reserved and read returns zeros.
19
—
Reserved
This field is reserved and read returns zeros.
18
—
Reserved
This field is reserved and read returns zeros.
17
—
Reserved
This field is reserved and read returns zeros.
16
—
Reserved
This field is reserved and read returns zeros.
15
—
Reserved
This field is reserved and read returns zeros.
14
—
Reserved
This field is reserved and read returns zeros.
13
—
Reserved
This field is reserved and read returns zeros.
12
—
Reserved
This field is reserved and read returns zeros.
11
—
Reserved
This field is reserved and read returns zeros.
10
Reserved
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1776 / 5251


---
# 페이지 119

Table continued from the previous page...
Field
Function
—
This field is reserved and read returns zeros.
9
—
Reserved
This field is reserved and read returns zeros.
8
—
Reserved
This field is reserved and read returns zeros.
7
—
Reserved
This field is reserved and read returns zeros.
6
—
Reserved
This field is reserved and read returns zeros.
5
—
Reserved
This field is reserved and read returns zeros.
4
—
Reserved
This field is reserved and read returns zeros.
3
BLOCK3
IP block status
This bit provides the clock status of ERM1 in partition 0.
0b - Clock is not running.
1b - Clock is running.
2
BLOCK2
IP block status
This bit provides the clock status of block 2 in partition 0.
0b - Clock is not running.
1b - Clock is running.
1
—
Reserved
This field is reserved and read returns zeros.
0
—
Reserved
This field is reserved and read returns zeros.
46.7.12 Partition 0 COFB Set 1 Clock Status Register (PRTN0_COFB1_STAT)
Offset
Register
Offset
PRTN0_COFB1_STAT
114h
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1777 / 5251


---
# 페이지 120

Function
This register provides the status of set 1 of COFBs inside partition 0.
 
The reset value of this register can vary depending on the availability of active clock pulses inside partition 0.
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
0
0
0
0
0
0
0
0
0
0
BLOC
K52 
BLOC
K51 
BLOC
K50 
BLOC
K49 
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
BLOC
K47 
BLOC
K46 
BLOC
K45 
BLOC
K44 
0
BLOC
K42 
BLOC
K41 
BLOC
K40 
BLOC
K39 
BLOC
K38 
0
BLOC
K36 
BLOC
K35 
BLOC
K34 
BLOC
K33 
BLOC
K32 
W
Reset
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
This field is reserved and read returns zeros.
30
—
Reserved
This field is reserved and read returns zeros.
29
—
Reserved
This field is reserved and read returns zeros.
28
—
Reserved
This field is reserved and read returns zeros.
27
—
Reserved
This field is reserved and read returns zeros.
26
—
Reserved
This field is reserved and read returns zeros.
25
—
Reserved
This field is reserved and read returns zeros.
24
Reserved
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1778 / 5251


---
# 페이지 121

Table continued from the previous page...
Field
Function
—
This field is reserved and read returns zeros.
23
—
Reserved
This field is reserved and read returns zeros.
22
—
Reserved
This field is reserved and read returns zeros.
21
—
Reserved
This field is reserved and read returns zeros.
20
BLOCK52
IP block status
This bit provides the clock status of MU_4_MUB in partition 0.
0b - Clock is not running.
1b - Clock is running.
19
BLOCK51
IP block status
This bit provides the clock status of MU_4_MUA in partition 0.
0b - Clock is not running.
1b - Clock is running.
18
BLOCK50
IP block status
This bit provides the clock status of MU_3_MUB in partition 0.
0b - Clock is not running.
1b - Clock is running.
17
BLOCK49
IP block status
This bit provides the clock status of MU_3_MUA in partition 0.
0b - Clock is not running.
1b - Clock is running.
16
—
Reserved
This field is reserved and read returns zeros.
15
BLOCK47
IP block status
This bit provides the clock status of MU_2_MUB in partition 0.
0b - Clock is not running.
1b - Clock is running.
14
IP block status
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1779 / 5251


---
# 페이지 122

Table continued from the previous page...
Field
Function
BLOCK46
This bit provides the clock status of MU_2_MUA in partition 0.
0b - Clock is not running.
1b - Clock is running.
13
BLOCK45
IP block status
This bit provides the clock status of PIT_1 in partition 0.
0b - Clock is not running.
1b - Clock is running.
12
BLOCK44
IP block status
This bit provides the clock status of PIT_0 in partition 0.
0b - Clock is not running.
1b - Clock is running.
11
—
Reserved
This field is reserved and read returns zeros.
10
BLOCK42
IP block status
This bit provides the clock status of ADC_2 in partition 0.
0b - Clock is not running.
1b - Clock is running.
9
BLOCK41
IP block status
This bit provides the clock status of ADC_1 in partition 0.
0b - Clock is not running.
1b - Clock is running.
8
BLOCK40
IP block status
This bit provides the clock status of ADC_0 in partition 0.
0b - Clock is not running.
1b - Clock is running.
7
BLOCK39
IP block status
This bit provides the clock status of LCU_1 in partition 0.
0b - Clock is not running.
1b - Clock is running.
6
BLOCK38
IP block status
This bit provides the clock status of LCU_0 in partition 0.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1780 / 5251


---
# 페이지 123

Table continued from the previous page...
Field
Function
0b - Clock is not running.
1b - Clock is running.
5
—
Reserved
This field is reserved and read returns zeros.
4
BLOCK36
IP block status
This bit provides the clock status of eMIOS_2 in partition 0.
0b - Clock is not running.
1b - Clock is running.
3
BLOCK35
IP block status
This bit provides the clock status of eMIOS_1 in partition 0.
0b - Clock is not running.
1b - Clock is running.
2
BLOCK34
IP block status
This bit provides the clock status of eMIOS_0 in partition 0.
0b - Clock is not running.
1b - Clock is running.
1
BLOCK33
IP block status
This bit provides the clock status of BCTU in partition 0.
0b - Clock is not running.
1b - Clock is running.
0
BLOCK32
IP block status
This bit provides the clock status of TRGMUX in partition 0.
0b - Clock is not running.
1b - Clock is running.
46.7.13 Partition 0 COFB Set 0 Clock Enable Register (PRTN0_COFB0_CLKEN)
Offset
Register
Offset
PRTN0_COFB0_CLKEN
130h
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1781 / 5251


---
# 페이지 124

Function
This register provides clock control signaling to the individual COFBs in set 0 inside partition 0. Whenever a partition clock enable 
(non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock 
to the corresponding block in the partition.
 
The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific 
MC_ME information for clock source availability.
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
0
0
REQ2
8 
0
0
0
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
0
0
0
0
0
0
0
REQ3 
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
1
0
0
Fields
Field
Function
31
—
Reserved
This field is reserved and read returns zeros.
30
—
Reserved
This field is reserved and read returns zeros.
29
—
Reserved
This field is reserved and read returns zeros.
28
REQ28
Clock enable
This bit provides the clock enable control for SWT 3 in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
27
—
Reserved
This field is reserved and read returns zeros.
26
—
Reserved
This field is reserved and read returns zeros.
25
Reserved
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1782 / 5251


---
# 페이지 125

Table continued from the previous page...
Field
Function
—
This field is reserved and read returns zeros.
24
—
Reserved
This field is reserved and read returns zeros.
23
—
Reserved
This field is reserved and read returns zeros.
22
—
Reserved
This field is reserved and read returns zeros.
21
—
Reserved
This field is reserved and read returns zeros.
20
—
Reserved
This field is reserved and read returns zeros.
19
—
Reserved
This field is reserved and read returns zeros.
18
—
Reserved
This field is reserved and read returns zeros.
17
—
Reserved
This field is reserved and read returns zeros.
16
—
Reserved
This field is reserved and read returns zeros.
15
—
Reserved
This field is reserved and read returns zeros.
14
—
Reserved
This field is reserved and read returns zeros.
13
—
Reserved
This field is reserved and read returns zeros.
12
—
Reserved
This field is reserved and read returns zeros.
11
—
Reserved
This field is reserved and read returns zeros.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1783 / 5251


---
# 페이지 126

Table continued from the previous page...
Field
Function
10
—
Reserved
This field is reserved and read returns zeros.
9
—
Reserved
This field is reserved and read returns zeros.
8
—
Reserved
This field is reserved and read returns zeros.
7
—
Reserved
This field is reserved and read returns zeros.
6
—
Reserved
This field is reserved and read returns zeros.
5
—
Reserved
This field is reserved and read returns zeros.
4
—
Reserved
This field is reserved and read returns zeros.
3
REQ3
Clock enable
This bit provides the clock enable control for ERM1 in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
2
—
Reserved
This field is reserved and read returns zeros.
1
—
Reserved
This field is reserved and read returns zeros.
0
—
Reserved
This field is reserved and read returns zeros.
46.7.14 Partition 0 COFB Set 1 Clock Enable Register (PRTN0_COFB1_CLKEN)
Offset
Register
Offset
PRTN0_COFB1_CLKEN
134h
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1784 / 5251


---
# 페이지 127

Function
This register provides clock control signaling to the individual COFBs in set 1 inside partition 0. Whenever a partition clock enable 
(non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock 
to the corresponding block in the partition.
 
The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific 
MC_ME information for clock source availability.
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
0
0
0
0
0
0
0
0
0
0
REQ5
2 
REQ5
1 
REQ5
0 
REQ4
9 
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
REQ4
7 
REQ4
6 
REQ4
5 
REQ4
4 
0
REQ4
2 
REQ4
1 
REQ4
0 
REQ3
9 
REQ3
8 
0
REQ3
6 
REQ3
5 
REQ3
4 
REQ3
3 
REQ3
2 
W
Reset
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
This field is reserved and read returns zeros.
30
—
Reserved
This field is reserved and read returns zeros.
29
—
Reserved
This field is reserved and read returns zeros.
28
—
Reserved
This field is reserved and read returns zeros.
27
—
Reserved
This field is reserved and read returns zeros.
26
—
Reserved
This field is reserved and read returns zeros.
25
—
Reserved
This field is reserved and read returns zeros.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1785 / 5251


---
# 페이지 128

Table continued from the previous page...
Field
Function
24
—
Reserved
This field is reserved and read returns zeros.
23
—
Reserved
This field is reserved and read returns zeros.
22
—
Reserved
This field is reserved and read returns zeros.
21
—
Reserved
This field is reserved and read returns zeros.
20
REQ52
Clock enable
This bit provides the clock enable control for MU_4_MUB in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
19
REQ51
Clock enable
This bit provides the clock enable control for MU_4_MUA in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
18
REQ50
Clock enable
This bit provides the clock enable control for MU_3_MUB in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
17
REQ49
Clock enable
This bit provides the clock enable control for MU_3_MUA in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
16
—
Reserved
This field is reserved and read returns zeros.
15
REQ47
Clock enable
This bit provides the clock enable control for MU_2_MUB in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1786 / 5251


---
# 페이지 129

Table continued from the previous page...
Field
Function
14
REQ46
Clock enable
This bit provides the clock enable control for MU_2_MUA in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
13
REQ45
Clock enable
This bit provides the clock enable control for PIT_1 in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
12
REQ44
Clock enable
This bit provides the clock enable control for PIT_0 in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
11
—
Reserved
This field is reserved and read returns zeros.
10
REQ42
Clock enable
This bit provides the clock enable control for ADC_2 in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
9
REQ41
Clock enable
This bit provides the clock enable control for ADC_1 in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
8
REQ40
Clock enable
This bit provides the clock enable control for ADC_0 in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
7
REQ39
Clock enable
This bit provides the clock enable control for LCU_1 in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
6
Clock enable
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1787 / 5251


---
# 페이지 130

Table continued from the previous page...
Field
Function
REQ38
This bit provides the clock enable control for LCU_0 in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
5
—
Reserved
This field is reserved and read returns zeros.
4
REQ36
Clock enable
This bit provides the clock enable control for eMIOS_2 in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
3
REQ35
Clock enable
This bit provides the clock enable control for eMIOS_1 in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
2
REQ34
Clock enable
This bit provides the clock enable control for eMIOS_0 in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
1
REQ33
Clock enable
This bit provides the clock enable control for BCTU in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
0
REQ32
Clock enable
This bit provides the clock enable control for TRGMUX in partition 0.
0b - Clock is turned off.
1b - Clock is turned on.
46.7.15 Partition 0 Core 0 Process Configuration Register (PRTN0_CORE0_PCONF)
Offset
Register
Offset
PRTN0_CORE0_PCONF 140h
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1788 / 5251


---
# 페이지 131

Function
This register provides configurations for the Core 0 hardware processes corresponding to partition 0. Each of the configuration 
bit corresponds to the 'nature' of the processes; for example, enabling/disabling and the trigger is controlled by the corresponding 
field in the PRTN0_CORE0_PUPD register. When valid KEY combinations are written onto the CTL_KEY register, the 
PRTN0_CORE0_PUPD and PRTN0_CORE0_PCONF registers are used to determine the hardware processes to be executed. 
These processes are triggered in parallel and are independent of each other. All dependent processes should be requested one 
after another from the software.
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
CCE 
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
0
CCE
Core 0 clock enable
This bit controls whether the clock to Core 0 in partition 0 should be enabled or disabled.
0b - Disable the core clock
1b - Enable the core clock
46.7.16 Partition 0 Core 0 Process Update Register (PRTN0_CORE0_PUPD)
Offset
Register
Offset
PRTN0_CORE0_PUPD
144h
Function
This register provides trigger signaling for the core hardware processes corresponding to partition 0. Each of the control bit acts 
as a trigger for the corresponding hardware processes. When valid KEY combinations are written onto the CTL_KEY register, the 
hardware checks the bit fields that are programmed as logic-1 in this register, and then triggers the hardware process per the value 
in the corresponding bit field in the PRTN0_CORE0_PCONF register. When the hardware process is finished, the corresponding 
bit in this register is auto-cleared to logic-0.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1789 / 5251


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
W
Reset
0
0
0
0
0
0
0
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
CCUP
D 
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
0
CCUPD
Core 0 clock update
This bit controls whether the hardware processes for enabling/disabling the clock to Core 0 in the partition 
0 should be triggered or not.
0b - Do not trigger the hardware process
1b - Trigger the hardware process
46.7.17 Partition 0 Core 0 Status Register (PRTN0_CORE0_STAT)
Offset
Register
Offset
PRTN0_CORE0_STAT
148h
Function
This register provides the status corresponding to Core 0 in partition 0. The status signal corresponds to clock states and the WFI 
signal included from Core 0.
 
The value held in WFI field of this STATUS register is "current" value of the WFISTANDBY signal from the core. 
Hence out-of-reset, the reset value of this field will depend on the status of the core (core is running or in low power 
mode). So, simple reset read sweep will always return current value (different than other register reads such as on 
control registers).
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1790 / 5251


---
# 페이지 133

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
WFI 
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
CCS 
W
Reset
0
0
0
0
0
0
0
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
WFI
Wait for interrupt status
This bit provides the WFI status approaching from Core 0 in partition 0.
0b - No WFI executed
1b - WFI executed
30-1
—
Reserved
This field is reserved and read returns zeros.
0
CCS
Core 0 clock process status
This bit provides the status of the clock corresponding to core clock enablement/disablement.
0b - Clock is inactive.
1b - Clock is active.
46.7.18 Partition 0 Core 0 Address Register (PRTN0_CORE0_ADDR)
Offset
Register
Offset
PRTN0_CORE0_ADDR
14Ch
Function
This register contains the boot address for Core 0 in partition 0.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1791 / 5251


---
# 페이지 134

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
ADDR 
W
Reset
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
ADDR 
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
31-2
ADDR
Address
Core 0 boot address
1-0
—
Reserved
This field is reserved and read returns zeros.
46.7.19 Partition 0 Core 1 Process Configuration Register (PRTN0_CORE1_PCONF)
Offset
Register
Offset
PRTN0_CORE1_PCONF 160h
Function
This register provides configurations for the Core 1 hardware processes corresponding to partition 0. Each of the configuration 
bit corresponds to the 'nature' of the processes; for example, enabling/disabling and the trigger is controlled by the corresponding 
field in the PRTN0_CORE1_PUPD register. When valid KEY combinations are written onto the CTL_KEY register, the 
PRTN0_CORE1_PUPD and PRTN0_CORE1_PCONF registers are used to determine the hardware processes to be executed. 
These processes are triggered in parallel and are independent of each other. All dependent processes should be requested one 
after another from the software.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1792 / 5251


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
W
Reset
0
0
0
0
0
0
0
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
CCE 
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
0
CCE
Core 1 clock enable
This bit controls whether the clock to Core 1 in partition 0 should be enabled or disabled.
0b - Disable the core clock
1b - Enable the core clock
46.7.20 Partition 0 Core 1 Process Update Register (PRTN0_CORE1_PUPD)
Offset
Register
Offset
PRTN0_CORE1_PUPD
164h
Function
This register provides trigger signaling for the core hardware processes corresponding to partition 0. Each of the control bit acts 
as a trigger for the corresponding hardware processes. When valid KEY combinations are written onto the CTL_KEY register, the 
hardware checks the bit fields that are programmed as logic-1 in this register, and then triggers the hardware process per the value 
in the corresponding bit field in the PRTN0_CORE1_PCONF register. When the hardware process is finished, the corresponding 
bit in this register is auto-cleared to logic-0.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1793 / 5251


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
CCUP
D 
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
0
CCUPD
Core 1 clock update
This bit controls whether the hardware processes for enabling/disabling the clock to Core 1 in the partition 
0 should be triggered or not.
0b - Do not trigger the hardware process
1b - Trigger the hardware process
46.7.21 Partition 0 Core 1 Status Register (PRTN0_CORE1_STAT)
Offset
Register
Offset
PRTN0_CORE1_STAT
168h
Function
This register provides the status corresponding to Core 1 in partition 0. The status signal corresponds to clock states and the WFI 
signal included from Core 1.
 
The value held in WFI field of this STATUS register is "current" value of the WFISTANDBY signal from the core. 
Hence out-of-reset, the reset value of this field will depend on the status of the core (core is running or in low power 
mode). So, simple reset read sweep will always return current value (different than other register reads such as on 
control registers).
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1794 / 5251


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
WFI 
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
CCS 
W
Reset
0
0
0
0
0
0
0
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
WFI
Wait for interrupt status
This bit provides the WFI status approaching from Core 1 in partition 0.
0b - No WFI executed
1b - WFI executed
30-1
—
Reserved
This field is reserved and read returns zeros.
0
CCS
Core 1 clock process status
This bit provides the status of the clock corresponding to core clock enablement/disablement.
0b - Clock is inactive.
1b - Clock is active.
46.7.22 Partition 0 Core 1 Address Register (PRTN0_CORE1_ADDR)
Offset
Register
Offset
PRTN0_CORE1_ADDR
16Ch
Function
This register contains the boot address for Core 1 in partition 0.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1795 / 5251


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
ADDR 
W
Reset
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
ADDR 
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
31-2
ADDR
Address
Core 1 boot address
1-0
—
Reserved
This field is reserved and read returns zeros.
46.7.23 Partition 0 Core 2 Status Register (PRTN0_CORE2_STAT)
Offset
Register
Offset
PRTN0_CORE2_STAT
188h
Function
This register provides the status corresponding to Core 2 in partition 0. The status signal corresponds to clock states and the WFI 
signal included from Core 2.
 
The value held in WFI field of this STATUS register is "current" value of the WFISTANDBY signal from the core. 
Hence out-of-reset, the reset value of this field will depend on the status of the core (core is running or in low power 
mode). So, simple reset read sweep will always return current value (different than other register reads such as on 
control registers).
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1796 / 5251


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
WFI 
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
CCS 
W
Reset
0
0
0
0
0
0
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
WFI
Wait for interrupt status
This bit provides the WFI status approaching from Core 2 in partition 0.
0b - No WFI executed
1b - WFI executed
30-1
—
Reserved
This field is reserved and read returns zeros.
0
CCS
Core 2 clock process status
This bit provides the status of the clock corresponding to core clock enablement/disablement.
1b - Clock is active.
46.7.24 Partition 0 Core 2 Address Register (PRTN0_CORE2_ADDR)
Offset
Register
Offset
PRTN0_CORE2_ADDR
18Ch
Function
This register contains the boot address for Core 2 in partition 0.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1797 / 5251


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
ADDR 
W
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
ADDR 
0
W
Reset
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
0
0
Fields
Field
Function
31-2
ADDR
Address
Core 2 boot address
1-0
—
Reserved
This field is reserved and read returns zeros.
46.7.25 Partition 0 Core 3 Process Configuration Register (PRTN0_CORE3_PCONF)
Offset
Register
Offset
PRTN0_CORE3_PCONF 1A0h
Function
This register provides configurations for the Core 3 hardware processes corresponding to partition 0. Each of the configuration 
bit corresponds to the 'nature' of the processes; for example, enabling/disabling and the trigger is controlled by the corresponding 
field in the PRTN0_CORE3_PUPD register. When valid KEY combinations are written onto the CTL_KEY register, the 
PRTN0_CORE3_PUPD and PRTN0_CORE3_PCONF registers are used to determine the hardware processes to be executed. 
These processes are triggered in parallel and are independent of each other. All dependent processes should be requested one 
after another from the software.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1798 / 5251


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
W
Reset
0
0
0
0
0
0
0
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
CCE 
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
0
CCE
Core 3 clock enable
This bit controls whether the clock to Core 3 in partition 0 should be enabled or disabled.
0b - Disable the core clock
1b - Enable the core clock
46.7.26 Partition 0 Core 3 Process Update Register (PRTN0_CORE3_PUPD)
Offset
Register
Offset
PRTN0_CORE3_PUPD
1A4h
Function
This register provides trigger signaling for the core hardware processes corresponding to partition 0. Each of the control bit acts 
as a trigger for the corresponding hardware processes. When valid KEY combinations are written onto the CTL_KEY register, the 
hardware checks the bit fields that are programmed as logic-1 in this register, and then triggers the hardware process per the value 
in the corresponding bit field in the PRTN0_CORE3_PCONF register. When the hardware process is finished, the corresponding 
bit in this register is auto-cleared to logic-0.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1799 / 5251


---
# 페이지 142

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
CCUP
D 
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
0
CCUPD
Core 3 clock update
This bit controls whether the hardware processes for enabling/disabling the clock to Core 3 in the partition 
0 should be triggered or not.
0b - Do not trigger the hardware process
1b - Trigger the hardware process
46.7.27 Partition 0 Core 3 Status Register (PRTN0_CORE3_STAT)
Offset
Register
Offset
PRTN0_CORE3_STAT
1A8h
Function
This register provides the status corresponding to Core 3 in partition 0. The status signal corresponds to clock states and the WFI 
signal included from Core 3.
 
The value held in WFI field of this STATUS register is "current" value of the WFISTANDBY signal from the core. 
Hence out-of-reset, the reset value of this field will depend on the status of the core (core is running or in low power 
mode). So, simple reset read sweep will always return current value (different than other register reads such as on 
control registers).
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1800 / 5251


---
# 페이지 143

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
WFI 
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
CCS 
W
Reset
0
0
0
0
0
0
0
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
WFI
Wait for interrupt status
This bit provides the WFI status approaching from Core 3 in partition 0.
0b - No WFI executed
1b - WFI executed
30-1
—
Reserved
This field is reserved and read returns zeros.
0
CCS
Core 3 clock process status
This bit provides the status of the clock corresponding to core clock enablement/disablement.
0b - Clock is inactive.
1b - Clock is active.
46.7.28 Partition 0 Core 3 Address Register (PRTN0_CORE3_ADDR)
Offset
Register
Offset
PRTN0_CORE3_ADDR
1ACh
Function
This register contains the boot address for Core 3 in partition 0.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1801 / 5251


---
# 페이지 144

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
ADDR 
W
Reset
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
ADDR 
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
31-2
ADDR
Address
Core 3 boot address
1-0
—
Reserved
This field is reserved and read returns zeros.
46.7.29 Partition 0 Core 4 Process Configuration Register (PRTN0_CORE4_PCONF)
Offset
Register
Offset
PRTN0_CORE4_PCONF 1C0h
Function
This register provides configurations for the Core 4 hardware processes corresponding to partition 0. Each of the configuration 
bit corresponds to the 'nature' of the processes; for example, enabling/disabling and the trigger is controlled by the corresponding 
field in the PRTN0_CORE4_PUPD register. When valid KEY combinations are written onto the CTL_KEY register, the 
PRTN0_CORE4_PUPD and PRTN0_CORE4_PCONF registers are used to determine the hardware processes to be executed. 
These processes are triggered in parallel and are independent of each other. All dependent processes should be requested one 
after another from the software.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1802 / 5251


---
# 페이지 145

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
CCE 
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
0
CCE
Core 4 clock enable
This bit controls whether the clock to Core 4 in partition 0 should be enabled or disabled.
0b - Disable the core clock
1b - Enable the core clock
46.7.30 Partition 0 Core 4 Process Update Register (PRTN0_CORE4_PUPD)
Offset
Register
Offset
PRTN0_CORE4_PUPD
1C4h
Function
This register provides trigger signaling for the core hardware processes corresponding to partition 0. Each of the control bit acts 
as a trigger for the corresponding hardware processes. When valid KEY combinations are written onto the CTL_KEY register, the 
hardware checks the bit fields that are programmed as logic-1 in this register, and then triggers the hardware process per the value 
in the corresponding bit field in the PRTN0_CORE4_PCONF register. When the hardware process is finished, the corresponding 
bit in this register is auto-cleared to logic-0.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1803 / 5251


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
CCUP
D 
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
0
CCUPD
Core 4 clock update
This bit controls whether the hardware processes for enabling/disabling the clock to Core 4 in the partition 
0 should be triggered or not.
0b - Do not trigger the hardware process
1b - Trigger the hardware process
46.7.31 Partition 0 Core 4 Status Register (PRTN0_CORE4_STAT)
Offset
Register
Offset
PRTN0_CORE4_STAT
1C8h
Function
This register provides the status corresponding to Core 4 in partition 0. The status signal corresponds to clock states and the WFI 
signal included from Core 4.
 
The value held in WFI field of this STATUS register is "current" value of the WFISTANDBY signal from the core. 
Hence out-of-reset, the reset value of this field will depend on the status of the core (core is running or in low power 
mode). So, simple reset read sweep will always return current value (different than other register reads such as on 
control registers).
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1804 / 5251


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
WFI 
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
CCS 
W
Reset
0
0
0
0
0
0
0
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
WFI
Wait for interrupt status
This bit provides the WFI status approaching from Core 4 in partition 0.
0b - No WFI executed
1b - WFI executed
30-1
—
Reserved
This field is reserved and read returns zeros.
0
CCS
Core 4 clock process status
This bit provides the status of the clock corresponding to core clock enablement/disablement.
0b - Clock is inactive.
1b - Clock is active.
46.7.32 Partition 0 Core 4 Address Register (PRTN0_CORE4_ADDR)
Offset
Register
Offset
PRTN0_CORE4_ADDR
1CCh
Function
This register contains the boot address for Core 4 in partition 0.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1805 / 5251


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
ADDR 
W
Reset
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
ADDR 
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
31-2
ADDR
Address
Core 4 boot address
1-0
—
Reserved
This field is reserved and read returns zeros.
46.7.33 Partition 0 Core 5 Process Configuration Register (PRTN0_CORE5_PCONF)
Offset
Register
Offset
PRTN0_CORE5_PCONF 1E0h
Function
This register provides configurations for the Core 5 hardware processes corresponding to partition 0. Each of the configuration 
bit corresponds to the 'nature' of the processes; for example, enabling/disabling and the trigger is controlled by the corresponding 
field in the PRTN0_CORE5_PUPD register. When valid KEY combinations are written onto the CTL_KEY register, the 
PRTN0_CORE5_PUPD and PRTN0_CORE5_PCONF registers are used to determine the hardware processes to be executed. 
These processes are triggered in parallel and are independent of each other. All dependent processes should be requested one 
after another from the software.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1806 / 5251


---
# 페이지 149

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
CCE 
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
0
CCE
Core 5 clock enable
This bit controls whether the clock to Core 5 in partition 0 should be enabled or disabled.
0b - Disable the core clock
1b - Enable the core clock
46.7.34 Partition 0 Core 5 Process Update Register (PRTN0_CORE5_PUPD)
Offset
Register
Offset
PRTN0_CORE5_PUPD
1E4h
Function
This register provides trigger signaling for the core hardware processes corresponding to partition 0. Each of the control bit acts 
as a trigger for the corresponding hardware processes. When valid KEY combinations are written onto the CTL_KEY register, the 
hardware checks the bit fields that are programmed as logic-1 in this register, and then triggers the hardware process per the value 
in the corresponding bit field in the PRTN0_CORE5_PCONF register. When the hardware process is finished, the corresponding 
bit in this register is auto-cleared to logic-0.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1807 / 5251


---
# 페이지 150

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
CCUP
D 
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
0
CCUPD
Core 5 clock update
This bit controls whether the hardware processes for enabling/disabling the clock to Core 5 in the partition 
0 should be triggered or not.
0b - Do not trigger the hardware process
1b - Trigger the hardware process
46.7.35 Partition 0 Core 5 Status Register (PRTN0_CORE5_STAT)
Offset
Register
Offset
PRTN0_CORE5_STAT
1E8h
Function
This register provides the status corresponding to Core 5 in partition 0. The status signal corresponds to clock states and the WFI 
signal included from Core 5.
 
The value held in WFI field of this STATUS register is "current" value of the WFISTANDBY signal from the core. 
Hence out-of-reset, the reset value of this field will depend on the status of the core (core is running or in low power 
mode). So, simple reset read sweep will always return current value (different than other register reads such as on 
control registers).
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1808 / 5251


---
# 페이지 151

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
WFI 
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
CCS 
W
Reset
0
0
0
0
0
0
0
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
WFI
Wait for interrupt status
This bit provides the WFI status approaching from Core 5 in partition 0.
0b - No WFI executed
1b - WFI executed
30-1
—
Reserved
This field is reserved and read returns zeros.
0
CCS
Core 5 clock process status
This bit provides the status of the clock corresponding to core clock enablement/disablement.
0b - Clock is inactive.
1b - Clock is active.
46.7.36 Partition 0 Core 5 Address Register (PRTN0_CORE5_ADDR)
Offset
Register
Offset
PRTN0_CORE5_ADDR
1ECh
Function
This register contains the boot address for Core 5 in partition 0.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1809 / 5251


---
# 페이지 152

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
ADDR 
W
Reset
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
ADDR 
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
31-2
ADDR
Address
Core 5 boot address
1-0
—
Reserved
This field is reserved and read returns zeros.
46.7.37 Partition 1 Process Configuration Register (PRTN1_PCONF)
Offset
Register
Offset
PRTN1_PCONF
300h
Function
This register provides a configuration for the hardware processes corresponding to partition 1. Each of the configuration bit 
corresponds to the 'nature' of the processes; for example, enabling/disabling and the trigger is controlled by the corresponding 
field in the PRTN1_PUPD register. When valid KEY combinations are written onto the CTL_KEY register, the PRTN1_PCONF 
and PRTN1_PUPD registers are used to determine the hardware processes to be executed. These are triggered in parallel and 
independent of each other. All dependent processes should be requested one after another from the software.
 
The partition clock enable/disable are not standalone and must be done coherently in a fixed sequence. For details, 
see Software Reset Partition Turn-On Flow Chart and Software reset partition turn-off flowchart in Reset chapter.
  NOTE  
 
See chip-specific MC_ME information to check if this register is implemented on chip.
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1810 / 5251


---
# 페이지 153

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
0
0
0
0
PCE 
W
Reset
0
0
0
0
0
0
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
31-7
—
Reserved
This field is reserved and read returns zeros.
6
—
Reserved
This field is reserved and read returns zeros.
5
—
Reserved
This field is reserved and read returns zeros.
4
—
Reserved
This field is reserved and read returns zeros.
3
—
Reserved
This field is reserved and read returns zeros.
2
—
Reserved
This field is reserved and read returns zeros.
1
—
Reserved
This field is reserved and read returns zeros.
0
PCE
Partition clock enable
This bit controls whether the clock to IPs (other than core(s)) in the partition should be enabled or disabled.
0b - Disable the clock to IPs
1b - Enable the clock to IPs
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1811 / 5251


---
# 페이지 154

46.7.38 Partition 1 Process Update Register (PRTN1_PUPD)
Offset
Register
Offset
PRTN1_PUPD
304h
Function
This register provides trigger signaling for the hardware processes corresponding to partition 1. Each of the control bit acts as 
a trigger for the corresponding hardware processes. When valid KEY combinations are written onto the CTL_KEY register, the 
hardware checks the bit fields that are programmed as logic-1 in this register, and then triggers the hardware process per the value 
in the corresponding bit field in the PRTN1_PCONF register. When the hardware process is finished the corresponding bit in this 
register is auto-cleared to logic-0.
 
See chip-specific MC_ME information to check if this register is implemented on chip.
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
0
0
0
0
0
0
PCUD 
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
6
—
Reserved
This field is reserved and read returns zeros.
5
—
Reserved
This field is reserved and read returns zeros.
4
—
Reserved
This field is reserved and read returns zeros.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1812 / 5251


---
# 페이지 155

Table continued from the previous page...
Field
Function
3
—
Reserved
This field is reserved and read returns zeros.
2
—
Reserved
This field is reserved and read returns zeros.
1
—
Reserved
This field is reserved and read returns zeros.
0
PCUD
Partition clock update
This bit controls whether the hardware processes for enabling/disabling the clock to IPs (other than core(s)) 
in the partition should be triggered or not.
0b - Do not trigger the hardware process
1b - Trigger the hardware process
46.7.39 Partition 1 Status Register (PRTN1_STAT)
Offset
Register
Offset
PRTN1_STAT
308h
Function
This register provides the current status of the control signals from the partition 1.
 
See chip-specific MC_ME information to check if this register is implemented on chip.
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
0
0
0
0
0
0
PCS 
W
Reset
0
0
0
0
0
0
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
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1813 / 5251


---
# 페이지 156

Fields
Field
Function
31-7
—
Reserved
This field is reserved and read returns zeros.
6
—
Reserved
This field is reserved and read returns zeros.
5
—
Reserved
This field is reserved and read returns zeros.
4
—
Reserved
This field is reserved and read returns zeros.
3
—
Reserved
This field is reserved and read returns zeros.
2
—
Reserved
This field is reserved and read returns zeros.
1
—
Reserved
This field is reserved and read returns zeros.
0
PCS
Partition clock status
This bit provides the status of the clock to partition.
0b - Clock is inactive
1b - Clock is active
46.7.40 Partition 1 COFB Set 0 Clock Status Register (PRTN1_COFB0_STAT)
Offset
Register
Offset
PRTN1_COFB0_STAT
310h
Function
This register provides the status of set 0 of COFBs inside partition 1.
 
The reset value of this register can vary depending on the availability of active clock pulses inside partition 1.
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1814 / 5251


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
BLOC
K31 
BLOC
K30 
BLOC
K29 
BLOC
K28 
BLOC
K27 
BLOC
K26 
BLOC
K25 
BLOC
K24 
BLOC
K23 
0
BLOC
K21 
BLOC
K20 
BLOC
K19 
BLOC
K18 
BLOC
K17 
BLOC
K16 
W
Reset
0
1
0
1
1
1
1
0
0
0
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
BLOC
K15 
BLOC
K14 
BLOC
K13 
BLOC
K12 
BLOC
K11 
BLOC
K10 
BLOC
K9 
BLOC
K8 
BLOC
K7 
BLOC
K6 
BLOC
K5 
BLOC
K4 
BLOC
K3 
BLOC
K2 
BLOC
K1 
BLOC
K0 
W
Reset
0
0
0
0
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
Fields
Field
Function
31
BLOCK31
IP block status
This bit provides the clock status of INTM in partition 1.
0b - Clock is not running.
1b - Clock is running.
30
BLOCK30
IP block status
This bit provides the clock status of block 30 in partition 1.
0b - Clock is not running.
1b - Clock is running.
29
BLOCK29
IP block status
This bit provides the clock status of STM 0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
28
BLOCK28
IP block status
This bit provides the clock status of SWT 0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
27
BLOCK27
IP block status
This bit provides the clock status of block 27 in partition 1.
0b - Clock is not running.
1b - Clock is running.
26
IP block status
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1815 / 5251


---
# 페이지 158

Table continued from the previous page...
Field
Function
BLOCK26
This bit provides the clock status of block 26 in partition 1.
0b - Clock is not running.
1b - Clock is running.
25
BLOCK25
IP block status
This bit provides the clock status of block 25 in partition 1.
0b - Clock is not running.
1b - Clock is running.
24
BLOCK24
IP block status
This bit provides the clock status of MSCM in partition 1.
0b - Clock is not running.
1b - Clock is running.
23
BLOCK23
IP block status
This bit provides the clock status of ERM_0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
22
—
Reserved
This field is reserved and read returns zeros.
21
BLOCK21
IP block status
This bit provides the clock status of SDA-AP and Debug APB Paged Area in partition 1.
0b - Clock is not running.
1b - Clock is running.
20
BLOCK20
IP block status
This bit provides the clock status of block 20 in partition 1.
0b - Clock is not running.
1b - Clock is running.
19
BLOCK19
IP block status
This bit provides the clock status of block 19 in partition 1.
0b - Clock is not running.
1b - Clock is running.
18
BLOCK18
IP block status
This bit provides the clock status of block 18 in partition 1.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1816 / 5251


---
# 페이지 159

Table continued from the previous page...
Field
Function
0b - Clock is not running.
1b - Clock is running.
17
BLOCK17
IP block status
This bit provides the clock status of block 17 in partition 1.
0b - Clock is not running.
1b - Clock is running.
16
BLOCK16
IP block status
This bit provides the clock status of block 16 in partition 1.
0b - Clock is not running.
1b - Clock is running.
15
BLOCK15
IP block status
This bit provides the clock status of eDMA TCD 11 in partition 1.
0b - Clock is not running.
1b - Clock is running.
14
BLOCK14
IP block status
This bit provides the clock status of eDMA TCD 10 in partition 1.
0b - Clock is not running.
1b - Clock is running.
13
BLOCK13
IP block status
This bit provides the clock status of eDMA TCD 9 in partition 1.
0b - Clock is not running.
1b - Clock is running.
12
BLOCK12
IP block status
This bit provides the clock status of eDMA TCD 8 in partition 1.
0b - Clock is not running.
1b - Clock is running.
11
BLOCK11
IP block status
This bit provides the clock status of eDMA TCD 7 in partition 1.
0b - Clock is not running.
1b - Clock is running.
10
IP block status
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1817 / 5251


---
# 페이지 160

Table continued from the previous page...
Field
Function
BLOCK10
This bit provides the clock status of eDMA TCD 6 in partition 1.
0b - Clock is not running.
1b - Clock is running.
9
BLOCK9
IP block status
This bit provides the clock status of eDMA TCD 5 in partition 1.
0b - Clock is not running.
1b - Clock is running.
8
BLOCK8
IP block status
This bit provides the clock status of eDMA TCD 4 in partition 1.
0b - Clock is not running.
1b - Clock is running.
7
BLOCK7
IP block status
This bit provides the clock status of eDMA TCD 3 in partition 1.
0b - Clock is not running.
1b - Clock is running.
6
BLOCK6
IP block status
This bit provides the clock status of eDMA TCD 2 in partition 1.
0b - Clock is not running.
1b - Clock is running.
5
BLOCK5
IP block status
This bit provides the clock status of eDMA TCD 1 in partition 1.
0b - Clock is not running.
1b - Clock is running.
4
BLOCK4
IP block status
This bit provides the clock status of eDMA TCD 0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
3
BLOCK3
IP block status
This bit provides the clock status of eDMA_Control_and_Status in partition 1.
0b - Clock is not running.
1b - Clock is running.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1818 / 5251


---
# 페이지 161

Table continued from the previous page...
Field
Function
2
BLOCK2
IP block status
This bit provides the clock status of block 2 in partition 1.
0b - Clock is not running.
1b - Clock is running.
1
BLOCK1
IP block status
This bit provides the clock status of block 1 in partition 1.
0b - Clock is not running.
1b - Clock is running.
0
BLOCK0
IP block status
This bit provides the clock status of block 0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
46.7.41 Partition 1 COFB Set 1 Clock Status Register (PRTN1_COFB1_STAT)
Offset
Register
Offset
PRTN1_COFB1_STAT
314h
Function
This register provides the status of set 1 of COFBs inside partition 1.
 
The reset value of this register can vary depending on the availability of active clock pulses inside partition 1.
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
BLOC
K63 
BLOC
K62 
BLOC
K61 
BLOC
K60 
BLOC
K59 
BLOC
K58 
BLOC
K57 
BLOC
K56 
BLOC
K55 
BLOC
K54 
BLOC
K53 
BLOC
K52 
BLOC
K51 
BLOC
K50 
BLOC
K49 
0
W
Reset
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
1
1
1
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
BLOC
K47 
0
BLOC
K45 
0
BLOC
K43 
BLOC
K42 
BLOC
K41 
BLOC
K40 
BLOC
K39 
BLOC
K38 
BLOC
K37 
BLOC
K36 
BLOC
K35 
BLOC
K34 
BLOC
K33 
BLOC
K32 
W
Reset
0
0
1
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
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1819 / 5251


---
# 페이지 162

Fields
Field
Function
31
BLOCK63
IP block status
This bit provides the clock status of PIT 2 in partition 1.
0b - Clock is not running.
1b - Clock is running.
30
BLOCK62
IP block status
This bit provides the clock status of block 62 in partition 1.
0b - Clock is not running.
1b - Clock is running.
29
BLOCK61
IP block status
This bit provides the clock status of block 61 in partition 1.
0b - Clock is not running.
1b - Clock is running.
28
BLOCK60
IP block status
This bit provides the clock status of block 60 in partition 1.
0b - Clock is not running.
1b - Clock is running.
27
BLOCK59
IP block status
This bit provides the clock status of block 59 in partition 1.
0b - Clock is not running.
1b - Clock is running.
26
BLOCK58
IP block status
This bit provides the clock status of block 58 in partition 1.
0b - Clock is not running.
1b - Clock is running.
25
BLOCK57
IP block status
This bit provides the clock status of PLL 2 in partition 1.
0b - Clock is not running.
1b - Clock is running.
24
BLOCK56
IP block status
This bit provides the clock status of PLL in partition 1.
0b - Clock is not running.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1820 / 5251


---
# 페이지 163

Table continued from the previous page...
Field
Function
1b - Clock is running.
23
BLOCK55
IP block status
This bit provides the clock status of block 55 in partition 1.
0b - Clock is not running.
1b - Clock is running.
22
BLOCK54
IP block status
This bit provides the clock status of block 54 in partition 1.
0b - Clock is not running.
1b - Clock is running.
21
BLOCK53
IP block status
This bit provides the clock status of FXOSC in partition 1.
0b - Clock is not running.
1b - Clock is running.
20
BLOCK52
IP block status
This bit provides the clock status of block 52 in partition 1.
0b - Clock is not running.
1b - Clock is running.
19
BLOCK51
IP block status
This bit provides the clock status of SXOSC in partition 1.
0b - Clock is not running.
1b - Clock is running.
18
BLOCK50
IP block status
This bit provides the clock status of block 50 in partition 1.
0b - Clock is not running.
1b - Clock is running.
17
BLOCK49
IP block status
This bit provides the clock status of TSPC in partition 1.
0b - Clock is not running.
1b - Clock is running.
16
—
Reserved
This field is reserved and read returns zeros.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1821 / 5251


---
# 페이지 164

Table continued from the previous page...
Field
Function
15
BLOCK47
IP block status
This bit provides the clock status of CMU_0-5 in partition 1.
0b - Clock is not running.
1b - Clock is running.
14
—
Reserved
This field is reserved and read returns zeros.
13
BLOCK45
IP block status
This bit provides the clock status of WKPU in partition 1.
0b - Clock is not running.
1b - Clock is running.
12
—
Reserved
This field is reserved and read returns zeros.
11
BLOCK43
IP block status
This bit provides the clock status of block 43 in partition 1.
0b - Clock is not running.
1b - Clock is running.
10
BLOCK42
IP block status
This bit provides the clock status of SIUL_VIRTWRAPPER_PDAC3 in partition 1.
0b - Clock is not running.
1b - Clock is running.
9
BLOCK41
IP block status
This bit provides the clock status of block 41 in partition 1.
0b - Clock is not running.
1b - Clock is running.
8
BLOCK40
IP block status
This bit provides the clock status of block 40 in partition 1.
0b - Clock is not running.
1b - Clock is running.
7
BLOCK39
IP block status
This bit provides the clock status of block 39 in partition 1.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1822 / 5251


---
# 페이지 165

Table continued from the previous page...
Field
Function
0b - Clock is not running.
1b - Clock is running.
6
BLOCK38
IP block status
This bit provides the clock status of block 38 in partition 1.
0b - Clock is not running.
1b - Clock is running.
5
BLOCK37
IP block status
This bit provides the clock status of block 37 in partition 1.
0b - Clock is not running.
1b - Clock is running.
4
BLOCK36
IP block status
This bit provides the clock status of block 36 in partition 1.
0b - Clock is not running.
1b - Clock is running.
3
BLOCK35
IP block status
This bit provides the clock status of block 35 in partition 1.
0b - Clock is not running.
1b - Clock is running.
2
BLOCK34
IP block status
This bit provides the clock status of RTC in partition 1.
0b - Clock is not running.
1b - Clock is running.
1
BLOCK33
IP block status
This bit provides the clock status of DMAMUX 1 in partition 1.
0b - Clock is not running.
1b - Clock is running.
0
BLOCK32
IP block status
This bit provides the clock status of DMAMUX 0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1823 / 5251


---
# 페이지 166

46.7.42 Partition 1 COFB Set 2 Clock Status Register (PRTN1_COFB2_STAT)
Offset
Register
Offset
PRTN1_COFB2_STAT
318h
Function
This register provides the status of set 2 of COFBs inside partition 1.
 
The reset value of this register can vary depending on the availability of active clock pulses inside partition 1.
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
BLOC
K95 
0
BLOC
K93 
BLOC
K92 
BLOC
K91 
0
BLOC
K89 
BLOC
K88 
BLOC
K87 
BLOC
K86 
BLOC
K85 
BLOC
K84 
BLOC
K83 
BLOC
K82 
BLOC
K81 
BLOC
K80 
W
Reset
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
1
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
BLOC
K79 
BLOC
K78 
BLOC
K77 
BLOC
K76 
BLOC
K75 
BLOC
K74 
BLOC
K73 
BLOC
K72 
BLOC
K71 
BLOC
K70 
BLOC
K69 
BLOC
K68 
BLOC
K67 
BLOC
K66 
BLOC
K65 
BLOC
K64 
W
Reset
0
0
0
0
0
0
0
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
BLOCK95
IP block status
This bit provides the clock status of TMU in partition 1.
0b - Clock is not running.
1b - Clock is running.
30
—
Reserved
This field is reserved and read returns zeros.
29
BLOCK93
IP block status
This bit provides the clock status of LPCMP 1 in partition 1.
0b - Clock is not running.
1b - Clock is running.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1824 / 5251


---
# 페이지 167

Table continued from the previous page...
Field
Function
28
BLOCK92
IP block status
This bit provides the clock status of LPCMP 0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
27
BLOCK91
IP block status
This bit provides the clock status of SAI_0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
26
—
Reserved
This field is reserved and read returns zeros.
25
BLOCK89
IP block status
This bit provides the clock status of LPSPI 3 in partition 1.
0b - Clock is not running.
1b - Clock is running.
24
BLOCK88
IP block status
This bit provides the clock status of LPSPI 2 in partition 1.
0b - Clock is not running.
1b - Clock is running.
23
BLOCK87
IP block status
This bit provides the clock status of LPSPI 1 in partition 1.
0b - Clock is not running.
1b - Clock is running.
22
BLOCK86
IP block status
This bit provides the clock status of LPSPI 0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
21
BLOCK85
IP block status
This bit provides the clock status of LPI2C 1 in partition 1.
0b - Clock is not running.
1b - Clock is running.
20
IP block status
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1825 / 5251


---
# 페이지 168

Table continued from the previous page...
Field
Function
BLOCK84
This bit provides the clock status of LPI2C 0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
19
BLOCK83
IP block status
This bit provides the clock status of block 83 in partition 1.
0b - Clock is not running.
1b - Clock is running.
18
BLOCK82
IP block status
This bit provides the clock status of block 82 in partition 1.
0b - Clock is not running.
1b - Clock is running.
17
BLOCK81
IP block status
This bit provides the clock status of LPUART 7 in partition 1.
0b - Clock is not running.
1b - Clock is running.
16
BLOCK80
IP block status
This bit provides the clock status of LPUART 6 in partition 1.
0b - Clock is not running.
1b - Clock is running.
15
BLOCK79
IP block status
This bit provides the clock status of LPUART 5 in partition 1.
0b - Clock is not running.
1b - Clock is running.
14
BLOCK78
IP block status
This bit provides the clock status of LPUART 4 in partition 1.
0b - Clock is not running.
1b - Clock is running.
13
BLOCK77
IP block status
This bit provides the clock status of LPUART 3 in partition 1.
0b - Clock is not running.
1b - Clock is running.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1826 / 5251


---
# 페이지 169

Table continued from the previous page...
Field
Function
12
BLOCK76
IP block status
This bit provides the clock status of LPUART 2 in partition 1.
0b - Clock is not running.
1b - Clock is running.
11
BLOCK75
IP block status
This bit provides the clock status of LPUART 1 in partition 1.
0b - Clock is not running.
1b - Clock is running.
10
BLOCK74
IP block status
This bit provides the clock status of LPUART 0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
9
BLOCK73
IP block status
This bit provides the clock status of FlexIO in partition 1.
0b - Clock is not running.
1b - Clock is running.
8
BLOCK72
IP block status
This bit provides the clock status of FlexCAN 7 in partition 1.
0b - Clock is not running.
1b - Clock is running.
7
BLOCK71
IP block status
This bit provides the clock status of FlexCAN 6 in partition 1.
0b - Clock is not running.
1b - Clock is running.
6
BLOCK70
IP block status
This bit provides the clock status of FlexCAN 5 in partition 1.
0b - Clock is not running.
1b - Clock is running.
5
BLOCK69
IP block status
This bit provides the clock status of FlexCAN 4 in partition 1.
0b - Clock is not running.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1827 / 5251


---
# 페이지 170

Table continued from the previous page...
Field
Function
1b - Clock is running.
4
BLOCK68
IP block status
This bit provides the clock status of FlexCAN 3 in partition 1.
0b - Clock is not running.
1b - Clock is running.
3
BLOCK67
IP block status
This bit provides the clock status of FlexCAN 2 in partition 1.
0b - Clock is not running.
1b - Clock is running.
2
BLOCK66
IP block status
This bit provides the clock status of FlexCAN 1 in partition 1.
0b - Clock is not running.
1b - Clock is running.
1
BLOCK65
IP block status
This bit provides the clock status of FlexCAN 0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
0
BLOCK64
IP block status
This bit provides the clock status of PIT 3 in partition 1.
0b - Clock is not running.
1b - Clock is running.
46.7.43 Partition 1 COFB Set 3 Clock Status Register (PRTN1_COFB3_STAT)
Offset
Register
Offset
PRTN1_COFB3_STAT
31Ch
Function
This register provides the status of set 3 of COFBs inside partition 1.
 
The reset value of this register can vary depending on the availability of active clock pulses inside partition 1.
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1828 / 5251


---
# 페이지 171

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
BLOC
K127 
BLOC
K126 
BLOC
K125 
BLOC
K124 
BLOC
K123 
BLOC
K122 
BLOC
K121 
BLOC
K120 
BLOC
K119 
BLOC
K118 
BLOC
K117 
BLOC
K116 
BLOC
K115 
BLOC
K114 
BLOC
K113 
BLOC
K112 
W
Reset
0
0
0
0
0
0
0
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
BLOC
K110 
0
BLOC
K108 
BLOC
K107 
BLOC
K106 
BLOC
K105 
BLOC
K104 
BLOC
K103 
BLOC
K102 
BLOC
K101 
0
BLOC
K99 
BLOC
K98 
BLOC
K97 
BLOC
K96 
W
Reset
0
1
0
1
1
1
1
1
1
1
1
0
1
1
1
0
Fields
Field
Function
31
BLOCK127
IP block status
This bit provides the clock status of AES Application 2 in partition 1.
0b - Clock is not running.
1b - Clock is running.
30
BLOCK126
IP block status
This bit provides the clock status of AES Application 2 in partition 1.
0b - Clock is not running.
1b - Clock is running.
29
BLOCK125
IP block status
This bit provides the clock status of AES Application 2 in partition 1.
0b - Clock is not running.
1b - Clock is running.
28
BLOCK124
IP block status
This bit provides the clock status of AES Application 2 in partition 1.
0b - Clock is not running.
1b - Clock is running.
27
BLOCK123
IP block status
This bit provides the clock status of AES Application 1 in partition 1.
0b - Clock is not running.
1b - Clock is running.
26
IP block status
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1829 / 5251


---
# 페이지 172

Table continued from the previous page...
Field
Function
BLOCK122
This bit provides the clock status of AES Application 1 in partition 1.
0b - Clock is not running.
1b - Clock is running.
25
BLOCK121
IP block status
This bit provides the clock status of AES Application 1 in partition 1.
0b - Clock is not running.
1b - Clock is running.
24
BLOCK120
IP block status
This bit provides the clock status of AES Application 1 in partition 1.
0b - Clock is not running.
1b - Clock is running.
23
BLOCK119
IP block status
This bit provides the clock status of AES Application 0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
22
BLOCK118
IP block status
This bit provides the clock status of AES Application 0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
21
BLOCK117
IP block status
This bit provides the clock status of AES Application 0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
20
BLOCK116
IP block status
This bit provides the clock status of AES Application 0 in partition 1.
0b - Clock is not running.
1b - Clock is running.
19
BLOCK115
IP block status
This bit provides the clock status of AES Accelerator in partition 1.
0b - Clock is not running.
1b - Clock is running.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1830 / 5251


---
# 페이지 173

Table continued from the previous page...
Field
Function
18
BLOCK114
IP block status
This bit provides the clock status of AES Accelerator in partition 1.
0b - Clock is not running.
1b - Clock is running.
17
BLOCK113
IP block status
This bit provides the clock status of AES Accelerator in partition 1.
0b - Clock is not running.
1b - Clock is running.
16
BLOCK112
IP block status
This bit provides the clock status of AES Accelerator in partition 1.
0b - Clock is not running.
1b - Clock is running.
15
—
Reserved
This field is reserved and read returns zeros.
14
BLOCK110
IP block status
This bit provides the clock status of block 110 in partition 1.
0b - Clock is not running.
1b - Clock is running.
13
—
Reserved
This field is reserved and read returns zeros.
12
BLOCK108
IP block status
This bit provides the clock status of block 108 in partition 1.
0b - Clock is not running.
1b - Clock is running.
11
BLOCK107
IP block status
This bit provides the clock status of block 107 in partition 1.
0b - Clock is not running.
1b - Clock is running.
10
BLOCK106
IP block status
This bit provides the clock status of block 106 in partition 1.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1831 / 5251


---
# 페이지 174

Table continued from the previous page...
Field
Function
0b - Clock is not running.
1b - Clock is running.
9
BLOCK105
IP block status
This bit provides the clock status of block 105 in partition 1.
0b - Clock is not running.
1b - Clock is running.
8
BLOCK104
IP block status
This bit provides the clock status of STCU in partition 1.
0b - Clock is not running.
1b - Clock is running.
7
BLOCK103
IP block status
This bit provides the clock status of block 103 in partition 1.
0b - Clock is not running.
1b - Clock is running.
6
BLOCK102
IP block status
This bit provides the clock status of block 102 in partition 1.
0b - Clock is not running.
1b - Clock is running.
5
BLOCK101
IP block status
This bit provides the clock status of block 101 in partition 1.
0b - Clock is not running.
1b - Clock is running.
4
—
Reserved
This field is reserved and read returns zeros.
3
BLOCK99
IP block status
This bit provides the clock status of block 99 in partition 1.
0b - Clock is not running.
1b - Clock is running.
2
BLOCK98
IP block status
This bit provides the clock status of block 98 in partition 1.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1832 / 5251


---
# 페이지 175

Table continued from the previous page...
Field
Function
0b - Clock is not running.
1b - Clock is running.
1
BLOCK97
IP block status
This bit provides the clock status of block 97 in partition 1.
0b - Clock is not running.
1b - Clock is running.
0
BLOCK96
IP block status
This bit provides the clock status of CRC in partition 1.
0b - Clock is not running.
1b - Clock is running.
46.7.44 Partition 1 COFB Set 0 Clock Enable Register (PRTN1_COFB0_CLKEN)
Offset
Register
Offset
PRTN1_COFB0_CLKEN
330h
Function
This register provides clock control signaling to the individual COFBs in set 0 inside partition 1. Whenever a partition clock enable 
(non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock 
to the corresponding block in the partition.
 
The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific 
MC_ME information for clock source availability.
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
REQ3
1 
0
REQ2
9 
REQ2
8 
0
0
0
REQ2
4 
REQ2
3 
0
REQ2
1 
0
0
0
0
0
W
Reset
0
1
0
1
1
1
1
0
0
0
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
REQ1
5 
REQ1
4 
REQ1
3 
REQ1
2 
REQ1
1 
REQ1
0 
REQ9 
REQ8 
REQ7 
REQ6 
REQ5 
REQ4 
REQ3 
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
1
1
1
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1833 / 5251


---
# 페이지 176

Fields
Field
Function
31
REQ31
Clock enable
This bit provides the clock enable control for INTM in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
30
—
Reserved
This field is reserved and read returns zeros.
29
REQ29
Clock enable
This bit provides the clock enable control for STM 0 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
28
REQ28
Clock enable
This bit provides the clock enable control for SWT 0 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
27
—
Reserved
This field is reserved and read returns zeros.
26
—
Reserved
This field is reserved and read returns zeros.
25
—
Reserved
This field is reserved and read returns zeros.
24
REQ24
Clock enable
This bit provides the clock enable control for MSCM in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
23
REQ23
Clock enable
This bit provides the clock enable control for ERM_0 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
22
—
Reserved
This field is reserved and read returns zeros.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1834 / 5251


---
# 페이지 177

Table continued from the previous page...
Field
Function
21
REQ21
Clock enable
This bit provides the clock enable control for SDA-AP and Debug APB Paged Area in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
20
—
Reserved
This field is reserved and read returns zeros.
19
—
Reserved
This field is reserved and read returns zeros.
18
—
Reserved
This field is reserved and read returns zeros.
17
—
Reserved
This field is reserved and read returns zeros.
16
—
Reserved
This field is reserved and read returns zeros.
15
REQ15
Clock enable
This bit provides the clock enable control for eDMA TCD 11 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
14
REQ14
Clock enable
This bit provides the clock enable control for eDMA TCD 10 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
13
REQ13
Clock enable
This bit provides the clock enable control for eDMA TCD 9 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
12
REQ12
Clock enable
This bit provides the clock enable control for eDMA TCD 8 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1835 / 5251


---
# 페이지 178

Table continued from the previous page...
Field
Function
11
REQ11
Clock enable
This bit provides the clock enable control for eDMA TCD 7 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
10
REQ10
Clock enable
This bit provides the clock enable control for eDMA TCD 6 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
9
REQ9
Clock enable
This bit provides the clock enable control for eDMA TCD 5 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
8
REQ8
Clock enable
This bit provides the clock enable control for eDMA TCD 4 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
7
REQ7
Clock enable
This bit provides the clock enable control for eDMA TCD 3 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
6
REQ6
Clock enable
This bit provides the clock enable control for eDMA TCD 2 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
5
REQ5
Clock enable
This bit provides the clock enable control for eDMA TCD 1 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
4
REQ4
Clock enable
This bit provides the clock enable control for eDMA TCD 0 in partition 1.
0b - Clock is turned off.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1836 / 5251


---
# 페이지 179

Table continued from the previous page...
Field
Function
1b - Clock is turned on.
3
REQ3
Clock enable
This bit provides the clock enable control for eDMA_Control_and_Status in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
2
—
Reserved
This field is reserved and read returns zeros.
1
—
Reserved
This field is reserved and read returns zeros.
0
—
Reserved
This field is reserved and read returns zeros.
46.7.45 Partition 1 COFB Set 1 Clock Enable Register (PRTN1_COFB1_CLKEN)
Offset
Register
Offset
PRTN1_COFB1_CLKEN
334h
Function
This register provides clock control signaling to the individual COFBs in set 1 inside partition 1. Whenever a partition clock enable 
(non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock 
to the corresponding block in the partition.
 
The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific 
MC_ME information for clock source availability.
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1837 / 5251


---
# 페이지 180

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
REQ6
3 
0
0
0
0
0
REQ5
7 
REQ5
6 
0
0
REQ5
3 
0
REQ5
1 
0
REQ4
9 
0
W
Reset
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
1
1
1
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
REQ4
7 
0
REQ4
5 
0
0
REQ4
2 
0
0
0
0
0
0
0
REQ3
4 
REQ3
3 
REQ3
2 
W
Reset
0
0
1
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
Fields
Field
Function
31
REQ63
Clock enable
This bit provides the clock enable control for PIT 2 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
30
—
Reserved
This field is reserved and read returns zeros.
29
—
Reserved
This field is reserved and read returns zeros.
28
—
Reserved
This field is reserved and read returns zeros.
27
—
Reserved
This field is reserved and read returns zeros.
26
—
Reserved
This field is reserved and read returns zeros.
25
REQ57
Clock enable
This bit provides the clock enable control for PLL 2 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
24
REQ56
Clock enable
This bit provides the clock enable control for PLL in partition 1.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1838 / 5251


---
# 페이지 181

Table continued from the previous page...
Field
Function
0b - Clock is turned off.
1b - Clock is turned on.
23
—
Reserved
This field is reserved and read returns zeros.
22
—
Reserved
This field is reserved and read returns zeros.
21
REQ53
Clock enable
This bit provides the clock enable control for FXOSC in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
20
—
Reserved
This field is reserved and read returns zeros.
19
REQ51
Clock enable
This bit provides the clock enable control for SXOSC in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
18
—
Reserved
This field is reserved and read returns zeros.
17
REQ49
Clock enable
This bit provides the clock enable control for TSPC in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
16
—
Reserved
This field is reserved and read returns zeros.
15
REQ47
Clock enable
This bit provides the clock enable control for CMU_0-5 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
14
—
Reserved
This field is reserved and read returns zeros.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1839 / 5251


---
# 페이지 182

Table continued from the previous page...
Field
Function
13
REQ45
Clock enable
This bit provides the clock enable control for WKPU in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
12
—
Reserved
This field is reserved and read returns zeros.
11
—
Reserved
This field is reserved and read returns zeros.
10
REQ42
Clock enable
This bit provides the clock enable control for SIUL_VIRTWRAPPER_PDAC3 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
9
—
Reserved
This field is reserved and read returns zeros.
8
—
Reserved
This field is reserved and read returns zeros.
7
—
Reserved
This field is reserved and read returns zeros.
6
—
Reserved
This field is reserved and read returns zeros.
5
—
Reserved
This field is reserved and read returns zeros.
4
—
Reserved
This field is reserved and read returns zeros.
3
—
Reserved
This field is reserved and read returns zeros.
2
REQ34
Clock enable
This bit provides the clock enable control for RTC in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1840 / 5251


---
# 페이지 183

Table continued from the previous page...
Field
Function
1
REQ33
Clock enable
This bit provides the clock enable control for DMAMUX 1 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
0
REQ32
Clock enable
This bit provides the clock enable control for DMAMUX 0 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
46.7.46 Partition 1 COFB Set 2 Clock Enable Register (PRTN1_COFB2_CLKEN)
Offset
Register
Offset
PRTN1_COFB2_CLKEN
338h
Function
This register provides clock control signaling to the individual COFBs in set 2 inside partition 1. Whenever a partition clock enable 
(non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock 
to the corresponding block in the partition.
 
The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific 
MC_ME information for clock source availability.
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
REQ9
5 
0
REQ9
3 
REQ9
2 
REQ9
1 
0
REQ8
9 
REQ8
8 
REQ8
7 
REQ8
6 
REQ8
5 
REQ8
4 
0
0
REQ8
1 
REQ8
0 
W
Reset
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
1
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
REQ7
9 
REQ7
8 
REQ7
7 
REQ7
6 
REQ7
5 
REQ7
4 
REQ7
3 
REQ7
2 
REQ7
1 
REQ7
0 
REQ6
9 
REQ6
8 
REQ6
7 
REQ6
6 
REQ6
5 
REQ6
4 
W
Reset
0
0
0
0
0
0
0
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
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1841 / 5251


---
# 페이지 184

Fields
Field
Function
31
REQ95
Clock enable
This bit provides the clock enable control for TMU in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
30
—
Reserved
This field is reserved and read returns zeros.
29
REQ93
Clock enable
This bit provides the clock enable control for LPCMP 1 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
28
REQ92
Clock enable
This bit provides the clock enable control for LPCMP 0 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
27
REQ91
Clock enable
This bit provides the clock enable control for SAI_0 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
26
—
Reserved
This field is reserved and read returns zeros.
25
REQ89
Clock enable
This bit provides the clock enable control for LPSPI 3 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
24
REQ88
Clock enable
This bit provides the clock enable control for LPSPI 2 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
23
REQ87
Clock enable
This bit provides the clock enable control for LPSPI 1 in partition 1.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1842 / 5251


---
# 페이지 185

Table continued from the previous page...
Field
Function
0b - Clock is turned off.
1b - Clock is turned on.
22
REQ86
Clock enable
This bit provides the clock enable control for LPSPI 0 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
21
REQ85
Clock enable
This bit provides the clock enable control for LPI2C 1 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
20
REQ84
Clock enable
This bit provides the clock enable control for LPI2C 0 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
19
—
Reserved
This field is reserved and read returns zeros.
18
—
Reserved
This field is reserved and read returns zeros.
17
REQ81
Clock enable
This bit provides the clock enable control for LPUART 7 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
16
REQ80
Clock enable
This bit provides the clock enable control for LPUART 6 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
15
REQ79
Clock enable
This bit provides the clock enable control for LPUART 5 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
14
Clock enable
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1843 / 5251


---
# 페이지 186

Table continued from the previous page...
Field
Function
REQ78
This bit provides the clock enable control for LPUART 4 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
13
REQ77
Clock enable
This bit provides the clock enable control for LPUART 3 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
12
REQ76
Clock enable
This bit provides the clock enable control for LPUART 2 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
11
REQ75
Clock enable
This bit provides the clock enable control for LPUART 1 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
10
REQ74
Clock enable
This bit provides the clock enable control for LPUART 0 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
9
REQ73
Clock enable
This bit provides the clock enable control for FlexIO in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
8
REQ72
Clock enable
This bit provides the clock enable control for FlexCAN 7 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
7
REQ71
Clock enable
This bit provides the clock enable control for FlexCAN 6 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1844 / 5251


---
# 페이지 187

Table continued from the previous page...
Field
Function
6
REQ70
Clock enable
This bit provides the clock enable control for FlexCAN 5 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
5
REQ69
Clock enable
This bit provides the clock enable control for FlexCAN 4 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
4
REQ68
Clock enable
This bit provides the clock enable control for FlexCAN 3 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
3
REQ67
Clock enable
This bit provides the clock enable control for FlexCAN 2 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
2
REQ66
Clock enable
This bit provides the clock enable control for FlexCAN 1 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
1
REQ65
Clock enable
This bit provides the clock enable control for FlexCAN 0 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
0
REQ64
Clock enable
This bit provides the clock enable control for PIT 3 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1845 / 5251


---
# 페이지 188

46.7.47 Partition 1 COFB Set 3 Clock Enable Register (PRTN1_COFB3_CLKEN)
Offset
Register
Offset
PRTN1_COFB3_CLKEN
33Ch
Function
This register provides clock control signaling to the individual COFBs in set 3 inside partition 1. Whenever a partition clock enable 
(non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock 
to the corresponding block in the partition.
 
The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific 
MC_ME information for clock source availability.
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
REQ1
27 
REQ1
26 
REQ1
25 
REQ1
24 
REQ1
23 
REQ1
22 
REQ1
21 
REQ1
20 
REQ1
19 
REQ1
18 
REQ1
17 
REQ1
16 
REQ1
15 
REQ1
14 
REQ1
13 
REQ1
12 
W
Reset
0
0
0
0
0
0
0
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
0
0
REQ1
04 
0
REQ1
02 
0
0
0
0
0
REQ9
6 
W
Reset
0
1
0
1
1
1
1
1
1
1
1
0
1
1
1
0
Fields
Field
Function
31
REQ127
Clock enable
This bit provides the clock enable control for AES Application 2 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
30
REQ126
Clock enable
This bit provides the clock enable control for AES Application 2 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
29
REQ125
Clock enable
This bit provides the clock enable control for AES Application 2 in partition 1.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1846 / 5251


---
# 페이지 189

Table continued from the previous page...
Field
Function
0b - Clock is turned off.
1b - Clock is turned on.
28
REQ124
Clock enable
This bit provides the clock enable control for AES Application 2 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
27
REQ123
Clock enable
This bit provides the clock enable control for AES Application 1 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
26
REQ122
Clock enable
This bit provides the clock enable control for AES Application 1 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
25
REQ121
Clock enable
This bit provides the clock enable control for AES Application 1 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
24
REQ120
Clock enable
This bit provides the clock enable control for AES Application 1 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
23
REQ119
Clock enable
This bit provides the clock enable control for AES Application 0 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
22
REQ118
Clock enable
This bit provides the clock enable control for AES Application 0 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
21
Clock enable
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1847 / 5251


---
# 페이지 190

Table continued from the previous page...
Field
Function
REQ117
This bit provides the clock enable control for AES Application 0 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
20
REQ116
Clock enable
This bit provides the clock enable control for AES Application 0 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
19
REQ115
Clock enable
This bit provides the clock enable control for AES Accelerator in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
18
REQ114
Clock enable
This bit provides the clock enable control for AES Accelerator in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
17
REQ113
Clock enable
This bit provides the clock enable control for AES Accelerator in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
16
REQ112
Clock enable
This bit provides the clock enable control for AES Accelerator in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
15
—
Reserved
This field is reserved and read returns zeros.
14
—
Reserved
This field is reserved and read returns zeros.
13
—
Reserved
This field is reserved and read returns zeros.
12
Reserved
This field is reserved and read returns zeros.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1848 / 5251


---
# 페이지 191

Table continued from the previous page...
Field
Function
—
11
—
Reserved
This field is reserved and read returns zeros.
10
—
Reserved
This field is reserved and read returns zeros.
9
—
Reserved
This field is reserved and read returns zeros.
8
REQ104
Clock enable
This bit provides the clock enable control for STCU in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
7
—
Reserved
This field is reserved and read returns zeros.
6
REQ102
Clock enable
This bit provides the clock enable control for block 102 in partition 1.
0b - Clock is turned off.
1b - Clock is turned on.
5
—
Reserved
This field is reserved and read returns zeros.
4
—
Reserved
This field is reserved and read returns zeros.
3
—
Reserved
This field is reserved and read returns zeros.
2
—
Reserved
This field is reserved and read returns zeros.
1
—
Reserved
This field is reserved and read returns zeros.
0
REQ96
Clock enable
This bit provides the clock enable control for CRC in partition 1.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1849 / 5251


---
# 페이지 192

Table continued from the previous page...
Field
Function
0b - Clock is turned off.
1b - Clock is turned on.
46.7.48 Partition 2 Process Configuration Register (PRTN2_PCONF)
Offset
Register
Offset
PRTN2_PCONF
500h
Function
This register provides a configuration for the hardware processes corresponding to partition 2. Each of the configuration bit 
corresponds to the 'nature' of the processes; for example, enabling/disabling and the trigger is controlled by the corresponding 
field in the PRTN2_PUPD register. When valid KEY combinations are written onto the CTL_KEY register, the PRTN2_PCONF 
and PRTN2_PUPD registers are used to determine the hardware processes to be executed. These are triggered in parallel and 
independent of each other. All dependent processes should be requested one after another from the software.
 
The partition clock enable/disable are not standalone and must be done coherently in a fixed sequence. For details, 
see Software Reset Partition Turn-On Flow Chart and Software reset partition turn-off flowchart in Reset chapter.
  NOTE  
 
See chip-specific MC_ME information to check if this register is implemented on chip.
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
0
0
0
0
0
0
PCE 
W
Reset
0
0
0
0
0
0
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
31-7
Reserved
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1850 / 5251


---
# 페이지 193

Table continued from the previous page...
Field
Function
—
This field is reserved and read returns zeros.
6
—
Reserved
This field is reserved and read returns zeros.
5
—
Reserved
This field is reserved and read returns zeros.
4
—
Reserved
This field is reserved and read returns zeros.
3
—
Reserved
This field is reserved and read returns zeros.
2
—
Reserved
This field is reserved and read returns zeros.
1
—
Reserved
This field is reserved and read returns zeros.
0
PCE
Partition clock enable
This bit controls whether the clock to IPs (other than core(s)) in the partition should be enabled or disabled.
0b - Disable the clock to IPs
1b - Enable the clock to IPs
46.7.49 Partition 2 Process Update Register (PRTN2_PUPD)
Offset
Register
Offset
PRTN2_PUPD
504h
Function
This register provides trigger signaling for the hardware processes corresponding to partition 2. Each of the control bit acts as 
a trigger for the corresponding hardware processes. When valid KEY combinations are written onto the CTL_KEY register, the 
hardware checks the bit fields that are programmed as logic-1 in this register, and then triggers the hardware process per the value 
in the corresponding bit field in the PRTN2_PCONF register. When the hardware process is finished the corresponding bit in this 
register is auto-cleared to logic-0.
 
See chip-specific MC_ME information to check if this register is implemented on chip.
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1851 / 5251


---
# 페이지 194

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
0
0
0
0
PCUD 
W
Reset
0
0
0
0
0
0
0
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
This field is reserved and read returns zeros.
6
—
Reserved
This field is reserved and read returns zeros.
5
—
Reserved
This field is reserved and read returns zeros.
4
—
Reserved
This field is reserved and read returns zeros.
3
—
Reserved
This field is reserved and read returns zeros.
2
—
Reserved
This field is reserved and read returns zeros.
1
—
Reserved
This field is reserved and read returns zeros.
0
PCUD
Partition clock update
This bit controls whether the hardware processes for enabling/disabling the clock to IPs (other than core(s)) 
in the partition should be triggered or not.
0b - Do not trigger the hardware process
1b - Trigger the hardware process
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1852 / 5251


---
# 페이지 195

46.7.50 Partition 2 Status Register (PRTN2_STAT)
Offset
Register
Offset
PRTN2_STAT
508h
Function
This register provides the current status of the control signals from the partition 2.
 
See chip-specific MC_ME information to check if this register is implemented on chip.
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
0
0
0
0
0
0
PCS 
W
Reset
0
0
0
0
0
0
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
31-7
—
Reserved
This field is reserved and read returns zeros.
6
—
Reserved
This field is reserved and read returns zeros.
5
—
Reserved
This field is reserved and read returns zeros.
4
—
Reserved
This field is reserved and read returns zeros.
3
—
Reserved
This field is reserved and read returns zeros.
2
Reserved
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1853 / 5251


---
# 페이지 196

Table continued from the previous page...
Field
Function
—
This field is reserved and read returns zeros.
1
—
Reserved
This field is reserved and read returns zeros.
0
PCS
Partition clock status
This bit provides the status of the clock to partition.
0b - Clock is inactive
1b - Clock is active
46.7.51 Partition 2 COFB Set 0 Clock Status Register (PRTN2_COFB0_STAT)
Offset
Register
Offset
PRTN2_COFB0_STAT
510h
Function
This register provides the status of set 0 of COFBs inside partition 2.
 
The reset value of this register can vary depending on the availability of active clock pulses inside partition 2.
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
BLOC
K31 
BLOC
K30 
BLOC
K29 
BLOC
K28 
BLOC
K27 
BLOC
K26 
BLOC
K25 
BLOC
K24 
BLOC
K23 
BLOC
K22 
BLOC
K21 
BLOC
K20 
BLOC
K19 
BLOC
K18 
BLOC
K17 
BLOC
K16 
W
Reset
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
BLOC
K15 
BLOC
K14 
BLOC
K13 
BLOC
K12 
BLOC
K11 
BLOC
K10 
BLOC
K9 
BLOC
K8 
BLOC
K7 
BLOC
K6 
BLOC
K5 
BLOC
K4 
BLOC
K3 
BLOC
K2 
BLOC
K1 
BLOC
K0 
W
Reset
0
0
0
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
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1854 / 5251


---
# 페이지 197

Fields
Field
Function
31
BLOCK31
IP block status
This bit provides the clock status of STM 3 in partition 2.
0b - Clock is not running.
1b - Clock is running.
30
BLOCK30
IP block status
This bit provides the clock status of STM 2 in partition 2.
0b - Clock is not running.
1b - Clock is running.
29
BLOCK29
IP block status
This bit provides the clock status of STM 1 in partition 2.
0b - Clock is not running.
1b - Clock is running.
28
BLOCK28
IP block status
This bit provides the clock status of SWT 2 in partition 2.
0b - Clock is not running.
1b - Clock is running.
27
BLOCK27
IP block status
This bit provides the clock status of SWT 1 in partition 2.
0b - Clock is not running.
1b - Clock is running.
26
BLOCK26
IP block status
This bit provides the clock status of block 26 in partition 2.
0b - Clock is not running.
1b - Clock is running.
25
BLOCK25
IP block status
This bit provides the clock status of block 25 in partition 2.
0b - Clock is not running.
1b - Clock is running.
24
BLOCK24
IP block status
This bit provides the clock status of SEMA42 in partition 2.
0b - Clock is not running.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1855 / 5251


---
# 페이지 198

Table continued from the previous page...
Field
Function
1b - Clock is running.
23
BLOCK23
IP block status
This bit provides the clock status of eDMA TCD 31 in partition 2.
0b - Clock is not running.
1b - Clock is running.
22
BLOCK22
IP block status
This bit provides the clock status of eDMA TCD 30 in partition 2.
0b - Clock is not running.
1b - Clock is running.
21
BLOCK21
IP block status
This bit provides the clock status of eDMA TCD 29 in partition 2.
0b - Clock is not running.
1b - Clock is running.
20
BLOCK20
IP block status
This bit provides the clock status of eDMA TCD 28 in partition 2.
0b - Clock is not running.
1b - Clock is running.
19
BLOCK19
IP block status
This bit provides the clock status of eDMA TCD 27 in partition 2.
0b - Clock is not running.
1b - Clock is running.
18
BLOCK18
IP block status
This bit provides the clock status of eDMA TCD 26 in partition 2.
0b - Clock is not running.
1b - Clock is running.
17
BLOCK17
IP block status
This bit provides the clock status of eDMA TCD 25 in partition 2.
0b - Clock is not running.
1b - Clock is running.
16
BLOCK16
IP block status
This bit provides the clock status of eDMA TCD 24 in partition 2.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1856 / 5251


---
# 페이지 199

Table continued from the previous page...
Field
Function
0b - Clock is not running.
1b - Clock is running.
15
BLOCK15
IP block status
This bit provides the clock status of eDMA TCD 23 in partition 2.
0b - Clock is not running.
1b - Clock is running.
14
BLOCK14
IP block status
This bit provides the clock status of eDMA TCD 22 in partition 2.
0b - Clock is not running.
1b - Clock is running.
13
BLOCK13
IP block status
This bit provides the clock status of eDMA TCD 21 in partition 2.
0b - Clock is not running.
1b - Clock is running.
12
BLOCK12
IP block status
This bit provides the clock status of eDMA TCD 20 in partition 2.
0b - Clock is not running.
1b - Clock is running.
11
BLOCK11
IP block status
This bit provides the clock status of eDMA TCD 19 in partition 2.
0b - Clock is not running.
1b - Clock is running.
10
BLOCK10
IP block status
This bit provides the clock status of eDMA TCD 18 in partition 2.
0b - Clock is not running.
1b - Clock is running.
9
BLOCK9
IP block status
This bit provides the clock status of eDMA TCD 17 in partition 2.
0b - Clock is not running.
1b - Clock is running.
8
IP block status
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1857 / 5251


---
# 페이지 200

Table continued from the previous page...
Field
Function
BLOCK8
This bit provides the clock status of eDMA TCD 16 in partition 2.
0b - Clock is not running.
1b - Clock is running.
7
BLOCK7
IP block status
This bit provides the clock status of eDMA TCD 15 in partition 2.
0b - Clock is not running.
1b - Clock is running.
6
BLOCK6
IP block status
This bit provides the clock status of eDMA TCD 14 in partition 2.
0b - Clock is not running.
1b - Clock is running.
5
BLOCK5
IP block status
This bit provides the clock status of eDMA TCD 13 in partition 2.
0b - Clock is not running.
1b - Clock is running.
4
BLOCK4
IP block status
This bit provides the clock status of eDMA TCD 12 in partition 2.
0b - Clock is not running.
1b - Clock is running.
3
BLOCK3
IP block status
This bit provides the clock status of block 3 in partition 2.
0b - Clock is not running.
1b - Clock is running.
2
BLOCK2
IP block status
This bit provides the clock status of block 2 in partition 2.
0b - Clock is not running.
1b - Clock is running.
1
BLOCK1
IP block status
This bit provides the clock status of block 1 in partition 2.
0b - Clock is not running.
1b - Clock is running.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1858 / 5251


---
# 페이지 201

Table continued from the previous page...
Field
Function
0
BLOCK0
IP block status
This bit provides the clock status of block 0 in partition 2.
0b - Clock is not running.
1b - Clock is running.
46.7.52 Partition 2 COFB Set 1 Clock Status Register (PRTN2_COFB1_STAT)
Offset
Register
Offset
PRTN2_COFB1_STAT
514h
Function
This register provides the status of set 1 of COFBs inside partition 2.
 
The reset value of this register can vary depending on the availability of active clock pulses inside partition 2.
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
BLOC
K63 
BLOC
K62 
0
0
BLOC
K59 
BLOC
K58 
0
0
BLOC
K55 
0
0
0
BLOC
K51 
0
0
BLOC
K48 
W
Reset
1
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
BLOC
K47 
0
0
0
0
BLOC
K42 
BLOC
K41 
BLOC
K40 
BLOC
K39 
BLOC
K38 
BLOC
K37 
BLOC
K36 
BLOC
K35 
BLOC
K34 
BLOC
K33 
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
BLOCK63
IP block status
This bit provides the clock status of block 63 in partition 2.
0b - Clock is not running.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1859 / 5251


---
# 페이지 202

Table continued from the previous page...
Field
Function
1b - Clock is running.
30
BLOCK62
IP block status
This bit provides the clock status of block 62 in partition 2.
0b - Clock is not running.
1b - Clock is running.
29
—
Reserved
This field is reserved and read returns zeros.
28
—
Reserved
This field is reserved and read returns zeros.
27
BLOCK59
IP block status
This bit provides the clock status of block 59 in partition 2.
0b - Clock is not running.
1b - Clock is running.
26
BLOCK58
IP block status
This bit provides the clock status of LPCMP 2 in partition 2.
0b - Clock is not running.
1b - Clock is running.
25
—
Reserved
This field is reserved and read returns zeros.
24
—
Reserved
This field is reserved and read returns zeros.
23
BLOCK55
IP block status
This bit provides the clock status of SAI 1 in partition 2.
0b - Clock is not running.
1b - Clock is running.
22
—
Reserved
This field is reserved and read returns zeros.
21
—
Reserved
This field is reserved and read returns zeros.
20
Reserved
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1860 / 5251


---
# 페이지 203

Table continued from the previous page...
Field
Function
—
This field is reserved and read returns zeros.
19
BLOCK51
IP block status
This bit provides the clock status of QuadSPI in partition 2.
0b - Clock is not running.
1b - Clock is running.
18
—
Reserved
This field is reserved and read returns zeros.
17
—
Reserved
This field is reserved and read returns zeros.
16
BLOCK48
IP block status
This bit provides the clock status of LPSPI 5 in partition 2.
0b - Clock is not running.
1b - Clock is running.
15
BLOCK47
IP block status
This bit provides the clock status of LPSPI 4 in partition 2.
0b - Clock is not running.
1b - Clock is running.
14
—
Reserved
This field is reserved and read returns zeros.
13
—
Reserved
This field is reserved and read returns zeros.
12
—
Reserved
This field is reserved and read returns zeros.
11
—
Reserved
This field is reserved and read returns zeros.
10
BLOCK42
IP block status
This bit provides the clock status of LPUART 15 in partition 2.
0b - Clock is not running.
1b - Clock is running.
9
IP block status
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1861 / 5251


---
# 페이지 204

Table continued from the previous page...
Field
Function
BLOCK41
This bit provides the clock status of LPUART 14 in partition 2.
0b - Clock is not running.
1b - Clock is running.
8
BLOCK40
IP block status
This bit provides the clock status of LPUART 13 in partition 2.
0b - Clock is not running.
1b - Clock is running.
7
BLOCK39
IP block status
This bit provides the clock status of LPUART 12 in partition 2.
0b - Clock is not running.
1b - Clock is running.
6
BLOCK38
IP block status
This bit provides the clock status of LPUART 11 in partition 2.
0b - Clock is not running.
1b - Clock is running.
5
BLOCK37
IP block status
This bit provides the clock status of LPUART 10 in partition 2.
0b - Clock is not running.
1b - Clock is running.
4
BLOCK36
IP block status
This bit provides the clock status of LPUART 9 in partition 2.
0b - Clock is not running.
1b - Clock is running.
3
BLOCK35
IP block status
This bit provides the clock status of LPUART 8 in partition 2.
0b - Clock is not running.
1b - Clock is running.
2
BLOCK34
IP block status
This bit provides the clock status of GMAC 1 in partition 2.
0b - Clock is not running.
1b - Clock is running.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1862 / 5251


---
# 페이지 205

Table continued from the previous page...
Field
Function
1
BLOCK33
IP block status
This bit provides the clock status of GMAC 0 in partition 2.
0b - Clock is not running.
1b - Clock is running.
0
—
Reserved
This field is reserved and read returns zeros.
46.7.53 Partition 2 COFB Set 2 Clock Status Register (PRTN2_COFB2_STAT)
Offset
Register
Offset
PRTN2_COFB2_STAT
518h
Function
This register provides the status of set 2 of COFBs inside partition 2.
 
The reset value of this register can vary depending on the availability of active clock pulses inside partition 2.
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
BLOC
K95 
BLOC
K94 
BLOC
K93 
BLOC
K92 
BLOC
K91 
BLOC
K90 
BLOC
K89 
BLOC
K88 
BLOC
K87 
BLOC
K86 
BLOC
K85 
BLOC
K84 
BLOC
K83 
BLOC
K82 
BLOC
K81 
BLOC
K80 
W
Reset
0
0
0
0
0
0
0
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
BLOC
K79 
BLOC
K78 
BLOC
K77 
BLOC
K76 
BLOC
K75 
BLOC
K74 
BLOC
K73 
BLOC
K72 
0
BLOC
K70 
BLOC
K69 
BLOC
K68 
BLOC
K67 
0
BLOC
K65 
BLOC
K64 
W
Reset
0
0
0
0
0
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
Fields
Field
Function
31
IP block status
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1863 / 5251


---
# 페이지 206

Table continued from the previous page...
Field
Function
BLOCK95
This bit provides the clock status of FlexCAN 11 in partition 2.
0b - Clock is not running.
1b - Clock is running.
30
BLOCK94
IP block status
This bit provides the clock status of FlexCAN 10 in partition 2.
0b - Clock is not running.
1b - Clock is running.
29
BLOCK93
IP block status
This bit provides the clock status of FlexCAN 9 in partition 2.
0b - Clock is not running.
1b - Clock is running.
28
BLOCK92
IP block status
This bit provides the clock status of FlexCAN 8 in partition 2.
0b - Clock is not running.
1b - Clock is running.
27
BLOCK91
IP block status
This bit provides the clock status of AES Application 7 in partition 2.
0b - Clock is not running.
1b - Clock is running.
26
BLOCK90
IP block status
This bit provides the clock status of AES Application 7 in partition 2.
0b - Clock is not running.
1b - Clock is running.
25
BLOCK89
IP block status
This bit provides the clock status of AES Application 7 in partition 2.
0b - Clock is not running.
1b - Clock is running.
24
BLOCK88
IP block status
This bit provides the clock status of AES Application 7 in partition 2.
0b - Clock is not running.
1b - Clock is running.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1864 / 5251


---
# 페이지 207

Table continued from the previous page...
Field
Function
23
BLOCK87
IP block status
This bit provides the clock status of AES Application 6 in partition 2.
0b - Clock is not running.
1b - Clock is running.
22
BLOCK86
IP block status
This bit provides the clock status of AES Application 6 in partition 2.
0b - Clock is not running.
1b - Clock is running.
21
BLOCK85
IP block status
This bit provides the clock status of AES Application 6 in partition 2.
0b - Clock is not running.
1b - Clock is running.
20
BLOCK84
IP block status
This bit provides the clock status of AES Application 6 in partition 2.
0b - Clock is not running.
1b - Clock is running.
19
BLOCK83
IP block status
This bit provides the clock status of AES Application 5 in partition 2.
0b - Clock is not running.
1b - Clock is running.
18
BLOCK82
IP block status
This bit provides the clock status of AES Application 5 in partition 2.
0b - Clock is not running.
1b - Clock is running.
17
BLOCK81
IP block status
This bit provides the clock status of AES Application 5 in partition 2.
0b - Clock is not running.
1b - Clock is running.
16
BLOCK80
IP block status
This bit provides the clock status of AES Application 5 in partition 2.
0b - Clock is not running.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1865 / 5251


---
# 페이지 208

Table continued from the previous page...
Field
Function
1b - Clock is running.
15
BLOCK79
IP block status
This bit provides the clock status of AES Application 4 in partition 2.
0b - Clock is not running.
1b - Clock is running.
14
BLOCK78
IP block status
This bit provides the clock status of AES Application 4 in partition 2.
0b - Clock is not running.
1b - Clock is running.
13
BLOCK77
IP block status
This bit provides the clock status of AES Application 4 in partition 2.
0b - Clock is not running.
1b - Clock is running.
12
BLOCK76
IP block status
This bit provides the clock status of AES Application 4 in partition 2.
0b - Clock is not running.
1b - Clock is running.
11
BLOCK75
IP block status
This bit provides the clock status of AES Application 3 in partition 2.
0b - Clock is not running.
1b - Clock is running.
10
BLOCK74
IP block status
This bit provides the clock status of AES Application 3 in partition 2.
0b - Clock is not running.
1b - Clock is running.
9
BLOCK73
IP block status
This bit provides the clock status of AES Application 3 in partition 2.
0b - Clock is not running.
1b - Clock is running.
8
BLOCK72
IP block status
This bit provides the clock status of AES Application 3 in partition 2.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1866 / 5251


---
# 페이지 209

Table continued from the previous page...
Field
Function
0b - Clock is not running.
1b - Clock is running.
7
—
Reserved
This field is reserved and read returns zeros.
6
BLOCK70
IP block status
This bit provides the clock status of EIM 3 in partition 2.
0b - Clock is not running.
1b - Clock is running.
5
BLOCK69
IP block status
This bit provides the clock status of EIM 2 in partition 2.
0b - Clock is not running.
1b - Clock is running.
4
BLOCK68
IP block status
This bit provides the clock status of EIM 1 in partition 2.
0b - Clock is not running.
1b - Clock is running.
3
BLOCK67
IP block status
This bit provides the clock status of EIM 0 in partition 2.
0b - Clock is not running.
1b - Clock is running.
2
—
Reserved
This field is reserved and read returns zeros.
1
BLOCK65
IP block status
This bit provides the clock status of block 65 in partition 2.
0b - Clock is not running.
1b - Clock is running.
0
BLOCK64
IP block status
This bit provides the clock status of block 64 in partition 2.
0b - Clock is not running.
1b - Clock is running.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1867 / 5251


---
# 페이지 210

46.7.54 Partition 2 COFB Set 3 Clock Status Register (PRTN2_COFB3_STAT)
Offset
Register
Offset
PRTN2_COFB3_STAT
51Ch
Function
This register provides the status of set 3 of COFBs inside partition 2.
 
The reset value of this register can vary depending on the availability of active clock pulses inside partition 2.
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
0
0
0
0
0
0
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
0
0
0
0
0
0
0
0
BLOC
K98 
BLOC
K97 
BLOC
K96 
W
Reset
0
0
0
0
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
Fields
Field
Function
31
—
Reserved
This field is reserved and read returns zeros.
30
—
Reserved
This field is reserved and read returns zeros.
29
—
Reserved
This field is reserved and read returns zeros.
28
—
Reserved
This field is reserved and read returns zeros.
27
—
Reserved
This field is reserved and read returns zeros.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1868 / 5251


---
# 페이지 211

Table continued from the previous page...
Field
Function
26
—
Reserved
This field is reserved and read returns zeros.
25
—
Reserved
This field is reserved and read returns zeros.
24
—
Reserved
This field is reserved and read returns zeros.
23
—
Reserved
This field is reserved and read returns zeros.
22
—
Reserved
This field is reserved and read returns zeros.
21
—
Reserved
This field is reserved and read returns zeros.
20
—
Reserved
This field is reserved and read returns zeros.
19
—
Reserved
This field is reserved and read returns zeros.
18
—
Reserved
This field is reserved and read returns zeros.
17
—
Reserved
This field is reserved and read returns zeros.
16
—
Reserved
This field is reserved and read returns zeros.
15
—
Reserved
This field is reserved and read returns zeros.
14
—
Reserved
This field is reserved and read returns zeros.
13
—
Reserved
This field is reserved and read returns zeros.
12
Reserved
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1869 / 5251


---
# 페이지 212

Table continued from the previous page...
Field
Function
—
This field is reserved and read returns zeros.
11
—
Reserved
This field is reserved and read returns zeros.
10
—
Reserved
This field is reserved and read returns zeros.
9
—
Reserved
This field is reserved and read returns zeros.
8
—
Reserved
This field is reserved and read returns zeros.
7
—
Reserved
This field is reserved and read returns zeros.
6
—
Reserved
This field is reserved and read returns zeros.
5
—
Reserved
This field is reserved and read returns zeros.
4
—
Reserved
This field is reserved and read returns zeros.
3
—
Reserved
This field is reserved and read returns zeros.
2
BLOCK98
IP block status
This bit provides the clock status of block 98 in partition 2.
0b - Clock is not running.
1b - Clock is running.
1
BLOCK97
IP block status
This bit provides the clock status of block 97 in partition 2.
0b - Clock is not running.
1b - Clock is running.
0
BLOCK96
IP block status
This bit provides the clock status of block 96 in partition 2.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1870 / 5251


---
# 페이지 213

Table continued from the previous page...
Field
Function
0b - Clock is not running.
1b - Clock is running.
46.7.55 Partition 2 COFB Set 0 Clock Enable Register (PRTN2_COFB0_CLKEN)
Offset
Register
Offset
PRTN2_COFB0_CLKEN
530h
Function
This register provides clock control signaling to the individual COFBs in set 0 inside partition 2. Whenever a partition clock enable 
(non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock 
to the corresponding block in the partition.
 
The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific 
MC_ME information for clock source availability.
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
REQ3
1 
REQ3
0 
REQ2
9 
REQ2
8 
REQ2
7 
0
0
REQ2
4 
REQ2
3 
REQ2
2 
REQ2
1 
REQ2
0 
REQ1
9 
REQ1
8 
REQ1
7 
REQ1
6 
W
Reset
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
REQ1
5 
REQ1
4 
REQ1
3 
REQ1
2 
REQ1
1 
REQ1
0 
REQ9 
REQ8 
REQ7 
REQ6 
REQ5 
REQ4 
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
1
1
1
1
Fields
Field
Function
31
REQ31
Clock enable
This bit provides the clock enable control for STM 3 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1871 / 5251


---
# 페이지 214

Table continued from the previous page...
Field
Function
30
REQ30
Clock enable
This bit provides the clock enable control for STM 2 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
29
REQ29
Clock enable
This bit provides the clock enable control for STM 1 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
28
REQ28
Clock enable
This bit provides the clock enable control for SWT 2 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
27
REQ27
Clock enable
This bit provides the clock enable control for SWT 1 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
26
—
Reserved
This field is reserved and read returns zeros.
25
—
Reserved
This field is reserved and read returns zeros.
24
REQ24
Clock enable
This bit provides the clock enable control for SEMA42 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
23
REQ23
Clock enable
This bit provides the clock enable control for eDMA TCD 31 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
22
REQ22
Clock enable
This bit provides the clock enable control for eDMA TCD 30 in partition 2.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1872 / 5251


---
# 페이지 215

Table continued from the previous page...
Field
Function
0b - Clock is turned off.
1b - Clock is turned on.
21
REQ21
Clock enable
This bit provides the clock enable control for eDMA TCD 29 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
20
REQ20
Clock enable
This bit provides the clock enable control for eDMA TCD 28 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
19
REQ19
Clock enable
This bit provides the clock enable control for eDMA TCD 27 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
18
REQ18
Clock enable
This bit provides the clock enable control for eDMA TCD 26 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
17
REQ17
Clock enable
This bit provides the clock enable control for eDMA TCD 25 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
16
REQ16
Clock enable
This bit provides the clock enable control for eDMA TCD 24 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
15
REQ15
Clock enable
This bit provides the clock enable control for eDMA TCD 23 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
14
Clock enable
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1873 / 5251


---
# 페이지 216

Table continued from the previous page...
Field
Function
REQ14
This bit provides the clock enable control for eDMA TCD 22 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
13
REQ13
Clock enable
This bit provides the clock enable control for eDMA TCD 21 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
12
REQ12
Clock enable
This bit provides the clock enable control for eDMA TCD 20 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
11
REQ11
Clock enable
This bit provides the clock enable control for eDMA TCD 19 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
10
REQ10
Clock enable
This bit provides the clock enable control for eDMA TCD 18 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
9
REQ9
Clock enable
This bit provides the clock enable control for eDMA TCD 17 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
8
REQ8
Clock enable
This bit provides the clock enable control for eDMA TCD 16 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
7
REQ7
Clock enable
This bit provides the clock enable control for eDMA TCD 15 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1874 / 5251


---
# 페이지 217

Table continued from the previous page...
Field
Function
6
REQ6
Clock enable
This bit provides the clock enable control for eDMA TCD 14 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
5
REQ5
Clock enable
This bit provides the clock enable control for eDMA TCD 13 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
4
REQ4
Clock enable
This bit provides the clock enable control for eDMA TCD 12 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
3
—
Reserved
This field is reserved and read returns zeros.
2
—
Reserved
This field is reserved and read returns zeros.
1
—
Reserved
This field is reserved and read returns zeros.
0
—
Reserved
This field is reserved and read returns zeros.
46.7.56 Partition 2 COFB Set 1 Clock Enable Register (PRTN2_COFB1_CLKEN)
Offset
Register
Offset
PRTN2_COFB1_CLKEN
534h
Function
This register provides clock control signaling to the individual COFBs in set 1 inside partition 2. Whenever a partition clock enable 
(non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock 
to the corresponding block in the partition.
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1875 / 5251


---
# 페이지 218

 
The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific 
MC_ME information for clock source availability.
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
REQ6
3 
REQ6
2 
0
0
0
REQ5
8 
0
0
REQ5
5 
0
0
0
REQ5
1 
0
0
REQ4
8 
W
Reset
1
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
REQ4
7 
0
0
0
0
REQ4
2 
REQ4
1 
REQ4
0 
REQ3
9 
REQ3
8 
REQ3
7 
REQ3
6 
REQ3
5 
REQ3
4 
REQ3
3 
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
REQ63
Clock enable
This bit provides the clock enable control for block 63 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
30
REQ62
Clock enable
This bit provides the clock enable control for block 62 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
29
—
Reserved
This field is reserved and read returns zeros.
28
—
Reserved
This field is reserved and read returns zeros.
27
—
Reserved
This field is reserved and read returns zeros.
26
REQ58
Clock enable
This bit provides the clock enable control for LPCMP 2 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1876 / 5251


---
# 페이지 219

Table continued from the previous page...
Field
Function
25
—
Reserved
This field is reserved and read returns zeros.
24
—
Reserved
This field is reserved and read returns zeros.
23
REQ55
Clock enable
This bit provides the clock enable control for SAI 1 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
22
—
Reserved
This field is reserved and read returns zeros.
21
—
Reserved
This field is reserved and read returns zeros.
20
—
Reserved
This field is reserved and read returns zeros.
19
REQ51
Clock enable
This bit provides the clock enable control for QuadSPI in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
18
—
Reserved
This field is reserved and read returns zeros.
17
—
Reserved
This field is reserved and read returns zeros.
16
REQ48
Clock enable
This bit provides the clock enable control for LPSPI 5 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
15
REQ47
Clock enable
This bit provides the clock enable control for LPSPI 4 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1877 / 5251


---
# 페이지 220

Table continued from the previous page...
Field
Function
14
—
Reserved
This field is reserved and read returns zeros.
13
—
Reserved
This field is reserved and read returns zeros.
12
—
Reserved
This field is reserved and read returns zeros.
11
—
Reserved
This field is reserved and read returns zeros.
10
REQ42
Clock enable
This bit provides the clock enable control for LPUART 15 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
9
REQ41
Clock enable
This bit provides the clock enable control for LPUART 14 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
8
REQ40
Clock enable
This bit provides the clock enable control for LPUART 13 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
7
REQ39
Clock enable
This bit provides the clock enable control for LPUART 12 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
6
REQ38
Clock enable
This bit provides the clock enable control for LPUART 11 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
5
REQ37
Clock enable
This bit provides the clock enable control for LPUART 10 in partition 2.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1878 / 5251


---
# 페이지 221

Table continued from the previous page...
Field
Function
0b - Clock is turned off.
1b - Clock is turned on.
4
REQ36
Clock enable
This bit provides the clock enable control for LPUART 9 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
3
REQ35
Clock enable
This bit provides the clock enable control for LPUART 8 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
2
REQ34
Clock enable
This bit provides the clock enable control for GMAC 1 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
1
REQ33
Clock enable
This bit provides the clock enable control for GMAC 0 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
0
—
Reserved
This field is reserved and read returns zeros.
46.7.57 Partition 2 COFB Set 2 Clock Enable Register (PRTN2_COFB2_CLKEN)
Offset
Register
Offset
PRTN2_COFB2_CLKEN
538h
Function
This register provides clock control signaling to the individual COFBs in set 2 inside partition 2. Whenever a partition clock enable 
(non-core) hardware process is initiated, the value of logic-1 in the corresponding bit locations of this register enables the clock 
to the corresponding block in the partition.
 
The reset value of this register is not defined and is as per the availability of the clock source. See Chip-specific 
MC_ME information for clock source availability.
  NOTE  
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1879 / 5251


---
# 페이지 222

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
REQ9
5 
REQ9
4 
REQ9
3 
REQ9
2 
REQ9
1 
REQ9
0 
REQ8
9 
REQ8
8 
REQ8
7 
REQ8
6 
REQ8
5 
REQ8
4 
REQ8
3 
REQ8
2 
REQ8
1 
REQ8
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
REQ7
9 
REQ7
8 
REQ7
7 
REQ7
6 
REQ7
5 
REQ7
4 
REQ7
3 
REQ7
2 
0
REQ7
0 
REQ6
9 
REQ6
8 
REQ6
7 
0
REQ6
5 
REQ6
4 
W
Reset
0
0
0
0
0
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
Fields
Field
Function
31
REQ95
Clock enable
This bit provides the clock enable control for FlexCAN 11 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
30
REQ94
Clock enable
This bit provides the clock enable control for FlexCAN 10 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
29
REQ93
Clock enable
This bit provides the clock enable control for FlexCAN 9 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
28
REQ92
Clock enable
This bit provides the clock enable control for FlexCAN 8 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
27
REQ91
Clock enable
This bit provides the clock enable control for AES Application 7 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
26
REQ90
Clock enable
This bit provides the clock enable control for AES Application 7 in partition 2.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1880 / 5251


---
# 페이지 223

Table continued from the previous page...
Field
Function
0b - Clock is turned off.
1b - Clock is turned on.
25
REQ89
Clock enable
This bit provides the clock enable control for AES Application 7 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
24
REQ88
Clock enable
This bit provides the clock enable control for AES Application 7 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
23
REQ87
Clock enable
This bit provides the clock enable control for AES Application 6 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
22
REQ86
Clock enable
This bit provides the clock enable control for AES Application 6 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
21
REQ85
Clock enable
This bit provides the clock enable control for AES Application 6 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
20
REQ84
Clock enable
This bit provides the clock enable control for AES Application 6 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
19
REQ83
Clock enable
This bit provides the clock enable control for AES Application 5 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
18
Clock enable
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1881 / 5251


---
# 페이지 224

Table continued from the previous page...
Field
Function
REQ82
This bit provides the clock enable control for AES Application 5 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
17
REQ81
Clock enable
This bit provides the clock enable control for AES Application 5 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
16
REQ80
Clock enable
This bit provides the clock enable control for AES Application 5 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
15
REQ79
Clock enable
This bit provides the clock enable control for AES Application 4 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
14
REQ78
Clock enable
This bit provides the clock enable control for AES Application 4 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
13
REQ77
Clock enable
This bit provides the clock enable control for AES Application 4 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
12
REQ76
Clock enable
This bit provides the clock enable control for AES Application 4 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
11
REQ75
Clock enable
This bit provides the clock enable control for AES Application 3 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1882 / 5251


---
# 페이지 225

Table continued from the previous page...
Field
Function
10
REQ74
Clock enable
This bit provides the clock enable control for AES Application 3 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
9
REQ73
Clock enable
This bit provides the clock enable control for AES Application 3 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
8
REQ72
Clock enable
This bit provides the clock enable control for AES Application 3 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
7
—
Reserved
This field is reserved and read returns zeros.
6
REQ70
Clock enable
This bit provides the clock enable control for EIM 3 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
5
REQ69
Clock enable
This bit provides the clock enable control for EIM 2 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
4
REQ68
Clock enable
This bit provides the clock enable control for EIM 1 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
3
REQ67
Clock enable
This bit provides the clock enable control for EIM 0 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
2
Reserved
Table continues on the next page...
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1883 / 5251


---
# 페이지 226

Table continued from the previous page...
Field
Function
—
This field is reserved and read returns zeros.
1
REQ65
Clock enable
This bit provides the clock enable control for block 65 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
0
REQ64
Clock enable
This bit provides the clock enable control for block 64 in partition 2.
0b - Clock is turned off.
1b - Clock is turned on.
46.8 Glossary
WFI
Wait for interrupt
COFB
Collection of functional blocks also referred as number of peripherals
NXP Semiconductors
Mode Entry Module (MC_ME)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1884 / 5251


---