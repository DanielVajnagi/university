package labs.serializers;

import labs.Car;
import org.testng.Assert;
import org.testng.annotations.BeforeMethod;
import org.testng.annotations.Test;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.List;

public class TxtSerializerTest {

    private TxtSerializer<Car> format;


    @BeforeMethod
    public void setUp() {
        format = new TxtSerializer<>(Car.class);
    }

    @Test
    public void testSerializeAndDeserialize() {
        Car car = new Car.Builder("Bentley", 2022, "Space Blue").setNumberOfDoors(2).build();
        String serialized = format.serialize(car);

        Assert.assertNotNull(serialized);
        Assert.assertFalse(serialized.isEmpty());

        Car deserialized = format.deserialize(serialized);
        Assert.assertNotNull(deserialized);
        Assert.assertEquals(deserialized.getBrand(), "Bentley");
        Assert.assertEquals(deserialized.getYear(), 2022);
    }



    @Test
    public void testWriteToFileAndReadFromFile() throws IOException {
        List<Car> cars = Arrays.asList(
                new Car.Builder("Toyota", 2017, "White").setNumberOfDoors(4).build(),
                new Car.Builder("Nissan", 2013, "Gray").setNumberOfDoors(2).build(),
                new Car.Builder("Mitsubishi", 1996, "Red").setNumberOfDoors(2).build()
        );
        String testFilePath = "cars.txt";
        format.writeToFile(cars, testFilePath);

        Assert.assertTrue(Files.exists(Paths.get(testFilePath)));

        List<Car> readCars = format.readFromFile(testFilePath);

        Assert.assertNotNull(readCars);
        Assert.assertEquals(readCars.size(), 3);
        Assert.assertEquals(readCars.get(0).getBrand(), "Toyota");
        Assert.assertEquals(readCars.get(1).getColor(), "Gray");
    }
}



