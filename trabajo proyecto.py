#Proyecto github

#Funciones
def saldo_cuenta (ahorro, retiro):
    saldo = ahorro - retiro
    return saldo

#Variables globales
saldo = 0
retiro = 0

print ("Bienvenido a MazeBank\n")
print ("Bienvenido usuario\n")
#Este va a ser la interfaz de el programa
confirmacion_menu = int(input ("¿Desea hacer un depósito? ----- Ingrese 1 para acceder al sistema, o 0 para salir"))
if confirmacion_menu == 1:
    print(".........Accediendo al sistema.........")

    print ("¿Cuánto dinero desea depositar a su cuenta?")

    deposito = float(input("Ingrese la cantidad a depositar:\n"))

    while deposito <= 0:
        print("Eso no es un número válido")
        deposito = float(input("Ingrese una cantidad válida:\n"))
      
    print(".........Accediendo al sistema.........")

    print("Usted está a punto de depositar:\t",deposito,"\n¿Es correcto?")
    confirmacion = int(input("Ingrese 1 si desea continuar o 0 si desea cancelar\n"))

    if confirmacion == 0:
        print ("Cancelando transacción")
    else:
        saldo = saldo + deposito
        print ("Su saldo actual es de:\t",saldo, "de dólares")

    ahorro = saldo

    print ("¿Desea hacer algún retiro?")
    confirmacion_retiro = int(input("Ingrese 1 si desea continuar o 0 si desea cancelar\n"))
    if confirmacion_retiro == 0:
        print ("Cancelando transacción")
    elif confirmacion_retiro == 1:
        print ("Accediendo al sistema")
        retiro = float(input("Ingrese el monto a retirar"))
        while retiro > ahorro:
            print("Porfavor intente otra cantidad")
            retiro = float(input("Ingrese el monto a retirar"))
        print ("Tu saldo actual es de:\t",saldo_cuenta(ahorro,retiro), "dólares")
else:
    
    print("Gracias por usar nuestro servicio bancario, vuelva pronto")



