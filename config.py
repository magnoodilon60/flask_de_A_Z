import os, random, string


class Config(object):
    CSRF_ENABLE = True
    SECRET = 'd297b7656e5496e9c2c5f41f844c018652747ba91872f85057f9113a57c7db8c'
    TEMPLATE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    APP = None


class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = False
    IP_HOST = 'localhost'
    PORT_HOST = 8000
    URL_MAIN = 'http://%s/%s' % (IP_HOST, PORT_HOST) # http://localhost:8000


app_config = {
    'development': DevelopmentConfig(),
    'testing': None,
    'production': None
}

app_active = os.getenv('FLASK_ENV')

if app_config is None:
    app_config = 'development'
