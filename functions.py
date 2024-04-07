from pyeda.inter import *
import graphviz
import os
import time
#Returns if node is edge
def is_edge(i, j):
    return ((i + 3) % 32 == j % 32) or ((i + 8) % 32 == j % 32)

#Print boolean tree of BDD
def print_bdd(bdd, varmap=None, indent=0):
    if varmap is None:
        varmap = {}
    
    # Base case: BDD is terminal (constant 0 or 1)
    if bdd.is_zero():
        print(' ' * indent + 'False')
        return
    elif bdd.is_one():
        print(' ' * indent + 'True')
        return
    
    # Get the top variable of the BDD node
    var = bdd.top

    # Assign label to variable if not already assigned
    if var not in varmap:
        varmap[var] = var

    var_label = varmap[var]

    # Recursive call for high and low branches
    high_bdd = bdd.restrict({var: 1})
    low_bdd = bdd.restrict({var: 0})

    # Print node with variable label and branching information
    print(' ' * indent + f'If {var_label} is True:')
    print_bdd(high_bdd, varmap, indent + 4)
    print(' ' * indent + f'Else if {var_label} is False:')
    print_bdd(low_bdd, varmap, indent + 4)


#saves graph as a png file into build folder
def visualize_bdd(bdd):
    timestamp = time.strftime('%Y%m%d-%H%M%S')
    filename = f'bdd_structure_{timestamp}.txt'
    dot_str = bdd.to_dot()
    graph = graphviz.Source(dot_str)
    graph.render(filename=filename, format='png', view=True , directory=os.getcwd()+'/build')


