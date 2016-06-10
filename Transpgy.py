#!/usr/bin/python

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = original[0]
    print original
    new_word = word + first + pyg
    new_word = new_word[1:]
    print new_word
    
else:
    print 'empty'