import requests
from bs4 import BeautifulSoup
import urllib3
import pandas as pd

linkArray,namaArray, npypArray, kodeWilayah2 = [],[],[],[]
# Menonaktifkan peringatan SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

no = 1
# URL halaman web yang ingin Anda ambil datanya
link = pd.read_excel('yayasan-level-2.xlsx',sheet_name='Sheet1')
for index, row in link.iterrows():
    url = row['link']
    # Mengambil konten HTML dari halaman web dengan menonaktifkan verifikasi SSL
    response = requests.get(url, verify=False)

    data = BeautifulSoup(response.content, 'html.parser')
    for area in data.find_all('tr'):
        getlink = area.find('a')
             
        if getlink:
            url1 = getlink.get('href')
            wilayah = getlink.text.strip()
            linkArray.append(url1)
            # print(url)
            # print(wilayah)
    
    for row in data.find_all('tr'):
        cols = row.find_all('td')
        if len(cols) >= 4:
            npyp = cols[0].text.strip()
            nama = cols[1].text.strip()
            alamat = cols[2].text.strip()
            desa_kelurahan = cols[3].text.strip()
            # print(npyp)
            # print(nama)
            # print(alamat)
            npypArray.append(npyp)
            namaArray.append(nama)
        
            kode_wilayah2 = url[-6:]
            kodeWilayah2.append(kode_wilayah2)

    print(no)
    no+=1

df = pd.DataFramedf = pd.DataFrame({'link':linkArray,'ypyp':npypArray, 'nama':namaArray, 'kode wilayah 2': kodeWilayah2})
writer = pd.ExcelWriter('yayasan-level-3.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()             