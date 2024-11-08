# Faça uma função recursiva que permita inverter um número inteiro N. Ex: 123 - 321 

def inverter_numero(n):
    
    n_str = str(n)
    n_invertido = list(n_str)
    n_invertido.reverse()
    
    return int("".join(n_invertido))

n = 123
print(n)
print(inverter_numero(n)) 
