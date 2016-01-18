'''
Created on Jan 17, 2016

@author: zkphi
'''
# I wrote these functions to write random
# integers to a text file. Is it better to
# use a built in function or write your own ?

from random import randrange

def write_random_int(fout):
    x = randrange(1, 101)
    fout.write(str(x) + " " ) 

fout = open('output.txt','w')

for i in range(1,1000):
    write_random_int(fout)
    if i % 20 == 0:
        fout.write("\n")
        
fout.close()