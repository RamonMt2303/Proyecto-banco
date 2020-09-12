#Proyecto github

#Funciones
def saldo_cuenta (ahorro, retiro):
    saldo = ahorro - retiro
    return saldo

#Variables globales
saldo = 0
retiro = 0

print ("Bienvenido usuario\n")
#Este va a ser la interfaz de el programa
print ("¿Cuánto dinero desea ingresar?")

deposito = float(input("Ingrese la cantidad a depositar:\n"))

while deposito <= 0:
    print("Eso no es un número válido")
    deposito = float(input("Ingrese una cantidad válida:\n"))
  
print(".........Accediendo al sistema.........")

print("Usted está a punto de depositar:\t",deposito,"\n¿Es correcto?")
confirmacion = int(input("Ingrese 0 si desea cancelarlo o 1 si desea continuar\n"))

if confirmacion == 0:
    print ("Cancelando transacción")
else:
    saldo = saldo + deposito
    print ("Su saldo actual es de:\t",saldo, "dólares")

ahorro = saldo

print ("¿Desea hacer algún retiro?")
confirmacion_retiro = int(input("Ingrese 0 si desea cancelarlo, o 1 si desea continuar\n"))
if confirmacion_retiro == 0:
    print ("Cancelando transacción")
elif confirmacion_retiro == 1:
    print ("Accediendo al sistema")
    retiro = float(input("Ingrese el monto a retirar"))
    while retiro > ahorro:
        print("Porfavor intente otra cantidad")
        retiro = float(input("Ingrese el monto a retirar"))
    print ("Tu saldo actual es de:\t",saldo_cuenta(ahorro,retiro), "dólares")

    
print("Gracias por usar nuestro servicio bancario, vuelva pronto")



