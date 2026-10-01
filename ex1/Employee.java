package ex1;

public class Employee{
    private String name;
    private double salary;
    
    public Employee(String name, double salary){
        this.name = name;
        this.salary = salary;
    }

    public String getName(){
        return name;
    }

    public double getSalary(){
        return salary;
    }

    public void raiseSalary(double percent){
        salary += salary * percent / 100.0;
    }

    public static void main(String[] args){
        Employee emp = new Employee("Alice", 50000);
        System.out.println(emp.getName() + "earns" + emp.getSalary());
        emp.raiseSalary(10);
        System.out.println(emp.getSalary());
    }
}