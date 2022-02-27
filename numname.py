# numname
# Converts the name of each file in the parameter files address
# to a number in an ordered sequence starting from the parameter integer.
# Ignores period delimeters up to the parameter index.
#
# From the command line, enter the following:
# python
# import numname
# yourvar = numname
# yourvar.convert(r"[files address]", [num sequence initial], [num ignored delims])

import os

def convert(address : str, start : int, delim : int):

    os.chdir(address)
    prev_files = os.listdir(address)
    print(prev_files)

    n = start;

    for prev_name in prev_files:

        new_name = str(n)

        i = delim
        prev_name_arr = prev_name.split(".")
        arr_len = len(prev_name_arr)

        while i < arr_len:

            new_name = (new_name + "." + prev_name_arr[i])
            i = (i + 1)

        n = (n + 1)
        os.rename(prev_name, new_name)

    new_files = os.listdir(address)
    print(new_files)

# internal call (uncomment to run)
# convert(r"[files address]", 1, 1)

def help():

    print("# numname\n" +
	  "# Converts the name of each file in the parameter files address\n" +
	  "# to a number in an ordered sequence starting from the parameter integer.\n" +
	  "# Ignores period delimeters up to the parameter index.\n" +
	  "#\n" +
	  "# From the command line, enter the following:\n" +
	  "# python\n" +
	  "# import numname\n" +
	  "# yourvar = numname\n" +
	  "# yourvar.convert(r\"[files address]\", [num sequence initial], [num ignored delims])")
