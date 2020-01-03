import pandas as pd
from utils import create_sample
from pathlib import Path
import sys

MAX_NULL = 50000

from config.config import (
                train_csv_path,
                test_csv_path,
                sample_train_csv_path,
                sample_test_csv_path,
                processed_train_csv_path,
                processed_test_csv_path
)

def cleaning_csv_data(sampled_csv):
    '''

    :param sampled_csv:
    :return: processes the sampled csv file
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


if __name__ == '__main__':
    if not Path(train_csv_path).exists() or not Path(test_csv_path).exists() :
        print('train.csv or test.csv does not exist')
        sys.exit()

    print('Creating train_sample if does not exist')
    create_sample(train_csv_path, sample_train_csv_path)
    print('Creating train_sample if does not exist')
    create_sample(test_csv_path, sample_test_csv_path)

    print("Cleaning sample train csv")
    cleaning_csv_data(sample_train_csv_path)

    print("Cleaning sample test csv")
    cleaning_csv_data(sample_test_csv_path)


