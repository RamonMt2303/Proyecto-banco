#Proyecto github

print ("Bienvenido usuario")
#Este va a ser la interfaz de el programa
print ("¿Cuánto dinero desea ingresar?")
saldo = 0

deposito = float(input("Ingrese la cantidad a depositar"))
while deposito <= 0:
    print("Eso no es un número válido")
    deposito = float(input("Ingrese una cantidad válida"))
  
print("Accediendo al sistema")

print("Usted está a punto de depositar:",deposito,"¿Es correcto?")
confirmacion = int(input("Ingrese 0 si desea cancelarlo, o 1 si desea continuar"))
if confirmacion == 0:
    print ("Cancelando transacción")
else:
    print ("Accediendo al sistema")
    sum = saldo + deposito
    saldo = sum
    print ("Su saldo actual es de:",saldo)
    
print("Gracias por usar nuestro servicio bancario, vuelva pronto")



