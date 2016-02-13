package test.agents;

import java.util.Random;

import core.agent.Agent;

/**
 * Version 1.0
 * 
 * RandomAgent is an agent that chooses a random
 * action from the list of possible actions.
 * 
 * It becomes inactive after it has reached the 
 * goal.
 * 
 * This agent is used to compare effectiveness of 
 * other agents.
 * 
 * @author rz4
 *
 */
public class RandomAgent extends Agent{

	private Random rand;
	
	public RandomAgent(){
		super();
		rand = new Random();
	}
	
	@Override
	public void compute() {
		updateGoals(nextPercepts);
		if(goalsActive()) setActive(false);
		else nextAction = possibleActions[rand.nextInt(possibleActions.length)];
		
	}

}
