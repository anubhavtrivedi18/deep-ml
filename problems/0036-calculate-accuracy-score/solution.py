import numpy as np

def accuracy_score(y_true, y_pred):
    # Your code here
    true_prediction = 0
    for i,j in zip(y_true,y_pred):
        if i==j:
            true_prediction+=1
    accuracy = true_prediction/len(y_true)
    return accuracy