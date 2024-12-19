from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup, BeautifulStoneSoup
import time
import pandas as pd
driver = webdriver.Chrome()

linkArray,keteranganArray,kodeWilayah1 = [],[],[]

linkscrape = [
"https://dapo.kemdikbud.go.id/progres-paud/1/280000?view=tk",
"https://dapo.kemdikbud.go.id/progres-paud/1/280000?view=kb",
"https://dapo.kemdikbud.go.id/progres-paud/1/280000?view=tpa",
"https://dapo.kemdikbud.go.id/progres-paud/1/280000?view=sps",
"https://dapo.kemdikbud.go.id/progres-paud/1/280000?view=pkbm",
"https://dapo.kemdikbud.go.id/progres-paud/1/280000?view=skb",
"https://dapo.kemdikbud.go.id/progres-sd/1/280000",
"https://dapo.kemdikbud.go.id/progres-smp/1/280000",
"https://dapo.kemdikbud.go.id/progres-sma/1/280000",
"https://dapo.kemdikbud.go.id/progres-smk/1/280000",
"https://dapo.kemdikbud.go.id/progres-slb/1/280000"
]
# linkscrape = [
# "https://dapo.kemdikbud.go.id/progres/1/280000"
# ]
length = len(linkscrape)
i = 0
while i < length:
    # print(linkscrape[i])
    driver.get(linkscrape[i])
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
    print(i)
    i += 1
# df = pd.DataFramedf = pd.DataFrame({'link':linkArray,'keterangan':keteranganArray,'kode wiliayah1':kodeWilayah1})
df = pd.DataFrame({'link': linkArray, 'keterangan': keteranganArray, 'kode wilayah1': kodeWilayah1})

# writer = pd.ExcelWriter('dapodik-level-1.xlsx')
df.to_excel('dapodik-level-1.xlsx', index=False, sheet_name='Sheet1')

# df.to_excel(writer,'Sheet1',index=False)
# writer.save()