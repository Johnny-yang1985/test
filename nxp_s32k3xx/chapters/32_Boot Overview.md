# 페이지 25

Chapter 32
Boot Overview
32.1 Overview
32.1.1 Introduction
This chapter describes the system boot sequence and provides details about boot options.
After the hardware reset sequence completes, the only CPU available is in the HSE subsystem that is referred to as the HSE CPU.
The HSE CPU starts executing firmware code in the HSE code flash memory from a fixed location that contains the SBAF code. 
This code provides the boot sequence until the control is passed, based on the type of boot:
• Nonsecure boot: Passes control to the customer software that executes on one or all the application cores.
• Secure boot: Passes control to the HSE firmware running on the HSE CPU.
32.2 Appendix
SBAF takes into account the following scenarios to prevent stuck in reset of chip:
• After observing the eight functional resets in the chip, BAF enters Recovery mode sequence to recover the application 
core’s failing status.
• SBAF does not allow the chip's LC to advance to the OEM_PROD or IN_FIELD stage, if the application does not program 
CUST_DB_PSWD/A.
• SBAF boots the application from the system-RAM during recovery mode sequence to avoid unpredictable behavior.
32.2.1 Features
The features of SBAF are as follows:
• Supports secure and nonsecure boot modes
• Supports application boot core selection
• Allows chip LC advancement
• Supports debug authorization
• Supports XRDC configuration
32.3 Chip configuration
This section describes the chip configuration details for S32K3xx variants after you program SBAF and clear the HSE firmware 
feature flag.
If the security is enabled, see the HSE Firmware Reference manual for more information. Please contact NXP sales executive 
for details.
32.3.1 Memory map
This section explains the memory sections used by SBAF in various configurations.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1200 / 5251


---
# 페이지 26

32.3.1.1
Configuration details when the HSE firmware usage feature flag is disabled
Table 197. Configuration details when the HSE firmware usage feature flag is disabled
Memory section
S32K311
S32K341
S32K312, 
S32K322, 
S32K342
S32K314, 
S32K324, 
S32K344
S32K328, 
S32K338,
S32K348, 
S32K358, 
S32K388
S32K389
Flash memory
1 MB
1 MB
2 MB
4 MB
8 MB
12 MB
 
See Table 198.
  NOTE  
IVT locations in 
priority order
0040_0000h,
0048_0000h,
1000_0000h
0040_0000h,
1000_0000h
0040_0000h,
0050_0000h,
1000_0000h
0040_0000h,
0050_0000h,
0060_0000h,
0070_0000h,
1000_0000h
0040_0000h,
0060_0000h,
0080_0000h,
00A0_0000h,
1000_0000h
0040_0000h,
0060_0000h,
0080_0000h,
00A0_0000h,
1000_0000h
Reserved
004F_4000h
to 004F_FFFFh
(48 KB)
005F_4000h to 005F_FFFFh 
(48 KB)
007F_4000h
to 007F_FFFFh
(48 KB)
00BF_4000h to 
00BF_FFFFh 
(48 KB)
00FF_4000h to 
00FF_FFFFh 
(48KB)
Application flash 
memory area
0040_0000h
to 004F_3FFFh 
(976 KB)
0040_0000h
to 004F_FFFFh 
(1024 KB)
0040_0000h
to 005F_3FFFh 
(2000 KB)
0040_0000h
to 007F_3FFFh 
(4048 KB)
0040_0000h
to 00BF_3FFFh 
(8144 KB)
0040_0000h to 
00FF_3FFFh 
(12,240 KB)
Application data 
flash memory
1000_0000h to 
1000_FFFFh 
(64 KB)
1000_0000h to 1001_FFFFh (128 KB)
1000_0000h to 
1001_ffffh (128 
KB) and 
1002_0000h to 
1003_ffffh (256 
KB)
Table 198. PFLASH configuration in S32K389
Block start address
Block end address
Size (bytes)
Flash memory configuration
0x400000
0x4FFFFF
1024
Program flash (PFC1 Block 0)
0x500000
0x5FFFFF
1024
Program flash (PFC1 Block 1)
0x600000
0x6FFFFF
2048
Program flash (PFC0 Block 0)
0x800000
0x8FFFFF
2048
Program flash (PFC0 Block 1)
0xA00000
0xAFFFFF
1024
Program flash (PFC1 Block 2)
0xB00000
0xBFFFFF
1024
Program flash (PFC1 Block 3)
0xC00000
0xDFFFFF
2048
Program flash (PFC0 Block 2)
0xE00000
0xEFFFFF
2048
Program flash (PFC0 Block 3)
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1201 / 5251


---
# 페이지 27

32.3.1.2
Configuration details when the HSE_B firmware usage feature flag is enabled
The following table explains the memory sections used by the SBAF in case HSE firmware feature flag is enabled in UTEST.
Table 199. Configuration details when the HSE_B firmware usage feature flag is enabled
Memory section
S32K311
S32K341
S32K312, 
S32K322, 
S32K342
S32K314, 
S32K324, 
S32K344
S32K328, 
S32K338,
S32K348, 
S32K358 
S32K388
S32K389
Flash memory
1 MB
1 MB
2 MB
4 MB
8 MB
12 MB
 
See Table 198.
  NOTE  
IVT locations in 
priority order
0040_0000h,
0048_0000h,
1000_0000h 
(256 Bytes)
0040_0000h,
1000_0000h 
(256 Bytes)
0040_0000h,
0050_0000h,
1000_0000h 
(256 Bytes)
0040_0000h,
0050_0000h,
0060_0000h,
0070_0000h
1000_0000h 
(256 Bytes)
0040_0000h,
0060_0000h,
0080_0000h,
00A0_0000h
1000_0000h 
(256 Bytes)
0040_0000h,
0060_0000h,
0080_0000h,
00A0_0000h,
1000_0000h
(256 Bytes)
Reserved
004D_4000h to 
004F_FFFFh 
(176 KB)
005D_4000h to 005F_FFFFh 
(176 KB)
007D_4000h to 
007F_FFFFh 
(176 KB)
00BD_4000h to 
00BF_FFFFh 
(176 KB)
00FD_4000h to 
00FF_FFFFh 
(176KB)
Application flash 
memory area 
when full 
memory "HSE 
firmware" is 
present
0040_0000h to 
004D_3FFFh 
(848 KB)
0040_0000h to 
004F_FFFFh 
(1024 KB)
0040_0000h to 
005D_3FFFh 
(1872 KB)
0040_0000h to 
007D_3FFFh 
(3920 KB)
0040_0000h to 
00BD_3FFFh 
(8016 KB)
0040_0000h to 
00FD_3FFFh 
(12,112 KB)
Application data 
flash memory
1000_0000h to 
1000_FFFFh 
(64 KB)
1000_0000h to 1001_5FFFh (88 KB)
1000_0000h to 
1001_5fffh (88 
KB) and 
1002_0000h to 
1003_FFFFh 
(256 KB)
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1202 / 5251


---
# 페이지 28

32.3.1.3
AB swap configuration
Table 200. AB swap configuration
Memory section
S32K311
S32K341
S32K312, 
S32K322, 
S32K342
S32K314, 
S32K324, 
S32K344
S32K328, 
S32K338,
S32K348, 
S32K358, 
S32K388
S32K389
Flash memory
1 MB
1 MB
2 MB
4 MB
8 MB
12 MB
 
See Table 198.
  NOTE  
IVT locations in 
priority order
0040_0000h,
1000_0000h
0040_0000h,
1000_0000h
0040_0000h,
1000_0000h
0040_0000h,
0050_0000h,
1000_0000h
0040_0000h,
0060_0000h,
1000_0000h
0040_0000h,
0060_0000h,
1000_0000h
Reserved code 
area in active 
block
0045_4000h to 
0047_FFFFh 
(176 KB)
004D_4000h to 
004F_FFFFh 
(176 KB)
004D_4000h to 
004F_FFFFh 
(176 KB)
005D_4000h to 
005F_FFFFh 
(176 KB)
007D_4000h to 
007F_FFFFh 
(176 KB)
009D_4000h to 
009F_FFFFh 
(176 KB)
Reserved code 
area in passive 
block
004D_4000h to 
004F_FFFFh 
(176 KB)
005D_4000h to 
005F_FFFFh 
(176 KB)
005D_4000h to 
005F_FFFFh 
(176 KB)
007D_4000h to 
007F_FFFFh 
(176 KB)
00BD_4000h to 
00BF_FFFFh 
(176 KB)
00FD_4000h to 
00FF_FFFFh 
(176 KB)
Application flash 
memory area in 
active block
0040_0000h to 
0045_3FFFh 
(336 KB)
0040_0000h to 
0047_FFFFh 
(512 KB)
0040_0000h to 
004D_3FFFh 
(848 KB)
0040_0000h to 
005D_3FFFh 
(1872 KB)
0040_0000h to 
007D_3FFFh 
(3920 KB)
0040_0000h to 
009D_3FFFFh 
(5,968 KB)
Application flash 
memory area in 
passive block
0048_0000h to 
004D_3FFFh 
(336 KB)
0050_0000h to 
0057_FFFFh 
(512 KB)
0050_0000h to 
005D_3FFFh 
(848 KB)
0060_0000h to 
007D_3FFFh 
(1872 KB)
0080_0000h to 
00BD_3FFFh 
(3920 KB)
00A0_0000h to 
00FD_3FFF 
(5,968 KB)
Application data 
flash memory
1000_0000h to 
1000_FFFFh 
(64 KB)
1000_0000h to 1001_FFFFh (128 KB)
1000_0000h to 
1001_ffffh (128 
KB) and 
1002_0000h to 
1003_ffffh (256 
KB)
32.4 Common configuration pertaining to the chip
32.4.1 Feature configuration in CUST_DEL Device Life Cycle
The following table describes the status of various features when chip's LC is in the CUST_DEL stage. The application software 
configures features directly or indirectly.
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1203 / 5251


---
# 페이지 29

Table 201. Feature configuration in CUST_DEL Device Life Cycle
Feature
Configuration information
Status
Configurability
OTA functionality
Disabled
Yes
Application requests the 
HSE firmware or SBAF to 
enable this feature.
HSE firmware usage 
feature flag
Indicates whether the firmware installation is 
allowed in the chip. By default, this flag is 
unprogrammed, and SBAF assumes that the 
firmware installation is not allowed.
Unprogrammed
Yes
To enable this feature, 
program in the UTEST 
location (see UTEST 
flag description for 
more information).
SBAF firmware
Programmed
No
HSE firmware
You must program the HSE firmware.
An encrypted and signed firmware image is always 
delivered to you.
Not programmed
Yes
SBAF can install 
this feature when 
the application 
software requests.
Image vector table
Not programmed
Yes
The application software 
can program this feature.
SWT0
Disabled
By SWT bit in boot 
configuration word.
Boot sequence
Boot sequence is a nonsecure boot, which 
means, the SBAF boots the application without 
any authentication.
Nonsecure boot
Yes
It can be changed 
to secure boot 
by programming the 
BOOT_SEQ bit in IVT.
Life Cycle
Customer delivery
Yes
Advance by SBAF or HSE 
firmware when requested 
by application software.
Application core 
enablement status
Applications cores are booted in recovery mode 
sequence at address 2040_0100h.
Recovery 
mode sequence
Yes
Program the required 
fields in the IVT to 
enable single or all 
application cores at the 
required address.
FIRC frequency value
48 MHz
Yes
Table continues on the next page...
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1204 / 5251


---
# 페이지 30

Table 201. Feature configuration in CUST_DEL Device Life Cycle (continued)
Feature
Configuration information
Status
Configurability
The application can 
configure after SBAF 
moves to WFI.
Application debug 
authorization mode
This mode is password-based. You can program 
the configuration in UTEST to change the mode to 
Challenge Response.
Password-
based approach
When the HSE firmware 
feature flag clears, you 
cannot change Debug 
Authorization mode.
When the HSE firmware 
feature flag is set, 
you can request the 
HSE firmware to change 
Debug Authorization 
mode to Challenge 
Response mode.
Application core 
debug status
Debug of application cores is enabled in the 
customer delivery life cycle.
Enabled
No
32.4.2 UTEST memory location usage by SBAF
Table 202. UTEST memory location usage by SBAF
Start address
End address
Size (bytes)
Description
Programmed by
Write 
protected
1B00_0000h
1B00_0007h
8
HSE firmware feature usage flag. 
See UTEST flag description for 
more information.
Application 
software
No
1B00_0040h
1B00_0047h
8
Unique Chip Identifier (UID)
NXP
No
1B00_0050h
1B00_0057h
8
FXOSC configuration flag
See UTEST flag description for 
more information.
Application 
software
No
1B00_0080h
1B00_009Fh
32
Debug 
password (CUST_DB_PSWD_A)
After the HSE firmware usage feature 
flag clears, SBAF uses this location 
to run the debug authorization feature. 
SBAF copies this value in the 
application expected response register, 
which derives the HSE expected 
response register. The size of this 
register is 16 bytes, and 1B00_0090h – 
1B00_009Fh is reserved.
Application 
software
No
Table continues on the next page...
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1205 / 5251


---
# 페이지 31

Table 202. UTEST memory location usage by SBAF (continued)
Start address
End address
Size (bytes)
Description
Programmed by
Write 
protected
After the HSE firmware usage feature 
flag sets, the HSE firmware programs 
the password at a different location.
DCM scans the password during 
reset only and retains the password 
in standby.
See the DCF clients file attached to this document for more information.
32.4.3 UTEST flag description
32.4.3.1
HSE firmware usage feature flag
This flag indicates to SBAF that the application intends to use the HSE firmware on the chip. By default, this flag is 
unprogrammed, and SBAF assumes that the HSE firmware installation is not allowed in the secure samples. However, if 
application allows the installation of the HSE firmware, the HSE firmware usage feature flag can be programmed in the UTEST 
at the 1B00_0000h location.
Table 203. HSE firmware usage feature flag
Field type
Description
Remarks
Size
64 bits
Default value
0xFFFFFFFFFFFFFFFF
SBAF does not allow the installation of 
HSE firmware.
UTEST location
0x1B000000
Configurability
Application software in 
CUST_DEL lifecycle
Enable flag
Program any value other than the default 
value
This enables the installation of the 
HSE firmware.
32.4.3.2
Crystal oscillator configuration flag
See the below table for description of the flag:
Table 204. Flag fields
Field type
Description
Size
64 bits
Default value
FFFF_FFFF_FFFF_FFFFh (Boot via FIRC)
UTEST location
1B00_0050h
Configurability
Application software in any LC
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1206 / 5251


---
# 페이지 32

Table 205. Crystal oscillator configuration flag in UTEST
63
62
61
60
59
58
57
56
55
54
53
52
51
50
49
48
R
FXOSC_ENABLE_MAGIC_NUMBER
W
47
46
45
44
43
42
41
40
39
38
37
36
35
34
33
32
R
W
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
GMSEL
EOCV
W
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
CRYSTAL_OSCILLATOR_FREQUENCY
W
Table 206. Crystal oscillator configuration bit definition
Field
Description
63 - 33
FXOSC_ENABLE_MAGIC_NUMBER
AAAA_5555h – Enable (FXOSC.CTRL[OSCON] = 1h)
FFFF_FFFFh – Disable (FXOSC.CTRL[OSCON] = 0h)
31 - 28
Crystal overdrive protection (GMSEL)
For values = 0h or Fh
Uses the default value, Ch.
27 - 20
End Of Count Value (EOCV)
For value = 0h
Uses the default value, 9Dh.
19 - 16
Reserved
15 - 0
CRYSTAL_OSCILLATOR_FREQUENCY
Frequency value of used external crystal oscillator in kHz. The valid crystal frequency range is 8000–40000 kHz.
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1207 / 5251


---
# 페이지 33

32.5 Image vector table
The following section describes the fields in the image vector table that the application programs. SBAF scans the IVT after the 
chip is out of reset. The structure is 256 bytes in size. This structure contains application cores start addresses. IVT must be 
programmed at least at one of the locations described in Chip configuration.
After reset, SBAF searches for the first valid IVT starting from the lowest address. If there are multiple valid IVT at IVT locations 
at the same time, the IVT with lowest address is used.
Table 207. Image vector table
Address 
offset
Size in 
bytes
Content
Comments
00h
4
Image vector 
table marker
marks the starting of the image vector table location. Its value must 
be 5AA5_5AA5h.
04h
4
Boot 
configuration word
Indicates the configuration word that allows you to select the various 
configurations in which you can boot the chip. See the upcoming section 
for more information.
08h
4
Reserved
0Ch
4
Cortex-M7_0 core 
start address
Specifies the boot address of the Cortex-M7_0 core in the code flash 
memory area. It must honor core Vector Table Offset Register (VTOR) 
alignment restrictions.
10h
4
Reserved
14h
4
Cortex-M7_1 core 
start address
Specifies the boot address of the Cortex-M7_1 core in the code flash 
memory area. It must honor core VTOR register alignment restrictions.
18h
4
Reserved
1Ch
4
Cortex-M7_2 core 
start address
Specifies the boot address of the Cortex-M7_2 core in the code flash memory 
area. It must honor core VTOR register alignment restrictions.
20h
4
Reserved
24h
4
Address of 
LC configuration
Specifies the address of the configuration word that allows you to advance the 
LC. See the upcoming section for more information.
28h
4
Cortex-M7_3 core 
start address
Specifies the boot address of the Cortex-M7_3 core in the code flash 
memory area. It must honor core VTOR register alignment restrictions.
32.5.1 Boot configuration word
This register informs SBAF to allow booting of selected applications.
Table 208. Boot configuration register
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
W
Table continues on the next page...
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1208 / 5251


---
# 페이지 34

Table 208. Boot configuration register (continued)
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
CM7
_3_E
NAB
LE
RES
ERV
ED
RES
ERV
ED
APP_SWT_INIT
RESERVED
BOOT_SEQ
CM7_2_ENABLE
CM7_1_ENABLE
CM7_0_ENABLE
W
Table 209. Boot configuration register field definition
Field
Description
31 – 9
Reserved
8
CM7_3_ENABLE
Indicates whether the Cortex-M7_3 application core clock is gated after boot.
0b - Gated
1b - Ungated
7
Reserved
6
Reserved
5
APP_SWT_INIT
Controls the SWT0 enablement before passing the control to the application core(s).
0b - Disables
1b - Enables
SBAF initializes SWT0 before enabling the application cores. SBAF scans this field only when the HSE firmware 
usage feature flag is enabled and the BOOT_SEQ field is 0.
4
Reserved
3
BOOT_SEQ
Controls the boot flow of the application when HSE Firmware usage feature flag is enabled.
0b - Nonsecure boot: SBAF starts the application image without any authentication in parallel to the HSE 
firmware.
1b - Secure boot: The HSE firmware executes the application image after authentication. SBAF only starts the HSE 
firmware after successful authentication.
2
CM7_2_ENABLE
Indicates whether the Cortex-M7_2 application core clock is gated after boot.
0b - Gated
1b - Ungated
Table continues on the next page...
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1209 / 5251


---
# 페이지 35

Table 209. Boot configuration register field definition (continued)
1
CM7_1_ENABLE
Indicates whether the Cortex-M7_1 application core clock is gated after boot.
0b - Gated
1b - Ungated
0
CM7_0_ENABLE
Indicates whether the Cortex-M7_0 application core clock is gated after boot.
0b - Gated
1b - Ungated
32.5.2 Address LC configuration word
This field allows you to advance the LC. To advance LC, you must program a valid 32-bit wide value at an address given in IVT 
at an address offset of 24h. This address must be 4 bytes aligned and should not lie in HSE reserved area.
The following table shows the valid values for advancement in the next LCs. For all other values at the given address, LC 
advancement is not allowed.
Table 210. Valid values for LC advancement
Life cycle stage
Valid values for LC advancement
OEM_PROD
DADA_DADAh
IN_FIELD
BABA_BABAh
Depending on the HSE firmware feature flag, the application password on the location must program before LC advancement; 
otherwise, SBAF does not attempt LC advancement.
The chip provides an LC mechanism for an irreversible progression of restrictions to access the chip's security-related content. 
You cannot reverse the chip's LC, so it is only possible to mature the chip. SBAF advances the chip through the LC:
• CUST_DEL --> OEM_PROD or IN_FIELD
• OEM_PROD --> IN_FIELD
To advance the LC through SBAF involves inserting the LC configuration word address in the IVT. SBAF issues a destructive reset 
on successful advancement. If the chip is found in the same LC as the IVT indicated, you can ignore LC advancement.
32.5.3 Structure definition of image vector table
Application can use the following structure to configure the IVT.
typedef const struct image_vector_table
{
uint32_t Header; /*Header of IVT Structure */
uint32_t BootConfig; /*Boot Configuration Word */
const uint32_t Reserved1; /* Reserved */
const uint32_t * CM7_0_StartAddress; /*Start Address of Application on CM7_0 Core */ 
const uint32_t Reserved2; /* Reserved */
const uint32_t * CM7_1_StartAddress; /*Start Address of Application on CM7_1 Core */ 
const uint32_t Reserved3; /* Reserved */
const uint32_t * CM7_2_StartAddress; /*Start Address of Application on CM7_2 Core */ 
const uint32_t * Reserved4; /* Reserved */
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1210 / 5251


---
# 페이지 36

const uint32_t * LCConfig; /*Address of LC configuration Word */
const uint32_t * CM7_3_StartAddress; /*Start Address of Application on CM7_3 Core */
const uint32_t * HseFwHeaderStartAddress; /*Start address of HSE firmware pink header image */
const uint32_t * Reserved5[2U]; /* Reserved */
const uint32_t * XrdcMDACConfiguration; /*XRDC input MDAC configuration Data */
const uint32_t * Reserved6; /* Reserved */
const uint32_t * Recoveryapp_StartAddress; /*Start Address of Application Core for Recovery 
Application */
const uint32_t * LengthRecoevryApp; /*Length of Application */
const uint8_t * Reserved7[156U]; /* Reserved */
const uint8_t * Random_IV[12U]; /*Random IV for GMAC calculation of IVT */
const uint8_t * GMAC[16U]; /*GMAC of the IVT. Reserved for Unsecure BAF */
}ivt_t;        
32.6 Boot flow
Below diagram explains boot sequence flow of SBAF.
Standby boot
Start
Standby exit
System initialization
Reset exit
Normal boot
Load and verify the  
IVT
Yes
Is the
IVT valid?
No
Boot the application
Failure
Execute recovery 
mode sequence
Success
Execute debug 
authorization 
sequence
Shutdown
SBAF
Figure 151. Boot flow
32.7 Standby boot
SBAF supports boot from standby exit. Chip register DCM.DCMRWF5 (address 402AC610h) supports boot on standby exit. 
This register clears on POR. See the "Device Configuration Module (DCM)" chapter in the S32K3xx reference manual for 
more information.
You must program this register before entering Standby mode.
There are two types of boot mode on exit from standby.
• Fast Standby
• Normal boot on exit from standby
In Fast Standby mode, the SBAF boots the Cortex-M7_0 core and halts the HSE CPU. The flow of Standby Boot is 
explained below:
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1211 / 5251


---
# 페이지 37

Standby boot flow
Normal boot flow
Reset exit
Normal standby exit
Continue with
SBAF boot flow
Start
MC_ME.MODE_ 
Status[PreviousMode]
Standby exit
DCMRWF5[0] for standby boot 
configuration
Fast standby exit
Release FIRC divider for 
application core
PRTN0_CORE0_ADDR = Core Reset
 Address for standby Exit
Enable Cortex-M7_0 core
Shut down
SBAF
Read the start address for CM7_0 
from DCMRWF5[31:1]
Figure 152. Standby boot flow
32.8 Reduced clock mode configuration
If you use clocking option B (Reduced clock mode configuration), the application sets the “dcf_client_utest_misc” DCF record 
to enable Reduced Clock mode. See the DCF clients file attached to the S32K3xx reference manual for more information on 
DCF records.
After reset, SBAF checks for DCMROF21[HSE_CLK_MODE_OPTION]. If you configure this field for clocking option B, the SBAF 
configures the following dividers in MC_CGM:
• MUX_0_DC_1
• MUX_0_DC_2
Below figure explains steps for reduced clock mode configuration steps by SBAF.
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1212 / 5251


---
# 페이지 38

Start
End
Yes
No
Write 4d to
MC_CGM.MUX_0_DC_2[DIV]
for AIPS_SLOW_CLK
STATUS =
CONFIGURATION_NOT_REQUIRED
STATUS =
CONFIGURATION_SUCCESS
Return STATUS
HSE_CLK_MODE_OPTION =2'b10
Figure 153. Reduced clock mode configuration
32.9 Debug authorization
You must program CUST_DB_PSWD_A at location 1B00_0080h. The application core debug is always password-based if the 
HSE firmware usage feature flag is cleared. See UTEST memory location usage by SBAF for more information.
32.10 FIRC divider register control
HSE.CONFIG_REG_GPR, at register address 4039C064h, controls the FIRC divider. This register is write-protected by default 
for the FIRC divider, and you cannot modify its settings.
After SBAF executes WFI, it provides write access to HSE.CONFIG_REG_GPR[FIRC_DIV_SEL], and you can configure this 
register. Before accessing this register, you must wait for the SBAF to enter WFI by reading core status register of HSE 
CPU (PRTN0_CORE2_STAT).
32.11 Application boot
The HSE firmware is responsible for securely booting the application image and not the SBAF. If secure boot is not requested (by 
writing 0 to the BOOT_SEQ field in Boot configuration word in IVT structure), SBAF always loads the application image, without 
authentication, in all chips, LC. By default, SBAF releases the reset of every core that you configure to enable.
Following flow chart explains the steps of application boot performed by SBAF.
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1213 / 5251


---
# 페이지 39

Start
Extract the core enable bit mask
from the boot configuration field
Extract the start address of
application core(s) from IVT
Is at least one 
bit mask = 1?
Yes
Yes
No
End
Enable application core(s)
In the boot configuration
word, is SWT = 1?
No
Enable the SWT0 watchdog
Trigger mode transition
Figure 154. Application boot sequence
Before configuring HSE_CLK, you must wait for the SBAF to enter WFI by reading core status register of HSE 
CPU (PRTN0_CORE2_STAT).
32.12 Recovery mode sequence
This feature allows you to program the application image in LC = MCU_PROD and LC = CUST_DEL and debug the reason of 
corruption of IVT and re-program the IVT in other LC.
The following scenarios take place when SBAF executes the recovery mode sequence.
• Valid IVT is not found (corrupted or not programmed).
• SBAF does not boot the application.
• Boot configuration word in IVT does not program the application enablement field.
• The application issued more than eight functional resets and Disable Recovery mode on functional reset field is not set in 
DCM.DCMRWP1.
• The application issued more than eight destructive resets and Disable Recovery mode on destructive reset field is not set 
in DCM.DCMRWP1.
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1214 / 5251


---
# 페이지 40

Start
Yes
No
No
Yes
Yes
Is life cycle MCU_PROD
or CUST_DEL?
Yes
Start the STM timer
Issue Functional Reset
Disable the STM timer
Copy infinite loop
code to SRAM
 Is HSE_GPR[EDB] =1?
No
No
No
Yes
Enable the application 
core(s) at SRAM address
Is DCMDEB
[APPDBG_STAT_SOC]
= 1?
Has a 30-second
timeout occurred?
End
This field determines
whether the debugger is
attached to the system.
Application cores are
enabled at the default
address only when the
debugger is attached.
This field determines
whether a successful
debug authorization
sequence has
completed and JTAG
is enabled on the
application core
Recovery mode reset 
counter += 1
Is recovery mode reset 
counter > 8 && < 16?
Figure 155. Recovery mode sequence
The infinite loop with the WFI code copies to SRAM1 that is 2040_0100h, and the code size is 16 bytes. To prevent prefetching 
errors in the application cores, place the infinite loop instruction at 2040_012Ch.
32.13 XRDC configuration
SBAF ensures that it has access to its resources and the application does not have access to area reserved for SBAF. 
The following sections describe the XRDC default configuration values when you clear the HSE firmware usage feature flag. 
Application should configure its XRDC and enable the XRDC by itself as SBAF does not enable the XRDC.
32.13.1 XRDC configuration of MDAC
Following table list down the default configuration of MDAC by SBAF.
Table 211. XRDC configuration of MDAC
Serial No.
Chip variant
MDAC register HSE CPU
Value
Domain number 
assigned to HSE CPU
1
S32K31x
MDA_W0_3_DFMT0
C000_0001h
1
2
S32K32x and S32K34x
MDA_W0_3_DFMT0
C000_0002h
2
Table continues on the next page...
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1215 / 5251


---
# 페이지 41

Table 211. XRDC configuration of MDAC (continued)
Serial No.
Chip variant
MDAC register HSE CPU
Value
Domain number 
assigned to HSE CPU
3
S32K35x and S32K33x
MDA_W0_3_DFMT0
C000_0003h
3
4
S32K388 and S32K389
MDA_W0_3_DFMT0
C000_0004h
4
32.13.2 XRDC configuration of MRC
Following table list down the MRC used by SBAF.
Table 212. XRDC configuration of MRC
MRC number
Region descriptor number
Remarks
0
14
Reserved for application
0
15
Reserved for application
32.13.3 XRDC configuration of PDAC
SBAF configures and lock the following peripherals for its use. SBAF provides all permissions to all domains.
Table 213. XRDC configuration of PDAC
Serial No.
Peripheral name
Peripheral PDAC number
1
Flash controller alternate
155
2
Flash memory alternate
188
3
HSE_GPR
231
32.14 BAF flash programming controls
The platform flash controller generates an exception of read-while-write if you simultaneously perform read and write on the same 
block. HSE CPU uses the Configuration PE Lock Register (CONFIG_PE_LOCK) in the HSE space to control the block program 
and erase for application.
BAF locks the high addressing code flash memory block during its execution, and it is cleared when the HSE CPU enters WFI. 
See the "Chip Configuration" chapter for the address of the high addressing code flash memory area.
Before programming, erasing, or executing from this address space, the application core polls for PRTN0_CORE2_STAT[WFI] 
to ensure that the HSE CPU is in the WFI state.
For boot sequence 1 or flash synchronization with the HSE firmware, see the HSE Firmware Reference Manual.
Below table explains PE lock bits setting in CONFIG_PE_LOCK register of HSE GPR during SBAF execution.
Table 214. PE lock fields setting in HSE.CONFIG_PE_LOCK
Chip
UTEST
block
Data flash block
Code flash block 
3
Code flash block 
2
Code flash block 
1
Code flash block 
0
S32K3x1
1
0
NA
NA
NA
1
Table continues on the next page...
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1216 / 5251


---
# 페이지 42

Table 214. PE lock fields setting in HSE.CONFIG_PE_LOCK (continued)
Chip
UTEST
block
Data flash block
Code flash block 
3
Code flash block 
2
Code flash block 
1
Code flash block 
0
S32K3x2
1
0
NA
NA
1
1
S32K3x4
1
0
1
0
0
1
S32K3x8
1
0
1
0
0
1
32.15 Status registers for application usage
This section explains various status registers to provide status information to the application.
32.15.1 SBAF version information
The SBAF version is a 64-bit field. The application can read the SBAF from address 4039_C020h. The following table describes 
the version information.
Table 215. SBAF version information
Bits
Field name
Description
0 – 7
Reserved
Reserved
8 - 15
SOC_TYPE_ID
This field represents the SBAF firmware, which is targeted for S32K3XX chip variant. 
Values of this field are:
0x5 – used for HSE-B S32K344/S32K314/S32K324
0xB - used for HSE-B S32K310
0xC - used for HSE-B S32K311/S32K341
0xD - used for HSE-B S32K312/S32K322/S32K342
0xE - used for HSE-B S32K358/S32K348/S32K328/S32K328
0x10- used for HSE-B S32K388
0x11- used for HSE-B S32K389
16 - 31
FW_TYPE
This field represents the SBAF firmware type. Values of this field are:
0 – used for standard generic firmware targeting all customers
1-7 – Reserved
>=8 used for Custom 1, Custom 2 (for example: Custom 1 = customer X’s project A, 
Custom 2 = customer Y’s project B)
32 - 39
Reserved
Reserved
40 - 47
BASELINE_NUMBER
Incremented when the compatibility with the previous version is broken.
48 - 55
INCREMENTAL_
NUMBER
Incremented when new features are added but compatibility kept.
56 - 63
RC_NUMBER
Release Candidate Number
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1217 / 5251


---
# 페이지 43

32.15.2 DCM.DCMRWP1
The application can disable Recovery mode entry by SBAF after programming bits 23 and 22 of DCM.DCMRWP1.
Table 216. DCM.DCMRWP1 (address 0x402AC400)
Bits
Number 
of bits
R/W access 
by application
Description
24-31
8
Reserved
23
1
R/W
Disable Recovery Mode On Destructive Reset
Indicates that this field resets by default, and SBAF allows Recovery mode 
sequence if the application issues > 8 destructive resets. The application 
can set this field to disable Recovery mode when the application issues > 8 
destructive resets.
22
1
R/W
Disable Recovery Mode On Functional Reset
Indicates that this field resets by default, and SBAF allows Recovery mode 
sequence if the application issues > 8 functional resets. The application can set this 
field to disable Recovery mode when the application issues > 8 functional resets.
21
1
R
Reserved
16-20
5
R
Recovery Mode Reset Counter
Indicates that to enable Recovery mode functionality for the OEM_PROD and 
IN_FIELD LC stages, SBAF increments this counter when a functional or 
destructive reset is issued.
15
1
R
Reserved
11-14
4
R
Destructive Reset Counter
Indicates that SBAF increments this counter when a destructive reset is issued.
0-10
11
R
Reserved
32.15.3 Status bits on HSE.GPR
SBAF writes HSE.GPR at address 4039_C028h to show status information as described in the following table.
Table 217. Status bits on HSE.GPR
Bit
Description
0
Indicates that SBAF presents and boots the HSE FW.
1-4
Reserved.
5
Indicates that SBAF boots the application cores in Recovery mode sequence.
6
Indicates that SBAF performs the debug authentication.
7-31
Reserved.
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1218 / 5251


---
# 페이지 44

32.16 Interrupt and exception handling
• Interrupt handling: No special interrupt handling routines are required during the boot process. Interrupts are disabled 
during SBAF execution.
• Exception handling: SBAF enters the recovery mode sequence after enabling debug authorization. After eight consecutive 
functional resets or destructive resets from Application Firmware, the device enters the recovery mode sequence.
• Boot target watchdog: SBAF enables/disables SWT0 watchdog with default timeout, that is 25 ms according to the boot 
configuration word, before enabling the application core(s). It is expected that the application services this watchdog 
before expiration.
32.17 Hardware modules used by SBAF
• MC_ME: SBAF uses MC_ME to enable the application cores, mode switch, and other operations during its execution.
• FXOSC: SBAF configures FXOSC according to the crystal oscillator configuration flag in UTEST.
• Clock Generation Module (MC_CGM): SBAF configures MC_CGM in Reduced clock mode configuration.
• DCM: SBAF uses the DCM to identify the Life Cycle, standby boot mode configuration, lockstep, and clock mode 
configuration.
• HSE_GPR: SBAF configures hardware protection, program erase lock, FIRC divider control, and SBAF version number.
• XRDC: SBAF configures the XRDC module.
• Flash Module: SBAF always perform the write and erase operation on alternate interface. See Chip configuration for 
details of flash memory usage by SBAF.
32.18 Hardware IP registers details modified by SBAF
Below table summarizes the registers which are modified by SBAF when HSE Firmware usage feature flag is disabled.
Table 218. Hardware IP registers modified by SBAF
IP
Register Name
Default value (hex)
Modified value (hex)
MC_ME
MC_ME.PRTN1_COFB1_STAT
1CFE_2FFCh
FXOSC and MC_CGM clocks 
are enabled by default. 
However, for 120 MHz clock 
requests, SBAF ensures if the 
MC_CGM clock is enabled.
MC_ME.PRTN0_COREx_ADDR
0040_0000h
SBAF updates this address 
if you request the application 
core 0 boot during the 
normal boot sequence 
in IVT or Recovery 
mode (0x2040012C).
MC_ME.PRTN0_COREx_PCONF
0000_0000h
The core clock is enabled 
when the recovery mode 
sequence is executed or when 
the clock is enabled in Boot 
configuration word.
MC_ME.PRTN0_COREx_PUPD
0000_0000h
Table continues on the next page...
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1219 / 5251


---
# 페이지 45

Table 218. Hardware IP registers modified by SBAF (continued)
IP
Register Name
Default value (hex)
Modified value (hex)
MC_ME.CTL_KEY
0000_5AF0h
SBAF updates this register if 
SBAF boots any one of the 
application core. 0000_5AF0h 
and then 0000_A50Fh.
FXOSC
FXOSC.CTRL
019D_00C0h
See Crystal oscillator 
configuration flag
MC_RGM
MC_RGM.DRET
0000_0000h
0000_000Fh
SWT_0
SWT_0.CR
FF00_010Ah
FF00_000Bh, when SWT_0 
is enabled in the boot 
configuration word and 
FF00_000Ah when the 
SWT_0 is disabled in the boot 
configuration word.
SWT_0.IR
0000_0000h
0000_0001h
32.19 Glossary
BAF
Boot assist flash
CUST_DEL
Chip's life cycle stage, customer delivery
IN_FIELD
Chip's life cycle stage, in field
IVT
Image vector table
LC
Chip's life cycle—limits by design the configuration and debug/test possibilities of the chip for in-field usage
MCU_PROD
Chip's life cycle stage, MCU production
OEM_PROD
Chip's life cycle stage, OEM production
OTA
Over the air
SBAF
Secure boot assist flash
NXP Semiconductors
Boot Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1220 / 5251


---