import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium import webdriver
import numbers
import pandas as pd
import time
import re as regex


class covid:
    lodp_aktif = [] #A
    lodp_meninggal = [0] #B
    lodp_sembuh = [] #C
    lpdp_aktif = [] #D
    lpdp_meninggal = [] #E
    lpdp_sembuh = [] #F
    lpositif_aktif = [] #G
    lpositif_meninggal = [0] #H
    lpositif_sembuh = [] #I

    def covid_Selenium (site):

        site = site
        #hdr = {'user-agent' : 'GoogleChrome'}
        driver = webdriver.Chrome(r"D:\New folder\chrome driver\chromedriver.exe")

        driver.get(site)
        driver.implicitly_wait(10)


        odp_aktif = driver.find_elements_by_xpath('//*[@id="data"]/div/div/div[1]/div[1]/div[1]/div/p')
        for data in odp_aktif:
            odp_aktif = data.text
            odp_aktif = int(odp_aktif.rstrip())
            covid.lodp_aktif.append(odp_aktif)

        #odp_meninggal = driver.find_elements_by_xpath('')
        #for data in odp_meninggal:
          #  odp_meninggal = data.text
          #  odp_meninggal = int(odp_meninggal.rstrip())
          #  covid_magelang.lodp_meninggal.append(odp_meninggal)


        odp_sembuh = driver.find_elements_by_xpath('//*[@id="data"]/div/div/div[1]/div[1]/div[2]/span[3]/b')
        for data in odp_sembuh :
            odp_sembuh = data.text
            odp_sembuh = int(odp_sembuh.rstrip())
            covid.lodp_sembuh.append(odp_sembuh)

        pdp_aktif_rawat = driver.find_elements_by_xpath('//*[@id="data"]/div/div/div[1]/div[3]/div[1]/div/p')
        for data in pdp_aktif_rawat:
            pdp_aktif_rawat = data.text
            pdp_aktif_rawat = int(pdp_aktif_rawat.rstrip())
            covid.lpdp_aktif.append(pdp_aktif_rawat)

        pdp_aktif_rujuk = driver.find_elements_by_xpath('//*[@id="data"]/div/div/div[1]/div[3]/div[2]/span[5]/b')
        for data in pdp_aktif_rujuk:
            pdp_aktif_rujuk = data.text
            pdp_aktif_rujuk = int(pdp_aktif_rujuk.rstrip())
            covid.lpdp_aktif.append(pdp_aktif_rujuk)

        pdp_aktif_pantau = driver.find_elements_by_xpath('//*[@id="data"]/div/div/div[1]/div[3]/div[1]/div/p')
        for data in pdp_aktif_pantau:
            pdp_aktif_pantau = data.text
            pdp_aktif_pantau = int(pdp_aktif_pantau.rstrip())
            covid.lpdp_aktif.append(pdp_aktif_pantau)


        pdp_meninggal = driver.find_elements_by_xpath(
            '//*[@id="data"]/div/div/div[1]/div[3]/div[2]/span[2]/b')
        for data in pdp_meninggal:
            pdp_meninggal1 = data.text
            pdp_meninggal1 = int(pdp_meninggal1.rstrip())
            covid.lpdp_meninggal.append(pdp_meninggal1)


        pdp_meninggal2 = driver.find_elements_by_xpath(
            '//*[@id="data"]/div/div/div[1]/div[3]/div[2]/span[3]/b')
        for data in pdp_meninggal2:
            pdp_meninggal2 = data.text
            pdp_meninggal2 = int(pdp_meninggal2.rstrip())
            covid.lpdp_meninggal.append(pdp_meninggal2)


        pdp_meninggal3 = driver.find_elements_by_xpath(
            '//*[@id="data"]/div/div/div[1]/div[3]/div[2]/span[4]/b')
        for data in pdp_meninggal3:
            pdp_meninggal3 = data.text
            pdp_meninggal3 = int(pdp_meninggal3.rstrip())
            covid.lpdp_meninggal.append(pdp_meninggal3)


        positif_aktif_rawat = driver.find_elements_by_xpath('//*[@id="data"]/div/div/div[2]/div[1]/div[1]/div/p')
        for data in positif_aktif_rawat:
            positif_aktif_rawat = data.text
            positif_aktif_rawat =int (positif_aktif_rawat.rstrip())
            covid.lpositif_aktif.append(positif_aktif_rawat)


        positif_sembuh = driver.find_elements_by_xpath('//*[@id="data"]/div/div/div[2]/div[2]/div/div/p')
        for data in positif_sembuh:
            positif_sembuh = data.text
            positif_sembuh = int (positif_sembuh.rstrip())
            covid.lpositif_sembuh.append(positif_sembuh)

        driver.quit()

covid.covid_Selenium('https://awasicorona.klatenkab.go.id/')
