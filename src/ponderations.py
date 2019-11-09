from collections import OrderedDict
import random

# def helperPonderByUnionOfChannels(channels, MAX_DEEP, DEEP, rep = {}):
#     pass

def ponderByFollowers(channel):
    #folowes       : mult
    #0      -   100: 1.0
    #101    -  1000: 1.5
    #1001   -  5000: 1.8
    #5001   - 10000: 2.0
    #10000  - 50000: 3.0
    #50001  - 90000: 4.0
    #900001+       : 5.0

    #return mult/following
    pass

#It adds to the ponderation bases on how many local channels follow the same one
def ponderByUnionOfChannels(channels):
    rep = {}
    for channel in channels:
        #multiplyer = ponderByFollowers(channel)
        multiplyer = random.random() + 1
        for subchannel in channel: #channel.getFollowers():
            if subchannel in rep.keys():
                rep[subchannel] += multiplyer
            else:
                rep[subchannel] = multiplyer

    ls = [ [k,v] for k, v in rep.items() ]
    ls = sorted(ls, key = lambda x: x[1], reverse = True)
    return ls[:10]

#It ponders by recent activity of the user, day, week, month, etc..
#It ponders how many streams does it has
def ponderByActivity(channel):
    pass

#Maybe rising star?
def ponderByNewUser(channel):
    pass

def maint():
    ch1 = ["a", "b", "d", "p"]
    ch2 = ["a", "d", "c", "f"]
    ch3 = ["a", "b", "d", "e"]
    ch4 = ["a", "b", "c", "d"]
    mother_of_channels = []
    mother_of_channels.append(ch1)
    mother_of_channels.append(ch2)
    mother_of_channels.append(ch3)
    mother_of_channels.append(ch4)

    f = ponderByUnionOfChannels(mother_of_channels)
    print(f)

if __name__ == '__main__':
    maint()
