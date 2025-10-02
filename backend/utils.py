import boto3
from botocore.exceptions import ClientError
from config import Config

def generate_presigned_put(s3_key: str):
    """Generate a presigned URL to upload a file to S3"""
    try:
        s3 = boto3.client(
            "s3",
            region_name=Config.AWS_REGION,
            aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
        )
        url = s3.generate_presigned_url(
            "put_object",
            Params={"Bucket": Config.S3_BUCKET, "Key": s3_key},
            ExpiresIn=Config.PRESIGNED_EXPIRY
        )
        return url
    except ClientError as e:
        print(e)
        return None

def generate_presigned_get(s3_key: str):
    """Generate a presigned URL to download a file from S3"""
    try:
        s3 = boto3.client(
            "s3",
            region_name=Config.AWS_REGION,
            aws_access_key_id=Config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY,
        )
        url = s3.generate_presigned_url(
            "get_object",
            Params={"Bucket": Config.S3_BUCKET, "Key": s3_key},
            ExpiresIn=Config.PRESIGNED_EXPIRY
        )
        return url
    except ClientError as e:
        print(e)
        return None
