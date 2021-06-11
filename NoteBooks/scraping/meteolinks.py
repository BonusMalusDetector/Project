import requests
from bs4 import BeautifulSoup

url='https://www.historique-meteo.net/afrique/tunisie/'
ville=["tunis","zarzis","nabeul","kebili","monastir","bizerte","el-kef","gabes","gafsa","mahdia","sfax","sousse","tatouine","tabarka","tozeur","beja","kairouan","kasserine","rades","sidi-bouzid","zaghouan","siliana","mateur","carthage"]

annee=['2017','2018','2019']
links=[]
for city in ville:   
    for year in annee:
        for i in range(1,13):
            #response=requests.get(url) hedhi karni nehiteha khater tarzen 
            if (i<10):
                url= 'https://www.historique-meteo.net/afrique/tunisie/'+city+'/'+year+'/0'+str(i)
                print(url)
            else:
    	        url= 'https://www.historique-meteo.net/afrique/tunisie/'+city+'/'+year+'/'+str(i)
    	        print(url)
            links.append(url)
with open('urls2.txt','w') as file:
    for link in links:
        file.write(link+'\n')

