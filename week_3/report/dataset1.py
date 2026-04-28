import numpy as np
import pandas as pd

def true_function(x):
    return np.sin(np.pi * x * 0.8) * 10

def create_dataset(n=20, seed=0):
    np.random.seed(seed)
    x = np.random.uniform(-1, 1, n)
    y = true_function(x)

    df = pd.DataFrame({
        "観測点": x,
        "真値": y
    })
    return df

def add_noise(df, variance=2.0):
    sigma = np.sqrt(variance)
    noise = np.random.normal(0, sigma, len(df))
    noise = noise / 2

    df["観測値"] = df["真値"] + noise
    return df

def save_dataset(df, filename="dataset.tsv"):
    df.to_csv(filename, sep="\t", index=False)

def load_dataset(filename="dataset.tsv"):
    df = pd.read_csv(filename, sep="\t")
    return df