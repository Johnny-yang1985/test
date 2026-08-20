# 페이지 27

Chapter 38
Device Configuration Module General-Purpose 
Registers (DCM_GPR)
38.1 DCM controlled features and availability in product family
Based on the chip features described in ‘Feature comparison’ section in ‘Introduction’ chapter, there are some features which 
are present only in specific parts in the S32K3xx product family. The following table summarizes the corresponding DCM register 
fields along with the parts wherein the corresponding register fields are available. In rest of the parts within the product family, the 
corresponding fields are reserved.
Table 232. DCM controlled features and availability in product family
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMROD3[1]
CM7_1_LOCKUP
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMROD3[3]
CM7_RCCU1_ALARM
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K344, S32K342, 
S32K341,
DCMROD3[4]
CM7_RCCU2_ALARM
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K344, S32K342, 
S32K341,
DCMROD3[5]
TCM_GSKT_ALARM
See Register section for details
S32K389, S32K388, S32K344, 
S32K324, S32K314, S32K342, 
S32K341, S32K322, S32K312, 
S32K311
DCMROD3[6]
DMA_SYS_GSKT_ALARM
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMROD3[7]
DMA_PERIPH_GSKT_ALARM
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMROD3[9]
DMA_AXBS_ALARM
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMROD3[10]
SDHC_GSKT_ALARM
uSDHC IASHB Gasket Alarm 
Status. Read this bit to identify 
the reason of fault in case of 
FCCU NCF 1.
S32K358, S32K348, S32K338, 
S32K328
DCMROD3[12]
QSPI_GSKT_ALARM
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
Table continues on the next page...
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1279 / 5251


---
# 페이지 28

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMROD3[14]
AIPS2_GSKT_ALARM
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMROD3[17]
TCM_AXBS_ALARM
See Register section for details
S32K389, S32K388, S32K344, 
S32K324, S32K314, S32K342, 
S32K341, S32K322
DCMROD3[18]
MAC_GSKT_ALARM
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMROD3[19]
PERIPH_AXBS_ALARM
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMROD3[20]
PF3_CODE_ECC_ERR
The errors are reported from 
the FMU and are connected to 
FCCU NCFs. These are also 
connected to ERM. Read this 
bit to identify the reason of fault 
in case of FCCU NCF 3.
S32K388, S32K358, S32K338
DCMROD3[21]
PF3_DATA_ECC_ERR
The errors are reported from 
the FMU and are connected to 
FCCU NCFs. These are also 
connected to ERM. Read this 
bit to identify the reason of fault 
in case of FCCU NCF 3.
S32K388, S32K358, S32K338
DCMROD3[23]
PRAM2_ECC_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMROD3[24]
PRAM1_ECC_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314
DCMROD3[27]
CM7_1_DCDATA_ECC_ERR
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMROD3[29]
CM7_1_DCTAG_ECC_ERR
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMROD3[31]
CM7_1_ICDATA_ECC_ERR
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMROD4[1]
CM7_1_ICTAG_ECC_ERR
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1280 / 5251


---
# 페이지 29

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMROD4[5]
CM7_1_ITCM_ECC_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K342, 
S32K341, S32K322
DCMROD4[6]
CM7_1_DTCM0_ECC_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K342, 
S32K341, S32K322
DCMROD4[7]
CM7_1_DTCM1_ECC_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K342, 
S32K341, S32K322
DCMROD4[10]
PRAM1_FCCU_ALARM
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314
DCMROD4[16]
PF2_CODE_ECC_ERR
The errors are reported from 
the FMU and are connected to 
FCCU NCFs. These are also 
connected to ERM. Read this 
bit to identify the reason of fault 
in case of FCCU NCF 3.
S32K388, S32K338, S32K328, 
S32K324, S32K322
DCMROD4[17]
PF2_DATA_ECC_ERR
The errors are reported from 
the FMU and are connected to 
FCCU NCFs. These are also 
connected to ERM. Read this 
bit to identify the reason of fault 
in case of FCCU NCF 3.
S32K388, S32K338, S32K328, 
S32K324, S32K322
DCMROD4[23]
PRAM2_FCCU_ALARM
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMROD4[28]
SDHC_RDATA_EDC_ERR
Integrity(EDC) error on uSDHC 
read data for safety. Read this 
bit to identify the reason of fault 
in case of FCCU NCF 1.
S32K358, S32K348, S32K338, 
S32K328
DCMROD4[31]
CM7_2_LOCKUP
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMROD5[14]
TCM_RDATA_EDC_ERR
Specifies whether an integrity 
error is reported on the TCM 
read data for safety.
Read this field to identify the 
reason for a fault in case of 
FCCU NCF 1.
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMROD5[15]
MAC_RDATA_EDC_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1281 / 5251


---
# 페이지 30

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMROD5[18]
CM7_1_AHBP_RDATA_EDC_E
RR
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMROD5[19]
CM7_1_AHBM_RDATA_EDC_
ERR
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMROD5[23]
CM7_2_AHBP_RDATA_EDC_E
RR
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMROD5[24]
CM7_2_AHBM_RDATA_EDC_
ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMROD5[25]
CM7_2_DCDATA_ECC_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMROD5[26]
CM7_2_DCTAG_ECC_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMROD5[27]
CM7_2_ICDATA_ECC_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMROD5[28]
CM7_2_ICTAG_ECC_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMROD5[29]
CM7_2_ITCM_ECC_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMROD5[30]
CM7_2_DTCM0_ECC_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMROD5[31]
CM7_2_DTCM1_ECC_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMROD6[3]
QSPI_FLASHA_ECC_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMROD6[26]
AIPS0_GSKT_ALARM
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMROD6[30]
TCM_PRAM_AXBS_ALARM
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMROD7[0]
CM7_0_AHBM_ALARM
See Register section for details
S32K389, S32K388
DCMROD7[1]
CM7_1_AHBM_ALARM
See Register section for details
S32K389, S32K388
DCMROD7[2]
CM7_2_AHBM_ALARM
See Register section for details
S32K389, S32K388
DCMROD7[3]
CM7_0_AHBP_ALARM
See Register section for details
S32K389, S32K388
DCMROD7[4]
CM7_1_AHBP_ALARM
See Register section for details
S32K389, S32K388
DCMROD7[5]
CM7_2_AHBP_ALARM
See Register section for details
S32K389, S32K388
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1282 / 5251


---
# 페이지 31

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMROD7[11]
VDD1P1_GNG2_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMROD7[12]
VDD2P5_GNG2_ERR
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMROD7[28]
CM7_0_AHBS_ALARM
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMROD7[29]
CM7_1_AHBS_ALARM
See Register section for details
S32K389, S32K388, S32K338, 
S32K328
DCMROD7[30]
CM7_2_AHBS_ALARM
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMROD8[0]
PRAM0_GSKT_ALARM
PRAM0 IAHB Gasket monitor 
alarm status. Read this bit to 
identify the reason of fault in 
case of FCCU NCF 1.
S32K358, S32K348, S32K338, 
S32K328
DCMROD8[1]
PRAM1_GSKT_ALARM
PRAM1 IAHB Gasket monitor 
alarm status. Read this bit to 
identify the reason of fault in 
case of FCCU NCF 1.
S32K358, S32K348, S32K338, 
S32K328
DCMROD8[2]
PRAM2_TCM_GSKT_ALARM
PRAM2_TCM IAHB Gasket 
monitor alarm status. Read this 
bit to identify the reason of fault 
in case of FCCU NCF 1.
S32K358, S32K348, S32K338, 
S32K328
DCMROD8[3]
PRAM2_GSKT_ALARM
PRAM2 IAHB Gasket monitor 
alarm status. Read this bit to 
identify the reason of fault in 
case of FCCU NCF 1.
S32K358, S32K348, S32K338, 
S32K328
DCMROD8[4]
CM7_3_LOCKUP
See Register section for details
S32K389, S32K388
DCMROD8[5]
CM7_2_RCCU1_ALARM
See Register section for details
S32K389, S32K388
DCMROD8[6]
CM7_2_RCCU2_ALARM
See Register section for details
S32K389, S32K388
DCMROD8[7]
PERIPH_AXBS_S3_GSKT_AL
ARM
See Register section for details
S32K389, S32K388
DCMROD8[9]
MAC2_GSKT_ALARM
See Register section for details
S32K389, S32K388
DCMROD8[10]
MAC2_RDATA_EDC_ERR
See Register section for details
S32K389, S32K388
DCMROD8[11]
CM7_3_AHBP_RDATA_EDC_E
RR
See Register section for details
S32K389, S32K388
DCMROD8[12]
CM7_3_AHBM_RDATA_EDC_
ERR
See Register section for details
S32K389, S32K388
DCMROD8[13]
HSE_AES_ACCEL_AXBS_ALA
RM
See Register section for details
S32K389, S32K388
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1283 / 5251


---
# 페이지 32

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMROD8[14]
CM7_3_AHBS_ALARM
See Register section for details
S32K389, S32K388
DCMROD8[16]
ACE_RESULT_RDATA_EDC_E
RR
See Register section for details
S32K389, S32K388
DCMROD8[17]
ACE_FEED_RDATA_EDC_ER
R
See Register section for details
S32K389, S32K388
DCMROD8[18]
AES_ACCEL_AXBS_ALARM
See Register section for details
S32K389, S32K388
DCMROD8[19]
AES_ACCEL_GSKT_ALARM
See Register section for details
S32K389, S32K388
DCMROD8[21]
CM7_3_AHBM_ALARM
See Register section for details
S32K389, S32K388
DCMROD8[22]
CM7_3_AHBP_ALARM
See Register section for details
S32K389, S32K388
DCMROD8[23]
CM7_3_DCDATA_ECC_ERR
See Register section for details
S32K389, S32K388
DCMROD8[24]
CM7_3_DCTAG_ECC_ERR
See Register section for details
S32K389, S32K388
DCMROD8[25]
CM7_3_ICDATA_ECC_ERR
See Register section for details
S32K389, S32K388
DCMROD8[26]
CM7_3_ICTAG_ECC_ERR
See Register section for details
S32K389, S32K388
DCMROD8[27]
CM7_3_ITCM_ECC_ERR
See Register section for details
S32K389, S32K388
DCMROD8[28]
CM7_3_DTCM0_ECC_ERR
See Register section for details
S32K389, S32K388
DCMROD8[29]
CM7_3_DTCM1_ECC_ERR
See Register section for details
S32K389, S32K388
DCMROD9[0]
AES_FEED_DMA_TCD_ECC_
ERR
See Register section for details
S32K389, S32K388
DCMROD9[1]
AES_FEED_DMA_TCD_ADDR
_ECC_ERR
See Register section for details
S32K389, S32K388
DCMROD9[2]
AES_RESULT_DMA_TCD_EC
C_ERR
See Register section for details
S32K389, S32K388
DCMROD9[3]
AES_RESULT_DMA_TCD_AD
DR_ECC_ERR
See Register section for details
S32K389, S32K388
DCMROD9[4]
AES_KP_CRC_SAFETY_ERR
See Register section for details
S32K389, S32K388
DCMROD9[5]
AES_FEED_DID_SAFETY_ER
R
See Register section for details
S32K389, S32K388
DCMROD9[6]
AES_RESULT_DID_SAFETY_
ERR
See Register section for details
S32K389, S32K388
DCMROD9[7]
PF1_0_CODE_ECC_ERR
See Register section for details
S32K389
DCMROD9[8]
PF1_0_DATA_ECC_ERR
See Register section for details
S32K389
DCMROD9[9]
PF1_1_CODE_ECC_ERR
See Register section for details
S32K389
DCMROD9[10]
PF1_1_DATA_ECC_ERR
See Register section for details
S32K389
DCMROD9[11]
FLASH1_EDC_ERR
See Register section for details
S32K389
DCMROD9[12]
FLASH1_ADDR_ENC_ERR
See Register section for details
S32K389
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1284 / 5251


---
# 페이지 33

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMROD9[13]
FLASH1_REF_ERR
See Register section for details
S32K389
DCMROD9[14]
FLASH1_RST_ERR
See Register section for details
S32K389
DCMROD9[16]
FLASH1_ECC_ERR
See Register section for details
S32K389
DCMROD9[17]
PRAM3_ECC_ERR
See Register section for details
S32K389
DCMROD9[18]
PRAM3_FCCU_ALARM
See Register section for details
S32K389
DCMROD9[19]
PF0_0_CMP_ALARM
See Register section for details
S32K389
DCMROD9[20]
PF0_1_CMP_ALARM
See Register section for details
S32K389
DCMROD9[21]
PF1_0_CMP_ALARM
See Register section for details
S32K389
DCMROD9[22]
PF1_1_CMP_ALARM
See Register section for details
S32K389
DCMROD9[23]
PF0_0_CHK_CMP_ALARM
See Register section for details
S32K389
DCMROD9[24]
PF0_1_CHK_CMP_ALARM
See Register section for details
S32K389
DCMROD9[25]
PF1_0_CHK_CMP_ALARM
See Register section for details
S32K389
DCMROD9[26]
PF1_1_CHK_CMP_ALARM
See Register section for details
S32K389
DCMROF1[0]
MAC_MDC_CHID_0
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMROF1[1]
MAC_MDC_CHID_1
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMROF1[2]
MAC_MDC_CHID_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMROF1[3]
MAC1_MDC_CHID_0
See Register section for details
S32K389, S32K388, S32K358
DCMROF1[4]
MAC1_MDC_CHID_1
See Register section for details
S32K389, S32K388, S32K358
DCMROF1[5]
MAC1_MDC_CHID_2
See Register section for details
S32K389, S32K388, S32K358
DCMROF1[16]
AES_FEED_DID_ERR_PRIV
See Register section for details
S32K389, S32K388
DCMROF1[17]
AES_FEED_DID_ERR_NS
See Register section for details
S32K389, S32K388
DCMROF1[18]
AES_FEED_DID_ERR_DID
See Register section for details
S32K389, S32K388
DCMROF1[19]
DCMROF1[20]
DCMROF1[21]
DCMROF1[24]
AES_RESULT_DID_ERR_PRIV See Register section for details
S32K389, S32K388
DCMROF1[25]
AES_RESULT_DID_ERR_NS
See Register section for details
S32K389, S32K388
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1285 / 5251


---
# 페이지 34

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMROF1[26]
AES_RESULT_DID_ERR_DID
See Register section for details
S32K389, S32K388
DCMROF1[27]
DCMROF1[28]
DCMROF1[29]
DCMROF19[29]
LOCKSTEP_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K344, S32K342, 
S32K341,
DCMROF20[1]
LMAUTO_DIS
Specifies whether the PMC 
last-mile automatic crossover 
from the boot regulation feature 
is supported for the chip.
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMROF20[3]
DMA_AXBS_IAHB_BYP
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMROF20[5]
QSPI_IAHB_BYP
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWD3[1]
CM7_1_LOCKUP_EN
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD3[3]
CM7_RCCU1_ALARM_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K344, S32K342, 
S32K341,
DCMRWD3[4]
CM7_RCCU2_ALARM_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K344, S32K342, 
S32K341,
DCMRWD3[5]
TCM_GSKT_ALARM_EN
See Register section for details
S32K389, S32K388, S32K344, 
S32K324, S32K314, S32K342, 
S32K341, S32K322, S32K312, 
S32K311
DCMRWD3[6]
DMA_SYS_GSKT_ALARM_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWD3[7]
DMA_PERIPH_GSKT_ALARM_
EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWD3[9]
DMA_AXBS_ALARM_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1286 / 5251


---
# 페이지 35

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWD3[10]
SDHC_GSKT_ALARM_EN
Enable bit for enabling the fault 
monitoring at FCCU NCF 1 for 
the fault: uSDHC IAHB gasket 
alarm.
S32K358, S32K348, S32K338, 
S32K328
DCMRWD3[12]
QSPI_GSKT_ALARM_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWD3[14]
AIPS2_GSKT_ALARM_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWD3[17]
TCM_AXBS_ALARM_EN
See Register section for details
S32K389, S32K388, S32K344, 
S32K324, S32K314, S32K342, 
S32K341, S32K322
DCMRWD3[18]
MAC_GSKT_ALARM_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWD3[19]
PERIPH_AXBS_ALARM_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWD3[20]
PF3_CODE_ECC_ERR_EN
Enable bit for enabling the fault 
monitoring at FCCU NCF 3 
for the fault: Flash3 code ECC 
uncorrectable error.
S32K388, S32K358, S32K338
DCMRWD3[21]
PF3_DATA_ECC_ERR_EN
Enable bit for enabling the fault 
monitoring at FCCU NCF 3 
for the fault: Flash3 data ECC 
uncorrectable error.
S32K388, S32K358, S32K338
DCMRWD3[23]
PRAM2_ECC_ERR_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWD3[24]
PRAM1_ECC_ERR_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314
DCMRWD3[27]
CM7_1_DCDATA_ECC_ERR_E
N
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD3[29]
CM7_1_DCTAG_ECC_ERR_E
N
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1287 / 5251


---
# 페이지 36

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMRWD3[31]
CM7_1_ICDATA_ECC_ERR_E
N
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD4[1]
CM7_1_ICTAG_ECC_ERR_EN
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD4[5]
CM7_1_ITCM_ECC_ERR_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K342, 
S32K341, S32K322
DCMRWD4[6]
CM7_1_DTCM0_ECC_ERR_E
N
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K342, 
S32K341, S32K322
DCMRWD4[7]
CM7_1_DTCM1_ECC_ERR_E
N
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K342, 
S32K341, S32K322
DCMRWD4[10]
PRAM1_FCCU_ALARM_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314
DCMRWD4[16]
PF2_CODE_ECC_ERR_EN
Enable bit for enabling the fault 
monitoring at FCCU NCF 3 
for the fault: Flash2 code ECC 
uncorrectable error.
S32K388, S32K338, S32K328, 
S32K324, S32K322
DCMRWD4[17]
PF2_DATA_ECC_ERR_EN
Enable bit for enabling the fault 
monitoring at FCCU NCF 3 
for the fault: Flash2 data ECC 
uncorrectable error.
S32K388, S32K338, S32K328, 
S32K324, S32K322
DCMRWD4[23]
PRAM2_FCCU_ALARM_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWD4[28]
SDHC_RDATA_EDC_ERR_EN
Enable bit for enabling the fault 
monitoring at FCCU NCF 1 for 
the fault: Integrity (EDC) error 
on uSDHC read data for safety.
S32K358, S32K348, S32K338, 
S32K328
DCMRWD4[31]
CM7_2_LOCKUP_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD5[14]
TCM_RDATA_EDC_ERR_EN
Specifies whether an integrity 
error is reported on the TCM 
read data.
The field enables fault 
monitoring at FCCU NCF 1, if 
there is an integrity error on the 
TCM read data, for safety.
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1288 / 5251


---
# 페이지 37

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMRWD5[15]
MAC_RDATA_EDC_ERR_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWD5[18]
CM7_1_AHBP_RDATA_EDC_E
RR_EN
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD5[19]
CM7_1_AHBM_RDATA_EDC_
ERR_EN
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD5[23]
CM7_2_AHBP_RDATA_EDC_E
RR_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD5[24]
CM7_2_AHBM_RDATA_EDC_
ERR_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD5[25]
CM7_2_DCDATA_ECC_ERR_E
N
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD5[26]
CM7_2_DCTAG_ECC_ERR_E
N
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD5[27]
CM7_2_ICDATA_ECC_ERR_E
N
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD5[28]
CM7_2_ICTAG_ECC_ERR_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD5[29]
CM7_2_ITCM_ECC_ERR_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD5[30]
CM7_2_DTCM0_ECC_ERR_E
N
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD5[31]
CM7_2_DTCM1_ECC_ERR_E
N
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD6[6]
eMIOS2_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314
DCMRWD6[9]
SWT1_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD6[11]
STM1_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWD6[14]
PIT2_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1289 / 5251


---
# 페이지 38

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMRWD6[19]
LPSPI4_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314
DCMRWD6[20]
LPSPI5_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314
DCMRWD6[27]
FLEXCAN3_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322, 
S32K312
DCMRWD6[28]
FLEXCAN4_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K312
DCMRWD6[29]
FLEXCAN5_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K312
DCMRWD6[30]
SAI0_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWD6[31]
SAI1_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWD7[1]
FLEXCAN6_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWD7[2]
FLEXCAN7_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWD7[3]
STM2_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWD7[4]
SWT2_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD7[21]
SWT3_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388
DCMRWD7[22]
STM3_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388
DCMRWD7[23]
PIT3_DBG_DIS_CM7_0
See Register section for details
S32K389, S32K388
DCMRWD7[24]
FLEXCAN8_DBG_DIS_CM7_0
See Register section for details
S32K389
DCMRWD7[25]
FLEXCAN9_DBG_DIS_CM7_0
See Register section for details
S32K389
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1290 / 5251


---
# 페이지 39

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMRWD7[26]
FLEXCAN10_DBG_DIS_CM7_
0
See Register section for details
S32K389
DCMRWD7[27]
FLEXCAN11_DBG_DIS_CM7_
0
See Register section for details
S32K389
DCMRWD8[0]
EDMA_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[1]
FCCU_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[2]
LCU0_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[3]
LCU1_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[4]
eMIOS0_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[5]
eMIOS1_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[6]
eMIOS2_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324
DCMRWD8[7]
RTC_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[8]
SWT0_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[9]
SWT1_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[10]
STM0_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[11]
STM1_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[12]
PIT0_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[13]
PIT1_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[14]
PIT2_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[15]
LPSPI0_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[16]
LPSPI1_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1291 / 5251


---
# 페이지 40

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMRWD8[17]
LPSPI2_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[18]
LPSPI3_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[19]
LPSPI4_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324
DCMRWD8[20]
LPSPI5_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324
DCMRWD8[21]
LPI2C0_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[22]
LPI2C1_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[23]
FLEXIO_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[24]
FLEXCAN0_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[25]
FLEXCAN1_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[26]
FLEXCAN2_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[27]
FLEXCAN3_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[28]
FLEXCAN4_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324
DCMRWD8[29]
FLEXCAN5_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324
DCMRWD8[30]
SAI0_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD8[31]
SAI1_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWD9[1]
FLEXCAN6_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328
DCMRWD9[2]
FLEXCAN7_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328
DCMRWD9[3]
STM2_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338, 
S32K328
DCMRWD9[4]
SWT2_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388, S32K338
DCMRWD9[21]
SWT3_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1292 / 5251


---
# 페이지 41

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMRWD9[22]
STM3_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388
DCMRWD9[23]
PIT3_DBG_DIS_CM7_1
See Register section for details
S32K389, S32K388
DCMRWD9[24]
FLEXCAN8_DBG_DIS_CM7_1
See Register section for details
S32K389
DCMRWD9[25]
FLEXCAN9_DBG_DIS_CM7_1
See Register section for details
S32K389
DCMRWD9[26]
FLEXCAN10_DBG_DIS_CM7_
1
See Register section for details
S32K389
DCMRWD9[27]
FLEXCAN11_DBG_DIS_CM7_
1
See Register section for details
S32K389
DCMRWD12[0]
EDMA_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[1]
FCCU_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[2]
LCU0_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[3]
LCU1_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[4]
eMIOS0_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[5]
eMIOS1_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[6]
eMIOS2_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[7]
RTC_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[8]
SWT0_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[9]
SWT1_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K338
DCMRWD12[10]
STM0_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[11]
STM1_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[12]
PIT0_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[13]
PIT1_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[14]
PIT2_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1293 / 5251


---
# 페이지 42

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMRWD12[15]
LPSPI0_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[16]
LPSPI1_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[17]
LPSPI2_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[18]
LPSPI3_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[19]
LPSPI4_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[20]
LPSPI5_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[21]
LPI2C0_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[22]
LPI2C1_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[23]
FLEXIO_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[24]
FLEXCAN0_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[25]
FLEXCAN1_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[26]
FLEXCAN2_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[27]
FLEXCAN3_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[28]
FLEXCAN4_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[29]
FLEXCAN5_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[30]
SAI0_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD12[31]
SAI1_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD13[1]
FLEXCAN6_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD13[2]
FLEXCAN7_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1294 / 5251


---
# 페이지 43

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMRWD13[3]
STM2_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD13[4]
SWT2_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWD13[21]
SWT3_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388
DCMRWD13[22]
STM3_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388
DCMRWD13[23]
PIT3_DBG_DIS_CM7_2
See Register section for details
S32K389, S32K388
DCMRWD13[24]
FLEXCAN8_DBG_DIS_CM7_2
See Register section for details
S32K389
DCMRWD13[25]
FLEXCAN9_DBG_DIS_CM7_2
See Register section for details
S32K389
DCMRWD13[26]
FLEXCAN10_DBG_DIS_CM7_
2
See Register section for details
S32K389
DCMRWD13[27]
FLEXCAN11_DBG_DIS_CM7_
2
See Register section for details
S32K389
DCMRWD14[3]
QSPI_FLASHA_ECC_ERR_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWD14[26]
AIPS0_GSKT_ALARM_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWD14[30]
TCM_PRAM_AXBS_ALARM_E
N
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWD15[0]
CM7_0_AHBM_ALARM_EN
See Register section for details
S32K389, S32K388
DCMRWD15[1]
CM7_1_AHBM_ALARM_EN
See Register section for details
S32K389, S32K388
DCMRWD15[2]
CM7_2_AHBM_ALARM_EN
See Register section for details
S32K389, S32K388
DCMRWD15[3]
CM7_0_AHBP_ALARM_EN
See Register section for details
S32K389, S32K388
DCMRWD15[4]
CM7_1_AHBP_ALARM_EN
See Register section for details
S32K389, S32K388
DCMRWD15[5]
CM7_2_AHBP_ALARM_EN
See Register section for details
S32K389, S32K388
DCMRWD15[11]
VDD1P1_GNG2_ERR_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWD15[12]
VDD2P5_GNG2_ERR_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWD15[28]
CM7_0_AHBS_ALARM_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWD15[29]
CM7_1_AHBS_ALARM_EN
See Register section for details
S32K389, S32K388, S32K338, 
S32K328
DCMRWD15[30]
CM7_2_AHBS_ALARM_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1295 / 5251


---
# 페이지 44

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMRWD16[0]
PRAM0_GSKT_ALARM_EN
Enables bit for enabling the 
fault monitoring at FCCU NCF 
1 for the fault: PRAM0 IAHB 
Gasket monitor alarm.
S32K358, S32K348, S32K338, 
S32K328
DCMRWD16[1]
PRAM1_GSKT_ALARM_EN
Enables bit for enabling the 
fault monitoring at FCCU NCF 
1 for the fault: PRAM1 IAHB 
Gasket monitor alarm.
S32K358, S32K348, S32K338, 
S32K328
DCMRWD16[2]
PRAM2_TCM_GSKT_ALARM_
EN
Enables bit for enabling the 
fault monitoring at FCCU NCF 
1 for the fault: PRAM2_TCM 
IAHB Gasket monitor alarm.
S32K358, S32K348, S32K338, 
S32K328
DCMRWD16[3]
PRAM2_GSKT_ALARM_EN
Enables bit for enabling the 
fault monitoring at FCCU NCF 
1 for the fault: PRAM2 IAHB 
Gasket monitor alarm.
S32K358, S32K348, S32K338, 
S32K328
DCMRWD16[4]
CM7_3_LOCKUP_EN
See Register section for details
S32K389, S32K388
DCMRWD16[5]
CM7_2_RCCU1_ALARM_EN
See Register section for details
S32K389, S32K388
DCMRWD16[6]
CM7_2_RCCU2_ALARM_EN
See Register section for details
S32K389, S32K388
DCMRWD16[7]
PERIPH_AXBS_S3_GSKT_AL
ARM_EN
See Register section for details
S32K389, S32K388
DCMRWD16[9]
MAC2_GSKT_ALARM_EN
See Register section for details
S32K389, S32K388
DCMRWD16[10]
MAC2_RDATA_EDC_ERR_EN
See Register section for details
S32K389, S32K388
DCMRWD16[11]
CM7_3_AHBP_RDATA_EDC_E
RR_EN
See Register section for details
S32K389, S32K388
DCMRWD16[12]
CM7_3_AHBM_RDATA_EDC_
ERR_EN
See Register section for details
S32K389, S32K388
DCMRWD16[13]
HSE_AES_ACCEL_AXBS_ALA
RM_EN
See Register section for details
S32K389, S32K388
DCMRWD16[14]
CM7_3_AHBS_ALARM_EN
See Register section for details
S32K389, S32K388
DCMRWD16[16]
ACE_RESULT_RDATA_EDC_E
RR_EN
See Register section for details
S32K389, S32K388
DCMRWD16[17]
ACE_FEED_RDATA_EDC_ER
R_EN
See Register section for details
S32K389, S32K388
DCMRWD16[18]
AES_ACCEL_AXBS_ALARM_E
N
See Register section for details
S32K389, S32K388
DCMRWD16[19]
AES_ACCEL_GSKT_ALARM_E
N
See Register section for details
S32K389, S32K388
DCMRWD16[21]
CM7_3_AHBM_ALARM_EN
See Register section for details
S32K389, S32K388
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1296 / 5251


---
# 페이지 45

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMRWD16[22]
CM7_3_AHBP_ALARM_EN
See Register section for details
S32K389, S32K388
DCMRWD16[23]
CM7_3_DCDATA_ECC_ERR_E
N
See Register section for details
S32K389, S32K388
DCMRWD16[24]
CM7_3_DCTAG_ECC_ERR_E
N
See Register section for details
S32K389, S32K388
DCMRWD16[25]
CM7_3_ICDATA_ECC_ERR_E
N
See Register section for details
S32K389, S32K388
DCMRWD16[26]
CM7_3_ICTAG_ECC_ERR_EN
See Register section for details
S32K389, S32K388
DCMRWD16[27]
CM7_3_ITCM_ECC_ERR_EN
See Register section for details
S32K389, S32K388
DCMRWD16[28]
CM7_3_DTCM0_ECC_ERR_E
N
See Register section for details
S32K389, S32K388
DCMRWD16[29]
CM7_3_DTCM1_ECC_ERR_E
N
See Register section for details
S32K389, S32K388
DCMRWD17[0]
AES_FEED_DMA_TCD_ECC_
ERR_EN
See Register section for details
S32K389, S32K388
DCMRWD17[1]
AES_FEED_DMA_TCD_ADDR
_ECC_ERR_EN
See Register section for details
S32K389, S32K388
DCMRWD17[2]
AES_RESULT_DMA_TCD_EC
C_ERR_EN
See Register section for details
S32K389, S32K388
DCMRWD17[3]
AES_RESULT_DMA_TCD_AD
DR_ECC_ERR_EN
See Register section for details
S32K389, S32K388
DCMRWD17[4]
AES_KP_CRC_SAFETY_ERR_
EN
See Register section for details
S32K389, S32K388
DCMRWD17[5]
AES_FEED_DID_SAFETY_ER
R_EN
See Register section for details
S32K389, S32K388
DCMRWD17[6]
AES_RESULT_DID_SAFETY_
ERR_EN
See Register section for details
S32K389, S32K388
DCMRWD17[7]
PF1_0_CODE_ECC_ERR_EN
See Register section for details
S32K389
DCMRWD17[8]
PF1_0_DATA_ECC_ERR_EN
See Register section for details
S32K389
DCMRWD17[9]
PF1_1_CODE_ECC_ERR_EN
See Register section for details
S32K389
DCMRWD17[10]
PF1_1_DATA_ECC_ERR_EN
See Register section for details
S32K389
DCMRWD17[11]
FLASH1_EDC_ERR_EN
See Register section for details
S32K389
DCMRWD17[12]
FLASH1_ADDR_ENC_ERR_E
N
See Register section for details
S32K389
DCMRWD17[13]
FLASH1_REF_ERR_EN
See Register section for details
S32K389
DCMRWD17[14]
FLASH1_RST_ERR_EN
See Register section for details
S32K389
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1297 / 5251


---
# 페이지 46

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMRWD17[16]
FLASH1_ECC_ERR_EN
See Register section for details
S32K389
DCMRWD17[17]
PRAM3_ECC_ERR_EN
See Register section for details
S32K389
DCMRWD17[18]
PRAM3_FCCU_ALARM_EN
See Register section for details
S32K389
DCMRWD17[19]
PF0_0_CMP_EN
See Register section for details
S32K389
DCMRWD17[20]
PF0_1_CMP_EN
See Register section for details
S32K389
DCMRWD17[21]
PF1_0_CMP_EN
See Register section for details
S32K389
DCMRWD17[22]
PF1_1_CMP_EN
See Register section for details
S32K389
DCMRWD17[23]
PF0_0_CHK_CMP_EN
See Register section for details
S32K389
DCMRWD17[24]
PF0_1_CHK_CMP_EN
See Register section for details
S32K389
DCMRWD17[25]
PF1_0_CHK_CMP_EN
See Register section for details
S32K389
DCMRWD17[26]
PF1_1_CHK_CMP_EN
See Register section for details
S32K389
DCMRWD19[0]
EDMA_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[1]
FCCU_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[2]
LCU0_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[3]
LCU1_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[4]
eMIOS0_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[5]
eMIOS1_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[6]
eMIOS2_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[7]
RTC_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[8]
SWT0_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[9]
SWT1_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[10]
STM0_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[11]
STM1_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[12]
PIT0_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[13]
PIT1_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[14]
PIT2_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[15]
LPSPI0_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[16]
LPSPI1_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[17]
LPSPI2_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[18]
LPSPI3_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[19]
LPSPI4_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[20]
LPSPI5_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1298 / 5251


---
# 페이지 47

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMRWD19[21]
LPI2C0_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[22]
LPI2C1_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[23]
FLEXIO_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[24]
FLEXCAN0_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[25]
FLEXCAN1_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[26]
FLEXCAN2_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[27]
FLEXCAN3_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[28]
FLEXCAN4_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[29]
FLEXCAN5_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[30]
SAI0_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD19[31]
SAI1_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD20[1]
FLEXCAN6_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD20[2]
FLEXCAN7_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD20[3]
STM2_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD20[4]
SWT2_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD20[21]
SWT3_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD20[22]
STM3_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD20[23]
PIT3_DBG_DIS_CM7_3
See Register section for details
S32K389, S32K388
DCMRWD20[24]
FLEXCAN8_DBG_DIS_CM7_3
See Register section for details
S32K389
DCMRWD20[25]
FLEXCAN9_DBG_DIS_CM7_3
See Register section for details
S32K389
DCMRWD20[26]
FLEXCAN10_DBG_DIS_CM7_
3
See Register section for details
S32K389
DCMRWD20[27]
FLEXCAN11_DBG_DIS_CM7_
3
See Register section for details
S32K389
DCMRWF1[0]
CAN_TIMESTAMP_SEL
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWF1[1]
CAN_TIMESTAMP_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWF1[6]
MAC_CONF_SEL
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1299 / 5251


---
# 페이지 48

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMRWF1[7]
MAC_CONF_SEL
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWF1[15]
VDD_HV_B_IO_CTRL_LATCH
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWF1[19]
MAC_SB_END_CTRL
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWF1[26]
VDD_HV_B_VLT_DVDR_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWF1[27]
VDD_1_5_VLT_DVDR_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322
DCMRWF2[8]
PMOS_CTRL_GPIO_DATA
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWF2[11]
SAI_MCLK2_SEL
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWF2[12]
SUPPLY2_MON_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWF2[13]
SUPPLY2_MON_SEL
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWF2[14]
DCMRWF2[15]
DCMRWF2[17]
VIRT_WRAP_IPSYNC_BYPAS
S
See Register section for details
S32K389, S32K388
DCMRWF2[21]
PGOOD_POLARITY
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWF2[24]
PLL1_LOL_RST_EN
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWF2[25]
WKPU0_SRC_SELECT
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWF2[26]
WKPU14_SRC_SELECT
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWF2[27]
WKPU15_SRC_SELECT
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1300 / 5251


---
# 페이지 49

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMRWF2[28]
WKPU18_SRC_SELECT
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWF2[29]
WKPU27_SRC_SELECT
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWF2[30]
WKPU45_SRC_SELECT
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWF2[31]
WKPU8_SRC_SELECT
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWF3[13]
MAC_RX_CLK_MUX_BYPASS
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWF3[14]
MAC_RX_CLK_MUX_BYPASS
See Register section for details
S32K358, S32K348, S32K338, 
S32K328
DCMRWF3[15]
MAC_TX_CLK_MUX_BYPASS
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328
DCMRWF4[0]
MUX_MODE_EN_ADC1_S18
Controls the selection of GPIOs 
to drive ADC1 standard channel 
18th.
S32K311
DCMRWF4[5]
MUX_MODE_EN_ADC1_S22
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322, 
S32K312
DCMRWF4[6]
MUX_MODE_EN_ADC1_S23
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314, 
S32K342, S32K341, S32K322, 
S32K312
DCMRWF4[7]
MUX_MODE_EN_ADC0_S12
Controls the selection of GPIOs 
to drive ADC_0 standard 
channel 12.
S32K311
DCMRWF4[8]
MUX_MODE_EN_ADC0_S13
Controls the selection of GPIOs 
to drive ADC_0 standard 
channel 13.
S32K311
DCMRWF4[9]
MUX_MODE_EN_ADC2_S8
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314
DCMRWF4[10]
MUX_MODE_EN_ADC2_S9
See Register section for details
S32K389, S32K388, S32K358, 
S32K348, S32K338, S32K328, 
S32K344, S32K324, S32K314
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1301 / 5251


---
# 페이지 50

Table 232. DCM controlled features and availability in product family (continued)
Register field
Register field abbreviation
Register field description
Parts wherein this field is 
available
DCMRWF4[11]
MUX_MODE_EN_ADC0_S14
Controls the selection of GPIOs 
to drive ADC_0 standard 
channel 14.
S32K311
DCMRWF4[12]
MUX_MODE_EN_ADC0_S17
Controls the selection of GPIOs 
to drive ADC_0 standard 
channel 17.
S32K311
DCMRWF4[18]
CM7_1_CPUWAIT
See Register section for details
S32K389, S32K388, S32K338, 
S32K328, S32K324, S32K322
DCMRWF4[19]
CM7_2_CPUWAIT
See Register section for details
S32K389, S32K388, S32K358, 
S32K338
DCMRWF4[20]
CM7_3_CPUWAIT
See Register section for details
S32K389, S32K388
DCMRWF4[23]
MAC_SB_END_CTRL
See Register section for details
S32K389, S32K388
DCMRWF4[24]
MAC2_CONF_SEL
See Register section for details
S32K389, S32K388
DCMRWF4[25]
DCMRWF4[26]
MAC_RMII_CLK_MUX_BYPAS
S
See Register section for details
S32K389, S32K388
DCMRWF4[27]
MAC2_RMII_CLK_MUX_BYPA
SS
See Register section for details
S32K389, S32K388
DCMRWF4[28]
MUX_MODE_EN_ADC0_P2
Controls the selection of 
GPIOs to drive ADC0 precision 
channel 2nd.
S32K311
DCMRWF4[29]
MAC2_RX_CLK_MUX_BYPAS
S
See Register section for details
S32K389, S32K388
DCMRWF4[30]
DCMRWF4[31]
MAC2_TX_CLK_MUX_BYPAS
S
See Register section for details
S32K389, S32K388
38.2 DCM_GPR register descriptions
Before you start to work with the GPR register take care about the following:
• Do not modify the reserved locations, registers, or reserved bits with respect to their default configurations. Chip behavior is 
not guaranteed in case of such writes.
• The writes to the DCM Read Write registers (DCMRWPx, DCMRWDx, and DCMRWFx) are synchronized and take up to 4 
cycles of CORE_CLK, which means that the register configuration is effective at least 4 CORE_CLK after its write.
• The DCMROXn registers are sticky in nature. These registers latch the previous state and retain values across standby mode. 
Therefore, reading these registers might indicate a previously latched value. To read these sticky status registers after a reset 
event, a standby mode exit or any update in the signals which they latch, it is recommended to first clear the corresponding 
fields by writing 1 to the fields. This operation clears the previously latched status, and the fields get updated with the new 
status correctly.
• You must access DCM after at least 9 AIPS_SLOW_CLK cycles of writing to MC_RGM.ERCTRL because the configuration 
of MC_RGM.ERCTRL takes several cycles to be effective.
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1302 / 5251


---
# 페이지 51

 
The register section is based on the configuration of S32K389. For other chips, see Table 232 for more details.
  NOTE  
38.2.1 DCM_GPR memory map
DCM_GPR base address: 402A_C000h
Offset
Register
Width
(In bits)
Access
Reset value
200h
Read-Only GPR On Destructive Reset 1 (DCMROD1)
32
RW
0000_0000h
208h
Read-Only GPR On Destructive Reset 3 (DCMROD3)
32
RW
0000_0000h
20Ch
Read-Only GPR On Destructive Reset 4 (DCMROD4)
32
RW
0000_0000h
210h
Read-Only GPR On Destructive Reset 5 (DCMROD5)
32
RW
0000_0000h
214h
Read-Only GPR On Destructive Reset 6 (DCMROD6)
32
RW
0000_0000h
218h
Read-Only GPR On Destructive Reset 7 (DCMROD7)
32
RW
0000_0000h
21Ch
Read-Only GPR On Destructive Reset Register (DCMROD8)
32
RW
0000_0000h
220h
Read-Only GPR On Destructive Reset 9 (DCMROD9)
32
RW
0000_0000h
300h
Read-Only GPR On Functional Reset 1 (DCMROF1)
32
RW
0000_0000h
304h
Read-Only GPR On Functional Reset 2 (DCMROF2)
32
RW
0000_0000h
308h
Read-Only GPR On Functional Reset 3 (DCMROF3)
32
RW
0000_0000h
30Ch
Read-Only GPR On Functional Reset 4 (DCMROF4)
32
RW
0000_0000h
310h
Read-Only GPR On Functional Reset 5 (DCMROF5)
32
RW
0000_0000h
314h
Read-Only GPR On Functional Reset 6 (DCMROF6)
32
RW
0000_0000h
318h
Read-Only GPR On Functional Reset 7 (DCMROF7)
32
RW
0000_0000h
31Ch
Read-Only GPR On Functional Reset 8 (DCMROF8)
32
RW
0000_0000h
320h
Read-Only GPR On Functional Reset 9 (DCMROF9)
32
RW
0000_0000h
324h
Read-Only GPR On Functional Reset 10 (DCMROF10)
32
RW
0000_0000h
328h
Read-Only GPR On Functional Reset 11 (DCMROF11)
32
RW
0000_0000h
32Ch
Read-Only GPR On Functional Reset 12 (DCMROF12)
32
RW
0000_0000h
330h
Read-Only GPR On Functional Reset 13 (DCMROF13)
32
RW
0000_0000h
334h
Read-Only GPR On Functional Reset 14 (DCMROF14)
32
RW
0000_0000h
338h
Read-Only GPR On Functional Reset 15 (DCMROF15)
32
RW
0000_0000h
33Ch
Read-Only GPR On Functional Reset 16 (DCMROF16)
32
RW
0000_0000h
340h
Read-Only GPR On Functional Reset 17 (DCMROF17)
32
RW
0000_0000h
348h
Read-Only GPR On Functional Reset 19 (DCMROF19)
32
R
4000_0000h
34Ch
Read-Only GPR On Functional Reset 20 (DCMROF20)
32
R
See section
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1303 / 5251


---
# 페이지 52

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
350h
Read-Only GPR On Functional Reset 21 (DCMROF21)
32
R
0000_0000h
400h
Read Write GPR On POR 1 (DCMRWP1)
32
RW
0000_0400h
408h
Read Write GPR On POR 3 (DCMRWP3)
32
RW
0000_0000h
504h
Read Write GPR On Destructive Reset 2 (DCMRWD2)
32
RW
0000_0000h
508h
Read Write GPR On Destructive Reset 3 (DCMRWD3)
32
RW
FFFF_FBFFh
50Ch
Read Write GPR On Destructive Reset 4 (DCMRWD4)
32
RW
EFFF_FFFFh
510h
Read Write GPR On Destructive Reset 5 (DCMRWD5)
32
RW
FFFF_BFFFh
514h
Read Write GPR On Destructive Reset 6 (DCMRWD6)
32
RW
0000_0000h
518h
Read Write GPR On Destructive Reset 7 (DCMRWD7)
32
RW
0000_0000h
51Ch
Read Write GPR On Destructive Reset 8 (DCMRWD8)
32
RW
0000_0000h
520h
Read Write GPR On Destructive Reset 9 (DCMRWD9)
32
RW
0000_0000h
52Ch
Read Write GPR On Destructive Reset 12 (DCMRWD12)
32
RW
0000_0000h
530h
Read Write GPR On Destructive Reset 13 (DCMRWD13)
32
RW
0000_0000h
534h
Read Write GPR On Destructive Reset 14 (DCMRWD14)
32
RW
4400_0008h
538h
Read Write GPR On Destructive Reset 15 (DCMRWD15)
32
RW
7000_183Fh
53Ch
Read Write GPR On Destructive Reset 16 (DCMRWD16)
32
RW
3FEF_7EF0h
540h
Read Write GPR On Destructive Reset 17 (DCMRWD17)
32
RW
0000_007Fh
548h
Read Write GPR On Destructive Reset 19 (DCMRWD19)
32
RW
0000_0000h
54Ch
Read Write GPR On Destructive Reset 20 (DCMRWD20)
32
RW
0000_0000h
600h
Read Write GPR On Functional Reset 1 (DCMRWF1)
32
RW
0000_0000h
604h
Read Write GPR On Functional Reset 2 (DCMRWF2)
32
RW
0000_0000h
608h
Read Write GPR On Functional Reset 3 (DCMRWF3)
32
RW
0000_0000h
60Ch
Read Write GPR On Functional Reset 4 (DCMRWF4)
32
RW
0000_0000h
610h
Read Write GPR On Functional Reset 5 (DCMRWF5)
32
RW
See section
700h
Read-Only GPR On PMCPOR Reset 1 (DCMROPP1)
32
RW
0000_0000h
704h
Read-Only GPR On PMCPOR Reset 2 (DCMROPP2)
32
RW
0000_0000h
708h
Read-Only GPR On PMCPOR Reset 3 (DCMROPP3)
32
RW
0000_0000h
70Ch
Read-Only GPR On PMCPOR Reset 4 (DCMROPP4)
32
RW
0000_0000h
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1304 / 5251


---
# 페이지 53

38.2.2 Read-Only GPR On Destructive Reset 1 (DCMROD1)
Offset
Register
Offset
DCMROD1
200h
Function
Contains information related to:
• Key response ready status.
• DCF violation from HSE_B.
• PCU input isolation status.
This register resets after destructive reset 1.
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
Reserved 
Reserv
ed 
Reserv
ed 
PCU_I
SO...
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
31-3
—
Reserved
2
—
Reserved
1
—
Reserved
0
PCU_ISO_STA
TUS
PCU Input Isolation Status On Previous Standby Entry
Specifies whether input isolation was enabled in the previous standby entry.
0b - No
1b - Yes
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1305 / 5251


---
# 페이지 54

38.2.3 Read-Only GPR On Destructive Reset 3 (DCMROD3)
Offset
Register
Offset
DCMROD3
208h
Function
Contains information related to:
• ECC and life cycle errors.
• AXBS, RCCU, and gasket alarms.
This register resets after destructive reset 3.
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
CM7_1
_I...
CM7_0
_I...
CM7_1
_D...
CM7_0
_D...
CM7_1
_D...
CM7_0
_D...
PRAM
0_E...
PRAM
1_E...
PRAM
2_E...
LC_
ERR 
Reserved 
PERIP
H_...
MAC_
GSK...
TCM_
AXB...
DATA_
ED...
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
Reset
0
0
0
0
0
0
0
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
ADDR
_ED...
AIPS2
_G...
AIPS1
_G...
QSPI_
GS...
HSE_
GSK...
Reserv
ed 
DMA_
AXB...
SYS_A
XB...
DMA_
PER...
DMA_
SYS...
TCM_
GSK...
CM7_
RCC...
CM7_
RCC...
HSE_L
OC...
CM7_1
_L...
CM7_0
_L...
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
CM7_1_ICDAT
A_ECC_ERR
Cortex-M7_1 I-cache Multi-Bit ECC Error
Specifies whether the Cortex-M7_1 core's I-cache data memory detected a multi-bit ECC error.
Read this field to identify the reason for a fault in case of FCCU noncritical fault (NCF) 2.
0b - No
1b - Yes
30
CM7_0_ICDAT
A_ECC_ERR
Cortex-M7_0 I-cache Data ECC Error
Specifies whether the Cortex-M7_0 core's I-cache data memory detected a multi-bit ECC error.
Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1306 / 5251


---
# 페이지 55

Table continued from the previous page...
Field
Function
29
CM7_1_DCTAG
_ECC_ERR
Cortex-M7_1 D-cache Tag ECC Error
Specifies whether the Cortex-M7_1 core's D-cache tag memory detected a multi-bit ECC error.
Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
28
CM7_0_DCTAG
_ECC_ERR
Cortex-M7_0 D-cache Tag ECC Error
Specifies whether the Cortex-M7_0 core's D-cache tag memory detected a multi-bit ECC error.
Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
27
CM7_1_DCDAT
A_ECC_ERR
Cortex-M7_1 D-cache Data Memory ECC Error
Specifies whether the Cortex-M7_1 core's D-cache data memory detected a multi-bit ECC error.
Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
26
CM7_0_DCDAT
A_ECC_ERR
Cortex-M7_0 D-cache Data Memory ECC Error
Specifies whether the Cortex-M7_0 core's D-cache data memory detected a multi-bit ECC error.
Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
25
PRAM0_ECC_E
RR
Multi-Bit ECC Error From PRAM0
Specifies whether a multi-bit ECC error occurred from PRAM0.
Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
24
PRAM1_ECC_E
RR
Multi-Bit ECC Error From PRAM1
Specifies whether a multi-bit ECC error occurred from PRAM1.
Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
23
Multi bit ECC error from SRAM2. Read this bit to identify the reason for a fault in case of FCCU NCF 2.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1307 / 5251


---
# 페이지 56

Table continued from the previous page...
Field
Function
PRAM2_ECC_E
RR
0b - No multi-bit ECC error.
1b - Multi-bit ECC error.
22
LC_ERR
Error In Life Cycle Scanning
Specifies whether an error occurred during life-cycle scanning.
Read this bit to identify the reason of fault in case of FCCU NCF 3.
0b - No error while lifecycle scanning.
1b - Error while lifecycle scanning
21-20
—
Reserved
19
PERIPH_AXBS
_ALARM
Peripheral AXBS_Lite Safety Alarm Status
Specifies whether peripheral AXBS_Lite reported a safety alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
18
MAC_GSKT_AL
ARM
MAC IAHB Gasket Alarm Status
Specifies whether the MAC IAHB gasket reported an alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
17
TCM_AXBS_AL
ARM
TCM AHB Splitter Safety Alarm Status
Specifies whether the TCM AHB splitter reported a safety alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
16
DATA_EDC_ER
R
Data EDC Error
Specifies whether an integrity error occurred on address for safety.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
15
Address EDC Error Status
Specifies whether an integrity error occurred on address for safety.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1308 / 5251


---
# 페이지 57

Table continued from the previous page...
Field
Function
ADDR_EDC_E
RR
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
14
AIPS2_GSKT_A
LARM
AIPS2 IAHB Gasket Alarm Status. Read this bit to identify the reason for a fault in case of FCCU NCF 1.
0b - No alarm indicated by AIPS2 IAHB gasket.
1b - Alarm indicated by AIPS2 IAHB gasket.
13
AIPS1_GSKT_A
LARM
AIPS1 IAHB Gasket Alarm Status. Read this bit to identify the reason for a fault in case of FCCU NCF 1.
0b - No alarm indicated by AIPS1 IAHB gasket.
1b - Alarm indicated by AIPS1 IAHB gasket.
12
QSPI_GSKT_A
LARM
QuadSPI IAHB Gasket Alarm Status
Specifies whether the QuadSPI IAHB gasket reported an alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
11
HSE_GSKT_AL
ARM
HSE IAHB Gasket Alarm Status
Specifies whether the HSE_B IAHB gasket reported an alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
10
—
Reserved
9
DMA_AXBS_AL
ARM
eDMA AXBS_Lite Safety Alarm Status
Specifies whether eDMA AXBS_Lite reported a safety alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
8
SYS_AXBS_AL
ARM
System AXBS Safety Alarm Status
Specifies whether the system AXBS indicated a safety alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1309 / 5251


---
# 페이지 58

Table continued from the previous page...
Field
Function
7
DMA_PERIPH_
GSKT_ALARM
eDMA Peripheral Gasket Alarm Status
Specifies whether the eDMA peripheral AXBS IAHB gasket reported a safety alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
6
DMA_SYS_GS
KT_ALARM
eDMA System Gasket Alarm Status
Specifies whether the IAHB gasket safety alarm, from the eDMA system AXBS IAHB gasket, reported a 
safety alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
5
TCM_GSKT_AL
ARM
TCM IAHB Gasket Monitor Alarm Status
Specifies whether the TCM IAHB gasket reported an alarm. If the value of this field is 1, the gasket reports 
a monitor alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
4
CM7_RCCU2_A
LARM
Cortex-M7 Core Redundant Lockstep Error Status
Specifies whether RCCU reported a lockstep alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 0.
0b - No
1b - Yes
3
CM7_RCCU1_A
LARM
Cortex-M7 Core Lockstep Error Status
Specifies whether RCCU reported a lockstep alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 0.
0b - No
1b - Yes
2
HSE_LOCKUP
HSE_B Core Lockup Status
Specifies whether the HSE_B core is in the Lockup state.
Read this field to identify the reason for a fault in case of FCCU NCF 0.
0b - No
1b - Yes
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1310 / 5251


---
# 페이지 59

Table continued from the previous page...
Field
Function
1
CM7_1_LOCKU
P
Cortex-M7_1 Core Lockup Status
Specifies whether the Cortex_M7_1 core is in the Lockup state.
Read this field to identify the reason for a fault in case of FCCU NCF 0.
0b - No
1b - Yes
0
CM7_0_LOCKU
P
Cortex-M7_0 Core Lockup Status
Specifies whether the Cortex-M7_0 core is in the Lockup state.
Read this field to identify the reason for a fault in case of FCCU NCF 0.
0b - No
1b - Yes
38.2.4 Read-Only GPR On Destructive Reset 4 (DCMROD4)
Offset
Register
Offset
DCMROD4
20Ch
Function
Contains information related to:
• Accidental partial test activation errors.
• Go/No-go indicator supply statuses.
• Flash memory errors.
• Alarm statuses.
This register resets after destructive reset 4.
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1311 / 5251


---
# 페이지 60

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
CM7_2
_L...
TEST_
AC...
TEST_
AC...
Reserv
ed 
VDD2
P5_...
VDD1
P1_...
FLAS
H_E...
Reserv
ed 
PRAM
2_F...
FLAS
H_S...
FLAS
H_R...
FLAS
H_R...
FLAS
H_A...
FLAS
H_E...
Reserv
ed 
Reserv
ed 
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
PF1_D
AT...
PF1_C
OD...
PF0_D
AT...
PF0_C
OD...
HSE_
RAM...
PRAM
1_F...
PRAM
0_F...
DMA_
TCD...
CM7_1
_D...
CM7_1
_D...
CM7_1
_I...
CM7_0
_D...
CM7_0
_D...
CM7_0
_I...
CM7_1
_I...
CM7_0
_I...
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
CM7_2_LOCKU
P
CM7_2 Core Lockup Status
Read this bit to identify the reason of fault in case of FCCU NCF 0.
0b - CM7_2 core not in lockup state.
1b - CM7_2 core in lockup state.
30
TEST_ACTIVA
TION_1_ERR
Accidental Partial Test Activation 1 Error
Specifies whether partial test 1 is activated accidentally.
Read this field to identify the reason for a fault in case of FCCU NCF 5.
0b - No
1b - Yes
29
TEST_ACTIVA
TION_0_ERR
Accidental Partial Test Activation 0 Error
Specifies whether partial test 0 is activated accidentally.
Read this field to identify the reason for a fault in case of FCCU NCF 5.
0b - No
1b - Yes
28
—
Reserved
27
VDD2P5_GNG_
ERR
Go/No-go Indicator For VDD_HV_FLA
Specifies whether the VDD_HV_FLA (double-bond) supply going to XOSC and PLL is clean.
Read this field to identify the reason for a fault in case of FCCU NCF 4.
If this field = 1, the "go" indication specifies a clean supply, and if this field = 0, the "no-go" indication specifies 
an unclean supply with a fault in the double-bond connection or its routing within the chip.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1312 / 5251


---
# 페이지 61

Table continued from the previous page...
Field
Function
0b - Yes
1b - No
26
VDD1P1_GNG_
ERR
Go/No-go Indicator For VDD1PD1
Specifies whether the VDD1PD1 (double-bond) supply going to PLL is clean.
Read this field to identify the reason for a fault in case of FCCU NCF 4.
If this field = 1, the "go" indication specifies a clean supply, and if this field = 0, the "no-go" indication specifies 
an unclean supply with a fault in the double-bond connection or its routing within the chip.
0b - Yes
1b - No
25
FLASH_ECC_E
RR
ECC Error From Flash Controller
This alarm Specifies that the flash controller detected an error in the address ECC manipulation logic 
through EDC. Read this bit to identify the reason for a fault in case of FCCU NCF 3.
0b - No ECC error from flash controller.
1b - ECC error from flash controller.
24
—
Reserved
23
PRAM2_FCCU_
ALARM
Status of PRAM2 safety alarm. This alarm is set on faulty SRAM2 read or read-modify error. Read this 
bit to identify the reason for a fault in case of FCCU NCF 2.
0b - No safety alarm indicated by PRAM2.
1b - Safety alarm indicated by PRAM2.
22
FLASH_SCAN_
ERR
Flash Memory Scan Error Status
Specifies whether the flash memory encountered an error during the DCM flash scanning process because 
of invalid data.
Read this field to identify the reason for a fault in case of FCCU NCF 3.
0b - No
1b - Yes
21
FLASH_RST_E
RR
Flash Reset Error Status
Specifies whether the flash memory encountered a flash memory reset error during its reset reads.
Read this field to identify the reason for a fault in case of FCCU NCF 3.
0b - No
1b - Yes
20
Flash Memory Reference Error Status
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1313 / 5251


---
# 페이지 62

Table continued from the previous page...
Field
Function
FLASH_REF_E
RR
Specifies whether the flash memory encountered a reference current loss or read voltage error during 
previous read(s).
Read this field to identify the reason for a fault in case of FCCU NCF 3.
0b - No
1b - Yes
19
FLASH_ADDR_
ENC_ERR
Flash Memory Address Encode Error Status
Specifies whether FMU reported an address encode error in the flash memory.
During address decoding, if multiple or no address line is selected, FMU reports an address encode error. 
Read this field to identify the reason for a fault in case of FCCU NCF 3.
0b - No
1b - Yes
18
FLASH_EDC_E
RR
Flash Memory EDC Error Status
Specifies whether FMU reported an integrity error after an ECC correction error in the flash memory.
Read this field to identify the reason for a fault in case of FCCU NCF 3.
0b - No
1b - Yes
17
—
Reserved
16
—
Reserved
15
PF1_DATA_EC
C_ERR
Program Flash Memory 1 Data ECC Error Status
Specifies whether FMU reported uncorrectable errors in the flash memory controller port 1 data memory.
These errors are connected to FCCU NCFs and to ERM. See the "Error Reporting Module (ERM)" chapter 
for memory errors and mapping onto ERM channels.
Read this field to identify the reason for a fault in case of FCCU NCF 3.
0b - No
1b - Yes
14
PF1_CODE_EC
C_ERR
Program Flash Memory 1 Code ECC Error Status
Specifies whether FMU reported uncorrectable errors in the flash memory controller port 1 code memory.
These errors are connected to FCCU NCFs and to ERM. See the "Error Reporting Module (ERM)" chapter 
for memory errors and mapping onto ERM channels.
Read this field to identify the reason for a fault in case of FCCU NCF 3.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1314 / 5251


---
# 페이지 63

Table continued from the previous page...
Field
Function
0b - No
1b - Yes
13
PF0_DATA_EC
C_ERR
Program Flash Memory 0 Data ECC Error Status
Specifies whether FMU reported uncorrectable errors in the flash memory controller port 0 data memory.
These errors are connected to FCCU NCFs and to ERM. See the "Error Reporting Module (ERM)" chapter 
for memory errors and mapping onto ERM channels.
Read this field to identify the reason for a fault in case of FCCU NCF 3.
0b - No
1b - Yes
12
PF0_CODE_EC
C_ERR
Program Flash Memory 0 Code ECC Error Status
Specifies whether FMU reported uncorrectable errors in the flash memory controller port 0 code memory.
These errors are connected to FCCU NCFs and to ERM. See the "Error Reporting Module (ERM)" chapter 
for memory errors and mapping onto ERM channels.
Read this field to identify the reason for a fault in case of FCCU NCF 3.
0b - No
1b - Yes
11
HSE_RAM_EC
C_ERR
HSE_B RAM Uncorrectable ECC Status
Specifies whether HSE_B RAM reported an uncorrectable ECC error.
Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
10
PRAM1_FCCU_
ALARM
PRAM1 FCCU Alarm Status
Specifies whether PRAM1 reported a safety alarm.
This field specifies the status of the PRAM1 safety alarm, whether the alarm is set on faulty PRAM1 read 
or read-modify error. Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
9
PRAM0_FCCU_
ALARM
PRAM0 FCCU Alarm Status
Specifies whether PRAM0 reported a safety alarm.
This field specifies the status of the PRAM0 safety alarm, whether the alarm is set on faulty PRAM0 read 
or read-modify error. Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1315 / 5251


---
# 페이지 64

Table continued from the previous page...
Field
Function
8
DMA_TCD_RA
M_ECC_ERR
eDMA TCD RAM ECC Error
Specifies whether the eDMA_TCD memory detected an uncorrectable ECC error.
This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. Read this 
field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
7
CM7_1_DTCM1
_ECC_ERR
Cortex-M7_1 DTCM 1 ECC Error
Specifies whether the Cortex-M7_1 core's DTCM block 1 detected an uncorrectable ECC error.
This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. The 
Cortex-M7_1 core's DTCM consists of two physical blocks. Read this field to identify the reason for a fault 
in case of FCCU NCF 2.
 
The Cortex-M7_1 core's DTCM 1 does not support address ECC errors in S32K324, 
S32K344, and S32K314.
  NOTE  
0b - No
1b - Yes
6
CM7_1_DTCM0
_ECC_ERR
Cortex-M7_1 DTCM 0 ECC Error
Specifies whether the Cortex-M7_1 core's DTCM block 0 detected an uncorrectable ECC error.
This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. The 
Cortex-M7_1 core's DTCM consists of two physical blocks. Read this field to identify the reason for a fault 
in case of FCCU NCF 2.
 
The Cortex-M7_1 core's DTCM 0 does not support address ECC errors in S32K324, 
S32K344, and S32K314.
  NOTE  
0b - No
1b - Yes
5
CM7_1_ITCM_
ECC_ERR
Cortex-M7_1 ITCM ECC Error
Specifies whether the Cortex-M7_1 core's ITCM detected an uncorrectable ECC error.
This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. Read this 
field to identify the reason for a fault in case of FCCU NCF 2.
 
The Cortex-M7_1 core's ITCM does not support address ECC errors in S32K324, S32K344, 
and S32K314.
  NOTE  
0b - No
1b - Yes
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1316 / 5251


---
# 페이지 65

Table continued from the previous page...
Field
Function
4
CM7_0_DTCM1
_ECC_ERR
Cortex-M7_0 DTCM 1 ECC Error
Specifies whether the Cortex-M7_0 core's DTCM block 1 detected an uncorrectable ECC error.
This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. The 
Cortex-M7_0 core's DTCM consists of two physical blocks. Read this field to identify the reason for a fault 
in case of FCCU NCF 2.
 
The Cortex-M7_0 core's DTCM 1 does not support address ECC errors in S32K324, 
S32K344, and S32K314.
  NOTE  
0b - No
1b - Yes
3
CM7_0_DTCM0
_ECC_ERR
Cortex-M7_0 DTCM 0 ECC Error
Specifies whether the Cortex-M7_0 core's DTCM block 0 detected an uncorrectable ECC error.
This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. The 
Cortex-M7_0 core's DTCM consists of two physical blocks. Read this field to identify the reason for a fault 
in case of FCCU NCF 2.
 
The Cortex-M7_0 core's DTCM 0 does not support address ECC errors in S32K324, 
S32K344, and S32K314.
  NOTE  
0b - No
1b - Yes
2
CM7_0_ITCM_
ECC_ERR
Cortex-M7_0 ITCM ECC Error
Specifies whether the Cortex-M7_0 core's ITCM detected an uncorrectable ECC error.
This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. Read this 
field to identify the reason of fault in case of FCCU NCF 2.
 
The Cortex-M7_0 core's ITCM does not support address ECC errors in S32K324, S32K344, 
and S32K314.
  NOTE  
0b - No
1b - Yes
1
CM7_1_ICTAG_
ECC_ERR
Cortex-M7_1 I-cache Tag ECC Error
Specifies whether the Cortex-M7_1 core's I-cache tag memory detected a multi-bit ECC error.
Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1317 / 5251


---
# 페이지 66

Table continued from the previous page...
Field
Function
0
CM7_0_ICTAG_
ECC_ERR
Cortex-M7_0 I-cache Tag ECC Error
Specifies whether the Cortex-M7_0 core's I-cache tag memory detected a multi-bit ECC error.
Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
38.2.5 Read-Only GPR On Destructive Reset 5 (DCMROD5)
Offset
Register
Offset
DCMROD5
210h
Function
Contains information related to:
• ECC and EDC errors.
• Activation and bus errors.
This register resets after destructive reset 5.
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
CM7_2
_D...
CM7_2
_D...
CM7_2
_I...
CM7_2
_I...
CM7_2
_I...
CM7_2
_D...
CM7_2
_D...
CM7_2
_A...
CM7_2
_A...
HSE_
RDA...
CM7_0
_A...
CM7_0
_A...
CM7_1
_A...
CM7_1
_A...
DMA_
RDA...
Reserv
ed 
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
MAC_
RDA...
Reserv
ed 
DEBU
G_A...
MCT_
BUS...
STCU
_BI...
MBIST
_A...
STCU
_NCF 
SW_N
CF_3 
SW_N
CF_2 
SW_N
CF_1 
SW_N
CF_0 
INTM_
3_...
INTM_
2_...
INTM_
1_...
INTM_
0_...
Reserv
ed 
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
Cortex-M7_2 DTCM 1 ECC Error
Specifies whether the Cortex-M7_2 core's DTCM block 1 detected an uncorrectable ECC error.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1318 / 5251


---
# 페이지 67

Table continued from the previous page...
Field
Function
CM7_2_DTCM1
_ECC_ERR
This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. The 
Cortex-M7_2 core's DTCM consists of two physical blocks. Read this field to identify the reason for a fault 
in case of FCCU NCF 2.
 
The Cortex-M7_2 core's DTCM 1 does not support address ECC errors in S32K324, 
S32K344, and S32K314.
  NOTE  
0b - No
1b - Yes
30
CM7_2_DTCM0
_ECC_ERR
Cortex-M7_2 DTCM 0 ECC Error
Specifies whether the Cortex-M7_2 core's DTCM block 0 detected an uncorrectable ECC error.
This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. The 
Cortex-M7_2 core's DTCM consists of two physical blocks. Read this field to identify the reason for a fault 
in case of FCCU NCF 2.
 
The Cortex-M7_2 core's DTCM 0 does not support address ECC errors in S32K324, 
S32K344, and S32K314.
  NOTE  
0b - No
1b - Yes
29
CM7_2_ITCM_
ECC_ERR
Cortex-M7_2 ITCM ECC Error
Specifies whether the Cortex-M7_2 core's ITCM detected an uncorrectable ECC error.
This uncorrectable ECC error consists of a multi-bit data ECC error and an address ECC error. Read this 
field to identify the reason for a fault in case of FCCU NCF 2.
 
The Cortex-M7_2 core's ITCM does not support address ECC errors in S32K324, S32K344, 
and S32K314.
  NOTE  
0b - No
1b - Yes
28
CM7_2_ICTAG_
ECC_ERR
Cortex-M7_2 I-cache Tag ECC Error
Specifies whether the Cortex-M7_2 core's I-cache tag memory reported a multi-bit ECC error.
Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
27
Cortex-M7_2 I-cache Data ECC Error
Specifies whether the Cortex-M7_2 core's I-cache data memory reported a multi-bit ECC error.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1319 / 5251


---
# 페이지 68

Table continued from the previous page...
Field
Function
CM7_2_ICDAT
A_ECC_ERR
Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
26
CM7_2_DCTAG
_ECC_ERR
Cortex-M7_2 D-cache Tag ECC Error
Specifies whether the Cortex-M7_2 core's D-cache tag memory detected a multi-bit ECC error.
Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
25
CM7_2_DCDAT
A_ECC_ERR
Cortex-M7_2 D-cache Data ECC Error
Specifies whether the Cortex-M7_2 core's D-cache data memory detected a multi-bit ECC error.
Read this field to identify the reason for a fault in case of FCCU NCF 2.
0b - No
1b - Yes
24
CM7_2_AHBM_
RDATA_EDC_E
RR
Cortex-M7_2 AHBM Read Data EDC Error
Specifies whether an integrity error is reported on the Cortex-M7_2 core's main read data for safety.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
23
CM7_2_AHBP_
RDATA_EDC_E
RR
Cortex-M7_2 AHBP Read Data EDC Error
Specifies whether an integrity error is reported on the Cortex-M7_2 core's peripheral read data for safety.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
22
HSE_RDATA_E
DC_ERR
HSE_B Read Data EDC Error
Specifies whether an integrity error is reported on the HSE_B read data for safety.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
21
CM7_0_AHBM_
RDATA_EDC_E
RR
Cortex-M7_0 AHBM Read Data EDC Error
Specifies whether an integrity error is reported on the Cortex-M7_0 core's main read data for safety.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1320 / 5251


---
# 페이지 69

Table continued from the previous page...
Field
Function
0b - No
1b - Yes
20
CM7_0_AHBP_
RDATA_EDC_E
RR
Cortex-M7_0 AHBP Read Data EDC Error
Specifies whether an integrity error is reported on the Cortex-M7_0 core's peripheral read data for safety.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
19
CM7_1_AHBM_
RDATA_EDC_E
RR
Cortex-M7_1 AHBM Read Data EDC Error
Specifies whether an integrity error is reported on the Cortex-M7_1 core's main read data for safety.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
18
CM7_1_AHBP_
RDATA_EDC_E
RR
Cortex-M7_1 AHBP Read Data EDC Error
Specifies whether an integrity error is reported on the Cortex-M7_1 core's peripheral read data for safety.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
17
DMA_RDATA_
EDC_ERR
eDMA Read Data EDC Error
Specifies whether an integrity error is reported on the eDMA read data for safety.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
16
—
Reserved
15
MAC_RDATA_
EDC_ERR
MAC Read Data EDC Error
Specifies whether an integrity error is reported on the MAC read data for safety.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
14
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1321 / 5251


---
# 페이지 70

Table continued from the previous page...
Field
Function
13
DEBUG_ACTIV
ATION_ERR
Debug Activation Error
Specifies whether an unintended debug is activated.
This field monitors unintended debug activation. It displays 1 as its value when the core is in halted state 
with the application debug or debugger request not enabled. Read this field to identify the reason for a fault 
in case of FCCU NCF 5.
0b - No
1b - Yes
12
MCT_BUS_ER
R
MCT Bus Error
Fault reported due to illegal access on MBIST Master Controller (MCT). This fault is reported via a 
transfer error indication to the system. Read this bit to identify the reason of fault in case of FCCU NCF 
5.
0b - No transfer error indicated from MCT.
1b - Transfer error indicated from MCT.
11
STCU_BIST_U
SER_CF
STCU2 BIST User Critical Fault (CF)
Specifies whether LBIST or MBIST is enabled accidentally when the fault condition is detected in Run mode.
Read this field to identify the reason for a fault in case of FCCU NCF 5.
0b - No
1b - Yes
10
MBIST_ACTIVA
TION_ERR
MBIST Activation Error
Specifies whether an accidental backdoor access is enabled on memories.
DCMRWD5[MBIST_ACTIVATION_ERR_EN] needs to be disabled on FCCU when performing a 
fault injection.
Read this field to identify the reason for a fault in case of FCCU NCF 5.
0b - No
1b - Yes
9
STCU_NCF
STCU2 NCF Result Error
Specifies whether STCU2 NCF, which is a BIST result error, is reported.
Read this field to identify the reason for a fault in case of FCCU NCF 5.
0b - No
1b - Yes
8
SW_NCF_3
Software NCF3 Status
Specifies whether DCMRWF1[FCCU_SW_NCF3] is enabled.
Read this field to identify the reason for a fault in case of FCCU NCF 7.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1322 / 5251


---
# 페이지 71

Table continued from the previous page...
Field
Function
0b - No
1b - Yes
7
SW_NCF_2
Software NCF2 Status
Specifies whether DCMRWF1[FCCU_SW_NCF2] is enabled.
Read this field to identify the reason for a fault in case of FCCU NCF 7.
0b - No
1b - Yes
6
SW_NCF_1
Software NCF1 Status
Specifies whether DCMRWF1[FCCU_SW_NCF1] is enabled.
Read this field to identify the reason for a fault in case of FCCU NCF 7.
0b - No
1b - Yes
5
SW_NCF_0
Software NCF 0 Status
Specifies whether DCMRWF1[FCCU_SW_NCF0] is enabled.
Read this field to identify the reason for a fault in case of FCCU NCF 7.
0b - No
1b - Yes
4
INTM_3_ERR
INTM_3 Error
Specifies whether INTM_3 reported an error.
The reported error is recorded in INTM.INTM_STATUS3. See the "Functional description" section of the 
"Interrupt Monitor (INTM)" chapter for details.
Read this field to identify the reason for a fault in case of FCCU NCF 6.
0b - No
1b - Yes
3
INTM_2_ERR
INTM_2 Error
Specifies whether INTM_2 reported an error.
The reported error is recorded in INTM.INTM_STATUS2. See the "Functional description" section of the 
"Interrupt Monitor (INTM)" chapter for details.
Read this field to identify the reason for a fault in case of FCCU NCF 6.
0b - No
1b - Yes
2
INTM_1 Error
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1323 / 5251


---
# 페이지 72

Table continued from the previous page...
Field
Function
INTM_1_ERR
Specifies whether INTM_1 reported an error.
The reported error is recorded in INTM.INTM_STATUS1. See the "Functional description" section of the 
"Interrupt Monitor (INTM)" chapter for details.
Read this field to identify the reason for a fault in case of FCCU NCF 6.
0b - No
1b - Yes
1
INTM_0_ERR
INTM_0 Error
Specifies whether INTM_0 reported an error.
The reported error is recorded in INTM.INTM_STATUS0. See the "Functional description" section of the 
"Interrupt Monitor (INTM)" chapter for details.
Read this field to identify the reason for a fault in case of FCCU NCF 6.
0b - No
1b - Yes
0
—
Reserved
38.2.6 Read-Only GPR On Destructive Reset 6 (DCMROD6)
Offset
Register
Offset
DCMROD6
214h
Function
Contains information related to:
• Safety, RCCU, and AXI alarm statuses.
• Core memory errors.
• CF and NCF errors.
• ECC and EDC errors.
This register resets after destructive reset 6.
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1324 / 5251


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
Reserv
ed 
TCM_
PRA...
Reserv
ed 
Reserv
ed 
Reserv
ed 
AIPS0
_G...
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
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
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
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
—
Reserved
30
TCM_PRAM_A
XBS_ALARM
Status of TCM_PRAM AXBS_Lite safety alarm. Read this bit to identify the reason of fault in case of 
FCCU NCF 1.
0b - No safety alarm indicated by TCM_PRAM AXBS_Lite.
1b - Safety alarm indicated by TCM_PRAM AXBS_Lite.
29
—
Reserved
28
—
Reserved
27
—
Reserved
26
AIPS0_GSKT_A
LARM
AIPS0 IAHB Gasket Alarm Status. Read this bit to identify the reason of fault in case of FCCU NCF 1.
0b - No alarm indicated by AIPS0 IAHB gasket.
1b - Alarm indicated by AIPS0 IAHB gasket.
25
—
Reserved
24
—
Reserved
23
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1325 / 5251


---
# 페이지 74

Table continued from the previous page...
Field
Function
—
22
—
Reserved
21
—
Reserved
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
—
Reserved
9
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1326 / 5251


---
# 페이지 75

Table continued from the previous page...
Field
Function
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
38.2.7 Read-Only GPR On Destructive Reset 7 (DCMROD7)
Offset
Register
Offset
DCMROD7
218h
Function
Contains information related to:
• LVDS pad receiver fault statuses.
• AXBS, AHBP, and AHBM alarm statuses.
This field resets after destructive reset 7.
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1327 / 5251


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
Reserv
ed 
CM7_2
_A...
CM7_1
_A...
CM7_0
_A...
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
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
Reserv
ed 
Reserv
ed 
Reserv
ed 
VDD2
P5_...
VDD1
P1_...
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
CM7_2
_A...
CM7_1
_A...
CM7_0
_A...
CM7_2
_A...
CM7_1
_A...
CM7_0
_A...
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
—
Reserved
30
CM7_2_AHBS_
ALARM
CM7_2 AHBS interface IAHB Gasket monitor alarm status. Read this bit to identify the reason of fault in 
case of FCCU NCF 1.
0b - No alarm reported from CM7_0 AHBS interface IAHB gasket.
1b - Monitor alarm reported from CM7_0 AHBS interface IAHB gasket.
29
CM7_1_AHBS_
ALARM
CM7_1 AHBS interface IAHB Gasket monitor alarm status. Read this bit to identify the reason of fault in 
case of FCCU NCF 1.
0b - No alarm reported from CM7_0 AHBS interface IAHB gasket.
1b - Monitor alarm reported from CM7_0 AHBS interface IAHB gasket.
28
CM7_0_AHBS_
ALARM
CM7_0 AHBS interface IAHB Gasket monitor alarm status. Read this bit to identify the reason of fault in 
case of FCCU NCF 1.
0b - No alarm reported from CM7_0 AHBS interface IAHB gasket.
1b - Monitor alarm reported from CM7_0 AHBS interface IAHB gasket.
27
—
Reserved
26
—
Reserved
25
—
Reserved
24
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1328 / 5251


---
# 페이지 77

Table continued from the previous page...
Field
Function
—
23
—
Reserved
22
—
Reserved
21
—
Reserved
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
VDD2P5_GNG2
_ERR
Go/Nogo indicator status for VDD_HV_FLA (triple bond) going to FXOSC and PLL. Read this bit to 
identify the reason of fault in case of FCCU NCF4.
0b - Go indication referring to the supply being clean.
1b - No go indication referring to the supply being unclean and a fault in double bond connection 
or its routing within the chip.
11
Go/Nogo indicator status for VDD_HV_FLA (triple bond) going to FXOSC and PLL. Read this bit to 
identify the reason of fault in case of FCCU NCF4.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1329 / 5251


---
# 페이지 78

Table continued from the previous page...
Field
Function
VDD1P1_GNG2
_ERR
0b - Go indication referring to the supply being clean.
1b - No go indication referring to the supply being unclean and a fault in double bond connection 
or its routing within the chip.
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
CM7_2_AHBP_
ALARM
Cortex-M7_2 AHBP Alarm Status
Specifies the Cortex-M7_2 AHBP interface IAHB gasket monitor alarm status, showing whether or not the 
gasket reported a monitor alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
4
CM7_1_AHBP_
ALARM
Cortex-M7_1 AHBP Alarm Status
Specifies the Cortex-M7_1 AHBP interface IAHB gasket monitor alarm status, showing whether or not the 
gasket reported a monitor alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
3
CM7_0_AHBP_
ALARM
Cortex-M7_0 AHBP Alarm Status
Specifies the Cortex-M7_0 AHBP interface IAHB gasket monitor alarm status, showing whether or not the 
gasket reported a monitor alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
2
Cortex-M7_2 AHBM Alarm Status
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1330 / 5251


---
# 페이지 79

Table continued from the previous page...
Field
Function
CM7_2_AHBM_
ALARM
Specifies the Cortex-M7_2 AHBM interface IAHB gasket monitor alarm status, showing whether or not the 
gasket reported a monitor alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
1
CM7_1_AHBM_
ALARM
Cortex-M7_1 AHBM Alarm Status
Specifies the Cortex-M7_1 AHBM interface IAHB gasket monitor alarm status, showing whether or not the 
gasket reported a monitor alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
0
CM7_0_AHBM_
ALARM
Cortex-M7_0 AHBM Alarm Status
Specifies the Cortex-M7_0 AHBM interface IAHB gasket monitor alarm status, showing whether or not the 
gasket reported a monitor alarm.
Read this field to identify the reason for a fault in case of FCCU NCF 1.
0b - No
1b - Yes
38.2.8 Read-Only GPR On Destructive Reset Register (DCMROD8)
Offset
Register
Offset
DCMROD8
21Ch
Function
This is a read only general purpose register which captures the states and gets reset on destructive reset. Writing 1 to a bit in 
this register, clears the bit.
 
If the bit signal gets enabled again or is always enabled, the bit gets configured even after writing 1 to clear the bit.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1331 / 5251


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
Reserv
ed 
Reserv
ed 
CM7_3
_D...
CM7_3
_D...
CM7_3
_I...
CM7_3
_I...
CM7_3
_I...
CM7_3
_D...
CM7_3
_D...
CM7_3
_A...
CM7_3
_A...
Reserv
ed 
AES_A
CC...
AES_A
CC...
ACE_F
EE...
ACE_
RES...
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
Reserv
ed 
CM7_3
_A...
HSE_
AES...
CM7_3
_A...
CM7_3
_A...
MAC2
_RD...
MAC2
_GS...
Reserv
ed 
PERIP
H_...
CM7_2
_R...
CM7_2
_R...
CM7_3
_L...
Reserved 
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
Reset
0
0
0
0
0
0
0
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
30
—
Reserved
29
CM7_3_DTCM1
_ECC_ERR
Status of Uncorrectable ECC error from CM7_3 Data TCM memory block 1. This uncorrectable ECC 
error consists of multi-bit data ECC error and address ECC error. The CM7_3 Data TCM physically 
consists of two blocks. Read this bit to identify the reason of fault in case of FCCU NCF 2.
0b - Uncorrectable ECC error detection not enabled at FCCU
1b - Uncorrectable ECC error detection enabled at FCCU
28
CM7_3_DTCM0
_ECC_ERR
Status of Uncorrectable ECC error from CM7_3 Data TCM memory block 0. This uncorrectable ECC 
error consists of multi-bit data ECC error and address ECC error. The CM7_3 Data TCM physically 
consists of two blocks. Read this bit to identify the reason of fault in case of FCCU NCF 2.
0b - Uncorrectable ECC error detection not enabled at FCCU
1b - Uncorrectable ECC error detection enabled at FCCU
27
CM7_3_ITCM_
ECC_ERR
Status of Uncorrectable ECC error from CM7_3 Instruction TCM memory. This uncorrectable ECC error 
consists of multi-bit data ECC error and address ECC error. Read this bit to identify the reason of fault in 
case of FCCU NCF 2.
0b - No uncorrectable ECC error detected
1b - Uncorrectable ECC error detected
26
CM7_3_ICTAG_
ECC_ERR
Status of Multi bit ECC error from CM7_3 ICache tag memory. Read this bit to identify the reason of fault 
in case of FCCU NCF 2.
0b - No multi-bit ECC error reported
1b - Multi-bit ECC error reported
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1332 / 5251


---
# 페이지 81

Table continued from the previous page...
Field
Function
25
CM7_3_ICDAT
A_ECC_ERR
Status of Multi bit ECC error from CM7_3 ICache data memory. Read this bit to identify the reason of 
fault in case of FCCU NCF 2.
0b - No multi-bit ECC error reported
1b - Multi-bit ECC error reported
24
CM7_3_DCTAG
_ECC_ERR
Status of Multi bit ECC error from CM7_3 DCache tag memory. Read this bit to identify the reason of 
fault in case of FCCU NCF 2.
0b - No multi-bit ECC error reported
1b - Multi-bit ECC error reported
23
CM7_3_DCDAT
A_ECC_ERR
Status of Multi bit ECC error from CM7_3 DCache data memory. Read this bit to identify the reason of 
fault in case of FCCU NCF 2.
0b - No multi-bit ECC error reported
1b - Multi-bit ECC error reported
22
CM7_3_AHBP_
ALARM
Status of CM7_3 AHBP interface IAHB Gasket monitor alarm. Read this bit to identify the reason of fault 
in case of FCCU NCF 1.
0b - No alarm reported
1b - Monitor alarm reported
21
CM7_3_AHBM_
ALARM
Status of CM7_3 AHBM interface IAHB Gasket monitor alarm. Read this bit to identify the reason of fault 
in case of FCCU NCF 1.
0b - No alarm reported
1b - Monitor alarm reported
20
—
Reserved
19
AES_ACCEL_G
SKT_ALARM
AES ACCEL IAHB Gasket monitor alarm status. Read this bit to identify the reason of fault in case of 
FCCU NCF 1.
0b - No alarm reported
1b - Monitor alarm reported
18
AES_ACCEL_A
XBS_ALARM
AES_ACCEL AXBS_Lite safety alarm status. Read this bit to identify the reason of fault in case of FCCU 
NCF 1.
0b - No safety alarm indicated
1b - Safety alarm indicated
17
ACE_FEED_RD
ATA_EDC_ERR
Status of Integrity error on ACE ACCEL FEED DMA master port read data for safety. Read this bit to 
identify the reason of fault in case of FCCU NCF 1.
0b - No integrity error reported
1b - Integrity error reported
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1333 / 5251


---
# 페이지 82

Table continued from the previous page...
Field
Function
16
ACE_RESULT_
RDATA_EDC_E
RR
Status of Integrity error on ACE ACCEL RESULT DMA master port read data for safety. Read this bit to 
identify the reason of fault in case of FCCU NCF 1.
0b - No integrity error reported
1b - Integrity error reported
15
—
Reserved
14
CM7_3_AHBS_
ALARM
CM7_3 AHBS interface IAHB Gasket monitor alarm status. Read this bit to identify the reason of fault in 
case of FCCU NCF 1.
0b - No alarm reported
1b - Monitor alarm reported
13
HSE_AES_ACC
EL_AXBS_ALA
RM
HSE_AES_ACCEL AXBS_Lite safety alarm status. Read this bit to identify the reason of fault in case of 
FCCU NCF 1.
0b - No safety alarm indicated
1b - Safety alarm indicated
12
CM7_3_AHBM_
RDATA_EDC_E
RR
Status of Integrity error on CM7_3 main read data for safety. Read this bit to identify the reason of fault in 
case of FCCU NCF 1.
0b - No integrity error reported
1b - Integrity error reported
11
CM7_3_AHBP_
RDATA_EDC_E
RR
Status of Integrity error on CM7_3 peripheral read data for safety. Read this bit to identify the reason of 
fault in case of FCCU NCF 1.
0b - No integrity error reported
1b - Integrity error reported
10
MAC2_RDATA_
EDC_ERR
Status of Integrity(EDC) error on MAC2 read data for safety. Read this bit to identify the reason of fault in 
case of FCCU NCF 1.
0b - No integrity error reported
1b - Integrity error reported
9
MAC2_GSKT_A
LARM
MAC2 IAHB gasket alarm status. Read this bit to identify the reason of fault in case of FCCU NCF 1.
0b - No alarm indicated
1b - Alarm indicated
8
—
Reserved
7
Peripheral AXBS bridge S3 IAHB gasket alarm status. Read this bit to identify the reason of fault in case 
of FCCU NCF 1.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1334 / 5251


---
# 페이지 83

Table continued from the previous page...
Field
Function
PERIPH_AXBS
_S3_GSKT_AL
ARM
0b - No alarm reported
1b - Monitor alarm reported
6
CM7_2_RCCU2
_ALARM
Cortex M7 cores (CM7_2 and CM7_2_checker core) redundant lockstep error status. Read this bit to 
identify the reason of fault in case of FCCU NCF 0.
0b - No Error reported.
1b - Error reported
5
CM7_2_RCCU1
_ALARM
Cortex M7 cores (CM7_2 and CM7_2_checker core) lockstep error status. Read this bit to identify the 
reason of fault in case of FCCU NCF 0.
0b - No Error reported.
1b - Error reported
4
CM7_3_LOCKU
P
CM7_3 core lockup status. Read this bit to identify the reason of fault in case of FCCU NCF 0.
0b - Not in lockup state
1b - In lockup state
3-0
—
Reserved
38.2.9 Read-Only GPR On Destructive Reset 9 (DCMROD9)
Offset
Register
Offset
DCMROD9
220h
Function
This is a read only general purpose register which captures the states and gets reset on destructive reset. Writing 1 to a bit in 
this register, clears the bit.
 
If the bit signal gets enabled again or is always enabled, the bit gets configured even after writing 1 to clear the bit.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1335 / 5251


---
# 페이지 84

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
PF1_1
_C...
PF1_0
_C...
PF0_1
_C...
PF0_0
_C...
PF1_1
_C...
PF1_0
_C...
PF0_1
_C...
PF0_0
_C...
PRAM
3_F...
PRAM
3_E...
FLASH
1_...
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
Reset
0
0
0
0
0
0
0
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
Reserv
ed 
FLAS
H1_...
FLAS
H1_...
FLAS
H1_...
FLAS
H1_...
PF1_1
_D...
PF1_1
_C...
PF1_0
_D...
PF1_0
_C...
AES_
RES...
AES_F
EE...
AES_K
P_...
AES_
RES...
AES_
RES...
AES_F
EE...
AES_F
EE...
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
Reset
0
0
0
0
0
0
0
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
31-27
—
Reserved
26
PF1_1_CHK_C
MP_ALARM
Status of PFLASH3 checker (redundant) safety comparator alarm. Read this bit to identify the reason of 
fault in case of FCCU NCF 3.
0b - No comparator error indicated by PFLASH3.
1b - Comparator error indicated by PFLASH3.
25
PF1_0_CHK_C
MP_ALARM
Status of PFLASH2 checker (redundant) safety comparator alarm. Read this bit to identify the reason of 
fault in case of FCCU NCF 3.
0b - No comparator error indicated by PFLASH2.
1b - Comparator error indicated by PFLASH2.
24
PF0_1_CHK_C
MP_ALARM
Status of PFLASH1 checker (redundant) safety comparator alarm. Read this bit to identify the reason of 
fault in case of FCCU NCF 3.
0b - No comparator error indicated by PFLASH1.
1b - Comparator error indicated by PFLASH1.
23
PF0_0_CHK_C
MP_ALARM
Status of PFLASH0 checker (redundant) safety comparator alarm. Read this bit to identify the reason of 
fault in case of FCCU NCF 3.
0b - No comparator error indicated by PFLASH0.
1b - Comparator error indicated by PFLASH0.
22
PF1_1_CMP_A
LARM
Status of PFLASH3 safety comparator alarm. Read this bit to identify the reason of fault in case of FCCU 
NCF 3.
0b - No comparator error indicated by PFLASH3.
1b - Comparator error indicated by PFLASH3.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1336 / 5251


---
# 페이지 85

Table continued from the previous page...
Field
Function
21
PF1_0_CMP_A
LARM
Status of PFLASH2 safety comparator alarm. Read this bit to identify the reason of fault in case of FCCU 
NCF 3.
0b - No comparator error indicated by PFLASH2.
1b - Comparator error indicated by PFLASH2.
20
PF0_1_CMP_A
LARM
Status of PFLASH1 safety comparator alarm. Read this bit to identify the reason of fault in case of FCCU 
NCF 3.
0b - No comparator error indicated by PFLASH1.
1b - Comparator error indicated by PFLASH1.
19
PF0_0_CMP_A
LARM
Status of PFLASH0 safety comparator alarm. Read this bit to identify the reason of fault in case of FCCU 
NCF 3.
0b - No comparator error indicated by PFLASH0.
1b - Comparator error indicated by PFLASH0.
18
PRAM3_FCCU_
ALARM
PRAM3 FCCU Alarm Status
Status of PRAM3 safety alarm. This alarm is set on faulty SRAM3 read or read modify error. Read this 
bit to identify the reason of fault in case of FCCU NCF 2.
0b - No safety alarm indicated by PRAM3.
1b - Safety alarm indicated by PRAM3.
17
PRAM3_ECC_E
RR
PRAM3 Multi-bit ECC Error Status
Multi-bit ECC error from SRAM3. Read this bit to identify the reason of fault in case of FCCU NCF 2.
0b - No multi-bit ECC error.
1b - Multi-bit ECC error.
16
FLASH1_ECC_
ERR
ECC Error From Flash Controller1
This alarm indicates that the flash controller1 detected an error in the address ECC manipulation logic 
through EDC. Read this bit to identify the reason of fault in case of FCCU NCF 3.
0b - No ECC error from flash controller1.
1b - ECC error from flash controller1.
15
—
Reserved
14
FLASH1_RST_
ERR
Flash1 Reset Error Status
This error indication is set when flash1 encounters errors during its reset reads. Read this bit to identify 
the reason of fault in case of FCCU NCF 3.
0b - No flash1 reset error indicated.
1b - Flash1 reset error indicated.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1337 / 5251


---
# 페이지 86

Table continued from the previous page...
Field
Function
13
FLASH1_REF_
ERR
Flash1 Reference Error
Flash1 reference current loss or read voltage error while prevoius read. Read this bit to identify the 
reason of fault in case of FCCU NCF 3.
0b - No reference current loss or read voltage error while previous read.
1b - Reference current loss or read voltage error while previous read.
12
FLASH1_ADDR
_ENC_ERR
Flash1 Address Encode Error
In address decoding, if multiple or no address line is selected, FMU reports address encode error. Read 
this bit to identify the reason of fault in case of FCCU NCF 3.
0b - No address encode error in flash1.
1b - Address enocde error in flash1.
11
FLASH1_EDC_
ERR
Flash1 EDC Error
Status of flash1 ECC correction error through EDC reported by FMU. Read this bit to identify the reason 
of fault in case of FCCU NCF 3.
0b - No EDC after ECC error reported in flash1.
1b - EDC after ECC error reported in flash1.
10
PF1_1_DATA_E
CC_ERR
Flash3 Data ECC Uncorrectable Error
The errors are reported from the FMU and are connected to FCCU NCFs. These are also connected to 
ERM. See ERM chapter for the memory errors and mapping onto ERM channels. Read this bit to identify 
the reason of fault in case of FCCU NCF 3. The path is from FMU to PFLASH controller to ERM to 
FCCU.
0b - No uncorrectable error reported in flash controller port 3 data memory by FMU.
1b - Uncorrectable error reported in flash controller port 3 data memory by FMU.
9
PF1_1_CODE_
ECC_ERR
Flash3 Code ECC Uncorrectable Error
The errors are reported from the FMU and are connected to FCCU NCFs. These are also connected to 
ERM. See ERM chapter for the memory errors and mapping onto ERM channels. Read this bit to identify 
the reason of fault in case of FCCU NCF 3. The path is from FMU to PFLASH controller to ERM to 
FCCU.
0b - No uncorrectable error reported in flash controller port 3 code memory by FMU.
1b - Uncorrectable error reported in flash controller port 3 code memory by FMU.
8
PF1_0_DATA_E
CC_ERR
Flash2 Data ECC Uncorrectable Error
The errors are reported from the FMU and are connected to FCCU NCFs. These are also connected to 
ERM. See ERM chapter for the memory errors and mapping onto ERM channels. Read this bit to identify 
the reason of fault in case of FCCU NCF 3. The path is from FMU to PFLASH controller to ERM to 
FCCU.
0b - No uncorrectable error reported in flash controller port 2 data memory by FMU.
1b - Uncorrectable error reported in flash controller port 2 data memory by FMU.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1338 / 5251


---
# 페이지 87

Table continued from the previous page...
Field
Function
7
PF1_0_CODE_
ECC_ERR
Flash2 Code ECC Uncorrectable Error
The errors are reported from the FMU and are connected to FCCU NCFs. These are also connected to 
ERM. See ERM chapter for the memory errors and mapping onto ERM channels. Read this bit to identify 
the reason of fault in case of FCCU NCF 3. The path is from FMU to PFLASH controller to ERM to 
FCCU.
0b - No uncorrectable error reported in flash controller port 2 code memory by FMU.
1b - Uncorrectable error reported in flash controller port 2 code memory by FMU.
6
AES_RESULT_
DID_SAFETY_
ERR
AES RESULT DMA DID error status
Read this bit to identify the reason of fault in case of FCCU NCF 2.
0b - AES RESULT DMA DID error not reported.
1b - AES RESULT DMA DID error reported.
5
AES_FEED_DI
D_SAFETY_ER
R
AES FEED DMA DID Error Status
Read this bit to identify the reason of fault in case of FCCU NCF 2.
0b - AES FEED DMA DID error not reported.
1b - AES FEED DMA DID error reported.
4
AES_KP_CRC_
SAFETY_ERR
AES Key Property CRC Safety Error status
Read this bit to identify the reason of fault in case of FCCU NCF 2.
0b - AES key-property CRC safety error not reported.
1b - AES key-property CRC safety error reported.
3
AES_RESULT_
DMA_TCD_AD
DR_ECC_ERR
AES ACCEL RESULT DMA_TCD Address ECC Error Status
Read this bit to identify the reason of fault in case of FCCU NCF 2.
0b - No address error reported in AES ACCEL RESULT DMA_TCD memory.
1b - Address error reported in AES ACCEL RESULT DMA_TCD memory.
2
AES_RESULT_
DMA_TCD_EC
C_ERR
AES ACCEL RESULT DMA_TCD memory uncorrectable ECC error status. Read this bit to identify the 
reason of fault in case of FCCU NCF 2.
0b - No uncorrectable error reported
1b - Uncorrectable error reported
1
AES_FEED_DM
A_TCD_ADDR_
ECC_ERR
AES ACCEL FEED DMA TCD Address ECC Error Status
Read this bit to identify the reason of fault in case of FCCU NCF 2.
0b - No address error reported in AES ACCEL FEED DMA_TCD memory.
1b - Address error reported in AES ACCEL FEED DMA_TCD memory.
0
AES ACCEL FEED DMA_TCD memory uncorrectable ECC error status. Read this bit to identify the 
reason of fault in case of FCCU NCF 2.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1339 / 5251


---
# 페이지 88

Table continued from the previous page...
Field
Function
AES_FEED_DM
A_TCD_ECC_E
RR
0b - No uncorrectable error reported
1b - Uncorrectable error reported
38.2.10 Read-Only GPR On Functional Reset 1 (DCMROF1)
Offset
Register
Offset
DCMROF1
300h
Function
Specifies current transfer channel ID.
This register resets after functional reset 1.
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
AES_RESULT_DID_ERR_DID 
AES_R
ES...
AES_R
ES...
Reserved 
AES_FEED_DID_ERR_DID 
AES_F
EE...
AES_F
EE...
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
Reserved 
Reserved 
Reserv
ed 
Reserv
ed 
Reserved 
MAC1
_MD...
MAC1
_MD...
MAC1
_MD...
MAC_
MDC...
MAC_
MDC...
MAC_
MDC...
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
Reset
0
0
0
0
0
0
0
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
29-26
AES_RESULT_
DID_ERR_DID
Indicates DID[3:0] value when the AES result DID error was reported.
25
Indicates whether the non-secure attribute was set or not when the AES result DID error was reported.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1340 / 5251


---
# 페이지 89

Table continued from the previous page...
Field
Function
AES_RESULT_
DID_ERR_NS
0b - Not set
1b - Set
24
AES_RESULT_
DID_ERR_PRIV
Indicates whether the privilege attribute was set or not when the AES result DID error was reported.
0b - Not set
1b - Set
23-22
—
Reserved
21-18
AES_FEED_DI
D_ERR_DID
Indicates DID[3:0] value when the AES feed DID error was reported.
17
AES_FEED_DI
D_ERR_NS
Indicates whether the non-secure attribute was set or not when the AES feed DID error was reported.
0b - Not set
1b - Set
16
AES_FEED_DI
D_ERR_PRIV
Indicates whether the privilege attribute was set or not when the AES feed DID error was reported.
0b - Not set
1b - Set
15-14
—
Reserved
13-10
—
Reserved
9
—
Reserved
8
—
Reserved
7-6
—
Reserved
5
MAC1_MDC_C
HID_2
MAC eDMA Channel ID2 Status
Specifies whether channel ID2 is the current transfer channel ID.
0b - No
1b - Yes
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1341 / 5251


---
# 페이지 90

Table continued from the previous page...
Field
Function
4
MAC1_MDC_C
HID_1
MAC eDMA Channel ID1 Status
Specifies whether channel ID1 is the current transfer channel ID.
0b - No
1b - Yes
3
MAC1_MDC_C
HID_0
MAC eDMA Channel ID0 Status
Specifies whether channel ID0 is the current transfer channel ID.
0b - No
1b - Yes
2
MAC_MDC_CHI
D_2
MAC eDMA Channel ID2 Status
Specifies whether channel ID2 is the current transfer channel ID.
0b - No
1b - Yes
1
MAC_MDC_CHI
D_1
MAC eDMA Channel ID1 Status
Specifies whether channel ID1 is the current transfer channel ID.
0b - No
1b - Yes
0
MAC_MDC_CHI
D_0
MAC eDMA Channel ID0 Status
Specifies whether channel ID0 is the current transfer channel ID.
0b - No
1b - Yes
38.2.11 Read-Only GPR On Functional Reset 2 (DCMROF2)
Offset
Register
Offset
DCMROF2
304h
Function
Specifies the SDID0 contents that DCM scans from the flash memory.
This register resets after functional reset 2.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1342 / 5251


---
# 페이지 91

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
DCF_SDID0 
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
DCF_SDID0 
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
DCF_SDID0
DCF Client SDID 0 Configuration
38.2.12 Read-Only GPR On Functional Reset 3 (DCMROF3)
Offset
Register
Offset
DCMROF3
308h
Function
Specifies the SDID1 contents that DCM scans from the flash memory.
This register resets after functional reset 3.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1343 / 5251


---
# 페이지 92

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
DCF_SDID1 
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
DCF_SDID1 
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
DCF_SDID1
DCF Client SDID 1 Configuration
38.2.13 Read-Only GPR On Functional Reset 4 (DCMROF4)
Offset
Register
Offset
DCMROF4
30Ch
Function
Specifies the SDID2 contents that DCM scans from the flash memory.
This register resets after functional reset 4.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1344 / 5251


---
# 페이지 93

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
DCF_SDID2 
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
DCF_SDID2 
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
DCF_SDID2
DCF Client SDID 2 Configuration
38.2.14 Read-Only GPR On Functional Reset 5 (DCMROF5)
Offset
Register
Offset
DCMROF5
310h
Function
Specifies the SDID3 contents that DCM scans from the flash memory.
This register resets after functional reset 5.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1345 / 5251


---
# 페이지 94

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
DCF_SDID3 
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
DCF_SDID3 
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
DCF_SDID3
DCF Client SDID 3 Configuration
38.2.15 Read-Only GPR On Functional Reset 6 (DCMROF6)
Offset
Register
Offset
DCMROF6
314h
Function
Specifies the SDID4 contents that DCM scans from the flash memory.
This register resets after functional reset 6.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1346 / 5251


---
# 페이지 95

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
DCF_SDID4 
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
DCF_SDID4 
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
DCF_SDID4
DCF Client SDID 4 Configuration
38.2.16 Read-Only GPR On Functional Reset 7 (DCMROF7)
Offset
Register
Offset
DCMROF7
318h
Function
Specifies the SDID5 contents that DCM scans from the flash memory.
This register resets after functional reset 7.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1347 / 5251


---
# 페이지 96

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
DCF_SDID5 
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
DCF_SDID5 
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
DCF_SDID5
DCF Client SDID 5 Configuration
38.2.17 Read-Only GPR On Functional Reset 8 (DCMROF8)
Offset
Register
Offset
DCMROF8
31Ch
Function
Specifies the SDID6 contents that DCM scans from the flash memory.
This register resets after functional reset 8.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1348 / 5251


---
# 페이지 97

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
DCF_SDID6 
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
DCF_SDID6 
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
DCF_SDID6
DCF Client SDID 6 Configuration
38.2.18 Read-Only GPR On Functional Reset 9 (DCMROF9)
Offset
Register
Offset
DCMROF9
320h
Function
Specifies the SDID7 contents that DCM scans from the flash memory.
This register resets after functional reset 9.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1349 / 5251


---
# 페이지 98

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
DCF_SDID7 
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
DCF_SDID7 
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
DCF_SDID7
DCF Client SDID 7 Configuration
38.2.19 Read-Only GPR On Functional Reset 10 (DCMROF10)
Offset
Register
Offset
DCMROF10
324h
Function
Specifies the SDID8 contents that DCM scans from the flash memory.
This register resets after functional reset 10.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1350 / 5251


---
# 페이지 99

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
DCF_SDID8 
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
DCF_SDID8 
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
DCF_SDID8
DCF Client SDID 8 Configuration
38.2.20 Read-Only GPR On Functional Reset 11 (DCMROF11)
Offset
Register
Offset
DCMROF11
328h
Function
Specifies the SDID9 contents that DCM scans from the flash memory.
This register resets after functional reset 11.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1351 / 5251


---
# 페이지 100

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
DCF_SDID9 
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
DCF_SDID9 
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
DCF_SDID9
DCF Client SDID 9 Configuration
38.2.21 Read-Only GPR On Functional Reset 12 (DCMROF12)
Offset
Register
Offset
DCMROF12
32Ch
Function
Specifies the SDID10 contents that DCM scans from the flash memory.
This register resets after functional reset 12.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1352 / 5251


---
# 페이지 101

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
DCF_SDID10 
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
DCF_SDID10 
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
DCF_SDID10
DCF Client SDID 10 Configuration
38.2.22 Read-Only GPR On Functional Reset 13 (DCMROF13)
Offset
Register
Offset
DCMROF13
330h
Function
Specifies the SDID11 contents that DCM scans from the flash memory.
This register resets after functional reset 13.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1353 / 5251


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
DCF_SDID11 
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
DCF_SDID11 
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
DCF_SDID11
DCF Client SDID 11 Configuration
38.2.23 Read-Only GPR On Functional Reset 14 (DCMROF14)
Offset
Register
Offset
DCMROF14
334h
Function
Specifies the SDID12 contents that DCM scans from flash memory.
This register resets after functional reset 14.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1354 / 5251


---
# 페이지 103

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
DCF_SDID12 
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
DCF_SDID12 
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
DCF_SDID12
DCF Client SDID 12 Configuration
38.2.24 Read-Only GPR On Functional Reset 15 (DCMROF15)
Offset
Register
Offset
DCMROF15
338h
Function
Specifies the SDID13 contents that DCM scans from the flash memory.
This register resets after functional reset 15.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1355 / 5251


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
DCF_SDID13 
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
DCF_SDID13 
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
DCF_SDID13
DCF Client SDID 13 Configuration
38.2.25 Read-Only GPR On Functional Reset 16 (DCMROF16)
Offset
Register
Offset
DCMROF16
33Ch
Function
Specifies the SDID14 contents that DCM scans from the flash memory.
This register resets after functional reset 16.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1356 / 5251


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
DCF_SDID14 
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
DCF_SDID14 
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
DCF_SDID14
DCF Client SDID 14 Configuration
38.2.26 Read-Only GPR On Functional Reset 17 (DCMROF17)
Offset
Register
Offset
DCMROF17
340h
Function
Specifies the SDID15 contents that DCM scans from the flash memory.
This register resets after functional reset 17.
 
See the DCF clients file attached to this document for more information. The Utest section contains chip-
configurable ID information, captured as status on read-only GPR in functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1357 / 5251


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
DCF_SDID15 
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
DCF_SDID15 
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
DCF_SDID15
DCF Client SDID 15 Configuration
38.2.27 Read-Only GPR On Functional Reset 19 (DCMROF19)
Offset
Register
Offset
DCMROF19
348h
Function
Contains information related to:
• FCCU EOUT status.
• Flash memory scanning status.
• Lockstep enable.
This register resets after functional reset 19.
 
The reset value is undefined on reset and is loaded from the flash memory contents at the end of the 
reset sequence.
  NOTE  
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1358 / 5251


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
FCCU
_EO...
DCM_
DONE 
LOCK
STE...
Reserved 
W
Reset
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
W
Reset
0
0
0
0
0
0
0
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
FCCU_EOUT_
DEDICATED
FCCU EOUT Status
Specifies the status of FCCU_EOUT pins on GPIO_2 and GPIO_3 as configured in the DCF record, 
UTEST_MISC[FCCU_EOUT_DEDICATED]. See the DCF clients file attached to this document for more 
information.
 
If the pads are dedicated to FCCU error output, these must not be programmed as input.
  NOTE  
0b - General purpose, supporting all functions
1b - Dedicated EOUT pins
30
DCM_DONE
Flash Memory Scanning Status
Specifies the status of flash memory scanning by DCM.
0b - Incomplete
1b - Complete
29
LOCKSTEP_EN
Lockstep Enable
Specifies the current chip operation mode as configured in the DCF record, 
UTEST_MISC[LOCKSTEP_EN]. See the DCF clients file attached to this document for more information.
0b - Decoupled operation of Cortex-M7_0 and Cortex-M7_1
1b - Lockstep operation of Cortex-M7_0 and Cortex-M7_1
28-0
—
Reserved
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1359 / 5251


---
# 페이지 108

38.2.28 Read-Only GPR On Functional Reset 20 (DCMROF20)
Offset
Register
Offset
DCMROF20
34Ch
Function
Specifies the information of chip destructive reset escalation support for destructive reset sources as configured in the DCF 
record, DEST_RST_ESC[13:0]. See the DCF clients file attached to this document for the mapping of corresponding destructive 
reset events.
This register resets after functional reset 20.
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
DCF_DEST_RST_ESC 
Reserv
ed 
Reserv
ed 
W
Reset
u1
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
Reserved 
AIPS_I
A...
QSPI_I
A...
Reserv
ed 
DMA_
AXB...
Reserv
ed 
Reserv
ed 
POR_
WDG..
.
W
Reset
0
0
0
0
0
0
0
0
0
u2
u1
0
u2
0
0
u1
1. The reset value of this register is dependent on the DCF client's default value.
2. The reset value of this register is dependent on DCF client default value.
Fields
Field
Function
31-18
DCF_DEST_RS
T_ESC
DCF Destructive Reset Escalation
Enables the destructive reset escalation feature for the corresponding destructive reset event.
00_0000_0000_0000b - Disables
00_0000_0000_0001b - Enables
17
—
Reserved
16
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1360 / 5251


---
# 페이지 109

Table continued from the previous page...
Field
Function
15-12
—
Reserved
11-7
—
Reserved
6
AIPS_IAHB_BY
P
Status of AIPS1/2 IAHB gasket as configured in DCF record, UTEST_MISC[AIPS_IAHB_BYP].
0b - Register wall enabled.
1b - Register wall bypassed.
5
QSPI_IAHB_BY
P
QuadSPI IAHB Bypass Status
Specifies the status of the QuadSPI IAHB gasket as configured in the DCF record, 
UTEST_MISC[QSPI_IAHB_BYP]. See the DCF clients file attached to this document for more 
information.
0b - Register wall enabled
1b - Register wall bypassed
4
—
Reserved
3
DMA_AXBS_IA
HB_BYP
Status of DMA AXBS IAHB gasket as configured in DCF record, UTEST_MISC[DMA_AXBS_IAHB_BYP].
0b - Register wall enabled.
1b - Register wall bypassed.
2
—
Reserved
1
—
Reserved
0
POR_WDG_EN
POR Watchdog (POR_WDG) Status
Specifies the status of POR_WDG as configured in the DCF record, UTEST_MISC[POR_WDG_EN]. 
The POR_WDG is enabled by default. See the DCF clients file attached to this document for more 
information.
0b - Disabled
1b - Enabled
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1361 / 5251


---
# 페이지 110

38.2.29 Read-Only GPR On Functional Reset 21 (DCMROF21)
Offset
Register
Offset
DCMROF21
350h
Function
Specifies the information of chip destructive reset escalation support for destructive reset sources as configured in the DCF 
record, DEST_RST_ESC[31:14].
This register resets after functional reset 21.
See the DCF clients file attached to this document for the mapping of corresponding destructive reset events.
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
HSE_CLK_MOD
E_OP...
Reserv
ed 
DCF_DEST_RS
T_ESC 
W
Reset
0
0
0
0
0
0
0
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
DCF_DEST_RST_ESC 
W
Reset
0
0
0
0
0
0
0
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
31-21
—
Reserved
20-19
HSE_CLK_MO
DE_OPTION
HSE_B Clock Mode Option
Specifies the applicable clocking options.
• If the value of this field is 0b, the ratio of 1:2 between the HSE_B IPS interface clock 
(AIPS_SLOW_CLK), HSE_B module clock (HSE_CLK), and HSE_IAHB gasket is enabled.
• If the value of this field is 1b, the ratio of 1:2 between the HSE_B IPS interface clock 
(AIPS_SLOW_CLK), HSE_B module clock (HSE_CLK), and HSE_IAHB gasket is bypassed.
• If the value of this field is 10b or 11b, the ratio of 1:4 between the HSE_B IPS interface clock 
(AIPS_SLOW_CLK), HSE_B module clock (HSE_CLK), and HSE_IAHB gasket is enabled.
00b - Option A
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1362 / 5251


---
# 페이지 111

Table continued from the previous page...
Field
Function
01b - Options C, D, E, E2, and F
10b - Option B
11b - Option B
18
—
Reserved
17-0
DCF_DEST_RS
T_ESC
DCF Destructive Reset Escalation
Enables the destructive reset escalation feature for the corresponding destructive reset event.
00_0000_0000_0000_0000b - Disables
00_0000_0000_0000_0001b - Enables
38.2.30 Read Write GPR On POR 1 (DCMRWP1)
Offset
Register
Offset
DCMRWP1
400h
Function
Contains information related to:
• Voltage dividers.
• Supply voltage monitoring.
• Ethernet modes.
• Software NCFs.
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
SBAF_
RE...
SBAF_
RE...
Reserv
ed 
SYS_REC_COUNTER 
W
Reset
0
0
0
0
0
0
0
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
Reserv
ed 
DEST_RESET_COUNT 
POR_WDOG_T
RIM 
STAN
BDY...
Reserv
ed 
Reserv
ed 
Reserved 
CLKO
UT_...
Reserved 
Reserv
ed 
W
Reset
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
0
0
0
0
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1363 / 5251


---
# 페이지 112

Fields
Field
Function
31-24
—
Reserved
23
SBAF_REC_DI
S_DRST
Disable Recovery Mode On Destructive Reset
This bit is reset by default and Secure BAF allows recovery mode sequence if Application issues > 
8 destructive reset. Application can set this bit to disable recovery mode when Application issues > 8 
destructive reset.
0 - Recovery mode is enabled on greater than 8 destructive resets.
1 - Recovery mode is disabled on greater than 8 destructive resets.
22
SBAF_REC_DI
S_FRST
Disable Recovery Mode On Functional Reset
This bit is reset by default and Secure BAF allows recovery mode sequence if Application issues > 
8 functional reset. Application can set this bit to disable recovery mode when Application issues > 8 
functional reset.
0 - Recovery mode is enabled on greater than 8 functional resets.
1 - Recovery mode is disabled on greater than 8 functional resets.
21
—
Reserved
20-16
SYS_REC_CO
UNTER
System Recovery Counter
System recovery counter stored by sBAF and HSE FW
15
—
Reserved
14-11
DEST_RESET_
COUNT
Destructive Reset Counts
This bit is used by sBAF internally to preserve destructive reset counts.
10-9
POR_WDOG_T
RIM
POR_WDG Trim
Specifies the trims for the POR_WDG timeout value.
00b - POR_WDG timeout = 06.25 ms
01b - POR_WDG timeout = 12.50 ms
10b - POR_WDG timeout = 25.00 ms
11b - POR_WDG timeout = 50.00 ms
8
STANBDY_PW
DOG_DIS
Standby POR_WDG Disable
Disables the standby entry and exit monitoring window of POR_WDG.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1364 / 5251


---
# 페이지 113

Table continued from the previous page...
Field
Function
0b - Enables
1b - Disables
7
—
Reserved
6
—
Reserved
5-4
—
Reserved
3
CLKOUT_STAN
DBY
Clockout Standby Expose Over Functional And Destructive Reset
Specifies whether the CLKOUT_STANDBY function is available during functional or destructive reset 
on PTA12.
0b - No
1b - Yes
2-1
—
Reserved
0
—
Reserved
38.2.31 Read Write GPR On POR 3 (DCMRWP3)
Offset
Register
Offset
DCMRWP3
408h
Function
Resets after POR 3.
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1365 / 5251


---
# 페이지 114

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
Reserv
ed 
W
Reset
0
0
0
0
0
0
0
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
DEST_
RS...
Reserved 
W
Reset
0
0
0
0
0
0
0
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
31-17
—
Reserved
16
—
Reserved
15-10
—
Reserved
9
DEST_RST9_A
S_IPI
Destructive Reset 9
Configures a destructive reset to interrupt.
0b - Destructive reset
1b - PLL LOL interrupt
8-0
—
Reserved
38.2.32 Read Write GPR On Destructive Reset 2 (DCMRWD2)
Offset
Register
Offset
DCMRWD2
504h
Function
Controls the EOUT state during self-test.
This register resets after destructive reset 2.
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1366 / 5251


---
# 페이지 115

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
Reset
0
0
0
0
0
0
0
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
EOUT
_ST...
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
W
Reset
0
0
0
0
0
0
0
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
7
EOUT_STAT_D
UR_STEST
Controls the EOUT state during self-test
If this field = 0, the EOUT state changes to high impedance post self-test when the 
chip is under reset, and if this field = 1, the EOUT state remains in Fault state until 
this field becomes 0. DCMROF19[FCCU_EOUT_DEDICATED] is required for the feature. 
DCMROF19[FCCU_EOUT_DEDICATED] = 1 when you are using this feature.
0b - High impedance
1b - Fault state
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
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1367 / 5251


---
# 페이지 116

38.2.33 Read Write GPR On Destructive Reset 3 (DCMRWD3)
Offset
Register
Offset
DCMRWD3
508h
Function
Includes fault disable fields and resets after destructive reset.
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
Reserv
ed 
CM7_0
_I...
Reserv
ed 
CM7_0
_D...
Reserv
ed 
CM7_0
_D...
PRAM
0_E...
PRAM
1_E...
PRAM
2_E...
LC_ER
R_...
Reserved 
PERIP
H_...
MAC_
GSK...
TCM_
AXB...
DATA_
ED...
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
_ED...
AIPS2
_G...
AIPS1
_G...
QSPI_
GS...
HSE_
GSK...
Reserv
ed 
DMA_
AXB...
SYS_A
XB...
DMA_
PER...
DMA_
SYS...
TCM_
GSK...
CM7_
RCC...
CM7_
RCC...
Reserv
ed 
Reserv
ed 
CM7_0
_L...
W
Reset
1
1
1
1
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
Fields
Field
Function
31
—
Reserved
30
CM7_0_ICDAT
A_ECC_ERR_E
N
Cortex-M7_0 I-cache ECC Error Enable
Specifies whether the Cortex-M7_0 core's I-cache data memory detected a multi-bit ECC error.
The field enables fault monitoring at FCCU NCF 2 if there is a multi-bit ECC error from the Cortex-M7_0 
core's I-cache data memory.
0b - No
1b - Yes
29
—
Reserved
28
CM7_0_DCTAG
_ECC_ERR_EN
Cortex-M7_0 D-cache Tag ECC Error Enable
Specifies whether the Cortex-M7_0 core's D-cache tag memory detected a multi-bit ECC error.
The field enables fault monitoring at FCCU NCF 2 if there is a multi-bit ECC error from the Cortex-M7_0 
core's D-cache tag memory.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1368 / 5251


---
# 페이지 117

Table continued from the previous page...
Field
Function
0b - No
1b - Yes
27
—
Reserved
26
CM7_0_DCDAT
A_ECC_ERR_E
N
Cortex-M7_0 D-cache Data ECC Error Enable
Specifies whether the Cortex-M7_0 core's D-cache data memory detected a multi-bit ECC error.
The field enables fault monitoring at FCCU NCF 2 if there is a multi-bit ECC error from the Cortex-M7_0 
core's D-cache data memory.
0b - No
1b - Yes
25
PRAM0_ECC_E
RR_EN
PRAM0 ECC Error Enable
Specifies whether a multi-bit ECC error occurred from PRAM0.
The field enables fault monitoring at FCCU NCF 2 if there is a multi-bit ECC error from PRAM0.
0b - No
1b - Yes
24
PRAM1_ECC_E
RR_EN
PRAM1 ECC Error Enable
Specifies whether a multi-bit ECC error occurred from PRAM1.
The field enables fault monitoring at FCCU NCF 2 if there is a multi-bit ECC error from PRAM1.
0b - No
1b - Yes
23
PRAM2_ECC_E
RR_EN
Enable bit for enabling the fault monitoring at FCCU NCF 2 for the fault: Multi bit ECC error from SRAM1.
0b - No multi-bit ECC error.
1b - Multi-bit ECC error.
22
LC_ERR_EN
Life Cycle Scanning Error Enable
Specifies whether an error is encountered during life-cycle scanning.
The field enables fault monitoring at FCCU NCF 3 if there is an error in life-cycle scanning.
 
On any POR or destructive reset event, because this field becomes 0, the field has no effect. 
A life-cycle error (in case it is present) is not disabled.
  NOTE  
0b - No
1b - Yes
21-20
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1369 / 5251


---
# 페이지 118

Table continued from the previous page...
Field
Function
—
19
PERIPH_AXBS
_ALARM_EN
Peripheral AXBS Alarm Enable
Specifies whether peripheral AXBS_Lite reported a safety alarm.
The field enables fault monitoring at FCCU NCF 1 in case of a peripheral AXBS_Lite safety alarm.
0b - No
1b - Yes
18
MAC_GSKT_AL
ARM_EN
MAC Gasket Alarm Enable
Specifies whether the MAC IAHB gasket reported an alarm.
The field enables fault monitoring at FCCU NCF 1 in case of an MAC IAHB gasket alarm.
0b - No
1b - Yes
17
TCM_AXBS_AL
ARM_EN
TCM AXBS Alarm Enable
Specifies whether the TCM AHB splitter reported a safety alarm.
The field enables fault monitoring at FCCU NCF 1 in case of a TCM AHB splitter safety alarm.
0b - No
1b - Yes
16
DATA_EDC_ER
R_EN
Data EDC Error Enable
Specifies whether a data EDC error occurred.
The field enables fault monitoring at FCCU NCF 1, in case of an integrity error on data, for safety.
0b - No
1b - Yes
15
ADDR_EDC_E
RR_EN
Address EDC Error Enable
Specifies whether an address integrity (EDC) error occurred.
The field enables fault monitoring at FCCU NCF 1, in case of an integrity error on address, for safety.
0b - No
1b - Yes
14
AIPS2_GSKT_A
LARM_EN
Enable bit for enabling the fault monitoring at FCCU NCF 1 for the fault: AIPS2 IAHB gasket alarm.
0b - No alarm indicated by AIPS2 IAHB gasket.
1b - Alarm indicated by AIPS2 IAHB gasket.
13
AIPS1_GSKT_A
LARM_EN
Enable bit for enabling the fault monitoring at FCCU NCF 1 for the fault: AIPS1 IAHB gasket alarm.
0b - No alarm indicated by AIPS1 IAHB gasket.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1370 / 5251


---
# 페이지 119

Table continued from the previous page...
Field
Function
1b - Alarm indicated by AIPS1 IAHB gasket.
12
QSPI_GSKT_A
LARM_EN
QuadSPI Gasket Alarm Enable
Specifies whether the QuadSPI IAHB gasket reported an alarm.
The field enables fault monitoring at FCCU NCF 1 in case of QuadSPI IAHB gasket alarm.
0b - No
1b - Yes
11
HSE_GSKT_AL
ARM_EN
HSE_B Gasket Alarm Enable
Specifies whether the HSE_B IAHB gasket reported an alarm.
The field enables fault monitoring at FCCU NCF 1 in case of HSE_B IAHB gasket alarm.
0b - No
1b - Yes
10
—
Reserved
9
DMA_AXBS_AL
ARM_EN
DMA AXBS Alarm Enable
Specifies whether eDMA AXBS_Lite reported a safety alarm.
The field enables fault monitoring at FCCU NCF 1 in case of an eDMA AXBS_Lite safety alarm.
0b - No
1b - Yes
8
SYS_AXBS_AL
ARM_EN
System AXBS Alarm Enable
Specifies whether the system AXBS reported a safety alarm.
The field enables fault monitoring at FCCU NCF 1 in case of a system AXBS safety alarm.
0b - No
1b - Yes
7
DMA_PERIPH_
GSKT_ALARM_
EN
TCM Gasket Alarm Enable
Specifies whether the eDMA-peripheral AXBS IAHB gasket reported a safety alarm.
The field enables fault monitoring at FCCU NCF 1 in case of IAHB gasket safety alarm from the eDMA 
peripheral AXBS IAHB gasket.
0b - No
1b - Yes
6
DMA_SYS_GS
KT_ALARM_EN
DMA System Gasket Alarm Enable
Specifies whether the eDMA-system AXBS IAHB gasket reported a safety alarm.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1371 / 5251


---
# 페이지 120

Table continued from the previous page...
Field
Function
The field enables fault monitoring at FCCU NCF 1 in case of IAHB gasket safety alarm from the 
eDMA-system AXBS IAHB gasket.
0b - No
1b - Yes
5
TCM_GSKT_AL
ARM_EN
TCM Gasket Alarm Enable
Specifies whether the TCM IAHB gasket reported an alarm. If this field = 1, the gasket reports a 
monitor alarm.
The field enables fault monitoring at FCCU NCF 1 in case of TCM IAHB gasket monitor alarm.
0b - No
1b - Yes
4
CM7_RCCU2_A
LARM_EN
Cortex-M7 RCCU2 Alarm Enable
Specifies whether a redundant RCCU reported a lockstep alarm.
The field enables fault monitoring at FCCU NCF 0 in case of the Cortex-M7 core redundant lockstep.
0b - No
1b - Yes
3
CM7_RCCU1_A
LARM_EN
Cortex-M7 RCCU1 Alarm Enable
Specifies whether RCCU reported a lockstep alarm.
The field enables fault monitoring at FCCU NCF 0 in case of the Cortex-M7 core lockstep.
0b - No
1b - Yes
2
—
Reserved
1
—
Reserved
0
CM7_0_LOCKU
P_EN
Cortex-M7 Lockup Enable
Specifies whether the Cortex-M7_0 core is in the Lockup state.
The field enables fault monitoring at FCCU NCF 0 in case of the Cortex-M7_0 core lockup.
0b - No
1b - Yes
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1372 / 5251


---
# 페이지 121

38.2.34 Read Write GPR On Destructive Reset 4 (DCMRWD4)
Offset
Register
Offset
DCMRWD4
50Ch
Function
Contains information related to:
• Test activation errors.
• Fault monitoring.
• DCM flash memory scanning.
• ECC errors.
This register resets after destructive reset 4.
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
CM7_2
_L...
TEST_
AC...
TEST_
AC...
Reserv
ed 
VDD2
P5_...
VDD1
P1_...
Reserv
ed 
FLAS
H_A...
PRAM
2_F...
FLAS
H_S...
FLAS
H_R...
FLAS
H_R...
FLAS
H_A...
FLAS
H_E...
Reserv
ed 
Reserv
ed 
W
Reset
1
1
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
PF1_D
AT...
PF1_C
OD...
PF0_D
AT...
PF0_C
OD...
Reserv
ed 
PRAM
1_F...
PRAM
0_F...
DMA_
TCD...
CM7_1
_D...
CM7_1
_D...
CM7_1
_I...
CM7_0
_D...
CM7_0
_D...
CM7_0
_I...
Reserv
ed 
CM7_0
_I...
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
31
CM7_2_LOCKU
P_EN
Enable bit for enabling the fault monitoring at FCCU NCF 0 for the fault: CM7_2 core lockup.
0b - CM7_2 core not in lockup state.
1b - CM7_2 core in lockup state.
30
TEST_ACTIVA
TION_1_ERR_E
N
Test Activation 1 Error Enable
Specifies whether a partial test is activated accidentally.
The field enables fault monitoring at FCCU NCF 5 in case of an accidental partial test activation 1.
0b - No
1b - Yes
29
Test Activation 0 Error Enable
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1373 / 5251


---
# 페이지 122

Table continued from the previous page...
Field
Function
TEST_ACTIVA
TION_0_ERR_E
N
Specifies whether a partial test is activated accidentally.
The field enables fault monitoring at FCCU NCF 5 in case of an accidental partial test activation 0.
0b - No
1b - Yes
28
—
Reserved
27
VDD2P5_GNG_
ERR_EN
VDD2P5 Go/No-go Error Enable
Specifies whether the VDD2P5 (double bond) supply is clean.
The field enables fault monitoring at FCCU NCF 4 if there is a "go/no-go" indicator for VDD_HV_FLA (double 
bond) going to FXOSC and PLL. If the value of this field = 0, there is a "go" indication that the supply if clean; 
if it = 1, there is a "no-go" indication that the supply is unclean and there is a fault in double-bond connection 
or its routing within the chip.
0b - Clean
1b - Unclean
26
VDD1P1_GNG_
ERR_EN
VDD1PD1 Go/No-go Error Enable
Specifies whether the VDD1PD1 (double bond) supply is clean.
The field enables fault monitoring at FCCU NCF 4 if there is a "go/no-go" indicator for VDD1PD1 (double 
bond) supply going to PLL. If the value of this field = 0, there is a "go" indication that the supply if clean; if 
it = 1, there is a "no-go" indication that the supply is unclean and there is a fault in double-bond connection 
or its routing within the chip.
0b - Clean
1b - Unclean
25
—
Reserved
24
FLASH_ACCES
S_ERR_EN
Flash Memory Access Error Enable
Specifies whether a transaction monitor mismatch error occurred from the flash memory controller.
The field enables fault monitoring at FCCU NCF 3 in case of a transaction monitor mismatch error from the 
flash memory controller. The alarm indicates that the flash memory controller detected a transaction monitor 
mismatch when compared to the flash memory safety feedback output. The flash memory specifies where 
the reconstructed address is compared with the address that invoked the flash memory access.
0b - No
1b - Yes
23
PRAM2_FCCU_
ALARM_EN
Enable bit for enabling the fault monitoring at FCCU NCF 2 for the fault: PRAM2 safety alarm. This alarm 
is set on faulty SRAM1 read or read-modify error.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1374 / 5251


---
# 페이지 123

Table continued from the previous page...
Field
Function
0b - No safety alarm indicated by PRAM2.
1b - Safety alarm indicated by PRAM2.
22
FLASH_SCAN_
ERR_EN
Flash Memory Scanning Error Enable
Specifies whether an error occurred during DCM flash memory scanning.
The field enables fault monitoring at FCCU NCF 3 in case of an error during the DCM flash memory scanning 
process because of invalid data.
 
On a POR or destructive reset event, because this field becomes 0, the field has no effect. 
A life-cycle error (in case it is present) is not disabled.
  NOTE  
0b - No
1b - Yes
21
FLASH_RST_E
RR_EN
Flash Memory Reset Error Enable
Specifies whether a flash memory reset error occurred.
The field enables fault monitoring at FCCU NCF 3 in case of a flash memory reset error. This error indication 
is set when the flash memory encounters errors during its reset reads.
0b - No
1b - Yes
20
FLASH_REF_E
RR_EN
Flash Memory Reference Error Encode
Specifies whether a reference current loss or read voltage error occurred during previous read(s).
The field enables fault monitoring at FCCU NCF 3 if there is a flash memory reference current loss or read 
voltage error during previous read(s).
0b - No
1b - Yes
19
FLASH_ADDR_
ENC_ERR_EN
Flash Memory Address Encode Error Enable
Specifies whether an address encode error occurred in the flash memory.
The field enables fault monitoring at FCCU NCF 3 if there is a flash memory address encode error. During 
address decoding, if multiple or no address line is selected, FMU reports an address encode error.
0b - No
1b - Yes
18
FLASH_EDC_E
RR_EN
Flash Memory EDC Error Enable
Specifies whether EDC after ECC error is reported in the flash memory.
The field enables fault monitoring at FCCU NCF 3 in case of a flash memory ECC correction error via EDC, 
reported by FMU.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1375 / 5251


---
# 페이지 124

Table continued from the previous page...
Field
Function
0b - No
1b - Yes
17
—
Reserved
16
—
Reserved
15
PF1_DATA_EC
C_ERR_EN
PF1 Data ECC Error Enable
Specifies whether FMU reported an uncorrectable error in the flash memory controller port 1 data memory.
The field enables fault monitoring at FCCU NCF 3 in case of Flash1 data ECC uncorrectable error.
0b - No
1b - Yes
14
PF1_CODE_EC
C_ERR_EN
PF1 Code ECC Error Enable
Specifies whether FMU reported an uncorrectable error in the flash memory controller port 1 code memory.
The field enables fault monitoring at FCCU NCF 3 in case of Flash1 code ECC uncorrectable error.
0b - No
1b - Yes
13
PF0_DATA_EC
C_ERR_EN
PF0 Data ECC Error Enable
Specifies whether FMU reported an uncorrectable error in the flash memory controller port 0 data memory.
The field enables fault monitoring at FCCU NCF 3 in case of Flash0 data ECC uncorrectable error.
0b - No
1b - Yes
12
PF0_CODE_EC
C_ERR_EN
PF0 Code ECC Error Enable
Specifies whether FMU reported an uncorrectable error in the flash memory controller port 0 code memory.
The field enables fault monitoring at FCCU NCF 3 in case of Flash0 code ECC uncorrectable error.
0b - No
1b - Yes
11
—
Reserved
10
PRAM1_FCCU_
ALARM_EN
PRAM1 FCCU Alarm Enable
Specifies whether PRAM1 reported a safety alarm.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1376 / 5251


---
# 페이지 125

Table continued from the previous page...
Field
Function
The field enables fault monitoring at FCCU NCF 2 in case of PRAM1 safety alarm. This alarm is set on faulty 
SRAM1 read or read-modify error.
0b - No
1b - Yes
9
PRAM0_FCCU_
ALARM_EN
PRAM0 FCCU Alarm Enable
Specifies whether PRAM0 reported a safety alarm.
The field enables fault monitoring at FCCU NCF 2 in case of PRAM0 safety alarm. This alarm is set to faulty 
SRAM0 read or read-modify error.
0b - No
1b - Yes
8
DMA_TCD_RA
M_ECC_ERR_E
N
eDMA TCD RAM ECC Error Enable
Specifies whether uncorrectable ECC error detection is enabled at FCCU.
The field enables fault monitoring at FCCU NCF 2 in case of an uncorrectable ECC error reported from the 
eDMA_TCD memory. This uncorrectable ECC error consists of a multi-bit data ECC error and an address 
ECC error.
0b - No
1b - Yes
7
CM7_1_DTCM1
_ECC_ERR_EN
Cortex-M7_1 DTCM 1 ECC Error Enable
Specifies whether uncorrectable ECC error detection is enabled at FCCU.
The field enables fault monitoring at FCCU NCF 2 in case of an uncorrectable ECC error from the 
Cortex-M7_1 core's DTCM block 1. This uncorrectable ECC error consists of a multi-bit data ECC error and 
an address ECC error.
The Cortex-M7_1 core's DTCM 1 consists of two physical blocks.
 
The Cortex-M7_1 core's DTCM 1 does not support address ECC errors in S32K324, 
S32K344, and S32K314.
  NOTE  
0b - No
1b - Yes
6
CM7_1_DTCM0
_ECC_ERR_EN
Cortex-M7_1 DTCM 0 ECC Error Enable
Specifies whether uncorrectable ECC error detection is enabled at FCCU. This uncorrectable ECC error 
consists of a multi-bit data ECC error and an address ECC error. The Cortex-M7_1 core's DTCM consists 
of two physical blocks.
This field enables fault monitoring at FCCU NCF 2 in case of an uncorrectable ECC error from the 
Cortex-M7_1 core's DTCM block 0.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1377 / 5251


---
# 페이지 126

Table continued from the previous page...
Field
Function
 
The Cortex-M7_1 core's DTCM 0 does not support address ECC errors in S32K324, 
S32K344, and S32K314.
  NOTE  
0b - No
1b - Yes
5
CM7_1_ITCM_
ECC_ERR_EN
Cortex-M7_1 ITCM ECC Error Enable
Specifies whether uncorrectable ECC error detection is enabled at FCCU.
The field enables fault monitoring at FCCU NCF 2 in case of an uncorrectable ECC error from the 
Cortex-M7_1 core's ITCM. This uncorrectable ECC error consists of a multi-bit data ECC error and an 
address ECC error.
 
The Cortex-M7_1 core's ITCM does not support address ECC errors in S32K324, S32K344, 
and S32K314.
  NOTE  
0b - No
1b - Yes
4
CM7_0_DTCM1
_ECC_ERR_EN
Cortex-M7_0 DTCM 1 ECC Error Enable
Specifies whether uncorrectable ECC error detection is enabled at FCCU.
The field enables fault monitoring at FCCU NCF 2 in case of an uncorrectable ECC error from the 
Cortex-M7_0 core's DTCM block 1. This uncorrectable ECC error consists of a multi-bit data ECC error and 
an address ECC error. The Cortex-M7_0 core's DTCM consists of two physical blocks.
 
The Cortex-M7_0 core's DTCM 1 does not support address ECC errors in S32K324, 
S32K344, and S32K314.
  NOTE  
0b - No
1b - Yes
3
CM7_0_DTCM0
_ECC_ERR_EN
Cortex-M7_0 DTCM 0 ECC Error Enable
Specifies whether uncorrectable ECC error detection is enabled at FCCU.
The field enables fault monitoring at FCCU NCF 2 in case of an uncorrectable ECC error from the 
Cortex-M7_0 core's DTCM block 0. This uncorrectable ECC error consists of a multi-bit data ECC error and 
an address ECC error. The Cortex-M7_0 core's DTCM consists of two physical blocks.
 
The Cortex-M7_0 core's DTCM 0 does not support address ECC errors in S32K324, 
S32K344, and S32K314.
  NOTE  
0b - No
1b - Yes
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1378 / 5251


---
# 페이지 127

Table continued from the previous page...
Field
Function
2
CM7_0_ITCM_
ECC_ERR_EN
Cortex-M7 ITCM ECC Error Enable
Specifies whether uncorrectable ECC error detection is enabled at FCCU.
The field enables fault monitoring at FCCU NCF 2 in case of an uncorrectable ECC error from the 
Cortex-M7_0 core's ITCM. This uncorrectable ECC error consists of a multi-bit data ECC error and an 
address ECC error.
 
The Cortex-M7_0 core's ITCM does not support address ECC errors in S32K324, S32K344, 
and S32K314.
  NOTE  
0b - No
1b - Yes
1
—
Reserved
0
CM7_0_ICTAG_
ECC_ERR_EN
Cortex-M7_0 I-cache Tag ECC Error Enable
Specifies whether the Cortex-M7_0 core's I-cache tag memory detected a multi-bit ECC error.
The field enables fault monitoring at FCCU NCF 2 if there is a multi-bit ECC error from the Cortex-M7_0 
core's I-cache tag memory.
0b - No
1b - Yes
38.2.35 Read Write GPR On Destructive Reset 5 (DCMRWD5)
Offset
Register
Offset
DCMRWD5
510h
Function
Contains information related to:
• Uncorrectable ECC error detection.
• I-cache and D-cache ECC errors.
• Fault monitoring.
This register resets after destructive reset 5.
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1379 / 5251


---
# 페이지 128

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
CM7_2
_D...
CM7_2
_D...
CM7_2
_I...
CM7_2
_I...
CM7_2
_I...
CM7_2
_D...
CM7_2
_D...
CM7_2
_A...
CM7_2
_A...
Reserv
ed 
CM7_0
_A...
CM7_0
_A...
Reserv
ed 
Reserv
ed 
DMA_
RDA...
Reserv
ed 
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
MAC_
RDA...
Reserv
ed 
DEBU
G_A...
MCT_
BUS...
STCU
_BI...
MBIST
_A...
STCU
_NC...
SW_N
CF_...
SW_N
CF_...
SW_N
CF_...
SW_N
CF_...
INTM_
3_...
INTM_
2_...
INTM_
1_...
INTM_
0_...
Reserv
ed 
W
Reset
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
1
1
1
1
Fields
Field
Function
31
CM7_2_DTCM1
_ECC_ERR_EN
Cortex-M7_2 DTCM 1 ECC Error Enable
Specifies whether uncorrectable ECC error detection is enabled at FCCU from the Cortex-M7_2 core's 
DTCM block 1.
The field enables fault monitoring at FCCU NCF 2 in case of an uncorrectable ECC error from the 
Cortex-M7_2 core's DTCM block 1. This uncorrectable ECC error consists of a multi-bit data ECC error and 
an address ECC error. The Cortex-M7_2 core's DTCM consists of two physical blocks.
 
The Cortex-M7_2 core's DTCM 1 does not support address ECC errors in S32K324, 
S32K344, and S32K314.
  NOTE  
0b - No
1b - Yes
30
CM7_2_DTCM0
_ECC_ERR_EN
Cortex-M7_2 DTCM 0 ECC Error Enable
Specifies whether uncorrectable ECC error detection is enabled at FCCU from the Cortex-M7_2 core's 
DTCM block 0.
The field enables fault monitoring at FCCU NCF 2 in case of an uncorrectable ECC error from the 
Cortex-M7_2 core's DTCM block 0. This uncorrectable ECC error consists of a multi-bit data ECC error and 
an address ECC error. The Cortex-M7_2 core's DTCM consists of two physical blocks.
 
The Cortex-M7_2 core's DTCM 0 does not support address ECC errors in S32K324, 
S32K344, and S32K314.
  NOTE  
0b - No
1b - Yes
29
CM7_2_ITCM_
ECC_ERR_EN
Cortex-M7_2 ITCM ECC Error Enable
Specifies whether uncorrectable ECC error detection is enabled at FCCU from the Cortex-M7_2 
core's ITCM.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1380 / 5251


---
# 페이지 129

Table continued from the previous page...
Field
Function
The field enables fault monitoring at FCCU NCF 2 in case of an uncorrectable ECC error from the 
Cortex-M7_2 core's ITCM. This uncorrectable ECC error consists of a multi-bit data ECC error and an 
address ECC error.
 
The Cortex-M7_2 core's ITCM does not support address ECC errors in S32K324, S32K344, 
and S32K314.
  NOTE  
0b - No
1b - Yes
28
CM7_2_ICTAG_
ECC_ERR_EN
Cortex-M7_2 I-cache Tag ECC Error Enable
Specifies whether the Cortex-M7_2 core's I-cache tag memory detected a multi-bit error.
The field enables fault monitoring at FCCU NCF 2 if there is a multi-bit ECC error from the Cortex-M7_2 
core's I-cache tag memory.
0b - No
1b - Yes
27
CM7_2_ICDAT
A_ECC_ERR_E
N
Cortex-M7_2 I-cache Data ECC Error Enable
Specifies whether the Cortex-M7_2 core's I-cache data memory detected a multi-bit ECC error.
The field enables fault monitoring at FCCU NCF 2 if there is a multi-bit ECC error from the Cortex-M7_2 
core's I-cache data memory.
0b - No
1b - Yes
26
CM7_2_DCTAG
_ECC_ERR_EN
Cortex-M7_2 D-cache Tag ECC Error Enable
Specifies whether the Cortex-M7_2 core's D-cache tag memory detected a multi-bit ECC error.
The field enables fault monitoring at FCCU NCF 2 if there is a multi-bit ECC error from the Cortex-M7_2 
core's D-cache tag memory.
0b - No
1b - Yes
25
CM7_2_DCDAT
A_ECC_ERR_E
N
Cortex-M7_2 D-cache Data ECC Error Enable
Specifies whether the Cortex-M7_2 core's D-cache data memory detected a multi-bit ECC error.
The field enables fault monitoring at FCCU NCF 2 if there is a multi-bit ECC error from the Cortex-M7_2 
core's D-cache data memory.
0b - No
1b - Yes
24
Cortex-M7_2 AHBM Read Data EDC Error Enable
Specifies whether an integrity error is reported on the Cortex-M7_2 core's main read data.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1381 / 5251


---
# 페이지 130

Table continued from the previous page...
Field
Function
CM7_2_AHBM_
RDATA_EDC_E
RR_EN
The field enables fault monitoring at FCCU NCF 1, if there is an integrity error on the Cortex-M7_2 core's 
main read data, for safety.
0b - No
1b - Yes
23
CM7_2_AHBP_
RDATA_EDC_E
RR_EN
Cortex-M7_2 AHBP Read Data EDC Error Enable
Specifies whether an integrity error is reported on the Cortex-M7_2 core's peripheral read data.
The field enables fault monitoring at FCCU NCF 1, if there is an integrity error on the Cortex-M7_2 core's 
peripheral read data, for safety.
0b - No
1b - Yes
22
—
Reserved
21
CM7_0_AHBM_
RDATA_EDC_E
RR_EN
Cortex-M7_0 AHBM Read Data EDC Error Enable
Specifies whether an integrity error is reported on the Cortex-M7_0 core's main read data.
The field enables fault monitoring at FCCU NCF 1, if there is an integrity error on the Cortex-M7_0 core's 
main read data, for safety.
0b - No
1b - Yes
20
CM7_0_AHBP_
RDATA_EDC_E
RR_EN
Cortex-M7_0 AHBP Read Data EDC Error Enable
Specifies whether an integrity error is reported on the Cortex-M7_0 core's peripheral read data.
The field enables fault monitoring at FCCU NCF 1, if there is an integrity error on the Cortex-M7_0 core's 
peripheral read data, for safety.
0b - No
1b - Yes
19
—
Reserved
18
—
Reserved
17
DMA_RDATA_
EDC_ERR_EN
eDMA Read Data EDC Error Enable
Specifies whether an integrity error is reported on the eDMA read data.
The field enables fault monitoring at FCCU NCF 1, if there is an integrity error on the eDMA read data, 
for safety.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1382 / 5251


---
# 페이지 131

Table continued from the previous page...
Field
Function
0b - No
1b - Yes
16
—
Reserved
15
MAC_RDATA_
EDC_ERR_EN
MAC Read Data EDC Error Enable
Specifies whether an integrity error is reported on the MAC read data.
The field enables fault monitoring at FCCU NCF 1, if there is an integrity error on the MAC read data, 
for safety.
0b - No
1b - Yes
14
—
Reserved
13
DEBUG_ACTIV
ATION_ERR_E
N
Debug Activation Error Enable
Specifies whether unintended debug is activated.
The field enables fault monitoring at FCCU NCF 5 for monitoring of unintended debug activation. The value 
of this field is 1 when the core is in the Halted state with application debug not enabled or debugger request 
not enabled.
 
While the debugger is connected, DEBUG_ACTIVATION_ERR_EN must be 0 to disable 
debug activation error monitoring because the debugger is intentionally connected to 
the chip.
  NOTE  
0b - No
1b - Yes
12
MCT_BUS_ER
R_EN
MCT Bus Error Enable
Enable bit for enabling the fault monitoring at FCCU NCF 5 for the fault: Fault reported due to illegal access 
on MBIST Master Controller (MCT). This fault is reported via a transfer error indication to the system.
0b - No transfer error indicated from MCT.
1b - Transfer error indicated from MCT.
11
STCU_BIST_U
SER_CF_EN
STCU2 BIST User CF Enable
Specifies whether LBIST or MBIST is enabled accidentally (a fault condition is detected in Run mode).
The field enables fault monitoring at FCCU NCF 5 if LBIST or MBIST is enabled accidentally.
0b - No
1b - Yes
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1383 / 5251


---
# 페이지 132

Table continued from the previous page...
Field
Function
10
MBIST_ACTIVA
TION_ERR_EN
MBIST Activation Error Enable
Specifies whether accidental backdoor is enabled on memories.
The field enables fault monitoring at FCCU NCF 5 in case of an accidental backdoor access on memories. 
This monitor needs to be disabled on FCCU when performing a fault injection.
0b - No
1b - Yes
9
STCU_NCF_EN
STCU2 NCF Enable
Enables fault monitoring at FCCU NCF 5 for STCU2 NCF, that is, BIST result error.
0b - Disables
1b - Enables
8
SW_NCF_3_EN
Software NCF 3 Enable
Enables fault monitoring at FCCU NCF 7 for software NCF3 ( DCMRWF1[FCCU_SW_NCF3] ).
0b - Disables
1b - Enables
7
SW_NCF_2_EN
Software NCF 2 Enable
Enables fault monitoring at FCCU NCF 7 for software NCF2 ( DCMRWF1[FCCU_SW_NCF2] ).
0b - Disables
1b - Enables
6
SW_NCF_1_EN
Software NCF 1 Enable
Enables fault monitoring at FCCU NCF 7 for software NCF1 ( DCMRWF1[FCCU_SW_NCF1]).
0b - Disables
1b - Enables
5
SW_NCF_0_EN
Software NCF 0 Enable
Enables fault monitoring at FCCU NCF 7 for software NCF0 ( DCMRWF1[FCCU_SW_NCF0] ).
0b - Disables
1b - Enables
4
INTM_3_ERR_
EN
INTM 3 Error Enable
Specifies whether interrupt monitor 3 reported an error.
The field enables fault monitoring at FCCU NCF 6 if INTM reports an interrupt monitor 3 error. This error 
is also reported in INTM.INTM_STATUS3. See the "Functional description" section in the INTM chapter 
for details.
0b - No
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1384 / 5251


---
# 페이지 133

Table continued from the previous page...
Field
Function
1b - Yes
3
INTM_2_ERR_
EN
INTM 2 Error Enable
Specifies whether interrupt monitor 2 reported an error.
The field enables fault monitoring at FCCU NCF 6 if INTM reports an interrupt monitor 2 error. This error 
is also reported in INTM.INTM_STATUS2. See the "Functional description" section in the INTM chapter 
for details.
0b - No
1b - Yes
2
INTM_1_ERR_
EN
INTM 1 Error Enable
Specifies whether interrupt monitor 1 reported an error.
The field enables fault monitoring at FCCU NCF 6 if INTM reports an interrupt monitor 1 error. This error 
is also reported in INTM.INTM_STATUS1. See the "Functional description" section in the INTM chapter 
for details.
0b - No
1b - Yes
1
INTM_0_ERR_
EN
INTM 0 Error Enable
Specifies whether interrupt monitor 0 reported an error.
The field enables fault monitoring at FCCU NCF 6 if INTM reports an interrupt monitor 0 error. This error 
is also reported in INTM.INTM_STATUS0. See the "Functional description" section in the INTM chapter 
for details.
0b - No
1b - Yes
0
—
Reserved
38.2.36 Read Write GPR On Destructive Reset 6 (DCMRWD6)
Offset
Register
Offset
DCMRWD6
514h
Function
Contains information related to module debug disable.
This register resets after destructive reset 6.
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1385 / 5251


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
SAI1_
DB...
SAI0_
DB...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEXI
O_...
LPI2C
1_...
LPI2C
0_...
LPSPI
5_...
LPSPI
4_...
LPSPI
3_...
LPSPI
2_...
LPSPI
1_...
W
Reset
0
0
0
0
0
0
0
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
LPSPI
0_...
PIT2_
DB...
PIT1_
DB...
PIT0_
DB...
STM1_
DB...
STM0_
DB...
Reserv
ed 
SWT0
_DB...
RTC_
DBG...
EMIO
S2_...
EMIO
S1_...
EMIO
S0_...
LCU1_
DB...
LCU0_
DB...
FCCU
_DB...
EDMA
_DB...
W
Reset
0
0
0
0
0
0
0
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
SAI1_DBG_DIS
_CM7_0
SAI1 debug disable bit for CM7_0. Set this bit 1 to disable the debug of IP.
0b - SAI1 enters debug mode when CM7_0 enters debug mode.
1b - SAI1 remains functional and is not impacted when CM7_0 enters debug mode.
30
SAI0_DBG_DIS
_CM7_0
SAI0 debug disable bit for CM7_0. Set this bit 1 to disable the debug of IP.
0b - SAI0 enters debug mode when CM7_0 enters debug mode.
1b - SAI0 remains functional and is not impacted when CM7_0 enters debug mode.
29
FLEXCAN5_DB
G_DIS_CM7_0
FlexCAN_5 Debug Disable Cortex-M7_0
Specifies whether FlexCAN_5 enters Debug mode or remains functional and unimpacted when the 
Cortex-M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
28
FLEXCAN4_DB
G_DIS_CM7_0
FlexCAN_4 Debug Disable Cortex-M7_0
Specifies whether FlexCAN_4 enters Debug mode or remains functional and unimpacted when the 
Cortex-M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
27
FLEXCAN3_DB
G_DIS_CM7_0
FlexCAN_3 Debug Disable Cortex-M7_0
Specifies whether FlexCAN_3 enters Debug mode or remains functional and unimpacted when the 
Cortex-M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1386 / 5251


---
# 페이지 135

Table continued from the previous page...
Field
Function
1b - Remains functional and unimpacted
26
FLEXCAN2_DB
G_DIS_CM7_0
FlexCAN_2 Debug Disable Cortex-M7_0
Specifies whether FlexCAN_2 enters Debug mode or remains functional and unimpacted when the 
Cortex-M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
25
FLEXCAN1_DB
G_DIS_CM7_0
FlexCAN_1 Debug Disable Cortex-M7_0
Specifies whether FlexCAN_1 enters Debug mode or remains functional and unimpacted when the 
Cortex-M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
24
FLEXCAN0_DB
G_DIS_CM7_0
FlexCAN_0 Debug Disable Cortex-M7_0
Specifies whether FlexCAN_0 enters Debug mode or remains functional and unimpacted when the 
Cortex-M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
23
FLEXIO_DBG_
DIS_CM7_0
FlexIO Debug Disable Cortex-M7_0
Specifies whether FlexIO enters Debug mode or remains functional and unimpacted when the Cortex-M7_0 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
22
LPI2C1_DBG_D
IS_CM7_0
LPI2C_1 Debug Disable Cortex-M7_0
Specifies whether LPI2C_1 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
21
LPI2C_0 Debug Disable Cortex-M7_0
Specifies whether LPI2C_0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_0 core enters Debug mode.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1387 / 5251


---
# 페이지 136

Table continued from the previous page...
Field
Function
LPI2C0_DBG_D
IS_CM7_0
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
20
LPSPI5_DBG_
DIS_CM7_0
LPSPI_5 Debug Disable Cortex-M7_0
Specifies whether LPSPI_5 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
19
LPSPI4_DBG_
DIS_CM7_0
LPSPI_4 Debug Disable Cortex-M7_0
Specifies whether LPSPI_4 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
18
LPSPI3_DBG_
DIS_CM7_0
LPSPI_3 Debug Disable Cortex-M7_0
Specifies whether LPSPI_3 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
17
LPSPI2_DBG_
DIS_CM7_0
LPSPI_2 Debug Disable Cortex-M7_0
Specifies whether LPSPI_2 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
16
LPSPI1_DBG_
DIS_CM7_0
LPSPI_1 Debug Disable Cortex-M7_0
Specifies whether LPSPI_1 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1388 / 5251


---
# 페이지 137

Table continued from the previous page...
Field
Function
15
LPSPI0_DBG_
DIS_CM7_0
LPSPI_0 Debug Disable Cortex-M7_0
Specifies whether LPSPI_0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
14
PIT2_DBG_DIS
_CM7_0
PIT_2 Debug Disable Cortex-M7_0
Specifies whether PIT_2 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
13
PIT1_DBG_DIS
_CM7_0
PIT_1 Debug Disable Cortex-M7_0
Specifies whether PIT_1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
12
PIT0_DBG_DIS
_CM7_0
PIT_0 Debug Disable Cortex-M7_0
Specifies whether PIT_0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
11
STM1_DBG_DI
S_CM7_0
STM_1 Debug Disable Cortex-M7_0
Specifies whether STM_1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
10
STM0_DBG_DI
S_CM7_0
STM_0 Debug Disable Cortex-M7_0
Specifies whether STM_0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0 
core enters Debug mode.
Write 1 to this field to disable debug.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1389 / 5251


---
# 페이지 138

Table continued from the previous page...
Field
Function
0b - Enters Debug mode
1b - Remains functional and unimpacted
9
—
Reserved
8
SWT0_DBG_DI
S_CM7_0
SWT_0 Debug Disable Cortex-M7_0
Specifies whether SWT_0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
7
RTC_DBG_DIS
_CM7_0
RTC Debug Disable Cortex-M7_0
Specifies whether RTC enters Debug mode or remains functional and unimpacted when the Cortex-M7_0 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
6
EMIOS2_DBG_
DIS_CM7_0
EMIOS2 debug disable bit for CM7_0. Set this bit 1 to disable the debug of IP.
0b - eMIOS2 enters debug mode when CM7_0 enters debug mode.
1b - eMIOS2 remains functional and is not impacted when CM7_0 enters debug mode.
5
EMIOS1_DBG_
DIS_CM7_0
EMIOS1 debug disable bit for CM7_0. Set this bit 1 to disable the debug of IP.
0b - eMIOS1 enters debug mode when CM7_0 enters debug mode.
1b - eMIOS1 remains functional and is not impacted when CM7_0 enters debug mode.
4
EMIOS0_DBG_
DIS_CM7_0
eMIOS_0 Debug Disable Cortex-M7_0
Specifies whether eMIOS_0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
3
LCU1_DBG_DI
S_CM7_0
LCU_1 Debug Disable Cortex-M7_0
Specifies whether LCU_1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0 
core enters Debug mode.
Write 1 to this field to disable debug.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1390 / 5251


---
# 페이지 139

Table continued from the previous page...
Field
Function
0b - Enters Debug mode
1b - Remains functional and unimpacted
2
LCU0_DBG_DI
S_CM7_0
LCU_0 Debug Disable Cortex-M7_0
Specifies whether LCU_0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
1
FCCU_DBG_DI
S_CM7_0
FCCU Debug Disable Cortex-M7_0
Specifies whether FCCU enters Debug mode or remains functional and unimpacted when the Cortex-M7_0 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
0
EDMA_DBG_DI
S_CM7_0
eDMA Debug Disable Cortex-M7_0
Specifies whether eDMA enters Debug mode or remains functional and unimpacted when the Cortex-M7_0 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
38.2.37 Read Write GPR On Destructive Reset 7 (DCMRWD7)
Offset
Register
Offset
DCMRWD7
518h
Function
Contains information related to module debug disable.
This register resets after destructive reset 7.
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1391 / 5251


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
Reserved 
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
PIT3_
DB...
STM3_
DB...
SWT3
_DB...
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
W
Reset
0
0
0
0
0
0
0
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
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
SWT2
_DB...
STM2_
DB...
FLEX
CAN...
FLEX
CAN...
Reserv
ed 
W
Reset
0
0
0
0
0
0
0
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
27
FLEXCAN11_D
BG_DIS_CM7_
0
FLEXCAN11 Debug Disable Cortex-M7_0
FLEXCAN11 debug disable bit for CM7_0. Set this bit 1 to disable the debug of module.
0b - FLEXCAN11 enters debug mode when CM7_0 enters debug mode.
1b - FLEXCAN11 remains functional and is not impacted when CM7_0 enters debug mode.
26
FLEXCAN10_D
BG_DIS_CM7_
0
FLEXCAN10 Debug Disable Cortex-M7_0
FLEXCAN10 debug disable bit for CM7_0. Set this bit 1 to disable the debug of module.
0b - FLEXCAN10 enters debug mode when CM7_0 enters debug mode.
1b - FLEXCAN10 remains functional and is not impacted when CM7_0 enters debug mode.
25
FLEXCAN9_DB
G_DIS_CM7_0
FLEXCAN9 Debug Disable Cortex-M7_0
FLEXCAN9 debug disable bit for CM7_0. Set this bit 1 to disable the debug of module.
0b - FLEXCAN9 enters debug mode when CM7_0 enters debug mode.
1b - FLEXCAN9 remains functional and is not impacted when CM7_0 enters debug mode.
24
FLEXCAN8_DB
G_DIS_CM7_0
FLEXCAN8 Debug Disable Cortex-M7_0
FLEXCAN8 debug disable bit for CM7_0. Set this bit 1 to disable the debug of module.
0b - FLEXCAN8 enters debug mode when CM7_0 enters debug mode.
1b - FLEXCAN8 remains functional and is not impacted when CM7_0 enters debug mode.
23
PIT3_DBG_DIS
_CM7_0
PIT3 Debug Disable Cortex-M7_0
Specifies whether PIT3 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0 
core enters Debug mode.
Write 1 to this field to disable debug.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1392 / 5251


---
# 페이지 141

Table continued from the previous page...
Field
Function
0b - Enters Debug mode
1b - Remains functional and unimpacted
22
STM3_DBG_DI
S_CM7_0
STM3 Debug Disable Cortex-M7_0
Specifies whether STM3 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
21
SWT3_DBG_DI
S_CM7_0
SWT3 Debug Disable Cortex-M7_0
Specifies whether SWT3 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
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
16-15
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
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1393 / 5251


---
# 페이지 142

Table continued from the previous page...
Field
Function
—
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
SWT2_DBG_DI
S_CM7_0
SWT_2 Debug Disable Cortex-M7_0
Specifies whether SWT_2 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_0 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
3
STM2_DBG_DI
S_CM7_0
STM_2 Debug Disable Cortex-M7_0
Specifies whether STM_2 enters Debug mode or remains functional and unimpacted when the Cortex-M7_0 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
2
FLEXCAN7_DB
G_DIS_CM7_0
FLEXCAN7 debug disable bit for CM7_0. Set this bit 1 to disable the debug of module.
0b - FLEXCAN7 enters debug mode when CM7_0 enters debug mode.
1b - FLEXCAN7 remains functional and is not impacted when CM7_0 enters debug mode.
1
FLEXCAN6_DB
G_DIS_CM7_0
FLEXCAN6 debug disable bit for CM7_0. Set this bit 1 to disable the debug of module.
0b - FLEXCAN6 enters debug mode when CM7_0 enters debug mode.
1b - FLEXCAN6 remains functional and is not impacted when CM7_0 enters debug mode.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1394 / 5251


---
# 페이지 143

Table continued from the previous page...
Field
Function
0
—
Reserved
38.2.38 Read Write GPR On Destructive Reset 8 (DCMRWD8)
Offset
Register
Offset
DCMRWD8
51Ch
Function
Provides module debug disable information.
This register resets after destructive reset 8.
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
SAI1_
DB...
SAI0_
DB...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEXI
O_...
LPI2C
1_...
LPI2C
0_...
LPSPI
5_...
LPSPI
4_...
LPSPI
3_...
LPSPI
2_...
LPSPI
1_...
W
Reset
0
0
0
0
0
0
0
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
LPSPI
0_...
PIT2_
DB...
PIT1_
DB...
PIT0_
DB...
STM1_
DB...
STM0_
DB...
SWT1
_DB...
SWT0
_DB...
RTC_
DBG...
EMIO
S2_...
EMIO
S1_...
EMIO
S0_...
LCU1_
DB...
LCU0_
DB...
FCCU
_DB...
EDMA
_DB...
W
Reset
0
0
0
0
0
0
0
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
SAI1_DBG_DIS
_CM7_1
SAI1 debug disable bit for CM7_1. Set this bit 1 to disable the debug of IP.
0b - SAI1 enters debug mode when CM7_1 enters debug mode.
1b - SAI1 remains functional and is not impacted when CM7_1 enters debug mode.
30
SAI0_DBG_DIS
_CM7_1
SAI0 debug disable bit for CM7_1. Set this bit 1 to disable the debug of IP.
0b - SAI0 enters debug mode when CM7_1 enters debug mode.
1b - SAI0 remains functional and is not impacted when CM7_1 enters debug mode.
29
FlexCAN_5 Debug Disable Cortex-M7_1
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1395 / 5251


---
# 페이지 144

Table continued from the previous page...
Field
Function
FLEXCAN5_DB
G_DIS_CM7_1
Specifies whether FlexCAN_5 enters Debug mode or remains functional and unimpacted when the 
Cortex-M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
28
FLEXCAN4_DB
G_DIS_CM7_1
FlexCAN_4 Debug Disable Cortex-M7_1
Specifies whether FlexCAN_4 enters Debug mode or remains functional and unimpacted when the 
Cortex-M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
27
FLEXCAN3_DB
G_DIS_CM7_1
FlexCAN_3 Debug Disable Cortex-M7_1
Specifies whether FlexCAN_3 enters Debug mode or remains functional and unimpacted when the 
Cortex-M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
26
FLEXCAN2_DB
G_DIS_CM7_1
FlexCAN_2 Debug Disable Cortex-M7_1
Specifies whether FlexCAN_2 enters Debug mode or remains functional and unimpacted when the 
Cortex-M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
25
FLEXCAN1_DB
G_DIS_CM7_1
FlexCAN_1 Debug Disable Cortex-M7_1
Specifies whether FlexCAN_1 enters Debug mode or remains functional and unimpacted when the 
Cortex-M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
24
FLEXCAN0_DB
G_DIS_CM7_1
FlexCAN_0 Debug Disable Cortex-M7_1
Specifies whether FlexCAN_0 enters Debug mode or remains functional and unimpacted when the 
Cortex-M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1396 / 5251


---
# 페이지 145

Table continued from the previous page...
Field
Function
0b - Enters Debug mode
1b - Remains functional and unimpacted
23
FLEXIO_DBG_
DIS_CM7_1
FlexIO Debug Disable Cortex-M7_1
Specifies whether FlexIO enters Debug mode or remains functional and unimpacted when the Cortex-M7_1 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
22
LPI2C1_DBG_D
IS_CM7_1
LPI2C_1 Debug Disable Cortex-M7_1
Specifies whether LPI2C_1 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
21
LPI2C0_DBG_D
IS_CM7_1
LPI2C_0 Debug Disable Cortex-M7_1
Specifies whether LPI2C_0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
20
LPSPI5_DBG_
DIS_CM7_1
LPSPI_5 Debug Disable Cortex-M7_1
Specifies whether LPSPI_5 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
19
LPSPI4_DBG_
DIS_CM7_1
LPSPI_4 Debug Disable Cortex-M7_1
Specifies whether LPSPI_4 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
18
LPSPI_3 Debug Disable Cortex-M7_1
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1397 / 5251


---
# 페이지 146

Table continued from the previous page...
Field
Function
LPSPI3_DBG_
DIS_CM7_1
Specifies whether LPSPI_3 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
17
LPSPI2_DBG_
DIS_CM7_1
LPSPI_2 Debug Disable Cortex-M7_1
Specifies whether LPSPI_2 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
16
LPSPI1_DBG_
DIS_CM7_1
LPSPI_1 Debug Disable Cortex-M7_1
Specifies whether LPSPI_1 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
15
LPSPI0_DBG_
DIS_CM7_1
LPSPI_0 Debug Disable Cortex-M7_1
Specifies whether LPSPI_0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
14
PIT2_DBG_DIS
_CM7_1
PIT_2 Debug Disable Cortex-M7_1
Specifies whether PIT_2 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
13
PIT1_DBG_DIS
_CM7_1
PIT_1 Debug Disable Cortex-M7_1
Specifies whether PIT_1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1 
core enters Debug mode.
Write 1 to this field to disable debug.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1398 / 5251


---
# 페이지 147

Table continued from the previous page...
Field
Function
0b - Enters Debug mode
1b - Remains functional and unimpacted
12
PIT0_DBG_DIS
_CM7_1
PIT_0 Debug Disable Cortex-M7_1
Specifies whether PIT_0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
11
STM1_DBG_DI
S_CM7_1
STM_1 Debug Disable Cortex-M7_1
Specifies whether STM_1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
10
STM0_DBG_DI
S_CM7_1
STM_0 Debug Disable Cortex-M7_1
Specifies whether STM_0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
9
SWT1_DBG_DI
S_CM7_1
SWT_1 Debug Disable Cortex-M7_1
Specifies whether SWT_1 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
8
SWT0_DBG_DI
S_CM7_1
SWT_0 Debug Disable Cortex-M7_1
Specifies whether SWT_0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
7
RTC Debug Disable Cortex-M7_1
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1399 / 5251


---
# 페이지 148

Table continued from the previous page...
Field
Function
RTC_DBG_DIS
_CM7_1
Specifies whether RTC enters Debug mode or remains functional and unimpacted when the Cortex-M7_1 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
6
EMIOS2_DBG_
DIS_CM7_1
EMIOS2 debug disable bit for CM7_1. Set this bit 1 to disable the debug of IP.
0b - EMIOS2 enters debug mode when CM7_1 enters debug mode.
1b - EMIOS2 remains functional and is not impacted when CM7_1 enters debug mode.
5
EMIOS1_DBG_
DIS_CM7_1
EMIOS1 debug disable bit for CM7_1. Set this bit 1 to disable the debug of IP.
0b - EMIOS1 enters debug mode when CM7_1 enters debug mode.
1b - EMIOS1 remains functional and is not impacted when CM7_1 enters debug mode.
4
EMIOS0_DBG_
DIS_CM7_1
eMIOS_0 Debug Disable Cortex-M7_1
Specifies whether eMIOS_0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_1 core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
3
LCU1_DBG_DI
S_CM7_1
LCU_1 Debug Disable Cortex-M7_1
Specifies whether LCU_1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
2
LCU0_DBG_DI
S_CM7_1
LCU_0 Debug Disable Cortex-M7_1
Specifies whether LCU_0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
1
FCCU_DBG_DI
S_CM7_1
FCCU Debug Disable Cortex-M7_1
Specifies whether FCCU enters Debug mode or remains functional and unimpacted when the Cortex-M7_1 
core enters Debug mode.
Write 1 to this field to disable debug.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1400 / 5251


---
# 페이지 149

Table continued from the previous page...
Field
Function
0b - Enters Debug mode
1b - Remains functional and unimpacted
0
EDMA_DBG_DI
S_CM7_1
eDMA Debug Disable Cortex-M7_1
Specifies whether eDMA enters Debug mode or remains functional and unimpacted when the Cortex-M7_1 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
38.2.39 Read Write GPR On Destructive Reset 9 (DCMRWD9)
Offset
Register
Offset
DCMRWD9
520h
Function
Provides module debug disable information.
This register resets after destructive reset 9.
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
FLEXC
AN...
FLEXC
AN...
FLEXC
AN...
FLEXC
AN...
PIT3_
DB...
STM3_
DB...
SWT3
_DB...
Reserved 
Reserv
ed 
W
Reset
0
0
0
0
0
0
0
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
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserved 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
W
Reset
0
0
0
0
0
0
0
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
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1401 / 5251


---
# 페이지 150

Table continued from the previous page...
Field
Function
27
FLEXCAN11_D
BG_DIS_CM7_
1
FLEXCAN11 Debug Disable Cortex-M7_1
FLEXCAN11 debug disable bit for CM7_1. Set this bit 1 to disable the debug of module.
0b - FLEXCAN11 enters debug mode when CM7_1 enters debug mode.
1b - FLEXCAN11 remains functional and is not impacted when CM7_1 enters debug mode.
26
FLEXCAN10_D
BG_DIS_CM7_
1
FLEXCAN10 Debug Disable Cortex-M7_1
FLEXCAN10 debug disable bit for CM7_1. Set this bit 1 to disable the debug of module.
0b - FLEXCAN10 enters debug mode when CM7_1 enters debug mode.
1b - FLEXCAN10 remains functional and is not impacted when CM7_1 enters debug mode.
25
FLEXCAN9_DB
G_DIS_CM7_1
FLEXCAN9 Debug Disable Cortex-M7_1
FLEXCAN9 debug disable bit for CM7_1. Set this bit 1 to disable the debug of module.
0b - FLEXCAN9 enters debug mode when CM7_1 enters debug mode.
1b - FLEXCAN9 remains functional and is not impacted when CM7_1 enters debug mode.
24
FLEXCAN8_DB
G_DIS_CM7_1
FLEXCAN8 Debug Disable Cortex-M7_1
FLEXCAN8 debug disable bit for CM7_1. Set this bit 1 to disable the debug of module.
0b - FLEXCAN8 enters debug mode when CM7_1 enters debug mode.
1b - FLEXCAN8 remains functional and is not impacted when CM7_1 enters debug mode.
23
PIT3_DBG_DIS
_CM7_1
PIT3 Debug Disable Cortex-M7_1
Specifies whether PIT3 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
22
STM3_DBG_DI
S_CM7_1
STM3 Debug Disable Cortex-M7_1
Specifies whether STM3 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
21
SWT3_DBG_DI
S_CM7_1
SWT3 Debug Disable Cortex-M7_1
Specifies whether SWT3 enters Debug mode or remains functional and unimpacted when the Cortex-M7_1 
core enters Debug mode.
Write 1 to this field to disable debug.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1402 / 5251


---
# 페이지 151

Table continued from the previous page...
Field
Function
0b - Enters Debug mode
1b - Remains functional and unimpacted
20-17
—
Reserved
16-15
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
10-6
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
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1403 / 5251


---
# 페이지 152

38.2.40 Read Write GPR On Destructive Reset 12 (DCMRWD12)
Offset
Register
Offset
DCMRWD12
52Ch
Function
Provides module debug disable information.
This register resets after destructive reset 12.
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
SAI1_
DB...
SAI0_
DB...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEXI
O_...
LPI2C
1_...
LPI2C
0_...
LPSPI
5_...
LPSPI
4_...
LPSPI
3_...
LPSPI
2_...
LPSPI
1_...
W
Reset
0
0
0
0
0
0
0
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
LPSPI
0_...
PIT2_
DB...
PIT1_
DB...
PIT0_
DB...
STM1_
DB...
STM0_
DB...
Reserv
ed 
SWT0
_DB...
RTC_
DBG...
eMIOS
2_...
eMIOS
1_...
eMIOS
0_...
LCU1_
DB...
LCU0_
DB...
FCCU
_DB...
EDMA
_DB...
W
Reset
0
0
0
0
0
0
0
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
SAI1_DBG_DIS
_CM7_2
SAI1 debug disable bit for CM7_2. Set this bit 1 to disable the debug of module.
0b - SAI1 enters debug mode when CM7_2 enters debug mode.
1b - SAI1 remains functional and is not impacted when CM7_2 enters debug mode.
30
SAI0_DBG_DIS
_CM7_2
SAI0 debug disable bit for CM7_2. Set this bit 1 to disable the debug of module.
0b - SAI0 enters debug mode when CM7_2 enters debug mode.
1b - SAI0 remains functional and is not impacted when CM7_2 enters debug mode.
29
FLEXCAN5_DB
G_DIS_CM7_2
FlexCAN5 Debug Disable For Cortex M7_2
Specifies whether FlexCAN5 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, FlexCAN5 enters Debug mode, and if this field = 1, FlexCAN5 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
28
FlexCAN4 Debug Disable For Cortex M7_2
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1404 / 5251


---
# 페이지 153

Table continued from the previous page...
Field
Function
FLEXCAN4_DB
G_DIS_CM7_2
Specifies whether FlexCAN4 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, FlexCAN4 enters Debug mode, and if this field = 1, FlexCAN4 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
27
FLEXCAN3_DB
G_DIS_CM7_2
FlexCAN3 Debug Disable For Cortex M7_2
Specifies whether FlexCAN3 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, FlexCAN3 enters Debug mode, and if this field = 1, FlexCAN3 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
26
FLEXCAN2_DB
G_DIS_CM7_2
FlexCAN2 Debug Disable For Cortex M7_2
Specifies whether FlexCAN2 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, FlexCAN2 enters Debug mode, and if this field = 1, FlexCAN2 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
25
FLEXCAN1_DB
G_DIS_CM7_2
FlexCAN1 Debug Disable For Cortex M7_2
Specifies whether FlexCAN1 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, FlexCAN1 enters Debug mode, and if this field = 1, FlexCAN1 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
24
FLEXCAN0_DB
G_DIS_CM7_2
FlexCAN0 Debug Disable For Cortex M7_2
Specifies whether FlexCAN0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, FlexCAN0 enters Debug mode, and if this field = 1, FlexCAN0 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
23
FlexIO Debug Disable For Cortex M7_2
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1405 / 5251


---
# 페이지 154

Table continued from the previous page...
Field
Function
FLEXIO_DBG_
DIS_CM7_2
Specifies whether FlexIO enters Debug mode or remains functional and unimpacted when the Cortex-M7_2 
core enters Debug mode. If this field = 0, FlexIO enters Debug mode, and if this field = 1, FlexIO 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
22
LPI2C1_DBG_D
IS_CM7_2
LPI2C1 Debug Disable For Cortex M7_2
Specifies whether LPI2C1 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, LPI2C1 enters Debug mode, and if this field = 1, LPI2C1 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
21
LPI2C0_DBG_D
IS_CM7_2
LPI2C0 Debug Disable For Cortex M7_2
Specifies whether LPI2C0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, LPI2C0 enters Debug mode, and if this field = 1, LPI2C0 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
20
LPSPI5_DBG_
DIS_CM7_2
LPSPI5 Debug Disable For Cortex M7_2
Specifies whether LPSPI5 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, LPSPI5 enters Debug mode, and if this field = 1, LPSPI5 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
19
LPSPI4_DBG_
DIS_CM7_2
LPSPI4 Debug Disable For Cortex M7_2
Specifies whether LPSPI4 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, LPSPI4 enters Debug mode, and if this field = 1, LPSPI4 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
18
LPSPI3 Debug Disable For Cortex M7_2
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1406 / 5251


---
# 페이지 155

Table continued from the previous page...
Field
Function
LPSPI3_DBG_
DIS_CM7_2
Specifies whether LPSPI3 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, LPSPI3 enters Debug mode, and if this field = 1, LPSPI3 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
17
LPSPI2_DBG_
DIS_CM7_2
LPSPI2 Debug Disable For Cortex M7_2
Specifies whether LPSPI2 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, LPSPI2 enters Debug mode, and if this field = 1, LPSPI2 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
16
LPSPI1_DBG_
DIS_CM7_2
LPSPI1 Debug Disable For Cortex M7_2
Specifies whether LPSPI1 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, LPSPI1 enters Debug mode, and if this field = 1, LPSPI1 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
15
LPSPI0_DBG_
DIS_CM7_2
LPSPI0 Debug Disable For Cortex M7_2
Specifies whether LPSPI0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, LPSPI0 enters Debug mode, and if this field = 1, LPSPI0 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
14
PIT2_DBG_DIS
_CM7_2
PIT2 Debug Disable For Cortex M7_2
Specifies whether PIT2 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, PIT2 enters Debug mode, and if this field = 1, PIT2 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
13
PIT1 Debug Disable For Cortex M7_2
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1407 / 5251


---
# 페이지 156

Table continued from the previous page...
Field
Function
PIT1_DBG_DIS
_CM7_2
Specifies whether PIT1 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, PIT1 enters Debug mode, and if this field = 1, PIT1 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
12
PIT0_DBG_DIS
_CM7_2
PIT0 Debug Disable For Cortex M7_2
Specifies whether PIT0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, PIT0 enters Debug mode, and if this field = 1, PIT0 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
11
STM1_DBG_DI
S_CM7_2
STM1 Debug Disable For Cortex M7_2
Specifies whether STM1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2 
core enters Debug mode. If this field = 0, STM1 enters Debug mode, and if this field = 1, STM1 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
10
STM0_DBG_DI
S_CM7_2
STM0 Debug Disable For Cortex M7_2
Specifies whether STM0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2 
core enters Debug mode. If this field = 0, STM0 enters Debug mode, and if this field = 1, STM0 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
9
—
Reserved
8
SWT0_DBG_DI
S_CM7_2
SWT0 Debug Disable For Cortex M7_2
Specifies whether SWT0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2 
core enters Debug mode. If this field = 0, SWT0 enters Debug mode, and if this field = 1, SWT0 
remains functional.
Write 1 to this field to disable debug.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1408 / 5251


---
# 페이지 157

Table continued from the previous page...
Field
Function
0b - Enables Debug mode
1b - Disables Debug mode
7
RTC_DBG_DIS
_CM7_2
RTC Debug Disable For Cortex M7_2
Specifies whether RTC enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, RTC enters Debug mode, and if this field = 1, RTC 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
6
eMIOS2_DBG_
DIS_CM7_2
eMIOS2 debug disable bit for CM7_2. Set this bit 1 to disable the debug of module.
0b - eMIOS2 enters debug mode when CM7_2 enters debug mode.
1b - eMIOS2 remains functional and is not impacted when CM7_2 enters debug mode.
5
eMIOS1_DBG_
DIS_CM7_2
eMIOS1 debug disable bit for CM7_2. Set this bit 1 to disable the debug of module.
0b - eMIOS1 enters debug mode when CM7_2 enters debug mode.
1b - eMIOS1 remains functional and is not impacted when CM7_2 enters debug mode.
4
eMIOS0_DBG_
DIS_CM7_2
eMIOS0 Debug Disable For Cortex M7_2
Specifies whether eMIOS0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, eMIOS0 enters Debug mode, and if this field = 1, eMIOS0 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
3
LCU1_DBG_DI
S_CM7_2
LCU1 Debug Disable For Cortex M7_2
Specifies whether LCU1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2 
core enters Debug mode. If this field = 0, LCU1 enters Debug mode, and if this field = 1, LCU1 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
2
LCU0_DBG_DI
S_CM7_2
LCU0 Debug Disable For Cortex M7_2
Specifies whether LCU0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2 
core enters Debug mode. If this field = 0, LCU0 enters Debug mode, and if this field = 1, LCU0 
remains functional.
Write 1 to this field to disable debug.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1409 / 5251


---
# 페이지 158

Table continued from the previous page...
Field
Function
0b - Enables Debug mode
1b - Disables Debug mode
1
FCCU_DBG_DI
S_CM7_2
FCCU Debug Disable For Cortex M7_2
Specifies whether FCCU enters Debug mode or remains functional and unimpacted when the Cortex-M7_2 
core enters Debug mode. If this field = 0, FCCU enters Debug mode, and if this field = 1, FCCU 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
0
EDMA_DBG_DI
S_CM7_2
eDMA Debug Disable For Cortex M7_2
Specifies whether eDMA enters Debug mode or remains functional and unimpacted when the Cortex-M7_2 
core enters Debug mode. If this field = 0, eDMA enters Debug mode, and if this field = 1, eDMA 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
38.2.41 Read Write GPR On Destructive Reset 13 (DCMRWD13)
Offset
Register
Offset
DCMRWD13
530h
Function
Provides module debug disable information.
This register resets after destructive reset 13.
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1410 / 5251


---
# 페이지 159

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
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
PIT3_
DB...
STM3_
DB...
SWT3
_DB...
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
W
Reset
0
0
0
0
0
0
0
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
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
SWT2
_DB...
STM2_
DB...
FLEX
CAN...
FLEX
CAN...
Reserv
ed 
W
Reset
0
0
0
0
0
0
0
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
27
FLEXCAN11_D
BG_DIS_CM7_
2
FLEXCAN11 Debug Disable Cortex-M7_2
FLEXCAN11 debug disable bit for CM7_2. Set this bit 1 to disable the debug of module.
0b - FLEXCAN11 enters debug mode when CM7_2 enters debug mode.
1b - FLEXCAN11 remains functional and is not impacted when CM7_2 enters debug mode.
26
FLEXCAN10_D
BG_DIS_CM7_
2
FLEXCAN10 Debug Disable Cortex-M7_2
FLEXCAN10 debug disable bit for CM7_2. Set this bit 1 to disable the debug of module.
0b - FLEXCAN10 enters debug mode when CM7_2 enters debug mode.
1b - FLEXCAN10 remains functional and is not impacted when CM7_2 enters debug mode.
25
FLEXCAN9_DB
G_DIS_CM7_2
FLEXCAN9 Debug Disable Cortex-M7_2
FLEXCAN9 debug disable bit for CM7_2. Set this bit 1 to disable the debug of module.
0b - FLEXCAN9 enters debug mode when CM7_2 enters debug mode.
1b - FLEXCAN9 remains functional and is not impacted when CM7_2 enters debug mode.
24
FLEXCAN8_DB
G_DIS_CM7_2
FLEXCAN8 Debug Disable Cortex-M7_2
FLEXCAN8 debug disable bit for CM7_2. Set this bit 1 to disable the debug of module.
0b - FLEXCAN8 enters debug mode when CM7_2 enters debug mode.
1b - FLEXCAN8 remains functional and is not impacted when CM7_2 enters debug mode.
23
PIT3_DBG_DIS
_CM7_2
PIT3 Debug Disable Cortex-M7_2
Specifies whether PIT3 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2 
core enters Debug mode.
Write 1 to this field to disable debug.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1411 / 5251


---
# 페이지 160

Table continued from the previous page...
Field
Function
0b - Enters Debug mode
1b - Remains functional and unimpacted
22
STM3_DBG_DI
S_CM7_2
STM3 Debug Disable Cortex-M7_2
Specifies whether STM3 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
21
SWT3_DBG_DI
S_CM7_2
SWT3 Debug Disable Cortex-M7_2
Specifies whether SWT3 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - Enters Debug mode
1b - Remains functional and unimpacted
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
16-15
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
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1412 / 5251


---
# 페이지 161

Table continued from the previous page...
Field
Function
—
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
SWT2_DBG_DI
S_CM7_2
SWT2 Debug Disable For Cortex-M7_2
Specifies whether SWT2 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2 
core enters Debug mode. If this field = 0, SWT2 enters Debug mode, and if this field = 1, SWT2 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
3
STM2_DBG_DI
S_CM7_2
STM2 Debug Disable For Cortex-M7_2
Specifies whether STM2 enters Debug mode or remains functional and unimpacted when the Cortex-M7_2 
core enters Debug mode. If this field = 0, STM2 enters Debug mode, and if this field = 1, STM2 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
2
FLEXCAN7_DB
G_DIS_CM7_2
FLEXCAN7 debug disable bit for CM7_2. Set this bit 1 to disable the debug of module.
0b - FLEXCAN7 enters debug mode when CM7_2 enters debug mode.
1b - FLEXCAN7 remains functional and is not impacted when CM7_2 enters debug mode.
1
FlexCAN6 Debug Disable For Cortex-M7_2
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1413 / 5251


---
# 페이지 162

Table continued from the previous page...
Field
Function
FLEXCAN6_DB
G_DIS_CM7_2
Specifies whether FlexCAN6 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_2 core enters Debug mode. If this field = 0, FlexCAN6 enters Debug mode, and if this field = 1, FlexCAN6 
remains functional.
Write 1 to this field to disable debug.
0b - Enables Debug mode
1b - Disables Debug mode
0
—
Reserved
38.2.42 Read Write GPR On Destructive Reset 14 (DCMRWD14)
Offset
Register
Offset
DCMRWD14
534h
Function
Provides module debug disable information.
This register resets after destructive reset 14.
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
Reserv
ed 
TCM_
PRA...
Reserv
ed 
Reserv
ed 
Reserv
ed 
AIPS0
_G...
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
W
Reset
0
1
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
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
W
Reset
0
0
0
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
Fields
Field
Function
31
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1414 / 5251


---
# 페이지 163

Table continued from the previous page...
Field
Function
30
TCM_PRAM_A
XBS_ALARM_E
N
TCM_PRAM AXBS Alarm Enable
Specifies whether TCM_PRAM AXBS_Lite reported a safety alarm.
The field enables fault monitoring at FCCU NCF 1 for TCM_PRAM AXBS_Lite safety alarm.
0b - No
1b - Yes
29
—
Reserved
28
—
Reserved
27
—
Reserved
26
AIPS0_GSKT_A
LARM_EN
AIPS0 Gasket Alarm Enable
Specifies whether AIPS0 gasket reported a safety alarm.
The field enables fault monitoring at FCCU NCF 1 for AIPS0 gasket safety alarm.
0b - No
1b - Yes
25
—
Reserved
24
—
Reserved
23
—
Reserved
22
—
Reserved
21
—
Reserved
20
—
Reserved
19
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1415 / 5251


---
# 페이지 164

Table continued from the previous page...
Field
Function
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
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1416 / 5251


---
# 페이지 165

Table continued from the previous page...
Field
Function
—
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
38.2.43 Read Write GPR On Destructive Reset 15 (DCMRWD15)
Offset
Register
Offset
DCMRWD15
538h
Function
Provides module debug disable information.
This register resets after destructive reset 15.
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
Reserv
ed 
CM7_2
_A...
Reserv
ed 
CM7_0
_A...
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
W
Reset
0
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
Reserv
ed 
Reserv
ed 
Reserv
ed 
VDD2
P5_...
VDD1
P1_...
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
CM7_2
_A...
CM7_1
_A...
CM7_0
_A...
CM7_2
_A...
CM7_1
_A...
CM7_0
_A...
W
Reset
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
1
1
1
1
1
1
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1417 / 5251


---
# 페이지 166

Fields
Field
Function
31
—
Reserved
30
CM7_2_AHBS_
ALARM_EN
Cortex-M7_2 AHBS Alarm Enable
Specifies whether the Cortex-M7_2 AHBS interface IAHB gasket reported an alarm. Enables fault 
monitoring at FCCU NCF 1 in case of a Cortex-M7_2 AHBS interface IAHB Gasket monitor alarm.
0b - No
1b - Yes
29
—
Reserved
28
CM7_0_AHBS_
ALARM_EN
Cortex-M7_0 AHBS Alarm Enable
Specifies whether the Cortex-M7_0 AHBS interface IAHB gasket reported an alarm. Enables fault 
monitoring at FCCU NCF 1 in case of a Cortex-M7_0 AHBS interface IAHB Gasket monitor alarm.
0b - No
1b - Yes
27
—
Reserved
26
—
Reserved
25
—
Reserved
24
—
Reserved
23
—
Reserved
22
—
Reserved
21
—
Reserved
20
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1418 / 5251


---
# 페이지 167

Table continued from the previous page...
Field
Function
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
VDD2P5_GNG2
_ERR_EN
VDD2P5 Go Nogo Error Enable
Enables bit for enabling the fault monitoring at FCCU NCF 4 for the fault: Go/Nogo for VDD_HV_FLA 
(triple bond) going to FXOSC and PLL.
0b - Go indication referring to the supply being clean.
1b - No go indication referring to the supply being unclean and a fault in double bond connection 
or its routing within the chip.
11
VDD1P1_GNG2
_ERR_EN
VDD1P1 Go Nogo Error Enable
Enable bit for enabling the fault monitoring at FCCU NCF 4 for the fault: Go/Nogo indicator for VDD1PD1 
(triple bond) supply going to PLL.
0b - Go indication referring to the supply being clean.
1b - No go indication referring to the supply being unclean and a fault in double bond connection 
or its routing within the chip.
10
—
Reserved
9
—
Reserved
8
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1419 / 5251


---
# 페이지 168

Table continued from the previous page...
Field
Function
—
7
—
Reserved
6
—
Reserved
5
CM7_2_AHBP_
ALARM_EN
Cortex-M7_2 AHBP Alarm Enable
Specifies whether the Cortex-M7_2 AHBP interface IAHB gasket reported an alarm. If this field = 1, the 
gasket reports a monitor alarm.
The field enables fault monitoring at FCCU NCF 1 in case of a Cortex-M7_2 AHBP interface IAHB gasket 
monitor alarm.
0b - No
1b - Yes
4
CM7_1_AHBP_
ALARM_EN
Cortex-M7_1 AHBP Alarm Enable
Specifies whether the Cortex-M7_1 AHBP interface IAHB gasket reported an alarm. If this field = 1, the 
gasket reports a monitor alarm.
The field enables fault monitoring at FCCU NCF 1 in case of a Cortex-M7_1 AHBP interface IAHB gasket 
monitor alarm.
0b - No
1b - Yes
3
CM7_0_AHBP_
ALARM_EN
Cortex-M7_0 AHBP Alarm Enable
Specifies whether the Cortex-M7_0 AHBP interface IAHB gasket reported an alarm. If this field = 1, the 
gasket reports a monitor alarm.
The field enables fault monitoring at FCCU NCF 1 in case of a Cortex-M7_0 AHBP interface IAHB gasket 
monitor alarm.
0b - No
1b - Yes
2
CM7_2_AHBM_
ALARM_EN
Cortex-M7_2 AHBM Alarm Enable
Specifies whether the Cortex-M7_2 AHBM interface IAHB gasket reported an alarm. If this field = 1, the 
gasket reports a monitor alarm.
The field enables fault monitoring at FCCU NCF 1 in case of a Cortex-M7_2 AHBM interface IAHB gasket 
monitor alarm.
0b - No
1b - Yes
1
Cortex-M7_1 AHBM Alarm Enable
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1420 / 5251


---
# 페이지 169

Table continued from the previous page...
Field
Function
CM7_1_AHBM_
ALARM_EN
Specifies whether the Cortex-M7_1 AHBM interface IAHB gasket reported an alarm. If this field = 1, the 
gasket reports a monitor alarm.
The field enables fault monitoring at FCCU NCF 1 in case of a Cortex-M7_1 AHBM interface IAHB gasket 
monitor alarm.
0b - No
1b - Yes
0
CM7_0_AHBM_
ALARM_EN
Cortex-M7_0 AHBM Alarm Enable
Specifies whether the Cortex-M7_0 AHBM interface IAHB gasket reported an alarm. If this field = 1, the 
gasket reports a monitor alarm.
The field enables fault monitoring at FCCU NCF 1 in case of a Cortex-M7_0 AHBM interface IAHB gasket 
monitor alarm.
0b - No
1b - Yes
38.2.44 Read Write GPR On Destructive Reset 16 (DCMRWD16)
Offset
Register
Offset
DCMRWD16
53Ch
Function
This is a readable and writable general purpose register which gets reset on destructive reset.
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
Reserv
ed 
Reserv
ed 
CM7_3
_D...
CM7_3
_D...
CM7_3
_I...
CM7_3
_I...
CM7_3
_I...
CM7_3
_D...
CM7_3
_D...
CM7_3
_A...
CM7_3
_A...
Reserv
ed 
AES_A
CC...
AES_A
CC...
ACE_F
EE...
ACE_
RES...
W
Reset
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
1
0
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
Reserv
ed 
CM7_3
_A...
HSE_
AES...
CM7_3
_A...
CM7_3
_A...
MAC2
_RD...
MAC2
_GS...
Reserv
ed 
PERIP
H_...
CM7_2
_R...
CM7_2
_R...
CM7_3
_L...
Reserved 
W
Reset
0
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
1
0
0
0
0
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1421 / 5251


---
# 페이지 170

Fields
Field
Function
31
—
Reserved
30
—
Reserved
29
CM7_3_DTCM1
_ECC_ERR_EN
Enables bit for enabling the fault monitoring at FCCU NCF 2 for the fault: Uncorrectable ECC error from 
CM7_3 Data TCM memory block 1. This uncorrectable ECC error consists of multi-bit data ECC error 
and address ECC error. The CM7_3 Data TCM physically consists of two blocks.
0b - Uncorrectable ECC error detection at FCCU not enabled.
1b - Uncorrectable ECC error detection enabled at FCCU.
28
CM7_3_DTCM0
_ECC_ERR_EN
Enables bit for enabling the fault monitoring at FCCU NCF 2 for the fault: Uncorrectable ECC error from 
CM7_3 Data TCM memory block 0. This uncorrectable ECC error consists of multi-bit data ECC error 
and address ECC error. The CM7_3 Data TCM physically consists of two blocks.
0b - Uncorrectable ECC error detection at FCCU not enabled.
1b - Uncorrectable ECC error detection enabled at FCCU.
27
CM7_3_ITCM_
ECC_ERR_EN
Enables bit for enabling the fault monitoring at FCCU NCF 2 for the fault: Uncorrectable ECC error from 
CM7_3 Instruction TCM memory. This uncorrectable ECC error consists of multi-bit data ECC error and 
address ECC error.
0b - Uncorrectable ECC error detection at FCCU not enabled.
1b - Uncorrectable ECC error detection enabled at FCCU.
26
CM7_3_ICTAG_
ECC_ERR_EN
Enables bit for enabling the fault monitoring at FCCU NCF 2 for the fault: Multi bit ECC error from CM7_3 
ICache tag memory.
0b - No multi-bit ECC error.
1b - Multi-bit ECC error.
25
CM7_3_ICDAT
A_ECC_ERR_E
N
Enables bit for enabling the fault monitoring at FCCU NCF 2 for the fault: Multi bit ECC error from CM7_3 
ICache data memory
0b - No multi-bit ECC error.
1b - Multi-bit ECC error.
24
CM7_3_DCTAG
_ECC_ERR_EN
Enables bit for enabling the fault monitoring at FCCU NCF 2 for the fault: Multi bit ECC error from CM7_3 
DCache tag memory
0b - No multi-bit ECC error.
1b - Multi-bit ECC error.
23
CM7_3_DCDAT
A_ECC_ERR_E
N
Enables bit for enabling the fault monitoring at FCCU NCF 2 for the fault: Multi bit ECC error from CM7_3 
DCache data memory.
0b - No multi-bit ECC error.
1b - Multi-bit ECC error.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1422 / 5251


---
# 페이지 171

Table continued from the previous page...
Field
Function
22
CM7_3_AHBP_
ALARM_EN
Enables bit for enabling the fault monitoring at FCCU NCF 1 for the fault: CM7_3 AHBP interface IAHB 
Gasket monitor alarm.
0b - No alarm reported from CM7_3 AHBP interface IAHB gasket.
1b - Monitor alarm reported from CM7_3 AHBP interface IAHB gasket.
21
CM7_3_AHBM_
ALARM_EN
Enables bit for enabling the fault monitoring at FCCU NCF 1 for the fault: CM7_3 AHBM interface IAHB 
Gasket monitor alarm.
0b - No alarm reported from CM7_3 AHBP interface IAHB gasket.
1b - Monitor alarm reported from CM7_3 AHBP interface IAHB gasket.
20
—
Reserved
19
AES_ACCEL_G
SKT_ALARM_E
N
Enables bit for enabling the fault monitoring at FCCU NCF 1 for the fault: AES ACCEL IAHB Gasket 
monitor alarm.
0b - No alarm reported from AES ACCEL IAHB gasket.
1b - Monitor alarm reported from AES ACCEL IAHB gasket.
18
AES_ACCEL_A
XBS_ALARM_E
N
Enables bit for enabling the fault monitoring at FCCU NCF 1 for the fault: AES_ACCEL AXBS_Lite safety 
alarm.
0b - No safety alarm indicated by AES_ACCEL AXBS_Lite.
1b - Safety alarm indicated by AES_ACCEL AXBS_Lite.
17
ACE_FEED_RD
ATA_EDC_ERR
_EN
Enables bit for enabling the fault monitoring at FCCU NCF 1 for the fault: Integrity error on ACE ACCEL 
FEED DMA master port read data for safety.
0b - No integrity error reported on ACE ACCEL FEED DMA master port read data.
1b - Integrity error reported on ACE ACCEL FEED DMA master port read data.
16
ACE_RESULT_
RDATA_EDC_E
RR_EN
Enables bit for enabling the fault monitoring at FCCU NCF 1 for the fault: Integrity error on ACE ACCEL 
RESULT DMA master port read data for safety.
0b - No integrity error reported on ACE ACCEL RESULT DMA master port read data.
1b - Integrity error reported on ACE ACCEL RESULT DMA master port read data.
15
—
Reserved
14
CM7_3_AHBS_
ALARM_EN
Enables bit for enabling the fault monitoring at FCCU NCF 1 for the fault: CM7_3 AHBS interface IAHB 
Gasket monitor alarm.
0b - No alarm reported from CM7_3 AHBS interface IAHB gasket.
1b - Monitor alarm reported from CM7_3 AHBS interface IAHB gasket.
13
Enables bit for enabling the fault monitoring at FCCU NCF 1 for the fault: HSE_AES_ACCEL AXBS_Lite 
safety alarm.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1423 / 5251


---
# 페이지 172

Table continued from the previous page...
Field
Function
HSE_AES_ACC
EL_AXBS_ALA
RM_EN
0b - No safety alarm indicated by HSE_AES_ACCEL AXBS_Lite.
1b - Safety alarm indicated by HSE_AES_ACCEL AXBS_Lite.
12
CM7_3_AHBM_
RDATA_EDC_E
RR_EN
Enables bit for enabling the fault monitoring at FCCU NCF 1 for the fault: Integrity error on CM7_3 main 
read data for safety.
0b - No integrity error reported on CM7_3 main read data.
1b - Integrity error reported on CM7_3 main read data.
11
CM7_3_AHBP_
RDATA_EDC_E
RR_EN
Enables bit for enabling the fault monitoring at FCCU NCF 1 for the fault: Integrity error on CM7_3 
peripheral read data for safety.
0b - No integrity error reported on CM7_3 peripheral read data.
1b - Integrity error reported on CM7_3 peripheral read data.
10
MAC2_RDATA_
EDC_ERR_EN
Enables bit for enabling the fault monitoring at FCCU NCF 1 for the fault: Integrity(EDC) error on MAC2 
read data for safety.
0b - No integrity error reported on MAC2 read data.
1b - Integrity error reported on MAC2 read data.
9
MAC2_GSKT_A
LARM_EN
Enables bit for enabling the fault monitoring at FCCU NCF 1 for the fault: MAC2 IAHB gasket alarm.
0b - No alarm indicated by MAC2 IAHB gasket.
1b - Alarm indicated by MAC2 IAHB gasket.
8
—
Reserved
7
PERIPH_AXBS
_S3_GSKT_AL
ARM_EN
Enables bit for enabling the fault monitoring at FCCU NCF 1 for the fault: Peripheral AXBS bridge S3 
IAHB gasket alarm.
0b - No alarm indicated by Peripheral AXBS bridge S3 IAHB gasket alarm.
1b - Alarm indicated by Peripheral AXBS bridge S3 IAHB gasket alarm.
6
CM7_2_RCCU2
_ALARM_EN
Enables bit for enabling the fault monitoring at FCCU NCF 0 for the fault: Cortex M7 cores (CM7_2 and 
CM7_2_checker core) redundant lockstep error.
0b - No lockstep alarm reported by redundant RCCU.
1b - Lockstep alarm reported by redundant RCCU.
5
CM7_2_RCCU1
_ALARM_EN
Enables bit for enabling the fault monitoring at FCCU NCF 0 for the fault: Cortex M7 cores (CM7_2 and 
CM7_2_checker core) lockstep error.
0b - No lockstep alarm reported by RCCU.
1b - Lockstep alarm reported by RCCU.
4
Enables bit for enabling the fault monitoring at FCCU NCF 0 for the fault: CM7_3 core lockup.
0b - CM7_3 core not in lockup state.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1424 / 5251


---
# 페이지 173

Table continued from the previous page...
Field
Function
CM7_3_LOCKU
P_EN
1b - CM7_3 core in lockup state.
3-0
—
Reserved
38.2.45 Read Write GPR On Destructive Reset 17 (DCMRWD17)
Offset
Register
Offset
DCMRWD17
540h
Function
This is a readable and writable general purpose register which gets reset on destructive reset.
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
PF1_1
_C...
PF1_0
_C...
PF0_1
_C...
PF0_0
_C...
PF1_1
_C...
PF1_0
_C...
PF0_1
_C...
PF0_0
_C...
PRAM
3_F...
PRAM
3_E...
FLASH
1_...
W
Reset
0
0
0
0
0
0
0
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
Reserv
ed 
FLAS
H1_...
FLAS
H1_...
FLAS
H1_...
FLAS
H1_...
PF1_1
_D...
PF1_1
_C...
PF1_0
_D...
PF1_0
_C...
AES_
RES...
AES_F
EE...
AES_K
P_...
AES_
RES...
AES_
RES...
AES_F
EE...
AES_F
EE...
W
Reset
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
1
1
1
Fields
Field
Function
31-27
—
Reserved
26
PF1_1_CHK_C
MP_EN
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: PFLASH3 checker(redundant) 
safety comparator.
0b - No comparator error by PFLASH3.
1b - Comparator error by PFLASH3.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1425 / 5251


---
# 페이지 174

Table continued from the previous page...
Field
Function
25
PF1_0_CHK_C
MP_EN
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: PFLASH2 checker(redundant) 
safety comparator.
0b - No comparator error by PFLASH2.
1b - Comparator error by PFLASH2.
24
PF0_1_CHK_C
MP_EN
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: PFLASH1 checker(redundant) 
safety comparator.
0b - No comparator error by PFLASH1.
1b - Comparator error by PFLASH1.
23
PF0_0_CHK_C
MP_EN
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: PFLASH0 checker(redundant) 
safety comparator.
0b - No comparator error by PFLASH0.
1b - Comparator error by PFLASH0.
22
PF1_1_CMP_E
N
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: PFLASH3 safety comparator.
0b - No comparator error by PFLASH3.
1b - Comparator error by PFLASH3.
21
PF1_0_CMP_E
N
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: PFLASH2 safety comparator.
0b - No comparator error by PFLASH2.
1b - Comparator error by PFLASH2.
20
PF0_1_CMP_E
N
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: PFLASH1 safety comparator.
0b - No comparator error by PFLASH1.
1b - Comparator error by PFLASH1.
19
PF0_0_CMP_E
N
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: PFLASH0 safety comparator.
0b - No comparator error by PFLASH0.
1b - Comparator error by PFLASH0.
18
PRAM3_FCCU_
ALARM_EN
Enable bit for enabling the fault monitoring at FCCU NCF 2 for the fault: PRAM3 safety alarm. This alarm 
is set on faulty SRAM3 read or read modify error.
0b - No safety alarm indicated by PRAM3.
1b - Safety alarm indicated by PRAM3.
17
PRAM3_ECC_E
RR_EN
Enable bit for enabling the fault monitoring at FCCU NCF 2 for the fault: Multi bit ECC error from SRAM3.
0b - No multi-bit ECC error.
1b - Multi-bit ECC error.
16
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: ECC error from Flash 
Controller1. This alarm indicates that the flash controller1 detected an error in the address ECC 
manipulation logic through EDC.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1426 / 5251


---
# 페이지 175

Table continued from the previous page...
Field
Function
FLASH1_ECC_
ERR_EN
0b - No ECC error from flash controller1.
1b - ECC error from flash controller1.
15
—
Reserved
14
FLASH1_RST_
ERR_EN
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: Flash1 reset error . This error 
indication is set when flash1 encounters errors during its reset reads.
0b - No flash1 reset error indicated.
1b - Flash1 reset error indicated.
13
FLASH1_REF_
ERR_EN
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: Flash1 reference current loss or 
read voltage error while prevoius read.
0b - No reference current loss or read voltage error while previous read.
1b - Reference current loss or read voltage error while previous read.
12
FLASH1_ADDR
_ENC_ERR_EN
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: Flash1 address encode error. In 
address decoding, if multiple or no address line is selected, FMU reports address encode error.
0b - No address encode error in flash1.
1b - Address encode error in flash1.
11
FLASH1_EDC_
ERR_EN
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: Flash1 ECC correction error 
through EDC reported by FMU.
0b - No EDC after ECC error reported in flash1.
1b - EDC after ECC error reported in flash1.
10
PF1_1_DATA_E
CC_ERR_EN
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: Flash3 data ECC uncorrectable 
error. The path is from FMU to PFLASH controller to ERM to FCCU.
0b - No uncorrectable error reported in flash controller port 3 data memory by FMU.
1b - Uncorrectable error reported in flash controller port 3 data memory by FMU.
9
PF1_1_CODE_
ECC_ERR_EN
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: Flash3 code ECC uncorrectable 
error. The path is from FMU to PFLASH controller to ERM to FCCU.
0b - No uncorrectable error reported in flash controller port 3 code memory by FMU.
1b - Uncorrectable error reported in flash controller port 3 code memory by FMU.
8
PF1_0_DATA_E
CC_ERR_EN
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: Flash2 data ECC uncorrectable 
error. The path is from FMU to PFLASH controller to ERM to FCCU.
0b - No uncorrectable error reported in flash controller port 2 data memory by FMU.
1b - Uncorrectable error reported in flash controller port 2 data memory by FMU.
7
Enable bit for enabling the fault monitoring at FCCU NCF 3 for the fault: Flash2 code ECC uncorrectable 
error. The path is from FMU to PFLASH controller to ERM to FCCU.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1427 / 5251


---
# 페이지 176

Table continued from the previous page...
Field
Function
PF1_0_CODE_
ECC_ERR_EN
0b - No uncorrectable error reported in flash controller port 2 code memory by FMU.
1b - Uncorrectable error reported in flash controller port 2 code memory by FMU.
6
AES_RESULT_
DID_SAFETY_
ERR_EN
Enables bit for enabling the fault monitoring at FCCU NCF 2 for the fault: AES RESULT DMA DID error.
0b - AES RESULT DMA DID error not enabled.
1b - AES RESULT DMA DID error enabled.
5
AES_FEED_DI
D_SAFETY_ER
R_EN
Enables bit for enabling the fault monitoring at FCCU NCF 2 for the fault: AES FEED DMA DID error.
0b - AES FEED DMA DID error not enabled.
1b - AES FEED DMA DID error enabled.
4
AES_KP_CRC_
SAFETY_ERR_
EN
Enables bit for enabling the fault monitoring at FCCU NCF 2 for the fault: AES Key Property CRC Safety 
Error.
0b - AES key-property CRC safety error not enabled.
1b - AES key-property CRC safety error enabled.
3
AES_RESULT_
DMA_TCD_AD
DR_ECC_ERR_
EN
Enables bit for enabling the fault monitoring at FCCU NCF 2 for the fault: AES ACCEL RESULT 
DMA_TCD address ECC error.
0b - No address error reported in AES ACCEL RESULT DMA_TCD memory.
1b - Address error reported in AES ACCEL RESULT DMA_TCD memory.
2
AES_RESULT_
DMA_TCD_EC
C_ERR_EN
Enables bit for enabling the fault monitoring at FCCU NCF 2 for the fault: AES ACCEL RESULT 
DMA_TCD memory uncorrectable ECC error.
0b - No uncorrectable error reported in AES ACCEL RESULT DMA_TCD memory.
1b - Uncorrectable error reported in AES ACCEL RESULT DMA_TCD memory.
1
AES_FEED_DM
A_TCD_ADDR_
ECC_ERR_EN
Enables bit for enabling the fault monitoring at FCCU NCF 2 for the fault: AES ACCEL FEED DMA_TCD 
address ECC error.
0b - No address error reported in AES ACCEL FEED DMA_TCD memory.
1b - Address error reported in AES ACCEL FEED DMA_TCD memory.
0
AES_FEED_DM
A_TCD_ECC_E
RR_EN
Enables bit for enabling the fault monitoring at FCCU NCF 2 for the fault: AES ACCEL FEED DMA_TCD 
memory uncorrectable ECC error.
0b - No uncorrectable error reported in AES ACCEL FEED DMA_TCD memory.
1b - Uncorrectable error reported in AES ACCEL FEED DMA_TCD memory.
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1428 / 5251


---
# 페이지 177

38.2.46 Read Write GPR On Destructive Reset 19 (DCMRWD19)
Offset
Register
Offset
DCMRWD19
548h
Function
This is a readable and writable general purpose register which gets reset on destructive reset.
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
SAI1_
DB...
SAI0_
DB...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEX
CAN...
FLEXI
O_...
LPI2C
1_...
LPI2C
0_...
LPSPI
5_...
LPSPI
4_...
LPSPI
3_...
LPSPI
2_...
LPSPI
1_...
W
Reset
0
0
0
0
0
0
0
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
LPSPI
0_...
PIT2_
DB...
PIT1_
DB...
PIT0_
DB...
STM1_
DB...
STM0_
DB...
SWT1
_DB...
SWT0
_DB...
RTC_
DBG...
eMIOS
2_...
eMIOS
1_...
eMIOS
0_...
LCU1_
DB...
LCU0_
DB...
FCCU
_DB...
EDMA
_DB...
W
Reset
0
0
0
0
0
0
0
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
SAI1_DBG_DIS
_CM7_3
Specifies whether SAI1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - SAI1 enters debug mode when CM7_3 enters debug mode.
1b - SAI1 remains functional and is not impacted when CM7_3 enters debug mode.
30
SAI0_DBG_DIS
_CM7_3
Specifies whether SAI0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - SAI0 enters debug mode when CM7_3 enters debug mode.
1b - SAI0 remains functional and is not impacted when CM7_3 enters debug mode.
29
FLEXCAN5_DB
G_DIS_CM7_3
FlexCAN5 Debug Disable For Cortex-M7_3
Specifies whether FlexCAN5 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - FlexCAN5 enters debug mode when CM7_3 enters debug mode.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1429 / 5251


---
# 페이지 178

Table continued from the previous page...
Field
Function
1b - FlexCAN5 remains functional and is not impacted when CM7_3 enters debug mode.
28
FLEXCAN4_DB
G_DIS_CM7_3
FlexCAN4 Debug Disable For Cortex-M7_3
Specifies whether FlexCAN4 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - FlexCAN4 enters debug mode when CM7_3 enters debug mode.
1b - FlexCAN4 remains functional and is not impacted when CM7_3 enters debug mode.
27
FLEXCAN3_DB
G_DIS_CM7_3
FlexCAN3 Debug Disable For Cortex-M7_3
Specifies whether FlexCAN3 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - FlexCAN3 enters debug mode when CM7_3 enters debug mode.
1b - FlexCAN3 remains functional and is not impacted when CM7_3 enters debug mode.
26
FLEXCAN2_DB
G_DIS_CM7_3
FlexCAN2 Debug Disable For Cortex-M7_3
Specifies whether FlexCAN2 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - FlexCAN2 enters debug mode when CM7_3 enters debug mode.
1b - FlexCAN2 remains functional and is not impacted when CM7_3 enters debug mode.
25
FLEXCAN1_DB
G_DIS_CM7_3
FlexCAN1 Debug Disable For Cortex-M7_3
Specifies whether FlexCAN1 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - FlexCAN1 enters debug mode when CM7_3 enters debug mode.
1b - FlexCAN1 remains functional and is not impacted when CM7_3 enters debug mode.
24
FLEXCAN0_DB
G_DIS_CM7_3
FlexCAN0 Debug Disable For Cortex-M7_3
Specifies whether FlexCAN0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - FlexCAN0 enters debug mode when CM7_3 enters debug mode.
1b - FlexCAN0 remains functional and is not impacted when CM7_3 enters debug mode.
23
FlexIO Debug Disable For Cortex-M7_3
Specifies whether FlexIO enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1430 / 5251


---
# 페이지 179

Table continued from the previous page...
Field
Function
FLEXIO_DBG_
DIS_CM7_3
Write 1 to this field to disable debug.
0b - FlexIO enters debug mode when CM7_3 enters debug mode.
1b - FlexIO remains functional and is not impacted when CM7_3 enters debug mode.
22
LPI2C1_DBG_D
IS_CM7_3
LPI2C1 Debug Disable For Cortex-M7_3
Specifies whether LPI2C1 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - LPI2C1 enters debug mode when CM7_3 enters debug mode.
1b - LPI2C1 remains functional and is not impacted when CM7_3 enters debug mode.
21
LPI2C0_DBG_D
IS_CM7_3
LPI2C0 Debug Disable For Cortex-M7_3
Specifies whether LPI2C0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - LPI2C0 enters debug mode when CM7_3 enters debug mode.
1b - LPI2C0 remains functional and is not impacted when CM7_3 enters debug mode.
20
LPSPI5_DBG_
DIS_CM7_3
LPSPI5 Debug Disable For Cortex-M7_3
Specifies whether LPSPI5 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - LPSPI5 enters debug mode when CM7_3 enters debug mode.
1b - LPSPI5 remains functional and is not impacted when CM7_3 enters debug mode.
19
LPSPI4_DBG_
DIS_CM7_3
LPSPI4 Debug Disable For Cortex-M7_3
Specifies whether LPSPI4 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - LPSPI4 enters debug mode when CM7_3 enters debug mode.
1b - LPSPI4 remains functional and is not impacted when CM7_3 enters debug mode.
18
LPSPI3_DBG_
DIS_CM7_3
LPSPI3 Debug Disable For Cortex-M7_3
Specifies whether LPSPI3 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - LPSPI3 enters debug mode when CM7_3 enters debug mode.
1b - LPSPI3 remains functional and is not impacted when CM7_3 enters debug mode.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1431 / 5251


---
# 페이지 180

Table continued from the previous page...
Field
Function
17
LPSPI2_DBG_
DIS_CM7_3
LPSPI2 Debug Disable For Cortex-M7_3
Specifies whether LPSPI2 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - LPSPI2 enters debug mode when CM7_3 enters debug mode.
1b - LPSPI2 remains functional and is not impacted when CM7_3 enters debug mode.
16
LPSPI1_DBG_
DIS_CM7_3
LPSPI1 Debug Disable For Cortex-M7_3
Specifies whether LPSPI1 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - LPSPI1 enters debug mode when CM7_3 enters debug mode.
1b - LPSPI1 remains functional and is not impacted when CM7_3 enters debug mode.
15
LPSPI0_DBG_
DIS_CM7_3
LPSPI0 Debug Disable For Cortex-M7_3
Specifies whether LPSPI0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - LPSPI0 enters debug mode when CM7_3 enters debug mode.
1b - LPSPI0 remains functional and is not impacted when CM7_3 enters debug mode.
14
PIT2_DBG_DIS
_CM7_3
PIT2 Debug Disable For Cortex-M7_3
Specifies whether PIT2 enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - PIT2 enters debug mode when CM7_3 enters debug mode.
1b - PIT2 remains functional and is not impacted when CM7_3 enters debug mode.
13
PIT1_DBG_DIS
_CM7_3
PIT1 Debug Disable For Cortex-M7_3
Specifies whether PIT1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - PIT1 enters debug mode when CM7_3 enters debug mode.
1b - PIT1 remains functional and is not impacted when CM7_3 enters debug mode.
12
PIT0_DBG_DIS
_CM7_3
PIT0 Debug Disable For Cortex-M7_3
Specifies whether PIT0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode.
Write 1 to this field to disable debug.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1432 / 5251


---
# 페이지 181

Table continued from the previous page...
Field
Function
0b - PIT0 enters debug mode when CM7_3 enters debug mode.
1b - PIT0 remains functional and is not impacted when CM7_3 enters debug mode.
11
STM1_DBG_DI
S_CM7_3
STM1 Debug Disable For Cortex-M7_3
Specifies whether STM1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - STM1 enters debug mode when CM7_3 enters debug mode.
1b - STM1 remains functional and is not impacted when CM7_3 enters debug mode.
10
STM0_DBG_DI
S_CM7_3
STM0 Debug Disable For Cortex-M7_3
Specifies whether STM0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - STM0 enters debug mode when CM7_3 enters debug mode.
1b - STM0 remains functional and is not impacted when CM7_3 enters debug mode.
9
SWT1_DBG_DI
S_CM7_3
SWT1 Debug Disable For Cortex-M7_3
Specifies whether SWT1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - SWT1 enters debug mode when CM7_3 enters debug mode.
1b - SWT1 remains functional and is not impacted when CM7_3 enters debug mode.
8
SWT0_DBG_DI
S_CM7_3
SWT0 Debug Disable For Cortex-M7_3
Specifies whether SWT0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - SWT0 enters debug mode when CM7_3 enters debug mode.
1b - SWT0 remains functional and is not impacted when CM7_3 enters debug mode.
7
RTC_DBG_DIS
_CM7_3
RTC Debug Disable For Cortex-M7_3
Specifies whether RTC enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - RTC enters debug mode when CM7_3 enters debug mode.
1b - RTC remains functional and is not impacted when CM7_3 enters debug mode.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1433 / 5251


---
# 페이지 182

Table continued from the previous page...
Field
Function
6
eMIOS2_DBG_
DIS_CM7_3
Specifies whether eMIOS2 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - eMIOS2 enters debug mode when CM7_3 enters debug mode.
1b - eMIOS2 remains functional and is not impacted when CM7_3 enters debug mode.
5
eMIOS1_DBG_
DIS_CM7_3
Specifies whether eMIOS1 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - eMIOS1 enters debug mode when CM7_3 enters debug mode.
1b - eMIOS1 remains functional and is not impacted when CM7_3 enters debug mode.
4
eMIOS0_DBG_
DIS_CM7_3
eMIOS0 Debug Disable For Cortex-M7_3
Specifies whether eMIOS0 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - eMIOS0 enters debug mode when CM7_3 enters debug mode.
1b - eMIOS0 remains functional and is not impacted when CM7_3 enters debug mode.
3
LCU1_DBG_DI
S_CM7_3
LCU1 Debug Disable For Cortex-M7_3
Specifies whether LCU1 enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode. If this field = 0, LCU1 enters Debug mode, and if this field = 1, LCU1 
remains functional.
Write 1 to this field to disable debug.
0b - LCU1 enters debug mode when CM7_3 enters debug mode.
1b - LCU1 remains functional and is not impacted when CM7_3 enters debug mode.
2
LCU0_DBG_DI
S_CM7_3
LCU0 Debug Disable For Cortex-M7_3
Specifies whether LCU0 enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode. If this field = 0, LCU0 enters Debug mode, and if this field = 1, LCU0 
remains functional.
Write 1 to this field to disable debug.
0b - LCU0 enters debug mode when CM7_3 enters debug mode.
1b - LCU0 remains functional and is not impacted when CM7_3 enters debug mode.
1
FCCU_DBG_DI
S_CM7_3
FCCU Debug Disable For Cortex-M7_3
Specifies whether FCCU enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode. If this field = 0, FCCU enters Debug mode, and if this field = 1, FCCU 
remains functional.
Write 1 to this field to disable debug.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1434 / 5251


---
# 페이지 183

Table continued from the previous page...
Field
Function
0b - FCCU enters debug mode when CM7_3 enters debug mode.
1b - FCCU remains functional and is not impacted when CM7_3 enters debug mode.
0
EDMA_DBG_DI
S_CM7_3
EDMA Debug Disable For Cortex-M7_3
Specifies whether eDMA enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode. If this field = 0, eDMA enters Debug mode, and if this field = 1, eDMA 
remains functional.
Write 1 to this field to disable debug.
0b - EDMA enters debug mode when CM7_3 enters debug mode.
1b - EDMA remains functional and is not impacted when CM7_3 enters debug mode.
38.2.47 Read Write GPR On Destructive Reset 20 (DCMRWD20)
Offset
Register
Offset
DCMRWD20
54Ch
Function
This is a readable and writable general purpose register which gets reset on destructive reset.
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
FLEXC
AN...
FLEXC
AN...
FLEXC
AN...
FLEXC
AN...
PIT3_
DB...
STM3_
DB...
SWT3
_DB...
Reserved 
W
Reset
0
0
0
0
0
0
0
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
SWT2
_DB...
STM2_
DB...
FLEXC
AN...
FLEXC
AN...
Reserv
ed 
W
Reset
0
0
0
0
0
0
0
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
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1435 / 5251


---
# 페이지 184

Table continued from the previous page...
Field
Function
27
FLEXCAN11_D
BG_DIS_CM7_
3
FLEXCAN11 Debug Disable Cortex-M7_3
FLEXCAN11 debug disable bit for CM7_3. Set this bit 1 to disable the debug of module.
0b - FLEXCAN11 enters debug mode when CM7_3 enters debug mode.
1b - FLEXCAN11 remains functional and is not impacted when CM7_3 enters debug mode.
26
FLEXCAN10_D
BG_DIS_CM7_
3
FLEXCAN10 Debug Disable Cortex-M7_3
FLEXCAN10 debug disable bit for CM7_3. Set this bit 1 to disable the debug of module.
0b - FLEXCAN10 enters debug mode when CM7_3 enters debug mode.
1b - FLEXCAN10 remains functional and is not impacted when CM7_3 enters debug mode.
25
FLEXCAN9_DB
G_DIS_CM7_3
FLEXCAN9 Debug Disable Cortex-M7_3
FLEXCAN9 debug disable bit for CM7_3. Set this bit 1 to disable the debug of module.
0b - FLEXCAN9 enters debug mode when CM7_3 enters debug mode.
1b - FLEXCAN9 remains functional and is not impacted when CM7_3 enters debug mode.
24
FLEXCAN8_DB
G_DIS_CM7_3
FLEXCAN8 Debug Disable Cortex-M7_3
FLEXCAN8 debug disable bit for CM7_3. Set this bit 1 to disable the debug of module.
0b - FLEXCAN8 enters debug mode when CM7_3 enters debug mode.
1b - FLEXCAN8 remains functional and is not impacted when CM7_3 enters debug mode.
23
PIT3_DBG_DIS
_CM7_3
PIT3 Debug Disable Cortex-M7_3
Specifies whether PIT3 enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - PIT3 enters debug mode when CM7_3 enters debug mode.
1b - PIT3 remains functional and is not impacted when CM7_3 enters debug mode.
22
STM3_DBG_DI
S_CM7_3
STM3 Debug Disable Cortex-M7_3
Specifies whether STM3 enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - STM3 enters debug mode when CM7_3 enters debug mode.
1b - STM3 remains functional and is not impacted when CM7_3 enters debug mode.
21
SWT3_DBG_DI
S_CM7_3
SWT3 Debug Disable Cortex-M7_3
Specifies whether SWT3 enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode.
Write 1 to this field to disable debug.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1436 / 5251


---
# 페이지 185

Table continued from the previous page...
Field
Function
0b - SWT3 enters debug mode when CM7_3 enters debug mode.
1b - SWT3 remains functional and is not impacted when CM7_3 enters debug mode.
20-5
—
Reserved
4
SWT2_DBG_DI
S_CM7_3
SWT2 Debug Disable For Cortex-M7_3
Specifies whether SWT2 enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - SWT2 enters debug mode when CM7_3 enters debug mode.
1b - SWT2 remains functional and is not impacted when CM7_3 enters debug mode.
3
STM2_DBG_DI
S_CM7_3
STM2 Debug Disable For Cortex-M7_3
Specifies whether STM2 enters Debug mode or remains functional and unimpacted when the Cortex-M7_3 
core enters Debug mode.
Write 1 to this field to disable debug.
0b - STM2 enters debug mode when CM7_3 enters debug mode.
1b - STM2 remains functional and is not impacted when CM7_3 enters debug mode.
2
FLEXCAN7_DB
G_DIS_CM7_3
Specifies whether FLEXCAN7 enters Debug mode or remains functional and unimpacted when the 
Cortex-M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - FLEXCAN7 enters debug mode when CM7_3 enters debug mode.
1b - FLEXCAN7 remains functional and is not impacted when CM7_3 enters debug mode.
1
FLEXCAN6_DB
G_DIS_CM7_3
FlexCAN6 Debug Disable For Cortex-M7_3
Specifies whether FlexCAN6 enters Debug mode or remains functional and unimpacted when the Cortex-
M7_3 core enters Debug mode.
Write 1 to this field to disable debug.
0b - FlexCAN6 enters debug mode when CM7_3 enters debug mode.
1b - FlexCAN6 remains functional and is not impacted when CM7_3 enters debug mode.
0
—
Reserved
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1437 / 5251


---
# 페이지 186

38.2.48 Read Write GPR On Functional Reset 1 (DCMRWF1)
Offset
Register
Offset
DCMRWF1
600h
Function
Contains information related to:
• Voltage dividers, LFAST clocks, and supply voltage monitoring.
• I/O configurations.
This field resets after functional reset 1.
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
MAC_
TX_...
Reserved 
VDD_1
_5...
VDD_
HV_...
VDD_
HV_...
VSS_L
V_...
SUPPLY_MON_SEL 
SUPP
LY_...
MAC_
SB_...
PMIC_
PG...
Reserv
ed 
STAN
DBY...
W
Reset
0
0
0
0
0
0
0
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
VDD_
HV_...
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
MAC_CONF_S
EL 
FCCU
_SW...
FCCU
_SW...
FCCU
_SW...
FCCU
_SW...
CAN_
TIM...
CAN_
TIM...
W
Reset
0
0
0
0
0
0
0
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
MAC_TX_RMII_
CLK_LPBCK_E
N
MAC_TX_RMII_CLK Loopback Enable
Enables the MAC_TX_RMII_CLK loopback.
0b - Disables
1b - Enables
30-28
—
Reserved
27
VDD_1_5_VLT_
DVDR_EN
VDD1P5 Voltage Divider Enable
Enables the VDD1P5 2:1 divider for voltage measurement using the supply voltage that ADC monitors.
0b - Disables
1b - Enables
26
VDD_HV_B Voltage Divider Enable
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1438 / 5251


---
# 페이지 187

Table continued from the previous page...
Field
Function
VDD_HV_B_VL
T_DVDR_EN
Enables the VDD_HV_B 2:1 divider for voltage measurement by using the supply voltage that ADC 
monitors.
0b - Disables
1b - Enables
25
VDD_HV_A_VL
T_DVDR_EN
VDD_HV_A Voltage Divider Enable
Enables the VDD_HV_A 2:1 divider for voltage measurement by using supply voltage that ADC monitors.
0b - Disables
1b - Enables
24
VSS_LV_ANMU
X_EN
VSS_LV Monitoring Enable
Enables VSS_LV monitoring.
 
You must write 1 to this field (with DCMRWF1[SUPPLY_MON_EN] = 1b0 for VSS_LV 
monitoring by ADC0).
  NOTE  
0b - Disables
1b - Enables
23-21
SUPPLY_MON
_SEL
Supply Monitoring Select
Selects the source of voltage that ADC uses for supply monitoring.
 
• The SUPPLY_MON_SEL configurations are effective only when SUPPLY_MON_EN 
is 1.
• When SUPPLY_MON_EN is 0 and VSS_LV_ANMUX_EN is 1, VSS_LV is monitored.
  NOTE  
000b - VDD_HV_A_DIV
001b - VDD_HV_B_DIV
010b - VDD_1.5_DIV
011b - VDD_2.5_OSC
100b - VDD1.1_PD1_HOT_POINT
101b - VDD1.1_PD1_COLD_POINT
110b - VDD1.1_PLL
111b - VDD1.1_PD0
20
SUPPLY_MON
_EN
Supply Monitoring Enable
Enables the ADC supply voltage monitoring.
0b - Disables
1b - Enables
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1439 / 5251


---
# 페이지 188

Table continued from the previous page...
Field
Function
19
MAC_SB_END_
CTRL
MAC Sideband Data Endianness Control
0b - The MAC sideband data is transferred in little-endian mode.
1b - The MAC sideband data is transferred in big-endian mode.
18
PMIC_PGOOD_
HNDSHK_BYP
Controls the PMIC_PGOOD handshake with the external Power Management IC (PMIC) while standby 
exit.
0b - The standby exit proceeds only when the active edge (as per 
DCMRWF2[PGOOD_POLARITY] configuration) is detected on the PGOOD signal.
1b - The PMIC_PGOOD handshake with the PMIC is bypassed.
17
—
Reserved
16
STANDBY_IO_
CONFIG
Standby I/O Configuration
Controls the IO state in the standby mode. This bit needs to be written both at the standby entry as well 
as standby exit as per the below description.
0b - Must be written as 0 before IO configurations are done in standby entry sequence.
1b - Must be written as 1 after IO configurations are done on standby exit.
15
VDD_HV_B_IO_
CTRL_LATCH
VDD_HV_B I/O Control Latch
Controls the IO controls (SRC, DSE, PKE, PUS, PUE, IBE and OBE) latching in low frequency RUN 
mode to reduce power consumption on VDD_HV_B domain pins. The pad output path is functional as 
usual.
 
This field must remain 0, except in FIRC 3 MHz and FIRC 187.5 kHz operation modes.
  NOTE  
0b - VDD_HV_B domain pins function as normal.
1b - The IO controls of VDD_HV_B domain pins are latched.
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
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1440 / 5251


---
# 페이지 189

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
7-6
MAC_CONF_S
EL
Selects between MII and RMII mode of ethernet.
00b - MII mode
01b - RGMII mode
10b - RMII mode
11b - Reserved
5
FCCU_SW_NC
F3
FCCU Software NCF 3
Specifies whether NCF 3 to FCCU is generated. For the exact FCCU slot, see the "Fault Collection and 
Control Unit (FCCU)" chapter.
0b - Not generated
1b - Generated
4
FCCU_SW_NC
F2
FCCU Software NCF 2
Specifies whether NCF 2 to FCCU is generated. For the exact FCCU slot, see the "Fault Collection and 
Control Unit (FCCU)" chapter.
0b - Not generated
1b - Generated
3
FCCU_SW_NC
F1
FCCU Software NCF 1
Specifies whether NCF 1 to FCCU is generated. For the exact FCCU slot, see the "Fault Collection and 
Control Unit (FCCU)" chapter.
0b - Not generated
1b - Generated
2
FCCU_SW_NC
F0
FCCU Software NCF 0
Specifies whether NCF0 to FCCU is generated. For the exact FCCU slot, see the "Fault Collection and 
Control Unit (FCCU)" chapter.
0b - Not generated
1b - Generated
1
CAN_TIMESTA
MP_EN
FlexCAN Timestamp Enable
Enables the FlexCAN timestamping feature.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1441 / 5251


---
# 페이지 190

Table continued from the previous page...
Field
Function
0b - Disables
1b - Enables
0
CAN_TIMESTA
MP_SEL
FlexCAN Timestamp Select
Selects either EMAC or STM for FlexCAN timestamping.
0b - EMAC
1b - STM0
38.2.49 Read Write GPR On Functional Reset 2 (DCMRWF2)
Offset
Register
Offset
DCMRWF2
604h
Function
Contains information related to:
• WKPU source select.
• PGOOD polarity.
• HSE_B gasket bypass.
• Bypass standby exit.
This register resets after functional reset 2.
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
WKPU
8_S...
WKPU
45_...
WKPU
27_...
WKPU
18_...
WKPU
15_...
WKPU
14_...
WKPU
0_S...
PLL1_
LO...
Reserved 
PGOO
D_P...
Reserv
ed 
Reserv
ed 
Reserv
ed 
VIRT_
WR...
HSE_
GSK...
W
Reset
0
0
0
0
0
0
0
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
SUPPLY2_MON_SEL 
SUPP
LY2...
SAI_M
CL...
MAC_TX_RX_C
LK_M...
PMOS
_CT...
Reserved 
PMC_
TRI...
FIRC_
TR...
DCM_
SCA...
MAC2
_LO...
MAC2
_TX...
Reserv
ed 
W
Reset
0
0
0
0
0
0
0
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
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1442 / 5251


---
# 페이지 191

Fields
Field
Function
31
WKPU8_SRC_
SELECT
WKPU[8] Source Select
Controls and specifies the source of WKPU[8].
0b - GPIO[34]
1b - GPIO[231]
30
WKPU45_SRC_
SELECT
WKPU[45] Source Select
Controls and specifies the source of WKPU[45].
0b - GPIO[89]
1b - GPIO[217]
29
WKPU27_SRC_
SELECT
WKPU[27] Source Select
Controls and specifies the source of WKPU[27].
0b - GPIO[130]
1b - GPIO[233]
28
WKPU18_SRC_
SELECT
WKPU[18] Source Select
Controls and specifies the source of WKPU[18].
0b - GPIO[75]
1b - GPIO[235]
27
WKPU15_SRC_
SELECT
Controls the source of WKPU[15].
0b - GPIO[6] is used as source of WKPU[15].
1b - GPIO[227] is used as source of WKPU[15].
26
WKPU14_SRC_
SELECT
Controls the source of WKPU[14].
0b - GPIO[49] is used as source of WKPU[14].
1b - GPIO[229] is used as source of WKPU[14].
25
WKPU0_SRC_
SELECT
Controls the source of WKPU[0].
0b - GPIO[2] is used as source of WKPU[0].
1b - GPIO[225] is used as source of WKPU[0].
24
PLL1_LOL_RST
_EN
PLL1 LOL Reset Enable
Controls the functional reset or interrupt behavior of the PLL1 LOL event.
0b - PLL1 LOL event results in an interrupt
1b - PLL1 LOL event results in a reset
23-22
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1443 / 5251


---
# 페이지 192

Table continued from the previous page...
Field
Function
21
PGOOD_POLA
RITY
PGOOD Signal Edge Polarity
See the PMIC documentation before performing this configuration.
 
PGOOD_POLARITY configuration is valid only if PMIC_PGOOD_HNDSHK_BYP is set 
as 1'0b.
  NOTE  
0b - Rising egde. PGOOD signal is considered active while it sees a transitioning edge from 
active low state to active high state.
1b - Falling egde. PGOOD signal is considered active while it sees a transitioning edge from 
active high state to active low state.
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
VIRT_WRAP_IP
SYNC_BYPAS
S
VIRT_WRAPPER IPSYNC Bypass
Bypasses the VIRT_WRAPPER IPSYNC.
 
The VIRT_WRAPPER IPSYNC can alternatively also be bypassed using 
UTEST_MISC[12]. See UTEST client description for details.
  NOTE  
0b - Enables
1b - Bypasses
16
HSE_GSKT_BY
PASS
HSE_B Gasket Bypass
Enables the HSE_B IAHB gasket behavior out of Standby mode.
• If you write 0 to this field, the DCF client controls the HSE_B IAHB gasket bypass configuration. The 
system must continue to run on FIRC, and if intended to run on PLL, a functional reset must be 
asserted.
• If you write 1 to this field, the HSE_B IAHB gasket is bypassed out of standby.
0b - Not bypassed
1b - Bypassed
15-13
SUPPLY2_MO
N_SEL
Supply 2 Monitoring Select
Selects the source of voltage that ADC uses for supply monitoring.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1444 / 5251


---
# 페이지 193

Table continued from the previous page...
Field
Function
 
The SUPPLY2_MON_SEL configurations are effective only when SUPPLY2_MON_EN is 1.
  NOTE  
000b - VDD2P5_PLL2
001b - VDD1P1_PLL2
010b - Reserved
011b - Reserved
12
SUPPLY2_MO
N_EN
Supply 2 Monitoring Enable
Enables supply voltage that ADC monitors to makes use of another ANAMUX.
0b - Disables
1b - Enables
11
SAI_MCLK2_S
EL
SAI MCLK2 Select
Controls the SAI_MCLK2 clk source.
0b - FXOSC is the SAI_MCLK2 clock source.
1b - PLL_AUX_PHI1 is the SAI_MCLK2 clock source.
10-9
MAC_TX_RX_C
LK_MUX_BYPA
SS
MAC TX RX CLK MUX BYPASS
Bypasses the MAC_TX_CLK and MAC_RX_CLK sources depending on DCMRWF3[15:13] configuration.
00b - The MAC_RX_CLK in the configuration if DCMRWF3[14:13] is 2'b00 is derived from 
MC_CGM_MUX7. The MAC_TX_CLK in the configuration if DCMRWF3[15] is 1'b0 is derived 
from MC_CGM_MUX8.
01b - The MAC_RX_CLK in the configuration if DCMRWF3[14:13] is 2'b00 is derived from 
RMII_CLK DIV2. The MAC_TX_CLK in the configuration if DCMRWF3[15] is 1'b0 is derived from 
RMII_CLK DIV2.
10b - The MAC_RX_CLK in the configuration if DCMRWF3[14:13] is 2'b00 is derived from 
RMII_CLK DIV20. The MAC_TX_CLK in the configuration if DCMRWF3[15] is 1'b0 is derived 
from RMII_CLK DIV20.
11b - The MAC_RX_CLK in the configuration if DCMRWF3[14:13] is 2'b00 is inactive/disabled. 
The MAC_TX_CLK in the configuration if DCMRWF3[15] is 1'b0 is inactive/disabled.
8
PMOS_CTRL_
GPIO_DATA
PMOS Control GPIO Data
Controls the data-out from the PMOS_CTRL pad when PMC.CONFIG[LMSMPSEN] is 0. 
PMOS_CTRL_GPIO_DATA is not impacted if PMC.CONFIG[LMSMPSEN] is 1.
0b - Data is 0
1b - Data is 1
7-6
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1445 / 5251


---
# 페이지 194

Table continued from the previous page...
Field
Function
5
PMC_TRIM_RG
M_DCF_BYP_S
TDBY_EXT
PMC Trim MC_RGM DCF Bypass Standby Exit
Controls the bypassing of PMC trimming and MC_RGM loading on standby exit.
0b - Not bypassed
1b - Bypassed
4
FIRC_TRIM_BY
P_STDBY_EXT
FIRC Trim Bypass Standby Exit
Controls the bypassing of FIRC trimming on standby exit.
0b - Not bypassed
1b - Bypassed
3
DCM_SCAN_B
YP_STDBY_EX
T
DCM Scan Bypass Standby Exit
Controls the bypassing of DCM scanning on standby exit.
0b - Not bypassed
1b - Bypassed
2
MAC2_LOOBP
ACK_CLK_SEL
Selects MAC2_LOOPBACK_CLK source.
0b - Reserved
1b - MAC_CLK_TX is selected.
1
MAC2_TX_RMII
_CLK_LPBCK_
EN
Enables the MAC2_TX_RMII_CLK loopback.
0b - Disabled
1b - Enabled
0
—
Reserved
38.2.50 Read Write GPR On Functional Reset 3 (DCMRWF3)
Offset
Register
Offset
DCMRWF3
608h
Function
Controls and specifies sources of WKPU.
This register resets after functional reset 3.
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1446 / 5251


---
# 페이지 195

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
Reserv
ed 
Reserved 
Reserved 
Reserved 
W
Reset
0
0
0
0
0
0
0
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
MAC_
TX_...
MAC_RX_CLK_
MUX_...
Reserved 
W
Reset
0
0
0
0
0
0
0
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
27
—
Reserved
26-24
—
Reserved
23-22
—
Reserved
21-16
—
Reserved
15
MAC_TX_CLK_
MUX_BYPASS
MAC TX Clock MUX Bypass
Bypasses the MAC_TX_CLK mux MC_CGM_MUX8 and the TX_CLK arrives without MC_CGM_MUX8 to 
the MAC in case of external clock source.
 
The MAC_RX_CLK in this configuration is derived based on 
DCMRWF2[10:9] configuration.
  NOTE  
0b - The MAC_TX_CLK is derived from MC_CGM_MUX8.
1b - The MAC_TX_CLK arrives directly from the RMII_TX_CLK pin.
14-13
MAC_RX_CLK_
MUX_BYPASS
MAC RX Clock MUX Bypass
Bypasses the MAC_RX_CLK mux MC_CGM_MUX7 and the RX_CLK arrives without MC_CGM_MUX7 
to the MAC in case of external clock source.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1447 / 5251


---
# 페이지 196

Table continued from the previous page...
Field
Function
 
The MAC_RX_CLK in this configuration is derived based on 
DCMRWF2[10:9] configuration.
  NOTE  
00b - The MAC_RX_CLK is derived from MC_CGM_MUX7.
01b - The MAC_RX_CLK arrives directly from the RX_CLK pin.
10b - The MAC_RX_CLK arrives directly from the RMII_TX_CLK pin. RESERVED for S32K388 
and S32K389.
11b - Reserved
12-0
—
Reserved
38.2.51 Read Write GPR On Functional Reset 4 (DCMRWF4)
Offset
Register
Offset
DCMRWF4
60Ch
Function
Contains information related to:
• Mux mode enable.
• Input bypass.
This field resets after functional reset 4.
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
MAC2
_TX...
MAC2_RX_CLK
_MUX...
Reserv
ed 
MAC2
_RM...
MAC_
RMI...
MAC2_CONF_
SEL 
MAC_
SB_...
MAC2_TX_RX_
CLK_...
CM7_3
_C...
CM7_2
_C...
CM7_1
_C...
CM7_0
_C...
GLITC
H_...
W
Reset
0
0
0
0
0
0
0
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
GLITC
H_...
GLITC
H_...
GLITC
H_...
Reserved 
MUX_
MOD...
MUX_
MOD...
Reserved 
MUX_
MOD...
MUX_
MOD...
MUX_
MOD...
MUX_
MOD...
MUX_
MOD...
MUX_
MOD...
Reserv
ed 
W
Reset
0
0
0
0
0
0
0
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
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1448 / 5251


---
# 페이지 197

Fields
Field
Function
31
MAC2_TX_CLK
_MUX_BYPASS
MAC2 TX Clock Mux Bypass
Bypasses the MAC2_TX_CLK mux MC_CGM_MUX16 and the TX_CLK arrives without 
MC_CGM_MUX16 to the MAC2 in case of external clock source.
 
The MAC2_TX_CLK in this configuration is derived based on 
DCMRWF4[22:21] configuration.
  NOTE  
0b - The MAC2_TX_CLK is derived from MC_CGM_MUX16.
1b - The MAC2_TX_CLK arrives directly from the RMII_TX_CLK pin.
30-29
MAC2_RX_CLK
_MUX_BYPASS
MAC2 RX Clock Mux Bypass
Bypasses the MAC2_RX_CLK mux MC_CGM_MUX15 and the RX_CLK arrives without 
MC_CGM_MUX15 to the MAC2 in case of external clock source.
 
The MAC2_RX_CLK in this configuration is derived based on 
DCMRWF4[22:21] configuration.
  NOTE  
00b - The MAC2_RX_CLK is derived from MC_CGM_MUX15.
01b - The MAC2_RX_CLK arrives directly from the MAC RX_CLK pin.
10b - The MAC2_RX_CLK arrives directly from the MAC2 RMII_TX_CLK pin.
11b - Reserved.
28
—
Reserved
27
MAC2_RMII_CL
K_MUX_BYPAS
S
MAC2 RMII Clock Mux Bypass
Bypasses MAC2_RMII_CLK mux MC_CGM_MUX16 and RMII_CLK arrives without MC_CGM_MUX16 to 
the MAC2 in case of external clock source.
0b - The MAC2_RMII_CLK is derived from MC_CGM_MUX16.
1b - The MAC2_RMII_CLK arrives directly from the RMII2_TX_CLK pin.
26
MAC_RMII_CL
K_MUX_BYPAS
S
MAC RMII Clock Mux Bypass
Bypasses MAC_RMII_CLK mux MC_CGM_MUX8 and RMII_CLK arrives without MC_CGM_MUX8 to the 
MAC in case of external clock source.
0b - The MAC_RMII_CLK is derived from MC_CGM_MUX8.
1b - The MAC_RMII_CLK arrives directly from the RMII_TX_CLK pin.
25-24
MAC2_CONF_
SEL
MAC Configuration Selection
Selects between MII and RMII mode of ethernet.
00b - MII mode
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1449 / 5251


---
# 페이지 198

Table continued from the previous page...
Field
Function
01b - RGMII mode
10b - RMII mode
11b - Reserved. Device operation not guaranteed.
23
MAC_SB_END_
CTRL
MAC Sideband Data Endianness Control
0b - Data is transferred in little-endian mode.
1b - Data is transferred in big-endian mode.
22-21
MAC2_TX_RX_
CLK_MUX_BYP
ASS
MAC2 TX RX Clock MUX Bypass
Bypasses the MAC2_TX_CLK and MAC2_RX_CLK sources depending on DCMRWF4[31:29] 
configuration.
00b - The MAC2_RX_CLK in the configuration if DCMRWF4[30:29] is 2'b00 is derived from 
MC_CGM_MUX7. The MAC2_TX_CLK in the configuration if DCMRWF4[31] is 1'b0 is derived 
from MC_CGM_MUX8.
01b - The MAC2_RX_CLK in the configuration if DCMRWF4[30:29] is 2'b00 is derived from 
RMII_CLK DIV2. The MAC2_TX_CLK in the configuration if DCMRWF4[31] is 1'b0 is derived from 
RMII_CLK DIV2.
10b - The MAC2_RX_CLK in the configuration if DCMRWF4[30:29] is 2'b00 is derived from 
RMII_CLK DIV20. The MAC2_TX_CLK in the configuration if DCMRWF4[31] is 1'b0 is derived 
from RMII_CLK DIV20.
11b - The MAC2_RX_CLK in the configuration if DCMRWF4[30:29] is 2'b00 is inactive/disabled. 
The MAC2_TX_CLK in the configuration if DCMRWF4[31] is 1'b0 is inactive/disabled.
20
CM7_3_CPUW
AIT
Cortex-M7_3 CPU Wait
Enables the configuration to place the Cortex-M7_3 core into CPU wait mode.
0b - Disables CPUWAIT
1b - Enables CPUWAIT
19
CM7_2_CPUW
AIT
Cortex-M7_2 CPU Wait
Enables the configuration to place the Cortex-M7_2 core into CPU wait mode.
0b - Disables CPUWAIT
1b - Enables CPUWAIT
18
CM7_1_CPUW
AIT
Cortex-M7_1 CPU Wait
Enables the configuration to place the Cortex-M7_1 core into CPU wait mode.
0b - Disables CPUWAIT
1b - Enables CPUWAIT
17
Cortex-M7_0 CPU Wait
Enables the configuration to place the Cortex-M7_0 core in CPU wait mode.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1450 / 5251


---
# 페이지 199

Table continued from the previous page...
Field
Function
CM7_0_CPUW
AIT
0b - Disables CPUWAIT
1b - Enables CPUWAIT
16
GLITCH_FIL_T
RG_IN3_BYP
Glitch Filter TRGMUX Input 3 Bypass
Selects whether to bypass or filter out the pulse. If this field = 0, it enables glitch filter on TRGMUX input 
60, and if the field = 1, it bypasses glitch filter on TRGMUX input 60.
0b - Enables
1b - Bypasses
15
GLITCH_FIL_T
RG_IN2_BYP
Glitch Filter TRGMUX Input 2 Bypass
Selects whether to bypass or filter out the pulse. If this field = 0, it enables glitch filter on TRGMUX input 
61, and if the field = 1, it bypasses glitch filter on TRGMUX input 61.
0b - Enables
1b - Bypasses
14
GLITCH_FIL_T
RG_IN1_BYP
Glitch Filter TRGMUX Input 1 Bypass
Selects whether to bypass or filter out the pulse. If this field = 0, it enables glitch filter on TRGMUX input 
62, and if the field = 1, it bypasses glitch filter on TRGMUX input 62.
0b - Enables
1b - Bypasses
13
GLITCH_FIL_T
RG_IN0_BYP
Glitch Filter TRGMUX Input 0 Bypass
Selects whether to bypass or filter out the pulse. If this field = 0, it enables glitch filter on TRGMUX input 
63, and if the field = 1, it bypasses glitch filter on TRGMUX input 63.
0b - Enables
1b - Bypasses
12-11
—
Reserved
10
MUX_MODE_E
N_ADC2_S9
Mux Mode Enable ADC2 Standard Channel 9
Controls the selection of GPIOs to drive ADC_2 standard channel 9.
0b - GPIO_132
1b - GPIO_46
9
MUX_MODE_E
N_ADC2_S8
Mux Mode Enable ADC2 Standard Channel 8
Controls the selection of GPIOs to drive ADC_2 standard channel 8.
0b - GPIO_133
1b - GPIO_45
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1451 / 5251


---
# 페이지 200

Table continued from the previous page...
Field
Function
8-7
—
Reserved
6
MUX_MODE_E
N_ADC1_S23
Mux Mode Enable ADC_1 Standard Channel 23
Controls the selection of GPIOs to drive ADC_1 standard channel 23.
0b - GPIO_125
1b - GPIO_146
5
MUX_MODE_E
N_ADC1_S22
Mux Mode Enable ADC_1 Standard Channel 22
Controls the selection of GPIOs to drive ADC_1 standard channel 22.
0b - GPIO_124
1b - GPIO_145
4
MUX_MODE_E
N_ADC1_S15
Mux Mode Enable ADC_1 Standard Channel 15
Controls the selection of GPIOs to drive ADC_1 standard channel 15.
0b - GPIO_4
1b - GPIO_33
3
MUX_MODE_E
N_ADC1_S14
Mux Mode Enable ADC_1 Standard Channel 14
Controls the selection of GPIOs to drive ADC_1 standard channel 14.
0b - GPIO_69
1b - GPIO_32
2
MUX_MODE_E
N_ADC0_S9
Mux Mode Enable ADC_0 Standard Channel 9
Controls the selection of GPIOs to drive ADC_0 standard channel 9.
0b - GPIO_1
1b - GPIO_46
1
MUX_MODE_E
N_ADC0_S8
Mux Mode Enable ADC_0 Standard Channel 8
Controls the selection of GPIOs to drive ADC_0 standard channel 8.
0b - GPIO_0
1b - GPIO_45
0
—
Reserved
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1452 / 5251


---
# 페이지 201

38.2.52 Read Write GPR On Functional Reset 5 (DCMRWF5)
Offset
Register
Offset
DCMRWF5
610h
Function
Contains boot address and boot mode.
This register resets after functional reset 5.
The reset value of this register is undefined on reset and is loaded from the flash memory contents at the end of the 
reset sequence.
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
BOOT_ADDRESS 
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
BOOT_ADDRESS 
BOOT
_MO...
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
31-1
BOOT_ADDRE
SS
Boot Address
Specifies the Cortex-M7_0 base address of the vector table to be used after exiting Standby mode (only 
to be considered in Fast Standby mode).
0
BOOT_MODE
Boot Mode
Selects the type of Boot mode after exiting Standby mode.
0b - Normal
1b - Fast Standby
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1453 / 5251


---
# 페이지 202

38.2.53 Read-Only GPR On PMCPOR Reset 1 (DCMROPP1)
Offset
Register
Offset
DCMROPP1
700h
Function
Resets after PMCPOR reset 1 and captures the status of the functional reset sequence process when POR_WDG overflows.
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
POR_
WDG..
.
POR_
WDG..
.
POR_
WDG..
.
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
POR_
WDG..
.
Reserv
ed 
Reserv
ed 
POR_
WDG..
.
Reserv
ed 
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
Reserv
ed 
POR_
WDG..
.
Reserv
ed 
Reserv
ed 
POR_
WDG..
.
POR_
WDG..
.
Reserv
ed 
Reserv
ed 
Reserv
ed 
POR_
WDG..
.
POR_
WDG..
.
POR_
WDG..
.
POR_
WDG..
.
POR_
WDG..
.
POR_
WDG..
.
POR_
WDG..
.
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
POR_WDG_ST
AT31
POR_WDG Status 31
Captures the status of the MC_RGM reset event (if occurred) while the chip is in Standby mode.
 
This field is used only for standby sequence monitoring.
  NOTE  
0b - Not detected
1b - Detected
30
POR_WDG_ST
AT30
POR_WDG Status 30
Captures the status of standby exit acknowledgement by MC_PCU when POR_WDG overflows.
 
This field is used only for standby sequence monitoring.
  NOTE  
0b - Not acknowledged
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1454 / 5251


---
# 페이지 203

Table continued from the previous page...
Field
Function
1b - Acknowledged
29
POR_WDG_ST
AT29
POR_WDG Status 29
Captures the status of the MC_ME standby entry request that MC_ME initiates when POR_WDG overflows.
 
This field is used only for standby sequence monitoring.
  NOTE  
0b - Active
1b - Inactive
28
—
Reserved
27
—
Reserved
26
—
Reserved
25
—
Reserved
24
—
Reserved
23
—
Reserved
22
—
Reserved
21
—
Reserved
20
POR_WDG_ST
AT20
POR_WDG Status 20
Specifies the status of the functional reset sequence process, DEST0, when POR_WDG overflows.
0b - Inactive
1b - Active
19
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1455 / 5251


---
# 페이지 204

Table continued from the previous page...
Field
Function
18
—
Reserved
17
POR_WDG_ST
AT17
POR_WDG Status 17
Specifies the status of the functional reset sequence process, FUNC10, when POR_WDG overflows.
0b - Inactive
1b - Active
16
—
Reserved
15
—
Reserved
14
POR_WDG_ST
AT14
POR_WDG Status 14
Specifies the status of the functional reset sequence process, FUNC9, when POR_WDG overflows.
0b - Inactive
1b - Active
13
—
Reserved
12
—
Reserved
11
POR_WDG_ST
AT11
POR_WDG Status 11
Specifies the status of the functional reset sequence process, FUNC8, when POR_WDG overflows.
0b - Inactive
1b - Active
10
POR_WDG_ST
AT10
POR_WDG Status 10
Specifies the status of the functional reset sequence process, FUNC7, when POR_WDG overflows.
0b - Inactive
1b - Active
9
—
Reserved
8
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1456 / 5251


---
# 페이지 205

Table continued from the previous page...
Field
Function
7
—
Reserved
6
POR_WDG_ST
AT6
POR_WDG Status 6
Specifies the status of the functional reset sequence process, FUNC6, when POR_WDG overflows.
0b - Inactive
1b - Active
5
POR_WDG_ST
AT5
POR_WDG Status 5
Specifies the status of the functional reset sequence process, FUNC5, when POR_WDG overflows.
0b - Inactive
1b - Active
4
POR_WDG_ST
AT4
POR_WDG Status 4
Specifies the status of the functional reset sequence process, FUNC4, when POR_WDG overflows.
0b - Inactive
1b - Active
3
POR_WDG_ST
AT3
POR_WDG Status 3
Specifies the status of the functional reset sequence process, FUNC3, when POR_WDG overflows.
0b - Inactive
1b - Active
2
POR_WDG_ST
AT2
POR_WDG Status 2
Specifies the status of the functional reset sequence process, FUNC2, when POR_WDG overflows.
0b - Inactive
1b - Active
1
POR_WDG_ST
AT1
POR_WDG Status 1
Specifies the status of the functional reset sequence process, FUNC1, when POR_WDG overflows.
0b - Inactive
1b - Active
0
POR_WDG_ST
AT0
POR_WDG Status 0
Specifies the status of the functional reset sequence process, FUNC0, when POR_WDG overflows.
0b - Inactive
1b - Active
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1457 / 5251


---
# 페이지 206

38.2.54 Read-Only GPR On PMCPOR Reset 2 (DCMROPP2)
Offset
Register
Offset
DCMROPP2
704h
Function
Resets after PMCPOR reset 2 and captures the MC_RGM functional or external event status when POR_WDG overflows.
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
Reserv
ed 
POR_
WDG..
.
POR_
WDG..
.
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
POR_
WDG..
.
Reserv
ed 
Reserv
ed 
Reserv
ed 
POR_
WDG..
.
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
Reserv
ed 
Reserv
ed 
Reserv
ed 
POR_
WDG..
.
Reserv
ed 
Reserv
ed 
POR_
WDG..
.
POR_
WDG..
.
POR_
WDG..
.
POR_
WDG..
.
Reserv
ed 
POR_
WDG..
.
POR_
WDG..
.
Reserv
ed 
Reserv
ed 
POR_
WDG..
.
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
—
Reserved
30
POR_WDG_ST
AT62
POR_WDG Status 62
Specifies the value of MC_RGM.FES[DEBUG_FUNC] when POR_WDG overflows.
0b - 0
1b - 1
29
POR_WDG_ST
AT61
POR_WDG Status 61
Specifies the value of MC_RGM.FES[SW_FUNC] when POR_WDG overflows.
0b - 0
1b - 1
28
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1458 / 5251


---
# 페이지 207

Table continued from the previous page...
Field
Function
—
27
—
Reserved
26
—
Reserved
25
—
Reserved
24
—
Reserved
23
—
Reserved
22
—
Reserved
21
—
Reserved
20
POR_WDG_ST
AT52
POR_WDG Status 52
Specifies the value of MC_RGM.FES[HSE_BOOT_RST] when POR_WDG overflows.
0b - 0
1b - 1
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
POR_WDG_ST
AT48
POR_WDG Status 48
Specifies the value of MC_RGM.FES[HSE_SWT_RST] when POR_WDG overflows.
0b - 0
1b - 1
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1459 / 5251


---
# 페이지 208

Table continued from the previous page...
Field
Function
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
POR_WDG_ST
AT44
POR_WDG Status 44
Specifies the value of MC_RGM.FES[PLL_AUX] when POR_WDG overflows.
0b - 0
1b - 1
11
—
Reserved
10
—
Reserved
9
POR_WDG_ST
AT41
POR_WDG Status 41
Specifies the value of MC_RGM.FES[JTAG_RST] when POR_WDG overflows.
0b - 0
1b - 1
8
POR_WDG_ST
AT40
POR_WDG Status 40
Specifies the value of MC_RGM.FES[Reserved] when POR_WDG overflows.
0b - 0
1b - 1
7
POR_WDG_ST
AT39
POR_WDG Status 39
Specifies the value of MC_RGM.FES[SWT1_RST] when POR_WDG overflows.
0b - 0
1b - 1
6
POR_WDG_ST
AT38
POR_WDG Status 38
Specifies the value of MC_RGM.FES[SWT0_RST] when POR_WDG overflows.
0b - 0
1b - 1
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1460 / 5251


---
# 페이지 209

Table continued from the previous page...
Field
Function
5
—
Reserved
4
POR_WDG_ST
AT36
POR_WDG Status 36
Specifies the value of MC_RGM.FES[ST_DONE] when POR_WDG overflows.
0b - 0
1b - 1
3
POR_WDG_ST
AT35
POR_WDG Status 35
Specifies the value of MC_RGM.FES[FCCU_RST] when POR_WDG overflows.
0b - 0
1b - 1
2
—
Reserved
1
—
Reserved
0
POR_WDG_ST
AT32
POR_WDG Status 32
Specifies the value of MC_RGM.FES[F_EXR] when POR_WDG overflows.
0b - 0
1b - 1
38.2.55 Read-Only GPR On PMCPOR Reset 3 (DCMROPP3)
Offset
Register
Offset
DCMROPP3
708h
Function
Resets after PMCPOR reset 3 and captures the MC_RGM destructive event status when POR_WDG overflows.
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1461 / 5251


---
# 페이지 210

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
Reserv
ed 
POR_
WDG..
.
POR_
WDG..
.
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserv
ed 
POR_
WDG..
.
POR_
WDG..
.
POR_
WDG..
.
W
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
POR_
WDG..
.
POR_
WDG..
.
Reserv
ed 
POR_
WDG..
.
Reserv
ed 
POR_
WDG..
.
POR_
WDG..
.
POR_
WDG..
.
Reserv
ed 
POR_
WDG..
.
Reserv
ed 
POR_
WDG..
.
POR_
WDG..
.
Reserv
ed 
Reserv
ed 
POR_
WDG..
.
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
Reset
0
0
0
0
0
0
0
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
30
POR_WDG_ST
AT94
POR_WDG Status 94
Specifies the value of MC_RGM.DES[DEBUG_DEST] when POR_WDG overflows.
0b - 0
1b - 1
29
POR_WDG_ST
AT93
POR_WDG Status 93
Specifies the value of MC_RGM.DES[SW_DEST] when POR_WDG overflows.
0b - 0
1b - 1
28
—
Reserved
27
—
Reserved
26
—
Reserved
25
—
Reserved
24
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1462 / 5251


---
# 페이지 211

Table continued from the previous page...
Field
Function
—
23
—
Reserved
22
—
Reserved
21
—
Reserved
20
—
Reserved
19
—
Reserved
18
POR_WDG_ST
AT82
POR_WDG Status 82
Specifies the value of MC_RGM.DES[HSE_SNVS_RST] when POR_WDG overflows.
0b - 0
1b - 1
17
POR_WDG_ST
AT81
POR_WDG Status 81
Specifies the value of MC_RGM.DES[HSE_TMPR_RST] when POR_WDG overflows.
0b - 0
1b - 1
16
POR_WDG_ST
AT80
POR_WDG Status 80
Specifies the value of MC_RGM.DES[CM7_CORE_CLK_FAIL] when POR_WDG overflows.
0b - 0
1b - 1
15
POR_WDG_ST
AT79
POR_WDG Status 79
Specifies the value of MC_RGM.DES[SYS_DIV_FAIL] when POR_WDG overflows.
0b - 0
1b - 1
14
POR_WDG_ST
AT78
POR_WDG Status 78
Specifies the value of MC_RGM.DES[HSE_CLK_FAIL] when POR_WDG overflows.
0b - 0
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1463 / 5251


---
# 페이지 212

Table continued from the previous page...
Field
Function
1b - 1
13
—
Reserved
12
POR_WDG_ST
AT76
POR_WDG Status 76
Specifies the value of MC_RGM.DES[AIPS_PLAT_CLK_FAIL] when POR_WDG overflows.
0b - 0
1b - 1
11
—
Reserved
10
POR_WDG_ST
AT74
POR_WDG Status 74
Specifies the value of MC_RGM.DES[CORE_CLK_FAIL] when POR_WDG overflows.
0b - 0
1b - 1
9
POR_WDG_ST
AT73
POR_WDG Status 73
Specifies the value of MC_RGM.DES[PLL_LOL] when POR_WDG overflows.
0b - 0
1b - 1
8
POR_WDG_ST
AT72
POR_WDG Status 72
Specifies the value of MC_RGM.DES[SWT2_RST] when POR_WDG overflows.
0b - 0
1b - 1
7
—
Reserved
6
POR_WDG_ST
AT70
POR_WDG Status 70
Specifies the value of MC_RGM.DES[MC_RGM_FRE] when POR_WDG overflows.
0b - 0
1b - 1
5
—
Reserved
4
POR_WDG Status 68
Table continues on the next page...
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1464 / 5251


---
# 페이지 213

Table continued from the previous page...
Field
Function
POR_WDG_ST
AT68
Specifies the value of MC_RGM.DES[STCU_URF] when POR_WDG overflows.
0b - 0
1b - 1
3
POR_WDG_ST
AT67
POR_WDG Status 67
Specifies the value of MC_RGM.DES[FCCU_FTR] when POR_WDG overflows.
0b - 0
1b - 1
2
—
Reserved
1
—
Reserved
0
POR_WDG_ST
AT64
POR_WDG Status 64
Specifies the value of MC_RGM.DES[F_POR] when POR_WDG overflows.
0b - 0
1b - 1
38.2.56 Read-Only GPR On PMCPOR Reset 4 (DCMROPP4)
Offset
Register
Offset
DCMROPP4
70Ch
Function
Resets after PMCPOR reset 4 and captures the POR_WDG reset event if POR_WDG initiates a POR sequence.
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1465 / 5251


---
# 페이지 214

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
Reserved 
POR_
WDG...
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
31-1
—
Reserved
0
POR_WDG_ST
AT96
POR_WDG Status 96
Specifies the status of POR_WDG. If this field = 1, it indicates that a stuck scenario is detected and the chip 
POR event is raised.
See POR_WDG_STAT[95:0] for the chip status when POR_WDG overflows.
0b - Inactive
1b - Active
NXP Semiconductors
Device Configuration Module General-Purpose Registers (DCM_GPR)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1466 / 5251


---