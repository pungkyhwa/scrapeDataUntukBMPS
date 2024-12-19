from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup, BeautifulStoneSoup
import time
import pandas as pd

link = pd.read_excel('dapodik-level-1.xlsx',sheet_name='Sheet1')

linkArray,kecamatanArray, kabArray, kodeWilayah1,kodeWilayah2= [],[],[],[],[]

# Meloopi setiap baris di DataFrame
for index, row in link.iterrows():
    url = row['link']  # Mengambil nilai dari kolom 'link'
    
    driver = webdriver.Chrome()

    driver.get(url)
    driver.set_window_size(1300,800)
    content = driver.page_source
    data = BeautifulSoup(content,'html.parser')

    for area in data.find_all('td'):
        for getlink in area.find_all('a'):
            link = getlink.get('href')
            teks_tautan = area.get_text(strip=True)

            linkArray.append("https://dapo.kemdikbud.go.id"+link)
            kecamatanArray.append(teks_tautan)
            
            for areaUl in data.find_all('ul', class_='breadcrumb'):
                active_li = areaUl.find('li', class_='active')
                active_text = active_li.get_text(strip=True)
                kabArray.append(active_text)
                

                kode_wilayah1 = url[-8:]
                kodeWilayah1.append(kode_wilayah1)
                kode_wilayah2 = link[-8:]
                kodeWilayah2.append(kode_wilayah2)

                # print(kode_wilayah1)

df = pd.DataFramedf = pd.DataFrame({'link':linkArray,'kode kecamatan': kodeWilayah2,'kecamatan':kecamatanArray, 'kode kab/kota':kode_wilayah1,'kab/kota':kabArray})
writer = pd.ExcelWriter('dapodik-level-2.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()