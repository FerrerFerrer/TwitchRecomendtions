from abs.absBolt import AbstactBolt
#Main program - User Interface
import sys
sys.path.append('../classes')
from channel import Channel


class mockBolt(AbstactBolt):
        def __init__(self, api, basedatos):
            super().__init__(basedatos)
            self.api = api
            self.ls_recomendated = []

            def get_index_in_list(self, id_name, nameB, ls):
                for r in range(len(ls)):
                    ls_in = ""
                    if(nameB):
                        ls_in = ls[r].name
                    else:
                        ls_in = ls[r].id

                    if ls_in is id_name:
                        return r

                return -1

        def addChanel(self, name):
            id = api.get_userid(name)
            temp = Channel(id = id, name = name)
            self.ls_channel.append(temp)

        def removeChanel(self, name):
            idx = get_index_in_list(name, True, self.ls_channel)
            if idx is not -1:
                self.ls_channel.pop(idx)
            else:
                print("ERROR: Couldn´t find that channel in the list")

        def blockChanel(self, name):
            idx = get_index_in_list(name, True, self.ls_channel)
            if idx is not -1:
                self.ls_channel[idx].block(True)
            else:
                print("ERROR: Couldn´t find that channel in the list")

        def calculate(self):
            print("Calculating")

        def printRecomendations(self):
            print("This are your recomendations!")

        def get_session(self):
            pass

        def save_session(self):
            pass

        ####################
        ##  Ponderations  ##
        ####################
        def ponderByFollowers(number):
            if number < 100:
                return 10.0
            elif number < 1000:
                return 15.0
            elif number < 5000:
                return 18.0
            elif number < 10000:
                return 20.0
            elif number < 50000:
                return 30.0
            elif number < 100000:
                return 40.0
            elif number < 1000000:
                return 50.0
            else:
                return 70.0

        def ponderByUnionOfChannels(self):
            self.ls_recomendated = []           #Reseting list...
            for channel in channels:
                if channel.blocked is True:
                    continue
                num_fol = api.get_followe(channel.id)
                mult = ponderByFollowers(num_fol)
                subs = api.get_followers(channel.id)
                mult = mult / len(subs)

                for subchannel in subs: #channel.getFollowers():

                    #Existe como un usuario que ya sigue?
                    idx_temp = get_index_in_list(idx, False, self.ls_channel)
                    if idx_temp is not -1:
                        #Ya existe
                        continue
                    else:
                        #No existe

                        #Existe como ya recomendado?
                        idx = get_index_in_list(subchannel, False, self.ls_recomendated)
                        if idx is -1:
                            #No existe
                            temp_channel = Channel(id = subchannel, name = api.get_name(subchannel), ponderation = mult)
                            self.ls_recomendated.append(temp_channel)
                        else:
                            #Ya existe
                            self.ls_recomendated[idx].addPonderation(mult)


if __name__ == '__main__':
    bo = mockBolt("api", "bd")
    bo.calculate()
