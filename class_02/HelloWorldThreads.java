package class_02;

class PrintThread extends Thread{
    private String message;

    PrintThread(String message){
        this.message = message;
    }

    @Override
    public void run(){
        for (int i=0; i<10_000; i++){
            System.out.println(message);
        }
    }
}

// start: OS creates thread and puts into queue
// then OS scheduler decides which one will be printed first

public class HelloWorldThreads{
    public static void main(String[] args){
        PrintThread t1 = new PrintThread("hello");
        PrintThread t2 = new PrintThread("world");
        t1.start();
        t2.start();
    }
}


// 1) freely interleaved: hello hello world hello world...
// 2) one finishes, then the other
// 3) big chucks 

// single-core CPU (concurrent): rapidly switches between
// 2 threads: hello world hello...

// multi-core CPU (parallel): runs 2 threads simultaneosly 