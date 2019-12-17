import java.io.IOException;

public class ExceptionClass {
	
	//method exception using 'throws'
	static void handlingException() throws Exception {
		throw new Exception();
	}

	public static void main(String[] args){
		// TODO Auto-generated method stub
		
		byte[] list= {'a', 'b', 'c'};
		try {
			System.out.write(list);
			System.out.println();
		} catch(IOException e) {
			e.printStackTrace();
		} catch(Exception e) { //contain IOException
			e.printStackTrace();
		}
		
		/* USE '|'
		try {
			//
		} catch(IOException | SQLException e) {
			e.printStackTrace();
		}
		*/
	
		try {
			System.out.println(1/0);
		} catch (ArithmeticException e) {
			System.out.println("occured exception : "+e.toString());
			System.out.println("occured exception : "+e.getMessage());
		}
		
		try {
			handlingException();
		} catch(Exception e) {
			System.out.println("main() method was occured excption!");
		}
		
	}
}
