package labs.serializers;

import com.google.gson.*;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.Writer;
import java.lang.reflect.Type;
import java.util.ArrayList;
import java.util.List;
import labs.interfaces.EntitySerializer;


public class JsonSerializer<T> implements EntitySerializer<T> {

    private final Gson gson;
    private final Type typeOfT;

    public JsonSerializer(Type typeOfT) {
        this.gson = new GsonBuilder().setPrettyPrinting().create();
        this.typeOfT = typeOfT;
    }

    @Override
    public String serialize(T object) {
        return gson.toJson(object);
    }

    @Override
    public T deserialize(String json) {
        return gson.fromJson(json, typeOfT);
    }

    @Override
    public void writeToFile(List<T> objects, String filePath) throws IOException {
        try (Writer writer = new FileWriter(filePath)) {
            String json = gson.toJson(objects);
            writer.write(json);
        }
    }

    @Override
    public List<T> readFromFile(String filePath) throws IOException {
        try (FileReader reader = new FileReader(filePath)) {
            JsonArray jsonArray = JsonParser.parseReader(reader).getAsJsonArray();
            List<T> list = new ArrayList<>();
            for (JsonElement element : jsonArray) {
                T obj = gson.fromJson(element, typeOfT);
                list.add(obj);
            }
            return list;
        }
    }
}