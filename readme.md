# 🔁 Crypto Trending ETL to BigQuery

This project demonstrates a minimal but professional Extract-Transform-Load (ETL) pipeline that reads trending cryptocurrency data from a JSON file, transforms it into a clean tabular format using Python (Pandas), and loads it into a Google BigQuery table for further analysis or visualization.

---

## 🚀 Project Overview

**Goal**: Build a working end-to-end ETL pipeline using Python and BigQuery.

- **Extract**: Read data from a local `trending_data.json` file (simulating an API response).
- **Transform**: Parse and clean selected fields using `pandas`.
- **Load**: Upload the processed data to Google BigQuery via the `pandas-gbq` package.

---

## 🔧 Setup Instructions

### 1. Clone the repository

### 2. Create a virtual environment

python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Set up Google Cloud credentials

Create a service account with roles:

    BigQuery Data Editor
    BigQuery Job User

Download the JSON key and rename it to gcp_key.json

Set the environment variable:

export GOOGLE_APPLICATION_CREDENTIALS="gcp_key.json"

### 5. Run the pipeline

python main.py


The pipeline will:

Parse the input JSON
Convert it into a Pandas DataFrame
Load it into the BigQuery table:

## Technologies Used

Python 3.10

Pandas

Google BigQuery

pandas-gbq and google-cloud-bigquery for BigQuery integration

## Next patch

Fully autonomous system using Apache Airflow or Github Actions