from random import randint
import time

klass = [ 'kairo' , 'aigar' , 'timo' , 'mario' , 'aulis' ]

print klass


print len (klass)

a=len(klass)

min= 0
max= a-1

a = randint (min,max)

print klass [a]

--------------------------------------
print klass [randint(0,len(klass)-1)]
