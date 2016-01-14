package papnet;

import java.util.ArrayList;

public class PAPNet {
	
	private ArrayList<PAPNode> nodes;
	private ArrayList<PAPRoute> routes;
	private PAPNode currentNode;

	public PAPNet(){
		nodes = new ArrayList<PAPNode>();
		routes = new ArrayList<PAPRoute>();
	}
	
	public void updateNet(String[] percept, String[] goal, String action){
		PAPNode n = getNode(percept);
		if(n == null){
			n = new PAPNode(percept, perceptSimilar(percept, goal));
			nodes.add(n);
		}else n.incrVisits();
		
		if(currentNode != null && action != null){
			PAPRoute r = getRoute(currentNode, n);
			if(r == null){
				r = new PAPRoute(action, currentNode, n);
				routes.add(r);
			}else r.incrVisits();
		}
		
		currentNode = n;
	}
	
	public PAPNode getNode(String[] percept){
		for(PAPNode n : nodes){
			if(perceptSame(n.getPercept(), percept)) return n;
		}
		return null;
	}
	
	public PAPRoute getRoute(PAPNode parent, PAPNode child){
		for(PAPRoute r: routes){
			if(r.getParent() == parent && r.getChild() == child)
				return r;
		}
		return null;
	}
	
	public static boolean perceptSame(String[] percept1, String[] percept2){
		boolean flag = true;
		for(int i = 0; i < percept1.length; i++){
			if(!percept1[i].equals(percept2[i])) flag = false;
		}
		return flag;
	}
	
	public static float perceptSimilar(String[] percept1, String[] percept2){
		float val = 0;
		for(int i = 0; i < percept1.length; i++){
			if(percept1[i].equals(percept2[i])) val ++;
		}
		return val / percept1.length;
	}
	
	public String toString(){
		String s = "Net:\n";
		s += "\tNodes:\n";
		for(PAPNode n : nodes){
			s += "\t\t" + n + "\n";
		}
		s += "\tRoutes:\n";
		for(PAPRoute r : routes){
			s += "\t\t" + r + "\n";
		}
		return s;
	}

}
