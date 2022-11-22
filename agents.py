'''
Author: Tianle Zhu
Date: 2022-11-20 17:04:47
LastEditTime: 2022-11-20 17:32:31
LastEditors: Tianle Zhu
FilePath: \AI_Game_Agent\agents.py
'''
from play import *
import util

"""
State:
A list of integer
Investment and corresponding idx
    Ship1 : 0
    Ship2 : 1
    Ship3 : 2
    Port1 : 3
    Port2 : 4
    Port3 : 5
    Shipyard1 : 6
    Shipyard2 : 7
    Shipyard3 : 8

Values:
    Ships : num of seats left
    Other investments : 0 == unavailable; 1 == available
    
Action:
Action idx : 9
Values:
    Ship1 : 0
    Ship2 : 1
    Ship3 : 2
    Port1 : 3
    Port2 : 4
    Port3 : 5
    Shipyard1 : 6
    Shipyard2 : 7
    Shipyard3 : 8
    Skip : 9
    
Eg. [2,2,1,0,1,0,0,1,1,3]
"""
class QlearningAgent(Player):
    def __init__(self, name, money, color, game):
        super().__init__(name, money, color, game)
        self.qtable = util.Qtable()
    
    def get_action(self):
        
    
    def my_turn(self):
        