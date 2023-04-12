import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
	static int N,M;
	static boolean inVisit[];
	static int index[];
	static ArrayList<Integer> aa= new ArrayList<Integer>();

	static void find(int count) {
		if(count>=M) {
			for(int i=0;i<index.length-1;i++) {
				
				System.out.print(index[i]+" ");
			}
			System.out.println(index[index.length-1]);
		}
		else {
			for(int i=0;i<N;i++) {
				if(!inVisit[i]) {
					inVisit[i]=true;

					index[count]=(int)aa.get(i);
					
					find(count+1);
					inVisit[i]=false;
				}
			}
		}
	}
	public static void main(String[] args) {
		Scanner in= new Scanner(System.in);

		N=in.nextInt();
		M=in.nextInt();
		inVisit=new boolean[N];
		index=new int[M];

		for(int i=1;i<N+1;i++) {
			aa.add(i);
		}
		find(0);
	}


}
