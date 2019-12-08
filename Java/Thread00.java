
public class Thread00 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Thread t1=new Thread(new ThreadInterfaceRunnable());
		ThreadInheritanceClass t2=new ThreadInheritanceClass();
		
		t2.setPriority(2);
		
		t1.start();
		t2.start();
		
		System.out.println(t1.getPriority());
		System.out.println(t2.getPriority());
		
	}

}

class ThreadInheritanceClass extends Thread{
	public void run() {
		for(int start=0;start<5;start++) {
			System.out.println(getName()+ "= " +start+" thread class thread");
			try {
				Thread.sleep(1500);
			} catch(InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}

class ThreadInterfaceRunnable implements Runnable{
	
	public void run() {
		for(int start=0;start<5;start++) {
			System.out.println(Thread.currentThread().getName() + "= " + start+" runnable thread");
			try {
				Thread.sleep(1500);
			} catch(InterruptedException e) {
				e.printStackTrace();
			}
		}
	}
}