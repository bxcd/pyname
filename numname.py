# numname
# Converts the name of each file in the specified files address
# to a number in an ordered sequence starting from the specified index.
# Ignores a number of consecutive period delimeters up to the specified count.
#
# From the command line, enter the following:
# python
# import numname
# yourvar = numname
# yourvar.convert(r"[files address]", [sequence initial index], [ignored delims count])

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
	  "# Converts the name of each file in the specified files address\n" +
	  "# to a number in an ordered sequence starting from the specified index.\n" +
	  "# Ignores a number of consecutive period delimeters up to the specified count.\n" +
	  "#\n" +
	  "# From the command line, enter the following:\n" +
	  "# python\n" +
	  "# import numname\n" +
	  "# yourvar = numname\n" +
	  "# yourvar.convert(r\"[files address]\", [sequence initial index], [ignored delims count])")
