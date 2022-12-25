from google.cloud import storage
from sqlalchemy import create_engine
from decouple import config

def upload_file_to_gcs(bucket, object_name, local_file):
	"""
	Ref: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-python
	"""
	# # WORKAROUND to prevent timeout for files > 6 MB on 800 kbps upload speed.
	# # (Ref: https://github.com/googleapis/python-storage/issues/74)
	# storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # 5 MB
	# storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  # 5 MB

	client = storage.Client()
	bucket = client.bucket(bucket)
	blob = bucket.blob(object_name)
	blob.upload_from_filename(local_file)

def docker_pg_engine():
	user = config("USER_DEV")
	password = config("PASSWORD_DEV")
	host = config("HOST_DEV")
	port = config("PORT_DEV")
	db = config("DB_DEV")

	connection_string = f"postgresql://{user}:{password}@{host}:{port}/{db}"
	engine = create_engine(connection_string)
	engine.connect()

	return engine
