""" Recusros adicionais do exercício 2 de arquivos da lista PythonBrasil
Opcionalmente, desenvolva as seguintes funcionalidades:

(feito, line 39) 1- Ordenar os usuários pelo percentual de espaço ocupado;
(feito, line 42) 2- Mostrar apenas os n primeiros em uso, definido pelo usuário;
3- Gerar a saída numa página html;
4- Criar o programa que lê as pastas e gera o arquivo inicial;
"""

lista_de_dados = [] # para guardar os elemtentos do bloco #1

#2
# Para tranformar um numero inteiro em megabytes eu tenho que:
# 1º - transformar o numero inteiro em kbytes: num_int / (2**10)
# 2º - depois transformar kbytes em megabytes: kbytes ** 2 """
def transformar_em_megabytes(tamanho_em_bytes:str) -> float:
    """Tranformar numero inteiro em megabytes"""
    return int(tamanho_em_bytes) / (2**10) ** 2
#1
with open('/Users/fabricio/pyex/DesafioDevPro/usuarios.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        linha = linha.strip() # func .strip() remove espaços e caracteres vazios
        usuario = linha[:15] # pega os 15 primeiros caracteres de cada linha
        # pega a partir do 16º caractere ate o ultimo da linha
        tamanho_em_disco = transformar_em_megabytes(linha[16:])
     # adiciona na lista_de_dados os elemntos da tupla (tupla é uma lista q ñ pode adicioar + elem)
        lista_de_dados.append((tamanho_em_disco, usuario)) # tupla de par ordenado


#3
# Para usar uma string que vai pular linhas sem precisar do /n, utilize aspas triplas
cabecalho = '''ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso


'''

# 1- Ordenar os usuários pelo percentual de espaço ocupado;
lista_de_dados.sort(reverse=True)

# 2- Mostrar apenas os n primeiros em uso, definido pelo usuário;
n = int(input('Digite o número de usuários a ser mostrado: '))
lista_de_dados = lista_de_dados[:n]

#4
# Criar arquivo e escrever
with open('/Users/fabricio/pyex/DesafioDevPro/relatorio.txt', 'w', encoding='utf-8') as arquivo:
    tamanho_total_consumido = sum([tamanho for tamanho, _ in lista_de_dados])
    media = tamanho_total_consumido / len(lista_de_dados)
    arquivo.writelines(cabecalho) # Escreva o resultado da variavel (cabecalho)
    # Obter o numero de elementos dentro da lista
    # enumerate(lista_de_dados), enumera os elementos da lista (indice)
    # start=1, gera a contagem a partir do num 1, ao inves do num 0
    for indice, dados in enumerate(lista_de_dados, start=1):
        tamanho_em_disco, usuario = dados
        #indice:<4, cria espaçamento de 4 caracteres ordenando pela esquerda(<)
        arquivo.writelines(
            f'{indice:<4} {usuario} {tamanho_em_disco:9.2f} MB          '
            f'{tamanho_em_disco/tamanho_total_consumido:>6.2%}\n')

    arquivo.writelines('\n')
    arquivo.writelines('\n')

    arquivo.writelines(f'Espaço total ocupado: {tamanho_total_consumido:.2f} MB\n')
    arquivo.writelines(f'Espaço médio ocupado: {media:.2f} MB')
