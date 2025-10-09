saldo = 1000

value = True

while value :
    
    try:
        print()
        print("ELIJA UNA DE LAS SIGUIENTES OPCIONES")
        print("====================================")
        print("1)  Consultar saldo")
        print("2)  Depositar dinero")
        print("3)  Retirar dinero")
        print("4)  salir")
        print()
        ingreso = int(input("Elija una de las opciones: "))
        print()
        
    except:
        print("La opcion ingresada no es valida\n")
        continue 
    
    if ingreso in range(1,5) :

        
        if 1 == ingreso:
            print(f"El saldo disponible es ${saldo}\n")
            
        elif 2 == ingreso:
            try:
                saldo += int(input("Ingrese el monto a depositar: "))
                print()
            except:
                print("El valor ingresado no es valido\n")
            
        elif 3 == ingreso:
            try:
                retiro = int(input("Ingrese el monto a retirar: "))
                if retiro > saldo:
                    print()
                    print("No dispone de saldo suficiente\n")
                else:
                    saldo -= retiro
            except:
                print()
                print("LA OPCION INGRESADA NO ES VALIDA ")
            
        else:
            value = False
        
    else:
        print("LA OPCION INGRESADA NO ES VALIDA")
        print()
        
        
        


