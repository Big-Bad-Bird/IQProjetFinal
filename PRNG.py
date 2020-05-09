from random import getrandbits
from matplotlib import pyplot

sequence = []
nb_bits = 2**20
for i in range(nb_bits):
    sequence.append(getrandbits(1))

nb_1=sequence.count(1)
r_1=(nb_1/nb_bits)*100
print("frequency of 1:",r_1)

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

spectre=[]
for i in range(1,max(l_speed)+1):
    spectre.append(l_speed.count(i))
print(spectre)
pyplot.bar(range(1,max(l_speed)+1),spectre)
pyplot.title("spectre")
pyplot.xlabel("vitesse d'oscillation")
pyplot.ylabel("nombre d'occurences")
pyplot.show()   
    
