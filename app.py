from flask import Flask
from flask_restful import Api
from view.views import CarrefourScrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Secret_Key'
api = Api(app, prefix="")

api.add_resource(CarrefourScrap, '/scrap')
