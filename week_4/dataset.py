import numpy as np

def load_linear_example():
    # Generate synthetic data for linear regression
    np.random.seed(0)
    X = np.array([[1,4], [1,8],[1,13],[1,17]])
    y = np.array([7,10,11,14])
    return X, y

