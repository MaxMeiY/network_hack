#!/usr/bin/python

from scapy.all import *

iface = 'wlp4s0'
wpa_handshake = []

def handle_packet(packet):
    # Got EAPOL KEY packet
    if packet.haslayer(EAPOL) and packet.type == 2:
        print(packet.summary())
        wpa_handshake.append(packet)

        # Got complete handshake ? Dump it pcap file
        if len(wpa_handshake) >= 4:
            wrpcap('wpa_handshake.pcap', wpa_handshake)


# Set device into monitor mode
os.system('iwconfig ' + iface + ' mode monitor')

# Start sniffing
print("Sniffing on interface " + iface)
sniff(iface=iface, prn=handle_packet)