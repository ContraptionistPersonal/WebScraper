import numpy as np
from hashtablentry import ScraperHashTableEntry as SHTE
class ScraperHashTable:

    def __init__(self,size):
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append(0)
           
    def hashLink(self,link):
        return hash(link) % self.size

    def addLink(self,link):
        hashedLink = self.hashLink(link) # hash link
        indexValue = self.getIndex(hashedLink) # check if hashed positon is empty
        
        invalid = False
        entry = SHTE(link,hashedLink)
        if indexValue == 0:
            self.setIndex(hashedLink,entry)

        else:
            node = self.getIndex(hashedLink)
            while node.getNext() != None:
                if link != node.getData():
                    node = node.getNext()
                else:
                    print("-------------------------->duplicate")
                    invalid = True
                    break
            if invalid == False:
                node.setNext(entry)

    def displayTable(self):
        for i in range(self.size):
            if (isinstance(self.getIndex(i),SHTE)):
                node = self.getIndex(i)
                print(node.getData())
                while node.getNext() != None:
                    print(node.getData())
                    node = node.getNext()

            else:
                print("Empty")

    def getIndex(self,index):
        return self.table[index]

    def setIndex(self,index,data):
        self.table[index] = data;

    
