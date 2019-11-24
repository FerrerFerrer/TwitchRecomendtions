from abc import ABC, abstractmethod

class AbstactClassDB(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def save_list(self, lisofchannels, bool):
        pass

    @abstractmethod
    def get_list(self, bool):
        pass
