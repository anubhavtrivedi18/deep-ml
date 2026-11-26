import numpy as np

def precision_recall_at_threshold(y_true, y_scores, threshold):
    """
    Compute precision and recall at a given decision threshold.

    Args:
        y_true: list/array of true binary labels (0 or 1)
        y_scores: list/array of predicted scores in [0, 1]
        threshold: float, classification threshold (predict positive if score >= threshold)

    Returns:
        [precision, recall] as a list of two floats rounded to 4 decimals.
    """
    # Your code here
    y_true = np.array(y_true)
    y_scores = (np.array(y_scores)>threshold).astype(int)
    true_positive = 0
    false_positive = 0
    false_negative = 0 
    for i,j in zip(y_true,y_scores):
        if i==j==1:
            true_positive+=1
        elif i==0 and j==1:
            false_positive+=1
        elif i==1 and j==0:
            false_negative+=1
        else:
            continue
    if (true_positive+false_negative)==0 or (true_positive+false_positive)==0:
        return [0.0,0.0]
    else:
        P = true_positive/(true_positive+false_positive)
        R = true_positive/(true_positive+false_negative)
        return [P,R]