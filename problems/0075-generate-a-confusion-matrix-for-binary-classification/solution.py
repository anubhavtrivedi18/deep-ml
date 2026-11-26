
from collections import Counter

def confusion_matrix(data):
    # Implement the function here
    pass
    true_positive = 0
    false_negative = 0
    false_positive = 0
    true_negative = 0 
    for row in data:
        if row[0] ==0 and row[1]==0:
            true_negative+=1
        elif row[0] ==0 and row[1]==1:
            false_positive+=1
        elif row[0]==1 and row[1]==1:
            true_positive+=1
        else:
            false_negative+=1
    return [[true_positive,false_negative],[false_positive,true_negative]]