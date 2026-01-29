def export_cleaned_university_data(exp):
    cleaned_data = exp.dropna()
    cleaned_data.to_csv('university_data_cleaned.csv', index=False)
   
