import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:root@127.0.0.1:3306/mic_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False