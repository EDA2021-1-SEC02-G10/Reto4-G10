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

# Funciones para la carga de datos
def init():
    analyzer = model.newAnalyzer()
    return analyzer
#req 1
def calcular_glusteres(landing_1,landing_2):
    return model.calcular_glusteres(landing_1,landing_2)
#req 2
def calcular_landings():
    return model.calcular_landings()
#req 3
def minima_paises(Pais_1,Pais_2):
    return model.minima_paises(Pais_1,Pais_2)
#req 4
def infraestructura_critica():
    return model.infraestructura_critica()
#req 5
def inpacto_landing(landing):
    return model.inpacto_landing(landing)


# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
