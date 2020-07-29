import json
import matplotlib.pyplot as plt

#pariez pe fiecare meci, pe cota cea mai mica


file=open('text files_corecte/meciuri_salvate_15-16.txt','r')
l_meciuri=json.load(file)
rezultat=0
suma_init=38000
suma_partiala=suma_init
money=[]
money.append(suma_init)
for i in range(1,39):
    for meci in l_meciuri:
        if int(meci['fixture'])==i:
            lista_cote=[float(meci['Unibet'][0]),float(meci['Unibet'][1]),float(meci['Unibet'][2])]
            cota_minima=min(float(meci['Unibet'][0]),float(meci['Unibet'][1]),float(meci['Unibet'][2]))
            if int(meci['result'][0])>int(meci['result'][1]):
                rezultat=0
            elif int(meci['result'][0])<int(meci['result'][1]):
                rezultat=2
            else:
                rezultat=1
            if lista_cote.index(cota_minima)==rezultat:
                suma_partiala=suma_partiala+(cota_minima-1)*100
            else:
                suma_partiala=suma_partiala-100
            money.append(suma_partiala)

plt.plot(money)
plt.show()