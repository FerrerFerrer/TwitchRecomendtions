from abc import ABC, abstractmethod

class AbstactClassApi(ABC):
    def __init__(self, client_id = 'vnsbdjciw4fcif1k57w1c07a65wk03', oauth_token = 'oauth:17qyf4koyvfdqjs4me7zr451lccmtn', accept = "application/vnd.twitchtv.v5+json"):
        super().__init__()
        self.client_id = client_id
        self.oauth_token = oauth_token
        self.accept = accept
        self.HEADS = {
            "Accept" : self.accept,
            "Client-ID" : self.client_id
            }

    @abstractmethod
    def get_userid(self, name):
        pass

    #Who he follows - should work both with id's and name
    @abstractmethod
    def get_followers(self, name_or_id):
        pass

    #@abstractmethod
    #def get_name(self, id):
    #    pass
#
    #Who follows him - should work both with id's and name
    @abstractmethod
    def get_followe(self, name_or_id):
        pass
