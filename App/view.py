"""""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """
 
import config as cf
import sys
import controller
import threading
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
assert cf
 
servicefile_landing = 'landing_points.csv'
servicefile_connections = 'connections.csv'
servicefile_countries = 'countries.csv'
initialStation = None
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
 
def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información")
    print("3- Calcular la cantidad de clústeres: ")
    print("4- Se desea encontrar el (los) landing point(s):")
    print("5- Encontrar la ruta mínima entre dos paices: ")
    print("6- identificar la infraestructura crítica: ")
    print("7- Conocer el impacto que tendría el fallo de un determinado landing point: ")
    print("8- Conocer el ancho de banda máximo:")
    print("9- Encontrar la ruta mínima en número de saltos:")
    print("0- Salir")
    print("*******************************************")
 
catalog = None
 
"""
Menu principal
"""
def thread_cycle():
    while True:
        printMenu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs[0]) == 1:
            print("Cargando información de los archivos ....")
            cont = controller.init()
        elif int(inputs[0]) == 2:
            print("\nInicializando....")
            controller.loadServices(cont)          
 
        elif int(inputs[0]) == 3:                      #req 1
            landing_1= input("Nombre del landing point 1 (Ejem. Redondo Beach- 4992):")
            landing_2= input("Nombre del landing point 2 (Ejem. Vung Tau-6013):")
            clusteres = controller.connectedComponents(cont)
            landing_pints = controller.estan_closter(cont,landing_1,landing_2)
            print("")
            print("Número total de clústeres presentes en la red: " + str(clusteres))
            if landing_pints:
                print("Los dos landing points están en el mismo clúster")  
            else:
                print(" los dos landing points NO están en el mismo clúster")
            
        elif int(inputs[0]) == 4:                      #req 2
            max_edge=controller.servedRoutes(cont)
            print("El total de cables conectados a dichos landiing points son:")
            print(max_edge[0])
            print("lista de landing points")
            print(max_edge[1])
 
        elif int(inputs[0]) == 5:                      #req 3
            Pais_1 = " " + input("Primer país eje: Colombia - 4315 : ")
            Pais_2 = " " + input("Segundo país eje: Indonesia - 16660 : ")
            controller.minimumCostPaths(cont, Pais_1)
            camino = controller.camino(cont,Pais_2)
            iterador = it.newIterator(camino)
            print("Camino del primer pais al segundo pais:")
            while it.hasNext(iterador):
                elemento = it.next(iterador)
                print(elemento)
            distancia = controller.distancia_total(cont,Pais_2)
            print("-------------------------------------------------------")
            print("La distancia total entre los dos landing points es:")
            print(distancia)
 
            
        elif int(inputs[0]) == 6:                      #req 4
            rta=controller.infraestructura_critica(cont)
            print("")
            print("El número de nodos conectados a la red de expansión mínima es: " + str(rta[0]))
            print("El costo total (distancia en [km]) de la red de expansión mínima es: " + str(rta[1]) + " Km")
            print("La rama más larga que hace parte de la red de expansión mínima es: " + str(rta[2]))
            print("")

            
            
        elif int(inputs[0]) == 7:                      #req 5
            landing = input("Nombre del landing point (Ejem. Fortaleza):")
            rta=controller.inpacto_landing(cont, landing)
            print("")
            print("EL número de paises es: " + str(rta[0]))
            print("Los paises son: ")
            print("")
            iterador = it.newIterator(rta[1])
            while it.hasNext(iterador):
                Pais = str(it.next(iterador))
                print(Pais)
            print("")
        elif int(inputs[0]) == 8:                     #req 6
            pais = input("Nombre del país: ")
            cable = input("Nombre del cable: ")
            rta =controller.ancho_de_banda(cont, pais, cable)
            print(rta)
        elif int(inputs[0]) == 9:                     #req 7                     
            ruta_1 = input("Ingrese la Dirección IP1 (Ejem. 165.132.67.89 ): ")
            ruta_2 = input("Ingrese la Dirección IP2 (Ejem. 8.8.8.8): ")
            rta =controller.saltos_minimos(cont, ruta_1, ruta_2)
            print(rta) 
        else:
            sys.exit(0)
    sys.exit(0)
 
if __name__ == "__main__":
    print(sys.getrecursionlimit())
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=thread_cycle)
    thread.start()

