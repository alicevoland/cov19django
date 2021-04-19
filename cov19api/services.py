import pandas as pd

def fetch_departments_and_regions():
    df = pd.read_csv('https://www.data.gouv.fr/fr/datasets/r/70cef74f-70b1-495a-8500-c089229c0254')
    print(df)
