package algorithm;

public class SelectionSort {
	public void sort(int[] data) {
		int size=data.length;
		int min;
		int res;
		
		for(int i=0; i<size-1; i++) {
			min=i;
			for(int j=i+1; j<size; j++) {
				if(data[min]>data[j]) {
					min=j;
				}
			}
			res=data[min];
			data[min]=data[i];//switch
			data[i]=res;
		}
	}
	public void main(String[] args) {
		SelectionSort selsort=new SelectionSort();
		int data[]= {40,55,47,52,49,60};
		selsort.sort(data);
		for(int i=0; i<data.length; i++) {
			System.out.println("data["+i+"] ดย"+data[i]);
		}
		
	}
}