import psutil
import socket

def list_network_interfaces():
    interfaces = psutil.net_if_addrs()  # Get network interfaces
    for interface, addresses in interfaces.items():
        print(f"Interface: {interface}")
        for address in addresses:
            if address.family == socket.AF_INET:
                print(f"  IPv4 Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif address.family == socket.AF_INET6:
                print(f"  IPv6 Address: {address.address}")
            elif address.family == psutil.AF_LINK:
                print(f"  MAC Address: {address.address}")
        print("-" * 40)

# Run the function
list_network_interfaces()

