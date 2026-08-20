# 페이지 2

Chapter 36
Hardware Security Engine (HSE_B)
36.1 HSE subsystem
HSE is a security subsystem. It runs security functions for applications having stringent confidentiality and authenticity 
requirements. HSE has the following objectives:
• Isolating security-sensitive information (for example, secret keys) from the application (the host)
• Transferring the cryptographic operations from application cores and processing them
• Accelerating cryptographic operations with dedicated coprocessors
• Enforcing security measures on the application, during runtime and system startup
The HSE subsystem is the only master that is unconditionally released from reset after POR. It then releases the CPU subsystems 
in the host from reset, with the opportunity to apply certain checks beforehand (secure system startup). Based on certain 
conditions, HSE can also trigger interrupts and reset signals to the host during runtime.
36.1.1 CPU subsystem
The HSE CPU subsystems process the security functions and control system resources to provide security services to the 
application domain (the host).
36.1.2 Cryptographic accelerators
The HSE subsystem supports the following cryptographic accelerators:
• An AES engine supporting all standard key sizes (128, 192, 256 bits) and various complex ciphering modes (ECB, CBC, CTR, 
OFB, CFB, CCM, CMAC)
• A hash engine that supports standard several primitives: MD5, SHA-1, SHA-224, SHA-256
• PKC which accelerates RSA and ECC operations (key generation, signature generation, signature verification, ciphering)
— RSA (1024, 2048, 3072, 4096-bit)
— ECC over prime numbers
◦BN P256, P638
◦ANSI X9P192 to X9P512
◦Brainpool P160 to P512
◦Sec P128 to P521
◦TU Darmstadt prime Curve 1 to 35
◦Ed25519
The HSE subsystem supports several other cryptographic primitives through the software. See HSE firmware for 
more information.
36.1.3 Random number generator (RNG)
The RNG in this chip consists of a TRNG and a DRBG. Both are designed to be compliant to the highest strength in security as 
specified in
• BSI AIS20/31
• NIST SP800-90a,b,c
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1254 / 5251


---
# 페이지 3

The TRNG function provides a seed for the DRBG, while the DRBG is available to the host via dedicated random number 
generation services.
36.1.4 Timers
The HSE subsystem features:
• An independent dedicated system timer
• HSE_STM (apart from chip timer resources), that allows recurring autonomous functions such as runtime memory 
verification checks
• A watchdog timer to reset the HSE subsystem in case of unexpected runtime failure
36.1.5 Memory resources
See Configuration_GPR memory map for more information on configuration controls related to HSE memory resources.
36.1.5.1
Secure RAM
The Secure area sizes are enforced by the Memory controllers and updated to appropriate value by HSE before any Host core 
release. This ensures that these secure areas are never exposed to any other core than HSE.
Secure sizes for each K3 derivative are described in the HSE Firmware Refence Manual.
Secure RAM refers to RAM area that the HSE subsystem access exclusively.
36.1.5.2
Secure flash
Secure flash refers to nonvolatile memory that the HSE subsystem accesses exclusively.
36.2 HSE interface
36.2.1 Messaging unit (MU)
The HSE subsystem has two messaging units:
• HSE_MU0
• HSE_MU1
See the "Messaging Unit (MU)" chapter for more information.
36.2.1.1
Overview
MU is the communication interface between the host and the HSE subsystem. The host uses MU to trigger service requests and 
to receive service responses. The HSE firmware uses MU to receive service requests, return service responses, and provide a 
general status of the HSE subsystem.
Each of the two MU instances available in the HSE subsystem has:
• Two sides:
— MUA: Only the HSE subsystem accesses it.
— MUB: The host accesses it.
The registers on one side have corresponding registers on the other side.
• A set of 32-bit readable and writable transmit registers (MUB_TRn), which the host uses to transfer the address of the service 
descriptor to the HSE firmware. The HSE firmware retrieves the address of the service descriptor in the corresponding 
registers MUA_RRn.
• A set of 32-bit read-only receive registers (MUB_RRn), which the host uses to retrieve the response to the service requests. 
The HSE firmware provides the response to service requests in the corresponding registers MUA_TRn.
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1255 / 5251


---
# 페이지 4

• Control and status registers to manage MU and the access to transmit and receive registers.
The advantages of using the MU to manage the HSE service requests and responses are:
• Hardware mechanisms are in place on the transmit registers to avoid service request overrun.
• Interrupt signals are available to allow asynchronous management of the requests (avoiding active waiting loops).
• Freedom from interference between different application cores. You can configure each MU instance with specific access 
restrictions that can be used, for example, to isolate the requests that different masters make (in different MU instances). You 
configure such access controls using XRDC.
36.3 Debug
36.3.1 HSE subsystem debug
The debugging of the HSE subsystem and associated firmware is restricted to NXP engineering teams.
36.3.2 Host debug
The host debug is either open or protected, depending on the device Lifecycle state. See the ‘Life cycle’ section in ‘Device 
Configuration Module’ chapter for details on device lifecycle advancement and decoding. See the Debug chapter for details on 
host/application core debug.
The debug protection consists of locking the debugger access through the JTAG interface until the HSE firmware authenticates 
the debugger. This authentication is based on ADK/P, a 16-byte region within UTEST used for application core debug. This 
location will be used by SBAF to run the debug authorization feature. SBAF will use this value to derive the application 
expected response register and HSE expected response register. See UTEST memory map in the DCF clients file attached to 
this document.
The authentication method can be:
• Static: In this case, ADK/P is a password which the debugger provides in plain form.
• Dynamic: In this case, ADK/P is a cryptographic key which the debugger uses to calculate a cryptographic response to a 
random challenge.
36.4 HSE firmware
Factory supplied firmware that runs in the HSE subsystem controls HSE functionality. It essentially serves the host with a set of 
security services as described in Table 224.
Table 224. Summary of firmware security services
Service
Summary
Administration
Install, configure, update, and test the HSE firmware
Key management
Available for the application to manage different sets of keys that the HSE firmware manages, for 
example, cryptographic services
Cryptographic
Provide the application with cryptographic primitives that high level security tasks use in 
the application
Random number
Generate random streams that can be used in various security protocols
Memory verification
Allow the application to verify different memory areas at startup (after reset) and during runtime
Monotonic counter
Provide the application with a set of monotonic counters that can be read and only incremented
Secure time
Allow the configuration of a secure tick to be signaled to the application
Table 225 provides an overview of services and features that the HSE firmware supports.
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1256 / 5251


---
# 페이지 5

Table 225. HSE firmware features
Service
Category
Feature
Cryptography
Ciphers
AES: ECB, CBC, CFB, OFB, CTR, XTS1
RSAES: PKCS1-v1_5, OAEP
Message 
Authentication 
Code (MAC)
AES: CMAC, XCBC-MAC1, HMAC1, and GMAC1
Hashing
SHA1
SHA224, SHA256, SHA384, SHA512
SHA3_2241, SHA3_2561, SHA3_3841, SHA3_5121
MD5
Miyaguchi-Preneel Compression
Authenticated ciphers
AES: CCM, GCM1
Digital signature 
generation 
and verification
RSASSA_PSS
RSASSA_PKCS1-v1_5
ECDSA – ECC over GF(P) with all prime standard curve supported
EdDSA - Ed25519 pre-hashed curve
Key management
Max key sizes
AES: 256 bits
RSA: 4096 bits
ECC: 521 bits
DH: 4096 bits
Key generation
Permanent and ephemeral RSA and ECC key pair generation
Key import or export
Plain or encrypted form, with optional authentication tag.
SHE key update protocol
Key derivation
NIST 800-108, PBKDF2, and so on
Key exchange
ECDH and Classic DH
Certificate handling
Key Installation from X.509 and CVC certificates
Certificate installation for Root of Trust establishment.
Boot and 
memory verification
Authentication schema
AES CMAC, XCBC-MAC
RSA & ECC signatures
Verification flow
Before application startup (strict secure boot)
In parallel to the application startup
On the application demand
Sanctions
No startup (strict secure boot)
Table continues on the next page...
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1257 / 5251


---
# 페이지 6

Table 225. HSE firmware features (continued)
Service
Category
Feature
Chip reset
Key usage restrictions
Monotonic counter
Counter management
Incrementing and reading volatile and non-volatile counters
Random number
Deterministic random 
bit generation
Based on a True Random Number
AIS31 Class P2 high and FIPS 140-2 compliant
Secure time
Secure tick
Application interrupts at configurable frequency
Administration services
HSE administration
Firmware installation and update
Subsystem configuration and testing
1. Software implementation of cryptographic primitives.
See documents in Table 226 for more information about how to install, configure, and use the HSE firmware that NXP provides.
Table 226. References
Document number
Document title
Description
HSEFWRM
HSE Firmware 
Reference Manual
Contains details about how to install, configure, and use the 
HSE firmware.
HSESIRM
HSE Service Interface 
Reference Manual
Security firmware API reference for non-AUTOSAR users.
36.5 Configuration_GPR register descriptions
36.5.1 Configuration_GPR memory map
This section describes the chip configurations that only the HSE core manages. These constitute control of peripherals, secure 
size configurations for SRAM and flash memory, flash memory program or erase control, and so on.
 
Write accesses to configuration registers apart from 32-bit accesses might result in unpredictable chip behavior, 
therefore must not be done.
  NOTE  
Configuration_GPR base address: 4039_C000h
Offset
Register
Width
(In bits)
Access
Reset value
1Ch
General Purpose Configuration 0 (CONFIG_REG0)
32
R
0000_0000h
34h
General Purpose Configuration 6 (CONFIG_REG6)
32
R
0000_0035h
38h
Configuration RAM Protected Region (CONFIG_RAMPR)
32
R
See section
3Ch
Configuration Code Flash Memory Active Block (CONFIG_CFPRL)
32
R
See section
40h
Configuration Code Flash Memory Passive Block (CONFIG_CFPRH)
32
R
See section
Table continues on the next page...
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1258 / 5251


---
# 페이지 7

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
44h
Configuration Data Flash Memory Protected Region 
(CONFIG_DFPR)
32
R
See section
50h
Configuration Program and Erase Lock (CONFIG_PE_LOCK)
32
R
0000_0000h
54h
Configuration RAM Protected Region Alternate 
(CONFIG_RAMPR_ALT)
32
R
See section
58h
Configuration Code Flash Memory Active Block Alternate 
(CONFIG_CFPRL_ALT)
32
R
See section
5Ch
Configuration Code Flash Memory Passive Block Alternate 
(CONFIG_CFPRH_ALT)
32
R
See section
60h
Configuration Data Flash Memory Protected Region Alternate 
(CONFIG_DFPR_ALT)
32
R
See section
64h
Configuration REG_GPR (CONFIG_REG_GPR)
32
RW
A000_0003h
36.5.2 General Purpose Configuration 0 (CONFIG_REG0)
Offset
Register
Offset
CONFIG_REG0
1Ch
Function
The EDB field resets on destructive or POR reset events and functional reset has no impact on it.
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
EDB 
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
1. If export_control=1, the reset value of EDB is 1. If export_control=0, the reset value is 0.
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1259 / 5251


---
# 페이지 8

Fields
Field
Function
31-7
—
Reserved
6
EDB
Hardware Debugger Attached
This is a sticky field that clears on destructive reset or POR.
0b - Debugger not connected
1b - Debugger connected
5-0
—
Reserved
36.5.3 General Purpose Configuration 6 (CONFIG_REG6)
Offset
Register
Offset
CONFIG_REG6
34h
Function
Resets on functional reset.
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
HL 
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
Reserv
ed 
SAI_S
DI...
FLEXI
O_...
Reserv
ed 
MAC_
CLO...
Reserv
ed 
QUAD
SPI...
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
1
1
0
1
0
1
Fields
Field
Function
31
HL
Hard Lock
This is a sticky field. If you write 1 to it, it remains 1 until next reset or POR.
Table continues on the next page...
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1260 / 5251


---
# 페이지 9

Table continued from the previous page...
Field
Function
0b - You can write to this register
1b - Register is locked for any write
30-7
—
Reserved
6
—
Reserved
5
SAI_SDID_PCT
L
SAI0 and SAI1 clock gating
Clock to SAI peripheral is on or off.
0b - Clock is off (gated)
1b - Clock is on
4
FLEXIO_CLOC
K_GATE
FlexIO Clock Gating
Clock to FlexIO peripheral is on or off.
0b - Clock is off (gated)
1b - Clock is on
3
—
Reserved
2
MAC_CLOCK_
GATE
Ethernet Clock Gating
Clock to Ethernet peripheral is on or off.
0b - Clock is off (gated)
1b - Clock is on
1
—
Reserved
0
QUADSPI_SDI
D_PCTL
QuadSPI Clock Gating
Clock to QuadSPI peripheral is on or off.
0b - Clock is off (gated)
1b - Clock is on
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1261 / 5251


---
# 페이지 10

36.5.4 Configuration RAM Protected Region (CONFIG_RAMPR)
Offset
Register
Offset
CONFIG_RAMPR
38h
Function
Resets on functional reset.
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
HARD
_LO...
SOFT_
LO...
Reserved 
SECURE_SIZE 
W
Reset
1
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
SECURE_SIZE 
Reserved 
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
1. The default reset value of this register varies on the part basis, depending on NXP factory configurations.
Fields
Field
Function
31
HARD_LOCK
Hard Lock
This is a sticky field. If you write 1 to it, it remains 1 until next reset or POR.
0b - Write access to this register is allowed
1b - Write access to this register is not allowed until next functional reset
30
SOFT_LOCK
Soft Lock
0b - Write access to this register is allowed
1b - Write access to this register is not allowed
29-21
—
Reserved
20-5
SECURE_SIZE
Secure Size
Secure size region (in bytes) for PRAM1. This is 32-byte-aligned to ensure alignment with cache lines.
4-0
Reserved
Table continues on the next page...
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1262 / 5251


---
# 페이지 11

Table continued from the previous page...
Field
Function
—
36.5.5 Configuration Code Flash Memory Active Block (CONFIG_CFPRL)
Offset
Register
Offset
CONFIG_CFPRL
3Ch
Function
Resets on functional reset.
 
The secure size will go to default or reset value on assertion of any DCF violation from HSE.
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
HARD
_LO...
SOFT_
LO...
Reserved 
SECURE_SIZE 
W
Reset
1
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
SECURE_SIZE 
Reserved 
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
1. The default reset value of this register varies on the part basis, depending on NXP factory configurations.
Fields
Field
Function
31
HARD_LOCK
Hard Lock
This is a sticky field. If you write 1 to it, it remains 1 until next reset or POR.
0b - Write access to this register is allowed
1b - Write access to this register is not allowed until next functional reset
30
Soft Lock
Table continues on the next page...
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1263 / 5251


---
# 페이지 12

Table continued from the previous page...
Field
Function
SOFT_LOCK
0b - Write access to this register is allowed
1b - Write access to this register is not allowed
29-21
—
Reserved
20-13
SECURE_SIZE
Secure Size
Flash memory active block secure size in bytes to align to 8 KB (sector) aligned write.
12-0
—
Reserved
36.5.6 Configuration Code Flash Memory Passive Block (CONFIG_CFPRH)
Offset
Register
Offset
CONFIG_CFPRH
40h
Function
Resets on functional reset.
 
The secure size will go to default or reset value on assertion of any DCF violation from HSE.
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
HARD
_LO...
SOFT_
LO...
Reserved 
SECURE_SIZE 
W
Reset
1
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
SECURE_SIZE 
Reserved 
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
1. The default reset value of this register varies on the part basis, depending on NXP factory configurations.
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1264 / 5251


---
# 페이지 13

Fields
Field
Function
31
HARD_LOCK
Hard Lock
This is a sticky field. If you write 1 to it, it remains 1 until next reset or POR.
0b - Write access to this register is allowed
1b - Write access to this register is not allowed until next functional reset
30
SOFT_LOCK
Soft Lock
0b - Write access to this register is allowed
1b - Write access to this register is not allowed
29-21
—
Reserved
20-13
SECURE_SIZE
Secure Size
Secure size region (in bytes) for flash memory passive block for alignment with 8 KB (sector) aligned 
writes.
12-0
—
Reserved
36.5.7 Configuration Data Flash Memory Protected Region (CONFIG_DFPR)
Offset
Register
Offset
CONFIG_DFPR
44h
Function
Resets on functional reset.
 
The secure size will go to default or reset value on assertion of any DCF violation from HSE.
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
HARD
_LO...
SOFT_
LO...
Reserved 
SECURE_SIZE 
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
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1265 / 5251


---
# 페이지 14

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
SECURE_SIZE 
Reserved 
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
1. The default reset value of this register varies on the part basis, depending on NXP factory configurations.
Fields
Field
Function
31
HARD_LOCK
Hard Lock
This is a sticky field. If you write 1 to it, it remains 1 until next reset or POR.
0b - Write access to this register is allowed
1b - Write access to this register is not allowed until next functional reset
30
SOFT_LOCK
Soft Lock
0b - Write access to this register is allowed
1b - Write access to this register is not allowed
29-21
—
Reserved
20-13
SECURE_SIZE
Secure Size
Secure size region (in bytes) for data flash memory aligned to 8KB (sector) aligned writes.
12-0
—
Reserved
36.5.8 Configuration Program and Erase Lock (CONFIG_PE_LOCK)
Offset
Register
Offset
CONFIG_PE_LOCK
50h
Function
Resets on functional reset.
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1266 / 5251


---
# 페이지 15

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
Reserv
ed 
PE_LO
CK...
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
PE_LO
CK...
PE_LO
CK...
PE_LO
CK...
PE_LO
CK...
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
31-19
—
Reserved
18
—
Reserved
17
—
Reserved
16
PE_LOCK_BLO
CK_4
Program/Erase Lock for Block 4
0b - Block 4 is available for program and erase operations
1b - Block 4 is locked and unavailable for program and erase operations
15
PE_LOCK_BLO
CK_3
Program/Erase Lock for Block 3
0b - Block 3 is available for program and erase operations
1b - Block 3 is locked and unavailable for program and erase operations
14
PE_LOCK_BLO
CK_2
Program/Erase Lock for Block 2
0b - Block 2 is available for program and erase operations
1b - Block 2 is locked and unavailable for program and erase operations
13
PE_LOCK_BLO
CK_1
Program/Erase Lock for Block 1
0b - Block 1 is available for program and erase operations
1b - Block 1 is locked and unavailable for program and erase operations
12
PE_LOCK_BLO
CK_0
Program/Erase Lock for Block 0
0b - Block 0 is available for program and erase operations
1b - Block 0 is locked and unavailable for program and erase operations
Table continues on the next page...
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1267 / 5251


---
# 페이지 16

Table continued from the previous page...
Field
Function
11-0
—
Reserved
36.5.9 Configuration RAM Protected Region Alternate (CONFIG_RAMPR_ALT)
Offset
Register
Offset
CONFIG_RAMPR_ALT
54h
Function
Resets on functional reset.
 
The secure size will go to default or reset value on assertion of any DCF violation from HSE.
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
INVERT_VALUE_RAMPR 
W
Reset
1
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
INVERT_VALUE_RAMPR 
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
1. The default reset value of this register varies on the part basis, depending on NXP factory configurations.
Fields
Field
Function
31-0
INVERT_VALU
E_RAMPR
Invert Value DFPR
Write inverted value of register CONFIG_RAMPR to CONFIG_RAMPR_ALT.
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1268 / 5251


---
# 페이지 17

36.5.10 Configuration Code Flash Memory Active Block Alternate (CONFIG_CFPRL_ALT)
Offset
Register
Offset
CONFIG_CFPRL_ALT
58h
Function
Resets on functional reset.
 
The secure size will go to default or reset value on assertion of any DCF violation from HSE.
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
INVERT_VALUE_CFPRAB 
W
Reset
1
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
INVERT_VALUE_CFPRAB 
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
1. The default reset value of this register varies on the part basis, depending on NXP factory configurations.
Fields
Field
Function
31-0
INVERT_VALU
E_CFPRAB
Invert Value CFPRAB
Write inverted value of register CONFIG_CFPRL to CONFIG_CFPRL_ALT.
36.5.11 Configuration Code Flash Memory Passive Block Alternate (CONFIG_CFPRH_ALT)
Offset
Register
Offset
CONFIG_CFPRH_ALT
5Ch
Function
Resets on functional reset.
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1269 / 5251


---
# 페이지 18

 
The secure size will go to default or reset value on assertion of any DCF violation from HSE.
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
INVERT_VALUE_CFPRP 
W
Reset
1
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
INVERT_VALUE_CFPRP 
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
1. The default reset value of this register varies on the part basis, depending on NXP factory configurations.
Fields
Field
Function
31-0
INVERT_VALU
E_CFPRP
Invert Value CFPRP
Write inverted value of register CONFIG_CFPRH to CONFIG_CFPRH_ALT.
36.5.12 Configuration Data Flash Memory Protected Region Alternate (CONFIG_DFPR_ALT)
Offset
Register
Offset
CONFIG_DFPR_ALT
60h
Function
Resets on functional reset.
 
The secure size will go to default or reset value on assertion of any DCF violation from HSE.
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
INVERT_VALUE_DFPR 
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
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1270 / 5251


---
# 페이지 19

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
INVERT_VALUE_DFPR 
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
1. The default reset value of this register varies on the part basis, depending on NXP factory configurations.
Fields
Field
Function
31-0
INVERT_VALU
E_DFPR
Invert Value DFPR
Write inverted value of register CONFIG_DFPR to CONFIG_DFPR_ALT.
36.5.13 Configuration REG_GPR (CONFIG_REG_GPR)
Offset
Register
Offset
CONFIG_REG_GPR
64h
Function
Resets on functional reset.
 
This register can be changed by application core when HSE is not installed.
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
APP_CORE_ACC 
Reserved 
W
Reset
1
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
FIRC_DIV_SEL 
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
1
1
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1271 / 5251


---
# 페이지 20

Fields
Field
Function
31-29
APP_CORE_A
CC
APP_CORE_ACC
 
While writing to this register, APP_CORE_ACC is RO and should not be changed 
from 0b101.
  NOTE  
101b - Application core can write the [FIRC_DIV_SEL] field. The APP_CORE_ACC must be 101b 
to have access to FIRC_DIV_SEL field
All other values - No access to application core
28-2
—
Reserved
1-0
FIRC_DIV_SEL
FIRC Divider
Indicates this chip's FIRC clock division factor.
00b - Divided by 2
01b - Divided by 2
10b - Divided by 16
11b - Undivided
36.6 Glossary
ADK/P
Application debug key/password
AES
Advanced encryption standard
CBC
Cipher block chaining
CCM
Counter with CBC MAC (Cipher block chaining message authentication code)
CFB
Cipher feedback mode
CMAC
Cipher-based message authentication code
CTR
Counter-based block cipher mode
CVC
Card verifiable certificates
Classic DH
Classical Diffie–Hellman, a key exchange method
DRBG
Deterministic random bit generator
DH
Diffie Hellman, a key exchange method
ECB
Electronic code book
ECC
Elliptic curve cryptography
ECDSA
Elliptic curve digital signature algorithm
ECDH
Elliptic-curve Diffie–Hellman, a key exchange method
EdDSA
Edwards-curve digital signature algorithm
FIPS
Federal information processing standards
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1272 / 5251


---
# 페이지 21

MUA
Messaging unit A interface
MUB
Messaging unit B interface
MD5
Message-Digest Algorithm 5
NIST
National institute of standards and technology
OAEP
Optimal asymmetric encryption padding
OFB
Output feedback based block cipher mode
GCM
Galois/counter mode
GMAC
Galois message authentication code
HMAC
Keyed-hash message authentication code
PKC
Public key cryptographic engine
PKCS1
Public-key cryptography standards. PKCS provides the basic definitions of, and recommendations for 
implementing the RSA algorithm.
POR
Power-on reset
RNG
Random number generator
RSA
Rivest–Shamir–Adleman (a public key cryptosystem)
RSASSA_PSS RSA Signature Scheme with Appendix - Probabilistic Signature Scheme
SHE
Secure hardware extension
SHA
Secure Hash Algorithm
TRNG
True random number generator
XCBC-MAC
Extended ciphertext block chaining MAC
XTS
XEX (XOR encrypt XOR) based tweaked-codebook mode with ciphertext stealing
NXP Semiconductors
Hardware Security Engine (HSE_B)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1273 / 5251


---