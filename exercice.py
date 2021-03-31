from math import *
import os
import numpy as np

tab_vent = np.loadtxt('wind.data', dtype=float)
print(tab_vent)
print ( tab_vent.shape)
print(tab_vent.size)
stat = tab_vent[:,3: ]
stat_size = stat.shape

#pour dataset
print(f'le vent mx est:{stat.max()}, le vent min est :{stat.min()}, la moyenne est: {stat.mean()}, et l ecart type est {stat.std()}')

#pour chaque emplacement




#Question 5: l'endroit où la vitesse du vent est la plus élevée chaque jour.

#question 6: l'année, le mois et le jour où la vitesse du vent la plus élevée a été enregistrée

print("l'année, le mois et le jour où la vitesse du vent la plus élevée a été enregistrée est:", )
 
#Question 7


    


        

