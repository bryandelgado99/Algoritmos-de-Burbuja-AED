'''Este algoritmo permite ordenar arreglos basicos por medio del método de la Burbuja'''

#Definimos funcion para imprimir arreglos
def imprimir_arreglos(arreglo):
  for i in range(len(arreglo) - 1 ):  #Se puede utilizar son -1, el efecto es el mismo
    print(f'[{arreglo[i]}]', end = "")

#Definimos funcion para ordenar, por Burbuja, los elementos de la lista
def algoritmo_burbuja(arreglo):
  for i in range(len(arreglo) - 1 ):
    for j in range(len(arreglo)-1-i):
      if arreglo[j] > arreglo[j+1]:
        aux = arreglo[j]
        arreglo[j] = arreglo[j+1]
        arreglo[j+1] = aux


#Definimos el arreglo ejemplo
lista_sueldos = [20.8, 150.5, 170.5, 180.8, 190, 30, 75.6, 200]

#Imprimimos el algoritmo original
print("\nAlgoritmo Original:")
imprimir_arreglos(lista_sueldos)

#Pasamos el algoritmo
algoritmo_burbuja(lista_sueldos)

#Imprimimos el arreglo ordenado por burbuja
print("\n\nAlgoritmo Arreglado por Burbuja:")
imprimir_arreglos(lista_sueldos)
