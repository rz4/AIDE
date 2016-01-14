package environments.base;

public class OneDimenEnviro extends SingleAgentEnviro {

	private String[] enviro;
	private int size;
	private int agentPos;
	
	@Override
	public void init() {
		size = 10; //Change size of environment here.
		agentPos = 0; //Change initial position of agent here.
		String[] a = {"L", "R"};
		actionList = a;
		String[] g = {"8"};//Change goal here.
		goal = g;
		enviro = new String[size];
		for(int i = 0; i < size; i++){
			enviro[i] = Integer.toString(i);
		}
	}

	@Override
	public String toString() {
		String display = "One Dimensional Environment:\n";
		for(String s : enviro){
			if(Integer.parseInt(s) == agentPos) display += "A ";
			else if(s.equals(goal[0])) display += "G ";
			else display += "0 ";
		}
		return display;
	}

	@Override
	public String[] getPerceptsforAgent() {
		String[] percept = new String[1];
		percept[0] = enviro[agentPos];
		return percept;
	}

	@Override
	public void updateEnviro(String action) {
		if(action == null) return;
		switch(action){
		case "L":
			if(agentPos > 0) agentPos --;
			break;
		case "R":
			if(agentPos < size-1) agentPos ++;
			break;
		default:
			break;
		}
		
	}

}
