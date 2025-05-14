from etl import extract, transform, load
import os
import dotenv
dotenv.load_dotenv()


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "gcp_key.json"
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
API_KEY = os.getenv("API_KEY")


if __name__ == "__main__":
    trending_data = extract.extract_data('https://api.coingecko.com/api/v3/search/trending', API_KEY)    
    df = transform.transform_data(trending_data['coins'])
    load.load_df_to_gbq(df, dataset='cryptos', table_id='exchange', project_id=GCP_PROJECT_ID)