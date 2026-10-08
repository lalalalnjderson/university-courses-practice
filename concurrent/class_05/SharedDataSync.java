package class_05;
import java.util.ArrayList;
import java.util.List;

// still unordered
// size is correct
// SLOWER: threads take turns instead of running simultaneously

public class SharedDataSync{
    public static void main(String[] args) throws InterruptedException{
        List<Integer> list = new ArrayList<>();

        Thread t1 = new Thread(() -> {
            for (int i=1; i<1_000_000; i += 2){
                synchronized(list){ // lock object = only 1 thread can be inside this block
                    list.add(i);
                }
            }
        });
        Thread t2 = new Thread(() -> {
            for (int i=0; i<1_000_000; i += 2){
                synchronized(list){ 
                    list.add(i);
                }
            }
        });

        t1.start();
        t2.start();
        t1.join();
        t2.join();

        System.out.println("Actual size: " + list.size());

        int inversions = 0;
        for (int i=1; i<list.size(); i++){
            if (list.get(i) < list.get(i-1)){
                inversions++;
            }
        }
        System.out.println("Inversions: " + inversions);

        int showSize = Math.min(20, list.size());
        System.out.println(list.subList(0, showSize));
    }
}