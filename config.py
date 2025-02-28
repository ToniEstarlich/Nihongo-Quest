import os

DATABASE_URI = "postgresql://postgres:Toni2207@localhost/nihongo_db"

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "0000"
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False