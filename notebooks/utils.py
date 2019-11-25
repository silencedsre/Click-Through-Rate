import pandas as pd
import random

def create_sample(filename = '../datasets/data/train.csv', sample_filename = '../datasets/data/train_sample.csv'):
    num_lines = sum(1 for l in open(filename))
    sample = int(num_lines/10)
    skip = sorted(random.sample(range(1,num_lines+1), num_lines-sample))
    print("reading csv and creating sample df")
    df = pd.read_csv(
         filename,
         header=0,
         skiprows= skip,
    )
    print("Saving sample df to csv")
    try:
        df.to_csv(sample_filename)
    except Exception as e:
        print("Error occured while creating sample csv file. Error: {}".format(e))
    return "Success"
