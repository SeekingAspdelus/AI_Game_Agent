'''
Author: Tianle Zhu
Date: 2022-11-20 17:04:47
LastEditTime: 2022-11-24 21:34:54
LastEditors: Tianle Zhu
FilePath: \AI_Game_Agent\agents.py
'''
import numpy as np
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
        self.tValue = 0
        self.seed = None
        self.action_val_dic = {"Port1" : 0, "Port2" : 1, "Port3" : 2,
                               "Shipyard1" : 3, "Shipyard2" : 4, "Shipyard3" : 5,
                               "Ship1" : 6, "Ship2" : 7, "Ship3" : 8,
                               "Skip" : 9}
        
    def saveQtable(self,filepath):
        self.qtable.save(filepath)
        
    def loadQtable(self,filepath):
        self.qtable.load(filepath)
    
    def set_seed(self, Myseed):
        self.seed = Myseed
    
    def set_factor(self, factor):
        self.factor = factor
    
    def get_qvalue(self,s_a_pair):
        return self.qtable[tuple(s_a_pair)]
    
    def update_Qtable(self, newQ, state, action):
        s_a_pair = tuple(state + [self.convertAction(action)])
        self.qtable[s_a_pair] = newQ
    
    def convertAction(self, action):
        return self.action_val_dic[action.name]
    
    def get_action(self):
        action_ls = []
        money = self.get_money()
        for action in self.game.action_ls:
            if action.get_availability() and action.get_cost() < money:
                action_ls.append(action)
        return action_ls
    
    def my_turn(self):
        # compute action with maximum Qvalue
        action, currentQ, currentState = self.computeMax()
        # compute Reward
        R = self.computeReward(action)
        # take the action
        action.invest(self)
        # observe nextState and compute maximum Qvalue of nextState
        _,nextQ,_ = self.computeMax()
        # update Qtable
        newQ = (1 - self.alpha) * currentQ + self.alpha * (R + self.gamma * nextQ)
        self.update_Qtable(newQ,currentState,action)
        
    def get_state(self):
        state = []
        investment_ls = self.game.action_ls[:-1]
        for investment in investment_ls:
            investor_num = len(investment.get_investors())
            slot_left = investment.get_length() - investor_num
            state.append(slot_left)
        
        return state

    def computeMax(self):
        # compute the maximum Qvalue based current state and available actions
        state = self.get_state()
        action_ls = self.get_action()
        qMax = float('-inf')
        candidate = []
        actionMax = None
        for action in action_ls:
            action_val = self.convertAction(action)
            s_a_pair = state + [action_val]
            qvalue = self.get_qvalue(s_a_pair)
            if qvalue == qMax:
                candidate.append(action)
            if qvalue > qMax:
                qMax = qvalue
                actionMax = action
                candidate = [action]
        # break tie randomly
        if len(candidate) != 0:
            actionMax = util.randomChoice(candidate,self.seed)
        return actionMax, qMax, state
    
    def computeReward(self,action):
        ship_pos_ls = [self.game.ship_ls[0].get_position(), self.game.ship_ls[1].get_position(), self.game.ship_ls[2].get_position()]
        ship_pos_ls_sort = sorted(ship_pos_ls)
        ship_pos_max = ship_pos_ls_sort[2]
        ship_pos_mid = ship_pos_ls_sort[1]
        ship_pos_min = ship_pos_ls_sort[0]

        if(action.get_type() == "ship"):
            payback = action.get_payback()/(len(action.get_investors())+1)-action.get_cost()
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
