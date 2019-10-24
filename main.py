from crypt import *
from RSA_keys import *

crypt = Crypt()
key = Key(8)
openKey, closeKey = key.getKeys()

# open("Vlad.txt", 'w')
encrypt = crypt.encrypt("Vlad", openKey)
print(crypt.decrypt(encrypt, closeKey))