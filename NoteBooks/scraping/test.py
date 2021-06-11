import requests
from bs4 import BeautifulSoup
url='https://www.historique-meteo.net/afrique/tunisie/tunis/2017/01/02/'
response=requests.get(url)
if response.ok:
    print("ok")
    soup=BeautifulSoup(response.text,'lxml')
    donnees=soup.find('div', {'class': 'col-md-4 meteo_13h'} )
    p=donnees.find('p')
    etat=p.text
    table=soup.findAll('table', {'class': 'table'})
for td in table:
    donnees=td.findAll('td')
    donnees=td.findAll('td',{'class':'text-center bg-primary'})
    date=donnees[0].text
    temperatureMaximale=donnees[1].text
    temperatureMinimale=donnees[2].text
    vitesseVent=donnees[3].text
    Humidite=donnees[6].text 
    Visibilite=donnees[7].text
                  
    #print("lieu: "+lieu)
    print("etat:"+etat)
    print("date: "+date)
    print("temperatureMaximale: "+temperatureMaximale)
    print("temperatureMinimale: "+temperatureMinimale)
    print("vitesseVent: "+vitesseVent)
    print("Humidite: "+Humidite)
    print("Visibilite: "+Visibilite)
               
             
    

