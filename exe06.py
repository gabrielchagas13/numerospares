#Exercício (6)
#Use a estrutura de loop for para que o programa retorne todos números pares de 0 até um número especificado por terminal

numero = int(input("Coloque um numero -> "))

for x in range(0, numero+1):
    if x % 2 == 0:
        print (x)
        