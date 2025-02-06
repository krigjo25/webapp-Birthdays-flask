
class DefaultConfig(object):
    DEBUG = False
    TESTING = False
    SESSION_TYPE = None
    SESSION_PERMANENT = False
    DATABASE_URL = 'sqlite:///birthdays.db'

class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SESSION_TYPE = 'filesystem'
