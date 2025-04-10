import os

DATABASE_URL = "postgresql://postgres:Toni2207@localhost/nihongo_db"

# SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@host:port/nihongo_quest'

# DATABASE_URI = os.environ.get("DATABASE_URL")

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "0000"
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False