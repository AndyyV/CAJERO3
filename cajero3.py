saldo=550
contraseña=1234 
while True:
    U=input("Ingrese su Usuario: ") 
    if U==("ADMIN"):     
        while True:
            C=int(input("Escriba su Contraseña: "))
            if C==contraseña:
                print("*****")
                print("MENU")
                print("*****")
                print("1. RETIRAR")
                print("2. DEPOSITAR")
                print("3. REALIZAR TRANSFERENCIA")
                print("4. ESTADO DE CUENTA")
                print("5. SALIR")
                while True: 
                    O=int(input("Seleccione una Opcion: "))
                    if O==1:
                        print("*****")
                        print("MENU")
                        print("*****")
                        print("1. Q100")
                        print("2. Q300")
                        print("3. Q500")
                        print("4. Q1000")
                        print("5. SALIR")
                        K=int(input("SELECCIONAR CANTIDAD: "))
                        print("Retiro Realizado")
                        if K==1:
                            saldo=saldo-100
                        elif K==2:
                            saldo=saldo-300
                        elif K==3:
                            saldo=saldo-500
                        elif K==4:
                            saldo=saldo-1000
                        else:
                            print("Opcion Incorrecta")
                    elif O==4:
                        print("Su Saldo Disponible es de: "+str(saldo))
                        break;       
                    elif O==2:
                        print("*****")
                        print("MENU")
                        print("*****")
                        print("1. Q100")
                        print("2. Q300")
                        print("3. Q500")
                        print("4. Q1000")
                        print("5. SALIR")
                        D=int(input("SELECCIONE UNA CANTIDAD: "))
                        print("Deposito Realizado")
                        if D==1:
                            saldo=saldo+100
                        elif D==2:
                            saldo=saldo+300
                        elif D==3:
                            saldo=saldo+500
                        elif D==4:
                            saldo=saldo+1000   
                        else:
                            print("Opcion Incorrecta")
                            break;
                    elif O==3:
                        
                        D=int(input("SELECCIONE UNA CANTIDAD: "))
                        print("Transferencia Realizada")
                    elif O==4:
                        print("Su Saldo Disponible es de: "+str(saldo))
                        break;
            else:
                print("Contraseña Incorrecta")
    else:
        print("Usuario Incorrecto")