from funciones2 import *

matriz = [[1,2,3], [4,5,6], [7,8,9]]

media_geo = media_geometrica(matriz)

print (f"media geo = {media_geo}")


matriz2 = [[1,2,3], [4,5,6], [7,8,9]]

opcion = str(input ("quieres ambas diagonales (si o no): "))

diagonales = suma_diagonales(matriz2, opcion)

print (f"diagonales = {diagonales}")


transpuesta = transponer_matriz (matriz2)

print (f"transpuesta = {transpuesta}")