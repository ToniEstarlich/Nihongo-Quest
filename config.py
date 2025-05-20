import os

class Config:
    # SECRET_KEY = os.environ.get("SECRET_KEY", "0000")
    # SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:Toni2207@localhost/nihongo_db"
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
   # app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    # SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.environ.get("SECRET_KEY", "default_secret")
    uri = os.environ.get("DATABASE_URL")
    if uri and uri.startswith("postgres://"):
        uri = uri.replace("postgres://", "postgresql://", 1)
    
    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False