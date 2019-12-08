
class Calculator{
  static int thisIsClassMember=10;
  int left; int right;

  public void setOprands(int left, int right){
    this.left=left;
    this.right=right;
  }

  public Calculator(int left, int right){
    this.left=left;
    this.right=right;
  }

  public void sum(){
    System.out.println(this.left+this.right);
  }

  public void avg(){
    System.out.println((this.left+this.right)/2);
  }

  void printClassMember(){
    int left=9;
    System.out.println(this.left);
  }

  //not work, ClassInstance.java:21: error: non-static variable left cannot be referenced from a static context
  /*static void static_printInstance(){
    System.out.println(left);
  }*/

}

public class ClassInstance {

  public static void main(String[] args) {

    /*
    //Calculator c1=new Calculator();
    //c1.setOprands(10,20);
    //c1.sum();
    //c1.avg();

    Calculator c2=new Calculator();
    c2.setOprands(20,40);
    //c2.sum();
    //c2.avg(); //using instance

    Calculator.thisIsClassMember=7; //using class
    //System.out.println(Calculator.thisIsClassMember);

    Calculator c3=new Calculator();
    c3.setOprands(90,100);
    c3.printClassMember();
    */

    Calculator c4=new Calculator(40, 50);
    c4.printClassMember();
  }
}
