package labs.DB;

import labs.Car;
import labs.Driver;

import java.sql.Statement;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.time.LocalDate;

public class InsertDriver {

    public static void main(String[] args) {
        try (Connection connection = DBConnector.getConnection()) {
            // Створення об'єктів Car
            Car car1 = new Car.Builder("Toyota", 2018, "Black").setNumberOfDoors(4).build();
            Car car2 = new Car.Builder("Honda", 2019, "Yellow").setNumberOfDoors(2).build();

            // Додавання даних в таблицю Cars
            insertDataIntoCarsTable(connection, car1);
            insertDataIntoCarsTable(connection, car2);

            // Створення об'єктів Driver
            Driver driver1 = new Driver.Builder("John", LocalDate.of(1990, 5, 15), car1.getCarId()).build();
            Driver driver2 = new Driver.Builder("Alice", LocalDate.of(1992, 6, 1), car2.getCarId()).build();

            // Додавання даних в таблицю Drivers
            insertDataIntoDriversTable(connection, driver1);
            insertDataIntoDriversTable(connection, driver2);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void insertDataIntoCarsTable(Connection connection, Car car) throws SQLException {

        String insertDataSQL = "INSERT INTO Cars (brand, year, color, doors) VALUES (?, ?, ?, ?)";
        try (PreparedStatement preparedStatement = connection.prepareStatement(insertDataSQL, Statement.RETURN_GENERATED_KEYS)) {

            preparedStatement.setString(1, car.getBrand());
            preparedStatement.setInt(2, car.getYear());
            preparedStatement.setString(3, car.getColor());
            preparedStatement.setInt(4, car.getNumberOfDoors());

            preparedStatement.executeUpdate();

            int carId;
            try (ResultSet generatedKeys = preparedStatement.getGeneratedKeys()) {
                if (generatedKeys.next()) {
                    carId = generatedKeys.getInt(1);
                    car.setCarId(carId);
                } else {
                    throw new SQLException("Failed to get the generated car_id.");
                }
            }

            System.out.println("Data inserted into Cars table successfully. Car ID: " + carId);
        }
    }

    private static void insertDataIntoDriversTable(Connection connection, Driver driver) throws SQLException {
        String insertDataSQL = "INSERT INTO Drivers (name, date_of_birth, car_id) VALUES (?, ?, ?)";
        try (PreparedStatement preparedStatement = connection.prepareStatement(insertDataSQL)) {
            preparedStatement.setString(1, driver.getName());
            preparedStatement.setDate(2, java.sql.Date.valueOf(driver.getDateOfBirth()));
            preparedStatement.setInt(3, driver.getCarID());
            preparedStatement.executeUpdate();

            System.out.println("Data inserted into Drivers table successfully.");
        }
    }
}

