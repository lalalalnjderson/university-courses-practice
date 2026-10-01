package class_03;

// ThreadGroup: a way to organize threads into logical groups
// Useful for monitoring — you can ask "how many threads are still running?"

public class ThreadNaming{
    public static void main(String[] args){
        ThreadGroup group = new ThreadGroup("MyWorkers");

        // Thread(ThreadGroup, Runnable, name)
        Thread t1 = new Thread(group, () -> {
            for (int i=0; i<100; i++){
                System.out.println(Thread.currentThread().getName() + ": hello");
            }
        }, "HelloThread");

        Thread t2 = new Thread(group, () -> {
            for (int i=0; i<100; i++){
                System.out.println(Thread.currentThread().getName() + ": world");
            }
        }, "WorldThread");

        t1.start();
        t2.start();

        t1.setName("HelloThread2");


        // activeCount(): how many threads in this group are still alive
        // group.list(): prints all threads in the group to System.out (for debugging)
        // we check each 100ms while threads are running

        while (group.activeCount() > 0){
            System.out.println("---- Active threads: " + group.activeCount() + "-----");
            group.list();
            try{
                Thread.sleep(100); // wait 100ms between checks 
            } 
            catch(InterruptedException e){
                //
            }
        }
        System.out.println("All threads finished");
    }
}