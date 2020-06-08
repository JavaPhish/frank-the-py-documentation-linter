<h1>Frank</h1>
<h3>A documentation checker to help Holberton students along with PEP8</h3>
-   -   -
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
-Expects """ (comment) on the line after a function definition
-Expects """ (comment) on the line after a class declaration
-Expects """ (comment) on the 2nd line of every python file (Right after the python shebang)
-Expects #!/usr/bin/python3 on the first line of every python file (Python shebang)
