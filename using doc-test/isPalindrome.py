import math
import os
import random
import re
import sys
import inspect


def isPalindrome(x):
    """
    >>> isPalindrome(121)
    True
    >>> isPalindrome(344)
    False
    >>> isPalindrome(-121)
    Traceback (most recent call last):
    ValueError: x must be positive integer.
    >>> isPalindrome("hello")
    Traceback (most recent call last):
    TypeError: x must be integer.
    """  
    try:
        x = int(x)
        temp=x
        rev=0
        if(x>0):
            while(x>0):
                dig=x%10
                rev=rev*10+dig
                x=x//10
            if(temp==rev):
                return True
            else:
                return False
        elif(x<0):
            raise TypeError
        else:
            raise ValueError
    except ValueError:
        raise ValueError("x must be positive integer")
    except TypeError:
        raise TypeError("x must be an integer")
