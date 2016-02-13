package test.tests;

import core.AIDESimulator;
import core.GeneralAgent;
import core.environments.AgentEnviro;
import test.agents.RandomAgent;
import test.environments.OneDimenEnviro;

/**
 * This driver runs test of AIDE simulating
 * One Dimensional Environment with Random Agent.
 * 
 * @author rz4
 *
 */
public class OneDimEnviro_RandomAgent_Test {

	public static void main(String[] args) {
		OneDimenEnviro o = new OneDimenEnviro();
		o.addAgent(new RandomAgent());
		AIDESimulator sim = new AIDESimulator(o,"/home/rz4/AIResults/OneDimEnviro_RandomAgent_Test.txt",100);
		sim.simulate();
	}

}
