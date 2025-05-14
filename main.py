from etl import extract, transform, load
import os
import dotenv
dotenv.load_dotenv()


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "gcp_key.json"
GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
API_KEY_GH = os.getenv("API_KEY_GH")


if __name__ == "__main__":
    try:
        trending_data = extract.extract_data('https://api.coingecko.com/api/v3/search/trending', API_KEY_GH)    
        df = transform.transform_data(trending_data['coins'])
        load.load_df_to_gbq(df, dataset='cryptos', table_id='exchange', project_id=GCP_PROJECT_ID)
    except Exception as e:
        print("GCP_PROJECT_ID is set:", bool(GCP_PROJECT_ID))
        print('API_KEY_GH is set:', bool(API_KEY_GH))
        print(f"An error occurred: {e}")
        print('Response content:', trending_data)
