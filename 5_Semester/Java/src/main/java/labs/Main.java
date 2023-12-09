package labs;


import labs.DB.DBConnector;

import java.sql.*;

public class Main {
    public static void main(String[] args) {
        String testFilePath = "test_vehicles.txt";

        Vehicle myVehicle = new Vehicle.Builder("Toyota", 2022, "Blue").build();
        System.out.println(myVehicle);

/*
        try (Connection connection = DBConnector.getConnection()) {
            String selectQuery = "SELECT * FROM rental.cars";

            try (PreparedStatement preparedStatement = connection.prepareStatement(selectQuery);
                 ResultSet resultSet = preparedStatement.executeQuery()) {

                while (resultSet.next()) {
                    int id = resultSet.getInt("car_id");
                    String brand = resultSet.getString("brand");
                    int year = resultSet.getInt("year");
                    String color = resultSet.getString("color");
                    int numberOfDoors = resultSet.getInt("doors");

                    System.out.println("ID: " + id + ", Brand: " + brand + ", Year: " + year +
                            ", Color: " + color + ", Doors: " + numberOfDoors);
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
*/
    }
}
