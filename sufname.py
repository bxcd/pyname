# sufname
# Converts the name of each file in the specified files address
# by appending the specified suffix to the previous file name.
# Ignores a number of consecutive period delimeters up to the specified count.
#
# From the command line, enter the following:
# python
# import sufname
# yourvar = sufname
# yourvar.convert(r"[files address]", "[suffix]", count ignored delims])

import os

def convert(address : str, suffix : str, delim : int):

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

def help():

    print("# sufname\n" +
	  "# Converts the name of each file in the specified files address\n" +
	  "# by appending the specified suffix to the previous file name.\n" +
	  "# Ignores a number of consecutive period delimeters up to the specified integer.\n" +
	  "#\n" +
	  "# From the command line, enter the following:\n" +
	  "# python\n" +
	  "# import sufname\n" +
	  "# yourvar = sufname\n" +
	  "# yourvar.convert(r\"[files address]\", \"[suffix]\", [num ignored delims])")
