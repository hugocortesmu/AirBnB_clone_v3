#!/usr/bin/python3

import os
from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
from flask import Blueprint
from flask_cors import CORS
app = Flask(__name__)

@app.teardown_appcontext
def teardown_db(exception):
    """
    this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()

app.register_blueprint(app_views)


    app.run(host=os.getenv('HBNB_API_HOST', "0.0.0.0"),
            port=os.getenv('HBNB_API_PORT', "5000"), threaded=True)
