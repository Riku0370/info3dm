# フォント設定
import numpy as np
import pandas as pd

#　真の関数
def true_function(x):
    y = np.sin(np.pi * x * 0.8) * 10
    return y

#　データセット
def create_dataset(n = 20, seed = 0):
    np.random.seed(seed)
    x = np.random.uniform(-1, 1, n)
    y = true_function(x)

    df = pd.DataFrame({
        "観測点": x,
        "真値": y
    })
    return df