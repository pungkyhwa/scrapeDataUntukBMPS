import requests
from bs4 import BeautifulSoup
import urllib3
import pandas as pd
npsnArray,namaArray, jenjangArray, kecamatanArray, kabupatenArray, provinsiArray, nmYayasanArray = [],[],[],[],[],[],[]

# Menonaktifkan peringatan SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

no = 1
# URL halaman web yang ingin Anda ambil datanya
link = pd.read_excel('yayasan-level-3.xlsx',sheet_name='Sheet1')
for index, row in link.iterrows():
    url = row['link']
    # Mengambil konten HTML dari halaman web dengan menonaktifkan verifikasi SSL
    response = requests.get(url, verify=False)

    data = BeautifulSoup(response.content, 'html.parser')
    for row in data.find_all('tr'):
            cols = row.find_all('td')
            if len(cols) >= 6:
                npsn = cols[0].text.strip()
                nama = cols[1].text.strip()
                jenjang = cols[2].text.strip()
                kecamatan = cols[3].text.strip()
                kabupaten = cols[4].text.strip()
                provinsi = cols[5].text.strip()

                text = data.h4.get_text(strip=True, separator='|')
                text_parts = text.split('|')
                desired_text = text_parts[0]

                nmYayasanArray.append(desired_text)
                npsnArray.append(npsn)
                namaArray.append(nama)
                jenjangArray.append(jenjang)
                kecamatanArray.append(kecamatan)
                kabupatenArray.append(kabupaten)
                provinsiArray.append(provinsi)
    print(no)
    no+=1

df = pd.DataFramedf = pd.DataFrame({'npsn':npsnArray,'nama':namaArray, 'jenjang': jenjangArray, 'kecamatan':kecamatanArray, 'kabupaten':kabupatenArray, 'provinsi':provinsiArray, 'Nama yayasan':nmYayasanArray})
writer = pd.ExcelWriter('yayasan-level-4.xlsx')
df.to_excel(writer,'Sheet1',index=False)
writer.save()