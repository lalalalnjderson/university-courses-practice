package class_04;

public class JoinExample{
    public static void main(String[] args){
        Thread t1 = new Thread(() -> {
            for (int i=0; i<1_000; i++){
                System.out.println("hello");
            }
        });
        Thread t2 = new Thread(() -> {
            for (int i=0; i<1_000; i++){
                 System.out.println("world");
            }
        });
        t1.start();
        t2.start();

        // Wait for BOTH threads to finish before printing "ready"
        // main thread waits for t1, then checks t2
        // "hello" and "world" still interleaved
        try {
            t1.join();
            t2.join();
        }
        catch (InterruptedException e){ // "checked exception"
            //
        }
        
        System.out.println("ready");
    }
}