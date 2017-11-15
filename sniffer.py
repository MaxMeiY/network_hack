import sys
import getopt
import pcapy
from impacket.ImpactDecoder import EthDecoder

dev = 'wlp4s0'
filter = 'arp'
decoder = EthDecoder()

# This function will be called for every packet
# and just print it
def handler_packet(hdr, data):
    print(decoder.decode(data))

def usage():
    print(sys.argv[0] + ' -i <dev> -f <pcap_filter')
    sys.exit(1)

# parsing parameter
try:
    cmd_opts = 'f:i:'
    opts, args = getopt.getopt(sys.argv[1:], cmd_opts)
except get.GetoptError:
    usage()

for opt in opts:
    if opt[0] == '-f':
        filter = opt[1]
    elif opt[0] == '-i':
        dev = opt[1]
    else:
        usage()

# open device in promisc mode
pcap = pcapy.open_live(dev, 1500, 0, 100)

# set pcap filter
pcap.setfilter(filter)

# start sniffing
pcap.loop(0, handler_packet)