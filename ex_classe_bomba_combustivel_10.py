""" Classe Bomba de Combustível:
Faça um programa completo utilizando classes e métodos que:

a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
    1. tipoCombustivel.
    2. valorLitro
    3. quantidadeCombustivel

b. Possua no mínimo esses métodos:
    1. abastecerPorValor() – método onde é informado o valor a ser abastecido
    e mostra a quantidade de litros que foi colocada no veículo
    2. abastecerPorLitro() – método onde é informado a quantidade em litros de combustível
    e mostra o valor a ser pago pelo cliente.
    3. alterarValor() – altera o valor do litro do combustível.
    4. alterarCombustivel() – altera o tipo do combustível.
    5. alterarQuantidadeCombustivel() – altera a quantidade de combustível restante na bomba.

OBS: Sempre que acontecer um abastecimento é necessário atualizar
a quantidade de combustível total na bomba. """

class BombaCombustivel:
    def __init__(self, tipo_combustivel:str, valor_litro:float, qtde_combustivel:float):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.qtde_combustivel = qtde_combustivel


    def abastercer_por_valor(self, valor):
        qtde_abastecido = valor / self.valor_litro
        self._apresentar_abastecimento_se_possivel(qtde_abastecido, valor)

    def _apresentar_abastecimento_se_possivel(self, qtde_abastecido:float, valor:float):
        if qtde_abastecido > self.qtde_combustivel:
            print('Não há combustível o suficiente.')
            print(f'faltam {qtde_abastecido - self.qtde_combustivel:.2f} litros, para completar')
            print('Reabasteça a bomba!')
        else:
            self.qtde_combustivel -= qtde_abastecido
            print(f'Foi colocado {qtde_abastecido:.2f} litros de\
 {self.tipo_combustivel} a um valor de € {valor:.2f}')
            print(f'A quantidade de combustível restante na bomba\
 é de {self.qtde_combustivel:.2f} litros')


    def abastercer_por_litro(self, litro:float):
        valor_pago = litro * self.valor_litro
        self._apresentar_abastecimento_se_possivel(litro, valor_pago)

    # Método não necessário
    #  def alterar_valor(self, novo_valor:float):
        #  self.valor_litro = novo_valor


    # Método não necessário
    #  def alterar_combustivel(self, novo_tipo:str):
        #  self.tipo_combustivel = novo_tipo


    def adicionar_mais_combustivel(self, quantidade:float):
        if quantidade >= 0:
            self.qtde_combustivel += quantidade
        else:
            print('Não subtraia combustível desta bomba!')


bomba = BombaCombustivel('Disel', 1.80, 100.0)

#  bomba.alterar_valor(1.89)
bomba.valor_litro = 1.89

#  bomba.alterar_combustivel('Gasolina')
bomba.tipo_combustivel = 'Gasolina'

bomba.adicionar_mais_combustivel(-10.00)
#  bomba.abastercer_por_valor(10)
print()
bomba.abastercer_por_litro(10)
print()
#  bomba.abastercer_por_valor(100)
print()
#  bomba.abastercer_por_litro(10)
