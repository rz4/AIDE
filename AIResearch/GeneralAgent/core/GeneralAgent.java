package core;

import java.util.Random;

import agents.Agent;
import papnet.PAPNet;

public class GeneralAgent extends Agent{

	private PAPNet net;
	private Random rand;
	
	public GeneralAgent(){
		net = new PAPNet();
		rand = new Random();
	}
	
	@Override
	public void compute() {
		net.updateNet(nextPercept, goalPercept, nextAction);
		if(isAtGoal()) setActive(false);
		else nextAction = possibleActions[rand.nextInt(possibleActions.length)];
	}
	
	public PAPNet getNet(){
		return net;
	}

}
