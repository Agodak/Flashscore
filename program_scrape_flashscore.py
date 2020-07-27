from selenium import webdriver
import time
import json

options=webdriver.ChromeOptions()
options.add_argument("--headless")

browser=webdriver.Chrome()
browser.get('https://www.flashscore.ro/fotbal/anglia/premier-league-2019-2020/rezultate/')
buton=browser.find_element_by_class_name('event__more')
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
        time.sleep(3.5)
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
        link='https://www.flashscore.ro/meci/'+meci.get_attribute('id')[4:]+'/#comparare-cote;cote-1x2;final'
        tab_nou.get(link)

        tab_nou.implicitly_wait(10)
        div_home=tab_nou.find_element_by_class_name('home-box')
        div_away=tab_nou.find_element_by_class_name('away-box')
        div_scor=tab_nou.find_element_by_class_name('current-result')
        div_date=tab_nou.find_element_by_class_name('description')

        meciuri_de_salvat[i]['home_team']=div_home.text
        meciuri_de_salvat[i]['away_team']=div_away.text
        meciuri_de_salvat[i]['result']=div_scor.text.split('\n-')
        meciuri_de_salvat[i]['fixture']=div_date.text.split()[5]
        meciuri_de_salvat[i]['date_time']=div_date.text.split()[6], div_date.text.split()[7]

        tab_nou.implicitly_wait(10)
        print(tab_nou.current_url)
        div_tabel=tab_nou.find_element_by_id('odds_1x2')
        l_odd=div_tabel.find_elements_by_class_name('odd')
        l_even=div_tabel.find_elements_by_class_name('even')
        lista_case=l_odd+l_even
        tab_nou.implicitly_wait(10)
        for casa in lista_case:
            meciuri_de_salvat[i][casa.find_element_by_class_name('elink').get_attribute('title')]=casa.text.split()
        tab_nou.quit()
        print('am facut '+str(i)+' meciuri')
        time.sleep(1)
        i += 1
    except:
        print('am ratat meciul: '+str(len(meciuri_de_salvat)))
        continue

file=open('meciuri_salvate_19-20.txt','w')
file.write(json.dumps(meciuri_de_salvat))
file.close()