package agents;

/**
 * Version 1.0
 * 
 * @author rz4
 *
 * @param <T>
 */
public class Percept<T> {

	protected T percept;
	
	public Percept(T p){
		percept = p;
	}
	
	public boolean equals(Object p){
		if(p instanceof Percept)
			return ((Percept<?>) p).percept.equals(percept);
		else return false;
	}
	
	public String toString(){
		return percept.toString();
	}
	
	public static boolean perceptsEqual(Percept[] pa1, Percept[] pa2){
		boolean flag = true;
		if(pa1.length != pa2.length) flag = false;
		for(int i = 0; i < pa1.length; i++) if(!pa1[i].equals(pa2[i])) flag = false;
		return flag;
	}
	
	public static float perceptsSimilar(Percept[] pa1, Percept[] pa2){
		float val = 0;
		if(pa1.length != pa2.length) return val;
		for(int i = 0; i < pa1.length; i++){
			if(pa1[i].equals(pa2[i])) val ++;
		}
		return val / pa1.length;
	}
	
}
