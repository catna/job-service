#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import db

class CompanyInfo(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    coname = db.Column(db.String(255), nullable=False)
    cosize = db.Column(db.String(255), nullable=False)
    cotype = db.Column(db.String(255), nullable=False)
    vocation = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    source = db.Column(db.String(255), nullable=False)
    coid = db.Column(db.String(255), nullable=True)
    cohash = db.Column(db.String(255), nullable=True)

    def __init__(self, coname='', cosize='', cotype='', vocation='', location='', description='', source='', coid=''):
        self.coname = coname
        self.cosize = cosize
        self.cotype = cotype
        self.vocation = vocation
        self.location = location
        self.description = description
        self.source = source
        self.coid = coid
        self.cohash = str(hash(self.coname))


