from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

def process_packet(packet):
    print("=" * 60)

    if packet.haslayer(IP):
        ip = packet[IP]

        print("Source IP      :", ip.src)
        print("Destination IP :", ip.dst)

        if packet.haslayer(TCP):
            print("Protocol       : TCP")
        elif packet.haslayer(UDP):
            print("Protocol       : UDP")
        elif packet.haslayer(ICMP):
            print("Protocol       : ICMP")
        else:
            print("Protocol       :", ip.proto)

        print(packet.summary())

print("Starting Packet Sniffer...")
print("Press Ctrl+C to stop.\n")

# Replace "Wi-Fi" with your interface name if different
sniff(iface="Wi-Fi", prn=process_packet, store=False)