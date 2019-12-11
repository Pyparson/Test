#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Parson
# 参数化示例,包含加载直接参数化,加载Json文件和yaml文件
import logging
import allure
import yaml
import pytest
import json

logging.basicConfig(level=logging.INFO)


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


class TestParams:
    @pytest.fixture(scope="class", autouse=True)
    def class_logging(self):
        logging.info("Start Class...")
        yield
        logging.info("Finish Class...")

    @pytest.fixture(autouse=True)
    def method_logging(self):
        logging.info("Start Method...")
        yield
        logging.info("Finnish Method...")

    @allure.description("加法计算")
    @pytest.mark.parametrize("a,b,expected", [(5, 7, 9),
                                              (4, 4, 8),
                                              (9, 9, 18),
                                              (40, 40, 1),
                                              (6, 5, 30)])
    def test_add(self, a, b, expected):
        sum = add(a, b)
        assert expected == sum, "Test Failed!!!"

    @allure.description("减法计算")
    @pytest.mark.parametrize("a,b,expected", yaml.load(open("params.yaml"))["Sub"])
    def test_sub(self, a, b, expected):
        sum = sub(a, b)
        assert expected == sum, "Test Failed!!!"

    @allure.description("乘法计算")
    @pytest.mark.parametrize("a,b,expected", yaml.load(open("params.yaml"))["Mul"])
    def test_mul(self, a, b, expected):
        sum = mul(a, b)
        assert expected == sum, "Test Failed!!!"

    @allure.description("除法计算")
    @pytest.mark.parametrize("a,b,expected", json.load(open("calc.json")))
    def test_div(self, a, b, expected):
        sum = div(a, b)
        assert expected == sum, "Test Failed!!!"

    # @pytest.mark.skip(reason="no way of currently testing this")
    # @pytest.mark.parametrize("a,b,expected", yaml.load(open("params.yaml"))["Mix"])
    # def test_mix(self,a, b, expected):
    #     print(yaml.load(open("params.yaml"))["Mix"])
    #     print(a)
    #     print(b)
    #     print(expected)

    @pytest.mark.parametrize("a", yaml.load(open("params.yaml"))["Mix"])
    def test_mix(self, a):
        print(yaml.load(open("params.yaml"))["Mul"])
        print(a)