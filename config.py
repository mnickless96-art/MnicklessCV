import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['mnickless@gmail.com']
    POSTS_PER_PAGE = 25
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY ="6Vrwd12PmMjD3MynpSHhkehs61Et470OBJrKf8xgrNNZ8wBpEvUYJQQJ99CEACmepeSXJ3w3AAAbACOG3NNQ"

