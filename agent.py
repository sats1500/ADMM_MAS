import numpy as np

class NodeAgent(object):
    def __init__(self, id, bus):
        self.id = id
        self.bus = bus
        self.neighbors = dict()

    def connection(self, branch):
        pass
