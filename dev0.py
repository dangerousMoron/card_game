#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:06:05 2020

@author: tfinney

simple implementation
"""

import numpy
import random

d_cards = numpy.arange(1,11)

p_count_1 = 0
p_count_2 = 0

print("p1,p2")
while True:
    if(p_count_1 == 20 and p_count_2 == 20):
        print("its a tie!")
        break
        
    if(p_count_1 > 20):
        # print("player 1 loses!")
        print("player 2 wins!")
        break
    
    if(p_count_2 > 20):
        # print("player 2 loses!")
        print("player 1 wins!")
        break
    
    if(p_count_1 == 20):
        print("player 1 wins!")
        break
    
    if(p_count_2 == 20):
        print("player 2 wins!")
        break
    

    
    else:
        p_1_draw = random.choice(d_cards)
        p_count_1 += p_1_draw
        
        p_2_draw = random.choice(d_cards)
        p_count_2 += p_2_draw
        
        # print("player 1 draws:",p_1_draw)
        # print("player 1 total:",p_count_1)
        # print("-=-=-=-=")
        # print("player 2 draws:",p_2_draw)
        # print("player_2_total:",p_count_2)
        print(p_count_1,p_count_2)
        
        print('-------------------')
    
    
    
