# RM_HSE_B

이 문서는 PDF에서 자동으로 변환된 문서입니다.

---

# 페이지 1

RM00286
HSE_B Firmware Reference Manual
Rev. 2.5 — 28 May 2025
Reference manual
COMPANY CONFIDENTIAL
Document information
Information
Content
Keywords
HSE, S32K3XX, Reference Manual, RN00286
Abstract
This is the HSE-B Reference Manual to install, configure, and use the HSE firmware provided by
NXP for its Arm®-based S32x device family featuring the HSE_B subsystem.
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 2

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
1   Document Description
1.1  Content
This document is the reference manual to install, configure, and use the HSE firmware provided by NXP for its
Arm®-based S32x device family featuring the HSE_B subsystem.
This document explains all the standard features that are supported by HSE firmware. For the custom firmware,
some additional features need to be supported and some standard feature needs to be removed. Refer to the
HSE Firmware Annexure Document which contains the feature list supported by the custom release. It also
contains the details of the custom features and services. The description of features in this document that are
not part of the annexure document should be ignored by the reader. This document is applicable for following
devices:
• S32K311, S32K310, MWCT2014S, S32M274, S32M276 (S32K3X1 family)
• S32K342, S32K341, S32K322, MWCT2D16S, S32K312, MWCT2016S (S32K3X2 family)
• S32K344, S32K324, S32K314, MWCT2D17S (S32K3X4 family)
• S32K396, S32K394, S32K376, S32K374 (S32K3X6 family)
• S32K358, S32K356, S32K348, S32K338, S32K336, S32K328 (S32K358 family)
• S32K388
• S32K389
1.2  Intended readers
This document is intended to help security architects and security software developers to use the services
provided by the NXP HSE firmware operating within the HSE subsystem.
Readers of this document are desired to have:
• Software programming skills with the C language
• A general understanding of the NXP S32x device architectures
1.3  Disclaimer
While NXP has implemented advanced security features, all products may be subject to unidentified
vulnerabilities. Customers are responsible for the design and operation of their applications and products to
reduce the effect of such vulnerabilities on their applications and products, and NXP accepts no liability for any
vulnerability that is discovered. Customers need to implement appropriate design and operating safeguards to
minimize the risks associated with their applications and products.
Furthermore, NXP encourages its customers to make a well-informed decision regarding the selection of
security algorithms and protocols to use in their products and systems. The HSE firmware supports certain
cryptographic functions, key lengths, and protocols but it is not an endorsement of their security: they are
provided because there can be use cases where it is legitimate to use them (for example, for legacy purposes).
For a first set of recommendations, refer to the document Selecting and using cryptographic algorithms and
protocols.
1.4  Reference documents
For further details, refer to the following documents:
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
2 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 3

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Tag
Document name
Reference
Author(s) /
Issuer(s)
[REF01]
HSE Service API Reference Manual
HSEAPIRM
NXP
[REF02]
S32K3xx Reference Manual
Device-specific reference manual
NXP
[REF03]
Selecting and using cryptographic algorithms and
protocols
Application Note AN649711
NXP
[REF04]
AES_ACCEL Subsystem Reference Manual
-
[REF10]
Recommendation for Block Cipher Modes of Operation
NIST Special Publication
800-38A
NIST
[REF11]
Recommendation for Block Cipher Modes of Operation:
The CMAC Mode for Authentication
NIST Special Publication
800-38B
NXP
[REF12]
Recommendation for Block Cipher Modes of Operation:
The CCM Mode for Authentication and Confidentiality
NIST Special Publication
800-38C
NIST
[REF13]
Recommendation for Block Cipher Modes of Operation:
Galois/Counter Mode (GCM) and GMAC
NIST Special Publication
800-38D
NIST
[REF14]
The Keyed-Hash Message Authentication Code
(HMAC)
FIPS PUB 198-1 July 2008
NIST
[REF15]
Secure Hash Standard (SHS)
FIPS PUB 180-4
NIST
[REF16]
SHA-3 Standard
FIPS PUB 202
NIST
[REF17]
Recommendation for Random Number Generation
Using Deterministic Random Bit Generators
NIST Special Publication
800-90A
NIST
[REF18]
Recommendation for Key-Derivation Methods in Key-
Establishment Schemes
NIST Special Publication
800-56C Revision 1
NIST
[REF19]
Recommendation for Key Derivation Using
Pseudorandom Functions (Revised)
NIST Special Publication 800-108 NIST
[REF20]
The AES-XCBC-MAC-96 Algorithm and Its Use with
IPsec
RFC 3566 September 2003
NIST, Intel
[REF22]
Elliptic Curve Cryptography (ECC) Brainpool Standard
Curves and Curve Generation
RFC 5639 March 2010
BSI, secunet
[REF23]
Internet X.509 Public Key Infrastructure Certificate and
Certificate Revocation List (CRL) Profile
RFC 5280 May 2008
NIST
[REF24]
Elliptic Curves for Security
RFC 7748 January 2016
Google, Rambus,
sn3rd
[REF25]
Edwards-Curve Digital Signature Algorithm (EdDSA)
RFC 8032 January 2017
SJD AB, I.
Liusvaara
[REF26]
PKCS #10: Certification Request Syntax Specification
Version 1.7
RFC 2986 November 2000
RSA security
[REF27]
PKCS #5: Password-Based Cryptography Specification
Version 2.
rfc8018 January 2017
IETF
[REF28]
HMAC-based Extract-and-Expand Key Derivation
Function (HKDF)
RFC 5869 May 2010
IBM Research,
Nokia
[REF29]
The Transport Layer Security (TLS) Protocol Version 1.2 RFC 5246 August 2008
T. Dierks, RTFM
Inc.
[REF30]
Internet Key Exchange (IKEv2) Protocol
RFC 4306 December 2005
Microsoft
Table 1. Reference documents
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
3 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 4

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Tag
Document name
Reference
Author(s) /
Issuer(s)
[REF31]
Transport Layer Security (TLS) Session Hash and
Extended Master Secret Extension
RFC 7627 September 2015
IETF
[REF32]
Pre-Shared Key Cipher suites for Transport Layer
Security (TLS)
RFC 4279 December 2005
IETF
[REF33]
A Secure and Efficient Conference Key Distribution
System
-
Mike Burmester,
Yvo Desmedt
[REF34]
ECDHE_PSK Cipher Suites for Transport Layer
Security (TLS)
RFC 5489 March 2009
IETF
[REF40]
SHE – Secure Hardware Extension Functional
Specification
Version 1.1 01/04/2009
HIS consortium [1]
[REF41]
Standards for Efficient Cryptography 1 (SEC1)
Version 2.0 May 2009
Certicom
[REF42]
Standards for Efficient Cryptography 2 (SEC2)
Version 1.0 September 2000
Certicom
[REF43]
Functionality classes and evaluation methodology for
true (physical) random number generators
AIS31, Version 3.1, 25/09/2001
BSI
[REF44]
Standard for Cryptographic Protection of Data on Block-
Oriented Storage Devices
IEEE 1619-2018 January 2019
IEEE
[REF45]
PKCS #1: RSA Cryptography Standard
Version 2.2 October 2012
RSA Laboratories
[REF46]
Information technology - Security techniques -
Encryption algorithms - Part 2: Asymmetric ciphers
ISO/IEC 18033-2:2006
ISO/IEC JTC 1/
SC 27
[REF47]
Elliptic Curves for Security
RFC 7748 January 2016
IETF
[REF48]
SHE Verification Specification
Version 1.0.1(rev 79)
[REF50]
IEEE Standard for Local and Metropolitan Area
Networks— Port Based Network Access Control
IEEE Std 802.1X™ 2020
IEEE
Table 1. Reference documents...continued
[1]
Document currently owned by Audi AG and BMW, since the HIS consortium does not exist anymore.
1.5  Acronyms
Acronym
Meaning / Description
ACMU
Analog Clock Monitoring Unit
ADKP
Application Debug Key/Password; one-time programmable parameter
AES
Advanced Encryption Standard; a cipher primitive
AES-ACCEL
Advanced Encryption Standard Accelerator
CUST
Identifies direct customer of NXP to which the devices are delivered for ECU manufacturing
DER
Distinguished Encoding Rules; a standardized encoding method of Abstract Syntax Notation One (ASN.1)
commonly used to encode public key certificates
DH
A key agreement protocol named after the creators Mr. Diffie and Mr. Hellman
DID
Domain ID (in XRDC)
DIP
Dual In-line Package
DRBG
Deterministic Random Bit Generator – same as DRNG
DRNG
Deterministic Random Number Generator
Table 2. Acronyms
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
4 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 5

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Acronym
Meaning / Description
ECC
Elliptic Curve Cryptography; a public-key cryptosystem; Also, Error Correcting Code
ECDH
A key agreement protocol combining ECC and DH algorithm
ECDSA
Elliptic Curve Digital Signature Algorithm
ECU
Electronic Control Unit; an embedded system that controls one or more of the electrical systems in a car
EdDSA
Edwards-curve Digital Signature Algorithm
FIRC
Fast Internal Reference Clock
FW-IMG
The HSE firmware image as provided by NXP (also called Pink FW-IMG)
FW-IMG*
The FW-IMG reencrypted using a device-specific key (also called Blue FW-IMG)
GF
Galois Field
HID
Host Identity, determined by the device life cycle and the execution rights
HSE
Hardware Security Engine
I2C
Inter-Integrated Circuit (standard communication bus)
IC
Integrated Circuit; For this document, it refers to NXP ICs
ID
Identifier
IVT
Image Vector Table; references pointers (addresses) to different system images
JTAG
Named after the Joint Test Action Group that standardized a test and debug interface
KDF
Key Derivation Function
LC
Device Life Cycle; used to limit by design the configuration and debug/test possibilities of the device for in-field
usage
LSB
The Least Significant Bits, or the last bits of value in reading order
MAC
Message Authentication Code; by extension: HMAC, CMAC, and so forth, are different types of MAC
MACsec
Media Access Control security
MSB
Most Significant Bits, or the first bits of a value in reading order
MU
Messaging Unit; the communication interface between the host and the HSE
MSC
Managed Security Component – any hardware accelerator on the host-side that uses the keys managed by HSE
firmware
N/A
Not Applicable
NVM
Non-Volatile Memory; typically Flash that can be embedded in the device or externally connected to the device
OEM
Original Equipment Manufacturer; the final user of NXP device after it has been integrated into an ECU
OID
Object Identifier; an encoded identifier of a standardized object commonly used in public key certificates
OTP
One-Time Programmable; applies to NVM
PID
Process ID (in XRDC)
PLL
Phase-Locked Loop (clock)
PRF
Pseudo-Random Function
PRNG
Pseudo Random Number Generator – same as DRNG
QuadSPI
Quad Serial Peripheral Interface; used to connect serial NOR Flash modules
RFU
Reserved for Future Use
RSA
A public-key cryptosystem named after the inventors Mr. Rivest, Mr. Shamir, and Mr. Adleman
SBAF
Secure Boot Assist Flash. Boot component in HSE.
SHA
Secure Hash Algorithm; a set of hash primitives
SMR
Secure Memory Region; used to verify memory areas at start-up (secure boot) and during run-time
Table 2. Acronyms...continued
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
5 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 6

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Acronym
Meaning / Description
TRNG
True Random Number Generator
XOR
Exclusive OR (binary operation)
XRDC
Extended Resource Domain Controller; can restrict master access to certain memory-mapped resources (RAM,
peripherals, and so forth)
Table 2. Acronyms...continued
1.6  Conventions and notations
1.6.1  Number representation
Number endianness or byte and bit order relates to the memory representation of a number. Two forms of
endianness exist; big and little. Numbers in big-endian form are represented in memory in the same way as they
are written (from left to right), that is, with the most significant bits first. Number in little-endian form, however,
are represented in memory with their least significant bits first. In addition, the little-endian form requires to
specify the size of the biggest word for which the byte and bit order swap applies.
64-bit number 0x1122334455667788
Byte ordering in memory from address A (in hexadecimal form)
Byte address
A
A+1
A+2
A+3
A+4
A+5
A+6
A+7
Big-endian form
11
22
33
44
55
66
77
88
64-bit little-endian form
88
77
66
55
44
33
22
11
32-bit little-endian form
44
33
22
11
88
77
66
55
16-bit little-endian form
22
11
44
33
66
55
88
77
Table 3. Illustrating big- vs. little-endianness byte ordering
Unless otherwise indicated, all numbers are represented in the big-endian form with the most significant digit or
bit first (from left to right).
Large integers (keys, messages, and so forth) are represented in the API as byte arrays.
For a byte array T[] of n elements, the first element is T[0] and the last element is T[n-1]. If the address of
T[0] is A, the address of T[n-1] is (A+n-1). The most significant byte of the number represented by T is the
byte T[0]. The least significant byte of the number represented by T is the byte T[n-1].
Byte array T[] with n##elements
Address of each element T[i]
T[0]
A
A+1
A+n-1
T[1]
T[n-1]
...
Figure 1. Illustrating a byte array storage in memory
Hexadecimal numbers are provided with the prefix “0x”. For instance, “0x0A” equals to the decimal value 10.
Binary values with 2 bits or more are ended with the subscript “b”. For instance, “1010b” equals to the decimal
value 10.
1.6.2  C-like memory representation
A 'pointer' refers to a memory address. A 'pointer to X' refers to the address of the first byte of the value X.
A pointer set to NULL by the host indicates a pointer not processed (that is, not used) by the HSE.
If 'Ptr' is defined as a memory pointer, '*Ptr' refers to the value read at the memory location 'Ptr'.
If 'Ptr' is defined as a pointer to a structure, 'Ptr→X' refers to the data field 'X' within that structure.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
6 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 7

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
If 'Struct' is defined as a structure, 'Struct.X' refers to the data field 'X' within that structure.
1.6.3  Mathematical notations and functions
An interval in the integer finite field is noted “i ~ j” and corresponds to all integers between i and j.
The operator mod is a modulus calculation; “a mod n” refers to the remainder of the division of a by n (for
example, 15 mod 10 = 5, 8 mod 2 = 0). The function ceil(x) returns the smallest integer greater than or
equal to the real number x (for example, ceil(15∕2) = 8, ceil(16) = 16).
1.6.4  Cryptographic notations
A “plaintext” (key, text, file, message, and so on) refers to an unencrypted value.
A “ciphertext” (key, text, file, message, and so on) refers to an encrypted value.
The x and y coordinates of a point Q (on an elliptic curve) are noted Q.x and Q.y respectively.
Eb() is the encryption function using the key k.Dk() is the decryption function using the key k. The underlying
cipher primitive supported by the HSE is AES.
1.6.5  Bit manipulation functions
The symbol “|” corresponds to the binary OR operation. For instance, 0xAA | 0x55 equals to 0xFF.
The symbol “&” corresponds to the binary AND operation. For instance, 0xAF & 0x55 equals to 0x05.
The symbol “⊕” corresponds to the binary exclusive OR (XOR) operation. For instance, 0xAF ⊕ 0x5F equals
0xF0.
The symbol “||” corresponds to the concatenation operation. For instance, 0xAA || 0x55 equals to 0xAA55.
The function msb(M,l) returns the l MSB of the message M.
The function lsb(M,l) returns the l LSB of the message M.
The function pad(M,l) is padding the message M with zeroes on the LSB side to align its size on a multiple of
l bits.
The function bitsize(M,l) returns the size in bits of the given message M padded with leading zeroes on the
MSB side to obtain a l-bit number. If l is omitted, the leading zeroes are discarded.
The function size(M,l) returns the size in bytes of the given message M padded with leading zeroes on the
MSB side to obtain a l-bit number. If is omitted, the leading zeroes are discarded.
The function array(B,n) is a byte array having n elements of value B.
The function add(X,Y,l) increments by Y the (l - 1) bits on the LSB side of X. It is defined as follows:
add(X,Y,l) = (X ⊕ W) + (W + Y) mod 2l with W = X mod 2l
Examples:
            M = 0xF0F1F2F3
     msb(M,8) = 0xF0
     lsb(M,8) = 0xF3
    pad(M,40) = 0xF0F1F2F300
    pad(M,64) = 0xF0F1F2F300000000
bitsize(M,32) = 0x00000020
bitsize(M,64) = 0x0000000000000020
   size(M,16) = 0x0004
      size(M) = 4
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
7 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 8

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
array(0xFF,2) = 0xFFFF
array(0xA5,4) = 0xA5A5A5A5
            X = 0xAABBFF
   add(X,1,8) = 0xAABB00
  add(X,8,16) = 0xAABC07
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
8 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 9

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
2   High-Level System View
2.1  Top-level system architecture
NXP S32K3xx and S32M27x devices feature:
• An application domain referred to as the host
• A security domain
Figure 2. Top-level system view (simplified)
The application domain comprises various system resources:
• One or several CPU subsystems
• On-chip memory resources (RAM, NVM)
• Several peripheral subsystems such as communication interfaces, timers, encoders/decoders
• Interfaces to external memory resources
• A system bus that is interconnecting all system resources together
The security domain is the Hardware Security Engine (HSE) subsystem. It has its own exclusive system
resources (see section The HSE Subsystem) and connects to the host via a dedicated interface.
The device subsystems (including the HSE) are also referred to as system masters (or masters).
A system master has read and/or write access, via the system bus, to certain on-chip and off-chip resources.
Each master is tagged with a unique identifier. Access restrictions are either defined by design (that is the case
for the HSE) or by specific device configuration, via the eXtended Resource Domain Controller (XRDC).
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
9 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 10

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
For system details on the host (block diagrams, memory resources available, peripheral descriptions, and so
on), refer to the S32K3xx Reference Manual.
2.2  The host
2.2.1  CPU subsystems
A CPU subsystem within the host contains a CPU (core) and dedicated CPU resources (cache memories,
interrupt controller, floating point units, and so on). It processes the application images (executable,
configuration data, application data, and so on) and controls the system resources to achieve the desired
functions in the target ECU where the device integrates (for example, gateway).
The host can feature several CPU subsystems.
2.2.2  Memory resources
2.2.2.1  Application RAM
Application RAM refers to on-chip and external RAM areas accessible by any system master.
2.2.2.2  Application NVM
Application NVM refers to nonvolatile memories accessible by any system masters.
In devices with embedded Flash, the application NVM maps to:
• A one-time-programmable (OTP) on-chip nonvolatile memory; for information related to read and program this
memory, refer DCF sheet attached in S32K3xx Reference Manual.
• In devices with embedded Flash, the application NVM maps to the on-chip Code and Data Flash.
• The total available on-chip flash memory available for code execution depends on the device memory
configuration. Refer to the section Device Specific Parameters (S32K3xx) for more information.
2.2.3  Unique device identifier (UID)
NXP provisions a 64-bit unique device identifier (UID) in the application OTP area. This UID uniquely identifies
each device from any other.
The UID can be retrieved through the SDA-AP interface as explained in the S32K3xx Reference Manual. It can
also be retrieved from OTP non-volatile memory region. Details are explained in the DCF sheet attached in the
S32K3xx Reference Manual.
2.2.4  Host system images
The host system images required to operate in a device with embedded Flash are:
• The Image Vector Table referred to as IVT.
• Various applications images (executables, data, and so on) referred to as Apps.
• An (optional) authenticated application image referred to as AppBL. It can run in the host in lieu of the Apps
and after the HSE has verified its authenticity.
Note:  IVT is sometimes referred to as the "boot header".
The IVT is the main entry point for the system to operate after reset. It contains:
• The storage location of Apps and firmware executable (encrypted).
• The Boot Configuration Word (BCW) that configures the startup behavior; see BCW Content.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
10 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 11

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• Life-cycle Configuration Word (LCW) that allows the host to advance the life-cycle state whenever the HSE
firmware is not operating (that is, not available). When the HSE operates, the life cycle can also be advanced
using the HSE system attribute management services.
The IVT can hold an optional authentication tag that guarantees its integrity and authenticity. The HSE
calculates it on-demand from the host via one specific administration service (see Authenticate the Host System
Images) and verifies it at startup when it is configured to do so (see IVT_AUTH). By design, the storage location
of the IVT is fixed.
The "Apps" are the first executable to run in the host during normal operation after reset. BOOT_TARGET
in BCW select the CPU subsystems to release. The HSE can verify the authenticity of the Apps before the
related CPU subsystems are released from reset. See chapter Secure Boot and Memory Verification Services.
Alternatively, "AppBL" can run in the host after HSE verification.
For a detailed structure of IVT and AppBL, refer to the section Device Specific Parameters (S32K3xx).
2.2.5  System bus and XRDC
The system bus interconnects the CPU subsystems with the system resources: RAM and internal Flash.
The eXtended Resource Domain Controller (XRDC) can restrict certain CPU subsystems (system masters)
from accessing select system resources.
Each master is identified in the system with a Process ID (PID) and can be associated with specific resource
domains. Each resource domain is identified through a Domain ID (DID) that can be linked to a set of
peripherals (via the Peripheral Access Controlled (PAC)) and different memory ranges (via the Memory Region
Controller (MRC)).
The application primarily handles the XRDC configuration. HSE undertakes minimal configuration related to
secure area. By default, the secure code flash and secure data flash are protected and accessible only by the
HSE subsystem. The size of all the secure memories that is, code flash, data flash, secure RAM can be read
from the HSE GPR register (refer to section HSE Secure Memory Sizes in HSE GPR Registers).
For more information on the FULL_MEM and AB_SWAP, refer to the section Flash Memory Configuration.
2.3  The HSE subsystem
The Hardware Security Engine (HSE) is a security subsystem, which aims at running relevant security functions
for applications having stringent confidentiality and/or authenticity requirements, with the following foremost
objectives:
• Safekeeping security-sensitive information (for example, secret key values) for the application (the host)
• Offloading the application by processing cryptographic operations with dedicated coprocessors
• Enforcing security measures for the application, during runtime and system startup
The HSE subsystem is the only master that operates after power-on reset (POR). It selectively releases CPU
subsystems in the host from reset, with the opportunity to apply certain checks beforehand (secure boot). It can
also trigger interrupts and reset signals to the host during runtime, based on certain conditions.
2.3.1  HSE subsystem variants and software packages
The HSE subsystem exists in three variants, depending on the device in which it integrates:
• HSE_H (High) are available on Flash-less S32x product variants (such as S32G2, S32G3, S32ZSE, and
S32R45)
• HSE_M (Medium) is available on Flash-less S32x product variants (such as S32R41 and SAF85)
• HSE_B (Base) are available in S32x product variants with embedded Flash (such as S32K3XX).
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
11 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 12

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The HSE firmware is available as described below:
• The Standard package supports all the features as described in this reference manual and the HSE Service
API Reference Manual delivered with the HSE Firmware Package.
• The Premium package is a custom firmware supporting specific functions; contact the NXP sales
representation for further details.
2.3.2  CPU subsystem
The HSE CPU subsystem processes the HSE images and controls its subsystem resources to offer a set
of security services to the application domain (the host). For more information, see the HSE Service API
Reference Manual.
2.3.3  Cryptographic accelerators
The HSE subsystem features the following cryptographic accelerators:
• An AES engine supporting all standard key sizes (128, 192, 256 bits) and various complex ciphering modes
(CBC, CTR, GCM, and so on).
• A hash engine that supports standard SHA1 and SHA2 hash primitives up to 256-bit digest. For SHA-384 and
SHA-512, software support is available.
• A Public Key Cryptography (PKC) engine, which accelerates RSA and ECC operations.
2.3.4  True random number generator
The HSE subsystem features a True Random Number Generator (TRNG) which is used as the entropy source
to seed the Deterministic Random Number Generator (DRNG, aka DRBG or PRNG) available to the host via
dedicated random generation services.
The TRNG complies with the following standards:
• AIS31 Class P2 High (see the Functionality classes and evaluation methodology for true (physical) random
number generators document)
• FIPS 140-2
2.3.5  System timers for self-monitoring
The HSE subsystems feature a system timer to allow recurring autonomous functions such as runtime memory
verification checks, and a watchdog timer to reset the HSE subsystem if there is unexpected runtime failure.
2.3.6  Memory resources
2.3.6.1  Secure RAM
Secure RAM refers to RAM areas exclusively accessible by the HSE subsystem, and used to operate the HSE,
and to store a copy of the cryptographic keys in service.
2.3.6.2  Secure NVM
Secure NVM refers to nonvolatile memories that are exclusively accessible by the HSE subsystem .
For HSE_B, the secure NVM maps to the on-chip code, data, and configuration (aka UTEST) Flash areas
configured by the system to be only accessible by the HSE subsystem. This implies that the total available NVM
for the application is reduced by the size of those HSE memory areas.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
12 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 13

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The HSE-exclusive code (aka HSE code Flash) and data (aka HSE data Flash) Flash areas map to the end of
the available memory spaces.
Part of the configuration memory area, referred to as UTEST, is also exclusively reserved for the HSE
subsystem.
See chapter Device Specific Parameters (S32K3xx) for the mapping of the NVM in the host.
2.3.6.3  Memory mapped resources accessible by the HSE
By default, the HSE subsystem has unrestricted access to memory-mapped system resources via the system
bus.
It is possible to restrict its access to Non Secure Resources via the XRDC configuration by the application.
The HSE subsystem has a fixed PID (Process ID) and can be allocated to one DID via the Master Domain
Assignment in the XRDC.
2.3.7  HSE images
2.3.7.1  Overview
The HSE images are:
• The HSE firmware executable referred to as FW-IMG
• The HSE system image that contains public and private (secret) keys, monotonic counters, and configuration
data (aka HSE system attributes), referred to as SYS-IMG
The location, access, and update policies that apply to each HSE image depend on the type of host where the
HSE integrates.
The HSE_B subsystems have all their images stored in the secure NVM mapping to the embedded Flash:
1. FW-IMG is stored in the HSE code Flash area
2. FW-IMG backup is stored in:
• HSE data flash area for FULL_MEM configuration (Refer to section Installation Process in FULL_MEM
Configuration)
• HSE code flash area for AB_SWAP configuration (Refer to section Installation Process in AB_SWAP
Configuration)
3. SYS-IMG is stored in the HSE data Flash area
The HSE images are read-out and updated exclusively by the HSE.
2.3.8  Life cycle (LC)
The life cycle (LC) is an internal device state which conditions access to certain system and HSE functionalities
and configuration options.
The HSE subsystem manages the LC. The LC state can be read-out and modified via the HSE system attribute
management services. The LC state can also be advanced using the LCW within the IVT.
The LC states link with the HSE firmware installation and configuration phases.
A parallel can be drawn between the LC states and the ECU manufacturing steps, in-vehicle usage, and testing
for failure analysis.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
13 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 14

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
LC state
Description
CUST_DEL
Device (that is, NXP IC) delivered to system integrator (that is, NXP’s customer) for ECU
manufacturing and initial configuration.
OEM_PROD
ECU (device) delivered to the OEM for vehicle integration and final configuration.
IN_FIELD
ECU integrated in the vehicle and operating; it is the state of normal device use (and most
secure state).
PRE_FA
Similar to IN_FIELD; Provides capabilities for failure analysis.
FA
ECU (device) failure; this is the state for functional testing of the IC.
Table 4. LC states
To enable analysis of failing devices by NXP, the device can be advanced to the FA lifecycle or the PRE_FA
mode:
• Advancing to the FA lifecycle requires an NXP secret and only NXP can do it. In FA LC, the SBAF doesn't
erase the customer assets. If a customer asset is present then it is accessible similar to the Customer
Application. Advancing the device to the FA lifecycle is a destructive operation, meaning that the device
cannot be used for normal operation anymore.
• Advancing to the PRE_FA life cycle can only be done by NXP. This life cycle enables a limited set of test
features while keeping the device capability like IN_FIELD life cycle ((device operates like IN_FIELD).
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
14 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 15

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
LC == CUST_DEL
HSE firmware not installed
LC == CUST_DEL
HSE firmware not configured
LC == OEM_PROD
HSE firmware partially configured
LC == IN_FIELD
HSE firmware fully configured
installation
configuration (partial)
configuration (complete)
LC == PRE_FA
HSE firmware fully configured
prepare for failure analysis
configuration (complete)
LC == FA
HSE firmware not operating
failure analysis
Figure 3. HSE installation / configuration states vs. LC states: (Frame of reference from SBAF (HSE Core))
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
15 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 16

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
LC == CUST_DEL
HSE firmware not installed
LC == CUST_DEL
HSE firmware not configured
LC == OEM_PROD
HSE firmware partially configured
LC == IN_FIELD
HSE firmware fully configured
installation
configuration (partial)
configuration (complete)
LC == PRE_FA
HSE firmware fully configured
prepare for failure analysis
configuration 
(complete)
prepare for
failure analysis
LC == FA
HSE firmware not operating
failure analysis
Figure 4. HSE installation / configuration states vs. LC states: (Frame of reference from Host Core)
The following table lists the HSE firmware services and configuration options that are available to the host,
depending on the LC state.
LC state
HSE firmware capabilities
CUST_DEL
HSE firmware ready for installation and configuration.
OEM_PROD
HSE firmware ready for additional configuration; no restrictions except those implicitly implied
by the security policies.
IN_FIELD
Key management capabilities (import, export, and so on) are restricted (most secure state).
PRE_FA
HSE firmware fully configured. It is similar to IN_FIELD.
FA
HSE firmware not operating.
Table 5. HSE firmware capabilities vs. LC
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
16 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 17

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The below table lists the host debugging capabilities that are available, depending on the LC state.
LC state
Host debugging
CUST_DEL
Host debug open (unrestricted)
OEM_PROD
IN_FIELD
Host debug protected (with ADKP) or permanently disabled
PRE_FA
Host debug protected (with ADKP) or permanently disabled
FA
HSE debug open and Host Core not open
Table 6. Host debugging capabilities vs. LC
When moving toward the different configuration phases, the host can advance the LC using:
• The LCW in the IVT; in this case, the LC state is changed by the HSE during start-up (reset).
• Or via the HSE system attribute management services; according to how the HSE changes the LC state
during runtime.
In both cases, the new LC state is considered after reset.
Important:
An LC transition is always one way. Reverting to a previous LC state is never possible.
Only NXP can process the LC transition from CUST_DEL, OEM_PROD or IN_FIELD to PRE_FA or FA.
If HSE FW Feature Enable:
The transition from CUST_DEL to OEM_PROD or IN_FIELD is only possible if the application debug key /
password (ADKP at 0x1b000360) is provisioned.
If HSE FW Feature Disable:
The transition from CUST_DEL to OEM_PROD or IN_FIELD is only possible if the application password
(Password at 0x1b000080) is provisioned.
LC transition is not possible through LCW in IVT when the user has installed the HSE Firmware in the device.
2.4  HSE subsystem software components
There are two software components that operate the HSE subsystem:
• SBAF
• HSE Firmware
2.4.1  SBAF
Secure Boot Assist Flash (aka SBAF) is a software component programmed in devices by NXP during
production. This software component resides in the HSE code flash area. The features provided by this
software component are:
• Secure and Non-secure boot modes
• Application boot core selection
• HSE firmware installation
• HSE firmware restoration
• HSE firmware boot
• Device OTA feature enablement
• Chip LC advancement
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
17 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 18

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• Debug authorization
• Partition swapping enablement
• XRDC configuration
• FA advancement
• Support in firmware update
• Secure and JTAG-based recovery mode
• HSE firmware handshake
• HSE firmware update support
• ECC error detection/handling
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
18 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 19

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
2.4.2  The HSE firmware
The HSE firmware is the software component that provides various native security services as described below.
2.4.2.1  HSE firmware deliverables
The HSE firmware deliverables consist of several files as summarized in the below table.
Filename
Description
hse_interface.h
hse_srv_responses.h
hse_status_and_errors.h
hse_gpr_status.h
std_typedefs.h
Header files for the HSE firmware API and security services
to be included in the host driver (application).
These header files also contain information that explains
about the various error codes and status returned from HSE
firmware.
hse_srv_<xxx>.h
Header files for the security service <xxx>; all service
header files are included in the file hse_interface.h
hse_srv_custom.h
Header file for the custom HSE firmware API and security
services. It is to be included in the host driver. Not needed
for Standard FW Type.
hse_config.h
hse_target.h
hse_platform.h
hse_b_config.h
hse_compile_abs.h
hse_compile_defs.h
Header files that identify what features are implemented in
the HSE firmware, depending on the selected configuration
and target device.
All enabled HSE features are listed in the hse_b_config.h file
(the features commented/disabled in hse_b config.h file are
not supported)
<device>_hse_fw_<config>_<version>.bin.pink
The HSE firmware in executable form. The filename includes
the HSE firmware platform, software package, version, and
date (for example, s32k3x4_hse_fw_0.5.0_0.12.0_pb210720
.bin.pink) that are correlated with the hse_target.h header
file.
Table 7. HSE firmware deliverables
2.4.2.2  HSE security services
The native security services refer to the services available in the HSE firmware provided by NXP.
These native services are split in the following service classes:
• Administration services are provided to install, configure, and test the HSE.
• Key management services are available for the application to manage different sets of keys that are handled
by the HSE, for example, through the cryptographic services.
• Cryptographic services provide the application with cryptographic primitives that are used by high-level
security stacks in the application.
• Random number services generate random streams that can be used in various security protocols.
• Memory verification services allow the application to verify different memory areas at startup (after reset)
and during runtime.
• Monotonic counter services provide the application with a set of monotonic counters that can be read and
only incremented.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
19 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 20

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
2.4.2.3  General operation flow
2.4.2.3.1  Installation
The HSE firmware executable is delivered encrypted and authenticated. The installation of the HSE firmware
entails:
• Transferring the HSE firmware to the HSE code Flash area
• Decrypting the firmware
• Verifying the authenticity of the firmware
The necessary keys to decrypt and verify the authenticity of the HSE firmware are provisioned by NXP (before
shipment) in secure NVM within the HSE subsystem. The keys are provisioned in the ROM Key Catalog instead
of the Secure NVM to avoid misreading of the keys being in the NVM Key Catalog.
The HSE firmware installation is initiated during device startup, under certain conditions, when the executable
is provided to the HSE subsystem. For details on the HSE firmware installation, see chapter HSE Firmware
Installation.
2.4.2.3.2  Configuration
Once the HSE firmware executable has been installed, it must be configured to operate according to the
security policies defined at the system level. This configuration step involves:
• Creating and formatting the key catalogs that hold the keys to be used by the application and the HSE
• Provisioning the key values and attributes in the nonvolatile key catalog
• Configuring the application boot conditions based on the authenticity of certain memory regions
• Configuring specific security policies controlled by the HSE (for example, periodic memory verification checks)
• Configuring the various monotonic counters
The HSE firmware configuration is controlled and handled, under certain conditions, by the application through
the different HSE services available. For details on the HSE firmware configuration, see the chapter HSE
Firmware Configuration.
2.4.2.3.3  Usage
Once configured, the HSE essentially serves the host with a set of security services. In this context, the HSE
subsystem is a slave to the host, and responds to service requests triggered from one or multiple application
CPU subsystems.
Before triggering a service request, host must ensure HSE_STATUS_INIT_OK is set.
The host must wait for HSE_STATUS_INIT_OK before changing the device clock configurations like enabling
PLL.
To trigger a service request to the HSE subsystem, the host:
• Formats (that is, instantiates) the request within a dedicated data structure, referred to as the service
descriptor, where each field corresponds to the parameters of the service.
• Stores the service request within RAM that can also be read and written by the HSE subsystem.
• Provides the address of that service descriptor via a dedicated Messaging Unit (MU). This operation triggers
an interrupt signal to the HSE subsystem to indicate a pending service request.
All service requests end up with a service response written by the HSE into a dedicated register within the MU
(see Messaging unit). If a service response is not received, then there is a possibility that FW has encountered
an error and has gone into shutdown mode. In that case, the application must refer to register GSR in MU for
more details. For more details, refer to Error and Warning Management.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
20 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 21

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
To check for completion of a service, the host can regularly check for the availability of a response (error code)
within the MU. It can optionally serve the interrupt request triggered by the HSE subsystem (via the MU) which
indicates that a service processing is completed.
The HSE subsystem has read and write-access to all system resources that are also accessible by the host,
except for resources that are protected by the host (for example, for safety purposes). Most of the service
requests contain pointers to byte arrays that represent either the data to be read (and processed) by the HSE,
or the buffer to be filled-in by the HSE.
The detailed structure format for each service can be found in the HSE Service API Reference Manual.
2.4.2.3.4  Autonomous operations
The HSE subsystem is the only master to operate after power-on reset (POR). The HSE starts running after
startup (that is, before the application) and performs various operations that are not all visible to the host:
• It releases from reset the CPU subsystems in the host, after having verified the authenticity of predefined
memory areas, when configured to do so.
• It performs background memory verification checks during runtime, when configured to do so.
• It informs the host on the overall security status based on background verification checks and other
conditions.
Those autonomous operations are configurable by the host, as described in this document.
2.4.2.4  Special operation flow
2.4.2.4.1  Firmware update
A specific service allows the host to update the HSE firmware in a secure manner. Such an update can be
initiated at any time providing that the HSE firmware is operating. For details, see the chapter HSE Firmware
Updates.
2.5  The HSE interface
2.5.1  Messaging Unit (MU)
2.5.1.1  Overview
The Messaging Unit (MU) is the communication interface between the host and the HSE subsystem. It is used
by the host to trigger service requests and receive service responses. It is used by the HSE to receive service
requests, return service responses and provide several HSE status information relevant to the host.
Note:
The MU has two sides, referred to as MUA and MUB. The HSE has exclusive control over one side (MUA) while
the host controls the other side (MUB). A value written in a transmit register (TRi) on one side can be read in
the corresponding receive register (RRi) on the other side. Similarly, select control registers on one side (for
example, FCR) interact with status registers on the other side (for example, FSR).
The MU description in this document is done from the host perspective (MUB). Therefore, only the registers that
are in use to interact with the HSE are documented here.
Each of the MU instances available in the system has:
• A set of 32-bit readable and writable transmit registers (TRi), to provide the address of the service descriptors
to process by the HSE
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
21 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 22

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• A set of 32-bit read-only receive registers (RRi), to retrieve the responses to the service requests
• Two 32-bit read-only status registers (FSR and GSR), to log HSE status and system events
• Control and status registers to manage the access to the transmit and receive registers, and the related
interrupt signals
The number of available MU instances and TRi/RRi registers is device (host) dependent.
See Device Specific Parameters for the number of MU instances in different S32x devices.
Messaging Unit (MU) instance 1
Messaging Unit (MU) instance 0
service
channel0
FSR: HSE firmware status
TSR: transmit status (full / empty)
RSR: receive status (full / empty)
service
channel 1
RR1: service response
service
channel2
TR2: service descriptoraddr.
RR2: service response
service
channel 3
TR3: service descriptoraddr.
RR3: service response
HSE/host interface RAM
Service
Descriptor
(e.g. encryption)
Service
Descriptor
(e.g. hashing)
TR1: service descriptoraddr.
RR0: service response
TR0: service descriptoraddr.
Application RAM
Plain text
Cipher text
Hash value
GSR: HSE system events
INT
INT
INT
TCR: Transmit control register
RCR: Receive control register
Figure 5. Illustrating the Messaging Unit (MU)
The advantages of using the MU to manage the HSE service requests and responses are manifold:
• Hardware mechanisms are in place on the transmit/receive registers to avoid overrun on service requests
• Interrupt signals are available to allow asynchronous management of the requests (avoiding active waiting
loops)
• Each MU instance can be configured with specific access restrictions that can be used, for example, to isolate
the requests made by different masters (in different MU instances); such access control can be configured via
the XRDC
• It is possible to restrict the cryptographic key usage by MU instances
For details on the MU, refer to the S32K3xx Reference Manual.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
22 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 23

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
2.5.1.2  Service channel
A service channel is a transient construct, which links to one service request (once started) and maps to a pair
of TRi/RRi registers (in one MU instance).
A service channel #i is free until the host opens the channel by writing the service descriptor address in the
corresponding TRi register. It is busy until completion of the service execution by the HSE, and until the host
has read the response from the corresponding RRi register.
Free
Busy
Opened by the host
Closed by the HSE
and response read by the host
Figure 6. Service channel status transitions
The maximum number of service channels the host can simultaneously open equals the number of MU
instances multiplied by the number of TRi registers.For example, in S32K344: up to 2 x 4 = 8 service channels
can be opened simultaneously.
The service channel #i is free when all the following conditions are true:
• Register TRi is empty, that is, the value previously written in TRi has been read by the HSE
– This is true when bit #i in register TSR equals 1
• Register RRi is empty, that is, the previous value has been read by the host
– This is true when bit #i in register RSR equals 0
• The service channel #i is not being processed
– This is true when bit #i in register FSR equals 0
The service channel #i is opened when the host writes, in TRi, the address of the service descriptor to process
by the HSE.
The first service channel found free in a given MU instance can be used to trigger a service request. The
service channel #0 must only be used to request for administration services: triggering another class of service
on channel #0 generates an error. There is no restriction on the other service channels as per the service class.
Note that the channel #0 of any other enabled MU instance can request for administrative services.
Opening a service channel that is not free must be avoided.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
23 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 24

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The below table summarizes the MU registers in play for the service channel #i.
MU register
Access rights
Usage / description
TRi
Write[1]
Contains a 32-bit memory address pointing to the service descriptor
TSR bit #i
Read-only
Service request acknowledged (by the HSE)
Automatically cleared to 0 when TRi is written by the host
Automatically set to 1 when the HSE has read TRi
RRi
Read-only
Contains a 32-bit integer indicating the service response (OK / error)
RSR bit #i
Read-only
Service response acknowledged (by the host)
Automatically set to 1 when the HSE has written RRi
Automatically cleared to 0 when RRi has been read by the host
FSR bit #i
Read-only
Service execution status
Set to 1 by the HSE whenever the service is acknowledged and
queued (that is, execution in progress)
Cleared to 0 by the HSE whenever a service response is provided
(that is, execution finished)
Table 8. MU register usage for service channel #i (from the host perspective)
[1]
Reading TRi (from the host side) always returns 0x00000000.
2.5.1.3  HSE status
Bits 0 to 15 in the read-only register FSR provide the execution status of each service channel as described in
MU Register Usage. Bits 16 to 31 log HSE status bits as described in the below table.
Note:  The values of bits 16 to 31 are replicated in all MU instances. Reading this upper most 16-bit word from
the FSR in MU instance 0 returns the same value as reading it from the FSR in any other MU instances.
Bit #
Description
31
RFU
30
HSE_STATUS_PUBLISH_NVM_KEYSTORE_RAM_TO_FLASH: signals the application to publish
the SYS-IMG to Secure NVM; the host must trigger the service HSE_SRV_ID_PUBLISH_NVM_
KEYSTORE_RAM_TO_FLASH
29
HSE_STATUS_FW_UPDATE_IN_PROGRESS; when set to 1, indicates that a firmware update is
in progress.
28
HSE_STATUS_OEM_SUPER_USER; when set to 1, indicates that SU rights are granted to
OWNER_OEM
27
HSE_STATUS_CUST_SUPER_USER; when set to 1, indicates that SU rights are granted to
OWNER_CUST
26
HSE_STATUS_BOOT_OK; set to 1 when all the secure boot conditions (pre-boot phase) defined
in the HSE successfully pass
25
HSE_STATUS_INSTALL_OK; set to 1 once the key catalogs have been successfully formatted;
when cleared to 0, indicates to the host that the key catalogs must be formatted
24
HSE_STATUS_INIT_OK; set to 1 when the HSE initialization is completed; when cleared to 0, no
service request can be made to the HSE (MU disabled)
23
HSE_STATUS_HSE_DEBUGGER_ACTIVE; set to 1 when an HSE debug session is active
22
HSE_STATUS_HOST_DEBUGGER_ACTIVE; set to 1 when a host debug session is active
Table 9. HSE global status bits in FSR
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
24 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 25

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Bit #
Description
21
HSE_STATUS_RNG_INIT_OK; set to 1 when the RNG initialization is complete; when cleared to
0, any services using the random number is unavailable to the host
20
HSE_SHE_STATUS_SECURE_BOOT_OK; set to 1 when SMR #0 successfully verified against
BOOT_MAC
19
HSE_SHE_STATUS_SECURE_BOOT_FINISHED; set to 1 when SMR #0 was not successfully
verified
18
HSE_SHE_STATUS_SECURE_BOOT_INIT; set to 1 when SMR #0 has been installed and
authenticated with BOOT_MAC_KEY
17
HSE_SHE_STATUS_SECURE_BOOT; set to 1 when SMR #0 has been installed and BOOT_
SEQ equals 1
16
RFU
15
Set to 1 when service channel #15 execution is in progress
14
Set to 1 when service channel #14 execution is in progress
…
…
2
Set to 1 when service channel #2 execution is in progress
1
Set to 1 when service channel #1 execution is in progress
0
Set to 1 when service channel #0 execution is in progress
Table 9. HSE global status bits in FSR...continued
Bits #17 to #20 in the HSE status relate to the secure boot management as described in SHE – Secure
Hardware Extension Functional Specification. Their values depend on the definition and the verification
status of SMR #0 as described in the below table. For more information on CMD_BOOT_OK and
CMD_BOOT_FAILURE, refer to Secure Boot and Memory Verification Services.
Condition
SECURE_BOOT
BOOT_INIT
BOOT_FINISHED
BOOT_OK
SMR #0 not defined
0
0
0
0
SMR #0 defined but
not installed
1
0
0
0
SMR #0 defined and
installed without initial
proof of authenticity
(autonomous
bootstrap)
1
1
1
0
SMR #0 defined and
successfully verified
1
0
0
1
SMR #0 defined and
successfully verified,
after CMD_BOOT_OK
1
0
1
1
SMR #0 defined,
verification failed or
after CMD_BOOT_
FAILURE
1
0
1
0
Table 10. HSE global status bits #17 to #20
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
25 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 26

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
2.5.1.4  Interrupts
Three interrupt signals per MU instance are triggered to the host whenever any of the following events occur in
one of the service channels:
• A service request is acknowledged by the HSE
• A service execution completes in the HSE
• A system event occurs in the HSE
The below table describes the HSE action related to each interrupt signal, and the condition for the interrupt
signal to be raised to the host (that is, how to unmask the interrupt signal) and the register to parse in the
interrupt handler to retrieve the interrupt source.
Event description
HSE action
Interrupt condition
Status flag to check in
interrupt handler
Acknowledge the request on
service channel #i
Reading TRi
TCR bit #i equals 1
TSR bit #i equals 1
Provide a response to the request
on service channel #i
Writing RRi
RCR bit #i equals 1
RSR bit #i equals 1
Signal the HSE system event #n
(with n between 0 and 31)
GSR bit #n set from 0 to 1 GIER bit #n equals 1
GSR bit #n equals 1
Table 11. HSE interrupt to host
The interrupt on HSE system events is only triggered when the GSR bits are transitioning from 0 to 1. To clear a
bit to 0, the host must write this bit to 1 (“w1c” or “write 1 to clear”).
For more information on interrupt management in general and the allocation of HSE interrupts in the host, refer
to the S32K3xx Reference Manual.
2.5.1.5  Restrictions on key usage
Each cryptographic key group defined by the host must be associated with one or several MU instances. The
host defines these associations as one of the configurable attributes during the key catalog formatting see
section Key Catalog.
Only when a MU instance is associated with a key, the service requests triggered via this instance can make
use of that key. By allocating different MU instances to different masters (CPUs) via the XRDC, the HSE
enforces the usage of specific keys for specific tasks or applications.
2.5.1.6  Access restrictions enforced by the XRDC
The XRDC configuration can allocate each MU instance to a Domain ID (DID) via the Peripheral Access
Controller (PAC) and its Peripheral Domain Access Control (PDAC) registers.
Each domain can then be allocated to different CPU subsystems. This process allows isolation for the usage of
different sets of keys for different applications (run by different CPU subsystems).
The below figure illustrates how different applications can be partitioned to access different sets of keys within
the HSE subsystem.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
26 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 27

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Figure 7. Illustrating application, MU instances and key group partitioning
The Domain (DID) 0 includes the MU instance 0 and Application 1 that resides in the application flash block.
The Domain 1 includes the MU instances 1 and Application 2.
The Domain 0 is linked (via its PID) to the M7_0 CPU subsystem. The Domain 1 is linked (via its PID) to the
M7_1 CPU subsystem instance 1. Through these associations, the two applications can use two different sets
of keys declared in the NVM catalogs of the HSE.
For more information on the XRDC and its configuration by the application, refer to chapter “Extended Resource
Domain Controller (XRDC)” from the S32K3xx Reference Manual.
For more information on the association between keys and MU instances, refer to the section Key Catalog.
2.5.1.7  Enabling or disabling service channels
The host can enable or disable service channels within a specific MU instance. When the host disables a MU
instance, the HSE does not serve any service channels in that MU instance.
The enablement and disablement of MU instances is handled via the HSE system attributes that also define the
HSE/host interface RAM access restrictions (see section Manage HSE System Attributes).
By default, only the MU instance 0 is enabled. All other MU instances are disabled. In addition, it is not possible
to configure the MU instance 0 as disabled.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
27 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 28

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
2.5.1.8  Reference HSE MU driver
A reference HSE MU driver is provided upon request. It covers the necessary functionalities to find a free
service channel, open a service channel, check for the completion of a service request, and enable or disable
the related interrupt signals. This reference HSE MU driver is also included in NXP production software package
(AUTOSAR, QNX, and so on).
Function call
Description
ch = HSE_MU_GetFreeChannel(MU)
Returns the first free service channel (ch) available in the
specified MU instance; returns 0xFF when there is no free
service channel available
status = HSE_MU_GetChannelStatus(MU, ch)
Returns the status (busy/free) of the service channel (ch) in
the specified MU instance
HSE_MU_IsAckPending(MU, ch)
Returns true if the HSE acknowledgment is pending for the
service channel (ch) in the specified MU instance
HSE_MU_IsResponseReady(MU, ch)
Returns true if a response is ready to be read for the service
channel (ch) in the specified MU instance
HSE_MU_SendRequest(MU, ch, addr)
Triggers a service request for the service channel (ch) in the
specified MU instance, providing the address (addr) of the
service descriptor
err = HSE_MU_ReceiveResponse(MU, ch)
Reads-out the service result for the service channel (ch) in
the specified MU instance
status = HSE_MU_GetHSEStatus(MU)
Reads-out the 16-bit HSE status (upper most 16-bit word in
register FSR) from the specified MU instance
HSE_MU_EnableInterrupts(MU, type, mask)
Enables one type of interrupt signal based on a bit field
mask for the specified MU instance
HSE_MU_DisableInterrupts(MU, type, mask)
Disables one type of interrupt signal based on a bit field
mask for the specified MU instance
Table 12. Functions covered by the reference HSE MU driver
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
28 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 29

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The below code snippet illustrates how to trigger a service request on a free service channel and wait for the
response.
 
    // trigger a service requests on a free channel
    // wait for the response and return (blocking call)
    // takes in input the address to the service descriptor
    hseSrvResponse_t runSrv(hseSrvDescriptor_t *pSrvDesc)
    {
        // get a free service channel in MU 0
        uint8_t MU = 0;
        hseSrvResponse_t hseResp = HSE_SRV_RSP_NOT_SUPPORTED;
        uint8_t ch = HSE_MU_GetFreeChannel(MU);
        if(ch != HSE_INVALID_CHANNEL)
        {
            // trigger the service request
            HSE_MU_SendRequest(MU, ch, pSrvDesc);
            // wait for the response
            while(!HSE_MU_IsResponseReady(MU, ch));
            hseResp = HSE_MU_ReceiveResponse(MU, ch);
        }
        return (hseResp);
    }
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
29 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 30

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The below code snippet illustrates how to trigger a service request on a specific service channel, wait for the
request acknowledgment, and then serve the interrupt upon service completion (interrupt handler declaration
not described).
 
            MU = 0; 
            ch = 1; 
            //disable interrupts on HSE acknowledgement 
            HSE_MU_DisableInterrupts(MU, HSE_INT_ACK_REQUEST, 0xFFFF); 
            // enable interrupt on HSE response, for the selected service channel 
            HSE_MU_EnableInterrupts (MU, HSE_INT_RESPONSE, (1 << ch)); 
            //enable all system event interrupts 
            HSE_MU_EnableInterrupts (MU, HSE_INT_SYS_EVENT, 0xFFFFFFFF); 
            // trigger the service request and wait for the HSE acknowledgement
            if(HSE_MU_GetChannelStatus(MU, ch) == MU_CHANNEL_FREE) 
                { 
                    HSE_MU_SendRequest(MU, ch, &my_service_request);             
                    while(HSE_MU_IsAckPending(MU, ch)); 
                } 
            // at this point the service is running in the HSE
            // the response is handled in the interrupt handler
            .../... 
            // interrupt handler on MU 0 transmit 
            hse_interrupt_handler_mu0_tr() 
            { 
                .../...
                // search for a service channel with a pending response
                for(ch = 0; ch < NB_CHANNELS;ch++) 
                { 
                    if(HSE_MU_IsResponseReady(0, ch)) 
                    { 
                        // retrieve the service response and exit
                        response = HSE_MU_ReceiveResponse(0, ch); 
                        break;
                    } 
                } 
                .../... 
             } 
        
2.6  External system interfaces
2.6.1  Reset (start-up flow)
2.6.1.1  Reset-release flow (CPU subsystems)
The CPU subsystems (masters) within the device are released from reset in a certain order and under certain
conditions and configuration.
The CPU subsystem in the HSE is the only master unconditionally released from reset after power on.
Select CPU subsystems within the host are released from reset by the HSE depending on the configuration that
has been defined prior to startup, as described in the below table. The CPU subsystems not released by the
HSE can be released by other CPU subsystems (defined by the application).
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
30 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 31

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Configuration
Identification of the CPU subsystem(s)
to release from reset
Release conditions
BOOT_SEQ == 0
BOOT_TARGET (in IVT)
Unconditional
BOOT_SEQ == 1
Core Reset table (in SYS-IMG)
Defined in the Secure Memory Region (SMR) tables
Table 13. CPU subsystems released from reset by the HSE
Based on the above, one of the "secure boot" process on one or more application images can be established
when BOOT_SEQ equals 1. This secure boot process must be handled through the memory verification
services that manage secure memory regions (SMR). For more information on the memory verification services,
SMR, and Core Reset tables, refer to the chapter Secure Boot and Memory Verification Services.
It is also possible to limit the secure boot process to the sole authenticity check of AppBL using ADKP. This is
only possible when no CR entries are defined through advanced secure boot configuration services.
Note:
If there is no SYS-IMG when BOOT_SEQ =0, the key catalog format is permitted (the host gains CUST and
OEM rights). In this way, the host can reconfigure the device.
If BOOT_SEQ =0 in IVT, the HSE FW does not reset the SOC if the SYS-IMG is corrupted (or does not exist).
2.6.1.2  Start-up flow
At start-up, the HSE subsystem runs either a normal boot or an installation boot. The selection between the two
boot processes depends on:
• The presence of IVT
• The presence of FW-IMG
• The need for FW-IMG install
If IVT_AUTH is set to 1, IVT must be authenticated before being used. The authentication tag over IVT is
calculated by the HSE on demand from the host via one specific administration service.
If the Crystal Oscillator enablement flag is switched on, the HSE subsystem starts the oscillator. The flag
location is defined in UTEST. Details can be found in the S32K3xx Reference Manual.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
31 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 32

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Power -On Reset (POR)
Search for a valid IVT header  
tag in application NVM
IVT found?
IVT_AUTH == 1?
Verify IVT authenticity
IVT authentic?
yes
no
yes
FW- IMG available
in secure NVM?
yes
FW-IMG
Installation required?
yes
no
no
Normal boot
(see separately)
Installation boot
(see separately)
yes
no
no
reset_cnt= 0
Functional Reset
Standby Exit
no
yes
?
Enable Crystal Oscillator
no
yes
Standby boot
(see separately)
Enable Crystal Oscillator
Figure 8. Start-up flow
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
32 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 33

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
In the installation boot, the HSE reads the encrypted and authenticated FW-IMG from the application NVM,
decrypts it, and stores the result in protected system RAM. Once the authenticity of the decrypted image is
verified, the HSE programs to its code Flash area and deletes the plain image from the protected system RAM.
The source address for FW-IMG is either provided by IVT, or by placing the FW-IMG at the first IVT location
IVT_START, refer chapter Device Specific Parameters (S32K3xx).
Installation boot
FW_IMG provided by
IVT
Valid IVT present?
FW_IMG default  
IVT_FIRST
Upload and decrypt FW - IMG  
from FW_IMG in chunks  
into HSE RAM
Verify FW - IMG authenticity
FW - IMG authentic?
no
yes
Program FW - IMG in
secure NVM
Normal boot
(see separately)
no
yes
Figure 9. Installation boot flow
In the normal boot flow, the IVT is loaded and parsed by the HSE subsystem to:
• HSE never enables the XRDC, and it configures only some of the MRGD to gain the access of its secure
area.
• Finally run the HSE firmware if present in secure NVM; otherwise goes in wait-for-interrupt mode (WFI).
The BOOT_SEQ and BOOT_TARGET parameters control the reset-release of the CPU subsystem to execute
the Apps. Before releasing the host, the application watchdog (watchdog instance 0, that is, SWT_0) is also
enabled, if SWT is set to 1.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
33 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 34

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
*BOOT_TARGET defines the CPU subsystems to be released from reset
Normal Boot
XRDC configuration of HSE 
resources
IVT Available?
Jump to Recovery Mode
NO
IVT_AUTH == 1?
YES
NO
BOOT_SEQ == 1?
YES
FW-IMG available in
secure NVM?
YES
BOOT_TARGET == 0?
NO
YES
Release BOOT_TARGET*
from reset to run Apps
SWT == 1?
NO
Enable application 
watchdog (SWT_0)
NO
NO
YES
Jump to FW--IMG in
secure NVM
FW-IMG available in
secure NVM?
YES
YES
Disable HSE watchdog
NO
SBAF authenticates the 
IVT using AES-GMAC 
operation?
NO
YES
(No target defined)
Wait for interrupts 
(WFI)
Figure 10. HSE normal boot flow
2.6.1.3  Recovery Mode
The recovery mode allows the host to recover from the following abnormal situations:
1. IVT is not present or corrupted.
2. There are more than 8 consecutive functional or destructive resets.
3. Secure boot authentication of application image failed.
This feature enables debugging of application failures therefore avoiding device “bricking”. Once the problem
is fixed, the host application must clear the functional reset counter and the destructive reset counter in register
“DCMRWP1”.
There are two methods of recovery modes – Secure Recovery Mode and JTAG Based Recovery Mode.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
34 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 35

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Refer to “Boot Chapter” in the S32K3xx Reference Manual or see the Device Specific Parameters (S32K3xx)
chapter in this document for more details.
2.6.1.3.1  Secure Recovery Mode
In Secure Recovery mode, the HSE subsystem boots the Secure Recovery Application after its authenticity vs.
ADKP is confirmed (see the below figure).
This Secure Recovery mode needs to be enabled by HSE_SECURE_RECOVERY_CONFIG_ATTR_ID. The
start address and the size of the secure recovery application must be provided in the IVT and Secure Recovery
Application includes random IV.
The application core is ungated at the start address of the Secure Recovery Application.
Setting the HSE_SECURE_RECOVERY_CONFIG_ATTR_ID multiple times is allowed. The UTEST
programming is done only the first time and skipped for subsequent calls. Reading it will return invalid
parameters status response, although this attribute has been configured successfully according to the UTEST
flag value.
If the Secure Recovery Mode fails, the device enters JTAG Based Recovery Mode. After enablement of Secure
Recovery Mode via HSE_SECURE_RECOVERY_CONFIG_ATTR_ID, it can be disabled again by setting a bit
in BCW.
Note:  The Boot data sign service cannot be used for GMAC of Secure Recovery App.
ADKP  
AES - 256 - GMAC  
Verification
Secure Recovery  
Application
Random IV (12  
Bytes)
GMAC (128 bit)
SHA - 256
Key
Length of 
Secure 
Recovery 
Application
Figure 11. Secure Recovery Mode
2.6.1.3.2  JTAG Based Recovery Mode
In JTAG Based Recovery mode, the HSE subsystem waits for debugger connection (that must be authenticated
when LC is OEM_PROD or IN_FIELD) and then releases the host from reset at a predefined address
JTAG_RECOVERY_START_ADDRESS to a RAM application with application core in sleeping mode. For
details on predefined address, refer section Recovery Mode Start Address.
If the Recovery Counter > 16 then HSE firmware always issues a reset. The HSE is kept in reset to prevent the
battery from draining. For details on Recovery Counter, refer S32K3xx Reference Manual.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
35 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 36

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Recovery mode
recovery_cnt  
below 16 ?
Wait for debugger connection
LC == CUST_DEL?
Wait for successful debugger  
connection
Functional reset
no
yes
time-out (30 sec )
Recovery  
successful
Release the host from reset at  
debug reset address*
* The CPU subsystem released from reset and the reset address
are fixed by design and device specific.  
-
connection
successful
no
yes
recovery_cnt  
above 8 ?
yes
no
Figure 12. JTAG Based Recovery Mode
2.6.1.3.3  Disable entry into reset recovery mode
The entry into recovery mode because of consecutive functional or destructive resets can be disabled by
setting bit number 22 and 23 in register “DCMRWP1”. This must be done on every power on reset as bits in this
register are cleared only on POR.
If the device contains Secure-BAF 0.15.0 or above, then an additional bit in the BCW is used to determine entry
into the recovery mode sequence, in addition to the ones in DCMRWP1. See this section Start-up Parameters in
IVT for more details.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
36 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 37

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Following table describes the behavior of entry into recovery mode based on the value of bits at these two
places:
DCMRWP1 (SBAF_REC_DIS_FRST
or SBAF_REC_DIS_DRST)
BCW (RESET_RECOVERY_MODE)
Entry into recovery mode
0
0
No
0
1
Yes
1
0
No
1
1
No
Table 14. Entry into recovery mode behavior
Note:
This does not disable entry into recovery mode if consecutive functional resets have occurred via application of
sanctions during secure boot. See details on Sanctions.
2.6.1.3.4  Authenticity checks during start-up
The below table summarizes the authenticity checks performed on certain images depending upon the start-up
conditions.
Image
Verification trigger
Conditions
Authentication scheme
IVT
Normal boot, all HSE variants
IVT_AUTH == 1
GMAC using ADKP extension
AppBL
Normal boot
BOOT_SEQ == 1 and no
SMR defined
GMAC using ADKP extension
FW-IMG
Installation boot and Normal boot
Installation detection or
update service execution
Undisclosed
Table 15. Authenticity checks during start-up
The IVT and AppBL authenticity checks are performed by the HSE using the GMAC authentication tags
provided at the end of each of those images. See IVT Structure for image structure details.
Those GMAC authentication tags can be calculated by the HSE when requested by the host through the
administration service specified in section Authenticate the Host System Images. They can also be calculated
off-chip in any system having the knowledge of the ADKP. The GMAC algorithm is described in section Mac
Generation and Verification. The input message M is the IVT and AppBL content without the 16-byte GMAC
value: for example, when authenticating the IVT, the message M has a size of exactly 240 bytes. The key is
the ADKP extension that is derived by applying a hash primitive over ADKP as described in Secure Boot and
Memory Verification Services.
Note:  The 12 bytes located in the IVT before the GMAC must be used as an Initial Vector (IV) in the GMAC
calculation: It should be a randomly chosen value that must change every time a new GMAC is calculated over
an updated IVT and/or AppBL.
2.6.1.4  Debug
2.6.1.4.1  HSE subsystem debug
The debugging of the HSE subsystem and associated firmware is restricted to NXP engineering teams.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
37 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 38

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
2.6.1.4.2  Host debug
The host debug is either open or protected, depending on the LC state (see Host Debugging Capabilities vs.
LC).
The debug protection consists of closing the debugger access through the JTAG interface until the HSE
authenticates the debugger. This authentication is based on the knowledge of a 128-bit secret named ADKP,
provisioned as one of the one-time programmable HSE system attributes.
The authentication method can be:
• Static: in this case, ADKP is a password which is provided in plain form by the debugger
• Dynamic (recommended): Authentication by challenge response; in this case, ADKP is a cryptographic key
which is used by the debugger to calculate a cryptographic response to a random challenge.
The authentication method is configured by the host via the HSE system attribute AUTH_METHOD. Since the
dynamic authentication method does not expose any secrets in plaintext form, it should be the preferred method
to reach a higher level of security on the debug protection.
The debugger runs the authentication process through the JTAG interface via two registers:
• JIN is a 256-bit input data register (debugger ➔ device)
• JOUT is a 256-bit output data register (device ➔ debugger)
The static debugger authentication works as follows:
• The debugger transmits the (user provided) 128-bit password to the lowest significant bits of JIN (bits 0 to
127); the remaining bits (bit 128 to 255) are transmitted as zeroes (padding)
• If JIN matches the value stored in ADKP, the debug connection is opened
• Otherwise, the debug connection remains closed
The dynamic debugger authentication works as follows:
• The debugger reads-out the 256-bit challenge from JOUT
• The debugger calculates the cryptographic response, which is an AES ECB encryption over the 256-bit
challenge using the debug key available at the debugger side; note that it is recommended that this key is
stored and used in a secure environment (secure USB token, Hardware Security Module, smart card, and so
on)
• The debugger transmits the 256-bit cryptographic response to JIN
• If JIN matches the response calculated internally and in parallel by the HSE, the debug connection is opened
• Otherwise, the debug connection remains closed
When the debugger authentication fails, the debugger must reset the device before trying to connect again and
authenticate itself.
Note that a possible repurposing of the JTAG pins for functional purposes during boot can influence the
challenge and response operation, and thus influence field quality analysis activities. Users are therefore asked
to include this factor in their development.
For more details on the JTAG interface, refer to S32K3xx Reference Manual.
To enable the debug authorization in OEM_PROD or IN_FIELD life cycle, the steps below must be followed:
1. Provision the ADKP using the HSE_APP_DEBUG_KEY_ATTR_ID attribute.
It can be provisioned:
• in plaintext
• in plaintext diversified with the device’s UID; refer to Provisioning a device-dependent ADKP.
• or from an existing key slot that was previously previsioned in a secure way (the key was imported in an
encrypted format); refer to Secure ADKP Provisioning.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
38 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 39

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
2. Set authorization method: password-based or challenge-response based, using the
HSE_DEBUG_AUTH_MODE_ATTR_ID system attribute.
3. Set the life cycle to OEM_PROD or IN_FIELD using the HSE_SECURE_LIFECYCLE_ATTR_ID system
attribute.
For more details about the attributes refer to section Manage HSE System Attributes.
Note:
RNG initialization is a basic requirement for debug authorization. If RNG or PKC initialization fails, its not
advisable to perform debug authorization. It is treated as critical error and the initialization flow will be exited as
a major issue.
RNG initialization done for debug authorization reasons is impacting HSE boot time, as this is done before HSE
sets HSE_STATUS_INIT_OK. Currently, debug authorization is done for every boot, this will be subject of future
improvements.
2.6.1.4.3  Provisioning a device-dependent ADKP
When ADKP is provisioned, it can be optionally diversified with the device’s UID before being written in secure
NVM. This allows to provision a device-dependent debug key (or password) and to use ADKP as a master
debug key: the device-dependent key can be calculated based on the UID and the knowledge of the master key
which is never shared.
Important:  Although the ADKP diversification using the device’s UID is optional, it is strongly recommended to
use it and enforce that each device gets a unique debug key or password.
To configure the device-dependent ADKP, the following steps must be followed:
1. The ADKP diversification is selected via service HSE_SRV_ID_SET_ATTR, using the attribute
HSE_EXTEND_CUST_SECURITY_POLICY_ATTR_ID (refer to enableADKm option that sets the
ADKP_MASTER in UTEST) before programming the ADKP.
2. The host application programs the master ADKP via service HSE_SRV_ID_SET_ATTR, using the attribute
HSE_APP_DEBUG_KEY_ATTR_ID.
3. The firmware internally derives the actual ADKP from the master ADKP and the Unique Identifier (UID) of
the device as shown in the figure below.
(first 16 bytes encrypted and saved in secure NVM)
Key
Key (256 bit)
ADKP
Input to the "set attribute" services
AES-ECB
SHA256
SHA256
UID
64 bit
Input
(ADKPm 128 bit)
Figure 13. Provisioning a device-dependent password / debug key
For this diversification process to take place, the value of ADKP_MASTER must be set before provisioning
ADKP.
Important:
If the host debug is allowed (that is, not permanently disabled), ADKP_MASTER and ADKP must be
provisioned before LC is transitioning to the state OEM_PROD or IN_FIELD.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
39 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 40

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
2.6.1.4.4  Secure ADKP Provisioning
The ADKP can be provisioned by securely importing the key (via import key service) in secure key catalog and
then use the value to initialize ADKP.
The following steps must be followed to provision the ADKP in a secure manner:
1. Import an AES-128 key in an encrypted format in a RAM key slot.
2. Call the Set Attribute service using the hseAttrSecureApplDebugKey_t attribute. Use the parameter
pAttr to provide a pointer to the 32-bit ‘keyHandle’ to the previously imported key (instead of using pAttr as a
pointer to the 16-byte plain ADKP).
3. The HSE copies the AES-128 RAM key to the UTEST memory.
4. Verify if the ADKP was correctly programmed by calling the Get Attribute using the
hseAttrSecureApplDebugKey_t attribute. HSE returns the first 16 bytes of SHA2_224 over (ADKP).
For more information, refer to hseAttrSecureApplDebugKey_t in HSE System Attributes.
The following flowchart explains the logic of HSE firmware when the SET ATTRIBUTE command is given to
program the ADKP.
Figure 14. Logic in HSE Firmware for programming the ADKP
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
40 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 41

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3   HSE Firmware Installation
3.1  Scope
This chapter covers HSE Firmware Installation via Secure-BAF.
Note:
The illustrations shown in this chapter are for the S32K3x4 device family, but the concept remains generic and is
applicable for other devices.
3.2  Installation process in FULL_MEM configuration
The installation process consists in bringing the host and HSE images from an external programming entity (a
PC, a tester, and so on), connected via the JTAG interface, to the device’s application and secure NVM.
Before HSE firmware can be installed in the device, the application software must enable the security in the
device by programming the “HSE Firmware usage feature flag” in the UTEST area. Please refer to the Device
Configuration section.
HSE Firmware can be installed via 3 methods:
1. Installation via IVT.
2. By programming encrypted FW-IMG at default location IVT_START.
3. By programming encrypted FW-IMG and using the MU interface.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
41 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 42

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.2.1  Installation via IVT
The below section explains the installation of HSE Firmware via programming IVT and encrypted FW-IMG.
ECU / test board
S32K3xx (host)
HSE
Programming entity
JTAG
IVT
FW-IMG
(encrypted)
Apps
secure RAM
secure NVM
application RAM
application NVM
IVT
FW-IMG
(encrypted)
application NVM (OTP)
system attributes (default)
secure NVM (OTP)
HSE system attributes (default)
Apps
Figure 15. Simplified system view before installation
All images are first copied to the internal application NVM (internal Flash) via the JTAG interface. The IVT must
be written at a specific address that can be selected among one of the possible addresses referenced in the
section Device Specific Parameters (S32K3xx). The start addresses of all the other images must match the
values that are provided within the IVT.
At reset, when the HSE firmware is not available in the secure NVM, the HSE runs the installation boot process
that:
• Decrypts FW-IMG into the internal memory
• Verifies the authenticity of FW-IMG
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
42 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 43

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• Programs FW-IMG in plain in secure NVM
• If FW-IMG is for AB_Swap enabled configuration then enable the AB_Swap feature on the device and
program the plaintext image in secure NVM
Once this installation boot is successfully executed, FW-IMG can be removed from the application NVM, and
potentially replaced by application code or data.
ECU / test board
S32K3xx (host)
HSE
secure RAM
secure NVM
application RAM
application NVM
IVT
FW-IMG
(encrypted)
application NVM (OTP)
system attributes (default)
secure NVM (OTP)
HSE system attributes (default)
Apps
FW-IMG
(plain)
Figure 16. Simplified system view after installation
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
43 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 44

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.2.2  Installation via default Application NVM location
In this Firmware installation method, Encrypted FW-IMG is programmed at default location IVT_START and no
IVT is programmed in the device. The process of HSE Firmware installation is similar as installation via IVT. For
IVT_START, refer to the chapter Device Specific Parameters (S32K3xx).
Figure 17. Simplified system view before installation
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
44 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 45

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
ECU / test board
S32K3xx (host)
HSE
secure RAM
secure NVM
application RAM
application NVM
FW- IMG
(encrypted)
application NVM (OTP)
system attributes (configured)
secure NVM (OTP)
HSE sys attributes (configured)
FW- IMG
(plain)
Figure 18. Simplified system view after installation
3.2.3  Installation via MU interface
This method provides flexibility to install HSE firmware by placing encrypted FW-IMG at system RAM. HSE
firmware can be installed via programming encrypted FW-IMG in code flash or in System RAM memory and the
start address of encrypted FW-IMG must be provided via MU channel 0 interface by application.
To enable installation via MU interface, the Host application must write bits 24th - 31st of DCM Register
(DCMRWP1 0x402AC400) with value 0xA5.
Note:  If the bit FW_USAGE_FLAG_PROGRAM (see BCW Bit Mapping) is set, then writing 0xA5 in DCMRWP1
is not required.
On the next functional reset, Secure BAF enables HSE Firmware installation via MU0 instance and sets
HSE_CONFIG_GPR3 (0x4039C028) bit 1 to indicate the installation state machine is executing. Secure BAF
transmits response over MU channel 0 to confirm installation of HSE Firmware. The Host application then
transmits the expected response within the timeout period. This sequence is mentioned in the next flowchart.
Below figures explains installation of HSE Firmware via programming encrypted FW-IMG and using MU
interface.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
45 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 46

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
ECU / test board
S32K3xx (host)
HSE
Programming entity
JTAG
FW- IMG
(encrypted)
secure RAM
secure NVM
application RAM
application NVM
FW- IMG
(encrypted)
application NVM (OTP)
system attributes (default)
secure NVM (OTP)
HSE system attributes (default)
Figure 19. Simplified system view before installation
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
46 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 47

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
ECU / test board
S32K3xx (host)
HSE
secure RAM
secure NVM
application RAM
application NVM
FW- IMG
(encrypted)
application NVM (OTP)
system attributes (configured)
secure NVM (OTP)
HSE sys attributes (configured)
FW- IMG
(plain)
Figure 20. Simplified system view after installation
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
47 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 48

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
HSE Firmware Installation    
from MU
FW_USAGE_FLAG_PROGRAM
is set?
No
DCMRWP1    
No
Yes
bits 24 - 31 == 0xA5 ?
Secure BAF transmits 0xFF00F00F    
over MU0.MUA to indicate HSE FW    
installation required
Set HSE_CONFIG_GPR3 bit 1
Response received on MU* ?
Response == 0xF0F00F0F ?
80 Sec timeout?
Yes
No
Secure BAF transmits 0xDADABABA    
over MU0.MUA to get address of    
Encrypted HSE Firmware
Yes
Response received on MU ?
Secure BAF Installs HSE Firmware
Installation Success ?
Secure BAF transmits 0xDACACADA    
over MU to indicate installation    
Success
Clear
 HSE_CONFIG_GPR3
bit 1
Shutdown    
Secure BAF
*App core transmits response over MU Channel 0 (MU0.MUB)
60 Sec timeout?
Yes
Yes
Yes
Yes
No
No
No
No
No
Yes
Figure 21. MU Interface installation flow for SBAF in FULL_MEM configuration
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
48 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 49

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.2.3.1  MU Installation steps by host in FULL_MEM configuration
The steps below can be followed for using the MU Interface to install HSE Firmware when device is in
FULL_MEM configuration.
1. Write 0xA5 on register DCMRWP1 (0x402AC400, [24:31 bits]) followed by functional reset. This will
set Bit 1 in HSE_CONFIG_GPR3 (0x4039C028) indicating SBAF has activated MU0 for installation.
2. If SBAF sends '0xFF00F00F' response on MU Rx register (0x4038c280), it means new HSE
firmware installation is required.
3. App Core to respond by writing value ‘0xF0F00F0F’ on MU Tx register (0x4038c200) to confirm
installation within 80 seconds.
4. SBAF sends ‘0xDADABABA’ on MU Rx register (0x4038c280).
5. App core responds by writing Pink Image Location on MU Tx register (0x4038c200) within 60
seconds.
6. If SBAF sends '0xDACACADA' response on MU Rx register (0x4038c280) to indicate success.
7. App Core to issue a functional reset.
8. App core must wait for Bit 0 in GPR to set (that means SBAF has completed and booted new HSE
Firmware). If the bit is NOT SET even after approximately 1 second, either you can retry again from
beginning or contact NXP.
3.2.4  Flash Memory Layout (FULL_MEM) during Firmware Installation
The figure below illustrates the Flash memory layout during HSE Firmware installation in FULL_MEM
configuration. The SBAF and HSE FW are always present in the top section of memory for all variants. Refer to
the chapter HSE Firmware Update for more details.
Device delivered by NXP 
(FULL MEM configuration)
Program IVT and NXP 
delivered HSE firmware 
image in application NVM 
an issue reset
IVT
HSE Firmware Image 
(FULL MEM 
configuration, 
encrypted image)
SECURE BAF 
(48Kb)
HSE Code 
Flash
HSE Firmware Plaintext 
(128Kb)
HSE Firmware decrypts 
authenticates and programs 
HSE firmware in plaintext to 
HSE code flash
SECURE BAF
HSE Code 
Flash
SECURE BAF
HSE Code 
Flash
0x00400000
0x007FFFFF
0x007F4000
0x00400000
0x007FFFFF
0x007F4000
0x00400000
0x007F4000
0x007FFFFF
0x007D4000
0x007D4000
0x007D4000
HSE Firmware Image 
(FULL MEM 
configuration, 
encrypted image)
IVT
Application 
NVM
Application 
NVM
Application 
NVM
Figure 22. Flash memory layout during HSE firmware installation (FULL_MEM)
The above figure illustrates for S32K344 and the same will be applicable for other S32K3XX Variants. For
details of FLASH MEMORY LAYOUT for all other variants, refer to the Flash Memory Layout section.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
49 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 50

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.3  Installation process in AB_SWAP configuration
If the device is in AB_SWAP configuration, the firmware needs to be installed if it gets erased by SBAF due to
some issue in the firmware as explained in the section HSE Firmware Handshake. The only way through which
HSE Firmware can be installed is - “Installation via MU interface”.
If HSE firmware is not present in the passive block then, HSE Firmware can be installed via the MU interface in
passive block. And if HSE firmware is already present in passive block or if it is installed via MU interface then
the active – passive block switching is allowed via MU interface.
To enable installation via MU interface, Host application must write bits 24th -31st of DCM Register (DCMRWP1
0x402AC400) with value 0xA5.
Note:  If the bit FW_USAGE_FLAG_PROGRAM (see BCW Bit Mapping) is set, then writing 0xA5 in DCMRWP1
is not required.
On next functional reset, Secure BAF enables HSE Firmware installation/active-passive block switching via
MU interface and sets HSE_CONFIG_GPR3 (0x4039C028) bit 1 to indicate installation state machine is
executing. Secure BAF transmits response over MU channel 0 to confirm installation of HSE Firmware then
Host application transmits expected response within the timeout period. This sequence is mentioned in below
flowchart.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
50 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 51

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
HSE Firmware Installation  
from MU
No
DCMRWP1  
Yes
bits 24 - 31 == 0xA5 ?
Yes
FW_USAGE_FLAG_PROGRAM
is set?
Set HSE_CONFIG_GPR3 bit 1
in Passive Block ?
Valid HSE Firmware present  
Yes
No
Secure BAF transmits 0xFF00F00F  
over MU0.MUA to indicate HSE FW  
installation required
Secure BAF transmits 0xAA55A55A  
over MU0.MUA to confirm HSE FW  
installation Passive block switching
Response received on MU* ?
Response received on MU* ?
Response == 0xF0F00F0F ?
Yes
HSE Firmware already
installed via Handshake state  
machine
Yes
No
Secure BAF transmits 0xDADABABA
over MU0.MUA to get address of  
Encrypted HSE Firmware
Response received on MU ?
Secure BAF Installs HSE Firmware
Installation Success ?
80 Sec timeout?
No
Clear
HSE_CONFIG_GPR3
bit 1
Shutdown  
Secure BAF
No
60 Sec timeout?
No
No
Yes
Yes
No
Yes
80 Sec timeout?
No
No
No
No
Response == 0x5A5AA5A5 ?
No
Yes
No
Secure BAF Switches Active and  
Passive Code Flash Blocks
Yes
Switching success?
Yes
Secure BAF transmits 0xDABABADA  
over MU to indicate switching Success
No
Yes
Yes
Figure 23. MU Interface installation flow for SBAF in AB_SWAP configuration
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
51 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 52

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.3.1  MU Installation steps by host in AB_SWAP configuration
The steps below can be followed for using the MU Interface to install/recover HSE Firmware when device is in
AB_SWAP configuration.
1. Write 0xA5 on register DCMRWP1 (0x402AC400, [24:31 bits]) followed by functional reset. This will
set Bit 1 in HSE_CONFIG_GPR3 (0x4039C028) indicating SBAF has activated MU0 for installation.
2. If SBAF sends '0xFF00F00F' response on MU Rx register (0x4038c280) (that means new HSE
firmware installation is required) then go to Step 3 else skip to Step 6.
3. App Core to respond by writing value ‘0xF0F00F0F’ on MU Tx register (0x4038c200) to confirm
installation within 80 seconds.
4. SBAF sends ‘0xDADABABA’ on MU Rx register (0x4038c280).
5. App core responds by writing Pink Image Location on MU Tx register (0x4038c200) within 60
seconds.
6. If SBAF sends '0xAA55A55A' response on MU Rx register (0x4038c280) it means valid firmware
was present in Passive Region / Backup found.
7. App Core to choose whether to switch partitions for backup, or install a new HSE Firmware image. If
app wants to switch to backup, it responds by writing value ‘0x5A5AA5A5’ on MU Tx register
(0x4038c200) within 80 seconds. Go to next Step. Otherwise, for installation of new HSE Firmware, go to
step 3.
8. SBAF activates passive block and sends ‘0xDABABADA’ on MU Rx register (0x4038c280) to
indicate success.
9. App Core to issue a functional reset.
10. App core must wait for Bit 0 in GPR to set (that means SBAF has completed and booted new HSE
Firmware). If the bit is NOT SET even after approximately 1.5 second, either you can retry again from
beginning or contact NXP.
3.3.2  Flash Memory Layout (AB_SWAP) during Firmware Installation
The figure below illustrates the Flash memory layout during HSE Firmware installation in AB_SWAP
configuration. This memory configuration is enabled after a reset is issued on completion of the installation
procedure.
ACTIVE BLOCK
Device delivered by NXP 
(FULL MEM configuration)
Program IVT and NXP 
delivered HSE firmware 
image in application NVM 
an issue reset
IVT
HSE Firmware Image 
(AB_SWAP 
configuration, 
encrypted image)
SECURE BAF 
(48Kb)
HSE Code 
Flash
HSE Firmware Plaintext 
(176Kb)
After reset, Secure BAF 
decrypts, authenticated and 
programs HSE firmware to 
passive HSE code flash and 
enables AB_SWAP configuration
SECURE BAF
HSE Code 
Flash
SECURE BAF
HSE Code 
Flash
0x00400000
0x007FFFFF
0x007F4000
0x00400000
0x007FFFFF
0x007F4000
0x00400000
0x007F4000
0x007FFFFF
0x007D4000
0x007D4000
0x007D4000
HSE Firmware Image 
(FULL MEM 
configuration, 
encrypted image)
IVT
Application 
NVM
Application 
NVM
Application 
NVM
HSE code 
flash
Application 
NVM
0x005D4000
0x005FFFFF
SECURE BAF 
(48Kb)
HSE Code 
Flash
HSE Firmware Plaintext 
(176Kb)
After reset, device switches to 
AB_SWAP configuration
0x007F4000
0x007FFFFF
0x007D4000
IVT
Application 
NVM
HSE code 
flash
Application 
NVM
0x005D4000
0x005FFFFF
0x00600000
0x00400000
Figure 24. Flash memory layout during HSE firmware installation (AB_SWAP)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
52 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 53

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The above figure illustrates for S32K344 and the same will be applicable for other S32K3XX Variants. For
details of FLASH MEMORY LAYOUT for all other variants please refer to Flash Memory Layout section for more
details.
3.4  Potential causes of failure
Below are the potential causes for an unsuccessful HSE firmware installation.
• The relevant bits in DCMRWP1 are not set or the FW_USAGE_FLAG_PROGRAM bit is not set in BCW in IVT.
• Integrity of encrypted FW-IMG is not valid.
• During first HSE install on K312 devices, there must be reduced speed mode configured in UTEST. After HSE
is installed, it can be cleared.
3.5  Flash memory layout
The following memory configurations are possible:
• FULL_MEM: In this configuration, the entire Flash memory is seen as one continuous memory partition.
• AB_SWAP: In this configuration, the Flash memory splits into two partitions of equal size, referenced as
partition A and partition B.
• PARTIAL AB_SWAP: This configuration is similar to the AB_SWAP configuration with the difference that
swapping of blocks happens only between BLOCK 1 and BLOCK 3 while BLOCK 0 and BLOCK 2 are fixed.
This mode is supported only for S32K328, S32K338, S32K348, S32K358, S32K356, S32K336, and S32K388
devices. For more information, refer to the chapter HSE Firmware Update.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
53 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 54

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.1  Flash Memory Layout for S32K311, S32M276, MWCT2015S devices
3.5.1.1  Illustrations of Flash memory layout in FULL_MEM
0x00400000
0x0047FFFF
Code 
Flash 
Block 
(512 KB)
BLOCK 0
0x10000000
0x1003FFFF
64 KB
0x10010000
Data 
Flash 
Block
(256 KB)
BLOCK 2
192 KB
0x00480000
0x004FFFFF
0x004D4000
Code 
Flash 
Block 
(512 KB)
BLOCK 1
176 KB
Secure 
Flash
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
Figure 25. Illustrations of Flash memory layout of S32K311 in FULL_MEM
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
54 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 55

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.1.2  Illustrations of Flash memory layout in AB_SWAP
0x00400000
176KB 
Secure 
Flash
0x00480000
0x004FFFFF
0x004D4000
176KB 
Secure 
Flash
Active  
                      Partition
Passive 
Partition
0x0047FFFF
0X00454000
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
Code 
Flash 
Block 
(512 KB)
BLOCK 0
BLOCK 1
Code 
Flash 
Block 
(512 KB)
0x10000000
0x1003FFFF
64 KB
0x10010000
BLOCK 2
192 KB
Data 
Flash 
Block
(256 KB)
Figure 26. Illustrations of Flash memory layout of S32K311 in AB_SWAP
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
55 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 56

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.2  Flash Memory Layout for S32K310, MWCT2014S and S32M274 devices
3.5.2.1  Illustrations of Flash memory layout in FULL_MEM
0x00400000
0x00480000
0x004FFFFF
512 KB 
Secure 
Flash
0x0047FFFF
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
Code 
Flash 
Block 
(512 KB)
BLOCK 0
BLOCK 1
Code 
Flash 
Block 
(512 KB)
0x10000000
0x1003FFFF
64 KB
0x10010000
BLOCK 2
192 KB
Data 
Flash 
Block
(256 KB)
Figure 27. Illustrations of Flash memory layout of S32K310 in FULL_MEM
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
56 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 57

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.2.2  Illustrations of Flash memory layout in AB_SWAP
0x00400000
256 KB 
Secure 
Flash
0x00480000
0x004FFFFF
0x004C0000
256 KB 
Secure 
Flash
Active 
                      Partition
Passive 
Partition
0x0047FFFF
0x00440000
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
Code 
Flash 
Block 
(512 KB)
BLOCK 0
BLOCK 1
Code 
Flash 
Block 
(512 KB)
0x10000000
0x1003FFFF
64 KB
0x10010000
BLOCK 2
192 KB
Data 
Flash 
Block
(256 KB)
Figure 28. Illustrations of Flash memory layout of S32K310 in AB_SWAP
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
57 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 58

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.3  Flash Memory Layout for S32K312, S32K322 and S32K342 devices
3.5.3.1  Illustrations of Flash memory layout in FULL_MEM
0x00400000
0x00500000
0x005FFFFF
0x005D4000
176 KB 
Secure 
Flash
0x0047FFFF
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
Code 
Flash 
Block 
(1 MB)
BLOCK 0
BLOCK 1
Code 
Flash 
Block 
(1 MB)
0x10000000
0x1003FFFF
88 KB
0x10016000
BLOCK 2
168 KB
Data 
Flash 
Block
(256 KB)
Figure 29. Illustrations of Flash memory layout of S32K312, S32K322 and S32K342 in FULL_MEM
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
58 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 59

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.3.2  Illustrations of Flash memory layout in AB_SWAP
0x00500000
0x005FFFFF
0x005D4000
176 KB 
Secure 
Flash
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 1
Code 
Flash 
Block 
(1 MB)
0x10000000
0x1003FFFF
128 KB
0x10020000
BLOCK 2
128 KB
Data 
Flash 
Block
(256 KB)
0x00400000
0x004FFFFF
0x004D4000
176 KB 
Secure 
Flash
Code 
Flash 
Block 
(1 MB)
BLOCK 0
Active 
                      Partition
Passive 
Partition
Figure 30. Illustrations of Flash memory layout of S32K312, S32K322 and S32K342 in AB_SWAP
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
59 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 60

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.4  Flash Memory Layout for S32K341 device
3.5.4.1  Illustrations of Flash memory layout in FULL_MEM
0x00500000
0x005FFFFF
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 1
Code 
Flash 
Block 
(1 MB)
0x10000000
0x1003FFFF
88 KB
0x10016000
BLOCK 2
168 KB
Data 
Flash 
Block
(256 KB)
0x00400000
0x004FFFFF
Code 
Flash 
Block 
(1 MB)
BLOCK 0
Figure 31. Illustrations of Flash memory layout of S32K341 in FULL_MEM
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
60 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 61

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.4.2  Illustrations of Flash memory layout in AB_SWAP
0x00500000
0x005FFFFF
0x00580000
512 KB 
Secure 
Flash
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 1
Code 
Flash 
Block 
(1 MB)
0x10000000
0x1003FFFF
128 KB
0x10020000
BLOCK 2
128 KB
Data 
Flash 
Block
(256 KB)
0x00400000
0x004FFFFF
0x00480000
512 KB 
Secure 
Flash
Code 
Flash 
Block 
(1 MB)
BLOCK 0
Active 
                      Partition
Passive 
Partition
Figure 32. Illustrations of Flash memory layout of S32K341 in AB_SWAP
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
61 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 62

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.5  Flash Memory Layout for S32K344, S32K314 and S32K324 devices
3.5.5.1  Illustrations of Flash memory layout in FULL_MEM
0x00600000
0x006FFFFF
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 2
Code 
Flash 
Block 
(1 MB)
0x00700000
0x007FFFFF
0x007D4000
BLOCK 3
176 KB
Secure 
Flash
Code 
Flash 
Block
(1 MB)
0x00400000
0x004FFFFF
Code 
Flash 
Block 
(1 MB)
BLOCK 0
0x00500000
0x005FFFFF
Code 
Flash 
Block 
(1 MB)
BLOCK 1
0x10000000
0x1003FFFF
0x10016000
BLOCK 4
168 KB
Data 
Flash 
Block
(256 KB)
88 KB
Figure 33. Illustrations of Flash memory layout of S32K344, S32K314 and S32K324 in FULL_MEM
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
62 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 63

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.5.2  Illustrations of Flash memory layout in AB_SWAP
0x00600000
0x006FFFFF
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 2
Code 
Flash 
Block 
(1 MB)
0x00700000
0x007FFFFF
0x007D4000
BLOCK 3
176 KB
Secure 
Flash
Code 
Flash 
Block
(1 MB)
0x00400000
0x004FFFFF
Code 
Flash 
Block 
(1 MB)
BLOCK 0
0x00500000
0x005FFFFF
Code 
Flash 
Block 
(1 MB)
BLOCK 1
0x10000000
0x1003FFFF
0x10020000
BLOCK 4
128 KB
Data 
Flash 
Block
(256 KB)
128 KB
Active 
                      Partition
Passive 
Partition
176 KB
Secure 
Flash
0x005D4000
Figure 34. Illustrations of Flash memory layout of S32K344, S32K314 and S32K324 in AB_SWAP
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
63 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 64

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.6  Flash Memory Layout for S32K396 and S32K376 devices
3.5.6.1  Illustrations of Flash memory layout in FULL_MEM
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 3
0x00400000
0x005FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 0
0x00600000
0x007FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 1
0x10000000
0x10040000
0x10016000
168 KB
Data 
Flash 
Block
(256 KB)
88 KB
Fixed Block
0x00800000
0x009FFFFF
0x009D4000
176 KB
Secure 
Flash
Code 
Flash 
Block
(2 MB)
BLOCK 2
Figure 35. Illustrations of Flash memory layout of S32K396 and S32K376 in FULL_MEM
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
64 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 65

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.6.2  Illustrations of Flash memory layout in AB_SWAP
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 2
0x00800000
0x009FFFFF
0x009D4000
176 KB
Secure 
Flash
Code 
Flash 
Block
(2 MB)
0x00400000
0x005FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 0
0x00600000
0x007FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 1
Active 
                      Partition
Passive 
Partition
176 KB
Secure 
Flash
0x007D4000
0x10000000
0x1003FFFF
128 KB
0x10020000
128 KB
Data 
Flash 
Block
(256 KB)
Figure 36. Illustrations of Flash memory layout of S32K396 and S32K376 in AB_SWAP
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
65 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 66

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.7  Flash Memory Layout for S32K394 and S32K374 device
3.5.7.1  Illustrations of Flash memory layout in FULL_MEM
0x00800000
0x009FFFFF
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 2
Code 
Flash 
Block 
(2 MB)
0x00400000
0x005FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 0
0x00600000
0x007FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 1
0x10000000
0x1003FFFF
0x10016000
BLOCK 4
168 KB
Data 
Flash 
Block
(256 KB)
88 KB
Figure 37. Illustrations of Flash memory layout of S32K394 and S32K374 in FULL_MEM
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
66 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 67

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.7.2  Illustrations of Flash memory layout in AB_SWAP
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
0x00400000
0x005FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 0
0x00600000
0x007FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 1
0x1003FFFF
0x10020000
BLOCK 3
128 KB
Data 
Flash 
Block
(256 KB)
128 KB
Active 
                      Partition
Passive 
Partition
1 MB
Secure 
Flash
0x00700000
0x00800000
0x009FFFFF
BLOCK 2
1 MB
Secure 
Flash
0x00900000
Code 
Flash 
Block 
(2 MB)
0x10000000
Figure 38. Illustrations of Flash memory layout of S32K394 and S32K374 in AB_SWAP
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
67 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 68

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.8  Flash Memory Layout for S32K328, S32K338, S32K348 and S32K358 devices
3.5.8.1  Illustrations of Flash Memory Layout in FULL_MEM
0x00800000
0x009FFFFF
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 2
Code 
Flash 
Block 
(2 MB)
0x00400000
0x005FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 0
0x00600000
0x007FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 1
0x10000000
0x1003FFFF
0x10016000
BLOCK 4
168 KB
Data 
Flash 
Block
(256 KB)
88 KB
0x00A00000
0x00BFFFFF
0x00BD4000
176 KB
Secure 
Flash
BLOCK 3
Code 
Flash 
Block 
(2 MB)
Figure 39. Illustrations of Flash memory layout of S32K328, S32K338, S32K348 and S32K358 in FULL_MEM
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
68 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 69

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.8.2  Illustrations of Flash Memory Layout in AB_SWAP
0x00800000
0x009FFFFF
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 2
Code 
Flash 
Block 
(2 MB)
0x00A00000
0x00BFFFFF
0x00BD4000
BLOCK 3
176 KB
Secure 
Flash
Code 
Flash 
Block
(2 MB)
0x00400000
0x005FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 0
0x00600000
0x007FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 1
0x10000000
0x1003FFFF
0x10020000
BLOCK 4
128 KB
Data 
Flash 
Block
(256 KB)
128 KB
Active 
                      Partition
Passive 
Partition
176 KB
Secure 
Flash
0x007D4000
Figure 40. Illustrations of Flash memory layout of S32K328, S32K338, S32K348 and S32K358 in AB_SWAP
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
69 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 70

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.8.3  Illustrations of Flash Memory Layout in Partial AB_SWAP
0x00800000
0x009FFFFF
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 2
Code 
Flash 
Block 
(2 MB)
0x00A00000
0x00BFFFFF
0x00B00000
BLOCK 3
1 MB
Secure 
Flash
Code 
Flash 
Block
(2 MB)
0x00400000
0x005FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 0
0x00600000
0x007FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 1
0x10000000
0x1003FFFF
0x10020000
BLOCK 4
128 KB
Data 
Flash 
Block
(256 KB)
128 KB
Active 
                      Partition
Passive 
Partition
1 MB
Secure 
Flash
0x0700000
Fixed Block
Fixed Block
Figure 41. Illustrations of Flash memory layout of S32K328, S32K338, S32K348 and S32K358 in Partial AB_SWAP
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
70 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 71

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.9  Flash Memory Layout for S32K336 and S32K356 devices
3.5.9.1  Illustrations of Flash Memory Layout in FULL_MEM
0x00800000
0x009FFFFF
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 2
Code 
Flash 
Block 
(2 MB)
BLOCK 3
0x00400000
0x005FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 0
0x00600000
0x007FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 1
0x00A00000
0x00BFFFFF
Code 
Flash 
Block
(2 MB)
BLOCK 4
0x10000000
0x1003FFFF
0x10016000
168 KB
Data 
Flash 
Block
(256 KB)
88 KB
Figure 42. Illustrations of Flash memory layout of S32K336 and S32K356 in FULL_MEM
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
71 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 72

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.9.2  Illustrations of Flash memory layout in AB_SWAP
0x00800000
0x009FFFFF
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 2
Code 
Flash 
Block 
(2 MB)
0x00A00000
0x00BFFFFF
0x00B00000
BLOCK 3
1 MB
Secure 
Flash
Code 
Flash 
Block
(2 MB)
0x00400000
0x005FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 0
0x00600000
0x007FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 1
0x10000000
0x1003FFFF
0x10020000
BLOCK 4
128 KB
Data 
Flash 
Block
(256 KB)
128 KB
Active 
                      Partition
Passive 
Partition
1 MB
Secure 
Flash
0x0700000
Figure 43. Illustrations of Flash memory layout of S32K336 and S32K356 in AB_SWAP
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
72 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 73

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.9.3  Illustrations of Flash Memory Layout in Partial AB_SWAP
0x00800000
0x009FFFFF
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 2
Code 
Flash 
Block 
(2 MB)
0x00A00000
0x00BFFFFF
0x00B00000
BLOCK 3
1 MB
Secure 
Flash
Code 
Flash 
Block
(2 MB)
0x00400000
0x005FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 0
0x00600000
0x007FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 1
0x10000000
0x1003FFFF
0x10020000
BLOCK 4
128 KB
Data 
Flash 
Block
(256 KB)
128 KB
Active 
                      Partition
Passive 
Partition
1 MB
Secure 
Flash
0x0700000
Figure 44. Illustrations of Flash memory layout of S32K336 and S32K356 in Partial AB_SWAP
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
73 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 74

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.10  Flash Memory Layout for S32K388 devices
3.5.10.1  Illustrations of Flash memory layout in FULL_MEM
0x00800000
0x009FFFFF
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 2
Code 
Flash 
Block 
(2 MB)
0x00400000
0x005FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 0
0x00600000
0x007FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 1
0x10000000
0x1003FFFF
0x10016000
BLOCK 4
168 KB
Data 
Flash 
Block
(256 KB)
88 KB
0x00A00000
0x00BFFFFF
0x00BD4000
176 KB
Secure 
Flash
BLOCK 3
Code 
Flash 
Block 
(2 MB)
Figure 45. Illustrations of Flash memory layout of S32K388 in FULL_MEM
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
74 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 75

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.10.2  Illustrations of Flash Memory Layout in AB_SWAP
0x00800000
0x009FFFFF
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
BLOCK 2
Code 
Flash 
Block 
(2 MB)
0x00400000
0x005FFFFF
Code 
Flash 
Block 
(2 MB)
BLOCK 0
0x10000000
0x1003FFFF
0x10020000
BLOCK 4
128 KB
Data 
Flash 
Block
(256 KB)
128 KB
BLOCK 3
Code 
Flash 
Block 
(2 MB)
Active 
                      Partition
0x00600000
0x007FFFFF
176 KB
Secure 
Flash
0x007D4000
BLOCK 1
Code 
Flash 
Block 
(2 MB)
Passive 
Partition
0x00A00000
0x00BFFFFF
0x00BD4000
176 KB
Secure 
Flash
Figure 46. Illustrations of Flash memory layout of S32K388 in AB_SWAP
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
75 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 76

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.11  Flash Memory Layout for S32K389 devices
3.5.11.1  Illustrations of Flash memory layout in FULL_MEM
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
0x00400000
0x004FFFFF
PFC1
BLOCK 0
0x10000000
0x1003FFFF
BLOCK 4
Data 
Flash 
Block
(256 KB)
BLOCK 3
PFC0
0x00600000
0x00500000
0x005FFFFF
PFC1
BLOCK 1
0x009FFFFF
PFC0
0x00800000
0x00A00000
0x00AFFFFF
PFC1
BLOCK 2
PFC0
0x00C00000
0x00DFFFFF
0x00B00000
0x00BFFFFF
PFC1
0x00E00000
0x00FFFFFF
0x007FFFFF
PFC0
UTEST NVM
0x1B000000
0x1B00FFFFF
8 KB
Code 
Flash 
Block 
(1MB)
Code 
Flash 
Block 
(2MB)
Code 
Flash 
Block 
(1MB)
Code 
Flash 
Block 
(2MB)
Code 
Flash 
Block 
(1MB)
Code 
Flash 
Block 
(2MB)
Code 
Flash 
Block 
(1MB)
Code 
Flash 
Block 
(2MB)
BLOCK 0
PFC0
0x00FD0000
192 KB
PFC0
Figure 47. Illustrations of Flash memory layout of S32K389 in FULL_MEM
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
76 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 77

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.11.2  Illustrations of Flash Memory Layout in AB_SWAP
Secure Area(Read/Write Restricted)
User Flash Area(Read/Write Permitted)
0x00400000
0x004FFFFF
PFC1
BLOCK 0
0x10000000
0x1003FFFF
BLOCK 4
Data 
Flash 
Block
(256 KB)
BLOCK 3
PFC0
0x00600000
0x00500000
0x005FFFFF
PFC1
BLOCK 1
0x009FFFFF
0x00800000
0x00A00000
0x00AFFFFF
PFC1
BLOCK 2
PFC0
0x00C00000
0x00DFFFFF
0x00B00000
0x00BFFFFF
PFC1
0x00E00000
0x00FFFFFF
0x007FFFFF
PFC0
UTEST NVM
0x1B000000
0x1B00FFFFF
8 KB
Code 
Flash 
Block 
(1MB)
Code 
Flash 
Block 
(2MB)
Code 
Flash 
Block 
(1MB)
Code 
Flash 
Block 
(2MB)
Code 
Flash 
Block 
(1MB)
Code 
Flash 
Block 
(2MB)
Code 
Flash 
Block 
(1MB)
Code 
Flash 
Block 
(2MB)
BLOCK 0
PFC0
0x00FD0000
Passive 
Partition
192 KB
PFC0
0x009D0000
192 KB
Active 
Partition
PFC0
Figure 48. Illustrations of Flash memory layout of S32K389 in AB_SWAP
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
77 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 78

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
4   HSE Firmware Configuration
4.1  Scope
The device and HSE firmware configuration is controlled by the host (application) either directly configuring the
UTEST area or via HSE services after a normal boot process, once the HSE firmware has been installed (see
chapter HSE Firmware Installation. This chapter explains the HSE firmware configuration which are done by
using HSE services. For other configurations, refer to the chapter Device Specific Parameters (S32K3xx).
The HSE configuration entails:
• The configuration of certain system attributes (OTP) that impact the start-up behavior of the device
• The configuration of HSE system attributes (OTP)
• The configuration of start-up parameters in IVT
• The HSE firmware configuration
• The (optional) authentication of IVT
The HSE firmware configuration comprises:
• Formatting the NVM and RAM key catalogs (see Key Catalog Formatting)
• Provisioning initial NVM keys; potentially requesting key generation (for example, RSA/ECC key pairs)
• Configuring the secure memory regions for enabling secure boot and other operations
• Configuring the Monotonic counters (Optional)
The HSE configuration must be done in LC states CUST_DEL or OEM_PROD. Once complete, LC must be
advanced to the IN_FIELD state.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
78 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 79

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
4.2  Configuration
This section describes the specific configuration parameters.
ECU / test board
S32x (host)
HSE
secure RAM
secure NVM
application RAM
application NVM
IVT
FW- IMG
(encrypted)
application NVM (OTP)
system attributes (default)
secure NVM (OTP)
HSE system attributes (default)
Apps
FW- IMG
(plain)
SYS- IMG
(plain)
Figure 49. Simplified system view before configuration
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
79 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 80

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
ECU / test board
S32x (host)
HSE
secure RAM
secure NVM
application RAM
application NVM
IVT
FW- IMG
(encrypted)
application NVM (OTP)
system attributes (configured)
secure NVM (OTP)
HSE system attributes 
(configured)
Apps
FW- IMG
(plain)
SYS- IMG
(plain)
Mac
Figure 50. Simplified system view after configuration
4.2.1  Configurable HSE system attributes
A set of programmable HSE system attributes within the secure NVM can be provisioned by the host via HSE
administration services. Some of these attributes, once set, cannot be updated.
Parameter
Size
Description
IVT_AUTH
8 bits
Selects the IVT authentication method:
• When 0 (default): no authentication check
• When 1: forces the IVT authentication check before running the HSE
firmware
AUTH_MODE
8 bits
Selects the method to open the host debug protection:
• When 0 (default): static authentication (password)
• When 1: dynamic authentication (challenge / response)
ADKP
128 bits
Value of the application debug key or password
• If AUTH_MODE equals 0, ADKP is a password
• If AUTH_MODE equals 1, ADKP is a cryptographic key
Table 16. One-time configurable HSE system attributes
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
80 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 81

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Parameter
Size
Description
ADKP_MASTER
1 bit
Selects the method to provision ADKP in secure NVM:
• When 0 (default): the input value is ADKP and is written “as is” in secure
NVM
• When 1: the input value is considered as a master debug key and is
diversified with the device’s UID before being written in secure NVM
LC
8 bits
Selects the life cycle: OEM_PROD or IN_FIELD
Table 16. One-time configurable HSE system attributes...continued
They can be read and initialized via the HSE system attribute management services. See Manage HSE System
Attributes.
4.2.2  Start-up parameters in IVT
A set of programmable parameters that influence on the start-up behavior of the HSE and the system can be
set in the BCW (Boot Configuration Word) in IVT.
Parameter
Size
Description
BOOT_SEQ
1 bit
Selects the boot sequence flow:
• When 0: releases the host from reset, then runs the HSE firmware
• When 1: keeps the host on reset and runs the HSE firmware first; must be
set to run a pre-boot verification
BOOT_TARGET
Device
dependent
Indicates which CPU subsystem (i.e. boot target) is released from reset
during the normal boot process
For details, refer to Device Specific Parameters (S32K3xx).
SWT
1 bit
Boot target watchdog configuration:
• When 0: disabled
• When 1: enabled before releasing the boot target from reset
PLL_ENABLE
1 bit
PLL enabled by HSE
• When 0: PLL not enabled by HSE
• When 1: PLL enabled by HSE only if BOOT_SEQ is also 1
SECURE_RECOVERY _
DISABLE
1 bit
Secure Recovery configuration
• When 0: Secure Recovery enabled
• When 1: Secure Recovery disabled
RESET_RECOVERY_
MODE
1 bit
Application entry in recovery mode sequence due to functional / destructive
reset can be enabled/disabled:
• When 0: Reset recovery mode Disabled
• When 1: Reset recovery mode Enabled
For details, refer to section Recovery Mode.
FW_USAGE_FLAG_
PROGRAM
1 bit
Used to enable the HSE Firmware Usage feature flag in UTEST.
• When 0: HSE Firmware Usage Feature flag is not programmed.
• When 1: HSE Firmware Usage Feature flag is programmed in UTEST if
not already programmed.
Also, removes the requirement to program 0xA5 marker in DCMRWP1
register during HSE Firmware Installation via MU Interface.
Usable only with SBAF >= v0.15.0. Boot Configuration Word.
Table 17. BCW content
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
81 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 82

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
When BOOT_SEQ equals 0 and BOOT_TARGET is set to a value different from 0, the start addresses of Apps
must also be provided in IVT, since it is at those addresses that the selected CPU subsystem are released from
reset .
Multiple bits in BOOT_TARGET can be set to 1 to release multiple CPU subsystems from reset at once.
For more details on IVT and BCW mapping, refer to Device Specific Parameters (S32K3xx).
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
82 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 83

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
5   HSE Firmware Usage
5.1  Service descriptor
HSE services are triggered by the host via service channels through the Messaging Unit (MU). The requests are
formatted within service descriptors (usually) stored in RAM.
A service descriptor is an ISO C99 data structure that encompasses the different parameters of a service to be
executed by the HSE firmware.
The service descriptor is defined by the C type hseSrvDescriptor_t.
 
    typedef struct hseSrvDescriptor_tag
    {
        /** @brief The service ID of the service descriptor */
        hseSrvId_t srvId;
        /** @brief The meta data related to the service */
        hseSrvMetaData_t srvMetaData;
        union
        {
            hseXXXSrv_t XXX;
            hseYYYSrv_t YYY;
        } hseSrv;
    } hseSrvDescriptor_t;
The service (for example, encryption, signature verification, and so on) is identified by the service ID in the
parameter srvID. The number and types of all the subsequent parameters within the service descriptor depend
on that service ID and are grouped in union hseSrv.
A complete and detailed description of each of the service descriptor supported in native by the NXP HSE
firmware can be found in the HSE Service API Reference Manual.
Important:
In case of pointer addresses, if the given address is of Internal Flash, user has to make sure that the respective
Flash block should not have the programming ongoing. This may terminate the service with error or firmware
may enter shutdown state. For more details, refer to Synchronizing Flash Read/Write Access Between HSE and
Application Core.
5.2  Service ID
A service ID is made of a version, type, a class, and subclass. It is defined by the C type hseSrvId_t. The
version field is used to highlight the current version for each service. When a version is changed, the current
service is no longer compatible with the previous one.
Bit field
31 ~ 24
23 ~ 16
15 ~ 8
7 ~ 0
Description
Service Version
Service Type
Service class
Service subclass
Table 18. Service ID format
Service Type
Description
0x00
Service request is queued and executed by the HSE in a FIFO fashion; this type of service can be
canceled if it is still in the job queue. (preemptive)
Table 19. Service Type
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
83 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 84

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
0xA5
Service request is directly executed by the HSE; this type of service cannot be canceled. (non-
preemtive)
Table 19. Service Type...continued
The below table lists the different service class that can be instantiated by the host.
Service class
Description
Service subclass
0x00
HSE firmware administration services
• Setting / reading system attributes
• Firmware update
• Cancel service
• Functional self-tests
• Boot Data Sign / Verify
• System rights authorization (User / Super
User)
• MSC Services
• Import/Export Stream Context
0x01
Cryptographic key management
• Format key catalogs
• Key import / export
• Get key Information / erase key(s)
• Key generation /derivation
• Key agreement
0x02
Cryptographic functions
• Encrypt / decrypt
• Sign / verify
• MAC generate / verify
• Hash
0x03
Random number generation
• Get random
0x04
Monotonic counter management
• Set monotonic counter value
• Increment counter
• Read-out counter
0x05
Secure memory regions (SMR) management
• SMR definition
• SMR installation
• SMR on-demand verification
0x07 ~ 0x8F
RFU
RFU
0x90
Extended services
• Customized services
0xA1
SHE
• Load Key, Load Plain Key
• Export RAM key
• GET UID
• Boot OK, Boot Failure
Table 20. Service classes
The service IDs are defined by the C macro HSE_SRV_ID_XXX where XXX indicates the service type. The
requests with the service ID that starts with 0x00A5XXXX cannot be canceled. The complete list of service IDs
can be found in the HSE Service API Reference Manual.
5.3  Service request and response
To trigger a service request, the host:
• Instantiates a service class in application RAM via the desired service descriptor
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
84 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 85

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Note:  It is also possible to have a service class instantiated in a constant area (for example, Flash)
• Selects a free service channel within one of the MU instances
• Provides the address of the instantiated service descriptor to the selected channel
Note:  At the time of using an address in ITCM and DTCM (tightly coupled memories) as input or output
address for any service, the host application must make sure that the address passed lies in the address ranges
given in the below tables for all SoC variants. User must add a fixed offset to the address.
Refer to the HSE Service API Reference Manual for the exact offset values for each memory. For example, the
ITCM0 address 0x00000400 is not accessible by the HSE. Instead, the same address is accessible at location
0x11000400.
To check the result of a service request, the host:
• Checks for the end of operation on the selected service channel
• Alternatively waits until the interrupt on the selected service channel is triggered
• Retrieves the service response from the selected channel, and checks for potential errors
For a description on how the MU is used for transferring service requests and receiving service responses, refer
to Messaging Unit.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
85 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 86

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The flow below illustrates how the host triggers a service request and handles the service response in a
synchronous way. The flow is completed with corresponding code snippets.
Service request to HSE 
(synchronous)
Select a service channel 
within a MU instance
Instantiate a service 
descriptor in RAM
Provide the address of the 
service descriptor to the
selected service channel
Wait for service completion
Analyze the service response
hseSrvDescriptor_tservice;
.../...
service.srvId = HSE_SRV_ID_SYM_CIPHER;
service.symCipherReq.cipherAlgo= HSE_CIPHER_ALGO_AES;
service.symCipherReq.cipherBlockMode= HSE_CIPHER_BLOCK_MODE_CTR;
service.symCipherReq.cipherDir= HSE_CIPHER_DIR_ENCRYPT;
.../...
MU = 0;
ch = HSE_MU_GetFreeChannel(MU);
ch = HSE_MU_SendRequest(MU, ch, &service);
while( HSE_MU_GetChannelStatus(MU, ch) == BUSY );
err = HSE_MU_ReceiveResponse(MU, 
ch);
if(err != 0)
{
.../...
}
End
Figure 51. Service request flow (synchronous)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
86 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 87

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The flow below illustrates how the host triggers a service request, checking for the service response in an
asynchronous way. The flow is completed with the corresponding code snippets.
Service request to HSE 
(asynchronous)
Select a service channel 
within a MU instance
Instantiate a service 
descriptor in RAM
Provide the address of the 
service descriptor to the
selected service channel
Enable the interrupt of the 
service channel
MU = 0;
ch = HSE_MU_GetFreeChannel(MU);
HSE_MU_EnableInterrupt(MU, ch);
End
hseSrvDescriptor_tservice;
.../...
service.srvId = HSE_SRV_ID_SYM_CIPHER;
service.symCipherReq.cipherAlgo= HSE_CIPHER_ALGO_AES;
service.symCipherReq.cipherBlockMode= HSE_CIPHER_BLOCK_MODE_CTR;
service.symCipherReq.cipherDir= HSE_CIPHER_DIR_ENCRYPT;
.../...
ch = HSE_MU_SendRequest (MU, ch, &service);
Figure 52. Service request flow (asynchronous)
The flow below illustrates the interrupt routine for checking a service response in an asynchronous way.
Interrupt from service 
channel
Analyze the service response
err = HSE_MU_ReceiveResponse(MU, 
ch);
if(err != 0)
{
.../...
}
End
Figure 53. Service response flow (asynchronous)
A service response is always provided by the HSE, via one of the service channels, to indicate the end of a
service request. It indicates if the service requested ended successfully with the value HSE_SRV_RSP_OK or
terminated with an error with a different value.
The service response is defined by the C type hseSrvResponse_t. The complete list of service responses
can be found in HSE Service API Reference Manual.
Important:  The service response must be read by the host to free the service channel associated.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
87 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 88

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
5.4  Service execution
5.4.1  Service execution order
When multiple masters are triggering multiple service requests on different MU instances, the HSE implements
the following service execution ordering:
• HSE parses each MU instance in a sequential order, starting from the MU instance that received the first
service request, in a round-robin fashion (when the last MU instance is reached, the HSE goes back to
MU0), until all the service requests are served.
• Within one MU instance, the HSE searches for the next service request to process, starting from the last
channel served, in a round-robin fashion (when the last service channel is reached, the HSE goes back to
service channel #0).
• If a service request is found, it is pushed to the job queue; then the HSE moves to the next MU instance.
• If no service request is found, the HSE moves to the next MU instance.
• An AES, MAC, or HASH operation interrupts an ECC or RSA operation. HSE allocates an execution period
of 666 microseconds (at 120MHz HSE core frequency) for ECC or RSA, and 3333 microseconds for AES,
MAC, and HASH operations. In this way, the fast operations don’t completely starve the heavy operations.
For example, if 300 hash services are sent during an RSA signature generation execution, HSE interrupts the
RSA operation to process hash services for 3333 microseconds (let's say 100 hash services), continues with
RSA operation for 666 microseconds, interrupts again the RSA service to execute 100 hash services (3333
microseconds) and so on. If there are no hash services to be processed, the RSA operation continues without
interruption.
Important:
• The non-HW accelerated crypto operations (refer to Status Bits for HSE FW and Secure BAF are considered
heavy operations and can be interrupted by fast operations.
• If the host requests only symmetric operations (for example, fast operations), HSE schedules the service
requests in a round-robin fashion across MU instances and channels (as described above).
• Once a symmetric crypto operation is programed into the HW crypto accelerator, it cannot be interrupted.
For this reason, if large data is used as input for the symmetric crypto operation along with other symmetric
crypto operations (with small input data), the recommendation is to use the streaming execution mode for
large data inputs (start/update/finish calls). In this way, other symmetric crypto operations with small input data
can interleave the symmetric crypto operation with large input data.
The execution scheme ensures that all MU instances and all service channels are equally served, avoiding one
MU instance taking precedence over all other MU instances.
The below figure illustrates how service and jobs are handled by the HSE.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
88 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 89

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Wait for 
Interrupts
TDES / AES / SHA
operation
RSA / ECC
operation
Other operations
(admin, etc.)
Initiate operation in 
dedicated crypto
engine
Compute operation 
with HW engine
(CPU intensive)
Compute operation 
(not CPU intensive)
Retrieve the 
service request
Queue job
Dispatch job 
from queue
No job in
queue
Crypto engine 
Interrupt
(non-blocking)
Return response to 
service
MU 
Interrupt
Complete
Complete
(blocking)
Complete 
(non-blocking)
Fast non-blocking 
operation
Blocking
operation
MU 
Interrupt
MU 
Interrupt
Complete
Figure 54. Illustrating service execution by the HSE
Secret-key based cryptographic operations (for example, AES) or hash operations are accelerated by dedicated
cryptographic engines. Once initialized with the operation to perform, they run independently from the HSE
firmware. Upon completion, an interrupt is served to return the service response to the host.
RSA/ECC operations that are CPU intensive (although hardware accelerated) can be interrupted by other
service requests. This means that other cryptographic operations (for example, AES) can be interleaved with
those time-consuming operations.
5.4.2  Execution rights (Super User vs. User)
5.4.2.1  Definition
The execution of certain HSE services is conditioned by the execution rights granted to the host.
There are two levels of execution rights that can be granted to the host:
• Super User (SU) rights
• User rights
The below tables list the differences in execution rights in the selected HSE services.
Service
SU rights
User rights
Encryption
Optional
Mandatory
Import a new NVM key (that is, in an empty key slot)
Authentication
Optional
Mandatory
Table 21. Execution rights and respective limitations in Key Management
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
89 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 90

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Service
SU rights
User rights
NVM key generation (that is, in an empty key slot)
Possible
Not possible
NVM key deletion
Possible
Not possible
Copy part of a RAM key to an NVM key slot
Possible
Not possible
Load a user defined ECC curve
Possible
Not possible
Table 21. Execution rights and respective limitations in Key Management...continued
Service
SU rights
User rights
Set HSE system attributes
Possible
Not possible (except for SET-ONCE-ATTR
and RAM-RW attribute types)
Authenticate the host system images (IVT)
Possible
Not possible
Complete SMR entry update (including key handle)
Possible
Not possible
Update a Core Reset entry
Possible
Not possible
Monotonic counter configuration
Possible
Not possible
Table 22. Execution rights and respective limitations in HSE configuration
Note:
The list of all service identifiers that can be executed with limitations (or fewer restrictions) when the device has
Super User execution rights can be found in section Super-user Execution Rights.
In addition, the host is given an identity (HID) depending on the life-cycle state and on the grant condition for the
execution rights, as described in the below tables.
Execution rights
Grant condition
Host identity
SU
After reset
Depending on LC value
User
After reset
Depending on the LC value. It can be granted unconditionally after an
HSE authorization requests (with User rights) at runtime.
SU
After authorization
Depending on the key group owner of the authorization key handle
Table 23. Determining the host identity
LC
Host identity (HID)
CUST_DEL
System integrator (CUST)
OEM_PROD
OEM
IN_FIELD
Not identified (ANY)
PRE_FA
Not identified (ANY)
Table 24. Host identity vs. LC
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
90 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 91

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Key group owner
Host identity (HID)
HSE_KEY_OWNER_CUST
System integrator (CUST)
HSE_KEY_OWNER_OEM
OEM
HSE_KEY_OWNER_ANY
Not identified (ANY)
Table 25. Host identity vs. key group owner
The host can check the current execution rights and host identity using the HSE status flags
HSE_STATUS_CUST_SUPER_USER and HSE_STATUS_OEM_SUPER_USER.
HSE_STATUS_CUST_
SUPER_USER
HSE_STATUS_OEM_
SUPER_USER
Execution rights
Host identity (HID)
1
0
SU
CUST
0
1
SU
OEM
0
0
User
ANY
1
1
SU
ANY (key catalogs are not formatted -
no key is installed)
Table 26. Checking execution rights and host identity
5.4.2.2  Execution rights after reset
The HSE firmware initialization and configuration align with the ECU manufacturing steps, and are taking place
while the life-cycle state is CUST_DEL or OEM_PROD.
LC state
ECU manufacturing step
Owner of the configuration
CUST_DEL
ECU assembly and initial configuration
System integrator (NXP’s customer)
OEM_PROD
ECU vehicle integration and final configuration
OEM
Table 27. LC states vs. ECU manufacturing steps
In those LC states, the host is granted with Super User (SU) rights after reset, which gives the configuration
owner high execution privileges and no limitation on service requests. In other LC states, the host is granted
with User rights after reset, which gives the most restricted execution privileges and limits the possibilities of
certain services.
The execution rights after reset in LC states CUST_DEL and OEM_PROD can be forced to User
rights configuring the “Start As User” option within hseAttrExtendedCustSecurityPolicy_t and
hseAttrExtendedOemSecurityPolicy_t attributes.
LC state
HSE system attribute
Host rights after reset
Host identity (HID)
CUST_DEL
CUST_START_AS_USER = 0
Super User (SU)
System integrator (CUST)
CUST_DEL
CUST_START_AS_USER = 1
User
System integrator (CUST)
OEM_PROD
OEM_START_AS_USER = 0
Super User (SU)
OEM
OEM_PROD
OEM_START_AS_USER = 1
User
OEM
IN_FIELD
N/A
User
Not identified (ANY)
PRE_FA
N/A
User
Not identified (ANY)
Table 28. Execution rights after reset
Note:  In FA lifecycle, the HSE Firmware never executes.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
91 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 92

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
5.4.2.3  Requesting for SU rights
The host can temporarily request the HSE for Super User (SU) rights via a specific administration service. The
request must be authenticated as follows:
• The host triggers the request and the HSE returns a random challenge
• The host then computes a cryptographic response over the challenge using the selected authentication key
and provides it to the HSE
• If the response provided is the expected one, the HSE grants the host with SU rights
SU rights are granted until the next reset, or until the host request for User rights: such request does not require
any authentication.
SU rights are provided to the owner of the key used for authentication. This is different from the default SU
rights after reset that are granted according to the LC state (see Execution Rights (Super User vs User)).
SU rights, when granted through the administration service, are granted only for the MU instance through which
SU rights were requested. All other MU instances subsequently receive User rights.
The administration service to request SU rights is documented in Request for Super User Rights.
5.4.2.4  Flash resources locked during HSE execution
The following figure explains how HSE firmware is locking the Flash blocks to ensure the synchronization
between the application core and the HSE. For details, refer to the section Synchronizing Flash Read/Write
Access Between HSE and Application Core.
Figure 55. Flash resources locked during HSE execution
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
92 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 93

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
5.4.3  One-pass execution mode
All cryptographic services can be executed in one-pass mode: upon reception of a service request, the HSE
gets the service parameters, reads the data to process, eventually writes the results to memory and returns a
service result to the host.
For certain services that can operate in streaming mode (see Streaming Execution Mode), the data field
accessMode must be set to HSE_ACCESS_MODE_ONE_PASS to force the execution in one-pass mode.
5.4.4  Streaming execution mode
For certain cryptographic services which involve manipulation of large data or streams, the host has the
possibility to run operations in streaming mode, that is, in multiple service calls instead of one. This flexibility in
use can be helpful when, for instance, the data to process by the HSE are not yet entirely available in the host
memory.
The streaming mode of operation can be split into three steps:
• The initial step (“START”): this is the first service call from the host to initialize the service; only one START
service call can be performed
• The update step (“UPDATE”): this is a subsequent service call from the host to provide the HSE with the
“next” data to process; there can be multiple update steps performed
• The final step (“FINISH”): this is the final service call from the host to get the result of the operation; only one
FINISH service call can be performed
The data field accessMode within the service descriptor specifies the step to process by the HSE:
• accessMode = HSE_ACCESS_MODE_START for the initial step
• accessMode = HSE_ACCESS_MODE_UPDATE for the update step
• accessMode = HSE_ACCESS_MODE_FINISH for the final step
The data field streamId is the stream identifier that links each step (that is, calls) together.
The stream identifier is chosen by the host and is associated with a MU instance. Its value must be between
0 and (HSE_STREAM_COUNT – 1), so it is possible for the host to initiate up to HSE_STREAM_COUNT
streams per MU instance. HSE_STREAM_COUNT is defined in the HSE header files.
Once a service ID is set on the initial step (START) and associated with a stream identifier, all subsequent calls
(UPDATE and FINISH) must refer to the same service ID for that stream identifier. Using a different service ID
yields a service error.
The START and FINISH steps must be unique. If START is called before FINISH, the corresponding stream
identifier is reset, and the previous execution context is lost.
Once a stream has been started, its execution context can be securely exported outside the HSE to be
reimported at a later stage. This feature allows, for example, the computation of a digest or a MAC over data
sets that grow sequentially over time: instead of recomputing the entire data set every time, it is possible to
update the computation with the data added to the set, therefore reducing the computation time.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
93 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 94

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
This is what the following figure illustrates.
D0
D0
D1
data-set
data-set
Start hash 
stream #0
Update hash 
stream #0 with D0
Export 
stream #0
Finish hash 
stream #0
Import 
stream #0
Update hash 
stream #0 with D1
Export 
stream #0
Finish hash 
stream #0
Execution 
context
stream #0
(encrypted)
time
time
digest over 
data-set
time
Figure 56. Illustrating streaming contexts import / export
Stream execution context import and export services are part of the HSE administration services documented in
chapter Administration Services.
There are no restrictions related to the service channel used in streaming mode: it does not have to be the
same for each of the calls.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
94 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 95

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The below source code illustrates how an AES CMAC can execute in streaming mode. The buffer[] array
is used as the data input twice (in the START and UPDATE calls). The resulting CMAC is stored in the mac[]
array in the FINISH call.
void test_aes_cmac_in_streaming(void)
{
    hseSrvDescriptor_t* pHseSrvDesc;
    hseMacSrv_t*        pMacSrv;
    hseSrvResponse_t    srvResponse;
    uint8_t  buffer[64];
    uint8_t  mac[16];
    uint32_t macLen = sizeof(mac);
    uint8_t  ch;
    uint8_t  MU = 0;
    uint8_t  ID = 0;
    …/… (e.g. pointer initializations)
    // initialization of the MAC service request
    pHseSrvDesc->srvId = HSE_SRV_ID_MAC;
    pMacSrv = &(pHseSrvDesc->hseSrv.macReq);
    macScheme.macAlgo             = HSE_MAC_ALGO_CMAC;
    macScheme.sch.cmac.cipherAlgo = HSE_CIPHER_ALGO_AES;
    pMacSrv->macScheme.macAlgo    = HSE_MAC_ALGO_CMAC;
    pMacSrv->macScheme.sch.cmac.cipherAlgo = HSE_CIPHER_ALGO_AES;
    pMacSrv->authDir     = HSE_AUTH_DIR_GENERATE;
    pMacSrv->keyHandle   = GET_KEY_HANDLE(HSE_KEY_CATALOG_ID_NVM, 2, 1); // 2nd key slot in 3rd key
 group
    pMacSrv->inputLength = sizeof(buffer);
    pMacSrv->pInput      = buffer;
    pMacSrv->sgtOption   = 0;
    // streaming mode: initial step
    pMacSrv->streamId   = ID;
    pMacSrv->accessMode = HSE_ACCESS_MODE_START;
    srvResponse = runSrv(pHseSrvDesc);
    if(HSE_SRV_RSP_OK != srvResponse) goto error;
    …/… (e.g. waiting for further data to be available in array buffer)
    // streaming mode: update step
    pMacSrv->streamId   = ID;
    pMacSrv->accessMode = HSE_ACCESS_MODE_UPDATE;
    srvResponse = runSrv(pHseSrvDesc);
    if(HSE_SRV_RSP_OK != srvResponse) goto error;
    …/… (e.g. waiting for further data to be available in array buffer)
    // streaming mode: final step
    // retrieves the authentication tag (AES-CMAC)
    pMacSrv->inputLength = 0;
    pMacSrv->pTagLength  = &macLen;
    pMacSrv->pTag        = mac;
    pMacSrv->streamId    = ID;
    pMacSrv->accessMode  = HSE_ACCESS_MODE_FINISH;
    srvResponse = runSrv(pHseSrvDesc);
    if(HSE_SRV_RSP_OK != srvResponse) goto error;
error:
    …/…(e.g. analysing the response)
    return;
}
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
95 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 96

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
5.4.5  Canceling a service request
A service request accepted by the HSE can be canceled only under the following conditions:
• The services with the ID= 0x00A5XXXX cannot be canceled.(non-preemptive)
• Its associated job is still in the pending job queue (that is, the HSE has not yet started processing it).
See Administration Services for more information on how to cancel a service request.
5.4.6  Scatter/gather input and output
Input/output data to/from the HSE services are provided as pointers to byte arrays. In addition, the HSE
supports, for specific cryptographic services, the possibility to provide pointers to scatter/gather lists that chain
pointers to byte arrays. This allows for processing, in one single service request, data that are distributed (that is
“scattered”) across multiple byte arrays (or chunks) in memory.
The scatter/gather list format supported by the HSE is an array of type hseScatterList_t as illustrated in the
below figure.
Chunk #0
Chunk #1
Chunk #2
byte size of Chunk #0
byte size of Chunk #1
0 0
0 0
byte size of Chunk #2
0 1
pointer to Chunk #0
pointer to Chunk #1
pointer to Chunk #2
bit #31 always 0
bit #30 set to 1
to indicate the end
of the list
hseScatterList_t
last chunk
Figure 57. Illustrating a scatter/gather list
The first data field length is a 32-bit word that provides:
• One control bit (bit #30) that indicates the end of the scatter/gather list when set to 1; in any case, the
maximum number of chunks in one list cannot exceed HSE_MAX_NUM_OF_SGT_ENTRIES which is defined in
HSE header files.
• The byte size (encoded from bit #0 to bit #29) of the chunk pointed by the second data field pPtr.
The HSE services that support scatter/gather input and/or output have a data field sgtOption of type
hseSGTOption_t. This field indicates the type of data pointed by pInput and pOutput when available:
• When both pInput and pOutput points to byte arrays, sgtOption must be set to
HSE_SGT_OPTION_NONE (0)
• When pInput points to a scatter/gather list, this sgtOption must be set to HSE_SGT_OPTION_INPUT
• When both pInput and pOutput points to scatter/gather list, sgtOption must be set to
HSE_SGT_OPTION_INPUT | HSE_SGT_OPTION_OUTPUT
All possible combinations are summarized in the below table.
pInput points to…
pOutput points to…
sgtOption set to…
Byte array
Byte array or not provided
HSE_SGT_OPTION_NONE (0)
Table 29. Scatter/gather options vs. input / output parameter types
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
96 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 97

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
pInput points to…
pOutput points to…
sgtOption set to…
Scatter/gather list
Byte array or not provided
HSE_SGT_OPTION_INPUT
Byte array
Scatter/gather list
HSE_SGT_OPTION_OUTPUT
Scatter/gather list
Scatter/gather list
HSE_SGT_OPTION_INPUT | HSE_SGT_OPTION_
OUTPUT
Table 29. Scatter/gather options vs. input / output parameter types...continued
In addition, the corresponding input and output sizes specified in the service request must account for the total
number of bytes to process. This means that if this inputLength is the input size of a scatter/gather list, then it
must equal the sum of all byte sizes provided in the list.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
97 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 98

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6   Cryptographic Services
6.1  Cryptographic keys
6.1.1  Scope
The keys accessible to the host via the cryptographic services are organized in groups of certain types, within
catalogs that are statically configured by the host. Each key has a value and certain attributes contained into
individual key slots, that are dynamically configured by the host via key management services. These keys can
be provisioned by different mechanisms, including generation and derivation from other keys.
The NVM and RAM key catalogs are defined in SYS-IMG. The ROM key catalog is defined in the HSE.
HSE Firmware
Key group #0
10 x AES 128-bit keys
Key slot #0
Key slot #1
…/…
Key slot #9
Key group #1
1 x ECC 256-bit key pair
Key slot #0
Key catalog ROM
Key catalog RAM
Key catalog NVM
Key slot #1
Key group #0
1 x AES 128-bit key
Key slot #0
Key group #1
2 x AES 256-bit keys
Key slot #0
Key slot #1
Key group #2
1 x RSA 2048-bit key
Key slot #0
Key group #3
1 x ECC 256-bit key
Key slot #0
SYS-IMG
Figure 58. Illustrating the key catalogs
6.1.2  Key storage
SYS-IMG contains:
• The structure of the RAM and NVM key catalogs
• The NVM key properties
• The NVM key values, or a pointer to the key values stored in the host memory for the key types
HSE_KEY_TYPE_RSA_PUB_EXT and HSE_KEY_TYPE_ECC_PUB_EXT
Key properties and values are updated within SYS-IMG after successful key provisioning operations.
SYS-IMG is saved in secure NVM (that is, internal Flash) by the host. SYS-IMG is loaded and authenticated by
the HSE at start-up.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
98 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 99

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.1.3  Key group and key type
A key group is a set of cryptographic keys of the same type. Each group is identified by an index within the key
catalog where it is declared (see next section). The index aligns with the order of declaration in the group: the
first group has the index 0, the second group has the index 1, and so on.
The below table lists the different key types supported by the HSE.
Key type
Description
Key catalog
HSE_KEY_TYPE_AES
AES key
NVM and RAM
HSE_KEY_TYPE_SHE
AES key used with SHE specific services
NVM and RAM
HSE_KEY_TYPE_HMAC
HMAC key
NVM and RAM
HSE_KEY_TYPE_RSA_PAIR
RSA key pair (public and private)
NVM only
HSE_KEY_TYPE_RSA_PUB
RSA public key
NVM and RAM
HSE_KEY_TYPE_RSA_PUB_EXT
RSA public key, stored in application NVM
NVM and RAM
HSE_KEY_TYPE_ECC_PAIR
ECC key pair (public and private)
NVM and RAM
HSE_KEY_TYPE_ECC_PUB
ECC public key
NVM and RAM
HSE_KEY_TYPE_ECC_PUB_EXT
ECC public key, stored in application NVM
NVM and RAM
HSE_KEY_TYPE_DH_PAIR
DH key pair (public & private)
NVM and RAM
HSE_KEY_TYPE_DH_PUB
DH public key
NVM and RAM
HSE_KEY_TYPE_SHARED_SECRET
Shared secret - can be used to derive a secret key
RAM only
Table 30. Key types
Except for the key types HSE_KEY_TYPE_ECC_PUB_EXT and HSE_KEY_TYPE_RSA_PUB_EXT, key values
and attributes are stored in key slots exclusively accessible by the HSE.
For the key types HSE_KEY_TYPE_ECC_PUB_EXT and HSE_KEY_TYPE_RSA_PUB_EXT, the key values
are stored in application NVM to save space in SYS-IMG, since it is common that RSA and ECC public keys are
provided in the form of certificates that are comparatively larger than the key value itself.
The key type HSE_KEY_TYPE_SHARED_SECRET is meant to be used as a temporary value only. Therefore,
it must only to be declared in the RAM key catalog.
The key type HSE_KEY_TYPE_RSA_PAIR must only be declared in the NVM key catalog.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
99 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 100

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
SYS-IMG
Key catalog NVM
Key catalog RAM
RSA_PUB_EXT
Key properties
Pointer to key values
RSA_PAIR
Key properties
Key values
AES
Key properties
Key values
ECC_PUB_EXT
Key properties
Pointer to key values
ECC_PAIR
Key properties
Key values
AES
Key properties
Key values
User file
RSA public key
(X.509 certificate)
ECC public key
(X.509 certificate)
Figure 59. Illustrating the repartition of key values and properties
6.1.4  Key slot
A key slot is a memory container that holds a single key, with its value(s) and attributes. Each slot is identified
by an index within the key group where it is declared. The index aligns with the order of presence in the group:
the first key slot has the index 0, the second key slot has the index 1, and so on.
6.1.4.1  Key values
Key values are represented by one or several unsigned integers of various sizes (expressed in bit length)
depending on their types. The below table lists the key characteristics in correspondence with Key values.
Key type
Key value(s)
Key size and properties
RSA private key
Private exponent 
Modulus 
The key size is given by the bit length of , which equals the bit length of
 is an integer that satisfies the equation 
 is the public exponent (see below)
 is the result of the multiplication of two random primes  and 
(
)
 is the Euler's totient function: 
Table 31. Key characteristics
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
100 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 101

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Key type
Key value(s)
Key size and properties
RSA public key
Public exponent 
Modulus 
The key size is given by the bit length of 
 is an integer co-prime with 
; usually,  is a small prime value (for
example, 65537 (0x10001))
 is the shared modulus with the private key (see above)
ECC private key
Private scalar 
The key size is given by the bit length of 
 is a random integer
ECC public key
Public point 
The key size is given by the bit length of  and  coordinates of 
, which
equals the bit length of 
 is the result of the multiplication of the private scalar 
 (see above) and
a given point  (
) (see also Notes on ECC)
 is the base point on a given curve 
DH private key
Private exponent 
Modulus 
The key size is given by the bit length of 
 is a random integer
 is a prime
DH public key
Temporary secret 
Modulus 
The key size is given by the bit length of 
 is the result of the modular exponentiation with the private exponent 
(see above) over the base  (
)
 is the modulus shared with the private key
Note:
• Base  is a primitive root modulus  that satisfies the equation
; usually,  is a small integer (for example, 2, 3, and
so on).
 is the Euler's totient function: 
•
 is provided by the host only when the key is generated and is not
stored by HSE
AES key
Secret 
The key size is given by the bit length of 
 is a random integer of size 128 bits, 192 bits or 256 bits
HMAC key Shared
secret
Secret 
The key size is given by the bit length of 
 is a random integer
Table 31. Key characteristics...continued
6.1.4.1.1  Notes on RSA
The HSE supports RSA key pair generation. However, due to the nature of those keys, which involve finding
two large prime numbers, the key generation can take several seconds, depending on the size of the key.
6.1.4.1.2  Notes on ECC
Elliptic curve cryptography (ECC) operations are based on point additions (
 and 
 when
). The points lie on “elliptic” curves that are defined by an equation and a set of parameters.
The HSE supports three types of curves (that is, curve equations) in the prime field (
) as listed in the
below table.
Curve type
Curve equation
Conditions
Weierstrass form
The base point  is such that 
Table 32. Elliptic curve types supported
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
101 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 102

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Montgomery form
 the order of ;  must be prime
 defines the field of ;  must be prime
Twisted Edwards
form
Curve parameters  and  are derived from the
birationally equivalent Montgomery curves
Table 32. Elliptic curve types supported...continued
The HSE also supports:
• A set of predefined Weierstrass curve parameters (that is, ,
,
,  and ) as defined by commonly used
standards (for example, NIST)
• A set of user-defined Weierstrass curve parameters, which can be set when the ECC keys are imported or
generated
• One Montgomery curve, to be only used with the ECDH key agreement protocol
• One twisted Edwards curve, which is the birational equivalent to the only Montgomery curve supported; this
curve is to be used only with the EdDSA signature algorithm
For keys on the twisted Edwards curve, the public point  is computed with a value 
 that is derived from the
private scalar 
.
For more information, refer to Key Values.
6.1.4.1.3  Notes on DH
In the Diffie-Hellmann (DH) key agreement protocol, the use of the base  is only required to compute the
temporary secret 
, which is then used by the other party to compute a shared secret.
In the HSE, the base  is not saved. Instead 
 is saved, along with the modulus  and the private exponent .
6.1.4.2  Key attributes
The below table lists the key attributes available to the host for configuring the size, access, and the usage of
each individual cryptographic key. For the SHE key type HSE_KEY_TYPE_SHE as one more access restriction
flag (WILDCARD) that can be set via the SHE key update protocol.
Key attribute
Type
Description
Bit size
16-bit integer
The key size in bits
Update counter
32-bit integer
A counter used to protect against roll-back updates; when updating
a key value and attributes, the new counter value must be strictly
above the current counter value.
For NVM keys, the key counter must be between 0 and 0xFFFFFF
FE (inclusive).
For RAM keys, the 32-bit integer key counter is forced to 0xFF
FFFFFF (not used).
Exception: only 28-bits are used for SHE keys; for SHE RAM keys,
the counter is forced to zero.
Access restriction flags
Bit field
A set of flags that define access restrictions to the key; see Key
access restriction flags.
Usage flags
Bit field
A set of flags that define how a key can be used; see Key usage
flags.
Table 33. Key attributes
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
102 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 103

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Key attribute
Type
Description
MU instance map
Bit field
A set of flags that define what Messaging Unit (MU) instances can
trigger services making use of the key; this attribute is defined at key
group level.
SMR verification map
Bit field
A set of flags that define what secure memory regions (SMR) must
be verified before the key can be used; see SMR verification map for
key usage and related section in this document.
Key Type
8-bit integer
The key type as defined in Key access restriction flags.
Union of “ECC Curve ID",
“RSA Public Exponent Size”
and “AES Block mode”
8-bit integer
Either: the curve ID (used with ECC keys).
Or: the size (in bytes) of the RSA Public Exponent (used with RSA
keys).
Or: an aesBlockModeMask that specified the block cipher modes
that can be used with an AES key.
Table 33. Key attributes...continued
The update counter is managed by the key provisioning services. This counter is only available for the keys in
the NVM key catalog and not available for the following key types:
• HSE_KEY_TYPE_RSA_PUB
• HSE_KEY_TYPE_RSA_PUB_EXT
• HSE_KEY_TYPE_ECC_PUB
• HSE_KEY_TYPE_ECC_PUB_EXT
• HSE_KEY_TYPE_DH_PUB
• HSE_KEY_TYPE_SHARED_SECRET
The access restriction flags can be set using a binary OR combination of the enumerates listed in the below
table.
Enumerate
Influence on the key when set
HSE_KF_ACCESS_WRITE_PROT
The key is write-protected.
HSE_KF_ACCESS_DEBUG_PROT
The key cannot be accessed (that is, used) when a debugger is
connected to the host when life cycle is OEM_PROD or IN_FIELD; in
CUST_DEL LC, this access restriction flag has no effect.
HSE_KF_ACCESS_ EXPORTABLE
If it is set, the key can be exported out of the HSE; otherwise, the key
cannot be exported.
Note:  RSA/ECC private keys are never exportable.
Table 34. Key access restriction flags
To specify, for example, that a key is write protected and not exportable, its restriction flags are set to:
HSE_KF_ACCESS_WRITE_PROT.
The usage flags can be set using a binary OR combination of the enumerates listed in the below table.
Enumerate
Influence on the key when set
HSE_KF_USAGE_ENCRYPT
The key can be used for encryption operations.
HSE_KF_USAGE_DECRYPT
The key can be used for decryption operations.
HSE_KF_USAGE_SIGN
For RSA/ECC keys: the key can be used for signature generation (only
applicable to the private key part).
For AES/HMAC keys: the key can be used for MAC generation.
Table 35. Key usage flags
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
103 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 104

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Enumerate
Influence on the key when set
HSE_KF_USAGE_VERIFY
For RSA/ECC keys: the key can be used for signature verification (only
applicable to the public key part).
For AES/HMAC keys: the key can be used for MAC verification.
HSE_KF_USAGE_EXCHANGE
For DH/ECC keys: the key can be used in key agreement protocols (DH/
ECDH).
HSE_KF_USAGE_DERIVE
The key can be used to derive other keys; cannot be set for RSA, ECC,
or DH keys.
HSE_KF_USAGE_KEY_PROVISION
When this flag is set, only key import and export operations can
instantiate that key, that is, the key can only be used to e.g. decrypt
a key value that is imported encrypted, or encrypt a key value that is
exported.
When the flag is cleared, only cryptographic operations (encrypt,
decrypt, sign, verify) on memory contents can instantiate that key, that
is, the key can be used to for example, encrypt a plaintext, or verify a
signature; attempting to use that key in key import / export operations
triggers an error.
HSE_KF_USAGE_AUTHORIZATION
When this flag is set, the key can be used to verify a host request to
elevate its execution rights to Super User (SU); this flag can only be set
with the HSE_KF_USAGE_VERIFY flag (HSE_KF_USAGE_SIGN must
not be set).
HSE_KF_USAGE_SMR_DECRYPT
When this flag is set, the key can be used for SMR decryption. If this
bit is set during key installation, the HSE firmware sets the HSE_KF_
USAGE_DECRYPT flag to zero.
Table 35. Key usage flags...continued
To specify, for example, that an AES key can be used for CMAC verification and key derivation, its usage flags
are set to: HSE_KF_USAGE_VERIFY | HSE_KF_USAGE_DERIVE.
The MU instance map is defined at the key group level in the key catalog definition. See Key catalog.
The SMR verification map defines 1 bit for 1 SMR index as listed in the below table. This allows the application
to restrict key usage depending on the SMR verification status. For more details, refer to the related section in
this document.
Enumerate
Influence on the key when set
HSE_KF_SMR_0
The key can be used only if the secure memory region #0 has been successfully verified.
HSE_KF_SMR_1
The key can be used only if the secure memory region #1 has been successfully verified.
…
…
HSE_KF_SMR_7
The key can be used only if the secure memory region #7 has been successfully verified.
Table 36. SMR verification map for key usage
To specify, for example, that a key can be used only when the secure memory regions #2 and #5 are
successfully verified, the SMR verification map must be set to: HSE_KF_SMR_2 | HSE_KF_SMR_5.
An AES key can be configured to be used with specific AES cipher modes. These are provided as a bit mask in
the key attributes using the aesBlockModeMask field. If the mask is set 0, any block cipher mode can be used
with that AES key.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
104 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 105

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.1.5  Key catalog
Keys are managed in three key catalogs, as described in the below table. Each key catalog is identified by a
unique identifier and holds a set of key groups. The structure of the NVM and RAM key catalogs is configured
by the host, whereas the ROM key catalog structure is fixed by design.
Key catalog ID
Value
Configurable
Description
HSE_KEY_CATALOG_ID_ROM
0
No
ROM key catalog; keys stored in secure NVM,
provisioned by NXP before shipment.
HSE_KEY_CATALOG_ID_NVM
1
Yes
NVM key catalog; key values stored in SYS-IMG or in
application NVM for (select) public RSA and ECC key
certificates; key attributes stored in SYS-IMG.
HSE_KEY_CATALOG_ID_RAM
2
Yes
RAM key catalog; key attributes and values stored in
secure RAM.
Table 37. Key catalogs
6.1.5.1  ROM key catalog
The ROM key catalog references four keys (see below table) provisioned by NXP that can be used by the host
in select services.
Key group
index
Key slot index Key type
Key size and information
0
HSE_KEY_TYPE_AES
256-bit device-specific secret.
It can be used to encrypt/decrypt application data.
0
1
HSE_KEY_TYPE_AES
256-bit shared secret (owned by NXP).
1
0
HSE_KEY_TYPE_RSA_PUB
3072-bit modulus Public exponent 
 65537
(0x10001) (corresponding to the private key
owned by NXP). It can only be used for signature
verification or key decryption during key
provisioning operation.
2
0
HSE_KEY_TYPE_ECC_PUB
256-bit public point NIST curve P-256
(corresponding to the private key owned by NXP).
It can only be used for signature verification during
key provisioning operation.
Table 38. ROM key catalog configuration
The ROM keys can be accessed via any MU instance.
The last three ROM keys from the table (AES key owned by NXP, RSA, and ECC keys) can be used only for
key provisioning operation. This means that a customer secret can be encrypted and signed using the ROM
keys owned by NXP before being provisioned. For more details, contact the NXP support team.
The ROM keys have the following access restriction flags set: HSE_KF_ACCESS_WRITE_PROT |
HSE_KF_ACCESS_DEBUG_PROT.
The ROM keys have usage flags set depending on their slot index, as listed in the below table.
Note:
Depending on the HSE variant and software package (for example, Standard or Premium package), certain
ROM keys may be disabled (see the macros available in the HSE header files).
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
105 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 106

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Key group index
Key slot index
Usage restrictions
0
HSE_KF_USAGE_ENCRYPT | HSE_KF_USAGE_DECRYPT
0
1
HSE_KF_USAGE_DERIVE |
HSE_KF_USAGE_VERIFY |
HSE_KF_USAGE_ENCRYPT |
HSE_KF_USAGE_DECRYPT |
HSE_KF_USAGE_KEY_PROVISION
1
0
HSE_KF_USAGE_ENCRYPT |
HSE_KF_USAGE_VERIFY |
HSE_KF_USAGE_KEY_PROVISION
2
0
HSE_KF_USAGE_VERIFY |
HSE_KF_USAGE_KEY_PROVISION
Table 39. Usage restrictions on ROM keys
6.1.5.2  NVM and RAM key catalogs
The NVM and RAM key catalogs are statically configured by the host via a table, where each element is a set of
five attributes that defines a key group:
• A MU instance map which defines the MU instances that can be used to access the key group
• The owner of the key group, as described in Key group owners
• A key type as described in Key types
• The number of key slots (that is, the number of keys)
• The maximum key size in bits: see the below table
Key type
Maximum key sizes allowed
HSE_KEY_TYPE_AES
128, 192 or 256
HSE_KEY_TYPE_SHE
128
HSE_KEY_TYPE_HMAC
128 and 
 1152
HSE_KEY_TYPE_ECC_PAIR
192 and 
 640
HSE_KEY_TYPE_ECC_PUB
192 and 
 640
HSE_KEY_TYPE_ECC_PUB_EXT
192 and 
 640
HSE_KEY_TYPE_RSA_PAIR
1024 and 
 4096
HSE_KEY_TYPE_RSA_PUB
1024 and 
 4096
HSE_KEY_TYPE_RSA_PUB_EXT
1024 and 
 4096
HSE_KEY_TYPE_DH_PAIR
1024 and 
 4096
HSE_KEY_TYPE_DH_PUB
1024 and 
 4096
HSE_KEY_TYPE_SHARED_SECRET
128 and 
 2048
Table 40. Maximum key sizes vs. key types
Note:  Depending on the HSE variant and software package (e.g. Standard or Premium package), certain key
type may be disabled or the maximum key size may be smaller (see the macros available in the HSE header
files).
The MU instance map defines 1 bit for 1 MU instance as listed in the below table. This allows the application to
segregate the key group (hence individual key usage) per MU instance, that is per XRDC domains referencing
the different MU instances.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
106 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 107

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Enumerate
Influence on the key when set
HSE_MU0_MASK
The key group can be used through services triggered via the MU instance 0
HSE_MU1_MASK
The key group can be used through services triggered via the MU instance 1
Table 41. MU instance map for key usage
To specify, for example, that a key group can be used only through the MU instances 0 and 1, the MU instance
map must be set to: HSE_MU0_MASK | HSE_MU1_MASK.
A key group owner is defined to restrict the key management capabilities as described in the below table. For
more details on the key management services, refer to Key management.
Key group owner
Applies to
Description
HSE_KEY_OWNER_CUST
NVM key catalog
Keys can be managed without restrictions if the host is
granted with Super User (SU) rights and if the HID is CUST
(system integrator).
With User rights, the host can provision keys only based on
the knowledge of a key owned by CUST (system integrator).
HSE_KEY_OWNER_OEM
NVM key catalog
Keys can be managed without restrictions if the host is
granted with Super User (SU) rights and if the HID is OEM.
With User rights, the host can provision keys only based on
the knowledge of a key owned by the OEM.
HSE_KEY_OWNER_ANY
NVM[1]and RAM key
catalog
Keys can be managed without restrictions if the host is
granted with Super User (SU) rights.
With User rights, restrictions apply on the key management
services.
Table 42. Key group owners
[1]
NVM key groups with owner HSE_KEY_OWNER_ANY are permitted only for the key type HSE_KEY_TYPE_SHE.
A key catalog is configured through the C type hseKeyGroupCfgEntry_t.
The below code is an example of NVM key catalog configuration.
hseKeyGroupCfgEntry_t my_key_catalog[] = {
/* AES keys                            */
/* Accessible through MU0              */
/* key group #0:  5 x 128-bit AES keys */
/* key group #1: 10 x 192-bit AES keys */
/* key group #2: 15 x 256-bit AES keys */
    {HSE_MU0_MASK, HSE_KEY_OWNER_CUST,  HSE_KEY_TYPE_AES,           5,   128},
    {HSE_MU0_MASK, HSE_KEY_OWNER_CUST,  HSE_KEY_TYPE_AES,          10,   192},
    {HSE_MU0_MASK, HSE_KEY_OWNER_OEM,   HSE_KEY_TYPE_AES,          15,   256},
/* ECC keys                                  */
/* Accessible through MU0 and MU1            */
/* key group #3: 2 x 256-bit ECC key pairs   */
/* key group #4: 5 x 256-bit ECC public keys */
/* key group #5: 2 x 521-bit ECC key pairs   */
/* key group #6: 5 x 521-bit ECC public keys */
    {HSE_MU0_MASK | HSE_MU1_MASK, HSE_KEY_OWNER_OEM,   HSE_KEY_TYPE_ECC_PAIR,      2,   256},
    {HSE_MU0_MASK | HSE_MU1_MASK, HSE_KEY_OWNER_OEM,   HSE_KEY_TYPE_ECC_PUB,       5,   256},
    {HSE_MU0_MASK | HSE_MU1_MASK, HSE_KEY_OWNER_OEM,   HSE_KEY_TYPE_ECC_PAIR,      2,   521},
    {HSE_MU0_MASK | HSE_MU1_MASK, HSE_KEY_OWNER_OEM,   HSE_KEY_TYPE_ECC_PUB,       5,   521},
/* RSA keys                                    */
/* Accessible through MU1                      */
/* key group #7:  2 x 2048-bit RSA key pairs   */
/* key group #8: 10 x 4096-bit RSA public keys */
/* key group #9: 15 x 4096-bit RSA public keys (stored in application NVM) */
    {HSE_MU1_MASK, HSE_KEY_OWNER_OEM,   HSE_KEY_TYPE_RSA_PAIR,      2,  2048},
    {HSE_MU1_MASK, HSE_KEY_OWNER_OEM,   HSE_KEY_TYPE_RSA_PUB,      10,  4096},
    {HSE_MU1_MASK, HSE_KEY_OWNER_OEM,   HSE_KEY_TYPE_RSA_PUB_EXT,  15,  4096},
    {0, 0, 0, 0, 0}
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
107 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 108

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
};
The end of key catalog configuration table must be indicated with the element {0, 0, 0, 0, 0 }.
The maximum number of key groups and the maximum number of key slots that can be declared at compile
time in both the NVM and RAM key catalogs depends on the HSE implementation. Those maximum values are
defined by three C macros defined in the HSE header files, as documented in the below table.
C macro
Description
HSE_TOTAL_NUM_OF_KEY_GROUPS
Total number of key groups that can be declared altogether in both the
NVM and RAM key catalogs
HSE_MAX_NVM_STORE_SIZE
The maximum size (in bytes) of the NVM key catalog
HSE_MAX_RAM_STORE_SIZE
The maximum size (in bytes) of the RAM key catalog
Table 43. Maximum number of key groups and key slots
It is not possible to specify more than 256 key slots within one key group.
The NVM and RAM key catalog configurations are validated by the HSE during the key catalog formatting
process (see below).
6.1.5.3  Key catalog formatting
The NVM and RAM key catalogs must be formatted before any keys can be provisioned. This process is
handled via a key catalog formatting service, defined by the structure hseFormatKeyCatalogsSrv_t.
This service is only available to the host when LC is CUST_DEL. It must be the first configuration step of the
HSE.
The key catalog formatting takes as inputs:
• A pointer to the NVM key catalog configuration: pNvmKeyCatalogCfg
• A pointer to the RAM key catalog configuration: pRamKeyCatalogCfg
Upon successful completion, the service creates the key catalogs within SYS-IMG in secure RAM.
The service can fail for one of the following reasons:
• The number of key groups declared in both catalogs exceeds the limit supported by the HSE
• The number of key slots declared in both catalogs exceeds the limit supported by the HSE
• The overall size of the key material declared does not fit within the maximum allowed size
• The key group provided in one of the table entries is incorrect (see Key types)
• The key type HSE_KEY_TYPE_RSA_PAIR is specified for a key group in the RAM key catalog
• The key type HSE_KEY_TYPE_SHARED_SECRET is specified for a key group in the NVM key catalog
• The maximum key size provided for one of the key groups is incorrect
6.1.5.4  Empty keys
Right after the NVM and RAM key catalog formatting operation, the keys declared in those catalogs are empty.
An empty key cannot be used by the host.
For the keys declared as HSE_KEY_TYPE_SHE, the empty key value to use in the key update protocol as
specified in SHE – Secure Hardware Extension Functional Specification equals to 128 bits cleared to 0.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
108 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 109

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.1.6  Key handle
A key handle is a 32-bit integer that uniquely references a key within a key catalog. Whenever a key is being
used in a service, it is referenced via its key handle.
The key handle is defined by the C type hseKeyHandle_t.
The below table describes how the application must format the handle to reference a key.
Bit number
31 ~ 24
23 ~ 16
15 ~ 8
7 ~ 0
Description
0
Key catalog ID
Key group index
Key slot index
Table 44. Key handle format
In the above table:
• The key catalog ID is one of the enumerate as listed in Key catalogs
• The key group index corresponds to the order of the key group declaration where the key is to be found; the
first key group has the index 0
• The key slot index corresponds to the order of presence of the key within the target key group; the first key
slot has the index 0
The next table lists valid and invalid key handle values in view of an NVM and RAM key catalog configuration
provided hereafter. For the ROM key catalog, refer to ROM key catalog.
hseKeyGroupCfgEntry_t my_NVM_key_catalog[] = {
/* AES keys */
    {HSE_MU0_MASK, HSE_KEY_OWNER_CUST, HSE_KEY_TYPE_AES,        10,  128},
    {HSE_MU0_MASK, HSE_KEY_OWNER_CUST, HSE_KEY_TYPE_AES,        10,  256},
/* ECC keys */
    {HSE_MU0_MASK, HSE_KEY_OWNER_CUST, HSE_KEY_TYPE_ECC_PAIR,    2,  256},
    {HSE_MU0_MASK, HSE_KEY_OWNER_CUST, HSE_KEY_TYPE_ECC_PUB,     5,  256},
/* RSA keys */
    {HSE_MU0_MASK, HSE_KEY_OWNER_CUST, HSE_KEY_TYPE_RSA_PAIR,    2, 2048},
    {HSE_MU0_MASK, HSE_KEY_OWNER_CUST, HSE_KEY_TYPE_RSA_PUB,    10, 4096},
    {0, 0, 0, 0, 0}
};
hseKeyGroupCfgEntry_t my_RAM_key_catalog[] = {
/* ECC keys */
    {HSE_MU0_MASK, HSE_KEY_OWNER_ANY, HSE_KEY_TYPE_ECC_PUB,     5,  256},
/* AES keys */
    {HSE_MU0_MASK, HSE_KEY_OWNER_ANY, HSE_KEY_TYPE_AES,        10,  128},
    {HSE_MU0_MASK, HSE_KEY_OWNER_ANY, HSE_KEY_TYPE_AES,        10,  256},
    {0, 0, 0, 0, 0}
};
Key handle value
Description
0x00000000
The 256-bit AES device-dependent secret key in the ROM key catalog
0x00000100
The 256-bit AES device-dependent secret key in the ROM key catalog
0x00000109
Invalid key handle since there are only 2 key slots declared in the second group within the ROM
key catalog
0x00000500
Invalid key handle since there are only 3 groups (indexed 0 to 2) declared in the ROM key catalog
0x00010000
The first 128-bit AES key (first group) in the NVM key catalog
0x00010009
The last 128-bit AES key in the NVM key catalog
Table 45. Key handle examples
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
109 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 110

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Key handle value
Description
0x0001000A
Invalid key handle since there are only 10 128-bit AES keys (indexed 0 to 9) declared in the first
group
0x00010101
The second 256-bit AES key (second group) in the NVM key catalog
0x00010300
The first 256-bit ECC public key (fourth group) in the NVM key catalog
0x00010306
Invalid key handle since there are only 5 256-bit ECC public keys (indexed 0 to 4) declared in the
fourth group
0x00010509
The last 4096-bit RSA public key (sixth group) in the NVM key catalog
0x00010600
Invalid key handle since there are only 6 groups (indexed 0 to 5) declared in the NVM key catalog
0x00020100
The first 128-bit AES key (second group) in the RAM key catalog
0x00020209
The last 256-bit AES key (third group) in the RAM key catalog
0x00020400
Invalid key handle since there are only 3 groups (indexed 0 to 2) declared in the RAM key catalog
0x00050000
Invalid key handle since the key catalog ID specified is invalid
Table 45. Key handle examples...continued
The C macro GET_KEY_HANDLE(catalogId, groupIdx, slotIdx) is defined in the HSE firmware headers to
help the application format the key handle.
6.2  Key management
6.2.1  Scope
Key management services are available to the host to:
• Initialize and update key values and properties
• Export key values and properties
• Generate and derivate key values
• Establish secret keys in a secure manner
6.2.2  Key catalog formatting
All the services described in this section are available to the host once the key catalogs have been formatted.
See previous section on Key Catalog Formatting.
6.2.3  Key import
All cryptographic keys declared within the NVM and RAM key catalogs, except for the key type
HSE_KEY_TYPE_SHE, can be provisioned (that is, initialized and updated) by the host via a key import
service, defined by the structure hseImportKeySrv_t.
Important:
The key catalogs must have been formatted prior to provisioning the keys.
The host triggers one service request per key to provision. Once a key is successfully provisioned, it can be
used to secure subsequent key provisioning operations, as well as configuring SMR.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
110 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 111

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.2.3.1  Scheme
A key 
 can be imported by the host to the HSE in plain or encrypted with an encryption key 
. It can be
further authenticated using an authentication key 
.
Depending on its type, a key 
 has either a single value (a secret that can be shared) or a pair of values made
of a private key (a secret that is never shared) and a public key (not a secret).
The secret or private value of a key 
 is noted 
. The public key value of 
 is noted 
.
The properties of 
 (usage, access restrictions, and so on) are defined by the host and provided along with the
key values.
 is used to decrypt 
 when it is provided encrypted by the host. 
 (if any) is always provided in plain.
 is used to authenticate a container where 
 and 
 are stored among other information (if any).
6.2.3.2  Key selection
The handle to the imported key 
 is specified by the data field targetKeyHandle.
If the target key handle is in the NVM key catalog:
• It must reference a key slot that is either empty or set with a key for which the access restriction flag
HSE_KF_ACCESS_WRITE_PROT is not set
• If the target key slot is not empty, the authentication is not optional
• If the host is granted with Super User (SU) rights, the owner of the target key handle must match the host
identity (HID) (see Execution Rights (Super User vs. User))
• If the host has User rights, the owner of the target key handle must be HSE_KEY_OWNER_CUST if LC is
CUST_DEL, or HSE_KEY_OWNER_OEM if LC is OEM_PROD
The key handle to the authentication key 
 is specified by the data field keyContainer.authKeyHandle.
The key handle to the encryption key 
 is specified by the data field cipher.cipherKeyHandle. The owner
of both keys must be the same as the target key handle.
Data field
Value
Explanation
HSE_INVALID_KEY_HANDLE
The imported key is not authenticated
keyContainer.authKey
Handle
Any value different from HSE_
INVALID_KEY_HANDLE
A proof of authenticity is provided by the host
along with the imported key
HSE_INVALID_KEY_HANDLE
The secret part of the imported key 
 is
provided in plain
cipher.cipherKeyHandle
Any value different from HSE_
INVALID_KEY_HANDLE
The secret part of the imported key 
 is
encrypted
Table 46. Encryption and authentication key handles (key import/export services)
If the host has User rights, a key can only be imported based on the knowledge of another key (that is,
authenticated), and secret key parts are always provided encrypted.
The below tables indicate when the provisioning keys 
 and 
 must be provided.
Super User (SU) rights
User rights
Key Type (below) | Provisioning keys
(right)
Table 47. Key provisioning usage when importing a key in an empty slot in the NVM key catalog
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
111 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 112

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Super User (SU) rights
User rights
HSE_KEY_TYPE_AES
Optional
Always, if 
 is
used
Optional, if 
 is
not used
Always
Always
HSE_KEY_TYPE_SHE
Provisioning via SHE services only
HSE_KEY_TYPE_HMAC
Optional
Always, if 
 is
used
Optional, if 
 is
not used
Always
Always
HSE_KEY_TYPE_SHARED_SECRET
Key type not available in NVM key catalog
HSE_KEY_TYPE_RSA_PAIR
Optional
Always, if 
 is
used
Optional, if 
 is
not used
Always
Always
HSE_KEY_TYPE_ECC_PAIR
Optional
Always, if 
 is
used
Optional, if 
 is
not used
Always
Always
HSE_KEY_TYPE_DH_PAIR
Optional
Always, if 
 is
used
Optional, if 
 is
not used
Always
Always
HSE_KEY_TYPE_RSA_PUB
N/A
Optional
N/A
Always
HSE_KEY_TYPE_ECC_PUB
N/A
Optional
N/A
Always
HSE_KEY_TYPE_DH_PUB
N/A
Optional
N/A
Always
HSE_KEY_TYPE_RSA_PUB_EXT
N/A
Optional
N/A
Always
HSE_KEY_TYPE_ECC_PUB_EXT
N/A
Optional
N/A
Always
Table 47. Key provisioning usage when importing a key in an empty slot in the NVM key catalog...continued
Super User (SU) rights
User rights
Key Type (below) | Provisioning keys
(right)
HSE_KEY_TYPE_AES
Optional
Always
Always
Always
HSE_KEY_TYPE_SHE
Provisioning via SHE services only
HSE_KEY_TYPE_HMAC
Optional
Always
Always
Always
HSE_KEY_TYPE_SHARED_SECRET
Key type not available in NVM key catalog
HSE_KEY_TYPE_RSA_PAIR
Optional
Always
Always
Always
HSE_KEY_TYPE_ECC_PAIR
Optional
Always
Always
Always
HSE_KEY_TYPE_DH_PAIR
Optional
Always
Always
Always
HSE_KEY_TYPE_RSA_PUB
N/A
Always
N/A
Always
Table 48. Key provisioning usage when updating a key (non-empty slot) in the NVM Key Catalog
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
112 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 113

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Super User (SU) rights
User rights
HSE_KEY_TYPE_ECC_PUB
N/A
Always
N/A
Always
HSE_KEY_TYPE_DH_PUB
N/A
Always
N/A
Always
HSE_KEY_TYPE_RSA_PUB_EXT
N/A
Always
N/A
Always
HSE_KEY_TYPE_ECC_PUB_EXT
N/A
Always
N/A
Always
Table 48. Key provisioning usage when updating a key (non-empty slot) in the NVM Key Catalog...continued
Super User (SU) rights
User rights
Key Type (below) | Provisioning keys
(right)
HSE_KEY_TYPE_AES
Optional
Always, if 
 is
used
Optional, if 
 is
not used
Optional
Always, if 
 is used
Optional, if 
 is not
used
HSE_KEY_TYPE_SHE
Provisioning via SHE services only
HSE_KEY_TYPE_HMAC
Optional
Always, if 
 is
used
Optional, if 
 is
not used
Optional
Always, if 
 is used
Optional, if 
 is not
used
HSE_KEY_TYPE_SHARED_SECRET
Optional
Optional
Optional
Always, if 
 is used
Optional, if 
 is not
used
HSE_KEY_TYPE_RSA_PAIR
Key type not available in RAM key catalog
HSE_KEY_TYPE_ECC_PAIR
Optional
Always, if 
 is
used
Optional, if 
 is
not used
Always
Always
HSE_KEY_TYPE_DH_PAIR
Optional
Always, if 
 is
used
Optional, if 
 is
not used
Always
Always
HSE_KEY_TYPE_RSA_PUB
N/A
Optional
N/A
Always
HSE_KEY_TYPE_ECC_PUB
N/A
Optional
N/A
Always
HSE_KEY_TYPE_DH_PUB
N/A
Optional
N/A
Always
HSE_KEY_TYPE_RSA_PUB_EXT
N/A
Optional
N/A
Always
HSE_KEY_TYPE_ECC_PUB_EXT
N/A
Optional
N/A
Always
Table 49. Key provisioning usage when provisioning a key in the RAM Key Catalog
Note:  Although it is possible to import ECC and DH key pairs in the RAM key catalog, it is recommended to
only use the key generation service to provision these types of keys. ECC key pairs in the RAM key catalog can
be used for ECDHE (using ephemeral keys in a key agreement protocol).
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
113 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 114

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.2.3.3  Service configuration
The below table indicates what additional data fields must be provided when the imported key is provisioned in
an encrypted form.
Data field
Explanation
cipher.cipherScheme
The cipher scheme used to decrypt 
cipher.cipherKeyHandle
The key handle to 
, which must:
• Be declared in a key group owned by the same owner as the target key handle
• Refer to a non-empty key slot having its key usage flags HSE_KF_USAGE_
KEY_PROVISION and HSE_KF_USAGE_DECRYPT set
• Refer to a key type that matches with the ciphering scheme selected
Table 50. Parameters for an encrypted key import
The below table indicates what additional data fields must be provided when the imported key is provisioned
with a proof of authenticity.
Data field
Explanation
keyContainer.pKeyContainer
The pointer to the memory container that contains the imported key value(s) and
the key properties.
The memory location must be accessible by both the host and the HSE.
keyContainer.keyContainerLen
The byte size of the container.
keyContainer.authScheme
The authentication scheme used to authenticate the key container.
The proof of authenticity can be an authentication tag (i.e. a Message
Authentication Code (MAC)) or a public key signature scheme (that is, RSA or
ECC signature).
keyContainer.authKeyHandle
The key handle to 
, which must:
• Be declared in a key group owned by the same owner as the target key handle
• Refer to a non-empty key slot having its key usage flags HSE_KF_USAGE_
KEY_PROVISION and HSE_KF_USAGE_VERIFY set
• Refer to a key type that matches with the authentication scheme selected
keyContainer.pAuth[i]
The pointer(s) (i is 0 or 1) to the proof of authenticity, calculated over the key
container.
The memory location must be accessible by both the host and the HSE.
When the proof of authenticity is a RSA signature, pAuth[0] is the pointer to that
signature calculated over the key container and pAuth[1] is not used.
When the proof of authenticity is an ECC signature, pAuth[0] is the pointer to the
x coordinate of the verification point, and pAuth[1] is the pointer to the signature
calculated over the key container.
For more information on the MAC algorithms supported by the HSE, refer to Mac
Generation and Verification.
For more information on the signature algorithms supported by the HSE, refer to
Signature Generation and Verification RSA ECC.
keyContainer.authLen[i]
The byte size of the values pointed by pAuth[i] (i is 0 or 1).
Table 51. Parameters for an authenticated key import
The proof of authenticity provided along with the key container must be calculated over that container.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
114 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 115

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Remember:  The provisioning keys 
 and 
 can be declared in the NVM and RAM key catalogs and the key
usage flag HSE_KF_USAGE_KEY_PROVISION must be set. The RAM provisioning keys can be used only to
import RAM keys (cannot be used to import NVM keys).
6.2.3.4  Key properties
The imported key attributes defined in Key attributes must be provided with the pointer pKeyInfo as listed in
the below table.
Key attribute
Data field
Possible values
Key bit size
pKeyInfo➔keyBitLen
16-bit integer
Key Type
pKeyInfo➔keyType
Key type; see Key group and key type
Update counter
pKeyInfo➔keyCounter
32-bit integer For NVM keys, the key counter must
be between 0 and 0xFFFFFFFE (inclusive). For RAM
keys, the key counter is forced to 0xFFFFFFFF (not
used)
Exception: only 28-bits are used for SHE keys; for
SHE RAM keys, the counter is forced to zero
Access restriction flags
Usage flags
pKeyInfo➔keyFlags
Binary OR combination of HSE_KF_ACCESS_xxx
and HSE_KF_USAGE_xxx
SMR verification map
pKeyInfo➔smrFlags
Binary OR combination of HSE_KF_SMR_xxx
enumerates
Curve ID (ECC keys only)
pKeyInfo➔specific.eccCurve
Id
See Notes on ECC keys
Public exponent size (RSA
keys only)
pKeyInfo➔specific.pub
ExponentSize
The public exponent size in bytes; see Key values
AES Block Mode Mask (AES
keys only)
pKeyInfo➔aesBlockModeMask
Bit field to declare the block cipher modes that can
be used with the key. If it is cleared to 0, any AES
cipher mode can be used. See HSE Service API
Reference Manual.
Table 52. Key attribute mapping in pKeyInfo
The pointer pKeyInfo must reference a memory area that is accessible by both the host and the HSE.
When the key is imported in the NVM key catalog, and if the key slot is not empty, the update counter value
provided pKeyInfo➔keyCounter must be strictly above the counter value in the target key slot.
When the key is imported in the RAM key catalog, the update counter and the SMR verification map are cleared
to 0. In addition, its access restriction flags are set as follows:
• Write protection is cleared
• Debug protection is cleared
• Export capability is kept as defined by the host pKeyInfo➔keyFlags
Important:
When a secret (for example, an AES key or a key pair) is imported within an authenticated container,
pKeyInfo must be within that container. When the key import is using combined authentication and encryption
(for example, GCM), the key container is not used and pKeyInfo must point to a location within the memory
area referenced as the Additional Authentication Data pointed by pAAD.
The public key (PUB_EXT and PUB key) imported within an authenticated container (for example, X.509
certificate) can include the pKeyInfo inside or outside the key container.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
115 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 116

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Key usage flags in relation to key management (that is, key exchange, key derive, key provisioning) cannot be
defined for all imported keys. The below table lists the restrictions vs. the key type and key catalog.
Key usage flag (key management)
Imported key types
Key catalogs
HSE_KF_USAGE_EXCHANGE
HSE_KEY_TYPE_ECC_PAIR
HSE_KEY_TYPE_ECC_PUB
HSE_KEY_TYPE_ECC_PUB_EXT
HSE_KEY_TYPE_DH_PAIR
HSE_KEY_TYPE_DH_PUB
NVM and RAM key catalogs
HSE_KF_USAGE_DERIVE
HSE_KEY_TYPE_AES
HSE_KEY_TYPE_HMAC
NVM and RAM key catalogs
HSE_KF_USAGE_KEY_PROVISION
HSE_KEY_TYPE_AES
HSE_KEY_TYPE_HMAC
HSE_KEY_TYPE_RSA_PAIR
HSE_KEY_TYPE_RSA_PUB
HSE_KEY_TYPE_RSA_PUB_EXT
HSE_KEY_TYPE_ECC_PAIR
HSE_KEY_TYPE_ECC_PUB
HSE_KEY_TYPE_ECC_PUB_EXT
NVM and RAM key catalogs.
Note:  RAM provisioning
keys can be used only to
import RAM keys (cannot be
used to import NVM keys)
Table 53. Key usage flag restrictions for key import/export services
The below table provides key attribute setting examples depending on the specific key definition.
Key characteristics
Key attributes
RSA/ECC public key used to verify a signature over a key value
HSE_KF_USAGE_VERIFY |
HSE_KF_USAGE_KEY_PROVISION
AES key used to decrypt a key value that is being imported encrypted,
and used to encrypt key values that are exported
HSE_KF_USAGE_ENCRYPT |
HSE_KF_USAGE_DECRYPT |
HSE_KF_USAGE_KEY_PROVISION
DH/ECC key pair used in a Diffie-Hellmann key agreement
HSE_KF_USAGE_EXCHANGE
AES key used to generate and verify CMAC and to derive a shared
secret
HSE_KF_USAGE_SIGN |
HSE_KF_USAGE_VERIFY |
HSE_KF_USAGE_DERIVE
Table 54. Key attribute setting examples
6.2.3.5  Key values
The imported key values are provided via the array of pointers pKey[] as listed in the below table.
Key type
pKey[0]
pKey[1]
pKey[2]
HSE_KEY_TYPE_AES
unused
unused
Value of 
HSE_KEY_TYPE_SHE
Provisioning via SHE services only
HSE_KEY_TYPE_HMAC
unused
unused
Value of 
HSE_KEY_TYPE_SHARED_SECRET
unused
unused
Value of 
HSE_KEY_TYPE_RSA_PAIR
Value of 
Value of 
Value of 
Table 55. Pointer to provisioning key values vs. key type
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
116 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 117

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Key type
pKey[0]
pKey[1]
pKey[2]
HSE_KEY_TYPE_RSA_PUB
Value of 
Value of 
unused
HSE_KEY_TYPE_RSA_PUB_EXT
Value of 
Value of 
unused
HSE_KEY_TYPE_ECC_PAIR
Value of 
 [1]
unused
Value of 
HSE_KEY_TYPE_ECC_PUB
Value of 
[1]
unused
unused
HSE_KEY_TYPE_ECC_PUB_EXT
Value of 
[1]
unused
unused
HSE_KEY_TYPE_DH_PAIR
Value of 
Value of 
Value of 
HSE_KEY_TYPE_DH_PUB
Value of 
Value of 
unused
Table 55. Pointer to provisioning key values vs. key type...continued
[1]
The point coordinates are encoded depending on the curve type (see Notes on ecc keys)
The memory pointers pKey[] must reference memory areas that are accessible by both the host and the HSE.
The values pointed by pKey[0] and pKey[1] must always be provided in plain. The values pointed by
pKey[2] (
) can be provided either in plain or encrypted. The encryption is either optional or mandatory
depending on the user rights granted to the host (see below). “Unused” indicate that the data field is not
processed by the HSE.
When a key container is provided, it must be ensured that the key values pointed by pKey[] are within
the key container, that means (for i between 0 and 2) addresses pKey[i] and (pKey[i] + keyLen[i])
must be between keyContainer.pKeyContainer and (keyContainer.pKeyContainer +
keyContainer.keyContainerLen - 1).
RSA Public Key Container
Key Attributes
Value of n
Value of e
keyContainer.pkeyContainer
size:keyContainer.keyContainerLen
pKeyInfo
pKey[0]
Size:keyLen[0]
pKey[1]
Size:keyLen[1]
RSA Signature
keyContainer.pAuth[0]
Size:keyContainer.authLen[0]
Figure 60. Illustrating the use of a key container (provisioning an RSA public key)
The number of bytes to be read at the memory location pKey[i] must be provided in the field keyLen[i]
(with i between 0 and 2). When key values are provided in plain format, the number of bytes to read must align
with the key size settings. When key values are provided encrypted, the number of bytes to read depends on
the encryption scheme selected.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
117 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 118

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The imported key size information is provided in the data fields pointed by pKeyInfo as listed in the below
table.
Key type
Key size
information
Data field
Size unit
Size of 
Size of 
pKeyInfo➔keyBitLen
Bits
RSA keys
Size of 
pKeyInfo➔specific.pubExponentSize
Bytes
Size of 
 (see
below)
Size of 
 (see
below)
Size of 
pKeyInfo➔keyBitLen
Bits
ECC keys
EC curve of base
point 
pKeyInfo➔specific.eccCurveId [1]
N/A
Size of 
Size of 
DH keys
Size of 
pKeyInfo➔keyBitLen
Bits
AES/HMAC/Shared
Secret
Size of 
pKeyInfo➔keyBitLen
Bits
Table 56. Key size setting vs. key type
[1]
For more information, refer to Notes on ecc keys
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
118 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 119

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.2.3.5.1  Notes on ECC keys
For ECC keys, the value of the public point  corresponds to the encoding of its coordinates according to the
curve type to which it is associated.
Curve type
ECC key format
eccKeyFormat
Encoding of public point 
 (in
pKey[0])
keyLen[0]
HSE_KEY_FORMAT_ECC_PUB_
RAW
 || 
HSE_KEY_FORMAT_ECC_PUB_
UNCOMPRESSED
0x04 || 
 // 
2
Weierstrass
form
HSE_KEY_FORMAT_ECC_PUB_
COMPRESSED
0x02/0x03 || 
//
Montgomery
form
HSE_KEY_FORMAT_ECC_PUB_
RAW
||
Twisted
Edward
form
HSE_KEY_FORMAT_ECC_PUB_
RAW
 where 
msb (
, 1)
= Isb (
,1)
Table 57. Encoding of EC point coordinates
The Weierstrass public keys can be imported in three formats using the eccKeyFormat parameter:
• HSE_KEY_FORMAT_ECC_PUB_RAW - the raw format is the 
 coordinate concatenated with the 
coordinate.
• HSE_KEY_FORMAT_ECC_PUB_UNCOMPRESSED - the uncompressed format is a byte of 0x04, concatenated
with the 
 coordinate and 
 coordinates.
• HSE_KEY_FORMAT_ECC_PUB_COMPRESSED - the compressed format is a byte of 0x02 or 0x03, depending
on the less significant bit of 
, concatenated with the 
 coordinate:
–
, if the least significant bit of 
 is 0
–
, if the least significant bit of 
 is 1
The Montgomery and Twisted Edward public keys can be imported only in raw format.
The curve, on which the base point  lies, is given by an identifier via the data field
pKeyInfo➔specific.eccCurveId. A set of enumerates is available to the host for the curve identifier,
where the prefix indicates where the curve parameters are defined, as listed in the below table.
Curve ID prefix
Curve ID example
Curve parameter definition
HSE_EC_SEC
HSE_EC_SEC_SECP384R1
Standards for Efficient Cryptography 2
(SEC2)
HSE_EC_BRAINPOOL
HSE_EC_BRAINPOOL_BRAINPOOLP256R1
Elliptic Curve Cryptography (ECC) Brainpool
Standard Curves and Curve Generation
HSE_EC_25519
HSE_EC_25519_ED25519
Elliptic Curves for Security
HSE_EC_USER
HSE_EC_USER_CURVE1
User defined
Table 58. Elliptic curve identifiers and parameter definition
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
119 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 120

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The supported elliptic curve identifies are listed in the below table.
Curve ID
Description
HSE_EC_SEC_SECP256R1
SECP256R1 / NIST P-256 Weierstrass curve.
HSE_EC_SEC_SECP384R1
SECP384R1 / NIST P-384 Weierstrass curve.
HSE_EC_SEC_SECP521R1
SEC521R1 / NIST P-521 Weierstrass curve.
HSE_EC_BRAINPOOL_BRAINPOOLP256R1
Brainpool (Weierstrass curve).
HSE_EC_BRAINPOOL_BRAINPOOLP320R1
Brainpool (Weierstrass curve).
HSE_EC_BRAINPOOL_BRAINPOOLP384R1
Brainpool (Weierstrass curve).
HSE_EC_BRAINPOOL_BRAINPOOLP512R1
Brainpool (Weierstrass curve).
HSE_EC_25519_CURVE25519
Montgomery form (Curve25519). Usable only with the ECDH
key agreement protocol.
HSE_EC_25519_ED25519
Twisted Edward form; the curve that is birationally equivalent to
Curve25519. Usable only with the EdDSA signature algorithm
HSE_EC_USER_CURVE1(/CURVE2/CURVE3)
User-defined curves. Can be used only if the ECC domain
parameters were set before (see hseLoadEccCurveSrv_t)
Table 59. HSE ECC curves
For all curves, the private key is the secret scalar 
. For all curves except HSE_EC_25519_ED25519, the
public point  is calculated as follows:
 
For HSE_EC_25519_ED25519, the public point  is calculated as follows:
 
 
The 
 primitive for HSE_EC_25519_ED25519 is SHA512, which produces a digest of exactly two times
the size of 
.
The 
 function for HSE_EC_25519_ED25519 ensures that the secret scalar 
 is a multiple of 8 (the
last 3 LSB are cleared) and 2254 (the first MSB is cleared, and the second MSB is set) as follows:
  
Important:
The EdDSA standard (refer to Edwards-Curve Digital Signature Algorithm (EdDSA) and Elliptic Curves for
Security ) specifies that keys on the HSE_EC_25519_ED25519 curve are also processed by conversion to
little-endian bit strings. Montgomery curve keys on curve HSE_EC_25519_CURVE25519 are also represented
in little-endian (refer to Elliptic Curves for Security ).
However, the HSE expects such keys in the same format as any other ECC key: in big-endian format. In order
to import an EdDSA key in little-endian format into the HSE, it must first be swapped to big-endian on the host.
Furthermore, an EdDSA or Montgomery curve key is always exported by the HSE in big-endian format.
User-defined curve parameters can be initialized by the host via a dedicated key management utility, defined
by the structure hseLoadEccCurveSrv_t. The host must be granted with Super User (SU) rights to use this
service. The loaded user-defined curves are persistent.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
120 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 121

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The data field eccCurveId specifies the curve ID for which the curve parameters are defined. It is one of the
enumerates having a HSE_EC_USER prefix.
The following data fields specify the domain parameter of the Weierstrass curve:
• pA and pBare the pointers to parameters  and 
• pGis the pointer to the  and  coordinates of the generator point ; both coordinates are concatenated
together as follows: 
• pPis the pointer to the field of the curve 
• pNis the pointer to the order of 
The data field pBitLen specifies the size in bits of:
• The public point coordinates 
 and 
• The domain parameters , ,  and 
The data field nBitLen specifies the size in bits of ECC curve order pN (noted n) and private scalar 
.
Except for pN the byte size of each data arrays equals 
. The size of pN equals 
.
For pG, the byte size array is 
 (to properly encode each coordinate 
 and 
).
The below code snippet illustrates how the curve brainpoolP192r1 can be defined as the user-defined curve ID
HSE_EC_USER_CURVE1.
// curve brainpoolP192r1
const uint8_t a[]  = {0x6A, 0x91, 0x17, 0x40, 0x76, 0xB1, 0xE0, 0xE1, 0x9C, 0x39, 0xC0, 0x31,
                      0xFE, 0x86, 0x85, 0xC1, 0xCA, 0xE0, 0x40, 0xE5, 0xC6, 0x9A, 0x28, 0xEF};
const uint8_t b[]  = {0x46, 0x9A, 0x28, 0xEF, 0x7C, 0x28, 0xCC, 0xA3, 0xDC, 0x72, 0x1D, 0x04,
                      0x4F, 0x44, 0x96, 0xBC, 0xCA, 0x7E, 0xF4, 0x14, 0x6F, 0xBF, 0x25, 0xC9};
const uint8_t G[]  = {0xC0, 0xA0, 0x64, 0x7E, 0xAA, 0xB6, 0xA4, 0x87, 0x53, 0xB0, 0x33, 0xC5,
                      0x6C, 0xB0, 0xF0, 0x90, 0x0A, 0x2F, 0x5C, 0x48, 0x53, 0x37, 0x5F, 0xD6,
                      0x14, 0xB6, 0x90, 0x86, 0x6A, 0xBD, 0x5B, 0xB8, 0x8B, 0x5F, 0x48, 0x28,
                      0xC1, 0x49, 0x00, 0x02, 0xE6, 0x77, 0x3F, 0xA2, 0xFA, 0x29, 0x9B, 0x8F};
const uint8_t p[]  = {0xC3, 0x02, 0xF4, 0x1D, 0x93, 0x2A, 0x36, 0xCD, 0xA7, 0xA3, 0x46, 0x30,
                      0x93, 0xD1, 0x8D, 0xB7, 0x8F, 0xCE, 0x47, 0x6D, 0xE1, 0xA8, 0x62, 0x97};
const uint8_t n[]  = {0xC3, 0x02, 0xF4, 0x1D, 0x93, 0x2A, 0x36, 0xCD, 0xA7, 0xA3, 0x46, 0x2F,
                      0x9E, 0x9E, 0x91, 0x6B, 0x5B, 0xE8, 0xF1, 0x02, 0x9A, 0xC4, 0xAC, 0xC1};
…/…
 hseLoadEccCurveSrv_t defineMyCurve;
 defineMyCurve.eccCurveId = HSE_EC_USER_CURVE1;
 defineMyCurve. pbitLen  = 192;
 defineMyCurve. nbitLen  = 192;
 defineMyCurve.pA         = a;
 defineMyCurve.pB         = b;
 defineMyCurve.pG         = G;
 defineMyCurve.pP         = p;
 defineMyCurve.pN         = n;
6.2.3.6  Importing standard key certificates
A key container can be formatted according to a standard certificate format. The host only needs to provide the
pointers to the key values and container within the certificate. Those values can be retrieved by a certificate
parser (available on the host side).
For example, to import an RSA public key provided in the form of a RSA-signed X.509 certificate:
• keyContainer.pKeyContainer must point to the certificate field tbsCertificate (within Certificate)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
121 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 122

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• pKey[0] must point to the certificate field modulus (within subjectPublicKey)
• pKey[1] must point to the certificate field publicExponent (within subjectPublicKey)
• keyContainer.pAuth[0] must point to the certificate field signatureValue (within Certificate)
• pKeyInfo can point inside or outside the certificate (the signed key container). If the pKeyInfo points inside
the certificate, it must be defined as a custom certificate extension as specified by the version 3 of the X.509
certificate format; this extension must define the key properties as documented in Key Properties; this custom
field must match with the content of the certificate field keyUsage.
For more information on X.509 certificates, refer to Internet X.509 Public Key Infrastructure Certificate and
Certificate Revocation List (CRL) Profile.
In the same manner as above, key values stored in specific or standard key container (for example, different
types of certificates) can be imported into HSE.
6.2.3.7  Possible error causes
The key provisioning service can fail for one of the following reasons:
• The key catalogs have not been formatted
• The host is not the owner of the key slot (for example, key group owner declared as
HSE_KEY_OWNER_CUST but the host has OEM SU rights)
• The target key handle refers to an incorrect key type (HSE_KEY_TYPE_SHE)
• The target key handle refers to a non-empty key slot with the access restriction flag
HSE_KF_ACCESS_WRITE_PROT set
• The target key handle refers to a non-empty key slot with a counter value above the new counter value
provided in the input
• The key usage flags do not match with the key type and key catalog provided in the input
• The number of bytes to read from the pointers pKey[] do not match with the maximum size for the target key
slot
• The handle to 
 does not refer to a key having its usage flags HSE_KF_USAGE_KEY_PROVISION and
HSE_KF_USAGE_DECRYPT set
• The 
owner does not match with the target key owner
• The 
 type does not match with the ciphering scheme selected
• The handle to 
 does not refer to a key having its usage flags HSE_KF_USAGE_KEY_PROVISION and
HSE_KF_USAGE_VERIFY set
• The 
 owner does not match with the target key owner
• The 
 type does not match with the authentication scheme selected
•
 is provided in plain, while it must be encrypted (expecting an encryption key handle different from
HSE_INVALID_KEY_HANDLE)
•
 is provided without any proof of authenticity, while it should be authenticated (expecting an authentication
key handle different from HSE_INVALID_KEY_HANDLE)
• At least one of the imported key values is stored outside the key container provided in the input
• At least one of the memory pointers provided in input is referring to a memory area that is not accessible by
both the host and the HSE
6.2.4  Key export
The cryptographic keys declared within the NVM and RAM key catalogs can be exported (i.e. exposed)
with some restrictions (described in the sections below) via a key export service, defined by the structure
hseExportKeySrv_t.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
122 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 123

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.2.4.1  Scheme
A key 
 can be exported by the HSE to the host in plain or encrypted with an encryption key 
. It can be
further authenticated using an authentication key 
.
Depending on its type, a key 
 has either a single value (a secret that can be shared) or a pair of values made
of a private key (a secret that is never shared) and a public key (not a secret).
The secret or private value of a key 
 is noted 
. The public key value of 
 is noted 
.
The properties of 
 (usage, access restrictions, and so on) are returned by the HSE along with the key values.
 is used to encrypt 
 which is always provided encrypted to the host. 
 (if any) is always provided in
plain.
 is used to authenticate a container where 
 and 
 are stored among other information (if any).
6.2.4.2  Key selection
The key handle to the exported key 
 is specified by the data field targetKeyHandle.
The target key handle must reference a key slot set with a key for which the access restriction flag
HSE_KF_ACCESS_ EXPORTABLE is set.
Trying to export an empty key slot is not possible.
Exporting a key of type HSE_KEY_TYPE_SHE, HSE_KEY_TYPE_RSA_PUB_EXT,
HSE_KEY_TYPE_RSA_ECC_EXT or the private part of an RSA / ECC key is not possible.
The handle to the authentication key 
 is specified by the data field keyContainer.authKeyHandle. The
handle to the encryption key 
 is specified by the data field cipher.cipherKeyHandle.
The owner of both keys must be the same as the exported key handle (that is, all keys involved in the export
key service must belong to a key group having the same key owner).
Data field
Value
Explanation
HSE_INVALID_KEY_HANDLE
The exported key is not authenticated
keyContainer.authKey
Handle
Any value different from HSE_INVALID_
KEY_HANDLE
A proof of authenticity is provided by the
HSE along with the key value
HSE_INVALID_KEY_HANDLE
Invalid configuration when 
 is exported:
a valid key handle must always be provided
when exporting a secret.
cipher.cipherKeyHandle
Any value different from HSE_INVALID_
KEY_HANDLE
The secret part of the exported key 
 is
encrypted
Table 60. Key export settings (encrypted and authenticated key)
6.2.4.3  Service configuration
The below table indicates what additional data fields must be provided when a private key is exported.
Data field
Explanation
cipher.cipherScheme
The cipher scheme used to encrypt 
cipher.cipherKeyHandle
The key handle to 
, which must:
• Be declared in a key group owned by the same owner as the target key handle
Table 61. Parameters for an encrypted key export
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
123 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 124

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Data field
Explanation
• Refer to a non-empty key slot having its key usage flags HSE_KF_USAGE_
KEY_PROVISION and HSE_KF_USAGE_ENCRYPT set
• Refer to a key type that matches with the ciphering scheme selected
Table 61. Parameters for an encrypted key export...continued
The below table indicates what additional data fields must be provided when a key is exported with a proof of
authenticity.
Data field
Explanation
keyContainer.pKeyContainer
The pointer to the memory container that contains the key value(s)
The memory location must be accessible by both the host and the HSE
keyContainer.keyContainerLen
The byte size of the container
keyContainer.authScheme
The authentication scheme used to authenticate the key container
The proof of authenticity can be an authentication tag (that is, a Message
Authentication Code (MAC)) or a public key signature scheme (that is, RSA or
ECC signature)
keyContainer.authKeyHandle
The key handle to 
, which must:
• Be declared in a key group owned by the same owner as the target key handle
• Refer to a non-empty key slot having its key usage flags HSE_KF_USAGE_
KEY_PROVISION and HSE_KF_USAGE_SIGN set
• Refer to a key type that matches with the authentication scheme selected
keyContainer.pAuth[i]
The pointer(s) (i is 0 or 1) to buffers to receive the authenticity proof, calculated
over the key container
The memory location must be accessible by both the host and the HSE
When the proof of authenticity is an authentication tag, pAuth[0] is the pointer to
the MAC calculated over the key container
When the proof of authenticity is an RSA signature, pAuth[0] is the pointer to
that signature calculated over the key container
When the proof of authenticity is an ECC signature, pAuth[0] is the pointer to the
x-coordinate of the verification point, and pAuth[1] is the pointer to the signature
calculated over the key container
For more information on the MAC algorithms supported by the HSE, refer to
Streaming vs one-pass mode
For more information on the signature algorithms supported by the HSE, refer to
Signature generation and verification rsa ecc
keyContainer.pAuthLen[i]
The pointer(s) to 16-bit words indicating the size of the pAuth[i] buffers (i is 0 or
1)
The memory locations must be accessible by both the host and the HSE
The maximum byte size of the value pointed by pAuth[i] (i is 0 or 1) must be
provided in *keyContainer.pAuthLen[i]; in output, the host retrieves in *key
Container.pAuthLen[i] the number of bytes that have been written by the
HSE in pAuth[i]
Table 62. Parameters for an authenticated key export
The proof of authenticity is calculated by the HSE over the entire key container.
Remember:
The provisioning keys 
 and 
 can be declared in the NVM or RAM key catalog and the key usage flag
HSE_KF_USAGE_KEY_PROVISION must be set. The RAM provisioning keys can be used only to export RAM
keys (cannot be used to export NVM keys).
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
124 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 125

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.2.4.4  Key properties
When a memory address accessible by both the host and the HSE is set in pKeyInfo, the HSE returns at this
memory location the key attributes as listed in Key properties, and the key size as listed in Key values.
6.2.4.5  Key values
Key values are exported outside the HSE and saved at memory locations provided via the pKey[] data fields,
as listed in the below table.
Key type
pKey[0]
pKey[1]
pKey[2]
HSE_KEY_TYPE_AES
unused
unused
Value of 
HSE_KEY_TYPE_SHE
RAM key export via SHE services only
HSE_KEY_TYPE_HMAC
unused
unused
Value of 
HSE_KEY_TYPE_SHARED_SECRET
unused
unused
Value of 
HSE_KEY_TYPE_RSA_PAIR
Value of 
Value of 
unused
HSE_KEY_TYPE_RSA_PUB
Value of 
Value of 
unused
HSE_KEY_TYPE_RSA_PUB_EXT
Export not supported
HSE_KEY_TYPE_ECC_PAIR
Value of 
[1][1]
unused
unused
HSE_KEY_TYPE_ECC_PUB
Value of 
[1]
unused
unused
HSE_KEY_TYPE_ECC_PUB_EXT
Export not supported
HSE_KEY_TYPE_DH_PAIR
Value of 
Value of 
unused
HSE_KEY_TYPE_DH_PUB
Value of 
Value of 
unused
Table 63. Pointer to exported key values vs. key type
[1]
The point coordinates are encoded depending on the curve type (see Notes on ECC keys ).
The Weierstrass public keys can be exported in three formats (raw, uncompressed and compressed) providing
the eccKeyFormat parameter as specified in Notes on ECC keys. The Montgomery and Twisted Edward
public keys can be exported only in raw format.
The memory pointers pKey[] must reference memory areas that are accessible by both the host and the HSE.
The values pointed by pKey[0] and pKey[1] are always exported in plain. The values pointed by pKey[2]
(
) are always exported encrypted. “Unused” indicate that the data field is not used (that is, written) by the
HSE.
When a key container is defined by the host, it must be ensured that the key values pointed by pKey[]
are within the key container, that means (for i between 0 and 2) addresses pKey[i] and (pKey[i] +
*pKeyLen[i]) must be between keyContainer.pKeyContainer and (keyContainer.pKeyContainer
+ keyContainer.keyContainerLen - 1).
The number of bytes written by the HSE and to be read at each memory location pKey[i] is provided by the
pointer pKeyLen[i] (with i between 0 and 2).
The pointer pKeyLen[i] must be initialized with a RAM address of a 16-bit word that is accessible by both the
host and the HSE; in input, the host must set *pKeyLen[i] with the maximum number of bytes that can be
written at memory location pKey[i]; in output, the host retrieves in *pKeyLen[i] the number of bytes that
have been written by the HSE at memory location pKey[i].
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
125 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 126

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.2.4.6  Certificate signing request
The HSE can fill in a certificate signing request (CSR) that is pre-formatted by the host. The host just needs to
provide the pointers to the key values that must be located within the CSR.
For example, to export an ECC public key within a RSA-signed CSR as specified in PKCS#10:
• keyContainer.pKeyContainer must point to the CSR field certificationRequestInfo (within
CertificationRequest)
• pKey[0] must point to the CSR field subjectPublicKey (within subjectPKInfo)
• pKey[1] is not used
• keyContainer.pAuth[0] must point to the certificate field signature (within CertificationRequest)
For more information on CSR, refer to the PKCS #10: Certification Request Syntax Specification Version 1.7.
CertificationRequestInfo
subjectPublicKey
(value of public point Q)
keyContainer.pkeyContainer
size:keyContainer.keyContainerLen
pKey[0]
Size:keyLen[0]
Signature
keyContainer.pAuth[0]
Size:keyContainer.authLen[0]
Figure 61. Illustrating the use of a key container (exporting an ECC key in a CSR)
6.2.4.7  Possible error causes
The key export service can fail for one of the following reasons:
• he target key handle refers to an empty key slot
• The host is not the owner of the key slot (e.g. key group owner declared as HSE_KEY_OWNER_CUST but
the host has OEM SU rights)
• The target key handle refers to an incorrect key type (HSE_KEY_TYPE_SHE,
HSE_KEY_TYPE_RSA_PUB_EXT or HSE_KEY_TYPE_ECC_PUB_EXT)
• The target key handle refers to a non-empty key slot with the access restriction flag
HSE_KF_ACCESS_EXPORTABLE not set
• At least one of the maximum buffer sizes provided in *pKeyLen[] does not match with the size of the key
value to be returned
• At least one of the maximum buffer sizes provided in *pAuthLen[] does not match with the buffer size of the
authenticity proof to be returned
• The handle to 
 does not refer to a key having its usage flags HSE_KF_USAGE_KEY_PROVISION and
HSE_KF_USAGE_ENCRYPT set
• The 
 owner does not match with the target key owner
• The 
 type does not match with the ciphering scheme selected
• The key handle to 
 does not refer to a key having its usage flags HSE_KF_USAGE_KEY_PROVISION and
HSE_KF_USAGE_SIGN set
• The 
 owner does not match with the target key owner
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
126 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 127

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• The 
 type does not match with the authentication scheme selected
• At least one of the memory pointers provided in input is referring to a memory area that is not accessible by
both the host and the HSE
6.2.5  Key generation
Key generation within the HSE is handled via a service defined by the structure hseKeyGenerateSrv_t.
6.2.5.1  Algorithms
A key 
 can be generated by the HSE.
6.2.5.1.1  Symmetric keys
The generation of secret that can be an AES or HMAC key consists in:
• Choosing a key size, that aligns with the key type.
• Drawing a random  of selected size
The symmetric key is that random .
6.2.5.1.2  RSA key pairs
The generation of a RSA key pair consists in:
• Choosing a public exponent  and a modulus size
• Searching for two random primes  and , each with a size equal to half of the size of the resulting modulus
• Calculating the modulus 
• Calculating the private exponent  as 
, with 
The private RSA key is the pair (
). The public RSA key is the pair (
).
6.2.5.1.3  ECC key pairs
The generation of an ECC key pair consists in:
• Choosing a curve  on 
 of generator point , where  is the order of  (
 and  is prime)
• Drawing a random 
 such as 
• On a Weierstrass or Montgomery curve: calculating the public point 
• On a Twisted Edward curve: calculating the public point 
 ; for details, refer to the Notes on
ECC keys.
• Verifying that  is on the curve (i.e.
 and 
 and 
 and 
 verifies the equation given by )
The private ECC key is the random scalar 
. The public ECC key is the public point .
6.2.5.1.4  DH key pairs
The generation of a DH key pair consists in:
• Choosing a prime modulus  and  a primitive root modulus 
• Drawing a random  such as 
• Calculates 
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
127 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 128

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The private DH key is the triplet (
. The public DH key is the triplet (
).
6.2.5.1.5  Pre-master Secret for TLS1.2 RSA Key Exchange
The pre-master secret for TLS1.2 RSA key exchange can be computed in a shared-secret slot as specified
by rfc5246 (TLS1.2) or rfc4279 (RSA_PSK). It is computed using the ProtocolVersion (2 bytes specifying the
version for TLS1.2 or DTLS1.2) concatenated with a 46-byte random number.
To encrypt and authenticate the generated pre-master secret, the key export service (with the proper RSA
scheme) must be used. The encrypted and authenticated pre-master secret is sent to the peer node.
To decrypt and authenticate an encrypted pre-master secret (received from the peer node), the import
service must be used. The destination key slot must be an HSE_KEY_TYPE_SHARED_SECRET (with
HSE_KF_USAGE_DERIVE key flag set) that further can be used to derive the TLS 1.2 keys.
For more details, refer to hseKeyGenTls12RsaPreMaster_t scheme from HSE Service API Reference
Manual.
6.2.5.2  Key selection
The generated key 
 is provided by a key handle in the data field targetKeyHandle.
The target key type can be:
• HSE_KEY_TYPE_AES
• HSE_KEY_TYPE_HMAC
• HSE_KEY_TYPE_RSA_PAIR (only in the NVM key catalog)
• HSE_KEY_TYPE_ECC_PAIR
• HSE_KEY_TYPE_DH_PAIR
• HSE_KEY_TYPE_SHARED_SECRET (only in the RAM key catalog)
When the target key handle is within the NVM key catalog, it must reference an empty key slot. When the target
key handle is within the RAM key catalog, the key slot (empty or not) is replaced with the generated key.
If 
 is generated within the NVM key catalog, the host must be granted with Super User (SU) rights, and the
owner of 
 must match the host identity (HID). See Execution Rights (Super User vs. User)).
There are no restrictions when 
 is generated within the RAM key catalog.
6.2.5.3  Key properties
The key attributes of the key to generate must be provided via the data field keyInfo as listed in Key
properties.
An internally generated key can be updated via the key import service unless its write protection property is
set.
6.2.5.4  Service configuration
When generating an AES, HMAC or shared secret key, the size of  is given by the data field
keyInfo.keyBitLen. The key size must match the key type and key slot definition.
Upon successful key generation, the value  is saved in the target key slot.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
128 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 129

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Code snippet example for an AES key generation.
                // generate a 128-bit AES key
                hseSrvDescriptor_t*    pHseSrvDesc;
                hseKeyGenerateSrv_t*   pGenAESkey;
                hseSrvResponse_t        srvResp;
                // allocate the memory for the service descriptor in HSE/host interface RAM (not
 described here)
                pHseSrvDesc = myAllocMem(sizeof(hseKeyGenerateSrv_t));
                pHseSrvDesc->srvId = HSE_SRV_ID_KEY_GENERATE;
                pGenAESkey = &(pHseSrvDesc->hseSrv.keyGenReq);
                // intialize the service descriptor
                pGenAESkey->targetKeyHandle = GET_KEY_HANDLE(HSE_KEY_CATALOG_ID_NVM, 4, 10); // key
 slot 10 in group 4
                pGenAESkey->keyInfo.keyBitLen  = 128;
                pGenAESkey->keyInfo.keyFlags   = HSE_KF_USAGE_ENCRYPT|HSE_KF_USAGE_VERIFY|
HSE_KF_USAGE_KEY_PROVISION;
                pGenAESkey->keyInfo.smrFlags   = 0;
                pGenAESkey->keyInfo.keyCounter = 1;
                pGenAESkey->keyInfo.specific.aesBlockModeMask = 0; //any AES block mode             
   
                pGenAESkey->keyGenScheme = HSE_KEY_GEN_SYM_RANDOM_KEY;
                // run the service
                srvResp = runSrv(pHseSrvDesc);
        
When generating an RSA key pair:
• The size of the modulus  is provided in the data field keyInfo.keyBitLen
– The modulus size must always be an even value
– The size of  and  are half of that size
– Depending on the size of the primes to find, this operation can take several seconds to complete
– Also, this operation may not complete and terminate with an error, after the HSE has drawn several numbers
that are not passing the primality tests
• The public exponent  is provided via the pointer sch.rsaKey.pPubExp
– The size of this byte array must be provided in sch.rsaKey.pubExpLength
Upon successful key generation, the values ,  and  are saved in the target key slot.
In addition, the modulus  can be exported back to the host via the pointer sch.rsaKey.pModulus (if not
NULL); the host must allocate enough memory for the HSE to write the modulus value (at least the size of the
key).
Code snippet example for an RSA key pair generation.
 
// generate a 2048-bit RSA key pair
// get the modulus value back
const uint8_t e[] = {0x01, 0x00, 0x01}; // the public exponent (65537)
uint8_t n[2048/8]; // the modulus value returned after the generation
hseSrvDescriptor_t* pHseSrvDesc;
hseKeyGenerateSrv_t* pGenRSAkey;
/* allocate the memory for the service descriptor in
HSE/host interface RAM (not described here) */
hseSrvResponse_t srvResp;
pHseSrvDesc = myAllocMem(sizeof(hseKeyGenerateSrv_t));
pHseSrvDesc->srvId = HSE_SRV_ID_KEY_GENERATE;
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
129 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 130

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
pGenRSAkey = &(pHseSrvDesc->hseSrv.keyGenReq);
/* intialize the service descriptor */
genRSAkey.targetKeyHandle = GET_KEY_HANDLE(HSE_KEY_CATALOG_ID_NVM, 2, 0); // key slot 0 in group 2
pGenRSAkey->keyInfo.keyBitLen = 2048;
pGenRSAkey->keyInfo.keyFlags = HSE_KF_USAGE_SIGN | HSE_KF_USAGE_VERIFY;
pGenRSAkey->keyInfo.smrFlags = 0;
pGenRSAkey->keyInfo.keyCounter = 1;
pGenRSAkey->keyGenScheme = HSE_KEY_GEN_RSA_KEY_PAIR;
pGenRSAkey->sch.rsaKey.pPubExp = e;
pGenRSAkey->sch.rsaKey.pubExpLength = sizeof(e);
pGenRSAkey->sch.rsaKey.pModulus = n;
/* run the service */
srvResp = runSrv(pHseSrvDesc);
When generating an ECC key pair:
• The curve  is identified by the data field keyInfo.specific.eccCurveId
– The generator point , the order of  and the field of  are defined by the curve parameters
• The size of 
 is provided in keyInfo.keyBitLen
Upon successful key generation, the values 
 and  are saved in the target key slot.
In addition, the public point  can be exported back to the host via the pointer sch.eccKey.pPubKey (if not
NULL); the point coordinates are concatenated together as follows: 
; the host must allocate enough
memory for the HSE to write the point coordinates (at least two times the size of the key).
Code snippet example for an ECC key pair generation.
 /* generate a 256-bit ECC key pair on curve brainpoolp256r1
    get the public point back */
 uint8_t Q[2*256/8]; // the public point returned after the generation
 hseSrvDescriptor_t*    pHseSrvDesc;
 hseKeyGenerateSrv_t*   pGenECCkey;
 hseSrvResponse_t       srvResp;
 /* allocate the memory for the service descriptor in 
 HSE/host interface RAM (not described here) */
 pHseSrvDesc = myAllocMem(sizeof(hseKeyGenerateSrv_t));
 pHseSrvDesc->srvId = HSE_SRV_ID_KEY_GENERATE;
 pGenECCkey = &(pHseSrvDesc->hseSrv.keyGenReq);
 /* intialize the service descriptor */
 pGenECCkey->targetKeyHandle = GET_KEY_HANDLE(HSE_KEY_CATALOG_ID_NVM, 3, 5);  // key slot 5 in group
 3
 pGenECCkey->keyInfo.keyBitLen  = 256;
 pGenECCkey->keyInfo.keyFlags   = HSE_KF_USAGE_SIGN | HSE_KF_USAGE_VERIFY;
 pGenECCkey->keyInfo.smrFlags   = 0;
 pGenECCkey->keyInfo.keyCounter = 1;
 pGenECCkey->keyGenScheme = HSE_KEY_GEN_ECC_KEY_PAIR;
 pGenECCkey->keyInfo.specific.eccCurveId = HSE_EC_BRAINPOOL_BRAINPOOLP256R1;
 pGenECCkey->sch.eccKey.pPubKey = Q;
 /* run the service */
 srvResp = runSrv(pHseSrvDesc);
When generating a DH key pair:
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
130 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 131

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• The prime modulus  is provided via the pointer sch.classicDhKey.pModulus
– The size of this byte array must be provided in sch.classicDhKey.modulusLength
• The primitive root  is provided via the pointer sch.classicDhKey.pBaseG
• The size of this byte array must be provided in sch.classicDhKey.baseGLength
Upon successful key generation, the values 
,  and  are saved in the target key slot.
In addition, 
 can be exported back to the host via the pointer sch.classicDhKey.pPubKey (if not NULL);
the host must allocate enough memory for the HSE to write the temporary secret (at least the size of the key).
6.2.6  Key derivation
Keys can be derived from provisioned secrets within the HSE and without transferring to application RAM, via
key derivation and key copy services which enforce strict confidentiality over the derived secrets.
Key derivation within the HSE is handled via a service defined by the structure hseKeyDeriveSrv_t.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
131 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 132

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.2.6.1  Key transform algorithms (KDF)
The key derivation service applies a transform to a source secret key and outputs the result in a target secret
key as illustrated in the below figure.
Transform
secret key
(source)
shared secret 
(target)
HSE_KEY_TYPE_SHARED_SECRET
(not exportable)
HSE_KEY_TYPE_AES
HSE_KEY_TYPE_HMAC
HSE_KEY_TYPE_SHARED_SECRET
seed / salt
counter
transform key
transform key
Figure 62. Illustrating key derivation within the HSE
The HSE supports several standard transform algorithms:
• NIST KDF specified in Recommendation for Key-Derivation Methods in Key-Establishment Schemes and
Recommendation for Key Derivation Using Pseudorandom Functions (Revised)
• PKCS password-based KDF specified in PKCS #5: Password-Based Cryptography Specification Version 2.
• HMAC-based KDF specified in HMAC-based Extract-and-Expand Key Derivation Function (HKDF)
• The Transport Layer Security (TLS) V1.2 PRF specified in The Transport Layer Security (TLS) Protocol
Version 1.2
• ANSI X9.63 KDF specified in Standards for Efficient Cryptography 1 (SEC1)
• ISO KDF specified in Information technology - Security techniques - Encryption algorithms - Part 2:
Asymmetric ciphers
In addition, it supports one NXP proprietary algorithms (refer to HSE_KDF_ALGO_NXP_GENERIC from) HSE
Service API Reference Manual).
HSE KDF Algorithm ID
Description
HSE_KDF_ALGO_NXP_GENERIC
NXP Generic Key Derivation Function (KDF).
Computes a SHA2 over a source key and a seed. If the
requested key material is larger than the SHA or HMAC
output, the HSE expands it by performing more iterations.
This KDF also includes an option to export on the host side
maximum 8 bytes if the generated key material is greater
than or equal to 32 bytes. For more details, refer to the HSE
Service API Reference Manual.
HSE_KDF_ALGO_SP800_56C_ONE_STEP
One-step KDF as defined by Recommendation for Key-
Derivation Methods in Key-Establishment Schemes
HMAC and XCBC_MAC option as PRF algorithm is not
supported
HSE_KDF_ALGO_SP800_56C_TWO_STEP
Two-step KDF as defined by Recommendation for Key-
Derivation Methods in Key-Establishment Schemes.
Table 64. HSE KDF Algorithms
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
132 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 133

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
HSE KDF Algorithm ID
Description
HMAC and XCBC_MAC option as PRF algorithm is not
supported
HSE_KDF_ALGO_SP800_108
KDF as defined by Recommendation for Key Derivation
Using Pseudorandom Functions (Revised). Only Counter
mode is supported.
HSE_KDF_ALGO_PBKDF2HMAC
PBKDF2HMAC as defined by PKCS #5: Password-Based
Cryptography Specification Version 2.
Support of HMAC with Hash scheme SHA1, SHA224, and
SHA 256 is supported
HSE_KDF_ALGO_HKDF_EXPAND
HKDF Expand KDFs as defined by HMAC-based Extract-
and-Expand Key Derivation Function (HKDF).
Support of HMAC with Hash scheme SHA1, SHA224, and
SHA 256 is supported
HSE_KDF_ALGO_ANS_X963
KDF as defined by Standards for Efficient Cryptography 1
(SEC1)
HMAC and XCBC_MAC option as PRF algorithm is not
supported
HSE_KDF_ALGO_ISO18033_KDF1
KDF1 as defined by Information technology - Security
techniques - Encryption algorithms - Part 2: Asymmetric
ciphers
HMAC and XCBC_MAC option as PRF algorithm is not
supported
HSE_KDF_ALGO_ISO18033_KDF2
KDF2 as defined by Information technology - Security
techniques - Encryption algorithms - Part 2: Asymmetric
ciphers
HMAC and XCBC_MAC option as PRF algorithm is not
supported
HSE_KDF_ALGO_TLS12PRF
TLS 1.2 PRF as defined by The Transport Layer Security
(TLS) Protocol Version 1.2
Support of HMAC with Hash scheme SHA1, SHA224, and
SHA 256 is supported
HSE_KDF_ALGO_IKEV2
KDF IKEv2 as defined by Internet Key Exchange (IKEv2)
Protocol
Table 64. HSE KDF Algorithms...continued
Note:
Depending on the firmware variant and software package (that is, Standard or Premium package), some KDFs
may be disabled (see the macros available in the HSE header files).
Many KDFs use the Miyaguchi-Preneel compression function. It is important to note that the use of this function
is not limited to SHE keys.
The transform algorithm is specified via the data field kdfAlgo. The algorithm-specific parameters (salt, seed,
initial vectors, additional transform keys, and so on) are specified within dedicated structures as described in
HSE Service API Reference Manual.
6.2.6.2  Key selection
The source secret key is defined by the key handle srcKeyHandle.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
133 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 134

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The source of the key derivation can be any secret key of types AES or HMAC within the NVM or RAM
key catalog and having its usage flag HSE_KF_USAGE_DERIVE set. It can also be a shared secret
(HSE_KEY_TYPE_SHARED_SECRET).
The target key defined by the key handle targetKeyHandle must reference a key slot in the RAM key catalog
with the key type HSE_KEY_TYPE_SHARED_SECRET.
A key of the type HSE_KEY_TYPE_SHARED_SECRET can only be used in the key derivation service and
cannot be exported outside the HSE.
6.2.6.3  Resulting key
The key derivation function generates in a key material that can contain one or more keys.
The key(s) can be copied to an NVM or RAM key slot via the key copy service defined by the structure
hseKeyDeriveCopyKeySrv_t as illustrated in the below figure.
Figure 63. Illustrating key copy within the HSE
The data field keyHandle defines the source shared secret and must reference a RAM key of type
HSE_KEY_TYPE_SHARED_SECRET.
The data field targetKeyHandle defines the target secret and can reference a AES or HMAC key. The key
catalog for this key can be:
• The NVM key catalog only if the host is granted with SU rights; in addition, the target key slot must be empty
• The RAM key catalog; in this case, the key slot may not be empty
The copy operation consists in copying a number of bits defined by the data field keyInfo.keyBitLen from
the source key value at the offset defined by the data field startOffset (offset 0 means the first byte of the
source key is copied as the first byte of the target key). The startOffset can be zero or a multiple of 4 bytes.
The target key attributes are defined via the data field keyInfo.
6.2.7  Key agreement (Diffie-Hellman shared-secret computation)
Key agreement within the HSE is handled via a service defined by the structure
hseDHComputeSharedSecretSrv_t.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
134 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 135

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.2.7.1  Algorithms
The key agreement algorithms consist of securely establishing a secret between two parties  (for example, the
HSE) and  (for example, the host communicating with an external entity).
A secret  is computed based on the knowledge of a private key 
 owned by the party  and a public
key 
. The same secret can be computed based on the knowledge of the public key 
 associated
with 
 and the private key 
 owned by the party  and associated with 
. Doing so, the secret is
securely established even in a non-secure environment, since only public keys are exchanged between  and
.
6.2.7.1.1  DH key agreement
From ’s perspective, the DH key agreement protocol consists of:
• Choosing a prime modulus  and its primitive root  as the base of the agreement
• Knowing the private key 
 which is a private exponent 
• Knowing the public key 
 which is 
• Knowing the public key 
 which is 
 where  is the private exponent with  (
)
• Calculating 
From ’s perspective, the DH key agreement protocol consists of:
• Knowing  and  chosen by  (the base of the agreement)
• Knowing the private key 
• Knowing the public key 
• Knowing the public key 
• Calculating 
 is the shared secret since 
.
6.2.7.1.2  ECDH key agreement
From ’s perspective, the ECDH key agreement protocol consists in:
• Choosing an elliptic curve  of generator point 
• Knowing the private key 
 which is a private scalar 
• Knowing the public key 
 which is 
• Knowing the public key 
 which is 
 where 
 is the private scalar with  (
)
• Calculating 
From ’s perspective, the ECDH key agreement protocol consists in:
• Knowing the elliptic curve  chosen by 
• Knowing the private key 
• Knowing the public key 
• Knowing the public key 
• Calculating 
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
135 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 136

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
 is the shared secret (that is, point) since 
.
In practice, the shared secret is only the coordinate 
 (the coordinate 
 is discarded by the HSE).
6.2.7.2  Key selection
The shared secret  is calculated in the HSE and stored in a key slot defined by the key handle
targetKeyHandle.
The target key handle must reference a key slot in the RAM key catalog with the key type
HSE_KEY_TYPE_SHARED_SECRET.
The private key (
 or 
) is specified by the key handle privKeyHandle.
The public key (
 or 
) is specified by the key handle peerPubKeyHandle.
6.2.7.3  Service configuration
For a DH key agreement, the parameters  is defined via the key handle privKeyHandle.
For an ECDH key agreement, the elliptic curve  and the associated parameters are defined via the key handle
privKeyHandle.
6.2.7.4  Key properties
The properties of the shared secret  are defined as listed in the below table.
Key attribute
Value
Bit size
Defined by the private key handle
Update counter
0
Access restriction flags
None
Usage flags
HSE_KF_USAGE_DERIVE
MU instance map
As defined by the target key group
SMR verification map
0
Table 65. Properties of a shared secret (key agreement protocol)
6.2.7.5  Key values
Upon successful key agreement, the target key slot that defines the share secret  is initialized with either:
• The result of the modular exponentiation of the public key with the private exponent, or
• The result of the public point multiplied by the private scalar
6.2.8  Key erase
NVM and RAM key slots can be deleted by the host via a service defined by the structure
hseEraseKeysSrv_t.
6.2.8.1  Conditions
Keys in the RAM key catalog can be erased unconditionally.
Keys in the NVM key catalog can be erased only if the host is granted with Super User (SU) rights.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
136 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 137

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Keys can be erased only if their MU instance map includes the MU instance from which the key erase service is
issued.
6.2.8.2  Erasing one key
To erase one key, the data field keyHandle is set with the handle of the key to erase.
The owner of the deleted key (i.e. of the key group where the key belongs) must match the host identity (HID)
which is granted with SU rights (see section Execution Rights (Super User vs. User)).
The target key must not be write-protected: the access restriction flag HSE_KF_ACCESS_WRITE_PROT must
not be set.
6.2.8.3  Erasing all keys
To erase all keys of a certain type, the data field keyHandle is set with HSE_INVALID_KEY_HANDLE, and the
data field eraseKeyOptions is set with one of the enumerate listed in the below table to indicate what keys
are erased.
Only the keys for which the key group owner match the host identity (HID) are erased (see section Execution
Rights (Super User vs. User)).
Examples:
• In LC state OEM_PROD (and OEM_START_AS_USER is 0), the host (identified as OEM) which has SU
rights can only erase all NVM keys having their key group owner set to HSE_KEY_OWNER_OEM and
HSE_KEY_OWNER_ANY
• In LC state IN_FIELD, when the host gets granted with SU rights using a key owned by CUST, it
can only erase all NVM keys having their key group owner set to HSE_KEY_OWNER_CUST and
HSE_KEY_OWNER_ANY
Important:  When erasing multiple keys, the access restriction flag HSE_KF_ACCESS_WRITE_PROT has no
effect: write-protected keys are also erased.
Option
Description
HSE_ERASE_ALL_RAM_KEYS_ON_MU_IF
Erase all RAM keys
HSE_ERASE_ALL_NVM_KEYS_ON_MU_IF
Erase all NVM keys
HSE_ERASE_ALL_NVM_SYM_KEYS_ON_MU_IF
Erase all NVM secrets slots.
Exception: HSE_KEY_TYPE_SHE key slots are erased
only if the host is granted SU rights with the MASTER_
ECU_KEY and if there is no write-protected SHE key.
HSE_ERASE_ALL_NVM_ASYM_KEYS_ON_MU_IF
Erase all NVM public keys or public/private keys slots.
HSE_ERASE_KEYGROUP_ON_MU_IF
Erase all keys assigned to the key group.
Table 66. Erasing multiple keys
Important:
Erasing SHE keys in LC states CUST_DEL or OEM_PROD is always possible if the host is granted SU rights
after reset (that is, CUST_START_AS_USER or OEM_START_AS_USER is 0). In LC state IN_FIELD, erasing
SHE keys is only possible if the host is granted SU rights using the MASTER_ECU_KEY.
When the SHE keys are erased, the BOOT_MAC is also erased.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
137 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 138

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.2.9  Retrieving key properties
The key properties listed Key properties can be retrieved using the hseGetKeyInfoSrv_t service. The host
providers the keyHandle for the key and the pKeyInfo address where the key properties must be stored. This
service cannot be used with HSE_KEY_TYPE_SHE key type. For more details, refer to the HSE Service API
Reference Manual.
6.2.10  Key value verification
The symmetric and asymmetric key values stored inside HSE can be verified using the hseKeyVerifySrv_t
service. This service verifies a CMAC tag or a digest (SHA256/384/512) over a secret stored inside HSE.
The host providers the keyHandle for the secret and the pTag address where the CMAC tag or the digest is
located. If a CMAC tag is provided, the host also provides the key handle for the CMAC operation.
When the service is received, the HSE firmware verifies the CMAC tag or digest using the key value as the
input message for the operation; and returns the status (successful or failure) of the verification operation.
For more details, refer to the HSE Service API Reference Manual.
6.3  Key management: SHE keys
6.3.1  Scope
The key type HSE_KEY_TYPE_SHE allows key management as specified in SHE – Secure Hardware
Extension Functional Specification. This section details how these keys must be declared and how to invoke
SHE key provisioning commands in the HSE.
6.3.2  Declaring SHE keys
The AES 128-bit keys specified in SHE – Secure Hardware Extension Functional Specification are declared as
HSE_KEY_TYPE_SHE in specific key groups and slots within the key catalogs as described in the below table.
SHE key name (ID)
Key catalog
Key group index
Key slot index
SECRET_KEY (0x00)
ROM key catalog
N/A
N/A
MASTER_ECU_KEY (0x01)
0
BOOT_MAC_KEY (0x02)
1
KEY_1 (0x04)
2
KEY_2 (0x05)
3
KEY_3 (0x06)
4
KEY_4 (0x07)
5
KEY_5 (0x08)
6
KEY_6 (0x09)
7
KEY_7 (0x0A)
8
KEY_8 (0x0B)
9
KEY_9 (0x0C)
10
KEY_10 (0x0D)
NVM key catalog
0
11
RAM_KEY (0x0E)
RAM key catalog
0
0
Table 67. SHE keys
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
138 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 139

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The SHE keys must map to the key group 0 in the three key catalogs. Trying to map those keys in a
different group either results in an error during the key catalog formatting operation, or in an error during key
provisioning.
All SHE keys must belong to the HSE_KEY_OWNER_ANY group owner; otherwise an error is reported during
key catalog formatting.
Except for SECRET_KEY (which is a read-only key) and RAM_KEY (which is the only volatile key), all the
keys listed above must be provisioned with the SHE key update protocol (see below). RAM_KEY can either be
provisioned with the SHE key update protocol or with the SHE plain key update service (see SHE Plain Key
Update).
The “special” BOOT_MAC value defined in the SHE – Secure Hardware Extension Functional Specification
is the CMAC value over the “boot” (and its size) calculated using the key BOOT_MAC_KEY. In the HSE, this
“special” key corresponds to the reference authentication tag of the secure memory region (SMR) #0. It is not
mapped as a key but can still be updated using the SHE key update protocol.
6.3.3  Declaring extended SHE keys
In addition to the SHE keys KEY_1 to KEY_10 (key ID 0x4 to 0x0D), the HSE allows the application to provision
extra AES 128-bit keys using the SHE key update protocol. The mapping of those extra keys, referred to as
“extended SHE keys”, is listed in the below table.
Extended SHE key names
Key catalog
Group index
Slot index interval
KEY_11, KEY_12, … KEY_20
1
0 to 9
KEY_21, KEY_22, … KEY_30
2
0 to 9
KEY_31, KEY_32, … KEY_40
3
0 to 9
KEY_41, KEY_42, … KEY_50
NVM key catalog
4
0 to 9
Table 68. Extended SHE keys
The extended SHE keys must map to the key groups 1 to 4 in the NVM key catalogs. Trying to map those keys
in groups 5 and above result in an error during the key catalog formatting operation.
6.3.4  Declaration example
The below code is an example of NVM and RAM key catalog structures to (only) support the SHE and extended
SHE keys.
 
hseKeyGroupCfgEntry_t my_NVM_key_catalog[] = {
/* SHE keys */
  {HSE_MU0_MASK, HSE_KEY_OWNER_ANY, HSE_KEY_TYPE_SHE, 12, 128}, /* MASTER_ECU_KEY, BOOT_MAC_KEY */
                                                                /* KEY_1 to KEY_10 */
/* Extended SHE keys */
  {HSE_MU0_MASK, HSE_KEY_OWNER_ANY, HSE_KEY_TYPE_SHE, 10, 128}, /* KEY_11 to KEY_20 */
  {HSE_MU0_MASK, HSE_KEY_OWNER_ANY, HSE_KEY_TYPE_SHE, 10, 128}, /* KEY_21 to KEY_30 */
  {HSE_MU0_MASK, HSE_KEY_OWNER_ANY, HSE_KEY_TYPE_SHE, 10, 128}, /* KEY_31 to KEY_40 */
  {HSE_MU0_MASK, HSE_KEY_OWNER_ANY, HSE_KEY_TYPE_SHE, 10, 128}, /* KEY_41 to KEY_50 */
  {0, 0, 0, 0, 0}
};
hseKeyGroupCfgEntry_t my_RAM_key_catalog[] = {
/* SHE keys */ {HSE_MU0_MASK, HSE_KEY_OWNER_ANY, HSE_KEY_TYPE_SHE,  1, 128}, /* RAM_KEY */
  {0, 0, 0, 0, 0}
};
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
139 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 140

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.3.5  SHE key attributes
6.3.5.1  Security flags
SHE (and extended SHE) keys have security flags as specified in SHE – Secure Hardware Extension
Functional Specification that can be set via the SHE key update protocol (see below). Except for WILDCARD,
the security flags are shared with the other key types.
Security flags
Value
Description
0
The key can be provisioned (updated)
Write-protection of
memory slots
WRITE_PROTECTION
1
The key is write protected
0
The key can be used in all conditions
Disabling keys on boot
failure
BOOT_PROTECTION
1
The key cannot be used if SMR #0 authentication
failed
0
The key can be used in all conditions
Disabling keys on
debugger activation
DEBUGGER_PROTECTION
1
The key cannot be used if a debugger is connected
0
The key can be used for encryption and decryption
Key usage
determination
KEY_USAGE
1
The key can be used for CMAC generation and
verification; works in combination with VERIFY_
ONLY (see below)
0
The key can be used for CMAC generation and
verification
CMAC verification
usage
VERIFY_ONLY
1
The key can be used for CMAC verification only
0
The key can be provisioned with UID equal to 0.
Disable wildcard usage
for key updates (UID’ is
message M1)
WILDCARD
1
The UID must be provided when the key is
provisioned
Table 69. SHE key security flags
The “plain key flag” referenced in SHE – Secure Hardware Extension Functional Specification is internally
managed by the HSE.
The “key usage determination” flag reference in the SHE – Secure Hardware Extension Functional Specification
is enriched with one additional bit: VERIFY_ONLY; to be fully compliant with SHE – Secure Hardware Extension
Functional Specification, this flag must be 0.
6.3.5.2  Counter
SHE (and extended SHE) keys declared in the NVM key catalog hold a key update counter encoded on 28 bits
that is provisioned together with the key properties and value. During a key update, the new counter value must
be strictly above the value saved in its key slot. For the first-time initialization, the counter can take any value
strictly above 0 (that is, the minimum counter value is 1).
6.3.6  SHE key provisioning
SHE (and extended SHE) keys declared in the NVM key catalog can only be provisioned according to the key
update protocol defined in SHE – Secure Hardware Extension Functional Specification, hereafter referenced as
the “SHE key update protocol”. The RAM_KEY can also be provisioned using such protocol.
A SHE key can be provisioned based on the knowledge of an authentication key value.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
140 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 141

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.3.6.1  SHE key update protocol
Important:  If the SMR #0 failed verification (i.e. secure boot failed), all SHE keys, including RAM_KEY, can still
be provisioned with the SHE key update protocol.
The SHE key update protocol implements:
• Three input messages (M1, M2, M3); those messages specify the identifier of the key to update, the identifier
of the key used to authenticate the update (the authentication key), the new key value and attributes (security
flags, counter)
• Two output messages (M4, M5); those messages can be used by the application to verify that the key update
has completed successfully
The UID returned in message M4 is always equal to the UID value provided in message M1: it is either the
wildcard UID (all 0) or the device’s UID. This logic follows the SHE verification specification SHE – Secure
Hardware Extension Functional Specification. The messages M4 and M5 are provided as a "proof of memory
update". To verify that the key was correctly updated, it is possible to only verify that the last 16 bytes of M4 (bits
0 to 127) are as expected. These last 16 bytes should always match an expected M4 value regardless the value
of UID. If those bytes are as expected, it implies that both the counter and the key value have been correctly
provisioned to memory.
Acronym
Description
ID
Identifier of the key to update KID (see SHE key update protocol)
AuthID
Identifier of the authentication key KAuthID(see SHE key update protocol)
KID’
New key value
KAuthID
Authentication key value
CID’
New counter value
FID’
New security flag values, the concatenation WRITE_PROTECTION || BOOT_PROTECTION ||
DEBUGGER_PROTECTION || KEY_USAGE || WILDCARD || VERIFY_ONLY
CID
Current counter value
FID
Current security flag values
CMACK(M)
CMAC calculation over M using key K
ENCK(M)
AES CBC-encryption of M using key K (IV = 0)
CENC
KDF input constant for deriving an encryption key
CMAC
KDF input constant for deriving an authentication key
Table 70. Acronyms used in the SHE key update protocol
The below table provides the correspondence between the SHE key (and extended SHE key) names and the
identifiers ID and AuthID as they must be used in the SHE key update protocol.
Key to update / Authentication key
ID / AuthID
SECRET_KEY
0x00
MASTER_ECU_KEY
0x01
BOOT_MAC_KEY
0x02
BOOT_MAC
0x03
KEY_1, KEY_11, KEY_21, KEY_31, KEY_41
0x04
Table 71. Key ID values in SHE key update protocol
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
141 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 142

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Key to update / Authentication key
ID / AuthID
KEY_2, KEY_12, KEY_22, KEY_32, KEY_42
0x05
KEY_3, KEY_13, KEY_23, KEY_33, KEY_43
0x06
KEY_4, KEY_14, KEY_24, KEY_34, KEY_44
0x07
KEY_5, KEY_15, KEY_25, KEY_35, KEY_45
0x08
KEY_6, KEY_16, KEY_26, KEY_36, KEY_46
0x09
KEY_7, KEY_17, KEY_27, KEY_37, KEY_47
0x0A
KEY_8, KEY_18, KEY_28, KEY_38, KEY_48
0x0B
KEY_9, KEY_19, KEY_29, KEY_39, KEY_49
0x0C
KEY_10, KEY_20, KEY_30, KEY_40, KEY_50
0x0D
RAM_KEY
0x0E
Table 71. Key ID values in SHE key update protocol...continued
The below tables document the mapping of the input messages M1, M2 and M3.
Bit number
127 ~ 72
71 ~ 8
7 ~ 4
3 ~ 0
Field size
56 bits
64 bits
4 bits
4 bits
M1
0
UID or 0[1]
ID
AuthID
Table 72. Mapping of M1, M2 and M3
[1]
M1 can start with 120 bits to 0 only if WILDCARD FID is 0; otherwise, the UID must be provided.
Bit number
255 ~ 228
227 ~ 223
222 ~ 128
127 ~ 0
Field size
28 bits
6 bits
94 bits
128 bits
M2P
CID’ > CID
[1]
FID’
0
KID’
[1]
[Note]Providing a new counter value below or equal the current counter value terminates the key provisioning with an error. When ID = 0x0E (RAM_KEY),
this check is discarded.
Bit number
255 ~ 0
Field size
256 bits
M2
ENCK1(M2P)
Bit number
127 ~ 0
Field size
128 bits
M3
CMACK2(M1 || M2)
The below tables document the mapping of the output messages M4, and M5:
Bit number
127 ~ 100
99
98 ~ 0
Field size
28 bits
1 bit
99 bits
Table 73. Mapping of M4 and M5
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
142 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 143

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
M4P
CID’
1
0
Table 73. Mapping of M4 and M5...continued
Bit number
255 ~ 200
199 ~ 136
135 ~ 132
131 ~ 128
127 ~ 0
Field size
56 bits
64 bits
4 bits
4 bits
128 bits
M4
0
UID
ID
AuthID
ENCK3(M4P)
Bit number
127 ~ 0
Field size
128 bits
M5
CMACK4(M4)
The UID returned in message M4 is always equal to the UID value provided in message M1: it is either
the wildcard UID (all 0) or the device’s UID. This logic follows the SHE verification specification (see SHE
Verification Specification).
The messages M4 and M5 are provided as a “proof of memory update”. To verify that the key was correctly
updated, it is possible to only verify that the last 16 bytes of M4 (bits 0 to 127) are as expected.
These last 16 bytes should always match an expected M4 value regardless the value of UID. If those bytes are
as expected, it implies that both the counter and the key value have been correctly provisioned to memory.
A key derivation function (KDF) is defined to calculate the keys K1, K2, K3 and K4 as follows:
• K1 = KDF(KAuhtID, CENC)
• K2 = KDF(KAuhtID, CMAC)
• K3 = KDF(KID, CENC)
• K4 = KDF(KID, CMAC)
AES-ECB
K
AES-ECB
C
0
XOR
XOR
key
key
input
input
KDERIV
Figure 64. KDERIV = KDF(K, C)
Input key (K)
Input constant (CENC)
KEY_1 to KEY_10, RAM_KEY
KEY_UPDATE_ENC_C = 0x01015348 45008000 00000000 000000B0
KEY_11 to KEY_20
KEY_UPDATE_ENC_C + 0x00800000 00000000 00000000 00000000
KEY_21 to KEY_30
KEY_UPDATE_ENC_C + 0x00900000 00000000 00000000 00000000
KEY_31 to KEY_40
KEY_UPDATE_ENC_C + 0x00A00000 00000000 00000000 00000000
Table 74. KDF input constants for K1 and K3
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
143 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 144

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Input key (K)
Input constant (CENC)
KEY_41 to KEY_50
KEY_UPDATE_ENC_C + 0x00B00000 00000000 00000000 00000000
Table 74. KDF input constants for K1 and K3...continued
Input key (K)
Input constant (CMAC)
KEY_1 to KEY_10, RAM_KEY
KEY_UPDATE_MAC_C = 0x01025348 45008000 00000000 000000B0
KEY_11 to KEY_20
KEY_UPDATE_MAC_C + 0x00800000 00000000 00000000 00000000
KEY_21 to KEY_30
KEY_UPDATE_MAC_C + 0x00900000 00000000 00000000 00000000
KEY_31 to KEY_40
KEY_UPDATE_MAC_C + 0x00A00000 00000000 00000000 00000000
KEY_41 to KEY_50
KEY_UPDATE_MAC_C + 0x00B00000 00000000 00000000 00000000
Table 75. KDF input constants for K2 and K4
The SHE and extended SHE keys can be provisioned by the host via a SHE key import service, defined by the
structure hseSheLoadKeySrv_t, which takes in input:
• sheGroupIndex: the key group index on which the key update applies (see section Declaring Extended SHE
Keys)
– This index is different from 0 only if one of the SHE extended keys is being provisioned (KEY_11 to
KEY_50)
• pM1, pM2, pM3, pM4, pM5: pointers to byte arrays M1[], M2[], M3[], M4[] and M5[]
The MU instance map is defined in the target key group (see Key Catalog).
6.3.6.2  SHE key update policies
The following update policies apply to the SHE and extended SHE keys:
• The MASTER_ECU_KEY can be updated only based on the knowledge of MASTER_ECU_KEY
– In message M1: AuthID = ID = MASTER_ECU_KEY
• BOOT_MAC_KEY can be updated based on the knowledge of MASTER_ECU_KEY or BOOT_MAC_KEY
– In message M1: AuthID = ID = BOOT_MAC_KEY or AuthID = MASTER_ECU_KEY
• BOOT_MAC can be updated based on the knowledge of MASTER_ECU_KEY or BOOT_MAC_KEY
– In message M1: AuthID = BOOT_MAC_KEY or AuthID = MASTER_ECU_KEY
– BOOT_MAC cannot be used as an authentication key
• KEY_<n> (with n 
 {1, 50}) can be updated based on the knowledge of MASTER_ECU_KEY or the current
KEY_<n>
– In message M1: AuthID = ID or AuthID = MASTER_ECU_KEY
• ID cannot be set to 0x00 (SECRET_KEY)
• RAM_KEY can be updated based on the knowledge of any KEY_<n> (with n 
 {1, 50})
– In message M1: AuthID = KEY_<n> (with n 
 {1, 50})
• It is only possible to use an empty key as the authentication key when that key is being initialized for the first
time (i.e. when ID = AuthID)
– In this case, the key value to calculate the authentication tag (M3) is the value of an empty key
Important:  The empty key value in the SHE key update protocol equals to 128 bits cleared to 0.
The following restrictions apply to the SHE keys within the RAM key catalog:
• When RAM_KEY is updated with the SHE key update protocol, it cannot be exported, until it is updated in
plain via the key import service or via the SHE plain key update (see below)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
144 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 145

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.3.7  SHE plain key update
The SHE key RAM_KEY can be provisioned by the host in plain, as defined in SHE – Secure Hardware
Extension Functional Specification, via a SHE plain key import service, defined by the structure
hseSheLoadPlainKeySrv_t, which takes in input:
• pKey: pointer to the RAM key value (in plain)
The MU instance map is defined in the target key group (see Key Catalog).
6.3.8  SHE key export
The SHE key RAM_KEY can be securely exported by the host, as defined in SHE – Secure
Hardware Extension Functional Specification, via a SHE key export service, defined by the structure
hseSheExportRamKeySrv_t, which takes in input:
• pM1, pM2, pM3, pM4, pM5: pointers to messages M1 to M5
All messages (M1 to M5) are calculated by the HSE using:
• ID = 0x0E (RAM_KEY)
• AuthID = 0x00 (SECRET_KEY)
• CID = CID’ = 0
• FID’ = 0
For the details on the computation of messages M1 to M5, see section SHE Key Provisioning.
6.3.9  Using SHE keys
Apart from the above described key management functions, keys of type HSE_KEY_TYPE_SHE can be used in
the following services:
• Block ciphering (all modes)
• AES MACs (CMAC, GMAC and XCBC-MAC if supported)
• Securing the authenticity and integrity of SMR #0 only (this SMR is used to implement the secure boot as
described in SHE – Secure Hardware Extension Functional Specification).
6.4  Cryptographic functions
6.4.1  Generalities
6.4.1.1  Key usage restrictions
Keys can be used in the services described in this chapter only if their usage flag
HSE_KF_USAGE_KEY_PROVISION is not set and only if all the related SMRs have been successfully
verified.
6.4.1.2  Cipher block size
The input and output blocks to a cipher primitive (e.g. AES) have a fixed size, referred hereafter as the “cipher
block size”, which imposes some restrictions on the inputs/outputs to/from the HSE as documented in the
subsequent sections in this chapter.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
145 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 146

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Cipher primitive
Cipher block size in bits
Cipher block size in bytes
AES
128 bits
16 bytes
Table 76. Ciphers and corresponding block sizes
6.4.1.3  Useful bits
In the context of a ciphering operation, the terms “useful bits” denote that only certain bits within a (message)
block are used by the ciphering function. Unless otherwise specified, the useful bits are MSB. For example, if an
input block 0xAA551122 has only 8 useful bits, 0xAA is used by the ciphering function, the rest of the input block
is not used.
6.4.1.4  Hash block size
The digest size (or hash size) is the output size of the hashing operation.
The hash block size is the size of the block that is processed by a hash primitive. This is different from the
digest size and imposes some restrictions on the inputs to the HSE as documented in the subsequent sections
in this chapter.
Hash primitive
Hash block size in bits
Digest size in bits
SHA1
512
160
SHA224
512
224
SHA256
512
256
SHA384
1024
384
SHA512
1024
512
SHA512-224
1024
224
SHA512-256
1024
256
Table 77. Hash block sizes and digest sizes
6.4.1.5  Streaming vs. one-pass mode
All cryptographic services run in one-pass mode: the host makes one service request to the HSE, which then
handles all the required data transfers and processing without any further involvement of the host.
For certain cryptographic services which involve manipulation of large data potentially scattered over different
memory locations, the host has the possibility to run operations in streaming mode: in this case, the host
triggers several service requests to the HSE. The HSE handles the saving of the execution context in between
the calls.
When possible, the selection between streaming and one-pass mode is done by the host via the the data field
accessMode. For more information, refer to the section Service Execution.
6.4.2  Block ciphering
The host can request for message encryption and decryption with different block ciphering modes as
specified in Recommendation for Block Cipher Modes of Operation via the service defined by the structure
hseSymCipherSrv_t.
6.4.2.1  Algorithms
A message 
 transforms into a message  based on the knowledge of a secret key .
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
146 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 147

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
When running an encryption, 
 is a plaintext and  is the corresponding ciphertext (encrypted text). When
running a decryption, 
 is a ciphertext and  is the corresponding plaintext.
The message 
 is the concatenation of  blocks 
 having a size equal to the cipher block size.
The message  is the concatenation of  blocks 
 having a size equal to the cipher block size.
Except for ECB, all block ciphering modes take in input an initialization vector 
 having a size equal to the
cipher block size.
The underlying cipher primitive can be AES.
The below table details the encryption and decryption algorithms for the different block ciphering modes
supported.
Block
ciphering
mode
Encryption (
 ) 
 is the resulting ciphertext
Decryption (
 ) 
 is the resulting
decrypted text
ECB
CBC
CTR
CFB
OFB
Table 78. Block ciphering modes and corresponding encryption / decryption algorithms
In ECB, CBC and CFB modes, the size of the message 
 must be a multiple of the cipher block size.
In the HSE:
• The size of the data segments as specified in the Recommendation for Block Cipher Modes of Operation
equal the block cipher size
• The parameter 
 in CTR mode aligns with the block cipher size (that is, 
= 128 for AES)
In CTR and OFB modes, the message 
 can be any size. The unused bits in the last block are discarded from
the resulting message .
For more information, refer to Recommendation for Block Cipher Modes of Operation.
6.4.2.2  Key selection
A message transforms into a cipher based on the knowledge of a secret key.
The data field keyHandle specifies the key  to be used. It must point to a valid and non-empty key.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
147 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 148

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The key type (HSE_KEY_TYPE_AES) must align with the underlying ciphering algorithm selected, and its
usage restriction must allow an encryption and/or decryption operation (that is, HSE_KF_USAGE_ENCRYPT
and/or HSE_KF_USAGE_DECRYPT are set).
For the key type HSE_KEY_TYPE_SHE, the SHE key attribute must be:
• KEY_USAGE = 0
If the ciphering operation is processed in streaming mode, the key handle must only be provided in the START
call.
6.4.2.3  Service configuration
The data field cipherAlgo specifies the cipher primitive to be used: AES.
The data field cipherBlockMode specifies the block ciphering mode to be used: ECB, CBC, CTR, CFB, OFB.
The data field cipherDir specifies the ciphering operation:
• HSE_CIPHER_DIR_ENCRYPT indicates an encryption operation
• HSE_CIPHER_DIR_DECRYPT indicates a decryption operation
6.4.2.4  Input and output data
The initialization IV vector is provided via the data field pIV. The byte size of this vector is 16 bytes, exactly
equal to the underlying cipher block size of AES.
• In ECB mode, this data field is not used by the HSE
• In streaming mode, those data fields are mandatory in the START call
The input message M is provided via the data field pInput.
• In one-pass mode, pInput is the pointer to the first byte of the message to process, and the data field
inputLength specifies the number of bytes to be read from that memory location (that is, the entire
message size)
– For ECB, CBC and CFB modes: inputLength must be a multiple of the underlying cipher block size
– For CTR and OFB modes: inputLength can be any value strictly above 0
– The number of blocks n equals 
 (where blocksize is the cipher block size)
• In streaming mode, pInput is the pointer to the first or next message chunk to process, and inputLength
is the byte size of that chunk
– For the START call, inputLength can be 0; otherwise, it must be a multiple of the underlying cipher block
size
– For UPDATE calls, inputLength cannot be 0 and must be a multiple of the underlying cipher block size.
The UPDATE call is not mandatory
– For the FINISH call, inputLength cannot be 0; in addition:
–
For ECB, CBC and CFB modes: it must be a multiple of the underlying cipher block size
–
For CTR, CFB and OFB modes: it can be any value above 0
– The number of blocks n equals 
 (where mlen is the overall message size in bytes and
blocksize is the cipher block size)
The resulting message  (that is, the cipher or the decrypted message) is returned by the HSE at the memory
location pointed by pOutput.
• The size of the output message equals the size of the input message; the host must allocate enough memory
for the HSE to write the resulting cipher value
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
148 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 149

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• In streaming mode, pOutput is filled with a part of the resulting message, corresponding to the input chunk
provided
All memory locations provided in the service structure must be accessible by both the host and the HSE.
When the input and/or output messages are scattered across multiple memory locations, pInput and/or
pOutput can point to scatter/gather lists as described in Scatter Gather Input and Output. In this case, the data
field sgtOption must be set according to the selected configuration[note].
Note:  SGT is only supported for SHA1, SHA224, and SHA256.
6.4.2.5  Service result
Upon successful block ciphering operation, the service terminates with the response HSE_SRV_RSP_OK. The
resulting message  can be retrieved by the host at memory location pOutput (inputLength bytes to be
read).
6.4.3  Hashing
The host can request for message hashing with different hash primitives as specified in Secure Hash Standard
(SHS) and SHA-3 Standard. via the service defined by the structure hseHashSrv_t.
6.4.3.1  Algorithms
Hash functions are one-way transforms that map any message of arbitrary size to a digest of (relatively) small
size.
The hash primitive 
has an output digest size .
A message 
 is compressed into an  bit digest  as follows:
For a given message 
, computing a hash is easy. However, recalculating the value of the message 
 from
the digest value is very hard.
Changing just one bit within a (very) large input message 
 completely changes the output of the hash primitive
. For that reason, digests over messages are a good way to guarantee their integrity.
Various hash primitives (SHA1, SHA2, SHA3) are supported depending on the HSE subsystem: see Device
Specific Parameters.
6.4.3.2  Key selection
Hash primitives do not involve the use of a key.
6.4.3.3  Service configuration
The data field hashAlgo specifies the hash primitive to be used.
6.4.3.4  Input and output data
The input message 
 is provided via the data field pInput.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
149 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 150

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• In one-pass mode, pInput is the pointer to the first byte of the message to process, and the data field
inputLength specifies the number of bytes to be read from that memory location (that is, the entire
message size)
– inputLength can be 0
• In streaming mode, pInput is the pointer to the first or next message chunk to process, and inputLength
is the byte size of that chunk
– pInput is always mandatory in any calls (START, UPDATE, FINISH), unless inputLength is 0
– inputLength must be a multiple of the hash block size (see Hash block size)
The resulting digest  is returned by the HSE at the memory location pointed by pHash.
• The data field pHashLength is a pointer to a 32-bit word containing the byte size of the digest to generate
• On service call, *pHashLength must be set with the size of the byte array pointed by pHashor the expected
digest size in bytes
– *pHashLength multiplied by 8 defines the bit size ; if  is above the digest size (see Hash block size), the
output digest is truncated on the MSB side
– *pHashLength cannot be 0
• Once the digest is generated by the HSE, *pHashLength is set with the number of bytes actually written by
the HSE at memory location pHash
• In streaming mode, pHash and pHashLength must be provided in the FINISH call (data fields ignored in
START and UPDATE calls)
All memory locations provided in the service structure must be accessible by both the host and the HSE.
When the input message is scattered across multiple memory locations, pInput can point to a scatter/gather
list as described in Scatter gather input and output. In this case, the data field sgtOption must be set to
HSE_SGT_OPTION_INPUT.
6.4.3.5  Service result
Upon successful hashing, the service terminates with the response HSE_SRV_RSP_OK. The resulting digest 
can be retrieved by the host at memory location pHash (*pHashLength bytes to be read).
6.4.4  Message compression
The host can request for message compression using the Miyaguchi–Preneel compression function via the
service defined by the structure hseHashSrv_t.
6.4.4.1  Algorithms
The Miyaguchi–Preneel compression function maps a message with a digest in a similar way as a hashing
function, except that it is based on a one-way transform using a cipher primitive. In the HSE, this cipher primitive
is AES.
The message 
 is the concatenation of  blocks 
 having a size equal to the cipher block size.
The minimum message size must be 128 bits (at least one cipher block size).
A message 
 is compressed into a 128-bit digest  as follows:
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
150 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 151

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.4.4.2  Key selection
The key used in the Miyaguchi–Preneel compression function is defined by the result of the previous block
calculation (
). Hence it does not involve a key selection by the host.
6.4.4.3  Service configuration
The data field hashAlgo must be set to HSE_HASH_ALGO_MP.
This service can only be used in one-pass mode, hence the data field accessMode must be set to
HSE_ACCESS_MODE_ONE_PASS.
6.4.4.4  Input and output data
The input message 
 is provided via the data field pInput.
The data field pInput is the pointer to the first byte of the message to process, and the data field
inputLength specifies the number of bytes to be read from that memory location (i.e. the entire message
size).
The data field inputLength must be a multiple of the underlying cipher block size.
The resulting digest  is returned by the HSE at the memory location pointed by pHash.
• The data field pHashLength is a pointer to a 32-bit word containing the byte size of the digest to generate
• On service call, *pHashLength must be set with the size of the byte array pointed by pHashor the expected
digest size in bytes
– *pHashLength must be at least 16 and cannot be 0
• Once the digest is generated by the HSE, *pHashLength is set with the number of bytes actually written by
the HSE at memory location pHash
6.4.4.5  Service result
Upon successful message compression, the service terminates with the response HSE_SRV_RSP_OK. The
resulting digest  can be retrieved by the host at memory location pHash (*pHashLength bytes to be read).
6.4.5  MAC generation and verification
The host can request for the generation and the verification of message authentication codes (MAC) with
different algorithms as specified in Recommendation for Block Cipher Modes of Operation: The CMAC Mode
for Authentication, The Keyed-Hash Message Authentication Code (HMAC) and The AES-XCBC-MAC-96
Algorithm and Its Use with IPsec via the service defined by the structure hseMacSrv_t.
6.4.5.1  Algorithms
A Message Authentication Code (MAC) is a tag, also referred to as authentication tag, calculated over a
message to attest its authenticity. The calculation involves either a ciphering or hash primitive and requires the
knowledge of a secret key.
The following subsections describe the algorithms to compress a message 
 into an  bit authentication tag 
based on the knowledge of a secret key .
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
151 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 152

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.4.5.1.1  CMAC
The message 
 is the concatenation of  blocks 
 having a size equal to the cipher block size.
The number of useful bits  in the last block 
 can be below the cipher block size. In this case, the remaining
bits are padded with the constant 
, where  is the cipher block size in bits.
• For example: if 
, 
 and 
, the padded
block 
 is 
For a given message 
 and a private key , the -bit cipher-based MAC generation algorithm
is:
For the CMAC as defined in The AES-XCBC-MAC-96 Algorithm and Its Use with IPsec , the cipher primitive is
always AES and the 
 function computes the subkeys 
, 
 and 
 as follows:
When using the AES cipher primitive,  = 0x87 and  = 128.
For a given message 
, its  bit authentication tag  and a private key , the cipher-based MAC verification
algorithm is:
For more information refer to Recommendation for Block Cipher Modes of Operation: The CMAC Mode for
Authentication.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
152 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 153

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.4.5.1.2  HMAC
For a given message 
 and a private key , the -bit hash-based MAC (HMAC) generation algorithm
is:
The 
 function is defined as follows:
In the above,  is the block size of the hash primitive 
.
In the HSE, the key  cannot be bigger than .
For a given message 
, its  bit authentication tag  and a private key , the HMAC verification algorithm is:
 as defined above
 the tag (message) is authentic
For more information refer to the The Keyed-Hash Message Authentication Code (HMAC).
6.4.5.1.3  GMAC
The underlying cipher primitive is AES. The cipher block size is 128 bits (16 bytes).
The message 
 is the concatenation of  blocks 
 having a size equal to 128 bits.
The number of useful bits  in the last block 
 can be below 128. In this case, only the most significant  bits
of 
 are used in the encryption or decryption process, and the number of blocks  must be strictly above 1.
GMAC takes in input an initialization vector 
. The 
 byte size 
. In the HSE, 
 is minimum 1 byte.
For a given message 
, an initialization vector 
 and a private key , the -bit GCM-based authentication tag
(GMAC) generation algorithm 
is:
The 
 encoding function 
 is defined as follows:
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
153 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 154

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The function 
 is defined as follows:
For a given message 
, its -bit GMAC tag , an initialization vector 
 and a private key , the GMAC
verification algorithm is:
 as defined above
 the tag (message) is authentic
For more information, refer to Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode
(GCM) and GMAC.
6.4.5.2  Key selection
A MAC is calculated over a message based on the knowledge of a secret key.
The data field keyHandle specifies the key to be used. It must point to a valid and non-empty key.
The key type (HSE_KEY_TYPE_AES or HSE_KEY_TYPE_HMAC) must align with the underlying MAC
algorithm selected, and its usage restriction must allow a MAC operation (i.e. HSE_KF_USAGE_SIGN and/or
HSE_KF_USAGE_VERIFY are set).
For the key type HSE_KEY_TYPE_SHE, only the MAC algorithms based on AES are supported and the SHE
key attribute must be:
• KEY_USAGE == 1
• VERIFY_ONLY == 0 for a MAC generation or verification
• VERIFY_ONLY == 1 for a MAC verification
For HMAC, the key size must be smaller than or equal to the hash block size (i.e. maximum 512 bits for
SHA256).
If the MAC operation is processed in streaming mode, the key handle must only be provided in the START call.
6.4.5.3  Service configuration
The data field macScheme.macAlgo specifies the MAC algorithm, that can be:
• CMAC as specified in Recommendation for Block Cipher Modes of Operation: The CMAC Mode for
Authentication
• GMAC (Galois MAC) as specified in Recommendation for Block Cipher Modes of Operation: Galois/Counter
Mode (GCM) and GMAC
• HMAC (hash-based MAC) as specified in The Keyed-Hash Message Authentication Code (HMAC)
The GMAC algorithm is implying the use of the AES cipher primitive.
For a CMAC algorithm, the data field macScheme.sch.cmac.cipherAlgo specifies the underlying ciphering
function (AES).
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
154 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 155

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
For a HMAC algorithm, the data field macScheme.sch.hmac.hashAlgo specifies the underlying hash
primitive (e.g. SHA256).
The data field authDir specifies the MAC operation mode:
• HSE_AUTH_DIR_GENERATE indicates a MAC generation: the HSE calculates a MAC and returns it to the
host
• HSE_AUTH_DIR_VERIFY indicates a MAC verification: the HSE calculates a MAC and compares it with the
reference value provided by the host
6.4.5.4  Input and output data
GMAC is the only scheme that requires the definition of an initialization vector, provided via the data field
macScheme.sch.gmac.pIV and macScheme.sch.gmac.ivLength.
The input message 
 is provided via the data field pInput.
• In one-pass mode, pInput is the pointer to the first byte of the message to process, and the data field
inputLength specifies the number of bytes to be read from that memory location (that is, the entire
message size)
– For CMAC and GMAC, the number of blocks  equals 
 (where 
 is the cipher
block size)
– The number of useful bits  in the last block equals inputLength modulus the cipher block size
– inputLength can be 0
• In streaming mode, pInput is the pointer to the first or next message chunk to process, and inputLength
is the byte size of that chunk
– For the START call, inputLength cannot be 0 and must be a multiple of the underlying cipher block size
or hash block size (i.e. n x 16 bytes for AES, n x 32 bytes for SHA256)
– For the UPDATE call, inputLength must be a multiple of the underlying cipher block size (for CMAC and
GMAC) or hash block size (for HMAC) and cannot be zero. The UPDATE call is not mandatory
– For the FINISH call, inputLength can be any value. For CMAC, zero length is invalid
For a MAC generation, the resulting authentication tag  is returned by the HSE at the memory location pointed
by pTag.
• The data field pTagLength is a pointer to a 32-bit word containing the byte size of the authentication tag to
generate
• On service call, *pTagLength must be set with the size of the byte array pointed by pTagor the expected tag
size in bytes
– *pTagLength multiplied by 8 defines the authentication tag bit size 
– *pTagLength cannot be 0
– *pTagLength must match with the MAC size constraints as listed in Input and output data
• Once the tag is generated by the HSE, *pTagLength is set with the number of bytes written by the HSE at
memory location pTag; if the expected tag size was set above the maximum possible value, *pTagLength is
set to that maximum value
• In streaming mode, pTag and pTagLength must be provided in the FINISH call (data fields ignored in
START and UPDATE calls)
For a MAC verification, the reference tag  (which is compared to the computed tab 
) is provided by the
pointer pTag.
• The data field pTagLength is a pointer to a 32-bit word containing the byte size of the authentication tag to
verify
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
155 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 156

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• On service call, *pTagLength must be set with the number of bytes to be verified at memory location pTag,
with the constraints as listed in Input and output data
MAC algorithm
Authentication tag size
AES-CMAC
8 to 16 bytes
GMAC
8, 12, 13, 14, 15 or 16 bytes
HMAC
8 byte to hash size (that is, 32 bytes for SHA256)
Table 79. MAC algorithms vs. tag sizes
All memory locations provided in the service structure must be accessible by both the host and the HSE.
When the input message is scattered across multiple memory locations, pInput can point to a scatter/gather
list as described in section Scatter Gather Input and Output. In this case, the data field sgtOption must be set
to HSE_SGT_OPTION_INPUT.
6.4.5.5  Service result
Upon successful MAC generation, the service terminates with the response HSE_SRV_RSP_OK and the
authentication tag can be retrieved by the host at memory location pTag (*pTagLength bytes to be read).
Upon successful completion of the MAC verification, the service terminates with the response
HSE_SRV_RSP_OK if the MAC provided is found authentic, or with HSE_SRV_RSP_VERIFY_FAILED if the
MAC does not match with the message.
6.4.5.6  Variant: Fast CMAC generation and verification
A timing-optimized implementation of the AES-CMAC generation and the verification is available to the host via
the service defined by the structure hseFastCMACSrv_t.
• Most of the data fields defined in this service are common with the default MAC service described in this
section: the key to use to compute the CMAC is defined by keyHandle
• The data field authDir specifies the MAC operation mode (generate or verify)
• The input message is defined by pInput and inputBitLength
• The input / output CMAC is defined by pTag and tagBitLength.The tagBitLength must be between
the size specified by HSE_FAST_CMAC_MIN_TAG_BIT_LEN_ATTR_ID attribute and 128 bits. Note that the
default HSE_FAST_CMAC_MIN_TAG_BIT_LEN_ATTR_ID attribute value is HSE_DEFAULT_MIN_FAST_
CMAC_TAG_BITLEN bits (refer to HSE_FAST_CMAC_MIN_TAG_BIT_LEN_ATTR_ID attribute)
The differences with the default MAC service are as follows:
• It only implements the CMAC algorithm as described in Recommendation for Block Cipher Modes of
Operation: The CMAC Mode for Authentication
• The cipher primitive is AES; hence the input key must be of type HSE_KEY_TYPE_AES or
HSE_KEY_TYPE_SHE
• The streaming execution mode is not supported
• The size of input message and tag length is taken in bits instead of bytes
This service is tailored for AES-CMAC operations on small messages and yields faster timing than the default
MAC service.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
156 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 157

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.4.5.7  CMAC with counter
The HSE supports a service defined by the structure hseCmacWithCounterSrv_t to generate/verify the
CMAC of a given input message concatenated with a selected monotonic counter. For monotonic counter
configuration refer to Monotonic counter services.
Most of the data fields defined in this service are common with the Fast CMAC service described in the above
section.
The differences with the Fast CMAC service are the following:
• The data field counterIdx, which specifies the monotonic counter index.
• The data field RPOffset, which specifies the Rollover protection offset used to adjust the Rollover protection
bits of the counter in the CMAC verify operation.
• The data field pVolatileCounter which specifies the address of a 32-bit value for the volatile counter. This
field is used as output for CMAC generate and input for CMAC verify.
On CMAC generate, the service computes the CMAC tag over the input concatenated with a counter specified
by counterIdx.
On CMAC verify, the service performs the following steps:
• Builds the counter to be used for CMAC verification: adding the RPOffset to the Rollover value to adjust the
RP and concatenating the RP with the pVolatileCounter value.
• If the CMAC verification succeeds, the monotonic counter is updated with the value of the built counter.
For more details refer to HSE Service API Reference Manual.
6.4.6  Authenticated block ciphering (AEAD)
The host can request for message authentication and encryption / decryption with different block ciphering
algorithms as specified in Recommendation for Block Cipher Modes of Operation: The CCM Mode for
Authentication and Confidentiality and Recommendation for Block Cipher Modes of Operation: Galois/Counter
Mode (GCM) and GMAC via the service defined by the structure hseAeadSrv_t.
6.4.6.1  Algorithms
The following subsections describe the algorithms to transform a message 
 into a message  and at the
same time produce an  bit authentication tag  that authenticates the message 
 and additional authenticated
data , based on the knowledge of a secret key .
6.4.6.1.1  CCM
The underlying cipher primitive is AES. The cipher block size is 128 bits (16 bytes).
The message 
 is the concatenation of  blocks 
 having a size equal to 128 bits.
The number of useful bits  in the last block 
 can be below 128. In this case, only the most significant  bits
of 
 are used in the encryption or decryption process, and the number of blocks  must be strictly above 1.
The associated authentication data 
 is the concatenation of 
 blocks 
 having a size equal to 128 bits.
The number of useful bits 
 in the last block 
 can be below 128. In this case, only the most significant 
 bits
of 
 are used in the authentication process, and the number of blocks 
 must be strictly above 1.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
157 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 158

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
CCM takes in input an initialization vector 
. The 
 byte size 
 is minimum 7 bytes and maximum 13
bytes.
The message  is the concatenation of  blocks 
 having a size equal to 128 bits. 
 has  useful bits as
defined by the input message 
.
For a given associated authentication data 
, message 
, initialization vector 
 and a private key , the 
bit authentication tag (CBC-MAC) generation algorithm 
is:
The two 
 encoding functions are defined as follows:
The bytes 
 and 
 are defined as follows:
Note:  The authentication tag bit size  must be a multiple of 8 bits and minimum 32 bits.
The message  is the AES CTR encryption / decryption of the message 
 with an input vector 
 and the key
. 
 is defined as follows:
For a given associated authentication data 
, message 
, initialization vector 
, a private key  and an 
bit authentication tag , the CBC-MAC verification algorithm is:
as defined above
 the tag (message) is authentic
For more information, refer to Recommendation for Block Cipher Modes of Operation: The CCM Mode for
Authentication and Confidentiality.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
158 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 159

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.4.6.1.2  GCM
The underlying cipher primitive is AES. The cipher block size is 128 bits (16 bytes).
The message 
 is the concatenation of  blocks 
 having a size equal to 128 bits.
The number of useful bits  in the last block 
 can be below 128. In this case, only the most significant  bits
of 
 are used in the encryption or decryption process, and the number of blocks  must be strictly above 1.
The associated authentication data 
 is the concatenation of 
 blocks 
 having a size equal to 128 bits.
The number of useful bits 
 in the last block 
 can be below 128. In this case, only the most significant 
 bits
of 
 are used in the authentication process, and the number of blocks 
 must be strictly above 1.
GCM takes in input an initialization vector 
. The 
 byte size 
. In the HSE, 
 is minimum 1 byte.
The message  is the concatenation of  blocks 
 having a size equal to 128 bits. 
 has  useful bits as
defined by the input message 
.
The message  is the AES CTR encryption / decryption of the message 
 with an input vector 
 and the key
. The CTR mode is operated with 
 = 32 (see Cipher Block Size). 
 is defined as follows:
For a given associated authentication data 
, a ciphertext or decrypted message , an initialization vector
 and a private key , the  bit authentication tag (GMAC) generation algorithm 
is:
The 
 encoding function 
 is defined as follows:
The function 
 is defined as follows:
For a given associated authentication data 
, a ciphertext or decrypted message , an initialization vector
a private key  and an  bit authentication tag , the GMAC verification algorithm is:
as defined above
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
159 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 160

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
the tag (message) is authentic
For more information, refer to Recommendation for Block Cipher Modes of Operation: Galois/Counter Mode
(GCM) and GMAC.
6.4.6.2  Key selection
A message 
 transforms into a message  with an authentication tag based on the knowledge of a secret
key .
The data field keyHandle specifies the key to be used. It must point to a valid and non-empty key.
The key type must be HSE_KEY_TYPE_AES, and the key usage restriction must allow an encryption and/or
decryption operation (i.e. HSE_KF_USAGE_ENCRYPT and/or HSE_KF_USAGE_DECRYPT are set).
If the ciphering operation is processed in streaming mode, the key handle must only be provided in the START
call. 
6.4.6.3  Service configuration
The data field authCipherMode specifies ciphering algorithm to be used: CCM, GCM.
The data field cipherDir specifies the ciphering operation:
• HSE_CIPHER_DIR_ENCRYPT indicates an encryption operation; the result is an encrypted message and an
authentication tag
• HSE_CIPHER_DIR_DECRYPT indicates a decryption and authentication operation; the result is a decrypted
message and an authenticity check
6.4.6.4  Input and output data
The initialization vector 
 is provided via the data field pIV. The byte size 
 is provided in ivLength:
• In CCM mode, ivLength must be strictly above 6 and strictly below 14
• In GCM mode, ivLength must be strictly above 0 (12 bytes recommended)
• In streaming mode, those data fields must be provided in the START call
The associated authentication data 
 are provided via the data field pAAD. The byte size of those data is
provided in aadLength:
• aadLength can be 0; in this case, pAAD is ignored by the HSE
• In CCM mode, aadLength cannot be greater than 65280 bytes (216 – 28)
• In streaming mode, the data field must only be provided in the START call (ignored in the UPDATE and
FINISH calls)
– The entire authentication data (if available) must be provided at once
The input message 
 (either a plaintext or a ciphertext) is provided via the data field pInput:
• In one-pass mode, pInput is the pointer to the first byte of the message to process, and the data field
inputLength specifies the number of bytes to be read from that memory location (i.e. the entire message
size)
– inputLength can be 0; in this case, the service only calculates the authentication tag over the AAD
– It is also possible to have both inputLength and aadLength equal to 0
• In streaming mode, pInput is the pointer to the first or next message chunk to process, and inputLength
is the byte size of that chunk
– pInput is ignored if inputLength is 0
– For UPDATE call(s), the inputLength must be a multiple of the underlying cipher block size
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
160 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 161

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
– For the FINISH call, inputLength can be any value (including 0)
The resulting message  (either a ciphertext or a plaintext) is returned by the HSE at the memory location
pointed by pOutput:
• The size of the output message equals the size of the input message; the host must allocate enough memory
for the HSE to write the result
• In streaming mode, pOutput is filled with a part of the resulting ciphertext or plaintext, corresponding to the
input chunk provided
– This data field must be provided in UPDATE and FINISH calls; it is ignored in START call.
For an encryption, the calculated authentication tag  is returned by the HSE at the memory location pointed by
pTag. For a decryption, pTag points to the reference tag to be verified:
• The data field tagLength multiplied by 8 defines the authentication tag bit size 
• In CCM mode, tagLength can be any even integer between 4 and 16
• In GCM mode, tagLength can be 4, 8 or any integer between 12 and 16
• In streaming mode, pTag and tagLength must be provided in the FINISH call (data fields ignored in START
and UPDATE calls)
All memory locations provided in the service structure must be accessible by both the host and the HSE.
When the input and/or output messages are scattered across multiple memory locations, pInput and/or
pOutput can point to scatter/gather lists as described in section Scatter Gather Input and Output. In this case,
the data field sgtOption must be set according to the selected configuration.
6.4.6.5  Service result
Upon successful encryption, the service terminates with the response HSE_SRV_RSP_OK. The resulting
ciphertext  can be retrieved by the host at memory location pOutput (inputLength bytes to be read), and
the associated authentication tag  can be retrieved at memory location pTag (tagLength bytes to be read).
Upon successful decryption, the service terminates with the response HSE_SRV_RSP_OK if the tag
authenticity is verified, or HSE_SRV_RSP_VERIFY_FAILED it the authentication tag does not match with the
decrypted message. In both cases, the resulting decrypted message  can be retrieved by the host at memory
location pOutput (inputLength bytes to be read).
6.4.7  Signature generation and verification (RSA / ECC)
The host can request for the generation and the verification of signatures with different public-key based
algorithms as specified in Standards for Efficient Cryptography 1 (SEC1), PKCS #1: RSA Cryptography
Standard and Edwards-Curve Digital Signature Algorithm (EdDSA) via the service defined by the structure
hseSignSrv_t.
6.4.7.1  Algorithms
A message’s signature is the result of a cryptographic operation over the message’s digest using a private key
solely known to the entity producing the signature.
The first part of the service consists in calculating the message’s digest, which is the output of a (one-way) hash
primitive. This part of the service can be processed in streaming mode.
The second part of the service consists in:
• For a RSA signature: formatting the digest (e.g. padding)
• Computing the cryptographic operation
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
161 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 162

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.4.7.1.1  RSA signature
The message 
 is a byte array of any size.
The resulting signature  is a number such as 
, where  is the modulus of the private and public keys. The
size of  is equal to the size of .
For a given message 
 and a private RSA key 
, the RSA signature generation algorithm is:
For a given message 
, its signature  and a public RSA key 
, the RSA signature verification
algorithm is:
Two digest encoding schemes are supported in the HSE: PKCS1 V1.5 and PSS.
The PKCS1 V1.5 encoding function is defined as follows:
In the above, 
 is the DER encoded OID of the hash primitive used and 
 is a string of 0xFF
bytes to complement the size of the resulting value such as it aligns with the size of the modulus .
The PSS encoding function is defined as follows:
In the above, 
 is a random value of byte size 
, 
 is a mask generation function based on the
 primitive selected to calculate the message digest, and 
 is a string of 0x00 bytes with a byte
size such as the size of 
 is the size of the modulus  minus the size of  minus 1.
For more information, refer to PKCS #1: RSA Cryptography Standard.
6.4.7.1.2  ECDSA signature
An ECDSA signature can be computed on curves having a Weierstrass form.
The message 
 is a byte array of any size.
The resulting signature  is a number such as 
, where  is the order of the generator point . The size of 
equals the size of the private key 
.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
162 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 163

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The signature is provided with a verification point  that allows the authenticity check with the public key. Only
the  coordinate of  is provided (
). The size of 
 equals the size of the private key 
.
For a given message 
 and a private ECC key 
 on a Weierstrass curve  of generator point  of order , the
ECDSA signature generation algorithm is:
For a given message 
, its signature  with the verification point  and a public ECC point (key)  on a
Weierstrass curve  of generator point  of order , the ECDSA signature verification algorithm is:
For more information, refer to Standards for Efficient Cryptography 1 (SEC1).
6.4.7.1.3  EdDSA signature
An EdDSA signature can be computed on curves having a Twisted Edward form.
The message 
 is a byte array of any size.
The resulting signature  is a number such as 
, where  is the order of the generator point . The size of 
equals the size of the private key 
.
The signature is provided with a verification point  that allows the authenticity check with the public key.
For a given message 
 and a private ECC key 
 and the associated public point  on a Twisted Edward curve
 of generator point  of order , the EdDSA signature generation algorithm is:
 is provided in an encoded form. The size of 
 equals the size of the private key 
.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
163 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 164

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
For a given message 
, its signature  with the verification point  and a public ECC point (key)  on a Twisted
Edward curve  of generator point , the EdDSA signature verification algorithm is:
The point encoding function 
 is defined as follows:
In the above, 
 MSB is always 0, so the LSB of 
 becomes the MSB of 
. It should be also noted that the
public point  is always stored encoded in the HSE (see Key Values).
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
164 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 165

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The function 
 and the value  instantiate differently depending on the EdDSA signature mode selected, as
described in the below table.
EdDSA
signature mode
EdDSA signScheme configuration
“PureEdDSA”
signScheme.sch.eddsa.bHashEddsa
== FALSE
and
signScheme.sch. eddsa. context
Length/ pContext == 0
Note:  The message cannot be provided pre-
hashed (bInputIsHashed == FALSE)
.
“Context”
signScheme.sch.eddsa.bHashEddsa
== FALSE
and
signScheme.sch. eddsa. context
Length/ pContext != 0
Note:  The message cannot be provided pre-
hashed (bInputIsHashed == FALSE)
.
“HashEdDSA”
signScheme.sch.eddsa.bHashEddsa
== TRUE
Note: If
bInputIsHashed == TRUE, the input
message is pre-hashed and 
 is
not computed.
If bInputIsHashed == FALSE, the
 is not computed by the firmware.
Table 80. EdDSA parameter instances vs. the signature mode
The value  is a user-specified context. It has a maximum size of 255 bytes.
The 
 primitive and the value of 
 are defined by the selected Twisted Edward curve.
Twisted Edward Curve ID
HSE_EC_25519_ED25519
SHA512
"SigEd25519 no Ed25519 collision" (32 bytes)
Table 81. EdDSA parameters instances vs. the selected curve
For more information, refer to Edwards-Curve Digital Signature Algorithm (EdDSA).
6.4.7.2  Key selection
A signature is calculated over a message based on the knowledge of a secret key. A message’s signature
authenticity is verified using the corresponding public key.
The data field keyHandle specifies the key to be used. It must point to a valid and non-empty key.
The key type can be:
• HSE_KEY_TYPE_RSA_PAIR
• HSE_KEY_TYPE_RSA_PUB
• HSE_KEY_TYPE_RSA_PUB_EXT
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
165 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 166

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• HSE_KEY_TYPE_ECC_PAIR
• HSE_KEY_TYPE_ECC_PUB
• HSE_KEY_TYPE_ECC_PUB_EXT
The key type must align with the underlying signature algorithm selected, the operation selected (keys having
a private key part are the only one that can be used in signing operations), and its usage restriction must allow
a signature generation and/or verification (i.e. HSE_KF_USAGE_SIGN and/or HSE_KF_USAGE_VERIFY are
set).
If the signature operation is processed in streaming mode, the key handle must only be provided in the FINISH
call (data field ignored in START and FINISH calls).
6.4.7.3  Service configuration
The first part of the service consists in calculating the message’s digest. This part of the service can be
processed in streaming mode.
The second part of the service consists in formatting the digest (for RSA) and computing the cryptographic
operation. In streaming mode, these operations take place on the FINISH call, therefore the below data fields
must only be provided during the FINISH call (data fields ignored in START and UPDATE calls).
The data field signScheme specifies:
• The hash primitive (signScheme.hashAlgo) to compute the message’s digest and the digest formatting
when necessary
• The algorithm (signScheme.signSch) to generate or verify the signature:
– RSA with PKCS1 V1.5 digest formatting
– RSA with PSS digest formatting
– ECDSA using ECC keys lying on Weierstrass curves
– EdDSA using ECC keys lying on Twisted Edward curves
• Additional scheme parameters for the PSS encoding / decoding:
– signScheme.sch.rsaPSS.saltLength specifies the byte size of the random 
 used in the encoding
function; a typical value is 20 bytes.
• Additional scheme parameters for EdDSA:
– signScheme.sch. eddsa. bHashEddsa specifies whether to pre-hash the input message and perform
a HashEddsa signature
– signScheme.sch. eddsa. contextLength/ pContext specifies the EdDSA context;
contextLength set to zero means that a user context is not used
The data field signDir specifies the signature operation mode:
• HSE_AUTH_DIR_GENERATE indicates a signature generation: the HSE calculates a signature and returns it
to the host
• HSE_AUTH_DIR_VERIFY indicates a signature verification: the HSE verifies that the signature and the
message match
6.4.7.4  Input and output data
The data field pInput is:
• Either a pointer to the input message 
 over which the digest  is calculated
• Or a pointer to the pre-calculated digest ; in this case, the streaming mode is not supported and
bInputIsHashed must be set to TRUE.
For PureEDDSA, providing a pre-calculated digest in input is not possible (bInputIsHashed must be set to
FALSE)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
166 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 167

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
In addition:
• In one-pass mode, pInput is the pointer to the first byte of the message (or digest) to process, and the data
field inputLength specifies the number of bytes to be read from that memory location (that is, the entire
message size)
• In streaming mode, pInput is the pointer to the first or next message (or digest) chunk to process, and
inputLength is the byte size of that chunk
– inputLength can be provided for any streaming calls and must be multiple of hash-block length or zero for
START and UPDATE calls, and any value for FINISH call.
For a signature generation, the resulting signature is returned by the HSE at the memory location pointed by
pSignature[]:
• When using RSA as the signing algorithm, pSignature[0] is a pointer to the signature 
• When using ECDSA or EdDSA algorithms, pSignature[0] is a pointer to the coordinate 
 and
pSignature[1] is a pointer the signature . The length of each is the same as the length of the order n, of
the related ECC curve (important for curves where the length of n is greater than the length of p)
The data field pSignatureLength[] are pointers to 32-bit words:
• On service call, *pSignatureLength[0] (respectively *pSignatureLength[1]) must be set with the
size of the byte array pointed by pSignature[0] (respectively pSignature[1])
• Once the signature is generated by the HSE, *pSignatureLength[0] and *pSignatureLength[1]
are set with the number of bytes written by the HSE at the memory location pSignature[0] and
pSignature[1]
• In streaming mode, pSignature[] and pSignatureLength[] must be provided in the FINISH call (data
fields ignored in START and UPDATE calls)
For a signature verification, the message’s signature is provided by the pointers pSignature[]:
• When using RSA as the signing algorithm, pSignature[0] is a pointer to the signature 
• When using ECDSA or EdDSA algorithms, pSignature[0] is a pointer to the  coordinate of the verification
point  and pSignature[1] is a pointer to the signature 
• On service call, *pSignatureLength[0] (respectively *pSignatureLength[1]) must be set with the
size of the byte array pointed by pSignature[0] (respectively pSignature[1])
Signature scheme
inputLength
*pSignatureLength[0]
*pSignatureLength[1]
RSA
Any value
Not used
ECDSA or EdDSA
Any value
Table 82. Input and output size constraints on service call (RSA / ECC signature)
In the above table, 
 is the modulus size in bytes and  is the length of the order of the curve n, in bytes.
Note:  An EdDSA signature is expected and provided by the HSE as separate r and s components in big-
endian format. The conversion to and from a little-endian bit string must be performed by the host.
When the input message is scattered across multiple memory locations, this pInput can point to a scatter/
gather list as described in section Scatter Gather Input and Output. In this case, the data field sgtOption must
be set to HSE_SGT_OPTION_INPUT.
All memory locations provided in the service structure must be accessible by both the host and the HSE.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
167 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 168

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.4.7.5  Service result
Upon successful signature generation, the service terminates with the response HSE_SRV_RSP_OK and the
signature can be retrieved by the host at memory location pSignature[] (*pSignatureLength[] bytes to
be read).
Upon successful signature verification, the service terminates with the response HSE_SRV_RSP_OK if the
signature is found authentic, or with HSE_SRV_RSP_VERIFY_FAILED if the signature and the message do not
match.
6.4.8  RSA ciphering
The host can request for message encryption and decryption with the RSA algorithm as specified in PKCS #1:
RSA Cryptography Standard via the service defined by the structure hseRsaCipherSrv_t.
6.4.8.1  Algorithm
The RSA algorithm allows the encryption of a message using a public key, and the decryption using the
corresponding private key.
The message 
 and the ciphertext  are numbers such as 
 and 
, where  is the modulus of the
private and public keys.
For a given message 
 and a public RSA key 
, the RSA encryption algorithm is:
For a given ciphertext  and a private RSA key 
, the RSA decryption algorithm is:
The size of the encoded message 
 equals the size of the modulus . The size of the message 
 (
)
must be below the size of the modulus  augmented with the size of the additional padding imposed by the
encoding scheme.
Two message encoding schemes are supported in the HSE: PKCS1 V1.5 and OAEP.
The PKCS1 V1.5 encoding function is defined as follows:
In the above, 
 is a string of random bytes to complement the size of the resulting value such as it aligns
with the size of the modulus . Since 
 has a minimum size of 8 bytes, 
 must be below or equal to
the size of  minus 11 bytes.
Modulus size (key size)
Maximum input message size (
)
 bits
 bytes
1024 bits
117 bytes
Table 83. Maximum input message size (RSA encryption with PKCS1 V1.5 encoding)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
168 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 169

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Modulus size (key size)
Maximum input message size (
)
2048 bits
245 bytes
3072 bits
373 bytes
4096 bits
501 bytes
Table 83. Maximum input message size (RSA encryption with PKCS1 V1.5 encoding)...continued
The PSS encoding function is defined as follows:
In the above, 
 is a random value of byte size equal to the size of output of the selected 
 primitive,
 is an (optional) byte array of byte size 
, 
 is a mask generation function based on the
selected 
 primitive, and 
 is a string of 0x00 bytes with a certain byte size. 
 must be below
or equal to the size of  minus 2 times the hash length minus 2 bytes.
Modulus size (key size)
Digest size
Maximum input message size (
)
 bits
 bits
 bytes
2048 bits
256 bits
190 bytes
4096 bits
256 bits
446 bytes
2048 bits
512 bits
126 bytes
4096 bits
512 bits
382 bytes
Table 84. Maximum of input message (RSA encryption with OAEP encoding)
For more information, refer to PKCS #1: RSA Cryptography Standard.
6.4.8.2  Key selection
A RSA encryption uses a public key. The RSA decryption requires the knowledge of the corresponding secret
key.
The data field keyHandle specifies the key to be used. It must point to a valid and non-empty key.
The key type can be:
• HSE_KEY_TYPE_RSA_PAIR
• HSE_KEY_TYPE_RSA_PUB
• HSE_KEY_TYPE_RSA_PUB_EXT
The key type must align with the operation selected (keys having a private key part are the only one that
can be used in decryptions), and its usage restriction must allow for an encryption or decryption (i.e.
HSE_KF_USAGE_ENCRYPT and/or HSE_KF_USAGE_DECRYPT are set).
6.4.8.3  Service configuration
The data field rsaScheme specifies:
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
169 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 170

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• The message encoding / decoding scheme (rsaScheme.rsaAlgo):
– PKCS1 V1.5
– OAEP
– NO PADDING (the input is processed as an unsigned integer and perform a modular exponentiation)
• Additional parameters for the OAEP encoding:
– rsaScheme.rsaAlgo.rsaOAEP.hashAlgo specifies the hash primitive to use
– rsaScheme.rsaAlgo.rsaOAEP.pLabel provides a pointer to the (optional) 
 used in the encoding
sequence; rsaScheme.rsaAlgo.rsaOAEP.labelLength is 
; it can be 0
The data field cipherDir specifies the ciphering operation:
• HSE_CIPHER_DIR_ENCRYPT indicates an encryption operation
• HSE_CIPHER_DIR_DECRYPT indicates a decryption operation
6.4.8.4  Input and output data
The input message (either 
 or ) is provided via the data field pInput, which is the pointer to the first byte
of the message to process. The data field inputLength specifies the number of bytes to be read from that
memory location.
• For an encryption, it must be below the modulus size augmented with the size of the additional padding
imposed by the encoding scheme (see below table)
• For a decryption, inputLength must equal the modulus size
The result of the encryption or decryption operation is returned by the HSE at the memory location pointed by
pOutput.
• The data field pOutputLength is a pointer to a 32-bit word
• On service call, *pOutputLength must be set with the size of the byte array pointed by pOutput; it must be
at least equal to the key size (i.e. the size of the modulus)
• Once the encryption or decryption operation is completed by the HSE, *pOutputLength is set with the
number of bytes written by the HSE at memory location pOutput
The below table summarizes the conditions on the input and output sizes when calling the service.
Operation (cipherDir)
Encoding scheme (rsaAlgo)
inputLength
*pOutputLength
PKCS1 V1.5
OAEP
Encryption
NO PADDING
Decryption
PKCS1 V1.5 or OAEP or NO
PADDING
Table 85. Input and output size constraints on service call (RSA ciphering)
In the above table, 
 is the modulus size in bytes and 
 is the digest size in bytes.
All memory locations provided in the service structure must be accessible by both the host and the HSE.
6.4.8.5  Service result
Upon successful operation, the service terminates with the response HSE_SRV_RSP_OK. The resulting
encrypted or decrypted message can be retrieved by the host at memory location pOutput (*pOutputLength
bytes to be read).
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
170 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 171

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.5  Random number generation
The host can request for the generation of random numbers via the service defined by the structure
hseGetRandomNumSrv_t.
6.5.1  Generalities
The generation of random numbers involves:
• The use of a hardware source of entropy to generate a true-random seed; this source must be designed as
such that its output cannot be predicted nor influenced
• A generation function that takes in input the true-random seed and outputs random numbers
The hardware source of entropy ensures non-determinism on the true-random seed.
The true-random seed generation, also referred to as seeding, separates from the actual generation of
random numbers because it requires a high number of iterations and checks that are time-consuming and not
compatible with most of the use cases where random numbers are required.
The generation of random numbers is based on a cryptographic function which is fast but also introduces a
deterministic factor. This means that after a certain quantity of random number generated, the true-random
source must change: this process is referred to as reseeding.
6.5.2  Implementation
In the HSE, the source of entropy is provided by its TRNG, and the generation function is part of a Deterministic
Random Number Generator (DRNG, aka DRBG or PRNG) module as specified in Recommendation for
Random Number Generation Using Deterministic Random Bit Generators.
Figure 65. Random number generation: high-level view
The TRNG is not directly accessible to the host but used by the DRNG for the generation of the true-random
seed. This process is triggered:
• By POR or system reset: this is the initial instantiation
• By the generation function: this is the reseeding
The reseeding frequency is defined as one input of the service request (see below).
It is possible to test the reseeding function via one of the self-test functions available to the host.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
171 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 172

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The generation function is the Hash_DRBG as documented in Recommendation for Random Number
Generation Using Deterministic Random Bit Generators.
6.5.3  Service configuration
The data field rngClass specifies the reseeding frequency in the DRNG as documented in the below table.
rngClass
Reseeding frequency
HSE_RNG_CLASS_DRG3
Reseeds every 1 000 000 service calls.
This is the most efficient class in terms of performance.
HSE_RNG_CLASS_DRG4
Reseeds on every service call.
It complies with the AIS-20/SP800-90A specification
HSE_RNG_CLASS_PTG3
Reseeds before the first generation and after every 16 bytes generated during the
execution of the service request.
It complies with the AIS 31/SP800-90B specification. This is the most costly class
in terms of performance.
Table 86. RNG Classes
To generate random numbers in the fastest possible way, set rngClass to HSE_RNG_CLASS_DRG3.
To generate random numbers with the highest level of non-determinism set rngClass to
HSE_RNG_CLASS_PTG3.
6.5.4  Input and output data
The random numbers are returned by the HSE at the memory location pointed by the data field pRandomNum.
This memory location must be accessible by both the host and the HSE.
The data field randomNumLength defines the number of random bytes to be generated and returned. It cannot
be set to 0.
6.5.5  Potential error
At runtime, the service that requires a random number may terminate with the error
HSE_SRV_RSP_GENERAL_ERROR and the HSE_STATUS_RNG_INIT_OK status flag will be cleared to 0.
In this case, the true-random seed is unavailable to the DRNG module, which cannot generate the random
numbers as requested by the application.
In such situation, when the HSE_STATUS_RNG_INIT_OK status flag is 0, the call of any service that
requires a random number (e.g. Get Random Number, ECDSA signature generate etc.) triggers a RNG re-
initialization before requesting the random number. If the RNG re-initialization is executed successfully, the
HSE_STATUS_RNG_INIT_OK status flag is set to 1.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
172 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 173

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
7   Secure Boot and Memory Verification Services
7.1  Types of secure boot
The HSE firmware supports three types of secure boot:
1. Advanced secure boot (aka SMR-based secure boot):
• It supports booting single or multiple cores
• It is based on SMR (Secure Memory Region) and CR (Core Reset) configuration
• It supports symmetric authentication schemes (AES-CMAC, GMAC, HMAC and so on)
• It supports RSA, ECDSA, and EDDSA signature verification schemes.
2. SHE-based secure boot (refer to SHE Based Secure Boot SMR):
• It emulates the secure boot operation specified by SHE protocol.
• Only one application core can be released from reset.
• SHE supports only the CMAC based authentication scheme with the BOOT_MAC_KEY key.
• It is a variant of SMR-based secure boot that uses the first SMR entry (entry index 0). The HSE firmware
identifies the SHE secure boot by reading the key handle in the SMR#0. If the key handle of SMR#0 is the
SHE BOOT_MAC_KEY key, then HSE Firmware initiates a SHE secure boot.
3. Basic Secure Boot (aka IVT-based secure boot):
• It supports booting one target core (AppBL).
• It can be used only if the SMR-based secure boot is not available (there is no Core Reset entry
configured).
• All parameters (except for the ADKP) are configured in the IVT. Application related parameters, such as
entry pointer and size, are allocated in the AppBL header. There is no need to update the HSE SYS_IMG.
The AppBL structure is described by AppBL Structure.
• The AppBL image (provide in the IVT) can be authenticated using a GMAC tag computed using a key
derived from ADKP (refer to Authenticate Host System Images). The tag (GMAC) must be calculated over
the whole image including the header. It can be done either using the hseBootDataImageSignSrv_t
service (refer to Authenticate Host System Images), or by an offline tool. When using offline tool, random
IV must be selected by user. The random IV and tag must be added to the tail of the AppBL image.
Important:
If the SMRs are configured along with the Basic Secure Boot (AppBL is configured), and at start-up, the SYS-
IMG loading fails (SMRs are not available) or no CR entry is present, the application core is still started using
the AppBL image. The AppBL image can be seen as a recovery image.
To authenticate the host system images such as IVT, the IVT_AUTH attribute must be set using the
HSE_ENABLE_BOOT_AUTH_ATTR_ID attribute. The authentication tag for these images can be computed by an
offline tool or using the hseBootDataImageSignSrv_t service (refer to Authenticate Host System Images ).
7.2  Memory Verification Services
The memory verification services are available for the host to secure the start-up of one or several application
images for one or several CPU subsystems. This process is also referred to as “secure boot” (of the application
image(s)).
The secure memory regions (SMR) managed by these services offer the possibility to apply different types
of sanctions when the secure boot is failing. The platform supports a wide variety of authentication schemes
(MAC, RSA / ECC signatures) to verify the application images, as well as encryption schemes (AEAD-GCM,
AES-CTR) which provide image confidentiality and can accelerate the verification time at start-up by relying on
authenticity checks performed by the HSE.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
173 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 174

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
In addition, the memory verification services can be used to trigger automatic and recurrent SMR verification
operations during run-time.
7.3  System overview
A secure memory region (SMR) is defined by a start address and a size, associated with a proof of authenticity,
either a MAC or an RSA/ECC signature, which authenticates the region’s content.
The host can define up to 8 SMR clustered into the SMR table. It must also provide the proof of authenticity for
each memory region content (except for one specific region: see details in this chapter).
For all SMR that have been defined, the HSE verifies the authenticity of memory contents:
• During the device start-up phase (after reset)
• While the application(s) is(are) running on the host side (during run-time)
The SMR verification results translate into sanctions imposed on the system by the HSE:
• Unsuccessful verification can keep select subsystems on the host side in reset state; those subsystems are
referenced in the Core Reset (CR) table
• Likewise, failing to verify certain SMR can render selected keys within the HSE unusable; these restrictions
are defined individually for each key via the SMR verification map
S32x (host)
HSE
SYS-IMG
Application 
CPU
subsystem
Application 
CPU
subsystem
Application 
CPU
subsystem
SMR Table
Application Memory
SMR #0
SMR #8
addr
size
config
addr
size
config
addr
size
config
SMR verification status (8 bits)
CR Table
Core ID
reset vec
SMR entries
Core ID
reset vec
SMR entries
authenticity proof
authenticity proof
measures
verifies
releases
from reset
Key catalog NVM
Key catalog RAM
allows/restricts
usage
Figure 66. Illustrating the memory verification service (SMR)
7.4  Principle of operation
The memory verification services are made of:
• The SMR installation service
• The SMR verification service
• The Core Reset table installation service
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
174 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 175

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
With the SMR installation service, the host:
• Defines each of the secure memory region (SMR) to be subsequently verified (up to 8)
• Provides, for each SMR, an initial authenticity proof which is verified by the HSE; when successful, it triggers
the calculation of a reference authenticity proof (one for each SMR) only known by the HSE
• Configures how and when the subsequent verification process is triggered (either by the HSE independently
from the host, or by the host itself)
The SMR verification service consists in the HSE verifying the initial or reference authenticity proof calculated
during the installation process and taking actions towards the host based on the verification result.
Application Memory
SMR #i
Initial authenticity
proof (for SMR #i)
HSE
SYS-IMG
Reference authenticity 
proof(for SMR #i)
SMR installation 
process
SMR verification 
process
measures
verifies
measures
verifies
generates
alternate verification(optional)



1
2
2
Figure 67. Illustrating the SMR installation and verification processes
When BOOT_SEQ equals 1, the verification service is automatically triggered at start-up (after reset), and the
verification successes link with the reset release of certain subsystems, which are associated with SMR in the
Core Reset (CR) table installed by the host via another specific service.
The verification status of each SMR can also be associated with each individual key declared in the NVM key
catalog via the SMR verification map: in this 32-bit word, bit #i (with i between 0 and 7) is set to 1 by the host
(during key provisioning) to indicate that the SMR #i must be successfully verified before the key can be used.
The initial authentication scheme is defined by the host. The memory content can be verified against an
authentication tag (a MAC) or an RSA/ECC signature.
During the verification process, the HSE uses either the initial authentication scheme as defined by the host,
or its own scheme to verify the reference authenticity proof internally calculated during the installation process.
This selection is done by the host during the installation. Using the internal authentication method improves the
verification response timing against a public-key based authentication scheme.
7.5  System tables
The memory verification services are using two tables that are part of SYS-IMG. For devices with internal flash
the SYS-IMG is stored in HSE secure data flash.
7.5.1  SMR table
The SMR table allows the host to define up to 8 memory regions and associate each one with an installation
and a verification method.
Each SMR entry in the SMR table holds a set of attributes listed in the below table.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
175 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 176

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Attribute
Data field
Description
Source address
pSmrSrc
A pointer to the memory region to be verified.
Size
smrSize
A 32-bit integer that provides the size in bytes of the memory
region to be verified.
Destination address
pSmrDest
A pointer where the memory region is copied before verification.
Initial authenticity proof
pInstAuthTag[]
Pointers to the initial authenticity proof of the memory region,
that can be used in the verification process if the flag HSE_
SMR_CFG_FLAG_INSTALL_AUTH is set. If used, must be a
valid address in Application memory.
Authentication scheme
authScheme
The initial authentication scheme used to authenticate the
memory region.
The proof of authenticity can be an authentication tag (that is, a
Message Authentication Code (MAC)) or a public key signature
scheme (that is, RSA or ECC signature).
Authentication key
authKeyHandle
The handle to the authentication key, which must:
• Be declared in a key group in the NVM key catalog
• Refer to a non-empty key slot having its key usage flag HSE_
KF_USAGE_VERIFY set while HSE_KF_USAGE_SIGN flag
must not be set
• Refer to a key type that matches with the initial authentication
scheme selected
Decryption parameters
smrDecrypt
Optional parameters for SMR decryption when an encrypted
SMR is installed. More details in SMR decryption parameters.
Verification period
checkPeriod
A 32-bits integer that defines the scaled number of system clock
cycles between two consecutive verification process (more
details in section Recurrent Automatic SMR Verification.
SMR configuration flags
configFlags
A binary OR combination of configuration flags between a
memory interface and the authenticity proof used for verification,
as specified in Additional SMR configuration flags.
Version Offset
versionOffset
The offset in SMR where the image version can be found. The
SMR version offers protection for the image against rollback
attacks during update. The version offset must be aligned to 4
bytes and the version value is a 32-bit value. If the version offset
is different than zero, during SMR update/installation, the version
value must be greater than the previous one. If the version offset
is zero, it means that the SMR does not include a version (SMR
is not protected against rollback attacks).
Table 87. SMR table entry attributes
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
176 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 177

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Attribute
Data field
Description
Decryption key
decryptKeyHandle
The handle to the decryption key. If set to HSE_SMR_
DECRYPT_KEY_HANDLE_NOT_USED, the image is not
decrypted and all decryption parameters are ignored. If used,
the key must:
• Be declared in an AES key group in the NVM key catalog
• Refer to a non-empty key slot having its keyusage flag
HSE_KF_USAGE_SMR_DECRYPT set and block modes
0, AEAD-GCM or AES-CTR.
GMAC tag
pGmacTag
Pointer in application memory to the GMAC tag over the
encrypted image. If provided, the image must be encrypted
using AEAD-GCM with AAD (if is not zero) and the generated
tag must be stored to this location. If used, it must be a valid
address in application memory.
If not provided, the application must be encrypted using AES-
CTR. In this case, HSE generates internally an integrity hash
over the encrypted image.
HSE always verifies the integrity/authenticity of the encrypted
image before decrypting it.
AAD length
aadLength
The length in bytes of the Authenticated Additional Data
(AAD). It is used only if the pGmacTag tag is provided.
It can be 0 (not used), 64 bytes or 128 bytes.
Additional Authenticated
Data
pAAD
Pointer to AAD data used with AEAD-GCM operation.
It is ignored if aadLength is set to zero.
Table 88. SMR decryption parameters
Config Flags
SMR configuration
HSE_SMR_CFG_FLAG_QSPI_FLASH
N/A
HSE_SMR_CFG_FLAG_SD_FLASH
N/A
HSE_SMR_CFG_FLAG_MMC_FLASH
N/A
HSE_SMR_CFG_FLAG_INSTALL_AUTH
Use the initial authenticity proof provided by the host during the SMR
installation process in the subsequent SMR verification process.
HSE_SMR_CFG_FLAG_AUTH_AAD
When it is set, the SMR must be configured to use AEAD_GCM
decryption (for example, AAD and GMAC tag are provided) and the
authentication is computed over “AAD || Plain SMR” image.
When is not set, the authentication is computed over the SMR in
plain.
Table 89. Additional SMR configuration flags
The content of the memory region to be verified is provided by the data field pSmrSrc. This source address can
point to any memory area in the host domain (i.e. outside of the HSE subsystem) that is directly readable by the
HSE. For the devices with internal flash, the data field configFlags identifies the authenticity scheme only.
Alternatively, pSmrDest specifies a valid SRAM address where the SMR content is to be copied by the HSE
before it is verified.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
177 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 178

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Figure 68. SMR table configuration example (S32K3)
When checkPeriod is set to a value different from 0, the SMR is also verified during run-time. checkPeriod
defines the interval of time between two verification processes. The value provided is a number of system clock
cycles. For more details, see the subsequent sections in this chapter.
7.5.2  Core Reset table
The Core Reset (CR) table allows the host to associate each CPU-driven subsystem available in a device with
up to 8 SMR, so that sanctions are applied on those subsystems after the pre-boot and post-boot phases,
depending on the SMR verification status. For the devices with internal flash, the user can install maximum 4
core reset entry depending on the availability of the application core on the device.
Each entry in the CR table holds a set of attributes listed in the below table.
Attribute
Data field
Description
Core identifier
coreId
A unique number that identifies a CPU-driven subsystem.
Pre-boot SMR verification
map
preBootSmrMap
A set of flags that define which SMR, indexed from 0 to 7 (bit #i for
SMR #i), must be verified before releasing from reset the associated
subsystem.
Alternate Pre-boot SMR
verification map
altPreBootSmr
Map
A set of flags that define which SMR, indexed from 0 to 7 (bit #i for
SMR #i), must be verified before releasing from reset the associated
subsystem when one or more SMR specified in preBootSmrMap
failed the verification. This can be used to declare backup image(s)
for the associated CPU subsystem. This field can be set only if pre
BootSmrMap is set (that is, not used for parallel secure boot).
Post-boot SMR
verification map
postBootSmrMap
A set of flags that define which SMR, indexed from 0 to 7 (bit #i for
SMR #i), must be verified after releasing from reset the associated
subsystem.
Table 90. CR table entry attributes
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
178 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 179

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Attribute
Data field
Description
Reset address
pPassReset
A Value of the VTOR of associated application subsystem
• Either after a successful verification of all SMR specified in pre
BootSmrMap. This address must lie within one of the verified SMR.
• Or unconditionally, if there are no SMR specified in preBoot
SmrMap, but they are linked through postBootSmrMap to the
core reset entry. This is known as parallel secure boot and the
verification is done after the core is released from reset. This
address must lie within one of the loaded SMR.
Alternate reset address
pAltReset
Value of the VTOR of an associated application subsystem if all the
SMR defined in altSmrVerifMap pass the verification.
Core boot option
startOption
Specifies whether the core is automatically started by the HSE at
boot-time or if the CR entry is used for on-demand booting at run-
time.
Sanctions on failed
verification
crSanction
The sanction HSE applies for the CR entry if one of the associated
SMR fails verification. See Sanctions on pre-boot and post-boot
phases.
Table 90. CR table entry attributes...continued
crSanction
Sanction
HSE_CR_SANCTION_KEEP_CORE_IN_RESET
Keep the associated subsystem in reset.
HSE_CR_SANCTION_RESET_SOC
Reset the device.
HSE_CR_SANCTION_DIS_ALL_KEYS
Disable the usage of all keys.
HSE_CR_SANCTION_DIS_INDIV_KEYS
Disable the usage of selected keys via the key attribute smr
Flags. This represents the default sanction.
Table 91. Sanctions on pre-boot and post-boot phases
Each CPU-driven subsystem is identified by a unique number (coreId). See Device Specific Parameters
(S32K3xx) for the list of available subsystems and their respective identifier in a specific device.
The association of a CPU subsystem with a set of SMR is realized via the data fields preBootSmrMap,
altPreBootSmrMap and postBootSmrMap: when bit #i is set to 1, SMR #i is associated with that CPU
subsystem. The associated SMR entries have to be installed prior to installing the CR entry they are linked to.
The verification of the associated SMR is done:
• Either while the CPU subsystem is kept in reset and the associated SMR is specified in preBootSmrMap or
altPreBootSmrMap data fields.
• Or after the CPU subsystem has been released from reset and the associated SMR is specified in the
postBootSmrMap data field.
When an SMR failed the verification, a sanction applies to the associated subsystem as defined by the data
field crSanction.
The reset address provided in the data field pPassReset and pAltReset can be an address within the on-
chip Flash .
The address pPassReset must lie within one of the SMR listed in preBootSmrMap or postBootSmrMap.
Similarly, the address pAltReset must lie within one of the SMR listed in altPreBootSmrMap.
Important:  If a CPU subsystem is not listed in the Core Reset table, it is not released from reset by the HSE.
For more details, see the subsequent sections in this chapter.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
179 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 180

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
7.6  SMR installation
The host can request for SMR installation via the service defined by the structure
hseSmrEntryInstallSrv_t.
The SMR installation consists in:
• Defining the SMR attributes for each SMR entry
• Providing a proof of authenticity over the SMR content
• Optionally, encrypting the SMR content and providing a proof of authenticity over the encrypted content
7.6.1  SMR installation conditions
The first-time definition of a SMR entry can be performed when LC is set to CUST_DEL.
In addition, when the host is granted with User rights, the following SMR entries cannot be modified:
• authKeyHandle
• authScheme
• configFlags
• checkPeriod
• pSmrDest
• smrDecrypt
• versionOffset
To modify the values of the above data fields in a SMR entry already defined, the host must be granted with SU
rights.
All other data fields in the SMR entry (such as pSmrSrc, smrSize and pInstAuthTag[]) can be updated
unconditionally.
7.6.2  SMR installation attributes
The SMR installation service takes as input:
• An SMR number between 0 and 7 via the data field entryIndex
• A set of attributes via the data field pSmrEntry that holds the SMR entry as listed in SMR table
• The installation mode (see next section)
Important:
The address pSmrData can be equal to pSmrEntry#pSmrSrc and pAuthTag[] can be equal to
pSmrEntry#pInstAuthTag[] as long as these are pointing in internal flash memory.
7.6.3  SMR installation options
7.6.3.1  One-pass installation mode
When the SMR content to install is fully available in Flash or RAM, the most convenient way to process it is to
run the service in one-pass mode.
In this case:
• The data field accessMode must be set to HSE_ACCESS_MODE_ONE_PASS
• pSmrData must be set with the start address of the SMR content
• smrDataLength must be equal to pSmrEntry➔smrSize, that this the entire size of the SMR
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
180 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 181

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• The address (pAuthTag[]) and size (pAuthTagLength[]) of the initial authenticity proof must be provided
along with the address content (see next section for details)
7.6.3.2  Streaming installation mode
It is possible to process a SMR installation even if the entire content is not already programmed in Flash or
RAM. A typical example for such use case is an image (code or data) that is too big to fit in the available
application RAM entirely and is provided to the host in chunks via a communication interface, and each
individual chunk is then programmed in Flash.
In this case, the SMR is installed in streaming mode:
• The SMR number (entryIndex), configuration (pSmrEntry) and decryption initialization vector
(cipher.pIV) must be provided only in the START call.
• For the START, UPDATE or FINISH calls, pSmrData must point to the next SMR chunk to process and
smrDataLength is set with the size of that chunk. The minimum chunk size is 64 bytes.
• The START and FINISH calls are mandatory, the UPDATE call is optional.
• The address (pAuthTag[]) and size (authTagLength[]) of the initial authenticity proof must only be
provided during the FINISH call (see next section for details).
7.6.3.3  Non-reentrant service
A new SMR can be installed only if there is no on-going installation of a previous SMR:
• By default, when no SMR installation has been requested.
• Previous SMR was processed in one-pass mode.
• Previous SMR was processed in streaming mode and finished with a successful FINISH call or an error in any
of the other calls.
7.6.4  Initial SMR authentication
7.6.4.1  General use
The array pAuthTag[] provides the pointers to the initial authenticity proof verified by the HSE during the
installation process. When the authentication is successful, the SMR is installed and can be subsequently
verified.
The initial authenticity proof is optional when LC is set to CUST_DEL and when the entryIndex equals 0 (see
next section). In all the other cases, the initial authenticity proof must be provided by the host to terminate the
installation and trigger the calculation of a reference authenticity proof. In streaming mode, this data field must
only be provided during the FINISH call.
The data field pSmrEntry➔authScheme provides the type of authentication scheme selected by the host for
this initial SMR authentication, and indicates what value are pointed by pAuthTag[]:
• When the initial authenticity proof is an authentication tag, pAuthTag[0] is the pointer to the MAC calculated
over the SMR content. The authTagLength[0] must be at least 16 bytes.
• When the initial authenticity proof is a RSA signature, pAuthTag[0] is the pointer to that signature calculated
over the SMR content.
• When the initial authenticity proof is an ECC signature, pAuthTag[0] is the pointer to the x coordinate of the
verification point (also called R), and pAuthTag[1] is the pointer to the signature (also called S) calculated
over the SMR content. The size of S and R (authTagLength[0]) and authTagLength[1]) must match
the ECC key size in bytes (that is, for an ECC key of 256 bits, the size of R and S must be 32 bytes).
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
181 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 182

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
When HSE_SMR_CFG_FLAG_INSTALL_AUTH is set in the data field pSmrEntry➔configFlags,
pSmrEntry➔pInstAuthTag[] must be used similarly to pAuthTag[], pointing to the same authentication
proof value, but in internal Flash memory.
For more information on the MAC algorithms supported by the HSE, refer to section Mac Generation and
Verification. For more information on the signature algorithms supported by the HSE, refer to section Signature
Generation and Verification (RSA/ECC).
The key to be used by the HSE to verify the initial authenticity proof is provided by the data field
pSmrEntry➔authKeyHandle. The key type of the selected key must align with the authentication scheme
selected (pSmrEntry➔authScheme). In addition, the key must be stored in the NVM key catalog, its key
usage flag HSE_KF_USAGE_VERIFY should be set while the flag HSE_KF_USAGE_KEY_SIGN must not be set.
The SMR can be optionally encrypted and authenticated, depending on the value of the
pSmrEntry➔smrDecrypt.decryptKeyHandle. If used, the decryption key must be an AES key stored in
the NVM key catalog and have its key usage key flag HSE_KF_USAGE_SMR_DECRYPT set. The initialization
vector for the cipher operation is provided at installation time via the cipher.pIV data field and is copied
internally by the HSE.
Additional to the SMR encrypted content, an authentication tag over the encrypted image may be provided
using cipher.pGmacTag data field (and pSmrEntry➔smrDecrypt.pGmacTag). If the GMAC tag
is provided, the SMR must be encrypted using the AEAD-GCM algorithm with null AAD . In case the
authentication proof over the encrypted SMR is not provided, the algorithm used for encryption must be AES-
CTR and HSE generates internally an integrity hash over the encrypted SMR that is used for verification.
7.6.4.2  Specific use (SMR #0)
The SMR #0 is the only SMR that can be associated with the SHE AES key BOOT_MAC_KEY as the SMR
authentication key. In this case, the reference authentication tag is the CMAC value referred to as BOOT_MAC.
The BOOT_MAC value can be initialized and updated via the SHE key update protocol (see section SHE Key
Provisioning.
In addition, when host is granted with SU rights, BOOT_MAC can be automatically calculated as described
below.
On the first SMR #0 installation using BOOT_MAC_KEY, if BOOT_MAC is empty (that is, not initialized) and
if BOOT_MAC_KEY has been provisioned, the reference authentication tag is calculated by the HSE and
saved in BOOT_MAC. This specific installation process satisfies the requirement in SHE – Secure Hardware
Extension Functional Specification referred to as “autonomous bootstrap configuration”.
Important:
The input message for the BOOT_MAC calculation in the HSE is the concatenation of:
- A 128-bit block consisting of 96 bits with the value 0 followed by 32 bits encoding the size N of SMR #0 in big-
endian format and in bits (for example, if the size N of SMR #0 is 4 660 bytes, the first 128-bit block equals to
0x000000000000000000000000000091A0)
- N consecutive bytes representing the content of SMR #0
When installing SMR #0 using the BOOT_MAC_KEY while the BOOT_MAC is already initialized, the
BOOT_MAC value must be updated via the SHE key update protocol prior to issuing the SMR installation
service.
In all cases, the data fields pAuthTag[] and pAuthTagLength[] are always discarded and should be set
respectively to NULL and 0.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
182 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 183

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Figure 69. SMR Installation for SHE
7.6.5  SMR installation result
Upon successful installation, the HSE saves the entry in the SMR table and calculates a reference authenticity
proof that can be used in subsequent SMR verification process. This process ensures the fastest response time
on SMR verification to be performed at start-up.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
183 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 184

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
However, the host may decide to have the HSE always verify the initial authenticity proof. In this case, the
flag HSE_SMR_CFG_FLAG_INSTALL_AUTH must be set in pSmrEntry➔configFlags and the data field
pInstAuthTag[] must be set with the pointers to the proof of authenticity provided during installation.
SYS-IMG is modified only once the SMR content has been successfully verified. This is to preserve an SMR
entry during an update operation in case the SMR installation fails.
7.7  Core Reset table installation
The host can request for installing an entry in the Core Reset (CR) table via the service defined by the structure
hseCrEntryInstallSrv_t.
7.7.1  CR table entry installation conditions
The first-time definition of a CR entry can be performed when LC is set to CUST_DEL.
Once defined, a CR entry can be updated only when all the associated SMR have been successfully verified
first.
In addition, to modify any of the values in a CR entry already defined, the host must be granted with SU rights.
7.7.2  CR table entry attributes
The CR table entry installation takes in input:
• A CR entry number between 0 and (HSE_NUM_OF_CORE_RESET_ENTRIES - 1) via the data field
crEntryIndex. HSE_NUM_OF_CORE_RESET_ENTRIES is defined in HSE header files.
• A set of attributes via the data field pCrEntry that holds the CR table entry attributes as listed in Core reset
table.
The data fields pCrEntry➔pPassReset and pCrEntry➔pAltReset can only be a valid address in on-chip
Flash.
At least one SMR should be linked to the CR entry via pCrEntry➔preBootSmrMap or
pCrEntry➔postBootSmrMap data fields.
Note:
The interface files are generic for all S32K3xx devices. The number of cores for specific device must be referred
from S32K3xx Reference Manual.
7.7.3  CR table entry installation result
Upon successful installation, the HSE saves the entry in the CR table.
7.7.4  Core Reset table update
The host can request for erasing an entry in the Core Reset (CR) table via the service defined by the structure
hseCrEntryEraseSrv_t. Before calling this service, the host must be granted with SU rights.
7.8  SMR verification
At start-up, all SMR declared in the SMR table are unverified.
The verification process for a specific SMR is triggered by the host or automatically by the HSE depending
on how the SMR are linked to the CR entries during installation phase via pCrEntry➔preBootSmrMap,
pCrEntry➔altPreBootSmrMap or pCrEntry➔postBootSmrMap data fields.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
184 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 185

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
7.8.1  Encrypted SMR
If an SMR is encrypted using smrEntry.smrDecrypt data field, HSE verifies firstly the authenticity of the
encrypted content (i.e. the GMAC tag if provided at installation time or the internal generated integrity hash).
Upon successful verification of the encrypted SMR authenticity, HSE proceeds with decrypting the SMR content
at the valid address in RAM specified by smrEntry.pSmrDest data field.
In all cases, when SMR destination is specified via smrEntry.pSmrDest data field, the authentication of the
plain SMR is performed in RAM, after the content is copied (and optionally decrypted) from the source address
in the Flash (smrEntry.pSmrSrc). Note that for encrypted SMR entries smrEntry.pSmrDest data field must
be set to a valid RAM address.
The smrEntry.pAAD field can be used to specify the location of additional plain data that can be used if the
SMR is encrypted using AEAD-GCM (e.g. as a header containing meta-data about the image). This is included
in the encrypted image authentication by default and by setting the HSE_SMR_CFG_FLAG_AUTH_AAD
configuration flag, it is also included in the authentication of the plain image (that is, after decryption).
7.8.2  Authenticity proof
In the verification process, the plain SMR content is verified:
• Either against the reference authenticity proof calculated by the HSE upon successful completion of the
installation process: this is the default verification process, designed to be as fast as possible
• Or against the initial authenticity proof provided by the host during the installation process: to enforce such
verification, HSE_SMR_CFG_FLAG_INSTALL_AUTH must be set in pSmrEntry->configFlags and
pInstAuthTag[] must include pointers to the proof of authenticity in Flash memory provided during
installation
7.8.3  Memory region verified
If a SMR destination address (data field smrEntry.pSmrDest) is set with a valid RAM address, the SMR
content at address smrEntry.pSmrSrc is first copied to that RAM space, before it is verified by the HSE from
that RAM address.
The HSE does not carry-out any decryption process during the copy to RAM.
7.8.4  On-demand SMR verification
SMR entries which are not linked to the CR table are unverified until the host triggers, at run-time, the
verification via the service defined by the structure hseSmrVerifySrv_t or until HSE triggers the verification
automatically if checkPeriod is different from 0.
This service takes two data fields: entryIndex that specifies the index of the SMR to verify and options as
described in the below table.
Option
Description
HSE_SMR_VERIFICATION_OPTION_NONE
Default verification of the SMR at run-time
HSE_SMR_VERIFICATION_OPTION_NO_LOAD
SMR is verified from flash (using pSmrSrc address) even
if pSmrDest is specified or if already loaded. Can be used
only, if SMR is in a flash. Additionally the SMR cannot be
encrypted.
HSE_SMR_VERIFICATION_OPTION_RELOAD
SMR is loaded from the flash and verified even if it is already
loaded. Can be used only if SMR is in a flash.
Table 92. Options in hseSmrVerifySrv_t
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
185 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 186

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Option
Description
HSE_SMR_VERIFICATION_OPTION_PASSIVE_MEM
Only for HSE_B with AB_Swap Configuration. Verifies the
SMR from the passive block, applying address translation to
pSmrSrc and pInstAuthTag[0]/pInstAuthTag[1].
Table 92. Options in hseSmrVerifySrv_t...continued
This service can also be used to verify any SMR during run-time. However, when the SMR to verify is in Flash,
it must be ensured that no concurrent programming operation is triggered by the host while the verification
takes place. See section Memory Location for more details on the memory location of a SMR depending on its
verification method and verification status.
7.8.4.1  Application and SMR update steps in AB_SWAP configuration
This section explains the steps that should be followed to update the application or rollback to its previous
version.
The updated application is programmed in the passive partition.
1. If already installed SMRs are modified because of this update, then all the modified SMRs needs to be
updated using hseSmrEntryInstallSrv_t.
2. SMR entries are updated with:
a. pSmrData pointing to an address in the passive partition and pSmrSrc pointing to an address in active
partition.
b. pAuthTag[0]/pAuthTag[1] pointing to an address in the passive partition and pInstAuthTag[0]/
pInstAuthTag[1] pointing to an address in active partition.
c. Optionally, if SMR is encrypted and authenticated, cipher.pGmacTag and cipher.pAAD data field
pointing to an address in the passive partition. Whereas, SmrEntry→smrDecrypt.pGmacTag and
pSmrEntry→smrDecrypt.pAAD pointing to an address in active partition.
This is illustrated as shown in the diagram below.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
186 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 187

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
0x00400000
0x007FFFFF
0x007D4000
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
0x005D4000
0x005FFFFF
SMR update
SMR region v1
Application v1
Active 
Partition
(Lower 
Address)
Passive
Partition
(Higher 
Address)
0x00400000
0x007FFFFF
0x007D4000
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
0x005D4000
0x005FFFFF
SMR Installation
SMR region v1
Application v1
Application v2
SMR region v2
Addresses in hseSmrEntryInstallSrv_t 
[2**] points to addresses in passive 
partition
Addresses in hseSmrEntry_t [1*] 
points to addresses in active partition
Customer wants to perform application 
update, Update SMR and application v2  in 
passive partition  
Application & SMR v1 configured in In 
active partition
Active 
Partition
(Lower 
Address)
Passive
Partition
(Higher 
Address)
[1*]: pSmrSrc/pInstAuthTag[0]/pInstAuthTag[1]/
pSmrEntry→smrDecrypt.pGmacTag/
pSmrEntry→smrDecrypt.pAAD
[2**]: pSmrData/pAuthTag[0]/pAuthTag[1]/
cipher.pGmacTag/cipher.pAAD    
Figure 70. Application and SMR update scenario
Before activating the passive partition, the SMR verification fails on the updated SMR as its contents on
pSmrSrc/pInstAuthTag[0]/pInstAuthTag[1] (active partition) and corresponding pSmrData/
pAuthTag[0]/pAuthTag[1] (passive partition) addresses are different. The below figure illustrates an SMR
verification failure use case.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
187 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 188

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Active 
Partition
(Lower 
Address)
Passive
Partition
(Higher 
Address)
0x00400000
0x007FFFFF
0x007D4000
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
0x005D4000
0x005FFFFF
SMR Verification request 
(without HSE_SMR_VERIFICATION_OPTION_PASSIVE_MEM  option)
SMR verification fails
HSE firmware verifies 
SMR from pSmrSrc 
address in active partition 
while tag is generated 
over pSmrData present in 
passive partition
Application v1
SMR region v1
Application v2
SMR region v2
Figure 71. SMR verification failure scenario
To overcome such failure, below steps must be followed:
1. Host triggers, at run-time, the verification via the service defined by the structure hseSmrVerifySrv_t
with option HSE_SMR_VERIFICATION_OPTION_PASSIVE_MEM.
2. HSE_SMR_VERIFICATION_OPTION_PASSIVE_MEM option indicates to the HSE that there is a need to
perform an address translation, that is to add or subtract a block offset value to or from the SMR verification
source address to map it to the correct source address.
3. The HSE performs the verification using translated address calculated in step 2.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
188 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 189

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
0x00400000
0x007FFFFF
0x007D4000
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
0x005D4000
0x005FFFFF
Application v1
SMR region v1
Application v2
Active 
Partition
(Lower 
Address)
SMR region v2
Passive
Partition
(Higher 
Address)
SMR Verification request 
(with HSE_SMR_VERIFICATION_OPTION_PASSIVE_MEM  option)
SMR verification passes
HSE adds block 
offset(0x200000) to 
addresses [1*] 
to map them to correct 
addresses
[1*]: pSmrSrc/pInstAuthTag[0]/pInstAuthTag[1]/
pSmrEntry→smrDecrypt.pGmacTag/
pSmrEntry→smrDecrypt.pAAD
Figure 72. SMR verification passing scenario
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
189 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 190

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
START
Is AB Swap 
device?
Check value of options 
in hseSmrVerifySrv _t 
structure
Is 
HSE_INT_SMR_VERIF_OPTION_PASSIVE_
MEM
 enabled?
Add block 
address offset to 
map it to correct 
addresses  
NO
YES
NO
END
Verification addresses 
lies in active (lower code 
flash memory) partition?
Subtract block 
address offset to 
map it to correct 
addresses  
NO
YES
The verification addresses 
(e.g. pSmrSrc, 
pInstAuthTag[0] etc) is read 
directly (No offset)
YES
Verification addresses 
lies in passive (higher code 
flash memory) partition?
YES
No offset added/
subtracted to/
from verification 
addresses
NO
The verification addresses 
(e.g. pSmrSrc, 
pInstAuthTag[0] etc) is read 
directly (No offset)
Figure 73. Address translation logic AB_SWAP configuration
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
190 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 191

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
7.8.5  Recurrent automatic SMR verification
When its data field smrEntry.checkPeriod is set to a value different from 0, a SMR is automatically verified
recurrently by the HSE during run-time, i.e. during normal operating conditions, once the pre-boot and post-boot
phases are over.
The verification recurrence is defined by a number of system clock cycles, each unit corresponding to 100ms at
maximum frequency. For example, if smrEntry.checkPeriod = 80, a verification process is triggered every
2s for a system clock frequency of 160MHz, 4s at 80MHz, and so on.
It can be configured for any SMR that is loaded in RAM and for which the internal proof of authenticity
generated by HSE is used for verification (that is, HSE_SMR_CFG_FLAG_INSTALL_AUTH is not set).
7.9  SMR Entry erase
The host can request for erasing an SMR entry via the service defined by the structure
hseSmrEntryEraseSrv_t. Before calling this service, the host must be granted with SU rights.
7.10  Secure boot and automatic SMR verification
When BOOT_SEQ equals 1 in IVT, HSE uses the configuration in the SMR and CR tables to boot the
application cores securely. As such, the SMR linked with the CR table is verified automatically by the HSE
during start-up.
Important:
If BOOT_SEQ equals 0, the automatic SMR verification is not triggered after reset.
To test an SMR configuration BOOT_SEQ value can be changed in IVT without needing to authenticate it if
IVT_AUTH bit is not set to 1
The automatic verification at start-up splits in three phases:
• The pre-boot phase, during which the SMR are verified before any CPU subsystem in the host is released
from reset; this is the first phase after start-up
• The booting phase, during which the SMR are verified after the first CPU subsystem in the host has been
released from reset (when allowed); this is the second phase after start-up
• The post-boot phase, during which the SMR are verified after all CPU subsystems in the host have been
released from reset (when allowed); this is the third phase after start-up
The end of the pre-boot and booting phases can be monitored via the status flag HSE_STATUS_BOOT_OK and
the end of the post-boot phase can be monitored via the status flag HSE_STATUS_INIT_OK as illustrated in the
below figure.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
191 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 192

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
HSE_STATUS_INIT_OK == 1
Application CPU subsystems operating
HSE_STATUS_BOOT_OK == 1
HSE Running
HSE Initializing
Pre-boot phase
boot
Post-boot phase
Run-time phase
time
reset
Figure 74. Pre-boot / boot / post-boot phases (BOOT_SEQ == 1)
7.10.1  Pre-boot phase
During the pre-boot phase, HSE parses the CR table from the smallest entry index to the highest. For each
CR entry, SMR linked via pCrEntry➔preBootSmrMap data field are verified first. If any of these SMR fails
verification, HSE verifies the SMR specified by pCrEntry➔altPreBootSmrMap data field is configured.
If all SMR are verified successful from either of the pre-boot SMR maps, HSE may release from reset the CPU
subsystem in the host depending on the core reset release strategy (see section Booting Phase and Core Reset
Release Strategies for more details).
If both pre-boot SMR maps have at least one SMR for which the verification fails, HSE applies the sanction
configured for that CR entry. For more details on sanctions, see section Sanctions.
The SMR linked to the CR entry via pCrEntry➔postBootSmrMap data field are loaded to the destination
address in RAM during the pre-boot phase only if pCrEntry➔preBootSmrMap data field is 0. Such
configuration enables a CPU subsystem in the host to be released from reset before the SMR authenticity is
verified, as this is done in post-boot phase. This is known as “parallel secure boot” and can be used for better
performance during start-up.
The pre-boot phase complete flow is illustrated in section Secure Boot Flow.
7.10.2  Booting phase and core reset release strategies
While the CR table is parsed in the pre-boot phase, HSE releases the associated CPU from reset according to
the core reset release strategy, configurable via hseAttrCoreResetRelease_t attribute:
• ALL_AT_ONCE, by which HSE parses first the entire CR table and verifies all the associated pre-boot SMR
entries and then releases from reset all CPU subsystems configured that passed the verification.
• ONE_BY_ONE, by which HSE releases from reset each CPU subsystem one by one, after the associated CR
entry and pre-boot SMR entries have been verified successfully.
The pre-boot phase ends when the first CPU subsystem is released from reset.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
192 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 193

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The end of both pre-boot and booting phases which implies all configured CPU subsystems being booted is
signaled by the HSE via the status flag HSE_STATUS_BOOT_OK.
The booting phase complete flow is illustrated in section Secure Boot Flow.
7.10.3  Post-boot phase
After all configured application CPU subsystems are released from reset and the booting phase is
over, HSE reiterates through the CR table and for each entry it verifies the associated SMR linked via
pCrEntry➔postBootSmrMap data field. The authenticity proof verification is done over the content in RAM/
FLASH. As such, If a SMR destination address (data field smrEntry.pSmrDest) is set with a valid RAM address,
if the SMR is not already loaded, HSE first copies the content from the source address in internal Flash to the
RAM destination address, otherwise verification is done over the contents in the flash.
If any of the SMR verified during the post-boot phase fails verification, HSE applies the configured sanction for
the associated CR entry. In this case, HSE_CR_SANCTION_KEEP_CORE_IN_RESET is not applicable (i.e.
HSE can not keep an application CPU in RESET phase that has been already booted).
The post-boot phase complete flow is illustrated in section Secure Boot Flow.
7.10.4  Sanctions
When SMR verification fails, two types of sanctions can apply:
• Sanctions on key usage
• Sanctions on device operation
Important:
If any core not booted by HSE FW and sanction need to apply, HSE FW enters in default recovery mode based
on Sanction need to apply. For recovery mode, kindly refer to the Recovery Mode section.
Each key usage can be individually conditioned by the verification status of up to 8 SMR via the SMR
verification map (see section Key Attributes). This configuration is performed during the provisioning of each key
in the NVM key catalog. Note that this sanction does not apply to the keys within the RAM key catalog.
No. of SMR to be verified (smr
Flags in key attributes)
SMR verification status
Sanction on key usage
0
N/A
All SMR verified
Key can be used by the host
1 to 8
At least one SMR not verified
Key cannot be used by the host
Table 93. Sanction on a key usage after SMR verification
The sanction taken by the HSE for a CR entry associated with SMR that failed verification depends on the
phase when it is applied (i.e. pre-boot or post-boot). The below table summarizes the conditions and HSE
behavior in terms of sanctions applied in the pre-boot and booting phases.
Conditions
Sanction on subsystem
pPassReset within a verified SMR
Release from reset at address pPassReset
pPassReset NOT within a verified SMR
Verify altPreBootSmrMap if configured, otherwise sanction is the
same as if one SMR failed the verification (see below)
pAltReset within a verified SMR
Release from reset at address pAltReset
pAltReset NOT within a verified SMR
Same as if one SMR failed the verification (see below)
Table 94. Sanction on a subsystem (all SMR verified in pre-boot phase)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
193 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 194

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
crSanction (xxx = HSE_CR_
SANCTION)
Conditions
Sanction on subsystem
xxx_KEEP_CORE_IN_RESET
Keep in reset
Device enters in recovery mode.
xxx_RESET_SOC
Reset the device (all subsystems
impacted)
After 8 reset device enters in recovery
mode.
xxx_DIS_ALL_KEYS
xxx_DIS_INDIV_KEYS
altPreBootSmrMap == 0
OR
at least one SMR listed in altPreBootSmr
Map NOT verified
OR
pAltReset == 0
OR
pAltReset NOT within a verified SMR
Keep in reset and disable key
usage[Note]
Device enters in recovery mode.
Table 95. Sanction on a subsystem (at least one SMR in primary map not verified in pre-boot phase)
Note:  If the sanction is HSE_CR_SANCTION_DIS_ALL_KEYS, HSE disables all keys; otherwise, key usage is
individually disabled via the smrFlags key attribute
The below tables summarize the conditions and HSE behavior in terms of sanctions applied in the post-boot
phase.
SMR verification status
crSanction (xxx = HSE_CR_
SANCTION)
Sanction on subsystem
All SMR verified
N/A
None (continue operation)
xxx_KEEP_CORE_IN_RESET
None (continue operation)
xxx_RESET_SOC
Reset the device (all subsystems impacted)
After 8 reset device enters in recovery mode.
xxx_DIS_ALL_KEYS
Disable all key usage
At least one SMR not
verified
xxx_DIS_INDIV_KEYS
Disable the usage of selected keys via the key
attribute smrFlags
Table 96. Sanction on a subsystem (at least one SMR not verified in post-boot phase)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
194 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 195

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
7.10.5  Secure boot flow
The following figures detail the SMR verification processes during pre-boot and post-boot phases and the
sanctions taken by the HSE at the end of each phase.
Core ID
0
1
2
3
…
…
4
5
6
…
0
1
2
3
…
0
X
X
1
X
X
X
2
X
A
B
PRE_BOOT
PRE_BOOT ALT
POST_BOOT
SMR map
M(SMR0)
F
L+D(SMR0)
M(SMR1)
V
L+D(SMR1)
L+D(SMR3)
Exec (SMR4)
Exec (SMR1)
Exec (SMR3)
M(SMR3)
V
M(SMR4) V
L+D(SMR4)
M(SMR0)
F
L+D(SMR0)
M(SMR4) V
L+D(SMR4)
Exec (SMR4)
M(SMR1)
V
L+D(SMR1)
Exec (SMR1)
L+D(SMR3)
Exec (SMR3)
CR Table
POR
POR
M(SMR2) V
L+D(SMR2)
M(SMR3)
V
M(SMR2) V
L+D(SMR2)
ALL AT ONCE strategy
ONE BY ONE strategy
L – Load; D – Decrypt; M– Measure; V– Verified; F - Failed
Boot from alternate pre-boot SMR
Boot from pre-boot SMR
Boot from post-boot SMR
Figure 75. Example of secure boot configuration depending on core reset strategies
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
195 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 196

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
CR Table Parsing 
Start
j >= CoreEntryInstall
CoreIdx j = 0
j++
CR table Parsing 
Finish
YES
YES
NO
CR[j].CoreId == INVALID ||
CR[j].StartOption == ON_DEMAND
NO
CR[j].PreBootSmrMap != 0
Verify PRE-BOOT SMR entries
All SMR entries Verified
Mark the entries to boot from pass reset address
Verify PRE-BOOT Alter SMR entries, apply 
Sanctions
CR[j].postBootSmrMap != 0
coreResetReleaseOption = = 
ONE_BY_ONE
Enables Core
Enables Core
Parse the POST_BOOT entries, verify and 
apply sanctions
YES
NO
YES
NO
NO
NO
YES
Copy POST-BOOT SMR entries
smrEntry.pDest !=0
YES
YES
NO
Figure 76. Secure boot and CR table parsing
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
196 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 197

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Pre Boot SMR 
Verify
If
SMR[i].pSmrDest != 0
Copy SMR[i] from Flash to RAM
Verify plain SMR[i]
Continue for CR 
Table Parsing
NO
Verify and Decrypt Encypted SMR[i]
Smrldx i=0, Crldx = j
YES
Is
SMR[i] encrypted?
YES
Decrypt Successful?
YES
Verify Successfully?
YES
i++
If I >= Cr[j].preBootSmrMap
YES
NO
NO
NO
NO
Figure 77. Verification of SMR linked via preBootSmrMap
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
197 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 198

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Application Core Ungate?
Start Recovery Mode
NO
End
YES
Pre Boot Alter 
SMR verify
SMR[i].pSmrDest
!= 0
I >= Cr[j].preBootSmrMap
SmrIdx i=0, CrIdx = j
Copy SMR[i] From Flash To 
RAM
SMR[i] encrypted
Verify & Decrypt Encrypted 
SMR[i] 
i++
Continue for CR 
table Parsing
YES
NO
YES
YES
NO
NO
Decrypt Successfully
YES
Verify plain SMR[i] 
Verify Successfully
YES
NO
NO
Cr[j].sanction == 
HSE_CR_SANCTION_DIS_ALL_KEYS
Disable All Keys
Cr[j].sanction == 
HSE_CR_SANCTION_KEEP_CORE_I
N_RESET
Keep Core in Reset
Cr[j].sanction == 
HSE_CR_SANCTION_RESET_SOC
Issue Functional Reset
YES
NO
YES
NO
NO
YES
Figure 78. Verification of SMR linked via altPreBootSmrMap and applying sanctions in pre-boot phase
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
198 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 199

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Figure 79. Loading SMR linked via postBootSmrMap in pre-boot phase
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
199 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 200

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Figure 80. Releasing the cores from reset - boot phase
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
200 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 201

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Figure 81. Verification of SMR linked via postBootSmrMap and applying sanctions in post-boot phase
7.10.6  On-demand secure boot
CR entries having the data field startOption set to HSE_CR_ON_DEMAND is skipped by HSE during start-
up. Processing these entries by the HSE can be triggered by the host CPU subsystems at run-time, using
hseCrOnDemandBootSrv_t service.
This service takes as input a number between 0 and up to 3 which represents the index in the CR table of the
entry to be processed.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
201 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 202

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
To use this service, Super User access rights are needed with configuration privileges.
When BOOT_SEQ is set to 0 in IVT (i.e. non-secure boot mode), this service can be used to release application
CPU from reset that are not already booted (i.e. cannot be used for the BOOT_TARGET core as specified in
IVT .
Upon calling this service, HSE loads and verifies the associated SMR entries. If all SMR are verified
successfully the CPU subsystem is released from reset. Otherwise, if any of the SMR verification fails, the
HSE applies the configured sanction similarly to the sanctions taken during post-boot phase for the CR entry
requested to be booted on-demand.
The below picture illustrates the on-demand CR entry boot with more details.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
202 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 203

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
On Demand Req 
Start
If
CR[j].coreId == INVALID || CR[j].StartOption != 
ON_DEMAND
Mark the entries to boot from pass reset address
On Demand Req 
Finish
NO
Coreldx  j
All SMR entries verified?
PassResetAdd !=0 || AlterResetAdds != 0
NO
NO
NO
If
CR[j].preBootSmrMap != 0
NO
Verify PRE-BOOT SMR entries
YES
Verify PRE-BOOT SMR entries
If
CR[j].postBootSmrMap != 0
YES
Parse the POST_BOOT entries, verify and apply 
sanctions
YES
Mark the entries to boot from pass reset address
YES
Enables Core
YES
Figure 82. On-demand secure boot request
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
203 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 204

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
7.10.7  Verification status
The host can check the SMR installation and verification status, as well as the CPU core reset status by reading
the HSE system attribute HSE_SMR_CORE_BOOT_STATUS_ATTR_ID (see section Manage HSE System
Attributes.
7.10.8  Validate/Invalidate SMR verification status (SMR #0)
The service ID HSE_SRV_ID_SHE_BOOT_FAILURE (that takes no input parameters) allows the host to
invalidate the SMR verification service over SMR #0 if its authentication key handle refers to the SHE AES key
BOOT_MAC_KEY.
Upon successful execution, the SMR #0 verification status is set to failed. Subsequent on-demand verification
on this SMR are then rejected.
This specific service is to satisfy the CMD_BOOT_FAILURE command defined in SHE – Secure Hardware
Extension Functional Specification.
The service ID HSE_SRV_ID_SHE_BOOT_OK (that takes no input parameters) allows the host to render the
above described service ineffective and satisfies the CMD_BOOT_OK command defined in SHE – Secure
Hardware Extension Functional Specification. This service can only execute if SMR #0 was successfully verified
first.
7.10.9  SHE-based secure boot (SMR #0)
The SMR #0 is the only SMR that can be associated to the SHE AES key BOOT_MAC_KEY as the SMR
authentication key. In this case, the reference authentication tag is the CMAC value referred to as BOOT_MAC.
The BOOT_MAC value can be initialized and updated as mentioned in Specific Use (SMR #0).
If BOOT_SEQ == 1, authentication process started as mention in section Authenticity Proof. The reference
authentication tag is calculated by the HSE and compared with saved BOOT_MAC. This specific installation
process satisfies the requirement in SHE – Secure Hardware Extension Functional Specification referred to as
“autonomous bootstrap configuration”.
If BOOT_SEQ == 0, authentication process started as mention in section SHE-Based Secure Boot (SMR #0).
Bits #17 to #20 in the HSE status relate to the secure boot management as described in SHE – Secure
Hardware Extension Functional Specification are also updated as described in section HSE Status.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
204 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 205

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Figure 83. SHE SMR Verifications
7.10.10  Memory location
The below table summarizes the possible source and destination addresses that can be defined for an SMR
depending on its verification method.
Verification method
PRE_BOOT/PRE_BOOT_ALT/POST_
BOOT
Boot/Periodic check
Source address
on-chip Flash Address
on_chip Flash Address
Destination address
Valid SRAM address or NULL
Valid SRAM address
Table 97. SMR source / destination addresses
Note:  HSE requires periodic SMR to be copied to RAM before verification i.e. pSMRDest to be not NULL.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
205 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 206

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The below table summarizes what SMR are loaded in RAM after start-up depending on the linkage with the
CR table, its verification status and the availability of an alternate image. It also indicates when the on-demand
verification is possible.
Link with CR
table
Specified in preBootSmr
Map
Specified in altPreBoot
SmrMap
Specified in post
BootSmrMap
No CR link or linked with
CR on-demand entry
Verification
status
Pass/Fail
Fail
Not verified
Pass/Fail
Pass/Fail
Not verified
Alternate
SMR defined
No
Yes (through
same CR)
N/A
N/A
N/A
N/A
Loaded in
RAM
Yes
No (alternate
SMR loaded)
No
Yes
Yes
No
On-demand
verification
Possible
Not possible
Not
possible
Possible
Possible
Possible
Table 98. SMR availability in RAM after start-up
Note:  After SMR is loaded in RAM, subsequent verifications are done directly, without reloading from Flash.
7.10.11  Recommendations
The internal scheme for authentication of the SMR plain image (i.e. not having the
HSE_SMR_CFG_FLAG_INSTALL_AUTH configuration flag set) uses a SHA256 digest that is stored by HSE
FW internally to verify the integrity (and implicitly, the authenticity) of the image. It is recommended to use this
option as it provides the best performance (being the fastest among the possible authentication schemes) for
the same security level. However, using this option would require for any update of the SMR content to include
calling the SMR installation service, providing a signature with the initial scheme of authentication, such that
HSE FW recomputes the internal hash over the new image.
To provide confidentiality over the application code/data defined as SMR, the following mechanism can be used:
• Using the SMR decryption parameters by which the data can be encrypted and authenticated using either
AEAD-GCM or AES-CTR with an internal computed hash over the encrypted image to ensure the integrity
(and implicitly, the authenticity). More details in Encrypted SMR.
It is recommended for sensitive application code/data defined as SMR to use one of the encryption
mechanisms.
SMR entries can be versioned and hence protected against rollback attacks (i.e. by setting versionOffset to
a non-zero value, pointing to the version location in the image). Once a versioned SMR is installed, subsequent
updates must be versioned, and the version value must be strictly bigger.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
206 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 207

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
8   Administration Services
8.1  Manage HSE system attributes
8.1.1  Set HSE system attributes
The host can initialize the value of different HSE system attributes via the service defined by the structure
hseSetAttrSrv_t.
Certain attributes can be set by the host only when it is granted with Super User (SU) rights (LC can be
CUST_DEL, OEM_PROD or IN_FIELD).
The data field attrId identifies the attribute to be initialized. The data field pAttr is a pointer to the value to
set for the given attribute and the data field attrLen should be initialized with the size in bytes of that value.
The list of the different attributes, their related identifier (attrId) and their access restrictions (certain
configuration attributes are read-only) can be found in HSE Service API Reference Manual.
Further description on the system attributes having an impact on the security policies can be found in section
HSE System Attributes to Configure Security Policies.
8.1.2  Retrieve HSE system attributes
The host can retrieve the value of different HSE configuration attributes via the service defined by the structure
hseGetAttrSrv_t.
The data field attrId identifies the attribute to be read. The data field pAttr is a pointer to a RAM buffer
where the value of the attribute is written by the HSE. The data field attrLen must be initialized with the size in
bytes of that buffer. It can be equal to or bigger than the expected value size.
The list of the different attributes and their related identifier (attrId) and their access restrictions (certain
configuration attributes are write-only) can be found in HSE Service API Reference Manual.
Further description on the system attributes having an impact on the security policies can be found in section
HSE System Attributes to Configure Security Policies.
8.1.3  HSE system attributes to configure security policies
8.1.3.1  Description
The below tables list the attributes, the corresponding input / output structures and the read / write access rights
to configure certain security policies.
For further information and a complete list of HSE system attributes, refer to HSE Service API Reference
Manual.
The following attribute types are defined:
• RO-ATTR – Read-only attribute
• OTP-ATTR – One Time Programmable; can be written only once (set OTP area) and can be read at any time
• OTP-ADVANCE-ATTR – One Time Programmable attribute that can only be advanced (e.g. life cycle); can be
read at any time.
• NVM-RW-ATTR – System NVM attribute; can be read or written.
• SET-ONCE-ATTR – Once the attribute is set, it can only be changed after a reset (e.g. can be set once at
initialization time)
• RAM-RW – RAM attribute which can be set/reset as many times as possible by the customer in each reset.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
207 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 208

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
To be able to set/update the OTP or NVM attributes (except SET-ONCE-ATTR), the host needs Super User
(SU) rights.
attrId
*pAttr
Type
HSE_FW_VERSION_ATTR_ID
hseAttrFwVersion_t
RO-ATTR
HSE_CAPABILITIES_ATTR_ID
hseAttrCapabilities_t
RO-ATTR
HSE_SMR_CORE_BOOT_STATUS_ATTR_ID
hseAttrSmrCoreStatus_t
RO-ATTR
HSE_FW_BUILD_INFO_ATTR_ID
hseFwBuildInfo_t
RO-ATTR
HSE_DEBUG_AUTH_MODE_ATTR_ID
hseAttrDebugAuthMode_t
OTP-ATTR
HSE_APP_DEBUG_KEY_ATTR_ID
hseAttrApplDebugKey_t or hse
AttrSecureApplDebugKey_t
(based on the attribute size provided to
the Set Attribute service)
OTP-ATTR [1]
HSE_SECURE_LIFE CYCLE_ATTR_ID
hseAttrSecureLifecycle_t
OTP-ADVANCE-ATTR
HSE_ENABLE_BOOT_AUTH_ATTR_ID
hseAttrConfigBootAuth_t
OTP-ATTR
HSE_MU_CONFIG_ATTR_ID
hseAttrMUConfig_t
NVM-RW-ATTR
HSE_EXTEND_CUST_SECURITY_POLICY_ATTR_
ID
hseAttrExtendCustSecurity
Policy_t
OTP-ATTR and NVM-RW-
ATTR[2]
HSE_EXTEND_OEM_SECURITY_POLICY_ATTR_
ID
hseAttrExtendOemSecurity
Policy_t
NVM-RW-ATTR
HSE_FAST_CMAC_MIN_TAG_BIT_LEN_ATTR_ID
hseAttrFastCmacMinTagBitLen_
t
NVM-RW-ATTR
HSE_SECURE_RECOVERY_CONFIG_ATTR_ID
hseAttrConfigSecureRecovery_
t
OTP_ATTR
HSE_FIRC_DIVIDER_CONFIG_ATTR_ID
hseFircDivConfig_t
RAM-RW
HSE_CORE_RESET_RELEASE_ATTR_ID
hseAttrCoreResetRelease_t
NVM-RW-ATTR
HSE_PHYSICAL_TAMPER_ATTR_ID
hseAttrPhysicalTamperConfig_
t
SET-ONCE-ATTR
HSE_MEM_REGIONS_PROTECT_ATTR_ID
hseAttrAllMuMemRegions_t
SET-ONCE-ATTR
HSE_RAM_PUB_KEY_IMPORT_POLICY_ATTR_ID
hseAttrRamPubKeyImport
Policy_t
NVM-RW-ATTR
HSE_ENABLE_PUBLISH_KEY_STORE_RAM_
TO_FLASH_ATTR_ID
hsePublishNvmKeystoreRamtTo
Flash_t
RAM-RW
Table 99. HSE system attributes
[1]
It is possible to read-out 16 bytes of the hash (SHA2-224) over ADKP.
[2]
The attribute structure contains data fields that set OTP and NVM configurations (that is, enableADKm is set in OTP, and StartAsUser is stored in NVM).
Structure
Description
hseAttrFwVersion_t
A structure with the following data fields:
Reserved:
1. '1' means AB_SWAP configuration
2. '0' means FULL_MEM configuration
socTypeId: identifies the device
fwTypeId: identifies the device and the HSE variant
Table 100. System attribute structures
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
208 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 209

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Structure
Description
• 0: standard generic firmware
• 1: premium generic firmware
majorVersion: the firmware major revision; increase if breaking changes
were introduced
minorVersion: the firmware minor revision; bumped on new compatible
changes added; reset to 0 on majorVersion bump
patchVersion: the firmware patch revision; used to identify version with bug
fixes
hseAttrCapabilities_t
A 64-bit integer that identifies the HSE capabilities; refer to HSE Service API
Reference Manual for details.
hseAttrSmrCoreStatus_t
Provides the SMR verification status and Core Boot status; refer to HSE
Service API Reference Manual for the details.
hseFwBuildInfo_t
This attribute is available if the HSE_FW_BUILD_INFO_ATTR_ID macro is
defined. If available, it provides information about the firmware build: an unique
8-byte identifier, and the build date and time; for details, refer to HSE Service
API Reference Manual.
hseAttrDebugAuthMode_t
Specifies if the host debug authorization (AUTH_METHOD) is password-based
(static authentication) or challenge-response based (dynamic authentication);
by default, the host debug authorization is password-based; refer to HSE
Service API Reference Manual for details.
hseAttrApplDebugKey_t
An array of 16 bytes that defines the ADKP value (write once only).
Depending on the value of enableADKm, the value saved in secure NVM is
either ADKP provided in input to the service, or a diversified value based on
the device’s UID (see section Provisioning Device-Dependent ADKP).
On read, the HSE returns the first 16 bytes of SHA224 over ADKP value.
The ADKP can be set only if the life cycle is set to CUST_DEL, and the
provided bytes must be different from all zeros or all FFs.
hseAttrSecureApplDebugKey_t
The ADKP can also be set from an already installed/generated RAM or NVM
key slot. The hseAttrSecureApplDebugKey_t structure contains the key
handle of an AES-128 key from RAM or NVM key.
Note:  The hseAttrApplDebugKey_t and hseAttrSecureApplDebug
Key_t structures are used with the same attribute ID when calling the
Set Attribute service (HSE_APP_DEBUG_KEY_ATTR_ID). The HSE FW
differentiates between plain/secure ADKP provisioning based on the attribute
size.
hseAttrSecureLifecycle_t
An integer value that defines or returns the LC.
Possible set values that define the new LC state on next reset:
• HSE_LC_OEM_PROD
• HSE_LC_IN_FIELD
• HSE_LC_SIMULATED_OEM_PROD (test purpose)
• HSE_LC_SIMULATED_IN_FIELD (test purpose)
Reading the LC can be done by using DCM Registers. Refer to the HSE
Service API Reference Manual for more details.
Moving the life cycle from CUST_DEL to OEM_PROD or IN_FIELD is only
possible if ADKP has been provisioned.
Key Catalog must be formatted before advancing the LC.
hseAttrConfigBootAuth_t
An integer value that defines or returns IVT_AUTH:
• HSE_IVT_NO_AUTH: no authentication check
• HSE_IVT_AUTH: IVT images authenticated before starting the HSE
Table 100. System attribute structures...continued
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
209 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 210

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Structure
Description
This service is only allowed if ADKP has been provisioned.
hseAttrExtendCustSecurity
Policy_t
A structure with the following data fields:
enableADKm: defines or returns ADKP_MASTER
startAsUser: defines or returns the value of CUST_START_AS_USER
Important:  ADKP_MASTER must be set before provisioning ADKP.
If ADKP is programmed, then setting of enableADKm is not allowed.
hseAttrMUConfig_t
A table of hseAttrMUInstanceConfig_t to configure the MU instances;
the number of elements in the table is defined by HSE_NUM_OF_MU_
INSTANCES
Each table element is a structure with the following data fields:
• muInstances[i].muConfig: an integer that indicates if the MU instance
#i is active or not.
• muInstances[i].xrdcDomainId : ignored
• muInstances[i].sharedMemChunkSize: this field is cleared to 0 when
reading the attribute, and discarded when setting the attribute)
By default, only MU instance 0 is enabled and it cannot be disabled.
hseAttrExtendOemSecurityPolicy_
t
A structure with the following data field:
• startAsUser: defines or returns the value of OEM_START_AS_USER
Refer to HSE Service API Reference Manual for details.
hseAttrFastCmacMinTagBitLen_t
The minimal length of the tag for the Fast CMAC service. By default, this
value is HSE_DEFAULT_MIN_FAST_CMAC_TAG_BITLEN bits (refer to HSE
Service API Reference Manual). This attribute allows the use of the service
with the tag bit length less than HSE_DEFAULT_MIN_FAST_CMAC_TAG_
BITLEN bits. The value must be provided in bits.
hseAttrCoreResetRelease_t
This attribute defines the start-up method for releasing the application cores
from reset. One can configure the way the cores are released from reset in two
different ways: all at once or one by one. Refer to HSE Service API Reference
Manual for more details.
hseAttrAllMuMemRegions_t
The HSE access to memory areas can be defined for each MU instance using
this attribute. One can configure a set of memory ranges with permissions (In/
Out/InOut) for each MU instance and the HSE FW uses the configuration to
restrict the access outside of the defined ranges of a specific MU instance for
the services received on that MU. For more information on the configuration,
refer to HSE Service API Reference Manual.
hseAttrPhysicalTamperConfig_t
Enables the tamper violation in HSE subsystem for all physical tampers
supported by the device. Once the violation is enabled, it cannot be cleared
until next reset. User is recommended to configure the tampers pads GPIO
in tamper mode and can optionally lock those pads configuration for further
modification using virtual wrapper; refer to HSE Service API Reference Manual
and S32K3xx Reference Manual for details.
hseFircDivConfig_t
FIRC Divider Configuration; refer to HSE Service API Reference Manual for
the details. This attribute is used to configure the FIRC divider through HSE
Firmware as write access on this register is disabled for application. HSE
firmware goes to shutdown mode if the divider value selected is 16.
hseAttrConfigSecureRecovery_t
Secure recovery mode feature enablement. The secure recovery mode allows
application to boot its secure recovery image, in case, it is not booted by SBAF
or HSE FW. For more details refer to Secure recovery mode section in chapter
Device Specific Parameters (S32K3xx).
Table 100. System attribute structures...continued
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
210 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 211

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Structure
Description
hseAttrRamPubKeyImportPolicy_t
Determines whether public keys can be imported without authentication in
advanced LCs. Default value is HSE_KM_POLICY_DEFAULT, i.e. HSE does
not allow public key import in RAM, when having User rights, if they are not an
authenticated key container. Otherwise, if set to HSE_KM_POLICY_ALLOW_
RAM_PUB_KEY_IMPORT, RAM public keys are allowed to be imported
without authentication, regardless of the access rights. SU access rights with
configuration privileges are required to update this attribute value.
hsePublishNvmKeystoreRamtTo
Flash_t
Setting of this attribute can be used to reduce the number of write operations
in the data flash and increase the performance when the key store is updated.
Once this attribute is set, the HSE FW updates the NVM keys only in the mirror
RAM memory and keys are updated to secure flash area only when “HSE_
SRV_ID_PUBLISH_NVM_KEYSTORE_RAM_TO_FLASH” is given. For more
information on the configuration, refer to the HSE Service API Reference
Manual.
hseAttrMacSecManagedMode_t
This attribute is set by default to MACSec Open Mode, as K358 device only
supports MACSec open mode configuration.
The HSE can only be configured in Open Mode for MACSec on K358 device :
MACsec Open Mode:
• Secure Association Key (SAK) can be exported in plaintext when the key is
derived or when it is unwrapped.
• Programming the keys into the MACsec HW IP is managed by the
application.
For more details, refer to HSE Service API Reference Manual.
Table 100. System attribute structures...continued
The tamper configuration is available for the host side to read from a GPR register. This status register is
updated when a tamper is configured in HSE during initialization or via attributes. For more information on the
status format refer to Tamper Configuration Status Bits Fields or HSE Service API Reference Manual.
Bit
Name
Description
0
HSE_CMU_TAMPER_CONFIG_STATUS
Indicates that the CMU tamper is configured. The HSE FW configures
the CMU at initialization time. The range of CMU is 3Mhz to 126Mhz
For S32K388, the range of CMU is 3Mhz to 168Mhz.
1
HSE_PHYSICAL_TAMPER_CONFIG_
STATUS
Indicates the configuration of the physical tamper. This tamper can be
enabled using the HSE_PHYSICAL_TAMPER_ATTR_ID attribute. The
application must configure SIUL2 pads before enabling.
Table 101. Tamper configuration status bit fields
8.1.3.2  Example: MU configuration
The below code snippet illustrates a possible configuration of the MU instances in S32K that corresponds to the
illustration provided in section Messaging Unit : MU instance 0 and 1 enabled.
      /* configure the HSE/host interface RAM */
  hseSrvDescriptor_t*    pHseSrvDesc;
  hseSetAttrSrv_t*       pSetSysAttr;
  hseAttrMUConfig_t      config;
  hseSrvResponse_t        srvResp;
  /* allocate the memory for the service descriptor
     in HSE/host interface RAM (not described here)
  */
  pHseSrvDesc = myAllocMem(sizeof(hseSetAttrSrv_t));
  pHseSrvDesc->srvId = HSE_SRV_ID_SET_ATTR;
  pSetSysAttr = &(pHseSrvDesc->hseSrv.setAttrReq);
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
211 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 212

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
  /* enable MU1 */
  config.muInstances[1].muConfig = HSE_MU_ACTIVATED
  /* format the service request and run it */
  pSetSysAttr->attrId  = HSE_MU_CONFIG_ATTR_ID;
  pSetSysAttr->pAttr   = &config;
  pSetSysAttr->attrLen = sizeof(config);
  /* run the service */
  srvResp = runSrv(pHseSrvDesc);
8.2  Authenticate the host system images
8.2.1  Authentication
The host can request for the calculation of an authentication tag (GMAC) over the host system images via the
service defined by the structure hseBootDataImageSignSrv_t.
This service is available to host only when it is granted with Super User (SU) rights (LC can be CUST_DEL,
OEM_PROD or IN_FIELD).
The data field pInImage is a pointer to the system image to authenticate (IVT, AppBL, AuthApp). The first 32-
bit word pointed by pInImage is a magic number that provides the information to the HSE on the type and size
of image to process.
See chapter Device Specific Parameters (S32K3xx) for IVT structure details.
The data field pOutTagAddr is the pointer to a buffer where the HSE outputs the resulting GMAC (the
authentication tag). The data field inTagLength must be set with the size in bytes of the output buffer. It must
be bigger or equal to 16.
The key used to calculate the GMAC is a 256-bit AES key resulting from SHA256 operation over the user-
defined application debug key / password (ADKP) as illustrated in the below picture.
The random initial vector (IV) for the GMAC operation is of size 12-bytes should be provided with host system
images and should be included in GMAC calculation.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
212 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 213

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
SHA256
ADKP
(Saved in secure NVM)
128-bit input
256-bit output
ADKP - extended
For IVT Authentication
Figure 84. ADKP extension for IVT authentication
Important:  ADKP can be optionally diversified with the device UID before being provisioned in the HSE, hence
making the IVT authentication key device specific. Refer to section Provisioning a Device-dependent ADKP.
The host must program the resulting GMAC in application NVM, at the required location provided by the system
image mapping before execution of the service.
More information on those mapping (and more particularly on the memory location of the authentication tag),
see Device Specific Parameters (S32K3xx).
8.2.2  Verification
The host can verify the authenticity of the host system images via the service defined by the structure
hseBootDataImageVerifySrv_t.
The data field pInImage is a pointer to the system image to authenticate (IVT). The first 32-bit word pointed by
pInImage provides the information to the HSE on the type and size of image to process.
The authentication tag to verify is a 16-byte GMAC value stored at the end of the image.
More information on those mapping (and more particularly on the memory location of the authentication tag),
see Device Specific Parameters (S32K3xx).
8.3  Cancel a service request
The host can cancel a service request via the service defined by the structure hseCancelSrv_t.
The data field muChannelIdx indicates the service channel to cancel within the MU through which the service
is triggered.
This service is effective only on service requests that are not yet being executed by the HSE. A service being
processed by the HSE cannot be cancelled by the host.
The service requests with the service ID that starts with 0x00A5XXXX cannot be canceled(non-preemtive).
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
213 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 214

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
8.4  Retrieve the SHE-UID
The host can retrieve the UID as defined in SHE – Secure Hardware Extension Functional Specification , also
referred to as the SHE-UID, via the service defined by the structure hseSheGetIdSrv_t.
The data field pChallenge is a pointer to a 16-byte challenge.
The data field pId is a pointer to a buffer of at least 15 bytes where the HSE returns the 120-bit SHE-UID to the
host which consists of 7 bytes to 0 concatenated with the 8-byte UID.
The data field pSreg is a pointer to a buffer where the HSE returns a copy of the HSE global status bits 16 to
23 as described in section HSE Status.
The data field pMac is a pointer to a buffer of at 16 bytes where the HSE returns the 128-bit CMAC
calculated over the 32-byte concatenation (challenge || UID || status). The key used for this calculation is the
MASTER_ECU_KEY declared in the SHE key group #0 slot #0. If this key is not provisioned, the CMAC value
returned is 16 bytes to 0.
For more information, refer to SHE – Secure Hardware Extension Functional Specification.
8.5  Request for Super User rights
8.5.1  Initiating the request
The host can initiate a request to be temporarily (i.e. until next reset or until the host request for User rights)
granted with Super User rights via the service defined by the structure hseSysAuthorizationReqSrv_t.
The purpose of this service is to request for a challenge to be later used in the response that grants the Super
User rights (see following section).
The data field sysRights specifies if the request is to get Super User rights or User rights. In the latter case,
all other fields do not have to be specified, and User rights are granted after the execution of the service
request: no need to finalize the request (as described in the following section).
The data field sysAuthOption defines the scope of Super User rights once granted: for key management
and/or for HSE configuration (see section Execution Rights (Super User vs User) and Execution Rights and
Respective Limitations in Key Management and Determining the Host Identity).
The data field ownerKeyHandle defines the key handle to be used to sign the challenge. It must reference:
• Either an NVM key having its usage flags set to HSE_KF_USAGE_VERIFY |
HSE_KF_USAGE_AUTHORIZATION
• Or the MASTER_ECU_KEY declared in the SHE key group #0 slot #0; other keys declared as
HSE_KEY_TYPE_SHE cannot be used as the authentication key to initiate the request
The data field authScheme specifies the type of authentication scheme to be used to grant authorization to
Super User, i.e. how the response to the challenge is calculated:
• Either a 16-byte CMAC
• Or an RSA signature
• Or an ECDSA signature
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
214 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 215

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
The data field pChallenge is a pointer to a buffer where the HSE returns a random value and the UID in
different format depending on ownerKeyHandle (see below tables). The buffer should have a minimum size of
32 bytes. The below table specifies the pChallenge layout depending on the key handle provided in input to
the service.
Bytes 30~15
Bytes 14~7
Bytes 7~0
16-byte random
7-bytes to 0
8-bytes UID
31 bytes in total
Table 102. Challenge format when requesting SU rights with MASTER_ECU_KEY
Bytes 31~8
Bytes 7~0
24-byte random
8-byte UID
32 bytes in total
Table 103. Challenge format when requesting SU rights with a key different from MASTER_ECU_KEY
8.5.2  Finalizing the request
The host can finalize a request to be temporarily granted with Super User rights via the service defined by the
structure hseSysAuthorizationRespSrv_t.
The data field pAuth[] provides the response to the challenge provided by the HSE in the SU right request
initialization (see previous section).
Authentication scheme
pAuth[0]
pAuth[1]
CMAC
Pointer to the 16-byte CMAC
Not used
RSA signature
Pointer to the signature 
Not used
ECDSA signature
Pointer to the coordinate 
Pointer the signature 
Table 104. : Response parameters vs. authentication scheme
The data field authLen[] must be set with the size of the response in the corresponding pAuth[] data field
(e.g. authLen [0] = 16 and authLen [1] = 0 when CMAC is used).
For more information on CMAC, refer to section CMAC. For more information on RSA / ECC signature
schemes, refer to section Signature Generation and Verification RSA ECC.
Upon successful verification of the response in the HSE, the host is granted with Super User rights until next
reset. The SU rights owner is the owner of the key handle used to respond to the challenge.
Owner of authentication key
SU rights owner
HSE_KEY_OWNER_CUST
System integrator (CUST)
HSE_KEY_OWNER_OEM
OEM
HSE_KEY_OWNER_ANY
Not identified (ANY)
Table 105. SU rights owner after request
8.5.3  Example
The below code snippet illustrates how the host can request for Super User rights to perform some key
management tasks and go back to User rights.
void RequestSURights(void)
{
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
215 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 216

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
    hseSrvDescriptor_t*           pHseSrvDesc;
    hseSysAuthorizationReqSrv_t*  pInitiateSysAuth;
    hseSysAuthorizationRespSrv_t* pFinalizeSysAuth;
    uint8_t challenge[32];
    uint8_t response[256];
    // initialize the service descriptor to initiate a request for SU rights
    pHseSrvDesc        = myAllocMem(sizeof(hseSysAuthorizationReqSrv_t)); // not described here
    pHseSrvDesc->srvId = HSE_SRV_ID_SYS_AUTH_REQ;
    pInitiateSysAuth   = &(pHseSrvDesc->hseSrv.sysAuthorizationReq);
    pInitiateSysAuth->sysAuthOption  = HSE_SYS_AUTH_KEY_MGMT;
    pInitiateSysAuth->sysRights      = HSE_RIGHTS_SUPER_USER;
    pInitiateSysAuth->ownerKeyHandle = GET_KEY_HANDLE(HSE_KEY_CATALOG_ID_NVM, 5, 9);
    pInitiateSysAuth->pChallenge     = challenge;
    // authentication method using a RSA signature over the challenge
    // the key selected for the verification should match that scheme
    pInitiateSysAuth->authScheme.sigScheme.signSch  = rsaPKCS1V15;
    pInitiateSysAuth->authScheme.sigScheme.hashAlgo = HSE_HASH_ALGO_SHA2_256;
    // initiate the request
    if(HSE_SRV_RSP_OK != myRunSrv(pHseSrvDesc)) goto error;
    // get the response to the challenge
    // this could involve connexion to a distant server
    GrantMeAccess(challenge, sizeof(challenge), response, sizeof(response)); // not described here
    // initialize the service descriptor to finalize the request for SU rights
    pHseSrvDesc        = myAllocMem(sizeof(hseSysAuthorizationRespSrv_t)); // not described here
    pHseSrvDesc->srvId = HSE_SRV_ID_SYS_AUTH_RESP;
    pFinalizeSysAuth   = &(pHseSrvDesc->hseSrv.sysAuthorizationResp);
    pFinalizeSysAuth->pAuth[0]   = response;
    pFinalizeSysAuth->authLen[0] = sizeof(response);
    pFinalizeSysAuth->pAuth[1]   = NULL;
    // provide the response to the challenge
    if(HSE_SRV_RSP_OK != myRunSrv(pHseSrvDesc)) goto error;
    // at this point host is granted with SU rights
    // do some key management
    DoSomeKeyMangementStuff(); // not described here
    // initialize the service descriptor to initiate a request for User rights
    // i.e. cancel SU rights
    pHseSrvDesc        = myAllocMem(sizeof(hseSysAuthorizationReqSrv_t)); // not described here
    pHseSrvDesc->srvId = HSE_SRV_ID_SYS_AUTH_REQ;
    pInitiateSysAuth   = &(pHseSrvDesc->hseSrv.sysAuthorizationReq);
    pInitiateSysAuth->sysRights      = HSE_RIGHTS_USER;
    // initiate the request
    if(HSE_SRV_RSP_OK != myRunSrv(pHseSrvDesc)) goto error;
    // at this point host is back with User rights only
error:
    // error management to be done here
}
8.6  Managing execution streams and related contexts
The host can save and restore streaming execution contexts outside of HSE exclusive memories via the service
defined by the structure hseImportExportStreamCtxSrv_t.
The data field streamId indicates the stream identifier for which the execution context is saved or restored.
The data field operation indicates the type of operation to perform on the service call:
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
216 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 217

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• To save (i.e. export) a streaming execution context, it must be set to
HSE_EXPORT_STREAMING_CONTEXT
• To restore (i.e. import) a streaming execution context, it must be set to
HSE_IMPORT_STREAMING_CONTEXT
The data field pStreamContext is the pointer in RAM to a buffer where:
• Either the HSE outputs the streaming execution context in an encrypted and authenticated form
• Or the HSE reads the streaming execution context to be imported back
The following restrictions apply:
• The byte size of the buffer that contains a streaming execution context must be at least equal to
MAX_STREAMING_CONTEXT_SIZE.
• It is only possible to export the execution context of a stream that is started and not finished.
• A streaming context can be imported or exported on the same MU instance on which the streaming START
step was called (e.g. the steaming context is allocated when the START step is called).
• Attempting to import a streaming context that was not created out of an export service ends with an error.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
217 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 218

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
9   Miscellaneous Services
9.1  Monotonic counter services
The host can manage monotonic counters handled within the HSE via three services defined by the structures
hseConfigSecCounterSrv_t, hseReadCounterSrv_t and hseIncrementCounterSrv_t.
9.1.1  General use
The HSE monotonic counters are 64-bit integers that can be read and only incremented until
saturation. The number of counters available for the application is defined by the C macro
HSE_NUM_OF_MONOTONIC_COUNTERS.
To read a monotonic counter, the data field counterIndex in the service structure hseReadCounterSrv_t
is set with the counter index (from 0 to HSE_NUM_OF_MONOTONIC_COUNTERS – 1) and the corresponding
64-bits counter is returned by the HSE at the memory location pointed by pCounterVal.
To increment a monotonic counter, the data field counterIndex in the service
structure hseIncrementCounterSrv_t is set with the counter index (from 0 to
HSE_NUM_OF_MONOTONIC_COUNTERS - 1) and the data field value is set with the 32-bit increment to add
to the current counter value.
Note:
In HSE Firmware v0.2.40.0 and above, the Increment Counter service is treated by the HSE FW as a service of
type 0x00 (see Service Type) internally, though being denoted as of type 0xA5 in the HSE Interface (refer HSE
Service API Reference Manual).
9.1.2  Configure monotonic counters
The host can use the hseConfigSecCounterSrv_t service to initialize and configure the monotonic
counters. By default, those counters are disabled.
A monotonic counter is the concatenation of bitfields:
• Rollover Protection (RP) – the most significant bits (MSB) of the counter; each time the RP is updated, the
monotonic counter is saved in HSE data Flash. The size of RP bits must be greater than equal to 32 bits. It
must be always multiple of 8 bits.
• Volatile Counter (VC) – the LSB bitfield from the counter that does not trigger a store in data flash.
The RP / VC split allows to reduce the number erasing operations in HSE data Flash: the higher the size of
RP, the higher the erasing frequency. An erase operation is triggered every 512 RP bitfield updates (over all
the monotonic counters managed by the HSE). Since the data Flash can endure a maximum of 100 000 erase
operations, RP sizes must be configured according to the counter update frequencies.
The size of the RP bitfield can be configured from 32 to 64 bits in multiple of 8 bits. The remaining bits are used
as the VC bitfield. If the RP size is set to 64 bits, the monotonic counter is saved to HSE data Flash every time it
is updated.
The below table illustrates the counter value as it can be read by the host (application) and as it is available in
HSE data Flash, with a RP size set to 48 bits (hence a VC size set to 16 bits).
Current counter value
Value added
New counter value
Counter value in Flash
0
0x10
0x10
0
0x10
0x100
0x110
0
Table 106. Illustrating monotonic counter value evolution in application and data Flash
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
218 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 219

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Current counter value
Value added
New counter value
Counter value in Flash
0x110
0x10000
0x10110
0x10110
0x10110
0x20000
0x30110
0x30110
0x30110
0x100
0x30210
0x30110
Table 106. Illustrating monotonic counter value evolution in application and data Flash...continued
9.2  Erase HSE Data Flash
During development, the host can request to erase the HSE Data Flash (such as NVM key store, NVM
attributes) via the service ID HSE_SRV_ID_ERASE_HSE_NVM_DATA. This service can be called only in
CUST_DEL life cycle.
After the response is received by the host, application must poll for HSE_STATUS_INIT_OK before issuing any
service request to HSE.
Refer to the HSE Service API Reference Manual for more details.
9.3  HSE Flash Memory Integrity
9.3.1  Scope
The host can check the integrity of HSE Firmware code area in the code Flash memory, for the HSE Firmware
backup (in data flash memory or passive code flash memory depending on device configuration) and SYS-IMG
in data flash memory via the service ID HSE_SRV_ID_FW_INTEGRITY_CHECK.
9.3.2  General use
The host can check the integrity of the secure NVM for ECC errors.
• In case of an ECC error in HSE code Flash, HSE set GSR[0] to indicate a HSE shutdown (HSE enters in the
secure failure state). ECC recovery is heavily evolved over time, therefore the behavior is dependent on SBAF
and HSE versions.
– HSE Versions >= 2.40.0 & SBAF >= 0.15.0: In most of the cases 1 functional reset from Host triggers
the ECC recovery. Refer to Flash ECC Errors for detailed information and software flows on ECC error
handling.
– Rest of the versions: Host must provide the functional-reset 5 times to trigger the handshaking logic for ECC
recovery. Refer to HSE Firmware Handshake section for more details.
• In case of ECC error in HSE data Flash/ passive partition memory, HSE takes backup from the code Flash /
active partition memory. If backup fails, HSE sends HSE_SRV_RSP_GENERAL_ERROR to the host and sets
warning bit in MUB_GSR register.
Refer to Error and Warning Management for more details.
9.4  HSE idle state
The HSE enters in wait-for-interrupt mode (WFI) when there is no pending service request or internal task to
be executed. The HSE automatically resumes its execution when a service request is received or if an internal
event is triggered.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
219 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 220

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
9.5  MACsec Key Management
The HSE provides key management services for the system architecture that supports port-based network
access control using MACsec protocol to secure the communication with authenticated and authorized systems.
In this context, the HSE services can be used for:
• key derivation as it defined by the MACsec Key Agreement Protocol (MKA) key hierarchy.
• key wrapping/un wrapping for protecting the key distribution.
For more details about the MACsec, refer to IEEE Standard for Local and Metropolitan Area Networks— Port
Based Network Access Control.
The HSE can only be configured in MACSec Open Mode. This is done by setting the system attribute
hseAttrMacSecManagedMode_t to HSE_CFG_NO by default (refer to HSE system attributes).
Note:
• The services for MACsec key management are available if the HSE_SPT_MACSEC macro is defined in the
interface.
• The MACsec Managed mode is not supported.
• MACSec support is only applicable for K358 and related phantoms devices.
Important:  MACsec is available only for K358 and only starting with HSE release 0.2.73.0.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
220 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 221

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
10   Error and Warning Management
10.1  Scope
This section describes the various errors and warnings that can be reported by the HSE to the host. The HSE
communicates the status of various events to the host by writing MU_GSR register. The host can enable the
interrupts on GSR register to take immediate action on such events.
10.2  HSE system events
The GSR register logs the HSE system events as described in the table below.
The 16 most-significant bits are reserved for NXP internal errors, and the 16 least-significant bits notify the host
about fatal and warning events (that are relevant to the host). The host should read the GSR register and write
back the register value to clear the bits (W1C - write one to clear). Furthermore, the 16 least-significant bits are
logically divided into two subgroups:
• 0-7 bits signal fatal errors. Any fatal error triggers an HSE sub-system shutdown (refer to section HSE
Shutdown Mode).
• 8-15 bits signal warnings (non-fatal failures).
Note that this 32-bit value is mirrored in all MU instances: reading the GSR in MU instance 0 returns the same
value as reading GSR in any other MU instances.
Bit #
Description
31-16
The most significant 16 bits are reserved for NXP internal errors. These bits are set when a fatal error is
triggered and represents an error code that can be decoded only by NXP.
11-15
RFU
10
HSE_WA_RNG_NOT_INIT; RNG is not initialized. RNG-based services may be delayed as the HSE
attempts to re-initialize the RNG.
9
HSE_WA_DATA_FLASH_INTEGRITY_FAIL: warning event indicating that backup of firmware is not
available or integrity of HSE backup image has failed.
8
HSE_WA_SMR_PERIODIC_CHECK_FAILED; warning event, signaling that SMR periodic check failed. The
application can read the HSE_SMR_CORE_BOOT_STATUS_ATTR_ID attribute to see what SMR failed.
1-7
RFU
0
HSE_ERR_GENERAL; set to 1 when a fatal error (e.g. multi-bit ECC error) or intrusion detection is detected
in the HSE; this error cannot be recovered from, and a system reset should be triggered.
Table 107. HSE system events logging in GSR
10.2.1  HSE shutdown mode
Due to any error or tamper event in HSE subsystem, the firmware enters non-operational state by disabling all
the interrupts and finally enters sleep mode. As the interrupts are disabled, the host cannot request any service
to HSE Firmware. To exit the shutdown mode, the host needs to reset the device.
10.2.2  Fatal error details
10.2.2.1  General error
Any internal fatal error (such as ECC error, fault attack, watchdog event etc.) detected by the HSE firmware can
lead to the HSE_ERR_GENERAL error.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
221 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 222

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
10.2.2.2  Clock Monitoring Unit
During its initialization flow, the HSE Firmware configures CMU_5 which monitors HSE_CLK, for details on
HSE_CLK (refer to S32K3xx Reference Manual). The HSE Firmware is configured to be functional in the range:
3Mhz < HSE_CLK <126Mhz(3Mhz < HSE_CLK < 168Mhz for S32K388). Beyond this range, the CMU asserts
Destructive Reset. The status of the same can be checked in below register of MC_RGM.
Register Name
Bit number
Bit name
Destructive Event Status Register (DES)
14
HSE_CLK_FAIL, for details refer to S32K3xx Reference
Manual.
Table 108. MC_RGM Destructive reset status during CMU configuration
The status of enablement of the CMU is published at HSE_GPR_STATUS_ADDRESS (refer to the HSE Service
API Reference Manual for more information on HSE_GPR_STATUS_ADDRESS).
Though the firmware CMU is configured for 3MHz – 126Mhz(168 Mhz for S32K388), the HSE Firmware is
operational for the range of 24MHz to 120Mhz (160 Mhz for S32K388).
When HSE-ATTR (HSE_FIRC_DIVIDER_CONFIG_ATTR_ID) is requested to configure the divider as (÷16),
making the FIRC_CLK as 3MHz. CMU is not functional on FIRC_CLK ≤ 24MHz, so HSE disables the CMU and
enters shutdown mode.
The host can read a HSE GPR register (refer to HSE_GPR_STATUS_ADDRESS in the HSE Service API
Reference Manual) to check if the tamper is enabled or not.
10.2.2.3  Physical Tamper
The Physical tamper detection can be enabled by setting the hseAttrPhysicalTamperConfig_t attribute.
This attribute can be set only once (at initialization time). The attribute parameters are described in HSE Service
API Reference Manual.
After setting the hseAttrPhysicalTamperConfig_t attribute, the host can read a HSE GPR register (refer
to HSE_GPR_STATUS_ADDRESS in HSE Service API Reference Manual) to check if the tamper is enabled or
not.
10.2.2.3.1  Passive tamper
If the device is intended to be configured for passive tamper, the SIUL2 must be configured for
HSE_TAMPER_EXTIN0 S32K3xx Reference Manual] as input before enabling the tamper.
The passive tampers are level triggered tampers which can be configured as active low or active high
depending on the use case. The HSE firmware receives an alert if there is any disturbance or unexpected
change in the input signal to the tamper. If this happens, the HSE firmware signals a fatal error and enters
shutdown mode.
A filter duration can be configured to prevent glitches to the input (to prevent false errors). The filter duration
can be configured by changing the parameter ‘filterDuration’. The filters can be configured from 1 to 128, where
the length of the filter duration is calculated as 128 + ((FilterDuration-1) x 256) clock cycles. The clock frequency
is 32KHz. The length of the filter duration can range from 128 to 32640 clock cycles.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
222 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 223

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Figure 85. Passive Tamper Example Behavior
10.2.2.3.2  Active tamper
If the device is intended to be configured for active tamper detection, the SIUL2 must be configured for
HSE_TAMPER_EXTIN0 as input and HSE_TAMPER_LOOP_OUT0 as output before enabling the tamper (for
more details, refer to S32K3xx Reference Manual).
The active tampers are tampers which require to be connected in a loopback configuration where HSE
generates a random output pattern and expects the same pattern as input. The pattern output frequency is
configured by the host setting the active tamper clock. If HSE does not receive the same input pattern that was
generated in the output side, an alert is raised. If this happens, the HSE firmware signals a fatal error and enters
shutdown mode.
Important:  For active tamper, the filter configuration as specified in the previous section is mandatory to
compensate the loopback delay.
In the example shown below, the pattern generated by HSE is 0110. But due to some error in the environment,
the pattern received by HSE on the input pin is 0100, which is not the same, hence HSE raises an alert and
enters shutdown mode.
Figure 86. Active Tamper Example Behavior
10.2.2.4  Code Flash Firmware Integrity Check
Due to erroneous/interrupted flash write operations, the flash hardware introduces ECC errors on the device.
It is highly advisable to call HSE_SRV_ID_FW_INTEGRITY_CHECK after the application is booted to check the
integrity of HSE Firmware on the device.
Due to any reason, if the integrity check of the code flash firmware fails, the firmware sets a fatal error bit and
moves to the shutdown state. The host must assert functional reset to the device, to retry and check the health
of firmware again. This process needs to be continued, if firmware area cannot be recovered, the SBAF erases
the firmware from the system as per the handshaking logic.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
223 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 224

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
10.2.2.5  Firmware Update Error
When the firmware update operation encounters an exception, HSE core goes into shutdown mode. This also
signifies that the firmware update was interrupted and could not be completed, so the user is requested to reset
the device and re-attempt the firmware update operation.
10.2.2.6  Flash ECC error
The ECC Error is a fatal error. The HSE has the capability to read from a Flash location with ECC without
causing Exception. If it encounters such error while reading from HSE-Internal Flash, it tries to recover the data
with minimal loss.
However, exception can still occur during a direct Read/Write attempt on a Flash location with ECC. In this case,
the data recovery is not feasible. Following sections explain how HSE handles and recovers from an ECC Error
during such scenario.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
224 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 225

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
10.2.2.6.1  Encountering ECC error
Functional Reset
HSE tries to read or write a DWORD 
(8 bytes) of flash with ECC Error
Is EER Bit in MCRS set?
YES
Continue with General 
Shutdown
ECC Error in HSE Secure Flash?
Set a ECC Error Flag for 
ECC recovery after 
Functional reset. Save the 
ECC Error Location
NO
HSE Core encounters Exception
HSE starts Shutdown Process
NO
YES
Figure 87. Encountering ECC Error
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
225 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 226

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
10.2.2.6.2  Recovering from ECC error
Functional Reset
Boot Flow
Is ECC Error Flag set?
Is ECC Error in Secure Data 
Flash (SYS-IMG)?
YES
Find the Sector with ECC
Take the Backup of data other than 
the ECC Address and mark this data 
as Active
Erase the Sector with ECC
Publish Status in CONFIG_REG4
Continue with General 
Boot Flow
YES
Is ECC in HSE Backup Area?
Is ECC in HSE Active Code 
Area?
NO
NO
Erase and retake Backup
Set Handshake status as failure 
which informs SBAF on next Boot 
that the HSE FW is Invalid
YES
YES
Note: The SBAF shall try to 
recover by erasing the Active 
FW and copying the Backup 
FW and then trying to boot it 
as per Handshake Flow
Note: Continue with 
General Boot Flow until 
Exception occurs due to 
ECC in Code Flash Area 
OR until Functional Reset 
by Application
NO
NO
Figure 88. Recovering from ECC Error
For more details on HSE Firmware Handshake and SYS-IMG ECC error status, see sections HSE Firmware
Handshake and Non-notifying Error Events.
10.2.3  Warning Events
10.2.3.1  Periodic SMR Check Failed
The verification of periodic check SMR (hseSmrEntry_t#checkPeriod != 0) failed. The host can read
#HSE_SMR_CORE_BOOT_STATUS_ATTR_ID attribute to see what SMR failed.
10.2.3.2  Backup Firmware Integrity Check
When the HSE_SRV_ID_FW_INTEGRITY_CHECK is called and the backup HSE Firmware is corrupted,
firmware sends HSE_WA_DATA_FLASH_INTEGRITY_FAIL warning signal to the host but does not render the
firmware unoperational.
10.2.3.3  RNG module in HSE is not working
When HSE_WA_RNG_NOT_INIT bit is set, it indicates that the RNG module in HSE is not working. In this case,
all the HSE service that rely on a random source cannot be used. If this bit does not get cleared after several
retries, the host must issue a reset to recover the RNG module in the HSE.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
226 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 227

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
10.2.3.4  Non-Notifying Error Events
The bits in the register HSE_GPR_STATUS_ADDRESS denote that an active segment of the
SYS-IMG component was erased. Refer to S32K3xx Reference Manual) for more information on
HSE_GPR_STATUS_ADDRESS.
This is to inform the application that there is a loss of data due to ECC error or invalid data present in the sector,
and that the user needs to take necessary steps on its end to recover the data and the device state.
Bit #
Description
31-19
RFU
18
Monotonic Counter Erase Status
17
Config Data Erase Status
16
KeyStore Erase Status
15-0
Reserved for Tamper Status
Table 109. HSE data flash error logging in GPR
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
227 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 228

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
11   HSE Firmware Update
11.1  Scope
The host can update the HSE Firmware in any device lifecycle via the service defined by the structure
hseFirmwareUpdateSrv_t. The HSE Firmware can be updated in one shot or in streaming mode.
The host can also request for Flash partition swapping via the service ID
HSE_SRV_ID_ACTIVATE_PASSIVE_BLOCK (only in AB_Swap configuration).
Note:  The illustrations shown in this chapter are for S32K3x4 device family, but the concept remains generic
and is applicable for other variants as well.
11.2  Service configuration (HSE Firmware update)
The HSE Firmware update service takes in input a new HSE executable FW-IMG (encrypted and authenticated)
to be installed in HSE code Flash:
• The data fields accessMode specifies the access mode.
• The data fields streamLength must point to the length in bytes of chunk. It is used only for STREAMING
mode.
• The data fields pInFwFile must point to the first byte of the new firmware image.
Note:
Firmware update with a SYS-IMG of size greater than the one previously installed is allowed.
Firmware update is only allowed when the firmware size is greater than or equal to 128kb.
If the previous firmware installed is in Backup enable mode, then the firmware can be updated only in backup
enable mode. Similarly, if the previous firmware has a backup disable setting, then the firmware can be updated
only in backup disable mode.
FW Update Service
attribute
Data field
Characteristics
Access Mode
accessMode
Specifies the access mode, which must be:
• ONE-PASS
• START
• UPDATE
• FINISH
Chunk Size
streamLength
The length in bytes of a chunk. It is used only for STREAMING
mode. It must be at least 64 bytes or multiple of 64 bytes:
otherwise, an HSE error is returned.
• START mode: must be multiple of 64bytes.
• UPDATE mode: must be multiple of 64bytes.
• FINISH mode: can be any value.
Input Address
pInFwFile
The address of new version of HSE Firmware file:
• ONE-PASS USAGE: The address of new version of HSE
Firmware file to be updated into the HSE internal flash
memory
• STREAMING USAGE: The address of chunk to be updated
into the HSE internal flash memory
Table 110. FW Update Service Structure
Important:
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
228 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 229

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• Before calling the firmware update service, it must be ensured that the HSE has programming access to the
Flash blocks where the update operation is taking place.
• In FULL_MEM configuration, after the firmware update response is received by the host, application must
issue a reset to the device and poll for HSE_STATUS_INIT_OK before issuing any service request to the
HSE.
• For S32K389 HSE firmware update is supported only when encrypted HSE FW-IMG is flashed inside PFC0
Code flash memory.
11.3  HSE Firmware update (AB_SWAP)
In the AB_SWAP Flash configuration, both partitions are memory mapped, but the application and the HSE can
only execute code from one of them: this partition is referred to as the “active” partition. By opposition, the other
partition is referred to as “passive” partition: this partition can be programmed / updated with new application /
HSE code. The HSE service ID HSE_SRV_ID_ACTIVATE_PASSIVE_BLOCK allows the host to swap the active
and passive partitions: when calling this service, on the next reset, the passive partition becomes the active
partition, and the active partition becomes the passive partition.
The new HSE Firmware image is programmed in the selected Flash area. When calling the HSE Firmware
update service, the new firmware image is authenticated and decrypted, then stored in the passive partition, as
illustrated in the below picture. After successful execution of the HSE Firmware update service, host must call
the service ID HSE_SRV_ID_ACTIVATE_PASSIVE_BLOCK. The host must have Super User rights in order to
issue this service successfully. After completion of this service, reset should be issued and after this first reset,
the new HSE Firmware is executed.
The HSE takes the backup of itself in the new passive partition after reset post every swap service, whether FW
is updated or not. So, for these sequences, the boot time will be more by approximately 1 second as HSE FW
takes backup.
Note:
• The host application code must always be compiled for the lower address space.
• Before activating a passive partition, it must be ensured that a valid code is present in the passive partition.
• The host (application) can read the DCM status register (DCMSTAT) to identify which partition is Active and
which partition is passive; For more information, refer to the section DCM Register DCMSTAT.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
229 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 230

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
AB_SWAP HSE Firmware 
version 1 installed on device
Customer programs IVT and 
Encrypted HSE Firmware Version 2 in 
Application Active partition area
V1 HSE IMG* programs V2 HSE 
IMG* into Passive partition
After Reset Active and 
Passive partition
AB_SWAP HSE IMG* V2 take backup of 
Active partition into Passive partition.
Active 
Partition
Passive
Partition
HSE Code 
Flash
0x00400000
0x007FFFFF
0x007D4000
0x10000000
Data 
Flash
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
HSE-IMG* V1  
AB_SWAP
0x005D4000
0x005FFFFF
Application Flash
HSE Code 
Flash
Application Flash
HSE-IMG* V1  
AB_SWAP
Active 
Partition
Passive
Partition
HSE Code 
Flash
0x00400000
0x007FFFFF
0x007D4000
0x10000000
Data 
Flash
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
HSE-IMG* V1  
AB_SWAP
0x005D4000
0x005FFFFF
Application Flash
HSE Code 
Flash
Application Flash
HSE-IMG* V1  
AB_SWAP
IVT
Encrypted HSE F/w V2 
Image (AB_SWAP)
Active 
Partition
Passive
Partition
HSE Code 
Flash
0x00400000
0x007FFFFF
0x007D4000
0x10000000
Data 
Flash
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
HSE-IMG* V1  
AB_SWAP
0x005D4000
0x005FFFFF
Application Flash
HSE Code 
Flash
Application Flash
HSE-IMG* V2  
AB_SWAP
IVT
Encrypted HSE F/w V2 
Image (AB_SWAP)
Passive 
Partition
Active 
Partition
HSE Code 
Flash
0x10000000
Data 
Flash
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
HSE-IMG* V1  
AB_SWAP
Application Flash
HSE Code 
Flash
Application Flash
HSE-IMG* V2  
AB_SWAP
IVT
Encrypted HSE F/w V2 
Image (AB_SWAP)
Passive 
Partition
Active 
Partition
HSE Code 
Flash
0x10000000
Data 
Flash
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
HSE-IMG* V2  
AB_SWAP
Application Flash
HSE Code 
Flash
Application Flash
HSE-IMG* V2  
AB_SWAP
IVT
Encrypted HSE F/w V2 
Image (AB_SWAP)
0x00600000
0x005FFFFF
0x005D4000
0x00700000
0x00400000
0x00500000
0x007D4000
0x007FFFFF
0x00600000
0x005FFFFF
0x005D4000
0x00700000
0x00400000
0x00500000
0x007D4000
0x007FFFFF
Note: 
1. User code must build 
for Block 0 and Block 1 
address space always.
2. Application SW should 
take backup of itself in 
Passive Partition.
3. Valid Application code 
must be present in 
Passive Partition before 
HSE FW update.
Figure 89. Illustrating HSE Firmware update in AB_SWAP configuration
When the Flash configuration is set to AB_SWAP, it is not possible to go back to the FULL_MEM configuration.
Hence, only an AB_SWAP HSE Firmware image can be used in this configuration.
11.4  HSE Firmware update (Full_MEM)
In the FULL_MEM Flash configuration, the entire Flash memory is seen as one continuous memory partition.
The new HSE Firmware image is programmed at any address in the Flash memory before calling the HSE
Firmware update service.
In this configuration, it is also possible to change to the AB_SWAP configuration. In this case, the AB_SWAP
HSE Firmware image is programmed at a selected Flash area. When calling the HSE Firmware update service,
the new firmware image is authenticated and decrypted, then stored in two Flash memory areas corresponding
to the end of each partition, as illustrated in the below picture.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
230 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 231

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Device programmed with 
Full_Mem HSE Firmware
Customer programs IVT and 
AB_SWAP HSE Firmware 
into Application Code Flash
Full_Mem HSE-IMG* 
decrypts Authenticates and 
programs AB_SWAP HSE-FW 
to HSE Code Flash
Active 
Partition
Passive
Partition
AB_SWAP HSE Firmware takes backup of 
Active Partition into Passive Partition. 
SECURE BAF  
HSE Code 
Flash
0x00400000
0x007FFFFF
0x007F4000
Application Flash
0x007D4000
0x10000000
Data 
Flash
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
HSE-IMG*  
Full_Mem
SECURE BAF  
HSE Code 
Flash
0x00400000
0x007FFFFF
0x007F4000
Application Flash
0x007D4000
0x10000000
Data 
Flash
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
IVT
Encrypted HSE FW 
Image (AB_SWAP)
HSE-IMG*  
Full_Mem
SECURE BAF  
HSE Code 
Flash
0x00400000
0x007FFFFF
0x007F4000
0x007D4000
0x10000000
Data 
Flash
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
IVT
Encrypted HSE FW 
Image (AB_SWAP)
HSE-IMG*  
Full_Mem
HSE-IMG*  
AB_SWAP
0x005D4000
0x005FFFFF
Application Flash
HSE Code 
Flash
Application Flash
SECURE BAF  
HSE Code 
Flash
0x00400000
0x007FFFFF
0x007F4000
0x007D4000
0x10000000
Data 
Flash
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
IVT
Encrypted HSE FW 
Image (AB_SWAP)
HSE-IMG*  
Full_Mem
HSE-IMG*  
AB_SWAP
0x005D4000
0x005FFFFF
Application Flash
HSE Code 
Flash
Application Flash
After RESET Code executes 
from Active Partition
Active 
Partition
Passive
Partition
HSE Code 
Flash
0x00400000
0x007FFFFF
0x007D4000
0x10000000
Data 
Flash
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
IVT
Encrypted HSE FW 
Image (AB_SWAP)
HSE-IMG*  
AB_SWAP
0x005D4000
0x005FFFFF
Application Flash
HSE Code 
Flash
Application Flash
HSE-IMG*  
AB_SWAP
Note: 
1. User code must 
build for Block 0 
and Block 1 address 
space always.
2. Application SW 
should take backup 
of itself in Passive 
Partition.
3. Valid Application 
code must be 
present in Passive 
Block before HSE 
FW update.
Figure 90. Illustrating the change from FULL_MEM to AB_SWAP configuration
11.5  Application update (AB_SWAP)
In the AB_SWAP configuration, the host can update its application by:
• Programming the new application image in the passive partition. It must be ensured that passive area
contains the new application images, all constants and IVT at appropriate locations. This ensures that once
passive area becomes active, application image boots without any issues.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
231 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 232

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• Request the HSE for active / passive partition swapping via the service ID
HSE_SRV_ID_ACTIVATE_PASSIVE_BLOCK. On the next reset, the new application image is executed.
Important:  Both the active and passive partitions must hold the same HSE Firmware version.
Active 
Partition
Passive
Partition
HSE Code 
Flash
0x00400000
0x007FFFFF
0x007D4000
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
HSE-IMG* V1
AB_SWAP
0x005D4000
0x005FFFFF
Application Flash
HSE Code 
Flash
Application Flash
HSE-IMG* V1
AB_SWAP
Note: 
1. Application code must 
build for Block 0 and 
Block 1 address space 
always.
2. Application must issue 
Reset after Passive 
Partition activation 
command. i.e. Between 2 
consecutives Passive 
Partition activation 
command reset must be 
given.
Application SW V1
Active 
Partition
Passive
Partition
HSE Code 
Flash
0x00400000
0x007FFFFF
0x007D4000
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
HSE-IMG* V1
AB_SWAP
0x005D4000
0x005FFFFF
Application Flash
HSE Code 
Flash
Application Flash
HSE-IMG* V1
AB_SWAP
Application SW V1
Application SW V2
Passive 
Partition
Active 
Partition
HSE Code 
Flash
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
HSE-IMG* V1
AB_SWAP
Application Flash
HSE Code 
Flash
Application Flash
HSE-IMG* V1
AB_SWAP
Application SW V1
Application SW V2
0x00600000
0x005FFFFF
0x005D4000
0x00700000
0x00400000
0x00500000
0x007D4000
0x007FFFFF
App SW V1 is programmed 
in Device with Block 0 and 1 
is Active Partition
Customer programs Application SW 
V2 in Passive Partition then call 
srv_id 
HSE_SRV_ID_ACTIVATE_PASSIVE_B
LOCK, And issue reset.
After Reset, Application SW V2 gets 
control and becomes Active.
Passive 
Partition
Active 
Partition
HSE Code 
Flash
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
HSE-IMG* V1
AB_SWAP
Application Flash
HSE Code 
Flash
Application Flash
HSE-IMG* V1
AB_SWAP
Application SW V3
Application SW V2
0x00600000
0x005FFFFF
0x005D4000
0x00700000
0x00400000
0x00500000
0x007D4000
0x007FFFFF
Customer programs Application SW V3 in 
Passive Partition then call srv_id 
HSE_SRV_ID_ACTIVATE_PASSIVE_BLOCK, 
And issue reset.
Active 
Partition
Passive
Partition
HSE Code 
Flash
0x00400000
0x007FFFFF
0x007D4000
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
HSE-IMG* V1
AB_SWAP
0x005D4000
0x005FFFFF
Application Flash
HSE Code 
Flash
Application Flash
HSE-IMG* V1
AB_SWAP
Application SW V3
Application SW V2
After Reset, Application SW V3 gets 
control and becomes Active.
Figure 91. Illustrating application update in AB_SWAP configuration
The host can roll back to a previous version of the application image by simply calling the partition swapping
service. On the next reset, the application image in the passive partition is executed.
User must ensure that passive area must contain the valid application image, all constants and IVT at
appropriate locations. This is to ensure that once passive area become active, application image gets booted
without any issues.
Important:  After every partition switch operation, the boot time for the HSE will be more by approximately 1
second.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
232 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 233

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Active 
Partition
Passive
Partition
HSE Code 
Flash
0x00400000
0x007FFFFF
0x007D4000
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
0x00500000
0x00600000
0x00700000
HSE-IMG*  
AB_SWAP
0x005D4000
0x005FFFFF
Applicati
on Flash
HSE Code 
Flash
Applicati
on Flash
HSE-IMG*  
AB_SWAP
Application SW V1
Application SW V2
Application SW V2 running on Active 
Partition[2-3].
Application wants to rollback to V1 so call 
srv_id 
HSE_SRV_ID_ACTIVATE_PASSIVE_BLOCK
and then issues Reset.
Passive
Partition
Active 
Partition
HSE Code 
Flash
Block 0
1 MB
Block 1
1 MB
Block 2
1 MB
Block 3
1 MB
HSE-IMG*  
AB_SWAP
Applicati
on Flash
HSE Code 
Flash
Applicati
on Flash
HSE-IMG*  
AB_SWAP
Application SW V1
Application SW V2
0x00600000
0x005FFFFF
0x005D4000
0x00700000
0x00400000
0x00500000
0x007D4000
0x007FFFFF
After Reset, Application SW V1 gets 
control as Block[0
-1] becomes 
Active Partition.
Figure 92. Illustrating roll back to previous version of application image
11.6  HSE Firmware header format
The HSE Firmware is delivered for a specific Flash memory configuration. The first four bytes in the FW-IMG
define the required Flash configuration as described in the below tables.
Byte 0
Byte 1
Byte 2
Byte 3
0xDA
0xFF
0xFF
0x60
Table 111. FW-IMG header format (FULL_MEM)
Byte 0
Byte 1
Byte 2
Byte 3
0xDB
0xFF
0xFF
0x60
Table 112. FW-IMG header format (AB_SWAP)
11.7  Secure-BAF update
The host can update the Secure-BAF via the service defined by the structure hseSbafUpdateSrv_t in one
shot or in streaming mode.
The new Secure-BAF image is programmed at any address in the application Flash memory before calling the
Secure-BAF update service. The new firmware image is authenticated and decrypted, then stored in the HSE
code Flash memory.
On the next reset, the new Secure-BAF will boot the HSE Firmware.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
233 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 234

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Note:
• NXP recommends to update Secure-BAF in one shot mode.
• Secure-BAF update must be performed in a stable environment because any failure in the update process
causes the bricking of device.
• Secure-BAF update service is only applicable for FULL_MEM configuration.
• Secure-BAF update to an older version is not allowed.
• If the device has an older Secure-BAF, some functionality of HSE Firmware might be restricted. Secure-BAF
must be updated to enable such functionality. For more details, see section Section 14.7.
11.8  Service description
The Secure-BAF update service takes in input a new Secure-BAF executable image (encrypted and
authenticated) to be installed in HSE code Flash:
• The data fields accessMode specifies the access mode.
• The data fields streamLength must point to the length in bytes of chunk. It is only used for STREAMING
mode.
• The data fields pInFwFile must point to the first byte of the new Secure-BAF image.
FW Update Service attribute
Data field
Characteristics
Access Mode
accessMode
Specifies the access mode, which must be:
• ONE-PASS
• START
• UPDATE
• FINISH
Chunk Size
streamLength
The length in bytes of a chunk. It is used only for STR
EAMING mode. It must be at least 64 bytes or multiple of 64
bytes:
otherwise, an HSE error is returned.
• START mode: must be multiple of 64bytes.
• UPDATE mode: must be multiple of 64bytes.
• FINISH mode: can be any value.
Input Address
pInFwFile
The address of new version of Secure-BAF file:
• ONE-PASS USAGE: The address of new version of HSE
Firmware file to be updated into the HSE internal flash
memory
• STREAMING USAGE: The address of chunk to be
updated into the HSE internal flash memory
Table 113. Secure-BAF Update Service Structure
Important:
Before calling the Secure-BAF update service, it must be ensured that the HSE has programming access to the
Flash blocks where the update operation is taking place.
This service must be executed in an environment with stable power supply. Any reset during this service
execution can brick the device.
One shot mode is recommended for this service request.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
234 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 235

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Byte 0
Byte 1
Byte 2
Byte 3
0xDC
0xFF
0xFF
0x60
Table 114. Secure-BAF header format
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
235 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 236

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
12   Security Policies
12.1  Scope
The services offered by the HSE firmware operate under certain security policies, summarized in this section.
12.2  Key usage
The use of cryptographic key is enforced by:
• Its storage location (that is, its catalog)
• Its usage flags
• Its SMR verification map and the verification status of the associated SMR
• Its MU instance map that defines possible service channels to make use of a key
12.3  Key import / update
• When a key is imported encrypted, the decryption key (provisioning key) must:
– Be declared in a key group (NVM or RAM) owned by the same owner as the target key handle
– Refer to a non-empty key slot having its key usage flags HSE_KF_USAGE_KEY_PROVISION and
HSE_KF_USAGE_DECRYPT set
• When a key is imported with a proof of authenticity, the authentication key (provisioning key) must:
– Be declared in a key group (NVM or RAM) owned by the same owner as the target key handle
– Refer to a non-empty key slot having its key usage flags HSE_KF_USAGE_KEY_PROVISION and
HSE_KF_USAGE_VERIFY set
• An NVM cryptographic key can be updated if it is not write-protected, and if its update counter is not
saturated.
• The RAM provisioning keys can be imported only authenticated and can be used only to import RAM keys
(cannot be used to import NVM keys).
• SHE keys can only be provisioned via the SHE services
• The key import depends on system rights (Super User or User rights).
• The key properties (keyInfo) along with the public key values are always imported in plain format.
• Key import restrictions when the host is granted with SU rights:
– NVM keys:
–
In empty slots, NVM keys can be imported in an encrypted format only with authentication; a plain key
can be imported with/without authentication (public keys must be imported in plain).
–
In non-empty slots, NVM keys can be imported (overwritten) in plain/encrypted, only authenticated.
– RAM keys:
–
RAM keys can be imported in an encrypted format only with authentication. A plain key can be imported
with/without authentication. Exception: RAM provisioning keys can be imported only authenticated.
• Key import restrictions when the host is granted with User rights:
– NVM keys:
–
NVM secrets and public/private pairs can be imported only encrypted and authenticated. For a key
pair, the private value must be encrypted, and public value(s) unencrypted. NVM secrets imported from a
signed key container MUST include the key properties (keyInfo) in the container.
–
NVM public keys can be imported in plain, only authenticated. NVM public key imported from a signed
key container can/cannot include the keyInfo in the container.
– RAM keys:
–
RAM secret keys can be imported in an encrypted format only with authentication. A plain secret can be
imported with/without authentication.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
236 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 237

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
–
Public/private key pairs can be imported only authenticated; private value encrypted, and public
value(s) unencrypted.
–
Public keys can be imported in plain, only authenticated. Authentication is optional if HSE_RAM_PUB_
KEY_IMPORT_POLICY_ATTR_ID attribute is set to HSE_KM_POLICY_ALLOW_RAM_PUB_KEY_
IMPORT.
12.4  Key export
• Only the keys that have the HSE_KF_ACCESS_EXPORTABLE set can be exported.
• The private part of a key pair (e.g. RSA or ECC) can NOT be exported (the private part is never disclosed to
the host).
• Provisioning/Authorization keys are NOT exportable (HSE_KF_ACCESS_EXPORTABLE flag is ignored).
• NVM/RAM secret keys can be exported only encrypted, with/without authentication.
• NVM/RAM public keys (from key pair or public key slots) can be exported in plain; the authentication is
optional.
• NVM keys cannot be exported using RAM provisioning keys.
• To export an encrypted/authenticated NVM key, the provided provisioning key must have the same group
owner as the exported NVM key (not applicable for RAM keys).
• When the SHE key RAM_KEY within the RAM key catalog has been updated using the SHE key update
protocol, it cannot be exported.
• NVM SHE keys cannot be exported.
12.5  Memory areas and isolation between hosts
Memory isolation between hosts is achieved at MU instance level as follows:
• Messaging Unit Peripheral – each MU can be dedicated to a specific host via platform XRDC-PDAC.
• Input and output data linked via pointers in the service descriptor (these are typically pointers to SRAM or
DRAM) can be isolated between hosts using the HSE_MEM_REGIONS_PROTECT_ATTR_ID attribute. The
host can communicate to HSE the memory ranges that are associated with each MU instance. If provided, the
HSE dismisses the data that falls outside the ranges for a particular MU instance. This attribute must be set
for each run-time session (SET_ONCE_ATTR attribute type).
For more details about attribute configuration refer to HSE System Attributes to Configure Security Policies and
HSE Service API Reference Manual.
The following default restrictions apply on memory areas:
• The service descriptor and any parameter provided as pointer to the HSE cannot be in memory areas within
the secure NVM or secure RAM.
• The address in output parameters can be in the following memory areas:
– System RAM
– Host ITCMs and DTCMs (using alternate addresses)
• The data provided by the host (including the service descriptor) must be provided from non-cacheable
memory ranges.
• The input parameters provided as pointers for the services must be in the memory areas specified above for
service descriptor.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
237 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 238

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
12.6  SMR installation
• In User mode, the SMR can be updated only changing the pSmrSrc, smrSize and pInstAuthTag. Any other
configuration fields (such as keyHandle, configFlags, verifMethod, versionOffset etc.) of a SMR entry can only
be updated if the host has SuperUser rights.
• A Core Reset Entry can be installed/updated only having Super User rights.
12.7  User/Super User rights
• When the host is granted with User rights, certain services are not accessible.
• The host can request to be temporarily granted with Super User rights based on the knowledge of a secret or
private key.
• NVM SHE keys can be erased only if the host has been granted with Super User rights using the SHE
MASTER_ECU_KEY. Non-SHE NVM keys can be erased only having Super User rights.
12.8  Debug
• Debugging the HSE is not possible.
• Debugging the host can either be completely disabled or protected (based on a password or key) via an
authentication mechanism that can either be static (use of a password) or dynamic (use of a key).
• If the host debugger is opened, the keys that has the HSE_KF_ACCESS_WRITE_PROT flag set cannot be
used.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
238 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 239

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
13   Platform Specific Behavioral and Features
13.1  Scope
The sections below describe the features and behaviors that are specific for different platforms.
13.2  AES ACCEL support
The Advanced Encryption Standard Accelerator (AES_ACCEL) module is a subsystem that provides DMA-
controlled safe and secure AES acceleration. It consists of an AES engine with integrated keystore (ACE)
and two DMA controllers. An application can be assigned a set of DMA channels to feed parameters for
cryptographic operations and receive the status and output data.
For more details about the AES_ACCEL refer to AES_ACCEL Subsystem Reference Manual.
In the following sections, the "Managed Security Component" (MSC) term is used for any hardware accelerator
on the host-side (such as AES_ACCEL) that uses keys managed by HSE firmware.
13.2.1  AES_ACCEL start-up
Before using the AES_ACCEL module, it must be enabled by the application core as follow:
• The application must enable the AES_ACCEL clock (at clock initialization phase)
The following MC_ME slots must be explicitly enabled:
PRTN1_COFB3_CLKEN[REQ112]
PRTN1_COFB3_CLKEN[REQ113]
PRTN1_COFB3_CLKEN[REQ114]
PRTN1_COFB3_CLKEN[REQ115]
For more details, refer S32K3xx Reference Manual chapter MC_ME.
• The application must enable the ACE hardware module setting the “enable bit” (bit 0) in the ace_control
register (refer to refer to AES_ACCEL Subsystem Reference Manual.
After enabling the ACE module, the NVM MSC keys can be loaded from SYS-IMG into MSC keystore by calling
the hsePushMscKeySrv_t service with the hseKeyHandle parameter equal to HSE_INVALID_KEY_HANDLE.
13.2.2  The Key Handle Translation Table (KHTT)
The MSC keys can be provisioned only from the HSE subsystem, through a private bus which is hardened
against side channel attacks. The MSC keystore contains 80 X AES128 keys and the associated key properties.
Without considering the key properties, it can be seen as an array of 80 elements, the size of each element
being 16 bytes; e.g keystore [80][16].
The configuration of MSC keys starts with the definition of the Key Handle Translation Table (KHTT). This table
is statically defined by the application at configuration phase. Each KHTT entry contains the correspondence
between HSE key handles and MSC key slots (e.g. ACE key slots), and additional proprieties.
The keys that are configured to be used with MSC accelerator (using the KHTT table) have the following
proprieties:
• The keys specified by KHTT table are mirrored by HSE subsystem in the MSC keystore. This means that any
key update/erase is automatically performed on both key stores (HSE and MSC key stores).
• The key bit length can only be 128 or 256 bits. The 256-bit key group cannot get a key of 128-bit size. The
maximum number of MSC AES keys is 80 x 128-bit keys or 40 x 256-bit keys or any combination in between.
An AES256 key uses two 16-byte entries.
– The MSC subsystem accesses a key selecting a key slot in the range 0 to 79 (using the mscKeySlotIdx
index). The KHTT table maps each HSE key handle to MSC key slot.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
239 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 240

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
• Before provisioning any AES_ACCEL key, the application must enable the AES_ACCEL clock (at clock
initialization phase).
An KHTT entry is defined by hseKHTTEntry_t structure (refer to AES_ACCEL Subsystem Reference Manual)
and has the following fields:
Key attribute
Type
Description
hseKeyHandle
32-bit integer
The key handle used with HSE keystore. The key handles can point to NVM
or RAM AES keys.
Note: The key bit length of HSE key can only be 128 or 256 bits (e.g. the
256 bit key group cannot get a key of 128 bit size).
mscKeySlotIdx
8-bit integer
The MSC key slot index. The MSC subsystem accesses a key selecting a
key slot in the range 0 to 79. HSE uses mscKeySlotIdx index to push the
key specified by the hseKeyHandle field.
Note:  Given that an AES256 key occupies 2 MSC key slots, the key slot
that follows an AES256 key slot must be placed at N+2 (e.g. keystore[N
+2]), where N is the AES256 key slot index.
mscInstance
8-bit integer
The MSC instance identifier of the hardware accelerator on the host side.
On S32K388, this field is ignored (only one instance is available)
aceDidFlags
16-Bit field
16-bit for Domain ID (DID) filtering. The aceDidFlags is compared against
"1<<bus DID value".
On the buses the DID value is 4 bits only. The DID comparison works in this
way: if bus DID is equal 4, it means bit 4 in aceDidFlags must be set to be
able to use the key.
restrictFlags
8-Bit field
Specifies 1 bit:
Bit0: HSE_KHTT_RESTRICT_PUSH_MANY restriction. This restriction
applies when more MSC keys are pushed at once (refer to section 14.2.1.
4):
• If it is clear to 0, HSE loads the MSC key when the hsePushMscKey
Srv_t service is called with the hseKeyHandle parameter equal to HSE_
INVALID_KEY_HANDLE.
• If it is set to 1, HSE doesnot load the MSC key when the hsePushMsc
KeySrv_t service is called with the hseKeyHandle parameter equal to
HSE_INVALID_KEY_HANDLE.
Bit1..7: reserved
Table 115. hseKHTTEntry_t structure
Important:
If the keyFlags of an HSE key is set to any of the HSE_KF_USAGE_VERIFY and HSE_KF_USAGE_SIGN
flags, the key can only be used with CMAC operation on MSC side.
If the DID input received over AES_ACCEL buses are not matching the above properties, the key cannot be
used.
The host can map multiple HSE key handles to only one MSC slot, but it is application responsibility to push the
key (using the hsePushMscKeySrv_t service) before using it with the MSC accelerator.
The table below shows an example of how to map each hseKeyHandle to MSC mscKeySlotIdx:
• mscKeySlotIdx starts from zero
• If the previous key size is 16 bytes, the mscKeySlotIdx = previous mscKeySlotIdx + 1
• If the previous key size is 32 bytes, the mscKeySlotIdx= previous mscKeySlotIdx + 2
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
240 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 241

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
hseKeyHandle
mscKeySlotIdx
Number of ACE key slots
0x00010100
0
1 X 16-byte slot (NVM)
0x00010101
1
1 X 16-byte slot (NVM)
0x00010200
2
2 X 16-byte slot (NVM)
0x00010201
4[1]
2 X 16-byte slot (NVM)
0x00020100
6[1]
1 X 16-byte slot (RAM)
0x00020200
7
2 X 16-byte slot (RAM)
Table 116. HSE key handle vs ACE key index mapping
[1]
The previous key size is 32 bytes, the mscKeySlotIdx = previous mscKeySlotIdx + 2.
Note:
The key handles can be NVM or RAM keys.
13.2.3  KHTT configuration service
The host can request to configure the KHTT table via the service defined by the structure hseConfigKHTTSrv_t.
The host must provide the following parameters:
• The number of KHTT entries (numOfKHTTEntries parameter). It shall be maximum 80 entries.
• Pointer to the KHTT table that contains numOfKHTTEntries entries of type hseKHTTEntry_t (refer to
hseKHTTEntry_t structure).
Before configuring the MSC keys, the following shall be considered:
• The HSE key catalogs must be formatted
• The application must enable the MSC clock
• The host must have Super User rights
Once the KHTT entries have passed the validation, the KHTT table is stored in SYS-IMG.
For more details, refer to AES_ACCEL Subsystem Reference Manual.
13.2.4  Push MSC key(s) service
The host can request to push one or more HSE keys in the corresponding MSC key slots via the service defined
by the structure hsePushMscKeySrv_t.
The host must provide as parameter the hseKeyHandle:
• The hseKeyHandle must be found in the KHTT table
• The pushed key(s) must not be empty
• If hseKeyHandle is different from HSE_INVALID_KEY_HANDLE, HSE pushes a single key corresponding to
hseKeyHandle
• If hseKeyHandle equals HSE_INVALID_KEY_HANDLE, HSE pushes all key slots (not empty) from KHTT
table that do not have the HSE_KHTT_RESTRICT_PUSH_MANY flag set.
– Note:  This option can be used to load (at initialization time) the NVM HSE keys whose handles are found in
the KHTT table that do not have the HSE_KHTT_RESTRICT_PUSH_MANY flag set.
For more details, refer to HSE Service API Reference Manual.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
241 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 242

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
14   Device Specific Parameters
14.1  Scope
This section documents the parameters specific to HSE_B subsystem.
14.2  System attributes
14.2.1  IVT Start Addresses
The IVT start address can be selected from one of the values provided in the below table. At reset, the HSE
searches for the first valid IVT header tag starting from the lowest address.
Device
Start addresses (FULL_
MEM)
Start addresses (AB_
SWAP)
Start addresses (Partial
AB_SWAP)
S32K310
0x00400000,
0x10000000
0x00400000,
0x10000000
NA
S32K311
0x00400000,
0x00480000,
0x10000000
0x00400000,
0x10000000
NA
S32K341
0x00400000,
0x10000000
0x00400000,
0x10000000
NA
S32K312
S32K342
S32K322
0x00400000,
0x00500000,
0x10000000
0x00400000,
0x10000000
NA
S32K344
S32K324
S32K314
0x00400000,
0x00500000,
0x00600000,
0x00700000,
0x10000000
0x00400000,
0x00500000,
0x10000000
NA
S32K374
S32K394
0x00400000,
0x00600000
0x00400000,
0x00600000,
0x10000000
NA
S32K396
S32K376
0x00400000,
0x00600000,
0x00800000
0x10000000
0x00400000,
0x00600000,
0x10000000
NA
S32K356
S32K336
0x00400000,
0x00600000,
0x00800000,
0x10000000
0x00400000,
0x00600000,
0x10000000
0x00400000,
0x00600000,
0x00800000,
0x10000000
S32K388
S32K358
S32K348
S32K338
0x00400000,
0x00600000,
0x00800000,
0x00A00000
0x00400000,
0x00600000,
0x10000000
0x00400000,
0x00600000,
0x00800000,
0x10000000
Table 117. IVT start address
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
242 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 243

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Device
Start addresses (FULL_
MEM)
Start addresses (AB_
SWAP)
Start addresses (Partial
AB_SWAP)
S32K328
0x10000000
S32K389
0x00400000,
0x00600000,
0x00800000,
0x00A00000
0x10000000
0x00400000,
0x00600000,
0x10000000
0x00400000,
0x00600000,
0x00800000,
0x10000000
Table 117. IVT start address...continued
14.2.2  IVT Structure
The below table provides the IVT structure, with the following notes:
• The pointers for Apps must match the VTOR alignment restrictions. Refer to S32K3xx Reference Manual for
more information.
• All other pointers must align on a 32-bit boundary (that is, must be a multiple of 4 bytes).
• The reserved fields must be cleared to 0xFF.
More descriptions of the structures within or pointed to are described in the following tables in this section.
Note:  If IVT is not provided, placing the FW-IMG at address 0x00400000 (also referred to as IVT_START)
starts the firmware installation.
Offset
Byte size
Category
Description
Value/Value type
0x00
4
Tag
IVT header tag
Magic number(0x5AA55AA5)
0x04
4
Configuration
BCW
Bit field
0x08
4
Reserved
0x0C
4
Executable
Apps for BOOT_TARGET bit #0
Pointer
0x10
4
Reserved
0x14
4
Executable
Apps for BOOT_TARGET bit#1
Pointer[1][2][3]
0x18
4
Reserved
0x1C
4
Executable
Apps for BOOT_TARGET bit#2
Pointer [2][3]
0x20
4
Reserved
0x24
4
Configuration
LCW
Pointer[4]
0x28
4
Executable
Apps for BOOT_TARGET bit #8
Pointer [3]
0x2C
4
Executable
FW_IMG
Pointer[5]
0x30
4
Executable
AppBL
Pointer
0x34
12
Reserved
0x40
4
Executable
Start Address of Application Core
for Secure Recovery mode.
Pointer
0x44
4
Length
Length of Recovery Application
32-bits data
0x48
156
Reserved
0xE4
12
12-byte random vector
(IV)
Initialization vector value to be
used in the calculation of GMAC.
Byte array [6]
Table 118. IVT structure
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
243 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 244

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Offset
Byte size
Category
Description
Value/Value type
IV value is also included in GMAC
calculation.
0xF0
16
TAG
Authentication tag (GMAC)
Byte array
Table 118. IVT structure...continued
[1]
Applicable for devices that support 2 Application cores.
[2]
Applicable for devices that support 3 Application cores.
[3]
Applicable for devices that support 4 Application cores.
[4]
This is a pointer to LCW, not the LCW value itself.
[5]
Pointer to FW-IMG is only valid for FULL_MEM configuration.
[6]
The IV must be randomly generated every time the GMAC is calculated.
14.2.2.1  The Boot Configuration Word (BCW)
Bit #
Description
Remarks
31
RFU
30
RFU
…
…
10
BACKUP_DISABLE[1]
Used for Backup Enable and Backup Disable.
• When 0: HSE backup feature is enabled.
• When 1: HSE backup feature is disabled.
9
FW_USAGE_FLAG_PROGRAM [2]
Used to enable the HSE Firmware Usage feature flag
in UTEST.
• When 0: HSE Firmware Usage Feature flag is not
programmed.
• When 1: HSE Firmware Usage Feature flag is
programmed in UTEST if not already programmed.
Also, removes the requirement to program 0xA5
marker in DCMRWP1 register during HSE Firmware
Installation via MU Interface.
8
BOOT_TARGET (CM7_3_ENABLE) [3]
Enable CM7_3 application core ungating (non-secure
boot).
• When 0: CM7_3 is gated.
• When 1: CM7_3 is ungated at address in IVT.
7
RESET_RECOVERY_MODE[2]
Used to disable entry into recovery mode because
of consecutive resets. See Disable Entry into Reset
Recovery Mode for more details.
6
DISABLE_SECURE_RECOVERY_MODE [4]
Used to skip the Secure Recovery Mode in the
recovery mode sequence.
• When 0: Secure Recovery Enable.
• When 1: Secure Recovery Disable.
For more details, refer Secure Recovery Mode
5
SWT0_ENABLE
Used to enable Application SWT0 before application
core ungating.
• When 0: Application SWT0 is not enabled.
• When 1: Application SWT0 is enabled before
ungating application cores.
4
PLL_ENABLE[5][6]
Used to enable PLL during Secure Boot.
• When 0: No clock configuration done.
Table 119. BCW bit mapping
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
244 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 245

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Bit #
Description
Remarks
• When 1: Configure FXOSC and PLL for Secure
Boot.
3
BOOT_SEQ
Secure Boot Enabled/Disabled.
• When 0: Secure Boot disabled.
• When 1: Secure Boot enabled.
2
BOOT_TARGET (CM7_2_ENABLE) [3][7]
Enable CM7_2 application core ungating (non-secure
boot).
• When 0: CM7_2 is gated.
• When 1: CM7_2 is ungated at address in IVT.
1
BOOT_TARGET (CM7_1_ENABLE) [8][3][7]
Enable CM7_1 application core ungating (non-secure
boot).
• When 0: CM7_1 is gated.
• When 1: CM7_1 is ungated at address in IVT.
0
BOOT_TARGET (CM7_0_ENABLE)
Enable CM7_0 application core ungating (non-secure
boot).
• When 0: CM7_0 is gated.
• When 1: CM7_0 is ungated at address in IVT.
Table 119. BCW bit mapping...continued
[1]
When doing a firmware update for a full mem layout, the old HSE image and the new HSE image must have the same backup disable setting, otherwise
the update will fail with error HSE_SRV_RSP_NOT_SUPPORTED.
[2]
when doing a firmware update for a full mem layout, the old HSE image and the new HSE image must have the same backup disable setting, otherwise
the update will fail with error HSE_SRV_RSP_NOT_SUPPORTED
[3]
Applicable for devices which support 4 Application cores.
[4]
Disable the secure recovery mode feature. HSE only attempts JTAG based recovery mode to recover the device in bricking scenarios as explained in
“Recovery Mode” section.
[5]
FXOSC enablement flag must be enabled in UTEST area as described inHSE Service API Reference Manual
[6]
PLL is configured only when BOOT_SEQ==1
[7]
Applicable for devices which support 3 Application cores.
[8]
Applicable for devices which support 2 Application cores.
Note:  If Lockstep is enabled for the device, Firmware does not boot M7_1 core.
14.2.2.2  Clock Frequency Options for Devices
HSE Firmware supports clocking options based on devices. These clk sttings are done by HSE as part of boot
process
Device
Options Available
S32K311
Option B
S32K312
Option B
S32K342
Option A and Option B
S32K344
Option A and Option B
S32K396
Option A+ and Option B
S32K358
Option A+ and Option B
S32K388
Option A++
Table 120. PLL Configuration in HSE Firmware
The following tables list the frequencies of Clocks to HSE Core and Application Cores (CM7) in different devices
in different clocking options.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
245 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 246

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Clock
HSE_CLK
CORE_CLK
Option A
80MHz
160MHz
Option B
120MHz
120MHz
Option A+ (only in
S32K358 and its family)
120MHz
240MHz
Table 121. Clock Frequencies for various clocking options in S32K3xx devices (except S32K3X6 and
S32K388)
Only Option A+ is available in the S32K358 family.
Clock
HSE_CLK
CM7_CORE_CLK
Option A+
80MHz
320MHz
Option B
120MHz
240MHz
Table 122. Clock Frequencies for various clocking options in the S32K3X6 family of devices
Clock
HSE_CLK
CORE_CLK
CM7_CORE_CLK
Option A++
160MHz
160MHz
320MHz
Table 123. Clock Frequencies for various clocking options in the S32K388 family of devices
Clock
HSE_CLK
CORE_CLK
CM7_CORE_CLK
Option A++
160MHz
160MHz
320MHz
Table 124. Clock Frequencies for various clocking options in the S32K389 devices
Note:
If the user wants to enable Option B/A+(S32K358)/ A++(S32K388/S32K389 ), then the host application
must program the UTEST Miscellaneous register (UTEST_MISC): dcf_client_utest and must configure the
HSE_CLK_MODE_AND_GSKT_CTRL (bit 30-29) in this register.
For more details, refer to DCF Clients information available with Device Reference Manual.
To get the confirmation that the DCF record has been successfully programmed, the user must check the DCM
GPR register DCMROF21 at address 0x402AC350U has bit 20 set to ‘1’.
For the S32K312 on firmware installation/update /SBAF update the user shall enable the reduce clock mode,
expect a HSE Init complete. Post update and successful HSE Init, user shall disable the Reduced Clock Mode
to allow application to benefit from the maximum HSE performance. If user maintain the Reduced Clock Mode
enabled, the applications will suffer both in booting and crypto algorithm performance.
14.2.2.3  The LifeCycle Configuration Word (LCW)
LCW is a 32-bit value that specifies the LC state advancement:
• LCW = 0xDADADADA advances LC to OEM_PROD
• LCW = 0xBABABABA advances LC to IN_FIELD
The below table maps the BOOT_TARGET bits with the CPU subsystem to release from reset when
BOOT_SEQ equals 0, and when the corresponding BOOT_TARGET bit is set to 1.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
246 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 247

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
14.2.2.4  Boot Targets
BOOT_TARGET bit #
S32K3xx
0
M7_0
1
M7_1 [1][2][3]
2
M7_2 [1][2]
8
M7_3 [3]
Table 125. BOOT_TARGET vs. CPU subsystem
[1]
Applicable for devices that support 2 Application cores.
[2]
Applicable for devices that support 3 Application cores.
[3]
Applicable for devices that support 4 Application cores.
[*] If Lockstep is enabled for the device, Firmware does not boot M7_1 core.
14.2.2.5  AppBL Structure
Offset
Byte size
Category
Description
Value / Value type
0x00
1
Tag
AppBL header tag
Magic number (0xD5)
0x01
2
Reserved
0x03
1
Tag
AppBL version
Magic number (0x60)
0x04
4
Reserved
0x08
4
Configuration
Start address (in Flash) Pointer
0x0C
4
Configuration
AppBL size (N)
32-bit integer
0x10
1
Configuration
Core identifier (see
Subsystem vs core
identifiers)
Value
0x11
47
Reserved
0x40
N[1]
Executable
AppBL content (in
plain)
Executable
N +0x40
12
IV
12-byte random vector
Byte array[2]
N +0x4C
16
Tag
Authentication tag
(GMAC)
Byte array
Table 126. AppBL structure
[1]
As defined in offset 0x0C.
[2]
This must be a 12-byte random value that must be used as an IV in the calculation of GMAC. This field is also included in GMAC calculation.
14.3  Recovery mode Start address
The below table lists the JTAG based Recovery mode Start address in HSE_B.
Description
Start Address
JTAG_RECOVERY_START_ADDRESS
0x20400100
Table 127. JTAG based Recovery mode Start address
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
247 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 248

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
14.4  Size of the HSE Firmware
The below table lists the size of the standard HSE Firmware.
Flash Memory Configuration
HSE FW Size
Sys Image Size
FULL_MEM
128 KB
40 KB
AB_SWAP
176 KB
40 KB
Table 128. Current size of the HSE Firmware
Flash Memory Configuration
Size
FULL_MEM
192 KB
AB_SWAP
256 KB
Table 129. Maximum size of the HSE Firmware
For AB_SWAP configuration, the reason that the HSE Firmware image having more size is because it includes
the SBAF component that has the size of 48 KB.
For custom firmware, the code size of HSE firmware and sys image can change. Contact the NXP support team
to get more details on custom firmware.
HSE can claim the following anytime:
• Code Flash: 240K (192K+48K)
• Data Flash: 192K
Note:
With increasing market demand for additional features and security improvements HSE can expand its secure
memory regions to 192KB in both Code Flash & Data Flash (when Backup Feature is enabled) for future
releases.
14.5  Cryptographic services
The below table lists the hash primitives supported in HSE_B.
Hash primitive
HSE_B
HW accelerated
SHA1
Supported
Yes
SHA224 / SHA256
Supported
Yes
SHA384 / SHA512
Supported
No
SHA3-224 / SHA3-256
Supported
No
SHA3-384 / SHA3-512
Supported
No
Table 130. Hash primitives supported (HSE_B)
HMAC primitive
HSE_B
HW accelerated
HMAC_SHA1
Supported
Yes
HMAC_SHA224 / SHA256
Supported
Yes
HMAC_SHA384 / SHA512
Supported
No
Table 131. HMAC primitives supported (HSE_B)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
248 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 249

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
For a detailed description of each of the hash primitives listed above, refer to Secure Hash Standard (SHS) and
SHA-3 Standard .
For GCM operations, the NIST SP800-38D Standard recommends using the IV of length 96 bits.
For any IV size different from 96 bits, the authentication tag generated by the GCM encryption operation might
not be correct. In GCM decryption operations, the authentication check may fail.
14.6  Specific parameters (S32K3XX)
14.6.1  On-chip secure NVM
The below table maps the on-chip Flash memory areas used by the HSE subsystem.
Device
Flash area
Start address
Size
HSE data flash
0x10016000
168KB
Common
HSE configuration (UTEST)
0x1B000000
8KB
S32K311,
S32K310
HSE code flash
0x004D4000
176KB
S32K312,
S32K342,
S32K322,
S32K341
HSE code flash
0x005D4000
176KB
S32K344,
S32K324,
S32K314
HSE code flash
0x007D4000
176KB
S32K396,
S32K376,
S32K394,
S32K374
HSE code flash
0x009D4000
176KB
S32K388,
S32K358,
S32K348,
S32K338,
S32K328,
S32K356,
S32K336
HSE code flash
0x00BD4000
176KB
S32K389
HSE code flash
0x00FD0000
192KB
Table 132. Secure NVM mapping (FULL_MEM)
Device
Flash area
Start address
Size
HSE data flash
0x10020000
128KB
Common
HSE configuration (UTEST)
0x1B000000
8KB
HSE code flash (passive
area)
0x004D4000
176KB
S32K311,
S32K310,
HSE code flash (active area)
0x00454000
176KB
Table 133. Secure NVM mapping (AB_SWAP)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
249 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 250

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Device
Flash area
Start address
Size
HSE code flash (passive
area)
0x005D4000
176KB
S32K312,
S32K342,
S32K322,
S32K341
HSE code flash (active area)
0x004D4000
176KB
HSE code flash (passive
area)
0x007D4000
176KB
S32K344,
S32K324,
S32K314
HSE code flash (active area)
0x005D4000
176KB
HSE code flash (passive
area)
0x009D4000
176KB
S32K396,
S32K376,
S32K394,
S32K374
HSE code flash (active area)
0x007D4000
176KB
HSE code flash (passive
area)
0x00BD4000
176KB
S32K388,
S32K358,
S32K348,
S32K338,
S32K328,
S32K356,
S32K336
HSE code flash (active area)
0x007D4000
176KB
HSE code flash (passive
area)
0x00FD0000
192KB
S32K389
HSE code flash (active area)
0x009D0000
192KB
Table 133. Secure NVM mapping (AB_SWAP)...continued
* The sizes mentioned are only valid for Standard Firmware.
The below table maps the on-chip Flash memory areas used by the Application.
Device
Flash area
Start address
Size
Common
APP code flash
0x10000000
88KB
S32K310
APP code flash
0x00400000
512 KB
S32K311
APP code flash
0x00400000
848 KB
S32K341
APP code flash
0x00400000
1024KB
S32K312,
S32K342,
S32K322,
APP code flash
0x00400000
1872KB
S32K344,
S32K324,
S32K314
APP code flash
0x00400000
3920KB
S32K396,
S32K376
APP code flash
0x00400000
5968 KB
S32K356,
S32K336
APP code flash
0x00400000
6144 KB
S32K374,
S32K394
APP code flash
0x00400000
4096 KB
Table 134. Application NVM mapping (FULL_MEM)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
250 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 251

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Device
Flash area
Start address
Size
S32K388,
S32K358,
S32K348,
S32K338,
S32K328
APP code flash
0x00400000
8016 KB
S32K389
APP code flash
0x00400000
12096 KB
Table 134. Application NVM mapping (FULL_MEM)...continued
* The sizes mentioned are only valid for Standard Firmware.
Device
Flash area
Start address
Size
Common
APP data flash
0x10000000
128KB
APP code flash (active area)
0x00400000
256KB
S32K310
APP code flash (passive
area)
0x00480000
256KB
APP code flash (active area)
0x00400000
336KB
S32K311
APP code flash (passive
area)
0x00480000
336KB
APP code flash (active area)
0x00400000
512KB
S32K341
APP code flash (passive
area)
0x00500000
512KB
APP code flash (active area)
0x00400000
848KB
S32K312,
S32K342,
S32K322
APP code flash (passive
area)
0x00500000
848KB
APP code flash (active area)
0x00400000
1872KB
S32K344,
S32K324,
S32K314
APP code flash (passive
area)
0x00600000
1872KB
APP code flash
0x00400000
2048KB
APP code flash (active area)
0x00600000
1024KB
S32K374,
S32K394
APP code flash (passive
area)
0x00800000
1024KB
APP code flash (active area)
0x00400000
3072KB
S32K356,
S32K336
APP code flash (passive
area)
0x00800000
3072KB
APP code flash
0x00400000
2048KB
APP code flash (active area)
0x00600000
1872KB
S32K396,
S32K376
APP code flash (passive
area)
0x00800000
1872KB
APP code flash (active area)
0x00400000
3920KB
S32K388
S32K358,
S32K348,
S32K338,
APP code flash (passive
area)
0x00800000
3920KB
Table 135. Application NVM mapping (AB_SWAP)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
251 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 252

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Device
Flash area
Start address
Size
S32K328
APP code flash (active area)
0x00400000
5952KB
S32K389
APP code flash (passive
area)
0x00A00000
5952KB
Table 135. Application NVM mapping (AB_SWAP)...continued
* The sizes mentioned are only valid for Standard Firmware.
14.6.2  OTP Device configuration
This section explains various device configuration option available to user by directly programming certain
values to a fixed location in UTEST area.
Configuration Name
UTEST Location
Size (in bytes)
Description
HSE Firmware Usage
feature flag
0x1B000000
8 bytes
Programming this location enables the security in
the device. This flag must be programmed before
the HSE firmware installation can be performed.
This location can be programmed by any value
directly by application in CUST_DEL lifecycle only.
Secure-BAF can also program this field based on
the BCW. Refer BCW bit mapping for more details.
Reserved
0x1B000048
8 bytes
Used by HSE. Can be programmed by application.
FXOSC configuration
0x1B000050
8 bytes
Oscillator configuration values in case PLL enabled
by HSE firmware during secure boot. Refer to “Boot
Chapter” in S32K3xx Reference Manual for more
details.
Partial AB_Swap
0x1B000058
8 bytes
Only applicable for S32K358 family and S32K388
devices. Programming this location with a value “0x
DABADABADABADABA” configures the device for
partial AB_Swap mode when device is converted
to AB_Swap configuration. For more details refer to
HSE firmware Installation or HSE Firmware Update
section. Note that S32K3x6 devices are always
configured in Partial AB_Swap configuration instead
of Normal AB_Swap configuration.
JDC clock disable
0x1B000060
8 bytes
Programming this location disables the JDC clock.
This helps to save the power consumption of
the device. When this feature is enabled, debug
authorization is only performed on SDAP interface
not on JDC. This feature is supported only for S32
K3x1, S32K3x6, S32K358, S32K388 and S32K389
device families.
Table 136. UTEST Device configuration
14.6.3  XRDC Configuration
This section explains default configuration of XRDC. It also explains application specific configuration details
and restrictions. HSE protects access to its own resources. Hence, XRDC module is minimally configured
during initialization of HSE.
Important:
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
252 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 253

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Since the GVLD bit of XRDC is not configured by HSE, the Application must set this bit to enable the XRDC.
XRDC should be enabled only after the HSE_STATUS_INIT_OK bit is set by the HSE. This is to ensure that any
Flash program/erase operation done by the HSE is not interrupted.
For details on the XRDC controller, refer chapter “Extended Resource Domain Controller (XRDC)” from
S32K3xx Reference Manual.
14.6.3.1  Default MDAC configuration
The HSE applies default XRDC configuration on MDAC assigned to HSE core. HSE allocates itself the highest
domain number available S32K3 device variant.
The HSE uses domain ID as shown in below table. All domain ID’s are still available for application to configure.
For details on the XRDC registers (MDAC and domain ID), refer chapter “eXtended Resource Domain
Controller (XRDC)” from S32K3xx Reference Manual.
Device
MDAC Register
HSE Domain ID
S32K31x
MDAC3
1
S32K34x, S32K32x
MDAC3
2
S32K33x, S32K35x, S32K37x,
S32K39x
MDAC3
3
S32K388
MDAC3
4
Table 137. HSE Domain ID values
14.6.3.2  Default MRC 0 configuration (FULL_MEM)
The following table explains configuration of memory region descriptor 0 as done by the HSE.
MRC
Number
Region
Descriptor
Number
(K310,
K311,
K312)
Region
Descriptor
Number
(Other K3
devices)
Region
Name
Access rights
Configuration done by HSE
0
5
13
HSE data
flash
Data flash area
accessible by HSE only.
Please refer section On-
chip secure NVM for start
and end address range.
W0= Start address
W1= End Address
W2={
SE=0,SNUM=0,
HSE domain =0x7[All
 permission]
Other domains =0x00[No
 Permission]
}
W3={VLD=1, LK2=0x3}
0
6
14
HSE
UTEST
UTEST accessible by
HSE only.
Please refer section On-
chip secure NVM for start
and end address range.
W0= Start address
W1= End Address
W2={ 
SE=0,SNUM=0, 
HSE domain =0x7[All
 permission]
Other domains =0x00[No
 Permission]
} 
Table 138. Default programming of MRC register by HSE
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
253 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 254

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
MRC
Number
Region
Descriptor
Number
(K310,
K311,
K312)
Region
Descriptor
Number
(Other K3
devices)
Region
Name
Access rights
Configuration done by HSE
W3={VLD=1, LK2=0x3} 
0
7
15
HSE code
flash
Data flash area
accessible by HSE only.
Please refer section On-
chip secure NVM for start
and end address range.
W0= Start address 
W1= End address 
W2={ 
SE=0,SNUM=0, 
HSE domain =0x7[All
 permission]
Other domains =0x00[No
 Permission]
} 
W3={VLD=1, LK2=0x3}
Table 138. Default programming of MRC register by HSE...continued
For details on the XRDC registers (MRC, W0, W1, W2, SE, SNUM, W3, VLD, LK2), refer chapter “Extended
Resource Domain Controller (XRDC)” from S32K3xx Reference Manual.
14.6.3.3  Default MRC 0 configuration (AB_SWAP)
The following table explains the default configuration of Memory Region Descriptors of MRC 0.
MRC
Number
Region
Descriptor
Number
(K310,
K311,K312)
Region
Descriptor
Number
(other K3
devices)
Name
Remarks
Configuration done by Boot
Component
0
4
12
HSE FW
Active flash
area
Active Code area that is
accessible by the HSE
only. Please refer to
section On-chip secure
NVM for start and end
address range.
W0= Start address
W1= End Address
W2={
SE=0,SNUM=0,
HSE domain =0x7[All
 permission]
Other domains =0x00[No
 Permission]
}
W3={VLD=1, LK2=0x3}
{This size increases if size
 of HSE (Full) Firmware is
 increased}
              
0
5
13
HSE FW
data flash
area/
keystore
area
Data Flash area that is
accessible by the HSE
only. Please refer to
section On-chip secure
NVM for start and end
address range.
W0= Start address
W1= End Address
W2={
SE=0,SNUM=0,
HSE domain =0x7[All
 permission]
Other domains =0x00[No
 Permission]
}
W3={VLD=1, LK2=0x3}
Table 139. Default Configuration of MRC when HSE FW Usage Feature Flag is Enabled
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
254 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 255

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
MRC
Number
Region
Descriptor
Number
(K310,
K311,K312)
Region
Descriptor
Number
(other K3
devices)
Name
Remarks
Configuration done by Boot
Component
              
0
6
14
HSE
UTEST
area
UTEST area that is
accessible by the HSE
only. Please refer to
section On-chip secure
NVM for start and end
address range.
W0= Start address
W1= End Address
W2={
SE=0,SNUM=0,
HSE domain =0x7[All
 permission]
Other domains =0x00[No
 Permission]
}
W3={VLD=1, LK2=0x3}
              
0
7
15
HSE FW
Passive
flash area
Passive Code area that
is accessible by the HSE
only. Please refer to
section On-chip secure
NVM for start and end
address range.
W0= Start address
W1= End Address
W2={
SE=0,SNUM=0,
HSE domain =0x7[All
 permission]
Other domains =0x00[No
 Permission]
}
W3={VLD=1, LK2=0x3}
{This size increases if size
 of HSE (Full) Firmware is
 increased}
              
Table 139. Default Configuration of MRC when HSE FW Usage Feature Flag is Enabled...continued
For details on the XRDC registers (MRC, W0, W1, W2, SE, SNUM, W3, VLD, LK2), refer chapter “Extended
Resource Domain Controller (XRDC)” from S32K3xx Reference Manual.
14.6.3.4  Default configuration of PAC
HSE configures and lock the following peripherals for its exclusive use. Read and write access to these
peripherals are not provided to application domains. All other PDAC registers which are not shared by
Application and the HSE is in default state i.e. VLD and LK2 bit is 0 and can be configured by application. By
default, access is granted to all domains.
For details on the XRDC registers (PAC), refer chapter “Extended Resource Domain Controller (XRDC)” from
S32K3xx Reference Manual.
Peripheral Name
PDAC Number
Description
Flash controller alternate interface[1]
155
Alternate interface is exclusively reserved
for HSE
Flash memory alternate interface[1]
188
Alternate interface is exclusively reserved
for HSE
HSE_GPR[2]
231
Read/Write permission given to all core
Table 140. PDAC programing by HSE
[1]
For detail on Flash controller alternate interface, refer chapter “Flash Memory Controller (PFLASH)” from S32K3xx Reference Manual.
[2]
For detail on HSE_GPR refer chapter “Hardware Security Engine (HSE_B)” from S32K3xx Reference Manual.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
255 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 256

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
14.6.4  Status Bits for the HSE Firmware and Secure BAF
This section explains various status bits usage by the HSE Firmware and the Secure BAF.
14.6.4.1  Secure BAF version number
Secure BAF version is a 64bit field. Secure BAF version can be read by application from HSE_CONFIG_GPR3
register 0x4039C020.
Note:  These are indicative register structures/values, for details refer to the HSE Service API Reference
Manual.
The version information is explained in the table below.
Bit #
Field Name
Description
56 - 63
RC_NUMBER
Release Candidate Number.
48 - 55
INCREMENTAL_NUMBER
Incremented when new features are added but compatibility kept.
40 - 47
BASELINE_NUMBER
Incremented when the compatibility with the previous version is
broken.
32 - 39
RESERVED
Reserved
16 - 31
FW_TYPE
This field identify the FW type:
0 – Standard generic FW targeting all customers
1-7 – Reserved
8 >= Custom1, Custom2....(e.g. Custom1 = customer X’s project
A, Custom2 = customer Y’s project B)
8 – 15
SOC_TYPE_ID
This field Identifies the SoC family[1]
5 – S32K344, S32K324 and S32K314 devices
12 – S32K311 and S32K310 devices
13 – S32K312, S32K342, S32K322 and S32K341 devices
14 – S32K358, S32K348, S32K338, S32K328 S32K336 and
S32K356 devices
15 – S32K396, S32K376, S32K394 and S32K374 devices
16 – S32K388
17 – S32K389
0 – 7
RESERVED
Reserved
Table 141. Secure BAF version number HSE_CONFIG_GPR3 (0x4039C020)
[1]
User should refer to MIDR register to get the specific device name for a particular SOC family.
14.6.4.2  HSE_CONFIG_GPR3
Secure BAF updates status bits on HSE_CONFIG_GPR3 (0x4039C028) as explained in below table.
Bit #
Description
31-30
Reserved
29
1: Application read/execute is blocked from flash Block 4 as HSE FW is performing
flash write operation on this block.
0: Application can read/execute from flash block 4.
28
1: Application read/execute is blocked from flash Block 3 as HSE FW is performing
flash write operation on this block.
Table 142. Status Bits on HSE_CONFIG_GPR3 (0x4039C028)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
256 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 257

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Bit #
Description
0: Application can read/execute from flash block 3.
27
1: Application read/execute is blocked from flash Block 2 as HSE FW is performing
flash write operation on this block.
0: Application can read/execute from flash block 2.
26
1: Application read/execute is blocked from flash Block 1 as HSE FW is performing
flash write operation on this block.
0: Application can read/execute from flash block 1.
25
1: Application read/execute is blocked from flash Block 0 as HSE FW is performing
flash write operation on this block.
0: Application can read/execute from flash block 0.
24
1: Application read/execute is blocked from UTEST area as HSE FW is performing
flash write operation on this block.
0: Application can read/execute from flash block 4.
22-23
Reserved for future use
21
1: Application program and erase is blocked for Block 4 as HSE FW is reading or
executing on this block.
0: Block 4 is available for program and erase for application.
20
1: Application program and erase is blocked for Block 3 as HSE FW is reading or
executing on this block.
0: Block 3 is available for program and erase for application.
19
1: Application program and erase is blocked for Block 2 as HSE FW is reading or
executing on this block.
0: Block 2 is available for program and erase for application.
18
1: Application program and erase is blocked for Block 1 as HSE FW is reading or
executing on this block.
0: Block 1 is available for program and erase for application.
17
1: Application program and erase is blocked for Block 0 as HSE FW is reading or
executing on this block.
0: Block 0 is available for program and erase for application.
16
1: Application program and erase is blocked for UTEST block as HSE FW is reading or
executing on this block.
0: Block 4 is available for program and erase for application.
15-8
Reserved for future
7
1: SBAF verifies the IVT and secure recovery image with random IV.
0: SBAF verifies the IVT and secure recovery image with fixed IV.
6
Reserved for HSE
5
Application cores booted in Recovery mode by SBAF.
4
No HSE Firmware is present in Device due to Erase performed by SBAF Handshake
logic. This bit resets on presence of valid HSE Firmware.
3
HSE Firmware from Data flash area is erased by SBAF Handshake logic in current
reset cycle.
2
HSE Firmware from code flash area is erased by SBAF Handshake logic in current
reset cycle.
1
MU interface is enabled for installation of HSE Firmware.
Table 142. Status Bits on HSE_CONFIG_GPR3 (0x4039C028)...continued
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
257 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 258

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Bit #
Description
0
HSE FW is present and SBAF Booted HSE Firmware
Table 142. Status Bits on HSE_CONFIG_GPR3 (0x4039C028)...continued
14.6.4.3  HSE Secure Memory sizes in HSE GPR Registers
This section explains the size of all the secure memories reserved for HSE.
Register name
Register
Address
Secure
Memory
Value for
FULL_MEM
Size for FULL_
MEM
Value for AB_
SWAP
Size for AB_
SWAP
CONFIG_
RAMPR
0x4039C038
SRAM memory
0x40000000
0
0x40000000
0
CONFIG_
CFPRL
0x4039C03C
Code Flash
Memory Active
Block
0x40000000
0
0x4002C000
176 KB for HSE
Firmware
CONFIG_
CFPRH
0x4039C040
Code Flash
Memory
Passive Block
0x4002C000
128 KB for
HSE Firmware
and 48 KB for
Secure BAF
0x4002C000
176 KB for HSE
Firmware
CONFIG_DFPR 0x4039C044
Data Flash
Memory
0x4002A000
128 KB for
HSE Firmware
backup and 40
KB for SYS_
IMG
0x40020000
128 KB
reserved for
HSE
Table 143. HSE Secure Memory sizes in HSE GPR Registers
14.6.4.4  DCM register DCMRWP1
Application can configures various bits of this register DCMRWP1 (address 0x402AC400), to allow Secure BAF
recovery mode and HSE Firmware installation via MU interface. Below table explains this register.
Bit #
Num of bits
R/W access by Application
Description
24-31
8
R/W
Marker Value 0xA5 needs to be written by application core
to enable MU interface for installation of HSE Firmware. The
user must poll for enablement of bit 1 of HSE_CONFIG_
GPR3 (0x4039C028) before communication over MU
interface, see Status Bits on HSE_CONFIG_GPR3 (0x4039
C028).
23
1
R/W
Disable recovery mode on destructive reset.
This bit is reset by default and Secure BAF allows recovery
mode sequence if Application issues >8 destructive reset.
Application can set this bit to disable recovery mode when
Application issues > 8 destructive reset.[1]
22
1
R/W
Disable recovery mode on functional reset.
This bit is reset by default and Secure BAF allows recovery
mode sequence if Application issues >8 functional reset.
Application can set this bit to disable recovery mode when
Application issues > 8 functional reset. [1][2]
21
1
R
Reserved
Table 144. DCM register DCMRWP1 (address 0x402AC400)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
258 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 259

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Bit #
Num of bits
R/W access by Application
Description
16-20
5
R
Recovery mode reset counter.
LC CUST_DEL:
After more than 8 Functional or Destructive reset, the reset
recovery count directly set to 9.
LC OEM_PROD/IN-FIELD:
1. After more than 8 Functional or Destructive reset, the
reset recovery count directly set to 9.
2. After step 1, Secure BAF increments this counter when
Functional or destructive reset is issued.
3. Reset recovery counter run ahead (count + 1) of actual
reset count.
4. If host not attach core in JTAG Recovery mode, then
SBAF give functional reset after every ~30sec which will
increase Reset recovery counter
5. If reset recovery counter > 16 then SBAF will never
enable host core util a hard power given on board to
reset the Reset recovery counter value and start step
#1 again.
6. Functional and Destructive reset counter gets 0 when
15th destructive reset is issued.
15
1
R
Reserved
11-14
4
R
Destructive reset counter. Secure SBAF increments this
counter when destructive reset is set.
0-10
11
R
Reserved
Table 144. DCM register DCMRWP1 (address 0x402AC400)...continued
[1]Application core should not modify other bits of this register while updating these bits.
[2]Applications would be booted in Recovery mode sequence irrespective of the Bit#22 if the functional reset is
caused by application of the CR sanction HSE_CR_SANCTION_RESET_SOC during Advanced Secure Boot.
See section Disable Entry into Recovery Mode for more details.
14.6.4.5  DCM register DCMSTAT
The below table explains various status bits configuration of DCMSTAT (0x402AC000) by HSE.
Bit #
Field Name
Description
19-31
-
Refer S32K3xx Reference Manual.
18
DCMOTAA_EX (Valid for devices
configured in Partial AB_SWAP
Mode)
AB_SWAP (OTA) Active State (valid only if DCMDONE bit is set)
0b - Inactive
1b – Active
17
DCMOTAR
AB_SWAP (OTA) Active region (valid only if DCMDONE bit is set)
0b - Low address
1b - High address
16
DCMOTAA
AB_SWAP (OTA) Active State (valid only if DCMDONE bit is set)
0b - Inactive
1b – Active
10-15
-
Refer S32K3xx Reference Manual for more details.
Table 145. DCM register DCMSTAT (0x402AC000)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
259 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 260

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Bit #
Field Name
Description
9
DCMOTAS
DCM AB_SWAP (OTA) Scanning Status (valid only when the value
of the DCMDONE field is 1)
0b - Completed with errors
1b - Completed successfully
1-8
-
Refer S32K3xx Reference Manual for more details.
0
DCMDONE
DCM Scanning Status
Indicates whether the DCM scanning is in progress or complete.
0b - Running
1b - Completed
Table 145. DCM register DCMSTAT (0x402AC000)...continued
14.6.4.6  HSE Secure Memory sizes in HSE GPR Registers
This section explains the size of all the secure memories reserved for HSE.
Register name
Register
Address
Secure
Memory
Value for
FULL_MEM
Size for FULL_
MEM
Value for AB_
SWAP
Size for AB_
SWAP
CONFIG_
RAMPR
0x4039C038
SRAM memory
0x40000000
0
0x40000000
0
CONFIG_
CFPRL
0x4039C03C
Code Flash
Memory Active
Block
0x40000000
0
0x4002C000
176 KB for HSE
Firmware
CONFIG_
CFPRH
0x4039C040
Code Flash
Memory
Passive Block
0x4002C000
128 KB for
HSE Firmware
and 48 KB for
Secure BAF
0x4002C000
176 KB for HSE
Firmware
CONFIG_DFPR 0x4039C044
Data Flash
Memory
0x4002A000
128 KB for
HSE Firmware
backup and 40
KB for SYS_
IMG
0x40020000
128 KB
reserved for
HSE
Table 146. HSE Secure Memory sizes in HSE GPR Registers
14.6.5  Synchronizing flash read/write access between HSE and application core
Synchronization with the HSE must be managed by host core whenever they flash resources are shared
as mentioned in the figure. Following subsequent sections summarizes various scenarios in which these
synchronization issue can happen between application cores(s) and the HSE.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
260 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 261

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Figure 93. High level system configuration for flash access
The flash blocks used in the firmware are as follows:
UTEST and Block 0 are common for all the device variants of S32K3XX.
SOC
Active Block
(Default)
Passive Block (Default) /
Code Flash Block (FULL_MEM)
Data Flash Block
S32K311,
S32K310
BLOCK 0
BLOCK 1
BLOCK 2
S32K312,
S32K342,
S32K322,
S32K341
BLOCK 0
BLOCK 1
BLOCK 2
S32K344,
S32K324,
S32K314
BLOCK 1
BLOCK 3
BLOCK 4
S32K396,
S32K394,
S32K376,
S32K374
BLOCK 1
BLOCK 2
BLOCK 3
S32K388
S32K358,
S32K356,
S32K348,
S32K338,
S32K328
BLOCK 1
BLOCK 3
BLOCK 4
S32K389
BLOCK 1
BLOCK 3
BLOCK 4
Table 147. FLASH BLOCKS IN DIFFERENT SOC
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
261 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 262

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
To avoid synchronization issues, HSE Firmware sets the write block whenever it is executing or reading from a
block and sets the read block CONFIG_GPR3 at the address (0x4039C028). Details of the register is already
explained in previous section.
Note:  Data Flash is shown at different flash blocks for different devices. For 4MB/8MB devices the data flash is
denoted by Block 4. For 2MB/1MB devices the data flash is denoted by Block 2. For 6MB devices the data flash
is denoted by Block 3.
Application needs to read from CONFIG_GPR3 before read or write on flash so the synchronization issue can
be avoided between HSE and application core(s).
uint32_t *pGPR_Status = HSE_GPR_RW_STATUS_REG;
//Block 0 read check
if((((*pGPR_Status)>>16U) & (1U << 9U)) == (1U << 9U))
{
 //Application should not read/execute from flash Block 0
}else{
 //Application can read/execute from flash Block 0
}
//Block 0 write check
if((((*pGPR_Status)>>16U) & (1U << 1U)) == (1U << 1U))
{
 //Application program and erase is blocked for Block 0 as HSE FW is reading or executing on this
 block
}else{
 //Block 0 is available for program and erase for application
}
      
Important:  In AB_SWAP configuration, HSE_READ_WRITE_LOCK REGISTER work on physical flash Blocks
and not on swapped blocks. In case of higher block being active and firmware is executing from physical block
1 (for 2MB devices) and physical block 3 (for 4MB devices) although the addressing of flash still represents to
block 0 and block 1, respectively.
Sample code for S32K312 device to wait and check if HSE is executing from its active flash block which is block
0 by address but physical blocks depend on higher/lower flash active block:
volatile uint32_t *pFlashBlockRWStatus = (volatile uint32_t *)HSE_GPR_READ_WRITE_BLOCK_REGISTER;
if (DCM_BIT_HIGH_ADDRESS_OTA_ACTIVE == Dcm_ActiveAddressOTARegion())
{
    while((HSE_GPR_WRITE_BLK_BLK1 << 16U) == (*pFlashBlockRWStatus & (HSE_GPR_WRITE_BLK_BLK1 <<
 16U)));
}
else
{
    while((HSE_GPR_WRITE_BLK_BLK0 << 16U) == (*pFlashBlockRWStatus & (HSE_GPR_WRITE_BLK_BLK0 <<
 16U)));
} 
Similar concept is applicable for all devices of S32K3 family.
Operation done by
M7_0/1
Operation done by HSE
M7_0/1 issues if steps
not followed
Steps to be done by application
Programs data
flash
Programs data flash
No issues
No synchronization steps to be followed.
It is expected that M7_0/1 core does
not issue any command to HSE which
involves program/erase operation when it is
programming data flash.
Table 148. Potential synchronization issues between core_0/1 and HSE while accessing data flash
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
262 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 263

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Operation done by
M7_0/1
Operation done by HSE
M7_0/1 issues if steps
not followed
Steps to be done by application
Reads data flash
Programs data flash
M7_0/1 read operation
may terminate with
exception.
The scenario can occur in a specific
command like import keys, programming
of monotonic counter and erase of keys.
It is expected that application core reads
the read block bits for data flash in the
CONFIG_GPR3 and wait for these bits to
be cleared before accessing the data flash
block.
Programs data
flash
Read data flash
M7_0/1 starting program/
erase may terminate with
error.
It is expected that application core reads
the write block bits for data flash in the
CONFIG_GPR3 and wait for these bits
to be cleared before trying to program or
erase the data flash block.
Table 148. Potential synchronization issues between core_0/1 and HSE while accessing data flash...continued
Operation done
by M7_0/1
Operation done by
HSE
M7_0/1 issues if steps
not followed
Steps to be done by application
Programs code
flash block
Programs code flash
block.
No issues
No synchronization steps to be followed. It is
expected that M7_0/1 core does not issue any
command to HSE which involves program/erase
operation when it is programming code flash block.
Programs code
flash block.
Execute from code
flash block.
M7_0/1 program
operation may terminate
with programming error
It is expected that application core reads the write
block bits for data flash in the CONFIG_GPR3 and
wait for these bits to be cleared before trying to
program or erase the code flash block.
Table 149. Potential synchronization issues between core_0/1 and HSE while accessing code flash block
Operation done
by M7_0/1
Operation done
by HSE
M7_0/1 issues if
steps not followed
Steps to be done by application
Programs UTEST
Programs UTEST
No issues
No synchronization steps to be followed. It is expected that
M7_0/1 core does not issue any command to HSE which
involves program/erase operation when it is programming
UTEST.
Execute from
flash block #0
UTEST program
M7_0/1 execution
may terminate with
exception.
This scenario occurs in a specific command which
mandates HSE to program UTEST. It is expected that
application core reads the read block bits for UTEST and
block 0 in the CONFIG_GPR3 and wait for these bits to be
cleared before accessing the UTEST flash block or Block
0.
This command must be called from SRAM. Different cores
within a multicore architecture must not execute from block
#0 during command execution.
Program UTEST
Read UTEST
M7_0/1 programing
flash block #0 may
terminate with an
error.
It is expected that application core reads the write block
bits for UTEST and block 0 flash in the CONFIG_GPR3
and wait for these bits to be cleared before trying to
program or erase the block 0 / before trying to program
UTEST block.
Table 150. Potential synchronization issues between core_0/1 and HSE while accessing UTEST
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
263 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 264

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
14.6.5.1  Usage of Internal Flash by HSE FW services
Following tables provide details of internal flash access made on various blocks for every service provided by
HSE FW.
14.6.5.1.1  Flash access in FULL_MEM devices
Service Class
HSE Service ID
Data Flash
Code Flash
UTEST area/
Block 0
NOTES
Administrative
HSE_SRV_ID_
SET_ATTR
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – Yes
Write- Yes
HSE_SRV_ID_
GET_ATTR
Read – Yes
Write- No
Read – Yes
Write- No
Read – Yes
Write- No
HSE_SRV_ID_
CANCEL
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
FIRMWARE_
UPDATE
Read – Yes
Write- Yes
Read – Yes
Write- Yes
Read – Yes
Write- No
HSE_SRV_ID_
SBAF_UPDATE
Read – Yes
Write- No
Read – Yes
Write- Yes
Read – Yes
Write- No
HSE_SRV_ID_
SYS_AUTH_REQ
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
SYS_AUTH_RESP
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
BOOT_DATA_
IMAGE_SIGN
Read – No
Write- No
Read – Yes
Write- No
Read – Yes
Write- No
HSE_SRV_ID_
BOOT_DATA_
IMAGE_VERIFY
Read – No
Write- No
Read – Yes
Write- No
Read – Yes
Write- No
HSE_SRV_
ID_IMPORT_
EXPORT_
STREAM_CTX
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
ERASE_HSE_
NVM_DATA
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
ERASE_FW
Read – No
Write- Yes
Read – Yes
Write- Yes
Read – No
Write- No
HSE_SRV_ID_
FW_INTEGRITY_
CHECK
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – Yes
Write- No
HSE_SRV_ID_
PUBLISH_NVM_
KEYSTORE_
RAM_TO_FLASH
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
Table 151. Flash Access by HSE FW Services in FULL_MEM Devices
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
264 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 265

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Service Class
HSE Service ID
Data Flash
Code Flash
UTEST area/
Block 0
NOTES
Key
Management
HSE_SRV_ID_
LOAD_ECC_
CURVE
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
FORMAT_KEY_
CATALOGS
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
ERASE_KEY
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
GET_KEY_INFO
Read – Yes
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
IMPORT_KEY
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
EXPORT_KEY
Read – Yes
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
KEY_GENERATE
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
DH_COMPUTE_
SHARED_
SECRET
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
KEY_DERIVE
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
KEY_DERIVE_
COPY
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
KEY_VERIFY
Read – Yes
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
SHE_LOAD_KEY
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – Yes
Write- No
If the Auth ID is
Secret Key, then
UTEST Access is
performed
HSE_SRV_ID_
SHE_LOAD_
PLAIN_KEY
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
SHE_EXPORT_
RAM_KEY
Read – No
Write- No
Read – Yes
Write- No
Read – Yes
Write- No
UTEST is
accessed to read
UID and SECRET
Key
HSE_SRV_ID_
SHE_GET_ID
Read – No
Write- No
Read – Yes
Write- No
Read – Yes
Write- No
The UID is read
from UTEST
HSE_SRV_ID_
SHE_BOOT_OK
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
SHE_BOOT_
FAILURE
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
Table 151. Flash Access by HSE FW Services in FULL_MEM Devices...continued
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
265 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 266

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Service Class
HSE Service ID
Data Flash
Code Flash
UTEST area/
Block 0
NOTES
Cryptographic
HSE_SRV_ID_
HASH
Read – See NOTE
Write- No
Read – Yes
Write- No
Read – See NOTE
Write- No
HSE_SRV_ID_
MAC
Read – See NOTE
Write- No
Read – Yes
Write- No
Read – See NOTE
Write- No
HSE_SRV_ID_
FAST_CMAC
Read – See NOTE
Write- No
Read – Yes
Write- No
Read – See NOTE
Write- No
HSE_SRV_ID_
SYM_CIPHER
Read – See NOTE
Write- No
Read – Yes
Write- No
Read – See NOTE
Write- No
HSE_SRV_ID_
AEAD
Read – See NOTE
Write- No
Read – Yes
Write- No
Read – See NOTE
Write- No
HSE_SRV_ID_
SIGN
Read – See NOTE
Write- No
Read – Yes
Write- No
Read – See NOTE
Write- No
HSE_SRV_ID_
RSA_CIPHER
Read – See NOTE
Write- No
Read – Yes
Write- No
Read – See NOTE
Write- No
If the provided
Input Address in
any of the Crypto
Service lies in
Data Flash or
UTEST, then the
corresponding
Read Access is
performed.
RNG
HSE_SRV_ID_
GET_RANDOM_
NUM
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
Counters
HSE_SRV_ID_
INCREMENT_
COUNTER
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
READ_COUNTER
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_
ID_CONFIG_
COUNTER
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
Advance Secure
Booting
(SMR/CR)
HSE_SRV_ID_
SMR_ENTRY_
INSTALL
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
SMR_VERIFY
Read – Yes
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
CORE_RESET_
ENTRY_INSTALL
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
ON_DEMAND_
CORE_RESET
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
SMR_ENTRY_
ERASE
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
CORE_RESET_
ENTRY_ERASE
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
Table 151. Flash Access by HSE FW Services in FULL_MEM Devices...continued
[*] Code Flash Block refers to the Block in which HSE Firmware is present.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
266 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 267

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
[*] If an input address of a Flash Block is provided to HSE Firmware, then it will perform a Read operation in that
Block.
14.6.5.1.2  Flash access in AB_SWAP devices
Service Class
HSE Service ID
Data Flash
Code Flash
UTEST area/
Block 0
NOTES
Administrative
HSE_SRV_ID_
SET_ATTR
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – Yes
Write- Yes
HSE_SRV_ID_
GET_ATTR
Read – Yes
Write- No
Read – Yes
Write- No
Read – Yes
Write- No
HSE_SRV_ID_
CANCEL
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
FIRMWARE_
UPDATE
Read – No
Write- No
Read – Yes
Write- Yes
Read – Yes
Write- No
HSE_SRV_ID_
SBAF_UPDATE
Read – Yes
Write- No
Read – Yes
Write- Yes
Read – Yes
Write- No
HSE_SRV_ID_
SYS_AUTH_REQ
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
SYS_AUTH_RESP
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
BOOT_DATA_
IMAGE_SIGN
Read – No
Write- No
Read – Yes
Write- No
Read – Yes
Write- No
HSE_SRV_ID_
BOOT_DATA_
IMAGE_VERIFY
Read – No
Write- No
Read – Yes
Write- No
Read – Yes
Write- No
HSE_SRV_
ID_IMPORT_
EXPORT_
STREAM_CTX
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
ERASE_HSE_
NVM_DATA
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
ERASE_FW
Read – No
Write- Yes
Read – Yes
Write- Yes
Read – No
Write- No
HSE_SRV_ID_
FW_INTEGRITY_
CHECK
Read – No
Write- No
Read – Yes
Write- Yes (In
Passive)
Read – Yes
Write- No
HSE_SRV_ID_
ACTIVATE_
PASSIVE_BLOCK
Read – Yes
Write- No
Read – Yes
Write- Yes ( In
passive code flash
area)
Read – Yes
Write- No
HSE_SRV_ID_
PUBLISH_NVM_
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
Table 152. Flash Access by HSE FW Services in AB_SWAP Devices
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
267 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 268

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Service Class
HSE Service ID
Data Flash
Code Flash
UTEST area/
Block 0
NOTES
KEYSTORE_
RAM_TO_FLASH
Key
Management
HSE_SRV_ID_
LOAD_ECC_
CURVE
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
FORMAT_KEY_
CATALOGS
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
ERASE_KEY
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
GET_KEY_INFO
Read – Yes
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
IMPORT_KEY
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
EXPORT_KEY
Read – Yes
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
KEY_GENERATE
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
DH_COMPUTE_
SHARED_
SECRET
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
KEY_DERIVE
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
KEY_DERIVE_
COPY
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
KEY_VERIFY
Read – Yes
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
SHE_LOAD_
PLAIN_KEY
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
SHE_EXPORT_
RAM_KEY
Read – No
Write- No
Read – Yes
Write- No
Read – Yes
Write- No
UTEST is
accessed to read
UID and SECRET
Key
HSE_SRV_ID_
SHE_GET_ID
Read – No
Write- No
Read – Yes
Write- No
Read – Yes
Write- No
The UID is read
from UTEST
HSE_SRV_ID_
SHE_LOAD_KEY
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – Yes
Write- No
If the Auth ID is
Secret Key, then
UTEST Access is
performed
HSE_SRV_ID_
SHE_BOOT_OK
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
Table 152. Flash Access by HSE FW Services in AB_SWAP Devices...continued
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
268 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 269

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Service Class
HSE Service ID
Data Flash
Code Flash
UTEST area/
Block 0
NOTES
HSE_SRV_ID_
SHE_BOOT_
FAILURE
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
Cryptographic
HSE_SRV_ID_
HASH
Read – See NOTE
Write- No
Read – Yes
Write- No
Read – See NOTE
Write- No
HSE_SRV_ID_
MAC
Read – See NOTE
Write- No
Read – Yes
Write- No
Read – See NOTE
Write- No
HSE_SRV_ID_
FAST_CMAC
Read – See NOTE
Write- No
Read – Yes
Write- No
Read – See NOTE
Write- No
HSE_SRV_ID_
SYM_CIPHER
Read – See NOTE
Write- No
Read – Yes
Write- No
Read – See NOTE
Write- No
HSE_SRV_ID_
AEAD
Read – See NOTE
Write- No
Read – Yes
Write- No
Read – See NOTE
Write- No
HSE_SRV_ID_
SIGN
Read – See NOTE
Write- No
Read – Yes
Write- No
Read – See NOTE
Write- No
HSE_SRV_ID_
RSA_CIPHER
Read – See NOTE
Write- No
Read – Yes
Write- No
Read – See NOTE
Write- No
If the provided
Input Address in
any of the Crypto
Service lies in
Data Flash or
UTEST, then the
corresponding
Read Access is
performed.
RNG
HSE_SRV_ID_
GET_RANDOM_
NUM
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
Counters
HSE_SRV_ID_
INCREMENT_
COUNTER
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
READ_COUNTER
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_
ID_CONFIG_
COUNTER
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
Advance Secure
Booting
(SMR/CR)
HSE_SRV_ID_
SMR_ENTRY_
INSTALL
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
SMR_VERIFY
Read – Yes
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
CORE_RESET_
ENTRY_INSTALL
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
ON_DEMAND_
CORE_RESET
Read – No
Write- No
Read – Yes
Write- No
Read – No
Write- No
HSE_SRV_ID_
SMR_ENTRY_
ERASE
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
Table 152. Flash Access by HSE FW Services in AB_SWAP Devices...continued
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
269 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 270

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Service Class
HSE Service ID
Data Flash
Code Flash
UTEST area/
Block 0
NOTES
HSE_SRV_ID_
CORE_RESET_
ENTRY_ERASE
Read – Yes
Write- Yes
Read – Yes
Write- No
Read – No
Write- No
Table 152. Flash Access by HSE FW Services in AB_SWAP Devices...continued
[*] Code flash block refers to the active code flash block unless stated otherwise.
[*] If an input address of a Flash Block is provided to HSE Firmware, then it will perform a Read operation in that
Block.
14.6.6  HSE interface
The following table provides the number of MU instances and the number of TX/RX registers per instance.
Number of MU instances
Number of transmit / receive
registers per MU instance
Total number of transmit / receive
registers
2
4
8
Table 153. Number of MU instances and TRi / RRi registers
The number of MU instances can be referred to in the host source code via the symbol
HSE_NUM_OF_MU_INSTANCES.
14.6.7  HSE Firmware Handshake
Secure BAF and HSE Firmware have interdependent handshake mechanism that prevents bricking of device
by erasing the erroneous or corrupted HSE Firmware and reinstall new HSE Firmware. The Handshake
mechanism is only functional over functional resets.
HSE Firmware sets the status as successful after the device is successfully booted. If there are some major
corruptions in the device, during its initialization flow, the device goes into shutdown mode.
In case, the user does not see the HSE_STATUS_INIT_OK set, they are requested to assert a functional reset.
If the device fails to boot after repeated resets, the HSE Firmware is erased from the code flash location.
The status of firmware erase is set in HSE GPR (Register 3 (0x4039C028), refer chapter Hardware Security
Engine (HSE_B) from S32K3xx Reference Manual).
If valid backup firmware is present, it restores the firmware to code flash and retries booting the firmware. If the
data flash firmware also has major defect/corruptions, which leads to the HSE Firmware going into shutdown,
the user is requested to assert functional resets which is the similar process as of code flash.
The process is repeated for data flash firmware and in case the boot process fails, the HSE Firmware is erased
from the code flash and data flash.
In the case valid image is not present in backup or restoration was not successful, bit number 4 gets set in
HSE_CONFIG_GPR3 (0x4039C028).
The status of firmware erase is set in HSE_CONFIG_GPR3 (0x4039C028), refer to the Hardware Security
Engine (HSE_B) from S32K3xx Reference Manual). If no HSE Firmware is present in the device, the user must
install the firmware as mentioned in the HSE Firmware Installation chapter.
14.6.8  Integrity checks in SYS-Image locations
HSE Firmware verifies the data integrity check of SYS-IMAGE during the boot phase before loading content into
system RAM.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
270 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 271

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
14.6.9  Valid output address range (any memory configuration)
The tables below shows the valid output address range for HSE services for different SoCs.
Note:  At the time of using an address in ITCM and DTCM (tightly coupled memories) as an input or output
address for any service, the host application must ensure that the address passed lies in the address ranges
given in the below tables for all SoC variants. The user must add a fixed offset to the address. Refer to the
S32K3xx Reference Manual for the exact offset values for each memory.
For example, the ITCM0 address 0x00000400 is not accessible by the HSE. Instead, the same address is
accessible at location 0x11000400.
Memory region Name
Single Core (Size) (S32K311)
Single Core (Size) (S32K310)
SRAM
0x20400000 - 20407FFF
(32KB)
0x20400000 - 0x20403FFF
(16KB)
ITCM_0 Alternate Address
0x11000000 - 0x11007FFF
(32 KB)
0x11000000 - 0x11007FFF
(32 KB)
ITCM_1 Alternate Address
NA
N/A
DTCM_0 Alternate Address
0x21000000 - 0x2100FFFF
(64 KB)
0x21000000 - 0x2100FFFF
(64 KB)
DTCM_1 Alternate Address
NA
NA
Table 154. Valid output address range for S32K3x1
* ITCM and DTCM address range is accessible only when their corresponding core is enabled.
* ITCM and DTCM are accessed when core is disabled
Memory region Name
Single Core (Size) (S32
K312)
Multi Core Lock Step
Disable (Size) (S32K322)
Multi Core Lock Step Enable
(Size) (S32K342, S32K341)
SRAM
0x20400000 - 0x20417FFF
(96 KB)
0x20400000 - 0x2040FFFF
(64 KB)
ITCM_0 Alternate Address
0x11000000 - 0x11007FFF
(32 KB)
0x11000000 - 0x1100FFFF
(64 KB)
ITCM_1 Alternate Address
NA
0x11400000 - 0x11407FFF
(32 KB)
NA
DTCM_0 Alternate Address
0x21000000 - 0x2100FFFF
(64 KB)
0x21000000 - 0x2101FFFF
(128 KB)
DTCM_1 Alternate Address
NA
0x21400000 - 0x2140FFFF
(64 KB)
NA
Table 155. Valid output address range for S32K3x2
Memory region Name
Multi Core Lock Step Disable (Size)
Multi Core Lock Step Enable (Size)
SRAM
0x20400000 - 0x2044FFFF
(320 KB)
ITCM_0 Alternate Address
0x11000000 - 0x11007FFF
(32 KB)
0x11000000 - 0x1100FFFF
(64 KB)
Table 156. Valid output address range for S32K3x4
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
271 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 272

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Memory region Name
Multi Core Lock Step Disable (Size)
Multi Core Lock Step Enable (Size)
ITCM_1 Alternate Address
0x11400000 - 0x11407FFF
(32 KB)
NA
DTCM_0 Alternate Address
0x21000000 - 0x2100FFFF
(64 KB)
0x21000000 - 0x2101FFFF
(128 KB)
DTCM_1 Alternate Address
0x21400000 - 0x2140FFFF
(64 KB)
NA
Table 156. Valid output address range for S32K3x4...continued
Memory region Name
Multi Core
Lock Step Enable (Size)
Multi Core
Lock Step Disable (Size)
SRAM
0x20400000 - 0x2047FFFF
(512 KB)
ITCM_0 Alternate Address
0x11000000 - 0x1100FFFF
(64 KB)
0x11000000 - 0x11007FFF
(32 KB)
ITCM_1 Alternate Address
0x11400000 - 0x11407FFF
(32 KB)
ITCM_2 Alternate Address
0x11800000 – 0x11807FFF
(32 KB)
DTCM_0 Alternate Address
0x21000000 - 0x2101FFFF
(128 KB)
0x21000000 - 0x2100FFFF
(64 KB)
DTCM_1 Alternate Address
0x21400000 - 0x2140FFFF
(64 KB)
DTCM_2 Alternate Address
0x21800000 - 0x2180FFFF
(64 KB)
Table 157. Valid output address range for S32K3x6
Memory region Name
Multi Core
Lock Step
Disable (Size)
(S32K328)
Multi Core
Lock Step Disable
(Size) (S32K338)
Multi Core
Lock Step Enable
(Size) (S32K348)
Multi Core Lock Step
Enable (Size) (S32
K358, S32K356)
SRAM
0x20400000 - 0x204BFFFF
(768 KB)
ITCM_0 Alternate Address
0x11000000 - 0x11007FFF
(32 KB)
0x11000000 - 0x1100FFFF
(64 KB)
ITCM_1 Alternate Address
0x11400000 - 0x11407FFF
(32 KB)
NA
ITCM_2 Alternate Address
0x11800000 - 0x1180FFFF
(64 KB)
DTCM_0 Alternate Address
0x21000000 - 0x2100FFFF
(64 KB)
0x21000000 - 0x2101FFFF
(128 KB)
DTCM_1 Alternate Address
0x21400000 - 0x2140FFFF
(64 KB)
NA
DTCM_2 Alternate Address
0x21800000 - 0x2181FFFF
Table 158. Valid output address range for S32K358 series
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
272 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 273

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Memory region Name
Multi Core
Lock Step
Disable (Size)
(S32K328)
Multi Core
Lock Step Disable
(Size) (S32K338)
Multi Core
Lock Step Enable
(Size) (S32K348)
Multi Core Lock Step
Enable (Size) (S32
K358, S32K356)
(128 KB)
Table 158. Valid output address range for S32K358 series...continued
Memory region Name
Multi Core
Lock Step Enable (Size)
Multi Core
Lock Step Disable (Size)
SRAM
0x20400000 - 0x204BFFFF
(768 KB)
ITCM_0 Alternate Address
0x11000000 - 0x1100FFFF
(64 KB)
0x11000000 - 0x11007FFF
(32 KB)
ITCM_1 Alternate Address
NA
0x11400000 - 0x11407FFF
(32 KB)
ITCM_2 Alternate Address
0x11800000 – 0x11807FFF
(32 KB)
ITCM_3 Alternate Address
0x11C00000 – 0x11C07FFF
(32 KB)
DTCM_0 Alternate Address
0x21000000 - 0x2101FFFF
(128 KB)
0x21000000 - 0x2100FFFF
(64 KB)
DTCM_1 Alternate Address
NA
0x21400000 - 0x2140FFFF
(64 KB)
DTCM_2 Alternate Address
0x21800000 - 0x2180FFFF
(64 KB)
DTCM_3 Alternate Address
0x21C00000 - 0x21C0FFFF
(64 KB)
Table 159. Valid output address range for S32K388
Memory region Name
Multi Core
Lock Step Enable (Size)
Multi Core
Lock Step Disable (Size)
SRAM
0x20400000 - 00FF_FFFF
(1920 KB)
ITCM_0 Alternate Address
0x11000000 - 0x1100FFFF
(64 KB)
0x11000000 - 0x11007FFF
(32 KB)
ITCM_1 Alternate Address
NA
0x11400000 - 0x11407FFF
(32 KB)
ITCM_2 Alternate Address
0x11800000 – 0x11807FFF
(32 KB)
ITCM_3 Alternate Address
0x11C00000 – 0x11C07FFF
(32 KB)
DTCM_0 Alternate Address
0x21000000 - 0x2101FFFF
(128 KB)
0x21000000 - 0x2100FFFF
(64 KB)
DTCM_1 Alternate Address
NA
0x21400000 - 0x2140FFFF
Table 160. Valid output address range for S32K389
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
273 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 274

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Memory region Name
Multi Core
Lock Step Enable (Size)
Multi Core
Lock Step Disable (Size)
(64 KB)
DTCM_2 Alternate Address
0x21800000 - 0x2180FFFF
(64 KB)
DTCM_3 Alternate Address
0x21C00000 - 0x21C0FFFF
(64 KB)
Table 160. Valid output address range for S32K389...continued
14.6.10  Super User execution rights
The host needs Super User rights to be able to execute certain services. It can request to be temporarily
granted with Super User rights based on the knowledge of a secret or private key (refer to section Request for
Super User Rights). The table below lists the services that need Super User rights for execution.
Additional details can be found in each service chapter and section User vs Super User Rights.
Restricted services
Authorization
Description
HSE_SRV_ID_IMPORT_KEY
KEY_MGMT
Import a plain NVM key in an empty slot
without authentication.
Import a RAM provision key without
authentication.
Refer to section Key Import and Key
Import/Update.
HSE_SRV_ID_KEY_GENERATE
KEY_MGMT
NVM key generation in an empty key
slot.
HSE_SRV_ID_ERASE_KEY
KEY_MGMT
NVM key erase or NVM SHE key erase
(erasing key groups)
Refer to section Key Erase.
HSE_SRV_ID_KEY_DERIVE_COPY
Copy part of a RAM key to an empty
NVM key slot (refer to hseKeyDerive
CopyKeySrv_t).
HSE_SRV_ID_FORMAT_KEY_
CATALOGS
KEY_MGMT
Re-format the key catalog.
Refer to section Key Catalog
Formatting.
HSE_SRV_ID_CONFIG_KHTT (only for
S32K388)
KEY_MGMT
Configure the Key Handle Translation
Table (KHTT).
HSE_SRV_ID_LOAD_ECC_CURVE
HSE_CONFIG
Load an user defined ECC curve (refer
to hseLoadEccCurveSrv_t).
HSE_SRV_ID_SET_ATTR
HSE_CONFIG
Set/update the OTP-ATTR or NVM-
RW-ATTR attributes; exception: HSE_
SECURE_LIFE CYCLE_ATTR_ID
attribute.
Refer to section HSE System Attributes.
HSE_SRV_ID_BOOT_DATA_IMAGE_
SIGN
HSE_CONFIG
Authenticate the host system images
(IVT and AppBL). Refer to section
Authenticate Host System Images.
Table 161. Services that need Super User rights for execution
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
274 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 275

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Restricted services
Authorization
Description
HSE_SRV_ID_SMR_ENTRY_INSTALL
HSE_CONFIG
Complete SMR entry update (including
authScheme, configFlags, checkPeriod,
pSmrDest, smrDecrypt, versionOffset)
Refer to section System Tables.
HSE_SRV_ID_CORE_RESET_
ENTRY_INSTALL
HSE_CONFIG
Update a Core Reset entry.
Refer to section Core Reset Table
Installation>.
HSE_SRV_ID_CONFIG_COUNTER
HSE_CONFIG
Monotonic counter configuration.
HSE_SRV_ID_SMR_ENTRY_ERASE
HSE_CONFIG
SMR entry erase.
Refer to section SMR Entry Erase.
HSE_SRV_ID_CORE_RESET_
ENTRY_ERASE
HSE_CONFIG
Core Reset entry erase.
Refer to section Core Reset Table
Update.
HSE_SRV_ID_ON_DEMAND_CORE_
RESET
HSE_CONFIG
On-demand boot using a Core Reset
entry. Refer to section On-demand
Secure Boot.
HSE_SRV_ID_ACTIVATE_
PASSIVE_BLOCK (only in AB_Swap
configuration)
HSE_CONFIG
Activate the Passive Block in an AB_
SWAP Device.
Table 161. Services that need Super User rights for execution...continued
14.6.11  The mapping between SHE commands and HSE services
The table below shows the mapping between SHE commands (as defined by SHE specification) and HSE
services. For more details, refers to HSE Service API Reference Manual.
SHE command
HSE service
CMD_ENC_ECB
CMD_ENC_CBC
CMD_DEC_ECB
CMD_DEC_CBC
HSE_SRV_ID_SYM_CIPHER
CMD_GENERATE_MAC
CMD_VERIFY_MAC
HSE_SRV_ID_FAST_CMAC
CMD_LOAD_KEY
HSE_SRV_ID_SHE_LOAD_KEY
CMD_LOAD_PLAIN_KEY
HSE_SRV_ID_SHE_LOAD_PLAIN_KEY
CMD_EXPORT_RAM_KEY
HSE_SRV_ID_SHE_EXPORT_RAM_KEY
CMD_INIT_RNG
NA (RNG is initialized by HSE)
CMD_EXTEND_SEED
NA (RNG is initialized by HSE)
CMD_RND
HSE_SRV_ID_GET_RANDOM_NUM
CMD_SECURE_BOOT
Using the pre-boot SMR#0 with the BOOT_MAC_KEY key
(refer to section SHE-based secure boot (SMR #0)). SMR#0
is automatically verified at boot.
CMD_BOOT_FAILURE
HSE_SRV_ID_SHE_BOOT_FAILURE
CMD_BOOT_OK
HSE_SRV_ID_SHE_BOOT_OK
Table 162. SHE commands vs HSE services
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
275 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 276

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
SHE command
HSE service
CMD_GET_STATUS
The first 8 bit of MU FSR register ((uint8_t)(FSR_value)))
CMD_GET_ID
HSE_SRV_ID_SHE_GET_ID
CMD_CANCEL
HSE_SRV_ID_CANCEL
CMD_DEBUG
The CMD_DEBUG is not supported.
To erase the SHE keys, the
HSE_SRV_ID_SYS_AUTH_REQ / HSE_SRV_ID_SYS_
AUTH_RESP services with SHE MASTER_ECU_KEY key
can be used to gain Super User rights (refer to section
Execution Rights: Super user vs User), followed by HSE_
SRV_ID_ERASE_KEY service to erase the SHE key groups.
Table 162. SHE commands vs HSE services...continued
14.6.12  Delay in processing of first heavy operation after boot
In HSE_B, some heavy operations involve a delay of around 40ms when provided as the first heavy operation
after the device boots. This is because of initialization of the HSE RNG. Hence, once the RNG is initialized
during the first heavy operation, any subsequent heavy operation will take normal time. For example, if the
service HSE_SRV_ID_GET_RANDOM_NUM is executed, with this delay, then any subsequent service
execution of this service or any other relevant service won’t involve this delay. Application can request a random
number immediately after HSE_STATUS_INIT_OK flag is set.
The services which involve such delay are listed in the below table.
HSE Service ID
HSE_SRV_ID_SYS_AUTH_REQ
HSE_SRV_ID_KEY_GENERATE
HSE_SRV_ID_GET_RANDOM_NUM
Table 163. List of services involving delay when given for the first time after boot
14.6.13  HSE Firmware Features disabled in newer versions
The following table lists the HSE Firmware features that have been disabled in the 0.2.40.0 HSE Firmware.
HSE SPT Macro disabled
HSE Service ID/Attribute ID
HSE_SPT_BURMESTER_DESMEDT
HSE_SRV_ID_BURMESTER_DESMEDT
HSE_SPT_CMAC_WITH_COUNTER
HSE_SRV_ID_CMAC_WITH_COUNTER
HSE_SPT_CLASSIC_DH
NA
Table 164. HSE Firmware features disabled in 0.2.40.0
14.6.14  Debug and UID
ADKP can be provisioned using UID as a diversification parameter (see section Provisioning of ADKP). In this
case, the host debug can only be opened based on the knowledge of both ADKP and UID. Hence, the UID must
be retrieved by the debugger in order to calculate the expected response to the challenge.
UID is provided via a dedicated register (UID0 and UID1 in SD_DAP and JTAG SOC DATA[319:256] in JTAG
controller registers) in the Debugger interface refer S32K3xx Reference Manual It can also be retrieved by the
host via the SU right request service (see section Request for Super User Rights).
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
276 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 277

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
14.6.15  Reset
The security watchdog (SWT0) is started by the HSE with the default timeout configuration. See S32K3xx
Reference Manual for more information.
The below table lists the subsystems and their respective core identifiers (coreId) in S32K3xx devices. These
core identifiers must be used in the CR table entries defined by the host (see chapter Secure Boot and Memory
Verification Services).
Core Identifier
S32K3xx
0
M7_0
1
M7_1 [1][2][3]
2
M7_2[2][3]
3
M7_3[3]
Table 165. Subsystem vs. core identifiers (coreId)
[1]
Applicable for devices which support 2 Application cores.
[2]
Applicable for devices which support 3 Application cores.
[3]
Applicable for devices which support 4 Application cores.
14.7  HSE Firmware and Secure BAF release version compatibility
This section explains the details of various Secure BAF and HSE Firmware releases and their compatibility with
each other for various S32K3 devices.
Current SBAF Version Number
Current HSE Firmware version
numbers
Remarks
00 0C 00 00 00 0F 00 06
00 0C 00 00 02 28 00 00
Fully Compatible. All functionalities of HSE Firmware are
supported.
Table 166. SBAF and HSE Firmware version compatibility for S32K310 and S32K311 devices
Current SBAF Version Number
Current HSE Firmware version
numbers
Remarks
00 05 00 00 00 08 00 03
Fully Compatible. All functionalities of HSE Firmware are
supported.
00 05 00 00 00 0A 00 00
00 05 00 00 00 0C 00 00
00 05 00 00 01 01 00 00
All functionality supported except HSE firmware update service
“HSE_SRV_ID_FIRMWARE_UPDATE” is not supported.
Sequence of steps to be followed to update to the latest
version of SBAF and HSE FW:
1. Update Secure BAF to version “00 05 00 00 00 09 04 00”
with the help of HSE FW service “HSE_SRV_ID_SBAF_
UPDATE”.
2. Give a reset.
3. Update the HSE FW to the latest version “00 05 00 00 02
00 00 00” with the help of HSE FW service “HSE_SRV_ID_
FIRMWARE_UPDATE”.
4. Update Secure BAF to latest version “00 05 00 00 00 0A
00 03” with the help of HSE FW service “HSE_SRV_ID_
SBAF_UPDATE”.
5. Reset.
00 05 00 00 00 08 00 11
00 05 00 00 02 01 00 00 or
higher
Partially Compatible with the following limitations:
1. “HSE_SRV_ID_FIRMWARE_UPDATE” is not supported.
2. Setting of “IVT AUTH” attribute through service “HSE_SRV_
ID_SET_ATTR”.
Table 167. SBAF and HSE Firmware version compatibility for S32K344, S32K324, and S32K314 devices
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
277 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 278

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Current SBAF Version Number
Current HSE Firmware version
numbers
Remarks
3. Lifecycle advancement feature through service ““HSE_
SRV_ID_SET_ATTR”.
4. If SBAF is not updated (with IVT feature), the Boot Data
Sign feature is not allowed.
5. If pink image HSE Firmware or SBAF is not of latest
version, then the Firmware update is not allowed.
Sequence of steps to be followed to update to latest version
of SBAF and HSE FW:
Update Secure BAF to latest version “00 05 00 00 00 0A 00
03” with the help of HSE FW service “HSE_SRV_ID_SBAF_
UPDATE and give a reset.
00 05 00 00 00 08 00 03
Not compatible. This version of HSE FW should not be installed.
Sequence of steps to be followed to update to latest version
of SBAF and HSE FW:
1. Install latest version “00 05 00 00 02 00 00 00” of HSE
Firmware.
2. Update Secure BAF to latest version “00 05 00 00 00 0A
00 03” with the help of HSE FW service “HSE_SRV_ID_
SBAF_UPDATE”.
3. Reset.
00 05 00 00 00 0A 00 00
00 05 00 00 00 0C 00 00
00 05 00 00 01 01 00 00
Fully Compatible. Sequence of steps to be followed to update
to latest version of SBAF and HSE FW:
1. Update the HSE FW to latest version “00 05 00 00 02 00
00 00” with the help of HSE FW service. “HSE_SRV_ID_
FIRMWARE_UPDATE”.
2. Update Secure BAF to latest version “00 05 00 00 00 0A
00 03” with the help of HSE FW service “HSE_SRV_ID_
SBAF_UPDATE”.
3. Reset.
00 05 00 00 00 09 04 00
00 05 00 00 02 01 00 00 or
higher
Partially Compatible with following limitations:
If SBAF is not updated to latest version, the following services
return an error “HSE_SRV_RSP_SBAF_UPDATE_REQUIRED”.
1. Setting of “IVT AUTH” attribute through service “HSE_SRV_
ID_SET_ATTR”.
2. Lifecycle advancement feature through service ““HSE_
SRV_ID_SET_ATTR”.
3. If SBAF is not updated (with IVT feature), the Boot Data
Sign feature is not allowed.
4. If pink image HSE Firmware or SBAF is not of latest
version, then the Firmware update is not allowed.
Sequence of steps to be followed to update to latest version
of SBAF and HSE FW:
Update Secure BAF to latest version “00 05 00 00 00 0A 00
03” with the help of HSE FW service “HSE_SRV_ID_SBAF_
UPDATE” and give a reset.
Once the SBAF is updated to latest version, then all above
mentioned limitations are not applicable anymore.
00 05 00 00 02 01 00 00 or
higher
Fully Compatible.
00 05 00 00 00 0A 00 03
00 05 00 00 01 01 00 00 or lower
Not compatible. Earlier version HSE firmware do not install in
the device. Only latest version of HSE firmware is allowed to be
installed.
00 05 00 00 00 0F 00 06
00 05 00 00 02 01 00 00 or
higher
Fully Compatible.
Table 167. SBAF and HSE Firmware version compatibility for S32K344, S32K324, and S32K314 devices...continued
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
278 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 279

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Current SBAF Version Number
Current HSE Firmware version
numbers
Remarks
00 05 00 00 01 01 00 00 or lower
Not compatible. Earlier version HSE firmware do not install in
the device. Only latest version of HSE firmware is allowed to be
installed.
Table 167. SBAF and HSE Firmware version compatibility for S32K344, S32K324, and S32K314 devices...continued
SBAF Version Number
HSE Firmware version numbers
Remarks
00 0D 00 00 00 0B 00 00
00 0D 00 00 00 0E 00 00
00 0D 00 00 01 02 00 00
00 0D 00 00 01 02 00 01
Fully Compatible. Sequence of steps to be followed to
update to latest version of SBAF and HSE FW:
1. Update the HSE FW to latest version “00 05 00 00 02 00
00 00” with the help of HSE FW service “HSE_SRV_ID_
FIRMWARE_UPDATE”.
2. Update Secure BAF to latest version “00 05 00 00 00 09
00 01” with the help of HSE FW service “HSE_SRV_ID_
SBAF_UPDATE”.
3. Reset.
00 0D 00 00 00 08 00 00
00 05 00 00 02 06 00 00 or higher
Partially Compatible with following limitations:
If SBAF is not updated to latest version, the following
services return an error “HSE_SRV_RSP_SBAF_UPDATE_
REQUIRED”
1. Setting of “IVT AUTH” attribute through service “HSE_
SRV_ID_SET_ATTR”.
2. Lifecycle advancement feature through service ““HSE_
SRV_ID_SET_ATTR”.
3. If SBAF is not updated (with IVT feature), the Boot Data
Sign feature is not allowed.
4. If pink image HSE Firmware or SBAF is not of latest
version, then the Firmware update is not allowed.
Sequence of steps to be followed to update to latest
version of SBAF and HSE FW:
Update Secure BAF to latest version “00 05 00 00 00 09 00
01” with the help of HSE FW service “HSE_SRV_ID_SBAF_
UPDATE” and give a reset.
Once the SBAF is updated to latest version, then all above
mentioned limitations are not applicable anymore.
00 05 00 00 02 06 00 00 or higher
Fully Compatible.
00 05 00 00 00 09 00 01
00 0D 00 00 01 02 00 01 or lower
Not compatible. Earlier version HSE firmware do not install in
the device. Only latest version of HSE firmware is allowed to be
installed.
00 05 00 00 02 06 00 00 or higher
Fully Compatible.
00 0D 00 00 00 0F 00 06
00 0D 00 00 01 02 00 01 or lower
Not compatible. Earlier version HSE firmware do not install in
the device. Only latest version of HSE firmware is allowed to be
installed.
Table 168. SBAF and HSE Firmware version compatibility for S32K312, S32K342, S32K322 and S32K341
devices
Current SBAF Version Number
Current HSE Firmware version
numbers
Remarks
00 0F 00 00 00 0F 00 07
00 0F 00 00 02 28 00 00
Fully Compatible. All functionalities of HSE Firmware are
supported.
Table 169. SBAF and HSE Firmware version compatibility for S32K396, S32K394, S32K376 and S32K374
devices
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
279 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 280

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Current SBAF Version Number
Current HSE Firmware version
numbers
Remarks
00 0E 00 00 00 0F 00 06
00 0E 00 00 02 28 00 00
Fully Compatible. All functionalities of HSE Firmware are
supported.
Table 170. SBAF and HSE Firmware version compatibility for S32K328, S32K338, S32K348, S32K358, S32K336 and
S32K356 devices
Current SBAF Version Number
Current HSE Firmware version
numbers
Remarks
01 11 00 00 00 10 02 00
00 11 00 00 02 46 00 00
Fully Compatible. All functionalities of HSE Firmware are
supported.
Table 171. SBAF and HSE Firmware version compatibility for S32K389 devices
14.7.1  General guideline applicable for all S32K3 devices
Following steps must be implemented in sequence to update to latest version of SBAF and HSE firmware.
• Whenever there is an earlier version of HSE FW present on the device, then customer must make sure device
is updated to latest version of HSE firmware.
• After updating to latest version of HSE firmware, if older version of Secure BAF is present, then customer
must update to latest version of Secure BAF using the “HSE_SRV_ID_SBAF_UPDATE” service.
14.8  Hardware IP registers changed by HSE during PLL configuration
This section explains the details of registers changed by HSE during PLL configuration.
Below values are provided for based on these assumptions that device is S32K344, FXOSC configuration flag
is programmed in UTEST with value of 16 MHz crystal value and PLL output frequency is 160 MHz. Values
might change in case the crystal value is different and PLL output frequency is 120 MHz.
IP
Register Name
Default value (hex)
Modified value (hex)
PLL Control (PLLCR)
8000_0000h
0000_0000h
PLL Divider (PLLDV)
0C3F_1032h
0400_103Ch
PLL Fractional Divider
(PLLFD)
0000_0000h
0000_0000h
PLL Output Divider
(PLLODIV_0)
0000_0000h
8005_0000h
PLLDIG
PLL Output Divider
(PLLODIV_1)
0000_0000h
8001_0000h
MC_ME
Partition 1 COFB Set 1 Clock
Status Register (PRTN1_
COFB1_STAT)
7CFE_2FFCh
7DFE_2FFCh
Clock Mux 0 Divider 0
Control Register (MUX_0_
DC_0)
8000_0000h
8000_0000h
MC_CGM
Clock Mux 0 Divider 1
Control Register (MUX_0_
DC_1)
8000_0000h
8001_0000h
Table 172. Hardware IP registers changed by HSE during PLL configuration
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
280 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 281

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
IP
Register Name
Default value (hex)
Modified value (hex)
Clock Mux 0 Divider 2
Control Register (MUX_0_
DC_2)
8001_0000h
8003_0000h
Clock Mux 0 Divider 3
Control Register (MUX_0_
DC_3)
8000_0000h
8001_0000h
Clock Mux 0 Divider 4
Control Register (MUX_0_
DC_4)
8000_0000h
8003_0000h
Clock Mux 0 Divider 5
Control Register (MUX_0_
DC_5)
8003_0000h
8003_0000h
Clock Mux 0 Divider 6
Control Register (MUX_0_
DC_6)
8000_0000h
8000_0000h
Clock Mux 0 Select Control
Register (MUX_0_CSC)
0000_0000h
0800_0000h
Clock Mux 0 Divider Trigger
Control Register (MUX_0_
DIV_TRIG_CTRL)
0000_0000h
8000_0000h
PRAMC_0
Platform RAM Configuration
register 1 (PRCR1)
0000_0100h
0000_0001h
PRAMC_1
Platform RAM Configuration
register 1 (PRCR1)
0000_0100h
0000_0001h
c40asf_
flash
Module Control (CTL)
0000_0600h
0000_5000h (Option A)
0000_0400h (Option B)
PMC
PMC Configuration Register
(CONFIG)
refer to S32K3xx
Reference Manual.
HSE is Setting bit 1
(LMBCTLEN) and bit 0 (LMEN)
Table 172. Hardware IP registers changed by HSE during PLL configuration...continued
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
281 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 282

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
15   Revision History
15.1  Revision History
Version
Date
Description of Change
Rev 2.5
05/2025
• Added information for K389 devices.
• Updated table "System attribute structures" in section "HSE system attributes to 
configure security policies" for ABSWAP values.
• Replaced "premium" with "custom" in "Maximum size of the HSE Firmware" table for 
section "Size of the HSE Firmware".
• Added the bit for BACKUP enable/disable in "The Boot Configuration Word (BCW)".
• Updated section "Service channel" in chapter "High-Level System View" to include 
"Note that the channel #0 of any other enabled MU instance can request for 
administrative services".
• Updated section "Potential causes of failure" in chapter "HSE Firmware Installation".
• Added note in section "Memory location" in chapter "Secure Boot and Memory 
Verification Services".
• Updated section "Life cycle (LC)" in chapter "High-Level System View".
• Added section for "MACsec key management" in chapter "Miscellaneous Services".
• Specifying which service type is preemptive and which is non-preemptive in Service 
Type table from "HSE FIrmware Usage" chapter".
Rev 2.4
02/2025
• Updated valid output address table based on lockstep enable/disable for K3x4 devices
• Updated clock frequency options section of "Device Specific Parameters" chapter
• Updated "Delay in processing of first heavy operation after boot" in "Device Specific
Parameters" chapter
• Revised Boot phases diagram in Chapter "Secure boot and memory verification
services" section "Secure boot and automatic SMR verification"
• Added key verification for asymmetric keys
• Added K388 memory layout in Chapter "HSE Firmware Installation" section "Flash
Memory Layout"
• Revised section in chapter "High-Level System View" section "HSE Firmware: Usage"
as host has to wait for HSE_STATUS_INIT_OK before changing the device clock
configurations like enabling PLL
• Added the example code for checking the Flash read/write block bits
• Removed references to DEBUG_DISABLE as it is not supported in HSE-B
• Note added for Boot data sign service as it cannot be used for GMAC of secure
recovery app
• The app image structure for secure recovery application revised for
– GMAC formula
– Application execution begins from the address in IVT
• Host debug permanently disabled
• Updated HSE Flash Memory Integrity for combinations of Code Flash for ECC Older
and New SBAF and FW version
• New section added to include FW update scenarios - covered and not covered both
• Updated size of the firmware section
• Added AppBL backup in IVT table
• Updated MU Installation steps by host in AB_SWAP configuration and FULL_MEM
configuration
• Revised the HSE normal boot flow chart
• Added few alterations in size of Data flash section to deal with unfortunate bit flip
scenario
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
282 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 283

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Version
Date
Description of Change
• Correction related to one-time-programmable (OTP) on-chip non-volatile memory
(UTEST)
• Correction related to LC Advancement
• Correction related to Asset present in sample for FA LC
• Correction related FA LC
• Correct DISABLE_SECURE_RECOVERY_MODE bit Description in BCW
• HSE_B RM BCW Contradicts S32K3xx RM BCW: switched the statements for 0 and
1 for BOOT_SEQ, BOOT_TARGET (CM7_3_ENABLE), BOOT_TARGET (CM7_
2_ENABLE), BOOT_TARGET (CM7_1_ENABLE), and BOOT_TARGET (CM7_0_
ENABLE) in BCW.
Rev 2.3
02/2024
• Added code snippet for Flash Synchronization in Section "Synchronizing flash read/
write access between HSE and application core"
• Added Section "Recurrent automatic SMR verification"
• Updated the Section "Request for Super User rights"
• Added MU installation steps by host in AB_SWAB configuration
• Added MU installation steps by host in FULL_MEM configuration
• Small improvements in the following figures:
– "Illustrating key derivation within the HSE"
– "Encountering ECC Error"
– "Recovering from ECC Error"
• Corrections in the following figures:
– "Flash resources locked during HSE execution"
– "Illustrating application, MU instances and key group partitioning"
Rev 2.2
12/2023
• Update section “Non-Notifying Error Events” with status of SYS-IMG dataset erase
status in HSE_GPR_STATUS_ADDRESS register
• Added clarification for “Secure ADKP Provisioning” section and “Provisioning a
device-dependent ADKP” section
• Added section “Super User execution rights”
• Added “SHE commands vs HSE services”
• Updated “Service execution” section: added more important notes
• Updated section “Variant: fast CMAC generation and verification
• Updated section “Cryptographic services”
– Updated supported HASH primitives
– Added guideline to use the recommended IV size for AES-GCM.
• Updated section “XRDC Configuration”
– Added guideline to enable XRDC after HSE_STATUS_INIT_OK is set
– Fix Code flash mistakenly referred to as Data Flash in Table Default Programming
of MRC Register:
– Add S32K388 HSE Domain ID in Table HSE Domain ID values
• Updated section “Valid output address range (any memory configuration)”
– Re-arranged tables in order of increasing internal flash memory in devices
– Add valid output address ranges table for S32K388
• Update section “Synchronizing flash read/write access between HSE and application
core”
– Remove all sub-sections containing list of services
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
283 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 284

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Version
Date
Description of Change
– Add sub-section “Usage of Secure NVM by HSE FW services” with a table for
secure NVM usage by every HSE FW service in both FULL_MEM and AB_SWAP
configurations
• Update Table Secure BAF version number HSE GPR (0x4039C020)
– Add SOC_Type_ID for S32K388
• Updated section “System attributes”
– Re-arrange various tables and rows within them according to increasing order of
internal flash in devices, add information for S32K388
– Add Boot Target Pointer in IVT for CM7_3
– Add three new bits in BCW: FW_USAGE_FLAG_PROGRAM, BOOT_TARGET
(CM7_3_ENABLE) and RESET_RECOVERY_MODE
– Add details for each bit in the BCW
– Add HSE supported PLL configurations and frequencies on S32K388
• Added chapter “Platform Specific Behavioral and Features”
– Add description of AES_ACCEL in S32K388
• Formatting improvements in chapter “Security Policies”
• Added section “Remove HSE Firmware”
• Added section “SMR Entry erase”
• Added section “Core Reset table update”
• Added section “Disable entry into reset recovery mode” with description of RESET_
RECOVERY_MODE and DCMRWP1 bits
– Add note describing exception of disable recovery mode in case of advanced
secure boot (also added in “DCM register DCMRWP1”)
• Add usage of FW_USAGE_FLAG_PROGRAM in sections “Installation via MU
interface” and “Installation process in AB_SWAP configuration”
• Update table “Hardware IP registers changed by HSE during PLL configuration” –
Update CTL value for S32K3X4 based on Clock option
• Flash memory layout of S32K388 is same as that of S32K358 (see Flash Memory
Layout Section)
• Update “Content” section – Re-arrange in order of increasing internal flash in device
• Rename S32K3X8 with S32K358 in various sections
• Update section “HSE Firmware and Secure BAF release version compatibility” –
Added compatibility details of HSE Firmware with latest secure BAF 0.15.0 for all
S32K3XX devices
• Added section “HSE Firmware Features disabled in newer versions”. Removed their
corresponding detailed sections
• Added a note in section “Secure-BAF update”
• Added HSE_CLK operational frequency range and CMU configuration for S32K388 in
section “Clock Monitoring Unit” and Table Tamper Configuration Status Bit Fields.
• Added description of attribute HSE_FW_BUILD_INFO_ATTR_ID in section “Manage
HSE system attributes”
• Aligned content under various sub-sections of “System attributes”
• Added note describing execution behavioral change of Increment counter service
(section "Monotonic Counter Services")
• Added section “Delay in processing of first Heavy Operation after boot”
• Added details of MU instance when requesting SU rights via administration service
(section "Requesting for SU rights")]
• Added details of FW_IMG Backup flash block presence as per device config (section
"HSE Images: Overview")
• Added important notes of extra boot time after acive/passive partition swap (sections
"HSE Firmware Update (AB_SWAP)" and "Application Update (AB_SWAP)")
• Added details of keyType constraint on SMR authentication key (table SMR table
entry attributes)
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
284 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 285

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Version
Date
Description of Change
• Added more details for Re-seeding frequency (Table RNG Classes)
• Add details for SHA3 (table "MAC algorithms vs. tag sizes")
Rev 2.1
10/2022
1. Added detailed memory layout details in FULL _MEM and AB_SWAP for S32
K344,S32K324,S32K314,S32K312,S32K311,S32K310,S32K342,S32K341, S32
K322,S32K396,S32K394,S32K376,S32K374,S32K358,S32K338,S32K348, S32
K328,S32K356 and S32K336 devices and partial AB_SWAP for S32K358,S32
K338,S32K348,S32K328,S32K356 and S32K336 devices.
2. Addition of details of MWCT series
3. Updated the figure of Secure Recovery Application
4. Added details related to PLL configuration and DCF record programming
5. IVT contents are added for new S32K3XX variants
6. Valid output memory ranges contents are added for new S32K3XX variants
Rev 2.0
06/2022
1. Updated the description of XRDC configuration at various places.
2. IVT content is modified.
3. HSE GPR registers are updated.
4. Memory map of various K3 variants is updated.
5. Added details about SHE UID
6. Updated the UID usage for Provisioning a device-dependent ADKP.
7. Updated theSecure ADKP Provisioning section.
8. Added more clarifications in Debug section.
9. Update the DH private/public key description
10. Updated the key provisioning usage when importing a key: a key imported in an
encrypted format must be always authenticated (7.2.3.2 and 13.4 sections)
11. Updated Secure Boot and Memory Verification Services: add the types of secure
boot; updated the SMR entry to include the AAD data
12. Added the section which captures the details of various SBAF and HSE firmware
versions.
Rev 1.2
01/2022
1. Removed the chapter which describes the various releases of HSE FW. This
information is now captured in release notes
2. Modified the valid output address range table in “Device Specific Parameter”
chapter
3. Added the description of firmware installation through MU for AB swap configuration
4. Enhanced the recovery mode section
5. Added Secure BAF version, DCMSTAT in “Device specific Parameter” chapter.
Rev 1.1
10/2021
1. Added the content related to Import and Export stream context
2. Updated the content on flash synchronization scenario.
3. Updated the “Key management” section:
a. The RAM provisioning keys can be used only to import/export RAM keys
(cannot be used to import NVM keys)
b. Added HSE_ERASE_KEYGROUP_ON_MU_IF option to erase a group of keys
Rev 1.0
09/2021
1. Added the details of HSE firmware version and compatible S32K3 Device variants.
2. Added the description of HSE_RAM_PUB_KEY_IMPORT_POLICY_ATTR_ID
attribute.
3. Added the description about hse_status_and_errors.h and hse_srv_responses.h
files.
Rev.0 DRAFT M
08/2021
1. Added description for PLL configuration in HSE Firmware.
2. Updated Core Reset table installation in HSE Firmware.
Rev.0 DRAFT L
07/2021
1. Updated the new design of Secure-Boot and normal boot flow
2. Updated the new design by Firmware Update
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
285 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 286

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Version
Date
Description of Change
3. SBAF Update feature added.
4. Tamper Service added
5. Integrity Service added.
6. Memory Region Attribute added
7. Error Management Section added
8. HSE Firmware Handshake update
9. Removed TDES support
10. Monotonic Counter Configuration section updated
11. Valid output address range to be considered for Lockstep enabled and disabled
12. Addition of Handshake install mechanism
13. Added CMAC with Counter and Burmester Desmedt Protocol details.
Rev.0 DRAFT K
11/2020
1. Updated the content in the memory verification chapter related to SHE based
secure boot.
2. Updated the document description chapter related to custom firmware.
Rev.0 DRAFT J
09/2020
Initial Version
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
286 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 287

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Legal information
Definitions
Draft — A draft status on a document indicates that the content is still
under internal review and subject to formal approval, which may result
in modifications or additions. NXP Semiconductors does not give any
representations or warranties as to the accuracy or completeness of
information included in a draft version of a document and shall have no
liability for the consequences of use of such information.
Disclaimers
Limited warranty and liability — Information in this document is believed
to be accurate and reliable. However, NXP Semiconductors does not give
any representations or warranties, expressed or implied, as to the accuracy
or completeness of such information and shall have no liability for the
consequences of use of such information. NXP Semiconductors takes no
responsibility for the content in this document if provided by an information
source outside of NXP Semiconductors.
In no event shall NXP Semiconductors be liable for any indirect, incidental,
punitive, special or consequential damages (including - without limitation -
lost profits, lost savings, business interruption, costs related to the removal
or replacement of any products or rework charges) whether or not such
damages are based on tort (including negligence), warranty, breach of
contract or any other legal theory.
Notwithstanding any damages that customer might incur for any reason
whatsoever, NXP Semiconductors’ aggregate and cumulative liability
towards customer for the products described herein shall be limited in
accordance with the Terms and conditions of commercial sale of NXP
Semiconductors.
Right to make changes — NXP Semiconductors reserves the right to
make changes to information published in this document, including without
limitation specifications and product descriptions, at any time and without
notice. This document supersedes and replaces all information supplied prior
to the publication hereof.
Applications — Applications that are described herein for any of these
products are for illustrative purposes only. NXP Semiconductors makes no
representation or warranty that such applications will be suitable for the
specified use without further testing or modification.
Customers are responsible for the design and operation of their
applications and products using NXP Semiconductors products, and NXP
Semiconductors accepts no liability for any assistance with applications or
customer product design. It is customer’s sole responsibility to determine
whether the NXP Semiconductors product is suitable and fit for the
customer’s applications and products planned, as well as for the planned
application and use of customer’s third party customer(s). Customers should
provide appropriate design and operating safeguards to minimize the risks
associated with their applications and products.
NXP Semiconductors does not accept any liability related to any default,
damage, costs or problem which is based on any weakness or default
in the customer’s applications or products, or the application or use by
customer’s third party customer(s). Customer is responsible for doing all
necessary testing for the customer’s applications and products using NXP
Semiconductors products in order to avoid a default of the applications
and the products or of the application or use by customer’s third party
customer(s). NXP does not accept any liability in this respect.
Terms and conditions of commercial sale — NXP Semiconductors
products are sold subject to the general terms and conditions of commercial
sale, as published at https://www.nxp.com/profile/terms, unless otherwise
agreed in a valid written individual agreement. In case an individual
agreement is concluded only the terms and conditions of the respective
agreement shall apply. NXP Semiconductors hereby expressly objects to
applying the customer’s general terms and conditions with regard to the
purchase of NXP Semiconductors products by customer.
Suitability for use in automotive applications — This NXP product has
been qualified for use in automotive applications. If this product is used
by customer in the development of, or for incorporation into, products or
services (a) used in safety critical applications or (b) in which failure could
lead to death, personal injury, or severe physical or environmental damage
(such products and services hereinafter referred to as “Critical Applications”),
then customer makes the ultimate design decisions regarding its products
and is solely responsible for compliance with all legal, regulatory, safety,
and security related requirements concerning its products, regardless of
any information or support that may be provided by NXP. As such, customer
assumes all risk related to use of any products in Critical Applications and
NXP and its suppliers shall not be liable for any such use by customer.
Accordingly, customer will indemnify and hold NXP harmless from any
claims, liabilities, damages and associated costs and expenses (including
attorneys’ fees) that NXP may incur related to customer’s incorporation of
any product in a Critical Application.
Export control — This document as well as the item(s) described herein
may be subject to export control regulations. Export might require a prior
authorization from competent authorities.
HTML publications — An HTML version, if available, of this document is
provided as a courtesy. Definitive information is contained in the applicable
document in PDF format. If there is a discrepancy between the HTML
document and the PDF document, the PDF document has priority.
Translations — A non-English (translated) version of a document, including
the legal information in that document, is for reference only. The English
version shall prevail in case of any discrepancy between the translated and
English versions.
Security — Customer understands that all NXP products may be subject to
unidentified vulnerabilities or may support established security standards or
specifications with known limitations. Customer is responsible for the design
and operation of its applications and products throughout their lifecycles
to reduce the effect of these vulnerabilities on customer’s applications
and products. Customer’s responsibility also extends to other open and/or
proprietary technologies supported by NXP products for use in customer’s
applications. NXP accepts no liability for any vulnerability. Customer should
regularly check security updates from NXP and follow up appropriately.
Customer shall select products with security features that best meet rules,
regulations, and standards of the intended application and make the
ultimate design decisions regarding its products and is solely responsible
for compliance with all legal, regulatory, and security related requirements
concerning its products, regardless of any information or support that may be
provided by NXP.
NXP has a Product Security Incident Response Team (PSIRT) (reachable
at PSIRT@nxp.com) that manages the investigation, reporting, and solution
release to security vulnerabilities of NXP products.
NXP B.V. — NXP B.V. is not an operating company and it does not distribute
or sell products.
Trademarks
Notice: All referenced brands, product names, service names, and
trademarks are the property of their respective owners.
NXP — wordmark and logo are trademarks of NXP B.V.
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
287 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 288

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Tables
Tab. 1.
Reference documents ....................................... 3
Tab. 2.
Acronyms ...........................................................4
Tab. 3.
Illustrating big- vs. little-endianness byte
ordering ............................................................. 6
Tab. 4.
LC states .........................................................14
Tab. 5.
HSE firmware capabilities vs. LC .................... 16
Tab. 6.
Host debugging capabilities vs. LC ................. 17
Tab. 7.
HSE firmware deliverables ..............................19
Tab. 8.
MU register usage for service channel #i
(from the host perspective) ............................. 24
Tab. 9.
HSE global status bits in FSR .........................24
Tab. 10.
HSE global status bits #17 to #20 ...................25
Tab. 11.
HSE interrupt to host ...................................... 26
Tab. 12.
Functions covered by the reference HSE
MU driver .........................................................28
Tab. 13.
CPU subsystems released from reset by
the HSE ...........................................................31
Tab. 14.
Entry into recovery mode behavior ..................37
Tab. 15.
Authenticity checks during start-up ................. 37
Tab. 16.
One-time configurable HSE system
attributes ..........................................................80
Tab. 17.
BCW content ...................................................81
Tab. 18.
Service ID format ............................................ 83
Tab. 19.
Service Type ................................................... 83
Tab. 20.
Service classes ............................................... 84
Tab. 21.
Execution rights and respective limitations
in Key Management ........................................ 89
Tab. 22.
Execution rights and respective limitations
in HSE configuration ....................................... 90
Tab. 23.
Determining the host identity ...........................90
Tab. 24.
Host identity vs. LC .........................................90
Tab. 25.
Host identity vs. key group owner ................... 91
Tab. 26.
Checking execution rights and host identity .... 91
Tab. 27.
LC states vs. ECU manufacturing steps ..........91
Tab. 28.
Execution rights after reset ............................. 91
Tab. 29.
Scatter/gather options vs. input / output
parameter types .............................................. 96
Tab. 30.
Key types ........................................................ 99
Tab. 31.
Key characteristics ........................................ 100
Tab. 32.
Elliptic curve types supported ....................... 101
Tab. 33.
Key attributes ................................................ 102
Tab. 34.
Key access restriction flags ...........................103
Tab. 35.
Key usage flags ............................................ 103
Tab. 36.
SMR verification map for key usage ..............104
Tab. 37.
Key catalogs ..................................................105
Tab. 38.
ROM key catalog configuration ..................... 105
Tab. 39.
Usage restrictions on ROM keys ...................106
Tab. 40.
Maximum key sizes vs. key types ................. 106
Tab. 41.
MU instance map for key usage ....................107
Tab. 42.
Key group owners .........................................107
Tab. 43.
Maximum number of key groups and key
slots ............................................................... 108
Tab. 44.
Key handle format .........................................109
Tab. 45.
Key handle examples ....................................109
Tab. 46.
Encryption and authentication key handles
(key import/export services) .......................... 111
Tab. 47.
Key provisioning usage when importing a
key in an empty slot in the NVM key
catalog ...........................................................111
Tab. 48.
Key provisioning usage when updating a
key (non-empty slot) in the NVM Key
Catalog .......................................................... 112
Tab. 49.
Key provisioning usage when provisioning
a key in the RAM Key Catalog ......................113
Tab. 50.
Parameters for an encrypted key import ....... 114
Tab. 51.
Parameters for an authenticated key import ..114
Tab. 52.
Key attribute mapping in pKeyInfo ................ 115
Tab. 53.
Key usage flag restrictions for key import/
export services .............................................. 116
Tab. 54.
Key attribute setting examples ...................... 116
Tab. 55.
Pointer to provisioning key values vs. key
type ................................................................116
Tab. 56.
Key size setting vs. key type .........................118
Tab. 57.
Encoding of EC point coordinates .................119
Tab. 58.
Elliptic curve identifiers and parameter
definition ........................................................ 119
Tab. 59.
HSE ECC curves .......................................... 120
Tab. 60.
Key export settings (encrypted and
authenticated key) .........................................123
Tab. 61.
Parameters for an encrypted key export ....... 123
Tab. 62.
Parameters for an authenticated key export ..124
Tab. 63.
Pointer to exported key values vs. key type .. 125
Tab. 64.
HSE KDF Algorithms .....................................132
Tab. 65.
Properties of a shared secret (key
agreement protocol) ...................................... 136
Tab. 66.
Erasing multiple keys .................................... 137
Tab. 67.
SHE keys ...................................................... 138
Tab. 68.
Extended SHE keys ...................................... 139
Tab. 69.
SHE key security flags ..................................140
Tab. 70.
Acronyms used in the SHE key update
protocol ..........................................................141
Tab. 71.
Key ID values in SHE key update protocol ....141
Tab. 72.
Mapping of M1, M2 and M3 .......................... 142
Tab. 73.
Mapping of M4 and M5 .................................142
Tab. 74.
KDF input constants for K1 and K3 ...............143
Tab. 75.
KDF input constants for K2 and K4 ...............144
Tab. 76.
Ciphers and corresponding block sizes .........146
Tab. 77.
Hash block sizes and digest sizes ................ 146
Tab. 78.
Block ciphering modes and corresponding
encryption / decryption algorithms .................147
Tab. 79.
MAC algorithms vs. tag sizes ........................156
Tab. 80.
EdDSA parameter instances vs. the
signature mode ............................................. 165
Tab. 81.
EdDSA parameters instances vs. the
selected curve ............................................... 165
Tab. 82.
Input and output size constraints on service
call (RSA / ECC signature) ............................167
Tab. 83.
Maximum input message size (RSA
encryption with PKCS1 V1.5 encoding) .........168
Tab. 84.
Maximum of input message (RSA
encryption with OAEP encoding) ...................169
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
288 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 289

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Tab. 85.
Input and output size constraints on service
call (RSA ciphering) ...................................... 170
Tab. 86.
RNG Classes ................................................ 172
Tab. 87.
SMR table entry attributes .............................176
Tab. 88.
SMR decryption parameters ..........................177
Tab. 89.
Additional SMR configuration flags ............... 177
Tab. 90.
CR table entry attributes ............................... 178
Tab. 91.
Sanctions on pre-boot and post-boot
phases ...........................................................179
Tab. 92.
Options in hseSmrVerifySrv_t ....................... 185
Tab. 93.
Sanction on a key usage after SMR
verification ..................................................... 193
Tab. 94.
Sanction on a subsystem (all SMR verified
in pre-boot phase) .........................................193
Tab. 95.
Sanction on a subsystem (at least one
SMR in primary map not verified in pre-
boot phase) ................................................... 194
Tab. 96.
Sanction on a subsystem (at least one
SMR not verified in post-boot phase) ............ 194
Tab. 97.
SMR source / destination addresses .............205
Tab. 98.
SMR availability in RAM after start-up ...........206
Tab. 99.
HSE system attributes ...................................208
Tab. 100. System attribute structures ............................208
Tab. 101. Tamper configuration status bit fields ............ 211
Tab. 102. Challenge format when requesting SU
rights with MASTER_ECU_KEY ....................215
Tab. 103. Challenge format when requesting SU
rights with a key different from MASTER_
ECU_KEY ......................................................215
Tab. 104. : Response parameters vs. authentication
scheme ..........................................................215
Tab. 105. SU rights owner after request ....................... 215
Tab. 106. Illustrating monotonic counter value
evolution in application and data Flash ......... 218
Tab. 107. HSE system events logging in GSR ..............221
Tab. 108. MC_RGM Destructive reset status during
CMU configuration .........................................222
Tab. 109. HSE data flash error logging in GPR .............227
Tab. 110. FW Update Service Structure ....................... 228
Tab. 111.
FW-IMG header format (FULL_MEM) ...........233
Tab. 112. FW-IMG header format (AB_SWAP) .............233
Tab. 113. Secure-BAF Update Service Structure ..........234
Tab. 114. Secure-BAF header format ........................... 235
Tab. 115. hseKHTTEntry_t structure .............................240
Tab. 116. HSE key handle vs ACE key index
mapping .........................................................241
Tab. 117. IVT start address ...........................................242
Tab. 118. IVT structure ..................................................243
Tab. 119. BCW bit mapping ..........................................244
Tab. 120. PLL Configuration in HSE Firmware ............. 245
Tab. 121. Clock Frequencies for various clocking
options in S32K3xx devices (except
S32K3X6 and S32K388) ............................... 246
Tab. 122. Clock Frequencies for various clocking
options in the S32K3X6 family of devices ......246
Tab. 123. Clock Frequencies for various clocking
options in the S32K388 family of devices ......246
Tab. 124. Clock Frequencies for various clocking
options in the S32K389 devices ....................246
Tab. 125. BOOT_TARGET vs. CPU subsystem ............247
Tab. 126. AppBL structure ............................................ 247
Tab. 127. JTAG based Recovery mode Start address .. 247
Tab. 128. Current size of the HSE Firmware ................ 248
Tab. 129. Maximum size of the HSE Firmware .............248
Tab. 130. Hash primitives supported (HSE_B) ..............248
Tab. 131. HMAC primitives supported (HSE_B) ............248
Tab. 132. Secure NVM mapping (FULL_MEM) .............249
Tab. 133. Secure NVM mapping (AB_SWAP) ...............249
Tab. 134. Application NVM mapping (FULL_MEM) .......250
Tab. 135. Application NVM mapping (AB_SWAP) .........251
Tab. 136. UTEST Device configuration .........................252
Tab. 137. HSE Domain ID values ................................. 253
Tab. 138. Default programming of MRC register by
HSE ............................................................... 253
Tab. 139. Default Configuration of MRC when HSE
FW Usage Feature Flag is Enabled .............. 254
Tab. 140. PDAC programing by HSE ............................255
Tab. 141. Secure BAF version number HSE_
CONFIG_GPR3 (0x4039C020) .....................256
Tab. 142. Status Bits on HSE_CONFIG_GPR3
(0x4039C028) ................................................256
Tab. 143. HSE Secure Memory sizes in HSE GPR
Registers ....................................................... 258
Tab. 144. DCM register DCMRWP1 (address
0x402AC400) .................................................258
Tab. 145. DCM register DCMSTAT (0x402AC000) ....... 259
Tab. 146. HSE Secure Memory sizes in HSE GPR
Registers ....................................................... 260
Tab. 147. FLASH BLOCKS IN DIFFERENT SOC .........261
Tab. 148. Potential synchronization issues between
core_0/1 and HSE while accessing data
flash ...............................................................262
Tab. 149. Potential synchronization issues between
core_0/1 and HSE while accessing code
flash block ..................................................... 263
Tab. 150. Potential synchronization issues between
core_0/1 and HSE while accessing UTEST .. 263
Tab. 151. Flash Access by HSE FW Services in
FULL_MEM Devices ..................................... 264
Tab. 152. Flash Access by HSE FW Services in AB_
SWAP Devices ..............................................267
Tab. 153. Number of MU instances and TRi / RRi
registers .........................................................270
Tab. 154. Valid output address range for S32K3x1 ....... 271
Tab. 155. Valid output address range for S32K3x2 ....... 271
Tab. 156. Valid output address range for S32K3x4 ....... 271
Tab. 157. Valid output address range for S32K3x6 ....... 272
Tab. 158. Valid output address range for S32K358
series .............................................................272
Tab. 159. Valid output address range for S32K388 .......273
Tab. 160. Valid output address range for S32K389 .......273
Tab. 161. Services that need Super User rights for
execution ....................................................... 274
Tab. 162. SHE commands vs HSE services ................. 275
Tab. 163. List of services involving delay when given
for the first time after boot .............................276
Tab. 164. HSE Firmware features disabled in
0.2.40.0 ..........................................................276
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
289 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 290

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Tab. 165. Subsystem vs. core identifiers (coreId) ......... 277
Tab. 166. SBAF and HSE Firmware version
compatibility for S32K310 and S32K311
devices .......................................................... 277
Tab. 167. SBAF and HSE Firmware version
compatibility for S32K344, S32K324, and
S32K314 devices .......................................... 277
Tab. 168. SBAF and HSE Firmware version
compatibility for S32K312, S32K342,
S32K322 and S32K341 devices ....................279
Tab. 169. SBAF and HSE Firmware version
compatibility for S32K396, S32K394,
S32K376 and S32K374 devices ....................279
Tab. 170. SBAF and HSE Firmware version
compatibility for S32K328, S32K338,
S32K348, S32K358, S32K336 and
S32K356 devices .......................................... 280
Tab. 171. SBAF and HSE Firmware version
compatibility for S32K389 devices ................ 280
Tab. 172. Hardware IP registers changed by HSE
during PLL configuration ............................... 280
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
290 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 291

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Figures
Fig. 1.
Illustrating a byte array storage in memory ....... 6
Fig. 2.
Top-level system view (simplified) .....................9
Fig. 3.
HSE installation / configuration states vs.
LC states: (Frame of reference from SBAF
(HSE Core)) .................................................... 15
Fig. 4.
HSE installation / configuration states vs.
LC states: (Frame of reference from Host
Core) ............................................................... 16
Fig. 5.
Illustrating the Messaging Unit (MU) ............... 22
Fig. 6.
Service channel status transitions ...................23
Fig. 7.
Illustrating application, MU instances and
key group partitioning ......................................27
Fig. 8.
Start-up flow ....................................................32
Fig. 9.
Installation boot flow ....................................... 33
Fig. 10.
HSE normal boot flow ..................................... 34
Fig. 11.
Secure Recovery Mode ...................................35
Fig. 12.
JTAG Based Recovery Mode ..........................36
Fig. 13.
Provisioning a device-dependent
password / debug key ..................................... 39
Fig. 14.
Logic in HSE Firmware for programming
the ADKP ........................................................ 40
Fig. 15.
Simplified system view before installation ....... 42
Fig. 16.
Simplified system view after installation .......... 43
Fig. 17.
Simplified system view before installation ....... 44
Fig. 18.
Simplified system view after installation .......... 45
Fig. 19.
Simplified system view before installation ....... 46
Fig. 20.
Simplified system view after installation .......... 47
Fig. 21.
MU Interface installation flow for SBAF in
FULL_MEM configuration ................................48
Fig. 22.
Flash memory layout during HSE firmware
installation (FULL_MEM) .................................49
Fig. 23.
MU Interface installation flow for SBAF in
AB_SWAP configuration ..................................51
Fig. 24.
Flash memory layout during HSE firmware
installation (AB_SWAP) ...................................52
Fig. 25.
Illustrations of Flash memory layout of
S32K311 in FULL_MEM ..................................54
Fig. 26.
Illustrations of Flash memory layout of
S32K311 in AB_SWAP ....................................55
Fig. 27.
Illustrations of Flash memory layout of
S32K310 in FULL_MEM ................................. 56
Fig. 28.
Illustrations of Flash memory layout of
S32K310 in AB_SWAP ................................... 57
Fig. 29.
Illustrations of Flash memory layout of
S32K312, S32K322 and S32K342 in
FULL_MEM ..................................................... 58
Fig. 30.
Illustrations of Flash memory layout of
S32K312, S32K322 and S32K342 in AB_
SWAP .............................................................. 59
Fig. 31.
Illustrations of Flash memory layout of
S32K341 in FULL_MEM ................................. 60
Fig. 32.
Illustrations of Flash memory layout of
S32K341 in AB_SWAP ................................... 61
Fig. 33.
Illustrations of Flash memory layout of
S32K344, S32K314 and S32K324 in
FULL_MEM ..................................................... 62
Fig. 34.
Illustrations of Flash memory layout of
S32K344, S32K314 and S32K324 in AB_
SWAP .............................................................. 63
Fig. 35.
Illustrations of Flash memory layout of
S32K396 and S32K376 in FULL_MEM ...........64
Fig. 36.
Illustrations of Flash memory layout of
S32K396 and S32K376 in AB_SWAP .............65
Fig. 37.
Illustrations of Flash memory layout of
S32K394 and S32K374 in FULL_MEM ...........66
Fig. 38.
Illustrations of Flash memory layout of
S32K394 and S32K374 in AB_SWAP .............67
Fig. 39.
Illustrations of Flash memory layout
of S32K328, S32K338, S32K348 and
S32K358 in FULL_MEM ................................. 68
Fig. 40.
Illustrations of Flash memory layout
of S32K328, S32K338, S32K348 and
S32K358 in AB_SWAP ................................... 69
Fig. 41.
Illustrations of Flash memory layout
of S32K328, S32K338, S32K348 and
S32K358 in Partial AB_SWAP ........................ 70
Fig. 42.
Illustrations of Flash memory layout of
S32K336 and S32K356 in FULL_MEM ...........71
Fig. 43.
Illustrations of Flash memory layout of
S32K336 and S32K356 in AB_SWAP .............72
Fig. 44.
Illustrations of Flash memory layout of
S32K336 and S32K356 in Partial AB_
SWAP .............................................................. 73
Fig. 45.
Illustrations of Flash memory layout of
S32K388 in FULL_MEM ................................. 74
Fig. 46.
Illustrations of Flash memory layout of
S32K388 in AB_SWAP ................................... 75
Fig. 47.
Illustrations of Flash memory layout of
S32K389 in FULL_MEM ................................. 76
Fig. 48.
Illustrations of Flash memory layout of
S32K389 in AB_SWAP ................................... 77
Fig. 49.
Simplified system view before configuration ....79
Fig. 50.
Simplified system view after configuration .......80
Fig. 51.
Service request flow (synchronous) ................ 86
Fig. 52.
Service request flow (asynchronous) .............. 87
Fig. 53.
Service response flow (asynchronous) ............87
Fig. 54.
Illustrating service execution by the HSE ........ 89
Fig. 55.
Flash resources locked during HSE
execution ......................................................... 92
Fig. 56.
Illustrating streaming contexts import /
export ...............................................................94
Fig. 57.
Illustrating a scatter/gather list ........................ 96
Fig. 58.
Illustrating the key catalogs .............................98
Fig. 59.
Illustrating the repartition of key values and
properties .......................................................100
Fig. 60.
Illustrating the use of a key container
(provisioning an RSA public key) .................. 117
Fig. 61.
Illustrating the use of a key container
(exporting an ECC key in a CSR) ................. 126
Fig. 62.
Illustrating key derivation within the HSE .......132
Fig. 63.
Illustrating key copy within the HSE .............. 134
Fig. 64.
KDERIV = KDF(K, C) ....................................143
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
291 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 292

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Fig. 65.
Random number generation: high-level
view ............................................................... 171
Fig. 66.
Illustrating the memory verification service
(SMR) ............................................................ 174
Fig. 67.
Illustrating the SMR installation and
verification processes ....................................175
Fig. 68.
SMR table configuration example (S32K3) ....178
Fig. 69.
SMR Installation for SHE .............................. 183
Fig. 70.
Application and SMR update scenario .......... 187
Fig. 71.
SMR verification failure scenario ...................188
Fig. 72.
SMR verification passing scenario ................ 189
Fig. 73.
Address translation logic AB_SWAP
configuration ..................................................190
Fig. 74.
Pre-boot / boot / post-boot phases (BOOT_
SEQ == 1) .....................................................192
Fig. 75.
Example of secure boot configuration
depending on core reset strategies ...............195
Fig. 76.
Secure boot and CR table parsing ................ 196
Fig. 77.
Verification of SMR linked via
preBootSmrMap ............................................ 197
Fig. 78.
Verification of SMR linked via
altPreBootSmrMap and applying sanctions
in pre-boot phase ..........................................198
Fig. 79.
Loading SMR linked via postBootSmrMap
in pre-boot phase ..........................................199
Fig. 80.
Releasing the cores from reset - boot
phase .............................................................200
Fig. 81.
Verification of SMR linked via
postBootSmrMap and applying sanctions in
post-boot phase ............................................ 201
Fig. 82.
On-demand secure boot request ...................203
Fig. 83.
SHE SMR Verifications ................................. 205
Fig. 84.
ADKP extension for IVT authentication ......... 213
Fig. 85.
Passive Tamper Example Behavior ...............223
Fig. 86.
Active Tamper Example Behavior ................. 223
Fig. 87.
Encountering ECC Error ............................... 225
Fig. 88.
Recovering from ECC Error .......................... 226
Fig. 89.
Illustrating HSE Firmware update in AB_
SWAP configuration ...................................... 230
Fig. 90.
Illustrating the change from FULL_MEM to
AB_SWAP configuration ................................231
Fig. 91.
Illustrating application update in AB_SWAP
configuration ..................................................232
Fig. 92.
Illustrating roll back to previous version of
application image .......................................... 233
Fig. 93.
High level system configuration for flash
access ........................................................... 261
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
292 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 293

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
Contents
1
Document Description .................................... 2
1.1
Content .............................................................. 2
1.2
Intended readers ............................................... 2
1.3
Disclaimer .......................................................... 2
1.4
Reference documents ........................................2
1.5
Acronyms ...........................................................4
1.6
Conventions and notations ................................6
1.6.1
Number representation ......................................6
1.6.2
C-like memory representation ............................6
1.6.3
Mathematical notations and functions ............... 7
1.6.4
Cryptographic notations .....................................7
1.6.5
Bit manipulation functions ..................................7
2
High-Level System View ................................. 9
2.1
Top-level system architecture ............................ 9
2.2
The host ...........................................................10
2.2.1
CPU subsystems ............................................. 10
2.2.2
Memory resources ...........................................10
2.2.2.1
Application RAM .............................................. 10
2.2.2.2
Application NVM .............................................. 10
2.2.3
Unique device identifier (UID) ..........................10
2.2.4
Host system images ........................................ 10
2.2.5
System bus and XRDC ................................... 11
2.3
The HSE subsystem ........................................11
2.3.1
HSE subsystem variants and software
packages ..........................................................11
2.3.2
CPU subsystem ...............................................12
2.3.3
Cryptographic accelerators ..............................12
2.3.4
True random number generator .......................12
2.3.5
System timers for self-monitoring .................... 12
2.3.6
Memory resources ...........................................12
2.3.6.1
Secure RAM .................................................... 12
2.3.6.2
Secure NVM .................................................... 12
2.3.6.3
Memory mapped resources accessible by
the HSE ........................................................... 13
2.3.7
HSE images .....................................................13
2.3.7.1
Overview ..........................................................13
2.3.8
Life cycle (LC) ................................................. 13
2.4
HSE subsystem software components ............ 17
2.4.1
SBAF ................................................................17
2.4.2
The HSE firmware ...........................................19
2.4.2.1
HSE firmware deliverables .............................. 19
2.4.2.2
HSE security services ......................................19
2.4.2.3
General operation flow .................................... 20
2.4.2.4
Special operation flow ..................................... 21
2.5
The HSE interface ...........................................21
2.5.1
Messaging Unit (MU) .......................................21
2.5.1.1
Overview ..........................................................21
2.5.1.2
Service channel ............................................... 23
2.5.1.3
HSE status .......................................................24
2.5.1.4
Interrupts ..........................................................26
2.5.1.5
Restrictions on key usage ............................... 26
2.5.1.6
Access restrictions enforced by the XRDC ...... 26
2.5.1.7
Enabling or disabling service channels ............27
2.5.1.8
Reference HSE MU driver ...............................28
2.6
External system interfaces .............................. 30
2.6.1
Reset (start-up flow) ........................................ 30
2.6.1.1
Reset-release flow (CPU subsystems) ............ 30
2.6.1.2
Start-up flow .................................................... 31
2.6.1.3
Recovery Mode ............................................... 34
2.6.1.4
Debug .............................................................. 37
3
HSE Firmware Installation ............................ 41
3.1
Scope ...............................................................41
3.2
Installation process in FULL_MEM
configuration .................................................... 41
3.2.1
Installation via IVT ...........................................42
3.2.2
Installation via default Application NVM
location .............................................................44
3.2.3
Installation via MU interface ............................ 45
3.2.3.1
MU Installation steps by host in FULL_
MEM configuration ...........................................49
3.2.4
Flash Memory Layout (FULL_MEM) during
Firmware Installation ........................................49
3.3
Installation process in AB_SWAP
configuration .................................................... 50
3.3.1
MU Installation steps by host in AB_SWAP
configuration .................................................... 52
3.3.2
Flash Memory Layout (AB_SWAP) during
Firmware Installation ........................................52
3.4
Potential causes of failure ............................... 53
3.5
Flash memory layout ....................................... 53
3.5.1
Flash Memory Layout for S32K311,
S32M276, MWCT2015S devices .....................54
3.5.1.1
Illustrations of Flash memory layout in
FULL_MEM ......................................................54
3.5.1.2
Illustrations of Flash memory layout in AB_
SWAP .............................................................. 55
3.5.2
Flash Memory Layout for S32K310,
MWCT2014S and S32M274 devices ...............56
3.5.2.1
Illustrations of Flash memory layout in
FULL_MEM ......................................................56
3.5.2.2
Illustrations of Flash memory layout in AB_
SWAP .............................................................. 57
3.5.3
Flash Memory Layout for S32K312,
S32K322 and S32K342 devices ......................58
3.5.3.1
Illustrations of Flash memory layout in
FULL_MEM ......................................................58
3.5.3.2
Illustrations of Flash memory layout in AB_
SWAP .............................................................. 59
3.5.4
Flash Memory Layout for S32K341 device ...... 60
3.5.4.1
Illustrations of Flash memory layout in
FULL_MEM ......................................................60
3.5.4.2
Illustrations of Flash memory layout in AB_
SWAP .............................................................. 61
3.5.5
Flash Memory Layout for S32K344,
S32K314 and S32K324 devices ......................62
3.5.5.1
Illustrations of Flash memory layout in
FULL_MEM ......................................................62
3.5.5.2
Illustrations of Flash memory layout in AB_
SWAP .............................................................. 63
3.5.6
Flash Memory Layout for S32K396 and
S32K376 devices .............................................64
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
293 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 294

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
3.5.6.1
Illustrations of Flash memory layout in
FULL_MEM ......................................................64
3.5.6.2
Illustrations of Flash memory layout in AB_
SWAP .............................................................. 65
3.5.7
Flash Memory Layout for S32K394 and
S32K374 device .............................................. 66
3.5.7.1
Illustrations of Flash memory layout in
FULL_MEM ......................................................66
3.5.7.2
Illustrations of Flash memory layout in AB_
SWAP .............................................................. 67
3.5.8
Flash Memory Layout for S32K328,
S32K338, S32K348 and S32K358 devices ......68
3.5.8.1
Illustrations of Flash Memory Layout in
FULL_MEM ......................................................68
3.5.8.2
Illustrations of Flash Memory Layout in AB_
SWAP .............................................................. 69
3.5.8.3
Illustrations of Flash Memory Layout in
Partial AB_SWAP ............................................ 70
3.5.9
Flash Memory Layout for S32K336 and
S32K356 devices .............................................71
3.5.9.1
Illustrations of Flash Memory Layout in
FULL_MEM ......................................................71
3.5.9.2
Illustrations of Flash memory layout in AB_
SWAP .............................................................. 72
3.5.9.3
Illustrations of Flash Memory Layout in
Partial AB_SWAP ............................................ 73
3.5.10
Flash Memory Layout for S32K388 devices .... 74
3.5.10.1
Illustrations of Flash memory layout in
FULL_MEM ......................................................74
3.5.10.2
Illustrations of Flash Memory Layout in AB_
SWAP .............................................................. 75
3.5.11
Flash Memory Layout for S32K389 devices .... 76
3.5.11.1
Illustrations of Flash memory layout in
FULL_MEM ......................................................76
3.5.11.2
Illustrations of Flash Memory Layout in AB_
SWAP .............................................................. 77
4
HSE Firmware Configuration ........................78
4.1
Scope ...............................................................78
4.2
Configuration ....................................................79
4.2.1
Configurable HSE system attributes ................80
4.2.2
Start-up parameters in IVT .............................. 81
5
HSE Firmware Usage .................................... 83
5.1
Service descriptor ............................................83
5.2
Service ID ........................................................83
5.3
Service request and response .........................84
5.4
Service execution ............................................ 88
5.4.1
Service execution order ...................................88
5.4.2
Execution rights (Super User vs. User) ............89
5.4.2.1
Definition ..........................................................89
5.4.2.2
Execution rights after reset ..............................91
5.4.2.3
Requesting for SU rights ................................. 92
5.4.2.4
Flash resources locked during HSE
execution ..........................................................92
5.4.3
One-pass execution mode ...............................93
5.4.4
Streaming execution mode ..............................93
5.4.5
Canceling a service request ............................ 96
5.4.6
Scatter/gather input and output ....................... 96
6
Cryptographic Services ................................ 98
6.1
Cryptographic keys ..........................................98
6.1.1
Scope ...............................................................98
6.1.2
Key storage ..................................................... 98
6.1.3
Key group and key type .................................. 99
6.1.4
Key slot ..........................................................100
6.1.4.1
Key values .....................................................100
6.1.4.2
Key attributes .................................................102
6.1.5
Key catalog ....................................................105
6.1.5.1
ROM key catalog ...........................................105
6.1.5.2
NVM and RAM key catalogs ......................... 106
6.1.5.3
Key catalog formatting ...................................108
6.1.5.4
Empty keys ....................................................108
6.1.6
Key handle .....................................................109
6.2
Key management ...........................................110
6.2.1
Scope .............................................................110
6.2.2
Key catalog formatting ...................................110
6.2.3
Key import ..................................................... 110
6.2.3.1
Scheme ..........................................................111
6.2.3.2
Key selection ................................................. 111
6.2.3.3
Service configuration ..................................... 114
6.2.3.4
Key properties ............................................... 115
6.2.3.5
Key values .....................................................116
6.2.3.6
Importing standard key certificates ................ 121
6.2.3.7
Possible error causes ....................................122
6.2.4
Key export ..................................................... 122
6.2.4.1
Scheme ..........................................................123
6.2.4.2
Key selection ................................................. 123
6.2.4.3
Service configuration ..................................... 123
6.2.4.4
Key properties ............................................... 125
6.2.4.5
Key values .....................................................125
6.2.4.6
Certificate signing request ............................. 126
6.2.4.7
Possible error causes ....................................126
6.2.5
Key generation .............................................. 127
6.2.5.1
Algorithms ......................................................127
6.2.5.2
Key selection ................................................. 128
6.2.5.3
Key properties ............................................... 128
6.2.5.4
Service configuration ..................................... 128
6.2.6
Key derivation ................................................131
6.2.6.1
Key transform algorithms (KDF) .................... 132
6.2.6.2
Key selection ................................................. 133
6.2.6.3
Resulting key ................................................. 134
6.2.7
Key agreement (Diffie-Hellman shared-
secret computation) ....................................... 134
6.2.7.1
Algorithms ......................................................135
6.2.7.2
Key selection ................................................. 136
6.2.7.3
Service configuration ..................................... 136
6.2.7.4
Key properties ............................................... 136
6.2.7.5
Key values .....................................................136
6.2.8
Key erase ...................................................... 136
6.2.8.1
Conditions ......................................................136
6.2.8.2
Erasing one key .............................................137
6.2.8.3
Erasing all keys ............................................. 137
6.2.9
Retrieving key properties ...............................138
6.2.10
Key value verification .....................................138
6.3
Key management: SHE keys .........................138
6.3.1
Scope .............................................................138
6.3.2
Declaring SHE keys .......................................138
6.3.3
Declaring extended SHE keys .......................139
6.3.4
Declaration example ......................................139
6.3.5
SHE key attributes .........................................140
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
294 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 295

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
6.3.5.1
Security flags ................................................. 140
6.3.5.2
Counter .......................................................... 140
6.3.6
SHE key provisioning .................................... 140
6.3.6.1
SHE key update protocol ...............................141
6.3.6.2
SHE key update policies ............................... 144
6.3.7
SHE plain key update ....................................145
6.3.8
SHE key export ............................................. 145
6.3.9
Using SHE keys ............................................ 145
6.4
Cryptographic functions ................................. 145
6.4.1
Generalities ....................................................145
6.4.1.1
Key usage restrictions ................................... 145
6.4.1.2
Cipher block size ...........................................145
6.4.1.3
Useful bits ......................................................146
6.4.1.4
Hash block size ............................................. 146
6.4.1.5
Streaming vs. one-pass mode .......................146
6.4.2
Block ciphering .............................................. 146
6.4.2.1
Algorithms ......................................................146
6.4.2.2
Key selection ................................................. 147
6.4.2.3
Service configuration ..................................... 148
6.4.2.4
Input and output data .................................... 148
6.4.2.5
Service result .................................................149
6.4.3
Hashing ..........................................................149
6.4.3.1
Algorithms ......................................................149
6.4.3.2
Key selection ................................................. 149
6.4.3.3
Service configuration ..................................... 149
6.4.3.4
Input and output data .................................... 149
6.4.3.5
Service result .................................................150
6.4.4
Message compression ...................................150
6.4.4.1
Algorithms ......................................................150
6.4.4.2
Key selection ................................................. 151
6.4.4.3
Service configuration ..................................... 151
6.4.4.4
Input and output data .................................... 151
6.4.4.5
Service result .................................................151
6.4.5
MAC generation and verification ....................151
6.4.5.1
Algorithms ......................................................151
6.4.5.2
Key selection ................................................. 154
6.4.5.3
Service configuration ..................................... 154
6.4.5.4
Input and output data .................................... 155
6.4.5.5
Service result .................................................156
6.4.5.6
Variant: Fast CMAC generation and
verification ......................................................156
6.4.5.7
CMAC with counter ........................................157
6.4.6
Authenticated block ciphering (AEAD) ...........157
6.4.6.1
Algorithms ......................................................157
6.4.6.2
Key selection ................................................. 160
6.4.6.3
Service configuration ..................................... 160
6.4.6.4
Input and output data .................................... 160
6.4.6.5
Service result .................................................161
6.4.7
Signature generation and verification
(RSA / ECC) .................................................. 161
6.4.7.1
Algorithms ......................................................161
6.4.7.2
Key selection ................................................. 165
6.4.7.3
Service configuration ..................................... 166
6.4.7.4
Input and output data .................................... 166
6.4.7.5
Service result .................................................168
6.4.8
RSA ciphering ................................................168
6.4.8.1
Algorithm ........................................................168
6.4.8.2
Key selection ................................................. 169
6.4.8.3
Service configuration ..................................... 169
6.4.8.4
Input and output data .................................... 170
6.4.8.5
Service result .................................................170
6.5
Random number generation ..........................171
6.5.1
Generalities ....................................................171
6.5.2
Implementation .............................................. 171
6.5.3
Service configuration ..................................... 172
6.5.4
Input and output data .................................... 172
6.5.5
Potential error ................................................ 172
7
Secure Boot and Memory Verification
Services ........................................................ 173
7.1
Types of secure boot .....................................173
7.2
Memory Verification Services ........................ 173
7.3
System overview ............................................174
7.4
Principle of operation .....................................174
7.5
System tables ................................................ 175
7.5.1
SMR table ......................................................175
7.5.2
Core Reset table ........................................... 178
7.6
SMR installation .............................................180
7.6.1
SMR installation conditions ............................180
7.6.2
SMR installation attributes .............................180
7.6.3
SMR installation options ................................ 180
7.6.3.1
One-pass installation mode ........................... 180
7.6.3.2
Streaming installation mode .......................... 181
7.6.3.3
Non-reentrant service .................................... 181
7.6.4
Initial SMR authentication ..............................181
7.6.4.1
General use ...................................................181
7.6.4.2
Specific use (SMR #0) ...................................182
7.6.5
SMR installation result ...................................183
7.7
Core Reset table installation ..........................184
7.7.1
CR table entry installation conditions .............184
7.7.2
CR table entry attributes ................................184
7.7.3
CR table entry installation result ....................184
7.7.4
Core Reset table update ............................... 184
7.8
SMR verification .............................................184
7.8.1
Encrypted SMR ............................................. 185
7.8.2
Authenticity proof ...........................................185
7.8.3
Memory region verified ..................................185
7.8.4
On-demand SMR verification .........................185
7.8.4.1
Application and SMR update steps in AB_
SWAP configuration .......................................186
7.8.5
Recurrent automatic SMR verification ........... 191
7.9
SMR Entry erase ...........................................191
7.10
Secure boot and automatic SMR
verification ......................................................191
7.10.1
Pre-boot phase .............................................. 192
7.10.2
Booting phase and core reset release
strategies ....................................................... 192
7.10.3
Post-boot phase ............................................ 193
7.10.4
Sanctions ....................................................... 193
7.10.5
Secure boot flow ............................................195
7.10.6
On-demand secure boot ................................201
7.10.7
Verification status ...........................................204
7.10.8
Validate/Invalidate SMR verification status
(SMR #0) ....................................................... 204
7.10.9
SHE-based secure boot (SMR #0) ................ 204
7.10.10
Memory location ............................................ 205
7.10.11
Recommendations .........................................206
8
Administration Services ..............................207
8.1
Manage HSE system attributes ..................... 207
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
295 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 296

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
8.1.1
Set HSE system attributes .............................207
8.1.2
Retrieve HSE system attributes .....................207
8.1.3
HSE system attributes to configure security
policies ...........................................................207
8.1.3.1
Description .....................................................207
8.1.3.2
Example: MU configuration ............................211
8.2
Authenticate the host system images ............ 212
8.2.1
Authentication ................................................ 212
8.2.2
Verification ..................................................... 213
8.3
Cancel a service request ...............................213
8.4
Retrieve the SHE-UID ................................... 214
8.5
Request for Super User rights .......................214
8.5.1
Initiating the request ...................................... 214
8.5.2
Finalizing the request .................................... 215
8.5.3
Example .........................................................215
8.6
Managing execution streams and related
contexts ..........................................................216
9
Miscellaneous Services .............................. 218
9.1
Monotonic counter services ...........................218
9.1.1
General use ...................................................218
9.1.2
Configure monotonic counters .......................218
9.2
Erase HSE Data Flash .................................. 219
9.3
HSE Flash Memory Integrity ..........................219
9.3.1
Scope .............................................................219
9.3.2
General use ...................................................219
9.4
HSE idle state ................................................219
9.5
MACsec Key Management ............................220
10
Error and Warning Management ................ 221
10.1
Scope .............................................................221
10.2
HSE system events ....................................... 221
10.2.1
HSE shutdown mode .....................................221
10.2.2
Fatal error details .......................................... 221
10.2.2.1
General error ................................................. 221
10.2.2.2
Clock Monitoring Unit .................................... 222
10.2.2.3
Physical Tamper ............................................ 222
10.2.2.4
Code Flash Firmware Integrity Check ............223
10.2.2.5
Firmware Update Error ..................................224
10.2.2.6
Flash ECC error ............................................ 224
10.2.3
Warning Events ............................................. 226
10.2.3.1
Periodic SMR Check Failed ...........................226
10.2.3.2
Backup Firmware Integrity Check ..................226
10.2.3.3
RNG module in HSE is not working ...............226
10.2.3.4
Non-Notifying Error Events ............................227
11
HSE Firmware Update ................................. 228
11.1
Scope .............................................................228
11.2
Service configuration (HSE Firmware
update) ...........................................................228
11.3
HSE Firmware update (AB_SWAP) ...............229
11.4
HSE Firmware update (Full_MEM) ................230
11.5
Application update (AB_SWAP) .....................231
11.6
HSE Firmware header format ........................233
11.7
Secure-BAF update ....................................... 233
11.8
Service description ........................................ 234
12
Security Policies ..........................................236
12.1
Scope .............................................................236
12.2
Key usage ......................................................236
12.3
Key import / update ....................................... 236
12.4
Key export ..................................................... 237
12.5
Memory areas and isolation between hosts ...237
12.6
SMR installation .............................................238
12.7
User/Super User rights ..................................238
12.8
Debug ............................................................ 238
13
Platform Specific Behavioral and
Features ........................................................239
13.1
Scope .............................................................239
13.2
AES ACCEL support ..................................... 239
13.2.1
AES_ACCEL start-up .................................... 239
13.2.2
The Key Handle Translation Table (KHTT) .... 239
13.2.3
KHTT configuration service ........................... 241
13.2.4
Push MSC key(s) service .............................. 241
14
Device Specific Parameters ........................242
14.1
Scope .............................................................242
14.2
System attributes ...........................................242
14.2.1
IVT Start Addresses ...................................... 242
14.2.2
IVT Structure ................................................. 243
14.2.2.1
The Boot Configuration Word (BCW) .............244
14.2.2.2
Clock Frequency Options for Devices ............245
14.2.2.3
The LifeCycle Configuration Word (LCW) ......246
14.2.2.4
Boot Targets .................................................. 247
14.2.2.5
AppBL Structure ............................................ 247
14.3
Recovery mode Start address ....................... 247
14.4
Size of the HSE Firmware .............................248
14.5
Cryptographic services .................................. 248
14.6
Specific parameters (S32K3XX) .................... 249
14.6.1
On-chip secure NVM ..................................... 249
14.6.2
OTP Device configuration ..............................252
14.6.3
XRDC Configuration ...................................... 252
14.6.3.1
Default MDAC configuration .......................... 253
14.6.3.2
Default MRC 0 configuration (FULL_MEM) ... 253
14.6.3.3
Default MRC 0 configuration (AB_SWAP) ..... 254
14.6.3.4
Default configuration of PAC ......................... 255
14.6.4
Status Bits for the HSE Firmware and
Secure BAF ................................................... 256
14.6.4.1
Secure BAF version number ......................... 256
14.6.4.2
HSE_CONFIG_GPR3 ....................................256
14.6.4.3
HSE Secure Memory sizes in HSE GPR
Registers ........................................................258
14.6.4.4
DCM register DCMRWP1 ..............................258
14.6.4.5
DCM register DCMSTAT ................................259
14.6.4.6
HSE Secure Memory sizes in HSE GPR
Registers ........................................................260
14.6.5
Synchronizing flash read/write access
between HSE and application core ................260
14.6.5.1
Usage of Internal Flash by HSE FW
services ..........................................................264
14.6.6
HSE interface ................................................ 270
14.6.7
HSE Firmware Handshake ............................ 270
14.6.8
Integrity checks in SYS-Image locations ........270
14.6.9
Valid output address range (any memory
configuration) ................................................. 271
14.6.10
Super User execution rights .......................... 274
14.6.11
The mapping between SHE commands and
HSE services ................................................. 275
14.6.12
Delay in processing of first heavy operation
after boot ....................................................... 276
14.6.13
HSE Firmware Features disabled in newer
versions ..........................................................276
14.6.14
Debug and UID ..............................................276
RM00286
All information provided in this document is subject to legal disclaimers.
© 2025 NXP B.V. All rights reserved.
Reference manual
Rev. 2.5 — 28 May 2025
COMPANY CONFIDENTIAL
296 / 297
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
# 페이지 297

NXP Semiconductors
RM00286
HSE_B Firmware Reference Manual
14.6.15
Reset ..............................................................277
14.7
HSE Firmware and Secure BAF release
version compatibility ...................................... 277
14.7.1
General guideline applicable for all S32K3
devices ...........................................................280
14.8
Hardware IP registers changed by HSE
during PLL configuration ................................280
15
Revision History .......................................... 282
15.1
Revision History .............................................282
Legal information .........................................287
Please be aware that important notices concerning this document and the product(s)
described herein, have been included in section 'Legal information'.
© 2025 NXP B.V.
All rights reserved.
For more information, please visit: https://www.nxp.com
Date of release: 28 May 2025
Document identifier: RM00286
Provided under NDA only
COMPANY PROPRIETARY
 LG Chem 
 762dac6b-6595-4f84-aab2-f8e933188cd8 


---
