
class Calculator{

  int left;
  int right;

  Calcualter() {}

  public Calculator(int left, int right){
    this.left=left;
    this.right=right;
  }

  public void sum(){
    System.out.println(this.left+this.right);
  }

}

class SubCalculator extends Calculator{

}

public class Inheritance {

  public static void main(String[] args) {

    Calculator c1=new Calculator(10, 20);
  }
}
