package labs;

import labs.interfaces.StringSerializable;

import java.lang.reflect.Type;
import java.util.Objects;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Represents a car, which is a type of vehicle.
 */
public class Car extends Vehicle {
    private int numberOfDoors;

    private int carID;

    public int getCarId() {
        return carID;
    }

    public void setCarId(int carID) {
        this.carID = carID;
    }

    public Car(Builder builder) {
        super(builder);
        this.numberOfDoors = builder.numberOfDoors;
        validateNumberOfDoors(numberOfDoors);
    }
    public Car() {
    }
    private void validateNumberOfDoors(int numberOfDoors) {
        if (numberOfDoors < 1) {
            throw new IllegalArgumentException("Number of doors must be more than 0");
        }
    }

    public int getNumberOfDoors() {
        return numberOfDoors;
    }

    @Override
    public String toString() {
        return "Car: " + brand + ", " + year +
                " year, " + color +
                ", with " + numberOfDoors +
                " doors";
    }

    @Override
    public Car fromString(String data) {
        String patternString = "Car: (.*), (\\d+) year, (.*), with (\\d+) doors";

        Pattern pattern = Pattern.compile(patternString);
        Matcher matcher = pattern.matcher(data);

        if (matcher.matches()) {
            String brand = matcher.group(1);
            int year = Integer.parseInt(matcher.group(2));
            String color = matcher.group(3);
            int numberOfDoors = Integer.parseInt(matcher.group(4));
            return new Builder(brand, year, color).setNumberOfDoors(numberOfDoors).build();
        } else {
            throw new IllegalArgumentException("Pattern does not match the input string");
        }
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        if (!super.equals(o)) return false;
        Car car = (Car) o;
        return numberOfDoors == car.numberOfDoors;
    }

    @Override
    public int hashCode() {
        return Objects.hash(super.hashCode(), numberOfDoors);
    }

    public static class Builder extends Vehicle.Builder {
        private int numberOfDoors;

        public Builder(String brand, int year, String color) {
            super(brand, year, color);
        }

        /**
         * Sets the number of doors for the car.
         *
         * @param numberOfDoors The number of doors to set.
         * @return The {@link Builder} instance for method chaining.
         */
        public Builder setNumberOfDoors(int numberOfDoors) {
            this.numberOfDoors = numberOfDoors;
            return this;
        }

        public Car build() {
            return new Car(this);
        }
    }
}
