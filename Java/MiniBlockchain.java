
public class MiniBlockchain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		Block b1=new Block(1, 1, "data!!!");
		b1.getInfo();	
	}
}

class Block{
	
	private int blockID;
	private String hash;
	private String previousHash;
	private int nonce;
	private String data;
	
	public int getBlockID() {
		return blockID;
	}
	
	public void setBlockID(int blockID) {
		this.blockID=blockID;
	}
	
	public String getHash() {
		return "ishash";
	}
	
	public void setHash(String hash) {
		this.hash=hash;
	}
	
	public String getPreviousHash() {
		return previousHash;
	}
	
	public void setPrevicousHash(String previousHash) {
		this.previousHash=previousHash;
	}
	
	public int getNonce() {
		return nonce;
	}
	
	public void getNonce(int nonce) {
		this.nonce=nonce;
	}
	
	public String getData() {
		return data;
	}
	
	public void setData() {
		this.data=data;
	}
	
	public Block(int blockID, int nonce, String data) {
		this.blockID=blockID;
		this.nonce=nonce;
		this.data=data;
	}
	
	public void getInfo() {
		System.out.println("--------------------"); 
		System.out.println("id -> "+getBlockID());
		System.out.println("nonce -> "+getNonce());
		System.out.println("data -> "+getData());

	}
}