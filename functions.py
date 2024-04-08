from pyeda.inter import *
import graphviz
import os
import time

#size of graph
size = 32 
#number of bits (log2(32))
bits = 5
#bddvars
xa = bddvars('x', 5)
ya = bddvars('y', 5)
za = bddvars('z', 5)
#Returns if node is edge
def isEdge(i, j):
    return ((i + 3) % 32 == j % 32) or ((i + 8) % 32 == j % 32)

def boolListToExp(list, name):
    # Create list of Boolean variables
    bdds = bddvars(name, bits)
    
    bddlist = []
    # Creates a list of expressions for each bit in the list
    for key, value in zip(bdds, list):
        if value:
            bddlist.append(key)
        else:
            bddlist.append(~key)
    
    result = bddlist[0]
    # Combine all expressions with & 
    for expr in bddlist[1:]:
        result = result & expr
    
    return result

#converts integer to boolean array
def to_bin(num):
    #formats into 5 bit binary string
    binary_str = format(num, '05b') 
    result = []

    # Iterate over each bit and casts to int then bool then adds to list
    for bit in binary_str:
        bit_value = int(bit)
        boolean_value = bool(bit_value)
        result.append(boolean_value)

    return result

#returns the singlebdd for the edge set
def expressionFactory(i, j):
    argx = to_bin(i)
    argy = to_bin(j)

    x = boolListToExp(argx, 'x')
    y = boolListToExp(argy, 'y')

    return x & y

def bdd_compose(bdd1 , bdd2):
    for i in range(0, bits):
        bdd1 = bdd1.compose({ya[i]: za[i]})
        bdd2 = bdd2.compose({xa[i]: za[i]})
    return (bdd1 & bdd2).smoothing(za)


#saves graph as a png file into build folder
def visualize_bdd(bdd):
    timestamp = time.strftime('%Y%m%d-%H%M%S')
    filename = f'bdd_structure_{timestamp}.txt'
    dot_str = bdd.to_dot()
    graph = graphviz.Source(dot_str)
    graph.render(filename=filename, format='png', view=True , directory=os.getcwd()+'/build')



