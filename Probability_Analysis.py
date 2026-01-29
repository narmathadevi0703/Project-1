import pandas as pd
import matplotlib.pyplot as plt


def preprocess_dataset(df):
    df = df.copy()

    
    if 'company_size' in df.columns:
        df['company_size'] = (
            df['company_size']
            .astype(str)
            .str.replace(',', '', regex=True)
            .str.extract(r'(\d+)')[0]
        )
        df['company_size'] = pd.to_numeric(df['company_size'], errors='coerce')

    if 'revenue' in df.columns:
        df['revenue'] = (
            df['revenue']
            .astype(str)
            .str.replace('[€,]', '', regex=True)
            .str.replace('B', 'e9', regex=True)
            .str.replace('M', 'e6', regex=True)
            .str.extract(r'(\d+\.?\d*(?:e\d+)?)')[0]
        )
        df['revenue'] = pd.to_numeric(df['revenue'], errors='coerce')

    
    if 'salary' in df.columns:
        def parse_salary(s):
            s = str(s).replace('€', '').replace(',', '').strip()
            if '-' in s:
                try:
                    low, high = s.split('-')
                    return (float(low) + float(high)) / 2
                except:
                    return None
            else:
                try:
                    return float(s)
                except:
                    return None

        df['salary'] = df['salary'].apply(parse_salary)

    return df


def range_stats(df):
    df = df.copy()
    
    numeric_cols = [col for col in ['company_size', 'revenue', 'salary'] if col in df.columns]

    if not numeric_cols:
        print("No numeric columns available for range statistics.")
        return

    for col in numeric_cols:
        series = df[col].dropna()
        rng = series.max() - series.min()
        var = series.var()
        
        print(f"\nStatistics for '{col}':")
        print(f"  Range    : {rng:.2f}")
        print(f"  Variance : {var:.2f}")


def hist_rang(df):
    df = df.copy()
    
    numeric_cols = [col for col in ['company_size', 'revenue', 'salary'] if col in df.columns]

    if not numeric_cols:
        print("No numeric columns available for histogram.")
        return

    for col in numeric_cols:
        series = df[col].dropna()
        plt.figure(figsize=(8, 5))
        plt.hist(series, bins=10, density=True, edgecolor='black', color='skyblue')
        plt.title(f"Probability Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Probability Density")
        plt.grid(True)
        plt.tight_layout()
        plt.show()
