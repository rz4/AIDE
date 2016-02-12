package core;

import java.util.Random;

import agents.Agent;
import papnet.PAPNet;

public class GeneralAgent extends Agent{

	private PAPNet net;
	private Random rand;
	
	public GeneralAgent(){
		super();
		net = new PAPNet();
		rand = new Random();
	}
	
	@Override
	public void compute() {
		net.updateNet(nextPercepts, goals.get(0), nextAction);
		updateGoals(nextPercepts);
		if(goalsMet()) setActive(false);
		else nextAction = possibleActions[rand.nextInt(possibleActions.length)];
	}
	
	public PAPNet getNet(){
		return net;
	}
}