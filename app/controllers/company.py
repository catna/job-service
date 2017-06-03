# -*- coding: utf-8 -*-

from flask_restful import Resource
from flask_restful import request
from ..models.info import CompanyInfo
from ..models.info import CompanyInfoTaskItem
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


class CompanyInfoTask(Resource):

    def get(self):
        '''返回一个爬取列表'''
        # {
        #   "1" : "xx网",
        #   "2" : "xxxx"
        # }
        if 'need' not in request.args:
            return {}
        need = 100
        try:
            tmp = int(request.args['need'])
            need = tmp
        except Exception:
            pass
        tasks = CompanyInfoTaskItem.query.filter_by(status=0).limit(need)
        keys_dic = {}
        for task in tasks:
            keys_dic[str(task.id)] = task.coname 
            task.status = 1
        db.session.commit()
        return keys_dic
    
    def post(self):
        '''上传task表单'''
        # {
        #     "tasks": [
        #         "a",
        #         "b",
        #         "c"
        #     ]
        # }
        response = {
                'code': 0,
                'mesg': 'ok'
            }
        if 'tasks' in request.json:
            data = request.json['tasks']
            for d in data:
                a_task = CompanyInfoTaskItem()
                a_task.coname = d
                a_task.status = 0
                db.session.add(a_task)
            db.session.commit()
            return response
        response['code'] = 1
        response['mesg'] = '上传出错'
        return response
        
class CompanyInfoTaskResult(Resource):

    def post(self):
        '''上传一个爬取任务的结果'''
        # {
        #     "id": 1000,
        #     "ok": 0
        # }
        data = request.json
        if 'id' in data and 'ok' in data:
            a_task = CompanyInfoTaskItem.query.filter_by(id=data['id']).first()
            if data['ok'] == 1 and a_task:
                a_task.status = 2
            db.session.commit()
        response = {
            'code': 0,
            'mesg': 'ok'
        }
        return response

        