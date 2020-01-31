package control;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {

	public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		Scanner sc=new Scanner(System.in);
		ArrayList<String> filesList=new ArrayList<String>();
	
		Controller start=new Controller();
		System.out.print("(+) Input directory name to rename files  : ");
		String path=sc.next();
		System.out.print("(+) Input your password  : ");
		String password=sc.next();
		start.getKey(password);
		filesList=start.getFilesName(path);
		System.out.print("(+) Select type (en/de)  : ");
		String type=sc.next();
		System.out.print("(+) Do you want to proceed? : ");
		String check=sc.next();
		
		if(check.contains("y") || check.contains("Y"))
		{
			if(type.equals("en") || type.equals("EN"))
			{
				for(String element:filesList)
				{
					start.encryptFileName(path, element);
				}
				System.out.println("(x) Completed revise.");
			}else if(type.equals("de") || type.equals("DE"))
			{
				for(String element:filesList)
				{
					start.decryptFileName(path, element);
					System.out.println("(x) Completed revise.");
				}
			}
		}else if(check.contains("n") || check.contains("N"))
		{
			System.out.println("(x) Program exit. ");
			System.exit(0);
		}
		
	}
}
