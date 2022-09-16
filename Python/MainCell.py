from Cell import Cell
from CellMembrane import CellMembrane
from Cytoplasm import Cytoplasm
from HereditaryMaterial import HereditaryMaterial
from HumanBody import HumanBody
from LivingBeing import LivingBeing

newCytoplasm = Cytoplasm("Cytoplasm", 50, 50)
newMembrane = CellMembrane("Membrane", 4, 15)
newDna = HereditaryMaterial("Hereditary")

newCell1 = Cell("Cell", newCytoplasm, newDna, newMembrane)
newHuman1 = HumanBody(newCell1)
print("/////HUMAN/////////")
newHuman1.to_string()

newCytoplasm2 = Cytoplasm("Cytoplasm", 45, 55)
newMembrane2 = CellMembrane("Membrane", 2, 12)
newDna2 = HereditaryMaterial("Hereditary")

newCell2 = Cell("Cell", newCytoplasm2, newDna2, newMembrane2)
newOrganism = LivingBeing(newCell2)
print("///////LIVING BEING///////")
newOrganism.to_string()

