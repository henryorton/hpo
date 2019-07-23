import numpy as np
from matplotlib import pyplot as plt


def random_three_vector():
    """
    Generates a random 3D unit vector (direction) with a uniform spherical distribution
    Algo from http://stackoverflow.com/questions/5408276/python-uniform-spherical-distribution
    :return:
    """
    phi = np.random.uniform(0,np.pi*2)
    costheta = np.random.uniform(-1,1)

    theta = np.arccos( costheta )
    x = np.sin( theta) * np.cos( phi )
    y = np.sin( theta) * np.sin( phi )
    z = np.cos( theta )
    return (x,y,z)


B0 = np.array([0.,0.,1.])
csa_tensor = np.diag([-1.0,-3.0,4.0])




dist=[]
for i in range(10000):
	vec = random_three_vector()

	# vec = np.random.uniform(size=3)*2.-1.
	# vec /= np.linalg.norm(vec)
	B_ind = csa_tensor.dot(vec)
	zeeman = B_ind.dot(B_ind)
	dist.append(zeeman)



plt.hist(dist, bins=100)
plt.show()












