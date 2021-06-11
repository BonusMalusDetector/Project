import requests
from bs4 import BeautifulSoup
url='https://www.historique-meteo.net/afrique/tunisie/tunis/2017/01/'
#response=requests.get(url)
liens=[]
with open('urls2.txt','r') as file:
    with open('weadher_djerba.csv','w') as outf:
        outf.write('lieu,date,temperatureMaximale,temperatureMinimale,vitesseVent,Humidite,Visibilite,etat,ajuste\n')
        for row in file:
            print(row)
            url=row.strip()
            response=requests.get(url)   
            if response.ok:
                print("ok")
                soup=BeautifulSoup(response.text,'lxml')
    #title=soup.find('title')
                div=soup.find('div', {'class': 'col-lg-12'})
                a=div.findAll('a')
                lieu=a[3].text
                tables=soup.findAll('table', {'class': 'table table-striped'})
                for td in tables:
                    liens=td.findAll('a')
            
                    for link in liens:
                        url=link["href"]
                        print(url)
                        response=requests.get(url)
                        if response.ok:
                            print("ok")
                            soup=BeautifulSoup(response.text,'lxml')
                            donnees=soup.find('div', {'class': 'col-md-4 meteo_13h'} )
                            p=donnees.find('p')
                            etat=p.text.replace(',',' ')
                            table=soup.findAll('table', {'class': 'table'})
                            for td in table:
                                donnees=td.findAll('td',{'class':'text-center bg-primary'})
                                date=donnees[0].text
                                temperatureMaximale=donnees[1].text
                                temperatureMinimale=donnees[2].text
                                vitesseVent=donnees[3].text
                                ajuste=donnees[5].text
                                Humidite=donnees[6].text 
                                Visibilite=donnees[7].text
                                outf.write(lieu+','+date+','+temperatureMaximale+','+temperatureMinimale+','+vitesseVent+','+Humidite+','+Visibilite+','+ etat+','+ajuste+'\n')

                        
                         
                        """
                            print("etat: "+etat)                        
                            print("lieu: "+lieu)
            
                            print("date: "+date)
                            print("temperatureMaximale: "+temperatureMaximale)
                            print("temperatureMinimale: "+temperatureMinimale)
                            print("vitesseVent: "+vitesseVent)
                            print("Humidite: "+Humidite)
                            print("Visibilite: "+Visibilite)
             """
               
             
    

