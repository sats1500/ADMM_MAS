import numpy as np

class NodeAgent(object):
    def __init__(self, id, type, a, b, Pmin, Pmax, Pd, Qd):
        self.id = id
        self.type = type
        self.a = a  # variable term in bid curve bc = 2aP + b
        self.b = b  # constant term in bid curve bc = 2aP + b
        self.Pmin = Pmin
        self.Pmax = Pmax
        self.Pg = 0.0
        self.Qg = 0.0
        self.Pd = Pd
        self.Qd = Qd
        self.value = 0.0

    def __str__(self):
        '''
            This is the printing function of the object Agent, printed if cfg.print_agents = True
            - Return: string message
        '''
        return "|------> Agent id: %s, type: %1s, power: %8.2f, value: %8.2f"% (
            self.id, self.type, self.P, self.value) + "\n"

c