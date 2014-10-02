bind = '127.0.0.1:5000'
workers = 4
backlog = 2048
accesslog = '/var/log/gunicorn/access.log'
errorlog = '/var/log/gunicorn/error.log'
loglevel = 'debug'
