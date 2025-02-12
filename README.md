# Network Interface Scanner Using Python 

## What is Network Interface ?

A network interface is a point of connection between a computer (or any network device) and a network. It enables communication between devices over a network, allowing data transmission and reception.


## Types of NEtwork Interface 

  ### 1. Wired Interface (Ethernet)
  - Uses cables for a stable and high-speed connection. Example **eth0** ,**eth1** in linux.
     
  ### 2. Wireless Interface (Wi-Fi)
  - Enables wireless communication using radio signals. Example: **wlan0** (Linux)
    
  ### 3. Loopback Interface
  - Used for internal communication within a device. Example: **lo**, IP address **127.0.0.1**
    
  ### 4. Virtual Interface
  - These are software-defined interfaces used for internal or specialized communication.

### Network Interface Scanner Script

This Python script utilizes the **psutil** and **socket** modules to list all available network interfaces on the system along with their associated addresses, netmasks, and broadcast IPs. It is a useful tool for gathering network configuration details


### Prerequisites 
Ensure you have Python installed on your system. The script requires the **psutil** module, which can be installed using:
- ```bash
  pip install psutil
  ```

## Psutil Module in Python

The **psutil** (Process and System Utilities) module in Python is a cross-platform library used to interact with system resources and process management. It provides functions to retrieve information on system utilization (CPU, memory, disks, network, sensors, and more) as well as manage system processes.


