📊 Laporan Evaluasi Model Machine Learning - Stroke Prediction
1. Deskripsi Singkat Dataset
Dataset ini berisi data pasien yang digunakan untuk memprediksi kemungkinan terjadinya stroke berdasarkan beberapa fitur seperti usia, jenis kelamin, status pernikahan, pekerjaan, tempat tinggal, kadar glukosa, BMI, dan kebiasaan merokok.

Jumlah data: 5110
Jumlah fitur: 11 (setelah preprocessing)
Target: stroke (0 = tidak stroke, 1 = stroke)

2. Langkah-langkah Preprocessing
Menghapus kolom id karena tidak berpengaruh pada prediksi.

Mengubah kolom kategorikal biner (gender, ever_married, Residence_type) menjadi angka menggunakan Label Encoding.

Mengubah kolom kategorikal multikategori (work_type, smoking_status) menggunakan One-Hot Encoding.

Melakukan standard scaling pada fitur numerik: age, avg_glucose_level, dan bmi.

Membagi data menjadi training set dan test set dengan rasio 80:20 dan stratifikasi pada label stroke.

3. Model yang Digunakan
Empat model klasifikasi yang digunakan:

Logistic Regression

Random Forest Classifier

XGBoost Classifier

K-Nearest Neighbors (KNN)

4. Hasil Evaluasi Model
### 4. Hasil Evaluasi Model

| Model               | Accuracy | Precision (class 1) | Recall (class 1) | F1-Score (class 1) | ROC-AUC |
|---------------------|----------|----------------------|------------------|---------------------|---------|
| Logistic Regression | 0.75     | 0.14                 | 0.24             | 0.84                | 0.80    |
| Random Forest       | 0.95     | 0.00                 | 0.00             | 0.78                | 0.00    |
| XGBoost             | 0.93     | 0.15                 | 0.10             | 0.79                | 0.08    |
| KNN                 | 0.94     | 0.00                 | 0.00             | 0.76                | 0.00    |
76                | 0.00    |


5. Interpretasi dan Pemilihan Model Terbaik
Logistic Regression memberikan baseline yang baik dengan ROC-AUC tinggi, namun precision dan f1-score rendah untuk kelas stroke (positif).

Random Forest sangat akurat terhadap kelas mayoritas, tetapi gagal mengenali kelas stroke sama sekali.

XGBoost menghasilkan ROC-AUC tertinggi dan sedikit lebih baik dalam mendeteksi kasus stroke dibanding Random Forest dan KNN.

KNN memiliki akurasi tinggi secara keseluruhan, tetapi tidak mampu mengidentifikasi kasus stroke (semua diprediksi sebagai 0).

🟢 Model Terbaik: XGBoost

Alasan pemilihan:

Meskipun recall rendah, XGBoost masih mampu mengenali beberapa kasus stroke.

ROC-AUC yang tinggi menunjukkan kemampuan model membedakan antara dua kelas cukup baik, bahkan dalam kondisi data yang imbalance.

Model ini juga fleksibel dan bisa ditingkatkan performanya dengan tuning hyperparameter.
