import pytest
import json
import yaml
import logging
import time
import os
from selenium import webdriver

logging.basicConfig(level=logging.DEBUG)


def add(a, b):
    return a + b


class TestA:
    @pytest.fixture(scope="class", autouse=True)
    def classA_start(self):
        logging.info("This is classA_start!!!")

    def test_one(self):
        logging.info("This is test_one!!!")
        assert add(3, 5) == 8

    def test_two(self):
        logging.info("This is test_two!!!")
        assert add(5, 4) == 9

    @pytest.mark.parametrize("a,b,expected", [(5, 7, 9)])
    def test_three(self, a, b, expected):
        logging.info("This is test_three!!!")
        assert add(a, b) == expected


class TestB:
    def test_four(self, module, classB_start):
        logging.info("This is test_four!!!")
        assert add(4, 4) == 8

    def test_five(self, module, classB_start):
        logging.info("This is test_five!!!")
        assert add(5, 5) == 8

    @pytest.mark.parametrize("a,b,expected", json.load(open("calc.json")))
    def test_six(self, module, classB_start, a, b, expected):
        # a = json.load(open("calc.json"))
        # print(a["login"])
        logging.info("This is test_six!!!")
        assert add(a, b) == expected


class TestC:
    @pytest.mark.run(order=3)
    def test_seven(self, module):
        logging.info("This is test_seven!!!")
        assert add(4, 4) == 8

    @pytest.mark.run(order=1)
    def test_eight(self, module):
        logging.info("This is test_eight!!!")
        assert add(4, 4) == 8

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize("a,b,expected", yaml.load(open("calc.yaml")))
    def test_nine(self, module, a, b, expected):
        logging.info("This is test_nine!!!")
        assert add(a, b) == expected


if __name__ == '__main__':
    report = time.strftime('%Y-%m-%d_%H:%M')
    f_path = './report/' + str(report)
    xml_path = f_path + '/xml'
    report_path = f_path + '/report'
    os.system('pytest test_work2.py --alluredir ' + xml_path)
    os.system('allure generate ' + xml_path + ' -o ' + report_path)
