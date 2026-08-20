# 페이지 162

Chapter 51
Error Reporting Module (ERM)
51.1 Chip-specific ERM information
51.1.1 ERM instances
This chip supports up to two instances of ERM:
• ERM_0
• ERM_1
Table 291. ERM instances
Instances
S32K358/S32K348/
S32K338/S32K328/
S32K388/S32K389
S32K322/S32K324/S32K344/S32K342/S32K341/S32K312/S32K311/
S32K310/S32K314
ERM_0
Yes
Yes
ERM_1
Yes
No
51.1.2 ERM channel mapping
ERM provides information on memory events associated with ECC and parity. It also provides you an option to enable interrupt 
notification for these events.
Table 292. ERM_0 channel mapping for all chips except S32K389
Channel #
Module
Captured status
00
SRAM0
Single-bit error, multi-bit error, syndrome, absolute error address 
aligned to double-word (64-bit) boundary
01
SRAM1 1
Single-bit error, multi-bit error, syndrome, absolute error 
address+18000h aligned to double-word (64-bit) boundary2
02
Cortex-M7_0 I-cache tag RAM
Single-bit error, multi-bit error3
03
Cortex-M7_0 I-cache data RAM
Single-bit error, multi-bit error3
04
Cortex-M7_0 D-cache tag RAM
Single-bit error, multi-bit error3
05
Cortex-M7_0 D-cache data RAM
Single-bit error, multi-bit error3
06
Cortex-M7_1 I-cache tag RAM 4
Single-bit error, multi-bit error3
07
Cortex-M7_1 I-cache data RAM
Single-bit error, multi-bit error3
08
Cortex-M7_1 D-cache tag RAM
Single-bit error, multi-bit error3
09
Cortex-M7_1 D-cache data RAM
Single-bit error, multi-bit error3
10
Cortex-M7_0 ITCM
Single-bit error, multi-bit error, syndrome, offset error address
11
Cortex-M7_0 D0TCM
Single-bit error, multi-bit error, syndrome, offset error address
12
Cortex-M7_0 D1TCM
Single-bit error, multi-bit error, syndrome, offset error address5
13
Cortex-M7_1 ITCM
Single-bit error, multi-bit error, syndrome, offset error address
Table continues on the next page...
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2079 / 5251


---
# 페이지 163

Table 292. ERM_0 channel mapping for all chips except S32K389 (continued)
Channel #
Module
Captured status
14
Cortex-M7_1 D0TCM
Single-bit error, multi-bit error, syndrome, offset error address
15
Cortex-M7_1 D1TCM
Single-bit error, multi-bit error, syndrome, offset error address5
16
DMA TCD
Single-bit error, multi-bit error, syndrome, offset error address6
17
Flash memory port p0
Single-bit error, multi-bit error, absolute error address
18
Flash memory port p1
Single-bit error, multi-bit error, absolute error address
19
Flash memory port p2 7
Single-bit error, multi-bit error, absolute error address
1. SRAM1 is not available for the S32K342, S32K341, S32K322, S32K312, and S32K311 product variants.
2. For variants: S32K314, S32K324, and S32K344 size of SRAM0 is 160 KB, and therefore, to align addresses to the next 
power of 2, an address space of 256 KB is reserved for error reporting. However, SRAM0 and SRAM1 are in contiguous 
locations in the memory map. So, you must subtract 18000h (256 KB-160 KB = 96 KB that corresponds to 18000h) from the 
reported address to get an absolute address. See the "Memory and Memory Interfaces" chapter for SRAM details on different 
S32K3xx variants.
3. The cache controller does not report error addresses and syndrome.
4. Cortex-M7_1 and its associated RAM and caches are not available in the S32K312 and S32K311 product variants.
5. For address reporting, bit 2 of the address is masked because this bit decides whether the access (read or write) is for D0TCM 
or D1TCM. For example, if the offset address is 0h or 8h, it is routed to D0TCM, but if the offset address is 4h or Ch, it is routed 
to D1TCM. The errors that are latched for these offset addresses are as follows:
• Offset 0h : Address 0h is latched into the ERM channel corresponding to D0TCM.
• Offset 4h : Address 0h is latched into the ERM channel corresponding to D1TCM.
• Offset 8h : Address 8h is latched into the ERM channel corresponding to D0TCM.
• Offset Ch : Address 8h is latched into the ERM channel corresponding to D1TCM.
6. Bits [31:10] and [2:0] are always 0 because they are not connected.
Bits [9:5] indicate the corresponding TCD out of all the 32 implemented TCDs.
Bits [4:3] indicate an offset of TCDs with respect to a 64-bit aligned boundary.
• If [4:3] is 00, it indicates that an error is on offset address 20h.
• If [4:3] is 01, it indicates that an error is on offset address 28h.
• If [4:3] is 10, it indicates that an error is on offset address 30h.
• If [4:3] is 11, it indicates that an error is on offset address 38h.
7. Flash memory port p2 is not applicable for the S32K312 and S32K311 product variants.
Table 293. ERM_0 channel mapping for S32K389
Channel #
Module
Captured status
00
SRAM0
Single-bit error, multi-bit error, syndrome, absolute error address 
aligned to double-word (64-bit) boundary
01
SRAM1
Single-bit error, multi-bit error, syndrome, absolute error 
address+18000h aligned to double-word (64-bit) boundary
02
Cortex-M7_0 I-cache tag RAM
Single-bit error, multi-bit error1
03
Cortex-M7_0 I-cache data RAM
Single-bit error, multi-bit error1
04
Cortex-M7_0 D-cache tag RAM
Single-bit error, multi-bit error1
05
Cortex-M7_0 D-cache data RAM
Single-bit error, multi-bit error1
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2080 / 5251


---
# 페이지 164

Table 293. ERM_0 channel mapping for S32K389 (continued)
Channel #
Module
Captured status
06
Cortex-M7_1 I-cache tag RAM
Single-bit error, multi-bit error1
07
Cortex-M7_1 I-cache data RAM
Single-bit error, multi-bit error3
08
Cortex-M7_1 D-cache tag RAM
Single-bit error, multi-bit error3
09
Cortex-M7_1 D-cache data RAM
Single-bit error, multi-bit error3
10
Cortex-M7_0 ITCM
Single-bit error, multi-bit error, syndrome, offset error address
11
Cortex-M7_0 D0TCM
Single-bit error, multi-bit error, syndrome, offset error address
12
Cortex-M7_0 D1TCM
Single-bit error, multi-bit error, syndrome, offset error address2
13
Cortex-M7_1 ITCM
Single-bit error, multi-bit error, syndrome, offset error address
14
Cortex-M7_1 D0TCM
Single-bit error, multi-bit error, syndrome, offset error address
15
Cortex-M7_1 D1TCM
Single-bit error, multi-bit error, syndrome, offset error address2
16
DMA TCD
Single-bit error, multi-bit error, syndrome, offset error address3
17
Flash memory controller PFC0 port 0 Single-bit error, multi-bit error, absolute error address
18
Flash memory controller PFC0 port 1 Single-bit error, multi-bit error, absolute error address
19
Flash memory controller PFC1 port 0 Single-bit error, multi-bit error, absolute error address
20
Flash memory controller PFC1 port 1 Single-bit error, multi-bit error, absolute error address
21
SRAM3
Single-bit error, multi-bit error, syndrome, absolute error 
address+18000h aligned to double-word (64-bit) boundary
1. The cache controller does not report error addresses and syndrome.
2. For address reporting, bit 2 of the address is masked because this bit decides whether the access (read or write) is for D0TCM 
or D1TCM. For example, if the offset address is 0h or 8h, it is routed to D0TCM, but if the offset address is 4h or Ch, it is routed 
to D1TCM. The errors that are latched for these offset addresses are as follows:
• Offset 0h : Address 0h is latched into the ERM channel corresponding to D0TCM.
• Offset 4h : Address 0h is latched into the ERM channel corresponding to D1TCM.
• Offset 8h : Address 8h is latched into the ERM channel corresponding to D0TCM.
• Offset Ch : Address 8h is latched into the ERM channel corresponding to D1TCM.
3. Bits [31:10] and [2:0] are always 0 because they are not connected.
Bits [9:5] indicate the corresponding TCD out of all the 32 implemented TCDs.
Bits [4:3] indicate an offset of TCDs with respect to a 64-bit aligned boundary.
• If [4:3] is 00, it indicates that an error is on offset address 20h.
• If [4:3] is 01, it indicates that an error is on offset address 28h.
• If [4:3] is 10, it indicates that an error is on offset address 30h.
• If [4:3] is 11, it indicates that an error is on offset address 38h.
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2081 / 5251


---
# 페이지 165

Table 294. ERM_1 channel mapping (S32K389)
Channel #
Module
Captured status
0
SRAM2
Single-bit error, multi-bit error, syndrome, absolute error 
address aligned to double, word (64-bit) boundary
1
-
-
2
CM7_2 I-cache tag RAM
Single-bit error, multi-bit error
3
CM7_2 I-cache data RAM
Single-bit error, multi-bit error
4
CM7_2 D-cache tag RAM
Single-bit error, multi-bit error
5
CM7_2 D-cache data RAM
Single-bit error, multi-bit error
6
CM7_3 I-cache tag RAM1
Single-bit error, multi-bit error
7
CM7_3 I-cache data RAM1
Single-bit error, multi-bit error
8
CM7_3 D-cache tag RAM1
Single-bit error, multi-bit error
9
CM7_3 D-cache data RAM1
Single-bit error, multi-bit error
10
CM7_2 ITCM
Single-bit error, multi-bit error, syndrome, offset error address
11
CM7_2 D0TCM
Single-bit error, multi-bit error, syndrome, offset error address
12
CM7_2 D1TCM
Single-bit error, multi-bit error, syndrome, offset error address
13
CM7_3 ITCM
Single-bit error, multi-bit error, syndrome, offset error address
14
CM7_3 D0TCM
Single-bit error, multi-bit error, syndrome, offset error address
15
CM7_3 D1TCM
Single-bit error, multi-bit error, syndrome, offset error address
16
-
-
172
Flash memory port p3
Single-bit error, multi-bit error, syndrome, offset error address
18
ACE_ACCEL eDMA TCD 32-channel
Single-bit error, multi-bit error, syndrome, offset error address
19
ACE_ACCEL eDMA TCD 24-channel
Single-bit error, multi-bit error, syndrome, offset error address 
20
-
-
21
-
-
22
-
-
23
-
-
1. CM7_3 ports are reserved for all chips except S32K388/S32K389.
2. Not applicable for S32K389.
 
For S32K388/S32K389, channel 1 and channel 16 of ERM_1 are Reserved. Read and write to registers related to 
these channels will not give any transfer error.
  NOTE  
 
For S32K358/S32K348/S32K338/S32K328, you have to enable both the ERM instances even if you are only using 
one otherwise software might hang during interrupt subroutine.
  NOTE  
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2082 / 5251


---
# 페이지 166

51.1.3 ECC error address remapping (S32K389)
The software driver for the ERM module converts the reported error addresses (physical) to the system logic addresses, as per 
the table below:
Table 295. ECC error address remapping (S32K389)
PFC0 (ERM Channel #17, #18)
Physical Address (reported to ERM)
System Logical Address (to be converted to)
0x004x_xxxx
0x006x_xxxx
0x005x_xxxx
0x007x_xxxx
0x006x_xxxx
0x008x_xxxx
0x007x_xxxx
0x009x_xxxx
0x008x_xxxx
0x00Cx_xxxx
0x009x_xxxx
0x00Dx_xxxx
0x00Ax_xxxx
0x00Ex_xxxx
0x00Bx_xxxx
0x00Fx_xxxx
PFC1 (ERM Channel #19, #20)
Physical Address (reported to ERM)
System Logical Address (to be converted to)
0x004x_xxxx
0x004x_xxxx
0x005x_xxxx
0x005x_xxxx
0x006x_xxxx
0x00Ax_xxxx
0x007x_xxxx
0x00Bx_xxxx
51.2 Overview
The Error Reporting Module (ERM) provides information and optional interrupt notification on memory error events associated 
with ECC and parity. The ERM collects error events on memory accesses for memory arrays, such as flash memory, system 
RAM, or peripheral RAMs. ERM supports various channels for memory sources where each ERM channel is associated with 
a different memory module. See the chip-specific ERM information for details about supported memory sources and specific 
memory channel assignments. If memory supports ECC then ERM syndrome and error address information is captured along with 
error event. ERM does not receive this information in case of cache or memory with parity along with error event.
51.2.1 Features
The ERM includes these features:
• Optional interrupt notification on captured error events
• Capturing of address and syndrome information on single-bit correction and non-correctable ECC events
• Support for error event capturing for memory sources, with individual reporting fields and interrupt configuration per 
memory channel
• Recording the count value of the number of corrected error events
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2083 / 5251


---
# 페이지 167

51.2.2 Block diagram
Memory error (single-, multi-bit)
and attributes (error address, syndrome)
Register interface
Memory error
channel 0
Memory error (single- or multi-bit)
and attributes (error address, syndrome)
Memory error
channel 23
IPI single error interrupt
IPI multi error interrupt
Figure 208. Block diagram
51.3 Functional description
51.3.1 Single-bit correction events
When a single-bit correction event on Memory n is detected, the ERM:
• Records the event by changing the value of the applicable Status Register bit SRx[SBCn] to 1.
• Increments the correctable error count value (until the counter reaches its maximum value): CORR_ERR_CNTn[COUNT].
• Records the corresponding access address that initiated the event in the Memory n Error Address Register: EARn (if this 
register is present for the channel).
• Stores the corresponding ECC syndrome in the Memory n Error Syndrome Register: SYNn (if this register is present for the 
channel). This register identifies the bit position of the corrected data on single-bit data inversion.
The ERM holds event information only for the last reported event.
To clear the record of an event, write 1 to SRx[SBCn] to change its value to 0.
To reset the correctable error count value, write all zeros to CORR_ERR_CNTn[COUNT].
Optional interrupt notification for single-bit correction events
The ERM provides an option to generate an interrupt notification upon the report of a single-bit correction event. To enable 
single-bit correction interrupts for a channel:
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2084 / 5251


---
# 페이지 168

1. To enable interrupt notification for single-bit correction events on Memory n, set CRx[ESCIEn] to 1.
2. Subsequently, a single-bit correction event on Memory n is detected, the ERM:
• Records the event and address, and stores the ECC syndrome as usual.
• Additionally sends an interrupt notification corresponding to the event.
3. To clear both the record of an event and the corresponding interrupt notification, write 1 to SRx[SBCn] to change its value 
to 0.
51.3.2 Non-correctable error events
When a non-correctable ECC error event on Memory n is detected, the ERM:
• Records the event by changing the value of the applicable Status Register bit: SRx[NCEn] to 1.
• Records the corresponding access address that initiated the event in the Memory n Error Address Register: EARn (if this 
register is present for the channel).
• Stores the corresponding ECC syndrome in the Memory n Error Syndrome Register: SYNn (if this register is present for 
the channel).
— In the event of a non-correctable address bit inversion, SYNn identifies the pertinent address bit position.
— In the event of a non-correctable, multi-bit data inversion, the syndrome value does not provide any additional 
diagnostic information.
The ERM holds event information only for the last reported event.
To clear the record of an event, write 1 to SRx[NCEn] to change its value to 0.
Optional interrupt notification for non-correctable error events
The ERM provides an option to generate an interrupt notification upon the report of a non-correctable ECC event. To enable 
non-correctable error interrupts for a channel:
1. To enable interrupt notifications for non-correctable error events on Memory n, set CRx[ENCIEn] to 1.
2. Subsequently, when a non-correctable error event on Memory n is detected, the ERM:
• Records the event and address and stores the ECC syndrome as usual.
• Additionally sends an interrupt notification corresponding to the event.
3. To clear both the record of an event and the corresponding interrupt notification, write 1 to SRx[NCEn] to change its value 
to 0.
 
Parity errors can be mapped to non-correctable errors where error attributes like SYNDROME, ADDRESS are 
not provided.
  NOTE  
51.4 Initialization
For each ERM channel supporting memory with ECC, prepare the corresponding memory array before enabling ERM interrupts 
about errors for that memory.
1. Initialize the memory to a known value so that the correct corresponding ECC codeword is stored.
2. During the memory's initialization, if the ERM captures information about any ECC error event, clear the corresponding 
SRx[SBCn] or SRx[NCEn] field that stores the record of the event.
3. Program the applicable CRx[ESCIEn] and CRx[ENCIEn] fields to enable ERM interrupts as desired.
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2085 / 5251


---
# 페이지 169

51.5 ERM_0 register descriptions
You can access the programming model:
• Only in supervisor mode
• Using only 32-bit (word) accesses
Any of the following attempted references to the programming model generates an error termination:
• In user mode
• Using non-32-bit access sizes
Based on the design implementation, the following XFR error behavior is evident at the IPS interface.
• Within the ERM memory map, an XFR error is evident at reserved addresses from location 20h to FFh.
• No XFR error is evident at reserved addresses in memory spaces allocated to each channel. For example: For channel 0, for 
read/write accesses to reserved address 10Ch, the XFR error is 0.
• For accesses to locations beyond the addresses allocated for the final channel, the XFR error is 1.
 
• See the chip-specific ERM information at the beginning of this chapter for details on Memory channel mapping.
• To access the channel registers, corresponding memory channel clock must be enabled.
  NOTE  
51.5.1 ERM_0 memory map
ERM_0 base address: 4025_C000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
ERM Configuration Register 0 (CR0)
32
RW
0000_0000h
4h
ERM Configuration Register 1 (CR1)
32
RW
0000_0000h
8h
ERM Configuration Register 2 (CR2)
32
RW
0000_0000h
10h
ERM Status Register 0 (SR0)
32
RW
0000_0000h
14h
ERM Status Register 1 (SR1)
32
RW
0000_0000h
18h
ERM Status Register 2 (SR2)
32
RW
0000_0000h
100h
ERM Memory 0 Error Address Register (EAR0)
32
R
0000_0000h
104h
ERM Memory 0 Syndrome Register (SYN0)
32
R
0000_0000h
108h
ERM Memory 0 Correctable Error Count Register 
(CORR_ERR_CNT0)
32
RW
0000_0000h
110h
ERM Memory 1 Error Address Register (EAR1)
32
R
0000_0000h
114h
ERM Memory 1 Syndrome Register (SYN1)
32
R
0000_0000h
118h
ERM Memory 1 Correctable Error Count Register 
(CORR_ERR_CNT1)
32
RW
0000_0000h
128h
ERM Memory 2 Correctable Error Count Register 
(CORR_ERR_CNT2)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2086 / 5251


---
# 페이지 170

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
138h
ERM Memory 3 Correctable Error Count Register 
(CORR_ERR_CNT3)
32
RW
0000_0000h
148h
ERM Memory 4 Correctable Error Count Register 
(CORR_ERR_CNT4)
32
RW
0000_0000h
158h
ERM Memory 5 Correctable Error Count Register 
(CORR_ERR_CNT5)
32
RW
0000_0000h
168h
ERM Memory 6 Correctable Error Count Register 
(CORR_ERR_CNT6)
32
RW
0000_0000h
178h
ERM Memory 7 Correctable Error Count Register 
(CORR_ERR_CNT7)
32
RW
0000_0000h
188h
ERM Memory 8 Correctable Error Count Register 
(CORR_ERR_CNT8)
32
RW
0000_0000h
198h
ERM Memory 9 Correctable Error Count Register 
(CORR_ERR_CNT9)
32
RW
0000_0000h
1A0h
ERM Memory 10 Error Address Register (EAR10)
32
R
0000_0000h
1A4h
ERM Memory 10 Syndrome Register (SYN10)
32
R
0000_0000h
1A8h
ERM Memory 10 Correctable Error Count Register 
(CORR_ERR_CNT10)
32
RW
0000_0000h
1B0h
ERM Memory 11 Error Address Register (EAR11)
32
R
0000_0000h
1B4h
ERM Memory 11 Syndrome Register (SYN11)
32
R
0000_0000h
1B8h
ERM Memory 11 Correctable Error Count Register 
(CORR_ERR_CNT11)
32
RW
0000_0000h
1C0h
ERM Memory 12 Error Address Register (EAR12)
32
R
0000_0000h
1C4h
ERM Memory 12 Syndrome Register (SYN12)
32
R
0000_0000h
1C8h
ERM Memory 12 Correctable Error Count Register 
(CORR_ERR_CNT12)
32
RW
0000_0000h
1D0h
ERM Memory 13 Error Address Register (EAR13)
32
R
0000_0000h
1D4h
ERM Memory 13 Syndrome Register (SYN13)
32
R
0000_0000h
1D8h
ERM Memory 13 Correctable Error Count Register 
(CORR_ERR_CNT13)
32
RW
0000_0000h
1E0h
ERM Memory 14 Error Address Register (EAR14)
32
R
0000_0000h
1E4h
ERM Memory 14 Syndrome Register (SYN14)
32
R
0000_0000h
1E8h
ERM Memory 14 Correctable Error Count Register 
(CORR_ERR_CNT14)
32
RW
0000_0000h
1F0h
ERM Memory 15 Error Address Register (EAR15)
32
R
0000_0000h
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2087 / 5251


---
# 페이지 171

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1F4h
ERM Memory 15 Syndrome Register (SYN15)
32
R
0000_0000h
1F8h
ERM Memory 15 Correctable Error Count Register 
(CORR_ERR_CNT15)
32
RW
0000_0000h
200h
ERM Memory 16 Error Address Register (EAR16)
32
R
0000_0000h
204h
ERM Memory 16 Syndrome Register (SYN16)
32
R
0000_0000h
208h
ERM Memory 16 Correctable Error Count Register 
(CORR_ERR_CNT16)
32
RW
0000_0000h
210h
ERM Memory 17 Error Address Register (EAR17)
32
R
0000_0000h
218h
ERM Memory 17 Correctable Error Count Register 
(CORR_ERR_CNT17)
32
RW
0000_0000h
220h
ERM Memory 18 Error Address Register (EAR18)
32
R
0000_0000h
228h
ERM Memory 18 Correctable Error Count Register 
(CORR_ERR_CNT18)
32
RW
0000_0000h
230h
ERM Memory 19 Error Address Register (EAR19)
32
R
0000_0000h
238h
ERM Memory 19 Correctable Error Count Register 
(CORR_ERR_CNT19)
32
RW
0000_0000h
240h
ERM Memory 20 Error Address Register (EAR20)
32
R
0000_0000h
248h
ERM Memory 20 Correctable Error Count Register 
(CORR_ERR_CNT20)
32
RW
0000_0000h
250h
ERM Memory 21 Error Address Register (EAR21)
32
R
0000_0000h
254h
ERM Memory 21 Syndrome Register (SYN21)
32
R
0000_0000h
258h
ERM Memory 21 Correctable Error Count Register 
(CORR_ERR_CNT21)
32
RW
0000_0000h
51.5.2 ERM Configuration Register 0 (CR0)
Offset
Register
Offset
CR0
0h
Function
This 32-bit control register configures the interrupt notification capability for available channels.
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2088 / 5251


---
# 페이지 172

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
ESCIE
0 
ENCIE
0 
0
ESCIE
1 
ENCIE
1 
0
ESCIE
2 
ENCIE
2 
0
ESCIE
3 
ENCIE
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
ESCIE
4 
ENCIE
4 
0
ESCIE
5 
ENCIE
5 
0
ESCIE
6 
ENCIE
6 
0
ESCIE
7 
ENCIE
7 
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
ESCIE0
ESCIE0
Enable Memory 0 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 0 single-bit correction events is disabled.
1b - Interrupt notification of Memory 0 single-bit correction events is enabled.
30
ENCIE0
ENCIE0
Enable Memory 0 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 0 non-correctable error events is disabled.
1b - Interrupt notification of Memory 0 non-correctable error events is enabled.
29-28
—
Reserved
27
ESCIE1
ESCIE1
Enable Memory 1 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 1 single-bit correction events is disabled.
1b - Interrupt notification of Memory 1 single-bit correction events is enabled.
26
ENCIE1
ENCIE1
Enable Memory 1 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 1 non-correctable error events is disabled.
1b - Interrupt notification of Memory 1 non-correctable error events is enabled.
25-24
—
Reserved
23
ESCIE2
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2089 / 5251


---
# 페이지 173

Table continued from the previous page...
Field
Function
ESCIE2
Enable Memory 2 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 2 single-bit correction events is disabled.
1b - Interrupt notification of Memory 2 single-bit correction events is enabled.
22
ENCIE2
ENCIE2
Enable Memory 2 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 2 non-correctable error events is disabled.
1b - Interrupt notification of Memory 2 non-correctable error events is enabled.
21-20
—
Reserved
19
ESCIE3
ESCIE3
Enable Memory 3 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 3 single-bit correction events is disabled.
1b - Interrupt notification of Memory 3 single-bit correction events is enabled.
18
ENCIE3
ENCIE3
Enable Memory 3 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 3 non-correctable error events is disabled.
1b - Interrupt notification of Memory 3 non-correctable error events is enabled.
17-16
—
Reserved
15
ESCIE4
ESCIE4
Enable Memory 4 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 4 single-bit correction events is disabled.
1b - Interrupt notification of Memory 4 single-bit correction events is enabled.
14
ENCIE4
ENCIE4
Enable Memory 4 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 4 non-correctable error events is disabled.
1b - Interrupt notification of Memory 4 non-correctable error events is enabled.
13-12
—
Reserved
11
ESCIE5
Enable Memory 5 Single Correction Interrupt Notification
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2090 / 5251


---
# 페이지 174

Table continued from the previous page...
Field
Function
ESCIE5
0b - Interrupt notification of Memory 5 single-bit correction events is disabled.
1b - Interrupt notification of Memory 5 single-bit correction events is enabled.
10
ENCIE5
ENCIE5
Enable Memory 5 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 5 non-correctable error events is disabled.
1b - Interrupt notification of Memory 5 non-correctable error events is enabled.
9-8
—
Reserved
7
ESCIE6
ESCIE6
Enable Memory 6 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 6 single-bit correction events is disabled.
1b - Interrupt notification of Memory 6 single-bit correction events is enabled.
6
ENCIE6
ENCIE6
Enable Memory 6 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 6 non-correctable error events is disabled.
1b - Interrupt notification of Memory 6 non-correctable error events is enabled.
5-4
—
Reserved
3
ESCIE7
ESCIE7
Enable Memory 7 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 7 single-bit correction events is disabled.
1b - Interrupt notification of Memory 7 single-bit correction events is enabled.
2
ENCIE7
ENCIE7
Enable Memory 7 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 7 non-correctable error events is disabled.
1b - Interrupt notification of Memory 7 non-correctable error events is enabled.
1-0
—
Reserved
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2091 / 5251


---
# 페이지 175

51.5.3 ERM Configuration Register 1 (CR1)
Offset
Register
Offset
CR1
4h
Function
This 32-bit control register configures the interrupt notification capability for available channels.
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
ESCIE
8 
ENCIE
8 
0
ESCIE
9 
ENCIE
9 
0
ESCIE
10 
ENCIE
10 
0
ESCIE
11 
ENCIE
11 
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
ESCIE
12 
ENCIE
12 
0
ESCIE
13 
ENCIE
13 
0
ESCIE
14 
ENCIE
14 
0
ESCIE
15 
ENCIE
15 
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
ESCIE8
ESCIE8
Enable Memory 8 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 8 single-bit correction events is disabled.
1b - Interrupt notification of Memory 8 single-bit correction events is enabled.
30
ENCIE8
ENCIE8
Enable Memory 8 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 8 non-correctable error events is disabled.
1b - Interrupt notification of Memory 8 non-correctable error events is enabled.
29-28
—
Reserved
27
ESCIE9
ESCIE9
Enable Memory 9 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 9 single-bit correction events is disabled.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2092 / 5251


---
# 페이지 176

Table continued from the previous page...
Field
Function
1b - Interrupt notification of Memory 9 single-bit correction events is enabled.
26
ENCIE9
ENCIE9
Enable Memory 9 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 9 non-correctable error events is disabled.
1b - Interrupt notification of Memory 9 non-correctable error events is enabled.
25-24
—
Reserved
23
ESCIE10
ESCIE10
Enable Memory 10 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 10 single-bit correction events is disabled.
1b - Interrupt notification of Memory 10 single-bit correction events is enabled.
22
ENCIE10
ENCIE10
Enable Memory 10 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 10 non-correctable error events is disabled.
1b - Interrupt notification of Memory 10 non-correctable error events is enabled.
21-20
—
Reserved
19
ESCIE11
ESCIE11
Enable Memory 11 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 11 single-bit correction events is disabled.
1b - Interrupt notification of Memory 11 single-bit correction events is enabled.
18
ENCIE11
ENCIE11
Enable Memory 11 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 11 non-correctable error events is disabled.
1b - Interrupt notification of Memory 11 non-correctable error events is enabled.
17-16
—
Reserved
15
ESCIE12
ESCIE12
Enable Memory 12 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 12 single-bit correction events is disabled.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2093 / 5251


---
# 페이지 177

Table continued from the previous page...
Field
Function
1b - Interrupt notification of Memory 12 single-bit correction events is enabled.
14
ENCIE12
ENCIE12
Enable Memory 12 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 12 non-correctable error events is disabled.
1b - Interrupt notification of Memory 12 non-correctable error events is enabled.
13-12
—
Reserved
11
ESCIE13
ESCIE13
Enable Memory 13 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 13 single-bit correction events is disabled.
1b - Interrupt notification of Memory 13 single-bit correction events is enabled.
10
ENCIE13
ENCIE13
Enable Memory 13 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 13 non-correctable error events is disabled.
1b - Interrupt notification of Memory 13 non-correctable error events is enabled.
9-8
—
Reserved
7
ESCIE14
ESCIE14
Enable Memory 14 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 14 single-bit correction events is disabled.
1b - Interrupt notification of Memory 14 single-bit correction events is enabled.
6
ENCIE14
ENCIE14
Enable Memory 14 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 14 non-correctable error events is disabled.
1b - Interrupt notification of Memory 14 non-correctable error events is enabled.
5-4
—
Reserved
3
ESCIE15
ESCIE15
Enable Memory 15 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 15 single-bit correction events is disabled.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2094 / 5251


---
# 페이지 178

Table continued from the previous page...
Field
Function
1b - Interrupt notification of Memory 15 single-bit correction events is enabled.
2
ENCIE15
ENCIE15
Enable Memory 15 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 15 non-correctable error events is disabled.
1b - Interrupt notification of Memory 15 non-correctable error events is enabled.
1-0
—
Reserved
51.5.4 ERM Configuration Register 2 (CR2)
Offset
Register
Offset
CR2
8h
Function
This 32-bit control register configures the interrupt notification capability for available channels.
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
ESCIE
16 
ENCIE
16 
0
ESCIE
17 
ENCIE
17 
0
ESCIE
18 
ENCIE
18 
0
ESCIE
19 
ENCIE
19 
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
ESCIE
20 
ENCIE
20 
0
ESCIE
21 
ENCIE
21 
0
Reserved 
0
Reserved 
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
ESCIE16
ESCIE16
Enable Memory 16 Single Correction Interrupt Notification
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2095 / 5251


---
# 페이지 179

Table continued from the previous page...
Field
Function
0b - Interrupt notification of Memory 16 single-bit correction events is disabled.
1b - Interrupt notification of Memory 16 single-bit correction events is enabled.
30
ENCIE16
ENCIE16
Enable Memory 16 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 16 non-correctable error events is disabled.
1b - Interrupt notification of Memory 16 non-correctable error events is enabled.
29-28
—
Reserved
27
ESCIE17
ESCIE17
Enable Memory 17 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 17 single-bit correction events is disabled.
1b - Interrupt notification of Memory 17 single-bit correction events is enabled.
26
ENCIE17
ENCIE17
Enable Memory 17 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 17 non-correctable error events is disabled.
1b - Interrupt notification of Memory 17 non-correctable error events is enabled.
25-24
—
Reserved
23
ESCIE18
ESCIE18
Enable Memory 18 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 18 single-bit correction events is disabled.
1b - Interrupt notification of Memory 18 single-bit correction events is enabled.
22
ENCIE18
ENCIE18
Enable Memory 18 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 18 non-correctable error events is disabled.
1b - Interrupt notification of Memory 18 non-correctable error events is enabled.
21-20
—
Reserved
19
ESCIE19
ESCIE19
Enable Memory 19 Single Correction Interrupt Notification
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2096 / 5251


---
# 페이지 180

Table continued from the previous page...
Field
Function
0b - Interrupt notification of Memory 19 single-bit correction events is disabled.
1b - Interrupt notification of Memory 19 single-bit correction events is enabled.
18
ENCIE19
ENCIE19
Enable Memory 19 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 19 non-correctable error events is disabled.
1b - Interrupt notification of Memory 19 non-correctable error events is enabled.
17-16
—
Reserved
15
ESCIE20
ESCIE20
Enable Memory 20 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 20 single-bit correction events is disabled.
1b - Interrupt notification of Memory 20 single-bit correction events is enabled.
14
ENCIE20
ENCIE20
Enable Memory 20 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 20 non-correctable error events is disabled.
1b - Interrupt notification of Memory 20 non-correctable error events is enabled.
13-12
—
Reserved
11
ESCIE21
ESCIE21
Enable Memory 21 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 21 single-bit correction events is disabled.
1b - Interrupt notification of Memory 21 single-bit correction events is enabled.
10
ENCIE21
ENCIE21
Enable Memory 21 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 21 non-correctable error events is disabled.
1b - Interrupt notification of Memory 21 non-correctable error events is enabled.
9-8
—
Reserved
7-6
—
Reserved
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2097 / 5251


---
# 페이지 181

Table continued from the previous page...
Field
Function
5-4
—
Reserved
3-2
—
Reserved
1-0
—
Reserved
51.5.5 ERM Status Register 0 (SR0)
Offset
Register
Offset
SR0
10h
Function
This 32-bit status register reports error events for available channels.
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
SBC0 
NCE0 
0
SBC1 
NCE1 
0
SBC2 
NCE2 
0
SBC3 
NCE3 
0
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
SBC4 
NCE4 
0
SBC5 
NCE5 
0
SBC6 
NCE6 
0
SBC7 
NCE7 
0
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
31
SBC0
SBC0
Memory 0 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ESCIE0] 
is enabled.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2098 / 5251


---
# 페이지 182

Table continued from the previous page...
Field
Function
0b - No single-bit correction event on Memory 0 detected.
1b - Single-bit correction event on Memory 0 detected.
30
NCE0
NCE0
Memory 0 Non-Correctable Error Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ENCIE0] 
is enabled.
0b - No non-correctable error event on Memory 0 detected.
1b - Non-correctable error event on Memory 0 detected.
29-28
—
Reserved
27
SBC1
SBC1
Memory 1 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ESCIE1] 
is enabled.
0b - No single-bit correction event on Memory 1 detected.
1b - Single-bit correction event on Memory 1 detected.
26
NCE1
NCE1
Memory 1 Non-Correctable Error Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ENCIE1] 
is enabled.
0b - No non-correctable error event on Memory 1 detected.
1b - Non-correctable error event on Memory 1 detected.
25-24
—
Reserved
23
SBC2
SBC2
Memory 2 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ESCIE2] 
is enabled.
0b - No single-bit correction event on Memory 2 detected.
1b - Single-bit correction event on Memory 2 detected.
22
NCE2
NCE2
Memory 2 Non-Correctable Error Event
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2099 / 5251


---
# 페이지 183

Table continued from the previous page...
Field
Function
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ENCIE2] 
is enabled.
0b - No non-correctable error event on Memory 2 detected.
1b - Non-correctable error event on Memory 2 detected.
21-20
—
Reserved
19
SBC3
SBC3
Memory 3 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ESCIE3] 
is enabled.
0b - No single-bit correction event on Memory 3 detected.
1b - Single-bit correction event on Memory 3 detected.
18
NCE3
NCE3
Memory 3 Non-Correctable Error Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ENCIE3] 
is enabled.
0b - No non-correctable error event on Memory 3 detected.
1b - Non-correctable error event on Memory 3 detected.
17-16
—
Reserved
15
SBC4
SBC4
Memory 4 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ESCIE4] 
is enabled.
0b - No single-bit correction event on Memory 4 detected.
1b - Single-bit correction event on Memory 4 detected.
14
NCE4
NCE4
Memory 4 Non-Correctable Error Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ENCIE4] 
is enabled.
0b - No non-correctable error event on Memory 4 detected.
1b - Non-correctable error event on Memory 4 detected.
13-12
Reserved
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2100 / 5251


---
# 페이지 184

Table continued from the previous page...
Field
Function
—
11
SBC5
SBC5
Memory 5 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ESCIE5] 
is enabled.
0b - No single-bit correction event on Memory 5 detected.
1b - Single-bit correction event on Memory 5 detected.
10
NCE5
NCE5
Memory 5 Non-Correctable Error Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ENCIE5] 
is enabled.
0b - No non-correctable error event on Memory 5 detected.
1b - Non-correctable error event on Memory 5 detected.
9-8
—
Reserved
7
SBC6
SBC6
Memory 6 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ESCIE6] 
is enabled.
0b - No single-bit correction event on Memory 6 detected.
1b - Single-bit correction event on Memory 6 detected.
6
NCE6
NCE6
Memory 6 Non-Correctable Error Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ENCIE6] 
is enabled.
0b - No non-correctable error event on Memory 6 detected.
1b - Non-correctable error event on Memory 6 detected.
5-4
—
Reserved
3
SBC7
SBC7
Memory 7 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ESCIE7] 
is enabled.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2101 / 5251


---
# 페이지 185

Table continued from the previous page...
Field
Function
0b - No single-bit correction event on Memory 7 detected.
1b - Single-bit correction event on Memory 7 detected.
2
NCE7
NCE7
Memory 7 Non-Correctable Error Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ENCIE7] 
is enabled.
0b - No non-correctable error event on Memory 7 detected.
1b - Non-correctable error event on Memory 7 detected.
1-0
—
Reserved
51.5.6 ERM Status Register 1 (SR1)
Offset
Register
Offset
SR1
14h
Function
This 32-bit status register reports error events for available channels.
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
SBC8 
NCE8 
0
SBC9 
NCE9 
0
SBC10 NCE10 
0
SBC11 NCE11 
0
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
SBC12 NCE12 
0
SBC13 NCE13 
0
SBC14 NCE14 
0
SBC15 NCE15 
0
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
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2102 / 5251


---
# 페이지 186

Fields
Field
Function
31
SBC8
SBC8
Memory 8 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE8] 
is enabled.
0b - No single-bit correction event on Memory 8 detected.
1b - Single-bit correction event on Memory 8 detected.
30
NCE8
NCE8
Memory 8 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE8] 
is enabled.
0b - No non-correctable error event on Memory 8 detected.
1b - Non-correctable error event on Memory 8 detected.
29-28
—
Reserved
27
SBC9
SBC9
Memory 9 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE9] 
is enabled.
0b - No single-bit correction event on Memory 9 detected.
1b - Single-bit correction event on Memory 9 detected.
26
NCE9
NCE9
Memory 9 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE9] 
is enabled.
0b - No non-correctable error event on Memory 9 detected.
1b - Non-correctable error event on Memory 9 detected.
25-24
—
Reserved
23
SBC10
SBC10
Memory 10 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE10] 
is enabled.
0b - No single-bit correction event on Memory 10 detected.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2103 / 5251


---
# 페이지 187

Table continued from the previous page...
Field
Function
1b - Single-bit correction event on Memory 10 detected.
22
NCE10
NCE10
Memory 10 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE10] 
is enabled.
0b - No non-correctable error event on Memory 10 detected.
1b - Non-correctable error event on Memory 10 detected.
21-20
—
Reserved
19
SBC11
SBC11
Memory 11 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE11] 
is enabled.
0b - No single-bit correction event on Memory 11 detected.
1b - Single-bit correction event on Memory 11 detected.
18
NCE11
NCE11
Memory 11 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE11] 
is enabled.
0b - No non-correctable error event on Memory 11 detected.
1b - Non-correctable error event on Memory 11 detected.
17-16
—
Reserved
15
SBC12
SBC12
Memory 12 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE12] 
is enabled.
0b - No single-bit correction event on Memory 12 detected.
1b - Single-bit correction event on Memory 12 detected.
14
NCE12
NCE12
Memory 12 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE12] 
is enabled.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2104 / 5251


---
# 페이지 188

Table continued from the previous page...
Field
Function
0b - No non-correctable error event on Memory 12 detected.
1b - Non-correctable error event on Memory 12 detected.
13-12
—
Reserved
11
SBC13
SBC13
Memory 13 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE13] 
is enabled.
0b - No single-bit correction event on Memory 13 detected.
1b - Single-bit correction event on Memory 13 detected.
10
NCE13
NCE13
Memory 13 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE13] 
is enabled.
0b - No non-correctable error event on Memory 13 detected.
1b - Non-correctable error event on Memory 13 detected.
9-8
—
Reserved
7
SBC14
SBC14
Memory 14 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE14] 
is enabled.
0b - No single-bit correction event on Memory 14 detected.
1b - Single-bit correction event on Memory 14 detected.
6
NCE14
NCE14
Memory 14 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE14] 
is enabled.
0b - No non-correctable error event on Memory 14 detected.
1b - Non-correctable error event on Memory 14 detected.
5-4
—
Reserved
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2105 / 5251


---
# 페이지 189

Table continued from the previous page...
Field
Function
3
SBC15
SBC15
Memory 15 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE15] 
is enabled.
0b - No single-bit correction event on Memory 15 detected.
1b - Single-bit correction event on Memory 15 detected.
2
NCE15
NCE15
Memory 15 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE15] 
is enabled.
0b - No non-correctable error event on Memory 15 detected.
1b - Non-correctable error event on Memory 15 detected.
1-0
—
Reserved
51.5.7 ERM Status Register 2 (SR2)
Offset
Register
Offset
SR2
18h
Function
This 32-bit status register reports error events for available channels.
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
SBC16 NCE16 
0
SBC17 NCE17 
0
SBC18 NCE18 
0
SBC19 NCE19 
0
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
SBC20 NCE20 
0
SBC21 NCE21 
0
0
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
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2106 / 5251


---
# 페이지 190

Fields
Field
Function
31
SBC16
SBC16
Memory 16 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR2[ESCIE16] 
is enabled.
0b - No single-bit correction event on Memory 16 detected.
1b - Single-bit correction event on Memory 16 detected.
30
NCE16
NCE16
Memory 16 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ENCIE16] 
is enabled.
0b - No non-correctable error event on Memory 16 detected.
1b - Non-correctable error event on Memory 16 detected.
29-28
—
Reserved
27
SBC17
SBC17
Memory 17 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ESCIE17] 
is enabled.
0b - No single-bit correction event on Memory 17 detected.
1b - Single-bit correction event on Memory 17 detected.
26
NCE17
NCE17
Memory 17 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ENCIE17] 
is enabled.
0b - No non-correctable error event on Memory 17 detected.
1b - Non-correctable error event on Memory 17 detected.
25-24
—
Reserved
23
SBC18
SBC18
Memory 18 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ESCIE18] 
is enabled.
0b - No single-bit correction event on Memory 18 detected.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2107 / 5251


---
# 페이지 191

Table continued from the previous page...
Field
Function
1b - Single-bit correction event on Memory 18 detected.
22
NCE18
NCE18
Memory 18 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ENCIE18] 
is enabled.
0b - No non-correctable error event on Memory 18 detected.
1b - Non-correctable error event on Memory 18 detected.
21-20
—
Reserved
19
SBC19
SBC19
Memory 19 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ESCIE19] 
is enabled.
0b - No single-bit correction event on Memory 19 detected.
1b - Single-bit correction event on Memory 19 detected.
18
NCE19
NCE19
Memory 19 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ENCIE19] 
is enabled.
0b - No non-correctable error event on Memory 19 detected.
1b - Non-correctable error event on Memory 19 detected.
17-16
—
Reserved
15
SBC20
SBC20
Memory 20 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ESCIE20] 
is enabled.
0b - No single-bit correction event on Memory 20 detected.
1b - Single-bit correction event on Memory 20 detected.
14
NCE20
NCE20
Memory 20 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ENCIE20] 
is enabled.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2108 / 5251


---
# 페이지 192

Table continued from the previous page...
Field
Function
0b - No non-correctable error event on Memory 20 detected.
1b - Non-correctable error event on Memory 20 detected.
13-12
—
Reserved
11
SBC21
SBC21
Memory 21 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ESCIE21] 
is enabled.
0b - No single-bit correction event on Memory 21 detected.
1b - Single-bit correction event on Memory 21 detected.
10
NCE21
NCE21
Memory 21 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ENCIE21] 
is enabled.
0b - No non-correctable error event on Memory 21 detected.
1b - Non-correctable error event on Memory 21 detected.
9-8
—
Reserved
7-4
—
Reserved
3-0
—
Reserved
51.5.8 ERM Memory a Error Address Register (EAR0 - EAR21)
Offset
Register
Offset
EAR0
100h
EAR1
110h
EAR10
1A0h
EAR11
1B0h
EAR12
1C0h
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2109 / 5251


---
# 페이지 193

Table continued from the previous page...
Register
Offset
EAR13
1D0h
EAR14
1E0h
EAR15
1F0h
EAR16
200h
EAR17
210h
EAR18
220h
EAR19
230h
EAR20
240h
EAR21
250h
Function
Each ERM Memory n Error Address Register is a 32-bit register for capturing the address of the last ECC event in Memoryn, 
wheren denotes the memory channel. Any attempted write to EARn is ignored.
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
EAR 
W
Reset
0
0
0
0
0
0
0
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
EAR 
W
Reset
0
0
0
0
0
0
0
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
EAR
EAR
Memoryn Error Address — This field contains the faulting system address of the last recorded ECC event 
on Memoryn.
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2110 / 5251


---
# 페이지 194

51.5.9 ERM Memory a Syndrome Register (SYN0 - SYN21)
Offset
Register
Offset
SYN0
104h
SYN1
114h
SYN10
1A4h
SYN11
1B4h
SYN12
1C4h
SYN13
1D4h
SYN14
1E4h
SYN15
1F4h
SYN16
204h
SYN21
254h
Function
The ERM Memory n Syndrome Register is a 32-bit register for capturing the calculated syndrome of the last ECC event on 
Memoryn, wheren denotes the memory channel. Any attempted write to SYNn is ignored. The syndrome value identifies the 
pertinent bit position on a correctable, single-bit data inversion or a non-correctable, single-bit address inversion. The syndrome 
value does not provide any additional diagnostic information on non-correctable, multi-bit inversions.
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
SYNDROME 
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
W
Reset
0
0
0
0
0
0
0
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
SYNDROME
SYNDROME
Memoryn Syndrome — This field contains the ECC syndrome associated with the last recorded ECC event 
on Memoryn.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2111 / 5251


---
# 페이지 195

Table continued from the previous page...
Field
Function
23-0
—
Reserved
51.5.10 ERM Memory a Correctable Error Count Register (CORR_ERR_CNT0 - CORR_ERR_CNT21)
Offset
Register
Offset
CORR_ERR_CNT0
108h
CORR_ERR_CNT1
118h
CORR_ERR_CNT2
128h
CORR_ERR_CNT3
138h
CORR_ERR_CNT4
148h
CORR_ERR_CNT5
158h
CORR_ERR_CNT6
168h
CORR_ERR_CNT7
178h
CORR_ERR_CNT8
188h
CORR_ERR_CNT9
198h
CORR_ERR_CNT10
1A8h
CORR_ERR_CNT11
1B8h
CORR_ERR_CNT12
1C8h
CORR_ERR_CNT13
1D8h
CORR_ERR_CNT14
1E8h
CORR_ERR_CNT15
1F8h
CORR_ERR_CNT16
208h
CORR_ERR_CNT17
218h
CORR_ERR_CNT18
228h
CORR_ERR_CNT19
238h
CORR_ERR_CNT20
248h
CORR_ERR_CNT21
258h
Function
Each 32-bit ERM Memory n Correctable Error Count Register records the count value of the number of correctable ECC error 
events for Memoryn, wheren denotes the memory channel.
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2112 / 5251


---
# 페이지 196

 
Non-correctable errors are considered a serious fault, so the ERM does not provide any mechanism to count 
non-correctable errors. Only correctable errors are counted.
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
W
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
Reserved 
COUNT 
W
0
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
Fields
Field
Function
31-8
—
Reserved
7-0
COUNT
Memory n Correctable Error Count
For each correctable error event, the ERM increments this field's error count value until the counter reaches 
its maximum value FFh. COUNT value will stop when it reaches maximum value FFh and will not wrap even 
if additional errors occur.
Read this field to determine the correctable error count value so far.
Write all zeros to this field to reset the counter. Writing a non-zero value has no effect.
51.6 ERM_1 register descriptions
You can access the programming model:
• Only in supervisor mode
• Using only 32-bit (word) accesses
Any of the following attempted references to the programming model generates an error termination:
• In user mode
• Using non-32-bit access sizes
Based on the design implementation, the following XFR error behavior is evident at the IPS interface.
• Within the ERM memory map, an XFR error is evident at reserved addresses from location 20h to FFh.
• No XFR error is evident at reserved addresses in memory spaces allocated to each channel. For example: For channel 0, for 
read/write accesses to reserved address 10Ch, the XFR error is 0.
• For accesses to locations beyond the addresses allocated for the final channel, the XFR error is 1.
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2113 / 5251


---
# 페이지 197

 
• See the chip-specific ERM information at the beginning of this chapter for details on Memory channel mapping.
• To access the channel registers, corresponding memory channel clock must be enabled.
  NOTE  
51.6.1 ERM_1 memory map
ERM_1 base address: 4000_C000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
ERM Configuration Register 0 (CR0)
32
RW
0000_0000h
4h
ERM Configuration Register 1 (CR1)
32
RW
0000_0000h
8h
ERM Configuration Register 2 (CR2)
32
RW
0000_0000h
10h
ERM Status Register 0 (SR0)
32
RW
0000_0000h
14h
ERM Status Register 1 (SR1)
32
RW
0000_0000h
18h
ERM Status Register 2 (SR2)
32
RW
0000_0000h
100h
ERM Memory 0 Error Address Register (EAR0)
32
R
0000_0000h
104h
ERM Memory 0 Syndrome Register (SYN0)
32
R
0000_0000h
108h
ERM Memory 0 Correctable Error Count Register 
(CORR_ERR_CNT0)
32
RW
0000_0000h
128h
ERM Memory 2 Correctable Error Count Register 
(CORR_ERR_CNT2)
32
RW
0000_0000h
138h
ERM Memory 3 Correctable Error Count Register 
(CORR_ERR_CNT3)
32
RW
0000_0000h
148h
ERM Memory 4 Correctable Error Count Register 
(CORR_ERR_CNT4)
32
RW
0000_0000h
158h
ERM Memory 5 Correctable Error Count Register 
(CORR_ERR_CNT5)
32
RW
0000_0000h
168h
ERM Memory 6 Correctable Error Count Register 
(CORR_ERR_CNT6)
32
RW
0000_0000h
178h
ERM Memory 7 Correctable Error Count Register 
(CORR_ERR_CNT7)
32
RW
0000_0000h
188h
ERM Memory 8 Correctable Error Count Register 
(CORR_ERR_CNT8)
32
RW
0000_0000h
198h
ERM Memory 9 Correctable Error Count Register 
(CORR_ERR_CNT9)
32
RW
0000_0000h
1A0h
ERM Memory 10 Error Address Register (EAR10)
32
R
0000_0000h
1A4h
ERM Memory 10 Syndrome Register (SYN10)
32
R
0000_0000h
1A8h
ERM Memory 10 Correctable Error Count Register 
(CORR_ERR_CNT10)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2114 / 5251


---
# 페이지 198

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1B0h
ERM Memory 11 Error Address Register (EAR11)
32
R
0000_0000h
1B4h
ERM Memory 11 Syndrome Register (SYN11)
32
R
0000_0000h
1B8h
ERM Memory 11 Correctable Error Count Register 
(CORR_ERR_CNT11)
32
RW
0000_0000h
1C0h
ERM Memory 12 Error Address Register (EAR12)
32
R
0000_0000h
1C4h
ERM Memory 12 Syndrome Register (SYN12)
32
R
0000_0000h
1C8h
ERM Memory 12 Correctable Error Count Register 
(CORR_ERR_CNT12)
32
RW
0000_0000h
1D0h
ERM Memory 13 Error Address Register (EAR13)
32
R
0000_0000h
1D4h
ERM Memory 13 Syndrome Register (SYN13)
32
R
0000_0000h
1D8h
ERM Memory 13 Correctable Error Count Register 
(CORR_ERR_CNT13)
32
RW
0000_0000h
1E0h
ERM Memory 14 Error Address Register (EAR14)
32
R
0000_0000h
1E4h
ERM Memory 14 Syndrome Register (SYN14)
32
R
0000_0000h
1E8h
ERM Memory 14 Correctable Error Count Register 
(CORR_ERR_CNT14)
32
RW
0000_0000h
1F0h
ERM Memory 15 Error Address Register (EAR15)
32
R
0000_0000h
1F4h
ERM Memory 15 Syndrome Register (SYN15)
32
R
0000_0000h
1F8h
ERM Memory 15 Correctable Error Count Register 
(CORR_ERR_CNT15)
32
RW
0000_0000h
220h
ERM Memory 18 Error Address Register (EAR18)
32
R
0000_0000h
224h
ERM Memory 18 Syndrome Register (SYN18)
32
R
0000_0000h
228h
ERM Memory 18 Correctable Error Count Register 
(CORR_ERR_CNT18)
32
RW
0000_0000h
230h
ERM Memory 19 Error Address Register (EAR19)
32
R
0000_0000h
234h
ERM Memory 19 Syndrome Register (SYN19)
32
R
0000_0000h
238h
ERM Memory 19 Correctable Error Count Register 
(CORR_ERR_CNT19)
32
RW
0000_0000h
51.6.2 ERM Configuration Register 0 (CR0)
Offset
Register
Offset
CR0
0h
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2115 / 5251


---
# 페이지 199

Function
This 32-bit control register configures the interrupt notification capability for available channels.
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
ESCIE
0 
ENCIE
0 
0
Reserved 
0
ESCIE
2 
ENCIE
2 
0
ESCIE
3 
ENCIE
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
ESCIE
4 
ENCIE
4 
0
ESCIE
5 
ENCIE
5 
0
ESCIE
6 
ENCIE
6 
0
ESCIE
7 
ENCIE
7 
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
ESCIE0
ESCIE0
Enable Memory 0 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 0 single-bit correction events is disabled.
1b - Interrupt notification of Memory 0 single-bit correction events is enabled.
30
ENCIE0
ENCIE0
Enable Memory 0 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 0 non-correctable error events is disabled.
1b - Interrupt notification of Memory 0 non-correctable error events is enabled.
29-28
—
Reserved
27-26
—
Reserved
25-24
—
Reserved
23
ESCIE2
ESCIE2
Enable Memory 2 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 2 single-bit correction events is disabled.
1b - Interrupt notification of Memory 2 single-bit correction events is enabled.
22
ENCIE2
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2116 / 5251


---
# 페이지 200

Table continued from the previous page...
Field
Function
ENCIE2
Enable Memory 2 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 2 non-correctable error events is disabled.
1b - Interrupt notification of Memory 2 non-correctable error events is enabled.
21-20
—
Reserved
19
ESCIE3
ESCIE3
Enable Memory 3 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 3 single-bit correction events is disabled.
1b - Interrupt notification of Memory 3 single-bit correction events is enabled.
18
ENCIE3
ENCIE3
Enable Memory 3 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 3 non-correctable error events is disabled.
1b - Interrupt notification of Memory 3 non-correctable error events is enabled.
17-16
—
Reserved
15
ESCIE4
ESCIE4
Enable Memory 4 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 4 single-bit correction events is disabled.
1b - Interrupt notification of Memory 4 single-bit correction events is enabled.
14
ENCIE4
ENCIE4
Enable Memory 4 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 4 non-correctable error events is disabled.
1b - Interrupt notification of Memory 4 non-correctable error events is enabled.
13-12
—
Reserved
11
ESCIE5
ESCIE5
Enable Memory 5 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 5 single-bit correction events is disabled.
1b - Interrupt notification of Memory 5 single-bit correction events is enabled.
10
ENCIE5
Enable Memory 5 Non-Correctable Interrupt Notification
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2117 / 5251


---
# 페이지 201

Table continued from the previous page...
Field
Function
ENCIE5
0b - Interrupt notification of Memory 5 non-correctable error events is disabled.
1b - Interrupt notification of Memory 5 non-correctable error events is enabled.
9-8
—
Reserved
7
ESCIE6
ESCIE6
Enable Memory 6 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 6 single-bit correction events is disabled.
1b - Interrupt notification of Memory 6 single-bit correction events is enabled.
6
ENCIE6
ENCIE6
Enable Memory 6 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 6 non-correctable error events is disabled.
1b - Interrupt notification of Memory 6 non-correctable error events is enabled.
5-4
—
Reserved
3
ESCIE7
ESCIE7
Enable Memory 7 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 7 single-bit correction events is disabled.
1b - Interrupt notification of Memory 7 single-bit correction events is enabled.
2
ENCIE7
ENCIE7
Enable Memory 7 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 7 non-correctable error events is disabled.
1b - Interrupt notification of Memory 7 non-correctable error events is enabled.
1-0
—
Reserved
51.6.3 ERM Configuration Register 1 (CR1)
Offset
Register
Offset
CR1
4h
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2118 / 5251


---
# 페이지 202

Function
This 32-bit control register configures the interrupt notification capability for available channels.
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
ESCIE
8 
ENCIE
8 
0
ESCIE
9 
ENCIE
9 
0
ESCIE
10 
ENCIE
10 
0
ESCIE
11 
ENCIE
11 
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
ESCIE
12 
ENCIE
12 
0
ESCIE
13 
ENCIE
13 
0
ESCIE
14 
ENCIE
14 
0
ESCIE
15 
ENCIE
15 
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
ESCIE8
ESCIE8
Enable Memory 8 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 8 single-bit correction events is disabled.
1b - Interrupt notification of Memory 8 single-bit correction events is enabled.
30
ENCIE8
ENCIE8
Enable Memory 8 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 8 non-correctable error events is disabled.
1b - Interrupt notification of Memory 8 non-correctable error events is enabled.
29-28
—
Reserved
27
ESCIE9
ESCIE9
Enable Memory 9 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 9 single-bit correction events is disabled.
1b - Interrupt notification of Memory 9 single-bit correction events is enabled.
26
ENCIE9
ENCIE9
Enable Memory 9 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 9 non-correctable error events is disabled.
1b - Interrupt notification of Memory 9 non-correctable error events is enabled.
25-24
Reserved
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2119 / 5251


---
# 페이지 203

Table continued from the previous page...
Field
Function
—
23
ESCIE10
ESCIE10
Enable Memory 10 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 10 single-bit correction events is disabled.
1b - Interrupt notification of Memory 10 single-bit correction events is enabled.
22
ENCIE10
ENCIE10
Enable Memory 10 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 10 non-correctable error events is disabled.
1b - Interrupt notification of Memory 10 non-correctable error events is enabled.
21-20
—
Reserved
19
ESCIE11
ESCIE11
Enable Memory 11 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 11 single-bit correction events is disabled.
1b - Interrupt notification of Memory 11 single-bit correction events is enabled.
18
ENCIE11
ENCIE11
Enable Memory 11 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 11 non-correctable error events is disabled.
1b - Interrupt notification of Memory 11 non-correctable error events is enabled.
17-16
—
Reserved
15
ESCIE12
ESCIE12
Enable Memory 12 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 12 single-bit correction events is disabled.
1b - Interrupt notification of Memory 12 single-bit correction events is enabled.
14
ENCIE12
ENCIE12
Enable Memory 12 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 12 non-correctable error events is disabled.
1b - Interrupt notification of Memory 12 non-correctable error events is enabled.
13-12
Reserved
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2120 / 5251


---
# 페이지 204

Table continued from the previous page...
Field
Function
—
11
ESCIE13
ESCIE13
Enable Memory 13 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 13 single-bit correction events is disabled.
1b - Interrupt notification of Memory 13 single-bit correction events is enabled.
10
ENCIE13
ENCIE13
Enable Memory 13 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 13 non-correctable error events is disabled.
1b - Interrupt notification of Memory 13 non-correctable error events is enabled.
9-8
—
Reserved
7
ESCIE14
ESCIE14
Enable Memory 14 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 14 single-bit correction events is disabled.
1b - Interrupt notification of Memory 14 single-bit correction events is enabled.
6
ENCIE14
ENCIE14
Enable Memory 14 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 14 non-correctable error events is disabled.
1b - Interrupt notification of Memory 14 non-correctable error events is enabled.
5-4
—
Reserved
3
ESCIE15
ESCIE15
Enable Memory 15 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 15 single-bit correction events is disabled.
1b - Interrupt notification of Memory 15 single-bit correction events is enabled.
2
ENCIE15
ENCIE15
Enable Memory 15 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 15 non-correctable error events is disabled.
1b - Interrupt notification of Memory 15 non-correctable error events is enabled.
1-0
Reserved
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2121 / 5251


---
# 페이지 205

Table continued from the previous page...
Field
Function
—
51.6.4 ERM Configuration Register 2 (CR2)
Offset
Register
Offset
CR2
8h
Function
This 32-bit control register configures the interrupt notification capability for available channels.
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
0
Reserved 
0
ESCIE
18 
ENCIE
18 
0
ESCIE
19 
ENCIE
19 
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
Reserved 
0
Reserved 
0
Reserved 
0
Reserved 
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
31-30
—
Reserved
29-28
—
Reserved
27-26
—
Reserved
25-24
—
Reserved
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2122 / 5251


---
# 페이지 206

Table continued from the previous page...
Field
Function
23
ESCIE18
ESCIE18
Enable Memory 18 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 18 single-bit correction events is disabled.
1b - Interrupt notification of Memory 18 single-bit correction events is enabled.
22
ENCIE18
ENCIE18
Enable Memory 18 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 18 non-correctable error events is disabled.
1b - Interrupt notification of Memory 18 non-correctable error events is enabled.
21-20
—
Reserved
19
ESCIE19
ESCIE19
Enable Memory 19 Single Correction Interrupt Notification
0b - Interrupt notification of Memory 19 single-bit correction events is disabled.
1b - Interrupt notification of Memory 19 single-bit correction events is enabled.
18
ENCIE19
ENCIE19
Enable Memory 19 Non-Correctable Interrupt Notification
0b - Interrupt notification of Memory 19 non-correctable error events is disabled.
1b - Interrupt notification of Memory 19 non-correctable error events is enabled.
17-16
—
Reserved
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
—
Reserved
7-6
—
Reserved
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2123 / 5251


---
# 페이지 207

Table continued from the previous page...
Field
Function
5-4
—
Reserved
3-2
—
Reserved
1-0
—
Reserved
51.6.5 ERM Status Register 0 (SR0)
Offset
Register
Offset
SR0
10h
Function
This 32-bit status register reports error events for available channels.
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
SBC0 
NCE0 
0
0
SBC2 
NCE2 
0
SBC3 
NCE3 
0
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
SBC4 
NCE4 
0
SBC5 
NCE5 
0
SBC6 
NCE6 
0
SBC7 
NCE7 
0
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
31
SBC0
SBC0
Memory 0 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ESCIE0] 
is enabled.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2124 / 5251


---
# 페이지 208

Table continued from the previous page...
Field
Function
0b - No single-bit correction event on Memory 0 detected.
1b - Single-bit correction event on Memory 0 detected.
30
NCE0
NCE0
Memory 0 Non-Correctable Error Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ENCIE0] 
is enabled.
0b - No non-correctable error event on Memory 0 detected.
1b - Non-correctable error event on Memory 0 detected.
29-28
—
Reserved
27-24
—
Reserved
23
SBC2
SBC2
Memory 2 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ESCIE2] 
is enabled.
0b - No single-bit correction event on Memory 2 detected.
1b - Single-bit correction event on Memory 2 detected.
22
NCE2
NCE2
Memory 2 Non-Correctable Error Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ENCIE2] 
is enabled.
0b - No non-correctable error event on Memory 2 detected.
1b - Non-correctable error event on Memory 2 detected.
21-20
—
Reserved
19
SBC3
SBC3
Memory 3 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ESCIE3] 
is enabled.
0b - No single-bit correction event on Memory 3 detected.
1b - Single-bit correction event on Memory 3 detected.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2125 / 5251


---
# 페이지 209

Table continued from the previous page...
Field
Function
18
NCE3
NCE3
Memory 3 Non-Correctable Error Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ENCIE3] 
is enabled.
0b - No non-correctable error event on Memory 3 detected.
1b - Non-correctable error event on Memory 3 detected.
17-16
—
Reserved
15
SBC4
SBC4
Memory 4 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ESCIE4] 
is enabled.
0b - No single-bit correction event on Memory 4 detected.
1b - Single-bit correction event on Memory 4 detected.
14
NCE4
NCE4
Memory 4 Non-Correctable Error Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ENCIE4] 
is enabled.
0b - No non-correctable error event on Memory 4 detected.
1b - Non-correctable error event on Memory 4 detected.
13-12
—
Reserved
11
SBC5
SBC5
Memory 5 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ESCIE5] 
is enabled.
0b - No single-bit correction event on Memory 5 detected.
1b - Single-bit correction event on Memory 5 detected.
10
NCE5
NCE5
Memory 5 Non-Correctable Error Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ENCIE5] 
is enabled.
0b - No non-correctable error event on Memory 5 detected.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2126 / 5251


---
# 페이지 210

Table continued from the previous page...
Field
Function
1b - Non-correctable error event on Memory 5 detected.
9-8
—
Reserved
7
SBC6
SBC6
Memory 6 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ESCIE6] 
is enabled.
0b - No single-bit correction event on Memory 6 detected.
1b - Single-bit correction event on Memory 6 detected.
6
NCE6
NCE6
Memory 6 Non-Correctable Error Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ENCIE6] 
is enabled.
0b - No non-correctable error event on Memory 6 detected.
1b - Non-correctable error event on Memory 6 detected.
5-4
—
Reserved
3
SBC7
SBC7
Memory 7 Single-Bit Correction Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ESCIE7] 
is enabled.
0b - No single-bit correction event on Memory 7 detected.
1b - Single-bit correction event on Memory 7 detected.
2
NCE7
NCE7
Memory 7 Non-Correctable Error Event
Write 1 to clear this field.This write also clears the corresponding interrupt notification, if CR0[ENCIE7] 
is enabled.
0b - No non-correctable error event on Memory 7 detected.
1b - Non-correctable error event on Memory 7 detected.
1-0
—
Reserved
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2127 / 5251


---
# 페이지 211

51.6.6 ERM Status Register 1 (SR1)
Offset
Register
Offset
SR1
14h
Function
This 32-bit status register reports error events for available channels.
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
SBC8 
NCE8 
0
SBC9 
NCE9 
0
SBC10 NCE10 
0
SBC11 NCE11 
0
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
SBC12 NCE12 
0
SBC13 NCE13 
0
SBC14 NCE14 
0
SBC15 NCE15 
0
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
31
SBC8
SBC8
Memory 8 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE8] 
is enabled.
0b - No single-bit correction event on Memory 8 detected.
1b - Single-bit correction event on Memory 8 detected.
30
NCE8
NCE8
Memory 8 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE8] 
is enabled.
0b - No non-correctable error event on Memory 8 detected.
1b - Non-correctable error event on Memory 8 detected.
29-28
—
Reserved
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2128 / 5251


---
# 페이지 212

Table continued from the previous page...
Field
Function
27
SBC9
SBC9
Memory 9 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE9] 
is enabled.
0b - No single-bit correction event on Memory 9 detected.
1b - Single-bit correction event on Memory 9 detected.
26
NCE9
NCE9
Memory 9 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE9] 
is enabled.
0b - No non-correctable error event on Memory 9 detected.
1b - Non-correctable error event on Memory 9 detected.
25-24
—
Reserved
23
SBC10
SBC10
Memory 10 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE10] 
is enabled.
0b - No single-bit correction event on Memory 10 detected.
1b - Single-bit correction event on Memory 10 detected.
22
NCE10
NCE10
Memory 10 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE10] 
is enabled.
0b - No non-correctable error event on Memory 10 detected.
1b - Non-correctable error event on Memory 10 detected.
21-20
—
Reserved
19
SBC11
SBC11
Memory 11 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE11] 
is enabled.
0b - No single-bit correction event on Memory 11 detected.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2129 / 5251


---
# 페이지 213

Table continued from the previous page...
Field
Function
1b - Single-bit correction event on Memory 11 detected.
18
NCE11
NCE11
Memory 11 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE11] 
is enabled.
0b - No non-correctable error event on Memory 11 detected.
1b - Non-correctable error event on Memory 11 detected.
17-16
—
Reserved
15
SBC12
SBC12
Memory 12 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE12] 
is enabled.
0b - No single-bit correction event on Memory 12 detected.
1b - Single-bit correction event on Memory 12 detected.
14
NCE12
NCE12
Memory 12 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE12] 
is enabled.
0b - No non-correctable error event on Memory 12 detected.
1b - Non-correctable error event on Memory 12 detected.
13-12
—
Reserved
11
SBC13
SBC13
Memory 13 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE13] 
is enabled.
0b - No single-bit correction event on Memory 13 detected.
1b - Single-bit correction event on Memory 13 detected.
10
NCE13
NCE13
Memory 13 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE13] 
is enabled.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2130 / 5251


---
# 페이지 214

Table continued from the previous page...
Field
Function
0b - No non-correctable error event on Memory 13 detected.
1b - Non-correctable error event on Memory 13 detected.
9-8
—
Reserved
7
SBC14
SBC14
Memory 14 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE14] 
is enabled.
0b - No single-bit correction event on Memory 14 detected.
1b - Single-bit correction event on Memory 14 detected.
6
NCE14
NCE14
Memory 14 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE14] 
is enabled.
0b - No non-correctable error event on Memory 14 detected.
1b - Non-correctable error event on Memory 14 detected.
5-4
—
Reserved
3
SBC15
SBC15
Memory 15 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ESCIE15] 
is enabled.
0b - No single-bit correction event on Memory 15 detected.
1b - Single-bit correction event on Memory 15 detected.
2
NCE15
NCE15
Memory 15 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR1[ENCIE15] 
is enabled.
0b - No non-correctable error event on Memory 15 detected.
1b - Non-correctable error event on Memory 15 detected.
1-0
—
Reserved
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2131 / 5251


---
# 페이지 215

51.6.7 ERM Status Register 2 (SR2)
Offset
Register
Offset
SR2
18h
Function
This 32-bit status register reports error events for available channels.
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
SBC18 NCE18 
0
SBC19 NCE19 
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
W
Reset
0
0
0
0
0
0
0
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
—
Reserved
23
SBC18
SBC18
Memory 18 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ESCIE18] 
is enabled.
0b - No single-bit correction event on Memory 18 detected.
1b - Single-bit correction event on Memory 18 detected.
22
NCE18
NCE18
Memory 18 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ENCIE18] 
is enabled.
Table continues on the next page...
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2132 / 5251


---
# 페이지 216

Table continued from the previous page...
Field
Function
0b - No non-correctable error event on Memory 18 detected.
1b - Non-correctable error event on Memory 18 detected.
21-20
—
Reserved
19
SBC19
SBC19
Memory 19 Single-Bit Correction Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ESCIE19] 
is enabled.
0b - No single-bit correction event on Memory 19 detected.
1b - Single-bit correction event on Memory 19 detected.
18
NCE19
NCE19
Memory 19 Non-Correctable Error Event
Write 1 to clear this field. This write also clears the corresponding interrupt notification, if CR2[ENCIE19] 
is enabled.
0b - No non-correctable error event on Memory 19 detected.
1b - Non-correctable error event on Memory 19 detected.
17-16
—
Reserved
15-12
—
Reserved
11-8
—
Reserved
7-4
—
Reserved
3-0
—
Reserved
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2133 / 5251


---
# 페이지 217

51.6.8 ERM Memory a Error Address Register (EAR0 - EAR19)
Offset
Register
Offset
EAR0
100h
EAR10
1A0h
EAR11
1B0h
EAR12
1C0h
EAR13
1D0h
EAR14
1E0h
EAR15
1F0h
EAR18
220h
EAR19
230h
Function
Each ERM Memory n Error Address Register is a 32-bit register for capturing the address of the last ECC event in Memoryn, 
wheren denotes the memory channel. Any attempted write to EARn is ignored.
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
EAR 
W
Reset
0
0
0
0
0
0
0
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
EAR 
W
Reset
0
0
0
0
0
0
0
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
EAR
EAR
Memoryn Error Address — This field contains the faulting system address of the last recorded ECC event 
on Memoryn.
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2134 / 5251


---
# 페이지 218

51.6.9 ERM Memory a Syndrome Register (SYN0 - SYN19)
Offset
Register
Offset
SYN0
104h
SYN10
1A4h
SYN11
1B4h
SYN12
1C4h
SYN13
1D4h
SYN14
1E4h
SYN15
1F4h
SYN18
224h
SYN19
234h
Function
The ERM Memory n Syndrome Register is a 32-bit register for capturing the calculated syndrome of the last ECC event on 
Memoryn, wheren denotes the memory channel. Any attempted write to SYNn is ignored. The syndrome value identifies the 
pertinent bit position on a correctable, single-bit data inversion or a non-correctable, single-bit address inversion. The syndrome 
value does not provide any additional diagnostic information on non-correctable, multi-bit inversions.
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
SYNDROME 
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
W
Reset
0
0
0
0
0
0
0
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
SYNDROME
SYNDROME
Memoryn Syndrome — This field contains the ECC syndrome associated with the last recorded ECC event 
on Memoryn.
23-0
—
Reserved
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2135 / 5251


---
# 페이지 219

51.6.10 ERM Memory a Correctable Error Count Register (CORR_ERR_CNT0 - CORR_ERR_CNT19)
Offset
Register
Offset
CORR_ERR_CNT0
108h
CORR_ERR_CNT2
128h
CORR_ERR_CNT3
138h
CORR_ERR_CNT4
148h
CORR_ERR_CNT5
158h
CORR_ERR_CNT6
168h
CORR_ERR_CNT7
178h
CORR_ERR_CNT8
188h
CORR_ERR_CNT9
198h
CORR_ERR_CNT10
1A8h
CORR_ERR_CNT11
1B8h
CORR_ERR_CNT12
1C8h
CORR_ERR_CNT13
1D8h
CORR_ERR_CNT14
1E8h
CORR_ERR_CNT15
1F8h
CORR_ERR_CNT18
228h
CORR_ERR_CNT19
238h
Function
Each 32-bit ERM Memory n Correctable Error Count Register records the count value of the number of correctable ECC error 
events for Memoryn, wheren denotes the memory channel.
 
Non-correctable errors are considered a serious fault, so the ERM does not provide any mechanism to count 
non-correctable errors. Only correctable errors are counted.
  NOTE  
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2136 / 5251


---
# 페이지 220

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
Reserved 
COUNT 
W
0
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
Fields
Field
Function
31-8
—
Reserved
7-0
COUNT
Memory n Correctable Error Count
For each correctable error event, the ERM increments this field's error count value until the counter reaches 
its maximum value FFh. COUNT value will stop when it reaches maximum value FFh and will not wrap even 
if additional errors occur.
Read this field to determine the correctable error count value so far.
Write all zeros to this field to reset the counter. Writing a non-zero value has no effect.
51.7 Glossary
ECC
Error correction code
NXP Semiconductors
Error Reporting Module (ERM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2137 / 5251


---