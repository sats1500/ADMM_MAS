import numpy as np

from agent import NodeAgent
import case14 as dt
import matplotlib.pyplot as plt

case = dt.case14()

agents = dict()
branches = dict()

for item in case["bus"]:
    agents[int(item[0])] = NodeAgent(int(item[0]), item[1:])


for item in case["branch"]:

    node_f = int(item[0])
    node_t = int(item[1])

    if node_f not in agents[node_t].neighbors:
        agents[node_t].neighbors[node_f] = agents[node_f]

    if node_t not in agents[node_f].neighbors:
        agents[node_f].neighbors[node_t] = agents[node_t]

for agent in agents.values():
    print agent.id, agent.neighbors

# for ag in agents.values():
#     print ag.id, ag.bus


