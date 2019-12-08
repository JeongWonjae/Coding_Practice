
public class Inheritance {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
	    Calculator c1=new Calculator(10, 20);
	    c1.sum();
	    
	    SubCalculator subc1=new SubCalculator(20, 30);
	    subc1.substract();
	    
	    MultipleCalculator mc1=new MultipleCalculator(1356, 5329);
	    mc1.sum();
	    mc1.substract();
	    mc1.multiple();
	}
}

class Calculator{

	  int left;
	  int right;

	  Calculator() {}

	  public Calculator(int left, int right){
	    this.left=left;
	    this.right=right;
	  }

	  public void sum(){
		
	    System.out.println(this.left+this.right);
	  }

	}

class SubCalculator extends Calculator{
	
	public SubCalculator () {
		
	}
	
	public SubCalculator(int left, int right){
		this.left=left;
		this.right=right;
	}
	
	public void substract() {
		int compare;
		if(this.right>this.left) {
			compare=this.left;
			this.left=this.right;
			this.right=compare;
		}
		System.out.println(this.left-this.right);
	}
}

class MultipleCalculator extends SubCalculator{
	
	
	MultipleCalculator(int left, int right) {
		this.left=left;
		this.right=right;
		//or super(left, right);
	}

	public void multiple() {
		System.out.println(left*right);
	}
	
}
