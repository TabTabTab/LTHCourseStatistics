# Guidelines for developers


## Python

### PEP8
Follow PEP8 as well as possible

### Line length
If not too inconvenient, try to stay at a 80 char length per line

### Overall guidelines for python coding
* When arguments are separated with commas, add a space after each comma, as such:
    'k = Object(a, b, c)'
    not
    'k = Object(a,b,c)'

* Predefined arguments should be set without spaces between the equals symbol
    and the value
    'o = Obj(name='hello')'
    not
    'o = Obj(name = 'hello')'

### Imports
* Do not use wildcard (*) imports if unnecessary

### File header
1. optional sha-bang (#!)
2. empty line
3. imports from the project
4. empty line
5. external library imports
6. empty line
7. code goes here

#### Example

1 #!/usr/bin/python3
2
3 import errors
4 import pdf_parser
5
6 import os
7
8 class TestClass(object):
9 ...
