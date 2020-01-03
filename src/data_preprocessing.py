import sys
import pandas as pd
from pathlib import Path
from utils import create_sample, _convert_to_ffm

MAX_NULL = 50000

encoder = {"currentcode": 0,
           "catdict": {},
           "catcodes": {}
           }

from config.config import (
                train_csv_path,
                test_csv_path,
                sample_train_csv_path,
                sample_test_csv_path,
                processed_train_csv_path,
                processed_test_csv_path,
                train_ffm_path,
                test_ffm_path
)

def cleaning_csv_data(sampled_csv):
    '''

    :param sampled_csv:
    :return: target, numerics, categories, df
    '''

    if not Path(processed_test_csv_path).exists():
        df = pd.read_csv(sampled_csv)
        if sampled_csv == '../datasets/data/sample_test.csv':
            df['click_bool'] = 0
            temp = 'test'
            processed_csv_path = processed_test_csv_path
        else:
            df = df.drop('booking_bool', axis=1)
            temp = 'train'
            processed_csv_path = processed_train_csv_path

        null_counts = df.isnull().sum()
        refined_cols = null_counts[null_counts < MAX_NULL]
        cols = []
        for key in refined_cols.keys():
            cols.append(key)
        df = df.filter(cols, axis=1)
        df = df.drop(['Unnamed: 0', 'date_time'], axis=1)
        pd.to_numeric(df['prop_review_score'], errors='coerce')
        df['prop_review_score'].fillna((df['prop_review_score'].median()), inplace=True)
        df = df[df.price_usd < 5000]

        target = 'click_bool'
        numerics = ['prop_review_score', 'prop_location_score1', 'prop_log_historical_price', 'price_usd']
        categories = []

        for cols in df.columns:
            if cols in numerics:
                continue
            categories.append(cols)
        categories.remove('click_bool')

        for col in categories:
            df[col] = df[col].astype('category')

        for col in numerics:
            df[col] = df[col].astype('float16')

        df[target] = df[target].astype('int8')

        df.to_csv(processed_csv_path)

        print(f"processed_{temp}.csv generated in datasets/data")

        return target, numerics, categories, df

def return_dataframe(cleaned_csv_file):
    df = pd.read_csv(cleaned_csv_file)
    return df

if __name__ == '__main__':
    if not Path(train_csv_path).exists() or not Path(test_csv_path).exists() :
        print('train.csv or test.csv does not exist in datasets/data')
        sys.exit()

    print('Creating train_sample if does not exist')
    create_sample(train_csv_path, sample_train_csv_path)
    print('Creating train_sample if does not exist')
    create_sample(test_csv_path, sample_test_csv_path)

    print("Cleaning sample train csv")
    target_train, numerics_train, categories_train, df_train = cleaning_csv_data(sample_train_csv_path)
    encoded_train = _convert_to_ffm(
        path=train_ffm_path,
        df= df_train,
        type='train',
        target=target_train,
        numerics=numerics_train,
        categories=categories_train,
        encoder=encoder
    )

    print("Cleaning sample test csv")
    target_test, numerics_test, categories_test, df_test = cleaning_csv_data(test_csv_path)
    encoded_test = _convert_to_ffm(
        path=test_ffm_path,
        df= df_test,
        type='test',
        target=target_test,
        numerics=numerics_test,
        categories=categories_test,
        encoder=encoder
    )




