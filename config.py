import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "0000")
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Toni2207@localhost/nihongo_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False