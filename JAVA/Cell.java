public class Cell {

	LivingBeing theLivingBeing;
	HumanBody theHumanBody;
	CellMembrane theCellMembrane;
	Cytoplasm theCytoplasm;
	HereditaryMaterial theHereditaryMaterial;
	private String name;
	private Vector livingBeing;

	public String getName() {
		return this.name;
	}

	/**
	 * 
	 * @param name
	 */
	public void setName(String name) {
		this.name = name;
	}

	public Vector getLivingBeing() {
		return this.livingBeing;
	}

	/**
	 * 
	 * @param livingBeing
	 */
	public void setLivingBeing(Vector livingBeing) {
		this.livingBeing = livingBeing;
	}

}