package ex2;

public class Main{
    public static void main(String[] args){
        Subordinate alice = new Subordinate("Alice", 5000);
        Subordinate bob = new Subordinate("Bob", 60000);
        Manager carol = new Manager("Carol", 80000);

        carol.addEmployee(alice);
        carol.addEmployee(bob);

        System.out.println(alice.getName() + " earns " + alice.getSalary());
        System.out.println(bob.getName() + " earns " + bob.getSalary());
        System.out.println(carol.getName() + " earns " + carol.getSalary());

        carol.removeEmployee(bob);
        System.out.println("After removing Bob: " + carol.getName() + " earns " + carol.getSalary());
        alice.raiseSalary(5);
        System.out.println("Alice after 10% raise: " + alice.getSalary());
        System.out.println("Carol after Alice's raise: " + carol.getSalary());
    }
}