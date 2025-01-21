pip install pandas

def loadCSV():
    import pandas as pd
    from prophet import Prophet
    import matplotlib.pyplot as plt

    # Load your training data
    train = pd.read_csv('/kaggle/input/playground-series-s5e1/train.csv')

    # Check the first few rows
    print(train.head())

    return train
