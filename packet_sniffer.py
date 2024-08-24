# Import necessary libraries
from scapy.all import *

# Define the packet handling function
def packet_handler(packet):
    # Display the packet summary
    print(f"Packet Summary: {packet.summary()}")
    
    # Extract source and destination IP addresses
    if IP in packet: # type: ignore
        src_ip = packet[IP].src # type: ignore
        dst_ip = packet[IP].dst # type: ignore
        print(f"Source IP: {src_ip}")
        print(f"Destination IP: {dst_ip}")

    # Extract protocol information
    protocol = packet.payload.name
    print(f"Protocol: {protocol}")

    # Extract payload data (if available)
    if Raw in packet: # type: ignore
        payload = packet[Raw].load # type: ignore
        print(f"Payload Data: {payload.decode(errors='replace')}")
    
    print("\n" + "="*40 + "\n")

# Function to start packet sniffing
def start_sniffing(interface="Wi-Fi", count=10, filter="ip"):
    """
    Parameters:
    - interface: Network interface to listen on (e.g., 'Wi-Fi' for Windows, 'wlan0' for Wi-Fi on Linux).
    - count: Number of packets to capture.
    - filter: Filter expression to capture specific types of packets (e.g., 'ip', 'tcp', 'udp', 'icmp').
    """
    
    print(f"Starting packet sniffing on interface {interface}...")
    sniff(iface=interface, count=count, prn=packet_handler, filter=filter) # type: ignore

# Main function
if __name__ == "__main__":
    # Customize the following parameters as needed
    interface = "Wi-Fi"  # Set to your Wi-Fi interface on Windows
    packet_count = 20    # Number of packets to capture
    
    # Example 1: Capture all IP packets
    packet_filter = "ip"  # Filter for IP packets
    start_sniffing(interface=interface, count=packet_count, filter=packet_filter)

    # Example 2: Capture only TCP packets
    # packet_filter = "tcp"  # Filter for TCP packets
    # start_sniffing(interface=interface, count=packet_count, filter=packet_filter)

    # Example 3: Capture only ICMP packets
    # packet_filter = "icmp"  # Filter for ICMP packets
    # start_sniffing(interface=interface, count=packet_count, filter=packet_filter)
