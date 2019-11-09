from abc import ABC, abstractmethod

class AbstactBolt(ABC):
    def __init__(self):
        super().__init__()
        self.ls_channel = []

    @abstractmethod
    def addChanel(self, channel):
        pass

    @abstractmethod
    def removeChanel(self, channel):
        pass

    @abstractmethod
    def blockChanel(self, channel):
        pass

    @abstractmethod
    def calculate(self):
        pass

    @abstractmethod
    def printRecomendations(self):
        pass
