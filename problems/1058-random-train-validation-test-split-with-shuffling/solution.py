import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    # Your code here
    n = len(data)
    rng = np.random.default_rng(seed)
    index = rng.permutation(n)
    train_index = int(n*train_frac)
    validation_index = train_index+int(n*validation_frac)
    test_index = validation_index
    train_array = data[index[:train_index]]
    validation_array = data[index[train_index:validation_index]]
    test_array = data[index[validation_index:]]
    return train_array,validation_array,test_array