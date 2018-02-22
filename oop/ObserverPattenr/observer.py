
class Publisher:
    def __init__(self):
        pass

    def register(self,obs):
        pass

    def unregister(self,obs):
        pass

    def notifyAll(self):
        pass


class StockPublisher(Publisher):
    def __init__(self):
        super().__init__()
        self._listOfObs = []
        self.ibmprice = None
        self.appPrice = None
        self.googlePrice = None


    def register(self,obs):
        if obs not in self._listOfObs:
            self._listOfObs.append(obs)

    def unregister(self,obs):
        self._listOfObs.remove(obs)

    def notifyAll(self):
        for obs in self._listOfObs:
            obs.update(self.ibmprice,self.appPrice,self.googlePrice)

    def setIbmPrice(self,newPrice):
        self.ibmprice = newPrice
        self.notifyAll()

    def setAppPrice(self, newPrice):
        self.appPrice = newPrice
        self.notifyAll()

    def setGoglePrice(self, newPrice):
        self.googlePrice = newPrice
        self.notifyAll()


class Observer:
    def __init__(self):
        pass
    def update(self,ibmprice,appPrice,googlePrice):
        pass

class StockObserver(Observer):
    def __init__(self,id):
        super().__init__()
        self.id = id
    def update(self,ibmprice,appPrice,googlePrice):
        print("Stock Updated "+str(self.id)+": \nIBM :"+str(ibmprice)+"\nAPP :"+str(appPrice)+"\nGooG :"+str(googlePrice))

"""
if __name__ == "__main__":
    publishstock = StockPublisher()
    stockObserver1 = StockObserver()
    publishstock.register(stockObserver1)
    publishstock.setAppPrice(0.0)
    publishstock.setAppPrice(0.2)
    publishstock.setGoglePrice(23.0)
    publishstock.setIbmPrice(2.0)
"""
publishstock = StockPublisher()
stockObserver1 = StockObserver(1)
stockObserver2 = StockObserver(2)
publishstock.register(stockObserver1)
publishstock.register(stockObserver2)
publishstock.setAppPrice(0.0)
publishstock.setAppPrice(0.2)
publishstock.setGoglePrice(23.0)
publishstock.setIbmPrice(2.0)
