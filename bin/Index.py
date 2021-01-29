#by Nichvaragliotti

import os, sys
import random
import argparse
import random
import math

_ask = input ("would you like a Password genorated?:    ")



_words = #words txt file
_Numbers = list 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
_symbols = list !, $, &, *, ., 
_type = "", "", "", ""


def words_from_file():
  f = open('words.txt', 'r')
  lines = f.readlines()
  f.close()

  # remove \n
  words = [line[:-1] for line in lines]
  return words




def Randomly_Word(words):
  r = random.SystemRandom()
  return r.choice(words)



def random_word(words, n):
 chosen = []
 for i in range(n): 
  new_word = Randomly_Word(words)
  chosen.append(new_word)
  return chosen



