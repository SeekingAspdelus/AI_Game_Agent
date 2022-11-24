import numpy as np
class Qtable(dict):
    """
    dictionary-like object
    All keys have default value 0
    """    
    def __getitem__(self, idx):
        self.setdefault(idx, 0)
        return dict.__getitem__(self, idx)
    
def randomChoice(arr, Myseed = None):
    if Myseed != None:
        np.random.seed(Myseed)
    return arr[np.random.randint(len(arr))]