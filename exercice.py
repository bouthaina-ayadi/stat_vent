from math import *
from random import *
import numpy as np

tab_vent = np.loadtxt('vent.txt', dtype=float)
print(tab_vent)
print(tab_vent.shape)
print(tab_vent.size)
stat = tab_vent[:,3: ]
def Question2(): #pour chaque dataset
    print('vitesse minimal est:', stat.min(), "vitesse max:", stat.max(), "vitesse moyenne: ", stat.mean(),"l'ecart type est: ", stat.std() )

q2 = Question2()
print(q2)
def Question3(): # pour chaque enmplacement
    l1= []
    l2 = []
    l3= []
    l4= []
    for i in range(12):
       l1.append(stat[: , i].min())
       l2.append(stat[:, i].max())
       l3.append(stat[:, i].mean())
       l4.append(stat[:, i].std())
    print("le vent minimal pour chaque emplacement:" '\n', l1,'\n', "le vent max est: ", '\n', l2,'\n', "la moyenne est: ", '\n', '\n', l3, '\n', "l'ecart type est: ", '\n', l4 )       

q3 = Question3()
print(q3)

def Question4(): # pour chaque jour
    c1 = []
    c2 = []
    c3 = []
    c4 = []
    for j in range(3):
        c1.append(stat[j, :].min())
        c2.append(stat[j, :].max())
        c3.append(stat[j, :].mean())
        c4.append(stat[j, :].std())
    print("le vent min pour chaque jour:" '\n', c1,'\n', "le vent max est: ", '\n', c2,'\n', "la moyenne est: ", '\n', '\n', c3, '\n', "l'ecart type est: ", '\n', c4 )       
   
q4 = Question4()
print(q4)

a1 = tab_vent[:,0:3]
print(a1)

print(stat.max(axis=1))





        

