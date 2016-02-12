package agents;

import java.util.Random;

/**
 * RandomAgent is an agent that chooses a random
 * action from the list of possible actions.
 * 
 * It becomes inactive after it has reached the 
 * goal.
 * 
 * This agent is used to compare effectiveness of 
 * other agents.
 * 
 * @author Rafael Zamora
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
		if(goalsMet()) setActive(false);
		else nextAction = possibleActions[rand.nextInt(possibleActions.length)];
		
	}

}
