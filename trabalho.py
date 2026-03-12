import random

print("jogo par ou impar")

def verificar(numero):
    if numero % 2 == 0:
        return "PAR"
    else:
        return "ÍMPAR"

#int é uma função built-in que serve para deixar o numero em inteiro
jogador = int(input("Escolha um número:"))

#randining serve para nao deixar o numero vir enteiro 
oponente = random.randint(1,10)

soma = jogador + oponente

print("Você jogou:", jogador)
print("oponente jogou:", oponente)
print("Soma:", soma)

resultado = verificar(soma)

print("Resultado:", resultado)

print("Maior número jogado:", max(jogador, oponente))
print("Valor final:", abs(soma))