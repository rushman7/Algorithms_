#!/usr/bin/python

import sys

def eating_cookies(n, cache=None):
  result = 0
  if n < 2:
    return result + 1
  
  if n == 2:
    return result + 2

  result = eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

  return result

eating_cookies(5)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')