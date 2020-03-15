CRACKER3000
=======

Höfundar:
Daníel Þór Guðmundsson dthg7@hi.is
Agnar Pétursson agp11@hi.is

í þessu verkefni fáum við að kynnast "lykilorða brjótara". Cracker-inn getur brotið bæði söltuð og ósöltuð lykilorð fyrir 3 tegundir af höshum: md5, sha1, sha256. Hugbúnaðurinn notast við regnbogatöflur og brute force aðferðir. 

Tilgangur verkefnisins er að kynnast betur þeim aðferðum sem notaðar eru til að brjóta lykilorð og reyna að útfæra þær á eigin spýtur. Við fáum að kynnast hvernig mismunandi hash algóritmar hafa áhrif á flækjustig lykilorða. Einnig fáum við að sjá hvernig það að bæta við salti getur reynst öflug aðferð þegar það kemur að því að auka öryggi lykilorða.

Við höfum fengið gefnar 6 skrár sem innihalda höshuð lykilorða. Fyrir hvern algóritma höfum við eina saltaða skrá og eina ósaltaða skrá. Markmiðið er að reyna að brjóta sem flest lykilorð í þessum skrám.

Þetta verkefni er partur áfanganum Öryggi Tölvukerfa (HBV602M) í Háskóla Íslands. 


cracker.py		Brýtur lykilorð
hash.py			Býr til lykilorðaskrá
rainbow.py		Býr til regnbogatöflu

lib/hashfn.py		Hash library

test.sh			Skeljaskript sem prófar afkóðun

users.md5		Lykilorðaskrár án salts
users.sha1
users.sha256

users_salted.md5	Lykilorðaskrár með salti
users_salted.sha1
users_salted.sha256

passwords.txt		Listi af þekktum lykilorðum

Requires python3

# Programs:

* passwordGenerator.py
* * [password file] used as a basis
* * [output file]
* -r (include random passwords of length 4)
Example: python3 passwordGenerator.py passwords.txt passwordsAll.txt -r

* saltedPasswordGenrator.py
* * [password file]
* * [output]
* * [salt]

* rainbow.py
* * [password file]
* * [output rainbow file]
* * -v (verbose)
* * -a [algorithm]
* * -s (indicates that the passwords are already salted)

* cracker.py
* * -p [single hash]
* * -f [file of hashes]
* * -r [rainbow table]
* * -o [output]
* * -b (use brute force)
* * -m (min brute force word length)
* * -n (max brute force word length)
* * -a [algorithm]
* * -i [info]
* * -v [verbose]


# Use case scenarion:
* **Generate files to make rainbow tables from**
* * python3 passwordGenerator.py passwords.txt passwordsAll.txt -r (Create all passwords)
* * python3 passwordGenerator.py passwords.txt passwordsAll_noRandom.txt (No random)
* * python3 saltedPasswordGenerator.py passwordsAll_noRandom.txt passwords_salted.md5 users_salted.md5 (create salted version of the passwords)
* * python3 saltedPasswordGenerator.py passwordsAll_noRandom.txt passwords_salted.sha1 users_salted.sha1
* * python3 saltedPasswordGenerator.py passwordsAll_noRandom.txt passwords_salted.sha256 users_salted.sha256
* **Generate rainbow files**
* python3 rainbow.py passwordsAll.txt md5.rainbow -a md5
* python3 rainbow.py passwordsAll.txt sha1.rainbow -a sha1
* python3 rainbow.py passwordsAll.txt sha256.rainbow -a sha256
* python3 rainbow.py passwords_salted.md5 md5_salted.rainbow -a md5 -s
* python3 rainbow.py passwords_salted.sha1 sha1_salted.rainbow -a sha1 -s
* python3 rainbow.py passwords_salted.sha256 sha256_salted.rainbow -a sha256 -s
* **Crack passwords**
* python3 cracker.py -f users.md5 -r md5.rainbow -o users_md5.out -b -m 5 -n 5
* python3 cracker.py -f users.sha1 -r sha1.rainbow -o users_sha1.out -b -m 5 -n 5
* python3 cracker.py -f users.sha256 -r sha256.rainbow -o users_sha256.out -b -m 5 -n 5 
* python3 cracker.py -f users_salted.md5 -r md5_salted.rainbow -o users_salted_md5.out -b -m 4 -n 4
* python3 cracker.py -f users_salted.sha1 -r sha1_salted.rainbow -o users_salted_sha1.out -b -m 4 -n 4
* python3 cracker.py -f users_salted.sha256 -r sha256_salted.rainbow -o users_salted_sha256.out -b -m 4 -n 4

# Setting up Virtualenv

Set up
sudo apt-get install virtualenv

Make a new directory
mkdir cracker
cd cracker
virtualenv -p python3 VENV

Activate VENV
source VENV/bin/activate

There are no packages that are required to run this software

To exit VENV
deactivate









