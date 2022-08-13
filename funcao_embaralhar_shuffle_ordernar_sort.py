""" Fução shuffle -> embaralhar
    Fução sort -> ordernar """

from random import shuffle

numeros = list(range(10)) # -> Faz uma lista de numeros de 0 a 9
print(numeros)

shuffle(numeros) # Mostra a lista de numeros de 0 a 9 de forma embaralhada
print(numeros)

numeros.sort() # Mostra a lista de numeros de 0 a 9 de forma ordenada
print(numeros)

numeros.sort(reverse=True) # Mostra a lista de numeros de forma ordenada decrescente*
print(numeros)

#  print((10, 'Fabricio') < (11, 'Bento'))
