<h1>Frank</h1>
<h3>A documentation checker to help Holberton students along with PEP8</h3>
-   -   -
<h4>Usage:</h4> 

	frank <filename.py>
	Ex. frank main.py

<h4>Warnings:</h4> 
	
	<li>Frank does not work with wildcards because i havent figured that out yet in python.</li>
	<li>He still has a few false flags, trust but verify his output.</li>
	<li>Frank is not a replacement for PEP8, but rather something to be used along side of PEP8
	because PEP8 Does not check for documentation that is mandatory for Holberton students. </li>

<h4>Example usages/output cases:</h4> 

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

<h4>All of Franks expectations (Do not disapoint him.)</h4> 
<li>Expects """ (comment) on the line after a function definition</li>
<li>Expects """ (comment) on the line after a class declaration</li>
<li>Expects """ (comment) on the 2nd line of every python file (Right after the python shebang)</li>
<li>Expects #!/usr/bin/python3 on the first line of every python file (Python shebang)</li>
