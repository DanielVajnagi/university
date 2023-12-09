package labs.serializers;

import labs.interfaces.EntitySerializer;

import java.io.*;
import java.util.ArrayList;
import java.util.List;
import java.util.function.Function;

public class TxtSerializer<T> implements EntitySerializer<T> {

    private Function<String, T> deserializer;

    public TxtSerializer(Function<String, T> deserializer) {
        this.deserializer = deserializer;
    }

    @Override
    public String serialize(T object) {
        return object.toString();
    }

    @Override
    public T deserialize(String data) {
        return deserializer.apply(data);
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
                objects.add(deserializer.apply(line));
            }
        }
        return objects;
    }
}