package core.agent;

/**
 * Version 1.0
 * 
 * Class for defining goal states for Agents.
 * 
 * Goal value should be defined by the array of Percepts
 * of the goal state.
 * 
 * Weight value can be either negative or positive.
 * Positive weight means Agents should move towards goal.
 * Negative weight means Agents should avoid goal.
 * 
 * True Constant value means the goal must be met at all times.
 * False Constant value means the goal only needs to be met once.
 * 
 * Active value determines if the goal has been met.
 * 
 * @author rz4
 *
 */
public class Goal {

	protected Percept[] goal;
	protected float weight;
	protected boolean constant;
	protected boolean active;
	
	public Goal(Percept[] g, float w, boolean c) {
		goal = g;
		weight = w;
		constant = c;
		active = true;
	}
	
	public Goal(Goal g){
		goal = g.goal;
		weight = g.weight;
		constant = g.constant;
		active = true;
	}
	
	public boolean equals(Goal g){
		if(g instanceof Goal)
			return ((Goal) g).goal.equals(goal);
		else return false;
	}
	
	/**
	 * Method returns whether the Goal's Percept[] is
	 * equal to passed Percept[].
	 * 
	 * @param pa Percept[]
	 * @return boolean
	 */
	public boolean equalsPercepts(Percept[] pa){
		return Percept.perceptsEqual(goal, pa);
	}
	
	
    /**
	 * Method returns a float value between 0.0 and 1.0 depending on
	 * how the fraction of Goal Percept[] that are equal to the passed Percept[]s.
	 *
	 *@param pa Percept[]
	 *@return float
	 */
	public float similarPercepts(Percept[] pa){
		return Percept.perceptsSimilar(goal, pa);
	}
	
	public float getWeight(){
		return weight;
	}
	
	/**
	 * Method returns a float value of the relative weight value for
	 * the passed Percept[].
	 * 
	 * @param pa
	 * @return
	 */
	public float getRelativeWeight(Percept[] pa){
		return weight * similarPercepts(pa);
	}
	
	public boolean isConstant(){
		return constant;
	}
	
	public void setActive(boolean a){
		active = a;
	}
	
	public boolean isActive(){
		return active;
	}
}