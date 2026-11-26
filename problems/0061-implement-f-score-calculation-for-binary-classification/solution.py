import numpy as np

def f_score(y_true, y_pred, beta):
    """
    Calculate F-Score for a binary classification task.

    :param y_true: Numpy array of true labels
    :param y_pred: Numpy array of predicted labels
    :param beta: Weight of recall relative to precision (beta > 1 favours recall)
    :return: F-Score rounded to three decimal places
    """
    true_positive = 0
    false_positive = 0
    false_negative = 0
    for i,j in zip(y_true,y_pred):
        if i==j==1:
            true_positive+=1
        elif i==0 and j==1:
            false_positive+=1
        elif i==1 and j==0:
            false_negative+=1
        else:
            continue

    if true_positive+false_positive==0 or true_positive+false_negative==0:
        return 0.0
    else:
        P = true_positive/(true_positive+false_positive)
        R = true_positive/(true_positive+false_negative)
        if (beta**2*P+R)==0:
            return 0.0
        else:
            f1_score = np.round(((1+beta**2)*P*R)/(beta**2*P+R),3)
    return f1_score