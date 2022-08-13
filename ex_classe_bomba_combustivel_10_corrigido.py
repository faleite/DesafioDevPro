"""Classe bomba"""

class BombaCombustivel:
    def __init__(self, tipo_combustivel:str, valor_litro:float, qtde_combustivel:float):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.qtde_combustivel = qtde_combustivel


    def abastercer_por_valor(self, valor:float):
        litros_abastecidos = valor / self.valor_litro
        self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)


    # Método a parte, só utiliza internamenente dentro da classe
    # leva o _ como primeiro caractere do nome do método -> _apresentar_
    def _apresentar_abastecimento_se_possivel(self, litros_abastecidos:float, valor:float):
        if litros_abastecidos > self.qtde_combustivel:
            print(f'Não é possível abastercer, faltam\
 {litros_abastecidos - self.qtde_combustivel:.2f} litros.')
            print('Reabasteça a bomba')
        else:
            self.qtde_combustivel -= litros_abastecidos
            print(f'Foram abastecidos {litros_abastecidos:.2f} litros a um valor R$ {valor:.2f}')
            print(f'Sobraram na bomba {self.qtde_combustivel:.2f}\
 litros de {self.tipo_combustivel}')


    def abastercer_por_litros(self, litros_abastecidos:float):
        valor = litros_abastecidos * self.valor_litro
        self._apresentar_abastecimento_se_possivel(litros_abastecidos, valor)


    def adicionar_mais_combustivel(self, quantidade:float):
        if quantidade >= 0:
            self.qtde_combustivel += quantidade
        else:
            print('Não tire combustível dessa bomba')


bomba = BombaCombustivel('Gasolina', 4.59, 100.0)

bomba.abastercer_por_valor(100)
print()
bomba.abastercer_por_litros(50)
print()
bomba.valor_litro = 5.59
bomba.abastercer_por_litros(50)

bomba.adicionar_mais_combustivel(-100)
print()
bomba.abastercer_por_litros(50)
