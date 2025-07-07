#Calculadora de interés simple 
#Solicitar al usuario que ingrese el monto principal, la tasa de interés y periodo de tiempo
p = float(input("Ingresa el monto a invertir: $"))
r = float(input("Ingresa la tasa de interés: "))
t = float(input("Ingresa los meses a invertir: "))

#Calculo de interes simple utilizando la fórmula: interés = (principal * tasa * tiempo) / 100
interest = (p * r * t)/100

#Mostrar interés simple calculado
print("Interés simple: ", interest)
