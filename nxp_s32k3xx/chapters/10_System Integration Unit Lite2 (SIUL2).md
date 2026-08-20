# 페이지 252

Chapter 10
System Integration Unit Lite2 (SIUL2)
10.1 Chip-specific SIUL2 information
10.1.1 Feature availability
This chip:
• Supports input filter enable (MSCR5[IFE]) only for the reset pad (PTA5). For details, see the "Pad signal description" table in 
the "Signal Multiplexing" chapter.
• Does not implement the open-drain feature. LPI2C directly configures only the pads related to the I2C and LPUART 
functions in pseudo open-drain when these functions are muxed to the pads. See the LPI2C and LPUART chapters for 
more information.
• Reserves GPDO[25:24] and PGPDO1[7:6] because PTA24 and PTA25 are input-only pins.
 
• EIRQ[0-15] can be used either for interrupt or DMA request. EIRQ[16-31] can only be used for 
interrupt request.
• When a pad is used with IBE=1, the PAD must be actively driven. Otherwise, IO states are not deterministic.
  NOTE  
10.1.2 Mapping of MSCR and IMCR instances
• CR numbers 0-511 correspond to the MSCR instances.
• CR numbers 512-1023 correspond to the IMCR instances. IMCRs defined in the attached IOMUX file have an offset of 
512 with respect to the IMCR number defined in SIUL2 memory map section.
 
IMCR register only supports 32 bit access, any other access might result in unexpected data. See IOMUX file 
attached to this document for the reset value and exact number of IMCR and MSCR register instances.
  NOTE  
 
SIUL2 registers description in the "memory map" section is generic. The valid fields for MSCR0- MSCR323 must 
be checked from the IOMUX file attached to this document.
  NOTE  
10.2 Overview
SIUL2 provides control over all electrical pin controls and ports with 16 bits of bidirectional, general-purpose input and output (I/O) 
signals. It also performs the following functions:
• Enables you to select the functions and electrical characteristics that appear on external chip pins
• Controls the multiplexing of internal signals from one module to another and controls the chip I/O
• Supports a maximum of 32 external interrupts with trigger event configuration
10.2.1 Block diagram
SIUL2 provides a dedicated pad control to general-purpose pads that you can configure as either inputs or outputs. It provides 
registers for you to read values from GPIO pads configured as inputs and to write values to GPIO pads configured as outputs. 
Based on the configuration of GPIO, you can:
• Write to an internal register to control the state driven on the associated output pad (when configured as output).
• Detect the state of the associated pad by reading the value from an internal register (when configured as input).
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
303 / 5251


---
# 페이지 253

• Read back the pad value to check whether the written value appears on the pad (when configured as input and output).
Access the GPIO data registers in the following ways to allow port access and bit manipulation without read-modify-
write operations:
• Access to two 16-bit ports in one access
• Read/write access to a single bit
• 16-bit port write with a bit mask using a single 32-bit access
You can configure:
• External interrupt sources at the chip level to be used with any chip pad.
• Interrupt sources to have a digital filter to reject short glitches on the inputs.
The external interrupt or DMA requests map to the interrupt request pins (REQ) in the chip packages. The user-defined registers 
(UDRs) contain miscellaneous control and status bits.
MSCR and IMCR registers
Pad control and pin muxing
SIUL2
IPS master
IOMUX
Registers
IPS
bus
Chip-specific UDR registers
Miscellaneous logic
Interrupt controller
- Interrupt configuration
- Glitch filter
Interrupts and DMA requests
Pads
IP modules
DMA
Data registers
GPIO
Figure 23. Block diagram
10.2.2 Features
SIUL2 supports the following:
• 1 to 32 GPIO ports with data control:
— Drives data to as many as 16 independent I/O channels
— Samples data from as many as 16 independent I/O channels
• Read or write of two 16-bit registers with one access for a 32-bit port
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
304 / 5251


---
# 페이지 254

• External interrupt and DMA requests:
— 1 to 32 programmable digital glitch filters, one for each interrupt REQ pin
— Edge detection
• Multiplexed Signal Configuration Registers (MSCR) to configure the electrical parameters and settings for as many as 512 
functional pads.
See the interrupt map file and the DMAMUX map file attached to this document for mapping of interrupt and DMA sources to 
interrupt vectors and DMA channels.
10.3 Functional description
10.3.1 Pad control
SIUL2 controls the electrical characteristics of around 512 pads. It provides a consistent interface for all pads, both on a by-port 
and a by-bit basis.
The setting of each pad out of reset is fixed per chip but you can configure it individually. This way you can select special pull 
settings or peripheral pad ownership.
You can configure each pad independently of all other pads on the chip or other pads grouped within a single port, therefore 
allowing grouping of different pad types together in ports and operating the pads individually. Grouping the various functions for 
each pad into a single register allows configuration of each pad with a single write to a register, which further allows you to duplicate 
software for similar pads with index changes.
10.3.2 General-purpose input and output pads (GPIO)
SIUL2 allows each pad to be configured as either of the following:
• General-purpose input or output pad (GPIO)
• A pad for one or more alternate functions (input or output) determined by the peripheral that uses the pad
You can also implement the GPIO pads without any alternate function.
SIUL2 manages as many as 512 GPIO pads organized as ports that can be accessed for data reads and writes as 8-bit, 16-bit, 
or 32-bit.
All port accesses are identical, with each read or write performed only at a different location to access a different port width.
32-bit port
Base
0
7
15
23
31
Base+2h
8-bit port
Base
0
7
8-bit port
Base+1h
0
7
8-bit port
Base+2h
0
7
8-bit port
Base+3h
0
7
16-bit port
0
7
15
Base
16-bit port
0
7
15
Figure 24. Data port example arrangement showing configuration for different port width accesses
SIUL2 has separate data input and data output registers for all pads. You can therefore directly read back an input or output value 
of a pad to validate what is present on the pad instead of confirming the value that was written to the data input registers. The data 
output registers support both read and write operations whereas the data input registers support only the read access.
When you configure a pad for using one of its alternate functions, the data input values reflect the respective value of the pad. If 
you perform a write operation to the data output register for a pad configured as an alternate function (non-GPIO), this write is not 
reflected by the pad value until reconfigured to GPIO. All general-purpose pads are implemented as bidirectional.
If a bidirectional operation impacts the performance or is not needed for a pad function, you can limit the functionality of the pad 
to input-only.
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
305 / 5251


---
# 페이지 255

10.3.3 Clocking
This module has no clocking considerations.
10.3.4 External interrupts
SIUL2 supports 1–32 external interrupts allocated to pads by the chip.
See the interrupt map file and the DMAMUX map file attached to this document (device reference manual) for mapping of interrupt 
and DMA sources to interrupt vectors and DMA channels.
SIUL2 supports 1–4 interrupt vectors to the interrupt controller of the chip. Each interrupt vector can support as many as eight 
external interrupt sources from the chip pads.
All the external interrupt pads within a single group have equal priority. It is your responsibility to search for the application through 
a group of sources in an appropriate way.
 
Glitch filters applied to external interrupts require a running internal oscillator clock. If such a clock is not available, 
enabling the glitch filter on an external interrupt disables the interrupt.
  NOTE  
The external interrupt signals from a pad have internal synchronizers. Therefore, the width of the interrupt signals should be at 
least 2.5 or 3 times the internal RC oscillator (IRC) clock cycles to correctly capture the interrupts.
10.3.4.1
External interrupt initialization
Perform the following procedure to enable external interrupts (if you do not perform these steps, you may get a false interrupt flag 
during interrupt initialization):
1. Write 1 to the appropriate IFER[IFEn] fields to enable the glitch filter.
2. Write 0 to DIRER0[EIREn] to mask interrupts.
3. Write 1 to the appropriate IREEn fields in Interrupt Rising-Edge Event Enable 0 (IREER0) and IFEEn fields in Interrupt 
Falling-Edge Event Enable 0 (IFEER0) as needed to select the pin polarity.
4. Configure the appropriate fields in MSCR for the external interrupt pins:
a. Write 0 to the OBE and ODE to disable the output.
b. Write 1 to IBE field to enable the input buffer of the pin.
c. If you are using the internal pull-up or pull-down resistors, configure the appropriate PUE and PUS fields.
 
If you select external interrupt inputs for external interrupt pins, do not configure them as outputs (that is, 
MSCR[OBE] must not be 0) because it can cause false interrupt detection (such as from a GPIO configuration).
  NOTE  
5. Write to the appropriate DIRSR0[DIRSn] fields to select a request between DMA or interrupt.
6. Select the desired glitch filter setup for the pins:
a. Write an appropriate value to IFMCR0[MAXCNT] for the respective external interrupt to the filter counter.
b. Write an appropriate value to IFCPR[IFCP] to set the filter clock prescaler.
c. Write to the appropriate IFER0[IFEn] fields to enable the glitch filter for the external interrupt pins.
7. Set the appropriate DISR0[EIFn] to clear any flags.
8. Write to the appropriate DIRER0[EIREn] fields to enable the interrupt pins.
 
If you do not follow these steps you may get a false interrupt flag during interrupt initialization.
  NOTE  
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
306 / 5251


---
# 페이지 256

10.3.4.2
External interrupt management
You can enable or disable each interrupt independently using a single rolled up register, DIRER0.
You can configure a pad defined as an external interrupt to recognize interrupts with an active rising edge, an active falling edge, 
or both, using Interrupt Rising-Edge Event Enable 0 (IREER0) and Interrupt Falling-Edge Event Enable 0 (IFEER0).
 
You cannot disable both edge events of a given interrupt.
  NOTE  
Each external interrupt has an individual flag, held in DMA or Interrupt Status Flag 0 (DISR0). DISR0 is a clear-by-write-1 register, 
which prevents inadvertent overwriting of other flags in the same register.
Figure 25 provides an overview of the external interrupt implementation.
Glitch filter
Pads
Edge detection
EIF[31:24]
EIF[23:16]
Interrupt enable
EIF[15:8]
EIF[7:0]
EIRE[31:0]
IREE[31:0]
IFEE[31:0]
Interrupt edge 
enable rising
Falling
IFE[31:0]
IRQ glitch filter enable
MAXCOUNT[x]
Glitch filter counter_n
IFCP[3:0]
Glitch filter prescaler
Interrupt 
controller
Interrupt 
vectors
IRQ_31_24
OR
OR
OR
OR
IRQ_23_16
IRQ_15_08
IRQ_07_00
Figure 25. External interrupt pad diagram
10.3.4.3
External interrupt request
The REQ input pins on the chip are the sources for interrupt or DMA requests. The chip provides one possible interrupt vector for 
SIUL2. The 32 interrupt request sources map to vectors and channels as shown in Table 44.
Table 44. Interrupt source mapping to SIUL2 interrupt request output for 32 interrupt sources
Vector or channel #
Interrupt vector source
0
REQ[07] | REQ[06] | REQ[05] | REQ[04] | REQ[03] | REQ[02] | REQ[01] | REQ[00]
1
REQ[15] | REQ[14] | REQ[13] | REQ[12] | REQ[11] | REQ[10] | REQ[09] | REQ[08]
2
REQ[23] | REQ[22] | REQ[21] | REQ[20] | REQ[19] | REQ[18] | REQ[17] | REQ[16]
3
REQ[31] | REQ[30] | REQ[29] | REQ[28] | REQ[27] | REQ[26] | REQ[25] | REQ[24]
10.3.5 DMA requests
The REQ pins on the chip map to the independent DMA request channels in the DMA controller. See the DMAMUX map file 
attached to this document for the mapping of DMA sources to DMA channels.
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
307 / 5251


---
# 페이지 257

DISR0 and DIRSR0 manage DMA requests in the following way:
• Service a DMA request to clear the DISR0 register flags.
• Write to the appropriate DIRSR0[DIRSn] to select a request between DMA or interrupt.
• If you select DMA in DIRSR0 and set the corresponding DISR0 flag for it, SIUL2 sends a DMA request signal as an output.
10.4 External signal description
See the IOMUX file attached to this document for more information.
10.5 Initialization
This module does not require initialization.
10.6 SIUL2 register descriptions
This section describes the SIUL2 registers.
• Undocumented register spaces in the SIUL2 memory map, including addresses shown as blanks, are reserved:
— Reserved registers or spaces are read as 0.
— Writes to reserved registers or spaces generate a transfer error.
• Writes to read-only registers generate a transfer error.
 
• For the array of 8-bit registers, GPDOn and GPDIn:
— An 8-bit access to an unimplemented address (a "hole") within the array region generates a 
transfer error.
— However, when you perform a 16-bit or 32-bit access and if any register instance is implemented within 
the accessed range, a transfer error is not generated even if the range includes a hole.
• For the array of 16-bit registers, PGPDOn and PGPDIn:
— A 16-bit access to an unimplemented address (a "hole") within the array region generates a 
transfer error.
— However, a 32-bit access does not generate a transfer error for a hole irrespective of whether the other 
16-bit range includes a register instance.
  NOTE  
10.6.1 SIUL2 memory map
SIUL2 base address: 4029_0000h
Offset
Register
Width
(In bits)
Access
Reset value
4h
SIUL2 MCU ID Register #1 (MIDR1)
32
R
See section
8h
SIUL2 MCU ID Register #2 (MIDR2)
32
R
See section
10h
DMA or Interrupt Status Flag 0 (DISR0)
32
RW
0000_0000h
18h
DMA or Interrupt Request Enable 0 (DIRER0)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
308 / 5251


---
# 페이지 258

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
20h
DMA or Interrupt Request Select 0 (DIRSR0)
32
RW
0000_0000h
28h
Interrupt Rising-Edge Event Enable 0 (IREER0)
32
RW
0000_0000h
30h
Interrupt Falling-Edge Event Enable 0 (IFEER0)
32
RW
0000_0000h
38h
Interrupt Filter Enable 0 (IFER0)
32
RW
0000_0000h
40h - BCh
Interrupt Filter Maximum Counter (IFMCR0 - IFMCR31)
32
RW
0000_0000h
C0h
Interrupt Filter Clock Prescaler (IFCPR)
32
RW
0000_0000h
100h
MUX0 EMIOS ENABLE 1 (MUX0_EMIOS_EN1)
32
RW
See section
104h
MUX0 MISC ENABLE (MUX0_MISC_EN)
32
RW
See section
108h
MUX1 EMIOS ENABLE (MUX1_EMIOS_EN)
32
RW
See section
10Ch
MUX1 MISC ENABLE (MUX1_MISC_EN)
32
RW
See section
110h
MUX2 EMIOS ENABLE (MUX2_EMIOS_EN)
32
RW
See section
114h
MUX2 MISC ENABLE (MUX2_MISC_EN)
32
RW
See section
200h
SIUL2 MCU ID Register #3 (MIDR3)
32
R
See section
204h
SIUL2 MCU ID Register #4 (MIDR4)
32
R
See section
240h
Multiplexed Signal Configuration (MSCR0)
32
RW
0000_0000h
244h
Multiplexed Signal Configuration (MSCR1)
32
RW
0000_0000h
248h
Multiplexed Signal Configuration (MSCR2)
32
RW
0000_0000h
24Ch
Multiplexed Signal Configuration (MSCR3)
32
RW
0000_0000h
250h
Multiplexed Signal Configuration (MSCR4)
32
RW
0008_2827h
254h
Multiplexed Signal Configuration (MSCR5)
32
RW
0000_0000h
258h
Multiplexed Signal Configuration (MSCR6)
32
RW
0000_0000h
25Ch
Multiplexed Signal Configuration (MSCR7)
32
RW
0000_0000h
260h
Multiplexed Signal Configuration (MSCR8)
32
RW
0000_0000h
264h
Multiplexed Signal Configuration (MSCR9)
32
RW
0000_0000h
268h
Multiplexed Signal Configuration (MSCR10)
32
RW
0000_0127h
26Ch
Multiplexed Signal Configuration (MSCR11)
32
RW
0000_0000h
270h
Multiplexed Signal Configuration (MSCR12)
32
RW
0000_0003h
274h
Multiplexed Signal Configuration (MSCR13)
32
RW
0000_0000h
278h
Multiplexed Signal Configuration (MSCR14)
32
RW
0000_0000h
27Ch
Multiplexed Signal Configuration (MSCR15)
32
RW
0000_0000h
280h
Multiplexed Signal Configuration (MSCR16)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
309 / 5251


---
# 페이지 259

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
284h
Multiplexed Signal Configuration (MSCR17)
32
RW
0000_0000h
288h
Multiplexed Signal Configuration (MSCR18)
32
RW
0000_0000h
28Ch
Multiplexed Signal Configuration (MSCR19)
32
RW
0000_0000h
290h
Multiplexed Signal Configuration (MSCR20)
32
RW
0000_0000h
294h
Multiplexed Signal Configuration (MSCR21)
32
RW
0000_0000h
298h
Multiplexed Signal Configuration (MSCR22)
32
RW
0000_0000h
29Ch
Multiplexed Signal Configuration (MSCR23)
32
RW
0000_0000h
2A0h
Multiplexed Signal Configuration (MSCR24)
32
RW
0000_0000h
2A4h
Multiplexed Signal Configuration (MSCR25)
32
RW
0000_0000h
2A8h
Multiplexed Signal Configuration (MSCR26)
32
RW
0000_0000h
2ACh
Multiplexed Signal Configuration (MSCR27)
32
RW
0000_0000h
2B0h
Multiplexed Signal Configuration (MSCR28)
32
RW
0000_0000h
2B4h
Multiplexed Signal Configuration (MSCR29)
32
RW
0000_0000h
2B8h
Multiplexed Signal Configuration (MSCR30)
32
RW
0000_0000h
2BCh
Multiplexed Signal Configuration (MSCR31)
32
RW
0000_0000h
2C0h
Multiplexed Signal Configuration (MSCR32)
32
RW
0000_0000h
2C4h
Multiplexed Signal Configuration (MSCR33)
32
RW
0000_0000h
2C8h
Multiplexed Signal Configuration (MSCR34)
32
RW
0000_0000h
2CCh
Multiplexed Signal Configuration (MSCR35)
32
RW
0000_0000h
2D0h
Multiplexed Signal Configuration (MSCR36)
32
RW
0000_0000h
2D4h
Multiplexed Signal Configuration (MSCR37)
32
RW
0000_0000h
2E0h
Multiplexed Signal Configuration (MSCR40)
32
RW
0000_0000h
2E4h
Multiplexed Signal Configuration (MSCR41)
32
RW
0000_0000h
2E8h
Multiplexed Signal Configuration (MSCR42)
32
RW
0000_0000h
2ECh
Multiplexed Signal Configuration (MSCR43)
32
RW
0000_0000h
2F0h
Multiplexed Signal Configuration (MSCR44)
32
RW
0000_0000h
2F4h
Multiplexed Signal Configuration (MSCR45)
32
RW
0000_0000h
2F8h
Multiplexed Signal Configuration (MSCR46)
32
RW
0000_0000h
2FCh
Multiplexed Signal Configuration (MSCR47)
32
RW
0000_0000h
300h
Multiplexed Signal Configuration (MSCR48)
32
RW
0000_0000h
304h
Multiplexed Signal Configuration (MSCR49)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
310 / 5251


---
# 페이지 260

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
308h
Multiplexed Signal Configuration (MSCR50)
32
RW
0000_0000h
30Ch
Multiplexed Signal Configuration (MSCR51)
32
RW
0000_0000h
310h
Multiplexed Signal Configuration (MSCR52)
32
RW
0000_0000h
314h
Multiplexed Signal Configuration (MSCR53)
32
RW
0000_0000h
318h
Multiplexed Signal Configuration (MSCR54)
32
RW
0000_0000h
31Ch
Multiplexed Signal Configuration (MSCR55)
32
RW
0000_0000h
320h
Multiplexed Signal Configuration (MSCR56)
32
RW
0000_0000h
324h
Multiplexed Signal Configuration (MSCR57)
32
RW
0000_0000h
328h
Multiplexed Signal Configuration (MSCR58)
32
RW
0000_0000h
32Ch
Multiplexed Signal Configuration (MSCR59)
32
RW
0000_0000h
330h
Multiplexed Signal Configuration (MSCR60)
32
RW
0000_0000h
334h
Multiplexed Signal Configuration (MSCR61)
32
RW
0000_0000h
338h
Multiplexed Signal Configuration (MSCR62)
32
RW
0000_0000h
33Ch
Multiplexed Signal Configuration (MSCR63)
32
RW
0000_0000h
340h
Multiplexed Signal Configuration (MSCR64)
32
RW
0000_0000h
344h
Multiplexed Signal Configuration (MSCR65)
32
RW
0000_0000h
348h
Multiplexed Signal Configuration (MSCR66)
32
RW
0000_4000h
34Ch
Multiplexed Signal Configuration (MSCR67)
32
RW
0000_4000h
350h
Multiplexed Signal Configuration (MSCR68)
32
RW
0008_2000h
354h
Multiplexed Signal Configuration (MSCR69)
32
RW
0008_2800h
358h
Multiplexed Signal Configuration (MSCR70)
32
RW
0000_0000h
35Ch
Multiplexed Signal Configuration (MSCR71)
32
RW
0000_0000h
360h
Multiplexed Signal Configuration (MSCR72)
32
RW
0000_0000h
364h
Multiplexed Signal Configuration (MSCR73)
32
RW
0000_0000h
368h
Multiplexed Signal Configuration (MSCR74)
32
RW
0000_0000h
36Ch
Multiplexed Signal Configuration (MSCR75)
32
RW
0000_0000h
370h
Multiplexed Signal Configuration (MSCR76)
32
RW
0000_4000h
374h
Multiplexed Signal Configuration (MSCR77)
32
RW
0000_0000h
378h
Multiplexed Signal Configuration (MSCR78)
32
RW
0000_0000h
37Ch
Multiplexed Signal Configuration (MSCR79)
32
RW
0000_0000h
380h
Multiplexed Signal Configuration (MSCR80)
32
RW
0000_4000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
311 / 5251


---
# 페이지 261

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
384h
Multiplexed Signal Configuration (MSCR81)
32
RW
0000_0000h
388h
Multiplexed Signal Configuration (MSCR82)
32
RW
0000_0000h
38Ch
Multiplexed Signal Configuration (MSCR83)
32
RW
0000_0000h
390h
Multiplexed Signal Configuration (MSCR84)
32
RW
0000_0000h
394h
Multiplexed Signal Configuration (MSCR85)
32
RW
0000_0000h
398h
Multiplexed Signal Configuration (MSCR86)
32
RW
0000_0000h
39Ch
Multiplexed Signal Configuration (MSCR87)
32
RW
0000_0000h
3A0h
Multiplexed Signal Configuration (MSCR88)
32
RW
0000_0000h
3A4h
Multiplexed Signal Configuration (MSCR89)
32
RW
0000_0000h
3A8h
Multiplexed Signal Configuration (MSCR90)
32
RW
0000_0000h
3ACh
Multiplexed Signal Configuration (MSCR91)
32
RW
0000_0000h
3B0h
Multiplexed Signal Configuration (MSCR92)
32
RW
0000_0000h
3B4h
Multiplexed Signal Configuration (MSCR93)
32
RW
0000_0000h
3B8h
Multiplexed Signal Configuration (MSCR94)
32
RW
0000_0000h
3BCh
Multiplexed Signal Configuration (MSCR95)
32
RW
0000_0000h
3C0h
Multiplexed Signal Configuration (MSCR96)
32
RW
0000_0000h
3C4h
Multiplexed Signal Configuration (MSCR97)
32
RW
0000_0000h
3C8h
Multiplexed Signal Configuration (MSCR98)
32
RW
0000_0000h
3CCh
Multiplexed Signal Configuration (MSCR99)
32
RW
0000_0000h
3D0h
Multiplexed Signal Configuration (MSCR100)
32
RW
0000_0000h
3D4h
Multiplexed Signal Configuration (MSCR101)
32
RW
0000_4000h
3D8h
Multiplexed Signal Configuration (MSCR102)
32
RW
0000_4000h
3DCh
Multiplexed Signal Configuration (MSCR103)
32
RW
0000_4000h
3E0h
Multiplexed Signal Configuration (MSCR104)
32
RW
0000_0000h
3E4h
Multiplexed Signal Configuration (MSCR105)
32
RW
0000_0000h
3E8h
Multiplexed Signal Configuration (MSCR106)
32
RW
0000_4000h
3ECh
Multiplexed Signal Configuration (MSCR107)
32
RW
0000_4000h
3F0h
Multiplexed Signal Configuration (MSCR108)
32
RW
0000_4000h
3F4h
Multiplexed Signal Configuration (MSCR109)
32
RW
0000_0000h
3F8h
Multiplexed Signal Configuration (MSCR110)
32
RW
0000_0000h
3FCh
Multiplexed Signal Configuration (MSCR111)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
312 / 5251


---
# 페이지 262

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
400h
Multiplexed Signal Configuration (MSCR112)
32
RW
0000_0000h
404h
Multiplexed Signal Configuration (MSCR113)
32
RW
0000_0000h
408h
Multiplexed Signal Configuration (MSCR114)
32
RW
0000_0000h
40Ch
Multiplexed Signal Configuration (MSCR115)
32
RW
0000_0000h
410h
Multiplexed Signal Configuration (MSCR116)
32
RW
0000_0000h
414h
Multiplexed Signal Configuration (MSCR117)
32
RW
0000_0000h
418h
Multiplexed Signal Configuration (MSCR118)
32
RW
0000_0000h
41Ch
Multiplexed Signal Configuration (MSCR119)
32
RW
0000_0000h
420h
Multiplexed Signal Configuration (MSCR120)
32
RW
0000_0000h
424h
Multiplexed Signal Configuration (MSCR121)
32
RW
0000_0000h
428h
Multiplexed Signal Configuration (MSCR122)
32
RW
0000_0000h
42Ch
Multiplexed Signal Configuration (MSCR123)
32
RW
0000_0000h
430h
Multiplexed Signal Configuration (MSCR124)
32
RW
0000_0000h
434h
Multiplexed Signal Configuration (MSCR125)
32
RW
0000_0000h
438h
Multiplexed Signal Configuration (MSCR126)
32
RW
0000_0000h
43Ch
Multiplexed Signal Configuration (MSCR127)
32
RW
0000_0000h
440h
Multiplexed Signal Configuration (MSCR128)
32
RW
0000_0000h
444h
Multiplexed Signal Configuration (MSCR129)
32
RW
0000_0000h
448h
Multiplexed Signal Configuration (MSCR130)
32
RW
0000_0000h
44Ch
Multiplexed Signal Configuration (MSCR131)
32
RW
0000_0000h
450h
Multiplexed Signal Configuration (MSCR132)
32
RW
0000_0000h
454h
Multiplexed Signal Configuration (MSCR133)
32
RW
0000_0000h
458h
Multiplexed Signal Configuration (MSCR134)
32
RW
0000_0000h
45Ch
Multiplexed Signal Configuration (MSCR135)
32
RW
0000_0000h
460h
Multiplexed Signal Configuration (MSCR136)
32
RW
0000_4000h
464h
Multiplexed Signal Configuration (MSCR137)
32
RW
0000_0000h
468h
Multiplexed Signal Configuration (MSCR138)
32
RW
0000_0000h
46Ch
Multiplexed Signal Configuration (MSCR139)
32
RW
0000_0000h
470h
Multiplexed Signal Configuration (MSCR140)
32
RW
0000_0000h
478h
Multiplexed Signal Configuration (MSCR142)
32
RW
0000_0000h
47Ch
Multiplexed Signal Configuration (MSCR143)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
313 / 5251


---
# 페이지 263

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
480h
Multiplexed Signal Configuration (MSCR144)
32
RW
0000_0000h
484h
Multiplexed Signal Configuration (MSCR145)
32
RW
0000_0000h
488h
Multiplexed Signal Configuration (MSCR146)
32
RW
0000_0000h
48Ch
Multiplexed Signal Configuration (MSCR147)
32
RW
0000_0000h
490h
Multiplexed Signal Configuration (MSCR148)
32
RW
0000_0000h
494h
Multiplexed Signal Configuration (MSCR149)
32
RW
0000_0000h
498h
Multiplexed Signal Configuration (MSCR150)
32
RW
0000_0000h
49Ch
Multiplexed Signal Configuration (MSCR151)
32
RW
0000_0000h
4A0h
Multiplexed Signal Configuration (MSCR152)
32
RW
0000_0000h
4A4h
Multiplexed Signal Configuration (MSCR153)
32
RW
0000_0000h
4A8h
Multiplexed Signal Configuration (MSCR154)
32
RW
0000_0000h
4ACh
Multiplexed Signal Configuration (MSCR155)
32
RW
0000_0000h
4B0h
Multiplexed Signal Configuration (MSCR156)
32
RW
0000_0000h
4B4h
Multiplexed Signal Configuration (MSCR157)
32
RW
0000_0000h
4B8h
Multiplexed Signal Configuration (MSCR158)
32
RW
0000_0000h
4BCh
Multiplexed Signal Configuration (MSCR159)
32
RW
0000_0000h
4C0h
Multiplexed Signal Configuration (MSCR160)
32
RW
0000_0000h
4C4h
Multiplexed Signal Configuration (MSCR161)
32
RW
0000_0000h
4C8h
Multiplexed Signal Configuration (MSCR162)
32
RW
0000_0000h
4CCh
Multiplexed Signal Configuration (MSCR163)
32
RW
0000_0000h
4D0h
Multiplexed Signal Configuration (MSCR164)
32
RW
0000_0000h
4D4h
Multiplexed Signal Configuration (MSCR165)
32
RW
0000_0000h
4D8h
Multiplexed Signal Configuration (MSCR166)
32
RW
0000_0000h
4DCh
Multiplexed Signal Configuration (MSCR167)
32
RW
0000_0000h
4E0h
Multiplexed Signal Configuration (MSCR168)
32
RW
0000_0000h
4E4h
Multiplexed Signal Configuration (MSCR169)
32
RW
0000_0000h
4E8h
Multiplexed Signal Configuration (MSCR170)
32
RW
0000_0000h
4ECh
Multiplexed Signal Configuration (MSCR171)
32
RW
0000_0000h
4F0h
Multiplexed Signal Configuration (MSCR172)
32
RW
0000_0000h
4F4h
Multiplexed Signal Configuration (MSCR173)
32
RW
0000_0000h
4F8h
Multiplexed Signal Configuration (MSCR174)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
314 / 5251


---
# 페이지 264

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
4FCh
Multiplexed Signal Configuration (MSCR175)
32
RW
0000_0000h
500h
Multiplexed Signal Configuration (MSCR176)
32
RW
0000_0000h
504h
Multiplexed Signal Configuration (MSCR177)
32
RW
0000_0000h
508h
Multiplexed Signal Configuration (MSCR178)
32
RW
0000_0000h
50Ch
Multiplexed Signal Configuration (MSCR179)
32
RW
0000_0000h
510h
Multiplexed Signal Configuration (MSCR180)
32
RW
0000_0000h
514h
Multiplexed Signal Configuration (MSCR181)
32
RW
0000_0000h
518h
Multiplexed Signal Configuration (MSCR182)
32
RW
0000_0000h
51Ch
Multiplexed Signal Configuration (MSCR183)
32
RW
0000_0000h
520h
Multiplexed Signal Configuration (MSCR184)
32
RW
0000_0000h
524h
Multiplexed Signal Configuration (MSCR185)
32
RW
0000_0000h
528h
Multiplexed Signal Configuration (MSCR186)
32
RW
0000_0000h
52Ch
Multiplexed Signal Configuration (MSCR187)
32
RW
0000_0000h
530h
Multiplexed Signal Configuration (MSCR188)
32
RW
0000_0000h
534h
Multiplexed Signal Configuration (MSCR189)
32
RW
0000_0000h
538h
Multiplexed Signal Configuration (MSCR190)
32
RW
0000_0000h
53Ch
Multiplexed Signal Configuration (MSCR191)
32
RW
0000_0000h
540h
Multiplexed Signal Configuration (MSCR192)
32
RW
0000_0000h
544h
Multiplexed Signal Configuration (MSCR193)
32
RW
0000_0000h
548h
Multiplexed Signal Configuration (MSCR194)
32
RW
0000_0000h
54Ch
Multiplexed Signal Configuration (MSCR195)
32
RW
0000_0000h
550h
Multiplexed Signal Configuration (MSCR196)
32
RW
0000_0000h
554h
Multiplexed Signal Configuration (MSCR197)
32
RW
0000_0000h
558h
Multiplexed Signal Configuration (MSCR198)
32
RW
0000_0000h
55Ch
Multiplexed Signal Configuration (MSCR199)
32
RW
0000_0000h
560h
Multiplexed Signal Configuration (MSCR200)
32
RW
0000_0000h
564h
Multiplexed Signal Configuration (MSCR201)
32
RW
0000_0000h
568h
Multiplexed Signal Configuration (MSCR202)
32
RW
0000_0000h
56Ch
Multiplexed Signal Configuration (MSCR203)
32
RW
0000_0000h
570h
Multiplexed Signal Configuration (MSCR204)
32
RW
0000_0000h
574h
Multiplexed Signal Configuration (MSCR205)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
315 / 5251


---
# 페이지 265

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
578h
Multiplexed Signal Configuration (MSCR206)
32
RW
0000_0000h
57Ch
Multiplexed Signal Configuration (MSCR207)
32
RW
0000_0000h
580h
Multiplexed Signal Configuration (MSCR208)
32
RW
0000_0000h
584h
Multiplexed Signal Configuration (MSCR209)
32
RW
0000_0000h
588h
Multiplexed Signal Configuration (MSCR210)
32
RW
0000_0000h
58Ch
Multiplexed Signal Configuration (MSCR211)
32
RW
0000_0000h
590h
Multiplexed Signal Configuration (MSCR212)
32
RW
0000_0000h
594h
Multiplexed Signal Configuration (MSCR213)
32
RW
0000_0000h
598h
Multiplexed Signal Configuration (MSCR214)
32
RW
0000_0000h
59Ch
Multiplexed Signal Configuration (MSCR215)
32
RW
0000_0000h
5A0h
Multiplexed Signal Configuration (MSCR216)
32
RW
0000_0000h
5A4h
Multiplexed Signal Configuration (MSCR217)
32
RW
0000_0000h
5A8h
Multiplexed Signal Configuration (MSCR218)
32
RW
0000_0000h
5ACh
Multiplexed Signal Configuration (MSCR219)
32
RW
0000_0000h
5B0h
Multiplexed Signal Configuration (MSCR220)
32
RW
0000_0000h
5B4h
Multiplexed Signal Configuration (MSCR221)
32
RW
0000_0000h
5B8h
Multiplexed Signal Configuration (MSCR222)
32
RW
0000_0000h
5BCh
Multiplexed Signal Configuration (MSCR223)
32
RW
0000_0000h
5C0h
Multiplexed Signal Configuration (MSCR224)
32
RW
0000_0000h
5C4h
Multiplexed Signal Configuration (MSCR225)
32
RW
0000_0000h
5C8h
Multiplexed Signal Configuration (MSCR226)
32
RW
0000_0000h
5CCh
Multiplexed Signal Configuration (MSCR227)
32
RW
0000_0000h
5D0h
Multiplexed Signal Configuration (MSCR228)
32
RW
0000_0000h
5D4h
Multiplexed Signal Configuration (MSCR229)
32
RW
0000_0000h
5D8h
Multiplexed Signal Configuration (MSCR230)
32
RW
0000_0000h
5DCh
Multiplexed Signal Configuration (MSCR231)
32
RW
0000_0000h
5E0h
Multiplexed Signal Configuration (MSCR232)
32
RW
0000_0000h
5E4h
Multiplexed Signal Configuration (MSCR233)
32
RW
0000_0000h
5E8h
Multiplexed Signal Configuration (MSCR234)
32
RW
0000_0000h
5ECh
Multiplexed Signal Configuration (MSCR235)
32
RW
0000_0000h
5F0h
Multiplexed Signal Configuration (MSCR236)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
316 / 5251


---
# 페이지 266

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
5F4h
Multiplexed Signal Configuration (MSCR237)
32
RW
0000_0000h
5F8h
Multiplexed Signal Configuration (MSCR238)
32
RW
0000_0000h
5FCh
Multiplexed Signal Configuration (MSCR239)
32
RW
0000_0000h
600h
Multiplexed Signal Configuration (MSCR240)
32
RW
0000_0000h
604h
Multiplexed Signal Configuration (MSCR241)
32
RW
0000_0000h
608h
Multiplexed Signal Configuration (MSCR242)
32
RW
0000_0000h
60Ch
Multiplexed Signal Configuration (MSCR243)
32
RW
0000_0000h
610h
Multiplexed Signal Configuration (MSCR244)
32
RW
0000_0000h
614h
Multiplexed Signal Configuration (MSCR245)
32
RW
0000_0000h
618h
Multiplexed Signal Configuration (MSCR246)
32
RW
0000_0000h
61Ch
Multiplexed Signal Configuration (MSCR247)
32
RW
0000_0000h
620h
Multiplexed Signal Configuration (MSCR248)
32
RW
0000_0000h
624h
Multiplexed Signal Configuration (MSCR249)
32
RW
0000_0000h
628h
Multiplexed Signal Configuration (MSCR250)
32
RW
0000_0000h
62Ch
Multiplexed Signal Configuration (MSCR251)
32
RW
0000_0000h
630h
Multiplexed Signal Configuration (MSCR252)
32
RW
0000_0000h
634h
Multiplexed Signal Configuration (MSCR253)
32
RW
0000_0000h
638h
Multiplexed Signal Configuration (MSCR254)
32
RW
0000_0000h
63Ch
Multiplexed Signal Configuration (MSCR255)
32
RW
0000_0000h
640h
Multiplexed Signal Configuration (MSCR256)
32
RW
0000_0000h
644h
Multiplexed Signal Configuration (MSCR257)
32
RW
0000_0000h
648h
Multiplexed Signal Configuration (MSCR258)
32
RW
0000_0000h
64Ch
Multiplexed Signal Configuration (MSCR259)
32
RW
0000_0000h
650h
Multiplexed Signal Configuration (MSCR260)
32
RW
0000_0000h
654h
Multiplexed Signal Configuration (MSCR261)
32
RW
0000_0000h
658h
Multiplexed Signal Configuration (MSCR262)
32
RW
0000_0000h
65Ch
Multiplexed Signal Configuration (MSCR263)
32
RW
0000_0000h
660h
Multiplexed Signal Configuration (MSCR264)
32
RW
0000_0000h
664h
Multiplexed Signal Configuration (MSCR265)
32
RW
0000_0000h
668h
Multiplexed Signal Configuration (MSCR266)
32
RW
0000_0000h
66Ch
Multiplexed Signal Configuration (MSCR267)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
317 / 5251


---
# 페이지 267

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
670h
Multiplexed Signal Configuration (MSCR268)
32
RW
0000_0000h
674h
Multiplexed Signal Configuration (MSCR269)
32
RW
0000_0000h
678h
Multiplexed Signal Configuration (MSCR270)
32
RW
0000_0000h
67Ch
Multiplexed Signal Configuration (MSCR271)
32
RW
0000_0000h
680h
Multiplexed Signal Configuration (MSCR272)
32
RW
0000_0000h
684h
Multiplexed Signal Configuration (MSCR273)
32
RW
0000_0000h
688h
Multiplexed Signal Configuration (MSCR274)
32
RW
0000_0000h
68Ch
Multiplexed Signal Configuration (MSCR275)
32
RW
0000_0000h
690h
Multiplexed Signal Configuration (MSCR276)
32
RW
0000_0000h
694h
Multiplexed Signal Configuration (MSCR277)
32
RW
0000_0000h
698h
Multiplexed Signal Configuration (MSCR278)
32
RW
0000_0000h
69Ch
Multiplexed Signal Configuration (MSCR279)
32
RW
0000_0000h
6A0h
Multiplexed Signal Configuration (MSCR280)
32
RW
0000_0000h
6A4h
Multiplexed Signal Configuration (MSCR281)
32
RW
0000_0000h
6A8h
Multiplexed Signal Configuration (MSCR282)
32
RW
0000_0000h
6ACh
Multiplexed Signal Configuration (MSCR283)
32
RW
0000_0000h
6B0h
Multiplexed Signal Configuration (MSCR284)
32
RW
0000_0000h
6B4h
Multiplexed Signal Configuration (MSCR285)
32
RW
0000_0000h
6B8h
Multiplexed Signal Configuration (MSCR286)
32
RW
0000_0000h
6BCh
Multiplexed Signal Configuration (MSCR287)
32
RW
0000_0000h
6C0h
Multiplexed Signal Configuration (MSCR288)
32
RW
0000_0000h
6C4h
Multiplexed Signal Configuration (MSCR289)
32
RW
0000_0000h
6C8h
Multiplexed Signal Configuration (MSCR290)
32
RW
0000_0000h
6CCh
Multiplexed Signal Configuration (MSCR291)
32
RW
0000_0000h
6D0h
Multiplexed Signal Configuration (MSCR292)
32
RW
0000_0000h
6D4h
Multiplexed Signal Configuration (MSCR293)
32
RW
0000_0000h
6D8h
Multiplexed Signal Configuration (MSCR294)
32
RW
0000_0000h
6DCh
Multiplexed Signal Configuration (MSCR295)
32
RW
0000_0000h
6E0h
Multiplexed Signal Configuration (MSCR296)
32
RW
0000_0000h
6E4h
Multiplexed Signal Configuration (MSCR297)
32
RW
0000_0000h
6E8h
Multiplexed Signal Configuration (MSCR298)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
318 / 5251


---
# 페이지 268

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
6ECh
Multiplexed Signal Configuration (MSCR299)
32
RW
0000_0000h
6F0h
Multiplexed Signal Configuration (MSCR300)
32
RW
0000_0000h
6F4h
Multiplexed Signal Configuration (MSCR301)
32
RW
0000_0000h
6F8h
Multiplexed Signal Configuration (MSCR302)
32
RW
0000_0000h
6FCh
Multiplexed Signal Configuration (MSCR303)
32
RW
0000_0000h
700h
Multiplexed Signal Configuration (MSCR304)
32
RW
0000_0000h
704h
Multiplexed Signal Configuration (MSCR305)
32
RW
0000_0000h
708h
Multiplexed Signal Configuration (MSCR306)
32
RW
0000_0000h
70Ch
Multiplexed Signal Configuration (MSCR307)
32
RW
0000_0000h
710h
Multiplexed Signal Configuration (MSCR308)
32
RW
0000_0000h
714h
Multiplexed Signal Configuration (MSCR309)
32
RW
0000_0000h
718h
Multiplexed Signal Configuration (MSCR310)
32
RW
0000_0000h
71Ch
Multiplexed Signal Configuration (MSCR311)
32
RW
0000_0000h
720h
Multiplexed Signal Configuration (MSCR312)
32
RW
0000_0000h
724h
Multiplexed Signal Configuration (MSCR313)
32
RW
0000_0000h
728h
Multiplexed Signal Configuration (MSCR314)
32
RW
0000_0000h
72Ch
Multiplexed Signal Configuration (MSCR315)
32
RW
0000_0000h
730h
Multiplexed Signal Configuration (MSCR316)
32
RW
0000_0000h
734h
Multiplexed Signal Configuration (MSCR317)
32
RW
0000_0000h
738h
Multiplexed Signal Configuration (MSCR318)
32
RW
0000_0000h
73Ch
Multiplexed Signal Configuration (MSCR319)
32
RW
0000_0000h
740h
Multiplexed Signal Configuration (MSCR320)
32
RW
0000_0000h
744h
Multiplexed Signal Configuration (MSCR321)
32
RW
0000_0000h
748h
Multiplexed Signal Configuration (MSCR322)
32
RW
0000_0000h
74Ch
Multiplexed Signal Configuration (MSCR323)
32
RW
0000_0000h
A40h
Input Multiplexed Signal Configuration (IMCR0)
32
RW
0000_0000h
A44h
Input Multiplexed Signal Configuration (IMCR1)
32
RW
0000_0000h
A48h
Input Multiplexed Signal Configuration (IMCR2)
32
RW
0000_0000h
A4Ch
Input Multiplexed Signal Configuration (IMCR3)
32
RW
0000_0000h
A50h
Input Multiplexed Signal Configuration (IMCR4)
32
RW
0000_0000h
A54h
Input Multiplexed Signal Configuration (IMCR5)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
319 / 5251


---
# 페이지 269

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
A80h
Input Multiplexed Signal Configuration (IMCR16)
32
RW
0000_0000h
A84h
Input Multiplexed Signal Configuration (IMCR17)
32
RW
0000_0000h
A88h
Input Multiplexed Signal Configuration (IMCR18)
32
RW
0000_0000h
A8Ch
Input Multiplexed Signal Configuration (IMCR19)
32
RW
0000_0000h
A90h
Input Multiplexed Signal Configuration (IMCR20)
32
RW
0000_0000h
A94h
Input Multiplexed Signal Configuration (IMCR21)
32
RW
0000_0000h
A98h
Input Multiplexed Signal Configuration (IMCR22)
32
RW
0000_0000h
A9Ch
Input Multiplexed Signal Configuration (IMCR23)
32
RW
0000_0000h
AA0h
Input Multiplexed Signal Configuration (IMCR24)
32
RW
0000_0000h
AA4h
Input Multiplexed Signal Configuration (IMCR25)
32
RW
0000_0000h
AA8h
Input Multiplexed Signal Configuration (IMCR26)
32
RW
0000_0000h
AACh
Input Multiplexed Signal Configuration (IMCR27)
32
RW
0000_0000h
AB0h
Input Multiplexed Signal Configuration (IMCR28)
32
RW
0000_0000h
AB4h
Input Multiplexed Signal Configuration (IMCR29)
32
RW
0000_0000h
AB8h
Input Multiplexed Signal Configuration (IMCR30)
32
RW
0000_0000h
ABCh
Input Multiplexed Signal Configuration (IMCR31)
32
RW
0000_0000h
AC0h
Input Multiplexed Signal Configuration (IMCR32)
32
RW
0000_0000h
AC4h
Input Multiplexed Signal Configuration (IMCR33)
32
RW
0000_0000h
AC8h
Input Multiplexed Signal Configuration (IMCR34)
32
RW
0000_0000h
ACCh
Input Multiplexed Signal Configuration (IMCR35)
32
RW
0000_0000h
AD0h
Input Multiplexed Signal Configuration (IMCR36)
32
RW
0000_0000h
AD4h
Input Multiplexed Signal Configuration (IMCR37)
32
RW
0000_0000h
AD8h
Input Multiplexed Signal Configuration (IMCR38)
32
RW
0000_0000h
ADCh
Input Multiplexed Signal Configuration (IMCR39)
32
RW
0000_0000h
AE0h
Input Multiplexed Signal Configuration (IMCR40)
32
RW
0000_0000h
AE4h
Input Multiplexed Signal Configuration (IMCR41)
32
RW
0000_0000h
AE8h
Input Multiplexed Signal Configuration (IMCR42)
32
RW
0000_0000h
AECh
Input Multiplexed Signal Configuration (IMCR43)
32
RW
0000_0000h
AF0h
Input Multiplexed Signal Configuration (IMCR44)
32
RW
0000_0000h
AF4h
Input Multiplexed Signal Configuration (IMCR45)
32
RW
0000_0000h
AF8h
Input Multiplexed Signal Configuration (IMCR46)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
320 / 5251


---
# 페이지 270

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
AFCh
Input Multiplexed Signal Configuration (IMCR47)
32
RW
0000_0000h
B00h
Input Multiplexed Signal Configuration (IMCR48)
32
RW
0000_0000h
B04h
Input Multiplexed Signal Configuration (IMCR49)
32
RW
0000_0000h
B08h
Input Multiplexed Signal Configuration (IMCR50)
32
RW
0000_0000h
B0Ch
Input Multiplexed Signal Configuration (IMCR51)
32
RW
0000_0000h
B10h
Input Multiplexed Signal Configuration (IMCR52)
32
RW
0000_0000h
B14h
Input Multiplexed Signal Configuration (IMCR53)
32
RW
0000_0000h
B18h
Input Multiplexed Signal Configuration (IMCR54)
32
RW
0000_0000h
B1Ch
Input Multiplexed Signal Configuration (IMCR55)
32
RW
0000_0000h
B20h
Input Multiplexed Signal Configuration (IMCR56)
32
RW
0000_0000h
B24h
Input Multiplexed Signal Configuration (IMCR57)
32
RW
0000_0000h
B28h
Input Multiplexed Signal Configuration (IMCR58)
32
RW
0000_0000h
B2Ch
Input Multiplexed Signal Configuration (IMCR59)
32
RW
0000_0000h
B30h
Input Multiplexed Signal Configuration (IMCR60)
32
RW
0000_0000h
B34h
Input Multiplexed Signal Configuration (IMCR61)
32
RW
0000_0000h
B38h
Input Multiplexed Signal Configuration (IMCR62)
32
RW
0000_0000h
B3Ch
Input Multiplexed Signal Configuration (IMCR63)
32
RW
0000_0000h
B40h
Input Multiplexed Signal Configuration (IMCR64)
32
RW
0000_0000h
B44h
Input Multiplexed Signal Configuration (IMCR65)
32
RW
0000_0000h
B48h
Input Multiplexed Signal Configuration (IMCR66)
32
RW
0000_0000h
B4Ch
Input Multiplexed Signal Configuration (IMCR67)
32
RW
0000_0000h
B50h
Input Multiplexed Signal Configuration (IMCR68)
32
RW
0000_0000h
B54h
Input Multiplexed Signal Configuration (IMCR69)
32
RW
0000_0000h
B58h
Input Multiplexed Signal Configuration (IMCR70)
32
RW
0000_0000h
B5Ch
Input Multiplexed Signal Configuration (IMCR71)
32
RW
0000_0000h
B80h
Input Multiplexed Signal Configuration (IMCR80)
32
RW
0000_0000h
B84h
Input Multiplexed Signal Configuration (IMCR81)
32
RW
0000_0000h
B88h
Input Multiplexed Signal Configuration (IMCR82)
32
RW
0000_0000h
B8Ch
Input Multiplexed Signal Configuration (IMCR83)
32
RW
0000_0000h
B90h
Input Multiplexed Signal Configuration (IMCR84)
32
RW
0000_0000h
B94h
Input Multiplexed Signal Configuration (IMCR85)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
321 / 5251


---
# 페이지 271

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
B98h
Input Multiplexed Signal Configuration (IMCR86)
32
RW
0000_0000h
B9Ch
Input Multiplexed Signal Configuration (IMCR87)
32
RW
0000_0000h
BA0h
Input Multiplexed Signal Configuration (IMCR88)
32
RW
0000_0000h
BA4h
Input Multiplexed Signal Configuration (IMCR89)
32
RW
0000_0000h
BA8h
Input Multiplexed Signal Configuration (IMCR90)
32
RW
0000_0000h
BACh
Input Multiplexed Signal Configuration (IMCR91)
32
RW
0000_0000h
BB0h
Input Multiplexed Signal Configuration (IMCR92)
32
RW
0000_0000h
BB4h
Input Multiplexed Signal Configuration (IMCR93)
32
RW
0000_0000h
BB8h
Input Multiplexed Signal Configuration (IMCR94)
32
RW
0000_0000h
BBCh
Input Multiplexed Signal Configuration (IMCR95)
32
RW
0000_0000h
BC0h
Input Multiplexed Signal Configuration (IMCR96)
32
RW
0000_0000h
BC4h
Input Multiplexed Signal Configuration (IMCR97)
32
RW
0000_0000h
BC8h
Input Multiplexed Signal Configuration (IMCR98)
32
RW
0000_0000h
BCCh
Input Multiplexed Signal Configuration (IMCR99)
32
RW
0000_0000h
BD0h
Input Multiplexed Signal Configuration (IMCR100)
32
RW
0000_0000h
BD4h
Input Multiplexed Signal Configuration (IMCR101)
32
RW
0000_0000h
BD8h
Input Multiplexed Signal Configuration (IMCR102)
32
RW
0000_0000h
BDCh
Input Multiplexed Signal Configuration (IMCR103)
32
RW
0000_0000h
C00h
Input Multiplexed Signal Configuration (IMCR112)
32
RW
0000_0000h
C04h
Input Multiplexed Signal Configuration (IMCR113)
32
RW
0000_0000h
C08h
Input Multiplexed Signal Configuration (IMCR114)
32
RW
0000_0000h
C0Ch
Input Multiplexed Signal Configuration (IMCR115)
32
RW
0000_0000h
C10h
Input Multiplexed Signal Configuration (IMCR116)
32
RW
0000_0000h
C14h
Input Multiplexed Signal Configuration (IMCR117)
32
RW
0000_0000h
C18h
Input Multiplexed Signal Configuration (IMCR118)
32
RW
0000_0000h
C1Ch
Input Multiplexed Signal Configuration (IMCR119)
32
RW
0000_0000h
C20h
Input Multiplexed Signal Configuration (IMCR120)
32
RW
0000_0000h
C24h
Input Multiplexed Signal Configuration (IMCR121)
32
RW
0000_0000h
C28h
Input Multiplexed Signal Configuration (IMCR122)
32
RW
0000_0000h
C2Ch
Input Multiplexed Signal Configuration (IMCR123)
32
RW
0000_0000h
C30h
Input Multiplexed Signal Configuration (IMCR124)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
322 / 5251


---
# 페이지 272

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
C34h
Input Multiplexed Signal Configuration (IMCR125)
32
RW
0000_0000h
C38h
Input Multiplexed Signal Configuration (IMCR126)
32
RW
0000_0000h
C3Ch
Input Multiplexed Signal Configuration (IMCR127)
32
RW
0000_0000h
C40h
Input Multiplexed Signal Configuration (IMCR128)
32
RW
0000_0000h
C44h
Input Multiplexed Signal Configuration (IMCR129)
32
RW
0000_0000h
C48h
Input Multiplexed Signal Configuration (IMCR130)
32
RW
0000_0000h
C4Ch
Input Multiplexed Signal Configuration (IMCR131)
32
RW
0000_0000h
C50h
Input Multiplexed Signal Configuration (IMCR132)
32
RW
0000_0000h
C54h
Input Multiplexed Signal Configuration (IMCR133)
32
RW
0000_0000h
C58h
Input Multiplexed Signal Configuration (IMCR134)
32
RW
0000_0000h
C5Ch
Input Multiplexed Signal Configuration (IMCR135)
32
RW
0000_0000h
C80h
Input Multiplexed Signal Configuration (IMCR144)
32
RW
0000_0000h
C84h
Input Multiplexed Signal Configuration (IMCR145)
32
RW
0000_0000h
C88h
Input Multiplexed Signal Configuration (IMCR146)
32
RW
0000_0000h
C8Ch
Input Multiplexed Signal Configuration (IMCR147)
32
RW
0000_0000h
C90h
Input Multiplexed Signal Configuration (IMCR148)
32
RW
0000_0000h
C94h
Input Multiplexed Signal Configuration (IMCR149)
32
RW
0000_0000h
CA0h
Input Multiplexed Signal Configuration (IMCR152)
32
RW
0000_0000h
CA4h
Input Multiplexed Signal Configuration (IMCR153)
32
RW
0000_0000h
CA8h
Input Multiplexed Signal Configuration (IMCR154)
32
RW
0000_0000h
CACh
Input Multiplexed Signal Configuration (IMCR155)
32
RW
0000_0000h
CB0h
Input Multiplexed Signal Configuration (IMCR156)
32
RW
0000_0000h
CB4h
Input Multiplexed Signal Configuration (IMCR157)
32
RW
0000_0000h
CB8h
Input Multiplexed Signal Configuration (IMCR158)
32
RW
0000_0000h
CBCh
Input Multiplexed Signal Configuration (IMCR159)
32
RW
0000_0000h
CC0h
Input Multiplexed Signal Configuration (IMCR160)
32
RW
0000_0000h
CC4h
Input Multiplexed Signal Configuration (IMCR161)
32
RW
0000_0000h
CC8h
Input Multiplexed Signal Configuration (IMCR162)
32
RW
0000_0000h
CCCh
Input Multiplexed Signal Configuration (IMCR163)
32
RW
0000_0000h
CD0h
Input Multiplexed Signal Configuration (IMCR164)
32
RW
0000_0000h
CD4h
Input Multiplexed Signal Configuration (IMCR165)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
323 / 5251


---
# 페이지 273

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
CD8h
Input Multiplexed Signal Configuration (IMCR166)
32
RW
0000_0000h
CDCh
Input Multiplexed Signal Configuration (IMCR167)
32
RW
0000_0000h
CE0h
Input Multiplexed Signal Configuration (IMCR168)
32
RW
0000_0000h
CE4h
Input Multiplexed Signal Configuration (IMCR169)
32
RW
0000_0000h
CE8h
Input Multiplexed Signal Configuration (IMCR170)
32
RW
0000_0000h
CECh
Input Multiplexed Signal Configuration (IMCR171)
32
RW
0000_0000h
CF0h
Input Multiplexed Signal Configuration (IMCR172)
32
RW
0000_0000h
CF4h
Input Multiplexed Signal Configuration (IMCR173)
32
RW
0000_0000h
CF8h
Input Multiplexed Signal Configuration (IMCR174)
32
RW
0000_0000h
CFCh
Input Multiplexed Signal Configuration (IMCR175)
32
RW
0000_0000h
D00h
Input Multiplexed Signal Configuration (IMCR176)
32
RW
0000_0000h
D04h
Input Multiplexed Signal Configuration (IMCR177)
32
RW
0000_0000h
D08h
Input Multiplexed Signal Configuration (IMCR178)
32
RW
0000_0000h
D0Ch
Input Multiplexed Signal Configuration (IMCR179)
32
RW
0000_0000h
D10h
Input Multiplexed Signal Configuration (IMCR180)
32
RW
0000_0000h
D14h
Input Multiplexed Signal Configuration (IMCR181)
32
RW
0000_0000h
D18h
Input Multiplexed Signal Configuration (IMCR182)
32
RW
0000_0000h
D1Ch
Input Multiplexed Signal Configuration (IMCR183)
32
RW
0000_0000h
D20h
Input Multiplexed Signal Configuration (IMCR184)
32
RW
0000_0000h
D24h
Input Multiplexed Signal Configuration (IMCR185)
32
RW
0000_0000h
D28h
Input Multiplexed Signal Configuration (IMCR186)
32
RW
0000_0000h
D2Ch
Input Multiplexed Signal Configuration (IMCR187)
32
RW
0000_0000h
D30h
Input Multiplexed Signal Configuration (IMCR188)
32
RW
0000_0000h
D34h
Input Multiplexed Signal Configuration (IMCR189)
32
RW
0000_0000h
D38h
Input Multiplexed Signal Configuration (IMCR190)
32
RW
0000_0000h
D3Ch
Input Multiplexed Signal Configuration (IMCR191)
32
RW
0000_0000h
D40h
Input Multiplexed Signal Configuration (IMCR192)
32
RW
0000_0000h
D44h
Input Multiplexed Signal Configuration (IMCR193)
32
RW
0000_0000h
D48h
Input Multiplexed Signal Configuration (IMCR194)
32
RW
0000_0000h
D4Ch
Input Multiplexed Signal Configuration (IMCR195)
32
RW
0000_0000h
D50h
Input Multiplexed Signal Configuration (IMCR196)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
324 / 5251


---
# 페이지 274

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
D54h
Input Multiplexed Signal Configuration (IMCR197)
32
RW
0000_0000h
D58h
Input Multiplexed Signal Configuration (IMCR198)
32
RW
0000_0000h
D5Ch
Input Multiplexed Signal Configuration (IMCR199)
32
RW
0000_0000h
D60h
Input Multiplexed Signal Configuration (IMCR200)
32
RW
0000_0000h
D64h
Input Multiplexed Signal Configuration (IMCR201)
32
RW
0000_0000h
D68h
Input Multiplexed Signal Configuration (IMCR202)
32
RW
0000_0000h
D8Ch
Input Multiplexed Signal Configuration (IMCR211)
32
RW
0000_0000h
D90h
Input Multiplexed Signal Configuration (IMCR212)
32
RW
0000_0000h
D94h
Input Multiplexed Signal Configuration (IMCR213)
32
RW
0000_0000h
D98h
Input Multiplexed Signal Configuration (IMCR214)
32
RW
0000_0000h
D9Ch
Input Multiplexed Signal Configuration (IMCR215)
32
RW
0000_0000h
DA0h
Input Multiplexed Signal Configuration (IMCR216)
32
RW
0000_0000h
DA4h
Input Multiplexed Signal Configuration (IMCR217)
32
RW
0000_0000h
DA8h
Input Multiplexed Signal Configuration (IMCR218)
32
RW
0000_0000h
DACh
Input Multiplexed Signal Configuration (IMCR219)
32
RW
0000_0000h
DB0h
Input Multiplexed Signal Configuration (IMCR220)
32
RW
0000_0000h
DB4h
Input Multiplexed Signal Configuration (IMCR221)
32
RW
0000_0000h
DB8h
Input Multiplexed Signal Configuration (IMCR222)
32
RW
0000_0000h
DBCh
Input Multiplexed Signal Configuration (IMCR223)
32
RW
0000_0000h
DC0h
Input Multiplexed Signal Configuration (IMCR224)
32
RW
0000_0000h
DC4h
Input Multiplexed Signal Configuration (IMCR225)
32
RW
0000_0000h
DC8h
Input Multiplexed Signal Configuration (IMCR226)
32
RW
0000_0000h
DCCh
Input Multiplexed Signal Configuration (IMCR227)
32
RW
0000_0000h
DD0h
Input Multiplexed Signal Configuration (IMCR228)
32
RW
0000_0000h
DD4h
Input Multiplexed Signal Configuration (IMCR229)
32
RW
0000_0000h
DD8h
Input Multiplexed Signal Configuration (IMCR230)
32
RW
0000_0000h
DDCh
Input Multiplexed Signal Configuration (IMCR231)
32
RW
0000_0000h
DE0h
Input Multiplexed Signal Configuration (IMCR232)
32
RW
0000_0000h
DE4h
Input Multiplexed Signal Configuration (IMCR233)
32
RW
0000_0000h
DE8h
Input Multiplexed Signal Configuration (IMCR234)
32
RW
0000_0000h
DECh
Input Multiplexed Signal Configuration (IMCR235)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
325 / 5251


---
# 페이지 275

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
DF0h
Input Multiplexed Signal Configuration (IMCR236)
32
RW
0000_0000h
DF4h
Input Multiplexed Signal Configuration (IMCR237)
32
RW
0000_0000h
DF8h
Input Multiplexed Signal Configuration (IMCR238)
32
RW
0000_0000h
DFCh
Input Multiplexed Signal Configuration (IMCR239)
32
RW
0000_0000h
E00h
Input Multiplexed Signal Configuration (IMCR240)
32
RW
0000_0000h
E04h
Input Multiplexed Signal Configuration (IMCR241)
32
RW
0000_0000h
E08h
Input Multiplexed Signal Configuration (IMCR242)
32
RW
0000_0000h
E0Ch
Input Multiplexed Signal Configuration (IMCR243)
32
RW
0000_0000h
E10h
Input Multiplexed Signal Configuration (IMCR244)
32
RW
0000_0000h
E14h
Input Multiplexed Signal Configuration (IMCR245)
32
RW
0000_0000h
E18h
Input Multiplexed Signal Configuration (IMCR246)
32
RW
0000_0000h
E1Ch
Input Multiplexed Signal Configuration (IMCR247)
32
RW
0000_0000h
E20h
Input Multiplexed Signal Configuration (IMCR248)
32
RW
0000_0000h
E24h
Input Multiplexed Signal Configuration (IMCR249)
32
RW
0000_0000h
E28h
Input Multiplexed Signal Configuration (IMCR250)
32
RW
0000_0000h
E2Ch
Input Multiplexed Signal Configuration (IMCR251)
32
RW
0000_0000h
E30h
Input Multiplexed Signal Configuration (IMCR252)
32
RW
0000_0000h
E34h
Input Multiplexed Signal Configuration (IMCR253)
32
RW
0000_0000h
E38h
Input Multiplexed Signal Configuration (IMCR254)
32
RW
0000_0000h
E3Ch
Input Multiplexed Signal Configuration (IMCR255)
32
RW
0000_0000h
E40h
Input Multiplexed Signal Configuration (IMCR256)
32
RW
0000_0000h
E44h
Input Multiplexed Signal Configuration (IMCR257)
32
RW
0000_0000h
E48h
Input Multiplexed Signal Configuration (IMCR258)
32
RW
0000_0000h
E4Ch
Input Multiplexed Signal Configuration (IMCR259)
32
RW
0000_0000h
E50h
Input Multiplexed Signal Configuration (IMCR260)
32
RW
0000_0000h
E54h
Input Multiplexed Signal Configuration (IMCR261)
32
RW
0000_0000h
E58h
Input Multiplexed Signal Configuration (IMCR262)
32
RW
0000_0000h
E5Ch
Input Multiplexed Signal Configuration (IMCR263)
32
RW
0000_0000h
E60h
Input Multiplexed Signal Configuration (IMCR264)
32
RW
0000_0000h
E64h
Input Multiplexed Signal Configuration (IMCR265)
32
RW
0000_0000h
E68h
Input Multiplexed Signal Configuration (IMCR266)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
326 / 5251


---
# 페이지 276

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
E6Ch
Input Multiplexed Signal Configuration (IMCR267)
32
RW
0000_0000h
E70h
Input Multiplexed Signal Configuration (IMCR268)
32
RW
0000_0000h
EC4h
Input Multiplexed Signal Configuration (IMCR289)
32
RW
0000_0000h
EC8h
Input Multiplexed Signal Configuration (IMCR290)
32
RW
0000_0000h
ECCh
Input Multiplexed Signal Configuration (IMCR291)
32
RW
0000_0000h
ED0h
Input Multiplexed Signal Configuration (IMCR292)
32
RW
0000_0000h
ED4h
Input Multiplexed Signal Configuration (IMCR293)
32
RW
0000_0000h
ED8h
Input Multiplexed Signal Configuration (IMCR294)
32
RW
0000_0000h
EDCh
Input Multiplexed Signal Configuration (IMCR295)
32
RW
0000_0000h
EE0h
Input Multiplexed Signal Configuration (IMCR296)
32
RW
0000_0000h
EE4h
Input Multiplexed Signal Configuration (IMCR297)
32
RW
0000_0000h
EE8h
Input Multiplexed Signal Configuration (IMCR298)
32
RW
0000_0000h
EECh
Input Multiplexed Signal Configuration (IMCR299)
32
RW
0000_0000h
EF0h
Input Multiplexed Signal Configuration (IMCR300)
32
RW
0000_0000h
EF4h
Input Multiplexed Signal Configuration (IMCR301)
32
RW
0000_0000h
EF8h
Input Multiplexed Signal Configuration (IMCR302)
32
RW
0000_0000h
EFCh
Input Multiplexed Signal Configuration (IMCR303)
32
RW
0000_0000h
F00h
Input Multiplexed Signal Configuration (IMCR304)
32
RW
0000_0000h
F04h
Input Multiplexed Signal Configuration (IMCR305)
32
RW
0000_0000h
F08h
Input Multiplexed Signal Configuration (IMCR306)
32
RW
0000_0000h
F0Ch
Input Multiplexed Signal Configuration (IMCR307)
32
RW
0000_0000h
F10h
Input Multiplexed Signal Configuration (IMCR308)
32
RW
0000_0000h
F14h
Input Multiplexed Signal Configuration (IMCR309)
32
RW
0000_0000h
F2Ch
Input Multiplexed Signal Configuration (IMCR315)
32
RW
0000_0000h
F30h
Input Multiplexed Signal Configuration (IMCR316)
32
RW
0000_0000h
F34h
Input Multiplexed Signal Configuration (IMCR317)
32
RW
0000_0000h
F38h
Input Multiplexed Signal Configuration (IMCR318)
32
RW
0000_0000h
F3Ch
Input Multiplexed Signal Configuration (IMCR319)
32
RW
0000_0000h
F40h
Input Multiplexed Signal Configuration (IMCR320)
32
RW
0000_0000h
F44h
Input Multiplexed Signal Configuration (IMCR321)
32
RW
0000_0000h
F48h
Input Multiplexed Signal Configuration (IMCR322)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
327 / 5251


---
# 페이지 277

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
F4Ch
Input Multiplexed Signal Configuration (IMCR323)
32
RW
0000_0000h
F50h
Input Multiplexed Signal Configuration (IMCR324)
32
RW
0000_0000h
F54h
Input Multiplexed Signal Configuration (IMCR325)
32
RW
0000_0000h
F9Ch
Input Multiplexed Signal Configuration (IMCR343)
32
RW
0000_0000h
FA0h
Input Multiplexed Signal Configuration (IMCR344)
32
RW
0000_0000h
FA4h
Input Multiplexed Signal Configuration (IMCR345)
32
RW
0000_0000h
FA8h
Input Multiplexed Signal Configuration (IMCR346)
32
RW
0000_0000h
FACh
Input Multiplexed Signal Configuration (IMCR347)
32
RW
0000_0000h
FB0h
Input Multiplexed Signal Configuration (IMCR348)
32
RW
0000_0000h
FB4h
Input Multiplexed Signal Configuration (IMCR349)
32
RW
0000_0000h
FB8h
Input Multiplexed Signal Configuration (IMCR350)
32
RW
0000_0000h
FBCh
Input Multiplexed Signal Configuration (IMCR351)
32
RW
0000_0000h
FC0h
Input Multiplexed Signal Configuration (IMCR352)
32
RW
0000_0000h
FC4h
Input Multiplexed Signal Configuration (IMCR353)
32
RW
0000_0000h
FC8h
Input Multiplexed Signal Configuration (IMCR354)
32
RW
0000_0000h
FCCh
Input Multiplexed Signal Configuration (IMCR355)
32
RW
0000_0000h
FD0h
Input Multiplexed Signal Configuration (IMCR356)
32
RW
0000_0000h
FD4h
Input Multiplexed Signal Configuration (IMCR357)
32
RW
0000_0000h
FD8h
Input Multiplexed Signal Configuration (IMCR358)
32
RW
0000_0000h
FDCh
Input Multiplexed Signal Configuration (IMCR359)
32
RW
0000_0000h
FE0h
Input Multiplexed Signal Configuration (IMCR360)
32
RW
0000_0000h
FE4h
Input Multiplexed Signal Configuration (IMCR361)
32
RW
0000_0000h
FE8h
Input Multiplexed Signal Configuration (IMCR362)
32
RW
0000_0000h
FECh
Input Multiplexed Signal Configuration (IMCR363)
32
RW
0000_0000h
FF0h
Input Multiplexed Signal Configuration (IMCR364)
32
RW
0000_0000h
FF4h
Input Multiplexed Signal Configuration (IMCR365)
32
RW
0000_0000h
FF8h
Input Multiplexed Signal Configuration (IMCR366)
32
RW
0000_0000h
FFCh
Input Multiplexed Signal Configuration (IMCR367)
32
RW
0000_0000h
1000h
Input Multiplexed Signal Configuration (IMCR368)
32
RW
0000_0000h
1004h
Input Multiplexed Signal Configuration (IMCR369)
32
RW
0000_0000h
1008h
Input Multiplexed Signal Configuration (IMCR370)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
328 / 5251


---
# 페이지 278

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1014h
Input Multiplexed Signal Configuration (IMCR373)
32
RW
0000_0000h
1018h
Input Multiplexed Signal Configuration (IMCR374)
32
RW
0000_0000h
101Ch
Input Multiplexed Signal Configuration (IMCR375)
32
RW
0000_0000h
1020h
Input Multiplexed Signal Configuration (IMCR376)
32
RW
0000_0000h
1024h
Input Multiplexed Signal Configuration (IMCR377)
32
RW
0000_0000h
1028h
Input Multiplexed Signal Configuration (IMCR378)
32
RW
0000_0000h
1054h
Input Multiplexed Signal Configuration (IMCR389)
32
RW
0000_0000h
1078h
Input Multiplexed Signal Configuration (IMCR398)
32
RW
0000_0000h
107Ch
Input Multiplexed Signal Configuration (IMCR399)
32
RW
0000_0000h
10A4h
Input Multiplexed Signal Configuration (IMCR409)
32
RW
0000_0000h
10A8h
Input Multiplexed Signal Configuration (IMCR410)
32
RW
0000_0000h
10ACh
Input Multiplexed Signal Configuration (IMCR411)
32
RW
0000_0000h
10B0h
Input Multiplexed Signal Configuration (IMCR412)
32
RW
0000_0000h
10B4h
Input Multiplexed Signal Configuration (IMCR413)
32
RW
0000_0000h
10B8h
Input Multiplexed Signal Configuration (IMCR414)
32
RW
0000_0000h
10BCh
Input Multiplexed Signal Configuration (IMCR415)
32
RW
0000_0000h
10C0h
Input Multiplexed Signal Configuration (IMCR416)
32
RW
0000_0000h
10C4h
Input Multiplexed Signal Configuration (IMCR417)
32
RW
0000_0000h
10C8h
Input Multiplexed Signal Configuration (IMCR418)
32
RW
0000_0000h
1120h
Input Multiplexed Signal Configuration (IMCR440)
32
RW
0000_0000h
1140h
Input Multiplexed Signal Configuration (IMCR448)
32
RW
0000_0000h
1144h
Input Multiplexed Signal Configuration (IMCR449)
32
RW
0000_0000h
1148h
Input Multiplexed Signal Configuration (IMCR450)
32
RW
0000_0000h
114Ch
Input Multiplexed Signal Configuration (IMCR451)
32
RW
0000_0000h
1150h
Input Multiplexed Signal Configuration (IMCR452)
32
RW
0000_0000h
1154h
Input Multiplexed Signal Configuration (IMCR453)
32
RW
0000_0000h
1158h
Input Multiplexed Signal Configuration (IMCR454)
32
RW
0000_0000h
115Ch
Input Multiplexed Signal Configuration (IMCR455)
32
RW
0000_0000h
1160h
Input Multiplexed Signal Configuration (IMCR456)
32
RW
0000_0000h
1164h
Input Multiplexed Signal Configuration (IMCR457)
32
RW
0000_0000h
1168h
Input Multiplexed Signal Configuration (IMCR458)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
329 / 5251


---
# 페이지 279

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
116Ch
Input Multiplexed Signal Configuration (IMCR459)
32
RW
0000_0000h
1170h
Input Multiplexed Signal Configuration (IMCR460)
32
RW
0000_0000h
1174h
Input Multiplexed Signal Configuration (IMCR461)
32
RW
0000_0000h
1178h
Input Multiplexed Signal Configuration (IMCR462)
32
RW
0000_0000h
117Ch
Input Multiplexed Signal Configuration (IMCR463)
32
RW
0000_0000h
1180h
Input Multiplexed Signal Configuration (IMCR464)
32
RW
0000_0000h
1184h
Input Multiplexed Signal Configuration (IMCR465)
32
RW
0000_0000h
1188h
Input Multiplexed Signal Configuration (IMCR466)
32
RW
0000_0000h
118Ch
Input Multiplexed Signal Configuration (IMCR467)
32
RW
0000_0000h
1190h
Input Multiplexed Signal Configuration (IMCR468)
32
RW
0000_0000h
1194h
Input Multiplexed Signal Configuration (IMCR469)
32
RW
0000_0000h
1198h
Input Multiplexed Signal Configuration (IMCR470)
32
RW
0000_0000h
119Ch
Input Multiplexed Signal Configuration (IMCR471)
32
RW
0000_0000h
11A0h
Input Multiplexed Signal Configuration (IMCR472)
32
RW
0000_0000h
11A4h
Input Multiplexed Signal Configuration (IMCR473)
32
RW
0000_0000h
1300h
GPIO Pad Data Output (GPDO3)
8
RW
00h
1301h
GPIO Pad Data Output (GPDO2)
8
RW
00h
1302h
GPIO Pad Data Output (GPDO1)
8
RW
00h
1303h
GPIO Pad Data Output (GPDO0)
8
RW
00h
1304h
GPIO Pad Data Output (GPDO7)
8
RW
00h
1305h
GPIO Pad Data Output (GPDO6)
8
RW
00h
1306h
GPIO Pad Data Output (GPDO5)
8
RW
00h
1307h
GPIO Pad Data Output (GPDO4)
8
RW
00h
1308h
GPIO Pad Data Output (GPDO11)
8
RW
00h
1309h
GPIO Pad Data Output (GPDO10)
8
RW
00h
130Ah
GPIO Pad Data Output (GPDO9)
8
RW
00h
130Bh
GPIO Pad Data Output (GPDO8)
8
RW
00h
130Ch
GPIO Pad Data Output (GPDO15)
8
RW
00h
130Dh
GPIO Pad Data Output (GPDO14)
8
RW
00h
130Eh
GPIO Pad Data Output (GPDO13)
8
RW
00h
130Fh
GPIO Pad Data Output (GPDO12)
8
RW
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
330 / 5251


---
# 페이지 280

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1310h
GPIO Pad Data Output (GPDO19)
8
RW
00h
1311h
GPIO Pad Data Output (GPDO18)
8
RW
00h
1312h
GPIO Pad Data Output (GPDO17)
8
RW
00h
1313h
GPIO Pad Data Output (GPDO16)
8
RW
00h
1314h
GPIO Pad Data Output (GPDO23)
8
RW
00h
1315h
GPIO Pad Data Output (GPDO22)
8
RW
00h
1316h
GPIO Pad Data Output (GPDO21)
8
RW
00h
1317h
GPIO Pad Data Output (GPDO20)
8
RW
00h
1318h
GPIO Pad Data Output (GPDO27)
8
RW
00h
1319h
GPIO Pad Data Output (GPDO26)
8
RW
00h
131Ah
GPIO Pad Data Output (GPDO25)
8
RW
00h
131Bh
GPIO Pad Data Output (GPDO24)
8
RW
00h
131Ch
GPIO Pad Data Output (GPDO31)
8
RW
00h
131Dh
GPIO Pad Data Output (GPDO30)
8
RW
00h
131Eh
GPIO Pad Data Output (GPDO29)
8
RW
00h
131Fh
GPIO Pad Data Output (GPDO28)
8
RW
00h
1320h
GPIO Pad Data Output (GPDO35)
8
RW
00h
1321h
GPIO Pad Data Output (GPDO34)
8
RW
00h
1322h
GPIO Pad Data Output (GPDO33)
8
RW
00h
1323h
GPIO Pad Data Output (GPDO32)
8
RW
00h
1326h
GPIO Pad Data Output (GPDO37)
8
RW
00h
1327h
GPIO Pad Data Output (GPDO36)
8
RW
00h
1328h
GPIO Pad Data Output (GPDO43)
8
RW
00h
1329h
GPIO Pad Data Output (GPDO42)
8
RW
00h
132Ah
GPIO Pad Data Output (GPDO41)
8
RW
00h
132Bh
GPIO Pad Data Output (GPDO40)
8
RW
00h
132Ch
GPIO Pad Data Output (GPDO47)
8
RW
00h
132Dh
GPIO Pad Data Output (GPDO46)
8
RW
00h
132Eh
GPIO Pad Data Output (GPDO45)
8
RW
00h
132Fh
GPIO Pad Data Output (GPDO44)
8
RW
00h
1330h
GPIO Pad Data Output (GPDO51)
8
RW
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
331 / 5251


---
# 페이지 281

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1331h
GPIO Pad Data Output (GPDO50)
8
RW
00h
1332h
GPIO Pad Data Output (GPDO49)
8
RW
00h
1333h
GPIO Pad Data Output (GPDO48)
8
RW
00h
1334h
GPIO Pad Data Output (GPDO55)
8
RW
00h
1335h
GPIO Pad Data Output (GPDO54)
8
RW
00h
1336h
GPIO Pad Data Output (GPDO53)
8
RW
00h
1337h
GPIO Pad Data Output (GPDO52)
8
RW
00h
1338h
GPIO Pad Data Output (GPDO59)
8
RW
00h
1339h
GPIO Pad Data Output (GPDO58)
8
RW
00h
133Ah
GPIO Pad Data Output (GPDO57)
8
RW
00h
133Bh
GPIO Pad Data Output (GPDO56)
8
RW
00h
133Ch
GPIO Pad Data Output (GPDO63)
8
RW
00h
133Dh
GPIO Pad Data Output (GPDO62)
8
RW
00h
133Eh
GPIO Pad Data Output (GPDO61)
8
RW
00h
133Fh
GPIO Pad Data Output (GPDO60)
8
RW
00h
1340h
GPIO Pad Data Output (GPDO67)
8
RW
00h
1341h
GPIO Pad Data Output (GPDO66)
8
RW
00h
1342h
GPIO Pad Data Output (GPDO65)
8
RW
00h
1343h
GPIO Pad Data Output (GPDO64)
8
RW
00h
1344h
GPIO Pad Data Output (GPDO71)
8
RW
00h
1345h
GPIO Pad Data Output (GPDO70)
8
RW
00h
1346h
GPIO Pad Data Output (GPDO69)
8
RW
00h
1347h
GPIO Pad Data Output (GPDO68)
8
RW
00h
1348h
GPIO Pad Data Output (GPDO75)
8
RW
00h
1349h
GPIO Pad Data Output (GPDO74)
8
RW
00h
134Ah
GPIO Pad Data Output (GPDO73)
8
RW
00h
134Bh
GPIO Pad Data Output (GPDO72)
8
RW
00h
134Ch
GPIO Pad Data Output (GPDO79)
8
RW
00h
134Dh
GPIO Pad Data Output (GPDO78)
8
RW
00h
134Eh
GPIO Pad Data Output (GPDO77)
8
RW
00h
134Fh
GPIO Pad Data Output (GPDO76)
8
RW
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
332 / 5251


---
# 페이지 282

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1350h
GPIO Pad Data Output (GPDO83)
8
RW
00h
1351h
GPIO Pad Data Output (GPDO82)
8
RW
00h
1352h
GPIO Pad Data Output (GPDO81)
8
RW
00h
1353h
GPIO Pad Data Output (GPDO80)
8
RW
00h
1354h
GPIO Pad Data Output (GPDO87)
8
RW
00h
1355h
GPIO Pad Data Output (GPDO86)
8
RW
00h
1356h
GPIO Pad Data Output (GPDO85)
8
RW
00h
1357h
GPIO Pad Data Output (GPDO84)
8
RW
00h
1358h
GPIO Pad Data Output (GPDO91)
8
RW
00h
1359h
GPIO Pad Data Output (GPDO90)
8
RW
00h
135Ah
GPIO Pad Data Output (GPDO89)
8
RW
00h
135Bh
GPIO Pad Data Output (GPDO88)
8
RW
00h
135Ch
GPIO Pad Data Output (GPDO95)
8
RW
00h
135Dh
GPIO Pad Data Output (GPDO94)
8
RW
00h
135Eh
GPIO Pad Data Output (GPDO93)
8
RW
00h
135Fh
GPIO Pad Data Output (GPDO92)
8
RW
00h
1360h
GPIO Pad Data Output (GPDO99)
8
RW
00h
1361h
GPIO Pad Data Output (GPDO98)
8
RW
00h
1362h
GPIO Pad Data Output (GPDO97)
8
RW
00h
1363h
GPIO Pad Data Output (GPDO96)
8
RW
00h
1364h
GPIO Pad Data Output (GPDO103)
8
RW
00h
1365h
GPIO Pad Data Output (GPDO102)
8
RW
00h
1366h
GPIO Pad Data Output (GPDO101)
8
RW
00h
1367h
GPIO Pad Data Output (GPDO100)
8
RW
00h
1368h
GPIO Pad Data Output (GPDO107)
8
RW
00h
1369h
GPIO Pad Data Output (GPDO106)
8
RW
00h
136Ah
GPIO Pad Data Output (GPDO105)
8
RW
00h
136Bh
GPIO Pad Data Output (GPDO104)
8
RW
00h
136Ch
GPIO Pad Data Output (GPDO111)
8
RW
00h
136Dh
GPIO Pad Data Output (GPDO110)
8
RW
00h
136Eh
GPIO Pad Data Output (GPDO109)
8
RW
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
333 / 5251


---
# 페이지 283

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
136Fh
GPIO Pad Data Output (GPDO108)
8
RW
00h
1370h
GPIO Pad Data Output (GPDO115)
8
RW
00h
1371h
GPIO Pad Data Output (GPDO114)
8
RW
00h
1372h
GPIO Pad Data Output (GPDO113)
8
RW
00h
1373h
GPIO Pad Data Output (GPDO112)
8
RW
00h
1374h
GPIO Pad Data Output (GPDO119)
8
RW
00h
1375h
GPIO Pad Data Output (GPDO118)
8
RW
00h
1376h
GPIO Pad Data Output (GPDO117)
8
RW
00h
1377h
GPIO Pad Data Output (GPDO116)
8
RW
00h
1378h
GPIO Pad Data Output (GPDO123)
8
RW
00h
1379h
GPIO Pad Data Output (GPDO122)
8
RW
00h
137Ah
GPIO Pad Data Output (GPDO121)
8
RW
00h
137Bh
GPIO Pad Data Output (GPDO120)
8
RW
00h
137Ch
GPIO Pad Data Output (GPDO127)
8
RW
00h
137Dh
GPIO Pad Data Output (GPDO126)
8
RW
00h
137Eh
GPIO Pad Data Output (GPDO125)
8
RW
00h
137Fh
GPIO Pad Data Output (GPDO124)
8
RW
00h
1380h
GPIO Pad Data Output (GPDO131)
8
RW
00h
1381h
GPIO Pad Data Output (GPDO130)
8
RW
00h
1382h
GPIO Pad Data Output (GPDO129)
8
RW
00h
1383h
GPIO Pad Data Output (GPDO128)
8
RW
00h
1384h
GPIO Pad Data Output (GPDO135)
8
RW
00h
1385h
GPIO Pad Data Output (GPDO134)
8
RW
00h
1386h
GPIO Pad Data Output (GPDO133)
8
RW
00h
1387h
GPIO Pad Data Output (GPDO132)
8
RW
00h
1388h
GPIO Pad Data Output (GPDO139)
8
RW
00h
1389h
GPIO Pad Data Output (GPDO138)
8
RW
00h
138Ah
GPIO Pad Data Output (GPDO137)
8
RW
00h
138Bh
GPIO Pad Data Output (GPDO136)
8
RW
00h
138Ch
GPIO Pad Data Output (GPDO143)
8
RW
00h
138Dh
GPIO Pad Data Output (GPDO142)
8
RW
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
334 / 5251


---
# 페이지 284

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
138Fh
GPIO Pad Data Output (GPDO140)
8
RW
00h
1390h
GPIO Pad Data Output (GPDO147)
8
RW
00h
1391h
GPIO Pad Data Output (GPDO146)
8
RW
00h
1392h
GPIO Pad Data Output (GPDO145)
8
RW
00h
1393h
GPIO Pad Data Output (GPDO144)
8
RW
00h
1394h
GPIO Pad Data Output (GPDO151)
8
RW
00h
1395h
GPIO Pad Data Output (GPDO150)
8
RW
00h
1396h
GPIO Pad Data Output (GPDO149)
8
RW
00h
1397h
GPIO Pad Data Output (GPDO148)
8
RW
00h
1398h
GPIO Pad Data Output (GPDO155)
8
RW
00h
1399h
GPIO Pad Data Output (GPDO154)
8
RW
00h
139Ah
GPIO Pad Data Output (GPDO153)
8
RW
00h
139Bh
GPIO Pad Data Output (GPDO152)
8
RW
00h
139Ch
GPIO Pad Data Output (GPDO159)
8
RW
00h
139Dh
GPIO Pad Data Output (GPDO158)
8
RW
00h
139Eh
GPIO Pad Data Output (GPDO157)
8
RW
00h
139Fh
GPIO Pad Data Output (GPDO156)
8
RW
00h
13A0h
GPIO Pad Data Output (GPDO163)
8
RW
00h
13A1h
GPIO Pad Data Output (GPDO162)
8
RW
00h
13A2h
GPIO Pad Data Output (GPDO161)
8
RW
00h
13A3h
GPIO Pad Data Output (GPDO160)
8
RW
00h
13A4h
GPIO Pad Data Output (GPDO167)
8
RW
00h
13A5h
GPIO Pad Data Output (GPDO166)
8
RW
00h
13A6h
GPIO Pad Data Output (GPDO165)
8
RW
00h
13A7h
GPIO Pad Data Output (GPDO164)
8
RW
00h
13A8h
GPIO Pad Data Output (GPDO171)
8
RW
00h
13A9h
GPIO Pad Data Output (GPDO170)
8
RW
00h
13AAh
GPIO Pad Data Output (GPDO169)
8
RW
00h
13ABh
GPIO Pad Data Output (GPDO168)
8
RW
00h
13ACh
GPIO Pad Data Output (GPDO175)
8
RW
00h
13ADh
GPIO Pad Data Output (GPDO174)
8
RW
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
335 / 5251


---
# 페이지 285

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
13AEh
GPIO Pad Data Output (GPDO173)
8
RW
00h
13AFh
GPIO Pad Data Output (GPDO172)
8
RW
00h
13B0h
GPIO Pad Data Output (GPDO179)
8
RW
00h
13B1h
GPIO Pad Data Output (GPDO178)
8
RW
00h
13B2h
GPIO Pad Data Output (GPDO177)
8
RW
00h
13B3h
GPIO Pad Data Output (GPDO176)
8
RW
00h
13B4h
GPIO Pad Data Output (GPDO183)
8
RW
00h
13B5h
GPIO Pad Data Output (GPDO182)
8
RW
00h
13B6h
GPIO Pad Data Output (GPDO181)
8
RW
00h
13B7h
GPIO Pad Data Output (GPDO180)
8
RW
00h
13B8h
GPIO Pad Data Output (GPDO187)
8
RW
00h
13B9h
GPIO Pad Data Output (GPDO186)
8
RW
00h
13BAh
GPIO Pad Data Output (GPDO185)
8
RW
00h
13BBh
GPIO Pad Data Output (GPDO184)
8
RW
00h
13BCh
GPIO Pad Data Output (GPDO191)
8
RW
00h
13BDh
GPIO Pad Data Output (GPDO190)
8
RW
00h
13BEh
GPIO Pad Data Output (GPDO189)
8
RW
00h
13BFh
GPIO Pad Data Output (GPDO188)
8
RW
00h
13C0h
GPIO Pad Data Output (GPDO195)
8
RW
00h
13C1h
GPIO Pad Data Output (GPDO194)
8
RW
00h
13C2h
GPIO Pad Data Output (GPDO193)
8
RW
00h
13C3h
GPIO Pad Data Output (GPDO192)
8
RW
00h
13C4h
GPIO Pad Data Output (GPDO199)
8
RW
00h
13C5h
GPIO Pad Data Output (GPDO198)
8
RW
00h
13C6h
GPIO Pad Data Output (GPDO197)
8
RW
00h
13C7h
GPIO Pad Data Output (GPDO196)
8
RW
00h
13C8h
GPIO Pad Data Output (GPDO203)
8
RW
00h
13C9h
GPIO Pad Data Output (GPDO202)
8
RW
00h
13CAh
GPIO Pad Data Output (GPDO201)
8
RW
00h
13CBh
GPIO Pad Data Output (GPDO200)
8
RW
00h
13CCh
GPIO Pad Data Output (GPDO207)
8
RW
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
336 / 5251


---
# 페이지 286

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
13CDh
GPIO Pad Data Output (GPDO206)
8
RW
00h
13CEh
GPIO Pad Data Output (GPDO205)
8
RW
00h
13CFh
GPIO Pad Data Output (GPDO204)
8
RW
00h
13D0h
GPIO Pad Data Output (GPDO211)
8
RW
00h
13D1h
GPIO Pad Data Output (GPDO210)
8
RW
00h
13D2h
GPIO Pad Data Output (GPDO209)
8
RW
00h
13D3h
GPIO Pad Data Output (GPDO208)
8
RW
00h
13D4h
GPIO Pad Data Output (GPDO215)
8
RW
00h
13D5h
GPIO Pad Data Output (GPDO214)
8
RW
00h
13D6h
GPIO Pad Data Output (GPDO213)
8
RW
00h
13D7h
GPIO Pad Data Output (GPDO212)
8
RW
00h
13D8h
GPIO Pad Data Output (GPDO219)
8
RW
00h
13D9h
GPIO Pad Data Output (GPDO218)
8
RW
00h
13DAh
GPIO Pad Data Output (GPDO217)
8
RW
00h
13DBh
GPIO Pad Data Output (GPDO216)
8
RW
00h
13DCh
GPIO Pad Data Output (GPDO223)
8
RW
00h
13DDh
GPIO Pad Data Output (GPDO222)
8
RW
00h
13DEh
GPIO Pad Data Output (GPDO221)
8
RW
00h
13DFh
GPIO Pad Data Output (GPDO220)
8
RW
00h
13E0h
GPIO Pad Data Output (GPDO227)
8
RW
00h
13E1h
GPIO Pad Data Output (GPDO226)
8
RW
00h
13E2h
GPIO Pad Data Output (GPDO225)
8
RW
00h
13E3h
GPIO Pad Data Output (GPDO224)
8
RW
00h
13E4h
GPIO Pad Data Output (GPDO231)
8
RW
00h
13E5h
GPIO Pad Data Output (GPDO230)
8
RW
00h
13E6h
GPIO Pad Data Output (GPDO229)
8
RW
00h
13E7h
GPIO Pad Data Output (GPDO228)
8
RW
00h
13E8h
GPIO Pad Data Output (GPDO235)
8
RW
00h
13E9h
GPIO Pad Data Output (GPDO234)
8
RW
00h
13EAh
GPIO Pad Data Output (GPDO233)
8
RW
00h
13EBh
GPIO Pad Data Output (GPDO232)
8
RW
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
337 / 5251


---
# 페이지 287

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
13ECh
GPIO Pad Data Output (GPDO239)
8
RW
00h
13EDh
GPIO Pad Data Output (GPDO238)
8
RW
00h
13EEh
GPIO Pad Data Output (GPDO237)
8
RW
00h
13EFh
GPIO Pad Data Output (GPDO236)
8
RW
00h
13F0h
GPIO Pad Data Output (GPDO243)
8
RW
00h
13F1h
GPIO Pad Data Output (GPDO242)
8
RW
00h
13F2h
GPIO Pad Data Output (GPDO241)
8
RW
00h
13F3h
GPIO Pad Data Output (GPDO240)
8
RW
00h
13F4h
GPIO Pad Data Output (GPDO247)
8
RW
00h
13F5h
GPIO Pad Data Output (GPDO246)
8
RW
00h
13F6h
GPIO Pad Data Output (GPDO245)
8
RW
00h
13F7h
GPIO Pad Data Output (GPDO244)
8
RW
00h
13F8h
GPIO Pad Data Output (GPDO251)
8
RW
00h
13F9h
GPIO Pad Data Output (GPDO250)
8
RW
00h
13FAh
GPIO Pad Data Output (GPDO249)
8
RW
00h
13FBh
GPIO Pad Data Output (GPDO248)
8
RW
00h
13FCh
GPIO Pad Data Output (GPDO255)
8
RW
00h
13FDh
GPIO Pad Data Output (GPDO254)
8
RW
00h
13FEh
GPIO Pad Data Output (GPDO253)
8
RW
00h
13FFh
GPIO Pad Data Output (GPDO252)
8
RW
00h
1400h
GPIO Pad Data Output (GPDO259)
8
RW
00h
1401h
GPIO Pad Data Output (GPDO258)
8
RW
00h
1402h
GPIO Pad Data Output (GPDO257)
8
RW
00h
1403h
GPIO Pad Data Output (GPDO256)
8
RW
00h
1404h
GPIO Pad Data Output (GPDO263)
8
RW
00h
1405h
GPIO Pad Data Output (GPDO262)
8
RW
00h
1406h
GPIO Pad Data Output (GPDO261)
8
RW
00h
1407h
GPIO Pad Data Output (GPDO260)
8
RW
00h
1408h
GPIO Pad Data Output (GPDO267)
8
RW
00h
1409h
GPIO Pad Data Output (GPDO266)
8
RW
00h
140Ah
GPIO Pad Data Output (GPDO265)
8
RW
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
338 / 5251


---
# 페이지 288

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
140Bh
GPIO Pad Data Output (GPDO264)
8
RW
00h
140Ch
GPIO Pad Data Output (GPDO271)
8
RW
00h
140Dh
GPIO Pad Data Output (GPDO270)
8
RW
00h
140Eh
GPIO Pad Data Output (GPDO269)
8
RW
00h
140Fh
GPIO Pad Data Output (GPDO268)
8
RW
00h
1410h
GPIO Pad Data Output (GPDO275)
8
RW
00h
1411h
GPIO Pad Data Output (GPDO274)
8
RW
00h
1412h
GPIO Pad Data Output (GPDO273)
8
RW
00h
1413h
GPIO Pad Data Output (GPDO272)
8
RW
00h
1414h
GPIO Pad Data Output (GPDO279)
8
RW
00h
1415h
GPIO Pad Data Output (GPDO278)
8
RW
00h
1416h
GPIO Pad Data Output (GPDO277)
8
RW
00h
1417h
GPIO Pad Data Output (GPDO276)
8
RW
00h
1418h
GPIO Pad Data Output (GPDO283)
8
RW
00h
1419h
GPIO Pad Data Output (GPDO282)
8
RW
00h
141Ah
GPIO Pad Data Output (GPDO281)
8
RW
00h
141Bh
GPIO Pad Data Output (GPDO280)
8
RW
00h
141Ch
GPIO Pad Data Output (GPDO287)
8
RW
00h
141Dh
GPIO Pad Data Output (GPDO286)
8
RW
00h
141Eh
GPIO Pad Data Output (GPDO285)
8
RW
00h
141Fh
GPIO Pad Data Output (GPDO284)
8
RW
00h
1420h
GPIO Pad Data Output (GPDO291)
8
RW
00h
1421h
GPIO Pad Data Output (GPDO290)
8
RW
00h
1422h
GPIO Pad Data Output (GPDO289)
8
RW
00h
1423h
GPIO Pad Data Output (GPDO288)
8
RW
00h
1424h
GPIO Pad Data Output (GPDO295)
8
RW
00h
1425h
GPIO Pad Data Output (GPDO294)
8
RW
00h
1426h
GPIO Pad Data Output (GPDO293)
8
RW
00h
1427h
GPIO Pad Data Output (GPDO292)
8
RW
00h
1428h
GPIO Pad Data Output (GPDO299)
8
RW
00h
1429h
GPIO Pad Data Output (GPDO298)
8
RW
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
339 / 5251


---
# 페이지 289

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
142Ah
GPIO Pad Data Output (GPDO297)
8
RW
00h
142Bh
GPIO Pad Data Output (GPDO296)
8
RW
00h
142Ch
GPIO Pad Data Output (GPDO303)
8
RW
00h
142Dh
GPIO Pad Data Output (GPDO302)
8
RW
00h
142Eh
GPIO Pad Data Output (GPDO301)
8
RW
00h
142Fh
GPIO Pad Data Output (GPDO300)
8
RW
00h
1430h
GPIO Pad Data Output (GPDO307)
8
RW
00h
1431h
GPIO Pad Data Output (GPDO306)
8
RW
00h
1432h
GPIO Pad Data Output (GPDO305)
8
RW
00h
1433h
GPIO Pad Data Output (GPDO304)
8
RW
00h
1434h
GPIO Pad Data Output (GPDO311)
8
RW
00h
1435h
GPIO Pad Data Output (GPDO310)
8
RW
00h
1436h
GPIO Pad Data Output (GPDO309)
8
RW
00h
1437h
GPIO Pad Data Output (GPDO308)
8
RW
00h
1438h
GPIO Pad Data Output (GPDO315)
8
RW
00h
1439h
GPIO Pad Data Output (GPDO314)
8
RW
00h
143Ah
GPIO Pad Data Output (GPDO313)
8
RW
00h
143Bh
GPIO Pad Data Output (GPDO312)
8
RW
00h
143Ch
GPIO Pad Data Output (GPDO319)
8
RW
00h
143Dh
GPIO Pad Data Output (GPDO318)
8
RW
00h
143Eh
GPIO Pad Data Output (GPDO317)
8
RW
00h
143Fh
GPIO Pad Data Output (GPDO316)
8
RW
00h
1440h
GPIO Pad Data Output (GPDO323)
8
RW
00h
1441h
GPIO Pad Data Output (GPDO322)
8
RW
00h
1442h
GPIO Pad Data Output (GPDO321)
8
RW
00h
1443h
GPIO Pad Data Output (GPDO320)
8
RW
00h
1500h
GPIO Pad Data Input (GPDI3)
8
R
00h
1501h
GPIO Pad Data Input (GPDI2)
8
R
00h
1502h
GPIO Pad Data Input (GPDI1)
8
R
00h
1503h
GPIO Pad Data Input (GPDI0)
8
R
00h
1504h
GPIO Pad Data Input (GPDI7)
8
R
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
340 / 5251


---
# 페이지 290

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1505h
GPIO Pad Data Input (GPDI6)
8
R
00h
1506h
GPIO Pad Data Input (GPDI5)
8
R
00h
1507h
GPIO Pad Data Input (GPDI4)
8
R
00h
1508h
GPIO Pad Data Input (GPDI11)
8
R
00h
1509h
GPIO Pad Data Input (GPDI10)
8
R
00h
150Ah
GPIO Pad Data Input (GPDI9)
8
R
00h
150Bh
GPIO Pad Data Input (GPDI8)
8
R
00h
150Ch
GPIO Pad Data Input (GPDI15)
8
R
00h
150Dh
GPIO Pad Data Input (GPDI14)
8
R
00h
150Eh
GPIO Pad Data Input (GPDI13)
8
R
00h
150Fh
GPIO Pad Data Input (GPDI12)
8
R
00h
1510h
GPIO Pad Data Input (GPDI19)
8
R
00h
1511h
GPIO Pad Data Input (GPDI18)
8
R
00h
1512h
GPIO Pad Data Input (GPDI17)
8
R
00h
1513h
GPIO Pad Data Input (GPDI16)
8
R
00h
1514h
GPIO Pad Data Input (GPDI23)
8
R
00h
1515h
GPIO Pad Data Input (GPDI22)
8
R
00h
1516h
GPIO Pad Data Input (GPDI21)
8
R
00h
1517h
GPIO Pad Data Input (GPDI20)
8
R
00h
1518h
GPIO Pad Data Input (GPDI27)
8
R
00h
1519h
GPIO Pad Data Input (GPDI26)
8
R
00h
151Ah
GPIO Pad Data Input (GPDI25)
8
R
00h
151Bh
GPIO Pad Data Input (GPDI24)
8
R
00h
151Ch
GPIO Pad Data Input (GPDI31)
8
R
00h
151Dh
GPIO Pad Data Input (GPDI30)
8
R
00h
151Eh
GPIO Pad Data Input (GPDI29)
8
R
00h
151Fh
GPIO Pad Data Input (GPDI28)
8
R
00h
1520h
GPIO Pad Data Input (GPDI35)
8
R
00h
1521h
GPIO Pad Data Input (GPDI34)
8
R
00h
1522h
GPIO Pad Data Input (GPDI33)
8
R
00h
1523h
GPIO Pad Data Input (GPDI32)
8
R
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
341 / 5251


---
# 페이지 291

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1526h
GPIO Pad Data Input (GPDI37)
8
R
00h
1527h
GPIO Pad Data Input (GPDI36)
8
R
00h
1528h
GPIO Pad Data Input (GPDI43)
8
R
00h
1529h
GPIO Pad Data Input (GPDI42)
8
R
00h
152Ah
GPIO Pad Data Input (GPDI41)
8
R
00h
152Bh
GPIO Pad Data Input (GPDI40)
8
R
00h
152Ch
GPIO Pad Data Input (GPDI47)
8
R
00h
152Dh
GPIO Pad Data Input (GPDI46)
8
R
00h
152Eh
GPIO Pad Data Input (GPDI45)
8
R
00h
152Fh
GPIO Pad Data Input (GPDI44)
8
R
00h
1530h
GPIO Pad Data Input (GPDI51)
8
R
00h
1531h
GPIO Pad Data Input (GPDI50)
8
R
00h
1532h
GPIO Pad Data Input (GPDI49)
8
R
00h
1533h
GPIO Pad Data Input (GPDI48)
8
R
00h
1534h
GPIO Pad Data Input (GPDI55)
8
R
00h
1535h
GPIO Pad Data Input (GPDI54)
8
R
00h
1536h
GPIO Pad Data Input (GPDI53)
8
R
00h
1537h
GPIO Pad Data Input (GPDI52)
8
R
00h
1538h
GPIO Pad Data Input (GPDI59)
8
R
00h
1539h
GPIO Pad Data Input (GPDI58)
8
R
00h
153Ah
GPIO Pad Data Input (GPDI57)
8
R
00h
153Bh
GPIO Pad Data Input (GPDI56)
8
R
00h
153Ch
GPIO Pad Data Input (GPDI63)
8
R
00h
153Dh
GPIO Pad Data Input (GPDI62)
8
R
00h
153Eh
GPIO Pad Data Input (GPDI61)
8
R
00h
153Fh
GPIO Pad Data Input (GPDI60)
8
R
00h
1540h
GPIO Pad Data Input (GPDI67)
8
R
00h
1541h
GPIO Pad Data Input (GPDI66)
8
R
00h
1542h
GPIO Pad Data Input (GPDI65)
8
R
00h
1543h
GPIO Pad Data Input (GPDI64)
8
R
00h
1544h
GPIO Pad Data Input (GPDI71)
8
R
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
342 / 5251


---
# 페이지 292

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1545h
GPIO Pad Data Input (GPDI70)
8
R
00h
1546h
GPIO Pad Data Input (GPDI69)
8
R
00h
1547h
GPIO Pad Data Input (GPDI68)
8
R
00h
1548h
GPIO Pad Data Input (GPDI75)
8
R
00h
1549h
GPIO Pad Data Input (GPDI74)
8
R
00h
154Ah
GPIO Pad Data Input (GPDI73)
8
R
00h
154Bh
GPIO Pad Data Input (GPDI72)
8
R
00h
154Ch
GPIO Pad Data Input (GPDI79)
8
R
00h
154Dh
GPIO Pad Data Input (GPDI78)
8
R
00h
154Eh
GPIO Pad Data Input (GPDI77)
8
R
00h
154Fh
GPIO Pad Data Input (GPDI76)
8
R
00h
1550h
GPIO Pad Data Input (GPDI83)
8
R
00h
1551h
GPIO Pad Data Input (GPDI82)
8
R
00h
1552h
GPIO Pad Data Input (GPDI81)
8
R
00h
1553h
GPIO Pad Data Input (GPDI80)
8
R
00h
1554h
GPIO Pad Data Input (GPDI87)
8
R
00h
1555h
GPIO Pad Data Input (GPDI86)
8
R
00h
1556h
GPIO Pad Data Input (GPDI85)
8
R
00h
1557h
GPIO Pad Data Input (GPDI84)
8
R
00h
1558h
GPIO Pad Data Input (GPDI91)
8
R
00h
1559h
GPIO Pad Data Input (GPDI90)
8
R
00h
155Ah
GPIO Pad Data Input (GPDI89)
8
R
00h
155Bh
GPIO Pad Data Input (GPDI88)
8
R
00h
155Ch
GPIO Pad Data Input (GPDI95)
8
R
00h
155Dh
GPIO Pad Data Input (GPDI94)
8
R
00h
155Eh
GPIO Pad Data Input (GPDI93)
8
R
00h
155Fh
GPIO Pad Data Input (GPDI92)
8
R
00h
1560h
GPIO Pad Data Input (GPDI99)
8
R
00h
1561h
GPIO Pad Data Input (GPDI98)
8
R
00h
1562h
GPIO Pad Data Input (GPDI97)
8
R
00h
1563h
GPIO Pad Data Input (GPDI96)
8
R
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
343 / 5251


---
# 페이지 293

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1564h
GPIO Pad Data Input (GPDI103)
8
R
00h
1565h
GPIO Pad Data Input (GPDI102)
8
R
00h
1566h
GPIO Pad Data Input (GPDI101)
8
R
00h
1567h
GPIO Pad Data Input (GPDI100)
8
R
00h
1568h
GPIO Pad Data Input (GPDI107)
8
R
00h
1569h
GPIO Pad Data Input (GPDI106)
8
R
00h
156Ah
GPIO Pad Data Input (GPDI105)
8
R
00h
156Bh
GPIO Pad Data Input (GPDI104)
8
R
00h
156Ch
GPIO Pad Data Input (GPDI111)
8
R
00h
156Dh
GPIO Pad Data Input (GPDI110)
8
R
00h
156Eh
GPIO Pad Data Input (GPDI109)
8
R
00h
156Fh
GPIO Pad Data Input (GPDI108)
8
R
00h
1570h
GPIO Pad Data Input (GPDI115)
8
R
00h
1571h
GPIO Pad Data Input (GPDI114)
8
R
00h
1572h
GPIO Pad Data Input (GPDI113)
8
R
00h
1573h
GPIO Pad Data Input (GPDI112)
8
R
00h
1574h
GPIO Pad Data Input (GPDI119)
8
R
00h
1575h
GPIO Pad Data Input (GPDI118)
8
R
00h
1576h
GPIO Pad Data Input (GPDI117)
8
R
00h
1577h
GPIO Pad Data Input (GPDI116)
8
R
00h
1578h
GPIO Pad Data Input (GPDI123)
8
R
00h
1579h
GPIO Pad Data Input (GPDI122)
8
R
00h
157Ah
GPIO Pad Data Input (GPDI121)
8
R
00h
157Bh
GPIO Pad Data Input (GPDI120)
8
R
00h
157Ch
GPIO Pad Data Input (GPDI127)
8
R
00h
157Dh
GPIO Pad Data Input (GPDI126)
8
R
00h
157Eh
GPIO Pad Data Input (GPDI125)
8
R
00h
157Fh
GPIO Pad Data Input (GPDI124)
8
R
00h
1580h
GPIO Pad Data Input (GPDI131)
8
R
00h
1581h
GPIO Pad Data Input (GPDI130)
8
R
00h
1582h
GPIO Pad Data Input (GPDI129)
8
R
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
344 / 5251


---
# 페이지 294

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1583h
GPIO Pad Data Input (GPDI128)
8
R
00h
1584h
GPIO Pad Data Input (GPDI135)
8
R
00h
1585h
GPIO Pad Data Input (GPDI134)
8
R
00h
1586h
GPIO Pad Data Input (GPDI133)
8
R
00h
1587h
GPIO Pad Data Input (GPDI132)
8
R
00h
1588h
GPIO Pad Data Input (GPDI139)
8
R
00h
1589h
GPIO Pad Data Input (GPDI138)
8
R
00h
158Ah
GPIO Pad Data Input (GPDI137)
8
R
00h
158Bh
GPIO Pad Data Input (GPDI136)
8
R
00h
158Ch
GPIO Pad Data Input (GPDI143)
8
R
00h
158Dh
GPIO Pad Data Input (GPDI142)
8
R
00h
158Fh
GPIO Pad Data Input (GPDI140)
8
R
00h
1590h
GPIO Pad Data Input (GPDI147)
8
R
00h
1591h
GPIO Pad Data Input (GPDI146)
8
R
00h
1592h
GPIO Pad Data Input (GPDI145)
8
R
00h
1593h
GPIO Pad Data Input (GPDI144)
8
R
00h
1594h
GPIO Pad Data Input (GPDI151)
8
R
00h
1595h
GPIO Pad Data Input (GPDI150)
8
R
00h
1596h
GPIO Pad Data Input (GPDI149)
8
R
00h
1597h
GPIO Pad Data Input (GPDI148)
8
R
00h
1598h
GPIO Pad Data Input (GPDI155)
8
R
00h
1599h
GPIO Pad Data Input (GPDI154)
8
R
00h
159Ah
GPIO Pad Data Input (GPDI153)
8
R
00h
159Bh
GPIO Pad Data Input (GPDI152)
8
R
00h
159Ch
GPIO Pad Data Input (GPDI159)
8
R
00h
159Dh
GPIO Pad Data Input (GPDI158)
8
R
00h
159Eh
GPIO Pad Data Input (GPDI157)
8
R
00h
159Fh
GPIO Pad Data Input (GPDI156)
8
R
00h
15A0h
GPIO Pad Data Input (GPDI163)
8
R
00h
15A1h
GPIO Pad Data Input (GPDI162)
8
R
00h
15A2h
GPIO Pad Data Input (GPDI161)
8
R
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
345 / 5251


---
# 페이지 295

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
15A3h
GPIO Pad Data Input (GPDI160)
8
R
00h
15A4h
GPIO Pad Data Input (GPDI167)
8
R
00h
15A5h
GPIO Pad Data Input (GPDI166)
8
R
00h
15A6h
GPIO Pad Data Input (GPDI165)
8
R
00h
15A7h
GPIO Pad Data Input (GPDI164)
8
R
00h
15A8h
GPIO Pad Data Input (GPDI171)
8
R
00h
15A9h
GPIO Pad Data Input (GPDI170)
8
R
00h
15AAh
GPIO Pad Data Input (GPDI169)
8
R
00h
15ABh
GPIO Pad Data Input (GPDI168)
8
R
00h
15ACh
GPIO Pad Data Input (GPDI175)
8
R
00h
15ADh
GPIO Pad Data Input (GPDI174)
8
R
00h
15AEh
GPIO Pad Data Input (GPDI173)
8
R
00h
15AFh
GPIO Pad Data Input (GPDI172)
8
R
00h
15B0h
GPIO Pad Data Input (GPDI179)
8
R
00h
15B1h
GPIO Pad Data Input (GPDI178)
8
R
00h
15B2h
GPIO Pad Data Input (GPDI177)
8
R
00h
15B3h
GPIO Pad Data Input (GPDI176)
8
R
00h
15B4h
GPIO Pad Data Input (GPDI183)
8
R
00h
15B5h
GPIO Pad Data Input (GPDI182)
8
R
00h
15B6h
GPIO Pad Data Input (GPDI181)
8
R
00h
15B7h
GPIO Pad Data Input (GPDI180)
8
R
00h
15B8h
GPIO Pad Data Input (GPDI187)
8
R
00h
15B9h
GPIO Pad Data Input (GPDI186)
8
R
00h
15BAh
GPIO Pad Data Input (GPDI185)
8
R
00h
15BBh
GPIO Pad Data Input (GPDI184)
8
R
00h
15BCh
GPIO Pad Data Input (GPDI191)
8
R
00h
15BDh
GPIO Pad Data Input (GPDI190)
8
R
00h
15BEh
GPIO Pad Data Input (GPDI189)
8
R
00h
15BFh
GPIO Pad Data Input (GPDI188)
8
R
00h
15C0h
GPIO Pad Data Input (GPDI195)
8
R
00h
15C1h
GPIO Pad Data Input (GPDI194)
8
R
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
346 / 5251


---
# 페이지 296

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
15C2h
GPIO Pad Data Input (GPDI193)
8
R
00h
15C3h
GPIO Pad Data Input (GPDI192)
8
R
00h
15C4h
GPIO Pad Data Input (GPDI199)
8
R
00h
15C5h
GPIO Pad Data Input (GPDI198)
8
R
00h
15C6h
GPIO Pad Data Input (GPDI197)
8
R
00h
15C7h
GPIO Pad Data Input (GPDI196)
8
R
00h
15C8h
GPIO Pad Data Input (GPDI203)
8
R
00h
15C9h
GPIO Pad Data Input (GPDI202)
8
R
00h
15CAh
GPIO Pad Data Input (GPDI201)
8
R
00h
15CBh
GPIO Pad Data Input (GPDI200)
8
R
00h
15CCh
GPIO Pad Data Input (GPDI207)
8
R
00h
15CDh
GPIO Pad Data Input (GPDI206)
8
R
00h
15CEh
GPIO Pad Data Input (GPDI205)
8
R
00h
15CFh
GPIO Pad Data Input (GPDI204)
8
R
00h
15D0h
GPIO Pad Data Input (GPDI211)
8
R
00h
15D1h
GPIO Pad Data Input (GPDI210)
8
R
00h
15D2h
GPIO Pad Data Input (GPDI209)
8
R
00h
15D3h
GPIO Pad Data Input (GPDI208)
8
R
00h
15D4h
GPIO Pad Data Input (GPDI215)
8
R
00h
15D5h
GPIO Pad Data Input (GPDI214)
8
R
00h
15D6h
GPIO Pad Data Input (GPDI213)
8
R
00h
15D7h
GPIO Pad Data Input (GPDI212)
8
R
00h
15D8h
GPIO Pad Data Input (GPDI219)
8
R
00h
15D9h
GPIO Pad Data Input (GPDI218)
8
R
00h
15DAh
GPIO Pad Data Input (GPDI217)
8
R
00h
15DBh
GPIO Pad Data Input (GPDI216)
8
R
00h
15DCh
GPIO Pad Data Input (GPDI223)
8
R
00h
15DDh
GPIO Pad Data Input (GPDI222)
8
R
00h
15DEh
GPIO Pad Data Input (GPDI221)
8
R
00h
15DFh
GPIO Pad Data Input (GPDI220)
8
R
00h
15E0h
GPIO Pad Data Input (GPDI227)
8
R
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
347 / 5251


---
# 페이지 297

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
15E1h
GPIO Pad Data Input (GPDI226)
8
R
00h
15E2h
GPIO Pad Data Input (GPDI225)
8
R
00h
15E3h
GPIO Pad Data Input (GPDI224)
8
R
00h
15E4h
GPIO Pad Data Input (GPDI231)
8
R
00h
15E5h
GPIO Pad Data Input (GPDI230)
8
R
00h
15E6h
GPIO Pad Data Input (GPDI229)
8
R
00h
15E7h
GPIO Pad Data Input (GPDI228)
8
R
00h
15E8h
GPIO Pad Data Input (GPDI235)
8
R
00h
15E9h
GPIO Pad Data Input (GPDI234)
8
R
00h
15EAh
GPIO Pad Data Input (GPDI233)
8
R
00h
15EBh
GPIO Pad Data Input (GPDI232)
8
R
00h
15ECh
GPIO Pad Data Input (GPDI239)
8
R
00h
15EDh
GPIO Pad Data Input (GPDI238)
8
R
00h
15EEh
GPIO Pad Data Input (GPDI237)
8
R
00h
15EFh
GPIO Pad Data Input (GPDI236)
8
R
00h
15F0h
GPIO Pad Data Input (GPDI243)
8
R
00h
15F1h
GPIO Pad Data Input (GPDI242)
8
R
00h
15F2h
GPIO Pad Data Input (GPDI241)
8
R
00h
15F3h
GPIO Pad Data Input (GPDI240)
8
R
00h
15F4h
GPIO Pad Data Input (GPDI247)
8
R
00h
15F5h
GPIO Pad Data Input (GPDI246)
8
R
00h
15F6h
GPIO Pad Data Input (GPDI245)
8
R
00h
15F7h
GPIO Pad Data Input (GPDI244)
8
R
00h
15F8h
GPIO Pad Data Input (GPDI251)
8
R
00h
15F9h
GPIO Pad Data Input (GPDI250)
8
R
00h
15FAh
GPIO Pad Data Input (GPDI249)
8
R
00h
15FBh
GPIO Pad Data Input (GPDI248)
8
R
00h
15FCh
GPIO Pad Data Input (GPDI255)
8
R
00h
15FDh
GPIO Pad Data Input (GPDI254)
8
R
00h
15FEh
GPIO Pad Data Input (GPDI253)
8
R
00h
15FFh
GPIO Pad Data Input (GPDI252)
8
R
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
348 / 5251


---
# 페이지 298

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1600h
GPIO Pad Data Input (GPDI259)
8
R
00h
1601h
GPIO Pad Data Input (GPDI258)
8
R
00h
1602h
GPIO Pad Data Input (GPDI257)
8
R
00h
1603h
GPIO Pad Data Input (GPDI256)
8
R
00h
1604h
GPIO Pad Data Input (GPDI263)
8
R
00h
1605h
GPIO Pad Data Input (GPDI262)
8
R
00h
1606h
GPIO Pad Data Input (GPDI261)
8
R
00h
1607h
GPIO Pad Data Input (GPDI260)
8
R
00h
1608h
GPIO Pad Data Input (GPDI267)
8
R
00h
1609h
GPIO Pad Data Input (GPDI266)
8
R
00h
160Ah
GPIO Pad Data Input (GPDI265)
8
R
00h
160Bh
GPIO Pad Data Input (GPDI264)
8
R
00h
160Ch
GPIO Pad Data Input (GPDI271)
8
R
00h
160Dh
GPIO Pad Data Input (GPDI270)
8
R
00h
160Eh
GPIO Pad Data Input (GPDI269)
8
R
00h
160Fh
GPIO Pad Data Input (GPDI268)
8
R
00h
1610h
GPIO Pad Data Input (GPDI275)
8
R
00h
1611h
GPIO Pad Data Input (GPDI274)
8
R
00h
1612h
GPIO Pad Data Input (GPDI273)
8
R
00h
1613h
GPIO Pad Data Input (GPDI272)
8
R
00h
1614h
GPIO Pad Data Input (GPDI279)
8
R
00h
1615h
GPIO Pad Data Input (GPDI278)
8
R
00h
1616h
GPIO Pad Data Input (GPDI277)
8
R
00h
1617h
GPIO Pad Data Input (GPDI276)
8
R
00h
1618h
GPIO Pad Data Input (GPDI283)
8
R
00h
1619h
GPIO Pad Data Input (GPDI282)
8
R
00h
161Ah
GPIO Pad Data Input (GPDI281)
8
R
00h
161Bh
GPIO Pad Data Input (GPDI280)
8
R
00h
161Ch
GPIO Pad Data Input (GPDI287)
8
R
00h
161Dh
GPIO Pad Data Input (GPDI286)
8
R
00h
161Eh
GPIO Pad Data Input (GPDI285)
8
R
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
349 / 5251


---
# 페이지 299

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
161Fh
GPIO Pad Data Input (GPDI284)
8
R
00h
1620h
GPIO Pad Data Input (GPDI291)
8
R
00h
1621h
GPIO Pad Data Input (GPDI290)
8
R
00h
1622h
GPIO Pad Data Input (GPDI289)
8
R
00h
1623h
GPIO Pad Data Input (GPDI288)
8
R
00h
1624h
GPIO Pad Data Input (GPDI295)
8
R
00h
1625h
GPIO Pad Data Input (GPDI294)
8
R
00h
1626h
GPIO Pad Data Input (GPDI293)
8
R
00h
1627h
GPIO Pad Data Input (GPDI292)
8
R
00h
1628h
GPIO Pad Data Input (GPDI299)
8
R
00h
1629h
GPIO Pad Data Input (GPDI298)
8
R
00h
162Ah
GPIO Pad Data Input (GPDI297)
8
R
00h
162Bh
GPIO Pad Data Input (GPDI296)
8
R
00h
162Ch
GPIO Pad Data Input (GPDI303)
8
R
00h
162Dh
GPIO Pad Data Input (GPDI302)
8
R
00h
162Eh
GPIO Pad Data Input (GPDI301)
8
R
00h
162Fh
GPIO Pad Data Input (GPDI300)
8
R
00h
1630h
GPIO Pad Data Input (GPDI307)
8
R
00h
1631h
GPIO Pad Data Input (GPDI306)
8
R
00h
1632h
GPIO Pad Data Input (GPDI305)
8
R
00h
1633h
GPIO Pad Data Input (GPDI304)
8
R
00h
1634h
GPIO Pad Data Input (GPDI311)
8
R
00h
1635h
GPIO Pad Data Input (GPDI310)
8
R
00h
1636h
GPIO Pad Data Input (GPDI309)
8
R
00h
1637h
GPIO Pad Data Input (GPDI308)
8
R
00h
1638h
GPIO Pad Data Input (GPDI315)
8
R
00h
1639h
GPIO Pad Data Input (GPDI314)
8
R
00h
163Ah
GPIO Pad Data Input (GPDI313)
8
R
00h
163Bh
GPIO Pad Data Input (GPDI312)
8
R
00h
163Ch
GPIO Pad Data Input (GPDI319)
8
R
00h
163Dh
GPIO Pad Data Input (GPDI318)
8
R
00h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
350 / 5251


---
# 페이지 300

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
163Eh
GPIO Pad Data Input (GPDI317)
8
R
00h
163Fh
GPIO Pad Data Input (GPDI316)
8
R
00h
1640h
GPIO Pad Data Input (GPDI323)
8
R
00h
1641h
GPIO Pad Data Input (GPDI322)
8
R
00h
1642h
GPIO Pad Data Input (GPDI321)
8
R
00h
1643h
GPIO Pad Data Input (GPDI320)
8
R
00h
1700h - 
1704h
Parallel GPIO Pad Data Output (PGPDO0 - PGPDO3) 1
16
RW
0000h
1706h
Parallel GPIO Pad Data Output (PGPDO2)
16
RW
0000h
1708h - 
1710h
Parallel GPIO Pad Data Output (PGPDO4 - PGPDO9) 1
16
RW
0000h
1712h
Parallel GPIO Pad Data Output (PGPDO8)
16
RW
0000h
1714h - 
1726h
Parallel GPIO Pad Data Output (PGPDO10 - PGPDO19) 1
16
RW
0000h
1740h - 
1744h
Parallel GPIO Pad Data Input (PGPDI0 - PGPDI3) 1
16
R
0000h
1746h
Parallel GPIO Pad Data Input (PGPDI2)
16
R
0000h
1748h - 
1750h
Parallel GPIO Pad Data Input (PGPDI4 - PGPDI9) 1
16
R
0000h
1752h
Parallel GPIO Pad Data Input (PGPDI8)
16
R
0000h
1754h - 
1766h
Parallel GPIO Pad Data Input (PGPDI10 - PGPDI19) 1
16
R
0000h
1780h - 
1784h
Masked Parallel GPIO Pad Data Output (MPGPDO0 - MPGPDO1)
32
W
0000_0000h
1788h
Masked Parallel GPIO Pad Data Output (MPGPDO2)
32
W
0000_0000h
178Ch - 
179Ch
Masked Parallel GPIO Pad Data Output (MPGPDO3 - MPGPDO7)
32
W
0000_0000h
17A0h
Masked Parallel GPIO Pad Data Output (MPGPDO8)
32
W
0000_0000h
17A4h - 
17CCh
Masked Parallel GPIO Pad Data Output (MPGPDO9 - MPGPDO19)
32
W
0000_0000h
1. In this array, the index and offset values of the registers do not increment in direct alignment. For details, see the register 
description.
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
351 / 5251


---
# 페이지 301

10.6.2 SIUL2 MCU ID Register #1 (MIDR1)
Offset
Register
Offset
MIDR1
4h
Function
This register holds identification information about the device.
 
This register supports only 32-bit accesses. Byte and half-word accesses are not supported.
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
PRODUCT_LINE_LETTER 
PART_NO 
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
Reserved 
MAJOR_MASK 
MINOR_MASK 
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
31-26
PRODUCT_LIN
E_LETTER
Product Line Letter
Identified the ASCII character in MCU Part Number. This field specifies the part number suffix, and needs 
to be combined with MIDR1[PART_NO] to provide the full chip number.
0x0B K
This value is set at the factory and cannot be changed. All other values are reserved.
25-16
PART_NO
MCU Part Number
S32K310 - 0x136
S32K341 - 0x155
S32K311 - 0x137
S32K312 - 0x138
S32K314 - 0x13A
S32K322 - 0x142
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
352 / 5251


---
# 페이지 302

Table continued from the previous page...
Field
Function
S32K324 - 0x144
S32K328 - 0x148
S32K338 - 0x152
S32K342 - 0x156
S32K344 - 0x158
S32K348 - 0x15C
S32K358 - 0x166
S32K388 - 0x184
S32K389 - 0x185
15-8
—
Reserved
7-4
MAJOR_MASK
Major Mask Revision
For all variants - 0
3-0
MINOR_MASK
Minor Mask Revision
S32K358 - 1
For other variants - 0
10.6.3 SIUL2 MCU ID Register #2 (MIDR2)
Offset
Register
Offset
MIDR2
8h
Function
 
This register supports only 32-bit accesses. Byte and half-word accesses are not supported.
  NOTE  
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
353 / 5251


---
# 페이지 303

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
TECHNOLOGY 
TEMPERATURE 
PACKAGE 
FREQUENCY 
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
FLASH_CODE 
FLASH_DATA 
FLASH_SIZE_DATA 
FLASH_SIZE_CODE 
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
31-29
TECHNOLOGY
Technology
Identifies the silicon technology.
001b - C40EFS3
28-26
TEMPERATUR
E
Temperature
Identifies the ambient temperature range.
010b - V = 105C
100b - M = 125C
25-20
PACKAGE
Package
This field can by read by software to determine the package type that is used for the particular device.
00_0011b - 257-MAPBGA
00_0100b - 289-MAPBGA
10_0010b - 100-HDQFP
10_0011b - 100-HDQFP
10_0101b - 172-HDQFP
10_0110b - 172-HDQFP
10_0111b - 172-HDQFP-EP
19-16
FREQUENCY
Frequency
Identifies maximum core frequency. Qualified by Product Line Letter to provide wider range of 
frequencies.
0011b - 120 MHz
0100b - 160 MHz
0101b - 240 MHz
0110b - 320 MHz
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
354 / 5251


---
# 페이지 304

Table continued from the previous page...
Field
Function
15-14
FLASH_CODE
Flash Code
Identifies the location of Code Flash, if any, within the package.
10b - Monolithic
13-12
FLASH_DATA
Flash Data
Identifies the location of Data Flash, if any, within the package.
10b - Monolithic
11-8
FLASH_SIZE_D
ATA
Flash Size Data
Identifies the Flash (EE) memory size.
0000b - 64KB
0001b - 128KB
0010b - 256KB
7-0
FLASH_SIZE_C
ODE
Flash Size Code
Identifies the Flash (code) memory size.
0000_0010b - 512kB
0000_0100b - 1MB
0000_1000b - 2.00MB
0000_1100b - 3.00MB
0001_0000b - 4.00MB
0001_1000b - 6.00MB
0010_0000b - 8.00MB
10.6.4 DMA or Interrupt Status Flag 0 (DISR0)
Offset
Register
Offset
DISR0
10h
Function
Contains flags that record an event on the external IRQ pins. This register supports 8-, 16-, and 32-bit accesses.
When an event (as defined in Interrupt Rising-Edge Event Enable 0 (IREER0) and IFEER0) occurs, the corresponding flag is set. 
The IRQ flag is set regardless of the state of the corresponding DIRER0[EIREn]. The IRQ flag remains set until you clear it or is 
cleared by servicing of a DMA request. The IRQ flags are cleared when you write 1 to them. A write of 0 has no effect.
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
355 / 5251


---
# 페이지 305

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
EIF31 
EIF30 
EIF29 
EIF28 
EIF27 
EIF26 
EIF25 
EIF24 
EIF23 
EIF22 
EIF21 
EIF20 
EIF19 
EIF18 
EIF17 
EIF16 
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
EIF15 
EIF14 
EIF13 
EIF12 
EIF11 
EIF10 
EIF9 
EIF8 
EIF7 
EIF6 
EIF5 
EIF4 
EIF3 
EIF2 
EIF1 
EIF0 
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
EIF31
External Interrupt Status Flag 31
Indicates whether an interrupt event (as defined by IREER31 and IFEER31) has occurred.
If this flag is set (DIRERR31 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
30
EIF30
External Interrupt Status Flag 30
Indicates whether an interrupt event (as defined by IREER30 and IFEER30) has occurred.
If this flag is set (DIRERR30 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
356 / 5251


---
# 페이지 306

Table continued from the previous page...
Field
Function
29
EIF29
External Interrupt Status Flag 29
Indicates whether an interrupt event (as defined by IREER29 and IFEER29) has occurred.
If this flag is set (DIRERR29 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
28
EIF28
External Interrupt Status Flag 28
Indicates whether an interrupt event (as defined by IREER28 and IFEER28) has occurred.
If this flag is set (DIRERR28 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
27
EIF27
External Interrupt Status Flag 27
Indicates whether an interrupt event (as defined by IREER27 and IFEER27) has occurred.
If this flag is set (DIRERR27 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
357 / 5251


---
# 페이지 307

Table continued from the previous page...
Field
Function
1b - Clear the flag
26
EIF26
External Interrupt Status Flag 26
Indicates whether an interrupt event (as defined by IREER26 and IFEER26) has occurred.
If this flag is set (DIRERR26 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
25
EIF25
External Interrupt Status Flag 25
Indicates whether an interrupt event (as defined by IREER25 and IFEER25) has occurred.
If this flag is set (DIRERR25 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
24
EIF24
External Interrupt Status Flag 24
Indicates whether an interrupt event (as defined by IREER24 and IFEER24) has occurred.
If this flag is set (DIRERR24 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
358 / 5251


---
# 페이지 308

Table continued from the previous page...
Field
Function
0b - No effect
1b - Clear the flag
23
EIF23
External Interrupt Status Flag 23
Indicates whether an interrupt event (as defined by IREER23 and IFEER23) has occurred.
If this flag is set (DIRERR23 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
22
EIF22
External Interrupt Status Flag 22
Indicates whether an interrupt event (as defined by IREER22 and IFEER22) has occurred.
If this flag is set (DIRERR22 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
21
EIF21
External Interrupt Status Flag 21
Indicates whether an interrupt event (as defined by IREER21 and IFEER21) has occurred.
If this flag is set (DIRERR21 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
359 / 5251


---
# 페이지 309

Table continued from the previous page...
Field
Function
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
20
EIF20
External Interrupt Status Flag 20
Indicates whether an interrupt event (as defined by IREER20 and IFEER20) has occurred.
If this flag is set (DIRERR20 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
19
EIF19
External Interrupt Status Flag 19
Indicates whether an interrupt event (as defined by IREER19 and IFEER19) has occurred.
If this flag is set (DIRERR19 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
18
EIF18
External Interrupt Status Flag 18
Indicates whether an interrupt event (as defined by IREER18 and IFEER18) has occurred.
If this flag is set (DIRERR18 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
360 / 5251


---
# 페이지 310

Table continued from the previous page...
Field
Function
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
17
EIF17
External Interrupt Status Flag 17
Indicates whether an interrupt event (as defined by IREER17 and IFEER17) has occurred.
If this flag is set (DIRERR17 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
16
EIF16
External Interrupt Status Flag 16
Indicates whether an interrupt event (as defined by IREER16 and IFEER16) has occurred.
If this flag is set (DIRERR16 = 1), it causes an interrupt.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
15
EIF15
External Interrupt Status Flag 15
Indicates whether an interrupt event (as defined by IREER15 and IFEER15) has occurred.
If this flag is set (DIRERR15 = 1), it causes an interrupt or DMA request.
 
This field behaves differently for register reads and writes.
  NOTE  
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
361 / 5251


---
# 페이지 311

Table continued from the previous page...
Field
Function
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
14
EIF14
External Interrupt Status Flag 14
Indicates whether an interrupt event (as defined by IREER14 and IFEER14) has occurred.
If this flag is set (DIRERR14 = 1), it causes an interrupt or DMA request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
13
EIF13
External Interrupt Status Flag 13
Indicates whether an interrupt event (as defined by IREER13 and IFEER13) has occurred.
If this flag is set (DIRERR13 = 1), it causes an interrupt or DMA request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
12
EIF12
External Interrupt Status Flag 12
Indicates whether an interrupt event (as defined by IREER12 and IFEER12) has occurred.
If this flag is set (DIRERR12 = 1), it causes an interrupt or DMA request.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
362 / 5251


---
# 페이지 312

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
11
EIF11
External Interrupt Status Flag 11
Indicates whether an interrupt event (as defined by IREER11 and IFEER11) has occurred.
If this flag is set (DIRERR11 = 1), it causes an interrupt or DMA request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
10
EIF10
External Interrupt Status Flag 10
Indicates whether an interrupt event (as defined by IREER10 and IFEER10) has occurred.
If this flag is set (DIRERR10 = 1), it causes an interrupt or DMA request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
9
EIF9
External Interrupt Status Flag 9
Indicates whether an interrupt event (as defined by IREER9 and IFEER9) has occurred.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
363 / 5251


---
# 페이지 313

Table continued from the previous page...
Field
Function
If this flag is set (DIRERR9 = 1), it causes an interrupt or DMA request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
8
EIF8
External Interrupt Status Flag 8
Indicates whether an interrupt event (as defined by IREER8 and IFEER8) has occurred.
If this flag is set (DIRERR8 = 1), it causes an interrupt or DMA request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
7
EIF7
External Interrupt Status Flag 7
Indicates whether an interrupt event (as defined by IREER7 and IFEER7) has occurred.
If this flag is set (DIRERR7 = 1), it causes an interrupt or DMA request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
6
External Interrupt Status Flag 6
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
364 / 5251


---
# 페이지 314

Table continued from the previous page...
Field
Function
EIF6
Indicates whether an interrupt event (as defined by IREER6 and IFEER6) has occurred.
If this flag is set (DIRERR6 = 1), it causes an interrupt or DMA request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
5
EIF5
External Interrupt Status Flag 5
Indicates whether an interrupt event (as defined by IREER5 and IFEER5) has occurred.
If this flag is set (DIRERR5 = 1), it causes an interrupt or DMA request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
4
EIF4
External Interrupt Status Flag 4
Indicates whether an interrupt event (as defined by IREER4 and IFEER4) has occurred.
If this flag is set (DIRERR4 = 1), it causes an interrupt or DMA request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
365 / 5251


---
# 페이지 315

Table continued from the previous page...
Field
Function
3
EIF3
External Interrupt Status Flag 3
Indicates whether an interrupt event (as defined by IREER3 and IFEER3) has occurred.
If this flag is set (DIRERR3 = 1), it causes an interrupt or DMA request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
2
EIF2
External Interrupt Status Flag 2
Indicates whether an interrupt event (as defined by IREER2 and IFEER2) has occurred.
If this flag is set (DIRERR2 = 1), it causes an interrupt or DMA request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
1
EIF1
External Interrupt Status Flag 1
Indicates whether an interrupt event (as defined by IREER1 and IFEER1) has occurred.
If this flag is set (DIRERR1 = 1), it causes an interrupt or DMA request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
366 / 5251


---
# 페이지 316

Table continued from the previous page...
Field
Function
1b - Clear the flag
0
EIF0
External Interrupt Status Flag 0
Indicates whether an interrupt event (as defined by IREER0 and IFEER0) has occurred.
If this flag is set (DIRERR0 = 1), it causes an interrupt or DMA request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Interrupt event did not occur on the pad
1b - Interrupt event occurred
When writing
0b - No effect
1b - Clear the flag
10.6.5 DMA or Interrupt Request Enable 0 (DIRER0)
Offset
Register
Offset
DIRER0
18h
Function
Enables the assertion of a DMA or interrupt request to the interrupt controller if the corresponding DISR0[EIFn] flag is 1. The type 
of request is determined by the corresponding DIRSR0[DIRSRn] field.
This register supports 8-, 16-, and 32-bit accesses.
 
You cannot enable or disable DIRSR0 after it selects a DMA request.
  NOTE  
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
367 / 5251


---
# 페이지 317

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
EIRE3
1 
EIRE3
0 
EIRE2
9 
EIRE2
8 
EIRE2
7 
EIRE2
6 
EIRE2
5 
EIRE2
4 
EIRE2
3 
EIRE2
2 
EIRE2
1 
EIRE2
0 
EIRE1
9 
EIRE1
8 
EIRE1
7 
EIRE1
6 
W
Reset
0
0
0
0
0
0
0
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
EIRE1
5 
EIRE1
4 
EIRE1
3 
EIRE1
2 
EIRE1
1 
EIRE1
0 
EIRE9 
EIRE8 
EIRE7 
EIRE6 
EIRE5 
EIRE4 
EIRE3 
EIRE2 
EIRE1 
EIRE0 
W
Reset
0
0
0
0
0
0
0
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
EIRE31
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
30
EIRE30
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
29
EIRE29
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
28
EIRE28
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
27
EIRE27
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
26
EIRE26
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
368 / 5251


---
# 페이지 318

Table continued from the previous page...
Field
Function
0b - Disable
1b - Enable
25
EIRE25
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
24
EIRE24
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
23
EIRE23
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
22
EIRE22
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
21
EIRE21
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
20
EIRE20
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
19
EIRE19
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
18
External Interrupt Request Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
369 / 5251


---
# 페이지 319

Table continued from the previous page...
Field
Function
EIRE18
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
17
EIRE17
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
16
EIRE16
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
15
EIRE15
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
14
EIRE14
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
13
EIRE13
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
12
EIRE12
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
11
EIRE11
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
370 / 5251


---
# 페이지 320

Table continued from the previous page...
Field
Function
10
EIRE10
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
9
EIRE9
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
8
EIRE8
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
7
EIRE7
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
6
EIRE6
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
5
EIRE5
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
4
EIRE4
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
3
EIRE3
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
371 / 5251


---
# 페이지 321

Table continued from the previous page...
Field
Function
1b - Enable
2
EIRE2
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
1
EIRE1
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
0
EIRE0
External Interrupt Request Enable
Enables the interrupt requests from the corresponding pin.
0b - Disable
1b - Enable
10.6.6 DMA or Interrupt Request Select 0 (DIRSR0)
Offset
Register
Offset
DIRSR0
20h
Function
Selects the type of request (DMA or interrupt request). This register supports 8-, 16-, and 32-bit accesses.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
DIRSR
31 
DIRSR
30 
DIRSR
29 
DIRSR
28 
DIRSR
27 
DIRSR
26 
DIRSR
25 
DIRSR
24 
DIRSR
23 
DIRSR
22 
DIRSR
21 
DIRSR
20 
DIRSR
19 
DIRSR
18 
DIRSR
17 
DIRSR
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
DIRSR
15 
DIRSR
14 
DIRSR
13 
DIRSR
12 
DIRSR
11 
DIRSR
10 
DIRSR
9 
DIRSR
8 
DIRSR
7 
DIRSR
6 
DIRSR
5 
DIRSR
4 
DIRSR
3 
DIRSR
2 
DIRSR
1 
DIRSR
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
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
372 / 5251


---
# 페이지 322

Fields
Field
Function
31
DIRSR31
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
30
DIRSR30
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
29
DIRSR29
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
28
DIRSR28
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
27
DIRSR27
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
373 / 5251


---
# 페이지 323

Table continued from the previous page...
Field
Function
26
DIRSR26
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
25
DIRSR25
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
24
DIRSR24
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
23
DIRSR23
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
22
DIRSR22
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
374 / 5251


---
# 페이지 324

Table continued from the previous page...
Field
Function
21
DIRSR21
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
20
DIRSR20
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
19
DIRSR19
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
18
DIRSR18
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
17
DIRSR17
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
375 / 5251


---
# 페이지 325

Table continued from the previous page...
Field
Function
16
DIRSR16
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - Reserved
15
DIRSR15
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
14
DIRSR14
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
13
DIRSR13
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
12
DIRSR12
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
376 / 5251


---
# 페이지 326

Table continued from the previous page...
Field
Function
11
DIRSR11
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
10
DIRSR10
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
9
DIRSR9
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
8
DIRSR8
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
7
DIRSR7
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
377 / 5251


---
# 페이지 327

Table continued from the previous page...
Field
Function
6
DIRSR6
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
5
DIRSR5
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
4
DIRSR4
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
3
DIRSR3
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
2
DIRSR2
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
378 / 5251


---
# 페이지 328

Table continued from the previous page...
Field
Function
1
DIRSR1
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
0
DIRSR0
DMA or Interrupt Request Select
Selects either a DMA request or an external interrupt request when an edge-triggered event occurs on the 
corresponding pin.
This field determines whether a DMA request or an interrupt request asserts the 
corresponding DISR0[EIFn].
0b - Interrupt request
1b - DMA request
10.6.7 Interrupt Rising-Edge Event Enable 0 (IREER0)
Offset
Register
Offset
IREER0
28h
Function
Enables the rising-edge triggered events on the corresponding interrupt pads. This register supports 8-, 16-, and 32-bit accesses.
 
If you write 0 to both the IREE and IFEE fields for the same interrupt source, the interrupt status flag for the 
corresponding external interrupt never sets.
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
IREE3
1 
IREE3
0 
IREE2
9 
IREE2
8 
IREE2
7 
IREE2
6 
IREE2
5 
IREE2
4 
IREE2
3 
IREE2
2 
IREE2
1 
IREE2
0 
IREE1
9 
IREE1
8 
IREE1
7 
IREE1
6 
W
Reset
0
0
0
0
0
0
0
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
IREE1
5 
IREE1
4 
IREE1
3 
IREE1
2 
IREE1
1 
IREE1
0 
IREE9 
IREE8 
IREE7 
IREE6 
IREE5 
IREE4 
IREE3 
IREE2 
IREE1 
IREE0 
W
Reset
0
0
0
0
0
0
0
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
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
379 / 5251


---
# 페이지 329

Fields
Field
Function
31
IREE31
Interrupt Rising-Edge Event Enable 31
Enables the rising-edge events to set DISR0[EIF31].
0b - Disable
1b - Enable
30
IREE30
Interrupt Rising-Edge Event Enable 30
Enables the rising-edge events to set DISR0[EIF30].
0b - Disable
1b - Enable
29
IREE29
Interrupt Rising-Edge Event Enable 29
Enables the rising-edge events to set DISR0[EIF29].
0b - Disable
1b - Enable
28
IREE28
Interrupt Rising-Edge Event Enable 28
Enables the rising-edge events to set DISR0[EIF28].
0b - Disable
1b - Enable
27
IREE27
Interrupt Rising-Edge Event Enable 27
Enables the rising-edge events to set DISR0[EIF27].
0b - Disable
1b - Enable
26
IREE26
Interrupt Rising-Edge Event Enable 26
Enables the rising-edge events to set DISR0[EIF26].
0b - Disable
1b - Enable
25
IREE25
Interrupt Rising-Edge Event Enable 25
Enables the rising-edge events to set DISR0[EIF25].
0b - Disable
1b - Enable
24
IREE24
Interrupt Rising-Edge Event Enable 24
Enables the rising-edge events to set DISR0[EIF24].
0b - Disable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
380 / 5251


---
# 페이지 330

Table continued from the previous page...
Field
Function
1b - Enable
23
IREE23
Interrupt Rising-Edge Event Enable 23
Enables the rising-edge events to set DISR0[EIF23].
0b - Disable
1b - Enable
22
IREE22
Interrupt Rising-Edge Event Enable 22
Enables the rising-edge events to set DISR0[EIF22].
0b - Disable
1b - Enable
21
IREE21
Interrupt Rising-Edge Event Enable 21
Enables the rising-edge events to set DISR0[EIF21].
0b - Disable
1b - Enable
20
IREE20
Interrupt Rising-Edge Event Enable 20
Enables the rising-edge events to set DISR0[EIF20].
0b - Disable
1b - Enable
19
IREE19
Interrupt Rising-Edge Event Enable 19
Enables the rising-edge events to set DISR0[EIF19].
0b - Disable
1b - Enable
18
IREE18
Interrupt Rising-Edge Event Enable 18
Enables the rising-edge events to set DISR0[EIF18].
0b - Disable
1b - Enable
17
IREE17
Interrupt Rising-Edge Event Enable 17
Enables the rising-edge events to set DISR0[EIF17].
0b - Disable
1b - Enable
16
IREE16
Interrupt Rising-Edge Event Enable 16
Enables the rising-edge events to set DISR0[EIF16].
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
381 / 5251


---
# 페이지 331

Table continued from the previous page...
Field
Function
0b - Disable
1b - Enable
15
IREE15
Interrupt Rising-Edge Event Enable 15
Enables the rising-edge events to set DISR0[EIF15].
0b - Disable
1b - Enable
14
IREE14
Interrupt Rising-Edge Event Enable 14
Enables the rising-edge events to set DISR0[EIF14].
0b - Disable
1b - Enable
13
IREE13
Interrupt Rising-Edge Event Enable 13
Enables the rising-edge events to set DISR0[EIF13].
0b - Disable
1b - Enable
12
IREE12
Interrupt Rising-Edge Event Enable 12
Enables the rising-edge events to set DISR0[EIF12].
0b - Disable
1b - Enable
11
IREE11
Interrupt Rising-Edge Event Enable 11
Enables the rising-edge events to set DISR0[EIF11].
0b - Disable
1b - Enable
10
IREE10
Interrupt Rising-Edge Event Enable 10
Enables the rising-edge events to set DISR0[EIF10].
0b - Disable
1b - Enable
9
IREE9
Interrupt Rising-Edge Event Enable 9
Enables the rising-edge events to set DISR0[EIF9].
0b - Disable
1b - Enable
8
Interrupt Rising-Edge Event Enable 8
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
382 / 5251


---
# 페이지 332

Table continued from the previous page...
Field
Function
IREE8
Enables the rising-edge events to set DISR0[EIF8].
0b - Disable
1b - Enable
7
IREE7
Interrupt Rising-Edge Event Enable 7
Enables the rising-edge events to set DISR0[EIF7].
0b - Disable
1b - Enable
6
IREE6
Interrupt Rising-Edge Event Enable 6
Enables the rising-edge events to set DISR0[EIF6].
0b - Disable
1b - Enable
5
IREE5
Interrupt Rising-Edge Event Enable 5
Enables the rising-edge events to set DISR0[EIF5].
0b - Disable
1b - Enable
4
IREE4
Interrupt Rising-Edge Event Enable 4
Enables the rising-edge events to set DISR0[EIF4].
0b - Disable
1b - Enable
3
IREE3
Interrupt Rising-Edge Event Enable 3
Enables the rising-edge events to set DISR0[EIF3].
0b - Disable
1b - Enable
2
IREE2
Interrupt Rising-Edge Event Enable 2
Enables the rising-edge events to set DISR0[EIF2].
0b - Disable
1b - Enable
1
IREE1
Interrupt Rising-Edge Event Enable 1
Enables the rising-edge events to set DISR0[EIF1].
0b - Disable
1b - Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
383 / 5251


---
# 페이지 333

Table continued from the previous page...
Field
Function
0
IREE0
Interrupt Rising-Edge Event Enable 0
Enables the rising-edge events to set DISR0[EIF0].
0b - Disable
1b - Enable
10.6.8 Interrupt Falling-Edge Event Enable 0 (IFEER0)
Offset
Register
Offset
IFEER0
30h
Function
Enables the falling-edge triggered events on the corresponding interrupt pads. This register supports 8-, 16-, and 32-bit accesses.
 
If you write 0 to both the IREE and IFEE fields for the same interrupt source, the interrupt status flag for the 
corresponding external interrupt never sets.
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
IFEE3
1 
IFEE3
0 
IFEE2
9 
IFEE2
8 
IFEE2
7 
IFEE2
6 
IFEE2
5 
IFEE2
4 
IFEE2
3 
IFEE2
2 
IFEE2
1 
IFEE2
0 
IFEE1
9 
IFEE1
8 
IFEE1
7 
IFEE1
6 
W
Reset
0
0
0
0
0
0
0
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
IFEE1
5 
IFEE1
4 
IFEE1
3 
IFEE1
2 
IFEE1
1 
IFEE1
0 
IFEE9 
IFEE8 
IFEE7 
IFEE6 
IFEE5 
IFEE4 
IFEE3 
IFEE2 
IFEE1 
IFEE0 
W
Reset
0
0
0
0
0
0
0
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
IFEE31
Interrupt Falling-Edge Event Enable 31
Enables the falling-edge events to set DISR0[EIF31].
0b - Disable
1b - Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
384 / 5251


---
# 페이지 334

Table continued from the previous page...
Field
Function
30
IFEE30
Interrupt Falling-Edge Event Enable 30
Enables the falling-edge events to set DISR0[EIF30].
0b - Disable
1b - Enable
29
IFEE29
Interrupt Falling-Edge Event Enable 29
Enables the falling-edge events to set DISR0[EIF29].
0b - Disable
1b - Enable
28
IFEE28
Interrupt Falling-Edge Event Enable 28
Enables the falling-edge events to set DISR0[EIF28].
0b - Disable
1b - Enable
27
IFEE27
Interrupt Falling-Edge Event Enable 27
Enables the falling-edge events to set DISR0[EIF27].
0b - Disable
1b - Enable
26
IFEE26
Interrupt Falling-Edge Event Enable 26
Enables the falling-edge events to set DISR0[EIF26].
0b - Disable
1b - Enable
25
IFEE25
Interrupt Falling-Edge Event Enable 25
Enables the falling-edge events to set DISR0[EIF25].
0b - Disable
1b - Enable
24
IFEE24
Interrupt Falling-Edge Event Enable 24
Enables the falling-edge events to set DISR0[EIF24].
0b - Disable
1b - Enable
23
IFEE23
Interrupt Falling-Edge Event Enable 23
Enables the falling-edge events to set DISR0[EIF23].
0b - Disable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
385 / 5251


---
# 페이지 335

Table continued from the previous page...
Field
Function
1b - Enable
22
IFEE22
Interrupt Falling-Edge Event Enable 22
Enables the falling-edge events to set DISR0[EIF22].
0b - Disable
1b - Enable
21
IFEE21
Interrupt Falling-Edge Event Enable 21
Enables the falling-edge events to set DISR0[EIF21].
0b - Disable
1b - Enable
20
IFEE20
Interrupt Falling-Edge Event Enable 20
Enables the falling-edge events to set DISR0[EIF20].
0b - Disable
1b - Enable
19
IFEE19
Interrupt Falling-Edge Event Enable 19
Enables the falling-edge events to set DISR0[EIF19].
0b - Disable
1b - Enable
18
IFEE18
Interrupt Falling-Edge Event Enable 18
Enables the falling-edge events to set DISR0[EIF18].
0b - Disable
1b - Enable
17
IFEE17
Interrupt Falling-Edge Event Enable 17
Enables the falling-edge events to set DISR0[EIF17].
0b - Disable
1b - Enable
16
IFEE16
Interrupt Falling-Edge Event Enable 16
Enables the falling-edge events to set DISR0[EIF16].
0b - Disable
1b - Enable
15
IFEE15
Interrupt Falling-Edge Event Enable 15
Enables the falling-edge events to set DISR0[EIF15].
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
386 / 5251


---
# 페이지 336

Table continued from the previous page...
Field
Function
0b - Disable
1b - Enable
14
IFEE14
Interrupt Falling-Edge Event Enable 14
Enables the falling-edge events to set DISR0[EIF14].
0b - Disable
1b - Enable
13
IFEE13
Interrupt Falling-Edge Event Enable 13
Enables the falling-edge events to set DISR0[EIF13].
0b - Disable
1b - Enable
12
IFEE12
Interrupt Falling-Edge Event Enable 12
Enables the falling-edge events to set DISR0[EIF12].
0b - Disable
1b - Enable
11
IFEE11
Interrupt Falling-Edge Event Enable 11
Enables the falling-edge events to set DISR0[EIF11].
0b - Disable
1b - Enable
10
IFEE10
Interrupt Falling-Edge Event Enable 10
Enables the falling-edge events to set DISR0[EIF10].
0b - Disable
1b - Enable
9
IFEE9
Interrupt Falling-Edge Event Enable 9
Enables the falling-edge events to set DISR0[EIF9].
0b - Disable
1b - Enable
8
IFEE8
Interrupt Falling-Edge Event Enable 8
Enables the falling-edge events to set DISR0[EIF8].
0b - Disable
1b - Enable
7
Interrupt Falling-Edge Event Enable 7
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
387 / 5251


---
# 페이지 337

Table continued from the previous page...
Field
Function
IFEE7
Enables the falling-edge events to set DISR0[EIF7].
0b - Disable
1b - Enable
6
IFEE6
Interrupt Falling-Edge Event Enable 6
Enables the falling-edge events to set DISR0[EIF6].
0b - Disable
1b - Enable
5
IFEE5
Interrupt Falling-Edge Event Enable 5
Enables the falling-edge events to set DISR0[EIF5].
0b - Disable
1b - Enable
4
IFEE4
Interrupt Falling-Edge Event Enable 4
Enables the falling-edge events to set DISR0[EIF4].
0b - Disable
1b - Enable
3
IFEE3
Interrupt Falling-Edge Event Enable 3
Enables the falling-edge events to set DISR0[EIF3].
0b - Disable
1b - Enable
2
IFEE2
Interrupt Falling-Edge Event Enable 2
Enables the falling-edge events to set DISR0[EIF2].
0b - Disable
1b - Enable
1
IFEE1
Interrupt Falling-Edge Event Enable 1
Enables the falling-edge events to set DISR0[EIF1].
0b - Disable
1b - Enable
0
IFEE0
Interrupt Falling-Edge Event Enable 0
Enables the falling-edge events to set DISR0[EIF0].
0b - Disable
1b - Enable
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
388 / 5251


---
# 페이지 338

10.6.9 Interrupt Filter Enable 0 (IFER0)
Offset
Register
Offset
IFER0
38h
Function
Enables a digital filter counter on the corresponding interrupt pads to filter out glitches on the inputs. This register supports 8-, 16-, 
and 32-bit accesses.
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
IFE31 
IFE30 
IFE29 
IFE28 
IFE27 
IFE26 
IFE25 
IFE24 
IFE23 
IFE22 
IFE21 
IFE20 
IFE19 
IFE18 
IFE17 
IFE16 
W
Reset
0
0
0
0
0
0
0
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
IFE15 
IFE14 
IFE13 
IFE12 
IFE11 
IFE10 
IFE9 
IFE8 
IFE7 
IFE6 
IFE5 
IFE4 
IFE3 
IFE2 
IFE1 
IFE0 
W
Reset
0
0
0
0
0
0
0
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
IFE31
Interrupt Filter Enable 31
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
30
IFE30
Interrupt Filter Enable 30
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
29
IFE29
Interrupt Filter Enable 29
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
28
Interrupt Filter Enable 28
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
389 / 5251


---
# 페이지 339

Table continued from the previous page...
Field
Function
IFE28
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
27
IFE27
Interrupt Filter Enable 27
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
26
IFE26
Interrupt Filter Enable 26
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
25
IFE25
Interrupt Filter Enable 25
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
24
IFE24
Interrupt Filter Enable 24
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
23
IFE23
Interrupt Filter Enable 23
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
22
IFE22
Interrupt Filter Enable 22
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
21
IFE21
Interrupt Filter Enable 21
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
390 / 5251


---
# 페이지 340

Table continued from the previous page...
Field
Function
20
IFE20
Interrupt Filter Enable 20
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
19
IFE19
Interrupt Filter Enable 19
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
18
IFE18
Interrupt Filter Enable 18
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
17
IFE17
Interrupt Filter Enable 17
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
16
IFE16
Interrupt Filter Enable 16
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
15
IFE15
Interrupt Filter Enable 15
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
14
IFE14
Interrupt Filter Enable 14
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
13
IFE13
Interrupt Filter Enable 13
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
391 / 5251


---
# 페이지 341

Table continued from the previous page...
Field
Function
1b - Enable
12
IFE12
Interrupt Filter Enable 12
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
11
IFE11
Interrupt Filter Enable 11
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
10
IFE10
Interrupt Filter Enable 10
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
9
IFE9
Interrupt Filter Enable 9
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
8
IFE8
Interrupt Filter Enable 8
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
7
IFE7
Interrupt Filter Enable 7
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
6
IFE6
Interrupt Filter Enable 6
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
5
IFE5
Interrupt Filter Enable 5
Enables the digital glitch filter on the interrupt pad input.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
392 / 5251


---
# 페이지 342

Table continued from the previous page...
Field
Function
0b - Disable
1b - Enable
4
IFE4
Interrupt Filter Enable 4
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
3
IFE3
Interrupt Filter Enable 3
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
2
IFE2
Interrupt Filter Enable 2
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
1
IFE1
Interrupt Filter Enable 1
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
0
IFE0
Interrupt Filter Enable 0
Enables the digital glitch filter on the interrupt pad input.
0b - Disable
1b - Enable
10.6.10 Interrupt Filter Maximum Counter (IFMCR0 - IFMCR31)
Offset
For a = 0 to 31:
Register
Offset
IFMCRa
40h + (a × 4h)
Function
Configures the filter counter associated with each of the digital glitch filter and supports only 32-bit accesses. It does not support 
byte and halfword accesses.
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
393 / 5251


---
# 페이지 343

Diagram
Bits
31
30
29
28
27
26
25
24
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
MAXCNT 
W
Reset
0
0
0
0
0
0
0
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
MAXCNT
Maximum Interrupt Filter Counter Setting
Specifies the settings of the maximum interrupt filter counter.
The value of this field varies between 0d – 15d. Based on its value, it exhibits the following settings:
• A value of 0d, 1d, or 2d sets the filter as an all pass filter
• A value of 3d to 15d sets the filter period to TCK × MAXCNT + n × TCK, where:
— n is 1, 2, 3, or 4 (n accounts for the uncertainty factor in filter period calculation)
— TCK is the prescaled filter clock period, which is the IRC clock prescaled to the IFCP value 
specified in IFCPR
10.6.11 Interrupt Filter Clock Prescaler (IFCPR)
Offset
Register
Offset
IFCPR
C0h
Function
Configures the clock prescaler that selects the clock for all digital filters and supports only 32-bit accesses. Byte and half-word 
accesses are not supported. A prescaler is applied to the input clock to SIUL2, which is the peripheral clock counter in SIUL2.
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
394 / 5251


---
# 페이지 344

Diagram
Bits
31
30
29
28
27
26
25
24
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
IFCP 
W
Reset
0
0
0
0
0
0
0
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
IFCP
Interrupt Filter Clock Prescaler Setting
Specifies the settings of the interrupt filter clock prescaler.
The prescaled filter clock period is determined by TIRC × (IFCP + 1), where:
• TIRC is the internal oscillator period
• IFCP is 0 to 15
10.6.12 MUX0 EMIOS ENABLE 1 (MUX0_EMIOS_EN1)
Offset
Register
Offset
MUX0_EMIOS_EN1
100h
Function
 
This register is reserved for S32K3x4.
  NOTE  
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
395 / 5251


---
# 페이지 345

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
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
Reserved 
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
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
31
EMIOSFLG15_
EN
EMIOS0 Output Flag 15 Monitor Enable
30
EMIOSFLG14_
EN
EMIOS0 Output Flag 14 Monitor Enable
29
EMIOSFLG13_
EN
EMIOS0 Output Flag 13 Monitor Enable
28
EMIOSFLG12_
EN
EMIOS0 Output Flag 12 Monitor Enable
27
EMIOSFLG11_
EN
EMIOS0 Output Flag 11 Monitor Enable
26
EMIOSFLG10_
EN
EMIOS0 Output Flag 10 Monitor Enable
25
EMIOSFLG9_E
N
EMIOS0 Output Flag 9 Monitor Enable
24
EMIOSFLG8_E
N
EMIOS0 Output Flag 8 Monitor Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
396 / 5251


---
# 페이지 346

Table continued from the previous page...
Field
Function
23
EMIOSFLG7_E
N
EMIOS0 Output Flag 7 Monitor Enable
22
EMIOSFLG6_E
N
EMIOS0 Output Flag 6 Monitor Enable
21
EMIOSFLG5_E
N
EMIOS0 Output Flag 5 Monitor Enable
20
EMIOSFLG4_E
N
EMIOS0 Output Flag 4 Monitor Enable
19
EMIOSFLG3_E
N
EMIOS0 Output Flag 3 Monitor Enable
18
EMIOSFLG2_E
N
EMIOS0 Output Flag 2 Monitor Enable
17
EMIOSFLG1_E
N
EMIOS0 Output Flag 1 Monitor Enable
16
EMIOSFLG0_E
N
EMIOS0 Output Flag 0 Monitor Enable
15-8
—
Reserved
7
EMIOSFLG23_
EN
EMIOS0 Output Flag 23 Monitor Enable
6
EMIOSFLG22_
EN
EMIOS0 Output Flag 22 Monitor Enable
5
EMIOS0 Output Flag 21 Monitor Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
397 / 5251


---
# 페이지 347

Table continued from the previous page...
Field
Function
EMIOSFLG21_
EN
4
EMIOSFLG20_
EN
EMIOS0 Output Flag 20 Monitor Enable
3
EMIOSFLG19_
EN
EMIOS0 Output Flag 19 Monitor Enable
2
EMIOSFLG18_
EN
EMIOS0 Output Flag 18 Monitor Enable
1
EMIOSFLG17_
EN
EMIOS0 Output Flag 17 Monitor Enable
0
EMIOSFLG16_
EN
EMIOS0 Output Flag 16 Monitor Enable
10.6.13 MUX0 MISC ENABLE (MUX0_MISC_EN)
Offset
Register
Offset
MUX0_MISC_EN
104h
Function
 
This register is reserved for S32K3x4.
  NOTE  
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
398 / 5251


---
# 페이지 348

Diagram
Bits
31
30
29
28
27
26
25
24
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
BCTU
ADC...
BCTU
ADC...
BCTU
ADC...
BCTU
LIS...
BCTU
FIF...
BCTU
FIF...
BCTU
ADC...
BCTU
ADC...
BCTU
ADC...
BCTU
FIF...
BCTU
FIF...
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
Reserved 
LPUA
RT3...
LPUA
RT2...
LPUA
RT1...
LPUA
RT0...
Reserved 
ADC2
EOC...
ADC1
EOC...
ADC0
EOC...
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
31-27
—
Reserved
26
BCTUADC2INT
_EN
BCTU ADC2DR Interrupt Request Monitor Enable
25
BCTUADC1INT
_EN
BCTU ADC1DR Interrupt Request Monitor Enable
24
BCTUADC0INT
_EN
BCTU ADC0DR Interrupt Request Monitor Enable
23
BCTULISTINT_
EN
BCTU Conversion List Interrupt Request Enable
22
BCTUFIFO1INT
_EN
BCTU FIFO0 Interrupt Request Monitor Enable
21
BCTUFIFO0INT
_EN
BCTU FIFO0 Interrupt Request Monitor Enable
20
BCTUADC2DM
A_EN
BCTU ADC2DR DMA Request Monitor Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
399 / 5251


---
# 페이지 349

Table continued from the previous page...
Field
Function
19
BCTUADC1DM
A_EN
BCTU ADC1DR DMA Request Monitor Enable
18
BCTUADC0DM
A_EN
BCTU ADC0DR DMA Request Monitor Enable
17
BCTUFIFO1DM
A_EN
BCTU FIFO1 DMA Request Monitor Enable
16
BCTUFIFO0DM
A_EN
BCTU FIFO0 DMA Request Monitor Enable
15-12
—
Reserved
11
LPUART3TRG_
EN
LPUART3 Output Trigger Monitor Enable
10
LPUART2TRG_
EN
LPUART2 Output Trigger Monitor Enable
9
LPUART1TRG_
EN
LPUART1 Output Trigger Monitor Enable
8
LPUART0TRG_
EN
LPUART0 Output Trigger Monitor Enable
7-3
—
Reserved
2
ADC2EOC_EN
ADC2 End of Conversion Trigger Monitor
1
ADC1EOC_EN
ADC1 End of Conversion Trigger Monitor
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
400 / 5251


---
# 페이지 350

Table continued from the previous page...
Field
Function
0
ADC0EOC_EN
ADC0 End of Conversion Trigger Monitor
10.6.14 MUX1 EMIOS ENABLE (MUX1_EMIOS_EN)
Offset
Register
Offset
MUX1_EMIOS_EN
108h
Function
 
This register is reserved for S32K3x4.
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
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
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
Reserved 
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
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
31
EMIOSFLG15_
EN
EMIOS0 Output Flag 15 Monitor Enable
30
EMIOSFLG14_
EN
EMIOS0 Output Flag 14 Monitor Enable
29
EMIOS0 Output Flag 13 Monitor Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
401 / 5251


---
# 페이지 351

Table continued from the previous page...
Field
Function
EMIOSFLG13_
EN
28
EMIOSFLG12_
EN
EMIOS0 Output Flag 12 Monitor Enable
27
EMIOSFLG11_
EN
EMIOS0 Output Flag 11 Monitor Enable
26
EMIOSFLG10_
EN
EMIOS0 Output Flag 10 Monitor Enable
25
EMIOSFLG9_E
N
EMIOS0 Output Flag 9 Monitor Enable
24
EMIOSFLG8_E
N
EMIOS0 Output Flag 8 Monitor Enable
23
EMIOSFLG7_E
N
EMIOS0 Output Flag 7 Monitor Enable
22
EMIOSFLG6_E
N
EMIOS0 Output Flag 6 Monitor Enable
21
EMIOSFLG5_E
N
EMIOS0 Output Flag 5 Monitor Enable
20
EMIOSFLG4_E
N
EMIOS0 Output Flag 4 Monitor Enable
19
EMIOSFLG3_E
N
EMIOS0 Output Flag 3 Monitor Enable
18
EMIOS0 Output Flag 2 Monitor Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
402 / 5251


---
# 페이지 352

Table continued from the previous page...
Field
Function
EMIOSFLG2_E
N
17
EMIOSFLG1_E
N
EMIOS0 Output Flag 1 Monitor Enable
16
EMIOSFLG0_E
N
EMIOS0 Output Flag 0 Monitor Enable
15-8
—
Reserved
7
EMIOSFLG23_
EN
EMIOS0 Output Flag 23 Monitor Enable
6
EMIOSFLG22_
EN
EMIOS0 Output Flag 22 Monitor Enable
5
EMIOSFLG21_
EN
EMIOS0 Output Flag 21 Monitor Enable
4
EMIOSFLG20_
EN
EMIOS0 Output Flag 20 Monitor Enable
3
EMIOSFLG19_
EN
EMIOS0 Output Flag 19 Monitor Enable
2
EMIOSFLG18_
EN
EMIOS0 Output Flag 18 Monitor Enable
1
EMIOSFLG17_
EN
EMIOS0 Output Flag 17 Monitor Enable
0
EMIOS0 Output Flag 16 Monitor Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
403 / 5251


---
# 페이지 353

Table continued from the previous page...
Field
Function
EMIOSFLG16_
EN
10.6.15 MUX1 MISC ENABLE (MUX1_MISC_EN)
Offset
Register
Offset
MUX1_MISC_EN
10Ch
Function
 
This register is reserved for S32K3x4.
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
Reserved 
BCTU
ADC...
BCTU
ADC...
BCTU
ADC...
BCTU
LIS...
BCTU
FIF...
BCTU
FIF...
BCTU
ADC...
BCTU
ADC...
BCTU
ADC...
BCTU
FIF...
BCTU
FIF...
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
Reserved 
LPUA
RT3...
LPUA
RT2...
LPUA
RT1...
LPUA
RT0...
Reserved 
ADC2
EOC...
ADC1
EOC...
ADC0
EOC...
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
31-27
—
Reserved
26
BCTUADC2INT
_EN
BCTU ADC2DR Interrupt Request Monitor Enable
25
BCTUADC1INT
_EN
BCTU ADC1DR Interrupt Request Monitor Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
404 / 5251


---
# 페이지 354

Table continued from the previous page...
Field
Function
24
BCTUADC0INT
_EN
BCTU ADC0DR Interrupt Request Monitor Enable
23
BCTULISTINT_
EN
BCTU Conversion List Interrupt Request Enable
22
BCTUFIFO1INT
_EN
BCTU FIFO0 Interrupt Request Monitor Enable
21
BCTUFIFO0INT
_EN
BCTU FIFO0 Interrupt Request Monitor Enable
20
BCTUADC2DM
A_EN
BCTU ADC2DR DMA Request Monitor Enable
19
BCTUADC1DM
A_EN
BCTU ADC1DR DMA Request Monitor Enable
18
BCTUADC0DM
A_EN
BCTU ADC0DR DMA Request Monitor Enable
17
BCTUFIFO1DM
A_EN
BCTU FIFO1 DMA Request Monitor Enable
16
BCTUFIFO0DM
A_EN
BCTU FIFO0 DMA Request Monitor Enable
15-12
—
Reserved
11
LPUART3TRG_
EN
LPUART3 Output Trigger Monitor Enable
10
LPUART2 Output Trigger Monitor Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
405 / 5251


---
# 페이지 355

Table continued from the previous page...
Field
Function
LPUART2TRG_
EN
9
LPUART1TRG_
EN
LPUART1 Output Trigger Monitor Enable
8
LPUART0TRG_
EN
LPUART0 Output Trigger Monitor Enable
7-3
—
Reserved
2
ADC2EOC_EN
ADC2 End of Conversion Trigger Monitor
1
ADC1EOC_EN
ADC1 End of Conversion Trigger Monitor
0
ADC0EOC_EN
ADC0 End of Conversion Trigger Monitor
10.6.16 MUX2 EMIOS ENABLE (MUX2_EMIOS_EN)
Offset
Register
Offset
MUX2_EMIOS_EN
110h
Function
 
This register is reserved for S32K3x4, S32K310, S32K311, S32K312, S32K322, S32K341 and S32K342.
  NOTE  
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
406 / 5251


---
# 페이지 356

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
EMIO
SFL...
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
Reserved 
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
EMIOS
FL...
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
31
EMIOSFLG15_
EN
EMIOS0 Output Flag 15 Monitor Enable
30
EMIOSFLG14_
EN
EMIOS0 Output Flag 14 Monitor Enable
29
EMIOSFLG13_
EN
EMIOS0 Output Flag 13 Monitor Enable
28
EMIOSFLG12_
EN
EMIOS0 Output Flag 12 Monitor Enable
27
EMIOSFLG11_
EN
EMIOS0 Output Flag 11 Monitor Enable
26
EMIOSFLG10_
EN
EMIOS0 Output Flag 10 Monitor Enable
25
EMIOSFLG9_E
N
EMIOS0 Output Flag 9 Monitor Enable
24
EMIOSFLG8_E
N
EMIOS0 Output Flag 8 Monitor Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
407 / 5251


---
# 페이지 357

Table continued from the previous page...
Field
Function
23
EMIOSFLG7_E
N
EMIOS0 Output Flag 7 Monitor Enable
22
EMIOSFLG6_E
N
EMIOS0 Output Flag 6 Monitor Enable
21
EMIOSFLG5_E
N
EMIOS0 Output Flag 5 Monitor Enable
20
EMIOSFLG4_E
N
EMIOS0 Output Flag 4 Monitor Enable
19
EMIOSFLG3_E
N
EMIOS0 Output Flag 3 Monitor Enable
18
EMIOSFLG2_E
N
EMIOS0 Output Flag 2 Monitor Enable
17
EMIOSFLG1_E
N
EMIOS0 Output Flag 1 Monitor Enable
16
EMIOSFLG0_E
N
EMIOS0 Output Flag 0 Monitor Enable
15-8
—
Reserved
7
EMIOSFLG23_
EN
EMIOS0 Output Flag 23 Monitor Enable
6
EMIOSFLG22_
EN
EMIOS0 Output Flag 22 Monitor Enable
5
EMIOS0 Output Flag 21 Monitor Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
408 / 5251


---
# 페이지 358

Table continued from the previous page...
Field
Function
EMIOSFLG21_
EN
4
EMIOSFLG20_
EN
EMIOS0 Output Flag 20 Monitor Enable
3
EMIOSFLG19_
EN
EMIOS0 Output Flag 19 Monitor Enable
2
EMIOSFLG18_
EN
EMIOS0 Output Flag 18 Monitor Enable
1
EMIOSFLG17_
EN
EMIOS0 Output Flag 17 Monitor Enable
0
EMIOSFLG16_
EN
EMIOS0 Output Flag 16 Monitor Enable
10.6.17 MUX2 MISC ENABLE (MUX2_MISC_EN)
Offset
Register
Offset
MUX2_MISC_EN
114h
Function
 
This register is reserved for S32K3x4, S32K310, S32K311, S32K312, S32K322, S32K341 and S32K342.
  NOTE  
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
409 / 5251


---
# 페이지 359

Diagram
Bits
31
30
29
28
27
26
25
24
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
BCTU
ADC...
BCTU
ADC...
BCTU
ADC...
BCTU
LIS...
BCTU
FIF...
BCTU
FIF...
BCTU
ADC...
BCTU
ADC...
BCTU
ADC...
BCTU
FIF...
BCTU
FIF...
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
Reserved 
LPUA
RT3...
LPUA
RT2...
LPUA
RT1...
LPUA
RT0...
Reserved 
ADC2
EOC...
ADC1
EOC...
ADC0
EOC...
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
31-27
—
Reserved
26
BCTUADC2INT
_EN
BCTU ADC2DR Interrupt Request Monitor Enable
25
BCTUADC1INT
_EN
BCTU ADC1DR Interrupt Request Monitor Enable
24
BCTUADC0INT
_EN
BCTU ADC0DR Interrupt Request Monitor Enable
23
BCTULISTINT_
EN
BCTU Conversion List Interrupt Request Enable
22
BCTUFIFO1INT
_EN
BCTU FIFO0 Interrupt Request Monitor Enable
21
BCTUFIFO0INT
_EN
BCTU FIFO0 Interrupt Request Monitor Enable
20
BCTUADC2DM
A_EN
BCTU ADC2DR DMA Request Monitor Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
410 / 5251


---
# 페이지 360

Table continued from the previous page...
Field
Function
19
BCTUADC1DM
A_EN
BCTU ADC1DR DMA Request Monitor Enable
18
BCTUADC0DM
A_EN
BCTU ADC0DR DMA Request Monitor Enable
17
BCTUFIFO1DM
A_EN
BCTU FIFO1 DMA Request Monitor Enable
16
BCTUFIFO0DM
A_EN
BCTU FIFO0 DMA Request Monitor Enable
15-12
—
Reserved
11
LPUART3TRG_
EN
LPUART3 Output Trigger Monitor Enable
10
LPUART2TRG_
EN
LPUART2 Output Trigger Monitor Enable
9
LPUART1TRG_
EN
LPUART1 Output Trigger Monitor Enable
8
LPUART0TRG_
EN
LPUART0 Output Trigger Monitor Enable
7-3
—
Reserved
2
ADC2EOC_EN
ADC2 End of Conversion Trigger Monitor
1
ADC1EOC_EN
ADC1 End of Conversion Trigger Monitor
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
411 / 5251


---
# 페이지 361

Table continued from the previous page...
Field
Function
0
ADC0EOC_EN
ADC0 End of Conversion Trigger Monitor
10.6.18 SIUL2 MCU ID Register #3 (MIDR3)
Offset
Register
Offset
MIDR3
200h
Function
 
This register supports only 32-bit accesses. Byte and half-word accesses are not supported.
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
PROD_FAM_LET 
PROD_FAM_NO 
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
PART_NO_SUF 
0
SYS_RAM_SIZE 
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
31-26
PROD_FAM_LE
T
Product Family Letter
Identifies the product family letter.
01_0011b - S
25-16
PROD_FAM_N
O
Product Family Number
Identifies the product family number.
00_0010_0000b - 32
15-10
Part Number Suffix
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
412 / 5251


---
# 페이지 362

Table continued from the previous page...
Field
Function
PART_NO_SUF Describes the part number suffix.
00_0000b - None
9-6
—
Reserved
5-0
SYS_RAM_SIZ
E
System RAM Size
Total RAM size in SoC, including TCMs.
00_0010b - 128 kB
00_0011b - 192 kB
00_0100b - 256 kB
00_0110b - 512 kB
00_1100b - 1152 kB
10.6.19 SIUL2 MCU ID Register #4 (MIDR4)
Offset
Register
Offset
MIDR4
204h
Function
 
This register supports only 32-bit accesses. Byte and half-word accesses are not supported.
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
CORE_PLAT_F
ET_1 
0
CORE_PLAT_FET_2 
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
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
413 / 5251


---
# 페이지 363

Fields
Field
Function
31-16
—
Reserved
15-14
CORE_PLAT_F
ET_1
Core Platform Options Feature
Core platform options feature.
 
The 5-bit field is a concatenation of bits 15-14 (CORE_PLAT_FET_1) and 
2-0 (CORE_PLAT_FET_2).
  NOTE  
00000b
1x M7 core
00001b
2x M7 cores
00010b
1x M7 LS core
00011b
1x M7 LS core + 1x M7 core
00100b
3x M7 cores
01001b
2x M7 LS cores + 1x M7 core or 1x M7 LS core + 3x 
M7 cores
13-3
—
Reserved
2-0
CORE_PLAT_F
ET_2
Core Platform Options Feature
Core platform options feature. For field values see description of CORE_PLAT_FET_1
10.6.20 Multiplexed Signal Configuration (MSCR0 - MSCR323)
Offset
Register
Offset
MSCR0
240h
MSCR1
244h
MSCR2
248h
MSCR3
24Ch
MSCR4
250h
MSCR5
254h
MSCR6
258h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
414 / 5251


---
# 페이지 364

Table continued from the previous page...
Register
Offset
MSCR7
25Ch
MSCR8
260h
MSCR9
264h
MSCR10
268h
MSCR11
26Ch
MSCR12
270h
MSCR13
274h
MSCR14
278h
MSCR15
27Ch
MSCR16
280h
MSCR17
284h
MSCR18
288h
MSCR19
28Ch
MSCR20
290h
MSCR21
294h
MSCR22
298h
MSCR23
29Ch
MSCR24
2A0h
MSCR25
2A4h
MSCR26
2A8h
MSCR27
2ACh
MSCR28
2B0h
MSCR29
2B4h
MSCR30
2B8h
MSCR31
2BCh
MSCR32
2C0h
MSCR33
2C4h
MSCR34
2C8h
MSCR35
2CCh
MSCR36
2D0h
MSCR37
2D4h
MSCR40
2E0h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
415 / 5251


---
# 페이지 365

Table continued from the previous page...
Register
Offset
MSCR41
2E4h
MSCR42
2E8h
MSCR43
2ECh
MSCR44
2F0h
MSCR45
2F4h
MSCR46
2F8h
MSCR47
2FCh
MSCR48
300h
MSCR49
304h
MSCR50
308h
MSCR51
30Ch
MSCR52
310h
MSCR53
314h
MSCR54
318h
MSCR55
31Ch
MSCR56
320h
MSCR57
324h
MSCR58
328h
MSCR59
32Ch
MSCR60
330h
MSCR61
334h
MSCR62
338h
MSCR63
33Ch
MSCR64
340h
MSCR65
344h
MSCR66
348h
MSCR67
34Ch
MSCR68
350h
MSCR69
354h
MSCR70
358h
MSCR71
35Ch
MSCR72
360h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
416 / 5251


---
# 페이지 366

Table continued from the previous page...
Register
Offset
MSCR73
364h
MSCR74
368h
MSCR75
36Ch
MSCR76
370h
MSCR77
374h
MSCR78
378h
MSCR79
37Ch
MSCR80
380h
MSCR81
384h
MSCR82
388h
MSCR83
38Ch
MSCR84
390h
MSCR85
394h
MSCR86
398h
MSCR87
39Ch
MSCR88
3A0h
MSCR89
3A4h
MSCR90
3A8h
MSCR91
3ACh
MSCR92
3B0h
MSCR93
3B4h
MSCR94
3B8h
MSCR95
3BCh
MSCR96
3C0h
MSCR97
3C4h
MSCR98
3C8h
MSCR99
3CCh
MSCR100
3D0h
MSCR101
3D4h
MSCR102
3D8h
MSCR103
3DCh
MSCR104
3E0h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
417 / 5251


---
# 페이지 367

Table continued from the previous page...
Register
Offset
MSCR105
3E4h
MSCR106
3E8h
MSCR107
3ECh
MSCR108
3F0h
MSCR109
3F4h
MSCR110
3F8h
MSCR111
3FCh
MSCR112
400h
MSCR113
404h
MSCR114
408h
MSCR115
40Ch
MSCR116
410h
MSCR117
414h
MSCR118
418h
MSCR119
41Ch
MSCR120
420h
MSCR121
424h
MSCR122
428h
MSCR123
42Ch
MSCR124
430h
MSCR125
434h
MSCR126
438h
MSCR127
43Ch
MSCR128
440h
MSCR129
444h
MSCR130
448h
MSCR131
44Ch
MSCR132
450h
MSCR133
454h
MSCR134
458h
MSCR135
45Ch
MSCR136
460h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
418 / 5251


---
# 페이지 368

Table continued from the previous page...
Register
Offset
MSCR137
464h
MSCR138
468h
MSCR139
46Ch
MSCR140
470h
MSCR142
478h
MSCR143
47Ch
MSCR144
480h
MSCR145
484h
MSCR146
488h
MSCR147
48Ch
MSCR148
490h
MSCR149
494h
MSCR150
498h
MSCR151
49Ch
MSCR152
4A0h
MSCR153
4A4h
MSCR154
4A8h
MSCR155
4ACh
MSCR156
4B0h
MSCR157
4B4h
MSCR158
4B8h
MSCR159
4BCh
MSCR160
4C0h
MSCR161
4C4h
MSCR162
4C8h
MSCR163
4CCh
MSCR164
4D0h
MSCR165
4D4h
MSCR166
4D8h
MSCR167
4DCh
MSCR168
4E0h
MSCR169
4E4h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
419 / 5251


---
# 페이지 369

Table continued from the previous page...
Register
Offset
MSCR170
4E8h
MSCR171
4ECh
MSCR172
4F0h
MSCR173
4F4h
MSCR174
4F8h
MSCR175
4FCh
MSCR176
500h
MSCR177
504h
MSCR178
508h
MSCR179
50Ch
MSCR180
510h
MSCR181
514h
MSCR182
518h
MSCR183
51Ch
MSCR184
520h
MSCR185
524h
MSCR186
528h
MSCR187
52Ch
MSCR188
530h
MSCR189
534h
MSCR190
538h
MSCR191
53Ch
MSCR192
540h
MSCR193
544h
MSCR194
548h
MSCR195
54Ch
MSCR196
550h
MSCR197
554h
MSCR198
558h
MSCR199
55Ch
MSCR200
560h
MSCR201
564h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
420 / 5251


---
# 페이지 370

Table continued from the previous page...
Register
Offset
MSCR202
568h
MSCR203
56Ch
MSCR204
570h
MSCR205
574h
MSCR206
578h
MSCR207
57Ch
MSCR208
580h
MSCR209
584h
MSCR210
588h
MSCR211
58Ch
MSCR212
590h
MSCR213
594h
MSCR214
598h
MSCR215
59Ch
MSCR216
5A0h
MSCR217
5A4h
MSCR218
5A8h
MSCR219
5ACh
MSCR220
5B0h
MSCR221
5B4h
MSCR222
5B8h
MSCR223
5BCh
MSCR224
5C0h
MSCR225
5C4h
MSCR226
5C8h
MSCR227
5CCh
MSCR228
5D0h
MSCR229
5D4h
MSCR230
5D8h
MSCR231
5DCh
MSCR232
5E0h
MSCR233
5E4h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
421 / 5251


---
# 페이지 371

Table continued from the previous page...
Register
Offset
MSCR234
5E8h
MSCR235
5ECh
MSCR236
5F0h
MSCR237
5F4h
MSCR238
5F8h
MSCR239
5FCh
MSCR240
600h
MSCR241
604h
MSCR242
608h
MSCR243
60Ch
MSCR244
610h
MSCR245
614h
MSCR246
618h
MSCR247
61Ch
MSCR248
620h
MSCR249
624h
MSCR250
628h
MSCR251
62Ch
MSCR252
630h
MSCR253
634h
MSCR254
638h
MSCR255
63Ch
MSCR256
640h
MSCR257
644h
MSCR258
648h
MSCR259
64Ch
MSCR260
650h
MSCR261
654h
MSCR262
658h
MSCR263
65Ch
MSCR264
660h
MSCR265
664h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
422 / 5251


---
# 페이지 372

Table continued from the previous page...
Register
Offset
MSCR266
668h
MSCR267
66Ch
MSCR268
670h
MSCR269
674h
MSCR270
678h
MSCR271
67Ch
MSCR272
680h
MSCR273
684h
MSCR274
688h
MSCR275
68Ch
MSCR276
690h
MSCR277
694h
MSCR278
698h
MSCR279
69Ch
MSCR280
6A0h
MSCR281
6A4h
MSCR282
6A8h
MSCR283
6ACh
MSCR284
6B0h
MSCR285
6B4h
MSCR286
6B8h
MSCR287
6BCh
MSCR288
6C0h
MSCR289
6C4h
MSCR290
6C8h
MSCR291
6CCh
MSCR292
6D0h
MSCR293
6D4h
MSCR294
6D8h
MSCR295
6DCh
MSCR296
6E0h
MSCR297
6E4h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
423 / 5251


---
# 페이지 373

Table continued from the previous page...
Register
Offset
MSCR298
6E8h
MSCR299
6ECh
MSCR300
6F0h
MSCR301
6F4h
MSCR302
6F8h
MSCR303
6FCh
MSCR304
700h
MSCR305
704h
MSCR306
708h
MSCR307
70Ch
MSCR308
710h
MSCR309
714h
MSCR310
718h
MSCR311
71Ch
MSCR312
720h
MSCR313
724h
MSCR314
728h
MSCR315
72Ch
MSCR316
730h
MSCR317
734h
MSCR318
738h
MSCR319
73Ch
MSCR320
740h
MSCR321
744h
MSCR322
748h
MSCR323
74Ch
Function
Selects the source signal connected to the register's associated destination, which is a chip output pin or a chip pin that can be 
configured as an output. It also specifies the electrical properties of the associated pin.
This register supports only 32-bit accesses. Byte and half-word write accesses are not supported.
For chip-pin MSCR assignments and pin types, see the IOMUX file attached to this document.
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
424 / 5251


---
# 페이지 374

 
• Configure these registers only during application initialization; you must not modify them during 
application runtime.
• Accessing a reserved MSCRn register generates a transfer error.
• These registers are a part of the SIUL memory map but the physical implementation of these registers is a part 
of the IOMUX RTL.
• SIUL2 interprets accesses to MSCRn at the module level.
  NOTE  
Internal connections
Destination (module port)
Module-port IMCR
Input port
Module 0
Output port
Input buffer
Input buffer
Destination (chip pin)
Pin a
Pin b
Output 
buffer
Output port
Module n
Output port
Chip-pin MSCR
Figure 26. MSCR and IMCR port and pin connection
Diagram
Bits
31
30
29
28
27
26
25
24
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
OBE 
0
IBE 
0
INV 
PKE 
W
Reset
See Register reset values.
Bits
15
14
13
12
11
10
9
8
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
SRC 
PUE 
0
PUS 
0
DSE 
0
IFE 
SMC 
0
SSS_3 
SSS_2 
SSS_1 
SSS_0 
W
Reset
See Register reset values.
Register reset values
Register
Reset value
MSCR0–MSCR3
0000_0000h
MSCR4
0008_2827h
MSCR5–MSCR9
0000_0000h
MSCR10
0000_0127h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
425 / 5251


---
# 페이지 375

Table continued from the previous page...
Register
Reset value
MSCR11
0000_0000h
MSCR12
0000_0003h
MSCR13–MSCR65
0000_0000h
MSCR38–MSCR39
Register not supported
MSCR66–MSCR67
0000_4000h
MSCR68
0008_2000h
MSCR69
0008_2800h
MSCR70–MSCR75
0000_0000h
MSCR76
0000_4000h
MSCR77–MSCR79
0000_0000h
MSCR80
0000_4000h
MSCR81–MSCR100
0000_0000h
MSCR101–MSCR103
0000_4000h
MSCR104–MSCR105
0000_0000h
MSCR106–MSCR108
0000_4000h
MSCR109–MSCR135
0000_0000h
MSCR136
0000_4000h
MSCR137–MSCR323
0000_0000h
MSCR141
Register not supported
Fields
Field
Function
31-22
—
Reserved
21
OBE
GPIO Output Buffer Enable
Applies only to digital pins. Otherwise this bit is reserved.
0b - Output driver disabled
1b - Output driver enabled
20
—
Reserved
19
Input Buffer Enable
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
426 / 5251


---
# 페이지 376

Table continued from the previous page...
Field
Function
IBE
Used only when the associated destination is a chip pin. Enables the associated pin's input buffer.
0b - Disabled
1b - Enabled
18
—
Reserved
17
INV
Invert
Inverts the signal selected by SSS before transmitting it to the associated destination (chip pin or module 
port).
0b - Don't invert
1b - Invert
16
PKE
Pad keeping enable
Pad keeping enable
0b - Disabled
1b - Enabled
15
—
Reserved
14
SRC
Slew Rate Control
0b - Fastest setting
1b - Slowest setting
13
PUE
Pull Enable
Enables the pull function. Used only when the associated destination is a chip pin.
0b - Disabled
1b - Enabled
12
—
Reserved
11
PUS
Pull Select
Determines whether the pull function is a pullup or pulldown when the pull function is enabled by the 
PUE field. Used only when the associated destination is a chip pin.
0b - Pull down
1b - Pull up
10-9
Reserved
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
427 / 5251


---
# 페이지 377

Table continued from the previous page...
Field
Function
—
8
DSE
DSE
Drive strength enable
0b - Disabled
1b - Enabled
7
—
Reserved
6
IFE
IFE
Input filter enable
 
This field is supported for RESET pad only (PTA5).
  NOTE  
0b - Disabled
1b - Enabled
5
SMC
Safe Mode Control
Used only when the associated destination is a chip pin. Specifies whether the chip disables the pin's 
output buffer when the chip enters Safe mode.
0b - Disable (The output buffer returns to its previous state when the chip leaves Safe mode.)
1b - Don't disable
4
—
Reserved
3
SSS_3
Source Signal Select_3
Selects a function for the pad. Refer to "SSS" column of the 'IO Signal Table' tab of the IOMUX 
spreadsheet attachment.
2
SSS_2
Source Signal Select_2
Selects a function for the pad. Refer to "SSS" column of the 'IO Signal Table' tab of the IOMUX 
spreadsheet attachment.
1
SSS_1
Source Signal Select_1
Selects a function for the pad. Refer to "SSS" column of the 'IO Signal Table' tab of the IOMUX 
spreadsheet attachment.
0
SSS_0
Source Signal Select_0
Selects a function for the pad. Refer to "SSS" column of the 'IO Signal Table' tab of the IOMUX 
spreadsheet attachment.
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
428 / 5251


---
# 페이지 378

10.6.21 Input Multiplexed Signal Configuration (IMCR0 - IMCR473)
Offset
Register
Offset
IMCR0
A40h
IMCR1
A44h
IMCR2
A48h
IMCR3
A4Ch
IMCR4
A50h
IMCR5
A54h
IMCR16
A80h
IMCR17
A84h
IMCR18
A88h
IMCR19
A8Ch
IMCR20
A90h
IMCR21
A94h
IMCR22
A98h
IMCR23
A9Ch
IMCR24
AA0h
IMCR25
AA4h
IMCR26
AA8h
IMCR27
AACh
IMCR28
AB0h
IMCR29
AB4h
IMCR30
AB8h
IMCR31
ABCh
IMCR32
AC0h
IMCR33
AC4h
IMCR34
AC8h
IMCR35
ACCh
IMCR36
AD0h
IMCR37
AD4h
IMCR38
AD8h
IMCR39
ADCh
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
429 / 5251


---
# 페이지 379

Table continued from the previous page...
Register
Offset
IMCR40
AE0h
IMCR41
AE4h
IMCR42
AE8h
IMCR43
AECh
IMCR44
AF0h
IMCR45
AF4h
IMCR46
AF8h
IMCR47
AFCh
IMCR48
B00h
IMCR49
B04h
IMCR50
B08h
IMCR51
B0Ch
IMCR52
B10h
IMCR53
B14h
IMCR54
B18h
IMCR55
B1Ch
IMCR56
B20h
IMCR57
B24h
IMCR58
B28h
IMCR59
B2Ch
IMCR60
B30h
IMCR61
B34h
IMCR62
B38h
IMCR63
B3Ch
IMCR64
B40h
IMCR65
B44h
IMCR66
B48h
IMCR67
B4Ch
IMCR68
B50h
IMCR69
B54h
IMCR70
B58h
IMCR71
B5Ch
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
430 / 5251


---
# 페이지 380

Table continued from the previous page...
Register
Offset
IMCR80
B80h
IMCR81
B84h
IMCR82
B88h
IMCR83
B8Ch
IMCR84
B90h
IMCR85
B94h
IMCR86
B98h
IMCR87
B9Ch
IMCR88
BA0h
IMCR89
BA4h
IMCR90
BA8h
IMCR91
BACh
IMCR92
BB0h
IMCR93
BB4h
IMCR94
BB8h
IMCR95
BBCh
IMCR96
BC0h
IMCR97
BC4h
IMCR98
BC8h
IMCR99
BCCh
IMCR100
BD0h
IMCR101
BD4h
IMCR102
BD8h
IMCR103
BDCh
IMCR112
C00h
IMCR113
C04h
IMCR114
C08h
IMCR115
C0Ch
IMCR116
C10h
IMCR117
C14h
IMCR118
C18h
IMCR119
C1Ch
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
431 / 5251


---
# 페이지 381

Table continued from the previous page...
Register
Offset
IMCR120
C20h
IMCR121
C24h
IMCR122
C28h
IMCR123
C2Ch
IMCR124
C30h
IMCR125
C34h
IMCR126
C38h
IMCR127
C3Ch
IMCR128
C40h
IMCR129
C44h
IMCR130
C48h
IMCR131
C4Ch
IMCR132
C50h
IMCR133
C54h
IMCR134
C58h
IMCR135
C5Ch
IMCR144
C80h
IMCR145
C84h
IMCR146
C88h
IMCR147
C8Ch
IMCR148
C90h
IMCR149
C94h
IMCR152
CA0h
IMCR153
CA4h
IMCR154
CA8h
IMCR155
CACh
IMCR156
CB0h
IMCR157
CB4h
IMCR158
CB8h
IMCR159
CBCh
IMCR160
CC0h
IMCR161
CC4h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
432 / 5251


---
# 페이지 382

Table continued from the previous page...
Register
Offset
IMCR162
CC8h
IMCR163
CCCh
IMCR164
CD0h
IMCR165
CD4h
IMCR166
CD8h
IMCR167
CDCh
IMCR168
CE0h
IMCR169
CE4h
IMCR170
CE8h
IMCR171
CECh
IMCR172
CF0h
IMCR173
CF4h
IMCR174
CF8h
IMCR175
CFCh
IMCR176
D00h
IMCR177
D04h
IMCR178
D08h
IMCR179
D0Ch
IMCR180
D10h
IMCR181
D14h
IMCR182
D18h
IMCR183
D1Ch
IMCR184
D20h
IMCR185
D24h
IMCR186
D28h
IMCR187
D2Ch
IMCR188
D30h
IMCR189
D34h
IMCR190
D38h
IMCR191
D3Ch
IMCR192
D40h
IMCR193
D44h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
433 / 5251


---
# 페이지 383

Table continued from the previous page...
Register
Offset
IMCR194
D48h
IMCR195
D4Ch
IMCR196
D50h
IMCR197
D54h
IMCR198
D58h
IMCR199
D5Ch
IMCR200
D60h
IMCR201
D64h
IMCR202
D68h
IMCR211
D8Ch
IMCR212
D90h
IMCR213
D94h
IMCR214
D98h
IMCR215
D9Ch
IMCR216
DA0h
IMCR217
DA4h
IMCR218
DA8h
IMCR219
DACh
IMCR220
DB0h
IMCR221
DB4h
IMCR222
DB8h
IMCR223
DBCh
IMCR224
DC0h
IMCR225
DC4h
IMCR226
DC8h
IMCR227
DCCh
IMCR228
DD0h
IMCR229
DD4h
IMCR230
DD8h
IMCR231
DDCh
IMCR232
DE0h
IMCR233
DE4h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
434 / 5251


---
# 페이지 384

Table continued from the previous page...
Register
Offset
IMCR234
DE8h
IMCR235
DECh
IMCR236
DF0h
IMCR237
DF4h
IMCR238
DF8h
IMCR239
DFCh
IMCR240
E00h
IMCR241
E04h
IMCR242
E08h
IMCR243
E0Ch
IMCR244
E10h
IMCR245
E14h
IMCR246
E18h
IMCR247
E1Ch
IMCR248
E20h
IMCR249
E24h
IMCR250
E28h
IMCR251
E2Ch
IMCR252
E30h
IMCR253
E34h
IMCR254
E38h
IMCR255
E3Ch
IMCR256
E40h
IMCR257
E44h
IMCR258
E48h
IMCR259
E4Ch
IMCR260
E50h
IMCR261
E54h
IMCR262
E58h
IMCR263
E5Ch
IMCR264
E60h
IMCR265
E64h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
435 / 5251


---
# 페이지 385

Table continued from the previous page...
Register
Offset
IMCR266
E68h
IMCR267
E6Ch
IMCR268
E70h
IMCR289
EC4h
IMCR290
EC8h
IMCR291
ECCh
IMCR292
ED0h
IMCR293
ED4h
IMCR294
ED8h
IMCR295
EDCh
IMCR296
EE0h
IMCR297
EE4h
IMCR298
EE8h
IMCR299
EECh
IMCR300
EF0h
IMCR301
EF4h
IMCR302
EF8h
IMCR303
EFCh
IMCR304
F00h
IMCR305
F04h
IMCR306
F08h
IMCR307
F0Ch
IMCR308
F10h
IMCR309
F14h
IMCR315
F2Ch
IMCR316
F30h
IMCR317
F34h
IMCR318
F38h
IMCR319
F3Ch
IMCR320
F40h
IMCR321
F44h
IMCR322
F48h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
436 / 5251


---
# 페이지 386

Table continued from the previous page...
Register
Offset
IMCR323
F4Ch
IMCR324
F50h
IMCR325
F54h
IMCR343
F9Ch
IMCR344
FA0h
IMCR345
FA4h
IMCR346
FA8h
IMCR347
FACh
IMCR348
FB0h
IMCR349
FB4h
IMCR350
FB8h
IMCR351
FBCh
IMCR352
FC0h
IMCR353
FC4h
IMCR354
FC8h
IMCR355
FCCh
IMCR356
FD0h
IMCR357
FD4h
IMCR358
FD8h
IMCR359
FDCh
IMCR360
FE0h
IMCR361
FE4h
IMCR362
FE8h
IMCR363
FECh
IMCR364
FF0h
IMCR365
FF4h
IMCR366
FF8h
IMCR367
FFCh
IMCR368
1000h
IMCR369
1004h
IMCR370
1008h
IMCR373
1014h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
437 / 5251


---
# 페이지 387

Table continued from the previous page...
Register
Offset
IMCR374
1018h
IMCR375
101Ch
IMCR376
1020h
IMCR377
1024h
IMCR378
1028h
IMCR389
1054h
IMCR398
1078h
IMCR399
107Ch
IMCR409
10A4h
IMCR410
10A8h
IMCR411
10ACh
IMCR412
10B0h
IMCR413
10B4h
IMCR414
10B8h
IMCR415
10BCh
IMCR416
10C0h
IMCR417
10C4h
IMCR418
10C8h
IMCR440
1120h
IMCR448
1140h
IMCR449
1144h
IMCR450
1148h
IMCR451
114Ch
IMCR452
1150h
IMCR453
1154h
IMCR454
1158h
IMCR455
115Ch
IMCR456
1160h
IMCR457
1164h
IMCR458
1168h
IMCR459
116Ch
IMCR460
1170h
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
438 / 5251


---
# 페이지 388

Table continued from the previous page...
Register
Offset
IMCR461
1174h
IMCR462
1178h
IMCR463
117Ch
IMCR464
1180h
IMCR465
1184h
IMCR466
1188h
IMCR467
118Ch
IMCR468
1190h
IMCR469
1194h
IMCR470
1198h
IMCR471
119Ch
IMCR472
11A0h
IMCR473
11A4h
Function
Selects the source signal connected to the register's associated destination, which is an internal module port that is an input port 
or can be configured as an input.
This register supports only 32-bit accesses. Byte and half-word write accesses are not supported.
For IMCR assignments and field values, see the IOMUX file attached to this document.
 
• Configure these registers only during application initialization; you must not modify them during 
application runtime.
• Accessing a reserved IMCRn register generates a transfer error.
• These registers are a part of the SIUL memory map but the physical implementation of these registers is a part 
of the IOMUX RTL.
• SIUL2 interprets accesses to MSCRn at the module level.
  NOTE  
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
439 / 5251


---
# 페이지 389

Internal connections
Destination (module port)
Module-port IMCR
Input port
Module 0
Output port
Input buffer
Input buffer
Destination (chip pin)
Pin a
Pin b
Output 
buffer
Output port
Module n
Output port
Chip-pin MSCR
Figure 27. MSCR and IMCR port and pin connection
Diagram
Bits
31
30
29
28
27
26
25
24
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
SSS 
W
Reset
0
0
0
0
0
0
0
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
SSS
Source Signal Select
Selects which source signal is connected to the associated destination (chip pin).
10.6.22 GPIO Pad Data Output (GPDO0 - GPDO323)
Offset
For n = 0 to 37; n = 40 to 140; n = 142 to 323:
Register
Offset
GPDOn
1300h + (n + 3 - 2 × (n mod 4))
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
440 / 5251


---
# 페이지 390

Function
Writes 0 or 1 to a single GPIO pad with a byte access and supports 8-, 16-, and 32-bit accesses.
Diagram
Bits
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
PDO_n 
W
Reset
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
7-1
—
Reserved
0
PDO_n
Pad Data Out
Stores the data to be driven out on an external GPIO pad (controlled by this register) when you configure 
the pad as an output.
It also represents PDO[n], where n is the instance of the register.
0b - Logic low value
1b - Logic high value
10.6.23 GPIO Pad Data Input (GPDI0 - GPDI323)
Offset
For n = 0 to 37; n = 40 to 140; n = 142 to 323:
Register
Offset
GPDIn
1500h + (n + 3 - 2 × (n mod 4))
Function
Reads the GPIO pad data with a byte access and supports 8-, 16-, and 32-bit accesses.
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
441 / 5251


---
# 페이지 391

Diagram
Bits
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
PDI_n 
W
Reset
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
7-1
—
Reserved
0
PDI_n
Pad Data In
Stores the value of the external GPIO pad associated with this register.
It represents PDI[n], where n is the instance of the register.
0b - Logic low
1b - Logic high
10.6.24 Parallel GPIO Pad Data Output (PGPDO0 - PGPDO3)
Offset
Register
Offset
PGPDO1
1700h
PGPDO0
1702h
PGPDO3
1704h
Function
Sets or clears the respective pads of the chip and supports 8-, 16-, and 32-bit accesses. This register also accesses the same 
physical resource as the PDO and MPGPDO address locations.
This register sets the values of all the output pins assigned to a chip port with a single 16-bit register write, while the GPDOn 
register sets the value on a specific pin with byte writes.
The access to this register's location is coherent with access to the bitwise GPDOn.
For a given PGPDOx[PPDOy], where x is the register instance index and y is the field index, the following equation shows the 
equivalent GPDOn[PDO_n] field:
PGPDOx[PPDOy] = GPDO(x × 16) + (15 - y)[PDO_(x × 16) + (15 - y)]
Following are some of the examples of mapping:
• PGPDO0[PPDO15] = GPDO0[PDO_0]
• PGPDO2[PPDO15] = GPDO32[PDO_32]
• PGPDO31[PPDO0] = GPDO511[PDO_511]
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
442 / 5251


---
# 페이지 392

Diagram
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
PPDO
15 
PPDO
14 
PPDO
13 
PPDO
12 
PPDO
11 
PPDO
10 
PPDO
9 
PPDO
8 
PPDO
7 
PPDO
6 
PPDO
5 
PPDO
4 
PPDO
3 
PPDO
2 
PPDO
1 
PPDO
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
15
PPDO15
Parallel Pad Data Out 15
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
14
PPDO14
Parallel Pad Data Out 14
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
13
PPDO13
Parallel Pad Data Out 13
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
12
PPDO12
Parallel Pad Data Out 12
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
11
PPDO11
Parallel Pad Data Out 11
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
10
PPDO10
Parallel Pad Data Out 10
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
9
PPDO9
Parallel Pad Data Out 9
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
443 / 5251


---
# 페이지 393

Table continued from the previous page...
Field
Function
0b - Logic low
1b - Logic high
8
PPDO8
Parallel Pad Data Out 8
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
7
PPDO7
Parallel Pad Data Out 7
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
6
PPDO6
Parallel Pad Data Out 6
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
5
PPDO5
Parallel Pad Data Out 5
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
4
PPDO4
Parallel Pad Data Out 4
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
3
PPDO3
Parallel Pad Data Out 3
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
2
PPDO2
Parallel Pad Data Out 2
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
1
Parallel Pad Data Out 1
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
444 / 5251


---
# 페이지 394

Table continued from the previous page...
Field
Function
PPDO1
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
0
PPDO0
Parallel Pad Data Out 0
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
10.6.25 Parallel GPIO Pad Data Output (PGPDO2)
Offset
Register
Offset
PGPDO2
1706h
Function
Sets or clears the respective pads of the chip and supports 8-, 16-, and 32-bit accesses. This register also accesses the same 
physical resource as the PDO and MPGPDO address locations.
This register sets the values of all the output pins assigned to a chip port with a single 16-bit register write, while the GPDOn 
register sets the value on a specific pin with byte writes.
The access to this register's location is coherent with access to the bitwise GPDOn.
For a given PGPDOx[PPDOy], where x is the register instance index and y is the field index, the following equation shows the 
equivalent GPDOn[PDO_n] field:
PGPDOx[PPDOy] = GPDO(x × 16) + (15 - y)[PDO_(x × 16) + (15 - y)]
Following are some of the examples of mapping:
• PGPDO0[PPDO15] = GPDO0[PDO_0]
• PGPDO2[PPDO15] = GPDO32[PDO_32]
• PGPDO31[PPDO0] = GPDO511[PDO_511]
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
445 / 5251


---
# 페이지 395

Diagram
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
PPDO
15 
PPDO
14 
PPDO
13 
PPDO
12 
PPDO
11 
PPDO
10 
0
0
PPDO
7 
PPDO
6 
PPDO
5 
PPDO
4 
PPDO
3 
PPDO
2 
PPDO
1 
PPDO
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
15
PPDO15
Parallel Pad Data Out 15
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
14
PPDO14
Parallel Pad Data Out 14
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
13
PPDO13
Parallel Pad Data Out 13
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
12
PPDO12
Parallel Pad Data Out 12
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
11
PPDO11
Parallel Pad Data Out 11
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
10
PPDO10
Parallel Pad Data Out 10
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
9
—
Reserved
Always write zero to this field.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
446 / 5251


---
# 페이지 396

Table continued from the previous page...
Field
Function
8
—
Reserved
Always write zero to this field.
7
PPDO7
Parallel Pad Data Out 7
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
6
PPDO6
Parallel Pad Data Out 6
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
5
PPDO5
Parallel Pad Data Out 5
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
4
PPDO4
Parallel Pad Data Out 4
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
3
PPDO3
Parallel Pad Data Out 3
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
2
PPDO2
Parallel Pad Data Out 2
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
1
PPDO1
Parallel Pad Data Out 1
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
0
Parallel Pad Data Out 0
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
447 / 5251


---
# 페이지 397

Table continued from the previous page...
Field
Function
PPDO0
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
10.6.26 Parallel GPIO Pad Data Output (PGPDO4 - PGPDO9)
Offset
Register
Offset
PGPDO5
1708h
PGPDO4
170Ah
PGPDO7
170Ch
PGPDO6
170Eh
PGPDO9
1710h
Function
Sets or clears the respective pads of the chip and supports 8-, 16-, and 32-bit accesses. This register also accesses the same 
physical resource as the PDO and MPGPDO address locations.
This register sets the values of all the output pins assigned to a chip port with a single 16-bit register write, while the GPDOn 
register sets the value on a specific pin with byte writes.
The access to this register's location is coherent with access to the bitwise GPDOn.
For a given PGPDOx[PPDOy], where x is the register instance index and y is the field index, the following equation shows the 
equivalent GPDOn[PDO_n] field:
PGPDOx[PPDOy] = GPDO(x × 16) + (15 - y)[PDO_(x × 16) + (15 - y)]
Following are some of the examples of mapping:
• PGPDO0[PPDO15] = GPDO0[PDO_0]
• PGPDO2[PPDO15] = GPDO32[PDO_32]
• PGPDO31[PPDO0] = GPDO511[PDO_511]
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
448 / 5251


---
# 페이지 398

Diagram
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
PPDO
15 
PPDO
14 
PPDO
13 
PPDO
12 
PPDO
11 
PPDO
10 
PPDO
9 
PPDO
8 
PPDO
7 
PPDO
6 
PPDO
5 
PPDO
4 
PPDO
3 
PPDO
2 
PPDO
1 
PPDO
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
15
PPDO15
Parallel Pad Data Out 15
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
14
PPDO14
Parallel Pad Data Out 14
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
13
PPDO13
Parallel Pad Data Out 13
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
12
PPDO12
Parallel Pad Data Out 12
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
11
PPDO11
Parallel Pad Data Out 11
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
10
PPDO10
Parallel Pad Data Out 10
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
9
PPDO9
Parallel Pad Data Out 9
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
449 / 5251


---
# 페이지 399

Table continued from the previous page...
Field
Function
0b - Logic low
1b - Logic high
8
PPDO8
Parallel Pad Data Out 8
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
7
PPDO7
Parallel Pad Data Out 7
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
6
PPDO6
Parallel Pad Data Out 6
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
5
PPDO5
Parallel Pad Data Out 5
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
4
PPDO4
Parallel Pad Data Out 4
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
3
PPDO3
Parallel Pad Data Out 3
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
2
PPDO2
Parallel Pad Data Out 2
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
1
Parallel Pad Data Out 1
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
450 / 5251


---
# 페이지 400

Table continued from the previous page...
Field
Function
PPDO1
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
0
PPDO0
Parallel Pad Data Out 0
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
10.6.27 Parallel GPIO Pad Data Output (PGPDO8)
Offset
Register
Offset
PGPDO8
1712h
Function
Sets or clears the respective pads of the chip and supports 8-, 16-, and 32-bit accesses. This register also accesses the same 
physical resource as the PDO and MPGPDO address locations.
This register sets the values of all the output pins assigned to a chip port with a single 16-bit register write, while the GPDOn 
register sets the value on a specific pin with byte writes.
The access to this register's location is coherent with access to the bitwise GPDOn.
For a given PGPDOx[PPDOy], where x is the register instance index and y is the field index, the following equation shows the 
equivalent GPDOn[PDO_n] field:
PGPDOx[PPDOy] = GPDO(x × 16) + (15 - y)[PDO_(x × 16) + (15 - y)]
Following are some of the examples of mapping:
• PGPDO0[PPDO15] = GPDO0[PDO_0]
• PGPDO2[PPDO15] = GPDO32[PDO_32]
• PGPDO31[PPDO0] = GPDO511[PDO_511]
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
451 / 5251


---
# 페이지 401

Diagram
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
PPDO
15 
PPDO
14 
PPDO
13 
PPDO
12 
PPDO
11 
PPDO
10 
PPDO
9 
PPDO
8 
PPDO
7 
PPDO
6 
PPDO
5 
PPDO
4 
PPDO
3 
0
PPDO
1 
PPDO
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
15
PPDO15
Parallel Pad Data Out 15
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
14
PPDO14
Parallel Pad Data Out 14
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
13
PPDO13
Parallel Pad Data Out 13
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
12
PPDO12
Parallel Pad Data Out 12
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
11
PPDO11
Parallel Pad Data Out 11
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
10
PPDO10
Parallel Pad Data Out 10
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
9
PPDO9
Parallel Pad Data Out 9
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
452 / 5251


---
# 페이지 402

Table continued from the previous page...
Field
Function
0b - Logic low
1b - Logic high
8
PPDO8
Parallel Pad Data Out 8
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
7
PPDO7
Parallel Pad Data Out 7
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
6
PPDO6
Parallel Pad Data Out 6
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
5
PPDO5
Parallel Pad Data Out 5
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
4
PPDO4
Parallel Pad Data Out 4
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
3
PPDO3
Parallel Pad Data Out 3
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
2
—
Reserved
Always write zero to this field.
1
PPDO1
Parallel Pad Data Out 1
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
453 / 5251


---
# 페이지 403

Table continued from the previous page...
Field
Function
0b - Logic low
1b - Logic high
0
PPDO0
Parallel Pad Data Out 0
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
10.6.28 Parallel GPIO Pad Data Output (PGPDO10 - PGPDO19)
Offset
For n = 10 to 19:
Register
Offset
PGPDOn
1714h + 2 × (n + 1 – 2 × (n mod 2))
Function
Sets or clears the respective pads of the chip and supports 8-, 16-, and 32-bit accesses. This register also accesses the same 
physical resource as the PDO and MPGPDO address locations.
This register sets the values of all the output pins assigned to a chip port with a single 16-bit register write, while the GPDOn 
register sets the value on a specific pin with byte writes.
The access to this register's location is coherent with access to the bitwise GPDOn.
For a given PGPDOx[PPDOy], where x is the register instance index and y is the field index, the following equation shows the 
equivalent GPDOn[PDO_n] field:
PGPDOx[PPDOy] = GPDO(x × 16) + (15 - y)[PDO_(x × 16) + (15 - y)]
Following are some of the examples of mapping:
• PGPDO0[PPDO15] = GPDO0[PDO_0]
• PGPDO2[PPDO15] = GPDO32[PDO_32]
• PGPDO31[PPDO0] = GPDO511[PDO_511]
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
454 / 5251


---
# 페이지 404

Diagram
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
PPDO
15 
PPDO
14 
PPDO
13 
PPDO
12 
PPDO
11 
PPDO
10 
PPDO
9 
PPDO
8 
PPDO
7 
PPDO
6 
PPDO
5 
PPDO
4 
PPDO
3 
PPDO
2 
PPDO
1 
PPDO
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
15
PPDO15
Parallel Pad Data Out 15
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
14
PPDO14
Parallel Pad Data Out 14
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
13
PPDO13
Parallel Pad Data Out 13
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
12
PPDO12
Parallel Pad Data Out 12
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
11
PPDO11
Parallel Pad Data Out 11
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
10
PPDO10
Parallel Pad Data Out 10
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
9
PPDO9
Parallel Pad Data Out 9
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
455 / 5251


---
# 페이지 405

Table continued from the previous page...
Field
Function
0b - Logic low
1b - Logic high
8
PPDO8
Parallel Pad Data Out 8
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
7
PPDO7
Parallel Pad Data Out 7
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
6
PPDO6
Parallel Pad Data Out 6
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
5
PPDO5
Parallel Pad Data Out 5
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
4
PPDO4
Parallel Pad Data Out 4
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
3
PPDO3
Parallel Pad Data Out 3
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
2
PPDO2
Parallel Pad Data Out 2
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
1
Parallel Pad Data Out 1
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
456 / 5251


---
# 페이지 406

Table continued from the previous page...
Field
Function
PPDO1
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
0
PPDO0
Parallel Pad Data Out 0
Writes to or reads the data register that stores the value to be driven on the pad in Output mode.
0b - Logic low
1b - Logic high
10.6.29 Parallel GPIO Pad Data Input (PGPDI0 - PGPDI3)
Offset
Register
Offset
PGPDI1
1740h
PGPDI0
1742h
PGPDI3
1744h
Function
Holds the synchronized input value from the pads and supports 8-, 16-, and 32-bit accesses.
This register reads the values of all input pins assigned to a chip port with a single 16-bit register read, while GPDIn registers read 
the value on a specific pin with a byte read.
The access to this register's location is coherent with the access to the bitwise GPDIn.
For a given PGPDIx[PPDIy], where x is the register instance index and y is the field index, the following equation shows the 
equivalent GPDIn[PDI_n] field:
PGPDIx[PPDIy] = GPDI(x × 16) + (15 - y)[PDI_(x × 16) + (15 - y)]
Following are some of the examples of mapping:
• PGPDI0[PPDI15] = GPDI0[PDI_0]
• PGPDI2[PPDI15] = GPDI32[PDI_32]
• PGPDI31[PPDI0] = GPDI511[PDI_511]
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
457 / 5251


---
# 페이지 407

Diagram
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
PPDI1
5 
PPDI1
4 
PPDI1
3 
PPDI1
2 
PPDI1
1 
PPDI1
0 
PPDI9 
PPDI8 
PPDI7 
PPDI6 
PPDI5 
PPDI4 
PPDI3 
PPDI2 
PPDI1 
PPDI0 
W
Reset
0
0
0
0
0
0
0
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
15
PPDI15
Parallel Pad Data Input 15
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
14
PPDI14
Parallel Pad Data Input 14
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
13
PPDI13
Parallel Pad Data Input 13
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
12
PPDI12
Parallel Pad Data Input 12
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
11
PPDI11
Parallel Pad Data Input 11
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
10
PPDI10
Parallel Pad Data Input 10
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
9
Parallel Pad Data Input 9
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
458 / 5251


---
# 페이지 408

Table continued from the previous page...
Field
Function
PPDI9
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
8
PPDI8
Parallel Pad Data Input 8
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
7
PPDI7
Parallel Pad Data Input 7
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
6
PPDI6
Parallel Pad Data Input 6
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
5
PPDI5
Parallel Pad Data Input 5
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
4
PPDI4
Parallel Pad Data Input 4
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
3
PPDI3
Parallel Pad Data Input 3
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
2
PPDI2
Parallel Pad Data Input 2
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
459 / 5251


---
# 페이지 409

Table continued from the previous page...
Field
Function
1
PPDI1
Parallel Pad Data Input 1
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
0
PPDI0
Parallel Pad Data Input 0
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
10.6.30 Parallel GPIO Pad Data Input (PGPDI2)
Offset
Register
Offset
PGPDI2
1746h
Function
Holds the synchronized input value from the pads and supports 8-, 16-, and 32-bit accesses.
This register reads the values of all input pins assigned to a chip port with a single 16-bit register read, while GPDIn registers read 
the value on a specific pin with a byte read.
The access to this register's location is coherent with the access to the bitwise GPDIn.
For a given PGPDIx[PPDIy], where x is the register instance index and y is the field index, the following equation shows the 
equivalent GPDIn[PDI_n] field:
PGPDIx[PPDIy] = GPDI(x × 16) + (15 - y)[PDI_(x × 16) + (15 - y)]
Following are some of the examples of mapping:
• PGPDI0[PPDI15] = GPDI0[PDI_0]
• PGPDI2[PPDI15] = GPDI32[PDI_32]
• PGPDI31[PPDI0] = GPDI511[PDI_511]
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
460 / 5251


---
# 페이지 410

Diagram
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
PPDI1
5 
PPDI1
4 
PPDI1
3 
PPDI1
2 
PPDI1
1 
PPDI1
0 
Reserv
ed 
Reserv
ed 
PPDI7 
PPDI6 
PPDI5 
PPDI4 
PPDI3 
PPDI2 
PPDI1 
PPDI0 
W
Reset
0
0
0
0
0
0
0
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
15
PPDI15
Parallel Pad Data Input 15
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
14
PPDI14
Parallel Pad Data Input 14
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
13
PPDI13
Parallel Pad Data Input 13
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
12
PPDI12
Parallel Pad Data Input 12
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
11
PPDI11
Parallel Pad Data Input 11
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
10
PPDI10
Parallel Pad Data Input 10
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
9
Reserved
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
461 / 5251


---
# 페이지 411

Table continued from the previous page...
Field
Function
—
8
—
Reserved
7
PPDI7
Parallel Pad Data Input 7
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
6
PPDI6
Parallel Pad Data Input 6
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
5
PPDI5
Parallel Pad Data Input 5
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
4
PPDI4
Parallel Pad Data Input 4
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
3
PPDI3
Parallel Pad Data Input 3
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
2
PPDI2
Parallel Pad Data Input 2
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
1
PPDI1
Parallel Pad Data Input 1
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
462 / 5251


---
# 페이지 412

Table continued from the previous page...
Field
Function
0
PPDI0
Parallel Pad Data Input 0
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
10.6.31 Parallel GPIO Pad Data Input (PGPDI4 - PGPDI9)
Offset
Register
Offset
PGPDI5
1748h
PGPDI4
174Ah
PGPDI7
174Ch
PGPDI6
174Eh
PGPDI9
1750h
Function
Holds the synchronized input value from the pads and supports 8-, 16-, and 32-bit accesses.
This register reads the values of all input pins assigned to a chip port with a single 16-bit register read, while GPDIn registers read 
the value on a specific pin with a byte read.
The access to this register's location is coherent with the access to the bitwise GPDIn.
For a given PGPDIx[PPDIy], where x is the register instance index and y is the field index, the following equation shows the 
equivalent GPDIn[PDI_n] field:
PGPDIx[PPDIy] = GPDI(x × 16) + (15 - y)[PDI_(x × 16) + (15 - y)]
Following are some of the examples of mapping:
• PGPDI0[PPDI15] = GPDI0[PDI_0]
• PGPDI2[PPDI15] = GPDI32[PDI_32]
• PGPDI31[PPDI0] = GPDI511[PDI_511]
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
463 / 5251


---
# 페이지 413

Diagram
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
PPDI1
5 
PPDI1
4 
PPDI1
3 
PPDI1
2 
PPDI1
1 
PPDI1
0 
PPDI9 
PPDI8 
PPDI7 
PPDI6 
PPDI5 
PPDI4 
PPDI3 
PPDI2 
PPDI1 
PPDI0 
W
Reset
0
0
0
0
0
0
0
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
15
PPDI15
Parallel Pad Data Input 15
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
14
PPDI14
Parallel Pad Data Input 14
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
13
PPDI13
Parallel Pad Data Input 13
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
12
PPDI12
Parallel Pad Data Input 12
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
11
PPDI11
Parallel Pad Data Input 11
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
10
PPDI10
Parallel Pad Data Input 10
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
9
Parallel Pad Data Input 9
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
464 / 5251


---
# 페이지 414

Table continued from the previous page...
Field
Function
PPDI9
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
8
PPDI8
Parallel Pad Data Input 8
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
7
PPDI7
Parallel Pad Data Input 7
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
6
PPDI6
Parallel Pad Data Input 6
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
5
PPDI5
Parallel Pad Data Input 5
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
4
PPDI4
Parallel Pad Data Input 4
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
3
PPDI3
Parallel Pad Data Input 3
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
2
PPDI2
Parallel Pad Data Input 2
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
465 / 5251


---
# 페이지 415

Table continued from the previous page...
Field
Function
1
PPDI1
Parallel Pad Data Input 1
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
0
PPDI0
Parallel Pad Data Input 0
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
10.6.32 Parallel GPIO Pad Data Input (PGPDI8)
Offset
Register
Offset
PGPDI8
1752h
Function
Holds the synchronized input value from the pads and supports 8-, 16-, and 32-bit accesses.
This register reads the values of all input pins assigned to a chip port with a single 16-bit register read, while GPDIn registers read 
the value on a specific pin with a byte read.
The access to this register's location is coherent with the access to the bitwise GPDIn.
For a given PGPDIx[PPDIy], where x is the register instance index and y is the field index, the following equation shows the 
equivalent GPDIn[PDI_n] field:
PGPDIx[PPDIy] = GPDI(x × 16) + (15 - y)[PDI_(x × 16) + (15 - y)]
Following are some of the examples of mapping:
• PGPDI0[PPDI15] = GPDI0[PDI_0]
• PGPDI2[PPDI15] = GPDI32[PDI_32]
• PGPDI31[PPDI0] = GPDI511[PDI_511]
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
466 / 5251


---
# 페이지 416

Diagram
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
PPDI1
5 
PPDI1
4 
PPDI1
3 
PPDI1
2 
PPDI1
1 
PPDI1
0 
PPDI9 
PPDI8 
PPDI7 
PPDI6 
PPDI5 
PPDI4 
PPDI3 
Reserv
ed 
PPDI1 
PPDI0 
W
Reset
0
0
0
0
0
0
0
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
15
PPDI15
Parallel Pad Data Input 15
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
14
PPDI14
Parallel Pad Data Input 14
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
13
PPDI13
Parallel Pad Data Input 13
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
12
PPDI12
Parallel Pad Data Input 12
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
11
PPDI11
Parallel Pad Data Input 11
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
10
PPDI10
Parallel Pad Data Input 10
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
9
Parallel Pad Data Input 9
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
467 / 5251


---
# 페이지 417

Table continued from the previous page...
Field
Function
PPDI9
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
8
PPDI8
Parallel Pad Data Input 8
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
7
PPDI7
Parallel Pad Data Input 7
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
6
PPDI6
Parallel Pad Data Input 6
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
5
PPDI5
Parallel Pad Data Input 5
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
4
PPDI4
Parallel Pad Data Input 4
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
3
PPDI3
Parallel Pad Data Input 3
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
2
—
Reserved
1
PPDI1
Parallel Pad Data Input 1
Reads the current pad value of the corresponding pad.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
468 / 5251


---
# 페이지 418

Table continued from the previous page...
Field
Function
0b - Logic low
1b - Logic high
0
PPDI0
Parallel Pad Data Input 0
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
10.6.33 Parallel GPIO Pad Data Input (PGPDI10 - PGPDI19)
Offset
For n = 10 to 19:
Register
Offset
PGPDIn
1754h + 2 × (n + 1 – 2 × (n mod 2))
Function
Holds the synchronized input value from the pads and supports 8-, 16-, and 32-bit accesses.
This register reads the values of all input pins assigned to a chip port with a single 16-bit register read, while GPDIn registers read 
the value on a specific pin with a byte read.
The access to this register's location is coherent with the access to the bitwise GPDIn.
For a given PGPDIx[PPDIy], where x is the register instance index and y is the field index, the following equation shows the 
equivalent GPDIn[PDI_n] field:
PGPDIx[PPDIy] = GPDI(x × 16) + (15 - y)[PDI_(x × 16) + (15 - y)]
Following are some of the examples of mapping:
• PGPDI0[PPDI15] = GPDI0[PDI_0]
• PGPDI2[PPDI15] = GPDI32[PDI_32]
• PGPDI31[PPDI0] = GPDI511[PDI_511]
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
469 / 5251


---
# 페이지 419

Diagram
Bits
15
14
13
12
11
10
9
8
7
6
5
4
3
2
1
0
R
PPDI1
5 
PPDI1
4 
PPDI1
3 
PPDI1
2 
PPDI1
1 
PPDI1
0 
PPDI9 
PPDI8 
PPDI7 
PPDI6 
PPDI5 
PPDI4 
PPDI3 
PPDI2 
PPDI1 
PPDI0 
W
Reset
0
0
0
0
0
0
0
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
15
PPDI15
Parallel Pad Data Input 15
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
14
PPDI14
Parallel Pad Data Input 14
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
13
PPDI13
Parallel Pad Data Input 13
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
12
PPDI12
Parallel Pad Data Input 12
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
11
PPDI11
Parallel Pad Data Input 11
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
10
PPDI10
Parallel Pad Data Input 10
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
9
Parallel Pad Data Input 9
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
470 / 5251


---
# 페이지 420

Table continued from the previous page...
Field
Function
PPDI9
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
8
PPDI8
Parallel Pad Data Input 8
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
7
PPDI7
Parallel Pad Data Input 7
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
6
PPDI6
Parallel Pad Data Input 6
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
5
PPDI5
Parallel Pad Data Input 5
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
4
PPDI4
Parallel Pad Data Input 4
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
3
PPDI3
Parallel Pad Data Input 3
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
2
PPDI2
Parallel Pad Data Input 2
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
471 / 5251


---
# 페이지 421

Table continued from the previous page...
Field
Function
1
PPDI1
Parallel Pad Data Input 1
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
0
PPDI0
Parallel Pad Data Input 0
Reads the current pad value of the corresponding pad.
0b - Logic low
1b - Logic high
10.6.34 Masked Parallel GPIO Pad Data Output (MPGPDO0 - MPGPDO1)
Offset
Register
Offset
MPGPDO0
1780h
MPGPDO1
1784h
Function
Modifies the pad values associated with PGPDOn selectively and supports only 32-bit accesses. It does not support byte and 
half-word accesses.
 
Access this register only with 32-bit writes. 8-bit or 16-bit writes do not modify any bits in the register resulting in a 
transfer error. Read access returns 0.
  NOTE  
The accesses to each of this register location is coherent with access to the bitwise GPDOn.
For a given MPGPDOx[MPPDOy], where x is the register instance index and y is the field index, the following equation shows the 
equivalent GPDOn[PDO_n]:
MPGPDOx[MPPDOy] = GPDO(x × 16) + (15 - y)[PDO_(x × 16) + (15 - y)]
Following are some of the examples of mapping:
• MPGPDO0[MPPDO15] = GPDO0[PDO_0]
• MPGPDO2[MPPDO15] = GPDO32[PDO_32]
• MPGPDO31[MPPDO0] = GPDO511[PDO_511]
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
472 / 5251


---
# 페이지 422

Diagram
Bits
31
30
29
28
27
26
25
24
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
MASK
15 
MASK
14 
MASK
13 
MASK
12 
MASK
11 
MASK
10 
MASK
9 
MASK
8 
MASK
7 
MASK
6 
MASK
5 
MASK
4 
MASK
3 
MASK
2 
MASK
1 
MASK
0 
Reset
0
0
0
0
0
0
0
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
0
0
0
W
MPPD
O15 
MPPD
O14 
MPPD
O13 
MPPD
O12 
MPPD
O11 
MPPD
O10 
MPPD
O9 
MPPD
O8 
MPPD
O7 
MPPD
O6 
MPPD
O5 
MPPD
O4 
MPPD
O3 
MPPD
O2 
MPPD
O1 
MPPD
O0 
Reset
0
0
0
0
0
0
0
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
MASK15
Mask Field 15
Masks MPPDO15 in the corresponding MPGPDOn register instance.
0b - MPPDO15 is ignored
1b - MPPDO15 is written
30
MASK14
Mask Field 14
Masks MPPDO14 in the corresponding MPGPDOn register instance.
0b - MPPDO14 is ignored
1b - MPPDO14 is written
29
MASK13
Mask Field 13
Masks MPPDO13 in the corresponding MPGPDOn register instance.
0b - MPPDO13 is ignored
1b - MPPDO13 is written
28
MASK12
Mask Field 12
Masks MPPDO12 in the corresponding MPGPDOn register instance.
0b - MPPDO12 is ignored
1b - MPPDO12 is written
27
MASK11
Mask Field 11
Masks MPPDO11 in the corresponding MPGPDOn register instance.
0b - MPPDO11 is ignored
1b - MPPDO11 is written
26
Mask Field 10
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
473 / 5251


---
# 페이지 423

Table continued from the previous page...
Field
Function
MASK10
Masks MPPDO10 in the corresponding MPGPDOn register instance.
0b - MPPDO10 is ignored
1b - MPPDO10 is written
25
MASK9
Mask Field 9
Masks MPPDO9 in the corresponding MPGPDOn register instance.
0b - MPPDO9 is ignored
1b - MPPDO9 is written
24
MASK8
Mask Field 8
Masks MPPDO8 in the corresponding MPGPDOn register instance.
0b - MPPDO8 is ignored
1b - MPPDO8 is written
23
MASK7
Mask Field 7
Masks MPPDO7 in the corresponding MPGPDOn register instance.
0b - MPPDO7 is ignored
1b - MPPDO7 is written
22
MASK6
Mask Field 6
Masks MPPDO6 in the corresponding MPGPDOn register instance.
0b - MPPDO6 is ignored
1b - MPPDO6 is written
21
MASK5
Mask Field 5
Masks MPPDO5 in the corresponding MPGPDOn register instance.
0b - MPPDO5 is ignored
1b - MPPDO5 is written
20
MASK4
Mask Field 4
Masks MPPDO4 in the corresponding MPGPDOn register instance.
0b - MPPDO4 is ignored
1b - MPPDO4 is written
19
MASK3
Mask Field 3
Masks MPPDO3 in the corresponding MPGPDOn register instance.
0b - MPPDO3 is ignored
1b - MPPDO3 is written
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
474 / 5251


---
# 페이지 424

Table continued from the previous page...
Field
Function
18
MASK2
Mask Field 2
Masks MPPDO2 in the corresponding MPGPDOn register instance.
0b - MPPDO2 is ignored
1b - MPPDO2 is written
17
MASK1
Mask Field 1
Masks MPPDO1 in the corresponding MPGPDOn register instance.
0b - MPPDO1 is ignored
1b - MPPDO1 is written
16
MASK0
Mask Field 0
Masks MPPDO0 in the corresponding MPGPDOn register instance.
0b - MPPDO0 is ignored
1b - MPPDO0 is written
15
MPPDO15
Masked Parallel Pad Data Out 15
Writes to the data register that stores the value to be driven on the pad in Output mode.
14
MPPDO14
Masked Parallel Pad Data Out 14
Writes to the data register that stores the value to be driven on the pad in Output mode.
13
MPPDO13
Masked Parallel Pad Data Out 13
Writes to the data register that stores the value to be driven on the pad in Output mode.
12
MPPDO12
Masked Parallel Pad Data Out 12
Writes to the data register that stores the value to be driven on the pad in Output mode.
11
MPPDO11
Masked Parallel Pad Data Out 11
Writes to the data register that stores the value to be driven on the pad in Output mode.
10
MPPDO10
Masked Parallel Pad Data Out 10
Writes to the data register that stores the value to be driven on the pad in Output mode.
9
MPPDO9
Masked Parallel Pad Data Out 9
Writes to the data register that stores the value to be driven on the pad in Output mode.
8
MPPDO8
Masked Parallel Pad Data Out 8
Writes to the data register that stores the value to be driven on the pad in Output mode.
7
MPPDO7
Masked Parallel Pad Data Out 7
Writes to the data register that stores the value to be driven on the pad in Output mode.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
475 / 5251


---
# 페이지 425

Table continued from the previous page...
Field
Function
6
MPPDO6
Masked Parallel Pad Data Out 6
Writes to the data register that stores the value to be driven on the pad in Output mode.
5
MPPDO5
Masked Parallel Pad Data Out 5
Writes to the data register that stores the value to be driven on the pad in Output mode.
4
MPPDO4
Masked Parallel Pad Data Out 4
Writes to the data register that stores the value to be driven on the pad in Output mode.
3
MPPDO3
Masked Parallel Pad Data Out 3
Writes to the data register that stores the value to be driven on the pad in Output mode.
2
MPPDO2
Masked Parallel Pad Data Out 2
Writes to the data register that stores the value to be driven on the pad in Output mode.
1
MPPDO1
Masked Parallel Pad Data Out 1
Writes to the data register that stores the value to be driven on the pad in Output mode.
0
MPPDO0
Masked Parallel Pad Data Out 0
Writes to the data register that stores the value to be driven on the pad in Output mode.
10.6.35 Masked Parallel GPIO Pad Data Output (MPGPDO2)
Offset
Register
Offset
MPGPDO2
1788h
Function
Modifies the pad values associated with PGPDOn selectively and supports only 32-bit accesses. It does not support byte and 
half-word accesses.
 
Access this register only with 32-bit writes. 8-bit or 16-bit writes do not modify any bits in the register resulting in a 
transfer error. Read access returns 0.
  NOTE  
The accesses to each of this register location is coherent with access to the bitwise GPDOn.
For a given MPGPDOx[MPPDOy], where x is the register instance index and y is the field index, the following equation shows the 
equivalent GPDOn[PDO_n]:
MPGPDOx[MPPDOy] = GPDO(x × 16) + (15 - y)[PDO_(x × 16) + (15 - y)]
Following are some of the examples of mapping:
• MPGPDO0[MPPDO15] = GPDO0[PDO_0]
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
476 / 5251


---
# 페이지 426

• MPGPDO2[MPPDO15] = GPDO32[PDO_32]
• MPGPDO31[MPPDO0] = GPDO511[PDO_511]
Diagram
Bits
31
30
29
28
27
26
25
24
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
MASK
15 
MASK
14 
MASK
13 
MASK
12 
MASK
11 
MASK
10 
Reserv
ed 
Reserv
ed 
MASK
7 
MASK
6 
MASK
5 
MASK
4 
MASK
3 
MASK
2 
MASK
1 
MASK
0 
Reset
0
0
0
0
0
0
0
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
0
0
0
W
MPPD
O15 
MPPD
O14 
MPPD
O13 
MPPD
O12 
MPPD
O11 
MPPD
O10 
Reserv
ed 
Reserv
ed 
MPPD
O7 
MPPD
O6 
MPPD
O5 
MPPD
O4 
MPPD
O3 
MPPD
O2 
MPPD
O1 
MPPD
O0 
Reset
0
0
0
0
0
0
0
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
MASK15
Mask Field 15
Masks MPPDO15 in the corresponding MPGPDOn register instance.
0b - MPPDO15 is ignored
1b - MPPDO15 is written
30
MASK14
Mask Field 14
Masks MPPDO14 in the corresponding MPGPDOn register instance.
0b - MPPDO14 is ignored
1b - MPPDO14 is written
29
MASK13
Mask Field 13
Masks MPPDO13 in the corresponding MPGPDOn register instance.
0b - MPPDO13 is ignored
1b - MPPDO13 is written
28
MASK12
Mask Field 12
Masks MPPDO12 in the corresponding MPGPDOn register instance.
0b - MPPDO12 is ignored
1b - MPPDO12 is written
27
MASK11
Mask Field 11
Masks MPPDO11 in the corresponding MPGPDOn register instance.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
477 / 5251


---
# 페이지 427

Table continued from the previous page...
Field
Function
0b - MPPDO11 is ignored
1b - MPPDO11 is written
26
MASK10
Mask Field 10
Masks MPPDO10 in the corresponding MPGPDOn register instance.
0b - MPPDO10 is ignored
1b - MPPDO10 is written
25
—
Reserved
Always write zero to this field.
24
—
Reserved
Always write zero to this field.
23
MASK7
Mask Field 7
Masks MPPDO7 in the corresponding MPGPDOn register instance.
0b - MPPDO7 is ignored
1b - MPPDO7 is written
22
MASK6
Mask Field 6
Masks MPPDO6 in the corresponding MPGPDOn register instance.
0b - MPPDO6 is ignored
1b - MPPDO6 is written
21
MASK5
Mask Field 5
Masks MPPDO5 in the corresponding MPGPDOn register instance.
0b - MPPDO5 is ignored
1b - MPPDO5 is written
20
MASK4
Mask Field 4
Masks MPPDO4 in the corresponding MPGPDOn register instance.
0b - MPPDO4 is ignored
1b - MPPDO4 is written
19
MASK3
Mask Field 3
Masks MPPDO3 in the corresponding MPGPDOn register instance.
0b - MPPDO3 is ignored
1b - MPPDO3 is written
18
Mask Field 2
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
478 / 5251


---
# 페이지 428

Table continued from the previous page...
Field
Function
MASK2
Masks MPPDO2 in the corresponding MPGPDOn register instance.
0b - MPPDO2 is ignored
1b - MPPDO2 is written
17
MASK1
Mask Field 1
Masks MPPDO1 in the corresponding MPGPDOn register instance.
0b - MPPDO1 is ignored
1b - MPPDO1 is written
16
MASK0
Mask Field 0
Masks MPPDO0 in the corresponding MPGPDOn register instance.
0b - MPPDO0 is ignored
1b - MPPDO0 is written
15
MPPDO15
Masked Parallel Pad Data Out 15
Writes to the data register that stores the value to be driven on the pad in Output mode.
14
MPPDO14
Masked Parallel Pad Data Out 14
Writes to the data register that stores the value to be driven on the pad in Output mode.
13
MPPDO13
Masked Parallel Pad Data Out 13
Writes to the data register that stores the value to be driven on the pad in Output mode.
12
MPPDO12
Masked Parallel Pad Data Out 12
Writes to the data register that stores the value to be driven on the pad in Output mode.
11
MPPDO11
Masked Parallel Pad Data Out 11
Writes to the data register that stores the value to be driven on the pad in Output mode.
10
MPPDO10
Masked Parallel Pad Data Out 10
Writes to the data register that stores the value to be driven on the pad in Output mode.
9
—
Reserved
Always write zero to this field.
8
—
Reserved
Always write zero to this field.
7
MPPDO7
Masked Parallel Pad Data Out 7
Writes to the data register that stores the value to be driven on the pad in Output mode.
6
Masked Parallel Pad Data Out 6
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
479 / 5251


---
# 페이지 429

Table continued from the previous page...
Field
Function
MPPDO6
Writes to the data register that stores the value to be driven on the pad in Output mode.
5
MPPDO5
Masked Parallel Pad Data Out 5
Writes to the data register that stores the value to be driven on the pad in Output mode.
4
MPPDO4
Masked Parallel Pad Data Out 4
Writes to the data register that stores the value to be driven on the pad in Output mode.
3
MPPDO3
Masked Parallel Pad Data Out 3
Writes to the data register that stores the value to be driven on the pad in Output mode.
2
MPPDO2
Masked Parallel Pad Data Out 2
Writes to the data register that stores the value to be driven on the pad in Output mode.
1
MPPDO1
Masked Parallel Pad Data Out 1
Writes to the data register that stores the value to be driven on the pad in Output mode.
0
MPPDO0
Masked Parallel Pad Data Out 0
Writes to the data register that stores the value to be driven on the pad in Output mode.
10.6.36 Masked Parallel GPIO Pad Data Output (MPGPDO3 - MPGPDO7)
Offset
Register
Offset
MPGPDO3
178Ch
MPGPDO4
1790h
MPGPDO5
1794h
MPGPDO6
1798h
MPGPDO7
179Ch
Function
Modifies the pad values associated with PGPDOn selectively and supports only 32-bit accesses. It does not support byte and 
half-word accesses.
 
Access this register only with 32-bit writes. 8-bit or 16-bit writes do not modify any bits in the register resulting in a 
transfer error. Read access returns 0.
  NOTE  
The accesses to each of this register location is coherent with access to the bitwise GPDOn.
For a given MPGPDOx[MPPDOy], where x is the register instance index and y is the field index, the following equation shows the 
equivalent GPDOn[PDO_n]:
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
480 / 5251


---
# 페이지 430

MPGPDOx[MPPDOy] = GPDO(x × 16) + (15 - y)[PDO_(x × 16) + (15 - y)]
Following are some of the examples of mapping:
• MPGPDO0[MPPDO15] = GPDO0[PDO_0]
• MPGPDO2[MPPDO15] = GPDO32[PDO_32]
• MPGPDO31[MPPDO0] = GPDO511[PDO_511]
Diagram
Bits
31
30
29
28
27
26
25
24
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
MASK
15 
MASK
14 
MASK
13 
MASK
12 
MASK
11 
MASK
10 
MASK
9 
MASK
8 
MASK
7 
MASK
6 
MASK
5 
MASK
4 
MASK
3 
MASK
2 
MASK
1 
MASK
0 
Reset
0
0
0
0
0
0
0
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
0
0
0
W
MPPD
O15 
MPPD
O14 
MPPD
O13 
MPPD
O12 
MPPD
O11 
MPPD
O10 
MPPD
O9 
MPPD
O8 
MPPD
O7 
MPPD
O6 
MPPD
O5 
MPPD
O4 
MPPD
O3 
MPPD
O2 
MPPD
O1 
MPPD
O0 
Reset
0
0
0
0
0
0
0
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
MASK15
Mask Field 15
Masks MPPDO15 in the corresponding MPGPDOn register instance.
0b - MPPDO15 is ignored
1b - MPPDO15 is written
30
MASK14
Mask Field 14
Masks MPPDO14 in the corresponding MPGPDOn register instance.
0b - MPPDO14 is ignored
1b - MPPDO14 is written
29
MASK13
Mask Field 13
Masks MPPDO13 in the corresponding MPGPDOn register instance.
0b - MPPDO13 is ignored
1b - MPPDO13 is written
28
MASK12
Mask Field 12
Masks MPPDO12 in the corresponding MPGPDOn register instance.
0b - MPPDO12 is ignored
1b - MPPDO12 is written
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
481 / 5251


---
# 페이지 431

Table continued from the previous page...
Field
Function
27
MASK11
Mask Field 11
Masks MPPDO11 in the corresponding MPGPDOn register instance.
0b - MPPDO11 is ignored
1b - MPPDO11 is written
26
MASK10
Mask Field 10
Masks MPPDO10 in the corresponding MPGPDOn register instance.
0b - MPPDO10 is ignored
1b - MPPDO10 is written
25
MASK9
Mask Field 9
Masks MPPDO9 in the corresponding MPGPDOn register instance.
0b - MPPDO9 is ignored
1b - MPPDO9 is written
24
MASK8
Mask Field 8
Masks MPPDO8 in the corresponding MPGPDOn register instance.
0b - MPPDO8 is ignored
1b - MPPDO8 is written
23
MASK7
Mask Field 7
Masks MPPDO7 in the corresponding MPGPDOn register instance.
0b - MPPDO7 is ignored
1b - MPPDO7 is written
22
MASK6
Mask Field 6
Masks MPPDO6 in the corresponding MPGPDOn register instance.
0b - MPPDO6 is ignored
1b - MPPDO6 is written
21
MASK5
Mask Field 5
Masks MPPDO5 in the corresponding MPGPDOn register instance.
0b - MPPDO5 is ignored
1b - MPPDO5 is written
20
MASK4
Mask Field 4
Masks MPPDO4 in the corresponding MPGPDOn register instance.
0b - MPPDO4 is ignored
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
482 / 5251


---
# 페이지 432

Table continued from the previous page...
Field
Function
1b - MPPDO4 is written
19
MASK3
Mask Field 3
Masks MPPDO3 in the corresponding MPGPDOn register instance.
0b - MPPDO3 is ignored
1b - MPPDO3 is written
18
MASK2
Mask Field 2
Masks MPPDO2 in the corresponding MPGPDOn register instance.
0b - MPPDO2 is ignored
1b - MPPDO2 is written
17
MASK1
Mask Field 1
Masks MPPDO1 in the corresponding MPGPDOn register instance.
0b - MPPDO1 is ignored
1b - MPPDO1 is written
16
MASK0
Mask Field 0
Masks MPPDO0 in the corresponding MPGPDOn register instance.
0b - MPPDO0 is ignored
1b - MPPDO0 is written
15
MPPDO15
Masked Parallel Pad Data Out 15
Writes to the data register that stores the value to be driven on the pad in Output mode.
14
MPPDO14
Masked Parallel Pad Data Out 14
Writes to the data register that stores the value to be driven on the pad in Output mode.
13
MPPDO13
Masked Parallel Pad Data Out 13
Writes to the data register that stores the value to be driven on the pad in Output mode.
12
MPPDO12
Masked Parallel Pad Data Out 12
Writes to the data register that stores the value to be driven on the pad in Output mode.
11
MPPDO11
Masked Parallel Pad Data Out 11
Writes to the data register that stores the value to be driven on the pad in Output mode.
10
MPPDO10
Masked Parallel Pad Data Out 10
Writes to the data register that stores the value to be driven on the pad in Output mode.
9
Masked Parallel Pad Data Out 9
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
483 / 5251


---
# 페이지 433

Table continued from the previous page...
Field
Function
MPPDO9
Writes to the data register that stores the value to be driven on the pad in Output mode.
8
MPPDO8
Masked Parallel Pad Data Out 8
Writes to the data register that stores the value to be driven on the pad in Output mode.
7
MPPDO7
Masked Parallel Pad Data Out 7
Writes to the data register that stores the value to be driven on the pad in Output mode.
6
MPPDO6
Masked Parallel Pad Data Out 6
Writes to the data register that stores the value to be driven on the pad in Output mode.
5
MPPDO5
Masked Parallel Pad Data Out 5
Writes to the data register that stores the value to be driven on the pad in Output mode.
4
MPPDO4
Masked Parallel Pad Data Out 4
Writes to the data register that stores the value to be driven on the pad in Output mode.
3
MPPDO3
Masked Parallel Pad Data Out 3
Writes to the data register that stores the value to be driven on the pad in Output mode.
2
MPPDO2
Masked Parallel Pad Data Out 2
Writes to the data register that stores the value to be driven on the pad in Output mode.
1
MPPDO1
Masked Parallel Pad Data Out 1
Writes to the data register that stores the value to be driven on the pad in Output mode.
0
MPPDO0
Masked Parallel Pad Data Out 0
Writes to the data register that stores the value to be driven on the pad in Output mode.
10.6.37 Masked Parallel GPIO Pad Data Output (MPGPDO8)
Offset
Register
Offset
MPGPDO8
17A0h
Function
Modifies the pad values associated with PGPDOn selectively and supports only 32-bit accesses. It does not support byte and 
half-word accesses.
 
Access this register only with 32-bit writes. 8-bit or 16-bit writes do not modify any bits in the register resulting in a 
transfer error. Read access returns 0.
  NOTE  
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
484 / 5251


---
# 페이지 434

The accesses to each of this register location is coherent with access to the bitwise GPDOn.
For a given MPGPDOx[MPPDOy], where x is the register instance index and y is the field index, the following equation shows the 
equivalent GPDOn[PDO_n]:
MPGPDOx[MPPDOy] = GPDO(x × 16) + (15 - y)[PDO_(x × 16) + (15 - y)]
Following are some of the examples of mapping:
• MPGPDO0[MPPDO15] = GPDO0[PDO_0]
• MPGPDO2[MPPDO15] = GPDO32[PDO_32]
• MPGPDO31[MPPDO0] = GPDO511[PDO_511]
Diagram
Bits
31
30
29
28
27
26
25
24
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
MASK
15 
MASK
14 
MASK
13 
MASK
12 
MASK
11 
MASK
10 
MASK
9 
MASK
8 
MASK
7 
MASK
6 
MASK
5 
MASK
4 
MASK
3 
Reserv
ed 
MASK
1 
MASK
0 
Reset
0
0
0
0
0
0
0
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
0
0
0
W
MPPD
O15 
MPPD
O14 
MPPD
O13 
MPPD
O12 
MPPD
O11 
MPPD
O10 
MPPD
O9 
MPPD
O8 
MPPD
O7 
MPPD
O6 
MPPD
O5 
MPPD
O4 
MPPD
O3 
Reserv
ed 
MPPD
O1 
MPPD
O0 
Reset
0
0
0
0
0
0
0
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
MASK15
Mask Field 15
Masks MPPDO15 in the corresponding MPGPDOn register instance.
0b - MPPDO15 is ignored
1b - MPPDO15 is written
30
MASK14
Mask Field 14
Masks MPPDO14 in the corresponding MPGPDOn register instance.
0b - MPPDO14 is ignored
1b - MPPDO14 is written
29
MASK13
Mask Field 13
Masks MPPDO13 in the corresponding MPGPDOn register instance.
0b - MPPDO13 is ignored
1b - MPPDO13 is written
28
Mask Field 12
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
485 / 5251


---
# 페이지 435

Table continued from the previous page...
Field
Function
MASK12
Masks MPPDO12 in the corresponding MPGPDOn register instance.
0b - MPPDO12 is ignored
1b - MPPDO12 is written
27
MASK11
Mask Field 11
Masks MPPDO11 in the corresponding MPGPDOn register instance.
0b - MPPDO11 is ignored
1b - MPPDO11 is written
26
MASK10
Mask Field 10
Masks MPPDO10 in the corresponding MPGPDOn register instance.
0b - MPPDO10 is ignored
1b - MPPDO10 is written
25
MASK9
Mask Field 9
Masks MPPDO9 in the corresponding MPGPDOn register instance.
0b - MPPDO9 is ignored
1b - MPPDO9 is written
24
MASK8
Mask Field 8
Masks MPPDO8 in the corresponding MPGPDOn register instance.
0b - MPPDO8 is ignored
1b - MPPDO8 is written
23
MASK7
Mask Field 7
Masks MPPDO7 in the corresponding MPGPDOn register instance.
0b - MPPDO7 is ignored
1b - MPPDO7 is written
22
MASK6
Mask Field 6
Masks MPPDO6 in the corresponding MPGPDOn register instance.
0b - MPPDO6 is ignored
1b - MPPDO6 is written
21
MASK5
Mask Field 5
Masks MPPDO5 in the corresponding MPGPDOn register instance.
0b - MPPDO5 is ignored
1b - MPPDO5 is written
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
486 / 5251


---
# 페이지 436

Table continued from the previous page...
Field
Function
20
MASK4
Mask Field 4
Masks MPPDO4 in the corresponding MPGPDOn register instance.
0b - MPPDO4 is ignored
1b - MPPDO4 is written
19
MASK3
Mask Field 3
Masks MPPDO3 in the corresponding MPGPDOn register instance.
0b - MPPDO3 is ignored
1b - MPPDO3 is written
18
—
Reserved
Always write zero to this field.
17
MASK1
Mask Field 1
Masks MPPDO1 in the corresponding MPGPDOn register instance.
0b - MPPDO1 is ignored
1b - MPPDO1 is written
16
MASK0
Mask Field 0
Masks MPPDO0 in the corresponding MPGPDOn register instance.
0b - MPPDO0 is ignored
1b - MPPDO0 is written
15
MPPDO15
Masked Parallel Pad Data Out 15
Writes to the data register that stores the value to be driven on the pad in Output mode.
14
MPPDO14
Masked Parallel Pad Data Out 14
Writes to the data register that stores the value to be driven on the pad in Output mode.
13
MPPDO13
Masked Parallel Pad Data Out 13
Writes to the data register that stores the value to be driven on the pad in Output mode.
12
MPPDO12
Masked Parallel Pad Data Out 12
Writes to the data register that stores the value to be driven on the pad in Output mode.
11
MPPDO11
Masked Parallel Pad Data Out 11
Writes to the data register that stores the value to be driven on the pad in Output mode.
10
MPPDO10
Masked Parallel Pad Data Out 10
Writes to the data register that stores the value to be driven on the pad in Output mode.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
487 / 5251


---
# 페이지 437

Table continued from the previous page...
Field
Function
9
MPPDO9
Masked Parallel Pad Data Out 9
Writes to the data register that stores the value to be driven on the pad in Output mode.
8
MPPDO8
Masked Parallel Pad Data Out 8
Writes to the data register that stores the value to be driven on the pad in Output mode.
7
MPPDO7
Masked Parallel Pad Data Out 7
Writes to the data register that stores the value to be driven on the pad in Output mode.
6
MPPDO6
Masked Parallel Pad Data Out 6
Writes to the data register that stores the value to be driven on the pad in Output mode.
5
MPPDO5
Masked Parallel Pad Data Out 5
Writes to the data register that stores the value to be driven on the pad in Output mode.
4
MPPDO4
Masked Parallel Pad Data Out 4
Writes to the data register that stores the value to be driven on the pad in Output mode.
3
MPPDO3
Masked Parallel Pad Data Out 3
Writes to the data register that stores the value to be driven on the pad in Output mode.
2
—
Reserved
Always write zero to this field.
1
MPPDO1
Masked Parallel Pad Data Out 1
Writes to the data register that stores the value to be driven on the pad in Output mode.
0
MPPDO0
Masked Parallel Pad Data Out 0
Writes to the data register that stores the value to be driven on the pad in Output mode.
10.6.38 Masked Parallel GPIO Pad Data Output (MPGPDO9 - MPGPDO19)
Offset
For a = 9 to 19:
Register
Offset
MPGPDOa
1780h + (a × 4h)
Function
Modifies the pad values associated with PGPDOn selectively and supports only 32-bit accesses. It does not support byte and 
half-word accesses.
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
488 / 5251


---
# 페이지 438

 
Access this register only with 32-bit writes. 8-bit or 16-bit writes do not modify any bits in the register resulting in a 
transfer error. Read access returns 0.
  NOTE  
The accesses to each of this register location is coherent with access to the bitwise GPDOn.
For a given MPGPDOx[MPPDOy], where x is the register instance index and y is the field index, the following equation shows the 
equivalent GPDOn[PDO_n]:
MPGPDOx[MPPDOy] = GPDO(x × 16) + (15 - y)[PDO_(x × 16) + (15 - y)]
Following are some of the examples of mapping:
• MPGPDO0[MPPDO15] = GPDO0[PDO_0]
• MPGPDO2[MPPDO15] = GPDO32[PDO_32]
• MPGPDO31[MPPDO0] = GPDO511[PDO_511]
Diagram
Bits
31
30
29
28
27
26
25
24
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
MASK
15 
MASK
14 
MASK
13 
MASK
12 
MASK
11 
MASK
10 
MASK
9 
MASK
8 
MASK
7 
MASK
6 
MASK
5 
MASK
4 
MASK
3 
MASK
2 
MASK
1 
MASK
0 
Reset
0
0
0
0
0
0
0
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
0
0
0
W
MPPD
O15 
MPPD
O14 
MPPD
O13 
MPPD
O12 
MPPD
O11 
MPPD
O10 
MPPD
O9 
MPPD
O8 
MPPD
O7 
MPPD
O6 
MPPD
O5 
MPPD
O4 
MPPD
O3 
MPPD
O2 
MPPD
O1 
MPPD
O0 
Reset
0
0
0
0
0
0
0
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
MASK15
Mask Field 15
Masks MPPDO15 in the corresponding MPGPDOn register instance.
0b - MPPDO15 is ignored
1b - MPPDO15 is written
30
MASK14
Mask Field 14
Masks MPPDO14 in the corresponding MPGPDOn register instance.
0b - MPPDO14 is ignored
1b - MPPDO14 is written
29
MASK13
Mask Field 13
Masks MPPDO13 in the corresponding MPGPDOn register instance.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
489 / 5251


---
# 페이지 439

Table continued from the previous page...
Field
Function
0b - MPPDO13 is ignored
1b - MPPDO13 is written
28
MASK12
Mask Field 12
Masks MPPDO12 in the corresponding MPGPDOn register instance.
0b - MPPDO12 is ignored
1b - MPPDO12 is written
27
MASK11
Mask Field 11
Masks MPPDO11 in the corresponding MPGPDOn register instance.
0b - MPPDO11 is ignored
1b - MPPDO11 is written
26
MASK10
Mask Field 10
Masks MPPDO10 in the corresponding MPGPDOn register instance.
0b - MPPDO10 is ignored
1b - MPPDO10 is written
25
MASK9
Mask Field 9
Masks MPPDO9 in the corresponding MPGPDOn register instance.
0b - MPPDO9 is ignored
1b - MPPDO9 is written
24
MASK8
Mask Field 8
Masks MPPDO8 in the corresponding MPGPDOn register instance.
0b - MPPDO8 is ignored
1b - MPPDO8 is written
23
MASK7
Mask Field 7
Masks MPPDO7 in the corresponding MPGPDOn register instance.
0b - MPPDO7 is ignored
1b - MPPDO7 is written
22
MASK6
Mask Field 6
Masks MPPDO6 in the corresponding MPGPDOn register instance.
0b - MPPDO6 is ignored
1b - MPPDO6 is written
21
Mask Field 5
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
490 / 5251


---
# 페이지 440

Table continued from the previous page...
Field
Function
MASK5
Masks MPPDO5 in the corresponding MPGPDOn register instance.
0b - MPPDO5 is ignored
1b - MPPDO5 is written
20
MASK4
Mask Field 4
Masks MPPDO4 in the corresponding MPGPDOn register instance.
0b - MPPDO4 is ignored
1b - MPPDO4 is written
19
MASK3
Mask Field 3
Masks MPPDO3 in the corresponding MPGPDOn register instance.
0b - MPPDO3 is ignored
1b - MPPDO3 is written
18
MASK2
Mask Field 2
Masks MPPDO2 in the corresponding MPGPDOn register instance.
0b - MPPDO2 is ignored
1b - MPPDO2 is written
17
MASK1
Mask Field 1
Masks MPPDO1 in the corresponding MPGPDOn register instance.
0b - MPPDO1 is ignored
1b - MPPDO1 is written
16
MASK0
Mask Field 0
Masks MPPDO0 in the corresponding MPGPDOn register instance.
0b - MPPDO0 is ignored
1b - MPPDO0 is written
15
MPPDO15
Masked Parallel Pad Data Out 15
Writes to the data register that stores the value to be driven on the pad in Output mode.
14
MPPDO14
Masked Parallel Pad Data Out 14
Writes to the data register that stores the value to be driven on the pad in Output mode.
13
MPPDO13
Masked Parallel Pad Data Out 13
Writes to the data register that stores the value to be driven on the pad in Output mode.
12
Masked Parallel Pad Data Out 12
Writes to the data register that stores the value to be driven on the pad in Output mode.
Table continues on the next page...
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
491 / 5251


---
# 페이지 441

Table continued from the previous page...
Field
Function
MPPDO12
11
MPPDO11
Masked Parallel Pad Data Out 11
Writes to the data register that stores the value to be driven on the pad in Output mode.
10
MPPDO10
Masked Parallel Pad Data Out 10
Writes to the data register that stores the value to be driven on the pad in Output mode.
9
MPPDO9
Masked Parallel Pad Data Out 9
Writes to the data register that stores the value to be driven on the pad in Output mode.
8
MPPDO8
Masked Parallel Pad Data Out 8
Writes to the data register that stores the value to be driven on the pad in Output mode.
7
MPPDO7
Masked Parallel Pad Data Out 7
Writes to the data register that stores the value to be driven on the pad in Output mode.
6
MPPDO6
Masked Parallel Pad Data Out 6
Writes to the data register that stores the value to be driven on the pad in Output mode.
5
MPPDO5
Masked Parallel Pad Data Out 5
Writes to the data register that stores the value to be driven on the pad in Output mode.
4
MPPDO4
Masked Parallel Pad Data Out 4
Writes to the data register that stores the value to be driven on the pad in Output mode.
3
MPPDO3
Masked Parallel Pad Data Out 3
Writes to the data register that stores the value to be driven on the pad in Output mode.
2
MPPDO2
Masked Parallel Pad Data Out 2
Writes to the data register that stores the value to be driven on the pad in Output mode.
1
MPPDO1
Masked Parallel Pad Data Out 1
Writes to the data register that stores the value to be driven on the pad in Output mode.
0
MPPDO0
Masked Parallel Pad Data Out 0
Writes to the data register that stores the value to be driven on the pad in Output mode.
NXP Semiconductors
System Integration Unit Lite2 (SIUL2)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
492 / 5251


---