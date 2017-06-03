# -*- coding: utf-8 -*-

import unittest
import sys
sys.path.append('..')
from app.models.info import CompanyInfo
from app import db

class TestCompanyInfo(unittest.TestCase):

    def setUp(self):
        db.create_all()
        pass

    def tearDown(self):
        pass

    def test_usage(self):
        a_info = CompanyInfo('测试', '100人', '民营', '互联网', '上海市', '', '51job', '1002')
        db.session.add(a_info)
        db.session.commit()
        pass

def main():
    unittest.main()

if __name__ == '__main__':
    main()
