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
        ch1 = Channel(12)
        ch2 = Channel(13, 10)
        ch3 = Channel(14, name= "Carlos")
        ch4 = Channel(15, name = "Roberto")
        ch5 = Channel(16, 15, name = "Rodrigo")
        ch6 = Channel(17, 20, name = "Jesus")
        ch7 = Channel(17, 1, name = "Chuy")
        ch8 = Channel(17, 7, name = "Lupe")
        self.channels = [ch1, ch2, ch3, ch4, ch5, ch6, ch7, ch8]

        #Bolt
        #Need to patch..?
        api = apiTwitch()
        self.testingBolt = Bolt(api, "bd")


    def testAddCHannel(self):
        apireturn = [["Carlos", 1], ["Roberto", 2], ["Rodrigo", 3], ["Jesus", 4],
        ["Ricardo", 5], ["Chuy", 6], ["Lupe", 7], ["Ricardo", 8]]

        for r in range(len(self.channels)):
            with self.subTest(r=r):
                self.testingBolt.api.get_userid = MagicMock(return_value = apireturn[r][1])

                self.testingBolt.addChanel(apireturn[r][0])

                for l in range(0,r):
                    chan = self.testingBolt.ls_channel[l]
                    name = chan.name
                    id = chan.id

                    self.assertEqual(name, apireturn[l][0])
                    self.assertEqual(id, apireturn[l][1])


if __name__ == '__main__':
    unittest.main()
