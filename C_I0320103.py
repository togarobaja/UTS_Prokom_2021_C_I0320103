import io
import csv
import urllib.request

def csv_import(url):
    url_open = urllib.request.urlopen(url)
    csvfile = csv.reader(io.StringIO(url_open.read().decode('utf-8')), delimiter=',')
    return csvfile

url = "https://raw.githubusercontent.com/priyandari/Python-tutorial-for-beginners/tutorial2021/nilaiKuliah.csv"

datafile = csv_import(url)
#Diperoleh data mentah sebagai berikut
data_nilaimhs =list(datafile)

#Konversi data nilai dari string menjadi float
for datamhs in data_nilaimhs:
    if datamhs[0] != 'NIM':
        datamhs[2] = float(datamhs[2])
        datamhs[3] = float(datamhs[3])
        datamhs[4] = float(datamhs[4])
        datamhs[5] = float(datamhs[5])

#Menampilkan masing-masing data nilai mahasiswa
for nilai in data_nilaimhs:
    print(nilai)

#menambahkan nilai akhir
for datanilai in data_nilaimhs[:]:
    bobotUK1 = 0.2
    bobotUK2 = 0.2
    bobotUK3 = 0.3
    bobotUK4 = 0.3
    if datanilai[0] =='NIM':
        datanilai.append('nilai akhir')
    else:
        nilaiakhir = bobotUK1 * datanilai[2] + bobotUK2 * datanilai[3] + bobotUK3 * datanilai[4] + bobotUK4 * datanilai[5]
        printf(nilaiakhir)
        datanilai.append(nilaiakhir)

#Menampilkan masing-masing data nilai mahasiswa
for nilai in data_nilaimhs:
    print(nilai)
print("---"*12)
#menghitung rata-rata nilai
rata_ratamhs = []
for datanilai in data_nilaimhs[1:]:
    rata_ratamhs.append(datanilai[6])
rata_nilai = sum(rata_ratamhs)/len(rata_ratamhs)
print(f"rata-rata nilai :, {rata_nilai} ")

#menghitung rata-rata angkatan 2020
rata_rata2020 = []
for datanilai in data_nilaimhs[12:]:
    rata_rata2020.append(datanilai[6])
rata_rata_nilai20 = sum(rata_rata2020)/len(rata_rata2020)
print(f"rata-rata nilai angkatan 2020 :, {rata_rata_nilai20} ")

#menambahkan nilai berupa huruf
for datanilai in data_nilaimhs:
    if datanilai[0] == "NIM":
        datanilai.append("Huruf")
    elif datanilai[6] >= 85 :
        datanilai.append("A")
    elif datanilai[6] >= 75 :
        datanilai.append("B")
    elif datanilai[6] >= 65 :
        datanilai.append("C")
    elif datanilai[6] >= 50 :
        datanilai.append("D")
    else:
        datanilai.append("E")
#menghitung mahasiswa angkatan 2019 yang mendapat nilai B
jmlhmhs2019 = 0
for data in data_nilaimhs[1:12]:
    if data[7] == "B":
        jmlhmhs2019 += 1
    else:
        pass
print("Jumlah mahasiswa angkatan 2019 yang mendapat nilai B :",(jmlhmhs2019))

#menghitung nilai B di tahun angkatan tahun 2020
jmlhmhs2020 = 0
for datanilai in data_nilaimhs[12:]:
    if datanilai[7]=="B":
        jmlhmhs2020 +=1
    else:
        pass
print("Jumlah mahasiswa angkatan 2020 yang mendapat nilai B :",(jmlhmhs2020))