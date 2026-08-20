# 페이지 1

Chapter 49
Safety Overview
49.1 Introduction
This chip family is developed following the ISO 26262 standards, with derivatives targeting to be operable in a system that fulfills 
the requirements of the ASIL D or ASIL B safety integrity levels. The S32K388, S32K389, and S32K358 can target an ASIL B 
safety integrity level with one portion of the chip, while targeting an ASIL D safety integrity level with another portion.
Table 270. ASIL levels
Chip
ASIL level
S32K388, S32K389, S32K358, S32K348, S32K344, S32K342, S32K341
D and B
S32K338, S32K328, S32K324, S32K314, S32K322, S32K312, S32K311, S32K310
B
The ASIL level targets the safety processing, which means the software functions are executed as intended:
1. Read instructions from memory.
2. Execute instructions.
3. Read data from memory.
4. Process data.
5. Write back the result data into memory.
Some elements of the safety concept are based on the assumption that the chip is connected to an external SBC or PMIC. 
The SBC or PMIC performs observations and control functionalities that are essential to fulfill some related functional safety 
requirements. If you do not use an SBC or PMIC, you must ensure that your S32K-family chip provides an equivalent functionality 
that properly manages the corresponding interface(s).
The following figure illustrates the safety interface between the chip and the SBC or PMIC.
aaa-038719
Voltage regulator
VDD output
External watchdog
SPI communication
RESET_b (bidirectional)
1) External reset source
2) Output to external subsystem
Internal chip safe state
Power supply
(VDD_HV_A, VDD_HV_B,
V1.5V)
Safety
interface
Chip
FCCU monitoring
FCCU_0
FCCU_1
Software-driven SPI communication
FCCU drives the EOUT pads
actively during functional reset if
1)
2)
dcf_client_utest_misc
[FCCU_EOUT_DEDICATED]
SW CONFIG (FCCU-CFG)
FCCU_0
FCCU_1
Internal PMC:
Internal voltage
generation: 1.1 V, 2.5 V,
redundant LVDs,
and single HVDs
MC_RGM
Figure 204. Safety interface between the chip and the SBC or PMIC
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1918 / 5251


---
# 페이지 2

In the safety context, the chip interfaces can be classified into the groups shown in the table.
Table 271. Chip interface groups
Interface
Description
Power supply
This interface is between the SBC and the chip. It ensures 
that the supply to the chip is in the correct range. In case 
of any low-voltage event, the chip has POR, LVR, and LVD 
circuits in place and in case of any HVD event, the chip 
raises an interrupt. The SBC must ensure that the voltage 
regulator outputs never exceed the allowed range (more 
specifically for HVD range).
Communication
Responsible for communication between the SBC and the 
chip. Though the chip supports multiple communication 
protocols (UART, LIN, SPI, I2C, FlexCAN, and so on), SPI 
is the preferred communication with SBC. This is relevant to 
initialize an external watchdog when the chip is inoperative 
for a considerably long time (this is indicated by the pin states 
of the communication interface).
Reset
The chip consists of a reset bidirectional pin interfaced with 
SBC. The SBC can initiate a chip reset via this pin as a 
safety reaction in case of:
• Extreme critical faults
• An inoperative chip
• Stuck cases based on the criticality and the application 
requirements
The SBC also samples the reset pin state to identify the chip 
condition (whether in running state or in reset).
FCCU
The chip indicates the chip faults to the SBC via FCCU 
EOUT pins through this interface.
The interfaces in Table 271 ensure the chip's operational safety and integrity.
49.2 Safety architecture elements
The chip safety architecture consists of following elements that operate in an interconnected way to meet the ASIL requirements:
• Cortex-M7 core complex (including the cache controllers) operating in delayed lockstep (ASIL D only)
• eDMA controller
• Internal windowed watchdogs with independent clock sources
• Power supply monitoring with redundant low-voltage detectors, single high-voltage detectors, and internal ADC connection 
to check the internal voltages during application
• Robust clock monitoring, including PLL loss of lock detection
• Embedded flash memory with ECC SECDED and address encoding (parallel address path) check
• System RAM with ECC SECDED and error detection
• Cortex-M7 cache memories with ECC SECDED
• Peripherals memories (EMAC, FlexCAN) with ECC SECDED
NXP Semiconductors
Safety Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1919 / 5251


---
# 페이지 3

• End-to-End EDC (E2E EDC), with address encoding and monitoring of the control signals done by a dedicated module 
(EDC interface gaskets and XBIC). This ensures the safety of storage operations and of the data path to the internal 
storage (RAM, flash memory, core cache) and peripherals across the crossbar switch. See the XBIC chapter for details.
• Hardware CRC module that supports end-to-end data check integrity for any data transfer in the system (SRAM to 
peripherals via DMA transfer, external interfaces to SRAM/peripherals, and so on)
• Cortex-M7 MPUs
• XRDC for memory and peripheral protection
• AIPS_Lite peripheral protection with trusted master-slave connection
• Register protection mechanism for safety-critical registers
• On-chip temperature sensor for temperature monitoring
• Hardware self-test that can be triggered by software:
— LBIST to detect latent faults in functional logic as well as in safety integrity mechanisms
 
LBIST is not supported in S32K312, S32K311, and S32K310.
  NOTE  
— MBIST to ensure integrity of the memories in the chip (SRAM, ITCM, DTCM, peripheral memories, and so on)
• ADC self-test
• FCCU for error collection and reaction, including reporting error status to system; FCCU supports these programmable 
reaction types:
— Interrupt
— Functional reset
• Error pads indicate the chip's internal state to the external chip interface or SBC.
• EIM to inject errors into the memories and interface gaskets to verify the error-detection features of the memory controllers 
and the interface gaskets
• ERM to collect diagnostic information from memory controllers in case of an error event
These hardware elements can be supported by software safety measures, for example a structural core self-test or the 
check-the-checker software library.
49.3 I/O peripherals
The arrangement of I/O peripherals across peripheral bridges allows redundant use of peripherals while limiting possible causes 
of CCF. Redundant use includes using equivalent peripherals in a replicated way as well as using functionally different peripherals 
in, for example, feedback measurement loops. Comparison of redundant operation is the responsibility of the application software, 
not the safety hardware mechanism.
The peripherals are distributed evenly across the peripheral bridges (AIPSn), except for singular modules like EMAC, QuadSPI, 
and so on.
 
EMAC and QuadSPI are not present in S32K312 and S32K311.
  NOTE  
49.4 Self-test
The chip supports a self-test operation. Your safety software must initiate the self-test operation by configuring STCU2; the chip 
does not initiate it. STCU2 then controls the self-test operation. Self-test supports both MBIST and LBIST. After the self-test 
operation completes, the chip enters a reset sequence. Self-test results are stored in STCU2 and your safety software can read 
the results after the reset sequence.
NXP Semiconductors
Safety Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1920 / 5251


---
# 페이지 4

Figure 205 depicts the processing steps related to the self-test operation, and its linkage to the chip reset and an application start. 
You decide whether to run a self-test or to skip it before starting an application. You must also specify the self-test configuration 
before relinquishing control to STCU2 for performing the self-test operation. This processing finishes by reentering the chip 
reset sequence, depending on whether the chip encountered an unrecoverable fault during the self-test operation. When an 
unrecoverable fault is encountered during the self-test operation, the chip enters a reset sequence by performing a destructive 
reset. When no such fault is encountered, the self-test operation completes by entering the chip sequence with a functional reset 
sequence. You can prevent reset cycling by limiting the amount of resets permitted; the chip shuts down when this limit has been 
reached. See the "Functional reset escalation" and "Destructive reset escalation" sections in the MC_RGM chapter.
Destructive reset
sequence
Software checks the
LBIST or MBIST results
Power-on reset
Functional reset
sequence
Software configures STCU2
for self-test execution.
Chip reset sequence
Self-test completion results in a functional reset.
STCU2 encounters an unrecoverable fault and
generates a destructive reset.
STCU2 is under destructive reset.
The self-test configurations and the results
(assuming self-test execution was successful)
remains preserved across self-test within STCU2.
Out of reset
Too many resets?
Yes
No
No
Yes
STCU2 executes
LBIST or MBIST
Software reads STCU2
and MC_RGM registers.
Software decides:
run the self-test?
Is previous reset
due to self-test?
Yes
Chip shutdown
No
Does STCU2
encounter any
unrecoverable
fault?
No
Yes
Software starts application
execution
Figure 205. LBIST/MBIST execution
Figure 206 visualizes the top-level partitioning of the chip. The chip consists of two partitions, Run and Standby.
NXP Semiconductors
Safety Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1921 / 5251


---
# 페이지 5

• Run: This partition consists of logic which is present in switchable domain and is shut off (has no supply) while the chip 
operates in low-power (Standby) mode.
• Standby: This partition consists of always-on logic which is functional even while the chip operates In low-power 
(Standby) mode.
The Run partition also contains the control logic that is essential for the chip self-test operation, as well as blocks that undergo 
self-test. The chip consists of a single LBIST partition, which is a subpartition within the Run partition. The LBIST subpartition 
contains the logic over which self-test is executed. The logic outside the LBIST subpartition and within the Run partition consists 
of the LBIST control logic as well as logic which does not undergo LBIST.
The Standby partition cannot participate in the LBIST of the Run partition because it is a different partition of the chip. Any module 
within the Standby partition is therefore excluded from the LBIST. The components within the Standby partition are listed within 
the section "Chip power domain partitioning" in the "Power Management" chapter.
LBIST
Run
Standby
1
1. LBIST is not supported on S32K312, S32K311, and S32K310
Figure 206. S32K3xx chip top-level partition view
See "STCU2 LBIST/MBIST mapping" in the STCU chip-specific section for modules participating in the LBIST operation.
 
REG_PROT of an IP undergoes (or does not undergo) LBIST in conjunction with the protected module that 
undergoes (or does not undergo) LBIST.
  NOTE  
The modules that are vital to the self-test operation are excluded from LBIST regions to allow LBIST to execute successfully.
You must run self-test with PLLDIG configured as the system clock. The LBIST clock controller controls the clock during serial 
shift, but returns clock control to the functional nodes during the self-test.
49.5 Glossary
ASIL
Automotive safety integrity level. This is a risk classification scheme as defined by ISO 26262 for automotive 
standard.
CCF
Common cause failure
DTCM
Data tightly coupled memory
ECC
Error correction code
EDC
Error detection code
ITCM
Instruction tightly coupled memory
LBIST
Logic built-in self-test
MBIST
Memory built-in self-test
NXP Semiconductors
Safety Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1922 / 5251


---
# 페이지 6

PLL
Phase-locked loop oscillator
PMIC
Power management integrated chip
SECDED Single error correction, Double error detection
SBC
System basis chip
NXP Semiconductors
Safety Overview
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1923 / 5251


---