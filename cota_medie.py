import json
import matplotlib.pyplot as plt

#pariez pe fiecare meci, pe cota cea mai mica
lista_salvari=['meciuri_salvate_{}-{}.txt'.format(i,i+1) for i in range(11,20)]
for j in range(9):
    file=open('text files_corecte/'+lista_salvari[j],'r')
    l_meciuri=json.load(file)
    wins=0
    rezultat=0
    suma_init=38000
    suma_partiala=suma_init
    money=[]
    money.append(suma_init)
    for i in range(1,39):
        for meci in l_meciuri:
            if int(meci['fixture'])==i:
                lista_cote=[float(meci['Unibet'][0]),float(meci['Unibet'][1]),float(meci['Unibet'][2])]
                a,b,c=float(meci['Unibet'][0]),float(meci['Unibet'][1]),float(meci['Unibet'][2])
                if a<b:
                    if c<a:
                        cota_medie=a
                    elif c<b:
                        cota_medie=c
                    else:
                        cota_medie=b
                else:
                    if c<b:
                        cota_medie=b
                    elif c<a:
                        cota_medie=c
                    else:
                        cota_medie=a
                if int(meci['result'][0])>int(meci['result'][1]):
                    rezultat=0
                elif int(meci['result'][0])<int(meci['result'][1]):
                    rezultat=2
                else:
                    rezultat=1
                if lista_cote.index(cota_medie)==rezultat:
                    suma_partiala=suma_partiala+(cota_medie-1)*100
                    wins=wins+1
                else:
                    suma_partiala=suma_partiala-100
                money.append(suma_partiala)
    if money[-1]<suma_init:
        text='Loss: '+ str(round((suma_init-money[-1])/suma_init*100,2))+'%'
    else:
        text='Profit: '+ str(round(-(suma_init-money[-1])/suma_init*100,2))+'%'
    plt.figure(figsize=(15,6))
    plt.plot(money)
    plt.title('PL '+str(j+11)+'/'+str(j+12) +'. Middle odd bet on every match')
    plt.xlabel('Number of matches')
    plt.ylabel('Amount of money')

    plt.text(0.8,0.8,'Number of winning bets: '+str(wins) +' out of '+str(len(l_meciuri))+'\n'+text,
             horizontalalignment='center',verticalalignment='center',transform=plt.gcf().transFigure)
    plt.xticks(range(0,390,10))
    plt.grid(True)
    plt.savefig('plots_pl/Plot_pl_'+str(j+11)+'-'+str(j+12)+'_middle_odd.png')
    file.close()