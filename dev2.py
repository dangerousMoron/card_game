#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 10 15:46:51 2020

@author: tfinney

with human player
"""

import numpy
import random
import matplotlib.pyplot as pyplot

d_cards = numpy.arange(1,11) #a shitty way to build a deck but cool for now

# h_cards = [1,-1,2,-2,-6,6]
h_cards = [1,2,3,4,5,6,-1,-2,-3,-4,-5,-6]
# h_cards = [1]

p1_cards = d_cards
p2_cards = d_cards


class h_player():
    def __init__(self,name):
        self.hand = random.choices(h_cards,k=4)
        self.stand = False
        self.cards_dealt =[]
        self.count = 0
        self.played_card_this_round = False

        self.pause = False
        self.cheat = False
    
    # def play_card(self,card)
    
    def check_self(self):
        print('your count is',self.count)
        if(self.count == 20):
            self.stand = True
            
        if(self.stand==True):
            print("you can\'t do anything because you stood!")
        
        
        else:
            self.pause = True
            self.played_card_this_round = False
            while self.pause ==True:
                x = input('enter command: ')
                
                if(x==''):
                    # print('continuing game...')
                    self.pause = False
                
                if(x=='stand'):
                    print('you have stood at',self.count)
                    self.stand = True
                    self.pause = False
                    
                if(x=='cheat'):
                    print('debug enabled...')
                    self.cheat = True
                
                if(x=='cards'):
                    print('your cards are:',self.hand)
                    
                    y = input('play card: ')
                    if(y==''):
                        self.pause = False
                        continue
                        
                    y = int(y)
                    if(self.played_card_this_round==True):
                        print('you can only play one card per turn')
                        continue

                    if isinstance(y,int) == True:
                        
                        #cheat code to test things
                        if self.cheat == True:
                            print('you have played',y)
                            print('creating:',self.count,'+',y,'=',self.count + y)
                            self.count += y
                            
                            print('your score is now: ',self.count)
                                # self.pause = False
                            self.played_card_this_round = True
                            
                            if(self.count == 20):
                                self.stand = True
                                print('you have stood at 20')
                                self.pause = False
                                break
                            
                            break
                        
                        for i in range(len(self.hand)):
                            if(int(y)==self.hand[i]):
                                print('you have played',self.hand[i])
                                print('creating:',self.count,'+',self.hand[i],'=',self.count+self.hand[i])
                                
                                self.count  += self.hand[i]
                                self.hand[i] = 0
                                print('your score is now: ',self.count)
                                # self.pause = False
                                self.played_card_this_round = True
                                
                                if(self.count == 20):
                                    self.stand = True
                                    print('you have stood at 20')
                                    self.pause = False
                                    break
                                
                                break
                            
                    
                    
                    
            print('continuing game...')
            
            
            
        
    
    
# # p1 = h_player('test')
# p1.check_self()    

class ai_player():
    
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








p2 = ai_player('p2',18,True)
# p1 = ai_player('p1',18,True)
p1 = h_player('p1')

print('p1 has hand:',p1.hand)
print('p2 has hand:',p2.hand)
while True:
    # p1.check_self(p2)
    # p2.check_self(p1)
    p_win, status = check_state(p1,p2)
    if(status==False):
        print(p1.count,p2.count)
        print("-=--=-=-=-=-=-=-=")
        # return p_win
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
        
        # p1.play_card(p2)
        # p1.check_self(p2)
        p1.check_self()
        
            
        #end player 1 turn        
        p_win, status = check_state(p1,p2)
        if(status==False):
            print(p1.count,p2.count)
            print("-=--=-=-=-=-=-=-=")
            # return p_win
            break
        
        #player 2 turn
        if(p2.stand==False):
            # p2_draw = random.choice(d_cards)
            p2_draw = random.choice(p2_cards)
            print('Player 2 draws:',p2_draw)
            p2.cards_dealt.append(p2_draw)
            p2.count += p2_draw
        p2.play_card(p1)
        p2.check_self(p1)   









