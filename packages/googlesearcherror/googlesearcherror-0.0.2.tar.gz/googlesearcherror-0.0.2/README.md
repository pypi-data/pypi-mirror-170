This project is for people who new to python and cannot understand what's wrong with their code, 

if your code raise an Exception, the code will automatically search for a fix on google and print a link on the terminal

## Installation

```pip install googlesearcherror```

## Usage

put this code at the top of your code

```python
from googlesearcherror import googlesearcherror
googlesearcherror.searcherror()
```

Example:


Input:
```python
from googlesearcherror import googlesearcherror
googlesearcherror.searcherror()

print(0/0)
```

Output:
```
 File "test.py", line 4, in <module>
    print(0/0)
ZeroDivisionError: division by zero

-->  https://www.google.com/search?q=python+ZeroDivisionError++division+by+zero+site:stackoverflow.com
```
