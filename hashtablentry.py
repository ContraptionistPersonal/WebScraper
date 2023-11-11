class ScraperHashTableEntry:
        def __init__(self,data,hashVal):
            self.data = data
            self.hashVal = hashVal
            self.next  = None

        def getData(self):
            return self.data

        def getHash(self):
            return self.hashVal

        def getNext(self):
            return self.next

        def setNext(self,entry):
            self.next = entry
