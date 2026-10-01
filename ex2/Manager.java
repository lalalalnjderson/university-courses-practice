package ex2;
import java.util.ArrayList;
import java.util.List;

public class Manager extends Employee{
    private List<Employee> employees;

    public Manager(String name, double salary){
        super(name, salary);
        employees = new ArrayList<>();
    }

    public void addEmployee(Employee e){
        employees.add(e);
    }

    public void removeEmployee(Employee e){
        employees.remove(e);
    }

    public List<Employee> getEmployees(){
        return employees;
    }

    @Override
    public double getSalary(){
        double total = getBaseSalary();
        for (Employee e : employees){
            total += e.getSalary() * 0.05;
        }
        return total;
    }
}