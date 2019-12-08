/* �������̽��� ����
1. ���߻�� ����
2. ��Ը� ������Ʈ ���� �� �ϰ��ǰ� ����ȭ�� ������ ���� ǥ��ȭ�� ����
3. Ŭ������ �ۼ��� �������̽��� ������ ���ÿ� ������ �� �����Ƿ�, ���� �ð��� ����
4. Ŭ������ Ŭ���� ���� ���踦 �������̽��� �����ϸ�, Ŭ�������� �������� ���α׷����� ����
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