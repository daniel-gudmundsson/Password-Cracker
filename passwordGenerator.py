import os
import hashlib
import base64
import re
import argparse
import itertools
import time

start_time = time.time()

def leet(passwords):
    """
        Converges a password to leetspeak
    """
    for pw in passwords:
        pw = pw.replace("o","0")
        pw = pw.replace("l","1")
        pw = pw.replace("e","3")
        pw = pw.replace("a","4")
        pw = pw.replace("s","5")
        passwordsAll.append(pw)


def symbol(passwords):
    """
        Adds a symbol as a suffix to the passwords
    """
    for pw in passwords:
        for s in symbols:
            passwordsAll.append(pw+s)

def random(passwords, base, n):
    """
    Generates random words. 
    n is the length of the words
    If a base is given then that base can be used in the calculation for random
    strings of one letter longer. If base is all the possible 4 letter words than it
    can be used to genearte five letter words in less time.
    """
    if base ==[]:
        lsts = []
        for i in range(n):
            lsts.append(symbols)
    #    lsts = [symbols, symbols, symbols, symbols]
    #    lsts.append(symbols)
        new = list(map(lambda x: "".join(x), list(itertools.product(*lsts))))
    else:
        lsts = [base, symbols]
        new = list(map(lambda x: "".join(x), list(itertools.product(*lsts))))
        
    passwordsAll.extend(new)
    return new
    
parser = argparse.ArgumentParser('Crack some passwords')
parser.add_argument('passwords', help="A file of hashed passwords")
parser.add_argument('output', help="The cracked passwords")
parser.add_argument('-r', '--random' ,action="store_true",dest="random")
args = parser.parse_args()

password_file = args.passwords
output = args.output
r = args.random

symbols = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1#$%&*?")
passwords = []
with open(password_file, "r") as f_in:
    for pw in f_in:
        pw = pw.strip(" \r\n")
        passwords.append(pw)

passwordsAll = list(passwords)    

leet(passwords)
symbol(passwords)
if r:    ### If we want random words.
    base4 = random(passwords, [], 4)
#base5 = random(passwords, base4, 5) ### To slow and not enough memory to execute this line
with open(output, "w") as f_out:
    for pw in passwordsAll:
        f_out.write("%s\n" % pw)


print("Finished in %s seconds" % (time.time() - start_time))








       