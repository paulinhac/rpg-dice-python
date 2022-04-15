# importando o módulo random
import random

# perguntando o desejo do usuário
jogar_dado = input("Você deseja jogar o dado? Responda 'sim' ou 'não'")


# perguntando que tipo de dado o usuário quer jogar
def inicia_jogo():
    tipo_de_dado = int(input("Você quer jogar um dado de quantas faces? Opções: 4,6,8,10,12 e 20"))
    if tipo_de_dado == 4:
        resposta = random.randint(1, 4)
        print(resposta)
    elif tipo_de_dado == 6:
        resposta = random.randint(1, 6)
        print(resposta)
    elif tipo_de_dado == 8:
        resposta = random.randint(1, 8)
        print(resposta)
    elif tipo_de_dado == 10:
        resposta = random.randint(1, 10)
        print(resposta)
    elif tipo_de_dado == 12:
        resposta = random.randint(1, 12)
        print(resposta)
    elif tipo_de_dado == 20:
        resposta = random.randint(1, 20)
        print(resposta)
    else:
        print("Valor inválido, tente novamente!")


# Criando as estrututras de repetição para que o jogo não encerre na primeira tentativa, caso o usuário deseje continuar
while jogar_dado.upper() != "SIM" and jogar_dado.upper() != "NÃO":
    print("Resposta inválida, tente novamente")
    jogar_dado = input("Você deseja jogar o dado? Responda 'sim' ou 'não'")

while jogar_dado.upper() == "SIM":
    inicia_jogo()
    jogar_dado = input("Você deseja jogar o dado? Responda 'sim' ou 'não'")
    while jogar_dado.upper() != "SIM" and jogar_dado.upper() != "NÃO":
        print("Resposta inválida, tente novamente")
        jogar_dado = input("Você deseja jogar o dado? Responda 'sim' ou 'não'")

# Encerrando o jogo
if jogar_dado.upper() == "NÃO":
    print("Até a próxima")
