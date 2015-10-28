#include <ga/GASimpleGA.h>	// we're going to use the simple GA
#include <ga/GA1DBinStrGenome.h> // and the 1D binary string genome
#include <ga/std_stream.h>

#define cout STD_COUT

float Objective(GAGenome &);	// This is the declaration of our obj function. // The definition comes later in the file.

// Declare variables for the GA parameters and set them to some default values.

int length    = 10;
int popsize  = 20;
int ngen     = 400;
float pmut   = 0.001;
float pcross = 0.9;

main() {
  GA1DBinaryStringGenome genome(length, Objective));
  GASimpleGA ga(genome);
  ga.populationSize(popsize);
  ga.nGenerations(ngen);
  ga.pMutation(pmut);
  ga.crossover(GA1DBinaryStringGenome::OnePointCrossover);
  ga.evolve();
}

