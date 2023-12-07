package labs.interfaces;


import java.io.IOException;
import java.util.List;

public interface EntitySerializer<T> {

    /**
     * Serialize an object to a string in the corresponding format.
     *
     * @param object the object to serialize
     * @return string representation of the object in the format
     * @throws IOException if an input/output error occurs
     */
    String serialize(T object) throws IOException;

    /**
     * Deserialize an object from a string in the corresponding format.
     *
     * @param data the string representation of the object in the format
     * @return the object created from the string
     * @throws IOException if an input/output error occurs
     */
    T deserialize(String data) throws IOException;

    /**
     * Write a list of objects to a file in the corresponding format.
     *
     * @param objects list of objects to write
     * @param filePath path to the file for writing
     * @throws IOException if an input/output error occurs
     */
    void writeToFile(List<T> objects, String filePath) throws IOException;

    /**
     * Read a list of objects from a file in the corresponding format.
     *
     * @param filePath path to the file for reading
     * @return list of objects read from the file
     * @throws IOException if an input/output error occurs
     */
    List<T> readFromFile(String filePath) throws IOException;
}
