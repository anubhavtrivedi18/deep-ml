import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    if norm_type == "l1":
        l1_norm = np.sum(np.abs(arr))
        return l1_norm
    elif norm_type == "l2":
        l2_norm = np.sqrt(np.sum(arr**2))
        return l2_norm
    elif norm_type =="linf":
        linf_norm = np.max(np.abs(arr))
        return linf_norm
    elif norm_type =="frobenius":
        if arr.ndim==2:
            frobenius_norm = np.sqrt(np.sum(arr**2))
            return frobenius_norm
    else:
        import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    """
    Compute the specified norm of the input array.

    'l1', 'l2' and 'linf' are entrywise norms and accept a 1D or 2D array.
    'frobenius' is a matrix norm and must raise a ValueError if arr is not 2D.

    Args:
        arr: Input numpy array (1D or 2D)
        norm_type: Type of norm ('l1', 'l2', 'linf', or 'frobenius')

    Returns:
        The computed norm as a float
    """
    # Your code here
    if norm_type == "l1":
        l1_norm = np.sum(np.abs(arr))
        return l1_norm
    elif norm_type == "l2":
        l2_norm = np.sqrt(np.sum(arr**2))
        return l2_norm
    elif norm_type =="linf":
        linf_norm = np.max(np.abs(arr))
        return linf_norm
    elif norm_type =="frobenius":
        if arr.ndim!=2:
            raise ValueError("ValueError")
        else:
            frobenius_norm = np.sqrt(np.sum(arr**2))
            return frobenius_norm
        
    else:
        raise ValueError("Invalid norm type")