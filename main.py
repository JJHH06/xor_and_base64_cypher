from nltk import trigrams, bigrams, FreqDist


import xor_cypher as xor


textoBinario = xor.getBinaryText('You call me a dog, well, thats fair enough Cause it aint no use to\
    pretend youre wrong And you call me out, I cant hide anymore \
    I have no disguise you cant see through')

print('\nFrecuencia de estrofa de You call me a dog: ')

print(dict(FreqDist(textoBinario)))

print('\nFrecuencia de estrofa cifrado en Xor')

textoXor = xor.xorRandomString(textoBinario)






