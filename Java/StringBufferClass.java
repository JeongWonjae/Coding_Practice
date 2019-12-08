
public class StringBufferClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		appendM appendV=new appendM();
		appendV.test();
		
		capacityM capacityV=new capacityM();
		capacityV.test();
		
		insertANDdeleteM insertANDdeleteV=new insertANDdeleteM();
		insertANDdeleteV.test();
	}

}


class appendM{
	public void test() {
		StringBuffer str=new StringBuffer("Hello ");
		System.out.println(str.append("World!"));
	}
}

class capacityM{
	public void test() {
		StringBuffer org=new StringBuffer(); //default length is 16
		System.out.println(org.capacity());
		StringBuffer str=new StringBuffer("Hello World!");
		System.out.println(str.capacity());
	}
}

class insertANDdeleteM{
	public void test() {
		StringBuffer str=new StringBuffer("Hello World!"); //default length is 16
		System.out.println(str.insert(2, "insertword!!!!"));
		System.out.println(str.delete(0, 1));
	}
}