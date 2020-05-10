#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  7 16:01:09 2020

@author: tfinney
"""

import random
import numpy
import matplotlib.pyplot as pyplot

d_cards = numpy.arange(1,11) #a shitty way to build a deck but cool for now

# h_cards = [1,-1,2,-2,-6,6]
h_cards = [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]
# h_cards = [1]

p1_cards = d_cards
p2_cards = d_cards

# p1_cards = [18]
# p2_cards = [15]
# p1_cards = [18]
# p2_cards = [18]


class player():
    
    def __init__(self,name,stop_at,use_hand=False):
        self.name = str(name)
        self.stop_val = stop_at
        self.stand = False
        self.count = 0
        self.cards_dealt = []
        self.tie = False
        if(use_hand==True):
            self.use_hand = True
            self.hand = random.choices(h_cards,k=4)
        else:
            self.use_hand = False
            self.hand = []
        
        self.opponent_stand = False
        
    def check_self(self,opponent):
        if(self.stand == True):
            print(self.name,'is already standing so no checks!')
        
        else:
            if(opponent.count == 20):
                
                if(self.count == 20):
                    print(self.name,"we both have 20, so stand!")
                    self.stand = True
                    
                else:
                    print(self.name,'won\'t stand because opponent has 20' )
                    self.stand = False
                
            
            elif(self.count==20):
                print(self.name,'stands because they have 20')
                self.stand = True
            elif(self.count >= self.stop_val and self.count < 20):
                print(self.name,'stands at stop var!')
                self.stand = True
                
            if opponent.stand == True:
                if(self.count > opponent.count):
                    print(self.name,'stands because opponent stood')
                    self.stand = True
                # if(self.count < opp)
            
        
    def play_card(self,opponent):
        # if(self.stand==True):
            # print('no card play while standing')
        
        if(self.count == 20 and self.use_hand == True):
            print(self.name,'already has 20 so no cards to play')
            self.stand = True
            # self.use_hand = False
        
        if(self.use_hand == True and self.stand == False):
            for i in range(len(self.hand)):
                if(self.stand == True):
                    break
                
                maybe_card = self.hand[i] + self.count 
                # print(maybe_card)
                
                if(maybe_card >= self.stop_val and maybe_card <=20):
                    if(self.hand[i]==0):
                        continue
                    else:
                        if(maybe_card == 20):
                            print(self.name,'plays',self.hand[i],'to', self.count,' to make',self.hand[i] + self.count)
                            self.count += self.hand[i]
                            self.hand[i] = 0
                            self.check_self(opponent)
                            break
                        
                        else:     
                            if (maybe_card >= self.stop_val and maybe_card < 20):
                                # print('opt 2')
                                print(self.name,'plays',self.hand[i],'to make',self.hand[i] + self.count,'opt2')
                                self.count += self.hand[i]
                                self.hand[i] = 0
                                self.check_self(opponent)
                                break
                            
                        
                    
                
                # if(maybe_card == 20):
                #     if(self.hand[i]==0):
                #         continue 
                    
                #     # print(self.name,'playing this card could make me win!')
                #     print(self.name,'plays',self.hand[i],'to make',self.hand[i] + self.count)
                #     self.count += self.hand[i]
                #     self.hand[i] = 0
                #     continue
                    
                # if(maybe_card >= self.stop_val and maybe_card <= 20):
                #     if(self.hand[i]==0):
                #         continue
                #     print(self.name,'plays',self.hand[i],'to make',self.hand[i] + self.count)
                #     self.count += self.hand[i]
                #     self.hand[i] = 0
                #     continue
                    



def check_state(p_1,p_2):
    
    # tie scenario
    
    if(p_1.count == 20 and p_2.count ==20):
        print('its a tie')
        return 0, False
    
    if(p_1.stand == True and p_2.stand == True):
        if(p_1.count == p_2.count):
            print('its a tie because they both stood')
            return 0,False
    #p1 wins
    
    if (p_1.count <= 20 and p_2.count > 20):
        print("player 1 wins!")
        return 1,False
    
    #p2 wins
    if (p_2.count <= 20 and p_1.count > 20):
        print("player 2 wins!")
        return 2,False
    
    #stand scenarios
    if(p_1.stand==True and p_2.stand==True):
        if(p_1.count > p_2.count):
            print('player 1 wins!')
            return 1,False
        
        if(p_2.count > p_1.count):
            print('player 2 wins!')
            return 2,False
    
    #not really winning scenarios
    if (p_1.count == 20 and p_2.count < 20 ):
        return -1, True
    
    if(p_2.count == 20 and p_1.count <20 ):
        return -1, True
    
    else:
        return -1, True
    

# p1 = player('p1',19,use_hand = True)
# p2 = player('p2',19,use_hand = True)

# p3 = player('p3',20)
# p4 = player('p4',20)

# p4.count = 20
# p3.check_self(p4)


#play the game
def play_round(p1,p2):
    # p1 = player('p1',18,use_hand = True)
    # p2 = player('p2',18,use_hand = True)
    print('p1 has hand:',p1.hand)
    print('p1 has hand:',p2.hand)
    while True:
        # p1.check_self(p2)
        # p2.check_self(p1)
        p_win, status = check_state(p1,p2)
        if(status==False):
            print(p1.count,p2.count)
            print("-=--=-=-=-=-=-=-=")
            return p_win
            break
        
        else:
            #player 1 turn
            # p1.check_self(p2)
            if(p1.stand==False):
                # p1_draw = random.choice(d_cards)
                p1_draw = random.choice(p1_cards)
                p1.cards_dealt.append(p1_draw)
                p1.count += p1_draw
            
            print(p1.count,p2.count,'after p1 turn')
            print('---------------------------')
            
            p1.play_card(p2)
            p1.check_self(p2)
    
                
            #end player 1 turn        
            p_win, status = check_state(p1,p2)
            if(status==False):
                print(p1.count,p2.count)
                print("-=--=-=-=-=-=-=-=")
                return p_win
                break
            
            #player 2 turn
            if(p2.stand==False):
                # p2_draw = random.choice(d_cards)
                p2_draw = random.choice(p2_cards)
                p2.cards_dealt.append(p2_draw)
                p2.count += p2_draw
            p2.play_card(p1)
            p2.check_self(p1)        
            


    
    print(p1.count,p2.count,'after p2 turn')
    print('---------------------------')
    

def play_game():
    """
    3 rounds per game
    """
    p1 = player('p1',18,True)
    p2 = player('p2',18,True)
    
    p1_wins = 0
    p2_wins = 0
    ties = 0
    tally =[]
    # for i in range(3):
    while True:
        winner = play_round(p1,p2)
        tally.append(winner)
        # if(winner==0):
            # continue
        if(winner == 1):
            p1_wins += 1
        if(winner ==2):
            p2_wins += 1
        
        if(winner == 0):
            ties += 0
        p1.count = 0
        p1.stand = False
        
        p2.count = 0
        p2.stand = False        
            
        if(p1_wins == 3):
            print('p1 wins this game!')
            return 1,tally
            break
    
        if(p2_wins == 3):
            print('p2 wins this game!')
            return 2,tally
            break
            

play_game()


# n = 10000
# ties = 0
# one_wins = 0
# two_wins = 0

# for i in range(n):
#     x = play_game()
#     # print(x)
#     if(x == 0):
#         ties +=1
#     if (x==1):
#         one_wins+=1
#     if (x==2):
#         two_wins+=1


# pyplot.bar(['tie','p1','p2'],[ties,one_wins,two_wins])

# print(play_game())
# 


    
    