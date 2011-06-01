from libcpp.vector cimport vector
from cython.operator cimport dereference as deref, preincrement as inc

ctypedef unsigned long long int HashIntoType
ctypedef unsigned char Byte

cdef extern from "../lib/dbgraph.hh" namespace "dbg":
   cdef cppclass DBGraph:
      DBGraph(unsigned int s, unsigned int k)
      void set(HashIntoType h)
      void unset(HashIntoType h)
      unsigned char get(HashIntoType h)
      void clear()
      void fill(float p)
      vector[HashIntoType]* getNeighbors(HashIntoType h)
      vector[unsigned int]* getComponentLens()

cdef class DBG:
   cdef DBGraph *thisptr
   def __cinit__(self, unsigned int s, unsigned int k):
      self.thisptr = new DBGraph(s, k)
   def set(self, HashIntoType h):
      self.thisptr.set(h)
   def unset(self, HashIntoType h):
      self.thisptr.unset(h)
   def get(self, HashIntoType h):
      return self.thisptr.get(h)
   def clear(self):
      self.thisptr.clear()
   def fill(self, float p):
      self.thisptr.fill(p)
   def getNeighbors(self, HashIntoType h):
      cdef vector[HashIntoType]* v = self.thisptr.getNeighbors(h)
      neighs = []

      cdef vector[HashIntoType].iterator it = v.begin()
      while it != v.end():
         neighs.append(deref(it))
         inc(it)

      del v
      return neighs

   def getComponentLens(self):
      cdef vector[unsigned int]* v = self.thisptr.getComponentLens()
      lens = []

      cdef vector[unsigned int].iterator it = v.begin()
      while it != v.end():
         lens.append(deref(it))
         inc(it)

      del v
      return lens
      
