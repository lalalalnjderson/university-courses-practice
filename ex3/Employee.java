package ex3;

public abstract class Employee implements SalariedEntity{
    private String name;
    private double salary;

    public Employee(String name, double salary){
        this.name = name;
        this.salary = salary;
    }

    public String getName(){
        return name;
    }

    protected double getBaseSalary(){
        return salary;
    }

    public void raiseSalary(double percent){
        salary += salary * percent / 100.0;
    }
}