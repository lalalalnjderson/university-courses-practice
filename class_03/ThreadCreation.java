package class_03;

class MyThread extends Thread{
    private String message;
    private int count;

    MyThread(String message, int count){
        this.message = message;
        this.count = count;
    }

    @Override
    public void run(){
        for (int i=0; i<count; i++){
            System.out.println(message);
        }
    }
}

// MyRunnable can implement several interfaces
// but MyThread can only extend thread

class MyRunnable implements Runnable{
    private String message;
    private int count;

    MyRunnable(String message, int count){
        this.message = message;
        this.count = count;
    }

    @Override
    public void run(){
        for (int i=0; i<count; i++){
            System.out.println(message);
        }
    }
}

public class ThreadCreation{
    public static void main(String[] args){
        int count = 1_000;

        // 1 option: extending Thread
        Thread w1a = new MyThread("Hello", count);
        Thread w1b = new MyThread("world", count);
        w1a.start();
        w1b.start();

        // 2 option: with Runnable
        System.out.println("=== Way 2: Runnable interface ===");
        Thread w2a = new Thread(new MyRunnable("hello", count));
        Thread w2b = new Thread(new MyRunnable("world", count));
        w2a.start();
        w2b.start();

        // 3 option: anonymous class derived from Thread | new Thread(){ ... }
        // so you create nameless subclass of Thread
        String msg3a = "hello"; // must be effectively final 
        String msg3b = "world";
        Thread w3a = new Thread(){
            @Override 
            public void run(){
                for (int i=0; i<count; i++){
                    System.out.println(msg3b);
                }
            }
        };
        Thread w3b = new Thread(){
            @Override
            public void run(){
                for (int i=0; i<count; i++){
                    System.out.println(msg3b);
                }
            }
        };
        w3a.start();
        w3b.start();

        // 4 option: anonymous class derived from Runnable 
        // effectively final rule applied IF word is passed directly - not via constructor
        Runnable r4a = new Runnable(){
            @Override
            public void run(){
                for (int i=0; i<count; i++){
                    System.out.println("hello");
                }
            }
        };
        Runnable r4b = new Runnable(){
            @Override
            public void run(){
                for (int i=0; i<count; i++){
                    System.out.println("hello");
                }
            }
        };
        new Thread(r4a).start();
        new Thread(r4b).start();

        // 5 option: Lambda
        // you pass Runnable to Thread constructor 
        // Rubbable has 1 method run()
        Thread w5a = new Thread(() -> {
            for (int i=0; i< count; i++){
                System.out.println("hello");
            }
        });
        Thread w5b = new Thread(() -> {
            for (int i=0; i<count; i++){
                System.out.println("world");
            }
        });
        w5a.start();
        w5b.start();
    }
}