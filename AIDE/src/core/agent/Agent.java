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
 * This class allows for goals to be defined
 * and check if agent has met goals.
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
	 * Method should define the decision behavior
	 * of the agent. This method will be accessed by the 
	 * environment.
	 */
	public abstract void compute();
	
	/**
	 * Method initializes agent for simulations.
	 */
	public void initAgent(){
		goals = new ArrayList<Goal>();
		nextPercepts = null;
		nextAction = null;
	}
	
	/**
	 * Method sets the array of legal actions
	 * the agent can take use in order to meet defined
	 * goals.
	 * 
	 * @param actionList String[]
	 */
	public void setLegalActions(Action[] actionList){
		possibleActions = actionList;
	}
	
	/**
	 * Method adds a goal to the list
	 * goals that need to be met.
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
	 * @param pa Percept[]
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
	 * Method returns a boolean value indicating 
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
	 * Method sets the current percept of the agent.
	 * This method will be accessed by the environment.
	 *  
	 * @param percepts Percept[]
	 */
	public void sense(Percept[] percepts){
		nextPercepts = percepts;
	}
	
	/**
	 * Method returns the current action the agent
	 * will take. This method will be accessed by the 
	 * environment.
	 * 
	 * @return nextAction Action
	 */
	public Action act(){
		return nextAction;
	}

	/**
	 * Method returns whether the agent is active.
	 * This method will be accessed by the environment.
	 * 
	 * @return active boolean
	 */
	public boolean isActive(){
		return active;
	}
	
	/**
	 * Method sets whether the agent is active.
	 * 
	 * @param active boolean
	 */
	public void setActive(boolean active){
		this.active = active;
	}	
}