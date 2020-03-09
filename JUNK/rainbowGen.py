import argparse
import leetspeakConverter as leet
from lib.hashfn import hash_pw
import saltedPasswordsGenerator as saltpw


def getSalt(saltedFile):
    salts = []
    with open(saltedFile, 'r') as f_in:
        for s in f_in: 
            temp = s.split('$')
            salt = temp[2]
            salts.append(salt)
    return salts


parser = argparse.ArgumentParser('Generate a rainbow table')
parser.add_argument('passwords', help="The passwords file")
parser.add_argument('rainbow', help="The output - rainbow file")
parser.add_argument('-a', '--algorithm', help="algorithm (md5,sha1,sha256)", dest="algo")
parser.add_argument('-s', '--salt', help="salt",dest = "withsalt")
parser.add_argument('-l', help = 'leet', action = "store_true", dest = "toLeet")
parser.add_argument('-e', help = 'suffix', action = "store_true", dest = "suffix")
parser.add_argument('-r', help = 'random', action = "store_true")
args = parser.parse_args()

passwords = args.passwords
output = args.rainbow
algo = args.algo
saltedFile = args.withsalt
passwordList = []
with open(passwords, "r") as f_in:
    with open(output, 'w') as f_out:
        for pw in f_in:
    #        passwordList.append[pw]
            pw = pw.strip(" \r\n")
            passwordList = [pw]
            if args.toLeet:
                passwordList.extend(leet.wordToLeet(pw))
            if args.suffix:
                pass
            salted = []
            if args.withsalt:
                for p in passwordList:
                    salt = getSalt(saltedFile)
                    salted.extend(saltpw.addsalt_single(p, salt))
                passwordList = list(salted) 
            for word in passwordList:
                if not args.withsalt:
                    f_out.write("%s:%s\n" % (hash_pw(word, algo=algo), word))
                else:
                    f_out.write("%s:%s\n" % (hash_pw(word, algo=algo, salt = word[:4],useSalt=False), word[4:]))
                

#with open(output, 'w') as f_out:
#    for pw in passwordList:
#        if not args.withsalt:
#            f_out.write("%s:%s\n" % (hash_pw(pw, algo=algo), pw))
#        else:
#            f_out.write("%s:%s\n" % (hash_pw(pw, algo=algo, salt = pw[:4],useSalt=False), pw[4:]))
