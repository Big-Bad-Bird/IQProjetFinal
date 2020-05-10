#Auteurs: Hugo Morneau et Alexis Dogin


""" On importe les bibliothèques necéssaires """

from random import getrandbits
from matplotlib import pyplot


""" Création de la séquence de bits """

sequence = []
nb_bits = 2**20  #Pour la dernière partie du programme, il est préférable 2**10 pour avoir un temps d'execution correct avec un nombre de bits significatif.
for i in range(nb_bits):
    sequence.append(getrandbits(1))  #On utilise getrandbits pour générer un bit à 0 ou à 1 et on l'ajoute à la séquence.


""" Calcul de la fréquence de 0 et de 1 """

nb_1=sequence.count(1)  #On compte le nombre de 1 dans la séquence
r_1=(nb_1/nb_bits)*100  #On calcule le pourcentage de 1
print("Frequency of 0:",100-r_1,"%")
print("Frequency of 1:",r_1,"%")


""" Calcul de la vitesse d'oscillation """

l_speed=[]
cpt=0
while cpt<nb_bits-1:  #On se déplace sur la liste grâce au pointeur cpt
    startbit=sequence[cpt]
    pos=1
    while startbit==sequence[cpt+pos]:  #Tant que le bit suivant à la même valeur que le bit sur lequel on travaille, on avance dans la liste
        pos+=1
        if cpt+pos==nb_bits:  #On s'arrete quand on est à la fin de la séquence
            break
    l_speed.append(pos)  #On récupère le nombre de bits à la suite de même valeur
    cpt=cpt+pos  #A chaque changement de valeur, on rénitialise le pointeur de la liste sur le premier bit différent

speed=sum(l_speed)/len(l_speed)  #On calcule la vitesse moyenne d'oscillation
print("Vitesse d'oscillation:",speed)


""" Calcul du spectre """

spectre=[]  
for i in range(1,max(l_speed)+1):  #On réutilise la liste de la partie d'avant
    spectre.append(l_speed.count(i)) 
pyplot.bar(range(1,max(l_speed)+1),spectre)  #On trace l'histogramme des vitesses d'oscillation
pyplot.title("spectre")
pyplot.xlabel("vitesse d'oscillation")
pyplot.ylabel("nombre d'occurences")
pyplot.show()


""" Calcul de la plus grande suite de bits répétée dans la séquence """

test=False    
for i in range(nb_bits-1,2,-1): #On parcourt toutes les tailles de séquences, de la plus grande à la plus petite
    #print("Nombre de bits par séquence:",i) #permet de suivre en direct le traitement
    for j in range(0,nb_bits-i-1):  #On prend une première suite de bits de la taille voulue que l'on va comparer avec toutes les suites suivantes
        for k in range(j+1,nb_bits-i):  #On prend une seconde suite placée juste derrière la première suite
            if sequence[j:j+i]==sequence[k:k+i]:  #On compare les deux suites
                seqdupliquee=sequence[j:j+i]  #Si elles sont égales, alors on les récupère dans une liste et on sort de la boucle
                test=True
                break  #Sinon on continue avec la suite suivante jusqu'à la fin de la séuqence
        if test: 
            break  #Si on a rien trouvé pour la première suite, on continue avec la suivante
    if test:
        break  #Si on a rien trouvé, on passe à la taille inférieure



nbre=0
for k in range(0,nb_bits-len(seqdupliquee)): #On compte le nombre de fois que la suite apparait dans la séquence (au moins 2)
            if seqdupliquee==sequence[k:k+i]:
                nbre+=1

print("Suite de bits dupliquée dans la séquence:",seqdupliquee)
print("Taille de la suite:",len(seqdupliquee))
print("Nombre de fois que la suite apparait dans la séquence",nbre)

