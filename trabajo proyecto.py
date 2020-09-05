#Proyecto github

print ("Bienvenido usuario")
#Este va a ser la interfaz de el programa
print ("¿Cuánto dinero desea ingresar?")
ahorro = 0
#Esto lo metí porque quiero meter la opción de si/no pero no me salió al momento de realizar esta entrega, asi que no los usaré esta priemra entrega
si = 1
no = 0
deposito = int(input("Ingrese el monto a depositar en números enteros y sin decimales"))
while deposito <= 0:
    print("Eso no es un número válido")
    
    deposito = int(input("Ingrese un número entero y sin decimales válido"))
    if deposito == 0:
        print("Usted escribió 0, eso no es un número válido")
        deposito = int(input("Ingrese un número entero y sin decimales válido"))
           
print("Accediendo al sistema")

print("Usted está a punto de depositar:",deposito,"¿es correcto?")
confirmacion = int(input("Ingrese 0 si desea cancelarlo, o 1 si desea continuar"))
#def confirmacion (1, 0):
if confirmacion == 0:
    print ("Cancelando transacción")
else:
    print ("Accediendo al sistema")
    sum = ahorro + deposito
    saldo = sum
    print ("Su saldo actual es de:",saldo)
print("Gracias por usar nuestro servicio bancario, vuelva pronto")



