from copy import deepcopy
class colonTuple:
    def tupleColon(self,Tup):
        Tup_copy=deepcopy(Tup)
        Tup_copy[2].append('e')
        print(Tup_copy)
        print(Tup)

Tup=('a','b',[],'c','d')
Tuple=colonTuple()
Tuple.tupleColon(Tup)