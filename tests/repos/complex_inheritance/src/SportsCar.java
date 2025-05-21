public class SportsCar extends Car {
    private int maxSpeed;
    
    public SportsCar(String brand, int year, int numDoors, int maxSpeed) {
        super(brand, year, numDoors);
        this.maxSpeed = maxSpeed;
    }
    
    @Override
    public void start() {
        System.out.println("Starting sports car");
    }
} 