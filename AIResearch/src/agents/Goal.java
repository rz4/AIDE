package agents;

public class Goal {

	private Percept[] goal;
	private boolean active;
	
	public Goal(Percept[] g) {
		goal = g;
		active = true;
	}
	
	public boolean equalsPercepts(Percept[] pa){
		boolean flag = true;
		if(pa.length != goal.length) flag = false;
		for(int i = 0; i < pa.length; i++) if(!pa[i].equals(goal[i])) flag = false;
		return flag;
	}
	
	public float similarPercepts(Percept[] pa){
		float val = 0;
		for(int i = 0; i < pa.length; i++){
			if(goal[i].equals(pa[i])) val ++;
		}
		return val / goal.length;
	}
	
	public void setActive(boolean a){
		active = a;
	}
	
	public boolean isActive(){
		return active;
	}

}
