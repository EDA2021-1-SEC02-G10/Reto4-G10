"""
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
from DISClib.Algorithms.Sorting import mergesort as merge
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
            landing_1= input("Nombre del landing point 1 (Ejem. Redondo Beach):")
            landing_2= input("Nombre del landing point 2 (Ejem. Vung Tau):")
            clusteres = controller.connectedComponents(cont)
            controller.minimumCostPaths(cont, landing_1)
            landing_pints = controller.estan_closter(cont,landing_2)
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
            Pais_1 = input("Primer país: ")
            Pais_2 = input("Segundo país: ")
            
            
        elif int(inputs[0]) == 6:                      #req 4
            rta=controller.infraestructura_critica(cont)
            
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
        else:
            sys.exit(0)
    sys.exit(0)

if __name__ == "__main__":
    print(sys.getrecursionlimit())
    threading.stack_size(67108864)  # 64MB stack
    sys.setrecursionlimit(2 ** 20)
    thread = threading.Thread(target=thread_cycle)
    thread.start()
