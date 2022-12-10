# Write the pubkey from local machine to the pubkey file
import os
import sys

home_dir = os.path.expanduser('~')
local_pubkey_file = os.path.join(home_dir, '.ssh', 'id_rsa.pub')
if not os.path.exists(local_pubkey_file):
    print('No pubkey file found')
    sys.exit(1)

os.system('git pull')

with open(local_pubkey_file, encoding='utf-8') as f:
    local_pubkey = f.read()
with open('pubkeys', encoding='utf-8') as f:
    public_pubkeys = f.read()
if local_pubkey not in public_pubkeys:
    with open('pubkeys', 'a', encoding='utf-8') as f:
        f.write('\n' + local_pubkey)

os.system('git add pubkeys')
os.system('git commit -m "Update pubkey"')

print('Pubkey updated')
