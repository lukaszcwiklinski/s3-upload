from storages.backends.s3boto3 import S3Boto3Storage

class FilesStorage(S3Boto3Storage):
    location = 'static'
    file_overwrite = False