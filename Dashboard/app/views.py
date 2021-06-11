# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
import joblib
import pandas as pd
import numpy as np


@login_required(login_url="/login/")
def index(request):

    
    context = {}
    context['segment'] = 'index'
    
    
    
    
    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    context = {}
    

    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        
        
        context['segment'] = load_template
        FP=0
        USE=0
        GROUP=0
        NaturePolice=0
        EXP=0
        TypePolice=0
        EtatPolice=0
        TypeIntermidaire=0
        ENERGIE=0
        VRT=0
        TEMP=0
        VENT=0
        humidite=0
        Visibilite=0
        Precipitations=0
        DATE=0
        Location=0
        STATE=0
        DATESS=0
        DATEEP=0
        Responsablite=0
        HeureSS=0
        LieuSinistre=0
        BMC=0
        NatureSinistre=0
        GROUP_CAR=""
        context["y"]=-1

        if (load_template=="ui-typography.html"):
            if "FP" in request.GET:
                FP=request.GET["FP"] 
            if "USE" in request.GET:
                USE=request.GET["USE"]  
            if "GROUP" in request.GET:
                GROUP=request.GET["GROUP"] 
            if "EXP" in request.GET:
                EXP=request.GET["EXP"]   
            if "NaturePolice" in request.GET:
                NaturePolice=request.GET["NaturePolice"]  
            if "TypePolice" in request.GET:
                TypePolice=request.GET["TypePolice"] 
            if "EtatPolice" in request.GET:
                EtatPolice=request.GET["EtatPolice"] 
            if "TypeIntermidaire" in request.GET:
                TypeIntermidaire=request.GET["TypeIntermidaire"]  
            if "ENERGIE" in request.GET:
                ENERGIE=request.GET["ENERGIE"]  
            if "VRT" in request.GET:
                VRT=request.GET["VRT"]
            

        
            value=""
            list_Usage={1:'Autres_Usage',2:'Privé et professionnel',3:'Taxi',4:'Transport public de marchandise (avec matière dangereuse et inflammable)',5:'Utilitaire 1 véhicule dont le PTC < 3500 kg (y compris usage voirie)',6:'Utilitaire 2 véhicule dont le PTC > 3500 kg (y compris voirie)'}
            list_group={1:'BMW',2:'DAIMLER',3:'FORD',4:'GENERAL_MOTORS',5:'HYUNDAI',6:'ISUZU',7:'MAZDA',8:'RenaultNissanMitsubishi',9:'STELLLANTIS',10:'TOYOTA',11:'VOLKSWAGEN_AG'}
            list_VRT={1:'RS',2:'TRAC',3:'TU'}
            list_energie={1:'ESSENCE',2:'GASOIL'}
            list_EtatPolice={1:'S',2:'V'}

            
            
            data = { 'BMW': [0],'DAIMLER': [0], 'FORD': [0],"GENERAL_MOTORS":[0],'HYUNDAI': [0], 'ISUZU': [0],'MAZDA': [0], 'RenaultNissanMitsubishi': [0],'STELLLANTIS': [0], 'TOYOTA': [0],'VOLKSWAGEN_AG': [0], 'RS': [0],'TRAC': [0], 'TU': [0],'Autres_Usage': [0], 'Privé et professionnel': [0],'Taxi':[0],'Transport public de marchandise (avec matière dangereuse et inflammable)': [0], 'Utilitaire 1 véhicule dont le PTC < 3500 kg (y compris usage voirie)': [0],'Utilitaire 2 véhicule dont le PTC > 3500 kg (y compris voirie)':[0],'ESSENCE':[0],'GASOIL':[0],'S':[0],'V':[0],'typeIntermediaire':[0],'naturePolice':[0],'typePolice':[0],'puissanceFiscal':[0],'Experience':[0]}  
            
            # Create DataFrame           
            df = pd.DataFrame(data) 
            if(int(USE)!=0):
                df[list_Usage.get(int(USE))]=1
            if(int(GROUP)!=0):
                df[list_group.get(int(GROUP))]=1
            if(int(VRT)!=0):   
                df[list_VRT.get(int(VRT))]=1
            if(int(ENERGIE)!=0):   
                df[list_energie.get(int(ENERGIE))]=1
            if(int(EtatPolice)!=0):
                df[list_EtatPolice.get(int(EtatPolice))]=1
            df["puissanceFiscal"]=int(FP)
            df["naturePolice"]=int(NaturePolice)
            if(int(EtatPolice)!=0):
                df["typePolice"]=int(TypePolice)
            df["typeIntermediaire"]=int(TypeIntermidaire)
        
            if(int(EXP)!=0):
                df["Experience"]=int(EXP)
        
            #SC=joblib.load("StandardScaler.sav")
            model=joblib.load("model.sav")
            ans=""
            if(~(df.values.sum()==0) ):               
                ans=model.predict(df.values)
                
                
            value=str(ans)                    
            context["ans"]=value
        if (load_template=="ui-icons.html"):
            if "TEMP" in request.GET:
                TEMP=request.GET["TEMP"] 
            if "VENT" in request.GET:
                VENT=request.GET["VENT"]  
            if "humidite" in request.GET:
                humidite=request.GET["humidite"] 
            if "Visibilite" in request.GET:
                Visibilite=request.GET["Visibilite"]   
            if "Precipitations" in request.GET:
                Precipitations=request.GET["Precipitations"]  
            if "DATE" in request.GET:
                DATE=request.GET["DATE"] 
            if "Location" in request.GET:
                Location=request.GET["Location"] 
            if "STATE" in request.GET:
                STATE=request.GET["STATE"]
            data = { 'temperature': [0],'vitesseVent': [0], 'Humidite': [0],"Visibilite":[0],'Precipitations': [0], 'lieu_encode': [0],'etat_encode': [0], 'annee': [0],'mois': [0], 'jour': [0]}  
            # Create DataFrame  
            df = pd.DataFrame(data)
            li=[]
            li.append(str(STATE))
            li_location=[]
            li_location.append(str(Location))

            
            WeatherEncoder=joblib.load("weather_Encoder.sav")
            LocationEncoder=joblib.load("Location_Encoder.sav")
            if "STATE" in request.GET:
                STATE=WeatherEncoder.transform(li)[0]

            if "Location" in request.GET:
                Location=LocationEncoder.transform(li_location)[0]
        
            
            df["temperature"]=int(TEMP)
            df["vitesseVent"]=int(VENT)
            df["Humidite"]=int(humidite)
            df["Visibilite"]=int(Visibilite)
            df["Precipitations"]=int(Precipitations)
            df["lieu_encode"]=Location
            df["etat_encode"]=STATE

            if "DATE" in request.GET:
                df['annee']=int(DATE[0:4])
                df['mois']=int(DATE[5:7])
                df['jour']=int(DATE[8:10])
            
            
            LGBM=joblib.load("LGBM.sav")
            ans=LGBM.predict(df.values)
            
            y=np.round(int(ans[0]))
            
            if(y<0):
                y=0            
            if (request.GET):
                context["y"]=y
        if (load_template=="ui-maps.html"):
            if "DATESS" in request.GET:
                DATESS=request.GET["DATESS"] 
            if "DATEEP" in request.GET:
                DATEEP=request.GET["DATEEP"]  
            if "Responsablite" in request.GET:
                Responsablite=request.GET["Responsablite"] 
            if "HeureSS" in request.GET:
                HeureSS=request.GET["HeureSS"]   
            if "LieuSinistre" in request.GET:
                LieuSinistre=request.GET["LieuSinistre"]  
            if "BMC" in request.GET:
                BMC=request.GET["BMC"] 
            if "USE" in request.GET:
                USE=request.GET["USE"] 
            if "GROUP_CAR" in request.GET:
                GROUP_CAR=request.GET["GROUP_CAR"]  
            if "EtatPolice" in request.GET:
                EtatPolice=request.GET["EtatPolice"]  
            if "TypePolice" in request.GET:
                TypePolice=request.GET["TypePolice"]
            if "NaturePolice" in request.GET:
                NaturePolice=request.GET["NaturePolice"]
            if "NatureSinistre" in request.GET:
                NatureSinistre=request.GET["NatureSinistre"]
            data = { 'pourcentadeDeResponsabilite': [0],'natureDuSinistre': [0], 'lieuDuSinistreajuste': [0],"heureSurvanceDusinistreajuste":[0],'Usage': [0], 'naturePolice': [0],'typePolice': [0], 'Etat_Police': [0],'classeBonusMalus': [0], 'groupe': [0], 'annee_Suervenace': [0], 'mois_Suervenace': [0], 'annee_EffetPolice': [0], 'mois_EffetPolice': [0]}  
            # Create DataFrame  
            df = pd.DataFrame(data)
            li_car=[]
            li_car.append(str(GROUP_CAR))

            Car_Encoder=joblib.load("GroupCarsEncoder.sav")
            if "GROUP_CAR" in request.GET:
                GROUP_CAR=Car_Encoder.transform(li_car)[0]
            
            df["pourcentadeDeResponsabilite"]=int(Responsablite)
            df["natureDuSinistre"]=int(NatureSinistre)
            df["lieuDuSinistreajuste"]=int(LieuSinistre)
            df["heureSurvanceDusinistreajuste"]=int(HeureSS)
            df["Usage"]=int(USE)
            df["naturePolice"]=int(NaturePolice)
            df["typePolice"]=int(TypePolice)
            df["Etat_Police"]=int(EtatPolice)
            df["typePolice"]=int(TypePolice)
            df["classeBonusMalus"]=int(BMC)
            df["groupe"]=GROUP_CAR

            if "DATESS" in request.GET:
                df['annee_Suervenace']=int(DATESS[0:4])
                df['mois_Suervenace']=int(DATESS[5:7])
            
            if "DATEEP" in request.GET:
                df['annee_EffetPolice']=int(DATEEP[0:4])
                df['mois_EffetPolice']=int(DATEEP[5:7])   
            
                model=joblib.load("FraudeModel.sav")
                ans=model.predict(df)
                value=str(ans)  
                context["ans"]=value
            
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))
"""
def typography(request):

    
    context = {}
    context['segment'] = 'typography'
    
    
    LGBM=joblib.load("model.sav")
    X=[3.91,-0.208,-0.302 ,-0.233,-0.227,-0.209,-0.15 ,-0.44 ,-0.511,-0.2473 ,-0.401,-0.406,5.73,-2.024,2.57 ,-1.06 ,-0.23,-0.17,-0.403 ,-0.256,-0.71, 0.73,-0.19,  0.68,-0.81, -0.27,-0.18,-1.171, 4.35]
  

    ans=LGBM.predict([X])

    #context['FP']=request.GET["FP"]
    #context['USE']=request.GET["USE"]

    
    html_template = loader.get_template('ui-typography.html')
    
    return HttpResponse(html_template.render(context, request))
"""


