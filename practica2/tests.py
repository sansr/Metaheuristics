from PyGMO import *
from PyGMO.util import hypervolume as hypervolume
import numpy
import matplotlib.pyplot as plt

def eliminar_no_dominadas(poblacion):
    p = poblacion
    if (len(p.compute_pareto_fronts()) != 1):
        l = list(p.compute_pareto_fronts())
        no_dominados = list(l.pop(0))
        eliminar = range(0,100,1)
        no_dominados.sort(reverse=True)

        for value in no_dominados:
            del eliminar[value]
            eliminar.sort(reverse=True)

        for indv in eliminar:
            p.erase(indv)
            
    return p

# Definicion del problema de Zitzler
# Hay que cambiar el primer parámetro en función del problema que se quiera evaluar
# Segundo argumento es la dimensión de ZDT
poblem = problema.zdt(1,30)

# Algoritmo SPEA
algoritmo = algorithm.spea2(gen=200, cr = 0.95, eta_c = 10, m = 0.01, eta_m = 50)
algoritmo = algorithm.spea1(archive_size = 0) # Para que se adapte al tamaño de población

# Generar población inicial
pobl = population(prob, 250) # Pasar el número de individuos. Ej: 250

# Ejecutar el algoritmo
pobl = algoritmo.evolve(pobl)

# Coger solo las soluciones no dominadas para pintarlas
pobl = eliminar_no_dominadas(pobl)
pobl.plot_pareto_fronts()

# Obtener distancia generacional e hiprvolumen
print 'Distancia generacional:'
print problem.p_distance(pobl)
print 'Hipervolumen'
hpv = hypervolume(pobl)
print hpv.compute(r=(1,2))

# Dibujar
plt.show()

