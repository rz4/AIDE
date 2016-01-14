package papnet;

public class PAPNode {
	
	private String[] percept;
	private int visits;
	private float value;
	
	public PAPNode(String[] per, float val){
		percept = per;
		visits = 1;
		value = val;
	}

	public String[] getPercept() {
		return percept;
	}

	public int getVisits() {
		return visits;
	}

	public void incrVisits() {
		visits ++;
	}

	public float getValue() {
		return value;
	}

	public void setValue(float value) {
		this.value = value;
	}
	
	public String toString(){
		String s = "[Node: ( ";
		for(String p : percept){
			s += p + " ";
		}
		s += ") " + visits + " " + value + " ]" ;
		return s;
	}
	
	
}
