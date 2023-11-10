import numpy as np
class ScraperHashTable:

    def __init__(self,size):
        self.size = size
        self.table = np.empty(size)
    

    def addHt(self,link):
        return hash(link) % self.size

    
