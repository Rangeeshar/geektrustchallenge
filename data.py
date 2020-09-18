import os
from config import VALID_PATH_ERROR

class Data:
    def __init__(self, input_file):
        self.file = input_file
        assert os.path.exists(self.file), VALID_PATH_ERROR
    
    def parsedata(self):
        '''
        parses and returns data in list of lists
        :params:
            None
        :response_format:
            [["AIR", "message"], ["SPACE", "message"]]
        '''
        inp_data = []
        with open(self.file) as f:
            for line in f:
                d1, d2 = line.strip().split(" ", 1)
                inp_data.append([d1, d2.lower()])
        return inp_data


