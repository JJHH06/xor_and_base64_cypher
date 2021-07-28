from random import randint
import re

#Convierte un caracter a su equivalente a binario en 8 bits
def getBinaryChar(character):
    return '{0:08b}'.format(ord(character))

#Da el texto convirtiendo cada caracter en binario
def getBinaryText(text):
    return ''.join(map(getBinaryChar, text))

# convierte la cadena de 8 bits a su equivalente en ascii    
def getCharBinary(binary):
    return chr(int(binary, 2))

# da el texto conviertiendo cada 8 bits a su caracter ascii
def binaryToText(binary):
    separated = re.findall('........', binary)
    return ''.join(map(getCharBinary, separated))


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


