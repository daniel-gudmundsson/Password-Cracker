import os
import hashlib
import base64

def hash_pw(s, algo="md5", gen_salt=False, salt=None, useSalt = False):
	if not algo in ["md5","sha1","sha256"]:
		raise Exception("Algorithm '%s' is not supported" % algo)
	res = "$%s$" % algo
	if gen_salt:
		salt = gensalt()
	if salt:
            if useSalt:
                s = salt + s
            res += salt + "$"
	if algo == "md5":
		hashed=hashlib.md5(s.encode('utf-8'))
	if algo == "sha1":
		hashed=hashlib.sha1(s.encode('utf-8'))
	if algo == "sha256":
		hashed=hashlib.sha256(s.encode('utf-8'))
	return res+encode(hashed.hexdigest())

def gensalt():
	r = os.urandom(32)
	return base64.b64encode(r)[:4].decode('utf-8').lower()

def encode(s):
	return base64.b64encode(s.encode('utf-8')).decode('utf-8').strip("= ").lower()

def verify(s, hash):
	hash = hash.strip(" $\r\n")
	algo,rest = hash.split("$",1)
	if "$" in rest:
		salt, hash = rest.split("$")
		v = hash_pw(s, algo, salt=salt)
	else:
		v = hash_pw(s, algo)
	v = v[v.rfind("$",1)+1:]
	return v==hash

#print(hash_pw('password'))