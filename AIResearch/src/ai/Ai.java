package ai;

public abstract class Ai {

	protected String[] nextPercept;
	protected String nextAction;
	protected boolean active;
	
	public void sense(String[] percepts){
		nextPercept = percepts;
	}
	
	public String act(){
		return nextAction;
	}
	
	public boolean isActive(){
		return active;
	}
	
	public void setAcive(boolean active){
		this.active = active;
	}
}
