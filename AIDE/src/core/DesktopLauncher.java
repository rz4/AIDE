package core;

import environments.OneDimenEnviro;

/**
 * DesktopLauncher is the main driver of 
 * the AI simulations.
 * 
 * @author rz4
 *
 */
public class DesktopLauncher {

	public static void main(String[] args) {
		GeneralAgent a = new GeneralAgent();
		OneDimenEnviro o = new OneDimenEnviro();
		o.addAgent(a);
		o.run(true);// Run simulation
		System.out.println(a.getNet());// Print PAPNet of General Agent.
	}

}
