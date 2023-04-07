package com.example;

import java.util.List;
import java.util.ArrayList;

/**
 * This is an example class that includes every possible syntax construct in
 * Java.
 */
public class ExampleComplex {
    // Fields
    private int num;
    private String name;

    // Constructor
    public ExampleComplex(int num, String name) {
        this.num = num;
        this.name = name;
    }

    // Getters and setters
    public int getNum() {
        return num;
    }

    public void setNum(int num) {
        this.num = num;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    // Methods
    public static void main(String[] args) {
        System.out.println("Hello, world!");
    }

    public int add(int a, int b) {
        return a + b;
    }

    public void printInfo() {
        System.out.println("Num: " + num);
        System.out.println("Name: " + name);
    }

    // Inner class
    public class InnerClass {
        private String message;

        public InnerClass(String message) {
            this.message = message;
        }

        public String getMessage() {
            return message;
        }

        public void setMessage(String message) {
            this.message = message;
        }
    }

    // Enumeration
    public enum ExampleEnum {
        VALUE1,
        VALUE2,
        VALUE3
    }

    // Static initialization block
    static {
        System.out.println("Static initialization block");
    }

    // Instance initialization block
    {
        System.out.println("Instance initialization block");
    }

    /* Throws smth */
    @Override
    protected void finalize() throws Throwable {
        super.finalize();
        System.out.println("Finalizer");
    }

    // Annotation
    @SuppressWarnings("unused")
    public void unusedMethod() {
        System.out.println("This method is unused");
    }

    // Generic method
    public <T> T genericMethod(T param) {
        return param;
    }

    // Varargs method
    public int sum(int... nums) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }
        return total;
    }

    // Native method
    public native void nativeMethod();

    // Synchronized method
    public synchronized void synchronizedMethod() {
        System.out.println("Synchronized method");
    }

    // Abstract method
    public abstract void abstractMethod();

    // Final method
    public final void finalMethod() {
        System.out.println("Final method");
    }

    // Static method
    public static void staticMethod() {
        System.out.println("Static method");
    }

    // Interface
    public interface ExampleInterface {
        void exampleMethod();
    }

    // Nested interface
    public interface NestedInterface {
        void nestedMethod();
    }

    // Lambda expression
    public void processList(List<String> list) {
        list.forEach(item -> System.out.println(item));
    }

    // Diamond operator
    public List<String> createList() {
        return new ArrayList<>();
    }

    // Try-with-resources statement
    public void writeToFile(String text) {
        try (FileWriter writer = new FileWriter("output.txt")) {
            writer.write(text);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    // Switch statement
    public void handleEnum(ExampleEnum exampleEnum) {
        switch (exampleEnum) {
            case VALUE1:
                System.out.println("Value is VALUE1");
                break;
            case VALUE2:
                System.out.println("Value is VALUE2");
                break;
            case VALUE3:
                System.out.println("Value is VALUE3");
                break;
            default:
                System.out.println("Invalid value");
        }
    }

    // Enhanced for loop
    public void printList(List<String> list) {
        for (String item : list) {
            System.out.println(item);
        }
    }

    // Multi-catch exception handling
    // Code stops here
    public void handleExceptions() {
        try {
            // Some code that might throw an exception
        } catch (NullPointerException | IllegalArgumentException | ArithmeticException e) {
            e.printStackTrace();
        }
    }

    // Type inference with local variables
    public void printMessage() {
        var message = "Hello, world!";
        System.out.println(message);
    }

    // Optional parameter in method declaration
    public void optionalParameter(int a, int b, int... c) {
        int total = a + b;
        for (int num : c) {
            total += num;
        }
        System.out.println("Total: " + total);
    }
}