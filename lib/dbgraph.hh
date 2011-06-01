#ifndef DBGRAPH_HH
#define DBGRAPH_HH

#include "dbg.hh"
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#include <vector>

namespace dbg {
   class DBGraph {
   protected:
      unsigned int _s;
      unsigned int _k;
      HashIntoType _n_bytes;

      Byte * _counts;

   public:
      DBGraph(unsigned int s, unsigned int k) {
         _s = s;
         _k = k;
         _n_bytes = pow(_s, _k) / 8 + 1;

         _counts = new Byte[_n_bytes];
         memset(_counts, 0, _n_bytes);
      }

      ~DBGraph() {
         delete _counts;
      }

      void set(HashIntoType h) {
         HashIntoType byte = h / 8;
         unsigned char bit = h % 8;

         _counts[byte] |= (1 << bit);
      }

      void unset(HashIntoType h) {
         HashIntoType byte = h / 8;
         unsigned char bit = h % 8;
 
         _counts[byte] &= (255 ^ (1 << bit));
      }

      unsigned char get(HashIntoType h) {
         HashIntoType byte = h / 8;
         unsigned char bit = h % 8;

         if (!(_counts[byte] & (1 << bit))) {
            return 0;
         }
         return 1;
      }

      void clear() {
         memset(_counts, 0, _n_bytes);
      }

      void fill(float p);
      std::vector<HashIntoType>* getNeighbors(HashIntoType h);
      std::vector<unsigned int>* getComponentLens();
   };
};

#endif // DBGRAPH_HH
