# PRODIGY_CS_05
# Packet Sniffer Tool
This project is a packet sniffer tool developed using Python and Scapy. It captures and analyzes network packets, displaying relevant information such as source and destination IP addresses, protocols, and payload data. The tool is intended for educational purposes and ethical use only.

# Features
- Capture and display IP, TCP, and ICMP packets.
- Display packet details, including source and destination IP addresses, protocol information, and payload data.
- Support for different network interfaces (e.g., Ethernet, Wi-Fi).
- Cross-platform support (Windows and Linux).

# Requirements
### Python
- Python 3.6 or higher
### Python Libraries
- Scapy
## Platform-Specific Requirements
### Windows
- [Npcap](https://npcap.com/#download) (compatible with WinPcap API)
## Linux
- [libpcap](https://www.linuxfromscratch.org/blfs/view/svn/basicnet/libpcap.html)

# Installation
1. Install Python

    Ensure you have Python 3.6 or higher installed on your system.
- **Windows:** Download [Python](https://www.python.org/downloads/windowsA)
- **Linux:** Install Python using your package manager
  ``` bash
  sudo apt-get install python3
  ```
2. Install Required Python Libraries
 
    Install ***Scapy*** using pip:
  ```bash
  pip install scapy
  ```
3. Install Platform-Specific Dependencies
     
   **Windows (Npcap)**
    1. Download and install [Npcap](https://npcap.com/#download).
    2. During installation, ensure you select the option "Install Npcap in WinPcap API-compatible mode."
       
   **Linux (libpcap)**      
      Install libpcap, which is usually included in most Linux distributions:
   ```bash
   sudo apt-get install libpcap-dev
   ```
## Usage
1. **Clone the Repository**
   
    Clone this repository to your local machine:
    ```bash
    git clone https://github.com/shreyashbandekar/PRODIGY_CS_05.git
    cd packet_sniffer
    ```
2. **Running the Packet Sniffer**     

    **Windows**
  - Open an Administrator Command Prompt.
  - Navigate to the directory containing the script.
  - Run the script using Python:
      
    ```bash
    python app.py
    ```
    - By default, the script captures IP packets on the Wi-Fi interface. Make sure the interface name ("Wi-Fi") matches your     system's Wi-Fi interface.     

    **Linux**
    
1. Open a terminal.
2. Navigate to the directory containing the script.
3. Run the script with root privileges:
 ```bash
sudo python3 app.py
```
- By default, the script captures IP packets on the wlan0 interface. Make sure the interface name ("wlan0") matches your system's Wi-Fi interface.
  
3. **Customizing the Packet Capture**
   
You can modify the script to capture different types of packets by changing the packet_filter variable in the script:

- IP Packets: Captures all IP packets (default).
- TCP Packets: Uncomment packet_filter = "tcp" to capture only TCP packets.
- ICMP Packets: Uncomment packet_filter = "icmp" to capture only ICMP packets.
  
4. **Viewing Network Interfaces**
   
If you're unsure of your network interface name, you can list all available interfaces using Scapy:

```python
#python 
from scapy.all import get_if_list
print(get_if_list())
```
Update the interface variable in the script to match the correct interface.

# Example Output
```plaintext
Packet Summary: IP / TCP 192.168.1.10:12345 > 192.168.1.1:http S
Source IP: 192.168.1.10
Destination IP: 192.168.1.1
Protocol: TCP
Payload Data: b'\x16\x03\x01\x02\x00\x01\x00\x01\xfc\x03\x03'
========================================
```
