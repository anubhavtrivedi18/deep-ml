import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):

    mean = np.mean(data,axis = 0)
    std = np.std(data,axis = 0)
    min_value = np.min(data,axis = 0)
    max_value = np.max(data,axis = 0)
    standardized_data = (data-mean)/std
    normalized_data = (data-min_value)/(max_value-min_value)
    standardized_data = np.round(standardized_data,4).tolist()
    normalized_data = np.round(normalized_data,4).tolist()
    return standardized_data,normalized_data