# Converts the name of each file in the parameter files address
# by appending the parameter extentsion to the previous file name.
#
# command line call
# python
# import extname
# instance = extname
# instance.convert(r"[files address]", "[extentsion]")

import os

def convert(address : str, extentsion : str):

    os.chdir(address)
    prev_files = os.listdir(address)
    print(prev_files)

    for prev_name in prev_files:

        new_name = (prev_name + "." + extentsion)
        os.rename(prev_name, new_name)

    new_files = os.listdir(address)
    print(new_files)

# internal call (uncomment to run)
# convert(r"[files address]", "[extentsion]")
