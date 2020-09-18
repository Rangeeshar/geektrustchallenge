from config import RULER, KINGDOM, REQUIRED_ALLEGIANCE

class Ally:
    def __init__(self, message, decoder):
        self.secret_message = message
        self.decoder = decoder
    
    def process_ally(self, pattern, message):
        '''
        Process the message from kingdom and\
                returns True if emblem in it else false
        :params:
            pattern:
                type: string
            txt:
                type: string
        :response:
            True/False
        '''
        m1 = sorted(pattern)
        m2 = sorted(message)
        if len(pattern) >= 1 and len(message) >= 1:
            for alpha in m2:
                try:
                    m1.remove(alpha)
                except:
                    return False
            return True
        return False

    def check_ally(self):
        '''
        Checks allies count
        :params:
            data:
                type: string
        :response:
            "None"/(list of allies)
        '''
        ally, allies = 0, [RULER]
        for encoded_message in self.secret_message.parsedata():
            decoded_message = self.decoder.decode(encoded_message)
            resp = self.process_ally(decoded_message, KINGDOM[encoded_message[0]])
            if resp:
                ally += 1
            if encoded_message[0] not in allies:
                allies.append(encoded_message[0])

        if len(allies) >= REQUIRED_ALLEGIANCE:
            print(" ".join(allies))
        else:
            print("NONE") 
