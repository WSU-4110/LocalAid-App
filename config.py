import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'devkey123'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///localaid.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
