# 페이지 1

Chapter 85
Temperature Sensor (TempSense)
85.1 Overview
TEMPSENSE is used to measure the temperature on the chip through an ADC and to flag if an overtemperature condition occurs.
The TEMPSENSE module contains control registers for use with the Engineering temperature sensor (ETS) hard block and the 
flag generation hard block. These registers use a peripheral bus interface to communicate with the chip.
85.1.1 Block diagram
The functional structure of the TEMPSENSE can be seen in the block diagram in Figure 578.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5223 / 5251


---
# 페이지 2

ETS_EN
GNDSEL
To ADC
ETSCTL
ETS_EN
GNDSEL
Vdd
&
&
Figure 578. TEMPSENSE block diagram
85.1.2 Features
The TEMPSENSE includes the following features:
• Provide a voltage proportional to the temperature which will be read out by ADC
• Ground selection for improved precision in the ETS. The ETS ground could be different from the ADC ground. By 
exposing it to the ADC, the temperature calculation could be improved as the voltage value will be more precise.
NXP Semiconductors
Temperature Sensor (TempSense)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5224 / 5251


---
# 페이지 3

85.2 Functional description
85.2.1 Clocking
This module has no clocking considerations.
85.2.2 Interrupts
This module has no interrupts.
85.2.3 General
The TEMPSENSE module is designed to measure the temperature on the chip.
The TEMPSENSE output can be read by an ADC on demand so that the software can determine the current die temperature. The 
software should enable the TEMPSENSE by setting ETSCTL[ETS_EN].
The TEMPSENSE output can be read by an ADC on demand so that the software can determine the current die temperature..
Coefficients are used to allow a simple and accurate calculation of linearized temperature directly from the ADC. The increase of 
the sampling time of the ADC from the minimum sampling value is increasing the temperature accuracy.
85.2.4 Initialization
85.2.4.1
Conversion from voltage to temperature
Solve the equation for the conversion from voltage to temperature, where VETS is the difference of Vbe and VGND. VGND is expose 
on the ADC output when ETSCTL[GNDSEL] is set.
The coefficients TCA0, TCA1 and TCA2 are read from the corresponding registers. They are stored in a signed fixed-point format 
as the following TCAx(11,4) (1 bit for the sign, 11 bits for the integer part and 4 bits for the decimal part).
The calculation of the temperature should be done with the actual coefficient values provided in the TCAx fields. See the example 
below for an ambient temperature of 25C, and an ADC reference voltage (VREFH) of 5V. See the ADC section of the device data 
sheet for more details on VREFH and N-bit level resolution.
N
VREFH
By using the formula, the junction temperature calculated is 26.5838 C.
The maximal calculation error is 0.0313 C.
85.3 External signals
There are no external signals for this module.
NXP Semiconductors
Temperature Sensor (TempSense)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5225 / 5251


---
# 페이지 4

85.4 Memory map and register definition
85.4.1 Transfer error description
The following actions will cause a transfer error and will not change the register content:
• Any access to an unused register address
• Write access to a read-only register (TCAx)
85.4.2 TEMPSENSE register descriptions
85.4.2.1
TEMPSENSE memory map
TEMPSENSE base address: 4037_C000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
ETS Control (ETSCTL)
32
RW
0000_0000h
8h
Temperature Coefficient (TCA0)
32
R
See section
Ch
Temperature Coefficient (TCA1)
32
R
See section
10h
Temperature Coefficient (TCA2)
32
R
See section
85.4.2.2
ETS Control (ETSCTL)
Offset
Register
Offset
ETSCTL
0h
Function
This register contains control bits that control ETS.
Diagram
Bits
31
30
29
28
27
26
25
24
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
GNDS
EL 
ETS_
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
Temperature Sensor (TempSense)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5226 / 5251


---
# 페이지 5

Fields
Field
Function
31-2
—
Reserved
1
GNDSEL
Ground selection
0b - No exposure of the ground
1b - Expose ground on the ADC output if ETSCTL[ETS_EN]=1
0
ETS_EN
Temperature Sensor enable
Power up the ETS.
0b - Power down
1b - Functional mode
85.4.2.3
Temperature Coefficient (TCA0)
Offset
Register
Offset
TCA0
8h
Function
This register contains the coefficient TCA0 needed to calculate the temperature. the reset value is specific for each chip.
Diagram
Bits
31
30
29
28
27
26
25
24
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
u
u
u
u
u
u
u
u
u
u
u
u
u
u
u
u
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
TCA0 
W
Reset
u
u
u
u
u
u
u
u
u
u
u
u
u
u
u
u
Fields
Field
Function
31-16
Reserved
Table continues on the next page...
NXP Semiconductors
Temperature Sensor (TempSense)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5227 / 5251


---
# 페이지 6

Table continued from the previous page...
Field
Function
—
15-0
TCA0
Temperature coefficient A0
see Conversion from voltage to temperature for the usage of this coefficient
85.4.2.4
Temperature Coefficient (TCA1)
Offset
Register
Offset
TCA1
Ch
Function
This register contains the coefficient TCA1 needed to calculate the temperature. the reset value is specific for each chip.
Diagram
Bits
31
30
29
28
27
26
25
24
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
u
u
u
u
u
u
u
u
u
u
u
u
u
u
u
u
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
TCA1 
W
Reset
u
u
u
u
u
u
u
u
u
u
u
u
u
u
u
u
Fields
Field
Function
31-16
—
Reserved
15-0
TCA1
Temperature coefficient A1
see Conversion from voltage to temperature for the usage of this coefficient
NXP Semiconductors
Temperature Sensor (TempSense)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5228 / 5251


---
# 페이지 7

85.4.2.5
Temperature Coefficient (TCA2)
Offset
Register
Offset
TCA2
10h
Function
This register contains the coefficient TCA2 needed to calculate the temperature. the reset value is specific for each chip.
Diagram
Bits
31
30
29
28
27
26
25
24
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
u
u
u
u
u
u
u
u
u
u
u
u
u
u
u
u
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
TCA2 
W
Reset
u
u
u
u
u
u
u
u
u
u
u
u
u
u
u
u
Fields
Field
Function
31-16
—
Reserved
15-0
TCA2
Temperature coefficient A2
see Conversion from voltage to temperature for the usage of this coefficient
85.5 Glossary
ADC
Analog to digital converter
ETS
Engineering temperature sensor
CTS
Customer temperature sensor
Vbe
Base emitter voltage
VETS
Engineering temperature sensor voltage
VGND
Ground voltage
NXP Semiconductors
Temperature Sensor (TempSense)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5229 / 5251


---
# 페이지 8

Appendix A
General Changes
A.1 General changes
Added S32K389 information.
In chapter CAN (FlexCAN) removed the following registers and bit fields:
• ET (External Timer) register
• FLTCONF_IE (Fault Confinement Interrupt Enable) register
• MCR[TPOE] and MCR[TPOV] bit fields
• CTRL1[ROM] bit field
• ESR1[ATP] and ESR1[PTA] bit fields
• CTRL2[RETRY] and CTRL2[FLT_RXN] bit fields
• ESR2[RX_PIN_ST] bit field
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5230 / 5251


---
