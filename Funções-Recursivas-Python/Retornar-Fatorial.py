#Faça uma função recursiva que calcule e retorne o fatorial de um número inteiro N.  

def fatorial_recursivo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial_recursivo(n - 1)

def fatorial(nf):
    if nf < 0:
        return "O fatorial nao é definido para números negativos."
    elif nf == 0 or nf == 1:
        return 1
    else:
        return fatorial_recursivo(nf)
nf = 5
print(fatorial(nf))
