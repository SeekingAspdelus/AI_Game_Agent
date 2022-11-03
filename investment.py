'''
Author: Tianle Zhu
Date: 2022-10-27 12:07:34
LastEditTime: 2022-11-03 13:38:19
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
    def __init__(self,name,cost_ls,payback):
        '''
        instantiate with cost and potential reward
        -- cost_ls : [,,,]
        -- payback : int
        '''
        
        self.name = str(name) # name of the ship
        # check for type error
        if type(cost_ls) != list:
            raise TypeError
        for cost in cost_ls:
            if type(cost) != int:
                raise TypeError
        if type(payback) != int:
            raise TypeError
        
        self.cost = cost_ls
        self.payback = payback
        self.position = 3
        self.available = True
        self.investors = []
        self.invest_idx = 0
        
    # methods allowed
    
    def get_position(self):
        return self.position

    def get_availability(self):
        return self.available
    
    def get_investors(self):
        return self.investors
    
    def get_payback(self):
        return self.payback
    
    def get_cost(self):
        # return the current cost to invest this ship
        return self.cost[self.invest_idx]
    
    def invest(self,player):
        if self.get_availability == False:
            print("invalide investment, unavailable ship")
            return 
        if self.get_cost() > player.get_money():
            print("invalid investment, insufficient fund!")
            return
        self.investors.append(player)
        self.invest_idx += 1
        if len(self.investors) == len(self.cost):
            self.available = False
    
    def move(self,steps):
        # move the ship steps further
        self.position += steps
    
    # methods not allowed
    
class port():
    '''
    port in the game Manila
    '''
    def __init__(self,name,cost,payback):
        '''
        instantiate with cost and potential reward
        -- cost : int
        -- money : int
        '''
        
        self.name = str(name) # name of the ship
        # check for type error
        if type(cost) != int:
            raise TypeError
        if type(payback) != int:
            raise TypeError
        
        self.cost = cost
        self.payback = payback
        self.available = True
        self.investors = []
     
    # methods allowed 
    def get_availability(self):
        return self.available
    
    def get_investors(self):
        return self.investors
    
    def get_payback(self):
        return self.payback
    
    def get_cost(self):
        return self.cost
    
    def invest(self,player):
        if self.available == False:
            print("invalid investment, unavailable port")
            return
        if self.get_cost() > player.get_money():
            print("invalid investment, insufficient fund!")
            return
        self.investors.append(player)
        self.available = False
        
class shipyard():
    '''
    shipyard in the game Manila
    '''
    def __init__(self,name,cost,payback):
        '''
        instantiate with cost and potential reward
        -- cost : int
        -- money : int
        '''
        
        self.name = str(name) # name of the ship
        # check for type error
        if type(cost) != int:
            raise TypeError
        if type(payback) != int:
            raise TypeError
        
        self.cost = cost
        self.payback = payback
        self.available = True
        self.investors = []
     
    # methods allowed 
    def get_availability(self):
        return self.available
    
    def get_investors(self):
        return self.investors
    
    def get_payback(self):
        return self.payback
    
    def get_cost(self):
        return self.cost
    
    def invest(self,player):
        if self.available == False:
            print("invalid investment, unavailable shipyayd")
            return
        if self.get_cost() > player.get_money():
            print("invalid investment, insufficient fund!")
            return
        self.investors.append(player)
        self.available = False
        
        
