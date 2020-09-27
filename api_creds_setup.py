from argparse import ArgumentParser, PARSER
from base64 import urlsafe_b64encode
import os
import base64
import argparse
from cryptography.fernet import Fernet

PARSER = argparse.ArgumentParser()
PARSER.add_argument_group('required arguments')
PARSER.add_argument("--token", required=True, dest="GH_TOKEN", action="store")
PROGRAM_ARGS = PARSER.parse_args()

key = Fernet.generate_key()
cipher_suite = Fernet(key)
cipher_text = cipher_suite.encrypt(bytes(PROGRAM_ARGS.GH_TOKEN, 'ascii'))

export_stmts = ['\nexport GH_KEY="' + key.decode('utf-8') + '"\n', 
                'export GH_TOKEN="' + cipher_text.decode('utf-8') + '"\n']

env_file_path = os.environ['HOME'] + '/.zshrc'
#if MacOS, write encrypted token and key to .zshrc
try:
    if os.path.exists(env_file_path):
        with open(env_file_path, mode='a+') as zshrc:
            zshrc.writelines(export_stmts)
            zshrc.close()
except FileNotFoundError:
    print("zshrc not found")


env_file_path = os.environ['HOME'] + '/.bashrc'

#if Ubuntu or similar, write encrypted token and key to .bashrc
try:
    if os.path.exists(env_file_path):
        with open(env_file_path, mode='a+') as bashrc:
            bashrc.writelines(export_stmts)
            bashrc.close()
except FileNotFoundError:
    print("bashrc not found")
