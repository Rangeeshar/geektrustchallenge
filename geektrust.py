import os
import sys
from config import *
from data import Data
from message import Message
from ally import Ally

class KingDom:
    def __init__(self, secret_messages):
        # We can change the parsing methods also in this Data class
        self.secret_messages = Data(secret_messages)
        # We can implement any new decoding methods in Message class.
        self.message_decoder = Message()
        # We can implement new method ally checking methods in Ally class.
        self.ally = Ally(self.secret_messages, self.message_decoder)
        self.ally.check_ally()

if __name__ == "__main__":
    # Starting point 
    file_name = sys.argv[1]
    obj = KingDom(file_name)
