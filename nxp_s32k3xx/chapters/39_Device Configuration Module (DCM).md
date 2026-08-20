# 페이지 215

Chapter 39
Device Configuration Module (DCM)
39.1 Overview
DCM controls:
• LC
• DCF client registers
• Debug authorization (Export Control mode)
The module also establishes a RoT for the chip by parsing the master root key and other security records.
39.1.1 Block diagram
This figure is a block representation of DCM.
Block 0
uTest sector
PFC flash memory
interface
Flash memory
scanner
DCF client
bus controller
DCM debug
DCM registers
Block 1
Block 2
Block 3
Block 4
Block 5
DCM
SWD/JTAG
interface
Lifecycle  
Lifecycle
DCF client
Flash
Memory
Platform Flash Controller (PFC)
Figure 163. DCM block diagram
39.1.2 Features
• Scans flash memory and configures the system for following information:
— LC detection
— DCF records configuration using flash memory
• Allows debug features for flash memory content and the chip
• Provides debug enable control for HSE and application
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1467 / 5251


---
# 페이지 216

• Provides a valid boot address detection
• Enables the DCF client to be writable via the IPS bus
• Parametrizes control to mask a set of DCF client chip select
• Supports temporary advancement of the LC by programming DCMLCC[DCMFLC]
• Manages debug features for flash memory content and the chip like debug enable control and debug authorization.
39.2 Functional description
DCM provides information about the current state and configuration of the system that you could use to:
• Configure the application software.
• Debug the system.
39.2.1 Modes of operation
DCM operates identically in all system modes of operation.
39.2.2 DCF mechanism
The DCF mechanism handles chip parameter settings via the OTP flash memory.
You can store a series of DCF records in UTEST flash memory, and each record is 64 bits in length. The chip processes these 
records during the system reset sequence before the CPU leaves reset.
39.2.3 DCF error recording
DCF errors are recorded in DCM for both types of clients—spread spectrum safe and normal. See DCF client error mechanism 
for details on spread spectrum safe clients.
39.2.4 DCF client error mechanism
The DCM consists of DCMMISC[DCMCERS] for detecting faulty DCF records. The DCMSRRn registers capture the details up 
to 16 faulty records. The DCMCERS bit can be cleared by writing 1 to it.
While scanning the flash, in case if a faulty record is encountered, the DCMMISC[DCMCERS] gets set indicating that there is 
atleast one faulty record. In such a case, the user can identify the details about the faulty record in the DCMSRRn registers and 
should update the flash memory with a new record, provided the record is not write-once.
For example, in the image below, if the faulty DCF record is DCF2, then the correct DCF record must also be DCF2. Even in case 
if the faulty record is updated, the DCM stores the faulty record via the DCMMISC[DCMCERS] and DCMSRRn registers.
This figure shows that a faulty DCF record is loaded between the original and final DCF record sets.
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1468 / 5251


---
# 페이지 217

DCM
DCM error flags
and reports
IPS interface
Pulse
wrapper
DCF2
DCF1
DCF1
Original
DCF
DCF2
Utest flash memory
Faulty
DCF
DCF2
Final
DCF
DCF2
Figure 164. DCF error handling
39.2.5 DCM error detection mechanism
This figure shows the flow diagram of errors logged into DCM from DCF clients and Flash memory scanner. It also shows that 
DCM provides software control for lifecycle and export control mode.
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1469 / 5251


---
# 페이지 218

Flash memory
Flash memory
DCF scanner
Utest
Start record
End record
Software control
TimeOut/ECC/
FlashIntfViol
DCF bus
DCF bus
DCF bus
Error logging
DCM regs
DCF client 
error /
Safe DCF 
client error
Mux
Lifecycle &
ExportControl DCF client
control
Figure 165. DCM error detection mechanism
39.2.6 LC
DCM determines the LC of the chip by reading the LC slots from the Utest flash memory. This read operation is performed during 
the reset phase, with normal timings. The operating monitors and an ECC check protect the operation. Additionally, a set of sanity 
checks executed over the LC read data guarantee the integrity of the final LC value.
At the end of the reset phase, the LC contains one of the following values:
• OEM production (OEM_PROD)
• In field (IN_FIELD)
• Pre-FA
• FA
The DCM LC progresses in the direction shown in this figure:
MCU
production
Customer
delivery
OEM
production
In field
Pre-failure
analysis
Failure
analysis
Figure 166. LC sequence
The LC is written into six slots, 128 bits each, and at fixed locations in the Utest flash memory block. Each LC slot is read in a single 
atomic operation and is organized in two types of fields:
• Valid (lower 64b of LC slot)
• Invalid (higher 64b of LC slot)
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1470 / 5251


---
# 페이지 219

Depending on the possible combinations of data programmed into these fields, each LC slot indicates one of the four possible 
statuses as shown in Table 233. To know more about LC slots, see Table 234.
Table 233. LC slot status
LC slots
LC slot value
Valid field (64 bits)
Invalid field (64 bits)
Erased
Erased
Erased
Marked
Erased
Active
Marked
Marked
Inactive
Other values
Illegal
In this case, "Marked" refers to a value that is configured based on the bit pattern 55AA_50AF_55AA_50AFh, and "Erased" is 
detected using the bit pattern FFFF_FFFF_FFFF_FFFFh.
Table 234. LC slots
LC slot 2
OEM_PROD
LC slot 3
IN_FIELD
LC slot 4
Pre-FA
LC slot 5
FA
Resulting LC
Active
Erased
Erased
Erased
OEM_PROD
Inactive
Active
Erased
Erased
IN_FIELD
Inactive
Inactive
Active
Erased
Pre-FA
Inactive
Inactive
Inactive
Active
FA
 
When triggering DCM for rescanning, the software must ensure that the flash memory program and erase fields are 
not set. Otherwise, DCM does not configure the chip and ignores all data returned from the UTEST flash memory. 
This results in LC becoming IN_FIELD. All DCF clients indicate their default values in this case.
  NOTE  
39.3 DCM register descriptions
39.3.1 DCM memory map
DCM base address: 402A_C000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
DCM Status (DCMSTAT)
32
R
0000_0371h
4h
LC and LC Control (DCMLCC)
32
RW
See section
8h
LC Scan Status (DCMLCS)
32
RW
0000_0000h
1Ch
DCM Miscellaneous (DCMMISC)
32
RW
0000_0001h
20h
Debug Status and Configuration (DCMDEB)
32
RW
0000_0000h
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1471 / 5251


---
# 페이지 220

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
2Ch
DCF Error Count (DCMEC)
32
R
0000_0000h
30h
DCF Scan Report (DCMSRR1)
32
RW
0000_0000h
34h
DCF Scan Report (DCMSRR2)
32
RW
0000_0000h
38h
DCF Scan Report (DCMSRR3)
32
RW
0000_0000h
3Ch
DCF Scan Report (DCMSRR4)
32
RW
0000_0000h
40h
DCF Scan Report (DCMSRR5)
32
RW
0000_0000h
44h
DCF Scan Report (DCMSRR6)
32
RW
0000_0000h
48h
DCF Scan Report (DCMSRR7)
32
RW
0000_0000h
4Ch
DCF Scan Report (DCMSRR8)
32
RW
0000_0000h
50h
DCF Scan Report (DCMSRR9)
32
RW
0000_0000h
54h
DCF Scan Report (DCMSRR10)
32
RW
0000_0000h
58h
DCF Scan Report (DCMSRR11)
32
RW
0000_0000h
5Ch
DCF Scan Report (DCMSRR12)
32
RW
0000_0000h
60h
DCF Scan Report (DCMSRR13)
32
RW
0000_0000h
64h
DCF Scan Report (DCMSRR14)
32
RW
0000_0000h
68h
DCF Scan Report (DCMSRR15)
32
RW
0000_0000h
6Ch
DCF Scan Report (DCMSRR16)
32
RW
0000_0000h
80h
LC Scan Status 2 (DCMLCS_2)
32
RW
0000_0000h
39.3.2 DCM Status (DCMSTAT)
Offset
Register
Offset
DCMSTAT
0h
Function
Indicates the status of DCM at different stages.
 
This register resets on functional reset.
  NOTE  
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1472 / 5251


---
# 페이지 221

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
DCMD
BGPS 
0
DCMU
TS 
0
DCML
CST 
0
DCME
RR 
DCMD
ONE 
W
Reset
0
0
0
0
0
0
1
1
0
1
1
1
0
0
0
1
Fields
Field
Function
31-19
—
Reserved
18-16
—
Reserved
15-12
—
Reserved
11
—
Reserved
10
DCMDBGPS
Debug Password Scanning Status
Indicates the DCM debug password scanning status.
0b - Completed with errors
1b - Completed successfully
9
—
Reserved
8
DCMUTS
DCM Utest DCF Scanning Status (valid only if DCMDONE bit is set)
 
This bit always returns 0 in In Field LC.
  NOTE  
0b - Completed with errors.
1b - Completed successfully.
7-5
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1473 / 5251


---
# 페이지 222

Table continued from the previous page...
Field
Function
—
4
DCMLCST
LC Scanning Status (valid only if DCMDONE bit is set)
Indicates the DCM LC scanning status.
 
This bit always returns 0 in INFIELD lifecycle.
  NOTE  
0b - Completed with errors
1b - Completed successfully
3-2
—
Reserved
1
DCMERR
DCM Completion of Flash Scan with Error Status (valid only if DCMDONE bit is set)
0b - Completed with success.
1b - Completed with error.
0
DCMDONE
DCM Flash Scanning Status
Indicates whether the DCM scanning is in progress or complete.
0b - Running
1b - Completed
39.3.3 LC and LC Control (DCMLCC)
Offset
Register
Offset
DCMLCC
4h
Function
Resets on the functional reset.
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1474 / 5251


---
# 페이지 223

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
Reserved 
0
DCMRLC 
Reserv
ed 
DCMCLC 
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
u1
u
u
0
u1
u
u
1. Post reset, the reset value of this register is 0000_0077h, and after scanning, it changes according to the programmed 
value.
Fields
Field
Function
31-10
—
Reserved
9-8
—
Reserved
7
—
Reserved
6-4
DCMRLC
Real LC
Projects the real LC of the chip.
The LC can move in this sequence: (010 : OEM_PROD) > (111 : IN_FIELD) > (001 : Pre-FA) > (000 : FA)
000b - FA
001b - Pre-FA
010b - OEM_PROD
100b - Reserved
101b - Reserved
111b - IN_FIELD
3
—
Reserved
2-0
DCMCLC
Current LC
Projects the current LC of the chip.
The LC can move in this sequence: (010 : OEM_PROD) > (111 : IN_FIELD) > (001 : Pre-FA) > (000 : FA)
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1475 / 5251


---
# 페이지 224

Table continued from the previous page...
Field
Function
000b - FA
001b - Pre-FA
010b - OEM_PROD
100b - Reserved
101b - Reserved
111b - IN_FIELD
39.3.4 LC Scan Status (DCMLCS)
Offset
Register
Offset
DCMLCS
8h
Function
Stores the status of LC scanning. By default, the status of each LC is "not yet scanned."
This register:
• Resets on destructive reset.
• Always returns 0 in a valid IN_FIELD LC (in LC without an error).
This register captures the errors related to LC scanning on each of these resets: POR, destructive, and functional. If an error is 
captured, its status in this register is cleared by writing 1 to the corresponding field or to any of the destructive or POR events.
All LC slot errors are captured and cleared independently.
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
DCML
CFE5 
DCML
CE5 
DCMLCC5 
DCML
CSS5 
DCML
CFE4 
DCML
CE4 
DCMLCC4 
DCML
CSS4 
DCML
CFE3 
DCML
CE3 
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
DCMLCC3 
DCML
CSS3 
Reserved 
W
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
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1476 / 5251


---
# 페이지 225

Fields
Field
Function
31-30
—
Reserved
29
DCMLCFE5
Pre-FA Flash Memory Error Check
Indicates the status of the Pre-FA flash memory error check.
0b - No errors
1b - Errors exist
28
DCMLCE5
Pre-FA ECC Errors
Indicates if Pre-FA is successful or has ECC errors.
0b - No errors
1b - Errors exist
27-25
DCMLCC5
Pre-FA Marking Status
Indicates the Pre-FA marking status.
These errors may cause this field to indicate the "not scanned yet" status:
• If the reading completes too early and DCM has not yet scanned the LC.
• If there is an error in the flash memory after completion of the reading.
000b - Not scanned yet
001b - Marked as active
010b - Marked as inactive
011b - Region is erased/virgin
101b - Marked as inactive by an unknown pattern
110b - Scanning timed out
24
DCMLCSS5
Pre-FA Scan Status
Indicates the status of the Pre-FA scan.
0b - No errors
1b - Errors exist
23
DCMLCFE4
IN_FIELD Flash Memory Error Check
Indicates the status of IN_FIELD flash memory error check.
0b - No errors
1b - Errors exist
22
DCMLCE4
IN_FIELD ECC Errors
Indicates if IN_FIELD has ECC errors.
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1477 / 5251


---
# 페이지 226

Table continued from the previous page...
Field
Function
0b - No errors
1b - Errors exist
21-19
DCMLCC4
IN_FIELD Marking Status
Indicates the IN_FIELD marking status.
These errors may cause this field to indicate the "not scanned yet" status:
• If the reading completes too early and DCM has not yet scanned the LC.
• If there is an error in the flash memory after completion of the reading.
000b - Not scanned yet
001b - Marked as active
010b - Marked as inactive
011b - Region is erased/virgin
101b - Marked as inactive by an unknown pattern
110b - Scanning timed out
18
DCMLCSS4
IN_FIELD Scan Status
Indicates the status of the IN_FIELD scan.
0b - No errors
1b - Errors exist
17
DCMLCFE3
OEM_PROD Flash Memory Error Check
Indicates the status of the OEM_PROD flash memory error check.
0b - No errors
1b - Errors exist
16
DCMLCE3
OEM_PROD ECC Errors
Indicates if OEM_PROD has ECC errors.
0b - No errors
1b - Errors exist
15-13
DCMLCC3
OEM_PROD Marking
Indicates the OEM_PROD marking status.
These errors may cause this field to indicate the "not scanned yet" status:
• If the reading completes too early and DCM has not yet scanned the LC.
• If there is an error in the flash memory after completion of the reading.
000b - Not scanned yet
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1478 / 5251


---
# 페이지 227

Table continued from the previous page...
Field
Function
001b - Marked as active
010b - Marked as inactive
011b - Region is erased/virgin
101b - Marked as inactive by an unknown pattern
110b - Scanning timed out
12
DCMLCSS3
OEM_PROD Scan Status
Indicates the status of OEM_PROD scan.
0b - No errors
1b - Errors exist
11-0
—
Reserved
39.3.5 DCM Miscellaneous (DCMMISC)
Offset
Register
Offset
DCMMISC
1Ch
Function
Resets on destructive reset.
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
DCMC
ERS 
0
0
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
0
0
DCMD
BGE 
DCMD
BGT 
0
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
1
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1479 / 5251


---
# 페이지 228

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
—
Reserved
28
DCMCERS
DCF Client Errors
Records the status of errors from DCF clients.
0b - No errors on any of the DCF clients
1b - Atleast one safety DCF client has an error
27-24
—
Reserved
23-14
—
Reserved
13-12
—
Reserved
11
DCMDBGE
DCM ECC error on DBG sections
This bit is set if there is any ECC error during scanning of CUST_PWD, or UID.
0b - No ECC error
1b - ECC error
10
DCMDBGT
DBG Section Timeout Error
Indicates if there is a DCM UTEST flash memory timeout error in DBG sections. The value of this field is 
1 in case a timeout error occurs when scanning CUST_PWD, or UID.
0b - No error
1b - Error exists
9-0
—
Reserved
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1480 / 5251


---
# 페이지 229

39.3.6 Debug Status and Configuration (DCMDEB)
Offset
Register
Offset
DCMDEB
20h
Function
Resets on destructive reset.
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
APPD
BG_...
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
Reserved 
DCM_
APP...
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
31-17
—
Reserved
16
APPDBG_STAT
_SOC
Application Debug Status
Indicates the application debug status of the chip.
0b - Disabled
1b - Enabled
15
—
Reserved
14
—
Reserved
13
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1481 / 5251


---
# 페이지 230

Table continued from the previous page...
Field
Function
12
—
Reserved
11-10
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
5-2
—
Reserved
1
DCM_APPDBG
_STAT
DCM Authentication Engine Status for Application Core
 
This bit will read 0 in non-export control mode.
  NOTE  
0
—
Reserved
39.3.7 DCF Error Count (DCMEC)
Offset
Register
Offset
DCMEC
2Ch
Function
Indicates the number of faulty DCF records.
This register resets on destructive reset.
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1482 / 5251


---
# 페이지 231

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
DCMECT 
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
DCMECT
DCF Error Count
Indicates the number of faulty DCF records.
39.3.8 DCF Scan Report (DCMSRR1)
Offset
Register
Offset
DCMSRR1
30h
Function
Resets on destructive reset.
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
DCMD
CFT1 
DCME
SD1 
DCME
SF1 
DCMDCFF1 
0
DCMDCFE1 
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
DCMDCFE1 
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
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1483 / 5251


---
# 페이지 232

Fields
Field
Function
31-30
—
Reserved
29
DCMDCFT1
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD1
Chip Side Error
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF1
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF1
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
20-0
DCMDCFE1
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.9 DCF Scan Report (DCMSRR2)
Offset
Register
Offset
DCMSRR2
34h
Function
Resets on destructive reset.
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1484 / 5251


---
# 페이지 233

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
DCMD
CFT2 
DCME
SD2 
DCME
SF2 
DCMDCFF2 
0
DCMDCFE2 
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
DCMDCFE2 
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
31-30
—
Reserved
29
DCMDCFT2
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD2
Chip Side Error
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF2
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF2
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1485 / 5251


---
# 페이지 234

Table continued from the previous page...
Field
Function
20-0
DCMDCFE2
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.10 DCF Scan Report (DCMSRR3)
Offset
Register
Offset
DCMSRR3
38h
Function
Resets on destructive reset.
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
DCMD
CFT3 
DCME
SD3 
DCME
SF3 
DCMDCFF3 
0
DCMDCFE3 
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
DCMDCFE3 
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
31-30
—
Reserved
29
DCMDCFT3
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD3
Chip Side Error
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1486 / 5251


---
# 페이지 235

Table continued from the previous page...
Field
Function
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF3
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF3
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
20-0
DCMDCFE3
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.11 DCF Scan Report (DCMSRR4)
Offset
Register
Offset
DCMSRR4
3Ch
Function
Resets on destructive reset.
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1487 / 5251


---
# 페이지 236

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
DCMD
CFT4 
DCME
SD4 
DCME
SF4 
DCMDCFF4 
0
DCMDCFE4 
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
DCMDCFE4 
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
31-30
—
Reserved
29
DCMDCFT4
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD4
Chip Side Error
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF4
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF4
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1488 / 5251


---
# 페이지 237

Table continued from the previous page...
Field
Function
20-0
DCMDCFE4
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.12 DCF Scan Report (DCMSRR5)
Offset
Register
Offset
DCMSRR5
40h
Function
Resets on destructive reset.
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
DCMD
CFT5 
DCME
SD5 
DCME
SF5 
DCMDCFF5 
0
DCMDCFE5 
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
DCMDCFE5 
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
31-30
—
Reserved
29
DCMDCFT5
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD5
Chip Side Error
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1489 / 5251


---
# 페이지 238

Table continued from the previous page...
Field
Function
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF5
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF5
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
20-0
DCMDCFE5
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.13 DCF Scan Report (DCMSRR6)
Offset
Register
Offset
DCMSRR6
44h
Function
Resets on destructive reset.
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1490 / 5251


---
# 페이지 239

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
DCMD
CFT6 
DCME
SD6 
DCME
SF6 
DCMDCFF6 
0
DCMDCFE6 
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
DCMDCFE6 
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
31-30
—
Reserved
29
DCMDCFT6
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD6
Chip Side Error
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF6
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF6
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1491 / 5251


---
# 페이지 240

Table continued from the previous page...
Field
Function
20-0
DCMDCFE6
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.14 DCF Scan Report (DCMSRR7)
Offset
Register
Offset
DCMSRR7
48h
Function
Resets on destructive reset.
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
DCMD
CFT7 
DCME
SD7 
DCME
SF7 
DCMDCFF7 
0
DCMDCFE7 
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
DCMDCFE7 
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
31-30
—
Reserved
29
DCMDCFT7
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD7
Chip Side Error
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1492 / 5251


---
# 페이지 241

Table continued from the previous page...
Field
Function
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF7
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF7
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
20-0
DCMDCFE7
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.15 DCF Scan Report (DCMSRR8)
Offset
Register
Offset
DCMSRR8
4Ch
Function
Resets on destructive reset.
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1493 / 5251


---
# 페이지 242

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
DCMD
CFT8 
DCME
SD8 
DCME
SF8 
DCMDCFF8 
0
DCMDCFE8 
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
DCMDCFE8 
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
31-30
—
Reserved
29
DCMDCFT8
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD8
Chip Side Error
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF8
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF8
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1494 / 5251


---
# 페이지 243

Table continued from the previous page...
Field
Function
20-0
DCMDCFE8
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.16 DCF Scan Report (DCMSRR9)
Offset
Register
Offset
DCMSRR9
50h
Function
Resets on destructive reset.
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
DCMD
CFT9 
DCME
SD9 
DCME
SF9 
DCMDCFF9 
0
DCMDCFE9 
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
DCMDCFE9 
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
31-30
—
Reserved
29
DCMDCFT9
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD9
Chip Side Error
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1495 / 5251


---
# 페이지 244

Table continued from the previous page...
Field
Function
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF9
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF9
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
20-0
DCMDCFE9
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.17 DCF Scan Report (DCMSRR10)
Offset
Register
Offset
DCMSRR10
54h
Function
Resets on destructive reset.
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1496 / 5251


---
# 페이지 245

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
DCMD
CFT...
DCME
SD10 
DCME
SF10 
DCMDCFF10 
0
DCMDCFE10 
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
DCMDCFE10 
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
31-30
—
Reserved
29
DCMDCFT10
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD10
Chip Side Error
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF10
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF10
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1497 / 5251


---
# 페이지 246

Table continued from the previous page...
Field
Function
20-0
DCMDCFE10
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.18 DCF Scan Report (DCMSRR11)
Offset
Register
Offset
DCMSRR11
58h
Function
Resets on destructive reset.
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
DCMD
CFT...
DCME
SD11 
DCME
SF11 
DCMDCFF11 
0
DCMDCFE11 
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
DCMDCFE11 
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
31-30
—
Reserved
29
DCMDCFT11
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD11
Chip Side Error
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1498 / 5251


---
# 페이지 247

Table continued from the previous page...
Field
Function
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF11
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF11
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
20-0
DCMDCFE11
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.19 DCF Scan Report (DCMSRR12)
Offset
Register
Offset
DCMSRR12
5Ch
Function
Resets on destructive reset.
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1499 / 5251


---
# 페이지 248

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
DCMD
CFT...
DCME
SD12 
DCME
SF12 
DCMDCFF12 
0
DCMDCFE12 
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
DCMDCFE12 
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
31-30
—
Reserved
29
DCMDCFT12
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD12
Chip Side Error
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF12
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF12
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1500 / 5251


---
# 페이지 249

Table continued from the previous page...
Field
Function
20-0
DCMDCFE12
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.20 DCF Scan Report (DCMSRR13)
Offset
Register
Offset
DCMSRR13
60h
Function
Resets on destructive reset.
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
DCMD
CFT...
DCME
SD13 
DCME
SF13 
DCMDCFF13 
0
DCMDCFE13 
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
DCMDCFE13 
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
31-30
—
Reserved
29
DCMDCFT13
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD13
Chip Side Error
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1501 / 5251


---
# 페이지 250

Table continued from the previous page...
Field
Function
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF13
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF13
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
20-0
DCMDCFE13
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.21 DCF Scan Report (DCMSRR14)
Offset
Register
Offset
DCMSRR14
64h
Function
Resets on destructive reset.
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1502 / 5251


---
# 페이지 251

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
DCMD
CFT...
DCME
SD14 
DCME
SF14 
DCMDCFF14 
0
DCMDCFE14 
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
DCMDCFE14 
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
31-30
—
Reserved
29
DCMDCFT14
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD14
Chip Side Error
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF14
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF14
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1503 / 5251


---
# 페이지 252

Table continued from the previous page...
Field
Function
20-0
DCMDCFE14
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.22 DCF Scan Report (DCMSRR15)
Offset
Register
Offset
DCMSRR15
68h
Function
Resets on destructive reset.
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
DCMD
CFT...
DCME
SD15 
DCME
SF15 
DCMDCFF15 
0
DCMDCFE15 
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
DCMDCFE15 
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
31-30
—
Reserved
29
DCMDCFT15
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD15
Chip Side Error
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1504 / 5251


---
# 페이지 253

Table continued from the previous page...
Field
Function
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF15
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF15
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
20-0
DCMDCFE15
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.23 DCF Scan Report (DCMSRR16)
Offset
Register
Offset
DCMSRR16
6Ch
Function
Resets on destructive reset.
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1505 / 5251


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
0
DCMD
CFT...
DCME
SD16 
DCME
SF16 
DCMDCFF16 
0
DCMDCFE16 
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
DCMDCFE16 
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
31-30
—
Reserved
29
DCMDCFT16
Scanning Timeout On Flash Memory
Indicates if scanning timeout exists on flash memory address.
0b - Does not exist
1b - Exists
28
DCMESD16
Chip Side Error
Indicates if an error exists on chip side. These errors could be parity errors or the ones reported by the 
DCF client, such as write-once error.
0b - No errors
1b - Errors exist
27
DCMESF16
Flash Memory Error
Indicates if a UTEST flash memory ECC error exists.
0b - No errors
1b - Errors exist
26-24
DCMDCFF16
DCF Record Location
Indicates the DCF record location.
010b - Utest flash memory
101b - Others: Reserved
23-21
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1506 / 5251


---
# 페이지 255

Table continued from the previous page...
Field
Function
20-0
DCMDCFE16
Flash Memory Address
Indicates the flash memory address of the DCF client having an error.
39.3.24 LC Scan Status 2 (DCMLCS_2)
Offset
Register
Offset
DCMLCS_2
80h
Function
Stores the status of LC scanning. By default, the status of each LC is "not yet scanned."
This register:
• Resets on destructive reset.
• Always returns 0 in a valid IN_FIELD LC (in LC without an error).
This register captures the errors related to LC scanning on each of these resets: POR, destructive, and functional. If an error is 
captured, its status in this register is cleared by writing 1 to the corresponding field or to any of the destructive or POR events.
All LC slot errors are captured and cleared independently.
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
DCML
CFE6 
DCML
CE6 
DCMLCC6 
DCML
CSS6 
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
31-6
—
Reserved
Table continues on the next page...
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1507 / 5251


---
# 페이지 256

Table continued from the previous page...
Field
Function
5
DCMLCFE6
Flash Memory Error Check
Indicates the status of flash memory check.
0b - No errors
1b - Errors exist
4
DCMLCE6
FA ECC Errors
Indicates if ECC errors exist in FA.
0b - No errors
1b - Errors exist
3-1
DCMLCC6
FA Marking
Indicates the FA marking status.
These errors may cause this field to indicate the "not scanned yet" status:
• If the reading completes too early and DCM has not yet scanned the LC.
• If there is an error in the flash memory after completion of the reading.
000b - Not scanned yet
001b - Marked as active
010b - Marked as inactive
011b - Region is erased/virgin
101b - Marked as inactive by an unknown pattern
110b - Scanning timed out
0
DCMLCSS6
FA Scan Status
Indicates if errors exist in the FA scan.
0b - No errors
1b - Errors exist
39.4 Glossary
FA
Failure analysis
LC
Life cycle
Pre-FA
Pre-failure analysis
RoT
Root of trust
OTP
One Time Programmable
DCF
Device Configuration Format
PFC
Platform Flash Controller
NXP Semiconductors
Device Configuration Module (DCM)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1508 / 5251


---