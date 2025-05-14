from google.cloud import bigquery

def load_df_to_gbq(df, dataset, table_id, project_id, if_exists='append'):
    """
    Load a DataFrame to Google BigQuery using the official BigQuery client.
    
    Parameters:
    df (pd.DataFrame): The DataFrame to load.
    table_id (str): The name of the table to load the data into (without dataset).
    dataset (str): The BigQuery dataset name.
    project_id (str): The Google Cloud project ID.
    if_exists (str): 'replace', 'append', or 'fail'.
    """

    client = bigquery.Client(project=project_id)

    full_table_id = f"{project_id}.{dataset}.{table_id}"

    if if_exists == 'replace':
        # Delete existing table
        try:
            client.delete_table(full_table_id)
            print(f"Deleted table {full_table_id}.")
        except Exception as e:
            print(f"Table {full_table_id} does not exist or couldn't be deleted: {e}")

    job_config = bigquery.LoadJobConfig(
        write_disposition=(
            bigquery.WriteDisposition.WRITE_TRUNCATE
            if if_exists == 'replace'
            else bigquery.WriteDisposition.WRITE_APPEND
        ),
        autodetect=True,
    )

    job = client.load_table_from_dataframe(df, full_table_id, job_config=job_config)
    job.result()  # Wait for the job to complete

    print(f"Loaded {df.shape[0]} rows to {full_table_id}")