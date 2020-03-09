import os
import sys
import argparse
from lib.hashfn import hash_pw
import time

start_time = time.time()

class Cracker():
    
    def __init__(self, rainbow = None, algo = "md5", method = "rainbow", verbose = False):
        self.rainbow = {}
        self.rainbow_algo = None
        self.rainbow_file = rainbow
        self.algo = algo
        self.method = method
        self.verbose = verbose
        if self.rainbow_file:
            self.__load_rainbow(self.rainbow_file)
      
    def info(self):
        print("\n Cracker")
        print("Algorithm:")
    
    
    def crack(self, userhash = None, hashfile = None, output = None):
        if not userhash and not hashfile:
            raise Exception("Nothing to crack!")
        if userhash:
            return self.__crack_single(userhash)
        else:
            return self.__crack_file(hashfile, output)
    
    def __crack_single(self, userhash):
        user, hash = self.__split_user(userhash)
        if not hash or hash == "":
            raise Exception('Invalid has format')
        pw = self.__get_from_rainbow(hash)
#        print(pw)
        if pw:
            return user, pw, 1,1
        else:
            return None, None, 1, 0
    
    def __crack_file(self, hashfile, output):
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
                        print("%.1f - %s - %s" % (100*(float(cracked)/total),user,pw))
                        f_out.write("%s:%s\n" % (user,pw))
        
        output_file = open(output, 'a')
        output_file.write("Total:%d - Cracked:%d - Percent:%.1f\n" % (total,cracked,100*(float(cracked)/total)))
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
        
#        self.algo = self.rainbow_algo    # Override cracker algo if rainbow loaded
          # Override cracker algo if rainbow loaded
                
                
parser = argparse.ArgumentParser('Crack some passwords')
parser.add_argument('-p', '--password-hash', help="A single password hash", dest="passhash")
parser.add_argument('-f', '--password-file', help="A file of hashed passwords", dest="passhashfile")
parser.add_argument('-r', '--rainbow-file', help="A rainbow file to help us crack", dest="rainbow")
parser.add_argument('-o', '--output-file', help="The cracked passwords", dest="output")
parser.add_argument('-m', '--method', help="Method (brute,rainbow,rainbow_subst)", dest="method")
parser.add_argument('-a', '--algorithm', help="Algorithm (md5,sha1,sha256)", dest="algo")
parser.add_argument('-i', '--info', help="Display info and quit", action="store_true")
parser.add_argument('-v', '--verbose', help="Verbose output", action="store_true")
args = parser.parse_args()                
                
                
                
passhash = args.passhash
passhashfile = args.passhashfile
output = args.output
rainbow = args.rainbow
method = args.method
algo = args.algo

if not algo: algo = "md5"
if not method and rainbow: method="rainbow"
if not method and not rainbow: method="brute"                
                
                
c = Cracker(rainbow=rainbow, method=method, algo=algo)
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
    _,_,total,cracked = c.crack(hashfile=passhashfile, output=output)
    print("Total:%d - Cracked:%d - Percent:%.1f" % (total,cracked,100*(float(cracked)/total)))   
         
                
print("Finished in %s seconds" % (time.time() - start_time))                
                
                
                
                
                
                
                
                
                