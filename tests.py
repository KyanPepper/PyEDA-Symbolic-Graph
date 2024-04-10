from main import even_set, prime_set, edgeSet, RR2
from pyeda.inter import bdd2expr, expr2bdd, exprvar,bddvar,Or,And,Not
from functions import expressionFactory

def testFiniteSets():
    assert (27, 3) in edgeSet 
    assert (16, 20) not in edgeSet
    assert 14 in even_set
    assert 13 not in even_set
    assert 7 in prime_set
    assert 2 not in prime_set



def testRR2():
    RR2str = (str(bdd2expr(RR2)))
    
    edgeTestPass = expressionFactory(27,6)
    edgeStr = (str(bdd2expr(edgeTestPass)))

    edgeTestFail = expressionFactory(23,6)
    edgeStrF = (str(bdd2expr(edgeTestFail)))

    assert edgeStr in RR2str
    assert edgeStrF not in RR2str
    

   