import numpy as np
from scipy.spatial.distance import squareform


savedir = 'data/'
simfilename = savedir + 'dissim.tsv'
X = np.genfromtxt(simfilename, delimiter='\t', encoding='utf8', dtype=None)
labels = []
for label in [x[0] for x in X]:
    if label in labels:
        continue
    labels.append(label)
for label in [x[1] for x in X]:
    if label in labels:
        continue
    labels.append(label)

dismat = squareform([x[2] for x in X])
np.savetxt(savedir+"dismat.txt",dismat,delimiter=",",fmt="%f")
k = np.loadtxt(savedir+"dismat.txt",delimiter=",",dtype=float)
np.save(savedir+'1',k)
i= np.load(savedir+'1.npy')
print(k)
print(i)
# print(len(dismat[:][0]))
# with open(savedir+'hw_data.csv','a',encoding='utf-8') as f:
#     for i in range(len(labels)):
#         for  j in range(len(labels)):
#             f.write(str(labels[i])+','+str(labels[j])+','+str(dismat[i][j])+'\n')
# print(len(labels))