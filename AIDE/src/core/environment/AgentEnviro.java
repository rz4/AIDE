package core.environment;

import java.util.ArrayList;

import core.agent.Action;
import core.agent.Agent;
import core.agent.Goal;
import core.agent.Percept;

/**
 * Abstract Class
 * @author rz4
 *
 */
public abstract class AgentEnviro {
	
	protected ArrayList<Agent> agents;
	protected ArrayList<Integer> agentCycles;
	protected Action[] legalActions;
	protected Goal goal;
	protected int cycle;
	protected int cycleLimit;
	
	public AgentEnviro(){
		agents = new ArrayList<Agent>();
		agentCycles = new ArrayList<Integer>();
		cycleLimit = 0;
	}
	
	protected abstract void initEnviro();
	
	protected abstract void updateEnviro(Action action);
	
	protected abstract Percept[] getPerceptsforAgent();

	public abstract String toString();
	
	private boolean checkforErrors(){
		if(agents.isEmpty()){
			System.out.println("Error: No Agents have been set.");
			return true;
		}
		if(legalActions == null){
			System.out.println("Error: Actions have not been defined.");
			return true;
		}
		if(goal == null){
			System.out.println("Error: Goal has not been defined.");
			return true;
		}
		return false;
	}
	
	public void addAgent(Agent agent){
		agents.add(agent);
	}
	
	private void initAgents(){
		for(Agent agent: agents){
			agent.initAgent();
			agent.setLegalActions(legalActions);
			agent.addGoal(new Goal(goal));
			agent.setActive(true);
			agentCycles.add(0);
		}
	}
	
	private void updateAgents(){
		for(int i = 0; i < agents.size(); i++){
			Agent agent = agents.get(i);
			if(agent.isActive()){
				agent.sense(getPerceptsforAgent());
				agent.compute();
				updateEnviro(agent.act());
				agentCycles.set(i, cycle);
			}
		}		
	}

	protected boolean agentsActive(){
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
		while(agentsActive() && cycle < cycleLimit+1){
			updateAgents();
			cycle ++;
			if(verbose) System.out.println(toString());
		}
		if(verbose) System.out.println("Simulation Finished.");
	}
	
	public String[] getResults(){
		ArrayList<String> resultsList = new ArrayList<String>();
		for(int i = 0; i < agents.size(); i++){
			resultsList.add(agents.get(i).getClass().getName());
			int c = agentCycles.get(i);
			if(c < cycleLimit) resultsList.add(Integer.toString(c));
			else resultsList.add("DNF");
		}
		String[] results = new String[resultsList.size()];
		resultsList.toArray(results);
		return results;
	}
	
	public int getCycleLimit(){
		return cycleLimit;
	}
}