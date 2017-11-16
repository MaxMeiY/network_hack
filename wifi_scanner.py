#!/usr/bin/python

from pythonwifi.iwlibs import Wireless

wifi = Wireless('wlp4s0')

for ap in wifi.scan():
    print("SSID: " + ap.essid)
    print("AP: " + ap.bssid)
    print("Signal: " + str(ap.quality.getSignallevel()))
    print("Frequency: " + str(
        ap.frequency.getFrequency()))
    print("")