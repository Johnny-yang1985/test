# 페이지 1

Chapter 20
Memory and Memory Interfaces
20.1 Introduction
This chapter discusses the configuration of memories and memory interfaces, such as flash memory, flash memory controller, 
and SRAM.
20.2 Flash memory controller and flash memory modules
For information on this, see the following chapters:
• Flash Memory Controller (PFLASH)
• Embedded Flash Memory
20.3 Related information
Table 99. Related information
Topic
Related chapters
For additional information
System memory map
Memory Map
See the memory map file attached to this document.
Clocking
• Clocking Overview
• Clock Generation Module (MC_CGM)
—
Arm Cortex-M7 core
Cortex-M7 Overview
XRDC
Extended Resource Domain Controller
Direct-memory access
• Direct Memory Access Multiplexer 
(DMAMUX)
• Enhanced Direct Memory Access 
(eDMA)
See the DMAMUX map file attached to 
this document.
EIM
Error Injection Module
—
ERM
Error Reporting Module
—
20.4 SRAM access
In case a master accesses an SRAM with multi-bit ECC errors, the chip may respond as follows:
• Map all such faults to FCCU. The recommended reaction for the fault is to generate the functional reset.
• Map such faults to ERM. If the ERM interrupt is enabled, ERM generates an interrupt.
20.5 Memories
The following table provides information on the types of memories, with their associated configurations, available in 
S32K3xx family.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
766 / 5251


---
# 페이지 2

Table 100. Memory configuration
Memory
Size
Configuration 
(words × bits)
ECC or parity
ECC or 
parity 
width
Diagnostic 
information or 
error report
Applicability
SRAM0
160 KB
32 KB with 
STANDBY mode retention 
(4096 × (64 + 8))
ECC (SECDED)
8
ERM
S32K314
S32K324
S32K344
128 KB (16384 × (64 + 8))
64 KB
32 KB with 
STANDBY mode retention 
(4096 × (64 + 8))
ECC (SECDED)
8
ERM
S32K342
S32K322
S32K341
32 KB (4096 × (64 + 8))
96 KB
32 KB with 
STANDBY mode retention 
(4096 × (64 + 8))
ECC (SECDED)
8
ERM
S32K312
64 KB (8192 × (64 + 8))
32 KB
32 KB with 
STANDBY mode retention 
(4096 × (64 + 8))
ECC (SECDED)
8
ERM
S32K311
16 KB
16 KB with 
STANDBY mode retention 
(2048 × (64 + 8))
ECC (SECDED)
8
ERM
S32K310
256 KB
64 KB with standby mode 
retention (8192 x (64 +8))
ECC (SECDED)
8
ERM
S32K358 
S32K388 
S32K338 
S32K348 
S32K328
128 KB (16384 x (64+8))
64 KB (8192 x (64 +8))
512 KB
64 KB with STANDBY 
mode retention (8192 x 
(64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
ECC (SECDEC)
8
ERM
S32K389
SRAM1
160 KB
32 KB (4096 × (64 + 8))
ECC (SECDED)
8
ERM
S32K314
S32K324
S32K344
128 KB (16384 × (64 + 8))
Table continues on the next page...
NXP Semiconductors
Memory and Memory Interfaces
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
767 / 5251


---
# 페이지 3

Table 100. Memory configuration (continued)
Memory
Size
Configuration 
(words × bits)
ECC or parity
ECC or 
parity 
width
Diagnostic 
information or 
error report
Applicability
256 KB
128 KB (16384 x (64+8))
ECC (SECDED)
8
ERM
S32K358 
S32K388 
S32K338
S32K348
S32K328
128 KB (16384 x (64+8))
512 KB
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
ECC (SECDEC)
8
ERM
S32K389
SRAM_2
256 KB
64 KB (8192 x (64 +8))
ECC (SECDED)
8
ERM
S32K358 
S32K388 
S32K338
S32K348
S32K328
128 KB (16384 x (64+8))
64KB (8192 x (64 +8))
512 KB
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
ECC (SECDEC)
8
ERM
S32K389
SRAM_3
384 KB
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
64 KB (8192 x (64 +8))
ECC (SECDEC)
8
ERM
S32K389
Table continues on the next page...
NXP Semiconductors
Memory and Memory Interfaces
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
768 / 5251


---
# 페이지 4

Table 100. Memory configuration (continued)
Memory
Size
Configuration 
(words × bits)
ECC or parity
ECC or 
parity 
width
Diagnostic 
information or 
error report
Applicability
CM7_1 I-cache 
data
8 KB
4 KB (512 × (64 + 8))
ECC (SECDED)
8
ERM
S32K324
S32K322
4 KB (512 × (64 + 8))
CM7_1 I-cache 
tag
672 bytes
336 bytes (128 × (21 + 7))
ECC (SECDED)
7
ERM
336 bytes (128 × (21 + 7))
CM7_1 D-cache 
data
8 KB
1 KB (256 × (32 + 7))
ECC (SECDED)
7
ERM
1 KB (256 × (32 + 7))
1 KB (256 × (32 + 7))
1 KB (256 × (32 + 7))
1 KB (256 × (32 + 7))
1 KB (256 × (32 + 7))
1 KB (256 × (32 + 7))
1 KB (256 × (32 + 7))
CM7_1 D-cache 
tag
800 bytes
200 bytes (64 × (25 + 7))
ECC (SECDED)
7
ERM
200 bytes (64 × (25 + 7))
200 bytes (64 × (25 + 7))
200 bytes (64 × (25 + 7))
CM7_0 I-cache 
data
8 KB
4 KB (512 × (64 + 8))
ECC (SECDED)
8
ERM
S32K314
S32K324
S32K344
S32K312
S32K342
S32K341
S32K311
S32K310
S32K322
4 KB (512 × (64 + 8))
CM7_0 I-cache 
tag
672 bytes
336 bytes (128 × (21 + 7))
ECC (SECDED)
7
ERM
336 bytes (128 × (21 + 7))
CM7_0 D-cache 
data
8 KB
1 KB (256 × (32 + 7))
ECC (SECDED)
7
ERM
1 KB (256 × (32 + 7))
1 KB (256 × (32 + 7))
1 KB (256 × (32 + 7))
1 KB (256 × (32 + 7))
1 KB (256 × (32 + 7))
1 KB (256 × (32 + 7))
1 KB (256 × (32 + 7))
CM7_0 D-cache 
tag
800 bytes
200 bytes (64 × (25 + 7))
ECC (SECDED)
7
ERM
200 bytes (64 × (25 + 7))
200 bytes (64 × (25 + 7))
Table continues on the next page...
NXP Semiconductors
Memory and Memory Interfaces
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
769 / 5251


---
# 페이지 5

Table 100. Memory configuration (continued)
Memory
Size
Configuration 
(words × bits)
ECC or parity
ECC or 
parity 
width
Diagnostic 
information or 
error report
Applicability
200 bytes (64 × (25 + 7))
CM7_0 I-
cache data
CM7_1 I-cache 
data 1
CM7_2 I-cache 
data 2
16 KB
8 KB (1024 x (64 + 8))
ECC (SECDED)
8
ERM
S32K358
S32K388
S32K389
S32K338
S32K348
S32K328
8 KB (1024 x (64 + 8))
CM7_3 I-cache 
data
16 KB
8 KB (1024 x (64 + 8))
ECC (SECDED)
8
ERM
S32K388/
S32K389
8 KB (1024 x (64 + 8))
CM7_0 I-cache tag
CM7_1 I-cache 
tag 1
CM7_2 I-cache 
tag 2
1280 
bytes
640 bytes (256 x (20 + 7))
ECC (SECDED)
7
ERM
S32K358 
S32K388 
S32K389
640 bytes (256 x (20 + 7))
CM7_3 I-cache 
tag
1280 
bytes
640 bytes (256 x (20 + 7))
ECC (SECDED)
7
ERM
S32K388/
S32K389
640 bytes (256 x (20 + 7))
CM7_0 D-
cache data
CM7_1 D-cache 
data 1
CM7_2 D-cache 
data 2
16 KB
2048 bytes (512 x (32 + 7))
ECC (SECDED)
7
ERM
S32K358 
S32K388 
S32K389
2048 bytes (512 x (32 + 7))
2048 bytes (512 x (32 + 7))
2048 bytes (512 x (32 + 7))
2048 bytes (512 x (32 + 7))
2048 bytes (512 x (32 + 7))
2048 bytes (512 x (32 + 7))
2048 bytes (512 x (32 + 7))
CM7_3 D-
cache data
16 KB
2048 bytes (512 x (32 + 7))
ECC (SECDED)
7
ERM
S32K388/
S32K389
2048 bytes (512 x (32 + 7))
2048 bytes (512 x (32 + 7))
2048 bytes (512 x (32 + 7))
2048 bytes (512 x (32 + 7))
2048 bytes (512 x (32 + 7))
2048 bytes (512 x (32 + 7))
2048 bytes (512 x (32 + 7))
Table continues on the next page...
NXP Semiconductors
Memory and Memory Interfaces
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
770 / 5251


---
# 페이지 6

Table 100. Memory configuration (continued)
Memory
Size
Configuration 
(words × bits)
ECC or parity
ECC or 
parity 
width
Diagnostic 
information or 
error report
Applicability
CM7_0 D-
cache tag
CM7_1 D-cache 
tag 1
CM7_2 D-cache 
tag 2
1536 
bytes
384 bytes (128 x (24 + 7))
ECC (SECDED)
7
ERM
S32K358 
S32K388 
S32K389
384 bytes (128 x (24 + 7))
384 bytes (128 x (24 + 7))
384 bytes (128 x (24 + 7))
CM7_3 D-
cache tag
1536 
bytes
384 bytes (128 x (24 + 7))
ECC (SECDED)
7
ERM
S32K388/
S32K389
384 bytes (128 x (24 + 7))
384 bytes (128 x (24 + 7))
384 bytes (128 x (24 + 7))
DMA TCD
1 KB
1 KB (128 × (64 + 8))
ECC (SECDED)
8
ERM
S32K314
S32K324
S32K344
S32K342
S32K341
S32K322
S32K338
S32K348
S32K328
S32K358
S32K388
S32K389
640 bytes
640 bytes (80 × (64 + 8))
ECC (SECDED)
8
ERM
S32K312
S32K311
S32K310
FlexCAN_0
5 KB
5 KB (640 × (64 + 40))
ECC (SECDED)
40
FlexCAN_0
S32K344 
S32K314 
S32K324 
S32K358 
S32K338 
S32K328 
S32K348 
S32K388 
S32K389
Table continues on the next page...
NXP Semiconductors
Memory and Memory Interfaces
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
771 / 5251


---
# 페이지 7

Table 100. Memory configuration (continued)
Memory
Size
Configuration 
(words × bits)
ECC or parity
ECC or 
parity 
width
Diagnostic 
information or 
error report
Applicability
FlexCAN_0
3968 
bytes
3968 bytes 
(496 × (64 + 40))
ECC (SECDED)
40
FlexCAN_0
S32K311
S32K310
S32K312 
S32K322 
S32K342
S32K341
FlexCAN_1
1920 
bytes
1920 bytes 
(240 × (64 + 40))
ECC (SECDED)
40
FlexCAN_1
S32K314
S32K324
S32K344
S32K312
S32K342
S32K341
S32K311
S32K310
S32K322
FlexCAN_2
1920 
bytes
1920 bytes 
(240 × (64 + 40))
ECC (SECDED)
40
FlexCAN_2
FlexCAN_3
1152 
bytes
1152 bytes 
(144 × (64 + 40))
ECC (SECDED)
40
FlexCAN_3
S32K314
S32K324
S32K344
S32K312
S32K342
S32K341
S32K322
FlexCAN_4
1152 
bytes
1152 bytes 
(144 × (64 + 40))
ECC(SECDED)
40
FlexCAN_4
S32K314
S32K324
S32K344
S32K312
FlexCAN_5
1152 
bytes
1152 bytes 
(144 × (64 + 40))
ECC (SECDED)
40
FlexCAN_5
FlexCAN_1
5120 
bytes
5120 bytes (640 x (64 + 
40))
ECC (SECDED)
40
ERM
S32K338
S32K348
S32K328
S32K358
S32K388
S32K389
Table continues on the next page...
NXP Semiconductors
Memory and Memory Interfaces
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
772 / 5251


---
# 페이지 8

Table 100. Memory configuration (continued)
Memory
Size
Configuration 
(words × bits)
ECC or parity
ECC or 
parity 
width
Diagnostic 
information or 
error report
Applicability
FlexCAN_2
5120 
bytes
5120 bytes (640 x (64 + 
40))
ECC (SECDED)
40
ERM
S32K338
S32K348
S32K328
S32K358
S32K388
S32K389
FlexCAN_3-
FlexCAN_7
1920 
bytes
1920 bytes (240 x (64 + 
40))
ECC (SECDED)
40
ERM
S32K328 
S32K338 
S32K348 
S32K358 
S32K388 
S32K389
FlexCAN_8 
- FlexCAN_11
1920 
bytes
1920 bytes (240 x (64 + 
40))
ECC (SECDEC)
40
ERM
S32K389
GMAC_TX
17408 
bytes
8704 bytes (1024 x (68 + 
8))
ECC (SECDED)
8
GMAC
S32K328 
S32K338 
S32K348 
S32K358
8704 bytes (1024 x (68 + 
8))
GMAC_0_TX
GMAC_1_TX
17408 
bytes
8704 bytes (1024 x (68 + 
8))
ECC (SECDED)
8
GMAC
S32K388/
S32K389
8704 bytes (1024 x (68 + 
8))
GMAC_RX
17408 
bytes
8704 bytes (1024 x (68 + 
8))
ECC (SECDED)
8
GMAC
S32K328 
S32K338 
S32K348 
S32K358
8704 bytes (1024 x (68 + 
8))
GMAC_0_RX
GMAC_1_RX
17408 
bytes
8704 bytes (1024 x (68 + 
8))
ECC (SECDED)
8
GMAC
S32K388/
S32K389
8704 bytes (1024 x (68 + 
8))
GMAC_TSN
1728 
bytes
1728 bytes (512 x (27 + 7))
ECC (SECDED)
7
GMAC
S32K328 
S32K338 
S32K348 
S32K358
GMAC_0_TSN
GMAC_1_TSN
1728 
bytes
1728 bytes (512 x (27 + 7))
ECC (SECDED)
7
GMAC
S32K388/
S32K389
Table continues on the next page...
NXP Semiconductors
Memory and Memory Interfaces
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
773 / 5251


---
# 페이지 9

Table 100. Memory configuration (continued)
Memory
Size
Configuration 
(words × bits)
ECC or parity
ECC or 
parity 
width
Diagnostic 
information or 
error report
Applicability
GMAC_RXPARS
ER
960 bytes
960 Bytes (80 x (96 + 8)
ECC (SECDED)
8
GMAC
S32K328 
S32K338 
S32K348 
S32K358
GMAC_0_RXPAR
SER
GMAC_1_RXPAR
SER
960 bytes
960 Bytes (80 x (96 + 8)
ECC (SECDED)
8
GMAC
S32K388/
S32K389
QuadSPI RAM
1 KB
1 KB (128×64)
No
0
Not applicable
S32K328 
S32K338 
S32K348 
S32K358 
S32K388 
S32K389
EMAC TX
8960 
bytes
4480 bytes 
(1024 × (35 + 7))
ECC (SECDED)
7
EMAC
S32K314 
S32K324 
S32K344 
S32K342
S32K341
S32K322
4480 bytes 
(1024 × (35 + 7))
EMAC RX
8960 
bytes
4480 bytes 
(1024 × (35 + 7))
ECC (SECDED)
7
EMAC
4480 bytes 
(1024 × (35 + 7))
EMAC TSN
1664 
bytes
1664 bytes (512 × (26 + 7)) ECC (SECDED)
7
EMAC
EMAC 
RXPARSER
960 bytes
960 bytes (80 × (96 + 8))
ECC (SECDED)
8
EMAC
QuadSPI TX
320 bytes
320 bytes (80×32)
No
0
Not applicable
Boot ROM3
160 kB
32 kB(8192x(32+0))
No
0
Not applicable
S32K311
S32K310
S32K312 
S32K342 
S32K341 
S32K344
S32K338
S32K348
S32K328
S32K358
S32K388
Table continues on the next page...
NXP Semiconductors
Memory and Memory Interfaces
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
774 / 5251


---
# 페이지 10

Table 100. Memory configuration (continued)
Memory
Size
Configuration 
(words × bits)
ECC or parity
ECC or 
parity 
width
Diagnostic 
information or 
error report
Applicability
S32K389
QuadSPI TX
1152 
bytes
1152 bytes (256 x (36 + 0))
No
0
Not applicable
S32K328 
S32K338 
S32K348 
S32K358 
S32K388 
S32K389
Cortex-M7 cluster 
ETF ETMI
1 KB
1 KB (128×64)
No
0
Not applicable
S32K314
S32K324
S32K344
Cortex-M7 cluster 
ETF ETMD
2 KB
2 KB (128×128)
No
0
Not applicable
HTM ETF
1 KB
1 KB (128×64)
No
0
Not applicable
Shared system 
ETF
2 KB
2 KB (256×64)
No
0
Not applicable
Cortex-M7 cluster 
ETF ETMI
2 KB
2 KB (256 x 64)
No
0
Not applicable
S32K328 
S32K338 
S32K348 
S32K358
Cortex-M7 cluster 
ETF ETMI
4 KB
4 KB (512 x 64)
No
0
Not applicable
S32K388/
S32K389
Cortex-M7 cluster 
ETF ETMD
2 KB
2 KB (128 x 128)
No
0
Not applicable
S32K328 
S32K338 
S32K348 
S32K358
Cortex-M7 cluster 
ETF ETMD
4 KB
4 KB (256 x 128)
No
0
Not applicable
S32K388/
S32K389
HTM ETF
1 KB
1 KB (128 x 64)
No
0
Not applicable
S32K338
S32K348
S32K328
S32K358
HTM ETF
2 KB
2 KB (256 x 64)
No
0
Not applicable
S32K388/
S32K389
Shared System 
ETF
4 KB
4 KB (512 x 64)
No
0
Not applicable
S32K328 
S32K338 
S32K348 
S32K358 
Table continues on the next page...
NXP Semiconductors
Memory and Memory Interfaces
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
775 / 5251


---
# 페이지 11

Table 100. Memory configuration (continued)
Memory
Size
Configuration 
(words × bits)
ECC or parity
ECC or 
parity 
width
Diagnostic 
information or 
error report
Applicability
S32K388 
S32K389
CM7_0_ITCM
32kB
4096x(64+8)
ECC (SECDED)
8
ERM
S32K311
S32K310
S32K312 
S32K322 
S32K314 
S32K324 
S32K328 
S32K338 
S32K388 
S32K389 
(CM7_0 not in 
lockstep)
CM7_0_DTCM
64kB
8192x(32+8)
ECC (SECDED)
8
ERM
S32K311
S32K310
S32K312 
S32K322 
S32K314 
S32K324 
S32K328 
S32K338 
S32K388 
S32K389 
(CM7_0 not in 
lockstep)
8192x(32+8)
CM7_1_ITCM
32kB
4096x(64+8)
ECC (SECDED)
8
ERM
S32K322 
S32K324 
S32K328 
S32K338 
S32K388 
S32K389 
(CM7_0 not in 
lockstep)
CM7_1_DTCM
64kB
8192x(32+8)
ECC (SECDED)
8
ERM
S32K322 
S32K324 
S32K328 
S32K338 
S32K388 
S32K389 
(CM7_0 not in 
lockstep)
8192x(32+8)
CM7_2_ITCM
64kB
8192*(64+8)
ECC (SECDED)
8
ERM
S32K338
Table continues on the next page...
NXP Semiconductors
Memory and Memory Interfaces
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
776 / 5251


---
# 페이지 12

Table 100. Memory configuration (continued)
Memory
Size
Configuration 
(words × bits)
ECC or parity
ECC or 
parity 
width
Diagnostic 
information or 
error report
Applicability
S32K348
S32K328
S32K358
CM7_2_DTCM
128kB
16384x(32+8)
ECC (SECDED)
8
ERM
S32K338
S32K348
S32K328
S32K358
16384x(32+8)
CM7_2_ITCM
32kB
4096x(64+8)
ECC (SECDED)
8
ERM
S32K388/
S32K389
CM7_2_DTCM
64kB
8192x(32+8)
ECC (SECDED)
8
ERM
S32K388/
S32K389
8192x(32+8)
CM7_3_ITCM
32kB
4096x(64+8)
ECC (SECDED)
8
ERM
S32K388/
S32K389
CM7_3_DTCM
64kB
8192x(32+8)
ECC (SECDED)
8
ERM
S32K388/
S32K389
8192x(32+8)
CM7_0_ITCM
64kB
4096x(64+8)
ECC (SECDED)
8
ERM
S32K358 
S32K348 
S32K344 
S32K342 
S32K341
4096x(64+8)
CM7_0_DTCM
128kB
8192x(32+8)
ECC (SECDED)
8
ERM
S32K358 
S32K348 
S32K344 
S32K342 
S32K341
8192x(32+8)
8192x(32+8)
8192x(32+8)
ACE FEED_DMA
1 Kb
128x(64+8)
ECC (SECDED)
8
S32K388/
S32K389
ACE 
RESULT_DMA
1 Kb
128x(64+8)
ECC (SECDED)
8
S32K388/
S32K389
1. Not applicable for S32K358 and S32K348.
2. Not applicable for S32K348 and S32K328.
3. Five instances of this memory
20.6 Recommendations for Arm memories
As per Arm M-7 Safety manual, following considerations must be ensured for proper operation of Arm memories:
• ITCM and DTCM must be properly initialized with correct ECC before any read operation to avoid any code runaway or 
software malfunction or core lockup.
NXP Semiconductors
Memory and Memory Interfaces
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
777 / 5251


---
# 페이지 13

 
ITCM must be initialized with 64-bit writes whereas DTCM can be initialized with 32-bit writes also.
  NOTE  
• To safely disable TCM:
1. Clear ITCMCR[EN] or DTCMCR[EN] as required. See Arm Cortex-M7 Devices Generic User Guide for details on 
ITCMCR and DTCMCR register.
2. Execute DSB instruction
3. Execute ISB instruction
 
Care must be taken if disabling the ITCM while executing from it. In this case, software must ensure that the 
switch-off code is stored in the L2 code memory region from where execution continues when the ITCM is disabled.
  NOTE  
• To safely disable the I-cache:
1. Clear CCR[IC]. See Arm Cortex-M7 Devices Generic User Guide for details on CCR register.
2. Execute DSB instruction
3. Execute ISB instruction
• To safely disable the D-cache:
1. Clean and invalidate non-WT locations in D-cache
2. Clear CCR[DC]
3. Execute DSB instruction
See Table 101 for details on memory ECC initialization.
20.7 Memory ECC initialization summary
The table below summarizes memory ECC initialization.
Table 101. Memory ECC initialization summary
Memory
Write access size
Masters
CM7_ n
CM7_ m
eDMA
SRAM
64-bits only
System
System
System
CM7_n ITCM
64-bits only
Direct or Backdoor
Backdoor
Not possible
CM7_n DTCM
32-bits or 64-bits
Direct or Backdoor
Backdoor
Backdoor
CM7_m ITCM
64-bits only
Backdoor
Direct or Backdoor
Not possible
CM7_m DTCM
32-bits or 64-bits
Backdoor
Direct or Backdoor
Backdoor
20.8 Glossary
DTCM
Data tightly coupled memory
ECC
Error code correction
ETF
Embedded trace FIFO
ETMD
Embedded trace macrocell-data
ETMI
Embedded trace macrocell-instruction
ITCM
Instruction tightly coupled memory
NXP Semiconductors
Memory and Memory Interfaces
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
778 / 5251


---
# 페이지 14

MTB
Macrocell trace buffer
PKC
Public key cryptography
RXPARSER
Receive parser memory
SECDED
Single error correction double error detection
SRAM
Static random access memory
TSN
Time sensitive network
NXP Semiconductors
Memory and Memory Interfaces
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
779 / 5251


---