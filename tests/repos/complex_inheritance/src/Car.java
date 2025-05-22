public class Car extends Vehicle {
    private int numDoors;
    
    public Car(String brand, int year, int numDoors) {
        super(brand, year);
        this.numDoors = numDoors;
    }
    
    @Override
    public void start() {
        System.out.println("Starting car");
    }
} 