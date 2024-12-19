from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup, BeautifulStoneSoup
import time
import pandas as pd
driver = webdriver.Chrome()
linkscrape = "https://vervalyayasan.data.kemdikbud.go.id/index.php/Chome/rekapitulasi?kode_wilayah=280000"

driver.get(linkscrape)
driver.set_window_size(1300,800)
python_button = driver.find_element(By.XPATH, "/html/body/div/div/div/section[2]/div/div/div/div/div/div[2]/label/select")
python_button.click()
python_button1 = driver.find_element(By.XPATH, "/html/body/div/div/div/section[2]/div/div/div/div/div/div[2]/label/select/option[3]")
python_button1.click()
time.sleep(5)

linkArray,wilayahArray,kodeWilayah1 = [],[],[]
content = driver.page_source
data = BeautifulSoup(content,'html.parser')


for area in data.find_all('tr'):
    getlink = area.find('a')
    if getlink:
        url = getlink.get('href')
        wilayah = getlink.text.strip()
        linkArray.append(url)
        wilayahArray.append(wilayah)
        kode_wilayah = url[-6:]
        kodeWilayah1.append(kode_wilayah)

        # print(kode_wilayah)
        # print(wilayah)



# df = pd.DataFramedf = pd.DataFrame({'link':linkArray,'wilayah':wilayahArray,'kode wilayah 1':kodeWilayah1})
df = pd.DataFrame({'link':linkArray,'wilayah':wilayahArray,'kode wilayah 1':kodeWilayah1})

# writer = pd.ExcelWriter('yayasan-level-1.xlsx')
df.to_excel('yayasan-level-1.xlsx', index=False, sheet_name='Sheet1')

# df.to_excel(writer,'Sheet1',index=False)
# writer.save()

