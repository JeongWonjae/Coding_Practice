
public class MethodOverriding {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Calculator2 c1=new Calculator2(10, 20);
		c1.sum();
		
		SubCalculator2 c2=new SubCalculator2(10, 20);
		c2.sum();
		
	}

}

class Calculator2{
	int left; int right;
	
	Calculator2(){}
	Calculator2(int left, int right){
		this.left=left;
		this.right=right;
	}
	
	public void sum() {
		System.out.println(left+right);
	}
}

class SubCalculator2 extends Calculator2{
	
	SubCalculator2(int left, int right){
		super(left, right);
	}

	public void sum() {
		System.out.println(left+right+10);
	}
	
}