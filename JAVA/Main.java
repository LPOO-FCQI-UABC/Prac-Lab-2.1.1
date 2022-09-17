import java.util.ArrayList;

public class Main {
    public static void main(String[] args){
        System.out.println("////// HUMAN ///////\n");
        Cytoplasms cytoplasm1 = new Cytoplasms("Cytoplasm", 50, 50);
        CellMembranes cellMembranes1 = new CellMembranes("Membrane", 4, 15);
        HereditaryMaterial hereditaryMaterial1 = new HereditaryMaterial("Hereditary");
        Cell cell1 = new Cell("Cell 1", cytoplasm1, cellMembranes1, hereditaryMaterial1);
        HumanBody cuerpo_humano = new HumanBody(cell1);
        cuerpo_humano.to_String();

        System.out.println("\n/////// LIVING BEINGS ///////\n");
        Cytoplasms cytoplasm2 = new Cytoplasms("Cytoplasm", 15, 35);
        CellMembranes cellMembranes2 = new CellMembranes("Membrane", 6, 1);
        HereditaryMaterial hereditaryMaterial2 = new HereditaryMaterial("Hereditary");
        Cell cell2 = new Cell("Cell 2", cytoplasm2, cellMembranes2, hereditaryMaterial2);
        
        Cytoplasms cytoplasm3 = new Cytoplasms("Cytoplasm", 0, 100);
        CellMembranes cellMembranes3 = new CellMembranes("Membrane", 66, 69);
        HereditaryMaterial hereditaryMaterial3 = new HereditaryMaterial("Hereditary");
        Cell cell3 = new Cell("Cell 3", cytoplasm3, cellMembranes3, hereditaryMaterial3);
        
         
        ArrayList<Cell> vector_LivingBeing = new ArrayList<Cell>();
        vector_LivingBeing.add(cell2);
        vector_LivingBeing.add(cell3);
        for(Cell cell: vector_LivingBeing){
            cell.to_String();
        }
        
    }
}