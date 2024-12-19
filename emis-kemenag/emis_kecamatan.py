from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup, BeautifulStoneSoup
import time
import pandas as pd
driver = webdriver.Chrome()
linkscrape = "http://localhost/test/"

driver.get(linkscrape)
driver.set_window_size(1300,800)
content = driver.page_source
data = BeautifulSoup(content,'html.parser')
# time.sleep(5)
# driver.find_element(By.XPATH, '//*[@id="example_length"]/label/select').click()
# driver.find_element(By.XPATH, '//*[@id="example_length"]/label/select/option[4]').click()
# time.sleep(5)


length = 83
i = 0
while i < length:
    list_link = []
    cariTagtr = data.find('table')
    # for area in cariTagtr.find_all('tr'):
    #     getlink = area.find('a')
    #     print(getlink)
    #     list_link.append(getlink)
    for area in cariTagtr.find_all('tr'):
        for getlink in area.find_all('a'):
            link = getlink.get('href')
            list_link.append(link)
            print(link)

    # driver.find_element(By.XPATH, '//*[@id="example_next"]/a').click()
    # time.sleep(3)
    i += 1
    
df = pd.DataFramedf =pd.DataFrame({'link':list_link})
writer = pd.ExcelWriter('kecamatan-emis.xlsx')
df.to_excel(writer,sheet_name='Sheet1',index=False)
writer.save()