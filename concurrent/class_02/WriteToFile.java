package class_02;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

class FileThread extends Thread{
    private String message;
    private String filename;

    FileThread(String message, String filename){
        this.message = message;
        this.filename = filename;
    }

    @Override
    public void run(){
        try(PrintWriter pw = new PrintWriter(new FileWriter(filename))){
            for (int i=0; i < 10_000; i++){
                pw.println(message);
            }
        } 
        catch(IOException e){
            e.printStackTrace();
        }
    }
}

public class WriteToFile{
    public static void main(String[] args){
        FileThread t1 = new FileThread("hello", "hello.txt");
        FileThread t2 = new FileThread("world", "world.txt");
        t1.start();
        t2.start();
    }
}