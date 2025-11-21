import os
import shutil
import boto3
from fastapi import UploadFile
from app.core.config import settings

class S3Connector:
    def __init__(self, bucket_name: str = settings.S3_BUCKET_NAME):
        self.bucket_name = bucket_name
        self.use_real_s3 = settings.USE_REAL_S3
        
        if self.use_real_s3:
            self.s3_client = boto3.client(
                "s3",
                aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
                region_name=settings.AWS_REGION
            )
        else:
            self.local_storage_path = os.path.join(os.getcwd(), "local_s3_storage", bucket_name)
            os.makedirs(self.local_storage_path, exist_ok=True)

    async def upload_file(self, file: UploadFile, object_name: str = None) -> str:
        """
        Upload a file to S3 (Real or Mock).
        Returns the file path or S3 URI.
        """
        if object_name is None:
            object_name = file.filename

        if self.use_real_s3:
            try:
                # Reset file pointer to beginning
                file.file.seek(0)
                self.s3_client.upload_fileobj(file.file, self.bucket_name, object_name)
                return f"s3://{self.bucket_name}/{object_name}"
            except Exception as e:
                print(f"Error uploading to S3: {e}")
                raise e
        else:
            file_path = os.path.join(self.local_storage_path, object_name)
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            return file_path

    def list_files(self):
        if self.use_real_s3:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            return [obj['Key'] for obj in response.get('Contents', [])]
        else:
            return os.listdir(self.local_storage_path)
