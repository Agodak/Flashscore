import json

lista_meciuri = []
for i in range(0, 380):
    with open('meci_' + str(i) + '.txt') as f:
        lista_meciuri.append(json.load(f))
file=open('meciuri_salvate_corect.txt','w')
file.write(json.dumps(lista_meciuri))
file.close()