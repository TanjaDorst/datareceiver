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
quelle = ".\\Achse8_PTB\\"
      
# Ziel (Der Ordner muss auf der Festplatte bereits angelegt sein)
# Statt IP Adresse Ordner einfach einbinden im Explorer
ziel = "Z:\\Achse8_PTB\\PTB_Board\\"

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
    
    # Jedem Sensor eine Liste seiner Dateien zuordnen
    BMA = []
    MPU = []
    MS5837 = []
    STM32 = []
    for i in range(0,len(data)):
        data_tmp = data[i]
        if "BMA" in data_tmp:
            BMA.append(data_tmp)
        elif "MPU" in data_tmp:
            MPU.append(data_tmp)
        elif "MS5837" in data_tmp:
            MS5837.append(data_tmp)
        elif "STM32" in data_tmp:
            STM32.append(data_tmp)  
        
    # Ist mehr als 1 Dateien in der Liste, dann streiche die beiden letzten 
    # Datei, da diese nicht kopiert werden sollen
    if len(BMA) > 0:
        BMA = BMA[0:-2]
    if len(MPU) > 0:
        MPU = MPU[0:-2]
    if len(MS5837) > 0:
        MS5837 = MS5837[0:-2]
    if len(STM32) > 0:
        STM32 = STM32[0:-2]
         
    # Kopieren der Dateien vom BMA Sensor    
    for i in range(0,len(BMA)):
        try: 
            # Tipp: for element in mylist[:-1]
            shutil.copy2(quelle+BMA[i], ziel+BMA[i]) 
            print("Kopie hat geklappt: "+BMA[i]) 
            os.remove(quelle+BMA[i]) 
        except: 
            print("Kopie hat nicht geklappt: "+BMA[i]) 
            pass
        
    # Kopieren der Dateien vom MPU Sensor    
    for i in range(0,len(MPU)):
        try: 
            shutil.copy2(quelle+MPU[i], ziel+MPU[i]) 
            print("Kopie hat geklappt: "+MPU[i]) 
            os.remove(quelle+MPU[i]) 
        except: 
            print("Kopie hat nicht geklappt: "+MPU[i]) 
            pass
    
    # Kopieren der Dateien vom MS5837 Sensor        
    for i in range(0,len(MS5837)):
        try: 
            shutil.copy2(quelle+MS5837[i], ziel+MS5837[i]) 
            print("Kopie hat geklappt: "+MS5837[i]) 
            os.remove(quelle+MS5837[i]) 
        except: 
            print("Kopie hat nicht geklappt: "+MS5837[i]) 
            pass
    
    # Kopieren der Dateien vom STM32 Sensor     
    for i in range(0,len(STM32)):
        try: 
            shutil.copy2(quelle+STM32[i], ziel+STM32[i]) 
            print("Kopie hat geklappt: "+STM32[i]) 
            os.remove(quelle+STM32[i]) 
        except: 
            print("Kopie hat nicht geklappt: "+STM32[i]) 
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
            
  