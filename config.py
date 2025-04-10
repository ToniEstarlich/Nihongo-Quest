import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = "postgresql://postgres:Toni2207@localhost/nihongo_db"

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "0000"
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False