#Solicita al usuario que ingrese 3 números
a = float(input("Ingresa el primero número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

#Encontrar el número más grande con la función max()
max_num = max(a, b, c)

#Mostrar el número más grande
print("El número más grande es: ", max_num)