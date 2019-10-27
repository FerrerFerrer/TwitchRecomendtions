class Channel:
    def __init__(self, id, ponderation = 0):
        self.id = id
        self.ponderation = ponderation
        self.followers = []

    def addPonderation(num):
        self.ponderation += num

    def multiplyPonderation(num):
        self.ponderation *= num

    def resetPonderation():
        self.ponderation = 0

    def changeId(id):
        self.id = id

    def addFollower(channel):
        self.followers.append(channel)

    def removeFollower(channel):
        self.followers.remove(channel)

    def getFollowers():
        #return something
        pass
