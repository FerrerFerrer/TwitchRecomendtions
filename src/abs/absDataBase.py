from abc import ABC, abstractmethod

class AbstactClassApi(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def save_list(self, lisofchannels):
        pass

    @abstractmethod
    def get_list(self):
        pass
