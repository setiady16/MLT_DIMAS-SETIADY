<<<<<<< HEAD
📊 Laporan Evaluasi Model Machine Learning - Stroke Prediction
1. Deskripsi Singkat Dataset
Dataset ini berisi data pasien yang digunakan untuk memprediksi kemungkinan terjadinya stroke berdasarkan beberapa fitur seperti:
=======
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
- *Sumber Dataset Kaggle, [Online]. Available:* https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset

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

### Solution Statement

Untuk mencapai tujuan di atas, beberapa solusi akan diuji dan dibandingkan:

- **Baseline model:** Logistic Regression – sebagai model sederhana dan interpretable.  
- **Model alternatif:**  
  - Random Forest Classifier  
  - XGBoost Classifier  
  - K-Nearest Neighbors  

Setiap model akan dievaluasi menggunakan metrik berikut:

- Accuracy  
- Precision  
- Recall  
- F1-Score  
- ROC-AUC (untuk mengevaluasi performa model terhadap imbalance class)

---




# 📊 Laporan Evaluasi Model Machine Learning - Stroke Prediction

## 1. Deskripsi Singkat Dataset
Dataset ini berisi data pasien yang digunakan untuk memprediksi kemungkinan terjadinya stroke berdasarkan beberapa fitur seperti usia, jenis kelamin, status pernikahan, pekerjaan, tempat tinggal, kadar glukosa, BMI, dan kebiasaan merokok.
>>>>>>> ac3d7a4 (Done)

- **Jumlah data:** 5110  
- **Jumlah fitur:** 11 (setelah preprocessing)  
- **Target:** stroke (0 = tidak stroke, 1 = stroke)

<<<<<<< HEAD
2. Langkah-langkah Preprocessing
- Menghapus kolom id karena tidak berpengaruh pada prediksi.
- Mengubah kolom kategorikal biner (gender, ever_married, Residence_type) menjadi angka menggunakan Label Encoding.
- Mengubah kolom multikategori (work_type, smoking_status) menggunakan One-Hot Encoding.
- Melakukan Standard Scaling pada fitur numerik: age, avg_glucose_level, dan bmi.
- Membagi data menjadi training dan testing dengan rasio 80:20 serta stratifikasi label stroke.
- 
3. Model yang Digunakan
Empat model klasifikasi yang digunakan:
- Logistic Regression
- Random Forest Classifier
- XGBoost Classifier
- K-Nearest Neighbors (KNN)

4. Hasil Evaluasi Model
   
=======
## 2. Langkah-langkah Preprocessing
- Menghapus kolom `id` karena tidak berpengaruh pada prediksi.  
- Mengubah kolom kategorikal biner (`gender`, `ever_married`, `Residence_type`) menjadi angka menggunakan Label Encoding.  
- Mengubah kolom kategorikal multikategori (`work_type`, `smoking_status`) menggunakan One-Hot Encoding.  
- Melakukan standard scaling pada fitur numerik: `age`, `avg_glucose_level`, dan `bmi`.  
- Membagi data menjadi training set dan test set dengan rasio 80:20 dan stratifikasi pada label stroke.  

## 3. Model yang Digunakan
Empat model klasifikasi yang digunakan:  
- Logistic Regression  
- Random Forest Classifier  
- XGBoost Classifier  
- K-Nearest Neighbors (KNN)  

## 4. Hasil Evaluasi Model

>>>>>>> ac3d7a4 (Done)
| Model               | Accuracy | Precision (class 1) | Recall (class 1) | F1-Score (class 1) | ROC-AUC |
| ------------------- | -------- | ------------------- | ---------------- | ------------------ | ------- |
| Logistic Regression | 0.75     | 0.14                | 0.24             | 0.20               | 0.80    |
| Random Forest       | 0.95     | 0.00                | 0.00             | 0.00               | 0.78    |
| XGBoost             | 0.93     | 0.15                | 0.10             | 0.12               | 0.79    |
| KNN                 | 0.94     | 0.00                | 0.00             | 0.00               | 0.76    |

## 5. Interpretasi dan Pemilihan Model Terbaik
- Logistic Regression memberikan baseline yang baik dengan ROC-AUC tinggi, namun precision dan f1-score rendah untuk kelas stroke (positif).  
- Random Forest sangat akurat terhadap kelas mayoritas, tetapi gagal mengenali kelas stroke sama sekali.  
- XGBoost menghasilkan ROC-AUC tertinggi dan sedikit lebih baik dalam mendeteksi kasus stroke dibanding Random Forest dan KNN.  
- KNN memiliki akurasi tinggi secara keseluruhan, tetapi tidak mampu mengidentifikasi kasus stroke (semua diprediksi sebagai 0).  

<<<<<<< HEAD
5. Interpretasi dan Pemilihan Model Terbaik
Logistic Regression memberikan baseline yang baik dengan ROC-AUC tinggi, namun precision dan F1-score untuk kelas stroke masih rendah.

Random Forest sangat akurat terhadap kelas mayoritas (non-stroke), namun gagal mengenali kelas stroke sama sekali.

XGBoost menghasilkan ROC-AUC yang cukup tinggi dan lebih baik dalam mendeteksi kasus stroke dibanding model lainnya.

KNN juga akurat secara keseluruhan, tetapi sepenuhnya gagal mengenali kasus stroke (semua diprediksi sebagai 0).

🟢 Model Terbaik: XGBoost
Alasan pemilihan:

Mampu mengenali sebagian kasus stroke meskipun dengan recall rendah.

ROC-AUC tinggi menandakan kemampuan diskriminatif yang baik, terutama pada dataset yang imbalanced.

Model fleksibel dan masih bisa ditingkatkan dengan tuning hyperparameter.
=======
🟢 **Model Terbaik: XGBoost**

**Alasan pemilihan:**  
- Meskipun recall rendah, XGBoost masih mampu mengenali beberapa kasus stroke.  
- ROC-AUC yang tinggi menunjukkan kemampuan model membedakan antara dua kelas cukup baik, bahkan dalam kondisi data yang imbalance.  
- Model ini juga fleksibel dan bisa ditingkatkan performanya dengan tuning hyperparameter.  
>>>>>>> ac3d7a4 (Done)
