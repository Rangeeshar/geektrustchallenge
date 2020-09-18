import unittest
from geektrust import KingDom
from data import Data
from ally import Ally
from message import Message
from config import KINGDOM


class TestConsumer(unittest.TestCase):

    def test_file_exits(self):
        try:
            self.assertRaises(KingDom("empty.txt"))
        except AssertionError:
            print("Passed")

    def test_parsing_whitespaces(self):
        parser = Data("test_whitespace.txt")
        self.assertTrue([["AIR", ["I HAVE WHITESPACE"]]], parser.parsedata())


    def test_process_ally(self):
        process_checker = Ally(Data("dummy.txt"), Message())
        self.assertTrue(True, process_checker.process_ally(KINGDOM["ICE"], "VTBTBHTBBBOBAB".lower()))


    def test_check_ally(self):
        checker = Ally(Data("test_check_ally.txt"), Message())
        self.assertTrue("SPACE FIRE WATER AIR", checker.check_ally())

    def test_decode(self):
        decoder = Message()
        result = decoder.decode(["ICE", "STHSTSTVSASOS"])
        self.assertTrue("mammoth", result)


    def test_secret_message_exclude_water(self):
        result = KingDom("test1.txt")
        self.assertTrue("SPACE AIR LAND ICE", result)
    
    def test_secret_message_only_air(self):
        result = KingDom("test2.txt")
        self.assertTrue("NONE", result)

if __name__ == '__main__':
    unittest.main()
