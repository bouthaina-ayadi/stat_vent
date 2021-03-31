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
print(f' vitesse min: {stat.min(axis=0)}, vitesse max: {stat.max(axis=0)}, vitesse moyenne est: {stat.mean(axis=0)}, l"écart type est: {stat.std(axis=0)} ')

#pour chaque jour
print(f' vitesse min: {stat.min(axis=1)}, vitesse max: {stat.max(axis=1)}, vitesse moyenne est: {stat.mean(axis=1)}, l"écart type est: {stat.std(axis=1)} ')

#Question 5: l'endroit où la vitesse du vent est la plus élevée chaque jour.
print(stat.argmax(axis=1))

#question 6: l'année, le mois et le jour où la vitesse du vent la plus élevée a été enregistrée
# max par jour
s= stat.max(axis=1)
# Trouver l'indice du jour ayant la valeur max
indice=s.argmax()
# Chercher l'année, le mois et le jour depuis le dataset original
print(tab_vent[indice,:3])
 
#la vitesse moyenne du vent en janvier pour chaque lieu.
indices_janvier = tab_vent[:,1]==1
print(indices_janvier)
print(stat[indices_janvier].mean(axis=0))






    


        

