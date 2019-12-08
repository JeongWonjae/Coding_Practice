/* 인터페이스의 장점
1. 다중상속 가능
2. 대규모 프로젝트 개발 시 일관되고 정형화된 개발을 위한 표준화가 가능
3. 클래스의 작성과 인터페이스의 구현을 동시에 진행할 수 있으므로, 개발 시간을 단축
4. 클래스와 클래스 간의 관계를 인터페이스로 연결하면, 클래스마다 독립적인 프로그래밍이 가능
 */


public class Interface {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Desktop d=new Desktop();
		Laptop l=new Laptop();
		
		d.powerOn(); d.kindOf();
		l.powerOn(); l.kindOf();
	}

}

interface Computer{
	
	public abstract void powerOn();
	
}

interface Game{
	
	public abstract void kindOf();
}

class Desktop implements Computer, Game{
	
	public void powerOn() {
		System.out.println("Desktop Power On.");
	}
	
	public void kindOf() {
		System.out.println("Play Starcarft!");
		
	}
	
}

class Laptop implements Computer, Game{
	
	public void powerOn() {
		System.out.println("Laptop Power On.");
	}
	
	public void kindOf() {
		System.out.println("Play FIFA!");
	}
}