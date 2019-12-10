import java.util.Arrays;

public class ArraysClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		binarySearchMethod b1=new binarySearchMethod();
		b1.test();
		copyOfMethod c1=new copyOfMethod();
		c1.test();
		fillANDsordMethod f1=new fillANDsordMethod();
		System.out.println();
		f1.fillM();
		System.out.println();
		f1.sortM();
	}

}


class binarySearchMethod{
	
	void test() {
		int[] arr = new int[1000];
		for(int i=0;i<arr.length;i++) {
			arr[i]=i+10;
		}
		System.out.println(Arrays.binarySearch(arr, 12)); //return index
	}
}

class copyOfMethod{
	
	void test() {
		int[] arr1= {1,2,3,4,5};
		int[] arr2=Arrays.copyOf(arr1, 2);
		
		for(int i=0;i<arr2.length;i++) {
			System.out.print(arr2[i]+" ");
		}
		
		System.out.println();
		
		int[] arr3=Arrays.copyOfRange(arr1, 2, 5);
		for(int i=0;i<arr3.length;i++) {
			System.out.print(arr3[i]+" ");
		}
	}
}

class fillANDsordMethod {
	
	void fillM() {
		int[] arr=new int[10];
		Arrays.fill(arr, 10);
		for(int i=0;i<arr.length;i++) {
			System.out.print(arr[i]+" ");
		}
	}
	
	void sortM() {
		int [] arr= {7,3,7,2,5};
		Arrays.sort(arr);
		for(int i=0;i<arr.length;i++) {
			System.out.print(arr[i]+" ");
		}
	}
}