# 페이지 22

Chapter 37
Device Configuration Format (DCF) records
37.1 Overview
DCF configures certain registers of this chip during system boot while the reset signal asserts. An individual DCF record points 
to an internal register in the chip and the data to be written to that register.
UTEST DCF—The UTEST DCF clients are present within the UTEST region of the flash and programmed during production 
testing. You may write the other records and program them at the same time the application code is programmed in the flash 
memory. See the DCF client file attached to this document for the description on the UTEST DCF records.
System boot is a complex process that requires you to initialize the chip properly before releasing reset. Before using the chip, 
the user writes the application specific code into the flash memory. The user can also update the DCF records from their initial 
settings as per application requirements, in case if needed.
After power is supplied to an appropriately configured chip, PMC controls the chip, and after the system power supplies reach 
predefined levels, PMC signals MC_RGM to start the boot sequence. During this sequence, MC_RGM enables DCM to read the 
chip configuration records and then write the configuration information to the specified registers.
37.2 DCF clients
These are 32-bit wide hardware registers inside a module that receive and store data from a DCF record. This stored data is used 
to initialize registers and configure features.
DCF clients:
• Are assigned a default value before any DCF records are written.
• May have special writing constraints, such as:
— Write once.
— Change from 1 to 0 only.
— Change from 0 to 1 only.
• May not implement all 32 bits.
37.2.1 Safety features of DCF clients
Depending on the DCF client's role in the chip, the client may be equipped with a safety feature or a combination of these features.
37.2.1.1
Parity
If a DCF client implements parity checking, the client receives a parity bit in addition to its data in the DCF record. During 
chip operation, the client continuously monitors whether the data it stores matches the parity. The parity scheme used is even 
parity. So, the number of 1s in the WDATA and parity field needs to be even. For example, if the WDATA field has the value 
0000_0001h, the value of the parity field needs to be 1 so that the total number of 1s is even. It also reports errors to DCM in case 
of discrepancies.
37.2.1.2
Triple voting
DCF clients that use triple voting have three copies of the register. DCM writes to all the three registers in a single write cycle. 
During chip operation, the DCF client continuously monitors whether all these three copies match. In case of discrepancies, the 
client reports errors to DCM. The chip uses the majority result, so single errors do not affect the chip's operation. If case of single 
error, since the chip uses the majority result, there will be no impact to the chip's behavior.
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1274 / 5251


---
# 페이지 23

37.2.2 DCF client modification rules
Depending on its role in the chip, a DCF client may implement one or a combination of modification rules. If a modification rule is 
in effect, the order in which DCF records are placed in the record list may be important.
37.2.2.1
Write once
A DCF client using the write once rule can only be written with a single DCF record. The records that are appended later in the 
list are ignored and do not change the value of the client.
37.2.2.2
Write 0 only
A field in a DCF client can only be changed from 1 to 0. Therefore, if the value of a field in the previous DCF record is 0, an attempt 
by a later record to write 1 to it is ignored.
37.2.2.3
Write 1 only
A field in a DCF client can only be changed from 0 to 1. Therefore, if the value of a field in the previous DCF record is 1, an attempt 
by a later record to write 0 to the field is ignored.
37.3 DCF record structure
A DCF record is a double-word (64-bit) entry that consists of the following:
• Control word—This provides information to locate the corresponding DCF client internal to the chip (pointer to the location of 
a register internal to the chip).
• Data word—This contains the data to be written to the DCF client.
DCF records select the target DCF client using a 30-bit field in the DCF record that consists of a 15-bit chip select field and a 
15-bit address field. All modules that include DCF clients are assigned a chip select during chip definition. The address field is only 
relevant for address decoding within that module and may not necessarily relate to the address of a register that is visible to you.
C
S
14
31
Bit number
Offset
C
S
13
30
C
S
12
29
C
S
11
28
C
S
10
27
4h
5h
6h
7h
C
S
9
26
C
S
8
25
C
S
7
24
C
S
6
23
C
S
5
22
C
S
4
21
C
S
3
20
C
S
2
19
C
S
1
18
C
S
0
17 16 15 14 13 12 11 10 9
8
7
6
5
4
3
2
Parity
Address[16:2]
1
Stop
63
0
Bit number
Offset
62 61 60 59
0h
1h
2h
3h
58 57 56 55 54 53 52 51 50 49 48 47 46 45 44 43 42 41 40 39 38 37 36 35 34
Data[0:31]
33
32
Figure 161. DCF record structure
Table 227. DCF record field descriptions
Field
Name
Description
0-31
Data[0:31]
Provides the data that is to be written to the DCF client.
32-46
CSn
Indicates chip select n.
The value 1 is written to a chip select per DCF record to select the target module for the 
DCF client. The value 0 must be written to all other chip selects.
Table continues on the next page...
NXP Semiconductors
Device Configuration Format (DCF) records
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1275 / 5251


---
# 페이지 24

Table 227. DCF record field descriptions (continued)
Field
Name
Description
47-61
Address[16:2]
Contains the address of the DCF client within the selected module.
Address decoding for DCF clients may not match the standard software address map 
decoding. For details, see the DCF client addresses provided with each module.
62
Parity
Indicates parity for the DCF record.
63
Stop
Indicates the end of the list for DCF records.
0 – Not the end
1 – End
The erased state of flash memory is FFFF_FFFF_FFFF_FFFFh. Therefore, the list ends 
with the first unprogrammed double word.
This location can be programmed with a new record to extend the list.
37.4 DCF records sequence
An individual DCF record contains information to locate the corresponding DCF client internal to the chip (control word) and the 
data to be written to that client (data word).
DCF records appear as contiguous series of entries programmed at a specific address within UTEST flash memory, and must 
present the following pattern:
• The first DCF record must be a start record. This record must be placed at the beginning of a DCF area in UTEST flash 
memory to indicate to the chip that the specified records must be processed.
• DCF records containing configuration data must immediately follow the start record with no blank records in between. An 
unprogrammed record is interpreted as a stop record and no DCF records following that are processed. This allows you to 
program the records in several sessions, appending new records at the end of the list each time.
• DCF stop record with bit set indicates the end of configuration records. It is not recommended to set STOP bit in last 
DCF record programmed during production because that prevents appending additional DCFs records. The UTEST flash 
memory location following the last DCF record programmed at the factory is an unprogrammed location, which has 
FFFF_FFFFh as its content. Thus, the stop bit location in this unprogrammed flash memory location is logic 1, signifying 
that this is the last DCF record and it is not to be acted upon.
Table 228 shows the record that DCM recognizes as a start record.
Table 228. DCF start record
0h (0:31)
4h (32:63)
05AA_55AFh
0000_0000h
The factory sets the DCF start record at the beginning of the UTEST flash memory area.
Table 229 shows the record that DCM recognizes as a stop record.
Table 229. DCF stop record
0:31
32:62
63
Ignored
Ignored
1
The DCF records that you supply must be added in a contiguous manner immediately following the factory-written DCF records. 
You must never have an unprogrammed record in the series of DCF records because that is interpreted as a stop record.
NXP Semiconductors
Device Configuration Format (DCF) records
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1276 / 5251


---
# 페이지 25

Table 230 shows the series of DCF records when n data records are stored in the UTEST flash memory.
Table 230. Series of DCF records in UTEST flash memory
Record type
Address offset
Data
Start
0h
05AA_55AFh
4h
0000_0000h
STOP = 0
Data
8h
WDATA[31:0]
Ch
CS[14:0]
ADDR[16:2]
Parity
STOP = 0
10h
WDATA[31:0]
14h
CS[14:0]
ADDR[16:2]
Parity
STOP = 0
...
...
Stop
8(n-1) + 0h
Reserved
8(n-1) + 4h
Reserved
1
Ignored
8n + 0h
8n + 4h
More than one DCF records can write to the same DCF client. In this case, the later record usually overrides a DCF client 
value defined by a previous record. However, not all DCF clients allow overwrites; this depends on individual implementation of 
DCF clients.
No start record
No start record
No start record
No start record
No start record
Empty UTEST flash memory
- no action
Start record
Data record - CS0, Ad = 0
Data record - CS1, Ad = 0
Data record - CS2, Ad = 0
Stop record
Initial programming
Extension
Start record
Data record - CS0, Ad = 0
Data record - CS1, Ad = 0
Data record - CS0, Ad = 0
Data record - CS2, Ad = 0
Stop record
Overwrite
Figure 162. Appending DCF records
37.5 Chip configuration records
The DCF clients table contains information on DCF clients available in the chip. See the DCF clients file attached to this document.
The next table shows an example of how the information in this chapter is integrated with the attached DCF clients file.
NXP Semiconductors
Device Configuration Format (DCF) records
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1277 / 5251


---
# 페이지 26

Table 231. Integration of DCF information
Type
Data(n) 
assuming 
Quad page 
program
Data
Comment
Reset pad dedicated control DCF 
client (dcf_client_reset_pad_dedicated 
- column D in the "Utest DCF 
Clients" sheet)
Data word 
(determined 
base on the 
DCF record 
description in 
the "Utest DCF 
Client Register 
Bits" sheet)
0000_0001h
Data to enable pad as dedicated reset pad
Control word 
(without parity) 
(selected from 
column C in the 
"Utest DCF 
Clients" sheet)
0010_0008h
Chip Select is 3 and address is 8, 
0010_0000h+ 8h
37.6 Glossary
UTEST
User test. Refers to UTEST region of the flash.
NXP Semiconductors
Device Configuration Format (DCF) records
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1278 / 5251


---