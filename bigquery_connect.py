from google.cloud import bigquery

client = bigquery.Client.from_service_account_json("/home/sumit_modi_sunrise_net/gcp_keys/gcp-ch-d-prj-i-edp-56f1418e2387.json")

print("✓ Successfully connected to BigQuery!")
print(f"Project ID: {client.project}")
