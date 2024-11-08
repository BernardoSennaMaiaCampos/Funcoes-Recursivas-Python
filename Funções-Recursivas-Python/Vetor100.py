#Crie um programa em python que receba um vetor de números reais com 100 elementos. Escreva uma função recursiva que inverta ordem dos elementos presentes no vetor. 

def inverter_vetor(vetor):
    if not vetor: return vetor
    return inverter_vetor(vetor[1:]) + [vetor[0]]

vetor = [i * 1 for i in range(1, 101)]
print(vetor)
print(inverter_vetor(vetor))
