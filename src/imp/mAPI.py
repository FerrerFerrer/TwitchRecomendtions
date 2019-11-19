from abs.absAPI import AbstactClassApi

class mockAPI(AbstactClassApi):
        def __init__(self, *args):
            super().__init__(*args)

        def get_userid(self, name):
            return "4732"

        #Who he follows - should work both with id's and name
        def get_followers(self, name_or_id):
            l = ["a", "b", "c", "d"]
            return l

        def get_name(self, id):
            return "StreamerGamer"

        #Who follows him - should work both with id's and name
        def get_followe(self, name_or_id):
            l = ["z", "x", "l", "p", "i"]
            return l

working = mockAPI("jhbdfj", "djfk")
x = working.get_name("DJFID")
print(x)
