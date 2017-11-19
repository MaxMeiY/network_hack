#!/usr/bin/python

import os
import re
import tailer
import random

logfile = '/var/log/auth.log'
max_failed = 3
max_failed_cmd = "/sbin/shutdown -h now"
failer_login = {}

success_patterns = [
    re.compile(
        "Accepted password for (?P<user>.+?) from \
        (?P<host>.+?) port"),
    re.compile(
        "session opened for user (?P<user>.+?) by")
]

failed_patterns = [
    re.compile(
        "Failed password for (?P<user>.+?) from \
        (?P<host>.+?) port"),
    re.compile(
        "FAILED LOGIN (\(\d\)) on `(.+?)' FOR \
        `(?P<user>.+?)'")
]

shutdown_msgs =[
    'Eat my shorts',
    'Follow the white rabbit',
    'System will explode in three seconds!',
    'Go home and leave me alone.',
    'Game... Over'
]

def check_match(line, pattern, failed_login_check):
    found = False
    match = pattern.search(line)

    if (match != None):
        found = True
        failed_login.setdefault(match.group('user'), 0)
        