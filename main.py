import numpy as np

from agent import NodeAgent
import case as dt
import matplotlib.pyplot as plt


Node = dt.bus.shape[0]
print('node = '+str(Node))

allagents = []
for n in range(Node):
    tagent = NodeAgent('N'+str(1), 'node', dt.gencost.item((n,4)), dt.gencost.item((n,5)), dt.gen.item((n,8)), 2.0, 0.0, 0.0)
    allagents.append(tagent)


print allagents[0].a