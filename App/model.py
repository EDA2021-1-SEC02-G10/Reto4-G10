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
from DISClib.Algorithms.Graphs import prim as p
from DISClib.Algorithms.Sorting import mergesort as merge
from DISClib.DataStructures import bst as tree

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
                    'landing_points': None,
                    'paises_nombre':None,
                    'paises_codigos':None
                    }
 
        analyzer['Vertices'] = mp.newMap(numelements=14000,
                                     maptype='PROBING',
                                     comparefunction=compareStopIds)
 
        analyzer['Arcos'] = gr.newGraph(datastructure='ADJ_LIST',
                                              directed=True,
                                              size=14000,
                                              comparefunction=compareStopIds)
        analyzer["landing_points"] = mp.newMap()
        analyzer["paises_nombre"] = mp.newMap()
        analyzer["paises_codigos"] = mp.newMap()
        return analyzer
    except Exception as exp:
        error.reraise(exp, 'model:newAnalyzer')
# Funciones para agregar informacion al catalogo
 
def addinfo_landing(analyzer,info):
    nombre = str(info["name"]).split(",")
    nombre_landing = str(nombre[0])
    mp.put(analyzer["landing_points"],nombre_landing,info)
 
def addinfo_ciudad(analyzer,info):
    nombre = str(info["name"]).split(",")
    nombre_pais = str(nombre[-1])
    mp.put(analyzer["paises_nombre"],nombre_pais,str(info["landing_point_id"]))
 
def addinfo_codigo(analyzer,info):
    mp.put(analyzer["paises_codigos"],str(info["landing_point_id"]),info)
 
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
 
#para mirar si hay camino
def estan_closter(analyzer,pais1,pais2):
    Entry1 = mp.get(analyzer["landing_points"], pais1)
    Pais_1 = me.getValue(Entry1)
    entry2 = mp.get(analyzer["landing_points"],pais2)
    pais_2 = me.getValue(entry2)
    booleano = scc.stronglyConnected(analyzer["components"],str(Pais_1["landing_point_id"]),str(pais_2["landing_point_id"]))
    return booleano
 
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
    iterador_1 = it.newIterator(lista)
    while it.hasNext(iterador_1):
        elemento = it.next(iterador_1)
        pareja = mp.get(analyzer["paises_codigos"],elemento)
        valor = me.getValue(pareja)
        lt.addLast(final,valor["id"])
        lt.addLast(final,valor["name"])
    return total,final
 
#req 3
 
def minimumCostPaths(analyzer, pais1):
    """
    Calcula los caminos de costo mínimo desde la estacion initialStation
    a todos los demas vertices del grafo
    """
    Entry1 = mp.get(analyzer["paises_nombre"], pais1)
    pais_1 = me.getValue(Entry1)
    analyzer['paths'] = djk.Dijkstra(analyzer['Arcos'], pais_1)
    return analyzer
    
 
def camino(analyzer,pais2):
    Entry1 = mp.get(analyzer["paises_nombre"], pais2)
    Pais_id = me.getValue(Entry1)
    rta = djk.pathTo(analyzer["paths"],Pais_id)
    iterador = it.newIterator(rta)
    lista = lt.newList()
    while it.hasNext(iterador):
        dic = {}
        elemento = it.next(iterador)
        vertex_a = elemento["vertexA"]
        pais_a_pareja = mp.get(analyzer["paises_codigos"],vertex_a)
        nommbre_paisa = me.getValue(pais_a_pareja)
        vertex_b = elemento["vertexB"]
        pais_b_pareja = mp.get(analyzer["paises_codigos"],vertex_b)
        nombre_paisb = me.getValue(pais_b_pareja)
        weight = elemento["weight"]
        dic["vertexA"] = nommbre_paisa["name"]
        dic["vertexB"] = nombre_paisb["name"]
        dic["weight"] = weight
        lt.addLast(lista,dic)
    return lista
 
def distancia_total(analyzer,pais2):
    Entry1 = mp.get(analyzer["paises_nombre"], pais2)
    Pais_id = me.getValue(Entry1)
    camino = djk.distTo(analyzer["paths"],Pais_id)
    return camino
 
#req 4
def infraestructura_critica(analyzer):
    arbol = p.PrimMST(analyzer["Arcos"])
    vertices = gr.numVertices(analyzer["Arcos"])
    Peso = p.weightMST(analyzer["Arcos"], arbol)
    rama = p.edgesMST(analyzer["Arcos"], arbol)
    rama = rama["edgeTo"]["table"]["elements"]
    #iterador = it.newIterator(rama)
    maximo = 0
    for i in range(len(rama)):
        valor = rama[i]["value"]
        if (valor is not None) and (float(valor["weight"]) > maximo):
            maximo = valor["weight"]

    return vertices, Peso, maximo
#req 5
def inpacto_landing(analyzer, landing):
    Entry1 = mp.get(analyzer["landing_points"], landing)
    Pais_id = me.getValue(Entry1)
    numero = gr.indegree(analyzer["Arcos"],str(Pais_id["landing_point_id"]))
    paises_id = gr.adjacentEdges(analyzer["Arcos"], str(Pais_id["landing_point_id"]))


    iterador = it.newIterator(paises_id)
    pesos = lt.newList()
    while it.hasNext(iterador):
        Pais_id = it.next(iterador)
        lt.addLast(pesos, Pais_id)
    merge.sort(pesos, comparar_pesos)

    iterador_2 = it.newIterator(pesos)
    IDs = lt.newList()
    Paises = lt.newList()
    while it.hasNext(iterador_2):
        Pais_id = it.next(iterador_2)
        vertice_id = Pais_id["vertexB"]
        Entry2 = mp.get(analyzer["paises_codigos"], vertice_id)
        Pais = me.getValue(Entry2)
        lt.addLast(IDs, Pais["name"])

    return numero, IDs


 
 
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
def comparar_pesos(peso1, peso2):

    rta = True
    if int(peso1["weight"]) < int(peso2["weight"]):
        rta = False
    return rta
