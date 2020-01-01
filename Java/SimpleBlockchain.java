import java.util.ArrayList;
import java.util.Date;

public class Block {
	
	private static int BlockID=0;
	private static String previousHash="First block!";
	private String hash;
	private String data;
	private long timeStamp;
	
	public Block() {
		
	}
	
	public String getHash() {
		return hash;
	}
	
	public String getData() {
		return data;
	}
	
	public long getTimeStamp() {
		return timeStamp;
	}
	
	public void increaseBlockID() {
		BlockID+=1;
	}
	
	public Block(String data) {
		increaseBlockID();
		this.data=data;
		this.hash=makeHashData(data);
		this.timeStamp=new Date().getTime();
	}
	
	public String makeHashData(String data) {
		String hash;
		hash="This is temporary hash data : "+data+ " ID="+BlockID+ "<"+previousHash+">";
		previousHash=hash;
		return hash;
	}

	public static void main(String[] args) throws InterruptedException {
		// TODO Auto-generated method stub
	
		ArrayList<Block> blockChain1=new ArrayList<Block>();
		
		Block b1=new Block("[first block]");
		blockChain1.add(b1);
		
		Thread.sleep(1000);
		
		Block b2=new Block("[second block]");
		blockChain1.add(b2);
		
		Block b3=new Block("[third block]");
		blockChain1.add(b3);
		
		Block b4=new Block("wonjae wonjae");
		blockChain1.add(b4);
		
		for(Block b : blockChain1) {
			System.out.println("["+b.timeStamp+" | "+b.data+" | "+b.hash+"]");
		}
	}
}
