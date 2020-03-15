import os
import sys
import argparse
from lib.hashfn import hash_pw
import time
from collections import defaultdict

start_time = time.time()

class Cracker():
    
    def __init__(self, rainbow = None, algo = "md5", min_brute = 4, max_brute = 5, verbose = False):
        self.rainbow = {}
        self.rainbow_algo = None
        self.rainbow_file = rainbow
        self.algo = algo
        self.verbose = verbose
        if self.rainbow_file:
            self.__load_rainbow(self.rainbow_file)
            
        self.salt = []
        self.cracked = defaultdict(lambda : False)
        self.passwords = {} # (HASH, user)
        self.numPasswords = 0
        self.minBruteForceLenght = min_brute
        self.maxBruteForceLength = max_brute
        self.symbols = list("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1#$%&*?")
        self.crack80 = False
      
    def info(self):
        print("\n Cracker")
        print("Algorithm:")
    
    
    def crack(self, userhash = None, hashfile = None, output = None, brute = False):
        if not userhash and not hashfile:
            raise Exception("Nothing to crack!")
        if userhash:
            return self.__crack_single(userhash)
        else:
            return self.__crack_file(hashfile, output, brute)
    
    def __crack_single(self, userhash):
        user, hash = self.__split_user(userhash)
        if not hash or hash == "":
            raise Exception('Invalid has format')
        pw = self.__get_from_rainbow(hash)
#        print(pw)
        if pw:
            self.cracked[hash] = True
            return user, pw, 1,1
        else:
            return None, None, 1, 0
    
    def convertToWord(self, stringList):
        """Maps the stringList into a word"""
        word = ''
        for i in stringList:
            if i == -1:
                break
            word+=self.symbols[i]
        
        return word
    
    def incrementList(self, stringList):
        """ Increments the stringList in order to check the next word
            e.g. if the current word is aaa then the next word should be aab
            and so on
        """
        end= 0
        while end < len(stringList):
            if stringList[end] == -1:
                break
            end+=1
        i = end-1
        
        stop = False
        while not stop:
            if stringList[i]+1 > 68:
                stringList[i] = 0
                i-=1
                if i < 0:
                    stringList[end] = 0
                    stop = True
            else:
                stringList[i]+=1
                stop = True
        return stringList
            
      
    def bruteForce(self,cracked, output):
        """ Brute forces a password to crack it. Tries every combination
            of letters by creating strings from minBruteForceLength to maxBruteForceLenght.
            It then checks for each word if the hash of it exists in the password file
        """
        f_out = open(output, 'a')
        stringList = [-1]*self.maxBruteForceLength
        stringList[0] = 0
        stringList[:self.minBruteForceLenght] = [0 for i in range(self.minBruteForceLenght)]
        while True:
        
            if self.salt == []: ## No salt
                word = self.convertToWord(stringList)
#                    print(word)
                hash = hash_pw(word, algo = self.algo)
                if hash in self.passwords and not self.cracked[hash]:
                    user = self.passwords[hash]
                    cracked +=1
                    if cracked/self.numPasswords >= 0.8 and not self.crack80:
                        self.crack80 = True
                        print('80% or more passwords cracked in %s seconds' %(time.time() - start_time))
                    self.cracked[hash] = True
                    print("%.1f - %s - %s" % (100*(float(cracked)/self.numPasswords),user,word))
                    f_out.write("%s:%s\n" % (user,word))
                    if cracked == self.numPasswords:
                        break
            
            else:
#                    print(self.salt)
                word = self.convertToWord(stringList)
                for salt in self.salt:
#                        saltedWord = salt+word
                    hash = hash_pw(word, algo = self.algo, salt = salt, useSalt=True)
                    if hash in self.passwords and not self.cracked[hash]:
                        user = self.passwords[hash]
                        cracked +=1
                        if cracked/self.numPasswords >= 0.8 and not self.crack80:
                            self.crack80 = True
                            print('80% or more passwords cracked in %s seconds' %(time.time() - start_time))
                        self.cracked[hash] = True
                        print("%.1f - %s - %s" % (100*(float(cracked)/self.numPasswords),user,word))
                        f_out.write("%s:%s\n" % (user,word))
                        break
                        
                    if cracked == self.numPasswords:
                        break
            if sum(stringList) == len(stringList) * 68:
                break
            
            stringList = self.incrementList(stringList)
        
        return cracked
        
    def __crack_file(self, hashfile, output, brute):
        total = 0
        cracked = 0
        if not output:
            filename,_ =  os.path.splitext(hashfile)
            output = filename + ".out"
        with open(hashfile, 'r') as f_in:
            with open(output, 'w') as f_out:
                for l in f_in:
                    l = l.strip(" \r\n")
#                    print(l)
                    if not l or len(l)== 0: continue
                    total+=1
                    user, pw, _,_ = self.__crack_single(l)
#                    print(user, pw)
                    if user and pw:
                        cracked +=1
                        if cracked/self.numPasswords >= 0.8 and not self.crack80:
                            self.crack80 = True
                            print('80% or more passwords cracked in %s seconds' %(time.time() - start_time))
#                        self.cracked[pw] = True
                        print("%.1f - %s - %s" % (100*(float(cracked)/total),user,pw))
                        f_out.write("%s:%s\n" % (user,pw))
        
        if brute and cracked < self.numPasswords:
            cracked = self.bruteForce(cracked, output)
            
            
        output_file = open(output, 'a')
        output_file.write("Total:%d - Cracked:%d - Percent:%.1f\n" % (self.numPasswords,cracked,100*(float(cracked)/total)))
        return None,None,total,cracked
    
    
    def __get_from_rainbow(self,hash):
#        print(self.rainbow)
#        print(self.rainbow_algo)
        if self.rainbow == {} or self.rainbow_algo == None: return None
        algo,_,_ = self.__split_hash(hash)
#        print(algo)
        if not algo == self.rainbow_algo:
            raise Exception("Hash algorithm not compatible with loaded rainbow")
        if not hash in self.rainbow:
            return None
        return self.rainbow[hash]

    def __split_user(self, userhash):
        if userhash.find(":")<0: return None,userhash
        user,hash = userhash.split(":")
        return user,hash
        
    
    def __split_hash(self, userhash):
        _,hashpart = self.__split_user(userhash)
        hashpart = hashpart.strip(" $")
        algo,hashpart = hashpart.split("$",1)
        if hashpart.find("$")<0:
            return algo,None,hashpart # Not salted
        else:
            salt,hash = hashpart.split("$",1)
        return algo,salt,hash # return full algo salt hash split
    
    
    def __load_rainbow(self, rainbow_file):
        self.rainbow={}
        self.rainbow_algo = None
#        print('hallo')
        with open(rainbow_file, "r") as f:
            for l in f:
                l = l.strip(" \r\n")
                if not l or len(l)==0: continue
                hash,plain = l.split(":")
                algo,_,_ = self.__split_hash(hash)
                if self.rainbow_algo == None: 
                    self.rainbow_algo = algo
                else:
                    if not algo == self.rainbow_algo: continue
                self.rainbow[hash]=plain
                if self.verbose: print("Loading '%s' for password '%s'" % (hash,plain)) 
        self.algo = self.rainbow_algo    # Override cracker algo if rainbow loaded
        
                
parser = argparse.ArgumentParser('Crack some passwords')
parser.add_argument('-p', '--password-hash', help="A single password hash", dest="passhash")
parser.add_argument('-f', '--password-file', help="A file of hashed passwords", dest="passhashfile")
parser.add_argument('-r', '--rainbow-file', help="A rainbow file to help us crack", dest="rainbow")
parser.add_argument('-o', '--output-file', help="The cracked passwords", dest="output")
parser.add_argument('-b', '--brute', help = 'Use brute force',action="store_true", dest="brute")
parser.add_argument('-m', '--min-word-length', help = 'Min length of a brute force word', dest="min")
parser.add_argument('-n', '--max-word-length', help = 'Max length of a brute force word', dest="max")
parser.add_argument('-a', '--algorithm', help="Algorithm (md5,sha1,sha256)", dest="algo")
parser.add_argument('-i', '--info', help="Display info and quit", action="store_true")
parser.add_argument('-v', '--verbose', help="Verbose output", action="store_true")
args = parser.parse_args()                
                
                
                
passhash = args.passhash
passhashfile = args.passhashfile
output = args.output
rainbow = args.rainbow
algo = args.algo
brute = args.brute
min_brute = int(args.min)
max_brute = int(args.max)

if not algo: algo = "md5"
#if not method and rainbow: method="rainbow"
#if not method and not rainbow: brute = True              
      

c = Cracker(rainbow=rainbow, algo=algo, min_brute = min_brute, max_brute = max_brute)          
                
### Start by reading in the passwords file and create a dictonary that maps a hash to a user
with open(passhashfile, "r") as f:
    for l in f:
        l = l.strip(" \r\n")
        l = l.split('$')
#        print(l)
        if len(l) == 4: # Has salt
            user, algo, salt, pw = l
            user.strip(':')
            c.salt.append(salt)
            res = "$%s$" % algo
            res += salt + "$"
            res+=pw
            c.passwords[res] = user
        else:
            user, algo, pw = l
            user.strip(':')
            res = "$%s$" % algo
            res+=pw
            c.passwords[res] = user
        c.numPasswords+=1   

if args.info:                
    c.info()
    sys.exit(0)
                
if passhash:                
    user,pw,_,_ = c.crack(userhash=passhash)
    if user and pw:
        print("User:%s - Password:%s" % (user,pw))
    else:
        print("Not cracked")
if passhashfile:
    _,_,total,cracked = c.crack(hashfile=passhashfile, output=output, brute = brute)
    print("Total:%d - Cracked:%d - Percent:%.1f" % (total,cracked,100*(float(cracked)/total)))   
         
                
print("Finished in %s seconds" % (time.time() - start_time))                
                
                
                
                
                
                
                
                
                