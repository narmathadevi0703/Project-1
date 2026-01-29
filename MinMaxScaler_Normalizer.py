from sklearn.preprocessing import StandardScaler, MinMaxScaler, Normalizer
from sklearn.impute import SimpleImputer

def Standard_Scaler(df):
    numerics = df.select_dtypes(include='number')

    if numerics.empty:
        print("No numerical university ranking indicators found for scaling!")
        return df

 
    imputer = SimpleImputer(strategy='mean')
    numerics_imputed = imputer.fit_transform(numerics)

    scaler = StandardScaler()
    df[numerics.columns] = scaler.fit_transform(numerics_imputed)

    print("\nStandard Scaling applied successfully after handling missing values")
    print(df[numerics.columns].head())
    return df

def Min_Max_Values(df):
    numerics = df.select_dtypes(include='number')

    if numerics.empty:
        print("No numerical university ranking indicators found for scaling!")
        return df

 
    imputer = SimpleImputer(strategy='mean')
    numerics_imputed = imputer.fit_transform(numerics)

    scaler = MinMaxScaler()
    df[numerics.columns] = scaler.fit_transform(numerics_imputed)

    print("\nMin-Max Scaling applied successfully after handling missing values")
    print(df[numerics.columns].head())
    return df

def normalizer_values(df):
    numerics = df.select_dtypes(include='number')

    if numerics.empty:
        print("No numerical university ranking indicators found for normalization!")
        return df

 
    imputer = SimpleImputer(strategy='mean')
    numerics_imputed = imputer.fit_transform(numerics)

    scaler = Normalizer()
    df[numerics.columns] = scaler.fit_transform(numerics_imputed)

    print("\nNormalization applied successfully after handling missing values")
    print(df[numerics.columns].head())
    return df
