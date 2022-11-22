'''
Author: Tianle Zhu
Date: 2022-11-20 17:04:47
LastEditTime: 2022-11-22 21:12:46
LastEditors: Please set LastEditors
FilePath: \AI_Game_Agent\agents.py
'''
from play import *
import util

"""
State:
A list of integer
Investment and corresponding idx
    Port1 : 0
    Port2 : 1
    Port3 : 2
    Shipyard1 : 3
    Shipyard2 : 4
    Shipyard3 : 5
    Ship1 : 6
    Ship2 : 7
    Ship3 : 8

Values:
    Ships : num of seats left
    Other investments : 0 == unavailable; 1 == available
    
Action:
Action idx : 9
Values:
    Port1 : 0
    Port2 : 1
    Port3 : 2
    Shipyard1 : 3
    Shipyard2 : 4
    Shipyard3 : 5
    Ship1 : 6
    Ship2 : 7
    Ship3 : 8
    Skip : 9
    
Eg. [2,2,1,0,1,0,0,1,1,3]
"""
class QlearningAgent(Player):
    def __init__(self, name, money, color, game):
        super().__init__(name, money, color, game)
        self.qtable = util.Qtable()
        self.factor = 0
    
    def set_factor(self, factor):
        self.factor = factor
    
    def get_action(self):
        action_ls = []
        money = self.get_money()
        for action in self.game.action_ls:
            if action.get_availability() and action.get_cost() > money:
                action_ls.append(action)
        return action_ls
    
    def my_turn(self):
        action_ls = self.get_action()
        
        pass
    
    def get_state(self):
        state = []
        for ship in self.game.ship_ls
    
    def computeAction(self,action_ls):
        state = self.game.get
    def update(self):
        pass
    
    def computeReward(self,action):
        if(action.name == )
        pass
