# Master Toolbox - Cybersecurity Toolkit

## Overview
Master Toolbox is a comprehensive cybersecurity toolkit designed for both beginners and professionals. It provides a suite of tools for network analysis, penetration testing, and web security, with a focus on simplicity and ease of use. The program is written in Python 3.8 and includes both CLI and GUI versions.

---

## Features

### 1. **Man-in-the-Middle (MITM) Attacks**
This section simulates ARP Spoofing attacks and provides tools to detect them. ARP Spoofing allows an attacker to intercept network traffic between two devices by poisoning the ARP cache.

#### **Features**:
- **ARP Spoofing Attack**:  
  - Redirects traffic between a target device (e.g., a laptop) and the router through the attacker's machine.  
  - Enables packet sniffing, session hijacking, or data manipulation.  
  - Simplified activation/deactivation via GUI/CLI (no manual service configuration required).  

- **ARP Spoofing Detector**:  
  - Monitors the network for suspicious ARP replies.  
  - Alerts when duplicate IP-MAC mappings (indicative of ARP spoofing) are detected.

### 2. **Network Tools**
   - **Ping Sweep**: Scans for active hosts on a network.
   - **HTTP Sniffer**: Captures HTTP traffic.
   - **Packet Sniffer**: Monitors network packets.
   - **Domain to IP**: Converts domain names to IP addresses.
   - **IP Routing**: Displays routing information.
   - **Port Scanner**: Scans open ports on a target.
   - **MAC Table**: Displays the MAC address table.
   - **Interface Info**: Lists network interfaces.
   - **WiFi Tools**: Utilities for WiFi network analysis.

### 3. **WiFi Attacks**
   - **SYN Flood**: Simulates a SYN flood attack to test network resilience.
   - **SYN Flood Detector**: Detects and mitigates SYN flood attacks.

### 4. **Website Scanner**
   - **Subdomain Finder**: Discovers subdomains of a target website.
   - **Admin Panel Finder**: Locates admin panels.
   - **URL Info**: Retrieves header and domain information.
   - **Full Scan**: Performs a comprehensive scan of a website.

### 5. **WordPress Attacks**
   - **Directory Searcher**: Identifies vulnerable directories in WordPress sites for security testing or patching.

---

## Requirements
- **Operating System**: Windows (compatible with most versions).
- **Dependencies**:
  - **Npcap**: Required for packet capturing and network analysis.
  - **Python 3.8**: Ensure Python 3.8 or compatible is installed.
  - **Routing and Remote Access Service**: Must be enabled for simulating certain attacks.
- **APIs Used**:
  - **WhoisXMLAPI**: For domain information lookup.
  - **IP-API**: For retrieving server header details.

---

## Key Advantages
- **User-Friendly**: Default parameters are provided for beginners.
- **Modular Design**: Code is organized into modules for readability and maintenance.
- **Error Handling**: Robust error handling ensures uninterrupted operation.

---

## Installation
1. Install Python 3.8 from the official Python website.
2. Download and install **Npcap** (available at [https://npcap.com](https://npcap.com)).
3. Enable **Routing and Remote Access Service** on Windows.
4. Clone or download the Master Toolbox repository.
5. Install required Python packages using:
   ```bash
   pip install -r requirements.txt

---

## Usage
1. Run the program via CLI or GUI:
    ```python 
    master_toolbox.py
2. Follow the on-screen prompts to select tools and configure parameters.