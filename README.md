<h1>Frank</h1>
<h3>A documentation checker to help Holberton students along with PEP8</h3>
-   -   -
Usage: 

	frank <filename.py>
	Ex. frank main.py

Warnings:
	
	-Frank does not work with wildcards because i havent figured that out yet in python.
	-He still has a few false flags, trust but verify his output.
	-Frank is not a replacement for PEP8, but rather something to be used along side of PEP8
	because PEP8 Does not check for documentation that is mandatory for Holberton students. 

Example usages/output cases:

	root@JavaFish:~/doc_check# frank test.py 

	_- Python documentation checker for Holberton students -_
	 ISSUE: Expecting comment after function definition. LINE: 10
	---
	Total conflicts found: 1

-----------------------------
	root@JavaFish:~/doc_check# frank test.py 

	_- Python documentation checker for Holberton students -_
	---
	0 conflicts found -> Looks good!

-----------------------------

All of Franks expectations (Do not disapoint him.)
<li>-Expects """ (comment) on the line after a function definition</li>
<li>-Expects """ (comment) on the line after a class declaration</li>
<li>-Expects """ (comment) on the 2nd line of every python file (Right after the python shebang)</li>
<li>-Expects #!/usr/bin/python3 on the first line of every python file (Python shebang)</li>
