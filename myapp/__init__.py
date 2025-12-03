from flask import Flask

application = Flask(__name__)

from myapp import routes

