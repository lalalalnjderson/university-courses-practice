public class SynchExample{
    static class UnsafeCounter{
        private int count = 0;
        
        void increment(){
            count++;
        }

        int get(){
            return count;
        }
    }

    static class SynchronizedMethodCounter {
        private int count;
        synchronized void increment(){
            count++;
        }
        synchronized int get(){
            return count;
        }
    }

    static class SynchronizedBlockCounter {
        private final Object lock = new Object();
        private int count =0;
        void increment(){
            synchronized (lock){
                count++;
            }
        }
        int get(){
            synchronized(lock){
                return count;
            }
        }
    }
}