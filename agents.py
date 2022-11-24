'''
Author: Tianle Zhu
Date: 2022-11-20 17:04:47
LastEditTime: 2022-11-24 17:14:02
LastEditors: Tianle Zhu
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
        self.alpha = 0.7
        self.gamma = 0.5
        self.action_val_dic = {"Port1" : 0, "Port2" : 1, "Port3" : 2,
                               "Shipyard1" : 3, "Shipyard2" : 4, "Shipyard3" : 5,
                               "Ship1" : 6, "Ship2" : 7, "Ship" : 8,
                               "Skip" : 9}
    
    def set_factor(self, factor):
        self.factor = factor
    
    def get_qvalue(self,s_a_pair):
        return self.qtable[s_a_pair]
    
    def get_action(self):
        action_ls = []
        money = self.get_money()
        for action in self.game.action_ls:
            if action.get_availability() and action.get_cost() > money:
                action_ls.append(action)
        return action_ls
    
    def my_turn(self):
        action, _ = self.computeMax()
        action.invest(self)
        self.update()
        
        
    def get_state(self):
        state = []
        investment_ls = self.game.action_ls[:-1]
        for investment in investment_ls:
            investor_num = len(investment.get_investors())
            slot_left = investment.get_length() - investor_num
            state.append(slot_left)
        
        return state

    def computeMax(self):
        state = self.get_state()
        action_ls = self.get_action()
        qMax = float('-inf')
        actionMax = None
        for action in action_ls:
            action_val = self.action_val_dic[action.name]
            s_a_pair = state + [action_val]
            qvalue = self.get_qvalue(s_a_pair)
            if qvalue > qMax:
                qMax = qvalue
                actionMax = action
                
        return actionMax, qMax
    
    def update(self):
        pass
    
    def computeReward(self,action):
        ship_pos_ls = [self.game.ship_ls[0].get_position(), self.game.ship_ls[1].get_position(), self.game.ship_ls[2].get_position()]
        ship_pos_ls_sort = sorted(ship_pos_ls)
        ship_pos_max = ship_pos_ls_sort[2]
        ship_pos_mid = ship_pos_ls_sort[1]
        ship_pos_min = ship_pos_ls_sort[0]

        if(action.get_type() == "ship"):
            payback = action.get_payback()/len(action.get_investors())-action.get_cost()
            reward = payback + self.factor*payback*(3.5*(3-self.game.current_round)+action.get_position()-13)

        elif((action.get_type() == "port")):
            payback = action.get_payback() - action.get_cost()
            if(action.name == "Port1"):
                reward = payback + self.factor*payback*(3.5*(3-self.game.current_round)+ship_pos_max-13)
            elif(action.name == "Port2"):
                reward = payback + self.factor*payback*(3.5*(3-self.game.current_round)+ship_pos_mid-13)
            else:
                reward = payback + self.factor*payback*(3.5*(3-self.game.current_round)+ship_pos_min-13)
                

        elif(action.get_type() == "shipyard"):
            payback = action.get_payback() - action.get_cost()
            if(action.name == "Shipyard1"):
                reward = payback - self.factor*payback*(3.5*(3-self.game.current_round)+ship_pos_min-13)
            elif(action.name == "Shipyard2"):
                reward = payback - self.factor*payback*(3.5*(3-self.game.current_round)+ship_pos_mid-13)
            else:
                reward = payback - self.factor*payback*(3.5*(3-self.game.current_round)+ship_pos_max-13)
        else:
            reward = 0
        
        return reward
