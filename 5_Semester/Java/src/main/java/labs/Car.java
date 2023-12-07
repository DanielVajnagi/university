package labs;


import java.util.Objects;

/**
 * Represents a car, which is a type of vehicle.
 */
public class Car extends Vehicle {
    private final int numberOfDoors;

    public Car(Builder builder) {
        super(builder);
        this.numberOfDoors = builder.numberOfDoors;
    }


    public int getNumberOfDoors() {
        return numberOfDoors;
    }
    @Override
    public String toString() {
        return "Car{" +
                "brand='" + brand + '\'' +
                ", year=" + year +
                ", color='" + color + '\'' +
                ", numberOfDoors=" + numberOfDoors +
                '}';
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

    /**
     * Represents a builder for creating instances of the {@link Car} class.
     */
    public static class Builder extends Vehicle.Builder {
        private int numberOfDoors;

        public Builder(String brand,int year,String color) {
            super(brand,year,color);
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