# 페이지 1

Chapter 82
Debug Subsystem
82.1 Introduction
This chapter discusses the debug and trace architecture of the chip that is based on the specifications provided in the Arm® 
CoreSight™ SoC-400 Technical Reference Manual. See References for a link to this document and to other related documentation 
available on the Arm website.
The chip architecture includes debug and trace modules. See Features for details on the debug and trace features that Cortex-M7 
core clusters support.
The debug components that the Cortex-M7 core supports are accessible via the Arm DAP controller-based architecture. The DAP 
controller works in parallel with the system JTAGC. Both these controllers share the JTAG port and JTAG instruction set.
The system components are similar for different chips in the same family and include the primary core debug interfaces, the 
chip-level debug interfaces, and chip-level trace interfaces. The accelerator components include debug and trace circuits. These 
circuits are necessary for any application-specific accelerators required for the different application spaces that a chip supports. 
They vary from one chip to another and could include only trace components.
82.2 Interfaces supported in S32K3 family
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5153 / 5251


---
# 페이지 2

Table 825. Interfaces supported in S32K3xx family
S32K344
S32K324
S32K322
S32K342/
S32K341
S32K312/
S32K311/
S32K310
S32K314
S32K338
S32K358
S32K348
S32K328
S32K388/
S32K389
Cortex-M7_0 (CTI, DWT, 
BPU, ETM, ITM)
Cortex-M7_0 (CTI, DWT, BPU, ITM)
Cortex-M7_0 (CTI, DWT, BPU, ETM, ITM)
—
Cortex-M7_1 
(CTI, DWT, 
BPU, ETM, 
ITM)
Cortex-M7_1 
(CTI, DWT, 
BPU, ITM)
—
Cortex-M7_1 (CTI, DWT, BPU, ETM, ITM)
—
Cortex-M7_2 (CTI, DWT, BPU, ETM, ITM)
Cortex-M7_3 
(CTI, DWT, 
BPU, ETM, 
ITM)
Cortex-M0+
HTM (CTI+DMA/EMAC 
TRACE)
—
HTM (CTI+DMA/EMAC/GMAC TRACE)
HTM 
(CTI+DMA/
GMAC_0/
GMAC_1)
SWO
TPIU
—
TPIU
4x ETF
—
4x ETF
3x Funnel
—
3x Funnel
3x CTI
4x CTI
3x CTI
2x CTI
3x CTI
5x CTI
4x CTI
3x CTI
4x CTI
6x CTI
1x CTM
2x CTM
Timestamp
MDM_AP
SDA_AP
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5154 / 5251


---
# 페이지 3

82.3 Block diagram
This figure illustrates the DAP architecture of the S32K3xx family.
JTAG pins
DAP/TAP
AHB_AP
HTM64
Time
stamp
Boundary
scan
System
JDC
Security
JDC
ETF_x
CSTF_x
HSE_B
AHB_AP
MDM_AP
Cortex-M7_0
IPS2APB
System interconnect (AHB)
Cortex-M7_1
CTl_x
SWO
TPIU
SDA_AP
SWJ-DP
DAPMUX
JTAGC
System debug APB interconnect (APBIC)
APB-AP
AHB_AP
Cortex-M0+
1:1 Gasket
Only available 
on the S32K358
Available only on the
 S32K3x4
Available only on the
 S32K3x4
Cortex-M7_2
AHB_AP
Cortex-M7_3
AHB_AP
Only available 
on the S32K388
JTAG pins
DAP/TAP
AHB_AP
HTM64
Time
stamp
Boundary
scan
System
JDC
Security
JDC
ETF_x
CSTF_x
HSE_B
AHB_AP
MDM_AP
Cortex-M7_0
IPS2APB
System interconnect (AHB)
Cortex-M7_1
CTl_x
SWO
TPIU
SDA_AP
SWJ-DP
DAPMUX
JTAGC
System debug APB interconnect (APBIC)
APB-AP
AHB_AP
Cortex-M0+
1:1 Gasket
Only available 
on the S32K358
Available only on the
 S32K3x4
Available only on the
 S32K3x4
Cortex-M7_2
AHB_AP
Cortex-M7_3
AHB_AP
Only available 
on the S32K388 
and S32K389
Only available 
on the S32K388
and S32K389
Figure 557. DAP architecture
 
Debug components other than the Cortex-M0+ core are accessible through software path (CORE > AXBS > AIPS > 
DAPMUX > APs), that is, by directly specifying the memory mapped addresses without doing challenge response.
  NOTE  
82.4 Features
This chip includes these features that support the functions listed under each feature type:
• Debug control
— Is implemented via IEEE 1149.1-compliant JTAG
• Test control
— Is implemented via IEEE 1149.1-compliant JTAG
— Uses IEEE 1149.6 extension to IEEE 1149.1
• Trace interface
— Includes four high-speed data pads and one clock pad up to 125 MHz (125 MB/s throughput per pad)
— Includes 16 low-speed data pads and one clock pad @25 MHz (100 MB/s throughput per pad)
• Debug security
— Includes a DAP/TAP interface that controls all debug features and is gated by Cortex M0+ JDC module
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5155 / 5251


---
# 페이지 4

— Includes security modes as described in the "Security" chapter
• Debugging and run control
— Is implemented through stopping points, starting points, breakpoints, and watchpoints
— Each Cortex-M7 core supports eight instruction comparators and a watchpoint unit having four watchpoints
• Trace source
— Includes Cortex-M7:
◦ETM that provides instruction and data trace
◦ITM that provides DWT, time-stamping, and diagnostic information
• Cross-triggering support
— Controls run-control options of cores based on other cores
— Provides a matrix having connections to:
◦HTM via system CTI
◦All Cortex-M7 CPUs
• Ability to view and modify all memory-mapped areas that are not otherwise blocked—includes a system bus debug access 
port
• Performance monitoring of cores—implements a performance monitoring unit (PMU) on each Cortex core
• Safety
— Supports monitoring of debug signals to avoid common mode faults
— Allows checking of erroneous activation of debugging, especially if intrusive (for example, a CPU entering Debug 
state)
• Timestamps
— Generates a timestamp bus for distribution to the trace sources
— Includes a 48-bit binary timestamp bus
— Clocks timestamp generator by a frequency given in Table 833
82.5 Debug
82.5.1 TAP connectivity
This figure shows a detailed view of TAP connectivity. JTAG select, SWJ-DP, and JTAG-DP are parts of DAP.
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5156 / 5251


---
# 페이지 5

SWD-JTAG
switcher
JTAG-mode
TCK
TDO
0
1
TMS
TDI
JTAGC
TDO
Arm JTAG-DP
instruction loaded
TCK
TDO
TMS
TDI
JTAG-DP
DBGCLK
DBGDOEN
DBGDO
DBGDI
SWJ-DP
TCK
TMS
TDI
Figure 558. TAP connectivity
The debug port comes out of reset in a standard JTAG mode. It switches to another mode by using the change sequences. After 
the mode changes, unused debug pins can be reassigned to any of their alternative muxed functions.
JTAG-DP and JTAGC are connected in an overlay scheme and both have an Instruction Register (IR) length of 8 bits.
82.5.2 DAP TAP
DAP is an Arm component that provides multiple-master driving ports. A single external interface port accesses and controls these 
ports to provide system-wide debug.
The DAP Instruction Register (DAP IR) overlays with the system JTAG Instruction Register (JTAGC IR). Table 826 presents DAP 
instructions. In addition to the four codes listed in the table, DAP uses BYPASS, which is identical to JTAGC BYPASS and is 
therefore not shown in the table.
Table 826. DAP IR codes
Code
DAP IR
1111_1000b
ABORT
1111_1010b
DPACC
1111_1011b
APACC
1111_1110b
IDCODE
DAP offers an AHB master interface to access system buses. It also exports the internal DAP bus to extend the access ports. For 
more information on DAP TAP, see the Arm Debug Interface Architecture Specification document available in References.
In this chip:
• The AHB slave ports of all Cortex-Mx cores provide debugger access to all memory units and registers in the system.
• The new pass-through approach allows the debugger to see a cache coherent view of the memory map for that core.
• The debugger must access the corresponding AHB_AP port to access the AHB-S port of that subsystem.
• XRDC controls system access.
• A core can access the debug components of another core through a DAPMUX to the bus interconnect.
• The exported DAP bus hosts AHB_AP and MDM_AP.
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5157 / 5251


---
# 페이지 6

— MDM_AP hosts system-level JTAG status and control registers. These registers can be used for cross triggering, 
synchronized debug, and other miscellaneous control and status functions.
— APB_AP uses an APSEL value of 1h to access any APB-mapped debug modules.
Table 830 describes the access addresses of APB-mapped debug modules. The value of the DAP select signal in the APSEL field 
of SWJ-DP's Select register selects the access ports in the DAP. Table 827 shows APSEL decoding.
Table 827. DAP master address mapping
DAP master #
DAP 
component
DAPBUS base 
address 
(access from 
debugger) 1
System memory map address
(access from cores)
Selected port or 
master
Applicability
Page number
Base address
0h
Reserved
0000_0000h
0
4025_0000h
Reserved
-
1h
APB_AP to all 
APB-mapped 
debug modules 
(for example, 
ETFs, HTM, 
and trace 
funnels)
0100_0000h
0
4025_0100h
APB_AP to all 
APB-mapped 
debug modules 
(for example, 
ETFs, HTM, 
CSTF, and so 
on)
All (for ETF, 
HTM, and 
CSTF see 
Table 825).
2h
Reserved
0200_0000h
0
4025_0200h
Reserved
-
3h
AHB_AP to 
Cortex-M7_2 
debug modules 
and chip system 
memory map
0300_0000h
0
4025_0300h
AHB_AP to 
Cortex-M7_2 
debug modules 
and chip system 
memory map
S32K358, 
S32K338, 
S32K388, 
S32K389
4h
AHB_AP to 
Cortex-M7_0 
debug modules 
and chip system 
memory map
0400_0000h
0
4025_0400h
AHB_AP to 
Cortex-M7_0 
debug modules 
and chip system 
memory map
All
5h
AHB_AP to 
Cortex-M7_1 
debug modules 
and chip system 
memory map
0500_0000h
0
4025_0500h
AHB_AP to 
Cortex-M7_1 
debug modules 
and chip system 
memory map
S32K344, 
S32K324, 
S32K322, 
S32K358, 
S32K388, 
S32K389
6h
MDM_AP
0600_0000h
0
4025_0600h
MDM_AP
All
7h
SDA_AP
0700_0000h
0
4025_4700h
SDA_AP used 
for challenge-
response (CR) 
in SWJ-DP 
mode
All
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5158 / 5251


---
# 페이지 7

Table 827. DAP master address mapping (continued)
DAP master #
DAP 
component
DAPBUS base 
address 
(access from 
debugger) 1
System memory map address
(access from cores)
Selected port or 
master
Applicability
Page number
Base address
8h
AHB_AP to 
Cortex-M7_3 
debug modules 
and chip system 
memory map
0800_0000h
0
4025_0700h
AHB_AP to 
Cortex-M7_3 
debug modules 
and chip system 
memory map
S32K388, 
S32K389
9h—FFh
Reserved 
(default AP 
response)
—
—
—
—
—
1. For example, 4025_XXYYh address is provided when accessing access ports (APs) via the core. Here, XX shows the AP 
select number and YY shows the address to be accessed. If you access MDM_AP via the cores on 4h, you must provide 
the address 4025_0604h
 
Accessing SDA_AP simultaneously from the core and the debugger is prohibited. If you try to do so, you may 
receive unpredictable responses to core-initiated transactions (for example, incorrect data read, a failed attempt 
to write to the register, or a transfer error). Debugger-initiated transactions proceed correctly.
  NOTE  
82.5.3 System JTAGC
JTAGC connects in parallel with the TAP controller (JTAG-DP of DAP), which has an IR length of 8 bits. The JTAGC IR codes 
overlay the ones of the DAP controller. DAP uses four instructions and JTAGC uses the remaining ones. The TAP outputs (TPOs) 
are multiplexed based on the selected IR code. This chip is fully JTAG-compliant and appears as a single TAP to the JTAG chain.
This table shows the JTAGC IR codes. The instructions that are used by Arm DAP TAP are shown in Table 826.
Table 828. JTAG instructions for JTAGC
Code
JTAGC IR
0000_0000b
IDCODE
0000_0001b
Reserved
0000_0010b
SAMPLE/PRELOAD
0000_0011b
SAMPLE
0000_0100b
EXTEST
0000_0101b
HI-Z
0000_0110b
Reserved
0000_0111b
Reserved
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5159 / 5251


---
# 페이지 8

Table 828. JTAG instructions for JTAGC (continued)
Code
JTAGC IR
0000_1000b—0000_1001b
Reserved
0000_1010b—0000_1011b
Reserved
0000_1100b
CLAMP
0000_1101b
ENABLE_SOC_DATA1
0000_1110b
Reserved
0000_1111b
Reserved
1000_0000b
Reserved
1000_0001b
Reserved
1000_0010b
Reserved
1000_0011b
Reserved
1000_0100b
Reserved
1000_0101b
Reserved
1000_0110b—1000_0111b
Reserved
1000_1000b
Reserved
1000_1001b
Reserved
1000_1010b—1000_1111b
Reserved
1001_0000b
Security JDC
1001_0001b
System JDC
1001_0010b—1001_0111b
Reserved for other system auxiliary clients
1001_1000b—1001_1011b
Reserved
1001_1100b—1011_1111b
Reserved for other system auxiliary clients
1100_0000b
Reserved
1100_0001b
Reserved
1100_0010b—1110_1111b
Reserved
1111_1000b
ABORT (Arm)
1111_1001b
Reserved
1111_1010b
DPACC (Arm)
1111_1011b
APACC (Arm)
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5160 / 5251


---
# 페이지 9

Table 828. JTAG instructions for JTAGC (continued)
Code
JTAGC IR
1111_1100b
Reserved
1111_1101b
Reserved
1111_1110b
IDCODE (Arm)
1111_1111b
BYPASS
82.5.3.1
Chip JTAG/Target ID
Each chip in the S32K3xx family includes a unique JTAG ID, which must be changed when instantiated with a different die in an 
SiP. The next table shows the JTAGC ID for this chip.
Table 829. JTAG/Target ID
Chip
PRN
DC
PIN
MIC
IDCODE ID
JTAG ID
Target ID
S32K344
0
26h (38d)
160h (352d)
Eh (14d)
1
0996_001Dh
0995_C01Dh
S32K324
0
26h (38d)
160h (352d)
Eh (14d)
1
0996_001Dh
0996_001Dh
S32K314
0
26h (38d)
160h (352d)
Eh (14d)
1
0996_001Dh
0996_001Dh
S32K311/
S32K310
0
26h (38d)
16Ch (364d)
Eh (14d)
1
0996_C01Dh
0996_C01Dh
S32K312
0
26h (38d)
168h (360d)
Eh (14d)
1
0996_801Dh
0996_801Dh
S32K342 / 
S32K341 / 
S32K322
0
26h (38d)
164h (356d)
Eh (14d)
1
0996_401Dh
0996_401Dh
S32K358 / 
S32K348 / 
S32K338 / 
S32K328
0
26h (38d)
15Eh (350d)
Eh (14d)
1
1995_E01Dh
1995_E01Dh
S32K388
0
26h(38d)
15Ah (346d)
Eh (14d)
1
0995_A01Dh
0995_A01Dh
S32K389
0
26h(38d)
162h(354d)
Eh (14d)
1
0996_201Dh
0996_201Dh
82.5.3.2
JDC
JDC allows you to access two 32-bit data registers by using the JTAG interface and by software running on one of the CPUs in 
the chip. These registers exchange data between an internal CPU and an external debug tool.
82.5.4 Peripheral IPG debug implementation
Any core can control a peripheral instance individually. You define the core's control over a peripheral during 
application development.
For peripheral halt, all individual cores have the same capability and are gated by a dedicated MDM_AP core halt register field. 
For more information, see the configurations defined in MDM_AP register descriptions.
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5161 / 5251


---
# 페이지 10

 
 
 
 
 
Cortex-M7_0  is halted
Cortex-M7_1  is halted
Cortex-M7_0 
Cortex-M7_1
 
GPR_CORE1_DBGFRZ0[P0]
GPR_CORE0_DBGFRZ0[P0]
  
Peripheral 0
Not available on the S32K311, S32K312, and S32K314
 
 
 
Cortex-M7_2
Only available on S32K358
Cortex-M7_2  is halted
 
 
 
Cortex-M7_3
Only available on S32K388
Cortex-M7_3  is halted
GPR_CORE2_DBGFRZ0[P0]
GPR_CORE3_DBGFRZ0[P0]
Figure 559. Peripheral IPG debug implementation
82.5.5 Application debugging
This section covers the following two cases:
• Case 1: Debugger connected—application debugging from the first instruction
• Case 2: Debugger not connected
82.5.5.1
Application debugging from first instruction
This chip supports debugging from the first instruction on system power-up, destructive reset, functional reset, and standby exit. 
However, by default, debugging from the first instruction is disabled.
The next figure shows the timing diagram of application debug implementation from first instruction on system power-up or 
destructive reset.
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5162 / 5251


---
# 페이지 11

SDA_AP [Reset_Release]
Debugger keeps the chip in reset by pressing reset pin
Debugger configures to hold app core’s reset
Debugger releases the chip’s reset pin; app core still in reset
The expected response; status is written in SDA_AP
The application core clock is enabled as per the configurations
Debugger provides the expected response and CR passes status to SDA_AP
Debugger configures the core’s debug and releases the core’s resets
Reset_b pad
Valid challenge
CCTL
app dbg en
Before app dbg en becomes 1, the debugger has
no access to the chip except for some SDA_AP
response, status, and reset-release registers.
Debugger decision must be configured before
reset deassertionbecause the debugger isn't
aware about the moment the application core
clock gets enabled
Figure 560. Application debug implementation from first instruction
These are the steps involved in enabling application debug from the first instruction on system power-up or destructive reset. 
Similar steps are to be performed for application debugging for core Cortex-M7_2 and core Cortex-M7_3 as applicable.
1. After the reset is applied, the debugger provides an option to debug from the first instruction. To do this:
a. Write 0 to SDAAPRSTCTRL[RSTRELTLCM70] and SDAAPRSTCTRL[RSTRELTLCM71].
b. Set the reset value of Reset Control (SDAAPRSTCTRL).
2. Cortex M0+ starts after the reset pin is released.
3. Debugger challenge-response (CR) starts.
4. Cortex-M7 cores remain in reset until MC_ME's PRTN0_COREx_PCONF[CCE] field becomes 1 for respective Cortex-
M7 core.
5. When BAF or FW writes 1 to MC_ME's PRTN0_CORE0_PCONF[CCE] field for Cortex-M7_0 and to 
PRTN0_CORE1_PCONF[CCE] field for Cortex-M7_1, and the debugger CR has passed:
• Configure the core debug registers, then write SDAAPRSTCTRL[RSTRELTLCM70] and 
SDAAPRSTCTRL[RSTRELTLCM71] to 1 that start the code execution.
To debug from the first instruction during the low-power debug protocol, the debugger:
1. Writes 0 to SDAAPRSTCTRL[RSTRELTLCM71] and SDAAPRSTCTRL[RSTRELTLCM70] for their respective cores.
2. Writes 1 to MDMAPWIRREL[WTRSTRGM].
82.5.5.1.1
Debug from first instruction on functional reset onwards
If you enable debug, on functional reset, the debug connection is retained. That is because the complete debug infrastructure is 
on destructive reset domain.
82.5.5.1.2
Debug on standby exit by wake-up or functional reset
If you enable debug before standby entry, then the Standby domain stores the final status. The configuration for 
reset release is reset (SDA_AP.SDAAPRSTCTRL[RSTRELTLCM70], SDA_AP.SDAAPRSTCTRL[RSTRELTLCM71] and 
SDA_AP.SDAAPRSTCTRL[RSTRELTLCM72]. The reset value of the three fields is 1), which defaults to debug from the 
first instruction disabled.
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5163 / 5251


---
# 페이지 12

You must configure the reset release on standby exit. It uses MC_RGM's low-power debug protocol before ungating the 
reset deassertion.
82.5.5.2
Debugger not connected
If the debugger is not connected, the value of the DBGPWRUP_ACK signal is 0 as there is no DBGPWRUP_REQ. This results 
in the following scenario:
1. The booting core writes 1 to MC_ME's PRTN0_CORE0_PCONF[CCE] field for Cortex-M7_0, 
PRTN0_CORE1_PCONF[CCE] field for Cortex-M7_1, PRTN0_CORE4_PCONF[CCE] field for Cortex-M7_2, and 
PRTN0_CORE3_PCONF[CCE] field for Cortex-M7_3 (as per core's availability).
2. The application core starts running. In case of Lock-step mode, the checker core executes the same code after a delay of 
two cycles.
82.5.6 Debugger considerations while flash program/erase
The flash programming can be done by application cores as well as debugger. The debugger can program/erase flash using either 
of the following two options:
1. Loading the program/erase code to SRAM from the debugger and then executing the program/erase sequence by 
application code from SRAM.
• Debugger is connected and authenticated.
• The debugger loads the code in the form of application binary image into the on-chip SRAM.
• The debugger then initiates the application core to execute the binary from SRAM.
2. Debugger executing the program/erase sequence.
• Debugger is connected and authenticated.
• The debugger then initiates the flash programming by reading/writing the registers involved and following the program/
erase sequence.
First option is the recommended because of less execution time. In second option, the debugger is the master and since the debug 
interface is serial, the execution takes more time.
In some cases, you might experience flash program/erase failure due to flash watchdog timeout when debugger executes the flash 
program/erase sequence due to the serial interface. Therefore, it is recommended to use the first option. In case second option 
is required, it should be performed in reduced clocking options (Option E and E2 only. For details, refer to the Clocking details 
section in the Clocking chapter).
82.5.7 SWJ-DP sequence for debug authentication
To perform the SWJ-DP sequence for debug authentication, the debugger:
1. Polls the AUTHSTTS[CHALRDY] field until it indicates the challenge status.
2. Reads Key Challenge (KEYCHAL0 - KEYCHAL7) if the challenge is valid and creates an authenticated 256-bit 
response key.
3. Writes a 256-bit response key to Key Response (KEYRESP0 - KEYRESP7).
4. Indicates that the response is ready by configuring AUTHCTL[HSEAUTHREQ].
5. Checks the status of Authentication Status (AUTHSTTS) to evaluate if the operation is successful.
If the authentication process is successful and the debugger has write access to Debug Enable Control (DBGENCTRL), 
the challenge or response is considered successful too.
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5164 / 5251


---
# 페이지 13

 
SDA_AP supports challenge and response based on both JTAG and SWJ-DP modes. See 
SDAAPGENCTRL0[JTAG_CR_EN] for details.
  NOTE  
82.6 APB memory map
You can access the debug registers via the APB_AP bus. The next table shows all the addresses for the CoreSight APB 
components and the addressing used for accessing the DAP components via the memory interface. You can also access all APB 
registers from the processing cores.
Table 830. APB components mapping
Debug APB 
component
APBIC base 
address (access 
from debugger)
System memory map address
(access from cores)
Memory 
allocation (KB)
APB-AP0 slot 
number
Applicability
Page number
Base address
APB_AP ROM 
table
F8h
0
4024_00F8h
4
APBIC base
All
Funnel 0
1000h
0
4024_1000h
4
0
ETM/
ITM:S32K344, 
S32K324, 
S32K314 
S32K358, 
S32K348, 
S32K338, 
S32K328, 
S32K388, 
S32K389
ITM: S32K312, 
S32K310, 
S32K311, 
S32K342, 
S32K341, 
S32K322
Funnel 1
2000h
0
4024_2000h
4
1
S32K344, 
S32K324, 
S32K314 
S32K358, 
S32K348, 
S32K338, 
S32K328, 
S32K388, 
S32K389
Funnel 2
3000h
0
4024_3000h
4
2
S32K344, 
S32K324, 
S32K314 
S32K358, 
S32K348, 
S32K338, 
S32K328, 
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5165 / 5251


---
# 페이지 14

Table 830. APB components mapping (continued)
Debug APB 
component
APBIC base 
address (access 
from debugger)
System memory map address
(access from cores)
Memory 
allocation (KB)
APB-AP0 slot 
number
Applicability
Page number
Base address
S32K388, 
S32K389
CM7_cluster_E
TF_ETMI
4000h
1
4024_4000h
4
3
S32K344, 
S32K324, 
S32K314 
S32K358, 
S32K348, 
S32K338, 
S32K328, 
S32K388, 
S32K389
CM7_cluster_E
TF_ETMD
5000h
1
4024_5000h
4
4
S32K344, 
S32K324, 
S32K314 
S32K358, 
S32K348, 
S32K338, 
S32K328, 
S32K388, 
S32K389
HTM ETF
6000h
1
4024_6000h
4
5
S32K344, 
S32K324, 
S32K314 
S32K358, 
S32K348, 
S32K338, 
S32K328, 
S32K388, 
S32K389
Shared_system
_ETF
7000h
1
4024_7000h
4
6
S32K344, 
S32K324, 
S32K314 
S32K358, 
S32K348, 
S32K338, 
S32K328, 
S32K388, 
S32K389
HTM 0
8000h
2
4024_8000h
4
7
S32K344, 
S32K324, 
S32K314 
S32K358, 
S32K348, 
S32K338, 
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5166 / 5251


---
# 페이지 15

Table 830. APB components mapping (continued)
Debug APB 
component
APBIC base 
address (access 
from debugger)
System memory map address
(access from cores)
Memory 
allocation (KB)
APB-AP0 slot 
number
Applicability
Page number
Base address
S32K328, 
S32K388, 
S32K389
HTM 0 CTI
9000h
2
4024_9000h
4
8
S32K358, 
S32K348, 
S32K338, 
S32K328, 
S32K344, 
S32K324, 
S32K314, 
S32K388, 
S32K389
TPIU
A000h
2
4024_A000h
4
9
S32K344, 
S32K324, 
S32K314 
S32K358, 
S32K348, 
S32K338, 
S32K328, 
S32K388, 
S32K389
System SWO
B000h
2
4024_B000h
4
10
All
Timestamp CTL
C000h
3
4024_C000h
4
11
All
Funnel 0 should be configure to buffer the data coming from the different sources, to avoid padding data with null packets that 
affect the bandwidth.
82.7 Trace
82.7.1 Trace modules and connectivity
The Trace subsystem:
• Combines trace data from all internal clients that generate trace information
• Includes a 32-bit TPIU
• Includes these components:
— ATB
— ATBR
— CSTF
— Debug APB
— ETF
— TPIU
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5167 / 5251


---
# 페이지 16

Multiple options for trace output allow parallel tracing. Trace information can be read from the trace interface or the DAP interface, 
and traces can be alternatively read out from ETF at a slow speed via APB_AP. Table 831 shows EFT sizes.
Table 831. ETF sizes
FIFO
Memory interface data width 
(in bits)
Size (KB)Applicable for All, 
except S32K388
Size (KB)Applicable for 
S32K388/S32K389
Cortex-M7 ETM/ITM cluster 
ETF
64
1
4
Cortex-M7 ETMD cluster ETF
128
2
4
HTM ETF
64
1
2
Shared system ETF
64
2
4
 
• The DMA-HTM trace supports four words at 80 MHz. For HTM trace, both DBGENCTRL[GSPNIDEN] and 
DBGENCTRL[GSPIDEN] must be 1.
• Enabling any one of data trace causes overflow inside ETM and trace packets get dropped. Enabling 
instruction trace of both the core simultaneously does not cause any overflow.
  NOTE  
Control (MDMAPCTL) provides fields to override the speed control (see Table 832 for details) from some of the trace sinks (and 
TPIU). The complete trace pipeline bandwidth is limited by the slowest sink component. The default settings of these fields allow 
maximum bandwidth for the TPIU to trace. When tracing to memory (if supported), the fields may need to be changed.
Table 832. Trace output overrides
Trace destination
SWO_override
TPIU_override
TPIU
1
0
The trace sources of the chip are the cores and their related modules. Trace funnels exist for all possible trace clients. For more 
information on the various components in the trace bus connectivity, see the CoreSight Components Technical Reference Manual 
(available in References). See Table 833 for details on funnel assignments.
The ATBR is integrated to send a shared funnel output across TPIU. This figure illustrates the chip's detailed trace architecture.
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5168 / 5251


---
# 페이지 17

Trace @ 25 MHz DDR: 50 MHz Clock Logic
Trace @ 125 MHz DDR: 250 MHz Clock Logic (Room Temp Only)
Trace Clkout: 25 MHz
Trace Clkout: 125 MHz
150 MHz
UP = Upsizer ; DN = Downsizer
32
ETF
4KB
320M
F
U
N
N
E
L
0
32
CM7_0: ETMD
64
CM7_1: ETMD
64
CM7_2_LS: ETMD
64
CM7_3: ETMD
64
F
U
N
N
E
L
2
DMA
GMAC_0
GMAC_1
ETF
2KB
HTM
32
D
N
F
U
N
N
E
L
1
64
ETF
4KB
320M
32
32
160M
32
ETF
4KB
A
Async
Bridge
B
320M
Replicator
125/25M
TPIU
SWO
D
N
32
8
A
Async
Bridge
B
320M
32
300 MHz
CLKOUT
U
P
CM7_3: ITM
8
32
U
P
CM7_3: ETMI
8
32
U
P
CM7_2_LS: ITM
8
32
U
P
CM7_2_LS: ETMI
8
32
U
P
CM7_1: ITM
8
32
U
P
CM7_1: ETMI
8
32
U
P
CM7_0: ITM
8
32
U
P
CM7_0: ETMI
8
32
Figure 561. S32K389 detailed trace architecture
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5169 / 5251


---
# 페이지 18

Trace @ 25 MHz DDR: 50 MHz Clock Logic
Trace @ 125 MHz DDR: 250 MHz Clock Logic (Room Temp Only)
Trace Clkout: 25 MHz
Trace Clkout: 125 MHz
160 MHz
UP = Upsizer ; DN = Downsizer
32
ETF
4KB
320M
F
U
N
N
E
L
0
32
CM7_0: ETMD
64
CM7_1: ETMD
64
CM7_2_LS: ETMD
64
CM7_3: ETMD
64
F
U
N
N
E
L
2
DMA
GMAC_0
GMAC_1
ETF
2KB
HTM
32
D
N
F
U
N
N
E
L
1
64
ETF
4KB
320M
32
32
160M
32
ETF
4KB
A
Async
Bridge
B
320M
Replicator
125/25M
TPIU
SWO
D
N
32
8
A
Async
Bridge
B
320M
32
320 MHz
CLKOUT
U
P
CM7_3: ITM
8
32
U
P
CM7_3: ETMI
8
32
U
P
CM7_2_LS: ITM
8
32
U
P
CM7_2_LS: ETMI
8
32
U
P
CM7_1: ITM
8
32
U
P
CM7_1: ETMI
8
32
U
P
CM7_0: ITM
8
32
U
P
CM7_0: ETMI
8
32
Figure 562. S32K388 detailed trace architecture
Trace @ 25 MHz DDR: 50 MHz Clock Logic
Trace @ 125 MHz DDR: 250 MHz Clock Logic (Room Temp Only)
Trace Clkout: 25 MHz
Trace Clkout: 125 MHz
UP = Upsizer ; DN = Downsizer
32
ETF
1KB
240M
F
U
N
N
E
L
0
32
CM7_0: ETMD
64
CM7_1: ETMD
64
CM7_2: ETMD
64
F
U
N
N
E
L
2
DMA
GMAC
ETF
1KB
HTM
32
D
N
F
U
N
N
E
L
1
64
ETF
2KB
240M
32
32
32
ETF
2KB
A
Async
Bridge
B
240M
Replicator
125/25M
TPIU
SWO
D
N
32
8
240M
32
240 MHz
CLKOUT
8
32
CM7_0: ETMI
U
P
8
32
CM7_0: ITM
U
P
8
32
CM7_1: ETMI
U
P
8
32
CM7_1: ITM
U
P
8
32
CM7_2: ETMI
U
P
8
32
CM7_2: ITM
U
P
Not available on
S32K328 and S32K348
Not available on
S32K328 and S32K348
Figure 563. S32K358, S32K348, S32K338, and S32K328 detailed trace architecture
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5170 / 5251


---
# 페이지 19

Trace @ 25 MHz DDR: 50 MHz Clock Logic
Trace @ 120 MHz DDR: 240 MHz Clock Logic (Room Temp Only)
Trace Clkout: 25 MHz
Trace Clkout: 120 MHz
UP = Upsizer ; DN = Downsizer
32
ETF 
1KB
160M
F
U
N
N
E
L
0
32
CM7_0: ETMD
64
CM7_1: ETMD
64
F
U
N
N
E
L
2
DMA
EMAC
ETF 
1KB
HTM
32
D
N
F
U
N
N
E
L
1
64
ETF 
2KB
160M
32
32
32
ETF 
2KB
A
Async
Bridge
B
160M
Replicator
120/25M
TPIU
SWO
D
N
32
8
160M
32
160 MHz
CLKOUT
8
32
CM7_0: ETMI
U
P
8
32
CM7_0: ITM
U
P
8
32
CM7_1: ETMI
U
P
8
32
CM7_1: ITM
U
P
Not available on 
S32K314
Not available on 
S32K314
Figure 564. S32K344, S32K324, and S32K314 detailed trace architecture
25 MHz
F
U
N
N
E
L
0
8
A
Async
Bridge
B
160M
25M
SWO
8
160 MHz
8
CM7_0: ITM
8
CM7_1: ITM
Figure 565. S32K342, S32K341, and S32K322 detailed trace architecture
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5171 / 5251


---
# 페이지 20

25 MHz
8
A
Async
Bridge
B
120M
25M
SWO
8
120 MHz
CM7_0: ITM
Figure 566. S32K312, S32K311, and S32K310 detailed trace architecture
Table 833. Funnel assignments
Funnel
Port
Input
Frequency (in MHz)
S32K342/S32K341/S32K322 
S32K344/S32K324/S32K314
S32K328/S32K338/S32K348/S32K358
S32K388 S32K
389
0
0
Cortex-M7_0 
ETMI
160
240
320
300
0
1
Cortex-M7_0 
ITM
160
240
320
300
0
2
Cortex-M7_1 
ETMI
160
240
320
300
0
3
Cortex-M7_1 
ITM
160
240
320
300
0
4
Cortex-M7_2 
ETMI
-
240
320
300
0
5
Cortex-M7_2 
ITM
-
240
320
300
0
6
Cortex-M7_3 
ETMI
-
-
320
300
0
7
Cortex-M7_3 
ITM
-
-
320
300
1
0
Cortex-M7_0 
ETMD
160
240
320
300
1
1
Cortex-M7_1 
ETMD
160
240
320
300
1
2
Cortex-M7_2 
ETMD
-
240
320
300
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5172 / 5251


---
# 페이지 21

Table 833. Funnel assignments (continued)
Funnel
Port
Input
Frequency (in MHz)
S32K342/S32K341/S32K322 
S32K344/S32K324/S32K314
S32K328/S32K338/S32K348/S32K358
S32K388 S32K
389
1
3
Cortex-M7_3 
ETMD
-
-
320
300
1
4-7
Reserved
-
-
-
-
2
0
Cortex-M7 
instruction ETF 
through an 
asynchronous 
bridge
160
240
320
300
2
1
Cortex-M7 data 
ETF through an 
asynchronous 
bridge
160
240
320
300
2
2
HTM ETF 
through an 
asynchronous 
bridge
160
240
320
300
2
3-7
Reserved
-
-
-
-
82.7.1.1
Chip's bus trace client
Chips in the S32K3xx family include a bus trace client.
HTM provides the address and data trace information about AXBS buses. The information from an HTM can be used with the 
debugger to enable easy, accurate debugging on AXBS-based embedded systems. The chip implements an HTM64 configuration 
to trace 64-bit AXBS masters in the system. To simplify the implementation, instead of tracing the individual ports of various AXBS 
masters and slaves, which may be running at different frequencies, HTM64 snoops the AXBS crossbar master ports that are all 
synchronous with a 160 MHz system clock. This table provides details related to the HTM input connectivity.
Table 834. HTM connections
HTM64 port
AHB crossbar port
HTMBUSSELECT0
M0 AXBS_Lite XBIC (DMA)
HTMBUSSELECT1
M3 AXBS (Ethernet)
HTMBUSSELECT21
M6 AXBS (Ethernet 2)
1. Only applicable for S32K388 and S32K389.
82.7.1.2
TPIU interface
A standard 16-bit parallel TPIU is integrated into the debug subsystem. Chips in the S32K3xx family generate the trace via the 
trace port.
To prevent instruction trace from being dropped in a multi-core environment, a TPIU throughput of 55.2 MB/s or higher must be 
maintained. You could use these pin and frequency combinations:
• Four high-speed data + one clock pads @120 MHz (240 Mbit/s throughput per pad) totaling 120 MB/s
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5173 / 5251


---
# 페이지 22

• 16 low-speed data + one clock pads @25 MHz (50 Mbit/s throughput per pad) totaling 100 MB/s
High-end chips from the S32K3xx family support at least 56 MB/s of trace throughput on the TPIU interface.
Table 835. Throughput for S32K389 and S32K388
Core
Throughput value
Cortex-M7_0
31.06 MB/s
Cortex-M7_1
31.06 MB/s
Cortex-M7_2
31.06 MB/s
Cortex-M7_3
31.06 MB/s
Total
124.24 MB/s
Table 836. Throughput for all chips except S32K388
Core
Throughput value
Applicability
Cortex-M7_0
27.6 MB/s
S32K344, S32K324, 
S32K314 S32K358, S32K348, 
S32K338, S32K328
Cortex-M7_1
27.6 MB/s
S32K338, S32K328, S32K324
Cortex-M7_2
27.6 MB/s
S32K358, S32K338
Total
82.8 MB/s
82.7.1.3
TPIU flush
To allow the chip to enter Standby mode, software executes an WFI instruction indicating Standby entry. When the chip enters this 
mode, MC_RGM asserts a trace flush request to the TPIU and waits for a trace flush done signal from the TPIU  before requesting 
MC_PCU to proceed. The TPIU and debug infrastructure clocks can be gated after this. Because the TPIU is sourced from system 
clock, the clock must not be gated until this point.
82.7.1.4
Trace through reset
All debug and trace components (HTM, ETM, ETF, and so on) are on destructive reset. When tracing through reset, the clock 
switches from PLL to FIRC. It is recommended to preserve the following pad configurations across reset, which are performed 
through MDMAPCTL[DBGRSTFASTPAD] and MDMAPCTL[DBGRSTSLOWPAD]:
• Four high-speed data + one clock pads @120 MHz (240 Mbits/s throughput per pad) totaling 120 MB/s
• 16 low-speed data + one clock pads @25 MHz (50 Mbits/s throughput per pad) totaling 100 MB/s
The implementation involves writing 1 to MDMAPCTL[DBGRSTFASTPAD] or MDMAPCTL[DBGRSTSLOWPAD], depending on 
which set of trace pads you need to enable. These fields also control:
• The trace pad mux.
• The "obe" of the trace pads, which, if configured, is retained over functional reset because the reset is controlled using the 
above-mentioned corresponding fields.
82.8 Embedded cross trigger (ECT)
ECT allows multi-core run control and trace cross-triggering, such as synchronous stop-start for all cores or trigger trace on a 
trigger event from another core or module. See the CoreSight Components Technical Reference Manual (available in References) 
for detailed information on ECT. 
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5174 / 5251


---
# 페이지 23

ECT architecture involves CTMs and CTIs. The CTIs provide a cross-triggering interface between the cores and other debug and 
trace modules. The channels of these CTIs are interconnected using CTMs, as shown in this figure. 
The following figure shows ECT
CTM 0
CH 1
CH 2
CH 3
CH 0
CTM 1
CH 0
CH 1
CH 2
CH 3
CTI
Cortex-M7_0
CTI
Cortex-M7_1
CTI
Cortex-M7_2
CTI
Cortex-M7_3
HSE Subsystem CTI
CTI
5
off_pl_ETF
_Trigger
HTM
Only available
  on S32K358, S32K388, 
and S32K389
Only available
on  S32K388 
and S32K389
Figure 567. ECT
82.8.1 CTI assignments
Table 837. CTI assignments
CTI instance
Trigger number
Trigger in
Trigger out
CTI_Cortex-M7_0
7
ETM event output 3
Processor restart
6
ETM event output 2
ETM event input 3
5
ETM event output 1
ETM event input 2
4
ETM event output 0
ETM event input 1
3
DWT comparator output 2
ETM event input 0
2
DWT comparator output 1
Interrupt request 1
1
DWT comparator output 0
Interrupt request 0
0
Processor halted
Processor debug request
CTI_Cortex-M7_1
7
ETM event output 3
Processor restart
6
ETM event output 2
ETM event input 3
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5175 / 5251


---
# 페이지 24

Table 837. CTI assignments (continued)
CTI instance
Trigger number
Trigger in
Trigger out
5
ETM event output 1
ETM event input 2
4
ETM event output 0
ETM event input 1
3
DWT comparator output 2
ETM event input 0
2
DWT comparator output 1
Interrupt request 1
1
DWT comparator output 0
Interrupt request 0
0
Processor halted
Processor debug request
CTI_Cortex-M7_2
7
ETM event output 3
Processor restart
6
ETM event output 2
ETM event input 3
5
ETM event output 1
ETM event input 2
4
ETM event output 0
ETM event input 1
3
DWT comparator output 2
ETM event input 0
2
DWT comparator output 1
Interrupt request 1
1
DWT comparator output 0
Interrupt request 0
0
Processor halted
Processor debug request
CTI_Cortex-M7_3
7
ETM event output 3
Processor restart
6
ETM event output 2
ETM event input 3
5
ETM event output 1
ETM event input 2
4
ETM event output 0
ETM event input 1
3
DWT comparator output 2
ETM event input 0
1
DWT comparator output 0
Interrupt request 0
0
Processor halted
Processor debug request
2
DWT comparator output 1
Interrupt request 1
CTI_0
7
Reserved (grounded)
Reserved (no connection)
6
ETF_3 full
ETF_3 trigger input
5
ETF_2 full
ETF_2 trigger input
4
ETF_1 full
ETF_1 trigger input
3
ETF_0 full
ETF_0 trigger input
2
HTM trigger out 2
HTM trigger in 1
1
HTM trigger out 1
HTM trigger in 0
0
HTM trigger out 0
Reserved
82.9 Low-power debug handshake protocol
The debugger must perform this sequence to enter or exit Standby mode, if the debugger handshake is enabled:
1. Power on DAP.
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5176 / 5251


---
# 페이지 25

The debugger connection is established.
2. Configure the Debug subsystem for the relevant operations.
3. Write 1 to MDMAPWIREN[LWPWREN] to gate entry into Standby mode with the debugger handshake.
4. Disable POR_WDG for monitoring the entry to or exit from Standby mode by writing 1 to DCM's DCMRWP1[8] field. 
This is required for low-power debug handshake because debugger configurations can be more time consuming than 
the POR_WDG threshold levels and can raise a false POR_WDG event.
5. Write 1 to DCMRWF1[STANDBY_IO_CONFIG] in the Device Configuration Module (DCM). This causes padkeeping 
to be disabled on standby entry itself without any software dependency. This is needed in case of low-power 
debug since otherwise the padkeeping on TDO would result in no debugger communication. In other cases, 
DCMRWF1[STANDBY_IO_CONFIG] should be configured as 0 before standby entry.
6. Initiate entry into Standby mode. See the "Power Management" chapter for the Standby mode entry sequence and 
configurations.
7. Identify whether the low-power debug is enabled on the low-power entry.
• If low-power debug is enabled and TPIU is enabled too, trace flush starts, and the debugger acknowledges the 
following:
— Low-power debug traces
— DAP-related configuration reception and context saving
After this, the chip enters Standby mode.
• If TPIU is disabled:
— The debugger acknowledges DAP-related configuration reception and context saving by writing 1 to 
MDMAPWIRREL[PRVNTRSTRGM].
After this, the chip enters Standby mode.
• If low-power debug is disabled, the chip enters Standby mode without waiting for debugger acknowledgment.
On any wakeup event, the chip starts the Standby mode exit sequence described in the "Power Management" chapter. After 
the chip exits Standby mode, the debugger connection is restored. By this time, the debugger is already aware that it has 
enabled the low-power debug handshake. In this case, the debugger must poll MDMAPSTTS[DESTRST] to check whether:
• The debug infrastructure is out of reset.
• The DAP connection can be established.
After DAP is powered on (the debugger connection is established), the debugger:
a. Reconfigures the debug and trace attributes using the fields in DBGENCTRL
b. Writes 1 to MDMAPWIRREL[WTRSTRGM] after the debugger trace context is restored
The chip exits Standby mode.
If low-power debug is not configured, the chip exits Standby mode without waiting for the debugger to write 
to MDMAPWIRREL[WTRSTRGM].
8. Reconfigure the debug and trace configuration in SDA_AP register descriptions after the chip exits Standby mode.
 
If the chip wakes up from Standby mode through pad reset, the debugger must perform a CR again.
  NOTE  
82.10 Debug resets
The debug subsystem follows this sequence on the source of reset:
1. POR resets the complete debug logic.
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5177 / 5251


---
# 페이지 26

2. The destructive reset resets all types of debug logic except JTAGC.
Conversely, the debug subsystem can generate a system reset using these mechanisms:
• System destructive reset defined in Control (MDMAPCTL) that allows the debugger to provide the destructive reset to the 
system. The debugger loses connection to the system with this reset.
• System functional reset defined in Control (MDMAPCTL) that allows the debugger to hold the system in functional reset.
To program various debug registers, the functional clocks must be enabled. All debug and trace components must be on 
destructive reset.
82.11 Debug across device LifeCycles
The debug access to the system is available in early lifecycles and subsequently based on NVM configuration settings.
After the debug is set to 'Trusted', the system access is allowed after a successful authorization step between the debugger and 
the system.
The authorization provides provisions to allow debug for Cortex M0+ core and Cortex M7 cores.
Following table shows the debug access based on various configuration bits.
Table 838. Debug access based on LifeCycle and bit configurations
LifeCycle
Debug access
Appl Core Debug
MCU_PROD
Open
Open
CUST_DEL
Open
Open
OEM_PROD
Closed
Trusted
Trusted
Disabled
IN_FIELD
Closed
Trusted
Trusted
Disabled
PRE_FA
Trusted
Trusted
FA
Open
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5178 / 5251


---
# 페이지 27

 
1. Open: Debug is always possible
2. Trusted: Debug is possible after successful authentication (Challenge/Response handshake with 
correct credentials)
3. During functional reset, the debug-enable will retain its last status, while DCM scans NVM for lifecycle and 
DCF values. Debug status will be re-evaluated once dcm_done gets 1.
4. During temporary advancement of lifecycle, debug-en will immediately reflect the status based on updated 
lifecycle/DCF bits.
  NOTE  
82.12 Pin interface
This table presents a summary of functional and power pins that are used for debugging purposes.
Table 839. Pin interface 
Pin type
Pins
Number of pins (balls)1
Nominal voltage
Functional JTAG
JCOMP, TCK, TMS, TDI, TDO
Five (only TDI and TDO can be 
multiplexed with GPIO or other 
functions)
3.3 V, 5 V
Functional trace pins 
(parallel trace)
TRACE_CLK
One
3.3 V, 5 V
TRACE_D[15:0]
16
3.3 V, 5 V
Ground
VSS
See the IOMUX file attached to 
this document for information on 
the number of VSS pins in various 
packages.
0 V
1. The terms pins and balls are used interchangeably. Some chip packages include pins and others include balls.
 
Fast Trace pad TRACE_D[15:0] is available only in S32K344.
  NOTE  
82.12.1 Debug port and pin descriptions
The pads to which the debug signals are mapped operate using the JTAG functionality out of reset but can later be reassigned 
to their alternate functionalities. TDI and TDO can operate as alternate GPIO functions. See this table for pin assignments in 
different modes.
Table 840. Debug port pins
Pin name
JTAG debug port
Internal pullup or 
pulldown logic
Type
Description
TMS
I/O
JTAG test mode selection (TMS)
Pullup
TCK/SWCLK
I
JTAG test clock (TCK)
Pulldown
TDI
I
JTAG test data input (TDI)
Pullup
TDO/TRACESWO
O
JTAG test data output (TDO)
Not connected
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5179 / 5251


---
# 페이지 28

82.12.2 Trace port pin descriptions
This chip generates trace via TPIU that transmits the trace data out of the chip over a parallel trace port. The trace port consists 
of an ETM trace clock and 16 parallel trace data outputs. The Arm optional trace port control (TRACECTRL), debug request 
(DBGRQ), and debug acknowledge (DBGACK) signals are not implemented.
Table 841. Trace output port pins
Pin name
Description
TRACE_DATA00
ETM parallel trace data output 01
TRACE_DATA01
ETM parallel trace data output 01
TRACE_DATA02
ETM parallel trace data output 02
TRACE_DATA03
ETM parallel trace data output 03
TRACE_DATA04
ETM parallel trace data output 04
TRACE_DATA05
ETM parallel trace data output 05
TRACE_DATA06
ETM parallel trace data output 06
TRACE_DATA07
ETM parallel trace data output 07
TRACE_DATA08
ETM parallel trace data output 08
TRACE_DATA09
ETM parallel trace data output 09
TRACE_DATA10
ETM parallel trace data output 10
TRACE_DATA11
ETM parallel trace data output 11
TRACE_DATA12
ETM parallel trace data output 12
TRACE_DATA13
ETM parallel trace data output 13
TRACE_DATA14
ETM parallel trace data output 14
TRACE_DATA15
ETM parallel trace data output 15
TRACE_CLK
ETM parallel trace clock output
 
ETM is supported in S32K344 only
  NOTE  
 
By default, Rx pins float and are not pulled inside. An internal active pulldown logic exists only when you enable 
Rx via software (IBE).
  NOTE  
82.13 Timestamp distribution network
The timestamp distribution network uses CoreSight timestamp components to generate a 48-bit timestamp value for the trace 
sources, as shown in the next figure. The CoreSight timestamp generator generates a 64-bit counter value, but only the 
least significant 48 bits are distributed to the trace sources. A 7-bit narrow timestamp is derived from the 48-bit timestamp 
and distributed to the trace client, where a decoder regenerates the 48-bit timestamp. The generator must be programmed, 
and you could find the related programming information in the CoreSight Components Technical Reference Manual (available 
in References).
This chip supports 48-bit timestamping. The generator operates at a frequency of up to 320 MHz and gives a 64-bit 
timestamp value. .
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5180 / 5251


---
# 페이지 29

Generator at
320 MHz
64-bit output
Cortex-M7_0 (Timestamp)
[63:48] - GND
[47:0] - Tied to generator
Cortex-M7_1 (Timestamp)
[63:48] - GND
[47:0] - Tied to generator
Not available on the
S32K311 and S32K312
Cortex-M7_2 (Timestamp)
[63:48] - GND
[47:0] - Tied to generator
Only available
on S32K358
and S32K388
Cortex-M7_3 (Timestamp)
[63:48] - GND
[47:0] - Tied to generator
Only available
on S32K389 
and S32K388
Figure 568. Timestamp distribution network
82.14 Peripheral debug freeze register descriptions
Implement the logic provided in this section for each peripheral instance supporting the debug operation.
 
Debug freeze is enabled for all the peripherals so that as soon as the core halts, peripherals can be frozen to 
support debugging from the first instruction.
  NOTE  
For register details, refer to the following registers in the Device Configuration Module (DCM):
• Read Write GPR On Destructive Reset Register (DCMRWD6)
• Read Write GPR On Destructive Reset Register (DCMRWD7)
• Read Write GPR On Destructive Reset Register (DCMRWD8)
• Read Write GPR On Destructive Reset Register (DCMRWD9)
82.15 MDM_AP register descriptions
The debugger has access to the status and control elements implemented as registers in MDM_AP, which is selected by APSEL 
(6h) on the DAP bus. These registers provide additional control and status information for typical debug, cross-triggering, and 
run-control scenarios. Also, the register fields provide a way for the debugger to get the updated status of the core without initiating 
a bus transaction across the crossbar switch, thus remaining less intrusive during a debug session.
MDM_AP is accessible as DAP (see DAP TAP for details).
82.15.1 MDM_AP memory map
MDM_AP base address: 4025_0600h
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5181 / 5251


---
# 페이지 30

Offset
Register
Width
(In bits)
Access
Reset value
0h
Status (MDMAPSTTS)
32
R
F800_0000h
4h
Control (MDMAPCTL)
32
RW
0640_0000h
30h
WIR Enable (MDMAPWIREN)
32
RW
0000_0000h
38h
MDM AP WIR Release (MDMAPWIRREL)
32
RW
0000_0000h
82.15.2 Status (MDMAPSTTS)
Offset
Register
Offset
MDMAPSTTS
0h
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
CM72
DBG...
Reserv
ed 
CM71
DBG...
CM70
DBG...
CM73
DBG...
CM73
SLP...
CM73
DPS...
CM73
HLT 
CM0P
SLP...
CM72
SLP...
CM71
SLP...
CM70
SLP...
CM0P
DPS...
CM72
DPS...
CM71
DPS...
CM70
DPS...
W
Reset
1
1
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
HSEH
LT 
CM72
HLT 
CM71
HLT 
CM70
HLT 
Reserved 
FUNC
RST 
DEST
RST 
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
31
CM72DBGRST
RD
Cortex-M7_2 Debug Restarted
Indicates if Cortex-M7_2 has returned to Normal mode from Debug mode.
0b - In Debug mode
1b - In Normal mode
30
—
Reserved
29
Cortex-M7_1 Debug Restarted
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5182 / 5251


---
# 페이지 31

Table continued from the previous page...
Field
Function
CM71DBGRST
RD
Indicates if Cortex-M7_1 has returned to Normal mode from Debug mode.
0b - In Debug mode
1b - In Normal mode
28
CM70DBGRST
RD
Cortex-M7_0 Debug Restarted
Indicates if Cortex-M7_0 has returned to Normal mode from Debug mode.
0b - In Debug mode
1b - In Normal mode
27
CM73DBGRST
RD
Cortex-M7_3 Debug Restarted
Indicates if Cortex-M7_3 has returned to Normal mode from Debug mode.
0b - In Debug mode
1b - In Normal mode
26
CM73SLPNG
CM7_3 Sleeping
Indicates if Cortex-M7_3 is in Sleep mode.
0b - Not in Sleep mode
1b - In Sleep mode
25
CM73DPSLP
Cortex-M7_3 Deep Sleep
Indicates if Cortex-M7_3 is in Deep Sleep mode.
0b - Not in Deep Sleep mode
1b - In Deep Sleep mode
24
CM73HLT
CM7_3 Debug Halted
Indicates if Cortex-M7_3 is halted because of entry into Debug mode.
0b - Core is not halted
1b - Core is halted
23
CM0PSLPNG
Cortex-M0+ Sleeping
Indicates if Cortex-M0+ is in Sleep mode.
0b - Not in Sleep mode
1b - In Sleep mode
22
CM72SLPNG
CM7_2 Sleeping
Indicates if Cortex-M7_2 is in Sleep mode.
0b - Not in Sleep mode
1b - In Sleep mode
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5183 / 5251


---
# 페이지 32

Table continued from the previous page...
Field
Function
21
CM71SLPNG
CM7_1 Sleeping
Indicates if Cortex-M7_1 is in Sleep mode.
0b - Not in Sleep mode
1b - In Sleep mode
20
CM70SLPNG
Cortex-M7_0 Sleeping
Indicates if Cortex-M7_0 is in Sleep mode.
0b - Not in Sleep mode
1b - In Sleep mode
19
CM0PDPSLP
Cortex-M0+ Deep Sleep
Indicates if Cortex-M0+ is in Deep Sleep mode.
0b - Not in Deep Sleep mode
1b - In Deep Sleep mode
18
CM72DPSLP
Cortex-M7_2 Deep Sleep
Indicates if Cortex-M7_2 is in Deep Sleep mode.
0b - Not in Deep Sleep mode
1b - In Deep Sleep mode
17
CM71DPSLP
Cortex-M7_1 Deep Sleep
Indicates if Cortex-M7_1 is in Deep Sleep mode.
0b - Not in Deep Sleep mode
1b - In Deep Sleep mode
16
CM70DPSLP
Cortex-M7_0 Deep Sleep
Indicates if Cortex-M7_0 is in Deep Sleep mode.
0b - Not in Deep Sleep mode
1b - In Deep Sleep mode
15
HSEHLT
Cortex-M0+ Halted
Indicates if Cortex-M0+ is halted because of entry into Debug mode.
0b - Core is not halted
1b - Core is halted
14
CM72HLT
CM7_2 Debug Halted
Indicates if Cortex-M7_2 is halted because of entry into Debug mode.
0b - Core is not halted
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5184 / 5251


---
# 페이지 33

Table continued from the previous page...
Field
Function
1b - Core is halted
13
CM71HLT
CM7_1 Debug Halted
Indicates if Cortex-M7_1 is halted because of entry into Debug mode.
0b - Core is not halted
1b - Core is halted
12
CM70HLT
Cortex-M7_0 Halted
Indicates if Cortex-M7_0 is halted because of entry into Debug mode.
0b - Core is not halted
1b - Core is halted
11-3
—
Reserved
2
FUNCRST
Functional Reset
Indicates the system reset state.
0b - Not in functional reset
1b - In functional reset
1
DESTRST
Destructive Reset
Indicates the system reset state.
0b - Not in destructive reset
1b - In destructive reset
0
—
Reserved
82.15.3 Control (MDMAPCTL)
Offset
Register
Offset
MDMAPCTL
4h
Function
Allows the debugger:
• To give the destructive reset to the system. A system destructive reset enables this. The debugger also loses connection 
to the system with this reset.
• To hold the system in functional reset. A system functional reset enables this.
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5185 / 5251


---
# 페이지 34

 
• The trace functionality on trace pins is selected with this register and is retained across the functional reset.
• For S32K388, you must always write:
— Bitfields 18 and 19 in conjunction.
— Write bitfields 16 and 17 in conjunction if lockstep is enabled for Cortex-M7_0 and Cortex-M7_1.
• For S32K358, S32K348, S32K338, S32K328, S32K342, S32K341, S32K322, S32K344, S32K324, and 
S32K314, write bitfields 16 and 17 in conjunction if lockstep is enabled for Cortex-M7_0 and Cortex-M7_1. 
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
CM72
DBG...
Reserv
ed 
CM71
DBG...
CM70
DBG...
CM73
DBG...
Reserved 
SWOO
VRD 
CM7_3
_C...
TRIUO
VRD 
CM7_2
_C...
CM7_2
_C...
CM7_1
_C...
CM7_0
_C...
W
Reset
0
0
0
0
0
1
1
0
0
1
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
CM73
DBG...
DBGR
STF...
DBGR
STS...
Reserv
ed 
CM72
DBG...
CM71
DBG...
CM70
DBG...
Reserved 
SYSF
UNC...
SYSR
ESE...
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
CM72DBGRSR
T
Cortex-M7_2 Debug Restart
Indicates if a request to Cortex-M7_2 to leave the debug halt state is asserted.
0b - Normal operation
1b - Request asserted
30
—
Reserved
29
CM71DBGRSR
T
Cortex-M7_1 Debug Restart
Indicates if a request to Cortex-M7_1 to leave the debug halt state is asserted.
0b - Normal operation
1b - Request asserted
28
CM70DBGRSR
T
Cortex-M7_0 Debug Restart
Indicates if a request to Cortex-M7_0 to leave the debug halt state is asserted.
0b - Normal operation
1b - Request asserted
27
Cortex-M7_3 Debug Restart
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5186 / 5251


---
# 페이지 35

Table continued from the previous page...
Field
Function
CM73DBGRSR
T
Indicates if a request to Cortex-M7_3 to leave the debug halt state is asserted.
0b - Normal operation
1b - Request asserted
26-23
—
Reserved
22
SWOOVRD
SWO Override
Indicates if the SWO trace response is overriden. When SWO is not the selected trace sink target, you 
must override the trace response.
0b - Not overridden, and SWO generates the trace response
1b - Is overridden
21
CM7_3_CORE_
ACCESS
Debugger Access To Application Cortex-M7_3
Indicates if debugger access to Cortex-M7_3 across the functional reset phase is supported.
After programming the Cortex-M7_3 core debug logic, the debugger can write 1 to this field. Because of this, 
the clock gating control for CLK and FCLK of Cortex-M7_3 shifts to CCTL.
0b - Supported
1b - Not supported
20
TRIUOVRD
TPIU Override
Indicates if TPIU trace response is overridden. When TPIU is not the selected trace sink target, you must 
override the trace response.
0b - Not overridden, and TPIU generates the trace response
1b - Is overridden and asserted
19
CM7_2_CHK
Cortex-M7_2 Check
Indicates if debugger access to Cortex-M7_2 CHK across the functional reset phase is supported.
After programming the Cortex-M7_2 CHK core debug logic, the debugger can write 1 to this field. Because 
of this, the clock gating control for CLK and FCLK of Cortex-M7_2 CHK shifts to CCTL.
0b - Supported
1b - Not supported
18
CM7_2_CORE_
ACCESS
Debugger Access To Application Cortex-M7_2
Indicates if debugger access to Cortex-M7_2 across the functional reset phase is supported.
After programming the Cortex-M7_2 core debug logic, the debugger can write 1 to this field. Because of this, 
the clock gating control for CLK and FCLK of Cortex-M7_2 shifts to CCTL.
0b - Supported
1b - Not supported
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5187 / 5251


---
# 페이지 36

Table continued from the previous page...
Field
Function
17
CM7_1_CORE_
ACCESS
Debugger Access To Application Cortex-M7_1
Indicates if debugger access to Cortex-M7_1 across the functional reset phase is supported.
After programming the Cortex-M7_1 core debug logic, the debugger can write 1 to this field. Because of this, 
the clock gating control for CLK and FCLK of Cortex-M7_1 shifts to CCTL.
0b - Supported
1b - Not supported
16
CM7_0_CORE_
ACCESS
Debugger Access To Application Cortex-M7_0
Indicates if debugger access to Cortex-M7_0 across the functional reset phase is supported.
After programming the Cortex-M7_0 core debug logic, the debugger can write 1 to this field. Because of this 
scenario, the clock gating control for CLK and FCLK of Cortex-M7_0 shifts to CCTL.
0b - Supported
1b - Not supported
15
POR_WDG_DI
S_FUNC_RST
Power Watchdog Status
0b - Power watchdog is disabled
1b - Power watchdog is enabled
14
CM73DBGREQ
Cortex-M7_3 Debug Request
Drives the EDBGREQ input for Cortex-M7_3 and indicates if the debug request is generated. 
When the core goes into debug state, the field acknowledges that with a halted output signal (see 
MDMAPSTTS[CM73HLT]). If the core is in Stop mode, this field is used to wake up the core and 
transition it to the debug halt state.
0b - Debug request is not generated
1b - Debug request is generated
13
DBGRSTFAST
PAD
Debug Over Reset Via Fast Pads
Enables or diasables trace via fast pads. If enabled, the trace pads have trace over functional reset 
feature enabled. This field does not take care of the clock configuration.
0b - Disabled
1b - Enabled
12
DBGRSTSLOW
PAD
Debug Over Reset Via Slow Pads
Enables or diasables trace via slow pads. If enabled, the trace pads have trace over functional reset 
feature enabled. This field does not take care of the clock configuration.
0b - Disabled
1b - Enabled
11
—
Reserved
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5188 / 5251


---
# 페이지 37

Table continued from the previous page...
Field
Function
10
CM72DBGREQ
Cortex-M7_2 Debug Request
Drives the EDBGREQ input for Cortex-M7_2 and indicates if the debug request is generated. 
When the core goes into debug state, the field acknowledges that with a halted output signal (see 
MDMAPSTTS[CM72HLT]). If the core is in Stop mode, this field is used to wake up the core and 
transition it to the debug halt state.
0b - Debug request is not generated
1b - Debug request is generated
9
CM71DBGREQ
Cortex-M7_1 Debug Request
Drives the EDBGREQ input for Cortex-M7_1 and indicates if the debug request is generated. 
When the core goes into debug state, the field acknowledges that with a halted output signal (see 
MDMAPSTTS[CM71HLT]). If the core is in Stop mode, this field is used to wake up the core and 
transition it to the debug halt state.
0b - Debug request is not generated
1b - Debug request is generated
8
CM70DBGREQ
Cortex-M7_0 Debug Request
Drives the EDBGREQ input for Cortex-M7_0 and indicates if the debug request is generated. 
When the core goes into debug state, the field acknowledges that with a halted output signal (see 
MDMAPSTTS[CM70HLT]). If the core is in Stop mode, this field is used to wake up the core and 
transition it to the debug halt state.
0b - Debug request is not generated
1b - Debug request is generated
7-6
—
Reserved
5
SYSFUNCRST
System Functional Reset
Asserts or deasserts functional reset to the chip. The debugger maintains connection with the chip.
0b - Deasserted
1b - Asserted
4
SYSRESETRE
Q
System Destructive Reset
Asserts or deasserts destructive reset to the chip. The debugger also loses connection with this reset. 
When this field is reset, the entire system comes out of reset.
0b - Deasserted
1b - Asserted
3-0
—
Reserved
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5189 / 5251


---
# 페이지 38

82.15.4 WIR Enable (MDMAPWIREN)
Offset
Register
Offset
MDMAPWIREN
30h
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
PRVN
TRS...
LWPW
REN 
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
31-2
—
Reserved
1
PRVNTRSTEN
Prevent Reset Enable
Indicates if bit field PRVNTRSTRGM in register MDMAPWIRREL is capable of preventing MC_RGM 
from generating reset.
 
Reserved for S32K31x.
  NOTE  
0b - Automatic low power entry enabled
1b - Low power entry enabled controlled by bit field PRVNTRSTRGM of register 
MDMAPWIRREL.
0
LWPWREN
Low Power Debug Enable
Enables or disables low-power debug.
0b - Disabled
1b - Enabled
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5190 / 5251


---
# 페이지 39

82.15.5 MDM AP WIR Release (MDMAPWIRREL)
Offset
Register
Offset
MDMAPWIRREL
38h
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
PRVN
TRS...
WTRS
TRGM 
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
31-2
—
Reserved
1
PRVNTRSTRG
M
Prevent Reset
Indicates if MC_RGM is prevented from generating reset.
After TPIU flush, this field prevents MC_RGM from generating reset even if MC_RGM receives an 
acknowledge response from TPIU. This is valid for low-power entry.
0b - Normal operation
1b - MC_RGM prevented
0
WTRSTRGM
Wait In Reset B
Indicates if waiting of MC_RGM from generating reset is supported.
On exiting Standby mode, MC_RGM waits until the debugger writes to another field in the MDM_AP register 
to allow it to exit reset.
0b - Normal operation
1b - Wait supported
82.16 SDA_AP register descriptions
The debugger and system have access to secure authentication control and status, implemented as registers in SDA_AP 
on the DAP bus. These registers provide authentication control, authentication status, key exchange information, and debug 
enable controls.
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5191 / 5251


---
# 페이지 40

82.16.1 SDA_AP memory map
SDA_AP base address: 4025_4700h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Authentication Status (AUTHSTTS)
32
R
6000_0004h
4h
Authentication Control (AUTHCTL)
32
W
0000_0000h
10h - 2Ch
Key Challenge (KEYCHAL0 - KEYCHAL7)
32
R
See section
40h - 5Ch
Key Response (KEYRESP0 - KEYRESP7)
32
RW
0000_0000h
70h
User Identification 0 (UID0)
32
R
See section
74h
User Identification 1 (UID1)
32
R
See section
80h
Debug Enable Control (DBGENCTRL)
32
RW
See section
90h
Reset Control (SDAAPRSTCTRL)
32
RW
1E00_0000h
A0h
SDA_AP Generic Status (SDAAPGENSTATUS0)
32
R
0000_0000h
A4h
Generic Control 0 (SDAAPGENCTRL0)
32
RW
0000_0000h
B0h
SDA_AP Generic Status (SDAAPGENSTATUS1)
32
R
0000_0000h
C0h
SDA_AP Generic Status (SDAAPGENSTATUS2)
32
R
0000_0000h
D0h
SDA_AP Generic Status (SDAAPGENSTATUS3)
32
R
0000_0000h
E0h
SDA_AP Generic Status (SDAAPGENSTATUS4)
32
R
0000_0000h
FCh
Identity (ID)
32
R
001C_0040h
82.16.2 Authentication Status (AUTHSTTS)
Offset
Register
Offset
AUTHSTTS
0h
Function
Indicates the status of the authentication process.
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5192 / 5251


---
# 페이지 41

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
APPD
BGEN 
Reserved 
W
Reset
0
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
SWAP
PDBG 
UIDST
AT...
Reserv
ed 
CHAL
RDY 
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
1
0
0
Fields
Field
Function
31
—
Reserved
30
APPDBGEN
Application Debug Enabled or Disabled
Indicates:
• The status of application debug
• Whether CR is satisfied
• Whether access to other APs is allowed
0b - Application debug disabled
1b - Application debug enabled
29-4
—
Reserved
3
SWAPPDBG
Software Application Debug
Indicates:
• The status of software application debug
• Whether access to debug controls is allowed
0b - Software application debug disabled
1b - Software application debug enabled
2
UIDSTATUS
User Identification Status
Indicates:
• The status of UID
• Whether DCM has finished reading the flash memory user section
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5193 / 5251


---
# 페이지 42

Table continued from the previous page...
Field
Function
0b - UID is not ready and is invalid
1b - UID is ready and is valid
1
—
Reserved
0
CHALRDY
Challenge Ready
Indicates:
• The status of challenge ready when the value of export control is 0
• The status of the DCM_DONE signal if the value of export control is 1
0b - Challenge is not ready
1b - Challenge is ready
82.16.3 Authentication Control (AUTHCTL)
Offset
Register
Offset
AUTHCTL
4h
Function
Controls the authentication process.
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
W
Reserved 
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
W
Reserved 
HSEN
EWD...
HSEA
UTH...
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
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5194 / 5251


---
# 페이지 43

Fields
Field
Function
31-2
—
Reserved
1
HSENEWDATA
CTL
New Data Control
Indicates that the debugger has consumed the data registers. It is alright for the core to provide new 
data.
0b - Does not indicate that the debugger has consumed the data registers
1b - Indicates that the debugger has consumed the data registers
0
HSEAUTHREQ
Debug Enablement Authentication Request
Indicates that all key values are written and the chip can start the authentication request.
0b - Does not start the authentication request
1b - Starts the authentication request
82.16.4 Key Challenge (KEYCHAL0 - KEYCHAL7)
Offset
For a = 0 to 7:
Register
Offset
KEYCHALa
10h + (a × 4h)
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
KEYCHAL 
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
KEYCHAL 
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
1. The reset value of this register depends on NXP factory settings.
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5195 / 5251


---
# 페이지 44

Fields
Field
Function
31-0
KEYCHAL
Debug Enablement Key Challenge
82.16.5 Key Response (KEYRESP0 - KEYRESP7)
Offset
For a = 0 to 7:
Register
Offset
KEYRESPa
40h + (a × 4h)
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
KEYRESP 
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
KEYRESP 
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
31-0
KEYRESP
Debug Enablement Key Response
82.16.6 User Identification 0 (UID0)
Offset
Register
Offset
UID0
70h
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5196 / 5251


---
# 페이지 45

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
UID0 
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
UID0 
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
1. The reset value of this register depends on NXP factory settings.
Fields
Field
Function
31-0
UID0
User ID 0
Indicates the JTAG user ID bits of the lower word.
82.16.7 User Identification 1 (UID1)
Offset
Register
Offset
UID1
74h
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
UID1 
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
UID1 
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
1. The reset value of this register depends on NXP factory settings.
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5197 / 5251


---
# 페이지 46

Fields
Field
Function
31-0
UID1
User ID 1
Indicates the JTAG user ID bits of the upper word.
82.16.8 Debug Enable Control (DBGENCTRL)
Offset
Register
Offset
DBGENCTRL
80h
Function
Includes a special protection that allows access from Cortex-M0+ only if bit 30 of Authentication Status (AUTHSTTS) is 1.
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
CNIDE
N 
CDBG
EN 
Reserved 
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
Reserved 
GSPNI
DEN 
GSPID
EN 
GNIDE
N 
GDBG
EN 
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
1. The reset value is controlled by an export control enable input. If export control is enabled, the reset value of this register is 
FFFF_FFF0h. Otherwise, it is 0000_0000h.
Fields
Field
Function
31-30
—
Reserved
29
CNIDEN
Core Non-Invasive Debug Enable
Controls CNIDEN of debug blocks coupled with the Cortex-M7 core.
0b - Disabled
1b - Enabled
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5198 / 5251


---
# 페이지 47

Table continued from the previous page...
Field
Function
28
CDBGEN
Core Debug Enable
Controls CDBGEN of debug blocks coupled with the Cortex-M7 core.
0b - Disabled
1b - Enabled
27-8
—
Reserved
7
GSPNIDEN
Global Secure Privileged Non-Invasive Debug Enable
Controls GSPNIDEN of debug blocks coupled with Cortex-M7's subsystems, ETM, ITM, and CTI.
0b - Disabled
1b - Enabled
6
GSPIDEN
Global Secure Privileged Debug Enable
Controls GSPIDEN of debug blocks coupled with Cortex-M7's subsystems, ETM, ITM, and CTI.
0b - Disabled
1b - Enabled
5
GNIDEN
Global Non-Invasive Debug Enable
Controls GNIDEN of debug blocks coupled with Cortex-M7's subsystems, ETM, ITM, and CTI.
0b - Disabled
1b - Enabled
4
GDBGEN
Global Debug Enable
Controls GDBGEN of debug blocks coupled with Cortex-M7's subsystems, ETM, ITM, and CTI.
0b - Disabled
1b - Enabled
3-0
—
Reserved
82.16.9 Reset Control (SDAAPRSTCTRL)
Offset
Register
Offset
SDAAPRSTCTRL
90h
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5199 / 5251


---
# 페이지 48

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
RSTR
ELT...
RSTR
ELT...
RSTR
ELT...
RSTR
ELT...
Reserved 
W
Reset
0
0
0
1
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
31-29
—
Reserved
28
RSTRELTLCM7
3
Reset Release Cortex-M7_3
Indicates if the control signal released the reset for Cortex-M7_3. The reset is released to debug the core 
from first instruction.
The default value of this field is 1.
0b - Core is in reset
1b - Reset is released
27
RSTRELTLCM7
2
Reset Release Cortex-M7_2
Indicates if the control signal released the reset for Cortex-M7_2. The reset is released to debug the core 
from first instruction.
The default value of this field is 1.
0b - Core is in reset
1b - Reset is released
26
RSTRELTLCM7
1
Reset Release Cortex-M7_1
Indicates if the control signal released the reset for Cortex-M7_1. The reset is released to debug the core 
from first instruction.
The default value of this field is 1.
0b - Core is in reset
1b - Reset is released
25
RSTRELTLCM7
0
Reset Release Cortex-M7_0
Indicates if the control signal released the reset for Cortex-M7_0. The reset is released to debug the core 
from the first instruction.
Table continues on the next page...
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5200 / 5251


---
# 페이지 49

Table continued from the previous page...
Field
Function
The default value of this field is 1.
0b - Core is in reset
1b - Reset is released
24-0
—
Reserved
82.16.10 SDA_AP Generic Status (SDAAPGENSTATUS0 - SDAAPGENSTATUS4)
Offset
Register
Offset
SDAAPGENSTATUS0
A0h
SDAAPGENSTATUS1
B0h
SDAAPGENSTATUS2
C0h
SDAAPGENSTATUS3
D0h
SDAAPGENSTATUS4
E0h
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
SDAAPGENSTATUS 
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
SDAAPGENSTATUS 
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
31-0
SDAAPGENST
ATUS
DAP Generic Status
Is a generic status field for future use.
0b - Does not show generic status
1b - Shows generic status
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5201 / 5251


---
# 페이지 50

82.16.11 Generic Control 0 (SDAAPGENCTRL0)
Offset
Register
Offset
SDAAPGENCTRL0
A4h
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
JTAG_
CR...
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
31-1
—
Reserved
0
JTAG_CR_EN
JTAG CR Enable
Performs CR or password comparison based on SWJ-DP mode or JTAG mode. If you write 1 to this 
field, this function is performed using JTAG irrespective of SWJ-DP mode of the debugger.
0b - Function performed on the basis of SWJ-DP mode
1b - Function performed on the basis of JTAG mode
82.16.12 Identity (ID)
Offset
Register
Offset
ID
FCh
Function
 
This register does not generate the bus error on performing the write operation.
  NOTE  
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5202 / 5251


---
# 페이지 51

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
ID 
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
1
1
1
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
ID 
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
ID
Identity
82.17 Glossary
AHB
Advanced high-performance bus
AHB_AP
Advanced high-performance bus access port
APB
Advanced peripheral bus
APB_AP
Advanced peripheral bus access port
ATB
Advanced trace bus
ATBR
ATB replicator
CSTF
CoreSight trace funnel
DAP
Debug access port
DC
Design center
ETF
Embedded CoreSight funnels
JTAG-DP
JTAG debug port
MDM_AP
Miscellaneous debug module access port
MIC
Manufacturer identity code
PIN
Part identification number
PRN
Part revision number
SDA_AP
Serial data access port
SiP
System-in-package
SWJ-DP
Serial wire/JTAG debug port
TAP
Test and debug access port
TPIU
Trace port interface unit
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5203 / 5251


---
# 페이지 52

82.18 References
• Arm CoreSight SoC-400 Technical Reference Manual
https://developer.arm.com/documentation/100536/0302/?lang=en
• Arm CoreSight Architecture Specification
http://infocenter.arm.com/help/topic/com.arm.doc.ihi0029d/IHI0029D_coresight_architecture_spec_v2_0.pdf
• CoreSight Components Technical Reference Manual
http://infocenter.arm.com/help/topic/com.arm.doc.ddi0314h/DDI0314H_coresight_components_trm.pdf
• Arm Debug Interface Architecture Specification
https://developer.arm.com/documentation/ihi0031/g/?lang=en
NXP Semiconductors
Debug Subsystem
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5204 / 5251


---