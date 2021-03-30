from math import *
import os
import numpy as np

tab_vent = np.loadtxt('wind.data', dtype=float)
print(tab_vent)
print ( tab_vent.shape)
print(tab_vent.size)
stat = tab_vent[:,3: ]
stat_size = stat.shape
def dataset(t): #pour dataset
    print('vitesse minimal est:', t.min(), "vitesse max:", t.max(), "vitesse moyenne: ", t.mean(),"l'ecart type est: ", t.std() )

dataset(stat)


def place(t, l1, l2, l3, l4): # pour chaque emplacement
    
    for i in range(stat_size[1]):
       l1.append(t[: , i].min())
       l2.append(t[:, i].max())
       l3.append(t[:, i].mean())
       l4.append(t[:, i].std())
    
    
li1, li2, li3, li4  = [], [], [], []   
place(stat,li1, li2, li3, li4 )
print("le vent minimal pour chaque emplacement:" '\n', li1,'\n', "le vent max est: ", '\n', li2,'\n', "la moyenne est: ", '\n', li3, '\n', "l'ecart type est: ", '\n', li4 )       

def everyDay(t, c1, c2, c3, c4): # pour chaque jour
    
    for j in range(stat_size[0]):
        c1.append(t[j, :].min())
        c2.append(t[j, :].max())
        c3.append(t[j, :].mean())
        c4.append(t[j, :].std())
   
ci1, ci2, ci3, ci4  = [], [], [], []
everyDay(stat, ci1, ci2, ci3, ci4)
print("le vent minimal pour chaque jour:" '\n', ci1,'\n', "le vent max est: ", '\n', ci2,'\n', "la moyenne est: ", '\n', ci3, '\n', "l'ecart type est: ", '\n', ci4 )       


#Question 5: l'endroit où la vitesse du vent est la plus élevée chaque jour.
tab_size = tab_vent.shape
def Q5(tab):
    for k in range (tab_size[0]):

        print("le vitesse le plus élevée le",tab_vent[k:,2:], "/", tab_vent[k:,1:], "/", tab_vent[k:,0:], "est : ", tab_vent[k:,:].max())

Q5(tab_vent)
#question 6: l'année, le mois et le jour où la vitesse du vent la plus élevée a été enregistrée

print("l'année, le mois et le jour où la vitesse du vent la plus élevée a été enregistrée est:", )
 
#Question 7


    


        

