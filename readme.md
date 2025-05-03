# pyname

Custom utility functions for bulk revision of filenames. 

## Instructions

To use: 
* Run python (enter 'python')
* Import the desired function(s) (enter 'import [func name]')
* Assign a function instance to a variable (enter '[var name] = [func name]')
* Invoke from the variable either the convert([params...]) or help() functions
* The help() function specifies the parameters for the convert function.

### numname

Converts the name of each file in the specified files address to a number in an ordered sequence starting from the specified index. Ignores a number of consecutive period delimeters up to the specified count.

### prename

Converts the name of each file in the specified files address by appending the specified prefix to the previous file name.

### modname

Converts the name of each file in the specified files address by replacing the specified previous key with the specified new key. Parameter previous key is case insensitive.

### sufname

Converts the name of each file in the specified files address by appending the specified suffix to the previous file name. Ignores a number of consecutive period delimeters up to the specified count.

### extname

Converts the name of each file in the parameter files address by appending the specified extension to the previous file name.

## Attribution

Made with Python.

#### Author: John Basil
#### Date:   22 Jan 2022
