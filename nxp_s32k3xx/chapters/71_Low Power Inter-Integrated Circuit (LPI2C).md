# 페이지 56

Chapter 71
Low Power Inter-Integrated Circuit (LPI2C)
71.1 Chip-specific LPI2C information
71.1.1 LPI2C instances and configuration
This chip has two instances of LPI2C: LPI2C_0 and LPI2C_1.
Table 454. LPI2C configuration
Instances
TX FIFO Size
RX FIFO Size
SMBus1
Slave Mode Enable
LPI2C_0
4x11 bit
4x8 bit
Yes
Yes
LPI2C_1
4x11 bit
4x8 bit
Yes
Yes
1. System Management Bus
• LPI2C target mode operation supports up to high speed mode = 3.4MHz (3.4 Mbps data rate; effective data rate reduces 
according to I2C protocol).
• LPI2C controller mode operation supports up to fast Mode = 400KHz (400 kbps data rate; effective data rate reduces 
according to I2C protocol).
• The LPI2C module includes SMBus (System Management Bus) support and DMA support.
• LPI2C RX FIFO is 8-bit and TX FIFO is 11-bit (8bit data + 3bit command)
• LPI2C supports fast data communication as per I2C standard v3.0.
71.2 Overview
LPI2C supports an efficient interface to an I2C bus as a controller and target:
• Implements logic support for Standard, Fast, Fast+, HS-mode (target only) and Ultra-Fast modes of operation
• Uses little CPU overhead, with DMA offloading of FIFO register accesses
LPI2C also complies with the System Management Bus (SMBus) Specification, version 3. The SMBus is a single-ended simple 
two-wire bus, which is typically used for low-bandwidth communications.
The Inter-Integrated Circuit (I2C) serial bus is multi-controller, multi-target, packet-switched, and single-ended, and is often used 
to attach microcontroller ICs to lower-speed peripheral ICs.
 
Terminology in this chapter has been updated to align with I2C-bus specification, Rev. 7.0, as shown in Table 455.
Table 455. Updated terms
Updated term
Deprecated term
Controller
Master
Target
Slave
  NOTE  
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2916 / 5251


---
# 페이지 57

71.2.1 Block diagram
Internal chip
peripheral bus
Controller
Target
Bus clock
External clock
Clock domains
LPI2C
Functional clock
Glitch
filter
SDAS
HREQ
SCLS
Configuration
registers
Controller
logic
Glitch
filter
Prescaler
Trigger
SDA
SCL
Target
logic
Configuration
registers
RX data/ 
address
TX data
RX FIFO
Command/ 
TX FIFO
Figure 393. Block diagram
71.2.2 Features
LPI2C supports:
• Standard, Fast, Fast+ and Ultra Fast modes
• HS mode in target mode
• Multicontroller, including synchronization and arbitration, means that any number of controller nodes can be present. Also, 
controller and target roles can be changed between messages (after a Stop signal is sent).
• Clock stretching. Used on the SCL line, as an I2C flow control mechanism.
• Arbitration for when the system has more than one controller. When used on the SDA line, ensures that there is only one 
I2C transmitter at a time.
• General call, seven-bit addressing, and ten-bit addressing
• Software reset, Start byte, and device ID (also require software support)
The LPI2C controller supports:
• Command and transmit FIFO of 4 words (8-bit transmit data + 3-bit command)
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2917 / 5251


---
# 페이지 58

• Receive FIFO of 4 words (8-bit receive data).
• Command FIFO waiting for an I2C idle bus before initiating a transfer
• Initiation of repeated Start and Stop conditions and one or more controller-receiver transfers by command FIFO
• Stop condition generation from command FIFO, or automatic generation of Stop condition when the transmit FIFO is 
empty
• Host request input to control the start time of an I2C bus transfer
• Interrupt generation on data match and unwanted data rejection, via flexible receive data match
• Flags and optional interrupt signals at repeated Start condition, Stop condition, loss of arbitration, unexpected NACK, and 
command word errors
• Configurable bus idle timeout and pin-stuck-low timeout
The LPI2C target supports:
• Separate I2C target registers to minimize software overhead because of controller or target switching
• 7-bit or 10-bit addressing, address range, SMBus alert, and general call address.
• Transmit data register that supports interrupt or DMA requests
• Receive data register that supports interrupt or DMA requests
• Software-controllable ACK or NACK, with optional clock stretching on ACK or NACK field
• Configurable clock stretching, to avoid transmit-FIFO-underrun and receive-FIFO-overrun errors
• Flags and optional interrupt at end of packet, Stop condition, or bit error detection
71.3 Functional description
71.3.1 Controller mode
The LPI2C controller logic operates independently from the target logic to perform all controller-mode transfers on the I2C bus.
71.3.1.1
Transmit and Command FIFO commands
The transmit FIFO stores command data to initiate various I2C operations. The following operations can be initiated through 
commands in the transmit FIFO:
• Start or repeated Start condition with address byte, expecting ACK or NACK.
• Transmit data. This operation is the default for zero-extended-byte writes to the transmit FIFO.
• Receive 1-256 bytes of data. You can configure this operation to discard received data and not to store it in the receive 
FIFO.
• Stop condition. You can configure this operation to send a Stop condition when the transmit FIFO is empty.
Multiple transmit and receive commands can be inserted between the Start and Stop conditions. To comply with the I2C 
specification, transmit and receive commands must not be interleaved. The receive data command and the receive data and 
discard commands can be interleaved. This interleaving ensures that only the desired received data is stored in the receive FIFO 
(or compared with the data match logic).
The LPI2C controller automatically transmits a NACK on the last byte of a receive data command. It transmits the NACK unless 
the next command in the FIFO is also a receive data command. If the transmit FIFO is empty when a receive data command 
completes, a NACK is also automatically transmitted.
The LPI2C controller supports 10-bit addressing via a (repeated) Start condition, followed by a transmit data byte containing the 
second address byte, followed by any number of data bytes with the controller transmit data.
A Start or repeated Start condition expecting a NACK (for example, HS mode controller code) must be followed by a Stop or 
(repeated) Start condition.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2918 / 5251


---
# 페이지 59

71.3.1.2
Controller operations
When LPI2C is enabled, it monitors the I2C bus to detect when the I2C is idle (MSR[BBF]). If either SCL or SDA are low, the 
I2C bus is no longer considered idle. The bus becomes idle if a Stop condition is detected or if a bus idle timeout is detected (as 
configured by MCFGR2[BUSIDLE]). After the bus is idle, if the transmit FIFO is not empty and the host request is asserted or 
disabled, the LPI2C controller initiates a transfer on the bus. This transfer involves the following steps:
1. Wait the bus idle time equal to (MCCR0[CLKLO] + 1) multiplied by the prescaler (MCFGR1[PRESCALE]).
2. Transmit a Start condition and address byte using the timing configuration in Controller Clock Configuration 0 (MCCR0). 
If an HS mode transfer is configured, the timing configuration from Controller Clock Configuration 1 (MCCR1) is used 
instead.
3. Perform controller transmit or controller receive transfers, as configured by the transmit FIFO.
4. Transmit NACK on the last byte of a controller receive transfer. This action is performed unless the next command in 
the transmit FIFO is also a receive data command and the transmit FIFO is not empty.
5. Transmit a repeated Start or Stop condition as configured by the transmit FIFO or MCFGR1[AUTOSTOP]. A repeated 
Start can change which timing configuration register is used.
When the LPI2C controller is disabled, LPI2C continues emptying the transmit FIFO until a Stop condition is transmitted. 
(The controller could be disabled due to MCR[MEN] being 0, or automatically due to mode entry.) However, LPI2C no longer 
stalls the I2C bus by waiting for the transmit or receive FIFO. After the transmit FIFO is empty, LPI2C generates a Stop 
condition automatically.
The LPI2C controller can stall the I2C bus under certain conditions. This stalling results in SCL pulled low continuously on the first 
bit of a byte, until these conditions change:
• The LPI2C controller is enabled and busy, the transmit FIFO is empty, and MCFGR1[AUTOSTOP] is 0. The LPI2C 
controller continues to stall the bus until the transmit FIFO is loaded with more data.
• The LPI2C controller is enabled and receiving data, receive data is not being discarded (due to command or receive data 
match), and the receive FIFO is full. The LPI2C controller continues to stall the I2C bus until the receive FIFO is emptied.
71.3.1.3
Receive FIFO and data matching
The receive FIFO stores receive data during controller-receiver transfers. You can configure the LPI2C controller to discard 
received data instead of storing it in the receive FIFO. This option is configured via the command word in the transmit FIFO.
Received data supports a receive data match function that can match received data against one of two bytes, or against a masked 
data byte. You can configure the data match function to compare only the first one or two data words received since the last 
(repeated) Start condition. Received data that is already discarded due to the command word cannot cause a data match. It delays 
the match on the first data word received until after the discarded data is received.
You can configure the receiver match function to discard all received data until a data match is detected, using MCFGR0[RDMO]. 
Following a data match, write 0 to MCFGR0[RDMO] before writing 0 to MSR[DMF] to allow all subsequent data to be received.
71.3.1.4
Timing parameters
The LPI2C controller can configure the following timing parameters. Parameters are configured separately for HS mode 
(Controller Clock Configuration 1 (MCCR1)) and other modes (Controller Clock Configuration 0 (MCCR0)). This separation allows 
the HS mode controller code to be sent using regular timing parameters. Then it allows a switch to HS mode timing (following a 
repeated Start) until the next STOP condition.
Configure the LPI2C controller timing parameters, measured in LPI2C functional clock cycles, as shown in Table 456. You must 
configure these parameters to meet the I2C timing specification for the required mode.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2919 / 5251


---
# 페이지 60

Table 456. Timing parameters
I2C specification timing parameter
I2C specification timing 
symbol
LPI2C timing parameter (in LPI2C functional clock 
cycles)
SCL clock period
tSCL
(CLKHI + CLKLO + 2 + SCL_LATENCY) × (2 ^ 
PRESCALE)
Hold time (repeated) Start condition
tHD:STA
(SETHOLD +1) × (2 ^ PRESCALE)
Low period of the SCL clock
tLOW
(CLKLO + 1) × (2 ^ PRESCALE)
High period of the SCL clock
tHIGH
(CLKHI + 1 + SCL_LATENCY) × (2 ^ 
PRESCALE)
Setup time for a repeated Start condition 
or Stop condition
tSU:STA, tSU:STO
(SETHOLD + 1 + SCL_LATENCY) × (2 ^ 
PRESCALE)
Data hold time
tHD:DAT
(DATAVD + 1) × (2 ^ PRESCALE)
Data setup time
tSU:DAT
(SDA_LATENCY + 1) × (2 ^ PRESCALE)
Bus free time between a Stop and Start 
condition
tBUF
(CLKLO + 1 + SDA_LATENCY) × (2 ^ 
PRESCALE)
Data valid time, data valid acknowledge 
time
tVD:DAT, tVD:ACK
(DATAVD + 1) × (2 ^ PRESCALE)
Table 457 defines the latency parameters. These parameters assume that the risetime is less than one LPI2C functional clock 
cycle. The risetime depends on a number of factors, including the I/O propagation delay, the I2C bus loading, and the external 
pullup resistor sizing. A larger risetime increases the number of cycles that the signal takes to propagate through the synchronizer 
(and glitch filter), which increases the latency.
Table 457. Synchronization latency
Timing parameter
Timing definition
SCL_LATENCY
ROUNDDOWN ((2 + FILTSCL + SCL_RISETIME) ÷ (2 ^ PRESCALE))
SDA_LATENCY
ROUNDDOWN ((2 + FILTSDA + SDA_RISETIME) ÷ (2 ^ PRESCALE))
The following timing restrictions must be enforced to avoid unexpected Start or Stop conditions on the I2C bus. These restrictions 
also avoid unexpected Start or Stop conditions detected by the LPI2C controller. The timing restrictions can be summarized as 
"SDA cannot change when SCL is high outside a transmitted (repeated) Start or Stop condition."
Table 458. LPI2C timing parameter restrictions
Timing parameter
Minimum
Maximum
Comment
CLKLO
03h
—
CLKLO x (2 ^ PRESCALE) > 
SCL_LATENCY
CLKHI
01h
—
Configure CLKHI to meet the duty cycle 
requirements in the I2C specification
SETHOLD
02h
—
SETHOLD × (2 ^ PRESCALE) > 
SDA_LATENCY
DATAVD
01h
CLKLO –
 SDA_LATENCY – 1
Configure DATAVD to meet the data 
hold requirement in the I2C specification
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2920 / 5251


---
# 페이지 61

Table 458. LPI2C timing parameter restrictions (continued)
Timing parameter
Minimum
Maximum
Comment
FILTSCL
00h
[CLKLO × (2 ^ 
PRESCALE)] – 3
FILTSCL and FILTSDA are the 
only parameters not multiplied by 
(2 ^ PRESCALE)
FILTSDA
FILTSCL
[CLKLO × (2 ^ 
PRESCALE)] – 3
Configuring FILTSDA greater than 
FILTSCL can delay the SDA input to 
compensate for board level skew
BUSIDLE
(CLKLO + SETHOLD + 2)
 × 2
—
Must also be greater than (CLKHI + 1)
See the UM10204, I2C-bus specification and user manual.
See Application information for example LPI2C timing configurations.
71.3.1.5
Error conditions
The LPI2C controller monitors errors while it is active. The following conditions generate an error flag and block a new Start 
condition from being sent, until the flag is cleared by software:
• A Start or Stop condition is detected and is not generated by the LPI2C controller (MSR[ALF] becomes 1).
• Transmitting data on SDA and different values are received (MSR[ALF] becomes 1).
• NACK is detected when transmitting data, and MCFGR1[IGNACK] is 0 (MSR[NDF] becomes 1).
• NACK is detected and is expecting ACK for the address byte, and MCFGR1[IGNACK] is 0 (MSR[NDF] becomes 1).
• ACK is detected and is expecting NACK for the address byte, and MCFGR1[IGNACK] is 0 (MSR[NDF] becomes 1).
• Transmit FIFO is requesting to transmit or receive data without a Start condition (MSR[FEF] becomes 1).
• SCL (or SDA if MCFGR1[TIMECFG] is 1) is low for (MCFGR2[TIMELOW] × 256) prescaler cycles without a pin transition 
(MSR[PLTF] becomes 1).
You must respond to MSR[PLTF] to terminate the existing command. You can terminate the command cleanly by writing 0 to 
MCR[MEN], or you can terminate it abruptly by writing 1 to MCR[RST].
You can use MCFGR2[BUSIDLE] to force the I2C bus to be considered idle when SCL and SDA remain high for (BUSIDLE + 1) 
prescaler cycles. The bus is considered idle when the LPI2C controller is first enabled. When BUSIDLE is configured greater than 
zero, then SCL or SDA must be high for (BUSIDLE + 1) prescaler cycles before the I2C bus is considered idle.
71.3.1.6
Pin configuration
Configuration
Description
Open-drain support
The LPI2C controller defaults to open-drain configuration of the SDA and SCL pins. Support for true 
open drain depends on the specific device, and requires the pins where LPI2C pins are muxed to 
support true open drain.
HS mode support
Support for HS mode depends on the specific device. This mode requires the SCL pin to support 
the current source pullup required in the I2C specification.
Ultra-Fast mode 
support
The LPI2C controller supports the output-only push-pull function required for I2C Ultra-Fast mode 
using the SDA and SCL pins. Support for Ultra-Fast mode also requires MCFGR1[IGNACK] to be 
1.
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2921 / 5251


---
# 페이지 62

Table continued from the previous page...
Configuration
Description
Push-pull two-wire 
support
A push-pull two-wire configuration is available to the LPI2C controller. If LPI2C is the only controller 
and all I2C pins on the bus are at the same voltage, this configuration may support a partial HS 
mode. A partial HS mode, not a full HS mode, because this configuration actively drives high rather 
than enabling a current service pull-up. This configuration sets the SCL pin as push-pull for every 
clock except the first clock pulse, to allow HS-mode-compatible targets to perform clock stretching. 
In this mode, the SDA pin is tristated for controller-receive data bits and controller-transmit ACK/
NACK bits, and is configured as push-pull at other times. To avoid the risk of contention when SDA 
is push-pull, configure the pin for open-drain operation, as part of the device-specific configuration.
Push-pull four-wire 
support
The push-pull four-wire configuration separates the SCL input data and output data into separate 
pins. It also separates the SDA input data and output data into separate pins. The SCL/SDA 
pins are used for input data; the SCLS/SDAS pins are used for output data, with configurable 
polarity. This configuration simplifies external connections when connecting the LPI2C to the I2C 
bus through external level shifters or discrete components. When using this four-wire configuration, 
the LPI2C controller logic and LPI2C target logic cannot connect to separate I2C buses.
71.3.2 Target mode
To perform all target mode transfers on the I2C bus, the LPI2C target logic operates independently from the LPI2C controller logic.
71.3.2.1
Address matching
You can configure the LPI2C target:
• To match one of two addresses, using either 7-bit or 10-bit addressing modes for each address.
• To match a range of addresses in either 7-bit or 10-bit addressing modes.
• To match the general call address and generate appropriate flags.
• To match the SMBus alert address and generate appropriate flags.
• To detect the HS mode controller code address, and to disable the digital filters and output valid delay time until the next 
Stop condition is detected.
After a valid address is matched, the LPI2C target automatically performs target-transmit or target-receive transfers until:
• A NACK is detected (unless SCFGR1[IGNACK] becomes 1).
• A bit error is detected (the LPI2C target is driving SDA, but a different value is sampled).
• A (repeated) Start or Stop condition is detected.
71.3.2.2
Transmit and receive data
Target Transmit Data (STDR) and Target Receive Data (SRDR) are double-buffered and only update during a target-transmit and 
target-receive transfer, respectively.
You can configure the target address that was received to be read from SRDR (for example, when using DMA to transfer data) 
or from Target Address Status (SASR).
You can configure STDR to request data only after a target-transmit transfer is detected. You can also configure it to request new 
data whenever STDR is empty.
Write to STDR only when SSR[TDF] is set.
Read SRDR only when SSR[RDF] is set, or when SSR[AVF] is set and SCFGR1[RXCFG] = 1.
Read SASR only when SSR[AVF] is set.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2922 / 5251


---
# 페이지 63

71.3.2.3
Clock stretching
The LPI2C target supports many configurable options for clock stretching. You can configure these conditions to perform 
clock stretching:
• SSR[AVF] is set during the ninth clock pulse of the address byte.
• SSR[TDF] is set during the ninth clock pulse of a target-transmit transfer.
• SSR[RDF] is set during the ninth clock pulse of a target-receive transfer.
• SSR[TAF] is set during the eighth clock pulse of an address byte or a target-receive transfer. In HS mode, this option is 
disabled.
• Clock stretching can be extended for a number of cycles equal to the value of SCFGR2[CLKHOLD] cycles. This stretching 
allows additional setup time to sample the SDA pin externally. In HS mode, this option is disabled.
When clock stretching is enabled, clock stretching extends for one peripheral bus clock cycle after SDA updates, unless extended 
by the SCFGR2[CLKHOLD] configuration.
71.3.2.4
Timing parameters
The LPI2C target can configure the following timing parameters:
• SDA data valid time from SCL negation to SDA update
• SCL hold time when clock stretching is enabled to increase setup time when sampling SDA externally
• SCL glitch filter time
• SDA glitch filter time
These parameters are disabled when SCR[FILTEN] is 0, when SCR[FILTDZ] is 1 in Doze mode, and when LPI2C target detects 
HS mode. When disabled, the LPI2C target is clocked directly from the I2C bus. In this case, the target may not satisfy all timing 
requirements of the I2C specification (such as SDA minimum hold time in Standard/Fast mode).
The LPI2C target places the following restrictions on the timing parameters:
• You must configure SCFGR2[FILTSDA] to be greater than or equal to SCFGR2[FILTSCL] (unless compensating for board 
level skew between SDA and SCL).
• You must configure SCFGR2[DATAVD] to be less than the minimum SCL low period.
71.3.2.5
Error conditions
The LPI2C target can flag the following error conditions:
• SSR[BEF] is set when the LPI2C target is driving SDA but it samples a different value than what is expected.
• SSR[FEF] is set due to a transmit data underrun or a receive data overrun. To eliminate the possibility of underrun and 
overrun, enable clock stretching.
• SSR[FEF] is also set due to an address overrun, but only when SCFGR1[RXCFG] is 1. To eliminate the possibility of 
overrun, enable clock stretching.
The LPI2C target does not implement a timeout due to SCL or SDA being stuck low. If this detection is required, use the LPI2C 
controller logic so you can reset the LPI2C target when this condition is detected.
71.3.3 Low-power modes
LPI2C remains functional during low-power modes, if MCR[DOZEN] = 0 and LPI2C uses an external or internal clock source that 
remains enabled. LPI2C can generate an interrupt or DMA request to cause a wake-up from low-power modes.
You can configure LPI2C to be disabled in low-power modes when MCR[DOZEN] = 1. In this case, LPI2C waits for the current 
transfer to complete any pending operation.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2923 / 5251


---
# 페이지 64

 
See the chip-specific information for low-power modes available on your chip.
  NOTE  
71.3.4 Debug mode
Table 459. Debug mode
Mode
LPI2C operation
Debug
If MCR[DBGEN] = 1, can continue operating in Debug mode.
71.3.5 Peripheral triggers
The connection of the LPI2C peripheral triggers to other peripherals depends upon the specific device being used.
Table 460. LPI2C triggers
Trigger
Description
Controller output trigger Generates an output trigger that can be connected to other peripherals on the device. The controller 
output trigger asserts on either a repeated Start or a Stop condition. The trigger remains asserted for 
one cycle of the LPI2C functional clock divided by MCFGR1[PRESCALE].
Target output trigger
Generates an output trigger that can be connected to other peripherals on the device. The target output 
trigger asserts on either a repeated Start or a Stop condition that occurs after a target address match. 
The target output trigger remains asserted until the next target SCL pin negation.
Input trigger
To control the start of a LPI2C bus transfer, the LPI2C input trigger can be selected instead of the 
HREQ input. The input trigger is synchronized. To be detected, the input trigger must assert for at least 
two cycles of the LPI2C functional clock divided by the value of MCFGR1[PRESCALE]. When LPI2C 
is busy, the HREQ input (and therefore the input trigger) is ignored.
71.3.6 Clocking
Table 461. LPI2C clocks
Clock
Description
LPI2C functional clock
The LPI2C functional clock is asynchronous to the bus clock. It can remain enabled in low-power 
modes to support I2C bus transfers by the LPI2C controller. The functional clock is also used by the 
LPI2C target to support digital filter and data hold time configurations. The LPI2C controller divides 
the functional clock by a prescaler (MCFGR1[PRESCALE]) and the resulting frequency must be at 
least eight times faster than the I2C bus bandwidth.
External clock
The LPI2C target logic is clocked directly from the external pins. These pins are SCL and SDA, 
or SCLS and SDAS if the controller and target are implemented on separate pins). This clocking 
allows the LPI2C target to remain operational, even when the LPI2C functional clock is disabled.
 
If the LPI2C functional clock is disabled, the LPI2C target digital filter must be 
disabled. This condition can affect compliance with some timing parameters of the 
I2C specification, such as data hold time.
  NOTE  
Bus clock
The bus clock is only used for bus accesses to the control and configuration registers. The bus 
clock frequency must be sufficient to support the data bandwidth requirements of the LPI2C 
controller and target registers.
For chip-specific clocking information, see the Clocking chapter.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2924 / 5251


---
# 페이지 65

71.3.7 Reset
Table 462. LPI2C resets
Reset
Description
Chip reset
The logic and registers for the LPI2C controller and target are reset to their default states after a 
chip reset.
Software reset
The LPI2C controller implements a software reset field in its control register. MCR[RST] resets all 
controller logic and registers to their default states, except for Controller Control (MCR) itself.
The LPI2C target implements a software reset field in its control register. SCR[RST] resets all target 
logic and registers to their default states, except for Target Control (SCR) itself.
FIFO reset
The LPI2C controller implements write-only control fields that reset the transmit FIFO (MCR[RTF]) and 
receive FIFO (MCR[RRF]). After a FIFO is reset, that FIFO is empty.
The LPI2C target implements write-only control fields that reset the transmit data register (SCR[RTF]) 
and receive data register (SCR[RRF]). After a data register is reset, that data register is empty.
71.3.8 Interrupts and DMA requests
Depending on the configuration, interrupts and DMA requests can be combined:
• LPI2C controller and target interrupts
• LPI2C controller and target transmit DMA requests
• LPI2C controller and target receive DMA requests
71.3.8.1
Controller mode
Table 463 lists the Controller mode sources that can generate LPI2C controller interrupts and LPI2C controller transmit and 
receive DMA requests.
Table 463. Controller interrupts and DMA requests
Status flag
Description
Can generate
Interrupt?
DMA request?
Low-power 
wake-up?
Transmit Data Flag 
(MSR[TDF])
Data can be written to transmit FIFO, as 
configured by MFCR[TXWATER].
Y
TX
Y
Receive Data Flag 
(MSR[RDF])
Data can be read from the receive FIFO, 
as configured by MFCR[RXWATER].
Y
RX
Y
End Packet Flag 
(MSR[EPF])
Controller has transmitted a repeated Start 
or Stop condition.
Y
N
Y
Stop Detect Flag 
(MSR[SDF])
Controller has transmitted a Stop 
condition .
Y
N
Y
NACK Detect Flag 
(MSR[NDF])
During an address byte, the controller 
expects an ACK but detects a NACK.
During an address byte, the controller 
expects a NACK but detects an ACK.
Y
N
Y
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2925 / 5251


---
# 페이지 66

Table 463. Controller interrupts and DMA requests (continued)
Status flag
Description
Can generate
Interrupt?
DMA request?
Low-power 
wake-up?
During a controller-transmitter data byte, the 
controller detects a NACK.
Arbitration Lost Flag 
(MSR[ALF])
The controller lost arbitration due to a Start 
or Stop condition detected at the wrong 
time, or the controller was transmitting data 
but received data different from the data 
that was transmitted.
Y
N
Y
FIFO Error Flag 
(MSR[FEF])
The controller expects a Start condition in 
the command FIFO, but the next entry in 
the command FIFO is not a Start condition.
Y
N
Y
Pin Low Timeout Flag 
(MSR[PLTF])
Pin low timeout is enabled and SCL (or 
SDA, if configured) is low for longer than 
the configured timeout.
Y
N
Y
Data Match Flag 
(MSR[DMF])
The received data matches the configured 
data match, but the received data is not 
discarded due to a command FIFO entry.
Y
N
Y
Controller Busy Flag 
(MSR[MBF])
LPI2C controller is busy transmitting or 
receiving data.
N
N
N
Bus Busy Flag 
(MSR[BBF])
LPI2C controller is enabled and activity 
is detected on the I2C bus, but no Stop 
condition is detected and no bus idle 
timeout (if enabled) occurred.
N
N
N
71.3.8.2
Target mode
Table 464 lists the target mode sources that can generate LPI2C target interrupts and LPI2C target transmit and receive 
DMA requests.
Table 464. Target interrupts and DMA requests
Status flag
Description
Can generate
Interrupt?
DMA request?
Low-power 
wake-up?
Transmit Data Flag 
(SSR[TDF])
Data can be written to Target Transmit 
Data (STDR).
Y
TX
Y
Receive Data Flag 
(SSR[RDF])
Data can be read from Target Receive 
Data (SRDR).
Y
RX
Y
Address Valid Flag 
(SSR[AVF])
Address can be read from Target Address 
Status (SASR).
Y
RX
Y
Transmit ACK Flag 
(SSR[TAF])
ACK or NACK can be written to Target 
Transmit ACK (STAR).
Y
N
Y
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2926 / 5251


---
# 페이지 67

Table 464. Target interrupts and DMA requests (continued)
Status flag
Description
Can generate
Interrupt?
DMA request?
Low-power 
wake-up?
Repeated Start Flag 
(SSR[RSF])
Target has detected an address match 
followed by a repeated Start condition.
Y
N
Y
Stop Detect Flag 
(SSR[SDF])
Target has detected an address match 
followed by a Stop condition.
Y
N
Y
Bit Error Flag 
(SSR[BEF])
Target was transmitting data, but received 
data is different from what was transmitted.
Y
N
Y
FIFO Error Flag 
(SSR[FEF])
This flag is set by:
• Transmit data underrun
• Receive data overrun
• Address status overrun when 
SCFGR1[RXCFG] = 1
This flag can only be set when clock 
stretching is disabled.
Y
N
Y
Address Match 0 Flag 
(SSR[AM0F])
Target detected an address match 
SAMR[ADDR0].
Y
N
N
Address Match 1 Flag 
(SSR[AM1F])
Target detected an address match with 
SAMR[ADDR1] or using an address range.
Y
N
N
General Call Flag 
(SSR[GCF])
Target detected an address match with the 
general call address.
Y
N
N
SMBus Alert Response 
Flag (SSR[SARF])
Target detected an address match with the 
SMBus alert address.
Y
N
N
Target Busy Flag 
(SSR[SBF])
LPI2C target is busy receiving an address 
byte or is transmitting or receiving data.
N
N
N
Bus Busy Flag 
(SSR[BBF])
LPI2C target is enabled and a Start 
condition is detected on I2C bus, but no 
Stop condition detected.
N
N
N
71.4 External signals
Table 465. External signals
Signal
Name
Two-wire scheme
Four-wire scheme
Direction
SCL
LPI2C clock line
SCL
In Four-Wire mode, this pin is the SCL input 
pin.
Input
or output
SDA
LPI2C data line
SDA
In Four-Wire mode, this pin is the SDA input 
pin.
Input
or output
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2927 / 5251


---
# 페이지 68

Table 465. External signals (continued)
Signal
Name
Two-wire scheme
Four-wire scheme
Direction
SCLS
Secondary I2C clock 
line
Not used
In Four-Wire mode, this pin is the SCLS 
output pin. If LPI2C controller/target are 
configured to use separate pins, then this 
pin is the LPI2C target SCL pin.
Input
or output
SDAS
Secondary I2C data 
line
Not used
In Four-Wire mode, this pin is the SDAS 
output pin. If LPI2C controller/target are 
configured to use separate pins, then this 
pin is the LPI2C target SDA pin.
Input
or output
HREQ
Host request
If host request is asserted and the I2C bus is idle, then it initiates an 
LPI2C controller transfer.
HREQ is an additional pin separate from the two-wire or four-
wire scheme.
Input
Figure 394 shows the two-signal connection.
MCU
Microcontroller
Data (SDA)
Clock (SCL)
Two-wire
peripheral
device # 1
Target
Two-wire
peripheral
device # 2
I2C (Inter-Integrated Circuit) two-wire serial bus
Target
Two-wire
peripheral
device # 3
Target
Printed circuit board (PCB)
  
 
Figure 394. I2C two-wire serial bus
Figure 395 shows a possible four-signal connection.
SDA
simple line drivers
Vdd
SDAS
SCL
SDA
Microcontroller
side
SCL
SCLS
Vdd of I2C bus
Figure 395. I2C four-wire serial bus
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2928 / 5251


---
# 페이지 69

71.5 Initialization
To initialize the LPI2C controller:
1. Configure Controller Configuration 0 (MCFGR0)–Controller Configuration 3 (MCFGR3) as required by the application.
2. Configure Controller Clock Configuration 0 (MCCR0) and Controller Clock Configuration 1 (MCCR1) to satisfy the timing 
requirements of the I2C mode supported by the application.
3. Enable controller interrupts and DMA requests as required by the application.
4. Enable the LPI2C controller by writing 1 to MCR[MEN].
To initialize the LPI2C target:
1. Configure Target Address Match (SAMR) with the I2C address of the target location on the I2C bus.
2. Configure Target Configuration 1 (SCFGR1) as required by the application.
3. Configure Target Configuration 2 (SCFGR2) to satisfy the timing requirements of the I2C mode supported by the 
application.
4. Enable target interrupts and DMA requests as required by the application.
5. Enable the LPI2C target by writing 1 to SCR[SEN].
71.6 Application information
Configure the I2C timing parameters to meet the requirements of the I2C specification. This configuration depends on the 
supported mode and LPI2C functional clock frequency. When switching between two modes using different clock configuration 
registers (for example, Fast mode and HS mode), MCFGR1[PRESCALE] must remain constant between the modes.
Table 466. Example timing configurations
I2C mode
Clock 
frequency
Baud rate
PRESCALE
FILTSCL / 
FILTSDA
SETHOLD
CLKLO
CLKHI
DATAVD
Standard
8 MHz
100 kbit/s
0h
0h/0h
24h
28h
24h
02h
Standard
48 MHz
100 kbit/s
2h
1h/1h
37h
3Fh
37h
03h
Standard
60 MHz
100 kbit/s
2h
1h/1h
45h
50h
44h
04h
Fast
8 MHz
400 kbit/s
0h
0h/0h
04h
0Bh
05h
02h
Fast+
8 MHz
1 Mbit/s
0h
0h/0h
02h
03h
01h
01h
Fast
48 MHz
400 kbit/s
0h
1h/1h
1Dh
3Eh
35h
0Fh
Fast
48 MHz
400 kbit/s
2h
1h/1h
07h
11h
0Bh
03h
Fast+
48 MHz
1 Mbit/s
2h
1h/1h
03h
06h
04h
04h
HS
48 MHz
3.2 Mbit/s
0h
0h/0h
07h
08h
03h
01h
Fast
60 MHz
400 kbit/s
1h
2h/2h
11h
28h
1Fh
08h
Fast+
60 MHz
1 Mbit/s
1h
2h/2h
07h
0Fh
0Bh
01h
HS
60 MHz
3.33 Mbit/s
1h
0h/0h
04h
04h
02h
01h
71.7 Memory map and registers
71.7.1 LPI2C register descriptions
Writing to a read-only register or reading from a write-only register can cause bus errors. This module does not check whether 
programmed values in the registers are correct; you must ensure that valid programmed values are written to the registers.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2929 / 5251


---
# 페이지 70

71.7.1.1
LPI2C memory map
LPI2C_0 base address: 4035_0000h
LPI2C_1 base address: 4035_4000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
Version ID (VERID)
32
R
0102_0003h
4h
Parameter (PARAM)
32
R
0000_0202h
10h
Controller Control (MCR)
32
RW
0000_0000h
14h
Controller Status (MSR)
32
RW
0000_0001h
18h
Controller Interrupt Enable (MIER)
32
RW
0000_0000h
1Ch
Controller DMA Enable (MDER)
32
RW
0000_0000h
20h
Controller Configuration 0 (MCFGR0)
32
RW
0000_0000h
24h
Controller Configuration 1 (MCFGR1)
32
RW
0000_0000h
28h
Controller Configuration 2 (MCFGR2)
32
RW
0000_0000h
2Ch
Controller Configuration 3 (MCFGR3)
32
RW
0000_0000h
40h
Controller Data Match (MDMR)
32
RW
0000_0000h
48h
Controller Clock Configuration 0 (MCCR0)
32
RW
0000_0000h
50h
Controller Clock Configuration 1 (MCCR1)
32
RW
0000_0000h
58h
Controller FIFO Control (MFCR)
32
RW
0000_0000h
5Ch
Controller FIFO Status (MFSR)
32
R
0000_0000h
60h
Controller Transmit Data (MTDR)
32
W
0000_0000h
70h
Controller Receive Data (MRDR)
32
R
0000_4000h
110h
Target Control (SCR)
32
RW
0000_0000h
114h
Target Status (SSR)
32
RW
0000_0000h
118h
Target Interrupt Enable (SIER)
32
RW
0000_0000h
11Ch
Target DMA Enable (SDER)
32
RW
0000_0000h
124h
Target Configuration 1 (SCFGR1)
32
RW
0000_0000h
128h
Target Configuration 2 (SCFGR2)
32
RW
0000_0000h
140h
Target Address Match (SAMR)
32
RW
0000_0000h
150h
Target Address Status (SASR)
32
R
0000_4000h
154h
Target Transmit ACK (STAR)
32
RW
0000_0000h
160h
Target Transmit Data (STDR)
32
W
0000_0000h
170h
Target Receive Data (SRDR)
32
R
0000_4000h
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2930 / 5251


---
# 페이지 71

71.7.1.2
Version ID (VERID)
Offset
Register
Offset
VERID
0h
Function
Contains version numbers for the module design and feature set.
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
MAJOR 
MINOR 
W
Reset
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
1
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
FEATURE 
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
Fields
Field
Function
31-24
MAJOR
Major Version Number
Returns the major version number for the module design specification.
23-16
MINOR
Minor Version Number
Returns the minor version number for the module design specification.
15-0
FEATURE
Feature Specification Number
Returns the feature set number.
0000_0000_0000_0010b - Controller only, with standard feature set
0000_0000_0000_0011b - Controller and target, with standard feature set
71.7.1.3
Parameter (PARAM)
Offset
Register
Offset
PARAM
4h
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2931 / 5251


---
# 페이지 72

Function
Contains parameter values implemented in the module.
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
MRXFIFO 
0
MTXFIFO 
W
Reset
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
0
1
0
Fields
Field
Function
31-16
—
Reserved
15-12
—
Reserved
11-8
MRXFIFO
Controller Receive FIFO Size
Configures the number of words in the controller receive FIFO to 2MRXFIFO.
7-4
—
Reserved
3-0
MTXFIFO
Controller Transmit FIFO Size
Configures the number of words in the controller transmit FIFO to 2MTXFIFO.
71.7.1.4
Controller Control (MCR)
Offset
Register
Offset
MCR
10h
Function
Contains resets, debug enable, and other controller control settings.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2932 / 5251


---
# 페이지 73

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
0
0
0
DBGE
N 
DOZE
N 
RST 
MEN 
W
RRF 
RTF 
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
31-10
—
Reserved
9
RRF
Reset Receive FIFO
Resets the receive FIFO in Controller Receive Data (MRDR).
0b - No effect
1b - Reset receive FIFO
8
RTF
Reset Transmit FIFO
Resets the transmit FIFO in Controller Transmit Data (MTDR).
0b - No effect
1b - Reset transmit FIFO
7-4
—
Reserved
3
DBGEN
Debug Enable
Enables the controller in Debug mode.
0b - Disable
1b - Enable
2
DOZEN
Doze Mode Enable
Enables the controller in Doze mode.
0b - Enable
1b - Disable
1
Software Reset
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2933 / 5251


---
# 페이지 74

Table continued from the previous page...
Field
Function
RST
Resets all internal controller logic and registers except Controller Control (MCR).
This field remains 1 (enabled) until you write 0 to it. The reset takes effect immediately and remains asserted 
until negated by software. There is no minimum delay required before clearing the software reset.
0b - No effect
1b - Reset
0
MEN
Controller Enable
Enables the controller logic.
0b - Disable
1b - Enable
71.7.1.5
Controller Status (MSR)
Offset
Register
Offset
MSR
14h
Function
Contains status flags for transmit and receive data, for start and stop conditions, and for bus and controller busy or idle status.
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
BBF 
MBF 
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
DMF 
PLTF 
FEF 
ALF 
NDF 
SDF 
EPF 
0
RDF 
TDF 
W
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
1
Fields
Field
Function
31-26
—
Reserved
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2934 / 5251


---
# 페이지 75

Table continued from the previous page...
Field
Function
25
BBF
Bus Busy Flag
Specifies whether the I2C bus is busy.
0b - Idle
1b - Busy
24
MBF
Controller Busy Flag
Specifies whether the I2C controller is busy.
0b - Idle
1b - Busy
23-16
—
Reserved
15
—
Reserved
14
DMF
Data Match Flag
Indicates whether the received data matches MDMR[MATCH0] or MDMR[MATCH1] (as configured by 
MCFGR1[MATCFG]). Received data discarded due to MTDR[CMD] does not cause this flag to set.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Matching data not received
1b - Matching data received
When writing
0b - No effect
1b - Clear the flag
13
PLTF
Pin Low Timeout Flag
Indicates whether pin low timeout has occurred. Sets when the SCL or SDA input is low for more than 
the number of PINLOW cycles defined by MCFGR3[PINLOW], even when the LPI2C controller is idle.
You must resolve the pin low condition via software. PLTF cannot be cleared as long as the pin low timeout 
continues. Before LPI2C can initiate a Start condition, you must clear this flag.
See MCFGR1[TIMECFG] for the SCL and/or SDA timeout settings.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2935 / 5251


---
# 페이지 76

Table continued from the previous page...
Field
Function
0b - Pin low timeout did not occur
1b - Pin low timeout occurred
When writing
0b - No effect
1b - Clear the flag
12
FEF
FIFO Error Flag
Detects the LPI2C controller's attempt to send or receive data without first generating a (repeated) Start 
condition. This error can occur when the transmit FIFO underflows when MCFGR1[AUTOSTOP] = 1. 
When this flag is set, the LPI2C controller sends a Stop condition (if busy). The controller does not 
initiate a new Start condition until the flag is cleared.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No FIFO error
1b - FIFO error
When writing
0b - No effect
1b - Clear the flag
11
ALF
Arbitration Lost Flag
Indicates whether arbitration is lost. Either of these conditions sets this flag:
• The LPI2C controller transmits a logic 1 and detects a logic 0 on the I2C bus.
• The LPI2C controller detects a Start or Stop condition when the LPI2C controller is transmitting data.
When ALF is set, the LPI2C controller releases the I2C bus (goes idle), and the LPI2C controller does not 
initiate a new Start condition until the ALF is cleared.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Controller did not lose arbitration
1b - Controller lost arbitration
When writing
0b - No effect
1b - Clear the flag
10
NACK Detect Flag
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2936 / 5251


---
# 페이지 77

Table continued from the previous page...
Field
Function
NDF
Indicates whether an unexpected NACK has been detected. This flag is set when the LPI2C controller 
detects a NACK it was not expecting when transmitting an address or data. When set, the controller does 
not initiate a new Start condition until this flag is cleared. If a NACK is expected for a given address (as 
configured by the command word), this flag is set if a NACK is not generated.
When this flag is set, the LPI2C controller automatically transmits a Stop condition if 
MCFGR1[AUTOSTOP] = 1, or if the transmit FIFO is not empty.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No unexpected NACK detected
1b - Unexpected NACK detected
When writing
0b - No effect
1b - Clear the flag
9
SDF
Stop Detect Flag
Indicates whether the LPI2C controller has generated a Stop condition.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No Stop condition generated
1b - Stop condition generated
When writing
0b - No effect
1b - Clear the flag
8
EPF
End Packet Flag
Indicates whether the LPI2C controller has generated a repeated Start condition or a Stop condition. 
When the controller first generates a Start condition, this flag is not set.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No Stop or repeated Start generated
1b - Stop or repeated Start generated
When writing
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2937 / 5251


---
# 페이지 78

Table continued from the previous page...
Field
Function
0b - No effect
1b - Clear the flag
7-2
—
Reserved
1
RDF
Receive Data Flag
Indicates whether the receive data is ready. This flag is set when the number of words in the receive 
FIFO is greater than MFCR[RXWATER].
0b - Receive data not ready
1b - Receive data ready
0
TDF
Transmit Data Flag
Indicates whether transmit data is requested. This flag is set when the number of words in the transmit 
FIFO is equal or less than MFCR[TXWATER].
0b - Transmit data not requested
1b - Transmit data requested
71.7.1.6
Controller Interrupt Enable (MIER)
Offset
Register
Offset
MIER
18h
Function
Contains enables for:
• Transmit and receive data interrupts
• Start, Stop, and NACK detection interrupts
• DMA interrupts
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2938 / 5251


---
# 페이지 79

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
DMIE 
PLTIE 
FEIE 
ALIE 
NDIE 
SDIE 
EPIE 
0
RDIE 
TDIE 
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
15
—
Reserved
14
DMIE
Data Match Interrupt Enable
Enables interrupt for data match.
0b - Disable
1b - Enable
13
PLTIE
Pin Low Timeout Interrupt Enable
Enables interrupt for pin-low timeout.
0b - Disable
1b - Enable
12
FEIE
FIFO Error Interrupt Enable
Enables interrupt for FIFO error.
0b - Disable
1b - Enable
11
ALIE
Arbitration Lost Interrupt Enable
Enables interrupt for arbitration lost.
0b - Disable
1b - Enable
10
NACK Detect Interrupt Enable
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2939 / 5251


---
# 페이지 80

Table continued from the previous page...
Field
Function
NDIE
Enables interrupt for NACK detection.
0b - Disable
1b - Enable
9
SDIE
Stop Detect Interrupt Enable
Enables interrupt for Stop detection.
0b - Disable
1b - Enable
8
EPIE
End Packet Interrupt Enable
Enables interrupt for end packet.
0b - Disable
1b - Enable
7-2
—
Reserved
1
RDIE
Receive Data Interrupt Enable
Enables interrupt for receive data.
0b - Disable
1b - Enable
0
TDIE
Transmit Data Interrupt Enable
Enables interrupt for transmit data.
0b - Disable
1b - Enable
71.7.1.7
Controller DMA Enable (MDER)
Offset
Register
Offset
MDER
1Ch
Function
Contains DMA transmit, request, and receive enables.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2940 / 5251


---
# 페이지 81

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
RDDE 
TDDE 
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
RDDE
Receive Data DMA Enable
Enables DMA receive data.
0b - Disable
1b - Enable
0
TDDE
Transmit Data DMA Enable
Enables DMA transmit data.
0b - Disable
1b - Enable
71.7.1.8
Controller Configuration 0 (MCFGR0)
Offset
Register
Offset
MCFGR0
20h
Function
Contains host settings and other receive and transfer settings.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2941 / 5251


---
# 페이지 82

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
RDMO 
CIRFIF
O 
0
0
HRSE
L 
HRPO
L 
HREN 
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
31-18
—
Reserved
17-16
—
Reserved
15-10
—
Reserved
9
RDMO
Receive Data Match Only
Determines whether all received data that does not set MSR[DMF] is discarded. After MSR[DMF] is 
set, the RDMO configuration is ignored. When disabling RDMO, write 0 to this field before writing 0 to 
MSR[DMF] to ensure that no receive data is lost.
0b - Received data is stored in the receive FIFO
1b - Received data is discarded unless MSR[DMF] is set
8
CIRFIFO
Circular FIFO Enable
Enables the transmit FIFO read pointer to be saved to a temporary register. The transmit FIFO empties 
as normal. After the LPI2C controller is idle and the transmit FIFO is empty, the read pointer value is 
restored from the temporary register. This setting causes the contents of the transmit FIFO to be cycled 
through repeatedly. If MCFGR1[AUTOSTOP] is 1, then a Stop condition is sent whenever the transmit 
FIFO is empty and the read pointer is restored.
0b - Disable
1b - Enable
7-4
—
Reserved
3
Reserved
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2942 / 5251


---
# 페이지 83

Table continued from the previous page...
Field
Function
—
2
HRSEL
Host Request Select
Selects the source of the host request input. When host request is enabled, this field must not change.
0b - Host request input is pin HREQ
1b - Host request input is input trigger
1
HRPOL
Host Request Polarity
Configures the polarity of the host request input. When host request is enabled, this field must not change.
HRPOL sets the polarity for both the HREQ pin and the input trigger.
• When HRPOL=0, the polarity is configured for active low, so host request is asserted if the HREQ 
pin or input trigger are logic 0.
• When HRPOL=1, the polarity is configured for active high, so host request is asserted if the HREQ 
pin or input trigger are logic 1.
0b - Active low
1b - Active high
0
HREN
Host Request Enable
Enables host request. When enabled, the LPI2C controller only initiates a Start condition if the host 
request input is asserted and the bus is idle. A repeated Start condition is not affected by the host 
request.
0b - Disable
1b - Enable
71.7.1.9
Controller Configuration 1 (MCFGR1)
Offset
Register
Offset
MCFGR1
24h
Function
Contains controls for pin configuration, clock prescaler, and various other control settings.
Write to this register only when the I2C controller is disabled.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2943 / 5251


---
# 페이지 84

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
Reserv
ed 
PINCFG 
0
MATCFG 
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
TIMEC
FG 
IGNAC
K 
AUTO
STOP 
0
PRESCALE 
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
31-28
—
Reserved
27
—
Reserved
26-24
PINCFG
Pin Configuration
Configures the pin mode for LPI2C.
000b - Two-pin open drain mode. SCL/SDA pins: Bidirectional open drain for controller and target. 
SCLS/SDAS pins: Not used.
001b - Two-pin output only mode (Ultra-Fast mode). SCL/SDA pins: Output-only (Ultra-Fast 
mode) open drain for controller and target. SCLS/SDAS pins: Not used.
010b - Two-pin push-pull mode. SCL/SDA pins: Bidirectional push-pull for controller and target. 
SCLS/SDAS pins: Not used.
011b - Four-pin push-pull mode. SCL/SDA pins: Input only for controller and target. SCLS/SDAS 
pins: Output-only push-pull for controller and target.
100b - Two-pin open-drain mode with separate LPI2C target. SCL/SDA pins: Bidirectional open 
drain for controller. SCLS/SDAS pins: Bidirectional open drain for target.
101b - Two-pin output only mode (Ultra-Fast mode) with separate LPI2C target. SCL/SDA pins: 
Output-only (Ultra-Fast mode) open drain for controller. SCLS/SDAS pins: Output-only open drain 
for target.
110b - Two-pin push-pull mode with separate LPI2C target. SCL/SDA pins: Bidirectional push-pull 
for controller. SCLS/SDAS pins: Bidirectional push-pull for target.
111b - Four-pin push-pull mode (inverted outputs). SCL/SDA pins: Input only for controller and 
target. SCLS/SDAS pins: Inverted output-only push-pull for controller and target.
23-19
—
Reserved
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2944 / 5251


---
# 페이지 85

Table continued from the previous page...
Field
Function
18-16
MATCFG
Match Configuration
Configures the condition that sets MSR[DMF]. See Controller Data Match (MDMR).
000b - Match is disabled
001b - Reserved
010b - Match is enabled: first data word equals MDMR[MATCH0] OR MDMR[MATCH1]
011b - Match is enabled: any data word equals MDMR[MATCH0] OR MDMR[MATCH1]
100b - Match is enabled: (first data word equals MDMR[MATCH0]) AND (second data word 
equals MDMR[MATCH1)
101b - Match is enabled: (any data word equals MDMR[MATCH0]) AND (next data word equals 
MDMR[MATCH1)
110b - Match is enabled: (first data word AND MDMR[MATCH1]) equals (MDMR[MATCH0] AND 
MDMR[MATCH1])
111b - Match is enabled: (any data word AND MDMR[MATCH1]) equals (MDMR[MATCH0] AND 
MDMR[MATCH1])
15-13
—
Reserved
12-11
—
Reserved
10
TIMECFG
Timeout Configuration
Configures which signals must be low for longer than the configured timeout to set MSR[PLTF].
When this field is 0, MSR[PLTF] is set when SCL is low for longer than the configured timeout.
0b - SCL
1b - SCL or SDA
9
IGNACK
Ignore NACK
Determines whether the LPI2C controller ignores a received NACK and treats it as an ACK. This field 
must be 1 in Ultra-Fast mode.
0b - No effect
1b - Treat a received NACK as an ACK
8
AUTOSTOP
Automatic Stop Generation
Determines whether a Stop condition is generated when the LPI2C controller is busy and the transmit 
FIFO is empty. A Stop condition can also be generated using a transmit FIFO command.
When this field is 1, a Stop condition is automatically generated when the transmit FIFO is empty and the 
LPI2C controller is busy.
0b - No effect
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2945 / 5251


---
# 페이지 86

Table continued from the previous page...
Field
Function
1b - Stop automatically generated
7-3
—
Reserved
2-0
PRESCALE
Prescaler
Configures the clock prescaler used for all LPI2C controller logic except the digital glitch filters.
000b - Divide by 1
001b - Divide by 2
010b - Divide by 4
011b - Divide by 8
100b - Divide by 16
101b - Divide by 32
110b - Divide by 64
111b - Divide by 128
71.7.1.10
Controller Configuration 2 (MCFGR2)
Offset
Register
Offset
MCFGR2
28h
Function
Contains the configuration for the bus idle timeout and glitch filters for SDA and SCL.
Write to this register only when the I2C controller is disabled.
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
FILTSDA 
0
FILTSCL 
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
BUSIDLE 
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
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2946 / 5251


---
# 페이지 87

Fields
Field
Function
31-28
—
Reserved
27-24
FILTSDA
Glitch Filter SDA
Configures the I2C controller digital glitch filters for the SDA input.
The latency through the glitch filter is equal to the number of cycles defined by this field. The value of this 
field must be less than the minimum SCL low or high period.
Glitches equal to or less than the number of cycles defined by this field are filtered out and ignored. Writing 
0 to this field disables the glitch filter.
MCFGR1[PRESCALE] does not affect the glitch filter cycle count. It is automatically bypassed in HS mode.
23-20
—
Reserved
19-16
FILTSCL
Glitch Filter SCL
Configures the I2C controller digital glitch filters for SCL input.
The latency through the glitch filter is equal to the number of cycles defined by this field. The value of this 
field must be less than the minimum SCL low or high period.
Glitches equal to or less than the number of cycles defined by this field are filtered out and ignored. These 
cycles are based on the functional clock. Writing 0 to this field disables the glitch filter.
MCFGR1[PRESCALE] does not affect the glitch filter cycle count. It is automatically bypassed in HS mode.
15-12
—
Reserved
11-0
BUSIDLE
Bus Idle Timeout
Configures the bus idle timeout period, in clock cycles.
If both SCL and SDA are high for longer than the number of cycles defined by this field, the I2C bus is 
assumed to be idle and the controller can generate a Start condition.
Writing 0 to this field disables the bus idle timeout.
71.7.1.11
Controller Configuration 3 (MCFGR3)
Offset
Register
Offset
MCFGR3
2Ch
Function
Configures the threshold value for the pin low timeout flag.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2947 / 5251


---
# 페이지 88

Write to this register only when the I2C controller is disabled.
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
PINLOW 
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
PINLOW 
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
31-20
—
Reserved
19-8
PINLOW
Pin Low Timeout
Configures the threshold value, in clock cycles, that sets MSR[PLTF].
If SCL or SDA (selected by MCFGR1[TIMECFG]) is low for longer than (PINLOW × 256) cycles, MSR[PLTF] 
is set.
When this field is 0, the pin low timeout feature is disabled.
7-0
—
Reserved
71.7.1.12
Controller Data Match (MDMR)
Offset
Register
Offset
MDMR
40h
Function
Contains data match values.
Write to this register only when the I2C controller is disabled or idle.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2948 / 5251


---
# 페이지 89

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
MATCH1 
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
MATCH0 
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
31-24
—
Reserved
23-16
MATCH1
Match 1 Value
Specifies match 1 value that is compared to the received data when receive data match is enabled.
15-8
—
Reserved
7-0
MATCH0
Match 0 Value
Specifies match 0 value that is compared to the received data when receive data match is enabled.
71.7.1.13
Controller Clock Configuration 0 (MCCR0)
Offset
Register
Offset
MCCR0
48h
Function
Configures various clock controls.
You cannot make changes to this register when the I2C controller is enabled and is used for standard, fast, fast-mode plus, and 
ultra-fast transfers.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2949 / 5251


---
# 페이지 90

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
DATAVD 
0
SETHOLD 
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
CLKHI 
0
CLKLO 
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
31-30
—
Reserved
29-24
DATAVD
Data Valid Delay
Specifies the minimum number of cycles (minus one) used as the data hold time for SDA. This value 
must be less than the minimum SCL low period.
23-22
—
Reserved
21-16
SETHOLD
Setup Hold Delay
Specifies the minimum number of cycles (minus one) used by the controller for these conditions:
• Hold time for a Start
• Setup and hold time for a repeated Start
• Setup time for a Stop
The setup time is extended by the time it takes to detect a rising edge on the external SCL pin. Ignoring any 
additional board delay due to external loading, this time is equal to (2 + FILTSCL) ÷ 2^PRESCALE cycles.
15-14
—
Reserved
13-8
CLKHI
Clock High Period
Specifies the minimum number of cycles (minus one) that the controller drives the SCL clock high. The 
SCL high time is extended by the time needed to detect a rising edge on the external SCL pin. Ignoring 
any additional board delay due to external loading, this time is equal to (2 + FILTSCL) ÷ 2^PRESCALE 
cycles.
7-6
—
Reserved
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2950 / 5251


---
# 페이지 91

Table continued from the previous page...
Field
Function
5-0
CLKLO
Clock Low Period
Specifies the minimum number of cycles (minus one) that the controller drives the SCL clock low. This 
value is also used for the minimum bus free time between a Stop and a Start condition. This period is 
extended by the time needed to detect a rising edge on the external SCL pin. Ignoring any additional 
board delay due to external loading, this time is equal to (2 + FILTSCL) ÷ 2^PRESCALE cycles.
71.7.1.14
Controller Clock Configuration 1 (MCCR1)
Offset
Register
Offset
MCCR1
50h
Function
Configures various clock controls.
You cannot makes changes to this register when the I2C controller is enabled and is used for HS mode transfers. The separate 
clock configuration for HS mode allows arbitration to take place in Fast mode (with timing configured by Controller Clock 
Configuration 0 (MCCR0)), before switching to HS mode (with timing configured by MCCR1).
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
DATAVD 
0
SETHOLD 
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
CLKHI 
0
CLKLO 
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
31-30
—
Reserved
29-24
DATAVD
Data Valid Delay
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2951 / 5251


---
# 페이지 92

Table continued from the previous page...
Field
Function
Specifies the minimum number of cycles (minus one) used as the data hold time for SDA. This value 
must be less than the minimum SCL low period.
23-22
—
Reserved
21-16
SETHOLD
Setup Hold Delay
Specifies the minimum number of cycles (minus one) used by the controller for these conditions:
• Hold time for a Start condition
• Setup and hold time for a repeated Start condition
• Setup time for a Stop condition
The setup time is extended by the time needed to detect a rising edge on the external SCL pin. Ignoring any 
additional board delay due to external loading, this time is equal to (2 + FILTSCL) ÷ 2^PRESCALE cycles.
15-14
—
Reserved
13-8
CLKHI
Clock High Period
Specifies the minimum number of cycles (minus one) that the controller drives the SCL clock high. The 
SCL high time is extended by the time needed to detect a rising edge on the external SCL pin. Ignoring 
any additional board delay due to external loading, this time is equal to (2 + FILTSCL) ÷ 2^PRESCALE 
cycles.
7-6
—
Reserved
5-0
CLKLO
Clock Low Period
Specifies the minimum number of cycles (minus one) that the controller drives the SCL clock low. This 
value is also used for the minimum bus free time between a Stop and a Start condition. This period is 
extended by the time needed to detect a rising edge on the external SCL pin. Ignoring any additional 
board delay due to external loading, this time is equal to (2 + FILTSCL) ÷ 2^PRESCALE cycles.
71.7.1.15
Controller FIFO Control (MFCR)
Offset
Register
Offset
MFCR
58h
Function
Controls the receive and transmit FIFO watermark values.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2952 / 5251


---
# 페이지 93

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
RXWATER 
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
TXWATER 
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
31-18
—
Reserved
17-16
RXWATER
Receive FIFO Watermark
Determines the watermark for setting SSR[RDF]. That flag is set when the number of words in the 
receive FIFO is greater than the value of this field. Writing a value equal to or greater than the FIFO size 
truncates the value.
15-2
—
Reserved
1-0
TXWATER
Transmit FIFO Watermark
Determines the watermark for setting SSR[TDF]. That flag is set when the number of words in the 
transmit FIFO is equal or less than the value of this field. Writing a value equal to or greater than the 
FIFO size truncates the value.
71.7.1.16
Controller FIFO Status (MFSR)
Offset
Register
Offset
MFSR
5Ch
Function
Specifies the number of words in the transmit and receive FIFOs.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2953 / 5251


---
# 페이지 94

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
RXCOUNT 
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
TXCOUNT 
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
18-16
RXCOUNT
Receive FIFO Count
Specifies the number of words in the receive FIFO.
15-3
—
Reserved
2-0
TXCOUNT
Transmit FIFO Count
Specifies the number of words in the transmit FIFO.
71.7.1.17
Controller Transmit Data (MTDR)
Offset
Register
Offset
MTDR
60h
Function
Configures transmit data:
• An 8-bit write to MTDR[CMD] is ignored and does not increment the FIFO write pointer.
• An 8-bit write to MTDR[DATA] zero-extends the value of MTDR[CMD] and increments the FIFO write pointer.
• A 16-bit or 32-bit write operation writes to both MTDR[CMD] and MTDR[DATA] and increments the FIFO write pointer.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2954 / 5251


---
# 페이지 95

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
0
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
0
CMD 
DATA 
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
31-11
—
Reserved
10-8
CMD
Command Data
Selects command transmitted by controller.
000b - Transmit the value in DATA[7:0]
001b - Receive (DATA[7:0] + 1) bytes. DATA[7:0] is used as a byte counter. Receive that many 
bytes and check each for a data match (if configured) before storing the received data in the 
receive FIFO.
010b - Generate Stop condition on I2C bus
011b - Receive and discard (DATA[7:0] + 1) bytes. DATA[7:0] is used as a byte counter. Receive 
that many bytes but do not check for a data match or store those bytes in the receive FIFO.
100b - Generate (repeated) Start on the I2C bus and transmit the address in DATA[7:0]
101b - Generate (repeated) Start on the I2C bus and transmit the address in DATA[7:0] (this 
transfer expects a NACK to be returned)
110b - Generate (repeated) Start on the I2C bus and transmit the address in DATA[7:0] using HS 
mode
111b - Generate (repeated) Start on the I2C bus and transmit the address in DATA[7:0] using HS 
mode (this transfer expects a NACK to be returned)
7-0
DATA
Transmit Data
Contains data used by the commands listed in MTDR[CMD]. Performing an 8-bit write to this field 
zero-extends the value of MTDR[CMD].
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2955 / 5251


---
# 페이지 96

71.7.1.18
Controller Receive Data (MRDR)
Offset
Register
Offset
MRDR
70h
Function
Contains the status of the receive FIFO and the data received by the I2C controller that has not been discarded.
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
RXEM
PTY 
0
DATA 
W
Reset
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
0
Fields
Field
Function
31-15
—
Reserved
14
RXEMPTY
Receive Empty
Indicates whether the controller receive data FIFO is empty.
0b - Not empty
1b - Empty
13-8
—
Reserved
7-0
DATA
Receive Data
Contains data received by the I2C controller that has not been discarded. Received data can be 
discarded due to the command in MTDR[CMD], or the controller can be configured to discard 
nonmatching data.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2956 / 5251


---
# 페이지 97

71.7.1.19
Target Control (SCR)
Offset
Register
Offset
SCR
110h
Function
Contains resets and other target control settings.
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
0
0
0
FILTD
Z 
FILTE
N 
0
RST 
SEN 
W
RRF 
RTF 
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
31-10
—
Reserved
9
RRF
Reset Receive FIFO
Empties the receive FIFO in Target Receive Data (SRDR).
0b - No effect
1b - SRDR is now empty
8
RTF
Reset Transmit FIFO
Empties the transmit FIFO in Target Transmit Data (STDR).
0b - No effect
1b - STDR is now empty
7-6
—
Reserved
5
Filter Doze Enable
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2957 / 5251


---
# 페이지 98

Table continued from the previous page...
Field
Function
FILTDZ
Enables filter in Doze mode. Update this field only when the I2C target is disabled.
0b - Enable
1b - Disable
4
FILTEN
Filter Enable
Enables digital filter and output delay counter for target mode. Update this field only when the I2C target 
is disabled.
0b - Disable
1b - Enable
3-2
—
Reserved
1
RST
Software Reset
Resets target mode logic. The reset takes effect immediately. The value of this field remains 1 until you 
write 0 to it. There is no minimum delay required before clearing the software reset.
0b - Not reset
1b - Reset
0
SEN
Target Enable
Enables I2C Target mode.
0b - Disable
1b - Enable
71.7.1.20
Target Status (SSR)
Offset
Register
Offset
SSR
114h
Function
Contains status flags for transmit and receive data, for error conditions, and for bus and target busy or idle status.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2958 / 5251


---
# 페이지 99

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
BBF 
SBF 
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
SARF 
GCF 
AM1F 
AM0F 
FEF 
BEF 
SDF 
RSF 
0
TAF 
AVF 
RDF 
TDF 
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
31-26
—
Reserved
25
BBF
Bus Busy Flag
Indicates whether an I2C bus is idle or busy.
0b - Idle
1b - Busy
24
SBF
Target Busy Flag
Indicates whether an I2C target is idle or busy.
0b - Idle
1b - Busy
23-16
—
Reserved
15
SARF
SMBus Alert Response Flag
Indicates whether an SMBus alert response has been detected.
You can clear this flag by reading Target Address Status (SASR). This flag cannot generate an 
asynchronous wakeup.
0b - Disabled or not detected
1b - Enabled and detected
14
GCF
General Call Flag
Indicates whether a target has detected the general call address.
You can clear this flag by reading Target Address Status (SASR). This flag cannot generate an 
asynchronous wakeup.
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2959 / 5251


---
# 페이지 100

Table continued from the previous page...
Field
Function
0b - General call address disabled or not detected
1b - General call address detected
13
AM1F
Address Match 1 Flag
Indicates whether the received address matches the value in ADDR1, or it falls within the ADDR0 to 
ADDR1 range as configured by SCFGR1[ADDRCFG].
This flag is cleared by reading Target Address Status (SASR). This flag cannot generate an 
asynchronous wakeup.
0b - Matching address not received
1b - Matching address received
12
AM0F
Address Match 0 Flag
Indicates whether the received address matches the ADDR0 field, as configured by 
SCFGR1[ADDRCFG].
This flag is cleared by reading Target Address Status (SASR). This flag cannot generate an 
asynchronous wakeup.
0b - ADDR0 matching address not received
1b - ADDR0 matching address received
11
FEF
FIFO Error Flag
Indicates whether there is a FIFO error. This flag can only be set when clock stretching is disabled.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No FIFO error
1b - FIFO error
When writing
0b - No effect
1b - Clear the flag
10
BEF
Bit Error Flag
Indicates whether the LPI2C target has transmitted a logic 1 and detects a logic 0 on the I2C bus. The 
target ignores the rest of the transfer until the next (repeated) Start condition.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No bit error occurred
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2960 / 5251


---
# 페이지 101

Table continued from the previous page...
Field
Function
1b - Bit error occurred
When writing
0b - No effect
1b - Clear the flag
9
SDF
Stop Detect Flag
Indicates whether the LPI2C target detects a Stop condition, and if the LPI2C target matched the last 
address byte.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No Stop detected
1b - Stop detected
When writing
0b - No effect
1b - Clear the flag
8
RSF
Repeated Start Flag
Indicates whether the LPI2C target detects a repeated Start condition and if the LPI2C target matched 
the last address byte. This flag is not set when the target first detects a Start condition.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No repeated Start detected
1b - Repeated Start detected
When writing
0b - No effect
1b - Clear the flag
7-4
—
Reserved
3
TAF
Transmit ACK Flag
Indicates whether a transmit ACK or NACK is required. You can clear this flag by writing to Target 
Transmit ACK (STAR).
0b - Not required
1b - Required
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2961 / 5251


---
# 페이지 102

Table continued from the previous page...
Field
Function
2
AVF
Address Valid Flag
Indicates whether the contents of Target Address Status (SASR) are valid. You can clear this flag by 
reading SASR. When SCFGR1[RXCFG] = 1, this flag is also cleared by reading Target Receive Data 
(SRDR).
0b - Not valid
1b - Valid
1
RDF
Receive Data Flag
Indicates whether receive data is ready. You can clear this flag by reading Target Receive Data (SRDR). 
When SCFGR1[RXCFG] = 1, this flag is not cleared when reading Target Receive Data (SRDR) if 
SSR[AVF] = 1.
0b - Not ready
1b - Ready
0
TDF
Transmit Data Flag
Indicates whether transmit data has been requested. This flag is cleared by writing to Target Transmit 
Data (STDR). When SCFGR1[TXCFG] = 0, if a NACK, repeated Start, or Stop condition is detected, this 
flag is also cleared.
0b - Transmit data not requested
1b - Transmit data is requested
71.7.1.21
Target Interrupt Enable (SIER)
Offset
Register
Offset
SIER
118h
Function
Contains transmit and receive data interrupt enables, start and stop detect interrupt enables, and other target interrupt 
enables.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2962 / 5251


---
# 페이지 103

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
SARIE 
GCIE 
AM1IE 
AM0IE 
FEIE 
BEIE 
SDIE 
RSIE 
0
TAIE 
AVIE 
RDIE 
TDIE 
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
15
SARIE
SMBus Alert Response Interrupt Enable
Enables interrupt for SMBus alert response.
0b - Disable
1b - Enable
14
GCIE
General Call Interrupt Enable
Enables interrupt for general call.
0b - Disabled
1b - Enabled
13
AM1IE
Address Match 1 Interrupt Enable
Enables interrupt for address match 1.
0b - Disable
1b - Enable
12
AM0IE
Address Match 0 Interrupt Enable
Enables interrupt for address match 0.
0b - Disable
1b - Enable
11
FEIE
FIFO Error Interrupt Enable
Enables interrupt for FIFO error.
0b - Disable
1b - Enable
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2963 / 5251


---
# 페이지 104

Table continued from the previous page...
Field
Function
10
BEIE
Bit Error Interrupt Enable
Enables interrupt for bit error.
0b - Disable
1b - Enable
9
SDIE
Stop Detect Interrupt Enable
Enables interrupt for Stop detection.
0b - Disable
1b - Enable
8
RSIE
Repeated Start Interrupt Enable
Enables interrupt for repeated start.
0b - Disable
1b - Enable
7-4
—
Reserved
3
TAIE
Transmit ACK Interrupt Enable
Enables interrupt for transmit ACK.
0b - Disable
1b - Enable
2
AVIE
Address Valid Interrupt Enable
Enables interrupt for valid address.
0b - Disable
1b - Enable
1
RDIE
Receive Data Interrupt Enable
Enables interrupt for receive data.
0b - Disable
1b - Enable
0
TDIE
Transmit Data Interrupt Enable
Enables interrupt for transmit data.
0b - Disable
1b - Enable
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2964 / 5251


---
# 페이지 105

71.7.1.22
Target DMA Enable (SDER)
Offset
Register
Offset
SDER
11Ch
Function
Contains the transmit, request, and receive enables for DMA.
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
AVDE 
RDDE 
TDDE 
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
31-3
—
Reserved
2
AVDE
Address Valid DMA Enable
Enables address valid DMA request. The address valid DMA request is shared with the receive data 
DMA request. If both are enabled, write 1 to SCFGR1[RXCFG] to allow the DMA to read the address 
from Target Receive Data (SRDR).
0b - Disable
1b - Enable
1
RDDE
Receive Data DMA Enable
Enables receive data for DMA.
0b - Disable DMA request
1b - Enable DMA request
0
TDDE
Transmit Data DMA Enable
Enables transmit data for DMA.
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2965 / 5251


---
# 페이지 106

Table continued from the previous page...
Field
Function
0b - Disable
1b - Enable
71.7.1.23
Target Configuration 1 (SCFGR1)
Offset
Register
Offset
SCFGR1
124h
Function
Configures various aspects of the target.
Write to this register only when the I2C target is disabled.
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
ADDRCFG 
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
HSME
N 
IGNAC
K 
RXCF
G 
TXCF
G 
SAEN 
GCEN 
0
0
ACKS
TALL 
TXDS
TALL 
RXST
ALL 
ADRS
TALL 
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
31-27
—
Reserved
26-24
—
Reserved
23-19
—
Reserved
18-16
Address Configuration
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2966 / 5251


---
# 페이지 107

Table continued from the previous page...
Field
Function
ADDRCFG
Configures the condition that causes an address to match.
000b - Address match 0 (7-bit)
001b - Address match 0 (10-bit)
010b - Address match 0 (7-bit) or address match 1 (7-bit)
011b - Address match 0 (10-bit) or address match 1 (10-bit)
100b - Address match 0 (7-bit) or address match 1 (10-bit)
101b - Address match 0 (10-bit) or address match 1 (7-bit)
110b - From address match 0 (7-bit) to address match 1 (7-bit)
111b - From address match 0 (10-bit) to address match 1 (10-bit)
15-14
—
Reserved
13
HSMEN
HS Mode Enable
Enables detection of the HS mode controller code of target address 0000_1XX, but does not cause 
an address match on this code. When this field is 1 and any HS mode controller code is detected, 
SCR[FILTEN] and SCFGR1[ACKSTALL] are ignored until the next Stop condition is detected.
0b - Disable
1b - Enable
12
IGNACK
Ignore NACK
Determines whether the target ends transfer when a NACK condition is detected. When this field is 1, 
the LPI2C target continues transfers after a NACK is detected. This field is required to be 1 in Ultra-Fast 
mode.
0b - End transfer on NACK
1b - Do not end transfer on NACK
11
RXCFG
Receive Data Configuration
Configures which data is returned and which flags are cleared when reading Target Receive Data (SRDR).
When this field is 0, reading SRDR returns received data and clears SSR[RDF].
When this field is 1, reading SRDR:
• Returns the value of Target Address Status (SASR) and clears SSR[AVF] when SSR[AVF] is set.
• Returns received data and clears SSR[RDF] when SSR[AVF] is not set.
0b - Return received data, clear SSR[RDF]
1b - Return SASR and clear SSR[AVF] when SSR[AVF] is set, return received data and clear 
SSR[RDF] when SSR[AFV] is not set
10
TXCFG
Transmit Flag Configuration
Determines which conditions set SSR[TDF].
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2967 / 5251


---
# 페이지 108

Table continued from the previous page...
Field
Function
This field always becomes 1 before a NACK is detected at the end of a target-transmit transfer. This change 
can cause an extra word to be written to the transmit data FIFO.
When this field is 0, Target Transmit Data (STDR) is automatically emptied when a target-transmit transfer 
is detected. SSR[TDF] is set when a target-transmit transfer is detected, and SSR[TDF] is cleared at the end 
of the target-transmit transfer.
When this field is 1, SSR[TDF] is set when STDR is empty, and SSR[TDF] is cleared when STDR is full. This 
setting allows STDR to be filled before a target-transmit transfer is detected. However, it can cause STDR 
to be written before a NACK is detected on the last byte of a target-transmit transfer.
0b - SSR[TDF] is set only during a target-transmit transfer when STDR is empty
1b - SSR[TDF] is set whenever STDR is empty
9
SAEN
SMBus Alert Enable
Enables a match on an SMBus alert.
0b - Disable
1b - Enable
8
GCEN
General Call Enable
Enables a general call address.
0b - Disable
1b - Enable
7-5
—
Reserved
4
—
Reserved
3
ACKSTALL
ACK SCL Stall
Enables SCL clock stretching during target-transmit address bytes and target-receiver address and data 
bytes, so you can write to Target Transmit ACK (STAR) before the ACK or NACK is transmitted. Clock 
stretching occurs when transmitting the ninth bit, and is therefore not compatible with HS mode.
If this field is 1:
• You do not need to write 1 to SCFGR1[RXSTALL] or SCFGR1[ADRSTALL].
• When there is an address match on the first byte of a 10-bit address, SSR[AVF] is set, allowing you 
to read the received address before writing to Target Transmit ACK (STAR).
0b - Disable
1b - Enable
2
TXDSTALL
Transmit Data SCL Stall
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2968 / 5251


---
# 페이지 109

Table continued from the previous page...
Field
Function
Enables SCL clock stretching when SSR[TDF] = 1 during a target-transmit transfer. Clock stretching 
occurs following the ninth bit, and is therefore compatible with HS mode.
0b - Disable
1b - Enable
1
RXSTALL
RX SCL Stall
Enables SCL clock stretching when SSR[RDF] = 1 during a target-receive transfer. Clock stretching 
occurs following the ninth bit, and is therefore compatible with HS mode.
0b - Disable
1b - Enable
0
ADRSTALL
Address SCL Stall
Enables SCL clock stretching when SSR[AVF] = 1. Clock stretching only occurs following the ninth bit, 
and is therefore compatible with HS mode.
0b - Disable
1b - Enable
71.7.1.24
Target Configuration 2 (SCFGR2)
Offset
Register
Offset
SCFGR2
128h
Function
Configures data valid delay, clock hold time, and glitch filters for SDA and SCL.
Write to this register only when the I2C target is disabled.
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
FILTSDA 
0
FILTSCL 
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
DATAVD 
0
CLKHOLD 
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
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2969 / 5251


---
# 페이지 110

Fields
Field
Function
31-28
—
Reserved
27-24
FILTSDA
Glitch Filter SDA
Configures the I2C target digital glitch filters for SDA input.
Writing 0 to this field disables the glitch filter.
Glitches equal to or less than the number of cycles defined by this field are filtered out and ignored.
The latency through the glitch filter is equal to the number of cycles defined by this field  + 3. The latency 
must be configured to be less than the minimum SCL low or high period.
MCFGR1[PRESCALE] does not affect the glitch filter cycle count, and the glitch filter cycle count is disabled 
in HS mode.
23-20
—
Reserved
19-16
FILTSCL
Glitch Filter SCL
Configures the I2C target digital glitch filters for SCL input.
Writing 0 to this field disables the glitch filter.
Glitches equal to or less than the number of cycles defined by this field are filtered out and ignored.
The latency through the glitch filter is equal to the number of cycles defined by this field  + 3. The latency 
must be configured to be less than the minimum SCL low or high period.
MCFGR1[PRESCALE] does not affect the glitch filter cycle count, and the glitch filter cycle count is disabled 
in HS mode.
15-14
—
Reserved
13-8
DATAVD
Data Valid Delay
Configures the SDA data valid delay time for the I2C target, which is equal to 
FILTSCL + DATAVD + 3 cycles.
The data valid delay must be configured to be less than the minimum SCL low period.
MCFGR1[PRESCALE] does not affect the I2C target data valid delay time, and the I2C target data valid 
delay time is disabled in HS mode.
7-4
—
Reserved
3-0
CLKHOLD
Clock Hold Time
Configures the minimum clock hold time for the I2C target, when clock stretching is enabled.
The minimum hold time is equal to the number of cycles defined by this field + 3.
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2970 / 5251


---
# 페이지 111

Table continued from the previous page...
Field
Function
MCFGR1[PRESCALE] does not affect the I2C target clock hold time, and the I2C target clock hold time is 
disabled in HS mode.
71.7.1.25
Target Address Match (SAMR)
Offset
Register
Offset
SAMR
140h
Function
Contains address values for received target match comparison.
Write to this register only when the I2C target is disabled.
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
ADDR1 
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
ADDR0 
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
31-27
—
Reserved
26-17
ADDR1
Address 1 Value
Contains the value of address 1, which is compared to the received address to detect the target address.
In 10-bit mode, the first address byte is compared to {11110, ADDR1[26:25]} and the second address byte 
is compared to ADDR1[24:17].
In 7-bit mode, the address is compared to ADDR1[23:17].
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2971 / 5251


---
# 페이지 112

Table continued from the previous page...
Field
Function
16-11
—
Reserved
10-1
ADDR0
Address 0 Value
Contains the value of address 0, which is compared to the received address to detect the target address.
In 10-bit mode, the first address byte is compared to {11110, ADDR0[10:9]} and the second address byte 
is compared to ADDR0[8:1].
In 7-bit mode, the address is compared to ADDR0[7:1].
0
—
Reserved
71.7.1.26
Target Address Status (SASR)
Offset
Register
Offset
SASR
150h
Function
Contains the received address and its validity.
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
ANV 
0
RADDR 
W
Reset
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
0
Fields
Field
Function
31-15
Reserved
Table continues on the next page...
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2972 / 5251


---
# 페이지 113

Table continued from the previous page...
Field
Function
—
14
ANV
Address Not Valid
Indicates whether SASR[RADDR] is valid.
0b - Valid
1b - Not valid
13-11
—
Reserved
10-0
RADDR
Received Address
Contains the received address. Updates whenever SSR[AM0F] or SSR[AM1F] is set. Reading Target 
Address Status (SASR) clears SSR[AM0F] and SSR[AM1F].
In 7-bit mode, the address byte is stored in RADDR[7:0].
In 10-bit mode, the first address byte is {11110, RADDR[10:9], RADDR[0]} and the second address byte is 
RADDR[8:1]. The Read-or-Write bit is therefore always stored in RADDR[0].
When SCFGR1[ACKSTALL] = 1, if the first address byte matches in 10-bit mode, the first address byte is 
stored in RADDR[7:0] so you can read this field before writing the Transmit ACK. If the second address byte 
matches, this field is then updated with the full 10-bit address.
71.7.1.27
Target Transmit ACK (STAR)
Offset
Register
Offset
STAR
154h
Function
Configures choice of ACK or NACK on each received word.
You can write to this register only when SCFGR1[ACKSTALL] = 1.
SCFGR1[ACKSTALL] enables clock stretching during the ACK-or-NACK bit slot. During this time, you can write to this register.
The logic ensures that the clock stretching continues for at least one bus clock cycle after this register is updated.
This clock stretching time can be extended via SCFGR2[CLKHOLD].
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2973 / 5251


---
# 페이지 114

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
TXNA
CK 
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
TXNACK
Transmit NACK
Selects whether transmit ACK (logic 0) or NACK (logic 1) is returned on the bus by the I2C target after 
receiving each word.
• When SCFGR1[ACKSTALL] = 1, a transmit NACK signal must be written once for each matching 
address byte and each received word. SCFGR1[ACKSTALL] must be 1, because that setting stalls 
the data transfer until software reads the received word (and determines whether to respond with an 
ACK or NACK).
• To configure the default (ACK or NACK), you can write to this field when LPI2C target is disabled or 
idle.
0b - Transmit ACK
1b - Transmit NACK
71.7.1.28
Target Transmit Data (STDR)
Offset
Register
Offset
STDR
160h
Function
Contains the I2C target data to transmit.
Clock stretching (enabled or disabled) affects when the transmit data is transferred. SCFGR1[TXDSTALL] enables clock 
stretching during the first data bit of a target-transmit transfer.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2974 / 5251


---
# 페이지 115

If clock stretching is enabled (SCFGR1[TXDSTALL] = 1), the transmit data transfer is stalled until this register is updated. Clock 
stretching is extended by at least 1 bus clock cycle after this register is updated. Clock stretching can be delayed further by 
using SCFGR2[CLKHOLD].
If clock stretching is disabled (SCFGR1[TXDSTALL] = 0), the transmit data must be written before the start of the target-transmit 
transfer, otherwise SSR[FEF] is set.
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
0
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
0
DATA 
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
31-8
—
Reserved
7-0
DATA
Transmit Data
Contains the I2C target data to transmit. Writing data to this register stores I2C target transmit data in 
this register.
71.7.1.29
Target Receive Data (SRDR)
Offset
Register
Offset
SRDR
170h
Function
Contains status of target receive data transfer.
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2975 / 5251


---
# 페이지 116

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
SOF 
RXEM
PTY 
0
RADDR 
DATA 
W
Reset
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
0
Fields
Field
Function
31-16
—
Reserved
15
SOF
Start of Frame
Indicates whether this data word is the first data word since a (repeated) Start or Stop condition.
0b - Not first
1b - First
14
RXEMPTY
Receive Empty
Indicates whether this register is empty.
0b - Not empty
1b - Empty
13-11
—
Reserved
10-8
RADDR
Received Address
Contains the address received by the IC2 target. When both SCFGR1[RXCFG] and SSR[AVF] are 1, bits 
[10:8] of SASR[RADDR] are returned. Otherwise, this field returns zero.
7-0
DATA
Received Data
Contains the data received by the I2C target. When both SCFGR1[RXCFG] and SSR[AVF] are 1, bits [7:0] 
of SASR[RADDR] are returned.
71.8 Glossary
HREQ
Host request
SCL
Serial clock line
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2976 / 5251


---
# 페이지 117

SCLS
Secondary serial clock line
SDA
Serial data line
SDAS
Secondary serial data line
NXP Semiconductors
Low Power Inter-Integrated Circuit (LPI2C)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
2977 / 5251


---