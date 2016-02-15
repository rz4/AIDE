package core.agent;

/**
 * Version 1.0
 * 
 * Class creates a Percept object used to
 * express and describe input information being
 * passed from the Environment to the Agent.
 * 
 * All Percepts should be initialized with a 
 * unique identifier.
 * 
 * @author rz4
 *
 * @param <T>
 */
public class Percept<T> {

	protected T per_id;
	
	/**
	 * Method constructs Percept with generic 
	 * identifier.
	 * 
	 * @param p
	 */
	public Percept(T p){
		per_id = p;
	}
	
	/**
	 * Method returns whether two Percepts are equal.
	 * 
	 */
	public boolean equals(Object p){
		if(p instanceof Percept)
			return ((Percept<?>) p).per_id.equals(per_id);
		else return false;
	}
	
	public String toString(){
		return per_id.toString();
	}
	
	/**
	 * Static Method returns whether two Percept[]s are equal.
	 * 
	 * @param pa1
	 * @param pa2
	 * @return
	 */
	public static boolean perceptsEqual(Percept[] pa1, Percept[] pa2){
		boolean flag = true;
		if(pa1.length != pa2.length) flag = false;
		for(int i = 0; i < pa1.length; i++) if(!pa1[i].equals(pa2[i])) flag = false;
		return flag;
	}
	
	/**
	 * Static Method returns a float value between 0.0 and 1.0 depending on
	 * how the fraction of Percepts that are equal between the two Percept[]s.
	 * 
	 * @param pa1
	 * @param pa2
	 * @return
	 */
	public static float perceptsSimilar(Percept[] pa1, Percept[] pa2){
		float val = 0;
		if(pa1.length != pa2.length) return val;
		for(int i = 0; i < pa1.length; i++){
			if(pa1[i].equals(pa2[i])) val ++;
		}
		return val / pa1.length;
	}
	
}
