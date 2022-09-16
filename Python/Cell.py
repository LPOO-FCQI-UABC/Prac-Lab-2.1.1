#!/usr/bin/python
# -*- coding: UTF-8 -*-

from CellMembrane import CellMembrane
from Cytoplasm import Cytoplasm
from HereditaryMaterial import HereditaryMaterial


class Cell(object):

	def get_name(self):
		"""@ReturnType String"""
		return self.___name

	def set_name(self, a_name):
		"""@ParamType aName String
		@ReturnType void"""
		self.___name = a_name

	def get_cytoplasm(self):
		"""@ReturnType String"""
		return self.___cytoplasm

	def set_cytoplasm(self, a_cytoplasm):
		self.___cytoplasm = a_cytoplasm

	def get_hereditary(self):
		"""@ReturnType String"""
		return self.___hereditary

	def set_hereditary(self, a_hereditary):
		"""@ParamType aName String
		@ReturnType void"""
		self.___hereditary = a_hereditary

	def get_cell_membrane(self):
		"""@ReturnType String"""
		return self.___cell_membrane

	def set_cell_membrane(self, a_cell_membrane):
		"""@ParamType aName String
		@ReturnType void"""
		self.___cell_membrane = a_cell_membrane

	def __init__(self, a_name, a_cytoplasm, a_hereditary, a_cell_membrane):
		self.___name = a_name
		self.___cytoplasm = a_cytoplasm
		self.___hereditary = a_hereditary
		self.___cell_membrane = a_cell_membrane

	def to_s(self):
		n = self.get_name()
		c1 = self.___cytoplasm
		cm1 = self.get_cell_membrane()
		h1 = self.get_hereditary()
		Cytoplasm.to_string(c1)
		CellMembrane.to_string(cm1)
		HereditaryMaterial.to_string(h1)

