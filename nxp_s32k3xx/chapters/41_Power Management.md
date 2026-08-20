# 페이지 1

Chapter 41
Power Management
41.1 Introduction
The power management system generates, monitors, and controls power supplies and related resets. This chapter describes the 
system's interaction with other peripherals.
The power management system includes the modules listed below.
Table 247. Power management system modules and their functions
Part
Function
MC_ME
Initiates entry into Low-Power mode
MC_PCU
Controls entry into and exit from Low-Power mode
PMC
Regulates and monitors power supplies of the Run and the 
Standby domains
MC_RGM
Ensures a clean state and correct Run domain functionality by 
controlling the reset sequence
FIRC, WKPU, and other chip peripherals
Controls Standby mode wake-up and operations in Run and 
Standby modes
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1659 / 5251


---
# 페이지 2

41.1.1 Power management system for S32K344, S32K324, S32K314, S32K341, S32K342, and 
S32K322
VDD_HV_A
V25
V11_RUN
VSS
ADC_n
VREFH
VREFL
Flash
memory
PMC
V25
 
(Double bond)
GPIO
Pads
VDD_HV_A
VSS
SW*
V11
 
(Double bond)
V11_STANDBY
V11_STANDBY
Registers
SOG
(Standby)
WKPU
MC_PCU
MC_RGM
32 K
SRAM
PIT_0
(RTI)
DCM
SOG
(Run)
LPCMP_n
FXOSC
SIRC
FIRC
SXOSC
PLLDIG
TempSense
RTC
- Standby domain
- Standby domain (optional)
- On during FPM (Run mode) only
SW*
B
VDD_HV_B
Optional
V15
VRC_CTRL
VC_BJT
 
Last Mile
distributed
regulator
FPM
Boot
GPIO
Pads
VDD_HV_B
VSS
LPM
V11_STANDBY
COUT_V15
Figure 171. Power management system for S32K344, S32K324, S32K314, S32K341, S32K342, and S32K322
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1660 / 5251


---
# 페이지 3

41.1.2 Power management system for S32K312 and S32K311, and S32K310
FPM
LPM
Not available 
in the S32K311
VDD_HV_A
V25
V11_RUN
VSS
ADC_n
VREFH
VREFL
Flash
memory
PMC
V25
 
(Double bond)
GPIO
Pads
VDD_HV_A
VSS
SW*
V11
 
(Double bond)
V11_STANDBY
V11_STANDBY
Registers
SOG
(Standby)
WKPU
MC_PCU
MC_RGM
32 K
SRAM
PIT_0
(RTI)
DCM
SOG
(Run)
LPCMP_n
FXOSC
SIRC
FIRC
SXOSC
PLLDIG
TempSense
RTC
- Standby domain
- Standby domain (optional)
- On during FPM (Run mode) only
SW*
B
Figure 172. Power management system for S32K312 and S32K311, and S32K310
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1661 / 5251


---
# 페이지 4

41.1.3 Power management system for S32K358/S32K348/S32K338/S32K328
SMPS
Flash
memory
LPCMP_n
FXOSC
SIRC
FIRC
SXOSC
Registers
- Standby domain
- Standby domain (optional)
- On during FPM (Run mode) only
PLLDIG0
MC_RGM
WKPU
MC_PCU
PIT_0
(RTI)
SOG
(Run)
SRAM
64 kB
RTC
DCM
PLLDIG1
TempSense
SOG
(Standby)
ADC_n
LPM
PMC
LPM (V15)
V11_STANDBY
V25
V11_RUN
V11_STANDBY
V11_STANDBY
(Triple bond)
Last Mile
distributed
regulator
FPM
SW*
SW*
optional
SMPS Option [See footnotes]
VIN
VC_BJT
VDD_HV_A
VREFH
VREFL
V11
V25
VSS
VSS_DCDC
PMOS_CTRL
VDD_DCDC
VDD_HV_B
VRC_CTRL
Pads
GPIO
VDD_HV_A
VSS
Pads
GPIO
VDD_HV_B
VSS
(Triple bond)
V15
[See footnotes]
The V15 input voltage can be supplied directly by an SBC or Voltage regulator. The S32K3x8 devices provide two options to derive the V15 regulator from the 5V or 3.3V supply.
Option 1: A DC/DC converter (SMPS) regulator can be implemented by connecting the external components (PMOS, inductor, diode) shown in the figure above, at pins VDD_DCDC,
PMOS_CTRL, and VSS_DCDC. In this case, VRC_CTRL must not be connected. VDD_DCDC must be connected to the VDD_HV_A or VDD_HV_B, supply voltage. In this
option COUT_V15 is specified in SMPS regulator electrical specifications.
VRC_CTRL pin must be connected to the base of the transistor. In this case, VDD_DCDC, PMOS_CTRL must not be connected. VSS_DCDC must be connected to MCU GND.
Option 2: A linear regulator can be implemented by connecting a bipolar NPN transistor from the VDD_HV_A or VDD_HV_B, supply voltage shown as VC_BJT in the figure above. The
COUT_V15
In this option, COUT_V15 is specified in Recommended decoupling capacitors.
V15
PMIC Option
Note: In the EP package, you must connect the exposed pad to ground (VSS).
Figure 173. Power management system for S32K358/S32K348/S32K338/S32K328
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1662 / 5251


---
# 페이지 5

41.1.4 Power management system for S32K388/S32K389
SMPS
Flash
memory
LPCMP_n
FXOSC
SIRC
FIRC
SXOSC
Registers
- Standby domain
- Standby domain (optional)
- On during FPM (Run mode) only
PLLDIG0
MC_RGM
WKPU
MC_PCU
PIT_0
(RTI)
SOG
(Run)
SRAM
64 kB
RTC
DCM
PLLDIG1
TempSense
SOG
(Standby)
LPM
PMC
LPM (V15)
V11_STANDBY
V25
V11_RUN
V11_STANDBY
(Triple bond)
Last Mile Regulator 
External NFET
FPM
SW*
SW*
SMPS Option
VIN
VDD_HV_A
VREFH
SARADC_n
VREFL
V11
V25
VSS
VSS_DCDC
PMOS_CTRL
VDD_DCDC
VDD_HV_B
Pads
GPIO
VDD_HV_A
VSS
Pads
GPIO
VDD_HV_B
VSS
(Triple bond)
V15
V11
NMOS_CTRL
V15
PMIC Option
Figure 174. Power management system for S32K388/S32K389
41.1.5 Features
• For S32K310, S32K311, S32K312, PMC uses VDD_HV_A to generate 1.1 V (nominal) supply for the core logic 
(V11_RUN).
• For other chips, PMC uses a 1.5 V supply to generate 1.1 V (nominal) supply for the core logic (V11_RUN).
• S32K358/S32K348/S32K338/S32K328, S32K342/S32K322/S32K341, S32K344/S32K324/S32K314 includes a linear 
regulator to use an optional external ballast (BJT) and VRC_CTRL output for 1.5 V generation.
• Supports a low-power regulator (LPM) supplying core logic during Standby mode (V11_STANDBY)
• Includes 1.1 V FPM regulator options for driving the logic in RUN mode (V11_RUN) from a 1.5V supply:
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1663 / 5251


---
# 페이지 6

— Boot LDO for S32K344/S32K324/S32K314, S32K342/S32K322/S32K341
— Internal Last-mile (FPM) for S32K344/S32K324/S32K314, S32K342/S32K322/S32K341, S32K358/S32K348/
S32K338/S32K328
— External Last-Mile (FPM) for S32K388/S32K389
• Supports power switches to isolate voltage islands and configure the chip in Standby mode
• S32K358/S32K348/S32K338/S32K328/S32K388/S32K389 supports a DC-DC buck converter stage, with a dedicated pin 
to control an external Power MOSFET, in the range from 1.4V to 1.5V.
• S32K388/S32K389 controls an external NMOS transistor, and uses V15 generated from SMPS as input to generate V11 
for a load current up to 1.5 A (disabled in Standby mode).
• Includes a linear regulator that generates a 2.5 V supply (V25) from VDD_HV_A
• Supports voltage monitors ensuring transitions to a safe state (POR) when a supply is out of a valid range
• Controls power-mode transitions through an interaction with the digital interface
• Offers a padkeeping feature that retains PAD state during standby mode till software boots up
• Provides separate ADC reference supplies (VREFH and VREFL)
41.1.6 Operational power modes
This chip has two power modes:
• Run mode (FPM): Main operation mode with full chip performance and a higher current consumption as compared to 
Standby mode.
• Standby mode (LPM): Low-performance mode of the chip in which the Run domain is turned off. The cores and most 
peripherals are off in this mode.
The boot regulator manages the chip during the booting process except S32K3x8, S32K312, S32K311 and S32K310.
The last-mile regulator is the full-performance regulator, which you enable for running applications. The upcoming sections 
discuss the sequence to enable or disable the regulator.
The LPM regulator manages the chip in Standby mode.
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1664 / 5251


---
# 페이지 7

41.1.7 External 1.5 V source
Power supply
5 V
S32K3xx
VDD_HV_B
1.5 V
V15
VDD_HV_A
Power supply
3.3 V
S32K3xx
VDD_HV_B
1.5 V
V15
VDD_HV_A
Power supply
3.3 V
5 V
S32K3xx
VDD_HV_B
1.5 V
V15
VDD_HV_A
Figure 175. Core supply from external 1.5 V source (except for S32K388, S32K389, S32K312, S32K311, S32K310)
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1665 / 5251


---
# 페이지 8

41.1.8 External 1.5 V source (applicable for S32K388/S32K389)
Power supply
5 V
S32K388/S32K389
VDD_HV_B
VDD_HV_A
Power supply
3.3 V
S32K388/S32K389
VDD_HV_B
VDD_HV_A
Power supply
3.3 V
5 V
S32K388/S32K389
VDD_HV_B
VDD_HV_A
1.5 V
V15
PMOS_CTRL
V11
1.5 V
V15
PMOS_CTRL
V11
1.5 V
V15
PMOS_CTRL
V11
Figure 176. Core supply from external 1.5 V source, with external last-mile regulator (applicable for S32K388/
S32K389)
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1666 / 5251


---
# 페이지 9

41.1.9 Using a BJT for 1.5 V generation (not applicable for S32K388, S32K389, S32K312, S32K311, 
and S32K310)
Power supply
5 V
S32K3xx
VDD_HV_B
VRC_CTRL
V15
VDD_HV_A
Power supply
3.3 V
S32K3xx
VDD_HV_B
VRC_CTRL
V15
VDD_HV_A
Power supply
3.3 V
5 V
S32K3xx
VDD_HV_B
VRC_CTRL
V15
VDD_HV_A
Figure 177. Using a BJT for 1.5 V generation
41.2 Power-up sequence
Figure 178 shows the reset sequence for a power-up or Standby mode event. This sequence starts from the POR phase. For the 
Run domain logic, Standby mode exit operation is same as power-up.
See the "Reset Overview" chapter for more information about the chip reset sequence.
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1667 / 5251


---
# 페이지 10

Chip
power-up
Keep chip in POR
Power-on reset
V > VtPOR
Yes
No
Yes
Continue to application
FIRC powers on
Wait for FIRC stabilization
Destructive reset
sequence proceeds
Yes
Functional reset
sequence proceeds
Flash memory initialization
Flash memory scanning
Trim loading
Change FIRC_DIV to DIV1
Enable FXOSC, PLL (Configurable)
Boot header parsing
XRDC configurations
CAAM_RNG initialization
Debug authorization
CAAM_RNG initialization
OS initialization
HSE_FW initialization code
Application boot
Security functions disabled
Standby
exit?
No
Chip out of reset in normal Run mode
Security functions enabled
sBAF initialization code
HSE_FW verification
STANDBY_ENTRY_SW1
Peripheral shutdown
STANDBY_ENTRY_SW4
Main core shutdown
STANDBY_ENTRY_SW2
Application core shutdown
lsolations in between Run and
standby logic enabled
Wake-up sequence proceeds with
PMC moving to run regulation 
MC_RGM asserts all
resets to Run domain
PMC moves to LPM regulator
and device enters standby
Run-domain POR
sequence proceeds
Run-domain destructive
reset sequence proceeds
Run-domain functional
reset sequence proceeds
STANDBY_ENTRY_SW3
Flash memory or PMC
low-power handshake
Secure
boot?
No
sBAF enabling application core
Standby recovery initialization
Application core VTOR change
HSE_FW boot
Execute self-test
Hardware
HSE_B sBAF
HSE_B firmware
Application core
software
Yes
no
Wake-up
event detected
Remain in
Standby mode
Yes
Legend:
Trigger
self-test?
No
HSE_FW enabling application core
Continue to standby
software entry
Yes
Enter
Standby mode
No
Run
Standby
Destructive reset
Functional reset
Run
Fast standby exit
Yes
Figure 178. Power-up sequence
41.3 PMC last-mile regulator auto-enable feature (applicable for S32K344, S32K324, 
S32K314, S32K341, S32K342, and S32K322)
PMC includes an automatic last-mile auto-enable feature. After starting on boot regulator, this feature allows automatic switch over 
to last-mile regulator if 1.5 V is present during:
• Chip startup
• Standby mode recovery
You can control the PMC last-mile regulator by appropriately configuring:
• PMC.CONFIG[LMAUTOEN] field
• PMC.CONFIG[LM_EN] field
For more information, see the descriptions of these fields in PMC.CONFIG register.
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1668 / 5251


---
# 페이지 11

 
You must write 1 to PMC.CONFIG[LM_EN] field before transtioning to faster clock frequencies irrespective of 
the setting of PMC.CONFIG[LMAUTOEN] field. This is because of the reduced clock speed when using the 
boot regulator.
  NOTE  
41.3.1 Last-mile regulator with 1.5 V from an external source (applicable for S32K344, S32K324, 
S32K314, S32K341, S32K342, and S32K322)
Table 248. Last-mile regulator with 1.5 V from an external source
Operating condition
Last-mile regulator operation
After POR
Boots on boot regulator and then automatically switches to the last-mile regulator
After destructive reset
Remains on last-mile regulator
 
If the destructive reset source is low voltage reset on 1.1 V then 
switchback happens from last-mile to boot regulator for boot.
  NOTE  
After functional reset
Remains on last-mile regulator
After PMC.LVSC[LVD15S] field 
becomes 1
Switches, automatically, to the boot regulator to configure clocks for slow speed
41.3.2 Last-mile regulator using a BJT (applicable for S32K344, S32K324, S32K314, S32K341, 
S32K342, and S32K322)
Table 249. Last-mile regulator using a BJT
Operating condition
Last-mile regulator operation
After POR
Boots on boot regulator; switches to the last-mile regulator post reset when the Cortex-M7 
core configures the software on FIRC
After destructive reset
Switches to boot regulator to check reset propagation delay
After functional reset
Remains on last-mile regulator
After PMC.LVSC[LVD15S] 
field becomes 1
Switches, automatically, to boot regulator to configure clocks for slow speed
41.4 PMC last-mile regulator auto-enable feature (applicable for S32K358, S32K348, 
S32K338 and S32K328)
PMC includes an automatic last-mile auto-enable feature.
You can control the PMC last-mile regulator by appropriately configuring:
• PMC.CONFIG[LM_EN] field
For more information, see the descriptions of these fields in PMC.CONFIG register.
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1669 / 5251


---
# 페이지 12

41.4.1 Last-mile regulator with 1.5 V from an external source (applicable for S32K358, S32K348, 
S32K338 and S32K328)
Table 250. Last-mile regulator with 1.5 V from an external source
Operating condition
Last-mile regulator operation
After POR
Waits for 1.5 V to start last-mile regulator
After destructive reset
Remains on last-mile regulator
After functional reset
Remains on last-mile regulator
41.4.2 Last-mile regulator using a BJT (applicable for S32K358, S32K348, S32K338 and S32K328)
Table 251. Last-mile regulator using a BJT
Operating condition
Last-mile regulator operation
After POR
Wait for 1.5 V, if it is at sustained level, PMC starts the last-mile regulator
After destructive reset
Remains on last-mile regulator
After functional reset
Remains on last-mile regulator
41.5 Standby mode entry sequence
The Standby mode entry sequence includes three phases of operation:
• Standby mode entry configuration phase or software Standby mode entry sequence
• Standby mode entry handshake phase or hardware Standby mode entry sequence
• Standby mode entry or PMC Standby mode entry
 
The Standby mode entry sequence described in this section is the only supported sequence. Contact NXP support 
if you require an alternate Standby mode entry sequence.
  NOTE  
 
In S32K388/S32K389, after triggering Standby Entry from Application, if Reset is asserted before Standby entry 
then reset can be issued to system, which will be visible at RESET_B pad.
  NOTE  
 
When "PMIC Handshake with MCU" is not used, to be able to exit from STANDBY mode, 
PMIC_PGOOD_HNDSHK_BYP must be set to 1.
  NOTE  
41.5.1 Software Standby mode entry sequence
The Standby mode entry sequence includes chip configuration as described in the following sections.
Before entering the software Standby mode sequence, the system clock source must be changed to FIRC at 48 MHz because 
PLLDIG is not available in Standby mode. In Standby mode, all clock sources can be optionally disabled (including FIRC, which 
results in a no-clock, low-power consumption mode). You could also use FXOSC, if enabled, when the 2.5 V supply is available 
by appropriate configuration of PMC.CONFIG[LPM25EN].
The software Standby mode entry sequence consists of four steps:
1. SW1: Module shutdown process
2. SW2: Application core shutdown process
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1670 / 5251


---
# 페이지 13

3. SW3: Flash memory low-power handshake and PMC last-mile regulator control[9]
4. SW4: Main core shutdown process
These processes are described in detail in the sections that follow. See Figure 178 that shows the relationship between these four 
steps in a flow diagram.
41.5.1.1
SW1: Module shutdown process
I/O and module configuration for Standby mode discusses the procedure to configure I/O and the chip modules for Standby mode.
The entry sequence for this mode includes module clock disabling steps (see the "Clocking" chapter for module clock turn on and 
turn off processes). You must use MC_ME.PRTNn_COFBm_CLKEN[REQp] fields to enable or disable module clocks. 
41.5.1.1.1
Disabling modules
Disable modules by configuring the appropriate fields in their registers for Standby mode operation. See specific module chapters 
for more information.
The Standby mode entry sequence includes the module clock disabling step, with which you can disable the modules that you do 
not need for Standby mode operation.
The sequence of disabling modules is shown in I/O and module configuration for Standby mode.
 
While enabling or disabling the modules, you must verify that the module is disabled when you read 
MC_ME.PRTNn_COFBm_STAT register and the module disable field, if applicable. In case of a discrepancy, you 
must perform proper diagnostic steps.
You must clear the I/O controls for the pads that you do not require in Standby mode (OBE, IBE, and so on). This 
avoids any unwanted pad keeping settings. See Pad keeping for more information on the chip pad keeping process.
For any standby wake source, if an interrupt occurs it must be disabled before entering Standby mode and only the 
wake up event of that source must be enabled. This is to avoid any SW conflict in the interrupt handling for multi 
application core cases.
  NOTE  
The MC_ME.PRTNn_COFBm_STAT register indicates the status of peripheral clock enable or disable. It may take up to three 
clock cycles for MC_ME.PRTNn_COFBm_STAT register to update after MC_ME.PRTNn_COFBm_CLKEN register is updated.
Once modules are disabled by following above steps:
• Switch to FIRC as the system clock.
• Disable FXOSC and wait for clock status.
• Configure Standby Entry.
[9] Not applicable for S32K388/S32K389.
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1671 / 5251


---
# 페이지 14

41.5.1.1.2
I/O and module configuration for Standby mode
Initiate Standby sequence
Application core shutdown
Clear all pending interrupts
Disable all communications
(QuadSPI, EMAC, and so on)
As needed, configure the associated
MC_ME.PRTNn_COFBm_CLKEN
fields for Standby mode
Have all
communications
stopped?
Yes
Need fast startup
of FXOSC_CLK after
Standby exit?
Yes
No
Configure entire chip to
only use FIRC_CLK
Configure FXOSC_CLK for
operation after Standby mode
Write 1 to
PMC.CONFIG[LPM25EN]
Configure module registers
used in Standby mode
Verify PMC.CONFIG[LPM25EN]
equals 0 disabling 2.5 V
during Standby mode
Write 1 to SIUL2.MSCRn[PKE]
of the I/O that you want active in
Standby mode
Configure SIUL2.MSCR
for the function of the I/O
during Standby mode
Write 0 to
DCM.DCMRWF1[STANDBY_IO_CONFIG]
to enable padkeeping
Are all necessary
MC_ME.PRTNn_COFBm_STAT
fields 0?
Yes
No
No
See the ‘’Padkeeping’’
section for details.
Not recommended if
minimum power
consumption is needed.
Use if faster FXOSC
start is required.
Before switching to
FIRC_CLK, you must
take the necessary
precautions to avoid
clock glitches.
Figure 179. I/O and module configuration for Standby mode
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1672 / 5251


---
# 페이지 15

41.5.1.2
SW2: Application core shutdown process
The application cores(s) execute a WFI (as opposed to the main core running the Standby mode entry sequence). See the section 
"Application core shutdown" in the MC_ME chapter for more information.
The main core configuration (programming valid core ID and enabling standby entry process) and wake-up source configuration 
must also be set in SW2, so that SW4 contains only the main core WFI execution.
41.5.1.3
SW3: Flash memory low-power handshake and PMC last-mile regulator
In this process, you execute a flash memory low-power handshake and disable the PMC last-mile regulator by executing the 
procedures indicated in Figure 180 and Figure 181.
Initiate a flash memory 
handshake to cofirm no high 
voltage operations are in process
High voltage
flash memory operation
in progress?
Yes
No
Flash memory 
disable
Disable PLLDIG by writing zero
to PLLDIG.PLLCR[PLLPD]
PLLDIG off during
Standby mode.
Configure SIRC, FXOSC, and
SXOSC as needed for Standby
mode
FIRC.STDBY_ENABLE[STDBY_ENABLE]
SIRC.MISCELLANEOUS_IN[STANDBY_ENABLE]
FXOSC.CTRL[OSCON]
SXOSC.SXOSC_CTRL[OSCON]
Configure the V25 regulator for
operation in Standby mode
DCMRWF2[PMC_TRIM_RGM_DCF_BYP_STDBY_EXT]=1;
DCMRWF2[FIRC_TRIM_BYP_STDBY_EXT]=1;
DCMRWF2[DCM_SCAN_BYP_STDBY_EXT]=1;
Configure the following DCM register fields as needed:
Notes: 
DCM configuration above present compliant to achieve the typical tMODE_STDBYEXIT_FAST time
Continue Standby
mode entry process
Figure 180. Flash memory Standby mode configuration
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1673 / 5251


---
# 페이지 16

 
Disable the last-mile regulator according to the Last-mile regulator disable sequence (not applicable for S32K3x8, 
S32K312, S32K311 and S32K310).
  NOTE  
41.5.1.3.1
Last-mile regulator disable sequence (not applicable for S32K3x8, S32K312, S32K311 and S32K310)
Simultaneously write 0 to both
PMC.CONFIG[LMEN] and
PMC.CONFIG[LMBCTLEN]
Software writes GPIO indicating
last-mile regulator is disabled
External source disables
BJT collector voltage
Continue Standby mode
disable process
Disable PMC
last-mile regulator
Figure 181. Last-mile regulator disable sequence
When exiting Standby mode, the 1.1 V capacitor is charging. You can charge the 1.5 V capacitor during or after the 1.1 V capacitor 
is charged. If you charge the 1.5 V capacitor sequentially after the 1.1 V capacitor, you will need additional time to complete the 
overall charging process.
Leaving PMC.CTRL[LMBCTLEN] = 1 saves time when exiting Standby mode and does not draw any additional current during 
this mode.
41.5.1.4
SW4: Main core shutdown process
For information on this process, see these in the "Mode Entry Module (MC_ME)" chapter:
• Figure "Standby entry sequence along with main core shutdown"
• Section "Main core shutdown and Standby mode entry"
You must configure WKPU before disabling interrupts to avoid missing any events as shown in the Standby entry sequence along 
with main core shutdown flowchart in the MC_ME chapter. You must program WKPU, disable interrupts, and configure MC_ME's 
Standby mode entry in SW1 (see SW1: Module shutdown process for more information). In SW4, you must perform only the 
main-core WFI execution.
41.5.2 Hardware Standby mode entry sequence
The hardware Standby mode entry sequence consists of handshaking between MC_PCU and MC_ME occurring after Software 
Standby mode entry sequence completes. The FSM in MC_PCU performs these steps automatically and does not require your 
intervention (see Power sequence FSM in the MC_PCU chapter for more information).
During the MC_ME and PCU phase, MC_ME and PCU:
• Enable FIRC.
• Deassert isolation.
• Deassert reset to PD1.
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1674 / 5251


---
# 페이지 17

41.5.3 PMC Standby mode entry
The PMC Standby mode entry sequence starts after Hardware Standby mode entry sequence completes, and consists of 
these phases:
1. Standby mode entry acknowledgment and initiation of an internal low-power process on receiving Standby mode 
entry request.
2. Disabling of the boot regulator within the PMC low-power process. This point is only applicable for S32K344/S32K324/
S32K314 and S32K342/S32K322/S32K341.
3. Disabling of the V25 regulator and the FPM LVR monitors.
4. Disabling of the V25 regulator (oscillator and flash memory supply) and the LPM monitor, unless it is enabled during 
Standby mode (see PMC.CONFIG[LPM25EN] field in the PMC chapter for more information).
5. Disabling of the VDD_HV_B LPM monitors except S32K312, S32K311 and S32K310.
During PMC phase, after receiving an LPM request, PMC:
• Deasserts FPM ready signal.
• Starts the courtesy timer.
• When the courtesy timer expires, PMC:
— Disables the V25 regulator.
— Disables the HP reference blocks.
— Disables the external NMOS.
— Opens the PD0 switch.
— Enables a core LPM request.
— If selected, enables a 2.5 V LPM request.
— Disengages FPM monitors.
— Disables the VDD_HV_B LPM monitor, if present and deselected.
• Waits for LPM signal deassertion.
41.6 Chip status at the end of Standby mode entry sequence
After PMC Standby mode entry completes, the chip completes Standby mode entry as follows:
1. Configures Standby domain peripherals according to SW1 (see SW1: Module shutdown process).
2. Enables pad keeping on pins as described in SW1 (see SW1: Module shutdown process). See Pad keeping for other 
details.
3. Powers down all memory types except Standby RAM (in SRAM0).
• The V25 regulator can remain on during Standby mode. However, for maximum power savings, it must remain off in 
this mode.
4. Isolates Standby and Run domains from each other:
• Standby domain is functional.
• Run domain is held in reset.
5. Configures the system clock (FIRC_CLK or PLL_PHIn_CLK, depending on their configuration) and other clock sources 
according to SW3 (see Figure 180 for the procedure details).
The cores are off and in the Standby domain.
6. Turns off the boot[10] and FPM regulators.
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1675 / 5251


---
# 페이지 18

7. Waits for a wake-up event to initiate recovery from Standby mode.
41.7 Chip operation in Standby mode
This chip supports the following functionalities in Standby mode:
• STANDBY_RAM content retention during Standby mode.
• Wake-up from up to 60 digital inputs (for details, see the signals WKUP[n] functions of WKPU module in the IOMUX file 
attached to this document). The section "Wakeup Unit Configurations" in the "Wakeup Unit (WKPU)" chapter shows mapping 
of the wake-up sources.
• Wake-up from up to 16 analog inputs through the Trigger mode functionality (see the signals CMPn_INm functions of CMPn 
modules in the IOMUX file attached to this document).
• Wake-up from on-chip timers:
— RTI (function of PIT[0])
— SWT0
— RTC
• Ability to configure the chip clocking modules to optionally enable or disable in Standby mode (FIRC, SXOSC, FXOSC, 
and SIRC).
41.8 Standby mode exit
This chip supports Standby mode exit from a wake-up, functional reset, or destructive reset event. The sources that cause chip 
Standby mode exit are:
• MC_RGM functional reset event
• MC_RGM destructive reset event
• WKPU wake-up events, WKPU[0]–WKPU[63]. See the WKPU chapter for more information.
After Standby mode exit, the following events occur (for more information, see "Power sequence FSM" in the MC_PCU chapter 
for MC_PCU FSM transitions during entry into and exit from Standby mode):
1. A wake-up event arrives.
2. FIRC starts powering up (if disabled in Standby mode).
3. PMC starts the transition process to FPM (for example, enables the last-mile regulator and provides V11_RUN supply to 
the chip).
4. MC_PCU removes the isolation between Run and Standby domains.
5. Run domain reset deasserts (asserts on Standby mode entry) and the chip undergoes a functional reset exit sequence for 
this domain.
6. The chip enters Run mode of operation.
 
A reset event during standby results in pad controls to get reset. Thereby, resulting in unpredictable toggling 
at GPIO.
  NOTE  
[10] Not applicable for S32K388, S32K389, S32K312, S32K311, and S32K310.
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1676 / 5251


---
# 페이지 19

41.8.1 Faster Standby mode exit
The chip supports an optional configuration for faster recovery from Standby mode on the expense of a higher capacitor 
recharging current. See the CONFIG[FASTREC] field description in the PMC chapter for more information on faster PMC recovery 
from Standby mode.
This chip supports an optional feature that bypasses:
• FIRC trimming
• PMC trimming
• DCM scanning
To use the bypass operation, write 1 to DCM.DCMRWF2[5], DCM.DCMRWF2[4], and DCM.DCMRWF2[3] respectively before 
Standby mode entry. This results in a considerable reduction in Standby mode exit duration. The trim values are retained across 
Standby mode and bypassing these values does not cause any impact. Even if the FIRC trimming is bypassed, the FIRC must 
be at 48 MHz before entering Standby mode.
Configuration to achieve the tMODE_STDBYEXIT_FAST as specified in Datasheet
DCMRWF2[PMC_TRIM_RGM_DCF__BYP_STDBY_EXT] = 1
DCMRWF2[FIRC_TRIM_BYP_STDBY_EXT] = 1
DCMRWF2[DCM_SCAN_BYP_STDBY_EXT] = 1
41.8.2 Last-mile regulator enable sequence (not applicable for S32K388, S32K389, S32K312, 
S32K311 and S32K310)
After Standby mode exit, if the Last Mile Regulator Auto Enable function is not enabled, you must re-enable the PMC last-mile 
regulator before transitioning to faster clock frequencies. Figure 182 shows the last-mile regulator enable sequence part of the 
Standby mode exit process.
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1677 / 5251


---
# 페이지 20

Enable PMC
last-mile regulator
If applicable,
turn on BJT collector voltage
Write 1 to PMC.LVSC[LVD15F]
to clear flag
Write 1 to
PMC.CONFIG[LMBCTLEN]
Request turn on of 1.5 V
Using BJT
for 1.5 V
generation?
Yes
No
Continue Standby
mode exit process
Wait 50 µs
Wait 15 µs
PMC
CONFIG[FASTREC]
equal 0?
Yes
No
Write 1 to
PMC.CONFIG[LMEN]
Wait tsettle_lm time before
proceeding (see data sheet
for settling time)
Do not turn on anything
else until after setting
time.
PMC
LVSC[LVD15S]
equal 0?
Yes
Yes
No
Figure 182. Last-mile regulator enable sequence
41.9 PMIC Handshake with MCU (applicable for S32K328, S32K338, S32K348, S32K358, 
S32K388, and S32K389)
For interfacing with PMIC where handshake is required, MCU will follow a sequence to come out of standby. This handshake will 
make sure that power supply to the MCU is in proper condition.
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1678 / 5251


---
# 페이지 21

3 GPIOs will be used to perform this handshake as shown in below figure.
Figure 183. PMIC Handshake with MCU
PMIC
PGOOD
EXTWAKE
RESET_b
MCU
MCU will assert EXTWAKE signal on receiving a wakeup request from any of the available wakeup sources. If the EXTWAKE 
signal is enabled via the MSCR configuration (see IOMIX file attached to this document), this wakeup will be triggered to the 
external PMIC and the PMIC will use it to come out of standby mode. MCU sends the reset_b signal to PMIC to reset the PMIC.
 
After EXTWAKE assertion, POR WDOG is triggered. If PGOOD assertion does not arrive within the configured 
time, POR WDOG will issue a reset to the MCU.
  NOTE  
PMIC will raise PGOOD signal towards MCU for indicating the MCU that it is now able to provide the supplies in proper 
conditions. If the PGOOD input is enabled via the corresponding IMCR configuration (see IOMIX file attached to this document) 
and the appropriate PGOOD polarity and enable settings are selected in the corresponding DCMRWF configuration registers 
(see PMIC_PGOOD_HNDSHK_BYP and PGOOD_POLARITY in Chapter 38, Device Configuration Module General-Purpose 
Registers (DCM_GPR)), the MCU will proceed to exit from STANDBY mode once the PGOOD input is asserted.
41.10 SMPS
SMPS is regarded as enhancement for the BJT regulator. The essential advantage of SMPS is that the power dissipation is much 
less compared to the linear regulators. SMPS generates the intermediate power rail of 1.5 V, which is then converted to 1.1 V by 
the last-mile regulator.
41.11 Chip power domain partitioning
The Standby domain includes the modules listed below. For more information, see "Peripheral reset status" in the "Reset 
Overview" chapter.
 
Modules within the Standby domain do not participate in the LBIST operation.
  NOTE  
41.11.1 Modules available in Standby domain
Table 252. Modules available in Standby domain
PD0 contents
S32K344/
S32K324/S32K314
S32K342/
S32K322/S32K341
S32K312
S32K311
S32K358/
S32K348/
S32K338/
S32K328/
S32K388/S32K389
External 
Pin wakeups
Minimum 60
Minimum 60
Minimum 60
33 on 100HDQFP & 
12 on 48LQFP
Minimum 60
Table continues on the next page...
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1679 / 5251


---
# 페이지 22

Table 252. Modules available in Standby domain (continued)
PD0 contents
S32K344/
S32K324/S32K314
S32K342/
S32K322/S32K341
S32K312
S32K311
S32K358/
S32K348/
S32K338/
S32K328/
S32K388/S32K389
RTC_API
Yes
Yes
Yes
Yes
Yes
LPCMP_0
Yes
Yes
Yes
Yes
Yes
LPCMP_1
Yes
Yes
Yes
No
Yes
LPCMP_2
Yes
No
No
No
Yes
SWT_0
Yes
Yes
Yes
Yes
Yes
WKPU
Yes
Yes
Yes
Yes
Yes
PMC
Yes
Yes
Yes
Yes
Yes
MC_RGM
Yes
Yes
Yes
Yes
Yes
SXOSC(only used 
for RTC)
Yes
Yes
Yes
No
Yes
FXOSC
Yes
Yes
Yes
Yes
Yes
FIRC
Yes
Yes
Yes
Yes
Yes
SIRC
Yes
Yes
Yes
Yes
Yes
CLK OUT
Yes
Yes
Yes
Yes
Yes
SRAM
32K
32K
32K
32K
64K
PIT_RTI_0
Yes
Yes
Yes
Yes
Yes
DCM and 
DCF records
Yes
Yes
Yes
Yes
Yes
DCM 
Flash Interface
Yes
Yes
Yes
Yes
Yes
SWT0 (Cortex-M7_0) resides in the Standby domain and supports a configurable hardware-based timer operation during Standby 
mode depending on the configuration of SWTs.
All clock sources (except PLLDIG) are available in Standby mode. SIRC is present in the Standby domain for low-power wake-up, 
but can be enabled.
 
This chip does not support Stop and Wait modes. The only low-power mode it supports is Standby.
  NOTE  
41.12 Pad keeping
Pad-keeping allows you to retain the state of the pads while the MCU is in the Standby mode.
41.12.1 Pad keeping on Run domain pins
The process of entering Standby mode ensures that the chip maintains the state of the pads until it 
wakes-up and re-configures them by software. Software Standby mode entry sequence specifies that you 
must write 0 to DCM.DCMRWF1[STANDBY_IO_CONFIG] before configuring I/O pad keeping. You could consider 
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1680 / 5251


---
# 페이지 23

DCM.DCMRWF1[STANDBY_IO_CONFIG] field as a global enable for all pad keeping purposes during Standby mode. If 
you are unable to write to this field as described, pad keeping works as explained in this chapter, during Standby mode.
After the chip exits Standby mode, you must first re-configure your pads, and then, write 1 to 
DCM.DCMRWF1[STANDBY_IO_CONFIG] field (see "Chip specific register descriptions" in the DCM chapter). Writing 1 to 
this field disables pad keeping.
41.12.2 Pad keeping on Standby domain pins
See Table 253 for the Standby domain pins (all the rest are Run domain pins).
The Standby domain pads can have pad keeping enabled or disabled based on pad availability in Standby mode. Writing to 
SIUL2.MSCRn[PKE] field configures Standby mode pad keeping on a selected I/O.
Ensure that DCM.DCMRWF1[STANDBY_IO_CONFIG] = 0 before Standby mode entry for pad keeping on Standby domain pads. 
Write 0 to the field in case its value is not 0 already.
If a pad is not required during Standby mode, the corresponding MSCRn[PKE] field in SIUL2 must be 0.
41.12.3 Pad keeping configuration procedure
This procedure specifies how to enable an I/O for pad keeping:
1. Configure SIUL2.MSCRn register to control the pad state prior to Standby mode entry (for example, writing 0 to 
SIUL2.MSCRn[OBE], MSCRn[IBE], and MSCR[PUE] fields tristates the corresponding I/O).
2. Configure SIUL2.MSCRn[PKE] field as needed for an I/O pad keeping state during Standby mode.
3. Write 0 to DCM.DCMRWF1[STANDBY_IO_CONFIG].
The application core executes WFI, and Standby mode sequence starts.
4. Write 1 to DCM.DCMRWF1[STANDBY_IO_CONFIG] field on Standby mode exit to disable pad keeping.
If you write 1 to DCM.DCMRWF1[STANDBY_IO_CONFIG] field before entering Standby mode, the isolation removal hardware 
removes pad keeping on Standby mode exit. This (writing 1 to DCM.DCMRWF1[STANDBY_IO_CONFIG] field before Standby 
mode entry) is useful in case of low-power debug because enabling pad keeping does not allow low-power debug protocol to work 
properly (because the TDO pad is padkept). For low-power debug, you must write 1 to DCM.DCMRWF1[STANDBY_IO_CONFIG] 
field prior to Standby mode entry.
In case of Standby mode exit by reset, the pad keeping of the reset pin is removed when the chip is reset on Standby mode wake 
up. See the "GPIO padkeeping enable" signal in Figure 185. The signal corresponds to wake-up via reset event case.
41.12.4 Pad keeping waveforms
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1681 / 5251


---
# 페이지 24

41.12.4.1
Pad keeping when the chip wakes up from Standby mode via an interrupt wake-up event
Standby domain reset (active low)
FIRC_CLK
Run domain reset (active low)
a
f
Run domain isolation
b
d
e
GPIO padkeeping enable
c
h
Wake-up event
Padkeeping enable, DCM.DCMRWF1[16]
g
Chip isolation enabled after Run
domain is reset on standby entry
Run domain comes out of reset
Isolation is removed on wake-up event and PMC
switches from Standby to Run mode gracefully
GPIO padkeeping enabled on isolation enable
You must write 0 to this GPR
before Standby entry.
GPR must be 1 to remove GPIO padkeeping
GPIO padkeeping disabled after padkeeping enable GPR is 1
Figure 184. Pad keeping when the chip wakes up from Standby mode via an interrupt event
41.12.4.2
Pad keeping when the chip wakes up from Standby mode via reset
If the chip exits Standby mode via reset, the reset pad keeping is removed when the chip resets after Standby-mode wake-up. 
See the figure's "GPIO padkeeping enable" waveform corresponding to wake-up via a reset event.
Standby domain reset (active low)
FIRC_CLK
Run domain reset (active low)
a
f
g
Run domain isolation
b
d
e
GPIO padkeeping enable
c
h
Wake-up event
(functional or destructive reset event)
Padkeeping enable, DCM.DCMRWF1[16]
Chip isolation enabled after Run
domain is reset on standby entry
After graceful Standby exit, the chip undergoes reset
(functional/destructive as per the reset event)
Isolation is removed on wake-up event and PMC
gracefully switches from Standby to Run mode
GPIO padkeeping enabled on isolation enable
You must write 0 to this GPR
before Standby entry.
GPIO padkeeping disabled due to reset.
GPR configuration is not required.
Run domain comes out of reset
Figure 185. Pad keeping when the chip wakes up from Standby mode via reset
41.12.5 SIUL2's fields for actively-driven pins in Standby mode
If you use a WKPU pin as a wake-up input, perform these operations on SIUL2's fields:
1. Write 1 to SIUL2.MSCRx[IBE].
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1682 / 5251


---
# 페이지 25

2. Program SIUL2.MSCRx[PUE] and SIUL2.MSCRx[PUS] according to the use case.
3. Write 0 to SIUL2.MSCRx[PKE].
For the GPIO pins that are driven to high impedance during Standby mode:
1. Write 0 to DCM.DCMRWF1[STANDBY_IO_CONFIG] field.
2. Write 0 to SIUL2.MSCRx[SSS] field (GPIO mode).
3. Write 0 to SIUL2.MSCRx[IBE] and SIUL2.MSCRx[OBE] fields.
Some of the pins are, by default, actively driven in Standby mode. If these pins retain a static value throughout the mode, program 
the corresponding SIUL2.MSCRx[PKE] bits individually.
This table shows the list of pins available in Standby mode along with the functions they perform.
Table 253. Active pins in Standby mode
Pin1
Function
GPIO_4
CMP0_OUT
GPIO_5
RESET_b
GPIO_9
CMP2_OUT
GPIO_11
CMP0_RRT
GPIO_12
CLKOUT_STANDBY; CMP1_OUT
GPIO_69
CMP2_RRT
GPIO_110
CMP0_RRT
GPIO_131
CMP0_OUT
GPIO_138
CLKOUT_STANDBY
GPIO_143
CMP1_RRT
GPIO_158
CMP1_OUT
GPIO_159
CMP1_RRT
GPIO_174
CMP0_OUT
GPIO_175
CMP0_RRT
GPIO_196
CMP2_OUT
GPIO_197
CMP2_RRT
1. See the IOMUX sheet attached to this document for details on pins configuration in different chips.
41.13 Glossary
Application core Core apart from the main core
Boot regulator
The on chip 1.1 V regulator that is active during startup and entry and exit from Standby mode
FSM
Finite state machine
FPM
Full-power mode (Run mode)—uses the last-mile regulator and 1.5 V source to generate the 1.1 V core 
logic supply during a full-power operation (V11_RUN)
LPM
Low-power mode (Standby mode)—uses the low-power regulator to generate the 1.1 V core logic supply 
during low-power operation (V11_STANDBY)
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1683 / 5251


---
# 페이지 26

LVR
Low voltage reset
Main core
Core initiating the chip Standby mode request (for example, the core corresponding to the "core index" in 
MC_ME's MAIN_COREID register)
Pad keeping
Maintains I/O pad configuration during Standby mode, if enabled
V11_STANDBY Core logic and clock sources, low-voltage supply to Standby domain
V11_RUN
Low-voltage supply to Run domain
V15
High-current input for core or logic supply from either an external BJT or from direct 1.5 V external supply
V25
Flash memory, FXOSC, and PLLDIG high-voltage supply
VDDA_ADC
ADC supply voltage
VREFH
ADC high-voltage reference supply
VREFL
ADC low-voltage reference supply
VSS
Core logic ground supply
VDD_HV_A
Main I/O voltage supply (5 V or 3.3 V)
VDD_HV_B
Other I/O domain voltage supply (5 V or 3.3 V)
VRC_CTRL
PMC voltage regulator control output using the BJT option to generate a 1.5 V supply
WFI
Wait for interrupt software instruction
NXP Semiconductors
Power Management
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
1684 / 5251


---