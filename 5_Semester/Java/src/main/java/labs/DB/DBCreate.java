package labs.DB;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

public class DBCreate {

    public static void main(String[] args) {
        try (Connection connection = DBConnector.getConnection()) {
            //createCarsTable(connection);
            createDriversTable(connection);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void createCarsTable(Connection connection) throws SQLException {
        try (Statement statement = connection.createStatement()) {
            String createTableSQL = "CREATE TABLE Cars (" +
                    "car_id INT AUTO_INCREMENT PRIMARY KEY," +
                    "brand VARCHAR(255)," +
                    "year INT," +
                    "color VARCHAR(255)," +
                    "doors INT" +
                    ")";
            statement.executeUpdate(createTableSQL);
            System.out.println("Cars table created successfully");
        }
    }

    private static void createDriversTable(Connection connection) throws SQLException {
        try (Statement statement = connection.createStatement()) {
            String createTableSQL = "CREATE TABLE Drivers (" +
                    "driver_id INT AUTO_INCREMENT PRIMARY KEY," +
                    "name VARCHAR(255)," +
                    "date_of_birth DATE," +
                    "car_id INT," +
                    "FOREIGN KEY (car_id) REFERENCES Cars(car_id)" +
                    ")";
            statement.executeUpdate(createTableSQL);
            System.out.println("Drivers table created successfully");
        }
    }
}
