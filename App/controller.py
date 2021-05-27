"""
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
    input_file = csv.DictReader(open(servicesfile, encoding="utf-8-sig"),
                                delimiter=",")
    input_file_1 = csv.DictReader(open(servicesfile_1, encoding="utf-8"),
                                delimiter=",")
    for cable in input_file:
        model.addRouteConnections(cont,cable)
    for info in input_file_1:
        model.addinfo(cont,info)
    return cont


# Funciones para la carga de datos
def init():
    analyzer = model.newAnalyzer()
    return analyzer

#req 1
def connectedComponents(analyzer):
    """
    Numero de componentes fuertemente conectados
    """
    return model.connectedComponents(analyzer)

def minimumCostPaths(analyzer, pais1):
    return model.estan_closter(analyzer, pais1)

def estan_closter(analyzer,pais2):
    return model.estan_closter(analyzer,pais2)

#req 2
def servedRoutes(analyzer):
    return model.servedRoutes(analyzer)
#req 3
def minimumCostPaths(analyzer, initialStation):
    return model.minimumCostPaths(analyzer, initialStation)
def hasPath(analyzer, destStation):
    return model.hasPath(analyzer, destStation)
def minimumCostPath(analyzer, destStation):
    return model.minimumCostPath(analyzer, destStation)
#req 4
def infraestructura_critica(analyzer):
    return model.infraestructura_critica()
#req 5
def inpacto_landing(landing):
    return model.inpacto_landing(landing)


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
