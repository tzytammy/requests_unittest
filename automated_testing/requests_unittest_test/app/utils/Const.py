# -*- coding: utf-8 -*-
# Filename: Const.py
"""
自定义常量类
"""
import sys


class _const(object):
	"""实现一个常量类"""

	class ConstError(TypeError):
		pass

	class ConstCaseError(ConstError):
		pass

	def __setattr__(self, name, value):
		"""
		定义一个常量
		:param name:
		:param value:
		:return:
		"""
		if name in self.__dict__.keys():
			raise self.ConstError("Can't change const {}".format(name))

		if not name.isupper():
			raise self.ConstCaseError("const name {} is not all uppercase.".format(name))

		self.__dict__[name] = value


sys.modules[__name__] = _const()
