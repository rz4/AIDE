package agents;

/**
 * Version 1.0
 * 
 * @author rz4
 *
 * @param <T>
 */
public class Action<T> {

	protected T action;
	
	public Action(T a) {
		action = a;
	}
	
	public boolean equals(Object a){
		if(a instanceof Action)
			return ((Action<?>)a).action.equals(action);
		else return false;
	}
	
	public String toString(){
		return action.toString();
	}

}
