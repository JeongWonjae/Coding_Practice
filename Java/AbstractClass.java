// 추상메소드/클래스의 필요성 : 모듈처럼 중복되는 부분이나 공통적인 부분은 미리 다 만들어진 것을 사용하고
//이를 받아 사용하는 쪽에서는 자신에게 필요한 부분만을 재정의하여 사용함으로써 생산성이 향상되고 배포 등이 쉬워짐


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