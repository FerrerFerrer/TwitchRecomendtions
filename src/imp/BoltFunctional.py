from abs.absBolt import AbstactBolt
#Main program - User Interface
import sys
sys.path.append('../classes')
from channel import Channel
from tqdm import tqdm

DEBUG = False

class Bolt(AbstactBolt):
        def __init__(self, api, basedatos):
            super().__init__(basedatos)
            self.api = api
            self.ls_recomendated = []

        def printChannel(self, ls):
            for x in ls:
                print(x.toString())

        def viewChannels(self):
            self.printChannel(self.ls_channel)

        def get_index_in_list(self, id_name, nameB, ls):
            if(DEBUG):
                print("Index", id_name, nameB)
            for r in range(len(ls)):
                if(DEBUG):
                    print(ls[r])
                ls_in = ""
                if(nameB):
                    ls_in = ls[r].name
                    if(DEBUG):
                        print(ls[r].name)
                else:
                    ls_in = ls[r].id
                    if(DEBUG):
                        print(ls[r].id)

                if ls_in == id_name:
                    if(DEBUG):
                        print("found", r)
                    return r
                else:
                    if(DEBUG):
                        print("Not found", ls_in, "is not", id_name)
            return -1

        def addChanel(self, name):
            try:
                id = self.api.get_userid(name)
                temp = Channel(id = id, name = name)
                self.ls_channel.append(temp)
                print("El canal se agrego correctamente")
            except:
                print("Hubo un error agregando el canal")
            if(DEBUG):
                self.printChannel(self.ls_channel)

        def removeChanel(self, name):
            try:
                idx = self.get_index_in_list(name, True, self.ls_channel)
                if idx is not -1:
                    self.ls_channel.pop(idx)
                    print("Se elimino correctamente")
                else:
                    print("ERROR: Couldn´t find that channel in the list")
            except:
                print("Hubo un error eliminando el canal")
            if(DEBUG):
                self.printChannel(self.ls_channel)

        def blockChanel(self, name):
            try:
                idx = self.get_index_in_list(name, True, self.ls_channel)
                if idx is not -1:
                    self.ls_channel[idx].block(True)
                    print("Se bloqueo correctamente")
                else:
                    print("ERROR: Couldn´t find that channel in the list")
            except:
                print("Hubo un error el bloquear el canal")
            if(DEBUG):
                self.printChannel(self.ls_channel)

        def printRecomendations(self):
            print("Esta es la lista completa")
            self.ls_recomendated.sort(key=lambda x: x._ponderation, reverse=True)
            self.printChannel(self.ls_recomendated[:10])

        def get_session(self):
            print("Coming soon...")

        def save_session(self):
            print("Coming soon...")

        ####################
        ##  Ponderations  ##
        ####################
        def ponderByFollowers(self, number):
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
            for channel in tqdm(self.ls_channel):
                if channel.blocked is True:
                    continue
                num_fol = self.api.get_followe(channel.id)
                mult = self.ponderByFollowers(num_fol)
                subs = self.api.get_followers(channel.id)
                mult = mult / len(subs)

                for subchannel in tqdm(subs):
                    #Existe como un usuario que ya sigue?
                    idx_temp = self.get_index_in_list(subchannel, False, self.ls_channel)
                    if idx_temp is not -1:
                        #Ya existe
                        continue
                    else:
                        #No existe

                        #Existe como ya recomendado?
                        idx = self.get_index_in_list(subchannel, False, self.ls_recomendated)
                        if idx is -1:
                            #No existe
                            try:
                                temp_channel = Channel(id = subchannel, name = self.api.get_name(subchannel), ponderation = mult)
                                self.ls_recomendated.append(temp_channel)
                            except:
                                print("ERROR", subchannel)
                        else:
                            #Ya existe
                            self.ls_recomendated[idx].addPonderation(mult)

        def calculate(self):
            self.ponderByUnionOfChannels()
            print("Calculo terminado")

if __name__ == '__main__':
    bo = mockBolt("api", "bd")
    bo.calculate()
