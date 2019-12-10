import java.util.ArrayList;

public class Generic {

	public static void main(String[] args) {
		// TODO Auto-generated method stub

			BrandList<KoreaBrand> koreaBrand=new BrandList<>();
			koreaBrand.add(new Samsung());
			koreaBrand.add(new Lifeisgood());
			
			for(int i=0;i<koreaBrand.size();i++) {
				koreaBrand.get(i).name();
			}
	}
}

abstract class KoreaBrand{ abstract void name();}
class Samsung extends KoreaBrand{ void name() {System.out.println("is sumsung");}}
class Lifeisgood extends KoreaBrand{ void name() {System.out.println("is LG");}}

class BrandList<T>{
	ArrayList<T> br=new ArrayList<T>();
	
	void add(T brand) {
		br.add(brand);
	}
	T get(int index) {
		return br.get(index);
	}
	boolean remove(T brand) {
		return br.remove(brand);
	}
	int size() {
		return br.size();
	}
}