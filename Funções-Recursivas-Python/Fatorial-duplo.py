#A função fatorial duplo é definida como o produto de todos os números naturais ímpares de 1 até algum número natural ímpar N. Assim, o fatorial duplo de 5 é 5!! = 1 * 3 * 5 = 15 Faça uma função recursiva que receba um número inteiro positivo impar N e retorne o fatorial duplo desse número.

def fatorial_duplo(n):
    return 1 if n == 1 else n * fatorial_duplo(n - 2)

N = int(input("Digite um número ímpar positivo: "))
if N % 2 == 1: print(fatorial_duplo(N))
else: print("Digite um número ímpar.")
