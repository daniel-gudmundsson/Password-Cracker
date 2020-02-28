import os
import argparse
from lib.hashfn import hash_pw

def to_rainbow(passwords, rainbow, algo):
	if not algo in ["md5","sha1","sha256"]:
		raise Exception("Invalid algorithm '%s'" % algo)
	with open(passwords, "r") as f_in:
		with open(rainbow, "w") as f_out:
			for l in f_in:
				l = l.strip(" \r\n")
				if not l or len(l)==0: continue
				f_out.write("%s:%s\n" % (hash_pw(l, algo=algo), l))
def to_rainbow_withsalt(passwords, rainbow, algo):
	if not algo in ["md5","sha1","sha256"]:
		raise Exception("Invalid algorithm '%s'" % algo)
	with open(passwords, "r") as f_in:
		with open(rainbow, "w") as f_out:
			for l in f_in:
				l = l.strip(" \r\n")
				if not l or len(l)==0: continue
				f_out.write("%s:%s\n" % (hash_pw(l, algo=algo, salt = l[:4],useSalt=False), l[4:]))
#
# Parse some arguments
#
parser = argparse.ArgumentParser('Generate a rainbow table')
parser.add_argument('passwords', help="The passwords file")
parser.add_argument('rainbow', help="The output - rainbow file")
parser.add_argument('-v', '--verbose', help="Verbose output", action="store_true")
parser.add_argument('-a', '--algorithm', help="algorithm (md5,sha1,sha256)", dest="algo")
parser.add_argument('-s', '--salt', help="salt", action="store_true",dest = "withsalt")
args = parser.parse_args()

passwords = args.passwords
rainbow = args.rainbow
algo = args.algo
withsalt = args.withsalt

if withsalt:
    to_rainbow_withsalt(passwords, rainbow, algo)
else:
    to_rainbow(passwords, rainbow, algo)
