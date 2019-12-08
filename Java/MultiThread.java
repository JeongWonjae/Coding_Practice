
public class MultiThread {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Thread t1=new Thread(new ThreadInterfaceRunnable2());
		t1.start();
		System.out.println(t1.getThreadGroup());
		
		ThreadGroup g1=new ThreadGroup("IsThread");
		g1.setMaxPriority(7);
		
		Thread t2=new Thread(g1, new ThreadInterfaceRunnable2());
		t2.start();
		System.out.println(t2.getThreadGroup());
		
		Thread t3=new Thread(g1, new ThreadInterfaceRunnable2());
		t3.start();
		System.out.println(t3.getThreadGroup());
	}

}

class ThreadInterfaceRunnable2 implements Runnable{
	public void run() {
		try {
            Thread.sleep(10);
        } catch (InterruptedException e) {
        	e.printStackTrace();
        }
	}
}