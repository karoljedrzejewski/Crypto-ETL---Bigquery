import pandas as pd
from pandas_gbq import to_gbq

def load_df_to_gbq(df, dataset, table_id, project_id, if_exists='replace'):
    """
    Load a DataFrame to Google BigQuery.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to load.
    table_id (str): The ID of the table to load the data into.
    project_id (str): The ID of the Google Cloud project.
    if_exists (str): What to do if the table already exists. Options are 'fail', 'replace', 'append'.
    """

    table_id = f'{dataset}.{table_id}'

    to_gbq(df, destination_table=table_id, project_id=project_id, if_exists=if_exists)