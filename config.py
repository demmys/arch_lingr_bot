class Default:
    DEBUG = False
    DATABASE_URI = 'sqlite://:memory:'
    SECRET_KEY = 'development key'

class Development(Default):
    DEBUG = True
    DATABASE = '/tmp/arch_lingr_bot.db'

class Production(Default):
    pass

class Test(Default):
    pass
