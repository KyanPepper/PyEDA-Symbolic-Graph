from main import even_set, prime_set, edgeSet,RR
from pyeda.inter import bdd2expr, expr2bdd, exprvar,bddvar,Or,And,Not

def testFiniteSets():
    assert (27, 3) in edgeSet 
    assert (16, 20) not in edgeSet
    assert 14 in even_set
    assert 13 not in even_set
    assert 7 in prime_set
    assert 2 not in prime_set



