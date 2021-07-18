#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## d
## File description:
## d
##

def letter_index(chars, string, val):
        i = 0
        for i in range(0, len(string)):
            if string[i] == chars and val == 1:
                return (i)
        return (-1)

def letter_index_n(chars, string, val):
        i = 0
        l = []
        j = 0
        for i in range(0, len(string)):
                if string[i] == chars:
                   l.append(i)
        if val == 2:
           return (l[1])
        if val == 3:
           return (l[2])
        if val == 4:
           return (l[3])
        if val == 5:
           return (l[4])

def letter_nbr(chars, string):
        i = 0
        count = 0
        for i in range(0, len(string)):
            if string[i] == chars:
                count = count + 1
        return (count)

#print(letter_index_n("q","cqqqqqqo",5))
#print(letter_nbr("q","cqqqqqqqqo"))
