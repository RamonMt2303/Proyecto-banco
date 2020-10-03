#Variables globales
saldo = 0
retiro = 0
deposito = 0
#Declaramos funciones
def saldo_cuenta (ahorro,retiro):
    saldo = ahorro - retiro
    return saldo
def fun_deposito ():
    deposito = float(input("Ingrese la cantidad a depositar:\n\t"))
    while deposito <= 0:
        print("Eso no es un numero valido")
        deposito = float(input("Ingrese una cantidad valida\n"))
                         
    print("Usted está a punto de depositar:",deposito,"¿Es correcto?\n")
    confirmacion = int(input("Ingrese 1 si desea continuar o 0 si desea cancelar\n\t"))

    if confirmacion == 0:
        print ("Cancelando transacción")
    else:
        saldo = 0
        saldo = saldo + deposito
        print ("Su saldo actual es de:\t" "%.3f" % saldo, "pesos mexicanos\n")
    return deposito,saldo

#Este va a ser la interfaz de el programa
print ("Bienvenido a MazeBank\n")
confirmacion_menu = int(input ("¿Desea hacer un depósito? 1 para continuar ó 0 para cancelar\n\t"))
if confirmacion_menu == 0:
    print ("Gracias por usar nuestro servicio bancario, vuelva pronto")
else:
    while confirmacion_menu != 4:
        print ("Bienvenido usuario\n")
        print ("........Accediendo al sistema.........\n")
        if confirmacion_menu == 1:
            deposito = float(input("Ingrese la cantidad a depositar:\n\t"))

            while deposito <= 0:
                print("Eso no es un número válido")
                deposito = float(input("Ingrese una cantidad válida:\n"))
                
            print("........Accediendo al sistema.........\n")

            print("Usted está a punto de depositar:",deposito,"¿Es correcto?\n")
            confirmacion = int(input("Ingrese 1 si desea continuar o 0 si desea cancelar\n\t"))

            if confirmacion == 0:
                print ("Cancelando transacción")
            else:
                saldo = saldo + deposito
                print ("Su saldo actual es de:\t" "%.3f" % saldo, "pesos mexicanos\n")

            ahorro = saldo
                                
            confirmacion_menu = int(input (" ¿Desea hacer un retiro? 2 para realizarlo, 3 para ver su estado de cuenta ó 4 para salir\n\t"))
        elif confirmacion_menu == 2:
            print ("¿Desea hacer algún retiro?\n")
            confirmacion_retiro = int(input("Ingrese 1 si desea continuar ó 0 si desea cancelar\n\t"))
            if confirmacion_retiro == 0:
                print ("Cancelando transacción\n")
            elif confirmacion_retiro == 1:
                print ("........Accediendo al sistema.........\n")
                retiro = float(input("Ingrese el monto a retirar\n\t"))
                while retiro > ahorro:
                    print("Porfavor intente otra cantidad\n")
                    retiro = float(input("Ingrese el monto a retirar\n\t"))
                print ("Tu saldo actual es de:" "%.3f" % saldo_cuenta(ahorro,retiro), "pesos mexicanos\n")
            confirmacion_menu = int(input("¿Desea hacer otra operación?, 1 para realizar un depósito, 2 para realizar un retiro, 3 para ver su estado de cuenta ó 4 para salir\n\t"))
        elif confirmacion_menu == 3:
            nombre = str(input("Ingrese su nombre para buscar su estado de cuenta en nuestra base de datos\n\t"))
            usuario1 = nombre
            estados_de_cuenta = {"usuario1":
                        ["Netflix: - 300 pesos", "Compras online: - 1500 pesos",
                        "Sueldo: + 15,000 pesos", "Retiro:", retiro, "Depósito:", deposito,  "Otros gastos: - 750 pesos"],
                        "usuario2":
                        ["Computadora: - 15,000 pesos", "Renta casa: - 2300 pesos",
                        "Gastos médicos: + 4000 pesos", "Otros gastos: + 7000 pesos",
                        "Sueldo: + 30,000 pesos", ]}
            print(estados_de_cuenta["usuario1"])
            confirmacion_menu = int(input("¿Desea hacer otra operación?, 1 para realizar un depósito, 2 para realizar un retiro, 3 para ver su estado de cuenta ó 4 para salir\n\t"))
        elif confirmacion_menu ==4:
            print("Gracias por usar nuestro servicio bancario, vuelva pronto")
        
