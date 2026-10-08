package class_05;
import java.util.ArrayList;
import java.util.List;

public class SharedDataOrdered{
    public static void main(String[] args) throws InterruptedException {
        List<Integer> list = new ArrayList<>();
        // plain int would need to be "effectively final"
        final int[] nextExpected = {1};

        Thread t1 = new Thread(() -> {
            for (int i=1; i <= 1_000_000; i += 2){
                synchronized(list){
                    while (nextExpected[0] != i){
                        try {
                            list.wait(); // release lock, sleep until notified
                        }
                        catch (InterruptedException e){
                            Thread.currentThread().interrupt();
                            return;
                        }
                    }
                    list.add(i);
                    nextExpected[0]++;
                    list.notify(); // wake the other thread
                }
            }
        });
        Thread t2 = new Thread(() -> {
            for (int i=2; i <= 1_000_000; i += 2){
                synchronized(list){
                    while(nextExpected[0] != i){
                        try{
                            list.wait();
                        }
                        catch (InterruptedException e){
                            Thread.currentThread().interrupt();
                            return;
                        }
                    }
                    list.add(i);
                    nextExpected[0]++;
                    list.notify();
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