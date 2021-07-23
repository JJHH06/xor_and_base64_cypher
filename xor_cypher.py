from random import randint

#Convierte un caracter a su equivalente a binario en 8 bits
def getBinaryChar(character):
    return '{0:08b}'.format(ord(character))

#Da el texto convirtiendo cada caracter en binario
def getBinaryText(text):
    return ''.join(map(getBinaryChar, text))


def randomBinaryString(bits):
    result = ''
    for n in range(bits):
        result += str(randint(0,1))
    return result


def xorRandomString(binaryText):
    result = ''
    randomText = randomBinaryString(len(binaryText))
    for n in range(len(binaryText)):
        result += '0' if binaryText[n] == randomText[n] else '1'
    return result

from nltk import trigrams, bigrams