#!/usr/bin/python3

import os
import sys
from pykeepass import PyKeePass



class Group:

    def __init__(parent_group, group_name, icon, notes):
        self.destination_group = parent_group
        self.group_name = group_name
        self.icon = icon
        self.notes = notes
        self.entries = []


class Entry:

    def __init__(title, username, password, url, note):
        self.title = title
        self.username = username
        self.password = password
        self.url = url
        self.note = note


class Keepass_Manager:


    def readConf(self, filepath):
        with open(filepath, 'r') as f:
            for line in f.readlines():
                param = line.split("|")[0]
                value = line.split("|")[1].rstrip()
                if param == "DBPATH":
                    self.dbpath = value
                elif param == "PASS_ENC":
                    self.pass_enc = value
                    stream = os.popen(f"./mcrypt -d {self.pass_enc}")
                    self.pass_dec = stream.read().rstrip().lstrip()


    def getDbContent(self):
        kp = PyKeePass(self.dbpath, password=self.pass_dec)
        groups = kp.find_groups(name='.*', regex=True)
        print(groups)
        for group in groups:
            print(group, group.entries)


################################################################ 
# MAIN FLOW
################################################################

if len(sys.argv) > 1:
    confpath = sys.argv[1]
if confpath == "":
    print("Error: No configuration path provided!")
    exit(0)

km = Keepass_Manager()
km.readConf(confpath)

print(f"dbpath = {km.dbpath}")
print(f"pass_enc = {km.pass_enc}")
print(f"pass_dec = {km.pass_dec}")

km.getDbContent()
