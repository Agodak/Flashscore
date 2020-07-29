from selenium import webdriver
import time
import json
from bs4 import BeautifulSoup

options=webdriver.ChromeOptions()
options.add_argument("--headless")

browser=webdriver.Chrome()
browser.implicitly_wait(10)
browser.get('https://www.flashscore.ro/fotbal/anglia/premier-league-2018-2019/rezultate/')
browser.implicitly_wait(10)
buton=browser.find_element_by_class_name('event__more')
browser.implicitly_wait(10)
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
j=1
while True:
    try:
        browser.implicitly_wait(10)
        buton.click()
        browser.implicitly_wait(10)
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        print('am facut '+str(j)+' click-uri')
        j+=1
        time.sleep(5)
    except :
        break

meciuri_de_salvat=[]
meciuri=browser.find_elements_by_class_name("event__match")
if(len(meciuri)!=380):
    print('am failat la viata')
    print('am luat '+str(len(meciuri))+' meciuri')
    browser.quit()
    exit()
else:
    print('am luat tot manca-ti-as')

i=0

for meci in meciuri:
    meciuri_de_salvat.append({})
    browser.implicitly_wait(10)

    try:
        tab_nou=webdriver.Chrome(options=options)
        tab_nou.implicitly_wait(10)
        link='https://www.flashscore.ro/meci/'+meci.get_attribute('id')[4:]+'/#comparare-cote;cote-1x2;final'
        tab_nou.get(link)
        tab_nou.implicitly_wait(10)
        pagina_salvata=tab_nou.page_source
        soup=BeautifulSoup(pagina_salvata,'html.parser')
        div_home=soup.find('div' , class_='home-box')
        div_away=soup.find('div' , class_='away-box')
        div_scor=soup.find('div' , class_='current-result')
        div_date=soup.find('div' , class_='description')

        meciuri_de_salvat[i]['home_team']=div_home.text.split('\n')
        print(meciuri_de_salvat[i]['home_team'])
        meciuri_de_salvat[i]['away_team']=div_away.text.split('\n')
        print(meciuri_de_salvat[i]['away_team'])
        meciuri_de_salvat[i]['result']=div_scor.text.split()
        print(meciuri_de_salvat[i]['result'])
        meciuri_de_salvat[i]['fixture']=div_date.text.split()[5]
        print(meciuri_de_salvat[i]['fixture'])
        meciuri_de_salvat[i]['date_time']=div_date.text.split()[6], div_date.text.split()[7]
        print(meciuri_de_salvat[i]['date_time'])

        div_tabel=soup.find(id='odds_1x2')
        l_odd=div_tabel.find_all('tr',class_='odd')
        l_even=div_tabel.find_all('tr',class_='even')
        lista_case=l_odd+l_even

        for casa in lista_case:
            variabila=casa.find('a' , class_='elink')['title']
            lista=casa.find_all('span',class_='odds-wrap')
            meciuri_de_salvat[i][variabila]=[]
            for cota in lista:
                meciuri_de_salvat[i][variabila].append(cota.text)
            print(variabila)
            print(meciuri_de_salvat[i][variabila])

        tab_nou.quit()
        print('am facut '+str(i)+' meciuri')
        time.sleep(1)
        i += 1

    except:
        print('am ratat meciul: '+str(len(meciuri_de_salvat)))
        continue


file=open('meciuri_salvate_18-19(2).txt','w')
file.write(json.dumps(meciuri_de_salvat))
file.close()
