from funciones import *

depositos = ["tierra_del_fuego","tucuman","mendoza","Bs As", "misiones", "santa_fe" ]
equipos = ["Barcelona", "Inter_Miami", "PSG", "Manchester_City", "Real_madrid"]

continuar = True
carga_1 = True
carga_5 = True

matriz = [[222, 32, 4, 42, 53], [5342, 65, 10000, 2, 321], [312, 56, 24, 123, 125], [226, 21, 67, 12, 54], [2, 1, 5, 6, 7],
          [100, 50, 25, 5, 2]]

lista_ventas =  [[222, 32, 4, 42, 53], [5342, 65, 10000, 2, 321], [312, 56, 24, 123, 125], [226, 21, 67, 12, 54], [2, 1, 5, 6, 7],
          [100, 50, 25, 5, 2]]


while continuar == True:

    print ("=============================================================================================")
    print ("Seleccione una opcion: ")
    print ("1: obtener existencias: ")
    print ("2: Mostrar depósitos que tienen en stock más de 10.000 camisetas.")
    print ("3: Mostrar equipos que hay en stock más de 5.000 camisetas.")
    print ("4: Obtener cantidad maxima de camisetas: ")
    print ("5: Cargar ventas: ")







    print ("6: salir")
    print ("=============================================================================================")

    opcion = int (input ("Ingrese la opcion que desea realizar: "))

    match opcion:
        case 1:
            if carga_1 == False:
                matriz = inicializar_matriz (len(depositos),len(equipos),0)
            
                for i in range (len(depositos)):
                    for j in range (len(equipos)):

                        aux_1 = int (input(f"ingrese cantidad de camisetas {equipos[j]} en {depositos[i]}: "))

                        matriz[i][j] = aux_1

                        print (matriz)

                        carga = True
            
            elif carga_1 == True:

                for i in range (len(depositos)):
                    for j in range (len(equipos)):

                        print (f"en {depositos[i]} hay {matriz[i][j]} {equipos[j]}")
        

        case 2:
            lista_totales = totales(matriz)
            stock = 10000
            print (lista_totales)

            for i in range (len(lista_totales)):
                if lista_totales[i] > stock:
                    print ("-------------------------------------------------------------")
                    print (f"el deposito de {depositos [i]} supero los stock de {stock}")
                    print ("-------------------------------------------------------------")
                
                else:
                    print (f"el deposito de {depositos [i]} no supero el stock")
        
        case 3:
            print ("no la entendi")
        

        case 4: 
            for i in range (len(equipos)):
                
                bandera = False

                for j in range (len(depositos)):
                    if bandera == False:
                        maximo = matriz [j][i]
                        deposito = depositos[j]
                        bandera = True
                    
                    elif matriz [j][i] > maximo:
                        maximo = matriz [j][i]
                        deposito = depositos[j]

                print (f"el deposito con mas {equipos[i]} es {deposito}")
        
        case 5:

            if carga_5 == False:
                lista_ventas = inicializar_matriz (len(depositos),len(equipos),0) 

            while carga_5 == False:
                
            
                i5 = int(input("seleccione un deposito del 0 al 5: "))
                j5 = int (input ("seleccione un equipo del 0 al 4: "))

                aux_5 = int (input (f"ventas de {equipos[j5]} en deposito de {depositos[i5]}: "))

                lista_ventas[i5][j5] = aux_5

                print (lista_ventas)

                seguir = input ("seguir cargando lista (si o no): ")
                if seguir == ("no"):
                    carga_5 = True
        
            if carga_5 == True:
                ventas = retornar_ventas (lista_ventas)

                print (ventas)

                for i in range (len (lista_ventas)):
                    
                    print (f"en el deposito {depositos [i]} se recaudo un total de {ventas[i]}") 


                        




            



    
        case 6:
            print ("usted ha salido del programa")
            continuar = False
    
    