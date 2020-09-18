from config import KINGDOM, ASCII_A, ALPHA_SIZE

class Message:
    def decode(self, message):
        '''
        decodes given encrypted message
        :params:
            message:
                type: string
        :response:
            decoded_message
        '''
        decrypted_message = ""
        cipher = len(KINGDOM[message[0]])
        data = message[1]
        for index in range(0, len(message[1])):
            decrypted_message += chr((ord(data[index]) - cipher - ASCII_A) % ALPHA_SIZE + ASCII_A)
        return decrypted_message
