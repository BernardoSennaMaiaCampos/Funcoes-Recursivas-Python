#Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente. 

def imprimir_decrescente(n):
    print(n)
    n > 0 and imprimir_decrescente(n - 1)

N = int(input("Digite um número inteiro positivo: "))
imprimir_decrescente(N)
