#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## d
## File description:
## d
##

import c
import d
from os import system, name
import sys

system('clear')
def change_letter(list, pos, char):

        first_ele = list.pop(pos)
        second_ele = char
        list.insert(pos, char)
        return list
if len(sys.argv) == 1:
   print("You must choose a file as first argument")
   sys.exit()
bigword = c.random_line(sys.argv[1])
word = bigword.strip()
i = 0
val = input("Press enter to play")
j = 0
c = 0
y = 0
check = 0
ans = []
bad_letter = []
if (sys.argv[1] != "fr_words" and sys.argv[1] != "en_words"):
        c = -1
while c < len(bigword) - 1:
        ans.append("-")
        c = c + 1
print(ans)
res = 0
bad = 5
while res < len(word):
    val = input("Type a letter or a word but if the word is wrong you lost: ")
    print("Number of trials remaining %d" % (bad))
    if val == word:
        print("Well done you won by typing a word good.")
        print("The word was %s" % (bigword))
        break
    if val != word and len(val) > 1:
        print("You lost trying to try the whole word")
        print("The word was %s" % (bigword))
        break
    if val == word[d.letter_index(val,word,1)] and d.letter_nbr(val,word) == 1:
        change_letter(ans, d.letter_index(val,word,1), val)
        print(ans)
        print("Wrong letter", bad_letter)
        res = res + 1
    if val == word[d.letter_index(val,word,1)] and d.letter_nbr(val,word) == 2:
        change_letter(ans, d.letter_index(val,word,1), val)
        change_letter(ans, d.letter_index_n(val,word,2), val)
        print(ans)
        print("Wrong letter", bad_letter)
        res = res + 2
    if val == word[d.letter_index(val,word,1)] and d.letter_nbr(val,word) == 3:
        change_letter(ans, d.letter_index(val,word,1), val)
        change_letter(ans, d.letter_index_n(val,word,2), val)
        change_letter(ans, d.letter_index_n(val,word,3), val)
        print(ans)
        print("Wrong letter", bad_letter)
        res = res + 3
    if val == word[d.letter_index(val,word,1)] and d.letter_nbr(val,word) == 4:
       change_letter(ans, d.letter_index(val,word,1), val)
       change_letter(ans, d.letter_index_n(val,word,2), val)
       change_letter(ans, d.letter_index_n(val,word,3), val)
       change_letter(ans, d.letter_index_n(val,word,4), val)
       print(ans)
       print("Wrong letter", bad_letter)
       res = res + 4
    if val == word[d.letter_index(val,word,1)] and d.letter_nbr(val,word) == 5:
       change_letter(ans, d.letter_index(val,word,1), val)
       change_letter(ans, d.letter_index_n(val,word,2), val)
       change_letter(ans, d.letter_index_n(val,word,3), val)
       change_letter(ans, d.letter_index_n(val,word,4), val)
       change_letter(ans, d.letter_index_n(val,word,5), val)
       print(ans)
       print("Wrong letter", bad_letter)
       res = res + 5
    if d.letter_index(val,word,1) == -1:
        print(ans)
        bad_letter.append(val)
        print("Wrong letter", bad_letter)
        bad = bad - 1
    if bad < 0:
        print("You lost")
        print("The word was %s" % (bigword))
        break
    if res == len(word):
        print("Well done you won")
        print("The word was %s" % (bigword))
        break
    i = i + 1
