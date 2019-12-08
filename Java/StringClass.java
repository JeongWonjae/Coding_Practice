
public class StringClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		charAtMethod charAtV=new charAtMethod(); //return string of certain index
		charAtV.test();
		
		compareToMethod compareToV=new compareToMethod();
		compareToV.test();
		
		indexOfMethod indexOfV=new indexOfMethod();
		indexOfV.test();
		
		trimMethod trimV=new trimMethod();
		trimV.test();
	}

}

class charAtMethod{
	public void test() {
		String str=new String("Hello world!"); //immutable object
		for(int i=0;i<str.length();i++) {
			System.out.print(str.charAt(i)+" ");
		}
		System.out.println();
	}
}

class compareToMethod{
	public void test() {
		String str=new String("Hello world!");
		System.out.print("Original String : " + str);
		if(str.compareTo("Hello world!")==0) { // <<compare string
			System.out.println("\nString is match!"); //return 0
		}
	}
}

class indexOfMethod{
	public void test() {
		String str=new String("Hello world!");
		System.out.println(str.indexOf("!")); //return index
	}
}

class trimMethod{
	public void test() {
		String str=new String("H e l l o w o r l d !              ");
		System.out.println(str.trim()+"<-exist blank?"); //delete blank
	}
}


