#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Parson

import requests
import pytest
from unittest.mock import MagicMock


@pytest.fixture(autouse=True)
def mock_get(monkeypatch):
    def mock(*args, **kwargs):
        print(args)
        print(kwargs)
        return "Get_Mock"

    # monkeypatch.setattr(requests.sessions.Session, "request", mock)
    # monkeypatch.setattr(requests.sessions.Session, "send", mock)
    monkeypatch.setattr(requests, "get", mock)

    # monkeypatch.setattr("requests.sessions.Session.get", mock)


def test_get(mock_get):
    print(requests.get("http://www.baidu.com"))
    print(requests.post("http://www.baidu.com"))


# from unittest.mock import MagicMock
#
# import requests
# import pytest

# @pytest.fixture(autouse=True)
# def mock_requests(monkeypatch):
#     """Remove requests.sessions.Session.request for all tests."""
#
#     # monkeypatch.delattr("requests.sessions.Session.request")
#     def mock(*args, **kwargs):
#         print("mock")
#         print(args)
#         print(kwargs)
#         return "Post_mock"
#
#     monkeypatch.setattr(requests.sessions.Session, "request", mock)
    # monkeypatch.setattr(requests.sessions.Session, "send", mock)
    # monkeypatch.setattr("requests.sessions.Session.request", mock)


# def test_post(mock_requests):
#     print(requests.request("get", "http://www.baidu.com"))
#     print(requests.post("http://www.baidu.com"))


# def test_mock():
#     requests.request = MagicMock(return_value="mock")
#     print(requests.request("get", "http://www.baidu.com"))



