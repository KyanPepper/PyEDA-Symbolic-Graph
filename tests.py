from main import even_set, prime_set
from functions import is_edge

def testFiniteSets():
    assert is_edge(27, 3) == True
    assert is_edge(16, 20) == False
    assert 14 in even_set
    assert 13 not in even_set
    assert 7 in prime_set
    assert 2 not in prime_set

   
