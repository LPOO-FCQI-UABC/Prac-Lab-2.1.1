#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Cell import Cell


class HumanBody(object):
	def get_cell(self):
		"""@ReturnType Cell"""
		return self.___cell

	def set_cell(self, a_cell):
		"""@ParamType aCell Cell
		@ReturnType void"""
		self.___cell = a_cell

	def __init__(self, a_cell):
		self.___cell = a_cell
		"""@AttributeType Cell"""
		self._theCell = []
		"""@AttributeType Cell*
		# @AssociationType Cell[]
		# @AssociationMultiplicity *
		# @AssociationKind Composition"""

	def to_string(self):
		a = self.get_cell()
		Cell.to_s(a)
