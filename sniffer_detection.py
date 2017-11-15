from scapy.all import promiscping
import sys

promiscping(sys.argv[1])