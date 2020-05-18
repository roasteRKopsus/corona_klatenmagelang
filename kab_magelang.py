import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from selenium import webdriver
import numbers
import pandas as pd
import time
import re as regex


class covid_selenium:
    lodp_aktif = [] #A
    lodp_meninggal = [] #B
    lodp_sembuh = [] #C
    lpdp_aktif = [] #D
    lpdp_meninggal = [] #E
    lpdp_sembuh = [] #F
    lpositif_aktif = [] #G
    lpositif_meninggal = [] #H
    lpositif_sembuh = [] #I

    def covid (site):

        site = site
        #hdr = {'user-agent' : 'GoogleChrome'}
        driver = webdriver.Chrome(r"D:\New folder\chrome driver\chromedriver.exe")

        driver.get(site)
        driver.implicitly_wait(10)


        odp_aktif = driver.find_elements_by_xpath('//*[@id="update"]/div/div/div/div[2]/div/div/div[4]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/p[2]/span')

        for data in odp_aktif :
            odp_aktif = data.text
            odp_aktif = int(odp_aktif.rstrip())
            covid.lodp_aktif.append(odp_aktif)

        odp_meninggal = driver.find_elements_by_css_selector('#update > div > div > div > div.brz-bg-content > div > div > div:nth-child(4) > div > div > div > div > div > div.brz-bg-content > div.brz-row__container.brz-css-uhxyd > div > div > div > div.brz-columns.brz-css-hcafg.brz-css-amlhg > div > div.brz-bg-content > div > div > div > p:nth-child(2) > span')
        for data in odp_meninggal:
            odp_meninggal = data.text
            odp_meninggal = int(odp_meninggal.rstrip())
            covid.lodp_meninggal.append(odp_meninggal)


        odp_sembuh = driver.find_elements_by_xpath('//*[@id="update"]/div/div/div/div[2]/div/div/div[4]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/p[2]/span')
        for data in odp_sembuh :
            odp_sembuh = data.text
            odp_sembuh = int(odp_sembuh.rstrip())
            covid.lodp_sembuh.append(odp_sembuh)

        pdp_aktif_rawat = driver.find_elements_by_xpath('//*[@id="update"]/div/div/div/div[2]/div/div/div[6]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/p[2]/span')
        for data in pdp_aktif_rawat:
            pdp_aktif_rawat = data.text
            pdp_aktif_rawat = int(pdp_aktif_rawat.rstrip())
            covid.lpdp_aktif.append(pdp_aktif_rawat)

        pdp_aktif_rujuk = driver.find_elements_by_xpath('//*[@id="update"]/div/div/div/div[2]/div/div/div[6]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/p[2]/span')
        for data in pdp_aktif_rujuk:
            pdp_aktif_rujuk = data.text
            pdp_aktif_rujuk = int(pdp_aktif_rujuk.rstrip())
            covid.lpdp_aktif.append(pdp_aktif_rujuk)

        pdp_aktif_pantau = driver.find_elements_by_xpath('//*[@id="update"]/div/div/div/div[2]/div/div/div[6]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div[2]/div/div/p[2]/span')
        for data in pdp_aktif_pantau:
            pdp_aktif_pantau = data.text
            pdp_aktif_pantau = int(pdp_aktif_pantau.rstrip())
            covid.lpdp_aktif.append(pdp_aktif_pantau)

        pdp_meninggal = driver.find_elements_by_xpath(
            '//*[@id="update"]/div/div/div/div[2]/div/div/div[6]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[2]/div[1]/div/div/p[2]/span')
        for data in pdp_meninggal:
            pdp_meninggal = data.text
            pdp_meninggal = int(pdp_meninggal.rstrip())
            covid.lpdp_meninggal.append(pdp_meninggal)

        pdp_sembuh = driver.find_elements_by_xpath(
           '//*[@id="update"]/div/div/div/div[2]/div/div/div[6]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div[3]/div/div/p[2]/span')
        for data in pdp_sembuh:
            pdp_sembuh = data.text
            pdp_sembuh = int(pdp_sembuh.rstrip())
            covid.lpdp_sembuh.append(pdp_sembuh)

        positif_aktif_rawat = driver.find_elements_by_xpath('//*[@id="update"]/div/div/div/div[2]/div/div/div[7]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[1]/div/div[2]/div/div/div/p[2]/span')
        for data in positif_aktif_rawat:
            positif_aktif_rawat = data.text
            positif_aktif_rawat =int (positif_aktif_rawat.rstrip())
            covid.lpositif_aktif.append(positif_aktif_rawat)

        positif_aktif_pantau = driver.find_elements_by_xpath('//*[@id="update"]/div/div/div/div[2]/div/div/div[7]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[2]/div/div[2]/div/div/div/p[2]/span')
        for data in positif_aktif_pantau:
            positif_aktif_pantau = data.text
            positif_aktif_pantau = int(positif_aktif_pantau.rstrip())
            covid.lpositif_aktif.append(positif_aktif_pantau)

        positif_meninggal = driver.find_elements_by_xpath('//*[@id="update"]/div/div/div/div[2]/div/div/div[7]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/div[2]/div/div/div/p[2]/span')
        for data in positif_meninggal:
            positif_meninggal = data.text
            positif_meninggal = int(positif_meninggal.rstrip())
            covid.lpositif_meninggal.append(positif_meninggal)

        positif_sembuh = driver.find_elements_by_xpath('//*[@id="update"]/div/div/div/div[2]/div/div/div[7]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/p[2]/span')
        for data in positif_sembuh:
            positif_sembuh = data.text
            positif_sembuh = int (positif_sembuh.rstrip())
            covid.lpositif_sembuh.append(positif_sembuh)

        driver.quit()

covid_magelang.covid_magelangSelenium('https://covid19.magelangkota.go.id/')

print(covid_magelang.lpositif_sembuh)