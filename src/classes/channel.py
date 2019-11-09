class Channel:
    def __init__(self, id, ponderation = 0, name = ""):
        self.id = id
        self._ponderation = ponderation
        self.followers = []
        self.blocked = False
        self.name = name

    def addPonderation(num):
        if(not blocked):
            self.ponderation += num
        else:
            return -1

    def multiplyPonderation(num):
        if(not blocked):
            self.ponderation *= num
        else:
            return -1

    def resetPonderation():
        if(not blocked):
            self.ponderation = 0
        else:
            return -1

    def changeId(id):
        self.id = id

    def addFollower(channel):
        self.followers.append(channel)

    def removeFollower(channel):
        self.followers.remove(channel)

    def getFollowers():
        #return something[]
        pass

    def block(b):
        self.blocked = b

        if self.blocked:
            self.ponderation = -9999999
        else:
            self.resetPonderation()
