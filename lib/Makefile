CXXFLAGS=-g -fPIC -Wall -O2

all: dbgraph.o 2d.o

clean:
	rm -f *.o

dbgraph.o: dbgraph.cc dbgraph.hh dbg.hh

2d.o: 2d.cc 2d.hh dbg.hh
