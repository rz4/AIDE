package papnet;

import agents.Percept;

public class PAPNode {
	
	private Percept[] percept;
	private int visits;
	private float value;
	private float mtsValue;
	
	public PAPNode(Percept[] per, float val) {
		percept = per;
		visits = 1;
		value = val;
		mtsValue = val;
	}

	public Percept[] getPercepts() {
		return percept;
	}

	public int getVisits() {
		return visits;
	}

	public void incrVisits(){
		visits ++;
	}
	
	public void resetVisits(){
		visits = 1;
	}

	public float getValue() {
		return value;
	}

	public float getMTSValue(){
		return mtsValue;
	}
	
	public void setMTSValue(float value) {
		mtsValue = value;
	}
	
	public String toString(){
		String s = "[Node: ( ";
		for(Percept p : percept){
			s += p + " ";
		}
		s += ") " + visits + " " + value + " " + mtsValue + " ]" ;
		return s;
	}
}