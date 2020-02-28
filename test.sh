#!/bin/bash

python3 crack.py -f users.md5 -r rainbow.md5 -a md5
python3 crack.py -f users.sha1 -r rainbow.sha1 -a sha1
python3 crack.py -f users.sha256 -r rainbow.sha256 -a sha256

python3 crack.py -f users_salted.md5 -r rainbow.md5 -a md5
python3 crack.py -f users_salted.sha1 -r rainbow.sha1 -a sha1
python3 crack.py -f users_salted.sha256 -r rainbow.sha256 -a sha256
