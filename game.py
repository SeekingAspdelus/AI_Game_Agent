'''
Author: Yutong Ren
Date: 2022-11-01 13:17:09
LastEditTime: 2022-11-01 23:00:58
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Manila\AI_Game_Agent-main\game.py
'''
import random

from ast import Try
import play

import investment

class Game():
    '''
    instantiate the players, ships, ports, and shipyards, and outputfile
    '''

    def __init__(self):

        player1 = play.Player("Player1", 30, None, self)
        player2 = play.Player("Player2", 30, None, self)
        player3 = play.Player("Player3", 30, None, self) 

        ship1 = investment.ship("Ship1", [2,3,4], 30)
        ship2 = investment.ship("Ship2", [3,3,3], 24)
        ship3 = investment.ship("Ship3", [5,3,2], 36)
    
        port1 = investment.port("Port1", 4, 6)
        port2 = investment.port("Port2", 5, 7)
        port3 = investment.port("Port3", 3, 4)

        shipyard1 = investment.shipyard("Shipyard1", 3, 4)
        shipyard2 = investment.shipyard("Shipyard2", 6, 8)
        shipyard3 = investment.shipyard("Shipyard3", 5, 6)

        self.player_ls = []
        self.ship_ls = []
        self.port_ls = []
        self.shipyard_ls = []
        '''
        put players, ships, ports, and shipyards into lists
        '''
        self.player_ls = [player1, player2, player3]
        self.ship_ls = [ship1, ship2, ship3]
        self.port_ls = [port1, port2, port3]
        self.shipyard_ls = [shipyard1, shipyard2, shipyard3]
        self.action_ls = [port1, port2, port3, shipyard1, shipyard2, shipyard3, ship1, ship2, ship3]

        outfile = 'outputfile.txt'

        

    def start(self):
        for i in range(3):
            print("This is round",(i+1))
            #加一个判定，如果选择的action不属于my_turn所给的，那就要继续输入
            #player1's turn to play
            action_taken = self.player_ls[0].my_turn()
            action_taken.available = False
            print("Player1 has current money:", test.player_ls[0].money)

            #player2's turn to play
            action_taken = self.player_ls[1].my_turn()
            action_taken.available = False
            print("Player2 has current money:", test.player_ls[1].money)

            #player3's turn to play
            action_taken = self.player_ls[2].my_turn()
            action_taken.available = False
            print("Player3 has current money:", test.player_ls[2].money)

            #roll ship1's dice and update the position
            dice_Ship1_str = str(input())
            if(dice_Ship1_str == "dice1"):
                dice_Ship1 = random.randint(1,6)
                self.ship_ls[0].position += dice_Ship1
            print(self.ship_ls[0].position)

            #roll ship2's dice and update the position
            dice_Ship2_str = str(input())
            if(dice_Ship2_str == "dice2"):
                dice_Ship2 = random.randint(1,6)
                self.ship_ls[1].position += dice_Ship2
            print(self.ship_ls[1].position)

            #roll ship3's dice and update the position
            dice_Ship3_str = str(input())
            if(dice_Ship3_str == "dice3"):
                dice_Ship3= random.randint(1,6)
                self.ship_ls[2].position += dice_Ship3
            print(self.ship_ls[2].position)

        if(self.ship_ls[0].position > 13):
            ave_ship1_payback = self.ship_ls[0].payback/len(self.ship_ls[0].investors)
            for j in range(len(self.ship_ls[0].investors)):
                self.ship_ls[0].investors[j].money += ave_ship1_payback
            

            
        
        

        


       
        
        


        
        
            
test = Game()
test.start()
        
        




    







