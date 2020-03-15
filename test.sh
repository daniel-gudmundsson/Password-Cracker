#!/bin/bash

python3 cracker.py -f users.md5 -r md5.rainbow -o users_md5.out -b -m 5 -n 5
python3 cracker.py -f users.sha1 -r sha1.rainbow -o users_sha1.out -b -m 5 -n 5
python3 cracker.py -f users.sha256 -r sha256.rainbow -o users_sha256.out -b -m 5 -n 5 

python3 cracker.py -f users_salted.md5 -r md5_salted.rainbow -o users_salted_md5.out -b -m 4 -n 4
python3 cracker.py -f users_salted.sha1 -r sha1_salted.rainbow -o users_salted_sha1.out -b -m 4 -n 4
python3 cracker.py -f users_salted.sha256 -r sha256_salted.rainbow -o users_salted_sha256.out -b -m 4 -n 4
