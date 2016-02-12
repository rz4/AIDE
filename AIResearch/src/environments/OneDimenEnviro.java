package environments;

import agents.Action;
import agents.Goal;
import agents.Percept;

public class OneDimenEnviro extends AgentEnviro {

	private String[] enviro;
	private int size;
	private int agentPos;
	private int goalPos;
	
	@Override
	public void initEnviro() {
		size = 10; //Change size of environment here.
		agentPos = 5; //Change initial position of agent here.
		Action[] a = {new Action("L"), new Action("R")};
		actionList = a;
		goalPos = 9;
		Percept[] g = {new Percept(Integer.toString(goalPos))};//Change goal here.
		goal = new Goal(g);
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
			else if(Integer.parseInt(s) == goalPos) display += "G ";
			else display += "0 ";
		}
		return display;
	}

	@Override
	public Percept[] getPerceptsforAgent() {
		Percept[] pa = new Percept[1];
		pa[0] = new Percept(enviro[agentPos]);
		return pa;
	}

	@Override
	public void updateEnviro(Action action) {
		if(action == null) return;
		else if(actionList[0].equals(action)){
			if(agentPos > 0) agentPos --;
		}
		else if(actionList[1].equals(action)){
			if(agentPos < size-1) agentPos ++;
		}
	}
}