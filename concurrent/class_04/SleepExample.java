package class_04;

public class SleepExample{
    public static void main(String[] args){
        Thread t1 = new Thread(() -> {
            for (int i=0; i<200; i++){
                System.out.println("hello " + i);
                try{
                    Thread.sleep(5);
                }
                catch(InterruptedException e){
                    //
                }
            }
        });
        Thread t2 = new Thread(() -> {
            for (int i=0; i<200; i++){
                System.out.println("world" + i);
                try {
                    Thread.sleep(5);
                }
                catch (InterruptedException e){
                    //
                }
            }
        });

        t1.start();
        t2.start();

        try{
            t1.join();
            t2.join();
        }
        catch (InterruptedException e){
            //
        }
        System.out.println("ready");
    }
}