package labs.serializers;


import labs.Vehicle;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.io.File;
import java.io.IOException;
import java.util.List;

public class XmlSerializerTest {

    @Test
    public void testXmlSerializationDeserialization() {
        // Створення серіалізатора для класу Vehicle
        XmlSerializer<Vehicle> vehicleXmlSerializer = new XmlSerializer<>(Vehicle.class);

        // Створення об'єкта Vehicle
        Vehicle myVehicle = new Vehicle.Builder("Toyota",2020,"yellow").build();

        // Серіалізація в XML та запис у файл
        File outputFile = new File("vehicle.xml");
        try {
            vehicleXmlSerializer.writeToFile(List.of(myVehicle), outputFile.getPath());
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Десеріалізація з файлу XML
        try {
            List<Vehicle> deserializedVehicles = vehicleXmlSerializer.readFromFile(outputFile.getPath());
            Assert.assertEquals(deserializedVehicles.size(), 1);
            Vehicle deserializedVehicle = deserializedVehicles.get(0);
            Assert.assertEquals(deserializedVehicle, myVehicle);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
