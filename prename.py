# prename
# Converts the name of each file in the parameter files address
# by appending the parameter prefix to the previous file name.
#
# From the command line, enter the following:
# python
# import prename
# yourvar = prename
# yourvar.convert(r"[files address]", "[prefix]")

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
# convert(r"[files address]", "[prefix]")

def help():

    print("# prename\n" +
	  "# Converts the name of each file in the parameter files address\n" +
	  "# by appending the parameter prefix to the previous file name.\n" +
	  "#\n" +
	  "# From the command line, enter the following:\n" +
	  "# python\n" +
	  "# import prename\n" +
	  "# yourvar = prename\n" +
	  "# yourvar.convert(r\"[files address]\", \"[prefix]\")")

