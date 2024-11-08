#Faça uma função recursiva que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem crescente. 

def imprimir_crescente(n):
    n > 0 and imprimir_crescente(n - 1)
    print(n)

N = int(input("Digite um número inteiro positivo: "))
imprimir_crescente(N)
