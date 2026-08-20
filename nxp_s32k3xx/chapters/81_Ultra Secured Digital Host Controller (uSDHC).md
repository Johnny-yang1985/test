# 페이지 2180

Chapter 81
Ultra Secured Digital Host Controller (uSDHC)
81.1 Chip-specific uSDHC information
81.1.1 uSDHC instances and configuration
This chip supports up to one instance of uSDHC module.
Table 810. uSDHC instances
Instance
S32K358/S32K348/S32K338/S32K328
S32K310/S32K311/S32K312/S32K314/
S32K322/S32K324/S32K341/S32K342/S32K344/
S32K388/S32K389
uSDHC
Yes
No
Table 811. Features supported
Features
Notes
MMC
• System specification version 4.2/4.3/4.4/4.41
• Bit Widths x1/x4/x8
• Full Speed Mode upto 25MHz
• High Speed SDR upto 50MHz
• High Speed DDR mode (50MHz both edges)
SD/ SDIO
• Card Specification version 2.0/3.0
• Bit Widths x1/x4
• Full Speed Mode upto 25MHz
• High Speed Mode upto 50MHz
FIFO
128 x 32 external FIFO supported
External DMA
Supported
Write Protect WP system implementation
Supported
Voltage support
3.3 V
 
• uSDHC cannot directly write QSPI if flash page is not 512 bytes.
• Card clock pin should have weak pull down enabled when configured for uSDHC function.
  NOTE  
This chip doesn’t support the following features:
• MMC HS400 MODE
• Card Detection (CD) System Implementation
• LED control (LCTL) output signal
• IO power Voltage selection Signal (VSELECT)
• Input clock for eMMC HS400 mode (STROBE)
NXP Semiconductors
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5040 / 5251


---
# 페이지 2181

• DLL tuning is not supported in S32K358 since SDHC has 50 MHz frequency. Whereas, ideal tuning frequency requirement 
is 200 MHz.
Figure 536. System connection of uSDHC
81.1.2 Sequence for DLL implementation in SDR25 mode
To implement DLL in SDR25 mode the following steps need to be done without using CMD19 and CMD21:
1. Set TUNING_CTRL[STD_TUNING_EN] to 0.
2. Set MIX_CTRL[EXE_TUNE] to 0.
3. Set SYS_CTRL[RSTA] to reset all.
4. Set MIX_CTRL[SMP_CLK_SEL] to 1.
5. Set bit[14:0] of CLK Tuning Control and Status (CLK_TUNE_CTRL_STATUS) with the 32'h400. This needs to be configured 
as per the number of delay cells.
6. Poll bit[30:16] of CLK Tuning Control and Status (CLK_TUNE_CTRL_STATUS) until the value written in Step 5 above 
is read.
81.2 Overview
uSDHC provides the interface between the host system and the eMMC, SD card, and SDIO as shown in Figure 538. The module 
acts as a bridge, passing host bus transactions to the eMMC, SD card, and SDIO by sending commands and performing data 
accesses to/from the cards. It handles the SD card/SDIO/eMMC protocols at the transmission level.
81.2.1 Block diagram
The following figure illustrates the block diagram for uSDHC. Dual port SRAM is FIFO for write/read. For more information, see 
Data buffer.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5041 / 5251


---
# 페이지 2182

 
 
Clock divider
CMD
CLK
 
 
 
Interrupt
generator
AHB master port
DMA
Sync
buffer
controller
CRC
TX buffer
DLL
RX buffer
SD-CLK Control
IPS bus
IRQ
ipg_clk_perclk
Dual port
SRAM
Register
 bank
CMD 
channel
CTRL
Data channel
CTRL
CRC
Async FIFO
DATAn
CRC
hclk
ipg_clk
ipg_clk_lp
WP
 
RESET_B
MISC
Figure 537. uSDHC block diagram
The figure below shows the System connection of uSDHC:
eMMC/SD/SDIO
Host controller
DMA interface
IP bus
eMMC 
SD card
SDIO
IP bus
Power supply
AHB bus
Transceiver
Card
slot
Figure 538. System connection of uSDHC
The following are brief descriptions of the cards supported by uSDHC:
• The Embedded MultiMediaCard (eMMC) is a universal low-cost data storage and communication media designed to cover 
a wide array of applications including mobile video and gaming. Previous eMMC were based on a 7-pin serial bus with a 
single data pin, while the new high speed eMMC communication is based on an advanced 11-pin serial bus designed to 
operate in the low-voltage range.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5042 / 5251


---
# 페이지 2183

• The Secure Digital Card (SD) is an evolution of the old eMMC technology. It is specifically designed to meet the security, 
capacity, performance, and environmental requirements inherent in newly emerging audio and video consumer electronic 
devices. The physical form factor, pin assignment, and data transfer protocol are backward compatible with the old eMMC 
(with some additions).
• Under the SD protocol, system connection can be categorized into memory card, I/O card, and combo card, which have 
both memory and I/O functions. The memory card invokes a copyright protection mechanism that complies with the 
security of the SDMI (Secure Digital Music Initiative) standard. The I/O card, which is also known as SDIO, provides 
high-speed data I/O with low-power consumption for mobile electronic devices.
81.2.2 Features
The list given below shows the features of the uSDHC module:
• Conforms to the SD Host Controller Standard Specification version 2.0
• Compatible with the eMMC System Specification version 4.2/4.3/4.4/4.41
• Compatible with the SD Memory Card Specification version 3.0 and supports the Extended Capacity SD Memory Card
• Compatible with the SDIO Specification version 2.0
• Designed to work with SD Memory, miniSD Memory, SDIO, miniSDIO, SD Combo, eMMC, MMC plus, and MMC RS 
cards
• For card bus clock frequency: See the product Data Sheet for the clock frequency of each supported mode.
• Supports 1-bit/4-bit SD and SDIO modes, and 1-bit/4-bit/8-bit eMMC modes
— Up to 200 Mbps of data transfer for SDIO using four parallel data lines in the Single Data Rate (SDR) mode
— Up to 400 Mbps of data transfer for SDIO using four parallel data lines in the Dual Data Rate (DDR) mode
— Up to 200 Mbps of data transfer for SDXC cards using four parallel data lines in the Single Data Rate (SDR) mode
— Up to 400 Mbps of data transfer for SDXC card using four parallel data lines in the Dual Data Rate (DDR) mode
— Up to 416 Mbps of data transfer for eMMC using eight parallel data lines in the Single Data Rate (SDR) mode
— Up to 832 Mbps of data transfer for eMMC using eight parallel data lines in the Dual Data Rate (DDR) mode
• Supports single block/multi-block read and write
• Supports block sizes of 1 ~ 4096 bytes
• Supports the write protection switch for write operations
• Supports both synchronous and asynchronous abort
• Supports pause during the data transfer at block gap
• Supports SDIO Read Wait and Suspend Resume operations
• Supports Auto CMD12 for multi-block transfer
• Host can initiate non-data transfer command while data transfer is in progress
• Allows cards to interrupt the host in 1-bit and 4-bit SDIO modes; also supports interrupt period
• Embodies a fully configurable 128x32-bit FIFO for read/write data
• Supports internal and external DMA capabilities
• Supports voltage selection by configuring vendor-specific register bit
• Supports Advanced DMA to perform linked memory access
 
This block can support all the above-listed speed mode and maximum data throughput. However, these may be 
specific to the device. See the corresponding chip-specific information or the device data sheet for accurate details.
  NOTE  
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5043 / 5251


---
# 페이지 2184

81.3 Functional description
The following sections provide a brief functional description of the major system blocks, including the data buffer, DMA AHB 
interface, register bank as well as IP Bus interface, dual-port memory wrapper, data/command controller, clock and reset 
manager, and clock generator.
81.3.1 Modes and operations
81.3.1.1
Data transfer modes
The uSDHC module can select the following modes for data transfer:
• SD 1-bit
• SD 4-bit
• eMMC 1-bit
• eMMC 4-bit
• eMMC 8-bit
• Identification mode (up to 400 kHz)
• eMMC full-speed mode (up to 26 MHz)
• eMMC high-speed mode (up to 52 MHz)
• eMMC DDR mode (52 MHz both edges)
• SD card or SDIO full-speed mode (up to 25 MHz)
• SD card or SDIO high-speed mode (up to 50 MHz)
 
This block can support all the above listed speed mode and maximum clock frequency. However, these may be 
specific to the device. See the corresponding chip-specific information or the device data sheet for accurate details.
  NOTE  
81.3.2 Data buffer
The uSDHC module uses one configurable data buffer to transfer data between the system bus (IP bus or advanced 
high-performance bus (AHB) bus) and the SD card in an optimized manner, maximizing throughput between the two clock 
domains (IP peripheral clock and the master clock). The buffer is used as a temporary storage for transferring data between 
the host system and the card. The watermark levels for read and write are both configurable and can range between 1 to 
128 words. The burst lengths for read and write are also configurable and can range between 1 to 31 words. The next figure 
provides the uSDHC buffer scheme as buffer control and buffer RAM wrapper.
IP bus
I/F
AHB
bus
uSDHC registers
Buffer control
Internal
DMA
Buffer
RAM
wrapper
dma_req
uSDHC_irq
Status sync
TX/RX
FIFO
SD bus
I/F
Sync
FIFOs
Figure 539. uSDHC buffer scheme
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5044 / 5251


---
# 페이지 2185

Here are 3 transfer modes to access the data buffer:
• CPU polling mode:
— For a host-read operation, when the number of words received in the buffer meets or exceeds the RD_WML 
watermark value, by polling the BRR bit, the host driver can read the Buffer Data Port register to fetch the amount 
of words set in the RD_WML register from the buffer. The write operation is similar. For more information on the 
process of writing operation, see Write operation sequence.
• External DMA mode:
— For a read operation, when there are more words received in the buffer than the amount set in 
WTMK_LVL[RD_WML], a DMA request is sent out to inform the external DMA to fetch the data. The request will be 
immediately de-asserted when there is an access on the Data Buffer Access Port (DATA_BUFF_ACC_PORT). If the 
number of words in the buffer after the current burst meets or exceeds RD_WML value, the DMA request is asserted 
again. For instance, if there are twice as many words in the buffer as there are in the RD_WML value, there are 
two successive DMA requests with only one cycle of de-assertion between. The write operation is similar. Note the 
accesses CPU polling mode and external DMA mode both use the IP bus, and if the external DMA is enabled, in 
both modes an external DMA request is sent when the buffer is ready.
• Internal DMA mode (includes simple and advanced DMA accesses):
— The internal DMA access, either by simple or advanced DMA, is over the AHB bus. For internal DMA access mode, 
the external DMA request will never be sent out.
For a read operation, when there are more words in the buffer than the amount set in WTMK_LVL[RD_WML], the internal DMA 
starts fetching data over the AHB bus. Except for INCR4 and INCR8, the burst type is always the INCR mode and the burst length 
depends on the shortest of the following factors:
• Burst length configured in the burst length field of the Watermark Level register
• Watermark level boundary
• Block size boundary
• Data boundary configured in the current descriptor (if the ADMA is active)
• 1 KB address boundary defined in the AHB protocol
The Write operation functions in a similar manner—sequential and contiguous access is necessary to ensure that the pointer 
address value is correct. Random or skipped access is not possible. The byte order, by reset, is little endian mode. The actual 
byte order is swapped inside the buffer, according to the endian mode configured by software (see the following figures). For a 
host write operation, the byte order is swapped after the data is fetched from the buffer and ready to send to the SD Bus. For a 
host read operation, the byte order is swapped before the data is stored in the buffer.
31-24
23-16
15-8
7-0
System IP bus or system AHB bus
7-0
15-8
23-16
31-24
uSDHC data buffer
Figure 540. Data swap between system bus and uSDHC data buffer in the byte little endian mode
15-8
7-0
31-24
23-16
System IP bus or system AHB bus
7-0
15-8
23-16
31-24
uSDHC data buffer
Figure 541. Data swap between system bus and uSDHC data buffer in half word big endian mode
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5045 / 5251


---
# 페이지 2186

81.3.2.1
Write operation sequence
There are 3 ways to write data into the buffer when the user transfers data to the card:
• External DMA through the uSDHC DMA request signal
• Processor core polling through the BWR bit in the Interrupt Status register (interrupt or polling)
• Internal DMA
When the internal DMA is not used, the DMAEN bit in the Transfer Type register is not set when the command is sent, uSDHC 
asserts a DMA request when the amount of buffer space exceeds the value set in WTMK_LVL[WR_WML] and is ready for 
receiving new data. At the same time, uSDHC sets the BWR bit. The buffer write ready interrupt is generated if it is enabled 
by software.
When internal DMA is used, uSDHC does not inform the system before all the required number of bytes are transferred (if no error 
is encountered). When an error occurs during the data transfer, uSDHC aborts the data transfer and abandons the current block. 
The host driver should read the contents of the DMA System Address register to obtain the starting address of the abandoned data 
block. If the current data transfer is in multi-block mode, uSDHC does not automatically send CMD12, even though the AC12EN 
bit in the Transfer Type register is set. The host driver sends CMD12 in this scenario and restarts the write operation from that 
address. It is recommended that a software reset for Data be applied before the transfer is restarted.
The uSDHC module does not start data transmission until the buffer has been filled with the number of words set in the WR_WML 
register. If the buffer is empty and the host system does not write data in time, uSDHC stops the CLK to avoid the data buffer 
underrun situation.
81.3.2.2
Read operation sequence
There are 3 ways to read data from the buffer when the data is received from the card:
• External DMA through uSDHC DMA request signal
• Processor core polling through the BRR bit in the Interrupt Status register (interrupt or polling)
• Internal DMA
When internal DMA is not used (DMAEN bit in Transfer Type register is not set when the command is sent), uSDHC asserts a DMA 
request when the amount of data exceeds the value set in the RD_WML register, which is available and ready for system fetching 
data. At the same time, uSDHC sets the BRR bit. The buffer read ready interrupt is generated if it is enabled by the software.
When internal DMA is used, uSDHC does not inform the system before all the required number of bytes are transferred (if no error 
is encountered). When an error occurs during the data transfer, uSDHC aborts the data transfer and abandons the current block. 
The host driver should read the content of the DMA System Address register to get the starting address of the abandoned data 
block. If the current data transfer is in multi-block mode, uSDHC does not automatically send CMD12, even though the AC12EN 
bit in the Transfer Type register is set. The host driver sends CMD12 in this scenario and restarts the read operation from that 
address. It is recommended that a software reset (in register RSTD) for data be applied before the transfer is restarted.
For any read transfer mode, uSDHC does not start data transmission until the number of words set in the RD_WML register 
are in buffer. If the buffer is full and the host system does not read data in time, uSDHC stops the CLK to avoid the data buffer 
overrun situation.
81.3.2.3
Data buffer and block size
In the uSDHC module, the data buffer can hold up to 128 words (32-bit) and the watermark levels for write and read can be 
configured accordingly. The user needs to know the buffer size for the buffer operation during a data transfer to utilize it in the 
most optimized way. For both read and write, the watermark level can range between 1 to 128 words. For both read and write, 
the burst length can range between from 1 to 31 words. The host driver may configure the value according to the system and 
requirement.
During a multi-block data transfer, the block length can be set to any value between 1 and 4096 bytes, satisfying the requirements 
of the external card. The only restriction is from the external card, which can be limited in size or support of a partial block access 
(which is not the integer times of 512 bytes). That means, the largest block size is 512 bytes.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5046 / 5251


---
# 페이지 2187

As uSDHC treats each block individually, for block sizes which are not multiples of four (not word-aligned), stuffed bytes are 
required at the end of each block. For example, if the block size is 7 bytes and there are 12 blocks to write, the software side must 
write twice for each block. For each block, the ending byte is abandoned by uSDHC because it only sends 7 bytes to the card and 
picks data from the following system write, resulting in 24 beats of write access in total.
81.3.2.4
Dividing large data transfer
This SDIO command CMD53 definition limits the maximum data size of data transfers according to the following formula:
Max data size = Block size x Block count
The length of a multiple block transfer needs to be in multiples of block size. If the total data length cannot be divided evenly into a 
multiple of the block size, then there are two options to transfer the data. These two options depend on the function and the card 
design. Option 1 is for the host driver to split the transaction. The remainder of the block size data is then transferred by using a 
single block command at the end. Option 2 is to add dummy data in the last block to fill the block size. For option 2, the card must 
manage the removal of the dummy data. Only for write, uSDHC sends data to the card.
See Figure 542 for an example showing the division of large data transfers, assuming a kind of WLAN SDIO that only supports 
a block size of up to 64 bytes. Although uSDHC supports a block size of up to 4096 bytes, SDIO can only accept a block size of 
less than 64 bytes, so the data must be divided (see the example below).
802.11
MAC Header
IV
Frame Body
ICV
FCS
544 Bytes WLAN Frame
-----
Data
64 bytes
Data
64 bytes
Data
64 bytes
Data
32 bytes
-----
SDIO Data
block #1
SDIO Data
block #2
SDIO Data
block #8
SDIO Data
32 bytes
WLAN Frame is divided equally into 64 byte blocks plus the remainder 32 bytes
-----
SDIO Data
block #1
SDIO Data
block #2
SDIO Data
block #8
CMD 53
CMD 53
SDIO Data
32 bytes
Eight 64 byte blocks are sent in Block Transfer mode and the
remainder 32 bytes are sent in Byte Transfer mode
Figure 542. Example for dividing large data transfers
81.3.2.5
External DMA request
When the internal DMA is not in use and external DMA is enabled, the Data Buffer will generate a DMA request to the system. 
During a write operation, when the number of WR_WML words can be held in the buffer free space, the signal uSDHC_dreq_b is 
asserted to 0, informing the Host System of a DMA write.
The BWR bit in the Interrupt Status register is also set, as long as the BWRSEN bit in the Interrupt Status Enable register is set. The 
DMA request is de-asserted after several accesses to the Data Buffer Access Port (DATA_BUFF_ACC_PORT) are made while 
the buffer's free space can't meet the watermark condition (free space> write watermark level).
On read operation, when the number of RD_WML words are already in the buffer, the signal uSDHC_dreq_b is asserted to 0, 
informing the Host System for a DMA read. The BRR bit in the Interrupt Status register is also set, as long as the BRRSEN bit in 
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5047 / 5251


---
# 페이지 2188

the Interrupt Status Enable register is set. The DMA request is de-asserted after several accesses to the Data Port register are 
made while the buffer's data can't meet the watermark condition (the number of data in buffer > read watermark level).
If the DMA burst length can't change during a data transfer for an external DMA transfer, the watermark level (read or write) must 
be a divisor of the block size. If it is not, transferring the block may cause buffer under-run (read operation) or over-run (write 
operation). For example, if the block size is 512 bytes, the watermark level of read (or write) must be a power of two between 1 and 
128. For processor core polling access there is no such issue, as the last access in the block transfer can be controlled by software. 
The watermark level can be any value, even larger than the block size (but no greater than 128 words) because the actual number 
of bytes transferred by the software can be controlled and does not exceed the block size in each transfer.
The uSDHC also supports non-word aligned block size, as long as the card supports that block size. In this case, the watermark 
level should be set as the number of words. For example, if the block size is 31 bytes, the watermark level can be set to any number 
of words. For this case, the BLK_ATT[BLKSIZE] will be set as 1fh. For the CPU polling access, the burst length can be 1 to 128 
words, without restriction. This is because the software will transfer 8 words, and the uSDHC will also set the BWR or BRR bits 
when the remaining data does not violate data buffer. See DMA burst length for more details about the dynamic watermark level 
of the data buffer.
For the above example, even though 8 words are transferred via Data Buffer Access Port (DATA_BUFF_ACC_PORT), the uSDHC 
will transfer only 31 bytes over the SD Bus, as required by the BLK_ATT[BLKSIZE] fields. In this data transfer, with non-word 
aligned block size, the endian mode should be set cautiously or invalid data will be transferred to and from the card.
81.3.3 DMA AHB interface
The internal DMA implements a DMA engine and the AHB master. When the internal DMA is enabled, but the BWR and BRR 
bits are set if the BWRSEN and BRRSEN bits have been set in the Interrupt Status Enable register. See Figure 543 for an 
illustration of the DMA AHB interface block.
AHB
Interface
Master
Logic
DMA
Engine
uSDHC Registers
Buffer Control
System Address
R/W Indication
Error Indication
Burst Length
Data Exchange
AHB signal
cluster
DMA Request
Figure 543. DMA AHB interface block
81.3.3.1
Internal DMA request
If the watermark level requirement is met in data transfer or if the last data of current block is ready in the data buffer, and the 
Internal DMA is enabled, the data buffer block sends a DMA request to AHB interface. Meanwhile, the external DMA request signal 
(uSDHC_dreq_b) is disabled.
The delay in response from the internal DMA engine depends on the system AHB bus loading and the priority assigned to uSDHC. 
The DMA engine does not respond to the request during its burst transfer, but is ready to serve as soon as the burst is over. The 
data buffer de-asserts the request if the data buffer space (for write) or bytes in data buffer is smaller than the watermark level. 
Upon access to the buffer by internal DMA, the data buffer updates its internal buffer pointer, and when the watermark level is 
satisfied or the last data of the current block is ready in the data buffer, another DMA request is sent.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5048 / 5251


---
# 페이지 2189

The data transfer is in the block unit, and the subsequent watermark level is always automatically set as the remaining number of 
words. For instance, for a multi block data read with each block size of 31 bytes, and the burst length set to six words (24 bytes). 
After the first burst transfer, if there are greater than or equal to two words in the buffer, which might contain some data of the next 
block), another DMA request is sent. This is because the remaining number of words to transfer for the current block is ceiling((31 
- 6 * 4) / 4) = 2. The uSDHC module reads two words out of the buffer, with seven valid bytes and one stuffed byte.
81.3.3.2
DMA burst length
Just like a CPU polling access, the DMA burst length for the internal DMA engine can range between 1 to 16 words. The actual 
burst length for the DMA depends on the lesser of the configured burst length or the remaining words of the current block. See the 
example in Internal DMA request. After six words are read, the burst length is two words, then the next burst length is six words. 
This is because the next block starts, which is 31 bytes, more than six words. The host driver may take this variable burst length 
into account. It is also acceptable to configure the burst length as the divisor of the block size, so that each time the burst length 
is the same.
81.3.3.3
AHB master interface
It is possible that the internal AHB DMA engine could fail during the data transfer. Upon detection of an AHB bus error during 
DMA transfer, the DMA engine stops the transfer and goes to the idle state. At that point, the internal data buffer stops 
receiving incoming data and sending out data. The DMAE bit in the Interrupt Status register is generated to host CPU to report 
a bus error condition.
After the DMAE interrupt is received, the software sends a CMD12 to abort the current transfer and read the DS_ADDR bits of the 
DMA System Address register to get the starting address of the corrupted block. After the DMA error is fixed, the software should 
apply a data reset and restart the transfer from this address to recover the corrupted block.
81.3.3.4
ADMA engine
In the SD host controller standard, a new DMA transfer algorithm called the Advanced DMA (ADMA) is defined. For simple 
DMA, after the page boundary is reached, a DMA interrupt is generated and the new system address is programmed by the 
host driver. The ADMA defines the programmable descriptor table in the system memory. The host driver can calculate the 
system address at the page boundary and program the descriptor table before executing ADMA. It reduces the frequency of 
interrupts to the host system. Therefore, higher speed DMA transfers could be realized because the host MCU intervention is 
not be needed during long DMA-based data transfers.
There are two types of ADMA in host controller: ADMA1 and ADMA2. ADMA1 can support data transfer of 4KB aligned data in 
system memory, and ADMA2 eliminates the restriction so that the data of any location and any size can be transferred in system 
memory. Their formats of Descriptor Table are different.
ADMA can recognize all kinds of descriptors defined in SD host controller Standard, and if the "End" flag is detected in the 
descriptor, ADMA stops after this descriptor is processed.
81.3.3.4.1
ADMA concept and descriptor format
ADMA1 includes the following descriptors:
• Valid/invalid descriptor
• Nop descriptor
• Set data length descriptor
• Set data address descriptor
• Link descriptor
• Interrupt flag and end flag in descriptor
ADMA2 includes the following descriptors:
• Valid/invalid descriptor
• Nop descriptor
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5049 / 5251


---
# 페이지 2190

• Rsv descriptor (new in ADMA2)
• Set data length and address descriptor
• Link descriptor
• Interrupt flag and end flag in descriptor
ADMA starts read/write operation after it reaches the tran state, using the data length and data address analyzed from most 
recent descriptor(s).
For ADMA1, the valid data length descriptor is the last set type descriptor before the tran type descriptor. Every tran type descriptor 
triggers a transfer, and the transfer data length is extracted from the most recent set type descriptor. If there is no set type 
descriptor after the previous Trans descriptor, the data length is the value for previous transfer, or 0 if no set descriptor is ever met.
For ADMA2, the tran type descriptor contains both data length and transfer data address, so the tran type descriptor itself can start 
a data transfer.
See Figure 544 for the format of the descriptor table for ADMA1.
       
Address/ Page Field     
       
Address/ Page Field     
       
Attribute Field     
       
0     
       
1     
       
2     
       
3     
       
4     
       
5     
       
6     
       
11     
       
12     
       
31     
       
Address or Data Length     
       
000000     
       
Act 2     
       
Act 1     
       
0     
       
Int     
       
End     
       
Valid     
       
Act 2     
       
Act1     
       
Symbol     
       
Comment     
       
31- 28     
       
27- 12     
       
0     
       
0     
       
1     
       
1     
       
0     
       
1     
       
0     
       
1     
       
Nop     
       
Set     
       
Tran     
       
Link     
       
No Operation     
       
Set Data Length     
       
Transfer Data     
       
Link Descriptor     
       
Don't Care     
       
Data Address     
       
0000     
       
Data Length     
       
Descriptor Address     
       
Valid     
       
End     
       
Int     
       
Valid = 1 indicates this line of descriptor is effective. If Valid = 0 generate ADMA Error Interrupt and stop ADMA.     
       
End = 1 indicates current descriptor is the ending one.     
       
Int = 1 generates DMA Interrupt when this descriptor is processed.     
Figure 544. Format of the ADMA1 descriptor table
See Figure 545 for the concept and access method of the descriptor table for ADMA1.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5050 / 5251


---
# 페이지 2191

System Address Register
Data Length (internal)
Data Address (internal)
SDMA
Flags
State
Machine
Address/Length
Attribute
Address
Tran
Address
Link
Address/Length
Attribute
Data Length
Set
Address
Tran, End
Descriptor Table
Page Data
Page Data
DMA Interrupt
Transfer Complete
Block Gap Event
System Memory
Advanced DMA
System Address Register points to 
the head node of Descriptor Table
Figure 545. Concept and access method of the ADMA1 descriptor table
The figure below explains the ADMA2 format. ADMA2 deals with the lower 32-bit first, and then the higher 32-bit. If the 'Valid' flag 
of descriptor is 0, it ignores the higher 32-bit. The Address field should be set to word aligned (lower 2-bit is always set to 0). Data 
length is in byte unit.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5051 / 5251


---
# 페이지 2192

       
Address Field     
       
Length     
       
Attribute Field     
       
00     
       
01     
       
02     
       
03     
       
04     
       
05     
       
06     
       
31     
       
32     
       
63     
       
32-bit Address     
       
Act 2     
       
Act 1     
       
0     
       
Int     
       
End     
       
Valid     
       
Act 2     
       
Act1     
       
Symbol     
       
Comment     
       
Operation     
       
0     
       
0     
       
1     
       
1     
       
0     
       
1     
       
0     
       
1     
       
Nop     
       
Rsv     
       
Tran     
       
Link     
       
No Operation     
       
Reserved     
       
Transfer Data     
       
Link Descriptor     
       
Don't Care     
       
Transfer data with address and length 
       
set in this descriptor line     
       
Same as Nop. Read this line and go to next one     
       
Link to another descriptor     
       
Valid     
       
End     
       
Int     
       
Valid = 1 indicates this line of descriptor is effective. If Valid = 0 generate ADMA Error Interrupt and stop ADMA.     
       
End = 1 indicates current descriptor is the ending one.     
       
Int = 1 generates DMA Interrupt when this descriptor is processed.     
            
       
Reserved     
       
16            
15     
       
16-bit length     
       
0000000000     
Figure 546. Format of the ADMA2 descriptor table
See Figure 547 for the concept and access method of the descriptor table for ADMA2.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5052 / 5251


---
# 페이지 2193

System Address Register
Data Length (internal)
Data Address (internal)
SDMA
Flags
State
Machine
Address
Address1
Address2
Descriptor Table
Data 4
DMA Interrupt
Transfer Complete
ADMA Error
System Memory
Advanced DMA
System Address Register points to 
the head node of Descriptor Table
Length
Attribute
Length1
Tran
Length2
Address
Address3
Attribute
Tran
Address
Link
-
Length
Length3
Address4
Tran, End
Length4
Tran
Data 3
Data 2
Data 1
Figure 547. Concept and access method of the ADMA2 descriptor table
81.3.3.4.2
ADMA interrupt
If the interrupt flag descriptor is set, ADMA generates an interrupt according to various types of descriptors.
For ADMA1:
• Set type of descriptor: interrupt is generated when data length is set.
• Tran type descriptor: interrupt is generated when this transfer is complete.
• Link type of descriptor: interrupt is generated when new descriptor address is set.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5053 / 5251


---
# 페이지 2194

• Nop type of descriptor: interrupt is generated just after this descriptor is fetched.
For ADMA2:
• Tran type of descriptor: interrupt is generated when this transfer is complete.
• Link type of descriptor: interrupt is generated when new descriptor address is set.
• Nop/Rsv type of descriptor: interrupt is generated just after this descriptor is fetched.
81.3.3.4.3
ADMA error
The ADMA stops whenever an error is encountered. These errors include:
• Fetching descriptor error
• AHB response error
• Data length mismatch error
An ADMA descriptor error is generated when it fails to detect a "valid" flag in the descriptor. If an ADMA descriptor error occurs, 
the interrupt is not generated even if the "Interrupt" flag of this descriptor is set.
When BLKCNTEN bit is set, data length set in register BLK_ATT must be equal to the whole data length set in descriptor, otherwise 
data length mismatch error is generated.
When BLKCNTEN bit is not set, then the whole data length set in descriptor is a multiple of block lengths; otherwise, when data 
set in the descriptor nodes are not performed at block boundaries, then data mismatch errors occur.
81.3.4 Register bank with IP bus interface
Register accesses through the IP bus interface are on the register bank. See Figure 548 for the block diagram.
Register Bank
IP Bus
Signals
Software
Visible
Registers
Write 1 Clear
Function
Array
Data Port
Buffer Control
Synchronizer
Control/ Status
Signals
with other domains
Control/ Status
Signals
Status Signals
from other modules
Control Signals
to other modules
Figure 548. Register bank diagram
Only a 32-bit access is allowed, and no partial read/write is supported; therefore, all accesses are word aligned.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5054 / 5251


---
# 페이지 2195

Access to an unimplemented address within the register memory map space does not generate a transfer error.
81.3.4.1
SD protocol unit
The SD protocol unit deals with all SD protocol affairs.
The SD protocol unit performs the following functions:
• Acts as the bridge between the internal buffer and the SD bus
• Sends the command data as well as its argument serially
• Stores the serial response bit stream into corresponding registers
• Detects the bus state on the CMD/DAT lines
• Monitors the interrupt from SDIO
• Asserts the read wait signal
• Gates off the SD clock when buffer is announcing danger status
• Detects the write protect state
The SD protocol unit consists of four sub-modules:
• SD control misc
• Command control
• Data control
• Clock control
81.3.4.2
SD control miscellaneous
In the SD control miscellaneous unit:
• The card detection (including DATA3 for card detection) and card interrupt are implemented.
• The module monitors the signal level on all the eight data lines and the command lines. It directly routes the level values 
into the register bank.
• The module also detects the Write Protect (WP) line. If WP is active, writes to memory and combo cards are ignored.
81.3.4.3
SD clock control
If the internal data buffer is near full (for read) or near empty (for write), the SD clock must be gated off to avoid buffer 
over/under-run. This module asserts the gate of the output SD clock to shut the clock off. After the buffer has space (for read) or 
has data (for write), the clock gate of this module opens, and the SD clock is active again.
81.3.4.4
Command control
The Command Control module deals with the transactions on the CMD line. 
See Figure 549 for an illustration of the structure for the Command CRC shift register.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5055 / 5251


---
# 페이지 2196

       
CLR_CRC     
       
ZERO     
       
CRC_IN     
       
CRC OUT     
       
CRC
       
Bus [0]     
       
CRC
       
Bus [1]     
       
CRC
       
Bus [2]     
       
CRC
       
Bus [3]     
       
CRC
       
Bus [4]     
       
CRC
       
Bus [5]     
       
CRC
       
Bus [6]     
Figure 549. Command CRC shift register
The CRC polynomials for the CMD are as follows:
Generator polynomial: G(x) = x7 + x3 + 1
M(x) = (first bit) * xn + (second bit) * xn-1 +...+ (last bit) * x0
CRC[6:0] = Remainder [(M(x) * x7) / G(x)]
81.3.4.5
Data control
The data agent deals with the transactions on the eight data lines. Moreover, this module also detects the busy state on the 
DATA0 line and generates the read wait state by the request from the transceiver. 
The CRC polynomials for the data are as follows:
Generator polynomial: G(x) = x16 + x12 + x5 +1
M(x) = (first bit) * xn + (second bit) * xn-1 +...+ (last bit) * x0
CRC[15:0] = Remainder [(M(x) * x16) / G(x)]
81.3.5 Card insertion and removal detection
The uSDHC module uses the DATA3 pin to detect card insertion or removal. It is controlled by SoC pad or other logic. When there 
is no card on the eMMC/SD bus, the DATA3 is pulled to a low voltage level by default.
When any card is inserted to or removed from the socket, uSDHC detects the logic value changes on the DATA3 pin and generates 
an interrupt.
81.3.6 Power management and wakeup events
When there is no operation between uSDHC and the card through the SD bus, the user can completely disable the peripheral clock 
and base clock in the chip-level clock control module to save power. When the user needs to use uSDHC to communicate with 
the card, it can enable the clock and start the operation.
In some circumstances, when the clocks to uSDHC are disabled, for instance, when the system is in low-power mode, there are 
some events for which the user needs to enable the clock and handle the event. These events are called wakeup interrupts. The 
uSDHC module can generate these interrupts even when there are no clocks enabled. The three interrupts that can be used as 
wakeup events are these:
• Card removal interrupt
• Card insertion interrupt
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5056 / 5251


---
# 페이지 2197

• Interrupt from SDIO (not available in multiple block data transfers)
These three wakeup events (or wakeup interrupts) can also be used to wakeup the system from low-power modes.
 
To make the interrupt a wakeup event, when all the clocks to uSDHC are disabled or when the entire system is in 
low power mode, the corresponding wakeup enabled bit needs to be set. Refer to Protocol Control (PROT_CTRL) 
for more information on the uSDHC Protocol Control register.
  NOTE  
81.3.6.1
Setting wakeup events
For uSDHC to respond to a wakeup event, the software must set the respective wakeup enable bit before the CPU enters the 
sleep mode. Before the software disables the host clock, it should ensure that all the following conditions have been met:
• No read or write transfer is active
• Data and command lines are not active
• No interrupts are pending
• Internal data buffer is empty
81.3.7 eMMC fast boot
The Embedded MultiMediaCard (eMMC4.3 or later) specification adds a fast boot feature that requires hardware support. There 
are two types of fast boot modes in the eMMC4.3 or later specification: boot operation and alternative boot operation. Each type 
also has with-acknowledge and without-acknowledge modes.
In the boot operation mode, the master (eMultiMediaCard host) can read boot data from the slave (eMMC device) by keeping CMD 
line low after power-on, or sending CMD0 with argument + 0xFFFFFFFA (optional for slave), before issuing CMD1.
 
For the eMMC4.3 setting, please see the eMMC4.3 specification.
  NOTE  
81.3.7.1
Boot operation
If the CMD line is held low for 74 clock cycles and more after power-up before the first command is issued, the slave recognizes 
that boot mode is being initiated and starts preparing boot data internally.
Within one second after the CMD line goes low, the slave starts to send the first boot data to the master on the DATA line(s). The 
master must keep the CMD line low to read all of the boot data.
 
For the purposes of this documentation, fast boot is called "normal fast boot mode".
  NOTE  
If boot acknowledge is enabled, the slave has to send acknowledge pattern '010' to the master within 50ms after the CMD line 
goes low. If boot acknowledge is disabled, the slave does not send out acknowledge pattern '010'.
The master can terminate the boot mode with the CMD line high.
The boot operation is terminated when all the contents of the enabled boot data are sent to the master. After the boot operation 
is executed, the slave gets ready for the CMD1 operation and the master needs to start a normal eMMC initialization sequence 
by sending CMD1.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5057 / 5251


---
# 페이지 2198

512 bytes
+CRC
CMD1
RESP
CMD2
RESP
CMD3
RESP
E
Boot terminated
S
512 bytes
+CRC
E
S
010
50 ms max
1 sec. max
E
S
DATA0
CMD
CLK
Min 8 clocks + 48 clocks =56 clocks required from CMD signal high to next eMMC command
Figure 550. Embedded MultiMediaCard state diagram (normal boot mode)
81.3.7.2
Alternative boot operation
This boot function is optional for the device. If bit 0 in the extended CSD byte[228] is set to '1', the device supports the 
alternative boot operation.
After power-up, if the host issues CMD0 with the argument of 0xFFFFFFFA after 74 clock cycles, before CMD1 is issued or the 
CMD line goes low, the slave recognizes that boot mode is being initiated and starts preparing boot data internally.
Within one second after CMD0 with the argument of 0xFFFFFFFA is issued, the slave starts to send the first boot data to the 
master on the DATA line(s).
If boot acknowledge is enabled, the slave must send the acknowledge pattern '010' to the master within 50ms after the CMD0 with 
the argument of 0xFFFFFFFA is received. If boot acknowledge is disabled, the slave does not send out acknowledge pattern '010'.
The master can terminate the boot mode by issuing CMD0 (Reset).
Boot operation is terminated when all the contents of the enabled boot data are sent to the master. After the boot operation is 
executed, the slave gets ready for the CMD1 operation and the master needs to start a normal eMMC initialization sequence by 
sending CMD1.
512 BYTES
+CRC
CMD0/Reset
CMD0 1
CMD1
RESP
CMD2
RESP
CMD3
RESP
E
S
512 BYTES
+CRC
E
S
010
NOTE 1: CMD0 with argument 0xFFFFFFFA
50 ms
max
1 sec. max
E
S
DATA0
Min 74 clocks
required after
power is stable
to start boot
command.
CMD
CLK
Figure 551. Embedded MultiMediaCard state diagram (alternative boot mode)
81.3.8 Commands for SD card, SDIO, and eMMC
A table containing the list of commands for the eMMC/SD card/SDIO is provided here.
Refer to the corresponding specifications for more details about the command information.
There are four kinds of commands defined to control the SD card, SDIO, and eMMC:
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5058 / 5251


---
# 페이지 2199

• Broadcast commands (bc), no response
• Broadcast commands with response (bcr), response from all cards simultaneously
• Addressed (point-to-point) commands (ac), no data transfer on the DATA
• Addressed (point-to-point) data transfer commands (adtc)
Response: A response is a token that is sent from the card to the host as an answer to a previously received command. A response 
is transferred serially on the CMD line.
Table 812. Commands for eMMC/SD card/SDIO
CMD INDEX
Type
Argument
Response 
type
Abbreviation
Description
CMD0
bc
[31:0] stuff bits
-
GO_IDLE_STATE
Resets all eMMC and SD memory 
cards to idle state.
CMD1
bcr
[31:0] OCR 
without busy
R3
SEND_OP_COND
Asks all eMMC and SD Memory 
cards in idle state to send 
their operation conditions register 
contents in the response on the 
CMD line.
CMD2
bcr
[31:0] stuff bits
R2
ALL_SEND_CID
Asks all cards to send their CID 
numbers on the CMD line.
CMD31
ac
[31:6] RCA
[15:0] stuff bits
R1
R6 (SDIO)
SET/
SEND_RELATIVE_AD
DR
Assigns relative address to 
the card.
CMD4
bc
[31:0] DSR
[15:0] stuff bits
-
SET_DSR
Programs the DSR of all cards.
CMD5
bc
[31:0] OCR 
without busy
R4
IO_SEND_OP_COND
Asks all SDIO in idle state to send 
them operation conditions register 
contents in the response on the 
CMD line.
CMD62
adtc
[31] Mode
0: Check function
1: Switch function 
[30:8] Reserved for 
function groups 6 ~ 3 
(All 0 or 0xFFFF)
[7:4] Function group1 
for command system
[3:0] Function group2 
for access mode
R1
SWITCH_FUNC
Checks switch ability (mode 0) and 
switch card function (mode 1). Refer 
to "SD Physical Specification V1.1" 
for more details.
CMD63
ac
[31:26] Set to 0
[25:24] Access
R1b
SWITCH
Switches the mode of operation of 
the selected card or modifies the 
EXT_CSD registers. Refer to "The 
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5059 / 5251


---
# 페이지 2200

Table 812. Commands for eMMC/SD card/SDIO (continued)
CMD INDEX
Type
Argument
Response 
type
Abbreviation
Description
[23:16] Index
[15:8] Value
[7:3] Set to 0
[2:0] Cmd Set
Embedded MultiMediaCard System 
Specification Version 4.0 Final draft 
2" for more details.
CMD7
ac
[31:6] RCA
[15:0] stuff bits
R1b
SELECT/
DESELECT_CARD
Toggles a card between the stand-
by and transfer states or between 
the programming and disconnect 
states. In both cases, the card is 
selected by its own relative address 
and gets deselected by any other 
address. Address 0 deselects all.
CMD8
adtc
[31:0] stuff bits
R1
SEND_EXT_CSD
The card sends its EXT_CSD 
register as a block of data, with a 
block size of 512 bytes.
CMD9
ac
[31:6] RCA
[15:0] stuff bits
R2
SEND_CSD
Addressed card sends its card-
specific data (CSD) on the 
CMD line.
CMD10
ac
[31:6] RCA
[15:0] stuff bits
R2
SEND_CID
Addressed card sends its card-
identification (CID) on the CMD line.
CMD11
adtc
[31:0] data address
R1
READ_DAT_UNTIL_S
TOP
Reads data stream from the card, 
starting at the given address, until a 
STOP_TRANSMISSION follows.
CMD12
ac
[31:0] stuff bits
R1b
STOP_TRANSMISSIO
N
Forces the card to 
stop transmission.
CMD13
ac
[31:6] RCA
[15:0] stuff bits
R1
SEND_STATUS
Addressed card sends its 
status register.
CMD14
Reserved
CMD15
ac
[31:6] RCA
[15:0] stuff bits
-
GO_INACTIVE_STAT
E
Sets the card to inactive 
state in order to protect 
the card stack against 
communication breakdowns.
CMD16
ac
[31:0] block length
R1
SET_BLOCKLEN
Sets the block length (in bytes) for 
all following block commands (read 
and write). Default block length is 
specified in the CSD.
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5060 / 5251


---
# 페이지 2201

Table 812. Commands for eMMC/SD card/SDIO (continued)
CMD INDEX
Type
Argument
Response 
type
Abbreviation
Description
CMD17
adtc
[31:0] data address
R1
READ_SINGLE_BLO
CK
Reads a block of the size selected 
by the SET_BLOCKLEN command.
CMD18
adtc
[31:0] data address
R1
READ_MULTIPLE_BL
OCK
Continuously transfers data blocks 
from card to host until interrupted by 
a stop command.
CMD19
Reserved
CMD20
adtc
[31:0] data address
R1
WRITE_DAT_UNTIL_
STOP
Writes data stream from the host, 
starting at the given address, until a 
STOP_TRANSMISION follows.
CMD21
Reserved
CMD22
Reserved
CMD23
ac
[31] reliable 
write request
[30:16] set to 0
[15:0] number 
of blocks
R1
SET_BLOCK_COUNT
Defines the number of blocks 
(read/write) and the reliable writer 
parameter (write) for a block read or 
write command.
CMD24
adtc
[31:0] data address
R1
WRITE_BLOCK
Writes a block of the size selected 
by the SET_BLOCKLEN command.
CMD25
adtc
[31:0] data address
R1
WRITE_MULTIPLE_B
LOCK
Continuously writes blocks 
of data until a 
STOP_TRANSMISSION follows.
CMD26
adtc
[31:0] stuff bits
R1
PROGRAM_CID
Programming of the card 
identification register. This 
command is issued only once per 
card. The card contains hardware 
to prevent this operation after 
the first programming. Normally 
this command is reserved for 
the manufacturer.
CMD27
adtc
[31:0] stuff bits
R1
PROGRAM_CSD
Programming of the programmable 
bits of the CSD.
CMD28
ac
[31:0] data address
R1b
SET_WRITE_PROT
If the card has write protection 
features, this command sets the 
write protection bit of the addressed 
group. The properties of write 
protection are coded in the card 
specific data (WP_GRP_SIZE).
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5061 / 5251


---
# 페이지 2202

Table 812. Commands for eMMC/SD card/SDIO (continued)
CMD INDEX
Type
Argument
Response 
type
Abbreviation
Description
CMD29
ac
[31:0] data address
R1b
CLR_WRITE_PROT
If the card provides write protection 
features, this command clears 
the write protection bit of the 
addressed group.
CMD30
adtc
[31:0] write protect 
data address
R1
SEND_WRITE_PROT
If the card provides write protection 
features, this command asks the 
card to send the status of the write 
protection bits.
CMD31
Reserved
CMD32
ac
[31:0] data address
R1
TAG_SECTOR_STAR
T
Sets the address of the first sector 
of the erase group.
CMD33
ac
[31:0] data address
R1
TAG_SECTOR_END
Sets the address of the last sector 
in a continuous range within the 
selection of a single sector to be 
selected for erase.
CMD34
ac
[31:0] data address
R1
UNTAG_SECTOR
Removes one previously selected 
sector from the erase selection.
CMD35
ac
[31:0] data address
R1
TAG_ERASE_GROUP
_START
Sets the address of the first erase 
group within a range to be selected 
for erase.
CMD36
ac
[31:0] data address
R1
TAG_ERASE_GROUP
_END
Sets the address of the last erase 
group within a continuous range to 
be selected for erase.
CMD37
ac
[31:0] data address
R1
UNTAG_ERASE_GR
OUP
Removes one previously 
selected erase group from the 
erase selection.
CMD38
ac
[31:0] stuff bits
R1b
ERASE
Erase all previously 
selected sectors.
CMD39
ac
[31:0] RCA
[15] register write flag
[14:8] 
register address
[7:0] register data
R4
FAST_IO
Used to write and read 8-bit 
(register) data fields. The command 
addresses a card, and a register, 
and provides the data for writing 
if the write flag is set. The R4 
response contains data read from 
the address register. This command 
accesses application dependent 
registers which are not defined in 
the eMMC standard.
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5062 / 5251


---
# 페이지 2203

Table 812. Commands for eMMC/SD card/SDIO (continued)
CMD INDEX
Type
Argument
Response 
type
Abbreviation
Description
CMD40
bcr
[31:0] stuff bits
R5
GO_IRQ_STATE
Sets the system into interrupt mode.
CMD41
Reserved
CDM42
adtc
[31:0] stuff bits
R1b
LOCK_UNLOCK
Used to set/reset the password 
or lock/unlock the card. The size 
of the data block is set by the 
SET_BLOCK_LEN command.
CMD43~51
Reserved
CMD52
ac
[31:0] stuff bits
R5
IO_RW_DIRECT
Access a single register within the 
total 128k of register space in any 
I/O function.
CMD53
ac
[31:0] stuff bits
R5
IO_RW_EXTENDED
Accesses a multiple I/O register 
with a single command. Allows the 
reading or writing of a large number 
of I/O registers.
CMD54
Reserved
CMD55
ac
[31:16] RCA
[15:0] stuff bits
R1
APP_CMD
Indicates to the card that the 
next command is an application 
specific command rather than a 
standard command.
CMD56
adtc
[31:1] stuff bits
[0]: RD/WR
R1b
GEN_CMD
Used either to transfer a data block 
to the card or to get a data block 
from the card for general purpose / 
application specific commands. The 
size of the data block is set by the 
SET_BLOCK_LEN command.
CMD57-59
Reserved
CMD60
adtc
[31] WR
[30:24] stuff bits
[23:16] address
[15:8] stuff bits
[7:0] byte count
R1b
RW_MULTIPLE_REGI
STER
These registers are used to 
control the behavior of the device 
and to retrieve status information 
regarding the operation of the 
device. All Status and Control 
registers are WORD (32-bit) in 
size and are WORD aligned. 
CMD60 is used to read and write 
these registers.
CMD61
adtc
[31] WR
[30:16] stuff bits
R1b
RW_MULTIPLE_BLO
CK
The host issues a 
RW_MULTIPLE_BLOCK (CMD61) 
to begin the data transfer.
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5063 / 5251


---
# 페이지 2204

Table 812. Commands for eMMC/SD card/SDIO (continued)
CMD INDEX
Type
Argument
Response 
type
Abbreviation
Description
[15:0] data unit count
CMD62-63
Reserved
ACMD64
ac
[31:2] stuff bits
[1:0] bus width
R1
SET_BUS_WIDTH
Defines the data bus width 
('00'=1bit or '10'=4bit bus) to be 
used for data transfer. The allowed 
data bus widths are given in 
SCR register.
ACMD134
adtc
[31:0] stuff bits
R1
SD_STATUS
Send the SD Memory Card status.
ACMD224
adtc
[31:0] stuff bits
R1
SEND_NUM_WR_SE
CTORS
Send the number of the written 
sectors (without errors). Responds 
with 32-bit plus the CRC data block.
ACMD234
ac
[31:23] stuff bits
[22:0] Number 
of blocks
R1
SET_WR_BLK_ERAS
E_COUNT
Set the number of write blocks to 
be pre-erased before writing (to 
be used for fast Multiple Block 
WR command). "1"=default(one 
write block).
ACMD414
bcr
[31:0] OCR
R3
SD_APP_OP_COND
Asks the accessed card to send its 
operating condition register (OCR) 
contents in the response on the 
CMD line.
ACMD424
ac
[31:1] stuff bits
[0] set_cd
R1
SET_CLR_CARD_DE
TECT
Connect(1)/Disconnect(0) the 
50KOhm pull-up resistor on DATA3 
of the card.
ACMD514
adtc
[31:0] stuff bits
R1
SEND_SCR
Reads the SD Configuration 
Register (SCR).
1. CMD3 differs for eMMC and SD cards. For eMMC, it is referred to as SET_RELATIVE_ADDR, with a response type of R1. 
For SD cards, it is referred to as SEND_RELATIVE_ADDR, with a response type of R6 (with RCA inside).
2. CMD6 differs completely between high speed eMMC and high-speed SD cards. Command SWITCH_FUNC is for high-
speed SD cards.
3. Command SWITCH is for high speed eMMC. The Index field can contain any value from 0-255, but only values 0-191 are 
valid. If the Index value is in the 192-255 range the card does not perform any modification and the SWITCH_ERROR 
status bit in the EXT_CSD register is set. The Access Bits are shown in Table 813.
4. ACMDs is preceded with the APP_CMD command. Commands listed are used for SD only, other SD commands not listed 
are not supported on this module.
The access bits for the EXT_CSD access modes are listed in the following table.
Table 813. EXT_CSD access modes
Bits
Access name
Operation
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5064 / 5251


---
# 페이지 2205

Table 813. EXT_CSD access modes (continued)
00
Command set
The command set is changed according to the Cmd Set field of the argument.
01
Set bits
The bits in the pointed byte are set, according to the bits set to 1 in the Value field.
10
Clear bits
The bits in the pointed byte are cleared, according to the bits set to 1 in the Value field.
11
Write byte
The Value field is written into the pointed byte.
81.3.9 SDIO interrupt
Information on interrupts in 1-bit mode, interrupts in 4-bit mode, and card interrupt handling are detailed in the sections below.
81.3.9.1
Interrupts in 1-bit mode
In this case, the DATA1 pin provides the interrupt function. An interrupt is asserted by pulling the DATA1 low from SDIO, until 
the interrupt service is finished to clear the interrupt.
81.3.9.2
Interrupt in 4-bit mode
As the interrupt and data line 1 share pin 8 in a 4-bit mode, an interrupt is only sent by the card and recognized by the host 
during a specific time. This is known as the interrupt period. The uSDHC module only provides samples the level on pin 8 
during the interrupt period. At all other times, the host treats it as the data signal. The definition of the interrupt period is 
different for operations with single block and multiple block data transfers.
In the case of normal single data block transmissions, the interrupt period becomes active two clock cycles after the completion of 
a data packet. This interrupt period lasts until after the card receives the end bit of the next command that has a data block transfer 
associated with it.
For multiple block data transfers in a 4-bit mode, there is only a limited period of time that the interrupt period can be active because 
of the limited period of data line availability between the multiple blocks of data. This requires stricter definition of the interrupt 
period. For this case, the interrupt period is limited to two clock cycles. This begins two clocks after the end bit of the previous data 
block. During this 2-clock cycle interrupt period, if an interrupt is pending, the DATA1 line holds low for one clock cycle, then pulls 
high for the next clock cycle . On completion of the interrupt period, the card releases the DATA1 line into the high Z state. The 
uSDHC module provides sample of the DATA1 during the interrupt period when the IABG bit in the Protocol Control register is set.
Refer to SDIO Specification v1.10 for further information about the SDIO interrupt.
81.3.9.3
Card interrupt handling
When the CINTIEN bit in the Interrupt Signal Enable Register is set to 0, uSDHC clears the interrupt request to the host 
system. The host driver should clear this bit before servicing the SDIO interrupt, and should set this bit again after all interrupt 
requests from the card are cleared to prevent inadvertent interrupts.
The SDIO Interrupt Status can be cleared by writing 1 to this bit. But as the interrupt source from SDIO does not clear, this bit is 
set again. To clear this bit, it is required to reset the interrupt source from the external card followed by writing 1 to this bit. In a 1-bit 
mode, uSDHC detects the SDIO interrupt with or without the SD clock (to support wakeup). In a 4-bit mode, the interrupt signal is 
sampled during the interrupt period, so there are some sample delays between the interrupt signal from SDIO and the interrupt to 
the Host System Interrupt Controller. When the SDIO status is set and the host driver needs to service this interrupt, the SDIO bit in 
the Interrupt Control Register of SDIO is cleared. This is required to clear the SDIO interrupt status latched in uSDHC and to stop 
driving the interrupt signal to the System Interrupt Controller. The host driver must issue a CMD52 to clear the card interrupt. After 
completion of the card interrupt service, the SDIO Interrupt Status Enable bit is set to 1 and uSDHC starts sampling the interrupt 
signal again.
See Figure 552 for an illustration of the SDIO interrupt scheme and for the sequences of software and hardware events that take 
place during a card interrupt handling procedure.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5065 / 5251


---
# 페이지 2206

Start
Enable card IRQ in Host
Detect and steer card IRQ
Read IRQ Status Register
Disable Card Interrupt Status enable in Host,
THEN write 1 to clear Card Interrupt status
Interrogate and Service Card IRQ
Response 
Error ?
Yes
No
Clear Card IRQ in Card
Enable card IRQ in Host
End
IP Bus
IRQ to CPUm
uSDHC Registers
SDIO IRQ Status
SDIO IRQ Enable
Command/
Response
Handling
IRQ Detecting & Steering
SDIO 
IRQ Routing
IRQ0
IRQ1
Function 0
Function 1
Clear IRQ1
Clear IRQ0
SD Host
SDIO 
Figure 552. Card interrupt scheme, card interrupt detection, and handling procedure
81.3.10 Software restrictions
81.3.10.1
Initialization active
The driver cannot set INITA bit in System Control register when any of the command line or data lines are active, so the driver 
must ensure both CDIHB and CIHB bits are cleared. 
81.3.10.2
Software polling procedure
For polling read or write, after the software begins a buffer read or write, it must access exactly the number of times as the 
values set in the Watermark Level Register; moreover, if the block size is not a multiple of the value in the Watermark Level 
Register (read and write respectively), the software must access exactly the remaining number of words at the end of each 
block. For example, for a read operation, if the RD_WML is 4, indicating the watermark level is 16 bytes, block size is 40 bytes, 
and the block number is 2, then the access times for the burst sequence in the whole transfer process must be 4, 4, 2, 4, 4, 2.
81.3.10.3
Suspend operation
To suspend the data transfer, the software must inform uSDHC that the suspend command is successfully accepted. To 
achieve this, after the Suspend command is accepted by SDIO, software must send another normal command marked as 
suspend command (CMDTYP bits set as '01') to inform uSDHC that the transfer is suspended.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5066 / 5251


---
# 페이지 2207

If software needs to resume the suspended transfer, it should read the value in BLKCNT register to save the remaining number of 
blocks before sending the normal command marked as suspend, otherwise on sending such a 'suspend' command, uSDHC treats 
the current transfer is aborted and change the BLKCNT register to its original value, instead of retaining the remaining number 
of blocks.
81.3.10.4
Data length setting
For either ADMA (ADMA1 or ADMA2) transfer, the data in the data buffer must be word aligned, so the data length set in the 
descriptor must be a multiple of 4.
ADMA1 is 4KB aligned.
81.3.10.5
(A)DMA address setting
To configure the ADMA1/ADMA2/DMA address register, when TC bit is set, the register always updates itself with the internal 
address value to support dynamic address synchronization, so the software must ensure that the TC bit is cleared prior to 
configuring the ADMA1/ADMA2/DMA address register.
81.3.10.6
Data port access
Data port does not support parallel access. For example, during an internal DMA access, it is not allowed to write any data to 
the data port by CPU; or during a CPU read operation, it is also prohibited to write any data to the data port, by either CPU or 
internal DMA. Otherwise the data is corrupted inside the uSDHC buffer.
81.3.10.7
Change clock frequency
The uSDHC module does not automatically gate off the card clock when the host driver changes the clock frequency. To 
prevent possible glitch on the card clock, clear the FRC_SDCLK_ON bit when changing the clock divisor value (SDCLKFS or 
DVS in System Control Register) or setting the RSTA bit.
Also, before changing the clock divisor value, the host driver should make sure that the SDSTB bit is high.
81.3.10.8
Multi-block read
For pre-defined multi-block read operation, that is, the number of blocks to read has been defined by previous CMD23 for 
eMMC, or pre-defined number of blocks in CMD53 for SDIO/SDCombo, or whatever multi-block read without abort command 
at card side, an abort command, either automatic or manual CMD12/CMD52, is still required by uSDHC after the pre-defined 
number of blocks are done, to drive the internal state machine to idle mode. In this case, the card may not respond to 
this extra abort command and uSDHC gets response timeout. It is recommended to manually send an abort command with 
RSPTYP[1:0] both bits cleared.
81.3.11 Clocking
The table found here describes the clock sources for uSDHC. For more information on clocking, see the Clocking chapter.
Table 814. Clocks
Clock name
Description
hclk
Bus clock
ipg_clk
Peripheral clock
ipg_clk_perclk
Base clock
ipg_clk_lp
Low power clock
81.3.11.1
Clock and reset manager
This module controls all four kinds reset signals within uSDHC:
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5067 / 5251


---
# 페이지 2208

• Hardware reset
• Software reset for all logic
• Software reset for the data logic
• Software reset for the command logic
All these signals are fed into this module and stable signals are generated inside the module to reset all other modules. The module 
also gates off all the inside signals.
81.3.11.2
Clock generator
The clock generator generates the card CLK by peripheral source clock in two stages. The clock divisor can be configured through 
register SYS_CTRL[SDCLKFS] for prescaler configuration while the [DVS] for divisor configuration. Details can be found in the 
register function description. See the following figure for the structure of the divider. The term "Base" represents the frequency of 
peripheral source clock (see ipg_clk_perclk in Table 814).
       
Base     
       
1st divisor
       
by 1, 2, 3, ..., 16     
       
DIV     
       
2nd divisor
       
by (1*), 2, 4, ..., 256     
       
/2     
       
DDR_EN     
       
card_clk     
       
CLK     
Figure 553. Two stages of the clock divider
The first stage outputs an intermediate clock (DIV) that can be Base, Base/2, Base/3, ..., or Base/16.
The second stage is a prescaler and outputs the actual internal working clock (card_clk). This clock is the driving clock for all 
the sub modules of the SD protocol unit, and helps in syncing FIFOs (see Figure 539) to synchronize with the data rate from the 
internal data buffer. The frequency of the clock output from this stage can be DIV, DIV/2, DIV/4,..., or DIV/256. Therefore, the 
highest frequency of the card_clk is base, and the next highest is Base/2, while the lowest frequency is Base/4096. If the duty cycle 
of the base clock is 50%, the duty cycle of card_clk is also 50%, even when the compound divisor is an odd value.
 
CLK is different for the SDR and DDR modes.
  NOTE  
- In the SDR mode, CLK is equal to the internal working clock (card_clk).
x
fCLK = fcard_clk
Equation 32. Equation for fcard_clk in SDR mode
card_clk
fCLK = fcard_clk = 200 MHz
- In the DDR mode, CLK is equal to card_clk/2
x
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5068 / 5251


---
# 페이지 2209

card_clk
Equation 33. Equation for fcard_clk in DDR mode
card_clk
card_clk
81.4 External signals
The following table describes the uSDHC external signals:
Table 815. uSDHC external signals
Signal
Description
Direction
CLK
Is an Internally generated clock used to drive the eMMC, SD 
card, and SDIO.
O
CMD
Is used to send commands and receive responses to and 
from the card.
I/O
DAT7
DAT7 line in the 8-bit mode —
Not used in other modes
I/O
DAT6
DAT6 line in the 8-bit mode —
Not used in other modes
I/O
DAT5
DAT5 line in the 8-bit mode —
Not used in other modes
I/O
DAT4
DAT4 line in the 8-bit mode —
Not used in other modes
I/O
 
If uSDHC needs to support a 4-bit data transfer, DAT7~DAT4 can also be optional and tied to high.
  NOTE  
DAT3
DAT3 line in the 4/8-bit mode or configured as card detection 
pin.
The bit may be configured as card detection pin in the 1-
bit mode.
I/O
DAT2
DAT2 line or Read Wait in the 4-bit mode
Read Wait in 1-bit mode
I/O
DAT1
DAT1 line in the 4/8-bit mode
Also, used to detect interrupt in 1/4-bit mode
I/O
DAT0
DAT0 line in all the modes
I/O
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5069 / 5251


---
# 페이지 2210

Table 815. uSDHC external signals (continued)
Signal
Description
Direction
Also, used to detect busy state
WP
Write protection signals directly routed from the socket.
Low value (0) indicates it is not write protected. In the case the 
pin is not used (for the embedded memory), tie low.
Optional for system implementation.
I
RESET_B
Is used to reset the eMMC.
O
81.5 Application information
All communication between the system and cards are controlled by the host. The host sends commands of two types: broadcast 
and addressed (point-to-point).
Broadcast commands are intended for all cards, such as GO_IDLE_STATE, SEND_OP_COND, and ALL_SEND_CID. In the 
Broadcast mode, eMMC are in the open-drain mode to avoid bus contention. See Commands for SD card, SDIO, and eMMC for 
the commands of bc and bcr categories.
After the broadcast command CMD3 is issued, the cards enter the standby mode. Addressed type commands are used from this 
point. In this mode, for eMMC, the CMD/DATA I/O pads turns to the push-pull mode to have the driving capability for maximum 
frequency operation. See Commands for SD card, SDIO, and eMMC for the commands of ac and adtc categories.
81.5.1 Command send and response receive basic operation
Assuming that the data type WORD is an unsigned 32-bit integer, the flow indicated below presents a guideline for sending a 
command to the card(s):
send_command(cmd_index, cmd_arg, other requirements)
{
    WORD wCmd; // 32-bit integer to make up the data to write into Transfer Type register, it is 
recommended to implement in a bit-field manner
    wCmd = (<cmd_index> & 0x3f) << 24; // set the first 8 bits as '00'+<cmd_index>
    set CMDTYP, DPSEL, CICEN, CCCEN, RSTTYP, DTDSEL according to the command index;
    if (internal DMA is used) wCmd |= 0x1;
    if (multi-block transfer) {
        set MSBSEL bit;
        if (finite block number) {
            set BCEN bit;
            if (auto12 command is to use) set AC12EN bit;
        }
    }
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5070 / 5251


---
# 페이지 2211

    write_reg(CMDARG, <cmd_arg>); // configure the command argument
    write_reg(XFERTYP, wCmd); // set Transfer Type register as wCmd value to issue the command
}
wait_for_response(cmd_index)
{
    while (CC bit in IRQ Status register is not set); // wait until Command Complete bit is set
    read IRQ Status register and check if any error bits about Command are set
    if (any error bits are set) report error;
    write 1 to clear CC bit and all Command Error bits;
}
For the sake of simplicity, the function wait_for_response is implemented here by means of polling. For an effective and formal 
way, the response is usually checked after the Command Complete Interrupt is received. When doing this, make sure that the 
corresponding interrupt status bits are enabled.
For some scenarios, the response time-out is expected. For instance, after all cards respond to CMD3 and move to the Standby 
state no response to the Host when CMD2 is sent. The host driver deals with "fake" errors like this with caution.
81.5.2 Card identification mode
When a card is inserted to the socket or the card is reset by the host, the host needs to validate the operation voltage range, 
identify the cards, request the cards to publish the Relative Card Address (RCA) or to set the RCA for eMMC. 
81.5.2.1
Card detect
See Figure 554 for a flow diagram showing the detection of SD card and SDIO using uSDHC.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5071 / 5251


---
# 페이지 2212

       
Enable card detection irq     
       
Wait for uSDHC interrupt     
       
Check CINS bit     
       
Yes cards present     
       
No cards present    
       
Clear CINSIEN to disable
       
card detection irq     
       
Voltage validation     
       
(2)     
       
(1)     
Figure 554. Flow diagram for card detection
Here is the card detect sequence:
• Set the CINSIEN bit to enable card detection interrupt.
• When an interrupt from uSDHC is received, check the CINS bit in the Interrupt Status register to see if it was caused by 
card insertion.
• Clear the CINSIEN bit to disable the card detection interrupt and ignore all card insertion interrupts afterwards.
81.5.2.2
Reset
The host consists of three types of resets:
• Hardware reset (Card and Host) that is driven by Power On Reset (POR).
• Software reset (Host only) is initiated by the write operation on the RSTD, RSTC, or RSTA bits of the System Control 
register to reset the data part, command part, or all parts of the host controller, respectively.
• Card reset (Card only): The command, "Go_Idle_State" (CMD0), is the software reset command for all types of eMMC and 
SD memory cards. This command sets each card into the idle state regardless of the current card state. For an SDIO, 
CMD52 is used to write an I/O reset in CCCR. The cards are initialized with a default relative card address (RCA=0x0000) 
and with a default driver stage register setting (lowest speed, highest driving current capability).
After the card is reset, the host needs to validate the voltage range of the card. See the figure below for the software flow to reset 
both uSDHC and the card.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5072 / 5251


---
# 페이지 2213

       
write "1" to RSTA bit to reset uSDHC     
       
Send 80 clocks to card     
       
Send CMD0/ CMD52 to card to reset card     
       
Voltage Validation     
Figure 555. Flow chart for resetting uSDHC and SD card or SDIO
software_reset() {
    set_bit(SYSCTRL, RSTA); // software reset the Host set DTOCV and SDCLKFS fields to get the CLK of
    //frequency around 400kHz
    //configure IO pad to set the power voltage of external card to around 3.0V
    //poll bits CIHB and CDIHB
    //bits of PRSSTAT to wait both fields are cleared
    set_bit(SYSCTRL, INTIA); // send 80 clock ticks for card to power up
    send_command(CMD_GO_IDLE_STATE, <other parameter>); // reset the card with CMD0 or
    send_command(CMD_IO_RW_DIRECT, <other parameter>);
}
81.5.2.3
Voltage validation
All cards should be able to establish communication with the host using any operation voltage in the maximum allowed voltage 
range specified in the card specification. However, the supported minimum and maximum values for VDD are defined in the 
Operation Conditions Register (OCR) and may not cover the whole range. Cards that store the CID and CSD data in the 
preload memory are only able to communicate this information under data transfer VDD conditions. This means that if the host 
and card have non-common VDD ranges, the card is neither able to complete the identification cycle nor able to send CSD 
data.
Therefore, special commands Send_Op_Cont (CMD1 for eMMC), SD_Send_Op_Cont (ACMD41 for SD Memory), and 
IO_Send_Op_Cont (CMD5 for SD I/O) are used. The voltage validation procedure is designed to provide a mechanism to 
identify and reject cards that do not match the VDD range(s) desired by the host. This is accomplished when the host sends the 
desired VDD voltage window as the operand of this command. Cards that cannot perform the data transfer in the specified range 
must discard themselves from further bus operations and go into the Inactive state. By omitting the voltage range in the command, 
the host can query each card and determine the common voltage range before sending out-of-range cards into the Inactive state. 
This query should be used if the host is able to select a common voltage range or if a notification is sent to the system when a 
non-usable card in the stack is detected.
The following steps show how to perform voltage validation when a card is inserted:
voltage_validation(voltage_range_argument) {
    label the card as UNKNOWN;
    send_command(IO_SEND_OP_COND, 0x0, <other parameters are omitted>); // CMD5, check SDIO operation 
voltage, command argument is zero
    if (RESP_TIMEOUT != wait_for_response(IO_SEND_OP_COND)) { // SDIO command is accepted
        if (0 < number of IO functions) {
            label the card as SDIO;
            IORDY = 0;
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5073 / 5251


---
# 페이지 2214

            while (!(IORDY in IO OCR response)) { // set voltage range for each IO function
                send_command(IO_SEND_OP_COND, <voltage range>, <other parameter>);
                wait_for_response(IO_SEND_OP_COND);
            } // end of while ...
        } // end of if (0 < ...
        if (memory part is present inside SDIO)
            Label the card as SDCombo; //this is an SD-Combo card
    } // end of if (RESP_TIMEOUT ...
    if (the card is labeled as SDIO)
        return; // card type is identified and voltage range is set, so exit the function;
    send_command(APP_CMD, 0x0, <other parameter>); // CMD55, Application specific CMD prefix
    if (no error calling wait_for_response(APP_CMD, <...>) { // CMD55 is accepted
        send_command(SD_APP_OP_COND, <voltage range>, <...>); // ACMD41, to set voltage range for 
memory part or SD card
        wait_for_response(SD_APP_OP_COND); // voltage range is set
        if (card type is UNKNOWN)
           label the card as SD;
        return; //
    } // end of if (no error ...
    else if (errors other than time-out occur) { // command/response pair is corrupted
        deal with it by program specific manner;
    } // of else if (response time-out
    else { // CMD55 is refuse, it must be eMMC
        if (card is already labeled as SDCombo) { // change label 
            re-label the card as SDIO;
            ignore the error or report it;
            return; // card is identified as SDIO
        } // end of if (card is ...
        send_command(SEND_OP_COND, <voltage range>, <...>);
        if(RESP_TIMEOUT == wait_for_response(SEND_OP_COND)) { // CMD1 is not accepted, 
            either label the card as UNKNOWN;
            return;
        } // end of if (RESP_TIMEOUT ...
    } // end of else
}
81.5.2.4
Card registry
This section briefly describes the registry flow. For details, please refer to the card specifications. Card registry for the eMMC 
and SD/SDIO/SD combo cards are different. For the SD card, the identification process starts at a clock rate lower than 400 
kHz and the power voltage higher than 2.7 V (as defined by the card spec). Currently, the CMD line output drives are push-pull 
drivers instead of open-drain. After the bus is activated, the host requests the card to send their valid operation conditions. The 
response to ACMD41 is the operation condition register of the card. The same command is sent to all the new cards in the system. 
Incompatible cards are put into the Inactive state. The host then issues the command, All_Send_CID (CMD2), to each card to get 
its unique card identification (CID) number. Cards that are currently unidentified (in the Ready state), send their CID number as 
the response. After the CID is sent by the card, the card goes into the Identification state.
The host then issues Send_Relative_Addr (CMD3), requesting the card to publish a new relative card address (RCA) that is 
shorter than the CID. This RCA is used to address the card for future data transfer operations. After the RCA is received, the card 
changes its state to the Standby state. At this point, if the host wants the card to have an alternative RCA number, it may ask the 
card to publish a new number by sending another Send_Relative_Addr command to the card. The last published RCA is the actual 
RCA of the card.
The host repeats the identification process with CMD2 and CMD3 for each card in the system until the last CMD2 gets no response 
from any of the cards in the system.
For eMMC operation, the host starts the card identification process in the open-drain mode with the identification clock rate lower 
than 400 kHz and the power voltage higher than 2.7 V. The open drain driver stages on the CMD line to allow parallel card 
operation during card identification. After the bus is activated, the host requests the cards to send their valid operation conditions 
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5074 / 5251


---
# 페이지 2215

(CMD1). The response to CMD1 is the "wired AND " operation on the condition restrictions of all cards in the system. Incompatible 
cards are sent into the Inactive state. The host then issues the broadcast command All_Send_CID (CMD2), asking all cards for 
their unique card identification (CID) number. All unidentified cards (the cards in the Ready state) simultaneously start sending 
their CID numbers serially, while bit-wise monitoring their outgoing bit stream. Those cards, whose outgoing CID bits do not match 
the corresponding bits on the command line in any one of the bit periods, stop sending their CID immediately and must wait for 
the next identification cycle. As the CID is unique for each card, only one card can be successfully sent its full CID to the host. 
This card then goes into the Identification state. Thereafter, the host issues Set_Relative_Addr (CMD3) to assign a relative card 
address (RCA) to the card. After the RCA is received, the state of the card changes to standby, and the card does not react in 
further identification cycles. Also, its output driver switches from open-drain to push-pull. The host repeats the process, mainly 
CMD2 and CMD3, until the host receives a time-out condition to recognize the completion of the identification process.
The following steps show how to perform an operation using eMMC:
card_registry() { 
    do { // decide RCA for each card until response time-out
        if(card is labelled as SDCombo or SDIO) { // for SDIO like device
            send_command(SET_RELATIVE_ADDR, 0x00, <...>); // ask SDIO to publish its RCA
            retrieve RCA from response; 
        } // end if (card is labelled as SDCombo ... 
        else if (card is labelled as SD) { // for SD card 
            send_command(ALL_SEND_CID, <...>); 
            if(RESP_TIMEOUT == wait_for_response(ALL_SEND_CID)) 
                break; 
            send_command(SET_RELATIVE_ADDR, <...>); 
            retrieve RCA from response; 
        } // else if (card is labelled as SD ... 
        else if (card is labelled as eMMC) { 
            send_command(ALL_SEND_CID, <...>); 
            rca = 0x1; //arbitrarily set RCA, 1 here for example 
            send_command(SET_RELATIVE_ADDR, 0x1 << 16, <...>); // send RCA at upper 16 bits 
        } // end of else if (card is labelled as eMMC... 
    } while (response is not time-out); 
}
81.5.3 Card access
Information about Block Write, Block Read, Suspense Resume, ADMA Usage, Transfer Error, and Card Interrupt are detailed in 
the sections below.
81.5.3.1
Block write
Information on Normal Write, DDR Write, and Write with Pause are detailed in the sections below.
81.5.3.1.1
Normal Write
During a block write (CMD24 - 27, CMD60, CMD61), one or more blocks of data are transferred from the host to the card with 
a CRC appended to the end of each block by the host. If the CRC fails, the card indicates that the failure on the DATA line. 
The transferred data is discarded and not written, and all further transmitted blocks (in multiple block write mode) are ignored.
If the host uses partial blocks whose accumulated length is not block aligned and block misalignment is not allowed (CSD 
parameter WRITE_BLK_MISALIGN is not set), the card detects the block misalignment error and aborts the programming before 
the beginning of the first misaligned block. The card sets the ADDRESS_ERROR error bit in the status register, and while ignoring 
all further data transfer, waits in the Receive-data-State for a stop command. The write operation is also aborted if the host tries 
to write over a write-protected area.
For eMMC and SD cards, programming of the CID and CSD registers does not require a previous block length setting. The 
transferred data is also CRC protected. If a part of the CSD or CID register is stored in ROM, then this unchangeable part must 
match the corresponding part of the receive buffer. If this match fails, then the card reports an error and does not change any 
register contents.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5075 / 5251


---
# 페이지 2216

For all types of cards, some may require long and unpredictable periods of time to write a block of data. After receiving a block 
of data and completing the CRC check, the card begins writing and holds the DATA line low if its write buffer is full and unable to 
accept new data from a new WRITE_BLOCK command. The host may poll the status of the card with a SEND_STATUS command 
(CMD13) or other means for SDIO at any time, and the card responds with its status. The responded status indicates whether the 
card can accept new data or whether the write process is still in progress. The host may deselect the card by issuing a CMD7 (to 
select a different card) to place the card into the Standby state and release the DATA line without interrupting the write operation. 
When re-selecting the card, it reactivates the busy indication by pulling data to low if the programming is still in progress and the 
write buffer is unavailable.
The software flow to write to a card that incorporates the internal DMA and the write operation is a multi-block write with the Auto 
CMD12 enabled. For the other two methods (by means of external DMA or CPU polling status with different transfer methods, the 
internal DMA parts should be removed and the alternative steps should be straightforward.
The software flow to write to a card is described below:
1. Check the card status, wait until the card is ready for data.
2. Set the card block length/size:
• For eMMC and SD cards, use SET_BLOCKLEN (CMD16).
• For SDIO cards or the I/O portion of SDCombo cards, use IO_RW_DIRECT (CMD52) to set the I/O Block Size bit 
field in the CCCR register (for function 0) or FBR register (for functions 1~7).
3. Set the uSDHC block length register to be the same as the block length set for the card in step 2.
4. Set the uSDHC number block register (NOB), where nob is 5, for instance.
5. Disable the buffer write ready interrupt, configure the DMA settings and enable the uSDHC DMA when sending the 
command with data transfer. The AC12EN bit should also be set.
6. Wait for the Transfer Complete interrupt.
7. Check the status bit to see if a write CRC error occurred, or another error that occurred during the auto12 command 
sending and response receiving.
81.5.3.1.2
DDR write
uSDHC supports the dual data rate mode.
The software flow to write to a card in the DDR mode is described as below:
1. Check the card status and wait until the card is ready for data.
 
For eMMC, block length only can be set to 512byte.
  NOTE  
2. Set the uSDHC number block register (NOB), where nob is 5, for instance.
3. Set the eMMC, SD card, or SDIO to high-speed mode and use SWITCH(CMD6).
4. Set the eMMC bus or SD with 4-bit/8-bit DDR mode and use SWITCH(CMD6).
5. Disable the buffer write ready interrupt, configure the DMA settings and enable the uSDHC DMA when sending the 
command with data transfer. The DDR_EN and AC12EN bits should be set.
6. Wait for the Transfer Complete interrupt.
7. Check the status bit to see if a write CRC error occurred or another error that occurred during the auto12 command 
sending and response receiving.
81.5.3.1.3
Write with Pause
The write operation can be paused during the transfer. Instead of stopping the CLK at any time to pause all the operations, 
which is also inaccessible to the host driver, the driver can set the Stop At Block Gap Request (SABGREQ) bit in the Protocol 
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5076 / 5251


---
# 페이지 2217

Control register to pause the transfer between the data blocks. As there is no time-out condition in a write operation during 
the data blocks, a write to all types of cards can be paused in this way, and if the DATA0 line is not required to de-assert to 
release the busy state, no suspend command is needed.
Similar to the flow described in Normal Write, the write with pause is shown with the same kind of write operation:
1. Check the card status and wait until the card is ready for data.
2. Set the card block length/size:
• For eMMC and SD cards, use SET_BLOCKLEN (CMD16).
• For SDIO or the I/O portion of SDCombo cards, use IO_RW_DIRECT(CMD52) to set the I/O Block Size bit field in 
the CCCR register (for function 0) or FBR register (for functions 1~7).
3. Set the uSDHC block length register to be the same as the block length set for the card in step 2.
4. Set the uSDHC number block register (NOB), where nob is 5, for instance.
5. Disable the buffer write ready interrupt, configure the DMA settings and enable the uSDHC DMA when sending the 
command with data transfer. The AC12EN bit should also be set.
6. Set the SABGREQ bit.
7. Wait for the Transfer Complete interrupt.
8. Clear the SABGREQ bit.
9. Check the status bit to see if a write CRC error occurred.
10. Set the CREQ bit to continue the write operation.
11. Wait for the Transfer Complete interrupt.
12. Check the status bit to see if a write CRC error occurred or some another error that occurred during the auto12 
command sending and response receiving.
The number of blocks left during the data transfer is accessible by reading the contents of the BLKCNT field in the Block Attribute 
register. As the data transfer and the setting of the SABGREQ bit are concurrent, and the delay of register read and the register 
setting, the actual number of blocks left may not be exactly the value read earlier. The host driver reads the value of BLKCNT after 
the transfer is paused and the Transfer Complete interrupt is received.
It is also possible that the last block has begun when the Stop At Block Gap Request is sent to the buffer. In this case, the next 
block gap is the end of the transfer. These types of requests are ignored, the driver should treat these as a non-pause transfer, 
and deal with it as a common write operation.
When the write operation is paused, the data transfer inside the host system is not stopped, and the transfer is active until the data 
buffer is full. Because of this, it is recommended to avoid using the Suspend command for SDIO. This is because when such a 
command is sent, uSDHC interprets the system that switches to another function on SDIO and flush the data buffer. uSDHC takes 
the Resume command as a normal command with data transfer, and it is left for the host driver to set all the relevant registers 
before the transfer is resumed. If there is only one block to send when the transfer is resumed, the MSBSEL and BCEN bits of the 
Transfer Type register are set as well as the AC12EN bit. However, the uSDHC module automatically sends a CMD12 to mark 
the end of the multi-block transfer.
81.5.3.2
Block read
Information about Normal read, DDR read, Read with Pause, and Delay Line (DLL) in Read Path are detailed in the sections below.
81.5.3.2.1
Normal read
For block reads, the basic unit of data transfer is a block whose maximum size is stored in areas defined by the corresponding 
card specification. A CRC is appended to the end of each block, ensuring data transfer integrity. The CMD17, CMD18, 
CMD53, CMD60, CMD61, and so on, can initiate a block read. After completing the transfer, the card returns to the Transfer 
state. For multi blocks read, data blocks are continuously transferred until a stop command is issued.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5077 / 5251


---
# 페이지 2218

The software flow to read from a card that incorporates the internal DMA and the read operation is a multi-block read with the Auto 
CMD12 enabled. For the other two methods (by means of external DMA or CPU polling status with different transfer methods, the 
internal DMA parts should be removed and the alternative steps should be straightforward.
The software flow to read from a card is described below:
1. Check the card status and wait until card is ready for data.
2. Set the card block length/size:
• For eMMC and SD cards, use SET_BLOCKLEN (CMD16).
• For SDIO or the I/O portion of SDCombo cards, use IO_RW_DIRECT(CMD52) to set the I/O Block Size bit field in 
the CCCR register (for function 0) or FBR register (for functions 1~7).
3. Set the uSDHC block length register to be the same as the block length set for the card in step 2.
4. Set the uSDHC number block register (NOB), where nob is 5, for instance.
5. Disable the buffer read ready interrupt, configure the DMA settings, and enable the uSDHC DMA when sending the 
command with data transfer. The AC12EN bit should also be set.
6. Wait for the Transfer Complete interrupt.
7. Check the status bit to see if a read CRC error occurred, or another error occurred during the auto12 command sending 
and response receiving.
81.5.3.2.2
DDR read
The uSDHC module supports dual data rate mode.
The software flow to write to a card in the DDR mode is described below:
1. Check the card status and wait until the card is ready for data.
 
For eMMC, block length can be set to only 512 bytes.
  NOTE  
2. Set the uSDHC number block register (NOB) where nob is 5, for instance.
3. Set the eMMC, SD card, or SDIO to high-speed mode and use SWITCH (CMD6).
4. Set the eMMC bus or SD with 4-bit /8-bit DDR mode and use SWITCH(CMD6).
5. Disable the buffer write ready interrupt, configure the DMA settings, and enable the uSDHC DMA when sending the 
command with data transfer. The DDR_EN and AC12EN bits should be set.
6. Wait for the Transfer Complete interrupt.
7. Check the status bit to see if a write CRC error occurred, or another error that occurred during the auto12 command 
sending and response receiving.
81.5.3.2.3
Read with Pause
The read operation is not generally able to pause. Only SDIO (and SDCombo card working under I/O mode) supporting the 
Read Wait feature can pause during the read operation. If SDIO supports Read Wait (SRW bit in CCCR register is 1), the host 
driver can set the SABGREQ bit in the Protocol Control register to pause the transfer between the data blocks. Before setting 
the SABGREQ bit, ensure that the RWCTL bit in the Protocol Control register is set, otherwise uSDHC does not assert the 
Read Wait signal during the block gap and data corruption occurs. It is recommended to set the RWCTL bit after the Read 
Wait capability of SDIO is recognized.
Similar to the flow described in Normal read, the read with pause is shown with the same kind of read operation:
1. Check the SRW bit in the CCR register on SDIO to confirm that the card supports the Read Wait mode.
2. Set the RWCTL bit.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5078 / 5251


---
# 페이지 2219

3. Check the card status and wait until the card is ready for data.
4. Set the card block length/size:
• For eMMC and SD cards, use SET_BLOCKLEN (CMD16).
• For SDIO or the I/O portion of SDCombo cards, use IO_RW_DIRECT(CMD52) to set the I/O Block Size bit field in 
the CCCR register (for function 0) or FBR register (for functions 1~7).
5. Set the uSDHC block length register to be the same as the block length set for the card in step 2.
6. Set the uSDHC number block register (NOB), where nob is 5, for instance.
7. Disable the buffer read ready interrupt, configure the DMA setting, and enable the uSDHC DMA when sending the 
command with data transfer. The AC12EN bit should also be set.
8. Set the SABGREQ bit.
9. Wait for the Transfer Complete interrupt.
10. Clear the SABGREQ bit.
11. Check the status bit to see if read CRC error occurred.
12. Set the CREQ bit to continue the read operation.
13. Wait for the Transfer Complete interrupt.
14. Check the status bit to see if a read CRC error occurred, or another error occurred during the auto12 command 
sending and response receiving.
Similar to the Write operation, it is possible to meet the ending block of the transfer when paused. In this case, uSDHC ignores 
the Stop At Block Gap Request and treats it as a command read operation.
Unlike the write operation, there is no remaining data inside the buffer when the transfer is paused. All data received before the 
pause is transferred to the host system. No matter if the Suspend command is sent or not, the internal data buffer is not flushed.
If the Suspend command is sent and the transfer is later resumed by means of a Resume command, uSDHC takes the command 
as a normal one accompanied with data transfer. It is left for the host driver to set all the relevant registers before the transfer is 
resumed. If there is only one block to send when the transfer is resumed, the MSBSEL and BCEN bits of the Transfer Type register 
are set, as well as the AC12EN bit. However, the uSDHC automatically sends CMD12 to mark the end of multi-block transfer.
81.5.3.2.4
Delay Line (DLL) in read path
The DLL is newly added to assist in sampling read data. The DLL provides the ability to programmatically select a quantized 
delay (in fractions of the clock period) regardless of on-chip variations such as process, voltage, and temperature (PVT).
The reasons why DLL is needed for uSDHC are these:
• The path of read data traveling from card to host varies.
• In the eMMC and SD cards DDR mode, the minimum input setup and hold time are both at 2.5 ns.
The data sampling window is so small that the delay of loopback clock needs to be accurate and consistent regardless of PVT. The 
DLL takes the divided card_clk as the reference clock and loopback clock as the input clock. It then generates a delayed version 
of the input clock according to the programmed target delay.
The DLL can be disabled or bypassed, and it can also be manually set for a fixed delay in the override mode. The override value 
set is the number of delay cells. In the override mode, there is no need to set the DLL_enable. Another DLL mode is target value 
mode. In this mode, the DLL automatically adjusts the number of delay cells according to the target value set by the user and 
PVT changes. Be aware that the target value is in units of 1/32 of the clock reference period. If the card_clk is 100Mhz, then the 
reference clock period is 10ns; setting target value of 16 means 5ns =(16/32)*10ns. The software can disable automatic update 
by the setting dll_gate_update bit.
As you might change the frequency of card_clk from time to time by changing SDCLKFS[7:0]/DVS[3:0], the software must adjust 
the delay value to ensure it works correctly when the reference clock (card_clk) is changed. If DLL is to be used, make sure 
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5079 / 5251


---
# 페이지 2220

SDCLKFS is used (at least be set to divided by 2) so that the REF_CLK generated are the same frequency as card_clk. There are 
two DLLs, PARTS DLL and STROBE DLL.
Step 1: Set the DLL_CTRL_RESET and DLL_CTRL_ENABLE fields
Step 2: Configure the SDCLKFS[7:0] and DVS[3:0]
Step 3: Wait until SDSTB is asserted
Step 4: Clear the DLL_CTRL_RESET field
Step 5: Wait until both the DLL_STS_SLV_LOCK and DLL_STS_REF_LOCK are asserted
Step 6: Set the DLL_CTRL_SLV_FORCE_UPD
Step 7: Clear the DLL_CTRL_SLV_FORCE_UPD
 
The software should make sure that the DLL_CTRL_SLV_FORCE_UPD lasts for at least one card_clk. So, the 
software may need to add some delay between step 6 and step 7.
  NOTE  
8
ipp_card_clk_in
ipp_card_clk_in_dll
DATA
card_clk_pad
Async
Buffer
Read Data
Card_clk
Delay Line
uSDHC
SD/eMMC
DDR_EN
/2
6
5
4
3
1
2
Figure 556. DLL in read path
81.5.3.3
Suspend Resume
The uSDHC module supports the Suspend Resume operations of SDIO, although slightly different than the suggested 
implementation of Suspend in the SDIO specification.
81.5.3.3.1
Suspend
After setting the SABGREQ bit, the host driver may send a Suspend command to switch to another function of SDIO. The uSDHC 
module does not monitor the content of the response, so it does not know if the Suspend command succeeded or not. Accordingly, 
it does not de-assert Read Wait for read pause. To solve this problem, the host driver does not mark the Suspend command as 
"Suspend", (that is, setting the CMDTYP bits to 01). Instead, the driver sends this command as if it were a normal command, 
and only when the command succeeds, and the BS bit is set in the response, can the Driver send another command marked as 
"Suspend" to inform uSDHC that the current transfer is suspended. Here is the sequence for the Suspend operation:
1. Set the SABREQ bit to pause the current data transfer at block gap.
2. After the BGE bit is set, send the Suspend command to suspend the active function. The CMDTYP bit field must be 
2'b00.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5080 / 5251


---
# 페이지 2221

3. Check the BS bit of the CCCR in the response. If it is 1, repeat this step until the BS bit is cleared or abandon the 
suspend operation according to the Driver strategy.
4. Send another normal I/O command to the suspended function. The CMDTYP of this command must be 2'b01, so 
uSDHC can detect this special setting and be informed that the paused operation has successfully suspended. If the 
paused transfer is a read operation, uSDHC stops driving DATA2 and goes to the idle state.
5. Save the context registers in the system memory for later use, including the DMA System Address Register (for internal 
DMA operation), and the Block Attribute Register.
6. Begin operation for another function on SDIO.
81.5.3.3.2
Resume
To resume the data transfer, a Resume command is issued:
1. To resume the suspended function, restore the context register with the saved value in step #5 of the Suspend 
operation.
2. Send the Resume command: In the Transfer Type register, all the bit fields are set to the value as if this were another 
ordinary data transfer instead of a transfer resume (except the CMDTYP is set to 2'b10).
3. If the Resume command has responded, the data transfer is resumed.
81.5.3.4
ADMA usage
To use the ADMA in a data transfer, the host driver must prepare the correct descriptor chain prior to sending the read/write 
command. The steps to prepare the correct descriptor chain are these:
1. Create a descriptor to set the data length that the current descriptor group is about to transfer. The data length should 
be even numbers of the block size.
2. Create another descriptor to transfer the data from the address setting in this descriptor. The data address must be at a 
page boundary (4KB address aligned).
3. If necessary, create a Link descriptor containing the address of the next descriptor. The descriptor group is created in 
steps 1 ~ 3.
4. Repeat steps 1 ~ 3 until all descriptors are created.
5. In the last descriptor, set the End flag to 1 and make sure the total length of all descriptors matches the product of the 
block size and block number configured in the Block Attribute Register.
6. Set the ADMA System Address Register to the address of the first descriptor and set the DMAS field in the Protocol 
Control Register to 01 to select the ADMA.
7. Issue a write or read command with the DMAEN bit set to 1 in the Transfer Type Register.
Steps 1 ~ 5 are independent of step 6, so step 6 can finish before steps 1 ~ 5. Regarding the descriptor configuration, it is 
recommended not to use the Link descriptor as it requires extra system memory access.
81.5.3.5
Transfer error
Information about CRC, Internal DMA, Transfer ADMA, and Auto CMD12 errors are detailed in the sections below.
81.5.3.5.1
CRC error
It is possible at the end of a block transfer that a write CRC status error or read CRC error occurs. For this type of error, 
the latest block received is discarded. This is because the integrity of the data block is not guaranteed. It is recommended to 
discard the following data blocks and re-transfer the block from the corrupted one. For a multi-block transfer, the host driver 
issues a CMD12 to abort the current process and start the transfer by a new data command. In this scenario, even when the 
AC12EN and BCEND bits are set, uSDHC does not automatically send a CMD12 because the last block is not transferred. On 
the other hand, if it is within the last block that the CRC error occurs, an Auto CMD12 is sent by uSDHC. In this case, the host 
driver re-sends or re-obtains the last block with a single block transfer.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5081 / 5251


---
# 페이지 2222

81.5.3.5.2
Internal DMA error
During the data transfer with internal Simple DMA, if the DMA engine encounters an error on the AHB bus, the DMA operation 
is aborted, and the DMA error interrupt is sent to the host system. When acknowledged by such an interrupt, the host driver 
calculates the start address of data block in which the error occurs. The start address can be calculated by either:
• Reading the DMA System Address register: The error occurs during the previous burst. Considering the block size, the 
previous burst length and the start address of the next burst transfer, it is straight forward to obtain the start address of the 
corrupted block.
• Reading the BLKCNT field of the Block Attribute register: Considering the number of blocks left, the total number 
to transfer, the start address of transfer, and the size of each block, the start address of corrupted block can be 
determined.To use this method, MIX_CTRL[BCEN] bit has to be set to enable Block Attribute register update.
When a DMA error occurs, it is recommended to abort the current transfer by means of a CMD12 (for multi block transfer), apply 
a reset for data, and restart the transfer from the corrupted block to recover from the error.
81.5.3.5.3
Transfer ADMA error
There are three kinds of possible ADMA errors: The AHB transfer, invalid descriptor, and data-length mismatch. Whenever 
these errors occur, the DMA transfer stops and the corresponding error status bit is set. For acknowledging the status, the 
host driver should recover the error as shown below and re-transfer from the place of interruption.
• AHB transfer error: Such errors may occur during data transfer or descriptor fetch. For either scenario, it is recommended 
to retrieve the transfer context, reset for the data part and re-transfer the block that was corrupted, or to the next block if 
no block is corrupted.
• Invalid descriptor error: For such errors, it is recommended to retrieve the transfer context, reset for the data part and 
recreate the descriptor chain from the invalid descriptor and issue a new transfer. As the data to transfer now may be less 
than the previous setting, the data length configured in the new descriptor chain should match the new value.
• Data-length mismatch error: It is similar to recover from this error. The Host Driver polls relating registers to retrieve the 
transfer context, apply a reset for the data part, configure a new descriptor chain and make another transfer if there is data 
left. Like the previous scenario of the invalid descriptor error, the data length must match the new transfer.
81.5.3.5.4
Auto CMD12 error
After the last block of the multi-block transfer is sent or received, and the AC12EN bit is set when the data transfer is initiated 
by the data command, uSDHC automatically sends a CMD12 to the card to stop the transfer. When errors with this command 
occur, it is recommended to the host driver to deal with the situations in the following manner:
• Auto CMD12 response time-out: It is not certain whether the command is accepted by the card or not. The host driver 
clears the auto CMD12 error status bits and re-send CMD12 until it is accepted by the card.
• Auto CMD12 response CRC error: As the card responds to CMD12, it aborts the transfer. The host driver may ignore the 
error and clear the error status bit.
• Auto CMD12 conflict error or not sent: The command is not sent; therefore, the host driver sends a CMD12 manually.
81.5.3.6
Card interrupt
The external cards can inform the host controller by means of some special signals. For SDIO, it can be the low-level on the DATA1 
line during some special period. The uSDHC module only monitors the DATA1 line and supports the SDIO interrupt.
When the SDIO interrupt is captured by uSDHC, and the host system is informed by uSDHC asserting the uSDHC interrupt line, 
the interrupt service from the host driver is called.
As the interrupt source is controlled by the external card, the interrupt from SDIO must be serviced before the CINT bit is cleared. 
Refer to Card interrupt handling for the card interrupt handling flow.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5082 / 5251


---
# 페이지 2223

81.5.4 Switch function
A switch command is issued by the host driver to enable new features added to the eMMC and SD cards. The eMMC and SD 
cards can transfer data at bus widths other than 1-bit. Different speed modes are also defined. To enable these features, a switch 
command is issued by the host driver.
For SDIO, the high-speed mode are enabled by writing the EHS bit in the CCCR register after the SHS bit is confirmed as high. 
For SD cards, the high-speed mode are queried and enabled by a CMD6 (with the mnemonic symbol as SWITCH_FUNC). For 
eMMC, the high-speed mode is queried by a CMD8 and enabled by a CMD6 (with the mnemonic symbol as SWITCH).
The SDR4-bit, SDR8-bit, DDR4-bit, and DDR8-bit width of eMMC is also enabled by the SWITCH command, but with a 
different argument.
These new functions can also be disabled by a software reset. For SDIO, it can be done by setting the RES bit in the CCCR 
register. For other cards, it can be accomplished by issuing a CMD0. This method of restoring to the normal mode is not 
recommended because a complete identification process is needed before the card is ready for data transfer.
For the sake of simplicity, the following pseudo-code examples do not show current capability check, which is recommended in 
the function switch process.
81.5.4.1
Query, enable, and disable SDIO high-speed mode
enable_sdio_high_speed_mode(void)
{
send CMD52 to query bit SHS at address 0x13;
if (SHS bit is '0') report SDIO does not support high speed mode and return;
send CMD52 to set bit EHS at address 0x13 and read after write to confirm EHS bit is set;
change clock divisor value or configure the system clock feeding into uSDHC to generate the card_clk 
of around 50MHz;
(data transactions like normal peers)
}
disable_sdio_high_speed_mode(void)
{
send CMD52 to clear bit EHS at address 0x13 and read after write to confirm EHS bit is cleared;
change clock divisor value or configure the system clock feeding into uSDHC to generate the card_clk 
of the desired value below 25MHz;
(data transactions like normal peers)
}
81.5.4.2
Query, enable, and disable SD high-speed mode
enable_sd_speed_mode(void)
{
set BLKCNT field to 1 (block), set BLKSIZE field to 64 (bytes);
send CMD6, with argument 0xFFFFFx and read 64 bytes of data accompanying the R1 response;(high speed 
mode,x=1;)
wait data transfer done bit is set;
check if the bit x of received 512 bits is set;
if (bit 401 is '0') report the SD card does not support high speed mode and return;
      send CMD6, with argument 0x80FFFFFx and read 64 bytes of data accompanying the R1 response;
(high speed mode,x=1;)
check if the bit field 379~376 is 0xF;
if (the bit field is 0xF) report the function switch failed and return;
change clock divisor value or configure the system clock feeding into uSDHC to generate the card_clk 
of around 50MHz for high speed mode
(data transactions like normal peers)
}
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5083 / 5251


---
# 페이지 2224

disable_sd_speed_mode(void)
{
set BLKCNT field to 1 (block), set BLKSIZE field to 64 (bytes);
send CMD6, with argument 0x80FFFFF0 and read 64 bytes of data accompanying the R1 response;
check if the bit field 379~376 is 0xF;
if (the bit field is 0xF) report the function switch failed and return;
change clock divisor value or configure the system clock feeding into uSDHC to generate the 
card_clk of the desired value below 25MHz;
(data transactions like normal peers)
}
81.5.4.3
Query, enable, and disable eMMC high-speed mode
enable_mmc_high_speed_mode(void)
{
send CMD9 to get CSD value of eMMC;
check if the value of SPEC_VER field is 4 or above;
if (SPEC_VER value is less than 4) report the eMMC does not support high speed mode and return;
set BLKCNT field to 1 (block), set BLKSIZE field to 512 (bytes);
send CMD8 to get EXT_CSD value of eMMC;
extract the value of CARD_TYPE field to check the 'high speed mode' in this eMMC is 26MHz or 
52MHz;
send CMD6 with argument 0x1B90100;
send CMD13 to wait card ready (busy line released);
send CMD8 to get EXT_CSD value of eMMC;
check if HS_TIMING byte (byte number 185) is 1;
if (HS_TIMING is not 1) report eMMC switching to high speed mode failed and return;
change clock divisor value or configure the system clock feeding into uSDHC to generate the 
card_clk of around 26MHz or 52MHz according to the CARD_TYPE;
(data transactions like normal peers)
}
disable_mmc_high_speed_mode(void)
{
send CMD6 with argument 0x2B90100;
set BLKCNT field to 1 (block), set BLKSIZE field to 512 (bytes);
send CMD8 to get EXT_CSD value of eMMC;
check if HS_TIMING byte (byte number 185) is 0;
if (HS_TIMING is not 0) report the function switch failed and return;
change clock divisor value or configure the system clock feeding into uSDHC to generate the 
card_clk of the desired value below 20MHz;
(data transactions like normal peers)
}
81.5.4.4
Set eMMC bus width
change_mmc_bus_width(void)
{
send CMD9 to get CSD value of eMMC;
check if the value of SPEC_VER field is 4 or above;
if (SPEC_VER value is less than 4) report the eMMC does not support multiple bit width and return;
send CMD6 with argument 0x3B70x00; (8-bit(dual data rate), x=6; 4-bit(dual data rate), x=5;8-bit, 
x=2; 4-bit, x=1; 1-bit, x=0)
send CMD13 to wait card ready (busy line released);
(data transactions like normal peers)
}
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5084 / 5251


---
# 페이지 2225

81.5.5 ADMA operation
Here are the codes for the ADMA1 and ADMA2 operations.
81.5.5.1
ADMA1 operation
Set_adma1_descriptor
{
if (to start data transfer) {
// Make sure the address is 4KB align.
Set 'Set' type descriptor;
{
Set Act bits to 01;
Set [31:12] bits data length (byte unit);
}
Set 'Tran' type descriptor;
{
Set Act bits to 10;
Set [31:12] bits address (4KB align);
}
}
else if (to fetch descriptor at non-continuous address) {
Set Act bits to 11;
Set [31:12] bits the next descriptor address (4KB aligned);
}
else { // other types of descriptor
Set Act bits accordingly
}
if (this descriptor is the last one) {
Set End bit to 1;
}
if (to generate interrupt for this descriptor) {
Set Int bit to 1;
}
Set Valid bit to 1;
}
81.5.5.2
ADMA2 operation
Set_adma2_descriptor
{
if (to start data transfer) {
// Make sure the address is a 32-bit boundary (lower 2-bit are always '00').
Set higher 32-bit of descriptor for this data transfer initial address;
Set [31:16] bits data length (byte unit);
Set Act bits to '10';
}
else if (to fetch descriptor at non-continuous address) {
Set Act bits to '11';
// Make sure the address is 32-bit boundary (lower 2-bit are always set to '00').
Set higher 32-bit of descriptor for the next descriptor address;
}
else { // other types of descriptor
Set Act bits accordingly
}
if (this descriptor is the last one) {
Set 'End' bit '1';
}
if (to generate interrupt for this descriptor) {
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5085 / 5251


---
# 페이지 2226

Set 'Int' bit '1';
}
Set the 'Valid' bit to '1';
}
81.5.6 Fast boot operation
81.5.6.1
Normal fast boot flow
Here are the steps for normal fast boot flow:
1. Software must configure the SYS_CTRL[INITA] bit to make sure that 74 card clocks are finished.
2. Software must configure the eMMC Boot Register (offset 0xc4) bit 6 to 1 (enable boot), and bit 5 to 0 (normal fast boot), 
and bit 4 to select the ack mode. If the data is sent through the DMA mode, the software should configure bit 7 to enable 
the automatic stop at block gap feature, and configure bit 3-bit 0 to select the ack timeout value according to the SD 
CLK frequency.
3. Software then needs to configure the Block Attributes Register to set the block size and count. If in DDR fast boot mode, 
the block size only can be configured to 512 bytes.
4. Software must configure the Protocol control register to set Data Transfer Width (DTW). If in the DDR fast boot mode, 
DTW only can be configured to 4-bit/8-bit dataline mode.
5. Software needs to configure the Command Argument Register to set argument if needed (no need in normal fast boot).
6. Software must configure the Transfer Type Register to start the boot process. In normal boot mode, CMDINX, 
CMDTYP, RSPTYP, CICEN, CCCEN, AC12EN, BCEN and DMAEN retain the default value, where DPSEL bit is set to 
1, DTDSEL is set to 1 and MSBSEL is set to 1.
7. DMAEN should be configured as 0 in the polling mode and if BCEN is configured as 1, it is recommended to configure 
the number of blocks in the Block Attributes Register to the maximum value. If in DDR fast boot mode, DDR_EN needs 
to be set to 1.
8. When step 6 is configured, the boot process begins. The software needs to poll the data buffer ready status to read 
the data from the buffer in time. If a boot timeout happens (ack times out or the first data read times out), an interrupt 
is triggered, and the software must configure eMMC Boot Register to bit 6 to 0 to disable boot. This makes CMD high, 
then after at least 56 clocks, it is ready to begin a normal initialization process.
9. If there is no timeout, software needs to determine when the data read is finished and then configure eMMC Boot 
Register bit 6 to 0 to disable boot. This render CMD line high and command completed asserted. After at least 56 
clocks, it is ready to begin the normal initialization process.
10. You must reset the host and begin the normal process.
81.5.6.2
Alternative fast boot flow
Here are the steps for alternative fast boot flow:
1. Software needs to configure SYS_CTRL[INITA] to make sure 74 card clocks are finished.
2. Software needs to configure eMMC Boot Register (offset 0xc4) bit 6 to 1 (enable boot), and bit 5 to 1 (alternative 
boot), and bit 4 to select the ack mode or not. If data needs to be sent through the DMA mode, then configure bit 7 to 
enable the automatic stop at block gap feature. Software should also configure bit 3-bit 0 to select the ack timeout value 
according to the SD clock frequency.
3. Software then needs to configure the Block Attributes Register to set the block size and count. If in the DDR fast boot 
mode, the block size only can be configured to 512 bytes.
4. Software needs to configure the Protocol control register to set the data transfer width (DTW). If in the DDR fast boot 
mode, DTW only can be configured to 4-bit/8-bit dataline mode.
5. Software needs to configure Command Argument Register to set argument to 0xFFFFFFFA.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5086 / 5251


---
# 페이지 2227

6. Software needs to configure the Transfer Type Register to start the boot process by CMD0 with the 0xFFFFFFFA 
argument. In alternative boot, CMDINX, CMDTYP, RSPTYP, CICEN, CCCEN, AC12EN, BCEN, and DMAEN retain the 
default value. DPSEL bit is set to 1, DTDSEL is set to 1, and MSBSEL is set to 1. Note DMAEN should be configured as 
0 in the polling mode, and if BCEN is configured as 1 in polling mode, it is recommended to configure the block count in 
the Block Attributes Register to the maximum value. If in the DDR fast boot mode, DDR_EN needs to be set to 1.
7. When step 6 is configured, the boot process begins. Software needs to poll the data buffer ready status to read the data 
from the buffer in time. If there is a boot timeout (ack data timeout in 50ms or data timeout in 1s), the host sends out 
the interrupt and the software needs to send CMD0 with reset and then configure the boot enable bit to 0 to stop this 
process.
8. If there is no time out, the software needs to decide when to stop the boot process, and send out the CMD0 with reset 
and then after the command is completed, configure the eMMC Boot Register bit 6 to stop the process. After 8 clocks 
from the command completion, the slave (card) is ready for the identification step.
9. You must reset the host and begin the normal process.
81.5.6.3
Fast boot application case (in DMA mode)
In the boot application case, because the image destination and the image size are contained in the beginning of the image, it 
is necessary to switch DMA parameters on the fly during eMMC fast boot.
In fast boot, the host can use Advanced DMA2 (ADMA2) with two destinations.
The detailed flow is described below:
1. The software needs to configure INIT_ACTIVE bit (system control register bit 27) to make sure that 74 card clocks are 
finished.
2. The software needs to configure the eMMC Boot Register (offset 0xc4) bit 6 to 1 (enable boot); and bit 5 to 0 (normal 
fast boot) or 1 (alternative boot); and bit 4 to select the ack mode. In DMA mode, configure bit 7 to 1 to enable the 
automatic stop at block gap feature. Also configure bits[31-16] to set the (BLK_CNT - VALUE1). Here VALUE1 is the 
value of the block count that needs to transfer the first time, so that the host stops at the block gap when the uSDHC 
controller gets VAULE1 blocks from the device. Also, configure bits[3-0] to select the ack timeout value according to the 
SD clock frequency.
3. The software then needs to configure the Block Attributes Register to set block size and count. If in DDR fast boot 
mode, the block size only can be configured to 512 bytes. In DMA mode, it is recommended to set the block count 
(BLK_CNT) to the max value (16'hffff).
4. The software needs to configure Protocol Control Register to set DTW (data transfer width). If in DDR fast boot mode, 
the DTW only can be configured to 4-bit/8-bit dataline mode.
5. Software enable ADMA2 by configuring Protocol Control Register bits [9-8].
6. The software needs to set at least three pairs of ADMA2 descriptor in boot memory (that is, in IRAM, at least six words). 
The first pair descriptor defines the start address (that is, IRAM) and data length (that is,512byte*VALUE1) of the first 
part boot code. The software also needs to set the second pair descriptor, the second start address (any value that 
is writable), and data length is suggested to set 1~2word (record as VALUE2). Note that the second couple desc also 
transfers useful data even at lease 1 word, because our ADMA2 cannot support 0 data_length data transfer descriptor.
7. The software needs to configure Command Argument Register to set argument to 0xFFFFFFFA in alternative fast boot 
and do not need to be set in normal fast boot.
8. The software needs to configure Transfer Type Register to start the boot process. CMDINX, CMDTYP, RSPTYP, 
CICEN, CCCEN, AC12EN, BCEN, and DMAEN retain the default value. DPSEL bit is set to 1, DTDSEL is set to 1, and 
MSBSEL is set to 1. DMAEN is configured as 1 in the DMA mode. And, if BCEN is configured as 1, then configure blk 
no in Bock Attributes Register to the max value. And, if in the DDR fast boot mode, DDR_EN needs to be set to 1.
9. When step 8 is configured, boot process begins, the first VALUE1 block number data gets transferred. The software 
needs to poll the TC bit (bit1 in Interrupt Status Register) to determine first transfer is ended. Also, the software needs to 
polling the BGE bit (bit2 in Interrupt Status Register) to determine if the first transfer stops at the block gap.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5087 / 5251


---
# 페이지 2228

10. When TC and BGE bits are set to 1, the software can analyze the first code of VALUE1 block, initializes the new 
memory device, if required, and sets the third pair of descriptors to define the start address and length of the remaining 
part of the boot code (VALUE3, the remain boot code block). Remember to set the last descriptor with END.
11. The software needs to configure the eMMC Boot Register (offset 0xc4) again. Set bit 6 to 1 (enable boot); and bit 5 
to 0 (normal fast boot), to 1 (alternative boot); and bit 4 to select the ack mode or not. In the DMA mode, configure 
bit 7 to 1 for enabling the automatically stop at block gap feature. Also, configure bit31-bit16 to set the (BLK_CNT - 
(VALUE1+1+VALUE3)), that host stops at block gap when the uSDHC controller gets (VALUE1+1+VALUE3)) blocks 
from device totally include the blocks received in step 9. And need to configure bit 3-bit0 to select the ack timeout value 
according to the sd clk frequency. Note that the software does not need to configure the BLK_CNT again, because it is 
counted down automatically by the uSDHC controller.
12. The software needs to clear the TC and BGE bits and the software needs to clear SABGREQ (bit 16 in the Protocol 
control register) and set CREQ (bit17 in the Protocol control register) to 1 to resume the data transfer. Host transfers 
the VALUE2 and VALUE3 data to the destination that is set by descriptor.
13. The software needs to do poll BGE bit to determine if the fast boot is over.
Note:
• When ADMA boot flow starts, for uSDHC, it is like a normal ADMA read operation. So, set ADMA2 descriptor as the 
normal ADMA2 transfer.
• Need a few words length memory to keep descriptor.
• For the 1~2-word data in second descriptor setting, it is a useful data, so the software needs to deal the data because of 
the application case.
81.6 uSDHC memory map and register definition
81.6.1 uSDHC register descriptions
This section includes the module memory map and detailed descriptions of all registers.
See the table below for the register memory map of uSDHC. All these registers only support 32-bit accesses.
 
The uSDHC registers are 32-bit wide and only support 32-bit access.
  NOTE  
81.6.1.1
uSDHC memory map
usdhc base address: 404E_4000h
Offset
Register
Width
(In bits)
Access
Reset value
0h
DMA System Address (DS_ADDR)
32
RW
0000_0000h
4h
Block Attributes (BLK_ATT)
32
RW
0001_0000h
8h
Command Argument (CMD_ARG)
32
RW
0000_0000h
Ch
Command Transfer Type (CMD_XFR_TYP)
32
RW
0000_0000h
10h
Command Response0 (CMD_RSP0)
32
R
0000_0000h
14h
Command Response1 (CMD_RSP1)
32
R
0000_0000h
18h
Command Response2 (CMD_RSP2)
32
R
0000_0000h
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5088 / 5251


---
# 페이지 2229

Table continued from the previous page...
Offset
Register
Width
(In bits)
Access
Reset value
1Ch
Command Response3 (CMD_RSP3)
32
R
0000_0000h
20h
Data Buffer Access Port (DATA_BUFF_ACC_PORT)
32
RW
0000_0000h
24h
Present State (PRES_STATE)
32
R
See section
28h
Protocol Control (PROT_CTRL)
32
RW
0880_0020h
2Ch
System Control (SYS_CTRL)
32
RW
0080_800Fh
30h
Interrupt Status (INT_STATUS)
32
RW
0000_0000h
34h
Interrupt Status Enable (INT_STATUS_EN)
32
RW
0000_0000h
38h
Interrupt Signal Enable (INT_SIGNAL_EN)
32
RW
0000_0000h
3Ch
Auto CMD12 Error Status (AUTOCMD12_ERR_STATUS)
32
R
0000_0000h
40h
Host Controller Capabilities (HOST_CTRL_CAP)
32
R
03F3_B404h
44h
Watermark Level (WTMK_LVL)
32
RW
0810_0810h
48h
Mixer Control (MIX_CTRL)
32
RW
8000_0000h
50h
Force Event (FORCE_EVENT)
32
RW
0000_0000h
54h
ADMA Error Status (ADMA_ERR_STATUS)
32
R
0000_0000h
58h
ADMA System Address (ADMA_SYS_ADDR)
32
RW
0000_0000h
60h
DLL (Delay Line) Control (DLL_CTRL)
32
RW
0000_0000h
64h
DLL Status (DLL_STATUS)
32
R
0000_0200h
C0h
Vendor Specific Register (VEND_SPEC)
32
RW
3000_7809h
C4h
eMMC Boot (MMC_BOOT)
32
RW
0000_0000h
C8h
Vendor Specific 2 Register (VEND_SPEC2)
32
RW
0001_9006h
81.6.1.2
DMA System Address (DS_ADDR)
Offset
Register
Offset
DS_ADDR
0h
Function
This register contains the physical system memory address used for DMA transfers.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5089 / 5251


---
# 페이지 2230

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
DS_ADDR 
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
DS_ADDR 
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
31-2
DS_ADDR
DMA system address
This field contains the memory address for a DMA transfer. Because the address must be word (4 bytes) 
aligned, the least 2 bits are reserved, always 0. When uSDHC stops a DMA transfer, this field points to 
the system address of the next contiguous data position. It can be accessed only when no transaction is 
executing (that is, after a transaction has stopped). Read operation during transfers may return an invalid 
value. The host driver initializes this field before starting a DMA transaction. After DMA has stopped, the 
system address of the next contiguous data position can be read from this field.
This field is protected during a data transfer. When data lines are active, write to this field is ignored. The 
host driver waits until the DLA field in the Present State register is cleared, before writing to this field.
The uSDHC internal DMA does not support a virtual memory system. It only supports continuous physical 
memory access. Also, because AHB burst limitations, if the burst must cross the 1 KB boundary, uSDHC 
automatically changes SEQ burst type to NSEQ.
Because this field supports dynamic address reflecting, when TC field is set, it automatically alters the value 
of internal address counter, so the software cannot change this field when TC field is set. Such restriction 
is also listed in Software restrictions.
1-0
—
Reserved
81.6.1.3
Block Attributes (BLK_ATT)
Offset
Register
Offset
BLK_ATT
4h
Function
This register is used to configure the number of data blocks and the number of bytes in each block.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5090 / 5251


---
# 페이지 2231

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
BLKCNT 
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
0
BLKSIZE 
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
BLKCNT
Blocks count for current transfer
This field is enabled when the Block Count Enable field in the Transfer Mode register is set to 1 and is valid 
only for multiple block transfers. For single block transfer, this field always reads as 1. The host driver sets 
this field to a value between 1 and the maximum block count. The uSDHC module decrements the block 
count after each block transfer and stops when the count reaches zero. Setting the block count to zero 
results in no data blocks being transferred.
This field should be accessed only when no transaction is executing (that is, after transactions are 
stopped). During data transfer, read operations on this field may return an invalid value and write operations 
are ignored.
When saving transfer content because of a Suspend command, the number of blocks yet to be transferred 
can be determined by reading this field. The reading of this field should be applied after transfer is paused 
by stop at block gap operation and before sending the command marked as suspend. This is because when 
the Suspend command is sent out, uSDHC treats the current transfer as aborted and change the BLKCNT 
field back to its original value instead of keeping the dynamical indicator of the remaining block count.
When restoring transfer content prior to issuing a Resume command, the host driver restores the previously 
saved block count.
 
Although the BLKCNT field is 0 after reset, the read of reset value is 0x1. This is because 
when MSBSEL field is indicating a single block transfer, the read value of BLKCNT is 
always 1.
  NOTE  
0000_0000_0000_0000b - Stop count
0000_0000_0000_0001b - 1 block
0000_0000_0000_0010b - 2 blocks
1111_1111_1111_1111b - 65535 blocks
15-13
—
Reserved
12-0
Transfer block size
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5091 / 5251


---
# 페이지 2232

Table continued from the previous page...
Field
Function
BLKSIZE
This field specifies the block size for block data transfers. Values ranging from 1 byte up to the 
maximum buffer size can be set. It can be accessed only when no transaction is executing (that is, 
after a transaction has stopped). Read operations during transfers may return an invalid value, and write 
operations are ignored.
0_0000_0000_0000b - No data transfer
0_0000_0000_0001b - 1 byte
0_0000_0000_0010b - 2 bytes
0_0000_0000_0011b - 3 bytes
0_0000_0000_0100b - 4 bytes
0_0001_1111_1111b - 511 bytes
0_0010_0000_0000b - 512 bytes
0_1000_0000_0000b - 2048 bytes
1_0000_0000_0000b - 4096 bytes
81.6.1.4
Command Argument (CMD_ARG)
Offset
Register
Offset
CMD_ARG
8h
Function
This register contains the SD/eMMC command argument.
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
CMDARG 
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
CMDARG 
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
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5092 / 5251


---
# 페이지 2233

Fields
Field
Function
31-0
CMDARG
Command argument
The SD/eMMC command argument is specified as bits 39-8 of the command format in the SD or eMMC 
specification. This field is write protected when the Command Inhibit (CMD) field in the Present State 
register is set.
81.6.1.5
Command Transfer Type (CMD_XFR_TYP)
Offset
Register
Offset
CMD_XFR_TYP
Ch
Function
This register is used to control the operation of data transfers. The host driver sets this register before issuing a command followed 
by a data transfer or before issuing a Resume command. To prevent data loss, uSDHC prevents writing to the bits, which are 
involved in the data transfer of this register, when data transfer is active. These fields are DPSEL, MBSEL, DTDSEL, AC12EN, 
BCEN, and DMAEN.
The host driver checks the Command Inhibit DAT field (PRES_STATE[CDIHB]) and the Command Inhibit CMD field 
(PRES_STATE[CIHB]) in the Present State register before writing to this register. When the CDIHB field in the Present 
State register is set, any attempt to send a command with data by writing to this register is ignored; when the CIHB field is set, 
any write to this register is ignored.
On sending commands with data transfer involved, it is mandatory that the block size is non-zero. Block count must also be 
non-zero, or indicated as a single block transfer (bit 5 of this register is '0' when written), or block count is disabled (bit 1 of this 
register is '0' when written), otherwise uSDHC ignores the sending of this command and do nothing. For write command, with all 
above restrictions, it is also mandatory that the write protect switch is not active (PRES_STATE[WPSPL] field of Present State 
register is '1'); otherwise, uSDHC also ignores the command.
If the commands with data transfer do not receive the response in 64 clock cycles, that is, if response time-out happens, uSDHC 
treats the external device, does not accept the command, and aborts the data transfer. In this scenario, the driver should issue 
the command again to retry the transfer. It is also possible that for some reason the card responds to the command but uSDHC 
does not receive the response, and if it is internal DMA (either simple DMA or ADMA) read operation, the external system memory 
is over-written by the internal DMA with data sent back from the card.
The table below shows the summary of how register settings determine the type of data transfer.
Table 816. Transfer type register setting for various transfer types
Multi/single block select
Block count enable
Block count
Function
0
Do not care
Do not care
Single transfer
1
0
Do not care
Infinite transfer
1
1
Positive number
Multiple transfer
1
1
Zero
No data transfer
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5093 / 5251


---
# 페이지 2234

The table below shows the relationship between the Command Index Check Enable and the Command CRC Check Enable, 
regarding the Response Type bits as well as the name of the response type.
Table 817. Relationship between parameters and the name of the response type
Response type
Index check enable
CRC check enable
Name of response type
00
0
0
No response
01
0
1
R2
10
0
0
R3, R4
10
1
1
R1, R5, R6
11
1
1
R1b,R5b
• In the SDIO specification, response type notation for R5b is not defined. R5 includes R5b in the SDIO specification, but 
R5b is defined in this specification to specify that uSDHC checks the busy status after receiving a response. For example, 
usually CMD52 is used with R5, but the I/O abort command is used with R5b.
• The CRC fields for R3 and R4 are expected to be all 1 bits. The CRC check is disabled for these response types.
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
CMDINX 
CMDTYP 
DPSE
L 
CICEN 
CCCE
N 
Reserv
ed 
RSPTYP 
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
AC23E
N 
NIBBL
E_...
MSBS
EL 
DTDS
EL 
DDR_
EN 
AC12E
N 
BCEN 
DMAE
N 
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
CMDINX
Command index
These fields are set to the command number that is specified in bits 45-40 of the command-format in the SD 
Memory Card Physical Layer Specification and SDIO Specification.
23-22
CMDTYP
Command type
There are three types of special commands: Suspend, Resume, and Abort. These fields are set to 00b for 
all other commands.
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5094 / 5251


---
# 페이지 2235

Table continued from the previous page...
Field
Function
• Suspend command: If the Suspend command succeeds, uSDHC assumes that the card bus has 
been released and that it is possible to issue the next command that uses the DATA line. Because 
uSDHC does not monitor the content of command response, it does not know if the Suspend 
command succeeded or not. It is the host driver's responsibility to check the status of the Suspend 
command and send another command marked as Suspend to inform uSDHC that a Suspend 
command was successfully issued. See Suspend Resume for more details. After the end bit of 
command is sent, uSDHC deasserts Read Wait for read transactions and stops checking busy for 
write transactions. In a 4-bit mode, the interrupt cycle starts. If the Suspend command fails, uSDHC 
maintains its current state, and the host driver restarts the transfer by setting the Continue Request 
field in the Protocol Control register.
• Resume command: The host driver re-starts the data transfer by restoring the registers saved before 
sending the Suspend command and then sends the Resume command. The uSDHC module checks 
for a pending busy state before starting write transfers.
• Abort command: If this command is set when executing a read transfer, uSDHC stops reads to the 
buffer. If this command is set when executing a write transfer, uSDHC stops driving the DATA line. 
After issuing the Abort command, the host driver should issue a software reset (Abort Transaction).
00b - Normal other commands
01b - Suspend CMD52 for writing bus suspend in CCCR
10b - Resume CMD52 for writing function select in CCCR
11b - Abort CMD12, CMD52 for writing I/O Abort in CCCR
21
DPSEL
Data present select
This field is set to 1 to indicate that data is present and is transferred using the DATA line. It is set to 0 for 
the following:
• Commands using only the CMD line (for example, CMD52)
• Commands with no data transfer, but using the busy signal on DATA0 line (R1b or R5b (for 
example, CMD38))
 
In resume command, this field is set, and other bits in this register is set the same as when 
the transfer was initially launched. When the write protect switch is on, (that is, the WPSPL 
field is active as '0'), any command with a write operation ignored. When this field is set, 
while the DTDSEL field is 0, writes to the register Transfer Type are ignored.
  NOTE  
0b - No data present
1b - Data present
20
CICEN
Command index check enable
If this field is set to 1, uSDHC checks the Index field in the response to see if it has the same value as the 
command index. If it is not, it is reported as a Command Index Error. If this field is set to 0, the Index field 
is not checked.
0b - Disable command index check
1b - Enables command index check
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5095 / 5251


---
# 페이지 2236

Table continued from the previous page...
Field
Function
19
CCCEN
Command CRC check enable
If this field is set to 1, uSDHC checks the CRC field in the response. If an error is detected, it is reported as 
a Command CRC Error. If this field is set to 0, the CRC field is not checked. The number of bits checked 
by the CRC field value changes according to the length of the response. See RSPTYP[1:0] and Command 
Transfer Type (CMD_XFR_TYP).
0b - Disables command CRC check
1b - Enables command CRC check
18
—
Reserved
17-16
RSPTYP
Response type select
00b - No response
01b - Response length 136
10b - Response length 48
11b - Response length 48, check busy after response
15-8
—
Reserved
7
AC23EN
AC23EN
This field is read when VEND_SPEC[CMD_BYTE_EN] is enabled; otherwise, this field is tied to '0'. When 
this field is set to 1, the host controller issues a CMD23 automatically before issuing a command specified 
in the Command Register.
0b - Disable
1b - Enable
6
NIBBLE_POS
NIBBLE_POS
This field indicates the nibble position in the DDR 4-bit mode. This field is read/write when 
VEND_SPEC[CMD_BYTE_EN] is enabled; otherwise, this field is read-only. 0- the sequence is 'odd 
high nibble -> even high nibble -> odd low nibble -> even low nibble'; 1- the sequence is 'odd high nibble -> 
odd low nibble -> even high nibble -> even low nibble'.
0b - Disable
1b - Enable
5
MSBSEL
MSBSEL
This field enables multiple block DATA line data transfers. This field is read/write when 
VEND_SPEC[CMD_BYTE_EN] is enabled; otherwise, this field is read-only. For any other commands, this 
field can be set to 0. If this field is 0, it is not necessary to set the Block Count register. See Command 
Transfer Type (CMD_XFR_TYP).
0b - Disable
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5096 / 5251


---
# 페이지 2237

Table continued from the previous page...
Field
Function
1b - Enable
4
DTDSEL
DTDSEL
This field defines the direction of DATA line data transfers. This field is read/write when 
VEND_SPEC[CMD_BYTE_EN] is enabled; otherwise, this field is read-only. The field is set to 1 by 
the host driver to transfer data from the SD card to uSDHC and is set to 0 for all other commands.
0b - Disable
1b - Enable
3
DDR_EN
DDR_EN
Dual data rate mode selection. This field is read/write when VEND_SPEC[CMD_BYTE_EN] is enabled; 
otherwise, this field is read-only.
0b - Disable
1b - Enable
2
AC12EN
AC12EN
Multiple block transfers for memory require a CMD12 to stop the transaction. This field is read/write when 
VEND_SPEC[CMD_BYTE_EN] is enabled; otherwise, this field is read-only. When this field is set to 1, 
uSDHC issues a CMD12 automatically when the last block transfer has completed. The host driver is not set 
this field to issue commands that do not require CMD12 to stop a multiple block data transfer. In particular, 
secure commands defined in File Security Specification (see reference list) do not require CMD12. In single 
block transfer, uSDHC ignores this field no matter it is set or not.
0b - Disable
1b - Enable
1
BCEN
BCEN
This field is used to enable the Block Count register, which is only relevant for multiple block transfers. This 
field is read/write when VEND_SPEC[CMD_BYTE_EN] is enabled; otherwise, this field is read-only. When 
this field is 0, the internal counter for block is disabled, which is useful in executing an infinite transfer.
0b - Disable
1b - Enable
0
DMAEN
DMAEN
This field enables DMA functionality. This field is read/write when VEND_SPEC[CMD_BYTE_EN] is 
enabled; otherwise, this field is read-only. If this field is set to 1, a DMA operation begins when the host driver 
sets the DPSEL field of this register. Whether the simple DMA or the advanced DMA is active depends on 
the DMA Select field of the Protocol Control register.
0b - Disable
1b - Enable
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5097 / 5251


---
# 페이지 2238

81.6.1.6
Command Response0 (CMD_RSP0)
Offset
Register
Offset
CMD_RSP0
10h
Function
This register is used to store part 0 of the response bits from the card.
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
CMDRSP0 
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
CMDRSP0 
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
CMDRSP0
Command response 0
See Command Response3 (CMD_RSP3) for the mapping of command responses from the SD bus to this 
field for each response type.
81.6.1.7
Command Response1 (CMD_RSP1)
Offset
Register
Offset
CMD_RSP1
14h
Function
This register is used to store part 1 of the response bits from the card.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5098 / 5251


---
# 페이지 2239

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
CMDRSP1 
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
CMDRSP1 
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
CMDRSP1
Command response 1
See Command Response3 (CMD_RSP3) for the mapping of command responses from the SD bus to this 
field for each response type.
81.6.1.8
Command Response2 (CMD_RSP2)
Offset
Register
Offset
CMD_RSP2
18h
Function
This register is used to store part 2 of the response bits from the card.
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
CMDRSP2 
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
CMDRSP2 
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
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5099 / 5251


---
# 페이지 2240

Fields
Field
Function
31-0
CMDRSP2
Command response 2
See Command Response3 (CMD_RSP3) for the mapping of command responses from the SD bus to this 
field for each response type.
81.6.1.9
Command Response3 (CMD_RSP3)
Offset
Register
Offset
CMD_RSP3
1Ch
Function
This register is used to store part 3 of the response bits from the card.
The table below describes the mapping of command responses from the SD bus to Command Response registers for each 
response type. In this table, R[ ] refers to a bit range within the response data as transmitted on the SD bus.
Table 818. Response bit definition for each response type
Response type
Meaning of response
Response field
Response register
R1,R1b (normal response)
Card status
R[39:8]
CMDRSP0
R1b (auto CMD12 response)
Card status for auto CMD12
R[39:8]
CMDRSP3
R2 (CID, CSD register)
CID/CSD register [127:8]
R[127:8]
{CMDRSP3[23:0],
CMDRSP2,
CMDRSP1,
CMDRSP0}
R3 (OCR register)
OCR register for memory
R[39:8]
CMDRSP0
R4 (OCR register)
OCR register for I/O etc.
R[39:8]
CMDRSP0
R5, R5b
SDIO response
R[39:8]
CMDRSP0
R6 (publish RCA)
New published RCA[31:16] 
and card status[15:0]
R[39:9]
CMDRSP0
This table shows that most responses with a length of 48 (R[47:0]) have 32-bits of the response data (R[39:8]) stored in the 
CMDRSP0 register. Responses of type R1b (Auto CMD12 responses) have response data bits (R[39:8]) stored in the CMDRSP3 
register. Responses with length 136 (R[135:0]) have 120-bits of the response data (R[127:8]) stored in the CMDRSP0, 1, 2, and 
3 registers.
To be able to read the response status efficiently, uSDHC only stores part of the response data in the Command Response 
registers. This enables the host driver to efficiently read 32-bits of response data in one read cycle on a 32-bit bus system. Parts 
of the response, the Index field and the CRC, are checked by uSDHC (as specified by the Command Index Check Enable and the 
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5100 / 5251


---
# 페이지 2241

Command CRC Check Enable bits in the Transfer Type register) and generate an error interrupt if any error is detected. The bit 
range for the CRC check depends on the response length. If the response length is 48, uSDHC checks R[47:1], and if the response 
length is 136 the uSDHC checks R[119:1].
Because uSDHC may have a multiple block data transfer executing concurrently with a CMD_wo_DAT command, uSDHC stores 
the Auto CMD12 response in the CMDRSP3 register. The CMD_wo_DAT response is stored in CMDRSP0. This allows uSDHC to 
avoid overwriting the Auto CMD12 response with the CMD_wo_DAT and vice versa. When uSDHC modifies part of the Command 
Response registers, as shown in the table above, it preserves the unmodified bits.
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
CMDRSP3 
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
CMDRSP3 
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
CMDRSP3
Command response 3
See Command Response3 (CMD_RSP3) for the mapping of command responses from the SD bus to this 
field for each response type.
81.6.1.10
Data Buffer Access Port (DATA_BUFF_ACC_PORT)
Offset
Register
Offset
DATA_BUFF_ACC_POR
T
20h
Function
The Buffer Data Port register is for 32-bit data access by the Arm platform or the external DMA. When the internal DMA is enabled, 
any write to this field is ignored, and any read from this field always yields 0s.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5101 / 5251


---
# 페이지 2242

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
DATCONT 
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
DATCONT 
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
DATCONT
Data content
This field is used to access the internal buffer.
81.6.1.11
Present State (PRES_STATE)
Offset
Register
Offset
PRES_STATE
24h
Function
The host driver can get status of uSDHC from this 32-bit read only register.
The host driver can issue CMD0, CMD12, CMD13 (for memory) and CMD52 (for SDIO) when the DATA lines are busy during a 
data transfer. These commands can be issued when Command Inhibit (CMD) is set to zero. Other commands are issued when 
Command Inhibit (DATA) is set to zero. Possible changes to the SD Physical Specification may add other commands to this list 
in the future.
 
The reset value of Present State register depends on board connectivity.
  NOTE  
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5102 / 5251


---
# 페이지 2243

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
DLSL 
CLSL 
0
WPSP
L 
Reserv
ed 
0
CINST 
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
0
0
0
u
u
0
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
0
0
BREN 
BWEN 
RTA 
WTA 
Reserved 
SDST
B 
DLA 
CDIHB 
CIHB 
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
1
0
0
0
u
0
0
0
Fields
Field
Function
31-24
DLSL
DATA[7:0] line signal level
This field is used to check the DATA line level to recover from errors, and for debugging. This is especially 
useful in detecting the busy signal level from DATA0. The reset value is affected by the external pull-up / 
pull-down resistors. By default, the read value of this field after reset is 8'b11110111, when DATA3 is pulled 
down and the other lines are pulled up.
0000_0000b - Data 0 line signal level
0000_0001b - Data 1 line signal level
0000_0010b - Data 2 line signal level
0000_0011b - Data 3 line signal level
0000_0100b - Data 4 line signal level
0000_0101b - Data 5 line signal level
0000_0110b - Data 6 line signal level
0000_0111b - Data 7 line signal level
23
CLSL
CMD line signal level
This field is used to check the CMD line level to recover from errors, and for debugging. The reset value is 
affected by the external pull-up / pull-down resistor, by default, the read value of this field after reset is 1'b1, 
when the command line is pulled up.
22-20
—
Reserved
19
WPSPL
Write protect switch pin level
The Write Protect switch is supported for memory and combo cards. This field reflects the inverted value of 
the WP pin of the card socket. A software reset does not affect this field. The reset value is affected by the 
external write protect switch. If the WP pin is not used, it should be tied low, so that the reset value of this 
field is high and write is enabled.
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5103 / 5251


---
# 페이지 2244

Table continued from the previous page...
Field
Function
0b - Write protected (WP = 1)
1b - Write enabled (WP = 0)
18
—
Reserved
17
—
Reserved
16
CINST
Card inserted
This field indicates whether a card has been inserted. The uSDHC module debounces this signal so that 
the host driver does not need to wait for it to stabilize. Changing from a 0 to 1 generates a Card Insertion 
interrupt in the Interrupt Status register. Changing from a 1 to 0 generates a Card Removal interrupt in the 
Interrupt Status register. A write to the Force Event Register does not affect this field.
The Software Reset For All in the System Control register does not affect this field. A software reset does 
not affect this field.
0b - Power on reset or no card
1b - Card inserted
15-13
—
Reserved
12
—
Reserved
11
BREN
Buffer read enable
This status field is used for non-DMA read transfers. The uSDHC module implements an internal buffer to 
transfer data efficiently. This read only flag indicates that valid data exists in the host side buffer. If this field 
is high, valid data greater than the watermark level exist in the buffer. A change of this field from 1 to 0 occurs 
when some reads from the buffer (read DATPORT (Base + 0x20)) are made and the buffer hasn't valid data 
greater than the watermark level. A change of this field from 0 to1 occurs when there is enough valid data 
ready in the buffer and the Buffer Read Ready interrupt has been generated and enabled.
0b - Read disable
1b - Read enable
10
BWEN
Buffer write enable
This status field is used for non-DMA write transfers. The uSDHC module implements an internal buffer to 
transfer data efficiently. This read only flag indicates if space is available for write data. If this field is 1, valid 
data greater than the watermark level can be written to the buffer. A change of this field from 1 to 0 occurs 
when some writes to the buffer (write DATPORT (Base + 0x20)) are made and the buffer hasn't valid space 
greater than the watermark level. A change of this field from 0 to 1 occurs when the buffer can hold valid 
data greater than the write watermark level and the Buffer Write Ready interrupt is generated and enabled.
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5104 / 5251


---
# 페이지 2245

Table continued from the previous page...
Field
Function
0b - Write disable
1b - Write enable
9
RTA
Read transfer active
This status field is used for detecting completion of a read transfer.
This field is set for either of the following conditions:
• After the end field of the read command
• When writing a 1 to the Continue Request field in the Protocol Control register to restart a read 
transfer
A transfer complete interrupt is generated when this field changes to 0. This field is cleared for either of the 
following conditions:
• When the last data block as specified by block length is transferred to the System, that is, all data 
are read away from uSDHC internal buffer.
• When all valid data blocks have been transferred from uSDHC internal buffer to the System and no 
current block transfers are being sent because of the Stop At Block Gap Request being set to 1.
0b - No valid data
1b - Transferring data
8
WTA
Write transfer active
This status field indicates a write transfer is active. If this field is 0, it means no valid write data exists 
in uSDHC.
This field is set in either of the following cases:
• After the end field of the write command
• When writing 1 to the Continue Request field in the Protocol Control register to restart a write 
transfer
This field is cleared in either of the following cases:
• After getting the CRC status of the last data block as specified by the transfer count (Single and 
Multiple)
• After getting the CRC status of any block where data transmission is about to be stopped by a Stop 
At Block Gap Request
During a write transaction, a Block Gap Event interrupt is generated when this field is changed to 0, as result 
of the Stop At Block Gap Request being set. This status is useful for the host driver in determining when to 
issue commands during Write Busy state.
0b - No valid data
1b - Transferring data
7-4
—
Reserved
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5105 / 5251


---
# 페이지 2246

Table continued from the previous page...
Field
Function
3
SDSTB
SD clock stable
This status field indicates that the internal card clock is stable. This field is for the host driver to poll clock 
status when changing the clock frequency. It is recommended to clear FRC_SDCLK_ON field in System 
Control register to remove glitches on the card clock when the frequency is changing.
Before changing clock divisor value (SDCLKFS or DVS), host driver should make sure the SDSTB field 
is high.
0b - Clock is changing frequency and not stable.
1b - Clock is stable.
2
DLA
Data line active
This status field indicates whether one of the DATA lines on the SD bus is in use.
In the case of read transactions:
This status indicates if a read transfer is executing on the SD bus. Changes in this value from 1 to 0, between 
data blocks, generates a Block Gap Event interrupt in the Interrupt Status register.
This field is set in either of the following cases:
• After the end field of the read command
• When writing a 1 to the Continue Request field in the Protocol Control register to restart a read 
transfer
This field is cleared in either of the following cases:
• When the end field of the last data block is sent from the SD bus to uSDHC.
• When the Read Wait state is stopped by a Suspend command and the DATA2 line is released.
The uSDHC module waits at the next block gap by driving Read Wait at the start of the interrupt cycle. If the 
Read Wait signal is already driven (data buffer cannot receive data), uSDHC can wait for a current block 
gap by continuing to drive the Read Wait signal. It is necessary to support Read Wait to use the suspend / 
resume function. This field remains 1 during Read Wait.
In the case of write transactions:
This status indicates that a write transfer is executing on the SD bus. Changes in this value from 1 to 0 
generate a Transfer Complete interrupt in the Interrupt Status register.
This field is set in either of the following cases:
• After the end field of the write command
• When writing to 1 to the Continue Request field in the Protocol Control register to continue a write 
transfer
This field is cleared in either of the following cases:
• When the SD card releases Write Busy of the last data block, uSDHC also detects if the output is 
not busy. If the SD card does not drive the busy signal after the CRC status is received, uSDHC 
assumes the card drive "Not Busy".
• When the SD card releases write busy, prior to waiting for write transfer, and because of a Stop At 
Block Gap Request.
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5106 / 5251


---
# 페이지 2247

Table continued from the previous page...
Field
Function
In the case of command with busy pending:
This status indicates that a busy state follows the command and the data line is in use. This field is cleared 
when the DATA0 line is released.
0b - DATA line inactive
1b - DATA line active
1
CDIHB
Command Inhibit Data (DATA)
This status field is generated if either the DAT Line Active or the Read Transfer Active is set to 1. If this 
field is 0, it indicates that uSDHC can issue the next SD / eMMC Command. Commands with a busy signal 
belong to Command Inhibit (DATA) (for example. R1b, R5b type). Changing from 1 to 0 generates a Transfer 
Complete interrupt in the Interrupt Status register.
 
The SD host driver can save registers for a suspend transaction after this field has changed 
from 1 to 0.
  NOTE  
0b - Can issue command that uses the DATA line
1b - Cannot issue command that uses the DATA line
0
CIHB
Command inhibit (CMD)
If this status bit is 0, it indicates that the CMD line is not in use and uSDHC can issue a SD / eMMC command 
using the CMD line.
This field is set also immediately after the Transfer Type register is written. This field is cleared when the 
command response is received. Even if the Command Inhibit (DATA) is set to 1, commands using only the 
CMD line can be issued if this field is 0. Changing from 1 to 0 generates a Command Complete interrupt in 
the Interrupt Status register. If uSDHC cannot issue the command because of a command conflict error (see 
Command CRC Error) or because of a Command Not Issued By Auto CMD12 Error, this field remains 1 and 
the Command Complete is not set. The Status of issuing an auto CMD12 does not show on this field.
0b - Can issue command using only CMD line
1b - Cannot issue command
81.6.1.12
Protocol Control (PROT_CTRL)
Offset
Register
Offset
PROT_CTRL
28h
Function
This register controls three cases to restart the transfer after stop at the block gap. Which case is appropriate depends on whether 
uSDHC issues a Suspend command or the SD card accepts the Suspend command.
• If the host driver does not issue a Suspend command, the Continue request is used to restart the transfer.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5107 / 5251


---
# 페이지 2248

• If the host driver issues a Suspend command and the SD card accepts it, a Resume command is used to restart the 
transfer.
• If the host driver issues a Suspend command and the SD card does not accept it, the Continue request is used to restart 
the transfer.
Any time stop at block gap request stops the data transfer, the host driver waits for a Transfer Complete (in the Interrupt Status 
register), before attempting to restart the transfer. When restarting the data transfer by Continue Request, the host driver clears 
the Stop At Block Gap Request before or simultaneously.
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
NON_
EXA...
BURST_LEN_EN 
WECR
M 
WECI
NS 
WECI
NT 
Reserved 
RD_D
ONE...
IABG 
RWCT
L 
CREQ 
SABG
REQ 
W
Reset
0
0
0
0
1
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
DMASEL 
Reserv
ed 
Reserv
ed 
EMODE 
D3CD 
DTW 
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
1
0
0
0
0
0
Fields
Field
Function
31
—
Reserved
Always write as 0
30
NON_EXACT_B
LK_RD
Non-exact block read
Current block read is non-exact block read. It is only used for SDIO.
0b - The block read is exact block read. Host driver does not need to issue abort command to 
terminate this multi-block read.
1b - The block read is non-exact block read. Host driver needs to issue abort command to 
terminate this multi-block read.
29-27
BURST_LEN_E
N
BURST length enable for INCR, INCR4 / INCR8 / INCR16, INCR4-WRAP / INCR8-WRAP / INCR16-WRAP
This field is used to enable or disable the burst length for the external AHB2AXI bridge. It is useful especially 
for INCR transfer because without burst length indicator, the AHB2AXI bridge does not know the burst length 
in advance. Without burst length indicator, AHB INCR transfers can only be converted to SINGLEs on the 
AXI side.
1xxb - Burst length is enabled for INCR4-WRAP / INCR8-WRAP / INCR16-WRAP.
x1xb - Burst length is enabled for INCR4 / INCR8 / INCR16.
xx1b - Burst length is enabled for INCR.
26
WECRM
Wakeup event enable on SD card removal
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5108 / 5251


---
# 페이지 2249

Table continued from the previous page...
Field
Function
This field enables a wakeup event, via a card removal, in the Interrupt Status register. FN_WUS (Wakeup 
Support) in CIS does not affect this field. When this field is set, the Card Removal Status and uSDHC 
interrupt can be asserted without CLK toggling. When the wakeup feature is not enabled, the CLK must be 
active to assert the Card Removal Status and uSDHC interrupt.
0b - Disables wakeup event enable on SD card removal
1b - Enables wakeup event enable on SD card removal
25
WECINS
Wakeup event enable on SD card insertion
This field enables a wakeup event, via a card insertion, in the Interrupt Status register. FN_WUS (Wakeup 
Support) in CIS does not affect this field. When this field is set, the Card Insertion Status and uSDHC 
interrupt can be asserted without CLK toggling. When the wakeup feature is not enabled, the CLK must be 
active to assert the Card Insertion Status and uSDHC interrupt.
0b - Disable wakeup event enable on SD card insertion
1b - Enable wakeup event enable on SD card insertion
24
WECINT
Wakeup event enable on card interrupt
This field enables a wakeup event, via a card interrupt, in the Interrupt Status register. This field can be set 
to 1 if FN_WUS (Wakeup Support) in CIS is set to 1. When this field is set, the Card Interrupt Status and 
uSDHC interrupt can be asserted without CLK toggling. When the wakeup feature is not enabled, the CLK 
must be active to assert the Card Interrupt Status and uSDHC interrupt.
0b - Disables wakeup event enable on card interrupt
1b - Enables wakeup event enable on card interrupt
23-21
—
Reserved
Always write as 3'b100
20
RD_DONE_NO
_8CLK
Read performed number 8 clock
According to the SD/eMMC spec, for read data transaction, 8 clocks are needed after the end field of the 
last data block. So, by default(RD_DONE_NO_8CLK=0), eight clocks are active after the end field of the last 
read data transaction.
However, these 8 clocks should not be active if user wants to use stop at block gap (include the auto stop at 
block gap in boot mode) feature for read and the RWCTL field (bit18) is not enabled. In this case, software 
should set RD_DONE_NO_8CLK to avoid these 8 clocks. Otherwise, the device might send extra data to 
uSDHC while uSDHC ignores these data.
In a summary, this field should be set only if the use case needs to use stop at block gap feature while the 
device can't support the read wait feature.
19
IABG
Interrupt at block gap
This field is valid only in 4-bit mode, of SDIO, and selects a sample point in the interrupt cycle. Setting to 
1 enables interrupt detection at the block gap for a multiple block transfer. Setting to 0 disables interrupt 
detection during a multiple block transfer. If SDIO cannot signal an interrupt during a multiple block transfer, 
this field should be set to 0 to avoid an inadvertent interrupt. When the host driver detects an SDIO insertion, 
it sets this field according to the CCCR of the card.
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5109 / 5251


---
# 페이지 2250

Table continued from the previous page...
Field
Function
0b - Disables interrupt at block gap
1b - Enables interrupt at block gap
18
RWCTL
Read wait control
The read wait function provided by this field is optional for SDIO. If the card supports read wait, set this field 
to enable use of the read wait protocol to stop read data using the DATA2 line. Otherwise, uSDHC has to 
stop the SD clock to hold read data, which restricts commands generation. When the host driver detects an 
SDIO insertion, it sets this field according to the CCCR of the card. If the card does not support read wait, this 
field should never be set to 1; otherwise, DATA line conflicts might occur. If this field is set to 0, stop at block 
gap during read operation is also supported, but uSDHC stops the SD clock to pause reading operation.
0b - Disables read wait control and stop SD clock at block gap when SABGREQ field is set
1b - Enables read wait control and assert read wait without stopping SD clock at block gap when 
SABGREQ field is set
17
CREQ
Continue request
This field is used to restart a transaction which was stopped using the stop at block gap request. When a 
suspend operation is not accepted by the card, it is also by setting this field to restart the paused transfer. To 
cancel stop at the block gap, set stop at block gap request to 0 and set this field to 1 to restart the transfer.
The uSDHC module automatically clears this field, therefore it is not necessary for the host driver to set this 
field to 0. If both stop at block gap request and this field are 1, the continue request is ignored.
0b - No effect
1b - Restart
16
SABGREQ
Stop at block gap request
This field is used to stop executing a transaction at the next block gap for both DMA and non-DMA transfers. 
Until the transfer complete is set to 1, indicating a transfer completion, the host driver leaves this field set 
to 1. Clearing both the stop at block gap request and continue request does not cause the transaction to 
restart. Read Wait is used to stop the read transaction at the block gap. The uSDHC module supports the 
stop at block gap request for write transfers, but for read transfers it requires that SDIO support read wait. 
Therefore, the host driver does not set this field during read transfers unless SDIO supports Read Wait and 
has set the read wait control to 1; otherwise, uSDHC stops the SD bus clock to pause the read operation 
during block gap. In the case of write transfers in which the host driver writes data to the Data Port register, 
the host driver sets this field after all block data is written. If this field is set to 1, the host driver does not 
write data to the Data Port register after a block is sent. Once this field is set, the host driver does not clear 
this field before the Transfer Complete field in Interrupt Status register is set, otherwise uSDHC's behavior 
is undefined.
This field effects read transfer active, write transfer active, DATA Line Active and Command Inhibit (DATA) 
in the Present State register.
0b - Transfer
1b - Stop
15-10
—
Reserved
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5110 / 5251


---
# 페이지 2251

Table continued from the previous page...
Field
Function
9-8
DMASEL
DMA select
This field is valid while DMA (SDMA or ADMA) is enabled and selects the DMA operation.
00b - No DMA or simple DMA is selected.
01b - ADMA1 is selected.
10b - ADMA2 is selected.
11b - Reserved
7
—
Reserved
6
—
Reserved
5-4
EMODE
Endian mode
This field supports all three endian modes in data transfer. See Data buffer for more details.
00b - Big endian mode
01b - Half word big endian mode
10b - Little endian mode
11b - Reserved
3
D3CD
DATA3 as card detection pin
If this field is set, DATA3 should be pulled down to act as a card detection pin. Be cautious when using this 
feature, because DATA3 is also a chip-select for the SPI mode. A pull-down on this pin and CMD0 might 
set the card into the SPI mode, which uSDHC does not support.
0b - DATA3 does not monitor card insertion
1b - DATA3 as card detection pin
2-1
DTW
Data transfer width
This field selects the data width of the SD bus for a data transfer. The host driver sets it to match the data 
width of the card. Possible data transfer width is 1-bit, 4-bits or 8-bits.
00b - 1-bit mode
01b - 4-bit mode
10b - 8-bit mode
11b - Reserved
0
—
Reserved
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5111 / 5251


---
# 페이지 2252

81.6.1.13
System Control (SYS_CTRL)
Offset
Register
Offset
SYS_CTRL
2Ch
Function
This register provides control of the system. See detail in the field description.
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
INITA 
RSTD 
RSTC 
RSTA 
IPP_R
ST...
RST_
FIFO 
Reserv
ed 
0
DTOCV 
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
1
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
SDCLKFS 
DVS 
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
1
1
1
1
Fields
Field
Function
31-28
—
Reserved
27
INITA
Initialization active
When this field is set, 80 SD-clocks are sent to the card. After the 80 clocks are sent, this field is self cleared. 
This field is very useful during the card power-up period when 74 SD-clocks are needed and the clock auto 
gating feature is enabled. Writing 1 to this bit when this field is already 1 has no effect. Writing 0 to this field 
at any time has no effect. When either of the CIHB and CDIHB fields in the Present State register are set, 
writing 1 to this field is ignored (that is, when command line or data lines are active, write to this field is not 
allowed). On the other-hand, when this field is set, that is, during initialization active period, it is allowed to 
issue command, and the command bit stream appears on the CMD pad after all 80 clock cycles are done. 
So, when this command ends, the driver can make sure the 80 clock cycles are sent out. This is very useful 
when the driver needs to send 80 cycles to the card and does not want to wait till this field is self cleared.
26
RSTD
Software reset for data line
Only part of the data circuit is reset. DMA circuit is also reset. After this field is set, the software waits 
for self-clear.
The following registers and bits are cleared by this field:
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5112 / 5251


---
# 페이지 2253

Table continued from the previous page...
Field
Function
• Data Port register
— Buffer is cleared and initialized
• Present State register
— Buffer read enable
— Buffer write enable
— Read transfer active
— Write transfer active
— DATA line active
— Command Inhibit (DATA)
• Protocol Control register
— Continue request
• Interrupt Status register
— Buffer read ready
— Buffer write ready
— DMA interrupt
— Block gap event
— Transfer complete
 
When reset, the software must make sure there is no incomplete data transferring. If there 
is data transfer going on, the software needs to wait TC or DC INT_STATUS register is set.
  NOTE  
0b - No reset
1b - Reset
25
RSTC
Software reset for CMD line
Only part of the command circuit is reset. After this field is set, the software waits for self-clear.
The following registers and bits are cleared by this field:
• Present State Register
— Command Inhibit (CMD)
• Interrupt Status Register
— Command Complete
0b - No reset
1b - Reset
24
RSTA
Software reset for all
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5113 / 5251


---
# 페이지 2254

Table continued from the previous page...
Field
Function
This reset affects the entire host controller except for the card detection circuit. RSTA resets all the registers 
that can be reset by RSTC/RSTD. During its initialization, the host driver is set this field to 1 to reset uSDHC. 
The uSDHC module resets this field to 0 when the capabilities registers are valid and the host driver can 
read them. Additional use of Software Reset For All does not affect the value of the capabilities registers. 
After this field is set, it is recommended that the host driver reset the external card and re-initialize it. After 
this field is set, the software should wait for self-clear.
 
When reset, the software must make sure there is no incomplete data transferring. If there 
is data transfer going on, the software needs to wait TC or DC INT_STATUS register is set.
  NOTE  
0b - No reset
1b - Reset
23
IPP_RST_N
Hardware reset
This field's value is output to card through pad directly to hardware reset pin of the card if the card supports 
this feature.
22
RST_FIFO
Reset the async FIFO
Reset the async FIFO between card interface and the internal logic. After this field is set, the software waits 
for self-clear.
21
—
Reserved
20
—
Reserved
19-16
DTOCV
Data timeout counter value
This value determines the interval by which DAT line timeouts are detected. See the Data Timeout Error 
field in the Interrupt Status register for information on factors that dictate time-out generation. Time-out clock 
frequency is generated by dividing the base clock SDCLK value by this value.
The host driver can clear the Data Timeout Error Status Enable (in the Interrupt Status Enable register) to 
prevent inadvertent time-out events.
0000b - SDCLK x 2 14
0001b - SDCLK x 2 15
0010b - SDCLK x 2 16
0011b - SDCLK x 2 17
0100b - SDCLK x 2 18
0101b - SDCLK x 2 19
0110b - SDCLK x 2 20
0111b - SDCLK x 2 21
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5114 / 5251


---
# 페이지 2255

Table continued from the previous page...
Field
Function
1000b - SDCLK x 2 22
1001b - SDCLK x 2 23
1010b - SDCLK x 2 24
1011b - SDCLK x 2 25
1100b - SDCLK x 2 26
1101b - SDCLK x 2 27
1110b - SDCLK x 2 28
1111b - SDCLK x 2 29
15-8
SDCLKFS
SDCLK frequency select
This field is used to select the frequency of the SDCLK pin. The frequency is not programmed directly, 
rather this field holds the prescaler (of this register) and divisor (next register) of the Base Clock 
Frequency register.
In Single Data Rate mode (DDR_EN field of MIXERCTRL is '0')
Only the following settings are allowed:
80h) Base clock divided by 256
40h) Base clock divided by 128
20h) Base clock divided by 64
10h) Base clock divided by 32
08h) Base clock divided by 16
04h) Base clock divided by 8
02h) Base clock divided by 4
01h) Base clock divided by 2
00h) Base clock divided by 1
While in Dual Data Rate mode (DDR_EN field of MIXERCTRL is '1')
Only the following settings are allowed:
80h) Base clock divided by 512
40h) Base clock divided by 256
20h) Base clock divided by 128
10h) Base clock divided by 64
08h) Base clock divided by 32
04h) Base clock divided by 16
02h) Base clock divided by 8
01h) Base clock divided by 4
00h) Base clock divided by 2
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5115 / 5251


---
# 페이지 2256

Table continued from the previous page...
Field
Function
When the software changes the DDR_EN field, SDCLKFS might need to be changed also.
In Single Data Rate mode, setting 00h bypasses the frequency prescaler of the SD clock.
Multiple bits must not be set, or the behavior of this prescaler is undefined. The two default divider values 
can be calculated by the frequency of ipg_perclk and the following Divisor bits.
The frequency of SDCLK is set by the following formula:
Clock Frequency = (Base Clock) / (prescaler x divisor)
For example, in Single Data Rate mode, if the Base Clock Frequency is 96 MHz, and the target frequency is 
25 MHz, then choosing the prescaler value of 01h and divisor value of 1h yields 24 MHz, which is the nearest 
frequency less than or equal to the target. Similarly, to approach a clock value of 400 kHz, the prescaler 
value of 08h and divisor value of eh yields the exact clock value of 400 kHz.
The reset value of this field is 80h, so if the input Base Clock (ipg_perclk) is about 96 MHz, the default SD 
clock after reset is 375 kHz.
Before changing clock divisor value (SDCLKFS or DVS), host driver should make sure the SDSTB field 
is high.
If setting SDCLKFS and DVS can generate the same clock frequency,(for example, in SDR mode, 
SDCLKFS = 01h is same as DVS = 01h.), SDCLKFS is highly recommended.
7-4
DVS
Divisor
This field is used to provide a more exact divisor to generate the desired SD clock frequency. Note the 
divider can even support odd divisors without deterioration of duty cycle.
Before changing clock divisor value (SDCLKFS or DVS), Host driver should make sure the SDSTB field 
is high.
The settings are as follows:
0000b - Divide-by-1
0001b - Divide-by-2
1110b - Divide-by-15
1111b - Divide-by-16
3-0
—
Reserved
Always write as 1.
81.6.1.14
Interrupt Status (INT_STATUS)
Offset
Register
Offset
INT_STATUS
30h
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5116 / 5251


---
# 페이지 2257

Function
An interrupt is generated when the normal interrupt signal enable is enabled and at least one of the status fields is set to 1. For all 
fields, writing 1 to a bit clears it; writing to 0 keeps the bit unchanged. More than one status can be cleared with a single register 
write. For card interrupt, before writing 1 to clear, it is required that the card stops asserting the interrupt, meaning that when the 
card driver services the interrupt condition; otherwise, the CINT field is asserted again.
The table below shows the relationship between the command timeout error and the command complete.
Table 819. uSDHC status for command timeout error/command complete bit combinations
Command complete
Command timeout error
Meaning of the status
0
0
X
X
1
Response not received within 64 SDCLK cycles
1
0
Response received
The table below shows the relationship between the transfer complete and the data timeout error.
Table 820. uSDHC status for data timeout error/transfer complete bit combinations
Transfer complete
Data timeout error
Meaning of the status
0
0
X
0
1
Timeout occurred during transfer
1
X
Data transfer complete
The table below shows the relationship between the command CRC error and command timeout error.
Table 821. uSDHC status for command CRC error/command timeout error bit combinations
Command CRC error
Command timeout error
Meaning of the status
0
0
No error
0
1
Response timeout error
1
0
Response CRC error
1
1
CMD line conflict
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5117 / 5251


---
# 페이지 2258

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
DMAE 
0
0
0
AC12E 
0
DEBE 
DCE 
DTOE 
CIE 
CEBE 
CCE 
CTOE 
W
W1C
W1C
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
ERR_I
NT...
0
0
0
0
Reserved 
CINT 
CRM 
CINS 
BRR 
BWR 
DINT 
BGE 
TC 
CC 
W
W1C
W1C
W1C
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
0
Fields
Field
Function
31
—
Reserved
30-29
—
Reserved
28
DMAE
DMA error
Occurs when an Internal DMA transfer has failed. This field is set to 1, when some error occurs in the data 
transfer. This error can be caused by either simple DMA or ADMA, depending on which DMA is in use. 
The value in DMA System Address register is the next fetch address where the error occurs. Because any 
error corrupts the whole data block, the host driver restarts the transfer from the corrupted block boundary. 
The address of the block boundary can be calculated either from the current DS_ADDR value or from the 
remaining number of blocks and the block size.
0b - No error
1b - Error
27
—
Reserved
26
—
Reserved
25
—
Reserved
24
AC12E
Auto CMD12 error
Occurs when detecting that one of the fields in the Auto CMD12 Error Status register has changed from 0 
to 1. This field is set to 1, not only when the errors in Auto CMD12 occur, but also, when the Auto CMD12 
is not executed due to the previous command error.
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5118 / 5251


---
# 페이지 2259

Table continued from the previous page...
Field
Function
0b - No error
1b - Error
23
—
Reserved
22
DEBE
Data end bit error
Occurs either when detecting 0 at the end field position of read data that uses the DATA line, or at the end 
field position of the CRC.
0b - No error
1b - Error
21
DCE
Data CRC error
Occurs when detecting a CRC error when transferring read data that uses the DATA line, or when detecting 
the Write CRC status having a value other than 010.
0b - No error
1b - Error
20
DTOE
Data timeout error
Occurs when detecting one of following time-out conditions.
• Busy time-out for R1b, R5b type
• Busy time-out after Write CRC status
• Read Data time-out.
0b - No error
1b - Time out
19
CIE
Command index error
Occurs if a command index error occurs in the command response.
0b - No error
1b - Error
18
CEBE
Command end bit error
Occurs when detecting that the end field of a command response is 0.
0b - No error
1b - End bit error generated
17
CCE
Command CRC error
Command CRC Error is generated in two cases.
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5119 / 5251


---
# 페이지 2260

Table continued from the previous page...
Field
Function
• If a response is returned and the Command Timeout Error is set to 0 (indicating no time-out), this 
field is set when detecting a CRC error in the command response.
• The uSDHC module detects a CMD line conflict by monitoring the CMD line when a command is 
issued. If uSDHC drives the CMD line to 1, but detects 0 on the CMD line at the next SDCLK edge, 
then uSDHC aborts the command (Stop driving CMD line) and set this bit to 1. The Command 
Timeout Error should also be set to 1 to distinguish CMD line conflict.
0b - No error
1b - CRC error generated
16
CTOE
Command timeout error
Occurs only if no response is returned within 64 SDCLK cycles from the end field of the command. If uSDHC 
detects a CMD line conflict, in which case a Command CRC Error is also be set (as shown in Interrupt 
Status (INT_STATUS)), this field is set without waiting for 64 SDCLK cycles. This is because the command 
is aborted by uSDHC.
0b - No error
1b - Time out
15
ERR_INT_STA
TUS
Error Interrupt Status
This bit is set when any of the error status bit DMAE, AC12E, DEBE, DCE, DTOE, CIE, CEBE, CCE and 
CTOE is set.
14
—
Reserved
13
—
Reserved
12
—
Reserved
11
—
Reserved
10-9
—
Reserved
8
CINT
Card interrupt
This status field is set when an interrupt signal is detected from the external card. In 1-bit mode, uSDHC 
detects the Card Interrupt without the SD clock to support wakeup. In 4-bit mode, the card interrupt signal 
is sampled during the interrupt cycle, so the interrupt from card can only be sampled during interrupt cycle, 
introducing some delay between the interrupt signal from SDIO and the interrupt to the host system. Writing 
this field to 1 can clear this field, but as the interrupt source from SDIO does not clear, this field is set again. 
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5120 / 5251


---
# 페이지 2261

Table continued from the previous page...
Field
Function
to clear this field, it is required to reset the interrupt source from the external card followed by a writing 1 to 
this field.
When this status has been set, and the host driver needs to service this interrupt, the Card Interrupt Signal 
Enable in the Interrupt Signal Enable register should be 0 to stop driving the interrupt signal to the host 
system. After completion of the card interrupt service (It should reset the interrupt sources in SDIO and the 
interrupt signal might not be asserted), write 1 to clear this field, set the Card Interrupt Signal Enable to 1, 
and start sampling the interrupt signal again.
0b - No card interrupt
1b - Generate card interrupt
7
CRM
Card removal
This status field is set if the Card Inserted field in the Present State register changes from 1 to 0. When the 
host driver writes this field to 1 to clear this status, the status of the Card Inserted in the Present State register 
should be confirmed. Because the card state might possibly be changed when the host driver clears this field 
and the interrupt event might not be generated. When this field is cleared, it is set again if no card is inserted. 
to leave it cleared, clear the Card Removal Status Enable field in Interrupt Status Enable register.
0b - Card state unstable or inserted
1b - Card removed
6
CINS
Card insertion
This status field is set if the Card Inserted field in the Present State register changes from 0 to 1. When the 
host driver writes this field to 1 to clear this status, the status of the Card Inserted in the Present State register 
should be confirmed. Because the card state might possibly be changed when the host driver clears this field 
and the interrupt event might not be generated. When this field is cleared, it is set again if a card is inserted. 
to leave it cleared, clear the Card Inserted Status Enable field in Interrupt Status Enable register.
0b - Card state unstable or removed
1b - Card inserted
5
BRR
Buffer read ready
This status field is set if the Buffer Read Enable field, in the Present State register, changes from 0 to 1. See 
the Buffer Read Enable field in the Present State register for additional information.
0b - Not ready to read buffer
1b - Ready to read buffer
4
BWR
Buffer write ready
This status field is set if the Buffer Write Enable field, in the Present State register, changes from 0 to 1. See 
the Buffer Write Enable field in the Present State register for additional information.
0b - Not ready to write buffer
1b - Ready to write buffer
3
DMA interrupt
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5121 / 5251


---
# 페이지 2262

Table continued from the previous page...
Field
Function
DINT
Occurs only when the internal DMA finishes the data transfer successfully. Whenever errors occur during 
data transfer, this field does not be set. Instead, the DMAE field is set. Either Simple DMA or ADMA finishes 
data transferring, this field is set.
0b - No DMA interrupt
1b - DMA interrupt is generated.
2
BGE
Block gap event
If the Stop At Block Gap Request field in the Protocol Control register is set, this field is set when a read or 
write transaction is stopped at a block gap. If Stop At Block Gap Request is not set to 1, this field is not set 
to 1.
In the case of a Read Transaction: This field is set at the falling edge of the DATA Line Active Status (When 
the transaction is stopped at SD bus timing). The Read Wait must be supported to use this function.
In the case of Write Transaction: This field is set at the falling edge of Write Transfer Active Status (After 
getting CRC status at SD Bus timing).
0b - No block gap event
1b - Transaction stopped at block gap
1
TC
Transfer complete
This field is set when a read or write transfer is completed.
In the case of a Read Transaction: This field is set at the falling edge of the Read Transfer Active Status. 
There are two cases in which this interrupt is generated. The first is when a data transfer is completed as 
specified by the data length (after the last data has been read to the host system). The second is when data 
has stopped at the block gap and completed the data transfer by setting the Stop At Block Gap Request field 
in the Protocol Control register (after valid data has been read to the host system).
In the case of a Write Transaction: This field is set at the falling edge of the DATA Line Active Status. There 
are two cases in which this interrupt is generated. The first is when the last data is written to the SD card as 
specified by the data length and the busy signal is released. The second is when data transfers are stopped 
at the block gap, by setting the Stop At Block Gap Request field in the Protocol Control register, and the data 
transfers are completed. (after valid data is written to the SD card and the busy signal released).
In the case of a command with busy, this field is set when busy is deasserted.
0b - Transfer does not complete
1b - Transfer complete
0
CC
Command complete
This field is set when you receive the end field of the command response (except auto CMD12). See the 
Command Inhibit (CMD) in the Present State register.
0b - Command not complete
1b - Command complete
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5122 / 5251


---
# 페이지 2263

81.6.1.15
Interrupt Status Enable (INT_STATUS_EN)
Offset
Register
Offset
INT_STATUS_EN
34h
Function
Setting any bit in this register to 1 enables the corresponding interrupt status be requested to the system. If any bit is set to 0, the 
corresponding interrupt request gets blocked.
• Depending on IABG field setting, uSDHC might be programmed to sample the card interrupt signal during the interrupt 
period and hold its value in the flip-flop. There are some delays on the Card Interrupt, asserted from the card, to the time 
the host system is informed.
• To detect a CMD line conflict, the host driver must set both Command Timeout Error Status Enable and Command CRC 
Error Status Enable to 1.
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
Reserved 
DMAE
SEN 
0
Reserv
ed 
0
AC12E
SEN 
0
DEBE
SEN 
DCES
EN 
DTOE
SEN 
CIESE
N 
CEBE
SEN 
CCES
EN 
CTOE
SEN 
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
Reserv
ed 
0
Reserved 
CINTS
EN 
CRMS
EN 
CINSS
EN 
BRRS
EN 
BWRS
EN 
DINTS
EN 
BGES
EN 
TCSE
N 
CCSE
N 
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
—
Reserved
30-29
—
Reserved
28
DMAESEN
DMA error status enable
0b - Masked
1b - Enabled
27
—
Reserved
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5123 / 5251


---
# 페이지 2264

Table continued from the previous page...
Field
Function
26
—
Reserved
25
—
Reserved
24
AC12ESEN
Auto CMD12 error status enable
0b - Masked
1b - Enabled
23
—
Reserved
22
DEBESEN
Data end bit error status enable
0b - Masked
1b - Enabled
21
DCESEN
Data CRC error status enable
0b - Masked
1b - Enabled
20
DTOESEN
Data timeout error status enable
0b - Masked
1b - Enabled
19
CIESEN
Command index error status enable
0b - Masked
1b - Enabled
18
CEBESEN
Command end bit error status enable
0b - Masked
1b - Enabled
17
CCESEN
Command CRC error status enable
0b - Masked
1b - Enabled
16
CTOESEN
Command timeout error status enable
0b - Masked
1b - Enabled
15
Reserved
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5124 / 5251


---
# 페이지 2265

Table continued from the previous page...
Field
Function
—
14
—
Reserved
13
—
Reserved
12
—
Reserved
11
—
Reserved
10-9
—
Reserved
8
CINTSEN
Card interrupt status enable
If this field is set to 0, uSDHC clears the interrupt request to the system. The Card Interrupt detection is 
stopped when this field is cleared and restarted when this field is set to 1. The host driver should clear 
the Card Interrupt Status Enable before servicing the Card Interrupt and should set this field again after all 
interrupt requests from the card are cleared to prevent inadvertent interrupts.
0b - Masked
1b - Enabled
7
CRMSEN
Card removal status enable
0b - Masked
1b - Enabled
6
CINSSEN
Card insertion status enable
0b - Masked
1b - Enabled
5
BRRSEN
Buffer read ready status enable
0b - Masked
1b - Enabled
4
BWRSEN
Buffer write ready status enable
0b - Masked
1b - Enabled
3
DMA interrupt status enable
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5125 / 5251


---
# 페이지 2266

Table continued from the previous page...
Field
Function
DINTSEN
0b - Masked
1b - Enabled
2
BGESEN
Block gap event status enable
0b - Masked
1b - Enabled
1
TCSEN
Transfer complete status enable
0b - Masked
1b - Enabled
0
CCSEN
Command complete status enable
0b - Masked
1b - Enabled
81.6.1.16
Interrupt Signal Enable (INT_SIGNAL_EN)
Offset
Register
Offset
INT_SIGNAL_EN
38h
Function
This register is used to select which interrupt status is indicated to the host system as the interrupt. These status fields all share 
the same interrupt lines. Setting any of these fields to 1 enables interrupt generation. The corresponding Status register field 
generates an interrupt when the corresponding interrupt signal enable field is set.
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
Reserved 
DMAEI
EN 
0
Reserv
ed 
0
AC12E
IEN 
0
DEBEI
EN 
DCEIE
N 
DTOEI
EN 
CIEIE
N 
CEBEI
EN 
CCEIE
N 
CTOEI
EN 
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
Reserv
ed 
0
Reserved 
CINTI
EN 
CRMI
EN 
CINSI
EN 
BRRIE
N 
BWRI
EN 
DINTI
EN 
BGEIE
N 
TCIEN 
CCIEN 
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
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5126 / 5251


---
# 페이지 2267

Fields
Field
Function
31
—
Reserved
30-29
—
Reserved
28
DMAEIEN
DMA error interrupt enable
0b - Masked
1b - Enable
27
—
Reserved
26
—
Reserved
25
—
Reserved
24
AC12EIEN
Auto CMD12 error interrupt enable
0b - Masked
1b - Enabled
23
—
Reserved
22
DEBEIEN
Data end bit error interrupt enable
0b - Masked
1b - Enabled
21
DCEIEN
Data CRC error interrupt enable
0b - Masked
1b - Enabled
20
DTOEIEN
Data timeout error interrupt enable
0b - Masked
1b - Enabled
19
CIEIEN
Command index error interrupt enable
0b - Masked
1b - Enabled
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5127 / 5251


---
# 페이지 2268

Table continued from the previous page...
Field
Function
18
CEBEIEN
Command end bit error interrupt enable
0b - Masked
1b - Enabled
17
CCEIEN
Command CRC error interrupt enable
0b - Masked
1b - Enabled
16
CTOEIEN
Command timeout error interrupt enable
0b - Masked
1b - Enabled
15
—
Reserved
14
—
Reserved
13
—
Reserved
12
—
Reserved
11
—
Reserved
10-9
—
Reserved
8
CINTIEN
Card interrupt enable
0b - Masked
1b - Enabled
7
CRMIEN
Card removal interrupt enable
0b - Masked
1b - Enabled
6
CINSIEN
Card insertion interrupt enable
0b - Masked
1b - Enabled
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5128 / 5251


---
# 페이지 2269

Table continued from the previous page...
Field
Function
5
BRRIEN
Buffer read ready interrupt enable
0b - Masked
1b - Enabled
4
BWRIEN
Buffer write ready interrupt enable
0b - Masked
1b - Enabled
3
DINTIEN
DMA interrupt enable
0b - Masked
1b - Enabled
2
BGEIEN
Block gap event interrupt enable
0b - Masked
1b - Enabled
1
TCIEN
Transfer complete interrupt enable
0b - Masked
1b - Enabled
0
CCIEN
Command complete interrupt enable
0b - Masked
1b - Enabled
81.6.1.17
Auto CMD12 Error Status (AUTOCMD12_ERR_STATUS)
Offset
Register
Offset
AUTOCMD12_ERR_STA
TUS
3Ch
Function
When the Auto CMD12 Error Status field in the Status register is set, the host driver checks this register to identify what kind of 
error the Auto CMD12 / CMD 23 indicated. Auto CMD23 errors are indicated in field 04-01. This register is valid only when the 
Auto CMD12 Error status field is set.
The table below shows the relationship between the Auto CMGD12 CRC Error and the Auto CMD12 Command Timeout Error.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5129 / 5251


---
# 페이지 2270

Table 822. Relationship between command CRC error and command timeout error for auto CMD12
Auto CMD12 CRC error
Auto CMD12 timeout error
Type of error
0
0
No error
0
1
Response timeout error
1
0
Response CRC error
1
1
CMD line conflict
Changes in Auto CMD12 Error Status register can be classified in three scenarios:
• When uSDHC is going to issue an Auto CMD12
— Set field 0 to 1 if the Auto CMD12 cannot be issued due to an error in the previous command
— Set field 0 to 0 if the Auto CMD12 is issued
• At the end field of an Auto CMD12 response
— Check errors correspond to fields 1-4
— Set fields 1-4 corresponding to detected errors
— Clear fields 1-4 corresponding to detected errors
• Before reading the Auto CMD12 Error Status field 7
— Set field 7 to 1 if there is a command that can't be issued
— Clear field 7 if there is no command to issue
The timing for generating the Auto CMD12 Error and writing to the Command register are asynchronous. After that, field 7 is 
sampled when the driver is not writing to the Command register. So, it is suggested to read this register only when the AC12E field 
in Interrupt Status register is set. An Auto CMD12 Error Interrupt is generated when one of the error fields (0-4) is set to 1. The 
Command Not Issued By Auto CMD12 Error does not generate an interrupt.
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
CNIBA
C1...
0
AC12I
E 
AC12E
BE 
AC12C
E 
AC12T
OE 
AC12N
E 
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
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5130 / 5251


---
# 페이지 2271

Fields
Field
Function
31-8
—
Reserved
7
CNIBAC12E
Command not issued by Auto CMD12 error
Setting this field to 1 means CMD_wo_DAT is not executed due to an Auto CMD12 error (D04-D01) in 
this register.
0b - No error
1b - Not issued
6-5
—
Reserved
4
AC12IE
Auto CMD12 / 23 index error
Occurs if the command index error occurs in response to a command.
0b - No error
1b - Error, the CMD index in response is not CMD12/23
3
AC12EBE
Auto CMD12 / 23 end bit error
Occurs when detecting that the end field of command response is 0 which should be 1.
0b - No error
1b - End bit error generated
2
AC12CE
Auto CMD12 / 23 CRC error
Occurs when detecting a CRC error in the command response.
0b - No CRC error
1b - CRC error met in Auto CMD12/23 response
1
AC12TOE
Auto CMD12 / 23 timeout error
Occurs if no response is returned within 64 SDCLK cycles from the end field of the command. If this field is 
set to1, the other error status fields (2-4) have no meaning.
0b - No error
1b - Time out
0
AC12NE
Auto CMD12 not executed
If memory multiple block data transfer is not started, due to a command error, this field is not set because it is 
not necessary to issue an Auto CMD12. Setting this field to 1 means uSDHC cannot issue the Auto CMD12 
to stop a memory multiple block data transfer due to some error. If this field is set to 1, other error status fields 
(1-4) have no meaning.
0b - Executed
1b - Not executed
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5131 / 5251


---
# 페이지 2272

81.6.1.18
Host Controller Capabilities (HOST_CTRL_CAP)
Offset
Register
Offset
HOST_CTRL_CAP
40h
Function
This register provides the host driver with information specific to uSDHC implementation. The value in this register is the 
power-on-reset value and does not change with a software reset.
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
VS30 
VS33 
SRS 
DMAS 
HSS 
ADMA
S 
0
MBL 
W
Reset
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
1
1
0
0
1
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
0
Reserv
ed 
Reserv
ed 
Reserv
ed 
W
Reset
1
0
1
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
1
0
0
Fields
Field
Function
31-27
—
Reserved
26
—
Reserved
25
VS30
Voltage support 3.0 V
This field depends on the host system ability.
0b - 3.0 V not supported
1b - 3.0 V supported
24
VS33
Voltage support 3.3 V
This field depends on the host system ability.
0b - 3.3 V not supported
1b - 3.3 V supported
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5132 / 5251


---
# 페이지 2273

Table continued from the previous page...
Field
Function
23
SRS
Suspend / resume support
This field indicates whether uSDHC supports Suspend / Resume functionality. If this field is 0, the Suspend 
and Resume mechanism, as well as the read wait, are not supported, and the host driver does not issue 
either Suspend or Resume commands.
0b - Not supported
1b - Supported
22
DMAS
DMA support
This field indicates whether uSDHC can use the internal DMA to transfer data between system memory and 
the data buffer directly.
0b - DMA not supported
1b - DMA supported
21
HSS
High speed support
This field indicates whether uSDHC supports High Speed mode and the host system can supply a SD clock 
frequency from 25 MHz to 50 MHz.
0b - High speed not supported
1b - High speed supported
20
ADMAS
ADMA support
This field indicates whether uSDHC supports the ADMA feature.
0b - Advanced DMA not supported
1b - Advanced DMA supported
19
—
Reserved
18-16
MBL
Max block length
This field indicates the maximum block size that the host driver can read and write to the buffer in uSDHC. 
The buffer transfers block size without wait cycles.
000b - 512 bytes
001b - 1024 bytes
010b - 2048 bytes
011b - 4096 bytes
15-3
—
Reserved
2
—
Reserved
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5133 / 5251


---
# 페이지 2274

Table continued from the previous page...
Field
Function
1
—
Reserved
0
—
Reserved
81.6.1.19
Watermark Level (WTMK_LVL)
Offset
Register
Offset
WTMK_LVL
44h
Function
This register indicates configurability of write and read watermark levels (FIFO threshold). Their value can range from 1 to 128 
words. Both write and read burst lengths are also configurable. Their value can range from 1 to 31 words.
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
WR_BRST_LEN 
WR_WML 
W
Reset
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
RD_BRST_LEN 
RD_WML 
W
Reset
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
WR_BRST_LE
N
Write burst length due to system restriction, the actual burst length might not exceed 16
This field indicates the number of words uSDHC writes in a single burst. The write burst length must be less 
than or equal to the write watermark level, and all bursts within a watermark level transfer is in back-to-back 
mode. On reset, this field is 8. Writing 0 to this field results in '01000' (that is, it is not able to clear this field).
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5134 / 5251


---
# 페이지 2275

Table continued from the previous page...
Field
Function
23-16
WR_WML
Write watermark level
This field indicates the number of words used as the watermark level (FIFO threshold) in a DMA write 
operation. Also, the number of words as a sequence of write bursts in back-to-back mode. The maximum 
legal value for the write watermark level is 128.
15-13
—
Reserved
12-8
RD_BRST_LEN
Read burst length due to system restriction, the actual burst length might not exceed 16
This field indicates the number of words uSDHC reads in a single burst. The read burst length must be less 
than or equal to the read watermark level, and all bursts within a watermark level transfer is in back-to-back 
mode. On reset, this field is 8. Writing 0 to this field results in '01000' (that is, it is not able to clear this field).
7-0
RD_WML
Read watermark level
This field indicates the number of words used as the watermark level (FIFO threshold) in a DMA read 
operation. Also, the number of words as a sequence of read bursts in back-to-back mode. The maximum 
legal value for the read water mark level is 128.
81.6.1.20
Mixer Control (MIX_CTRL)
Offset
Register
Offset
MIX_CTRL
48h
Function
This register is used to DMA and data transfer. To prevent data loss, the software should check if data transfer is active before 
writing this register. These fields are DPSEL, MBSEL, DTDSEL, AC12EN, BCEN, and DMAEN.
Table 823. Transfer type register setting for various transfer types
Multi/single block select
Block count enable
Block count
Function
0
Do not care
Do not care
Single transfer
1
0
Do not care
Infinite transfer
1
1
Positive number
Multiple transfer
1
1
Zero
No data transfer
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5135 / 5251


---
# 페이지 2276

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
Reserv
ed 
Reserv
ed 
0
0
0
0
0
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
AC23E
N 
NIBBL
E_...
MSBS
EL 
DTDS
EL 
DDR_
EN 
AC12E
N 
BCEN 
DMAE
N 
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
—
Reserved
Always write as 1.
30
—
Reserved
Always write as 0.
29
—
Reserved
Always write as 0.
28
—
Reserved
27
—
Reserved
26
—
Reserved
25-22
—
Reserved
21-8
—
Reserved
7
AC23EN
Auto CMD23 enable
This field is read/write when VEND_SPEC[CMD_BYTE_EN] is disabled; otherwise, this field is read-only. 
When this field is set to 1, the host controller issues a CMD23 automatically before issuing a command 
specified in the Command Register.
6
Nibble position indication
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5136 / 5251


---
# 페이지 2277

Table continued from the previous page...
Field
Function
NIBBLE_POS
This field indicates the nibble position in the DDR 4-bit mode. This field is read/write when 
VEND_SPEC[CMD_BYTE_EN] is disabled; otherwise, this field is read-only. 0- the sequence is 'odd 
high nibble -> even high nibble -> odd low nibble -> even low nibble'; 1- the sequence is 'odd high nibble -> 
odd low nibble -> even high nibble -> even low nibble'.
5
MSBSEL
Multi / Single block select
This field enables multiple block DATA line data transfers. This field is read/write when 
VEND_SPEC[CMD_BYTE_EN] is disabled; otherwise, this field is read-only. For any other commands, this 
field can be set to 0. If this field is 0, it is not necessary to set the Block Count register. See Command 
Transfer Type (CMD_XFR_TYP).
0b - Single block
1b - Multiple blocks
4
DTDSEL
Data transfer direction select
This field defines the direction of DATA line data transfers. This field is read/write when 
VEND_SPEC[CMD_BYTE_EN] is disabled; otherwise, this field is read-only. The field is set to 1 by 
the host driver to transfer data from the SD card to uSDHC and is set to 0 for all other commands.
0b - Write (Host to card)
1b - Read (Card to host)
3
DDR_EN
Dual data rate mode selection
This field is read/write when VEND_SPEC[CMD_BYTE_EN] is disabled; otherwise, this field is read-only.
2
AC12EN
Auto CMD12 enable
Multiple block transfers for memory require a CMD12 to stop the transaction. This field is read/write when 
VEND_SPEC[CMD_BYTE_EN] is disabled; otherwise, this field is read-only. When this field is set to 1, 
uSDHC issues a CMD12 automatically when the last block transfer has completed. The host driver is not set 
this field to issue commands that do not require CMD12 to stop a multiple block data transfer. In particular, 
secure commands defined in File Security Specification (see reference list) do not require CMD12. In single 
block transfer, uSDHC ignores this field no matter it is set or not.
0b - Disable
1b - Enable
1
BCEN
Block count enable
This field is used to enable the Block Count register, which is only relevant for multiple block transfers. This 
field is read/write when VEND_SPEC[CMD_BYTE_EN] is disabled; otherwise, this field is read-only. When 
this field is 0, the internal counter for block is disabled, which is useful in executing an infinite transfer.
0b - Disable
1b - Enable
0
DMAEN
DMA enable
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5137 / 5251


---
# 페이지 2278

Table continued from the previous page...
Field
Function
This field enables DMA functionality. This field is read/write when VEND_SPEC[CMD_BYTE_EN] is 
disabled; otherwise, this field is read-only. If this field is set to 1, a DMA operation begins when the host driver 
sets the DPSEL field of this register. Whether the simple DMA or the advanced DMA is active depends on 
the DMA Select field of the Protocol Control register.
0b - Disable
1b - Enable
81.6.1.21
Force Event (FORCE_EVENT)
Offset
Register
Offset
FORCE_EVENT
50h
Function
This register is not a physically implemented register. Rather, it is an address at which the Interrupt Status register can be written 
if the corresponding field of the Interrupt Status Enable Register is set. This register is a write only register and writing 0 to it has 
no effect. Writing 1 to this register sets the corresponding field of Interrupt Status register. A read from this register always results 
in 0's. to change the corresponding status fields in the Interrupt Status register, make sure to set IPGEN field in System Control 
Register so that peripheral clock is always active.
Forcing a card interrupt generates a short pulse on the DATA1 line, and the driver might treat this interrupt as a normal interrupt. 
The interrupt service routine might skip polling the card interrupt factor as the interrupt is self cleared.
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
0
0
0
0
0
0
0
0
0
0
0
0
W
FEVT
CINT 
FEVT
DMAE 
FEVT
AC1...
FEVT
DEBE 
FEVT
DCE 
FEVT
DTOE 
FEVT
CIE 
FEVT
CEBE 
FEVT
CCE 
FEVT
CTOE 
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
0
0
0
0
W
FEVT
CNI...
FEVTA
C1...
FEVTA
C1...
FEVTA
C1...
FEVTA
C1...
FEVTA
C1...
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
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5138 / 5251


---
# 페이지 2279

Fields
Field
Function
31
FEVTCINT
Force event card interrupt
Writing 1 to this field generates a short low-level pulse on the internal DATA1 line, as if a self-clearing 
interrupt was received from the external card. If enabled, the CINT field is set and the interrupt service 
routine might treat this interrupt as a normal interrupt from the external card.
30-29
—
Reserved
28
FEVTDMAE
Force event DMA error
Forces the DMAE field of Interrupt Status register to be set
27
—
Reserved
26
—
Reserved
25
—
Reserved
24
FEVTAC12E
Force event Auto Command 12 error
Forces the AC12E field of Interrupt Status register to be set
23
—
Reserved
22
FEVTDEBE
Force event data end bit error
Forces the DEBE field of Interrupt Status register to be set
21
FEVTDCE
Force event data CRC error
Forces the DCE field of Interrupt Status register to be set
20
FEVTDTOE
Force event data time out error
Force the DTOE field of Interrupt Status register to be set
19
FEVTCIE
Force event command index error
Forces the CCE field of Interrupt Status register to be set
18
FEVTCEBE
Force event command end bit error
Forces the CEBE field of Interrupt Status register to be set
17
FEVTCCE
Force event command CRC error
Forces the CCE field of Interrupt Status register to be set
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5139 / 5251


---
# 페이지 2280

Table continued from the previous page...
Field
Function
16
FEVTCTOE
Force event command time out error
Forces the CTOE field of Interrupt Status register to be set
15-8
—
Reserved
7
FEVTCNIBAC1
2E
Force event command not executed by Auto Command 12 error
Forces the CNIBAC12E field in the Auto Command12 Error Status register to be set
6-5
—
Reserved
4
FEVTAC12IE
Force event Auto Command 12 index error
Forces the AC12IE field in the Auto Command12 Error Status register to be set
3
FEVTAC12EBE
Force event Auto Command 12 end bit error
Forces the AC12EBE field in the Auto Command12 Error Status register to be set
2
FEVTAC12CE
Force event auto command 12 CRC error
Forces the AC12CE field in the Auto Command12 Error Status register to be set
1
FEVTAC12TOE
Force event auto command 12 time out error
Forces the AC12TOE field in the Auto Command12 Error Status register to be set
0
FEVTAC12NE
Force event auto command 12 not executed
Forces the AC12NE field in the Auto Command12 Error Status register to be set
81.6.1.22
ADMA Error Status (ADMA_ERR_STATUS)
Offset
Register
Offset
ADMA_ERR_STATUS
54h
Function
When an ADMA Error Interrupt has occurred, the ADMA error sates field in this register holds the ADMA state and the ADMA 
System Address register holds the address around the error descriptor.
For recovering from this error, the host driver requires the ADMA state to identify the error descriptor address as follows:
• ST_STOP: Previous location set in the ADMA System Address register is the error descriptor address.
• ST_FDS: Current location set in the ADMA System Address register is the error descriptor address.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5140 / 5251


---
# 페이지 2281

• ST_CADR: This state is never set because it only increments the descriptor pointer and does not generate an ADMA 
error.
• ST_TFR: Previous location set in the ADMA System Address register is the error descriptor address.
In case of a write operation, the host driver should use the ACMD22 to get the number of the written block, rather than using this 
information, because unwritten data might exist in the host controller.
The host controller generates the ADMA Error Interrupt when it detects invalid descriptor data (Valid=0) in the ST_FDS state. The 
host driver can distinguish this error by reading the Valid field of the error descriptor.
Table 824. ADMA error state coding
D01-D00
ADMA error state (when error 
has occurred)
Contents of ADMA System 
Address register 
00
ST_STOP (Stop DMA)
Holds the address of the next executable 
descriptor command
01
ST_FDS (Fetch descriptor)
Holds the valid descriptor address
10
ST_CADR (Change address)
No ADMA error is generated
11
ST_TFR (Transfer data)
Holds the address of the next executable 
descriptor command
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
ADMA
DCE 
ADMA
LME 
ADMAES 
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
31-4
—
Reserved
3
ADMADCE
ADMA descriptor error
This error occurs when invalid descriptor fetched by ADMA.
0b - No error
1b - Error
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5141 / 5251


---
# 페이지 2282

Table continued from the previous page...
Field
Function
2
ADMALME
ADMA length mismatch error
This error occurs in the following two cases:
• While the block count enable is being set, the total data length specified by the descriptor table is 
different from that specified by the block count and block length.
• Total data length cannot be divided by the block length.
0b - No error
1b - Error
1-0
ADMAES
ADMA error state (when ADMA error is occurred)
This field indicates the state of the ADMA when an error has occurred during an ADMA data transfer. See 
ADMA Error Status (ADMA_ERR_STATUS) for more details.
81.6.1.23
ADMA System Address (ADMA_SYS_ADDR)
Offset
Register
Offset
ADMA_SYS_ADDR
58h
Function
This register holds the word address of the executing command in the Descriptor table. At the start of ADMA, the host driver 
sets the start address of the Descriptor table. The ADMA engine increments this register address whenever fetching a Descriptor 
command. When the ADMA is stopped at the Block Gap, this register indicates the address of the next executable Descriptor 
command. When the ADMA Error Interrupt is generated, this register holds the valid Descriptor address depending on the ADMA 
state. The lower 2 bits of this register is tied to '0' so the ADMA address is always word aligned.
Because this register supports dynamic address reflecting, when TC field is set, it automatically alters the value of internal address 
counter, so the software cannot change this register when TC field is set. Such restriction is also listed in Software restrictions.
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
ADS_ADDR 
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
ADS_ADDR 
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
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5142 / 5251


---
# 페이지 2283

Fields
Field
Function
31-2
ADS_ADDR
ADMA system address
This field contains the physical system memory address used for ADMA transfers.
1-0
—
Reserved
81.6.1.24
DLL (Delay Line) Control (DLL_CTRL)
Offset
Register
Offset
DLL_CTRL
60h
Function
This register contains control fields for DLL.
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
DLL_CTRL_REF_UPDATE_INT 
DLL_CTRL_SLV_UPDATE_INT 
0
DLL_CTRL_SLV_DLY_T
ARGET1 
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
DLL_CTRL_SLV_OVERRIDE_VAL 
DLL_C
TR...
DLL_C
TR...
DLL_CTRL_SLV_DLY_TARGET0 
DLL_C
TR...
DLL_C
TR...
DLL_C
TR...
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
DLL_CTRL_RE
F_UPDATE_IN
T
DLL control loop update interval
The interval cycle is (2 + REF_UPDATE_INT) * REF_CLOCK. By default, the DLL control loop updates every 
two REF_CLOCK cycles. It should be noted that increasing the reference delay-line update interval reduces 
the ability of the DLL to adjust to fast changes in conditions that might effect the delay (such as voltage 
and temperature)
27-20
Slave delay line update interval
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5143 / 5251


---
# 페이지 2284

Table continued from the previous page...
Field
Function
DLL_CTRL_SL
V_UPDATE_IN
T
If default 0 is used, it means 256 cycles of REF_CLOCK. A value of 0x0f results in 15 cycles and so on. Note 
that software can always cause an update of the slave-delay line using the SLV_FORCE_UPDATE register. 
Note that the slave delay line also updates automatically when the reference DLL transitions to a locked 
state (from an un-locked state).
19
—
Reserved
18-16
DLL_CTRL_SL
V_DLY_TARGE
T1
DLL slave delay target1
See DLL_CTRL_SLV_DLY_TARGET0 below.
15-9
DLL_CTRL_SL
V_OVERRIDE_
VAL
DLL slave override val
When SLV_OVERRIDE = 1, this field is used to select 1 of 128 physical taps manually. A value of 0 selects 
tap 1, and a value of 0x7f selects tap 128.
8
DLL_CTRL_SL
V_OVERRIDE
DLL slave override
Set this field to 1 to Enable manual override for slave delay chain using SLV_OVERRIDE_VAL; to set 0 to 
disable manual override. This feature does not require the DLL to be enabled using the ENABLE field. In 
fact to reduce power, if SLV_OVERRIDE is used, it is recommended to disable the DLL with ENABLE = 0
7
DLL_CTRL_GA
TE_UPDATE
DLL gate update
Set this field to 1 to prevent the DLL from updating (because when clock_in exists, glitches might appear 
during DLL updates). This field might be used by software if such a condition occurs. Clear the bit to 0 to 
allow the DLL to update automatically.
6-3
DLL_CTRL_SL
V_DLY_TARGE
T0
DLL slave delay target0
The delay target for uSDHC loopback read clock can be programmed in 1/16th increments of an 
ref_clock half-period. The delay is (({DLL_CTRL_SLV_DLY_TARGET1,DLL_CTRL_SLV_DLY_TARGET0} 
+1)* REF_CLOCK / 2) / 16 So the input read-clock can be delayed relative input data from (REF_CLOCK / 
2) / 16 to REF_CLOCK * 4.
 
For the restrictions of delay cell implementation, the delay target must be set between 
REF_CLOCK/16 and REF_CLOCK*2 when REF_CLOCK is running at 200 MHz. When 
REF_CLOCK frequency is slower than 100 MHz, the maximum delay target might not 
reach REF_CLOCK*2.
  NOTE  
2
DLL_CTRL_SL
V_FORCE_UP
D
DLL slave delay line
Setting this field to 1, forces the slave delay line to update to the DLL calibrated value immediately. The slave 
delay line updates automatically based on the SLV_UPDATE_INT interval or when a DLL lock condition is 
sensed. Subsequent forcing of the slave-line update can only occur if SLV_FORCE_UP is set back to 0 and 
then asserted again (edge triggered). Be sure to use it when uSDHC is idle. This function might not work 
when uSDHC is working on data / cmd / response.
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5144 / 5251


---
# 페이지 2285

Table continued from the previous page...
Field
Function
1
DLL_CTRL_RE
SET
DLL reset
Setting this field to 1 force a reset on DLL. This causes the DLL to lose lock and re-calibrate to detect 
an REF_CLOCK half period phase shift. This signal is used by the DLL as edge-sensitive, so to create a 
subsequent reset, RESET must be taken low and then asserted again.
0
DLL_CTRL_EN
ABLE
DLL and delay chain
Set this field to 1 to enable the DLL and delay chain; otherwise; set to 0 to bypasses DLL. Note that using the 
slave delay line override feature with SLV_OVERRIDE and SLV_OVERRIDE VAL, the DLL does not need 
to be enabled.
81.6.1.25
DLL Status (DLL_STATUS)
Offset
Register
Offset
DLL_STATUS
64h
Function
This register contains the DLL status information. All fields are read only and reads the same as the power-reset value.
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
DLL_STS_REF_SEL 
DLL_STS_SLV_SEL 
DLL_S
TS...
DLL_S
TS...
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
0
0
Fields
Field
Function
31-16
—
Reserved
15-9
Reference delay line select taps
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5145 / 5251


---
# 페이지 2286

Table continued from the previous page...
Field
Function
DLL_STS_REF
_SEL
This is encoded by 7 fields for 127 taps.
8-2
DLL_STS_SLV_
SEL
Slave delay line select status
This is the instant value generated from reference chain. Because the reference chain can only be updated 
when REF_CLOCK is detected, this value should be the right value to be updated when the reference 
is locked.
1
DLL_STS_REF
_LOCK
Reference DLL lock status
This signifies that the DLL has detected and locked to a half-phase ref_clock shift, allowing the slave 
delay-line to perform programmed clock delays
0
DLL_STS_SLV_
LOCK
Slave delay-line lock status
This signifies that a valid calibration has been set to the slave-delay line and that the slave-delay line is 
implementing the programmed delay value
81.6.1.26
Vendor Specific Register (VEND_SPEC)
Offset
Register
Offset
VEND_SPEC
C0h
Function
This register contains the vendor specific control/status register.
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
CMD_
BYT...
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserved 
Reserved 
W
Reset
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
CRC_
CHK...
0
Reserv
ed 
Reserv
ed 
FRC_
SDC...
0
Reserv
ed 
Reserv
ed 
0
AC12_
WR...
Reserv
ed 
Reserv
ed 
EXT_D
MA...
W
Reset
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
1
0
0
1
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5146 / 5251


---
# 페이지 2287

Fields
Field
Function
31
CMD_BYTE_E
N
Register byte access for CMD_XFR_TYP
This field controls the register byte access for Command Transfer Type (CMD_XFR_TYP). If this field is 
enabled, the register can be configured through byte write enable. IPS_bus can write only one byte once for 
one write operation.
0b - Disable. MIX_CTRL[7:0] is read/write and CMD_XFR_TYP[7:0] is read-only.
1b - Enable. MIX_CTRL[7:0] is read-only and CMD_XFR_TYP[7:0] is read/write.
30
—
Reserved
Always write as 0.
29
—
Reserved
Always write as 1
28
—
Reserved
Always write as 0.
27-24
—
Reserved
Always write as 4'b0000.
23-16
—
Reserved
Always write as 8'h00.
15
CRC_CHK_DIS
CRC Check Disable
0b - Check CRC16 for every read data packet and check CRC fields for every write data packet
1b - Ignore CRC16 check for every read data packet and ignore CRC fields check for every write 
data packet
14-11
—
Reserved
Reserved
10
—
Reserved
Always write as 0.
9
—
Reserved
Always write as 0.
8
FRC_SDCLK_O
N
Force CLK
Force CLK output active
Do not set this bit to 1 unless it is necessary. Also, make sure that this bit is cleared when uSDHC’s clock 
is about to be changed (frequency change, clock source change, or delay chain tuning).
0b - CLK active or inactive is fully controlled by the hardware.
1b - Force CLK active
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5147 / 5251


---
# 페이지 2288

Table continued from the previous page...
Field
Function
7
—
Reserved
6
—
Reserved
5
—
Reserved
4
—
Reserved
3
AC12_WR_CH
KBUSY_EN
Check busy enable
Check busy enable after auto CMD12 for write data packet
0b - Do not check busy after auto CMD12 for write data packet
1b - Check busy after auto CMD12 for write data packet
2
—
Reserved
1
—
Reserved
0
EXT_DMA_EN
External DMA request enable
Enable the request to external DMA. When the internal DMA (either Simple DMA or Advanced DMA) is not 
in use, and this field is set, uSDHC sends out DMA request when the internal buffer is ready. This field is 
particularly useful when transferring data by Arm platform polling mode, and it is not allowed to send out the 
external DMA request. By default, this field is set.
0b - In any scenario, uSDHC does not send out external DMA request.
1b - When internal DMA is not active, the external DMA request is sent out.
81.6.1.27
eMMC Boot (MMC_BOOT)
Offset
Register
Offset
MMC_BOOT
C4h
Function
This register contains the eMMC Fast Boot control register.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5148 / 5251


---
# 페이지 2289

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
BOOT_BLK_CNT 
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
DISAB
LE...
AUTO
_SA...
BOOT
_EN 
BOOT
_MO...
BOOT
_ACK 
DTOCV_ACK 
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
BOOT_BLK_CN
T
Stop At Block Gap value of automatic mode
The value defines the Stop At Block Gap value of automatic mode. When received, card block cnt is equal 
to (BLK_CNT - BOOT_BLK_CNT) and AUTO_SABG_EN is 1, then Stop At Block Gap.
Here, BLK_CNT is defined in the Block Attributes Register, field 31 - 16 of 0x04.
15-9
—
Reserved
8
DISABLE_TIME
_OUT
Time out
 
When this field is set, there is no timeout check no matter whether BOOT_EN is set or not.
  NOTE  
0b - Enable time out
1b - Disable time out
7
AUTO_SABG_E
N
Auto stop at block gap
During boot, enable auto stop at block gap function. This function is triggered, and host stops at block gap 
when received card block cnt is equal to (BLK_CNT - BOOT_BLK_CNT).
6
BOOT_EN
Boot enable
Boot mode enable
0b - Fast boot disable
1b - Fast boot enable
5
BOOT_MODE
Boot mode
Boot mode select
0b - Normal boot
1b - Alternative boot
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5149 / 5251


---
# 페이지 2290

Table continued from the previous page...
Field
Function
4
BOOT_ACK
BOOT ACK
Boot ACK mode select
0b - No ack
1b - Ack
3-0
DTOCV_ACK
Boot ACK time out
Boot ACK time out counter value.
0000b - SDCLK x 2^14
0001b - SDCLK x 2^15
0010b - SDCLK x 2^16
0011b - SDCLK x 2^17
0100b - SDCLK x 2^18
0101b - SDCLK x 2^19
0110b - SDCLK x 2^20
0111b - SDCLK x 2^21
1110b - SDCLK x 2^28
1111b - SDCLK x 2^29
81.6.1.28
Vendor Specific 2 Register (VEND_SPEC2)
Offset
Register
Offset
VEND_SPEC2
C8h
Function
This register contains the vendor specific control 2 register.
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5150 / 5251


---
# 페이지 2291

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
EN_32
K_...
Reserv
ed 
Reserv
ed 
Reserv
ed 
Reserved 
0
0
0
0
CARD
_IN...
0
W
Reset
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
0
0
0
1
1
0
Fields
Field
Function
31-16
—
Reserved
15
EN_32K_CLK
Select the clock source for host card detection.
It can use low power clock for card detection, by setting this bit to 1.
0b - Use the peripheral clock (ipg_clk) for card detection.
1b - Use the low power clock (ipg_clk_lp) for card detection.
14
—
Reserved
13
—
Reserved
12
—
Reserved
11-10
—
Reserved
9
—
Reserved
8-7
—
Reserved
6
—
Reserved
Table continues on the next page...
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5151 / 5251


---
# 페이지 2292

Table continued from the previous page...
Field
Function
5-4
—
Reserved
3
CARD_INT_D3_
TEST
Card interrupt detection test
This field is used only for debugging.
0b - Check the card interrupt only when DATA3 is high.
1b - Check the card interrupt by ignoring the status of DATA3.
2-0
—
Reserved
NXP Semiconductors
Ultra Secured Digital Host Controller (uSDHC)
S32K3xx Reference Manual, Rev. 10, 04/16/2025
Reference Manual
Preliminary Information for S32K389
5152 / 5251


---
