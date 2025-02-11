import os

DATABASE_URI = "postgresql://postgres:Toni2207@localhost/nihongo_db"

class Config:
    SQLALCHEMY_DATABASE_URI = DATABASE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
