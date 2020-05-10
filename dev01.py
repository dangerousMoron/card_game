#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 11:06:06 2020

@author: tfinney
"""

import numpy
import random
import matplotlib.pyplot as pyplot

d_cards = numpy.arange(1,11)






def check_state(p_count_1,p_count_2):
    #tie scenarios
    if(p_count_1 == 20 and p_count_2 == 20):
        print('its a tie!')
        return 0, False
    
    #player 1 winning scenarios 
    # if(p_count_1 == 20 and p_count_2 > 20):
    #     print("player 1 wins!")
    #     return 1, False
    
    # if(p_count_1 < 20 and p_count_2 > 20):
    #     print("player 1 wins!")
    #     return 1, False
    
    if( p_count_1 <= 20 and p_count_2 > 20):
        print("player 1 wins!")
        return 1,False
    
        
    
    #player 2 winning scenarios
    # if(p_count_1 > 20 and p_count_2 < 20):
    #     print("player 2 wins!")
    #     return 2,False

    # if(p_count_1 > 20 and p_count_2 == 20):
    #     print("player 2 wins!")
    #     return 2,False
        
    if( p_count_2 <= 20 and p_count_1 > 20):
        print("player 2 wins!")
        return 2,False
    
    
    #not really winning scenarios yet...  
    if(p_count_1 == 20 and p_count_2 < 20):
        return -1, True
    
    if(p_count_1 < 20 and p_count_2 == 20):
        return -1, True


    else:
        return -1,True

def play_game():
    p_count_1 = 0
    p_count_2 = 0
    while True:
        p_win,status = check_state(p_count_1,p_count_2)
        if(status==False):
            print(p_count_1,p_count_2)
            print('--==--==--==')
            break
        
        else:
            p_1_draw = random.choice(d_cards)
            p_count_1 += p_1_draw
            
            p_win,status = check_state(p_count_1,p_count_2)
            if(status==False):
                print(p_count_1,p_count_2)
                print('--==--==--==')
                break
            
            p_2_draw = random.choice(d_cards)
            p_count_2 += p_2_draw
            
            # print("player 1 draws:",p_1_draw)
            # print("player 1 total:",p_count_1)
            # print("-=-=-=-=")
            # print("player 2 draws:",p_2_draw)
            # print("player_2_total:",p_count_2)
            print(p_count_1,p_count_2)
            
            print('-------------------')
        
    
    return p_win
    

play_game()

p1_wins = 0
p2_wins = 0

n = 10000
for i in range(n):
    winner = play_game()
    if(winner==2):
        p1_wins += 1
    if(winner==1):
        p2_wins += 1
    
# # x = play_game()
# print(x)

pyplot.bar(['p1','p2'],[p1_wins,p2_wins])

# print(p1_wins/p2_wins)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    