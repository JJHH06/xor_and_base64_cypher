from nltk import trigrams, bigrams, FreqDist
import xor_cypher as xor
import cifrado64 as cf64
import matplotlib.pyplot as plt


print('Convertir texto a cadena de 8 bits y viceversa, 3 ejemplos sencillos: \n')

b1 = xor.getBinaryText('Esta es una prueba para conversion de texto a binario')
tb1 = xor.binaryToText(b1)

print('binario 1:', b1, end='\n\n')
print('texto 1:', tb1, end='\n\n')
print('-----------------------------------\n')


b1 = xor.getBinaryText('Hola mundo desde el lenguaje de programacion python')
tb1 = xor.binaryToText(b1)

print('binario 2:', b1, end='\n\n')
print('texto 2:', tb1, end='\n\n')
print('-----------------------------------\n')


b1 = xor.getBinaryText(
    'Los algoritmos de cifrado son importantes para poder almacenar mensajes o informacion de forma segura para que solo nosotros sepamos que contiene')
tb1 = xor.binaryToText(b1)

print('binario 3:', b1, end='\n\n')
print('texto 3:', tb1, end='\n\n')
print('-----------------------------------\n')


print('\n\nConvertir texto a base 64 y viceversa, 3 ejemplos sencillos: \n')

b1 = cf64.encode('Esta es una prueba para conversion de texto a binario')
tb1 = cf64.decode(b1)

print('cifrado en base64 1:', b1, end='\n\n')
print('desifrado de base64 a texto 1:', tb1, end='\n\n')
print('-----------------------------------\n')


b1 = cf64.encode('Hola mundo desde el lenguaje de programacion python')
tb1 = cf64.decode(b1)

print('cifrado en base64 2:', b1, end='\n\n')
print('desifrado de base64 a texto 2:', tb1, end='\n\n')
print('-----------------------------------\n')


b1 = cf64.encode(
    'Los algoritmos de cifrado son importantes para poder almacenar mensajes o informacion de forma segura para que solo nosotros sepamos que contiene')
tb1 = cf64.decode(b1)

print('cifrado en base64 3:', b1, end='\n\n')
print('desifrado de base64 a texto 3:', tb1, end='\n\n')
print('-----------------------------------\n')


def plot(data, title):
    plt.figure(title)
    plt.style.use('ggplot')
    plt.ylabel("Frecuencia")
    plt.bar(data.keys(), data.values(), align='center', width=0.8)


def drawGraphs(textoBinario, title):
    freq = dict(FreqDist(textoBinario))
    plot(freq, f'Fracuencia de 0 y 1 {title}')

    bigramFreq = list(bigrams(textoBinario))
    freq = {}
    for n in bigramFreq:
        if n not in freq:
            freq[n] = 0
        freq[n] += 1
    freq = dict([(f'{item[0]}', item[1]) for item in freq.items()])
    plot(freq, f'Bigrama {title}')

    trigramFreq = list(trigrams(textoBinario))
    freq = {}
    for n in trigramFreq:
        if n not in freq:
            freq[n] = 0
        freq[n] += 1
    freq = dict([(f'{item[0]}', item[1]) for item in freq.items()])
    plot(freq, f'Trigrama {title}')

    plt.show()  # graficar histogramas


testText = """
You call me a dog, well, thats fair enough Cause it aint no use to
pretend youre wrong And you call me out, I cant hide anymore 
I have no disguise you cant see through
"""

textoBinario = xor.getBinaryText(testText)

print('\nFrecuencia de estrofa de You call me a dog: ')
drawGraphs(textoBinario, '- texto normal')


textoXor = xor.xorRandomString(textoBinario)
drawGraphs(textoXor, '- texto XOR')

