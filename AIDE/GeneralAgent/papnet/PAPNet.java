package papnet;

import java.util.ArrayList;

import core.agent.Action;
import core.agent.Goal;
import core.agent.Percept;

public class PAPNet {
	
	private ArrayList<PAPNode> nodes;
	private ArrayList<PAPRoute> routes;
	private PAPNode currentNode;

	public PAPNet(){
		nodes = new ArrayList<PAPNode>();
		routes = new ArrayList<PAPRoute>();
	}
	
	public void updateNet(Percept[] percept, Goal g, Action action){
		PAPNode n = getNode(percept);
		if(n == null){
			n = new PAPNode(percept, g.similarPercepts(percept));
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
	
	public void normalizeNet(){
		
	}
	
	public PAPNode getNode(Percept[] pa){
		for(PAPNode n : nodes){
			if(Percept.perceptsEqual(n.getPercepts(), pa)) return n;
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
	
	public ArrayList<PAPRoute> findRoutes(PAPNode parent, PAPNode child){
		ArrayList<PAPRoute> rts = new ArrayList<PAPRoute>();
		
		return rts;
	}
	
	public ArrayList<PAPNode> getNodes(){
		return nodes;
	}
	
	public ArrayList<PAPRoute> getRoutes(){
		return routes;
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