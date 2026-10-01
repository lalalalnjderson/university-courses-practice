package class_04;

// if thread sleeps/waits and you interrupt() -> InterruptedException is thrown immediately
// if running normally -> you must check 
 
public class InterruptedExample {
    public static void main(String[] args){
        Thread t1 = new Thread(() -> {
            for (int i=0; i<10_000; i++){
                // check 
                if (Thread.currentThread().isInterrupted()){
                    System.out.println("t1 was interrupted at i=" + i);
                    return;
                }
                System.out.println("hello" + i);
            }
        });
        Thread t2 = new Thread(() -> {
            try{
                for (int i=0; i<10_000; i++){
                    System.out.println("world " + i);
                    Thread.sleep(1);
                }
            }
            catch (InterruptedException e){
                System.out.println("t2 was interrupted during sleep");
            }
        });

        t1.start();
        t2.start();

        // let threads run for 1 sec, then interrupt
        try{
            Thread.sleep(1000); // sleep - just a static method of Thread
        }
        catch (InterruptedException e){
            //
        }

        t1.interrupt();
        t2.interrupt();
        System.out.println("both interrupted");
    }
}