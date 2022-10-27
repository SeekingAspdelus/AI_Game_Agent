'''
Author: Tianle Zhu
Date: 2022-10-27 12:07:34
LastEditTime: 2022-10-27 14:20:59
LastEditors: Tianle Zhu
FilePath: \AI_Game_Agent\investment.py

Include all investment obejct in the game Manila
    generic methods:
    -- get_availability
    -- get_investors
    -- get_payback
    -- get_cost
    -- invest
    
!! do not access the attributes directly !!
!!! you can only access/set the attributes using provided methods !!!
'''


class ship():
    '''
    ship in the game Manila
    '''
    def __init__(self,name,cost_ls,money):
        '''
        instantiate with cost and potential reward
        -- cost_ls : [,,,]
        -- money : int
        '''
        
        self.name = str(name) # name of the ship
        # check for type error
        if type(cost_ls) != list:
            raise TypeError
        for cost in cost_ls:
            if type(cost) != int:
                raise TypeError
        if type(money) != int:
            raise TypeError
        
        self.cost = cost_ls
        self.money = money
        self.position = 3
        self.available = True
        self.investors = []
        
    # methods allowed
    
    def get_availability(self):
        return self.available
    
    def get_investors(self):
        return self.investors
    
    def get_payback(self):
        return self.money
    
    def get_cost(self):
        # return the current cost to invest this ship
        idx = len(self.investors)-1
        return self.cost[idx]
    
    def invest(self,player):
        if self.get_cost > player.get_money():
            print("invalid investment, insufficient fund!")
            return
        self.investors.append(player.get_name())
        if len(self.investors) == len(self.cost):
            self.available = False
    
    # methods not allowed
    
class port():
    '''
    port in the game Manila
    '''
    def __init__(self,name,cost_ls,money):
        '''
        instantiate with cost and potential reward
        -- cost_ls : int
        -- money : int
        '''
        
        self.name = str(name) # name of the ship
        # check for type error
        if type(cost_ls) != list:
            raise TypeError
        for cost in cost_ls:
            if type(cost) != int:
                raise TypeError
        if type(money) != int:
            raise TypeError
        
        self.cost = cost_ls
        self.money = money
        self.position = 3
        self.available = True
        self.investors = []
        