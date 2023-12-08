package labs;

import java.time.LocalDate;
import java.util.Objects;

public class Driver {
    private final String name;
    private final LocalDate dateOfBirth;
    private final int carID;

    private Driver(Builder builder) {
        this.name = builder.name;
        this.dateOfBirth = builder.dateOfBirth;
        this.carID = builder.carID;
    }

    public String getName() {
        return name;
    }
    public LocalDate getDateOfBirth() {
        return dateOfBirth;
    }

    public int getCarID() {
        return carID;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Driver driver = (Driver) o;
        return Objects.equals(name, driver.name) &&
                Objects.equals(dateOfBirth, driver.dateOfBirth) &&
                Objects.equals(carID, driver.carID);
    }

    @Override
    public int hashCode() {
        return Objects.hash(name, dateOfBirth, carID);
    }

    @Override
    public String toString() {
        return "Driver{" +
                "name='" + name + '\'' +
                ", dateOfBirth=" + dateOfBirth +
                ", carID=" + carID +
                '}';
    }

    public static class Builder {
        private String name;
        private LocalDate dateOfBirth;
        private int carID;

        public Builder(String name, LocalDate dateOfBirth, int carID) {
            this.name = name;
            this.dateOfBirth = dateOfBirth;
            this.carID = carID;
        }

        public Builder setName(String name) {
            this.name = name;
            return this;
        }

        public Builder setDateOfBirth(LocalDate dateOfBirth) {
            this.dateOfBirth = dateOfBirth;
            return this;
        }

        public Builder setCarID(int carID) {
            this.carID = carID;
            return this;
        }


        public Driver build() {
            return new Driver(this);
        }
    }
}
