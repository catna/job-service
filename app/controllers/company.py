# -*- coding: utf-8 -*-

from flask_restful import Resource

class CompanyInfoUploader(Resource):

    def post(self):
        return {
            'code': 0,
            'mesg': 'ok'
        }

