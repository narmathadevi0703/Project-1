import pandas as pd

def clean_numeric_columns(df):
    df = df.copy()

    numeric_cols = [
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

    for col in numeric_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.replace('[^0-9.]', '', regex=True)
            )

            # SAFE numeric conversion
            df[col] = pd.to_numeric(df[col], errors='coerce')

    return df


def academic_reputation_outliers(df):
    df = clean_numeric_columns(df)

    qt1 = df['Academic Reputation'].quantile(0.25)
    qt3 = df['Academic Reputation'].quantile(0.75)
    iqr = qt3 - qt1

    print(f"\nAcademic Reputation IQR (Interquartile Range): {iqr}")

    lower_bound = qt1 - 1.5 * iqr
    upper_bound = qt3 + 1.5 * iqr

    outliers = df[
        (df['Academic Reputation'] < lower_bound) |
        (df['Academic Reputation'] > upper_bound)
    ]

    print("\nAcademic Reputation Outliers:")
    print(outliers[['Institution Name', 'Academic Reputation']])

def citations_per_faculty_outliers(df):
    df = clean_numeric_columns(df)

    qt1 = df['Citations per Faculty'].quantile(0.25)
    qt3 = df['Citations per Faculty'].quantile(0.75)
    iqr = qt3 - qt1

    print(f"\nCitations per Faculty IQR (Interquartile Range): {iqr}")

    lower_bound = qt1 - 1.5 * iqr
    upper_bound = qt3 + 1.5 * iqr

    outliers = df[
        (df['Citations per Faculty'] < lower_bound) |
        (df['Citations per Faculty'] > upper_bound)
    ]

    print("\nCitations per Faculty Outliers:")
    print(outliers[['Institution Name', 'Citations per Faculty']])


def qs_overall_score_outliers(df):
    df = clean_numeric_columns(df)

    qt1 = df['QS Overall Score'].quantile(0.25)
    qt3 = df['QS Overall Score'].quantile(0.75)
    iqr = qt3 - qt1

    print(f"\nQS Overall Score IQR (Interquartile Range): {iqr}")

    lower_bound = qt1 - 1.5 * iqr
    upper_bound = qt3 + 1.5 * iqr

    outliers = df[
        (df['QS Overall Score'] < lower_bound) |
        (df['QS Overall Score'] > upper_bound)
    ]

    print("\nQS Overall Score Outliers:")
    print(outliers[['Institution Name', 'QS Overall Score']])
