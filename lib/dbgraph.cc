#include "dbgraph.hh"
#include <iostream>

using namespace dbg;
using namespace std;

void DBGraph::fill(float p) {
   HashIntoType n = pow(DBGraph::_s, DBGraph::_k);

   srand(time(NULL));

   for (HashIntoType i = 0; i < n; i++) {
      float r = (float)rand() / RAND_MAX;

      if (r < p) { 
         DBGraph::set(i);
      }
   }
}

void DBGraph::altfill(float p) {
   HashIntoType n = pow(DBGraph::_s, DBGraph::_k);
   HashIntoType addVerts = (HashIntoType) n * p;
   HashIntoType vertsToAdd = addVerts;

   srand(time(NULL));
   
   while (vertsToAdd != 0) {
      HashIntoType vert = (HashIntoType)(((float)rand() / RAND_MAX) * n);

      if (!get(vert)) {
         DBGraph::set(vert);
         vertsToAdd--;
      }
   }
}

vector<HashIntoType>* DBGraph::getNeighbors(HashIntoType h) {
   vector<HashIntoType>* neighs = new vector<HashIntoType>();

   unsigned int s = DBGraph::_s;
   unsigned int k = DBGraph::_k;
   unsigned int lastPlace = (int) pow(s, k-1);

   HashIntoType back = (h - ((h/lastPlace)*lastPlace))*s;
   HashIntoType forw = h / s;

   for (unsigned int i = 0; i < s; i++) {
      HashIntoType neighOne = i*lastPlace + forw;
      HashIntoType neighTwo = back + i;

      if (get(neighOne)) {
         neighs->push_back(neighOne);
      }

      if (get(neighTwo)) {
         neighs->push_back(neighTwo);
      }
   }

   return neighs;
}

vector<unsigned int>* DBGraph::getComponentLens() {
   vector<unsigned int>* lens = new vector<unsigned int>();
   HashIntoType n = pow(DBGraph::_s, DBGraph::_k);

   Byte * graphCopy = new Byte[_n_bytes];
   for (HashIntoType i = 0; i < _n_bytes; i++) {
      graphCopy[i] = _counts[i];
   }

   for (HashIntoType i = 0; i < n; i++) {
      if (get(i)) {
         vector<HashIntoType> q;
         q.push_back(i);
         unset(i);
         unsigned int len = 0;

         while (q.size() > 0) {
            HashIntoType vert = q.back();
            q.pop_back();
            vector<HashIntoType>* neighs = getNeighbors(vert);
            len++;
 
/*
            unsigned int counter = 0;
            for (HashIntoType i = 0; i < n; i++) {
               if (get(i))
                  counter++;
            }
            cout << counter << endl;
*/

            for (vector<HashIntoType>::iterator i = neighs->begin(); i != neighs->end(); i++) {
               if (get(*i)) {
                  q.push_back(*i);
                  unset(*i);
               }
            }
            delete neighs;

         } // end while
         lens->push_back(len);
      } // end if
   } // end for

   Byte *oldPtr = DBGraph::_counts;
   DBGraph::_counts = graphCopy;
   delete oldPtr;

   return lens;   
}

/*
int main() {
   DBGraph* g = new DBGraph(2, 6);
   g->fill(0.15);

   vector<unsigned int>* compLens = g->getComponentLens();

   for (vector<unsigned int>::iterator i = compLens->begin(); i != compLens->end(); i++) {
      cout << *i << " ";
   }
   cout << endl;

   delete compLens;

   return 0;
}
*/
