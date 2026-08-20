# S32K3xx_DS

이 문서는 PDF에서 자동으로 변환된 문서입니다.

---

# 페이지 1

• Operating characteristics
— Voltage range: 2.97 V to 5.5 V
— Ambient temperature range: -40 °C to 125 °C for all 
power modes
• Arm™ Cortex-M7 core, 32-bit CPU
— M7 supports up to 320 MHz frequency with 2.14 
DMIPS / MHz
— Arm Core based on the Armv7 and Thumb®-2 ISA
— Integrated Digital Signal Processor (DSP)
— Configurable Nested Vectored Interrupt Controller 
(NVIC)
— Single Precision Floating Point Unit (FPU)
• Clock interfaces
— 8 - 40 MHz Fast External Oscillator (FXOSC)
— 48 MHz Fast Internal RC oscillator (FIRC)
— 32 kHz Low Power Oscillator (SIRC)
— 32 kHz Slow External Oscillator (SXOSC)
— System Phased Lock Loop (SPLL)
• I/O and package
— MAPBGA437 , LQFP48, HDQFP100, HDQFP172, 
MAPBGA257, MAPBGA289, HDQFP172 with 
Exposed pad (EP) package options
• Up to 32-channel DMA with up to 128 request sources 
using DMAMUX
• Memory and memory interfaces
— Up to 12 MB program flash memory with ECC
— Up to 256 KB of flexible program or data flash 
memory
— Up to 2304 KB SRAM with ECC, includes 384 KB 
of TCM RAM ensuring maximum CPU performance 
of fast control loops with minimal latency
— Data and instruction cache for each core to 
minimize performance impact of memory access 
latencies
— QuadSPI support
• Mixed-signal analog
— Up to three 12-bit Analog-to-Digital Converters 
(ADC) with up to 24 channel analog inputs per 
module
— One Temperature Sensor (TempSense)
— Up to three Analog Comparators (CMP), with each 
comparator having an internal 8-bit DAC
• Human-Machine Interface (HMI)
— Up to 320 GPIO pins
— Non-Maskable Interrupt (NMI)
— Up to 60 pins with wakeup capability
— Up to 32 pins with interrupt support
S32K3XX
S32K3xx Data Sheet
Supports S32K344, S32K324, S32K314, S32K312, S32K311, S32K310, 
S32K341, S32K342, S32K322, S32K328, S32K338, S32K348, S32K358 and 
S32K388. Data is preliminary for S32K389
Rev. 10 — 07/2024
Data Sheet: Technical Data
NXP reserves the right to change the detail specifications as may be required to 
permit improvements in the design of its products.


---
# 페이지 2

• Power management
— Low-power Arm Cortex-M7 core with excellent 
energy efficiency, balanced with performance
— Power Management Controller (PMC) with 
simplified mode management (RUN and 
STANDBY)
— Supports peripheral specific clock gating. Only 
specific peripherals remain working in low power 
modes.
• Communications interfaces
— Up to 16 serial communication interface (LPUART) 
modules, with LIN, UART and DMA support
— Up to six Low Power Serial Peripheral Interface 
(LPSPI) modules with DMA support
— Up to two Low Power Inter-Integrated Circuit 
(LPI2C) modules with DMA support
— Up to twelve FlexCAN modules (with optional CAN-
FD support)
— FlexIO module for flexible and high performance 
serial interfaces
— Up to two Ethernet modules
— Up to two Synchronous Audio Interface (SAI) 
modules
• Reliability, safety and security
— Hardware Security Engine (HSE_B) - Supports AES 
accelerator(for K388 and K389 only)
— Up to two Internal Software Watchdog Timers 
(SWT)
— Error-Correcting Code (ECC) on all memories
— Error Detection Code (EDC) on data path
— Cyclic Redundancy Check (CRC) module
— 120-bit Unique Identification (ID) number
— Extended Cross domain Domain Controller 
(XRDC), providing protection for master core 
access rights
— Virtualization Wrapper (VIRT_WRAPPER), 
providing I/O protection
• Debug functionality
— Serial Wire JTAG debug Port (SWJ-DP), with 2 pin 
Serial Wire Debug (SWD) for external debugger
— Debug Watchpoint and Trace (DWT), with four 
configurable comparators as hardware watchpoints
— Serial Wire Output (SWO)-synchronous trace data 
support
— Instrumentation Trace Macrocell (ITM) with 
software and hardware trace, plus time stamping
— CoreSight AHB Trace Macrocell (HTM)
— Flash Patch and Breakpoints (FPB) with ability to 
patch code and data from code space to system 
space
— Serial Wire Viewer (SWV): A trace capability 
providing displays of reads, writes, exceptions, PC 
Samples and print
— Full data trace for up to 16 output wide
— Embedded Cross Trigger (ECT) is used for 
multicore run-control and trace cross triggering, 
using CoreSight Cross Trigger Interface (CTI)
• Timing and control
— Up to three enhanced modular I/O system (eMIOS), 
offering up to 72 timer channels (IC/OC/PWM)
— Up to two System Timer Modules (STM)
— Up to two Logic Control Units (LCU)
— Full cross triggering support for ADC / timer (BCTU)
— One Trigger MUX Control (TRGMUX) module
— Up to three Periodic Interrupt Timer (PIT) modules
— 32-bit Real Time Counter (RTC) with autonomous 
periodic interrupt (API) function
NXP Semiconductors
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
2 / 152


---
# 페이지 3

Contents
1 
Overview............................................................ 5
2 
Block diagram.....................................................5
3 
Feature comparison......................................... 12
4 
Ordering information.........................................19
4.1 
Determining valid orderable parts ................ 19
5 
General.............................................................19
5.1 
Absolute maximum ratings............................20
5.2 
Voltage and current operating requirements.22
5.3 
Thermal operating characteristics.................24
5.4 
ESD and Latch-up Protection Characteristics
...................................................................... 24
6 
Power management......................................... 25
6.1 
Power mode transition operating behaviors..25
6.1.1 
Power mode transition operating behavior... 25
6.1.2 
Boot time, HSE firmware not installed.......... 26
6.1.3 
Boot time, HSE firmware installed................ 26
6.1.4 
HSE firmware memory verification time 
examples.......................................................27
6.2 
Supply Monitoring......................................... 31
6.3 
Recommended Decoupling Capacitors........ 33
6.3.1 
Recommended Decoupling Capacitor 
diagrams....................................................... 34
6.4 
V15 regulator (SMPS option) electrical 
specifications................................................ 48
6.5 
V15 regulator (BJT option, NPN ballast 
transistor control) electrical specifications.... 49
6.6 
V11 regulator (NMOS ballast transistor control) 
electrical specifications................................. 50
6.7 
Supply currents............................................. 50
6.8 
Operating mode............................................ 64
6.9 
Cyclic wake-up current .................................66
7 
I/O parameters................................................. 67
7.1 
GPIO DC electrical specifications, 3.3V Range 
(2.97V - 3.63V)..............................................67
7.2 
GPIO DC electrical specifications, 5.0V (4.5V - 
5.5V)............................................................. 71
7.3 
5.0V (4.5V - 5.5V) GPIO Output AC 
Specification..................................................75
7.4 
3.3V (2.97V - 3.63V) GPIO Output AC 
Specification..................................................77
8 
Glitch Filter....................................................... 79
9 
Flash memory specification..............................79
9.1 
Flash memory program and erase 
specifications................................................ 79
9.2 
Flash memory Array Integrity and Margin Read 
specifications................................................ 80
9.3 
Flash memory module life specifications...... 81
9.3.1 
Data retention vs program/erase cycles....... 82
9.4 
Flash memory AC timing specifications........ 82
9.5 
Flash memory read timing parameters......... 83
10 
Analog modules................................................84
10.1 
SAR_ADC..................................................... 84
10.2 
Supply Diagnosis.......................................... 86
10.3 
Low Power Comparator (LPCMP)................ 86
10.4 
Temperature Sensor..................................... 90
11 
Clocking modules............................................. 91
11.1 
FIRC..............................................................91
11.2 
SIRC............................................................. 91
11.3 
PLL................................................................91
11.4 
FXOSC..........................................................93
11.5 
SXOSC......................................................... 95
12 
Communication interfaces................................96
12.1 
LPSPI............................................................96
12.2 
LPSPI0 20 MHz and 15 MHz Combinations101
12.3 
LPSPI2 and LPSPI5 20MHz combination for 
S32K388 and S32K389.............................. 101
12.4 
Communication between two S32K388 
devices........................................................102
12.4.1 
Timing specification for S32K388 to S32K388 
communication............................................104
12.5 
I2C...............................................................104
12.6 
FlexCAN characteristics..............................104
12.7 
SAI electrical specifications........................ 104
12.7.1 
SAI Electrical Characteristics, Slave Mode.105
12.7.2 
SAI Electrical Characteristics, Master Mode106
12.8 
Ethernet characteristics.............................. 107
12.8.1 
Ethernet MII (10/100 Mbps)........................ 107
12.8.2 
Ethernet MII (200 Mbps)............................. 109
12.8.3 
Ethernet RMII (10/100 Mbps)......................111
12.8.4 
Ethernet RGMII........................................... 113
12.8.5 
MDIO timing specifications......................... 114
12.9 
QuadSPI..................................................... 115
12.9.1 
QuadSPI Quad 3.3V SDR 120MHz............ 115
12.9.2 
QuadSPI Octal 3.3V DDR 100MHz............ 117
12.9.3 
QuadSPI Quad 3.3V SDR 103.33MHz....... 118
12.9.4 
QuadSPI Octal 3.3V DDR 120MHz............ 119
12.9.5 
QuadSPI Quad 3.3V SDR 125MHz............ 120
12.10 
uSDHC........................................................121
12.10.1 
uSDHC SDR electrical specifications......... 121
12.10.2 
uSDHC DDR electrical specifications......... 123
12.11 
LPUART specifications............................... 124
13 
Debug modules.............................................. 124
13.1 
Debug trace timing specifications............... 124
13.2 
SWD electrical specifications......................125
13.3 
JTAG electrical specifications..................... 127
14 
Thermal Attributes.......................................... 129
14.1 
Description.................................................. 129
14.2 
Thermal characteristics...............................129
15 
Dimensions.....................................................132
15.1 
Obtaining package dimensions...................132


---
# 페이지 4

16 
Revision history.............................................. 132
Chapter 
Legal information............................................149


---
# 페이지 5

1 Overview
The S32K3xx product series further extends the highly-scalable portfolio of Arm ® Cortex ® - M0+/M4F S32K1xx chips in the 
automotive industry with the Arm Cortex-M7 core at higher frequency, more memory, ASIL-B and D rating and advanced security 
module. With a focus on automotive environment robustness, the S32K3xx product series devices are well suited to a wide range 
of applications in electrical harsh environments, and are optimized for cost-sensitive applications offering new, space saving 
package options. The S32K3xx series offers a broad range of memory, peripherals and performance options. Devices in this 
series share common peripherals and pin-out, allowing developers to migrate easily within a chip series or among other chip series 
to take advantage of more memory or feature integration.
 
S32K389 specific information is preliminary until this device is qualified and may change without notice.
  CAUTION  
2 Block diagram
The following figures show the S32K3xx product series block diagrams:
Fabric 
Memory
512 KB Pflash with ECC
64 KB Dflash with ECC
112 KB RAM with ECC
include 96 KB TCM
System
Debug/Trace (SWD/JTAG/ETB)
FXOSC (8-40MHz)
32ch ext. INT/WKUP
Security: HSE-B 
Symmetric Hardware Accelerators
Lifecycle
Management
XRDC
Access control
FIRC (48MHz)
SIRC (32KHz)
PLL
12ch DMA
Analog/Timers
2 x 24ch 12bit ADC
1 x LPCMP
2x24ch 16bit eMIOS Timer
BCTU (Body Control Trigger Unit)
LCU (Logic Control Unit)
MPU
CRC
FCCU
EIM/ERM
SWT
Functional Safety
CMU
STCU
Communication
4 x LPSPI
2 x LPI2C
Network
3 x FlexCAN, 
all ch support CAN FD
CPU Platform
Xbar (64bit)
Cortex-M0+
RAM
Single 
Core
Cortex-M7
FPU, DSP
120Mhz
I-Cache
D-cache 
16ch FlexIO
Emulating 
UART, I2C, SPI, 
I2S, SENT, PWM
4 x LPUART (LIN)
Asymmetric Hardware Accelerators
32bit RTC
TRNG/PRNG
Memory
•
OTA ready -
RWW, A/B swap
CPU Platform
•
 Scalable Arm M7
core in lockstep
•
Optimized for Real-
time with zero wait 
I/D-TCM
Network/ 
Communication
•
CAN/ CAN FD, LIN
•
Flexible IO emulation
Motor Control
•
On-chip motor 
control sub-
system
•
Offloading CPU
Security
•
HW accl for AES 256, 
RSA 4096, ECC 521
•
Firmware included, 
upgradable
•
Side-channel physical 
protection
•
Meet Evita Full 
function goal
•
•
•
•
•
Safety
HW redundancy
MBIST/LBIST/Self Test
Clock/Voltage monitor
Centralized error 
detection
ASIL B compliant
Future Proof Security/OTA
ISO26262 Compliant Safety System
Scalable Arm platform
Optimized for LOW power
Rich Network/Communication Interface
•
•
•
•
•
Figure 1. S32K310: ASIL B Single Core 512 KB General Purpose MCU
NXP Semiconductors
Overview
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
5 / 152


---
# 페이지 6

Xbar (64 bit)
Fabric
1 MB Pflash with ECC
Memory
3 x FlexCAN 
all ch support CAN FD
4 x LPUART (LIN)
Network
16 ch FlexIO 
Emulating 
UART, I2C, SPI 
I2S, SENT, PWM
Communication
64 kB Dflash with ECC
128 kB RAM with ECC 
Include 96 kB TCM
FXOSC (8-40 MHz)
Memory
OTA ready - 
RWW, A/B swap
•
CPU Platform
Single Arm M7 
core 
Optimized for Real- 
time with zero wait 
I/D-TCM
• 
•
Motor Control
On-chip motor 
control subsystem 
Offloading CPU
• 
•
Future Proof Security/OTA 
ISO26262 Compliant Safety System 
Scalable Arm platform 
Optimized for LOW power 
Rich Network/Communication Interface
• 
• 
• 
• 
•
Safety
HW redundancy 
MBIST/LBIST/Self Test 
Clock/Voltage monitor 
Centralized error 
detection 
ASIL B compliant
• 
• 
• 
• 
•
Security
HW accl for AES 256, 
RSA 4096, ECC 521 
Firmware included, 
upgradable 
Side-channel physical 
protection 
Meet Evita Full 
function goal
• 
• 
• 
•
Network/ 
Communication
CAN/CAN FD, LIN 
Flexible IO emulation
• 
•
System
FIRC (48 MHz)
CPU Platform
Cortex-M7
120 MHz
FPU, DSP
I-cache 
D-cache
Single Core
SIRC (32 KHz)
PLL
12ch DMA
32ch ext. INT/WKUP
4 x LPSPI
2 x LPI2C
Analog/Timers
BCTU (Body Control Trigger Unit)
2 x 24 ch 12 bit ADC
LCU (Logic Control Unit)
2 x 24 ch 16 bit eMIOS Timer
1 x LPCMP
32 bit RTC
Functional Safety
CMU
FCCU
MPU
SWT
EIM/ERM
STCU2
CRC
Security: HSE-B
Cortex-M0+
RAM
XRDC 
Access control
Lifecycle 
Management
Asymmetric Hardware Accelerators
Symmetric Hardware Accelerators
TRNG/PRNG
Debug/Trace (SWD/JTAG/ETB)
Figure 2. S32K311: ASIL B Single Core 1MB General Purpose MCU
Xbar (64 bit)
Fabric
2 MB Pflash with ECC
Memory
6 x FlexCAN 
all ch support CAN FD
8 x LPUART (LIN)
Network
32 ch FlexIO 
Emulating 
UART, I2C, SPI 
I2S, SENT, PWM
Communication
128 kB Dflash with ECC
192 kB RAM with ECC 
Include 96 kB TCM
FXOSC (8-40 MHz)
Memory
OTA ready - 
RWW, A/B swap
•
CPU Platform
Single Arm M7 
core 
Optimized for Real- 
time with zero wait 
I/D-TCM
• 
•
Motor Control
On-chip motor 
control subsystem 
Offloading CPU
• 
•
Future Proof Security/OTA 
ISO26262 Compliant Safety System 
Scalable Arm platform 
Optimized for LOW power 
Rich Network/Communication Interface
• 
• 
• 
• 
•
Safety
HW redundancy 
MBIST/LBIST/Self Test 
Clock/Voltage monitor 
Centralized error 
detection 
ASIL B compliant
• 
• 
• 
• 
•
Security
HW accl for AES 256, 
RSA 4096, ECC 521 
Firmware included, 
upgradable 
Side-channel physical 
protection 
Meet Evita Full 
function goal
• 
• 
• 
•
Network/ 
Communication
CAN/CAN FD, LIN 
Flexible IO emulation
• 
•
System
FIRC (48 MHz)
CPU Platform
Cortex-M7
120 MHz
FPU, DSP
I-cache 
D-cache
Single Core
SIRC (32 kHz)
SXOSC (32 kHz)
PLL
12ch DMA
32ch ext. INT/WKUP
4 x LPSPI
2 x LPI2C
Analog/Timers
BCTU (Body Control Trigger Unit)
2 x 24 ch 12 bit ADC
LCU (Logic Control Unit)
2 x 24 ch 16 bit eMIOS Timer
2 x LPCMP
Functional Safety
CMU
FCCU
MPU
SWT
EIM/ERM
STCU2
CRC
Security: HSE-B
Cortex-M0+
RAM
XRDC 
Access control
Lifecycle 
Management
Asymmetric Hardware Accelerators
Symmetric Hardware Accelerators
TRNG/PRNG
Debug/Trace (SWD/JTAG/ETB)
32-bit RTC
Figure 3. S32K312: ASIL B Single Core 2MB General Purpose MCU
NXP Semiconductors
Block diagram
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
6 / 152


---
# 페이지 7

Xbar (64 bit)
Fabric
2 MB Pflash with ECC
Memory
1 x QuadSPI 
Up to 480 Mbps 
4 bit data width
External Memory IF
1 x Ethernet, 100 Mbps 
AVB/TSN
4 x FlexCAN 
all ch support CAN FD
4 x LPUART (LIN)
Network
Communication
128 kB Dflash with ECC
256 kB RAM with ECC 
Include 192 kB TCM
FXOSC (8-40 MHz)
Memory
OTA ready - 
RWW, A/B swap 
External 
Flash/Ram 
expansion by 
QuadSPI
• 
•
CPU Platform
Two independent 
Arm M7 cores 
Optimized for Real- 
time with zero wait 
I/D-TCM
• 
•
Motor Control
On-chip motor 
control subsystem 
Offloading CPU
• 
•
Future Proof Security/OTA 
ISO26262 Compliant Safety System 
Scalable Arm platform 
Optimized for LOW power 
Rich Network/Communication Interface
• 
• 
• 
• 
•
Safety
HW redundancy 
MBIST/LBIST/Self Test 
Clock/Voltage monitor 
Centralized error 
detection 
ASIL B compliant
• 
• 
• 
• 
•
Security
HW accl for AES 256, 
RSA 4096, ECC 521 
Firmware included, 
upgradable 
Side-channel physical 
protection 
Meet Evita Full 
function goal
• 
• 
• 
•
Network/ 
Communication
Ethernet (TSN), CAN/ 
CAN FD, LIN 
SAI for Audio 
Flexible IO emulation
• 
• 
•
System
FIRC (48 MHz)
CPU Platform
Cortex-M7
160 MHz
FPU, DSP
I-cache 
D-cache
Cortex-M7
160 MHz
FPU, DSP
I-cache 
D-cache
Dual Core
SIRC (32 kHz)
SXOSC (32 kHz)
PLL
32ch DMA
32ch ext. INT/WKUP
Analog/Timers
BCTU (Body Control Trigger Unit)
2 x 24 ch 12 bit ADC
LCU (Logic Control Unit)
2 x 24 ch 16 bit eMIOS Timer
2 x LPCMP
Functional Safety
CMU
FCCU
MPU
SWT
EIM/ERM
STCU2
CRC
Security: HSE-B
Cortex-M0+
RAM
XRDC 
Access control
Lifecycle 
Management
Asymmetric Hardware Accelerators
Symmetric Hardware Accelerators
TRNG/PRNG
Debug/Trace (SWD/JTAG/ETB)
32 ch FlexIO 
Emulating 
UART, I2C, SPI 
I2S, SENT, PWM
4 x LPSPI
2 x LPI2C
2 x SAI (TDM, I2S)
32 bit RTC
 
Figure 4. S32K322: ASIL B Dual Core 2MB General Purpose MCU
Xbar (64 bit)
Fabric
1 MB Pflash with ECC
Memory
1 x QuadSPI
Up to 480 Mbps
4 bit data width
External Memory IF
1 x Ethernet, 100 Mbps
AVB/TSN
4 x FlexCAN
all ch support CAN FD
4 x LPUART (LIN)
Network
Communication
128 kB Dflash with ECC
256 kB RAM with ECC
Include 192 kB TCM
FXOSC (8-40 MHz)
Memory
OTA ready -
RWW, A/B swap
External
Flash/Ram
expansion by
QuadSPI
•
•
CPU Platform
Scalable Arm M7
core in Lockstep
Optimized for Real-
time with zero wait
I/D-TCM
•
•
Motor Control
On-chip motor
control subsystem
Offloading CPU
•
•
Future Proof Security/OTA
ISO26262 Compliant Safety System
Scalable Arm platform
Optimized for LOW power
Rich Network/Communication Interface
•
•
•
•
•
Safety
HW redundancy
MBIST/LBIST/Self Test
Clock/Voltage monitor
Centralized error
detection
ASIL D compliant
•
•
•
•
•
Security
HW accl for AES 256,
RSA 4096, ECC 521
Firmware included,
upgradable
Side-channel physical
protection
Meet Evita Full
function goal
•
•
•
•
Network/
Communication
Ethernet (TSN), CAN/
CAN FD, LIN
SAI for Audio
Flexible IO emulation
•
•
•
System
FIRC (48 MHz)
CPU Platform
Cortex-M7
160 MHz
FPU, DSP
I-cache
D-cache
Lockstep Core
SIRC (32 kHz)
SXOSC (32 kHz)
PLL
32ch DMA
32ch ext. INT/WKUP
Analog/Timers
BCTU (Body Control Trigger Unit)
2 x 24 ch 12 bit ADC
LCU (Logic Control Unit)
2 x 24 ch 16 bit eMIOS Timer
2 x LPCMP
Functional Safety
CMU
FCCU
MPU
SWT
EIM/ERM
STCU2
CRC
Security: HSE-B
Cortex-M0+
RAM
XRDC
Access control
Lifecycle
Management
Asymmetric Hardware Accelerators
Symmetric Hardware Accelerators
TRNG/PRNG
Debug/Trace (SWD/JTAG/ETB)
32 ch FlexIO
Emulating
UART, I2C, SPI
I2S, SENT, PWM
4 x LPSPI
2 x LPI2C
2 x SAI (TDM, I2S)
Cortex-M7
160 MHz
FPU, DSP
I-cache
D-cache
32 bit RTC
Figure 5. S32K341: ASIL D Lockstep Core 1MB General Purpose MCU
NXP Semiconductors
Block diagram
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
7 / 152


---
# 페이지 8

Xbar (64 bit)
Fabric
2 MB Pflash with ECC
Memory
1 x QuadSPI 
Up to 480 Mbps 
4 bit data width
External Memory IF
1 x Ethernet, 100 Mbps 
AVB/TSN
4 x FlexCAN 
all ch support CAN FD
4 x LPUART (LIN)
Network
Communication
128 kB Dflash with ECC
256 kB RAM with ECC 
Include 192 kB TCM
FXOSC (8-40 MHz)
Memory
OTA ready - 
RWW, A/B swap 
External 
Flash/Ram 
expansion by 
QuadSPI
• 
•
CPU Platform
Scalable Arm M7 
core in Lockstep 
Optimized for Real- 
time with zero wait 
I/D-TCM
• 
•
Motor Control
On-chip motor 
control subsystem 
Offloading CPU
• 
•
Future Proof Security/OTA 
ISO26262 Compliant Safety System 
Scalable Arm platform 
Optimized for LOW power 
Rich Network/Communication Interface
• 
• 
• 
• 
•
Safety
HW redundancy 
MBIST/LBIST/Self Test 
Clock/Voltage monitor 
Centralized error 
detection 
ASIL D compliant
• 
• 
• 
• 
•
Security
HW accl for AES 256, 
RSA 4096, ECC 521 
Firmware included, 
upgradable 
Side-channel physical 
protection 
Meet Evita Full 
function goal
• 
• 
• 
•
Network/ 
Communication
Ethernet (TSN), CAN/ 
CAN FD, LIN 
SAI for Audio 
Flexible IO emulation
• 
• 
•
System
FIRC (48 MHz)
CPU Platform
Cortex-M7
160 MHz
FPU, DSP
I-cache 
D-cache
Lockstep Core
SIRC (32 kHz)
SXOSC (32 kHz)
PLL
32ch DMA
32ch ext. INT/WUP
Analog/Timers
BCTU (Body Control Trigger Unit)
2 x 24 ch 12 bit ADC
LCU (Logic Control Unit)
2 x 24 ch 16 bit eMIOS Timer
2 x LPCMP
Functional Safety
CMU
FCCU
MPU
SWT
EIM/ERM
STCU2
CRC
Security: HSE-B
Cortex-M0+
RAM
XRDC 
Access control
Lifecycle 
Management
Asymmetric Hardware Accelerators
Symmetric Hardware Accelerators
TRNG/PRNG
Debug/Trace (SWD/JTAG/ETB)
32 ch FlexIO 
Emulating 
UART, I2C, SPI 
I2S, SENT, PWM
4 x LPSPI
2 x LPI2C
2 x SAI (TDM, I2S)
Cortex-M7
160 MHz
FPU, DSP
I-cache 
D-cache
32 bit RTC
Figure 6. S32K342: ASIL D Lockstep Core 2MB General Purpose MCU
Xbar (64 bit)
Fabric
4 MB Pflash with ECC
Memory
1 x QuadSPI 
Up to 480 Mbps 
4 bit data width
External Memory IF
1 x Ethernet, 100 Mbps 
AVB/TSN
6 x FlexCAN 
all ch support CAN FD
16 x LPUART (LIN)
Network
32 ch FlexIO 
Emulating 
UART, I2C, SPI 
I2S, SENT, PWM
Communication
128 kB Dflash with ECC
512 kB RAM with ECC 
Include 96 kB TCM
FXOSC (8-40 MHz)
Memory
OTA ready - 
RWW, A/B swap 
External 
Flash/Ram 
expansion by 
QuadSPI
• 
•
CPU Platform
Single Arm M7 
core 
Optimized for Real- 
time with zero wait 
I/D-TCM
• 
•
Motor Control
On-chip motor 
control subsystem 
Offloading CPU
• 
•
Future Proof Security/OTA 
ISO26262 Compliant Safety System 
Scalable Arm platform 
Optimized for LOW power 
Rich Network/Communication Interface
• 
• 
• 
• 
•
Safety
HW redundancy 
MBIST/LBIST/Self Test 
Clock/Voltage monitor 
Centralized error 
detection 
ASIL B compliant
• 
• 
• 
• 
•
Security
HW accl for AES 256, 
RSA 4096, ECC 521 
Firmware included, 
upgradable 
Side-channel physical 
protection 
Meet Evita Full 
function goal
• 
• 
• 
•
Network/ 
Communication
Ethernet (TSN), CAN/ 
CAN FD, LIN 
SAI for Audio 
Flexible IO emulation
• 
• 
•
System
FIRC (48 MHz)
CPU Platform
Cortex-M7
160 MHz
FPU, DSP
I-cache 
D-cache
Single Core
SIRC (32 kHz)
SXOSC (32 kHz)
PLL
32ch DMA
32ch ext. INT/WKUP
6 x LPSPI
2 x LPI2C
2 x SAI (TDM, I2S)
Analog/Timers
BCTU (Body Control Trigger Unit)
3 x 24 ch 12 bit ADC
LCU (Logic Control Unit)
3 x 24 ch 16 bit eMIOS Timer
3 x LPCMP
Functional Safety
CMU
FCCU
MPU
SWT
EIM/ERM
STCU2
CRC
Security: HSE-B
Cortex-M0+
RAM
XRDC 
Access control
Lifecycle 
Management
Asymmetric Hardware Accelerators
Symmetric Hardware Accelerators
TRNG/PRNG
Debug/Trace (SWD/JTAG/ETB)
32 bit RTC
Figure 7. S32K314: ASIL B Single Core 4MB General Purpose MCU
NXP Semiconductors
Block diagram
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
8 / 152


---
# 페이지 9

Xbar (64 bit)
Fabric
4 MB Pflash with ECC
Memory
1 x QuadSPI 
Up to 480 Mbps 
4 bit data width
External Memory IF
1 x Ethernet, 100 Mbps 
AVB/TSN
6 x FlexCAN 
all ch support CAN FD
16 x LPUART (LIN)
Network
32 ch FlexIO 
Emulating 
UART, I2C, SPI 
I2S, SENT, PWM
Communication
128 kB Dflash with ECC
512 kB RAM with ECC 
Include 192 kB TCM
FXOSC (8-40 MHz)
Memory
OTA ready - 
RWW, A/B swap 
External 
Flash/Ram 
expansion by 
QuadSPI
• 
•
CPU Platform
Two independent 
Arm M7 cores 
Optimized for Real- 
time with zero wait 
I/D-TCM
• 
•
Motor Control
On-chip motor 
control subsystem 
Offloading CPU
• 
•
Future Proof Security/OTA 
ISO26262 Compliant Safety System 
Scalable Arm platform 
Optimized for LOW power 
Rich Network/Communication Interface
• 
• 
• 
• 
•
Safety
HW redundancy 
MBIST/LBIST/Self Test 
Clock/Voltage monitor 
Centralized error 
detection 
ASIL B compliant
• 
• 
• 
• 
•
Security
HW accl for AES 256, 
RSA 4096, ECC 521 
Firmware included, 
upgradable 
Side-channel physical 
protection 
Meet Evita Full 
function goal
• 
• 
• 
•
Network/ 
Communication
Ethernet (TSN), CAN/ 
CAN FD, LIN 
SAI for Audio 
Flexible IO emulation
• 
• 
•
System
FIRC (48 MHz)
CPU Platform
Cortex-M7
160 MHz
FPU, DSP
I-cache 
D-cache
Dual Core
SIRC (32 kHz)
SXOSC (32 kHz)
PLL
32ch DMAMUX
32ch ext. INT/WKUP
6 x LPSPI
2 x LPI2C
2 x SAI (TDM, I2S)
Analog/Timers
BCTU (Body Control Trigger Unit)
3 x 24 ch 12 bit ADC
LCU (Logic Control Unit)
3 x 24 ch 16 bit eMIOS Timer
3 x LPCMP
Functional Safety
CMU
FCCU
MPU
SWT
EIM/ERM
STCU2
CRC
Security: HSE-B
Cortex-M0+
RAM
XRDC 
Access control
Lifecycle 
Management
Asymmetric Hardware Accelerators
Symmetric Hardware Accelerators
TRNG/PRNG
Debug/Trace (SWD/JTAG/ETB)
Cortex-M7
160 MHz
FPU, DSP
I-cache 
D-cache
32 bit RTC
Figure 8. S32K324: ASIL B Dual Core 4MB General Purpose MCU
Xbar (64 bit)
Fabric
4 MB Pflash with ECC
Memory
1 x QuadSPI 
Up to 480 Mbps 
4 bit data width
External Memory IF
1 x Ethernet, 100 Mbps 
AVB/TSN
6 x FlexCAN 
all ch support CAN FD
16 x LPUART (LIN)
Network
32 ch FlexIO 
Emulating 
UART, I2C, SPI 
I2S, SENT, PWM
Communication
128 kB Dflash with ECC
512 kB RAM with ECC 
Include 192 kB TCM
FXOSC (8-40 MHz)
Memory
OTA ready - 
RWW, A/B swap 
External 
Flash/Ram 
expansion by 
QuadSPI
• 
•
CPU Platform
Scalable Arm M7 
core in Lockstep 
Optimized for Real- 
time with zero wait 
I/D-TCM
• 
•
Motor Control
On-chip motor 
control subsystem 
Offloading CPU
Future Proof Security/OTA 
ISO26262 Compliant Safety System 
Scalable Arm platform 
Optimized for LOW power 
Rich Network/Communication Interface
• 
• 
• 
• 
•
Safety
HW redundancy 
MBIST/LBIST/Self Test 
Clock/Voltage monitor 
Centralized error 
detection 
ASIL D compliant
• 
• 
• 
• 
•
Security
HW accl for AES 256, 
RSA 4096, ECC 521 
Firmware included, 
upgradable 
Side-channel physical 
protection 
Meet Evita Full 
function goal
• 
• 
• 
•
Network/ 
Communication
Ethernet (TSN), CAN/ 
CAN FD, LIN 
SAI for Audio 
Flexible IO emulation
• 
• 
•
System
FIRC (48 MHz)
CPU Platform
Cortex-M7
160 MHz
FPU, DSP
I-cache 
D-cache
Cortex-M7
160 MHz
FPU, DSP
I-cache 
D-cache
Lockstep Core
SIRC (32 kHz)
SXOSC (32 kHz)
PLL
32ch DMA and DMAMUX
32ch ext. INT/WUP
6 x LPSPI
2 x LPI2C
2 x SAI (TDM, I2S)
Analog/Timers
BCTU (Body Control Trigger Unit)
3 x 24 ch 12 bit ADC
LCU(Logic Control Unit)
3 x 24 ch 16 bit eMIOS Timer
3 x LPCMP
Functional Safety
CMU
FCCU
MPU
SWT
EIM/ERM
STCU2
CRC
Security: HSE-B
Cortex-M0+
RAM
XRDC 
Access control
Lifecycle 
Management
Asymmetric Hardware Accelerators
Symmetric Hardware Accelerators
TRNG/PRNG
Debug/Trace (SWD/JTAG/ETB)
32 bit RTC
Figure 9. S32K344: ASIL D Lockstep Core 4MB General Purpose MCU
NXP Semiconductors
Block diagram
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
9 / 152


---
# 페이지 10

Xbar (64 bit)
Fabric
8 MB Pflash with ECC
Memory
External Memory IF
1 x Ethernet, 1 Gbps
AVB/TSN
8 x FlexCAN
all ch support CAN FD
16 x LPUART (LIN)
Network
32 ch FlexIO
Emulating
UART, I2C, SPI
I2S, SENT, PWM
Communication
128 kB Dflash with ECC
1152 kB RAM with ECC
Include 192 kB TCM
FXOSC (8-40 MHz)
Memory
OTA ready -
RWW, A/B swap
External
Flash/Ram
expansion by
QuadSPI
•
•
CPU Platform
Two independent
Arm M7 cores
Optimized for Real-
time with zero wait
I/D-TCM
•
•
Motor Control
On-chip motor
control subsystem
Offloading CPU
•
•
Future Proof Security/OTA
ISO26262 Compliant Safety System
Scalable Arm platform
Optimized for LOW power
Rich Network/Communication Interface
•
•
•
•
•
Safety
HW redundancy
MBIST/LBIST/Self Test
Clock/Voltage monitor
Centralized error
detection
ASIL B compliant
•
•
•
•
•
Security
HW accl for AES 256,
RSA 4096, ECC 521
Firmware included,
upgradable
Side-channel physical
protection
Meet Evita Full
function goal
•
•
•
•
Network/
Communication
Ethernet (TSN), CAN/
CAN FD, LIN
SAI for Audio
Flexible IO emulation
•
•
•
System
FIRC (48 MHz)
CPU Platform
Cortex-M7
240 MHz
FPU, DSP
I-cache
D-cache
SIRC (32 kHz)
SXOSC (32 kHz)
2 x PLL
32ch DMAMUX
32ch ext. INT/WKUP
6 x LPSPI
2 x LPI2C
2 x SAI (TDM, I2S)
Analog/Timers
BCTU (Body Control Trigger Unit)
3 x 24 ch 12 bit ADC
LCU (Logic Control Unit)
3 x 24 ch 16 bit eMIOS Timer
3 x LPCMP
Functional Safety
CMU
FCCU
MPU
SWT
EIM/ERM
STCU2
CRC
Security: HSE-B
Cortex-M0+
RAM
XRDC
Access control
Lifecycle
Management
Asymmetric Hardware Accelerators
Symmetric Hardware Accelerators
TRNG/PRNG
Debug/Trace (SWD/JTAG/ETB)
Cortex-M7
240 MHz
FPU, DSP
I-cache
D-cache
1 x QuadSPI
Up to 2 Gbps 
8 bit data width
1 x uSDHC
 
32 bit RTC
Figure 10. S32K328: ASIL B Dual Core 8MB General Purpose MCU
Xbar (64 bit)
Fabric
8 MB Pflash with ECC
Memory
External Memory IF
1 x Ethernet, 1 Gbps 
AVB/TSN
8 x FlexCAN 
all ch support CAN FD
16 x LPUART (LIN)
Network
32 ch FlexIO 
Emulating 
UART, I2C, SPI 
I2S, SENT, PWM
Communication
128 kB Dflash with ECC
1152 kB RAM with ECC 
Include 384 kB TCM
FXOSC (8-40 MHz)
Memory
OTA ready - 
RWW, A/B swap 
External 
Flash/Ram 
expansion by 
QuadSPI
• 
•
CPU Platform
Three independent 
Arm M7 cores 
Optimized for Real- 
time with zero wait 
I/D-TCM
• 
•
Motor Control
On-chip motor 
control subsystem 
Offloading CPU
• 
•
Future Proof Security/OTA 
ISO26262 Compliant Safety System 
Scalable Arm platform 
Optimized for LOW power 
Rich Network/Communication Interface
• 
• 
• 
• 
•
Safety
HW redundancy 
MBIST/LBIST/Self Test 
Clock/Voltage monitor 
Centralized error 
detection 
ASIL D compliant
• 
• 
• 
• 
•
Security
HW accl for AES 256, 
RSA 4096, ECC 521 
Firmware included, 
upgradable 
Side-channel physical 
protection 
Meet Evita Full 
function goal
• 
• 
• 
•
Network/ 
Communication
Ethernet (TSN), CAN/ 
CAN FD, LIN 
SAI for Audio 
Flexible IO emulation
• 
• 
•
System
FIRC (48 MHz)
CPU Platform
SIRC (32 kHz)
SXOSC (32 kHz)
2 x PLL
32ch DMA and DMAMUX
32ch ext. INT/WKUP
6 x LPSPI
2 x LPI2C
2 x SAI (TDM, I2S)
Analog/Timers
BCTU (Body Control Trigger Unit)
3 x 24 ch 12 bit ADC
LCU (Logic Control Unitl
3 x 24 ch 16 bit eMIOS Timer
3 x LPCMP
Functional Safety
CMU
FCCU
MPU
SWT
EIM/ERM
STCU2
CRC
Security: HSE-B
Cortex-M0+
RAM
XRDC 
Access control
Lifecycle 
Management
Asymmetric Hardware Accelerators
Symmetric Hardware Accelerators
TRNG/PRNG
Debug/Trace (SWD/JTAG/ETB)
Cortex-M7
240 MHz
FPU, DSP
I-cache 
D-cache
Cortex-M7
240 MHz
FPU, DSP
I-cache 
D-cache
Cortex-M7
240 MHz
FPU, DSP
I-cache 
D-cache
1 x QuadSPI
Up to 2 Gbps 
8 bit data width
1 x uSDHC
 
32 bit RTC
Figure 11. S32K338: ASIL B Three Core 8MB General Purpose MCU
NXP Semiconductors
Block diagram
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
10 / 152


---
# 페이지 11

Xbar (64 bit)
Fabric
8 MB Pflash with ECC
Memory
External Memory IF
1 x Ethernet, 1 Gbps
AVB/TSN
8 x FlexCAN
all ch support CAN FD
16 x LPUART (LIN)
Network
32 ch FlexIO
Emulating
UART, I2C, SPI
I2S, SENT, PWM
Communication
128 kB Dflash with ECC
1152 kB RAM with ECC
Include 192 kB TCM
FXOSC (8-40 MHz)
Memory
OTA ready -
RWW, A/B swap
External
Flash/Ram
expansion by
QuadSPI
•
•
CPU Platform
Arm M7 cores in
lockstep
Optimized for Real-
time with zero wait
I/D-TCM
•
•
Motor Control
On-chip motor
control subsystem
Offloading CPU
•
•
Future Proof Security/OTA
ISO26262 Compliant Safety System
Scalable Arm platform
Optimized for LOW power
Rich Network/Communication Interface
•
•
•
•
•
Safety
HW redundancy
MBIST/LBIST/Self Test
Clock/Voltage monitor
Centralized error
detection
ASIL D compliant
•
•
•
•
•
Security
HW accl for AES 256,
RSA 4096, ECC 521
Firmware included,
upgradable
Side-channel physical
protection
Meet Evita Full
function goal
•
•
•
•
Network/
Communication
Ethernet (TSN), CAN/
CAN FD, LIN
SAI for Audio
Flexible IO emulation
•
•
•
System
FIRC (48 MHz)
CPU Platform
Cortex-M7
240 MHz
FPU, DSP
I-cache
D-cache
Cortex-M7
240 MHz
FPU, DSP
I-cache
D-cache
Lockstep Core
SIRC (32 kHz)
SXOSC (32 kHz)
2 x PLL
32ch DMA and DMAMUX
32ch ext. INT/WKUP
6 x LPSPI
2 x LPI2C
2 x SAI (TDM, I2S)
Analog/Timers
BCTU (Body Control Trigger Unit)
3 x 24 ch 12 bit ADC
LCU (Logic Control Unit)
3 x 24 ch 16 bit eMIOS Timer
3 x LPCMP
Functional Safety
CMU
FCCU
MPU
SWT
EIM/ERM
STCU2
CRC
Security: HSE-B
Cortex-M0+
RAM
XRDC
Access control
Lifecycle
Management
Asymmetric Hardware Accelerators
Symmetric Hardware Accelerators
TRNG/PRNG
Debug/Trace (SWD/JTAG/ETB)
1 x QuadSPI
Up to 2 Gbps 
8 bit data width
32 bit RTC
1 x uSDHC
 
Figure 12. S32K348: ASIL D Lockstep Core 8MB General Purpose MCU
Xbar (64 bit)
Fabric
8 MB Pflash with ECC
Memory
External Memory IF
1 x Ethernet, 1 Gbps 
AVB/TSN
8 x FlexCAN 
all ch support CAN FD
16 x LPUART (LIN)
Network
32 ch FlexIO 
Emulating 
UART, I2C, SPI 
I2S, SENT, PWM
Communication
128 kB Dflash with ECC
1152 kB RAM with ECC 
Include 384 kB TCM
FXOSC (8-40 MHz)
Memory
OTA ready - 
RWW, A/B swap 
External 
Flash/Ram 
expansion by 
QuadSPI
• 
•
CPU Platform
Arm M7 cores in 
lockstep 
One independent 
Arm M7 for real 
time processing 
Optimized for Real- 
time with zero wait 
I/D-TCM
• 
• 
•
Motor Control
On-chip motor 
control subsystem 
Offloading CPU
• 
•
Future Proof Security/OTA 
ISO26262 Compliant Safety System 
Scalable Arm platform 
Optimized for LOW power 
Rich Network/Communication Interface
• 
• 
• 
• 
•
Safety
HW redundancy 
MBIST/LBIST/Self Test 
Clock/Voltage monitor 
Centralized error 
detection 
ASIL D compliant
• 
• 
• 
• 
•
Security
HW accl for AES 256, 
RSA 4096, ECC 521 
Firmware included, 
upgradable 
Side-channel physical 
protection 
Meet Evita Full 
function goal
• 
• 
• 
•
Network/ 
Communication
Ethernet (TSN), CAN/ 
CAN FD, LIN 
SAI for Audio 
Flexible IO emulation
• 
• 
•
System
FIRC (48 MHz)
CPU Platform
Cortex-M7
240 MHz
FPU, DSP
I-cache 
D-cache
Cortex-M7
240 MHz
FPU, DSP
I-cache 
D-cache
Lockstep Core
SIRC (32 kHz)
SXOSC (32 kHz)
2 x PLL
32ch DMA
32ch ext. INT/WKUP
6 x LPSPI
2 x LPI2C
2 x SAI (TDM, I2S)
Analog/Timers
BCTU (Body Control Trigger Unit)
3 x 24 ch 12 bit ADC
LCU (Logic Control Unit)
3 x 24 ch 16 bit eMIOS Timer
3 x LPCMP
Functional Safety
CMU
FCCU
MPU
SWT
EIM/ERM
STCU2
CRC
Security: HSE-B
Cortex-M0+
RAM
XRDC 
Access control
Lifecycle 
Management
Asymmetric Hardware Accelerators
Symmetric Hardware Accelerators
TRNG/PRNG
Debug/Trace (SWD/JTAG/ETB)
Cortex-M7
240 MHz
FPU, DSP
I-cache 
D-cache
 
1 x uSDHC
 
32 bit RTC
1 x QuadSPI
Upto 2 Gbps
8 bit data width
Figure 13. S32K358: ASIL D Lockstep Core + One, 8MB General Purpose MCU
NXP Semiconductors
Block diagram
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
11 / 152


---
# 페이지 12

Fabric
Memory
8 MB Pflash with ECC
128 KB Dflash with ECC
1152 KB RAM with ECC
Incl 384 KB TCM
System
Debug/Trace (SWD/JTAG/ETB)
FXOSC (8- 40MHz)
32ch ext. INT/WUP
Security: HSE-B
Asymmetric Hardware Accelerators
Symmetric Hardware Accelerators
Lifecycle 
Management
XRDC
Access control
FIRC (48MHz)
SIRC (32KHz)
SXOSC (32KHz)
2 x PLL
32ch DMA
Analog/Timers
3 x 24ch 12bit ADC
3x24ch 16bit eMIOS Timer
BCTU (Body Control Trigger Unit)
LCU (Logic Control Unit)
MPU
CRC
FCCU
EIM/ERM
SWT
Functional Safety
CMU
STCU
External Memory IF
Communication
6 x LPSPI
2 x LPI2C
2 x SAI (TDM, I2S)
Network
8 x FlexCAN,
all ch support CAN FD
2 x Ethernet, 1Gbps
AVB/TSN
Xbar (64bit)
Cortex- M0+
RAM
32ch FlexIO
Emulating
UART, I2C, SPI,
I2S, SENT, PWM
16 x LPUART (LIN)
TRNG/PRNG
3x LPCMP
CPU Platform
Lock- Step or Split- Lock
Permanent Lock
AES Accelerator
Dedicated to Communications
AES Accelerator 
optimized for
Low Latency
Performance
Cortex-M7
300 MHz
FPU, DSP
I-cache
D-cache
Cortex-M7
320 MHz
FPU, DSP
I-cache
D-cache
Cortex-M7
320 MHz
FPU, DSP
I-cache
D-cache
Cortex-M7
320 MHz
FPU, DSP
I-cache
D-cache
Cortex-M7
320 MHz
FPU, DSP
I-cache
D-cache
32 bit RTC
1 x QuadSPI
 
4 bit data width
Figure 14. S32K388: ASIL D 8MB MCU
Fabric
Memory
12 MB Pflash with ECC
256 KB Dflash with ECC
2.25MB SRAM with ECC
System
Debug/Trace (SWD/JTAG/ETB)
FXOSC (8-40MHz)
32ch ext. INT/WUP
Security: HSE-B
Asymmetric Hardware Accelerators
Symmetric Hardware Accelerators
Lifecycle
Management
XRDC
Access control
FIRC (48MHz)
SIRC (32KHz)
SXOSC (32KHz)
PLL
32ch DMA
Analog/Timers
3 x 24ch 12bit ADC
3x24ch 24bit eMIOSTimer
BCTU (Body Control Trigger Unit)
LCU (Logic Control Unit)
MPU
CRC
FCCU
EIM/ERM
SWT
Functional Safety
CMU
STCU
External Memory IF
1 x QuadSPI
4bit data width
Communication
6 x LPSPI
2 x LPI2C
2 x SAI (TDM, I2S)
Network
12x FlexCAN,
all ch support CAN FD
2 x Ethernet, 1Gbps
AVB/TSN
Xbar (64bit)
Cortex-M0+
RAM
32ch FlexIO
Emulating
UART, I2C, SPI,
I2S, SENT, PWM
16 x LPUART (LIN)
TRNG/PRNG
3x LPCMP
CPU Platform
Cortex-M7
32kB I-cache
NEON
32kB D-
32kB TCM32kB TCM
Cortex-M7
16 KB I-cache
16 KB D-cache
TCM: 32K-I, 64K-D
Cortex-M7
16 KB I-cache 16 KB D-cache
TCM: 32K-I, 64K-D
DP-FPU, DSP
DP-FPU, DSP
Lock-Step or Split-Lock
Permanent Lock
16 KB I-cache
Cortex-M7
32 KB I-
32 KB D-cache
TCM: 32K-I, 64K-D
DP-FPU, DSP
16 KB I-cache 16 KB D-cache
16 KB I-cache
Cortex-M7
32 KB I-cache
32 KB D-cache
TCM: 32K-I, 64K-D
DP-FPU, DSP
16 KB I-cache 16 KB D-
16 KB I-cache
AES Accelerator
Dedicated to Communications
+FLEXCANs
+FLASH
+SRAM
437BGA Package
Figure 15. S32K389: ASIL D 12MB MCU
3 Feature comparison
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
NXP Semiconductors
Feature comparison
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
12 / 152


---
# 페이지 13

• S32K348
• S32K358
• S32K388
• S32K389
NXP Semiconductors
Feature comparison
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
13 / 152


---
# 페이지 14

Table 1. S32K3xx chip's feature comparison
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
B
D
B
D
B
B
D
D
D
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
8 MB
12 MB
Data flash 
memory 
(KB)
64
64
128
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
1152KB 
(incl. 
384KB 
TCM)
1152KB 
incl. 
384KB 
TCM)
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
1xM7 LS+3xM7 or 
2xM7 LS+1xM7
Frequenc
y (MHz)
120
160
240
320
300
DMA 
channels
12
32
32
32
ASIL–B 
DMIPS 2 3
277–387-760
739–
1033-
2028
—
369–
516-
1014
739–
1033-
2028
—
1108-
1550-
3043
1663–
2325-
4564
—
554–
775-
1521
739-
1033-
2028 4
693-
969-
19024
Table continues on the next page...
NXP Semiconductors
Feature comparison
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
14 / 152


---
# 페이지 15

Table 1. S32K3xx chip's feature comparison (continued)
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
2217-
3100-
6086 5
2079-
2907-
5706 5
ASIL–D 
DMIPS 2 3
—
369–516-1014
—
369–
516-
1014
—
554–
775-
1521
775-
1521-
1269
1478-
2066-
4057 4
739-
1033-
2028 5
1386-
1938-
38044
693-
969-
1902 5
ASIL–B 
CoreMark 
score 2 6
634
1692
—
846
1692
—
2539
3808
—
1269
1692 4
5078 5
1587 4
4761 5
ASIL–D 
CoreMark 
score 2 6
—
846
—
846
—
1269
1269
3385 4
1692 5
31744
15875
FlexCAN 
instances
3
6
4
6
8
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
LPUART 
instances
4
8
4
16
Table continues on the next page...
NXP Semiconductors
Feature comparison
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
15 / 152


---
# 페이지 16

Table 1. S32K3xx chip's feature comparison (continued)
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
3
LPCMP 
instances
1
2
3
3
PIT 
instances
2
3
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
LCU 
instances
2
Table continues on the next page...
NXP Semiconductors
Feature comparison
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
16 / 152


---
# 페이지 17

Table 1. S32K3xx chip's feature comparison (continued)
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
100-
HDQFP 
package
Yes
No
Table continues on the next page...
NXP Semiconductors
Feature comparison
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
17 / 152


---
# 페이지 18

Table 1. S32K3xx chip's feature comparison (continued)
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
Feature comparison
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
18 / 152
—


---
# 페이지 19

4 Ordering information
Figure 16. Ordering information
Product status
Product status for ordering and marking
P: Prototype
S: Qualified ordering P/N
Extra feature
Security
Product type/brand
32: Automotive 32-bit MCU/MPU
Tx: Global foundry
x0: 1st mask revision
x1: 2nd mask revision
Product line
K: General purpose MCU
S: Standard family SW package, including:
I: ISELED SW licensed + standard family SW package
additional solution specific SW TBD
Memory size
P-Flash 512 kB 1 MB 2 MB 4 MB
0
1
2
4
6 MB 8 MB
6
8
12 MB
9
Series/family
3: K3 product family/Arm  CortexM7 based
Core platform
1: 1 x M7 core
2: 2 x M7 cores
3: 3 x M7 cores
4: 1 x M7 lockstep core
5: 1 x M7 lockstep core plus 1 x M7 core
6: 1 x M7 LS core + 1 x M7 core + DSP + 2 x eTPU
7: 1 x M7 LS core + 2 x M7 split-lock cores + DSP
8: 2 x M7 lockstep + 1 x M7 core or 1 x M7 lockstep +
9: 1 x M7 LS core + 2 x M7 split-lock cores  + 1 x DSP +
P/S
32
K
3
9
6
E
H
T0
M
JB
S
T
Product type/brand
Product line
Series/family
Core platform
Memory size
Features
Security
Fab and mask rev letter
Fab and mask rev letter
V: -40 °C to 105 °C
M: -40 °C to 125 °C
Ambient temperature (Ta)
Temperature suffix
Package suffix
Software
configuration
Tape and reel
Indicator
H
HSE B standard
security
G, V
Premium security
Package suffix
Software configuration
T: Trays/tubes
R: Tape and reel
Tape and reel
48
100
172
176
257
289
437
MM
JB
JG
PA
PB
PC
pins
MaxQFP-EP
MaxQFP
BGA
N
E
No ethernet
MAC
100 Mbps ethernet
MAC
G
1 Gbps
ethernet MAC
H
2 x 1 Gbps
ethernet MAC
LF
KU
LQFP
· Real time driver including Autosar MCAL
and non Autosar driver package (ISO26262 
compliant, crypto driver included)
Standard security firmware
Safety peripheral driver (SPD)
Inter-core communication framework (IPCF)
· 
· 
· 
2 x eTPU
3 x M7 cores
4.1 Determining valid orderable parts
To determine the orderable part numbers for this device, please contact NXP sales representative.
5 General
NXP Semiconductors
Ordering information
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
19 / 152


---
# 페이지 20

5.1 Absolute maximum ratings
 
When the MCU is in an unpowered state, current injected through the chip pins may bias internal chip structures 
(for example, ESD diodes) and incorrectly power up these internal structures through inadvertent paths. The 
presence of such residual voltage may influence different chip-internal blocks in an unpredictable manner and 
may ultimately result in unpredictable chip behavior (for example, POR flag not set). Once in the illegal state, 
powering up the chip further and then applying reset will clear the illegal state. Injection current specified for the 
chip under the aspect of absolute maximum ratings represent the capability of the internal circuitry to withstand 
such condition without causing physical damage. Functional operation of the chip under conditions - specified 
as absolute maximum ratings - is not implied.
  CAUTION  
 
Functional operating conditions appear in the DC electrical characteristics. Absolute maximum ratings are stress 
ratings only, and functional operation at the maximum values is not guaranteed. See footnotes in the following table 
for specific conditions. Stress beyond the listed maximum values may affect device reliability or cause permanent 
damage to the device. All the limits defined in the datasheet specification must be honored together and any 
violation to any one or more will not guarantee desired operation. Unless otherwise specified, all maximum and 
minimum values in the datasheet are across process, voltage, and temperature.
  NOTE  
The VDD_HV_B and V15 voltage supply domains are only present in certain devices and packages 
(S32K388, S32K389, S32K358, S32K348, S32K338, S32K328, S32K344, S32K324, S32K314, S32K342, S32K341, S32K322).
The VDD_DCDC supply voltage is only present in certain devices and packages (S32K358, S32K348, S32K338, S32K328, 
S32K388 and S32K389).
Table 2. Absolute maximum ratings
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
VDD_HV_A
Main I/O and 
analog supply 
voltage 1,2
-0.3
—
6.0
V
—
—
VDD_HV_B
Secondary I/O 
supply voltage 1,2
-0.3
—
6.0
V
—
—
VDD_DCDC
Supply voltage for 
the SMPS gate 
driver 1,2,3
-0.3
—
6.0
V
—
—
V15
Voltage sensing 
input 1,2
-0.3
—
2.75
V
For S32K388 and 
S32K389
—
V15
High-current 
logic supply 
voltage 1,2
-0.3
—
2.75
V
For S32K358, 
S32K348, S32K338 
and S32K328
—
V15
High-current 
logic supply 
voltage 1,2
-0.3
—
6.0
V
For all S32K3xx 
variants except 
S32K388, S32K389, 
S32K358, S32K348, 
S32K338 and S32K328
—
V25
Flash memory 
supply (2.5 V), 
internally regulated 2
-0.3
—
2.9
V
—
—
Table continues on the next page...
NXP Semiconductors
General
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
20 / 152


---
# 페이지 21

Table 2. Absolute maximum ratings (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
V11
High-current core 
logic supply input 2
-0.3
—
1.26
V
For S32K388 and 
S32K389
—
V11
Core logic 
voltage supply 
(1.1 V), internally 
regulated 2
-0.3
—
1.26
V
For all S32K3xx 
variants except 
S32K388 and S32K389
—
VREFH
ADC high reference 
voltage 1,2
-0.3
—
6.0
V
—
—
VREFL
ADC low reference 
voltage 2
-0.3
—
0.3
V
—
—
VGPIO_trans
Transient 
overshoot voltage 
allowed on I/
O pin 1,2,4
-
—
6.0
V
—
—
I_INJPAD_DC_
ABS
Continuous DC 
input current 
(positive/negative) 
that can be injected 
into an I/O pin 5
-3
—
3
mA
—
—
I_INJSUM_DC_
ABS
Sum of absolute 
value of injected 
currents on all the 
I/O pins (continuous 
DC limit) 5,6
—
—
30
mA
—
—
TSTG
Storage ambient 
temperature 7
-55
—
150
°C
—
—
1. 6.0 V maximum for 10 hours over lifetime; 7.0 V maximum for 60 seconds over lifetime.
2. All voltages are referred to VSS unless otherwise specified.
3. Voltage at VDD_DCDC cannot be higher than VDD_HV_A.
4. When a low impedance voltage source, without current limitation, is connected to one or more I/O pins, the VGPIO_trans 
absolute max rating must be honored. During current injection, the voltage at the I/O pin or pins could go beyond this limit if 
(and ONLY IF) the injected current is being limited (I_INJPAD_DC_ABS is respected).
5. When the input pad voltage levels are close to VDD_HV_A (respectively to VDD_HV_B) or VSS, plus /minus the forward 
voltage of ESD diodes, practically, no current is being injected. When these limits are exceeded, the maximum input 
current spec must be met. See S32K3 Hardware Design Guidelines for more details and recommendations for protecting 
the devices against injection current. 
6. If a positive injection current is present in one or more I/O pins when the device is in Low Speed RUN or STANDBY mode, 
the voltage in the respective I/O power domain (VDD_HV_A or VDD_HV_B) would increase and may cause damage to the 
MCU. It is recommended to add external circuitry (which are explained in the S32K3XX Hardware Design Guidelines) to 
protect the MCU against injection current.
7. TSTG specifies the storage temperature range. It is not the operating temperature range. Please refer to the Thermal 
operating characteristics table.
NXP Semiconductors
General
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
21 / 152


---
# 페이지 22

5.2 Voltage and current operating requirements
 
Device functionality is guaranteed down to the LVR assert level, however electrical performance of 12-bit ADC, 
CMP with 8-bit DAC, IO electrical characteristics, and communication modules electrical characteristics will be 
degraded when voltage drops below 2.97 V.
  NOTE  
The VDD_HV_B and V15 voltage supply domains are only present in certain devices and packages 
(S32K388, S32K389, S32K358, S32K348, S32K338, S32K328, S32K344, S32K324, S32K314, S32K342, S32K341, S32K322).
The VDD_DCDC supply voltage is only present in certain devices and packages (S32K358, S32K348, S32K338, S32K328, 
S32K388 and S32K389).
Table 3. Voltage and current operating requirements
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
VDD_HV_A
Main I/O and analog 
supply voltage 1
2.97
3.3 or 5.0
5.5
V
—
—
VDD_HV_B
Secondary I/O 
supply voltage 1
2.97
3.3 or 5.0
5.5
V
—
—
VDD_DCDC
Supply voltage for 
the SMPS gate 
driver 1,2
2.97
3.3 or 5.0
5.5
V
—
—
V15
Voltage sensing 
input 1,3
1.425
1.5
1.65
V
For S32K388 and 
S32K389
—
V15
High-current logic 
supply input 
voltage 1,3
1.425
1.5
1.65
V
For all S32K3xx 
variants except 
S32K388 and S32K389
—
V15_extended
High-current logic 
supply input 
voltage, extended 
range 1,3,4,5
1.425
3.3 or 5.0
5.5
V
For S32K322, 
S32K341, S32K342, 
S32K314, S32K324, 
S32K344
—
VREFH
ADC high reference 
voltage 1,6
2.97
3.3 or 5.0
5.5
V
—
—
VREFL
ADC low reference 
voltage 1
-0.1
0
0.1
V
—
—
VSS_DCDC
Power ground for the 
SMPS gate driver 1
-0.1
0
0.1
V
—
—
V25
Flash memory 
and clock 
supply (2.5 V), 
internally regulated 1
—
2.5
—
V
—
—
V11
High-current core 
logic supply input 1
—
1.14
—
V
For S32K388 and 
S32K389
—
V11
Core logic supply 
(1.1 V), internally 
regulated 1
—
1.14
—
V
For all S32K3xx 
variants except 
S32K388 and S32K389
—
Table continues on the next page...
NXP Semiconductors
General
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
22 / 152


---
# 페이지 23

Table 3. Voltage and current operating requirements (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
VGPIO
Input voltage range 
at any I/O or analog 
pin 1,7
-0.3
—
VDD_HV
_A/B + 
0.3
V
—
—
VODPU
Open-drain pull-up 
voltage 1,8
—
—
VDD_HV
_A/B
V
—
—
IINJPAD_DC_OP
Continuous DC input 
current (positive/
negative) that can be 
injected into an I/O 
pin 9
-3
—
3
mA
VDD_HV_A >= 3.6V
—
IINJPAD_DC_OP
Continuous DC input 
current (positive/
negative) that can be 
injected into an I/O 
pin 9
-2
—
3
mA
VDD_HV_A >= 2.97V
—
IINJSUM_DC_OP
Sum of 
absolute value of 
injected currents 
on all the I/O 
pins (continuous 
DC limit) 9,10
-30
—
30
mA
VDD_HV_A >= 3.6V
—
IINJSUM_DC_OP
Sum of 
absolute value of 
injected currents 
on all the I/O 
pins (continuous 
DC limit) 9,10
-20
—
30
mA
VDD_HV_A >= 2.97V
—
Vramp_slow
Supply ramp rate 
(slow) 1,11
0.5
—
—
V/min
—
—
Vramp_fast
Supply ramp rate 
(fast) 1,11
—
—
100
V/ms
—
—
1. All voltages are referred to VSS unless otherwise specified.
2. Voltage at VDD_DCDC cannot be higher than VDD_HV_A.
3. Min and Max values are applicable only for non-SMPS mode where V15 is sourced externally.
4. If total power dissipation and maximum junction temperature allows. Please refer to Thermal operating characteristics
table for the maximum junction temperature, and Thermal characteristics table for the thermal  characteristics, to determine
the maximum power dissipation allowed for a given package.
5. You must ensure that the junction temperature in the application must not exceed the maximum specified Tj.
6. VREFH should always be equal to or less than VDD_HV_A +0.1. Any positive differential voltage between VREFH and
VDD_HV_A i.e., VDD_HV_A < VREFH <= VDD_HV_A + 0.1V) is for RF-AC only. Appropriate decoupling capacitors should
be used to filter noise on the supplies. See application note AN5032 for reference supply design for SAR_ADC
7. Keeping the input voltage between this range practically ensures that no (noticeable) current is being injected. When
exceeding these limits, the current being injected must be lower than IINJPAD_DC_OP, all the time.
8. Open-drain outputs must be pulled respectively to their supply rail (VDD_HV_A or VDD_HV_B).
9. When the input pad voltage levels are close to VDD_HV_A (respectively to VDD_HV_B) or VSS, plus /minus the forward
voltage of ESD diodes, practically, no current is being injected. When these limits are exceeded, the maximum input
current spec must be honored. Refer to the S32K3 Hardware Design Guidelines AN for more details and recommendations
for protecting the devices against injection current.
NXP Semiconductors
General
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
23 / 152


---
# 페이지 24

10. If a positive injection current is present in one or more I/O pins, and the device is in Low-Speed RUN or STANDBY mode,
the VDD_HV_A (or respectively, VDD_HV_B) may lift and cause unexpected behavior. Therefore, it is recommended to
add external protection hardware, to safely cover this scenario.
11. The MCU supply ramp rate parameter must be applicable to the MCU input/external supplies. The ramp rate
assumes that the S32K3xx HW design guidelines available on www.nxp.com are followed.
5.3 Thermal operating characteristics
Table 4. Thermal operating characteristics
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
Tamb
Ambient temperature -40
—
105
°C
V- Grade
—
Tamb
Ambient temperature -40
—
125
°C
M- Grade
—
TJ
Junction 
temperature
-40
—
150
°C
—
—
For S32K388 and S32K389, applications running at 125°C Tamb, thermal management schemes at PCB level will have to be 
deployed to keep TJ below 150°C.
5.4 ESD and Latch-up Protection Characteristics
Table 5. ESD and Latch-up Protection Characteristics
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
Vhbm
Electrostatic 
discharge voltage, 
human body model 
(HBM) 1,2,3
-2000
—
2000
V
—
—
Vcdm
Electrostatic 
discharge voltage, 
charged-device 
model (CDM), 
all pins except 
corner 1,2,4
-500
—
500
V
—
—
Vcdm
Electrostatic 
discharge voltage, 
charged-device 
model (CDM), corner 
pins 1,2,4
-750
—
750
V
—
—
Ilat
Latch-up current at 
ambient temperature 
of 125°C 5
-100
—
100
mA
—
—
1. Device failure is defined as: "If after exposure to ESD pulses, the device does not meet specification requirements."
2. All ESD testing conforms with AEC-Q100 Stress Test Qualification for Automotive Grade Integrated Circuits.
3. This parameter is tested in conformity with AEC-Q100-002.
4. This parameter is tested in conformity with AEC-Q100-011.
5. This parameter is tested in conformity with AEC-Q100-004.
NXP Semiconductors
General
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
24 / 152


---
# 페이지 25

6 Power management
6.1 Power mode transition operating behaviors
6.1.1 Power mode transition operating behavior
The values in the table below are provided for reference only.
Table 6. Power mode transition operating behavior
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
tMODE_
STDBYENTRY
RUN --> 
STANDBY transition 
time
—
1035
—
ns
For S32K388 and 
S32K389
—
tMODE_
STDBYENTRY
RUN --> STANDBY 
transition time
—
955
—
ns
—
—
tMODE_ 
STDBYEXIT_FAST
STANDBY --> RUN 
transition time, Fast 
Recovery, V15 
SMPS with trickle 
LDO disabled
—
85.5
—
us
For S32K328, 
S32K338, S32K348 
and S32K358
—
tMODE_ 
STDBYEXIT_FAST
STANDBY --> RUN 
transition time, Fast 
Recovery, V15 
SMPS with trickle 
LDO enabled
—
58.6
—
us
For S32K328, 
S32K338, S32K348 
and S32K358
—
tMODE_
STDBYEXIT_FAST
STANDBY --> 
RUN transition 
time, FastRecovery, 
V15External
—
58.5
—
us
For S32K328, 
S32K338, S32K348 
and S32K358
—
tMODE_
STDBYEXIT_FAST
STANDBY --> RUN 
transition time, Fast 
Recovery exit
—
53
—
us
FIRC ON @48MHz 
in Standby mode, For 
all S32K3xx devices 
except S32K3x8 and 
S32K389
—
tMODE_
STDBYEXIT
STANDBY --> RUN 
transition time, 
normal recovery exit
—
80
—
us
For all S32K3xx 
devices except 
S32K3x8 and S32K389
—
tMODE_
STDBYEXIT
STANDBY --> RUN 
transition time, 
Normal Recovery, 
V15 External
—
140
—
us
For S32K328, 
S32K338, S32K348 
and S32K358
—
tMODE_
STDBYEXIT
STANDBY --> 
RUN transition 
time, V15 SMPS 
with  trickle LDO 
enabled
—
186
—
us
For S32K388 and 
S32K389
—
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
25 / 152


---
# 페이지 26

Table 6. Power mode transition operating behavior (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
tMODE_
STDBYEXIT
STANDBY --> RUN 
transition time, with 
SMPS trickle LDO 
disabled 1
—
212
—
us
For S32K388 and 
S32K389
—
tMODE_
STDBYEXIT
STANDBY --> RUN 
transition, time 
Normal Recovery, 
V15 SMPS
—
154
—
us
For S32K328, 
S32K338, S32K348 
and S32K358
—
1. S32K388 and S32K389 doesn’t support the FAST STANDBY EXIT recovery
6.1.2 Boot time, HSE firmware not installed
Table 7. Boot time, HSE firmware not installed
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
tBOOT_noHSE
After a POR event, 
amount of time to 
execution of the 
first instruction of 
the application core, 
when HSE firmware 
is not installed. (HSE 
FW feature flag is 
disabled)
—
2
—
ms
Device running from 
FIRC (clocking option 
D). CORE_CLK = 48 
MHz; HSE_CLK = 48 
MHz.
—
6.1.3 Boot time, HSE firmware installed
The following table provides the boot time of the S32K3 SBAF and Firmware initialization. To obtain the total boot time, the 
corresponding user code verification time must be added.
Table 8. Boot time, HSE firmware installed
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
tBOOT_HSE_
NONSECURE
After a POR event, 
amount of time to 
execution of the 
first instruction of 
the application core, 
when HSE firmware 
is installed. (BOOT 
SEQ = 0)
—
—
3
ms
Device running from 
FIRC (clocking option 
D). CORE_CLK = 48 
MHz; HSE_CLK = 48 
MHz.
—
tBOOT_HSE
After a POR event, 
amount of time to 
execution of the 
first instruction of 
—
12.36
—
ms
Device running from 
FIRC (clocking option 
D). CORE_CLK = 48 
—
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
26 / 152


---
# 페이지 27

Table 8. Boot time, HSE firmware installed (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
the application core, 
when HSE firmware 
is installed.
MHz; HSE_CLK = 48 
MHz.
tBOOT_HSE
After a POR event, 
amount of time to 
execution of the 
first instruction of 
the application core, 
when HSE firmware 
is installed.
—
9.51
—
ms
Device running from 
PLL (clocking option 
B). CORE_CLK = 120 
MHz; HSE_CLK = 120 
MHz.
—
tBOOT_HSE
After a POR event, 
amount of time to 
execution of the 
first instruction of 
the application core, 
when HSE firmware 
is installed.
—
10.91
—
ms
Device running from 
PLL (clocking option 
A). CORE_CLK = 160 
MHz; HSE_CLK = 80 
MHz.
—
6.1.4 HSE firmware memory verification time examples
Table 9. HSE firmware memory verification time examples
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
tCMAC_64KB
Memory verification 
of 64 KB of 
application firmware, 
using AES-128 
CMAC cipher.
—
11.3
—
ms
Device running from 
FIRC (clocking option 
D). CORE_CLK = 48 
MHz; HSE_CLK = 48 
MHz.
—
tCMAC_1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using AES-128 
CMAC cipher.
—
176
—
ms
Device running from 
FIRC (clocking option 
D). CORE_CLK = 48 
MHz; HSE_CLK = 48 
MHz.
—
tGMAC_64KB
Memory verification 
of 64 KB of 
application firmware, 
using AES-128 
GMAC cipher.
—
3.2
—
ms
Device running from 
FIRC (clocking option 
D). CORE_CLK = 48 
MHz; HSE_CLK = 48 
MHz.
—
tGMAC_1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using AES-128 
GMAC cipher.
—
46.8
—
ms
Device running from 
FIRC (clocking option 
D). CORE_CLK = 48 
MHz; HSE_CLK = 48 
MHz.
—
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
27 / 152


---
# 페이지 28

Table 9. HSE firmware memory verification time examples (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
tHMAC_64KB
Memory verification 
of 64 KB of 
application firmware, 
using AES-128 
HMAC cipher.
—
1.74
—
ms
Device running from 
FIRC (clocking option 
D). CORE_CLK = 48 
MHz; HSE_CLK = 48 
MHz.
—
tHMAC_1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using AES-128 
HMAC cipher.
—
22.87
—
ms
Device running from 
FIRC (clocking option 
D). CORE_CLK = 48 
MHz; HSE_CLK = 48 
MHz.
—
tRSA_64KB
Memory verification 
of 64 KB of 
application firmware, 
using RSA 2048 
cipher.
—
31.03
—
ms
Device running from 
FIRC (clocking option 
D). CORE_CLK = 48 
MHz; HSE_CLK = 48 
MHz.
—
tRSA_1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using RSA 2048 
cipher.
—
52.15
—
ms
Device running from 
FIRC (clocking option 
D). CORE_CLK = 48 
MHz; HSE_CLK = 48 
MHz.
—
tECDSA_64KB
Memory verification 
of 64 KB of 
application firmware, 
using ECDSA 521 
bits cipher.
—
126.46
—
ms
Device running from 
FIRC (clocking option 
D). CORE_CLK = 48 
MHz; HSE_CLK = 48 
MHz.
—
tECDSA_1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using ECDSA 521 
bits cipher.
—
147.53
—
ms
Device running from 
FIRC (clocking option 
D). CORE_CLK = 48 
MHz; HSE_CLK = 48 
MHz.
—
tSHA2_256_64KB
Memory verification 
of 64 KB of 
application firmware, 
using SHA2 256 bits 
bits cipher.
—
1.62
—
ms
Device running from 
FIRC (clocking option 
D). CORE_CLK = 48 
MHz; HSE_CLK = 48 
MHz.
—
tSHA2_256_
1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using SHA2 256 bits 
bits cipher.
—
22.73
—
ms
Device running from 
FIRC (clocking option 
D). CORE_CLK = 48 
MHz; HSE_CLK = 48 
MHz.
—
tCMAC_64KB
Memory verification 
of 64 KB of 
application firmware, 
—
6.67
—
ms
Device running from 
PLL (clocking option 
A). CORE_CLK = 160 
—
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
28 / 152


---
# 페이지 29

Table 9. HSE firmware memory verification time examples (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
using AES-128 
CMAC cipher.
MHz; HSE_CLK = 80 
MHz.
tCMAC_1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using AES-128 
CMAC cipher.
—
105.24
—
ms
Device running from 
PLL (clocking option 
A). CORE_CLK = 160 
MHz; HSE_CLK = 80 
MHz.
—
tGMAC_64KB
Memory verification 
of 64 KB of 
application firmware, 
using AES-128 
GMAC cipher.
—
1.85
—
ms
Device running from 
PLL (clocking option 
A). CORE_CLK = 160 
MHz; HSE_CLK = 80 
MHz.
—
tGMAC_1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using AES-128 
GMAC cipher.
—
28.03
—
ms
Device running from 
PLL (clocking option 
A). CORE_CLK = 160 
MHz; HSE_CLK = 80 
MHz.
—
tHMAC_64KB
Memory verification 
of 64 KB of 
application firmware, 
using AES-128 
HMAC cipher.
—
0.98
—
ms
Device running from 
PLL (clocking option 
A). CORE_CLK = 160 
MHz; HSE_CLK = 80 
MHz.
—
tHMAC_1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using AES-128 
HMAC cipher.
—
13.68
—
ms
Device running from 
PLL (clocking option 
A). CORE_CLK = 160 
MHz; HSE_CLK = 80 
MHz.
—
tRSA_64KB
Memory verification 
of 64 KB of 
application firmware, 
using RSA 2048 
cipher.
—
17.39
—
ms
Device running from 
PLL (clocking option 
A). CORE_CLK = 160 
MHz; HSE_CLK = 80 
MHz.
—
tRSA_1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using RSA 2048 
cipher.
—
23.32
—
ms
Device running from 
PLL (clocking option 
A). CORE_CLK = 160 
MHz; HSE_CLK = 80 
MHz.
—
tECDSA_64KB
Memory verification 
of 64 KB of 
application firmware, 
using ECDSA 521 
bits cipher.
—
72.2
—
ms
Device running from 
PLL (clocking option 
A). CORE_CLK = 160 
MHz; HSE_CLK = 80 
MHz.
—
tECDSA_1024KB
Memory verification 
of 1024 KB of 
—
84.91
—
ms
Device running from 
PLL (clocking option 
—
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
29 / 152


---
# 페이지 30

Table 9. HSE firmware memory verification time examples (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
application firmware, 
using ECDSA 521 
bits cipher.
A). CORE_CLK = 160 
MHz; HSE_CLK = 80 
MHz.
tSHA2_256_64KB
Memory verification 
of 64 KB of 
application firmware, 
using SHA2 256 bits 
bits cipher.
—
0.9
—
ms
Device running from 
PLL (clocking option 
A). CORE_CLK = 160 
MHz; HSE_CLK = 80 
MHz.
—
tSHA2_256_
1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using SHA2 256 bits 
bits cipher.
—
13.6
—
ms
Device running from 
PLL (clocking option 
A). CORE_CLK = 160 
MHz; HSE_CLK = 80 
MHz.
—
tCMAC_64KB
Memory verification 
of 64 KB of 
application firmware, 
using AES-128 
CMAC cipher.
—
4.5
—
ms
Device running from 
PLL (clocking option 
B). CORE_CLK = 120 
MHz; HSE_CLK = 120 
MHz.
—
tCMAC_1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using AES-128 
CMAC cipher.
—
69.9
—
ms
Device running from 
PLL (clocking option 
B). CORE_CLK = 120 
MHz; HSE_CLK = 120 
MHz.
—
tGMAC_64KB
Memory verification 
of 64 KB of 
application firmware, 
using AES-128 
GMAC cipher.
—
1.3
—
ms
Device running from 
PLL (clocking option 
B). CORE_CLK = 120 
MHz; HSE_CLK = 120 
MHz.
—
tGMAC_1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using AES-128 
GMAC cipher.
—
18.7
—
ms
Device running from 
PLL (clocking option 
B). CORE_CLK = 120 
MHz; HSE_CLK = 120 
MHz.
—
tHMAC_64KB
Memory verification 
of 64 KB of 
application firmware, 
using AES-128 
HMAC cipher.
—
0.7
—
ms
Device running from 
PLL (clocking option 
B). CORE_CLK = 120 
MHz; HSE_CLK = 120 
MHz.
—
tHMAC_1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using AES-128 
HMAC cipher.
—
9.12
—
ms
Device running from 
PLL (clocking option 
B). CORE_CLK = 120 
MHz; HSE_CLK = 120 
MHz.
—
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
30 / 152


---
# 페이지 31

Table 9. HSE firmware memory verification time examples (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
tRSA_64KB
Memory verification 
of 64 KB of 
application firmware, 
using RSA 2048 
cipher.
—
15.4
—
ms
Device running from 
PLL (clocking option 
B). CORE_CLK = 120 
MHz; HSE_CLK = 120 
MHz.
—
tRSA_1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using RSA 2048 
cipher.
—
23.8
—
ms
Device running from 
PLL (clocking option 
B). CORE_CLK = 120 
MHz; HSE_CLK = 120 
MHz.
—
tECDSA_64KB
Memory verification 
of 64 KB of 
application firmware, 
using ECDSA 521 
bits cipher.
—
53.95
—
ms
Device running from 
PLL (clocking option 
B). CORE_CLK = 120 
MHz; HSE_CLK = 120 
MHz.
—
tECDSA_1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using ECDSA 521 
bits cipher.
—
62.34
—
ms
Device running from 
PLL (clocking option 
B). CORE_CLK = 120 
MHz; HSE_CLK = 120 
MHz.
—
tSHA2_256_64KB
Memory verification 
of 64 KB of 
application firmware, 
using SHA2 256 bits 
bits cipher.
—
0.64
—
ms
Device running from 
PLL (clocking option 
B). CORE_CLK = 120 
MHz; HSE_CLK = 120 
MHz.
—
tSHA2_256_
1024KB
Memory verification 
of 1024 KB of 
application firmware, 
using SHA2 256 bits 
bits cipher.
—
9.07
—
ms
Device running from 
PLL (clocking option 
B). CORE_CLK = 120 
MHz; HSE_CLK = 120 
MHz.
—
6.2 Supply Monitoring
Certain monitors are present on certain devices. See Power Management chapter in reference manual.
Table 10. Supply Monitoring
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
LVD_V15
Low Voltage Detect 
(LVD) on V15, 
deassert threshold 
(in FPM)
1.34
1.38
1.42
V
—
—
HVD_V15
High Voltage Detect 
(HVD) on V15, 
—
2.5
—
V
—
—
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
31 / 152


---
# 페이지 32

Table 10. Supply Monitoring (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
assert threshold (in 
FPM) 1
LVR_VDD_HV_A
LVR on VDD_HV_A, 
assert threshold (in 
FPM)
2.77
2.85
2.93
V
—
—
LVR_VDD_HV_A
LVR on VDD_HV_A, 
assert threshold (in 
RPM)
2.77
2.85
2.93
V
—
—
—
VDD_HV_A LVR 
monitor hysteresis
—
18.75
—
mV
—
—
HVD_VDD_HV_A
HVD on VDD_HV_A, 
assert threshold (in 
FPM)
5.787
5.887
5.987
V
—
—
—
VDD_HV_A HVD 
monitor hysteresis
—
37.5
—
mV
—
—
LVR_VDD_HV_B
LVR on VDD_HV_B, 
assert threshold (in 
FPM)
2.77
2.85
2.93
V
—
—
LVR_VDD_HV_B
LVR on VDD_HV_B, 
assert threshold (in 
RPM)
2.77
2.85
2.93
V
—
—
—
VDD_HV_B LVR 
monitor hysteresis
—
18.75
—
mV
—
—
HVD_VDD_HV_B
HVD on VDD_HV_B, 
assert threshold (in 
FPM)
5.787
5.887
5.987
V
—
—
—
VDD_HV_B HVD 
monitor hysteresis
—
37.5
—
mV
—
—
LVD_VDD_HV_A
Low Voltage 
Detect (LVD5A) on 
VDD_HV_A, assert 
threshold (in FPM)
4.33
4.41
4.49
V
—
—
—
VDD_HV_A 
LVD monitor 
hysteresis
—
37.5
—
mV
—
—
VPOR_VDD_HV_A
Power-On-Reset 
(VPOR) on 
VDD_HV_A, 
deassert threshold
0.9
1.5
2.2
V
—
—
VREF12
Bandgap reference, 
trimmed
1.18
1.2
1.22
V
—
—
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
32 / 152


---
# 페이지 33

1. The HVD_V15 monitor is provided to indicate if the V15 rail is far above the standard V15 operating range , to ensure 
failures in the  V15 regulator are detected
6.3 Recommended Decoupling Capacitors
Table 11. Recommended Decoupling Capacitors
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
CDEC
Decoupling capacitor 
(one per supply 
pin) 1,2,3
70
100
—
nF
—
—
CBULK
Input supply bulk 
capacitor 2,4,5,6
—
4.7
—
µF
—
—
COUT_V15_NPN
V15 (1.5V 
Regulator) output 
capacitor 2,7
—
2.2
—
µF
—
—
COUT_V11
V11 (1.1V 
Regulator) 
output capacitor (all 
chips, except 
S32K312, S32K311, 
S32K310 and 
S32K388) 2
—
2.2
—
µF
—
—
COUT_V11
V11 (1.1V 
Regulator) 
output capacitor 
(S32K312, S32K311 
& S32K310) 2
—
1
—
µF
—
—
COUT_V11
V11 (1.1V 
Regulator) 
output capacitor 
(S32K388) 2
—
22
—
uF
—
—
COUT_V25
V25 (2.5V 
Regulator) output 
capacitor 1,2
140
220
—
nF
—
—
1. These capacitors must be placed as close as possible to the corresponding supply and ground pins. For BGA 
packages, the capacitors must be placed on the other side of the PCB to minimize the trace lengths.
2. All capacitors must be low ESR ceramic capacitors (for example, X7R).  The minimum recommendation is after 
considering component aging and tolerance.
3. Optionally, 1 nF capacitors can be added in parallel to the decoupling capacitors.
4. These capacitors must be placed close to the source.
5. For devices where the VDD_HV_B domain is present, if the VDD_HV_B supply is different supply from VDD_HV_A, a 
dedicated bulk capacitor is needed.
6. It is also possible to use higher capacitance values (for example, 10 μF) in place of the 4.7 μF capacitor.
7. For devices where V15 is present, the V15 regulator output capacitor and the filter capacitors are required when using an 
NPN bipolar ballast transistor for the regulation stage. When V15 is supplied from an external regulator, these capacitance 
recommendations can be followed in addition to the capacitance requirements of the external voltage regulator.
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
33 / 152


---
# 페이지 34

6.3.1 Recommended Decoupling Capacitor diagrams
CDEC
COUT_V25
V25
7
6
5
31
3
4
8
30
V11
V25
VDD_HV_A
VDD_HV_A
VREFH
VREFL
VSS
VSS
CBULK
VDD_HV_A
CDEC
VREFH
COUT_V11
V11
Figure 17. 48-pin LQFP decoupling capacitor pinout diagram (S32K311, S32K310)
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
34 / 152


---
# 페이지 35

CDEC
COUT_V25
V25
13
60
11
10
37
62
8
9
12
14
16
38
61
86
V11
V11
V25
VDD_HV_A
VDD_HV_A
VDD_HV_A
VREFH
VREFL
VSS
VSS
VSS
VSS
VSS
VSS
CBULK
VDD_HV_A
CDEC
CDEC
VREFH
CDEC
COUT_V11
V11
87
VDD_HV_A
CDEC
Figure 18. 100-pin HDQFP decoupling capacitor pinout diagram (S32K312, S32K311, S32K310)
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
35 / 152


---
# 페이지 36

CDEC
CBULK
VDD_HV_B
CDEC
COUT_V25
V25
13
60
7
11
25
37
10
62
87
8
9
14
16
24
38
61
86
V11
V11
VRC_CTRL
V25
VDD_HV_B
VDD_HV_B
VDD_HV_A
VDD_HV_A
VDD_HV_A
VREFH
VREFL
VSS
VSS
VSS
VSS
VSS
VSS
CBULK
VDD_HV_A
CDEC
CDEC
VREFH
Q_V15_NPN
RBTC15
VDD_HV_NPN
V15
BJT option
COUT_V15_NPN
12
59
V15
V15
CDEC
COUT_V11
V11
CDEC
CDEC
V15
Figure 19. 100-pin HDQFP decoupling capacitor pinout diagram (S32K342, S32K341, S32K322)
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
36 / 152


---
# 페이지 37

CDEC
COUT_V25
V25
21
59
19
18
38
57
77
16
17
20
22
24
37
58
78
107
127
150
V11
V11
V25
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VREFH
VREFL
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VREFH
108
VDD_HV_A
106
149
V11
V11
128
151
169
VDD_HV_A
VDD_HV_A
VDD_HV_A
CDEC
 CBULK
CDEC
VDD_HV_A
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
V11
COUT_V11
168
VSS
Figure 20. 172-pin HDQFP decoupling capacitor pinout diagram (S32K312)
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
37 / 152


---
# 페이지 38

CDEC
CDEC
CBULK
VDD_HV_B
CDEC
COUT_V25
V25
21
59
106
149
11
19
38
57
77
18
108
128
151
16
17
22
24
37
58
78
107
127
150
168
V11
V11
V11
V11
VRC_CTRL
V25
VDD_HV_B
VDD_HV_B
VDD_HV_B
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VREFH
VREFL
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
CBULK
VDD_HV_A
CDEC
CDEC
VREFH
Q_V15_NPN
RBTC15
VDD_HV_NPN
V15
BJT option
COUT_V15_NPN
20
60
105
148
V15
V15
V15
V15
CDEC
CDEC
CDEC
COUT_V11
V11
CDEC
CDEC
V15
169
VDD_HV_A
CDEC
Figure 21. 172-pin HDQFP decoupling capacitor pinout diagram (S32K344, S32K324, S32K314, S32K342, S32K341 
and S32K322)
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
38 / 152


---
# 페이지 39

CDEC
CDEC
CBULK
VDD_HV_B
CDEC
COUT_V25
V25
H9
J8
J10
K9
F1
J7
N4
R7
R10
D14
G10
H7
K11
H6
J6
B2
B16
D4
D9
G7
G11
J1
J4
J9
J14
L7
L11
P4
P14
T2
T7
T10
T16
V11
V11
V11
V11
VRC_CTRL
V25
VDD_HV_B
VDD_HV_B
VDD_HV_B
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VREFH
VREFL
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
CBULK
VDD_HV_A
CDEC
CDEC
CDEC
VREFH
Q_V15_NPN
RBTC15
VDD_HV_NPN
V15
BJT option
COUT_V15_NPN
H8
H10
K8
K10
V15
V15
V15
V15
CDEC
CDEC
CDEC
COUT_V11
V11
CDEC
CDEC
V15
L8
VDD_HV_A
Figure 22. 257BGA package decoupling capacitor pinout diagram (S32K344, S32K324 and S32K314)
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
39 / 152


---
# 페이지 40

CDEC
CDEC
CBULK
VDD_HV_B
21
59
106
149
11
27
28
19
38
57
77
18
108
128
151
169
16
17
26
22
24
37
58
78
107
127
150
168
EP
V11
V11
V11
V11
VRC_CTRL
PMOS_CTRL
VDD_DCDC
V25
VDD_HV_B
VDD_HV_B
VDD_HV_B
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VREFH
VREFL
VSS_DCDC
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
NC
Q_V15_NPN
RBTC15
VDD_HV_NPN
V15
BJT option
COUT_V15_NPN
20
36
60
79
105
V15
V15
V15
V15
V15
148
V15
CDEC
CDEC
CDEC
V15
CDEC
CDEC
CDEC
CDEC
CDEC
COUT_V11
V11
CDEC
CDEC
CDEC
CDEC
CDEC
VREFH
COUT_V25
V25
CBULK
VDD_HV_A
Figure 23. 172-pin HDQFP-EP decoupling capacitor pinout diagram (S32K358, S32K348, S32K338 and S32K328)
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
40 / 152


---
# 페이지 41

CDEC
CDEC
CBULK
VDD_HV_B
21
59
106
149
11
27
28
19
38
57
77
18
108
128
151
169
16
17
26
22
24
37
58
78
107
127
150
168
EP
V11
V11
V11
V11
VRC_CTRL
PMOS_CTRL
VDD_DCDC
V25
VDD_HV_B
VDD_HV_B
VDD_HV_B
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VREFH
VREFL
VSS_DCDC
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
NC
20
36
60
79
105
V15
V15
V15
V15
V15
148
V15
CDEC
CDEC
CDEC
V15
CDEC
CDEC
CDEC
CDEC
CDEC
COUT_V11
V11
CDEC
CDEC
CDEC
CDEC
CDEC
VREFH
COUT_V25
V25
VDD_DCDC
V15
L_SMPS
D_SMPS
Q_SMPS
COUT_V15_SMPS
SMPS option
CBULK
VDD_HV_A
CBULK_SMPS
Figure 24. 172-pin HDQFP-EP decoupling capacitor pinout diagram, SMPS (S32K358, S32K348, S32K338 
and S32K328)
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
41 / 152


---
# 페이지 42

CDEC
CDEC
CBULK
VDD_HV_B
H9
J8
J10
K9
F1
K5
L5
J7
N4
R7
R10
D14
E5
G10
H7
H13
K11
L8
N5
N9
H6
J6
J5
B2
B16
D4
D9
E13
G7
G11
J1
J9
J14
L7
L11
M5
N7
N10
P4
P14
T2
T7
T10
T16
V11
V11
V11
V11
VRC_CTRL
PMOS_CTRL
VDD_DCDC
V25
VDD_HV_B
VDD_HV_B
VDD_HV_B
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VREFH
VREFL
VSS_DCDC
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
CDEC
CDEC
CDEC
CBULK
VDD_HV_A
CDEC
CDEC
CDEC
NC
Q_V15_NPN
RBTC15
VDD_HV_NPN
V15
BJT option
COUT_V15_NPN
E9
H8
H10
J13
K8
V15
V15
V15
V15
V15
K10
N6
N8
V15
V15
V15
CDEC
CDEC
CDEC
V15
CDEC
CDEC
CDEC
CDEC
CDEC
COUT_V11
V11
CDEC
VREFH
CDEC
J4
VSS
COUT_V25
V25
Figure 25. 289BGA package decoupling capacitor pinout diagram (S32K358, S32K348, S32K338 and S32K328)
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
42 / 152


---
# 페이지 43

CDEC
CDEC
CBULK
VDD_HV_B
H9
J8
J10
K9
F1
K5
L5
J7
N4
R7
R10
D14
E5
G10
H7
H13
K11
L8
N5
N9
H6
J6
J5
B2
B16
D4
D9
E13
G7
G11
J1
J4
J9
J14
L7
L11
M5
N7
N10
P4
P14
T2
T7
T10
V11
V11
V11
V11
VRC_CTRL
PMOS_CTRL
VDD_DCDC
V25
VDD_HV_B
VDD_HV_B
VDD_HV_B
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VREFH
VREFL
VSS_DCDC
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
CDEC
CDEC
CDEC
CBULK
VDD_HV_A
CDEC
CDEC
CDEC
NC
E9
H8
H10
J13
K8
V15
V15
V15
V15
V15
K10
N6
N8
V15
V15
V15
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
COUT_V11
V11
VDD_DCDC
L_SMPS
D_SMPS
Q_SMPS
SMPS option
CDEC
VREFH
COUT_V15_SMPS
COUT_V25
V25
T16
VSS
CDEC
V15
V15
CBULK_SMPS
Figure 26. 289BGA package decoupling capacitor pinout diagram, SMPS (S32K358, S32K348, S32K338 and S32K328)
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
43 / 152


---
# 페이지 44

CDEC
CDEC
CBULK
VDD_HV_B
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
COUT_V25
V11
V25
V11
H9
H10
J8
J10
J13
K8
K9
K10
N6
N8
F1
H8
K5
L5
J7
N4
R7
R10
D14
E5
G10
H7
H13
K11
L8
N5
N9
H6
J6
J5
B2
B16
D4
D9
E13
G7
G11
J1
J4
J9
J14
L7
L11
M5
N7
N10
P4
P14
T2
T7
T10
E9
V11
V11
V11
V11
V11
V11
V11
V11
V11
V11
NMOS_CTRL
V15
PMOS_CTRL
VDD_DCDC
V25
VDD_HV_B
VDD_HV_B
VDD_HV_B
VDD_HV_A
VDD_HV_A
H7
H13
K11
L8
N5
N9
G10
VREFH
VREFL
VSS_DCDC
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
CBULK
CDEC
V15
PMIC option
CBULK should be defined as per PMIC
CDEC
CDEC
CDEC
CBULK
VDD_HV_A
CDEC
CDEC
CDEC
NC
CDEC
T16
VSS
CDEC
VREFH
LAST MILE
REGULATOR
EXTERNAL NFET
COUT_V11_NFET
V15
V11
Figure 27. 289BGA package decoupling capacitor pinout diagram, (S32K388)
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
44 / 152


---
# 페이지 45

CDEC
CDEC
CBULK
VDD_HV_B
CDEC
LAST MILE
REGULATOR
EXTERNAL NFET  
COUT_V11_NFET
CDEC
L_SMPS
D_SMPS
Q_SMPS
COUT_V15_SMPS
SMPS option
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
V15
V11
CDEC
E9
H9
H10
J8
J10
J13
K8
K9
K10
N6
N8
F1
H8
K5
L5
J7
N4
R7
R10
D14
E5
G10
H7
H13
K11
L8
N5
N9
H6
V11
V11
V11
V11
V11
V11
V11
V11
V11
V11
V11
NMOS_CTRL
V15
PMOS_CTRL
VDD_DCDC
V25
VDD_HV_B
VDD_HV_B
VDD_HV_B
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VREFH
CDEC
CDEC
CDEC
CBULK
VDD_HV_A
CDEC
CDEC
CDEC
V15
V11
J6
J5
B2
B16
D4
D9
E13
G7
G11
J1
J4
J9
J14
L7
L11
M5
N7
N10
P4
P14
T2
T7
T10
VREFL
VSS_DCDC
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
T16
VSS
COUT_V25
V25
CDEC
VREFH
VDD_DCDC
CBULK_SMPS
Figure 28. 289BGA package decoupling capacitor pinout diagram, SMPS (S32K388)
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
45 / 152


---
# 페이지 46

CDEC
CDEC
CBULK
VDD_HV_B
CDEC
CDEC
LAST MILE
REGULATOR
EXTERNAL NFET  
COUT_V11_NFET
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
COUT_V25
V11
B8
B10
B16
C20
G11
G20
K11
K12
L10
L12
E1
K10
K5
N7
L9
R6
U2
U9
B6
B12
B19
C2
E20
F16
G7
J12
K9
K8
L8
J5
A16
A20
AA2
AA11
AA19
B2
B7
B11
B20
D4
D18
E2
F1
F2
F6
F11
F20
G2
G15
H2
J1
B3
V11
V11
V11
V11
V11
V11
V11
V11
V11
V11
NMOS_CTRL
V15
PMOS_CTRL
VDD_DCDC
V25
VDD_HV_B
VDD_HV_B
VDD_HV_B
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VREFH
VREFL
VSS_DCDC
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
CDEC
CDEC
CDEC
CBULK
VDD_HV_A
CDEC
CDEC
CDEC
NC
NC
CDEC
V15
V11
VREFH
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
L15
V11
M10
V11
M11
V11
M12
V11
N2
V11
N20
V11
R2
V11
R8
V11
R10
V11
W2
V11
T20
V11
Y4
V11
Y8
V11
Y12
V11
Y17
V11
K15
VDD_HV_A
L20
VDD_HV_A
M13
VDD_HV_A
N10
VDD_HV_A
R7
VDD_HV_A
R11
VDD_HV_A
V20
VDD_HV_A
Y15
VDD_HV_A
Y19
VDD_HV_A
U12
VDD_HV_B
Y6
VDD_HV_B
Y10
VDD_HV_B
V25
J2
VSS
J3
VSS
J9
VSS
J13
VSS
J21
VSS
K2
VSS
K3
VSS
L2
VSS
L3
VSS
L6
VSS
L11
VSS
L16
VSS
M1
VSS
M2
VSS
M20
VSS
N9
VSS
N13
VSS
P7
VSS
R9
VSS
R12
VSS
T2
VSS
T6
VSS
T16
VSS
U20
VSS
V2
VSS
V4
VSS
V9
VSS
V12
VSS
V18
VSS
Y2
VSS
Y5
VSS
Y9
VSS
Y13
VSS
Y16
VSS
Y20
VSS
V11
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
V11
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
VDD_HV_A
V15
Figure 29. 437BGA package decoupling capacitor pinout diagram(S32K389)
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
46 / 152


---
# 페이지 47

CDEC
CDEC
CBULK
VDD_HV_B
CDEC
CDEC
LAST MILE
REGULATOR
EXTERNAL NFET  
COUT_V11_NFET
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
COUT_V25
V11
B8
B10
B16
C20
G11
G20
K11
K12
L10
L12
E1
K10
M7
N7
L9
R6
U2
U9
B6
B12
B19
C2
E20
F16
G7
J12
K9
K8
L8
J5
A16
A20
AA2
AA11
AA19
B2
B7
B11
B20
D4
D18
E2
F1
F2
F6
F11
F20
G2
G15
H2
J1
B3
V11
V11
V11
V11
V11
V11
V11
V11
V11
V11
NMOS_CTRL
V15
PMOS_CTRL
VDD_DCDC
V25
VDD_HV_B
VDD_HV_B
VDD_HV_B
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VDD_HV_A
VREFH
VREFL
VSS_DCDC
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
VSS
CDEC
CDEC
CDEC
CBULK
VDD_HV_A
CDEC
CDEC
CDEC
V15
V11
VREFH
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
L15
V11
M10
V11
M11
V11
M12
V11
N2
V11
N20
V11
R2
V11
R8
V11
R10
V11
W2
V11
T20
V11
Y4
V11
Y8
V11
Y12
V11
Y17
V11
K15
VDD_HV_A
L20
VDD_HV_A
M13
VDD_HV_A
N10
VDD_HV_A
R7
VDD_HV_A
R11
VDD_HV_A
V20
VDD_HV_A
Y15
VDD_HV_A
Y19
VDD_HV_A
U12
VDD_HV_B
Y6
VDD_HV_B
Y10
VDD_HV_B
V25
J2
VSS
J3
VSS
J9
VSS
J13
VSS
J21
VSS
K2
VSS
K3
VSS
L2
VSS
L3
VSS
L6
VSS
L11
VSS
L16
VSS
M1
VSS
M2
VSS
M20
VSS
N9
VSS
N13
VSS
P7
VSS
R9
VSS
R12
VSS
T2
VSS
T6
VSS
T16
VSS
U20
VSS
V2
VSS
V4
VSS
V9
VSS
V12
VSS
V18
VSS
Y2
VSS
Y5
VSS
Y9
VSS
Y13
VSS
Y16
VSS
Y20
VSS
V11
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
V11
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
CDEC
VDD_HV_A
V15
L_SMPS
D_SMPS
Q_SMPS
COUT_V15_SMPS
CDEC
V15
SMPS option
VDD_DCDC
CBULK
Figure 30. 437BGA package decoupling capacitor pinout diagram, SMPS(S32K389)
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
47 / 152


---
# 페이지 48

6.4 V15 regulator (SMPS option) electrical specifications
Some devices (S32K358, S32K348, S32K338, S32K328, S32K388 and S32K389) support a SMPS, DC-DC buck converter 
stage, with a dedicated pin to control an external Power P-channel MOSFET. In addition to the PMOS, an external inductor and 
a Schottky diode are required. See related figures in section "Recommended decoupling capacitors".
The chip hardware design guidelines document lists the recommended part numbers for PMOS, Schottky diode and inductor.
Table 12. V15 regulator (SMPS option) electrical specifications
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
V15
V15 output
—
1.5
—
V
—
—
L_SMPS
External coil 
inductance
—
4.7
—
uH
—
—
COUT_V15_SMPS
External bypass 
capacitor
—
20-22
—
uF
—
—
D_SMPS
External Schottky 
diode average 
forward current
—
2
—
A
—
—
VR
Schottky diode 
reverse voltage
5.0
—
—
V
—
—
IF
Schottky diode 
forward current
1.0
—
—
A
—
—
—
External P-channel 
MOSFET total gate 
charge
—
—
10
nC
VDD_DCDC = 5V
—
—
External P-channel 
MOSFET threshold 
voltage
—
—
2
V
—
—
CBULK_SMPS
Input supply bulk 
capacitor for internal 
SMPS 1
—
22
—
µF
—
—
1. Highly Recommended when internal SMPS is used to generate V15 and VDD_DCDC is supplied with isolated source from 
VDD_HV_A or VDD_HV_B
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
48 / 152


---
# 페이지 49

VDD_DCDC
V15
L_SMPS
D_SMPS
Q_SMPS
COUT_V15_SMPS
High-current
Logic supply 
(1.5 V)
CBULK_SMPS
VDD_DCDC
PMOS_CTRL
VSS_DCDC
Figure 31. SMPS circuit
6.5 V15 regulator (BJT option, NPN ballast transistor control) electrical specifications
Some devices (S32K358, S32K348, S32K338, S32K328, S32K344, S32K324, S32K314, S32K342, S32K322, S32K341) support 
a linear regulator stage, with a dedicated pin to control an external NPN bipolar transistor. The chip hardware design guidelines 
document lists the recommended part numbers for the external devices.
Table 13. V15 regulator (BJT option, NPN ballast transistor control) electrical specifications
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
V15
V15 output
—
1.51
—
V
—
—
V15
V15 input
—
1.5
—
V
—
—
IBCTL
IBCTL (V15 reg) 
source
10
—
—
mA
—
—
IBCTL
IBCTL (V15 reg) sink —
—
-50
uA
—
—
tsettle_lm
Required setting 
time from activating 
last mile regulator to 
load change
2
—
—
us
—
—
VDD_HV_NPN
Input voltage supply 
for NPN external 
ballast transistor
2.5
3.3 or 5
—
V
—
—
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
49 / 152


---
# 페이지 50

COUT_V15_NPN
Q_V15_NPN
RBTC15
V15
BJT option
External NPN
Ballast transistor
VDD_HV_NPN
V15
 PTE13 | VRC_CTRL
2.2k 
2.2uF  
High-current
Logic supply (1.5V)
IBCTL
Figure 32. Ballast circuit
6.6 V11 regulator (NMOS ballast transistor control) electrical specifications
The chip hardware design guidelines document lists the recommended part number for NMOS. The S32K388 and S32K389 
supports a  linear regulator stage for the V11 supply, with a dedicated pin to control an external NMOS transistor.
Table 14. V11 regulator (NMOS ballast transistor control) electrical specifications
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
V11
V11 output
—
1.14
—
V
—
—
VTH_NMOS
Vth of external 
NMOS
—
—
1.5
V
For 3.3 V supply
—
VTH_NMOS
Vth of external 
NMOS
—
—
2
V
For 5.0 V supply
—
IDS_NMOS
IDS of external 
NMOS
3
—
—
A
—
—
tsettle_lm
Required setting 
time from V11 in 
FPM to load change
10
—
—
us
—
—
CNMOS
NMOS gate stability 
capacitor
—
1
—
nF
—
—
6.7 Supply currents
 
All data in this table is preliminary and based on first samples.
  NOTE  
Typical current numbers are indicative for typical silicon process and may vary based on the silicon distribution and user 
configuration. Typical conditions assumes VDD_HV_A = VREFH = 5 V, VDD_HV_B = 5V (if the VDD_HV_B domain present in the 
device), temperature = 25 °C, and typical silicon process unless otherwise stated. In STANDBY configuration, no current flows 
through the V15 supply.
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
50 / 152


---
# 페이지 51

Table 15. STANDBY mode supply currents
Chip
Ambient Temperature (°C)
STANDBY 1
VDD_HV_A 2
VDD_HV_B 2
All clocks & 
peripherals 
OFF
(µA)
SIRC ON
(µA)
FIRC ON (24 
MHz)
(mA)
All Config.
(µA)
S32K389
25, typ 3
TBD
TBD
TBD
TBD
25, max 4
TBD
TBD
TBD
TBD
85, typ 3
TBD
TBD
TBD
TBD
85, max 4
TBD
TBD
TBD
TBD
105, typ 3
TBD
TBD
TBD
TBD
105, max 4
TBD
TBD
TBD
TBD
125, max 4
TBD
TBD
TBD
TBD
125, typ 3
TBD
TBD
TBD
TBD
S32K388
25, typ 3
74.0
74.0
2.236
3.5
25, max 4
233.2
236.4
2.658
5.6
85, typ 3
390.3
390.9
2.557
7.5
85, max 4
1165.2
1206.3
3.327
17.6
105, typ 3
747.5
747.9
2.915
14.3
105, max 4
2277.7
2352.5
4.319
38.4
125, typ 3
1389.9
1390.1
3.558
30.7
125, max 4
4192.3
4243.1
6.044
85.4
S32K358, 
S32K348, 
S32K338, S32K328
25, typ 3
64.9
67.1
1.5137
1.9
25, max 4
194.0
204.9
2.0132
3.9
85, typ 3
326.5
326.4
1.7222
6.1
85, max 4
1586.3
1621.4
3.2009
17.9
105, typ 3
617.8
621.6
2.0290
12.3
105, max 4
2977.6
2997.1
4.4926
33.8
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
51 / 152


---
# 페이지 52

Table 15. STANDBY mode supply currents (continued)
125, typ 3
1179.5
1180.2
2.5613
32.0
125, max 4
4997.2
5067.0
6.4388
77.8
S32K344, 
S32K324, S32K314
25, typ 3
50
52
0.91
1.8
25, max 4
153
153
1.09
3.8
85, typ 3
315
316
1.18
6.1
85, max4
900
910
1.78
15.4
105, typ 3
498
530
1.40
8.5
105, max 4
1672
1682
2.55
26.2
125, typ 3
932
998
1.88
18.5
125, max 4
2638
2650
3.5
47.3
S32K342, 
S32K322, S32K341
25, typ 3
46.5
49
0.900
1.8
25, max 4
88
94
1.090
3.5
85, typ 3
220.5
239.4
1.1619
5.4
85, max 4
627.0
642.9
1.587
13.9
105, typ 3
428.3
456.5
1.3638
7.3
105, max 4
1272.6
1301.6
2.2098
22.5
125, typ 3
715.2
745
1.6279
16.7
125, max 4
2113.4
2160.6
3.0016
41.6
S32K312
25, typ 3
40
41
0.887
NA
25, max 4
79
80
1.031
85, typ 3
178
178
1.027
85, max 4
496
497
1.422
105, typ 3
350
346
1.197
105, max 4
994
997
1.924
125, typ 3
620
611
1.457
125, max 4
1788
1792
2.761
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
52 / 152


---
# 페이지 53

Table 15. STANDBY mode supply currents (continued)
S32K311, S32K310 25, typ 3
38.9
39.8
1.365
NA
25, max 4
77.2
79.8
1.823
85, typ 3
144.3
144.9
1.480
85, max 4
491.5
494.8
2.263
105, typ 3
263.8
264.2
1.559
105, max 4
937.4
947.1
2.597
125, typ 3
508.5
510
1.811
125, max 4
1740.1
1760.3
3.488
1. See the configurations in Table 21.
2. IO load current is not included. The actual current requirements for IOs will depend on the I/O configuration in the 
application.
3. “typ” is indicative of the average current numbers at the nominal internally regulated V11 supply voltage, VDD_HV_A = 
5.0V, VDD_HV_B = 5.0V, for the typical silicon process..
4. “max” is indicative of the maximum current numbers at the maximum internally regulated V11 supply voltage (1.16 V), 
VDD_HV_A = 5.5V, VDD_HV_B = 5.5V, for the fast silicon process.
 
All data in this table is preliminary and based on first samples.
  NOTE  
Typical current numbers are indicative for typical silicon process and may vary based on the silicon distribution and user 
configuration. Typical conditions assumes VDD_HV_A = VREFH = 5 V, VDD_HV_B = 5V (if the VDD_HV_B domain present in the 
device), temperature = 25 °C, and typical silicon process unless otherwise stated.
Table 16. Low speed RUN mode supply currents
Chip
Ambient Temperature (°C)
Low Speed RUN Mode (mA) 1
BOOT Mode 2
[Clock Option C] FIRC @ 24 MHz
[Last Mile Disabled]
BOOT Mode 2
[Clock Option C] FIRC @ 24 MHz
[Last Mile Enabled]
Low Speed RUN 2
[Clock Option E] FIRC @3 MHz
[Last Mile Disabled]
Low Speed RUN 2
[Clock Option E] FIRC @3 MHz
[Last Mile Enabled]
Low Speed RUN 2
[Clock Option D] FIRC @48 MHz
[Last Mile Disabled]
Low Speed RUN 2
[Clock Option D] FIRC @48 MHz
[Last Mile Enabled]
All Config2.
VDD_HV_A 3, 4
V15 5/ V11 6
VDD_HV_A 3, 4
V15 5/ V116
VDD_HV_A 3, 4
V15 5/ V116
VDD_HV_A 3, 4
V15 5/ V116
VDD_HV_A 3, 4
V15 5/ V116
VDD_HV_A 3, 4
V15 5/ V116
VDD_HV_B 3
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
53 / 152


---
# 페이지 54

Table 16. Low speed RUN mode supply currents (continued)
S32K389
25, typ 7
NA
TBD
TBD
NA
TBD
TBD
NA
TBD
TBD
TBD
25, max 8
TBD
TBD
TBD
TBD
TBD
TBD
TBD
85, typ 7
TBD
TBD
TBD
TBD
TBD
TBD
TBD
105, typ 7
TBD
TBD
TBD
TBD
TBD
TBD
TBD
105, max 8
TBD
TBD
TBD
TBD
TBD
TBD
TBD
125, typ 7
TBD
TBD
TBD
TBD
TBD
TBD
TBD
125, 
max 8, 9
TBD
TBD
TBD
TBD
TBD
TBD
TBD
85, max 8
TBD
TBD
TBD
TBD
TBD
TBD
TBD
S32K388
25, typ 7
NA
2.7
43.0
NA
2.7
18.9
NA
2.7
70.4
2.4
25, max 8
3.8
153.6
3.1
129.2
3.9
180.7
2.8
85, typ 7
2.7
108.2
2.7
84.0
2.7
136.2
2.4
85, max 8
4.0
289.7
3.9
266.8
4.1
317.7
2.8
105, typ 7
2.8
216.8
2.8
192.7
2.9
243.7
2.4
105, max 8
4.2
534.9
4.2
516.1
4.3
558.8
2.8
125, typ 7
3.0
343.8
3.0
320.5
3.1
371.1
2.4
125, 
max 8, 9
5.5
936.1
5.3
915.7
5.6
960.0
2.8
S32K358, 
S32K348, 
S32K338, 
S32K328
25, typ 7
NA
3.1
34.1
NA
3.0
8.5
NA
3.2
63.3
1.6
25, max 8
3.6
52.7
3.5
26.4
3.7
83.0
2.4
85, typ 7
3.1
60.6
3.1
34.9
3.2
90.2
1.6
85, max 8
3.7
182.9
3.7
155.5
3.8
212.3
2.4
105, typ 7
3.2
88.4
3.2
62.4
3.3
117.8
1.6
105, max 8
3.9
297.2
3.9
273.9
4.0
323.4
2.4
125, typ 7
3.5
136.6
3.4
110.5
3.5
166.3
1.6
125, 
max 8, 9
4.5
494.9
4.4
468.6
4.7
521.0
2.4
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
54 / 152


---
# 페이지 55

Table 16. Low speed RUN mode supply currents (continued)
S32K344, 
S32K324, 
S32K314
25, typ 7
20.5
-
2.8
17.9
6.4
-
2.8
4.5
37.2
-
2.9
34
0.6
25, max8
29.4
-
3.3
27.2
14.8
-
3.3
12.6
46.8
-
3.4
46.6
0.8
85, typ 7
34.2
-
2.9
31.2
19.7
-
2.9
17.5
50.4
-
2.9
47.3
0.6
85, max 8
71.6
-
3.5
68.7
56.2
-
3.4
54
89.1
-
3.5
86.2
0.8
105, typ 7
46.1
-
2.9
43.1
31.7
-
2.9
29.3
62.2
-
2.9
59.2
0.6
105, max 8
114
-
3.7
111
99.1
-
3.6
96.1
131
-
3.9
128
0.8
125, typ 7
69.9
-
3.0
66.8
55.8
-
3.0
53.1
86
-
3.1
83
0.6
125, 
max 8, 9
161
-
4.2
159
148
-
4.1
145
178
-
4.3
176
0.8
S32K342, 
S32K322, 
S32K341
25, typ 7
19.6
-
2.8
17.6
6.0
-
2.8
4.0
36.2
-
2.9
33
0.5
25, max 8
25
-
3.3
24.9
8.8
-
3.3
8.2
41.4
-
3.4
40.8
0.8
85, typ 7
28.8
-
2.9
26.8
15.2
-
2.9
13.4
45.7
-
2.9
42.4
0.5
85, max 8
41.8
-
3.5
39.6
27.7
-
3.4
25.9
58.7
-
3.5
55.3
0.8
105, typ 7
38.6
-
2.9
36.9
25
-
2.9
23.3
55.6
-
2.9
52.4
0.5
105, max 8
63.1
-
3.7
61.5
49
-
3.7
46.5
80.1
-
3.9
77.2
0.8
125, typ 7
50.7
-
2.9
49.6
37.2
-
2.9
35.5
67.9
-
3.0
64.7
0.5
125, 
max 8, 9
88.2
-
4.1
88.5
75.3
-
4.0
73.3
105.2
-
4.2
103.1
0.8
S32K312
25, typ 7
15
NA
NA
5
NA
NA
26
NA
NA
NA
25, max 8
20
10
32
85, typ 7
20
10
31
85, max 8
35.2
24.6
46.4
105, typ 7
26.1
16.2
37
105, max 8
52.9
42.6
64.2
125, typ 7
35.3
25.3
46.4
125, 
max 8, 9, 10
79.8
66.9
90.1
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
55 / 152


---
# 페이지 56

Table 16. Low speed RUN mode supply currents (continued)
S32K311, 
S32K310
25, typ 7
12.9
NA
NA
4.4
NA
NA
22.4
NA
NA
NA
25, max 8
14.9
6.0
24.8
85, typ 7
16.0
7.5
25.6
85, max 8
31.0
22.2
41.1
105, typ 7
19.1
10.5
28.7
105, max 8
45.8
36.8
55.6
125, typ 7
25.2
16.5
34.7
125, 
max 8, 9, 10
73.2
64.3
82.4
1. Current numbers are for reduced configuration and may vary based on user configuration and silicon process variation.
2. See the example configurations in Table 21
3. IO load current is not included. The actual current requirements for IOs will depend on the I/O configuration in the 
application.
4. RUN IDD @ VDD_HV_A includes Flash memory read current from the V25 voltage rail.
5. RUN IDD @ V15 includes Flash memory read current from the V11 voltage rail
6. For S32K388, the current from a V15 supply will flow through the external NMOS for the V11 regulation stage, and into the 
V11 pins of the device.
7. “typ” is indicative of the average current numbers at the nominal internally regulated V11 supply voltage, VDD_HV_A = 
5.0V, VDD_HV_B = 5.0V, V15 = 1.5V, for the typical silicon process.
8. “max” is indicative of the maximum current numbers at the maximum internally regulated V11 supply voltage (1.16 V), 
VDD_HV_A = 5.5V, VDD_HV_B = 5.5V, V15 = 1.65V, for the fast silicon process.
9. For the maximum allowable RUN current in an application, the junction temperature must be kept below the maximum 
specification, TJ < 150°C, to avoid self-heating.
10. If the total power dissipation would cause the junction temperature to be exceeded when VDD_HV_A is at 5V, then 
VDD_HV_A should be limited to operate at 3.3V.
 
All data in this table is preliminary and based on first samples.
  NOTE  
Typical current numbers are indicative for typical silicon process and may vary based on the silicon distribution and user 
configuration. Typical conditions assumes VDD_HV_A = VREFH = 5 V, VDD_HV_B = 5V (if the VDD_HV_B domain present in the 
device), temperature = 25 °C and typical silicon process unless otherwise stated.
Table 17. RUN mode supply currents (peripherals disabled) for S32K3x8, S32K34x, S32K32x and S32K314
Chip
Ambient 
Temperature 
(°C)
RUN Mode (mA) 1
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
56 / 152


---
# 페이지 57

Table 17. RUN mode supply currents (peripherals disabled) for S32K3x8, S32K34x, S32K32x and S32K314 (continued)
Min. Config. 2 [Clock Option F]
Single Core @80 MHz
Min. Config. 2 [Clock Option B]
Single Core @120 MHz
Min. Config. 2 [Clock Option A]
Single Core @160 MHz
Min. Config. 2 [Clock Option F]
Dual Core @80 MHz
Min. Config. 2 [Clock Option B]
Dual Core @120 MHz
Min. Config. 2 [Clock Option A]
Dual Core @160 MHz
Min. Config. 2 [Clock Option A+]
Triple Core @240 MHz
Min. Config. 2 [Clock Option A++]
1xLS + 3xCores @320 MHz
All. Config. 2
All. Config. 2
V15 3/ V11 4
V15 3/ V114
V15 3/ V114
V15 3/ V114
V15 3/ V114
V15 3/ V114
V15 3/ V114
V15 3/ V114
VDD_HV_B 5
VDD_HV_A 5, 6
S32K389
25, typ 7,10
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
25, max 8,11
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
85, typ 10
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
85, max 11
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
105, typ 10
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
105, max 11
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
125, typ 10
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
125, 
max11, 9,12
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
S32K388
25, typ 10
NA
196.2
NA
231.4
339.4
440.3
2.4
3.6
25, max 11
291.4
318.4
456.6
565.3
2.8
4.3
85, typ 10
277.1
312.6
420.9
520.5
2.4
3.7
85, max 11
500.8
533.3
634.3
745.9
2.8
4.6
105, typ 10
351.8
387.2
495.3
593.8
2.4
3.8
105, max 11
703.3
737.6
837.6
951.5
2.8
5.1
125, typ 10
468.7
503.5
610.4
707.9
2.4
4.0
125, 
max11, 12
993.5
1040.0
1147.0
1254.1
2.8
5.7
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
57 / 152


---
# 페이지 58

Table 17. RUN mode supply currents (peripherals disabled) for S32K3x8, S32K34x, S32K32x and S32K314 (continued)
S32K358, 
S32K348, 
S32K338, 
S32K328
25, typ10
100.6
118.9
144.8
103.3
124.1
166.6
NA
NA
1.8
4.8
25, max11
119.8
138.9
165.6
122.8
144.4
186.3
3.0
5.4
85, typ 10
126.9
145.3
171.6
129.8
150.9
193.8
1.8
6.1
85, max 11
248.1
267.7
294.4
250.8
274.3
317.6
3.0
6.7
105, typ 10
153.4
172.0
198.4
156.6
178.0
221.2
1.8
6.1
105, max 11
349.5
371.6
398.2
358.3
381.4
423.7
3.0
6.9
125, typ 10
199.3
218.2
245.0
203.3
225.0
268.3
1.8
6.4
125, 
max11, 12
529.7
551.2
580.9
538.0
563.3
603.0
3.0
7.4
S32K344, 
S32K324, 
S32K314
25, typ 10
51.3
54.8
69.6
62.7
75.1
97.5
NA
NA
0.6
3.1
25, max 11
60.2
64.5
80.4
73.3
86.8
110
0.8
3.6
85, typ 10
64.5
68.1
83.1
76.2
89
111
0.6
3.2
85, max 11
104
108
124
117
131
155
0.8
3.9
105, typ 10
75.4
79
93.9
87.3
100
122.6
0.6
3.2
105, max 11
145
149
166
159
173
197
0.8
4.0
125, typ 10
97.4
101.2
116.4
110
122.9
145.7
0.6
3.3
125, 
max 11, 12
191
196
212
206
220
245
0.8
4.3
S32K342, 
S32K322, 
S32K341
25, typ 10
49.5
52.2
66.3
58.9
72.7
93.7
0.5
3.0
25, max 11
58.5
62.4
75.9
68.1
82.9
104.6
NA
NA
0.8
3.6
85, typ 10
58.6
63.6
75.7
67.9
82.3
106.1
0.5
3.0
85, max 11
89.6
102.3
110.8
105.4
124.1
155
0.8
3.8
105, typ 10
68.3
76
85.6
80
92.3
119.3
0.5
3.1
105, max 11
124
143.4
157.5
150.5
164.5
191.6
0.8
4.0
125, typ 10
79.8
85.1
97.1
89.1
103.8
140.1
0.5
3.2
125, 
max 11, 12
146.7
164.7
178
171.3
188.7
235.6
0.8
4.2
1. Current numbers are for reduced configuration and may vary based on user configuration and silicon process variation.
2. See the configurations in Table 22.
3. RUN IDD @ V15 includes Flash memory read current from the V11 voltage rail.
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
58 / 152


---
# 페이지 59

4. For S32K388, the current from a V15 supply will flow through the external NMOS for the V11 regulation stage, and into the 
V11 pins of the device.
5. IO load current is not included. The actual current requirements for IOs will depend on the I/O configuration in the 
application.
6. RUN IDD @ VDD_HV_A includes Flash memory read current from the V25 voltage rail.
7. “typ” is indicative of the average current numbers at the nominal internally regulated V11 supply voltage, VDD_HV_A = 
5.0V, VDD_HV_B = 5.0V, V15 = 1.5V, for the typical silicon process.
8. "max" is indicative of the maximum current numbers at the maximum internally regulated V11 supply voltage (1.16 V), 
VDD_HV_A = 5.5V, VDD_HV_B = 5.5V, V15= 1.65V, for the fast silicon process.
9. For the maximum allowable RUN current in an application, the junction temperature must be kept below the maximum 
specification, TJ < 150°C, to avoid self-heating.
10. “typ” is indicative of the average current numbers at the nominal internally regulated V11 supply voltage, VDD_HV_A = 
5.0V, VDD_HV_B = 5.0V, V15 = 1.5V, for the typical silicon process.
11. "max" is indicative of the maximum current numbers at the maximum internally regulated V11 supply voltage (1.16 V), 
VDD_HV_A = 5.5V, VDD_HV_B = 5.5V, V15= 1.65V, for the fast silicon process.
12. For the maximum allowable RUN current in an application, the junction temperature must be kept below the maximum 
specification, TJ < 150°C, to avoid self-heating.
 
The data in this table is preliminary and based on first samples.
  NOTE  
Typical current numbers are indicative for typical silicon process and may vary based on the silicon distribution and user 
configuration. Typical conditions assumes VDD_HV_A = VREFH = 5 V, VDD_HV_B = 5V (if the VDD_HV_B domain present in the 
device), temperature = 25 °C and typical silicon process unless otherwise stated.
Table 18. RUN mode supply currents (peripherals disabled) for S32K312, S32K311, S32K310
Chip
Ambient 
Temperature (°C)
RUN Mode (mA) 1
Min. Config. 2
Single Core @80 MHz
[Clock Option F]
Min. Config. 2
Single Core @120 MHz
[Clock Option B]
VDD_HV_A 3, 4
V15 5/ V11
VDD_HV_A 3, 4
V15 5/ V11
S32K312
25, typ 6
37
NA
37
NA
25, max 7
44
47
85, typ 6
42
43
85, max 7
58.5
59.7
105, typ 6
48.1
48.7
105, max 7
76.4
77.8
125, typ 6
56.5
57
125, max 7, 8, 9
98.7
99.9
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
59 / 152


---
# 페이지 60

Table 18. RUN mode supply currents (peripherals disabled) for S32K312, S32K311, S32K310 (continued)
S32K311 , S32K310
25, typ 6
34.9
NA
36.5
NA
25, max 7
39.1
41.1
85, typ 6
38.1
39.8
85, max 7
54.2
55.9
105, typ 6
41.5
43.2
105, max 7
69.1
71.1
125, typ 6
47.7
49.4
125, max 7, 8, 9
97
99.1
1. Current numbers are for reduced configuration and may vary based on user configuration and silicon process variation.
2. See the configurations in Table 22.
3. IO load current is not included. The actual current requirements for IOs will depend on the I/O configuration in the 
application.
4. RUN IDD @ VDD_HV_A includes Flash memory read current from the V25 voltage rail.
5. RUN IDD @ V15 includes Flash memory read current from the V11 voltage rail.
6. “typ” is indicative of the average current numbers at the nominal internally regulated V11 supply voltage, VDD_HV_A = 
5.0V, VDD_HV_B = 5.0V, V15 = 1.5V, for the typical silicon process.
7. “max” is indicative of the maximum current numbers at the maximum internally regulated V11 supply voltage (1.16 V), 
VDD_HV_A = 5.5V, VDD_HV_B = 5.5V, V15 = 1.65V, for the fast silicon process.
8. For the maximum allowable RUN current in an application, the junction temperature must be kept below the maximum 
specification, TJ < 150°C, to avoid self-heating.
9. If the total power dissipation would cause the junction temperature to be exceeded when VDD_HV_A is at 5V, then 
VDD_HV_A should be limited to operate at 3.3V.
 
The data in this table is preliminary and based on first samples.
  NOTE  
Typical current numbers are indicative for typical silicon process and may vary based on the silicon distribution and user 
configuration. Typical conditions assumes VDD_HV_A = VREFH = 5 V, VDD_HV_B = 5V (if the VDD_HV_B domain present in the 
device), temperature = 25 °C and typical silicon process unless otherwise stated.
Table 19. Example RUN mode configuration supply currents for S32K3x8, S32K34x, S32K32x and S32K314
Chip
Ambient 
Temperature 
(°C)
RUN Mode (mA) 1
Config. 1 2
Dual Core @160 MHz
Config. 2 2
Single Core @160 MHz
Config. 3 2
Dual Core @120 MHz
Config. 4 2
Single Core @120 MHz
Config. 5 2
Single Core @80 MHz
Config. 6-1 2
Dual Core @240 MHz
Config. 6-2 2
Triple Core @240 MHz
Config. 7 2
All Config. 2
All Config. 2
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
60 / 152


---
# 페이지 61

Table 19. Example RUN mode configuration supply currents for S32K3x8, S32K34x, S32K32x and S32K314 (continued)
1xLS + 3x Core (with AES and 
ENET2 enabled)@320 MHz
V15 3/V114
V15 3/ V114
V15 3/ V114
V15 3/ V114
V15 3/ V114
V15 3/ V114
V15 3/ V114
V15 3/ V114
VDD_HV_B 5
VDD_HV_A 5, 6
S32K389
25, typ 7
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
25, max 8
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
85, typ 7
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
85, max 8
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
105, typ 7
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
125, typ 7
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
125, max 8, 9
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
105, max 8
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
TBD
S32K388
25, typ 7
255.4
241.3
NA
310.8
393.1
620.1
3.0
3.8
25, max 8
382.6
378.0
424.4
525.5
774.2
3.3
4.5
85, typ 7
324.3
309.5
392.6
474.5
701.5
3.0
3.8
85, max 8
499.7
501.2
610.4
712.3
952.4
3.3
4.7
105, typ 7
426.8
425.1
466.9
548.5
774.5
3.0
3.9
105, max 8
731.2
738.1
823.2
918.7
1160.6
3.3
5.2
125, typ 7
554.5
538.7
582.4
663.4
887.5
3.0
4.1
125, max 8, 9
1128.4
1121.0
1169.6
1227.0
1467.4
3.3
5.9
S32K358, 
S32K348, 
25, typ 7
207.6
168.6
177.5
146.8
114.9
313
380.2
NA
2.1
5.3
25, max 8
229.4
188.3
197.4
167.9
135.3
340
395.9
3.2
6.0
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
61 / 152


---
# 페이지 62

Table 19. Example RUN mode configuration supply currents for S32K3x8, S32K34x, S32K32x and S32K314 (continued)
S32K338, 
S32K328
85, typ 7
235.5
195.9
205.1
174.0
141.6
333.4
413.6
2.1
6.3
85, max 8
363.7
322.1
331.3
299.2
263.2
418.5
552.8
3.2
7.1
105, typ 7
263.5
223.5
233.0
201.5
168.9
360.4
446.1
2.1
6.4
105, max 8
472.4
429.8
438.8
407.1
369.8
516.5
682.8
3.2
7.1
125, typ 7
311.9
271.3
281.0
249.0
216.2
413.8
501.0
2.1
6.7
125, max 8, 9
661.0
618.2
624.6
588.8
554.2
707
844.0
3.2
7.9
S32K344, 
S32K324, 
S32K314
25, typ 7
119
102
106
80
68
NA
NA
NA
0.6
3.1
25, max 8
133
115
119
92
79
0.8
3.6
85, typ 7
134
116
120
94
81.8
0.6
3.2
85, max 8
180
160
165
137
123
0.8
3.9
105, typ 7
145
128
132
105
93
0.6
3.2
105, max 8
222
203
208
179
165
0.8
4.0
125, typ 7
169
151
155
128
116
0.6
3.3
125, max 8, 9
271
250
256
226
213
0.8
4.5
S32K342, 
S32K322, 
S32K341
25, typ 7
115.3
93.2
96.1
79.6
64.1
NA
NA
NA
0.5
3.0
25, max 8
128.9
109.3
109.8
90.9
74.5
0.8
3.6
85, typ 7
125.0
102.7
105.8
89.2
73.6
0.5
3.0
85, max 8
178.8
126.5
132.0
105.0
92.5
0.8
3.6
105, typ 7
135.2
111.9
115.5
98.6
83.4
0.5
3.1
105, max 8
219.6
184.6
188.5
168.5
152.5
0.8
3.8
125, typ 7
145.8
123.8
127.3
110.2
94.7
0.5
3.1
125, max 8, 9
258.1
235.2
243.9
206.9
183.7
0.8
4.3
1. Current numbers are for reduced configuration and may vary based on user configuration and silicon process variation.
2. See the configurations in Table 22.
3. RUN IDD @ V15 includes Flash memory read current from the V11 voltage rail.
4. For S32K388, the current from a V15 supply will flow through the external NMOS for the V11 regulation stage, and into the 
V11 pins of the device.
5. IO current is not included. The actual current requirements for IOs will depend on the I/O configuration in the application.
6. RUN IDD @ VDD_HV_A includes Flash memory read current from the V25 voltage rail.
7. “typ” is indicative of the average current numbers at the nominal internally regulated V11 supply voltage, VDD_HV_A = 
5.0V, VDD_HV_B = 5.0V, V15 = 1.5V, for the typical silicon process.
8. “max” is indicative of the maximum current numbers at the maximum internally regulated V11 supply voltage (1.16 V), 
VDD_HV_A = 5.5V, VDD_HV_B = 5.5V, V15 = 1.65V, for the fast silicon process.
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
62 / 152


---
# 페이지 63

9. For the maximum allowable RUN current in an application, the junction temperature must be kept below the maximum 
specification, TJ < 150°C, to avoid self-heating.
Table 20. Example RUN mode configuration supply currents for S32K312, S32K311, S32K311
Chip
Ambient 
Temperature (°C)
RUN Mode (mA) 1
Config. 4 2
Single Core
@120 MHz
Config. 5 2
Single Core
@80 MHz
VDD_HV_A 3, 4
V15 5/V11
VDD_HV_A 3, 4
V15 5/ V11
S32K312
25, typ 6
54
NA
44
NA
25, max 7
62
54
85, typ 6
60
49
85, max 7
76.4
66.3
105, typ 6
65.8
55
105, max 7
94.4
84.4
125, typ 6
78.6
64.7
125, max 7, 8, 9
120.7
110.5
S32K311, S32K310
25, typ 6
53.4
NA
43
NA
25, max 7
57.7
51.2
85, typ 6
56.8
50.8
85, max 7
73.2
66
105, typ 6
60.1
54
105, max 7
88.5
81.9
125, typ 6
66.3
60.2
125, max 7, 8,9
115.3
109.3
1. Current numbers are for reduced configuration and may vary based on user configuration and silicon process variation.
2. See the configurations in Table 22.
3. IO current is not included. The actual current requirements for IOs will depend on the I/O configuration in the application.
4. RUN IDD @ VDD_HV_A includes Flash memory read current from the V25 voltage rail.
5. RUN IDD @ V15 includes Flash memory read current from the V11 voltage rail.
6. “typ” is indicative of the average current numbers at the nominal internally regulated V11 supply voltage, VDD_HV_A = 5.0V, 
VDD_HV_B = 5.0V, V15 = 1.5V, for the typical silicon process
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
63 / 152


---
# 페이지 64

7. "max” is indicative of the maximum current numbers at the maximum internally regulated V11 supply voltage (1.16 V), 
VDD_HV_A = 5.5V, VDD_HV_B = 5.5V, V15 = 1.65V, for the fast silicon proce
8. For the maximum allowable RUN current in an application, the junction temperature must be kept below the maximum 
specification, TJ < 150°C, to avoid self-heating.
9. If the total power dissipation would cause the junction temperature to be exceeded when VDD_HV_A is at 5V, then VDD_HV_A 
should be limited to operate at 3.3V.
6.8 Operating mode
Table 21. STANDBY and low speed RUN configuration options
MODULE
STANDBY
All OFF
STANDBY
SIRC ON
STANDBY
FIRC ON
BOOT Mode 
(OptionC1, FIRC 
@24 MHz)
Low Speed RUN 
(OptionE 1, FIRC 
@ 3MHz)
FIRC Mode
(OptionD 1, FIRC 
@48 MHz)
Core M7_0/1
OFF
OFF
OFF
24 MHz
3 MHz
48 MHz
HSE_B
OFF
OFF
OFF
24 MHz
3 MHz
48 MHz
FIRC
OFF
OFF
24 MHz
24 MHz
3 MHz
48 MHz
FXOSC
OFF
OFF
OFF
OFF
OFF
OFF
SIRC
OFF
ON
OFF
ON
ON
ON
PLL
OFF
OFF
OFF
OFF
OFF
OFF
Flash
OFF
OFF
OFF
ON
ON
ON
eDMA
OFF
OFF
OFF
ON
ON
ON
FlexCAN
All OFF
All OFF
All OFF
All OFF
All OFF
All OFF
LPUART
All OFF
All OFF
All OFF
All OFF
All OFF
All OFF
LPSPI
All OFF
All OFF
All OFF
All OFF
All OFF
All OFF
LPI2C
All OFF
All OFF
All OFF
All OFF
All OFF
All OFF
EMAC/GMAC
OFF
OFF
OFF
OFF
OFF
OFF
eMIOS
All OFF
All OFF
All OFF
All OFF
All OFF
All OFF
SAR_ADC
All OFF
All OFF
All OFF
All OFF
All OFF
All OFF
LPCMP
All OFF
All OFF
All OFF
All OFF
All OFF
All OFF
1. See clocking use case examples in the Clocking chapter of the S32K3xx Reference Manual.
Table 22. RUN mode configuration options
MODU
LE
Min. 
Config. 
(Optio
Min. 
Config. 
(Optio
Min. 
Config. 
(Optio
Min. 
Config. 
(Optio
nA+1), 
Min. 
Config. 
(Optio
nA+
Config. 
1
Config. 
2
Config. 
3
Config. 
4
Config. 
5
Config. 
6-1
Config. 
6-2
Config. 
7
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
64 / 152


---
# 페이지 65

Table 22. RUN mode configuration options (continued)
nF1), 
PLL@
80 
MHz
nB1), 
PLL@
120 
MHz
nA1), 
PLL@
160 
MHz
PLL@
240 
MHz
+1), 
PLL@
320 
MHz
Dual 
Core
@160
MHz
Single 
Core
@160
MHz
Dual 
Core
@120
MHz
Single 
Core
@120
MHz
Single 
Core
@80M
Hz
Dual 
Core
@240
MHz
Triple 
Core
@240
MHz
1xLS + 
3x 
cores
@320 
MHz
Core 
M7_0
80 
MHz
120 
MHz
160 
MHz
240 
MHz
320 
MHz
160 
MHz
160 
MHz
120 
MHz
120 
MHz
80 
MHz
240 
MHz
240 
MHz
320 
MHz
Core 
M7_1
80 
MHz
120 
MHz
160 
MHz
240 
MHz
320 
MHz
160 
MHz
-
120 
MHz
-
-
240 
MHz
240 
MHz
320 
MHz
Core 
M7_2
-
-
-
240 
MHz
320 
MHz
-
-
-
-
-
-
240 
MHz
320 
MHz
Core 
M7_3
-
-
-
-
320 
MHz
-
-
-
-
-
-
-
320 
MHz
HSE_B
2
80 
MHz
120 
MHz
80 
MHz
120 
MHz
160 
MHz
80 
MHz
80 
MHz
120 
MHz
120 
MHz
80 
MHz
120 
MHz
120 
MHz
160 
MHz
FIRC
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
FXOS
C
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
SIRC
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
PLL
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
Flash
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
eDMA
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
ON
FlexC
AN3
All 
OFF
All 
OFF
All 
OFF
All 
OFF
All 
OFF
6x
2x
4x
6x
1x
8x
8x
8x
LPUA
RT4
All 
OFF
All 
OFF
All 
OFF
All 
OFF
All 
OFF
16x
4x
10x
8x
7x
16x
16x
16x
LPSPI
5
All 
OFF
All 
OFF
All 
OFF
All 
OFF
All 
OFF
6x
4x
4x
4x
3x
5x
5x
5x
LPI2C6
All 
OFF
All 
OFF
All 
OFF
All 
OFF
All 
OFF
All 
OFF
2x
2x
2x
All 
OFF
1x
1x
1x
EMAC/
GMAC
7
OFF
OFF
OFF
OFF
OFF
ON
OFF
ON
OFF
OFF
ON
ON
ON
SAI
OFF
OFF
OFF
OFF
OFF
OFF
OFF
OFF
OFF
OFF
OFF
OFF
OFF
Table continues on the next page...
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
65 / 152


---
# 페이지 66

Table 22. RUN mode configuration options (continued)
QSPI
OFF
OFF
OFF
OFF
OFF
OFF
OFF
OFF
OFF
OFF
ON
ON
ON
eMIOS
8
All 
OFF
All 
OFF
All 
OFF
All 
OFF
All 
OFF
All 
OFF
3x
3x
2x
2x
2x
2x
2x
SAR_A
DC9
All 
OFF
All 
OFF
All 
OFF
All 
OFF
All 
OFF
All 
OFF
3x
3x
2x
2x
3x
3x
3x
LPCM
P10
All 
OFF
All 
OFF
All 
OFF
All 
OFF
All 
OFF
All 
OFF
2x
3x
All 
OFF
All 
OFF
OFF
OFF
OFF
1. See clocking use case examples in the Clocking chapter of the S32K3xx Reference Manual.
2. HSE_B: After start-up, the HSE core is in WFI.
3.
• FlexCAN0: Transmitting an 8-byte CAN-FD data frame at 5 Mbps, every 10 ms.
• FlexCAN1: Transmitting a 64-byte CAN-FD data frame at 2 Mbps, every 20 ms.
• FlexCAN2-5: Transmitting an 8-byte CAN data frame at 500 Kbps, every 20 ms.
4. LPUART0-15: Transmitting at 19200 bps, every 100ms.
5.
• LPSPI0: Transmitting 32 bits at 20 Mbps (GPIO Fast pads), every 5 ms.
• LPSPI1-5: Transmitting 32 bits at 1 Mbps, every 5 ms.
6. LPI2C0-1: Transmitting 3 bytes at 400 Kbps, every 100ms.
7. EMAC/GMAC: ON for MII interface.
8.
• eMIOS0: 6 channels in PWM mode @ 20 KHz.
• eMIOS1-2: 8 channels in PWM mode @ 400 Hz.
9.
• SAR_ADC0: 16 channels at 400 Hz rate, BCTU triggered.
• SAR_ADC1-2: 4 channels at 20 KHz rate, BCTU triggered.
10. LPCMP0: 8 channels enabled; LPCMP1-2: 4 channels enabled.
6.9 Cyclic wake-up current
The cyclic wake-up current is the calculated average current consumption during the periodic switching between RUN mode and 
STANDBY mode. This average current can be calculated with the following formula:
ICYCL = RUN Current According to Ratio + STANDBY Current According to Ratio
Where the Current According to Ratio value is calculated as follows:
Current According to Ratio = Supply Current × Ratio of Duration
As an example, the following data was obtained with an application that periodically (every 40ms) alternates between RUN mode, 
for approximately 200μs to scan several GPIO inputs (51 GPIOS), and spends the rest of the time in STANDBY mode.
Table 23. Cyclic wake-up current example
Chip
Device 
Operating Mode
Supply Current1 
[μA]
Duration 2 [ms]
Ratio of 
Duration 3
Current 
According to 
Ratio 4 [μA]
ICYCL - 
Average current
5 [μA]
S32K314
RUN
20000
0.2
0.005
100
159.7
STANDBY
60
39.8
0.995
59.7
1. The supply current is obtained through the measurements of the current during the corresponding operating mode.
2. The duration is defined by the application (how much time will the device spend in the according operating mode).
3. The ratio of duration is obtained by dividing the duration of the corresponding operating mode by the total duration of the 
application.
4. The current according to ratio is obtained by multiplying the supply current and the ratio of duration related to the proper 
operating mode.
NXP Semiconductors
Power management
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
66 / 152


---
# 페이지 67

5. The average current is calculated by the addition of each device operating mode’s current according to ratio.
7 I/O parameters
7.1 GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V)
The leakage current on the GPIO pins is specified as a function of the pad type (Standard, Standard Plus, Medium, Fast, or GPI) 
and the number of Analog functions (CMP and ADC channels) multiplexed per pin.
For S32K388, see the ILKG column in the Pinout section of the IOMUX file attached to the Reference Manual.
For other devices, the "Analog Function Count" is defined from the number of CMP and ADC channels multiplexed to a given 
pin. This information can be obtained from the "Direct Signals" column in the IOMUX files attached to the Reference Manual. The 
"Analog Function Count" is shown in the Condition column of the following table.
Table 24. GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
VIH
Input high level DC 
voltage threshold
0.70 x 
VDD_HV
_A/B
—
VDD_HV
_A/B + 
0.3
V
VDD_HV_A/B = 3.3V
—
VIL
Input low level DC 
voltage threshold
VSS - 0.3 —
0.30 x 
VDD_HV
_A/B
V
VDD_HV_A/B = 3.3V
—
WFRST
RESET Input 
Filtered pulse width 1
—
—
33
ns
—
—
WNFRST
RESET Input not 
filtered pulse width 2
100
—
—
ns
—
—
ILKG_33_S0
3.3V input leakage 
current for Standard 
GPIO 3
-133
—
300
nA
Pins with Analog 
Function Count = 0
—
ILKG_33_S1
3.3V input leakage 
current for Standard 
GPIO 3
-545
—
445
nA
Pins with Analog 
Function Count = 1
—
ILKG_33_S2
3.3V input leakage 
current for Standard 
GPIO 3
-749
—
517
nA
Pins with Analog 
Function Count = 2, 
plus PTA12, PTD1
—
ILKG_33_S3
3.3V input leakage 
current for Standard 
GPIO 3
-1288
—
679
nA
Pins with Analog 
Function Count = 3, 
plus PTD0
—
ILKG_33_S_PTE13
3.3V input leakage 
current for Standard 
GPIO 3
-1935
—
483
nA
PMC VRC_CTRL pin
—
ILKG_33_SP0
3.3V input leakage 
current for Standard 
Plus GPIO and 
RESET IO 3
-370
—
575
nA
Pins with Analog 
Function Count = 0
—
Table continues on the next page...
NXP Semiconductors
I/O parameters
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
67 / 152


---
# 페이지 68

Table 24. GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V) (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
ILKG_33_SP1
3.3V input leakage 
current for Standard 
Plus GPIO and 
RESET IO 3
-660
—
659
nA
Pins with Analog 
Function Count = 1
—
ILKG_33_SP2
3.3V input leakage 
current for Standard 
Plus GPIO and 
RESET IO 3
-1094
—
794
nA
Pins with Analog 
Function Count = 2
—
ILKG_33_M0
3.3V GPIO input 
leakage current for 
Medium GPIO 3
-792
—
750
nA
Pins with Analog 
Function Count = 0
—
ILKG_33_M1
3.3V GPIO input 
leakage current for 
Medium GPIO 3
-989
—
824
nA
Pins with Analog 
Function Count = 1, 
plus PTC16, PTD5
—
ILKG_33_M2
3.3V GPIO input 
leakage current for 
Medium GPIO 3
-1233
—
1248
nA
Pins PTD6 and PTE8
—
ILKG_33_F0
3.3V GPIO input 
leakage current for 
Fast GPIO 3
-1139
—
1178
nA
Pins with Analog 
Function Count = 0
—
ILKG_33_F1
3.3V GPIO input 
leakage current for 
Fast GPIO 3
-1464
—
1239
nA
Pins with Analog 
Function Count = 1
—
ILKG_33_I
3.3V input leakage 
current for GPI 3
-120
—
120
nA
—
—
VHYS_33
Input hysteresis 
voltage 4
0.06 x 
VDD_HV
_A/B
—
—
mV
Always Enabled, 
Applies to S32K34x, 
S32K3x8, S32K32x 
and S32K314 devices.
—
VHYS_33
Input hysteresis 
voltage
0.06 x 
VDD_HV
_A/B
—
—
mV
Always Enabled, 
Applies to S32K311, 
S32K312, and 
S32K310 devices.
—
CIN
GPIO Input 
capacitance
2
4
6
pF
add 2pF for package/
parasitic
—
IPU_33
3.3V GPIO pull up/
down resistance
20
—
60
kΩ
pull up @ 0.3 x VDD_
HV_A/B, pull down @ 
0.7 x VDD_HV_A/B
—
IOH_33_S
3.3V output 
high current for 
Standard GPIO 5,6
1.0
—
—
mA
VOH >= VDD_HV_A/B 
- 0.7V
—
Table continues on the next page...
NXP Semiconductors
I/O parameters
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
68 / 152


---
# 페이지 69

Table 24. GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V) (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
IOH_33_SP
3.3V output high 
current for Standard 
Plus GPIO and 
RESET IO 5,6
1.5
—
—
mA
DSE = 0, VOH >= 
VDD_HV_A/B - 0.7V
—
IOH_33_M
3.3V output high 
current for Medium 
GPIO 5,6
3
—
—
mA
DSE = 0, VOH >= 
VDD_HV_A/B - 0.7V
—
IOH_33_F
3.3V output high 
current for Fast 
GPIO 5,6
4.5
—
—
mA
DSE = 0, VOH >= 
VDD_HV_A/B - 0.7V
—
IOH_33_SP
3.3V output high 
current for Standard 
Plus GPIO and 
RESET IO 5,6
3
—
—
mA
DSE = 1, VOH >= 
VDD_HV_A/B - 0.7V
—
IOH_33_M
3.3V output high 
current for Medium 
GPIO 5,6
6
—
—
mA
DSE = 1, VOH >= 
VDD_HV_A/B - 0.7V
—
IOH_33_F
3.3V output high 
current for Fast 
GPIO 5,6
9
—
—
mA
DSE = 1, VOH >= 
VDD_HV_A/B - 0.7V
—
IOL_33_S
3.3V output low 
current for Standard 
GPIO 5,6
1.0
—
—
mA
VOL <= 0.7V
—
IOL_33_SP
3.3V output low 
current for Standard 
Plus GPIO and 
RESET IO 5,6
1.5
—
—
mA
DSE =0, VOL <= 0.7V
—
IOL_33_M
3.3V output low 
current for Medium 
GPIO 5,6
3.0
—
—
mA
DSE =0, VOL <= 0.7V
—
IOL_33_F
3.3V output low 
current for Fast 
GPIO 5,6
4.5
—
—
mA
DSE =0, VOL <= 0.7V
—
IOL_33_SP
3.3V output low 
current for Standard 
Plus GPIO and 
RESET IO 5,6
3
—
—
mA
DSE =1, VOL <= 0.7V
—
IOL_33_M
3.3V output low 
current for Medium 
GPIO 5,6
6
—
—
mA
DSE =1, VOL <= 0.7V
—
Table continues on the next page...
NXP Semiconductors
I/O parameters
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
69 / 152


---
# 페이지 70

Table 24. GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V) (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
IOL_33_F
3.3V output low 
current for Fast 
GPIO 5,6
9
—
—
mA
DSE =1, VOL <= 0.7V
—
FMAX_33_S
3.3V maximum 
frequency for 
Standard GPIO 5,7
—
—
10
MHz
2.9V - 3.6V CL(max) = 
25pF
—
FMAX_33_SP
3.3V maximum 
frequency for 
Standard Plus 
GPIO 5,7
—
—
25
MHz
2.9V - 3.6V CL (max) = 
25pF
—
FMAX_33_M
3.3V maximum 
frequency for 
Medium GPIO 5,7
—
—
50
MHz
2.9V - 3.6V CL (max) = 
25pF
—
FMAX_33_F
3.3V maximum 
frequency for Fast 
GPIO 5,7
—
—
120
MHz
2.9V - 3.6V CL(max) = 
25pF, for all S32K3xx 
except S32K3x8 
devices
—
FMAX_33_F
3.3V maximum 
frequency for Fast 
GPIO 5,7
—
—
125
MHz
2.9V - 3.6V, CL (max) 
= 25pF, for S32K3x8 
devices
—
IOHT
Output high current 
total for all ports 8
—
—
100
mA
—
—
1. Maximum length of RESET pulse will be filtered by an internal filter on this pin.
2. Minimum length of RESET pulse,  guaranteed not to be filtered by the internal filter.
3. A positive value is leakage flowing into pin with pin at VDD_HV_A/B (the GPIO supply level); a negative value is leakage 
flowing out the pin with the pin at ground.
4. Hysteresis spec does not apply to fast pad
5. GPIO output transition time information can be obtained from the device IBIS model. IBIS models are recommended for 
system level simulations, as discrete values for I/O transition times are not representative of the I/O pad behavior when 
connected to an actual transmission line load.  
6. I/O output current specifications are valid for the given reference load figure, and the constraints given in the Operating 
Conditions of this document.
7. I/O timing specifications are valid for the un-terminated 50ohm transmission line reference load given in the figure below. 
A lumped 8pF load is assumed in addition to a 5 inch microstrip trace on standard FR4 with approximately 3.3pF/inch. For 
signals with frequency greater than 63MHz, a maximum 2 inch PCB trace is assumed. For best signal integrity, the series 
resistance in the transmission line should be matched closely to the selected output resistance (ROUT_*) of the I/O pad.
8. To determine total switching current on any I/O supply, current values per output pin should not be incrementally summed. 
I/O interfaces on the device are asynchronous to each other, so not all switching occurs at the same instant. Actual use 
case must be considered.
NXP Semiconductors
I/O parameters
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
70 / 152


---
# 페이지 71

RDSON
RPCB = RDSON
PCB
External
device
MCUsee note 1
RDSON
5 in.
(4 layer FR4)
CPCB = ~3.3 pF/inch  * 5 inch 
CL = 8 pF
1. See IBIS models for further details.
Notes:
Figure 33. Reference Load Diagram
7.2 GPIO DC electrical specifications, 5.0V (4.5V - 5.5V)
The leakage current on the GPIO pins is specified as a function of the pad type (Standard, Standard Plus, Medium, Fast, or GPI) 
and the number of Analog functions (CMP and ADC channels) multiplexed per pin.
For S32K388, see the ILKG column in the Pinout section of the IOMUX file attached to the Reference Manual.
For other devices, the "Analog Function Count" is defined from the number of CMP and ADC channels multiplexed to a given 
pin. This information can be obtained from the "Direct Signals" column in the IOMUX files attached to the Reference Manual. The 
"Analog Function Count" is shown in the Condition column of the following table.
Table 25. GPIO DC electrical specifications, 5.0V (4.5V - 5.5V)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
VIH
Input high level DC 
voltage threshold
0.65 x 
VDD_HV
_A/B
—
VDD_HV
_A/B + 
0.3
V
VDD_HV_A/B = 5.0V
—
VIL
Input low level DC 
voltage threshold
VSS - 0.3 —
0.35 x 
VDD_HV
_A/B
V
VDD_HV_A/B = 5.0V
—
WFRST
RESET Input filtered 
pulse width 1
—
—
33
ns
—
—
WNFRST
RESET Input not 
filtered pulse width 2
100
—
—
ns
—
—
ILKG_50_S0
5.0V input leakage 
current for Standard 
GPIO 3
-193
—
389
nA
Pins with Analog 
Function Count = 0
—
ILKG_50_S1
5.0V input leakage 
current for Standard 
GPIO 3
-691
—
580
nA
Pins with Analog 
Function Count = 1
—
ILKG_50_S2
5.0V input leakage 
current for Standard 
GPIO 3
-947
—
673
nA
Pins with Analog 
Function Count = 2, 
plus PTA12, PTD1
—
Table continues on the next page...
NXP Semiconductors
I/O parameters
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
71 / 152


---
# 페이지 72

Table 25. GPIO DC electrical specifications, 5.0V (4.5V - 5.5V) (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
ILKG_50_S3
5.0V input leakage 
current for Standard 
GPIO 3
-1614
—
879
nA
Pins with Analog 
Function Count = 3, 
plus PTD0
—
ILKG_50_S_PTE13
5.0V input leakage 
current for Standard 
GPIO 3
-2335
—
619
nA
PMC VRC_CTRL pin
—
ILKG_50_SP0
5.0V input leakage 
current for Standard 
Plus GPIO and 
RESET IO 3
-553
—
736
nA
Pins with Analog 
Function Count = 0
—
ILKG_50_SP1
5.0V input leakage 
current for Standard 
Plus GPIO and 
RESET IO 3
-855
—
846
nA
Pins with Analog 
Function Count = 1
—
ILKG_50_SP2
5.0V input leakage 
current for Standard 
Plus GPIO and 
RESET IO 3
-1389
—
1017
nA
Pins with Analog 
Function Count = 2
—
ILKG_50_M0
5.0V input leakage 
current for Medium 
GPIO 3
-1036
—
951
nA
Pins with Analog 
Function Count = 0
—
ILKG_50_M1
5.0V input leakage 
current for Medium 
GPIO 3
-1284
—
1057
nA
Pins with Analog 
Function Count = 1, 
plus PTC16, PTD5
—
ILKG_50_M2
5.0V input leakage 
current for Medium 
GPIO 3
-1518
—
1298
nA
Pins PTD6 and PTE8
—
ILKG_50_F0
5.0V input leakage 
current for Fast 
GPIO 3
-1675
—
1497
nA
Pins with Analog 
Function Count = 0
—
ILKG_50_F1
5.0V input leakage 
current for Fast 
GPIO 3
-1805
—
1573
nA
Pins with Analog 
Function Count = 1
—
ILKG_50_I
5.0V input leakage 
current for GPI 3
-150
—
150
nA
—
—
VHYS_50
input hysteresis 
voltage 4
0.06 x 
VDD_HV
_A/B
—
—
mV
Always enabled, 
Applies to S32K34x, 
S32K3x8, S32K32x 
and S32K314
—
VHYS_50
input hysteresis 
voltage
0.06 x 
VDD_HV
_A/B
—
—
mV
Always enabled, 
Applies to S32K311, 
—
Table continues on the next page...
NXP Semiconductors
I/O parameters
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
72 / 152


---
# 페이지 73

Table 25. GPIO DC electrical specifications, 5.0V (4.5V - 5.5V) (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
S32K312 and S32K310 
devices.
CIN
GPIO Input 
capacitance
2
4
6
pF
add 2pF for package/
parasitic
—
IPU_50
5.0V GPIO pull up/
down resistance
20
—
55
kΩ
pull up @ 0.3 * VDD_
HV_*, pull down @ 0.7 
* VDD_HV_*
—
IOH_50_S
5.0V output 
high current 
Standard GPIO 5,6
1.6
—
—
mA
VOH >= VDD_HV_A/B 
- 0.7V
—
IOH_50_SP
5.0V output high 
current Standard 
Plus GPIO and 
RESET IO 5,6
2.5
—
—
mA
DSE = 0, VOH >= 
VDD_HV_A/B - 0.7V
—
IOH_50_M
5.0V output high 
current for Medium 
GPIO 5,6
4.0
—
—
mA
DSE = 0, VOH >= 
VDD_HV_A/B - 0.7V
—
IOH_50_F
5.0V output high 
current for Fast 
GPIO 5,6
6.0
—
—
mA
DSE = 0, VOH >= 
VDD_HV_A/B - 0.7V
—
IOH_50_SP
5.0V output high 
current for Standard 
Plus GPIO and 
RESET IO 5,6
5.0
—
—
mA
DSE = 1, VOH >= 
VDD_HV_A/B - 0.7V
—
IOH_50_M
5.0V output high 
current for Medium 
GPIO 5,6
8.0
—
—
mA
DSE = 1, VOH >= 
VDD_HV_A/B - 0.7V
—
IOH_50_F
5.0V GPIO output 
high current for Fast 
GPIO 5,6
12.0
—
—
mA
DSE = 1, VOH >= 
VDD_HV_A/B - 0.7V
—
IOL_50_S
5.0V output 
low current for 
Standard GPIO 5,6
1.6
—
—
mA
VOL <= 0.7V
—
IOL_50_SP
5.0V output low 
current for Standard 
Plus GPIO and 
RESET IO 5,6
2.5
—
—
mA
DSE =0, VOL <= 0.7V
—
IOL_50_M
5.0V output low 
current for Medium 
GPIO 5,6
4.0
—
—
mA
DSE =0, VOL <= 0.7V
—
Table continues on the next page...
NXP Semiconductors
I/O parameters
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
73 / 152


---
# 페이지 74

Table 25. GPIO DC electrical specifications, 5.0V (4.5V - 5.5V) (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
IOL_50_F
5.0V output low 
current for Fast 
GPIO 5,6
6.0
—
—
mA
DSE =0, VOL <= 0.7V
—
IOL_50_SP
5.0V output low 
current for Standard 
Plus GPIO and 
RESET IO 5,6
5.0
—
—
mA
DSE =1, VOL <= 0.7V
—
IOL_50_M
5.0V output low 
current for medium 
GPIO 5,6
8.0
—
—
mA
DSE =1, VOL <= 0.7V
—
IOL_50_F
5.0V output low 
current for Fast 
GPIO 5,6
12.0
—
—
mA
DSE =1, VOL <= 0.7V
—
FMAX_50_S
5.0V maximum 
frequency for 
Standard GPIO 5,7
—
—
10
MHz
3.6V - 5.5V CL (max) = 
25pF
—
FMAX_50_SP
5.0V maximum 
frequency for 
Standard Plus 
GPIO 5,7
—
—
25
MHz
3.6V - 5.5V CL (max) = 
25pF
—
FMAX_50_M
5.0V maximum 
frequency for 
Medium GPIO 5,7
—
—
25
MHz
3.6V - 5.5V CL (max) = 
25pF
—
FMAX_50_F
5.0V maximum 
frequency for Fast 
GPIO 5,7
—
—
25
MHz
3.6V - 5.5V CL (max) = 
25pF
—
IOHT
Output high current 
total for all ports 8
—
—
100
mA
—
—
1. Maximum length of RESET pulse will be filtered by an internal filter on this pin.
2. Minimum length of RESET pulse,  guaranteed not to be filtered by the internal filter.
3. A positive value is leakage flowing into pin with pin at VDD_HV_A/B (the GPIO supply level); a negative value is leakage 
flowing out the pin with the pin at ground.
4. Hysteresis spec does not apply to fast pad
5. GPIO output transition time information can be obtained from the device IBIS model. IBIS models are recommended for 
system level simulations, as discrete values for I/O transition times are not representative of the I/O pad behavior when 
connected to an actual transmission line load.
6. I/O output current specifications are valid for the given reference load figure, and the constraints given in the Operating 
Conditions of this document.
7. I/O timing specifications are valid for the un-terminated 50ohm transmission line reference load given in the figure below. 
A lumped 8pF load is assumed in addition to a 5 inch microstrip trace on standard FR4 with approximately 3.3pF/inch.. 
For best signal integrity, the series resistance in the transmission line should be matched closely to the selected output 
resistance (ROUT_*) of the I/O pad.
8. To determine total switching current on any I/O supply, current values per output pin should not be incrementally summed. 
I/O interfaces on the device are asynchronous to each other, so not all switching occurs at the same instant. Actual use 
case must be considered.
NXP Semiconductors
I/O parameters
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
74 / 152


---
# 페이지 75

RDSON
RPCB = RDSON
PCB
External
device
MCUsee note 1
RDSON
5 in.
(4 layer FR4)
CPCB = ~3.3 pF/inch  * 5 inch 
CL = 8 pF
1. See IBIS models for further details.
Notes:
Figure 34. Reference Load Diagram
7.3 5.0V (4.5V - 5.5V) GPIO Output AC Specification
Table 26. 5.0V (4.5V - 5.5V) GPIO Output AC Specification
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
TR_TF_50_S
5.0V Standard GPIO 
rise/fall time 1,2,3
5
—
21
ns
CL (max) = 25pF
—
TR_TF_50_S
5.0V Standard GPIO 
rise/fall time 1,2,3,4
8.5
—
31
ns
CL (max) = 50pF
—
TR_TF_50_SP
5.0V Standard 
Plus GPIO rise/fall 
time 1,2,3
3
—
13.2
ns
DSE=0 CL (max) = 
25pF
—
TR_TF_50_SP
5.0V Standard 
Plus GPIO rise/fall 
time 1,2,3
1
—
7.1
ns
DSE=1 CL (max) = 
25pF
—
TR_TF_50_SP
5.0V Standard 
Plus GPIO rise/fall 
time 1,2,3,4
6.4
—
18.8
ns
DSE=0 CL (max) = 
50pF
—
TR_TF_50_SP
5.0V Standard 
Plus GPIO rise/fall 
time 1,2,3,4
3.4
—
11
ns
DSE=1 CL (max) 
=50pF
—
TR_TF_50_M
5.0V Medium GPIO 
rise/fall time 1,2,3
1.8
—
8.2
ns
DSE=0, SRE=0 CL 
(max) = 25pF
—
TR_TF_50_M
5.0V Medium GPIO 
rise/fall time 1,2,3
2.5
—
9.8
ns
DSE=0, SRE=1 CL 
(max) = 25pF
—
TR_TF_50_M
5.0V Medium GPIO 
rise/fall time 1,2,3
0.7
—
4.5
ns
DSE=1, SRE=0 CL 
(max) = 25pF
—
TR_TF_50_M
5.0V Medium GPIO 
rise/fall time 1,2,3
1.8
—
7.2
ns
DSE=1, SRE=1 CL 
(max) = 25pF
—
TR_TF_50_M
5.0V Medium GPIO 
rise/fall time 1,2,3,4
3.95
—
13.2
ns
DSE=0, SRE=0 CL 
(max) = 50pF
—
Table continues on the next page...
NXP Semiconductors
I/O parameters
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
75 / 152


---
# 페이지 76

Table 26. 5.0V (4.5V - 5.5V) GPIO Output AC Specification (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
TR_TF_50_M
5.0V Medium GPIO 
rise/fall time 1,2,3,4
4.3
—
13.8
ns
DSE=0, SRE=1 CL 
(max) = 50pF
—
TR_TF_50_M
5.0V Medium GPIO 
rise/fall time 1,2,3,4
1.6
—
7.1
ns
DSE=1, SRE=0 CL 
(max) = 50pF
—
TR_TF_50_M
5.0V Medium GPIO 
rise/fall time 1,2,3,4
2.7
—
9.6
ns
DSE=1, SRE=1 CL 
(max) = 50pF
—
TR_TF_50_F
5.0V Fast GPIO rise/
fall time 1,2,3
0.4
—
3.15
ns
DSE=0, SRE=0 CL 
(max) = 25pF
—
TR_TF_50_F
5.0V Fast GPIO rise/
fall time 1,2,3
1.5
—
6.7
ns
DSE=0, SRE=1 CL 
(max) = 25pF
—
TR_TF_50_F
5.0V Fast GPIO rise/
fall time 1,2,3
0.3
—
2.02
ns
DSE=1, SRE=0 CL 
(max) = 25pF
—
TR_TF_50_F
5.0V Fast GPIO rise/
fall time 1,2,3
0.9
—
4.85
ns
DSE=1, SRE=1 CL 
(max) = 25pF
—
TR_TF_50_F
5.0V Fast GPIO rise/
fall time 1,2,3,4
1.0
—
5.8
ns
DSE=0, SRE=0 CL 
(max) = 50pF
—
TR_TF_50_F
5.0V Fast GPIO rise/
fall time 1,2,3,4
1.9
—
8.5
ns
DSE=0, SRE=1 CL 
(max) = 50pF
—
TR_TF_50_F
5.0V Fast GPIO rise/
fall time 1,2,3,4
0.9
—
3.0
ns
DSE=1, SRE=0 CL 
(max) = 50pF
—
TR_TF_50_F
5.0V Fast GPIO rise/
fall time 1,2,3,4
1.3
—
6.1
ns
DSE=1, SRE=1 CL 
(max) = 50pF
—
1. I/O timing specifications are valid for the un-terminated 50ohm transmission line reference load given in the figure below. 
A lumped 8pF load (typical) is assumed at the end of a 5 inch microstrip trace on standard FR4 with approximately 3.3pF/
inch. For best signal integrity, the series resistance in the transmission line should be matched closely to the selected 
output resistance (ROUT_*) of the I/O pad.
2. GPIO output transition time information can be obtained from the device IBIS model. IBIS models are recommended for 
system level simulations, as discrete values for I/O transition times are not representative of the I/O pad behavior when 
connected to an actual transmission line load.
3. GPIO rise/fall time specifications are derived from simulation model for the defined operating points (between 20% and 
80% of VDD_HV_A/B level). Actual application rise/fall time should be extracted from IBIS model simulations with the 
microcontroller models and application PCB.
4. Output timing valid for maximum external load C L = 50pF (includes PCB trace, package trace, and external device input 
load).
NXP Semiconductors
I/O parameters
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
76 / 152


---
# 페이지 77

RDSON
RPCB = RDSON
PCB
External
device
MCUsee note 1
RDSON
5 in.
(4 layer FR4)
CPCB = ~1.5 pF/inch  * 5 inch = ~7.5 pF
CL = 8 pF
1. See IBIS models for further details.
Notes:
Figure 35. Reference Load Diagram
7.4 3.3V (2.97V - 3.63V) GPIO Output AC Specification
Table 27. 3.3V (2.97V - 3.63V) GPIO Output AC Specification
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
TR_TF_33_S
3.3V Standard GPIO 
rise/fall time 1,2,3
5
—
28
ns
CL (max) = 25pF
—
TR_TF_33_S
3.3V Standard GPIO 
rise/fall time 1,2,3
9.5
—
43
ns
CL (max) = 50pF
—
TR_TF_33_SP
3.3V Standard 
Plus GPIO rise/fall 
time 1,2,3
4
—
17.5
ns
DSE=0 CL (max) = 
25pF
—
TR_TF_33_SP
3.3V Standard 
Plus GPIO rise/fall 
time 1,2,3
1.9
—
10
ns
DSE=1 CL (max) = 
25pF
—
TR_TF_33_SP
3.3V Standard 
Plus GPIO rise/fall 
time 1,2,3,4
7.5
—
27
ns
DSE=0 CL (max) = 
50pF
—
TR_TF_33_SP
3.3V Standard 
Plus GPIO rise/fall 
time 1,2,3,4
3.5
—
15
ns
DSE=1 CL (max) = 
50pF
—
TR_TF_33_M
3.3V Medium GPIO 
rise/fall time 1,2,3
2.2
—
12.3
ns
DSE=0, SRE=0 CL 
(max) = 25pF
—
TR_TF_33_M
3.3V Medium GPIO 
rise/fall time 1,2,3
3.0
—
14
ns
DSE=0, SRE=1 CL 
(max) = 25pF
—
TR_TF_33_M
3.3V Medium 
GPIO rise/fall 
time 1,2,3
0.8
—
6.6
ns
DSE=1, SRE=0 CL 
(max) = 25pF
—
TR_TF_33_M
3.3V Medium GPIO 
rise/fall time 1,2,3
2.4
—
10.5
ns
DSE=1, SRE=1 CL 
(max) = 25pF
—
TR_TF_33_M
3.3V Medium GPIO 
rise/fall time 1,2,3,4
4.5
—
17.3
ns
DSE=0, SRE=0 CL 
(max) = 50pF
—
Table continues on the next page...
NXP Semiconductors
I/O parameters
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
77 / 152


---
# 페이지 78

Table 27. 3.3V (2.97V - 3.63V) GPIO Output AC Specification (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
TR_TF_33_M
3.3V Medium GPIO 
rise/fall time 1,2,3,4
5
—
19.8
ns
DSE=0, SRE=1 CL 
(max) = 50pF
—
TR_TF_33_M
3.3V Medium GPIO 
rise/fall time 1,2,3,4
2.2
—
10
ns
DSE=1, SRE=0 CL 
(max) = 50pF
—
TR_TF_33_M
3.3V Medium GPIO 
rise/fall time 1,2,3,4
3.6
—
13.9
ns
DSE=1, SRE=1 CL 
(max) = 50pF
—
TR_TF_33_F
3.3V Fast GPIO rise/
fall time 1,2,3
0.5
—
4.9
ns
DSE=0, SRE=0 CL 
(max) = 25pF
—
TR_TF_33_F
3.3V Fast GPIO rise/
fall time 1,2,3
2.1
—
10
ns
DSE=0, SRE=1 CL 
(max) = 25pF
—
TR_TF_33_F
3.3V Fast GPIO rise/
fall time 1,2,3
0.4
—
2.2
ns
DSE=1, SRE=0 CL 
(max) = 25pF
—
TR_TF_33_F
3.3V Fast GPIO rise/
fall time 1,2,3
1.2
—
7.1
ns
DSE=1, SRE=1 CL 
(max) = 25pF
—
TR_TF_33_F
3.3V Fast GPIO rise/
fall time 1,2,3,4
1.1
—
8
ns
DSE=0, SRE=0 CL 
(max) = 50pF
—
TR_TF_33_F
3.3V Fast GPIO rise/
fall time 1,2,3,4
2.6
—
12.1
ns
DSE=0, SRE=1 CL 
(max) = 50pF
—
TR_TF_33_F
3.3V Fast GPIO rise/
fall time 1,2,3,4
0.8
—
4.2
ns
DSE=1, SRE=0 CL 
(max) = 50pF
—
TR_TF_33_F
3.3V Fast GPIO rise/
fall time 1,2,3,4
1.5
—
8.6
ns
DSE=1, SRE=1 CL 
(max) = 50pF
—
1. I/O timing specifications are valid for the un-terminated 50ohm transmission line reference load given in the figure below. 
A lumped 8pF load (typical) is assumed at the end of a 5 inch microstrip trace on standard FR4 with approximately 3.3pF/
inch. For signals with frequency greater than 63MHz, a maximum 2 inch PCB trace is assumed. For best signal integrity, 
the series resistance in the transmission line should be matched closely to the selected output resistance (ROUT_*) of the 
I/O pad.
2. GPIO rise/fall time specifications are derived from simulation model for the defined operating points (between 20% and 
80% of VDD_HV_A/B level). Actual application rise/fall time should be extracted from IBIS model simulations with the 
microcontroller models and application PCB.
3. GPIO output transition time information can be obtained from the device IBIS model. IBIS models are recommended for 
system level simulations, as discrete values for I/O transition times are not representative of the I/O pad behavior when 
connected to an actual transmission line load.
4. Output timing valid for maximum external load C L = 50pF (includes PCB trace, package trace, and external device input 
load).
NXP Semiconductors
I/O parameters
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
78 / 152


---
# 페이지 79

RDSON
RPCB = RDSON
PCB
External
device
MCUsee note 1
RDSON
5 in.
(4 layer FR4)
CPCB = ~3.3 pF/inch  * 5 inch 
CL = 8 pF
1. See IBIS models for further details.
Notes:
Figure 36. Reference Load Diagram
8 Glitch Filter
The glitch filter parameters in the following table apply to the filters of WKPU pins and TRGMUX inputs 60-63.
Table 28. Glitch Filter
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
TFILT
Glitch filter max 
filtered pulse 
width 1,2,3
—
—
20
ns
—
—
TUNFILT
Glitch filter min 
unfiltered pulse 
width 2,3,4
400
—
—
ns
—
—
1. Pulses shorter than defined by the maximum value are guaranteed to be filtered (not passed).
2. An input signal pulse is defined by the duration between the input signal's crossing of a Vil/Vih threshold voltage level, and 
the next crossing of the opposite level.
3. Pulses in between the max filtered and min unfiltered may or may not be passed through.
4. Pulses larger than defined by the minimum value are guaranteed to not be filtered (passed).
9 Flash memory specification
9.1 Flash memory program and erase specifications
Table 29. Flash memory program and erase specifications
Symbol
Characteristic1
Typ2
Factory 
Programming3,4
Field Update
Unit
Initial Max
Initial Max, 
Full Temp
Typical 
End of 
Life5
Lifetime Max6
20°C ≤TA 
≤30°C
-40°C ≤TJ 
≤150°C
-40°C ≤TJ 
≤150°C
≤ 1,000 
cycles
≤ 100,000 
cycles
tdwpgm
Doubleword (64 bits) program time
102
122
129
111
150
µs
Table continues on the next page...
NXP Semiconductors
Glitch Filter
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
79 / 152


---
# 페이지 80

Table 29. Flash memory program and erase specifications (continued)
Symbol
Characteristic1
Typ2
Factory 
Programming3,4
Field Update
Unit
Initial Max
Initial Max, 
Full Temp
Typical 
End of 
Life5
Lifetime Max6
20°C ≤TA 
≤30°C
-40°C ≤TJ 
≤150°C
-40°C ≤TJ 
≤150°C
≤ 1,000 
cycles
≤ 100,000 
cycles
tppgm
Page (256 bits) program time
142
171
180
157
200
µs
tqppgm
Quad-page (1024 bits) 
program time
314
377
396
341
450
µs
t8kpgm
8 KB Sector program time
20
24
26
22
30
ms
t8kers
8 KB Sector erase time
4.8
8.5
10.6
6.5
30
ms
t256kbers
256KB Block erase time
22.8
27.4
28.8
24.4
40
—
ms
t512kbers
512KB Block erase time
25.4
30.5
32.1
27.9
45
—
ms
t1mbers
1MB Block erase time
30.6
36.8
38.7
33.6
50
—
ms
t2mbers
2MB Block erase time
41.1
49.3
51.8
45.2
60
—
ms
1. Program times are actual hardware programming times and do not include software overhead. Sector program times 
assume quad-page programming.
2. Typical program and erase times represent the median performance and assume nominal supply values and operation at 
25 °C. Typical program and erase times may be used for throughput calculations.
3. Conditions: ≤ 25 cycles, nominal voltage.
4. Plant Programing times provide guidance for timeout limits used in the factory.
5. Typical End of Life program and erase times represent the median performance and assume nominal supply values. 
Typical End of Life program and erase values may be used for throughput calculations.
6. Conditions: -40°C ≤TJ ≤150°C, full spec voltage.
9.2 Flash memory Array Integrity and Margin Read specifications
Table 30. Flash memory Array Integrity and Margin Read specifications
Symbol
Characteristic
Min
Typical
Max1 2
Units3
tai256kseq
Array Integrity time and Margin 
Read time for sequential sequence 
on 256KB block.
—
—
8192 x Tperiod x Nread
(plus 40uS adder required if User 
Margin Read)
—
tai512kseq
Array Integrity time and Margin 
Read time for sequential sequence 
on 512KB block.
—
—
16384 x Tperiod x Nread
(plus 40uS adder required if User 
Margin Read)
—
Table continues on the next page...
NXP Semiconductors
Flash memory specification
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
80 / 152


---
# 페이지 81

Table 30. Flash memory Array Integrity and Margin Read specifications (continued)
Symbol
Characteristic
Min
Typical
Max1 2
Units3
tai1mseq
Array Integrity time and Margin 
Read time for sequential sequence 
on 1MB block.
—
—
32768 x Tperiod x Nread
(plus 40uS adder required if User 
Margin Read)
—
tai2mseq
Array Integrity time and Margin 
Read time for sequential sequence 
on 2MB block.
—
—
65536 x Tperiod x Nread
(plus 40uS adder required if User 
Margin Read)
—
tai256kprop
Array Integrity time for proprietary 
sequence on 256KB block.
—
—
106496
x Tperiod x Nread
—
tai512kprop
Array Integrity time for proprietary 
sequence on 512KB block.
—
—
229376
x Tperiod x Nread
—
tai1mprop
Array Integrity time for proprietary 
sequence on 1MB block.
—
—
491520
x Tperiod x Nread
—
tai2mprop
Array Integrity time for proprietary 
sequence on 2MB block.
—
—
1048576
x Tperiod x Nread
—
1. Array Integrity times need to be calculated and is dependent on system frequency and number of clocks per read. The 
equation presented require Tperiod (which is the unit accurate period, thus for 200 MHz, Tperiod would equal 5e-9) and 
Nread (which is the number of clocks required for read, including single read, dual read, quad read contribution. Thus for a 
read setup that requires 6 clocks to read Nread would equal 6.
2. Array Integrity times are actual hardware execution times and do not include software overhead or system code execution 
overhead.
3. The units for Array Integrity are determined by the period of the system clock. If unit accurate period is used in the 
equation, the results of the equation are also unit accurate.
9.3 Flash memory module life specifications
Table 31. Flash memory module life specifications
Symbol
Characteristic
Conditions
Min
Typical
Units
Array P/E 
cycles
Number of program/erase cycles per block 
for 256 KB and 512 KB blocks using 
Sector Erase.
—
100,000
—
P/E 
cycles
Number of program/erase cycles per block for 
1 MB and 2 MB blocks using Sector Erase.
—
1,000
—
P/E 
cycles
Number of program/erase cycles per block 
using Block Erase1
—
25
—
P/E 
cycles
Data 
retention
Minimum data retention.
Blocks with 0 - 1,000 
P/E cycles.
20
—
Years
Blocks with 100,000 
P/E cycles.
10
—
Years
NXP Semiconductors
Flash memory specification
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
81 / 152


---
# 페이지 82

1. Program and erase supported for factory conditions. Nominal supply values and operation at 25°C.
9.3.1 Data retention vs program/erase cycles
Graphically, Data Retention versus Program/Erase Cycles can be represented by the following figure.
The spec window represents qualified limits.
0
P/E Cycles (Sector Erases)
Minimum Data Retention Life (Years)
5
1
10
15
20
25
10
100
1000
10000
100000
1000000
Figure 37. Data retention vs program/erase cycles
9.4 Flash memory AC timing specifications
Table 32. Flash memory AC timing specifications
Symbol
Characteristic
Min
Typical
Max
Units
tdone
Time from 0 to 1 transition on the MCR[EHV] bit 
initiating a program/erase until the MCR[DONE] 
bit is cleared.
—
—
5
ns
tdones
Time from 1 to 0 transition on the MCR[EHV] bit 
aborting a program/erase until the MCR[DONE] 
bit is set to a 1.
5 plus four 
system clock 
periods
—
22 plus four 
system clock 
periods1
µs
tdrcv
Time to recover once exiting low power mode.
14 plus seven 
system clock 
periods2
17.5 plus 
seven system 
clock periods
21 plus seven 
system clock 
periods
µs
taistart
Time from 0 to 1 transition of UT0[AIE] initiating a 
Margin Read or Array Integrity until the UT0[AID] 
bit is cleared. This time also applies to the 
resuming from a suspend or breakpoint by 
clearing UT0[AISUS] or clearing UT0[NAIBP]
—
—
5
ns
taistop
Time from 1 to 0 transition of UT0[AIE] initiating 
an Array Integrity abort until the UT0[AID] bit is 
set. This time also applies to the UT0[AISUS] to 
—
—
50
system clock 
periods
ns
Table continues on the next page...
NXP Semiconductors
Flash memory specification
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
82 / 152


---
# 페이지 83

Table 32. Flash memory AC timing specifications (continued)
Symbol
Characteristic
Min
Typical
Max
Units
UT0[AID] setting in the event of a Array Integrity 
suspend request.
tmrstop
Time from 1 to 0 transition of UT0[AIE] initiating 
a Margin Read abort until the UT0[AID] bit is 
set. This time also applies to the UT0[AISUS] to 
UT0[AID] setting in the event of a Margin Read 
suspend request.
—
—
26
plus fifteen 
system clock 
periods
µs
1. For Block Erase, Tdones times may be 3x max spec.
2. In extreme cases (1 block configurations) Tdrcv min may be faster (12uS plus seven system clocks)
9.5 Flash memory read timing parameters
Table 33. Flash Read Wait State Settings (S32K344, S32K324, S32K314, S32K342, S32K322, S32K341, S32K312, 
S32K311, S2K310 and S32K389(PFC1))
Flash Frequency
RWSC setting
250 KHz < Freq ≤ 66 MHz
1
66 MHz < Freq ≤ 100 MHz
2
100 MHz < Freq ≤ 133 MHz
3
133 MHz < Freq ≤ 167 MHz
4
167 MHz < Freq ≤ 200 MHz
5
200 MHz < Freq ≤ 233 MHz
6
233 MHz < Freq ≤ 250 MHz
7
Table 34. Flash Read Wait State Settings (S32K358, S32K348, S32K338, S32K328, S32K388 and S32K389(PFC0))
Flash Frequency
RWSC setting
250 KHz < Freq ≤ 60 MHz
1
60 MHz < Freq ≤ 90 MHz
2
90 MHz < Freq ≤ 120 MHz
3
120 MHz < Freq ≤ 150 MHz
4
150 MHz < Freq ≤ 180 MHz
5
180 MHz < Freq ≤ 210 MHz
6
210 MHz < Freq ≤ 240 MHz
7
240 MHz < Freq ≤ 250 MHz
8
NXP Semiconductors
Flash memory specification
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
83 / 152


---
# 페이지 84

10 Analog modules
10.1 SAR_ADC
All below specs are applicable only when one ADC instance is in operation and averaging is used or multiple ADC instances are 
operational at the same time but sampling different channels. Best performance can be achieved if only one ADC is operational 
at a time sampling one channel
Table 35. SAR_ADC
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
VDD_HV_A
ADC Supply 
Voltage 1
2.97
—
5.5
V
—
—
DVREFL
VSS / VREFL 
Voltage Difference 2
-100
—
100
mV
—
—
VAD_INPUT
ADC Input Voltage 3
VREFL
—
VREFH
V
—
—
fAD_CK
ADC Clock 
Frequency 
(S32K344, 
S32K324, S32K314, 
S32K342, S32K341, 
S32K322)
10
—
80
MHz
—
—
fAD_CK
ADC Clock 
Frequency 
(S32K312, 
S32K311, S32K310, 
S32K358, S32K348, 
S32K338, S32K328, 
S32K388, S32K389)
10
—
120
MHz
—
—
tSAMPLE
ADC Input Sampling 
Time
275
—
—
ns
—
—
tCONV
ADC Total 
Conversion Time
1
—
—
us
12-bit result
—
tCONV
ADC Total 
Conversion Time
0.9
—
—
us
10-bit result
—
CAD_INPUT
ADC Input 
Capacitance
—
—
13.8
pF
ADC component 
plus pad capacitance 
(~2pF)
—
RAD_INPUT
ADC Input 
Resistance
—
—
4.6
KΩ
ADC + mux+SOC 
routing
—
RS
Source Impedance, 
precision channels
—
20
—
Ω
—
—
RS
Source Impedance, 
standard channels
—
20
—
Ω
—
—
Table continues on the next page...
NXP Semiconductors
Analog modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
84 / 152


---
# 페이지 85

Table 35. SAR_ADC (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
TUE
ADC Total 
Unadjusted Error 4,5
—
+/-4
+/-6
LSB
without adjacent pin 
current injection
—
TUE
ADC Total 
Unadjusted Error 5
—
+/-4
+/-8
LSB
with up to +/-3mA 
of current injection on 
adjacent pins
—
IAD_REF
Current 
Consumption on 
ADC Reference pin, 
VREFH.
—
—
200
uA
Per ADC for dedicated 
or shared reference 
pins
—
IDDA
Current 
Consumption on 
ADC Supply, 
VDD_HV_A
—
2.1
—
mA
Current consumption 
per ADC module, ADC 
enabled and converting
—
CS
Sampling 
Capacitance
6.4 
(gain=0) 
9.72 
pF(gain=
max)
7.36 
(gain=0) 
11.12 
pF(gain=
max)
8.32 
(gain=0) 
12.52 
(gain=ma
x)
pF
all channels
—
RAD
Sampling Switch 
Impedance
80
170
520
Ohm
all channels
—
CP1
Pin capacitance
1.42
—
5.30
pF
all channels
—
CP1
Pin capacitance
1.42
—
4.38
pF
Precision channels
—
CP1
Pin capacitance
1.61
—
5.30
pF
Standard channels
—
CP2
Analog Bus 
Capacitance
0.32
—
4.18
pF
all channels
—
CP2
Analog Bus 
Capacitance
0.32
—
1.42
pF
Precision channels
—
CP2
Analog Bus 
Capacitance
0.497
—
4.18
pF
Standard channels
—
RSW1
Channel selection 
Switch impedance
65.9
—
1410
Ohm
all channels
—
RSW1
Channel selection 
Switch impedance
65.9
—
712
Ohm
Precision channels
—
RSW1
Channel selection 
Switch impedance
65.9
—
1410
Ohm
Standard channels
—
1. Appropriate decoupling capacitors to be used to filter noise on the supplies. See application note AN5032 for reference supply design for 
SAR_ADC.
2. VSS and VREFL should be shorted on PCB. 100mV difference between VSS and VREFL is for transient only (not for DC).
3. This is ADC Input range for ADC accuracy guaranteed in this input range only. For SoC Pin capability, see Operation Condition Section.  
4. Spec valid if potential difference between VDD_HV_A and VREFH should follow VDD_HV_A +0.1V >=VREFH >= VDD_HV_A -1.5V
5. TUE spec for precision and standard channels is based on 12-bit level resolution.
NXP Semiconductors
Analog modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
85 / 152


---
# 페이지 86

VA
Source
Filter
Current Limiter
EXTERNAL CIRCUIT
RS
Source Impedance
RF
Filter Resistance
CF
Filter Capacitance
RL
Current Limiter Resistance
RSW1 Channel Selection Switch Impedance
RAD
Sampling Switch Impedance
CP
Pin Capacitance (two contributions: CP1, CP2)
CS
Sampling Capacitance
INTERNAL CIRCUIT SCHEME
CF
CP1
CP2
CS
RS
RF
RL
RSW1
VDD_HV_A
RAD
Channel
Selection
Sampling
Figure 38. SAR_ADC Input Circuit
10.2 Supply Diagnosis
The table below gives the specification for the on die supply diagnosis.
Table 36. Supply Diagnosis
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
AN_ACC
Offset to internally 
monitored supply at 
ADC input 1,2,3
-5
0
5
%
—
—
AN_T_on
Switching time from 
closed (OFF) to 
conducting (ON) 1
—
2.5
12
ns
—
—
AN_TADCSA
Required ADC 
sampling time 2
1.2
—
—
µs
—
—
1. These specs will have degraded performance when used in extended supply voltage operation range, i.e. normal supply 
voltage range specification is exceeded.
2. Required ADC sampling time specified by parameter AN_TADCSA needs to be used at the ADC conversion to guarantee 
the specified accuracy. A smaller sampling time leads to a less accurate result.
3. If V15 > VDD_HV_A +100mV then the V15 measurement via anamux may be imprecise.
10.3 Low Power Comparator (LPCMP)
Table 37. Low Power Comparator (LPCMP)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
idda(IDHSS)
vdda Supply 
Current, High Speed 
Mode 1,2
—
240
—
uA
—
—
Table continues on the next page...
NXP Semiconductors
Analog modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
86 / 152


---
# 페이지 87

Table 37. Low Power Comparator (LPCMP) (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
idda(IDLSS)
vdda Supply 
Current, Low Speed 
Mode 1,2
—
17
—
uA
—
—
idda(IDHSS)
vdda Supply 
Current, high speed 
mode, DAC only 2
—
10
—
uA
—
—
idda_lkg
vdda Supply 
Current, module 
disabled 2
—
2
—
nA
vdda=5.5V, T=25C
—
TDHSB
Propagation Delay, 
High Speed Mode 3
—
—
200
ns
—
—
TDLSB
Propagation Delay, 
Low Speed mode 3
—
—
2
us
—
—
TDHSS
Propagation Delay, 
High Speed Mode 4
—
—
400
ns
—
—
TDLSS
Propagation Delay, 
Low Speed mode 4
—
—
5
us
—
—
TIDHS
Initialization Delay, 
High Speed Mode 5
—
—
3
us
—
—
TIDLS
Initialization Delay, 
Low Speed mode 5
—
—
30
us
—
—
VAIO
Analog Input Offset 
Voltage, High Speed 
Mode
-25
+/-1
25
mV
—
—
VAIO
Analog Input Offset 
Voltage, Low Speed 
mode
-40
+ /- 5
40
mV
—
—
VAHYST0
Analog Comparator 
Hysteresis, High 
Speed Mode
—
0
—
mV
HYSTCTR[1:0]= 2'b00
—
VAHYST1
Analog Comparator 
Hysteresis, High 
Speed Mode
—
14
41
mV
HYSTCTR[1:0]= 2'b01
—
VAHYST2
Analog Comparator 
Hysteresis, High 
Speed Mode
—
27
76
mV
HYSTCTR[1:0]= 2'b10
—
VAHYST3
Analog Comparator 
Hysteresis, High 
Speed Mode
—
40
111
mV
HYSTCTR[1:0]= 2'b11
—
Table continues on the next page...
NXP Semiconductors
Analog modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
87 / 152


---
# 페이지 88

Table 37. Low Power Comparator (LPCMP) (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
VAHYST0
Analog Comparator 
Hysteresis, Low 
Speed mode
—
0
—
mV
HYSTCTR[1:0]= 2'b00
—
VAHYST1
Analog Comparator 
Hysteresis, Low 
Speed mode
—
8
60
mV
HYSTCTR[1:0]= 2'b01
—
VAHYST2
Analog Comparator 
Hysteresis, Low 
Speed mode
—
15
113
mV
HYSTCTR[1:0]= 2'b10
—
VAHYST3
Analog Comparator 
Hysteresis, Low 
Speed mode
—
23
165
mV
HYSTCTR[1:0]= 2'b11
—
INL
DAC integral 
linearity 2,6,7
-1
—
1
LSB
vrefh_cmp = vdda, 
vrefl_cmp = vss
—
INL
DAC integral 
linearity 2,6,7
-1.5
—
1.5
LSB
vrefh_cmp < vdda
—
DNL
DAC differential 
linearity 2,6
-1
—
1
LSB
vrefh_cmp = vdda, 
vrefl_cmp = vss
—
DNL
DAC differential 
linearity 2,6
-1.5
—
1.5
LSB
vrefh_cmp < vdda
—
tDDAC
DAC 
Initialization time
—
—
30
us
—
—
VAIN
Analog input voltage
0
—
VDDA
V
—
—
1. Difference at input > 200mV
2. vdda is comparator HV supply and internally shorted to VDD_HV_A pin. vss is comparator  ground
3. Applied +/- (100 mV + VAHYST0/1/2/3 + max. of VAIO) around switch point
4. Applied +/- (30 mV + VAHYST0/1/2/3 + max. of VAIO) around switch point
5. Applied ± (100 mV + VAHYST0/1/2/3 ).
6. 1 LSB = (vrefh_cmp - vrefl_cmp) /256. vrefh_cmp and vrefl_cmp are comparator reference high and low
7. Calculation method used: Linear Regression Least Square Method
For Comparator IN signals adjacent to VDD_HV_A/VDD_HV_B/VSS or XTAL/EXTAL or switching pins cross coupling may 
happen and hence hysteresis settings can be used to obtain the desired Comparator performance. Additionally an external 
capacitor to ground (1nF) should be used to filter noise on input signal. Also source drive should not be weak (Signal with <50K 
pull up/down is recommended). 
For devices where the VDD_HV_B domain is present, LPCMP0 channels must only be selected/enabled when VDD_HV_A >= 
VDD_HV_B. These channels must be disabled when VDD_HV_A goes below VDD_HV_B.
NXP Semiconductors
Analog modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
88 / 152


---
# 페이지 89

0
3.3
3.0
1.5
2.1
0.6
30
60
Hysteresis
(mV)
0
VAIN (V)
Junction Temp (°C)
VDD_HV_A (V)
HYSTCTR setting
0.3
1.2
2.4
2.7
0.9
1.8
3.3
25
90
00
01
10
11
Figure 39. Typical Hysteresis vs VAIN (VDD_HV_A = 3.3 V, High Speed Mode)
0
3.3
3.0
1.5
2.1
0.6
20
40
60
Hysteresis
(mV)
0
HYSTCTR setting
0.3
1.2
2.4
2.7
0.9
1.8
3.3
25
00
VAIN (V)
Junction Temp (°C)
VDD_HV_A (V)
01
10
11
Figure 40. Typical Hysteresis vs VAIN (VDD_HV_A = 3.3 V, Low Speed Mode)
0
3.0
4.0
30
60
Hysteresis
(mV)
0
VAIN (V)
Junction Temp (°C)
VDD_HV_A (V)
HYSTCTR setting
0.5
2.5
4.5
5.0
1.0
3.5
5
25
90
1.5
2.0
00
01
10
11
Figure 41. Typical Hysteresis vs VAIN (VDD_HV_A = 5 V, High Speed Mode).png
NXP Semiconductors
Analog modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
89 / 152


---
# 페이지 90

0
3.0
4.0
VAIN (V)
Junction Temp (°C)
VDD_HV_A (V)
HYSTCTR setting
0.5
2.5
4.5
5.0
1.0
3.5
5
25
1.5
2.0
00
01
10
11
20
40
60
Hysteresis
(mV)
0
Figure 42. Typical Hysteresis vs VAIN (VDD_HV_A = 5 V, Low Speed Mode).png
10.4 Temperature Sensor
The table below gives the specification for the MCU on-die temperature sensor.
Table 38. Temperature Sensor
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
TS_TJ
Junction 
temperature 
monitoring range
-40
—
150
°C
—
—
TS_IV25
ON state current 
consumption on V25
—
400
—
µA
ETS_EN=1
—
TS_ACC1
Temperature output 
error at circuit output 
(Voltage) 1,2,3
-5
0
+5
°C
100 °C < Tj <= 150 °C
—
TS_ACC2
Temperature output 
error at circuit output 
(Voltage) 1,2,3
-10
0
+10
°C
-40 °C <= Tj <=100 °C
—
TS_TSTART
Circuit start up time
—
4
30
µs
—
—
TS_TADCSA
Required ADC 
sampling time 1
1.2
—
—
µs
—
—
1. Required ADC sampling time specified by parameter TS_TADCSA needs to be used at the ADC conversion to guarantee 
the specified accuracy. A smaller sampling time leads to a less accurate result.
2. Note: The temperature sensor measures the junction temperature Tj at the location where it is placed on die. The local Tj 
is modulated by current and previous active state of the circuit elements on die.
3. The error caused by ADC conversion and provided temperature calculation formula is not included. 
NXP Semiconductors
Analog modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
90 / 152


---
# 페이지 91

11 Clocking modules
11.1 FIRC
Table 39. FIRC
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
fFIRC
FIRC nominal 
Frequency
—
48
—
MHz
—
—
FACC
FIRC Frequency 
deviation across 
process, voltage, 
and temperature 
after trimming
-5
—
5
%
—
—
TSTART
Startup Time 1
—
10
25
us
—
—
1. Startup time is for reference only.
11.2 SIRC
Table 40. SIRC
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
fSIRC
SIRC nominal 
Frequency
—
32
—
KHz
—
—
fSIRC_ACC
SIRC Frequency 
deviation across 
process, voltage, 
and temperature 
after trimming
-10
—
10
%
—
—
TSIRC_start
SIRC Startup Time 1
—
—
3
ms
—
—
TSIRC_DC
SIRC duty cycle
30
—
70
%
—
—
1. Startup time is for information only.
11.3 PLL
FPLL_DS, FPLL_FM and all fractional mode jitter specifications are not applicable to Auxiliary PLL on S32K328, S32K338, 
S32K348, S32K358, S32K388 and S32K389 devices.
Jitter values specified in this table are applicable for FXOSC reference clock input only.
Table 41. PLL
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
FPLL_in
PLL input frequency
8
—
40
MHz
This is the frequency 
after the Reference 
Divider within the PLL
—
Table continues on the next page...
NXP Semiconductors
Clocking modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
91 / 152


---
# 페이지 92

Table 41. PLL (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
FPLL_out
PLL output 
frequency 
(PLL_PHIn_CLK)
25
—
480
MHz
—
—
FPLL_vcoRange
VCO Frequency 
range
640
—
1280
MHz
—
—
FPLL_DS
Modulation Depth 
(down spread)
-0.5
—
-3
%
—
—
FPLL_FM
Modulation 
frequency
—
—
32
KHz
—
—
TPLL_start
PLL lock time
—
—
1
ms
—
—
JPLL_cyc
PLL period jitter (pk-
pk) 1,2,3
—
—
237
ps
FPLL_out = 240MHz, 
Integer Mode
—
JPLL_cyc
PLL period jitter (pk-
pk) 1,2,3
—
—
487
ps
FPLL_out = 240MHz, 
Fractional Mode
—
JPLL_acc
PLL accumulated 
jitter (pk-pk) 1,2,3
—
—
840
ps
FPLL_out = 240MHz, 
Integer Mode
—
JPLL_acc
PLL accumulated 
jitter (pk-pk) 1,2,3
—
—
1680
ps
FPLL_out = 240MHz, 
Fractional Mode
—
JPLL_cyc
PLL period jitter (pk-
pk) 1,2,3
—
—
295
ps
FPLL_out = 160MHz, 
Integer Mode
—
JPLL_cyc
PLL period jitter (pk-
pk) 1,2,3
—
—
670
ps
FPLL_out = 160MHz, 
Fractional Mode
—
JPLL_acc
PLL accumulated 
jitter (pk-pk) 1,2,3
—
—
840
ps
FPLL_out = 160MHz, 
Integer Mode
—
JPLL_acc
PLL accumulated 
jitter (pk-pk) 1,2,3
—
—
1680
ps
FPLL_out = 160MHz, 
Fractional Mode
—
JPLL_cyc
PLL period jitter (pk-
pk) 1,2,3
—
—
353
ps
FPLL_out = 120MHz, 
Integer Mode
—
JPLL_cyc
PLL period jitter (pk-
pk) 1,2,3
—
—
853
ps
FPLL_out = 120MHz, 
Fractional Mode
—
JPLL_acc
PLL accumulated 
jitter (pk-pk) 1,2,3
—
—
840
ps
FPLL_out = 120MHz, 
Integer Mode
—
JPLL_acc
PLL accumulated 
jitter (pk-pk) 1,2,3
—
—
1680
ps
FPLL_out = 120MHz, 
Fractional Mode
—
1. For SSCG, jitter due to systematic modulation needs to be added as per applied modulation. Accumulated jitter 
specification is not valid with SSCG
2. Jitter numbers calculated by extrapolating RMS jitter numbers to +/- 7 sigma .
3. Jitter numbers are valid only at IP boundary and does not include any degradation due to IO pad for clock measurement.
NXP Semiconductors
Clocking modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
92 / 152


---
# 페이지 93

11.4 FXOSC
Table 42. FXOSC
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
FREQ_BYPASS
Input clock 
frequency in bypass 
mode 1
—
—
50
MHz
—
—
TRF_BYPASS
Input clock rise/fall 
time in bypass 
mode 1
—
—
5
ns
—
—
CLKIN_DUTY_
BYPASS
Input clock duty 
cycle in bypass 
mode 1
47.5
—
52.5
%
—
—
FXOSC_CLK
output clock 
frequency in crystal 
mode
8
—
40
MHz
—
—
TFXOSC
Fxosc start up 
time (ALC enabled) 2
—
—
2
ms
—
—
IFXOSC
Oscillator Analog 
circuit supply 
current, V25 supply 
(ALC enable)
—
—
1
mA
using 8, 16 or 40 MHz 
crystal
—
IFXOSC
Oscillator Analog 
circuit supply 
current, V25 supply 
(ALC disabled)
—
—
2.7
mA
using 8, 16 or 40 MHz 
crystal
—
EXTAL_SWING_
PP
Peak-to-peak 
voltage swing on 
EXTAL pin in crystal 
oscillator mode (ALC 
enabled)
0.3
—
1.4
V
—
—
EXTAL_SWING_
PP
Peak-to-peak 
voltage swing on 
EXTAL pin in crystal 
oscillator mode (ALC 
disabled) 3
1.2
—
2.75
V
—
—
CLKIN_VIL_
EXTAL_BYPASS
Input clock low level 
in bypass mode 4
0
—
vref-1
V
vref=0.5*VDD_HV_A
—
CLKIN_VIH_
EXTAL_BYPASS
Input clock high level 
in bypass mode 4
vref+1
—
VDD_HV
_A
V
vref=0.5*VDD_HV_A
—
VSB
Self Bias Voltage
350
—
850
mV
—
—
GM
Amplifier 
Transconductance
9.7
—
18.5
mA/V
GM_SEL[3:0] = 
4`b1111
—
1. For bypass mode applications, the EXTAL pin should be driven low when FXOSC is in off/disabled state.
2. The startup time specification is valid only when the recommended crystal and load capacitors are used. For higher load 
capacitances, the actual startup time might be higher.
NXP Semiconductors
Clocking modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
93 / 152


---
# 페이지 94

3. The recommended gm setting to ensure extal swing < 2.75V at 8MHz in ALC-disabled mode is gm=4'b0010. 
Recommended gm settings in ALC-disabled mode for all other supported frequencies and crystals remain the same.
4. For bypass mode applications, the EXTAL pin should be driven symmetrical around Vref =0.5* VDD_HV_A
To ensure stable oscillations, FXOSC incorporates the feedback resistance internally.
In single ended bypass mode, the XTAL pin can be left unconnected.
Drive level is a crystal specification and if crystal load capacitance is increased beyond the recommended value, it may violate 
the crystal drive level rating. In such cases, contact NXP sales representative for selecting the correct crystal.
Crystal oscillator circuit provides stable oscillations when gmXOSC > 5 * gm_crit. The gm_crit is defined as:
gm_crit = 4 * (ESR + RS) * (2πF)2 * (C0 + CL)2
where:
• gmXOSC is the transconductance of the internal oscillator circuit
• ESR is the equivalent series resistance of the external crystal
• RS is the series resistance connected between XTAL pin and external crystal for current limitation
• F is the external crystal oscillation frequency
• C0 is the shunt capacitance of the external crystal
• CL is the external crystal total load capacitance. CL = Cs+ [C1*C2/(C1+C2)]
• Cs is stray or parasitic capacitance on the pin due to any PCB traces
• C1, C2 external load capacitances on EXTAL and XTAL pins
See manufacture datasheet for external crystal component values
Figure 43. Oscillation build-up equation
 
To improve the FXOSC & PLL jitter performance in S32K328, S32K338, S32K348, S32K358 the functionality of 
the pins (namely - PTG0,PTG3,PTF11,PTF19,PTF30, PMOS_CTRL in BGA289 package) cannot be 
toggling edge aligned.
  NOTE  
 
To improve the FXOSC jitter & duty cycle performance in S32K310, S32K311, S32K312, S32K322, S32K341 
S32K342, S32K314,S32K324 and S32K344, the functionality of the pin next to the Oscillator (namely, PTE14 in 
172-HDQFP and PTE3 in 100-HDQFP package) must be limited to static GPIO operation.
  NOTE  
 
To improve the FXOSC & PLL jitter performance in S32K388, the functionality of the pins (namely - PTG0, PTG2, 
PTG3, PTF30, PTE12, PTA29, PMOS_CTRL in BGA289 package) cannot be toggling edge-aligned.
  NOTE  
NXP Semiconductors
Clocking modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
94 / 152


---
# 페이지 95

Figure 44. Block diagram
11.5 SXOSC
Table 43. SXOSC
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
Fsxosc
Oscillator Crystal 
Frequency 1
—
32.768
—
KHz
IP in crystal mode
—
Tstart
SXOSC startup time
—
—
2
s
start up time is 
dependent upon board 
and crystal model.
—
ISXOSC
Oscillator Analog 
circuit supply current
—
2.1
10
uA
—
—
gm_sxocs
NMOS Amplifier 
Transconductance
3
—
40
u A/V
—
—
1. Supports single frequency
NXP Semiconductors
Clocking modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
95 / 152


---
# 페이지 96

12 Communication interfaces
12.1 LPSPI
The Low Power Serial Peripheral Interface (LPSPI) provides a synchronous serial bus with master and slave operations. Many 
of the transfer attributes are programmable. The following table provides timing characteristics for classic LPSPI timing modes.
1. All timing is shown with respect to 50% VDD_HV_A/B  thresholds.
2. All measurements are with maximum output load of 30pF (except 50pF support on K3x8 and S32K389 with Fast/Medium/
Standard-Plus IOs), input transition of 1 ns and pad configured  DSE = 1, SRC = 0.
See I/O parameters for GPIO electrical specifications.
Table 44. LPSPI
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
fperiph
Peripheral Frequenc
y 1,2,3
—
—
40
MHz
Master
—
fperiph
Peripheral Frequenc
y 1,2,3
—
—
40
MHz
Slave
—
fperiph
Peripheral Frequenc
y 2,3,4
—
—
80
MHz
Master Loopback
—
fop
Operating frequency
—
—
15
MHz
Slave
1
fop
Operating frequency
—
—
15
MHz
Master
1
fop
Operating 
frequency 5
—
—
10
MHz
Slave_10Mbps
1
fop
Operating 
frequency 5
—
—
10
MHz
Master_10Mbps
1
fop
Operating 
frequency 4,6
—
—
20
MHz
Master Loopback
1
tSPSCK
SPSCK period
66
—
—
ns
Slave
2
tSPSCK
SPSCK period
66
—
—
ns
Master
2
tSPSCK
SPSCK period 4
50
—
—
ns
Master Loopback
2
tSPSCK
SPSCK period
100
—
—
ns
Master_10Mbps
2
tSPSCK
SPSCK period
100
—
—
ns
Slave_10Mbps
2
tLEAD
Enable lead time 
(PCS to SPSCK 
delay) 7
tSPCK/2
—
—
ns
Slave
3
tLEAD
Enable lead time 
(PCS to SPSCK 
delay) 7
30
—
—
ns
Master
3
tLEAD
Enable lead time 
(PCS to SPSCK 
delay) 4,7
30
—
—
ns
Master Loopback
3
Table continues on the next page...
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
96 / 152


---
# 페이지 97

Table 44. LPSPI (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
tLAG
Enable lag time 
(After SPSCK 
delay) 8
tSPCK/2
—
—
ns
Slave
4
tLAG
Enable lag time 
(After SPSCK 
delay) 8
30
—
—
ns
Master
4
tLAG
Enable lag time 
(After SPSCK 
delay) 4,8
30
—
—
ns
Master Loopback
4
tWSPCK
Clock (SPSCK) time 
(SPSCK duty 
cycle) 9
tSPSCK/
2 - 3
—
tSPSCK/
2 + 3
ns
Slave
5
tWSPCK
Clock (SPSCK) time 
(SPSCK duty 
cycle) 9
tSPSCK/
2 - 3
—
tSPSCK/
2 + 3
ns
Master
5
tWSPCK
Clock (SPSCK) time 
(SPSCK duty 
cycle) 4,9
tSPSCK/
2 - 3
—
tSPSCK/
2 + 3
ns
Master Loopback
5
tSU
Data setup 
time(inputs)
6
—
—
ns
Slave
6
tSU
Data setup 
time(inputs)
25
—
—
ns
Master
6
tSU
Data setup 
time(inputs)
5
—
—
ns
Slave_10Mbps
6
tSU
Data setup 
time(inputs)
36
—
—
ns
Master_10Mbps
6
tSU
Data setup 
time(inputs) 4
6
—
—
ns
Master_Loopback
6
tHI
Data hold 
time(inputs)
3
—
—
ns
Slave
7
tHI
Data hold 
time(inputs)
0
—
—
ns
Master
7
tHI
Data hold 
time(inputs)
4
—
—
ns
Slave_10Mbps
7
tHI
Data hold 
time(inputs)
0
—
—
ns
Master_10Mbps
7
tHI
Data hold 
time(inputs) 4
3
—
—
ns
Master Loopback
7
tA
MISO valid time after 
SS assertion
—
—
50
ns
Slave
8
Table continues on the next page...
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
97 / 152


---
# 페이지 98

Table 44. LPSPI (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
tDIS
Slave MISO (SOUT) 
disable time
—
—
50
ns
Slave
9
tV
Data valid (after 
SPSCK edge) 10
—
—
26
ns
Slave
10
tV
Data valid (after 
SPSCK edge) 10
—
—
14
ns
Master
10
tV
Data valid (after 
SPSCK edge) 10
—
—
36
ns
Slave_10Mbps
10
tV
Data valid (after 
SPSCK edge) 10
—
—
21
ns
Master_10Mbps, for 
all S32K3xx variants 
except S32K3x8
10
tV
Data valid (after 
SPSCK edge) 10
—
—
24
ns
Master_10Mbps, for 
S32K3x8
10
tV
Data valid (after 
SPSCK edge) 4,10
—
—
8
ns
Master Loopback, 
applies to S32K388 
LPSPI2 and LPSPI5 
@20MHz
10
tV
Data valid (after 
SPSCK edge) 4,10
—
—
8
ns
Master Loopback, 
applies to S32K389 
LPSPI1, LPSPI2, 
LPSPI3, LPSPI4 and 
LPSPI5 @20MHz
10
tV
Data valid (after 
SPSCK edge) 4,10
—
—
17.5
ns
Master Loopback, 
applies to all devices 
LPSPI0 @20 MHz
10
tHO
Data hold time 
(outputs) 10
3
—
—
ns
Slave
11
tHO
Data hold time 
(outputs) 10
-8
—
—
ns
Master
11
tHO
Data hold time 
(outputs) 10
3
—
—
ns
Slave_10Mbps
11
tHO
Data hold time 
(outputs) 10
-15
—
—
ns
Master_10Mbps, for 
all S32K3xx variants 
except S32K3x8
11
tHO
Data hold time 
(outputs) 10
-18
—
—
ns
Master_10Mbps, for 
S32K3x8
11
tHO
Data hold time 
(outputs) 4,10
-4.5
—
—
ns
Master Looopback, 
applies to S32K389 
LPSPI1, LPSPI2, 
LPSPI3, LPSPI4 and 
LPSPI5 @20MHz
11
Table continues on the next page...
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
98 / 152


---
# 페이지 99

Table 44. LPSPI (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
tHO
Data hold time 
(outputs) 4,10
-4.5
—
—
ns
Master Looopback, 
applies to S32K388 
LPSPI2 and LPSPI5 
@20MHz
11
tHO
Data hold time 
(outputs) 4,10
-2
—
—
ns
Master Loopback, 
applies to all devices 
LPSPI0 @20 MHz
11
tRI/FI
Rise/Fall time 
input 11
—
—
1
ns
Slave
—
tRI/FI
Rise/Fall time 
input 11
—
—
1
ns
Master
—
tRI/FI
Rise/Fall time 
input 4,11
—
—
1
ns
Master Loopback
—
1. For LPSPI0 instance, max. peripheral frequency is equal to AIPS_PLAT_CLK.
2. tperiph = 1/fperiph
3. fperiph = LPSPI peripheral clock
4. Master Loopback mode: In this mode LPSPI_SCK clock is delayed for sampling the input data which is enabled by setting 
LPSPI_CFGR1[SAMPLE] bit as 1.
5. These specifications apply to the SPI operation, as master or slave, at up to 10 Mbps for the combinations not indicated 
in the table below. Unless otherwise noted, all other ‘master’ and ‘slave’ specifications are also applicable in the 10Mbps 
configurations. See table "LPSPI 20 MHz and 15 MHz Combinations.
6. LPSPI0 support up to 20MHz on fast pin.
7. Minimum configuration value for CCR[PCSSCK] field is 3(0x00000011).
8. Minimum configuration value for CCR[SCKPCS] field is 3(0x00000011).
9. While selecting odd dividers, ensure Duty Cycle is meeting this parameter.
10. Output rise/fall time is determined by the output load and GPIO pad drive strength setting. See the GPIO specifications for 
detail.
11. The input rise/fall time specification applies to both clock and data, and is required to guarantee related timing parameters.
SLAVE
MSB OUT
SLAVE LSB OUT
BIT 6 ... 1
BIT 6 ... 1
SS
(INPUT)
SPSCK
(CPOL = 0)
(INPUT)
SPSCK
(CPOL = 1)
(INPUT)
MOSI
(INPUT)
MISO
(OUTPUT)
LSB IN
MSB IN
3
5
5
7
6
11
10
8
4
2
9
Figure 45. LPSPI Slave Mode Timing (CPHA=1)
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
99 / 152


---
# 페이지 100

SLAVE MSB
SLAVE LSB OUT
BIT 6 ... 1
MSB IN
SS
(INPUT)
SPSCK
(CPOL = 0)
(INPUT)
SPSCK
(CPOL = 1)
(INPUT)
MOSI
(INPUT)
MISO
(OUTPUT)
LSB IN
BIT 6 ... 1
3
5
5
7
10
8
11
6
12
13
12
13
4
2
9
11
Figure 46. LPSPI Slave Mode Timing (CPHA=0)
MSB OUT2
LSB OUT
BIT 6 ... 1
MSB IN2
SS1
(OUTPUT)
SPSCK
(CPOL = 0)
(OUTPUT)
SPSCK
(CPOL = 1)
(OUTPUT)
MISO
(INPUT)
MOSI
(OUTPUT)
LSB IN
BIT 6 ... 1
3
5
5
7
10
11
6
4
2
Figure 47. LPSPI Master Mode Timing (CPHA=0)
PORT DATA
PORT DATA
MASTER MSB OUT
MASTER LSB OUT
BIT 6 ... 1
MSB IN2
SS1
(OUTPUT)
SPSCK
(CPOL = 0)
(OUTPUT)
SPSCK
(CPOL = 1)
(OUTPUT)
MISO
(INPUT)
MOSI
(OUTPUT)
LSB IN
BIT 6 ... 1
3
5
5
7
10
11
6
4
2
Figure 48. LPSPI Master Mode Timing (CPHA=1)
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
100 / 152


---
# 페이지 101

12.2 LPSPI0 20 MHz and 15 MHz Combinations
 
15 and 20 Mbps is supported on LPSPI0 only.
  NOTE  
All measurements are with maximum output load of 25pF (except 30pF support on K358 with Standard-Plus IOs, and 50pF 
support on K388 with Standard-Plus IOs). S32K31x devices support only 15 MHz modes and all other devices support both 15 
and 20 MHz combinations.
Table 45. LPSPI0 20 MHz and 15 MHz Combinations
PORT
SPI Signal
20Mbps (In loopback 
mode only)
15 Mbps
PTB1
LPSPI0_SOUT
LPSPI0_SOUT
PTB0
LPSPI0_PCS0
LPSPI0_PCS0
PTC9
LPSPI0_SIN
LPSPI0_SIN
PTC8
LPSPI0_SCK
LPSPI0_SCK
PTD6
LPSPI0_PCS0
LPSPI0_PCS0
PTD5
LPSPI0_PCS1
LPSPI0_PCS1
PTD12
LPSPI0_SOUT
LPSPI0_SOUT
PTD11
LPSPI0_SCK
LPSPI0_SCK
PTD10
LPSPI0_SIN
LPSPI0_SIN
 
Trace length should not exceed 11 inches for SCK pad when used in Master loopback mode.
  NOTE  
12.3 LPSPI2 and LPSPI5 20MHz combination for S32K388 and S32K389
 
LPSPI running at 20MHz speed is possible only on specific pads as per table below.
  NOTE  
All measurements are with maximum output load of 25pF.
Table 46. LPSPI2 and LPSPI5 20MHz combination for S32K388 and S32K389
LPSPI Instance
Signal Type
PIN
LPSPI Signal
LPSPI2 Master Loopback
PCS
PTF7
LPSPI2_PCS0
SCK
PTA11
LPSPI2_SCK
SOUT
PTF4
LPSPI2_SOUT
SIN
PTE24
LPSPI2_SIN
LPSPI5 Master Loopback
PCS
PTG23
LPSPI5_PCS0
SCK
PTD31
LPSPI5_SCK
SOUT
PTG25
LPSPI5_SOUT
SIN
PTD28
LPSPI5_SIN
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
101 / 152


---
# 페이지 102

Table 47. LPSPI5 and LPSPI0 20MHz combination for S32K388 and S32K389
LPSPI Instance
Signal Type
PIN
LPSPI Signal
LPSPI5 Master Loopback
PCS
PTD17
LPSPI5_PCS0
SCK
PTD14
LPSPI5_SCK
SOUT(MOSI)
PTE9
LPSPI5_SOUT
SIN(MISO)
PTD13
LPSPI5_SIN
LPSPI0 Master Loopback
PCS
PTD6
LPSPI0_PCS0
SCK
PTD11
LPSPI0_SCK
SOUT(MOSI)
PTD12
LPSPI0_SOUT
SIN(MISO)
PTD10
LPSPI0_SIN
Table 48. LPSPI1, LPSPI3 and LPSPI4 for S32K389
LPSPI Instance
Signal Type
PIN
LPSPI Signal
LPSPI1 Master Loopback
PCS
PTI16
LPSPI1_PCS0
SCK
PTI14
LPSPI1_SCK
SOUT
PTI18
LPSPI1_SOUT
SIN
PTI20
LPSPI1_SIN
LPSPI3 Master Loopback
PCS
PTJ12
LPSPI3_PCS0
SCK
PTJ10
LPSPI3_SCK
SOUT
PTJ14
LPSPI3_SOUT
SIN
PTJ16
LPSPI3_SIN
LPSPI4 Master Loopback
PCS
PTJ29
LPSPI4_PCS0
SCK
PTK0
LPSPI4_SCK
SIN
PTJ23
LPSPI4_SIN
SOUT
PTJ26
LPSPI4_SOUT
12.4 Communication between two S32K388 devices
S32K388 devices supports fast data sending between two of them. Interface uses is four data lines at frequency of 6.6MHz in one 
direction and four data lines at frequency of 6.6MHz in opposite direction. Configuration of LPSPI interface is 4x data lines half 
duplex mode. For purpose of this communication LPSPI2, LPSPI5 and set of PINs was designed. Below figure shows diagram of 
connection between two S32K388 devices. Left device will use LPSPI2 in Master 4x data line half duplex mode to send data to 
LPSPI2 in Slave 4x dataline half duplex mode on second device. Similarly LPSPI5, but for in opposite direction than LPSPI2 do.
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
102 / 152


---
# 페이지 103

K388 Right
LPSPI 2
Master mode 
K388 Left
PCS
SCK
D0
D1
D2
D3
PCS
SCK
D0
D1
D2
D3
LPSPI 5
Slave mode
LPSPI 5
Master mode
LPSPI 2
Slave mode
Figure 49. Connection between two S32K388 devices
Table 49. Pins and signals assignment for this communication.
K388 Left
K388 Right
LPSPI instance
Signal 
type
PIN
LPSPI signal
LPSPI instance
Signal 
type
PIN
LPSPI signal
LPSPI2
Master mode
PCS
PTF7
LPSPI2_PCS0
LPSPI2
Slave mode
PCS
PTF7
LPSPI2_PCS0
SCK
PTA11
LPSPI2_SCK
SCK
PTA11
LPSPI2_SCK
D0
PTF4
LPSPI2_SOUT
D0
PTF4
LPSPI2_SOUT
D1
PTE24
LPSPI2_SIN
D1
PTE24
LPSPI2_SIN
D2
PTH0
LPSPI2_PCS2
D2
PTH0
LPSPI2_PCS2
D3
PTH1
LPSPI2_PCS3
D3
PTH1
LPSPI2_PCS3
LPSPI5
Slave mode
PCS
PTG23
LPSPI5_PCS0
LPSPI5
Master mode
PCS
PTG28
LPSPI5_PCS0
SCK
PTD31
LPSPI5_SCK
SCK
PTG31
LPSPI5_SCK
D0
PTG25
LPSPI5_SOUT
D0
PTG30
LPSPI5_SOUT
D1
PTD28
LPSPI5_SIN
D1
PTG29
LPSPI5_SIN
D2
PTG24
LPSPI5_PCS2
D2
PTG13
LPSPI5_PCS2
D3
PTD30
LPSPI5_PCS3
D3
PTG8
LPSPI5_PCS3
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
103 / 152


---
# 페이지 104

12.4.1 Timing specification for S32K388 to S32K388 communication
Below table lists the timing parameters for this communication. This parameters is valid only on set of pins preselected for this 
device to device communication. All timing is shown with respect to 50% VDD_HV_A/B thresholds. All measurements are with 
maximum output load of 50 pF, input transition of 1 ns and pad configured with fastest slew setting (DSE = 1'b1).
Table 50. Timing specification for S32K388 to S32K388 communication
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
fcom
Communication 
frequency
—
—
6.6
MHz
—
—
tWSPCK
Clock (SPSCK) high 
or low time (SPSCK 
duty cycle)
69
—
79
ns
—
—
tSU
Data setup time
34
—
—
ns
Master mode
6
tSU
Data setup time
5
—
—
ns
Slave mode
6
tV
Data valid (after 
SPSCK edge)
—
—
21
ns
Master mode
10
tV
Data valid (after 
SPSCK edge)
—
—
34
ns
Slave mode
10
tHO
Input hold time
0
—
—
ns
Master mode input
7
tHO
Input hold time
4
—
—
ns
slave mode input
7
tHO
Output hold time
3
—
—
ns
Slave mode output
11
tHO
Output hold time
-15
—
—
ns
Master mode output
11
tLEAD
Enable lead time 
(PCS to SPSCK 
delay)
30
—
—
ns
Master mode
3
tA
Slave access time
—
—
50
ns
—
—
tDIS
Slave MISO (SOUT) 
disable time
—
—
50
ns
—
—
tLAG
Enable lag time 
(After SPSCK delay)
30
—
—
ns
—
—
12.5 I2C
See I/O parameters for I2C specification.
"For supported baud rate see section 'Chip-specific LPI2C information' of the Reference Manual."
12.6 FlexCAN characteristics
See I/O parameters for FlexCAN specification.
"For supported baud rate, see section 'Protocol timing' of the Reference Manual."
12.7 SAI electrical specifications
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
104 / 152


---
# 페이지 105

12.7.1 SAI Electrical Characteristics, Slave Mode
The following table describes the SAI electrical characteristics. Measurements are with maximum output load of 30pF, 
input transition of 1ns and pad configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97 V to 3.63 V.
Valid pin combinations to be referred from K3xx*_Use sheet in IOmux.
Table 51. SAI Electrical Characteristics, Slave Mode
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
S13
SAI_BCLK cycle 
time (input)
80
—
—
ns
—
—
S14
SAI_BCLK pulse 
width high/low 
(input) 1
45
—
55
%
—
—
S15
SAI_RXD input 
setup before 
SAI_BCLK
8
—
—
ns
—
—
S16
SAI_RXD input hold 
after SAI_BCLK
2
—
—
ns
—
—
S17
SAI_BCLK to 
SAI_TXD output 
valid
—
—
28
ns
—
—
S18
SAI_BCLK to 
SAI_TXD output 
invalid
0
—
—
ns
—
—
S19
SAI_FS input setup 
before SAI_BCLK
8
—
—
ns
—
—
S20
SAI_FS input hold 
after SAI_BCLK
2
—
—
ns
—
—
S21
SAI_BCLK to 
SAI_FS output valid
—
—
28
ns
—
—
S22
SAI_BCLK to 
SAI_FS output 
invalid
0
—
—
ns
—
—
1. The slave mode parameters (S15 - S22) assume 50% duty cycle on SAI_BCLK input. Any change in SAI_BCLK duty cycle 
input must be taken care during the board design or by the master timing.
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
105 / 152


---
# 페이지 106

SAI_TXD
SAI_RXD
SAI_FS (output)
SAI_BCLK (input)
S16
S17
S21
S14
S13
S14
S19
S18
S18
S17
S15
SAI_FS (input)
S20
S22
Figure 50. SAI slave mode
12.7.2 SAI Electrical Characteristics, Master Mode
The following table describes the SAI electrical characteristics. Measurements are with maximum output load of 30pF, 
input transition of 1ns and pad configured with DSE = 1'b1 and SRE = 1'b 0. I/O operating voltage ranges from 2.97 V to 3.63 V.
Valid pin combinations to be referred from K3xx*_Use sheet in IOmux.
Table 52. SAI Electrical Characteristics, Master Mode
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
S1
SAI_MCLK cycle 
time
40
—
—
ns
—
—
S2
SAI_MCLK pulse 
width high/low
45
—
55
%
—
—
S3
SAI_BCLK cycle 
time
80
—
—
ns
—
—
S4
SAI_BCLK pulse 
width high/low
45
—
55
%
—
—
S5
SAI_RXD input 
setup before 
SAI_BCLK
28
—
—
ns
—
—
S6
SAI_RXD input hold 
after SAI_BCLK
0
—
—
ns
—
—
S7
SAI_BCLK to 
SAI_TXD output 
valid
—
—
8
ns
—
—
S8
SAI_BCLK to 
SAI_TXD output 
invalid
-2
—
—
ns
—
—
S9
SAI_FS input setup 
before SAI_BCLK
28
—
—
ns
—
—
Table continues on the next page...
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
106 / 152


---
# 페이지 107

Table 52. SAI Electrical Characteristics, Master Mode (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
S10
SAI_FS input hold 
after SAI_BCLK
0
—
—
ns
—
—
S11
SAI_BCLK to 
SAI_FS output valid
—
—
8
ns
—
—
S12
SAI_BCLK to 
SAI_FS output 
invalid
-2
—
—
ns
—
—
Figure 51. SAI master mode
12.8 Ethernet characteristics
12.8.1 Ethernet MII (10/100 Mbps)
The following timing specs are defined at the device I/O pin and must be translated appropriately to arrive at timing specs/ 
constraints for the physical interface. Measurements are with maximum output load of 25pF, input transition of 1ns and pad 
configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97 V to 3.63 V.
Valid pin combinations to be referred from K3xx*_Use sheet in IOmux.
Table 53. Ethernet MII (10/100 Mbps)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
—
RXCLK frequency
—
2.5/25
—
MHz
10/100 Mbps
—
MII1
RXCLK pulse width 
high
35
—
65
%RXCLK 
period
—
—
Table continues on the next page...
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
107 / 152


---
# 페이지 108

Table 53. Ethernet MII (10/100 Mbps) (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
MII2
RXCLK pulse width 
low
35
—
65
%RXCLK 
period
—
—
MII3
RXD[3:0], RXDV, 
RXER to RXCLK 
setup
5
—
—
ns
10/100 Mbps
—
MII4
RXCLK to RXD[3:0], 
RXDV, RXER hold
5
—
—
ns
10/100 Mbps
—
tCYC_TX
TXCLK frequency
—
2.5 / 25
—
MHz
10/100 Mbps
—
MII5
TXCLK pulse width 
high
35
—
65
%TXCLK 
period
—
—
MII6
TXCLK pulse 
width low
35
—
65
%TXCLK 
period
—
—
MII7
TXCLK to TXD[3:0], 
TXEN, TXER invalid
2
—
—
ns
—
—
MII8
TXCLK to TXD[3:0], 
TXEN, TXER valid
—
—
25
ns
—
—
Figure 52. MII receive diagram
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
108 / 152


---
# 페이지 109

Figure 53. MII transmit diagram
12.8.2 Ethernet MII (200 Mbps)
The following timing specs are defined at the device I/O pin and must be translated appropriately to arrive at timing specs/ 
constraints for the physical interface. Measurements are with maximum output load of 25pF, input transition of 1ns and pad 
configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97 V to 3.63 V.
Valid pin combinations to be referred from K3xx*_Use sheet in IOmux.
Table 54. Ethernet MII (200 Mbps)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
—
RXCLK frequency
—
—
50
MHz
—
—
MII1
RXCLK pulse width 
high
35
—
65
% 
RXCLK 
period
—
—
MII2
RXCLK pulse width 
low
35
—
65
% 
RXCLK 
period
—
—
MII3
RXD[3:0], RXDV, 
RXER to RXCLK 
setup time
4
—
—
ns
—
—
MII4
RXCLK to RXD[3:0], 
RXDV, RXER hold 
time
2
—
—
ns
—
—
—
TXCLK frequency
—
—
50
MHz
—
—
Table continues on the next page...
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
109 / 152


---
# 페이지 110

Table 54. Ethernet MII (200 Mbps) (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
MII5
TXCLK pulse width 
high
35
—
65
% 
TXCLK 
period
—
—
MII6
TXCLK pulse width 
low
35
—
65
% 
TXCLK 
period
—
—
MII7
TXCLK to TXD[3:0], 
TXDV, TXER invalid
2
—
—
ns
—
—
MII8
TXCLK to TXD[3:0], 
TXDV, TXER valid
—
—
15
ns
—
—
Figure 54. MII receive diagram
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
110 / 152


---
# 페이지 111

Figure 55. MII transmit diagram
12.8.3 Ethernet RMII (10/100 Mbps)
The following timing specs are defined at the device I/O pin and must be translated appropriately to arrive at timing specs/ 
constraints for the physical interface. Measurements are with maximum output load of 25pF, input transition of 1ns and pad 
configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97 V to 3.63 V.
Valid pin combinations to be referred from K3xx*_Use sheet in IOmux.
Table 55. Ethernet RMII (10/100 Mbps)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
—
RMII input 
clock frequency 
(RMII_CLK)
—
—
50
MHz
10/100 Mbps
—
RMII1,RMII5
RMII_CLK pulse 
width high
35
—
65
%RMII_C
LK period
—
—
RMII2,RMII6
RMII_CLK pulse 
width low
35
—
65
%RMII_C
LK period
—
—
RMII3
RXD[1:0], CRS_DV, 
RXER to RMII_CLK 
setup
4
—
—
ns
—
—
RMII4
RMII_CLK to 
RXD[1:0], CRS_DV, 
RXER hold
2
—
—
ns
—
—
Table continues on the next page...
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
111 / 152


---
# 페이지 112

Table 55. Ethernet RMII (10/100 Mbps) (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
RMII8
RMII_CLK to 
TXD[1:0], TXEN 
data valid
—
—
15
ns
—
—
RMII7
RMII_CLK to 
TXD[1:0], TXEN 
data invalid
2
—
—
ns
—
—
Figure 56. RMII receive diagram
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
112 / 152


---
# 페이지 113

Figure 57. RMII transmit diagram
12.8.4 Ethernet RGMII
The following timing specs are defined at the device I/O pin and must be translated appropriately to arrive at timing specs/ 
constraints for the physical interface. Measurements are with maximum output load of 13.5pF, input transition of 1ns and pad 
configured with DSE = 1'b1 and SRE = 1'b0.
Valid pin combinations to be referred from K3xx*_Use sheet in IOmux.
Table 56. Ethernet RGMII
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
Tcyc
Clock cycle 
duration 1,2
7.2
—
8.8
ns
SRC = 0
—
TskewT
Data to clock 
output skew (at 
transmitter) 2
-500
—
500
ps
SRC=0
—
TskewRi
Data to clock input 
skew (at receiver) 2
1
—
2.6
ns
SRC=0
—
TskewRo
Data to clock output 
skew (at receiver) 2
-650
—
650
ps
SRC=0
—
Duty_G
Clock duty cycle for 
Gigabit 2
45
—
55
%
SRC=0
—
Duty_T
Clock duty cycle for 
10/100T 2
40
—
60
%
SRC=0
—
Tr
Output rise time 3
—
—
1
ns
SRC=0
—
Tf
Output fall time 3
—
—
1
ns
SRC=0
—
1. For 10 Mbps and 100 Mbps, Tcyc will scale to 400 ns ±40 ns and 40 ns ±4 ns respectively.
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
113 / 152


---
# 페이지 114

2. RGMII timing specifications is valid for 3.3V nominal I/O pad supply voltage.
3. Output timing valid for maximum external load CL = 13.5 pF (includes PCB trace, package trace (around 2pF) and flash 
input load).
RXC (at transmitter)
RXC (at receiver)
RX_CTL
RXD[8:5][3:0]
RXD[7:4][3:0]
RXD[8:5]
RXD[7:4]
RXD[3:0]
RXD[4]
RXDV
RXD[9]
RXERR
TskewT
TskewR
Figure 58. RGMII Receive Timing
TXC (at transmitter)
TXC (at receiver)
TX_CTL
TXD[8:5][3:0]
TXD[7:4][3:0]
TXD[8:5]
TXD[7:4]
TXD[3:0]
TXD[4]
TXEN
TXD[9]
TXERR
TskewT
TskewR
Figure 59. RGMII Transmit Timing
12.8.5 MDIO timing specifications
The following table describes the MDIO electrical characteristics. Measurements are with maximum output load of 25 pF, input 
transition of 1 ns and pad configured with fastest slew settings (DSE = 1'b1 and SRE = 1’b0). I/O operating voltage ranges from 
2.97 V to 3.63 V. MDIO pin must have external Pull-up.
Valid pin combinations to be referred from K3xx*_Use sheet in IOmux.
Table 57. MDIO timing specifications
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
—
MDC clock 
frequency
—
—
2.5
MHz
—
—
MDC1
MDC pulse width 
high
40
—
60
%MDC 
period
—
MDC1
MDC2
MDC pulse width low 40
—
60
%MDC 
period
—
MDC2
MDC5
MDC falling edge 
to MDIO output 
valid(maximum 
propagation delay)
—
—
25
ns
—
MDC5
Table continues on the next page...
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
114 / 152


---
# 페이지 115

Table 57. MDIO timing specifications (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
MDC6
MDC falling edge 
to MDIO output 
invalid(minimum 
propagation delay)
-10
—
—
ns
—
MDC6
MDC3
MDIO (input) to 
MDC rising edge 
setup time
25
—
—
ns
Applies to S32K3x4, 
S32K342, S32K341, 
S32K322, S32K328, 
S32K338, S32K348, 
S32K358 and all GPIO 
pads of S32K388 
except GPIO[113]
MDC3
MDC3
MDIO (input) to 
MDC rising edge 
setup time
29.5
—
—
ns
Applies to GPIO[113] 
pad of S32K388
MDC3
MDC4
MDIO (input) to 
MDC rising edge 
hold time
0
—
—
ns
—
MDC4
MDC (output)
MDIO (output)
MDIO (input)
MDC6
MDC5
MDC3
MDC4
MDC1
MDC2
Figure 60. MII/RMII serial management channel timing
12.9 QuadSPI
12.9.1 QuadSPI Quad 3.3V SDR 120MHz
The following table applies to S32K344, S32K324, S32K314, S32K342, S32K341, S32K322,  S32K328, S32K338, S32K348, 
and S32K358.
The following table describes the QuadSPI electrical characteristics. Measurements are with maximum output load of 25pF, input 
transition of 1ns and pads configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97V to 3.63V. QuadSPI 
trace length should be less than or equal to 2 inches. For Single and Dual IO modes of operation if external device doesn’t have 
pull-up feature, then external pull-up must be added at board level for unused device pins. With external pull-up, performance 
of the interface may degrade in Quad IO mode based on load associated with external pull-up. QuadSPI support delay chain 
upto length 16, wherein delay length of low-frequency segment is 16 and length of high-frequency segment is 0. See the device 
Reference Manual for register and bit descriptions. 
Valid pin combinations to be referred from K3xx*_Use sheet in IOmux
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
115 / 152


---
# 페이지 116

Program register value QuadSPI_FLSHCR[TCSS] = 4`h3.
Program register value QuadSPI_FLSHCR[TCSH] = 4`h3.
Program register value QuadSPI_DLLCRA[SLV_FINE_OFFSET] to 4'b0001.
Data transitions measured at 30%/70% supply for the write path. Data transitions measured at mid-supply for the read path. Clock 
transitions measured at mid-supply.
Table 58. QuadSPI Quad 3.3V SDR 120MHz
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
fSCK
SCK clock 
frequency 1
—
—
120
MHz
Pad Loopback
—
fSCK
SCK clock 
frequency 1
—
—
60
MHz
Internal Loopback
—
tSCK
SCK clock period
1/fSCK
—
—
ns
Pad Loopback
—
tSCK
SCK clock period
1/fSCK
—
—
ns
Internal Loopback
—
tSDC
SCK duty cycle 2
45
—
55
%
Internal Loopback
—
tSDC
SCK duty cycle 2
45
—
55
%
Pad Loopback
—
tIS
Data input setup 
time
1.75
—
—
ns
Pad Loopback
—
tIS
Data input setup 
time
9
—
—
ns
Internal Loopback
—
tIH
Data input hold time
1
—
—
ns
Pad Loopback
—
tIH
Data input hold time
1
—
—
ns
Internal Loopback
—
tOV
Data output valid 
time
—
—
1.75
ns
Pad Loopback
—
tOV
Data output valid 
time
—
—
1.75
ns
Internal Loopback
—
tIV
Data output invalid 
time
-1.5
—
—
ns
Pad Loopback
—
tIV
Data output invalid 
time
-1.5
—
—
ns
Internal Loopback
—
tCSSCK
CS to SCK time
5
—
—
ns
Pad Loopback
—
tCSSCK
CS to SCK time
5
—
—
ns
Internal Loopback
—
tSCKCS
SCK to CS time
3
—
—
ns
Pad Loopback
—
tSCKCS
SCK to CS time
3
—
—
ns
Internal Loopback
—
1. This frequency specification is valid only if output valid time of external flash is ≤ 5.5ns, and if output valid time of 
external flash is more than 5.5ns but ≤ 6.5ns, then maximum fSCK is 104MHz.
2. For S32K342 100HDQFP, tSDC spec would be 44%-56% when ENET and SAI active along with QuadSPI at 120MHZ
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
116 / 152


---
# 페이지 117

Figure 61. QuadSPI input timing (SDR mode)
Figure 62. QuadSPI output timing (SDR mode)
12.9.2 QuadSPI Octal 3.3V DDR 100MHz
The following table applies to S32K328, S32K338, S32K348, S32K358.
The following table describes the QuadSPI electrical characteristics. Measurements are with maximum output load of 25pF, input 
transition of 1ns and pads configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97V to 3.63V. QuadSPI 
trace length should be less than or equal to 2 inches. For Single and Dual IO modes of operation if external device doesn’t have 
pull-up feature, then external pull-up must be added at board level for unused device pins. With external pull-up, performance 
of the interface may degrade in Quad IO mode based on load associated with external pull-up. QuadSPI support delay chain 
upto length 16, wherein delay length of low-frequency segment is 16 and length of high-frequency segment is 0. See the device 
Reference Manual for register and bit descriptions.
Valid pin combinations to be referred from K3xx*_Use sheet in IOmux.
Set FLSHCR[TCSS]=2 and FLSHCR[TCSH]=5.
Data transitions measured at 30%/70% supply for the write path. Data transitions measured at mid-supply for the read path. Clock 
transitions measured at mid-supply.
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
117 / 152


---
# 페이지 118

Table 59. QuadSPI Octal 3.3V DDR 100MHz
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
fSCK_DQS
SCK / DQS 
frequency 1
—
—
100
MHz
—
—
tSDC
SCK duty cycle
45
—
55
%
—
—
tCL_SCK_DQS
SCK / DQS low 
time 1
4.500
—
—
ns
—
—
tCH_SCK_DQS
SCK / DQS high 
time 1
4.500
—
—
ns
—
—
tOD_DATA
Data output delay 
(w.r.t. SCK)
1.016
—
3.484
ns
—
—
tOD_CS
CS output delay 
(w.r.t. SCK) 2
3.016 - n/
fSCK
—
-0.016 + 
m/fSCK
ns
—
—
tDVW
Input data valid 
window 1
3.284
—
—
ns
—
—
tISU_DQS
Input setup time 
(w.r.t. DQS) 1
-0.816
—
—
ns
—
—
tIH_DQS
Input hold time (w.r.t. 
DQS) 1
3.684
—
—
ns
—
—
1. Input timing assumes maximum input signal transition of 1 ns (20%/80%).  DQS denotes external strobe provided by the 
Flash.
2. Where m=TCSS and n=TCSH-1.
12.9.3 QuadSPI Quad 3.3V SDR 103.33MHz
The following table applies only to S32K388 and S32K389.
The following table describes the QuadSPI electrical characteristics. Measurements are with maximum output load of 25pF, input 
transition of 1ns and pads configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97V to 3.63V. QuadSPI 
trace length should be less than or equal to 2 inches. For Single and Dual IO modes of operation if external device doesn’t have 
pull-up feature, then external pull-up must be added at board level for unused device pins. With external pull-up, performance 
of the interface may degrade in Quad IO mode based on load associated with external pull-up. QuadSPI support delay chain 
upto length 16, wherein delay length of low-frequency segment is 16 and length of high-frequency segment is 0. See the device 
Reference Manual for register and bit descriptions. 
Valid pin combinations to be referred from K3xx*_Use sheet in IOmux.
Data transitions measured at 30%/70% supply for the write path. Data transitions measured at mid-supply for the read path. Clock 
transitions measured at mid-supply.
Table 60. QuadSPI Quad 3.3V SDR 103.33MHz
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
fSCK
SCK clock frequency —
—
103.33
MHz
—
—
tCL_SCK
SCK clock low time 1
4.327
—
—
ns
—
—
Table continues on the next page...
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
118 / 152


---
# 페이지 119

Table 60. QuadSPI Quad 3.3V SDR 103.33MHz (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
tCH_SCK
SCK clock high 
time 1
4.327
—
—
ns
—
—
tOD_DATA
Data output delay 
(w.r.t. SCK)
-2.330
—
2.880
ns
—
—
tOD_CS
CS output delay 
(w.r.t. SCK) 2
3.391 - n/
fSCK
—
5.901 + 
m/fSCK
ns
—
—
tDVW
Input data valid 
window 1
5.5
—
—
ns
—
—
tISU_SCK
Input setup time 
(w.r.t. SCK) 1
2.152
—
—
ns
—
—
tIH_SCK
Input hold time (w.r.t. 
SCK) 1
2.0
—
—
ns
—
—
1. Input timing assumes maximum input signal transition of 1ns (20%/80%).
2. Where m=TCSS and n=TCSH-1.
12.9.4 QuadSPI Octal 3.3V DDR 120MHz
The following table applies to S32K328, S32K338, S32K348, S32K358.
The following table describes the QuadSPI electrical characteristics. Measurements are with maximum output load of 25pF, input 
transition of 1ns and pads configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97V to 3.63V. QuadSPI 
trace length should be less than or equal to 2 inches. For Single and Dual IO modes of operation if external device doesn’t have 
pull-up feature, then external pull-up must be added at board level for unused device pins. With external pull-up, performance 
of the interface may degrade in Quad IO mode based on load associated with external pull-up. QuadSPI support delay chain 
upto length 16, wherein delay length of low-frequency segment is 16 and length of high-frequency segment is 0. See the device 
Reference Manual for register and bit descriptions.
Valid pin combinations to be referred from K3xx*_Use sheet in IOmux.
Set FLSHCR[TCSS]=2 and FLSHCR[TCSH]=5.
Data transitions measured at 30%/70% supply for the write path. Data transitions measured at mid-supply for the read path. Clock 
transitions measured at mid-supply
Table 61. QuadSPI Octal 3.3V DDR 120MHz
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
fSCK_DQS
SCK / DQS 
frequency 1
—
—
120
MHz
DLL enabled
—
fSCK_DQS
SCK / DQS 
frequency 1
—
—
120
MHz
DLL mode enabled
—
tSCK
SCK clock period
1/
fSCK_D
QS
—
—
ns
External DQS
—
Table continues on the next page...
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
119 / 152


---
# 페이지 120

Table 61. QuadSPI Octal 3.3V DDR 120MHz (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
tSDC
SCK / DQS duty 
cycle
45
—
55
%
External DQS
—
tCL_SCK_DQS
SCK / DQS low 
time 1
3.75
—
—
ns
—
—
tCH_SCK_DQS
SCK / DQS high 
time 1
3.75
—
—
ns
—
—
tOD_DATA
Data output delay 
(w.r.t. SCK)
0.816
—
2.934
ns
—
—
tOD_CS
CS output delay 
(w.r.t. SCK)
3.016
—
-0.766
ns
—
—
tDVW
Input data valid 
window 1
2.518
—
—
ns
—
—
tISU_DQS
Input setup time 
(w.r.t. DQS) 1
-0.616
—
—
ns
—
—
tIH_DQS
Input hold time (w.r.t. 
DQS) 1
3.134
—
—
ns
—
—
1. Input timing assumes an input signal transition of 1 ns (20%/80%).  DQS denotes external strobe provided by the Flash.
12.9.5 QuadSPI Quad 3.3V SDR 125MHz
The following table applies only to S32K388 and S32K389.
The following table describes the QuadSPI electrical characteristics. Measurements are with maximum output load of 25pF, input 
transition of 1ns and pads configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 2.97V to 3.63V. QuadSPI 
trace length should be less than or equal to 2 inches. For Single and Dual IO modes of operation if external device doesn’t have 
pull-up feature, then external pull-up must be added at board level for unused device pins. With external pull-up, performance 
of the interface may degrade in Quad IO mode based on load associated with external pull-up. QuadSPI support delay chain 
upto length 16, wherein delay length of low-frequency segment is 16 and length of high-frequency segment is 0. See the device 
Reference Manual for register and bit descriptions. 
Valid pin combinations to be referred from K3xx*_Use sheet in IOmux.
Data transitions measured at 30%/70% supply for the write path. Data transitions measured at mid-supply for the read path. Clock 
transitions measured at mid-supply.
Table 62. QuadSPI Quad 3.3V SDR 125MHz
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
fSCK
SCK clock 
frequency 1
—
—
125
MHz
—
—
tCL_SCK
SCK clock low time 1
3.6
—
—
ns
—
—
tCH_SCK
SCK clock high 
time 1
3.6
—
—
ns
—
—
Table continues on the next page...
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
120 / 152


---
# 페이지 121

Table 62. QuadSPI Quad 3.3V SDR 125MHz (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
tOD_DATA
Data output delay 
(w.r.t. SCK)
-1.294
—
1.844
ns
—
—
tOD_CS
CS output delay 
(w.r.t. SCK) 2
3.391 - n/
fSCK
—
3.829 + 
m/fSCK
ns
—
—
tDVW
Input data valid 
window 1
4.724
—
—
ns
—
—
tISU_SCK
Input setup time 
(w.r.t. SCK) 1
1.580
—
—
ns
—
—
tIH_SCK
Input hold time (w.r.t. 
SCK) 1
1.5
—
—
ns
—
—
1. Input timing assumes maximum input signal transition of 1ns (20%/80%).
2. Where m=TCSS and n=TCSH-1.
12.10 uSDHC
12.10.1 uSDHC SDR electrical specifications
The following table describes the uSDHC electrical characteristics. Measurements are with maximum output load of 
25pF, input transition of 1ns(20%/80%) and pad configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 
2.97 V to 3.63 V.
Valid pin combinations to be referred from K3xx*_Use sheet in IOmux.
Data transitions measured at 25%/62.5% at 3.3V for the write path. Data transitions measured at mid-supply for the read path. 
Clock transitions measured at mid-supply.
Table 63. uSDHC SDR electrical specifications
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
fpp
Clock frequency (low 
speed) 1
—
—
400
kHz
—
SD1
fpp
Clock frequency 
(eMMC4.4/4.41 
SDR, SD3.0 
SDR) 1,2
—
—
50
MHz
Medium/Fast Pad
SD1
fpp
Clock frequency 
(eMMC4.4/4.41 
SDR, SD3.0 
SDR) 1,3
—
—
25
MHz
Standard plus/Medium 
pad
SD1
fOD
Clock frequency 
(identification 
mode) 1
100
—
400
kHz
—
SD1
tWL
Clock low time
6
—
—
ns
Medium/Fast pad
SD2
Table continues on the next page...
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
121 / 152


---
# 페이지 122

Table 63. uSDHC SDR electrical specifications (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
tWL
Clock low time
12
—
—
ns
Standard plus/Medium 
pad
SD2
tWH
Clock high time
6
—
—
ns
Medium/Fast pad
SD3
tWH
Clock high time
12
—
—
ns
Standard plus/Medium 
pad
SD3
tTLH
Clock rise time 1,4
—
—
4
ns
Medium/Fast pad
SD4
tTLH
Clock rise time 1,4
—
—
8
ns
Standard plus/Medium 
pad
SD4
tTHL
Clock fall time 1,4
—
—
4
ns
Medium/Fast pad
SD5
tTHL
Clock fall time 1,4
—
—
8
ns
Standard plus/Medium 
pad
SD5
tOD
SDHC output delay 
(output valid) 1
-5.6
—
2.6
ns
fpp= 50 MHz, SDHC_
CLK to SDHC_DAT
SD6
tOD
SDHC output delay 
(output valid) 1
-5.6
—
10.64
ns
fpp= 25 MHz, 400 KHz, 
SDHC_CLK to SDHC_
CMD / SDHC_DAT
SD6
tOD
SDHC output delay 
(output valid) 1
-5.6
—
3.1
ns
fpp= 50 MHz, SDHC_
CLK to SDHC_CMD
SD6
tISU
SDHC Input setup 
time
6.3
—
—
ns
fpp= 25 MHz, 400 KHz, 
SDHC_CMD / SDHC_
DAT to SDHC_CLK
—
tISU
SDHC Input setup 
time
4.8
—
—
ns
fpp= 50 MHz, SDHC_
CMD / SDHC_DAT to 
SDHC_CLK
SD7
tIH
SDHC Input hold 
time
2
—
—
ns
SDHC_CLK to SDHC_
CMD / SDHC_DAT
SD8
1. Output timing valid for maximum external load CL = 25 pF (includes PCB trace, package trace (around 1-2pF) and flash 
input load).
2. In normal (full) speed mode for SD/SDIO card, clock frequency can be any value between 0–25 MHz. In high-speed 
mode, clock frequency can be any value between 0–50 MHz.
3. In normal (full) speed mode for MMC card, clock frequency can be any value between 0–25 MHz. In high-speed mode, 
clock frequency can be any value between 0–50 MHz.
4. The SDHC_CLK rise/fall time specification applies to the input clock transition required in order to meet the output delay 
specifications. SDHC_CLK output transition time is dependent on output load and GPIO pad drive strength. See the GPIO 
pad specifications for detail.
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
122 / 152


---
# 페이지 123

SD4
SD5
SDx_CLK
Output from uSDHC to card
SDx_DATA[7:0]
Input from card to uSDHC
SDx_DATA[7:0]
SD3
SD2
SD6
SD7
SD8
SD1
Figure 63. SD/eMMC4.3 High Speed Mode Interface Timing
12.10.2 uSDHC DDR electrical specifications
The following table describes the uSDHC electrical characteristics. Measurements are with maximum output load of 
25pF, input transition of 1ns(20%/80%) and pad configured with DSE = 1'b1 and SRE = 1'b0. I/O operating voltage ranges from 
2.97 V to 3.63 V.
Valid pin combinations to be referred from K3xx*_Use sheet in IOmux.
Data transitions measured at 25%/62.5% at 3.3V for the write path. Data transitions measured at mid-supply for the read path. 
Clock transitions measured at mid-supply.
Table 64. uSDHC DDR electrical specifications
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
fpp
Clock frequency 
(eMMC4.4/4.41 
DDR) 1
—
—
50
MHz
Medium/Fast pad
SD1
tWL
Clock low time
6
—
—
ns
Medium/Fast pad
—
tWH
Clock high time
6
—
—
ns
Medium/Fast pad
—
tTLH
Clock rise time 1,2
—
—
4
ns
Medium/Fast pad
—
tTHL
Clock fall time 1,2
—
—
4
ns
Medium/Fast pad
—
tOD
SDHC output delay 
(output valid) 1
2.7
—
6.53
ns
SDHC_CLK to SDHC_
DAT
SD2
tOD
SDHC output delay 
(output valid) 1
-5.6
—
2.6
ns
SDHC_CLK to SDHC_
CMD
SD6 
(See 
SDR 
figure)
tISU
SDHC Input setup 
time
1.6
—
—
ns
SDHC_DAT to SDHC_
CLK
SD3
tISU
SDHC Input setup 
time
4.8
—
—
ns
SDHC_CMD to SDHC_
CLK
SD7 
(See 
Table continues on the next page...
NXP Semiconductors
Communication interfaces
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
123 / 152


---
# 페이지 124

Table 64. uSDHC DDR electrical specifications (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
SDR 
figure)
tIH
SDHC Input hold 
time
1.5
—
—
ns
SDHC_CLK to SDHC_
DAT
SD4
tIH
SDHC Input hold 
time
1.5
—
—
ns
SDHC_CLK to SDHC_
CMD
SD8 
(See 
SDR 
figure)
1. Output timing valid for maximum external load CL = 25 pF (includes PCB trace, package trace (around 1-2pF) and flash 
input load).
2. The SDHC_CLK rise/fall time specification applies to the input clock transition required in order to meet the output delay 
specifications. SDHC_CLK output transition time is dependent on output load and GPIO pad drive strength. See the GPIO 
pad specifications for detail.
SDx_CLK
Output from eSDHCv3 to card
SDx_DATA[7:0]
Input from card to eSDHCv3
SDx_DATA[7:0]
SD2
SD3
SD4
SD2
.......
.......
SD1
Figure 64. SD/eMMC4.4/4.41 DDR50 Mode Interface Timing
12.11 LPUART specifications
See I/O parameters for LPUART specifications.
13 Debug modules
13.1 Debug trace timing specifications
The following table describes the Debug trace electrical characteristics. Measurements are with maximum output load of 25pF, 
input transition of 1ns and pad configured with DSE = 1'b1 and SRE = 1'b0.
See I/O parameters for GPIO electrical specifications.
NXP Semiconductors
Debug modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
124 / 152


---
# 페이지 125

Table 65. Debug trace timing specifications
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
fTRACE
Trace clock 
frequency (trace on 
Fast pads)
—
—
120
MHz
Applies to all 
K3xx variants except 
S32K388 and S32K389
—
fTRACE
Trace clock 
frequency (trace on 
Fast pads)
—
—
125
MHz
Applies to S32K388 
and S32K389
—
fTRACE
Trace clock 
frequency (trace on 
StandardPlus pads)
—
—
25
MHz
—
—
tDVW
Data output valid 
window
1.2
—
—
ns
—
—
tDIV
Data output invalid
0.3
—
—
ns
—
—
Figure 65. Trace CLKOUT specifications
13.2 SWD electrical specifications
The following table describes the SWD electrical characteristics. Measurements are with maximum output load of 30pF, input 
transition of 1ns and pad configured with DSE = 1'b1 and SRE = 1'b0.
See I/O parameters for GPIO electrical specifications.
Table 66. SWD electrical specifications
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
S1
SWD_CLK 
frequency
—
—
33
MHz
—
S1
S2
SWD_CLK cycle 
period
1 / S1
—
—
ns
—
S2
S3
SWD_CLK pulse 
width
40
—
60
%
—
S3
Table continues on the next page...
NXP Semiconductors
Debug modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
125 / 152


---
# 페이지 126

Table 66. SWD electrical specifications (continued)
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
S4
SWD_CLK rise and 
fall times
—
—
1
ns
—
S4
S9
SWD_DIO input 
data setup time to 
SWD_CLK rise
5
—
—
ns
—
S9
S10
SWD_DIO input 
data hold time 
after SWD_CLK 
rising edge
5
—
—
ns
—
S10
S11
SWD_CLK high to 
SWD_DIO output 
data valid
—
—
22
ns
—
S11
S12
SWD_CLK high to 
SWD_DIO output 
data hi-Z
—
—
22
ns
—
S12
S13
SWD_CLK high to 
SWD_DIO output 
data invalid
0
—
—
ns
—
S13
S2
S4
S4
S3
S3
SWD_CLK (input)
Figure 66. SWD Input Clock Timing
S12
SWD_CLK
SWD_DIO
SWD_DIO
SWD_DIO
Input data valid
Output data valid
S9
S10
S13
S11
Figure 67. SWD Output Data Timing
NXP Semiconductors
Debug modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
126 / 152


---
# 페이지 127

13.3 JTAG electrical specifications
The following table describes the JTAG electrical characteristics. These specifications apply to JTAG and boundary scan. 
Measurements are with maximum output load of 30pF, input transition of 1ns and pad configured with DSE = 1'b1 and SRE = 1'b0.
See I/O parameters for GPIO electrical specifications.
Table 67. JTAG electrical specifications
Symbol
Description
Min
Typ
Max
Unit
Condition
Spec 
Number
tJCYC
TCK cycle time 1,2
30
—
—
ns
—
1
tJDC
TCK clock pulse 
width
40
—
60
%
—
2
tTCKRISE
TCK rise/fall times 
(40%-70%)
—
—
1
ns
—
3
tTMSS, tTDIS
TMS, TDI data setup 
time
5
—
—
ns
—
4
tTMSH, tTDIH
TMS, TDI data hold 
time
5
—
—
ns
—
5
tTDOV
TCK low to TDO 
data valid 3
—
—
22
ns
—
6
tTDOI
TCK low to TDO 
data invalid
0
—
—
ns
—
7
tTDOHZ
TCK low to TDO 
high impedance
—
—
22
ns
—
8
tBSDV
TCK falling edge to 
output valid 4
—
—
600
ns
—
11
tBSDVZ
TCK falling edge to 
output valid out of 
high impedance
—
—
600
ns
—
12
tBSDHZ
TCK falling edge 
to output high 
impedance
—
—
600
ns
—
13
tBSDST
Boundary scan input 
valid to TCK rising 
edge
15
—
—
ns
—
14
tBSDHT
TCK rising edge to 
boundary scan input 
invalid
15
—
—
ns
—
15
1. This timing applies to TDI, TDO, TMS pins, however, actual frequency is limited by pad type for EXTEST instructions. 
Refer to pad specification for allowed transition frequency
2. Cycle time is 30ns assuming full cycle timing. Cycle time is 60ns assuming half cycle timing.
3. Timing includes TCK pad delay, clock tree delay, logic delay and TDO output pad delay.
4. Applies to all pins, limited by pad slew rate. Refer to IO delay and transition specification and add 20 ns for JTAG delay.
NXP Semiconductors
Debug modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
127 / 152


---
# 페이지 128

TCK
3
1
3
2
2
Figure 68. JTAG TCK Input Timing
TMS, TDI
TCK
5
6
4
7
8
TDO
Figure 69. JTAG Test Access Port Timing
NXP Semiconductors
Debug modules
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
128 / 152


---
# 페이지 129

13
11
12
14
15
TCK
Output
signals
Output
signals
Input
signals
Figure 70. Boundary Scan Timing
14 Thermal Attributes
14.1 Description
The tables in the following sections describe the thermal characteristics of the device.
 
Junction temperature is a function of die size, on-chip power dissipation, package thermal resistance, mounting 
side (board) temperature, ambient temperature, air flow, power dissipation or other components on the board, and 
board thermal resistance.
  NOTE  
14.2 Thermal characteristics
Thermal Design and Characteristics
• Junction temperature of the device does not solely depend on package thermal resistance but is also a function of chip 
power dissipation, PCB attributes, environmental conditions (ambient temperature & air flow) and cumulative effects of 
other heat generating ICs on the PCB.
• The appropriate thermal design must be carried out on package so that it can safely dissipate the necessary amount of 
power needed for it to function properly without exceeding the maximum junction temperature. This may involve adding a 
cooling solution on the package, creating thermal enhancements on the PCB and improving environmental conditions.
• The customer is encouraged to use the package model to perform design and risk assessment through simulations. 
Package models in FloTHERM or Icepak formats can be obtained under NDA from the sales team.
Thermal Ratings
• The table below is the package thermal ratings for LQFP, HDQFP & MAPBGA package variants. These numbers are 
derived through simulations based on standardized tests as described in the footnotes.
NXP Semiconductors
Thermal Attributes
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
129 / 152


---
# 페이지 130

• Thermal resistance data in this report is solely for a thermal performance comparison of one package to another in a 
standardized specified environment. It is not meant to predict the performance of a package in an application-specific 
environment :
NXP Semiconductors
Thermal Attributes
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
130 / 152


---
# 페이지 131

Table 68. Thermal characteristics
Rating
Conditions
Symbol
Package
Device
Unit
S32K311
S32K310
S32K312
S32K342
S32K341
S32K322
S32K344
S32K314
S32K324
S32K358
S32K348
S32K328
S32K338
S32K388
S32K389
Thermal resistance, Junction 
to Ambient (Natural 
Convection)1
Four-layer 
board (2s2p)2
RϴJA
48-LQFP
45
NA
NA
NA
NA
NA
NA
°C/W
100-HDQFP
35.3
38
33.8
NA
NA
NA
NA
°C/W
172-HDQFP
NA
30.5
29.6
28.9
NA
NA
NA
°C/W
257-MAPBGA
NA
NA
NA
26.8
NA
NA
NA
°C/W
172 HDQFP_EP
NA
NA
NA
NA
15.6
NA
NA
°C/W
289-MAPBGA
NA
NA
NA
NA
20.9
20.4
NA
°C/W
437-BGA
NA
NA
NA
NA
NA
NA
TBD
°C/W
Thermal characterization 
parameter, Junction-to-Top of 
package1
Natural 
Convection
ΨJT
48-LQFP
2
NA
NA
NA
NA
NA
NA
°C/W
100-HDQFP
0.66
0.8
0.5
NA
NA
NA
NA
°C/W
172-HDQFP
NA
0.5
0.5
0.4
NA
NA
NA
°C/W
257-MAPBGA
NA
NA
NA
0.3
NA
NA
NA
°C/W
172 HDQFP_EP
NA
NA
NA
NA
0.3
NA
NA
°C/W
289-MAPBGA
NA
NA
NA
NA
0.4
0.4
NA
°C/W
437-BGA
NA
NA
NA
NA
NA
NA
TBD
°C/W
1. Determined in accordance to JEDEC JESD51-2A natural convection environment. Thermal resistance data in this report is solely for a thermal performance 
comparison of one package to another in a standardized specified environment. It is not meant to predict the performance of a package in an application-specific 
environment
2. Thermal test board meets JEDEC specification for this package (JESD51-9).
NXP Semiconductors
Thermal Attributes
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
131 / 152


---
# 페이지 132

15 Dimensions
15.1 Obtaining package dimensions
Package dimensions are provided in the package drawings. To find a package drawing, go to nxp.com and perform a keyword 
search for the drawing’s document number:
Package option
Document Number
48-pin LQFP
98ASH00962A
257-ball MAPBGA
98ASA01483D
172-pin HDQFP
98ASA01107D
100-pin HDQFP
98ASA01570D
172-pin HDQFP_EP
98ASA01667D
289-ball MAPBGA
98ASA01216D
437-BGA
TBD
16 Revision history
The following table lists the changes in this document.
Rev 10, July 2024
• Updated front matter, from "Upto 128K of flexible program" to "Upto 256KB of flexible program"
• In "Absolute Max Ratings" updated footnote from "…. the voltage in the respective I/O power domain (VDD_HV_A or 
VDD_HV_B) would increase …." to "…voltage in the respective I/O power domain (VDD_HV_A or VDD_HV_B) would 
increase and may cause damage to the MCU. It is recommended to.."
• In "S32K328" and "S32K348" block diagrams, updated the instances of FlexCAN to 8.
• Updated Part number nomenclature diagram.
• In "Power mode transition operating behavious", removed Fast Recovery from description of "tMODE_STDBYEXIT" for 
S32K388 and S32K389.
• Updated table. "HSE Firmware memory verification time examples".
• In "289BGA package decoupling cap pinout digram(S32K388)", added CBULK capacitor, to H8.
• In section "V15 regulator(SMPS option)", updated the footnote from "Only needed..." to "Highly Recommended..."
• Added CBULK_SMPS in fig "SMPS circuit"
• In "V11 regulator (NMOS ballast transistor control) electrical specifications", updated the Typ value of V11 to 1.14V.
• In Supply current added values for S32K388.
• In table. Run mode configuration options, updated footnote from EMAC to EMAC/GMAC
• In GPIO DC electrical specifications, updated spec "VHSYS_33" and added footnote " Hysteresis spec does not apply to 
fast pad"
• In PLL, for spec "FPLL_out" updated the Max value to 480 MHz.
Table continues on the next page...
NXP Semiconductors
Dimensions
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
132 / 152


---
# 페이지 133

Rev 10, July 2024
• In section "FXOSC":
— Updated the Max value of CLKIN_VIL_EXTAL_BYPASS and Min value of CLKIN_VIH_EXTAL_BYPASS and 
added new footnote "For bypass mode application, the EXTAL..."
— Added new note "To improve the FXOSC & PLL jitter performance in S32K388, the functionality of the pins 
(namely -PTG0, PTG2, PTG3, PTF30, PTE12, PTA2..." specifically for S32K388.
• In LPSPI :
— Added new spec "tV" and "tHO" specifically for S32K389
— Updated the desciption of tA to "MISO valid time after SS assertion" and its reference in figure.
• Added new table ""LPSPI1, LPSPI3 and LPSPI4 for S32K389.
• In uSDHC SDR and DDR electrical specifications sections, updated the footnote "Öutput timing valid for maximum 
external load CL= 25pF(includes PCB trace.…)"
• In section "V15 regulator (SMPS option) electrical specifications", added devices S32K388 and S32K389.
• In "FXOSC", added information "In single ended bypass mode, the XTAL pin can be left unconnected".
• Added CBULK capacitors for SMPS figures in Decoupling capacitor figures.
• In Table. "Thermal characteristics", added values for S32K388.
• Updated the attached Part Number sheet.
• Added information "See I/O parameters for GPIO electrical specifications" in LPSPI, JTAG, SWD and Debug Trace 
timing Specifications.
Rev 10_DraftA, March 2024
• Updated front matter as below :
— Added package : 437BGA
— Program flash memory to 12MB
— SRAM with ECC to 2304 KB
— HMI upto 320 GPIO Pins
— FlexCAN modules to 12
• Added block diagram for S32K389
• Added information for S32K389 device throught the data sheet.
Rev 9.1, March 2024
• In table "LPSPI5 and LPSPI0 20MHz combination for S32K388", updated the instances of LPSPI2 to LPSPI5.
• In "GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V)", updated conditions for "FMAX_33_F" mentioning it 
for specific devices.
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
133 / 152


---
# 페이지 134

Rev 9, January 2024
• In "features", updated "Up to 512 KB SRAM with ECC, includes 192 KB" to "Up to 1152 KB SRAM with ECC, includes 
384 KB".
• Updated "feature comparison".
• Updated the DMIPS values in the Table of Features to align with the footnotes.
• In Absolute Max Ratings :
— Updated footnote "When the input pad voltage levels are close to VDD_HV_A (respectively to VDD_HV_B)..." and 
referred to S32K3xx hardware design guidelines instead of AN.
— Updated footnotes "Absolute max ratings must be..." and "When the input pad voltage levels.."
— Added new footnote "If a positive injection current is present..." to spec "I_INJSUM_DC_ABS".
— Added "S32K388" in statement "The VDD_DCDC supply voltage is only present in certain devices.."
— Updated condition for V15 and V11 spec.
• In Voltage and current operating requirements :
— Updated footnote "When input pad voltage levels are close to VDD_HV_A..."
— Added new footnotes "Keeping the input voltage between" and "If a positive injection current is present..."
— Added "S32K388" in statement "The VDD_DCDC supply voltage is only present in certain devices.."
— Updated condition for V15 and V11 spec.
• In "Power mode transition operating behaviour", added values for S32K3x8 devices.
• In "Supply Monitoring", added footnote "The HVD_V15 monitor is provided to indicate if the V15 rail is far above the standard 
V15 operating range...".
• In Recommneded Decoupling capacitors diagrams and SMPS Circuit updated "VDD_HV_SMPS" to "VDD_DCDC".
• In Table. "V15 regulator (SMPS option) electrical specifications" added symbol "L_SMPS" for External coil inductance and 
"D_SMPS" for External Schottky diode average forward current.
• Added IBCTL label in "Ballast circuit" figure.
• In "V11 regulator (NMOS ballast transistor control) electrical specifications" added new spec "VTH_NMOS" for 5.0 V supply 
and updated Max value to "1.5" for VTH spec for 3.3 V supply.
• In "Supply currents" section , added values for "S32K358, S32K348, S32K338, S32K328".
• In RUN mode supply currents (peripherals disabled) for S32K3x8, deleted values from "
Min. Config. [Clock Option A+] Triple Core @240 MHz " for S32K358, S32K348, S32K338, S32K328 variants.
• In GPIO DC electrical specifications:-
— Updated footnote "I/O timing specifications are valid for the un-terminated 50ohm..." and figure related to it with correct 
load details.
— Updated the conditions for FMAX specs.
• In "GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V)", added spec "FMAX_33_F" with max frequency 
125 MHz.
• In GPIO Output AC electrical specifications, updated spec values and added new footnotes and figure.
• In "GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V)" and "GPIO DC electrical specifications, 5.0V (4.5V - 
5.5V)", updated the max and min values of ILKG parameters.
Table continues on the next page...
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
134 / 152


---
# 페이지 135

Rev 9, January 2024
• Updated table "FIRC" mentioning FACC +/-5% for all K3xx devices.
• Updating figure title to "S32K310: ASIL B Single Core 512 KB General Purpose MCU".
• In "FXOSC":
— Added note "To improve the FXOSC & PLL jitter performance..."
— Updated the footnote "To improve the FXOSC jitter & duty cycle performance.."
• In "PLL", updated min value for "FPLL_out" from 48 to 25 MHz.
• In LPSPI, updated the output loads.
• In "LPSPI2 and LPSPI5 20MHz combination for S32K388", added new table "LPSPI2 and LPSPI0 20MHz combination 
for S32K388".
• In "LPSPI"
— Updating min values of tLEAD/tLAG to ""tSPCK/2" for LPSPI Slave mode.
— For "tWPSCK", removed "high or low" from description.
— Updated information "All measurements are with maximum output load of 30pf.." at the top of the table.
— Removed Rise/Fall time output specs.
— Added footnotes "Output rise/fall time is determined by the output load and GPIO pad drive strength setting..." and 
"The input rise/fall time specification applies to both clock and data..."
— Added "tV" and "tHO" spec with condition "Master Loopback, S32K388 LPSPI2 and LPSPI5 @20MHz"
— For "tV" with max value "17.5" ns, updated condition to ""Master Loopback, applies to all devices LPSPI0 @20 MHz"
— For "tHO" with min value "-2" ns, updated condition to ""Master Loopback, applies to all devices LPSPI0 @20 MHz"
— Updated LPSPI timing diagrams with 50/50 levels.
• In "LPSPI" and "Timing specification for S32K388 to S32K388", updated information from "All timing is shown 
with respect to 20% VDD_HV_A/B and 80% VDD_HV_A/B thresholds" to "All timing is shown with respect to 50% 
VDD_HV_A/B thresholds."
• Added information "Valid pin combinations to be referred from K3xx*_Use sheet in IOmux." in all SAI, uSHDC, QSPI and 
Ethernet modes.
• Added information "Data transitions measured at 30%/70% supply for the write path. Data transitions measured at 
mid-supply for the read path. Clock transitions measured at mid-supply." in all QSPI modes.
• Changed footer to "Preliminary Information for S32K388"
• Updated Preliminary Information for S32K388 throughout the data sheet.
• In "HSE Firmware memory verification time examples" table, there are some TBC's. Those will be updated in the next 
revision as new measurements showed different timings. There is no major performance degradation to be expected.
• Added information in section "LPSPI 20 MHz and 15MHz combinations", and removed S32K344 PAD TYPE column from 
Table. "LPSPI 20 MHz and 15MHz combinations".
• Added new section "LPSPI2 and LPSPI5 20MHz combination for S32K388".
• In "Timing specification for S32K388 to S32K388", updated maximum output load from 30pF to 50pF.
• In "Ethernet RGMII", updated footnote to "Output timing valid for maximum external load CL = 13.5 pF (includes PCB trace, 
package trace (around 2pF) and flash input load)...."
Table continues on the next page...
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
135 / 152


---
# 페이지 136

Rev 9, January 2024
• In "QuadSPI Octal 3.3V DDR 120MHz", for spec "fSCK_DQS", updated condition from "DLL and Auto-Learning mode 
enabled" to "DLL enabled"
• In section "uSDHC SDR electrical specifications":
— Updated description for "fpp" spec.
— Updated condition for "tOD" with description "SDHC Output delay(Output valid)"
— Added 2 rows of spec "tOD" with value "-5.6" and description ""fpp= 25 MHz, 400 KHz,..." and "fpp= 50 MHz, SDHC_ 
CLK to SDHC_CMD".
— Updated min value for spec "tIH" to 2 ns.
— Removed footnote " In low speed mode, card clock must be lower than 400 kHz, voltage ranges from 2.7V to 3.6V."
• In '"uSDHC" modes :
— Added information "Data transitions measured at 25%/62.5% at 3.3V for the write path. Data transitions measured at 
mid-supply for the read path. Clock transitions measured at mid-supply."
— Removed footnote "Input timing assumes an input signal slew rate of 3ns (20%/80%)" from "uSDHC SDR electrical 
specifications" and "uSDHC DDR electrical specifications" table. Added input transition of 1ns (20%/80%) information 
to top of the table.
• In section "uSDHC DDR electrical specifications", removed spec "fpp" with description "Clock frequency (SD3.0 DDR)".
• In uSDHC SDR and uSDHC DDR electrical specifications updated footnote to "Output timing valid for maximum external 
load CL = 25 pF..."
Rev 8.1, November 2023
• Updated "supply currents" for "S32K344, S32K324, S32K314, S32K342, S32K322, S32K341 and S32K312".
Rev 8, Jun 2023
• Moved S32K311 and S32K310 to support list from preliminary and added S32K322 to supported list.
• Updated frequency to 320 MHz for S32K388 mentioned in features and updated S32K388 block diagram.
• In section "Thermal operating characteristics" added ambient temperature seperately for both V- and M-grade parts.
• Deleted power management figures. See reference manual for these figures.
• Decoupling capacitors are updated with new formats.
• In section "V15 regulator (SMPS option) electrical specifications" updated the SMPS circuit figure.
• In section "V11 regulator (NMOS ballast transistor control) electrical specifications" updated V11 output from 1.14 to 
1.155 V.
• In section "Supply currents" added current numbers for S32K311 and S32K310 and added support for 320MHz for 
S32K388.
• In section "Supply currents" merged VDD_HV_A for S32K3x8, S32K34x, S32K32x and S32K314 and mentioned the 
max current.
• Added table title to table in section "Cyclic wake-up current".
• In section "Low Power Comparator (LPCMP)",
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
136 / 152


---
# 페이지 137

Rev 8, Jun 2023
— for symbol tDDAC updated description from "DAC Initialization and switching settling time" to "DAC Initialization 
time".
— updated footnote attached to TDHSS and TDLSS from "Applied +/- (30 mV + 2 x VAHYST0/1/2/3 + max. of VAIO) 
around switch point" to "Applied +/- (30 mV + VAHYST0/1/2/3 + max. of VAIO) around switch point"
• In section "Temperature Sensor" clarified that its an MCU on-die temperature sensor.
• In section "FIRC" updated FACC for S32K311 and S32K310 for different temperature ranges.
• In section "PLL", added sentence "Jitter values specified in this table are applicable for FXOSC reference clock input 
only".
• In section "Fast External Oscillator (FXOSC)", added IFXOSC for ALC disabled.
• In section "Slow Crystal Oscillator (SXOSC)" updated ISXOSC max from 4 to 10 uA.
• In section " LPSPI" updated symbols of Data hold time (inputs) to tHI.
• Updated heading of Ethernet MII and RMII to mention support of 10 and 100 Mbps.
• In "uSDHC SDR electrical specifications" updated conditions for the supported pads.
• In "uSDHC DDR electrical specifications" updated conditions for the supported pads and deleted 25 MHz specifications.
• Updated RϴJA for 172HDQFP_EP to 15.6 °C/W.
Rev 7, Apr 2023
• Updated caution in overview and updated feature comparison.
• In "S32K3xx chip's feature comparison" section clarified via footnote that S32K388 supports QuadSPI SDR modes only.
• Updated S32K312 and S32K388 block diagram.
• QFP package references updated to HDQFP.
• In section "Absolute maximum ratings" added footnote to VDD_DCDC as "Voltage at VDD_DCDC cannot be higher than 
VDD_HV_A".
• In section "Voltage and current operating requirements" added footnote to V15 as "Min and Max values are applicable 
only for non-SMPS mode where V15 is sourced externally".
• Updated descriptions and condition in following sections:
— Boot time, HSE firmware not installed
— Boot time, HSE firmware installed
— HSE firmware memory verification time examples
• In section "Recommended Decoupling Capacitors" updated variants for COUT V11.
• In section "V15 regulator (SMPS option) electrical specifications" added CBULK_SMPS.
• In section "V15 regulator (BJT option, NPN ballast transistor control) electrical specifications" added V15 input.
• In section "SAR ADC" updated paragraph "All below specs are applicable...". and added footnote to TUE as "Spec valid 
if potential difference between VDD_HV_A.." and figure updated to show VDD_HV_A instead of VREFH.
• In LPCMP section changed ACMP0 to LPCMP0.
• In PLL added paragraph to mention Auxiliary PLL applicability and footnote updated to mention "Accumulated jitter 
specification is not valid with SSCG".
• In PLL added CLKIN_VIL_EXTAL_BYPASS and CLKIN_VIH_EXTAL_BYPASS specifications.
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
137 / 152


---
# 페이지 138

Rev 7, Apr 2023
• Added section "Communication between two S32K388 devices".
• In section "Ethernet MII (100 Mbps)" updated specification for 10 and 100 Mbps.
• In section "Ethernet RGMII" added paragraph "The following timing specs are defined at the device".
• In section "MDIO timing specifications" updated MDC3 for GPIO[113]pad of S32K388.
• Added following QuadSPI modes for S32K388:
— QuadSPI Quad 3.3V SDR 103.33MHz
— QuadSPI Quad 3.3V SDR 125MHz
• In QuadSPI modes, mentioned the applicability to the devices in K3 family.
• In "Debug trace timing specifications" section added row for 125 MHz for S32K388.
• Updated "Thermal characteristics" to add information on Thermal design and characteristics.
Rev 6, Nov 2022
• Added S32K388 decoupling capacitor diagrams.
• In section "Power mode transition operating behavior" tMODE_STDBYEXIT time is added as 80 us.
• In "V15 regulator (SMPS option) electrical specifications" section changed V15 output supply from 1.51V to 1.5V.
• In "5.0V (4.5V - 5.5V) GPIO Output AC Specification"
— TR_TF_50_F with condition DSE=1, SRE=0, Capacitance=25pF changed from 0.9 to 1.9 ns.
— TR_TF_50_F with condition DSE=0, SRE=0, Capacitance=50pF changed from 5.3 to 6.0 ns.
— TR_TF_50_F with condition DSE=0, SRE=1, Capacitance=50pF changed from 7.7 to 9.0 ns.
— TR_TF_50_F with condition DSE=1, SRE=1, Capacitance=50pF changed from 5.1 to 6.5 ns.
• In "3.3V (2.97V - 3.63V) GPIO Output AC Specification"
— TR_TF_33_F with condition DSE=0, SRE=0, Capacitance=25pF changed from 4 to 4.5 ns.
— TR_TF_33_F with condition DSE=1, SRE=0, Capacitance=25pF changed from 2 to 2.5 ns.
— TR_TF_33_F with condition DSE=0, SRE=0, Capacitance=50pF changed from 7 to 8 ns.
• In section "Fast External Oscillator (FXOSC)" added EXTAL_SWING_PP and VSB specs and related footnote.
Rev 5.2, Oct 2022
• Added S32K310 and S32K388 where applicable.
• Updated "overview".
• In "features":
— Updated M7 support upto 300 MHz.
— Updated Ethernet instance from one to two.
— Added Support to AES accelerator(for K388 only)
— Removed I3C instances.
• Added S32K310 and S32K388 block diagram and updated others to remove I3C.
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
138 / 152


---
# 페이지 139

Rev 5.2, Oct 2022
• Updated "Feature comparison".
• Updated "Ordering information".
• In "Absolute maximum ratings":
— Added symbol "V15" as "Voltage sensing input" for S32K388 and changed max value to 2.75V for S32K358.
— Added symbol "V11" for S32K388.
• In "Voltage and current operating requirements":
— Added symbol "V15" as "Voltage sensing input" for S32K388 and updated conditions for V15 and V15_extended. 
Also added a footnote to V15_extended as You must ensure that the junction temperature"...".
— Added symbol "V11" for S32K388.
— Updated link to download hardware design guidelines document.
• In section "Thermal operating characteristics" added sentence as "For S32K388, applications running at 125°C 
Tamb.....".
• Added S32K388 power management diagram and added other variants to diagrams as applicable.
• In section "Power mode transition operating behavior, added condition for tMODE_STDBYEXIT_FAST as "FIRC ON 
@48MHz in Standby mode".
• In section "Supply monitoring" added sentence as "Certain monitors are present on certain...".
• In section "Recommended Decoupling Capacitors" added COUT_V11 for S32K388 and updated decoupling capacitor 
diagrams.
• Section "SMPS regulator electrical specifications" changed to "V15 regulator (SMPS option) electrical specifications" and 
following changes done:
— Added paragraphs at the begining of table as:
◦"Some devices (S32K358, S32K348, S32K338, and S32K328)...."
◦"The table below describes the electrical parameters for the components needed to implement an SMPS...."
◦Updated existing to include inductor "The chip hardware design guidelines document lists the 
recommended...".
◦Added figure, removed redundant sentence "The table below describes the electrical parameters.." and 
updated part numbers.
— Added "External Schottky diode average forward current" as 2A.
— Added "External P-channel MOSFET threshold voltage" as 2V.
• Section "NPN Ballast Transistor Control Specification" renamed to "V15 regulator (BJT option, NPN ballast transistor 
control) electrical specifications" and updated the following:
— added paragraph "Some devices (S32K358, S32K348, S32K338, S32K328, S32K344, S32K324, S32K314, 
S32K342, S32K322, S32K341) support ...."
— Updated ballast circuit figure.
• Added section "V11 regulator (NMOS ballast transistor control) electrical specifications".
• In section "Supply currents":
— added template for S32K388.
— added values for S32K342.
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
139 / 152


---
# 페이지 140

Rev 5.2, Oct 2022
— added S32K310 along with S32K311.
• GMAC term is added along with EMAC in "Operating mode" section.
• Updated GPIO specs to clarify leakage specifications.
• In SAR ADC section, removed TBD from RS max specification.
• In section "SXOSC", Oscillator Analog circuit supply current max updated to 4 uA.
• In section "LPSPI", updated tV and tHO for S32K358 and a note is added as "15 and 20 Mbps is supported on LPSPI0 
only.".
• In section "uSDHC SDR electrical specifications" relaxed tISU for 25 MHz and 400 KHz from 4.8 to 6.3 ns.
• Deleted I3C specifications
• Updated "Thermal characteristics"
• Added 48-pin LQFP package drawing number in "Obtaining package dimensions" section.
• Editorial updates.
Rev 4, April 2022
• Removed S32K312 from preliminary list from the title of the document and "Overview".
• In features on first page added MAPBGA289 to the package list and updated GPIO pins upto 235.
• Removed "NDA required" term from all block diagrams.
• In "Ordering information", added HDQFP-EP package suffix.
• In section "Absolute maximum ratings", and "Voltage and current operating requirements", added S32K341 variant to 
the sentence "The VDD_HV_B and V15 voltage supply domains are only present....".
• In section “Voltage and current operation requirement”, the footnote attached to supply ramp rate is updated as “ The 
MCU Supply ramp applicable to the MCU input/external supplies...".
• Updated capacitor symbol to non-polarity in following figures at V25 and V11:
— Power management system - S32K344, S32K324, S32K341, S32K314, S32K342, and S32K322.
— Power management system - S32K312, S32K311
• In "Power management system - S32K358" figure, updated connections to optional circuit with dashed lines for 
PGATE_CTRL and VSS_DCDC.
• In section “SMPS regulator electrical specifications”, added a sentence “The chip hardware design guidelines 
documents lists the recommended part numbers of PMOS & Schottky diode."
• In table "SMPS regulator electrical specifications" :
— The typ. value of "External coil inductance" changed from 5 to 4.7uH.
— Added “Schottky diode reverse voltage” with Min value 5.0 V.
— Added “Schottky diode forward current” with Min value 1.0 A.
• In section "SMPS regulator electrical specifications" changed "COUT_V15" to "COUT_V15_SMPS" to match it with 
corresponding figure.
• In section "Recommended Decoupling Capacitors" changed "COUT_V15" to "COUT_V15_NPN" to match it with 
corresponding figure.
• In section "Recommended Decoupling Capacitors", following footnotes updated:
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
140 / 152


---
# 페이지 141

Rev 4, April 2022
— Footnote attached to CDEC "Optionally, 1 nF capacitors can be added...".
— Footnote attached to CBULK "For devices where the VDD_HV_B domain is present, if the VDD_HV_B...".
— Added footnote to CBULK "These capacitors must be placed close to the source."
• In section "Recommended Decoupling Capacitors", updated and added decoupling capacitors diagrams.
• In section "NPN Ballast Transistor Control Specification" added specification for VDD_HV_NPN.
• Updated "Ballast circuit" figure under section " NPN Ballast Transistor Control Specification".
• Current IDD specs are updated for S32K12 for following :
— Table “STANDBY mode supply currents”
— Table “Low speed RUN mode supply currents”
— Table “RUN mode supply currents (peripherals disabled)”
— Table “Example RUN mode configuration supply current”
• In section “supply current”, Removed table “Recommended current limits in board design” and related sentence “The 
power supplies for the voltage ...."
• In section “Power management”, added section ”Cyclic wake-up current” and removed table "Low-power, cyclic 
operation mode" from supply currents.
• In section "GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V)",with symbol "ILKG_33_S", the condition has 
been changed from PTC0 to PTD0.
• In section "5.0V (4.5V - 5.5V) GPIO Output AC Specification":
— for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=1, Capacitance=50pF" Min changed from "2.8" to "1.9".
— for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=1, Capacitance=50pF" Max changed from "10.2" to "7.7".
— for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=1, Capacitance=50pF" Min changed from "1.9" to "1.3".
— for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=1, Capacitance=50pF" Max changed from "6.7" to "5.1".
— for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=0, Capacitance=50pF" Min changed from "2.0" to "1.0".
— for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=0, Capacitance=50pF" Max changed from "7.4" to "5.3".
— for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=0, Capacitance=25pF" Min changed from "0.9" to "0.3".
— for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=0, Capacitance=25pF" Max changed from "3.0" to "0.9".
— for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=1, Capacitance=25pF" Min changed from "1.3" to "0.9".
— for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=1, Capacitance=25pF" Max changed from "5.1" to "4.1".
— for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=0, Capacitance=50pF" Min changed from "1.6" to "0.9".
— for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=0, Capacitance=50pF" Max changed from "3.6" to "3.0".
— for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=0, Capacitance=25pF" Min changed from "1.0" to "0.4".
— for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=0, Capacitance=25pF" Max changed from "5.3" to "3.1".
— for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=1, Capacitance=25pF" Min changed from "1.9" to "1.5".
— for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=1, Capacitance=25pF" Max changed from "7.7" to "6.1".
• In section “SAR ADC“, the footnote attached to “ADC Total Unadjusted Error” is updated as “TUE spec for precision and 
standard channels is based on 12-bit level resolution”.
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
141 / 152


---
# 페이지 142

Rev 4, April 2022
• In section "Supply Diagnosis", for Symbol "AN_ACC" and "AN_T_on" footnote added "These specs will have degraded 
performan..."
• In section "Fast External Oscillator (FXOSC)", for Symbol "TFXOSC" description changed from "Fxosc start up time" to 
"Fxosc start up time (ALC enabled)".
• In section "Fast External Oscillator (FXOSC)", removed the crystal part numbers and related information which includes 
following sentences, "In crystal mode NX5032GA crystal .....", " In crystal mode NX8045GB crystal …" and updated 
sentence "To ensure stable oscillations, FXOSC incorporates the feedback resistance internally.".
• In section "LPSPI", updated the sentence updated maximum output load of 50pF to 30pF.
• In section "LPSPI", footnote attached to "fperiph" is udated to mention clock name instead of frequency. "For LPSPI0 
instance, max. peripheral...".
• In section "I3C Push-Pull Timing Parameters for SDR Mode", Symbol "tV" and tHI are deleted.
• Added section "Ethernet RGMII".
• In all QuadSPI modes updated trace length from 3 inches to 2 inches.
• Added "QuadSPI Octal 3.3V DDR 100MHz" mode.
• Deleted "QuadSPI Quad 3.3V DDR 80MHz" mode.
• In section "QuadSPI Octal 3.3V DDR 120MHz" :
— For symbol “tOD_DATA”, Max. value changed from “2.567” to “ 2.934”.
— For symbol “tOD_CS”, Min value has been changed from “3.015” to “3.016” and Max. value changed from “-1.33” 
to “-0.766”.
— For symbol “tDVW”, Min value has been changed from “2.314” to “2.518”.
— For symbol “tIH_DQS”, Min value has been changed from “2.767” to “3.134”.
• uSDHC specifications are updated thoroughly.
• In "Thermal characteristics":
— Updated table header to include all variants.
— For S32K312 100-HDQFP updated RϴJA from 34.8 to 38 °C/W and RϴJT from 0.6 to 0.8 °C/W.
— For S32K3x4, 257MAPBGA updated RϴJA from 27 to 26.8 °C/W.
• Updated Legal information.
Rev 3, Oct 2021
• Datasheet classification is updated to "Technical data" for S32K344.
• In section "Supply currents" added values for 85C (typ and max) and updated 105 (max) and 125 (max) values for 
S32K344.
• In front page features, added HDQFP172 with Exposed pad (EP) option and information on I3C.
• In section "Overview", added a note "S32K3x1, S32K3x2 and S32K3x8 specific information ....".
• In "Feature comparision" section added footnote to add information about HDQFP172 with Exposed pad (EP) package 
for S32K3x8 devices.
• VDD_HV_SMPS is changed to VDD_DCDC throughout.
• In section "Absolute maximum ratings", footnote attached to "I_INJSUM_DC_ABS" is exteded to add information "See 
application note AN4731 for...".
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
142 / 152


---
# 페이지 143

Rev 3, Oct 2021
• Figure "Power management system - S32K344, S32K324, S32K341, S32K314, S32K342, and S32K322." is updated to 
add COUT_V15 capacitor.
• Figure "Power management system - S32K358" is updated to add COUT_V15 capacitor and optional circuit explained in 
the notes.
• In section "SMPS regulator electrical specifications", COUT_V15 is added to "External bypass capacitor".
• Figure "Package decoupling capacitor pinout diagram" is updated to show HDQFP172-EP package.
• Table title "Current limit requirements for board design" is changed to "Recommended current limits in board design" and 
added a note as "The power supplies for the voltage rails must be...".
• In section "GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V)":
— for ILKG_33_S updated condition to update pins which has Analog Function Count=2/3
— for ILKG_33_M updated condition to update pins which has Analog Function Count=1
— added ILKG_33_M with condition "PTE8 and PTD6"
— udpdated ILKG_33, -120 nA (min) and 120 nA (max).
— updated condition of IOH_*, IOL_* to add < and > symbols.
— added IOHT specification.
— Updated sentence "I/O current specifications are...". and removed "RMS current values are given....".
• In section "GPIO DC electrical specifications, 5.0V (4.5V - 5.5V)":
— for ILKG_50_S updated condition to update pins which has Analog Function Count=2/3
— for ILKG_50_M updated condition to update pins which has Analog Function Count=1
— added ILKG_50_M with condition "PTE8 and PTD6"
— udpdated ILKG_50, -150 nA (min) and 150 nA (max).
— updated condition of IOH_*, IOL_* to add < and > symbols.
— added IOHT specification.
— Updated sentence "I/O current specifications are...". and removed "RMS current values are given....".
• In section "5.0V (4.5V - 5.5V) GPIO Output AC Specification":
— for Symbol "TR_TF_50_S" with condition "Capacitance=25pF" Min changed from "TBD" to "5"
— for Symbol "TR_TF_50_S" with condition "Capacitance=25pF" Max changed from "TBD" to "21"
— for Symbol "TR_TF_50_S" with condition "Capacitance=50pF" Min changed from "TBD" to "10"
— for Symbol "TR_TF_50_S" with condition "Capacitance=50pF" Max changed from "TBD" to "31"
— for Symbol "TR_TF_50_SP" with condition "DSE=0, Capacitance=25pF" Min changed from "5" to "3.5"
— for Symbol "TR_TF_50_SP" with condition "DSE=1, Capacitance=25pF" Min changed from "2.4" to "1.2"
— for Symbol "TR_TF_50_SP" with condition "DSE=0, Capacitance=50pF" Min changed from "8.9" to "7.1"
— for Symbol "TR_TF_50_SP" with condition "DSE=1, Capacitance=50pF" Min changed from "4.1" to "3.4"
— for Symbol "TR_TF_50_M" with condition "DSE=0, SRE=0, Capacitance=25pF" Min changed from "2.5" to "1.8"
— for Symbol "TR_TF_50_M" with condition "DSE=0, SRE=1, Capacitance=25pF" Min changed from "3" to "2.5"
— for Symbol "TR_TF_50_M" with condition "DSE=1, SRE=0, Capacitance=25pF" Min changed from "1" to "0.8"
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
143 / 152


---
# 페이지 144

Rev 3, Oct 2021
— for Symbol "TR_TF_50_F" with condition "DSE=0, SRE=0, Capacitance=25pF" Max changed from "4.3" to "5.3"
— for Symbol "TR_TF_50_F" with condition "DSE=1, SRE=0, Capacitance=25pF" Max changed from "1.6" to "3.0"
• In section "3.3V (2.97V - 3.63V) GPIO Output AC Specification":
— for Symbol "TR_TF_33_S" with condition "Capacitance=25pF" Min changed from "TBD" to "6.5"
— for Symbol "TR_TF_33_S" with condition "Capacitance=25pF" Max changed from "TBD" to "28"
— for Symbol "TR_TF_33_S" with condition "Capacitance=50pF" Min changed from "TBD" to "11"
— for Symbol "TR_TF_33_S" with condition "Capacitance=50pF" Max changed from "TBD" to "43"
— for Symbol "TR_TF_33_SP" with condition "DSE=0, Capacitance=25pF" Min changed from "5" to "4"
— for Symbol "TR_TF_33_SP" with condition "DSE=1, Capacitance=25pF" Min changed from "2.4" to "2.0"
— for Symbol "TR_TF_33_M" with condition "DSE=0, SRE=0, Capacitance=25pF" Min changed from "3.2" to "2.2"
— for Symbol "TR_TF_33_M" with condition "DSE=0, SRE=1, Capacitance=25pF" Min changed from "3.8" to "3.0"
— for Symbol "TR_TF_33_M" with condition "DSE=1, SRE=0, Capacitance=25pF" Min changed from "1" to "0.8"
— for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=0, Capacitance=25pF" Min changed from "1.1" to "0.5"
— for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=0, Capacitance=25pF" Max changed from "7.0" to "4"
— for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=1, Capacitance=25pF" Min changed from "2.6" to "2.1"
— for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=1, Capacitance=25pF" Max changed from "11.0" to "9"
— for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=0, Capacitance=25pF" Min changed from "0.8" to "0.4"
— for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=0, Capacitance=25pF" Max changed from "3.4" to "2"
— for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=1, Capacitance=25pF" Min changed from "1.5" to "1.2"
— for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=1, Capacitance=25pF" Max changed from "7.8" to "6.4"
— for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=0, Capacitance=50pF" Min changed from "2.5" to "1.1"
— for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=0, Capacitance=50pF" Max changed from "10.8" to "7"
— for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=1, Capacitance=50pF" Min changed from "3.6" to "2.6"
— for Symbol "TR_TF_33_F" with condition "DSE=0, SRE=1, Capacitance=50pF" Max changed from "15.0" to "11"
— for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=0, Capacitance=50pF" Min changed from "1.5" to "0.8"
— for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=0, Capacitance=50pF" Max changed from "5.5" to "4.2"
— for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=1, Capacitance=50pF" Min changed from "2.2" to "1.5"
— for Symbol "TR_TF_33_F" with condition "DSE=1, SRE=1, Capacitance=50pF" Max changed from "10.0" to "7.8"
• In section "SAR ADC", added paragraph "All below specs are applicable when only one ADC instance is in operation ..... 
to determine the most appropriate settings for AVGS." and removed footnote from RS specification.
• In section "SAR ADC", added specifications for CP1, CP2 and RSW1 corresponding to all channels, shared channels 
and precision channels. Also added the related figure.
• In section "PLL", removed some non-applicable footnotes.
• In section "LPSPI", added information before the table The Low Power Serial Peripheral Interface (LPSPI) provides a 
synchronous serial bus with master....".
• In section "LPSPI0 20 MHz and 15 MHz Combinations", added note as "Trace length should not exceed 11 inches for 
SCK pad when used in Master loopback mode."
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
144 / 152


---
# 페이지 145

Rev 3, Oct 2021
• Added "I3C" specifications.
• In section "Ethernet MII (100 Mbps)", for "RXCLK frequency" typ value moved to max.
• In section "Ethernet RMII", added paragraph "The following timing specs are defined at the device I/O pin and must 
be .....I/O operating voltage ranges from 2.97 V to 3.63 V."
• In section "QuadSPI Quad 3.3V SDR 120MHz", for Symbol "tSDC" footnote added "For S32K342 100MQFP, tSDC spec 
would be ..."
• In section "QuadSPI Quad 3.3V SDR 120MHz" added sentence "Program register value 
QuadSPI_DLLCRA[SLV_FINE_OFFSET] to 4'b0001.".
• In section "QuadSPI Octal 3.3V DDR 120MHz", Symbol "tSCK" min is calrified, condition updated to External DQS and 
"tSCK" with condition Internal Loopback is deleted.
• In section "QuadSPI Octal 3.3V DDR 120MHz", Symbol "tSDC" condition updated to External DQS and "tSDC" with 
condition Internal Loopback is deleted..
• In section "QuadSPI Octal 3.3V DDR 120MHz", specifications tISU_PCS, tIH_PCS, tCK2CKmin and tCK2CKmax are 
deleted.
Rev 2, Aug 2021
• Added section "Overview".
• In block diagrams:
— S32K311/S32K312/S32K314 removed "Scalable ARM M7 core in Lock step" and added "Single ARM M7 core".
— S32K322/S32K324 removed "Scalable ARM M7 core in Lock step" and added "Two independent ARM M7 cores".
• In "Absolute maximum ratings" and "Voltage and current operating requirements":
— Some general footnotes are moved to top of table
— VDD_HV_SMPS added footnotes
• In "Voltage and current operating requirements" for VREFH extended footnote "VREFH should always be equal to...".
• Updated title - Power management system - S32K344, S32K324, S32K341, S32K314, S32K342, and S32K322.
• In figure "Power management system - S32K358" updated double bond to triple bond.
• In section "Recommended Decoupling Capacitors" added COUT_V11 with typ as 1 uF.
• Added section "Power mode transition operating behaviors" and its subsections:
— Power mode transition operating behaviour
— Boot time, HSE firmware not installed
— Boot time, HSE firmware installed
— HSE firmware memory verification time examples
• Moved information from "Supply monitoring" to "Supply diagnosos" and attached it to "AN_ACC". The information is "If 
V15 > VDD_HV_A +100mV then..."
• Updated figure "Package decoupling capacitor pinout diagram" to add 289 MapBGA
• In section "Glitch Filter", added sentence ".... WKPU pins and TRGMUX inputs 60-63.".
• Section "Flash memory program and erase specifications" updated thoroughly.
• In section "Flash memory module life specifications" removed footnotes 1 and 2.
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
145 / 152


---
# 페이지 146

Rev 2, Aug 2021
• In section "Data retention vs program/erase cycles" added sentence before related to figure "The spec window 
represents qualified limits.".
• In section "Flash memory AC timing specifications":
— Updated register naming representation
— Added footnote to tdrcv min as " In extreme cases (1 block configurations)...".
— Max updated to "50 system clock periods" for taistop
• Ins ection "Flash memory read timing parameters" mantioned part numbers for each table as applicable.
• >In section "SAR ADC", for Symbol "fAD_CK" added new spec and max updated to 120.
• In section "FIRC", Symbol "IFIRC" is deleted.
• In section "SIRC", Symbol "Ivdda" with condition "On state" is deleted.
• In section "PLL", clarification added in condition column for jitter specifications.
• In section "Fast External Oscillator (FXOSC)", for Symbol "FREQ_BYPASS", "TRF_BYPASS" and 
"CLKIN_DUTY_BYPASS" footnote added "For bypass mode applications, the EXTAL ...".
• In section "Fast External Oscillator (FXOSC)", for Symbol "TFXOSC" footnote added "The startup time specification is 
valid ...".
• In section "Fast External Oscillator (FXOSC)", Symbol "IFXOSC" specs are merged into one and description and 
condition updated.
• In section "Fast External Oscillator (FXOSC)", added paragraph "Drive level is a crystal specification and ....".
• In section "LPSPI", Symbol "tSPSCK" with condition "Slave_10Mbps" is added.
• In section "LPSPI", Symbol "tSPSCK" with condition "Master_10Mbps" is added.
• Updated title to mention LPSPI0 of "LPSPI0 20 MHz and 15 MHz Combinations", and updated header "20Mbps" to 
"20Mbps (In loopback mode only)".
• In "I3C" section, added two sentences.
• Updated "QuadSPI" sections.
• Editorial updates.
Rev 2 Draft B, Mar 2021
• Updated "block diagrams" and "Feature comparison"
• Updated "Ordering information" to add 289 pagkage and removed one.
• In section "Absolute maximum ratings", Symbol "VDD_HV_SMPS" is added.
• In section "Absolute maximum ratings", for Symbol "I_INJPAD_DC_ABS" and "I_INJSUM_DC_ABS" footnote updated 
"When input pad voltage levels are close ...".
• In section "Voltage and current operating requirements", Symbol "IINJSUM_DC_OP" and "IINJPAD_DC_OP" condition is 
updated
• In section "Voltage and current operating requirements", Symbol "VDD_HV_SMPS" is added.
• In section "Voltage and current operating requirements", for Symbol "I_INJPAD_DC_ABS" and "I_INJSUM_DC_ABS" 
footnote updated "When input pad voltage levels are close ...".
• In section "Power management":
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
146 / 152


---
# 페이지 147

Rev 2 Draft B, Mar 2021
— "Power management system - S32K344, S32K324, S32K314" figure updated.
— "Power management system - S32K312, S32K311" figure updated.
— "Power management system - S32K358" figure added.
• In section "Supply Monitoring", Symbol "HVD_V15" is added.
• In section "Supply Monitoring", for "LVD_VDD_HV_A", symbol and description updated.
• Added section "SMPS regulator electrical specifications"
• In section "NPN Ballast Transistor Control Specification", fig with title "Ballast circuit" is changed.
• In section "Supply currents" and "operating mode" tables are updated.
• In section "GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V)", fig with title "Reference Load Diagram" is 
changed.
• In section "GPIO DC electrical specifications, 3.3V Range (2.97V - 3.63V)", footnote updated "A positive value is 
leakage flowing into...".
• In section "GPIO DC electrical specifications, 5.0V (4.5V - 5.5V)", Symbol "ILKG_50_S_PTE13" with condition "PMC 
VRC_CTRL pin" is added.
• In section "GPIO DC electrical specifications, 5.0V (4.5V - 5.5V)", footnote updated "A positive value is leakage flowing 
into...".
• In section "GPIO DC electrical specifications, 5.0V (4.5V - 5.5V)", fig with title "Reference Load Diagram" is changed.
• In section "Flash memory specification", added specs for 512KB and 2MB specifications.
• In table "Flash memory AC timing specifications", taistop max updated.
• Updated "Flash Read Wait State Settings"
• In section "Low Power Comparator (LPCMP)", updated IDLSS typ to 17uA.
• In section "Low Power Comparator (LPCMP)", updated INL and DNL.
• In section "Low Power Comparator (LPCMP)", updated paragraph "For devices where the VDD_HV_B domain is 
present..."
• In "Low Power Comparator (LPCMP)" added hysterisis plots.
• In section "PLL", symbol "FPLL_out" description updated to add (PLL_PHIn_CLK)
• In section "PLL", "IPLL_V25" deleted.
• In section "PLL", updated jitter specifications.
• In section "FXOSC", updated paragraph "To improve the FXOSC jitter and duty cycle performance...".
• In section "SXOSC", updated description of "ISXOSC" to Oscillator Analog circuit supply current.
• In section "I2C", added paragraph "For supported baud rate ....."
• Added section "I3C".
• In section "FlexCAN characteristics", added paragraph "For supported baud rate ....."
• Added QuadSPI DDR electrical specifications for Octal and Quad.
• Added uSDHC specifications.
• Updated "Thermal characteristics" and "Obtaining package dimensions"
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
147 / 152


---
# 페이지 148

Rev 2 Draft A, Nov 2020
• Updated features to show maximum memory support up to 8 MB.
• Added information for S32K341.
• Updated "Block diagrams".
• Updated "Feature comparision"
• Updated "Thermal characterstics" to add data for S32K312 and S32K342.
• Added document number for 172-pin HDQFP package in section "Obtaining package dimensions"
NXP Semiconductors
Revision history
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
148 / 152


---
# 페이지 149

Legal information
Data sheet status
Document status[1][2]
Product status[3]
Definition
Objective [short] data sheet
Development
This document contains data from the objective specification for product 
development.
Preliminary [short] data sheet
Qualification
This document contains data from the preliminary specification.
Product [short] data sheet
Production
This document contains the product specification.
[1]
Please consult the most recently issued document before initiating or completing a design.
[2]
The term 'short data sheet' is explained in section "Definitions".
[3]
The product status of device(s) described in this document may have changed since this document was published and may differ in case of multiple devices. 
The latest product status information is available on the Internet at URL https://www.nxp.com.
Definitions
Draft — A draft status on a document indicates that the content is still 
under internal review and subject to formal approval, which may result 
in modifications or additions. NXP Semiconductors does not give any 
representations or warranties as to the accuracy or completeness of 
information included in a draft version of a document and shall have no 
liability for the consequences of use of such information.
Short data sheet — A short data sheet is an extract from a full data sheet with 
the same product type number(s) and title. A short data sheet is intended for 
quick reference only and should not be relied upon to contain detailed and full 
information. For detailed and full information see the relevant full data sheet, 
which is available on request via the local NXP Semiconductors sales office. 
In case of any inconsistency or conflict with the short data sheet, the full data 
sheet shall prevail.
Product specification — The information and data provided in a Product data 
sheet shall define the specification of the product as agreed between NXP 
Semiconductors and its customer, unless NXP Semiconductors and customer 
have explicitly agreed otherwise in writing. In no event however, shall an 
agreement be valid in which the NXP Semiconductors product is deemed to 
offer functions and qualities beyond those described in the Product data sheet.
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
lost profits, lost savings, business interruption, costs related to the removal or 
replacement of any products or rework charges) whether or not such damages 
are based on tort (including negligence), warranty, breach of contract or any 
other legal theory.
Notwithstanding any damages that customer might incur for any reason 
whatsoever, NXP Semiconductors’ aggregate and cumulative liability towards 
customer for the products described herein shall be limited in accordance with 
the Terms and conditions of commercial sale of NXP Semiconductors.
Right to make changes — NXP Semiconductors reserves the right to make 
changes to information published in this document, including without limitation 
specifications and product descriptions, at any time and without notice. This 
document supersedes and replaces all information supplied prior to the 
publication hereof.
NXP Semiconductors
Legal information
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
149 / 152


---
# 페이지 150

Applications — Applications that are described herein for any of these 
products are for illustrative purposes only. NXP Semiconductors makes no 
representation or warranty that such applications will be suitable for the 
specified use without further testing or modification.
Customers are responsible for the design and operation of their applications 
and products using NXP Semiconductors products, and NXP Semiconductors 
accepts no liability for any assistance with applications or customer product 
design. It is customer’s sole responsibility to determine whether the NXP 
Semiconductors product is suitable and fit for the customer’s applications and 
products planned, as well as for the planned application and use of customer’s 
third party customer(s). Customers should provide appropriate design and 
operating safeguards to minimize the risks associated with their applications 
and products.
NXP Semiconductors does not accept any liability related to any default, 
damage, costs or problem which is based on any weakness or default in the 
customer’s applications or products, or the application or use by customer’s 
third party customer(s). Customer is responsible for doing all necessary testing 
for the customer’s applications and products using NXP Semiconductors 
products in order to avoid a default of the applications and the products or of the 
application or use by customer’s third party customer(s). NXP does not accept 
any liability in this respect.
Limiting values — Stress above one or more limiting values (as defined in 
the Absolute Maximum Ratings System of IEC 60134) will cause permanent 
damage to the device. Limiting values are stress ratings only and (proper) 
operation of the device at these or any other conditions above those 
given in the Recommended operating conditions section (if present) or the 
Characteristics sections of this document is not warranted. Constant or 
repeated exposure to limiting values will permanently and irreversibly affect the 
quality and reliability of the device.
Terms and conditions of commercial sale — NXP Semiconductors products 
are sold subject to the general terms and conditions of commercial sale, 
as published at https://www.nxp.com/profile/terms, unless otherwise agreed 
in a valid written individual agreement. In case an individual agreement 
is concluded only the terms and conditions of the respective agreement 
shall apply. NXP Semiconductors hereby expressly objects to applying the 
customer’s general terms and conditions with regard to the purchase of NXP 
Semiconductors products by customer.
No offer to sell or license — Nothing in this document may be interpreted or 
construed as an offer to sell products that is open for acceptance or the grant, 
conveyance or implication of any license under any copyrights, patents or other 
industrial or intellectual property rights.
Quick reference data — The Quick reference data is an extract of the product 
data given in the Limiting values and Characteristics sections of this document, 
and as such is not complete, exhaustive or legally binding.
Export control — This document as well as the item(s) described herein may be 
subject to export control regulations. Export might require a prior authorization 
from competent authorities.
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
Suitability for use in automotive applications (functional safety) — This NXP 
product has been qualified for use in automotive applications. It has been 
developed in accordance with ISO 26262, and has been ASIL classified 
accordingly. If this product is used by customer in the development of, or for 
incorporation into, products or services (a) used in safety critical applications 
or (b) in which failure could lead to death, personal injury, or severe physical 
or environmental damage (such products and services hereinafter referred to 
as “Critical Applications”), then customer makes the ultimate design decisions 
regarding its products and is solely responsible for compliance with all legal, 
regulatory, safety, and security related requirements concerning its products, 
regardless of any information or support that may be provided by NXP. As 
such, customer assumes all risk related to use of any products in Critical 
Applications and NXP and its suppliers shall not be liable for any such use by 
customer. Accordingly, customer will indemnify and hold NXP harmless from 
any claims, liabilities, damages and associated costs and expenses (including 
attorneys’ fees) that NXP may incur related to customer’s incorporation of any 
product in a Critical Application.
NXP B.V. — NXP B.V. is not an operating company and it does not distribute 
or sell products.
Trademarks
Notice: All referenced brands, product names, service names, and 
trademarks are the property of their respective owners.
NXP — wordmark and logo are trademarks of NXP B.V.
NXP Semiconductors
Legal information
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
150 / 152


---
# 페이지 151

AMBA, Arm, Arm7, Arm7TDMI, Arm9, Arm11, Artisan, big.LITTLE, Cordio, 
CoreLink, CoreSight, Cortex, DesignStart, DynamIQ, Jazelle, Keil, Mali, 
Mbed, Mbed Enabled, NEON, POP, RealView, SecurCore, Socrates, Thumb, 
TrustZone, ULINK, ULINK2, ULINK-ME, ULINK-PLUS, ULINKpro, μVision, 
Versatile — are trademarks and/or registered trademarks of Arm Limited (or its 
subsidiaries or affiliates) in the US and/or elsewhere. The related technology 
may be protected by any or all of patents, copyrights, designs and trade 
secrets. All rights reserved.
Bluetooth — the Bluetooth wordmark and logos are registered trademarks 
owned by Bluetooth SIG, Inc. and any use of such marks by NXP 
Semiconductors is under license.
EdgeLock — is a trademark of NXP B.V.
eIQ — is a trademark of NXP B.V.
I2C-bus — logo is a trademark of NXP B.V.
NXP SECURE CONNECTIONS FOR A SMARTER WORLD — is a trademark 
of NXP B.V.
SafeAssure — is a trademark of NXP B.V.
SafeAssure — logo is a trademark of NXP B.V.
SuperFlash — This product uses SuperFlash® technology. SuperFlash® is a 
registered trademark of Silicon Storage Technology, Inc.
Synopsys & Designware — are registered trademarks of Synopsys, Inc.
Synopsys — Portions Copyright © 2018-2022 Synopsys, Inc. Used with 
permission. All rights reserved.
NXP Semiconductors
Legal information
S32K3xx Data Sheet, Rev. 10, 07/2024
Data Sheet: Technical Data
Preliminary Information for S32K389
151 / 152


---
# 페이지 152

Please be aware that important notices concerning this document and the product(s) described 
herein, have been included in section 'Legal information'.
© NXP B.V. 2024.
All rights reserved.
For more information, please visit: https://www.nxp.com
Date of release: 07/2024
Document identifier: S32K3XX


---
