#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from flask import Flask
from config import config
from flask_sqlalchemy import SQLAlchemy

env = 'product'

app = Flask(__name__)
app.config.from_object(config[env])
config[env].init_app(app)
db = SQLAlchemy(app)
db.init_app(app)

from .controllers import upload
app.register_blueprint(upload)




