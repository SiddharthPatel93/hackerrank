import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    k = k%26
    print(k)
    rstring=''
    for char in s:
        if (122 >= ord(char)>=97 or 65<=ord(char)<=90):
            val = ord(char) + k
            if (97<=val<=122 or 65<=val<=90) :
                rstring+=chr(val)
            else:
                val= val-26
                rstring+=chr(val)
        else:
            rstring+=char
    print(rstring)
    return rstring
    # Write your code here

caesarCipher(s='6DWV95HzxTCHP85dvv3NY2crzt1aO8j6g2zSDvFUiJj6XWDlZvNNr', k=87)