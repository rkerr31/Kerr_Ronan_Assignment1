
# coding: utf-8

# In[17]:

import numpy as np

def fact(num):
    res=1
    for i in xrange(num):
        res=res*(i+1)
    return res

def binco(n, k):
    return fact(n)/(fact(k)*fact(n-k))

def pascrow(n):
    k=0
    paslst=[]
    for i in xrange(n+1):
        paslst.append(binco(n, k))
        k=k+1
    return paslst

def pasctri(n):
    nn=0
    pascarr=[]
    for i in xrange(n+1):
        pascarr.append(pascrow(nn))
        nn=nn+1
    return pascarr
print pasctri(20) #prints all pascal's triangle rows up until n=20


# In[18]:

def P(p,n,k):
    return binco(n,k)*(p**k)*((1-p)**(n-k))

def Pthresh(p,n,k):
    pt=0
    for i in np.linspace(k,n,(n-k+1)):
        pt=pt+P(p,n,int(i))
    return pt



# In[ ]:

import numpy.random as random
import matplotlib.pyplot as plt

random.rand()

def Numsuc(N, p, n, k): #number of runs of experiment, probability of success per run, number of runs, number wanted
    numsuctot=0
    for i in xrange(int(N)):
        success=0
        for i in xrange(n):
            if (random.rand()<=p):
                success=success+1
        if success>=k:
            numsuctot=numsuctot+1
    return numsuctot

print Numsuc(1000, 0.25, 4, 1)
print Pthresh(0.25, 4,1)

Ns=np.linspace(100, 10000, (10000-100+1))

y=[]
for i in xrange(len(Ns)):
    y.append(Numsuc(Ns[i], 0.25, 4, 1))

plt.plot(Ns, y, 'r+')


