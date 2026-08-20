# 페이지 7

Chapter 50
Error Injection Module (EIM)
50.1 Chip-specific EIM information
50.1.1 EIM instances
This chip supports up to four instances of EIM:
• EIM_0
• EIM_1
• EIM_2
• EIM_3
Table 272. EIM instances
Instances
S32K388/S32K389
S32K358/S32K348/S32K338/
S32K328
S32K322/S32K324/S32K344/S32K342/S32K341/
S32K314/S32K312/S32K311/S32K310
EIM_0
Yes
Yes
Yes
EIM_1
Yes
Yes
No
EIM_2
Yes
Yes
No
EIM_3
Yes
No
No
50.1.2 EIM0 base address
Table 273. EIM0 base address
EIM0 base address
Variants
0x4025_8000
S32K322/S32K324/S32K344/S32K342/S32K341/S32K314/S32K312/S32K311/
S32K310
0x4050_C000
S32K388/S32K389/S32K358/S32K348/S32K338/S32K328
50.1.3 EIM channel mapping
EIM integrates with the memory controller and memory array to enable error injection in a controlled way. Each memory controller 
has its own EIM channel.
Cortex-M7_1, EMAC, AIPS2 gasket, Cortex-M7 lockstep, and QuadSPI gasket are not available in the S32K312 and S32K311 
product variants of the S32K3 family.
Table 274. EIM channel mapping - S32K3x1, S32K3x2, S32K344/S32K324/S32K314
Channel #
Target
Data bits 1
Check bits1
# of data bits
# of check bits
0
SRAM0
Word1[31:0] – SRAM0 
read data[63:32]
Word0[31:24] – SRAM0 
read data ECC[7:0]
64
8
Word2[31:0] – SRAM0 
read data[31:0]
Table continues on the next page...
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1924 / 5251


---
# 페이지 8

Table 274. EIM channel mapping - S32K3x1, S32K3x2, S32K344/S32K324/S32K314 (continued)
Channel #
Target
Data bits 1
Check bits1
# of data bits
# of check bits
1
SRAM12
Word1[31:0] – SRAM1 
read data[63:32]
Word0[31:24] SRAM1 read 
data ECC[7:0]
64
8
Word2[31:0] – SRAM1 
read data[31:0]
2
DMA TCD
Word1[31:0] – DMA TCD 
RAM read data[63:32]
Word0[31:24] DMA 
TCD RAM read 
data checkbits[7:0]
64
8
Word2[31:0] – DMA TCD 
RAM read data[31:0]
3
Cortex-M7_0 IC tag
Word1[12:0] – Cortex-M7_0 
IC tag read data1[28:16]
Word0[31:25] – Cortex-
M7_0 IC tag read data1[6:0]
44
14
Word2[31:22] – Cortex-
M7_0 IC tag 
read data1[15:7]
Word2[21:0] – Cortex-M7_0 
IC tag read data0[28:7]
Word0[24:18] – Cortex-
M7_0 IC tag read data1[6:0]
4
Cortex-M7_0 IC data
Word1[31:0] – Cortex-M7_0 
IC data read data1[71:40]
Word0[31:24] – Cortex-
M7_0 IC data data1[7:0]
128
16
Word2[31:0] – Cortex-M7_0 
IC data read data1[39:8]
Word3[31:0] – Cortex-M7_0 
IC data read data0[71:40]
Word0[23:16] – Cortex-
M7_0 IC data 
read data0[7:0]
Word4[31:0] – Cortex-M7_0 
IC data read data0[39:8]
5
Cortex-M7_0 DC tag
Word1[7:0] – Cortex-M7_0 
DC tag read data3[32:25]
Word0[31:25] – Cortex-
M7_0 DC tag 
read data3[6:0]
104
28
Word2[31:14] – Cortex-
M7_0 DC tag 
read data3[24:7]
Word2[13:0] – Cortex-M7_0 
DC tag read data2[32:19]
Word0[24:18] – Cortex-
M7_0 DC tag 
read data2[6:0]
Word3[31:20] – Cortex-
M7_0 DC tag 
read data2[18:7]
Word3[19:0] – Cortex-M7_0 
DC tag read data1[32:13]
Word0[17:11] – Cortex-
M7_0 DC tag 
read data1[6:0]
Word4[31:26] – Cortex-
M7_0 DC tag 
read data1[12:7]
Word4[25:0] – Cortex-M7_0 
DC tag read data0[32:7]
Word0[10:4] – Cortex-M7_0 
DC tag read data0[6:0]
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1925 / 5251


---
# 페이지 9

Table 274. EIM channel mapping - S32K3x1, S32K3x2, S32K344/S32K324/S32K314 (continued)
Channel #
Target
Data bits 1
Check bits1
# of data bits
# of check bits
6
Cortex-M7_0 
DC data0
Word1[31:0] – Cortex-M7_0 
DC data0 read data3[38:7]
Word0[31:25] – Cortex-
M7_0 DC data0 
read data3[6:0]
128
28
Word2[31:0] – Cortex-M7_0 
DC data0 read data2[38:7]
Word0[24:18] – Cortex-
M7_0 DC data0 
read data2[6:0]
Word3[31:0] – Cortex-M7_0 
DC data0 read data1[38:7]
Word0[17:11] – Cortex-
M7_0 DC data0 
read data1[6:0]
Word4[31:0] – Cortex-M7_0 
DC data0 read data0[38:7]
Word0[10:4] – Cortex-M7_0 
DC data0 read data0[6:0]
7
Cortex-M7_0 
DC data1
Word1[31:0] – Cortex-M7_0 
DC data1 read data3[38:7]
Word0[31:25] – Cortex-
M7_0 DC data1 
read data3[6:0]
128
28
Word2[31:0] – Cortex-M7_0 
DC data1 read data2[38:7]
Word0[24:18] – Cortex-
M7_0 DC data1 
read data2[6:0]
Word3[31:0] – Cortex-M7_0 
DC data1 read data1[38:7]
Word0[17:11] – Cortex-
M7_0 DC data1 
read data1[6:0]
Word4[31:0] – Cortex-M7_0 
DC data1 read data0[38:7]
Word0[10:4] – Cortex-M7_0 
DC data1 read data0[6:0]
8
Cortex-M7_1 IC tag
Word1[12:0] – Cortex-M7_1 
IC tag read data1[28:16]
Word0[31:25] – Cortex-
M7_1 IC tag read data1[6:0]
44
14
Word2[31:22] – Cortex-
M7_1 IC tag 
read data1[15:7]
Word2[21:0] – Cortex-M7_1 
IC tag read data0[28:7]
Word0[24:18] – Cortex-
M7_1 IC tag read data0[6:0]
9
Cortex-M7_1 IC tag
Word1[31:0] – Cortex-M7_1 
IC data read data0[71:40]
Word0[31:24] – Cortex-
M7_1 IC data 
read data1[7:0]
128
16
Word2[31:0] – Cortex-M7_1 
IC data read data0[39:8]
Word3[31:0] – Cortex-M7_1 
IC data read data0[71:40]
Word0[23:16] – Cortex-
M7_1 IC data 
read data0[7:0]
Word4[31:0] – Cortex-M7_1 
IC data read data0[39:8]
10
Cortex-M7_1 DC tag
Word1[7:0] – Cortex-M7_1 
DC tag read data3[32:25]
Word0[31:25] – Cortex-
M7_1 DC tag 
read data3[6:0]
104
28
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1926 / 5251


---
# 페이지 10

Table 274. EIM channel mapping - S32K3x1, S32K3x2, S32K344/S32K324/S32K314 (continued)
Channel #
Target
Data bits 1
Check bits1
# of data bits
# of check bits
Word2[31:14] – Cortex-
M7_1 DC tag 
read data3[24:7]
Word2[31:0] – Cortex-M7_1 
DC tag read data2[32:19]
Word0[24:18] – Cortex-
M7_1 DC tag 
read data2[6:0]
Word3[31:20] – Cortex-
M7_1 DC tag 
read data1[18:7]
Word3[19:0] – Cortex-M7_1 
DC tag read data1[32:13]
Word0[17:11] – Cortex-
M7_1 DC tag 
read data1[6:0]
Word4[31:26] – Cortex-
M7_1 DC tag 
read data1[12:7]
Word4[25:0] – Cortex-M7_1 
DC tag read data0[32:7]
Word0[10:4] – Cortex-M7_1 
DC tag read data0[6:0]
11
Cortex-M7_1 
DC data0
Word1[31:0] – Cortex-M7_1 
DC data0 read data3[38:7]
Word0[31:25] – Cortex-
M7_1 DC data0 
read data3[6:0]
128
28
Word2[31:0] – Cortex-M7_1 
DC data0 read data2[38:7]
Word0[24:18] – Cortex-
M7_1 DC data0 
read data2[6:0]
Word3[31:0] – Cortex-M7_1 
DC data0 read data1[38:7]
Word0[17:11] – Cortex-
M7_1 DC data0 
read data1[6:0]
Word4[31:0] – Cortex-M7_1 
DC data0 read data0[38:7]
Word0[10:4] – Cortex-M7_1 
DC data0 read data0[6:0]
12
Cortex-M7_1 
DC data1
Word1[31:0] – Cortex-M7_1 
DC data1 read data0[38:7]
Word0[31:25] – Cortex-
M7_1 DC data1 
read data3[6:0]
128
28
Word2[31:0] – Cortex-M7_1 
DC data1 read data0[38:7]
Word0[24:18] – Cortex-
M7_1 DC data1 
read data2[6:0]
Word3[31:0] – Cortex-M7_1 
DC data1 read data0[38:7]
Word0[17:11] – Cortex-
M7_1 DC data1 
read data1[6:0]
Word4[31:0] – Cortex-M7_1 
DC data1 read data0[38:7]
Word0[10:4] – Cortex-M7_1 
DC data1 read data0[6:0]
13
Cortex-M7_0 ITCM
Word1[31:0] – Cortex-M7_0 
ITCM read data[63:32]
Word0[31:24] – Cortex-
M7_0 ITCM read 
data ECC[7:0]
64
8
Word2[31:0] – Cortex-M7_0 
ITCM read data[31:0]
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1927 / 5251


---
# 페이지 11

Table 274. EIM channel mapping - S32K3x1, S32K3x2, S32K344/S32K324/S32K314 (continued)
Channel #
Target
Data bits 1
Check bits1
# of data bits
# of check bits
14
Cortex-M7_0 D0TCM Word1[31:0] – Cortex-M7_0 
D0TCM read data[31:0]
Word0[31:24] – Cortex-
M7_0 D0TCM read 
data ECC[7:0]
32
8
15
Cortex-M7_0 D1TCM Word1[31:0] – Cortex-M7_0 
D1TCM read data[31:0]
Word0[31:24] – Cortex-
M7_0 D1TCM read 
data ECC[7:0]
32
8
16
Cortex-M7_1 ITCM
Word1[31:0] – Cortex-M7_1 
ITCM read data[63:32]
Word0[31:24] – Cortex-
M7_1 ITCM read 
data ECC[7:0]
64
8
Word2[31:0] – Cortex-M7_1 
ITCM read data[31:0]
17
Cortex-M7_1 D0TCM Word1[31:0] – Cortex-M7_1 
D0TCM read data[31:0]
Word0[31:24] – Cortex-
M7_1 D0TCM read 
data ECC[7:0]
32
8
18
Cortex-M7_1 D1TCM Word1[31:0] – Cortex-M7_1 
D1TCM read data[31:0]
Word0[31:24] – Cortex-
M7_1 D1TCM read 
data ECC[7:0]
32
8
19
EMAC gasket
Word1[27:0] – EMAC AHB 
write data[63:36]
—
188
0
Word2[31:28] – EMAC AHB 
write data[35:32]
Word2[27:0] – EMAC AHB 
write data[31:4]
Word3[31:28] – EMAC AHB 
write data[3:0]
Word3[27:0] – EMAC AHB 
read data[63:36]
Word4[31:28] – EMAC AHB 
read data[35:32]
Word4[27:0] – EMAC AHB 
read data[31:4]
Word5[31:28] – EMAC AHB 
read data[3:0]
Word5[27:0] – EMAC 
gasket monitor 
error injection[59:32]
Word6[31:0] – EMAC 
gasket monitor 
error injection[31:0]
20
Cortex-M7 
TCM gasket
Word1[27:0] – TCM AHB 
write data[63:36]
—
188
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1928 / 5251


---
# 페이지 12

Table 274. EIM channel mapping - S32K3x1, S32K3x2, S32K344/S32K324/S32K314 (continued)
Channel #
Target
Data bits 1
Check bits1
# of data bits
# of check bits
Word2[31:28] – TCM AHB 
write data[35:32]
Word2[27:0] – TCM AHB 
write data[31:4]
Word3[31:28] – TCM AHB 
write data[3:0]
Word3[27:0] – TCM AHB 
read data[63:36]
Word4[31:28] – TCM AHB 
read data[35:32]
Word4[27:0] – TCM AHB 
read data[31:4]
Word5[31:28] – TCM AHB 
read data[3:0]
Word5[27:0] – TCM 
gasket monitor 
error injection[59:32]
Word6[31:0] – TCM gasket 
monitor error injection[31:0]
21
DMA AXBS 
S0 gasket
Word1[27:0] – DMA 
AXBS S0 gasket monitor 
error injection[59:32]
—
60
0
Word2[31:0] – DMA 
AXBS S0 gasket monitor 
error injection[0:31]
22
DMA AXBS 
S1 gasket
Word1[27:0] – DMA 
AXBS S1 gasket monitor 
error injection[59:32]
—
60
0
Word2[31:0] – DMA 
AXBS S1 gasket monitor 
error injection[31:0]
23
HSE gasket
Word1[27:0] – HSE 
gasket monitor 
error injection[59:32]
—
60
0
Word2[31:0] – HSE gasket 
monitor error injection[31:0]
24
QuadSPI gasket
Word1[27:0] – QuadSPI 
gasket monitor 
error injection[59:32]
—
60
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1929 / 5251


---
# 페이지 13

Table 274. EIM channel mapping - S32K3x1, S32K3x2, S32K344/S32K324/S32K314 (continued)
Channel #
Target
Data bits 1
Check bits1
# of data bits
# of check bits
Word2[31:0] – QuadSPI 
gasket monitor 
error injection[31:0]
25
AIPS1 gasket
Word1[27:0] – AIPS1 
gasket monitor 
error injection[59:32]
—
60
0
Word2[31:0] – AIPS1 
gasket monitor 
error injection[31:0]
26
AIPS2 gasket
Word1[27:0] – AIPS2 
gasket monitor 
error injection[59:32]
—
60
0
Word2[31:0] – AIPS2 
gasket monitor 
error injection[31:0]
27
Cortex-M7 lockstep
Word1[29:0] – Cortex-M7 
error injection[29:0]
—
30
0
28
ECC 
checking address
Word1[1:0] – Inject error on 
flash memory controller port 
0 address checker
—
24
0
Word1[3:2] – Inject error on 
flash memory controller port 
1 address checker
Word1[4:4] – Inject error on 
flash memory controller port 
2 address checker
Word1[7:6] – Inject error 
on PRAM0 controller 
address checker
Word1[9:8] – Inject error 
on PRAM1 controller 
address checker
Word1[11:10] – Inject 
error on 64-bit TCM bus 
address checker
Word1[13:12] – Inject 
error on QuadSPI path 
address checker
Word1[15:14] – Inject error 
on AIPS0 address checker
Word1[17:16] – Inject error 
on AIPS1 address checker
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1930 / 5251


---
# 페이지 14

Table 274. EIM channel mapping - S32K3x1, S32K3x2, S32K344/S32K324/S32K314 (continued)
Channel #
Target
Data bits 1
Check bits1
# of data bits
# of check bits
Word1[19:18] – Inject error 
on AIPS2 address checker
Word1[21:20] – Inject error 
on 32-bit TCM Cortex-M7_0 
path address checker
Word1[23:22] – Inject error 
on 32-bit TCM Cortex-M7_1 
path address checker
Word1[25:24] – Inject error 
on DMA AXBS S0 address 
parity checker3
Word1[27:26] – Inject error 
on DMA AXBS S1 address 
parity checker3
29
EDC checking wdata Word1[1:0] – Inject error 
on PRAM0 controller write 
data checker
—
18
0
Word1[3:2] – Inject error 
on PRAM1 controller write 
data checker
Word1[5:4] – Inject error 
on 64-bit TCM bus write 
data checker
Word1[7:6] – Reserved
Word1[9:8] – Inject error on 
AIPS0 write data checker
Word1[11:10] – Inject 
error on AIPS1 write 
data checker
Word1[13:12] – Inject 
error on AIPS2 write 
data checker
Word1[15:14] – Inject error 
on 32-bit TCM Cortex-M7_0 
path write data checker
Word1[17:16] – Inject error 
on 32-bit TCM Cortex-M7_1 
path write data checker
30
EDC checking rdata
Word1[1:0] – Inject error on 
Cortex-M7_0 AHBM read 
data checker
—
18
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1931 / 5251


---
# 페이지 15

Table 274. EIM channel mapping - S32K3x1, S32K3x2, S32K344/S32K324/S32K314 (continued)
Channel #
Target
Data bits 1
Check bits1
# of data bits
# of check bits
Word1[3:2] – Inject error 
on Cortex-M7_0 AHBP read 
data checker
Word1[5:4] – Inject error on 
DMA read data checker
Word1[7:6] – Inject error on 
STAM read data checker
Word1[9:8] – Inject error on 
HSE read data checker
Word1[11:10] – Inject 
error on EMAC read 
data checker
Word1[13:12] – Inject error 
on Cortex-M7_1 AHBM 
read data checker
Word1[15:14] – Inject error 
on Cortex-M7_1 AHBP read 
data checker
Word1[17:16] – Inject error 
on 32-bit TCM bus path 
read data checker
1. You must write to EICHDi_WORDj registers to inject errors in the desired data and check bits. For details, see tables "Error 
injection channel descriptor: DATA_MASK details" and "DATA_MASK bit: Channel-word mapping" in this chapter.
2. SRAM1 is not available for the S32K342/S32K322/S32K341, S32K312, and S32K311 variants.
3. Applicable for S32K342, S32K341, and S32K322 only.
The two enables, GEIEN and EICHENn, enable the error injection functionality. The former enables it globally and the latter does it 
for a particular channel. This double-layer enable provides protection against accidental enabling and reconfiguration of the error 
injection function for each channel.
EIM provides support for inducing single-bit and multi-bit inversions on read data when accessing peripheral RAMs through its 
data mask registers.
 
For enabling error injection on EDC gaskets (corresponding to channel 28, channel 29, and channel 30), you must 
also enable the fields corresponding to the required EDC gasket in the MSCM_ENEDC register before enabling 
the EIM channel.
EIM_EICHD1_CH01, EIM_EICHD1_CH08, EIM_EICHD1_CH09, EIM_EICHD1_CH10, EIM_EICHD1_CH11, 
EIM_EICHD1_CH12, EIM_EICHD1_CH16, EIM_EICHD1_CH17, EIM_EICHD1_CH18, EIM_EICHD1_CH19, 
EIM_EICHD1_CH21, EIM_EICHD1_CH22, EIM_EICHD1_CH24, EIM_EICHD1_CH26, EIM_EICHD1_CH27 are 
not present in S32K312 and S32K311, hence the registers corresponding to these channels are also not present 
in S32K312 and S32K311.
  NOTE  
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1932 / 5251


---
# 페이지 16

Table 275. EIM_0 channel mapping - S32K358/S32K348/S32K338/S32K328
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
0
Cortex-M7_0 IC 
tag
Word1[12:0] – Cortex-M7_0 IC 
tag read data1[28:16]
Word2[31:22] – Cortex-M7_0 IC 
tag read data1[15:7]
Word2[21:0] – Cortex-M7_0 IC 
tag read data0[28:7]
Word0[31:25] – Cortex- M7_0 IC 
tag read data1[6:0]
Word0[24:18] – Cortex- M7_0 IC 
tag read data1[6:0]
44
14
1
Cortex-M7_0 IC 
data
Word1[31:0] – Cortex-M7_0 IC 
data read data1[71:40]
Word2[31:0] – Cortex-M7_0 IC 
data read data1[39:8]
Word3[31:0] – Cortex-M7_0 IC 
data read data0[71:40]
Word4[31:0] – Cortex-M7_0 IC 
data read data0[39:8]
Word0[31:24] – Cortex- M7_0 IC 
data data1[7:0]
Word0[23:16] – Cortex-M7_0 IC 
data read data0[7:0]
128
16
2
Cortex-M7_0 DC 
tag
Word1[7:0] – Cortex-M7_0 DC tag 
read data3[32:25]
Word2[31:14] – Cortex-M7_0 DC 
tag read data3[24:7]
Word2[13:0] – Cortex-M7_0 DC 
tag read data2[32:19]
Word3[31:20] – Cortex-M7_0 DC 
tag read data2[18:7]
Word3[19:0] – Cortex-M7_0 DC 
tag read data1[32:13]
Word4[31:26] – Cortex-M7_0 DC 
tag read data1[12:7]
Word4[25:0] – Cortex-M7_0 DC 
tag read data0[32:7]
Word0[31:25] – Cortex-M7_0 DC 
tag read data3[6:0]
Word0[24:18] – Cortex-M7_0 DC 
tag read data2[6:0]
Word0[17:11] – Cortex-M7_0 DC 
tag read data1[6:0]
104
28
3
Cortex-M7_0 DC 
data0
Word1[31:0] – Cortex-M7_0 DC 
data0 read data3[38:7]
Word2[31:0] – Cortex-M7_0 DC 
data0 read data2[38:7]
Word3[31:0] – Cortex-M7_0 DC 
data0 read data1[38:7]
Word4[31:0] – Cortex-M7_0 DC 
data0 read data0[38:7]
Word0[31:25] – Cortex-M7_0 DC 
data0 read data3[6:0]
Word0[24:18] – Cortex-M7_0 DC 
data0 read data2[6:0]
Word0[17:11] – Cortex-M7_0 DC 
data0 read data1[6:0]
Word0[10:4] – Cortex-M7_0 DC 
data0 read data0[6:0]
128
28
4
Cortex-M7_0 DC 
data1
Word1[31:0] – Cortex-M7_0 DC 
data1 read data3[38:7]
Word0[31:25] – Cortex-M7_0 DC 
data1 read data3[6:0]
128
28
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1933 / 5251


---
# 페이지 17

Table 275. EIM_0 channel mapping - S32K358/S32K348/S32K338/S32K328 (continued)
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
Word2[31:0] – Cortex-M7_0 DC 
data1 read data2[38:7]
Word3[31:0] – Cortex-M7_0 DC 
data1 read data1[38:7]
Word4[31:0] – Cortex-M7_0 DC 
data1 read data0[38:7]
Word0[24:18] – Cortex-M7_0 DC 
data1 read data2[6:0]
Word0[17:11] – Cortex-M7_0 DC 
data1 read data1[6:0]
Word0[10:4] – Cortex-M7_0 DC 
data1 read data0[6:0]
5
Cortex-M7_1 IC 
tag
Word1[12:0] – Cortex-M7_1 IC 
tag read data1[28:16]
Word2[31:22] – Cortex-M7_1 IC 
tag read data1[15:7]
Word2[21:0] – Cortex-M7_1 IC 
tag read data0[28:7]
Word0[31:25] – Cortex- M7_1 IC 
tag read data1[6:0]
Word0[24:18] – Cortex- M7_1 IC 
tag read data1[6:0]
44
14
6
Cortex-M7_1 IC 
data
Word1[31:0] – Cortex-M7_1 IC 
data read data1[71:40]
Word2[31:0] – Cortex-M7_1 IC 
data read data1[39:8]
Word3[31:0] – Cortex-M7_1 IC 
data read data0[71:40]
Word4[31:0] – Cortex-M7_1 IC 
data read data0[39:8]
Word0[31:24] – Cortex- M7_1 IC 
data data1[7:0]
Word0[23:16] – Cortex-M7_1 IC 
data read data0[7:0]
128
16
7
Cortex-M7_1 DC 
tag
Word1[7:0] – Cortex-M7_1 DC tag 
read data3[32:25]
Word2[31:14] – Cortex-M7_1 DC 
tag read data3[24:7]
Word2[13:0] – Cortex-M7_1 DC 
tag read data2[32:19]
Word3[31:20] – Cortex-M7_1 DC 
tag read data2[18:7]
Word3[19:0] – Cortex-M7_1 DC 
tag read data1[32:13]
Word4[31:26] – Cortex-M7_1 DC 
tag read data1[12:7]
Word4[25:0] – Cortex-M7_1 DC 
tag read data0[32:7]
Word0[31:25] – Cortex-M7_1 DC 
tag read data3[6:0]
Word0[24:18] – Cortex-M7_1 DC 
tag read data2[6:0]
Word0[17:11] – Cortex-M7_1 DC 
tag read data1[6:0]
104
28
8
Cortex-M7_1 DC 
data0
Word1[31:0] – Cortex-M7_1 DC 
data0 read data3[38:7]
Word2[31:0] – Cortex-M7_1 DC 
data0 read data2[38:7]
Word0[31:25] – Cortex-M7_1 DC 
data0 read data3[6:0]
Word0[24:18] – Cortex-M7_1 DC 
data0 read data2[6:0]
128
28
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1934 / 5251


---
# 페이지 18

Table 275. EIM_0 channel mapping - S32K358/S32K348/S32K338/S32K328 (continued)
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
Word3[31:0] – Cortex-M7_1 DC 
data0 read data1[38:7]
Word4[31:0] – Cortex-M7_1 DC 
data0 read data0[38:7]
Word0[17:11] – Cortex-M7_1 DC 
data0 read data1[6:0]
Word0[10:4] – Cortex-M7_1 DC 
data0 read data0[6:0]
9
Cortex-M7_1 DC 
data1
Word1[31:0] – Cortex-M7_1 DC 
data1 read data3[38:7]
Word2[31:0] – Cortex-M7_1 DC 
data1 read data2[38:7]
Word3[31:0] – Cortex-M7_1 DC 
data1 read data1[38:7]
Word4[31:0] – Cortex-M7_1 DC 
data1 read data0[38:7]
Word0[31:25] – Cortex-M7_1 DC 
data1 read data3[6:0]
Word0[24:18] – Cortex-M7_1 DC 
data1 read data2[6:0]
Word0[17:11] – Cortex-M7_1 DC 
data1 read data1[6:0]
Word0[10:4] – Cortex-M7_1 DC 
data1 read data0[6:0]
128
28
10
Cortex-M7_0 
ITCM
Word1[31:0] – Cortex-M7_0 ITCM 
read data[63:32]
Word2[31:0] – Cortex-M7_0 ITCM 
read data[31:0]
Word0[31:24] – Cortex-M7_0 
ITCM read data ECC[7:0]
64
8
11
Cortex-M7_0 
D0TCM
Word1[31:0] – Cortex-M7_0 
D0TCM read data[31:0]
Word0[31:24] – Cortex- M7_0 
D0TCM read data ECC[7:0]
32
8
12
Cortex-M7_0 
d1tcm
Word1[31:0] – Cortex-M7_0 
D1TCM read data[31:0]
Word0[31:24] – Cortex- M7_0 
D1TCM read data ECC[7:0]
32
8
13
Cortex-M7_1 
ITCM
Word1[31:0] – Cortex-M7_1 ITCM 
read data[63:32]
Word2[31:0] – Cortex-M7_1 ITCM 
read data[31:0]
Word0[31:24] – Cortex-M7_1 
ITCM read data ECC[7:0]
64
8
14
Cortex-M7_1 
D0TCM
Word1[31:0] – Cortex-M7_1 
D0TCM read data[31:0]
Word0[31:24] – Cortex- M7_1 
D0TCM read data ECC[7:0]
32
8
15
Cortex-M7_1 
d1tcm
Word1[31:0] – Cortex-M7_1 
D1TCM read data[31:0]
Word0[31:24] – Cortex- M7_1 
D1TCM read data ECC[7:0]
32
8
16
Cortex-M7 
lockstep
Word1[29:0] – Cortex-M7 error 
injection[29:0]
-
30
0
17-31
Unused
Table 276. EIM_1 channel mapping - S32K358/S32K348/S32K338/S32K328
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
0
Cortex-M7_2 IC 
tag
Word1[12:0] – Cortex-M7_2 IC 
tag read data1[28:16]
Word0[31:25] – Cortex- M7_2 IC 
tag read data1[6:0]
44
14
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1935 / 5251


---
# 페이지 19

Table 276. EIM_1 channel mapping - S32K358/S32K348/S32K338/S32K328 (continued)
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
Word2[31:22] – Cortex-M7_2 IC 
tag read data1[15:7]
Word2[21:0] – Cortex-M7_2 IC 
tag read data0[28:7]
Word0[24:18] – Cortex- M7_2 IC 
tag read data1[6:0]
1
Cortex-M7_2 IC 
data
Word1[31:0] – Cortex-M7_2 IC 
data read data1[71:40]
Word2[31:0] – Cortex-M7_2 IC 
data read data1[39:8]
Word3[31:0] – Cortex-M7_2 IC 
data read data0[71:40]
Word4[31:0] – Cortex-M7_2 IC 
data read data0[39:8]
Word0[31:24] – Cortex- M7_2 IC 
data data1[7:0]
Word0[23:16] – Cortex-M7_2 IC 
data read data0[7:0]
128
16
2
Cortex-M7_2 DC 
tag
Word1[7:0] – Cortex-M7_2 DC tag 
read data3[32:25]
Word2[31:14] – Cortex-M7_3 DC 
tag read data3[24:7]
Word2[13:0] – Cortex-M7_2 DC 
tag read data2[32:19]
Word3[31:20] – Cortex-M7_3 DC 
tag read data2[18:7]
Word3[19:0] – Cortex-M7_2 DC 
tag read data1[32:13]
Word4[31:26] – Cortex-M7_3 DC 
tag read data1[12:7]
Word4[25:0] – Cortex-M7_2 DC 
tag read data0[32:7]
Word0[31:25] – Cortex-M7_2 DC 
tag read data3[6:0]
Word0[24:18] – Cortex-M7_2 DC 
tag read data2[6:0]
Word0[17:11] – Cortex-M7_2 DC 
tag read data1[6:0]
104
28
3
Cortex-M7_2 DC 
data0
Word1[31:0] – Cortex-M7_2 DC 
data0 read data3[38:7]
Word2[31:0] – Cortex-M7_2 DC 
data0 read data2[38:7]
Word3[31:0] – Cortex-M7_2 DC 
data0 read data1[38:7]
Word4[31:0] – Cortex-M7_2 DC 
data0 read data0[38:7]
Word0[31:25] – Cortex-M7_2 DC 
data0 read data3[6:0]
Word0[24:18] – Cortex-M7_2 DC 
data0 read data2[6:0]
Word0[17:11] – Cortex-M7_2 DC 
data0 read data1[6:0]
Word0[10:4] – Cortex-M7_2 DC 
data0 read data0[6:0]
128
28
4
Cortex-M7_2 DC 
data1
Word1[31:0] – Cortex-M7_2 DC 
data1 read data3[38:7]
Word2[31:0] – Cortex-M7_2 DC 
data1 read data2[38:7]
Word0[31:25] – Cortex-M7_2 DC 
data1 read data3[6:0]
Word0[24:18] – Cortex-M7_2 DC 
data1 read data2[6:0]
128
28
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1936 / 5251


---
# 페이지 20

Table 276. EIM_1 channel mapping - S32K358/S32K348/S32K338/S32K328 (continued)
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
Word3[31:0] – Cortex-M7_2 DC 
data1 read data1[38:7]
Word4[31:0] – Cortex-M7_2 DC 
data1 read data0[38:7]
Word0[17:11] – Cortex-M7_2 DC 
data1 read data1[6:0]
Word0[10:4] – Cortex-M7_2 DC 
data1 read data0[6:0]
5-9
Unused
10
Cortex-M7_2 
ITCM
Word1[31:0] – Cortex-M7_2 ITCM 
read data[63:32]
Word2[31:0] – Cortex-M7_2 ITCM 
read data[31:0]
Word0[31:24] – Cortex-M7_2 
ITCM read data ECC[7:0]
64
8
11
Cortex-M7_2 
D0TCM
Word1[31:0] – Cortex-M7_2 
D0TCM read data[31:0]
Word0[31:24] – Cortex- M7_2 
D0TCM read data ECC[7:0]
32
8
12
Cortex-M7_2 
d1tcm
Word1[31:0] – Cortex-M7_2 
D1TCM read data[31:0]
Word0[31:24] – Cortex- M7_2 
D1TCM read data ECC[7:0]
32
8
13-31
Unused
Table 277. EIM_2 channel mapping - S32K358/S32K348/S32K338/S32K328
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
0
sram0
Word1[31:0] – SRAM0 read data[63:32]
Word2[31:0] – SRAM0 read data[31:0]
Word0[31:24] – SRAM0 
read data ECC[7:0]
64
8
1
sram1
Word1[31:0] – SRAM1 read data[63:32]
Word2[31:0] – SRAM1 read data[31:0]
Word0[31:24] – SRAM1 
read data ECC[7:0]
64
8
2
sram2
Word1[31:0] – SRAM2 read data[63:32]
Word2[31:0] – SRAM2 read data[31:0]
Word0[31:24] – SRAM1 
read data ECC[7:0]
64
8
3
DMA TCD
Word1[31:0] – DMA TCD RAM 
read data[63:32]
Word2[31:0] – DMA TCD RAM 
read data[31:0]
Word0[31:24] DMA 
TCD RAM read 
data checkbits[7:0]
64
8
4
Unused
5
GMAC gasket
Word1[27:0] – GMAC gasket monitor 
error injection[59:32]
Word2[31:0] – GMAC gasket monitor 
error injection[31:0]
-
60
0
6
CM7 TCM 
gasket1
Word1[27:0] – TCM AHB write data[63:36]
Word2[31:28] – TCM AHB write data[35:32]
-
188
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1937 / 5251


---
# 페이지 21

Table 277. EIM_2 channel mapping - S32K358/S32K348/S32K338/S32K328 (continued)
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
Word2[27:0] – TCM AHB write data[31:4]
Word3[31:28] – TCM AHB write data[3:0]
Word3[27:0] – TCM AHB read data[63:36]
Word4[31:28] – TCM AHB read data[35:32]
Word4[27:0] – TCM AHB read data[31:4]
Word5[31:28] – TCM AHB read data[3:0]
Word5[27:0] – TCM gasket monitor 
error injection[59:32]
Word6[31:0] – TCM gasket monitor 
error injection[31:0]
7
DMA AXBS S0 
gasket
Word1[27:0] – DMA AXBS S0 gasket 
monitor error injection[59:32]
Word2[31:0] – DMA AXBS S0 gasket 
monitor error injection[31:0]
-
60
0
8
DMA AXBS S1 
gasket
Word1[27:0] – DMA AXBS S1 gasket 
monitor error injection[59:32]
Word2[31:0] – DMA AXBS S1 gasket 
monitor error injection[31:0]
-
60
0
9
pram0_gasket
Word1[27:0] – PRAM0 gasket monitor 
error injection[59:32]
Word2[31:0] – PRAM0 gasket monitor 
error injection[31:0]
-
60
0
10
pram1_gasket
Word1[27:0] – PRAM1 gasket monitor 
error injection[59:32]
Word2[31:0] – PRAM1 gasket monitor 
error injection[31:0]
-
60
0
11
tcm_pram_gaske
t
Word1[27:0] – TCM_PRAM gasket monitor 
error injection[59:32]
Word2[31:0] – TCM_PRAM gasket monitor 
error injection[31:0]
-
60
0
12
Cortex-
M7_0_ahbs 
gasket
Word1[27:0] – Cortex-M7_0 AHBS 
write data[63:36]
Word2[31:28] – Cortex-M7_0 AHBS 
write data[35:32]
Word2[27:0] – Cortex-M7_0 AHBS 
write data[31:4]
-
188
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1938 / 5251


---
# 페이지 22

Table 277. EIM_2 channel mapping - S32K358/S32K348/S32K338/S32K328 (continued)
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
Word3[31:28] – Cortex-M7_0 AHBS 
write data[3:0]
Word3[27:0] – Cortex-M7_0 AHBS 
read data[63:36]
Word4[31:28] – Cortex-M7_0 AHBS 
read data[35:32]
Word4[27:0] – Cortex-M7_0 AHBS 
read data[31:4]
Word5[31:28] – Cortex-M7_0 AHBS 
read data[3:0]
Word5[27:0] – Cortex-M7_0 AHBS gasket 
monitor error injection[59:32]
Word6[31:0] – Cortex-M7_0 AHBS gasket 
monitor error injection[31:0]
13
cm7_1_ahbs 
gasket
Word1[27:0] – Cortex-M7_1 AHBS 
write data[63:36]
Word2[31:28] – Cortex-M7_1 AHBS 
write data[35:32]
Word2[27:0] – Cortex-M7_1 AHBS 
write data[31:4]
Word3[31:28] – Cortex-M7_1 AHBS 
write data[3:0]
Word3[27:0] – Cortex-M7_1 AHBS 
read data[63:36]
Word4[31:28] – Cortex-M7_1 AHBS 
read data[35:32]
Word4[27:0] – Cortex-M7_1 AHBS 
read data[31:4]
Word5[31:28] – Cortex-M7_0 AHBS 
read data[3:0]
Word5[27:0] – Cortex-M7_1 AHBS gasket 
monitor error injection[59:32]
Word6[31:0] – Cortex-M7_1 AHBS gasket 
monitor error injection[31:0]
-
188
0
14
Cortex-
M7_2_ahbs 
gasket
Word1[27:0] – Cortex-M7_2 AHBS 
write data[63:36]
Word2[31:28] – Cortex-M7_2 AHBS 
write data[35:32]
-
188
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1939 / 5251


---
# 페이지 23

Table 277. EIM_2 channel mapping - S32K358/S32K348/S32K338/S32K328 (continued)
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
Word2[27:0] – Cortex-M7_2 AHBS 
write data[31:4]
Word3[31:28] – Cortex-M7_2 AHBS 
write data[3:0]
Word3[27:0] – Cortex-M7_2 AHBS 
read data[63:36]
Word4[31:28] – Cortex-M7_2 AHBS 
read data[35:32]
Word4[27:0] – Cortex-M7_2 AHBS 
read data[31:4]
Word5[31:28] – Cortex-M7_2 AHBS 
read data[3:0]
Word5[27:0] – Cortex-M7_2 AHBS gasket 
monitor error injection[59:32]
Word6[31:0] – Cortex-M7_2 AHBS gasket 
monitor error injection[31:0]
15
pram2_gasket
Word1[27:0] – PRAM2 gasket monitor 
error injection[59:32]
Word2[31:0] – PRAM2 gasket monitor 
error injection[31:0]
-
60
0
Unused
17
hse gasket
Word1[27:0] – HSE gasket monitor 
error injection[59:32]
Word2[31:0] – HSE gasket monitor 
error injection[31:0]
-
60
0
18
QuadSPI gasket
Word1[27:0] – QuadSPI gasket monitor 
error injection[59:32]
Word2[31:0] – QuadSPI gasket monitor 
error injection[31:0]
-
60
0
19
AIPS1
Word1[27:0] – AIPS1 gasket monitor 
error injection[59:32]
Word2[31:0] – AIPS1 gasket monitor 
error injection[31:0]
-
60
0
20
AIPS2
Word1[27:0] – AIPS2 gasket monitor 
error injection[59:32]
Word2[31:0] – AIPS2 gasket monitor 
error injection[31:0]
-
60
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1940 / 5251


---
# 페이지 24

Table 277. EIM_2 channel mapping - S32K358/S32K348/S32K338/S32K328 (continued)
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
21
AIPS0
Word1[27:0] – AIPS0 gasket monitor 
error injection[59:32]
Word2[31:0] – AIPS0 gasket monitor 
error injection[31:0]
-
60
0
22
Unused
23
uSDHC gasket
Word1[27:0] – uSDHC write data[63:36]
Word2[31:28] – uSDHC write data[35:32]
Word2[27:0] – uSDHC write data[31:4]
Word3[31:28] – uSDHC write data[3:0]
Word3[27:0] – uSDHC read data[63:36]
Word4[31:28] – uSDHC read data[35:32]
Word4[27:0] – uSDHC read data[31:4]
Word5[31:28] – uSDHC read data[3:0]
Word5[27:0] – uSDHC gasket monitor 
error injection[59:32]
Word6[31:0] – Cortex-M7_0 uSDHC gasket 
monitor error injection[31:0]
-
188
0
24-25
Unused
25
Unused
26
edc1 gaskets 
addr
Word1[1:0] - Inject error on flash controller 
3 port address checker
Word1[3:2] - Inject error on 32 bit CM7_2 
TCM path address checker
Word1 [5:4] - Inject error on PRAM2 
address checker
-
6
0
27
edc1 gaskets 
wdata
Word1 [1:0] - Inject error on CM7_2 TCM 
path write data checker
Word1 [3:2] - Inject error on PRAM2 write 
data checker
-
4
0
28
edc1 gaskets 
rdata
Word1 [1:0] - Inject error on CM7_2 AHBM 
read data checker
Word1[3:2] - Inject error on CM7_2 AHBP 
read data checker
Word1[5:4] - Inject error on uSDHC read 
data checker
-
6
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1941 / 5251


---
# 페이지 25

Table 277. EIM_2 channel mapping - S32K358/S32K348/S32K338/S32K328 (continued)
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
29
EDC gaskets 
addr
Word1[1:0] – Inject error on flash memory 
controller port 0 address checker
Word1[3:2] – Inject error on flash memory 
controller port 1 address checker
Word1[4:4] – Inject error on flash memory 
controller port 2 address checker
Word1[7:6] – Inject error on PRAM0 
controller address checker
Word1[9:8] – Inject error on PRAM1 
controller address checker
Word1[11:10] – Inject error on 64-bit TCM 
bus address checker
Word1[13:12] – Inject error on QuadSPI 
path address checker
Word1[15:14] – Inject error on AIPS0 
address checker
Word1[17:16] – Inject error on AIPS1 
address checker
Word1[19:18] – Inject error on AIPS2 
address checker
Word1[21:20] – Inject error on 32-bit TCM 
Cortex-M7_0 path address checker
Word1[23:22] – Inject error on 32-bit TCM 
Cortex-M7_1 path address checker
Word1[25:24] – Inject error on DMA AXBS 
S0 address parity checker
Word1[27:26] – Inject error on DMA AXBS 
S1 address parity checker
-
28
0
30
EDC gaskets 
wdata
Word1[1:0] – Inject error on PRAM0 
controller write data checker
Word1[3:2] – Inject error on PRAM1 
controller write data checker
Word1[5:4] – Inject error on 64-bit TCM bus 
write data checker
Word1[7:6] – Reserved
Word1[9:8] – Inject error on AIPS0 write 
data checker
Word1[11:10] – Inject error on AIPS1 write 
data checker
-
18
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1942 / 5251


---
# 페이지 26

Table 277. EIM_2 channel mapping - S32K358/S32K348/S32K338/S32K328 (continued)
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
Word1[13:12] – Inject error on AIPS2 write 
data checker
Word1[15:14] – Inject error on 32-bit TCM 
Cortex-M7_0 path write data checker
Word1[17:16] – Inject error on 32-bit TCM 
Cortex-M7_1 path write data checker
31
EDC gaskets 
rdata
Word1[1:0] – Inject error on Cortex-M7_0 
AHBM read data checker
Word1[3:2] – Inject error
on Cortex-M7_0 AHBP read data checker
Word1[5:4] – Inject error on DMA read 
data checker
Word1[7:6] – Inject error on STAM read 
data checker
Word1[9:8] – Inject error on HSE read 
data checker
Word1[11:10] – Inject error on EMAC read 
data checker
Word1[13:12] – Inject error on Cortex-M7_1 
AHBM read data checker
Word1[15:14] – Inject error on Cortex-M7_1 
AHBP read data checker
Word1[17:16] – Inject error on 32-bit TCM 
bus path read data checker
-
18
0
1. This tcm gasket is not present for S32K358, S32K338, S32K388, and S32K389. Hence, the channel 6 for EIM_2 is 
unused.
Table 278. EIM_0 channel mapping - S32K388/S32K389
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
0
Cortex-M7_0 IC 
tag
Word1[12:0] – 
Cortex-M7_0 IC tag 
read data1[28:16]
Word2[31:22] – 
Cortex-M7_0 IC tag 
read data1[15:7]
Word2[21:0] – 
Cortex-M7_0 IC tag 
read data0[28:7]
Word0[31:25] – 
Cortex- M7_0 IC 
tag read data1[6:0]
Word0[24:18] – 
Cortex- M7_0 IC 
tag read data1[6:0]
44
14
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1943 / 5251


---
# 페이지 27

Table 278. EIM_0 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
1
Cortex-M7_0 IC 
data
Word1[31:0] – 
Cortex-M7_0 
IC data 
read data1[71:40]
Word2[31:0] – 
Cortex-M7_0 
IC data 
read data1[39:8]
Word3[31:0] – 
Cortex-M7_0 
IC data 
read data0[71:40]
Word4[31:0] – 
Cortex-M7_0 
IC data 
read data0[39:8]
Word0[31:24] – 
Cortex- M7_0 IC 
data data1[7:0]
Word0[23:16] 
– Cortex-M7_0 
IC data 
read data0[7:0]
128
16
2
Cortex-M7_0 DC 
tag
Word1[7:0] – 
Cortex-M7_0 
DC tag 
read data3[32:25]
Word2[31:14] 
– Cortex-M7_0 
DC tag 
read data3[24:7]
Word2[13:0] – 
Cortex-M7_0 
DC tag 
read data2[32:19]
Word3[31:20] 
– Cortex-M7_0 
DC tag 
read data2[18:7]
Word3[19:0] – 
Cortex-M7_0 
DC tag 
read data1[32:13]
Word4[31:26] 
– Cortex-M7_0 
DC tag 
read data1[12:7]
Word4[25:0] – 
Cortex-M7_0 
DC tag 
read data0[32:7]
Word0[31:25] – 
Cortex-M7_0 DC 
tag read data3[6:0]
Word0[24:18] – 
Cortex-M7_0 DC 
tag read data2[6:0]
Word0[17:11] – 
Cortex-M7_0 DC 
tag read data1[6:0]
Word0[10:4] – 
Cortex-M7_0 DC 
tag read data0[6:0]
104
28
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1944 / 5251


---
# 페이지 28

Table 278. EIM_0 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
3
Cortex-M7_0 DC 
data0
Word1[31:0] – 
Cortex-M7_0 
DC data0 
read data3[38:7]
Word2[31:0] – 
Cortex-M7_0 
DC data0 
read data2[38:7]
Word3[31:0] – 
Cortex-M7_0 
DC data0 
read data1[38:7]
Word4[31:0] – 
Cortex-M7_0 
DC data0 
read data0[38:7]
Word0[31:25] 
– Cortex-M7_0 
DC data0 
read data3[6:0]
Word0[24:18] 
– Cortex-M7_0 
DC data0 
read data2[6:0]
Word0[17:11] 
– Cortex-M7_0 
DC data0 
read data1[6:0]
Word0[10:4] – 
Cortex-M7_0 
DC data0 
read data0[6:0]
128
28
4
Cortex-M7_0 DC 
data1
Word1[31:0] – 
Cortex-M7_0 
DC data1 
read data3[38:7]
Word2[31:0] – 
Cortex-M7_0 
DC data1 
read data2[38:7]
Word3[31:0] – 
Cortex-M7_0 
DC data1 
read data1[38:7]
Word4[31:0] – 
Cortex-M7_0 
DC data1 
read data0[38:7]
Word0[31:25] 
– Cortex-M7_0 
DC data1 
read data3[6:0]
Word0[24:18] 
– Cortex-M7_0 
DC data1 
read data2[6:0]
Word0[17:11] 
– Cortex-M7_0 
DC data1 
read data1[6:0]
Word0[10:4] – 
Cortex-M7_0 
DC data1 
read data0[6:0]
128
28
5
Cortex-M7_1 IC 
tag
Word1[12:0] – 
Cortex-M7_1 IC tag 
read data1[28:16]
Word2[31:22] – 
Cortex-M7_1 IC tag 
read data1[15:7]
Word2[21:0] – 
Cortex-M7_1 IC tag 
read data0[28:7]
Word0[31:25] – 
Cortex- M7_1 IC 
tag read data1[6:0]
Word0[24:18] – 
Cortex- M7_1 IC 
tag read data1[6:0]
44
14
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1945 / 5251


---
# 페이지 29

Table 278. EIM_0 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
6
Cortex-M7_1 IC 
data
Word1[31:0] – 
Cortex-M7_1 
IC data 
read data1[71:40]
Word2[31:0] – 
Cortex-M7_1 
IC data 
read data1[39:8]
Word3[31:0] – 
Cortex-M7_1 
IC data 
read data0[71:40]
Word4[31:0] – 
Cortex-M7_1 
IC data 
read data0[39:8]
Word0[31:24] – 
Cortex- M7_1 IC 
data data1[7:0]
Word0[23:16] 
– Cortex-M7_1 
IC data 
read data0[7:0]
128
16
7
Cortex-M7_1 DC 
tag
Word1[7:0] – 
Cortex-M7_1 
DC tag 
read data3[32:25]
Word2[31:14] 
– Cortex-M7_1 
DC tag 
read data3[24:7]
Word2[13:0] – 
Cortex-M7_1 
DC tag 
read data2[32:19]
Word3[31:20] 
– Cortex-M7_1 
DC tag 
read data2[18:7]
Word3[19:0] – 
Cortex-M7_1 
DC tag 
read data1[32:13]
Word4[31:26] 
– Cortex-M7_1 
DC tag 
read data1[12:7]
Word4[25:0] – 
Cortex-M7_1 
DC tag 
read data0[32:7]
Word0[31:25] – 
Cortex-M7_1 DC 
tag read data3[6:0]
Word0[24:18] – 
Cortex-M7_1 DC 
tag read data2[6:0]
Word0[17:11] – 
Cortex-M7_1 DC 
tag read data1[6:0]
Word0[10:4] – 
Cortex-M7_1 DC 
tag read data0[6:0]
104
28
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1946 / 5251


---
# 페이지 30

Table 278. EIM_0 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
8
Cortex-M7_1 DC 
data0
Word1[31:0] – 
Cortex-M7_1 
DC data0 
read data3[38:7]
Word2[31:0] – 
Cortex-M7_1 
DC data0 
read data2[38:7]
Word3[31:0] – 
Cortex-M7_1 
DC data0 
read data1[38:7]
Word4[31:0] – 
Cortex-M7_1 
DC data0 
read data0[38:7]
Word0[31:25] 
– Cortex-M7_1 
DC data0 
read data3[6:0]
Word0[24:18] 
– Cortex-M7_1 
DC data0 
read data2[6:0]
Word0[17:11] 
– Cortex-M7_1 
DC data0 
read data1[6:0]
Word0[10:4] – 
Cortex-M7_1 
DC data0 
read data0[6:0]
128
28
9
Cortex-M7_1 DC 
data1
Word1[31:0] – 
Cortex-M7_1 
DC data1 
read data3[38:7]
Word2[31:0] – 
Cortex-M7_1 
DC data1 
read data2[38:7]
Word3[31:0] – 
Cortex-M7_1 
DC data1 
read data1[38:7]
Word4[31:0] – 
Cortex-M7_1 
DC data1 
read data0[38:7]
Word0[31:25] 
– Cortex-M7_1 
DC data1 
read data3[6:0]
Word0[24:18] 
– Cortex-M7_1 
DC data1 
read data2[6:0]
Word0[17:11] 
– Cortex-M7_1 
DC data1 
read data1[6:0]
Word0[10:4] – 
Cortex-M7_1 
DC data1 
read data0[6:0]
128
28
10
Cortex-M7_0 ITCM
Word1[31:0] – 
Cortex-M7_0 ITCM 
read data[63:32]
Word2[31:0] – 
Cortex-M7_0 ITCM 
read data[31:0]
Word0[31:24] – 
Cortex-M7_0 ITCM 
read data ECC[7:0]
64
8
11
Cortex-M7_0 
D0TCM
Word1[31:0] – 
Cortex-M7_0 
D0TCM read 
data[31:0]
Word0[31:24] – 
Cortex- M7_0 
D0TCM read data 
ECC[7:0]
32
8
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1947 / 5251


---
# 페이지 31

Table 278. EIM_0 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
12
Cortex-M7_0 
D1TCM
Word1[31:0] – 
Cortex-M7_0 
D1TCM read 
data[31:0]
Word0[31:24] – 
Cortex- M7_0 
D1TCM read data 
ECC[7:0]
32
8
13
Cortex-M7_1 ITCM
Word1[31:0] – 
Cortex-M7_1 ITCM 
read data[63:32]
Word2[31:0] – 
Cortex-M7_1 ITCM 
read data[31:0]
Word0[31:24] – 
Cortex-M7_1 ITCM 
read data ECC[7:0]
64
8
14
Cortex-M7_1 
D0TCM
Word1[31:0] – 
Cortex-M7_1 
D0TCM read 
data[31:0]
Word0[31:24] – 
Cortex- M7_0 
D0TCM read data 
ECC[7:0]
32
8
15
Cortex-M7_1 
D1TCM
Word1[31:0] – 
Cortex-M7_0 
D1TCM read 
data[31:0]
Word0[31:24] – 
Cortex- M7_0 
D1TCM read data 
ECC[7:0]
32
8
16
Cortex-M7 
lockstep
Word1[29:0] – 
Cortex-M7 error 
injection[29:0]
30
0
Table 279. EIM_1 channel mapping - S32K388/S32K389
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
0
Cortex-M7_2 IC 
tag
Word1[12:0] – 
Cortex-M7_2 IC tag 
read data1[28:16]
Word2[31:22] – 
Cortex-M7_2 IC tag 
read data1[15:7]
Word2[21:0] – 
Cortex-M7_2 IC tag 
read data0[28:7]
Word0[31:25] – 
Cortex- M7_2 IC 
tag read data1[6:0]
Word0[24:18] – 
Cortex- M7_2 IC 
tag read data1[6:0]
44
14
1
Cortex-M7_2 IC 
data
Word1[31:0] – 
Cortex-M7_2 
IC data 
read data1[71:40]
Word2[31:0] – 
Cortex-M7_2 
IC data 
read data1[39:8]
Word0[31:24] – 
Cortex- M7_2 IC 
data data1[7:0]
Word0[23:16] 
– Cortex-M7_2 
IC data 
read data0[7:0]
128
16
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1948 / 5251


---
# 페이지 32

Table 279. EIM_1 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
Word3[31:0] – 
Cortex-M7_2 
IC data 
read data0[71:40]
Word4[31:0] – 
Cortex-M7_2 
IC data 
read data0[39:8]
2
Cortex-M7_2 DC 
tag
Word1[7:0] – 
Cortex-M7_2 
DC tag 
read data3[32:25]
Word2[31:14] 
– Cortex-M7_2 
DC tag 
read data3[24:7]
Word2[13:0] – 
Cortex-M7_2 
DC tag 
read data2[32:19]
Word3[31:20] 
– Cortex-M7_2 
DC tag 
read data2[18:7]
Word3[19:0] – 
Cortex-M7_2 
DC tag 
read data1[32:13]
Word4[31:26] 
– Cortex-M7_2 
DC tag 
read data1[12:7]
Word4[25:0] – 
Cortex-M7_2 
DC tag 
read data0[32:7]
Word0[31:25] – 
Cortex-M7_2 DC 
tag read data3[6:0]
Word0[24:18] – 
Cortex-M7_2 DC 
tag read data2[6:0]
Word0[17:11] – 
Cortex-M7_2 DC 
tag read data1[6:0]
Word0[10:4] – 
Cortex-M7_2 DC 
tag read data0[6:0]
104
28
3
Cortex-M7_2 DC 
data0
Word1[31:0] – 
Cortex-M7_2 
DC data0 
read data3[38:7]
Word2[31:0] – 
Cortex-M7_2 
DC data0 
read data2[38:7]
Word0[31:25] 
– Cortex-M7_2 
DC data0 
read data3[6:0]
Word0[24:18] 
– Cortex-M7_2 
DC data0 
read data2[6:0]
128
28
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1949 / 5251


---
# 페이지 33

Table 279. EIM_1 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
Word3[31:0] – 
Cortex-M7_2 
DC data0 
read data1[38:7]
Word4[31:0] – 
Cortex-M7_2 
DC data0 
read data0[38:7]
Word0[17:11] 
– Cortex-M7_2 
DC data0 
read data1[6:0]
Word0[10:4] – 
Cortex-M7_2 
DC data0 
read data0[6:0]
4
Cortex-M7_2 DC 
data1
Word1[31:0] – 
Cortex-M7_2 
DC data1 
read data3[38:7]
Word2[31:0] – 
Cortex-M7_2 
DC data1 
read data2[38:7]
Word3[31:0] – 
Cortex-M7_2 
DC data1 
read data1[38:7]
Word4[31:0] – 
Cortex-M7_2 
DC data1 
read data0[38:7]
Word0[31:25] 
– Cortex-M7_2 
DC data1 
read data3[6:0]
Word0[24:18] 
– Cortex-M7_2 
DC data1 
read data2[6:0]
Word0[17:11] 
– Cortex-M7_2 
DC data1 
read data1[6:0]
Word0[10:4] – 
Cortex-M7_2 
DC data1 
read data0[6:0]
128
28
5
Cortex-M7_3 IC 
tag
Word1[12:0] – 
Cortex-M7_3 IC tag 
read data1[28:16]
Word2[31:22] – 
Cortex-M7_3 IC tag 
read data1[15:7]
Word2[21:0] – 
Cortex-M7_3 IC tag 
read data0[28:7]
Word0[31:25] – 
Cortex- M7_3 IC 
tag read data1[6:0]
Word0[24:18] – 
Cortex- M7_3 IC 
tag read data1[6:0]
44
14
6
Cortex-M7_3 IC 
data
Word1[31:0] – 
Cortex-M7_3 
IC data 
read data1[71:40]
Word2[31:0] – 
Cortex-M7_3 
IC data 
read data1[39:8]
Word3[31:0] – 
Cortex-M7_3 
Word0[31:24] – 
Cortex- M7_3 IC 
data data1[7:0]
Word0[23:16] 
– Cortex-M7_3 
IC data 
read data0[7:0]
128
16
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1950 / 5251


---
# 페이지 34

Table 279. EIM_1 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
IC data 
read data0[71:40]
Word4[31:0] – 
Cortex-M7_3 
IC data 
read data0[39:8]
7
Cortex-M7_3 DC 
tag
Word1[7:0] – 
Cortex-M7_3 
DC tag 
read data3[32:25]
Word2[31:14] 
– Cortex-M7_3 
DC tag 
read data3[24:7]
Word2[13:0] – 
Cortex-M7_3 
DC tag 
read data2[32:19]
Word3[31:20] 
– Cortex-M7_3 
DC tag 
read data2[18:7]
Word3[19:0] – 
Cortex-M7_3 
DC tag 
read data1[32:13]
Word4[31:26] 
– Cortex-M7_3 
DC tag 
read data1[12:7]
Word4[25:0] – 
Cortex-M7_3 
DC tag 
read data0[32:7]
Word0[31:25] – 
Cortex-M7_3 DC 
tag read data3[6:0]
Word0[24:18] – 
Cortex-M7_3 DC 
tag read data2[6:0]
Word0[17:11] – 
Cortex-M7_3 DC 
tag read data1[6:0]
Word0[10:4] – 
Cortex-M7_3 DC 
tag read data0[6:0]
104
28
8
Cortex-M7_3 DC 
data0
Word1[31:0] – 
Cortex-M7_3 
DC data0 
read data3[38:7]
Word2[31:0] – 
Cortex-M7_3 
DC data0 
read data2[38:7]
Word0[31:25] 
– Cortex-M7_3 
DC data0 
read data3[6:0]
Word0[24:18] 
– Cortex-M7_3 
DC data0 
read data2[6:0]
128
28
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1951 / 5251


---
# 페이지 35

Table 279. EIM_1 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
Word3[31:0] – 
Cortex-M7_3 
DC data0 
read data1[38:7]
Word4[31:0] – 
Cortex-M7_3 
DC data0 
read data0[38:7]
Word0[17:11] 
– Cortex-M7_3 
DC data0 
read data1[6:0]
Word0[10:4] – 
Cortex-M7_3 
DC data0 
read data0[6:0]
9
Cortex-M7_3 DC 
data1
Word1[31:0] – 
Cortex-M7_3 
DC data1 
read data3[38:7]
Word2[31:0] – 
Cortex-M7_3 
DC data1 
read data2[38:7]
Word3[31:0] – 
Cortex-M7_3 
DC data1 
read data1[38:7]
Word4[31:0] – 
Cortex-M7_3 
DC data1 
read data0[38:7]
Word0[31:25] 
– Cortex-M7_3 
DC data1 
read data3[6:0]
Word0[24:18] 
– Cortex-M7_3 
DC data1 
read data2[6:0]
Word0[17:11] 
– Cortex-M7_3 
DC data1 
read data1[6:0]
Word0[10:4] – 
Cortex-M7_3 
DC data1 
read data0[6:0]
128
28
10
Cortex-M7_2 ITCM
Word1[31:0] – 
Cortex-M7_2 ITCM 
read data[63:32]
Word2[31:0] – 
Cortex-M7_2 ITCM 
read data[31:0]
Word0[31:24] – 
Cortex-M7_1 ITCM 
read data ECC[7:0]
64
8
11
Cortex-M7_2 
D0TCM
Word1[31:0] – 
Cortex-M7_2 
D0TCM read 
data[31:0]
Word0[31:24] – 
Cortex- M7_2 
D0TCM read data 
ECC[7:0]
32
8
12
Cortex-M7_2 
D1TCM
Word1[31:0] – 
Cortex-M7_2 
D1TCM read 
data[31:0]
Word0[31:24] – 
Cortex- M7_2 
D1TCM read data 
ECC[7:0]
32
8
13
Cortex-M7_3 ITCM
Word1[31:0] – 
Cortex-M7_3 ITCM 
read data[63:32]
Word0[31:24] – 
Cortex-M7_3 ITCM 
read data ECC[7:0]
64
8
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1952 / 5251


---
# 페이지 36

Table 279. EIM_1 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
Word2[31:0] – 
Cortex-M7_3 ITCM 
read data[31:0]
14
Cortex-M7_3 
D0TCM
Word1[31:0] – 
Cortex-M7_3 
D0TCM read 
data[31:0]
Word0[31:24] – 
Cortex- M7_3 
D0TCM read data 
ECC[7:0]
32
8
15
Cortex-M7_3 
D1TCM
Word1[31:0] – 
Cortex-M7_0 
D1TCM read 
data[31:0]
Word0[31:24] – 
Cortex- M7_3 
D1TCM read data 
ECC[7:0]
32
8
16
Cortex-M7 
PLS_lockstep
Word1[29:0] 
– Cortex-M7 
PLS_error 
injection[29:0]
30
0
17-31
Unused
Table 280. EIM_2 channel mapping - S32K388/S32K389
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
0
SRAM0
Word1[31:0] 
– SRAM0 
read data[63:32]
Word2[31:0] 
– SRAM0 
read data[31:0]
Word0[31:24] – 
SRAM0 read 
data ECC[7:0]
64
8
1
SRAM1
Word1[31:0] 
– SRAM1 
read data[63:32]
Word2[31:0] 
– SRAM1 
read data[31:0]
Word0[31:24] – 
SRAM1 read 
data ECC[7:0]
64
8
2
SRAM2
Word1[31:0] 
– SRAM2 
read data[63:32]
Word2[31:0] 
– SRAM2 
read data[31:0]
Word0[31:24] – 
SRAM2 read 
data ECC[7:0]
64
8
3
DMA TCD
Word1[31:0] – 
DMA TCD RAM 
read data[63:32]
Word0[31:24] DMA 
TCD RAM read 
data checkbits[7:0]
64
8
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1953 / 5251


---
# 페이지 37

Table 280. EIM_2 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
Word2[31:0] – 
DMA TCD RAM 
read data[31:0]
4
GMAC_1 gasket
Word1[27:0] – 
GMAC_1 gasket 
monitor error 
injection[59:32]
Word2[31:0] 
– GMAC_1 
gasket monitor 
error injection[0:31]
60
0
5
GMAC gasket
Word1[27:0] – 
GMAC gasket 
monitor error 
injection[59:32]
Word2[31:0] 
– GMAC 
gasket monitor 
error injection[0:31]
60
0
6
Unused
7
DMA AXBS S0 
gasket
Word1[27:0] – DMA 
AXBS S0 gasket 
monitor error 
injection[59:32]
Word2[31:0] – 
DMA AXBS S0 
gasket monitor 
error injection[0:31]
60
0
8
DMA AXBS S1 
gasket
Word1[27:0] – DMA 
AXBS S1 gasket 
monitor error 
injection[59:32]
Word2[31:0] – 
DMA AXBS S1 
gasket monitor 
error injection[0:31]
60
0
9
Cortex-M7_3 
AHBP
Word1[27:0] – 
Cortex-M7_3 
AHBP gasket 
monitor error 
injection[59:32]
60
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1954 / 5251


---
# 페이지 38

Table 280. EIM_2 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
Word2[31:0] 
– Cortex-
M7_3 AHBP 
gasket monitor 
error injection[0:31]
10
Cortex-M7_3 
AHBM
Word1[27:0] – 
Cortex-M7_3 
AHBM gasket 
monitor error 
injection[59:32]
Word2[31:0] 
– Cortex-
M7_3 AHBM 
gasket monitor 
error injection[0:31]
60
0
11
Cortex-M7_0 
AHBP
Word1[27:0] – 
Cortex-M7_0 
AHBP gasket 
monitor error 
injection[59:32]
Word2[31:0] 
– Cortex-
M7_0 AHBP 
gasket monitor 
error injection[0:31]
60
0
12
Cortex-M7_0 
AHBM
Word1[27:0] – 
Cortex-M7_0 
AHBM gasket 
monitor error 
injection[59:32]
Word2[31:0] 
– Cortex-
M7_0 AHBM 
gasket monitor 
error injection[0:31]
60
0
13
Cortex-M7_1 
AHBP
Word1[27:0] – 
Cortex-M7_1 
AHBP gasket 
monitor error 
injection[59:32]
Word2[31:0] 
– Cortex-
M7_1 AHBP 
60
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1955 / 5251


---
# 페이지 39

Table 280. EIM_2 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
gasket monitor 
error injection[0:31]
14
Cortex-M7_1 
AHBM
Word1[27:0] – 
Cortex-M7_1 
AHBM gasket 
monitor error 
injection[59:32]
Word2[31:0] 
– Cortex-
M7_1 AHBM 
gasket monitor 
error injection[0:31]
60
0
15
Cortex-M7_2 
AHBP
Word1[27:0] – 
Cortex-M7_2 
AHBP gasket 
monitor error 
injection[59:32]
Word2[31:0] 
– Cortex-
M7_2 AHBP 
gasket monitor 
error injection[0:31]
60
0
16
Cortex-M7_2 
AHBM
Word1[27:0] – 
Cortex-M7_2 
AHBM gasket 
monitor error 
injection[59:32]
Word2[31:0] 
– Cortex-
M7_2 AHBM 
gasket monitor 
error injection[0:31]
60
0
17
HSE gasket
Word1[27:0] – HSE 
gasket monitor 
error 
injection[59:32]
Word2[31:0] – HSE 
gasket monitor 
error injection[0:31]
60
0
18
QuadSPI gasket
Word1[27:0] – 
QuadSPI gasket 
monitor error 
injection[59:32]
60
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1956 / 5251


---
# 페이지 40

Table 280. EIM_2 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
Word2[31:0] 
– QuadSPI 
gasket monitor 
error injection[0:31]
19
AIPS1
Word1[27:0] – 
AIPS1 gasket 
monitor error 
injection[59:32]
Word2[31:0] 
– AIPS1 
gasket monitor 
error injection[0:31]
60
0
20
AIPS2
Word1[27:0] – 
AIPS2 gasket 
monitor error 
injection[59:32]
Word2[31:0] 
– AIPS2 
gasket monitor 
error injection[0:31]
60
0
21
AIPS0
Word1[27:0] – 
AIPS0 gasket 
monitor error 
injection[59:32]
Word2[31:0] 
– AIPS0 
gasket monitor 
error injection[0:31]
60
0
22
Cortex-M7_0_ahbs 
gasket
Word1[27:0] 
– Cortex-
M7_0 AHBS 
write data[63:36]
Word2[31:28] 
– Cortex-
M7_0 AHBS 
write data[35:32]
Word2[27:0] 
– Cortex-
M7_0 AHBS 
write data[31:4]
Word3[31:28] 
– Cortex-
188
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1957 / 5251


---
# 페이지 41

Table 280. EIM_2 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
M7_0 AHBS 
write data[3:0]
Word3[27:0] 
– Cortex-
M7_0 AHBS 
read data[63:36]
Word4[31:28] 
– Cortex-
M7_0 AHBS 
read data[35:32]
Word4[27:0] 
– Cortex-
M7_0 AHBS 
read data[31:4]
Word5[31:28] 
– Cortex-
M7_0 AHBS 
read data[3:0]
Word5[27:0] – 
Cortex-M7_0 
AHBS gasket 
monitor error 
injection[59:32]
Word6[31:0] 
– Cortex-
M7_0 AHBS 
gasket monitor 
error injection[31:0]
23
Cortex-M7_1_ahbs 
gasket
Word1[27:0] 
– Cortex-
M7_1 AHBS 
write data[63:36]
Word2[31:28] 
– Cortex-
M7_1 AHBS 
write data[35:32]
Word2[27:0] 
– Cortex-
M7_1 AHBS 
write data[31:4]
Word3[31:28] 
– Cortex-
M7_1 AHBS 
write data[3:0]
188
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1958 / 5251


---
# 페이지 42

Table 280. EIM_2 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
Word3[27:0] 
– Cortex-
M7_1 AHBS 
read data[63:36]
Word4[31:28] 
– Cortex-
M7_1 AHBS 
read data[35:32]
Word4[27:0] 
– Cortex-
M7_1 AHBS 
read data[31:4]
Word5[31:28] 
– Cortex-
M7_1 AHBS 
read data[3:0]
Word5[27:0] – 
Cortex-M7_1 
AHBS gasket 
monitor error 
injection[59:32]
Word6[31:0] 
– Cortex-
M7_1 AHBS 
gasket monitor 
error injection[31:0]
24
Cortex-M7_2_ahbs 
gasket
Word1[27:0] 
– Cortex-
M7_2 AHBS 
write data[63:36]
Word2[31:28] 
– Cortex-
M7_2 AHBS 
write data[35:32]
Word2[27:0] 
– Cortex-
M7_2 AHBS 
write data[31:4]
Word3[31:28] 
– Cortex-
M7_2 AHBS 
write data[3:0]
Word3[27:0] 
– Cortex-
188
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1959 / 5251


---
# 페이지 43

Table 280. EIM_2 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
M7_2 AHBS 
read data[63:36]
Word4[31:28] 
– Cortex-
M7_2 AHBS 
read data[35:32]
Word4[27:0] 
– Cortex-
M7_2 AHBS 
read data[31:4]
Word5[31:28] 
– Cortex-
M7_2 AHBS 
read data[3:0]
Word5[27:0] – 
Cortex-M7_2 
AHBS gasket 
monitor error 
injection[59:32]
Word6[31:0] 
– Cortex-
M7_2 AHBS 
gasket monitor 
error injection[31:0]
25
Cortex-M7_3_ahbs 
gasket
Word1[27:0] 
– Cortex-
M7_3 AHBS 
write data[63:36]
Word2[31:28] 
– Cortex-
M7_3 AHBS 
write data[35:32]
Word2[27:0] 
– Cortex-
M7_3 AHBS 
write data[31:4]
Word3[31:28] 
– Cortex-
M7_3 AHBS 
write data[3:0]
Word3[27:0] 
– Cortex-
M7_3 AHBS 
read data[63:36]
188
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1960 / 5251


---
# 페이지 44

Table 280. EIM_2 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
Word4[31:28] 
– Cortex-
M7_3 AHBS 
read data[35:32]
Word4[27:0] 
– Cortex-
M7_3 AHBS 
read data[31:4]
Word5[31:28] 
– Cortex-
M7_3 AHBS 
read data[3:0]
Word5[27:0] – 
Cortex-M7_3 
AHBS gasket 
monitor error 
injection[59:32]
Word6[31:0] 
– Cortex-
M7_3 AHBS 
gasket monitor 
error injection[31:0]
26
edc1 gaskets addr
Word1 [1:0] -- 
Inject error on flash 
controller 3 port 
address checker
Word1 [3:2] -- Inject 
error on 32 bit 
CM7_2 TCM path 
address checker
Word1 [5:4] -- Inject 
error on PRAM2 
address checker
Word1 [7:6] Inject 
error on 32 bit 
CM7_3 TCM path 
address checker
8
0
27
edc1 gaskets 
wdata
Word1 [1:0] -- Inject 
error on CM7_2 
TCM path write 
data checker
Word1 [3:2] -- Inject 
error on PRAM2 
write data checker
6
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1961 / 5251


---
# 페이지 45

Table 280. EIM_2 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
Word1 [5:4] Inject 
error on CM7_3 
TCM path write 
data checker
28
edc1 gaskets rdata
Word1[1:0] -- 
Inject error on 
CM7_2 AHBM read 
data checker
Word1[3:2] -- 
Inject error on 
CM7_2 AHBP read 
data checker
Word1[5:4] -- Inject 
error on ENET1 
read data checker
Word1[7:6] Inject 
error on CM7_3 
AHBM read 
data checker
Word1[9:8] Inject 
error on CM7_3 
AHBP read 
data checker
Word1[11:10] Inject 
error on ace 
mstr result read 
data checker
Word1[13:12] Inject 
error on ace 
master feed read 
data checker
14
0
29
EDC gaskets addr
Word1[1:0] – Inject 
error on flash 
memory controller 
port 0 
address[59:0] – 
ace_gskt_slave_err
_inj59:0] checker
Word1[3:2] – 
Inject error on 
flash memory 
controller port 1 
address checker
28
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1962 / 5251


---
# 페이지 46

Table 280. EIM_2 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
Word1[4:4] – 
Inject error on 
flash memory 
controller port 2 
address checker
Word1[7:6] – 
Inject error on 
PRAM0 controller 
address checker
Word1[9:8] – 
Inject error on 
PRAM1 controller 
address checker
Word1[11:10] – 
Inject error on 
64-bit TCM bus 
address checker
Word1[13:12] – 
Inject error on 
QuadSPI path 
address checker
Word1[15:14] – 
Inject error 
on AIPS0 
address checker
Word1[17:16] – 
Inject error 
on AIPS1 
address checker
Word1[19:18] – 
Inject error 
on AIPS2 
address checker
Word1[21:20] – 
Inject error on 
32-bit TCM 
Cortex-M7_0 path 
address checker
Word1[23:22] – 
Inject error on 
32-bit TCM 
Cortex-M7_1 path 
address checker
Word1[25:24] – 
Inject error on DMA 
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1963 / 5251


---
# 페이지 47

Table 280. EIM_2 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
AXBS S0 address 
parity checker
Word1[27:26] – 
Inject error on DMA 
AXBS S1 address 
parity checker
30
EDC gaskets 
wdata
Word1[1:0] – Inject 
error on PRAM0 
controller write 
data checker
Word1[3:2] – Inject 
error on PRAM1 
controller write 
data checker
Word1[5:4] – Inject 
error on 64-bit 
TCM bus write 
data checker
Word1[7:6] 
– Reserved
Word1[9:8] – Inject 
error on AIPS0 
write data checker
Word1[11:10] – 
Inject error on 
AIPS1 write 
data checker
Word1[13:12] – 
Inject error on 
AIPS2 write 
data checker
Word1[15:14] – 
Inject error on 32-
bit TCM Cortex-
M7_0 path write 
data checker
Word1[17:16] – 
Inject error on 32-
bit TCM Cortex-
M7_1 path write 
data checker
18
0
31
EDC gaskets rdata
Word1[1:0] – Inject 
error on Cortex-
16
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1964 / 5251


---
# 페이지 48

Table 280. EIM_2 channel mapping - S32K388/S32K389 (continued)
Channel Number
Target
Data bits
Check bits
Num of data bits
Num of check bits
M7_0 AHBM read 
data checker
Word1[3:2] – Inject 
error on Cortex-
M7_0 AHBP read 
data checker
Word1[5:4] – Inject 
error on DMA read 
data checker
Word1[7:6] – Inject 
error on STAM read 
data checker
Word1[9:8] – Inject 
error on HSE read 
data checker
Word1[11:10] – 
Inject error on 
EMAC read 
data checker
Word1[13:12] – 
Inject error 
on Cortex-M7_1 
AHBM read 
data checker
Word1[15:14] – 
Inject error 
on Cortex-M7_1 
AHBP read 
data checker
Table 281. EIM_3 channel mapping - S32K388
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
0
ACE gasket 
slave
Word1[27:0] – ACE gasket slave monitor 
error injection[59:32]
Word2[31:0] – ACE gasket slave monitor 
error injection[0:31]
60
0
1
ACE gasket 
master
Word1[27:0] – ACE gasket master monitor 
error injection[59:32]
Word2[31:0] – ACE gasket master monitor 
error injection[0:31]
60
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1965 / 5251


---
# 페이지 49

Table 281. EIM_3 channel mapping - S32K388 (continued)
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
2
ACE DMA 32 
channel
Word1[31:0] – ACE FEED_DMA read 
data[63:32]
Word2[31:0] – ACE FEED_DMA 
read data[31:0]
Word0[31:24] – ACE 
FEED_DMA read data 
ECC[7:0]
64
8
3
ACE DMA 24 
channel
Word1[31:0] – ACE RESULT_DMA read 
data[63:32]
Word2[31:0] – ACE RESULT_DMA 
read data[31:0]
Word0[31:24] – ACE 
RESULT_DMA read 
data ECC[7:0]
64
8
4
TCM gasket
Word1[27:0] – TCM gasket monitor 
error injection[59:32]
Word2[31:0] – TCM gasket monitor 
error injection[0:31]
60
0
5-31
Unused
Table 282. EIM_3 channel mapping - S32K389
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
0
ACE gasket 
slave
Word1[27:0] – ACE gasket slave monitor 
error injection[59:32]
Word2[31:0] – ACE gasket slave monitor 
error injection[0:31]
60
0
1
ACE gasket 
master
Word1[27:0] – ACE gasket master monitor 
error injection[59:32]
Word2[31:0] – ACE gasket master monitor 
error injection[0:31]
60
0
2
ACE DMA 32 
channel
Word1[31:0] – ACE FEED_DMA read 
data[63:32]
Word2[31:0] – ACE FEED_DMA 
read data[31:0]
Word0[31:24] – ACE 
FEED_DMA read data 
ECC[7:0]
64
8
3
ACE DMA 24 
channel
Word1[31:0] – ACE RESULT_DMA read 
data[63:32]
Word2[31:0] – ACE RESULT_DMA 
read data[31:0]
Word0[31:24] – ACE 
RESULT_DMA read 
data ECC[7:0]
64
8
4
TCM gasket
Word1[27:0] – TCM gasket monitor 
error injection[59:32]
Word2[31:0] – TCM gasket monitor 
error injection[0:31]
60
0
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1966 / 5251


---
# 페이지 50

Table 282. EIM_3 channel mapping - S32K389 (continued)
Channel 
Number
Target
Data bits
Check bits
Num of 
data bits
Num of 
check bits
5
Reserved
This channel is reserved but it uses 60 bits 
of error injection bus
60
0
6
SRAM3
Word1[31:0] – SRAM3 read data[63:32]
Word2[31:0] – SRAM3 read data[31:0]
Word0[31:24] – 
SRAM3 read data 
ECC[7:0]
64
8
7
PFC0_0
Word1[31:0] – PFC0_0 error injection[31:0]
32
0
8
PFC0_1
Word1[31:0] – PFC0_1 error 
injection[31:0]
32
0
9
PFC1_0
Word1[31:0] – PFC1_0 error 
injection[31:0]
32
0
10
PFC1_1
Word1[31:0] – PFC1_1 error 
injection[31:0]
32
0
11-31
Unused
50.1.4 Behavior of EIM error injection on gaskets
The error injection on gaskets don't impact the actual data flow. The gasket read data, write data and the monitor error don't get 
changed when EIM error injection is done. The gasket compares the actual data with the modified data (with error injection) and 
flags the gasket alarm. In case of single-bit error also, the alarm is flagged.
 
The channels which depict such behavior are the gasket channels. See section "EIM channel mapping" in this 
chapter for details.
  NOTE  
50.1.5 Constraints to use EIM on CM7 cache memories
The Cortex-M7 processor has Error Correcting Code (ECC) functionality for error detection and correction that is included in the 
data and instruction caches when implemented. If hard, or permanent errors occur on the cache RAM, the clean, invalidate and 
retry scheme might cause a deadlock, and the access is continuously replayed. To prevent this, error bank registers are provided 
to mask the faulty locations as unusable and invalid. To ensure such a deadlock scenario does not occur while testing the cache 
memory using EIM module, you must take care of the following points:
• Inject one single-bit error on a cache line at a time.
• Ensure that at least one error bank register of the tested cache is free before injecting any faults. This is to make sure that 
the fault recovery mechanism of the Cortex-M7 core works.
See ‘Cache RAM protection’ section in the Arm Cortex-M7 Processor Technical Reference Manual for more details.
 
• For S32K338, S32K348, S32K328, S32K358, S32K388. and S32K389: Error injection on 0th and 1st bit for 
Icache and Dcache is invalid since the Icache and Dcache size is 16 KB.
• For remaining S32K3xx variant: Error injection on 0th bit for Icache and Dcache is invalid since the Icache and 
Dcache size is 8 KB.
  NOTE  
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1967 / 5251


---
# 페이지 51

50.2 Overview
The Error Injection Module (EIM) is mainly used for diagnostic purposes. It provides a method to test the diagnostics (memory 
ECC, interconnect parity) by error injection in the field. See the chip-specific EIM information to determine which functional safety 
features are supported by this method.
EIM enables you to inject artificial errors on error-checking mechanisms of a system, such as ECC for RAM read data and 
parity bits. For each such mechanism that EIM supports on the chip, EIM can inject single-bit and multi-bit inversions on data 
in the applicable target bus. Injecting faults on memory accesses can be used to exercise the SEC-DED ECC function of the 
related system.
 
Terminology in this chapter has been updated as follows:
Table 283. Updated terms
Updated term
Deprecated term
Controller
Master
  NOTE  
50.2.1 Features
The EIM includes these features:
• Supports 17 error injection channels. See the chip-specific EIM information for channel assignment details.
• Protection against accidental enable and reconfiguration error injection function via two-stage enable mechanism
50.2.2 Block diagram
The following diagram shows an example of EIM implementation with a 64-bit read data bus and an 8-bit checkbit bus.
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1968 / 5251


---
# 페이지 52

Module
rdata[63](MSB)
rdata[62]
rdata[61]
rdata[0](LSB)
chkbit[7]
chkbit[0]
EIM
EIMCR[GEIEN]
EICHEN[EICHnEN]
EICHDn_WORD0
EICHDn_WORD1
EICHDn_WORD2
   RAM 
   array     
Figure 207. EIM functional block diagram (64-bit read data bus and 8-bit check bit bus)
Several memory elements are implemented within a device, which may not only be the large memory blocks (Flash and SRAM) 
but also smaller memories like caches, the TCD blocks, and the embedded peripheral memories. Some larger memories may 
actually be built from multiple memory elements, dependent on their size or function. Each of these memory elements implements 
its own control logic, the memory controller, that performs the accesses to the actual memory, the memory array. An EIM channel 
is associated with a memory controller and provides the capability to alter one or multiple signals in the read access path from 
the corresponding memory array(s). Only memory controllers controlling a safety related memory may be associated with an 
EIM channel.
50.3 Functional description
The EIM provides protection against accidental enabling and reconfiguration of the error injection function by enforcing a 
two-stage enablement mechanism. To properly enable the error injection mechanism for a channel:
• Write 1 to the EICHEN[EICHnEN] field, where n denotes the channel number.
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1969 / 5251


---
# 페이지 53

• Write 1 to EIMCR[GEIEN].
 
When the use case for a channel requires writing any EICHDn_WORD register, write the EICHDn_WORD register 
before executing the two-stage enablement mechanism. A successful write to any EICHDn_WORD register clears 
the corresponding EICHEN[EICHnEN] field.
  NOTE  
The EIM supports 17 error injection channels. See the chip-specific EIM information for channel assignment details. Each channel:
• Can be assigned to a single memory array interface by intercepting the assigned memory read data bus and checkbit bus, 
and injects errors by inverting the value transmitted for selected bits on each bus line.
• Can be assigned to a redundant comparison unit by intercepting the signals being compared, and injecting errors by 
inverting the value transmitted for selected bits on each bus line.
On a memory read access, the applicable EICHDn_WORD registers define which bits of the read data and/or checkbit bus 
to invert.
Figure 207 depicts the interception and override of a 64-bit read data bus and an 8-bit checkbit data bus for an example 
memory array.
Error injection scenarios
The EIM supports these cases of error injection:
• To generate a single-bit error, invert only 1 bit of the CHKBIT_MASK or DATA_MASK in the EICHDn_WORD registers.
• To generate a multi-bit error, invert only 2 bits of the CHKBIT_MASK or DATA_MASK in the EICHDn_WORD registers.
 
An attempt to invert more than 2 bits in one operation might result in undefined behavior.
  NOTE  
To enable error injection:
1. Set the EICHDn_WORDm[CHKBIT_MASK] and EICHDn_WORDm[Ba_bDATA_MASK] fields for each channel that will be 
driving an injection.
2. Program the EICHEN register to enable the channels that will be injecting errors.
3. Set the EIMCR[GEIEN] field to globally allow all enabled channels to actively inject errors.
To disable error injection, either disable the EIMCR[GEIEN] field or disable the individual channel enable fields of the 
EICHEN register.
50.4 Initialization
This module does not require initialization.
50.6 EIM_0 register descriptions
The EIM provides a programming model mapped to an on-platform peripheral slot.
Programming model access
All system bus controllers can access the programming model:
• Only in supervisor mode
• Using only 32-bit (word) accesses
Any of the following attempted references to the programming model generates an error termination:
• In user mode
• Using non-32-bit access sizes
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1970 / 5251


---
# 페이지 54

• To undefined (reserved) addresses
Attempted updates to the programming model while the EIM is in the midst of an operation result in non-deterministic behavior.
Error injection channel descriptor: function and structure
Each error injection channel descriptor:
• Specifies a mask that defines which bits of the read data and/or checkbit bus from target RAM are inverted on a read 
access.
• Consists of a 288-bit (36-byte) structure, composed of nine 32-bit words, in the EIM programming model. Unused words 
are not documented.
— Word0 (EICHDn_WORD0), if present, defines the checkbit mask.
— Word1 (EICHDn_WORD1) and additional words, if present, define the data mask. Word registers subsequent to 
Word1 are present only when required by the total width of the channel's data mask. Error injection channel 
descriptor: DATA_MASK details.
The multiple channel descriptors are organized sequentially.
Error injection channel descriptor: DATA_MASK details
For each channel: The following tables show the distribution of DATA_MASK's bits across the WORD registers. The first table 
shows the total width of DATA_MASK and the distribution of its bits across WORD1, WORD2, and WORD3. The second table 
shows the distribution of DATA_MASK's bits across WORD4 and subsequent registers.
Table 284. Error injection channel descriptor: DATA_MASK details
Channel
DATA_MASK total 
width (bits)
Specific bits of DATA_MASK in
WORD1
WORD2
WORD3
0
44
43-32
31-0
—
1
128
127-96
95-64
63-32
2
104
103-96
95-64
63-32
3
128
127-96
95-64
63-32
4
128
127-96
95-64
63-32
5
44
43-32
31-0
—
6
128
127-96
95-64
63-32
7
104
103-96
95-64
63-32
8
128
127-96
95-64
63-32
9
128
127-96
95-64
63-32
10
64
63-32
31-0
—
11
32
31-0
—
—
12
32
31-0
—
—
13
64
63-32
31-0
—
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1971 / 5251


---
# 페이지 55

Table 284. Error injection channel descriptor: DATA_MASK details (continued)
Channel
DATA_MASK total 
width (bits)
Specific bits of DATA_MASK in
WORD1
WORD2
WORD3
14
32
31-0
—
—
15
32
31-0
—
—
16
30
29-0
—
—
Table 285. DATA_MASK bit: Channel-word mapping
Channel
Specific bits of DATA_MASK in
WORD4
WORD5
WORD6
WORD7
WORD8
1
31-0
—
—
—
—
2
31-0
—
—
—
—
3
31-0
—
—
—
—
4
31-0
—
—
—
—
6
31-0
—
—
—
—
7
31-0
—
—
—
—
8
31-0
—
—
—
—
9
31-0
—
—
—
—
50.6.1 EIM_0 memory map
EIM_0 base address: 4050_C000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Error Injection Module Configuration Register (EIMCR)
32
RW
0000_0000h
4h
Error Injection Channel Enable register (EICHEN)
32
RW
0000_0000h
100h
Error Injection Channel Descriptor 0, Word0 (EICHD0_WORD0)
32
RW
0000_0000h
104h
Error Injection Channel Descriptor 0, Word1 (EICHD0_WORD1)
32
RW
0000_0000h
108h
Error Injection Channel Descriptor 0, Word2 (EICHD0_WORD2)
32
RW
0000_0000h
140h
Error Injection Channel Descriptor 1, Word0 (EICHD1_WORD0)
32
RW
0000_0000h
144h
Error Injection Channel Descriptor 1, Word1 (EICHD1_WORD1)
32
RW
0000_0000h
148h
Error Injection Channel Descriptor 1, Word2 (EICHD1_WORD2)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1972 / 5251


---
# 페이지 56

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
14Ch
Error Injection Channel Descriptor 1, Word3 (EICHD1_WORD3)
32
RW
0000_0000h
150h
Error Injection Channel Descriptor 1, Word4 (EICHD1_WORD4)
32
RW
0000_0000h
180h
Error Injection Channel Descriptor 2, Word0 (EICHD2_WORD0)
32
RW
0000_0000h
184h
Error Injection Channel Descriptor 2, Word1 (EICHD2_WORD1)
32
RW
0000_0000h
188h
Error Injection Channel Descriptor 2, Word2 (EICHD2_WORD2)
32
RW
0000_0000h
18Ch
Error Injection Channel Descriptor 2, Word3 (EICHD2_WORD3)
32
RW
0000_0000h
190h
Error Injection Channel Descriptor 2, Word4 (EICHD2_WORD4)
32
RW
0000_0000h
1C0h
Error Injection Channel Descriptor 3, Word0 (EICHD3_WORD0)
32
RW
0000_0000h
1C4h
Error Injection Channel Descriptor 3, Word1 (EICHD3_WORD1)
32
RW
0000_0000h
1C8h
Error Injection Channel Descriptor 3, Word2 (EICHD3_WORD2)
32
RW
0000_0000h
1CCh
Error Injection Channel Descriptor 3, Word3 (EICHD3_WORD3)
32
RW
0000_0000h
1D0h
Error Injection Channel Descriptor 3, Word4 (EICHD3_WORD4)
32
RW
0000_0000h
200h
Error Injection Channel Descriptor 4, Word0 (EICHD4_WORD0)
32
RW
0000_0000h
204h
Error Injection Channel Descriptor 4, Word1 (EICHD4_WORD1)
32
RW
0000_0000h
208h
Error Injection Channel Descriptor 4, Word2 (EICHD4_WORD2)
32
RW
0000_0000h
20Ch
Error Injection Channel Descriptor 4, Word3 (EICHD4_WORD3)
32
RW
0000_0000h
210h
Error Injection Channel Descriptor 4, Word4 (EICHD4_WORD4)
32
RW
0000_0000h
240h
Error Injection Channel Descriptor 5, Word0 (EICHD5_WORD0)
32
RW
0000_0000h
244h
Error Injection Channel Descriptor 5, Word1 (EICHD5_WORD1)
32
RW
0000_0000h
248h
Error Injection Channel Descriptor 5, Word2 (EICHD5_WORD2)
32
RW
0000_0000h
280h
Error Injection Channel Descriptor 6, Word0 (EICHD6_WORD0)
32
RW
0000_0000h
284h
Error Injection Channel Descriptor 6, Word1 (EICHD6_WORD1)
32
RW
0000_0000h
288h
Error Injection Channel Descriptor 6, Word2 (EICHD6_WORD2)
32
RW
0000_0000h
28Ch
Error Injection Channel Descriptor 6, Word3 (EICHD6_WORD3)
32
RW
0000_0000h
290h
Error Injection Channel Descriptor 6, Word4 (EICHD6_WORD4)
32
RW
0000_0000h
2C0h
Error Injection Channel Descriptor 7, Word0 (EICHD7_WORD0)
32
RW
0000_0000h
2C4h
Error Injection Channel Descriptor 7, Word1 (EICHD7_WORD1)
32
RW
0000_0000h
2C8h
Error Injection Channel Descriptor 7, Word2 (EICHD7_WORD2)
32
RW
0000_0000h
2CCh
Error Injection Channel Descriptor 7, Word3 (EICHD7_WORD3)
32
RW
0000_0000h
2D0h
Error Injection Channel Descriptor 7, Word4 (EICHD7_WORD4)
32
RW
0000_0000h
300h
Error Injection Channel Descriptor 8, Word0 (EICHD8_WORD0)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1973 / 5251


---
# 페이지 57

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
304h
Error Injection Channel Descriptor 8, Word1 (EICHD8_WORD1)
32
RW
0000_0000h
308h
Error Injection Channel Descriptor 8, Word2 (EICHD8_WORD2)
32
RW
0000_0000h
30Ch
Error Injection Channel Descriptor 8, Word3 (EICHD8_WORD3)
32
RW
0000_0000h
310h
Error Injection Channel Descriptor 8, Word4 (EICHD8_WORD4)
32
RW
0000_0000h
340h
Error Injection Channel Descriptor 9, Word0 (EICHD9_WORD0)
32
RW
0000_0000h
344h
Error Injection Channel Descriptor 9, Word1 (EICHD9_WORD1)
32
RW
0000_0000h
348h
Error Injection Channel Descriptor 9, Word2 (EICHD9_WORD2)
32
RW
0000_0000h
34Ch
Error Injection Channel Descriptor 9, Word3 (EICHD9_WORD3)
32
RW
0000_0000h
350h
Error Injection Channel Descriptor 9, Word4 (EICHD9_WORD4)
32
RW
0000_0000h
380h
Error Injection Channel Descriptor 10, Word0 (EICHD10_WORD0)
32
RW
0000_0000h
384h
Error Injection Channel Descriptor 10, Word1 (EICHD10_WORD1)
32
RW
0000_0000h
388h
Error Injection Channel Descriptor 10, Word2 (EICHD10_WORD2)
32
RW
0000_0000h
3C0h
Error Injection Channel Descriptor 11, Word0 (EICHD11_WORD0)
32
RW
0000_0000h
3C4h
Error Injection Channel Descriptor 11, Word1 (EICHD11_WORD1)
32
RW
0000_0000h
400h
Error Injection Channel Descriptor 12, Word0 (EICHD12_WORD0)
32
RW
0000_0000h
404h
Error Injection Channel Descriptor 12, Word1 (EICHD12_WORD1)
32
RW
0000_0000h
440h
Error Injection Channel Descriptor 13, Word0 (EICHD13_WORD0)
32
RW
0000_0000h
444h
Error Injection Channel Descriptor 13, Word1 (EICHD13_WORD1)
32
RW
0000_0000h
448h
Error Injection Channel Descriptor 13, Word2 (EICHD13_WORD2)
32
RW
0000_0000h
480h
Error Injection Channel Descriptor 14, Word0 (EICHD14_WORD0)
32
RW
0000_0000h
484h
Error Injection Channel Descriptor 14, Word1 (EICHD14_WORD1)
32
RW
0000_0000h
4C0h
Error Injection Channel Descriptor 15, Word0 (EICHD15_WORD0)
32
RW
0000_0000h
4C4h
Error Injection Channel Descriptor 15, Word1 (EICHD15_WORD1)
32
RW
0000_0000h
504h
Error Injection Channel Descriptor 16, Word1 (EICHD16_WORD1)
32
RW
0000_0000h
50.6.2 Error Injection Module Configuration Register (EIMCR)
Offset
Register
Offset
EIMCR
0h
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1974 / 5251


---
# 페이지 58

Function
The EIM Configuration Register is used to globally enable/disable the error injection function.
Diagram
Bits
31
30
29
28
27
26
25
24
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
GEIEN 
W
Reset
0
0
0
0
0
0
0
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
0
GEIEN
Global Error Injection Enable
This bit globally enables or disables the error injection function of the EIM. This field is initialized by 
hardware reset.
0b - Disabled
1b - Enabled
50.6.3 Error Injection Channel Enable register (EICHEN)
Offset
Register
Offset
EICHEN
4h
Function
Each field of the Error Injection Channel Enable register (EICHEN) is used to enable or disable the corresponding error 
injection channel.
 
To enable an error injection channel, the Global Error Injection Enable (EIMCR[GEIEN]) field must also 
be asserted.
  NOTE  
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1975 / 5251


---
# 페이지 59

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
EICH0
EN 
EICH1
EN 
EICH2
EN 
EICH3
EN 
EICH4
EN 
EICH5
EN 
EICH6
EN 
EICH7
EN 
EICH8
EN 
EICH9
EN 
EICH1
0EN 
EICH1
1EN 
EICH1
2EN 
EICH1
3EN 
EICH1
4EN 
EICH1
5EN 
W
Reset
0
0
0
0
0
0
0
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
EICH1
6EN 
0
0
0
0
0
0
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
Fields
Field
Function
31
EICH0EN
Error Injection Channel 0 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 0
1b - Error injection is enabled on Error Injection Channel 0
30
EICH1EN
Error Injection Channel 1 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 1
1b - Error injection is enabled on Error Injection Channel 1
29
EICH2EN
Error Injection Channel 2 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1976 / 5251


---
# 페이지 60

Table continued from the previous page...
Field
Function
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 2
1b - Error injection is enabled on Error Injection Channel 2
28
EICH3EN
Error Injection Channel 3 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 3
1b - Error injection is enabled on Error Injection Channel 3
27
EICH4EN
Error Injection Channel 4 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 4
1b - Error injection is enabled on Error Injection Channel 4
26
EICH5EN
Error Injection Channel 5 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 5
1b - Error injection is enabled on Error Injection Channel 5
25
EICH6EN
Error Injection Channel 6 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1977 / 5251


---
# 페이지 61

Table continued from the previous page...
Field
Function
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 6
1b - Error injection is enabled on Error Injection Channel 6
24
EICH7EN
Error Injection Channel 7 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 7
1b - Error injection is enabled on Error Injection Channel 7
23
EICH8EN
Error Injection Channel 8 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 8
1b - Error injection is enabled on Error Injection Channel 8
22
EICH9EN
Error Injection Channel 9 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 9
1b - Error injection is enabled on Error Injection Channel 9
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1978 / 5251


---
# 페이지 62

Table continued from the previous page...
Field
Function
21
EICH10EN
Error Injection Channel 10 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 10
1b - Error injection is enabled on Error Injection Channel 10
20
EICH11EN
Error Injection Channel 11 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 11
1b - Error injection is enabled on Error Injection Channel 11
19
EICH12EN
Error Injection Channel 12 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 12
1b - Error injection is enabled on Error Injection Channel 12
18
EICH13EN
Error Injection Channel 13 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1979 / 5251


---
# 페이지 63

Table continued from the previous page...
Field
Function
0b - Error injection is disabled on Error Injection Channel 13
1b - Error injection is enabled on Error Injection Channel 13
17
EICH14EN
Error Injection Channel 14 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 14
1b - Error injection is enabled on Error Injection Channel 14
16
EICH15EN
Error Injection Channel 15 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 15
1b - Error injection is enabled on Error Injection Channel 15
15
EICH16EN
Error Injection Channel 16 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 16
1b - Error injection is enabled on Error Injection Channel 16
14
—
Reserved
13
—
Reserved
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1980 / 5251


---
# 페이지 64

Table continued from the previous page...
Field
Function
12
—
Reserved
11
—
Reserved
10
—
Reserved
9
—
Reserved
8
—
Reserved
7
—
Reserved
6
—
Reserved
5
—
Reserved
4
—
Reserved
3
—
Reserved
2
—
Reserved
1
—
Reserved
0
—
Reserved
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1981 / 5251


---
# 페이지 65

50.6.4 Error Injection Channel Descriptor 0, Word0 (EICHD0_WORD0)
Offset
Register
Offset
EICHD0_WORD0
100h
Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
CHKBIT_MASK 
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
31-18
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always 
in the position of the most significant bit. For CHKBIT_MASK[13:0] (14 bits wide), 
CHKBIT_MASK[13] is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
1b - The corresponding bit of the checkbit bus is inverted.
17-0
—
Reserved
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1982 / 5251


---
# 페이지 66

50.6.5 Error Injection Channel Descriptor 0, Word1 (EICHD0_WORD1)
Offset
Register
Offset
EICHD0_WORD1
104h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1983 / 5251


---
# 페이지 67

50.6.6 Error Injection Channel Descriptor n, Word2 (EICHD0_WORD2 - EICHD13_WORD2)
Offset
Register
Offset
EICHD0_WORD2
108h
EICHD1_WORD2
148h
EICHD2_WORD2
188h
EICHD3_WORD2
1C8h
EICHD4_WORD2
208h
EICHD5_WORD2
248h
EICHD6_WORD2
288h
EICHD7_WORD2
2C8h
EICHD8_WORD2
308h
EICHD9_WORD2
348h
EICHD10_WORD2
388h
EICHD13_WORD2
448h
Function
The third word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in 
B4_7DATA_MASK correspond to bytes 4–7 of the read data bus. Each bit specifies whether the corresponding bit of the read data 
bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field clears the 
corresponding error injection channel valid field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B4_7DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B4_7DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
Data Mask Bytes 4-7
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1984 / 5251


---
# 페이지 68

Field
Function
B4_7DATA_MA
SK
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified.
 
For each channel: For the specific DATA_MASK bits to which B4_7DATA_MASK 
corresponds, See Error injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 4-7 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 4-7 on the read data bus is inverted.
50.6.7 Error Injection Channel Descriptor 1, Word0 (EICHD1_WORD0)
Offset
Register
Offset
EICHD1_WORD0
140h
Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
CHKBIT_MASK 
W
Reset
0
0
0
0
0
0
0
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
31-16
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1985 / 5251


---
# 페이지 69

Table continued from the previous page...
Field
Function
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always 
in the position of the most significant bit. For CHKBIT_MASK[15:0] (16 bits wide), 
CHKBIT_MASK[15] is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
1b - The corresponding bit of the checkbit bus is inverted.
15-0
—
Reserved
50.6.8 Error Injection Channel Descriptor 1, Word1 (EICHD1_WORD1)
Offset
Register
Offset
EICHD1_WORD1
144h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1986 / 5251


---
# 페이지 70

Fields
Field
Function
31-0
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.6.9 Error Injection Channel Descriptor n, Word3 (EICHD1_WORD3 - EICHD9_WORD3)
Offset
Register
Offset
EICHD1_WORD3
14Ch
EICHD2_WORD3
18Ch
EICHD3_WORD3
1CCh
EICHD4_WORD3
20Ch
EICHD6_WORD3
28Ch
EICHD7_WORD3
2CCh
EICHD8_WORD3
30Ch
EICHD9_WORD3
34Ch
Function
The fourth word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in 
B8_11DATA_MASK correspond to bytes 8–11 of the read data bus. Each bit specifies whether the corresponding bit of the read 
data bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field clears 
the corresponding error injection channel valid field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1987 / 5251


---
# 페이지 71

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B8_11DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B8_11DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B8_11DATA_M
ASK
Data Mask Bytes 8-11
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified.
 
For each channel: For the specific DATA_MASK bits to which B8_11DATA_MASK 
corresponds, See Error injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 8-11 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 8-11 on the read data bus is inverted.
50.6.10 Error Injection Channel Descriptor n, Word4 (EICHD1_WORD4 - EICHD9_WORD4)
Offset
Register
Offset
EICHD1_WORD4
150h
EICHD2_WORD4
190h
EICHD3_WORD4
1D0h
EICHD4_WORD4
210h
EICHD6_WORD4
290h
EICHD7_WORD4
2D0h
EICHD8_WORD4
310h
EICHD9_WORD4
350h
Function
The fifth word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in 
B12_15DATA_MASK correspond to bytes 12–15 of the read data bus. Each bit specifies whether the corresponding bit of 
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1988 / 5251


---
# 페이지 72

the read data bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field 
clears the corresponding error injection channel valid field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B12_15DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B12_15DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B12_15DATA_
MASK
Data Mask Bytes 12-15
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified.
 
For each channel: For the specific DATA_MASK bits to which B12_15DATA_MASK 
corresponds, See Error injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 12-15 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 12-15 on the read data bus is inverted.
50.6.11 Error Injection Channel Descriptor n, Word0 (EICHD2_WORD0 - EICHD4_WORD0)
Offset
Register
Offset
EICHD2_WORD0
180h
EICHD3_WORD0
1C0h
EICHD4_WORD0
200h
Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1989 / 5251


---
# 페이지 73

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
CHKBIT_MASK 
W
Reset
0
0
0
0
0
0
0
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
CHKBIT_MASK 
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
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always 
in the position of the most significant bit. For CHKBIT_MASK[27:0] (28 bits wide), 
CHKBIT_MASK[27] is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
1b - The corresponding bit of the checkbit bus is inverted.
3-0
—
Reserved
50.6.12 Error Injection Channel Descriptor 2, Word1 (EICHD2_WORD1)
Offset
Register
Offset
EICHD2_WORD1
184h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1990 / 5251


---
# 페이지 74

Diagram
Bits
31
30
29
28
27
26
25
24
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.6.13 Error Injection Channel Descriptor n, Word1 (EICHD3_WORD1 - EICHD4_WORD1)
Offset
Register
Offset
EICHD3_WORD1
1C4h
EICHD4_WORD1
204h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1991 / 5251


---
# 페이지 75

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.6.14 Error Injection Channel Descriptor 5, Word0 (EICHD5_WORD0)
Offset
Register
Offset
EICHD5_WORD0
240h
Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1992 / 5251


---
# 페이지 76

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
CHKBIT_MASK 
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
31-18
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always 
in the position of the most significant bit. For CHKBIT_MASK[13:0] (14 bits wide), 
CHKBIT_MASK[13] is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
1b - The corresponding bit of the checkbit bus is inverted.
17-0
—
Reserved
50.6.15 Error Injection Channel Descriptor 5, Word1 (EICHD5_WORD1)
Offset
Register
Offset
EICHD5_WORD1
244h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1993 / 5251


---
# 페이지 77

Diagram
Bits
31
30
29
28
27
26
25
24
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.6.16 Error Injection Channel Descriptor 6, Word0 (EICHD6_WORD0)
Offset
Register
Offset
EICHD6_WORD0
280h
Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1994 / 5251


---
# 페이지 78

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
CHKBIT_MASK 
W
Reset
0
0
0
0
0
0
0
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
31-16
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always 
in the position of the most significant bit. For CHKBIT_MASK[15:0] (16 bits wide), 
CHKBIT_MASK[15] is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
1b - The corresponding bit of the checkbit bus is inverted.
15-0
—
Reserved
50.6.17 Error Injection Channel Descriptor 6, Word1 (EICHD6_WORD1)
Offset
Register
Offset
EICHD6_WORD1
284h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1995 / 5251


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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.6.18 Error Injection Channel Descriptor n, Word0 (EICHD7_WORD0 - EICHD9_WORD0)
Offset
Register
Offset
EICHD7_WORD0
2C0h
EICHD8_WORD0
300h
EICHD9_WORD0
340h
Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1996 / 5251


---
# 페이지 80

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
CHKBIT_MASK 
W
Reset
0
0
0
0
0
0
0
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
CHKBIT_MASK 
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
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always 
in the position of the most significant bit. For CHKBIT_MASK[27:0] (28 bits wide), 
CHKBIT_MASK[27] is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
1b - The corresponding bit of the checkbit bus is inverted.
3-0
—
Reserved
50.6.19 Error Injection Channel Descriptor 7, Word1 (EICHD7_WORD1)
Offset
Register
Offset
EICHD7_WORD1
2C4h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1997 / 5251


---
# 페이지 81

Diagram
Bits
31
30
29
28
27
26
25
24
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.6.20 Error Injection Channel Descriptor n, Word1 (EICHD8_WORD1 - EICHD15_WORD1)
Offset
Register
Offset
EICHD8_WORD1
304h
EICHD9_WORD1
344h
EICHD10_WORD1
384h
EICHD11_WORD1
3C4h
EICHD12_WORD1
404h
EICHD13_WORD1
444h
EICHD14_WORD1
484h
EICHD15_WORD1
4C4h
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1998 / 5251


---
# 페이지 82

Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.6.21 Error Injection Channel Descriptor n, Word0 (EICHD10_WORD0 - EICHD15_WORD0)
Offset
Register
Offset
EICHD10_WORD0
380h
EICHD11_WORD0
3C0h
EICHD12_WORD0
400h
EICHD13_WORD0
440h
EICHD14_WORD0
480h
EICHD15_WORD0
4C0h
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1999 / 5251


---
# 페이지 83

Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
CHKBIT_MASK 
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
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always in the 
position of the most significant bit. For CHKBIT_MASK[7:0] (8 bits wide), CHKBIT_MASK[7] 
is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
1b - The corresponding bit of the checkbit bus is inverted.
23-0
—
Reserved
50.6.22 Error Injection Channel Descriptor 16, Word1 (EICHD16_WORD1)
Offset
Register
Offset
EICHD16_WORD1
504h
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2000 / 5251


---
# 페이지 84

Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
29-0
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.7 EIM_1 register descriptions
The EIM provides a programming model mapped to an on-platform peripheral slot.
Programming model access
All system bus controllers can access the programming model:
• Only in supervisor mode
• Using only 32-bit (word) accesses
Any of the following attempted references to the programming model generates an error termination:
• In user mode
• Using non-32-bit access sizes
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2001 / 5251


---
# 페이지 85

• To undefined (reserved) addresses
Attempted updates to the programming model while the EIM is in the midst of an operation result in non-deterministic behavior.
Error injection channel descriptor: function and structure
Each error injection channel descriptor:
• Specifies a mask that defines which bits of the read data and/or checkbit bus from target RAM are inverted on a read 
access.
• Consists of a 288-bit (36-byte) structure, composed of nine 32-bit words, in the EIM programming model. Unused words 
are not documented.
— Word0 (EICHDn_WORD0), if present, defines the checkbit mask.
— Word1 (EICHDn_WORD1) and additional words, if present, define the data mask. Word registers subsequent to 
Word1 are present only when required by the total width of the channel's data mask. Error injection channel 
descriptor: DATA_MASK details.
The multiple channel descriptors are organized sequentially.
Error injection channel descriptor: DATA_MASK details
For each channel: The following tables show the distribution of DATA_MASK's bits across the WORD registers. The first table 
shows the total width of DATA_MASK and the distribution of its bits across WORD1, WORD2, and WORD3. The second table 
shows the distribution of DATA_MASK's bits across WORD4 and subsequent registers.
Table 286. Error injection channel descriptor: DATA_MASK details
Channel
DATA_MASK total 
width (bits)
Specific bits of DATA_MASK in
WORD1
WORD2
WORD3
0
44
43-32
31-0
—
1
128
127-96
95-64
63-32
2
104
103-96
95-64
63-32
3
128
127-96
95-64
63-32
4
128
127-96
95-64
63-32
5
44
43-32
31-0
—
6
128
127-96
95-64
63-32
7
104
103-96
95-64
63-32
8
128
127-96
95-64
63-32
9
128
127-96
95-64
63-32
10
64
63-32
31-0
—
11
32
31-0
—
—
12
32
31-0
—
—
13
64
63-32
31-0
—
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2002 / 5251


---
# 페이지 86

Table 286. Error injection channel descriptor: DATA_MASK details (continued)
Channel
DATA_MASK total 
width (bits)
Specific bits of DATA_MASK in
WORD1
WORD2
WORD3
14
32
31-0
—
—
15
32
31-0
—
—
16
30
29-0
—
—
Table 287. DATA_MASK bit: Channel-word mapping
Channel
Specific bits of DATA_MASK in
WORD4
WORD5
WORD6
WORD7
WORD8
1
31-0
—
—
—
—
2
31-0
—
—
—
—
3
31-0
—
—
—
—
4
31-0
—
—
—
—
6
31-0
—
—
—
—
7
31-0
—
—
—
—
8
31-0
—
—
—
—
9
31-0
—
—
—
—
50.7.1 EIM_1 memory map
EIM_1 base address: 4051_0000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Error Injection Module Configuration Register (EIMCR)
32
RW
0000_0000h
4h
Error Injection Channel Enable register (EICHEN)
32
RW
0000_0000h
100h
Error Injection Channel Descriptor 0, Word0 (EICHD0_WORD0)
32
RW
0000_0000h
104h
Error Injection Channel Descriptor 0, Word1 (EICHD0_WORD1)
32
RW
0000_0000h
108h
Error Injection Channel Descriptor 0, Word2 (EICHD0_WORD2)
32
RW
0000_0000h
140h
Error Injection Channel Descriptor 1, Word0 (EICHD1_WORD0)
32
RW
0000_0000h
144h
Error Injection Channel Descriptor 1, Word1 (EICHD1_WORD1)
32
RW
0000_0000h
148h
Error Injection Channel Descriptor 1, Word2 (EICHD1_WORD2)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2003 / 5251


---
# 페이지 87

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
14Ch
Error Injection Channel Descriptor 1, Word3 (EICHD1_WORD3)
32
RW
0000_0000h
150h
Error Injection Channel Descriptor 1, Word4 (EICHD1_WORD4)
32
RW
0000_0000h
180h
Error Injection Channel Descriptor 2, Word0 (EICHD2_WORD0)
32
RW
0000_0000h
184h
Error Injection Channel Descriptor 2, Word1 (EICHD2_WORD1)
32
RW
0000_0000h
188h
Error Injection Channel Descriptor 2, Word2 (EICHD2_WORD2)
32
RW
0000_0000h
18Ch
Error Injection Channel Descriptor 2, Word3 (EICHD2_WORD3)
32
RW
0000_0000h
190h
Error Injection Channel Descriptor 2, Word4 (EICHD2_WORD4)
32
RW
0000_0000h
1C0h
Error Injection Channel Descriptor 3, Word0 (EICHD3_WORD0)
32
RW
0000_0000h
1C4h
Error Injection Channel Descriptor 3, Word1 (EICHD3_WORD1)
32
RW
0000_0000h
1C8h
Error Injection Channel Descriptor 3, Word2 (EICHD3_WORD2)
32
RW
0000_0000h
1CCh
Error Injection Channel Descriptor 3, Word3 (EICHD3_WORD3)
32
RW
0000_0000h
1D0h
Error Injection Channel Descriptor 3, Word4 (EICHD3_WORD4)
32
RW
0000_0000h
200h
Error Injection Channel Descriptor 4, Word0 (EICHD4_WORD0)
32
RW
0000_0000h
204h
Error Injection Channel Descriptor 4, Word1 (EICHD4_WORD1)
32
RW
0000_0000h
208h
Error Injection Channel Descriptor 4, Word2 (EICHD4_WORD2)
32
RW
0000_0000h
20Ch
Error Injection Channel Descriptor 4, Word3 (EICHD4_WORD3)
32
RW
0000_0000h
210h
Error Injection Channel Descriptor 4, Word4 (EICHD4_WORD4)
32
RW
0000_0000h
240h
Error Injection Channel Descriptor 5, Word0 (EICHD5_WORD0)
32
RW
0000_0000h
244h
Error Injection Channel Descriptor 5, Word1 (EICHD5_WORD1)
32
RW
0000_0000h
248h
Error Injection Channel Descriptor 5, Word2 (EICHD5_WORD2)
32
RW
0000_0000h
280h
Error Injection Channel Descriptor 6, Word0 (EICHD6_WORD0)
32
RW
0000_0000h
284h
Error Injection Channel Descriptor 6, Word1 (EICHD6_WORD1)
32
RW
0000_0000h
288h
Error Injection Channel Descriptor 6, Word2 (EICHD6_WORD2)
32
RW
0000_0000h
28Ch
Error Injection Channel Descriptor 6, Word3 (EICHD6_WORD3)
32
RW
0000_0000h
290h
Error Injection Channel Descriptor 6, Word4 (EICHD6_WORD4)
32
RW
0000_0000h
2C0h
Error Injection Channel Descriptor 7, Word0 (EICHD7_WORD0)
32
RW
0000_0000h
2C4h
Error Injection Channel Descriptor 7, Word1 (EICHD7_WORD1)
32
RW
0000_0000h
2C8h
Error Injection Channel Descriptor 7, Word2 (EICHD7_WORD2)
32
RW
0000_0000h
2CCh
Error Injection Channel Descriptor 7, Word3 (EICHD7_WORD3)
32
RW
0000_0000h
2D0h
Error Injection Channel Descriptor 7, Word4 (EICHD7_WORD4)
32
RW
0000_0000h
300h
Error Injection Channel Descriptor 8, Word0 (EICHD8_WORD0)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2004 / 5251


---
# 페이지 88

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
304h
Error Injection Channel Descriptor 8, Word1 (EICHD8_WORD1)
32
RW
0000_0000h
308h
Error Injection Channel Descriptor 8, Word2 (EICHD8_WORD2)
32
RW
0000_0000h
30Ch
Error Injection Channel Descriptor 8, Word3 (EICHD8_WORD3)
32
RW
0000_0000h
310h
Error Injection Channel Descriptor 8, Word4 (EICHD8_WORD4)
32
RW
0000_0000h
340h
Error Injection Channel Descriptor 9, Word0 (EICHD9_WORD0)
32
RW
0000_0000h
344h
Error Injection Channel Descriptor 9, Word1 (EICHD9_WORD1)
32
RW
0000_0000h
348h
Error Injection Channel Descriptor 9, Word2 (EICHD9_WORD2)
32
RW
0000_0000h
34Ch
Error Injection Channel Descriptor 9, Word3 (EICHD9_WORD3)
32
RW
0000_0000h
350h
Error Injection Channel Descriptor 9, Word4 (EICHD9_WORD4)
32
RW
0000_0000h
380h
Error Injection Channel Descriptor 10, Word0 (EICHD10_WORD0)
32
RW
0000_0000h
384h
Error Injection Channel Descriptor 10, Word1 (EICHD10_WORD1)
32
RW
0000_0000h
388h
Error Injection Channel Descriptor 10, Word2 (EICHD10_WORD2)
32
RW
0000_0000h
3C0h
Error Injection Channel Descriptor 11, Word0 (EICHD11_WORD0)
32
RW
0000_0000h
3C4h
Error Injection Channel Descriptor 11, Word1 (EICHD11_WORD1)
32
RW
0000_0000h
400h
Error Injection Channel Descriptor 12, Word0 (EICHD12_WORD0)
32
RW
0000_0000h
404h
Error Injection Channel Descriptor 12, Word1 (EICHD12_WORD1)
32
RW
0000_0000h
440h
Error Injection Channel Descriptor 13, Word0 (EICHD13_WORD0)
32
RW
0000_0000h
444h
Error Injection Channel Descriptor 13, Word1 (EICHD13_WORD1)
32
RW
0000_0000h
448h
Error Injection Channel Descriptor 13, Word2 (EICHD13_WORD2)
32
RW
0000_0000h
480h
Error Injection Channel Descriptor 14, Word0 (EICHD14_WORD0)
32
RW
0000_0000h
484h
Error Injection Channel Descriptor 14, Word1 (EICHD14_WORD1)
32
RW
0000_0000h
4C0h
Error Injection Channel Descriptor 15, Word0 (EICHD15_WORD0)
32
RW
0000_0000h
4C4h
Error Injection Channel Descriptor 15, Word1 (EICHD15_WORD1)
32
RW
0000_0000h
504h
Error Injection Channel Descriptor 16, Word1 (EICHD16_WORD1)
32
RW
0000_0000h
50.7.2 Error Injection Module Configuration Register (EIMCR)
Offset
Register
Offset
EIMCR
0h
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2005 / 5251


---
# 페이지 89

Function
The EIM Configuration Register is used to globally enable/disable the error injection function.
Diagram
Bits
31
30
29
28
27
26
25
24
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
GEIEN 
W
Reset
0
0
0
0
0
0
0
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
0
GEIEN
Global Error Injection Enable
This bit globally enables or disables the error injection function of the EIM. This field is initialized by 
hardware reset.
0b - Disabled
1b - Enabled
50.7.3 Error Injection Channel Enable register (EICHEN)
Offset
Register
Offset
EICHEN
4h
Function
Each field of the Error Injection Channel Enable register (EICHEN) is used to enable or disable the corresponding error 
injection channel.
 
To enable an error injection channel, the Global Error Injection Enable (EIMCR[GEIEN]) field must also 
be asserted.
  NOTE  
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2006 / 5251


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
EICH0
EN 
EICH1
EN 
EICH2
EN 
EICH3
EN 
EICH4
EN 
EICH5
EN 
EICH6
EN 
EICH7
EN 
EICH8
EN 
EICH9
EN 
EICH1
0EN 
EICH1
1EN 
EICH1
2EN 
EICH1
3EN 
EICH1
4EN 
EICH1
5EN 
W
Reset
0
0
0
0
0
0
0
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
EICH1
6EN 
0
0
0
0
0
0
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
Fields
Field
Function
31
EICH0EN
Error Injection Channel 0 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 0
1b - Error injection is enabled on Error Injection Channel 0
30
EICH1EN
Error Injection Channel 1 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 1
1b - Error injection is enabled on Error Injection Channel 1
29
EICH2EN
Error Injection Channel 2 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2007 / 5251


---
# 페이지 91

Table continued from the previous page...
Field
Function
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 2
1b - Error injection is enabled on Error Injection Channel 2
28
EICH3EN
Error Injection Channel 3 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 3
1b - Error injection is enabled on Error Injection Channel 3
27
EICH4EN
Error Injection Channel 4 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 4
1b - Error injection is enabled on Error Injection Channel 4
26
EICH5EN
Error Injection Channel 5 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 5
1b - Error injection is enabled on Error Injection Channel 5
25
EICH6EN
Error Injection Channel 6 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2008 / 5251


---
# 페이지 92

Table continued from the previous page...
Field
Function
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 6
1b - Error injection is enabled on Error Injection Channel 6
24
EICH7EN
Error Injection Channel 7 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 7
1b - Error injection is enabled on Error Injection Channel 7
23
EICH8EN
Error Injection Channel 8 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 8
1b - Error injection is enabled on Error Injection Channel 8
22
EICH9EN
Error Injection Channel 9 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 9
1b - Error injection is enabled on Error Injection Channel 9
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2009 / 5251


---
# 페이지 93

Table continued from the previous page...
Field
Function
21
EICH10EN
Error Injection Channel 10 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 10
1b - Error injection is enabled on Error Injection Channel 10
20
EICH11EN
Error Injection Channel 11 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 11
1b - Error injection is enabled on Error Injection Channel 11
19
EICH12EN
Error Injection Channel 12 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 12
1b - Error injection is enabled on Error Injection Channel 12
18
EICH13EN
Error Injection Channel 13 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2010 / 5251


---
# 페이지 94

Table continued from the previous page...
Field
Function
0b - Error injection is disabled on Error Injection Channel 13
1b - Error injection is enabled on Error Injection Channel 13
17
EICH14EN
Error Injection Channel 14 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 14
1b - Error injection is enabled on Error Injection Channel 14
16
EICH15EN
Error Injection Channel 15 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 15
1b - Error injection is enabled on Error Injection Channel 15
15
EICH16EN
Error Injection Channel 16 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 16
1b - Error injection is enabled on Error Injection Channel 16
14
—
Reserved
13
—
Reserved
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2011 / 5251


---
# 페이지 95

Table continued from the previous page...
Field
Function
12
—
Reserved
11
—
Reserved
10
—
Reserved
9
—
Reserved
8
—
Reserved
7
—
Reserved
6
—
Reserved
5
—
Reserved
4
—
Reserved
3
—
Reserved
2
—
Reserved
1
—
Reserved
0
—
Reserved
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2012 / 5251


---
# 페이지 96

50.7.4 Error Injection Channel Descriptor 0, Word0 (EICHD0_WORD0)
Offset
Register
Offset
EICHD0_WORD0
100h
Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
CHKBIT_MASK 
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
31-18
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always 
in the position of the most significant bit. For CHKBIT_MASK[13:0] (14 bits wide), 
CHKBIT_MASK[13] is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
1b - The corresponding bit of the checkbit bus is inverted.
17-0
—
Reserved
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2013 / 5251


---
# 페이지 97

50.7.5 Error Injection Channel Descriptor 0, Word1 (EICHD0_WORD1)
Offset
Register
Offset
EICHD0_WORD1
104h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2014 / 5251


---
# 페이지 98

50.7.6 Error Injection Channel Descriptor n, Word2 (EICHD0_WORD2 - EICHD13_WORD2)
Offset
Register
Offset
EICHD0_WORD2
108h
EICHD1_WORD2
148h
EICHD2_WORD2
188h
EICHD3_WORD2
1C8h
EICHD4_WORD2
208h
EICHD5_WORD2
248h
EICHD6_WORD2
288h
EICHD7_WORD2
2C8h
EICHD8_WORD2
308h
EICHD9_WORD2
348h
EICHD10_WORD2
388h
EICHD13_WORD2
448h
Function
The third word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in 
B4_7DATA_MASK correspond to bytes 4–7 of the read data bus. Each bit specifies whether the corresponding bit of the read data 
bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field clears the 
corresponding error injection channel valid field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B4_7DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B4_7DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
Data Mask Bytes 4-7
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2015 / 5251


---
# 페이지 99

Field
Function
B4_7DATA_MA
SK
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified.
 
For each channel: For the specific DATA_MASK bits to which B4_7DATA_MASK 
corresponds, See Error injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 4-7 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 4-7 on the read data bus is inverted.
50.7.7 Error Injection Channel Descriptor 1, Word0 (EICHD1_WORD0)
Offset
Register
Offset
EICHD1_WORD0
140h
Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
CHKBIT_MASK 
W
Reset
0
0
0
0
0
0
0
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
31-16
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2016 / 5251


---
# 페이지 100

Table continued from the previous page...
Field
Function
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always 
in the position of the most significant bit. For CHKBIT_MASK[15:0] (16 bits wide), 
CHKBIT_MASK[15] is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
1b - The corresponding bit of the checkbit bus is inverted.
15-0
—
Reserved
50.7.8 Error Injection Channel Descriptor 1, Word1 (EICHD1_WORD1)
Offset
Register
Offset
EICHD1_WORD1
144h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2017 / 5251


---
# 페이지 101

Fields
Field
Function
31-0
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.7.9 Error Injection Channel Descriptor n, Word3 (EICHD1_WORD3 - EICHD9_WORD3)
Offset
Register
Offset
EICHD1_WORD3
14Ch
EICHD2_WORD3
18Ch
EICHD3_WORD3
1CCh
EICHD4_WORD3
20Ch
EICHD6_WORD3
28Ch
EICHD7_WORD3
2CCh
EICHD8_WORD3
30Ch
EICHD9_WORD3
34Ch
Function
The fourth word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in 
B8_11DATA_MASK correspond to bytes 8–11 of the read data bus. Each bit specifies whether the corresponding bit of the read 
data bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field clears 
the corresponding error injection channel valid field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2018 / 5251


---
# 페이지 102

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B8_11DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B8_11DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B8_11DATA_M
ASK
Data Mask Bytes 8-11
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified.
 
For each channel: For the specific DATA_MASK bits to which B8_11DATA_MASK 
corresponds, See Error injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 8-11 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 8-11 on the read data bus is inverted.
50.7.10 Error Injection Channel Descriptor n, Word4 (EICHD1_WORD4 - EICHD9_WORD4)
Offset
Register
Offset
EICHD1_WORD4
150h
EICHD2_WORD4
190h
EICHD3_WORD4
1D0h
EICHD4_WORD4
210h
EICHD6_WORD4
290h
EICHD7_WORD4
2D0h
EICHD8_WORD4
310h
EICHD9_WORD4
350h
Function
The fifth word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in 
B12_15DATA_MASK correspond to bytes 12–15 of the read data bus. Each bit specifies whether the corresponding bit of 
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2019 / 5251


---
# 페이지 103

the read data bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field 
clears the corresponding error injection channel valid field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B12_15DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B12_15DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B12_15DATA_
MASK
Data Mask Bytes 12-15
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified.
 
For each channel: For the specific DATA_MASK bits to which B12_15DATA_MASK 
corresponds, See Error injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 12-15 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 12-15 on the read data bus is inverted.
50.7.11 Error Injection Channel Descriptor n, Word0 (EICHD2_WORD0 - EICHD4_WORD0)
Offset
Register
Offset
EICHD2_WORD0
180h
EICHD3_WORD0
1C0h
EICHD4_WORD0
200h
Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2020 / 5251


---
# 페이지 104

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
CHKBIT_MASK 
W
Reset
0
0
0
0
0
0
0
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
CHKBIT_MASK 
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
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always 
in the position of the most significant bit. For CHKBIT_MASK[27:0] (28 bits wide), 
CHKBIT_MASK[27] is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
1b - The corresponding bit of the checkbit bus is inverted.
3-0
—
Reserved
50.7.12 Error Injection Channel Descriptor 2, Word1 (EICHD2_WORD1)
Offset
Register
Offset
EICHD2_WORD1
184h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2021 / 5251


---
# 페이지 105

Diagram
Bits
31
30
29
28
27
26
25
24
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.7.13 Error Injection Channel Descriptor n, Word1 (EICHD3_WORD1 - EICHD4_WORD1)
Offset
Register
Offset
EICHD3_WORD1
1C4h
EICHD4_WORD1
204h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2022 / 5251


---
# 페이지 106

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.7.14 Error Injection Channel Descriptor 5, Word0 (EICHD5_WORD0)
Offset
Register
Offset
EICHD5_WORD0
240h
Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2023 / 5251


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
CHKBIT_MASK 
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
31-18
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always 
in the position of the most significant bit. For CHKBIT_MASK[13:0] (14 bits wide), 
CHKBIT_MASK[13] is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
1b - The corresponding bit of the checkbit bus is inverted.
17-0
—
Reserved
50.7.15 Error Injection Channel Descriptor 5, Word1 (EICHD5_WORD1)
Offset
Register
Offset
EICHD5_WORD1
244h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2024 / 5251


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
0
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.7.16 Error Injection Channel Descriptor 6, Word0 (EICHD6_WORD0)
Offset
Register
Offset
EICHD6_WORD0
280h
Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2025 / 5251


---
# 페이지 109

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
CHKBIT_MASK 
W
Reset
0
0
0
0
0
0
0
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
31-16
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always 
in the position of the most significant bit. For CHKBIT_MASK[15:0] (16 bits wide), 
CHKBIT_MASK[15] is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
1b - The corresponding bit of the checkbit bus is inverted.
15-0
—
Reserved
50.7.17 Error Injection Channel Descriptor 6, Word1 (EICHD6_WORD1)
Offset
Register
Offset
EICHD6_WORD1
284h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2026 / 5251


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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.7.18 Error Injection Channel Descriptor n, Word0 (EICHD7_WORD0 - EICHD9_WORD0)
Offset
Register
Offset
EICHD7_WORD0
2C0h
EICHD8_WORD0
300h
EICHD9_WORD0
340h
Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2027 / 5251


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
CHKBIT_MASK 
W
Reset
0
0
0
0
0
0
0
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
CHKBIT_MASK 
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
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always 
in the position of the most significant bit. For CHKBIT_MASK[27:0] (28 bits wide), 
CHKBIT_MASK[27] is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
1b - The corresponding bit of the checkbit bus is inverted.
3-0
—
Reserved
50.7.19 Error Injection Channel Descriptor 7, Word1 (EICHD7_WORD1)
Offset
Register
Offset
EICHD7_WORD1
2C4h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2028 / 5251


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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.7.20 Error Injection Channel Descriptor n, Word1 (EICHD8_WORD1 - EICHD15_WORD1)
Offset
Register
Offset
EICHD8_WORD1
304h
EICHD9_WORD1
344h
EICHD10_WORD1
384h
EICHD11_WORD1
3C4h
EICHD12_WORD1
404h
EICHD13_WORD1
444h
EICHD14_WORD1
484h
EICHD15_WORD1
4C4h
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2029 / 5251


---
# 페이지 113

Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.7.21 Error Injection Channel Descriptor n, Word0 (EICHD10_WORD0 - EICHD15_WORD0)
Offset
Register
Offset
EICHD10_WORD0
380h
EICHD11_WORD0
3C0h
EICHD12_WORD0
400h
EICHD13_WORD0
440h
EICHD14_WORD0
480h
EICHD15_WORD0
4C0h
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2030 / 5251


---
# 페이지 114

Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
CHKBIT_MASK 
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
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always in the 
position of the most significant bit. For CHKBIT_MASK[7:0] (8 bits wide), CHKBIT_MASK[7] 
is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
1b - The corresponding bit of the checkbit bus is inverted.
23-0
—
Reserved
50.7.22 Error Injection Channel Descriptor 16, Word1 (EICHD16_WORD1)
Offset
Register
Offset
EICHD16_WORD1
504h
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2031 / 5251


---
# 페이지 115

Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
29-0
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.8 EIM_2 register descriptions
The EIM provides a programming model mapped to an on-platform peripheral slot.
Programming model access
All system bus controllers can access the programming model:
• Only in supervisor mode
• Using only 32-bit (word) accesses
Any of the following attempted references to the programming model generates an error termination:
• In user mode
• Using non-32-bit access sizes
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2032 / 5251


---
# 페이지 116

• To undefined (reserved) addresses
Attempted updates to the programming model while the EIM is in the midst of an operation result in non-deterministic behavior.
Error injection channel descriptor: function and structure
Each error injection channel descriptor:
• Specifies a mask that defines which bits of the read data and/or checkbit bus from target RAM are inverted on a read 
access.
• Consists of a 288-bit (36-byte) structure, composed of nine 32-bit words, in the EIM programming model. Unused words 
are not documented.
— Word0 (EICHDn_WORD0), if present, defines the checkbit mask.
— Word1 (EICHDn_WORD1) and additional words, if present, define the data mask. Word registers subsequent to 
Word1 are present only when required by the total width of the channel's data mask. Error injection channel 
descriptor: DATA_MASK details.
The multiple channel descriptors are organized sequentially.
Error injection channel descriptor: DATA_MASK details
For each channel: The following tables show the distribution of DATA_MASK's bits across the WORD registers. The first table 
shows the total width of DATA_MASK and the distribution of its bits across WORD1, WORD2, and WORD3. The second table 
shows the distribution of DATA_MASK's bits across WORD4 and subsequent registers.
Table 288. Error injection channel descriptor: DATA_MASK details
Channel
DATA_MASK total 
width (bits)
Specific bits of DATA_MASK in
WORD1
WORD2
WORD3
0
64
63-32
31-0
—
1
64
63-32
31-0
—
2
64
63-32
31-0
—
3
64
63-32
31-0
—
4
60
59-32
31-0
—
5
60
59-32
31-0
—
7
60
59-32
31-0
—
8
60
59-32
31-0
—
9
60
59-32
31-0
—
10
60
59-32
31-0
—
11
60
59-32
31-0
—
12
60
59-32
31-0
—
13
60
59-32
31-0
—
14
60
59-32
31-0
—
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2033 / 5251


---
# 페이지 117

Table 288. Error injection channel descriptor: DATA_MASK details (continued)
Channel
DATA_MASK total 
width (bits)
Specific bits of DATA_MASK in
WORD1
WORD2
WORD3
15
60
59-32
31-0
—
16
60
59-32
31-0
—
17
60
59-32
31-0
—
18
60
59-32
31-0
—
19
60
59-32
31-0
—
20
60
59-32
31-0
—
21
60
59-32
31-0
—
22
188
187-160
159-128
127-96
23
188
187-160
159-128
127-96
24
188
187-160
159-128
127-96
25
188
187-160
159-128
127-96
26
14
13-0
—
—
27
8
7-0
—
—
28
14
13-0
—
—
29
28
27-0
—
—
30
18
17-0
—
—
31
16
15-0
—
—
Table 289. DATA_MASK bit: Channel-word mapping
Channel
Specific bits of DATA_MASK in
WORD4
WORD5
WORD6
WORD7
WORD8
22
95-64
63-32
31-0
—
—
23
95-64
63-32
31-0
—
—
24
95-64
63-32
31-0
—
—
25
95-64
63-32
31-0
—
—
50.8.1 EIM_2 memory map
EIM_2 base address: 4051_4000h
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2034 / 5251


---
# 페이지 118

Offset
Register
Width
(In bits)
Access
Reset value
0h
Error Injection Module Configuration Register (EIMCR)
32
RW
0000_0000h
4h
Error Injection Channel Enable register (EICHEN)
32
RW
0000_0000h
100h
Error Injection Channel Descriptor 0, Word0 (EICHD0_WORD0)
32
RW
0000_0000h
104h
Error Injection Channel Descriptor 0, Word1 (EICHD0_WORD1)
32
RW
0000_0000h
108h
Error Injection Channel Descriptor 0, Word2 (EICHD0_WORD2)
32
RW
0000_0000h
140h
Error Injection Channel Descriptor 1, Word0 (EICHD1_WORD0)
32
RW
0000_0000h
144h
Error Injection Channel Descriptor 1, Word1 (EICHD1_WORD1)
32
RW
0000_0000h
148h
Error Injection Channel Descriptor 1, Word2 (EICHD1_WORD2)
32
RW
0000_0000h
180h
Error Injection Channel Descriptor 2, Word0 (EICHD2_WORD0)
32
RW
0000_0000h
184h
Error Injection Channel Descriptor 2, Word1 (EICHD2_WORD1)
32
RW
0000_0000h
188h
Error Injection Channel Descriptor 2, Word2 (EICHD2_WORD2)
32
RW
0000_0000h
1C0h
Error Injection Channel Descriptor 3, Word0 (EICHD3_WORD0)
32
RW
0000_0000h
1C4h
Error Injection Channel Descriptor 3, Word1 (EICHD3_WORD1)
32
RW
0000_0000h
1C8h
Error Injection Channel Descriptor 3, Word2 (EICHD3_WORD2)
32
RW
0000_0000h
204h
Error Injection Channel Descriptor 4, Word1 (EICHD4_WORD1)
32
RW
0000_0000h
208h
Error Injection Channel Descriptor 4, Word2 (EICHD4_WORD2)
32
RW
0000_0000h
244h
Error Injection Channel Descriptor 5, Word1 (EICHD5_WORD1)
32
RW
0000_0000h
248h
Error Injection Channel Descriptor 5, Word2 (EICHD5_WORD2)
32
RW
0000_0000h
2C4h
Error Injection Channel Descriptor 7, Word1 (EICHD7_WORD1)
32
RW
0000_0000h
2C8h
Error Injection Channel Descriptor 7, Word2 (EICHD7_WORD2)
32
RW
0000_0000h
304h
Error Injection Channel Descriptor 8, Word1 (EICHD8_WORD1)
32
RW
0000_0000h
308h
Error Injection Channel Descriptor 8, Word2 (EICHD8_WORD2)
32
RW
0000_0000h
344h
Error Injection Channel Descriptor 9, Word1 (EICHD9_WORD1)
32
RW
0000_0000h
348h
Error Injection Channel Descriptor 9, Word2 (EICHD9_WORD2)
32
RW
0000_0000h
384h
Error Injection Channel Descriptor 10, Word1 (EICHD10_WORD1)
32
RW
0000_0000h
388h
Error Injection Channel Descriptor 10, Word2 (EICHD10_WORD2)
32
RW
0000_0000h
3C4h
Error Injection Channel Descriptor 11, Word1 (EICHD11_WORD1)
32
RW
0000_0000h
3C8h
Error Injection Channel Descriptor 11, Word2 (EICHD11_WORD2)
32
RW
0000_0000h
404h
Error Injection Channel Descriptor 12, Word1 (EICHD12_WORD1)
32
RW
0000_0000h
408h
Error Injection Channel Descriptor 12, Word2 (EICHD12_WORD2)
32
RW
0000_0000h
444h
Error Injection Channel Descriptor 13, Word1 (EICHD13_WORD1)
32
RW
0000_0000h
448h
Error Injection Channel Descriptor 13, Word2 (EICHD13_WORD2)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2035 / 5251


---
# 페이지 119

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
484h
Error Injection Channel Descriptor 14, Word1 (EICHD14_WORD1)
32
RW
0000_0000h
488h
Error Injection Channel Descriptor 14, Word2 (EICHD14_WORD2)
32
RW
0000_0000h
4C4h
Error Injection Channel Descriptor 15, Word1 (EICHD15_WORD1)
32
RW
0000_0000h
4C8h
Error Injection Channel Descriptor 15, Word2 (EICHD15_WORD2)
32
RW
0000_0000h
504h
Error Injection Channel Descriptor 16, Word1 (EICHD16_WORD1)
32
RW
0000_0000h
508h
Error Injection Channel Descriptor 16, Word2 (EICHD16_WORD2)
32
RW
0000_0000h
544h
Error Injection Channel Descriptor 17, Word1 (EICHD17_WORD1)
32
RW
0000_0000h
548h
Error Injection Channel Descriptor 17, Word2 (EICHD17_WORD2)
32
RW
0000_0000h
584h
Error Injection Channel Descriptor 18, Word1 (EICHD18_WORD1)
32
RW
0000_0000h
588h
Error Injection Channel Descriptor 18, Word2 (EICHD18_WORD2)
32
RW
0000_0000h
5C4h
Error Injection Channel Descriptor 19, Word1 (EICHD19_WORD1)
32
RW
0000_0000h
5C8h
Error Injection Channel Descriptor 19, Word2 (EICHD19_WORD2)
32
RW
0000_0000h
604h
Error Injection Channel Descriptor 20, Word1 (EICHD20_WORD1)
32
RW
0000_0000h
608h
Error Injection Channel Descriptor 20, Word2 (EICHD20_WORD2)
32
RW
0000_0000h
644h
Error Injection Channel Descriptor 21, Word1 (EICHD21_WORD1)
32
RW
0000_0000h
648h
Error Injection Channel Descriptor 21, Word2 (EICHD21_WORD2)
32
RW
0000_0000h
684h
Error Injection Channel Descriptor 22, Word1 (EICHD22_WORD1)
32
RW
0000_0000h
688h
Error Injection Channel Descriptor 22, Word2 (EICHD22_WORD2)
32
RW
0000_0000h
68Ch
Error Injection Channel Descriptor 22, Word3 (EICHD22_WORD3)
32
RW
0000_0000h
690h
Error Injection Channel Descriptor 22, Word4 (EICHD22_WORD4)
32
RW
0000_0000h
694h
Error Injection Channel Descriptor 22, Word5 (EICHD22_WORD5)
32
RW
0000_0000h
698h
Error Injection Channel Descriptor 22, Word6 (EICHD22_WORD6)
32
RW
0000_0000h
6C4h
Error Injection Channel Descriptor 23, Word1 (EICHD23_WORD1)
32
RW
0000_0000h
6C8h
Error Injection Channel Descriptor 23, Word2 (EICHD23_WORD2)
32
RW
0000_0000h
6CCh
Error Injection Channel Descriptor 23, Word3 (EICHD23_WORD3)
32
RW
0000_0000h
6D0h
Error Injection Channel Descriptor 23, Word4 (EICHD23_WORD4)
32
RW
0000_0000h
6D4h
Error Injection Channel Descriptor 23, Word5 (EICHD23_WORD5)
32
RW
0000_0000h
6D8h
Error Injection Channel Descriptor 23, Word6 (EICHD23_WORD6)
32
RW
0000_0000h
704h
Error Injection Channel Descriptor 24, Word1 (EICHD24_WORD1)
32
RW
0000_0000h
708h
Error Injection Channel Descriptor 24, Word2 (EICHD24_WORD2)
32
RW
0000_0000h
70Ch
Error Injection Channel Descriptor 24, Word3 (EICHD24_WORD3)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2036 / 5251


---
# 페이지 120

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
710h
Error Injection Channel Descriptor 24, Word4 (EICHD24_WORD4)
32
RW
0000_0000h
714h
Error Injection Channel Descriptor 24, Word5 (EICHD24_WORD5)
32
RW
0000_0000h
718h
Error Injection Channel Descriptor 24, Word6 (EICHD24_WORD6)
32
RW
0000_0000h
744h
Error Injection Channel Descriptor 25, Word1 (EICHD25_WORD1)
32
RW
0000_0000h
748h
Error Injection Channel Descriptor 25, Word2 (EICHD25_WORD2)
32
RW
0000_0000h
74Ch
Error Injection Channel Descriptor 25, Word3 (EICHD25_WORD3)
32
RW
0000_0000h
750h
Error Injection Channel Descriptor 25, Word4 (EICHD25_WORD4)
32
RW
0000_0000h
754h
Error Injection Channel Descriptor 25, Word5 (EICHD25_WORD5)
32
RW
0000_0000h
758h
Error Injection Channel Descriptor 25, Word6 (EICHD25_WORD6)
32
RW
0000_0000h
784h
Error Injection Channel Descriptor 26, Word1 (EICHD26_WORD1)
32
RW
0000_0000h
7C4h
Error Injection Channel Descriptor 27, Word1 (EICHD27_WORD1)
32
RW
0000_0000h
804h
Error Injection Channel Descriptor 28, Word1 (EICHD28_WORD1)
32
RW
0000_0000h
844h
Error Injection Channel Descriptor 29, Word1 (EICHD29_WORD1)
32
RW
0000_0000h
884h
Error Injection Channel Descriptor 30, Word1 (EICHD30_WORD1)
32
RW
0000_0000h
8C4h
Error Injection Channel Descriptor 31, Word1 (EICHD31_WORD1)
32
RW
0000_0000h
50.8.2 Error Injection Module Configuration Register (EIMCR)
Offset
Register
Offset
EIMCR
0h
Function
The EIM Configuration Register is used to globally enable/disable the error injection function.
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2037 / 5251


---
# 페이지 121

Diagram
Bits
31
30
29
28
27
26
25
24
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
GEIEN 
W
Reset
0
0
0
0
0
0
0
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
0
GEIEN
Global Error Injection Enable
This bit globally enables or disables the error injection function of the EIM. This field is initialized by 
hardware reset.
0b - Disabled
1b - Enabled
50.8.3 Error Injection Channel Enable register (EICHEN)
Offset
Register
Offset
EICHEN
4h
Function
Each field of the Error Injection Channel Enable register (EICHEN) is used to enable or disable the corresponding error 
injection channel.
 
To enable an error injection channel, the Global Error Injection Enable (EIMCR[GEIEN]) field must also 
be asserted.
  NOTE  
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2038 / 5251


---
# 페이지 122

Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
EICH0
EN 
EICH1
EN 
EICH2
EN 
EICH3
EN 
EICH4
EN 
EICH5
EN 
0
EICH7
EN 
EICH8
EN 
EICH9
EN 
EICH1
0EN 
EICH1
1EN 
EICH1
2EN 
EICH1
3EN 
EICH1
4EN 
EICH1
5EN 
W
Reset
0
0
0
0
0
0
0
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
EICH1
6EN 
EICH1
7EN 
EICH1
8EN 
EICH1
9EN 
EICH2
0EN 
EICH2
1EN 
EICH2
2EN 
EICH2
3EN 
EICH2
4EN 
EICH2
5EN 
EICH2
6EN 
EICH2
7EN 
EICH2
8EN 
EICH2
9EN 
EICH3
0EN 
EICH3
1EN 
W
Reset
0
0
0
0
0
0
0
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
EICH0EN
Error Injection Channel 0 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 0
1b - Error injection is enabled on Error Injection Channel 0
30
EICH1EN
Error Injection Channel 1 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 1
1b - Error injection is enabled on Error Injection Channel 1
29
EICH2EN
Error Injection Channel 2 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2039 / 5251


---
# 페이지 123

Table continued from the previous page...
Field
Function
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 2
1b - Error injection is enabled on Error Injection Channel 2
28
EICH3EN
Error Injection Channel 3 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 3
1b - Error injection is enabled on Error Injection Channel 3
27
EICH4EN
Error Injection Channel 4 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 4
1b - Error injection is enabled on Error Injection Channel 4
26
EICH5EN
Error Injection Channel 5 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 5
1b - Error injection is enabled on Error Injection Channel 5
25
—
Reserved
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2040 / 5251


---
# 페이지 124

Table continued from the previous page...
Field
Function
24
EICH7EN
Error Injection Channel 7 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 7
1b - Error injection is enabled on Error Injection Channel 7
23
EICH8EN
Error Injection Channel 8 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 8
1b - Error injection is enabled on Error Injection Channel 8
22
EICH9EN
Error Injection Channel 9 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 9
1b - Error injection is enabled on Error Injection Channel 9
21
EICH10EN
Error Injection Channel 10 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2041 / 5251


---
# 페이지 125

Table continued from the previous page...
Field
Function
0b - Error injection is disabled on Error Injection Channel 10
1b - Error injection is enabled on Error Injection Channel 10
20
EICH11EN
Error Injection Channel 11 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 11
1b - Error injection is enabled on Error Injection Channel 11
19
EICH12EN
Error Injection Channel 12 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 12
1b - Error injection is enabled on Error Injection Channel 12
18
EICH13EN
Error Injection Channel 13 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 13
1b - Error injection is enabled on Error Injection Channel 13
17
EICH14EN
Error Injection Channel 14 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2042 / 5251


---
# 페이지 126

Table continued from the previous page...
Field
Function
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 14
1b - Error injection is enabled on Error Injection Channel 14
16
EICH15EN
Error Injection Channel 15 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 15
1b - Error injection is enabled on Error Injection Channel 15
15
EICH16EN
Error Injection Channel 16 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 16
1b - Error injection is enabled on Error Injection Channel 16
14
EICH17EN
Error Injection Channel 17 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 17
1b - Error injection is enabled on Error Injection Channel 17
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2043 / 5251


---
# 페이지 127

Table continued from the previous page...
Field
Function
13
EICH18EN
Error Injection Channel 18 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 18
1b - Error injection is enabled on Error Injection Channel 18
12
EICH19EN
Error Injection Channel 19 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 19
1b - Error injection is enabled on Error Injection Channel 19
11
EICH20EN
Error Injection Channel 20 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 20
1b - Error injection is enabled on Error Injection Channel 20
10
EICH21EN
Error Injection Channel 21 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2044 / 5251


---
# 페이지 128

Table continued from the previous page...
Field
Function
0b - Error injection is disabled on Error Injection Channel 21
1b - Error injection is enabled on Error Injection Channel 21
9
EICH22EN
Error Injection Channel 22 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 22
1b - Error injection is enabled on Error Injection Channel 22
8
EICH23EN
Error Injection Channel 23 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 23
1b - Error injection is enabled on Error Injection Channel 23
7
EICH24EN
Error Injection Channel 24 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 24
1b - Error injection is enabled on Error Injection Channel 24
6
EICH25EN
Error Injection Channel 25 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2045 / 5251


---
# 페이지 129

Table continued from the previous page...
Field
Function
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 25
1b - Error injection is enabled on Error Injection Channel 25
5
EICH26EN
Error Injection Channel 26 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 26
1b - Error injection is enabled on Error Injection Channel 26
4
EICH27EN
Error Injection Channel 27 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 27
1b - Error injection is enabled on Error Injection Channel 27
3
EICH28EN
Error Injection Channel 28 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 28
1b - Error injection is enabled on Error Injection Channel 28
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2046 / 5251


---
# 페이지 130

Table continued from the previous page...
Field
Function
2
EICH29EN
Error Injection Channel 29 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Optionally, a hardware error event from the logic being injected by this channel can also disable the injection 
if that feature is utilized at the instantiation of the EIM.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 29
1b - Error injection is enabled on Error Injection Channel 29
1
EICH30EN
Error Injection Channel 30 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Optionally, a hardware error event from the logic being injected by this channel can also disable the injection 
if that feature is utilized at the instantiation of the EIM.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 30
1b - Error injection is enabled on Error Injection Channel 30
0
EICH31EN
Error Injection Channel 31 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Optionally, a hardware error event from the logic being injected by this channel can also disable the injection 
if that feature is utilized at the instantiation of the EIM.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 31
1b - Error injection is enabled on Error Injection Channel 31
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2047 / 5251


---
# 페이지 131

50.8.4 Error Injection Channel Descriptor n, Word0 (EICHD0_WORD0 - EICHD3_WORD0)
Offset
Register
Offset
EICHD0_WORD0
100h
EICHD1_WORD0
140h
EICHD2_WORD0
180h
EICHD3_WORD0
1C0h
Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
CHKBIT_MASK 
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
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always in the 
position of the most significant bit. For CHKBIT_MASK[7:0] (8 bits wide), CHKBIT_MASK[7] 
is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2048 / 5251


---
# 페이지 132

Table continued from the previous page...
Field
Function
1b - The corresponding bit of the checkbit bus is inverted.
23-0
—
Reserved
50.8.5 Error Injection Channel Descriptor n, Word1 (EICHD0_WORD1 - EICHD3_WORD1)
Offset
Register
Offset
EICHD0_WORD1
104h
EICHD1_WORD1
144h
EICHD2_WORD1
184h
EICHD3_WORD1
1C4h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
Data Mask Bytes 0-3
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2049 / 5251


---
# 페이지 133

Field
Function
B0_3DATA_MA
SK
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.8.6 Error Injection Channel Descriptor n, Word2 (EICHD0_WORD2 - EICHD25_WORD2)
Offset
Register
Offset
EICHD0_WORD2
108h
EICHD1_WORD2
148h
EICHD2_WORD2
188h
EICHD3_WORD2
1C8h
EICHD4_WORD2
208h
EICHD5_WORD2
248h
EICHD7_WORD2
2C8h
EICHD8_WORD2
308h
EICHD9_WORD2
348h
EICHD10_WORD2
388h
EICHD11_WORD2
3C8h
EICHD12_WORD2
408h
EICHD13_WORD2
448h
EICHD14_WORD2
488h
EICHD15_WORD2
4C8h
EICHD16_WORD2
508h
EICHD17_WORD2
548h
EICHD18_WORD2
588h
EICHD19_WORD2
5C8h
EICHD20_WORD2
608h
EICHD21_WORD2
648h
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2050 / 5251


---
# 페이지 134

Table continued from the previous page...
Register
Offset
EICHD22_WORD2
688h
EICHD23_WORD2
6C8h
EICHD24_WORD2
708h
EICHD25_WORD2
748h
Function
The third word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in 
B4_7DATA_MASK correspond to bytes 4–7 of the read data bus. Each bit specifies whether the corresponding bit of the read data 
bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field clears the 
corresponding error injection channel valid field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B4_7DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B4_7DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B4_7DATA_MA
SK
Data Mask Bytes 4-7
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified.
 
For each channel: For the specific DATA_MASK bits to which B4_7DATA_MASK 
corresponds, See Error injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 4-7 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 4-7 on the read data bus is inverted.
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2051 / 5251


---
# 페이지 135

50.8.7 Error Injection Channel Descriptor n, Word1 (EICHD4_WORD1 - EICHD25_WORD1)
Offset
Register
Offset
EICHD4_WORD1
204h
EICHD5_WORD1
244h
EICHD7_WORD1
2C4h
EICHD8_WORD1
304h
EICHD9_WORD1
344h
EICHD10_WORD1
384h
EICHD11_WORD1
3C4h
EICHD12_WORD1
404h
EICHD13_WORD1
444h
EICHD14_WORD1
484h
EICHD15_WORD1
4C4h
EICHD16_WORD1
504h
EICHD17_WORD1
544h
EICHD18_WORD1
584h
EICHD19_WORD1
5C4h
EICHD20_WORD1
604h
EICHD21_WORD1
644h
EICHD22_WORD1
684h
EICHD23_WORD1
6C4h
EICHD24_WORD1
704h
EICHD25_WORD1
744h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2052 / 5251


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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
27-0
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.8.8 Error Injection Channel Descriptor n, Word3 (EICHD22_WORD3 - EICHD25_WORD3)
Offset
Register
Offset
EICHD22_WORD3
68Ch
EICHD23_WORD3
6CCh
EICHD24_WORD3
70Ch
EICHD25_WORD3
74Ch
Function
The fourth word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in 
B8_11DATA_MASK correspond to bytes 8–11 of the read data bus. Each bit specifies whether the corresponding bit of the read 
data bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field clears 
the corresponding error injection channel valid field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2053 / 5251


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
B8_11DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B8_11DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B8_11DATA_M
ASK
Data Mask Bytes 8-11
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified.
 
For each channel: For the specific DATA_MASK bits to which B8_11DATA_MASK 
corresponds, See Error injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 8-11 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 8-11 on the read data bus is inverted.
50.8.9 Error Injection Channel Descriptor n, Word4 (EICHD22_WORD4 - EICHD25_WORD4)
Offset
Register
Offset
EICHD22_WORD4
690h
EICHD23_WORD4
6D0h
EICHD24_WORD4
710h
EICHD25_WORD4
750h
Function
The fifth word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in 
B12_15DATA_MASK correspond to bytes 12–15 of the read data bus. Each bit specifies whether the corresponding bit of 
the read data bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field 
clears the corresponding error injection channel valid field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2054 / 5251


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
B12_15DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B12_15DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B12_15DATA_
MASK
Data Mask Bytes 12-15
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified.
 
For each channel: For the specific DATA_MASK bits to which B12_15DATA_MASK 
corresponds, See Error injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 12-15 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 12-15 on the read data bus is inverted.
50.8.10 Error Injection Channel Descriptor n, Word5 (EICHD22_WORD5 - EICHD25_WORD5)
Offset
Register
Offset
EICHD22_WORD5
694h
EICHD23_WORD5
6D4h
EICHD24_WORD5
714h
EICHD25_WORD5
754h
Function
The sixth word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in 
B16_19DATA_MASK correspond to bytes 16–19 of the read data bus. Each bit specifies whether the corresponding bit of the read 
data bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field clears 
the corresponding error injection channel valid field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2055 / 5251


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
B16_19DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B16_19DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B16_19DATA_
MASK
Data Mask Bytes 16-19
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified.
 
For each channel: For the specific DATA_MASK bits to which B16_19DATA_MASK 
corresponds, See Error injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 16-19 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 16-19 on the read data bus is inverted.
50.8.11 Error Injection Channel Descriptor n, Word6 (EICHD22_WORD6 - EICHD25_WORD6)
Offset
Register
Offset
EICHD22_WORD6
698h
EICHD23_WORD6
6D8h
EICHD24_WORD6
718h
EICHD25_WORD6
758h
Function
The seventh word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in 
B20_23DATA_MASK correspond to bytes 20–23 of the read data bus. Each bit specifies whether the corresponding bit of the read 
data bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field clears 
the corresponding error injection channel valid field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2056 / 5251


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
B20_23DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B20_23DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B20_23DATA_
MASK
Data Mask Bytes 20-23
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified.
 
For each channel: For the specific DATA_MASK bits to which B20_23DATA_MASK 
corresponds, See Error injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 20-23 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 20-23 on the read data bus is inverted.
50.8.12 Error Injection Channel Descriptor 26, Word1 (EICHD26_WORD1)
Offset
Register
Offset
EICHD26_WORD1
784h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2057 / 5251


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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
31-14
—
Reserved
13-0
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.8.13 Error Injection Channel Descriptor 27, Word1 (EICHD27_WORD1)
Offset
Register
Offset
EICHD27_WORD1
7C4h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2058 / 5251


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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.8.14 Error Injection Channel Descriptor 28, Word1 (EICHD28_WORD1)
Offset
Register
Offset
EICHD28_WORD1
804h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2059 / 5251


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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
31-14
—
Reserved
13-0
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.8.15 Error Injection Channel Descriptor 29, Word1 (EICHD29_WORD1)
Offset
Register
Offset
EICHD29_WORD1
844h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2060 / 5251


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
0
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
27-0
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.8.16 Error Injection Channel Descriptor 30, Word1 (EICHD30_WORD1)
Offset
Register
Offset
EICHD30_WORD1
884h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2061 / 5251


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
B0_3DATA_MA
SK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
31-18
—
Reserved
17-0
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.8.17 Error Injection Channel Descriptor 31, Word1 (EICHD31_WORD1)
Offset
Register
Offset
EICHD31_WORD1
8C4h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2062 / 5251


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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.9 EIM_3 register descriptions
The EIM provides a programming model mapped to an on-platform peripheral slot.
Programming model access
All system bus controllers can access the programming model:
• Only in supervisor mode
• Using only 32-bit (word) accesses
Any of the following attempted references to the programming model generates an error termination:
• In user mode
• Using non-32-bit access sizes
• To undefined (reserved) addresses
Attempted updates to the programming model while the EIM is in the midst of an operation result in non-deterministic behavior.
Error injection channel descriptor: function and structure
Each error injection channel descriptor:
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2063 / 5251


---
# 페이지 147

• Specifies a mask that defines which bits of the read data and/or checkbit bus from target RAM are inverted on a read 
access.
• Consists of a 128-bit (16-byte) structure, composed of four 32-bit words, in the EIM programming model. Unused words 
are not documented.
— Word0 (EICHDn_WORD0), if present, defines the checkbit mask.
— Word1-3 (EICHDn_WORD1-3), if present, define the data mask. Word2 and Word3 are present only when required 
by the total width of the channel's data mask. See Error injection channel descriptor: DATA_MASK details.
The multiple channel descriptors are organized sequentially.
Error injection channel descriptor: DATA_MASK details
For each channel: The following table shows the total width of DATA_MASK and the distribution of its bits across the 
WORD registers.
Table 290. Error injection channel descriptor: DATA_MASK details
Channel
DATA_MASK total 
width (bits)
Specific bits of DATA_MASK in
WORD1
WORD2
WORD3
0
60
59-32
31-0
—
1
60
59-32
31-0
—
2
64
63-32
31-0
—
3
64
63-32
31-0
—
4
60
59-32
31-0
—
5
60
59-32
31-0
—
6
64
63-32
31-0
—
7
32
31-0
—
—
8
32
31-0
—
—
9
32
31-0
—
—
10
32
31-0
—
—
50.9.1 EIM_3 memory map
EIM_3 base address: 4051_8000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Error Injection Module Configuration Register (EIMCR)
32
RW
0000_0000h
4h
Error Injection Channel Enable register (EICHEN)
32
RW
0000_0000h
104h
Error Injection Channel Descriptor 0, Word1 (EICHD0_WORD1)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2064 / 5251


---
# 페이지 148

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
108h
Error Injection Channel Descriptor 0, Word2 (EICHD0_WORD2)
32
RW
0000_0000h
144h
Error Injection Channel Descriptor 1, Word1 (EICHD1_WORD1)
32
RW
0000_0000h
148h
Error Injection Channel Descriptor 1, Word2 (EICHD1_WORD2)
32
RW
0000_0000h
180h
Error Injection Channel Descriptor 2, Word0 (EICHD2_WORD0)
32
RW
0000_0000h
184h
Error Injection Channel Descriptor 2, Word1 (EICHD2_WORD1)
32
RW
0000_0000h
188h
Error Injection Channel Descriptor 2, Word2 (EICHD2_WORD2)
32
RW
0000_0000h
1C0h
Error Injection Channel Descriptor 3, Word0 (EICHD3_WORD0)
32
RW
0000_0000h
1C4h
Error Injection Channel Descriptor 3, Word1 (EICHD3_WORD1)
32
RW
0000_0000h
1C8h
Error Injection Channel Descriptor 3, Word2 (EICHD3_WORD2)
32
RW
0000_0000h
204h
Error Injection Channel Descriptor 4, Word1 (EICHD4_WORD1)
32
RW
0000_0000h
208h
Error Injection Channel Descriptor 4, Word2 (EICHD4_WORD2)
32
RW
0000_0000h
244h
Error Injection Channel Descriptor 5, Word1 (EICHD5_WORD1)
32
RW
0000_0000h
248h
Error Injection Channel Descriptor 5, Word2 (EICHD5_WORD2)
32
RW
0000_0000h
280h
Error Injection Channel Descriptor 6, Word0 (EICHD6_WORD0)
32
RW
0000_0000h
284h
Error Injection Channel Descriptor 6, Word1 (EICHD6_WORD1)
32
RW
0000_0000h
288h
Error Injection Channel Descriptor 6, Word2 (EICHD6_WORD2)
32
RW
0000_0000h
2C4h
Error Injection Channel Descriptor 7, Word1 (EICHD7_WORD1)
32
RW
0000_0000h
304h
Error Injection Channel Descriptor 8, Word1 (EICHD8_WORD1)
32
RW
0000_0000h
344h
Error Injection Channel Descriptor 9, Word1 (EICHD9_WORD1)
32
RW
0000_0000h
384h
Error Injection Channel Descriptor 10, Word1 (EICHD10_WORD1)
32
RW
0000_0000h
50.9.2 Error Injection Module Configuration Register (EIMCR)
Offset
Register
Offset
EIMCR
0h
Function
The EIM Configuration Register is used to globally enable/disable the error injection function.
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2065 / 5251


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
GEIEN 
W
Reset
0
0
0
0
0
0
0
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
0
GEIEN
Global Error Injection Enable
This bit globally enables or disables the error injection function of the EIM. This field is initialized by 
hardware reset.
0b - Disabled
1b - Enabled
50.9.3 Error Injection Channel Enable register (EICHEN)
Offset
Register
Offset
EICHEN
4h
Function
Each field of the Error Injection Channel Enable register (EICHEN) is used to enable or disable the corresponding error 
injection channel.
 
To enable an error injection channel, the Global Error Injection Enable (EIMCR[GEIEN]) field must also 
be asserted.
  NOTE  
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2066 / 5251


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
EICH0
EN 
EICH1
EN 
EICH2
EN 
EICH3
EN 
EICH4
EN 
EICH5
EN 
EICH6
EN 
EICH7
EN 
EICH8
EN 
EICH9
EN 
EICH1
0EN 
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
31
EICH0EN
Error Injection Channel 0 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 0
1b - Error injection is enabled on Error Injection Channel 0
30
EICH1EN
Error Injection Channel 1 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 1
1b - Error injection is enabled on Error Injection Channel 1
29
EICH2EN
Error Injection Channel 2 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2067 / 5251


---
# 페이지 151

Table continued from the previous page...
Field
Function
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 2
1b - Error injection is enabled on Error Injection Channel 2
28
EICH3EN
Error Injection Channel 3 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 3
1b - Error injection is enabled on Error Injection Channel 3
27
EICH4EN
Error Injection Channel 4 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 4
1b - Error injection is enabled on Error Injection Channel 4
26
EICH5EN
Error Injection Channel 5 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 5
1b - Error injection is enabled on Error Injection Channel 5
25
EICH6EN
Error Injection Channel 6 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2068 / 5251


---
# 페이지 152

Table continued from the previous page...
Field
Function
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 6
1b - Error injection is enabled on Error Injection Channel 6
24
EICH7EN
Error Injection Channel 7 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 7
1b - Error injection is enabled on Error Injection Channel 7
23
EICH8EN
Error Injection Channel 8 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 8
1b - Error injection is enabled on Error Injection Channel 8
22
EICH9EN
Error Injection Channel 9 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 9
1b - Error injection is enabled on Error Injection Channel 9
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2069 / 5251


---
# 페이지 153

Table continued from the previous page...
Field
Function
21
EICH10EN
Error Injection Channel 10 Enable
This field enables the corresponding error injection channel. The Global Error Injection Enable 
(EIMCR[GEIEN]) field must also be asserted to enable error injection.
After error injection is enabled, all subsequent read accesses incur one or more bit inversions as defined 
in the corresponding EICHDn_WORD registers. Error injection remains in effect until the error injection 
channel is manually disabled via software.
Any write to the corresponding EICHDn_WORD registers clears the corresponding EICHEN[EICHnEN] 
field, disabling the error injection channel.
0b - Error injection is disabled on Error Injection Channel 10
1b - Error injection is enabled on Error Injection Channel 10
20
—
Reserved
19
—
Reserved
18
—
Reserved
17
—
Reserved
16
—
Reserved
15
—
Reserved
14
—
Reserved
13
—
Reserved
12
—
Reserved
11
—
Reserved
10
Reserved
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2070 / 5251


---
# 페이지 154

Table continued from the previous page...
Field
Function
—
9
—
Reserved
8
—
Reserved
7
—
Reserved
6
—
Reserved
5
—
Reserved
4
—
Reserved
3
—
Reserved
2
—
Reserved
1
—
Reserved
0
—
Reserved
50.9.4 Error Injection Channel Descriptor n, Word1 (EICHD0_WORD1 - EICHD1_WORD1)
Offset
Register
Offset
EICHD0_WORD1
104h
EICHD1_WORD1
144h
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2071 / 5251


---
# 페이지 155

Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
27-0
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.9.5 Error Injection Channel Descriptor n, Word2 (EICHD0_WORD2 - EICHD6_WORD2)
Offset
Register
Offset
EICHD0_WORD2
108h
EICHD1_WORD2
148h
EICHD2_WORD2
188h
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2072 / 5251


---
# 페이지 156

Table continued from the previous page...
Register
Offset
EICHD3_WORD2
1C8h
EICHD4_WORD2
208h
EICHD5_WORD2
248h
EICHD6_WORD2
288h
Function
The third word of the Error Injection Channel Descriptor, when present, defines a right-justified mask field. The bits in 
B4_7DATA_MASK correspond to bytes 4–7 of the read data bus. Each bit specifies whether the corresponding bit of the read data 
bus from the target RAM should be inverted or remain unmodified on read accesses. A successful write to this field clears the 
corresponding error injection channel valid field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B4_7DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B4_7DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B4_7DATA_MA
SK
Data Mask Bytes 4-7
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified.
 
For each channel: For the specific DATA_MASK bits to which B4_7DATA_MASK 
corresponds, See Error injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 4-7 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 4-7 on the read data bus is inverted.
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2073 / 5251


---
# 페이지 157

50.9.6 Error Injection Channel Descriptor n, Word0 (EICHD2_WORD0 - EICHD6_WORD0)
Offset
Register
Offset
EICHD2_WORD0
180h
EICHD3_WORD0
1C0h
EICHD6_WORD0
280h
Function
The first word of the Error Injection Channel Descriptor defines a left-justified mask field: CHKBIT_MASK. Each bit of 
CHKBIT_MASK specifies whether the corresponding bit of the checkbit bus from the target RAM should be inverted or 
remain unmodified on read accesses. Successful write to this field clears the corresponding error injection channel valid 
bit, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
CHKBIT_MASK 
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
CHKBIT_MASK
Checkbit Mask
This field defines a bit-mapped mask that specifies whether the corresponding bit of the checkbit bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
For any unique details about the mapping of CHKBIT_MASK's bits to a channel's target RAM, see the 
chip-specific EIM information.
 
Because CHKBIT_MASK is left-justified, the highest bit in the bit range is always in the 
position of the most significant bit. For CHKBIT_MASK[7:0] (8 bits wide), CHKBIT_MASK[7] 
is in the position of the most significant bit.
  NOTE  
0b - The corresponding bit of the checkbit bus remains unmodified.
1b - The corresponding bit of the checkbit bus is inverted.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2074 / 5251


---
# 페이지 158

Table continued from the previous page...
Field
Function
23-0
—
Reserved
50.9.7 Error Injection Channel Descriptor n, Word1 (EICHD2_WORD1 - EICHD3_WORD1)
Offset
Register
Offset
EICHD2_WORD1
184h
EICHD3_WORD1
1C4h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2075 / 5251


---
# 페이지 159

Field
Function
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.9.8 Error Injection Channel Descriptor n, Word1 (EICHD4_WORD1 - EICHD5_WORD1)
Offset
Register
Offset
EICHD4_WORD1
204h
EICHD5_WORD1
244h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
27-0
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
Table continues on the next page...
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2076 / 5251


---
# 페이지 160

Table continued from the previous page...
Field
Function
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.9.9 Error Injection Channel Descriptor n, Word1 (EICHD6_WORD1 - EICHD10_WORD1)
Offset
Register
Offset
EICHD6_WORD1
284h
EICHD7_WORD1
2C4h
EICHD8_WORD1
304h
EICHD9_WORD1
344h
EICHD10_WORD1
384h
Function
The second word of the Error Injection Channel Descriptor defines a right-justified mask field. The bits in B0_3DATA_MASK 
correspond to bytes 0–3 of the target bus. Each bit specifies whether the corresponding bit of the target bus should be inverted 
or remain unmodified on read accesses. A successful write to this field clears the corresponding error injection channel valid 
field, EICHEN[EICHnEN].
Diagram
Bits
31
30
29
28
27
26
25
24
23
22
21
20
19
18
17
16
R
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
B0_3DATA_MASK 
W
Reset
0
0
0
0
0
0
0
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
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2077 / 5251


---
# 페이지 161

Fields
Field
Function
31-0
B0_3DATA_MA
SK
Data Mask Bytes 0-3
This field defines a bit-mapped mask that specifies whether the corresponding bit of the read data bus from 
the target RAM should be inverted or remain unmodified. Writes to unimplemented bits are ignored.
 
For the specific DATA_MASK bits to which B0_3DATA_MASK corresponds, See Error 
injection channel descriptor: DATA_MASK details.
  NOTE  
0b - The corresponding bit of bytes 0-3 on the read data bus remains unmodified.
1b - The corresponding bit of bytes 0-3 on the read data bus is inverted.
50.10 Glossary
SEC-DED
Single error correction – double error detection
ECC
Error correction code
NXP Semiconductors
Error Injection Module (EIM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2078 / 5251


---