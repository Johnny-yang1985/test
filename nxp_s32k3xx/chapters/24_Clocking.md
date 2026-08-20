# 페이지 1

Chapter 24
Clocking
24.1 Introduction
This chapter describes the clocking architecture and includes the following information:
• System clock specifics
• Clock sources
• Clock architecture
• Clock control registers
• Clock monitoring
• Clock gating
• Module clocking
This chapter discusses the clocks generated on the chip. Peripheral-specific protocol clocks are described in the corresponding 
peripheral chapters.
24.2 Features
• Multiple clock sources supported for clock generation:
— Fast internal RC oscillator (FIRC)
— Slow internal RC oscillator (SIRC)
— Fast external crystal oscillator (FXOSC)
— Slow external crystal oscillator (SXOSC)
 
SXOSC is not available in 100-HDQFP and 48-pin LQFP packages.
  NOTE  
— Phase-locked loop (PLL)
• Frequency-modulated PLL output clock to reduce electromagnetic emissions
• Precise clocks for timers and communication functions
• Glitchless clock switching Clock Generation module (MC_CGM) clock selectors
• System clock progressive clock frequency switching (PCFS)
• Clock monitoring units (CMU_FC, CMU_FM) to check clock integrity
• Core and peripheral clock gating using the Mode Entry module's (MC_ME) partition process configuration registers
24.3 Clocking overview
The S32K3xx clocking architecture consists of multiple:
• Clock sources
• Monitors
• Multiplexers
• Dividers
The blocks in the above bullet list provide the required clocking domains for the different functional blocks.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
903 / 5251


---
# 페이지 2

The sections in the following list show the clocking configuration of the chip:
• Clock source generation: PLL, FXOSC, FIRC, SIRC, and SXOSC
• MC_CGM mux 0 clocks: MC_CGM mux 0 generated clocks (not including EMAC/GMAC clock signals)
• Clockout overview: CLKOUT_STANDBY and CLKOUT_RUN
• Other clocks
• GMAC clocks (S32K388 and S32K389)
• GMAC clocks (S32K328, S32K338, S32K348, and S32K358)
• EMAC clocks (S32K344, S32K324, S32K314, S32K322, S32K341 and S32K342)
The figures shown in S32K389 clock system diagram, S32K388 clock system diagram, S32K328, S32K338, S32K348, and 
S32K358 clock system diagram, S32K344, S32K324, S32K314, S32K322, S32K341 and S32K342 clock system diagram, 
S32K312 clock system diagram, and S32K310 and S32K311 clock system diagram show the overall clock tree for the different 
chip variants of the S32K3xx family, which are a combination of the sections mentioned in the bullet list above.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
904 / 5251


---
# 페이지 3

24.3.1 Clock source generation
PLLDIG.PLLODIV_0[DIV]
PLLDIG.PLLODIV_1[DIV]
FIRC_CLK
FXOSC_CLK
SXOSC_CLK
SIRC_CLK
1...16
3
0
XTAL
EXTAL
1
2
DIV2
DIV16
PLLDIG
PLL
FIRC
HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL]
FXOSC
PLL_PHI0_CLK
PLL_PHI1_CLK
SIRC
SXOSC
OSC32K_XTAL
OSC32K_EXTAL
FIRC
CMU_FC_0
CMU_FM_2
CMU_FM_1
1...63
1...16
PLLDIG.PLLDV[ODIV2]
VCO_CLK
Not available on:
- S32K310
- S32K311
PLLODIV2_CLK
PLLDIG.PLLODIV_0[DIV]
PLLDIG.PLLODIV_2[DIV]
1...32
PLLDIG
PLL_AUX
PLL_AUX_PHI0_CLK
PLL_AUX_PHI2_CLK
1...63
1...32
PLLDIG.PLLDV[ODIV2]
VCO_CLK
PLLODIV2_CLK
PLL_AUX_PHI1_CLK
1...32
PLLDIG.PLLODIV_1[DIV]
Only available on:
- S32K328
- S32K338 
- S32K348
- S32K358
- S32K388
- S32K389
Not available on:
- S32K388
- S32K389
10
1
PLLDIG.PLLCLKMUX[REFCLKSEL]
Only available on:
- S32K310
- S32K311
REFCLKSEL is 0 
for rest of the chips
Figure 59. Clock source generation
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
905 / 5251


---
# 페이지 4

24.3.2 MC_CGM mux 0 clocks
PCFS
MUX_0_CSC[SELCTL]
1...8
MUX_0_DC_1[DIV]
AIPS_PLAT_CLK
8
0
MUX_0_DC_0[DIV]
CORE_CLK
1...8
QSPI_MEM_CLK
MUX_0_DC_6[DIV]
1...8
PLL_PHI0_CLK
FIRC_CLK
MUX_0_DC_2[DIV]
AIPS_SLOW_CLK
1...16
MUX_0_DC_3[DIV]
HSE_CLK
1...8
MUX_0_DC_4[DIV]
DCM_CLK
1...8
MUX_0_DC_5[DIV]
LBIST_CLK
1...8
MUX0_0_CSC[RAMPUP]
MUX0_0_CSC[RAMPDOWN]
PCFS_SDUR[SDUR]
CMU_FC_3
CMU_FC_4
CMU_FC_5
Not available on:
- S32K310
- S32K311
- S32K312
1...8
MUX_0_DC_7[DIV]
CM7_CORE_CLK
Only  available on:
- S32K388
- S32K389
CMU_FC_6
Figure 60. MC_CGM mux 0 clocks
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
906 / 5251


---
# 페이지 5

24.3.3 Clockout overview
1...8
MUX_5_DC_0[DIV]
CLKOUT_STANDBY
SIRC_CLK
FIRC_CLK
FXOSC_CLK
SXOSC_CLK
PLL_PHI0_CLK
PLL_AUX_PHI0_CLK
HSE_CLK
AIPS_PLAT_CLK
25
23
22
24
19
12
8
2
1
0
4
9
PLL_PHI1_CLK
EMAC_RX_CLK
EMAC_RMII_TX_CLK
AIPS_SLOW_CLK
MUX_6_CSC[SELCTL]
MUX_5_CSC[SELCTL]
FIRC_CLK
SIRC_CLK
FXOSC_CLK
SXOSC_CLK
AIPS_SLOW_CLK
23
4
1
0
2
SIUL2_MSCRm[OBE]
SIUL2_MSCRm[SSS]
Port
Only available on:
- S32K344
- S32K324
- S32K314
- S32K322
- S32K341
- S32K342
1...64
MUX_6_DC_0[DIV]
SIUL2_MSCRn[OBE]
SIUL2_MSCRn[SSS]
Port
CLKOUT_RUN
Not available on:
- S32K310
- S32K311
Not available on:
- S32K310
- S32K311
CORE_CLK
16
PLL_AUX_PHI2_CLK
14
PLL_AUX_PHI1_CLK
13
Only available on:
- S32K328
- S32K338 
- S32K348
- S32K358
Only available on:
- S32K328
- S32K338 
- S32K348
- S32K358
- S32K388
- S32K389
GMAC_MII_RGMII_RX_CLK
GMAC_MII_RMII_RGMII_TX_CLK
25
24
Only available on:
- S32K328
- S32K338 
- S32K348
- S32K358
GMAC0_MII_RGMII_RX_CLK
GMAC0_MII_RMII_RGMII_TX_CLK
25
24
Only available on:
- S32K388
- S32K389
Figure 61. Clockout overview
 
CLKOUT_RUN is not available during Standby mode.
  NOTE  
24.3.3.1
SIUL2 options for CLKOUT_RUN
Table 115. SIUL2 options for CLKOUT_RUN
Source
Destination
Port
MSCRn
MSCR fields
OBE
IBE
SSS
MUX_6_DC_0 divider 
output
CLKOUT_RUN
PTB5
37
1
0
0101b
PTD10
106
1
0
0110b
PTD14
110
1
0
0111b
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
907 / 5251


---
# 페이지 6

24.3.3.2
SIUL2 options for CLKOUT_STANDBY
Table 116. SIUL2 options for CLKOUT_STANDBY
Source
Destination
Port
MSCRm
MSCR fields
OBE
IBE
SSS
MUX_5_DC_0 divider 
output
CLKOUT_STANDBY
PTA12
12
1
0
0011b
PTE10
138
1
0
0101b
24.3.4 Other clocks
1...2
MUX_1_DC_0[DIV]
MUX_1_CSC[SELCTL]
22
0
2
STM0_CLK
MUX_2_DC_0[DIV]
STM1_CLK
MUX_3_DC_0[DIV]
FLEXCAN0_PE_CLK 
FLEXCAN1_PE_CLK 
FLEXCAN2_PE_CLK
MUX_4_DC_0[DIV]
AIPS_PLAT_CLK
FXOSC_CLK
FIRC_CLK
22
0
2
22
0
2
22
0
2
MUX_2_CSC[SELCTL]
MUX_3_CSC[SELCTL]
MUX_4_CSC[SELCTL]
1...2
1...4
1...4
QSPI_2xSFCK
MUX_11_DC_0[DIV]
TRACE_CLK
PLL_PHI0_CLK
PLL_PHI1_CLK
0
2
8
9
MUX_11_CSC[SELCTL]
MUX_10_CSC[SELCTL]
0
2
9
1...8
1...8
MUX_10_DC_0[DIV]
Not available on:
- S32K314
- S32K312
- S32K311
- S32K310
Not available on:
S32K310, S32K311, S32K322,
S32K341, S32K342
Not available on:
S32K312, S32K311, S32K310
FLEXCAN3_PE_CLK
FLEXCAN4_PE_CLK
FLEXCAN5_PE_CLK
Not available on:
- S32K311
- S32K310
16
CORE_CLK
16
FLEXCAN7_PE_CLK
FLEXCAN6_PE_CLK
Only available on:
S32K328, S32K338, S32K348,
S32K358, S32K388, S32K389
PLL_AUX_PHI0_CLK
12
DIV-BY-2
QSPI_SFCK
MUX_13_DC_0[DIV]
STM2_CLK
22
0
2
MUX_13_CSC[SELCTL]
1...2
MUX_14_DC_0[DIV]
uSDHC_PER_CLK
MUX_14_CSC[SELCTL]
1...2
0
2
9
14
Only available on:
- S32K328
- S32K338
- S32K348
- S32K358
PLL_AUX_PHI2_CLK
Only available on:
- S32K328
- S32K338
- S32K348
- S32K358
DIV-BY-2
12
MUX_18_DC_0[DIV]
STM3_CLK
MUX_18_CSC[SELCTL]
1...2
0
2
22
Only available on:
- S32K388
- S32K389
MUX_19_DC_0[DIV]
AES_1us_CLK
MUX_19_CSC[SELCTL]
1...2
0
13
Only available on:
- S32K388
- S32K389
PLL_AUX_PHI1_CLK
Only available on:
- S32K328
- S32K338 
- S32K348
- S32K358 
- S32K388
- S32K389
Only available on:
S32K328, S32K338, S32K348,
S32K358
Only available on:
S32K328, S32K338, S32K348,
S32K358, S32K388, S32K389
Only available on:
S32K328, S32K338, S32K348,
S32K358
Not available on:
- S32K388, S32K389
TCK
JTAG_TCK/SWD_CLK
MUX_20_DC_0[DIV]
FLEXCAN[8:11]_PE_CLK
MUX_20_CSC[SELCTL]
1...4
0
22
Only available on:
- S32K389
2
Only available on:
- S32K328
- S32K338 
- S32K348
- S32K358 
- S32K388
- S32K389
Figure 62. Other clocks
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
908 / 5251


---
# 페이지 7

24.3.5 GMAC clocks (S32K388 and S32K389)
MUX_15_DC_0[DIV]
GMAC1_CLK_RX
MUX_15_CSC[SELCTL]
1...2
0
30
MUX_16_DC_0[DIV]
GMAC1_CLK_TX
MUX_16_CSC[SELCTL]
1...2
0
12
30
MUX_9_DC_0[DIV]
GMAC_CLK_TS
1...64
MUX_9_CSC[SELCTL]
30
29
25
24
12
2
0
MUX_8_DC_0[DIV]
MUX_8_CSC[SELCTL]
1...64
0
12
24
MUX_7_DC_0[DIV]
GMAC0_CLK_RX
MUX_7_CSC[SELCTL]
1...64
24
0
FIRC_CLK
PLL_AUX_PHI0_CLK
FXOSC_CLK
GMAC1_MII_RMII_RGMII_TX_CLK
GMAC0_MII_RMII_RGMII_TX_CLK
GMAC1_MII_RGMII_RX_CLK
GMAC0_CLK_TX
GMAC0_MII_RGMII_RX_CLK
Figure 63. GMAC clocks (S32K388 and S32K389)
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
909 / 5251


---
# 페이지 8

24.3.6 GMAC clocks (S32K328, S32K338, S32K348, and S32K358)
MUX_9_DC_0[DIV]
GMAC_CLK_TS
1...64
MUX_9_CSC[SELCTL]
25
24
12
2
0
MUX_8_DC_0[DIV]
MUX_8_CSC[SELCTL]
1...64
0
12
24
MUX_7_DC_0[DIV]
MUX_7_CSC[SELCTL]
1...64
8
12
24
25
GMAC_CLK_RX
0
8
FIRC_CLK
PLL_AUX_PHI0_CLK
FXOSC_CLK
 8
PLL_PHI0_CLK
GMAC_MII_RMII_RGMII_TX_CLK
GMAC_MII_RGMII_RX_CLK
GMAC_CLK_TX
Figure 64. GMAC clocks (S32K328, S32K338, S32K348, and S32K358)
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
910 / 5251


---
# 페이지 9

24.3.7 EMAC clocks (S32K344, S32K324, S32K314, S32K322, S32K341 and S32K342)
MUX_9_DC_0[DIV]
1...64
MUX_9_CSC[SELCTL]
25
24
2
0
MUX_8_DC_0[DIV]
MUX_8_CSC[SELCTL]
1...64
0
24
MUX_7_DC_0[DIV]
MUX_7_CSC[SELCTL]
1...64
24
25
EMAC_CLK_RX
EMAC_CLK_TS
0
FIRC_CLK
FXOSC_CLK
 8
EMAC_MII_RMII_TX_CLK
EMAC_MII_RX_CLK
EMAC_CLK_TX
PLL_PHI0_CLK
Figure 65. EMAC clocks (S32K344, S32K324, S32K314, S32K322, S32K341 and S32K342)
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
911 / 5251


---
# 페이지 10

24.3.8 S32K389 clock system diagram
CMU with FXOSC reference
CMU with FIRC reference
1...2
MUX_1_DC_0[DIV]
MC_CGM_MUX1
PLLDIG.PLLODIV_1[DIV]
PLLDIG.PLLODIV_0[DIV]
PLLODIV2_CLK
PLLDIG.PLLDV[ODIV2]
PLL_PHI1_CLK
FXOSC_CLK
SXOSC_CLK
SIRC_CLK
VCO_CLK
PLL_PHI0_CLK
FIRC
(48 MHz)
DCM.DCMRWP1[1]
22
0
2
3
1
0
2
22
0
2
1...8
MUX_0_DC_5[DIV]
22
0
2
PCFS
MC_CGM_MUX0
1...8
MUX_0_DC_4[DIV]
1...8
MUX_0_DC_3[DIV]
1...8
MUX_0_DC_2[DIV]
1...8
MUX_0_DC_1[DIV]
1...8
CMU_FC_3
MUX_0_DC_0[DIV]
MC_CGM
CORE_CLK
AIPS_PLAT_CLK
AIPS_SLOW_CLK
HSE_CLK
DCM_CLK
LBIST_CLK
QSPI_MEM_CLK
STM0_CLK
1...2
MUX_2_DC_0[DIV]
MC_CGM_MUX2
STM1_CLK
MUX_3_DC_0[DIV]
MC_CGM_MUX3
FLEXCAN[0:2]_PE_CLK
FLEXCAN[3:7]_PE_CLK
MUX_4_DC_0[DIV]
MC_CGM_MUX4
MC_CGM_MUX5
MC_CGM_MUX6
1...8
MUX_0_DC_6[DIV]
CM7_CORE_CLK
1...4
MUX_0_DC_7[DIV]
8
0
22
0
2
MUX_7_DC_0[DIV]
MC_CGM_MUX7
MAC0_CLK_RX
MUX_6_DC_0[DIV]
CLKOUT_RUN
MUX_8_DC_0[DIV]
MC_CGM_MUX8
_CLK_TX
MUX_9_DC_0[DIV]
MC_CGM_MUX9
GMAC_CLK_TS
MUX_10_DC_0[DIV]
MC_CGM_MUX10
MC_CGM_MUX11
MC_CGM_MUX18
QSPI_SFCK
MUX_5_DC_0[DIV]
CLKOUT_STANDBY
25
2
0
24
24
22
19
23
16
13
12
23
9
4
2
1
0
8
22
0
2
1...2
MUX_13_DC_0[DIV]
FXOSC
(8-40 MHz)
XTAL
EXTAL
SXOSC
(32 kHz)
OSC32K_XTAL
OSC32K_EXTAL
GMAC0_MII_RMII_RGMII_TX_CLK
GMAC0_MII   RGMII_ 
_
RX_CLK
SIRC
(32 kHz)
4
1
0
2
CMU_FC_4
CMU_FC_5
1...4
1...4
1...8
1...64
1...64
1...64
1...64
1...8
CMU_FC_0
FIRC_CLK
CMU_FM_1
CMU_FM_2
÷ 2
÷ 2
÷ 16
PLL
1...16
1...63
1...16
PLLDIG.PLLODIV_1[DIV]
PLLDIG.PLLODIV_0[DIV]
PLLODIV2_CLK
PLLDIG.PLLDV[ODIV2]
VCO_CLK
PLL_AUX_PHI0_CLK
PLL_AUX_PHI1_CLK
PLL_
AUX
1...32
1...63
1...32
0
12
24
0
24
0
2
9
12
MC_CGM_MUX13
MUX_15_DC_0[DIV]
MC_CGM_MUX15
GMAC1_CLK_RX
1...2
0
30
MUX_16_DC_0[DIV]
MC_CGM_MUX16
GMAC1_CLK_TX
1...2
0
12
30
MUX_18_DC_0[DIV]
STM3_CLK
1...2
MC_CGM_MUX19
0
13
MUX_19_DC_0[DIV]
1...2
MUX_11_DC_0[DIV]
TRACE_CLK
STM2_CLK
12
2
0
9
1...8
AES_1us_CLK
G
MAC0
G
CMU_FC_6
12
GMAC1_MII_
RX_CLK
29
30
3
1
23
1
2
RTC_CLK
RTC.RTCC[CLKSEL]
RTC
4
2
0
1
JTAG_TCK/SWD_CLK
TCK
  RGMII_
GMAC1_MII_RMII_RGMII_TX_CLK
25
.div-by-2
0
22
2
FLEXCAN[8:11]_PE_CLK
MUX_20_ DC_0[DIV]
MC_CGM_MUX20
1...4
22
2
0
.div-by-2
.div-by-2
.div-by-2
Figure 66. S32K389 clock system diagram
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
912 / 5251


---
# 페이지 11

24.3.9 S32K388 clock system diagram
CMU with FXOSC reference
CMU with FIRC reference
1...2
MUX_1_DC_0[DIV]
MC_CGM_MUX1
PLLDIG.PLLODIV_1[DIV]
PLLDIG.PLLODIV_0[DIV]
PLLODIV2_CLK
PLLDIG.PLLDV[ODIV2]
PLL_PHI1_CLK
FXOSC_CLK
SXOSC_CLK
SIRC_CLK
VCO_CLK
PLL_PHI0_CLK
FIRC
(48 MHz)
DCM.DCMRWP1[1]
22
0
2
3
1
0
2
22
0
2
1...8
MUX_0_DC_5[DIV]
22
0
2
PCFS
MC_CGM_MUX0
1...8
MUX_0_DC_4[DIV]
1...8
MUX_0_DC_3[DIV]
1...8
MUX_0_DC_2[DIV]
1...8
MUX_0_DC_1[DIV]
1...8
CMU_FC_3
MUX_0_DC_0[DIV]
MC_CGM
CORE_CLK
AIPS_PLAT_CLK
AIPS_SLOW_CLK
HSE_CLK
DCM_CLK
LBIST_CLK
QSPI_MEM_CLK
STM0_CLK
1...2
MUX_2_DC_0[DIV]
MC_CGM_MUX2
STM1_CLK
MUX_3_DC_0[DIV]
MC_CGM_MUX3
FLEXCAN[0:2]_PE_CLK
FLEXCAN[3:7]_PE_CLK
MUX_4_DC_0[DIV]
MC_CGM_MUX4
MC_CGM_MUX5
MC_CGM_MUX6
1...8
MUX_0_DC_6[DIV]
CM7_CORE_CLK
1...4
MUX_0_DC_7[DIV]
8
0
22
0
2
MUX_7_DC_0[DIV]
MC_CGM_MUX7
MAC0_CLK_RX
MUX_6_DC_0[DIV]
CLKOUT_RUN
MUX_8_DC_0[DIV]
MC_CGM_MUX8
_CLK_TX
MUX_9_DC_0[DIV]
MC_CGM_MUX9
GMAC_CLK_TS
MUX_10_DC_0[DIV]
MC_CGM_MUX10
MC_CGM_MUX11
MC_CGM_MUX18
QSPI_SFCK
MUX_5_DC_0[DIV]
CLKOUT_STANDBY
0
22
2
25
2
0
24
24
22
19
23
16
13
12
23
9
4
2
1
0
8
22
0
2
1...2
MUX_13_DC_0[DIV]
FXOSC
(8-40 MHz)
XTAL
EXTAL
SXOSC
(32 kHz)
OSC32K_XTAL
OSC32K_EXTAL
GMAC0_MII_RMII_RGMII_TX_CLK
GMAC0_MII   RGMII_ 
_
RX_CLK
SIRC
(32 kHz)
4
1
0
2
CMU_FC_4
CMU_FC_5
1...4
1...4
1...8
1...64
1...64
1...64
1...64
1...8
CMU_FC_0
FIRC_CLK
CMU_FM_1
CMU_FM_2
÷ 2
÷ 2
÷ 16
PLL
1...16
1...63
1...16
PLLDIG.PLLODIV_1[DIV]
PLLDIG.PLLODIV_0[DIV]
PLLODIV2_CLK
PLLDIG.PLLDV[ODIV2]
VCO_CLK
PLL_AUX_PHI0_CLK
PLL_AUX_PHI1_CLK
PLL_
AUX
1...32
1...63
1...32
0
12
24
0
24
0
2
9
12
MC_CGM_MUX13
MUX_15_DC_0[DIV]
MC_CGM_MUX15
GMAC1_CLK_RX
1...2
0
30
MUX_16_DC_0[DIV]
MC_CGM_MUX16
GMAC1_CLK_TX
1...2
0
12
30
MUX_18_DC_0[DIV]
STM3_CLK
1...2
MC_CGM_MUX19
0
13
MUX_19_DC_0[DIV]
1...2
MUX_11_DC_0[DIV]
TRACE_CLK
STM2_CLK
12
2
0
9
1...8
AES_1us_CLK
G
MAC0
G
CMU_FC_6
12
GMAC1_MII_
RX_CLK
29
30
3
1
23
1
2
RTC_CLK
RTC.RTCC[CLKSEL]
RTC
4
2
0
1
JTAG_TCK/SWD_CLK
TCK
  RGMII_
GMAC1_MII_RMII_RGMII_TX_CLK
25
.div-by-2
.div-by-2
.div-by-2
.div-by-2
Figure 67. S32K388 clock system diagram
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
913 / 5251


---
# 페이지 12

24.3.10 S32K328, S32K338, S32K348, and S32K358 clock system diagram
QSPI_2XSFIF
 
MUX_10_DC_0[DIV]
QSPI_SFCK
1...32
PLLDIG.PLLODIV_0[DIV]
PLLDIG.PLLODIV_2[DIV]
1...32
VCO_CLK
PLL_
AUX
1...63
PLLDIG.PLLDV[ODIV2]
PLLODIV2_CLK
1...32
PLLDIG.PLLODIV_1[DIV]
PLL_AUX_PHI0_CLK
PLL_AUX_PHI1_CLK
PLL_AUX_PHI2_CLK
OSC32K_XTAL
OSC32K_EXTAL
SXOSC (32 KHZ) 
PLL_Aux only present in S32K358
MUX_7_DC_0[DIV]
MC_CGM_MUX7
24
0
25
0
24
GMAC_CLK_RX
MUX_8_DC_0[DIV]
MC_CGM_MUX8
GMAC_CLK_TX
MUX_9_DC_0[DIV]
MC_CGM_MUX9
GMAC_CLK_TS
25
2
0
24
8
1...64
1...64
1...64
0
2
9
 GMAC_MII_RGMII_RX_CLK
 GMAC_MII_RMII_RGMII_TX_CLK
MC_CGM_MUX1
22
0
2
MUX_2_DC_0[DIV]
MC_CGM_MUX2
STM1_CLK
1...2
QSPI_MEM_CLK
MUX_0_DC_6[DIV]
1...8
LBIST_CLK
MUX_0_DC_5[DIV]
1...8
MC_CGM_MUX13
1...2
MUX_13_DC_0[DIV]
22
0
2
STM2_CLK
12
12
12
8
22
0
2
MUX_4_DC_0[DIV]
MC_CGM_MUX4
1...4
FLEXCAN[3:7]_PE_CLK
4
4
3
1
2
3
1
2
3
1
2
RTC_CLK
0
1...16
PLLDIG.PLLODIV_0[DIV]
1...2
MUX_1_DC_0[DIV]
PLLDIG.PLLODIV_1[DIV]
FIRC_CLK
FXOSC_CLK
SIRC_CLK
PLL_PHI0_CLK
FIRC
(48 MHz)
RTC.RTCC[CLKSEL]
3
0
22
0
2
PCFS
MC_CGM_MUX0
MUX_0_DC_4[DIV]
MUX_0_DC_3[DIV]
MUX_0_DC_2[DIV]
MUX_0_DC_1[DIV]
MUX_0_DC_0[DIV]
CORE_CLK
AIPS_PLAT_CLK
AIPS_SLOW_CLK
HSE_CLK
DCM_CLK
STM0_CLK
MUX_3_DC_0[DIV]
MC_CGM_MUX3
FLEXCAN[0:2]_PE_CLK
MC_CGM_MUX5
MC_CGM_MUX6
8
0
22
0
2
MUX_6_DC_0[DIV]
CLKOUT_RUN
MC_CGM_MUX10
MC_CGM_MUX11
RTC
MUX_5_DC_0[DIV]
CLKOUT_STANDBY
0
8
2
MUX_11_DC_0[DIV]
TRACE_CLK
TCK
23
FXOSC
(8-40 MHz)
XTAL
EXTAL
SIRC
(32 kHz)
CMU with FXOSC reference
CMU with FIRC reference
1
0
2
÷2
1
2
÷2
÷16
9
1...4
1...8
1...8
1...8
1...8
1...16
1...8
1...8
1...64
MC_CGM
PLL_PHI1_CLK
1...16
HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL]
JTAG_TCK/SWD_CLK
CMU_FM_1
CMU_FM_2
CMU_FC_0
CMU_FC_3
CMU_FC_4
CMU_FC_5
VCO_CLK
PLL
1...63
PLLDIG.PLLDV[ODIV2]
25
24
23
22
19
16
9
8
2
1
0
PLLODIV2_CLK
MC_CGM_MUX14
1...2
MUX_14_DC_0[DIV]
14
0
2
uSDHC_PER_CLK
.div-by-2
12
12
9
13
14
8
16
.div-by-2
16
4
4
.div-by-2
.div-by-2
1...8
12
Figure 68. S32K328, S32K338, S32K348, and S32K358 clock system diagram
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
914 / 5251


---
# 페이지 13

24.3.11 S32K344, S32K324, S32K314, S32K322, S32K341 and S32K342 clock system diagram
1...16
PLLDIG.PLLODIV_0[DIV]
1...2
MUX_1_DC_0[DIV]
PLLDIG.PLLODIV_1[DIV]
FIRC_CLK
FXOSC_CLK
SIRC_CLK
PLL_PHI0_CLK
FIRC
(48 MHz)
RTC.RTCC[CLKSEL]
3
0
22
0
2
PCFS
MC_CGM_MUX0
MUX_0_DC_4[DIV]
MUX_0_DC_3[DIV]
MUX_0_DC_2[DIV]
MUX_0_DC_1[DIV]
MUX_0_DC_0[DIV]
CORE_CLK
AIPS_PLAT_CLK
AIPS_SLOW_CLK
HSE_CLK
DCM_CLK
STM0_CLK
MUX_3_DC_0[DIV]
MC_CGM_MUX3
FLEXCAN[0:2]_PE_CLK
MC_CGM_MUX5
MC_CGM_MUX6
8
0
22
0
2
MUX_6_DC_0[DIV]
CLKOUT_RUN
MC_CGM_MUX11
RTC
MUX_5_DC_0[DIV]
CLKOUT_STANDBY
0
8
2
MUX_11_DC_0[DIV]
TRACE_CLK
TCK
23
FXOSC
(8-40 MHz)
XTAL
EXTAL
SIRC
(32 kHz)
CMU with FXOSC reference
CMU with FIRC reference
1
0
2
1
2
÷2
÷16
9
1...4
1...8
1...8
1...8
1...8
1...16
1...8
1...8
1...64
MC_CGM
PLL_PHI1_CLK
1...16
HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL]
JTAG_TCK/SWD_CLK
CMU_FM_1
CMU_FM_2
CMU_FC_0
CMU_FC_3
CMU_FC_4
CMU_FC_5
S32K3xx
VCO_CLK
PLL
1...63
PLLDIG.PLLDV[ODIV2]
23
22
19
16
9
8
2
1
0
PLLODIV2_CLK
MC_CGM_MUX1
÷2
.div-by-2
MUX_7_DC_0[DIV]
MC_CGM_MUX7
24
0
25
0
24
EMAC_CLK_RX
MUX_8_DC_0[DIV]
MC_CGM_MUX8
EMAC_CLK_TX
MUX_9_DC_0[DIV]
MC_CGM_MUX9
EMAC_CLK_TS
25
2
0
24
8
1...64
1...64
1...64
0
2
MUX_10_DC_0[DIV]
QSPI_SFCK
9
1...8
EMAC_MII_RX_CLK
EMAC_MII_RMII_TX_CLK
22
0
2
MUX_2_DC_0[DIV]
MC_CGM_MUX2
STM1_CLK
1...2
Not available on
the S32K314
QSPI_MEM_CLK
MUX_0_DC_6[DIV]
1...8
Only
FLEXCAN[3]_PE_CLK
is available on the
S32K322, S32K341,
and S32K342 
LBIST_CLK
MUX_0_DC_5[DIV]
1...8
24
25
MC_CGM_MUX10
SXOSC
(32 kHz)
SXOSC_CLK
OSC32K_XTAL
OSC32K_EXTAL
22
0
2
MUX_4_DC_0[DIV]
MC_CGM_MUX4
1...4
FLEXCAN[3:5]_PE_CLK
0
4
4
3
1
2
RTC_CLK
Figure 69. S32K344, S32K324, S32K314, S32K322, S32K341, and S32K342 clock system diagram
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
915 / 5251


---
# 페이지 14

24.3.12 S32K312 clock system diagram
1...16
PLLDIG.PLLODIV_0[DIV]
1...2
MUX_1_DC_0[DIV]
PLLDIG.PLLODIV_1[DIV]
FIRC_CLK
FXOSC_CLK
SIRC_CLK
PLL_PHI0_CLK
FIRC
(48 MHz)
RTC.RTCC[CLKSEL]
3
0
22
0
2
PCFS
MC_CGM_MUX0
MUX_0_DC_4[DIV]
MUX_0_DC_3[DIV]
MUX_0_DC_2[DIV]
MUX_0_DC_1[DIV]
MUX_0_DC_0[DIV]
CORE_CLK
AIPS_PLAT_CLK
AIPS_SLOW_CLK
HSE_CLK
DCM_CLK
STM0_CLK
MUX_3_DC_0[DIV]
MC_CGM_MUX3
FLEXCAN[0:2]_PE_CLK
MC_CGM_MUX5
MC_CGM_MUX6
8
0
22
0
2
MUX_6_DC_0[DIV]
CLKOUT_RUN
MC_CGM_MUX11
RTC
MUX_5_DC_0[DIV]
CLKOUT_STANDBY
0
8
2
MUX_11_DC_0[DIV]
TRACE_CLK
TCK
23
FXOSC
(8-40 MHz)
XTAL
EXTAL
SIRC
(32 kHz)
CMU with FXOSC reference
CMU with FIRC reference
1
0
2
1
2
÷2
÷16
9
1...4
1...8
1...8
1...8
1...8
1...16
1...8
1...8
1...64
MC_CGM
PLL_PHI1_CLK
1...16
HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL]
JTAG_TCK/SWD_CLK
CMU_FM_1
CMU_FM_2
CMU_FC_0
CMU_FC_3
CMU_FC_4
CMU_FC_5
S32K3xx
VCO_CLK
PLL
1...63
PLLDIG.PLLDV[ODIV2]
23
22
19
16
9
8
2
1
0
PLLODIV2_CLK
MC_CGM_MUX1
÷2
.div-by-2
SXOSC
(32 kHz)
SXOSC_CLK
OSC32K_XTAL
OSC32K_EXTAL
22
0
2
MUX_4_DC_0[DIV]
MC_CGM_MUX4
1...4
FLEXCAN[3:5]_PE_CLK
0
4
4
3
1
2
RTC_CLK
Figure 70. S32K312 clock system diagram
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
916 / 5251


---
# 페이지 15

24.3.13 S32K310 and S32K311 clock system diagram
1...16
PLLDIG.PLLODIV_0[DIV]
1...2
MUX_1_DC_0[DIV]
PLLDIG.PLLODIV_1[DIV]
FIRC_CLK
FXOSC_CLK
SIRC_CLK
PLL_PHI0_CLK
FIRC
(48 MHz)
RTC.RTCC[CLKSEL]
3
0
22
0
2
PCFS
MC_CGM_MUX0
MUX_0_DC_4[DIV]
MUX_0_DC_3[DIV]
MUX_0_DC_2[DIV]
MUX_0_DC_1[DIV]
MUX_0_DC_0[DIV]
CORE_CLK
AIPS_PLAT_CLK
AIPS_SLOW_CLK
HSE_CLK
DCM_CLK
STM0_CLK
MUX_3_DC_0[DIV]
MC_CGM_MUX3
FLEXCAN[0:2]_PE_CLK
MC_CGM_MUX5
MC_CGM_MUX6
8
0
22
0
2
MUX_6_DC_0[DIV]
CLKOUT_RUN
MC_CGM_MUX11
RTC
MUX_5_DC_0[DIV]
CLKOUT_STANDBY
0
8
2
MUX_11_DC_0[DIV]
TRACE_CLK
TCK
23
FXOSC
(8-40 MHz)
XTAL
EXTAL
SIRC
(32 kHz)
CMU with FXOSC reference
CMU with FIRC reference
1
0
2
1
2
÷2
÷16
9
1...4
1...8
1...8
1...8
1...8
1...16
1...8
1...8
1...64
MC_CGM
PLL_PHI1_CLK
1...16
HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL]
JTAG_TCK/SWD_CLK
CMU_FM_1
CMU_FM_2
CMU_FC_0
CMU_FC_3
CMU_FC_4
CMU_FC_5
S32K3xx
VCO_CLK
PLL
1...63
PLLDIG.PLLDV[ODIV2]
23
22
19
16
9
8
2
1
0
PLLODIV2_CLK
MC_CGM_MUX1
÷2
.div-by-2
3
1
2
3
1
2
RTC_CLK
PLLDIG.PLLCLKMUX[REFCLKSEL]
0
1
Figure 71. S32K310 and S32K311 clock system diagram
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
917 / 5251


---
# 페이지 16

24.4 Clock sources
24.4.1 Introduction
The chip contains the following clock sourcing modules:
• FIRC
— FIRC_CLK is the default system clock source.
• SIRC
• PLL
• FXOSC
• SXOSC (not available in 100-HDQFP and 48-pin LQFP packages)
The following list shows some of the clock system features:
• All clock sources support application software configurability for enabling or disabling. [3]
• All clock sources, except SXOSC_CLK, are initialized to their default state on functional reset.
• The SXOSC_CLK supports RTC applications across functional reset and is reset on destructive reset.
Only SIRC_CLK and FIRC_CLK are enabled out of reset and are enabled on any functional reset. The other clock sources are 
disabled on reset.
24.4.1.1
Chip clock sources
Table 117. Chip clock sources
Clock source
Divider
Default
state
Reset
Uses
FIRC_CLK
(48 MHz)
1, 2, 16
On
POR (enabled on functional and 
destructive reset)
POR assertion - FIRC_CLK 
disabled asynchronously
POR deassertion - 
FIRC_CLK enabled
• Boot clock
• Default system clock source
• Safe clock for safety modules FCCU 
and FOSU
• SIUL2 filter clock
• MC_RGM clock source
PLL_PHIn_CLK
(25-480 MHz)
1...16
Off
Functional (disabled on functional 
reset)
• Optional system clock source
• Communication modules (FlexCAN, 
EMAC/GMAC, QuadSPI, and so on)
PLL_AUX_PHIn_
CLK (25-250 
MHz)
1...32
Off
Functional (disabled on functional 
reset)
• Communication modules (EMAC/
GMAC, uSDHC, SAI, and QuadSPI)
FXOSC_CLK
(8-40 MHz)
—
Off
Functional (disabled on functional 
reset)
• Reference clock source for PLL
• Communication modules (FlexCAN, 
EMAC/GMAC, QuadSPI, and so on)
Table continues on the next page...
[3] FIRC_CLK and SIRC_CLK cannot be disabled during Run mode.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
918 / 5251


---
# 페이지 17

Table 117. Chip clock sources (continued)
Clock source
Divider
Default
state
Reset
Uses
SXOSC_CLK1
(32.768 KHz)
—
Off
Destructive (disabled on 
destructive reset)
• RTC source for operation across 
functional reset
SIRC_CLK
(32 KHz)
—
On
POR (enabled on functional reset)
• Safe clock along with FIRC_CLK
• SWT clock source
• POR_WDG source clock
1. See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this module's 
availability on your chip variant.
24.4.2 Chip input clocks
Table 118. Chip input clocks
Pin
Description
XTAL
FXOSC crystal pins
EXTAL
OSC32K_XTAL
SXOSC crystal pins1
OSC32K_EXTAL
EMAC_MII_RMII_TX_CLK
EMAC transmitter clock/EMAC RMII clock1
GMAC_MII_RMII_RGMII_TX_CLK
GMAC transmitter clock/GMAC RMII clock1
GMAC0_MII_RMII_RGMII_TX_CL
K
GMAC0 transmitter clock/GMAC0 RMII clock1
GMAC1_MII_RMII_RGMII_TX_CL
K
GMAC1 transmitter clock/GMAC1 RMII clock1
EMAC_MII_RX_CLK
EMAC receiver clock1
GMAC_MII_RGMII_RX_CLK
GMAC receiver clock1
GMAC0_MII_RGMII_RX_CLK
GMAC0 receiver clock1
GMAC1_MII_RGMII_RX_CLK
GMAC1 receiver clock1
JTAG_TCLK/SWD_CLK
JTAG/SWD clock
SAIn_MCLK
SAIn clock in slave mode1
SAIn_BCLK
SAIn bit clock in slave mode1
LPSPIn_SCK
LPSPIn serial clock in slave mode
LPI2Cn_SCL
LPI2Cn clock in slave mode
LPI2Cn_SCLS
LPI2Cn secondary clock in slave mode
1. See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this module's 
availability on your chip variant.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
919 / 5251


---
# 페이지 18

24.4.3 Chip output clocks
Table 119. Chip output clocks
Pin
Description
CLKOUT_RUN
Available during Run mode, unavailable during Standby mode
CLKOUT_STANDBY
Available during both Run and Standby modes
LPSPIn_SCK
LPSPIn serial clock in master mode
LPI2Cn_SCL
LPI2Cn clock in master mode
LPI2Cn_SCLS
LPI2Cn secondary clock in master mode
EMAC_MII_RMII_MDC
EMAC clock for control data transfer to PHY 1
GMAC_MII_RMII_RGMII_MDC
GMAC clock for control data transfer to PHY1
GMAC0_MII_RMII_RGMII_MDC
GMAC0 clock for control data transfer to PHY1
GMAC1_MII_RMII_RGMII_MDC
GMAC1 clock for control data transfer to PHY1
EMAC_MII_RMII_TX_CLK
EMAC transmit clock1
GMAC_MII_RMII_RGMII_TX_CLK
GMAC transmit clock1
GMAC0_MII_RMII_RGMII_TX_CL
K
GMAC0 transmit clock1
GMAC1_MII_RMII_RGMII_TX_CL
K
GMAC1 transmit clock1
TRACE_ETM_CLKOUT
ETM trace clock2
SAIn_BCLK
SAIn bit clock in master mode1
QuadSPI_SCKFA
QuadSPI serial clock for serial flash device1
uSDHC_PER_CLK
uSDHC serial clock1
1. See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this module's 
availability on your chip variant.
2. See the section "Interfaces supported in S32K3 family" in this reference manual's "Debug Subsystem" chapter for details 
on this module's availability on your chip variant.
24.4.4 Fast internal RC oscillator (FIRC)
The chip has an FIRC with the following features:
• Acts as the system clock source on power-up and after any reset event.
• Acts as the chip's safe clock for safety-relevant applications.
• Is always enabled in Run mode and can be optionally enabled in Standby mode.
• Used as clock source for the following:
— MC_RGM
— FCCU and FOSU
— SIUL2 filters
24.4.4.1
FIRC failure detection
The FIRC_CLK is the safe clock source used as the FCCU and FOSU clock source. The chip supports FIRC_CLK failure detection 
and recovery by the mechanisms described in the following cases:
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
920 / 5251


---
# 페이지 19

• Case 1 - FIRC_CLK not used as system clock and goes out of range:
— CMU_FM_1 continuously measures the FIRC_CLK clock frequency using FXOSC_CLK as the reference. On 
each metering window completion, CMU_FM_1 asserts an interrupt (if configured, CMU_FM_1.IER[FMCIE] 
is 1). You store a configured reference clock count CMU_FM_1.RCCR[REF_CNT] (for example, number of 
FXOSC_CLK cycles in metering window). Your application software checks the FIRC_CLK clock counts by 
reading CMU_FM_1.SR[MET_CNT].
— In the event FIRC_CLK goes out of range, the application software detects the frequency variation after the 
subsequent metering window by checking CMU_FM_1.SR[MET_CNT] and takes necessary action by either of the 
recommended options:
◦SBC-driven power cycle: The chip indicates the SBC (through GPIO toggle, QuadSPI communication, and so on, 
as configured by your software and the connectivity to the SBC) to initiate a power cycle sequence.
◦Application software-driven functional reset: The chip executes a functional reset as configured by your 
application software.
• Case 2 - FIRC_CLK not used as system clock and fails (becomes stuck):
— CMU_FM_1 continuously measures the FIRC_CLK frequency with FXOSC_CLK as the reference. Application software 
must check FIRC_CLK after a defined time limit by reading CMU_FM_1.SR[MET_CNT] and CMU_FM_1.SR[FMTO].
— If there is an FIRC_CLK failure, the CMU_FM_1 writes a 1 to the timeout status flag CMU_FM_1.SR[FMTO].
— When CMU_FM_1.SR[FMTO] is 1, application software takes necessary action by an SBC-driven power cycle wherein 
the chip provides an indication to the SBC (through GPIO toggle, QuadSPI communication, and so on). The SBC then 
initiates a power cycle sequence.
• Case 3 - FIRC_CLK used as system clock and goes out of range or fails (becomes stuck):
— CMU_FC_3 continuously monitor the system clock nodes with FXOSC_CLK as reference for FLL or FHH events.
— CMU_FC_4 and CMU_FC_5 continuously monitor the system clock nodes with FIRC_CLK as reference for FLL or 
FHH events.
— In the event of FIRC_CLK failure (when FIRC_CLK acts as the system clock source), these CMUs report the FLL event, 
acting as a destructive reset source.
— The system then undergoes the reset sequence, during which the FIRC_CLK is reinitialized.
— The MC_RGM.DES fields indicate the source of the reset event.
— In addition, CMU_FM_1 monitors FIRC_CLK. If the application software is not able to service the CMU_FM_1 interrupt 
before POR_WDG timeout, POR_WDG treats this as a critical FIRC_CLK failure and initiates a POR_WDG recovery. 
Therefore, you must ensure that, if enabled, the CMU_FM_1 interrupt must be serviced within the POR_WDG 
timeout duration.
24.4.4.2
FIRC_CLK behavior in Standby mode
FIRC_CLK can be optionally enabled in Standby mode by configuring FIRC.STDBY_ENABLE[STDBY_EN].
When the PMC acknowledges the Standby mode entry, the FIRC_CLK switches from the On state to the Standby mode 
configuration selected by the FIRC.STDBY_ENABLE[STDBY_EN] configuration. On wakeup from Standby mode, the FIRC_CLK 
configuration switches from the Standby mode configured state to the On state.
The FIRC at 3 MHz is meant to be used with the Low Speed Run Mode only. If the chip needs to enter Standby mode, then the 
FIRC can be configured to 48MHz or 24MHz with the FIRC_DIV_SEL as '0b11' or '0b00', or '0b01' before entering Standby mode. 
After exiting the Standby mode, the FIRC can be changed to 3 MHz if desired.
 
During the functional reset sequence, the analog blocks are loaded with the configured trimmed values. During this 
step, the FIRC will appear as momentarily disabled, as shown in the "Reset overview" chapter.
  NOTE  
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
921 / 5251


---
# 페이지 20

24.4.5 SIRC
The chip has an SIRC having the following features:
• Is always enabled in Run mode and can be optionally enabled in Standby mode. Having the SIRC always enabled 
improves system robustness by ensuring that a clock is always available for various SWTs when reducing the chip power 
consumption in Standby mode.
• Used as clock source for the following:
— SWT
— POR_WDG
24.4.5.1
SIRC failure detection
Like the FIRC_CLK, the SIRC_CLK is a safe clock for the design and it is used as a clock source for SWTs and POR_WDOG and 
therefore it is important to detect SIRC failure and ensure its recovery. The chip supports SIRC_CLK failure detection and recovery 
by the mechanism described below.
• Case 1 - SIRC_CLK goes out of range:
— CMU_FM_2 continuously measures the SIRC_CLK clock frequency with FXOSC_CLK as reference. On each metering 
window completion, the CMU_FM_2 raises an interrupt. The application software checks the SIRC clock counts by 
CMU_FM_2.SR[MET_CNT] with respect to the reference clock counts CMU_FM_2.RCCR[REF_CNT].
— In the event of clock going out of range, the application software detects the frequency variation after the 
subsequent metering window by checking CMU_FM_2.SR[MET_CNT] and takes necessary action by either of the 
recommended options:
1. SBC-driven power cycle. The chip gives an indication to the SBC (through GPIO toggle, QuadSPI 
communication, and so on.). The SBC then initiates a power cycle sequence.
2. SW-driven functional reset. The chip executes a functional reset by application software.
• Case 2 - SIRC_CLK fails (becomes stuck):
— CMU_FM_2 continuously measures the SIRC clock frequency with FXOSC_CLK as reference. Application 
software needs to check this reference after a predefined time by checking CMU_FM_2.SR[MET_CNT] 
and CMU_FM_2.SR[FMTO].
— In the event of SIRC_CLK clock failure, the CMU_FM_2 writes 1 to the timeout status flag field in its status register, 
namely, CMU_FM_2.SR[FMTO].
— When CMU_FM_2.SR[FMTO] is 1, the application software takes necessary action by either of the 
recommended options:
1. SBC-driven power cycle: The chip gives an indication to the SBC (through GPIO toggle, QuadSPI 
communication, and so on). The SBC then initiates a power cycle sequence.
2. Application software-driven functional reset: User application software executes a functional reset.
24.4.5.2
SIRC behavior in Standby mode
SIRC can optionally be enabled in Standby mode by configuring SIRC.MISCELLANEOUS_IN[STANDBY_ENABLE].
When PMC acknowledges the Standby mode entry, the SIRC switches from the On state to the standby configuration selected 
by SIRC.MISCELLANEOUS_IN[STANDBY_ENABLE] configuration. On wake-up from Standby mode, the SIRC configuration 
switches back from the standby-configured state to the On state.
 
When the trims are being applied, the SIRC will appear as momentarily disabled similar to FIRC, as shown in 
section "Signal level reset flow timing".
  NOTE  
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
922 / 5251


---
# 페이지 21

24.4.6 FXOSC
The chip supports an 8–40 MHz fast crystal oscillator which has following features:
• Acts as the reference for PLL.
• Supports crystal input mode and bypass mode if using an external oscillator.
• Acts as a clock source for communication modules:
— FlexCAN
— QuadSPI[4]
— EMAC (EMAC_CLK_TS)[4]
— GMAC (GMAC_CLK_TS)[4]
24.4.7 SXOSC
The chip supports a slow crystal oscillator (SXOSC) which has the following features[5]:
• Supports crystal input mode.
• Bypass mode not supported.
• Acts as a clock source for RTC. As SXOSC is not affected by functional reset, it supports RTC operation across functional 
reset. SXOSC is only reset on destructive reset.
24.4.8 PLL
The chip contains up to two PLL to provide precision clock source with the following features:
• Optional system clock source (in high performance applications)
• System clock source in safety applications
• Can be used as clock source for communication modules, when configured as system clock source:
— FlexCAN (in SYNC mode operation)
— EMAC[6]
— GMAC[6]
— QuadSPI[6]
— LPSPI
— LPI2C
— FlexIO
— LPUART
• Supports frequency modulation
• Contains lock status monitoring logic which supports loss-of-lock indication
At power-up, the second PLL (PLL_AUX) will be disabled. It will be up to the application software to enable it when needed. In 
case of a loss of lock after lock has been acquired, PLL_AUX will generate a loss of lock flag. The default reaction of loss of lock 
[4] See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this module's 
availability on your chip variant.
[5] See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this module's 
availability on your chip variant.
[6] See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this module's 
availability on your chip variant.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
923 / 5251


---
# 페이지 22

flag from the Second PLL will be an interrupt. The reaction of a loss of lock from the Second PLL will be optionally configured as 
a functional reset, controlled by GPR.
The Second PLL supports a clock output frequency of up to 250MHz (nominal), for the FXOSC input frequencies.
 
See "PLL Digital Interface (PLLDIG)" for PLL configuration details. See the S32K3xx Data Sheet for 
PLL specifications.
  NOTE  
24.4.8.1
PLL configurations
The PLL output predivider frequency depends on the PLLDIG.PLLDV[RDIV] and PLLDIG.PLLDV[MFI] configurations. The PLL 
VCO clock can be divided further by configuring PLLDIG.PLLODIV_0[DIV] for PLL_PHI0_CLK and PLLDIG_PLLODIV_1[DIV] for 
PLL_PHI1_CLK (see the "PLL Digital Interface (PLLDIG)" chapter for configuration details).
24.4.8.1.1
PLL configuration sequence
Before enabling the PLL, you must enable FXOSC_CLK and wait until it is stable. FXOSC.STAT[OSC_STAT] must be monitored 
to determine the FXOSC_CLK status.
To disable the PLL, the application software must disable PLL first and only then disable FXOSC (if required).
For S32K311 and S32K310, FIRC_DIV2_CLK is also available as a PLL reference.
24.4.9 Chip clock outputs
The chip supports two CLKOUT_x pins for allowing viewing of some internal clocks as follows:
• CLKOUT_STANDBY
— Used for showing clocks available in Run and Standby modes.
• CLKOUT_RUN
— Used for showing only Run mode clocks.
See the Clockout overview section and the "Clock Generation Module (MC_CGM)" chapter for details on available clocks 
and configuration.
 
The CLKOUT_STANDBY registers are latched when the chip enters Standby mode and are reset in Standby mode 
sequence. Therefore, the CLKOUT_STANDBY signal needs to be reconfigured on Standby mode exit.
  NOTE  
 
CLKOUT_STANDBY is available on two pads GPIO[12] and GPIO[138] but CLKOUT across functional reset and 
standby is supported only on GPIO[12] and OBE(output buffer enable) is controlled by DCM GPR bit. Please refer 
to DCMRWP1[3] bit for detail.
  NOTE  
24.5 MC_CGM
The MC_CGM controls the clock functionality of the chip. See the Clock Generation Module (MC_CGM) chapter for details on 
MC_CGM clocking controls.
24.5.1 MC_CGM clock multiplexer types
In this chip, CLKOUT_RUN, CLKOUT_STANDBY, and TRACE_CLK multiplexers are software-controlled multiplexers. The 
rest are hardware-controlled multiplexers (see the "Clock Generation Module (MC_CGM)" chapter for details on software and 
hardware multiplexers).
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
924 / 5251


---
# 페이지 23

24.5.2 MC_CGM clock multiplexers for S32K310, S32K311, and S32K312
Table 120. MC_CGM clock multiplexers for S32K310, S32K311, and S32K312
Clock mux
Register description
Source inputs 1
Register
Divider output
Clock mux 0
Select Control
FIRC_CLK
PLL_PHI0_CLK
MUX_0_CSC
—
Select Status
MUX_0_CSS
Divider 0 Control
—
MUX_0_DC_0
CORE_CLK
Divider 1 Control
MUX_0_DC_1
AIPS_PLAT_CLK
Divider 2 Control
MUX_0_DC_2
AIPS_SLOW_CLK
Divider 3 Control
MUX_0_DC_3
HSE_CLK
Divider 4 Control
MUX_0_DC_4
DCM_CLK
Clock mux 1
Select Control
FIRC_CLK
FXOSC_CLK
AIPS_PLAT_CLK
MUX_1_CSC
—
Select Status
MUX_1_CSS
Divider 0 Control
—
MUX_1_DC_0
STM0_CLK
Clock mux 3
Select Control
FIRC_CLK
FXOSC_CLK
AIPS_PLAT_CLK
MUX_3_CSC
—
Select Status
MUX_3_CSS
Divider 0 Control
—
MUX_3_DC_0
FLEXCAN0_PE_CLK
FLEXCAN1_PE_CLK
FLEXCAN2_PE_CLK
Clock mux 4 2
Select Control
FIRC_CLK
FXOSC_CLK
AIPS_PLAT_CLK
MUX_4_CSC
—
Select Status
MUX_4_CSS
Divider 0 Control
—
MUX_4_DC_0
FLEXCAN3_PE_CLK
FLEXCAN4_PE_CLK
FLEXCAN5_PE_CLK
Clock mux 5
Select Control
FIRC_CLK
SIRC_CLK
FXOSC_CLK
SXOSC_CLK3
AIPS_SLOW_CLK
MUX_5_CSC
—
Select Status
MUX_5_CSS
Divider 0 Control
—
MUX_5_DC_0
CLKOUT_STANDBY
Clock mux 6
Select Control
FIRC_CLK
SIRC_CLK
FXOSC_CLK
SXOSC_CLK3
PLL_PHI0_CLK
MUX_6_CSC
—
Select Status
MUX_6_CSS
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
925 / 5251


---
# 페이지 24

Table 120. MC_CGM clock multiplexers for S32K310, S32K311, and S32K312 (continued)
Clock mux
Register description
Source inputs 1
Register
Divider output
PLL_PHI1_CLK
CORE_CLK
HSE_CLK
AIPS_PLAT_CLK
AIPS_SLOW_CLK
Divider 0 Control
—
MUX_6_DC_0
CLKOUT_RUN
Clock mux 11
Select Control
FIRC_CLK
FXOSC_CLK
PLL_PHI0_CLK
PLL_PHI1_CLK
MUX_11_CSC
—
Select Status
MUX_11_CSS
Divider 0 Control
—
MUX_11_DC_0
TRACE_CLK
1. The default clock selected for all clock mux selectors is FIRC_CLK (out of reset).
2. Clock mux 4 and FLEXCAN[3:5]_PE_CLK are not available on S32K310 and S32K311.
3. SXOSC as source for clock mux 5 is not available on S32K310 and S32K311.
24.5.3 MC_CGM clock multiplexers (excluding S32K310, S32K311, and S32K312)
Table 121. MC_CGM clock multiplexers (excluding S32K310, S32K311, and S32K312)
Clock mux
Register description
Source inputs 1
Register
Divider output
Clock mux 0
Select Control
FIRC_CLK
PLL_PHI0_CLK
MUX_0_CSC
—
Select Status
MUX_0_CSS
Divider 0 Control
—
MUX_0_DC_0
CORE_CLK
Divider 1 Control
MUX_0_DC_1
AIPS_PLAT_CLK
Divider 2 Control
MUX_0_DC_2
AIPS_SLOW_CLK
Divider 3 Control
MUX_0_DC_3
HSE_CLK
Divider 4 Control
MUX_0_DC_4
DCM_CLK
Divider 5 Control
MUX_0_DC_5
LBIST_CLK
Divider 6 Control
MUX_0_DC_6
QSPI_MEM_CLK
Divider 7 Control2
MUX_0_DC_7
CM7_CORE_CLK
Clock mux 1
Select Control
FIRC_CLK
FXOSC_CLK
AIPS_PLAT_CLK
MUX_1_CSC
—
Select Status
MUX_1_CSS
Divider 0 Control
—
MUX_1_DC_0
STM0_CLK
Clock mux 2
Select Control
FIRC_CLK
FXOSC_CLK
AIPS_PLAT_CLK
MUX_2_CSC
—
Select Status
MUX_2_CSS
Divider 0 Control
—
MUX_2_DC_0
STM1_CLK
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
926 / 5251


---
# 페이지 25

Table 121. MC_CGM clock multiplexers (excluding S32K310, S32K311, and S32K312) (continued)
Clock mux
Register description
Source inputs 1
Register
Divider output
Clock mux 3
Select Control
FIRC_CLK
FXOSC_CLK
AIPS_PLAT_CLK
CORE_CLK3
MUX_3_CSC
—
Select Status
MUX_3_CSS
Divider 0 Control
—
MUX_3_DC_0
FLEXCAN0_PE_CLK
FLEXCAN1_PE_CLK
FLEXCAN2_PE_CLK
Clock mux 4
Select Control
FIRC_CLK
FXOSC_CLK
AIPS_PLAT_CLK
CORE_CLK3
MUX_4_CSC
—
Select Status
MUX_4_CSS
Divider 0 Control
—
MUX_4_DC_0
FLEXCAN3_PE_CLK
FLEXCAN4_PE_CLK4
FLEXCAN5_PE_CLK4
FLEXCAN6_PE_CLK6
FLEXCAN7_PE_CLK6
Clock mux 5
Select Control
FIRC_CLK
SIRC_CLK
FXOSC_CLK
SXOSC_CLK
AIPS_SLOW_CLK
MUX_5_CSC
—
Select Status
MUX_5_CSS
Divider 0 Control
—
MUX_5_DC_0
CLKOUT_STANDBY
Clock mux 6
Select Control
FIRC_CLK
SIRC_CLK
FXOSC_CLK
SXOSC_CLK
PLL_PHI0_CLK
PLL_PHI1_CLK
PLL_AUX_PHI0_CLK6
PLL_AUX_PHI1_CLK6
PLL_AUX_PHI2_CLK3
CORE_CLK
HSE_CLK
AIPS_PLAT_CLK
AIPS_SLOW_CLK
GMAC_MII_RMII_RGMII_
TX_CLK3
GMAC_MII_RGMII_RX_C
LK3
GMAC0_MII_RMII_RGMII
_TX_CLK2
GMAC0_MII_RGMII_RX_
MUX_6_CSC
—
Select Status
MUX_6_CSS
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
927 / 5251


---
# 페이지 26

Table 121. MC_CGM clock multiplexers (excluding S32K310, S32K311, and S32K312) (continued)
Clock mux
Register description
Source inputs 1
Register
Divider output
CLK2
EMAC_MII_RMII_TX_CL
K5
EMAC_MII_RX_CLK5
Divider 0 Control
—
MUX_6_DC_0
CLKOUT_RUN
Clock mux 75
Select Control
FIRC_CLK
EMAC_MII_RMII_TX_CL
K
EMAC_MII_RX_CLK
MUX_7_CSC
—
Select Status
MUX_7_CSS
Divider 0 Control
—
MUX_7_DC_0
EMAC_CLK_RX
Clock mux 76
Select Control
FIRC_CLK
PLL_PHI0_CLK3
PLL_AUX_PHI0_CLK3
GMAC0_MII_RMII_RGMII
_TX_CLK2
GMAC_MII_RGMII_RX_C
LK3
GMAC_MII_RMII_RGMII_
TX_CLK3
MUX_7_CSC
—
Select Status
MUX_7_CSS
Divider 0 Control
—
MUX_7_DC_0
GMAC0_CLK_RX2
GMAC_CLK_RX3
Clock mux 85
Select Control
FIRC_CLK
EMAC_MII_RMII_TX_CL
K
MUX_8_CSC
—
Select Status
MUX_8_CSS
Divider 0 Control
—
MUX_8_DC_0
EMAC_CLK_TX
Clock mux 86
Select Control
FIRC_CLK
PLL_PHI0_CLK3
PLL_AUX_PHI0_CLK6 
GMAC0_MII_RMII_RGMII
_TX_CLK2
GMAC_MII_RGMII_RX_C
LK3
GMAC_MII_RMII_RGMII_
TX_CLK3
MUX_8_CSC
—
Select Status
MUX_8_CSS
Divider 0 Control
—
MUX_8_DC_0
GMAC_CLK_TX3
GMAC0_CLK_TX2
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
928 / 5251


---
# 페이지 27

Table 121. MC_CGM clock multiplexers (excluding S32K310, S32K311, and S32K312) (continued)
Clock mux
Register description
Source inputs 1
Register
Divider output
Clock mux 95
Select Control
FIRC_CLK
FXOSC_CLK
PLL_PHI0_CLK
EMAC_MII_RMII_TX_CL
K
EMAC_MII_RX_CLK
MUX_9_CSC
—
Select Status
MUX_9_CSS
Divider 0 Control
—
MUX_9_DC_0
EMAC_CLK_TS
Clock mux 96
Select Control
FIRC_CLK
FXOSC_CLK
PLL_PHI0_CLK3
GMAC_MII_RMII_RGMII_
TX_CLK3
GMAC_MII_RGMII_RX_C
LK3
PLL_AUX_PHI0_CLK 
GMAC0_MII_RMII_RGMII
_TX_CLK2
GMAC0_MII_RGMII_RX_
CLK2
GMAC1_MII_RMII_RGMII
_TX_CLK2
GMAC1_MII_RGMII_RX_
CLK2
MUX_9_CSC
—
Select Status
MUX_9_CSS
Divider 0 Control
—
MUX_9_DC_0
GMAC_CLK_TS
Clock mux 10
Select Control
FIRC_CLK
FXOSC_CLK
PLL_PHI1_CLK
PLL_AUX_PHI0_CLK6
MUX_10_CSC
—
Select Status
MUX_10_CSS
Divider 0 Control
—
MUX_10_DC_0
QSPI_SFCK
QSPI_2XSFIF3
Clock mux 11
Select Control
FIRC_CLK
FXOSC_CLK
PLL_PHI0_CLK
PLL_PHI1_CLK
PLL_AUX_PHI0_CLK6
MUX_11_CSC
—
Select Status
MUX_11_CSS
Divider 0 Control
—
MUX_11_DC_0
TRACE_CLK
Clock mux 12
Reserved
Clock mux 136
Select Control
AIPS_PLAT_CLK
FXOSC_CLK
FIRC_CLK
MUX_13_CSC
—
Select Status
MUX_13_CSS
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
929 / 5251


---
# 페이지 28

Table 121. MC_CGM clock multiplexers (excluding S32K310, S32K311, and S32K312) (continued)
Clock mux
Register description
Source inputs 1
Register
Divider output
Divider 0 Control
—
MUX_13_DC_0
STM2_CLK
Clock mux 143
Select Control
FIRC_CLK
FXOSC_CLK
PLL_PHI1_CLK
PLL_AUX_PHI2_CLK
MUX_14_CSC
—
Select Status
MUX_14_CSS
Divider 0 Control
—
MUX_14_DC_0
uSDHC_PER_CLK
Clock mux 152
Select Control
GMAC1_MII_RMII_RGMII
_TX_CLK
FIRC_CLK
MUX_15_CSC
—
Select Status
MUX_15_CSS
Divider 0 Control
—
MUX_15_DC_0
GMAC1_CLK_RX
Clock mux 162
Select Control
GMAC1_MII_RMII_RGMII
_TX_CLK
FIRC_CLK
MUX_16_CSC
—
Select Status
MUX_16_CSS
Divider 0 Control
—
MUX_16_DC_0
GMAC1_CLK_TX
Clock mux 17
Reserved
Clock mux 182
Select Control
AIPS_PLAT_CLK
FIRC_CLK
FXOSC_CLK
MUX_18_CSC
—
Select Status
MUX_18_CSS
Divider 0 Control
—
MUX_18_DC_0
STM3_CLK
Clock mux 192
Select Control
PLL_AUX_PHI1_CLK
FIRC_CLK
MUX_19_CSC
—
Select Status
MUX_19_CSS
Divider 0 Control
—
MUX_19_DC_0
AES_1us_CLK
Clock mux 207
Select Control
AIPS_PLAT_CLK 
FIRC_CLK FXOSC_CLK
MUX_20_CSC
—
Select Status
MUX_20_CSS
Divider 0 Control
—
MUX_20_DC_0
FLEXCAN[8:11]_PE_CLK
1. The default clock selected for all clock mux selectors is FIRC_CLK (out of reset).
2. Available only in S32K388 and S32K389.
3. For S32K358, S32K348, S32K338, and S32K328 only.
4. FLEXCAN[4:5]_PE_CLK are not available on the S32K342, S32K322, and S32K341.
5. For S32K314, S32K322, S32K324, S32K341, S32K342, and S32K344 only.
6. For S32K388 and S32K389 only.
7. Available only in S32K389.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
930 / 5251


---
# 페이지 29

24.5.4 MC_CGM clock sources mapping
Table 122. MC_CGM clock sources mapping
Clock selector index 1
MC_CGM clock source
Clock source
0
clk_src_0
FIRC_CLK
1
clk_src_1
SIRC_CLK
2
clk_src_2
FXOSC_CLK
3
Reserved
Reserved
4
clk_src_4
SXOSC_CLK 2
5–7
Reserved
Reserved
8
clk_src_8
PLL_PHI0_CLK
9
clk_src_9
PLL_PHI1_CLK
10–11
Reserved
Reserved
12
clk_src_12
PLL_AUX_PHI0_CLK3
13
clk_src_13
PLL_AUX_PHI1_CLK3
14
clk_src_14
PLL_AUX_PHI2_CLK4
15
Reserved
Reserved
16
clk_src_16
CORE_CLK
17–18
Reserved
Reserved
19
clk_src_19
HSE_CLK
20–21
Reserved
Reserved
22
clk_src_22
AIPS_PLAT_CLK
23
clk_src_23
AIPS_SLOW_CLK
24
clk_src_24
EMAC_MII_RMII_TX_CLK5
GMAC_MII_RMII_RGMII_TX_CLK4 
GMAC0_MII_RMII_RGMII_TX_CLK6
25
clk_src_25
EMAC_MII_RX_CLK 5
GMAC_MII_RGMII_RX_CLK4
GMAC0_MII_RGMII_RX_CLK6
26–28
Reserved
Reserved
29
clk_src_29
GMAC1_MII_RGMII_RX_CLK6
30
clk_src_30
GMAC1_MII_RMII_RGMII_TX_CLK6
31–50
Reserved
Reserved
1. All clock selector indexes not shown are reserved.
2. SXOSC_CLK is not available on S32K310 and S32K311.
3. Applicable for S32K388, S32K389, S32K358, S32K348, S32K338, and S32K328 only.
4. Applicable for S32K358, S32K348, S32K338, and S32K328 only.
5. Applicable for S32K344, S32K324, S32K314, S32K322, S32K341, and S32K342.
6. Applicable for S32K388 and S32K389 only.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
931 / 5251


---
# 페이지 30

 
Peripheral input clock source switching must not occur while peripheral is working.
  NOTE  
24.6 Peripheral clocking
The module clocking diagrams for the peripherals are shown in the following subsections (see Peripheral clock gating for 
peripheral clock gating possibilities).
24.6.1 Module clocking
The following sections show how the chip modules use MODULE_CLK and REG_INTF_CLK to control their functionality.
24.6.1.1
Communication modules
Figure 72 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 123 shows the REG_INTF_CLK and 
MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the 
same source for REG_INTF_CLK as used by MODULE_CLK.
See REG_INTF_CLK
and MODULE_CLK
columns in table below
MODULE_CLK
Module
REG_INTF_CLK
}
Figure 72. Communication module clocks
Table 123. Communication module clocking
Module
MODULE_CLK
FlexCAN
See FlexCANn clocking.
LPI2C
See LPI2Cn clocking.
GMAC
See GMAC clocking.
EMAC
See EMAC clocking.
LPSPI
See LPSPIn clocking.
LPUART
See LPUARTn clocking
FlexIO
See FlexIO clocking.
QuadSPI
See QuadSPI clocking.
SAI
See SAIn clocking.
uSDHC
See uSDHC clocking
24.6.1.1.1
FlexCANn clocking
The figure below shows the FlexCANn clocking.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
932 / 5251


---
# 페이지 31

FlexCANn
AIPS_PLAT_CLK
CAN_CHI_CLK
CAN_PE_CLK
MODULE_CLK
REG_INTF_CLK
AIPS_PLAT_CLK
CAN_CHI_CLK
FLEXCANn_PE_CLK
CAN_PE_CLK
MODULE_CLK
REG_INTF_CLK
Figure 73. FlexCANn clocking
FlexCAN has the following unique clocks:
• CAN_CHI_CLK—FlexCAN controller host interface clock
• CAN_PE_CLK—FlexCAN protocol engine clock
For all S32K3xx devices, the clock multiplexer to the CAN_FD protocol engine (PE) clock has an option to use the FXOSC_CLK 
(see Table 120 and Table 121). With a 40 MHz crystal source, FlexCAN supports up to an 8 Mbps data rate. With a 16 MHz crystal 
source, 3.2 Mbps is achievable. For baud rate calculations, see the section "Protocol timing" in the "CAN (FlexCAN)" chapter.
For some devices, the clock multiplexer to the CAN_FD protocol engine (PE) clock has an option to use the CORE_CLK. See 
Table 120 and Table 121. When the CORE_CLK is running at 240 MHz, the PLL derived clock to the CAN_FD protocol engine 
(PE) clock will be at 120 MHz (using the option to divide by 2), at 80 MHz (using the option to divide by 3), or at 60 MHz (using 
the option to divide by 4).
 
• See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this 
module's availability on your chip variant.
• For MC_CGM input sources for different variants, see clocking diagram in 'Clocking Overview' section in 
'Clocking' chapter
  NOTE  
24.6.1.1.1.1
FlexCAN timestamp implementation
The following figure shows the FlexCAN timestamping implementation. The related table shows the timestamp sources and 
corresponding clock nodes.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
933 / 5251


---
# 페이지 32

TS0_CNT_IN
TS_CNT_OUT
TS0_CLK
TS1_CNT_IN
TS1_CLK
TS_OUT_CLK
TS_OUT_CLK_SEL
DCM.DCMRWF1[0]
clk
D
Q
clk
D
Q
Figure 74. FlexCAN timestamping
Table 124. Timestamp sources and clock nodes
Timestamp
Module
TS clock domain
TS0_CLK
EMAC/GMAC
EMAC_CLK_TS/GMAC_CLK_TS
TS1_CLK
STM0
AIPS_PLAT_CLK
TS_OUT_CLK
FlexCANn
EMAC_CLK_TS/GMAC_CLK_TS
 
• See section "Feature comparison" in this reference manual's "Introduction" chapter for details on this module's 
availability on your chip variant.
• The timestamp clock (TS_OUT_CLK, EMAC_TS_CLK/GMAC_CLK_TS) must be greater than or equal 
to FLEXCANn_PE_CLK. When using STM0 as the timestamp source, the FlexCAN timestamp clock 
(TS_OUT_CLK, EMAC_TS_CLK/GMAC_CLK_TS) must be greater than or equal to STM0_CLK.
  NOTE  
24.6.1.1.2
LPI2Cn clocking
The following figure shows LPI2Cn clocking, and the related table shows the LPI2C SIUL2 configuration.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
934 / 5251


---
# 페이지 33

LPI2Cn
AIPS_SLOW_CLK
LPI2C_CLK
MODULE_CLK
REG_INTF_CLK
SCL
SIUL2_MSCRa[OBE]
SIUL2_MSCRa[IBE]
SIUL2_MSCRa[SSS]
SIUL2_IMCRb[SSS]
LPI2Cn_SCL
SIUL2
SIUL2_MSCRa[OBE]
SIUL2_MSCRa[IBE]
SIUL2_MSCRa[SSS]
SIUL2_IMCRb[SSS]
LPI2Cn_SCLS
SIUL2
SCLS
Figure 75. LPI2Cn clocking
 
• See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this 
module's availability on your chip variant.
• For MC_CGM input sources for different variants, see clocking diagram in 'Clocking Overview' section in 
'Clocking' chapter
  NOTE  
 
See the IOMUX file for your chip variant, attached to this document for details on the ports that support this function.
  NOTE  
24.6.1.1.3
GMAC clocking
Clocking details of GMAC for different modes is described in this section.
 
See the "Device Configuration Module General-Purpose Registers (DCM_GPR)" chapter for details on 
GMAC configuration.
  NOTE  
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
935 / 5251


---
# 페이지 34

CLK_tx_i
25 MHz
CLK_rx_i
25 MHz
25 MHz
Clk_ptp_ref_i
Clk_rmii_i
Div2
Div
Div
PLL_AUX_CLK
PLL_CLK
FIRC_CLK
1
0
0
1
1
0
3
2
1
0
3
2
2
1
0
25 MHz
50 MHz
0
1
MC_CGM_MUX7
FIRC_CLK
FXOSC_CLK
PLL_CLK
PLL_AUX_CLK
CORE_CLK
MC_CGM_MUX9
PLL_AUX_CLK
PLL_CLK
FIRC_CLK
Div
Hclk
MC_CGM_MUX8
0
1
Div20
Div2
DCMRWF2[10:9]
DCMRWF4[26]
DCMRWF1[6]
TX EN
GMAC0_MII_RMII_RGMII_TX_CLK
GMAC0
DCMRWF3[15]
DCMRWF1[6]
DCMRWF3[14]
DCMRWF3[13]
DCMRWF2[10:9]
GMAC0_MII_RMII_RGMII_TX_CLK
Figure 76. GMAC0 clocking (S32K389)
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
936 / 5251


---
# 페이지 35

CLK_tx_i
25 MHz
CLK_rx_i
25 MHz
25 MHz
Clk_ptp_ref_i
Clk_rmii_i
Div2
Div
Div
PLL_AUX_CLK
PLL_CLK
FIRC_CLK
1
0
0
1
1
0
3
2
1
0
3
2
2
1
0
25 MHz
50 MHz
0
1
FIRC_CLK
FXOSC_CLK
PLL_CLK
PLL_AUX_CLK
CORE_CLK
PLL_AUX_CLK
PLL_CLK
FIRC_CLK
Div
Hclk
0
1
Div20
Div2
DCMRWF4[22:21]
DCMRWF4[31]
DCMRWF4[24]
DCMRWF4[27]
DCMRWF2[2]
TX EN
GMAC1_MII_RMII_RGMII_TX_CLK
GMAC1_MII_RMII_RGMII_TX_CLK
DCMRWF4[22:21]
DCMRWF4[30]
DCMRWF4[29]
MC_CGM_MUX16
MC_CGM_MUX15
MC_CGM_MUX9
GMAC1
Figure 77. GMAC1 clocking (S32K389)
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
937 / 5251


---
# 페이지 36

MC_CGM_MUX9
hclk_i
clk_ptp_ref_i
clk_rmii_i
clk_tx_i
clk_rx_i
DIV
1
0
0
1
DIV2
DIV
MC_CGM_MUX8
MC_CGM_MUX7
DIV
0
1
PLL_AUX_CLK
PLL_CLK
FIRC_CLK
PLL_CLK
FIRC_CLK
FXOSC_CLK
PLL_AUX_CLK
PLL_CLK
FIRC_CLK
PLL_AUX_CLK
DCMRWF1[6]
DCMRWF3[15]
DCMRWF3[15]
DCMRWF1[6]
0
1
0
1
DCMRWF3[14]
DCMRWF4[26]
TX EN
5
GMAC0_MII_RMII_RGMII_TX_CLK
PLL_AIPS_CLK
GMAC0
GMAC0_MII_RGMII_TX_CLK
Figure 78. GMAC0 clocking (S32K388)
MC_CGM_MUX9
hclk_i
clk_ptp_ref_i
clk_rmii_i
clk_tx_i
clk_rx_i
DIV
1
0
0
1
DIV2
DIV
MC_CGM_MUX8
MC_CGM_MUX7
DIV
0
1
PLL_AUX_CLK
PLL_CLK
FIRC_CLK
PLL_CLK
FIRC_CLK
FXOSC_CLK
PLL_AUX_CLK
PLL_CLK
FIRC_CLK
PLL_AUX_CLK
DCMRWF4[24]
DCMRWF4[31]
DCMRWF4[29]
DCMRWF2[2]
0
1
0
1
DCMRWF4[30]
DCMRWF4[27]
TX EN
5
GMAC1_MII_RMII_RGMII_TX_CLK
PLL_AIPS_CLK
GMAC1
GMAC1_MII_RGMII_TX_CLK
Figure 79. GMAC1 clocking (S32K388)
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
938 / 5251


---
# 페이지 37

GMAC
5
GMAC_CLK_RMII
5
DCMGPR
TX EN
Figure 80. GMAC clocking (S32K358, S32K348, S32K338, and S32K328)
Table 125. MII clock configuration (for S32K358)
Source 
clock
Destination 
clock
Port
SIUL2
MSCRa
MSCR fields
IMCRb
IMCR[SSS]
OBE
IBE
SSS
GMAC_MII_
RMII_TX_C
LK
GMAC_CLK
_TX
PTC0
64
0
1
X
808
0100b
GMAC_CLK
_RX
GMAC_CLK
_TX
PTD6
102
0
1
X
808
0010b
GMAC_CLK
_RX
GMAC_CLK
_TX
PTD11
107
0
1
X
808
0001b
GMAC_CLK
_RX
GMAC_CLK
_TX
PTD12
108
0
1
X
808
0011b
GMAC_CLK
_RX
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
939 / 5251


---
# 페이지 38

Table 125. MII clock configuration (for S32K358) (continued)
Source 
clock
Destination 
clock
Port
SIUL2
MSCRa
MSCR fields
IMCRb
IMCR[SSS]
OBE
IBE
SSS
GMAC_MII_
RMII_TX_C
LK
GMAC_CLK
_TS
PTC0
64
0
1
X
808
0100b
PTD6
102
0
1
X
808
0010b
PTD11
107
0
1
X
808
0001b
PTD12
108
0
1
X
808
0011b
GMAC_MII_
RX_CLK
GMAC_CLK
_TS
PTC0
64
0
1
X
812
0100b
PTC1
65
0
1
X
812
0011b
PTD5
101
0
1
X
812
0010b
PTD10
106
0
1
X
812
0001b
Table 126. RGMII clock configuration (for S32K358)
Source 
clock
Destination 
clock
Port
SIUL2
MSCRa
MSCR fields
IMCRb
IMCR[SSS]
OBE
IBE
SSS
GMAC_MII_
RMII_RGMI
I_TX_CLK
GMAC_CLK
_TX
PTB3
35
0
1
X
808
0101b
GMAC_CLK
_RX
GMAC_CLK
_TX
PTC19
83
0
1
X
808
0110b
GMAC_CLK
_RX
GMAC_MII_
RMII_RGMI
I_TX_CLK
GMAC_CLK
_TS
PTB3
35
0
1
X
808
0101b
PTC19
83
0
1
X
808
0110b
GMAC_MII_
RGMII_RX_
CLK
GMAC_CLK
_TS
PTB22
54
0
1
X
812
0111b
PTB26
58
0
1
X
812
0101b
PTC16
80
0
1
X
812
0110b
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
940 / 5251


---
# 페이지 39

Table 127. GMAC_0 MII clock configuration (for S32K388/S32K389)
Source 
Clock
Destination 
clock
Port
SIUL2
MSCRa
MSCR fields
IMCRb
IMCR[SSS]
OBE
IBE
SSS
GMAC0_MII
_RMII_TX_
CLK
GMAC0_CL
K_TX
PTC0
64
0
1
X
808
0111b
GMAC0_CL
K_RX
GMAC0_CL
K_TX
PTD6
102
0
1
X
808
0010b
GMAC0_CL
K_RX
GMAC0_CL
K_TX
PTD11
107
0
1
X
808
0001b
GMAC0_CL
K_RX
GMAC0_CL
K_TX
PTD12
108
0
1
X
808
0011b
GMAC0_CL
K_RX
GMAC0_MII
_RMII_TX_
CLK
GMAC_CLK
_TS
PTC0
64
0
1
X
808
0111b
PTD6
102
0
1
X
808
0010b
PTD11
107
0
1
X
808
0001b
PTD12
108
0
1
X
808
0011b
GMAC0_MII
_RX_CLK
GMAC_CLK
_TS
PTB26
58
0
1
X
812
0101b
PTC1
65
0
1
X
812
0011b
PTD5
101
0
1
X
812
0010b
PTD10
106
0
1
X
812
0001b
Table 128. GMAC_0 RGMII clock configuration (for S32K388/S32K389)
Source 
clock
Destination 
clock
Port
SIUL2
MSCRa
MSCR fields
IMCRb
IMCR[SSS]
OBE
IBE
SSS
GMAC0_MII
_RMII_RGM
II_TX_CLK
GMAC0_CL
K_TX
PTB3
35
0
1
X
808
0101b
GMAC0_CL
K_RX
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
941 / 5251


---
# 페이지 40

Table 128. GMAC_0 RGMII clock configuration (for S32K388/S32K389) (continued)
Source 
clock
Destination 
clock
Port
SIUL2
MSCRa
MSCR fields
IMCRb
IMCR[SSS]
OBE
IBE
SSS
GMAC0_CL
K_TX
PTC1
65
0
1
X
808
0111b
GMAC0_CL
K_RX
GMAC0_CL
K_TX
PTC19
83
0
1
X
808
0110b
GMAC0_CL
K_RX
GMAC0_MII
_RMII_RGM
II_TX_CLK
GMAC_CLK
_TS
PTB3
35
0
1
X
808
0101b
PTC1
65
0
1
X
808
0111b
PTC19
83
0
1
X
808
0110b
GMAC0_MII
_RGMII_RX
_CLK
GMAC_CLK
_TS
PTB22
54
0
1
X
812
0111b
PTC16
80
0
1
X
812
0110b
Table 129. GMAC_1 RGMII clock configuration (for S32K388/S32K389)
Source 
Clock
Destination 
clock
Port
SIUL2
MSCRa
MSCR fields
IMCRb
IMCR[SSS]
OBE
IBE
SSS
GMAC1_MII
_RMII_RGM
II_TX_CLK
GMAC1_CL
K_TX
PTB3
35
0
1
X
975
0010b
GMAC1_CL
K_RX
GMAC1_CL
K_TX
PTC1
65
0
1
X
975
0001b
GMAC1_CL
K_RX
GMAC1_MII
_RMII_RGM
II_TX_CLK
GMAC_CLK
_TS
PTB3
35
0
1
X
975
0010b
PTC1
65
0
1
X
975
0001b
GMAC1_MII
_RGMII_RX
_CLK
GMAC_CLK
_TS
PTD10
106
0
1
X
962
0001b
24.6.1.1.4
EMAC clocking
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
942 / 5251


---
# 페이지 41

Clocking details of EMAC for different modes is described in this section.
MUX_7_DC_0[DIV]
24
0
25
0
24
EMAC_CLK_RX
MUX_8_DC_0[DIV]
EMAC_CLK_TX
MUX_9_DC_0[DIV]
EMAC_CLK_TS
25
2
0
24
8
EMAC_MII_RMII_TX_CLK
EMAC_MII_RX_CLK
FIRC_CLK
FXOSC_CLK
PLL_PHI0_CLK
 
SIUL2
MUX_7_CSC[SELCTL]
MUX_8_CSC[SELCTL]
MUX_9_CSC[SELCTL]
1...64
1...64
1...64
MC_CGM
EMAC
TS_CLK
TX_CLK
RX_CLK
RMII_CLK
IMCR300[SSS]
IMCR296[SSS]
REG_INTF_CLK
AIPS_PLAT_CLK
MODULE_CLK
CORE_CLK
Only available on:
S32K328, S32K338, S32K348, 
S32K358, S32K388 
Only available on:
S32K314, S32K322, S32K324, 
S32K341, S32K342, S32K344 
Figure 81. EMAC clocking
 
EMAC operates only in Clock options A, B, A+, and A++, since the module clock becomes lower than the protocol 
clock (RMII/MII clocks) in other modes.
  NOTE  
 
• See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this 
module's availability on your chip variant.
• For MC_CGM input sources for different variants, see clocking diagram in 'Clocking Overview' section in 
'Clocking' chapter
  NOTE  
PLL_AUX should be used for the GMAC TX and TS clocks to support 1 Gbps Ethernet operation.
PLL_AUX should operate in integer mode to meet the RGMII clock accuracy requirements.
24.6.1.1.4.1
EMAC RMII clocking
The following table shows the EMAC RMII clocking, and the related table shows the SIUL2 clock signal configuration for RMII.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
943 / 5251


---
# 페이지 42

MUX_7_DC_0[DIV]
24
24
EMAC_CLK_RX
MUX_8_DC_0[DIV]
EMAC_CLK_TX
MUX_9_DC_0[DIV]
EMAC_CLK_TS
25
2
0
24
8
EMAC_MII_RMII_TX_CLK
EMAC_MII_RX_CLK
FIRC_CLK
FXOSC_CLK
PLL_PHI0_CLK
 
SIUL2
MUX_7_CSC[SELCTL]
MUX_8_CSC[SELCTL]
MUX_9_CSC[SELCTL]
1...64
1...64
1...64
MC_CGM
EMAC
TS_CLK
TX_CLK
RX_CLK
RMII_CLK
IMCR300[SSS]
IMCR296[SSS]
REG_INTF_CLK
AIPS_PLAT_CLK
MODULE_CLK
CORE_CLK
Only available on:
S32K328, S32K338, S32K348, 
S32K358, S32K388 
Only available on:
S32K314, S32K322, S32K324, 
S32K341, S32K342, S32K344 
Figure 82. EMAC RMII clocking
 
• See the IOMUX file for your chip variant, attached to this document for details on the ports that support 
this function.
• The value of CGM divider depends on mode of working. For example, if 25 MHz mode is selected, then the 
divider value is 2, if 2.5 MHz mode is selected then the divider value is 20.
  NOTE  
24.6.1.1.4.2
EMAC MII clocking
The following figure shows the EMAC MII clocking, and the related table shows the SIUL2 clock signal configuration for MII.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
944 / 5251


---
# 페이지 43

MUX_7_DC_0[DIV]
24
25
EMAC_CLK_RX
MUX_8_DC_0[DIV]
EMAC_CLK_TX
MUX_9_DC_0[DIV]
EMAC_CLK_TS
25
2
0
24
8
EMAC_MII_RMII_TX_CLK
EMAC_MII_RX_CLK
FIRC_CLK
FXOSC_CLK
PLL_PHI0_CLK
 
SIUL2
MUX_7_CSC[SELCTL]
MUX_8_CSC[SELCTL]
MUX_9_CSC[SELCTL]
1...64
1...64
1...64
MC_CGM
EMAC
TS_CLK
TX_CLK
RX_CLK
RMII_CLK
IMCR300[SSS]
IMCR296[SSS]
REG_INTF_CLK
AIPS_PLAT_CLK
MODULE_CLK
CORE_CLK
Only available on:
S32K328, S32K338, S32K348, 
S32K358, S32K388 
Only available on:
S32K314, S32K322, S32K324, 
S32K341, S32K342, S32K344 
Figure 83. EMAC MII clocking
 
• See the IOMUX file for your chip variant, attached to this document for details on the ports that support 
this function.
• The value of CGM divider depends on mode of working. For example, if 25 MHz mode is selected, then the 
divider value is 2, if 2.5 MHz mode is selected then the divider value is 20.
  NOTE  
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
945 / 5251


---
# 페이지 44

24.6.1.1.5
LPSPIn clocking
LPSPI[y]
SCK
MODULE_CLK
REG_INTF_CLK
AIPS_SLOW_CLK
MODULE_CLK
REG_INTF_CLK
LPSPI[x]
AIPS_PLAT_CLK
LPSPI_CLK
SCK
MODULE_CLK
REG_INTF_CLK
AIPS_PLAT_CLK
SIUL2_MSCRa[OBE]
SIUL2_MSCRa[IBE]
SIUL2_MSCRa[SSS]
SIUL2_IMCRb[SSS]
LPSPIn_SCK
SIUL2_MSCRa[OBE]
SIUL2_MSCRa[IBE]
SIUL2_MSCRa[SSS]
SIUL2_IMCRb[SSS]
LPSPIn_SCK
LPSPI_CLK
SIUL2
SIUL2
Note: 
For all variants except S32K389 x=0 and y= 1...5
For S32K389 x=0...5
Figure 84. LPSPIn clocking
 
• See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this 
module's availability on your chip variant.
• For MC_CGM input sources for different variants, see clocking diagram in 'Clocking Overview' section in 
'Clocking' chapter
  NOTE  
24.6.1.1.6
LPUARTn clocking
The following figure shows the LPUARTn clocking configuration, and the related table shows LPUART use case baud rates.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
946 / 5251


---
# 페이지 45

AIPS_PLAT_CLK
AIPS_SLOW_CLK
LPUARTn
LPUARTn
MODULE_CLK
REG_INTF_CLK
MODULE_CLK
REG_INTF_CLK
Figure 85. LPUARTn clocking
See the following table to get correct configuration for each instance in your chip variant.
Table 130. LPUARTn instance clocking
Variant
LPUARTn instance
Description
For S32K344, S32K324, and S32K314
16
LPUART [0] and [8] is clocked 
by AIPS_PLAT_CLK
LPUART [1:7] and [9:15] is clocked 
by AIPS_SLOW_CLK
For S32K312
8
LPUART [0] is clocked 
by AIPS_PLAT_CLK
LPUART [1:7] is clocked 
by AIPS_SLOW_CLK
For S32K42, S32K341, S32K322, 
S32K311, and S32K310
4
LPUART [0] and [1] is clocked 
by AIPS_PLAT_CLK
LPUART [2:3] is clocked 
by AIPS_SLOW_CLK
For S32K358, S32K348, S32K338, and 
S32K328
16
LPUART [0], [1], and [8] is clocked 
by AIPS_PLAT_CLK
LPUART [2:7] and [9:15] is clocked 
by AIPS_SLOW_CLK
For S32K388 and S32K389
16
LPUART [0:15] is clocked 
by AIPS_PLAT_CLK
 
See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this module's 
availability on your chip variant.
  NOTE  
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
947 / 5251


---
# 페이지 46

Table 131. LPUART baud rate calculation
Required baud rate
(bps)
LPUART_CLK
(MHz)
OSR
SBR[12:0]
Calculated baud rate
(bps) 1
8192
40
4
976
8196
8192
80
15
610
8196
8192
48
15
366
8196
115200
48
15
26
115384
115200
40
7
43
116279
19200
80
4
833
19207
19200
40
7
260
19230
38400
40
7
130
38461
1. MODULE_CLK ÷ (LPUART.BAUD[SBR] × (LPUART.BAUD[OSR] + 1))
24.6.1.1.7
FlexIO clocking
The following figure shows the FlexIO clocking interface. The related two tables show the FlexIO baud rate use cases.
FlexIO
AIPS_PLAT_CLK
 
MODULE_CLK
CORE_CLK
FLEXIO_CLK
REG_INTF_CLK
Figure 86. FlexIO clocking
 
See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this module's 
availability on your chip variant.
  NOTE  
The following tables describes an example how to calculate baud rate for a given frequency. For actual frequency used in your 
chip, see System clock frequency limitations.
Table 132. FlexIO baud rate calculation (FlexIO.TIMCFGn[TIMDEC] = 101b)
FLEXIO_CLK 
(CORE_CLK)
Required baud 
rate
TIMCMPn[CMP]
Theoretical 
baud rate 1
Bit duration
Observed baud 
rate
Hex
Decimal
88 MHz
9600
0010h
16
10110.29
101.33 μs
9868
88 MHz
19200
0007h
7
21484.37
47.44 μs
21079
88 MHz
57600
0001h
1
85937.50
11.66 μs
85763
88 MHz
115200
0000h
0
171875.00
5.88 μs
170068
1. Theoretical baud rate = Frequency ÷ (256 × 2 × (TIMCMPn[CMP] + 1))
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
948 / 5251


---
# 페이지 47

Table 133. FlexIO baud rate calculation (FlexIO.TIMCFGn[TIMDEC] = 100b)
FLEXIO_CLK 
(CORE_CLK)
Required baud 
rate
TIMCMPn[CMP]
Theoretical 
baud rate1
Bit duration
Observed baud 
rate
Hex
Decimal
88 MHz
19200
8Eh
142
19230.77
51.88 μs
19275
88 MHz
57600
2Eh
46
58510.64
16.89 μs
59206
88 MHz
115200
16h
22
119565.21
8.44 μs
118483
1. Theoretical baud rate = Frequency ÷ (16 × 2 × (TIMCMPn[CMP] + 1))
24.6.1.1.8
QuadSPI clocking
QuadSPI
AIPS_PLAT_CLK
AHB_CLK
SFCK
MODULE_CLK
REG_INTF_CLK
SIUL2_MSCR106[OBE]
SIUL2_MSCR106[SSS]
QuadSPI_SCKFA
SF_IF_X_CLK
QSPI_SFCK
QSPI_RAM_CLK
QSPI_TX_MEM_CLK
QSPI_TX
QSPI_MEM_CLK
QSPI_RAM
7
QSPI_2xSFIF
2xSFIF_CLK
Only applicable for:
- S32K358
- S32K348
- S32K338
- S32K328
SFCK_OUT
SIUL2
Figure 87. QuadSPI clocking
 
• See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this 
module's availability on your chip variant.
• For MC_CGM input sources for different variants, see clocking diagram in 'Clocking Overview' section in 
'Clocking' chapter
  NOTE  
For S32K358, S32K348, S32K338, and S32K328, QSPI_SFCK will be generated by a fixed 1:2 divider from the QSPI_2xSFIF.
 
See System clocking configurations for details.
  NOTE  
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
949 / 5251


---
# 페이지 48

24.6.1.1.9
SAIn clocking
SAI.xCR2[MSEL]
11
10
01
00
SAI1
SIUL2_MSCR35[OBE]
SIUL2_MSCR35[IBE]
SIUL2_MSCR35[SSS]
SIUL2_IMCR320[SSS]
SAI0_MCLK
SAI.xCR2[MSEL]
11
10
01
00
SAI0
FXOSC_CLK
BCLK
BCLK
SIUL2_MSCR110[OBE]
SIUL2_MSCR110[IBE]
SIUL2_IMCR324[SSS]
SAI1_MCLK
SIUL2_MSCR136[OBE]
SIUL2_MSCR136[IBE]
SIUL2_MSCR136[SSS]
SIUL2_IMCR322[SSS]
SAI1_BCLK
SIUL2_MSCR76[OBE]
SIUL2_MSCR76[IBE]
SIUL2_MSCR76[SSS]
SIUL2_IMCR315[SSS]
SAI0_BCLK
MODULE_CLK/
REG_INTF_CLK
MODULE_CLK/
REG_INTF_CLK
AIPS_SLOW_CLK
SIUL2
Figure 88. SAIn clocking
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
950 / 5251


---
# 페이지 49

 
• See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this 
module's availability on your chip variant.
• For MC_CGM input sources for different variants, see clocking diagram in 'Clocking Overview' section in 
'Clocking' chapter
  NOTE  
 
See the IOMUX file for your chip variant, attached to this document for details on the ports that support this function.
  NOTE  
Internally generated MCLK is not supported on the S32K3xx chip family.
The Second PLL will be a clock source for the SAI Master Clock.
24.6.1.1.10
uSDHC clocking
uSDHC
 
MODULE_CLK
 
PER_CLK
AHB_CLK
32KHZ_CLK
SIRC_CLK
REG_INTF_CLK
AIPS_PLAT_CLK
uSDHC_PER_CLK
CARD_CLK_OUT
CARD_CLK_IN
Figure 89. uSDHC clocking
Clock multiplexer provides the clock for the uSDHC module with the following options:
1. FIRC_CLK
2. FXOSC_CLK
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
951 / 5251


---
# 페이지 50

3. PLL_PHI1_CLK
4. PLL_AUX_PHI2_CLK
 
• See section "Feature comparison" in this reference manual's "Introduction" chapter for details on this module's 
availability on your chip variant.
• As MC_CGM_MUX14 have max input frequecny limited to 240 MHz, so while sourcing uSDHC_PER_CLK 
from PLL_PHI1_CLK, QSPI can run only on 60 Mhz max frequency.
  NOTE  
24.6.1.2
System modules
Figure 90 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 134 shows the REG_INTF_CLK and 
MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the 
same source for REG_INTF_CLK as used by MODULE_CLK.
See REG_INTF_CLK
and MODULE_CLK
columns in table below
MODULE_CLK
Module
REG_INTF_CLK
}
Figure 90. System module clocks
Table 134. System module clocking
Module
MODULE_CLK
REG_INTF_CLK
MSCM
AIPS_PLAT_CLK
AIPS_PLAT_CLK
MCM
AIPS_SLOW_CLK
AIPS_SLOW_CLK
SIUL2
See SIUL2 clocking.
VIRT_WRAPPER
AIPS_SLOW_CLK
AIPS_SLOW_CLK
AXBS
CORE_CLK
AIPS_PLAT_CLK
DMAMUX
CORE_CLK
CORE_CLK
eDMA
CORE_CLK
AIPS_PLAT_CLK
INTM
AIPS_PLAT_CLK
AIPS_PLAT_CLK
SEMA42
AIPS_PLAT_CLK
AIPS_PLAT_CLK
XBIC
CORE_CLK
AIPS_PLAT_CLK
XRDC
CORE_CLK
AIPS_PLAT_CLK
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
952 / 5251


---
# 페이지 51

24.6.1.2.1
SIUL2 clocking
SIUL2
FIRC_CLK
MODULE_CLK
REG_INTF_CLK
FILTER_CLK
AIPS_SLOW_CLK
Figure 91. SIUL2 clocking
24.6.1.3
Clocking modules
Figure 92 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 135 shows the REG_INTF_CLK and 
MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the 
same source for REG_INTF_CLK as used by MODULE_CLK.
See REG_INTF_CLK
and MODULE_CLK
columns in table below
MODULE_CLK
Module
REG_INTF_CLK
}
Figure 92. Clocking module clocks
Table 135. Clocking module clocking
Module
MODULE_CLK
REG_INTF_CLK
FXOSC
See FXOSC clocking.
SXOSC
See SXOSC clocking.
SIRC
See SIRC clocking.
FIRC
See FIRC clocking.
PLLDIG
See PLLDIG clocking.
MC_CGM
—
AIPS_SLOW_CLK
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
953 / 5251


---
# 페이지 52

24.6.1.3.1
FIRC clocking
FIRC
REG_INTF_CLK
AIPS_SLOW_CLK
FIRC_CLK
3
0
÷2
1
2
÷2
÷16
HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL]
Oscillator
Figure 93. FIRC clocking
24.6.1.3.2
SIRC clocking
SIRC
REG_INTF_CLK
AIPS_SLOW_CLK
SIRC_CLK
Oscillator
Figure 94. SIRC clocking
24.6.1.3.3
FXOSC clocking
FXOSC
REG_INTF_CLK
AIPS_SLOW_CLK
XTAL
EXTAL
FXOSC_CLK
Figure 95. FXOSC clocking
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
954 / 5251


---
# 페이지 53

24.6.1.3.4
SXOSC clocking
SXOSC
REG_INTF_CLK
AIPS_SLOW_CLK
OSC32K_XTAL
OSC32K_EXTAL
SXOSC_CLK
Figure 96. SXOSC clocking
24.6.1.3.5
PLLDIG clocking
PLLDIG
REG_INTF_CLK
AIPS_SLOW_CLK
Reference
clock
FXOSC_CLK
PLL_AUX_PHI0_CLK
PLL_AUX_PHI1_CLK
PLL_AUX_PHI2_CLK
Only available on:
- S32K328
- S32K338
- S32K348
- S32K358
Figure 97. PLLDIG clocking
24.6.1.4
Reset modules
Figure 98 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 136 shows the REG_INTF_CLK and 
MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the 
same source for REG_INTF_CLK as used by MODULE_CLK.
See REG_INTF_CLK
and MODULE_CLK
columns in table below
MODULE_CLK
Module
REG_INTF_CLK
}
Figure 98. Reset module clocks
Table 136. Reset module clocking
Module
MODULE_CLK
REG_INTF_CLK
MC_RGM
FIRC_CLK
FIRC_CLK
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
955 / 5251


---
# 페이지 54

24.6.1.5
Security modules
Figure 99 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 137 shows the REG_INTF_CLK and 
MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the 
same source for REG_INTF_CLK as used by MODULE_CLK.
See REG_INTF_CLK
and MODULE_CLK
columns in table below
MODULE_CLK
Module
REG_INTF_CLK
}
Figure 99. Security module clocks
Table 137. Security module clocking
Module
MODULE_CLK
REG_INTF_CLK
HSE_B
See HSE_B clocking .
MU
AIPS_SLOW_CLK
AIPS_SLOW_CLK
DCM
DCM_CLK
DCM_CLK
AES_ACCEL
See ACE_ACCEL clocking.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
956 / 5251


---
# 페이지 55

24.6.1.5.1
HSE_B clocking
HSE_CLK
HSE_B
DCM_CLK
AIPS_SLOW_CLK
HSE_MU0
SIRC_CLK
TCK
PLL (MODULE_CLK)
HSE_MU1
MODULE_CLK
MODULE_CLK
REG_INTF_CLK
REG_INTF_CLK
TCK
TCK_n
DCF_clk
HSE_B_IPS
PLL standby
Slow 32k clk
Figure 100. HSE_B clocking
 
The clock frequency relationship between TCK and HSE_CLK clocks for HSE_B must be a minimum ratio of 1:1.5. 
For example, if HSE_CLK equals 80 MHz, then TCK must be less than or equal to 53 MHz (80 MHz ÷ 1.5).
  NOTE  
24.6.1.5.2
ACE_ACCEL clocking
HSE_CLK
AES_ACCEL
MODULE_CLK
REG_INTF_CLK
AES_1us_CLK
REFERENCE_1us
Figure 101. ACE_ACCEL clocking
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
957 / 5251


---
# 페이지 56

24.6.1.6
Power-management modules
Figure 102 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 138 shows the REG_INTF_CLK and 
MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the 
same source for REG_INTF_CLK as used by MODULE_CLK.
See REG_INTF_CLK
and MODULE_CLK
columns in table below
MODULE_CLK
Module
REG_INTF_CLK
}
Figure 102. Power-management module clocks
Table 138. Power-management module clocking
Module
MODULE_CLK
REG_INTF_CLK
PMC
AIPS_SLOW_CLK
AIPS_SLOW_CLK
MC_ME
AIPS_SLOW_CLK
AIPS_SLOW_CLK
MC_PCU
FIRC_CLK
FIRC_CLK
WKPU
AIPS_SLOW_CLK
AIPS_SLOW_CLK
24.6.1.7
Safety modules
Figure 103 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 139 shows the REG_INTF_CLK and 
MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the 
same source for REG_INTF_CLK as used by MODULE_CLK.
See REG_INTF_CLK
and MODULE_CLK
columns in table below
MODULE_CLK
Module
REG_INTF_CLK
}
Figure 103. Safety module clocks
Table 139. Safety module clocking
Module
MODULE_CLK
REG_INTF_CLK
EIM
AIPS_PLAT_CLK
AIPS_PLAT_CLK
ERM
See ERM clocking.
FCCU
See FCCU clocking.
STCU2
See STCU2 clocking.
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
958 / 5251


---
# 페이지 57

Table 139. Safety module clocking (continued)
Module
MODULE_CLK
REG_INTF_CLK
REG_PROT
AIPS_SLOW_CLK
AIPS_SLOW_CLK
CMU_FC
AIPS_SLOW_CLK
AIPS_SLOW_CLK
CMU_FM
AIPS_SLOW_CLK
AIPS_SLOW_CLK
CRC
AIPS_PLAT_CLK
AIPS_PLAT_CLK
24.6.1.7.1
FCCU clocking
FCCU
AIPS_PLAT_CLK
SAFE_CLK
FIRC_CLK
MODULE_CLK
REG_INTF_CLK
Figure 104. FCCU clocking
24.6.1.7.2
STCU2 clocking
STCU2
CORE_CLK
REG_INTF_CLK
AIPS_SLOW_CLK
SHIFT_CLK
JTAG_TCK
Figure 105. STCU2 clocking
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
959 / 5251


---
# 페이지 58

24.6.1.7.3
ERM clocking
MEM_CLK[n]
ERM
AIPS_PLAT_CLK
MODULE_CLK
CORE_CLK
Figure 106. ERM clocking
 
MEM_CLK[20:23] are not used. Source clock for MEM_CLK[0:19] is CORE_CLK.
  NOTE  
24.6.1.8
ADC and motor control modules
Figure 107 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 140 shows the REG_INTF_CLK and 
MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the 
same source for REG_INTF_CLK as used by MODULE_CLK.
See REG_INTF_CLK
and MODULE_CLK
columns in table below
MODULE_CLK
Module
REG_INTF_CLK
}
Figure 107. Motor control module clocks
Table 140. Motor control module clocking
Module
MODULE_CLK
REG_INTF_CLK
ADC
See ADCn clocking.
LCU
CORE_CLK
eMIOS
See eMIOSn clocking.
BCTU
See BCTU clocking.
TRGMUX
AIPS_SLOW_CLK
TSPC
AIPS_SLOW_CLK
24.6.1.8.1
ADCn clocking
The following figure shows ADCn clocking configuration.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
960 / 5251


---
# 페이지 59

ADCn
MODULE_CLK
REG_INTF_CLK
CORE_CLK
00
01
10
11
AD_CLK
÷2
÷4
ADC.MCR[ADCLKSEL]
÷8
Only available in 
S32K388, S32K389, S32K328, 
S32K338, S32K348, S32K358, 
S32K311, and S32K310 
Figure 108. ADCn clocking
 
See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this module's 
availability on your chip variant.
  NOTE  
The prescaler can be bypassed when using FIRC_CLK as the source (see MC_CGM mux 0 clocks for FIRC_CLK use details). The 
prescaler must be controlled such that the AD_CLK frequency is less than or equal to 120 MHz for S32K388/S32K389/S32K358/
S32K348/S32K338/S32K328/S32K312/S32K311/S32K310. For other S32K3xx products maximum frequency supported is 
80 Mhz.
The minimum operating speed of AD_CLK is 6 MHz using the following configuration:
1. Use FIRC_CLK (48 MHz) as clock source (MC_CGM.MUX_0_CSC[SELCTL] equal to 0000b).
2. Divide FIRC_CLK by 2 for CORE_CLK speed (MC_CGM.MUX_0_DC_0[DIV] equal to 1 (FIRC_CLK divide by 2 = 24 MHz)).
3. Write ADC.MCR[ADCCLKSEL] equal to 10b to divide the FIRC_CLK further by 4 (AD_CLK = 6 MHz).
However, at this lower speed, the ADCn results will be degraded.
24.6.1.8.2
eMIOSn clocking
eMIOSn
MODULE_CLK
REG_INTF_CLK
CORE_CLK
EMIOS_CLK
EMIOS_CHn_CLK
Figure 109. eMIOSn clocking
 
See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this module's 
availability on your chip variant.
  NOTE  
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
961 / 5251


---
# 페이지 60

24.6.1.8.3
BCTU clocking
BCTU
MODULE_CLK
REG_INTF_CLK
CORE_CLK
BCTU_CLK
Figure 110. BCTU clocking
24.6.1.9
Timer modules
Figure 111 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 141 shows the REG_INTF_CLK and 
MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the 
same source for REG_INTF_CLK as used by MODULE_CLK.
See REG_INTF_CLK
and MODULE_CLK
columns in table below
MODULE_CLK
Module
REG_INTF_CLK
}
Figure 111. Timer module clocks
Table 141. Timer module clocking
Module
MODULE_CLK
REG_INTF_CLK
PIT
See PITn clocking.
SWT
See SWTn clocking.
STMn
STMn_CLK
STMn_CLK
RTC
See RTC clocking.
24.6.1.9.1
PITn clocking
The following figure shows the PITn clocking configuration. The related tables show the use case configuration.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
962 / 5251


---
# 페이지 61

PIT[1,2,3]
 AIPS_SLOW_CLK
PIT_CLK
MODULE_CLK
REG_INTF_CLK
Timer 0
Timer 1
Timer 2
Timer 3
PIT0
 AIPS_SLOW_CLK
PIT_CLK
SIRC_CLK
RTI_CLK
MODULE_CLK
REG_INTF_CLK
Timer 0
Timer 1
Timer 2
Timer 3
RTI
Only applicable to S32K388
Figure 112. PITn clocking
 
See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this module's 
availability on your chip variant.
  NOTE  
Table 142. PIT0 modes of operation
MC_ME.PRTN0_COFB1_C
LKEN[REQ44]
PIT.MCR[MDIS]
PIT.MCR[MDIS_
RTI]
Mode
Application
0
X
X
PIT clock gated (minimum 
power)
Module clock gated and 
unused / Standby mode, 
PIT and RTI unused
1
0
0
Both PIT and RTI enabled
Run mode
1
0
1
PIT running, RTI disabled
Run mode with only PIT 
active
1
1
0
PIT disabled, RTI enabled
Standby mode with RTI 
enabled
1
1
1
Both PIT and RTI disabled
Standby mode with RTI 
disabled
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
963 / 5251


---
# 페이지 62

Table 143. PIT[1,2,3] modes of operation
MC_ME.PRTNn_C
OFB1_CLKEN[RE
Q[45,63,64]] 1
PIT.MCR[MDIS]
Mode
Application
0
X
PIT clock gated (minimum power)
Module clock gated and unused, 
Standby mode
1
0
PIT enabled
Run mode
1
0
PIT running
Run mode with PIT active
1
1
PIT disabled
Standby mode
1. PIT1, PIT2, and PIT3 MC_ME partition registers used are:
• PIT1 - MC_ME.PRTN0_COFB1_CLKEN[REQ45]
• PIT2 - MC_ME.PRTN1_COFB1_CLKEN[REQ63]
• PIT3 - MC_ME.PRTN1_COFB1_CLKEN[REQ64]
24.6.1.9.2
SWTn clocking
SWTn
AIPS_SLOW_CLK
MODULE_CLK
COUNTER_CLK
SIRC_CLK
Figure 113. SWTn clocking
 
• See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this 
module's availability on your chip variant.
• For MC_CGM input sources for different variants, see clocking diagram in 'Clocking Overview' section in 
'Clocking' chapter
  NOTE  
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
964 / 5251


---
# 페이지 63

24.6.1.9.3
RTC clocking
RTC
AIPS_SLOW_CLK
 
MODULE_CLK/REG_INTF_CLK
RTC.RTCC[SELCTL]
2
0
1
3
FXOSC_CLK
Clock source 3
FIRC_CLK
Clock source 2
SIRC_CLK
Clock source 1
SXOSC_CLK
Clock source 0
1
0
1
0
÷512
÷32
RTC_CLK
RTC.RTCC[DIV512EN]
RTC.RTCC[DIV32EN]
RTC.RTCC[CNTEN]
32-bit counter
To other modules
Not available on:
- S32K311
- S32K310
Figure 114. RTC clocking
 
The RTC is available in Standby mode. Although bus clock is gated, the RTC can run on FIRC_CLK, SIRC_CLK, 
FXOSC_CLK, or SXOSC_CLK.
  NOTE  
24.6.1.10
Debug modules
Figure 115 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 144 shows the REG_INTF_CLK and 
MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the 
same source for REG_INTF_CLK as used by MODULE_CLK.
See REG_INTF_CLK
and MODULE_CLK
columns in table below
MODULE_CLK
Module
REG_INTF_CLK
}
Figure 115. Debug module clocks
Table 144. Debug module clocking
Module
MODULE_CLK
REG_INTF_CLK
JTAGC
See JTAGC clocking.
JDC
See JDC clocking.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
965 / 5251


---
# 페이지 64

24.6.1.10.1
JTAGC clocking
JTAGC
JTAG_TCK/SWD_CLK
TCK_P
TCK_N
Figure 116. JTAGC clocking
24.6.1.10.2
JDC clocking
JDC
JTAG_TCK/SWD_CLK
MODULE_CLK
REG_INTF_CLK
TCK_P
TCK_N
AIPS_SLOW_CLK
Figure 117. JDC clocking
24.6.1.11
Analog modules
Figure 118 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 145 shows the REG_INTF_CLK and 
MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the 
same source for REG_INTF_CLK as used by MODULE_CLK.
See REG_INTF_CLK
and MODULE_CLK
columns in table below
MODULE_CLK
Module
REG_INTF_CLK
}
Figure 118. Analog module clocks
Table 145. Analog module clocking
Module
MODULE_CLK
REG_INTF_CLK
LPCMP
See LPCMPn clocking.
Temperature Sensor
AIPS_SLOW_CLK
AIPS_SLOW_CLK
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
966 / 5251


---
# 페이지 65

24.6.1.11.1
LPCMPn clocking
LPCMPn
MODULE_CLK
REG_INTF_CLK
AIPS_SLOW_CLK
ROUND_ROBIN_CLK
RTC_CLK
Figure 119. LPCMPn clocking
 
See the section "Feature comparison" in this reference manual's "Introduction" chapter for details on this module's 
availability on your chip variant.
  NOTE  
24.6.1.12
Memory modules
Figure 120 shows the REG_INTF_CLK and MODULE_CLK connections, and Table 146 shows the REG_INTF_CLK and 
MODULE_CLK signals used by these modules. Any module diagram that does not explicitly show a REG_INTF_CLK uses the 
same source for REG_INTF_CLK as used by MODULE_CLK.
See REG_INTF_CLK
and MODULE_CLK
columns in table below
MODULE_CLK
Module
REG_INTF_CLK
}
Figure 120. Memory module clocks
Table 146. Memory module clocking
Module
MODULE_CLK
REG_INTF_CLK
PFLASH/ FLASH
CORE_CLK
AIPS_SLOW_CLK
PRAM/ SRAM
CORE_CLK
AIPS_SLOW_CLK
24.6.2 Peripheral data rates
Table 147. Peripheral data rates
Peripheral
Maximum data rate
S32K322, S32K342, S32K341, S32K314, S32K324, 
S32K344, S32K328, S32K338, S32K348, S32K358, 
S32K388, and S32K389
S32K310, S32K311, and S32K312
ADC
See the S32K3xx Data Sheet for details.
See the S32K3xx Data Sheet for details.
eMIOS1
Able to shift PWM edge by 1 ÷ (240 MHz) = 4.17 ns12.
Able to shift PWM edge by 1 ÷ (120 MHz) = 8.33 ns.
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
967 / 5251


---
# 페이지 66

Table 147. Peripheral data rates (continued)
Peripheral
Maximum data rate
S32K322, S32K342, S32K341, S32K314, S32K324, 
S32K344, S32K328, S32K338, S32K348, S32K358, 
S32K388, and S32K389
S32K310, S32K311, and S32K312
Able to shift PWM edge by 1 ÷ (160 MHz) = 6.25 ns2.
BCTU3
BCTU to generate triggers at 160 MHz.
BCTU to generate triggers at 120 MHz.
LCU
Same domain as EMIOS and BCTU.
Same domain as EMIOS and BCTU.
QuadSPI
• Flash memory interface: SDR 120 MHz 4
• Flash memory interface: SDR 125 MHz2
• DDR and hyperflash not supported12
-
EMAC
See the section "Description" in the "Ethernet Media 
Access Controller (EMAC)" chapter for details.
See the section "Description" in the "Ethernet Media 
Access Controller (EMAC)" chapter for details.
FlexCAN5
8 Mbps
8 Mbps
LPI2C6
400 Kbps in fast mode.
400 Kbps in fast mode.
LPSPI7
For all variants except S32K389:
• LPSPI0 is to have a high clock rate of 20 Mbps
• LPSPI1–LPSPI5 can be 10 Mbps
For S32K389:
• LPSPI0–LPSPI5 can be 20 Mbps
• LPSPI0 is to have a high clock rate of 15 Mbps
• LPSPI1–LPSPI3 can be 7.5 Mbps in case of 50:50 
percent duty cycle
• LPSPI1–LPSPI3 can be 10 Mbps in case of 33:66 
or 66:33 percent duty cycle
SAI0/SAI1 
(I2S)8,9
• Bit rate = 12.288 MHz (12.288 Mbps—bit clock 
frequency governs the bit rate)
• Master clock = 24.576 MHz
• SAI0 and SAI1 operate asynchronously to 
each other
-
LPUART10
See the section "Baud rate generation" in the "Low 
Power Universal Asynchronous Receiver/ Transmitter 
(LPUART)" chapter and Table 131 for details
See the section "Baud rate generation" in the "Low 
Power Universal Asynchronous Receiver/ Transmitter 
(LPUART)" chapter and Table 131 for details
FlexIO11
The different protocol data rates supported by FlexIO 
are listed below. For master mode, max baud rate is 
FLEXIO_CLK ÷ 4. For slave mode, max baud rate 
is FLEXIO_CLK ÷ 6. The baud rate is controlled by 
TIMCMP (lower 8 bits in 8-bit mode and 16 bits in 
16-bit mode).
• UART: 19200 bps
• I2C: 400 Kbps
• SPI: 10 Mbps
• I2S: 12.288 Mbps
The different protocol data rates supported by FlexIO 
are listed below. For master mode, max baud rate is 
FLEXIO_CLK ÷ 4. For slave mode, max baud rate 
is FLEXIO_CLK ÷ 6. The baud rate is controlled by 
TIMCMP (lower 8 bits in 8-bit mode and 16 bits in 
16-bit mode).
• UART: 19200 bps
• I2C: 400 Kbps
• SPI: 7.5 Mbps
• I2S: 12.288 Mbps
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
968 / 5251


---
# 페이지 67

Table 147. Peripheral data rates (continued)
Peripheral
Maximum data rate
S32K322, S32K342, S32K341, S32K314, S32K324, 
S32K344, S32K328, S32K338, S32K348, S32K358, 
S32K388, and S32K389
S32K310, S32K311, and S32K312
Trace
• Fast-speed pins: 120 MHz4
• Fast-speed pins: 125 MHz2
• Standard plus-speed pins: 25 MHz
• SWO trace
uSDHC12
• eMMC mode: 800 Mbps
• SD mode: Maximum of 200 Mbps
-
1. See section "Global Clock Prescaler Submodule (GCP)" in the "Enhanced Modular IO Subsystem (eMIOS)" chapter 
for details.
2. Only applicable for S32K388/S32K389.
3. See section "Triggers" in the "Enhanced Modular IO Subsystem (eMIOS)" chapter.
4. Only applicable for S32K322, S32K341, S32K342, S32K314, S32K324, S32K344, S32K328, S32K338, S32K348, 
and S32K358.
5. See the section "Protocol timing" in the "CAN (FlexCAN)" chapter for data rate calculation details.
6. See the section "Clocks" in the "Low Power Inter-Integrated Circuit (LPI2C)" chapter for LPI2C_CLK frequency details.
7. See the section "Clocks" in the "Low Power Serial Peripheral Interface (LPSPI)" chapter.
8. SAI is not present in S32K310,S32K311, and S32K12.
9. See the section "SAI clocking" in the "Synchronous Audio Interface (SAI)" chapter and SAIn clocking for details.
10. At least one pair of LPUART instances (LPUART0 and LPUART1 for S32K328, S32K338, S32K348, and S32K358) support 
up to 12 Mbps.
11. See the section "Application Information" and "Chip-specific FlexIO information" in the "Flexible I/O (FlexIO)" chapter and 
FlexIO clocking for baud configuration details.
12. Only applicable for S32K328, S32K338, S32K348, and S32K358.
24.6.3 Core and peripheral clock control
The chip provides provisions for core and peripheral clock gating. The next sections describe the details on clock gating 
possibilities and controls (see "Power Management Controller (PMC)" and "Mode Entry Module (MC_ME)" for details).
24.6.3.1
Clock gating
Application core clocks are gated by individual MC_ME core clock enable bits. Additionally, application cores can be clock gated 
by executing WFI (see the "Mode Entry Module (MC_ME)" chapter for details).
Cortex-M7_n
APP DEBUGEN
DAP-PWRUP REQUEST
MDMAPCTL[CM7_n_CORE_ACCESS] 
FCLKEN
CLKEN
HCLKEN
MC_ME_PCTL | (CORE CM7 CCTL & !CORE SLEEPING)
CLKIN
Cortex-M7_n CCTL gating
CORE_CLK
Figure 121. Cortex-M7 core clock gating
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
969 / 5251


---
# 페이지 68

To support core debug across functional reset, challenge response done (application debug enable) gating is done so that the 
debugger can access core debug logic. When the debugger completes its programming with core debug logic, it must program 
the MDM_AP DAP control bit to shift the control of CLKIN and FCLK to CCTL.
See the section "MDM_AP register descriptions" in the "Debug Subsystem" chapter and the "Memory Map" chapter for details.
There are two cases in which other masters can access the TCM of each core:
• When the TCM is used as system memory—HCLK will always remain on if TCM PCTL is 1.
• In applications where TCM is not used as system memory, TCM PCTL is written to 0. TCM will then function as the core's 
memory and HCLK will be gated on WFI.
Ensure that the TCM AHBS interface is not accessed with HCLK disabled. In such case, the read/write transactions do not result 
in any error response.
24.6.3.2
Peripheral clock gating
See the tables in section "Core and peripheral clock control" for the chip partitions, plus peripheral initialization and 
shutdown details.
24.7 Clocking details
24.7.1 System clock frequency limitations
Table 148. System clock frequency limitations (For S32K388/S32K389)
System clock node
System clock divider
Maximum frequency 
allowed for 
S32K388/S32K389
Remarks
CM7_CORE_CLK
MC_CGM.MUX_0_DC_7[DIV]
• 320 MHz
This is the frequency for all cores in the 
S32K388/S32K389.
CM7_CORE_CLK is always greater 
than or equal to CORE_CLK.
CORE_CLK
MC_CGM.MUX_0_DC_0[DIV]
• 160 MHz
For S32K388/S32K389, CORE_CLK 
is the frequency used for AXBS 
interfaces and fast peripherals.
It does not correspond to the 
frequency of the Cortex-M7 cores.
For CM7_CORE_CLK frequencies > 
160 MHz, CORE_CLK is always half of 
CM7_CORE_CLK (2:1 relation).
AIPS_PLAT_CLK
MC_CGM.MUX_0_DC_1[DIV]
• 80 MHz
AIPS_PLAT_CLK is always less than 
or equal to CORE_CLK.
AIPS_SLOW_CLK
MC_CGM.MUX_0_DC_2[DIV]
• 40 MHz
AIPS_SLOW_CLK is always less than 
or equal to AIPS_PLAT_CLK.
HSE_CLK
MC_CGM.MUX_0_DC_3[DIV]
• 160 MHz
HSE_CLK
DCM_CLK
MC_CGM.MUX_0_DC_4[DIV]
• 48 MHz
DCM_CLK
LBIST_CLK
MC_CGM.MUX_0_DC_5[DIV]
• 48 MHz
LBIST clock
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
970 / 5251


---
# 페이지 69

Table 148. System clock frequency limitations (For S32K388/S32K389) (continued)
System clock node
System clock divider
Maximum frequency 
allowed for 
S32K388/S32K389
Remarks
QSPI_MEM_CLK
MC_CGM.MUX_0_DC_6[DIV]
• 160 MHz
QSPI_MEM_CLK is always equal 
to CORE_CLK.
Table 149. System clock frequency limitations (For S32K358, S32K348, S32K338, and S32K328)
System clock node
System clock divider
Maximum frequency allowed
Remarks
CORE_CLK
MC_CGM.MUX_0_DC_0[DIV]
• 240 MHz
CORE_CLK1 is always greater than 
or equal to AIPS_PLAT_CLK.
AIPS_PLAT_CLK
MC_CGM.MUX_0_DC_1[DIV]
• 120 MHz
AIPS_PLAT_CLK is always less than 
or equal to CORE_CLK.
AIPS_SLOW_CLK
MC_CGM.MUX_0_DC_2[DIV]
• 60 MHz
AIPS_SLOW_CLK is always less 
than or equal to AIPS_PLAT_CLK.
HSE_CLK
MC_CGM.MUX_0_DC_3[DIV]
• 120 MHz
When CORE_CLK is equal to or 
less than 120 MHz, HSE_CLK 
can be equal to CORE_CLK. 
When CORE_CLK is higher than 
120 MHz, HSE_CLK must be half of 
the CORE_CLK.
DCM_CLK
MC_CGM.MUX_0_DC_4[DIV]
• 60 MHz
DCM_CLK
LBIST_CLK
MC_CGM.MUX_0_DC_5[DIV]
• 60 MHz
LBIST clock
QSPI_MEM_CLK
MC_CGM.MUX_0_DC_6[DIV]
• 240 MHz
QSPI_MEM_CLK is always equal to 
CORE_CLK except in 1:1 mode (see 
Option F - Operation in 1:1 mode with 
CORE_CLK and AIPS_PLAT_CLK at 
same speed (For all chips except 
S32K388/S32K389)).
1. CORE_CLK is the frequency used for the CM7 cores, AXBS interfaces, and fast peripherals.
Table 150. System clock frequency limitations (For S32K344, S32K324, S32K314, S32K342, S32K322, and S32K341)
System clock node
System clock divider
Maximum frequency allowed
Remarks
CORE_CLK
MC_CGM.MUX_0_DC_0[DIV]
• 160 MHz
CORE_CLK1 is always greater than 
or equal to AIPS_PLAT_CLK.
AIPS_PLAT_CLK
MC_CGM.MUX_0_DC_1[DIV]
• 80 MHz
AIPS_PLAT_CLK is always less than 
or equal to CORE_CLK.
AIPS_SLOW_CLK
MC_CGM.MUX_0_DC_2[DIV]
• 40 MHz
AIPS_SLOW_CLK is always less 
than or equal to AIPS_PLAT_CLK.
HSE_CLK
MC_CGM.MUX_0_DC_3[DIV]
• 120 MHz
When CORE_CLK is equal to or 
less than 120 MHz, HSE_CLK 
can be equal to CORE_CLK. 
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
971 / 5251


---
# 페이지 70

Table 150. System clock frequency limitations (For S32K344, S32K324, S32K314, S32K342, S32K322, and 
S32K341) (continued)
System clock node
System clock divider
Maximum frequency allowed
Remarks
When CORE_CLK is higher than 
120 MHz, HSE_CLK must be half of 
the CORE_CLK.
DCM_CLK
MC_CGM.MUX_0_DC_4[DIV]
• 48 MHz
DCM_CLK
LBIST_CLK
MC_CGM.MUX_0_DC_5[DIV]
• 48 MHz
LBIST clock
QSPI_MEM_CLK
MC_CGM.MUX_0_DC_6[DIV]
• 160 MHz
QSPI_MEM_CLK is always equal to 
CORE_CLK except in 1:1 mode (see 
Option F - Operation in 1:1 mode with 
CORE_CLK and AIPS_PLAT_CLK at 
same speed (For all chips except 
S32K388/S32K389)).
1. CORE_CLK is the frequency used for the CM7 cores, AXBS interfaces, and fast peripherals.
Table 151. System clock frequency limitations (For S32K312, S32K311, and S32K310)
System clock node
System clock divider
Maximum frequency allowed
Remarks
CORE_CLK
MC_CGM.MUX_0_DC_0[DIV]
• 120 MHz
CORE_CLK1 is always greater than 
or equal to AIPS_PLAT_CLK.
AIPS_PLAT_CLK
MC_CGM.MUX_0_DC_1[DIV]
• 80 MHz
AIPS_PLAT_CLK is always less than 
or equal to CORE_CLK.
AIPS_SLOW_CLK
MC_CGM.MUX_0_DC_2[DIV]
• 30 MHz
AIPS_SLOW_CLK is always less 
than or equal to AIPS_PLAT_CLK.
HSE_CLK
MC_CGM.MUX_0_DC_3[DIV]
• 120 MHz
When CORE_CLK is equal to or 
less than 120 MHz, HSE_CLK 
can be equal to CORE_CLK. 
When CORE_CLK is higher than 
120 MHz, HSE_CLK must be half of 
the CORE_CLK.
DCM_CLK
MC_CGM.MUX_0_DC_4[DIV]
• 48 MHz
DCM_CLK
1. CORE_CLK is the frequency used for the CM7 cores, AXBS interfaces, and fast peripherals.
 
The chip supports 1:1 clocking mode, whereby the core(s) are clocked at the same frequency as the slave ports 
(flash memory, PRAM controller, AIPS controller). See Option F - Operation in 1:1 mode with CORE_CLK and 
AIPS_PLAT_CLK at same speed (For all chips except S32K388/S32K389).
The frequencies in the table above are maximum frequencies for a specific clock. However, any clock frequency 
selected must adhere to the same clock divider ratios shown in System clocking configurations.
  NOTE  
24.7.2 System clocking configurations
The chip supports the clocking modes shown in Table 152. All clock configurations are implemented by appropriate 
register settings.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
972 / 5251


---
# 페이지 71

Table 152. System clocking configurations
Clocking 
options
Option A
Option B
Option C
Option D
Option E
Option E2
Option F
Option G
High-
performanc
e mode
Reduced 
speed 
mode
Boot 
(default) 
Standby 
configuratio
n (for low 
dynamic 
current 
consumptio
n)
FIRC 
divider 
bypassed
Low speed 
Run mode, 
clocked by 
divided 
FIRC
Very low 
speed Run 
mode, clock 
by divided 
FIRC
Operation in 
1:1 mode 
with core 
and AXBS 
at same 
speed
PLL 
providing 48 
MHz (test 
bench use 
case)
System 
clock 
source 
(SYS_CLK)
PLL_PHI0_
CLK
PLL_PHI0_
CLK
FIRC_CLK 
÷ 2
FIRC_CLK
FIRC_CLK 
÷ 2
FIRC_CLK 
÷ 16
PLL_PHI0_
CLK
PLL_PHI0_
CLK
PLL VCO 
frequency
480 MHz
480 MHz
—
—
—
—
480 MHz
480 MHz
PLL_PHI1_
CLK
K344: 240 
MHz
(VCO ÷ 2)
K342: 160 
MHz
(VCO ÷ 3)
K344: 240 
MHz
(VCO ÷ 2)
K342: 160 
MHz
(VCO ÷ 3)
—
—
—
—
K344: 240 
MHz
(VCO/2)
K342: 160 
MHz
(VCO/3)
—
PLL_PHI0_
CLK
160 MHz
(VCO ÷ 3)
120 MHz
(VCO ÷ 4)
—
—
—
—
160 MHz
(VCO ÷ 3)
96 MHz
(VCO ÷ 5)
CORE_CLK 
(application 
cores, 
AXBS, 
SRAM, 
AIPS0, 
flash 
memory 
controller 
port clock, 
QSPI 
memory 
clock, fast-
speed 
peripherals 
clock)
160 MHz
(SYS_CLK)
120 MHz
(SYS_CLK)
24 MHz
(FIRC_CLK 
÷ 2)
48 MHz
(FIRC)
3 MHz
((FIRC ÷ 2) 
÷ 8)
187.5 kHz
((FIRC ÷ 
16) ÷ 16)
80 MHz
(SYS_CLK 
÷ 2)
48 MHz
(SYS_CLK 
÷ 2)
QSPI mem 
clock
160 MHz
120 MHz
—
—
—
—
160 MHz
—
AIPS_PLAT
_CLK 
(medium-
80 MHz
60 MHz
24 MHz
48 MHz
3 MHz
187.5 kHz
80 MHz
48 MHz
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
973 / 5251


---
# 페이지 72

Table 152. System clocking configurations (continued)
Clocking 
options
Option A
Option B
Option C
Option D
Option E
Option E2
Option F
Option G
High-
performanc
e mode
Reduced 
speed 
mode
Boot 
(default) 
Standby 
configuratio
n (for low 
dynamic 
current 
consumptio
n)
FIRC 
divider 
bypassed
Low speed 
Run mode, 
clocked by 
divided 
FIRC
Very low 
speed Run 
mode, clock 
by divided 
FIRC
Operation in 
1:1 mode 
with core 
and AXBS 
at same 
speed
PLL 
providing 48 
MHz (test 
bench use 
case)
speed 
peripheral 
clock
AIPS_SLO
W_CLK 
(slow-speed 
peripheral 
clock)
40 MHz
30 MHz
12 MHz
24 MHz
1.5 MHz
93.75 kHz
40 MHz
24 MHz
DCM/
DCF_CLK
40 MHz
30 MHz
24 MHz
48 MHz
3 MHz
187.5 kHz
40 MHz
48 MHz
HSE_CLK
80 MHz
K34x: 
60/120 MHz
K31x: 
60/120 MHz
24 MHz
48 MHz
3 MHz
187.5 kHz
80 MHz
48 MHz
LBIST_CLK
40 MHz
30 MHz
—
—
—
—
40 MHz
—
QSPI_SFC
K
K344: 120 
MHz (QSPI 
only)
80 MHz 
(QSPI + 
ENET RMII)
K342: 80 
MHz
K344: 120 
MHz (QSPI 
only)
80 MHz 
(QSPI + 
ENET RMII)
K342: 80 
MHz
—
—
—
—
K344: 120 
MHz (QSPI 
only)
80 MHz 
(QSPI + 
ENET RMII)
—
 
In system clocking configurations where CORE_CLK and AIPS_PLAT_CLK are configured for operation at same 
frequency, the RAM wait states and flash memory read/write wait cycles need to be configured. See Clock Option 
B in Gasket Configurations section for RAM wait states and gasket configurations for clocking options.
The PLL should only be enabled if it is used as the system clock source. When the FIRC is used directly as the 
system clock, the PLL must be disabled.
While enabling PLL, the PMC last mile regulator should be enabled first, by configuring PMC_CONFIG[LMEN] 
and PMC_CONFIG[LMBCTLEN] (in case of external BJT). The last mile regulator should be disabled after PLL 
is disabled.
PLL can be locked at minimum 640 MHz and then 8 MHz can be achieved with dividers in series - PLL divider(divide 
by 16) and CGM divider(divide by 5).
  NOTE  
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
974 / 5251


---
# 페이지 73

24.7.2.1
Option A++ - Very High Performance mode (CM7_CORE_CLK @ 320 MHz) (For S32K388/S32K389)
This option is only available in Run mode.
Table 153. Option A++ - Very High Performance mode (CM7_CORE_CLK @ 320 MHz) (For S32K388/S32K389)
Clocking options
Clock frequencies 1
S32K388/S32K389
PLL VCO frequency
640 MHz
PLLODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
640 MHz
(0001b)
FIRC_CLK
(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])
48 MHz
(11b)
PLL_PHI1_CLK-related clocks 2
PLL_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
160 MHz
(0011b)
200 MHz
(0011b)
PLL_AUX-related clocks 3
PLL_AUX_VCO_CLK
1000 MHz
PLL_AUXODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
500 MHz
(0010b)
PLL_AUX_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
250 MHz
(0001b)
PLL_AUX_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
25 MHz
(10011b)
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
125 MHz 4
(0000b)
GMAC0_CLK_TX
(MC_CGM.MUX_8_DC_0[DIV])
125 MHz 4
(0000b)
GMAC1_CLK_TX
(MC_CGM.MUX_16_DC_0[DIV])
125 MHz 4
(0000b)
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
For fast pads
125 MHz 4
(0000b)
For standard-plus pads
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
975 / 5251


---
# 페이지 74

Table 153. Option A++ - Very High Performance mode (CM7_CORE_CLK @ 320 MHz) (For S32K388/S32K389) 
(continued)
Clocking options
Clock frequencies 1
S32K388/S32K389
25 MHz 4
(0100b)
PLL_PHI0_CLK-related clocks 5
PLL_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
320 MHz
(0001b)
CM7_CORE_CLK
(MC_CGM.MUX_0_DC_7[DIV])
320 MHz
(0000b)
CORE_CLK
• AXBS
• SRAM
• Flash memory controller port clock
• AIPS0 (high-speed peripheral clock)
(MC_CGM.MUX_0_DC_0[DIV])
160 MHz
(0001b)
QSPI_MEM_CLK
(MC_CGM.MUX_0_DC_6[DIV])
160 MHz
(0001b)
AIPS_PLAT_CLK (medium-speed peripheral clock)
(MC_CGM.MUX_0_DC_1[DIV])
80 MHz
(0011b)
AIPS_SLOW_CLK (slow-speed peripheral clock)
(MC_CGM.MUX_0_DC_2[DIV])
40 MHz
(0111b)
DCM_CLK
(MC_CGM.MUX_0_DC_4[DIV])
40 MHz
(0111b)
HSE_CLK
(MC_CGM.MUX_0_DC_3[DIV])
160 MHz
(0001b)
LBIST_CLK
(MC_CGM.MUX_0_DC_5[DIV])
40 MHz
(0111b)
1. This table is only applicable for S32K388/S32K389.
2. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1001b.
3. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1100b.
4. The final clock frequency is derived from additional divider stages. See the chip's clock diagrams for details.
5. MC_CGM.MUX_0_CSC[SELCTL] must equal 1000b.
24.7.2.2
Option A+ - Very High Performance mode (CM7_CORE_CLK @ 240 MHz) (For S32K388/S32K389)
This option is only available in Run mode.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
976 / 5251


---
# 페이지 75

Table 154. Option A+ - Very High Performance mode (CM7_CORE_CLK @ 240 MHz) (For S32K388/S32K389)
Clocking options
Clock frequencies
S32K388/S32K3891
PLL VCO frequency
960 MHz
PLLODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
480 MHz
(0010b)
FIRC_CLK
(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])
48 MHz
(11b)
PLL_PHI1_CLK-related clocks 2
PLL_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
160 MHz
(0010b)
PLL_AUX-related clocks 3
PLL_AUX_VCO_CLK
1000 MHz
PLLAUXODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
500 MHz
(0010b)
PLL_AUX_PHI0_CLK
PLLODIV_0[DIV]
250 MHz
(0001b)
PLL_AUX_PHI1_CLK
PLLODIV_1[DIV]
25 MHz
(10011b)
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
125 MHz4
(0000b)
GMAC0_CLK_TX
(MC_CGM.MUX_8_DC_0[DIV])
125 MHz 4
(0000b)
GMAC1_CLK_TX
(MC_CGM.MUX_16_DC_0[DIV])
125 MHz 4
(0000b)
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
For fast pads
125 MHz 4
(0000b)
For standard-plus pads
25 MHz 4
(0100b)
PLL_PHI0_CLK-related clocks 5
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
977 / 5251


---
# 페이지 76

Table 154. Option A+ - Very High Performance mode (CM7_CORE_CLK @ 240 MHz) (For S32K388/S32K389) 
(continued)
Clocking options
Clock frequencies
S32K388/S32K3891
PLL_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
240 MHz
(0001b)
CM7_CORE_CLK
(MC_CGM.MUX_0_DC_7[DIV])
240 MHz
(0000b)
CORE_CLK
• AXBS
• SRAM
• Flash memory controller port clock
• AIPS0 (high-speed peripheral clock)
(MC_CGM.MUX_0_DC_0[DIV])
120 MHz
(0001b)
QSPI_MEM_CLK
(MC_CGM.MUX_0_DC_6[DIV])
120 MHz
(0001b)
AIPS_PLAT_CLK (medium-speed peripheral clock)
(MC_CGM.MUX_0_DC_1[DIV])
60 MHz
(0011b)
AIPS_SLOW_CLK (slow-speed peripheral clock)
(MC_CGM.MUX_0_DC_2[DIV])
30 MHz
(0111b)
DCM_CLK
(MC_CGM.MUX_0_DC_4[DIV])
30 MHz
(0111b)
HSE_CLK
(MC_CGM.MUX_0_DC_3[DIV])
120 MHz
(0001b)
LBIST_CLK
(MC_CGM.MUX_0_DC_5[DIV])
30 MHz
(0111b)
1. This table is only applicable for S32K388/S32K389.
2. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1001b.
3. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1100b.
4. The final clock frequency is derived from additional divider stages. See the chip's clock diagrams for details.
5. MC_CGM.MUX_0_CSC[SELCTL] must equal 1000b.
24.7.2.3
Option A+ - Very High Performance mode (CORE_CLK @ 240 MHz) (For S32K328, S32K338, 
S32K348, and S32K358)
This option is only available in Run mode.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
978 / 5251


---
# 페이지 77

Table 155. Option A+ - High Performance mode (CORE_CLK @ 240 MHz)
Clocking options
Clock frequencies
S32K358, S32K348, S32K338, and S32K3281
PLL VCO frequency
960 MHz
PLLODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
480 MHz
(0010b)
FIRC_CLK
(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])
48 MHz
(11b)
PLL_PHI1_CLK-related clocks 2
PLL_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
480 MHz
(0000b)
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
120 MHz 3
(0000b)
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
For fast pads
120 MHz 3
(0001b)
PLL_AUX-related clocks 4
PLL_AUX_VCO_CLK
1000 MHz
800 MHz
PLLAUXODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
500 MHz
(0010b)
400 MHz
(0010b)
PLL_AUX_PHI0_CLK-related clocks
PLL_AUX_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
500 MHz
(0000b)
400 MHz
(0000b)
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
NA
100 MHz 3
(0000b)
GMAC_CLK_TX
(MC_CGM.MUX_8_DC_0[DIV])
125 MHz 3
(0001b)
NA
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
For standard-plus pads
25 MHz 3
(1001b)
NA
PLL_AUX_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
25 MHz
(10011b)
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
979 / 5251


---
# 페이지 78

Table 155. Option A+ - High Performance mode (CORE_CLK @ 240 MHz) (continued)
Clocking options
Clock frequencies
S32K358, S32K348, S32K338, and S32K3281
PLL_AUX_PHI2_CLK
(PLLDIG.PLLODIV_2[DIV])
100 MHz
(0100b)
PLL_PHI0_CLK-related clocks 5
PLL_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
240 MHz
(0001b)
CORE_CLK
• Application cores
• AXBS
• SRAM
• Flash memory controller port clock
• AIPS0 (high-speed peripheral clock)
(MC_CGM.MUX_0_DC_0[DIV])
240 MHz
(0000b)
QSPI_MEM_CLK
(MC_CGM.MUX_0_DC_6[DIV])
240 MHz
(0000b)
AIPS_PLAT_CLK (medium-speed peripheral clock)
(MC_CGM.MUX_0_DC_1[DIV])
120 MHz
(0001b)
AIPS_SLOW_CLK (slow-speed peripheral clock)
(MC_CGM.MUX_0_DC_2[DIV])
60 MHz
(0011b)
DCM_CLK
(MC_CGM.MUX_0_DC_4[DIV])
60 MHz
(0011b)
HSE_CLK
(MC_CGM.MUX_0_DC_3[DIV])
120 MHz
(0001b)
LBIST_CLK
(MC_CGM.MUX_0_DC_5[DIV])
60 MHz
(0011b)
1. This table is only applicable for S32K328, S32K338, S32K348, and S32K358.
2. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1001b.
3. The final clock frequency is derived from additional divider stages. See the chip's clock diagrams for details.
4. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1100b.
5. MC_CGM.MUX_0_CSC[SELCTL] must equal 1000b.
24.7.2.4
Option A - High Performance mode (CM7_CORE_CLK @ 160 MHz) (For S32K388/S32K389
This option is only available in Run mode.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
980 / 5251


---
# 페이지 79

Table 156. Option A - High Performance mode (CM7_CORE_CLK @ 160 MHz) (For S32K388/S32K389
Clocking options
Clock frequencies
S32K388/S32K3891
PLL VCO frequency
640 MHz
PLLODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
640 MHz
(0001b)
FIRC_CLK
(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])
48 MHz
(11b)
PLL_PHI1_CLK-related clocks 2
PLL_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
160 MHz
(0011b)
PLL_AUX-related clocks 3
PLL_AUX_VCO_CLK
1000 MHz
PLLAUXODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
500 MHz
(0010b)
PLL_AUX_PHI0_CLK
PLLODIV_0[DIV]
250 MHz
(0001b)
PLL_AUX_PHI1_CLK
PLLODIV_1[DIV]
25 MHz
(10011b)
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
125 MHz 4
(0000b)
GMAC0_CLK_TX
(MC_CGM.MUX_8_DC_0[DIV])
125 MHz 4
(0000b)
GMAC1_CLK_TX
(MC_CGM.MUX_16_DC_0[DIV])
125 MHz 4
(0000b)
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
For fast pads
125 MHz 4
(0000b)
For standard-plus pads
25 MHz 4
(0100b)
PLL_PHI0_CLK-related clocks 5
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
981 / 5251


---
# 페이지 80

Table 156. Option A - High Performance mode (CM7_CORE_CLK @ 160 MHz) (For S32K388/S32K389 (continued)
Clocking options
Clock frequencies
S32K388/S32K3891
PLL_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
320 MHz
(0001b)
CM7_CORE_CLK
(MC_CGM.MUX_0_DC_7[DIV])
160 MHz
(0001b)
CORE_CLK
• AXBS
• SRAM
• Flash memory controller port clock
• AIPS0 (high-speed peripheral clock)
(MC_CGM.MUX_0_DC_0[DIV])
160 MHz
(0001b)
QSPI_MEM_CLK
(MC_CGM.MUX_0_DC_6[DIV])
160 MHz
(0001b)
AIPS_PLAT_CLK (medium-speed peripheral clock)
(MC_CGM.MUX_0_DC_1[DIV])
80 MHz
(0011b)
AIPS_SLOW_CLK (slow-speed peripheral clock)
(MC_CGM.MUX_0_DC_2[DIV])
40 MHz
(0111b)
DCM_CLK
(MC_CGM.MUX_0_DC_4[DIV])
40 MHz
(0111b)
HSE_CLK
(MC_CGM.MUX_0_DC_3[DIV])
160 MHz
(0001b)
LBIST_CLK
(MC_CGM.MUX_0_DC_5[DIV])
40 MHz
(0111b)
1. This table is only applicable for S32K388/S32K389.
2. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1001b.
3. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1100b.
4. The final clock frequency is derived from additional divider stages. See the chip's clock diagrams for details.
5. MC_CGM.MUX_0_CSC[SELCTL] must equal 1000b.
24.7.2.5
Option A - High Performance mode (CORE_CLK @ 160 MHz)
This option is only available in Run mode.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
982 / 5251


---
# 페이지 81

Table 157. Option A - High Performance mode (CORE_CLK @ 160 MHz)
Clocking options
Clock frequencies
S32K344, S32K324, S32K314, 
S32K342, S32K341, and 
S32K322 1
S32K328, S32K338, S32K348, and S32K358
PLL VCO frequency
960 MHz
960 MHz
PLLODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
480 MHz
(0010b)
480 MHz
(0010b)
FIRC_CLK
(HSE_B.CONFIG_REG_GPR[FIRC_DIV
_SEL])
48 MHz
(11b)
48 MHz
(11b)
PLL_PHI1_CLK-related clocks 2
PLL_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
240 MHz
(0001b)
160 MHz
(0010b)
480 MHz
(0000b)
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
120 MHz
(0001b)
80 MHz
(0001b)
120 MHz 3
(0000b)
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
For fast pads
For fast pads
120 MHz
(0001b)
80 MHz
(0001b)
120 MHz 3
(0001b)
For standard-plus pads
24 MHz
(1001b)
16 MHz
(1001b)
PLL_AUX-related clocks
PLL_AUX_VCO_CLK
NA
1000 MHz
800 MHz
PLLAUXODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
NA
500 MHz
(0010b)
400 MHz
(0010b)
PLL_AUX_PHI0_CLK-related clocks
PLL_AUX_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
NA
500 MHz
(0000b)
400 MHz
(0000b)
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
NA
NA
100 MHz 3
(0000b)
GMAC_CLK_TX
(MC_CGM.MUX_8_DC_0[DIV])
NA
125 MHz 3
(0001b)
NA
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
983 / 5251


---
# 페이지 82

Table 157. Option A - High Performance mode (CORE_CLK @ 160 MHz) (continued)
Clocking options
Clock frequencies
S32K344, S32K324, S32K314, 
S32K342, S32K341, and 
S32K322 1
S32K328, S32K338, S32K348, and S32K358
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
NA
25 MHz 3
(1001b)
NA
PLL_AUX_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
NA
25 MHz
(10011b)
PLL_AUX_PHI2_CLK
(PLLDIG.PLLODIV_2[DIV])
NA
100 MHz
(0100b)
PLL_PHI0_CLK-related clocks 4
PLL_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
160 MHz
(0010b)
160 MHz
(0010b)
CORE_CLK
• Application cores
• AXBS
• SRAM
• Flash memory controller port clock
• AIPS0 (high-speed peripheral clock)
(MC_CGM.MUX_0_DC_0[DIV])
160 MHz
(0000b)
160 MHz
(0000b)
QSPI_MEM_CLK
(MC_CGM.MUX_0_DC_6[DIV])
160 MHz
(0000b)
160 MHz
(0000b)
AIPS_PLAT_CLK (medium-speed 
peripheral clock)
(MC_CGM.MUX_0_DC_1[DIV])
80 MHz
(0001b)
80 MHz
(0001b)
AIPS_SLOW_CLK (slow-speed 
peripheral clock)
(MC_CGM.MUX_0_DC_2[DIV])
40 MHz
(0011b)
40 MHz
(0011b)
DCM_CLK
(MC_CGM.MUX_0_DC_4[DIV])
40 MHz
(0011b)
40 MHz
(0011b)
HSE_CLK
(MC_CGM.MUX_0_DC_3[DIV])
80 MHz
(0001b)
80 MHz
(0001b)
LBIST_CLK
(MC_CGM.MUX_0_DC_5[DIV])
40 MHz
(0011b)
40 MHz
(0011b)
1. This table does not apply to S32K310, S32K311, and S32K312.
2. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1001b.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
984 / 5251


---
# 페이지 83

3. The final clock frequency is derived from additional divider stages. See the chip's clock diagrams for details.
4. MC_CGM.MUX_0_CSC[SELCTL] must equal 1000b.
24.7.2.6
Option B - Reduced Speed mode (CORE_CLK @ 120 MHz)
This option is only available in Run mode.
Table 158. Option B - Reduced Speed mode (CORE_CLK @ 120 MHz)
Clocking options
Clock frequencies
S32K344, S32K324, 
S32K314, S32K342, 
S32K341, and 
S32K322
S32K310, S32K311, 
and S32K312
S32K328, S32K338, S32K348, and 
S32K358
PLL VCO frequency
960 MHz
960 MHz
960 MHz
PLLODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
480 MHz
(0010b)
240 MHz
(0100b)
480 MHz
(0010b)
FIRC_CLK
(HSE_B.CONFIG_REG_GPR[FIRC
_DIV_SEL])
48 MHz
(11b)
PLL_PHI1_CLK-related clocks 1, 2
PLL_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
240 MHz
(0001b)
160 MHz
(0010b)
48 MHz
(0100b)
480 MHz
(0000b)
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
120 MHz
(001b)
80 MHz
(001b)
—
120 MHz3
(0000b)
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
For fast pads
—
For fast pads
120 MHz
(001b)
80 MHz
(001b)
—
120 MHz3
(0001b)
For standard-plus pads
—
24 MHz
(1001b)
16 MHz 
(1001b)
—
PLL_AUX-related clocks4
PLL_AUX_VCO_CLK
NA
1000 MHz
800 MHz
PLLAUXODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
NA
500 MHz
(0010b)
400 MHz
(0010b)
PLL_AUX_PHI0_CLK-related clocks
PLL_AUX_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
NA
500 MHz
(0000b)
400 MHz
(0000b)
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
985 / 5251


---
# 페이지 84

Table 158. Option B - Reduced Speed mode (CORE_CLK @ 120 MHz) (continued)
Clocking options
Clock frequencies
S32K344, S32K324, 
S32K314, S32K342, 
S32K341, and 
S32K322
S32K310, S32K311, 
and S32K312
S32K328, S32K338, S32K348, and 
S32K358
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
NA
NA
100 MHz3
(0000b)
GMAC_CLK_TX
(MC_CGM.MUX_8_DC_0[DIV])
NA
125 MHz 3
(0001b)
NA
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
NA
For standard-plus pads
25 MHz3
(1001b)
NA
PLL_AUX_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
NA
25 MHz
(10011b)
PLL_AUX_PHI2_CLK
(PLLDIG.PLLODIV_2[DIV])
NA
100 MHz
(0100b)
PLL_PHI0_CLK-related clocks 5
PLL_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
120 MHz
(011b)
120 MHz
(001b)
120 MHz
(011b)
CORE_CLK
• Application cores
• AXBS
• SRAM
• Flash memory controller port 
clock
• AIPS0 (high-speed peripheral 
clock)
(MC_CGM.MUX_0_DC_0[DIV])
120 MHz
(000b)
120 MHz
(000b)
120 MHz
(000b)
QSPI_MEM_CLK
(MC_CGM.MUX_0_DC_6[DIV])
120 MHz
(000b)
—
120 MHz
(000b)
AIPS_PLAT_CLK (medium-speed 
peripheral clock)
(MC_CGM.MUX_0_DC_1[DIV])
60 MHz
(001b)
60 MHz
(001b)
60 MHz
(001b)
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
986 / 5251


---
# 페이지 85

Table 158. Option B - Reduced Speed mode (CORE_CLK @ 120 MHz) (continued)
Clocking options
Clock frequencies
S32K344, S32K324, 
S32K314, S32K342, 
S32K341, and 
S32K322
S32K310, S32K311, 
and S32K312
S32K328, S32K338, S32K348, and 
S32K358
AIPS_SLOW_CLK (slow-speed 
peripheral clock)
(MC_CGM.MUX_0_DC_2[DIV])
30 MHz
(011b)
30 MHz
(011b)
30 MHz
(011b)
DCM_CLK
(MC_CGM.MUX_0_DC_4[DIV])
30 MHz
(011b)
30 MHz
(011b)
30 MHz
(011b)
HSE_CLK
(MC_CGM.MUX_0_DC_3[DIV])
120 MHz6
(000b)
60 MHz
(001b)
120 MHz6
(000b)
60 MHz
(001b)
120 MHz6
(000b)
60 MHz
(001b)
LBIST_CLK
(MC_CGM.MUX_0_DC_5[DIV])
30 MHz
(011b)
30 MHz
(011b)
30 MHz
(011b)
1. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1001b.
2. Do not use the combination of different frequencies mentioned below across the 2x2 matrix. The values shown in each cell 
are valid and must not be clubbed with the values mentioned in any other cells.
3. The final clock frequency is derived from additional divider stages. See the chip's clock diagrams for details.
4. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1100b.
5. MC_CGM.MUX_0_CSC[SELCTL] must equal 1000b.
6. When 120 MHz is selected for HSE_CLK while AIPS_SLOW_CLK is 30 MHz, an DCF record for UTEST_MISC DCF client 
should be added with setting HSE_CLK_MODE_AND_GSKT_CTRL bit field as 2'b10 or 2'b11.
24.7.2.7
Option C - Boot Standby mode (CM7_CORE_CLK @ 24 MHz) (For S32K388/S32K389)
Table 159. Option C - Boot Standby mode (CM7_CORE_CLK @ 24 MHz) (For S32K388/S32K389)
Clocking options
Clock frequencies
S32K388/S32K3891
PLL VCO frequency
-
PLLODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
-
FIRC_CLK
(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])
24 MHz2
PLL_PHI1_CLK-related clocks 3
PLL_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
-
PLL_AUX-related clocks 4
PLL_AUX_VCO_CLK
-
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
987 / 5251


---
# 페이지 86

Table 159. Option C - Boot Standby mode (CM7_CORE_CLK @ 24 MHz) (For S32K388/S32K389) (continued)
Clocking options
Clock frequencies
S32K388/S32K3891
PLLAUXODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
-
PLL_AUX_PHI0_CLK
PLLODIV_0[DIV]
-
PLL_AUX_PHI1_CLK
PLLODIV_1[DIV]
-
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
-
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
-
PLL_PHI0_CLK-related clocks 5
PLL_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
-
CM7_CORE_CLK
(MC_CGM.MUX_0_DC_7[DIV])
24 MHz
(0000b)
CORE_CLK
• AXBS
• SRAM
• Flash memory controller port clock
• AIPS0 (high-speed peripheral clock)
(MC_CGM.MUX_0_DC_0[DIV])
24 MHz
(0000b)
QSPI_MEM_CLK
(MC_CGM.MUX_0_DC_6[DIV])
-
AIPS_PLAT_CLK (medium-speed peripheral clock)
(MC_CGM.MUX_0_DC_1[DIV])
24 MHz
(0000b)
AIPS_SLOW_CLK (slow-speed peripheral clock)
(MC_CGM.MUX_0_DC_2[DIV])
12 MHz
(0001b)
DCM_CLK
(MC_CGM.MUX_0_DC_4[DIV])
24 MHz
(0000b)
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
988 / 5251


---
# 페이지 87

Table 159. Option C - Boot Standby mode (CM7_CORE_CLK @ 24 MHz) (For S32K388/S32K389) (continued)
Clocking options
Clock frequencies
S32K388/S32K3891
HSE_CLK
(MC_CGM.MUX_0_DC_3[DIV])
24 MHz
(0000b)
LBIST_CLK
(MC_CGM.MUX_0_DC_5[DIV])
-
1. This table is only applicable for S32K388/S32K389.
2. The FIRC_DIV_SEL is configured by the sBAF code. It is set to 11b after reset or normal standby exit and FIRC_CLK is 48 
MHz. In case of fast standby exit, FIRC_DIV_SEL is 00b and FIRC_CLK is 24 MHz.
3. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] values are don't care since QSPI_SFCK and 
TRACE_CLK are not used in this use case.
4. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1100b.
5. MC_CGM.MUX_0_CSC[SELCTL] must equal 0000b.
24.7.2.8
Option C - Boot Standby mode (CORE_CLK @ 24 MHz)
Table 160. Option C - Boot Standby mode (CORE_CLK @ 24 MHz)
Clocking options
Clock frequencies
S32K3xx1
PLL VCO frequency
—
PLLODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
—
FIRC_CLK
(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])
24 MHz2
(00b)
PLL_PHI1_CLK-related clocks 3
PLL_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
—
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
—
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
—
PLL_PHI0_CLK-related clocks 4
PLL_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
—
LBIST_CLK
(MC_CGM.MUX_0_DC_5[DIV])
—
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
989 / 5251


---
# 페이지 88

Table 160. Option C - Boot Standby mode (CORE_CLK @ 24 MHz) (continued)
Clocking options
Clock frequencies
S32K3xx1
QSPI_MEM_CLK
(MC_CGM.MUX_0_DC_6[DIV])
—
CORE_CLK
• Application cores
• AXBS
• SRAM
• Flash memory controller port clock
• AIPS0 (high-speed peripheral clock)
(MC_CGM.MUX_0_DC_0[DIV])
24 MHz
(0000b)
AIPS_PLAT_CLK (medium-speed peripheral clock)
(MC_CGM.MUX_0_DC_1[DIV])
24 MHz
(0000b)
AIPS_SLOW_CLK (slow-speed peripheral clock)
(MC_CGM.MUX_0_DC_2[DIV])
12 MHz
(0001b)
DCM_CLK
(MC_CGM.MUX_0_DC_4[DIV])
24 MHz
(0000b)
HSE_CLK
(MC_CGM.MUX_0_DC_3[DIV])
24 MHz
(0000b)
1. This table is applicable for all S32K3xx variants except S32K388/S32K389.
2. The FIRC_DIV_SEL is configured by the sBAF code. It is set to 11b after reset or normal standby exit and FIRC_CLK is 48 
MHz. In case of fast standby exit, FIRC_DIV_SEL is 00b and FIRC_CLK is 24 MHz.
3. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] values are don't care since QSPI_SFCK and 
TRACE_CLK are not used in this use case.
4. MC_CGM.MUX_0_CSC[SELCTL] must equal 0000b.
24.7.2.9
Option D - Low-Speed Run mode (CM7_CORE_CLK @ 48 MHz) (For S32K388/S32K389)
Table 161. Option D - Low-Speed Run mode (CM7_CORE_CLK @ 48 MHz) (For S32K388/S32K389)
Clocking options
Clock frequencies
S32K388/S32K3891
PLL VCO frequency
-
PLLODIV2_CLK (PLLDIG.PLLDV[ODIV2])
-
FIRC_CLK
(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])
48 MHz
(11b)
PLL_PHI1_CLK-related clocks 2
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
990 / 5251


---
# 페이지 89

Table 161. Option D - Low-Speed Run mode (CM7_CORE_CLK @ 48 MHz) (For S32K388/S32K389) (continued)
Clocking options
Clock frequencies
S32K388/S32K3891
PLL_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
-
PLL_AUX-related clocks 3
PLL_AUX_VCO_CLK
-
PLLAUXODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
-
PLL_AUX_PHI0_CLK
PLLODIV_0[DIV]
-
PLL_AUX_PHI1_CLK
PLLODIV_1[DIV]
-
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
-
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
-
PLL_PHI0_CLK-related clocks 4
PLL_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
-
CM7_CORE_CLK
(MC_CGM.MUX_0_DC_7[DIV])
48 MHz
(0000b)
CORE_CLK
• AXBS
• SRAM
• Flash memory controller port clock
• AIPS0 (high-speed peripheral clock)
(MC_CGM.MUX_0_DC_0[DIV])
48 MHz
(0000b)
QSPI_MEM_CLK
(MC_CGM.MUX_0_DC_6[DIV])
-
AIPS_PLAT_CLK (medium-speed peripheral clock)
(MC_CGM.MUX_0_DC_1[DIV])
48 MHz
(0000b)
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
991 / 5251


---
# 페이지 90

Table 161. Option D - Low-Speed Run mode (CM7_CORE_CLK @ 48 MHz) (For S32K388/S32K389) (continued)
Clocking options
Clock frequencies
S32K388/S32K3891
AIPS_SLOW_CLK (slow-speed peripheral clock)
(MC_CGM.MUX_0_DC_2[DIV])
24 MHz
(0001b)
DCM_CLK
(MC_CGM.MUX_0_DC_4[DIV])
48 MHz
(0000b)
HSE_CLK
(MC_CGM.MUX_0_DC_3[DIV])
48 MHz
(0000b)
LBIST_CLK
(MC_CGM.MUX_0_DC_5[DIV])
-
1. This table is only applicable for S32K388/S32K389.
2. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] values are don't care since QSPI_SFCK and 
TRACE_CLK are not used in this use case.
3. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1100b.
4. MC_CGM.MUX_0_CSC[SELCTL] must equal 0000b.
24.7.2.10
Option D - Low-Speed Run mode (CORE_CLK @ 48 MHz)
Table 162. Option D - Low-Speed Run mode (CORE_CLK @ 48 MHz)
Clocking options
Clock frequencies
S32K3xx1
PLL VCO frequency
—
PLLODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
—
FIRC_CLK
(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])
48 MHz
(11b)
PLL_PHI1_CLK-related clocks 2
PLL_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
—
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
—
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
—
PLL_PHI0_CLK-related clocks 3
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
992 / 5251


---
# 페이지 91

Table 162. Option D - Low-Speed Run mode (CORE_CLK @ 48 MHz) (continued)
Clocking options
Clock frequencies
S32K3xx1
PLL_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
—
LBIST_CLK
(MC_CGM.MUX_0_DC_5[DIV])
—
QSPI_MEM_CLK
(MC_CGM.MUX_0_DC_6[DIV])
—
CORE_CLK
• Application cores
• AXBS
• SRAM
• Flash memory controller port clock
• AIPS0 (high-speed peripheral clock)
(MC_CGM.MUX_0_DC_0[DIV])
48 MHz
(0000b)
AIPS_PLAT_CLK (medium-speed peripheral clock)
(MC_CGM.MUX_0_DC_1[DIV])
48 MHz
(0000b)
AIPS_SLOW_CLK (slow-speed peripheral clock)
(MC_CGM.MUX_0_DC_2[DIV])
24 MHz
(0001b)
DCM_CLK
(MC_CGM.MUX_0_DC_4[DIV])
48 MHz
(0000b)
HSE_CLK
(MC_CGM.MUX_0_DC_3[DIV])
48 MHz
(0000b)
1. This table is applicable for all S32K3xx variants except S32K388/S32K389.
2. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] values are don't care since QSPI_SFCK and 
TRACE_CLK are not used in this use case.
3. MC_CGM.MUX_0_CSC[SELCTL] must equal 0000b.
24.7.2.11
Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz) (For S32K388/S32K389)
Table 163. Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz) (For S32K388/S32K389)
Clocking options
Clock frequencies
S32K388/S32K3891
PLL VCO frequency
—
PLLODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
—
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
993 / 5251


---
# 페이지 92

Table 163. Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz) (For S32K388/S32K389) (continued)
Clocking options
Clock frequencies
S32K388/S32K3891
FIRC_CLK
(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])
3 MHz2
(10b)
PLL_PHI1_CLK-related clocks 3
PLL_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
—
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
—
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
—
PLL_PHI0_CLK-related clocks 4
PLL_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
—
LBIST_CLK
(MC_CGM.MUX_0_DC_5[DIV])
—
QSPI_MEM_CLK
(MC_CGM.MUX_0_DC_6[DIV])
—
CM7_CORE_CLK
(MC_CGM.MUX_0_DC_7[DIV])
3 MHz
(0000b)
CORE_CLK
• AXBS
• SRAM
• Flash memory controller port clock
• AIPS0 (high-speed peripheral clock)
(MC_CGM.MUX_0_DC_0[DIV])
3 MHz
(0000b)
AIPS_PLAT_CLK (medium-speed peripheral clock)
(MC_CGM.MUX_0_DC_1[DIV])
3 MHz
(0000b)
AIPS_SLOW_CLK (slow-speed peripheral clock)
(MC_CGM.MUX_0_DC_2[DIV])
1.5 MHz
(0001b)
DCM_CLK
(MC_CGM.MUX_0_DC_4[DIV])
3 MHz
(0000b)
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
994 / 5251


---
# 페이지 93

Table 163. Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz) (For S32K388/S32K389) (continued)
Clocking options
Clock frequencies
S32K388/S32K3891
HSE_CLK
(MC_CGM.MUX_0_DC_3[DIV])
3 MHz
(0000b)
1. This table is only applicable for S32K388/S32K389.
2. The FIRC_DIV_SEL is configured by the sBAF code. It is set to 11b after reset or normal standby exit and FIRC_CLK is 48 
MHz. In case of fast standby exit, FIRC_DIV_SEL is 10b and FIRC_CLK is 3 MHz.
3. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] values are don't care since QSPI_SFCK and 
TRACE_CLK are not used in this use case.
4. MC_CGM.MUX_0_CSC[SELCTL] must equal 0000b.
 
For FIRC_CLK frequency modes less than 24 MHz, safety modules like the CMU_Fx_n must be disabled for safety 
applications, because safety applications are to run on the PLL clocks. The CMU_Fx_n will cause erroneous FHH 
events if not disabled.
  NOTE  
24.7.2.12
Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz)
Table 164. Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz)
Clocking options
Clock frequencies
S32K3xx1
PLL VCO frequency
—
PLLODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
—
FIRC_CLK
(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])
3 MHz2
(10b)
PLL_PHI1_CLK-related clocks 3
PLL_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
—
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
—
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
—
PLL_PHI0_CLK-related clocks 4
PLL_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
—
LBIST_CLK
(MC_CGM.MUX_0_DC_5[DIV])
—
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
995 / 5251


---
# 페이지 94

Table 164. Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz) (continued)
Clocking options
Clock frequencies
S32K3xx1
QSPI_MEM_CLK
(MC_CGM.MUX_0_DC_6[DIV])
—
CORE_CLK
• Application cores
• AXBS
• SRAM
• Flash memory controller port clock
• AIPS0 (high-speed peripheral clock)
(MC_CGM.MUX_0_DC_0[DIV])
3 MHz
(0000b)
AIPS_PLAT_CLK (medium-speed peripheral clock)
(MC_CGM.MUX_0_DC_1[DIV])
3 MHz
(0000b)
AIPS_SLOW_CLK (slow-speed peripheral clock)
(MC_CGM.MUX_0_DC_2[DIV])
1.5 MHz
(0001b)
DCM_CLK
(MC_CGM.MUX_0_DC_4[DIV])
3 MHz
(0000b)
HSE_CLK
(MC_CGM.MUX_0_DC_3[DIV])
3 MHz
(0000b)
1. This table is applicable for all S32K3xx variants except S32K388/S32K389.
2. The FIRC_DIV_SEL is configured by the sBAF code. It is set to 11b after reset or normal standby exit and FIRC_CLK is 48 
MHz. In case of fast standby exit, FIRC_DIV_SEL is 10b and FIRC_CLK is 3 MHz.
3. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] values are don't care since QSPI_SFCK and 
TRACE_CLK are not used in this use case.
4. MC_CGM.MUX_0_CSC[SELCTL] must equal 0000b.
 
For FIRC_CLK frequency modes less than 24 MHz, safety modules like the CMU_Fx_n must be disabled for safety 
applications, because safety applications are to run on the PLL clocks. The CMU_Fx_n will cause erroneous FHH 
events if not disabled.
  NOTE  
24.7.2.13
Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 KHz) (For S32K388/S32K389)
Table 165. Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 KHz) (For S32K388/S32K389)
Clocking options
Clock frequencies
S32K3xx1
PLL VCO frequency
—
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
996 / 5251


---
# 페이지 95

Table 165. Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 KHz) (For S32K388/S32K389) (continued)
Clocking options
Clock frequencies
S32K3xx1
PLLODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
—
FIRC_CLK
(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])
3 MHz2
(10b)
PLL_PHI1_CLK-related clocks 3
PLL_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
—
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
—
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
—
PLL_PHI0_CLK-related clocks 4
PLL_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
—
LBIST_CLK
(MC_CGM.MUX_0_DC_5[DIV])
—
QSPI_MEM_CLK
(MC_CGM.MUX_0_DC_6[DIV])
—
CM7_CORE_CLK
(MC_CGM.MUX_0_DC_7[DIV])
750 KHz
(0011b)
CORE_CLK
• AXBS
• SRAM
• Flash memory controller port clock
• AIPS0 (high-speed peripheral clock)
(MC_CGM.MUX_0_DC_0[DIV])
750 KHz
(0011b)
AIPS_PLAT_CLK (medium-speed peripheral clock)
(MC_CGM.MUX_0_DC_1[DIV])
750 KHz
(0011b)
AIPS_SLOW_CLK (slow-speed peripheral clock)
(MC_CGM.MUX_0_DC_2[DIV])
375 KHz
(0111b)
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
997 / 5251


---
# 페이지 96

Table 165. Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 KHz) (For S32K388/S32K389) (continued)
Clocking options
Clock frequencies
S32K3xx1
DCM_CLK
(MC_CGM.MUX_0_DC_4[DIV])
750 KHz
(0011b)
HSE_CLK
(MC_CGM.MUX_0_DC_3[DIV])
750 KHz
(0011b)
1. This table is only applicable for S32K388/S32K389.
2. The FIRC_DIV_SEL is configured by the sBAF code. It is set to 11b after reset or normal standby exit and FIRC_CLK is 48 
MHz. In case of fast standby exit, FIRC_DIV_SEL is 10b and FIRC_CLK is 3 MHz.
3. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] values are don't care since QSPI_SFCK and 
TRACE_CLK are not used in this use case.
4. MC_CGM.MUX_0_CSC[SELCTL] must equal 0000b.
 
For FIRC_CLK frequency modes less than 24 MHz, safety modules like the CMU_Fx_n must be disabled for safety 
applications, because safety applications are to run on the PLL clocks. The CMU_Fx_n will cause erroneous FHH 
events if not disabled.
  NOTE  
24.7.2.14
Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 KHz)
Table 166. Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 KHz)
Clocking options
Clock frequencies
S32K3xx1
PLL VCO frequency
—
PLLODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
—
FIRC_CLK
(HSE_B.CONFIG_REG_GPR[FIRC_DIV_SEL])
3 MHz2
(10b)
PLL_PHI1_CLK-related clocks 3
PLL_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
—
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
—
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
—
PLL_PHI0_CLK-related clocks 4
PLL_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
—
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
998 / 5251


---
# 페이지 97

Table 166. Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 KHz) (continued)
Clocking options
Clock frequencies
S32K3xx1
LBIST_CLK
(MC_CGM.MUX_0_DC_5[DIV])
—
QSPI_MEM_CLK
(MC_CGM.MUX_0_DC_6[DIV])
—
CORE_CLK
• Application cores
• AXBS
• SRAM
• Flash memory controller port clock
• AIPS0 (high-speed peripheral clock)
(MC_CGM.MUX_0_DC_0[DIV])
750 KHz
(0011b)
AIPS_PLAT_CLK (medium-speed peripheral clock)
(MC_CGM.MUX_0_DC_1[DIV])
750 KHz
(0011b)
AIPS_SLOW_CLK (slow-speed peripheral clock)
(MC_CGM.MUX_0_DC_2[DIV])
375 KHz
(0111b)
DCM_CLK
(MC_CGM.MUX_0_DC_4[DIV])
750 KHz
(0011b)
HSE_CLK
(MC_CGM.MUX_0_DC_3[DIV])
750 KHz
(0011b)
1. This table is applicable for all S32K3xx variants except S32K388/S32K389.
2. The FIRC_DIV_SEL is configured by the sBAF code. It is set to 11b after reset or normal standby exit and FIRC_CLK is 48 
MHz. In case of fast standby exit, FIRC_DIV_SEL is 10b and FIRC_CLK is 3 MHz.
3. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] values are don't care since QSPI_SFCK and 
TRACE_CLK are not used in this use case.
4. MC_CGM.MUX_0_CSC[SELCTL] must equal 0000b.
 
For FIRC_CLK frequency modes less than 24 MHz, safety modules like the CMU_Fx_n must be disabled for safety 
applications, because safety applications are to run on the PLL clocks. The CMU_Fx_n will cause erroneous FHH 
events if not disabled.
  NOTE  
24.7.2.15
Option F - Operation in 1:1 mode with CORE_CLK and AIPS_PLAT_CLK at same speed (For all chips 
except S32K388/S32K389)
This option is only available in Run mode.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
999 / 5251


---
# 페이지 98

Table 167. Option F - Operation in 1:1 mode with CORE_CLK and AIPS_PLAT_CLK at same speed
Clocking options
Clock frequencies
S32K344, S32K324, 
S32K314, S32K342, 
S32K341, and S32K322
S32K310, 
S32K311, 
and 
S32K312
S32K328, S32K338, S32K348, and 
S32K358
PLL VCO frequency
960 MHz
960 MHz
960 MHz
PLLODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
480 MHz
(0010b)
240 MHz
(0100b)
480 MHz
(0010b)
FIRC_CLK
(HSE_B.CONFIG_REG_GPR[FIRC_DIV
_SEL])
48 MHz
(11b)
PLL_PHI1_CLK-related clocks 1
PLL_PHI1_CLK
(PLLDIG.PLLODIV_1[DIV])
240 MHz
(0001b)
160 MHz
(0010b)
48 MHz
(0100b)
480 MHz
(0000b)
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
120 MHz
(001b)
80 MHz
(001b)
—
120 MHz2
(0000b)
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
For fast pads
—
For fast pads
120 MHz
(001b)
80 MHz
(001b)
—
120 MHz2
(0001b)
For standard-plus pads
—
24 MHz 
(1001b)
16 MHz
(1001b)
—
PLL_AUX-related clocks3
PLL_AUX_VCO_CLK
NA
1000 MHz
800 MHz
PLLAUXODIV2_CLK
(PLLDIG.PLLDV[ODIV2])
NA
500 MHz
(0000b)
400 MHz
(0000b)
PLL_AUX_PHI0_CLK-related clocks
PLL_AUX_PHI0_CLK 
(PLLDIG.PLLODIV_0[DIV])
NA
500 MHz
(0010b)
400 MHz
(0010b)
QSPI_SFCK
(MC_CGM.MUX_10_DC_0[DIV])
NA
NA
100 MHz2
(0000b)
GMAC_CLK_TX 
(MC_CGM.MUX_8_DC_0[DIV])
NA
125 MHz 2
(0001b)
NA
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1000 / 5251


---
# 페이지 99

Table 167. Option F - Operation in 1:1 mode with CORE_CLK and AIPS_PLAT_CLK at same speed (continued)
Clocking options
Clock frequencies
S32K344, S32K324, 
S32K314, S32K342, 
S32K341, and S32K322
S32K310, 
S32K311, 
and 
S32K312
S32K328, S32K338, S32K348, and 
S32K358
TRACE_CLK
(MC_CGM.MUX_11_DC_0[DIV])
NA
For standard-plus pads
25 MHz2
(1001b)
NA
PLL_AUX_PHI1_CLK 
(PLLDIG.PLLODIV_1[DIV])
NA
25 MHz
(10011b)
PLL_AUX_PHI2_CLK
(PLLDIG.PLLODIV_2[DIV])
NA
100 MHz
(0100b)
PLL_PHI0_CLK-related clocks 4
PLL_PHI0_CLK
(PLLDIG.PLLODIV_0[DIV])
160 MHz
(010b)
80 MHz
(010b)
160 MHz
(010b)
CORE_CLK
• Application cores
• AXBS
• SRAM
• Flash memory controller port clock
• AIPS0 (high-speed peripheral clock)
(MC_CGM.MUX_0_DC_0[DIV])
80 MHz
(001b)
80 MHz
(000b)
80 MHz
(001b)
QSPI_MEM_CLK
(MC_CGM.MUX_0_DC_6[DIV])
160 MHz
(000b)
—
160 MHz
(000b)
AIPS_PLAT_CLK (medium-speed 
peripheral clock)
(MC_CGM.MUX_0_DC_1[DIV])
80 MHz
(001b)
80 MHz
(000b)
80 MHz
(001b)
AIPS_SLOW_CLK (slow-speed 
peripheral clock)
(MC_CGM.MUX_0_DC_2[DIV])
40 MHz
(011b)
40 MHz
(001b)
40 MHz
(011b)
DCM_CLK
(MC_CGM.MUX_0_DC_4[DIV])
40 MHz
(011b)
40 MHz
(001b)
40 MHz
(011b)
HSE_CLK
(MC_CGM.MUX_0_DC_3[DIV])
80 MHz
(001b)
80 MHz
(000b)
80 MHz
(001b)
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1001 / 5251


---
# 페이지 100

Table 167. Option F - Operation in 1:1 mode with CORE_CLK and AIPS_PLAT_CLK at same speed (continued)
Clocking options
Clock frequencies
S32K344, S32K324, 
S32K314, S32K342, 
S32K341, and S32K322
S32K310, 
S32K311, 
and 
S32K312
S32K328, S32K338, S32K348, and 
S32K358
LBIST_CLK
(MC_CGM.MUX_0_DC_5[DIV])
40 MHz
(011b)
40 MHz
(001b)
40 MHz
(011b)
1. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1001b.
2. The final clock frequency is derived from additional divider stages. See the chip's clock diagrams for details.
3. MC_CGM.MUX_10_CSC[SELCTL] and MC_CGM.MUX_11_CSC[SELCTL] must equal 1100b.
4. MC_CGM.MUX_0_CSC[SELCTL] must equal 1000b.
24.7.3 Gasket configurations in various clocking modes
Table 168. Gasket configurations in various clocking modes (for S32K388/S32K389)
Gasket 
configuration
Option A+
+1
Option A+2
Option A3
Option C 
(Boot)4
Option D5
Option E6
Option E27
eDMA (S0)
1:1
Bypass / 1:1 (3 
priority)
1:1
Bypass
HSE_B
1:1
Bypass
AES_ACCEL
1:1
Bypass
AES_SLAVE
1:1
AIPS1/2/3
1:1
Bypass/1:1 (1 
priority)
1:1
Bypass
QuadSPI
2:1
Bypass
PRAMC
WS enabled
WS disabled
Cortex M7_Core
2:1
1:1
GMAC
1:1
BDRAM 64:32
1:2
1:1
1. See Option A++ - Very High Performance mode (CM7_CORE_CLK @ 320 MHz) (For S32K388/S32K389) for details.
2. See Option A+ - Very High Performance mode (CM7_CORE_CLK @ 240 MHz) (For S32K388/S32K389) for details.
3. See Option A - High Performance mode (CM7_CORE_CLK @ 160 MHz) (For S32K388/S32K389 for details.
4. See Option C - Boot Standby mode (CM7_CORE_CLK @ 24 MHz) (For S32K388/S32K389) for details.
5. See Option D - Low-Speed Run mode (CM7_CORE_CLK @ 48 MHz) (For S32K388/S32K389) for details.
6. See Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz) (For S32K388/S32K389) for details.
7. See Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 KHz) (For S32K388/S32K389) for details.
Table 169. Gasket configurations in various clocking modes (for S32K328, S32K338, S32K348, and S32K358)
Gasket configuration
Option 
A+1
Option A2
Option B3
Option C4
Option D5
Option E6
Option 
E27
Option F8
eDMA /STAM (S0, 
S1)
1:1
Bypass
Table continues on the next page...
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1002 / 5251


---
# 페이지 101

Table 169. Gasket configurations in various clocking modes (for S32K328, S32K338, S32K348, and S32K358) 
(continued)
Gasket configuration
Option 
A+1
Option A2
Option B3
Option C4
Option D5
Option E6
Option 
E27
Option F8
HSE_B
1:2
1:1
Bypass
APIS0
1:1
1:1/Bypass
Bypass
AIPS1/2
2:1
2:1
Bypass
QuadSPI
2:1
2:1
Bypass
1:1
PRAM GSKT
1:1
Bypass
Flash Read Path 
pipeline
1:1
Bypass
PRAM/SRAM
WS enabled
WS disabled
BDRAM 64:32
1:1
GMAC
1:1
uSDHC
1:2
1:1
1. See Option A+ - Very High Performance mode (CORE_CLK @ 240 MHz) (For S32K328, S32K338, S32K348, and 
S32K358) for details.
2. See Option A - High Performance mode (CORE_CLK @ 160 MHz) for details.
3. See Option B - Reduced Speed mode (CORE_CLK @ 120 MHz) for details.
4. See Option C - Boot Standby mode (CORE_CLK @ 24 MHz) for details.
5. See Option D - Low-Speed Run mode (CORE_CLK @ 48 MHz) for details.
6. See Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz) for details.
7. See Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 KHz) for details.
8. See Option F - Operation in 1:1 mode with CORE_CLK and AIPS_PLAT_CLK at same speed (For all chips except 
S32K388/S32K389) for details.
Table 170. Gasket configurations in various clocking modes (for S32K344, S32K324, S32K314, S32K342, S32K341, and 
S32K322)
Gasket 
configurations
Option A1
Option B2
Option C3
Option D4
Option E5
Option E26
Option F7
eDMA (S0)
1:1
Bypass
eDMA (S1)
Bypass
HSE_B
1:2
1:1, 1:2
Bypass
AIPS1/AIPS2
2:1
Bypass
QuadSPI
2:1
Bypass
PRAM/SRAM
WS enabled
WS disabled
EMAC 32:64
1:1
BDRAM 64:32
1:1
1. See Option A - High Performance mode (CORE_CLK @ 160 MHz) for details.
2. See Option B - Reduced Speed mode (CORE_CLK @ 120 MHz) for details.
3. See Option C - Boot Standby mode (CORE_CLK @ 24 MHz) for details.
4. See Option D - Low-Speed Run mode (CORE_CLK @ 48 MHz) for details.
5. See Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz) for details.
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1003 / 5251


---
# 페이지 102

6. See Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 KHz) for details.
7. See Option F - Operation in 1:1 mode with CORE_CLK and AIPS_PLAT_CLK at same speed (For all chips except 
S32K388/S32K389) for details.
Table 171. Gasket configurations in various clocking modes (for S32K311 and S32K312)
Gasket configurations
Option B1
Option C2
Option D3
Option E4
Option E25
Option F6
HSE_B
1:1, 1:2
Bypass
AIPS1
2:1
Bypass
PRAM/SRAM
WS disabled
BDRAM 64:32 (TCM 
WS)
1:1
1. See Option B - Reduced Speed mode (CORE_CLK @ 120 MHz) for details.
2. See Option C - Boot Standby mode (CORE_CLK @ 24 MHz) for details.
3. See Option D - Low-Speed Run mode (CORE_CLK @ 48 MHz) for details.
4. See Option E - Low-Speed Run mode (CORE_CLK @ 3 MHz) for details.
5. See Option E2 - Very-Low-Speed Run mode (CORE_CLK @ 750 KHz) for details.
6. See Option F - Operation in 1:1 mode with CORE_CLK and AIPS_PLAT_CLK at same speed (For all chips except 
S32K388/S32K389) for details.
24.7.4 Default clock configuration
At reset recovery, the chip runs on the FIRC_CLK as the default configuration as shown in Option C - Boot Standby mode 
(CORE_CLK @ 24 MHz). Clocking configuration Option_C is the default configuration out of reset with the HSE_B core as the 
boot core. The Cortex-M7_n application core clocks are gated by default. You need to enable the core clocks by the configuring 
the corresponding core clock enable bits shown in Core Clock Gating.
24.7.5 PCFS
The chip supports software-controllable PCFS for MC_CGM MUX_0 (see section "Progressive Clock Frequency Switching 
(PCFS)" in the "Clock Generation Module (MC_CGM)" chapter for details). PCFS increases and decreases the frequency in steps, 
avoiding any overshoots or undershoots. When a functional reset event occurs with PCFS enabled, the PCFS process runs and 
is then followed by the divider configuration updates.
24.7.6 Updating dividers: crossbar halt handshake
The clock divider update process consists of the crossbar halt handshake sequence (see section "Clock dividers update" in the 
"Clock Generation Module (MC_CGM)" chapter for the clock divider update process). A divider update asserts a request to the 
crossbar switch to halt any transaction that is in process. The dividers are updated when the crossbar switch acknowledges the 
request for halt. The halt request disables the crossbar switch gaskets in the following order:
1. Core gaskets (HSE_B gaskets)
2. Crossbar switch (AXBS)
3. Flash AXBS bridge
4. PRAM/SRAM gasket
Dividers are updated after the gaskets acknowledge the halt request.
24.7.7 Changing system clock configurations
Application software sequence for switching clock configurations from FIRC to PLL or PLL to PLL:
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1004 / 5251


---
# 페이지 103

1. Before changing the system clock dividers or before system clock switching, the communication modules working on 
the system clock should be disabled by the application software to avoid any erroneous communication during the 
clock transition.
2. The peripherals working on the system clock should be clock-gated used the MC_ME.PRTNx_COFBy_CLKEN 
configurations. The peripherals working on non-system clocks which are not being switched, can continue to operate.
3. All cores must be clock-gated, except the core being used to control the clock switching.
4. System clock switching can be done by configuration of MC_CGM_MUX_0_CSC[SELCTL].
Application software sequence for switching clock configurations from PLL to FIRC clock switching:
1. Before changing the system clock dividers or before system clock switching, the communication modules working on 
the system clock should be disabled by the application software to avoid any erroneous communication during the clock 
transition.
2. The peripherals working on the system clock should be clock-gated used the MC_ME.PRTNx_COFBy_CLKEN 
configurations. The peripherals working on non-system clocks which are not being switched, can continue to operate.
3. All cores must be clock-gated, except the core being used to control the clock switching.
4. System clock switching can be done by configuration of MC_CGM_MUX_0_CSC[SELCTL].
 
See the Clock divider update section in the MC_CGM chapter, which outlines the procedure for updating 
the dividers.
  NOTE  
 
When enabling PLL, the PMC last mile regulator should be enabled first by configuring PMC_CONFIG[LMEN] 
and PMC_CONFIG[LMBCTLEN] (if using an external BJT). The last mile regulator must be disabled after PLL is 
disabled. See the "Power Management" chapter in this reference manual for details on this module's availability on 
your chip variant.
  NOTE  
24.8 Clock monitoring
The chip contains an independent clock monitoring mechanism which signals malfunctions in the clocking system. This chip 
consists of seven Clock Monitoring Units (CMU_Fx_[0:6]) for monitoring system clock and clocking module outputs. Figure 122 
and Figure 123 show a lower-level view of the clocking monitoring system. Table 172 describes each CMU instance. Each CMU 
instance provides an independent interrupt or reset indication when the clock signal is out of range or lost. The CMU_FM_n 
provides a timeout indication in case there is a loss of metered clock. Your application software must periodically check the 
CMU_FM_1 and CMU_FM_2 status within the chip FTTI (as specified in the Safety Manual).
 
You must disable the CMU corresponding to the system clocks if the application changes the system clock source 
or changes the system clock divider configuration.
You must disable the CMU monitoring a clock source before disabling the clock source, then enable it after enabling 
the clock source.
The CMUs should be turned ON only after device has moved to PLL source (wherein LMR is ON).
  NOTE  
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1005 / 5251


---
# 페이지 104

CMU_FC_0
CMU_FC_4.SR[FHH]
CMU_FC_4.IER[FHHAIE]
CMU_FC_4 destructive reset
CMU_FC_4.GCR[FCE]
CMU_FC_4.SR[FLL]
CMU_FC_4.IER[FLLAIE]
CMU_FC_4
AIPS_PLAT_CLK
FIRC_CLK
monitored-clk
reference-clk
CMU_FC_5.SR[FHH]
CMU_FC_5.IER[FHHAIE]
CMU_FC_5.GCR[FCE]
CMU_FC_5.SR[FLL]
CMU_FC_5.IER[FLLAIE]
CMU_FC_5
CMU_FC_5 destructive reset
HSE_CLK
FIRC_CLK
monitored-clk
reference-clk
CMU_FC_3.SR[FHH]
CMU_FC_3.IER[FHHAIE]
CMU_FC_3.GCR[FCE]
CMU_FC_3.SR[FLL]
CMU_FC_3.IER[FLLAIE]
CMU_FC_3
CMU_FC_3 destructive reset
CORE_CLK
FXOSC_CLK
monitored-clk
reference-clk
CMU_FC_6
CMU_FC_6.GCR[FCE]
CMU_FC_6.SR[FHH]
CMU_FC_6.IER[FHHAIE]
CMU_FC_6 destructive reset
CMU_FC_6.IER[FHHIE]
CMU_FC_6.SR[FLL]
CMU_FC_6.IER[FLLAIE]
CMU_FC_6 interrupt
CMU_FC_6.IER[FLLIE]
CM7_CORE_CLK
FXOSC_CLK
monitored-clk
reference-clk
Sync
FLL
CMU_FC_0.IER[FLLIE]
CMU_FC_0.IER[FLLAIE]
CMU_FC_0.GCR[FCE]
FHH
CMU_FC_0.SR[FLL]
CMU_FC_0.SR[FHH]
CMU_FC_0.IER[FHHIE]
CMU_FC_0.IER[FLLIE]
FLL
FHH
CMU_FC_0.IER[FHHIE]
CMU_FC_0.IER[FHHAIE]
Sync
Interrupt
Mask
CMU_FC_0 
destructive reset
Mask
async FHH event
sync FHH event
async FLL event
sync FLL event
CMU_FC_0 interrupt
FXOSC_CLK
FIRC_CLK
monitored-clk
reference-clk
Figure 122. Frequency checking (FC) instances
CMU_FM_1.IER[FMCIE]
CMU_FM_1.SR[FMC]
CMU_FM_1
FIRC_CLK
FXOSC_CLK
metered-clk
reference-clk
CMU_FM_1
CMU_FM_2.IER[FMCIE]
CMU_FM_2.SR[FMC]
CMU_FM_2
SIRC_CLK
FXOSC_CLK
metered-clk
reference-clk
CMU_FM_2
frequency meter
complete interrupt
frequency meter
complete interrupt
Figure 123. Frequency metering (FM) instances
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1006 / 5251


---
# 페이지 105

Table 172. System clock monitors
CMU
Reference 
clock
Monitored or 
metered clock
Failure 
reaction
Monitoring type description
CMU_FC_0
FIRC_CLK
FXOSC_CLK
Destructive 
reset or 
interrupt
Precision over and under frequency
CMU_FM_1
FXOSC_CLK
FIRC_CLK
Interrupt
Current frequency measurement periodically triggered 
by application software
CMU_FM_2
FXOSC_CLK
SIRC_CLK
Interrupt
Current frequency measurement periodically triggered 
by application software
CMU_FC_3
FXOSC_CLK
CORE_CLK
Destructive 
reset
Precision over and under frequency
CMU_FC_4
FIRC_CLK
AIPS_PLAT_CLK
Destructive 
reset
Precision over and under frequency
CMU_FC_5
FIRC_CLK
HSE_CLK
Destructive 
reset
Precision over and under frequency
CMU_FC_6
FXOSC_CLK
CM7_CORE_CLK
Destructive 
reset or 
interrupt
Precision over and under frequency
 
See the clock system diagrams in the "Clocking Overview" section for details on the monitored clocks availability 
on your chip variant.
  NOTE  
24.9 Glossary
MODULE_CLK
Module operating clock
REG_INTF_CLK Module register interface clock used for register read and write
PCFS
Progressive Clock Frequency Switching (see section "Progressive Clock Frequency Switching (PCFS)" for 
details)
POR
Power On Reset
SBC
System Basis Chip (see NXP SBC portfolio)
FLL
Frequency lower than low frequency reference
FHH
Frequency higher than high frequency reference
FTTI
Fault Tolerance Time Interval
NXP Semiconductors
Clocking
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1007 / 5251


---