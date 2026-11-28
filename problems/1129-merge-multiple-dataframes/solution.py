import pandas as pd

def solution(df1, df2, df3):
    df1_df2_inner = pd.merge(df1,df2,on='emp_id',how='inner')
    result = pd.merge(df1_df2_inner,df3,on='emp_id',how='left')
    df = result
    return df.reset_index(drop=True)