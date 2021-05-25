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
from DISClib.ADT.graph import addEdge, gr, indegree, vertices
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
from DISClib.DataStructures import listiterator as it 
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
                    'paths': None,
                    'Ciudades': None 
                    }

        analyzer['Vertices'] = mp.newMap(numelements=14000,
                                     maptype='PROBING',
                                     comparefunction=compareStopIds)

        analyzer['Arcos'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000,
                                              comparefunction=compareStopIds)
        analyzer["Ciudades"] = mp.newMap()
        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')
# Funciones para agregar informacion al catalogo
def addinfo(analyzer,info):
    mp.put(analyzer["Ciudades"],int(info["landing_point_id"]),info)

def addStop(analyzer, stopid):
    """
    Adiciona una estación como un vertice del grafo
    """
    try:
        if not gr.containsVertex(analyzer['Arcos'], stopid):
            gr.insertVertex(analyzer['Arcos'], stopid)
        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:addstop')

def addRouteConnections(analyzer,info):
    """
    Por cada vertice (cada estacion) se recorre la lista
    de rutas servidas en dicha estación y se crean
    arcos entre ellas para representar el cambio de ruta
    que se puede realizar en una estación.
    """
    grafo = analyzer["Arcos"]
    llegada = info["destination"]
    origen = info["origin"]
    addStop(analyzer,origen)
    addStop(analyzer,llegada)
    distancia = 0
    if info["cable_length"] != "n.a.":
        final = ((info["cable_length"]).strip(" km")).split(",")
        if len(final) > 1:
            distancia = final[0]+ final[1]
    addEdge(grafo, origen, llegada,int(distancia))

            
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
def connectedComponents(analyzer):
    """
    Calcula los componentes conectados del grafo
    Se utiliza el algoritmo de Kosaraju
    """
    analyzer['components'] = scc.KosarajuSCC(analyzer['Arcos'])
    return scc.connectedComponents(analyzer['components'])

#para mirar si hay camino# tambien se usa para el req 3

def minimumCostPaths(analyzer, pais1):
    """
    Calcula los caminos de costo mínimo desde la estacion initialStation
    a todos los demas vertices del grafo
    """
    analyzer['paths'] = djk.Dijkstra(analyzer['Arcos'], pais1)
    return analyzer

def estan_closter(analyzer,pais2):
    rta = djk.hasPathTo(analyzer["paths"],pais2)
    return rta

#req 2
def servedRoutes(analyzer):
    iterador = it.newIterator(gr.vertices(analyzer["Arcos"]))
    lista = lt.newList()
    total = 0
    while it.hasNext(iterador):
        vertice = it.next(iterador)
        indegree = gr.indegree(analyzer["Arcos"],vertice)
        outdegree = gr.outdegree(analyzer["Arcos"],vertice)
        if indegree >= 1 and outdegree > 1:
            total += 1
            lt.addLast(lista,vertice)
    final = lt.newList()
    return total, lista
#req 3

def ruta(analyzer,pais1):
    distancia_total = djk.distTo(analyzer["path"],pais1)


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