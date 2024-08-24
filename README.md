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

   

