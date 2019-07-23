import community
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import json

savedir='D:\\'

def make_graph(sim, labels=None):
    G = nx.Graph()
    for (i, j) in [(i, j) for i in range(sim.shape[0]) for j in range(sim.shape[1]) if i != j and sim[i,j] != 0]:
        if labels == None:
            G.add_edge(i, j, weight=sim[i,j])
        else:
            G.add_edge(labels[i], labels[j], weight=sim[i,j])
    return G
def export_edge_list(sim, labels=None, filename="edges.csv", delim=",", header=True):
    f = open(savedir + filename, 'w')
    if header:
        f.write("Source,Target\n")
    loc = np.where(sim > 0)
    for (i, j) in [(i, j) for (i, j) in zip(loc[0], loc[1]) if i < j]:
        if labels == None:
            f.write(str(i) + delim + str(j) + "\n")
        else:
            f.write("\"" + labels[i] + "\"" + delim + "\"" + labels[j] + "\"\n")
    f.close()

simfilename =  savedir+'B1_result_dissimilarity.csv'
labelfilename = savedir+'labels.tsv' # We will write the labels from dissim.tsv to here

X = np.genfromtxt(simfilename, delimiter=',', encoding='utf8', dtype=None)

index = 0
name = {}
labels=[]
for i in range(0,len(X)):
  if X[i][0] in name:
    name = name
  else:
    name[X[i][0]] = index
    index = index + 1
  if X[i][1] in name:
    name = name
  else:
    name[X[i][1]] = index
    index = index + 1

dismat = np.zeros((index,index))
for i in X:
  a = name[i[0]]
  b = name[i[1]]
  dismat[a][b] = i[2]
  dismat[b][a] = i[2]

new_dict = {v : k for k, v in name.items()}
for i in range(0,len(new_dict)):
  labels.append(new_dict[i])

labels = list(np.array(labels))

threshold = 0.427 # Replace this with your choice of threshold
adjmat = dismat.copy()
np.fill_diagonal(adjmat, np.min(dismat)) # Set the diagonal elements to a small value so that they won't be zeroed out
adjmat = adjmat.reshape((-1,))
adjmat[adjmat > threshold] = 0
print("{} out of {} values set to zero".format(len(adjmat[adjmat == 0]), len(adjmat)))
# adjmat[adjmat > 0] = 1 - adjmat
for i in range(len(adjmat)):
    if adjmat[i] != 0:
        adjmat[i] = 1-adjmat[i]
adjmat = adjmat.reshape(dismat.shape)


G = make_graph(adjmat, labels=labels)

#first compute the best partition
partition = community.best_partition(G)
print(type(partition))



#drawing
size = float(len(set(partition.values())))
pos = nx.spring_layout(G)
count = 0.
for com in set(partition.values()) :
    count = count + 1.
    list_nodes = [nodes for nodes in partition.keys()
                                if partition[nodes] == com]
    nx.draw_networkx_nodes(G, pos, list_nodes, node_size = 40,node_color = str((count ) / size))
nx.draw_networkx_edges(G, pos, alpha=0.5,width=0.1,edge_color='c')
plt.show()