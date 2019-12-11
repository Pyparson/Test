#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Parson
import pytest


def add(x,y):
    return x+y

def div(x,y):
    return x/y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

@pytest.mark.parametrize("a,b,expected",[
    (1,3,4),
    (6,3,2),
    (5,3,2),
    (3,3,9),
    (20,20,40),
])
def test_add(a,b,expected):
    print(a,b,expected)
    assert add(a, b) == expected

@pytest.mark.parametrize("a,b,expected",[
    (1,3,4),
    (6,3,2),
    (5,3,2),
    (3,3,9),
    (20,20,40),
])
def test_div(a,b,expected):
    print(a, b, expected)
    assert div(a, b) == expected

@pytest.mark.parametrize("a,b,expected",[
    (1,3,4),
    (6,3,2),
    (5,3,2),
    (3,3,9),
    (20,20,40),
])
def test_sub(a,b,expected):
    print(a, b, expected)
    assert sub(a, b) == expected

@pytest.mark.parametrize("a,b,expected",[
    (1,3,4),
    (6,3,2),
    (5,3,2),
    (3,3,9),
    (20,20,40),
])
def test_mul(a,b,expected):
    print(a, b, expected)
    assert mul(a, b) == expected

@pytest.mark.parametrize("a,b,expected",[
    (3,5,8),
    (8,5,13),
    (6,6,12),
    (15,4,13),
    (20,20,40),
])
def test_add1(a,b,expected):
    print(a, b, expected)
    assert add(a,b) == expected