def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    # Your code here
    max_value = max(x)
    min_value = min(x)
    scaled_values = [ ]
    for i in x:
        if min_value-max_value!=0:
            value = (i-min_value)/(max_value-min_value)
            scaled_values.append(value)
        else:
            max_value-min_value == 0
            value = (i-min_value)/(max_value-min_value)
            scaled_values.append(value)
    return scaled_values