# Converts the name of each file in the parameter files address
# by appending the parameter suffix to the previous file name.
#
# command line call
# python
# import sufname
# instance = sufname
# instance.convert(r"[files address]", "[suffix]")

import os

def convert(address : str, suffix : str):
    os.chdir(address)
    prev_files = os.listdir(address)
    print(prev_files)

    for prev_name in prev_files:

        new_name_arr = prev_name.split(".")
        new_name = (new_name_arr[0] + suffix)
        if new_name_arr.len < 1:
            i = 1
            while i < new_name_arr.len:
                new_name = (new_name + new_name_arr[i])
                i = (i + 1)

        os.rename(prev_name, new_name)

    new_files = os.listdir(address)
    print(new_files)

# internal call (uncomment to run)
# instance.convert(r"[files address]", "[suffix]")
