# 페이지 424

Chapter 65
Trigger MUX (TRGMUX)
65.1 Chip-specific TRGMUX information
65.1.1 TRGMUX input output configuration and instances
This chip has one instance of TRGMUX module.
The device supports the triggering scheme between peripherals. For the supported trigger sources and destination, see the 
TRGMUX connectivity file attached to this document.
This device has 16 pads (SIUL2) mapped from TRGMUX inputs and TRGMUX outputs are mapped to the eMIOS channels, hence 
two timers channels can use a single pin of the device to do input capture.
While using TRGMUX, below points need to be taken care: 
• User must ensure the minimum pulse of 100 ns on SIUL2 pads when using them as trigger source on TRGMUX.
• Pulses which are visible on pads depends on the pad type. Different pad supports different frequencies. For more details on 
pad types and their respective bandwidth, see section "IO signal table" in "Signal Multiplexing" chapter.
• End of conversion (EOC) signals of ADC modules are mapped on TRGMUX inputs as trigger sources. The EOC signal is 
asserted after ADC conversion regardless whether conversion is signaled by polling flags, interrupt or DMA transfer. The 
signal shall not be used to start injected conversion on same ADC channel as it will overwrite current result register.
• The minimum pulse length requirement is 1.5X of destination clock, so that it gets properly sampled at the destination IP 
connected to TRGMUX outputs, otherwise there are chances of missing the triggers generated from source. For example, the 
trigger generated from PAD for ADC conversion should be kept high/low for at least 1.5X of ADC clock so that it gets sampled 
in ADC clock domain. To ensure this, pulse strechers have been placed before some of the hardware modules mapped on 
TRGMUX outputs.
• Some PADS are being shared by both ADC and TRGMUX. It is recommended that trigger initiated from such PADS should 
not be used to trigger a conversion on the ADC channel mapped on same PAD. Failing to do this will cause congestion on 
same PAD.
• Out of all the pads mapped on TRGMUX, first four pads have glitch filters. For details, see the TRGMUX connectivity 
file attached to this document. The trigger pulse width should honour the pulse width requirement as per Glitch Filter 
specifications. The same signal can be observed at output pin if the pulse width of the input data signal is more than 400ns 
and no output signal should be observed if the pulse width of the input data signal is less than 20ns. A signal with a pulse width 
that is between 20ns and 400 ns should not be applied as the behavior is not guaranteed.
• Trigger outputs are grouped peripheral-wise and have a common lock bit based on TRGMUX REGx. For instance, 
normal_trigger, injected_trigger and external_sync of ADC_0 are grouped onto TRGMUX_REG0 and have a common lock bit.
65.1.2 Pulse strechers in TRGMUX
TRGMUX has some hardware modules on its input side running at faster clock than some of the IPs present on output side. For 
instance, eMIOS reload outputs running at 160 MHz can trigger LPI2C trigger input clocked at 40 MHz, in that case there is a high 
chance that trigger from eMIOS will be missed. Following Pulse strechers are added for the IPs on output side of TRGMUX.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2733 / 5251


---
# 페이지 425

Table 428. Pulse strechers in TRGMUX
Evaluation 
Parameter
ADC_0/1/2 
external trigger 
to sync the start 
pulse
BCTU trigger 
23/47/71
FlexIO trigger 
input_0/1/2/31
LPI2C_0 
Trigger input
LPSPI_0/1/2 
Trigger input
CM7_0/1/2/3 
RXEV
IP expects
Synchronized 
single cycle 
pulse
Synchronized 
pulse
IP requirement 
is to have 2 
cycle pulse of 
flexio_clk
IP requirement 
is to have 2 
cycle pulse of 
lpi2c_clk
IP requirement 
is to have 2 
cycle pulse of 
lpspi_clk
Single cycle 
pulse
Frequency
CORE_CLK
CORE_CLK
CORE_CLK
AIPS_SLOW_C
LK
LPSPI_0 - 
PLAT_AIPS_CL
K
LPSPI_1/2/3 - 
AIPS_SLOW_C
LK
CORE_CLK
Inside IP
Used as combo 
signal
Flopped inside 
IP and clear 
after ADC 
conversion 
completed
Synchronized 
inside IP
Synchronized 
inside IP
Synchronized 
inside IP
-
At SoC
Since it an 
ASYNC signal 
and IP required 
synchronized 
single cycle 
pulse, so a pulse 
stretcher is 
added to convert 
pulse from any 
frequency 
domain into a 
single cycle 
pulse of 
CORE_CLK
Since slow IP 
such as LPCMP 
or from PAD can 
also trigger 
BCTU and 
BCTU wants 
that trigger 
should clear 
after the ADC 
conversion. So a 
pulse stretcher 
is added which 
convert any size 
of pulse to a 
single cycle 
pulse of BCTU 
clock 
(CORE_CLK)
Pulse stretcher 
is added to 
convert any 
pulse into a two 
cycle pulse of 
FLEXIO_CLK
Pulse stretcher 
is added to 
convert any 
pulse into a two 
cycle pulse of 
LPI2C_CLK
Pulse stretcher 
is added to 
convert any 
pulse into a two 
cycle pulse of 
LPSPI_CLK
Pulse stretcher 
is added to 
convert any 
pulse into a 
single cycle 
pulse of 
CORE_CLK
Output slot at 
which pulse 
stretcher is 
added
2, 6, 10
24, 25, 26
64, 65, 66, 67
84
88, 92, 96
156, 157, 1582, 
1593
1. These pulse stretchers are available in S32K314, S32K324 and S32K344 variants only.
2. CM7_2 is applicable for S32K358/S32K348/S32K338/S32K328 only.
3. CM7_3 is applicable for S32K388/S32K389 only.
 
The trigger outputs which have pulse stretcher before them, there should be atleast a gap of 5 cycle of destination 
clock for back to back trigger.
  NOTE  
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2734 / 5251


---
# 페이지 426

65.1.3 Trigger monitor
A trigger monitor is added before the TRGMUX inputs ADC12_0_EOC, ADC12_1_EOC and ADC12_2_EOC. You can configure 
the UDR registers in SIUL2 to select which trigger needs to propagate to the above TRGMUX inputs. By default after coming out 
of reset, all the enables are 0. Hence no trigger will be coming to these 3 TRGMUX inputs.
TRGMUX
Trigger monitor signals
Figure 379. Trigger monitor
 
Trigger monitor is not present in S32K314, S32K324 and S32K344.
  NOTE  
65.2 Overview
TRGMUX allows you to configure the trigger inputs for various peripherals.
65.2.1 Block diagram
Trigger disabled
TRGMUX
...000
Trigger input 1
...001
Trigger input 2
...010
Trigger input 3
...011
Trigger input 4
...100
Trigger input 5
...101
Trigger input 6
...110
Trigger input 7
...111
Output x
Up to four outputs per peripheral
To peripheral
trigger inputs
[SEL0] selects the trigger for output 0
[SEL1] selects the trigger for output 1
[SEL2] selects the trigger for output 2
[SEL3] selects the trigger for output 3
[SELx]
Trigger input N*
Figure 380. Block diagram
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2735 / 5251


---
# 페이지 427

 
Up to 255 trigger inputs may be available for SEL0, SEL1, and SEL2. For SEL3, up to 127 trigger inputs may 
be available. When the number of trigger inputs is 255, SEL3 is not available and becomes reserved. See the 
chip-specific TRGMUX information for details about trigger input and output configuration on this chip.
  NOTE  
65.2.2 Features
• Configurable trigger sources for peripherals
• Dedicated TRGMUX register for each peripheral
65.3 Functional description
65.3.1 Clocking
This module has no clocking considerations.
65.3.2 Interrupts
This module has no interrupts.
65.4 External signals
This module has no external signals.
65.5 Initialization
This module does not require initialization.
65.6 TRGMUX register descriptions
65.6.1 TRGMUX memory map
You can only write to TRGMUX registers in Supervisor mode.
Table 429. Select bit fields
Field
Description
SELx
Specifies the MUX select for the peripheral trigger inputs. Use this field to select the trigger sources for 
peripheral modules.
0h - LOGIC 0 (VSS)
1h - LOGIC 1 (VDD)
2h - ADC12_0_EOC
3h - ADC12_1_EOC
4h - ADC12_2_EOC
5h - LPCMP_0_COUT output
6h - LPCMP_1_COUT output
7h - LPCMP_2_COUT output
8h - eDMA_eDMA_0 DONE
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2736 / 5251


---
# 페이지 428

Table 429. Select bit fields
Field
Description
9h - eDMA_eDMA_1 DONE
Ah - eDMA_eDMA_16 DONE
Bh - eDMA_eDMA_17 DONE
Ch - eMIOS_0_RELOAD_OUT_CH[23]
Dh - eMIOS_0_RELOAD_OUT_CH[22]
Eh - eMIOS_0_RELOAD_OUT_CH[8]
Fh - eMIOS_0_RELOAD_OUT_CH[0]
10h - eMIOS_0_IPP_DO_eMIOS_CH[0]
11h - eMIOS_0_IPP_DO_eMIOS_CH[1]
12h - eMIOS_0_IPP_DO_eMIOS_CH[2]
13h - eMIOS_0_IPP_DO_eMIOS_CH[3]
14h - eMIOS_0_IPP_DO_eMIOS_CH[4]
15h - eMIOS_0_IPP_DO_eMIOS_CH[5]
16h - eMIOS_0_IPP_DO_eMIOS_CH[6]
17h - eMIOS_0_IPP_DO_eMIOS_CH[7]
18h - eMIOS_0_IPP_DO_eMIOS_CH[8]
19h - eMIOS_0_IPP_DO_eMIOS_CH[9]
1Ah - eMIOS_0_IPP_DO_eMIOS_CH[10]
1Bh - eMIOS_0_IPP_DO_eMIOS_CH[11]
1Ch - eMIOS_0_IPP_DO_eMIOS_CH[12]
1Dh - eMIOS_0_IPP_DO_eMIOS_CH[13]
1Eh - eMIOS_0_IPP_DO_eMIOS_CH[14]
1Fh - eMIOS_0_IPP_DO_eMIOS_CH[15]
20h - eMIOS_0_IPP_DO_eMIOS_CH[22]
21h - eMIOS_0_IPP_DO_eMIOS_CH[23]
22h - eMIOS_1_RELOAD_OUT_CH[23]
23h - eMIOS_1_RELOAD_OUT_CH[22]
24h - eMIOS_1_RELOAD_OUT_CH[8]
25h - eMIOS_1_RELOAD_OUT_CH[0]
26h - eMIOS_1_IPP_DO_eMIOS_CH[0]
27h - eMIOS_1_IPP_DO_eMIOS_CH[1]
28h - eMIOS_1_IPP_DO_eMIOS_CH[2]
29h - eMIOS_1_IPP_DO_eMIOS_CH[3]
2Ah - eMIOS_1_IPP_DO_eMIOS_CH[4]
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2737 / 5251


---
# 페이지 429

Table 429. Select bit fields
Field
Description
2Bh - eMIOS_1_IPP_DO_eMIOS_CH[5]
2Ch - eMIOS_1_IPP_DO_eMIOS_CH[6]
2Dh - eMIOS_1_IPP_DO_eMIOS_CH[7]
2Eh - eMIOS_1_IPP_DO_eMIOS_CH[8]
2Fh - eMIOS_1_IPP_DO_eMIOS_CH[9]
30h - eMIOS_1_IPP_DO_eMIOS_CH[10]
31h - eMIOS_1_IPP_DO_eMIOS_CH[11]
32h - eMIOS_1_IPP_DO_eMIOS_CH[12]
33h - eMIOS_1_IPP_DO_eMIOS_CH[13]
34h - eMIOS_1_IPP_DO_eMIOS_CH[14]
35h - eMIOS_1_IPP_DO_eMIOS_CH[15]
36h - eMIOS_1_IPP_DO_eMIOS_CH[22]
37h - eMIOS_1_IPP_DO_eMIOS_CH[23]
38h - FlexIO_External Output Trigger 0
39h - FlexIO_External Output Trigger 1
3Ah - FlexIO_External Output Trigger 2
3Bh - FlexIO_External Output Trigger 3
3Ch - SIUL_TRGMUX_IN0
3Dh - SIUL_TRGMUX_IN1
3Eh - SIUL_TRGMUX_IN2
3Fh - SIUL_TRGMUX_IN3
40h - SIUL_TRGMUX_IN4
41h - SIUL_TRGMUX_IN5
42h - SIUL_TRGMUX_IN6
43h - SIUL_TRGMUX_IN7
44h - SIUL_TRGMUX_IN8
45h - SIUL_TRGMUX_IN9
46h - SIUL_TRGMUX_IN10
47h - SIUL_TRGMUX_IN11
48h - SIUL_TRGMUX_IN12
49h - SIUL_TRGMUX_IN13
4Ah - SIUL_TRGMUX_IN14
4Bh - SIUL_TRGMUX_IN15
4Ch - LPI2C_0_Master trigger output
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2738 / 5251


---
# 페이지 430

Table 429. Select bit fields
Field
Description
4Dh - LPI2C_0_Slave trigger output
4Eh - LPSPI_0_End of frame trigger
4Fh - LPSPI_0_Receive data trigger
50h - LPSPI_1_End of frame trigger
51h - LPSPI_1_Receive data trigger
52h - LPSPI_2_End of frame trigger
53h - LPSPI_2_Receive data trigger
54h - LPUART_0_trg_txword
55h - LPUART_0_trg_rxword
56h - LPUART_0_trg_rxidle
57h - LPUART_1_trg_txword
58h - LPUART_1_trg_rxword
59h - LPUART_1_trg_rxidle
5Ah - LPUART_2_trg_txword
5Bh - LPUART_2_trg_rxword
5Ch - LPUART_2_trg_rxidle
5Dh - LCU_0_LC1_out_i1
5Eh - LCU_0_LC1_out_i2
5Fh - LCU_0_LC1_out_i3
60h - LCU_0_LC1_out_i4
61h - LCU_0_LC2_out_i1
62h - LCU_0_LC2_out_i2
63h - LCU_0_LC2_out_i3
64h - LCU_0_LC2_out_i4
65h - LCU_0_LC3_out_i1
66h - LCU_0_LC3_out_i2
67h - LCU_0_LC3_out_i3
68h - LCU_0_LC3_out_i4
69h - LCU_1_LC1_out_i1
6Ah - LCU_1_LC1_out_i2
6Bh - LCU_1_LC1_out_i3
6Ch - LCU_1_LC1_out_i4
6Dh - LCU_1_LC2_out_i1
6Eh - LCU_1_LC2_out_i2
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2739 / 5251


---
# 페이지 431

Table 429. Select bit fields
Field
Description
6Fh - LCU_1_LC2_out_i3
70h - LCU_1_LC2_out_i4
71h - LCU_1_LC3_out_i1
72h - LCU_1_LC3_out_i2
73h - LCU_1_LC3_out_i3
74h - LCU_1_LC3_out_i4
75h - PIT0_PIT0 CH0
76h - PIT0_PIT0 CH1
77h - PIT0_PIT0 CH2
78h - PIT0_PIT0 CH3
79h - PIT0_PIT0 CH4 RTI
7Ah - PIT1_PIT1 CH0
7Bh - PIT1_PIT1 CH1
7Ch - PIT1_PIT1 CH2
7Dh - PIT1_PIT1 CH3
7Eh - CM7_0_TXEV
7Fh - CM7_1_TXEV
TRGMUX base address: 4008_0000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
TRGMUX ADC12_0 (ADC12_0)
32
RW
0000_0000h
4h
TRGMUX ADC12_1 (ADC12_1)
32
RW
0000_0000h
8h
TRGMUX ADC12_2 (ADC12_2)
32
RW
0000_0000h
Ch
TRGMUX LPCMP_0 (LPCMP_0)
32
RW
0000_0000h
10h
TRGMUX LPCMP_1 (LPCMP_1)
32
RW
0000_0000h
14h
TRGMUX LPCMP_2 (LPCMP_2)
32
RW
0000_0000h
18h
TRGMUX BCTU (BCTU)
32
RW
0000_0000h
1Ch
TRGMUX eMIOS012_ODIS (eMIOS012_ODIS)
32
RW
0000_0000h
20h
TRGMUX eMIOS0_0 (eMIOS0_0)
32
RW
0000_0000h
24h
TRGMUX eMIOS0_1 (eMIOS0_1)
32
RW
0000_0000h
28h
TRGMUX eMIOS0_2 (eMIOS0_2)
32
RW
0000_0000h
2Ch
TRGMUX eMIOS0_3 (eMIOS0_3)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2740 / 5251


---
# 페이지 432

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
30h
TRGMUX eMIOS1_0 (eMIOS1_0)
32
RW
0000_0000h
34h
TRGMUX eMIOS1_1 (eMIOS1_1)
32
RW
0000_0000h
38h
TRGMUX eMIOS1_2 (eMIOS1_2)
32
RW
0000_0000h
3Ch
TRGMUX eMIOS1_3 (eMIOS1_3)
32
RW
0000_0000h
40h
TRGMUX FlexIO (FlexIO)
32
RW
0000_0000h
44h
TRGMUX SIUL_OUT0 (SIUL_OUT0)
32
RW
0000_0000h
48h
TRGMUX SIUL_OUT1 (SIUL_OUT1)
32
RW
0000_0000h
4Ch
TRGMUX SIUL_OUT2 (SIUL_OUT2)
32
RW
0000_0000h
50h
TRGMUX SIUL_OUT3 (SIUL_OUT3)
32
RW
0000_0000h
54h
TRGMUX LPI2C_0 (LPI2C_0)
32
RW
0000_0000h
58h
TRGMUX LPSPI_0 (LPSPI_0)
32
RW
0000_0000h
5Ch
TRGMUX LPSPI_1 (LPSPI_1)
32
RW
0000_0000h
60h
TRGMUX LPSPI_2 (LPSPI_2)
32
RW
0000_0000h
64h
TRGMUX LPUART_0 (LPUART_0)
32
RW
0000_0000h
68h
TRGMUX LPUART_1 (LPUART_1)
32
RW
0000_0000h
6Ch
TRGMUX LPUART_2 (LPUART_2)
32
RW
0000_0000h
70h
TRGMUX LPUART_3 (LPUART_3)
32
RW
0000_0000h
74h
TRGMUX LCU0_SYNC (LCU0_SYNC)
32
RW
0000_0000h
78h
TRGMUX LCU0_FORCE (LCU0_FORCE)
32
RW
0000_0000h
7Ch
TRGMUX LCU0_0 (LCU0_0)
32
RW
0000_0000h
80h
TRGMUX LCU0_1 (LCU0_1)
32
RW
0000_0000h
84h
TRGMUX LCU0_2 (LCU0_2)
32
RW
0000_0000h
88h
TRGMUX LCU1_SYNC (LCU1_SYNC)
32
RW
0000_0000h
8Ch
TRGMUX LCU1_FORCE (LCU1_FORCE)
32
RW
0000_0000h
90h
TRGMUX LCU1_0 (LCU1_0)
32
RW
0000_0000h
94h
TRGMUX LCU1_1 (LCU1_1)
32
RW
0000_0000h
98h
TRGMUX LCU1_2 (LCU1_2)
32
RW
0000_0000h
9Ch
TRGMUX CM7_RXEV (CM7_RXEV)
32
RW
0000_0000h
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2741 / 5251


---
# 페이지 433

65.6.2 TRGMUX ADC12_0 (ADC12_0)
Offset
Register
Offset
ADC12_0
0h
Function
Configures the ADC12_0 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
0
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2742 / 5251


---
# 페이지 434

Table continued from the previous page...
Field
Function
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.3 TRGMUX ADC12_1 (ADC12_1)
Offset
Register
Offset
ADC12_1
4h
Function
Configures the ADC12_1 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
0
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2743 / 5251


---
# 페이지 435

Table continued from the previous page...
Field
Function
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.4 TRGMUX ADC12_2 (ADC12_2)
Offset
Register
Offset
ADC12_2
8h
Function
Configures the ADC12_2 module.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2744 / 5251


---
# 페이지 436

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
0
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2745 / 5251


---
# 페이지 437

65.6.5 TRGMUX LPCMP_0 (LPCMP_0)
Offset
Register
Offset
LPCMP_0
Ch
Function
Configures the LPCMP_0 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
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
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
—
Reserved
15
—
Reserved
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2746 / 5251


---
# 페이지 438

Table continued from the previous page...
Field
Function
14-8
—
Reserved
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.6 TRGMUX LPCMP_1 (LPCMP_1)
Offset
Register
Offset
LPCMP_1
10h
Function
Configures the LPCMP_1 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
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
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2747 / 5251


---
# 페이지 439

Table continued from the previous page...
Field
Function
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
—
Reserved
15
—
Reserved
14-8
—
Reserved
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.7 TRGMUX LPCMP_2 (LPCMP_2)
Offset
Register
Offset
LPCMP_2
14h
Function
Configures the LPCMP_2 module.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2748 / 5251


---
# 페이지 440

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
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
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
—
Reserved
15
—
Reserved
14-8
—
Reserved
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2749 / 5251


---
# 페이지 441

65.6.8 TRGMUX BCTU (BCTU)
Offset
Register
Offset
BCTU
18h
Function
Configures the BCTU module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
0
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2750 / 5251


---
# 페이지 442

Table continued from the previous page...
Field
Function
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.9 TRGMUX eMIOS012_ODIS (eMIOS012_ODIS)
Offset
Register
Offset
eMIOS012_ODIS
1Ch
Function
Configures the eMIOS012_ODIS module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2751 / 5251


---
# 페이지 443

Table continued from the previous page...
Field
Function
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.10 TRGMUX eMIOS0_0 (eMIOS0_0)
Offset
Register
Offset
eMIOS0_0
20h
Function
Configures the eMIOS0_0 module.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2752 / 5251


---
# 페이지 444

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2753 / 5251


---
# 페이지 445

65.6.11 TRGMUX eMIOS0_1 (eMIOS0_1)
Offset
Register
Offset
eMIOS0_1
24h
Function
Configures the eMIOS0_1 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2754 / 5251


---
# 페이지 446

Table continued from the previous page...
Field
Function
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.12 TRGMUX eMIOS0_2 (eMIOS0_2)
Offset
Register
Offset
eMIOS0_2
28h
Function
Configures the eMIOS0_2 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2755 / 5251


---
# 페이지 447

Table continued from the previous page...
Field
Function
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.13 TRGMUX eMIOS0_3 (eMIOS0_3)
Offset
Register
Offset
eMIOS0_3
2Ch
Function
Configures the eMIOS0_3 module.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2756 / 5251


---
# 페이지 448

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
—
Reserved
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2757 / 5251


---
# 페이지 449

65.6.14 TRGMUX eMIOS1_0 (eMIOS1_0)
Offset
Register
Offset
eMIOS1_0
30h
Function
Configures the eMIOS1_0 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2758 / 5251


---
# 페이지 450

Table continued from the previous page...
Field
Function
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.15 TRGMUX eMIOS1_1 (eMIOS1_1)
Offset
Register
Offset
eMIOS1_1
34h
Function
Configures the eMIOS1_1 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2759 / 5251


---
# 페이지 451

Table continued from the previous page...
Field
Function
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.16 TRGMUX eMIOS1_2 (eMIOS1_2)
Offset
Register
Offset
eMIOS1_2
38h
Function
Configures the eMIOS1_2 module.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2760 / 5251


---
# 페이지 452

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2761 / 5251


---
# 페이지 453

65.6.17 TRGMUX eMIOS1_3 (eMIOS1_3)
Offset
Register
Offset
eMIOS1_3
3Ch
Function
Configures the eMIOS1_3 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
—
Reserved
15
—
Reserved
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2762 / 5251


---
# 페이지 454

Table continued from the previous page...
Field
Function
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.18 TRGMUX FlexIO (FlexIO)
Offset
Register
Offset
FlexIO
40h
Function
Configures the FlexIO module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2763 / 5251


---
# 페이지 455

Table continued from the previous page...
Field
Function
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.19 TRGMUX SIUL_OUT0 (SIUL_OUT0)
Offset
Register
Offset
SIUL_OUT0
44h
Function
Configures the SIUL_OUT0 module.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2764 / 5251


---
# 페이지 456

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2765 / 5251


---
# 페이지 457

65.6.20 TRGMUX SIUL_OUT1 (SIUL_OUT1)
Offset
Register
Offset
SIUL_OUT1
48h
Function
Configures the SIUL_OUT1 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2766 / 5251


---
# 페이지 458

Table continued from the previous page...
Field
Function
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.21 TRGMUX SIUL_OUT2 (SIUL_OUT2)
Offset
Register
Offset
SIUL_OUT2
4Ch
Function
Configures the SIUL_OUT2 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2767 / 5251


---
# 페이지 459

Table continued from the previous page...
Field
Function
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.22 TRGMUX SIUL_OUT3 (SIUL_OUT3)
Offset
Register
Offset
SIUL_OUT3
50h
Function
Configures the SIUL_OUT3 module.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2768 / 5251


---
# 페이지 460

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2769 / 5251


---
# 페이지 461

65.6.23 TRGMUX LPI2C_0 (LPI2C_0)
Offset
Register
Offset
LPI2C_0
54h
Function
Configures the LPI2C_0 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
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
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
—
Reserved
15
—
Reserved
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2770 / 5251


---
# 페이지 462

Table continued from the previous page...
Field
Function
14-8
—
Reserved
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.24 TRGMUX LPSPI_0 (LPSPI_0)
Offset
Register
Offset
LPSPI_0
58h
Function
Configures the LPSPI_0 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
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
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2771 / 5251


---
# 페이지 463

Table continued from the previous page...
Field
Function
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
—
Reserved
15
—
Reserved
14-8
—
Reserved
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.25 TRGMUX LPSPI_1 (LPSPI_1)
Offset
Register
Offset
LPSPI_1
5Ch
Function
Configures the LPSPI_1 module.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2772 / 5251


---
# 페이지 464

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
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
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
—
Reserved
15
—
Reserved
14-8
—
Reserved
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2773 / 5251


---
# 페이지 465

65.6.26 TRGMUX LPSPI_2 (LPSPI_2)
Offset
Register
Offset
LPSPI_2
60h
Function
Configures the LPSPI_2 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
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
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
—
Reserved
15
—
Reserved
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2774 / 5251


---
# 페이지 466

Table continued from the previous page...
Field
Function
14-8
—
Reserved
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.27 TRGMUX LPUART_0 (LPUART_0)
Offset
Register
Offset
LPUART_0
64h
Function
Configures the LPUART_0 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
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
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2775 / 5251


---
# 페이지 467

Table continued from the previous page...
Field
Function
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
—
Reserved
15
—
Reserved
14-8
—
Reserved
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.28 TRGMUX LPUART_1 (LPUART_1)
Offset
Register
Offset
LPUART_1
68h
Function
Configures the LPUART_1 module.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2776 / 5251


---
# 페이지 468

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
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
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
—
Reserved
15
—
Reserved
14-8
—
Reserved
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2777 / 5251


---
# 페이지 469

65.6.29 TRGMUX LPUART_2 (LPUART_2)
Offset
Register
Offset
LPUART_2
6Ch
Function
Configures the LPUART_2 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
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
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
—
Reserved
15
—
Reserved
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2778 / 5251


---
# 페이지 470

Table continued from the previous page...
Field
Function
14-8
—
Reserved
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.30 TRGMUX LPUART_3 (LPUART_3)
Offset
Register
Offset
LPUART_3
70h
Function
Configures the LPUART_3 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
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
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2779 / 5251


---
# 페이지 471

Table continued from the previous page...
Field
Function
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
—
Reserved
15
—
Reserved
14-8
—
Reserved
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.31 TRGMUX LCU0_SYNC (LCU0_SYNC)
Offset
Register
Offset
LCU0_SYNC
74h
Function
Configures the LCU0_SYNC module.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2780 / 5251


---
# 페이지 472

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
—
Reserved
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2781 / 5251


---
# 페이지 473

65.6.32 TRGMUX LCU0_FORCE (LCU0_FORCE)
Offset
Register
Offset
LCU0_FORCE
78h
Function
Configures the LCU0_FORCE module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
0
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2782 / 5251


---
# 페이지 474

Table continued from the previous page...
Field
Function
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.33 TRGMUX LCU0_0 (LCU0_0)
Offset
Register
Offset
LCU0_0
7Ch
Function
Configures the LCU0_0 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2783 / 5251


---
# 페이지 475

Table continued from the previous page...
Field
Function
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.34 TRGMUX LCU0_1 (LCU0_1)
Offset
Register
Offset
LCU0_1
80h
Function
Configures the LCU0_1 module.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2784 / 5251


---
# 페이지 476

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2785 / 5251


---
# 페이지 477

65.6.35 TRGMUX LCU0_2 (LCU0_2)
Offset
Register
Offset
LCU0_2
84h
Function
Configures the LCU0_2 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2786 / 5251


---
# 페이지 478

Table continued from the previous page...
Field
Function
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.36 TRGMUX LCU1_SYNC (LCU1_SYNC)
Offset
Register
Offset
LCU1_SYNC
88h
Function
Configures the LCU1_SYNC module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2787 / 5251


---
# 페이지 479

Table continued from the previous page...
Field
Function
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
—
Reserved
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.37 TRGMUX LCU1_FORCE (LCU1_FORCE)
Offset
Register
Offset
LCU1_FORCE
8Ch
Function
Configures the LCU1_FORCE module.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2788 / 5251


---
# 페이지 480

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
0
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
—
Reserved
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2789 / 5251


---
# 페이지 481

65.6.38 TRGMUX LCU1_0 (LCU1_0)
Offset
Register
Offset
LCU1_0
90h
Function
Configures the LCU1_0 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2790 / 5251


---
# 페이지 482

Table continued from the previous page...
Field
Function
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.39 TRGMUX LCU1_1 (LCU1_1)
Offset
Register
Offset
LCU1_1
94h
Function
Configures the LCU1_1 module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2791 / 5251


---
# 페이지 483

Table continued from the previous page...
Field
Function
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
65.6.40 TRGMUX LCU1_2 (LCU1_2)
Offset
Register
Offset
LCU1_2
98h
Function
Configures the LCU1_2 module.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2792 / 5251


---
# 페이지 484

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2793 / 5251


---
# 페이지 485

65.6.41 TRGMUX CM7_RXEV (CM7_RXEV)
Offset
Register
Offset
CM7_RXEV
9Ch
Function
Configures the CM7_RXEV module.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
LK 
SEL3 
0
SEL2 
W
Reset
0
0
0
0
0
0
0
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
SEL1 
0
SEL0 
W
Reset
0
0
0
0
0
0
0
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
LK
TRGMUX Register Lock
Disables writing to the register. You can write to this field once after system reset. When this field is 1, you 
cannot write to SELx until the next system reset. This field becomes 0 after system reset.
0b - Register is writable
1b - Register is not writable until the next system reset
30-24
SEL3
TRGMUX Source Select 3
Specifies the source select for output 3. See Table 429 for field values.
23
—
Reserved
22-16
SEL2
TRGMUX Source Select 2
Specifies the source select for output 2. See Table 429 for field values.
15
—
Reserved
Table continues on the next page...
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2794 / 5251


---
# 페이지 486

Table continued from the previous page...
Field
Function
14-8
SEL1
TRGMUX Source Select 1
Specifies the source select for output 1. See Table 429 for field values.
7
—
Reserved
6-0
SEL0
TRGMUX Source Select 0
Specifies the source select for output 0. See Table 429 for field values.
NXP Semiconductors
Trigger MUX (TRGMUX)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2795 / 5251


---