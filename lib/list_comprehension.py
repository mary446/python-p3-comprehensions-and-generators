#!/usr/bin/env python3

def return_evens(num_list):
    num=[]
    for i in num_list:
        if i%2==0:
            num.append(i)
    return num
    pass

def make_exclamation(sentence_list):
    sent=[]
    if len(sentence_list)>0:
        for sentence in sentence_list:
            sent.append(sentence[:]+"!")
        
    
    return sent