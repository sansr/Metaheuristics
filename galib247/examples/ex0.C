#include <stdio.h>
#include <stdlib.h>
#include <ga/GASimpleGA.h>
#include <ga/GAStringGenome.h>
#include <ga/GAAllele.h>
#include <ga/std_stream.h>

#define cout STD_COUT

// List of arguments
int* list;
int optimal;

// Parameters to create the poblation and individuals
int length = 5;
int popsize = 20;

int objective(GAGenome &);

int main(int argc, char* argv[])
{
  // Read parameters
  for (int i = 0; i < argc-1; i++) {
    list[i] = atoi(argv[i]);
  }
  optimal = atoi(argv[argc-1]);
  
  // Create allele set
  GAStringAlleleSet alleles;
  alleles.add('+');
  alleles.add('-');
  alleles.add('*');
  
  
  // Declare a genome object
  GAStringGenome genome(length, alleles, objective);

  // Mutator
  //genome.mutator(GAStringFlipMutator);
  
  // Declare the genetic algorithm
  GASimpleGA ga(genome);

  // Establish parameters
  ga.populationSize(popsize);

  // Crossover
  ga.crossover(GAStringOnePointCrossover);
  
  // Evolve
  ga.evolve();

  // Print statistics
  cout << ga.statistics();

  return 0;
}

// Fitness function
int objective(GAGenome & g)
{
  // Casting to the used genome
  GAStringGenome & genome = (GAStringGenome &) g;

  float acc = 0;
  for (int i = 0; i < genome.length(); i++) {
    // Apply operations codified into the genes
    switch (genome.gene(i)) {
      case '+':
	if (i == 0)
	  acc = list[i] + list[i+1];
	else
	  acc += list[i+1];
	break;
      case '-':
	if (i == 0)
	  acc = list[i] - list[i+1];
	else
	  acc -= list[i+1];
	break;
      case '*':
	if (i == 0)
	  acc = list[i] * list[i+1];
	else
	  acc *= list[i+1];
	break;
    }
  }
  
  return abs(852-acc);
}
