# extname
# Converts the name of each file in the parameter files address
# by appending the parameter extentsion to the previous file name.
#
# From the command line, enter the following:
# python
# import extname
# yourvar = extname
# yourvar.convert(r"[files address]", "[extentsion]")

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

def help():

    print("# extname\n" +
	  "# Converts the name of each file in the parameter files address\n" +
	  "# by appending the parameter extentsion to the previous file name.\n" +
	  "#\n" +
	  "# From the command line, enter the following:\n" +
	  "# python\n" +
	  "# import extname\n" +
	  "# yourvar = extname\n" +
	  "# yourvar.convert(r\"[files address]\", \"[extentsion]\")")