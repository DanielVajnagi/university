package labs.serializers;

import com.fasterxml.jackson.dataformat.xml.XmlMapper;
import labs.Car;
import labs.Vehicle;
import labs.interfaces.EntitySerializer;
import labs.interfaces.StringSerializable;

import java.io.*;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;

import static labs.Car.fromString;

public class TxtSerializer<T extends StringSerializable>  implements EntitySerializer<T> {

    private final Type typeOfT;
    public static void main(String[] args) throws IOException {
        TxtSerializer<Car> CarTxtSerializer = new TxtSerializer<>(Car.class);

        String testFilePath = "cars.txt";
        System.out.println(CarTxtSerializer.readFromFile(testFilePath));


    }

    public TxtSerializer(Class<T> typeOfT) {
        this.typeOfT = typeOfT;
    }
    @Override
    public String serialize(T object) {
        return object.toString();
    }
    @Override
    public T deserialize(String data) {
        return typeOfT.fromString(data);
    }
    @Override
    public void writeToFile(List<T> objects, String filePath) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {
            for (T obj : objects) {
                writer.write(obj.toString());
                writer.newLine();
            }
        }
    }

    @Override
    public List<T> readFromFile(String filePath) throws IOException {
        File file = new File(filePath);
        if (!file.exists()) {
            throw new IOException("File not found: " + filePath);
        }

        List<T> objects = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line = reader.readLine()) != null) {
                objects.add(typeOfT.fromString(line));
            }
        }
        return objects;
    }
}