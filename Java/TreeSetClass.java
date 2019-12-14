import java.util.Iterator;
import java.util.TreeSet;

public class TreeSetClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		TreeSet<Integer> ts1=new TreeSet<Integer>();
		
		ts1.add(2);
		ts1.add(5);
		ts1.add(1);
		ts1.add(4);
		ts1.add(3);
		ts1.add(7);
		
		for(int e:ts1) {
			System.out.print(e+" | ");
		}
		System.out.println();
		
		System.out.print(ts1.add(2)); //not allow duplication
		
		ts1.remove(2);
		Iterator<Integer> iter=ts1.iterator();
		while(iter.hasNext()){
			System.out.print(iter.next());
		}
		
		System.out.println("Binary Search Tree count  : "+ts1.size());
		
		//print sub set
		System.out.println(ts1.subSet(1, 5));
		System.out.println(ts1.subSet(5, 8));
		
		//string
		TreeSet<String> ts2=new TreeSet<String>();
		ts2.add("A");
		ts2.add("C");
		ts2.add("F");
		ts2.add("d");
		ts2.add("B");
		ts2.add("c");
		
		for(String s:ts2) {
			System.out.print(s+" | ");
		}
		
		
	}

}
