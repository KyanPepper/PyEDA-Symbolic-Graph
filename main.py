from pyeda.inter import bdd2expr, expr2bdd, exprvar,bddvar,Or,And,Not
from functions import *
#3.1
# Define the graph G with 32 nodes
nodes = range(32)

# Define the sets even and prime and edge
even_set = {i for i in nodes if i % 2 == 0}
prime_set = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
edgeSet = set()

for i in nodes:
    for j in nodes:
        if isEdge(i,j):
            edgeSet.add((i,j))

##Also known as RR
expressionList = []

# Iterate over node pair in edgeSet and add the expression to expressionlist
for i, j in edgeSet:  
    formula = expressionFactory(i, j)
    expressionList.append(formula)




print(expressionList)
visualize_bdd(expressionList[0])

