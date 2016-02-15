package core.tools;

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;

import core.environment.AgentEnviro;

public class AIDESimulator {

	private AgentEnviro enviro;
	private String outputFile;
	private ArrayList<String[]> resultData;
	private int runs;
	
	public AIDESimulator(AgentEnviro e, String o, int r) {
		enviro = e;
		outputFile = o;
		runs = r;
		resultData = new ArrayList<String[]>();
	}
	
	public void simulate(){
		for(int i = 0; i < runs; i++){
			enviro.run(false);
			resultData.add(enviro.getResults());
		}
		writeToFile();
	}
	
	private void writeToFile(){
		try {
			BufferedWriter bw = new BufferedWriter(new FileWriter(outputFile));
			bw.write(enviro.getClass().getName());
			bw.newLine();
			bw.write(Integer.toString(enviro.getCycleLimit()));
			bw.newLine();
			for(int j = 0; j < resultData.get(0).length; j++){	
				if(j%2 == 1){
					for(int i = 0; i < resultData.size(); i++) {
						bw.write(resultData.get(i)[j] + " ");
					}
					bw.newLine();
				}else bw.write(resultData.get(0)[j] + " ");
			}
			bw.flush();
		} catch (IOException e) {
			e.printStackTrace();}
	}

}
