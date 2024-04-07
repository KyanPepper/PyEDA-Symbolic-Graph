from pyeda.inter import *
from functions import *

# Define the graph G with 32 nodes
nodes = range(32)

# Define the sets even and prime
even_set = {i for i in nodes if i % 2 == 0}
prime_set = {3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
