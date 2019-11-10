from abc import ABC, abstractmethod

class AbstactClassApi(ABC):
    def __init__(self, client_id, oauth_token, accept = "application/vnd.twitchtv.v5+json"):
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

    @abstractmethod
    def get_followers(self, id):
        pass

    @abstractmethod
    def get_name(self, id):
        pass

    @abstractmethod
    def get_followe(self, id):
        pass
