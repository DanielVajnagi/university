package labs;

import java.time.LocalDate;
import java.util.Objects;

public class Driver {
    private final String name;
    private final LocalDate dateOfBirth;
    private final Car car;

    private Driver(Builder builder) {
        this.name = builder.name;
        this.dateOfBirth = builder.dateOfBirth;
        this.car = builder.car;
    }

    public String getName() {
        return name;
    }
    public LocalDate getDateOfBirth() {
        return dateOfBirth;
    }

    public Car getCar() {
        return car;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Driver driver = (Driver) o;
        return Objects.equals(name, driver.name) &&
                Objects.equals(dateOfBirth, driver.dateOfBirth);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, dateOfBirth, car);
    }

    @Override
    public String toString() {
        return "Driver{" +
                "name='" + name + '\'' +
                ", dateOfBirth=" + dateOfBirth +
                ", Car=" + car.toString() +
                '}';
    }

    public static class Builder {
        private String name;
        private LocalDate dateOfBirth;
        private Car car;

        public Builder(String name, LocalDate dateOfBirth, Car car) {
            this.name = name;
            this.dateOfBirth = dateOfBirth;
            this.car = car;
        }

        public Builder setName(String name) {
            this.name = name;
            return this;
        }

        public Builder setDateOfBirth(LocalDate dateOfBirth) {
            this.dateOfBirth = dateOfBirth;
            return this;
        }

        public Builder setCar(Car car) {
            this.car = car;
            return this;
        }


        public Driver build() {
            return new Driver(this);
        }
    }
}
