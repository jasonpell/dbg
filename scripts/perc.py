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
   ps = [x/float(100) for x in range(15, 20, 1)]
   n = 1
   s = 4
   k = 10
   n = int(s**k)

   g = _dbg.DBG(s, k)

   #for p in ps:
   for i in range(200):
      p = random.uniform(0.15, 0.35)

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
         #F = RSSquad / RSSlin
         F = ((float(RSSlin) - RSSquad) / (3.0 - 2)) / (RSSquad / (len(x) - 3.0))

         #Fquad = stats.f_value(RSSnull, RSSquad, len(x)-1, len(x)-3) #df = 1?
         #Flin = stats.f_value(RSSnull, RSSlin, len(x)-1, len(x)-2)

         #print p, Fquad, Flin, Fquad / float(Flin)
         print p, F, len(x)

main()
