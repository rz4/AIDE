package environments;

import java.util.ArrayList;

import agents.Action;
import agents.Agent;
import agents.Goal;
import agents.Percept;

public abstract class AgentEnviro {
	
	protected ArrayList<Agent> agents;
	protected Action[] actionList;
	protected Goal goal;
	protected int cycle;
	
	public AgentEnviro(){
		agents = new ArrayList<Agent>();
	}
	
	public abstract void initEnviro();
	
	public abstract String toString();
	
	public abstract Percept[] getPerceptsforAgent();
	
	public abstract void updateEnviro(Action action);
	
	public boolean checkforErrors(){
		if(agents.isEmpty()){
			System.out.println("Error: No Agents have been set.");
			return true;
		}
		if(actionList == null){
			System.out.println("Error: Actions have not been defined.");
			return true;
		}
		if(goal == null){
			System.out.println("Error: Goal has not been defined.");
			return true;
		}
		return false;
	}
	
	public void initAgents(){
		for(Agent agent: agents){
			agent.setActions(actionList);
			agent.addGoal(goal);
			agent.setActive(true);
		}
	}
	
	public void updateAgents(){
		for(Agent agent : agents){
			if(agent.isActive()){
				agent.sense(getPerceptsforAgent());
				agent.compute();
				updateEnviro(agent.act());
			}
		}		
	}

	public boolean areagentsActive(){
		boolean flag = false;
		for(Agent a : agents) if(a.isActive()) flag = true;
		return flag;
	}
	
	public void run(boolean verbose){
		initEnviro();
		if(checkforErrors()) return;
		initAgents();
		
		cycle = 0;
		
		if(verbose) System.out.println("Simulation Started:");
		while(areagentsActive()){
			updateAgents();
			cycle ++;
			if(verbose) System.out.println(toString());
		}
		if(verbose) System.out.println("Simulation Finished.");
		System.out.printf("\nTotal Number of Actions to Goal: %s\n",cycle);	
	}
	
	public void addAgent(Agent agent){
		agents.add(agent);
	}
}