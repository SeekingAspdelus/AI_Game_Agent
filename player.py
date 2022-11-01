'''
LastEditors: SeekingAspdelus jz332@duke.edu
Date: 2022-10-27 12:19:15
LastEditTime: 2022-11-01 12:17:17
FilePath: \AI_Game_Agent\player.py

All the method in this file is used to control the player's action.
method may be called in this file:
    get_behavior()
    get_name()
    get_money()
    get_color()
    get_action()
    invest()
    status()
'''


import pandas

class Player:
    def __init__(self, name, money, color):
        self.name = name # player's name 
        self.money = money # in Peso int
        self.color = color # player's color
        self.behavior = [] #player's used behavior

    def __str__(self):
        return f'{self.name} has {self.money} Peso, his/her color is {self.color}'  

    def add_behavior(self, behavior): 
        self.behavior.append(behavior)

    def get_behavior(self):
        return self.behavior

    def get_name(self):
        return self.name

    def get_money(self):
        return self.money

    def set_money(self, money):
        self.money = money

    def get_color(self):
        return self.color

    def get_action(self):
        self.available_action = []
        return self.available_action

    def invest(self, action):
        self.get_action()
        if action in self.available_action:
            self.add_behavior(action)
            self.money -= action.get_cost()
            action.invest(self.name)
            print(f'You have succeeded in investing  + {action.name}')
        else:
            print('Invalid action, please specify an action from the list')

    def profit(self, money):
        self.money += money

    def status(self):
        print(f'You are {self.name}, your color is {self.color}, you have {self.money} Peso')
        for i in self.behavior:
            print(f'You have invested in {i.name} for this turn')