# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 09:33:20 2020

@author: Tanja Dorst
"""
import glob
import os
import time
import shutil


# Quelle
quelle = "D:\\Messung_Buffer\\"
      
# Ziel (Der Ordner muss auf der Festplatte bereits angelegt sein)
# Statt IP Adresse Ordner einfach einbinden im Explorer
ziel = "Z:\\Achse8_PTB\\Lebensdauer\\"

teildateiname = "achse8_ptb"

def Datenaufzeichnung(start=True):
    i = 0
    while start:
        time.sleep(30)
        moveFiles(quelle, ziel)
        i = i + 1
        print("Verschiebung Nummer " + str(i))    

def moveFiles(quelle,ziel):
    
    # Liste aller Dateien im Quellordner
    data = sorted(os.listdir(quelle))
    
    # Sensorennamen auf PTB Board (nochmal kontrollieren am ZeMA-Prüfstand):
        # BMA_280_0xe0040000
        # MPU_9250_0xe0040100
        # MS5837_02BA_0xe0040300
        # STM32_Internal_ADC_0xe0040a00
    
    # Nur Dateien mit richtigem Namen berücksichtigen und in Liste schreiben
    Achsendaten = []
    for i in range(0,len(data)):
        data_tmp = data[i]
        if teildateiname in data_tmp:
            Achsendaten.append(data_tmp)
        
    # Ist mehr als 1 Dateien in der Liste, dann streiche die beiden letzten 
    # Datei, da diese nicht kopiert werden sollen
    if len(Achsendaten) > 0:
        Achsendaten = Achsendaten[0:-2]
          
    # Kopieren der Dateien   
    for i in range(0,len(Achsendaten)):
        try: 
            # Tipp: for element in mylist[:-1]
            shutil.copy2(quelle+Achsendaten[i], ziel+Achsendaten[i]) 
            print("Kopie hat geklappt: "+Achsendaten[i]) 
            os.remove(quelle+Achsendaten[i]) 
        except: 
            print("Kopie hat nicht geklappt: "+Achsendaten[i]) 
            pass
      
# ZUM TEST: Zurückkopieren
def removeFiles(ziel,quelle):
    data_re = os.listdir(ziel)
    for i in range(0,len(data_re)):
        try: 
            shutil.copy2(ziel+data_re[i], quelle+data_re[i]) 
            print("Kopie hat geklappt: "+data_re[i]) 
            os.remove(ziel+data_re[i]) 
        except: 
            print("Kopie hat nicht geklappt: "+data_re[i]) 
            pass    
        
#Datenaufzeichnung(True)
            
  