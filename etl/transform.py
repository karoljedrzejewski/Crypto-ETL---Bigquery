import sys
import json
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import pandas as pd

def transform_data(f, save=False):
    records = []
    for data in f:
        # data = json.loads(data)['item']
        data_i = data['item']
        name = data_i['name']
        nameid = data_i['id']
        price = data_i['data']['price']
        price_change_percentage = data_i['data']['price_change_percentage_24h']['eur']

        records.append({
            'name': name,
            'nameid': nameid,
            'price': price,
            'price_change_percentage': price_change_percentage
        })
    df = pd.DataFrame(records)
    if save:
        save_transformed_data(df)
    
    return df

def save_transformed_data(df):
    df.to_csv('trending_data.csv', index=False)


if __name__ == "__main__":
    transform_data()
    print('Data transformed and saved to trending_data.csv')