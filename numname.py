# Converts the name of each file in the parameter files address
# to a number in an ordered sequence starting from the parameter integer.
#
# command line call
# python
# import numname
# instance = numname
# instance.convert(r"[files address]", 1)

import os

def convert(address : str, start : int):

    os.chdir(address)
    prev_files = os.listdir(address)
    print(prev_files)

    i = start;

    for prev_name in prev_files:

        new_name = str(i)
        os.rename(prev_name, new_name)
        i = (i + 1)

    new_files = os.listdir(address)
    print(new_files)

# internal call (uncomment to run)
# convert(r"[files address]", 1)
