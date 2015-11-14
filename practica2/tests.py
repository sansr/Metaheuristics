from PyGMO import *
from PyGMO.util import hypervolume as hypervolume
from PyGMO.util import hv_algorithm as hv_algorithm
import matplotlib.pyplot as plt
import numpy
#eliminar_dominadas de la poblacion las soluciones dominadas.

#******************** Funcion Principal*****************
def eliminar_dominadas(pop):
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
                print ''
    return poblac


#Definicion de parametros segun Zitzler et. al, 2000
prob = problem.zdt(1, 30)
n_gen=250
pop_size=80
cross_rate=0.8
mut_rate=0.01
rep=30
archive_size=20


alg = algorithm.spea(gen=n_gen, cr=cross_rate, m=mut_rate, archive_size=archive_size) #Defino algoritmo SPEA
# alg2 = algorithm.spea2(gen=n_gen, cr=cross_rate, m=mut_rate, archive_size=archive_size) #Defino algoritmo SPEA
#
#
# alg = algorithm.nsga_II(gen = 100, cr = 0.95, eta_c = 10, m = 0.01, eta_m = 50)
# pop = population(prob, pop_size) #Genero poblacion inicial aleatoria del problema ZDT
# pop2 = population(prob, pop_size)
valores_pdistance=[]
valores_hv=[]
for i in range(rep):
    pop = population(prob, pop_size) #Genero poblacion inicial aleatoria del problema ZDT
    pop = alg.evolve(pop) #Poblacion final al ejecutar el algoritmo
    # pop3 = alg3.evolve(pop3)
    pop=eliminar_dominadas(pop) #Dejo solo las soluciones no dominadas de la poblacion final
    pop.plot_pareto_fronts() #Pinto las soluciones en el grafic
    # pop3.plot_pareto_fronts()

    valores_pdistance=valores_pdistance+[prob.p_distance(pop)] #Obtengo de la poblacion no dominada
    hv= hypervolume(pop) #Obtengo de la poblacion no dominada el hipervolumen
    ref_point = hv.get_nadir_point(0.1)
    valores_hv=valores_hv+[hv.compute(r=ref_point)] #Computo el hipervolumen especificando la referencia


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
