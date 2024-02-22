import pandas as pd
from pathlib import Path

def load_table():

    #load files
    df_ingredient=pd.read_csv('./ingredient_dummy_short2.csv')
    df_keyword=pd.read_csv('./keyword_dummy_short2.csv')
    # return df_ingredient.to_dict(), df_keyword.to_dict()
    return 1
