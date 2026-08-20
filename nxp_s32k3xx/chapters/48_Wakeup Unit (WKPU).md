# 페이지 230

Chapter 48
Wakeup Unit (WKPU)
48.1 Chip-specific WKPU information
48.1.1 WKPU configuration on the chip
WKPU provides the following features:
• A configurable, low-power wake-up capability to the chip from multiple configurable asynchronous wake-up events.
• Support for four internal and up to 60 external source that can generate interrupts or wake-up events.
• Support for an NMI input.
Table 268. WKPU configuration on the chip
Number of 
sources, interrupts, 
and vectors
S32K311/S32K310
S32K312/
S32K342/
S32K341/S32K322
S32K344/
S32K324/S32K314
S32K388/
S32K358/
S32K348/
S32K338/
S32K328/S32K389
Description
NMI sources
1
1
1
1
Single NMI pin 
routed to all 
application cores
Internal wake-up 
sources1
4
4
4
4
• SWT_0 wake-
up, RTC-API 
wake-up
• RTC timeout
• Analog 
comparator 
round robin 
wake-up (from 
LPCMP_0, 1, 
and 2 round 
robin wake-
up)2
• RTI wake-up
External wake-up 
sources
33
59
60
67 3
See the IOMUX 
file attached to 
this document for 
details about the 
number of wake 
up pins and 
their assignment 
to each wake up 
source.
Table continues on the next page...
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1888 / 5251


---
# 페이지 231

Table 268. WKPU configuration on the chip (continued)
Number of 
sources, interrupts, 
and vectors
S32K311/S32K310
S32K312/
S32K342/
S32K341/S32K322
S32K344/
S32K324/S32K314
S32K388/
S32K358/
S32K348/
S32K338/
S32K328/S32K389
Description
Glitch filters for 
external interrupts
33
59
60
67
Glitch filter on each 
external wake-up 
source
External interrupt 
vectors
8
8
8
8
—
1. Internal wakeup sources have only positive polarity, therefore, must not be configured for negedge triggered functionality.
2. Both wake-up sources 0 (RTC-API) and 2 (CMP_x trigger mode wake-up) use RTC-API wake-up, with Trigger mode 
having a higher priority. This means, if you configure LPCMP_x.RRCR0[ERR_EN] for either of the comparators, the 
RTC_API wake-up is used only for the CMP_x trigger mode operation. The RTC-API wake-up does not cause wake-up 
from Standby mode in this scenario.
3. Some of external sources are sharing the same WKPU channels. Please see DCM_GPR chapter to select one from 
multiple external sources.
All of the aforementioned wake-up sources can be enabled or disabled. Also, you can configure these wake-up sources, by using 
WKPU configuration registers, to provide wake-up on rising or falling events. See the WKPU register memory map for details.
 
You must use SIUL2 to perform WKPU pin configurations (PUE, PUS, and IBE). For this, you must first configure 
SIUL2.MSCR[IBE] for the corresponding pin. This chip does not support WKPU-provided pin configurations; it 
supports only bypass control.
  NOTE  
Two kinds of BYPASS connectivity for alternate glitch filters
Below figure is related to the BYPASS functionality of the Analog glitch filters associated with external wakeup pins.
48.1.2 WKPU register fields and their applicability
Table 269. WKPU register fields and applicability
Register
Field
Chips where applicable
NSR
NIF1
S32K324, S32K322
NSR
NOVF1
S32K324, S32K322
NSR
NIF3, NOVF3
S32K388/S32K389
NCR
NLOCK1
S32K324, S32K322
NCR
NDSS1
S32K324, S32K322
NCR
NWRE1
S32K324, S32K322
NCR
NREE1
S32K324, S32K322
NCR
NFEE1
S32K324, S32K322
NCR
NFE1
S32K324, S32K322
NCR
NLOCK3, NDSS3, NWRE3, 
NREE3, NFEE3, NFE3
S32K388/S32K389
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1889 / 5251


---
# 페이지 232

48.1.3 WKPU NMI configuration
WKPU supports one external source that can cause non-maskable interrupts to on-chip cores and wake-up events to the system.
The following figure shows applicable cores, some family chips may not have cores Cortex-M7_1, Cortex-M7_2 or Coretex-M7_3. 
In case of a wake-up event (internal or external), WKPU initiates the recovery of the chip and feeds an interrupt to the core(s) 
depending on the configuration. The sections that follow provide details related to the associated configurations.
NDSS[0]
NWRE[0]
NREE[0]
NFEE[0]
Edge detect
Destination
Edge detect
Glitch filter
NMI
Cortex-M7_0
Nonmaskable interrupt
Nonmaskable interrupt
Cortex-M7_1
Destination
System wake-up
Flag
Overrun
Flag
Overrun
NDSS[1]
NWRE[1]
NREE[1]
NFEE[1]
NMI Configuration Register (NCR)
NFE[0]
Edge detect
Nonmaskable interrupt
Cortex-M7_2
Destination
Flag
Overrun
NDSS[2]
NWRE[2]
NREE[2]
NFEE[2]
Edge detect
Nonmaskable interrupt
Cortex-M7_3
Destination
Flag
Overrun
NDSS[3]
NWRE[3]
NREE[3]
NFEE[3]
Figure 199. WKPU NMI configuration
48.1.4 WKPU wake-up source connectivity
WKPU allows the external NMI pin to assert the core NMIs on the chip. NMI supports NSR's status and overrun flags. This is what 
you could do using NCR:
• Control the NMI destination interrupt by configuring NCR[NDSS].
• Control the rising edge, falling edge, or either of the edge reactions to the NMI pin by using bits 2:0 of NCR[NFEE] and 
NCR[NREE]. The enabling of these edge reactions to the NMI pin is independent of each core.
WKPU supports the capturing of a second event per NMI input before the interrupt is cleared, thus reducing the chance of losing 
an NMI event.
The following figure shows routing of external wake-up events or interrupts with WKPU and the system interrupt controller.
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1890 / 5251


---
# 페이지 233

Interrupt
controller
Mode and
power control
IRER_64[31:0]
Interrupt vectors
Glitch filter enable
Interrupt enable
Edge detection
Flag[31:24]
Flag[23:16]
Flag[15:8]
Flag[7:0]
OR
WIFER_64[31:0]
WISR_64[31:0]
WIREER_64[31:0]
WIFEER_64[31:0]
Rising
Falling
Interrupt edge enable
OR
OR
OR
Analog glitch filter
External wake-up pins
IRER[31:0]
Glitch filter enable
Interrupt enable
Edge detection
Flag[31:24]
Flag[23:16]
Flag[15:8]
Flag[7:0]
OR
WIFER[31:0]
WISR[31:0]
WRER[31:0]
Wake-up enable
WRER_64[31:0]
WIREER[31:0]
WIFEER[31:0]
Rising
Falling
Interrupt edge enable
OR
OR
OR
Analog glitch filter
External wake-up pins
CMP_0 round-robin wake-up
CMP_1 round-robin wake-up
RTI wake-up
CMP_2 round-robin wake-up
SWT_0 timeout
RTC timeout
RTC API wake-up
Figure 200. WKPU wake-up source connectivity
This is the wake-up source mapping to WKPU:
• Wake-up source 0 : SWT_0 timeout, RTC-API API wake-up
• Wake-up source 1 : RTC-API RTC timeout
• Wake-up source 2 : Round robin wake-up interrupt (Trigger mode interrupt) from LPCMP_0, LPCMP_1, or LPCMP_2
• Wake-up source 3 : RTI wake-up
• Wake-up source 4 : Wake-up source up to 60-external pin wake-up sources, WKPU[0]-WKPU[59]
If you configure any or all of the LPCMP_x.RRCR0[RR_EN] fields to be active, the corresponding CMP_x pins must be dedicated 
for the CMP_x operation. In case you are not using any of the CMPs, you can use SIUL2.MSCRx[SSS] to configure the pins for 
digital functionalities.
 
You must enable WKPU (by using MC_ME.PRTNx_COFBy_CLKEN) before entering any of the chip's low-
power modes.
  NOTE  
48.2 Overview
WKPU supports 64 external sources that can generate interrupts or wake-up events, and 0 external sources that can cause 
nonmaskable interrupt requests or wake-up events. Additionally, it combines its wake-up events with those generated by other 
wake-up sources to supply a single wake-up to the system.
48.2.1 Block diagram
The following figure shows WKPU and its interfaces with the other system components.
 
The signal widths in the following diagram do not depict a particular configuration of this chip. See the chip-specific 
WKPU information for details.
  NOTE  
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1891 / 5251


---
# 페이지 234

NMI or wake-up
configuration
IRQ or wake-up
configuration
Platform
Peripheral bus
WKPU
Mode and
power control
Pads
IOMUX
Filter
0-4
0-4
NMI enable
Filter bypass
Filter bypass
System wake-up
IRQs
Wake-up
0-4
0-4
0-4
Filter
Interrupt
controller
0-64
Modules such
as STIMER
0-64
Figure 201. Block diagram
48.2.2 Features
• Supports nonmaskable interrupts including:
— 4 NMI sources
— 4 analog glitch filters
— Independent interrupt destination for each core:
◦Nonmaskable interrupt
◦Critical interrupt
— Active edge selection control (rise and fall) for events
— Configurable system wake-up triggering from NMI sources
• Supports external wake-up and interrupts that include the following:
— One System interrupt vector for interrupt sources
— 64 analog glitch filters
— Independent interrupt mask
— Edge detection
— Configurable system wake-up triggering from all interrupt sources
48.3 Functional description
48.3.1 Nonmaskable interrupts
WKPU supports the capturing of the second event according to the NMI input before the interrupt becomes 0. This reduces the 
chance of losing an NMI event, although it creates an overrun condition.
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1892 / 5251


---
# 페이지 235

Each NMI passes through a bypassable analog glitch filter.
 
When NMI is disabled, glitch filter control and pad configuration perform. This prevents erroneous triggering by 
glitches caused by the configuration process itself.
  NOTE  
 
The following figure represents a generic configuration and does not represent the configuration of this specific 
chip. See the chip-specific information for details on this chip's WKPU.
  NOTE  
CPU
MMI
Destination
Flag
Edge detect
Wake-up enable
Overrun
NDSS[0]
NWRE[0]
NREE[0]
NFEE[0]
NFE[0]
Critical IRQ
Machine check
Glitch filter
CPU
MMI
Destination
Flag
Edge detect
Wake-up enable
NMI Configuration Register (NCR)
Overrun
NDSS[1]
NWRE[1]
NREE[1]
NFEE[1]
NFE[1]
Critical IRQ
Machine check
Glitch filter
CPU
MMI
Destination
Flag
Edge detect
Wake-up enable
Overrun
NDSS[2]
NWRE[2]
NREE[2]
NFEE[2]
NFE[2]
Critical IRQ
Machine check
Glitch filter
CPU
MMI
Destination
Flag
Edge detect
Wake-up enable
Overrun
NDSS[3]
NWRE[3]
NREE[3]
NFEE[3]
NFE[3]
Critical IRQ
Machine check
Glitch filter
Mode and
power control
Figure 202. NMI pad diagram
48.3.1.1
NMI management
You can enable or disable each NMI independently. You can perform this by using the registers, NCR which are laid out to contain 
all configuration bits for a given NMI in a single byte (see NMI Configuration (NCR)). You can configure a pad defined as an NMI 
to recognize interrupts with an active rising edge, falling edge, or both edges being active. If both the edge events are disabled, 
it results in no interrupt being detected and does not get configured.
You can also control an active NMI edge through the configuration of the fields, NCR[NREEn] and NCR[NFEEn].
 
After a reset, NREE and NFEE are set to 0, which disables the NMI functionality and software enables it explicitly.
  NOTE  
After a pad's NMI functionality is enabled, the pad cannot be reconfigured to override or disable the NMI. See the chip-specific 
WKPU information for details of NMI implementation.
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1893 / 5251


---
# 페이지 236

Additionally, you can control the NMI destination interrupt through the configuration of the field, NCR[NDSSn]. See NMI 
Configuration (NCR) for details.
Each NMI supports a status flag and an overrun flag, both of which are located in NMI Status Flag (NSR). This register prevents 
an inadvertent overwriting of the other flags in the same register. The status flag is set whenever an NMI event is detected. 
The overrun flag is set whenever an NMI event is detected when the status flag is still set (that is, the status flag has not yet 
been cleared).
 
The overrun flag is cleared by writing 1 to the appropriate overrun field in NMI Status Flag (NSR). If the status field 
is 0 but the overrun field is still, the pending interrupt is not cleared.
During an NMI ISR, on wake-up of the chip from an NMI, any writes to the ECC-protected memory must have the 
correct ECC.
  NOTE  
48.3.2 Clocking
This module has no clocking considerations.
WKPU has ipg_clk and ipg_clk_s as input clocks having the same clock frequency for register configuration and internal logic.
48.3.3 Interrupts
WKPU supports 4 interrupt vectors to the interrupt controller of the chip. Each interrupt vector supports multiple external interrupt 
sources from the device pads, with the total across all vectors being equal to the number of external interrupt sources. Each 
external interrupt source is assigned to exactly one interrupt vector. The interrupt vector assignment follows a sequence: one 
interrupt vector is for external interrupt sources 0 to N-1, the next is for N to N+M-1, and so on.
See the following figure for an overview of the external interrupt implementation, showing an example of four interrupt vectors with 
eight external interrupt sources each.
 
The following figure represents a generic WKPU configuration. For details on this chip's configuration, see the 
chip-specific WKPU information.
  NOTE  
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1894 / 5251


---
# 페이지 237

Interrupt
vectors
Interrupt
controller
Mode and
power control
Interrupt enable
Edge detection
Flag[7:0]
Flag[15:8]
Flag[23:16]
Flag[31:24]
IRER
IRQ_31_24
OR
IRQ_23_16
OR
IRQ_15_08
OR
IRQ_07_00
OR
Analog glitch filter
Pads
WIFER
Glitch filter enable
WISR
WRER
Wake-up enable
WIREER
Rising
WIFEER
Falling
Interrupt edge enable
Figure 203. External interrupt pad diagram
All the external interrupt pads within a single group have equal priority. You must search through the group of sources in the most 
appropriate way for their application.
The priority of the vectors used by the external interrupt pads is set based on the platform and the priority levels of the interrupt 
controller. However, the chip can allow an independent configuration of pad allocation to each group of interrupts.
The external interrupt lines have a digital glitch filter applied to them.
48.3.3.1
External interrupt management
You can enable or disable each external interrupt independently using a single rolled-up register (Interrupt Request Enable 
(IRER)). You can configure a pad defined as an external interrupt to recognize interrupts with an active rising edge, an active falling 
edge, or both edges being active.
 
Writing 0 to both IREE[n] and IFEE[n] disables the external interrupt functionality for that pad completely (means 
no system wake-up or interrupt is generated from any activity on that pad).
  NOTE  
You can control an active IRQ edge through the configuration of the registers, WIREER and WIFEER.
Each external interrupt supports an individual flag, which is held in the flag register, WISR. This W1C register prevents inadvertent 
overwriting of other flags in the same register.
48.3.4 External signals
This module has no external signals.
48.4 Initialization
To initialize this module, you must perform the following configuration:
• Glitch filter and pad configuration
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1895 / 5251


---
# 페이지 238

• Nonmaskable interrupts
• Wake-up event
48.4.1 Glitch filter and pad configuration
You can perform glitch filter control and pad configuration when the NMI is disabled to avoid erroneous triggering by glitches 
caused by the configuration process.
When enabling the glitch filter, do not enable the rising and falling-edge events bits (that is, the NCR[NREE], NCR[NFEE], 
NCR[NREE], and NCR[NFEE]) in the same register write.
48.4.2 Nonmaskable interrupts
If IBE of NMI is tied off to 1, no false interrupt is expected.
48.4.3 Wake-up event
See the chip-specific WKPU information for wake-up event initialization.
48.5 WKPU memory map and registers
48.5.1 WKPU register descriptions
This section provides a detailed description of all the registers accessible in the WKPU module.
 
Reserved registers read as zero and writes have no effect. A transfer error is generated when trying to access a 
completely reserved register space. The field length of external pad control registers depends on the number of 
WKPU channels implemented in a chip.
  NOTE  
48.5.1.1
WKPU memory map
WKPU base address: 402B_4000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
NMI Status Flag (NSR)
32
RW
0000_0000h
8h
NMI Configuration (NCR)
32
RW
6060_6060h
14h
Wake-Up and Interrupt Status Flag (WISR)
32
RW
0000_0000h
18h
Interrupt Request Enable (IRER)
32
RW
0000_0000h
1Ch
Wake-Up Request Enable (WRER)
32
RW
0000_0000h
28h
Wake-Up and Interrupt Rising-Edge Event Enable (WIREER)
32
RW
0000_0000h
2Ch
Wake-Up and Interrupt Falling-Edge Event Enable (WIFEER)
32
RW
0000_0000h
30h
Wake-Up and Interrupt Filter Enable (WIFER)
32
RW
0000_0000h
54h
Wake-Up and Interrupt Status Flag (WISR_64)
32
RW
0000_0000h
58h
Interrupt Request Enable (IRER_64)
32
RW
0000_0000h
5Ch
Wake-Up Request Enable (WRER_64)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1896 / 5251


---
# 페이지 239

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
68h
Wake-Up and Interrupt Rising-Edge Event Enable (WIREER_64)
32
RW
0000_0000h
6Ch
Wake-Up and Interrupt Falling-Edge Event Enable (WIFEER_64)
32
RW
0000_0000h
70h
Wake-Up and Interrupt Filter Enable (WIFER_64)
32
RW
0000_0000h
48.5.1.2
NMI Status Flag (NSR)
Offset
Register
Offset
NSR
0h
Function
Holds the nonmaskable interrupt status flags.
 
This register is accessible by 8-, 16-, and 32-bit read/write operations.
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
NIF0 
NOVF
0 
Reserved 
NIF1 
NOVF
1 
Reserved 
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
NIF2 
NOVF
2 
Reserved 
NIF3 
NOVF
3 
Reserved 
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
Fields
Field
Function
31
NIF0
NMI Status Flag 0
Causes an interrupt request when an event, as defined by NREE0 and NFEE0, has occurred.
If NREE0 or NFEE0 is 1, this flag causes an interrupt request.
Table continues on the next page...
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1897 / 5251


---
# 페이지 240

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No event occurred on the pad
1b - An event occurred
When writing
0b - No effect
1b - Clear the flag
30
NOVF0
NMI Overrun Status Flag 0
Indicates whether an overrun has occurred on NMI input 0.
This flag has the same current value as of NIF0 (when the NMI event occurs), indicating that the 
NMI occurred when the previous one was not serviced. If NREE0 or NFEE0 is 1, this flag causes an 
interrupt request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No overrun occurred
1b - An overrun occurred
When writing
0b - No effect
1b - Clear the flag
29-24
—
Reserved
23
NIF1
NMI Status Flag 1
Causes an interrupt request when an event, as defined by NREE1 and NFEE1, has occurred.
If NREE1 or NFEE1 is 1, this flag causes an interrupt request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No event occurred on the pad
1b - An event occurred
When writing
Table continues on the next page...
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1898 / 5251


---
# 페이지 241

Table continued from the previous page...
Field
Function
0b - No effect
1b - Clear the flag
22
NOVF1
NMI Overrun Status Flag 1
Indicates whether an overrun has occurred on NMI input 1.
This flag has the same current value as of NIF1 (when the NMI event occurs), indicating that the 
NMI occurred when the previous one was not serviced. If NREE1 or NFEE1 is 1, this flag causes an 
interrupt request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No overrun occurred
1b - An overrun occurred
When writing
0b - No effect
1b - Clear the flag
21-16
—
Reserved
15
NIF2
NMI Status Flag 2
Causes an interrupt request when an event, as defined by NREE2 and NFEE2, has occurred.
If NREE2 or NFEE2 is 1, this flag causes an interrupt request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No event occurred on the pad
1b - An event occurred
When writing
0b - No effect
1b - Clear the flag
14
NOVF2
NMI Overrun Status Flag 2
Indicates whether an overrun has occurred on NMI input 2.
This flag has the same current value as of NIF2 (when the NMI event occurs), indicating that the 
NMI ocuurred when the previous one was not serviced. If NREE2 or NFEE2 is 1, this flag causes an 
interrupt request.
Table continues on the next page...
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1899 / 5251


---
# 페이지 242

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No overrun occurred
1b - An overrun occurred
When writing
0b - No effect
1b - Clear the flag
13-8
—
Reserved
7
NIF3
NMI Status Flag 3
Causes an interrupt request when an event, as defined by NREE3 and NFEE3, has occurred.
If NREE3 or NFEE3 is 1, this flag causes an interrupt request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No event occurred on the pad
1b - An event occurred
When writing
0b - No effect
1b - Clear the flag
6
NOVF3
NMI Overrun Status Flag 3
Indicates whether an overrun has occurred on NMI input 3.
This flag has the same current value as of NIF3 (when the NMI event occurs), indicating that the 
NMI occurred when the previous one was not serviced. If NREE3 or NFEE3 is 1, this flag causes an 
interrupt request.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No overrun occurred
1b - An overrun occurred
When writing
Table continues on the next page...
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1900 / 5251


---
# 페이지 243

Table continued from the previous page...
Field
Function
0b - No effect
1b - Clear the flag
5-0
—
Reserved
48.5.1.3
NMI Configuration (NCR)
Offset
Register
Offset
NCR
8h
Function
Holds the configuration fields for the nonmaskable interrupt settings.
 
• This register is accessible by 8-, 16-, and 32-bit read/write operations.
• Writing 0 to both NREE[n] and NFEE[n] disables the NMI functionality completely (means no nonmaskable 
interrupt is generated on any pad activity).
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
NLOC
K0 
NDSS0 
NWRE
0 
0
NREE
0 
NFEE0 
NFE0 
NLOC
K1 
NDSS1 
NWRE
1 
0
NREE
1 
NFEE1 
NFE1 
W
Reset
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
NLOC
K2 
NDSS2 
NWRE
2 
0
NREE
2 
NFEE2 
NFE2 
NLOC
K3_...
NDSS3_RDSS 
NWRE
3_R...
0
NREE
3_R...
NFEE3
_R...
NFE3 
W
Reset
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
0
0
Fields
Field
Function
31
NLOCK0
NMI Configuration Lock Register 0
Specifies the lock configuration for the NMI.
Table continues on the next page...
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1901 / 5251


---
# 페이지 244

Table continued from the previous page...
Field
Function
When you write 1 to this field, it locks the configuration for the NMI until it is unlocked by a system reset or 
Standby0 mode exit.
0b - No effect
1b - Locks the configuration for the NMI
30-29
NDSS0
NMI Destination Source Select 0
Specifies the NMI destination interrupt to platform.
 
As wake-up interrupt does not support another interrupt than NMI, the destination source 
select signal bits are reserved and always retain their reset value. This means no other 
request other than NMI can be generated.
  NOTE  
00b - Nonmaskable interrupt
01b - Reserved
10b - Reserved
11b - Reserved. Reserved
28
NWRE0
NMI Wake-Up Request Enable 0
Enables a system wake-up request when the corresponding NIF0 = 1 or NOVFO = 1.
0b - Disable
1b - Enable
27
—
Reserved
26
NREE0
NMI Rising-Edge Events Enable 0
Enables the NMI rising-edge event.
0b - Disable
1b - Enable
25
NFEE0
NMI Falling-Edge Events Enable 0
Enables the NMI falling-edge event.
0b - Disable
1b - Enable
24
NFE0
NMI Filter Enable 0
Enables analog glitch filter on the NMI pad input.
0b - Disable
Table continues on the next page...
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1902 / 5251


---
# 페이지 245

Table continued from the previous page...
Field
Function
1b - Enable
23
NLOCK1
NMI Configuration Lock 1
Specifies the lock configuration for the NMI.
When you write 1 to this field, it locks the configuration for the NMI until it is unlocked by a system reset or 
Standby0 mode exit.
0b - No effect
1b - Locks the configuration for the NMI
22-21
NDSS1
NMI Destination Source Select 1
Specifies the NMI destination interrupt to platform.
 
As wake-up does not support another interrupt than NMI, the destination source select 
signal bits are reserved and always retain their reset value. This means no other request 
other than NMI can be generated.
  NOTE  
00b - Nonmaskable interrupt
01b - Reserved
10b - Reserved
11b - Reserved
20
NWRE1
NMI Wake-Up Request Enable 1
Enables a system wake-up request when the corresponding NIF1 = 1 or NOVF1 = 1.
0b - Disable
1b - Enable
19
—
Reserved
18
NREE1
NMI Rising-Edge Events Enable 1
Enables the NMI rising-edge event.
0b - Disable
1b - Enable
17
NFEE1
NMI Falling-Edge Events Enable 1
Enables the NMI falling-edge event.
0b - Disable
1b - Enable
Table continues on the next page...
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1903 / 5251


---
# 페이지 246

Table continued from the previous page...
Field
Function
16
NFE1
NMI Filter Enable 1
Enables analog glitch filter on the NMI pad input.
0b - Disable
1b - Enable
15
NLOCK2
NMI Configuration Lock 2
Specifies the lock configuration for the NMI.
When you write 1 to this field, it locks the configuration for the NMI until it is unlocked by a system reset.
0b - No effect
1b - Locks the configuration for the NMI
14-13
NDSS2
NMI Destination Source Select 2
Specifies the NMI destination interrupt to platform.
 
Because wake-up does not support any other interrupt other than NMI, the destination 
source select signal bits are reserved and always retain their reset value. This means no 
other request other than NMI can be generated.
  NOTE  
00b - Nonmaskable interrupt
01b - Reserved
10b - Reserved
11b - Reserved
12
NWRE2
NMI Wake-Up Request Enable 2
Enables a system wake-up request when the corresponding NIF2 = 1 or NOVF2 =1.
0b - Disable
1b - Enable
11
—
Reserved
10
NREE2
NMI Rising-Edge Events Enable 2
Enables the NMI rising-edge event.
0b - Disable
1b - Enable
9
NFEE2
NMI Falling-Edge Events Enable 2
Enables the NMI falling-edge event.
Table continues on the next page...
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1904 / 5251


---
# 페이지 247

Table continued from the previous page...
Field
Function
0b - Disable
1b - Enable
8
NFE2
NMI Filter Enable 2
Enables analog glitch filter on the NMI pad input.
0b - Disable
1b - Enable
7
NLOCK3_RLO
CK
NMI Configuration Lock Register 3
Specifies the lock configuration for the NMI.
When you write 1 to this field, it locks the configuration for the NMI until it is unlocked by a system reset .
0b - No effect
1b - Locks the configuration for the NMI
6-5
NDSS3_RDSS
NMI Destination Source Select 3. .
00b - Nonmaskable interrupt
01b - Reserved
10b - Reserved
11b - Reserved
4
NWRE3_RWRE
NMI Wake-Up Request Enable 3
Enables system wake-up requests.
0b - System wake-up requests from the corresponding NIF3 bit are disabled
1b - NIF3 or NOVF3 being set causes a system wake-up request
3
—
Reserved
2
NREE3_RREE
NMI Rising-Edge Events Enable 3.
Enables the NMI rising-edge event.
0b - Disable
1b - Enable
1
NFEE3_RFEE
NMI Falling-Edge Events Enable 3
Enables the NMI falling-edge event.
0b - Disable
1b - Enable
0
NMI Filter Enable 3
Table continues on the next page...
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1905 / 5251


---
# 페이지 248

Table continued from the previous page...
Field
Function
NFE3
Enables analog glitch filter on the NMI pad input.
0b - Disable
1b - Enable
48.5.1.4
Wake-Up and Interrupt Status Flag (WISR)
Offset
Register
Offset
WISR
14h
Function
Holds the wake-up and interrupt flags.
 
• This register is accessible only by 32-bit read/write operations.
• The status fields associated with on-chip wake-up sources are located to the left of the external wake-up and 
interrupt status fields and are read-only. The wake-up for these sources must be configured and cleared at 
the on-chip wake-up source. Also, the configuration registers for the external interrupts/wake-ups do not have 
corresponding bits.
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
EIF 
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
EIF 
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
31-0
EIF
External Wake-Up and Interrupt Status Flag
Table continues on the next page...
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1906 / 5251


---
# 페이지 249

Field
Function
Specifies whether an event, as defined by WIREER and WIFEER, has occurred on the pad. If enabled 
(IRER[n]), EIF[n] causes an interrupt request.
0b - No event occurred
1b - An event occurred
48.5.1.5
Interrupt Request Enable (IRER)
Offset
Register
Offset
IRER
18h
Function
Enables the interrupt messaging from the wake-up and interrupt pads to the interrupt controller.
 
This register is accessible only by 32-bit read/write operations.
If a pin is disabled through this register, you must write 0 to the corresponding fields in WIFEER and WIREER to 
ensure that the pin does not respond to any change.
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
EIRE 
W
Reset
0
0
0
0
0
0
0
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
EIRE 
W
Reset
0
0
0
0
0
0
0
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
EIRE
External Interrupt Request Enable
Enables interrupt requests from the corresponding field, EIF[n].
0b - Disable
1b - Enable (with EIF[n] set)
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1907 / 5251


---
# 페이지 250

48.5.1.6
Wake-Up Request Enable (WRER)
Offset
Register
Offset
WRER
1Ch
Function
Enables the system wake-up messaging from the wake-up and interrupt pads to the mode entry and power control modules.
 
This register is accessible only by 32-bit read/write operations.
If a pin is disabled through this register, you must write 0 to the corresponding fields in WIFEER and WIREER to 
ensure that the pin does not respond to any change.
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
WRE 
W
Reset
0
0
0
0
0
0
0
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
WRE 
W
Reset
0
0
0
0
0
0
0
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
WRE
External Wake-Up Request Enable
Enables system wake-up requests from the corresponding field, EIF[n].
0b - Disable
1b - Enable (with EIF[n] set)
48.5.1.7
Wake-Up and Interrupt Rising-Edge Event Enable (WIREER)
Offset
Register
Offset
WIREER
28h
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1908 / 5251


---
# 페이지 251

Function
Enables rising-edge triggered events on the corresponding wake-up/interrupt pads.
 
• This register is accessible only by 32-bit read/write operations.
• WIREER or WIFEER is configured for rising or falling edge after WRER to enable wake-up source.
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
IREE 
W
Reset
0
0
0
0
0
0
0
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
IREE 
W
Reset
0
0
0
0
0
0
0
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
IREE
External Interrupt Rising-Edge Events Enable
Enables interrupt rising-edge event.
0b - Disable
1b - Enable
48.5.1.8
Wake-Up and Interrupt Falling-Edge Event Enable (WIFEER)
Offset
Register
Offset
WIFEER
2Ch
Function
Enables falling-edge triggered events on the corresponding wake-up and interrupt pads.
 
• This register is accessible only by 32-bit read/write operations.
• WIREER or WIFEER is configured for rising or falling edge after WRER to enable wake-up source.
  NOTE  
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1909 / 5251


---
# 페이지 252

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
IFEEx 
W
Reset
0
0
0
0
0
0
0
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
IFEEx 
W
Reset
0
0
0
0
0
0
0
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
IFEEx
External Interrupt Falling-Edge Events Enable
Enables interrupt falling-edge event.
0b - Disable
1b - Enable
48.5.1.9
Wake-Up and Interrupt Filter Enable (WIFER)
Offset
Register
Offset
WIFER
30h
Function
Enables an analog filter on the corresponding interrupt pads to filter out glitches on the inputs.
 
This register is accessible only by 32-bit read/write operations.
  NOTE  
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1910 / 5251


---
# 페이지 253

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
IFE 
W
Reset
0
0
0
0
0
0
0
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
IFE 
W
Reset
0
0
0
0
0
0
0
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
IFE
External Interrupt Filter Enable
Enables analog glitch filter on the external interrupt pad input.
0b - Disable
1b - Enable
48.5.1.10
Wake-Up and Interrupt Status Flag (WISR_64)
Offset
Register
Offset
WISR_64
54h
Function
Holds the wake-up and interrupt flags.
 
• This register is accessible only by 32-bit read/write operations.
• Status fields associated with on-chip wake-up sources are located to the left of the external wake-up/interrupt 
status fields and are read-only. The wake-up for these sources must be configured and cleared at the 
on-chip wake-up source. Also, the configuration registers for the external interrupts/wake-ups do not have 
corresponding fields.
  NOTE  
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1911 / 5251


---
# 페이지 254

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
EIF_1 
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
EIF_1 
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
31-0
EIF_1
External Wake-Up and Interrupt Status Flag
Specifies whether an event, as defined by WIREER and WIFEER, has occurred on the pad. If enabled 
(IRER[n]), EIF[n] causes an interrupt request.
0b - No event occurred
1b - An event occurred
48.5.1.11
Interrupt Request Enable (IRER_64)
Offset
Register
Offset
IRER_64
58h
Function
Enables interrupt messaging from the wake-up and interrupt pads to the interrupt controller.
 
This register is accessible only by 32-bit read/write operations.
  NOTE  
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1912 / 5251


---
# 페이지 255

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
EIRE_1 
W
Reset
0
0
0
0
0
0
0
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
EIRE_1 
W
Reset
0
0
0
0
0
0
0
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
EIRE_1
External Interrupt Request Enable
Enables interrupt requests from the corresponding field, EIF[n].
0b - Disable
1b - Enable (with EIF[n] set)
48.5.1.12
Wake-Up Request Enable (WRER_64)
Offset
Register
Offset
WRER_64
5Ch
Function
Enables system wake-up messaging from the wake-up and interrupt pads to the mode entry and power control modules.
 
This register is accessible only by 32-bit read/write operations.
If a pin is disabled through this register, you must write 0 to the corresponding fields in WIFEER and WIREER to 
ensure that the pin does not respond to any change.
  NOTE  
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1913 / 5251


---
# 페이지 256

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
WRE_1 
W
Reset
0
0
0
0
0
0
0
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
WRE_1 
W
Reset
0
0
0
0
0
0
0
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
WRE_1
External Wake-Up Request Enable
Enables system wake-up requests from the corresponding field, EIF[n].
0b - Disable
1b - Enable (with EIF[n] set)
48.5.1.13
Wake-Up and Interrupt Rising-Edge Event Enable (WIREER_64)
Offset
Register
Offset
WIREER_64
68h
Function
Enables rising-edge triggered events on the corresponding wake-up and interrupt pads.
 
• This register is accessible only by 32-bit read/write operations.
• WIREER or WIFEER is configured for rising or falling-edge after WRER to enable wake-up source.
  NOTE  
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1914 / 5251


---
# 페이지 257

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
IREE_1 
W
Reset
0
0
0
0
0
0
0
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
IREE_1 
W
Reset
0
0
0
0
0
0
0
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
IREE_1
External Interrupt Rising-edge Events Enable
Enables an external interrupt rising-edge event.
0b - Disable
1b - Enable
48.5.1.14
Wake-Up and Interrupt Falling-Edge Event Enable (WIFEER_64)
Offset
Register
Offset
WIFEER_64
6Ch
Function
Enables falling-edge triggered events on the corresponding wake-up and interrupt pads.
 
• This register is accessible only by 32-bit read/write operations.
• WIREER or WIFEER is configured for rising or falling-edge after WRER to enable a wake-up source.
  NOTE  
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1915 / 5251


---
# 페이지 258

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
IFEEx_1 
W
Reset
0
0
0
0
0
0
0
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
IFEEx_1 
W
Reset
0
0
0
0
0
0
0
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
IFEEx_1
External Interrupt Falling-Edge Events Enable
Enables an external interrupt falling-edge event.
0b - Disable
1b - Enable
48.5.1.15
Wake-Up and Interrupt Filter Enable (WIFER_64)
Offset
Register
Offset
WIFER_64
70h
Function
Enables an analog filter on the corresponding interrupt pads to filter out glitches on the inputs.
 
This register is accessible only by 32-bit read/write operations.
  NOTE  
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1916 / 5251


---
# 페이지 259

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
IFE_1 
W
Reset
0
0
0
0
0
0
0
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
IFE_1 
W
Reset
0
0
0
0
0
0
0
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
IFE_1
External Interrupt Filter Enable
Enables an analog glitch filter on the external interrupt pad input.
0b - Disable
1b - Enable
48.6 Glossary
NMI
Nonmaskable interrupts
NXP Semiconductors
Wakeup Unit (WKPU)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1917 / 5251


---
