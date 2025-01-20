# scripts/network_monitor.py
```python
import pyshark

def monitor_network(interface):
    print("Starting network monitoring on interface:", interface)

    capture = pyshark.LiveCapture(interface=interface)
    for packet in capture.sniff_continuously(packet_count=50):
        try:
            print(f"Packet: {packet.ip.src} -> {packet.ip.dst}")
        except AttributeError:
            # Ignore packets without IP layer
            continue

if __name__ == "__main__":
    interface = input("Enter the network interface to monitor (e.g., 'Wi-Fi', 'Ethernet'): ")
    monitor_network(interface)
```
