package class_03;

public class SpeedupTest{
    static long totalSum = 0;

    // static variable for shared sum is NOT thread-safe
    public static void main(String[] args){
        long n = 1_000_000_000L; // L = long literal, treat this number as long
        long startTime = System.nanoTime(); // nanoTime = high-precision clock
        long singleSum = 0;
        for (long i=1; i<=n; i++){
            singleSum += 1;
        }
        long singleTime = System.nanoTime() - startTime;
        System.out.println("Single thread sum: " + singleSum);
        System.out.println("Single thread time: " + singleTime / 1_000_000 + "ms");

        int threadCount = 10;
        long chunkSize = n / threadCount;
        Thread[] threads = new Thread[threadCount]; 

        totalSum = 0;
        startTime = System.nanoTime();

        for (int t=0; t<threadCount; t++){
            long from = t * chunkSize + 1;
            long to = (t + 1) * chunkSize;
            if (t == threadCount - 1){
                to = n;
            }
            
        }
    }
}