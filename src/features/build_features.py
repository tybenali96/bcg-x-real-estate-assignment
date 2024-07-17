import pandas as pd 

def get_report_profile_of_data(df: pd.DataFrame, filepath: str):
    profile = ProfileReport(df, title="Profiling Report of Real Estate Data")
    profile.to_file(filepath)


def get_columns_with_missing_values(data: pd.DataFrame) -> pd.DataFrame:
    columns_with_missing_values = [col for col in data.columns if data[col].isnull().sum() != 0]
    number_of_missing_values = [data[col].isnull().sum() for col in data.columns if data[col].isnull().sum() != 0]

    columns_with_missing_values_dict = {}
    columns_with_missing_values_dict['column_name'] = columns_with_missing_values
    columns_with_missing_values_dict['number_of_missing_values'] = number_of_missing_values

    columns_with_missing_values_df = pd.DataFrame.from_dict(columns_with_missing_values_dict)
    columns_with_missing_values_df['percentage_of_missing_values'] = columns_with_missing_values_df['number_of_missing_values'].apply(lambda x: x / data.shape[0])
    return columns_with_missing_values_df


def cap_outliers_with_iqr_method(df: pd.DataFrame, column: str) -> pd.DataFrame:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    df[column] = df[column].apply(lambda x: lower_bound if x < lower_bound else upper_bound if x > upper_bound else x)
    return df