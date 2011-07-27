import _dbg

import math
import random

from scipy import polyfit
from scipy import stats

def conv_to_xy(hist):
   x = []
   y = []

   for i in range(len(hist)):
      if hist[i] != 0:
         x.append(math.log(i+1))
         y.append(math.log(hist[i]))

   return x, y

def RSS_null(x, y, a):
   total = 0

   for i in range(len(x)):
      total += (y[i] - a + x[i])**2
      #total += math.fabs(y[i] - a + x[i])

   return total

def RSS_lin(x, y, b, a):
   total = 0
   # polyval??
   for i in range(len(x)):
      total += (y[i] - (a + b * x[i]))**2
      #total += math.fabs(y[i] - (a + b * x[i]))

   return total

def RSS_quad(x, y, c, b, a):
   total = 0

   for i in range(len(x)):
      total += (y[i] - (a  + b*x[i] + c*x[i]**2))**2
      #total += math.fabs(y[i] - (a  + b*x[i] + c*x[i]**2))

   return total

def main():
   #for s in range(2, 6):
   #   for k in range(2, 25):
   for s, k in [(4,9), (4,10), (5,8), (5,9), (5,10)]:
      for imratherlazy in range(1):
         n = int(s**k)
         if n < 200000 or n > 20000000:
            continue

         fd = open(str(s) + "-" + str(k) + ".txt", "w")
         fd.write("p,F\n")

         n = int(s**k)
         g = _dbg.DBG(s, k)

         for i in range(1000):
            p = random.uniform(0.10, 0.25)

            hist = [0 for x in range(n)]

            g.fill(p)
            comp_lens = sorted(g.getComponentLens(), reverse=True)
            g.clear()

            for comp_len in comp_lens:
               hist[comp_len-1] += 1

            x,y = conv_to_xy(hist)

            if len(x) != 0:
               null = polyfit(x,y,0)
               lin = polyfit(x,y,1)
               quad = polyfit(x,y,2)
               RSSnull = RSS_null(x,y,null[0])
               RSSlin = RSS_lin(x,y,lin[0],lin[1])
               RSSquad = RSS_quad(x,y,quad[0],quad[1],quad[2])
               F = ((float(RSSlin) - RSSquad) / (3.0 - 2)) / (RSSquad / (len(x) - 3.0))
               fd.write(str(p) + "," + str(F) + "\n")

         fd.close()

main()
