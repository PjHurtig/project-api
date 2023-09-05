import os

os.environ['DEV'] = '1'
os.environ.setdefault(
    "SECRET_KEY", 'django-insecure-f-zmzkk&6z^u9prl_y1x%5ev2($@4xu1#s^q5gs-fxbs^d3e@s')
os.environ['CLOUDINARY_URL'] = 'cloudinary://243422865716314:Q-wUvrkoCbkJQGnwKMF7O5K88Ew@dqoykema9'
os.environ['DATABASE_URL'] = 'postgres://tckxgbfc:f6ltF5Vniem_ljnoVuMUQsVlsRmoS0Zl@snuffleupagus.db.elephantsql.com/tckxgbfc'
