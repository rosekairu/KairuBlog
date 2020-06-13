import os

class Config:

    SECRET_KEY = os.environ.get('SECRET_KEY')
    API_BASE_URL='http://quotes.stormconsultancy.co.uk/random.json'
    
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://rose:kairu@localhost/kairublog'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
   
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    SUBJECT_PREFIX = 'KairuBlog'
    SENDER_EMAIL = 'moringawatchlist@gmail.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    

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