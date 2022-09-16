#!/usr/bin/python
# -*- coding: UTF-8 -*-
# import Cell


class Cytoplasm (object):
	def get_protein_percentage(self):
		"""@ReturnType int"""
		return self.___proteinPercentage

	def set_protein_percentage(self, a_protein_percentage):
		"""@ParamType aProteinPercentage int
		@ReturnType void"""
		self.___proteinPercentage = a_protein_percentage

	def get_lipid_percentage(self):
		"""@ReturnType int"""
		return self.___lipidPercentage

	def set_lipid_percentage(self, a_lipid_percentage):
		"""@ParamType aLipidPercentage int
		@ReturnType void"""
		self.___lipidPercentage = a_lipid_percentage

	def get_name(self):
		"""@ReturnType String"""
		return self.___name

	def set_name(self, a_name):
		"""@ParamType aName String
		@ReturnType void"""
		self.___name = a_name

	def __init__(self, a_name, a_protein_percentage, a_lipid_percentage):
		self.___name = a_name
		"""@AttributeType String"""
		self.___proteinPercentage = a_protein_percentage
		"""@AttributeType int"""
		self.___lipidPercentage = a_lipid_percentage
		"""@AttributeType int"""
		# self._theCell = None
		"""@AttributeType Cell
		# @AssociationType Cell
		# @AssociationMultiplicity 1"""

	def to_string(self):  # a_name, a_protein_percentage, a_lipid_percentage):
		n = self.get_name()
		pp = self.get_protein_percentage()
		lp = self.get_lipid_percentage()

		print("\nName: ", n)
		print("Protein porcentage: ", pp, "%")
		print("Lipid porcentage: ", lp, "%")
