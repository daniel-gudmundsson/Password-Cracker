import os
import hashlib
import base64
import argparse

parser = argparse.ArgumentParser('Generate a rainbow table')
parser.add_argument('file', help="The passwords file")
args = parser.parse_args()

file = args.file
with open(file, "r") as f_in:
    i = 1
    for l in f_in:
        user,hashpart = l.split(":")
        hashpart = hashpart.strip(" $")
        if len(hashpart.split("$",1))<2:
            print(i)
        i+=1

