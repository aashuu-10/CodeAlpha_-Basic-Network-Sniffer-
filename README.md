# Basic Network Sniffer

## Project Overview

This project is a Basic Network Sniffer developed using Python and Scapy. It captures live network packets and displays useful network information such as source IP, destination IP, protocol, and port numbers.

## Features

- Capture live network packets
- Display Source IP Address
- Display Destination IP Address
- Detect TCP packets
- Detect UDP packets
- Display Source and Destination Ports

## Technologies Used

- Python 3
- Scapy
- Npcap
- Windows 11

## Installation

1. Install Python
2. Install Scapy

```bash
pip install scapy
```

3. Install Npcap

https://npcap.com/

## Run the Program

```bash
python network_sniffer.py
```

## Sample Output

```
Starting Packet Sniffer...
Source IP: 192.168.1.10
Destination IP: 142.250.183.78
Protocol: TCP
Source Port: 51234
Destination Port: 443
```

## Project Structure

```
networksniffer
│── network_sniffer.py
│── README.md
│── requirements.txt
```

## Author

Ayush Kumar