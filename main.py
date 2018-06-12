from flask import Flask
import os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mscn:199132@localhost/urlshortener'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

from views import *

if __name__ == '__main__':
    app.run()
