package labs;

import labs.Car;
import org.testng.annotations.Test;

import static org.testng.Assert.assertEquals;

public class ValidationsTest {

    @Test
    public void testValidCarBuilder() {
        Car car = new Car.Builder("Toyota", 2022, "Red")
                .setNumberOfDoors(4)
                .build();

        // Все повинно бути в порядку, невалідних значень не повинно бути
    }

    @Test
    public void testInvalidNumberOfDoors() {
        try {
            new Car.Builder("Toyota", 2022, "Red")
                    .setNumberOfDoors(0)
                    .build();
        } catch (IllegalArgumentException e) {
            assertEquals(e.getMessage(), "Number of doors must be more than 0");
        }
    }

    @Test
    public void testInvalidBrand() {
        try {
            new Car.Builder(null, 2022, "Red")
                    .setNumberOfDoors(4)
                    .build();
        } catch (IllegalArgumentException e) {
            assertEquals(e.getMessage(), "Brand must be specified");
        }
    }

    @Test
    public void testInvalidYear() {
        try {
            new Car.Builder("Toyota", 1800, "Red")
                    .setNumberOfDoors(4)
                    .build();
        } catch (IllegalArgumentException e) {
            assertEquals(e.getMessage(), "Too old to be driven");
        }
        try {
            new Car.Builder("Toyota", 2025, "Red")
                    .setNumberOfDoors(4)
                    .build();
        } catch (IllegalArgumentException e) {
            assertEquals(e.getMessage(), "Cars from the future are not allowed");
        }
    }


    @Test
    public void testInvalidColor() {
        try {
            new Car.Builder("Toyota", 2022, "")
                    .setNumberOfDoors(4)
                    .build();
        } catch (IllegalArgumentException e) {
            assertEquals(e.getMessage(), "Color must be specified");
        }
    }

    @Test
    public void testInvalidBrandAndColor() {
        try {
            new Car.Builder("", 2022, "")
                    .setNumberOfDoors(4)
                    .build();
        } catch (IllegalArgumentException e) {
            assertEquals(e.getMessage(), "Brand must be specified. Color must be specified");
        }


    }
}
