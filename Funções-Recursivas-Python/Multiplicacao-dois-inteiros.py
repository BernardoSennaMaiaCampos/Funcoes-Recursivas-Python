#A multiplicação de dois números inteiros pode ser feita através de somas sucessivas. Proponha um algoritmo recursivo Multip_Rec(n1,n2) que calcule a multiplicação de dois inteiros. 

def Multip_Rec(n1, n2):
    return 0 if n2 == 0 else n1 + Multip_Rec(n1, n2 - 1)

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
print(Multip_Rec(n1, n2))
