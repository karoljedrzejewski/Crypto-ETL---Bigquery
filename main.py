from etl import extract, transform, load
import env
import json
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "gcp_key.json"

if __name__ == "__main__":
    trending_data = extract.extract_data('https://api.coingecko.com/api/v3/search/trending', env.API_KEY)
    print(trending_data)
    with open('trending_data.json', 'w') as f:
        for coin in trending_data['coins']:
            f.write(json.dumps(coin) + '\n')
    
    df = transform.transform_data(save=True)
    load.load_df_to_gbq(df, dataset='cryptos', table_id='exchange', project_id=env.GCP_PROJECT_ID)