#Proyecto github

print ("Bienvenido usuario")
#Este va a ser la interfaz de el programa
print ("¿Cuánto dinero desea ingresar?")
ahorro = 0
#Esto lo metí porque quiero meter la opción de si/no pero no me salió al momento de realizar esta entrega, asi que no los usaré esta priemra entrega
si = 'True'
no = 'False'
deposito = int(input("Ingrese el monto a depositar en números enteros y sin decimales"))
while deposito <= 0:
    print("Eso no es un número válido")
    deposito = int(input("Ingrese un número entero y sin decimales válido"))
    if deposito == 0:
        print("Usted escribió 0, eso no es un número válido")
        deposito = int(input("Ingrese un número entero y sin decimales válido"))
print("Accediendo al sistema")  
print("Usted está a punto de depositar:",deposito,"¿es correcto?")
confirmacion = input()
#Ahorita solo funciona si le pongo si, sigo aprendiendo a como poner condicional de si está mal el monto de depósito
sum = ahorro + deposito
saldo = sum
print ("Su saldo actual es de:",saldo)
print("Gracias por usar nuestro servicio bancario, vuelva pronto")



