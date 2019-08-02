import networkx as nx
import random
import matplotlib.pyplot as plt

# Create out networkx graph and call ig G
G = nx.Graph()

# Create an edge list where the first node is set as i which has a range of 1 to 20
# Second i is set to i + 1
# And the weight is i * 5 + 1
elist=[(i, i+1, (i*5)+1) for i in range(1, 20)]

# Run our elist through the shuffle function which shuffles our numbers around so they're not linear
random.shuffle(elist)

print("**************GRAPH APPLICATION**************")
print()
print('-'*250)
print("\nGenerated edge list with weights")
print()
print('-'*250)
wait = input("\nPress enter to shuffle and print out the edge list")

# Run our elist through the shuffle function which shuffles our numbers around so they're not linear
random.shuffle(elist)

# Print out our edge list
print()
print(elist)


# Adds the edge list as weighted edges to our graph
G.add_weighted_edges_from(elist)

# Generates a single line of the graph in an adjacency list format
adj = nx.generate_adjlist(G)

print('-'*250)
wait = input("\nPress enter to print out graph in adjacency list format")
print()

# For every edge in the adjacency list, print out the edge
for edge in adj:
    print(edge)

# Generate a single line of the graph in an edge list format
edg_list = nx.generate_edgelist(G)

print('-'*250)
wait = input("\nPress enter to print out graph in edge list format")
print()

# For every edge in the edge list, print out the edge
for edge in edg_list:
    print(edge)

print('-'*250)
wait = input("\nPress enter to run the graph through the "
             "shortest simple paths algorithm and both print and visually display it"
             "\n(Close out of graph when done)")
print()


# Run our graph through the shortest simple paths algorithm
paths = list(nx.shortest_simple_paths(G, 1, 20))

# Print out paths
print(paths)

# Draw the graph using matplotlib and display it
nx.draw(G, with_labels=True)
plt.draw()
plt.show()

print('-'*250)
wait = input("\nPress enter to run the graph through the "
             "A* algorithm and both print and visually display it"
             "\n(Close out of graph when done)")
print()
# Run our graph through the A* algorithm
astar_res = nx.astar_path(G, 1, 20)
print(astar_res)

# For every edge in the edge list, print out the edge
for edge in edg_list:
    print(edge)

# Draw the graph using matplotlib and display it
nx.draw(G, with_labels=True)
plt.draw()
plt.show()


print('-'*250)
wait = input("\nPress enter to run the graph through the "
             "Double edge swap algorithm and both print and visually display it"
             "\n(Close out of graph when done)")
print()
# Run our graph through the double edge swap algorithm
nx.double_edge_swap(G)
edg_list = nx.generate_edgelist(G)

# For every edge in the edge list, print out the edge
for edge in edg_list:
    print(edge)

# Draw the graph using matplotlib and display it
nx.draw(G, with_labels=True)
plt.draw()
plt.show()