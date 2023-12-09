package labs;

import java.time.Year;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

/**
 * Represents a generic vehicle.
 */
public class Vehicle {
    protected String brand;
    protected int year;
    protected String color;

    protected List<String> validationErrors=new ArrayList<>();

    protected Vehicle(Builder builder) {
        this.brand = builder.brand;
        this.year = builder.year;
        this.color = builder.color;
        validateFields();
    }

    private void validateFields() {
        List<String> validationErrors=new ArrayList<>();
        validateBrand();
        validateYear();
        validateColor();
        if (!validationErrors.isEmpty()) {
            throw new IllegalArgumentException(String.join(". ", validationErrors));
        }
    }

    private void validateBrand() {
        if (brand == null || brand.isEmpty()) {
            validationErrors.add("Brand must be specified");
        }
    }

    private void validateYear() {
        if (year < 1900) {
            validationErrors.add("Too old to be driven");
        }
        if (year > Year.now().getValue()) {
            validationErrors.add("Cars from the future are not allowed");
        }
    }

    private void validateColor() {
        if (color == null || color.isEmpty()) {
            validationErrors.add("Color must be specified");
        }
    }

    public String getBrand() {
        return brand;
    }

    public int getYear() {
        return year;
    }

    public String getColor() {
        return color;
    }

    public static Vehicle fromString(String data) {
        String[] parts = data.split(",");
        if (parts.length != 3) {
            throw new IllegalArgumentException("Invalid data format");
        }

        String brand = parts[0].trim();
        int year = Integer.parseInt(parts[1].trim().replaceAll(" year", ""));
        String color = parts[2].trim();

        return new Builder(brand, year, color).build();
    }

    public int compareTo(Vehicle other) {
        return Integer.compare(this.year, other.year);
    }

    /**
     * @return A string representation of the object.
     */
    @Override
    public String toString() {
        return "Vehicle: " + brand +
                ", " + year +
                " year, " + color;
    }

    /**
     * Indicates whether some other object is "equal to" this one.
     *
     * @param o The reference object with which to compare.
     * @return {@code true} if this object is the same as the obj argument; {@code false} otherwise.
     */
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Vehicle vehicle = (Vehicle) o;
        return year == vehicle.year && brand.equals(vehicle.brand) && color.equals(vehicle.color);
    }

    /**
     * Returns a hash code value for the object.
     *
     * @return A hash code value for this object.
     */
    @Override
    public int hashCode() {
        return Objects.hash(brand, year, color);
    }

    /**
     * Represents a builder for creating instances of the {@link Vehicle} class.
     */
    public static class Builder {
        protected String brand;
        protected int year;
        protected String color;



        public Builder(String brand, int year, String color) {
            this.brand = brand;
            this.year = year;
            this.color = color;
        }



        public Vehicle build() {
            return new Vehicle(this);
        }
    }
}
