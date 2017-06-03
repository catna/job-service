# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask_restful import request
from ..models.info import CompanyInfo
from .. import db

class CompanyInfoUploader(Resource):

    def post(self):
        response = {
            'code': 0,
            'mesg': 'ok'
        }
        data = request.json
        an_item = CompanyInfo()

        for (k, v) in data.items():
            try:
                setattr(an_item, k, v)
            except Exception:
                pass

        print an_item.__dict__
        if an_item.coname == '':
            response['code'] = 1
            response['mesg'] = 'faild'
            return response
        
        db.session.add(an_item)
        db.session.commit()
        return response

        
        