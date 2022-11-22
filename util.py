"""
Author: Tianle Zhu
Date: 2022-11-20 16:13:40
LastEditTime: 2022-11-20 16:22:44
LastEditors: Tianle Zhu
FilePath: \AI_Game_Agent\util.py
"""
class Qtable(dict):
    """
    dictionary-like object
    All keys have default value 0
    """    
    def __getitem__(self, idx):
        self.setdefault(idx, 0)
        return dict.__getitem__(self, idx)
    
test = Qtable()
test[0] = 1
print(test[0])
