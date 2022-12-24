import os
import glob
from utils import upload_file_to_gcs
from decouple import config

HOME_PATH = config("HOME_PATH")
BUCKET = config("GCP_GCS_BUCKET")
path_source = f"{HOME_PATH}/wasterwater-overflows/data/*"

def upload_to_gcs():
	for file_path in glob.glob(path_source):
		file_name = os.path.basename(file_path)
		print(f"Uploading file: {file_name} to cloud storage")
		upload_file_to_gcs(BUCKET, file_name, file_path)
		print("File uploaded")

def upload_to_bq():
	pass

if __name__ == '__main__':
	upload_to_gcs()
	upload_to_bq()