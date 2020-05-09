#authors: Hugo Morneau et Alexis Dogin

"""TO DO: commenter le code un peu plus en détail"""

from random import getrandbits
from matplotlib import pyplot

""" Création de la séquence de bits """
sequence = []
nb_bits = 2**10
for i in range(nb_bits):
    sequence.append(getrandbits(1))

""" Calcul de la fréquence de 0 et de 1 """
nb_1=sequence.count(1)
r_1=(nb_1/nb_bits)*100
print("frequency of 1:",r_1)

""" Calcul de la vitesse d'oscillation """
l_speed=[]
cpt=0
while cpt<nb_bits-1:
    startbit=sequence[cpt]
    pos=1
    while startbit==sequence[cpt+pos]:
        pos+=1
        if cpt+pos==nb_bits:
            break
    l_speed.append(pos)
    cpt=cpt+pos

speed=sum(l_speed)/len(l_speed)
print(speed)

""" Calcul du spectre """
spectre=[]
for i in range(1,max(l_speed)+1):
    spectre.append(l_speed.count(i))
pyplot.bar(range(1,max(l_speed)+1),spectre)
pyplot.title("spectre")
pyplot.xlabel("vitesse d'oscillation")
pyplot.ylabel("nombre d'occurences")
#pyplot.show()   

""" Calcul de la plus grande suite de bits répétée dans la séquence """
test=False    
for i in range(nb_bits-1,2,-1):
    print(i)
    for j in range(0,nb_bits-i-1):
        for k in range(j+1,nb_bits-i):
            if sequence[j:j+i]==sequence[k:k+i]:
                seqdupliquee=sequence[j:j+i]
                test=True
                break
        if test:
            break
    if test:
        break

print(seqdupliquee)

nbre=0
for k in range(0,nb_bits-len(seqdupliquee)):
            if seqdupliquee==sequence[k:k+i]:
                nbre+=1

print(nbre)
