from abs.absDataBase import AbstactClassDB

class mockBD(AbstactClassDB):
        def __init__(self, conection):
            super().__init__()
            self.conection = conection
            self.temp = []

        def save_list(self, lisofchannels):
            self.temp = lisofchannels

        def get_list(self):
            return self.temp
