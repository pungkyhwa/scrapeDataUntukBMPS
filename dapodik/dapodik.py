from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup, BeautifulStoneSoup
import time
import pandas as pd

# Mengatur opsi Chrome menjadi mode headless
chrome_options = Options()
chrome_options.add_argument("--headless")
# Inisialisasi WebDriver Chrome dengan opsi headless
driver = webdriver.Chrome(options=chrome_options)

linkscrape = [
"https://dapo.kemdikbud.go.id/sekolah/4EC4EA42D3BC43F98846",
"https://dapo.kemdikbud.go.id/sekolah/D46A75375C80E91951E0",
"https://dapo.kemdikbud.go.id/sekolah/07DC729E9B7160193A65",
"https://dapo.kemdikbud.go.id/sekolah/AD4917575A68BC3A5FF5",
"https://dapo.kemdikbud.go.id/sekolah/1EDC37D4F876703A4E8D"

]
length = len(linkscrape)
i = 0

# deklarasi array kosong untuk di push data
list_namasekolah, list_namakepsek, list_operator, list_akreditasi, list_kurikulum, list_waktu, list_npsn, list_status, list_bentuk_pendidikan, list_status_kepemilikan, list_sk_pendirian_sekolah, list_tanggal_sk_pendirian, list_sk_izin_operasional, list_tanggal_sk_izin_operasional, list_kebutuhan_khusus_dilayani,list_nama_bank, list_cabang_kcp_unit, list_rekening_atas_nama, list_status_bos, list_waku_penyelenggaraan, list_sertifikasi_iso, list_sumber_listrik, list_daya_listrik, list_akses_internet, list_alamat, list_rt_rw, list_dusun, list_desa_kelurahan, list_kecamatan, list_kabupaten, list_provinsi, list_kode_pos, list_lintang, list_bujur,list_jmlguru,list_jmltendik,list_jmlptk,list_jmlsiswa=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]


# menggunakan while loop
while i < length:
    print(linkscrape[i])
    driver.get(linkscrape[i])

    # driver.set_window_size(1300,800)
    content = driver.page_source
    data = BeautifulSoup(content,'html.parser')
    # print(data.encode("utf-8"))
    for area in data.find_all('div',class_="container isi"):
        namasekolah = area.find('h2',class_='name').get_text()
    
        li = data.find('div',class_="profile-usermenu")
        datali = []
        for strong in  li.find_all('strong'):
            # print(strong)
            datali.append(strong)
        namakepsek  = datali[0]
        operator    = datali[1]
        akreditasi  = datali[2]
        kurikulum   = datali[3]
        waktu       = datali[4]

        cariTagp = data.find(id="profil")
        dataltagp = []
        for tagp in cariTagp.findAll('p'):
            # print(tagp)
            dataltagp.append(tagp)
        npsn                        = dataltagp[0]
        status                      = dataltagp[1]
        bentuk_pendidikan           = dataltagp[2]
        status_kepemilikan          = dataltagp[3]
        sk_pendirian_sekolah        = dataltagp[4]
        tanggal_sk_pendirian        = dataltagp[5]
        sk_izin_operasional         = dataltagp[6]
        tanggal_sk_izin_operasional = dataltagp[7]
        kebutuhan_khusus_dilayani   = dataltagp[8]
        nama_bank                   = dataltagp[9]
        cabang_kcp_unit             = dataltagp[10]
        rekening_atas_nama          = dataltagp[11]
        status_bos                  = dataltagp[12]
        waku_penyelenggaraan        = dataltagp[13]
        sertifikasi_iso             = dataltagp[14]
        sumber_listrik              = dataltagp[15]
        daya_listrik                = dataltagp[16]
        akses_internet              = dataltagp[17]

        # jumlah mahasiswa
        cariTable = data.find('table', class_="table table-hover table-striped")
        datalorang = []
        for table in cariTable.findAll('th', class_='text-right'):
            # print(table)
            datalorang.append(table.find('a'))
        jmlguru     = datalorang[4]
        jmltendik   = datalorang[5]
        jmlptk      = datalorang[6]
        jmlsiswa    = datalorang[7]
      

        cariTagp1 = data.find(id="kontak")
        dataltagp1 = []
        for tagp1 in cariTagp1.findAll('p'):
            # print(tagp1)
            dataltagp1.append(tagp1)
        alamat          = dataltagp1[0]
        rt_rw           = dataltagp1[1]
        dusun           = dataltagp1[2]
        desa_kelurahan  = dataltagp1[3]
        kecamatan       = dataltagp1[4]
        kabupaten       = dataltagp1[5]
        provinsi        = dataltagp1[6]
        kode_pos        = dataltagp1[7]
        lintang         = dataltagp1[8]
        bujur           = dataltagp1[9]

    
        print("------ ",i)

    list_namasekolah.append(namasekolah)
    list_namakepsek.append(namakepsek)
    list_operator.append(operator)
    list_akreditasi.append(akreditasi)
    list_kurikulum.append(kurikulum)
    list_waktu.append(waktu)
    list_npsn.append(npsn)
    list_status.append(status)
    list_bentuk_pendidikan.append(bentuk_pendidikan)
    list_status_kepemilikan.append(status_kepemilikan)
    list_sk_pendirian_sekolah.append(sk_pendirian_sekolah)
    list_tanggal_sk_pendirian.append(tanggal_sk_pendirian)
    list_sk_izin_operasional.append(sk_izin_operasional)
    list_tanggal_sk_izin_operasional.append(tanggal_sk_izin_operasional)
    list_kebutuhan_khusus_dilayani.append(kebutuhan_khusus_dilayani)
    list_nama_bank.append(nama_bank)
    list_cabang_kcp_unit.append(cabang_kcp_unit)
    list_rekening_atas_nama.append(rekening_atas_nama)
    list_status_bos.append(status_bos)
    list_waku_penyelenggaraan.append(waku_penyelenggaraan)
    list_sertifikasi_iso.append(sertifikasi_iso)
    list_sumber_listrik.append(sumber_listrik)
    list_daya_listrik.append(daya_listrik)
    list_akses_internet.append(akses_internet)
    list_alamat.append(alamat)
    list_rt_rw.append(rt_rw)
    list_dusun.append(dusun)
    list_desa_kelurahan.append(desa_kelurahan)
    list_kecamatan.append(kecamatan)
    list_kabupaten.append(kabupaten)
    list_provinsi.append(provinsi)
    list_kode_pos.append(kode_pos)
    list_lintang.append(lintang)
    list_bujur.append(bujur)
    list_jmlguru.append(jmlguru)
    list_jmltendik.append(jmltendik)
    list_jmlptk.append(jmlptk)
    list_jmlsiswa.append(jmlsiswa)
       
    i += 1
    # print(list_namakepsek)
df = pd.DataFramedf =pd.DataFrame({'Nama Sekolah':list_namasekolah,'Nama Kepsek':list_namakepsek,'Operator':list_operator,'Akreditasi':list_akreditasi,'Kurikulum':list_kurikulum,'Waktu':list_waktu,'NPSN':list_npsn,'Status':list_status,'bentuk pendidikan':list_bentuk_pendidikan,'status kepemilikan':list_status_kepemilikan,'sk pendirian sekolah':list_sk_pendirian_sekolah,'tanggal sk pendirian':list_tanggal_sk_pendirian,'sk izin operasional':list_sk_izin_operasional,'tanggal sk izin operasional':list_tanggal_sk_izin_operasional,'kebutuhan khusus dilayani':list_kebutuhan_khusus_dilayani,'nama bank':list_nama_bank,'cabang kcp unit':list_cabang_kcp_unit,'rekening atas nama':list_rekening_atas_nama,'status bos':list_status_bos,'waku penyelenggaraan':list_waku_penyelenggaraan,'sertifikasi iso':list_sertifikasi_iso,'sumber listrik':list_sumber_listrik,'daya listrik':list_daya_listrik,'akses internet':list_akses_internet,'alamat':list_alamat,'rt/rw':list_rt_rw,'dusun':list_dusun,'desa/kelurahan':list_desa_kelurahan,'kecamatan':list_kecamatan,'kabupaten':list_kabupaten,'provinsi':list_provinsi,'kode pos':list_kode_pos,'lintang':list_lintang,'bujur':list_bujur,'jml_guru':list_jmlguru,'jml_tendik':list_jmltendik,'jml_ptk':list_jmlptk,'jml_siswa':list_jmlsiswa})
writer = pd.ExcelWriter('dapodik.xlsx')
df.to_excel(writer,sheet_name='Sheet1',index=False)
writer.save()