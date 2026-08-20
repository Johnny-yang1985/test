# 페이지 1727

Chapter 77
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
77.1 Chip-specific LPUART information
77.1.1 LPUART instances and configuration
Table 686. LPUART instances
Instance
S32K314/S32K324/S32K44/S32K358/S32K348/
S32K338/S32K328/S32K388/S32K389
S32K310/S32K311/S32K322/
S32K342/S32K341
S32K312
LPUART_0
Yes
Yes
Yes
LPUART_1
Yes
Yes
Yes
LPUART_2
Yes
Yes
Yes
LPUART_3
Yes
Yes
Yes
LPUART_4
Yes
No
Yes
LPUART_5
Yes
No
Yes
LPUART_6
Yes
No
Yes
LPUART_7
Yes
No
Yes
LPUART_8
Yes
No
No
LPUART_9
Yes
No
No
LPUART_10
Yes
No
No
LPUART_11
Yes
No
No
LPUART_12
Yes
No
No
LPUART_13
Yes
No
No
LPUART_14
Yes
No
No
LPUART_15
Yes
No
No
Table 687. LPUART Configuration
Feature
Configuration
S32K344/S32K324/
S32K314/S32K312
S32K342/
S32K322/S32K341/
S32K311/S32K310
S32K358/S32K348/S32K338/
S32K328/S32K388/S32K389
TX FIFO size
4 Words
16 Words (for instance 0,1)
4 Words (for instance 2,3)
16 Words (for instance 0,1)
4 Words (for instance 2 to 15)
RX FIFO size
4 Words
16 Words (for instance 0,1)
4 Words (for instance 2,3)
16 Words (for instance 0,1)
4 Words (for instance 2 to 15)
Table continues on the next page...
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4587 / 5251


---
# 페이지 1728

Table 687. LPUART Configuration (continued)
Feature
Configuration
Functionality supported
Standard LPUART functionality 
with MODEM/IrDA
• Standard LPUART functionality with MODEM/IrDA
• MODBUS and PPROFIBUS support1
LIN master and slave operation
1. Only supported for instance LPUART_0 and LPUART_1.
 
LPUART instances are not available during Standby.
LPUART[0:2]_trg_input is coming from TRGMUX and you should take care of the pulse width of trigger. It 
should follow the requirement mentioned in section "Peripheral Triggers". These triggers are not present 
in S32K314, S32K324, S32K344.
  NOTE  
77.2 Overview
LPUART provides asynchronous, serial communication capabilities with external devices. It supports the non-return-to-zero 
(NRZ) encoding format and infrared data association (IrDA)-compatible, low-speed serial infrared (SIR) protocol. LPUART can 
continue operating when the processor is in Low-Power mode, if an appropriate peripheral clock is available.
77.2.1 Block diagram
Figure 489 shows the transmitter portion of LPUART.
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4588 / 5251


---
# 페이지 1729

Internal chip peripheral bus
Write-only
CTRL[R9T8]
Parity generation
Transmit control
LPUART controls TxD
TxD direction
Load from FIFO
Shift enable
Preamble (all 1s)
Break (all 0s)
CTRL[PE]
CTRL[PT]
STAT[TDRE]
TX interrupt request
TxD logic
CTRL[TIE]
CTRL[M]
Transmit FIFO
Loop control
To receive data in
To TxD pin
OSR divider
Baud divider
Asynchronous
module clock
CTRL[LOOPS]
CTRL[RSRC]
CTRL[TXINV]
CTRL[TE]
CTRL[SBK]
CTRL[TXDIR]
STAT[BRK13]
11-bit Transmit shift register
Stop
H 8 7 6 5 4 3 2 1 0 L
Start
lsb
STAT[TC]
CTRL[TCIE]
Shift direction
Figure 489. Transmitter block diagram
Figure 490 shows the receiver portion of LPUART.
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4589 / 5251


---
# 페이지 1730

Receiver
source
control
Baud rate
generator
Variable 12-bit Receive
Shift Register
Receive FIFO
Internal chip peripheral bus
Shift direction
Stop
Start
Active edge
detect
Receive data
CTRL[LOOPS]
CTRL[RSRC]
CTRL[M]
BAUD[M10]
STAT[LBKDE]
 STAT[MSBF]
STAT[RXINV]
CTRL[RE]
 STAT[RAF]
BAUD[SBR]
From transmitter
IRQ and
DMA logic
Wakeup
logic
Parity
logic
Receive data
 (from RxD)
DMA requests
IRQ requests
Receive
control
CTRL[PE]
CTRL[PT]
Asynchronous
module clock
Figure 490. Receiver block diagram
77.2.2 Features
• Full-duplex, standard NRZ format
• Programmable baud rates (13-bit modulo divider) with a configurable oversampling ratio (OSR) from 4× to 32×
• Asynchronous operation of transmit and receive baud rates with respect to the bus clock:
— Baud rate can be configured independently of the bus clock frequency.
— Operation in Low-Power modes is supported.
• Interrupt, DMA, or polled operations:
— Transmit data empty and transmission complete
— Receive data full
— Receive overrun, parity error, framing error, and noise error
— Idle receiver detect
— Active edge on receive pin
— Break detect supporting LIN
— Receive data match
• Hardware parity generation and checking
• Programmable 7-bit, 8-bit, 9-bit, or 10-bit character length
• Programmable 1-bit or 2-bit stop bits
• Support for three receiver wake-up methods:
— Idle line wake-up
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4590 / 5251


---
# 페이지 1731

— Address mark wake-up
— Receive data match
• Automatic address matching to reduce ISR overhead:
— Address mark matching
— Idle line address matching
— Address match start, address match end
• Optional 13-bit and 11-bit break character generation
• Configurable idle length detection supporting 1, 2, 4, 8, 16, 32, 64, or 128 idle characters
• Selectable transmitter output and receiver input polarity
• Hardware flow control support for request to send (RTS) and clear to send (CTS) signals
• Selectable IrDA 1.4 return-to-zero-inverted (RZI) format with a programmable pulse width
• Independent FIFO structure for transmit and receive functions:
— Separate configurable watermarks for receive and transmit requests
— Option for receiver to assert request after a configurable number of idle characters, if receive FIFO is not empty
77.3 Functional description
LPUART supports full-duplex, asynchronous, NRZ serial communication and comprises a baud rate generator, transmitter, 
and receiver block. The transmitter and receiver operate independently, although they use the same baud rate generator. The 
following sections describe all LPUART blocks.
77.3.1 Baud rate generation
A 13-bit modulus counter in the baud rate generator derives the baud rate for both the receiver and transmitter. The value, ranging 
from 1 to 8191, written to BAUD[SBR] determines the baud clock divisor for the asynchronous LPUART baud clock. The baud 
rate clock drives the receiver, while a bit clock, generated from the baud rate clock divided by the OSR, drives the transmitter. 
Depending on the OSR, the receiver has an acquisition rate of 4 to 32 samples per bit time. LPUART requires BAUD[SBR] and 
BAUD[OSR] to accurately match the baud rate requirement. There is a relationship between the required baud rate and the input 
clock frequency, SBR, and OSR. See the below figure for details.
Modulo divide by
1 - 8191
BAUD[SBR]
Divide by
OSR + 1
OSR
Rx sampling clock
[(OSR+1) × baud rate]
LPUART asynchronous module clock
BAUD[SBR] × (OSR+1) 
Tx baud rate
Baud rate generator
off if BAUD[SBR] = 0 
Baud rate =
LPUART asynchronous
module clock
Figure 491. Baud rate generation
Baud rate generation is subject to these sources of error:
• Integer division of the asynchronous LPUART baud clock may not give the exact target frequency.
• Synchronization with the asynchronous LPUART baud clock can lead to a phase shift.
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4591 / 5251


---
# 페이지 1732

Baud rate generation is a free-running counter that continues whenever the transmitter or receiver is enabled. The transmitter bit 
clock continues whenever the transmitter is enabled; each transmitted character aligns to the next edge of the transmit bit clock.
In general, configuring OSR for a higher ratio and/or sampling on both edges of the clock slightly improves LPUART's tolerance 
to baud rate mismatch between the received data and LPUART configured baud rate. However, the three data samples in each 
bit (see Data sampling technique) are also closer together, which may impact noise sensitivity.
77.3.2 Baud rate tolerance
A transmitting device may operate at a baud rate below or above that of the receiver.
Accumulated bit time misalignment can cause one of the three stop bit data samples to fall outside the actual stop bit. A noise error 
will occur if the three samples are not all the same logical values. A framing error will occur if the receiver clock is misaligned in 
such a way that the majority of the three stop bit samples are a logic zero.
As the receiver samples an incoming frame, it may resynchronize the oversampling clock on any valid falling edge within the frame. 
Resynchronization within frames will correct a misalignment between transmitter bit times and receiver bit times.
In general, increasing the number of samples per bit will increase the baud rate tolerance and decreasing the number of samples 
per bit will reduce the baud rate tolerance. Note that since LPUART implements triple voting on consecutive receive data samples, 
increasing the number of samples per bit will move those samples closer together which would reduce the width of noise that can 
be filtered by the triple voting logic.
77.3.3 Calculating baud rate tolerance
Using the following definitions:
• SAM is the number of sample points per bit (valid range from 8 to 32; equal to (OSR + 1) × (BOTHEDGE + 1)).
• BIT is the number of bits in a character including start, data and stop bits (valid range from 9 to 13).
The ideal baud rate tolerance can be calculated as follows:
• Slow data rate tolerance = ( (SAM ÷ 2) - 1) ÷ ((SAM × BIT) - (SAM ÷ 2) + 2)
• Fast data rate tolerance = ( (SAM ÷ 2) - 2) ÷ (SAM × BIT)
As an example, if configured for 8-bit data, 1 stop bit (BIT = 10) and with OSR=0x7 and BOTHEDGE = 1 (SAM = 16):
• Slow data rate tolerance = (8 - 1) ÷ (160 - 8 + 2) = 7 ÷ 154 = 4.54%
• Fast data rate tolerance = (8 - 2) ÷ 160 = 6 ÷ 160 = 3.75%
If configured for 9-bit data with 1 stop bit (BIT = 11) with same oversampling configuration, then:
• Slow data rate tolerance = (8 - 1) ÷ (176 - 8 + 2) = 7 ÷ 170 = 4.12%
• Fast data rate tolerance = (8 - 2) ÷ 176 = 6 ÷ 176 = 3.41%
 
Additional factors can contribute to a lower baud rate tolerance than the ideal. These include clock uncertainty 
or jitter on the LPUART functional clock source, differences in rise and fall times on the transmitter output and 
synchronization of the external receive pin to the local LPUART functional clock.
  NOTE  
77.3.4 Transmitter functional description
This section describes the functioning of the LPUART transmitter, as shown in the transmitter portion of Block diagram, as well 
as specialized functions for sending break and idle characters.
The transmitter output (TXD) idle state defaults to logic high; the transmitter output is inverted when you write 1 to CTRL[TXINV], 
which becomes 0 following reset. You can enable the transmitter by writing 1 to CTRL[TE]. This queues a preamble character 
that is one full character frame of the Idle state. The transmitter then remains idle until data is available in the transmit FIFO and 
programs store data in the transmit FIFO by writing to Data (DATA).
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4592 / 5251


---
# 페이지 1733

The central element of the LPUART transmitter is the transmit shift register that is 9-bit to 13-bit long depending on the settings 
of CTRL[M], CTRL[M7], BAUD[M10], and BAUD[SBNS]. Going forward in this discussion, assume that CTRL[M], CTRL[M7], 
BAUD[M10], and BAUD[SBNS] are 0, selecting the normal 8-bit Data mode, in which the shift register holds a start bit, eight data 
bits, and a stop bit. When the transmit shift register is available for a new character, the value waiting in transmit FIFO is transferred 
to the transmit shift register, synchronized with the baud rate clock, and STAT[TDRE] becomes 1 to indicate that another character 
may be written to the transmit FIFO at Data (DATA).
If no new character is waiting in the transmit FIFO after a stop bit is shifted out of the TXD pin, the transmitter sets the transmit 
complete flag and enters an idle mode, with TXD high, waiting for more characters to transmit.
Writing 0 to CTRL[TE] does not immediately disable the transmitter. The current transmit activity in progress must first be 
completed (that could include a data character, idle character, or break character), although the transmitter does not start 
transmitting another character.
77.3.4.1
Break character length
CTRL[SBK] sends break characters, originally used to gain the attention of old teletype receivers. Break characters are a full 
character time of logic 0, 9-bit to 12-bit times, including the start and stop bits. You can enable a longer break of 13-bit times 
by writing 1 to STAT[BRK13]. Normally, a program waits for STAT[TDRE] to become 1 to indicate that the last character of a 
message has moved to the transmit shifter. Next, the program writes 1 and then writes 0 to CTRL[SBK]. This action queues a break 
character to be sent as soon as the shifter is available. If CTRL[SBK] remains 1 when the queued break moves into the shifter, 
synchronized with the baud rate clock, an additional break character is queued. When LPUART is the receiving module, it receives 
a break character as 0s in all data bits and a framing error (STAT[FE] = 1) is detected.
You can also transmit a break character by writing to Data (DATA) with DATA[FRETSC] = 1 and the data bits clear. This supports 
transmitting the break character as part of the normal data stream and also allows DMA to transmit a break character.
When idle line wake-up is used, a full character time of idle (logic 1) is needed between messages to wake up any sleeping 
receivers. Normally, a program waits for STAT[TDRE] to become 1 to indicate that the last character of a message has moved 
to the transmit shifter. Next, write 0 and then write 1 to CTRL[TE]. This action queues an idle character to be sent as soon as the 
shifter is available. As long as the character in the shifter does not finish while CTRL[TE] becomes 0, the LPUART transmitter does 
not release control of the TXD pin.
You can also write to Data (DATA) to transmit an idle character, with DATA[FRETSC] and DATA[R9T9] = 1 and the values of all 
the other fields = 0. This supports transmitting the idle character as part of the normal data stream and also allows DMA to transmit 
an idle character.
As shown in the following table, STAT[BRK13], CTRL[M], CTRL[M7], BAUD[M10], and BAUD[SBNS] affect the length of the 
break character.
Table 688. Break character length
STAT[BRK13]
CTRL[M]
BAUD[M10]
CTRL[M7]
BAUD[SBNS]
Break character 
length (in bit times)
0
0
0
0
0
10
0
0
0
0
1
11
0
0
0
1
0
9
0
0
0
1
1
10
0
1
0
—
0
11
0
1
0
—
1
12
0
—
1
—
0
12
0
—
1
—
1
13
1
0
0
0
0
13
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4593 / 5251


---
# 페이지 1734

Table 688. Break character length (continued)
STAT[BRK13]
CTRL[M]
BAUD[M10]
CTRL[M7]
BAUD[SBNS]
Break character 
length (in bit times)
1
0
0
0
1
13
1
0
0
1
0
12
1
0
0
1
1
12
1
1
0
—
0
14
1
1
0
—
1
14
1
—
1
—
0
15
1
—
1
—
1
15
77.3.4.2
Hardware flow control
The transmitter supports hardware flow control by gating the transmission with the value of CTS_B. If the CTS operation is 
enabled, the character is transmitted when CTS_B is asserted. If CTS_B is deasserted in the middle of a transmission with 
characters remaining in the transmitter FIFO, the character in the transmit shift register is complete. Any characters in the FIFO 
wait for CTS_B to assert again, and TXD remains in the mark state (idle state) until CTS_B is reasserted. The CTS_B pin must 
assert for longer than one bit period to guarantee that a new transmission is started when the transmitter is idle with CTS.
If the CTS operation is disabled, the transmitter ignores the state of CTS_B.
The transmitter's CTS_B signal can be enabled even if the same LPUART receiver's RTS_B signal is disabled.
77.3.4.3
Transceiver driver enable
The transmitter can use RTS_B as an enable signal for the driver of an external transceiver. See Transceiver driver enable using 
RTS_B for details. If the RTS operation is enabled, when a character is placed into an empty transmit shift register, RTS_B asserts 
1-bit time before the start bit is transmitted. RTS_B remains asserted for the whole time that the transmit shift register has any 
characters. RTS_B deasserts 1-bit time after all characters in the transmit FIFO and shift register are completely sent, including the 
last stop bit. In other words, when RTS_B is used as a transceiver enable, RTS_B asserts 1-bit time before the transmitter starts 
transmitting and negates 1-bit time after the transmitter goes idle.
Transmitting a break character also asserts RTS_B, with the same assertion and deassertion timing as having a character in the 
transmit shift register.
The transmitter's RTS_B signal asserts only when the transmitter is enabled. However, the transmitter's RTS_B signal is 
unaffected by its CTS_B signal. RTS_B remains asserted until the transfer is complete, even if the transmitter is disabled mid-way 
through a data transfer.
You can configure HDCR[RTSEXT] to the desired length by delaying the transmitter's RTS_B negation by up to 256-bit clock (baud 
rate) after the last stop bit.
77.3.4.4
Transceiver driver enable using RTS_B
RS-485 is a multiple drop communication protocol in which the LPUART transceiver's driver is three-stated unless LPUART is 
driving. The transmitter can use the RTS_B signal to enable the driver of a transceiver. The polarity of RTS_B can be matched to 
the polarity of the transceiver's driver enable signal.
The following figure shows the receiver enable signal asserted. This connection can also connect RTS_B to both DE and RE_B. 
The transceiver's receiver is disabled when driving. A pullup can pull RXD to a nonfloating value during this time. You can refine 
this option further by operating LPUART in Single-Wire mode, freeing the RXD pin for other uses.
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4594 / 5251


---
# 페이지 1735

Driver
RS-485 transceiver
DI
DE
Y
Z
Receiver
Transmitter
LPUART
Receiver
RO
RE_B
RTS_B
TXD
RXD
A
B
Figure 492. Transceiver driver enable using RTS_B
77.3.5 Receiver functional description
This section discusses the functioning of the LPUART receiver, as shown in the receiver portion of Block diagram. The section 
also discusses:
• The data sampling technique used to reconstruct receiver data.
• Different variations of the receiver wake-up function.
You can invert the receiver input by writing 1 to STAT[RXINV] and enable the receiver by writing 1 to CTRL[RE]. Character frames 
consist of a start bit of logic 0, along with N (7, 8, 9, 10) bits (MSB or LSB first), and one or two stop bits of logic 1. For information 
about 7-bit, 9-bit, or 10-bit Data mode, see Data modes. Going forward in this discussion, assume that LPUART is configured for 
a normal 8-bit Data mode.
After receiving the stop bit into the receive shifter, and provided the receive data register is not already full (STAT[RDRF] = 0), the 
data character is transferred to the receive FIFO, resulting in STAT[RDRF] becoming 1. However, if STAT[RDRF] is already 1, 
indicating that the receive data buffer is already full, STAT[OR] becomes 1 and the new data is lost.
Because the LPUART receiver is separate from the receive FIFO, the receive shift register can receive the next word when the 
receive FIFO is full, and it is only at the end of the character that the next data is written into the receive FIFO, potentially triggering 
the overrun flag if the FIFO is full.
When a program detects that the receive data register is full (STAT[RDRF] = 1), it gets the data from the FIFO by reading Data 
(DATA). See Interrupts for details about flag clearing.
77.3.5.1
Data sampling technique
The LPUART receiver supports a configurable oversampling rate of between 4× and 32× of the baud rate clock for sampling. The 
receiver starts by considering logic level samples at the oversampling rate times the baud rate to search for a falling edge on the 
RXD serial data input pin. A falling edge is defined as a logic 0 sample after three consecutive logic 1 samples. The oversampling 
baud rate clock divides the bit time into 4 to 32 segments from 1 to OSR (where OSR is the configured oversampling ratio). When 
a falling edge is located, three more samples are taken at (OSR ÷ 2), (OSR ÷ 2) + 1, and (OSR ÷ 2) + 2 to ensure that this is a real 
start bit and not merely noise. If at least two of these three samples are 0, the receiver assumes they are synchronized to a received 
character. If another falling edge is detected before the receiver is considered synchronized, the receiver restarts sampling from 
the first segment.
The receiver then samples each bit time, including the start and stop bits, at (OSR ÷ 2), (OSR ÷ 2) + 1, and (OSR ÷ 2) + 2, to 
determine the logic level for that bit. The logic level is interpreted to be that of the majority of the samples taken during the bit time. 
If any sample in any bit time, including the start and stop bits, in a character frame fails to agree with the logic level for that bit, 
noise flag (STAT[NF]) becomes 1 when the received character is transferred to the receive FIFO.
When the LPUART receiver is configured to sample on both edges of the baud rate clock (that is, when BAUD[BOTHEDGE] = 1), 
the number of segments in each received bit is effectively doubled (from 1 to OSR× 2). The start and data bits are then sampled 
at OSR, OSR + 1, and OSR + 2. You must enable sampling on both edges of the clock for oversampling rates of 4× to 7×. This 
sampling is optional for higher oversampling rates.
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4595 / 5251


---
# 페이지 1736

The synchronization feature of LPUART synchronizes the internal oversampling counter with a detected falling edge on the 
receive signal, and to adjust the data sampling window. The falling edge detection needs three consecutive 1s prior to the "1->0" 
(one to zero) transition. After the initial falling edge detection for the start bit, the circuit continuously monitors the next falling edge, 
and resets the counter after another falling edge is detected. This synchronization to the start bit is termed as resynchronization.
When BAUD[RESYNCDIS] is 0, you perform this falling edge detection and resynchronization not only for the start bit but also for 
the rest of the character reception after the start bit.
When BAUD[RESYNCDIS] is 1, you perform the falling edge detection and resynchronization only for the start bit. The use case 
for disabling the resynchronization is protocols that require this (for example, LIN 2.1 prohibits resynchronization within a byte).
The following table and figure explain LPUART resynchronization.
Table 689. LPUART resynchronization settings
Resynchronization
BAUD[RESYNCDIS] = 0
BAUD[RESYNCDIS] = 1
For the starting bit falling 
edge
Yes
Yes
For all falling edges after the 
start bit
Yes
No
Internal sampling
clock
RX with noise and delay
BAUD[RESYNCDIS] = 0
Oversample cycle number
-
-
-
1
2
3
4
1
2
3
4
5
6
7
8
1
2
3
4
5
6
7
8
1
1
2
3
4
5
6
7
8
1
2
-
-
-
1
2
3
4
1
2
3
4
5
6
7
8
1
2
3
4
5
6
7
8
1
2
3
4
5
6
7
8
1
2
3
RX with noise and delay
BAUD[RESYNCDIS] = 1
Oversample cycle number
Sample with both edges;
sample points: 1-8
Start bit
Data bit #0
Data bit #1
Falling edge
detection
Falling edge
detection
Falling edge
detection
Falling edge
detection
Falling edge
detection
Data sampling
Data sampling
Data sampling
Data sampling
Data sampling
Data sampling
Resynchronization
Resynchronization
Resynchronization
Figure 493. LPUART resynchronization diagram
77.3.5.2
Receiver wake-up operation
Receiver wake-up and receiver address matching are hardware mechanisms that allow an LPUART receiver to ignore the 
characters in a message intended for a different receiver.
During receiver wake-up, all receivers evaluate the first character(s) of each message, and as soon as they determine the 
message is intended for a different receiver, they write 1 to CTRL[RWU].
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4596 / 5251


---
# 페이지 1737

When CTRL[RWU] and STAT[RWUID] are 1, the status fields associated with the receiver, with the exception of STAT[IDLE], are 
inhibited from becoming 1, thus eliminating the software overhead for handling the unimportant message characters. At the end 
of a message, all receivers automatically force CTRL[RWU] to become 0. This results in all receivers waking up in time to look at 
the first character(s) of the next message.
During receiver address matching, the address matching is performed in hardware and the LPUART receiver ignores all 
characters that do not meet the address match requirements.
Table 690. Receiver wake-up options
CTRL[RWU]
BAUD[MAEN1] | 
BAUD[MAEN2]
BAUD[MATCFG]
CTRL[WAKE]:
STAT[RWUID]
Receiver wake-up
0
0
X
X
Normal operation
1
0
00
00
Receiver wake-up on 
idle line; STAT[IDLE] = 
0
1
0
00
01
Receiver wake-up on 
idle line; STAT[IDLE] = 
1
1
0
00
10
Receiver wake-up on 
address mark
1
1
11
10
Receiver wake-up on 
data match
0
1
00
X0
Address mark address 
match; STAT[IDLE] 
= 0 for discarded 
characters
0
1
00
X1
Address mark address 
match; STAT[IDLE] 
= 1 for discarded 
characters
0
1
01
X0
Idle line address match
0
1
10
X0
Match on and match 
off; STAT[IDLE] = 0 for 
discarded characters
0
1
10
X1
Match on and match 
off; STAT[IDLE] = 1 for 
discarded characters
77.3.5.2.1
Idle line wake-up
When CTRL[WAKE] is 0, you can configure the receiver for an idle line wake-up. In this mode, CTRL[RWU] becomes 0 
automatically when the receiver detects a full character time of the idle-line level.
CTRL[M], CTRL[M7], and BAUD[M10] select 7-bit to 10-bit Data mode and BAUD[SBNS] selects a 1-bit or 2-bit stop bit number 
that determines how many bit times of idle are needed to constitute a full character time, 9 to 13 bit times because of the start and 
stop bits.
When CTRL[RWU] is 1 and STAT[RWUID] is 0, the idle condition that wakes up the receiver does not lead to STAT[IDLE] 
becoming 1. The receiver wakes up and waits for the first data character of the next message that leads to STAT[RDRF] becoming 
1 and generates an interrupt if enabled. When STAT[RWUID] is 1, any idle condition leads to STAT[IDLE] becoming 1 and 
generates an interrupt if enabled, regardless of whether CTRL[RWU] is 0 or 1.
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4597 / 5251


---
# 페이지 1738

These are the ways to detect an idle line:
• When CTRL[ILT] is 0, the idle bit counter starts after the start bit so that the stop bit and any logic 1s at the end of a character 
count to calculate the full character time of idle.
• When CTRL[ILT] is 1, the idle bit counter does not start until after the stop bit time so that the data in the last character of the 
previous message does not impact the idle detection.
77.3.5.2.2
Address mark wake-up
When CTRL[WAKE] is 1, you can configure the receiver for an address mark wake-up. In this mode, CTRL[RWU] becomes 0 
automatically when the receiver detects a logic 1 in the most significant bit of the received character. When parity is enabled, the 
second most significant bit is used for address mark wake-up.
Address mark wake-up allows messages to contain idle characters, but requires one bit to be reserved for use in address frames. 
The logic 1 in the most significant bit (or second most significant bit when parity is enabled) of an address frame writes 0 to 
CTRL[RWU] and writes 1 to STAT[RDRF]. In this case, the character with the address mark bit is received even if the receiver is 
sleeping during most of this character time.
77.3.5.2.3
Data match wake-up
When CTRL[RWU] and CTRL[WAKE] are 1, and BAUD[MATCFG] equals 11, the receiver is configured for a data match wake-up. 
In this mode, CTRL[RWU] becomes 0 automatically when the receiver detects a character that matches MATCH[MA1] when 
BAUD[MAEN1] is 1, or that matches MATCH[MA2] when BAUD[MAEN2] is 1.
77.3.5.2.4
Address match operation
You can enable the address match operation when either BAUD[MAEN1] or BAUD[MAEN2] is 1 and BAUD[MATCFG] is 0. In this 
function, a character that the RXD pin receives with a logic 1 in the most significant bit (or the second most significant bit when 
parity is enabled) is considered an address and is compared to the associated MATCH[MA1] or MATCH[MA2]. The character is 
only transferred to the receive buffer, and STAT[RDRF] becomes 1 if the comparison matches. All subsequent characters received 
with a logic 0 in the most significant bit (or the second most significant bit when parity is enabled) are considered to be data 
associated with the address and are transferred to the receive FIFO. If no marked address match occurs, no transfer is made to 
the receive FIFO, and all the characters that follow, with logic 0 in the most significant bit (or second most significant bit when 
parity is enabled), are also discarded. If both BAUD[MAEN1] and BAUD[MAEN2] are 0, the receiver operates normally, and all 
the received data is transferred to the receive FIFO.
The address match operation functions in the same way for both MATCH[MA1] and MATCH[MA2]:
• If either BAUD[MAEN1] or BAUD[MAEN2] is 1, a marked address is compared only to the associated Match Address 
(MATCH) and data is transferred to the receive FIFO only on a match.
• If both BAUD[MAEN1] and BAUD[MAEN2] are 1, a marked address is compared to both MATCH[MA1] and MATCH[MA2] 
and data is transferred only on a match with either of these fields.
77.3.5.2.5
Idle match operation
You can enable the idle match operation when either BAUD[MAEN1] or BAUD[MAEN2] is 1 and BAUD[MATCFG] is 1. In this 
function, the first character that the RXD pin receives after an idle line condition is considered an address and is compared to the 
associated MATCH[MA1] or MATCH[MA2]. The character is transferred only to the receive buffer, and STAT[RDRF] becomes 1, 
if the comparison matches. All subsequent characters are considered to be data associated with the address and are transferred 
to the receive FIFO until the next idle line condition is detected. If no address match occurs, no transfer is made to the receive 
FIFO, and all the frames that follow, until the next idle condition, are also discarded. If both BAUD[MAEN1] and BAUD[MAEN2] 
are 0, the receiver operates normally, and all the received data is transferred to the receive FIFO.
An idle match operation functions in the same way for both MATCH[MA1] and MATCH[MA2]:
• If either BAUD[MAEN1] or BAUD[MAEN2] is 1, the first character after an idle line is compared only to the associated Data 
(DATA) and data is transferred to the receive FIFO only on a match.
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4598 / 5251


---
# 페이지 1739

• If both BAUD[MAEN1] and BAUD[MAEN2] are 1, the first character after an idle line is compared to both MATCH[MA1] and 
MATCH[MA2] and data is transferred only on a match with either of these fields.
77.3.5.2.6
Match on, match off operation
The match on, match off operation is enabled when both BAUD[MAEN1] and BAUD[MAEN2] are 1 and BAUD[MATCFG] = 
10. In this function, a character that the RXD pin receives matches MATCH[MA1] and is transferred to the receive buffer, and 
STAT[RDRF] becomes 1. All subsequent characters are considered to be data and are also transferred to the receive FIFO, 
until a character that matches MATCH[MA2] is received. The character that matches MATCH[MA2], along with all subsequent 
characters, is discarded; and this continues until another character that matches MATCH[MA1] is received. If both BAUD[MAEN1] 
and BAUD[MAEN2] are 0, the receiver operates normally, and all the received data is transferred to the receive FIFO.
 
The match on, match off operation requires both BAUD[MAEN1] and BAUD[MAEN2] to be 1.
  NOTE  
77.3.5.3
Hardware flow control
To support hardware flow control, you can program the receiver to automatically assert and deassert RTS_B:
• RTS_B remains asserted until the transfer is complete, even if the transmitter is disabled midway through a data transfer. 
See Transceiver driver enable using RTS_B for more information.
• If the receiver RTS functionality is enabled, the receiver automatically deasserts RTS_B if STAT[RDRF] is 1 or a start bit is 
detected that causes STAT[RDRF] to become 1.
• The receiver asserts RTS_B when STAT[RDRF] is 0 and has not detected a start bit that causes STAT[RDRF] to become 
1. There is no impact if STAT[RDRF] is 1 already.
• Even if RTS_B is deasserted, the receiver continues to receive characters until the receive FIFO is overrun.
• If the receiver RTS functionality is disabled, the receiver's RTS_B remains deasserted.
• When RTS is driven by receiver, it will be negated when the receiver is disabled irrespective of the FIFO level.
77.3.6 Additional LPUART functions
77.3.6.1
Data modes
You can configure the LPUART transmitter and receiver to operate in 7-bit Data mode by writing 1 to CTRL[M7], 9-bit Data mode 
by writing 1 to CTRL[M], or 10-bit Data mode by writing 1 to BAUD[M10]. In 9-bit Data mode, there exists a ninth data bit and in 
10-bit mode, there exists a tenth data bit.
When performing 8-bit writes to the transmit FIFO, the ninth and tenth bits are pushed into the FIFO from CTRL[T8] and CTRL[T9]. 
For coherent 8-bit writes, you must write to CTRL[T8] and CTRL[T9] before writing to Data (DATA)[7:0]. However, if the values 
in CTRL[T8] or CTRL[T9] do not need to change, it is not necessary to update CTRL[T8] and CTRL[T9] before every 8-bit write 
to Data (DATA).
When performing 16-bit or 32-bit writes to the transmit FIFO, all 10 bits are pushed into the transmit FIFO from the write data.
When performing 8-bit reads of the receive FIFO, the ninth and tenth bits are held in CTRL[R8] and CTRL[R9] but you must read 
them before reading Data (DATA). A 16-bit or 32-bit read of the receive FIFO returns all 10 bits in Data (DATA).
The 9-bit Data mode is typically used with parity to allow eight bits of data plus the parity in the ninth bit, or it is used with the 
address mark wake-up so that the ninth data bit can serve as the wake-up bit. The 10-bit Data mode is typically used with parity 
and address mark wake-up so that the ninth data bit can serve as the wake-up bit and the tenth bit can serve as the parity bit. In 
custom protocols, the ninth and/or tenth bits can also serve as software-controlled markers.
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4599 / 5251


---
# 페이지 1740

77.3.6.2
Idle length
An idle character is one where the start bit, all data bits, and stop bits are in the mark position (idle state, generally logic 1). You 
can configure CTRL[ILT] to start detecting an idle character from the previous start bit (any data bits and stop bits count for idle 
character detection) or from the previous stop bit.
You can also use CTRL[IDLECFG] to configure the number of idle characters that must be received before an idle line condition 
is detected. This field configures the number of idle characters that must be received before STAT[IDLE] becomes 1, STAT[RAF] 
becomes 0, and DATA[IDLINE] becomes 1 with the next received character.
CTRL[IDLECFG] also affects the idle line wake-up and idle match operations. When either the address match or match on/off 
operation is enabled, writing 1 to STAT[RWUID] causes any discarded characters to be treated as idle characters.
After the extended idle time is enabled for the receiver, you can configure an idle line condition by using REIR[IDTIME], which 
specifies the number of bits (baud rate) since the last stop bit that is required for an idle condition to be detected. This replaces 
the configuration of CTRL[ILT] and CTRL[IDLECFG].
The transmitter can also enable the extended idle time. In this case, any idle character queued through the transmit FIFO 
forces the transmitter to be idled for the configured number of bit clocks before the idle character is read from the FIFO and the 
transmitter continues.
After you enable the transmitter extended idle time, the transmitter does not automatically queue an idle character whenever it 
is enabled.
77.3.6.3
Loop mode
Enable Loop mode by setting CTRL[LOOPS] = 1 and CTRL[RSRC] = 0. You, sometimes, use Loop mode to check software, 
independent of connections in the external system, to help isolate system problems. In this mode, the transmitter output is 
internally connected to the receiver input and LPUART does not use the RXD pin.
Loop mode also internally connects the RTS_B output to the CTS_B input and the DTR_B output to the DSR_B input.
77.3.6.4
Single-Wire mode
Enable Single-Wire mode by setting CTRL[LOOPS] = 1 and CTRL[RSRC] = 1. Single-Wire mode implements a half-duplex serial 
connection. The receiver is internally connected to the transmitter output and TXD pin (the RXD pin is not used).
In Single-Wire mode, CTRL[TXDIR] controls the direction of serial data on the TXD pin. When CTRL[TXDIR] becomes 0, the TXD 
pin is an input to the receiver and the transmitter is temporarily disconnected from the TXD pin so that an external device can send 
serial data to the receiver. When CTRL[TXDIR] = 1, the TXD pin is an output that the transmitter drives. The internal loop back 
connection is disabled, and as a result, the receiver is unable to receive characters that the transmitter sends out.
Half Duplex Control (HDCR) replaces the implementation of CTRL[LOOPS] and CTRL[RSRC], and you can use this register to 
configure various options for both Single-Wire and Half-Duplex operations, using independent RXD and TXD pins:
• HDCR[TXSTALL] replaces the CTRL[TXDIR] functionality and prevents the transmitter from becoming busy or asserting the 
RTS_B transmitter if STAT[RAF] is 1.
• You can select the TXD pin, as the source for the receiver, to configure HDCR[RXSEL] for a single-wire operation. If 
HDCR[RXSEL] is 1, you must configure the TXD pin for an open-drain operation.
• HDCR[RXMSK] masks the receiver input when the RTS_B transmitter is asserted (this applies even if you have not configured 
RTS_B as an output).
• HDCR[RXWRMSK] blocks storage of the receive data in the receive FIFO when the RTS_B transmitter is asserted. This 
setting does not affect the receiver idle functionality.
• HDCR[RTSEXT] delays the negation of the RTS_B transmitter by the configured number of bit clocks (baud rate).
77.3.6.5
Timeout counter
LPUART implements four general-purpose timeout counters; counters 0 and 1 are used to monitor the receiver and counters 2 and 
3 are used to monitor the transmitter. When enabled, you can configure each counter to monitor one of the following conditions:
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4600 / 5251


---
# 페이지 1741

• Idle time in number of bits, starting to increment when first enabled and an idle condition is detected. The counter restarts 
whenever a character is received or transmitted.
• Idle time in number of bits, starting to increment after the next character is received or transmitted. The counter restarts 
whenever a character is received or transmitted.
• Idle time is more than the timeout interval, in number of bits, but less than the extended idle timeout. The counter restarts 
whenever a character is received or transmitted. You can use this to detect a gap between characters that is greater than a 
threshold (timeout) but less than the configured extended idle time. This configuration requires the extended idle feature for 
the transmitter or receiver to be enabled for a proper operation.
• Number of characters received or transmitted is equal to the configured timeout. The counter asserts at the start of the 
character that equals the timeout value.
The timeout counters restart counting whenever the counter is disabled and then enabled. These timeout counters are disabled 
when the corresponding STAT[TSF] field is 1. If the timeout enable is still set after STAT[TSF] becomes 0, the timeout counter 
restarts as if the counter had been disabled and then enabled. You can measure the idle time in bit times from the end of the last 
stop bit and until a start bit is validated.
77.3.7 Peripheral triggers
The connection of the LPUART peripheral triggers with other peripherals is chip-specific.
77.3.7.1
Output triggers
LPUART generates the following output triggers that can be connected to other peripherals on the chip:
• The transmit word trigger asserts at the end of each transmitted word and negates after 1-bit period.
• The transmit data trigger is identical to the TXD pin output, but without support for input trigger modulation.
• The receive word trigger asserts at the end of each received word that is written to the receive FIFO, for one oversampling 
clock period.
• The receive idle trigger asserts when STAT[IDLE] becomes 1, and negates when the next valid start bit is detected.
77.3.7.2
Input trigger
LPUART supports a peripheral input trigger that you can configure in one of the following ways:
• By enabling the CTS function: You can connect the input trigger instead of the CTS_B pin input. The input trigger must 
assert for longer than 1-bit clock period when the transmitter is idle, with data to send, to guarantee a new transmission.
• By making the input trigger modulate the transmit data output (trigger is logically ANDed with the TXD output): The input 
trigger is expected to be a free-running clock (carrier signal) that generates from a timer or PWM source with a frequency 
that is greater than the bit-clock frequency. The carrier signal must not toggle faster than the maximum supported bit time.
• By connecting the input trigger instead of the RXD pin input: The input trigger is expected to be generated from a receive 
data source, such as an analog comparator or external pin.
77.3.8 Infrared (IR) interface
LPUART provides the capability of transmitting narrow pulses to an IR LED and receiving narrow pulses, transforming them to 
serial bits, which are then sent to LPUART. The IrDA physical layer specification defines a half-duplex IR communication link for 
exchanging data. The full standard includes data rates up to 16 Mbit/s. The LPUART IrDA support is limited to SIR mode that 
supports data rates only between 2.4 kbit/s and 115.2 kbit/s.
LPUART has an infrared transmit encoder and a receive decoder. The infrared decoder converts the received character from the 
IrDA format to the NRZ format, which the receiver uses. It also has an OSR oversampling baud rate clock counter that filters noise 
and indicates when a 1 is received. LPUART transmits serial bits of data, which the infrared submodule encodes, to transmit a 
narrow pulse for every zero bit. No pulse is transmitted for every single bit. When receiving data, an IR photo diode (external to 
LPUART) detects the IR pulses. The IR receive decoder transforms them to CMOS levels. The infrared receive decoder then 
stretches the narrow pulses to get back to a serial bit stream that LPUART receives. You can invert the polarity of transmitted 
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4601 / 5251


---
# 페이지 1742

pulses and expected receive pulses so that a direct connection can be made to external IrDA transceiver modules that use 
active-high pulses.
The IR submodule receives its clock sources from LPUART. The submodule selects one of these clocks to generate either 1 ÷ 
OSR, 2 ÷ OSR, 3 ÷ OSR, or 4 ÷ OSR narrow pulses during transmission.
77.3.8.1
Infrared transmit encoder
The infrared transmit encoder converts serial bits of data from the transmit shift register to the TXD signal. A narrow pulse is 
transmitted for a 0 bit and no pulse is transmitted for a 1 bit. The narrow pulse is sent at the start of the bit with a duration of 1 ÷ 
OSR, 2 ÷ OSR, 3 ÷ OSR, or 4 ÷ OSR of a bit time. A narrow low pulse is transmitted for a 0 bit when CTRL[TXINV] is 0, while a 
narrow high pulse is transmitted for a 0 bit when CTRL[TXINV] is 1.
77.3.8.2
Infrared receive decoder
The infrared receive block converts data from the RXD signal to the receive shift register. A narrow pulse is expected for each 0 
received and no pulse is expected for each 1 received. A narrow low pulse is expected for a 0 bit when STAT[RXINV] is 0, while 
a narrow high pulse is expected for a 0 bit when STAT[RXINV] is 1. This receive decoder meets the edge jitter requirement as 
defined by the IrDA serial infrared physical layer specification.
77.3.8.3
Start-bit detection
When STAT[RXINV] is 0, the first falling edge of the received character corresponds to the start bit. The infrared decoder resets its 
counter. At this time, the receiver also begins its start bit detection process. After the start bit is detected, the receiver synchronizes 
its bit times to this start bit time. For the rest of the character reception, the infrared decoder's counter and the receiver's bit time 
counter count independently of each other.
77.3.8.4
Noise filtering
The decoder ignores any rising edges detected during the first half of the infrared decoder counter, and can leave any pulses less 
than one oversampling baud clock as undetected. This is regardless of whether the pulse is seen in the first or second half of 
the count.
77.3.8.5
Low-bit detection
During the second half of the decoder count, a rising edge is decoded as 0, which is sent to the receiver. The decoder counter is 
also reset.
77.3.8.6
High-bit detection
At OSR oversampling baud rate clocks after the previous rising edge, if a rising edge is not seen, the decoder sends a 1 to 
the receiver.
If the next bit is 0, which arrives late, a low bit is detected according to Low-bit detection. The value sent to the receiver is changed 
from 1 to 0. Then, if a noise pulse occurs outside the receiver's bit time sampling period, the delay of a 0 is not recorded as noise.
77.3.9 MODBUS protocol
77.3.9.1
MODBUS frame structure
MODBUS is an application layer messaging protocol, positioned at level 7 of the OSI model. It provides client and server 
communication between devices connected on different types of buses or networks.
The MODBUS protocol defines a simple protocol data unit (PDU) independent of the underlying communication layers. The 
mapping of the MODBUS protocol on specific buses or network can introduce some additional fields on the application data 
unit (ADU).
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4602 / 5251


---
# 페이지 1743

Additional address
Functional code
ADU
PDU
Error check
Data
Figure 494. MODBUS frame structure
The function code field informs the server about which action to perform, as requested by the client (only the client can initiate the 
communication), where the data field contains additional information that the server uses to take the action defined by the function 
code. MODBUS PDU for serial line communication = 256 - server address (1 byte) - CRC (2 bytes) = 253 bytes.
You can set up a MODBUS controller to communicate on standard MODBUS networks using either of the two transmission 
modes: ASCII or RTU. RTU mode allows better character density and throughput for the same baud rate as the ASCII format 
allows 7 bits to represent a character where RTU keeps 8 bits for data representation in each packet.
77.3.9.2
MODBUS frame for LPUART
Though the protocol resides in the application layer, it can also be checked at the physical layer using LPUART by considering 
the frame structure shown in the following figure, following RTU mode of data transmission.
Start
Address
Function
Data
CRC
End
3.5 Char time
16 Bit
N * 8Bit
8 Bit
8 Bit
3.5 Char time
Figure 495. MODBUS frame for LPUART
An entire message frame of MODBUS must contain start character, address, function code, data, and end character. LPUART 
does not support CRC calculation for TX and RX, instead, each LPUART packet containing frame information is transmitted with 
its individual parity, and the same is checked in RX. Following the last transmitted character, a similar interval of at least 3.5 
character times marks the end of the message and a new message can begin after this interval. The entire message frame must be 
transmitted as a continuous stream. If a silent interval of more than 1.5 character times occurs before the completion of the frame, 
the receiving device flushes the incomplete message, and assumes that the next byte is the address field of a new message. The 
correctness of timeout logic ensures the correctness of the MODBUS frame using LPUART.
Registers such as REIR, TEIR, TOCR, TOSR, TIMEOUT[0 - 3], TCBR, and TDBR are useful for realizing MODBUS using 
LPUART. The TX IDLE time is configured by using TEIR[IDTIME].
For higher baud rates, MODBUS recommends adopting fixed t1.5 and t3.5 times of 750us ms and 1.75 ms. The receiver idle line 
wake-up can be used by a MODBUS device to only wake-up on a matching address or broadcast address received after a valid idle 
time. The receiver end-of-packet DMA transfer can be used to offload the reception of a MODBUS packet onto the DMA controller.
77.3.9.3
MODBUS TX and RX programming sequence
The following programming sequences can be useful for sending and receiving MODBUS frames using LPUART.
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4603 / 5251


---
# 페이지 1744

Configure transmitter: set baud rate, 
9-bit data, even parity, 1 stop bit, 
TX_direction, single wire mode, 
MSB first 
Configure TX IDLE time: 
at least 3.5 - character time, 
for example, 
TIER = 0x0000_0027 or more. 
Enable: TX FIFO, enable transmitter
Send an IDLE character: 
TSC = 1, T9 = 1, 
T8:T0 = Clear (32 bit Write)
Use DMA with TCBR/ TDBR support 
to Queue rest of the packet 
(includes address, function code, data, 
and CRC)
Send an IDLE character: TSC = 1, 
T9 = 1, T8:T0 = Clear (32 bit Write)
Figure 496. MODBUS TX programming
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4604 / 5251


---
# 페이지 1745

Configure receiver: Set baud-rate,
9-bit data, even parity, 1 stop bit, 
RX_direction,
single wire mode, MSB first, and so on
Configure timeout: 
TIMEOUT[CFG]=2'B11;
TIMEOUT0[TIMEOUT] = 1.5-character 
time 
TIMEOUT1[TIMEOUT] = 3.5-character 
time 
Configure: Interrupt on timeout0
Turn on RX FIFO and RX,
Frame reception starts
MODBUS frame received, 
set RX Idle
Timeout1
overflew?
Receive frame (includes address, 
function code, data, and CRC
YES
NO
MODBUS Frame Error
YES
Timeout0 Interrupt 
received?
Figure 497. MODBUS RX programming
77.3.10 Modes of operation
77.3.10.1
Low-Power modes
 
See the chip-specific information for specific low-power modes available on your chip.
  NOTE  
77.3.10.2
Debug mode
LPUART remains functional in Debug mode.
77.3.11 Clocking
Table 691. Types of clocks
Clock
Description
Functional
Is asynchronous to the bus clock and can remain enabled in Low-Power modes to support transmit 
and/or receive functions, including low-power wake-up.
Bus
Is only used for bus accesses to the control and configuration registers. The bus clock frequency 
must be sufficient to support the data bandwidth requirements of the LPUART transmit and receive 
registers, including the FIFOs.
77.3.12 Reset
Table 692. Types of resets
Reset
Description
Chip
Enables the logic and registers for the LPUART transmitter and receiver to reset to their default 
states.
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4605 / 5251


---
# 페이지 1746

Table 692. Types of resets (continued)
Reset
Description
Software
Resets the LPUART logic and registers to their default states, except for Global (GLOBAL).
GLOBAL[RST] controls the LPUART software reset.
FIFO
Implements write-only control fields that reset the transmit FIFO (FIFO[TXFLUSH]) and receive 
FIFO (FIFO[RXFLUSH]). After a FIFO is reset, that FIFO becomes empty.
77.3.13 Interrupts
The LPUART transmitter has two status fields that can optionally generate hardware interrupt requests. If STAT[TDRE] is 1, it 
indicates that there is room in the transmit FIFO to write another transmit character to Data (DATA). If CTRL[TIE] is 1, a hardware 
interrupt is requested when STAT[TDRE] is 1.
STAT[TC] indicates that the transmitter is finished transmitting all data, preamble, and break characters and is idle with TXD at the 
inactive level. This field is often used in systems with modems to determine when it is safe to turn off the modem. If CTRL[TCIE] is 
1, a hardware interrupt is requested when STAT[TC] is 1. Instead of hardware interrupts, software polling may be used to monitor 
STAT[TDRE] and STAT[TC] if the corresponding CTRL[TIE] or CTRL[TCIE] field is 0.
When a program detects that STAT[RDRF] is 1, it gets the data from this field by reading Data (DATA). The field becomes 0 by 
reading Data (DATA).
STAT[IDLE] includes logic that prevents it from becoming 1 repeatedly when the RXD line remains idle for an extended period of 
time. STAT[IDLE] becomes 0 when you write 1 to it, and cannot become 1 again until the receiver has received at least one new 
character and has 1 as the value of STAT[RDRF].
If the associated error is detected in the received character that caused STAT[RDRF] to become 1, STAT[NF], STAT[FE], and 
STAT[PF] become 1 at the same time STAT[RDRF] becomes 1. These flags do not become 1 in overrun cases.
If STAT[RDRF] is already 1 when a new character is ready to be transferred from the receive shifter to the receive FIFO, STAT[OR] 
becomes 1, instead of the data along with any associated STAT[NF], STAT[FE], or STAT[PF] condition getting lost.
If the received character matches the contents of MATCH[MA1] and/or MATCH[MA2], then STAT[MA1F] and/or STAT[MA2F] 
become 1 at the same time that STAT[RDRF] becomes 1.
At any time, an active edge on the RXD serial data input pin causes STAT[RXEDGIF] to become 1. STAT[RXEDGIF] becomes 
0 when you write 1 to it. This function depends on the receiver being enabled (the value of CTRL[RE] being 1).
MODEM Status (MSR) can generate an interrupt from a configured status field, which STAT[MSF] indicates.
Timeout Status (TOSR) can generate an interrupt from a configured status field, which STAT[TSF] indicates.
77.3.14 DMA
77.3.14.1
DMA burst support
To support efficient DMA transfers to the transmit FIFO, two alias regions are implemented to support incrementing 8-bit, 16-bit, 
or 32-bit write accesses to the transmit FIFO:
• Transmit Command Burst (TCBR0 - TCBR127) is a 512-byte region that supports pushing 16-bit data into the transmit 
FIFO.
• Transmit Data Burst (TDBR0 - TDBR255) is a 1024-byte region that supports pushing zero extended 8-bit data into the 
transmit FIFO.
The aforementioned regions are contiguous, so a DMA transfer can start in Transmit Command Burst (TCBR0 - TCBR127) to 
initialize the transfer including address mark, idle word, or break character, and then complete the transfer in Transmit Data Burst 
(TDBR0 - TDBR255) with the data to transmit, without changing the transfer size.
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4606 / 5251


---
# 페이지 1747

The transmit FIFO block writes overflow the FIFO, but that does not signal an error. Do not perform 32-bit writes to Transmit Data 
Burst (TDBR0 - TDBR255) unless there are four empty slots in the transmit FIFO, and do not perform 16-bit writes to this register 
unless there are two empty slots in the transmit FIFO.
77.4 External signals
Table 693. External signals
Signal
Description
I/O
TXD
Transmit data: This pin is normally 
an output, but is an input (tristated) 
in Single-Wire mode whenever the 
transmitter is disabled or the transmit 
direction is configured for receive data.
I/O
RXD
Receive data
I
CTS_B
Clear-to-send
I
RTS_B
Request-to-send
O
DTR_B
Data terminal ready
O
DSR_B
Data set ready
I
DCD_B
Data carrier detect
I
RIN_B
Ring indicator
I
77.5 Initialization
This module does not require initialization.
77.6 LPUART register descriptions
LPUART includes registers to control baud rate, select options, report status, and store transmit and receive data. Access to an 
address outside the valid memory map generates a bus error.
 
Writing to a read-only (RO) register or reading a write-only (WO) register can cause bus errors. LPUART does not 
verify whether programmed values in the registers are correct; you must write valid values to them.
  NOTE  
77.6.1 LPUART memory map
LPUART_0 base address: 4032_8000h
LPUART_1 base address: 4032_C000h
LPUART_2 base address: 4033_0000h
LPUART_3 base address: 4033_4000h
LPUART_4 base address: 4033_8000h
LPUART_5 base address: 4033_C000h
LPUART_6 base address: 4034_0000h
LPUART_7 base address: 4034_4000h
LPUART_8 base address: 4048_C000h
LPUART_9 base address: 4049_0000h
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4607 / 5251


---
# 페이지 1748

LPUART_10 base address: 4049_4000h
LPUART_11 base address: 4049_8000h
LPUART_12 base address: 4049_C000h
LPUART_13 base address: 404A_0000h
LPUART_14 base address: 404A_4000h
LPUART_15 base address: 404A_8000h
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
See section
4h
Parameter (PARAM)
32
R
See section
8h
Global (GLOBAL)
32
RW
0000_0000h
Ch
Pin Configuration (PINCFG)
32
RW
0000_0000h
10h
Baud Rate (BAUD)
32
RW
0F00_0004h
14h
Status (STAT)
32
RW
00C0_0000h
18h
Control (CTRL)
32
RW
0000_0000h
1Ch
Data (DATA)
32
RW
0000_1000h
20h
Match Address (MATCH)
32
RW
0000_0000h
24h
MODEM IrDA (MODIR)
32
RW
0000_0000h
28h
FIFO (FIFO)
32
RW
See section
2Ch
Watermark (WATER)
32
RW
0000_0000h
30h
Data Read-Only (DATARO)
32
R
0000_1000h
40h
MODEM Control (MCR)
32
RW
0000_0000h
44h
MODEM Status (MSR)
32
RW
0000_0000h
48h
Receiver Extended Idle (REIR)
32
RW
0000_0000h
4Ch
Transmitter Extended Idle (TEIR)
32
RW
0000_0000h
50h
Half Duplex Control (HDCR)
32
RW
0000_0000h
58h
Timeout Control (TOCR)
32
RW
0000_0000h
5Ch
Timeout Status (TOSR)
32
RW
0000_000Fh
60h - 6Ch
Timeout N (TIMEOUT0 - TIMEOUT3)
32
RW
0000_0000h
200h - 3FCh
Transmit Command Burst (TCBR0 - TCBR127)
32
W
0000_0000h
400h - 7FCh
Transmit Data Burst (TDBR0 - TDBR255)
32
W
0000_0000h
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4608 / 5251


---
# 페이지 1749

77.6.2 Version ID (VERID)
Offset
Register
Offset
VERID
0h
Function
Indicates the version integrated for this instance on the chip and also specifies the inclusion and exclusion of several optional 
features.
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
See Register reset values.
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
See Register reset values.
Register reset values
Register
Reset value
VERID
LPUART_0,LPUART_1: 0404_0007h
LPUART_2–LPUART_15: 0404_0003h
Fields
Field
Function
31-24
MAJOR
Major Version Number
Indicates the major version number for the module specification.
23-16
MINOR
Minor Version Number
Indicates the minor version number for the module specification.
15-0
FEATURE
Feature Identification Number
Indicates the feature set number.
0000_0000_0000_0001b - Standard feature set
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4609 / 5251


---
# 페이지 1750

Table continued from the previous page...
Field
Function
0000_0000_0000_0011b - Standard feature set with MODEM and IrDA support
0000_0000_0000_0111b - Enhanced feature set with full MODEM, IrDA, and enhanced idle 
detection
77.6.3 Parameter (PARAM)
Offset
Register
Offset
PARAM
4h
Function
Indicates the parameter configuration for this instance on the chip.
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
See Register reset values.
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
RXFIFO 
TXFIFO 
W
Reset
See Register reset values.
Register reset values
Register
Reset value
PARAM
LPUART_0,LPUART_1: 0000_0404h
LPUART_2–LPUART_15: 0000_0202h
Fields
Field
Function
31-16
—
Reserved
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4610 / 5251


---
# 페이지 1751

Table continued from the previous page...
Field
Function
15-8
RXFIFO
Receive FIFO Size
Indicates the number of characters in the receive FIFO, which is 2^RXFIFO.
7-0
TXFIFO
Transmit FIFO Size
Indicates the number of characters in the transmit FIFO, which is 2^TXFIFO.
77.6.4 Global (GLOBAL)
Offset
Register
Offset
GLOBAL
8h
Function
Performs global functions.
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
RST 
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
31-2
—
Reserved
1
RST
Software Reset
Specifies whether the module is reset.
This field resets all internal logic and registers, except Global (GLOBAL). The reset takes effect immediately 
and remains asserted until you negate it. There is no minimum delay required before clearing the 
software reset.
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4611 / 5251


---
# 페이지 1752

Table continued from the previous page...
Field
Function
0b - Not reset
1b - Reset
0
—
Reserved
77.6.5 Pin Configuration (PINCFG)
Offset
Register
Offset
PINCFG
Ch
Function
Enables the selection of input pins.
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
TRGSEL 
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
1-0
TRGSEL
Trigger Select
Configures the input trigger usage.
You must change the value of this field only when both the transmitter and receiver are disabled.
00b - Input trigger disabled
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4612 / 5251


---
# 페이지 1753

Table continued from the previous page...
Field
Function
01b - Input trigger used instead of the RXD pin input
10b - Input trigger used instead of the CTS_B pin input
11b - Input trigger used to modulate the TXD pin output, which (after TXINV configuration) is 
internally ANDed with the input trigger
77.6.6 Baud Rate (BAUD)
Offset
Register
Offset
BAUD
10h
Function
Configures the baud rate.
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
MAEN
1 
MAEN
2 
M10 
OSR 
TDMA
E 
0
RDMA
E 
Reserv
ed 
MATCFG 
BOTH
EDGE 
RESY
NCD...
W
0
Reset
0
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
LBKDI
E 
RXED
GIE 
SBNS 
SBR 
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
MAEN1
Match Address Mode Enable 1
Enables automatic address matching or data matching mode for MATCH[MA1]. If this field is 0, normal 
operation takes place.
0b - Disable
1b - Enable
30
MAEN2
Match Address Mode Enable 2
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4613 / 5251


---
# 페이지 1754

Table continued from the previous page...
Field
Function
Enables automatic address matching or data matching mode for MATCH[MA2]. If this field is 0, normal 
operation takes place.
0b - Disable
1b - Enable
29
M10
10-Bit Mode Select
Causes the tenth bit to be a part of the serial transmission.
You must change the value of this field only when both the transmitter and receiver are disabled.
0b - Receiver and transmitter use 7-bit to 9-bit data characters
1b - Receiver and transmitter use 10-bit data characters
28-24
OSR
Oversampling Ratio
Configures the OSR of the receiver.
You must change the value of this field only when both the transmitter and receiver are disabled.
 
BAUD[OSR] results in an OSR of BAUD[OSR] + 1, for example, BAUD[OSR] = 0_0101b 
results in a final division by 6.
  NOTE  
0_0000b - Results in an OSR of 16
0_0001b - Reserved
0_0010b - Reserved
0_0011b - Results in an OSR of 4 (requires BAUD[BOTHEDGE] to be 1)
0_0100b - Results in an OSR of 5 (requires BAUD[BOTHEDGE] to be 1)
0_0101b - Results in an OSR of 6 (requires BAUD[BOTHEDGE] to be 1)
0_0110b - Results in an OSR of 7 (requires BAUD[BOTHEDGE] to be 1)
0_0111b - Results in an OSR of 8
0_1000b - Results in an OSR of 9
0_1001b - Results in an OSR of 10
0_1010b - Results in an OSR of 11
0_1011b - Results in an OSR of 12
0_1100b - Results in an OSR of 13
0_1101b - Results in an OSR of 14
0_1110b - Results in an OSR of 15
0_1111b - Results in an OSR of 16
1_0000b - Results in an OSR of 17
1_0001b - Results in an OSR of 18
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4614 / 5251


---
# 페이지 1755

Table continued from the previous page...
Field
Function
1_0010b - Results in an OSR of 19
1_0011b - Results in an OSR of 20
1_0100b - Results in an OSR of 21
1_0101b - Results in an OSR of 22
1_0110b - Results in an OSR of 23
1_0111b - Results in an OSR of 24
1_1000b - Results in an OSR of 25
1_1001b - Results in an OSR of 26
1_1010b - Results in an OSR of 27
1_1011b - Results in an OSR of 28
1_1100b - Results in an OSR of 29
1_1101b - Results in an OSR of 30
1_1110b - Results in an OSR of 31
1_1111b - Results in an OSR of 32
23
TDMAE
Transmitter DMA Enable
Enables STAT[TDRE] to generate a DMA request.
0b - Disable
1b - Enable
22
—
Reserved
21
RDMAE
Receiver Full DMA Enable
Enables STAT[RDRF] to generate a DMA request.
0b - Disable
1b - Enable
20
—
Reserved
19-18
MATCFG
Match Configuration
Configures the match addressing mode used.
You must change the value of this field only when both the transmitter and receiver are disabled.
00b - Address match wake-up
01b - Idle match wake-up
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4615 / 5251


---
# 페이지 1756

Table continued from the previous page...
Field
Function
10b - Match on and match off
11b - Enables RWU on data match and match on or off for the transmitter CTS input
17
BOTHEDGE
Both Edge Sampling
Enables sampling of the received data on both edges of the baud rate clock, effectively doubling the number 
of times the receiver samples the input data for a given OSR.
This field must be 1 for OSRs between x4 and x7 and is optional for higher OSRs. You must change the 
value of this field only when the receiver is disabled.
If this field is 0, the receiver samples input data using the rising edge of the baud rate clock. If this field is 1, 
the receiver samples input data using the rising and falling edges of the baud rate clock.
0b - Rising edge
1b - Both rising and falling edges
16
RESYNCDIS
Resynchronization Disable
Disables resynchronization of the received data word when a data one followed by data zero transition 
is detected.
You must change the value of this field only when the receiver is disabled.
0b - Enable
1b - Disable
15
LBKDIE
LIN Break Detect Interrupt Enable
Enables STAT[LBKDIF] to generate hardware interrupt requests.
If this field is 0, hardware interrupts from STAT[LBKDIF] (uses polling) are disabled. If this field is 1, hardware 
interrupts are requested when STAT[LBKDIF] is 1.
0b - Disable
1b - Enable
14
RXEDGIE
RX Input Active Edge Interrupt Enable
Enables STAT[RXEDGIF] to generate interrupt requests. If this field is 0, hardware interrupts from 
STAT[RXEDGIF] are disabled. If this field is 1, hardware interrupts are requested when STAT[RXEDGIF] 
is 1.
Changing the value of CTRL[LOOPS] or CTRL[RSRC] when this field (RXEDGIE) is 1 can cause 
STAT[RXEDGIF] to become 1.
0b - Disable
1b - Enable
13
SBNS
Stop Bit Number Select
Determines whether data characters include one or two stop bits.
You must change the value of this field only when both the transmitter and receiver are disabled.
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4616 / 5251


---
# 페이지 1757

Table continued from the previous page...
Field
Function
0b - One stop bit
1b - Two stop bits
12-0
SBR
Baud Rate Modulo Divisor
Sets the modulo divide rate for the baud rate generator.
• If SBR is 0, baud rate generator is disabled.
• If SBR is 1–8191, baud rate = baud clock ÷ ((OSR + 1) × SBR). You must update the 13-bit baud 
rate setting [SBR12:SBR0] only when both the transmitter and receiver are disabled (both CTRL[RE] 
and CTRL[TE] are 0).
77.6.7 Status (STAT)
Offset
Register
Offset
STAT
14h
Function
Provides the module status.
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
LBKDI
F 
RXED
GIF 
MSBF 
RXINV 
RWUI
D 
BRK13 
LBKD
E 
RAF 
TDRE 
TC 
RDRF 
IDLE 
OR 
NF 
FE 
PF 
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
1
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
MA1F 
MA2F 
0
TSF 
MSF 
0
AME 
LBKFE 
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
0
Fields
Field
Function
31
LBKDIF
LIN Break Detect Interrupt Flag
Indicates whether a LIN break character is detected.
This field becomes 1 when the LIN break detect circuitry is enabled and a LIN break character is detected.
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4617 / 5251


---
# 페이지 1758

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not detected
1b - Detected
When writing
0b - No effect
1b - Clear the flag
30
RXEDGIF
RXD Pin Active Edge Interrupt Flag
Indicates whether an active edge on the receive pin has occurred.
This field becomes 1 whenever the receiver is enabled and an active edge (falling if STAT[RXINV] is 0; rising 
if STAT[RXINV] is 1) on the RXD pin occurs.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not occurred
1b - Occurred
When writing
0b - No effect
1b - Clear the flag
29
MSBF
MSB First
Specifies the first bit that is transmitted after the start bit.
If this field is 0, LSB (bit 0) is the first bit transmitted after the start bit (which means, the first bit received after 
the start bit is identified as bit 0).
If this field is 1, MSB (identified as bit 9, bit 8, bit 7, or bit 6) is the first bit that is transmitted, after the start 
bit, depending on the settings of CTRL[M], CTRL[PE], and BAUD[M10].
Writing 1 to this field reverses the order of the bits that are transmitted and received on the wire. This field 
does not affect the polarity of the bits, the location of the parity bit, or the location of the start or stop bits. 
You must change the value of this field only when both the transmitter and receiver are disabled.
0b - LSB
1b - MSB
28
RXINV
Receive Data Inversion
Specifies whether receive data is inverted.
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4618 / 5251


---
# 페이지 1759

Table continued from the previous page...
Field
Function
Writing 1 to this field reverses the polarity of the received data input. You must change the value of this field 
only when the receiver is disabled.
 
Writing 1 to this field inverts the RXD input for all cases: data bits, start and stop bits, break, 
and idle.
  NOTE  
0b - Inverted
1b - Not inverted
27
RWUID
Receive Wake Up Idle Detect
Controls, for CTRL[RWU] on idle character detection, whether the idle character that wakes up the receiver 
writes 1 to STAT[IDLE].
For address match wake-up, this field controls whether STAT[IDLE] = 1 when the address does not match. 
You must change the value of this field only when the receiver is disabled.
If this field is 0, during the Receive Standby state (CTRL[RWU] = 1), STAT[IDLE] does not become 1 upon 
detection of an idle character. During address match wake-up, STAT[IDLE] does not become 1 when an 
address does not match.
If this field is 1, during the Receive Standby state (CTRL[RWU] = 1), STAT[IDLE] becomes 1 upon detection 
of an idle character. During address match wake-up, STAT[IDLE] becomes 1 when an address does 
not match.
0b - STAT[IDLE] does not become 1
1b - STAT[IDLE] becomes 1
26
BRK13
Break Character Generation Length
Selects the longer transmitted break character length.
The state of this field does not affect the detection of a framing error. You must change the value of this 
field only when the transmitter is disabled. You can send a break character by writing 1 to CTRL[SBK], or 
by writing the transmit FIFO when DATA[FRETSC] is 1 and DATA[R9T9] is 0.
0b - 9 to 13 bit times
1b - 12 to 15 bit times
25
LBKDE
LIN Break Detection Enable
Enables LIN break detection.
If this field is 0, LIN break detect is disabled, and only a normal break character can be detected.
If this field is 1, LIN break detect is enabled and the LIN break character is detected at a length of 11 bit times 
(if CTRL[M] is 0), 12 bit times (if CTRL[M] is 1), or 13 bit times (if BAUD[M10] is 1).
This field selects a longer break character detection length. When the field is 1, receive data is not stored 
in the receive FIFO.
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4619 / 5251


---
# 페이지 1760

Table continued from the previous page...
Field
Function
 
This field enables the LIN break detect circuit and disables writing receive data to FIFO. 
Therefore, it ignores all characters except a LIN break.
  NOTE  
0b - Disable
1b - Enable
24
RAF
Receiver Active Flag
Indicates whether the LPUART receiver is idle or active.
This field becomes 1 when the receiver detects the beginning of a valid start bit, and the field becomes 0 
automatically when the receiver detects an idle line.
0b - Idle, waiting for a start bit
1b - Receiver active (RXD pin input not idle)
23
TDRE
Transmit Data Register Empty Flag
Indicates whether the transmit FIFO level is greater than, equal to, or less than the watermark.
After the transmit FIFO is enabled, this field becomes 1 when the number of datawords in the transmit FIFO 
is equal to, or less than the number that WATER[TXWATER] indicates. To make the value of this field 0, 
write to it until the number of words in the transmit FIFO is greater than the number that WATER[TXWATER] 
indicates. After the transmit FIFO is disabled, this field becomes 1 to indicate that the FIFO level is less than 
the watermark. To make the value of this field 0 again, write to Data (DATA).
This register is not affected by a character that is in the process of being transmitted; it is updated at the start 
of each transmitted character.
0b - Greater than watermark
1b - Equal to or less than watermark
22
TC
Transmission Complete Flag
Indicates whether the transmitter is active.
This field becomes 0 when a transmission is in progress or a preamble or break character is loaded; in other 
words, when the transmitter is active (sending data, a preamble, or a break). The field becomes 1 when the 
transmit buffer is empty and no data, preamble, or break character is being transmitted; in other words, when 
the transmission activity is complete. When this happens, the transmit data output signal becomes idle (logic 
1). This field becomes 0 after you write to Data (DATA) to transmit new data, queuing a preamble by first 
writing 0 and then writing 1 to CTRL[TE], queuing a break character by writing 1 to CTRL[SBK].
0b - Transmitter active
1b - Transmitter idle
21
RDRF
Receive Data Register Full Flag
Indicates whether the receive FIFO level is less than, equal to, or greater than the watermark.
This field becomes 1 when the number of datawords in the receive buffer is greater than the number 
that WATER[RXWATER] indicates and the receive FIFO is enabled. To write 0 to this field, read Data 
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4620 / 5251


---
# 페이지 1761

Table continued from the previous page...
Field
Function
(DATA) until the number of datawords in the receive FIFO is equal to, or less than the number that 
WATER[RXWATER] indicates. When the receive FIFO is disabled, this field (RDRF) becomes 1 if the 
receive buffer (Data (DATA)) is full. To make this field 0, read Data (DATA).
A character that is in the process of being received does not cause a change in this field until the entire 
character is received. Even if this field is 1, the character continues to be received until an overrun condition 
occurs after the entire character is received.
0b - Equal to or less than watermark
1b - Greater than watermark
20
IDLE
Idle Line Flag
Indicates whether an idle line is detected.
This field becomes 1 when the LPUART receive line becomes idle for a full character time after a period 
of activity. When CTRL[ILT] is 0, the receiver starts counting idle bit times after the start bit. If the receive 
character is all 1s, these bit times and the stop bit time count towards the full character time of logic high, 10 
to 13 bit times, needed for the receiver to detect an idle line. After CTRL[ILT] becomes 1, the receiver does 
not start counting idle bit times until after the stop bits. The stop bits and any logic high bit times at the end 
of the previous character do not count towards the full character time of logic high needed for the receiver 
to detect an idle line.
For this field to become 0, write 1 to it. After the field becomes 0, you cannot write 1 to it again until after a 
new character is stored in the receive buffer or a LIN break character writes 1 to STAT[LBKDIF]. This field 
becomes 1 only once, even if the receive line remains idle for an extended period.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Idle line detected
1b - Idle line not detected
When writing
0b - No effect
1b - Clear the flag
19
OR
Receiver Overrun Flag
Indicates whether there is receive overrun.
This field becomes 1 when you cannot prevent STAT[RDRF] from overflowing with data. The field becomes 
1 immediately after the stop bit is completely received for the dataword that overflows the buffer and all the 
other error fields (STAT[FE], STAT[NF], and STAT[PF]) are prevented from becoming 1. The data in the shift 
register is lost, but the data already in the LPUART data registers is not affected. If STAT[LBKDE] is enabled 
and a LIN break is detected, this field becomes 1 if STAT[LBKDIF] is not 0 before the next data character 
is received.
When this field is 1, no additional data is stored in the receive FIFO even if sufficient room exists.
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4621 / 5251


---
# 페이지 1762

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No overrun
1b - Receive overrun (new LPUART data is lost)
When writing
0b - No effect
1b - Clear the flag
18
NF
Noise Flag
Indicates whether noise is detected in the received character of Data (DATA).
The advanced sampling technique used in the receiver takes three samples in each of the received bits. If 
some of these samples disagree with the rest of the samples within any bit time in the frame, then noise is 
detected for that character. This field becomes 1 whenever the next character to be read from Data (DATA) 
is received with noise detected within the character.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No noise detected
1b - Noise detected
When writing
0b - No effect
1b - Clear the flag
17
FE
Framing Error Flag
Indicates whether a framing error is detected.
This field becomes 1 whenever the next character to be read from Data (DATA) is received with logic 0 
detected where a stop bit was expected.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No framing error detected (this does not guarantee that the framing is correct)
1b - Framing error detected
When writing
0b - No effect
1b - Clear the flag
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4622 / 5251


---
# 페이지 1763

Table continued from the previous page...
Field
Function
16
PF
Parity Error Flag
Indicates whether a parity error is detected.
This field becomes 1 whenever the next character to be read from Data (DATA) is received when parity 
is enabled (CTRL[PE] is 1) and the parity bit in the received character does not agree with the expected 
parity value.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No parity error detected
1b - Parity error detected
When writing
0b - No effect
1b - Clear the flag
15
MA1F
Match 1 Flag
Indicates whether the received data is equal to MATCH[MA1].
This field becomes 1 whenever the next character to be read from Data (DATA) matches the value 
of MATCH[MA1].
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not equal to MA1
1b - Equal to MA1
When writing
0b - No effect
1b - Clear the flag
14
MA2F
Match 2 Flag
Indicates whether the received data is equal to MATCH[MA2].
This field becomes 1 whenever the next character to be read from Data (DATA) matches the value 
of MATCH[MA2].
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Not equal to MA2
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4623 / 5251


---
# 페이지 1764

Table continued from the previous page...
Field
Function
1b - Equal to MA2
When writing
0b - No effect
1b - Clear the flag
13-10
—
Reserved
9
TSF
Timeout Status Flag
Indicates whether a field in Timeout Status (TOSR) is 1 and configured to generate an interrupt.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
LPUART_0
STAT
—
LPUART_1
STAT
—
LPUART_2
—
STAT
LPUART_3
—
STAT
LPUART_4
—
STAT
LPUART_5
—
STAT
LPUART_6
—
STAT
LPUART_7
—
STAT
LPUART_8
—
STAT
LPUART_9
—
STAT
LPUART_10
—
STAT
LPUART_11
—
STAT
LPUART_12
—
STAT
LPUART_13
—
STAT
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4624 / 5251


---
# 페이지 1765

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
LPUART_14
—
STAT
LPUART_15
—
STAT
0b - Field is 0
1b - Field is 1
8
MSF
MODEM Status Flag
Indicates whether a field in MODEM Status (MSR) is 1 and configured to generate an interrupt.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
LPUART_0
STAT
—
LPUART_1
STAT
—
LPUART_2
—
STAT
LPUART_3
—
STAT
LPUART_4
—
STAT
LPUART_5
—
STAT
LPUART_6
—
STAT
LPUART_7
—
STAT
LPUART_8
—
STAT
LPUART_9
—
STAT
LPUART_10
—
STAT
LPUART_11
—
STAT
LPUART_12
—
STAT
LPUART_13
—
STAT
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4625 / 5251


---
# 페이지 1766

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
LPUART_14
—
STAT
LPUART_15
—
STAT
0b - Field is 0
1b - Field is 1
7-2
—
Reserved
1
AME
Address Mark Enable
Configures the location of the address mark when configured for MSB first transfers.
This field has no effect when configured for LSB first and you must change the value of this field only when 
both the transmitter and receiver are disabled. If this field is 0, address mark in character is MSB. If this field 
is 1, the address mark is stored in Data (DATA) at MSB (or MSB-1 when the parity bit is enabled). In other 
words, the address mark in character is the last bit before the stop bit (or parity bit when enabled).
0b - Disable
1b - Enable
0
LBKFE
LIN Break Flag Enable
Enables the LIN break flag to assert whenever a LIN break character is detected.
Unlike STAT[LBKDE], this does not impact data being stored in the receive data buffer, but does cause 
STAT[LBKDIF] to become 1 whenever a LIN break is detected.
Because a LIN break is longer than a normal character, the LIN break triggers a write to STAT[RDRF] with 
the data fields as 0 and STAT[FE] as 1. The character following the LIN break has DATA[LINBRK] as 1 to 
indicate that the previous character was a LIN break.
You must change the value of this field only when both the transmitter and receiver are disabled.
If this field is 1, the LIN break character is detected at a length of 11-bit times (if CTRL[M] is 0), 12 (if CTRL[M] 
is 1), or 13 (if BAUD[M10] is 1).
0b - Disable
1b - Enable
77.6.8 Control (CTRL)
Offset
Register
Offset
CTRL
18h
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4626 / 5251


---
# 페이지 1767

Function
Controls various optional features of the LPUART system.
You must write to the fields of this register only when both the transmitter and receiver are disabled.
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
R8T9 
R9T8 
TXDIR 
TXINV 
ORIE 
NEIE 
FEIE 
PEIE 
TIE 
TCIE 
RIE 
ILIE 
TE 
RE 
RWU 
SBK 
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
MA1IE 
MA2IE 
0
0
M7 
IDLECFG 
LOOP
S 
Reserv
ed 
RSRC 
M 
WAKE 
ILT 
PE 
PT 
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
R8T9
Receive Bit 8 Transmit Bit 9
Contains R8 and T9 that correspond to different functions.
R8 is the ninth data bit received after you configure LPUART for 9-bit or 10-bit data formats. When reading 
9-bit or 10-bit data, read R8 before reading Data (DATA).
T9 is the tenth data bit transmitted after you configure LPUART for 10-bit data formats. When writing 10-bit 
data, write T9 before writing to Data (DATA). If T9 does not need to change from its previous value, such 
as when it is used to generate address mark or parity, then you need not write to it each time you write to 
Data (DATA).
 
R8 is a read-only bit and T9 is a write-only bit; the value read is different from the 
value written.
  NOTE  
30
R9T8
Receive Bit 9 Transmit Bit 8
Contains R9 and T8 that correspond to different functions.
R9 is the tenth data bit received after you configure LPUART for 10-bit data formats. When reading 10-bit 
data, read R9 before reading Data (DATA).
T8 is the ninth data bit transmitted after you configure LPUART for 9-bit or 10-bit data formats. When writing 
9-bit or 10-bit data, write T8 before writing to Data (DATA). If T8 does not need to change from its previous 
value, such as when it is used to generate address mark or parity, then you need not write to it each time 
you write to Data (DATA).
 
R9 is a read-only field and T8 is a write-only field; the value read is different from the 
value written.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4627 / 5251


---
# 페이지 1768

Table continued from the previous page...
Field
Function
29
TXDIR
TXD Pin Direction in Single-Wire Mode
Determines the direction of data at the TXD pin, in Single-Wire mode, when LPUART is configured for a 
single-wire half-duplex operation (CTRL[LOOPS] and CTRL[RSRC] are 1). When writing 0 to this field, 
the transmitter finishes transmitting the current character (if any) before the receiver starts receiving data 
from the TXD pin.
0b - Input
1b - Output
28
TXINV
Transmit Data Inversion
Specifies whether transmit data is inverted.
Writing 1 to this field reverses the polarity of the transmitted data output. This action inverts the TXD output 
for all cases: data bits, start and stop bits, break, and idle.
0b - Not inverted
1b - Inverted
27
ORIE
Overrun Interrupt Enable
Enables STAT[OR] to generate hardware interrupt requests. When this field is 1, a hardware interrupt is 
requested. Use polling when OR interrupts are disabled.
0b - Disable
1b - Enable
26
NEIE
Noise Error Interrupt Enable
Enables STAT[NF] to generate hardware interrupt requests. When this field is 1, a hardware interrupt is 
requested. Use polling when NF interrupts are disabled.
0b - Disable
1b - Enable
25
FEIE
Framing Error Interrupt Enable
Enables STAT[FE] to generate hardware interrupt requests. When this field is 1, a hardware interrupt is 
requested. Use polling when FE interrupts are disabled.
0b - Disable
1b - Enable
24
PEIE
Parity Error Interrupt Enable
Enables STAT[PF] to generate hardware interrupt requests. When this field is 1, a hardware interrupt is 
requested. Use polling when PF interrupts are disabled.
0b - Disable
1b - Enable
23
Transmit Interrupt Enable
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4628 / 5251


---
# 페이지 1769

Table continued from the previous page...
Field
Function
TIE
Enables STAT[TDRE] to generate interrupt requests if STAT[TDRE] is 1.
0b - Disable
1b - Enable
22
TCIE
Transmission Complete Interrupt Enable
Enables STAT[TC] to generate interrupt requests if STAT[TC] is 1.
0b - Disable
1b - Enable
21
RIE
Receiver Interrupt Enable
Enables STAT[RDRF] to generate hardware interrupt requests if STAT[RDRF] is 1.
0b - Disable
1b - Enable
20
ILIE
Idle Line Interrupt Enable
Enables hardware interrupts.
This field enables STAT[IDLE] to generate interrupt requests.
If this field is 0, hardware interrupts from STAT[IDLE] are disabled and polling is used, and if this field is 1, 
hardware interrupts are enabled when STAT[IDLE] is 1.
0b - Disable
1b - Enable
19
TE
Transmitter Enable
Enables the LPUART transmitter.
Using this field, you can also queue an idle preamble by first writing 0 and then writing 1 to this field. After 
this field becomes 0, the field reads 1 until the transmitter has completed the current character and the TXD 
pin is tristated.
You can also queue a single idle character by writing to the transmit FIFO with DATA[FRETSC] and 
DATA[R9T9] = 1.
0b - Disable
1b - Enable
18
RE
Receiver Enable
Enables the LPUART receiver.
After you write 0 to this field, this field remains 1 until the receiver finishes receiving the current character 
(if any).
0b - Disable
1b - Enable
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4629 / 5251


---
# 페이지 1770

Table continued from the previous page...
Field
Function
17
RWU
Receiver Wake-Up Control
Specifies whether the LPUART receiver in standby is waiting for a wake-up condition.
You can write 1 to this field to place the LPUART receiver in a Standby state. The field becomes 0 
automatically when an RWU event occurs, that is, in case of an idle event when CTRL[WAKE] is 0 or an 
address match when CTRL[WAKE] is 1 and STAT[RWUID] is 0.
 
You must write 1 to this field only when CTRL[WAKE] is 0 (wake-up on idle), if the channel 
is currently not idle. You can determine this by the value of STAT[RAF]. If the field is 1 to 
wake up an idle event and the channel is already idle, LPUART, possibly, discards the data. 
This is because the data must be received or a LIN break is detected after an Idle condition 
is detected before the IDLE flag is allowed to be reasserted.
  NOTE  
0b - Normal receiver operation
1b - LPUART receiver in standby, waiting for a wake-up condition
16
SBK
Send Break
Specifies whether queue break character(s) are to be sent.
Writing 1 and then 0 to this field queues a break character in the transmit data stream. Additional break 
characters of 9 to 13 bits, or 12 to 15 bits if STAT[BRK13] is 1, and bit times of logic 0 are queued as long 
as this field is 1. Depending on the timing when this field is 1 and 0, relative to the character currently being 
transmitted, a second break character may be queued before you write 0 to this field. If the time taken to write 
0 to this field is too long, for example, if the field does not become 0 by the end of the first break character, 
a second break character is sent. This is compared to queuing a break character through the transmit FIFO 
that guarantees only one break character is sent.
You can also queue a single break character by writing to the transmit FIFO when DATA[FRETSC] is 1 and 
DATA[R9T9] is 0.
0b - Normal transmitter operation
1b - Queue break character(s) to be sent
15
MA1IE
Match 1 (MA1F) Interrupt Enable
Enables the MA1F interrupt.
0b - Disable
1b - Enable
14
MA2IE
Match 2 (MA2F) Interrupt Enable
Enables the MA2F interrupt.
0b - Disable
1b - Enable
13
—
Reserved
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4630 / 5251


---
# 페이지 1771

Table continued from the previous page...
Field
Function
12
—
Reserved
11
M7
7-Bit Mode Select
Specifies the data characters that the receiver and transmitter use.
You must change the value of this field only after both the transmitter and receiver are disabled.
0b - 8-bit to 10-bit
1b - 7-bit
10-8
IDLECFG
Idle Configuration
Configures the number of idle characters that must be received before you write 1 to STAT[IDLE].
000b - 1
001b - 2
010b - 4
011b - 8
100b - 16
101b - 32
110b - 64
111b - 128
7
LOOPS
Loop Mode Select
Selects Loop mode.
After this field becomes 1, the RXD pin is disconnected from LPUART and the transmitter output is internally 
connected to the receiver input. The transmitter and receiver must be enabled to use the loop function. 
In Loop mode or Single-Wire mode, the transmitter outputs are internally connected to the receiver input 
(see CTRL[RSRC]).
0b - Normal operation: RXD and TXD use separate pins
1b - Loop mode or Single-Wire mode
6
—
Reserved
5
RSRC
Receiver Source Select
Determines the source of the receiver shift register input if CTRL[LOOPS] is 1.
This field has no effect unless CTRL[LOOPS] is 1.
If this field is 0, internal Loopback mode is selected. LPUART does not use the RXD pin. Additionally, the 
CTS_B pin is not used and internally driven by the RTS_B output.
If this field is 1, single-wire LPUART mode is selected where the TXD pin is connected to the transmitter 
output and receiver input.
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4631 / 5251


---
# 페이지 1772

Table continued from the previous page...
Field
Function
0b - Internal Loopback mode
1b - Single-wire mode
4
M
9-Bit Or 8-Bit Mode Select
Specifies the data characters that the receiver and transmitter use.
0b - 8-bit
1b - 9-bit
3
WAKE
Receiver Wake-Up Method Select
Determines which condition wakes up LPUART when CTRL[RWU] = 1 and BAUD[MATCFG] = 0 (this field 
must be 1 when BAUD[MATCFG] = 11):
• Address mark in the bit preceding the stop bit (or bit preceding the parity bit when parity is enabled) 
of the received data character
• An idle condition on the receive pin input signal
If this field is 0, CTRL[RWU] is configured for idle line wake-up, and if this field is 1, CTRL[RWU] is configured 
with address mark wake-up.
0b - Idle
1b - Mark
2
ILT
Idle Line Type Select
Determines when the receiver starts counting logic 1s as idle character bits.
The count begins either after a valid start bit or the stop bit. If the count begins after the start bit, a string of 
logic 1s preceding the stop bit can cause false recognition of an idle character. Beginning the count after the 
stop bit avoids false idle character recognition, but requires properly synchronized transmissions.
 
In case you write 1 to this field, a logic 0 is automatically shifted after a received stop bit, 
therefore resetting the idle count.
  NOTE  
0b - After the start bit
1b - After the stop bit
1
PE
Parity Enable
Enables hardware parity generation and checking.
If parity is enabled, the bit immediately before the stop bit is treated as the parity bit.
0b - Disable
1b - Enable
0
PT
Parity Type
Selects the type of parity, even or odd, if parity is enabled (CTRL[PE] = 1):
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4632 / 5251


---
# 페이지 1773

Table continued from the previous page...
Field
Function
• Odd parity means that the total number of logic 1 bits in the data character, including the parity bit, is 
odd.
• Even parity means that the total number of 1s in the data character, including the parity bit, is even.
0b - Even parity
1b - Odd parity
77.6.9 Data (DATA)
Offset
Register
Offset
DATA
1Ch
Function
Supports 8-bit, 16-bit, or 32-bit writes, each type of write performing a separate function. An 8-bit write to DATA[7:0] pushes 
{CTRL[R8T9], CTRL[R9T8], DATA[7:0]} the transmit FIFO with TSC clear. A 16-bit or 32-bit write pushes the data written into the 
FIFO and does not update the value of CTRL[R8T9] or CTRL[R9T8].
Reads and writes of this register are also involved in the automatic flag clearing mechanisms for some of the LPUART status fields.
 
Reads return the contents of the read-only receive FIFO and writes go to the write-only transmit FIFO, making this 
register work as a set of two separate registers.
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
NOISY 
PARIT
YE 
FRET
SC 
RXEM
PT 
IDLIN
E 
LINBR
K 
R9T9 
R8T8 
R7T7 
R6T6 
R5T5 
R4T4 
R3T3 
R2T2 
R1T1 
R0T0 
W
Reset
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
0
0
0
0
0
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4633 / 5251


---
# 페이지 1774

Fields
Field
Function
31-16
—
Reserved
15
NOISY
Noisy Data Received
Indicates whether the current received dataword contained in DATA[R9:R0] is received with noise.
0b - Received without noise
1b - Received with noise
14
PARITYE
Parity Error
Indicates whether the current received dataword contained in DATA[R9:R0] is received with a parity 
error.
0b - Received without a parity error
1b - Received with a parity error
13
FRETSC
Frame Error Transmit Special Character
Specifies the way the dataword is received.
For reads, this field indicates that the current received dataword contained in DATA[R9:R0] is received with 
a frame error. For writes, the field indicates that a break or idle character is to be transmitted instead of the 
contents in DATA[T9:T0]. T9 indicates a break character when it is 0 and indicates an idle character when 
it is 1. The contents of DATA[T8:T0] must be 0.
0b - Received without a frame error on reads or transmits a normal character on writes
1b - Received with a frame error on reads or transmits an idle or break character on writes
12
RXEMPT
Receive Buffer Empty
Indicates whether the receive buffer contains valid data.
This field becomes 1 when there is no data in the receive buffer. The field does not consider data in the 
receive shift register.
0b - Valid data
1b - Invalid data and empty
11
IDLINE
Idle Line
Indicates whether the receiver line was idle before receiving the character in DATA[9:0]. It can be read 
as “1” on the first character when the receiver is first enabled. The difference between this field and 
STAT[IDLE] is that, STAT[IDLE] flag does not set on an idle line after the receiver is first enabled, it 
needs to receive a character before it can become set, whereas this field does not have this limitation 
and can be set on the first character received if an idle line is detected beforehand.
0b - Not idle
1b - Idle
10
LIN Break
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4634 / 5251


---
# 페이지 1775

Table continued from the previous page...
Field
Function
LINBRK
Indicates whether the receiver line detected a LIN break before receiving the character in DATA[9:0]. 
This field requires the value of STAT[LBKDIF] to be 1. If this field is 0, the LIN break detect circuitry is 
disabled.
0b - Not detected
1b - Detected
9
R9T9
Read receive FIFO bit 9 or write transmit FIFO bit 9
8
R8T8
Read receive FIFO bit 8 or write transmit FIFO bit 8
7
R7T7
Read receive FIFO bit 7 or write transmit FIFO bit 7
6
R6T6
Read receive FIFO bit 6 or write transmit FIFO bit 6
5
R5T5
Read receive FIFO bit 5 or write transmit FIFO bit 5
4
R4T4
Read receive FIFO bit 4 or write transmit FIFO bit 4
3
R3T3
Read receive FIFO bit 3 or write transmit FIFO bit 3
2
R2T2
Read receive FIFO bit 2 or write transmit FIFO bit 2
1
R1T1
Read receive FIFO bit 1 or write transmit FIFO bit 1
0
R0T0
Read receive FIFO bit 0 or write transmit FIFO bit 0
77.6.10 Match Address (MATCH)
Offset
Register
Offset
MATCH
20h
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4635 / 5251


---
# 페이지 1776

Function
Provides addresses for address matching during the receiver operation.
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
MA2 
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
MA1 
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
31-26
—
Reserved
25-16
MA2
Match Address 2
Is compared to input data addresses when the most significant bit is 1 and the associated Baud Rate (BAUD) 
field is 1.
If a match occurs, the data that follows is transferred to Data (DATA). If a match fails, the data that follows is 
discarded. You must write to MATCH[MA1] and MATCH[MA2] only when the associated Baud Rate (BAUD) 
field is 0.
15-10
—
Reserved
9-0
MA1
Match Address 1
Is compared to input data addresses when the most significant bit is 1 and the associated Baud Rate (BAUD) 
field is 1.
If a match occurs, the data that follows is transferred to Data (DATA). If a match fails, the data that follows is 
discarded. You must write to MATCH[MA1] and MATCH[MA2] fields only when the associated field in Baud 
Rate (BAUD) is 0.
77.6.11 MODEM IrDA (MODIR)
Offset
Register
Offset
MODIR
24h
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4636 / 5251


---
# 페이지 1777

Function
Controls options for setting the MODEM configuration.
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
IREN 
TNP 
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
RTSWATER 
0
TXCT
SSRC 
TXCT
SC 
RXRT
SE 
TXRT
SPOL 
TXRT
SE 
TXCT
SE 
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
IREN
IR Enable
Enables IR modulation and demodulation.
You must change the value of this field only when both the transmitter and receiver are disabled.
0b - Disable
1b - Enable
17-16
TNP
Transmitter Narrow Pulse
Specifies whether LPUART transmits a 1 ÷ OSR, 2 ÷ OSR, 3 ÷ OSR, or 4 ÷ OSR narrow pulse when the IR 
pulse is enabled.
You must change the value of this field only when both the transmitter and receiver are disabled.
The IR pulse width must be configured to less than half of the OSR. Common pulse widths are 3 ÷ 16, 1 ÷ 16, 
1 ÷ 32, or 1 ÷ 4 of the bit length. You can configure these by selecting the appropriate OSR and pulse width.
00b - 1 ÷ OSR
01b - 2 ÷ OSR
10b - 3 ÷ OSR
11b - 4 ÷ OSR
15-12
—
Reserved
11-8
Receive RTS Configuration
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4637 / 5251


---
# 페이지 1778

Table continued from the previous page...
Field
Function
RTSWATER
Configures the assertion and negation of the receiver's RTS_B output.
The receiver's RTS_B output negates when the number of empty words in the receive FIFO is greater or 
equal to the value of this field. If this field is 0, the RTS_B pin negates when the receive FIFO is full. For the 
purpose of receive RTS_B generation, the number of words in the receive FIFO updates when a start bit is 
detected. This supports additional latency between RTS_B negation and the external transmitter ceasing 
transmission. If both receive RTS_B and address or data matching is enabled, RTS_B could assert at the 
end of a character if there exists no match.
You must change the value of this field only when the receiver is disabled.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
LPUART_0
MODIR
—
LPUART_1
MODIR
—
LPUART_2
MODIR[9–8]
MODIR[11–10]
LPUART_3
MODIR[9–8]
MODIR[11–10]
LPUART_4
MODIR[9–8]
MODIR[11–10]
LPUART_5
MODIR[9–8]
MODIR[11–10]
LPUART_6
MODIR[9–8]
MODIR[11–10]
LPUART_7
MODIR[9–8]
MODIR[11–10]
LPUART_8
MODIR[9–8]
MODIR[11–10]
LPUART_9
MODIR[9–8]
MODIR[11–10]
LPUART_10
MODIR[9–8]
MODIR[11–10]
LPUART_11
MODIR[9–8]
MODIR[11–10]
LPUART_12
MODIR[9–8]
MODIR[11–10]
LPUART_13
MODIR[9–8]
MODIR[11–10]
LPUART_14
MODIR[9–8]
MODIR[11–10]
LPUART_15
MODIR[9–8]
MODIR[11–10]
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4638 / 5251


---
# 페이지 1779

Table continued from the previous page...
Field
Function
7-6
—
Reserved
5
TXCTSSRC
Transmit CTS Source
Configures the source of the CTS input.
0b - The CTS_B pin
1b - An internal connection to the receiver address match result
4
TXCTSC
Transmit CTS Configuration
Configures whether the CTS state or input is checked or sampled at the start of each character or only 
when the transmitter is idle.
0b - Sampled at the start of each character
1b - Sampled when the transmitter is idle
3
RXRTSE
Receiver RTS Enable
Allows the RTS output to control the CTS input of the transmitting device to prevent receiver overrun.
You must change the value of this field only when the receiver is disabled.
If this field is 0, the receiver has no effect on RTS.
If this field is 1, RTS is deasserted if STAT[RDRF] is 1 or a start bit is detected that causes STAT[RDRF] to 
become 1. RTS is asserted if STAT[RDRF] is 0 and has not detected a start bit that causes STAT[RDRF] 
to become 1.
 
Do not write 1 to both MODIR[RXRTSE] and MODIR[TXRTSE].
  NOTE  
0b - Disable
1b - Enable
2
TXRTSPOL
Transmitter RTS Polarity
Controls the polarity of the transmitter RTS.
This field does not affect the polarity of the receiver RTS that remains negated in the active-low state unless 
MODIR[TXRTSE] is 1. You must change the value of this field only when the transmitter is disabled.
0b - Active low
1b - Active high
1
TXRTSE
Transmitter RTS Enable
Controls the operation of RTS before and after a transmission.
You must change the value of this field only when the transmitter is disabled. If this field is 0, the transmitter 
has no effect on RTS, and if this field is 1, a character is placed into an empty transmit shift register. 
RTS asserts 1-bit time before the start bit is transmitted and deasserts 1-bit time after all characters in the 
transmitter FIFO and shift register are completely sent, including the last stop bit.
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4639 / 5251


---
# 페이지 1780

Table continued from the previous page...
Field
Function
0b - Disable
1b - Enable
0
TXCTSE
Transmitter CTS Enable
Enables the operation of the transmitter.
You can write 1 to this field irrespective of the states of MODIR[TXRTSE] and MODIR[RXRTSE]. If this 
field is 1, the transmitter checks the state of the CTS signal each time it is ready to send a character. If 
CTS is asserted, the character is sent. If CTS is deasserted, the TXD signal remains in the mark state and 
transmission is delayed until CTS is asserted. Changes in CTS, when a character is being sent, do not affect 
its transmission.
0b - Disable
1b - Enable
77.6.12 FIFO (FIFO)
Offset
Register
Offset
FIFO
28h
Function
Provides you the ability to turn on and turn off the FIFO functionality.
This register also provides you the size of the FIFO that has been implemented. You can read this register at any time and must 
write to it only when CTRL[RE] and CTRL[TE] are 0 and the FIFO is empty.
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
TXEM
PT 
RXEM
PT 
0
TXOF 
RXUF 
W
W1C
W1C
Reset
See Register reset values.
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
RXIDEN 
TXOF
E 
RXUF
E 
TXFE 
TXFIFOSIZE 
RXFE 
RXFIFOSIZE 
W
TXFLU
SH 
RXFL
USH 
Reset
See Register reset values.
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4640 / 5251


---
# 페이지 1781

Register reset values
Register
Reset value
FIFO
LPUART_0,LPUART_1: 00C0_0033h
LPUART_2–LPUART_15: 00C0_0011h
Fields
Field
Function
31-24
—
Reserved
23
TXEMPT
Transmit FIFO Or Buffer Empty
Indicates whether the transmit buffer is empty.
This field becomes 1 when there is no data in the transmit FIFO or buffer. The field does not consider data 
in the transmit shift register.
0b - Not empty
1b - Empty
22
RXEMPT
Receive FIFO Or Buffer Empty
Indicates whether the receive buffer is empty.
This field becomes 1 when there is no data in the receive FIFO or buffer. The field does not consider data 
in the receive shift register.
0b - Not empty
1b - Empty
21-18
—
Reserved
17
TXOF
Transmitter FIFO Overflow Flag
Indicates whether more data has been written to the transmit FIFO than it can hold.
If this field is 0, no transmit FIFO overflow has occurred since the last time the field was cleared, and if this 
field is 1, at least one transmit FIFO overflow has occurred since the last time the field was cleared.
This field becomes 1 regardless of the value of FIFO[TXOFE]. However, an interrupt is issued to the host 
only if FIFO[TXOFE] is 1.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No overflow
1b - Overflow
When writing
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4641 / 5251


---
# 페이지 1782

Table continued from the previous page...
Field
Function
0b - No effect
1b - Clear the flag
16
RXUF
Receiver FIFO Underflow Flag
Indicates whether more data has been read from the receive FIFO than was present.
If this field is 0, no receive FIFO underflow has occurred since the last time the field was cleared, and if this 
field is 1, at least one receive FIFO underflow has occurred since the last time the field was cleared.
This field becomes 1 regardless of the value of FIFO[RXUFE]. However, an interrupt is issued to the host 
only if FIFO[RXUFE] is 1.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - No underflow
1b - Underflow
When writing
0b - No effect
1b - Clear the flag
15
TXFLUSH
Transmit FIFO Flush
Causes all data that is stored in the transmit FIFO to be flushed.
If you write 0 to this field, no flush operation occurs, and if you write 1 to this field, all data in the transmit 
FIFO or buffer clears out.
This does not affect data in the transmit shift register.
0b - No effect
1b - All data flushed out
14
RXFLUSH
Receive FIFO Flush
Causes all data that is stored in the receive FIFO to be flushed.
If you write 0 to this field, no flush operation occurs, and if you write 1 to this field, all data in the receive FIFO 
or buffer clears out.
This does not affect data in the receive shift register.
0b - No effect
1b - All data flushed out
13
—
Reserved
12-10
Receiver Idle Empty Enable
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4642 / 5251


---
# 페이지 1783

Table continued from the previous page...
Field
Function
RXIDEN
Enables STAT[RDRF] to become 1 when the receiver is idle for a number of idle characters and the 
FIFO is not empty. This feature is not supported when the receiver extended idle time is enabled.
000b - Disable STAT[RDRF] to become 1 because of partially filled FIFO when the receiver is idle
001b - Enable STAT[RDRF] to become 1 because of partially filled FIFO when the receiver is idle 
for one character
010b - Enable STAT[RDRF] to become 1 because of partially filled FIFO when the receiver is idle 
for two characters
011b - Enable STAT[RDRF] to become 1 because of partially filled FIFO when the receiver is idle 
for four characters
100b - Enable STAT[RDRF] to become 1 because of partially filled FIFO when the receiver is idle 
for eight characters
101b - Enable STAT[RDRF] to become 1 because of partially filled FIFO when the receiver is idle 
for 16 characters
110b - Enable STAT[RDRF] to become 1 because of partially filled FIFO when the receiver is idle 
for 32 characters
111b - Enable STAT[RDRF] to become 1 because of partially filled FIFO when the receiver is idle 
for 64 characters
9
TXOFE
Transmit FIFO Overflow Interrupt Enable
Enables FIFO[TXOF] to generate an interrupt to the host.
0b - Disable
1b - Enable
8
RXUFE
Receive FIFO Underflow Interrupt Enable
Enables FIFO[RXUF] to generate an interrupt to the host.
0b - Disable
1b - Enable
7
TXFE
Transmit FIFO Enable
Enables the transmit FIFO.
If this field is 0, the transmit buffer operates as a FIFO of depth equal to 1 dataword, regardless of the value 
in FIFO[TXFIFOSIZE]. Both CTRL[TE] and CTRL[RE] must be 0 before you change the value of this field.
If this field is 1, the built-in FIFO structure for the transmit buffer is enabled. FIFO[TXFIFOSIZE] indicates 
the size of the FIFO structure.
0b - Disable
1b - Enable
6-4
TXFIFOSIZE
Transmit FIFO Buffer Depth
Indicates the maximum number of transmit datawords (transmit FIFO buffer depth) that can be stored in the 
transmit buffer.
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4643 / 5251


---
# 페이지 1784

Table continued from the previous page...
Field
Function
000b - 1
001b - 4
010b - 8
011b - 16
100b - 32
101b - 64
110b - 128
111b - 256
3
RXFE
Receive FIFO Enable
Enables the receive FIFO.
If this field is 0, the receive buffer operates as a FIFO of depth equal to 1 dataword, regardless of the value 
in FIFO[RXFIFOSIZE]. Both CTRL[RE] and CTRL[TE] must be 0 before you change the value of this field.
If this field is 1, the built-in FIFO structure for the receive buffer is enabled. FIFO[RXFIFOSIZE] indicates the 
size of the FIFO structure.
0b - Disable
1b - Enable
2-0
RXFIFOSIZE
Receive FIFO Buffer Depth
Indicates the maximum number of receive datawords (receive FIFO buffer depth) that can be stored in 
the receive buffer before an overrun occurs.
000b - 1
001b - 4
010b - 8
011b - 16
100b - 32
101b - 64
110b - 128
111b - 256
77.6.13 Watermark (WATER)
Offset
Register
Offset
WATER
2Ch
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4644 / 5251


---
# 페이지 1785

Function
Provides the ability to set a programmable threshold for notification, or sets the programmable thresholds to indicate that transmit 
data can be written or receive data can be read.
You may read this register at any time but must write to it only when CTRL[TE] is 0.
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
TXCOUNT 
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
31-29
—
Reserved
28-24
RXCOUNT
Receive Counter
Indicates the number of datawords in the receive FIFO or buffer.
If a dataword is being received in the receive shift register, it is not included in the count. This value may be 
used in conjunction with FIFO[RXFIFOSIZE] to calculate the room left in the receive FIFO or buffer.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
LPUART_0
WATER
—
LPUART_1
WATER
—
LPUART_2
WATER[26–24]
WATER[28–27]
LPUART_3
WATER[26–24]
WATER[28–27]
LPUART_4
WATER[26–24]
WATER[28–27]
LPUART_5
WATER[26–24]
WATER[28–27]
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4645 / 5251


---
# 페이지 1786

Field
Function
Instance
Field supported in
Field not supported in
LPUART_6
WATER[26–24]
WATER[28–27]
LPUART_7
WATER[26–24]
WATER[28–27]
LPUART_8
WATER[26–24]
WATER[28–27]
LPUART_9
WATER[26–24]
WATER[28–27]
LPUART_10
WATER[26–24]
WATER[28–27]
LPUART_11
WATER[26–24]
WATER[28–27]
LPUART_12
WATER[26–24]
WATER[28–27]
LPUART_13
WATER[26–24]
WATER[28–27]
LPUART_14
WATER[26–24]
WATER[28–27]
LPUART_15
WATER[26–24]
WATER[28–27]
23-20
—
Reserved
19-16
RXWATER
Receive Watermark
Generates an interrupt or a DMA request if the number of datawords in the receive FIFO or buffer is greater 
than the value of this field.
For proper operation, the value of this field must be less than the size of the receive FIFO or buffer, as 
indicated by FIFO[RXFIFOSIZE] and FIFO[RXFE].
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
LPUART_0
WATER
—
LPUART_1
WATER
—
LPUART_2
WATER[17–16]
WATER[19–18]
LPUART_3
WATER[17–16]
WATER[19–18]
LPUART_4
WATER[17–16]
WATER[19–18]
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4646 / 5251


---
# 페이지 1787

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
LPUART_5
WATER[17–16]
WATER[19–18]
LPUART_6
WATER[17–16]
WATER[19–18]
LPUART_7
WATER[17–16]
WATER[19–18]
LPUART_8
WATER[17–16]
WATER[19–18]
LPUART_9
WATER[17–16]
WATER[19–18]
LPUART_10
WATER[17–16]
WATER[19–18]
LPUART_11
WATER[17–16]
WATER[19–18]
LPUART_12
WATER[17–16]
WATER[19–18]
LPUART_13
WATER[17–16]
WATER[19–18]
LPUART_14
WATER[17–16]
WATER[19–18]
LPUART_15
WATER[17–16]
WATER[19–18]
15-13
—
Reserved
12-8
TXCOUNT
Transmit Counter
Indicates the number of datawords in the transmit FIFO or buffer.
If a dataword is being transmitted to the transmit shift register, it is not included in the count. This value may 
be used in conjunction with the value of FIFO[TXFIFOSIZE] to calculate the room left in the transmit FIFO 
or buffer.
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
LPUART_0
WATER
—
LPUART_1
WATER
—
LPUART_2
WATER[10–8]
WATER[12–11]
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4647 / 5251


---
# 페이지 1788

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
LPUART_3
WATER[10–8]
WATER[12–11]
LPUART_4
WATER[10–8]
WATER[12–11]
LPUART_5
WATER[10–8]
WATER[12–11]
LPUART_6
WATER[10–8]
WATER[12–11]
LPUART_7
WATER[10–8]
WATER[12–11]
LPUART_8
WATER[10–8]
WATER[12–11]
LPUART_9
WATER[10–8]
WATER[12–11]
LPUART_10
WATER[10–8]
WATER[12–11]
LPUART_11
WATER[10–8]
WATER[12–11]
LPUART_12
WATER[10–8]
WATER[12–11]
LPUART_13
WATER[10–8]
WATER[12–11]
LPUART_14
WATER[10–8]
WATER[12–11]
LPUART_15
WATER[10–8]
WATER[12–11]
7-4
—
Reserved
3-0
TXWATER
Transmit Watermark
Generates an interrupt or a DMA request when the number of datawords in the transmit FIFO or buffer is 
equal to or less than the value of this field.
For proper operation, the value of this field must be less than the size of the transmit buffer or FIFO, as 
indicated by FIFO[TXFIFOSIZE] and FIFO[TXFE].
 
This field is not supported in every instance. The following table includes only 
supported registers.
  NOTE  
Instance
Field supported in
Field not supported in
LPUART_0
WATER
—
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4648 / 5251


---
# 페이지 1789

Table continued from the previous page...
Field
Function
Instance
Field supported in
Field not supported in
LPUART_1
WATER
—
LPUART_2
WATER[1–0]
WATER[3–2]
LPUART_3
WATER[1–0]
WATER[3–2]
LPUART_4
WATER[1–0]
WATER[3–2]
LPUART_5
WATER[1–0]
WATER[3–2]
LPUART_6
WATER[1–0]
WATER[3–2]
LPUART_7
WATER[1–0]
WATER[3–2]
LPUART_8
WATER[1–0]
WATER[3–2]
LPUART_9
WATER[1–0]
WATER[3–2]
LPUART_10
WATER[1–0]
WATER[3–2]
LPUART_11
WATER[1–0]
WATER[3–2]
LPUART_12
WATER[1–0]
WATER[3–2]
LPUART_13
WATER[1–0]
WATER[3–2]
LPUART_14
WATER[1–0]
WATER[3–2]
LPUART_15
WATER[1–0]
WATER[3–2]
77.6.14 Data Read-Only (DATARO)
Offset
Register
Offset
DATARO
30h
Function
Indicates the first entry in the receive FIFO, but does not pull data from the FIFO.
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4649 / 5251


---
# 페이지 1790

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
DATA 
W
Reset
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
DATA
Receive Data
Indicates the first entry from the receive FIFO.
This register has the same functionality as that of Data (DATA).
77.6.15 MODEM Control (MCR)
Offset
Register
Offset
MCR
40h
Function
Controls the operation of the MODEM pins.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
LPUART_0
MCR
—
LPUART_1
MCR
—
LPUART_2
—
MCR
LPUART_3
—
MCR
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4650 / 5251


---
# 페이지 1791

Table continued from the previous page...
Instance
Register supported
Register not supported
LPUART_4
—
MCR
LPUART_5
—
MCR
LPUART_6
—
MCR
LPUART_7
—
MCR
LPUART_8
—
MCR
LPUART_9
—
MCR
LPUART_10
—
MCR
LPUART_11
—
MCR
LPUART_12
—
MCR
LPUART_13
—
MCR
LPUART_14
—
MCR
LPUART_15
—
MCR
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
RTS 
DTR 
0
DCD 
RIN 
DSR 
CTS 
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
31-10
—
Reserved
9
Request To Send
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4651 / 5251


---
# 페이지 1792

Table continued from the previous page...
Field
Function
RTS
Configures the default state of the RTS_B pin when the function is disabled.
0b - Logic one
1b - Logic zero
8
DTR
Data Terminal Ready
Configures the default state of the DTR_B pin.
0b - Logic one
1b - Logic zero
7-4
—
Reserved
3
DCD
Data Carrier Detect
Configures the interrupt, DCD_B, for change of state of the DCD_B pin.
0b - Disable interrupt
1b - Enable interrupt
2
RIN
Ring Indicator
Configures the interrupt, RIN_B, for change of state on the RIN_B pin.
0b - Disable interrupt
1b - Enable interrupt
1
DSR
Data Set Ready
Configures the interrupt, DSR_B, for change of state on the DSR_B pin.
0b - Disable interrupt
1b - Enable interrupt
0
CTS
Clear To Send
Configures the interrupt, CTS_B, for change of state on the CTS_B pin.
0b - Disable interrupt
1b - Enable interrupt
77.6.16 MODEM Status (MSR)
Offset
Register
Offset
MSR
44h
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4652 / 5251


---
# 페이지 1793

Function
Indicates the status of the MODEM pins.
 
You must appropriately configure the PAD connecting to DCD_B, RIN_B, DSR_B, and CTS_B inputs to get 
appropriate reset values for the MSR register fields.
  NOTE  
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
LPUART_0
MSR
—
LPUART_1
MSR
—
LPUART_2
—
MSR
LPUART_3
—
MSR
LPUART_4
—
MSR
LPUART_5
—
MSR
LPUART_6
—
MSR
LPUART_7
—
MSR
LPUART_8
—
MSR
LPUART_9
—
MSR
LPUART_10
—
MSR
LPUART_11
—
MSR
LPUART_12
—
MSR
LPUART_13
—
MSR
LPUART_14
—
MSR
LPUART_15
—
MSR
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4653 / 5251


---
# 페이지 1794

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
DCD 
RIN 
DSR 
CTS 
DDCD 
DRI 
DDSR 
DCTS 
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
31-8
—
Reserved
7
DCD
Data Carrier Detect
Indicates the state of the DCD_B pin.
0b - Logic one
1b - Logic zero
6
RIN
Ring Indicator
Indicates the state of the RIN_B pin.
0b - Logic one
1b - Logic zero
5
DSR
Data Set Ready
Indicates the state of the DSR_B pin.
0b - Logic one
1b - Logic zero
4
CTS
Clear To Send
Indicates the state of the CTS_B pin.
0b - Logic one
1b - Logic zero
3
DDCD
Delta Data Carrier Detect
Indicates whether the DCD_B pin changed state since the last time this field was 0.
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4654 / 5251


---
# 페이지 1795

Table continued from the previous page...
Field
Function
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Did not change state
1b - Changed state
When writing
0b - No effect
1b - Clear the flag
2
DRI
Delta Ring Indicator
Indicates whether the RIN_B pin changed state since the last time this field was 0.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Did not change state
1b - Changed state
When writing
0b - No effect
1b - Clear the flag
1
DDSR
Delta Data Set Ready
Indicates whether the DSR_B pin changed state since the last time this field was 0.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0b - Did not change state
1b - Changed state
When writing
0b - No effect
1b - Clear the flag
0
DCTS
Delta Clear To Send
Indicates whether the CTS_B pin changed state since the last time this field was 0.
 
This field behaves differently for register reads and writes.
  NOTE  
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4655 / 5251


---
# 페이지 1796

Table continued from the previous page...
Field
Function
When reading
0b - Did not change state
1b - Changed state
When writing
0b - No effect
1b - Clear the flag
77.6.17 Receiver Extended Idle (REIR)
Offset
Register
Offset
REIR
48h
Function
Configures the receiver extended idle functionality. You must not change this value when the receiver is enabled.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
LPUART_0
REIR
—
LPUART_1
REIR
—
LPUART_2
—
REIR
LPUART_3
—
REIR
LPUART_4
—
REIR
LPUART_5
—
REIR
LPUART_6
—
REIR
LPUART_7
—
REIR
LPUART_8
—
REIR
LPUART_9
—
REIR
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4656 / 5251


---
# 페이지 1797

Table continued from the previous page...
Instance
Register supported
Register not supported
LPUART_10
—
REIR
LPUART_11
—
REIR
LPUART_12
—
REIR
LPUART_13
—
REIR
LPUART_14
—
REIR
LPUART_15
—
REIR
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
IDTIME 
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
31-14
—
Reserved
13-0
IDTIME
Idle Time
Configures the idle length in number of bits (baud rate) since the end of the last stop bit. This affects 
the behavior of the idle wake-up, STAT[IDLE], DATA[IDLINE], and STAT[RAF]. The minimum supported 
extended idle time is equal to one idle character.
The extended idle feature is disabled when this field is 0.
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4657 / 5251


---
# 페이지 1798

77.6.18 Transmitter Extended Idle (TEIR)
Offset
Register
Offset
TEIR
4Ch
Function
Configures the transmitter extended idle functionality. You must not change this value when the transmitter is enabled.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
LPUART_0
TEIR
—
LPUART_1
TEIR
—
LPUART_2
—
TEIR
LPUART_3
—
TEIR
LPUART_4
—
TEIR
LPUART_5
—
TEIR
LPUART_6
—
TEIR
LPUART_7
—
TEIR
LPUART_8
—
TEIR
LPUART_9
—
TEIR
LPUART_10
—
TEIR
LPUART_11
—
TEIR
LPUART_12
—
TEIR
LPUART_13
—
TEIR
LPUART_14
—
TEIR
LPUART_15
—
TEIR
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4658 / 5251


---
# 페이지 1799

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
IDTIME 
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
31-14
—
Reserved
13-0
IDTIME
Idle Time
Configures the transmitter idle time in number of bits (baud rate) whenever an idle character is queued 
through the transmit FIFO. An idle character is not automatically queued whenever the transmitter is 
enabled. The minimum supported extended idle time equals one idle character.
The extended idle feature is disabled when this field is 0.
77.6.19 Half Duplex Control (HDCR)
Offset
Register
Offset
HDCR
50h
Function
Provides control for half-duplex-related operations.
You can use this register instead of CTRL[LOOPS], CTRL[RSRC], and CTRL[TXDIR] functions, although you can use 
CTRL[LOOPS] to loop-back the transmitter outputs to the receiver.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
LPUART_0
HDCR
—
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4659 / 5251


---
# 페이지 1800

Table continued from the previous page...
Instance
Register supported
Register not supported
LPUART_1
HDCR
—
LPUART_2
—
HDCR
LPUART_3
—
HDCR
LPUART_4
—
HDCR
LPUART_5
—
HDCR
LPUART_6
—
HDCR
LPUART_7
—
HDCR
LPUART_8
—
HDCR
LPUART_9
—
HDCR
LPUART_10
—
HDCR
LPUART_11
—
HDCR
LPUART_12
—
HDCR
LPUART_13
—
HDCR
LPUART_14
—
HDCR
LPUART_15
—
HDCR
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
RTSEXT 
0
RXMS
K 
RXWR
MSK 
RXSE
L 
TXSTA
LL 
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
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4660 / 5251


---
# 페이지 1801

Fields
Field
Function
31-16
—
Reserved
15-8
RTSEXT
RTS Extended
Specifies RTS extension. The transmit RTS_B remains asserted for (RTSEXT + 1) bit times after the end 
of the last stop bit. This applies even when the transmitter's RTS_B output is disabled and is only used 
internally to mask the receiver.
7-4
—
Reserved
3
RXMSK
Receive Mask
Specifies whether the transmitter RTS_B masks the receive data pin.
When enabled, the transmitter RTS_B masks the receive data pin.
0b - Do not mask
1b - Mask
2
RXWRMSK
Receive FIFO Write Mask
Specifies whether the transmitter RTS_B masks writes to the receive FIFO.
When enabled, the transmitter RTS_B masks receive FIFO writes, but the idle flag is not affected.
0b - Do not mask
1b - Mask
1
RXSEL
Receive Select
Specifies the receive data pin.
When enabled, the receive data is sourced from the TXD pin.
0b - RXD
1b - TXD
0
TXSTALL
Transmit Stall
Specifies whether the transmitter becomes busy when the receiver is active.
When enabled, the transmitter does not become busy or asserts transmitter RTS_B when the receiver is 
active (STAT[RAF] is 1).
0b - No effect
1b - Does not become busy
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4661 / 5251


---
# 페이지 1802

77.6.20 Timeout Control (TOCR)
Offset
Register
Offset
TOCR
58h
Function
Configures the behavior of the timeout logic. Timeouts 0 and 1 are used to monitor the receiver and timeouts 2 and 3 are used to 
monitor the transmitter.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
LPUART_0
TOCR
—
LPUART_1
TOCR
—
LPUART_2
—
TOCR
LPUART_3
—
TOCR
LPUART_4
—
TOCR
LPUART_5
—
TOCR
LPUART_6
—
TOCR
LPUART_7
—
TOCR
LPUART_8
—
TOCR
LPUART_9
—
TOCR
LPUART_10
—
TOCR
LPUART_11
—
TOCR
LPUART_12
—
TOCR
LPUART_13
—
TOCR
LPUART_14
—
TOCR
LPUART_15
—
TOCR
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4662 / 5251


---
# 페이지 1803

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
TOIE 
0
TOEN 
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
31-12
—
Reserved
11-8
TOIE
Timeout Interrupt Enable
Enables the corresponding timeout flag to generate an interrupt.
7-4
—
Reserved
3-0
TOEN
Timeout Enable
Enables the corresponding timeout counter.
77.6.21 Timeout Status (TOSR)
Offset
Register
Offset
TOSR
5Ch
Function
Indicates the status of the timeout logic. Timeouts 0 and 1 are used to monitor the receiver and timeouts 2 and 3 are used to 
monitor the transmitter.
 
Each module instance supports a different number of registers.
  NOTE  
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4663 / 5251


---
# 페이지 1804

Instance
Register supported
Register not supported
LPUART_0
TOSR
—
LPUART_1
TOSR
—
LPUART_2
—
TOSR
LPUART_3
—
TOSR
LPUART_4
—
TOSR
LPUART_5
—
TOSR
LPUART_6
—
TOSR
LPUART_7
—
TOSR
LPUART_8
—
TOSR
LPUART_9
—
TOSR
LPUART_10
—
TOSR
LPUART_11
—
TOSR
LPUART_12
—
TOSR
LPUART_13
—
TOSR
LPUART_14
—
TOSR
LPUART_15
—
TOSR
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
TOF 
0
TOZ 
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
1
1
1
1
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4664 / 5251


---
# 페이지 1805

Fields
Field
Function
31-12
—
Reserved
11-8
TOF
Timeout Flag
Indicates whether the corresponding timeout occurred. The timeout counter is disabled when this field is 
1.
 
This field behaves differently for register reads and writes.
  NOTE  
When reading
0000b - Not occurred
0001b - Occurred
When writing
0000b - No effect
0001b - Clear the flag
7-4
—
Reserved
3-0
TOZ
Timeout Zero
Indicates whether the corresponding timeout counter equals 0.
77.6.22 Timeout N (TIMEOUT0 - TIMEOUT3)
Offset
Register
Offset
TIMEOUT0
60h
TIMEOUT1
64h
TIMEOUT2
68h
TIMEOUT3
6Ch
Function
Configures the corresponding timeout counter and status field. Timeouts 0 and 1 are used to monitor the receiver and timeouts 
2 and 3 are used to monitor the transmitter. You must write to this register only when the corresponding timeout is disabled or 
when the value of the corresponding timeout field is 1.
 
Each module instance supports a different number of registers.
  NOTE  
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4665 / 5251


---
# 페이지 1806

Instance
Register supported
Register not supported
LPUART_0
TIMEOUT0–TIMEOUT3
—
LPUART_1
TIMEOUT0–TIMEOUT3
—
LPUART_2
—
TIMEOUT0–TIMEOUT3
LPUART_3
—
TIMEOUT0–TIMEOUT3
LPUART_4
—
TIMEOUT0–TIMEOUT3
LPUART_5
—
TIMEOUT0–TIMEOUT3
LPUART_6
—
TIMEOUT0–TIMEOUT3
LPUART_7
—
TIMEOUT0–TIMEOUT3
LPUART_8
—
TIMEOUT0–TIMEOUT3
LPUART_9
—
TIMEOUT0–TIMEOUT3
LPUART_10
—
TIMEOUT0–TIMEOUT3
LPUART_11
—
TIMEOUT0–TIMEOUT3
LPUART_12
—
TIMEOUT0–TIMEOUT3
LPUART_13
—
TIMEOUT0–TIMEOUT3
LPUART_14
—
TIMEOUT0–TIMEOUT3
LPUART_15
—
TIMEOUT0–TIMEOUT3
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
CFG 
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
TIMEOUT 
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
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4666 / 5251


---
# 페이지 1807

Fields
Field
Function
31-30
CFG
Idle Configuration
Configures the behavior of TIMEOUT[TIMEOUT].
00b - Becomes 1 after timeout characters are received
01b - Becomes 1 when idle for timeout bit clocks
10b - Becomes 1 when idle for timeout bit clocks following the next character
11b - Becomes 1 when idle for at least timeout bit clocks, but a new character is detected before 
the extended idle timeout is reached
29-14
—
Reserved
13-0
TIMEOUT
Timeout Value
Configures the timeout value.
77.6.23 Transmit Command Burst (TCBR0 - TCBR127)
Offset
For a = 0 to 127:
Register
Offset
TCBRa
200h + (a × 4h)
Function
Acts as an alias of Data (DATA), designed to support incrementing burst transfers to the transmit FIFO by a DMA controller, using 
aligned 8-bit, 16-bit, or 32-bit writes. The size of this register is 512 bytes:
• An aligned 32-bit write in this region pushes one entry into the transmit FIFO.
• An aligned 16-bit write in this region to TCBRx[15:0] pushes one entry into the transmit FIFO.
• An 8-bit write in this region to TCBRx[7:0] updates DATA[7:0], but does not push the data into the transmit FIFO.
• An 8-bit write in this region to TCBRx[15:8] pushes the data written to DATA[15:8] plus the previously written DATA[7:0] into 
the transmit FIFO.
• An 8-bit or 16-bit write in this region to TXBRx[31:16] is ignored.
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
LPUART_0
TCBR0–TCBR127
—
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4667 / 5251


---
# 페이지 1808

Table continued from the previous page...
Instance
Register supported
Register not supported
LPUART_1
TCBR0–TCBR127
—
LPUART_2
—
TCBR0–TCBR127
LPUART_3
—
TCBR0–TCBR127
LPUART_4
—
TCBR0–TCBR127
LPUART_5
—
TCBR0–TCBR127
LPUART_6
—
TCBR0–TCBR127
LPUART_7
—
TCBR0–TCBR127
LPUART_8
—
TCBR0–TCBR127
LPUART_9
—
TCBR0–TCBR127
LPUART_10
—
TCBR0–TCBR127
LPUART_11
—
TCBR0–TCBR127
LPUART_12
—
TCBR0–TCBR127
LPUART_13
—
TCBR0–TCBR127
LPUART_14
—
TCBR0–TCBR127
LPUART_15
—
TCBR0–TCBR127
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
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4668 / 5251


---
# 페이지 1809

Fields
Field
Function
31-16
—
Reserved
15-0
DATA
Data
Enables writing data to Data (DATA).
77.6.24 Transmit Data Burst (TDBR0 - TDBR255)
Offset
For a = 0 to 255:
Register
Offset
TDBRa
400h + (a × 4h)
Function
Acts as an alias of Data (DATA), designed to support incrementing burst transfers to the transmit FIFO by a DMA controller using 
8-bit, 16-bit, or 32-bit writes. The size of this register is 1024 bytes:
• An aligned 32-bit write in this region pushes four DATA byte entries into the transmit FIFO (DATA0 byte first). The register 
access is extended by three wait states.
• An aligned 16-bit write in this region to either half of a 32-bit word pushes two DATA byte entries into the transmit FIFO (DATA0 
or DATA2 first). The register access is extended by one wait state.
• An 8-bit write in this region pushes one DATA byte entry into the transmit FIFO.
Byte writes to Data (DATA) use the contents of CTRL[R9T8] for the ninth data bit, CTRL[R8T9] for the tenth data bit, and zero 
extend DATA[FRETSC].
 
Each module instance supports a different number of registers.
  NOTE  
Instance
Register supported
Register not supported
LPUART_0
TDBR0–TDBR255
—
LPUART_1
TDBR0–TDBR255
—
LPUART_2
—
TDBR0–TDBR255
LPUART_3
—
TDBR0–TDBR255
LPUART_4
—
TDBR0–TDBR255
LPUART_5
—
TDBR0–TDBR255
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4669 / 5251


---
# 페이지 1810

Table continued from the previous page...
Instance
Register supported
Register not supported
LPUART_6
—
TDBR0–TDBR255
LPUART_7
—
TDBR0–TDBR255
LPUART_8
—
TDBR0–TDBR255
LPUART_9
—
TDBR0–TDBR255
LPUART_10
—
TDBR0–TDBR255
LPUART_11
—
TDBR0–TDBR255
LPUART_12
—
TDBR0–TDBR255
LPUART_13
—
TDBR0–TDBR255
LPUART_14
—
TDBR0–TDBR255
LPUART_15
—
TDBR0–TDBR255
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
DATA3 
DATA2 
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
DATA1 
DATA0 
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
DATA3
Data3
Enables writing of data to Data (DATA).
23-16
DATA2
Data2
Enables writing of data to Data (DATA).
15-8
Data1
Table continues on the next page...
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4670 / 5251


---
# 페이지 1811

Table continued from the previous page...
Field
Function
DATA1
Enables writing of data to Data (DATA).
7-0
DATA0
Data0
Enables writing of data to Data (DATA).
77.7 Glossary
Baud rate
Number of bits per second that LPUART transmits or receives
Break character Break character is generated when the transmitter is holding the data line at the space level for at least one 
character time
Oversampling
Number of times the receive circuitry samples the receive input per baud period (that is, per data bit)
NXP Semiconductors
Low Power Universal Asynchronous Receiver/Transmitter (LPUART)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
4671 / 5251


---