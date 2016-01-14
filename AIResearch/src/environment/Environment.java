package environment;

import ai.Ai;

public abstract class Environment {
	
	protected Ai agent;
	
	public Environment(Ai agent){
		this.agent = agent;
	}
	
	public void run(boolean verbose){
		agent.setAcive(true);
	}
	
	public abstract void init();
}
