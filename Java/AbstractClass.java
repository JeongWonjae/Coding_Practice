// �߻�޼ҵ�/Ŭ������ �ʿ伺 : ���ó�� �ߺ��Ǵ� �κ��̳� �������� �κ��� �̸� �� ������� ���� ����ϰ�
//�̸� �޾� ����ϴ� �ʿ����� �ڽſ��� �ʿ��� �κи��� �������Ͽ� ��������ν� ���꼺�� ���ǰ� ���� ���� ������


public class AbstractClass {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

		
		Dog d=new Dog();
		Cat c=new Cat();
		
		d.kindOf();
		c.kindOf();
	}

}

abstract class Animal{
	abstract void kindOf();
}

class Dog extends Animal{
	
	void kindOf() {
		System.out.println("is dog");
	}
}

class Cat extends Animal{
	
	void kindOf() {
		System.out.println("is cat");
	}
}