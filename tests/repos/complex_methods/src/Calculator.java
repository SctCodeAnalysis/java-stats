public class Calculator {
    public int calculate(int a, int b, String operation) {
        if (operation == null) {
            throw new IllegalArgumentException("Operation cannot be null");
        }
        
        switch (operation) {
            case "add":
                return a + b;
            case "subtract":
                return a - b;
            case "multiply":
                return a * b;
            case "divide":
                if (b == 0) {
                    throw new ArithmeticException("Division by zero");
                }
                return a / b;
            default:
                throw new IllegalArgumentException("Unknown operation");
        }
    }
    
    public void processArray(int[] numbers) {
        for (int i = 0; i < numbers.length; i++) {
            while (numbers[i] > 0) {
                if (numbers[i] % 2 == 0) {
                    numbers[i] /= 2;
                } else {
                    numbers[i] = numbers[i] * 3 + 1;
                }
            }
        }
    }
} 