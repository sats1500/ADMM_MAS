import numpy as np

class NodeAgent(object):
    def __init__(self, id, num, a, b, Pmin, Pmax, Pd, Qd, neig):
        self.id = id
        self.type = num
        self.a = a  # variable term in bid curve bc = 2aP + b
        self.b = b  # constant term in bid curve bc = 2aP + b
        self.Pmin = Pmin
        self.Pmax = Pmax
        self.Pg = 0.0
        self.Qg = 0.0
        self.Pd = Pd
        self.Qd = Qd
        self.neig = neig
        self.value = 0.0

    def connection(self,branch):
