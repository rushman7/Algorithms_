#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if not cache:
    cache = [0 for i in range(n+1)]  # If cache has no value, default cache to an array of zeroes

  if n < 2:
    return 1

  if n == 2:
    return 2

  if cache[n] > 2: # If more than 2 ways, return the value of cache
    return cache[n] # cache[n] is number of ways we can get to n
  
  cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

  return cache[n]

eating_cookies(5)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')