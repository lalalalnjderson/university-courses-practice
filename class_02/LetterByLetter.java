package class_02;

class LetterThread extends Thread{
    private String message;

    LetterThread(String message){
        this.message = message;
    }

    @Override
    public void run(){
        for (int i=0; i<10_000; i++){
            for (char c : message.toCharArray()){
                System.out.print(c);
            }
        }
        System.out.print(" ");
    }
}

public class LetterByLetter{
    public static void main(String[] args){
        LetterThread t1 = new LetterThread("hello");
        LetterThread t2 = new LetterThread("world");
        t1.start();
        t2.start();
    }
}