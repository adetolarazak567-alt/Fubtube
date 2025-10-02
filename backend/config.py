import os

class Config:
    # --- Security ---
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")  

    # --- Database (Render gives DATABASE_URL automatically for PostgreSQL) ---
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///funtube.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- File Storage (AWS S3 or others) ---
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    S3_BUCKET = os.getenv("S3_BUCKET", "")
    AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID", "")
    AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "")

    # --- Upload Control ---
    ADMIN_TOKEN = os.getenv("ADMIN_TOKEN", "change-this")  # secure upload key

    # --- Presigned URL Expiry (seconds) ---
    PRESIGNED_EXPIRY = int(os.getenv("PRESIGNED_EXPIRY", "900"))

    # --- App Info ---
    APP_NAME = "FunTube"
    APP_ENV = os.getenv("APP_ENV", "development")
