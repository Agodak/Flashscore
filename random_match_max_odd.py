import json
import matplotlib.pyplot as plt

import random

#pariez pe fiecare meci, pe cota cea mai mica
lista_salvari=['meciuri_salvate_{}-{}.txt'.format(i,i+1) for i in range(11,20)]
for j in range(9):
    file=open('text files_corecte/'+lista_salvari[j],'r')
    l_meciuri=json.load(file)
    wins=0
    rezultat=0
    suma_init=3800
    suma_partiala=suma_init
    money=[]
    money.append(suma_init)
    l_meciuri_random=[]
    for i in range(1,39):
        l_temp=[]
        for meci in l_meciuri:
            if int(meci['fixture'])==i:
                l_temp.append(l_meciuri.index(meci))
        alesul=random.choice(l_temp)
        meci_ales=l_meciuri[alesul]
        lista_cote = [float(meci_ales['Unibet'][0]), float(meci_ales['Unibet'][1]), float(meci_ales['Unibet'][2])]
        cota_max = max(float(meci_ales['Unibet'][0]), float(meci_ales['Unibet'][1]), float(meci_ales['Unibet'][2]))
        if int(meci_ales['result'][0]) > int(meci_ales['result'][1]):
            rezultat = 0
        elif int(meci_ales['result'][0]) < int(meci_ales['result'][1]):
            rezultat = 2
        else:
            rezultat = 1
        if lista_cote.index(cota_max) == rezultat:
            suma_partiala = suma_partiala + (cota_max - 1) * 100
            wins = wins + 1
        else:
            suma_partiala = suma_partiala - 100
        money.append(suma_partiala)
    if money[-1]<suma_init:
        text='Loss: '+ str(round((suma_init-money[-1])/suma_init*100,2))+'%'
    else:
        text='Profit: '+ str(round(-(suma_init-money[-1])/suma_init*100,2))+'%'
    plt.figure(figsize=(15,6))
    plt.plot(money)
    plt.title('PL '+str(j+11)+'/'+str(j+12) +'. Maximal odd bet on one random match per fixture')
    plt.xlabel('Number of matches')
    plt.ylabel('Amount of money')

    plt.text(0.8,0.8,'Number of winning bets: '+str(wins) +' out of '+str(38)+'\n'+text,
             horizontalalignment='center',verticalalignment='center',transform=plt.gcf().transFigure)
    plt.xticks(range(0,39,1))
    plt.grid(True)
    plt.savefig('plots_pl/Plot_pl_'+str(j+11)+'-'+str(j+12)+'_maximal_odd_rand_match.png')
    file.close()