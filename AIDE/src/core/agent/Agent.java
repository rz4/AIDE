package core.agent;

import java.util.ArrayList;

/**
 * Version 1.0
 * 
 * Abstract Class for agents which allows
 * agent to interface with environments.
 * 
 * All decision making should be defined in
 * compute().
 * 
 * Environments will pass percept value prior
 * to execution of compute() through sense().
 * 
 * Environments will read computed action after
 * execution of compute() through act().
 * 
 * Environments will continue to simulate as long
 * as agent is active.
 * 
 * This class allows for a goal percept to be set
 * and check if agent has arrived at goal.
 * This should be used to determine when the agent
 * should no longer be active.
 * 
 * @author rz4
 *
 */
public abstract class Agent {

	protected Action[] possibleActions;
	protected ArrayList<Goal> goals;
	protected Percept[] nextPercepts;
	protected Action nextAction;
	protected boolean active;

	/**
	 * This method should define the decision making 
	 * of the agent. This method will be accessed by the 
	 * environment.
	 */
	public abstract void compute();
	
	/**
	 * This method initializes agent for simulations.
	 */
	public void initAgent(){
		goals = new ArrayList<Goal>();
	}
	
	/**
	 * This method sets the array of possible actions
	 * the agent can take in order to reach the goal
	 * percept.
	 * 
	 * @param actionList String[]
	 */
	public void setActions(Action[] actionList){
		possibleActions = actionList;
	}
	
	/**
	 * This method sets the goal percept array the
	 * agent should try to reach.
	 * 
	 * @param goal
	 */
	public void addGoal(Goal g){
		goals.add(g);
	}
	
	/**
	 * Method checks every goal against Percept[]
	 * and sets goals activity to false if met.
	 * Checks if goals are negative or positive.
	 * 
	 * @param pa
	 */
	public void updateGoals(Percept[] pa){
		for(Goal g : goals)
			if(g.getWeight() >= 0){
				if(g.equalsPercepts(pa)) g.setActive(false);
				else if(g.isConstant()) g.setActive(true);
			}
			else{
				if(!g.equalsPercepts(pa)) g.setActive(false);
				else if(g.isConstant()) g.setActive(true);
			}
	}
	
	/**
	 * This method returns a boolean value indicating 
	 * whether the agent goals are met.
	 * 
	 * @return boolean flag
	 */
	public boolean goalsActive(){
		boolean flag = true;
		for(Goal g : goals) if(g.isActive()) flag = false;
		return flag;
	}
	
	/**
	 * This method sets the current percept of the agent.
	 * This method will be accessed by the environment.
	 *  
	 * @param percepts String[]
	 */
	public void sense(Percept[] percepts){
		nextPercepts = percepts;
	}
	
	/**
	 * This method returns the current action the agent
	 * will take. This method will be accessed by the 
	 * environment.
	 * 
	 * @return nextAction String
	 */
	public Action act(){
		return nextAction;
	}

	/**
	 * This method returns whether the agent is active.
	 * This method will be accessed by the environment.
	 * 
	 * @return active boolean
	 */
	public boolean isActive(){
		return active;
	}
	
	/**
	 * This method sets whether the agent is active.
	 * 
	 * @param active boolean
	 */
	public void setActive(boolean active){
		this.active = active;
	}
	
}
