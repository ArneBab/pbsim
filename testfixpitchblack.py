#!/usr/bin/env python

"""Testing the fix to the pitch black attack following Oskar Sandberg's fix.

Taken from thesnarks solution: https://emu.freenetproject.org/pipermail/devl/2013-January/036774.html
"""

from pynetsim import *
from networkx import *
from pylab import *
small_world_network = navigable_small_world_graph(1000, 4, 2, 1, 1).to_undirected()
random_network = navigable_small_world_graph(1000, 4, 2, 1, 1).to_undirected()

randomize(random_network)

clean_swap_network = random_network.copy()
attacked_network = random_network.copy()
sandberg_solution_network = random_network.copy()

for i in range(2000):
    swapiteration(clean_swap_network)

def showlinklength(net):
    linklengths = [max([abs((e[0][0] - e[1][0])) for e in net.edges(n)]) for n in net.nodes()]
    ll_smallworld = [max([abs(e[0][0] - e[1][0]) for e in small_world_network.edges(n)]) for n in small_world_network.nodes()]
    ll_random = [max([abs(e[0][0] - e[1][0]) for e in random_network.edges(n)]) for n in random_network.nodes()]
    # hist(linklengths, 100)
    plot(sorted(linklengths), range(len(linklengths)), label="simulated")
    plot(sorted(ll_smallworld), range(len(ll_smallworld)), label="kleinberg")
    plot(sorted(ll_random), range(len(ll_random)), label="randomized")
    yscale('log')
    xscale('log')
    ylabel('number of nodes with this link length or less')
    xlabel('max link length of the node')
    legend()
    show()

showlinklength(clean_swap_network)

attackers = list()
pickmalnodes(attacked_network, attackers, 2)  # We're picking 2 malicious nodes because that is the number chosen by the writers of the Pitch Black paper.
attacksimulation(attacked_network, attackers) # We're using 2 nodes, each with 4 malicious locations.

showlinklength(attacked_network)

sandbergsolution(sandberg_solution_network, attackers, .037)

showlinklength(sandberg_solution_network)