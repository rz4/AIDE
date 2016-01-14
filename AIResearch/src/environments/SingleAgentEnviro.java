package environments;

import agents.Agent;

public abstract class SingleAgentEnviro {
	
	protected Agent agent;
	protected String[] actionList;
	protected String[] goal;
	
	public abstract void init();
	
	public abstract String toString();
	
	public abstract String[] getPerceptsforAgent();
	
	public abstract void updateEnviro(String action);
	
	public void run(boolean verbose){
		init();
		if(agent == null){
			System.out.println("Error: No Agent has been set.");
			return;
		}
		if(actionList == null){
			System.out.println("Error: Actions have not been defined.");
			return;
		}
		if(goal == null){
			System.out.println("Error: Goal has not been defined.");
			return;
		}
		agent.setActions(actionList);
		agent.setGoal(goal);
		agent.setActive(true);
		int numOfActions = 0;
		if(verbose) System.out.println("Simulation Started:");
		while(agent.isActive()){
			agent.sense(getPerceptsforAgent());
			agent.compute();
			if(!agent.isActive()) break;
			updateEnviro(agent.act());
			numOfActions ++;
			if(verbose) System.out.println(toString());
		}
		if(verbose) System.out.println("Simulation Finished.\nTotal Number of Actions to Goal:");
		System.out.println(numOfActions);	
	}
	
	public void setAgent(Agent agent){
		this.agent = agent;
	}
}
