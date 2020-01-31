package control;

import java.io.File;
import java.util.ArrayList;
import java.util.Base64;
import java.util.Base64.Decoder;
import java.util.Base64.Encoder;

import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class Controller {
	private String key;
	
	public void encryptFileName(String path, String fileName) throws Exception {
		
		XFile getFile=new XFile(path+fileName);
		String newName=encrypt(fileName);
		
		if(!getFile.exists())
		{
			System.out.println("(!) Not exist this file. Program exit. ");
			System.exit(0);
		}
		if(getFile.renameTo(new XFile(path+newName))==true)
		{
			System.out.println("(+) Encrypted file name ["+fileName+"] > ["+newName+"]");
		}else if(getFile.renameTo(new XFile(path+newName))==false)
		{
			System.out.println("(!) ["+fileName+"] Encrypt failed. ");
		}
	}
	
	public void decryptFileName(String path, String fileName) throws Exception {
		
		XFile getFile=new XFile(path+fileName);
		String recoverName=decrypt(fileName);
		
		if(!getFile.exists())
		{
			System.out.println("(!) Not exist this file. Program exit. ");
			System.exit(0);
		}
		if(getFile.renameTo(new XFile(path+recoverName))==true)
		{
			System.out.println("(+) Decrypted file name ["+fileName+"] > ["+recoverName+"]");
		}else if(getFile.renameTo(new XFile(path+recoverName))==false)
		{
			System.out.println("(!) ["+recoverName+"] Decrypt failed. ");
		}
	}
	
	public ArrayList<String> getFilesName(String path){
		ArrayList<String> fileList=new ArrayList<String>();
		File getDic=new File(path);
		
		if(!getDic.exists())
		{
			System.out.println("(!) Not exist this directory. Program exit. ");
			System.exit(0);
		}
		File[] list=getDic.listFiles();
		for(File f:list)
		{
			fileList.add(f.getName());
		}
		
		return fileList;
	}
	
	public void getKey(String password) {
		String key=password;
		this.key=key;
	}
	
	public String encrypt(String fileName) throws Exception{
		Cipher cipher=Cipher.getInstance("AES/CBC/PKCS5Padding");
		byte[] keyBytes=new byte[16]; //{"0x??", "0x??",  ... "0x??"}
		byte[] b=key.getBytes("UTF-8");
		int len=b.length;
		if(len>keyBytes.length)
		{
			len=keyBytes.length;
		}
		//copy from b to keyBytes by b.length
		System.arraycopy(b, 0, keyBytes, 0, len);
		SecretKeySpec keySpec=new SecretKeySpec(keyBytes, "AES");
		IvParameterSpec ivSpec=new IvParameterSpec(keyBytes);
		cipher.init(Cipher.ENCRYPT_MODE, keySpec, ivSpec);
		byte[] encrypted=cipher.doFinal(fileName.getBytes("UTF-8"));
		Encoder encoder=Base64.getMimeEncoder();
		return new String(encoder.encode(encrypted), "UTF-8");
	}
	
	public String decrypt(String fileName) throws Exception, IllegalArgumentException{
		Cipher cipher=Cipher.getInstance("AES/CBC/PKCS5Padding");
		byte[] keyBytes=new byte[16]; //{"0x??", "0x??",  ... "0x??"}
		byte[] b=key.getBytes("UTF-8");
		int len=b.length;
		if(len>keyBytes.length)
		{
			len=keyBytes.length;
		}
		//copy from b to keyBytes by b.length
		System.arraycopy(b, 0, keyBytes, 0, len); 
		SecretKeySpec keySpec=new SecretKeySpec(keyBytes, "AES");
		IvParameterSpec ivSpec=new IvParameterSpec(keyBytes);
		cipher.init(Cipher.DECRYPT_MODE, keySpec, ivSpec);
		Decoder decoder=Base64.getMimeDecoder();
		byte[] decrypted=cipher.doFinal(decoder.decode(fileName));
		return new String(decrypted, "UTF-8");
	}
}

class XFile extends File{
	
	XFile(String filePath) {
		super(filePath);
	}
	
	public boolean renameTo(File pNewFile) {
		  for (int i = 0; i < 20; i++) 
		  {
			   if (super.renameTo(pNewFile)) 
			   {
				   return true;
			   }
			   System.gc(); 
			   try
			   {
				   Thread.sleep(50);
			   }catch(InterruptedException ie)
			   {
				   ie.printStackTrace();
			   }
		  }
		  return false;
	 }
}
