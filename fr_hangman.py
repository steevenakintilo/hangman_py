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
from c import print_guy
import sys

system('clear')

def change_letter(list, pos, char):

        first_ele = list.pop(pos)
        second_ele = char
        list.insert(pos, char)
        return list
if len(sys.argv) == 1:
   print("Tu dois choisir un fichier en tant que 1er argument")
   sys.exit()
bigword = c.random_line(sys.argv[1])
word = bigword.strip()
i = 0
val = input("Tapes sur entre pour jouer")
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
    print_guy(bad)
    val = input("Tapes une lettre ou un mot mais si le mot est faux perdue: ")
    print("Nombre d'essaies restant %d" % (bad))
    if val == word:
        print("Bravo tu as gagne en tapant un mot chapeau")
        print("Le mot était %s" % (bigword))
        break
    if val != word and len(val) > 1:
        print("Tu as perdus en voulant tenter le mot entier")
        print("Le mot était %s" % (bigword))
        break
    if val == word[d.letter_index(val,word,1)] and d.letter_nbr(val,word) == 1:
        change_letter(ans, d.letter_index(val,word,1), val)
        print(ans)
        print("Lettre fausse", bad_letter)
        res = res + 1
    if val == word[d.letter_index(val,word,1)] and d.letter_nbr(val,word) == 2:
        change_letter(ans, d.letter_index(val,word,1), val)
        change_letter(ans, d.letter_index_n(val,word,2), val)
        print(ans)
        print("Lettre fausse", bad_letter)
        res = res + 2
    if val == word[d.letter_index(val,word,1)] and d.letter_nbr(val,word) == 3:
        change_letter(ans, d.letter_index(val,word,1), val)
        change_letter(ans, d.letter_index_n(val,word,2), val)
        change_letter(ans, d.letter_index_n(val,word,3), val)
        print(ans)
        print("Lettre fausse", bad_letter)
        res = res + 3
    if val == word[d.letter_index(val,word,1)] and d.letter_nbr(val,word) == 4:
       change_letter(ans, d.letter_index(val,word,1), val)
       change_letter(ans, d.letter_index_n(val,word,2), val)
       change_letter(ans, d.letter_index_n(val,word,3), val)
       change_letter(ans, d.letter_index_n(val,word,4), val)
       print(ans)
       print("Lettre fausse", bad_letter)
       res = res + 4
    if val == word[d.letter_index(val,word,1)] and d.letter_nbr(val,word) == 5:
       change_letter(ans, d.letter_index(val,word,1), val)
       change_letter(ans, d.letter_index_n(val,word,2), val)
       change_letter(ans, d.letter_index_n(val,word,3), val)
       change_letter(ans, d.letter_index_n(val,word,4), val)
       change_letter(ans, d.letter_index_n(val,word,5), val)
       print(ans)
       print("Lettre fausse", bad_letter)
       res = res + 5
    if d.letter_index(val,word,1) == -1:
        print(ans)
        bad_letter.append(val)
        print("Lettre fausse", bad_letter)
        bad = bad - 1
    if bad < 0:
        print_guy(-10)
        print("Tu as perdus")
        print("Le mot était %s" % (bigword))
        break
    if res == len(word):
        print("Bravo tu as gagne")
        print("Le mot était %s" % (bigword))
        break
    i = i + 1
