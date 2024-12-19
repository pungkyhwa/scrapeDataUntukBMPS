from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup, BeautifulStoneSoup
import time
import pandas as pd

linkArray,nmSekolahArray,npsnArray,bpArray,statusArray,kecamatanArray,kodeWilayah2, kodeWilayah1, namaWilayah1= [],[],[],[],[],[],[],[],[]

link = pd.read_excel('dapodik-level-2.xlsx',sheet_name='Sheet1')
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
            nmSekolah = area.get_text(strip=True)
            linkArray.append("https://dapo.kemdikbud.go.id"+link)
            nmSekolahArray.append(nmSekolah)
            

    td_texts = []
    for td in data.find_all('td', {'style': 'text-align: left;'}):
        td_texts.append(td.text)

    # Menyusun teks menjadi array 2D
    num_columns = 3  # Menentukan jumlah kolom
    array_2d = [td_texts[i:i+num_columns] for i in range(0, len(td_texts), num_columns)]
    for sublist in array_2d:
        npsnArray.append(sublist[0])
        bpArray.append(sublist[1])
        statusArray.append(sublist[2])

        for areaUl in data.find_all('ul', class_='breadcrumb'):
            active_li = areaUl.find('li', class_='active')
            active_text = active_li.get_text(strip=True)
            kecamatanArray.append(active_text)
            kode_wilayah2 = url[-8:]
            kodeWilayah2.append(kode_wilayah2)
            kode_wilayah1 = row['kode kab/kota']
            kodeWilayah1.append(kode_wilayah1)
            nama_wilayah1 = row['kab/kota']
            namaWilayah1.append(nama_wilayah1)

            # print(kode_wilayah1,nama_wilayah1)
            
df = pd.DataFramedf = pd.DataFrame({'link':linkArray,'nama Sekolah':nmSekolahArray,'NPSN':npsnArray, 'BP':bpArray, 'status':statusArray, 'kode kecamatan':kodeWilayah2,'kecamatan':kecamatanArray, 'kode kab/kota':kodeWilayah1, 'kab/kota': namaWilayah1 })
writer = pd.ExcelWriter('dapodik-level-3.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()