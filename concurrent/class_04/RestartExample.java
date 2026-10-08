package class_04;

public class RestartExample{
    public static void main(String[] args){
        Thread t1 = new Thread(() -> {
            for (int i=0; i < 10_000; i++){
                if (Thread.currentThread().isInterrupted()){
                    System.out.println("Interrupted, stopping");
                    return;
                }
                System.out.println("working " + i);
            }
        });

        t1.start();

        try{
            Thread.sleep(50);
        }
        catch (InterruptedException e){
            //   
        }

        t1.interrupt();;

        try {
            t1.join(); // wait for it to actually finish
        }
        catch (InterruptedException e){
            //
        }

        // try to restart the same thread -> IllegalThreadStateException
        // thread can be started only once
        try{
            t1.start();
        }
        catch (IllegalThreadStateException e){
            System.out.println("Cannot restart! " + e.getMessage());
        }
    }
}