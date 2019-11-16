from abc import ABC, abstractmethod

class AbstactBolt(ABC, basedatos):
    def __init__(self):
        super().__init__()
        self.ls_channel = []
        self.bd = basedatos

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

    @abstractmethod
    def save_session(self):
        #bd.save_list(self.ls_channel)
        pass

    @abstractmethod
    def get_session(self):
        #self.ls_channel = bd.get_list()
        pass
