package agents;

import java.util.Random;

public class RandomAgent extends Agent{

	private Random rand;
	
	public RandomAgent(){
		rand = new Random();
	}
	
	@Override
	public void compute() {
		if(isAtGoal()) setActive(false);
		else nextAction = possibleActions[rand.nextInt(possibleActions.length)];
		
	}

}
