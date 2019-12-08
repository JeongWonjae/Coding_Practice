
public class ObjectClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Hobby h=new Hobby();
		Hobby h2=new Hobby();
		
		System.out.println("toString Method >>> "+ h.toString());
		System.out.println("equlas Method >>> "+ h.equals(h2));
	}
}

class Hobby{
	void makeMusic() {
		System.out.println("I enjoy to make music using FLStudio program.");
	}
}