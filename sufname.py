# Converts the name of each file in the parameter files address
# by appending the parameter suffix to the previous file name.
# ignores period delimeters up to the parameter index.
#
# command line call
# python
# import sufname
# instance = sufname
# instance.convert(r"[files address]", "[suffix]", 1)

import os

def convert(address : str, suffix : str; delim : int):

    os.chdir(address)
    prev_files = os.listdir(address)
    print(prev_files)

    for prev_name in prev_files:

        prev_name_arr = prev_name.split(".")
        new_name = (prev_name_arr[0] + suffix)

        i = delim
        arr_len = len(prev_name_arr)

        while i < arr_len:

            new_name = (new_name + "." + prev_name_arr[i])
            i = (i + 1)

        os.rename(prev_name, new_name)

    new_files = os.listdir(address)
    print(new_files)

# internal call (uncomment to run)
# convert(r"[files address]", "[suffix]", 1)
