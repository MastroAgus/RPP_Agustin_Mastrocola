def inicializar_matriz (filas:int, columnas:int, iniciar: any = 0) -> list:

    matriz = []

    for i in range (filas):

        aux = [iniciar] * columnas
        matriz += [aux]

    return matriz 


def totales (matriz: list) -> list: 

    retorno = [0] * len(matriz)

    for i in range (len(matriz)):
        acumulador = 0
        for j in range (len (matriz[i])):
            acumulador += matriz[i][j]
            
            retorno[i] = acumulador
            
    
    return retorno 
 

def retornar_ventas (matriz: list, valor: int = 100) -> list:

    retorno = [0] * (len(matriz))

    for i in range (len(matriz)):

        recaudacion_total = 0

        for j in range (len(matriz[i])):

            recaudacion_total += matriz [i][j] * valor

            retorno [i] = recaudacion_total

    return retorno   

    
            
    
     