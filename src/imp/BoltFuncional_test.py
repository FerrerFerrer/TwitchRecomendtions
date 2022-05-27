from BoltFunctional import Bolt
from channel import Channel
from APIfuncional import apiTwitch

import unittest
from unittest.mock import Mock
from unittest.mock import patch
from unittest import TestCase
import io
import sys
import mock
from unittest.mock import MagicMock


class TestBolt(unittest.TestCase):

    def setUp(self):
        #Channels
        self.ch1 = Channel(12)
        self.ch2 = Channel(13, 10)
        self.ch3 = Channel(14, name= "Carlos")
        self.ch4 = Channel(15, name = "Roberto")
        self.ch5 = Channel(16, 15, name = "Rodrigo")
        self.ch6 = Channel(17, 20, name = "Jesus")
        self.ch7 = Channel(18, 1, name = "Chuy")
        self.ch8 = Channel(19, 7, name = "Lupe")
        self.ch9 = Channel("20","8", name ="Patty")
        self.ch10 = Channel("20",5 , name ="Ignacio")
        self.channels = [self.ch1, self.ch2, self.ch3, self.ch4, self.ch5, self.ch6, self.ch7, self.ch8, self.ch9, self.ch10]
        self.apireturn = [["Carlos", 1], ["Roberto", 2], ["Rodrigo", 3], ["Jesus", 4],
        ["Ricardo", 5], ["Chuy", 6], ["Lupe", 7], ["Ricardo", 8],["Patty", 9], ["Ignacio", 10]]


        #Bolt
        #Need to patch..?
        api = apiTwitch()
        self.testingBolt = Bolt(api, "bd")


    def testAddCHannel(self):

        for r in range(len(self.apireturn)):
            with self.subTest(r=r):
                self.testingBolt.api.get_userid = MagicMock(return_value = self.apireturn[r][1])

                self.testingBolt.addChanel(self.apireturn[r][0])

                for l in range(0,r):
                    chan = self.testingBolt.ls_channel[l]
                    name = chan.name
                    id = chan.id

                    self.assertEqual(name, self.apireturn[l][0])
                    self.assertEqual(id, self.apireturn[l][1])
        return self.testingBolt

    def testRemoveChanel(self):
        self.testingBolt.ls_channel = self.channels[2:]

        for r in range(len(self.channels[2:0]) -1 , -1, -1):
            with self.subTest(r=r):
                nametor = self.channels[r].name
                self.testingBolt.removeChanel(nametor)
                self.channels.pop(r)

                self.assertEqual(self.testingBolt.ls_channel, self.channels)

    def testBlockChannel(self):
        self.testingBolt.ls_channel = self.channels[2:]
        for r in range(len(self.channels[2:0]) -1 , -1, -1):
            with self.subTest(r=r):
                nametor = self.channels[r].name
                self.testingBolt.blockChanel(nametor)
                self.channels[r].block(True)

                self.assertEqual(self.testingBolt.ls_channel, self.channels)


    def testCalculate(self):
        self.testingBolt.ls_channel = self.channels[2:4]
        flowee = [5, 200]
        followers = [[self.ch7.id, self.ch8.id], [self.ch8.id, self.ch6.id]]
        get_name = [self.ch7.name, self.ch8.name, self.ch6.name]

        mockfolowee = MagicMock()
        mockfolowers = MagicMock()
        mockgetname = MagicMock()

        mockfolowee.side_effect = flowee
        mockfolowers.side_effect = followers
        mockgetname.side_effect = get_name

        self.testingBolt.api.get_followe = mockfolowee
        self.testingBolt.api.get_followers = mockfolowers
        self.testingBolt.api.get_name = mockgetname

        self.testingBolt.calculate()
        self.testingBolt.printRecomendations()

        expected = [self.ch8, self.ch6, self.ch7]
        obtained = self.testingBolt.ls_recomendated
        obtained.sort(key=lambda x: x._ponderation, reverse=True)
        for r in range(len(expected)):
            with self.subTest(r=r):
                self.assertEqual(obtained[r].name, expected[r].name)




if __name__ == '__main__':
    unittest.main()
