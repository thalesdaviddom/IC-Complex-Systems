import edu.princeton.cs.algs4.In;

public class Network {
	private int[][] linklist;
	private int size;
public Network(int size, int[][] linklist){
	this.size = size;
	this.linklist = linklist;
	
}

public int[][] BuildAdMatrix(){
	int[][] AdMatrix = new int[this.size][this.size];
	for(int i =0; i<this.linklist.length; i++){
		AdMatrix[this.linklist[i][0]][this.linklist[i][1]] = 1;
	} 
	return AdMatrix;
}

public void print(){
	int[][] M = this.BuildAdMatrix();
	for(int i = 0; i < this.size; i++){
		for(int j = 0; j < this.size; j++){
			System.out.print(M[i][j]);
		}
		System.out.println();
	}

}

public static void print(int size, int[][] linklist){
	Network a = new Network(size,linklist);
	a.print();
}

public static void main(String[] args){
	In stream = new In();
	int N = stream.readInt();
	int L = stream.readInt();
	int[][] linklist  = new int[L*2][2]; int i =0;
	while(!stream.isEmpty()){
		int a = stream.readInt();
		int b = stream.readInt();
		linklist[i][0] = a; linklist[i][1] = b; i++;
		System.out.print(i);
	}	

	print(N,linklist);
	
}

}
