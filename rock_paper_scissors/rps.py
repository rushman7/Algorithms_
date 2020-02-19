#!/usr/bin/python

import sys

options = ['rock', 'paper', 'scissors']

def rock_paper_scissors(n):
  pass

rock_paper_scissors(2)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')