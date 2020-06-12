import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    API_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rose:kairu@localhost/kairublog'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    SUBJECT_PREFIX = 'kairublog'
    SENDER_EMAIL = 'moringawatchlist@gmail.com'

    @staticmethod
    def init_app(app):
        pass

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rose:kairu@localhost/kairublog_test'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")



class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rose:kairu@localhost/kairublog'
    DEBUG = True


    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}