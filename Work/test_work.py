import pytest
import json
import yaml
import logging
import time
import os

logging.basicConfig(level=logging.DEBUG)


def setup_module():
    logging.info("login System...")


def teardown_module():
    logging.info("Clean module venv...")


def add(a, b):
    return a + b


class TestA:
    @classmethod
    def teardown_class(cls):
        logging.info("This is teardown_class!!!")
        logging.info("Clean the venv")

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
    def setup_method(self):
        logging.info("Setup...")

    def test_four(self):
        logging.info("This is test_four!!!")
        assert add(4, 4) == 8

    def test_five(self):
        logging.info("This is test_five!!!")
        assert add(5, 5) == 8

    @pytest.mark.parametrize("a,b,expected", json.load(open("calc.json")))
    def test_six(self, a, b, expected):
        logging.info("This is test_six!!!")
        assert add(a, b) == expected


class TestC:
    # @pytest.mark.run(after='test_nine')
    @pytest.mark.run(order=3)
    # @pytest.mark.run('last')
    def test_seven(self):
        logging.info("This is test_seven!!!")
        assert add(4, 4) == 8

    # @pytest.mark.run(before='test_nine')
    @pytest.mark.run(order=1)
    # @pytest.mark.run('first')
    def test_eight(self):
        logging.info("This is test_eight!!!")
        assert add(4, 4) == 8

    @pytest.mark.run(order=2)
    # @pytest.mark.run('second')
    @pytest.mark.parametrize("a,b,expected", yaml.load(open("calc.yaml")))
    def test_nine(self, a, b, expected):
        logging.info("This is test_nine!!!")
        assert add(a, b) == expected

    # @pytest.mark.run(order=2)
    # def test_nine(self):
    #     logging.info("This is test_four!!!")
    #     assert add(5, 4) == 8


if __name__ == '__main__':
    report = time.strftime('%Y-%m-%d_%H:%M')
    f_path = './report/' + str(report)
    xml_path = f_path + '/xml'
    report_path = f_path + '/report'
    os.system('pytest test_work.py --alluredir ' + xml_path)
    os.system('allure generate ' + xml_path + ' -o ' + report_path)
