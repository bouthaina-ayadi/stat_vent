from math import *
import os
import numpy as np

tab_vent = np.loadtxt('vent.txt', dtype=float)
print(tab_vent)
print(tab_vent.shape)
print(tab_vent.size)
stat = tab_vent[:,3: ]
def Question2(t): #pour dataset
    print('vitesse minimal est:', t.min(), "vitesse max:", t.max(), "vitesse moyenne: ", t.mean(),"l'ecart type est: ", t.std() )

q2 = Question2(stat)
print(q2)

def Question3(t): # pour chaque emplacement
    l1, l2, l3, l4 = [], [], [], []
    
    for i in range(12):
       l1.append(t[: , i].min())
       l2.append(t[:, i].max())
       l3.append(t[:, i].mean())
       l4.append(t[:, i].std())
    yield l1 
    yield l2
    yield l3
    yield l4
    
    
li1, li2, li3, li4 = Question3(stat)
print("le vent minimal pour chaque emplacement:" '\n', li1,'\n', "le vent max est: ", '\n', li2,'\n', "la moyenne est: ", '\n', li3, '\n', "l'ecart type est: ", '\n', li4 )       

def Question4(t): # pour chaque jour
    c1, c2, c3, c4 = [], [], [], []
   
    for j in range(3):
        c1.append(t[j, :].min())
        c2.append(t[j, :].max())
        c3.append(t[j, :].mean())
        c4.append(t[j, :].std())
    yield c1
    yield c2
    yield c3
    yield c4
   
ci1, ci2, ci3, ci4 = Question4(stat)
print("le vent minimal pour chaque jour:" '\n', ci1,'\n', "le vent max est: ", '\n', ci2,'\n', "la moyenne est: ", '\n', ci3, '\n', "l'ecart type est: ", '\n', ci4 )       


#Question 5: l'endroit où la vitesse du vent est la plus élevée chaque jour.

print("l'endroit ou la vitesse du vent est la plus élevée chaque jour est: ", max(li2))

#question 6: l'année, le mois et le jour où la vitesse du vent la plus élevée a été enregistrée
print("l'année, le mois et le jour où la vitesse du vent la plus élevée a été enregistrée est:", )
 
#Question 7

def Question7(t):
    m, r= [], []
    
    for i in range(12):
       m.append(t[: , i].sqrt())
       
           
      
    yield m
    


        

