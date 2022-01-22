# Converts the name of each file in the parameter files address
# by replacing the parameter previous key with the parameter new key.
# Parameter previous key is case insensitive.
#
# command line call
# python
# import modname
# instance = modname
# instance.convert(r"[files address]", "[old key]", "[new key]")

import os

def convert(address : str, prev_key : str, new_key : str):
    os.chdir(address)
    prev_files = os.listdir(address)
    print(prev_files)

    for prev_name in prev_files:

        prev_key = prev_key.lower()
        prev_name = prev_name.lower()
        key_find = prev_name.find(prev_key)
        if (key_find != -1):
            new_name = prev_name.replace(prev_key, new_key)
            os.rename(prev_name, new_name)

    new_files = os.listdir(address)
    print(new_files)

# internal call (uncomment to run)
# convert(r"[files address]", "[old key]", "[new key]")
