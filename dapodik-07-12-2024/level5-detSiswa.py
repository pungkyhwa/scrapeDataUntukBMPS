import logging
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import time
import json

# Inisialisasi logger
logging.basicConfig(filename="error.log", level=logging.ERROR, format="%(asctime)s - %(message)s")

# Setup Selenium WebDriver
driver = webdriver.Chrome()

# List untuk menyimpan data
list_pd, list_pd_laki, list_pd_perempuan, list_pd_kelas_1_laki, list_pd_kelas_1_perempuan, list_pd_kelas_2_laki, list_pd_kelas_2_perempuan, list_pd_kelas_3_laki, list_pd_kelas_3_perempuan, list_pd_kelas_4_laki, list_pd_kelas_4_perempuan, list_pd_kelas_5_laki, list_pd_kelas_5_perempuan, list_pd_kelas_6_laki, list_pd_kelas_6_perempuan, list_pd_kelas_7_laki, list_pd_kelas_7_perempuan, list_pd_kelas_8_laki, list_pd_kelas_8_perempuan, list_pd_kelas_9_laki, list_pd_kelas_9_perempuan, list_pd_kelas_10_laki, list_pd_kelas_10_perempuan, list_pd_kelas_11_laki, list_pd_kelas_11_perempuan, list_pd_kelas_12_laki, list_pd_kelas_12_perempuan, list_pd_kelas_13_laki, list_pd_kelas_13_perempuan, list_npsn = [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]
list_retry = []  # Daftar untuk menyimpan data gagal

# Baca file Excel
linksccrape = pd.read_excel('dapodik-level-5.xlsx', sheet_name='Sheet1')

# Fungsi untuk memproses data
def process_data(row, retry=False):
    try:
        link = row['link']
        npsn = row['NPSN']
        print(f"{'Retrying' if retry else 'Processing'} link: {link}")
        driver.get(link)
        driver.set_window_size(1300, 800)
        # time.sleep(2)  # Tunggu agar halaman selesai dimuat

        # Parsing dengan BeautifulSoup
        content = driver.page_source
        data = BeautifulSoup(content, 'html.parser')
       
        # Mengambil isi tag <body>
        body_content = data.body.text
       
        # Mengonversi string JSON menjadi objek Python
        data_json = json.loads(body_content)

        # Mengambil nilai 'pd' dari data
        pd_value = data_json[0]['pd']  # Indeks 0 karena data adalah list dengan satu elemen
        pd_laki_value = data_json[0]['pd_laki']  # Indeks 0 karena data adalah list dengan satu elemen
        pd_perempuan_value = data_json[0]['pd_perempuan']  # Indeks 0 karena data adalah list dengan satu elemen
        pd_kelas_1_laki_value = data_json[0]['pd_kelas_1_laki']
        pd_kelas_1_perempuan_value = data_json[0]['pd_kelas_1_perempuan']
        pd_kelas_2_laki_value = data_json[0]['pd_kelas_2_laki']
        pd_kelas_2_perempuan_value = data_json[0]['pd_kelas_2_perempuan']
        pd_kelas_3_laki_value = data_json[0]['pd_kelas_3_laki']
        pd_kelas_3_perempuan_value = data_json[0]['pd_kelas_3_perempuan']
        pd_kelas_4_laki_value = data_json[0]['pd_kelas_4_laki']
        pd_kelas_4_perempuan_value = data_json[0]['pd_kelas_4_perempuan']
        pd_kelas_5_laki_value = data_json[0]['pd_kelas_5_laki']
        pd_kelas_5_perempuan_value = data_json[0]['pd_kelas_5_perempuan']
        pd_kelas_6_laki_value = data_json[0]['pd_kelas_6_laki']
        pd_kelas_6_perempuan_value = data_json[0]['pd_kelas_6_perempuan']
        pd_kelas_7_laki_value = data_json[0]['pd_kelas_7_laki']
        pd_kelas_7_perempuan_value = data_json[0]['pd_kelas_7_perempuan']
        pd_kelas_8_laki_value = data_json[0]['pd_kelas_8_laki']
        pd_kelas_8_perempuan_value = data_json[0]['pd_kelas_8_perempuan']
        pd_kelas_9_laki_value = data_json[0]['pd_kelas_9_laki']
        pd_kelas_9_perempuan_value = data_json[0]['pd_kelas_9_perempuan']
        pd_kelas_10_laki_value = data_json[0]['pd_kelas_10_laki']
        pd_kelas_10_perempuan_value = data_json[0]['pd_kelas_10_perempuan']
        pd_kelas_11_laki_value = data_json[0]['pd_kelas_11_laki']
        pd_kelas_11_perempuan_value = data_json[0]['pd_kelas_11_perempuan']
        pd_kelas_12_laki_value = data_json[0]['pd_kelas_12_laki']
        pd_kelas_12_perempuan_value = data_json[0]['pd_kelas_12_perempuan']
        pd_kelas_13_laki_value = data_json[0]['pd_kelas_13_laki']
        pd_kelas_13_perempuan_value = data_json[0]['pd_kelas_13_perempuan']

        list_pd.append(pd_value)
        list_pd_laki.append(pd_laki_value)
        list_pd_perempuan.append(pd_perempuan_value)        
        list_pd_kelas_1_laki.append(pd_kelas_1_laki_value)
        list_pd_kelas_1_perempuan.append(pd_kelas_1_perempuan_value)
        list_pd_kelas_2_laki.append(pd_kelas_2_laki_value)
        list_pd_kelas_2_perempuan.append(pd_kelas_2_perempuan_value)
        list_pd_kelas_3_laki.append(pd_kelas_3_laki_value)
        list_pd_kelas_3_perempuan.append(pd_kelas_3_perempuan_value)
        list_pd_kelas_4_laki.append(pd_kelas_4_laki_value)
        list_pd_kelas_4_perempuan.append(pd_kelas_4_perempuan_value)
        list_pd_kelas_5_laki.append(pd_kelas_5_laki_value)
        list_pd_kelas_5_perempuan.append(pd_kelas_5_perempuan_value)
        list_pd_kelas_6_laki.append(pd_kelas_6_laki_value)
        list_pd_kelas_6_perempuan.append(pd_kelas_6_perempuan_value)
        list_pd_kelas_7_laki.append(pd_kelas_7_laki_value)
        list_pd_kelas_7_perempuan.append(pd_kelas_7_perempuan_value)
        list_pd_kelas_8_laki.append(pd_kelas_8_laki_value)
        list_pd_kelas_8_perempuan.append(pd_kelas_8_perempuan_value)
        list_pd_kelas_9_laki.append(pd_kelas_9_laki_value)
        list_pd_kelas_9_perempuan.append(pd_kelas_9_perempuan_value)
        list_pd_kelas_10_laki.append(pd_kelas_10_laki_value)
        list_pd_kelas_10_perempuan.append(pd_kelas_10_perempuan_value)
        list_pd_kelas_11_laki.append(pd_kelas_11_laki_value)
        list_pd_kelas_11_perempuan.append(pd_kelas_11_perempuan_value)
        list_pd_kelas_12_laki.append(pd_kelas_12_laki_value)
        list_pd_kelas_12_perempuan.append(pd_kelas_12_perempuan_value)
        list_pd_kelas_13_laki.append(pd_kelas_13_laki_value)
        list_pd_kelas_13_perempuan.append(pd_kelas_13_perempuan_value)
        list_npsn.append(npsn)

        print(f"Data berhasil diproses untuk link: {link}")
    except Exception as e:
        # Log error
        logging.error(f"Error pada link {row['link']}: {e}")
        print(f"Error pada link {row['link']}: {e}")
        # Tambahkan data ke list retry jika error
        list_retry.append(row)

# Looping utama
for index, row in linksccrape.iterrows():
    process_data(row)

# Proses ulang data yang gagal
if list_retry:
    print(f"\n{len(list_retry)} data gagal akan diulang...")
    for row in list_retry:
        process_data(row, retry=True)

# Simpan data ke Excel
df = pd.DataFrame({
    'pd' : list_pd, 
    'pd_laki' : list_pd_laki, 
    'pd_perempuan' : list_pd_perempuan,
    'pd_kelas_1_laki' : list_pd_kelas_1_laki,
    'pd_kelas_1_perempuan' : list_pd_kelas_1_perempuan,
    'pd_kelas_2_laki' : list_pd_kelas_2_laki,
    'pd_kelas_2_perempuan' : list_pd_kelas_2_perempuan,
    'pd_kelas_3_laki' : list_pd_kelas_3_laki,
    'pd_kelas_3_perempuan' : list_pd_kelas_3_perempuan,
    'pd_kelas_4_laki' : list_pd_kelas_4_laki,
    'pd_kelas_4_perempuan' : list_pd_kelas_4_perempuan,
    'pd_kelas_5_laki' : list_pd_kelas_5_laki,
    'pd_kelas_5_perempuan' : list_pd_kelas_5_perempuan,
    'pd_kelas_6_laki' : list_pd_kelas_6_laki,
    'pd_kelas_6_perempuan' : list_pd_kelas_6_perempuan,
    'pd_kelas_7_laki' : list_pd_kelas_7_laki,
    'pd_kelas_7_perempuan' : list_pd_kelas_7_perempuan,
    'pd_kelas_8_laki' : list_pd_kelas_8_laki,
    'pd_kelas_8_perempuan' : list_pd_kelas_8_perempuan,
    'pd_kelas_9_laki' : list_pd_kelas_9_laki,
    'pd_kelas_9_perempuan' : list_pd_kelas_9_perempuan,
    'pd_kelas_10_laki' : list_pd_kelas_10_laki,
    'pd_kelas_10_perempuan' : list_pd_kelas_10_perempuan,
    'pd_kelas_11_laki' : list_pd_kelas_11_laki,
    'pd_kelas_11_perempuan' : list_pd_kelas_11_perempuan,
    'pd_kelas_12_laki' : list_pd_kelas_12_laki,
    'pd_kelas_12_perempuan' : list_pd_kelas_12_perempuan,
    'pd_kelas_13_laki' : list_pd_kelas_13_laki,
    'pd_kelas_13_perempuan' : list_pd_kelas_13_perempuan,
    'NPSN':list_npsn,
    
    # Tambahkan kolom lainnya sesuai kebutuhan
})
df.to_excel('dapodik-level-6.xlsx', index=False, sheet_name='Sheet1')

driver.quit()
