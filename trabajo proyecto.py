from colorama import Fore
"""
Colorama es una biblioteca que nos ayuda a darle color al texto,
de igual forma se le puede agregar fondo de color
"""
#Variables globales
deposito = 0
retiro = 0

#Declaramos funciones
"""
Esta función lo que hace es que me regresa el saldo después de realizar un depósito,
para que no se sobreescriba el saldo en 0
"""
def cambiar_deposito(dinero, saldo):
    saldo += dinero
    print (Fore.GREEN + "Su saldo actual es de:\t" "%.2f" % saldo, "pesos mexicanos\n")
    return saldo

"""
Esta función lo que hace es que me regresa el saldo después de realizar un retiro,
para que no se sobreescriba el saldo en 0
"""
def cambiar_retiro(dinero, saldo):
    saldo -= dinero
    print (Fore.RED + "Su saldo actual es de:\t" "%.2f" % saldo, "pesos mexicanos\n")
    return saldo

"""
Esta función sirve para poder realizar un depósito,
le pide al usuario un monto a depositar, y se lo agrega al saldo
"""
def funcion_deposito ():
    deposito = float(input(Fore.GREEN + "Ingrese la cantidad a depositar\n\t"))
    while deposito <= 0:
        print("Eso no es un número válido")
        deposito = float(input(Fore.GREEN + "Ingrese una cantidad válida:\n"))
    print(Fore.BLACK + "Usted está a punto de depositar:",deposito,"¿Es correcto?\n")
    confirmacion_deposito = int(input(Fore.BLACK + "Ingrese 1 si desea continuar o 0 si desea cancelar\n\t"))
    if confirmacion_deposito == 0:
        print (Fore.BLACK + "Cancelando transacción\n")
        return 0
    else:
        return deposito       

"""
Esta función sirve para poder realizar un retiro,
le pide al usuario un monto a retirar, y se lo resta al saldo
"""
def funcion_retiro (saldo): 
    retiro = float(input(Fore.RED + "Ingrese la cantidad a retirar\n\t"))
    if retiro > saldo:
        print("Porfavor intente otra cantidad\n\t")
        retiro = float(input(Fore.RED + "Ingrese el monto a retirar\n\t"))
    else:
        print (Fore.BLACK + "Usted está a punto de retirar:", retiro, "¿Es correcto?\n")
    confirmacion_retiro = int(input(Fore.BLACK + "Ingrese 1 si desea continuar ó 0 si desea cancelar\n\t"))
    if confirmacion_retiro == 0:
        print (Fore.BLACK + "Cancelando transacción\n")
        return 0
    elif confirmacion_retiro == 1:
        return retiro

"""
Con esta función, el usuario puede agregar transacciones a su estado de cuenta,
primero tiene que registrar su usuario, para después agregar transacciones,
como lo sería el concepto,cantidad y monto, para después acceder.
"""
def agregar_transaccion(usuario, usuarios):
    if usuario in usuarios:      
        concepto = str(input(Fore.CYAN + "Introduce el concepto de la transacción: \t"))
        tipo = str(input(Fore.BLUE + "Que tipo dee transacción fué (retiro / deposito): \t "))
        cantidad = float(input(Fore.MAGENTA + "De cuanto fue el monto: \t" ))    
        usuarios[usuario].append([concepto, tipo, cantidad])
    else:
        usuarios[usuario] = []
        concepto = str(input(Fore.CYAN + "Introduce el concepto de la transacción: "))
        tipo = str(input(Fore.BLUE + "Que tipo dee transacción fué (retiro / deposito): "))
        cantidad = float(input(Fore.MAGENTA + "De cuanto fue el monto:" ))
        usuarios[usuario].append([concepto, tipo, cantidad])
 
"""
Una vez ingresando el nombre y transacciones, ahora si se puede acceder al historial
y ver el historial de transacciones que haya metido el usuario
"""
def revisar_historial(usuario, usuarios):
    if not usuario in usuarios:
        usuarios[usuario] = []
        print("Primero agrega transacciones para agregarte a nuestra base de datos.\n")
    for cuenta in usuarios:
        if usuario.lower() == cuenta.lower():
            if len(usuarios[cuenta]) <= 0:
                print("No tienes transacciones por el momento.\n")
            else:
                print(Fore.CYAN + "Sus transacciones son:\n")
                for transacciones in usuarios[cuenta]:
                    print(transacciones, "\n")


"""
Esta función sirve como el menú de la interfaz,
dependiendo la selección del usuario, va a mandar llamar las distintas funciones
"""
def opcion_menu(confirmacion_menu):
    saldo = 0
    usuarios = {"usuario1":[]}
    while confirmacion_menu != 5:
        print (Fore.BLACK + "Bienvenido usuario\n")
        print (Fore.GREEN + "........Accediendo al sistema.........\n")
        if confirmacion_menu == 1:
            cantidad_a_depositar = funcion_deposito()
            saldo = cambiar_deposito(cantidad_a_depositar, saldo)
            confirmacion_menu = int(input (Fore.BLUE + "¿Qué desea hacer?, 1 para realizar un depósito, \
2 para realizar un retiro, 3 para agregar una transacción, 4 para ver tu estado de cuenta ó 5 para salir\n\t"))
        elif confirmacion_menu == 2:
            cantidad_a_retirar = funcion_retiro(saldo)
            saldo = cambiar_retiro(cantidad_a_retirar, saldo)
            confirmacion_menu = int(input (Fore.BLUE + "¿Qué desea hacer?, 1 para realizar un depósito, \
2 para realizar un retiro, 3 para agregar una transacción, 4 para ver tu estado de cuenta ó 5 para salir\n\t"))
        elif confirmacion_menu == 3:
            nombre = str(input("Ingrese su nombre para añadir una transacción y guardarlo en tu historial\n\t"))       
            agregar_transaccion(nombre, usuarios)
            confirmacion_menu = int(input (Fore.BLUE + "¿Qué desea hacer?, 1 para realizar un depósito, \
2 para realizar un retiro, 3 para agregar una transacción, 4 para ver tu estado de cuenta ó 5 para salir\n\t"))
        elif confirmacion_menu == 4:
            nombre = str(input("Ingrese su nombre para buscar su historial\n\t"))
            revisar_historial(nombre, usuarios)
            
            confirmacion_menu = int(input (Fore.BLUE + "¿Qué desea hacer?, 1 para realizar un depósito, \
2 para realizar un retiro, 3 para agregar una transacción, 4 para ver tu estado de cuenta ó 5 para salir\n\t"))
        elif confirmacion_menu == 5:
            print(Fore.CYAN + "Gracias por usar nuestro servicio bancario, vuelva pronto\n")
        print(Fore.CYAN + "Gracias por usar nuestro servicio bancario, vuelva pronto\n")
        

#Este va a ser la interfaz de el menú del banco
print ("Bienvenido a MazeBank\n")
confirmacion_menu = int(input (Fore.BLUE + "¿Qué desea hacer?, 1 para realizar un depósito, \
2 para realizar un retiro, 3 para agregar una transacción, 4 para ver tu estado de cuenta ó 5 para salir\n\t"))
opcion_menu(confirmacion_menu)
print(Fore.CYAN + "Gracias por usar nuestro servicio bancario, vuelva pronto\n")
