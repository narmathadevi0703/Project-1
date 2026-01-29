from dataset_import import data_load
from DataClean import explore_university_dataset, summarize_university_statistics, check_missing_university_values, clean_duplicate_and_missing_universities
from expoert_data_clean import export_cleaned_university_data
from MinMaxScaler_Normalizer import Standard_Scaler, Min_Max_Values, normalizer_values
from Quant import academic_reputation_outliers,  citations_per_faculty_outliers, qs_overall_score_outliers
from Statitics import stats
from Basic_vasualise import Line_plot, Bar_plot, hist_plot
from advanced_visual import Pair_plot, Heat_plot, Heat_cov
from dashboard import Dash_board
from Probability_Analysis import range_stats, hist_rang
from knn import knn_modeling
from k_means import KMeans_clustering

datas = data_load()
explore_university_dataset(datas)
summarize_university_statistics(datas)
check_missing_university_values(datas)
clean_duplicate_and_missing_universities(datas)
export_cleaned_university_data(datas)
Standard_Scaler(datas)
Min_Max_Values(datas)
normalizer_values(datas)
academic_reputation_outliers(datas)
citations_per_faculty_outliers(datas)
qs_overall_score_outliers(datas)
stats(datas)
Line_plot(datas)
Bar_plot(datas)
hist_plot(datas)
Pair_plot(datas)
Heat_plot(datas)
Heat_cov(datas)
Dash_board(datas)
range_stats(datas)
hist_rang(datas)
knn_modeling(datas)
KMeans_clustering(datas)