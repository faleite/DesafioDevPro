""" Exercício 1

Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro
arquivo, contendo um relatório dos endereços IP válidos e inválidos.

- O arquivo de entrada possui o seguinte formato:

200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
9.8.234
192.168.0.256

- O arquivo de saída possui o seguinte formato:

[Endereços válidos:]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4

[Endereços inválidos:]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256

"""
def validar_ip(ips: str) -> bool:
    """ips validos e inválidos."""
    numeros = ips.split('.')

    if len(numeros) != 4:
        return False

    for numero in numeros:
        if not 0 <= int(numero) <= 255:
            return False
    return True

ips_validos = []
ips_invalidos = []

# Lista de endereços ip
# Acessa arquivo e retorna os valores
with open('/Users/fabricio/p_ex/ips.txt', 'r', encoding='utf-8') as arquivo:
    for linha in arquivo:
        ip = linha.strip()
        if validar_ip(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)

with open('/Users/fabricio/p_ex/lista_ips.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.writelines('[Endereços válidos:]\n')

    for ip in ips_validos:
        arquivo.writelines(f'{ip}\n')

    arquivo.writelines('\n')
    arquivo.writelines('\n')

    arquivo.writelines('[Endereços inválidos:]\n')
    for ip in ips_invalidos:
        arquivo.writelines(f'{ip}\n')
