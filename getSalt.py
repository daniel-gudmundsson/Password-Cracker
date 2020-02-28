import argparse

def getSalt(hashed):
    temp = hashed.split('$')
    salt = temp[2]
    return salt

parser = argparse.ArgumentParser('Generate a rainbow table')
parser.add_argument('passwords', help="The passwords file")
parser.add_argument('output', help="The output - rainbow file")
args = parser.parse_args()

passwords = args.passwords
output = args.output

with open(passwords, "r") as f_in:
		with open(output, "w") as f_out:
			for l in f_in:
				l = l.strip(" \r\n")
				if not l or len(l)==0: continue
				f_out.write("%s\n" % getSalt(l))