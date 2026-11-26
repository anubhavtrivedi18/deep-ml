import numpy as np
def precision(y_true, y_pred):
    # Your code here
    true_positive = 0
    false_positive = 0
    for i,j in zip(y_true,y_pred):
        if i==j==1:
            true_positive+=1
        elif i==0 and j==1:
            false_positive+=1
        else:
            continue
    if true_positive+false_positive==0:
        return 0.0
    else:
        precision = true_positive/(true_positive+false_positive)
        return precision
