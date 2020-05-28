import pandas as pd
import os.path as path

def  loadData(filename,  cat):
    df = pd.read_csv(filename)
    data = list(df[cat].dropna())

    return data

if __name__=="__main__":
    filename = "conf/biology.csv"
    data=loadData(filename, "mammals")
    print(data)