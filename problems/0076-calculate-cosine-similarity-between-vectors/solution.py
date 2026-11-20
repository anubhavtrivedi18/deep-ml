import numpy as np

def cosine_similarity(v1, v2):
    """
    Calculate the cosine_similarity of two vectors.
    Args:
        vec1 (numpy.ndarray): 1D array representing the first vector.
        vec2 (numpy.ndarray): 1D array representing the second vector.
    Returns:
        The cosine_similarity of the two vectors.
    """
    # Implement your code here
    vec1 = np.array(v1)
    vec2 = np.array(v2)
    if len(vec1)!=len(vec2):
        return [-1]
    vec1_vec2_dot = np.dot(vec1,vec2)
    vec1_l2_norm = np.sqrt(np.sum(vec1**2))
    vec2_l2_norm = np.sqrt(np.sum(vec2**2))
    product_norm = np.multiply(vec1_l2_norm,vec2_l2_norm)
    result = np.divide(vec1_vec2_dot,product_norm)
    return result