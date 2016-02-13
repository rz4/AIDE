package test.tests;

import core.GeneralAgent;
import test.environments.OneDimenEnviro;

public class OneDimEnviro_GeneralAgent_Test {

	public static void main(String[] args) {
		GeneralAgent a = new GeneralAgent();
		OneDimenEnviro o = new OneDimenEnviro();
		o.addAgent(a);
		o.run(false);// Run simulation
		System.out.println(a.getNet());// Print PAPNet of General Agent.
	}

}
