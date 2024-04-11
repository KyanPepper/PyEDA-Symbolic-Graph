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

##Before conversion
expressionList = []

# Iterate over node pair in edgeSet and add the expression to expressionlist
for i, j in edgeSet:  
    formula = expressionFactory(i, j)
    expressionList.append(formula)

# Combine all expressions with or to make RR BDD
RR = expressionList[0]
for expr in expressionList[1:]:
    RR |= expr  

##RR2
RR2 = bdd_compose(RR,RR)

#Computes R stars with transitive closuren, RR2star encodes the set of all node pairs such that one can reach the other in a positive even number of steps.
RR2Star = compute_transitive_closure(RR2)

#for every prime number  u, there exists at least one even number  v such that  u is related to  v
A = Not(RR2Star).smoothing().equivalent(False)


