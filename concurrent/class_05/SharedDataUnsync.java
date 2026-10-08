package class_05;
import java.util.ArrayList;
import java.util.List;

public class SharedDataUnsync{
    public static void main(String[] args) throws InterruptedException{
        List<Integer> list = new ArrayList<>();

        Thread t1 = new Thread(() -> {
            for(int i=1; i <= 1_000_000; i += 2){
                list.add(i);
            }
        });

        Thread t2 = new Thread(() -> {
            for (int i=2; i <= 1_000_000; i += 2){
                list.add(i);
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


// possible outputs:
// ArrayIndexOutOfBoundsException — the internal array is being resized
// NullPointerException
// Wrong size (lost elements) because list.add(i) consains several steps  