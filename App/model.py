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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newAnalyzer():
    try:
        analyzer = {
                    'Vertices': None,
                    'Arcos': None,
                    'components': None,
                    'paths': None
                    }

        analyzer['Vertices'] = m.newMap(numelements=14000,
                                     maptype='PROBING',
                                     comparefunction=compareStopIds)

        analyzer['Arcos'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000,
                                              comparefunction=compareStopIds)
        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')
# Funciones para agregar informacion al catalogo
def addRouteConnections(analyzer):
    """
    Por cada vertice (cada estacion) se recorre la lista
    de rutas servidas en dicha estación y se crean
    arcos entre ellas para representar el cambio de ruta
    que se puede realizar en una estación.
    """
    lststops = m.keySet(analyzer['stops'])
    for key in lt.iterator(lststops):
        lstroutes = m.get(analyzer['stops'], key)['value']
        prevrout = None
        for route in lt.iterator(lstroutes):
            route = key + '-' + route
            if prevrout is not None:
                addConnection(analyzer, prevrout, route, 0)
                addConnection(analyzer, route, prevrout, 0)
            prevrout = route

            
# Funciones para creacion de datos

# Funciones de consulta
def totalStops(analyzer):
    """
    Retorna el total de estaciones (vertices) del grafo
    """
    return gr.numVertices(analyzer['connections'])


def totalConnections(analyzer):
    """
    Retorna el total arcos del grafo
    """
    return gr.numEdges(analyzer['connections'])


#req 1
def calcular_glusteres(landing_1,landing_2):
    return None
#req 2
def calcular_landings():
    return None
#req 3
def minima_paises(Pais_1,Pais_2):
    return None
#req 4
def infraestructura_critica():
    return None
#req 5
def inpacto_landing(landing):
    return None


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento
def compareStopIds(stop, keyvaluestop):
    """
    Compara dos estaciones
    """
    stopcode = keyvaluestop['key']
    if (stop == stopcode):
        return 0
    elif (stop > stopcode):
        return 1
    else:
        return -1