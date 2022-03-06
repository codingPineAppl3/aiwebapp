import pandas as pd
import numpy as np
import matplotlib as plt

from tabulate import tabulate
from IPython.display import display

print("hello world")

# read training data
def read_train_data():
    #print("read training data")
    train_path = "ttmdb_app/static/ttmdb_app/data/train.csv"

    df_train = pd.read_csv(train_path)
    return df_train

def show_train_columns():
    print("show train columns")
    #return display_df_pretty(read_train_data().columns)
    return read_train_data().columns

def show_train_head():
    print("show train first 5 row")
    return read_train_data().head(5)
    

# read test data
def read_test_data():
    #print("read test data")
    test_path = "ttmdb_app/static/ttmdb_app/data/test.csv"

    df_test = pd.read_csv(test_path)
    df_test.head(5)
    return df_test
"""
def display_df_pretty(df):
    pd.set_option('display.max_rows', 5)
    pd.set_option('display.max_columns', 10)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')
    pd.set_option('display.precision', 3)
    return display(df)
"""

def main():
    print(show_train_columns())
    print(show_train_head())
    #print(read_test_data())

if __name__ == "__main__":
    main()

