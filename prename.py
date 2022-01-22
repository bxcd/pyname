# Converts the name of each file in the parameter files address
# by appending the parameter prefix to the previous file name.
#
# command line call
# python
# import prename
# instance = prename
# instance.convert(r"[files address]", "[prefix]")

import os

def convert(address : str, prefix : str):
    
    os.chdir(address)
    prev_files = os.listdir(address)
    print(prev_files)

    for prev_name in prev_files:

        new_name = (prefix + prev_name)
        os.rename(prev_name, new_name)

    new_files = os.listdir(address)
    print(new_files)

# internal call (uncomment to run)
# instance.convert(r"[files address]", "[prefix]")
