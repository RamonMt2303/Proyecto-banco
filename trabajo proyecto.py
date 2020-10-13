
#Variables globales
deposito = 0
retiro = 0
#Declaramos funciones
def cambiar_deposito(dinero, saldo):
    saldo += dinero
    print ("Su saldo actual es de:\t" "%.2f" % saldo, "pesos mexicanos\n")
    return saldo

def cambiar_retiro(dinero, saldo):
    saldo -= dinero
    print ("Su saldo actual es de:\t" "%.2f" % saldo, "pesos mexicanos\n")
    return saldo

def funcion_deposito ():
    deposito = float(input("Ingrese la cantidad a depositar\n\t"))
    while deposito <= 0:
        print("Eso no es un número válido")
        deposito = float(input("Ingrese una cantidad válida:\n"))
    print("Usted está a punto de depositar:",deposito,"¿Es correcto?\n")
    confirmacion_deposito = int(input("Ingrese 1 si desea continuar o 0 si desea cancelar\n\t"))
    if confirmacion_deposito == 0:
        print ("Cancelando transacción\n")
        return 0
    else:
        return deposito       


def funcion_retiro (saldo): 
    retiro = float(input("Ingrese la cantidad a retirar\n\t"))
    if retiro > saldo:
        print("Porfavor intente otra cantidad\n\t")
        retiro = float(input("Ingrese el monto a retirar\n\t"))
    else:
        print ("Usted está a punto de retirar:", retiro, "¿Es correcto?\n")
    confirmacion_retiro = int(input("Ingrese 1 si desea continuar ó 0 si desea cancelar\n\t"))
    if confirmacion_retiro == 0:
        print ("Cancelando transacción\n")
        return 0
    elif confirmacion_retiro == 1:
        return retiro


def agregar_transaccion(usuario, usuarios):
    if usuario in usuarios:
        
        concepto = str(input("Introduce el concepto de la transacción: \t"))
        tipo = str(input("Que tipo dee transacción fué (retiro / deposito): \t "))
        cantidad = float(input("De cuanto fue el monto: \t" ))
    
        usuarios[usuario].append([concepto, tipo, cantidad])
    else:
        usuarios[usuario] = []
        concepto = str(input("Introduce el concepto de la transacción: "))
        tipo = str(input("Que tipo dee transacción fué (retiro / deposito): "))
        cantidad = float(input("De cuanto fue el monto:" ))
    
        usuarios[usuario].append([concepto, tipo, cantidad])
        
def revisar_historial(usuario, usuarios):
    if not usuario in usuarios:
        usuarios[usuario] = []
    for cuenta in usuarios:
        if usuario.lower() == cuenta.lower():
            print("Sus transacciones son:")
            for transacciones in usuarios[cuenta]:
                print(transacciones)


def opcion_menu(confirmacion_menu):
    saldo = 0
    usuarios = {"usuario1":[]}
    while confirmacion_menu != 5:
        print ("Bienvenido usuario\n")
        print ("........Accediendo al sistema.........\n")
        if confirmacion_menu == 1:
            cantidad_a_depositar = funcion_deposito()
            saldo = cambiar_deposito(cantidad_a_depositar, saldo)
            confirmacion_menu = int(input ("¿Qué desea hacer?, 1 para realizar un depósito, \
2 para realizar un retiro, 3 para agregar una transacción, 4 para ver tu estado de cuenta ó 5 para salir\n\t"))
        elif confirmacion_menu == 2:
            cantidad_a_retirar = funcion_retiro(saldo)
            saldo = cambiar_retiro(cantidad_a_retirar, saldo)
            confirmacion_menu = int(input ("¿Qué desea hacer?, 1 para realizar un depósito, \
2 para realizar un retiro, 3 para agregar una transacción, 4 para ver tu estado de cuenta ó 5 para salir\n\t"))
        elif confirmacion_menu == 3:
            nombre = str(input("Ingrese su nombre para añadir una transacción y guardarlo en tu historial\n\t"))       
            agregar_transaccion(nombre, usuarios)
            confirmacion_menu = int(input ("¿Qué desea hacer?, 1 para realizar un depósito, \
2 para realizar un retiro, 3 para agregar una transacción, 4 para ver tu estado de cuenta ó 5 para salir\n\t"))
        elif confirmacion_menu == 4:
            nombre = str(input("Ingrese su nombre para buscar su historial\n\t"))
            revisar_historial(nombre, usuarios)
            
            confirmacion_menu = int(input ("¿Qué desea hacer?, 1 para realizar un depósito, \
2 para realizar un retiro, 3 para agregar una transacción, 4 para ver tu estado de cuenta ó 5 para salir\n\t"))
        elif confirmacion_menu == 5:
            print("Gracias por usar nuestro servicio bancario, vuelva pronto")
        print("Gracias por usar nuestro servicio bancario, vuelva pronto")
        

#Este va a ser la interfaz de el programa
print ("Bienvenido a MazeBank\n")
confirmacion_menu = int(input ("¿Qué desea hacer?, 1 para realizar un depósito, \
2 para realizar un retiro, 3 para agregar una transacción, 4 para ver tu estado de cuenta ó 5 para salir\n\t"))

if confirmacion_menu == 5:
    print ("Gracias por usar nuestro servicio bancario, vuelva pronto")
else:
    opcion_menu(confirmacion_menu)

