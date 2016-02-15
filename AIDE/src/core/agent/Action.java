package core.agent;

/**
 * Version 1.0
 * 
 * Class creates a Action object used to 
 * express and describe actuation desired by
 * an Agent.
 * 
 * Actions will be used to communicate between 
 * Environments and Agents what changes must be 
 * applied to the Environment by the Agent.
 * 
 * All Actions should be initialized with a 
 * unique identifier.
 * 
 * @author rz4
 *
 * @param <T>
 */
public class Action<T> {

	protected T act_id;
	
	/**
	 * Method constructs Action with generic
	 * identifier.
	 * 
	 * @param a
	 */
	public Action(T a) {
		act_id = a;
	}
	
	/**
	 * Method returns whether two Actions are 
	 * equal. 
	 * 
	 * @param a Object
	 * @return boolean
	 */
	public boolean equals(Object a){
		if(a instanceof Action)
			return ((Action<?>)a).act_id.equals(act_id);
		else return false;
	}
	
	
	public String toString(){
		return act_id.toString();
	}
	
	/**
	 * Static Method returns whether two Action[]s are
	 * equal.
	 * 
	 * @param aa1
	 * @param aa2
	 * @return
	 */
	public static boolean actionsEqual(Action[] aa1, Action[] aa2){
		boolean flag = true;
		if(aa1.length != aa2.length) flag = false;
		for(int i = 0; i < aa1.length; i++) if(!aa1[i].equals(aa2[i])) flag = false;
		return flag;
	}

}
