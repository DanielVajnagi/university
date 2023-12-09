package labs.DB;

import labs.Car;

import java.sql.*;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class InsertData {


    public static void main(String[] args) {
        try (Connection connection = DBConnector.getConnection()) {
            // Створення об'єктів Car
            Car car1 = new Car.Builder("Toyota", 2022, "Red").setNumberOfDoors(4).build();
            Car car2 = new Car.Builder("Honda", 2023, "Blue").setNumberOfDoors(2).build();

            // Додавання даних в таблицю Cars
            insertDataIntoCarsTable(connection, car1);
            insertDataIntoCarsTable(connection, car2);
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void insertDataIntoCarsTable(Connection connection, Car car) throws SQLException {
        // SQL-запит для вставки даних в таблицю Cars
        String insertDataSQL = "INSERT INTO Cars (brand, year, color, doors) VALUES (?, ?, ?, ?)";
        try (PreparedStatement preparedStatement = connection.prepareStatement(insertDataSQL, Statement.RETURN_GENERATED_KEYS)) {
            // Встановлення значень параметрів SQL-запиту з об'єкта Car
            preparedStatement.setString(1, car.getBrand());
            preparedStatement.setInt(2, car.getYear());
            preparedStatement.setString(3, car.getColor());
            preparedStatement.setInt(4, car.getNumberOfDoors());

            // Виконання SQL-запиту
            preparedStatement.executeUpdate();

            // Отримання згенерованого car_id
            int carId;
            try (ResultSet generatedKeys = preparedStatement.getGeneratedKeys()) {
                if (generatedKeys.next()) {
                    carId = generatedKeys.getInt(1);
                } else {
                    throw new SQLException("Failed to get the generated car_id.");
                }
            }

            System.out.println("Data inserted into Cars table successfully. Car ID: " + carId);
        }
    }
}

