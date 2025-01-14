﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
from DISClib.ADT import map as mp
import csv
 
 
"""
El controlador se encarga de mediar entre la vista y el modelo.
"""
 
# Inicialización del Catálogo de libros
 
 
def loadServices(cont):
    """
    Carga los datos de los archivos CSV en el modelo.
    Se crea un arco entre cada par de estaciones que
    pertenecen al mismo servicio y van en el mismo sentido.
 
    addRouteConnection crea conexiones entre diferentes rutas
    servidas en una misma estación.
    """
    servicesfile = cf.data_dir + 'connections.csv'
    servicesfile_1 = cf.data_dir + 'landing_points.csv'
    servicesfile_2 = cf.data_dir + 'countries.csv'

    input_file = csv.DictReader(open(servicesfile, encoding="utf-8-sig"),
                                delimiter=",")
    input_file_1 = csv.DictReader(open(servicesfile_1, encoding="utf-8"),
                                delimiter=",")
    input_file_2 = csv.DictReader(open(servicesfile_2, encoding="utf-8"),
                                delimiter=",")
    llave = 1
    for cable in input_file:
        model.addinfo_cables_origen(cont,llave,cable)       #analyzer["cables_origen"]
        llave += 1
        model.addRouteConnections(cont,cable)        
    for info in input_file_1:
        model.addinfo_landing(cont,info)                    #analyzer["landing_points"]
        model.addinfo_ciudad(cont,info)                     #analyzer["paises_nombre"]
        model.addinfo_codigo(cont,info)                     #analyzer["paises_codigos"]
        model.addinfo_ciudad_pais(cont,info)                #analyzer["ciudad_pais"]
    for info in input_file_2:                               
        model.addinfo_countries(cont,info)                  #analyzer["countries"]

    
    return cont
 
# Funciones para la carga de datos
def init():
    analyzer = model.newAnalyzer()
    return analyzer

# Funciones de consulta

def sacar_info(analyzer):
    return model.sacar_info(analyzer)


#############################################
#req 1
def connectedComponents(analyzer):
    """
    Numero de componentes fuertemente conectados
    """
    return model.connectedComponents(analyzer)
 
def estan_closter(analyzer,pais1,pais2):
    return model.estan_closter(analyzer,pais1,pais2)
 
#req 2
def servedRoutes(analyzer):
    return model.servedRoutes(analyzer)
#req 3
def minimumCostPaths(analyzer, pais_1):
    return model.minimumCostPaths(analyzer, pais_1)
 
def camino(analyzer,pais_2):
    return model.camino(analyzer,pais_2)
 
def distancia_total(analyzer,pais2):
    return model.distancia_total(analyzer,pais2)
 
#req 4
def infraestructura_critica(analyzer):
    return model.infraestructura_critica(analyzer)
#req 5
def inpacto_landing(cont, landing):
    return model.inpacto_landing(cont, landing)
#req 6
def ancho_de_banda(cont, pais, cable):
    return model.ancho_de_banda(cont, pais, cable)
#req 7
def saltos_minimos(cont, ruta_1, ruta_2):
    return model.saltos_minimos(cont, ruta_1, ruta_2)
 
# Funciones de ordenamiento
 
# Funciones de consulta sobre el catálogo
 
def totalStops(analyzer):
    """
    Total de paradas de autobus
    """
    return model.totalStops(analyzer)
 
 
def totalConnections(analyzer):
    """
    Total de enlaces entre las paradas
    """
    return model.totalConnections(analyzer)