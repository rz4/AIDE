package papnet;

public class PAPRoute {
	
	private String action;
	private PAPNode parent;
	private PAPNode child;
	private int visits;
	
	public PAPRoute(String act, PAPNode par, PAPNode chi){
		action = act;
		parent = par;
		child = chi;
		visits = 1;
	}
	
	public String getAction(){
		return action;
	}
	
	public PAPNode getParent(){
		return parent;
	}
	
	public PAPNode getChild(){
		return child;
	}
	
	public int getVisits(){
		return visits;
	}
	
	public void incrVisits(){
		visits ++;
	}
	
	public String toString(){
		String s = "{Route: " + parent + " " + action + " " + child + " " + visits + " }";
		return s; 
	}

}
