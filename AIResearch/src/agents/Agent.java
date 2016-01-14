package agents;

public abstract class Agent {

	protected String[] possibleActions;
	protected String[] goalPercept;
	protected String[] nextPercept;
	protected String nextAction;
	protected boolean active;
	
	public abstract void compute();
	
	public void setActions(String[] actionList){
		possibleActions = actionList;
	}
	
	public void setGoal(String[] goal){
		goalPercept = goal;
	}
	
	public boolean isAtGoal(){
		boolean flag = true;
		for(int i = 0; i < goalPercept.length; i++){
			if(!goalPercept[i].equals(nextPercept[i])){
				flag = false;
			}
		}
		return flag;
	}
	
	public void sense(String[] percepts){
		nextPercept = percepts;
	}
	
	public String act(){
		return nextAction;
	}
	
	public boolean isActive(){
		return active;
	}
	
	public void setActive(boolean active){
		this.active = active;
	}
	
}
