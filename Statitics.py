import pandas as pd

def stats(df):
    df = df.copy()
    ranking_numeric_cols = [
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

    for col in ranking_numeric_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace('[^0-9.]', '', regex=True)
            )
            df[col] = pd.to_numeric(df[col], errors='coerce')

 
    cols = df.select_dtypes(include='number').columns

    if cols.empty:
        print("No numerical university ranking indicators found for descriptive statistics.")
        return

    
    for c in cols:
        print(f"\nDescriptive Statistics for {c}")
        print("Mean   :", df[c].mean())
        print("Median :", df[c].median())
        print("Mode   :", df[c].mode().iloc[0] if not df[c].mode().empty else "No Mode")
        print("Std Dev:", df[c].std())
