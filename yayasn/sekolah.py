from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup, BeautifulStoneSoup
import time
import pandas as pd
driver = webdriver.Chrome()
linkscrape = [
"https://vervalyayasan.data.kemdikbud.go.id/index.php/Chome/rekapitulasi?kode_wilayah=280313",
]
length = len(linkscrape)
i = 0



dataltagp = []
while i < length:
    # print(linkscrape[i])
    driver.get(linkscrape[i])
    driver.set_window_size(1300,800)
    python_button = driver.find_element(By.XPATH, "/html/body/div/div/div/section[2]/div/div/div/div/div/div[2]/label/select")
    python_button.click()
    python_button1 = driver.find_element(By.XPATH, "html/body/div/div/div/section[2]/div/div/div/div/div/div[2]/label/select/option[3]")
    python_button1.click()
    # time.sleep(5)

    content = driver.page_source
    data = BeautifulSoup(content,'html.parser')
    
    for area in data.find_all('a'):
        # getlink = area.find('a')
        getlink1 = area.get('href')
        print (getlink1)
        dataltagp.append(getlink1)
    # print(dataltagp)
    i += 1
    
    df = pd.DataFramedf = pd.DataFrame({'Nama link':dataltagp})
    writer = pd.ExcelWriter('link_sekolah.xlsx')
    df.to_excel(writer,'Sheet1',index=False)
    writer.save()
   
