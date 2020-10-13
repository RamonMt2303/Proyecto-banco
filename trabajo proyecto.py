#Variables globales
saldo= []
deposito = 0
retiro = 0
#Declaramos funciones
def saldo_cuenta_retiro (saldo, retiro):
    saldo = 0
    saldo = saldo - retiro
    

def saldo_cuenta_deposito (saldo, deposito):
    saldo = 0
    saldo_nuevo = saldo + deposito
    

def funcion_deposito (deposito):
    confirmacion = 0
    confirmacion = int(input("Ingrese 1 si desea continuar o 0 si desea cancelar\n\t"))
    if confirmacion == 0:
        print("Cancelando transacción\n\t")
        return saldo
    elif confirmacion == 1:
        while deposito <= 0:
            print("Eso no es un número válido")
            deposito = float(input("Ingrese una cantidad válida:\n"))
        print("Usted está a punto de depositar:",deposito,"¿Es correcto?\n")
        confirmacion = int(input("Ingrese 1 si desea continuar o 0 si desea cancelar\n\t"))
        if confirmacion == 0:
            return saldo
            print ("Cancelando transacción")
        else:
            saldo_cuenta_deposito(saldo, deposito)
            print ("Su saldo actual es de:\t" "%.3f" % saldo_cuenta_deposito (saldo, deposito), "pesos mexicanos\n")
        return deposito

def funcion_retiro (): 
    retiro = float(input("Ingrese la cantidad a retirar"))
    if retiro > saldo:
        print("Porfavor intente otra cantidad\n")
        retiro = float(input("Ingrese el monto a retirar\n\t"))
    else:
        print ("Usted está a punto de retirar:", retiro, "¿Es correcto?\n")
    confirmacion_retiro = int(input("Ingrese 1 si desea continuar ó 0 si desea cancelar\n\t"))
    if confirmacion_retiro == 0:
        print ("Cancelando transacción\n")
    elif confirmacion_retiro == 1:
        saldo_cuenta_retiro (saldo,retiro)
        print ("Tu saldo actual es de:" "%.3f" % saldo_cuenta(saldo,retiro), "pesos mexicanos\n")
    return retiro, saldo

def opcion_menu(confirmacion_menu):
    while confirmacion_menu != 4:
        print ("Bienvenido usuario\n")
        print ("........Accediendo al sistema.........\n")
        if confirmacion_menu == 1:
            deposito = float(input("Ingrese la cantidad a depositar:\n\t"))
            funcion_deposito (deposito)
            confirmacion_menu = int(input ("¿Qué desea hacer?, 1 para realizar un depósito, 2 para realizar un retiro, 3 para ver su estado de cuenta ó 4 para salir\n\t"))
        elif confirmacion_menu == 2:
            retiro = funcion_retiro()
            confirmacion_menu = int(input ("¿Qué desea hacer?, 1 para realizar un depósito, 2 para realizar un retiro, 3 para ver su estado de cuenta ó 4 para salir\n\t"))
        elif confirmacion_menu == 3:
            nombre = str(input("Ingrese su nombre para buscar su estado de cuenta en nuestra base de datos\n\t"))
            usuario1 = nombre
            estado_cuenta = ["usuario1"]
            #for valor in estado_cuenta:
                #estado_cuenta [1] = estado_cuenta [1] + valor
            estados_de_cuenta = {"usuario1":
                        ["Netflix: - 300 pesos", "Compras online: - 1500 pesos",
                        "Sueldo: + 15,000 pesos", "Retiro:", retiro, "Depósito:", deposito,  "Otros gastos: - 750 pesos"],
                        "usuario2":
                        ["Computadora: - 15,000 pesos", "Renta casa: - 2300 pesos",
                        "Gastos médicos: + 4000 pesos", "Otros gastos: + 7000 pesos",
                        "Sueldo: + 30,000 pesos" ]}
            print(estados_de_cuenta["usuario1"])
            confirmacion_menu = int(input ("¿Qué desea hacer?, 1 para realizar un depósito, 2 para realizar un retiro, 3 para ver su estado de cuenta ó 4 para salir\n\t"))
        elif confirmacion_menu == 4:
            print("Gracias por usar nuestro servicio bancario, vuelva pronto")
        print("Gracias por usar nuestro servicio bancario, vuelva pronto")
        

#Este va a ser la interfaz de el programa
print ("Bienvenido a MazeBank\n")
confirmacion_menu = int(input ("¿Qué desea hacer?, 1 para realizar un depósito, 2 para realizar un retiro, 3 para ver su estado de cuenta ó 4 para salir\n\t"))
if confirmacion_menu == 4:
    print ("Gracias por usar nuestro servicio bancario, vuelva pronto")
else:
    opcion_menu(confirmacion_menu)
