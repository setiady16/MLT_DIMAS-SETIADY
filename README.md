📊 Laporan Evaluasi Model Machine Learning - Stroke Prediction
1. Deskripsi Singkat Dataset
Dataset ini berisi data pasien yang digunakan untuk memprediksi kemungkinan terjadinya stroke berdasarkan beberapa fitur seperti:

Jumlah data: 5110
Jumlah fitur: 11 (setelah preprocessing)
Target: stroke (0 = tidak stroke, 1 = stroke)

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
   
| Model               | Accuracy | Precision (class 1) | Recall (class 1) | F1-Score (class 1) | ROC-AUC |
| ------------------- | -------- | ------------------- | ---------------- | ------------------ | ------- |
| Logistic Regression | 0.75     | 0.14                | 0.24             | 0.20               | 0.80    |
| Random Forest       | 0.95     | 0.00                | 0.00             | 0.00               | 0.78    |
| XGBoost             | 0.93     | 0.15                | 0.10             | 0.12               | 0.79    |
| KNN                 | 0.94     | 0.00                | 0.00             | 0.00               | 0.76    |


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
