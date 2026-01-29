import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

def KMeans_clustering(data):
    
    df = pd.DataFrame(data)

    df['academic_rep_clean'] = pd.to_numeric(df['Academic Reputation'], errors='coerce')


    df['employer_rep_clean'] = pd.to_numeric(df['Employer Reputation'], errors='coerce')

   
    df['citations_clean'] = pd.to_numeric(df['Citations per Faculty'], errors='coerce')


    df['sustainability_clean'] = pd.to_numeric(df['Sustainability'], errors='coerce')


    df['score_clean'] = pd.to_numeric(df['QS Overall Score'], errors='coerce')


    X = df[['academic_rep_clean', 'employer_rep_clean', 'citations_clean', 'sustainability_clean', 'score_clean']].fillna(0)


    scaler = StandardScaler()
    scaled = scaler.fit_transform(X)

 
    kmeans = KMeans(n_clusters=3, random_state=98)
    df['Cluster'] = kmeans.fit_predict(scaled)

  
    plt.figure(figsize=(8, 6))
    plt.scatter(
        df['academic_rep_clean'],
        df['score_clean'],
        c=df['Cluster'],
        cmap='viridis',
        s=100
    )

    plt.xlabel("Academic Reputation")
    plt.ylabel("QS Overall Score")
    plt.title("k-Means Clustering of Universities (Scatter Plot)")
    plt.colorbar(label="Cluster")
    plt.tight_layout()
    plt.show()
  

   
    print("Cluster 1 Data (Universities with lower scores):")
    print(df[df['Cluster'] == 0])

    print("\nCluster 2 Data (Universities with mid-range scores):")
    print(df[df['Cluster'] == 1])

    print("\nCluster 3 Data (Universities with high scores):")
    print(df[df['Cluster'] == 2])

    print("\nComplete Data with Cluster Labels:")
    print(df)

    return df