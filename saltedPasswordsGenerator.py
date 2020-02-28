import argparse

def getSaltedPass(password, salts):
    res = []
    for salt in salts:
        res.append('%s%s' % (salt, password))
    return res



#salt  = ['hallo', 'world']
#pw = 'yes'
#
#ans = getSaltedPass(pw, salt)
#print(ans)
parser = argparse.ArgumentParser('Generate a rainbow table')
parser.add_argument('passwords', help="The passwords file")
parser.add_argument('salt', help="The salt file")
parser.add_argument('output', help="The output - salted passwords")
args = parser.parse_args()

passwords = args.passwords
salt = args.salt
output = args.output

salts = []
with open(salt, "r") as f_in:
    for l in f_in:
        l = l.strip(" \r\n")
        salts.append(l)
with open(passwords, "r") as f_in:
    with open(output, "w") as f_out:
        for l in f_in:
            l = l.strip(" \r\n")
            if not l or len(l)==0: continue
            saltedPass = getSaltedPass(l, salts)
#            print(saltedPass)
            for word in saltedPass:
                f_out.write("%s\n" % word)