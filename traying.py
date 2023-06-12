# -*- coding: utf-8 -*-
pip install streamlit
pip install pandas
pip install numpy
pip install sastrawi
pip install nltk
pip install sklearn

import streamlit as st
import pandas as pd
import numpy as np


st.title('Analisis Sentimen Pada Pantai Talang Siring di Google Map Menggunakan Naive Bayess')
st.markdown('Pantai Talang siring merupakan salah satu wisata yang berada pada kabupaten Pamekasan, Pantai ini cukup sering dikunjungi oleh wisatawan, hal itu dapat dilihat dari jumlah ulasan yang sudah mencapai 1000 ulasan lebih. Penelitian kali ini akan menggunakan algoritma Naive Bayess untuk melakukann klasifikasi pada ulasan google map di tempat wisata pantai Talang Siring. berikut ini adalah langkah demi langkahnya.')

st.markdown('berikut ini adalah link untuk menuju pantai Talang Siring menggunakan google map')
# Mendefinisikan link Google Maps
google_maps_link = "https://www.google.com/maps/place/Wisata+Pantai+Talang+Siring+Pamekasan/@-7.1360417,113.5818952,15z/data=!4m6!3m5!1s0x2dd9d8096c2281bd:0xa468bcedaaafc9b!8m2!3d-7.1383957!4d113.5895106!16s%2Fg%2F11c3l5tr2n?entry=ttu"

# Menampilkan iframe dengan link Google Maps
st.markdown(f"[Lihat di Google Maps]({google_maps_link})")


st.header('Langkah Langkah Analisis Sentimen pada pantai Talang Siring :sunglasses:')
st.subheader('1. Copy Komentar Google Map')
st.markdown('Mengambil komentar pada Google Map dengan cara manual yaitu di copy. Berikut ini adalah contoh salah satu komentar yang akan digunakan.\n “Tiket parkir beda. Tiket masuk beda. Tiket ke mangrovenya pun beda. Saran aja sih jadikan satu tiket aja untuk seluruh wahana pantai. Terus mangrove nya perlu pengembangan lg sih, terlalu basic dan kurang pengelolaannya". Data yang digunakan sebanyak 100 ulasan di gogle map. data tersebut terdiri dari 50 positif dan 50 negatif.')
url_ulasan_google = "ulasan google map.jpg"
st.image(url_ulasan_google)


st.markdown('berikut ini adalah data yang sudah di copy secara manual dan akan digunakan pada penelitian kali ini')
from openpyxl import load_workbook #library untuk menampilkan dokumen
import pandas as pd #import pandas 
from nltk.tokenize import word_tokenize #import library nltk - tokenize
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory #import library sastrawi untuk

wr = load_workbook(filename = 'komentar_awal.xlsx')
sheet_range = wr['Sheet1']

df = pd.DataFrame(sheet_range.values)
df.columns = ['komen','Label']
df = df.drop(0)
df




st.subheader('2. Melakukan preprocessing pada teks')
st.markdown('berikut ini adalah tahapan tahapan dalam melakukan preprocessing pada teks')
st.markdown('-	Case Folding')
st.markdown('''Case folding adalah proses pengubahan karakter huruf menjadi huruf kecil pada teks. Proses ini merupakan salah satu tahapan dalam preprocessing teks pada pemrosesan bahasa alami. Dalam bahasa Inggris, misalnya, teks yang dihasilkan dari berbagai sumber seperti dokumen atau pesan teks dapat mengandung karakter huruf besar (kapital) dan kecil (non-kapital). Pada tahap case folding, seluruh karakter huruf besar pada teks dikonversi menjadi karakter huruf kecil.\n

Proses case folding pada teks bertujuan untuk memperkecil kompleksitas data dan menghindari perbedaan penulisan karakter huruf yang sama, yang dapat mempengaruhi hasil analisis atau pengolahan teks. Selain itu, dengan hanya menggunakan karakter huruf kecil, akan memudahkan mesin atau program komputer dalam memproses teks dan melakukan pencocokan kata kunci pada pencarian teks.\n

Berikut ini adalah komentar yang sudah di terapkan proses case Folding.
“tiket parkir beda. tiket masuk beda. tiket ke mangrovenya pun beda. saran aja sih jadikan satu tiket aja untuk seluruh wahanan pantai. terus mangrove nya perlu pengembangan lg sih, terlalu basic dan kurang pengelolaannya.”
''')

st.markdown('-	Cleansing')
st.markdown(''' Cleansing dalam pemrosesan bahasa alami (natural language processing) merujuk pada proses penghapusan karakter atau informasi yang tidak relevan atau mengganggu dari suatu dokumen atau teks. Tujuan dari proses cleansing adalah untuk membersihkan dokumen atau teks dari karakter atau informasi yang tidak berguna atau mengganggu sehingga dapat menghasilkan teks yang lebih terstruktur dan berkualitas untuk diolah lebih lanjut./n

Contoh karakter atau informasi yang sering dihapus dalam proses cleansing meliputi tanda baca, angka, karakter khusus, kata pengisi, dan kata-kata yang umum dan tidak berguna seperti "a", "the", "and", dan sebagainya. Proses cleansing juga dapat mencakup penghapusan kata-kata yang berpotensi menimbulkan bias dalam analisis, seperti kata-kata kasar atau yang bersifat diskriminatif./n

Proses cleansing dapat dilakukan dengan menggunakan teknik-teknik seperti regular expression, tokenization, stop word removal, dan stemming/lemmatization. Proses cleansing menjadi salah satu tahap penting dalam pemrosesan bahasa alami untuk memastikan data yang diolah memiliki kualitas dan relevansi yang baik. Berikut ini adalah contoh komentar yang sudah diterapkan proses Cleansing.
 “tiket parkir beda tiket masuk beda tiket ke mangrovenya pun beda saran aja sih jadikan satu tiket aja untuk seluruh wahanan pantai terus mangrove nya perlu pengembangan lg sih terlalu basic dan kurang pengelolaannya”
''')

st.markdown('-	Tokenisasi')
st.markdown('''Tokenisasi adalah proses memecah teks menjadi bagian-bagian yang lebih kecil, yang disebut sebagai token atau kata-kata. Tokenisasi sering digunakan sebagai langkah awal dalam pemrosesan teks dan analisis teks. Dalam tokenisasi, karakter-karakter tertentu seperti spasi, tanda baca, dan tanda lainnya digunakan sebagai tanda pemisah antara token. Setelah tokenisasi, teks akan menjadi kumpulan token atau kata-kata yang siap untuk diproses lebih lanjut.\n
Berikut ini adalah hasil komentar dari proses tokenisasi.\n
“tiket, parkir, tiket, masuk, tiket, mangrovenya, tiket, seluruh, wahanan, pantai, mangrove, pengembangan, basic, pengelolaannya”
''')
st.markdown('-	Stopword Removal')
st.markdown('''Stopword Removal adalah proses penghapusan kata-kata penghubung atau kata-kata umum yang sering muncul dalam teks dan tidak memberikan kontribusi signifikan pada pemrosesan teks, seperti "dan", "atau", "yang", "di", "ke", dan lain-lain. Hal ini bertujuan untuk mengurangi ukuran dokumen dan meningkatkan efisiensi pemrosesan teks, serta memfokuskan pada kata-kata kunci yang lebih penting dalam analisis. Berikut ini adalah hasil dari proses Stopword Removal.  
\n“tiket parkir tiket masuk tiket mangrovenya tiket seluruh wahanan pantai mangrove pengembangan basic pengelolaannya”
''')
st.markdown('-	Stemming')
st.markdown('Stemming adalah proses dalam pengolahan bahasa alami yang digunakan untuk mengubah kata-kata menjadi bentuk dasar atau akar kata. Tujuan dari stemming adalah untuk mengurangi variasi kata yang serupa menjadi bentuk yang lebih sederhana, sehingga memudahkan dalam analisis teks atau pemrosesan informasi. Dengan menggunakan algoritma stemming, kata-kata yang memiliki akhiran atau imbuhan yang berbeda dapat disederhanakan menjadi bentuk dasar yang memiliki makna yang sama. Contohnya, kata-kata seperti "berlari", "berlari-lari", dan "berlari-lah" akan diubah menjadi kata dasar "lari". Stemming sangat berguna dalam analisis teks, informasi retrieval, dan pengolahan teks lainnya.')

data = [] #deklarasi variabel pada list
data= df['komen'].values.tolist() #masukan data kedalam list

data = [] #deklarasi variabel pada list
data= df['komen'].values.tolist() #masukan data kedalam list
print(data[1]) #cetak data dalam list

import re
dokumenre=[]
for i in data:
    hasil = re.sub(r"\d+", "", i)
    dokumenre.append(hasil)

dokumen2=[]
for i in dokumenre:
    hasil =  i.replace('\n','') 
    dokumen2.append(hasil) 


from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.tokenize import word_tokenize
factory = StopWordRemoverFactory()

stopword  = factory.create_stop_word_remover()

a=len(dokumen2)
dokumenstop=[]
for i in range(0, a):
    sentence = stopword.remove(dokumen2[i])
    dokumenstop.append(sentence)


import string
factory = StopWordRemoverFactory()
dokumenst=[]
for i in dokumenstop:
    output = i.translate(str.maketrans("","",string.punctuation))
    dokumenst.append(output)
    



from sklearn.feature_extraction.text import TfidfTransformer, CountVectorizer
vectorizer = CountVectorizer(min_df=1)
bag = vectorizer.fit_transform(dokumenst)

st.subheader("3. Extraksi fitur")
st.markdown('''Matriks fitur ini menunjukkan kemunculan kata dalam setiap kalimat.
Nilai 1 menandakan bahwa kata tersebut muncul dalam kalimat tersebut, sedangkan nilai 0 menandakan bahwa kata tersebut tidak muncul.
Matriks fitur ini akan menjadi dasar untuk melatih model klasifikasi atau melakukan analisis lebih lanjut terkait teks yang diolah.''')

matrik_vsm=bag.toarray()
a=vectorizer.get_feature_names_out()
print(len(matrik_vsm[:,1]))
#dfb =pd.DataFrame(data=matrik_vsm,index=df,columns=[a])
dfb =pd.DataFrame(data=matrik_vsm,index=list(range(1, len(matrik_vsm[:,1])+1, )),columns=[a])
dfb

tfidf = TfidfTransformer(use_idf=True,norm='l2',smooth_idf=True)
tf=tfidf.fit_transform(vectorizer.fit_transform(dokumenst)).toarray()
dfb =pd.DataFrame(data=tf,index=list(range(1, len(tf[:,1])+1, )),columns=[a])


dfb.to_csv('data_preproses1.csv', index = False)
data1= df['Label']

data1.to_csv('label1.csv',index = False)

tF= pd.read_csv('data_preproses1.csv', index_col =False) #memanggil file tf-idf

data_label = pd.read_csv('label1.csv', index_col = False)

data_baru = pd.concat([tF, data_label],axis = 1) #menggabungkan tabel tf-idf dengan label yang tela ada sebelumnya


from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(data_baru.drop(labels=['Label'], axis=1), data_label, test_size=0.2, random_state=0)

st.subheader("4. Pembagian Data")

st.markdown("setelah preprocessing selesai langkah selanjutnya adalah membagi data menjadi 2 bagian. yaitu data training dan data testing. Data training berjumlah 80 data dan data testing berjumalh 20 data. ")
st.markdown('berikut ini adalah daftar komentar yang akan digunakan menjadi data training. datar dibawah hanya menampilkan nomor dari setiap komentar dan juga menampilkan jumlah kata acara pada setiap komentar. Data training berjumlah 80 komentar.')

# Mengambil kolom pertama dari X_train
kolom_pertama = X_train.iloc[:, 0]
kolom_pertama

st.markdown('Setelah daftar dari data training, selanjutnya adalah daftar data testing yang akan digunakan pada penelitian kali ini. Daftar ini sama dengan daftar pada data training yang mana data test berjumlah 20 komentar.')
xtest = X_test.iloc[:,0]
xtest


st.subheader('5. Penerapan Naive Bayes')
st.markdown('Untuk menerapkan naive bayes penelitian ini menggunakan lbraru MultinomialNB. Setelah dijalan pada program ini didapatkan hasil dari tingkat akurasi yaitu sebesar')

classifier = MultinomialNB()

# Melatih model menggunakan data latih
mnb = classifier.fit(X_train, y_train)

st.markdown(mnb.score(X_test,y_test))



st.markdown('''Hasil dari penelitian ini menunjukkan bahwa dengan menggunakan 100 komentar pengunjung, terdiri dari 50 komentar positif dan 50 komentar negatif, tingkat akurasi analisis sentimen yang dilakukan dengan algoritma Naive Bayes mencapai 85%. Hal ini menunjukkan bahwa algoritma Naive Bayes dapat memberikan prediksi yang cukup akurat dalam mengklasifikasikan komentar-komentar tersebut menjadi kategori positif dan negatif.\n
Penelitian ini memiliki implikasi penting dalam pengembangan dan peningkatan kualitas layanan pariwisata di lokasi Pantai Talang Siring. Dengan menganalisis sentimen dari komentar pengunjung, pihak pengelola dapat memperoleh wawasan yang berharga mengenai kekuatan dan kelemahan lokasi wisata tersebut. Dengan demikian, mereka dapat mengambil tindakan yang tepat untuk meningkatkan layanan dan fasilitas yang disediakan, sehingga dapat meningkatkan tingkat kepuasan pengunjung.\n
Namun, perlu dicatat bahwa penelitian ini menggunakan sampel yang relatif kecil, yaitu 100 komentar. Sehingga, hasil akurasi 85% ini perlu diperhatikan dalam konteks tersebut dan dapat ditingkatkan lagi dengan menggunakan dataset yang lebih besar dan representatif. Selain itu, penelitian ini juga dapat menjadi dasar untuk penelitian lebih lanjut dalam pengembangan analisis sentimen pada lokasi pariwisata lainnya.
 ''')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')
st.markdown('')

