
public class EnumClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		EnumerationType e1=new EnumerationType();
		e1.valuesMethod();
		e1.valueOfMethod();
		e1.oridinalMethod();

	}

}

class EnumerationType{
	enum rainbow{
		RED(3), ORANGE(10), YELLOW(21), GREEN(5), BLUE(1);
		
		private final int value;
		rainbow(int value){this.value=value;}
		public int getValue() {return value;}
	}
	
	void valuesMethod(){
		rainbow[] arr=rainbow.values();
		for(rainbow rb:arr) {
			System.out.println(rb);
		}
	}
	
	void valueOfMethod() {
		rainbow rb=rainbow.valueOf("YELLOW");
		System.out.println(rb);
	}
	
	void oridinalMethod() {
		int idx=rainbow.YELLOW.ordinal(); //index number
		System.out.println(idx);
		System.out.println(rainbow.YELLOW.getValue()); //stored number
		
	}
}