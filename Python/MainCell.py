from Cell import Cell
from CellMembrane import CellMembrane
from Cytoplasm import Cytoplasm
from HereditaryMaterial import HereditaryMaterial
from HumanBody import HumanBody
from LivingBeing import LivingBeing

newCytoplasm = Cytoplasm("Cytoplasm", 50, 50)
newMembrane = CellMembrane("Membrane", 4, 15)
newDna = HereditaryMaterial("Hereditary")
newCell1 = Cell("Cell 1", newCytoplasm, newDna, newMembrane)

newHuman1 = HumanBody(newCell1)
print("/////HUMAN/////////")
newHuman1.to_string()

newCytoplasm2 = Cytoplasm("Cytoplasm", 45, 55)
newMembrane2 = CellMembrane("Membrane", 2, 12)
newDna2 = HereditaryMaterial("Hereditary")
newCell2 = Cell("Cell 2", newCytoplasm2, newDna2, newMembrane2)

newCytoplasm3 = Cytoplasm("Cytoplasm", 48, 52)
newMembrane3 = CellMembrane("Membrane", 3, 13)
newDna3 = HereditaryMaterial("Hereditary")
newCell3 = Cell("Cell 3", newCytoplasm3, newDna3, newMembrane3)

vector_LivingBeings = {LivingBeing(newCell1), LivingBeing(newCell2), LivingBeing(newCell3)}
print("///////LIVING BEING///////")
for i in vector_LivingBeings:
    i.to_string()

