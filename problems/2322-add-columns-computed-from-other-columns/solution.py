import pandas as pd
import numpy as np


def add_order_columns(df, country_names):
    """Return a copy of df with the columns total, size and country added."""
    df = df.copy()
    df['total'] = df['quantity']*df['unit_price']
    df['size'] = np.where(df['total']>=100,'large','small')
    df['country'] = df['country_code'].map(country_names).fillna('Other')

    return df.reset_index(drop=True)
