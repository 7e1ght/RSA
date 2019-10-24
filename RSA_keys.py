from random import *
from math import *
from os import urandom

class Key:
    def __init__(self, bitSize):
        self.__bitSize = bitSize

    def __isPrime(self, n):
        if n==2 or n==3: return True
        if n%2==0 or n<2: return False
        for i in range(3,int(n**0.5)+1,2):   # only odd numbers
            if n%i==0:
                return False
        return True

    def __randBitNumber(self):
        return randint(2**(self.__bitSize-1)+1, 2**self.__bitSize)

    def __getPrime(self):
        num = self.__randBitNumber()

        while not self.__isPrime(num):
            num = self.__randBitNumber()

        return num
    
    def __isRelativePrime(self, a, b):
        m = a*b
        while a != 0 and b != 0:
            if a > b:
                a %= b
            else:
                b %= a
        lcm = m // (a+b)

        if lcm == m: return True
        else: return False

    def __getRealativePrime(self, a):
        for i in range(3, int(a**1/2)):
            if self.__isRelativePrime(i, a): return i

        raise Exception("Не удалось найти относительно простое число.")

    def getD(self, a, b):
        if b == 0:
            return a, 1, 0
        else:
            d, x1, y1 = self.getD(b, a%b)
            x = y1
            y = x1-(a//b)*y1
            return d, x, y


    def getKeys(self):
        p = self.__getPrime()
        # p =  3557

        q = self.__getPrime() 
        # q = 2579

        n = p * q
        eler = (p-1) * (q-1)

        e = self.__getRealativePrime(eler)
        d = self.getD(e, eler)[1]

        if d < 0:
            d = d+abs(d)*e+1

        #open key, close key
        return [[e, n], [d, n]]