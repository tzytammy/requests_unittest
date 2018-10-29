# -*- coding: utf-8 -*-
__author__ = 'genghui'
__date__ = '2018/10/10 16:28'

"""
简单测试pytest、nose库用法

单个测试case  直接运行py.test
多个测试case，可以写一个测试类，用py.test -q ***.py的方式执行测试
断言使用基本的assert即可
"""

# class TestClass:


def test_one():
    assert "h" in "this"


# def test_two():
#     x = "hello"
#     assert hasattr(x, "check")
