#Faça uma função recursiva que receba um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem crescente. 

def imprimir_pares(n):
    if n > 0: imprimir_pares(n - 1)
    if n % 2 == 0: print(n)

N = int(input("Digite um número inteiro positivo: "))
imprimir_pares(N)
