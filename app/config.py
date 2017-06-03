#!/usr/bin/env pyhthon
# -*- coding: utf-8 -*-
import os
# get the absolute path of config.py
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'practice makes perfect!'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    @staticmethod
    def init_app(app):
        pass


class DevelopConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/jobs?charset=utf8'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/jobs?charset=utf8'


class ProductConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/jobs?charset=utf8'

config = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'product': ProductConfig,
    'default': DevelopConfig
}
