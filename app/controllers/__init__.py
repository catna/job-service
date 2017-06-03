# -*- coding: utf-8 -*-

from flask_restful import Api
from flask import Blueprint

upload = Blueprint('upload', __name__)
upload_api = Api(upload)

from company import *
upload_api.add_resource(CompanyInfoUploader, '/company/info')
upload_api.add_resource(CompanyInfoTask, '/company/info/task')
upload_api.add_resource(CompanyInfoTaskResult, '/company/info/task_result')

from home import *
upload_api.add_resource(Home, '/')