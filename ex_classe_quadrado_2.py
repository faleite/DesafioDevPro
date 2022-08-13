"""  Classe Quadrado:
Crie uma classe que modele um quadrado:

a. Atributos: Tamanho do lado
b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""



# Resolução professor:
class Quadrado:
    def __init__(self, lado = 1): # podemos receber os valores de atributos no __init__ -> lado
        self.lado = lado


    def calcular_area(self):
        return self.lado ** 2

quadrado = Quadrado(4) # A classe implicitamente chama o __init__ -> altera o lado para 4
print(quadrado.lado, quadrado.calcular_area())

# Minha resolução:
class ModelarQuadrado:
    def __init__(self):
        self.tamanho_do_lado = 10


    def mudar_valor_do_lado(self, tamanho_do_lado):
        self.tamanho_do_lado = tamanho_do_lado


    def retornar_valor_do_lado(self):
        self.tamanho_do_lado = 10


    def calcular_area(self):
        return self.tamanho_do_lado ** 2


quadrado_primeiro = ModelarQuadrado()
quadrado_segundo = ModelarQuadrado()

# print(id(quadrado_primeiro), id(quadrado_segundo))

#  print(quadrado_primeiro.tamanho_do_lado)

#  quadrado_primeiro.mudar_valor_do_lado(7)
#  print(quadrado_primeiro.tamanho_do_lado)

#  quadrado_primeiro.retornar_valor_do_lado()
#  print(quadrado_primeiro.tamanho_do_lado)

#  print(quadrado_primeiro.calcular_area())
