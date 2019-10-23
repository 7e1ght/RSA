from RSA_keys import Key

class Crypt:
    def __init__(self):
        self.keys = Key(8)
        self.openKey, self.closeKey = self.keys.getKeys()

    def encrypt(self, text):
        codeArray = []
        for i in range(len(text)):
            codeArray.append((ord(text[i])**self.openKey[0])%self.openKey[1])

        return codeArray

    def decode(self, encryptedArray):
        codeArray = []
        for i in range(len(encryptedArray)):
            codeArray.append(chr((encryptedArray[i]**self.closeKey[0])%self.closeKey[1]))
        s = ""
        return s.join(codeArray)

c = Crypt()

print(c.decode(c.encrypt("Vlad")))