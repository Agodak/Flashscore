import json
import os

file = open('meciuri_salvate.txt', "r")
file_prost = file.read()
i = 0
j = 0

while file_prost.find("{", i) != -1 :
    file_intermediar = open('meci_' + str(j) + '.txt', 'w')
    file_intermediar.write(file_prost[file_prost.find("{", i):file_prost.find("}", i+1) + 1])
    file_intermediar.close()
    i = file_prost.find("}", i+1)
    print(i)
    j = j + 1
