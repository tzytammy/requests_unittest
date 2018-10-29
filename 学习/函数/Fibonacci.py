def fab(max):
   n, a, b = 0, 0, 1
   while n < max:
       print('a=',a)
       print ('b=',b)
       a, b = b, a + b
       n = n + 1

print(fab(5))