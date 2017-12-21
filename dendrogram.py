from numpy import *
import scipy
import scipy.cluster.hierarchy as sch
import matplotlib.pylab as plt

X=loadtxt('cluster_test.txt')

# N = len(X)
# d = zeros((N,N))
# 
# for i in range(N):
# 	for j in range(i+1, N):
# 		d[j, i] = d[i, j] = (sum((X[i, :]-X[j, :])**2))**0.5

d = sch.distance.pdist(X)

print(d.shape, X.shape)

Z = sch.linkage(d, method='complete')

P = sch.dendrogram(Z, orientation='right')

plt.show()
# plt.savefig('plot_dendrogram.png')

T = sch.fcluster(Z, 0.5*d.max(), 'distance')

sch.leaders(Z,T)
