#!/usr/bin/python

import sys
import socket
from random import randint

if len(sys.argv) < 2:
    print(sys.argv[0] + ": <start_ip>-<stop_ip>")
    sys.exit(1)

def get_ips(start_ip, stop_ip):
    ips = []
    tmp = []

    for i in start_ip.split('.'):
        tmp.append("%02X" % long(i))

    start_dec = long(''.join(tmp), 16)
    tmp = []

    for i in stop_ip.split('.'):
        tmp.append("%02X" % long(i))

    stop_dec = long(''.join(tmp), 16)
    print(start_dec, stop_dec)

    while(start_dec < stop_dec + 1):
        bytess = []
        bytess.append(str(int(start_dec / 16777216)))
        rem = start_dec % 16777216
        bytess.append(str(int(rem / 65536)))
        rem = rem % 65536
        bytess.append(str(int(rem / 256)))
        rem = rem % 256
        bytess.append(str(rem))
        ips.append(".".join(bytess))
        start_dec += 1
    return ips

def dns_reverse_lookup(start_ip, stop_ip):
    ips = get_ips(start_ip, stop_ip)

    while len(ips) > 0:
        i = randint(0, len(ips) - 1)
        lookup_ip = str(ips[i])

        try:
            print(lookup_ip + ": " +  str(socket.gethostbyaddr(lookup_ip)[0]))
        except (socket.herror, socket.error):
            pass

        del ips[i]

start_ip, stop_ip = sys.argv[1].split('-')
dns_reverse_lookup(start_ip, stop_ip)