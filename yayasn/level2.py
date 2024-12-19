from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup, BeautifulStoneSoup
import time
import pandas as pd

linkArray,wilayahArray,kodeWilayah1,kodeWilayah2 = [],[],[],[]
link = pd.read_excel('yayasan-level-1.xlsx',sheet_name='Sheet1')

for index, row in link.iterrows():
    url = row['link']
    driver = webdriver.Chrome()
    driver.get(url)
    driver.set_window_size(1300,800)

    python_button = driver.find_element(By.XPATH, "/html/body/div/div/div/section[2]/div/div/div/div/div/div[2]/label/select")
    python_button.click()
    python_button1 = driver.find_element(By.XPATH, "/html/body/div/div/div/section[2]/div/div/div/div/div/div[2]/label/select/option[3]")
    python_button1.click()
    # time.sleep(15)

    
    content = driver.page_source
    data = BeautifulSoup(content,'html.parser')

    for area in data.find_all('tr'):
        getlink = area.find('a')
        if getlink:
            url1 = getlink.get('href')
            wilayah = getlink.text.strip()
            linkArray.append(url1)
            wilayahArray.append(wilayah)
            kode_wilayah1 = url[-6:]
            kodeWilayah1.append(kode_wilayah1)
            kode_wilayah2 = url1[-6:]
            kodeWilayah2.append(kode_wilayah2)
            # print(kode_wilayah2)
            # print(wilayah)

# df = pd.DataFramedf = pd.DataFrame({'link':linkArray,'wilayah 2':wilayahArray,'kode wilayah 1':kodeWilayah1,'kode wilayah 2':kodeWilayah2})
df = pd.DataFrame({'link':linkArray,'wilayah 2':wilayahArray,'kode wilayah 1':kodeWilayah1,'kode wilayah 2':kodeWilayah2})

# writer = pd.ExcelWriter('yayasan-level-2.xlsx')
df.to_excel('yayasan-level-2.xlsx', index=False, sheet_name='Sheet1')

# df.to_excel(writer,'Sheet1',index=False)
# writer.save()