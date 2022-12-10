# Write the public pubkeys to local authorized_keys file
import os

home_dir = os.path.expanduser('~')
local_authorized_keys_file = os.path.join(home_dir, '.ssh', 'authorized_keys')
if not os.path.exists(local_authorized_keys_file):
    local_authorized_keys = ""
else:
    with open(local_authorized_keys_file, encoding='utf-8') as f:
        local_authorized_keys = f.read()
with open('pubkeys', encoding='utf-8') as f:
    public_pubkeys = f.read()
for pubkey in public_pubkeys.splitlines():
    with open(local_authorized_keys_file, 'a', encoding='utf-8') as f:
        if pubkey not in local_authorized_keys:
            f.write('\n' + pubkey)

print('Authorized_keys updated')
