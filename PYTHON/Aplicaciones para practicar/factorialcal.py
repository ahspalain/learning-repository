def calculofactorial(num):
    factorial = 1
    for i in range(2, num+1):
        factorial *= i
    return factorial

numero_a_calcular = int(input("Ingrese un numero que desee hallar su factorial: "))
print(calculofactorial(numero_a_calcular))




#UNICAMENTE PARA NUMEROS PEQUEÑOS PORQUE CONSUME MuchO ESPACIO EN LA MEMORIA

def factorial(n):
   if n==0 or n==1:
            resultado=1
   elif n>1:
            resultado=n*factorial(n-1)
   return resultado

#CALCULAMOS EL FACTORIAL DE 5.
fact5=factorial(5)

#VISUALIZAMOS RESULTADO.
print(fact5)