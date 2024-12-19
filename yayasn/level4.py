from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup, BeautifulStoneSoup
import time
import pandas as pd

npsnArray,namaArray, jenjangArray, kecamatanArray, kabupatenArray, provinsiArray, nmYayasanArray = [],[],[],[],[],[],[]


link = pd.read_excel('yayasan-level-3.xlsx',sheet_name='Sheet1')

for index, row in link.iterrows():
    url = row['link']
    driver = webdriver.Chrome()
    driver.get(url)
    driver.set_window_size(1300,800)

    python_button = driver.find_element(By.XPATH, "/html/body/div/div/div/section[2]/div/div/div/div/div/div[2]/label/select")
    python_button.click()
    python_button1 = driver.find_element(By.XPATH, "/html/body/div/div/div/section[2]/div/div/div/div/div/div[2]/label/select/option[3]")
    python_button1.click()
    # time.sleep(5)

    content = driver.page_source
    data = BeautifulSoup(content,'html.parser')

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


# df = pd.DataFramedf = pd.DataFrame({'npsn':npsnArray,'nama':namaArray, 'jenjang': jenjangArray, 'kecamatan':kecamatanArray, 'kabupaten':kabupatenArray, 'provinsi':provinsiArray, 'Nama yayasan':nmYayasanArray})
df = pd.DataFrame({'npsn':npsnArray,'nama':namaArray, 'jenjang': jenjangArray, 'kecamatan':kecamatanArray, 'kabupaten':kabupatenArray, 'provinsi':provinsiArray, 'Nama yayasan':nmYayasanArray})

# writer = pd.ExcelWriter('yayasan-level-4.xlsx')
df.to_excel('yayasan-level-4.xlsx', index=False, sheet_name='Sheet1')

# df.to_excel(writer,'Sheet1',index=False)
# writer.save()