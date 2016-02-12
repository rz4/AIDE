package agents;

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
	
	public static boolean perceptsEquals(Percept[] pa1, Percept[] pa2){
		boolean flag = true;
		if(pa1.length != pa2.length) flag = false;
		for(int i = 0; i < pa1.length; i++) if(!pa1[i].equals(pa2[i])) flag = false;
		return flag;
	}
	
	public String toString(){
		return percept.toString();
	}
}
