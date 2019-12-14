import java.util.HashSet;
import java.util.Iterator;

public class HashSetClass {
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		HashSet<String> hs1=new HashSet<String>();
		HashSet<String> hs2=new HashSet<String>();
		
		hs1.add("wonjae");
		hs1.add("sangbin");
		System.out.println(hs1.add("picachu"));
		System.out.println(hs1.add("picachu")); //duplicate store -> return f
		
		for(String e : hs1) {
			System.out.print(e + "|");
		}
		
		System.out.println();
		
		hs2.add("CAT");
		hs2.add("DOG");
		hs2.add("BIRD");
		hs2.add("TIGER");
		
		Iterator<String> iter1=hs2.iterator();
		while(iter1.hasNext()) {
			System.out.print(iter1.next()+"|");
		}
		System.out.println();
		System.out.println("size of hs2 : "+hs2.size());
		
		//override hashCode(), equals()
		HashSet<Games> hs3=new HashSet<Games>();
		hs3.add(new Games("FPS", "SuddenAttack"));
		hs3.add(new Games("RPG", "Maplestory"));
		hs3.add(new Games("FPS", "SuddenAttack"));
		
		System.out.println();
		for(Games e : hs3) {
			System.out.print(e.name+"|");
		}
		System.out.println(hs3.size());
	}
}

//override hashCode(), equals()
//for allow duplication

class Games{
	String species;
	String name;
	
	Games(String species, String name){
		this.species=species;
		this.name=name;
	}

	public int hashCode() {
		return (species+name).hashCode();
	}
	
	public boolean equels(Object obj) {
		if(obj instanceof Games) {
			Games tmp=(Games)obj;
			return species.equals(tmp.species) && name.equals(tmp.name);
			//additionally, compare with species
		} else {
			return false;
		}
	  }
}

