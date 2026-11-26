import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """
    true_positive = 0
    false_positive = 0
    for i,j in zip(y_true,y_pred):
        if i==j==1:
            true_positive+=1
        elif i==1 and j==0:
            false_positive+=1
        else:
            continue
    if true_positive+false_positive==0:
        return 0.0
    else:
        return true_positive/(false_positive+true_positive)