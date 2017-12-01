Create a file called util.py, in that file create a class called Util.  In that class
create a @classmethod called delete_squares().  The method should accept a list of integers.
For every element in the list, test to see if the number is a square (if the square root is a whole number).
If the element is a square, delete it from the list.  delete_squares does not return anything.  For example:



>>> from util import Util
>>> alist = [3,7,4,9,3]
>>> Util.delete_squares(alist)
>>> alist
[3, 7, 3]
