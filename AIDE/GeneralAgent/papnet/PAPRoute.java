package papnet;

import agents.Action;

public class PAPRoute {
	
	private Action action;
	private PAPNode parent;
	private PAPNode child;
	private int visits;
	
	public PAPRoute(Action act, PAPNode par, PAPNode chi){
		action = act;
		parent = par;
		child = chi;
		visits = 1;
	}
	
	public Action getAction(){
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
	
	public void resetVisits(){
		visits = 0;
	}
	
	public String toString(){
		String s = "{Route: " + parent + " " + action + " " + child + " " + visits + " }";
		return s; 
	}
}