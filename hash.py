import os
import argparse
from lib.hashfn import hash_pw

def to_hashed(users_file, hashed_file, algo, salted=False):
	if not algo in ["md5", "sha1", "sha256"]:
		raise Exception("Invalid algorithm '%s'" % algo)
	with open(users_file, "r") as f_in:
		with open(hashed_file, "w") as f_out:
			for l in f_in:
				l = l.strip(" \r\n")
				if not l or len(l) == 0: continue
				user,passwd = l.split(":")
				print("hashing - user:%s, pass:%s" % (user,passwd))
				hashed = hash_pw(passwd, algo=algo, gen_salt=salted)
				f_out.write("%s:%s\n" % (user, hashed))

#
# Parse some arguments
#
parser = argparse.ArgumentParser('Hash my users passwords')
parser.add_argument('users', help="The users file")
parser.add_argument('hashed', help="The output - usernames and hashed passwords")
parser.add_argument('-v', '--verbose', help="Verbose output", action="store_true")
parser.add_argument('-s', '--salted', help="Salt the hash", action="store_true")
parser.add_argument('-a', '--algorithm', help="algorithm (md5,sha1,sha256)", dest="algo")
args = parser.parse_args()

users_file = args.users
output_file = args.hashed
algo = args.algo
salted = args.salted
if not algo or algo=="": algo="md5"

to_hashed(users_file, output_file, algo, salted=salted)
