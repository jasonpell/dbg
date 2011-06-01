import _dbg

for s in range(1, 6, 1):
   for k in range(2, 9, 1):
      g = _dbg.DBG(s, k)
      g.fill(1.0)
      n = int(s**k)

      max_count = 0
      not_max_count = 0

      for i in range(n):
         neighSet = set(g.getNeighbors(i))
         if len(neighSet) < 2*s:
            not_max_count += 1
         else:
            max_count += 1

      print s, k, max_count, not_max_count
         

