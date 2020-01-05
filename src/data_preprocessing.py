import sys
import pandas as pd
from pathlib import Path
from utils import create_sample, _convert_to_ffm

MAX_NULL = 50000
MAX_PRICE_USD = 5000

encoder = {"currentcode": 0,
           "catdict": {},
           "catcodes": {}
           }

from config import (
                train_csv_path,
                test_csv_path,
                sample_train_csv_path,
                sample_test_csv_path,
                processed_train_csv_path,
                processed_test_csv_path,
                train_ffm_path,
                test_ffm_path
)

def change_data_type(df):
    target = 'click_bool'
    numerics = ['prop_review_score', 'prop_location_score1', 'prop_log_historical_price', 'price_usd']
    categories = []

    for cols in df.columns:
        if not cols in numerics:
            categories.append(cols)
    categories.remove('click_bool')

    for col in categories:
        df[col] = df[col].astype('category')

    for col in numerics:
        df[col] = df[col].astype('float16')

    df[target] = df[target].astype('int8')

    return target, numerics, categories, df

def cleaning_csv_data(sampled_csv_path, processed_csv_path):
    '''

    :param sampled_csv_path, processed_csv_path:
    :return: target, numerics, categories, df
    '''

    if not Path(processed_csv_path).exists():
        df = pd.read_csv(sampled_csv_path)
        df = df.drop(['Unnamed: 0', 'date_time'], axis=1)
        if sampled_csv_path == sample_test_csv_path:
            df['click_bool'] = 0
        else:
            df = df.drop(['position', 'booking_bool'], axis=1)
        null_counts = df.isnull().sum()
        null_counts_df = null_counts[null_counts < MAX_NULL]

        refined_cols = []
        for col in null_counts_df.keys():
            refined_cols.append(col)
        df = df.filter(refined_cols, axis=1)

        pd.to_numeric(df['prop_review_score'], errors='coerce')
        df['prop_review_score'].fillna((df['prop_review_score'].median()), inplace=True)
        df = df[df.price_usd < MAX_PRICE_USD]
        target, numerics, categories, new_df = change_data_type(df)
        new_df.to_csv(processed_csv_path)
        return target, numerics, categories, new_df

    else:
        df = pd.read_csv(processed_csv_path)
        df = df.drop('Unnamed: 0', axis=1)
        target, numerics, categories, new_df = change_data_type(df)
        return target, numerics, categories, new_df

if __name__ == '__main__':
    if not Path(train_csv_path).exists() or not Path(test_csv_path).exists() :
        print('train.csv or test.csv does not exist in datasets/data')
        sys.exit()

    print('Creating train_sample if does not exist')
    create_sample(train_csv_path, sample_train_csv_path)
    print('Creating test_sample if does not exist')
    create_sample(test_csv_path, sample_test_csv_path)

    print("Creating processed_train.csv if does not exist")
    target_train, numerics_train, categories_train, df_train = cleaning_csv_data(sample_train_csv_path, processed_train_csv_path)
    print('Creating train_ffm.txt if does not exist')
    encoded_train = _convert_to_ffm(
        path=train_ffm_path,
        df= df_train,
        target=target_train,
        numerics=numerics_train,
        categories=categories_train,
        encoder=encoder
    )

    print("Creating processed_test.csv if does not exist")
    target_test, numerics_test, categories_test, df_test = cleaning_csv_data(sample_test_csv_path, processed_test_csv_path)
    print('Creating test_ffm.txt if does not exist')
    encoded_test = _convert_to_ffm(
        path=test_ffm_path,
        df= df_test,
        target=target_test,
        numerics=numerics_test,
        categories=categories_test,
        encoder=encoder
    )