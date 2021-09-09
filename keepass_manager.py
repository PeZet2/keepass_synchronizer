#!/usr/bin/python3

import sys
from pykeepass import PyKeePass

confpath = ""

if len(sys.argv) > 1:
    confpath = sys.argv[1]
if confpath == "":
    print("Error: No configuration path provided!")
    exit(0)


def readConf(filepath):
    global dbpath, pass_enc

    with open(filepath, 'r') as f:
        for line in f.readlines():
            param = line.split("=")[0]
            value = line.split("=")[1].rstrip()
            if param == "DBPATH":
                dbpath = value
            elif param == "PASS_ENC":
                pass_enc = value
  
readConf(confpath)

print(f"dbpath = {dbpath}")
print(f"pass_enc = {pass_enc}")


pass_dec = "pydb12"

kp = PyKeePass(dbpath, password=pass_dec)
