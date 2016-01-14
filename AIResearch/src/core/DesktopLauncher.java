package core;

import environments.OneDimenEnviro;

public class DesktopLauncher {

	public static void main(String[] args) {
		GeneralAgent a = new GeneralAgent();
		OneDimenEnviro o = new OneDimenEnviro();
		o.setAgent(a);
		o.run(true);
		System.out.println(a.getNet());
	}

}
