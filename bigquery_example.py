"""
Example script to connect to Google BigQuery and fetch data
"""
import os
from dotenv import load_dotenv
from google.cloud import bigquery
import pandas as pd

# Load environment variables from .env file
load_dotenv()

def connect_to_bigquery():
    """Connect to BigQuery using service account credentials"""
    # Get the service account JSON path from environment variable
    credentials_path = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
    
    if not credentials_path:
        raise ValueError("GOOGLE_APPLICATION_CREDENTIALS not set in .env file")
    
    print(f"Connecting to BigQuery using: {credentials_path}")
    
    # Create BigQuery client
    client = bigquery.Client.from_service_account_json(credentials_path)
    
    print("✓ Successfully connected to BigQuery!")
    return client

def fetch_data(client, query):
    """Execute a query and return results as a DataFrame"""
    print(f"\nExecuting query...")
    job_config = bigquery.QueryJobConfig()
    
    # Execute query
    query_job = client.query(query, job_config=job_config)
    
    # Convert results to pandas DataFrame
    df = query_job.result().to_dataframe()
    
    return df

def main():
    try:
        # Connect to BigQuery
        client = connect_to_bigquery()
        
        # Example query - modify this to your actual table
        # This is a simple test query
        query = """
        SELECT 
            'Hello' as greeting,
            'BigQuery' as source,
            CURRENT_TIMESTAMP() as timestamp
        """
        
        # Fetch data
        df = fetch_data(client, query)
        
        # Display results
        print("\n✓ Data fetched successfully!")
        print("\nDataFrame:")
        print(df)
        print(f"\nShape: {df.shape}")
        
        return df
    
    except Exception as e:
        print(f"✗ Error: {e}")
        raise

if __name__ == "__main__":
    df = main()
