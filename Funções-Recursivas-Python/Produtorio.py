#Crie uma função recursiva que receba um número inteiro positivo N e calcule o produtório dos números de 1 a N. 

def produtorio(N):
    return 1 if N == 1 else N * produtorio(N - 1)
N = int(input("Digite um número N: "))
print(produtorio(N))
