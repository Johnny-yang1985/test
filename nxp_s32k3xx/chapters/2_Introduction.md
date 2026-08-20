# 페이지 9

Chapter 2
Introduction
2.1 Overview
The S32K3xx product series further extends the highly-scalable portfolio of Arm ® Cortex ® - M0+/M4F S32K1xx chips in the 
automotive industry with the Arm Cortex-M7 core at higher frequency, more memory, ASIL-B and D rating and advanced security 
module. With a focus on automotive environment robustness, the S32K3xx product series devices are well suited to a wide range 
of applications in electrical harsh environments, and are optimized for cost-sensitive applications offering new, space saving 
package options. The S32K3xx series offers a broad range of memory, peripherals and performance options. Devices in this 
series share common peripherals and pin-out, allowing developers to migrate easily within a chip series or among other chip series 
to take advantage of more memory or feature integration.
 
S32K389 specific information is preliminary until the device is qualified and may change without notice.
  CAUTION  
2.2 S32K3xx product series
The S32K3xx series comes to market together with easy-to-use enablement software, application specific software, and various 
development tools, supported by broad third parties in different development phases.
The portfolio scalability, future-proof feature like advanced security, as well as software/tool/third-party development support 
allows developers to standardize on the S32K series for their end product platforms, maximizing hardware and software reuse, 
and reducing time-to-market.
Following are the general features of the S32K3xx series chips:
• 32-bit Arm Cortex-M7 core with IEEE-754 compliant SPFPU, executing up to 320 MHz
• Scalable memory footprints up to 12 MB flash memory and up to 2.25 MB SRAM
• Precision mixed-signal capability with low power comparators (LPCMP) and multiple 12-bit ADCs
• Powerful timers for a broad range of applications including motor control, lighting control and body applications
• Serial communication interfaces such as LPUART, LPSPI, LPI2C, FlexCAN with ISOCAN-FD support, Ethernet and 
QuadSPI. FXIO configuration allows other communication options including SENT.
• EVITA full and light functionality compliant HSE_B
• Power supply (3.0 – 5.5 V) with fully functional flash memory program/erase/read operations
• Functional safety compliance with ISO26262 levels B or D (features depend on device specification)
— Lockstep cores
— Multiple internal watchdogs
— Voltage monitors
— Clock monitors
— Memory protection
— Data transport checks
— ECC on memories
— Cyclic redundancy checking
• Ambient operation temperature range: –40°C to 125°C
• Junction temperature range: –40°C to 150°C
• Tools solutions:
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
15 / 5251


---
# 페이지 10

— S32 Design Studio IDE
— NXP GCC compilers for Cortex-M7 and IDE plugins for partner compilers support
— Low cost debugger with multi-core debug, tracing and profiling support
— S32 Configuration Tools:
◦Pin wizard with detailed pin configuration report
◦Graphical clock tree for clock configuration
◦Peripheral configuration
— Model-Based Design Toolbox:
◦Integrated Simulink®-embedded target for direct rapid prototyping and PIL development workflows
◦Peripheral device interface blocks and drivers
◦Target-optimized math and motor control algorithm blocks for efficient execution on the target chip
◦Bit-accurate simulation results in the Simulink® simulation environment
— FreeMaster
• Software solutions:
— RTD (Real Time Drivers)
◦Autosar 4.4 compliant MCAL plus complex device drivers for external ICs (e.g. PMIC) and miscellaneous SW 
components (e.g. inter core communication)
◦Low level drivers covering all device periphery
◦Example projects for each driver
◦Configuration components for Tresos Studio and S32ConfigTools framework
◦Integrated with S32 Design Studio
— Stacks/libraries
◦Communication stacks:
▪LIN, TCP/IP, gPTP, AVB, WiFi, AWS IOT
◦Security:
▪mBedTLS
◦Safety:
▪Safety Software Framework
◦Real time control:
▪AMMCLib
▪ISELED
◦RTOS:
▪FreeRTOS
◦Firmware:
▪Security firmware for on-chip crypto engine
◦Core to core communication:
▪IPCF
◦Edge to cloud connectivity:
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
16 / 5251


---
# 페이지 11

▪AWS IOT
• Designed to work in conjunction with NXP SBC UJA124x and SBC FS2600
2.3 Feature summary
The S32K3xx product family includes the Arm Cortex-M7 core features described in the following table.
Table 4. S32K3xx chip's feature summary
Feature
Inclusions
Core and architecture
• Arm Cortex-M7 core running up to 320 MHz
• Arm core based on the Armv7 architecture and Thumb-2 ISA
• Upto 16 KB data and 16 KB instruction cache for optimizing wait state 
execution from memories
• 96 KB Tightly Coupled Memory associated with each core
• On-core MPU for dynamic task protection (16 regions)
• SPFPU, IEEE 754 compliant
• Harvard bus architecture implementing dedicated instruction and data 
path
• 5-stage pipeline with branch speculation
• XRDC integrated with a crossbar switch to provide memory and 
peripheral protection
• DSP
• I/O protection (VIRT_WRAPPER)
• ETM supporting instruction trace
• Arm third-party ecosystem support: software and tools to help minimize 
development time and cost
DMA
• Up to 2x64-channel DMAMUX
• eDMA with up to 32 channels
• Complex data transfers performed with minimal intervention from a host 
processor
• Programmable support for scatter-gather DMA processing
System and power management
• Support for simplified power modes (Run and Standby)
• Support for clock gating of unused modules; specific peripherals 
continue to work in low-power modes
• Support for external ballast transistor to generate core supply
• Fully independent CPU and peripheral clocking scheme
• Rapid start-up from a 48 MHz FIRC
• Various low-power oscillators such as the 32 kHz SIRC and support for 
an external 32 kHz crystal (SXOSC)
Table continues on the next page...
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
17 / 5251


---
# 페이지 12

Table 4. S32K3xx chip's feature summary (continued)
Feature
Inclusions
• PMC with LVD and selectable trip points
• NMI
Memory and memory interfaces
• Up to 12 MB program flash memory, up to 256 KB data flash memory, 
and up to 2304 KB SRAM, all with an ECC
• 4-bit/8-bit QuadSPI
Clocks
• External 8 MHz–40 MHz crystal oscillator or resonator
• External 32 kHz crystal oscillator
• Internal clock references
— 48 MHz FIRC ±5%
— 32 kHz SIRC ±10%
• Up to 1280 MHz PLL for divided system clock operation
• Auxiliary PLL at up to 1 GHz for additional clocking options (on selected 
devices)
Security and integrity
• Hardware security engine (HSE_B)
— Upgradable Firmware delivered by NXP, to be programmed by the 
user
• Security ciphers:
— Symmetric: AES-128/192/256
— AES_ACCEL: Additional AES Accelerator for low latency AES 
128/256 signature/verify 1
— Cipher modes: ECB, CBC, CMAC, GMAC, CTR, OFB, CCM, and 
GCM
— Asymmetric: RSA (up to 4096 bits) and ECC (up to 521 bits)
— Hash: Miyaguchi-Preneel, SHA-2/SHA-3 (up to 512 bits)
— Number of keys is configurable and controlled by HSE FW
— Random number generator
• Security use case supported:
— Secure boot
— Secure communication
— Component protection
— Secure storage
— Key exchange
Safety ISO26262
• Classification up to ASIL-D
• ERM and EIM support
Table continues on the next page...
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
18 / 5251


---
# 페이지 13

Table 4. S32K3xx chip's feature summary (continued)
Feature
Inclusions
• WDOG with an independent clock source
• Voltage monitors
• Bandgap voltage available as ADC input
• External clock source monitoring using an independent reference
• PLL lock and loss-of-lock protection
• XRDC
• ECC on code flash memory, data flash memory, and system RAM
• ADC self-test feature
• Internal analog monitoring of all supplies available
• CRC generation module
• FCCU failure output
Analog
• 12-bit ADC
— Up to 72 external analog inputs
— 1 μs conversion time
— Internal bandgap voltage reference channel, supporting automatic 
compare and an optional hardware trigger
— Up to five internal reference inputs
— Automatic compare with interrupt
— Self-test and self-calibration scheme
• LPCMP with an internal 8-bit DAC as a reference
— Low power analog comparator with both positive and negative 
inputs, separately selectable interrupts on rising and falling 
comparator output
— Ability to cross trigger the timers from both the ADC and LPCMP 
outputs
• Temperature Sensor (TempSense) with output measurable by ADC.
Timers
• 16-bit or 24-bit eMIOS timers, offering up to 72 standard channels
— Input capture, output compare, and PWM modes
— Fault input support with global fault control
— Multiple features such as deadtime insertion, configurable polarity, 
quadrature decoding, and so on
• 32-bit PITs, with four channels, for raising interrupts and triggering DMA 
channels
• 32-bit RTC
Table continues on the next page...
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
19 / 5251


---
# 페이지 14

Table 4. S32K3xx chip's feature summary (continued)
Feature
Inclusions
• Motor control and power conversion using combination of eMIOS, LCU , 
BCTU, and ADC
• Up to four STMs, with four channels each
Communications
• LPSPI supporting DMA with full-duplex or single-wire bidirectional 
communication in Master or Slave mode
• FlexIO, with an option to configure it as different communication 
peripherals, offering support for SENT
• LPI2C modules with DMA support, low-power availability, master or 
slave support, and system management bus
• LPUART with DMA support, having an optional 13-bit break, full-duplex 
non-return- to-zero (NRZ), low-power availability and supports LIN 
protocol versions 1.3, 2.0, 2.1, 2.2A, and SAE J2602 with using SW 
LIN driver
• FlexCAN modules with ISOCAN-FD and DMA support
• SAI capable of supporting stereo audio channels
• uSDHC interface to interface with SD/SDIO/MMC cards.
• EMAC complex (10/100 Ethernet) that supports 1588 timers, MII/RMII 
interface, AVB, and TSN support
• GMAC (Gigabit Ethernet) with support for AVB (3.3 V only for RGMII) 
and Time Sensitive Networking (TSN) capability
Debug
• DWT, with four configurable comparators as hardware watchpoints
• SWO-synchronous trace data support
• ITM with software and hardware trace, plus time stamping
• FPB with an ability to patch code and data from code space to system 
space
• Trace of all execution units and bus masters made available through 
an Arm TPIU over GPIO pins; a very low bandwidth trace option also 
available via the SWO
• Embedded trace FIFO (ETF)—a dedicated trace buffer available for 
each of the core masters, allowing data to be captured internally before 
being optionally routed to external trace pins
• SWV—trace capability providing displays of reads, writes, exceptions, 
PC samples, and print
I/O and package
• Up to 320 GPIO pins
• Up to 144 GPIO pins with interrupt functionality
• Up to 60 GPIO pins with wakeup capability
• Pseudo open drain support on LPUART, FlexIO, LPI2C
Table continues on the next page...
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
20 / 5251


---
# 페이지 15

Table 4. S32K3xx chip's feature summary (continued)
Feature
Inclusions
• Package options of 289 MAPBGA, 257 MAPBGA, 172 HDQFP, 100 
HDQFP, 172 HDQFP-EP, 48 LQFP, and 437 MAPBGA
1. Available only in S32K388 and S32K389
2.4 Block diagram
The following figures depict the block diagrams of S32K3xx family devices.
CM7_0
MPU
FPU
DSP
NVIC
I-TCM
32KB
64-bit
D-TCM
32KB
32-bit
32-bit
AHBS
32-bit
AXI
64-bit
AHBP
32-bit
I- CACHE
D- CACHE
8KB
8KB
XHB400
Primary core
D-TCM
32KB
cm70_ahbs
* ECC data and address encode
AIPS1
AIPS0
PRAM0
64 - bit + ECC*
x72
SRAM0
16 KB
PAC0
M0
M3
M2
S3
S2
S5
S4
P0
PAC1
PFLASH
64
-
bit + ECC
x256
D-Flash
64KB
S1
S0
P0
P1
MRC0
eDMA3
12ch
MDAC1
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
AHB
64b
HSE-B
AHB
64b
WDATA 
GEN
RDATA 
CHECK
MDAC3
2:1
M1
XBIC
Trigger Multiplexing Control
Body Cross Triggering Unit
eMIOS_0
eMIOS_1
Logic Control Unit 0
Logic Control Unit 1
Analog-to-digital converter 0
Analog-to-digital converter 1
Programmable Interrupt Timer 0
Programmable Interrupt Timer 1
Crossbar Integrity Checker (System AXBS / AXBS Lite)
eDMA control & status (MP_CSR; MP_ES; MP_HRS)
eDMA transfer control descriptor 0
eDMA transfer control descriptor 1
eDMA transfer control descriptor 2
eDMA transfer control descriptor 3
eDMA transfer control descriptor 4
eDMA transfer control descriptor 5
eDMA transfer control descriptor 6
eDMA transfer control descriptor 7
eDMA transfer control descriptor 8
eDMA transfer control descriptor 9
eDMA transfer control descriptor 10
eDMA transfer control descriptor 11
Debug APB Page0
Debug APB Page1
Debug APB Page2
Debug APB Page3
Debug APB Paged Area
SDA-AP
EIM_0
ERM_0
MSCM
RAM controller 0
Flash controller
Flash controller alternate
Software Watchdog 0
System Timer Module 0
XRDC
Interrupt Monitor
DMA Channel Multiplexer 0
DMA Channel Multiplexer 1
Real-time clock
Reset Generation Module
SIUL2_VIRTWRAPPER_PDAC0
SIUL2_VIRTWRAPPER_PDAC0
SIUL2_VIRTWRAPPER_PDAC1
SIUL2_VIRTWRAPPER_PDAC1
SIUL2_VIRTWRAPPER_PDAC3
System Status and Configuration Module
Wakeup Unit
CMU 0-5
Touch Sensing Coupling Controller
32 kHz Slow Internal RC Oscillator
48 MHz Fast Internal RC Oscillator
8-40 MHz Fast External Crystal Oscillator
Clock Generation Module
Mode Entry Module
Frequency Modulated Phase-Locked Loop
Power management controller
Flash memory
Flash memory alternate
FlexCAN_0
FlexCAN_1
FlexCAN_2
Flexible IO
Low Power UART 0
Low Power UART 1
Low Power UART 2
Low Power UART 3
Low Power UART 0
Low Power UART 1
Low Power UART 2
Low Power UART 3
Low Power I2C 0
Low Power I2C 1
Low Power SPI 0
Low Power SPI 1
Low Power SPI 2
Low Power SPI 3
Low Power Comparator 0
TMU Temperature Sensor Unit
CRC
FCCU (+FOSU)
MU_0_MUB
MU_1_MUB
JDC (JTAG Data Communication)
Configuration GPR
Self-Test Control Unit
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
1:1 64:32
cm70_ahbs
MRC1
C-
C-C-
C- Flash
512KB
C-
C-C-
C- Flash
512KB
1:1
Up to 30 MHz
No programming model, preset to Round-robin arbitration scheme with slaves parked on masters performing last accesses.  
PFLASH Port  
Master Assignment
P0
P1
CM7_0
HSE & Others
AHB32
APB v3
AXI64
IPBUS
AHB64
AHB64 (optional 
based on split-lock)
On-platform
Off-platform
ECC gaskets
Configurable gaskets
Fixed gaskets
Up to 120MHz
AXBS  
(64-bit)
AHB_32_64
MDAC0
ADDR
GEN
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
ADDR 
CHECK
RDATA 
GEN
ADDR 
CHECK
RDATA 
GEN
16 KB
Part Number
Lockstep
Lockstep
Decoupled
Decoupled
Decoupled
Disabled
S32K310
S32K311
N/A
N/A
CM7_0
N/A
Program flash (Block 1)
16 KB of SRAM
N/A
N/A
N/A
N/A
N/A
N/A
CM7_0
Figure 5. Block diagram – S32K311 and S32K310
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
21 / 5251


---
# 페이지 16

CM7_0
MPU
FPU
DSP
NVIC
I-TCM
32KB
64-bit
D-TCM
32KB
32-bit
32-bit
AHBS
32-bit
AXI
64-bit
AHBP
32-bit
I- CACHE
D- CACHE
8KB
8KB
XHB400
Primary core
D-TCM
32KB
cm70_ahbs
* ECC data and address encode
AIPS1
AIPS0
PRAM0
64 - bit + ECC*
x72
SRAM0
96 KB
PAC0
M0
M3
M2
S3
S2
S5
S4
P0
PAC1
PFLASH
64
-
bit + ECC
x256
D-Flash
128KB
S1
S0
P0
P1
MRC0
eDMA3
12ch
MDAC1
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
AHB
64b
HSE-B
AHB
64b
WDATA 
GEN
RDATA 
CHECK
MDAC3
2:1
M1
XBIC
Trigger Multiplexing Control
Body Cross Triggering Unit
eMIOS_0
eMIOS_1
Logic Control Unit 0
Logic Control Unit 1
Analog-to-digital converter 0
Analog-to-digital converter 1
Programmable Interrupt Timer 0
Programmable Interrupt Timer 1
Crossbar Integrity Checker (System AXBS / AXBS Lite)
eDMA control & status (MP_CSR; MP_ES; MP_HRS)
eDMA transfer control descriptor 0
eDMA transfer control descriptor 1
eDMA transfer control descriptor 2
eDMA transfer control descriptor 3
eDMA transfer control descriptor 4
eDMA transfer control descriptor 5
eDMA transfer control descriptor 6
eDMA transfer control descriptor 7
eDMA transfer control descriptor 8
eDMA transfer control descriptor 9
eDMA transfer control descriptor 10
eDMA transfer control descriptor 11
Debug APB Page0
Debug APB Page1
Debug APB Page2
Debug APB Page3
Debug APB Paged Area
SDA-AP
EIM_0
ERM_0
MSCM
RAM controller 0
Flash controller
Flash controller alternate
Software Watchdog 0
System Timer Module 0
XRDC
Interrupt Monitor
DMA Channel Multiplexer 0
DMA Channel Multiplexer 1
Real-time clock
Reset Generation Module
SIUL2_VIRTWRAPPER_PDAC0
SIUL2_VIRTWRAPPER_PDAC0
SIUL2_VIRTWRAPPER_PDAC1
SIUL2_VIRTWRAPPER_PDAC1
SIUL2_VIRTWRAPPER_PDAC3
System Status and Configuration Module
Wakeup Unit
CMU 0-5
Touch Sensing Coupling Controller
32 kHz Slow Internal RC Oscillator
32 kHz Slow External Crystal Oscillator
48 MHz Fast Internal RC Oscillator
8-40 MHz Fast External Crystal Oscillator
Clock Generation Module
Mode Entry Module
Frequency Modulated Phase-Locked Loop
Power management controller
Flash memory
Flash memory alternate
FlexCAN_0
FlexCAN_1
FlexCAN_2
FlexCAN_3
FlexCAN_4
FlexCAN_5
Flexible IO
Low Power UART 0
Low Power UART 1
Low Power UART 2
Low Power UART 3
Low Power UART 4
Low Power UART 5
Low Power UART 6
Low Power UART 7
Low Power I2C 0
Low Power I2C 1
Low Power SPI 0
Low Power SPI 1
Low Power SPI 2
Low Power SPI 3
Low Power Comparator 0
Low Power Comparator 1
TMU Temperature Sensor Unit
CRC
FCCU (+FOSU)
MU_0_MUB
MU_1_MUB
JDC (JTAG Data Communication)
Configuration GPR
Self-Test Control Unit
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
1:1 64:32
cm70_ahbs
MRC1
C-
C-C-
C- Flash
1MB
C-
C-C-
C- Flash
1MB
1:1
Up to 30 MHz
No programming model, preset to Round-robin arbitration scheme with slaves parked on masters performing last accesses.  
PFLASH Port  
Master Assignment
P0
P1
CM7_0
HSE & Others
AHB32
APB v3
AXI64
IPBUS
AHB64
AHB64 (optional 
based on split-lock)
On-platform
Off-platform
ECC gaskets
Configurable gaskets
Fixed gaskets
Up to 120MHz
AXBS  
(64-bit)
AHB_32_64
MDAC0
ADDR
GEN
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
ADDR 
CHECK
RDATA 
GEN
ADDR 
CHECK
RDATA 
GEN
Part Number
Lockstep
Lockstep
Decoupled
Decoupled
Decoupled
Disabled
S32K312
N/A
N/A
CM7_0
N/A
N/A
N/A
Figure 6. Block diagram – S32K312
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
22 / 5251


---
# 페이지 17

CM7_0
MPU
FPU
DSP
NVIC
I-TCM
32KB
64-bit
64-bit
32-bit
D-TCM
32KB
32-bit
32-bit
32-bit
1
Decoupled =0
Lockstep = 1
0
1
0
1
0
1
Decoupled =0
Lockstep = 1
0
1
0
1
0
+
+
+
CM7_1
MPU
FPU
DSP
NVIC
32KB
D-TCM
32KB
D-TCM
32KB
AHBS
32-bit
AXI
64-bit
AHBP
32-bit
AHBS
32-bit
AXI
64-bit
AHBP
32-bit
I- CACHE
D- CACHE
I- CACHE
D- CACHE
8KB
8KB
8KB
8KB
Split-Lock Capable
Secondary  
(checker  
or split) core
XHB400
Primary core
D-TCM
32KB
I-TCM
MDAC0
cm70_ahbs
XHB400
ADDR
GEN
MDAC4
cm71_ahbs
* ECC data and address encode
AIPS1
AIPS0
PRAM0
64 - bit + ECC*
x72
SRAM0
64 KB
PAC0
M0
M0
M2
M1
M3
S3
S2
S1
S2
S0
P0
PAC1
AIPS2
PFLASH
64 - bit + ECC
x256
D-Flash
128KB
S1
S4
S0
P0
P2
P1
MRC0
ADDR 
CHECK
RDATA 
GEN
ADDR 
CHECK
RDATA 
GEN
ADDR 
CHECK
RDATA 
GEN
eDMA3
32ch
MDAC1
AXBS_Lite
S0
S1
M0
XBIC
ADDR
CHECK
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
1:1
ADDR
CHECK
ADDR
GEN
Bypass
AXBS_Lite
S0
S1
M0
AHB
64b
HSE
AHB
64b
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
1:2
MDAC3
M0
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
AXBS  
(64-bit)
AXBS_Lite
(64-bit)
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
2:1
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
2:1
M4
M1
M2
AHB splitter
XBIC
System AXBS  XBIC
Peripheral AXBS  XBIC
Trigger Multiplexing Control
Body Cross Triggering Unit
eMIOS_0
eMIOS_1
eMIOS_2
Logic Control Unit 0
Logic Control Unit 1
Analog-to-digital converter 0
Analog-to-digital converter 1
Analog-to-digital converter 2
Programmable Interrupt Timer 0
Programmable Interrupt Timer 1
MU_2_MUA
MU_2_MUB
PAC2
System crossbar switch
Crossbar Integrity Checker (System AXBS / AXBS Lite)
Crossbar Integrity Checker (Peripheral AXBS-Lite)
eDMA control & status (MP_CSR; MP_ES; MP_HRS)
eDMA transfer control descriptor 0
eDMA transfer control descriptor 1
eDMA transfer control descriptor 2
eDMA transfer control descriptor 3
eDMA transfer control descriptor 4
eDMA transfer control descriptor 5
eDMA transfer control descriptor 6
eDMA transfer control descriptor 7
eDMA transfer control descriptor 8
eDMA transfer control descriptor 9
eDMA transfer control descriptor 10
eDMA transfer control descriptor 11
Debug APB Page0
Debug APB Page1
Debug APB Page2
Debug APB Page3
Debug APB Paged Area
SDA-AP
EIM_0
ERM_0
MSCM
RAM controller 0
Flash controller
Flash controller alternate
Software Watchdog 0
System Timer Module 0
XRDC
Interrupt Monitor
DMA Channel Multiplexer 0
DMA Channel Multiplexer 1
Real-time clock
Reset Generation Module
SIUL2_VIRTWRAPPER_PDAC0
SIUL2_VIRTWRAPPER_PDAC0
SIUL2_VIRTWRAPPER_PDAC1
SIUL2_VIRTWRAPPER_PDAC1
SIUL2_VIRTWRAPPER_PDAC2
SIUL2_VIRTWRAPPER_PDAC2
SIUL2_VIRTWRAPPER_PDAC3
System Status and Configuration Module
Wakeup Unit
CMU 0-5
Touch Sensing Coupling Controller
32 kHz Slow Internal RC Oscillator
32 kHz Slow External Crystal Oscillator
48 MHz Fast Internal RC Oscillator
8-40 MHz Fast External Crystal Oscillator
Clock Generation Module
Mode Entry Module
Frequency Modulated Phase-Locked Loop
Power management controller
Flash memory
Flash memory alternate
Programmable Interrupt Timer 2
FlexCAN_0
FlexCAN_1
FlexCAN_2
FlexCAN_3
FlexCAN_4
FlexCAN_5
Flexible IO
Low Power UART 0
Low Power UART 1
Low Power UART 2
Low Power UART 3
Low Power UART 4
Low Power UART 5
Low Power UART 6
Low Power UART 7
Low Power I2C 0
Low Power I2C 1
Low Power SPI 0
Low Power SPI 1
Low Power SPI 2
Low Power SPI 3
Synchronous Audio Interface 0
Low Power Comparator 0
Low Power Comparator 1
TMU Temperature Sensor Unit
CRC
FCCU (+FOSU)
MU_0_MUB
JDC (JTAG Data Communication)
Configuration GPR
Self-Test Control Unit
Selftest GPR
Crossbar Integrity Checker (TCM backdoor AHB Splitter)
Crossbar Integrity Checker (eDMA & STAM AXBS-Lite)
eDMA transfer control descriptor 12
eDMA transfer control descriptor 13
eDMA transfer control descriptor 14
eDMA transfer control descriptor 15
eDMA transfer control descriptor 16
eDMA transfer control descriptor 17
eDMA transfer control descriptor 18
eDMA transfer control descriptor 19
eDMA transfer control descriptor 20
eDMA transfer control descriptor 21
eDMA transfer control descriptor 22
eDMA transfer control descriptor 23
eDMA transfer control descriptor 24
eDMA transfer control descriptor 25
eDMA transfer control descriptor 26
eDMA transfer control descriptor 27
eDMA transfer control descriptor 28
eDMA transfer control descriptor 29
eDMA transfer control descriptor 30
eDMA transfer control descriptor 31
Semaphores2
RAM controller 1
Software Watchdog 1
System Timer Module 1
EMAC
Low Power UART 8
Low Power UART 9
Low Power UART 10
Low Power UART 11
Low Power UART 12
Low Power UART 13
Low Power UART 14
Low Power UART 15
Low Power SPI 4
Low Power SPI 5
QuadSPI
Synchronous Audio Interface 1
Low Power Comparator 2
MU_1_MUB
EIM_3
AHB_32_64
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
AHB_32_64
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
1:1 64:32
PFLASH Port  
Master Assignment
P0
P1
P2
CM7_0
HSE & Others
CM7_1
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
S0
S1
cm70_ahbs
cm71_ahbs
ADDR 
GEN
ADDR 
CHECK
MRC1
RDATA 
GEN
WDATA 
CHECK
RDATA 
CHK
WDATA 
GEN
AXBS_Lite
(32-bit)
QSPI AHB 
Data & 
Code
S5
MRC2
ADDR 
CHECK
WDATA 
CHECK
RDATA 
GEN
2:1
MDAC5
RDATA 
CHECK
WDATA
GEN
1:2 32:64
ENET
ADDR
GEN
AHB
32b
M3
Part Number
Lockstep
Lockstep
Decoupled
Decoupled
Decoupled
Disabled
S32K322
S32K341
S32K342
N/A
N/A
CM7_0
CM7_1
N/A
CM7_0-CM7_1
N/A
N/A
N/A
Program flash (Block 1)
CM7_0-CM7_1
N/A
N/A
N/A
N/A
N/A
N/A
C-
C-C-
C- Flash
1MB
C-
C-C-
C- Flash
1MB
AHB32
APB v3
AXI64
IPBUS
AHB64
AHB64 (optional 
based on split-lock)
On-platform
Off-platform
ECC gaskets
Configurable gaskets
Fixed gaskets
Up to 160MHz
Up to 32 MHz
Up to 80MHz
Up to 80MHz
Up to 80MHz
N/A
Figure 7. Block diagram – S32K322, S32K342 and S32K341
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
23 / 5251


---
# 페이지 18

Up to 160MHz
Up to 32 MHz
Up to 80MHz
Up to 80MHz
Up to 80MHz
CM7_0
MPU
FPU
DSP
NVIC
I-TCM
32KB
64-bit
64-bit
32-bit
D-TCM
32KB
32-bit
32-bit
32-bit
1
Decoupled =0
Lockstep = 1
0
1
0
1
0
1
Decoupled =0
Lockstep = 1
0
1
0
1
0
+
+
+
CM7_1
MPU
FPU
DSP
NVIC
32KB
D-TCM
32KB
D-TCM
32KB
AHBS
32-bit
AXI
64-bit
AHBP
32-bit
AHBS
32-bit
AXI
64-bit
AHBP
32-bit
I- CACHE
D- CACHE
I- CACHE
D- CACHE
8KB
8KB
8KB
8KB
Split-Lock Capable
Secondary  
(checker  
or split) core
XHB400
Primary core
D-TCM
32KB
I-TCM
MDAC0
cm70_ahbs
XHB400
ADDR
GEN
MDAC4
cm71_ahbs
* ECC data and address encode
AIPS0
PRAM0
64 - bit + ECC*
x72
SRAM0
160 KB
PRAM1
64 - bit + ECC*
x72
SRAM1
160KB
PAC0
M0
M0
M2
M1
M3
S3
S6
S2
S1
S2
S0
P0
P0
AIPS1
PAC1
QSPI AHB 
Data & 
Code
S5
MRC2
ADDR 
CHECK
AIPS2
WDATA 
CHECK
RDATA 
GEN
C-
C-C-
C- Flash
1MB
PFLASH
64 - bit + ECC
x256
D-Flash
128KB
S1
S4
S0
P0
P2
P1
MRC0
C-
C-C-
C- Flash
1MB
C-
C-C-
C- Flash
1MB
C-
C-C-
C- Flash
1MB
ADDR 
CHECK
RDATA 
GEN
ADDR 
CHECK
RDATA 
GEN
ADDR 
CHECK
RDATA 
GEN
MDAC5
RDATA 
CHECK
WDATA
GEN
1:2 32:64
ENET
ADDR
GEN
eDMA3
32ch
MDAC1
AXBS_Lite
S0
S1
M0
XBIC
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
1:1
Bypass
AXBS_Lite
S0
S1
M0
AHB
64b
AHB
32b
HSE
AHB
64b
1:2
MDAC3
M0
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
AXBS  
(64-bit)
AXBS_Lite
(64-bit)
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
2:1
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
2:1
M4
M3
M1
M2
AHB splitter
XBIC
System AXBS  XBIC
Peripheral AXBS  XBIC
Trigger Multiplexing Control
Body Cross Triggering Unit
eMIOS_0
eMIOS_1
eMIOS_2
Logic Control Unit 0
Logic Control Unit 1
Analog-to-digital converter 0
Analog-to-digital converter 1
Analog-to-digital converter 2
Programmable Interrupt Timer 0
Programmable Interrupt Timer 1
MU_2_MUA
MU_2_MUB
PAC2
System crossbar switch
Crossbar Integrity Checker (System AXBS / AXBS Lite)
Crossbar Integrity Checker (Peripheral AXBS-Lite)
eDMA control & status (MP_CSR; MP_ES; MP_HRS)
eDMA transfer control descriptor 0
eDMA transfer control descriptor 1
eDMA transfer control descriptor 2
eDMA transfer control descriptor 3
eDMA transfer control descriptor 4
eDMA transfer control descriptor 5
eDMA transfer control descriptor 6
eDMA transfer control descriptor 7
eDMA transfer control descriptor 8
eDMA transfer control descriptor 9
eDMA transfer control descriptor 10
eDMA transfer control descriptor 11
Debug APB Page0
Debug APB Page1
Debug APB Page2
Debug APB Page3
Debug APB Paged Area
SDA-AP
EIM_0
ERM_0
MSCM
RAM controller 0
Flash controller
Flash controller alternate
Software Watchdog 0
System Timer Module 0
XRDC
Interrupt Monitor
DMA Channel Multiplexer 0
DMA Channel Multiplexer 1
Real-time clock
Reset Generation Module
SIUL2_VIRTWRAPPER_PDAC0
SIUL2_VIRTWRAPPER_PDAC0
SIUL2_VIRTWRAPPER_PDAC1
SIUL2_VIRTWRAPPER_PDAC1
SIUL2_VIRTWRAPPER_PDAC2
SIUL2_VIRTWRAPPER_PDAC2
SIUL2_VIRTWRAPPER_PDAC3
System Status and Configuration Module
Wakeup Unit
CMU 0-5
Touch Sensing Coupling Controller
32 kHz Slow Internal RC Oscillator
32 kHz Slow External Crystal Oscillator
48 MHz Fast Internal RC Oscillator
8-40 MHz Fast External Crystal Oscillator
Clock Generation Module
Mode Entry Module
Frequency Modulated Phase-Locked Loop
Power management controller
Flash memory
Flash memory alternate
Programmable Interrupt Timer 2
FlexCAN_0
FlexCAN_1
FlexCAN_2
FlexCAN_3
FlexCAN_4
FlexCAN_5
Flexible IO
Low Power UART 0
Low Power UART 1
Low Power UART 2
Low Power UART 3
Low Power UART 4
Low Power UART 5
Low Power UART 6
Low Power UART 7
Low Power I2C 0
Low Power I2C 1
Low Power SPI 0
Low Power SPI 1
Low Power SPI 2
Low Power SPI 3
Synchronous Audio Interface 0
Low Power Comparator 0
Low Power Comparator 1
TMU Temperature Sensor Unit
CRC
FCCU (+FOSU)
MU_0_MUB
JDC (JTAG Data Communication)
Configuration GPR
Self-Test Control Unit
Selftest GPR
Crossbar Integrity Checker (TCM backdoor AHB Splitter)
Crossbar Integrity Checker (eDMA & STAM AXBS-Lite)
eDMA transfer control descriptor 12
eDMA transfer control descriptor 13
eDMA transfer control descriptor 14
eDMA transfer control descriptor 15
eDMA transfer control descriptor 16
eDMA transfer control descriptor 17
eDMA transfer control descriptor 18
eDMA transfer control descriptor 19
eDMA transfer control descriptor 20
eDMA transfer control descriptor 21
eDMA transfer control descriptor 22
eDMA transfer control descriptor 23
eDMA transfer control descriptor 24
eDMA transfer control descriptor 25
eDMA transfer control descriptor 26
eDMA transfer control descriptor 27
eDMA transfer control descriptor 28
eDMA transfer control descriptor 29
eDMA transfer control descriptor 30
eDMA transfer control descriptor 31
Semaphores2
RAM controller 1
Software Watchdog 1
System Timer Module 1
EMAC
Low Power UART 8
Low Power UART 9
Low Power UART 10
Low Power UART 11
Low Power UART 12
Low Power UART 13
Low Power UART 14
Low Power UART 15
Low Power SPI 4
Low Power SPI 5
QuadSPI
Synchronous Audio Interface 1
Low Power Comparator 2
MU_1_MUB
EIM_3
AHB_32_64
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
AHB_32_64
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
1:1 64:32
PFLASH Port  
Master Assignment
P0
P1
P2
CM7_0
HSE & Others
CM7_1
Part Number
Lockstep
Lockstep
Decoupled
Decoupled
Decoupled
Disabled
S32K314
S32K344
S32K324
N/A
N/A
CM7_0
N/A
CM7_1
CM7_0-CM7_1
N/A
N/A
N/A
N/A
N/A
N/A
N/A
CM7_0
CM7_1
N/A
N/A
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
S0
S1
cm70_ahbs
cm71_ahbs
ADDR 
GEN
ADDR 
CHECK
MRC1
RDATA 
GEN
WDATA 
CHECK
RDATA 
CHK
WDATA 
GEN
AXBS_Lite
(32-bit)
2:1
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
AHB32
APB v3
AXI64
IPBUS
AHB64
AHB64 (optional 
based on split-lock)
On-platform
Off-platform
ECC gaskets
Configurable gaskets
Fixed gaskets
N/A
Figure 8. Block diagram – S32K324, S32K344 and S32K314
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
24 / 5251


---
# 페이지 19

CM7_0
MPU
FPU
DSP
NVIC
I-TCM
32KB
64-bit
64-bit
32-bit
D-TCM
32KB
32-bit
32-bit
32-bit
1
Decoupled =0
Lockstep = 1
0
1
0
1
0
1
Decoupled =0
Lockstep = 1
0
1
0
1
0
+
+
+
CM7_1
MPU
FPU
DSP
NVIC
32KB
D-TCM
32KB
D-TCM
32KB
AHBS
32-bit
AXI
64-bit
AHBP
32-bit
AHBS
32-bit
AXI
64-bit
AHBP
32-bit
I- CACHE
D- CACHE
I- CACHE
D- CACHE
16KB
16KB
16KB
16KB
Split-Lock Capable
Secondary  
(checker  
or split) core
XHB400
Primary core
D-TCM
32KB
I-TCM
CM7_2
16KB
16KB
I-TCM
64KB
64-bit
D-TCM
64KB
D-TCM
64KB
32-bit
32-bit
D- CACHE
I- CACHE
MDAC0
cm70_ahbs
XHB400
ADDR
GEN
MDAC4
cm71_ahbs
MDAC6
cm72_ahbs
XHB400
* ECC data and address encode
AIPS1
AIPS0
PRAM0
64 - bit + ECC*
x72
SRAM0
256 KB
PRAM1
64 - bit + ECC*
x72
SRAM1
256 KB
PAC0
M0
M0
M2
M4
M1
M3
S3
S6
S2
S1
S2
S0
P0
P0
PAC1
QSPI AHB 
Data & 
Code
S5
MRC2
ADDR 
CHECK
2:1
AIPS2
WDATA 
CHECK
RDATA 
GEN
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
C-
C-C-
C- Flash
2 MB
PFLASH
64 - bit + ECC
x256
D-Flash
128KB
S1
S4
S0
P0
P2
P1
P3
S7
MRC0
C-
C-C-
C- Flash
2 MB
C-
C-C-
C- Flash
2 MB
C-
C-C-
C- Flash
2 MB
ADDR 
CHECK
RDATA 
GEN
ADDR 
CHECK
RDATA 
GEN
ADDR 
CHECK
RDATA 
GEN
ADDR 
CHECK
RDATA 
GEN
MDAC5
RDATA 
CHECK
WDATA
GEN
1:1
GMAC
ADDR
GEN
eDMA3
32ch
MDAC1
AXBS_Lite
S0
S1
M0
XBIC
ADDR
CHECK
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
1:1
ADDR
CHECK
ADDR
GEN
1:1
AXBS_Lite
S0
S1
M0
AHB
64b
AHB
64b
HSE
AHB
64b
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
1:2
MDAC3
1:1 64:32
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
1:1 64:32
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
1:1 64:32
S0
S1
M0
S2
S3
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
MRC1
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
MRC3
AXBS  
(64-bit)
AXBS_Lite
(64-bit)
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
1:1
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
2:1
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
2:1
cm70_ahbs
cm71_ahbs
cm72_ahbs
M4
M5
M3
M6
M1
M2
MPU
FPU
DSP
NVIC
Secondary core
AHBS
32-bit
AXI
64-bit
AHBP
32-bit
AHB splitter
XBIC
System AXBS  XBIC
Peripheral AXBS  XBIC
MDAC7
uSDHC
AHB
32b
AXBS_Lite
(64-bit)
ERM_1
Trigger Multiplexing Control
Body Cross Triggering Unit
eMIOS_0
eMIOS_1
eMIOS_2
Logic Control Unit 0
Logic Control Unit 1
Analog-to-digital converter 0
Analog-to-digital converter 1
Analog-to-digital converter 2
Programmable Interrupt Timer 0
Programmable Interrupt Timer 1
MU_2_MUA
MU_2_MUB
PAC2
System crossbar switch
Crossbar Integrity Checker (System AXBS / AXBS Lite)
Crossbar Integrity Checker (Peripheral AXBS-Lite)
eDMA control & status (MP_CSR; MP_ES; MP_HRS)
eDMA transfer control descriptor 0
eDMA transfer control descriptor 1
eDMA transfer control descriptor 2
eDMA transfer control descriptor 3
eDMA transfer control descriptor 4
eDMA transfer control descriptor 5
eDMA transfer control descriptor 6
eDMA transfer control descriptor 7
eDMA transfer control descriptor 8
eDMA transfer control descriptor 9
eDMA transfer control descriptor 10
eDMA transfer control descriptor 11
Debug APB Page0
Debug APB Page1
Debug APB Page2
Debug APB Page3
Debug APB Paged Area
SDA-AP
ERM_0
MSCM
RAM controller 0
Flash controller
Flash controller alternate
Software Watchdog 0
System Timer Module 0
XRDC
Interrupt Monitor
DMA Channel Multiplexer 0
DMA Channel Multiplexer 1
Real-time clock
Reset Generation Module
SIUL2_VIRTWRAPPER_PDAC0
SIUL2_VIRTWRAPPER_PDAC0
SIUL2_VIRTWRAPPER_PDAC1
SIUL2_VIRTWRAPPER_PDAC1
SIUL2_VIRTWRAPPER_PDAC2
SIUL2_VIRTWRAPPER_PDAC2
SIUL2_VIRTWRAPPER_PDAC3
System Status and Configuration Module
Wakeup Unit
CMU 0-5
Touch Sensing Coupling Controller
32 kHz Slow Internal RC Oscillator
32 kHz Slow External Crystal Oscillator
48 MHz Fast Internal RC Oscillator
8-40 MHz Fast External Crystal Oscillator
Clock Generation Module
Mode Entry Module
Frequency Modulated Phase-Locked Loop
Frequency Modulated Phase-Locked Loop 2
Power management controller
Flash memory
Flash memory alternate
SIUL2_VIRTWRAPPER_PDAC4
SIUL2_VIRTWRAPPER_PDAC4
Programmable Interrupt Timer 2
FlexCAN_0
FlexCAN_1
FlexCAN_2
FlexCAN_3
FlexCAN_4
FlexCAN_5
FlexCAN_6
FlexCAN_7
Flexible IO
Low Power UART 0
Low Power UART 1
Low Power UART 2
Low Power UART 3
Low Power UART 4
Low Power UART 5
Low Power UART 6
Low Power UART 7
Low Power I2C 0
Low Power I2C 1
Low Power SPI 0
Low Power SPI 1
Low Power SPI 2
Low Power SPI 3
Synchronous Audio Interface 0
Low Power Comparator 0
Low Power Comparator 1
TMU Temperature Sensor Unit
CRC
FCCU (+FOSU)
MU_0_MUB
JDC (JTAG Data Communication)
Configuration GPR
Self-Test Control Unit
Selftest GPR
Crossbar Integrity Checker (eDMA & STAM AXBS-Lite)
Crossbar Integrity Checker (PRAM2 & TCM backdoor AHB Splitter)
eDMA transfer control descriptor 12
eDMA transfer control descriptor 13
eDMA transfer control descriptor 14
eDMA transfer control descriptor 15
eDMA transfer control descriptor 16
eDMA transfer control descriptor 17
eDMA transfer control descriptor 18
eDMA transfer control descriptor 19
eDMA transfer control descriptor 20
eDMA transfer control descriptor 21
eDMA transfer control descriptor 22
eDMA transfer control descriptor 23
eDMA transfer control descriptor 24
eDMA transfer control descriptor 25
eDMA transfer control descriptor 26
eDMA transfer control descriptor 27
eDMA transfer control descriptor 28
eDMA transfer control descriptor 29
eDMA transfer control descriptor 30
eDMA transfer control descriptor 31
Semaphores2
RAM controller 1
RAM controller 2
Software Watchdog 1
Software Watchdog 2
System Timer Module 1
System Timer Module 2
GMAC_0
Low Power UART 8
Low Power UART 9
Low Power UART 10
Low Power UART 11
Low Power UART 12
Low Power UART 13
Low Power UART 14
Low Power UART 15
Low Power SPI 4
Low Power SPI 5
QuadSPI
Synchronous Audio Interface 1
Ultra Secured Digital Host Controller
Low Power Comparator 2
MU_1_MUB
EIM_0
EIM_1
EIM_2
EIM_3
PRAM2
64 - bit + ECC*
x72
SRAM2
256 KB
P0
AHB_32_64
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
AHB_32_64
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
AHB_32_64
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
1:2AHB_32_64
ADDR 
CHECK
1:1
ADDR 
GEN
1:1
1:1
1:1
PFLASH Port  
Master Assignment
P0
P1
P2
P3
CM7_0
HSE & Others
CM7_1
CM7_2
RDATA 
CHECK
WDATA
GEN
ADDR
GEN
Part Number
Lockstep
Lockstep
Decoupled
Decoupled
Decoupled
Disabled
S32K328
S32K348
S32K358
S32K338
N/A
N/A
CM7_0
CM7_1
CM7_2
CM7_0-CM7_1
N/A
N/A
N/A
CM7_2
CM7_0-CM7_1
N/A
N/A
N/A
N/A
N/A
N/A
CM7_0
CM7_1
CM7_2
N/A
N/A
CM7_2
Up to 240MHz
Up to 30 MHz
Up to 120MHz
Up to 120MHz
Up to 120MHz
AHB32
APB v3
AXI64
IPBUS
AHB64
AHB64 (optional 
based on split-lock)
On-platform
Off-platform
ECC gaskets
Configurable gaskets
Fixed gaskets
N/A
CM7_2
Figure 9. Block diagram – S32K338, S32K358, S32K348 and S32K328
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
25 / 5251


---
# 페이지 20

CM7_0
MPU
FPU
DSP
NVIC
I-TCM
32KB
64-bit
64-bit
32-bit
D-TCM
32KB
32-bit
32-bit
32-bit
1
Decoupled =0
Lockstep = 1
0
1
0
1
0
1
Decoupled =0
Lockstep = 1
0
1
0
1
0
+
+
+
CM7_1
MPU
FPU
DSP
NVIC
32KB
D-TCM
32KB
D-TCM
32KB
AHBS
32-bit
AXI
64-bit
AHBP
32-bit
AHBS
32-bit
AXI
64-bit
AHBP
32-bit
I- CACHE
D- CACHE
I- CACHE
D- CACHE
16KB
16KB
16KB
16KB
Split-Lock Capable
Secondary  
(checker  
or split) core
XHB400
Primary core
D-TCM
32KB
I-TCM
CM7_2
16KB
16KB
I-TCM
32KB
64-bit
D-TCM
32KB
D-TCM
32KB
32-bit
32-bit
D- CACHE
I- CACHE
Permanent Lock-Step
2:1 AHB_32_64
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
2:1
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
CM7_3
MPU
FPU
DSP
NVIC
16KB
16KB
I-TCM
32KB
64-bit
D-TCM
32KB
D-TCM
32KB
32-bit
32-bit
Secondarycore
AHBS
32-bit
AXI
64-bit
AHBP
32-bit
D- CACHE
I- CACHE
MDAC0
cm70_ahbs
XHB400
2:1 AHB_32_64
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
2:1
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
MDAC4
cm71_ahbs
2:1 AHB_32_64
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
2:1
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
MDAC6
cm72_ahbs
XHB400
2:1 AHB_32_64
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
2:1
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
MDAC8
cm73_ahbs
XHB400
* ECC data and address encode
AIPS1
AIPS0
PRAM0
64 - bit + ECC*
x72
SRAM0
256 KB
PRAM1
64 - bit + ECC*
x72
SRAM1
256 KB
PAC0
M0
M0
M7
M2
M4
M1
M5
M3
S3
S6
S2
S1
S2
S0
P0
P0
PAC1
QSPI AHB 
Data & 
Code
S5
MRC2
ADDR 
CHECK
2:1
AIPS2
WDATA 
CHECK
RDATA 
GEN
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
C-
C-C-
C- Flash
2 MB
PFLASH
64 - bit + ECC
x256
D-Flash
128KB
S1
S4
S0
P0
P2
P1
P3
S7
MRC0
C-
C-C-
C- Flash
2 MB
C-
C-C-
C- Flash
2 MB
C-
C-C-
C- Flash
2 MB
ADDR 
CHECK
RDATA 
GEN
ADDR 
CHECK
RDATA 
GEN
ADDR 
CHECK
RDATA 
GEN
ADDR 
CHECK
RDATA 
GEN
MDAC5
RDATA 
CHECK
WDATA
GEN
1:1
GMAC0
ADDR
GEN
eDMA3
32ch
MDAC1
AXBS_Lite
S0
M0
ADDR
CHECK
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
1:1
ADDR
CHECK
ADDR
GEN
1:1
AXBS_Lite
S0
S1
M0
M1
XBIC
aes_accel
AHB
64b
AHB
64b
AES_ACCEL
AHB-M0
64b
AHB-M1
64b
AHB-S
64b
HSE
AHB
64b
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
1:1
MDAC3
ADR
CHECK
ADDR
GEN
1:1
1:2 64:32
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
1:2 64:32
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
1:2 64:32
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
1:2 64:32
S0
S1
M0
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
MRC1
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
MRC3
AXBS  
(64-bit)
AXBS_Lite
(64-bit)
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
1:1
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
1:1
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
1:1
S3
ADDR 
CHECK
RDATA 
GEN
WDATA 
CHECK
1:1
aes_accel
cm70_ahbs
cm71_ahbs
cm72_ahbs
cm73_ahbs
M4
M5
M3
M6
M1
M2
MPU
FPU
DSP
NVIC
Primary core
AHBS
32-bit
AXI
64-bit
AHBP
32-bit
CM7_checker
XBIC
System AXBS  XBIC
Peripheral AXBS  XBIC
MDAC7
RDATA 
CHECK
WDATA
GEN
1:1
GMAC1
ADDR
GEN
AHB
64b
MRC4
CM7_2
AXBS_Lite
(64-bit)
AXBS_Lite
S0
M0
M1
XBIC
Crossbar Integrity Checker (HSE_B & AES_ACCEL 
AXBS_Lite)
ERM_1
Software Watchdog 3
Trigger Multiplexing Control
Body Cross Triggering Unit
eMIOS_0
eMIOS_1
eMIOS_2
Logic Control Unit 0
Logic Control Unit 1
Analog-to-digital converter 0
Analog-to-digital converter 1
Analog-to-digital converter 2
Programmable Interrupt Timer 0
Programmable Interrupt Timer 1
MU_2_MUA
MU_2_MUB
MU_3_MUA
MU_3_MUB
MU_4_MUA
MU_4_MUB
PAC2
System crossbar switch
Crossbar Integrity Checker (System AXBS / AXBS Lite)
Crossbar Integrity Checker (Peripheral AXBS-Lite)
eDMA control & status (MP_CSR; MP_ES; MP_HRS)
eDMA transfer control descriptor 0
eDMA transfer control descriptor 1
eDMA transfer control descriptor 2
eDMA transfer control descriptor 3
eDMA transfer control descriptor 4
eDMA transfer control descriptor 5
eDMA transfer control descriptor 6
eDMA transfer control descriptor 7
eDMA transfer control descriptor 8
eDMA transfer control descriptor 9
eDMA transfer control descriptor 10
eDMA transfer control descriptor 11
Debug APB Page0
Debug APB Page1
Debug APB Page2
Debug APB Page3
Debug APB Paged Area
SDA-AP
ERM_0
MSCM
RAM controller 0
Flash controller
Flash controller alternate
Software Watchdog 0
System Timer Module 0
XRDC
Interrupt Monitor
DMA Channel Multiplexer 0
DMA Channel Multiplexer 1
Real-time clock
Reset Generation Module
SIUL2_VIRTWRAPPER_PDAC0
SIUL2_VIRTWRAPPER_PDAC0
SIUL2_VIRTWRAPPER_PDAC1
SIUL2_VIRTWRAPPER_PDAC1
SIUL2_VIRTWRAPPER_PDAC2
SIUL2_VIRTWRAPPER_PDAC2
SIUL2_VIRTWRAPPER_PDAC3
System Status and Configuration Module
Wakeup Unit
CMU 0-6
Touch Sensing Coupling Controller
32 kHz Slow Internal RC Oscillator
32 kHz Slow External Crystal Oscillator
48 MHz Fast Internal RC Oscillator
8-40 MHz Fast External Crystal Oscillator
Clock Generation Module
Mode Entry Module
Frequency Modulated Phase-Locked Loop
Frequency Modulated Phase-Locked Loop 2
Power management controller
Flash memory
Flash memory alternate
SIUL2_VIRTWRAPPER_PDAC4
SIUL2_VIRTWRAPPER_PDAC4
Programmable Interrupt Timer 2
Programmable Interrupt Timer 3
FlexCAN_0
FlexCAN_1
FlexCAN_2
FlexCAN_3
FlexCAN_4
FlexCAN_5
FlexCAN_6
FlexCAN_7
Flexible IO
Low Power UART 0
Low Power UART 1
Low Power UART 2
Low Power UART 3
Low Power UART 4
Low Power UART 5
Low Power UART 6
Low Power UART 7
SIUL2_VIRTWRAPPER_PDAC5
SIUL2_VIRTWRAPPER_PDAC5
Low Power I2C 0
Low Power I2C 1
Low Power SPI 0
Low Power SPI 1
Low Power SPI 2
Low Power SPI 3
Synchronous Audio Interface 0
Low Power Comparator 0
Low Power Comparator 1
TMU Temperature Sensor Unit
CRC
FCCU (+FOSU)
MU_0_MUB
JDC (JTAG Data Communication)
Configuration GPR
Self-Test Control Unit
Selftest GPR
AES Accelerator
AES Application 0
AES Application 1
AES Application 2
Crossbar Integrity Checker (TCM backdoor AHB Splitter)
Crossbar Integrity Checker (eDMA AXBS-Lite)
Crossbar Integrity Checker (PRAM2 & TCM backdoor AHB Splitter)
Crossbar Integrity Checker (AES_ACCEL AHB Multiplexer)
eDMA transfer control descriptor 12
eDMA transfer control descriptor 13
eDMA transfer control descriptor 14
eDMA transfer control descriptor 15
eDMA transfer control descriptor 16
eDMA transfer control descriptor 17
eDMA transfer control descriptor 18
eDMA transfer control descriptor 19
eDMA transfer control descriptor 20
eDMA transfer control descriptor 21
eDMA transfer control descriptor 22
eDMA transfer control descriptor 23
eDMA transfer control descriptor 24
eDMA transfer control descriptor 25
eDMA transfer control descriptor 26
eDMA transfer control descriptor 27
eDMA transfer control descriptor 28
eDMA transfer control descriptor 29
eDMA transfer control descriptor 30
eDMA transfer control descriptor 31
Semaphores2
RAM controller 1
RAM controller 2
Software Watchdog 1
Software Watchdog 2
System Timer Module 1
System Timer Module 2
System Timer Module 3
GMAC_0
GMAC_1
Low Power UART 8
Low Power UART 9
Low Power UART 10
Low Power UART 11
Low Power UART 12
Low Power UART 13
Low Power UART 14
Low Power UART 15
Low Power SPI 4
Low Power SPI 5
QuadSPI
Synchronous Audio Interface 1
Low Power Comparator 2
MU_1_MUB
EIM_0
EIM_1
EIM_2
EIM_3
AES Application 3
AES Application 4
AES Application 5
AES Application 6
AES Application 7
PRAM2
64 - bit + ECC*
x72
SRAM2
256 KB
P0
MDAC9
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
WDATA 
GEN
RDATA 
CHECK
ADDR
GEN
XBIC
S1
PFLASH Port
Master Assignment
P0
P1
P2
P3
CM7_0
HSE & Others
CM7_1 & CM7_3
CM7_2
Part Number
Lockstep
Lockstep
Decoupled
Decoupled
Decoupled
Disabled
S32K388LS
S32K388
CM7_0-CM7_1
CM7_2
CM7_3
N/A
N/A
N/A
CM7_2
N/A
CM7_0
CM7_1
CM7_3
N/A
AHB32
APB v3
AXI64
IPBUS
AHB64
AHB64 (optional 
based on split-lock)
On-platform
Off-platform
ECC gaskets
Configurable gaskets
Fixed gaskets
Up to 26.67 MHz
Up to 320MHz
Up to 160MHz
Up to 320MHz
Up to 320MHz
Up to 320MHz
Up to 80MHz
S0
M0
S1
S2
S3
AHB Splitter
XBIC
AXBS_Lite
(64-bit)
1:1
AHB Splitter
ADDR 
CHECK
ADDR
GEN
Figure 10. Block diagram – S32K388
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
26 / 5251


---
# 페이지 21

C-
C-
C-
C- Fla s h
1 MB
C-
C-
C-
C- Fla s h
1 MB
C-
C-
C-
C- Fla s h
2 MB
CM7_ 0
MPU
FPU
DSP
NVIC
I- TCM
32KB
64- b it
64- b it
32- b it
D- TCM
32KB
32- b it
32- b it
32- b it
1
De c oup le d  = 0
Loc kste p  = 1
0
1
0
1
0
1
Dec oup le d  = 0
Loc kste p  = 1
0
1
0
1
0
+
+
+
CM7_ 1
MPU
FPU
DSP
NVIC
32KB
D-TCM
32KB
D-TCM
32KB
AHBS
32- b it
AXI
64- b it
AHBP
32- b it
AHBS
32- b it
AXI
64- b it
AHBP
32- b it
I-CACHE
D-CACHE
I-CACHE
D- CACHE
16KB
16KB
16KB
16KB
Sp lit- Loc k Ca p a b le
Se c ond a ry
(c he c ke r
or sp lit) c ore
XHB4 0 0
Prim a ry c ore
(op tiona l)
D- TCM
32KB
I- TCM
CM7_ 2
16KB
16KB
I- TCM
32KB
64- b it
D-TCM
32KB
D- TCM
32KB
32- b it
32- b it
D- CACHE
I- CACHE
Pe rm a n e n t Loc k- Ste p
2:1 AHB_ 32_ 64
ADDR
GEN
WDATA
GEN
RDATA
CHECK
2:1
ADDR
GEN
WDATA
GEN
RDATA
CHECK
CM7_ 3
MPU
FPU
DSP
NVIC
16KB
16KB
I- TCM
32KB
64- b it
D- TCM
32KB
D- TCM
32KB
32- b it
32- b it
Se c ond a ry c ore
AHBS
32- b it
AXI
64- b it
AHBP
32- b it
D- CACHE
I- CACHE
MDAC0
c m 70_ a hb s
XHB4 0 0
2:1 AHB_ 32_ 64
ADDR
GEN
WDATA
GEN
RDATA
CHECK
2:1
ADDR
GEN
WDATA
GEN
RDATA
CHECK
MDAC4
c m 71_ a hb s
2:1 AHB_ 32_ 64
ADDR
GEN
WDATA
GEN
RDATA
CHECK
2:1
ADDR
GEN
WDATA
GEN
RDATA
CHECK
MDAC6
c m 72_ a hb s
XHB4 0 0
2:1 AHB_ 32_ 64
ADDR
GEN
WDATA
GEN
RDATA
CHECK
2:1
ADDR
GEN
WDATA
GEN
RDATA
CHECK
MDAC8
c m 73_ a hb s
XHB4 0 0
* ECC d a ta  a nd  a d d re ss e nc od e
AIPS1
PRAM0
64 - b it + ECC*
x72
SRAM0
512 KB
PRAM1
64- b it + ECC*
x72
SRAM1
512 KB
PAC0
M0
M0
M7
M2
M4
M1
M5
M3
S3
S6
S2
S1
S2
S0
P0
P0
PAC1
QSPI AHB
Da ta  & Cod e
S5
MRC2
ADDR
CHECK
2:1
WDATA
CHECK
RDATA
GEN
26.67 MHz
PFC0
64 - b it + ECC
x256
D - Fla s h
256 KB
S4
S0
P0
P1
MRC0
C-
C-
C-
C- Fla s h
2 MB
C-
C-
C-
C- Fla s h
2 MB
C-
C-
C-
C- Fla s h
2 MB
ADDR
CHECK
RDATA
GEN
ADDR
CHECK
RDATA
GEN
MDAC5
RDATA
CHECK
WDATA
GEN
1:1
GMAC0
ADDR
GEN
CORE_CLK = Up to 160 MHz 
e DMA3
32c h
MDAC1
AXBS_ Lite
S0
S1
M0
XBIC
ADDR
CHECK
ADDR
GEN
WDATA
GEN
RDATA
CHECK
ADDR
GEN
1:1
ADDR
CHECK
ADDR
GEN
1:1
AXBS_ Lite
S0
S1
M0
M1
XBIC
a e s_ a c c e l
AHB
64b
AHB
64 b
AES_ ACCEL
AHB- M0
64b
AHB- M1
64b
AHB- S
64b
HSE
AHB
64 b
WDATA
GEN
RDATA
CHECK
ADDR
GEN
1:1
MDAC3
ADR
CHECK
ADDR
GEN
1:1
S0
S1
M0
ADDR
CHECK
RDATA
GEN
WDATA
CHECK
MRC1
ADDR
CHECK
RDATA
GEN
WDATA
CHECK
ADDR
CHECK
RDATA
GEN
WDATA
CHECK
MRC3
AXBS
(64- b it)
AXBS_ Lite
(64- b it)
ADDR
CHECK
RDATA
GEN
WDATA
CHECK
1:1
ADDR
CHECK
RDATA
GEN
WDATA
CHECK
1:1
ADDR
CHECK
RDATA
GEN
WDATA
CHECK
1:1
S3
ADDR
CHECK
RDATA
GEN
WDATA
CHECK
1:1
a e s_ a c c e l
M4
M5
M3
M6
M1
M2
AXI64
AHB64
AHB32
IPBUS
APB v3
LEGEND
ECC g a ske ts
Con fig ura b le  g a ske ts
AHB64 (op tiona l
b a se d  on sp lit-
loc k)
On- p la tform
Off- p la tform
Fixe d
g a ske ts
MPU
FPU
DSP
NVIC
Prim a ry c ore
(op tiona l)
AHBS
32- b it
AXI
64- b it
AHBP
32- b it
CM7_ c h e c ke r
AHB Sp litte r
XBIC
Sys te m  AXBS
XBIC
Pe rip h e ra l AXBS
XBIC
MDAC7
RDATA
CHECK
WDATA
GEN
1:1
GMAC1
ADDR
GEN
AHB
64b
MRC4
CM7_ 2
AXBS_ Lite
(64- b it)
AXBS_ Lite
S0
M0
M1
XBIC
Crossb a r Inte g rity Che c ke r (HSE & AES_ ACCEL
AXBS_ Lite )
ERM1
Softwa re  Wa tc hd og  3
Trig g e r Multip le xing  Control
Bod y Cross Trig g e ring  Unit
e MIOS 0
e MIOS 1
e MIOS 2
Log ic  Control Unit 0
Log ic  Control Unit 1
Ana log - to- d ig ita l c onve rte r 0
Ana log - to- d ig ita l c onve rte r 1
Ana log - to- d ig ita l c onve rte r 2
Prog ra m m a b le  Inte rrup t Tim e r 0
Prog ra m m a b le  Inte rrup t Tim e r 1
MU_ 2_ MUA
MU_ 2_ MUB
MU_ 3_ MUA
MU_ 3_ MUB
MU_ 4_ MUA
MU_ 4_ MUB
PAC2
Sys te m  c rossb a r s witc h
Crossb a r Inte g rity Che c ke r (Syste m  AXBS /  AXBS
Lite )
Crossb a r Inte g rity Che c ke r (Pe rip he ra l AXBS- Lite )
e DMA c ontrol & sta tus (MP_ CSR; MP_ ES; MP_ HRS)
e DMA tra nsfe r c ontrol d e sc rip tor 0
e DMA tra nsfe r c ontrol d e sc rip tor 1
e DMA tra nsfe r c ontrol d e sc rip tor 2
e DMA tra nsfe r c ontrol d e sc rip tor 3
e DMA tra nsfe r c ontrol d e sc rip tor 4
e DMA tra nsfe r c ontrol d e sc rip tor 5
e DMA tra nsfe r c ontrol d e sc rip tor 6
e DMA tra nsfe r c ontrol d e sc rip tor 7
e DMA tra nsfe r c ontrol d e sc rip tor 8
e DMA tra nsfe r c ontrol d e sc rip tor 9
e DMA tra nsfe r c ontrol d e sc rip tor 10
e DMA tra nsfe r c ontrol d e sc rip tor 11
De b ug  APB Pa g e 0
De b ug  APB Pa g e 1
De b ug  APB Pa g e 2
De b ug  APB Pa g e 3
De b ug  APB Pa g e d  Are a
SDA- AP
ERM0
MSCM
RAM c ontrolle r 0
Fla sh c ontrolle r
Fla sh c ontrolle r a lte rna te
Softwa re  Wa tc hd og  0
Sys te m  Tim e r Mod ule  0
XRDC
Inte rrup t Monitor
DMA Cha nne l Multip le xe r 0
DMA Cha nne l Multip le xe r 1
Re a l- tim e  c loc k
Re se t Ge ne ra tion Mod ule
SIUL_ VIRTWRAPPER_ PDAC0
SIUL_ VIRTWRAPPER_ PDAC0
SIUL_ VIRTWRAPPER_ PDAC1
SIUL_ VIRTWRAPPER_ PDAC1
SIUL_ VIRTWRAPPER_ PDAC2
SIUL_ VIRTWRAPPER_ PDAC2
SIUL_ VIRTWRAPPER_ PDAC3
Sys te m  Sta tus a nd  Config ura tion Mod ule
Wa ke up  Unit
CMU 0- 6
Touc h Se nsing  Coup ling  Controlle r
32 kHz Slow Inte rna l RC Osc illa tor
32 kHz Slow Exte rna l Crysta l Osc illa tor
48 MHz Fa st Inte rna l RC Osc illa tor
8- 40 MHz Fa st Exte rna l Crysta l Osc illa tor
Cloc k Ge ne ra tion Mod ule
Mod e  Entry Mod ule
Fre q ue nc y Mod ula te d  Pha se - Loc ke d  Loop
Fre q ue nc y Mod ula te d  Pha se - Loc ke d  Loop  2
Powe r m a na g e m e nt c ontrolle r
Fla sh m e m ory
Fla sh m e m ory a lte rna te
SIUL_ VIRTWRAPPER_ PDAC4
SIUL_ VIRTWRAPPER_ PDAC4
Prog ra m m a b le  Inte rrup t Tim e r 2
Prog ra m m a b le  Inte rrup t Tim e r 3
Fle xCAN 0
Fle xCAN 1
Fle xCAN 2
Fle xCAN 3
Fle xCAN 4
Fle xCAN 5
Fle xCAN 6
Fle xCAN 7
Fle xib le  IO
Low Powe r UART 0
Low Powe r UART 1
Low Powe r UART 2
Low Powe r UART 3
Low Powe r UART 4
Low Powe r UART 5
Low Powe r UART 6
Low Powe r UART 7
SIUL_ VIRTWRAPPER_ PDAC5
SIUL_ VIRTWRAPPER_ PDAC5
Low Powe r I2C 0
Low Powe r I2C 1
Low Powe r SPI 0
Low Powe r SPI 1
Low Powe r SPI 2
Low Powe r SPI 3
Sync hronous  Aud io Inte rfa c e  0
Low Powe r Com p a ra tor 0
Low Powe r Com p a ra tor 1
TMU Te m p e ra ture  Se nsor Unit
CRC
FCCU (+FOSU)
Me m ory Te st a nd  Re p a ir
MU_ 0_ MUB
JDC (J TAG Da ta  Com m unic a tion)
Config ura tion GPR
Se lf- Te st Control Unit
Se lfte st GPR
AES Ac c e le ra tor
AES Ap p lic a tion 0
AES Ap p lic a tion 1
AES Ap p lic a tion 2
AES Ap p lic a tion 3
Crossb a r Inte g rity Che c ke r (TCM b a c kd oor AHB Sp litte r)
Crossb a r Inte g rity Che c ke r (e DMA & STAM AXBS- Lite )
Crossb a r Inte g rity Che c ke r (PRAM2 & TCM b a c kd oor AHB
Sp litte r)
Crossb a r Inte g rity Che c ke r (AES_ ACCEL AHB Multip le xe r)
e DMA tra nsfe r c ontrol d e sc rip tor 12
e DMA tra nsfe r c ontrol d e sc rip tor 13
e DMA tra nsfe r c ontrol d e sc rip tor 14
e DMA tra nsfe r c ontrol d e sc rip tor 15
e DMA tra nsfe r c ontrol d e sc rip tor 16
e DMA tra nsfe r c ontrol d e sc rip tor 17
e DMA tra nsfe r c ontrol d e sc rip tor 18
e DMA tra nsfe r c ontrol d e sc rip tor 19
e DMA tra nsfe r c ontrol d e sc rip tor 20
e DMA tra nsfe r c ontrol d e sc rip tor 21
e DMA tra nsfe r c ontrol d e sc rip tor 22
e DMA tra nsfe r c ontrol d e sc rip tor 23
e DMA tra nsfe r c ontrol d e sc rip tor 24
e DMA tra nsfe r c ontrol d e sc rip tor 25
e DMA tra nsfe r c ontrol d e sc rip tor 26
e DMA tra nsfe r c ontrol d e sc rip tor 27
e DMA tra nsfe r c ontrol d e sc rip tor 28
e DMA tra nsfe r c ontrol d e sc rip tor 29
e DMA tra nsfe r c ontrol d e sc rip tor 30
e DMA tra nsfe r c ontrol d e sc rip tor 31
Se m a p hore s2
RAM c ontrolle r 1
RAM c ontrolle r 2
Softwa re  Wa tc hd og  1
Softwa re  Wa tc hd og  2
Sys te m  Tim e r Mod ule  1
Sys te m  Tim e r Mod ule  2
Sys te m  Tim e r Mod ule  3
GMAC0
GMAC1
Low Powe r UART 8
Low Powe r UART 9
Low Powe r UART 10
Low Powe r UART 11
Low Powe r UART 12
Low Powe r UART 13
Low Powe r UART 14
Low Powe r UART 15
Low Powe r SPI 4
Low Powe r SPI 5
Qua d SPI
Sync hronous  Aud io Inte rfa c e  1
Low Powe r Com p a ra tor 2
MU_ 1_ MUB
EIM0
EIM1
EIM2
EIM3
AES Ap p lic a tion 4
AES Ap p lic a tion 5
AES Ap p lic a tion 6
AES Ap p lic a tion 7
Fle xCAN 8
Fle xCAN 9
Fle xCAN 10
Fle xCAN 11
Op tiona l g a ske ts
PRAM2
64- b it + ECC*
x72
SRAM2
512 KB
P0
PFLASH Port Master assignment
P0
CM7_0 & CM7_2
P1
CM7_1 & CM7_3 & HSE & others
MDAC9
WDATA
GEN
RDATA
CHECK
ADDR
GEN
WDATA
GEN
RDATA
CHECK
ADDR
GEN
CM7_CORE_CLK = 320 MHz
ADDR
CHECK
RDATA
GEN
WDATA
CHECK
1:2 64 :32
ADDR
CHECK
RDATA
GEN
WDATA
CHECK
1:2 64 :32
ADDR
CHECK
RDATA
GEN
WDATA
CHECK
1:2 64 :32
ADDR
CHECK
RDATA
GEN
WDATA
CHECK
1:2 64 :32
S0
M0
S1
S2
S3
c m 70_ a hb s
c m 71_ a hb s
c m 72_ a hb s
c m 73_ a h b s
AHB Sp litte r
XBIC
AXBS_ Lite
(64- b it)
1:1
ADDR
CHECK
ADDR
GEN
M0
32 MHz
PFC1
64 - b it + ECC
x256
S7
S1
P0
P1
MRC5
ADDR
CHECK
RDATA
GEN
ADDR
CHECK
RDATA
GEN
S2
ADDR
CHECK
RDATA
GEN
WDATA
CHECK
PRAM3
64- b it + ECC*
x72
SRAM3
384 KB
P0
AIPS2
AIPS0
FAR*
FAR*
C-
C-
C-
C- Fla s h
1 MB
C-
C-
C-
C- Fla s h
1 MB
C-
C-
C-
C- Fla s h
1 MB
C-
C-
C-
C- Fla s h
1 MB
*Only PRAM0, PRAM1, and PRAM2 support 
  code executioncontrol
CM7_CORE_CLK = 320 MHz
CM7_CORE_CLK = 320 MHz
QSPI_AHB_CLOCK = 80 MHz
CM7_CORE_CLK = 320 MHz
320 MHz
80 MHz
160 MHz
Figure 11. Block diagram – S32K389
2.5 Feature comparison
The following table compares some of the prominent features related to memory and package options of these chips from the 
S32K3xx family/product series:
• S32K310
• S32K311
• S32K312
• S32K322
• S32K341
• S32K342
• S32K314
• S32K324
• S32K344
• S32K328
• S32K338
• S32K348
• S32K358
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
27 / 5251


---
# 페이지 22

• S32K388
• S32K389
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
28 / 5251


---
# 페이지 23

Table 5. S32K3xx chip's feature comparison
Feature
Chip
S32K310
S32K311
S32K312
S32K322
S32K341
S32K342
S32K314
S32K324
S32K344
S32K328
S32K338
S32K348
S32K358
S32K388
S32K3891
Safety/
ASIL
B
D
B
D
B
D
Program 
flash 
memory
512 KB
1 MB
2 MB
1 MB
2 MB
4 MB
8 MB
12 MB
Data flash 
memory 
(KB)
64
128
128
256
Total 
RAM (KB)
112KB 
(incl. 
96KB 
TCM)
128KB 
(incl. 
96KB 
TCM)
192KB 
(incl. 
96KB 
TCM)
256KB (incl. 192KB TCM)
512KB 
(includin
g 96KB 
TCM)
512KB (incl. 
192KB TCM)
1152KB 
(incl. 
192KB 
TCM)
1152KB 
(incl. 
384KB 
TCM)
1152KB 
(incl. 
192KB 
TCM)
1152KB (incl. 
384KB TCM)
2304KB 
(incl. 
384KB 
TCM)
Standby 
RAM
16 KB
32 KB
64 KB
Security
HSE_B
HSE B + 
AES_ACCEL
Core 
quantity
1 x M7
2 x M7
1 x M7 LS
1 x M7
2 x M7
1 x M7 
LS
2 x M7
3 x M7
1 x M7 
LS
1xM7 
LS + 
1xM7
1xM7 
LS+3xM
7 or 
2xM7 
LS+1xM
7
1xM7 
LS + 
3xM7 or 
2xM7 
LS 
+1xM7
Frequenc
y (MHz)
120
160
240
320
DMA 
channels
12
32
Table continues on the next page...
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
29 / 5251


---
# 페이지 24

Table 5. S32K3xx chip's feature comparison (continued)
Feature
Chip
S32K310
S32K311
S32K312
S32K322
S32K341
S32K342
S32K314
S32K324
S32K344
S32K328
S32K338
S32K348
S32K358
S32K388
S32K3891
ASIL-B 
DMIPS 2 3
277-387-813
738-103
2-
2168
—
369-516
-
1084
738-103
2-
2168
—
1108-
1550-
3254
1662-23
25-
4881
—
554-
775-
1627
739-
1033-
2169 4
2217-
3099-
6507 5
ASIL-D 
DMIPS 2 3
—
369-516-1084
—
369-
516-
1084
—
554-
775-
1627
1478-
2066-
4338 4
739-
1033-
2169 5
ASIL-B 
CoreMark 
score 2 6
634
1692
—
846
1692
—
2538
3807
—
1269
1692 4
5078 5
ASIL-D 
CoreMark 
score 2 6
—
846
—
846
—
1269
1269
3384 4
1692 5
FlexCAN 
instances
3
6
4
6
8
12
EMAC 
instances
—
1
—
GMAC 
instances
—
1
2
SAI 
instances
—
2
Table continues on the next page...
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
30 / 5251


---
# 페이지 25

Table 5. S32K3xx chip's feature comparison (continued)
Feature
Chip
S32K310
S32K311
S32K312
S32K322
S32K341
S32K342
S32K314
S32K324
S32K344
S32K328
S32K338
S32K348
S32K358
S32K388
S32K3891
LPUART 
instances
4
8
4
16
LPSPI 
instances
4
6
I2C 
instances
2
FlexIO 
(incl. 
SENT 
support) 
channels
16
32
QuadSPI 
instances
—
17
18
17
uSDHC 
instances
—
1
—
ADC 
instances
2
3
LPCMP 
instances
1
2
3
PIT 
instances
2
3
4
SWT 
instances
1
2
1
2
1
2
3
1
2
4
STM 
instances
1
2
3
4
Table continues on the next page...
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
31 / 5251


---
# 페이지 26

Table 5. S32K3xx chip's feature comparison (continued)
Feature
Chip
S32K310
S32K311
S32K312
S32K322
S32K341
S32K342
S32K314
S32K324
S32K344
S32K328
S32K338
S32K348
S32K358
S32K388
S32K3891
LCU 
instances
2
BCTU 
instances
1
TRGMUX 
instances
1
eMIOS 
instances
2
3
RTC 
instances
1
437-ball 
MAPBGA 
package
No
Yes
289-ball 
MAPBGA 
package
No
Yes
No
257-ball 
MAPBGA 
package
No
Yes
No
172-
HDQFP 
package
No
Yes
No
172-
HDQFP - 
EP 
package
No
Yes
No
Table continues on the next page...
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
32 / 5251


---
# 페이지 27

Table 5. S32K3xx chip's feature comparison (continued)
Feature
Chip
S32K310
S32K311
S32K312
S32K322
S32K341
S32K342
S32K314
S32K324
S32K344
S32K328
S32K338
S32K348
S32K358
S32K388
S32K3891
100-
HDQFP 
package
Yes
No
48-pin 
LQFP 
package
Yes
No
1. This feature set is under evaluation and subject to change.
2. ASIL-B and ASIL-D performance is available simultaneously. ASIL-D performance can also be used for ASIL-B performance.
3. The first result abides by all of the "ground rules" out in Dhrystone documentation, the second permits inlining of functions, not just permitted C strings libraries, 
while the third additionally permits simultaneous ("multi-file") compilation. All are with the original (K and R) v2.1 of Dhrystone. Arm Compiler 6.17. See https://
developer.arm.com/Processors/Cortex-M7 for details.
4. Core configuration is 2xLS + 1 independent core
5. Core configuration is 1xLS + 3 independent cores
6. Results depends on specific compiler version, contact NXP sales representative for more details.
7. 4-bit data width, SDR mode only
8. 8-bit data width, SDR and DDR mode
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
33 / 5251


---
# 페이지 28

2.6 Glossary
AES
Advanced encryption standard
ASIL
Automotive safety integrity level. This is a risk classification scheme as defined by ISO 26262 for automotive 
standard.
AVB
Audio video bridging
CBC
Cipher block chaining
CCM
Counter with CBC MAC (Cipher block chaining message authentication code)
CMAC
Cipher-based message authentication code
CTR
Counter-based block cipher mode
DSP
Digital signal processor
DWT
Debug watchpoint and trace
ECB
Electronic code book
ECC
Elliptic curve cryptography/ Error code correction
ETM
Embedded trace macrocell
ETF
Embedded trace FIFO
EVITA
E-Safety vehicle intrusion protected applications
FPB
Flash patch and breakpoint unit
GCM
Galois/Counter mode, an encryption algorithm
GMAC
Galois message authentication code
GPIO
General purpose input/output
ITM
Instrumentation trace macrocell
ISOCAN-FD ISO 11898-1 compliant CAN with FD (Flexible datarate)
LVD
Low voltage detection
NMI
Non-maskable interrupt
OFB
Output feedback based block cipher mode
PIL
Processor-in-the-loop
PLL
Phase locked loop oscillator
PWM
Pulse width modulation
RTD
Real-Time Drivers
SDK
Software development kit
SENT
Single edge nibble transmission
SWV
Serial wire viewer
SPFPU
Single precision floating point unit
SWO
Serial wire output
TPIU
Trace port interface unit
TSN
Time sensitive networking
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
34 / 5251


---
# 페이지 29

uSDHC
Ultra Secure Digital Host Controller
WDOG
Windowed watchdog
NXP Semiconductors
Introduction
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
35 / 5251
