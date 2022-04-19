# Imports the Google Cloud client library
from google.cloud import storage
import os 
os.environ['GOOGLE_APPLICATION_CREDENTIALS']=r'proyectosoa-347218-89838b4c6af7.json'

# Instantiates a client
client = storage.Client()
# Retrieve an existing bucket
# https://console.cloud.google.com/storage/browser/[bucket-id]/
bucket = client.get_bucket('proyectosoa2022')
# Then do other things...
blob = bucket.get_blob('T.txt')
print(blob.download_as_bytes())