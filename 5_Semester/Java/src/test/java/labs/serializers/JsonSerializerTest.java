package labs.serializers;

import labs.Vehicle;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.io.File;
import java.io.IOException;
import java.util.List;

public class JsonSerializerTest {

    @Test
    public void testJsonSerializationDeserialization() {
        // Створення серіалізатора для класу Vehicle
        JsonSerializer<Vehicle> vehicleJsonSerializer = new JsonSerializer<>(Vehicle.class);

        // Створення об'єкта Vehicle
        Vehicle myVehicle = new Vehicle.Builder("Toyota",2020,"yellow").build();

        // Серіалізація в JSON та запис у файл
        File outputFile = new File("vehicle.json");
        try {
            vehicleJsonSerializer.writeToFile(List.of(myVehicle), outputFile.getPath());
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Десеріалізація з файлу JSON
        try {
            List<Vehicle> deserializedVehicles = vehicleJsonSerializer.readFromFile(outputFile.getPath());
            Assert.assertEquals(deserializedVehicles.size(), 1);
            Vehicle deserializedVehicle = deserializedVehicles.get(0);
            Assert.assertEquals(deserializedVehicle, myVehicle);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
