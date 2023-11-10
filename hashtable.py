import numpy as np
from hashtablentry import ScraperHashTableEntry
class ScraperHashTable:

    def __init__(self,size):
        self.size = size
        for i in range(size):
            self.table = []
            self.table[i]= 0
           
    

    def add(self,link):

        return hash(link) % self.size

    
