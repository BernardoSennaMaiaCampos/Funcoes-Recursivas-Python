#Faça uma função recursiva que permita somar os elementos de um vetor de inteiros. 

def soma_vetor(vetor):
    return 0 if not vetor else vetor[0] + soma_vetor(vetor[1:])

vetor = [1, 2, 3, 4, 5]
print(soma_vetor(vetor))  
