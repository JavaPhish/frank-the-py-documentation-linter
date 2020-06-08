#!/usr/bin/python3
""" documentation checker """
""" This is not a replacement for PEP8, rather
    a tool to be used with PEP8 to make sure all
    mandatory documentation is present """


import sys
import os.path


""" check argument count to make sure a filename was given"""
if len(sys.argv) != 2:
    print("USAGE: frank <filename>")
    print("Example: frank main.py")
    sys.exit(1)

""" Check if the file exists, cry about it if it doesnt """
if (os.path.isfile(sys.argv[1]) is False):
    print("File named: \"{}\" was not found".format(sys.argv[1]))
    sys.exit(1)

""" Open and read all contents from the file """
with open(sys.argv[1]) as file:
    codetxt = file.readlines()

print("")
print("_- Python documentation checker for Holberton students -_")

if (len(codetxt) < 1):
    print("This is an empty file...")
    sys.exit(1)

conflicts_found = 0
""" Loop through each line and try each line individually for expected documentation """
for i in range(0, len(codetxt)): 
    """ Check for python shebang """
    if (i == 0):

        if ("#!/usr/bin/python3" not in codetxt[0]):
            print(" ISSUE: Expecting \"#!/usr/bin/python3\" as first line. LINE 0")
            conflicts_found += 1

    """ File header comment thing """
    if (i == 1):
        if ("\"\"\"" not in codetxt[1]):
            print(" ISSUE: Expecting file head comment (after shebang). LINE: {}".format(i + 1))
            conflicts_found += 1

    """ Function definition comment """
    if ("def" in codetxt[i]):
        if (i + 1 == len(codetxt)):
            print(" ISSUE: Expecting comment after function definition. LINE: {}".format(i + 2))
            conflicts_found += 1
        elif ("\"\"\"" not in codetxt[i + 1]):
            print(" ISSUE: Expecting comment after function definition. LINE: {}".format(i + 2))
            conflicts_found += 1

    """ Class declaration comment """
    if ("class " in codetxt[i] and "__class__" not in codetxt[i] and "\"" not in codetxt[i]):
        if (i == len(codetxt) - 1):
            print(" ISSUE: Expecting comment after class declaration. LINE: {}".format(i + 2))
            conflicts_found += 1
        elif ("\"\"\"" not in codetxt[i + 1]):
            print(" ISSUE: Expecting comment after class declaration. LINE: {}".format(i + 2))
            conflicts_found += 1

print("---")

if (conflicts_found == 0):
    print("0 conflicts found -> Looks good!")
else:
    print("Total conflicts found: {}".format(conflicts_found))
print("")
