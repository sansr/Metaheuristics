/* ----------------------------------------------------------------------------
  ex12.C
  mbwall 13apr95
  Copyright (c) 1995-1996  Massachusetts Institute of Technology

 DESCRIPTION:
   This example shows how to use an order-based string genome.
---------------------------------------------------------------------------- */
#include <stdio.h>
#include <stdlib.h>
#include <ga/ga.h>
#include <ga/std_stream.h>

#define cout STD_COUT

#define INSTANTIATE_STRING_GENOME
#include <ga/GAStringGenome.h>


// This is the declaration of the objective function that we will use in this
// example.
float objective(GAGenome &);

// Every genome must have an initializer.  Here we declare our own initializer
// that will be used in this example.
void OperatorsInitializer(GAGenome &);

int values[6];
int optimal;
int length = 5;
int popsize  = 100;
int ngen     = 500;
float pmut   = 0.001;
float pcross = 0.9;

int
main(int argc, char *argv[])
{
  if(argc != 8){
    fputs("You must indicate 6 numbers and the result do you expect\n", stderr);
    return -1;
  }

  for (int i=1; i<(argc-1); i++) {
    values[i-1] = atoi(argv[i]);
  }

  optimal = atoi(argv[argc-1]);

// Now create the GA and run it.  We first create a genome with the
// operators we want.  Since we're using a template genome, we must assign
// all three operators.  We use the order-based crossover site when we assign
// the crossover operator.

  GAStringAlleleSet alleles;
  alleles.add('+');
  alleles.add('-');
  alleles.add('*');

  GAStringGenome genome(length, alleles, objective);
  cout << "poblacion inicial";
  genome.initializer(OperatorsInitializer);
  ///genome.mutator(GAStringSwapMutator);
  cout << "______________";

  GASimpleGA ga(genome);
  ga.populationSize(popsize);
  ga.nGenerations(ngen);
  ga.pMutation(pmut);
  ga.pCrossover(pcross);
  ga.minimize();
  ga.crossover(GAStringOnePointCrossover);
  ga.evolve();

  genome = ga.statistics().bestIndividual();
  cout << "the ga generated the following string (objective score is \n";
  cout << genome.score();
  cout << "\n" << genome << "\n";
  cout << genome.className() << "\n";
  return 0;
}

int Operations(int a, int b, char op){
  if (op == '+'){
    return a + b;
  }
  else if (op == '-'){
    return a - b;
  }
  else {
    return a * b;
  }
}

/* ----------------------------------------------------------------------------
Objective function
  The objective function try to minimize the difference betweent the operations
  defined by the genome and 852.
---------------------------------------------------------------------------- */
float
objective(GAGenome & c)
{
  GAStringGenome & genome = (GAStringGenome &)c;

  //int values [] = {25,6,9,75,50,3};
  int result = values [0];
  for(int i=0; i<genome.size(); i++){
    result = Operations (result, values[i+1], genome.gene(i));
  }
  cout << "\n\nresult\n";
  cout << result;
  cout << "\ngenome\n";
  cout << genome;
  return abs(result - optimal);
}



/* ----------------------------------------------------------------------------
OperatorsInitializer
  This initializer creates a string genome with the letters +-* as its
elements.  Once we have assigned all the values, we randomize the string.
---------------------------------------------------------------------------- */
void
OperatorsInitializer(GAGenome & c)
{
  GAStringGenome &genome=(GAStringGenome &)c;
  int i;
  char operators [] = {'+', '-', '*'};
  for (i = 0; i < genome.size(); i ++){
    genome.gene(i, operators[GARandomInt(0, 2)]);
  }
  for(i=0; i<genome.size(); i++)
    if(GARandomBit()) genome.swap(i, GARandomInt(0, genome.size()-1));
  //
  cout << genome;
  cout << "\n";
}
