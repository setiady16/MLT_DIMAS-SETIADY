# **Proyek Predictive Analytics : Prediksi Risiko Stroke**

## Domain Proyek

Stroke merupakan salah satu penyebab utama kematian dan kecacatan di dunia. Menurut data dari World Health Organization (WHO), sekitar 15 juta orang di dunia mengalami stroke setiap tahun. Dari jumlah tersebut, sekitar 5 juta orang meninggal dan 5 juta lainnya menjadi cacat permanen akibat komplikasi yang ditimbulkan [WHO, 2023].

Stroke dapat dicegah apabila faktor risikonya seperti tekanan darah tinggi, diabetes, merokok, obesitas, dan gaya hidup tidak sehat dapat dideteksi dan dikendalikan sedini mungkin. Namun, deteksi dini sering kali terhambat karena keterbatasan sumber daya medis, terutama di negara berkembang.

Dengan berkembangnya teknologi dan ketersediaan data kesehatan, pendekatan berbasis machine learning dapat membantu memprediksi risiko stroke secara otomatis dan cepat. Model prediktif ini dapat digunakan oleh tenaga medis atau aplikasi kesehatan digital untuk memberi peringatan dini bagi pasien yang berisiko tinggi.

### Mengapa dan Bagaimana Masalah Ini Harus Diselesaikan

Masalah ini penting untuk diselesaikan karena:

- Stroke bisa dicegah jika faktor risikonya dikenali sejak dini.  
- Sistem prediksi berbasis machine learning dapat membantu dalam skrining awal, terutama di daerah dengan akses terbatas ke tenaga medis.  
- Efisiensi waktu dan biaya: deteksi awal melalui data digital mengurangi kebutuhan uji klinis yang mahal dan memakan waktu.

Dengan membangun model prediksi stroke, instansi kesehatan, rumah sakit, maupun aplikasi kesehatan personal dapat memberikan peringatan atau rekomendasi medis yang lebih tepat dan personal.

### Referensi

- World Health Organization. (2023). Stroke: Key Facts. Diakses dari: https://www.who.int/news-room/fact-sheets/detail/stroke  
- Benjamin, E. J., et al. (2019). Heart disease and stroke statistics—2019 update: a report from the American Heart Association. Circulation, 139(10), e56–e528. https://doi.org/10.1161/CIR.0000000000000659  
- Feigin, V. L., et al. (2021). Global, regional, and national burden of stroke and its risk factors, 1990–2019: a systematic analysis for the Global Burden of Disease Study 2019. The Lancet Neurology, 20(10), 795–820.


---

## Business Understanding

### Problem Statement

Stroke merupakan penyakit yang dapat menyebabkan kematian atau kecacatan jangka panjang. Banyak pasien stroke datang ke rumah sakit setelah gejala muncul, padahal stroke dapat dicegah jika faktor risikonya terdeteksi lebih awal. Masalah utamanya adalah:

- Bagaimana cara mengidentifikasi individu yang berisiko mengalami stroke berdasarkan data profil kesehatan mereka?  
- Dapatkah kita membangun model machine learning yang mampu memprediksi risiko stroke secara akurat dan efisien?

### Goals

Tujuan dari proyek ini adalah:

- Mengembangkan model machine learning untuk memprediksi risiko stroke berdasarkan fitur-fitur seperti usia, tekanan darah, kadar glukosa, riwayat hipertensi, dan kebiasaan merokok.  
- Memberikan solusi prediktif yang bisa diintegrasikan dalam sistem pendukung keputusan medis (Clinical Decision Support System), atau aplikasi kesehatan digital untuk masyarakat umum.  
- Membantu pencegahan stroke dini melalui identifikasi kelompok berisiko tinggi secara otomatis.



---

## Data Understanding

Dataset yang digunakan dalam proyek ini adalah Stroke Prediction Dataset, tersedia di: https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset. Dataset ini dirancang untuk memprediksi kemungkinan seseorang mengalami stroke berdasarkan berbagai faktor risiko klinis dan demografis.


### Ringkasan Dataset

- Jumlah Baris: 5.110
- Jumlah Kolom: 12 
- Variabel Target: stroke (biner: 0 = tidak stroke, 1 = stroke)
- Tipe Data:
  - Numerik: id (integer), age (float), avg_glucose_level (float), bmi (float)
  - Kategorikal: gender (object), ever_married (object), work_type (object), Residence_type (object), smoking_status (object)
  - Biner: hypertension (integer: 0 atau 1), heart_disease (integer: 0 atau 1), stroke (integer: 0 atau 1)

### Deskripsi Fitur

Dataset ini memiliki 12 kolom berikut:
1. id: Pengenal unik untuk setiap individu (integer).
2. gender: Jenis kelamin individu, dengan kategori 'Male', 'Female', atau 'Other' (object).
3. age: Usia individu dalam tahun (float, berkisar dari 0,08 hingga 82).
4. hypertension: Menunjukkan apakah individu memiliki hipertensi (0 = tidak, 1 = ya, integer).
5. heart_disease: Menunjukkan apakah individu memiliki penyakit jantung (0 = tidak, 1 = ya, integer).
6. ever_married: Status pernikahan, dengan kategori 'Yes' atau 'No' (object).
7. work_type: Jenis pekerjaan, dengan kategori 'children', 'Govt_job', 'Never_worked', 'Private', dan 'Self-employed' (object).
8. Residence_type: Tempat tinggal, dengan kategori 'Urban' atau 'Rural' (object).
9. avg_glucose_level: Rata-rata kadar glukosa darah individu (float, berkisar dari 55,12 hingga 271,74).
10. bmi: Indeks Massa Tubuh (Body Mass Index), menunjukkan proporsi berat dan tinggi badan (float, berkisar dari 10,3 hingga 97,6).
11. smoking_status: Kebiasaan merokok, dengan kategori 'formerly smoked', 'never smoked', 'smokes', atau 'Unknown' (object).
12. stroke: Variabel target yang menunjukkan apakah individu mengalami stroke (0 = tidak, 1 = ya, integer).


### Kondisi Data Awal

- Nilai yang Hilang: Dataset memiliki nilai yang hilang pada kolom bmi, dengan 201 entri kosong (sekitar 3,9% dari total 5.110 baris). Tidak ada kolom lain yang memiliki nilai yang hilang.
- Duplikasi: Tidak ada baris duplikat dalam dataset, sebagaimana dikonfirmasi dengan pemeriksaan df.duplicated().sum().
- Ketidakseimbangan Kelas: Variabel target stroke sangat tidak seimbang, dengan hanya 249 kasus stroke (1) dibandingkan 4.861 kasus tanpa stroke (0), mewakili sekitar 4,9% kasus positif.

### Sumber Dataset

Dataset ini tersedia secara publik di Kaggle: Stroke Prediction Dataset . Dataset ini cocok untuk mengembangkan model Miroslav Stanković model machine learning untuk prediksi kesehatan, khususnya untuk deteksi dini risiko stroke.


---

## Data Preparation

Untuk mempersiapkan dataset agar dapat digunakan dalam pelatihan model machine learning, beberapa langkah preprocessing dilakukan sesuai dengan urutan eksekusi berikut:

1. Penanganan Nilai yang Hilang:
- Kolom bmi memiliki 201 nilai yang hilang (3,9% dari data). Nilai yang hilang diisi dengan median kolom bmi untuk menjaga distribusi data.

2. Pemeriksaan Duplikasi:
- Dataset diperiksa untuk memastikan tidak ada baris duplikat, dan hasilnya menunjukkan tidak ada duplikasi.

3. Encoding Kolom Kategorikal Biner:
- Kolom kategorikal biner (gender, ever_married, Residence_type) diubah menjadi nilai numerik menggunakan Label Encoding untuk mempermudah pemrosesan model.

4. Encoding Kolom Kategorikal Multikategori:
- Kolom kategorikal multikategori (work_type, smoking_status) diubah menjadi fitur biner menggunakan One-Hot Encoding untuk menangani kategori yang tidak memiliki hubungan ordinal.

5. Penghapusan Kolom Tidak Relevan:
- Kolom id dihapus karena tidak memberikan kontribusi pada prediksi. Kolom stroke dipisahkan sebagai variabel target.

6. Scaling Fitur Numerik:
- Fitur numerik (age, avg_glucose_level, bmi) diskalakan menggunakan StandardScaler untuk menormalkan rentang nilai, yang penting untuk algoritma sensitif terhadap skala seperti KNN.

7. Pembagian Data:
- Dataset dibagi menjadi training set (80%) dan test set (20%) dengan stratifikasi pada kolom stroke untuk menjaga proporsi kelas yang tidak seimbang.

Outlier pada fitur numerik tidak dihapus karena tidak ada indikasi kuat bahwa outlier tersebut adalah kesalahan data, dan mereka mungkin mencerminkan variasi nyata dalam populasi.


---

## Modeling

Untuk memprediksi risiko stroke, empat algoritma machine learning digunakan: Logistic Regression, Random Forest Classifier, XGBoost Classifier, dan K-Nearest Neighbors (KNN). Berikut adalah penjelasan cara kerja dan parameter utama untuk setiap model:

1. Logistic Regression:
- Cara Kerja: Logistic Regression adalah algoritma klasifikasi linier yang memprediksi probabilitas suatu observasi termasuk dalam kelas tertentu menggunakan fungsi sigmoid. Model ini cocok untuk data dengan hubungan linier antar fitur dan target, serta mudah diinterpretasikan.
- Parameter Utama:
  - class_weight='balanced': Menyesuaikan bobot kelas untuk menangani ketidakseimbangan data.
  - Parameter default lainnya dari scikit-learn digunakan (misalnya, solver='lbfgs', max_iter=100).

2. Random Forest Classifier:
- Cara Kerja: Random Forest adalah algoritma ensemble berbasis pohon keputusan. Model ini membangun beberapa pohon keputusan pada subset data yang berbeda dan menggabungkan prediksi mereka melalui voting mayoritas. Random Forest kuat terhadap overfitting dan cocok untuk data dengan fitur non-linier.
- Parameter Utama:
  - n_estimators=100: Jumlah pohon keputusan yang dibangun.
  - Parameter default lainnya digunakan (misalnya, max_depth=None, min_samples_split=2).

3. XGBoost Classifier:
- Cara Kerja: XGBoost (Extreme Gradient Boosting) adalah algoritma ensemble berbasis pohon yang menggunakan teknik gradient boosting. Model ini mengoptimalkan fungsi kerugian dengan menambahkan pohon secara berurutan, dengan setiap pohon memperbaiki kesalahan prediksi pohon sebelumnya. XGBoost efektif untuk data tidak seimbang dengan penyesuaian parameter seperti bobot kelas.
- Parameter Utama:
  - scale_pos_weight=19: Menyesuaikan bobot kelas minoritas berdasarkan rasio ketidakseimbangan (4861/249 ≈ 19).
  - Parameter default lainnya digunakan (misalnya, max_depth=6, learning_rate=0.3).

4. K-Nearest Neighbors (KNN):
- Cara Kerja: KNN adalah algoritma berbasis jarak yang mengklasifikasikan observasi berdasarkan mayoritas kelas dari k tetangga terdekat dalam ruang fitur. Algoritma ini sensitif terhadap skala fitur, sehingga scaling data sangat penting.
- Parameter Utama:
  - n_neighbors=5: Jumlah tetangga yang dipertimbangkan untuk klasifikasi.
  - Parameter default lainnya digunakan (misalnya, weights='uniform', metric='minkowski').

Setiap model dilatih pada training set (80% data) dan dievaluasi pada test set (20% data) menggunakan metrik Accuracy, Precision, Recall, F1-Score, dan ROC-AUC.


---

## Evaluation

Bagian ini menyajikan hasil evaluasi performa model berdasarkan metrik Accuracy, Precision, Recall, F1-Score, dan ROC-AUC pada test set. Metrik ini dipilih untuk mengevaluasi kemampuan model dalam mendeteksi kasus stroke (kelas 1), dengan mempertimbangkan ketidakseimbangan kelas (4,9% kasus positif).


### Hasil Evaluasi


| Model               | Accuracy | Precision (class 1) | Recall (class 1) | F1-Score (class 1) | ROC-AUC |
| ------------------- | -------- | ------------------- | ---------------- | ------------------ | ------- |
| Logistic Regression | 0.75     | 0.14                | 0.80             | 0.24               | 0.84    |
| Random Forest       | 0.95     | 0.00                | 0.00             | 0.00               | 0.78    |
| XGBoost             | 0.94     | 0.19                | 0.10             | 0.13               | 0.79    |
| KNN                 | 0.94     | 0.00                | 0.00             | 0.00               | 0.60    |


### Analisis dan Interpretasi

1. Logistic Regression:
- Recall (0.80): Model ini mendeteksi 80% kasus stroke, menjadikannya efektif untuk skrining awal di mana mengidentifikasi sebanyak mungkin kasus positif adalah prioritas.
- Precision (0.14): Rendahnya precision menunjukkan banyak false positive, yang dapat menyebabkan alarm berlebihan dalam aplikasi klinis.
- ROC-AUC (0.84): Nilai tertinggi di antara model, menunjukkan kemampuan baik dalam membedakan kelas.

2. Random Forest:
- Accuracy (0.95): Akurasi tinggi karena model sangat baik memprediksi kelas mayoritas (tidak stroke).
- Precision, Recall, F1-Score (0.00): Gagal mendeteksi kelas stroke, kemungkinan karena ketidakseimbangan kelas tidak ditangani dengan baik.
- ROC-AUC (0.78): Lebih rendah dari Logistic Regression, menunjukkan performa diskriminasi yang lebih lemah.

3. XGBoost:
- Recall (0.10): Hanya mendeteksi 10% kasus stroke, tetapi lebih baik dibandingkan Random Forest dan KNN.
- Precision (0.19): Lebih tinggi dari Logistic Regression, menunjukkan lebih sedikit false positive.
- ROC-AUC (0.79): Mendekati Logistic Regression, menunjukkan kemampuan diskriminasi yang baik.
- F1-Score (0.13): Keseimbangan antara precision dan recall lebih baik dibandingkan Random Forest dan KNN.

4. KNN:
- Accuracy (0.94): Akurasi tinggi karena memprediksi kelas mayoritas dengan baik.
- Precision, Recall, F1-Score (0.00): Gagal mendeteksi kelas stroke, kemungkinan karena sensitivitas terhadap ketidakseimbangan kelas dan distribusi data.
- ROC-AUC (0.60): Terendah di antara model, menunjukkan performa diskriminasi yang paling lemah.

### Pemilihan Model Terbaik

🟢 Model Terbaik: XGBoost

Alasan pemilihan:
- Meskipun recall rendah (0.10), XGBoost mampu mengenali beberapa kasus stroke, yang lebih baik dibandingkan Random Forest dan KNN.
- Precision (0.19) lebih tinggi dari Logistic Regression, menunjukkan lebih sedikit false positive.
- ROC-AUC (0.79) menunjukkan kemampuan model membedakan kelas dengan baik meskipun data tidak seimbang.
- Model ini fleksibel dan dapat ditingkatkan dengan tuning hyperparameter lebih lanjut, seperti menyesuaikan learning_rate atau menggunakan teknik oversampling seperti SMOTE.


## Catatan Evaluasi

Ketidakseimbangan kelas (4,9% kasus positif) sangat memengaruhi performa model, terutama Random Forest dan KNN, yang gagal mendeteksi kelas stroke. Logistic Regression memiliki recall tinggi tetapi precision rendah, cocok untuk skrining awal. XGBoost memberikan keseimbangan terbaik antara deteksi kelas minoritas dan pengendalian false positive.


---

### Solution Statement

Untuk mencapai tujuan di atas, beberapa solusi diuji dan dibandingkan:
- Baseline model: Logistic Regression – sebagai model sederhana dan interpretable.
- Model alternatif:
  - Random Forest Classifier
  - XGBoost Classifier
  - K-Nearest Neighbors

Setiap model dievaluasi menggunakan metrik Accuracy, Precision, Recall, F1-Score, dan ROC-AUC.


---


# 📊 Laporan Evaluasi Model Machine Learning - Stroke Prediction

## 1. Langkah-langkah Preprocessing

Ringkasan Hasil:

- Empat model (Logistic Regression, Random Forest, XGBoost, KNN) diuji untuk memprediksi risiko stroke. XGBoost dipilih sebagai model terbaik karena mampu mendeteksi beberapa kasus stroke (recall = 0.10) dengan precision yang lebih baik (0.19) dibandingkan model lain, serta memiliki ROC-AUC tinggi (0.79). Ketidakseimbangan kelas menjadi tantangan utama, yang menyebabkan Random Forest dan KNN gagal mendeteksi kelas stroke.
