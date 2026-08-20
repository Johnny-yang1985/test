# 페이지 358

Chapter 56
Clock Monitoring Unit – Frequency Check (CMU_FC)
56.1 Chip-specific CMU_FC information
56.1.1 CMU_FC configuration
The device consists of a robust clock monitoring architecture targeted to monitor various clock nodes to ensure device clock 
robustness. There are upto seven clock monitoring units present in the device out of which five are of type CMU_FC. See 'Clock 
monitoring' section in Clocking chapter for details on device clock monitoring architecture. Register interface clock is referred as 
'bus_clock' in the below sections. See Clocking chapter for details.
 
CMU_5 is accessible by Cortex-M0+ core only.
  NOTE  
CMU_FC combined spec variation: The combined spec variation for CMU (used for configuring CMU_FCx.HTCR[HFREF] and 
CMU_FCx.HTCR[LFREF]) is the absolute sum of frequency variations of the clock sources. Refer device datasheet for frequency 
variations for the corresponding clock sources.
56.2 Overview
CMU_FC ensures the clock integrity of selected clocks and allows continuous clock integrity verification.
CMU_FC checks if the frequency of a monitored clock (monitored_clock) is within a programmable frequency range specified 
by the user. If the frequency is outside the specified limits, it could lead to performance, protocol, and timing failures. CMU_FC 
requires a clock used as a base reference for the frequency check operation. This reference clock (reference_clock) must be within 
documented limits for correct CMU_FC operation.
56.2.1 Block diagram
CMU_FC counts clock cycles of the monitored clock during a user programmable time duration of n clock cycles of the reference 
clock. There is a comparison between the final count of the monitored clock and the user programmable upper and lower threshold 
count limits. The control logic determines whether the cycle count is within the programmed limits. If not it sets the Frequency 
Higher than High frequency reference threshold event status (FHH) field or the Frequency Lower than Low frequency reference 
threshold event status (FLL) field in the Status Register (SR). If you enable interrupts, an interrupt asserts when the status 
flag sets.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2275 / 5251


---
# 페이지 359

=
reference_clock
Enable
Reference counter
Checking window
Control logic
Monitor counter
High threshold
monitored_clock
Low threshold
SR[FHH]
SR[FLL]
<
>
Figure 228. CMU_FC block diagram
CMU_FC cannot detect the following:
• Monitored clock duty cycle variations
• Instantaneous monitored clock frequency variations that do not cross upper or lower threshold limits
56.2.2 Features
The CMU_FC features are:
• Programmable duration of reference clock cycles
• Initiates an event if a monitored clock frequency is higher than high frequency reference (FHH)
• Initiates an event if a monitored clock frequency is lower than low frequency reference (FLL)
• FLL event (if enabled) is generated when monitored clock is very slow or stops functioning
• Masking of FHH event interrupt
• Masking of FLL event interrupt
56.3 Functional description
56.3.1 Operating modes
CMU_FC supports the following operating modes:
• Frequency checking
See the succeeding sections for detailed descriptions of the functions.
56.3.2 Frequency checking
Frequency checking starts when software writes GCR[FCE] = 1. The Run Status field SR[RS] shows 1 after frequency check 
operation starts.
NXP Semiconductors
Clock Monitoring Unit – Frequency Check (CMU_FC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2276 / 5251


---
# 페이지 360

CMU_FC performs continuous periodic clock checking of the monitored clock. Each checking window involves the 
following operations:
• Stage 1 – Reference clock counter runs for RCCR[REF_CNT] reference clock cycles. Monitored clock counter runs in parallel 
for the same time duration as reference clock counter.
• Stage 2 – After stage 1, the module compares the final monitored clock count against the programmed thresholds.
If the monitored clock count is greater than the high threshold value in HTCR[HFREF], an FHH event occurs.
If the monitored clock count is lower than the low threshold value in LTCR[LFREF], an FLL event occurs.
Monitored clock count (Typ)
High Frequency ReferenceThreshold (HFREF)
Low Frequency ReferenceThreshold (LFREF)
Clock count
0
FHH event generation
FLL event generation
Healthy clock zone
Figure 229. Frequency checking HFREF and LFREF thresholds
56.3.2.1
Monitored clock lost
If a monitored clock ceases operation before evaluation of that clock (Stage 2, see Frequency checking), CMU_FC waits for 
RCCR[REF_CNT] reference clock periods by extending Stage 2 before triggering an FLL event.
• If monitored_clock is not running when enabling CMU_FC:
Worst case FLL response time = (2 × RCCR[REF_CNT] + 12) reference_clock 
cycles + 15 bus_clock cycles
• If monitored_clock stops when the CMU_FC is running:
Worst case FLL response time = (2 × RCCR[REF_CNT] + 2) reference_clock 
cycles + 3 bus_clock cycles
NXP Semiconductors
Clock Monitoring Unit – Frequency Check (CMU_FC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2277 / 5251


---
# 페이지 361

56.3.3 Clocking
This module has the following clock sources.
Table 325. Clock description
Clock
I/O
Description
reference_clock
I
Clock signal that the module uses as a 
reference to evaluate monitored_clock
monitored_clock
I
Clock signal on which frequency check 
is performed
bus_clock
I
Clock signal on which register read/write 
operation is performed
 
See the Clocking chapter for details of monitored and reference clocks used on this chip.
  NOTE  
56.3.4 Reset
This module has the following reset sources.
• Global hard reset input
• Reset port synchronized to reference clock domain input
• Reset port synchronized to monitored clock domain input
56.4 External signals
This module has no external signals.
56.5 Programming guidelines
56.5.1 Programming RCCR[REF_CNT]
RCCR[REF_CNT] defines the duration of the checking operation in number of reference_clock cycles. The minimum 
RCCR[REF_CNT] value can be calculated using the following formula:
, 8 + 5 X 
CEILING value of MAX
Minimum RCCR [REF_CNT] = 
X
3
reference_clock
reference_clock
monitored_clock
bus_clock
...where:
• freference_clock is the frequency of the reference clock
• fbus_clock is the frequency of the bus clock
• fmonitored_clock is the frequency of the monitored clock
Example to determine RCCR[REF_CNT]:
• fbus_clock = 16 MHz
• freference_clock = 8 MHz
• fmonitored_clock = 48 MHz
NXP Semiconductors
Clock Monitoring Unit – Frequency Check (CMU_FC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2278 / 5251


---
# 페이지 362

Formula #1:
reference_clock
bus_clock
X
3
Inserting the values:
3 × (8 / 16) = 1.5
Formula #2:
8 + 5 X 
reference_clock
monitored_clock
Inserting the values:
8 + 5 × (8 / 48) ≈ 8.83
MAX (1.5, 8.83):
8.83
CEILING value of MAX:
9
Therefore, minimum RCCR[REF_CNT]:
9
Programmed RCCR[REF_CNT] value must be greater than or equal to the calculated minimum value and should be decided after 
considering application requirements of frequency check completion response time and overall accuracy required from CMU_FC.
• Higher values of RCCR[REF_CNT] results in longer measurement window, leading to better accuracy in monitored clock 
check.
• Lower values of RCCR[REF_CNT] results in shorter measurement window, leading to faster FHH and FLL event 
response, but higher inaccuracy in reported result.
For measurement window calculation, see step 8 in Programming HFREF and LFREF
56.5.2 Programming HFREF and LFREF
You must consider the following when programming HFREF/LFREF:
• Tolerable monitored clock frequency variation
• Maximum reference clock frequency variation
• Inherent module inaccuracy
CMU_FC has an expected maximum deviation of ± 3 monitored_clock cycles (CMU_FCVAR+ = 3, CMU_FCVAR- = –3).
The following procedure shows how to calculate optimum values for HTCR[HFREF] and LTCR[LFREF] (numbers shown are from 
example in table):
1. Determine the ideal monitored_clock frequency (fmonitored_clock (ideal), 48 MHz).
2. Determine the specified variation of the monitored_clock (1.1%).
3. Calculate monitored_clock frequency variation: .
X
step 2
monitored_clock
• fmonitored_clock (max) = 48 MHz × (1 + (1.1 ÷ 100)) = 48.53 MHz
• fmonitored_clock (min)= 48 MHz × (1 – (1.1 ÷ 100)) = 47.47 MHz
4. Determine the ideal reference_clock frequency (freference_clock (ideal), 8 MHz).
5. Determine the specified variation of the reference_clock (3.3%).
NXP Semiconductors
Clock Monitoring Unit – Frequency Check (CMU_FC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2279 / 5251


---
# 페이지 363

6. Calculate ideal reference_clock frequency variation:
X
step 5
reference_clock
• freference_clock (max) = 8 MHz × (1 + (3.3 ÷ 100)) = 8.26 MHz
• freference_clock (min) = 8 MHz × (1 – (3.3 ÷ 100)) = 7.74 MHz
7. Select the value of RCCR[REF_CNT] needed (80). See Programming RCCR[REF_CNT].
8. Calculate ideal measurement window:
_
reference_clock
• 80 ÷ 8 MHz = 10000 ns
9. Calculate ideal monitored_clock count:
_
reference_clock
monitored_clock
• 80 ÷ 8 MHz × 48 MHz = 480.00 (round off this value, 480 in this case)
10. Calculate high threshold value (HTCR[HFREF]):
_
+
_
reference_clock
monitored_clock
Ceiling value of 
• HTCR[HFREF] = Ceiling(48.53 MHz ÷ 7.74 MHz × 80 + 3) = 505
11. Calculate low threshold value (LTCR[LFREF]):
_
-
_
reference_clock
monitored_clock
Floor value of 
-
• LTCR[LFREF] = Floor(47.47 MHz ÷ 8.26 MHz × 80 – 3) = 456
Table 326. HTCR[HFREF] and LTCR[LFREF] calculation example
Property
Value
Unit
Bus clock frequency (fbus_clock)
16
MHz
Monitored clock frequency (fmonitored_clock (ideal))
48
MHz
Specified variation of monitored clock
1.1
%
Monitored clock frequency (maximum after specified variation, 
fmonitored_clock (max))
48.53
MHz
Table continues on the next page...
NXP Semiconductors
Clock Monitoring Unit – Frequency Check (CMU_FC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2280 / 5251


---
# 페이지 364

Table 326. HTCR[HFREF] and LTCR[LFREF] calculation example (continued)
Property
Value
Unit
Monitored clock frequency (minimum after specified variation, 
fmonitored_clock (min))
47.47
MHz
Reference clock frequency (freference_clock (ideal))
8
MHz
Specified variation of reference clock
3.3
%
Reference clock frequency (maximum after specified variation, 
freference_clock (max))
8.26
MHz
Reference clock frequency (minimum after specified variation, 
freference_clock (min))
7.74
MHz
Minimum reference count (RCCR[REF_CNT])
9
—
Programmed reference count (RCCR[REF_CNT])
(must be ≥ minimum RCCR[REF_CNT])
80
—
Measurement window
10000.00
ns
Calculated monitored clock count
480.00
—
Calculated monitored clock Count (rounded)
480
—
Module positive variation (CMU_FCVAR+)
3
—
Module negative variation (CMU_FCVAR-)
-3
—
Programmed higher threshold (HTCR[HFREF])
505
—
Programmed lower threshold (LTCR[LFREF])
456
—
56.5.3 Module programming sequence
56.5.3.1
Module programming sequence
The recommended programming sequence for CMU_FC frequency checking is:
1. In any order, complete the following:
• Program RCCR[REF_CNT] to define the frequency measuring window duration in reference_clock cycles.
• Program LTCR[LFREF] and HTCR[HFREF] to set the permissible frequency range of the monitored_clock.
• Program IER to enable interrupt.
2. Write GCR[FCE] = 1 to start the frequency check operation.
 
When GCR[FCE] = 1, you must not write to RCCR, HTCR, LTCR, or IER. Attempting to do so generates a bus 
transfer error.
  NOTE  
3. To reconfigure RCCR, LTCR, HTCR , and IER or to stop frequency check operation, wait for SR[RS] = 1, then write 
GCR[FCE] = 0.
56.6 CMU_FC register descriptions
NXP Semiconductors
Clock Monitoring Unit – Frequency Check (CMU_FC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2281 / 5251


---
# 페이지 365

56.6.1 CMU_FC memory map
This section describes the address order of all the CMU_FC registers. Each description includes a standard register diagram and 
associated field descriptions.
CMU_0 base address: 402B_C000h
CMU_3 base address: 402B_C060h
CMU_4 base address: 402B_C080h
CMU_5 base address: 402B_C0A0h
CMU_6 base address: 402B_C0C0h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Global Configuration Register (GCR)
32
RW
0000_0000h
4h
Reference Count Configuration Register (RCCR)
32
RW
0000_0000h
8h
High Threshold Configuration Register (HTCR)
32
RW
00FF_FFFFh
Ch
Low Threshold Configuration Register (LTCR)
32
RW
0000_0000h
10h
Status Register (SR)
32
RW
0000_0000h
14h
Interrupt Enable Register (IER)
32
RW
0000_0000h
56.6.2 Global Configuration Register (GCR)
Offset
Register
Offset
GCR
0h
Function
Controls module level configurations such as enabling frequency check.
Diagram
Bits
31
30
29
28
27
26
25
24
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
FCE 
W
Reset
0
0
0
0
0
0
0
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
Clock Monitoring Unit – Frequency Check (CMU_FC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2282 / 5251


---
# 페이지 366

Fields
Field
Function
31-1
—
Reserved
0
FCE
Frequency Check Enable
Starts or stops frequency checking. FCE is disabled by default. Software can enable FCE at any time. To 
stop the ongoing operation, write 0 to FCE only when SR[RS] = 1.
0b - Stops frequency checking
1b - Starts frequency checking
56.6.3 Reference Count Configuration Register (RCCR)
Offset
Register
Offset
RCCR
4h
Function
Programs reference count duration of the frequency check window.
 
Write to RCCR only when GCR[FCE] = 0. A bus transfer error results if software writes RCCR when GCR[FCE] = 1.
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
REF_CNT 
W
Reset
0
0
0
0
0
0
0
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
Table continues on the next page...
NXP Semiconductors
Clock Monitoring Unit – Frequency Check (CMU_FC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2283 / 5251


---
# 페이지 367

Table continued from the previous page...
Field
Function
15-0
REF_CNT
Reference clock count
Total number of counts of reference_clock for which frequency check runs. This field defines the duration 
of one frequency check window. See Programming RCCR[REF_CNT] for RCCR calculation.
56.6.4 High Threshold Configuration Register (HTCR)
Offset
Register
Offset
HTCR
8h
Function
Determines the high threshold limit of the monitored clock counter.
 
Write HTCR only when GCR[FCE] = 0. A bus transfer error results if software writes HTCR when GCR[FCE] = 1.
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
HFREF 
W
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
HFREF 
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
31-24
—
Reserved
23-0
HFREF
High frequency reference threshold
HFREF determines the high reference value for the monitored clock frequency.
See Programming HFREF and LFREF for HFREF calculation.
Table continues on the next page...
NXP Semiconductors
Clock Monitoring Unit – Frequency Check (CMU_FC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2284 / 5251


---
# 페이지 368

Table continued from the previous page...
Field
Function
 
Do not program HFREF to a value greater than 0x00FFFFFC.
  NOTE  
56.6.5 Low Threshold Configuration Register (LTCR)
Offset
Register
Offset
LTCR
Ch
Function
Determines the low threshold limit of the monitored clock counter.
 
Write LTCR only when GCR[FCE] = 0. A bus transfer error results if software writes LTCR when GCR[FCE] = 1.
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
LFREF 
W
Reset
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
LFREF 
W
Reset
0
0
0
0
0
0
0
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
LFREF
Low Frequency Reference Threshold
LFREF determines the low reference value for the monitored clock frequency.
See Programming HFREF and LFREF for LFREF calculation.
 
Do not program LFREF to a value less than 0x00000003.
  NOTE  
NXP Semiconductors
Clock Monitoring Unit – Frequency Check (CMU_FC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2285 / 5251


---
# 페이지 369

56.6.6 Status Register (SR)
Offset
Register
Offset
SR
10h
Function
Provides the internal status of the module.
Diagram
Bits
31
30
29
28
27
26
25
24
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
RS 
Reserved 
FHH 
FLL 
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
31-5
—
Reserved
4
RS
Run Status
Shows the running status of module internal operation. After enabling the frequency check operation 
(GCR[FCE] = 1), there is a fixed delay before this field shows running status. If the system wants 
to disable the frequency check operation, then the software should read this register and write 
GCR[FCE] = 0 only when this field is 1.
0b - Frequency check stopped
1b - Frequency check running
3-2
—
Reserved
1
FHH
Frequency higher than high frequency reference threshold event status
Hardware writes 1 to FHH when the monitored clock frequency becomes higher than the high threshold 
value in HTCR[HFREF]. FHH clears when software writes 1.
Table continues on the next page...
NXP Semiconductors
Clock Monitoring Unit – Frequency Check (CMU_FC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2286 / 5251


---
# 페이지 370

Table continued from the previous page...
Field
Function
0b - No FHH event
1b - FHH event occurred
0
FLL
Frequency lower than low frequency reference threshold event status
Hardware writes 1 to FLL when the monitored clock frequency becomes lower than the low threshold 
value in LTCR[LFREF]. FLL clears when software writes 1.
0b - No FLL event
1b - FLL event occurred
56.6.7 Interrupt Enable Register (IER)
Offset
Register
Offset
IER
14h
Function
Enables CMU_FC interrupts.
 
Write IER only when GCR[FCE] = 0. A bus transfer error results if software writes IER when GCR[FCE] = 1.
  NOTE  
Enable only either asynchronous FHH event interrupt or synchronous FHH event interrupt at a time.
For example:
• If IER[FHHIE] is set to 1 then set IER[FHHAIE] to 0.
• If IER[FHHAIE] is set to 1 then set IER[FHHIE] to 0.
Enable only either asynchronous FLL event interrupt or synchronous FLL event interrupt at a time.
For example:
• If IER[FLLIE] is set to 1 then set IER[FLLAIE] to 0.
• If IER[FLLAIE] is set to 1 then set IER[FLLIE] to 0.
See Clocking chapter for interrupt usage information based on CMU_FC instances.
NXP Semiconductors
Clock Monitoring Unit – Frequency Check (CMU_FC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2287 / 5251


---
# 페이지 371

Diagram
Bits
31
30
29
28
27
26
25
24
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
W
Reset
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
0
Bits
15
14
13
12
11
10
9
8
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
FHHAI
E 
FLLAI
E 
FHHIE 
FLLIE 
W
Reset
0
0
0
0
0
0
0
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
23
—
Reserved
22
—
Reserved
21-20
—
Reserved
19-18
—
Reserved
17-16
—
Reserved
15-4
—
Reserved
3
FHHAIE
Frequency Higher than High Frequency Reference Threshold Asynchronous Interrupt Enable
FHHAIE enables FHH asynchronous interrupt at the module boundary.
0b - Asynchronous FHH event interrupt disabled
1b - Asynchronous FHH event interrupt enabled
2
FLLAIE
Frequency Lower than Low Frequency Reference Threshold Asynchronous Interrupt Enable
FLLAIE enables FLL asynchronous interrupt at the module boundary.
Table continues on the next page...
NXP Semiconductors
Clock Monitoring Unit – Frequency Check (CMU_FC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2288 / 5251


---
# 페이지 372

Table continued from the previous page...
Field
Function
0b - Asynchronous FLL event interrupt disabled
1b - Asynchronous FLL event interrupt enabled
1
FHHIE
Frequency Higher than High Frequency Reference Threshold Synchronous Interrupt Enable
FHHIE enables an FHH synchronous interrupt at the module boundary.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
CMU_0
IER
—
CMU_3
—
IER
CMU_4
—
IER
CMU_5
—
IER
CMU_6
—
IER
0b - Synchronous FHH event interrupt disabled
1b - Synchronous FHH event interrupt enabled
0
FLLIE
Frequency Lower than Low Frequency Reference Threshold Synchronous Interrupt Enable
FLLIE enables an FLL synchronous interrupt at the module boundary.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
CMU_0
IER
—
CMU_3
—
IER
CMU_4
—
IER
CMU_5
—
IER
CMU_6
—
IER
Table continues on the next page...
NXP Semiconductors
Clock Monitoring Unit – Frequency Check (CMU_FC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2289 / 5251


---
# 페이지 373

Table continued from the previous page...
Field
Function
0b - Synchronous FLL event interrupt disabled
1b - Synchronous FLL event interrupt enabled
56.7 Glossary
FHH
The state that the monitored clock frequency is higher than the high frequency reference. FHH is also the name 
of the register field that indicates this state.
FHH event The event that the module triggers when it detects FHH.
FLL
The state that the monitored clock frequency is lower than the lower frequency reference. FLL is also the name 
of the register field that indicates this state.
FLL event
The event that the module triggers when it detects FLL.
NXP Semiconductors
Clock Monitoring Unit – Frequency Check (CMU_FC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2290 / 5251


---