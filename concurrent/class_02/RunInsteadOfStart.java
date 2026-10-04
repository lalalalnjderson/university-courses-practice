package class_02;

public class RunInsteadOfStart{
    public static void main(String[] args){
        PrintThread t1 = new PrintThread("hello");
        PrintThread t2 = new PrintThread("world");
        t1.run();
        t2.run();
    }
}