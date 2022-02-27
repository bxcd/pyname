# modname
# Converts the name of each file in the parameter files address
# by replacing the parameter previous key with the parameter new key.
# Parameter previous key is case insensitive.
#
# From the command line, enter the following:
# python
# import modname
# yourvar = modname
# yourvar.convert(r"[files address]", "[old key]", "[new key]")

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

def help():

    print("# modname\n" +
	  "# Converts the name of each file in the parameter files address\n" +
	  "# by replacing the parameter previous key with the parameter new key.\n" +
	  "# Parameter previous key is case insensitive.\n" +
	  "#\n" +
	  "# command line call\n" +
	  "# python\n" +
	  "# import modname\n" +
	  "# yourvar = modname\n" +
	  "# yourvar.convert(r\"[files address]\", \"[old key]\", \"[new key]\")")
