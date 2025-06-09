# 1. Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from sklearn.metrics import classification_report, confusion_matrix, roc_auc_score
from sklearn.preprocessing import LabelEncoder, StandardScaler

# 2. Load dataset dari Google Drive
url = "https://drive.google.com/uc?export=download&id=10THN9kB_RssZlg6fc3DubQpnLJAO_k44"
df = pd.read_csv(url)

# 3. Cek dan tangani missing value
df['bmi'].fillna(df['bmi'].median(), inplace=True)

# 4. Cek duplikasi
print("Jumlah duplikat:", df.duplicated().sum())

# 5. Encoding variabel kategorikal
label_cols = ['gender', 'ever_married', 'Residence_type']
le = LabelEncoder()
for col in label_cols:
    df[col] = le.fit_transform(df[col])

df = pd.get_dummies(df, columns=['work_type', 'smoking_status'], drop_first=True)

# 6. Pisahkan fitur dan target
X = df.drop(columns=['id', 'stroke'])
y = df['stroke']

# 7. Tampilkan distribusi kelas target
print("Distribusi kelas stroke:")
print(y.value_counts(normalize=True))

# 8. Scaling fitur numerik
scaler = StandardScaler()
X[['age', 'avg_glucose_level', 'bmi']] = scaler.fit_transform(X[['age', 'avg_glucose_level', 'bmi']])

# 9. Split data menjadi train dan test set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 10. Logistic Regression
lr = LogisticRegression(class_weight='balanced', random_state=42)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)
y_proba_lr = lr.predict_proba(X_test)[:, 1]

print("\n=== Logistic Regression ===")
print(confusion_matrix(y_test, y_pred_lr))
print(classification_report(y_test, y_pred_lr))
print("ROC-AUC Score: {:.2f}".format(roc_auc_score(y_test, y_proba_lr)))

# 11. Random Forest
rf = RandomForestClassifier(class_weight='balanced', random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)
y_proba_rf = rf.predict_proba(X_test)[:, 1]

print("\n=== Random Forest ===")
print(confusion_matrix(y_test, y_pred_rf))
print(classification_report(y_test, y_pred_rf))
print("ROC-AUC Score: {:.2f}".format(roc_auc_score(y_test, y_proba_rf)))

# 12. XGBoost
xgb = XGBClassifier(scale_pos_weight=5, use_label_encoder=False, eval_metric='logloss', random_state=42)
xgb.fit(X_train, y_train)
y_pred_xgb = xgb.predict(X_test)
y_proba_xgb = xgb.predict_proba(X_test)[:, 1]

print("\n=== XGBoost ===")
print(confusion_matrix(y_test, y_pred_xgb))
print(classification_report(y_test, y_pred_xgb))
print("ROC-AUC Score: {:.2f}".format(roc_auc_score(y_test, y_proba_xgb)))

# 13. K-Nearest Neighbors
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
y_proba_knn = knn.predict_proba(X_test)[:, 1]

print("\n=== K-Nearest Neighbors ===")
print(confusion_matrix(y_test, y_pred_knn))
print(classification_report(y_test, y_pred_knn))
print("ROC-AUC Score: {:.2f}".format(roc_auc_score(y_test, y_proba_knn)))

# 14. Perbandingan ROC-AUC Score semua model
print("\n=== Perbandingan ROC-AUC Score ===")
print("Logistic Regression: {:.2f}".format(roc_auc_score(y_test, y_proba_lr)))
print("Random Forest      : {:.2f}".format(roc_auc_score(y_test, y_proba_rf)))
print("XGBoost            : {:.2f}".format(roc_auc_score(y_test, y_proba_xgb)))
print("KNN                : {:.2f}".format(roc_auc_score(y_test, y_proba_knn)))