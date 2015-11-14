from PyGMO import *
from PyGMO.util import hypervolume as hypervolume
from PyGMO.util import hv_algorithm as hv_algorithm
import matplotlib.pyplot as plt
import numpy
#Quitar de la poblacion las soluciones dominadas.
def quitar(pop):
    poblac=pop
    if (len(poblac.compute_pareto_fronts())==1):
        print 'Ya es no dominado'
    else:
        lista=list(poblac.compute_pareto_fronts())
        nodom=list(lista.pop(0))
        borrar=range(0,100,1)
        nodom.sort(reverse=True)
        for casos in nodom:
            del borrar[casos]
            borrar.sort(reverse=True)
        for individuo in borrar:
            try:
                poblac.erase(individuo)
            except:
                print '99'
    return poblac

#******************** Funcion Principal*****************

#Definicion de parametros segun Zitzler et. al, 2000
prob = problem.zdt(5, 11)
n_gen=250
pop_size=80
cross_rate=0.8
mut_rate=0.01
rep=30
archive_size = 20
#Algoritmo SPEA
#Inicializo contador y vectores de distancia genaracional e hipervolumen
contador=0




valores_pdistance=[]
valores_hv=[]
while(contador<rep): #Para cada una de las 30 ejecuciones...
    alg = algorithm.spea2(gen=n_gen, cr=cross_rate, m=mut_rate, archive_size=archive_size) #Defino algoritmo SPEA
    pop1 = population(prob, pop_size) #Genero poblacion inicial aleatoria del problema ZDT
    pop1 = alg.evolve(pop1) #Poblacion final al ejecutar el algoritmo
    pop1=quitar(pop1) #Dejo solo las soluciones no dominadas de la poblacion final
    pop1.plot_pareto_fronts() #Pinto las soluciones en el grafico
    valores_pdistance=valores_pdistance+[prob.p_distance(pop1)] #Obtengo de la poblacion no dominada
    hv1= hypervolume(pop1) #Obtengo de la poblacion no dominada el hipervolumen
    ref_point = hv1.get_nadir_point(0.1)
    valores_hv=valores_hv+[hv1.compute(r=ref_point, algorithm=hv_algorithm.hv2d())] #Computo el hipervolumen especificando la referencia
    contador=contador+1

#Obtengo la media y desviacion tipica de la distancia generacional y el hipervolumen
print 'mean p-distance SPEA'
print numpy.mean(valores_pdistance)
print 'standard deviation p-distance SPEA'
print numpy.std(valores_pdistance)
print 'mean hypervolume SPEA'
print numpy.mean(valores_hv)
print 'standard deviation hypervolume SPEA'
print numpy.std(valores_hv)

plt.show()
