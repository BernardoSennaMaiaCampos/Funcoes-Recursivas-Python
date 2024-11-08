#Crie um programa em python, que contenha uma função recursiva que receba dois inteiros positivos k e n e calcule k^n . Utilize apenas multiplicações. O programa principal deve solicitar ao usuário os valores de k e n e imprimir o resultado da chamada da função. 

def potenciakn(k, n): 
	
 if n == 0:
        return 1
 return k * potenciakn(k, n - 1)    

k = int(input("Digite um numero: "))
n = int(input("Digite um numero: ")) 
print(potenciakn(k,n))