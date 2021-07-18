#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## d
## File description:
## d
##
from random import randint

def letter_index(chars, string):
    i = 0
    while i < len(string):
        if string[i] == chars:
            return(i)
        i = i + 1
    pass

def random_str(char):
    return (randint(0, len(char) - 1))
    pass

def random_line(files):
    lines = []
    rand_line = []
    with open(files) as f:
        lines = f.readlines()
        return(lines[random_str(lines)])
    pass
