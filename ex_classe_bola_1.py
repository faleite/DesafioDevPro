""" Classe:

1. Classe Bola: Crie uma classe que modele uma bola:
    a. Atributos: Cor, circunferência, material
    b. Métodos: trocaCor e mostraCor
"""

# Classe -> É uma estrutura de dados, e uma forma de criar o seus próprios tipos
# Exemplo de tipos: int, float, str...
# class -> type, classe -> tipo (class e type são quase sinônimos)
# Classe possui Atributos, e Métodos
# Atributos -> atributos de dados
# Métodos -> atributos executáveis (exemplo método append da lista. -> .append())
# Métodos é uma função que sempre recebe como primeiro parâmetro um objeto

# criar uma classe:
# palavra reservada class e defina seu nome com as primeiras letras em Maiuscúlo
#  class CirculoPerfeito:
    #  pass ->usada para quando não é definido algo, desta forma ainda é possivel criar os objetos

class CirculoPerfeito:
    def __init__(self): # método que serve para criar os atributos de dados dos objetos
        self.cor = 'Azul' # Atributo cor
        self.circunferencia = 4 # Atributo circunferencia
        self.material = 'Papel' # Atributo papel


    # mostra_cor -> método, self -> obejto (primeiro parâmetro)
    def mostra_cor(self): #sempre recebe self como primeiro parâmetro, que sera o objeto em questão
        #  return id(self) # id é um numero de identificção de um objeto em execução
        return self.cor


    def troca_cor(self, cor): # cor -> segundo paramento
        self.cor = cor # troca atributo cor, passando o segundo parametro -> cor


# circulo_primeiro -> obejto -> ele é sempre o primeiro parâmetro do método -> self)
circulo_primeiro = CirculoPerfeito()
circulo_segundo = CirculoPerfeito()  # circulo_segundo -> obejto

print(type(circulo_primeiro))
# >>> <class '__main__.CirculoPerfeito'>
print(circulo_primeiro is circulo_segundo)
# >>> False

print(id(circulo_primeiro), circulo_primeiro.mostra_cor())
# >>> 4413456096 Azul (4413456096)
print(id(circulo_segundo), circulo_segundo.mostra_cor())
# >>> 4392615648 Azul (4392615648)

print(circulo_primeiro.cor, circulo_segundo.cor) # acessando o atributo cor
# >>> Azul Azul
circulo_segundo.cor = 'Amarelo' # desta forma você pode alterar o valor dos atributos de dados
print(circulo_segundo.cor)
# >>> Amarelo

circulo_segundo.troca_cor('Vermelho')
print(circulo_segundo.cor)
# >>> Vermelho
