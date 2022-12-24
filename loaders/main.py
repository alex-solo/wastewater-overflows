import os
import glob
from utils import upload_to_gcs
from decouple import config

HOME_PATH = config("HOME_PATH")
BUCKET = config("GCP_GCS_BUCKET")
path_source = f"{HOME_PATH}/wasterwater-overflows/data/*"

def main():
	for file_path in glob.glob(path_source):
		file_name = os.path.basename(file_path)
		print(f"Uploading file: {file_name} to cloud storage")
		upload_to_gcs(BUCKET, file_name, file_path)
		print("File uploaded")
if __name__ == '__main__':
    main()