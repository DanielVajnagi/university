package labs.interfaces;

public interface StringSerializable<T extends StringSerializable> {
    // Default method to create an instance from a string
    default T fromString(String data) {
        throw new UnsupportedOperationException("fromString method not implemented");
    }
}
