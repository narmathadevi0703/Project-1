import matplotlib.pyplot as plt
import pandas as pd



def Line_plot(df):
    df = df.copy()


    filtered = df[df['Location Full'].isin([
        'United States',
        'United Kingdom',
        'China (Mainland)',
        'India',
        'Germany'
    ])]

 
    filtered['QS Overall Score'] = pd.to_numeric(
        filtered['QS Overall Score'],
        errors='coerce'
    )

    filtered = filtered.dropna(subset=['QS Overall Score'])


    avg_score = (
        filtered
        .groupby('Location Full')['QS Overall Score']
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(10, 6))
    plt.plot(
        avg_score.index,
        avg_score.values,
        marker='o',
        linestyle='-'
    )

    plt.title('Average QS Overall Score by Country (QS 2025)')
    plt.xlabel('Country')
    plt.ylabel('Average QS Overall Score')
    plt.xticks(rotation=30)
    plt.grid(True)
    plt.tight_layout()
    plt.show()



def Bar_plot(df):
    df = df.copy()


    df['Citations per Faculty'] = pd.to_numeric(
        df['Citations per Faculty'], errors='coerce' )

    
    df = df.dropna(subset=['Citations per Faculty', 'Size'])

   
    size_avg = (
        df
        .groupby('Size')['Citations per Faculty']
        .mean()
        .sort_values()
    )

    plt.figure(figsize=(8, 5))
    plt.bar(
        size_avg.index,
        size_avg.values
    )

    plt.title('Bar Plot: Average Citations per Faculty by University Size')
    plt.xlabel('University Size')
    plt.ylabel('Average Citations per Faculty')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()



def hist_plot(df):
    df = df.copy()

   
    scores = pd.to_numeric(
        df['QS Overall Score'], errors='coerce'
    ).dropna()

    if scores.empty:
        print("No valid QS Overall Score data found.")
        return

    plt.figure(figsize=(8, 5))
    plt.hist(scores, bins=10, edgecolor='black')

    plt.title('Histogram: Distribution of QS Overall Scores')
    plt.xlabel('QS Overall Score')
    plt.ylabel('Number of Universities')
    plt.tight_layout()
    plt.show()
