class Crypt:
    def encrypt(self, text, key):
        codeArray = []
        for i in range(len(text)):
            codeArray.append(str((ord(text[i])**key[0])%key[1]))
        s = "."
        return s.join(codeArray)

    def decrypt(self, encryptedString, key):
        encryptedArray = encryptedString.split(".")
        codeArray = []
        for i in range(len(encryptedArray)):
            codeArray.append(chr((int(encryptedArray[i])**key[0])%key[1]))
        s = ""
        return s.join(codeArray)
