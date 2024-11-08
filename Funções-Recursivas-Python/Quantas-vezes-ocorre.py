#Escreva uma função recursiva que determine quantas vezes um dígito K ocorre em um número natural N. Por exemplo, o dígito 2 ocorre 3 vezes em 762021192. 

def contar_digito(N, K):
    return (N % 10 == K) + (contar_digito(N // 10, K) if N else 0)

N = int(input("Digite o numero: "))
K = int(input("Digite o numero que deseja contar quantas vezes se repete: "))
print(contar_digito(N, K))
