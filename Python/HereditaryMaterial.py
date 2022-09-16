#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import Cell


class HereditaryMaterial(object):
	def get_name(self):
		"""@ReturnType String"""
		return self.___name

	def set_name(self, a_name):
		"""@ParamType aName String
		@ReturnType void"""
		self.___name = a_name

	def __init__(self, a_name):
		self.___name = a_name
		"""@AttributeType String"""
	def to_string(self):
		n = self.get_name()
		print("\nCaracteristic: ", n)
