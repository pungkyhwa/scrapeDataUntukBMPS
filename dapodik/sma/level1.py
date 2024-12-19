from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup, BeautifulStoneSoup
import time
import pandas as pd
driver = webdriver.Chrome()
linkscrape = "https://dapo.kemdikbud.go.id/progres-sma/1/280000"

linkArray,keteranganArray,kodeWilayah1 = [],[],[]

driver.get(linkscrape)
driver.set_window_size(1300,800)
content = driver.page_source
data = BeautifulSoup(content,'html.parser')

for area in data.find_all('td'):
    for getlink in area.find_all('a'):
        link = getlink.get('href')
        teks_tautan = area.get_text(strip=True)

        linkArray.append("https://dapo.kemdikbud.go.id"+link)
        keteranganArray.append(teks_tautan)
        # print(link)
        # print(teks_tautan)
        kode_wilayah = link[-8:]
        kodeWilayah1.append(kode_wilayah)

df = pd.DataFramedf = pd.DataFrame({'link':linkArray,'keterangan':keteranganArray,'kode wiliayah1':kodeWilayah1})
writer = pd.ExcelWriter('dapodik-level-1.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()