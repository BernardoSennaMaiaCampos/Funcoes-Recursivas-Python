#O máximo divisor comum dos inteiros x e y é o maior inteiro que é divisível por x e y. Escreva uma função recursiva mdc em python, que retorna o máximo divisor comum de x e y. O mdc de x e y é definido como segue: se y é igual a 0, então mdc(x,y) é x; caso contrário, mdc(x,y) é mdc (y, x%y), onde % é o operador resto. 

x = int(input("Digite o numero X: "))
y = int(input("Digite o numero y: "))

def mdc(x, y):
    return x if not y else mdc(y, x % y)
print(mdc(x,y))
