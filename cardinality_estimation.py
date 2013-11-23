#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from bz2 import BZ2File
import json
import time
import mmh3
import re
import string

print_interval = 100
table = string.maketrans("","")

active = 1
hashset = set([])

def memory_usage():
  status = open('/proc/self/status').readlines()
  result = status[15].split(':')[1].split()[0].strip()
  return result

def update(algo, word, m=0):
  global hashset, active

  if isinstance(word, str):
    lowerword = remove_punctuation(word.lower())
  elif isinstance(word, unicode):
    lowerword = remove_punctuation(word.encode('utf8').lower())

  if (algo == 'exact'):
    hashset.add(lowerword)
  elif (algo == 'adaptive'):
    hashedword = mmh3.hash(lowerword)
    if ((hashedword & (active - 1)) == 0):
      hashset.add(hashedword)
    while (len(hashset) > m):
      active <<= 1
      hashset = set([e for e in hashset
                     if (e & (active - 1)) == 0])
  else:
    print 'error'
    sys.exit(1)

def estimate(algo):
  global hashset, active

  if (algo == 'exact'):
    return len(hashset)
  elif (algo == 'adaptive'):
    if (active >= 32):
      sys.exit(0)
    else:
      return len(hashset) * active
  else:
    print 'error'
    sys.exit(1)

def print_status(i, algo, elapsed):
  estimate_to_print = estimate(algo)
  if ((i+1) % print_interval == 0):
    print str(i+1) + '\t',
    print str(estimate_to_print) + '\t',
    print str(elapsed) + '\t',
    print memory_usage()

def remove_punctuation(s):
  return re.sub(r"[,!\?\.\|;\(\)\-':]", "", s)

def count_tweets(dir, algo, m=0):
  i = 0
  start = time.clock()

  print "NUMTWEETS\tCARDINALITY\tTIME\tMEM"
  
  for path, dirs, files in os.walk(dir):
    for file in files:
      if "bz2" in file:
        with BZ2File(path + "/" + file, 'r') as t:
          for tweetJson in t:
            tweet = json.loads(tweetJson)
            if 'text' in tweet:
              for word in tweet['text'].strip().split():
                update(algo, word, m)
              print_status(i, algo, time.clock() - start)
            i += 1

  print_status(i, algo, time.clock() - start)

def count_file(file, algo, m=0):
  i = 0
  start = time.clock()
  with open(file, 'r') as f:
    for line in f:
      words = line.strip().split()
      if (len(words)):
        for word in words:
          update(algo, word, m)
        print_status(i, algo, time.clock() - start)
      i += 1

def printset(hashset):
  print '[ ',
  for e in hashset:
    print "{0:b}".format(e) + ' ',
  print ']'

if __name__ == "__main__":
  dir = sys.argv[1]
  recursebzip2 = sys.argv[2]
  algo = sys.argv[3]
  
  m = 0
  if (len(sys.argv) == 5):
    m = int(sys.argv[4])

  if (int(recursebzip2) == 1):
    count_tweets(dir, algo, m)
  else:
    count_file(dir, algo, m)
