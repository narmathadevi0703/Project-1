import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def clean_numeric_columns(df):
    df = df.copy()

    ranking_cols = [
        'Academic Reputation',
        'Employer Reputation',
        'Faculty Student',
        'Citations per Faculty',
        'International Faculty',
        'International Students',
        'International Research Network',
        'Employment Outcomes',
        'Sustainability',
        'QS Overall Score'
    ]

    for col in ranking_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace('[^0-9.]', '', regex=True)
            )
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df


def Pair_plot(df):
    df = clean_numeric_columns(df)

    key_cols = [
        'Academic Reputation',
        'Citations per Faculty',
        'Employer Reputation',
        'QS Overall Score'
    ]

    df = df.dropna(subset=key_cols)

    sns.pairplot(df[key_cols])

    plt.suptitle(
        'Pair Plot of Key QS Ranking Indicators',
        y=1.02
    )
    plt.show()


def Heat_plot(df):
    df = clean_numeric_columns(df)

    key_cols = [
        'Academic Reputation',
        'Citations per Faculty',
        'Employer Reputation',
        'QS Overall Score'
    ]

    corr = df[key_cols].corr()

    plt.figure(figsize=(6, 5))
    sns.heatmap(
        corr,
        annot=True,
        cmap='coolwarm',
        fmt=".2f"
    )

    plt.title('Correlation Heatmap of QS Ranking Indicators')
    plt.tight_layout()
    plt.show()


def Heat_cov(df):
    df = clean_numeric_columns(df)

    key_cols = [
        'Academic Reputation',
        'Citations per Faculty',
        'Employer Reputation',
        'QS Overall Score'
    ]

    cov = df[key_cols].cov()

    plt.figure(figsize=(6, 5))
    sns.heatmap(
        cov,
        annot=True,
        cmap='coolwarm',
        fmt=".2f"
    )

    plt.title('Covariance Heatmap of QS Ranking Indicators')
    plt.tight_layout()
    plt.show()
