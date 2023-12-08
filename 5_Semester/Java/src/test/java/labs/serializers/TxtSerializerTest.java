package labs.serializers;

import labs.Vehicle;
import org.testng.Assert;
import org.testng.annotations.BeforeClass;
import org.testng.annotations.Test;

import java.io.*;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class TxtSerializerTest {

    private TxtSerializer<Vehicle> format;
    private String testFilePath = "test_vehicles.txt";



    @Test
    public void testWriteToFileAndReadFromFile() throws IOException {
        // Створення об'єктів для тесту
        Vehicle vehicle1 = new Vehicle.Builder("Toyota",2022,"Red").build();
        Vehicle vehicle2 = new Vehicle.Builder("Honda",2023,"Blue").build();

        // Запис об'єктів у файл
        List<Vehicle> vehicles = Arrays.asList(vehicle1, vehicle2);
        try (Writer writer = new FileWriter(testFilePath)) {
            for (Vehicle vehicle : vehicles) {
                writer.write(vehicle.toString());
                writer.write(System.lineSeparator()); // Додаємо перенос рядка
            }
        }

        // Читання об'єктів з файлу
        List<Vehicle> readVehicles = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(testFilePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                // Додавання об'єкта до списку
                readVehicles.add(Vehicle.fromString(line));
            }
        }


        // Перевірка результатів
        Assert.assertNotNull(readVehicles);
        Assert.assertEquals(readVehicles.size(), 2);
        Assert.assertTrue(readVehicles.get(0).toString().contains("Toyota"));
        Assert.assertTrue(readVehicles.get(1).toString().contains("Honda"));
    }
}
