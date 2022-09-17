public class HumanBody {

	private Cell cell;

	public HumanBody(Cell cell1) {
        cell = cell1;
    }

    public Cell getCell() {
		return this.cell;
	}

	public void setCell(Cell cell) {
		this.cell = cell;
	}

    public void to_String(){
        cell.to_String();
    }
}