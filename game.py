'''
Author: Yutong Ren
Date: 2022-11-01 13:17:09
LastEditTime: 2022-11-01 22:05:16
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: \Manila\AI_Game_Agent-main\game.py
'''

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

        ship1 = investment.ship("Ship1", [2,3,4], 3)
        ship2 = investment.ship("Ship2", [3,3,3], 4)
        ship3 = investment.ship("Ship3", [5,3,2], 5)
    
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
        print("Your current money is:",self.player_ls[0].money)
        for j in range(len(self.player_ls[0].get_action())):
            print(self.player_ls[0].get_action()[j].name)
        action_player1 = str(input())
        
            
test = Game()
test.player_ls[0].my_turn()
print(test.player_ls[0].money)
        
        




    







