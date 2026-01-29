import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report

def knn_modeling(df):

    label_encoder = LabelEncoder()
    df['target_encoded'] = label_encoder.fit_transform(df['Location Full'].astype(str))

   
    df['academic_rep_clean'] = pd.to_numeric(df['Academic Reputation'], errors='coerce')
    df['employer_rep_clean'] = pd.to_numeric(df['Employer Reputation'], errors='coerce')
    df['citations_clean'] = pd.to_numeric(df['Citations per Faculty'], errors='coerce')
    df['sustainability_clean'] = pd.to_numeric(df['Sustainability'], errors='coerce')
    df['score_clean'] = pd.to_numeric(df['QS Overall Score'], errors='coerce')

    
    X = df[['academic_rep_clean', 'employer_rep_clean', 'citations_clean', 'sustainability_clean', 'score_clean']]
    y = df['target_encoded']

   
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X.fillna(0))

 
    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)

 
    y_pred = knn.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print(classification_report(y_test, y_pred))