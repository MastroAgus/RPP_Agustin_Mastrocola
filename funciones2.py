from funciones import inicializar_matriz

def media_geometrica (matriz: list) -> list:

    n = len(matriz)

    retorno = []

    

    for fila in matriz: 
        producto = 1
        for elemento in fila: 
            producto *= elemento 
        
        media_geo = producto ** (1 / len(fila) )

        retorno.append(media_geo)

    return retorno
    
   



def suma_diagonales (matriz: list, opcion: bool) -> list:

    diagonal_1 = 0
    diagonal_2 = 0
    n = (len (matriz)) 

    if opcion == "si":

        for i in range (n):

            diagonal_1 += matriz [i][i]
            diagonal_2 += matriz [i][n - i - 1]
    
        retorno = diagonal_1 + diagonal_2

        return retorno

    elif opcion == "no":

        print ("1) diagonal principal") 
        print ("2) diagonal secundaria")

        seleccion = input ("diagonal principal o secundaria ?")

        match seleccion:

            case "1":
                for i in range (n):
                    diagonal_1 += matriz [i][i]
                return diagonal_1

            case "2":
                for i in range (n):
                    diagonal_2 += matriz [i][n - i - 1]
                return diagonal_2 
            
            case _:
                print ("esa opcion no existe")






def transponer_matriz (matriz: list) -> list: 

    filas = len (matriz)
    columnas = len (matriz [0])

    matriz_t = inicializar_matriz (filas, columnas)

    for i in range (filas):
        for j in range (columnas):
            matriz_t [j][i] = matriz [i][j]

    return matriz_t  