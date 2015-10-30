# -*- Mode: makefile -*-
# Copyright (c) 1999 Matthew Wall, all rights reserved
# -----------------------------------------------------------------------------
#   To make all of the examples, do 'make'.  You can compile any one of
# the examples by typing 'make exN' where N is the number of the example you
# want to compile.  See the README for a description of what each example does.
# -----------------------------------------------------------------------------

include galib247/makevars

# Set these paths to the location of the GA library and headers.
#GA_INC_DIR= /usr/local/include
#GA_LIB_DIR= /usr/local/lib
GA_INC_DIR= galib247/
GA_LIB_DIR= galib247/ga

INC_DIRS= -I$(GA_INC_DIR)
LIB_DIRS= -L$(GA_LIB_DIR)

EXS=cipher_game

.SUFFIXES: .C
.C.o:
	$(CXX) $(CXXFLAGS) $(INC_DIRS) -c $<

all: $(EXS)

# Use this for non-gnu make
#$(EXS): $$@.o
#	$(CXX) $@.o -o $@ $(LIB_DIRS) -lga -lm $(CXX_LIBS)

# Use this for gnu make
$(EXS): %: %.o
	$(CXX) $@.o -o $@ $(LIB_DIRS) -lga -lm $(CXX_LIBS)

clean:
	$(RM) $(EXS)
