
def explore_university_dataset(des):
    find_heads = des.head()
    print(f"\nFirst Five University Records:\n{find_heads}") 
    
    informations = des.info()
    print(f"\nUniversity Dataset Information:\n{informations}")



def summarize_university_statistics(des):
    details = des.describe()
    print(f"\nStatistical Summary of University Ranking Dataset:\n{details}")



def check_missing_university_values(des):
    miss1 = des.isnull().sum()
    print(f"\nMissing Values in University Ranking Dataset:\n{miss1}")



def clean_duplicate_and_missing_universities(des):
    drops_values = des.dropna().drop_duplicates().isnull().sum()
    print(f"\nMissing Values After Cleaning University Ranking Dataset:\n{drops_values}")
