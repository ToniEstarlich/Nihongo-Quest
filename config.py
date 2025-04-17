import os
#from dotenv import load_dotenv

#load_dotenv()

#DATABASE_URL = "postgresql://postgres:Toni2207@localhost/nihongo_db"
# DATABASE_URL = os.environ.get("DATABASE_URL")

class Config:
    # SECRET_KEY = os.environ.get("SECRET_KEY") or "0000"
    # SQLALCHEMY_DATABASE_URI = DATABASE_URL
    #SECRET_KEY = os.environ.get("SECRET_KEY", "0000")
   # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SECRET_KEY = "0000"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Toni2207@localhost/nihongo_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False