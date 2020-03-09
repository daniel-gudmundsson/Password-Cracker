import os
import hashlib
import base64
import re
import argparse
import itertools
import time

start_time = time.time()

def extractSalt(saltedHash):
    salts = []
    for s in saltedHash:
        salts.append(s.split('$')[2])
    return salts
parser = argparse.ArgumentParser('Crack some passwords')
parser.add_argument('passwords', help="A file of hashed passwords")
parser.add_argument('output', help="The cracked passwords")
parser.add_argument('salt', help="The cracked passwords")

args = parser.parse_args()

password_file = args.passwords
output = args.output
salt_file = args.salt


saltedPasswords = []
with open(salt_file, "r") as f_in:
    for pw in f_in:
        pw = pw.strip(" \r\n")
        saltedPasswords.append(pw)

salts = extractSalt(saltedPasswords)

with open(password_file, "r") as f_in:
    with open(output, "w") as f_out:
        for pw in f_in:
            pw = pw.strip(" \r\n")
            lsts = [salts,[pw]]
            new = list(map(lambda x: "".join(x), list(itertools.product(*lsts))))
            for p in new:
                f_out.write("%s\n" % p)
print("Finished in %s seconds" % (time.time() - start_time))